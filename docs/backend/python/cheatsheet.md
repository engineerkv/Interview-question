---
sidebar_position: 100
sidebar_label: Cheatsheet
description: "Condensed Python backend revision notes and a pre-interview checklist covering runtime, async, frameworks, databases, security, testing and production."
---

# Python Backend Cheatsheet

> **Reviewed:** 2026-09 · **Level:** Senior · **Type:** Foundational

Condensed revision notes for the [100 questions](./question-index.md). Each section links back to the full answers.

## Runtime and language ([Q1-Q14](./01-fundamentals-and-runtime.md))

- CPython: source to AST to bytecode (`.pyc`) to interpreter loop; speed comes from C extensions.
- GIL: one thread runs Python bytecode at a time; released on blocking I/O. Threads suit I/O work, processes suit CPU work.
- Names bind to objects; assignment never copies. Arguments are passed by object reference: mutations are visible to the caller, rebinding is not.
- `is` checks identity (use it for `None` and sentinels); `==` checks value.
- Mutable default arguments are evaluated once: use `None` and create the value inside.
- Memory: reference counting frees most objects immediately; the `gc` module collects reference cycles.
- Packaging: one venv per project, `pyproject.toml` for metadata, a lock file (uv, Poetry, pip-tools), frozen installs in CI.
- Type hints are ignored at runtime, but FastAPI and Pydantic read them to validate data.
- Defining `__eq__` sets `__hash__` to `None` unless you also define `__hash__`. Keep secrets out of `__repr__`.

## Data structures ([Q15-Q26](./02-data-structures-and-stdlib.md))

| Operation | list | dict / set | deque |
|-----------|------|------------|-------|
| Index / lookup | O(1) | O(1) average | O(n) in the middle |
| Append at end | O(1) amortised | O(1) average | O(1) |
| Insert/pop at front | O(n) | n/a | O(1) |
| Membership `in` | O(n) | O(1) average | O(n) |

- Dicts preserve insertion order (3.7+). Slices create shallow copies.
- Use a generator expression to stream values into `sum`, `any` or `max`; use a comprehension to build a collection.
- Iterators can be consumed only once. Generators give lazy pipelines with constant memory.
- Useful standard library tools: `defaultdict`, `Counter`, `deque(maxlen=)`, `heapq`, `itertools.batched`, and `groupby` (sort the input first).
- Dataclasses generate boilerplate but do not validate; use Pydantic at trust boundaries. Use `field(default_factory=list)` for mutable defaults.
- Sorting uses `key=`, is stable, and accepts tuple keys for multi-field sorts.

## Functions and OOP ([Q27-Q40](./03-functions-oop-and-design.md))

- Closures capture variables, not values (late binding). Use `nonlocal` to rebind an enclosing variable.
- `@d` means `f = d(f)`. Always apply `functools.wraps`. A decorator with arguments is a factory that returns a decorator.
- Use `*` to make later parameters keyword-only and `/` to make earlier ones positional-only.
- Use `with` for every resource. `contextlib.contextmanager` builds a context manager from a generator; `async with` is for async resources.
- `classmethod` suits alternative constructors, `property` suits computed or validated attributes, and `staticmethod` is rarely needed.
- `super()` calls the next class in the MRO (C3 linearisation), so mixins must cooperate by calling it too.
- An ABC enforces its interface at runtime through inheritance; a Protocol is structural and checked statically.
- Use `__slots__` when you create many small objects. Descriptors power `property`, methods and ORM fields.
- Try `__init_subclass__` or a class decorator before reaching for a metaclass.
- Apply SOLID by injecting Protocol-typed dependencies, and do not build hierarchies speculatively.

## Async and concurrency ([Q41-Q54](./04-async-and-concurrency.md))

- asyncio fits many concurrent sockets, threads fit blocking libraries, and processes fit CPU-bound work.
- Coroutines are lazy: calling one does nothing until it is awaited or wrapped in a Task. Keep references to background tasks.
- `gather` collects results (pass `return_exceptions=True` to get errors as values). `TaskGroup` cancels sibling tasks when one fails and raises an `ExceptionGroup`, handled with `except*`.
- Wrap every network await in `asyncio.timeout()`. Never swallow `CancelledError`.
- Never block the event loop. Use async libraries, `asyncio.to_thread` for blocking I/O, and a process pool for CPU work.
- In FastAPI, `def` endpoints run in a threadpool and `async def` endpoints run on the event loop.
- The GIL does not make `x += 1` atomic, so use locks. In-process locks do not work across workers; use the database or Redis for that.
- Use `asyncio.Semaphore` to cap outbound concurrency and bounded queues to create backpressure.
- Compared with Node: Python uses the same event-loop model, but async is opt-in and coroutines are lazy.
- Free-threaded CPython (PEP 703) is Emerging: optional build, check C-extension support.

## Web frameworks ([Q55-Q66](./05-web-frameworks.md))

- WSGI is synchronous (Django, Flask with gunicorn). ASGI is async and supports WebSockets and streaming (FastAPI with uvicorn).
- Framework choice: Django for full products with admin and ORM, FastAPI for typed async APIs, Flask for minimal custom stacks.
- In FastAPI, type hints drive parsing, validation, OpenAPI docs and response filtering (`response_model`).
- `Depends` provides per-request dependency injection. Dependencies that `yield` clean up after the response. Tests use `dependency_overrides`.
- Pydantic v2: `model_validate` and `model_dump`, `extra="forbid"`, strict types where coercion is risky. Use `BaseSettings` for configuration.
- Request lifecycle: server, then middleware, router, dependencies, validation, endpoint, response model, and finally cleanup and background tasks.
- `BackgroundTasks` is best-effort and runs in the same process. Use [Celery](../celery/index.md) for durable, retryable work.
- Scale with worker processes. Create shared clients once per worker in `lifespan`, not per request.

