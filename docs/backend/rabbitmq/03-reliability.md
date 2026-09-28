---
sidebar_label: "Reliability"
description: "End-to-end message safety in RabbitMQ: durable queues, persistent messages, publisher confirms, consumer acks and the mandatory flag."
---

# Reliability (Q9-Q12)

> **Reviewed:** 2026-09 · **Level:** Senior · **Type:** Foundational

## Q9. Surviving a broker restart needs durable queues and persistent messages, together

Durability is two settings. A **durable** queue's definition survives restart; a **persistent** message (`delivery_mode=2`) is written to disk. A persistent message in a non-durable queue is lost when the queue disappears; a transient message in a durable queue may be lost too. Quorum queues and streams are always durable and persist messages.

**Example:**

```python
ch.queue_declare("payments", durable=True, arguments={"x-queue-type": "quorum"})
ch.basic_publish(
    exchange="",
    routing_key="payments",
    body=payload,
    properties=pika.BasicProperties(delivery_mode=2, content_type="application/json",
                                    message_id=str(uuid4())),
)
```

**Trade-offs and pitfalls:**

- Persistence alone does not tell the publisher the message reached disk; that is what publisher confirms are for (Q10).
- Durability protects against restarts, not against losing the node's disk; that needs replicated queues ([Clustering and HA](./07-clustering-and-ha.md)).

**Remember:** Durable queue + persistent message + confirms + replication = safe.

## Q10. Publisher confirms tell the producer the broker has taken responsibility for a message

Without confirms, `basic.publish` is fire-and-forget: the client has no idea whether the broker accepted, persisted or dropped the message. With a channel in confirm mode, the broker sends `basic.ack` for each message once it is handled (for persistent messages on durable queues, after it has been written/replicated as the queue type requires), or `basic.nack` if it could not. The producer retries unconfirmed messages.

**How it works:**

- Publish in batches or asynchronously, track outstanding sequence numbers, and handle acks/nacks as they arrive. Waiting for a confirm after *every* single message is simple but slow.
- On timeout or nack, republish; consumers must deduplicate because republishing can create duplicates.

**Example:**

```javascript
// Node amqplib
const ch = await conn.createConfirmChannel();
ch.publish('events', 'order.eu.created', Buffer.from(JSON.stringify(evt)), {
  persistent: true,
  messageId: evt.id,
  contentType: 'application/json',
});
await ch.waitForConfirms();   // resolves when all outstanding publishes are acked
```

**Trade-offs and pitfalls:**

- Transactions (`tx.select`) also guarantee this but are much slower; confirms are the recommended mechanism.
- Confirms cover publisher-to-broker only. Broker-to-consumer safety is consumer acks (Q11).

**Remember:** No confirms means you don't know whether you published.

## Q11. Consumer acks hand responsibility back: ack, nack, reject and requeue

In manual ack mode, the broker keeps a delivered message as "unacked" until the consumer responds. `basic.ack` removes it. `basic.nack` / `basic.reject` with `requeue=true` returns it to the queue (typically near the head); with `requeue=false` it is dropped or dead-lettered. If the channel or connection closes with unacked messages, they are requeued and redelivered with `redelivered=true`.

**How it works:**

| Action | Effect |
|---|---|
| `ack` | Done; message removed |
| `nack`/`reject`, `requeue=true` | Put back and redelivered, possibly to another consumer |
| `nack`/`reject`, `requeue=false` | Dead-lettered if a DLX is configured, otherwise discarded |
| Connection lost | All unacked messages on that channel requeued |
| Auto-ack (`no_ack`) | Considered delivered on send; lost if the consumer crashes |

**Example:**

```python
def handle(ch, method, props, body):
    try:
        process(body)
        ch.basic_ack(method.delivery_tag)
    except TransientError:
        publish_to_retry_queue(props, body)                 # delayed retry, see next file
        ch.basic_ack(method.delivery_tag)
    except Exception:
        ch.basic_nack(method.delivery_tag, requeue=False)   # dead-letter for inspection
```

**Trade-offs and pitfalls:**

- `nack(requeue=true)` on a message that always fails creates a tight hot loop. Prefer dead-lettering with delayed retry ([Dead-lettering and retries](./04-dead-lettering-and-retries.md)).
- RabbitMQ enforces a delivery acknowledgement timeout (`consumer_timeout`, 30 minutes by default in modern versions); a consumer holding a message longer gets its channel closed. Long jobs need it raised or a different design.
- Ack on the same channel that received the message; delivery tags are per channel.

**Remember:** Ack after the work is done; never requeue forever.

## Q12. The `mandatory` flag and alternate exchanges catch unroutable messages

A message that matches no binding is dropped silently by default, and publisher confirms still ack it (the broker handled it correctly: it routed it nowhere). Set `mandatory=true` to have the broker return unroutable messages to the publisher (`basic.return`), or configure an alternate exchange to capture them server-side.

**Example:**

```javascript
ch.on('return', (msg) => {
  logger.error({ routingKey: msg.fields.routingKey }, 'unroutable message');
  // store for replay or alert
});
ch.publish('events', 'order.eu.created', body, { mandatory: true, persistent: true });
```

**Trade-offs and pitfalls:**

- Returns arrive asynchronously; your client must register a handler before publishing.
- Alternate exchanges are simpler operationally (no client code) and work for all publishers.

> **Interview tip:** "Confirms + mandatory (or an alternate exchange) + durable quorum queues + manual acks + idempotent consumers" is the full end-to-end reliability answer.

**Remember:** Confirms say "handled"; mandatory says "and it actually reached a queue".

## References

- [RabbitMQ documentation: confirms, acks and reliability](https://www.rabbitmq.com/docs)
- [Messaging systems overview: acks and durable queues](../architecture/05-messaging-systems.md)
