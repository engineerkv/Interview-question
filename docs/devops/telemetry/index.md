---
sidebar_position: 0
sidebar_label: Overview
description: "Telemetry and observability: signals, golden signals, OpenTelemetry, alerting, cardinality and vendor tooling."
---

# Telemetry & Observability

> **Reviewed:** 2026-09 · **Level:** Senior / Tech Lead · **Type:** Foundational

You can't operate what you can't see. Senior interviews expect you to design what to measure, how to alert on it, and how to trace a request across services and the frontend.

## Pages

- [CloudWatch and New Relic](./01-cloudwatch-and-new-relic.md) — 15 questions (Q120–Q134): CloudWatch metrics, logs, dashboards and alarms, X-Ray, New Relic APM, distributed tracing and alerting.
- [Observability & OpenTelemetry](./02-observability-with-opentelemetry.md) — 10 questions: logs vs metrics vs traces, golden signals/RED/USE, OpenTelemetry architecture, context propagation, symptom-based alerting, cardinality, RUM-to-APM correlation, structured logging, cost control, rolling out observability.

## What interviewers look for

- Choosing the right signal for the question.
- Alerting on user-visible symptoms tied to SLOs.
- Vendor-neutral instrumentation with OpenTelemetry.

## Related

- Using the signals under pressure: [SLOs, Incidents & Postmortems](../reliability-and-incidents/01-slos-incidents-and-postmortems.md)
