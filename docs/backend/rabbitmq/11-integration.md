---
sidebar_label: "Integration (Node, Python, Celery)"
description: "Production-style RabbitMQ clients in Node.js with amqplib, Python with pika and aio-pika, and running Celery on RabbitMQ."
---

# Integration: Node, Python and Celery (Q38-Q41)

> **Reviewed:** 2026-09 · **Level:** Senior · **Type:** Foundational

## Q38. A Node.js service uses amqplib with confirm channels, prefetch and manual acks

A production-grade Node client keeps one long-lived connection, uses a confirm channel for publishing, a separate channel for consuming with a prefetch, acks after processing, and handles connection errors by reconnecting with backoff.

**Example:**

```javascript
// publisher.js
import amqp from 'amqplib';

const conn = await amqp.connect(process.env.AMQP_URL);   // amqps://user:pass@host:5671/shop
conn.on('error', (err) => logger.error({ err }, 'amqp connection error'));
conn.on('close', () => scheduleReconnect());               // your backoff logic

const pub = await conn.createConfirmChannel();
await pub.assertExchange('orders', 'topic', { durable: true });

export async function publishOrderCreated(order) {
  const body = Buffer.from(JSON.stringify({ id: order.id, total: order.total }));
  pub.publish('orders', `order.${order.region}.created`, body, {
    persistent: true,
    contentType: 'application/json',
    messageId: `order-created-${order.id}`,
    mandatory: true,
  });
  await pub.waitForConfirms();
}
```

```javascript
// consumer.js
const ch = await conn.createChannel();
await ch.assertQueue('email.orders', { durable: true, arguments: { 'x-queue-type': 'quorum' } });
await ch.bindQueue('email.orders', 'orders', 'order.*.created');
await ch.prefetch(10);

await ch.consume('email.orders', async (msg) => {
  if (!msg) return;                                   // consumer cancelled by broker
  try {
    const evt = JSON.parse(msg.content.toString());
    await sendOrderEmail(evt);                        // idempotent on evt.id
    ch.ack(msg);
  } catch (err) {
    logger.error({ err }, 'failed to process');
    ch.nack(msg, false, false);                       // dead-letter via policy
  }
});

process.on('SIGTERM', async () => {                   // stop consuming, finish in-flight, close
  await ch.close();
  await conn.close();
});
```

**Trade-offs and pitfalls:**

- amqplib does not auto-reconnect; use a wrapper library or write reconnect + redeclare logic.
- Awaiting `waitForConfirms` per message is simple but serializes publishes; batch for throughput.
- See also the [Node/Express question index](../node-express/question-index.md) for general async and graceful-shutdown topics.

**Remember:** Confirm channel to publish, prefetch + manual ack to consume, reconnect on close.

## Q39. Python with pika (blocking) suits scripts and simple workers; aio-pika suits asyncio services

pika's `BlockingConnection` is straightforward but is not thread-safe; use one connection per thread. For FastAPI or other asyncio apps, aio-pika provides an async API and `connect_robust`, which reconnects and restores declared topology.

**Example:**

```python
# pika: blocking consumer
import json, pika

params = pika.URLParameters("amqps://user:pass@rabbit:5671/shop")
conn = pika.BlockingConnection(params)
ch = conn.channel()
ch.queue_declare("email.orders", durable=True, arguments={"x-queue-type": "quorum"})
ch.basic_qos(prefetch_count=10)

def on_message(ch, method, props, body):
    try:
        send_order_email(json.loads(body))
        ch.basic_ack(method.delivery_tag)
    except Exception:
        ch.basic_nack(method.delivery_tag, requeue=False)

ch.basic_consume("email.orders", on_message_callback=on_message)
ch.start_consuming()
```

