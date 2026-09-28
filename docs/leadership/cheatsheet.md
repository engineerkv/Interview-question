---
sidebar_position: 20
sidebar_label: Cheatsheet
description: Quick revision for Tech Lead, code review, and behavioral interviews.
---

# Leadership Cheatsheet

> **Review time:** 20 minutes · **Priority:** Night before a Tech Lead loop

## Decision framework

- Name 2–3 options.
- State criteria (user impact, time, risk, reversibility).
- Pick one and say what would change your mind.
- Write it down (ADR / RFC) if the decision outlives the meeting.

## Code review

- Human: architecture, correctness, API contracts, mentoring.
- Automated: lint, types, tests, SAST, secrets, size budgets.
- AI review is advisory. Do not auto-merge on AI alone.

## Delivery

- Slice work so a vertical slice ships.
- Estimate with ranges and risks, not fake precision.
- Delegate outcomes, not just tasks.
- Protect the error budget when reliability is already burning.

## Behavioral (STAR)

- Situation: one sentence of context.
- Task: your responsibility.
- Action: what you did.
- Result: a concrete outcome.
- Takeaway: what you would repeat or change.

## Related

- [Technical leadership](./tech-lead/index.md)
- [Automated review process](./code-reviews/automated-review-process.md)
- [STAR method](./behavioral/01-star-method.md)
