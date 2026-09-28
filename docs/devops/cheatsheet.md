---
sidebar_position: 100
sidebar_label: Cheatsheet
description: "Condensed revision notes and a readiness checklist for the whole DevOps and production engineering section."
---

# DevOps Cheatsheet

> **Reviewed:** 2026-09 · **Level:** Senior / Tech Lead · **Type:** Foundational

Quick revision for the whole section. Each block links to the full page.

## Git & Collaboration

[Full page](./git-and-collaboration/01-branching-and-team-workflows.md)

- Pick the branching model that keeps code away from `main` for the shortest time your release model allows.
- Trunk-based = short-lived branches + feature flags + fast CI + merge queue.
- Release branches only when you support multiple versions (mobile, SDKs, on-prem).
- CODEOWNERS routes reviews (last match wins; use teams); branch protection enforces them.
- Small PRs with a clear "why", green CI before review, fast turnaround.
- Monorepo needs affected-only builds; polyrepo needs dependency-upgrade discipline.
- Hotfix: fix on `main`, cherry-pick to release branch.
- Leaked secret: rotate first, clean history second.

## Containers

[Full page](./containers/01-docker-in-production.md)

- Container = isolated Linux process (namespaces + cgroups), shares host kernel.
- Order Dockerfiles stable → volatile; copy lockfiles before source.
- Multi-stage: build fat, ship thin. Pin base images (digest in prod).
- Run as non-root, read-only root FS, drop capabilities, never `--privileged` by default.
- Exec-form `CMD`, handle SIGTERM, drain within the grace period.
- No secrets in layers, `ARG` or `ENV`; use BuildKit secret mounts and runtime injection.
- Tag with git SHA, deploy by digest, never rely on `:latest`.

## CI/CD & Releases

[Full page](./ci-cd-and-releases/02-pipeline-design-and-release-strategies.md)

- Fast checks first; build once; promote the same artifact through environments.
- Speed: cache on lockfile hash, parallelise, shard tests, affected-only builds.
- Least-privilege workflow permissions, OIDC to the cloud, actions pinned by SHA.
- Deploy ≠ release: canary, blue-green, feature flags, dark launches.
- Flags need owners and expiry dates.
- Rollback order: flag off → shift traffic → redeploy previous artifact.
- Migrations: expand → dual-write → backfill → switch reads → stop old writes → contract.
- DORA: deployment frequency, lead time, change failure rate, time to restore.

## Cloud

[Full page](./cloud/02-multi-cloud-networking-and-cost.md)

- Learn categories: compute, containers, functions, object/block/file storage, SQL/NoSQL, queues, IAM.
- Multi-cloud is a business decision; portability has a price.
- VPC: public subnets for load balancers and NAT; private for apps; isolated for data; spread across AZs.
- Security groups are stateful allow-lists; reference groups, not CIDRs.
- Private endpoints for managed services to avoid NAT costs and public paths.
- RTO/RPO pick the DR pattern: backup/restore → pilot light → warm standby → active-active.
- Cost drivers: idle compute, data transfer/NAT, forgotten storage, always-on non-prod.

## Kubernetes

[Architecture](./orchestration/01-kubernetes-architecture-and-workloads.md) · [Operations](./orchestration/02-kubernetes-operations-and-debugging.md)

- Desired state in etcd via API server; controllers reconcile; scheduler places; kubelet runs.
- Deployment → ReplicaSet → Pods; Service = stable IP over Ready Pods; Ingress/Gateway = external HTTP routing.
- Secrets are base64, not encrypted — encryption at rest, RBAC, external secret manager.
- Readiness gates traffic; liveness restarts; startup buys time. Don't check the DB in liveness.
- Requests schedule, limits enforce. CPU over limit throttles; memory over limit OOM-kills (137).
- QoS: Guaranteed > Burstable > BestEffort (eviction order reversed).
- HPA scales Pods on metric vs target; Cluster Autoscaler/Karpenter add nodes; KEDA for events.
- Deployment (stateless), StatefulSet (identity + storage), DaemonSet (per node), Job/CronJob (run to completion).
- CrashLoopBackOff: `describe` + `logs --previous` + exit code.
- Pending: scheduling problem — read events (resources, affinity, taints, PVC zone, quota).
- Service not working: check EndpointSlices first.
- PDBs protect against voluntary disruption; spread replicas across zones.
- Managed K8s removes control-plane toil, not platform ownership.

## Infrastructure as Code