```python
# aio-pika: async publisher and consumer
import aio_pika, json

async def main():
    conn = await aio_pika.connect_robust("amqps://user:pass@rabbit:5671/shop")
    async with conn:
        ch = await conn.channel(publisher_confirms=True)
        await ch.set_qos(prefetch_count=20)
        orders = await ch.declare_exchange("orders", aio_pika.ExchangeType.TOPIC, durable=True)

        await orders.publish(
            aio_pika.Message(
                body=json.dumps({"id": 42}).encode(),
                delivery_mode=aio_pika.DeliveryMode.PERSISTENT,
                message_id="order-created-42",
                content_type="application/json",
            ),
            routing_key="order.eu.created",
        )

        queue = await ch.declare_queue("email.orders", durable=True,
                                       arguments={"x-queue-type": "quorum"})
        await queue.bind(orders, routing_key="order.*.created")
        async with queue.iterator() as it:
            async for message in it:
                async with message.process(requeue=False):   # ack on success, reject on exception
                    await send_order_email(json.loads(message.body))
```

**Trade-offs and pitfalls:**

- Long synchronous work inside a pika callback blocks heartbeats and the broker may drop the connection; run work in a thread and ack via `connection.add_callback_threadsafe`, or use shorter tasks.
- In asyncio consumers, CPU-heavy handlers block the event loop; offload to a process pool or a Celery worker.

**Remember:** pika for simple blocking code, aio-pika for asyncio; never share a channel across threads.

## Q40. Celery on RabbitMQ needs a few RabbitMQ-aware settings

Celery uses Kombu over AMQP. Declare queues explicitly so you control queue type and arguments, give Celery its own vhost and user, and align timeouts. Long ETA/countdown tasks and long late-acked tasks can hit RabbitMQ's `consumer_timeout`, so either raise it for that vhost/queue or avoid long ETAs.

**Example:**

```python
from kombu import Exchange, Queue

broker_url = "amqp://celery:secret@rabbit:5672/celery"
task_queues = [
    Queue("default", Exchange("default"), routing_key="default",
          queue_arguments={"x-queue-type": "quorum"}),
    Queue("email", Exchange("email"), routing_key="email",
          queue_arguments={"x-queue-type": "quorum"}),
]
task_default_queue = "default"
task_acks_late = True
worker_prefetch_multiplier = 1
broker_heartbeat = 60
```

**Trade-offs and pitfalls:**

- Quorum queues do not support the "global QoS" mode that older Celery versions relied on for ETA handling. Newer Celery releases (5.5+) added explicit quorum queue support (for example `task_default_queue_type` and native delayed delivery); verify against the Celery docs for your version before switching. *(Emerging)*
- Celery's remote-control and event exchanges create extra queues; include them in permission regexes, or disable events you don't use.
- Use the [Celery section](../celery/index.md) for worker-side reliability settings.

**Remember:** Dedicated vhost, explicitly declared queues, late ack, prefetch 1, and watch `consumer_timeout`.

## Q41. A message contract makes RabbitMQ integrations language-agnostic

When Node producers and Python consumers share queues, the schema is the contract. Use JSON (or Avro/Protobuf) with an explicit version, set `content_type`, `message_id` and a timestamp, and propagate tracing context (for example W3C `traceparent`) in headers. Consumers validate at the boundary and dead-letter invalid messages instead of crashing.

**Example:**

```json
{
  "type": "order.created",
  "version": 2,
  "id": "0b8f6a1e-2c7d-4d1a-9a55-5a1c2f0e9e11",
  "occurred_at": "2026-09-28T08:00:00Z",
  "data": { "order_id": 42, "region": "eu", "total_cents": 1999 }
}
```

**Trade-offs and pitfalls:**

- Additive changes (new optional fields) are safe; renames and type changes need a new version and a transition period where consumers accept both.
- Celery's task message format is Python-oriented; for cross-language consumers publish plain AMQP messages with your own schema rather than Celery tasks.

**Remember:** Version the schema, set ids and content type, validate at the edge.

## References

- [RabbitMQ documentation: client libraries and tutorials](https://www.rabbitmq.com/docs)
- [Celery documentation: using RabbitMQ](https://docs.celeryq.dev/en/stable/)
- [Python backend (this site)](../python/index.md)
