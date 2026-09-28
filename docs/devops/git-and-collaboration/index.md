---
sidebar_position: 0
sidebar_label: Overview
description: "Git and team collaboration at Tech Lead level: branching strategies, ownership, PR hygiene and repository layout."
---

# Git & Collaboration

> **Reviewed:** 2026-09 · **Level:** Senior / Tech Lead · **Type:** Foundational

At senior level, Git questions move from "what does rebase do?" to "how should *this team* work?". Interviewers want to hear how you balance delivery speed, safety and ownership.

## Pages

- [Branching & Team Workflows](./01-branching-and-team-workflows.md) — 10 questions: choosing a branching strategy, trunk-based development, CODEOWNERS, PR hygiene, monorepo vs polyrepo, conflicts at scale, branch protection, versioning, hotfixes, keeping secrets out of Git.
- Git mechanics (merge vs rebase, cherry-pick, fixing conflicts, GitFlow vs trunk) live in [Git, Docker, CI/CD, Tooling](../ci-cd-and-releases/01-git-docker-ci-cd-tooling.md).

## What interviewers look for

- You pick a strategy based on release model, not habit.
- You can explain how small PRs, fast CI and feature flags reinforce each other.
- You treat ownership (CODEOWNERS, branch protection) as enforcement of team agreements.

## Next

Continue to [Containers (Docker)](../containers/index.md).
