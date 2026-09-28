---
sidebar_label: "Prefetch and Flow Control"
description: "Consumer prefetch with basic.qos, backpressure strategies, and RabbitMQ memory and disk alarms that block publishers."
---

# Prefetch and Flow Control (Q21-Q23)

> **Reviewed:** 2026-09 · **Level:** Senior · **Type:** Foundational

## Q21. `basic.qos` prefetch caps how many unacked messages a consumer holds

Prefetch count is the maximum number of delivered-but-unacked messages per consumer (RabbitMQ applies `prefetch_count` per consumer on a channel by default; the `global` flag changes the scope and behaves differently across queue types). With prefetch 1 the broker waits for each ack before sending the next message: fair, low throughput. Unlimited prefetch (0) floods consumers and can exhaust their memory. Typical values are tens to a few hundred, tuned by measurement.

**How it works:**

| Workload | Prefetch guidance |
|---|---|
| Long, uneven tasks | 1 (or very small) for fair dispatch |
| Short, uniform tasks, high throughput | Larger (tens to hundreds) to hide network round-trip |
| Consumer processes N in parallel | At least N so all slots stay busy |

**Example:**

```javascript
await ch.prefetch(20);   // amqplib: per-consumer limit on this channel
await ch.consume('thumbnails', onMessage, { noAck: false });
```

**Trade-offs and pitfalls:**

- Prefetched messages are invisible to other consumers; a slow consumer with high prefetch hoards work.
- Auto-ack ignores prefetch entirely and pushes as fast as the network allows.
- Celery's `worker_prefetch_multiplier` is this setting in disguise ([Celery workers](../celery/03-workers-and-concurrency.md)).

**Remember:** Prefetch is your consumer-side backpressure knob.

## Q22. Backpressure has to exist on both ends of the queue

A queue absorbs bursts, but a queue that grows forever is a delayed outage. Consumer-side backpressure is prefetch plus bounded concurrency. Producer-side backpressure includes publisher confirms (outstanding window), queue length limits with `reject-publish` overflow (the producer gets a nack), and broker flow control.

**Example:**

```bash
rabbitmqctl set_policy ingest-limit '^ingest\.' \
  '{"max-length":100000,"overflow":"reject-publish"}' --apply-to queues
```

The producer sees nacks when the queue is full and can return `503`/`429` upstream instead of accepting work the system cannot finish.

**Trade-offs and pitfalls:**

- `drop-head` (the default overflow) silently discards the oldest messages; fine for telemetry, dangerous for orders.
- Autoscaling consumers helps only if the downstream (DB, API) can take more.

**Remember:** Bound the queue and push back on producers, or the queue becomes the outage.

## Q23. Memory and disk alarms block all publishing connections

RabbitMQ monitors its memory use against a high watermark and free disk space against a limit. When either alarm fires, the broker blocks connections that publish (clients can receive `connection.blocked` notifications) until the resource recovers. Consumers keep working, which is how the system drains. Separately, per-connection credit-based flow control slows individual publishers that outrun the broker.

**Trade-offs and pitfalls:**

- Because the block is per connection, a service that publishes and consumes on the same connection can stall its own consumers; use separate connections.
- Blocked publishers look like hung requests; handle `blocked`/`unblocked` events, time out publishes, and alert on alarms.
- Large backlogs of messages are the usual trigger. Fix with more consumers, length limits and TTLs, not by raising the watermark indefinitely.

**Example:**

```javascript
conn.on('blocked', (reason) => logger.warn({ reason }, 'rabbitmq blocked publishing'));
conn.on('unblocked', () => logger.info('rabbitmq unblocked'));
```

**Remember:** A resource alarm on any node blocks publishers across the cluster; keep publishing and consuming connections separate.

## References

- [RabbitMQ documentation: consumer prefetch, flow control, alarms](https://www.rabbitmq.com/docs)
- [Messaging systems overview: backpressure](../architecture/05-messaging-systems.md)