[Full page](./infrastructure-as-code/01-terraform-and-iac-practices.md)

- Terraform/OpenTofu: multi-cloud, HCL. CloudFormation/CDK: AWS-native. Pulumi: general-purpose languages.
- State: remote, locked, encrypted, versioned, split by system and environment.
- Reusable modules, thin environment roots, separate accounts per environment.
- PR runs fmt/validate/lint/policy + plan; pipeline applies the saved plan.
- Watch for replace/destroy on stateful resources; `prevent_destroy` and deletion protection.
- Scheduled `plan -detailed-exitcode` detects drift.
- Secrets end up in state — treat state as sensitive.
- `import` and `moved` blocks for safe adoption and refactors.

## Telemetry & Observability

[Full page](./telemetry/02-observability-with-opentelemetry.md)

- Metrics tell you *that*, traces tell you *where*, logs tell you *why*.
- RED for services, USE for resources, golden signals for user-facing view.
- OpenTelemetry: API + SDK + auto-instrumentation + Collector + OTLP + semantic conventions.
- Context propagation via W3C `traceparent`, including through queues.
- Page on symptoms (SLO burn rate); causes go to dashboards and tickets.
- Keep metric labels low-cardinality; IDs belong in traces and logs.
- Propagate trace context from browser RUM to backend APM.

## Reliability & Incidents

[Full page](./reliability-and-incidents/01-slos-incidents-and-postmortems.md)

- SLI measures, SLO targets, SLA promises (SLA looser than SLO).
- Error budget = 100% − SLO; 99.9% over 30 days ≈ 43 minutes.
- Error budget policy agreed in advance; exhausted budget shifts work to reliability.
- Incident roles: Incident Commander, ops lead, communications, scribe.
- Mitigate first, root-cause later.
- Runbooks linked from alerts, written for a stranger at 3 a.m.
- Blameless postmortems with owned, dated action items.
- Capacity: unit capacity via load tests, headroom for zone loss, check hard limits.
- Chaos engineering: hypothesis, small blast radius, abort conditions.

## Security & Supply Chain

[Full page](./security-and-supply-chain/01-devsecops-and-supply-chain.md)

- Shift left, shield right; a few high-signal blocking checks.
- Secrets in a manager, identity-based access, short-lived credentials, automated rotation.
- One IAM identity per workload, resource-scoped, reviewed.
- OIDC federation for CI, with tight trust conditions (repo + branch/environment).
- Kubernetes NetworkPolicies: default-deny, then allow; remember DNS egress.
- Prioritise CVEs by exploitability and reachability; automate updates.
- SBOM (SPDX/CycloneDX) turns "are we affected?" into a query.
- Sign in CI (Sigstore), record provenance (SLSA), verify at admission.
- Policy as code: audit mode first, then enforce.

## Platform Engineering (Emerging)

[Full page](./platform-engineering/01-platform-engineering-and-gitops.md)

- Platform = internal product that reduces cognitive load; developers are customers.
- Golden paths: opinionated, optional, easiest route; shared versioned building blocks.
- GitOps: Git is desired state; in-cluster agent pulls and reconciles; revert to roll back.
- Self-service with guardrails, not ticket gates.
- Success = voluntary adoption + developer outcomes (DORA, satisfaction).

## Readiness checklist

Use this before an interview (can you explain each item in under a minute?) and before a service goes live.

- [ ] I can justify a branching strategy for a given release model.
- [ ] I can write a multi-stage, non-root Dockerfile with good layer caching.
- [ ] I can sketch a pipeline that builds once and promotes the same artifact.
- [ ] I can compare rolling, blue-green, canary and feature flags, including rollback.
- [ ] I can explain expand/contract migrations step by step.
- [ ] I can draw a VPC with public, private and data subnets across AZs.
- [ ] I can explain the Kubernetes control plane and the Ingress → Service → Pod path.
- [ ] I can configure probes, requests/limits and an HPA, and explain each choice.
- [ ] I can debug CrashLoopBackOff, OOMKilled and Pending Pods out loud.
- [ ] I can explain Terraform state, locking, plan review and drift.
- [ ] I can define SLIs/SLOs and an error budget policy for a user journey.
- [ ] I can explain OpenTelemetry's architecture and context propagation.
- [ ] I can run an incident as Incident Commander and lead a blameless postmortem.
- [ ] I can explain OIDC for CI, SBOMs, and signing with verification at deploy.
- [ ] I can explain GitOps pull reconciliation and when a platform team is worth it.
