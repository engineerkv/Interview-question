---
sidebar_position: 100
sidebar_label: Cheatsheet
description: "One-page RabbitMQ revision sheet: model, exchange types, reliability checklist, key arguments, metrics and one-liners."
---

# RabbitMQ Cheatsheet (Q1-Q41)

> **Reviewed:** 2026-09 · **Level:** Senior · **Type:** Foundational

## Model

Producer → exchange (routing key) → binding → queue → consumer (ack). Default exchange `""` routes by queue name. One TCP connection, many channels; one channel per thread.

## Exchange types

| Type | Routes by | Use |
|---|---|---|
| direct | Exact routing key | Job types, commands |
| topic | Pattern (`*` one word, `#` zero or more) | Events by domain/region/type |
| fanout | Nothing (all bound queues) | Broadcast, cache invalidation |
| headers | Header values, `x-match` all/any | Multi-attribute routing |

## Reliability checklist

1. Durable queue (quorum for important data).
2. Persistent messages (`delivery_mode=2`).
3. Publisher confirms; retry unconfirmed.
4. `mandatory` or alternate exchange for unroutable messages.
5. Manual consumer acks after work is done.
6. Prefetch bounded.
7. DLX + delivery limit + parking lot.
8. Idempotent consumers keyed by `message_id`.

## Queue arguments and policies

| Key | Purpose |
|---|---|
| `x-queue-type` | `classic`, `quorum`, `stream` |
| `x-dead-letter-exchange` / `-routing-key` | Dead-letter target |
| `x-message-ttl` / `expiration` property | Queue TTL / per-message TTL |
| `x-expires` | Delete idle queue |
| `x-max-length` + `x-overflow` | Cap + `drop-head` / `reject-publish` |
| `x-delivery-limit` | Quorum queue poison-message cap |
| `x-single-active-consumer` | Ordered, one active consumer |
| `x-max-priority` | Priority queue (classic) |
| `x-stream-offset` (consumer arg) | Where a stream consumer starts |

## Versions and HA facts

- RabbitMQ 4.0 removed classic mirrored queues. Use quorum queues (Raft, majority) for HA work queues.
- Streams (since 3.9): append-only, replayable, retention by size/age.
- Clusters: odd node counts on a LAN; Federation or Shovel across WAN.
- `consumer_timeout` closes channels holding unacked deliveries too long (30 minutes by default in modern versions).

## Ports

| Port | Use |
|---|---|
| 5672 / 5671 | AMQP / AMQP over TLS |
| 15672 | Management UI and HTTP API |
| 15692 | Prometheus metrics |
| 5552 | Stream protocol |

## Metrics to alert on

Ready messages growing, unacked stuck, zero consumers, low consumer utilisation with backlog, redelivery spikes, DLQ growth, memory/disk alarms, connection churn.

## Commands

```bash
rabbitmqctl list_queues name type messages_ready messages_unacknowledged consumers
rabbitmqctl set_policy NAME 'PATTERN' '{"dead-letter-exchange":"dlx"}' --apply-to queues
rabbitmqctl export_definitions /backup/defs.json
rabbitmq-plugins enable rabbitmq_management rabbitmq_prometheus
rabbitmq-diagnostics status
```

## One-liners

- Publish to exchanges, consume from queues.
- Confirms say "handled"; mandatory says "routed".
- Never `nack(requeue=true)` forever; dead-letter with delayed retry tiers.
- Per-message TTL (classic) expires only at the head.
- Order holds per queue until you add competing consumers or retries.
- At-least-once + idempotency = exactly-once effect.
- Queues for jobs; logs (Kafka/Streams) for history.

## Where to go next

- [Overview](./index.md) · [Question index](./question-index.md)
- [Celery](../celery/index.md) · [Messaging systems overview](../architecture/05-messaging-systems.md)