## Databases ([Q67-Q76](./06-databases-and-orm.md))

- SQLAlchemy Core is SQL expressed in Python; the ORM adds objects and a Session. The two can be mixed.
- A Session is a unit of work with an identity map: use one per request or task and never share it.
- Fix N+1 queries with `selectinload` for collections and `joinedload` for many-to-one. In Django, use `select_related` and `prefetch_related`. Set `lazy="raise"` in API code.
- Connection pools are per process: total connections = pool size × workers × replicas, which must fit under the database's `max_connections` (or use PgBouncer).
- Keep transactions short. Stronger isolation levels mean you must retry on serialization failures.
- Use `FOR UPDATE` for hot rows and version columns for optimistic locking. Prefer conditional atomic `UPDATE`s.
- Migrations: review autogenerated ones, and use expand, backfill, contract for zero-downtime changes.
- Async apps need an async driver (`asyncpg`, psycopg 3) and eager loading.
- Use the ORM by default and raw SQL for reports and bulk work, always with bound parameters.
- Redis: always set TTLs, use pipelines, rely on `SET NX` for locks and idempotency, and plan for Redis being down.

## APIs and security ([Q77-Q84](./07-apis-auth-and-security.md))

- REST: correct status codes (201 plus `Location`, 204, 409, 422), separate input and output schemas, versioned paths.
- Pagination: keyset cursors for large or live data, offset only for small lists. Cap `limit` on the server.
- Idempotency keys: reserve atomically, store the response, compare request hashes.
- Sessions revoke easily; JWTs are stateless. A common compromise is short-lived access tokens plus refresh tokens, with the algorithm list, `aud`, `iss` and `exp` all validated.
- OAuth2: Authorization Code with PKCE for users, Client Credentials for services. Validate the JWT in a dependency.
- Hash passwords with Argon2id or bcrypt, never a fast hash. Run verification off the event loop.
- Never string-format SQL, never unpickle untrusted data, use `yaml.safe_load`, allowlist outbound URLs to prevent SSRF, and avoid `shell=True`.
- 12-factor: config from the environment, secrets from a manager, `SecretStr` in settings, no secrets in images or logs.

## Testing and tooling ([Q85-Q92](./08-testing-and-tooling.md))

- pytest: fixtures (with `yield` and scopes) in `conftest.py`, `parametrize` with ids, transaction-rollback fixtures for DB tests.
- Mocking: patch the name where it is used, set `autospec=True`, use `AsyncMock` for async code, and mock only at boundaries.
- Async tests need pytest-asyncio or the anyio plugin. Test timeouts and cancellation too.
- Endpoint tests: `TestClient` or `httpx.AsyncClient(transport=ASGITransport(app=app))`. Django tests use `client` plus `django_db`.
- Enable branch coverage with a `--cov-fail-under` floor in CI.
- Use ruff for linting and formatting (black-compatible), mypy or pyright with gradual strictness, and pre-commit locally with the same hooks in CI.

## Production ([Q93-Q100](./09-performance-and-production.md))

- Profiling: cProfile in development, py-spy (`top`, `record`, `dump`) against live processes.
- Leaks are usually lingering references. Compare `tracemalloc` snapshots and bound every cache. `max_requests` is a safety net, not a fix.
- Cache pure per-process work with `lru_cache` and shared data in Redis with TTLs, jitter and invalidation. Do not use `lru_cache` on async functions.
- Scale with processes and replicas, move heavy work to Celery, and autoscale on latency or queue depth, not CPU alone.
- Logging: one logger per module, JSON to stdout, request IDs via `contextvars`, `logger.exception` in except blocks.
- Docker: slim multi-stage image, locked dependencies, non-root user, exec-form `CMD`, `PYTHONUNBUFFERED=1`.
- Observability: OpenTelemetry auto-instrumentation, Prometheus metrics with low-cardinality labels, liveness and readiness probes.
- Python vs Node: Python for data, ML and batteries-included products; Node for JavaScript everywhere and real-time. Team fit decides close calls.

## Pre-interview checklist

- [ ] I can explain the GIL, and when threads, processes or asyncio are the right choice, in under a minute.
- [ ] I can explain the mutable default argument bug and pass-by-object-reference.
- [ ] I can write a decorator with arguments that uses `functools.wraps` and supports `async def`.
- [ ] I can write a context manager with both `__enter__`/`__exit__` and `@contextmanager`.
- [ ] I can explain why blocking calls freeze asyncio and how to fix them (`to_thread`, async drivers).
- [ ] I can compare `gather` and `TaskGroup`, including how each handles errors and cancellation.
- [ ] I can compare Django, FastAPI and Flask, and justify a choice for a given service.
- [ ] I can show a FastAPI `Depends` chain with a DB session that `yield`s and a test override.
- [ ] I can detect and fix N+1 queries in SQLAlchemy and Django.
- [ ] I can size connection pools across workers and replicas.
- [ ] I can design cursor pagination and idempotency keys.
- [ ] I can explain the JWT vs sessions trade-offs and how to validate a JWT safely.
- [ ] I can list the Python-specific security risks: pickle, `yaml.load`, `shell=True`, SSRF.
- [ ] I can explain "patch where it is used" and test async code.
- [ ] I can profile a live worker with py-spy and find a leak with tracemalloc.
- [ ] I can outline a production Dockerfile and a gunicorn/uvicorn worker configuration.
- [ ] I can argue Python vs Node for a service using workload, ecosystem and team criteria.
