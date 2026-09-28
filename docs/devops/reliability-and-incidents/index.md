---
sidebar_position: 0
sidebar_label: Overview
description: "Reliability engineering and incident management: SLOs, error budgets, on-call, incident command, postmortems and production debugging."
---

# Reliability & Incidents

> **Reviewed:** 2026-09 · **Level:** Senior / Tech Lead · **Type:** Foundational

This is where Tech Lead interviews test judgement under pressure: how you define "reliable enough", how you run an incident, and how the team learns afterwards.

## Pages

- [SLOs, Incidents & Postmortems](./01-slos-incidents-and-postmortems.md) — 12 questions: SLI/SLO/SLA, error budgets and policies, setting SLOs, on-call, incident roles, incident lifecycle (with diagram), runbooks, blameless postmortems, capacity planning, chaos engineering, a latency-after-deploy debugging scenario, production readiness reviews.

## What interviewers look for

- Reliability targets derived from user journeys.
- "Mitigate first, root-cause later" as a reflex.
- Blameless learning with action items that actually get done.

## Related

- The signals you'll use: [Observability & OpenTelemetry](../telemetry/02-observability-with-opentelemetry.md)
- Kubernetes debugging drills: [Kubernetes Operations & Debugging](../orchestration/02-kubernetes-operations-and-debugging.md)
- Rollback mechanics: [Pipeline Design & Release Strategies](../ci-cd-and-releases/02-pipeline-design-and-release-strategies.md)
