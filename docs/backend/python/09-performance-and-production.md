---
sidebar_label: "Performance and Production"
description: "Profiling, memory leaks, caching, scaling workers, structured logging, Docker images, observability and choosing Python vs Node for a service."
---

# Python Performance and Production (Q93-Q100)

> **Reviewed:** 2026-09 · **Level:** Senior · **Type:** Foundational

## Q93. Profiling with cProfile and py-spy

Measure before optimising. `cProfile` (built in) records deterministic per-function call counts and cumulative time, great for a script or a single slow code path in development. `py-spy` is a sampling profiler that attaches to a running process by PID without code changes and with low overhead, producing flame graphs or a live `top` view, which makes it suitable for diagnosing production workers. For async apps, also look at APM traces to separate waiting on I/O from CPU time.

- **Trade-offs**:
  - cProfile is precise but adds significant overhead and distorts very hot small functions; sampling profilers are low-overhead but statistical.
  - Attaching py-spy in containers may require extra ptrace capabilities.

**Example:**

```python
import cProfile, pstats

def build_report() -> None: ...

with cProfile.Profile() as prof:
    build_report()
pstats.Stats(prof).sort_stats("cumulative").print_stats(15)

# CLI alternatives:
# python -m cProfile -o out.prof app/script.py
# py-spy top --pid 12345                     # live view of a running worker
# py-spy record -o flame.svg --pid 12345     # flame graph
# py-spy dump --pid 12345                    # stack traces of a stuck process
```

**Remember:** cProfile in dev, py-spy against live processes; find the hot path before changing code.

## Q94. Finding and fixing memory leaks

In Python, "leaks" are usually references that live too long: unbounded module-level caches or lists, `lru_cache` on methods holding `self`, growing global registries, reference cycles through objects with finalizers, or C-extension leaks. Use `tracemalloc` snapshots to compare allocations over time, `gc.get_objects()`/`objgraph` for object counts, and watch RSS per worker in metrics. As a mitigation, gunicorn's `max_requests` recycles workers, but it hides the bug rather than fixing it.

- **Trade-offs**:
  - Bounded caches and weak references fix most leaks but may reduce hit rates; worker recycling is a cheap safety net with slight latency cost on restarts.
  - RSS may not shrink after freeing memory because of allocator fragmentation; that is not necessarily a leak.

**Example:**

```python
import tracemalloc

tracemalloc.start()
snap1 = tracemalloc.take_snapshot()

for _ in range(1000):
    handle_request()                         # suspected leaking path

snap2 = tracemalloc.take_snapshot()
for stat in snap2.compare_to(snap1, "lineno")[:10]:
    print(stat)                              # top growing allocation sites

# Common culprit and fix
_seen: dict[str, dict] = {}                  # grows forever
from functools import lru_cache
@lru_cache(maxsize=10_000)                   # bounded instead
def lookup(key: str) -> dict: ...

def handle_request() -> None: ...
```

**Remember:** Leaks are lingering references; compare tracemalloc snapshots and bound every cache.

## Q95. Caching with functools and Redis

`functools.lru_cache` (bounded) and `functools.cache` (unbounded) memoise pure functions in-process, ideal for expensive computations and config lookups. They are per process, so each gunicorn worker has its own copy and there is no cross-worker invalidation. For shared caching across workers and instances, use Redis with TTLs and a strategy such as cache-aside, and protect hot keys from stampedes with locks or jittered TTLs.

- **Trade-offs**:
  - In-process caches are fastest but duplicated and stale across workers; Redis is shared and invalidatable but adds a network hop and a dependency.
  - `lru_cache` requires hashable arguments and does not support TTL; it does not cache awaited results of async functions correctly (it would cache the coroutine object).

**Example:**

```python
import json, random
from functools import lru_cache
from redis.asyncio import Redis

@lru_cache(maxsize=1024)
def tax_rate(country: str) -> float:          # pure, in-process
    return {"IN": 0.18, "DE": 0.19}.get(country, 0.0)

redis = Redis.from_url("redis://redis:6379/0")

async def cached_profile(user_id: int) -> dict:
    key = f"profile:{user_id}"
    if raw := await redis.get(key):
        return json.loads(raw)
    profile = await fetch_profile_from_db(user_id)
    ttl = 300 + random.randint(0, 60)         # jitter avoids synchronized expiry
    await redis.set(key, json.dumps(profile), ex=ttl)
    return profile

async def invalidate_profile(user_id: int) -> None:
    await redis.delete(f"profile:{user_id}")  # call after writes

async def fetch_profile_from_db(user_id: int) -> dict: ...
```

**Remember:** lru_cache for pure per-process work, Redis for shared caches with TTL and invalidation.

## Q96. Scaling Python workers

