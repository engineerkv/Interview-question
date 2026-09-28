---
sidebar_label: "Retries, Timeouts and Failures"
description: "Automatic retries with exponential backoff, soft and hard time limits, dead-letter patterns, and handling poison tasks in Celery."
---

# Retries, Timeouts and Failures (Q25-Q29)

> **Reviewed:** 2026-09 · **Level:** Senior · **Type:** Foundational

## Q25. `autoretry_for` with exponential backoff handles transient failures declaratively

Most task failures are transient: a timeout from a partner API, a deadlock, a 503. Celery can retry automatically when specific exceptions are raised, with growing delays and jitter so a thousand failed tasks do not all retry at the same second.

**Example:**

```python
import requests

@app.task(
    bind=True,
    autoretry_for=(requests.Timeout, requests.ConnectionError),
    retry_backoff=True,        # 1s, 2s, 4s, ... (base configurable by passing a number)
    retry_backoff_max=600,     # cap at 10 minutes
    retry_jitter=True,         # randomize to avoid thundering herd (default True)
    retry_kwargs={"max_retries": 8},
    acks_late=True,
)
def sync_to_crm(self, customer_id: int) -> None:
    resp = requests.post(CRM_URL, json=payload(customer_id), timeout=10)
    if resp.status_code == 429:
        # explicit retry honoring the partner's Retry-After
        raise self.retry(countdown=int(resp.headers.get("Retry-After", 30)))
    resp.raise_for_status()
```

**Trade-offs and pitfalls:**

- `autoretry_for=(Exception,)` retries bugs too (a `KeyError` will fail identically 8 times). List transient exceptions only.
- Default `max_retries` is 3; `None` means retry forever, which is how poison tasks are born.
- A retry is a *new message* with a countdown, so it goes through the ETA path (see the visibility timeout note in [Reliability](./04-reliability.md)).
- Retrying non-idempotent side effects multiplies them.

**Remember:** Retry transient errors only, with backoff, jitter and a cap.

## Q26. Soft and hard time limits stop tasks that hang

A hung task holds a worker slot forever: stuck socket, infinite loop, deadlock. `soft_time_limit` raises `SoftTimeLimitExceeded` inside the task so it can clean up; `time_limit` (hard) kills the process and replaces it. Always set both, with the hard limit a bit above the soft one.

**Example:**

```python
from celery.exceptions import SoftTimeLimitExceeded

@app.task(soft_time_limit=120, time_limit=150)
def render_pdf(report_id: int) -> str:
    tmp = make_tempdir()
    try:
        return do_render(report_id, tmp)
    except SoftTimeLimitExceeded:
        mark_report_failed(report_id, reason="timeout")
        raise
    finally:
        cleanup(tmp)
```

```python
# global defaults
task_soft_time_limit = 300
task_time_limit = 330
```

**Trade-offs and pitfalls:**

- Time limits rely on signals and are fully supported in the prefork pool; check your pool and platform.
- Soft limits cannot interrupt a blocking C call; the hard limit is the backstop.
- Also set client-level timeouts (HTTP, DB statement timeouts). Time limits are the last line of defense, not the first.
- A hard kill with `task_reject_on_worker_lost=True` may requeue the task; make sure it does not loop.

**Remember:** Every network call has a timeout, and every task has soft and hard limits.

## Q27. Dead-letter patterns keep permanently failed tasks for inspection and replay

When retries are exhausted, you need the failure to go somewhere a human or process can look at, not just a log line. Options: dead-letter on the broker (RabbitMQ DLX), a "failed tasks" table written from a failure hook, or both.

**Example:**

