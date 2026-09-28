---
sidebar_position: 3
sidebar_label: Repository assessment
description: Assessment of the original Markdown repo, migration decisions, remaining risks, and acceptance criteria.
---

# Repository Assessment

> **Reviewed:** 2026-09 · **Status:** Migration in progress on Docusaurus 3

This is the Phase 1 assessment, updated after the first migration into `docs/`.

## Original repo (before the site)

The repository was a GitHub-browsable Markdown knowledge base: frontend drills, frontend system design essays, Node/SQL/Mongo, backend system design, DSA, 18 FE-focused project writeups, puzzles, and one FE Lead code-review guide.

Honest counts from disk (not the old README):

- About 171 Markdown files
- About 1,307 discrete tech/DSA questions
- 24 frontend system-design topics
- 18 projects (README claimed 20)
- 50 puzzles

The old README claimed 1,639+ questions. That number was inflated.

## Limitations we found

1. No Docusaurus, search, CI, or GitHub Pages deploy.
2. Filenames like `01) Foo.md` were awkward for static URLs.
3. Frontend drills and frontend system design overlapped without a documented “drill vs deep dive” role.
4. DevOps lived inside backend system design (AWS, CloudWatch/New Relic, a thin Git/Docker/CI chapter). Kubernetes, IaC, SLOs, and GitOps were thin or missing.
5. Projects were frontend talking points, not full-stack case studies.
6. No AI engineering, agentic workflows, Python, Celery, RabbitMQ, or MinIO tracks.
7. No behavioral / Tech Lead question bank. Code review was manual only.
8. Some answers were mid-level or dated (Pages Router as default, class components as peer to hooks).

## What we preserved

- Conversational drill voice (short answer + trade-offs + example)
- DSA Problem → Approach → Solution → Complexity
- Deep frontend internals essays
- Backend system design breadth
- Existing code-review checklist
- Cheatsheets as revision pages
- Stable question numbers when chapters moved (AWS Q95–Q117, observability Q120–Q134, tooling Q190–Q209)

## Information architecture (current)

```text
docs/
├── intro/                  # How to use the site, paths, this assessment
├── fundamentals/           # JavaScript, TypeScript, DSA
├── frontend/               # HTML, CSS, React, Next, RN, architecture
├── backend/                # Node, SQL, Mongo, Python, Celery, RabbitMQ, MinIO, architecture
├── devops/                 # Git, Docker, K8s, CI/CD, cloud, IaC, telemetry, SRE, security, platform
├── case-studies/           # 18 projects, expanded toward full-stack
├── ai/                     # LLM, RAG, evals, AI-assisted SDLC
├── agentic-workflows/      # Agents, MCP, orchestration, human gates
├── leadership/             # Reviews, Tech Lead, behavioral
├── puzzles/
├── reference/              # Cheatsheet index
└── contributing/           # Content standards
```

Hosting: GitHub Pages **project site** at `https://engineerkv.github.io/Interview-question/` (`baseUrl: /Interview-question/`).

## Remaining work

| Item | Notes |
| --- | --- |
| All-folder modernization | Continue labeling legacy topics and updating defaults (App Router, OTel, New Architecture) |
| Case studies waves 2–3 | Wave-1 flagship files already have backend + scale + AI sections; remaining projects should match |
| Visuals | Mermaid is enabled; add diagrams on remaining deep pages that still lack one |
| Broken-link cleanup | Production build must resolve every local Markdown link |
| README | Must match the live site structure and honest counts |

## Acceptance criteria

- Existing valuable Q&A is preserved or intentionally moved with a stub pointer
- Dedicated DevOps, Python, Celery, RabbitMQ, MinIO, AI, and Agentic tracks exist
- Code reviews include an automated review process
- `npm run build` succeeds
- Search, light/dark, and Mermaid work on GitHub Pages paths
