---
sidebar_label: "RabbitMQ vs Kafka, SQS and Redis"
description: "A decision table and a crisp interview answer for choosing between RabbitMQ, Kafka, Amazon SQS and Redis."
---

# RabbitMQ vs Kafka, SQS and Redis (Q35-Q37)

> **Reviewed:** 2026-09 · **Level:** Senior · **Type:** Foundational

The broad queue-vs-stream comparison lives in the [messaging systems overview (Q66-Q67)](../architecture/05-messaging-systems.md). This file focuses on the decision itself and how to say it in an interview.

## Q35. Choose by consumption model first: smart broker queues vs replayable logs

RabbitMQ is a smart broker: it routes, tracks per-message acks, redelivers, dead-letters and removes messages once consumed. Kafka is a distributed log: messages are retained, consumers track offsets and can replay, and ordering is per partition. SQS is a managed queue with visibility timeouts and no servers to run. Redis (lists or Streams) is fast and simple but its durability depends on how you run it.

**How it works:**

| Dimension | RabbitMQ | Kafka | Amazon SQS | Redis (lists / Streams) |
|---|---|---|---|---|
| Model | Queues + exchanges; consume-and-remove (Streams add a log) | Partitioned, retained log | Managed queue | In-memory data structures |
| Routing | Rich (direct, topic, fanout, headers) | By topic and partition key | None (use SNS/EventBridge for fan-out) | Manual |
| Replay | Streams only | Native, by offset | No | Streams, bounded by memory |
| Ordering | Per queue, single consumer | Per partition | FIFO queues (per message group) | Per list/stream |
| Per-message ack/retry/DLQ | Native (acks, DLX, delivery limit) | Consumer handles; commit offsets | Native (visibility timeout, redrive to DLQ) | Manual (Streams have pending entries) |
| Ops | Run a cluster (or managed offering) | Run a cluster (or managed) | Fully managed | Often already running; persistence is configuration |
| Sweet spot | Task queues, commands, complex routing, RPC | Event streaming, analytics, event sourcing, many independent consumers | AWS-native decoupling, serverless | Lightweight jobs, caching-adjacent queues |

**Trade-offs and pitfalls:**

- Kafka as a job queue is awkward: no per-message retry/delay, and a slow message blocks its partition.
- RabbitMQ as a long-term event store is awkward outside Streams: queues are meant to be short.
- SQS standard queues are at-least-once without strict ordering; FIFO queues add ordering and deduplication within limits described in AWS docs.

**Remember:** Commands and jobs go to queues; facts and history go to logs.

## Q36. Give a two-sentence answer, then justify with requirements

**Example interview answer:**

> "For background jobs and commands where each message should be processed once by one worker, with retries and dead-lettering, I'd use RabbitMQ, or SQS if we're on AWS and don't want to run brokers. For domain events that several services consume independently and that we may need to replay, like order events feeding analytics and search, I'd use Kafka. Redis is fine for lightweight jobs if we accept its durability trade-offs."

Then tie it to requirements the interviewer gave: throughput, replay, ordering, team skills, cloud, cost of operating a cluster.

**Trade-offs and pitfalls:**

- Don't claim one is "faster" without a workload; throughput depends heavily on message size, persistence, acks and replication settings.
- Mention the hybrid: many systems use both (Kafka for events, RabbitMQ or SQS for work).

**Remember:** Lead with the use case, not the brand.

## Q37. Scenario questions test whether you map requirements to guarantees

| Scenario | Good choice | Reason |
|---|---|---|
| Send transactional emails and resize images from a Django app | RabbitMQ + Celery (or SQS) | Job queue, retries, DLQ, per-queue workers |
| Clickstream of every page view for analytics, retained for days | Kafka | High-volume log, replay, many consumers |
| Order events consumed by five services, some added later that need history | Kafka (or RabbitMQ Streams in a RabbitMQ shop) | Replay from offset |
| Fully serverless on AWS, Lambda consumers | SQS (+ SNS or EventBridge for fan-out) | Managed, native triggers |
| Route messages by region and severity to different teams | RabbitMQ topic exchange | Rich routing |
| Small internal tool with a few background jobs, Redis already present | Redis-backed queue (RQ, Celery on Redis) | Simplicity |

**Trade-offs and pitfalls:**

- Managed offerings (Amazon MQ for RabbitMQ, managed Kafka services) change the ops argument; mention them when "we don't want to run clusters" comes up.
- Compliance or on-prem requirements can rule out managed cloud services.

**Remember:** Map each requirement (replay, routing, ordering, ops) to the system that gives it natively.

## References

- [RabbitMQ documentation](https://www.rabbitmq.com/docs)
- [Messaging systems overview](../architecture/05-messaging-systems.md)
- [AWS cloud architecture (this site)](../../devops/cloud/01-aws-cloud-architecture.md)
- [Celery: when Celery is the wrong tool](../celery/10-production-patterns.md)
