---
sidebar_label: "Fundamentals"
description: "Celery's core building blocks (producer, broker, worker, result backend) and the full lifecycle of a task."
---

# Celery Fundamentals (Q1-Q4)

> **Reviewed:** 2026-09 · **Level:** Senior · **Type:** Foundational

## Q1. Celery is a distributed task queue that moves slow work out of the request path

Celery lets a web process say "do this later, somewhere else" by serializing a function call into a message and handing it to a broker. Separate worker processes pull those messages and run the function. The web request returns fast, and the heavy work (emails, PDFs, image processing, calling slow third-party APIs, ML inference) runs asynchronously and can be scaled independently.

**How it works:**

| Component | Role | Typical choice |
|---|---|---|
| Producer (client) | Calls `task.delay()` / `apply_async()`; serializes name + args into a message | Django / FastAPI / Flask app |
| Broker | Stores and delivers task messages | RabbitMQ or Redis |
| Worker | Consumes messages, executes the task function, acknowledges | `celery -A proj worker` |
| Result backend (optional) | Stores return value / state keyed by task id | Redis, database, RPC |
| Beat (optional) | Scheduler that publishes periodic tasks | `celery -A proj beat` |

**Example:**

```python
# proj/celery_app.py
from celery import Celery

app = Celery(
    "proj",
    broker="amqp://guest:guest@rabbitmq:5672//",
    backend="redis://redis:6379/1",   # only if you need results
)
app.conf.update(
    task_serializer="json",
    accept_content=["json"],
    result_serializer="json",
    timezone="UTC",
)

@app.task
def send_welcome_email(user_id: int) -> None:
    ...  # load user by id, render template, call email provider

# In a request handler:
send_welcome_email.delay(user.id)   # returns AsyncResult immediately
```

**Trade-offs and pitfalls:**

- You now run and monitor extra infrastructure (broker, workers, maybe a backend).
- Work is asynchronous: the user cannot see the result in the same response, so you need status polling, webhooks or notifications.
- Delivery is at-least-once in realistic configurations, so tasks must tolerate re-execution (see [Reliability](./04-reliability.md)).

**Remember:** Celery = serialize a function call, queue it on a broker, run it on a worker.

## Q2. A task goes through publish, reserve, execute, acknowledge and (optionally) store result

Walking through the lifecycle is a common senior question because every reliability setting maps to one of these steps. The producer publishes a message; the broker holds it; a worker reserves it (it is delivered but unacknowledged, and may sit in the worker's prefetch buffer); the worker executes it; the message is acknowledged either before or after execution; and finally the state and return value are written to the result backend if one is configured.

**How it works:**

```mermaid
sequenceDiagram
    participant App
    participant Broker
    participant Worker
    participant Backend
    App->>Broker: publish task message with id, name, args
    Broker-->>App: accepted (confirm if enabled)
    Broker->>Worker: deliver message (reserved, unacked)
    Note over Worker: early ack by default happens here
    Worker->>Backend: STARTED if task_track_started is on
    Worker->>Worker: execute task function
    Worker->>Broker: ack (late ack happens here if task_acks_late)
    Worker->>Backend: store SUCCESS or FAILURE with result
    App->>Backend: AsyncResult.get or poll state by id
```

States you will see: `PENDING` (unknown, also the default for any unknown id), `RECEIVED`, `STARTED` (only with `task_track_started=True`), `RETRY`, `SUCCESS`, `FAILURE`, `REVOKED`.

**Example:** A user uploads a CSV. The API stores the file, publishes `import_csv.delay(upload_id)`, and returns `202 Accepted` with the task id. The UI polls `/imports/{task_id}`, which reads `AsyncResult(task_id).state`.

**Trade-offs and pitfalls:**

- `PENDING` does not mean "queued"; it means "the backend knows nothing about this id", which also covers typos and expired results.
- By default the ack happens *before* execution (early ack). A crash mid-task loses that task. Late acks trade this for possible duplicates.
- Results expire (`result_expires`, default one day), so do not treat the backend as a permanent store.

**Remember:** Every reliability knob (acks, prefetch, visibility timeout, backend) lives on one arrow of this lifecycle.

## Q3. Tasks should receive small, serializable identifiers, not rich objects

Task arguments are serialized into the message. With the JSON serializer you can only send JSON-compatible values, and even with other serializers you should pass IDs rather than ORM objects. The object may change between enqueue and execution, the message gets bloated, and you couple the message format to your model classes.

**Example:**

```python
# Bad: serializes a stale snapshot (and fails with JSON serializer)
generate_invoice.delay(order)

# Good: worker loads fresh state
generate_invoice.delay(order.id)

@app.task
def generate_invoice(order_id: int) -> str:
    order = Order.objects.get(pk=order_id)
    if order.invoice_id:          # idempotency guard
        return order.invoice_id
    ...
```

**Trade-offs and pitfalls:**

- Avoid `pickle` for task payloads; a malicious message on the broker could execute arbitrary code. Keep `accept_content=["json"]`.
- Large payloads (files, big lists) belong in object storage or the database; pass a key. See [MinIO app integration](../minio/07-app-integration.md).
- Passing an ID means the row must exist when the worker runs; enqueue after the transaction commits ([Production patterns](./10-production-patterns.md)).

**Remember:** Send pointers, not payloads.

## Q4. `delay()`, `apply_async()` and signatures are different ways to describe a task call

`task.delay(*args)` is a shortcut for `task.apply_async(args=args)`. Use `apply_async` when you need execution options: `countdown`, `eta`, `expires`, `queue`, `priority`, `task_id`, `headers`. A signature (`task.s(...)` / `task.si(...)`) is a serializable "call description" that you can pass around, compose into workflows, or enqueue later.

**Example:**

```python
send_report.delay(42)

send_report.apply_async(
    args=[42],
    countdown=60,              # not before 60 seconds from now
    expires=3600,              # discard if not started within an hour
    queue="reports",
    task_id=f"report-42-{date.today()}",  # deterministic id helps dedupe/tracing
)

sig = send_report.s(42).set(queue="reports")
sig.apply_async()

# Decouple producer from worker code: publish by name
app.send_task("reports.send_report", args=[42], queue="reports")
```

**Trade-offs and pitfalls:**

- `countdown`/`eta` tasks are delivered to a worker immediately and held in memory until due. Long delays interact badly with Redis `visibility_timeout` and RabbitMQ `consumer_timeout` (see [Reliability](./04-reliability.md)).
- `send_task` avoids importing worker code in the API service, but you lose argument checking; typos fail at runtime.
- Setting a custom `task_id` does not deduplicate by itself; Celery will happily run two messages with the same id.

<details>
<summary>Follow-up questions</summary>

- *How would you schedule something for next week?* Store the intent in the database with a due time and let a periodic task pick up due rows, instead of a week-long `eta`.
- *What does `expires` protect against?* Stale work after an outage, for example sending a "your code is 123456" SMS that is already invalid.

</details>

**Remember:** `delay` for simple calls, `apply_async` for options, signatures for composition.

## References

- [Celery documentation](https://docs.celeryq.dev/en/stable/)
- [Messaging systems overview](../architecture/05-messaging-systems.md)