```python
from kombu import Exchange, Queue
from celery.exceptions import Reject

task_queues = [
    Queue(
        "payments",
        Exchange("payments"),
        routing_key="payments",
        queue_arguments={
            "x-dead-letter-exchange": "dlx",
            "x-dead-letter-routing-key": "payments.dead",
        },
    ),
    Queue("payments.dead", Exchange("dlx"), routing_key="payments.dead"),
]

@app.task(bind=True, acks_late=True)
def settle(self, payment_id: int) -> None:
    try:
        do_settle(payment_id)
    except PermanentError as exc:
        # requeue=False -> broker dead-letters the message (RabbitMQ)
        raise Reject(str(exc), requeue=False)

# Application-level record of final failures (works with any broker)
from celery.signals import task_failure

@task_failure.connect
def record_failure(sender=None, task_id=None, exception=None, args=None, kwargs=None, **_):
    FailedTask.objects.create(task=sender.name, task_id=task_id, args=args, error=repr(exception))
```

**Trade-offs and pitfalls:**

- Broker DLX only triggers on reject/nack without requeue (or TTL/length/delivery-limit); a normal raised exception is acked as a failure and never reaches the DLX.
- A DLQ nobody watches is a black hole: alert on DLQ depth, and build a replay tool.
- Replaying requires the task to still be idempotent and compatible with current code.

**Remember:** Final failures must land somewhere visible, alertable and replayable.

## Q28. Poison tasks fail or crash every time and must be quarantined

A poison task is a message that can never succeed: malformed input, a record that crashes a native library, a payload too large for memory. With late ack plus requeue-on-worker-lost, it is redelivered, crashes the worker again, and can take down a whole fleet in a loop.

**How it works:**

- Detect: the same task id appearing repeatedly in logs, `WorkerLostError`, rising redelivery counts, workers restarting.
- Cap redeliveries: RabbitMQ quorum queues have a delivery limit and dead-letter after it; on Redis, track attempts in your DB or in the message headers.
- Quarantine: dead-letter, then fix data or code, then replay.

**Example:**

```python
@app.task(bind=True, acks_late=True, reject_on_worker_lost=True)
def process_upload(self, upload_id: int) -> None:
    attempts = Upload.objects.increment_attempts(upload_id)   # atomic UPDATE ... RETURNING
    if attempts > 3:
        Upload.objects.mark_quarantined(upload_id)
        return                                           # ack and stop the loop
    ...
```

**Trade-offs and pitfalls:**

- Counting attempts before the work means a crash still counts; that is the point.
- Run risky native processing (image decoding, PDF parsing) with memory limits and in dedicated queues so a crash loop is contained.

**Remember:** Anything that can be redelivered needs a maximum delivery count.

## Q29. Separate "retryable", "permanent" and "unknown" failures in task code

Senior answers classify errors. Retryable (timeouts, 5xx, 429, deadlocks) get backoff. Permanent (validation errors, 4xx, missing records) fail fast, record a reason and do not retry. Unknown exceptions are bugs: fail, alert, keep the payload for replay after a fix.

**Example:**

```python
class Retryable(Exception): ...
class Permanent(Exception): ...

@app.task(bind=True, autoretry_for=(Retryable,), retry_backoff=True, retry_kwargs={"max_retries": 6})
def deliver_webhook(self, delivery_id: int) -> None:
    d = WebhookDelivery.objects.get(pk=delivery_id)
    resp = post(d.url, d.body, timeout=5)
    if resp.status_code >= 500 or resp.status_code == 429:
        raise Retryable(resp.status_code)
    if resp.status_code >= 400:
        d.mark_failed(f"client error {resp.status_code}")
        return                                  # permanent, no retry
    d.mark_delivered()
```

**Trade-offs and pitfalls:**

- A missing DB row right after enqueue is often a race with an uncommitted transaction, not a permanent error; fix with enqueue-on-commit ([Production patterns](./10-production-patterns.md)).
- Record the final state in the domain model so users and support can see it.

**Remember:** Classify first: retry transient, fail permanent fast, alert on unknown.

## References

- [Celery documentation: tasks, retries and time limits](https://docs.celeryq.dev/en/stable/)
- [RabbitMQ documentation: dead lettering](https://www.rabbitmq.com/docs)
- [RabbitMQ dead-lettering and retries (this site)](../rabbitmq/04-dead-lettering-and-retries.md)
