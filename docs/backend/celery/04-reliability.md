---
sidebar_label: "Reliability"
description: "Early vs late acknowledgement, worker-lost handling, idempotent task design, the Redis visibility timeout trap, and recycling workers."
---

# Reliability (Q13-Q17)

> **Reviewed:** 2026-09 · **Level:** Senior · **Type:** Foundational

## Q13. `task_acks_late` moves the ack from "before execution" to "after execution"

By default Celery acknowledges a message just before running the task (early ack). If the worker is killed mid-task, the broker already considers the message done, so the task is lost: at-most-once. With `task_acks_late=True`, the ack happens after the task returns, so a crash causes the broker to redeliver: at-least-once. Late ack is the right default for anything important, but only if the task is idempotent.

**How it works:**

| Setting | Crash during execution | Guarantee |
|---|---|---|
| Early ack (default) | Task lost | At most once |
| `task_acks_late=True` | Message redelivered to another worker | At least once (duplicates possible) |

**Example:**

```python
app.conf.update(
    task_acks_late=True,
    task_reject_on_worker_lost=True,
    worker_prefetch_multiplier=1,
)

# or per task
@app.task(acks_late=True)
def charge_invoice(invoice_id: int) -> None:
    ...
```

**Trade-offs and pitfalls:**

- Late ack does not mean "ack only on success": by default a task that *raises* is still acked (`task_acks_on_failure_or_timeout=True`). Late ack protects against crashes, not exceptions. Use retries for exceptions.
- With late ack, the message stays unacked for the whole run, which is where broker timeouts bite (Q16).

**Remember:** Early ack loses work on crash; late ack duplicates it. Choose, then design for it.

## Q14. `task_reject_on_worker_lost` decides what happens when the child process dies

Even with late ack, if a prefork child process is killed (OOM killer, segfault in a C extension, `SIGKILL`), Celery by default acks the message and marks the task failed with `WorkerLostError`, to avoid a crash loop. Setting `task_reject_on_worker_lost=True` makes Celery reject and requeue the message instead, so another worker retries it.

**Trade-offs and pitfalls:**

- A task that *always* kills its process (a poison task, like a malformed image that crashes a native library) now loops forever. Protect with a delivery limit (RabbitMQ quorum queues have one), a retry counter in your DB, or dead-lettering. See [Retries and failures](./07-retries-timeouts-failures.md).
- Pair with `acks_late=True`; on its own it has no effect.

**Remember:** Requeue on worker loss only if you also cap how many times a message can come back.

## Q15. Idempotent tasks make at-least-once delivery safe

Idempotent means running a task twice has the same effect as running it once. Since late acks, retries, broker failovers and visibility timeouts can all cause duplicates, you design for it rather than hope. The techniques: check-then-act on a state column, unique constraints, idempotency keys passed to external APIs, and upserts instead of inserts.

**Example:**

```python
@app.task(bind=True, acks_late=True)
def charge_order(self, order_id: int) -> None:
    with transaction.atomic():
        order = Order.objects.select_for_update().get(pk=order_id)
        if order.status == "paid":
            return                                   # duplicate delivery: no-op
        charge = payments.charge(
            amount=order.total,
            idempotency_key=f"order-{order_id}",     # provider dedupes retries too
        )
        order.status, order.charge_id = "paid", charge.id
        order.save(update_fields=["status", "charge_id"])
```

**Trade-offs and pitfalls:**

- "Check a Redis key, then do the work" has a race; use a DB lock/unique constraint or an atomic `SET NX` with an expiry that exceeds task runtime.
- External side effects (email, SMS) are hard to make idempotent; record "sent" before or atomically with the call, and accept a small duplicate window, or use a provider idempotency key.
- A deterministic `task_id` helps correlation but does not deduplicate.

**Remember:** Assume every task runs twice; make the second run a no-op.

## Q16. With Redis, tasks that outlive `visibility_timeout` get executed twice

The Redis transport has no broker-side consumer tracking. When a worker takes a message, Kombu keeps it in an "unacked" structure with a timestamp. If it is not acked within `visibility_timeout` (default one hour), it is restored to the queue and another worker runs it, while the first is still running. This hits long tasks with late ack, and especially `countdown`/`eta` tasks, which are reserved immediately and held until due.

**How it works:**

- `eta` two hours in the future + visibility timeout one hour = the message is redelivered after one hour, and later both copies execute.
- Long task (90 minutes) with `acks_late` = a second worker starts it at the 60-minute mark.

**Example:**

```python
broker_transport_options = {"visibility_timeout": 6 * 3600}  # > longest task and longest eta
result_backend_transport_options = {"visibility_timeout": 6 * 3600}
```

**Trade-offs and pitfalls:**

- Raising the timeout also delays recovery of tasks from genuinely crashed workers.
- Better fixes: avoid long ETAs (schedule via DB + Beat), split long tasks into chunks, or use RabbitMQ.
- RabbitMQ has an analogous limit: `consumer_timeout` (defaults to 30 minutes in modern versions) closes the channel if a delivery stays unacked too long. Long ETA tasks and long late-acked tasks need it raised, or a design change.

> **Interview tip:** If a candidate says "we saw random duplicate emails with Celery on Redis", the visibility timeout is the first thing to check.

**Remember:** Every unacked message has a clock on it; know which broker's clock you are racing.

## Q17. `worker_max_tasks_per_child` recycles processes to contain leaks

Long-lived Python processes accumulate memory: leaky C extensions, caches, fragmented heaps, ML models loaded lazily. `worker_max_tasks_per_child` replaces a prefork child after N tasks; `worker_max_memory_per_child` (in KiB) replaces it after the task that pushes it over the resident memory limit.

**Example:**

```python
worker_max_tasks_per_child = 200
worker_max_memory_per_child = 500_000   # ~500 MB, checked after each task
```

**Trade-offs and pitfalls:**

- Recycling costs a fork plus re-initialization (DB connections, model loading); too low a limit kills throughput.
- It is a mitigation, not a fix; still profile the leak.
- The memory limit is checked after a task finishes, so a single huge task can still OOM the container. Set container limits with headroom.

**Remember:** Recycle children to bound memory drift, but find the leak.

## References

- [Celery documentation: tasks and configuration](https://docs.celeryq.dev/en/stable/)
- [RabbitMQ reliability guide](https://www.rabbitmq.com/docs)
- [RabbitMQ acks and confirms (this site)](../rabbitmq/03-reliability.md)
