---
sidebar_label: "Routing, Queues and Priorities"
description: "Routing Celery tasks to dedicated queues, isolating email, heavy and AI workloads, and how priorities really behave on RabbitMQ and Redis."
---

# Routing, Queues and Priorities (Q18-Q21)

> **Reviewed:** 2026-09 · **Level:** Senior · **Type:** Foundational

## Q18. `task_routes` maps tasks to queues so workloads stay isolated

Without routing, every task goes to the default queue (`celery`), so a burst of slow report jobs delays password-reset emails. `task_routes` sends tasks to named queues by task name or glob pattern, and workers subscribe only to the queues they should handle.

**Example:**

```python
# celeryconfig.py
task_default_queue = "default"
task_create_missing_queues = True   # default: auto-declare queues named in routes

task_routes = {
    "notifications.*": {"queue": "email"},
    "media.tasks.resize_image": {"queue": "heavy"},
    "ai.tasks.*": {"queue": "ai"},
}
```

```bash
celery -A proj worker -Q email -n email@%h -P gevent -c 100
celery -A proj worker -Q heavy -n heavy@%h -c 2 --prefetch-multiplier=1
celery -A proj worker -Q ai    -n ai@%h    -P solo
```

**Trade-offs and pitfalls:**

- A route to a queue nobody consumes means tasks pile up silently. Alert on queue depth per queue.
- Routing at call time (`apply_async(queue="x")`) overrides config and is easy to forget in code review; prefer central routes.
- Keep the queue list short; every queue needs an owner, alert and scaling policy.

**Remember:** Route by workload shape (latency-sensitive, heavy, bursty), not by team or module.

## Q19. Dedicated queues for email, heavy and AI jobs let you tune each one

Different job classes need different settings. Latency-sensitive work (emails, notifications) wants many cheap concurrent slots. Heavy CPU work wants few slots, prefetch 1, and generous memory. AI/GPU inference often wants one task per process or per GPU, long time limits, and scaling on queue length since GPUs are expensive.

**How it works:**

| Queue | Pool / concurrency | Prefetch | Time limits | Scale on |
|---|---|---|---|---|
| `email` | gevent, high | default | short | queue depth |
| `default` | prefork, cores | default | moderate | queue depth / CPU |
| `heavy` | prefork, low | 1 | long, with soft limit | queue depth |
| `ai` | solo or prefork 1 per GPU | 1 | long | queue depth, GPU availability |

**Example:**

```python
@app.task(queue="ai", soft_time_limit=600, time_limit=660, acks_late=True)
def summarize_document(doc_id: int) -> None:
    ...
```

**Trade-offs and pitfalls:**

- AI tasks often load a large model; load it once per process in `worker_process_init` (see [Production patterns](./10-production-patterns.md)).
- GPU workers idle are expensive; consider scale-to-zero with KEDA ([Monitoring and ops](./09-monitoring-and-ops.md)).

**Remember:** Queues are the unit of tuning and scaling.

## Q20. Priorities work differently on RabbitMQ and Redis

RabbitMQ supports priority natively on classic queues declared with `x-max-priority`; higher numbers are higher priority. Kombu's Redis transport emulates priority by splitting each queue into several lists (priority steps) and polling them in order; lower numbers are higher priority on Redis. Mixing these assumptions is a classic bug.

**Example:**

```python
from kombu import Queue

# RabbitMQ
task_queues = [
    Queue("default", queue_arguments={"x-max-priority": 10}),
]
task_default_priority = 5
send_sms.apply_async(args=[uid], priority=9)   # higher = sooner on RabbitMQ

# Redis
broker_transport_options = {
    "priority_steps": list(range(10)),
    "sep": ":",
    "queue_order_strategy": "priority",
}
```

**Trade-offs and pitfalls:**

- Prefetch undermines priority: messages already reserved by a worker will run before a new high-priority message. Use `worker_prefetch_multiplier=1` and `acks_late`.
- Priorities only reorder *within* a queue; they do not give capacity guarantees.
- On RabbitMQ, `x-max-priority` is fixed at declaration; changing it means a new queue. Check the current RabbitMQ docs for priority support per queue type (quorum queue priority support is newer and simpler than classic).

**Remember:** Separate queues give isolation; priorities only reorder a single queue.

## Q21. Prefer separate queues over priorities for most "urgent vs bulk" problems

When an interviewer asks "how do you make password resets fast while newsletters are sending?", the strongest answer is a separate queue with its own workers. That guarantees capacity for the urgent class regardless of backlog. Priorities are a finer tool for "mostly the same workload, some items slightly more urgent".

**Example:** Newsletter fan-out publishes 500k tasks to `bulk_email`, consumed by two small workers with a rate limit. Transactional emails go to `email`, consumed by always-on workers. A newsletter burst can never delay a password reset.

**Trade-offs and pitfalls:**

- Separate queues cost idle capacity; autoscaling reduces that.
- Starvation is still possible inside priority queues if high-priority traffic is constant.

<details>
<summary>Follow-up questions</summary>

- *How do you drain one tenant's flood without hurting others?* Per-tenant rate limits in task code, or shard tenants across queues; for strict fairness, a scheduler that pulls from per-tenant backlogs in the DB.
- *How do you move tasks from one queue to another?* Update routes and deploy; for existing backlog, temporarily point a worker at the old queue, or use a small script (or RabbitMQ Shovel) that consumes and republishes.

</details>

**Remember:** Isolation first, priority second.

## References

- [Celery documentation: routing tasks](https://docs.celeryq.dev/en/stable/)
- [RabbitMQ documentation: priority queues](https://www.rabbitmq.com/docs)
- [RabbitMQ exchanges and bindings (this site)](../rabbitmq/02-exchanges-queues-bindings.md)
