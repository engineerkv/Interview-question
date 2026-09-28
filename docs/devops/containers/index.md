---
sidebar_position: 0
sidebar_label: Overview
description: "Containers for production: how images work, secure Dockerfiles, Compose, secrets, registries and graceful shutdown."
---

# Containers (Docker)

> **Reviewed:** 2026-09 · **Level:** Senior / Tech Lead · **Type:** Foundational

Containers are the unit of delivery for almost every modern pipeline. Senior-level questions focus on *why* things work (layers, namespaces, signals) and *how* you'd harden and speed up builds.

## Pages

- [Docker in Production](./01-docker-in-production.md) — 10 questions: image vs container internals, layer caching, a production Dockerfile, image size, non-root hardening, Compose, secrets, registries and tagging, healthchecks, graceful shutdown.
- Introductory Docker questions (image vs container, multi-stage builds, reducing size, Compose, secrets, Kubernetes vs Docker) are in [Git, Docker, CI/CD, Tooling](../ci-cd-and-releases/01-git-docker-ci-cd-tooling.md).

## What interviewers look for

- You can explain a container as an isolated Linux process, not a mini VM.
- You write Dockerfiles that cache well, run as non-root and shut down cleanly.
- You never bake secrets into images and you deploy immutable, traceable tags.

## Next

Continue to [CI/CD & Releases](../ci-cd-and-releases/index.md), then [Kubernetes](../orchestration/index.md).
