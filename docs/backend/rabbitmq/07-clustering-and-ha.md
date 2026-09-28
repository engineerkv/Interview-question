---
sidebar_label: "Clustering and HA"
description: "RabbitMQ clustering, quorum queues as the replicated queue type, the removal of classic mirrored queues in 4.x, and RabbitMQ Streams."
---

# Clustering and High Availability (Q24-Q27)

> **Reviewed:** 2026-09 · **Level:** Senior · **Type:** Foundational

## Q24. A RabbitMQ cluster shares metadata, but a queue's data lives where its replicas are

A cluster is a group of nodes that share users, vhosts, exchanges, bindings, policies and queue definitions. Clients can connect to any node and reach any queue (the cluster routes internally). But a queue's messages are stored on its leader and replica nodes only. A classic (non-replicated) queue lives on one node: if that node is down, the queue is unavailable.

**How it works:**

- Use an odd number of nodes (commonly 3 or 5) so Raft-based queues and metadata keep a majority during a single-node failure.
- Clustering expects a low-latency, reliable LAN. For cross-region or WAN links, use **Federation** or **Shovel** to move messages between separate clusters instead of stretching one cluster.
- Nodes authenticate each other with a shared Erlang cookie; inter-node traffic should be on a private network (and can use TLS).
- Put a load balancer or client-side list of hosts in front so clients reconnect to a healthy node.

**Trade-offs and pitfalls:**

- Network partitions are a real concern for clusters; understand the partition handling strategy and prefer queue types built on Raft, which handle partitions predictably.
- Adding nodes does not automatically spread existing queue leaders; rebalance leaders after scaling.

**Remember:** Cluster = shared metadata; replication is a per-queue-type decision.

## Q25. Quorum queues are the recommended replicated queue type; classic mirrored queues are gone in 4.x

Quorum queues replicate each queue across several nodes using the Raft consensus algorithm. A message is confirmed once a majority of replicas have it, and a new leader is elected automatically if the leader fails. Classic mirrored queues (HA policies like `ha-mode`) were deprecated in the 3.x series and **removed in RabbitMQ 4.0**. On 4.x, the HA options are quorum queues for work queues and streams for log-style data.

**How it works:**

| Aspect | Quorum queue | Classic queue (4.x) |
|---|---|---|
| Replication | Raft, majority-based | None (single node) |
| Durability | Always durable | Durable or transient |
| Poison message handling | Delivery count and delivery limit | None built in |
| Non-durable / exclusive use | Not supported | Supported |
| Good for | Important work queues, commands, orders | Temporary, per-client, reply queues, low-value data |

**Example:**

```python
ch.queue_declare(
    "orders.work",
    durable=True,
    arguments={"x-queue-type": "quorum", "x-quorum-initial-group-size": 3},
)
```

**Trade-offs and pitfalls:**

- Queue type cannot be changed in place; migrate by creating a new queue and moving consumers/bindings (or via a blue/green vhost).
- Quorum queues trade some per-queue throughput and more disk/memory usage for safety; very long backlogs cost more than on classic queues. Keep queues short.
- Some classic-queue features behave differently or are unsupported on quorum queues (for example, non-durable and exclusive declarations, and some TTL and priority behaviors differ by version). Check the feature matrix in the docs for your version.
- Clients that request `x-ha-policy` or mirroring policies from old tutorials will not get HA on 4.x.

> **Interview tip:** Saying "we use mirrored queues for HA" in a 2026 interview is a red flag. Say "quorum queues, three replicas, publisher confirms, and odd-sized clusters".

**Remember:** HA on RabbitMQ 4.x means quorum queues (or streams), not mirroring.

## Q26. RabbitMQ Streams are an append-only, replayable log inside RabbitMQ

Streams (available since RabbitMQ 3.9) are a queue type where messages are appended to a replicated log and **not removed on consumption**. Consumers read from an offset (first, last, next, a timestamp or a specific offset) and many consumers can read the same data independently. Retention is by size or age. They can be consumed via AMQP 0-9-1 (with some constraints, such as a prefetch being required) or via the dedicated stream protocol for higher throughput. Super streams partition a logical stream across several streams.

**Example:**

```python
ch.queue_declare("audit.events", durable=True,
                 arguments={"x-queue-type": "stream", "x-max-age": "7D"})
ch.basic_qos(prefetch_count=100)            # required for stream consumers over AMQP
ch.basic_consume("audit.events", on_message_callback=handle,
                 arguments={"x-stream-offset": "first"})
```

**Trade-offs and pitfalls:**

- Streams give Kafka-like replay and fan-out in a RabbitMQ shop, but the ecosystem (connectors, stream processing libraries) is much smaller than Kafka's.
- Consumer offset tracking is the consumer's job (the stream protocol can store offsets server-side, but you decide when).
- Not a drop-in for work queues: there is no per-message ack-and-remove or dead-lettering in the same sense.

**Remember:** Streams = non-destructive, replayable log; queues = consume and remove.

## Q27. Designing for failure means clients, not just the broker, must be HA-aware

Broker HA only helps if clients recover. Producers should use publisher confirms and retry unconfirmed messages after reconnecting. Consumers must reconnect, redeclare topology if needed, and expect redeliveries of anything unacked. Libraries such as aio-pika's `connect_robust` or reconnecting wrappers around amqplib help, but you still own idempotency.

**Example:** During a rolling upgrade of a 3-node cluster, each node restarts in turn. Quorum queue leaders move to other nodes; clients connected to the restarting node reconnect through the load balancer; unconfirmed publishes are retried; consumers see some `redelivered=true` messages and deduplicate them.

**Trade-offs and pitfalls:**

- Reconnect storms after an outage can overload the broker; use jittered backoff.
- Exclusive and auto-delete queues are lost on reconnect by design; don't put important data there.
- Metadata store changes (the Raft-based Khepri store, introduced as an option in recent releases) are an evolving area; check release notes before major upgrades. *(Emerging)*

**Remember:** HA = replicated queues + confirms + reconnecting clients + idempotent consumers.

## References

- [RabbitMQ documentation: clustering, quorum queues, streams](https://www.rabbitmq.com/docs)
- [Messaging systems overview](../architecture/05-messaging-systems.md)
