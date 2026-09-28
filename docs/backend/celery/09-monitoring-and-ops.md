---
sidebar_label: "Monitoring and Operations"
description: "Observing Celery with Flower and events, alerting on queue depth, graceful shutdown, and running and autoscaling workers in Docker and Kubernetes."
---

# Monitoring and Operations (Q34-Q37)

> **Reviewed:** 2026-09 · **Level:** Senior · **Type:** Foundational

## Q34. Monitor queues, workers and tasks as three separate layers

Good Celery monitoring answers three questions: is work piling up (queue depth and age of oldest message), are workers healthy (alive, consuming, not restart-looping), and are tasks succeeding in reasonable time (failure rate, retries, runtime). Flower gives a live view from worker events; production alerting should come from metrics.

**How it works:**

| Layer | Signals | Source |
|---|---|---|
| Queues | Depth, oldest message age, publish vs consume rate, unacked | RabbitMQ management / Prometheus plugin, Redis `LLEN` on the queue key |
| Workers | Heartbeats, active tasks, restarts, memory | `celery inspect`, Flower, container metrics |
| Tasks | Success/failure counts, retries, runtime percentiles | Worker events, task signals exported to Prometheus/OpenTelemetry |

**Example:**

```bash
celery -A proj worker -E                 # send task events (or worker_send_task_events = True)
celery -A proj events                    # curses monitor
celery -A proj inspect active            # what is running now
celery -A proj inspect reserved          # what is prefetched
celery -A proj inspect ping
celery -A proj flower --port=5555        # web UI (protect it: it can revoke tasks)
```

**Trade-offs and pitfalls:**

- Flower keeps state in memory by default; it is a debugging tool, not your metrics store.
- Events add broker traffic; enable them deliberately.
- Queue *age* is often a better alert than depth: 10k tiny tasks may be fine, 50 tasks waiting 20 minutes is not.

**Remember:** Alert on backlog age and failure rate; use Flower to investigate.

## Q35. Queue depth alerts should be per queue and tied to an SLO

"Queue > 1000" is not meaningful on its own. Tie thresholds to the latency promise of each queue: emails should start within a minute, reports within 15 minutes. Alert when the oldest message exceeds the promise, or when depth grows continuously while consumers are present (throughput problem) or with zero consumers (outage).

**Example:**

- `email` queue: page if oldest message older than 2 minutes for 5 minutes.
- `heavy` queue: ticket if depth grows steadily for 30 minutes.
- Any queue: page if consumer count is 0.
- DLQ: alert on any growth.

**Trade-offs and pitfalls:**

- With Redis, delayed (`eta`) tasks are not in the list; they sit in worker memory and the unacked structure, so depth alone misses them.
- With RabbitMQ, watch `messages_unacknowledged` too: high unacked with low throughput suggests stuck tasks or too much prefetch.

**Remember:** Every queue needs a latency promise and an alert on breaking it.

## Q36. Graceful shutdown lets in-flight tasks finish before a worker exits

On `SIGTERM` a Celery worker does a warm shutdown: it stops consuming new messages and waits for running tasks to complete. A second signal or `SIGQUIT` forces a cold shutdown. In containers, the orchestrator sends `SIGTERM` and then `SIGKILL` after a grace period, so the grace period must exceed your longest normal task, or you must rely on late ack plus idempotency for the rest.

**Example:**

```yaml
# Kubernetes worker Deployment (excerpt)
spec:
  template:
    spec:
      terminationGracePeriodSeconds: 600   # > typical longest task
      containers:
        - name: worker
          image: registry.example.com/app:1.42.0
          command: ["celery", "-A", "proj", "worker", "-Q", "default", "-c", "4", "--prefetch-multiplier=1"]
          resources:
            requests: { cpu: "1", memory: "1Gi" }
            limits: { memory: "2Gi" }
```

```dockerfile
# Make celery PID 1 (exec form) so it receives SIGTERM directly
CMD ["celery", "-A", "proj", "worker", "--loglevel=info"]
```

**Trade-offs and pitfalls:**

- Shell-form `CMD` wraps Celery in `/bin/sh`, which may not forward signals; use exec form or an init like `tini`.
- Tasks longer than any reasonable grace period should be checkpointed or split.
- Liveness probes for workers are tricky; `celery inspect ping` against the node name is common, but make it cheap and tolerant.

**Remember:** SIGTERM = finish current work; set the grace period above your longest task.

## Q37. Autoscale workers on queue length, not CPU

CPU is a poor signal for queue consumers: I/O-bound workers idle on CPU while the backlog explodes, and CPU-bound workers peg CPU regardless of backlog. Scale on the thing you care about: messages waiting per worker. In Kubernetes, KEDA has scalers for RabbitMQ queues and Redis lists and can scale a Deployment to zero and back.

**Example:**

```yaml
# KEDA ScaledObject (excerpt): scale "heavy" workers on RabbitMQ queue length
apiVersion: keda.sh/v1alpha1
kind: ScaledObject
metadata:
  name: celery-heavy
spec:
  scaleTargetRef:
    name: celery-heavy-worker
  minReplicaCount: 0
  maxReplicaCount: 20
  triggers:
    - type: rabbitmq
      metadata:
        queueName: heavy
        mode: QueueLength
        value: "10"               # target messages per replica
      authenticationRef:
        name: rabbitmq-auth
```

**Trade-offs and pitfalls:**

- Scale-down sends SIGTERM; combine with graceful shutdown and late ack.
- Prefetch hides backlog inside workers; with a high prefetch, queue length undercounts work.
- Cap max replicas by downstream limits (DB connections, partner rate limits).
- Celery's own `--autoscale` adjusts processes inside one worker; container autoscaling is usually easier to reason about in Kubernetes.

**Remember:** Queue length drives replicas; downstream capacity caps them.

## References

- [Celery documentation: monitoring and management](https://docs.celeryq.dev/en/stable/)
- [RabbitMQ documentation: monitoring](https://www.rabbitmq.com/docs)
- [Orchestration (this site)](../../devops/orchestration/index.md)
- [RabbitMQ security and operations (this site)](../rabbitmq/09-security-and-ops.md)
