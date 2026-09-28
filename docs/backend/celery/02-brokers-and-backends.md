---
sidebar_label: "Brokers and Result Backends"
description: "Choosing Redis or RabbitMQ as the Celery broker, picking a result backend, and knowing when to skip results entirely."
---

# Brokers and Result Backends (Q5-Q8)

> **Reviewed:** 2026-09 · **Level:** Senior · **Type:** Foundational

## Q5. RabbitMQ is the more "correct" broker; Redis is the more convenient one

Both are officially supported and production-worthy. RabbitMQ is a real message broker: it tracks unacknowledged deliveries per consumer, redelivers when a connection dies, supports native priorities, dead-lettering and publisher confirms. Redis is a data structure server that Celery (via Kombu) uses as a broker by emulating acknowledgements with a visibility timeout. Redis is often already in the stack and is simple to run, which is why many teams start there.

**How it works:**

| Concern | RabbitMQ | Redis |
|---|---|---|
| Unacked message handling | Broker redelivers when the consumer's channel/connection closes | Redelivered after `visibility_timeout` expires (default one hour) |
| Long tasks / long ETAs | Works, but watch `consumer_timeout` for unacked deliveries | Tasks longer than the visibility timeout can be executed twice |
| Priorities | Native per-queue (`x-max-priority`) | Emulated with multiple lists per priority step |
| Dead-lettering | Native DLX | Not native; build it in task code |
| Remote control / broadcast | Supported | Supported (uses pub/sub) |
| Ops familiarity | Separate system to learn | Often already running |
| Durability | Durable queues + persistent messages; quorum queues for HA | Depends on AOF/RDB settings and replication |

**Example:**

```python
# RabbitMQ
broker_url = "amqp://app:secret@rabbitmq:5672/celery"   # vhost "celery"

# Redis
broker_url = "redis://redis:6379/0"
broker_transport_options = {
    "visibility_timeout": 4 * 3600,  # must exceed longest task and longest countdown/eta
}
```

**Trade-offs and pitfalls:**

- Redis as broker loses queued tasks if Redis is not configured for persistence and restarts.
- Using one Redis for cache (with eviction) *and* broker is dangerous: `maxmemory` eviction can drop task messages. Use a separate instance or `noeviction`.
- RabbitMQ needs capacity planning of its own: memory/disk alarms block publishers (see [RabbitMQ flow control](../rabbitmq/06-prefetch-flow-control.md)).

> **Interview tip:** Say "RabbitMQ when task loss or duplicates are expensive; Redis when simplicity matters and tasks are short and idempotent", then mention the visibility timeout pitfall. That shows you know the mechanism, not just the brand.

**Remember:** RabbitMQ has real acks; Redis fakes them with a timeout.

## Q6. The result backend stores task state and return values, and it is optional

A result backend is where workers write `SUCCESS`/`FAILURE` plus the return value, so a caller can later ask "is task X done, and what did it return?". Chords also need a backend to know when all header tasks finished. Common choices: Redis (fast, expiring keys), a SQL database via SQLAlchemy or `django-celery-results` (queryable, durable), and `rpc://` (results sent back over AMQP to the caller, transient).

**How it works:**

| Backend | Good for | Watch out for |
|---|---|---|
| Redis | Fast polling, chords, short-lived results | Memory growth if `result_expires` is disabled |
| SQL / Django ORM | Audit, admin visibility, joins with app data | Write load on the primary DB; table cleanup |
| RPC (`rpc://`) | Caller waits on its own result, no storage | Only the original caller can read it; lost on restart |
| Object stores / others | Large results (prefer storing a key instead) | Latency |

**Example:**

```python
result_backend = "redis://redis:6379/1"
result_expires = 3600          # seconds; default is one day
result_extended = True         # store task name, args, worker in the result meta
task_track_started = True      # expose STARTED state for progress UIs
```

**Trade-offs and pitfalls:**

- Do not return big objects; write them to storage and return a pointer.
- A DB backend on your main primary turns every task into an extra write.
- `AsyncResult.get()` in a web request turns async work back into a blocking call; poll or push instead.

**Remember:** The backend is a short-term status cache, not your system of record.

## Q7. Most fire-and-forget tasks should ignore results

If nobody reads the return value (emails, cache warming, webhooks), storing it is wasted I/O and memory. Set `ignore_result=True` per task or `task_ignore_result=True` globally, and record meaningful outcomes in your own domain tables instead ("email_sent_at", "export.status = ready").

**Example:**

```python
app.conf.task_ignore_result = True   # default off for everything

@app.task(ignore_result=False)       # opt in where a caller polls
def build_export(export_id: int) -> str:
    ...
    return object_key
```

**Trade-offs and pitfalls:**

- Chords need results from header tasks; ignoring results there breaks the chord.
- Without results you cannot `get()`; tracking must live in your data model or in monitoring (Flower, events).
- Domain status columns are usually better anyway: they survive result expiry and are queryable.

**Remember:** If nothing reads it, don't store it.

## Q8. Broker and backend choices shape failure modes, so plan for broker outages

A senior answer covers what happens when the broker is down. Producers calling `delay()` will retry the connection (governed by `broker_connection_retry` and publish retry policy) and may block or raise. If the web request cannot enqueue, you either fail the request, or write the intent to the database first (outbox) and publish later.

**Example:**

```python
task_publish_retry = True
task_publish_retry_policy = {
    "max_retries": 3,
    "interval_start": 0,
    "interval_step": 0.5,
    "interval_max": 2,
}
broker_connection_retry_on_startup = True
```

**Trade-offs and pitfalls:**

- Long publish retries inside a request handler increase latency and tie up web workers during an outage.
- Losing the broker without persistence loses queued work; durability settings on the broker matter as much as Celery settings.
- The outbox pattern ([Production patterns](./10-production-patterns.md)) decouples "the DB change happened" from "the broker was reachable".

**Remember:** Decide up front whether an enqueue failure fails the request or goes to an outbox.

## References

- [Celery documentation: brokers and backends](https://docs.celeryq.dev/en/stable/)
- [RabbitMQ documentation](https://www.rabbitmq.com/docs)
- [Messaging systems overview](../architecture/05-messaging-systems.md)
