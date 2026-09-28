---
sidebar_position: 0
sidebar_label: Overview
description: "Kubernetes for Senior and Tech Lead interviews: architecture, workloads, configuration, scaling, security and production debugging."
---

# Kubernetes

> **Reviewed:** 2026-09 · **Level:** Senior / Tech Lead · **Type:** Foundational

Kubernetes is usually the deepest DevOps topic in senior interviews. Expect to explain the architecture, write or read YAML, and debug a broken Pod out loud.

## Pages

- [Architecture & Workloads](./01-kubernetes-architecture-and-workloads.md) — 8 questions: control plane and nodes, Pods/Deployments/Services/Ingress (with request-flow diagram), ConfigMaps vs Secrets, probes, requests/limits and QoS, HPA, workload types, persistent storage.
- [Operations & Debugging](./02-kubernetes-operations-and-debugging.md) — 9 questions: namespaces and RBAC, rolling updates and rollback, CrashLoopBackOff, OOMKilled, Pending Pods, Service debugging, PodDisruptionBudgets, Pod security, managed Kubernetes trade-offs.

## Suggested order

1. Understand reconciliation and the control plane (Q1 of page 1).
2. Learn the request path Ingress → Service → Pod.
3. Master probes and resources — they cause most production incidents.
4. Practise the debugging walkthroughs on page 2 until you can say them without notes.

## Related

- Containers first: [Docker in Production](../containers/01-docker-in-production.md)
- Release strategies on Kubernetes: [Pipeline Design & Release Strategies](../ci-cd-and-releases/02-pipeline-design-and-release-strategies.md)
- GitOps delivery: [Platform Engineering & GitOps](../platform-engineering/01-platform-engineering-and-gitops.md)
