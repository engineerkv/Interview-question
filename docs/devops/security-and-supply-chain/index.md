---
sidebar_position: 0
sidebar_label: Overview
description: "DevSecOps and software supply chain security: secrets, IAM, network policies, scanning, SBOMs, signing and pipeline hardening."
---

# Security & Supply Chain

> **Reviewed:** 2026-09 · **Level:** Senior / Tech Lead · **Type:** Foundational (with Emerging topics)

Senior engineers are expected to build security into the delivery system, not bolt it on. Supply-chain security — proving what you ship and where it came from — is an increasingly common interview topic.

## Pages

- [DevSecOps & Supply Chain](./01-devsecops-and-supply-chain.md) — 10 questions: shift-left in practice, secrets management, least-privilege IAM, CI/CD hardening with OIDC, NetworkPolicies, dependency and image scanning, SBOMs, signing and SLSA, OWASP Top 10, policy as code.

## What interviewers look for

- No long-lived credentials anywhere a short-lived identity will do.
- Prioritising findings by exploitability rather than raw counts.
- Enforcement through automation with an audit-first rollout.

## Related

- Container hardening: [Docker in Production](../containers/01-docker-in-production.md)
- Pod security and RBAC: [Kubernetes Operations & Debugging](../orchestration/02-kubernetes-operations-and-debugging.md)
- Secrets in IaC: [Terraform & IaC Practices](../infrastructure-as-code/01-terraform-and-iac-practices.md)
