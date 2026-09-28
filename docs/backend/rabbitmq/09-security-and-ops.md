---
sidebar_label: "Security and Operations"
description: "Users, permissions and vhosts, TLS, the management UI, and the metrics that matter for operating RabbitMQ."
---

# Security and Operations (Q31-Q34)

> **Reviewed:** 2026-09 · **Level:** Senior · **Type:** Foundational

## Q31. Least privilege in RabbitMQ is users + vhosts + configure/write/read permissions

Each user gets permissions per vhost as three regular expressions: **configure** (declare/delete exchanges and queues), **write** (publish to exchanges, bind), and **read** (consume from queues, bind from exchanges). Topic permissions can further restrict which routing keys a user may publish. Tags (`administrator`, `monitoring`, `management`) control management UI/API access.

**Example:**

```bash
rabbitmqctl add_user orders_producer "$(cat /run/secrets/orders_producer)"
# can publish to the orders exchange only; cannot declare or consume
rabbitmqctl set_permissions -p shop orders_producer '^$' '^orders$' '^$'

rabbitmqctl add_user email_consumer "$(cat /run/secrets/email_consumer)"
rabbitmqctl set_permissions -p shop email_consumer '^email\..*' '^$' '^email\..*'
```

**Trade-offs and pitfalls:**

- The default `guest` user can only connect from localhost by default; do not undo that. Create real users and delete or disable `guest` in production.
- If apps declare their own topology, they need configure rights; alternatively, declare topology via definitions at deploy time and give apps only read/write.
- Rotate credentials via your secret manager; consider OAuth 2.0 / x.509 client certificates for machine identities.

**Remember:** One user per service, one vhost per app or domain, minimal regexes.

## Q32. Encrypt client and management traffic with TLS

AMQP over TLS conventionally uses port 5671 (plain AMQP uses 5672). Enable TLS for client connections, the management UI/API (default HTTP port 15672), and ideally inter-node traffic. Peer verification with client certificates lets you authenticate services by certificate.

**Example:**

```ini
# rabbitmq.conf (excerpt)
listeners.tcp = none
listeners.ssl.default = 5671
ssl_options.cacertfile = /etc/rabbitmq/ca.pem
ssl_options.certfile   = /etc/rabbitmq/server.pem
ssl_options.keyfile    = /etc/rabbitmq/server-key.pem
ssl_options.verify     = verify_peer
ssl_options.fail_if_no_peer_cert = true
management.ssl.port       = 15671
management.ssl.cacertfile = /etc/rabbitmq/ca.pem
management.ssl.certfile   = /etc/rabbitmq/server.pem
management.ssl.keyfile    = /etc/rabbitmq/server-key.pem
```

**Trade-offs and pitfalls:**

- Never expose the management UI or AMQP ports to the internet; keep them in private networks.
- TLS termination at a load balancer is possible but loses client-cert identity at the broker; end-to-end TLS is simpler to reason about.

**Remember:** 5671 with TLS, private networks, no public management UI.

## Q33. The management UI is for humans; Prometheus metrics are for alerting

The management plugin provides a web UI and HTTP API for browsing queues, connections, channels, publishing test messages and exporting definitions. For monitoring, enable the `rabbitmq_prometheus` plugin (metrics endpoint on port 15692) and use the official Grafana dashboards. Relying on the management API for high-frequency scraping of large clusters is discouraged.

**Example:**

```bash
rabbitmq-plugins enable rabbitmq_management rabbitmq_prometheus
rabbitmqctl export_definitions /backup/definitions.json    # topology + users + policies
rabbitmq-diagnostics check_port_connectivity
rabbitmq-diagnostics status
```

**Trade-offs and pitfalls:**

- Definitions export is topology backup, not message backup.
- Health checks: prefer targeted diagnostics commands over "is the port open".

**Remember:** UI to investigate, Prometheus to alert, definitions to rebuild.

## Q34. Queue depth, unacked messages and consumer utilisation are the key metrics

| Metric | What it tells you | Typical alert |
|---|---|---|
| Messages ready (queue depth) | Backlog waiting for consumers | Growing steadily, or above what consumers can drain within the queue's SLO |
| Messages unacknowledged | In-flight on consumers | High with low ack rate: stuck or slow consumers, prefetch too high |
| Consumer count | Anyone listening? | Zero consumers on a queue that has producers |
| Consumer utilisation | Fraction of time the queue can deliver immediately to consumers | Low with backlog: consumers are the bottleneck or prefetch too small |
| Publish / deliver / ack rates | Throughput balance | Publish rate > ack rate for a sustained period |
| Redelivery rate | Crashes, nacks, requeue loops | Sudden increase |
| Memory / disk / file descriptors | Broker health | Approaching alarm thresholds |
| Connection and channel churn | Client misuse | High open/close rate |
| DLQ depth | Permanently failed messages | Any growth |

**Example:** Queue `thumbnails` shows 50k ready, 200 unacked, 10 consumers, and utilisation well below full. Diagnosis: consumers are busy processing (unacked equals prefetch × consumers), so scale consumers or speed up processing. If ready is high and consumer count is zero, a deployment broke the consumers.

**Trade-offs and pitfalls:**

- Depth alone misleads; combine with rates and age.
- Per-queue metrics at very high queue counts are expensive; aggregate or sample where needed.

**Remember:** Ready = backlog, unacked = in flight, utilisation = are consumers keeping up.

## References

- [RabbitMQ documentation: access control, TLS, management, monitoring](https://www.rabbitmq.com/docs)
- [Celery monitoring and operations (this site)](../celery/09-monitoring-and-ops.md)
