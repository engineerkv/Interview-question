---
sidebar_position: 0
sidebar_label: "Question Index"
description: "Every Celery interview question in this section, grouped by topic with links."
---

# Celery Question Index (Q1-Q41)

> **Reviewed:** 2026-09 · **Level:** Senior · **Type:** Foundational

## [Fundamentals](./01-fundamentals.md)

- Q1. Celery is a distributed task queue that moves slow work out of the request path
- Q2. A task goes through publish, reserve, execute, acknowledge and store result
- Q3. Tasks should receive small, serializable identifiers, not rich objects
- Q4. `delay()`, `apply_async()` and signatures

## [Brokers and result backends](./02-brokers-and-backends.md)

- Q5. RabbitMQ vs Redis as broker
- Q6. The result backend stores task state and is optional
- Q7. Most fire-and-forget tasks should ignore results
- Q8. Planning for broker outages

## [Workers and concurrency](./03-workers-and-concurrency.md)

- Q9. Execution pools: prefork, threads, gevent/eventlet, solo
- Q10. Sizing concurrency for CPU vs I/O work
- Q11. The prefetch multiplier
- Q12. One worker deployment per queue class

## [Reliability](./04-reliability.md)

- Q13. `task_acks_late`: early vs late acknowledgement
- Q14. `task_reject_on_worker_lost`
- Q15. Idempotent tasks
- Q16. Redis `visibility_timeout` and duplicate execution
- Q17. `worker_max_tasks_per_child` and memory recycling

## [Routing, queues and priorities](./05-routing-queues-priorities.md)

- Q18. `task_routes` and queue isolation
- Q19. Dedicated queues for email, heavy and AI jobs
- Q20. Priorities on RabbitMQ vs Redis
- Q21. Separate queues vs priorities

## [Beat and scheduling](./06-beat-and-scheduling.md)

- Q22. Celery Beat publishes, workers execute
- Q23. The single-Beat problem
- Q24. Alternatives to Beat

## [Retries, timeouts and failures](./07-retries-timeouts-failures.md)

- Q25. `autoretry_for` with exponential backoff
- Q26. Soft and hard time limits
- Q27. Dead-letter patterns
- Q28. Poison tasks
- Q29. Classifying retryable, permanent and unknown failures

## [Workflows (canvas)](./08-workflows-canvas.md)

- Q30. Chains
- Q31. Groups and chords
- Q32. Never block on results inside a task
- Q33. Canvas vs durable orchestration

## [Monitoring and operations](./09-monitoring-and-ops.md)

- Q34. Monitoring queues, workers and tasks
- Q35. Queue depth alerts tied to SLOs
- Q36. Graceful shutdown in Docker and Kubernetes
- Q37. Autoscaling on queue length

## [Production patterns](./10-production-patterns.md)

- Q38. Django and FastAPI integration
- Q39. Fork safety: per-process clients via `worker_process_init`
- Q40. Enqueue after commit and the transactional outbox
- Q41. When Celery is the wrong tool