Python services scale horizontally with processes: multiple workers per container or one worker per container with more replicas. For I/O-bound async apps, a few uvicorn workers per core can handle many concurrent requests; for sync WSGI apps, concurrency equals workers times threads, so slow requests need more of them. Move CPU-heavy or slow work out of the request path to Celery workers that scale independently, and size everything against downstream limits like DB connections.

- **Trade-offs**:
  - More workers raise throughput but multiply memory and connection usage; autoscaling on CPU alone misleads for I/O-bound services, so also scale on latency, queue depth or in-flight requests.
  - Preloading the app (`--preload`) saves memory via copy-on-write but requires creating DB and network clients after fork.

**Example:**

```python
# Capacity sketch (not a benchmark): think in these terms
workers_per_pod = 4
pods = 5
pool_size, max_overflow = 5, 5
max_db_connections = workers_per_pod * pods * (pool_size + max_overflow)   # 200
print("need Postgres max_connections (or PgBouncer) above", max_db_connections)

# gunicorn hook: recreate resources after fork when using --preload
def post_fork(server, worker):
    from app.db import engine
    engine.dispose(close=False)      # do not reuse the parent's connections
```

**Remember:** Scale with processes and replicas; offload heavy work; budget downstream connections.

## Q97. Logging and structured logs

Use the standard `logging` module with a named logger per module (`logging.getLogger(__name__)`), configure handlers once at startup, and log to stdout in containers. In production, emit structured JSON logs (via a JSON formatter or `structlog`) with consistent fields such as timestamp, level, message, request ID, trace ID and user ID, so logs can be filtered and correlated. Use lazy `%s` formatting, `logger.exception` in except blocks, and never log secrets or full request bodies with PII.

- **Trade-offs**:
  - Rich structured context speeds debugging but increases log volume and cost; sample or lower levels on hot paths.

**Example:**

```python
import contextvars, json, logging, sys

request_id: contextvars.ContextVar[str] = contextvars.ContextVar("request_id", default="-")

class JsonFormatter(logging.Formatter):
    def format(self, record: logging.LogRecord) -> str:
        payload = {
            "ts": self.formatTime(record),
            "level": record.levelname,
            "logger": record.name,
            "msg": record.getMessage(),
            "request_id": request_id.get(),     # works across async tasks
        }
        if record.exc_info:
            payload["exc"] = self.formatException(record.exc_info)
        return json.dumps(payload)

handler = logging.StreamHandler(sys.stdout)
handler.setFormatter(JsonFormatter())
logging.basicConfig(level=logging.INFO, handlers=[handler])

log = logging.getLogger(__name__)
log.info("order created id=%s", 42)             # lazy formatting
try:
    1 / 0
except ZeroDivisionError:
    log.exception("failed to compute total")    # includes traceback
```

**Remember:** One logger per module, JSON to stdout, request IDs via contextvars, no secrets.

## Q98. Dockerizing Python apps

Use a slim official Python base image, a multi-stage build that installs dependencies from a lock file in a builder stage, and copy only the virtualenv and app code into the final image. Set `PYTHONDONTWRITEBYTECODE=1` and `PYTHONUNBUFFERED=1`, run as a non-root user, and order layers so dependency installs are cached when only code changes. Handle signals properly (exec-form `CMD`) so the server shuts down gracefully, and add a health endpoint for orchestration.

- **Trade-offs**:
  - Slim images are small but may lack build tools for C extensions (install them in the builder stage only); Alpine uses musl, which can force compiling wheels from source.

**Example:**

```python
# Dockerfile (shown as comments)
# FROM python:3.12-slim AS builder
# ENV PIP_NO_CACHE_DIR=1
# WORKDIR /app
# RUN python -m venv /opt/venv
# ENV PATH="/opt/venv/bin:$PATH"
# COPY requirements.lock .
# RUN pip install -r requirements.lock           # cached unless lock changes
#
# FROM python:3.12-slim
# ENV PYTHONDONTWRITEBYTECODE=1 PYTHONUNBUFFERED=1 PATH="/opt/venv/bin:$PATH"
# RUN useradd --create-home app
# COPY --from=builder /opt/venv /opt/venv
# WORKDIR /app
# COPY --chown=app:app app/ ./app/
# USER app
# EXPOSE 8000
# CMD ["gunicorn", "app.main:app", "-c", "app/gunicorn.conf.py"]   # exec form: receives SIGTERM

# Health endpoint used by the orchestrator
from fastapi import FastAPI
app = FastAPI()

@app.get("/healthz")
async def healthz() -> dict:
    return {"status": "ok"}
```

**Remember:** Slim multi-stage image, locked deps, non-root, exec-form CMD, health check.

## Q99. Observability hooks: metrics, traces and health

