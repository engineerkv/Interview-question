---
sidebar_position: 1
sidebar_label: Content standards
description: Format profiles and modernization rules for interview answers on this site.
---

# Content Standards

> **Reviewed:** 2026-09

These rules replace the older root `rule.md` playbook. Quality and spoken-interview clarity beat filling every heading on every page.

## Language

- Write answers you can say out loud.
- Start with intuition, then mechanism, then production details.
- Prefer practical examples over theory dumps.
- Do not invent interview frequency, benchmark numbers, or unsupported industry claims.
- Label example capacity numbers as **assumptions for practice**.

## Format profiles

| Type | Required | Optional |
| --- | --- | --- |
| Tech drill | Short answer, practical example, key points | Trade-offs, code, follow-ups |
| Deep dive | Intuition → mechanism → example → production notes → summary | Mermaid, Extra Points |
| Coding / DSA | Problem, approach, code, complexity, edge cases | Alternate solutions, diagram |
| Case study | FE + backend HLD + scale + talking points | RADIO deep dive, AI/agentic scale-up |
| Agentic workflow | Pattern, example, loop diagram, human gates, summary | Failure catalog |
| DevOps / SRE | Situation, approach, flow diagram, trade-offs, summary | Runbook sketch |
| Behavioral | STAR + takeaway + follow-ups | Metrics |

Do not force the full 10-part template onto every question.

## Visuals

Add an example plus one of these when the topic is a flow, architecture, or trade-off:

- Mermaid architecture, sequence, or flowchart
- Comparison table
- Simple chart only when numbers help, labeled as illustrative

Animation is additive. Every animated mental model needs a static diagram and must respect `prefers-reduced-motion`.

## Modernization

- Current recommended practice is the primary answer.
- Keep legacy topics only when labeled **Legacy / migration** (Pages Router, class components, older Node patterns).
- After a folder pass, sync `question-index.md` and the cheatsheet.
- Add `Reviewed: YYYY-MM` on upgraded files.

## Numbering and files

- Use URL-safe names: `01-core-concepts.md`.
- Keep question numbers stable when relocating content (for example AWS Q95–Q117 now live under DevOps).
- Cross-link drills to deep dives instead of copying the same essay twice.

## Ownership of AI-generated drafts

AI can draft answers, diagrams, and checklists. A human must verify technical accuracy, security claims, and links before publish.
