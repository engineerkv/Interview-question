---
sidebar_position: 100
sidebar_label: Cheatsheet
description: "One-page Celery revision sheet: key settings, commands, failure modes and interview one-liners."
---

# Celery Cheatsheet (Q1-Q41)

> **Reviewed:** 2026-09 · **Level:** Senior · **Type:** Foundational

## Production baseline config

```python
app.conf.update(
    broker_url="amqp://app:secret@rabbitmq:5672/celery",
    result_backend="redis://redis:6379/1",
    task_serializer="json",
    accept_content=["json"],
    task_ignore_result=True,            # opt in per task
    result_expires=3600,
    task_acks_late=True,                # at-least-once
    task_reject_on_worker_lost=True,    # requeue if child dies (cap redeliveries!)
    worker_prefetch_multiplier=1,       # long/uneven tasks
    task_soft_time_limit=300,
    task_time_limit=330,
    worker_max_tasks_per_child=500,
    task_default_queue="default",
    task_routes={"notifications.*": {"queue": "email"}, "media.*": {"queue": "heavy"}},
    # Redis broker only:
    # broker_transport_options={"visibility_timeout": 6 * 3600},
)
```

## Key settings

| Setting | Default behavior | Why you change it |
|---|---|---|
| `task_acks_late` | Ack before run | Survive worker crashes (Q13) |
| `task_reject_on_worker_lost` | Ack and fail on lost child | Requeue instead (Q14) |
| `worker_prefetch_multiplier` | 4 | 1 for long tasks, fairness, priorities (Q11) |
| `visibility_timeout` (Redis) | 1 hour | Must exceed longest task/ETA (Q16) |
| `task_time_limit` / `task_soft_time_limit` | None | Stop hung tasks (Q26) |
| `worker_max_tasks_per_child` | None | Contain memory leaks (Q17) |
| `result_expires` | 1 day | Control backend growth (Q6) |
| `task_ignore_result` | False | Skip writes nobody reads (Q7) |

## Commands

```bash
celery -A proj worker -Q default -c 4 -n default@%h --prefetch-multiplier=1
celery -A proj worker -P gevent -c 200 -Q email
celery -A proj beat
celery -A proj inspect active | reserved | scheduled | ping
celery -A proj control revoke <task_id>
celery -A proj purge -Q default        # destructive
celery -A proj flower
```

## Failure modes and fixes

| Symptom | Likely cause | Fix |
|---|---|---|
| Task ran twice | Late ack + crash, Redis visibility timeout, retries, duplicate Beat | Idempotency; raise timeout; one Beat |
| Task never ran | Routed to unconsumed queue; early ack + crash; expired | Check routes and consumers; late ack |
| `DoesNotExist` in worker | Enqueued before commit | `transaction.on_commit` / outbox |
| One worker busy, others idle | Prefetch hoarding | Prefetch 1, `-O fair` |
| Worker restart loop | Poison task + requeue | Delivery limit, quarantine |
| Random DB/SSL errors in children | Clients created before fork | `worker_process_init` |
| Channel closed after 30 min (RabbitMQ) | `consumer_timeout` on long unacked delivery | Raise timeout or avoid long ETAs |

## One-liners

- Early ack loses work on crash; late ack duplicates it. Make tasks idempotent.
- Send IDs, not objects. JSON, never pickle from untrusted brokers.
- Separate queues for isolation; priorities only reorder.
- Exactly one Beat. `Recreate` rollouts.
- Retry transient errors with backoff and jitter; cap retries; dead-letter the rest.
- Scale workers on queue length; SIGTERM grace period above longest task.
- Fork first, connect second.
- Celery runs jobs; Kafka keeps event logs; Temporal runs workflows.

## Where to go next

- [Overview](./index.md) · [Question index](./question-index.md)
- [RabbitMQ](../rabbitmq/index.md) · [Messaging systems overview](../architecture/05-messaging-systems.md)
