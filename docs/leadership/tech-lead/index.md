---
sidebar_position: 0
sidebar_label: Overview
description: "Overview of the technical leadership section: architecture decisions, design reviews, mentoring, delivery, stakeholders, tech debt and incidents."
---

# Technical Leadership

> **Reviewed:** 2026-09 · **Level:** Senior / Tech Lead · **Type:** Foundational

Scenario-style questions on the day-to-day work of a Tech Lead: making and recording decisions, raising the bar through reviews and standards, growing people, delivering predictably, communicating with stakeholders, managing quality, and leading through incidents and disagreements. Every page uses the same format: a short spoken answer, how to think about it, an example, trade-offs, and a one-line takeaway.

---

## Learning order

```mermaid
flowchart LR
    decisions["1. Architecture decisions"] --> reviews["2. Design reviews and standards"]
    reviews --> people["3. Mentoring and hiring"]
    people --> delivery["4. Planning, estimation, delivery"]
    delivery --> stakeholders["5. Stakeholders and communication"]
    stakeholders --> debt["6. Tech debt and quality"]
    debt --> incidents["7. Incidents and disagreements"]
```

| # | Page | Questions | Focus |
| --- | --- | --- | --- |
| 1 | [Architecture decisions](./01-architecture-decisions.md) | 6 | ADRs, RFCs, design docs, trade-offs, build vs buy, reversible decisions |
| 2 | [Design reviews and standards](./02-design-reviews-and-standards.md) | 5 | RFC lifecycle, running reviews, standards, tech radar |
| 3 | [Mentoring and hiring](./03-mentoring-and-hiring.md) | 6 | Mentoring, feedback, promotions, interviews, rubrics, bias |
| 4 | [Planning, estimation and delivery](./04-planning-estimation-delivery.md) | 7 | Estimation, slicing epics, prioritization, delegation, risk, scope |
| 5 | [Stakeholders and communication](./05-stakeholders-and-communication.md) | 5 | Stakeholder management, saying no, cross-team work, status updates |
| 6 | [Tech debt and quality](./06-tech-debt-and-quality.md) | 6 | Debt management, speed vs quality, migrations |
| 7 | [Incidents and disagreements](./07-incidents-and-disagreements.md) | 6 | Incident command, postmortems, disagreements, disagree and commit |

Total: 41 questions.

---

## How to use this section

- Read each question and answer it out loud before reading the model answer. Aim for 30 to 60 seconds.
- For each question, attach one real story from your own experience. Build these into your story bank using the [STAR method](../behavioral/01-star-method.md).
- Practice the scenario versions in [Tech Lead scenarios](../behavioral/04-tech-lead-scenarios.md).
- Revise with the [Leadership cheatsheet](../cheatsheet.md) before the interview.

> **Interview tip:** Tech Lead interviews reward *structure* and *trade-off awareness* more than any single "right" answer. Name the options, state your criteria, make a decision, and say what would make you change it.

## Related sections

- [Code reviews](../code-reviews/question-index.md)
- [Behavioral interviews](../behavioral/index.md)
- [System design case studies](../../case-studies/index.md)
- [DevOps and production engineering](../../devops/index.md)

---

## References

- [StaffEng guides](https://staffeng.com/guides/)
- [ADR GitHub organization](https://adr.github.io/)
- [DORA research](https://dora.dev/)
- [Google SRE Book: Postmortem Culture](https://sre.google/sre-book/postmortem-culture/)
