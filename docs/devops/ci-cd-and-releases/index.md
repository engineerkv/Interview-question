---
sidebar_position: 0
sidebar_label: Overview
description: "CI/CD and release engineering: pipeline design, artifact promotion, progressive delivery, rollbacks and safe migrations."
---

# CI/CD & Releases

> **Reviewed:** 2026-09 · **Level:** Senior / Tech Lead · **Type:** Foundational

A Tech Lead is expected to own how code gets to production: how fast, how safely, and how it's undone when something breaks.

## Pages

- [Git, Docker, CI/CD, Tooling](./01-git-docker-ci-cd-tooling.md) — 20 questions (Q190–Q209): merge vs rebase, cherry-pick, conflicts, GitFlow vs trunk, Docker basics, Kubernetes vs Docker, pipeline stages, blue-green vs canary, zero-downtime deploys, Postman, npm/Yarn and dependency management.
- [Pipeline Design & Release Strategies](./02-pipeline-design-and-release-strategies.md) — 10 questions: designing a pipeline, artifact promotion, pipeline speed, a GitHub Actions workflow, release strategies, feature flags, rollbacks, expand/contract migrations, environments, DORA metrics.

## What interviewers look for

- "Build once, promote many" and immutable artifacts.
- Deploy is separate from release (flags, canaries).
- Rollback is designed in, including database compatibility.

## Related

- Team workflows: [Branching & Team Workflows](../git-and-collaboration/01-branching-and-team-workflows.md)
- Pipeline security: [DevSecOps & Supply Chain](../security-and-supply-chain/01-devsecops-and-supply-chain.md)
- GitOps delivery: [Platform Engineering & GitOps](../platform-engineering/01-platform-engineering-and-gitops.md)
