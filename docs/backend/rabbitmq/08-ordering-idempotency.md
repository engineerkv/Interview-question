---
sidebar_label: "Ordering and Idempotency"
description: "What ordering RabbitMQ guarantees, where it breaks, how to build idempotent consumers, and why exactly-once delivery is a myth."
---

# Ordering and Idempotency (Q28-Q30)

> **Reviewed:** 2026-09 · **Level:** Senior · **Type:** Foundational

## Q28. RabbitMQ preserves order per queue for a single publisher channel, and consumers break it

Messages published on one channel, routed to one queue, are enqueued in publish order. Delivery order to consumers follows queue order. But anything that parallelizes or reorders processing breaks end-to-end ordering: multiple competing consumers, prefetch > 1 with concurrent handling, requeues (a requeued message goes back near the head, after others may have been processed), retries via delay queues, multiple publishers, and priorities.

**How it works:**

| Need | Technique |
|---|---|
| Strict order for one queue | One active consumer: `x-single-active-consumer: true` (others stand by for failover), prefetch 1 or sequential processing |
| Order per key (per order id, per user) with parallelism | Partition: consistent-hash exchange or N queues chosen by hash of the key; one active consumer per partition |
| Log-style ordered replay | Streams / super streams |
| Tolerate reordering | Version numbers or timestamps; ignore older updates |

**Example:**

```python
ch.queue_declare("ledger.account-42", durable=True,
                 arguments={"x-queue-type": "quorum", "x-single-active-consumer": True})
```

**Trade-offs and pitfalls:**

- Single active consumer caps throughput at one consumer's speed.
- Delayed retries move a message behind later ones; if order matters, stop the partition (don't ack, pause) rather than retrying out of band.
- Often the better design is to make the consumer order-insensitive: "set status to X if version > current".

**Remember:** Order holds per queue until you add parallel consumers or retries.

## Q29. Idempotent consumers make duplicates harmless

RabbitMQ gives at-least-once delivery when you use acks and confirms. Duplicates come from publisher retries after a lost confirm, redelivery after a consumer crash before ack, and connection drops. The consumer must make a second processing a no-op.

**Example:**

```python
def handle(ch, method, props, body):
    msg_id = props.message_id                          # producer sets a stable id
    with db.transaction():
        inserted = db.execute(
            "INSERT INTO processed_messages (id) VALUES (%s) ON CONFLICT DO NOTHING RETURNING id",
            (msg_id,),
        )
        if inserted:
            apply_business_change(json.loads(body))     # same transaction as the dedupe insert
    ch.basic_ack(method.delivery_tag)
```

**Trade-offs and pitfalls:**

- The dedupe record and the business change must commit atomically; otherwise a crash between them either loses or duplicates the effect.
- Dedupe tables grow; expire entries after a window longer than any plausible redelivery.
- Natural idempotency (upserts, "set" rather than "increment", unique constraints on business keys) is cheaper than a dedupe table when possible.

**Remember:** Stable message ids + atomic dedupe = safe at-least-once.

## Q30. Exactly-once delivery is a myth; exactly-once *effect* is an application property

Across a network, a sender cannot distinguish "the message was lost" from "the ack was lost", so it must either retry (risking duplicates) or not (risking loss). No broker can deliver exactly once to an arbitrary consumer with external side effects. What you can build is effectively-once processing: at-least-once delivery plus idempotent handling, or transactional boundaries that include both the consumption record and the effect.

**Trade-offs and pitfalls:**

- Kafka's "exactly-once semantics" applies to read-process-write within Kafka using transactions; it does not make an email or a card charge happen exactly once.
- For external APIs, pass an idempotency key so the provider deduplicates.
- Outbox on the producer side plus inbox (dedupe) on the consumer side is the standard end-to-end pattern.

> **Interview tip:** Say "at-least-once plus idempotency gives exactly-once effects", then give the dedupe-table example. That is the answer interviewers are listening for.

**Remember:** Delivery is at-least-once; exactly-once is something your consumer does.

## References

- [RabbitMQ documentation: reliability, single active consumer, consistent hash exchange](https://www.rabbitmq.com/docs)
- [Messaging systems overview: duplicate handling](../architecture/05-messaging-systems.md)
