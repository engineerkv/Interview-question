---
sidebar_label: "Workers and Concurrency"
description: "Celery execution pools (prefork, threads, gevent, eventlet, solo), sizing concurrency for CPU vs I/O work, and prefetch behavior."
---

# Workers and Concurrency (Q9-Q12)

> **Reviewed:** 2026-09 · **Level:** Senior · **Type:** Foundational

## Q9. The execution pool decides how a worker runs tasks in parallel

A Celery worker is a main process that consumes messages and hands them to an execution pool. The pool type is the most important performance choice you make: it determines whether tasks run in separate processes, threads, or green threads.

**How it works:**

| Pool | Flag | Parallelism model | Best for | Caveats |
|---|---|---|---|---|
| prefork (default) | `-P prefork` | Child processes (multiprocessing) | CPU-bound, mixed, anything using C extensions | Memory per child; fork-safety of clients |
| threads | `-P threads` | OS threads | I/O-bound code that releases the GIL | GIL limits CPU work |
| gevent / eventlet | `-P gevent` | Green threads, cooperative | Very high I/O concurrency (HTTP calls, webhooks) | Needs monkey-patched, cooperative libraries; one blocking call stalls all |
| solo | `-P solo` | One task at a time in the main process | Debugging, or one-task-per-container designs | No parallelism; remote control blocked while a task runs |

**Example:**

```bash
# CPU-heavy (image resize, PDF render): one process per core
celery -A proj worker -P prefork -c 4 -Q heavy

# I/O-heavy (call 3rd-party APIs): many green threads
celery -A proj worker -P gevent -c 200 -Q webhooks

# Kubernetes "one task per pod" style
celery -A proj worker -P solo -Q ai_inference
```

**Trade-offs and pitfalls:**

- Mixing CPU and I/O tasks on one worker leads to bad sizing for both; split them by queue.
- gevent with a non-cooperative driver (e.g., a blocking DB client that is not patched) serializes everything silently.
- Time limits are fully enforced in prefork; verify behavior before relying on them with other pools.

**Remember:** Pick the pool from the workload: processes for CPU, green threads for I/O.

## Q10. Size concurrency from the bottleneck, not from a formula

Default concurrency is the number of CPUs on the machine (or container limit visible to Python, which is not always correct in containers). For CPU-bound work, go near the core count; going higher just adds context switching. For I/O-bound work, concurrency can be far higher than cores because tasks mostly wait. The real limit is usually downstream: DB connections, API rate limits, memory.

**How it works:**

- CPU-bound: `concurrency ≈ cores available to the container`.
- I/O-bound: raise concurrency until latency or downstream error rates degrade; cap with connection pool sizes and rate limits.
- Total downstream pressure = workers × concurrency. Ten pods × 20 processes = 200 possible DB connections.

**Example:**

```python
# per-task rate limit (per worker instance, not global)
@app.task(rate_limit="10/s")
def call_partner_api(item_id: int) -> None:
    ...
```

```bash
# Autoscale child processes between 2 and 10 on a single worker
celery -A proj worker --autoscale=10,2
```

**Trade-offs and pitfalls:**

- `rate_limit` is enforced per worker, so N workers allow N times the rate. Global limits need a shared token bucket (e.g., Redis) or a single dedicated worker.
- In Kubernetes, set `-c` explicitly; CPU detection may see the node's cores rather than your CPU limit.
- Memory, not CPU, often caps prefork concurrency for ML or image workloads.

**Remember:** Concurrency × replicas must fit what the database and partners can take.

## Q11. The prefetch multiplier controls how many messages each worker reserves ahead

Workers reserve messages before they are ready to run them to cut round-trips. The number reserved is `worker_prefetch_multiplier × concurrency` (default multiplier is 4). For many short tasks that is great for throughput. For long or uneven tasks, prefetching causes one worker to hoard messages while others sit idle, and those messages are stuck behind a slow task.

**Example:**

```python
# Long-running or uneven tasks: take only what you can run
worker_prefetch_multiplier = 1
task_acks_late = True     # with late ack, a reserved-but-running task holds its slot
```

```bash
# Fair scheduling across prefork children (avoids sending tasks to busy children)
celery -A proj worker -O fair
```

**Trade-offs and pitfalls:**

- `worker_prefetch_multiplier = 0` means unlimited prefetch, which is rarely what you want.
- Prefetched messages are unacked; with Redis they count against the visibility timeout, with RabbitMQ against `consumer_timeout`.
- ETA/countdown tasks are fetched regardless of prefetch limits and held in memory, so thousands of delayed tasks can bloat a worker.
- Prefetch defeats priorities: a high-priority message cannot jump ahead of messages already reserved.

**Remember:** Short tasks like big prefetch; long tasks need prefetch 1.

## Q12. One worker per queue class beats one giant worker

A single worker consuming every queue means one slow job type can starve others and you cannot scale them independently. The production pattern is dedicated worker deployments per workload: `default`, `email`, `heavy`, `ai`, each with its own pool, concurrency, prefetch, memory limits and autoscaling rule.

**Example:**

```bash
celery -A proj worker -n default@%h -Q default -c 8
celery -A proj worker -n email@%h   -Q email   -P gevent -c 100
celery -A proj worker -n heavy@%h   -Q heavy   -c 2 --prefetch-multiplier=1
```

**Trade-offs and pitfalls:**

- More deployments to operate; keep configuration in one place (Helm values, Compose profiles).
- Give each worker a unique node name (`-n name@%h`) or remote control and monitoring get confused.
- Queue design is covered in [Routing, queues and priorities](./05-routing-queues-priorities.md).

**Remember:** Separate queues and workers per workload so they scale and fail independently.

## References

- [Celery documentation: workers guide](https://docs.celeryq.dev/en/stable/)
- [RabbitMQ prefetch and flow control](../rabbitmq/06-prefetch-flow-control.md)
