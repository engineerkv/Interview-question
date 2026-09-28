---
sidebar_label: "Fundamentals"
description: "The AMQP 0-9-1 model, connections vs channels, producers and consumers, and virtual hosts in RabbitMQ."
---

# RabbitMQ Fundamentals (Q1-Q4)

> **Reviewed:** 2026-09 · **Level:** Senior · **Type:** Foundational

For where RabbitMQ sits next to Kafka and SQS, see the [messaging systems overview](../architecture/05-messaging-systems.md). This section covers RabbitMQ in depth.

## Q1. In AMQP 0-9-1, producers publish to exchanges, and bindings route messages into queues

The key mental model: producers never write directly to a queue. They publish to an **exchange** with a **routing key**. The exchange uses **bindings** (rules linking the exchange to queues, with a binding key or header match) to decide which queues get a copy. Consumers subscribe to **queues**. This indirection lets you add new consumers or change routing without touching producers.

**How it works:**

| Concept | Meaning |
|---|---|
| Exchange | Routing entity; types: direct, topic, fanout, headers |
| Queue | Ordered buffer of messages, consumed by one or more consumers |
| Binding | Rule "exchange X sends messages matching K to queue Q" |
| Routing key | String set by the publisher, matched against bindings |
| Default exchange (`""`) | Pre-declared direct exchange; every queue is bound to it by its own name |
| Message | Body (bytes) + properties (content type, delivery mode, headers, message id, correlation id, reply-to, expiration) |

**Example:** Publishing to the default exchange with routing key `emails` delivers straight to the queue named `emails`, which is why simple tutorials look like "publish to a queue".

**Trade-offs and pitfalls:**

- An exchange with no matching binding silently drops the message unless you use the `mandatory` flag or an alternate exchange (see [Reliability](./03-reliability.md)).
- RabbitMQ 4.x also speaks AMQP 1.0 natively (plus MQTT, STOMP and the stream protocol), but most application libraries and interview questions still use the 0-9-1 model.

**Remember:** Publish to exchanges, consume from queues, bindings connect them.

## Q2. A connection is a TCP socket; channels are lightweight sessions multiplexed over it

Opening a TCP + TLS connection and authenticating is expensive, so AMQP multiplexes many **channels** over one connection. Each channel is an independent session with its own publishes, consumers, acks and QoS. The rule of thumb: few long-lived connections per process, one channel per thread or per logical consumer, never share a channel across threads.

**Example:**

```python
import pika

conn = pika.BlockingConnection(pika.URLParameters("amqp://app:secret@rabbit:5672/orders"))
publish_ch = conn.channel()      # used by the publishing code path
consume_ch = conn.channel()      # separate channel for consuming
```

**Trade-offs and pitfalls:**

- Opening a connection per message (common in serverless or naive web code) is a well-known anti-pattern that causes connection churn and high broker CPU.
- Channel-level errors (e.g., declaring a queue with different arguments) close the channel, not the connection; your client must reopen it.
- Separate publishing and consuming connections: if the broker applies flow control to publishers, it blocks the connection, which would also stall consumers on it.

**Remember:** One connection, many channels; one channel per thread.

## Q3. Producers and consumers are roles, and consumers can push or pull

A producer publishes messages; a consumer receives them. A single application often does both. Consumers usually register a subscription (`basic.consume`) and the broker pushes messages up to the prefetch limit. Polling with `basic.get` exists but is inefficient and should be avoided for steady workloads.

**Example:**

```python
def handle(ch, method, props, body):
    process(body)
    ch.basic_ack(delivery_tag=method.delivery_tag)

consume_ch.basic_qos(prefetch_count=20)
consume_ch.basic_consume(queue="orders.created", on_message_callback=handle)
consume_ch.start_consuming()
```

**Trade-offs and pitfalls:**

- Multiple consumers on one queue compete: each message goes to one of them (round-robin, subject to prefetch). That is how you scale workers.
- To give every service its own copy, give each its own queue bound to the exchange (pub/sub, see [Patterns](./05-patterns.md)).

**Remember:** Push consumers with a prefetch limit are the normal consumption mode.

## Q4. Virtual hosts are logical namespaces for isolation inside one broker

A vhost has its own exchanges, queues, bindings, users' permissions and policies. Use vhosts to separate applications or environments sharing a cluster (e.g., `/billing`, `/notifications`). Users are granted configure, write and read permissions per vhost using regex patterns.

**Example:**

```bash
rabbitmqctl add_vhost billing
rabbitmqctl add_user billing_svc 'S3cure!'
rabbitmqctl set_permissions -p billing billing_svc '^billing\..*' '^billing\..*' '^billing\..*'
```

**Trade-offs and pitfalls:**

- Vhosts isolate names and permissions, not resources: a noisy vhost still consumes the node's memory, disk and CPU. Use separate clusters for hard isolation (or per-vhost limits where appropriate).
- The default vhost is `/`; in URLs it is encoded as `%2F` (e.g., `amqp://host:5672/%2F`).

**Remember:** Vhosts separate namespaces and permissions, not capacity.

## References

- [RabbitMQ documentation](https://www.rabbitmq.com/docs)
- [Messaging systems overview](../architecture/05-messaging-systems.md)