Production services need the three signals: structured logs, metrics (request rate, errors, latency percentiles, queue depth, pool usage) and distributed traces across services. OpenTelemetry provides Python SDKs and auto-instrumentation for FastAPI, Django, SQLAlchemy, httpx, Redis and Celery, exporting to your backend of choice; `prometheus-client` is a common way to expose metrics. Add liveness and readiness endpoints, where readiness checks critical dependencies, and propagate trace context through message queues.

- **Trade-offs**:
  - Auto-instrumentation gives fast coverage but adds overhead and high-cardinality risk; avoid user IDs or raw URLs as metric labels and sample traces at high volume.

**Example:**

```python
from fastapi import FastAPI
from opentelemetry import trace
from opentelemetry.instrumentation.fastapi import FastAPIInstrumentor
from opentelemetry.instrumentation.sqlalchemy import SQLAlchemyInstrumentor
from prometheus_client import Counter, Histogram, make_asgi_app

app = FastAPI()
FastAPIInstrumentor.instrument_app(app)             # spans per request
SQLAlchemyInstrumentor().instrument(engine=engine)  # spans per query
app.mount("/metrics", make_asgi_app())              # Prometheus scrape endpoint

ORDERS = Counter("orders_created_total", "Orders created", ["channel"])
CHECKOUT_LATENCY = Histogram("checkout_seconds", "Checkout latency")
tracer = trace.get_tracer(__name__)

@app.post("/checkout")
async def checkout() -> dict:
    with CHECKOUT_LATENCY.time(), tracer.start_as_current_span("charge_card"):
        ...
    ORDERS.labels(channel="web").inc()               # low-cardinality label
    return {"ok": True}

@app.get("/readyz")
async def readyz() -> dict:
    # check DB and Redis connectivity here; return 503 if unavailable
    return {"ready": True}
```

**Remember:** Logs, metrics, traces via OpenTelemetry; readiness checks dependencies; keep labels low-cardinality.

## Q100. Choosing Python vs Node.js for a service

Both are strong for I/O-bound web backends. Choose Python when the service is close to data or ML (NumPy, pandas, PyTorch, scikit-learn), needs Django's admin and ORM for a data-heavy product, or runs heavy background processing with Celery, or when the team is Python-first. Choose Node when you want one language across frontend and backend, a very large number of concurrent lightweight connections with an async-by-default ecosystem (real-time, BFF, SSR), or shared TypeScript types with the client. For CPU-heavy work, neither is ideal in-process: both scale via multiple processes, native extensions or dedicated workers.

- **Trade-offs**:
  - Python: excellent data/ML ecosystem and readable code, but sync/async split and the GIL require deliberate architecture.
  - Node: async-first and one language end to end, but weaker numerical and ML ecosystem.
  - Team skills, existing platform tooling and operational maturity usually matter more than raw runtime differences.

| Factor | Python | Node.js |
|--------|--------|---------|
| Concurrency model | Sync or asyncio (opt-in) | Event loop, async by default |
| Multi-core | Multiple processes (free-threading emerging) | Multiple processes, worker_threads |
| Data / ML ecosystem | Excellent | Limited |
| Full-stack type sharing | Via OpenAPI codegen | Native with TypeScript |
| Batteries-included framework | Django | NestJS (more modular) |
| Background jobs | Celery, RQ, Dramatiq | BullMQ and similar |

**Example:**

```python
# A pragmatic split many teams use:
# - Node/TypeScript BFF: sessions, SSR, aggregation for the web app
# - Python FastAPI service: recommendations, pricing models, data pipelines
# - Celery workers: batch scoring and report generation via RabbitMQ
# Services talk over HTTP/JSON or a message broker with shared OpenAPI/JSON Schema contracts.
```

> **Interview tip:** Avoid tribal answers. Frame it as "workload shape, ecosystem fit, team skills, operational cost", then pick.

See the [Node.js question index](../node-express/question-index.md) for the Node perspective.

**Remember:** Python for data, ML and batteries-included products; Node for JS-everywhere and real-time; team fit decides ties.

## References

- [The Python profilers](https://docs.python.org/3/library/profile.html)
- [tracemalloc module](https://docs.python.org/3/library/tracemalloc.html)
- [functools.lru_cache](https://docs.python.org/3/library/functools.html#functools.lru_cache)
- [logging HOWTO](https://docs.python.org/3/howto/logging.html)
- [Logging cookbook](https://docs.python.org/3/howto/logging-cookbook.html)
- [contextvars module](https://docs.python.org/3/library/contextvars.html)
- [FastAPI deployment](https://fastapi.tiangolo.com/deployment/)
- [PEP 703 - Making the GIL optional](https://peps.python.org/pep-0703/)
