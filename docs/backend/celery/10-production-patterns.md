---
sidebar_label: "Production Patterns"
description: "Integrating Celery with Django and FastAPI, fork-safe client setup, enqueue-after-commit and outbox patterns, and when Celery is the wrong tool."
---

# Production Patterns (Q38-Q41)

> **Reviewed:** 2026-09 · **Level:** Senior · **Type:** Foundational

## Q38. Django and FastAPI integrate with Celery as producers, sharing code but not processes

The web app and the workers usually share one codebase and image, with different entrypoints. In Django, the standard layout is a `celery.py` next to `settings.py` that reads `CELERY_`-prefixed settings and autodiscovers `tasks.py` in each app. In FastAPI there is no framework glue: create the Celery app in a module, import tasks (or use `send_task` by name) from route handlers, and return `202` with a job id.

**Example:**

```python
# Django: proj/celery.py
import os
from celery import Celery

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "proj.settings")
app = Celery("proj")
app.config_from_object("django.conf:settings", namespace="CELERY")
app.autodiscover_tasks()

# settings.py
CELERY_BROKER_URL = "amqp://app:secret@rabbitmq:5672/celery"
CELERY_TASK_ACKS_LATE = True
CELERY_WORKER_PREFETCH_MULTIPLIER = 1
```

```python
# FastAPI
from fastapi import FastAPI
from worker.celery_app import app as celery_app

api = FastAPI()

@api.post("/exports", status_code=202)
async def create_export(req: ExportRequest):
    export_id = await exports_repo.create(req)          # commit first
    celery_app.send_task("exports.build", args=[export_id], queue="heavy")
    return {"export_id": export_id, "status": "queued"}
```

**Trade-offs and pitfalls:**

- `apply_async` is a synchronous network call; in an async FastAPI handler it briefly blocks the event loop. Usually acceptable; under heavy load, run it in a thread pool.
- Do not await Celery results in async handlers; poll a status endpoint instead.
- Sharing one image keeps task signatures in sync; separate repos need versioned task contracts.

**Remember:** Web app enqueues and returns; workers do the work; status lives in your DB.

## Q39. Create DB and HTTP clients per worker process, not at import time

The prefork pool forks child processes from the parent. Anything created at import time in the parent (DB connection pools, HTTP sessions with open sockets, gRPC channels, Mongo clients, some SDK clients with background threads) is copied into every child. Sharing a socket across processes corrupts protocol state, and threads do not survive fork. Initialize those per child with the `worker_process_init` signal and close them on `worker_process_shutdown`.

**Example:**

```python
from celery.signals import worker_process_init, worker_process_shutdown
import httpx
from sqlalchemy import create_engine

engine = None
http = None

@worker_process_init.connect
def init_clients(**_):
    global engine, http
    engine = create_engine(DB_URL, pool_size=5, pool_pre_ping=True)
    http = httpx.Client(timeout=10)
    # heavy one-time loads (ML models) belong here too, once per child

@worker_process_shutdown.connect
def close_clients(**_):
    if http:
        http.close()
    if engine:
        engine.dispose()
```

**Trade-offs and pitfalls:**

- If an engine already exists in the parent, call `engine.dispose(close=False)` in the child so it does not reuse the parent's connections.
- Django manages DB connections per task (`CONN_MAX_AGE` still applies); the main risk is custom clients created at module import.
- Pool size × processes × replicas = total connections; put PgBouncer in front if it gets large.

**Remember:** Fork first, connect second.

## Q40. Enqueue after commit, or use a transactional outbox

Two classic races. First, the task is published inside a DB transaction and a fast worker reads the row before it is committed ("DoesNotExist"). Second, the transaction rolls back after the task was published, so the task acts on something that never happened. Fix the first with enqueue-on-commit. Fix both (plus "broker was down at commit time") with a transactional outbox: write the event row in the same transaction, then a relay publishes it.

**How it works:**

```mermaid
sequenceDiagram
    participant Api
    participant Db
    participant Relay
    participant Broker
    participant Worker
    Api->>Db: BEGIN, insert order, insert outbox row, COMMIT
    Relay->>Db: poll unsent outbox rows
    Relay->>Broker: publish task
    Relay->>Db: mark outbox row sent
    Broker->>Worker: deliver task
    Worker->>Db: process order idempotently
```

**Example:**

```python
from django.db import transaction

def place_order(request):
    with transaction.atomic():
        order = Order.objects.create(...)
        transaction.on_commit(lambda: send_confirmation.delay(order.id))
    return JsonResponse({"id": order.id}, status=201)

# Celery 5.4+ also offers task.delay_on_commit(order.id) for Django tasks
```

**Trade-offs and pitfalls:**

- `on_commit` publishes after commit but is not durable: if the process dies or the broker is down between commit and publish, the task is lost. The outbox closes that gap.
- The outbox relay can publish twice (crash after publish, before marking sent), so consumers stay idempotent.
- In non-Django stacks (FastAPI + SQLAlchemy), publish after `await session.commit()`, or use the outbox.

> **Interview tip:** "Enqueue on commit for convenience, outbox when losing the side effect is unacceptable" is a crisp senior answer.

**Remember:** Never publish a task about data that is not committed yet.

## Q41. Celery is the wrong tool when you need event streams, durable workflows or a lighter queue

Celery is a strong default for Python background jobs. It is a poor fit when the problem is really something else.

| Need | Better fit | Why |
|---|---|---|
| Event log that many services replay, ordered per key, retention | Kafka (or RabbitMQ Streams) | Consumers read independently; data is retained |
| Multi-step business process with long waits, retries and compensation | Temporal or similar workflow engine | Durable state and timers are the core feature |
| Simple Python jobs, Redis only, minimal config | RQ, Dramatiq | Smaller surface area, fewer knobs |
| Cross-language consumers | Plain RabbitMQ/SQS with a documented message schema | Celery message protocol is Python-centric |
| Managed, serverless on AWS | SQS + Lambda | No brokers or workers to run |

**Example:** An e-commerce platform uses Celery for emails and thumbnails, Kafka for "order placed" events consumed by analytics, search indexing and fraud, and a workflow engine for the multi-day refund process.

**Trade-offs and pitfalls:**

- Replacing Celery is costly; many "Celery problems" are configuration problems (acks, prefetch, visibility timeout, routing).
- Adding a second system for one use case adds operational burden; justify it with a concrete requirement.

**Remember:** Celery runs jobs; it is not an event log or a workflow database.

## References

- [Celery documentation: Django integration and signals](https://docs.celeryq.dev/en/stable/)
- [Messaging systems overview](../architecture/05-messaging-systems.md)
- [Python backend (this site)](../python/index.md)
- [RabbitMQ vs Kafka vs SQS vs Redis (this site)](../rabbitmq/10-rabbitmq-vs-kafka-sqs-redis.md)
