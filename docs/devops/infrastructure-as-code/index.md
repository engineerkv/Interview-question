---
sidebar_position: 0
sidebar_label: Overview
description: "Infrastructure as Code for Tech Leads: tool choice, Terraform state, modules, drift, review workflows and secrets."
---

# Infrastructure as Code

> **Reviewed:** 2026-09 · **Level:** Senior / Tech Lead · **Type:** Foundational

IaC questions test whether you can change production infrastructure safely and repeatably as a team.

## Pages

- [Terraform & IaC Practices](./01-terraform-and-iac-practices.md) — 10 questions: why IaC, Terraform vs CloudFormation vs Pulumi, state and locking, modules and environments, drift, plan review and apply, secrets, testing, import and refactoring, IaC vs GitOps boundaries.

## What interviewers look for

- Remote, locked, encrypted state split by blast radius.
- Plans reviewed in PRs and applied from pipelines, never laptops.
- Guardrails against destructive changes and secrets in code.

## Related

- The resources you'll provision: [Multi-Cloud, Networking & Cost](../cloud/02-multi-cloud-networking-and-cost.md)
- Deploying into clusters: [Platform Engineering & GitOps](../platform-engineering/01-platform-engineering-and-gitops.md)
