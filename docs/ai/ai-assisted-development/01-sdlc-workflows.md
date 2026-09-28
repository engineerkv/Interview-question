---
sidebar_position: 1
sidebar_label: "SDLC Workflows & Prompts"
description: "Practical AI-assisted workflows with reusable prompt templates across the software development lifecycle."
---

# SDLC Workflows and Prompt Templates

> **Reviewed:** 2026-09 · **Level:** Senior / Tech Lead · **Type:** Emerging (workflows are evolving; the verification principles are Foundational)

These workflows work with most AI coding tools (IDE agents, terminal agents, chat assistants). Each has a reusable prompt template. Replace `{{placeholders}}`, keep the structure, and store the templates your team likes in the repository (see [context engineering](./03-context-engineering.md)).

**Patterns that apply to every template:**

- **Give context, constraints and a definition of done.** What, why, where, and how you will verify.
- **Plan before code.** Ask for a plan, review it, then implement in steps.
- **Ask for assumptions and questions.** Make the model surface what it does not know.
- **Keep diffs small.** One concern per change.
- **Verify with tools, not trust.** Tests, type checks, linters, running the code.

## Workflow 1. Understanding an unfamiliar codebase

Use when joining a team, reviewing an unfamiliar area, or before changing legacy code.

```text
I am new to this repository and need to understand {{area, e.g. "how order checkout works"}}.

Please:
1. Identify the entry points (routes, handlers, jobs, CLI commands) for this area.
2. Trace the main request/data flow step by step, naming files and functions.
3. List the external dependencies (databases, queues, third-party APIs) it touches.
4. Point out non-obvious conventions, feature flags, or configuration that affect behaviour.
5. List anything you are unsure about or could not find, rather than guessing.

Cite file paths for every claim. Do not modify any files.
```

**Verify:** open the cited files and step through one flow with a debugger or logs. Ask the model to produce a sequence diagram, then check it against the code.

## Workflow 2. Converting requirements into an implementation plan

```text
Here is a feature requirement:
{{paste user story / ticket / PRD excerpt}}

Relevant context:
- Affected services/modules: {{list}}
- Constraints: {{e.g. no schema changes to table X, must be backward compatible, p95 < 200ms}}

Produce an implementation plan:
1. Clarifying questions and ambiguities in the requirement (list first).
2. Assumptions you are making.
3. Step-by-step tasks, each small enough for one PR, with files likely to change.
4. Data model / API changes and migration strategy.
5. Risks (security, performance, backward compatibility) and how to mitigate them.
6. Test plan: unit, integration, e2e cases including edge cases.
7. Rollout plan (feature flag, migration order, rollback).

Do not write code yet.
```

**Verify:** resolve the clarifying questions with the product owner before implementing; review the plan like a design doc.

## Workflow 3. Generating and reviewing technical designs

Generating options:

```text
We need to design {{problem}}. Context: {{scale, SLAs, team skills, existing stack}}.

Propose 2–3 design options. For each:
- Architecture summary (components and data flow)
- Pros, cons, and operational cost
- Failure modes and how they are handled
- What would make this option the wrong choice

Then recommend one and explain what information would change your recommendation.
```

Reviewing an existing design:

```text
Act as a critical senior reviewer for this design document:
{{paste design}}

Identify:
1. Unstated assumptions
2. Missing failure modes (partial failure, retries, idempotency, data loss)
3. Security and privacy concerns
4. Scalability bottlenecks
5. Operational gaps (monitoring, alerting, rollback)
6. Questions the author should answer before approval

Be specific and reference sections. Do not rewrite the design.
```

**Verify:** the design decision is made by humans in design review. Use AI critique as an extra reviewer, not the approver.

## Workflow 4. Implementing features

```text
Implement step {{N}} of the approved plan: {{step description}}.

Constraints:
- Follow the conventions in {{rules file / example file path}}.
- Only change files needed for this step; list any other changes you think are needed instead of making them.
- Do not add new dependencies without asking.
- Keep public APIs backward compatible.

Definition of done:
- Code compiles and passes type checks
- Unit tests added/updated for new behaviour, including {{edge cases}}
- Existing tests pass: run `{{test command}}`

After implementing, summarize what changed, why, and anything I should review carefully.
```

**Verify:** read every line of the diff, run tests locally, check for unnecessary changes.

## Workflow 5. Fixing bugs

```text
Bug report: {{description, expected vs actual behaviour}}
Reproduction steps: {{steps or failing test}}
Relevant logs / stack trace:
{{paste, with secrets and PII removed}}

Please:
1. First write a failing test that reproduces the bug.
2. Explain the root cause, citing code.
3. Propose the minimal fix, and alternatives if the root cause is deeper.
4. Implement the fix and confirm the new test passes and existing tests still pass.
5. Note any other places with the same pattern that may have the same bug.
```

**Verify:** the failing test must fail before the fix and pass after. Watch for fixes that only mask symptoms (catching and ignoring exceptions).

## Workflow 6. Generating unit, integration and end-to-end tests

Unit tests:

```text
Write unit tests for {{function/class}} in {{file}} using {{test framework}}.
Follow the style of {{existing test file}}.
Cover: normal cases, boundary values, invalid input, error paths, and {{domain-specific edge cases}}.
Do not change the implementation. If you find behaviour that looks like a bug, list it instead of encoding it in a test.
Each test name should describe the behaviour being verified.
```

Integration tests:

```text
Write integration tests for {{API endpoint / service interaction}}.
Use {{real test database / testcontainers / existing fixtures}}; mock only {{external third-party services}}.
Cover success, validation errors, authorization failures, idempotency on retry, and concurrent requests where relevant.
```

End-to-end tests:

```text
Write an end-to-end test with {{e.g. Playwright/Cypress}} for the user journey: {{journey}}.
Use stable selectors ({{data-testid convention}}), no fixed sleeps, and clean up created data.
Keep it to the critical path; list additional scenarios that should be covered at lower test levels instead.
```

**Verify:** mutate the implementation (break it deliberately) and confirm tests fail. AI-generated tests commonly assert on whatever the code currently does, including bugs, or mock so much they test nothing.

## Workflow 7. Debugging and root cause analysis

```text
Symptom: {{what is observed, since when, how often}}
Recent changes: {{deploys, config changes, dependency bumps}}
Evidence: {{logs, metrics, traces — redacted}}

Help me debug systematically:
1. List hypotheses ranked by likelihood given the evidence.
2. For each, the cheapest check that would confirm or rule it out.
3. What additional data would most reduce uncertainty.
Do not propose a fix until we have confirmed the root cause.
```

For a postmortem draft:

```text
Using this incident timeline and notes: {{paste}}
Draft a blameless postmortem: summary, impact, timeline, root cause(s), contributing factors, what went well, action items with owners as placeholders.
Mark any statement not supported by the notes as [NEEDS CONFIRMATION].
```

**Verify:** hypotheses are checked against real data. Humans own incident decisions and postmortem conclusions.

## Workflow 8. Refactoring

```text
Refactor {{module/function}} to {{goal: e.g. separate I/O from business logic, remove duplication with X}}.

Rules:
- Behaviour must not change. First confirm existing tests cover the behaviour; if not, add characterization tests before refactoring.
- Make the change in small, separately reviewable steps; stop after each step and summarize.
- Do not rename public APIs or change serialized formats.
- Keep diff noise (formatting, reordering) out of the change.
```

**Verify:** tests pass before and after each step; review diffs for behaviour changes hidden in "cleanup".

## Workflow 9. Documentation

```text
Write {{README section / ADR / API docs / runbook}} for {{component}}.
Audience: {{new team members / API consumers / on-call engineers}}.
Base it only on the code and files in {{paths}}; cite file paths for any behaviour described.
Include: purpose, how to run it locally, configuration, key flows, failure modes, and how to get help.
Mark anything you had to infer as [VERIFY].
```

**Verify:** a person unfamiliar with the component follows the doc and reports gaps.

## Workflow 10. PR preparation and review

Preparing your PR:

```text
Here is my diff: {{diff or branch}}. Related ticket: {{link/summary}}.
Write a PR description with: summary of the change, motivation, notable implementation decisions, how it was tested, risks and rollback plan, and screenshots needed (list them).
Then review the diff as a strict reviewer and list: possible bugs, missing tests, security concerns, and unclear naming. I will fix these before requesting human review.
```

Assisting a human reviewer:

```text
Summarize this PR for a reviewer: what changed, which files matter most, and where the riskiest logic is.
List questions a reviewer should ask the author. Do not approve or reject.
```

**Verify:** a human reviewer reads the code, not just the summary. See also [automated review processes](../../leadership/code-reviews/automated-review-process.md).

## Workflow 11. Onboarding and junior productivity

```text
I am a junior engineer working on {{task}}. Act as a mentor, not a code generator.
1. Explain the concepts I need to understand for this task, with pointers to files in this repo.
2. Ask me how I would approach it, and give feedback on my approach.
3. Give hints rather than full solutions unless I ask explicitly.
4. When I write code, review it and explain the "why" behind each suggestion.
```

**Verify:** juniors should be able to explain every line they submit. Mentors review both the code and the learning.

## Q1. Walk me through how you use AI to implement a medium-sized feature

**Short answer:** I start by giving the tool the requirement and relevant code context and asking for clarifying questions and a plan, not code. I review and correct the plan, then implement it one small step at a time, each with tests, running the test suite and type checks after each step. I read every line of the diff, write the PR description with what I verified, and the change goes through normal human review and CI.

**How it works:** The key moves are separating planning from implementation, keeping each generated diff reviewable, and using deterministic tools (tests, compiler, linters) as the arbiter of correctness.

**Example:** For adding export-to-CSV to a reports page: plan (API endpoint, streaming for large reports, permission checks, tests), then step 1 backend endpoint + tests, step 2 frontend button + e2e test, step 3 docs. Each step a separate commit.

**Trade-offs and pitfalls:**

- One giant prompt for the whole feature produces large diffs that are hard to review and often wrong in subtle ways.
- Plans can look plausible and miss constraints only humans know (a downstream consumer, a contractual SLA).

**Remember:** Plan, small steps, tests each step, read the diff, normal review.

## Q2. How do you prevent AI-generated tests from being meaningless?

**Short answer:** I ask for tests that describe behaviour and edge cases, not implementation, forbid the model from changing the implementation while writing tests, review that assertions check meaningful outcomes, and sanity-check by breaking the code to see tests fail. Mutation testing, where available, makes this systematic.

**How it works:** Common failure modes: asserting on current (buggy) behaviour, excessive mocking, tautological assertions, and tests that only cover the happy path.

**Example:** Generated tests for a discount function all passed, but deliberately changing `>=` to `>` in the implementation did not fail any of them — the boundary case was missing. Adding an explicit boundary test fixed it.

**Trade-offs and pitfalls:** High coverage from generated tests can create false confidence; coverage measures execution, not verification.

**Remember:** A test that never fails is not a test. Break the code to prove it.

## Q3. How do you use AI for debugging without it sending you down the wrong path?

**Short answer:** I give it evidence (symptoms, logs, recent changes) and ask for ranked hypotheses with the cheapest check for each — not a fix. I confirm the root cause with real data or a failing test before changing code. AI is good at breadth (listing possibilities, reading unfamiliar code quickly); I stay responsible for evidence-based narrowing.

**How it works:** Models are biased toward confident, common explanations. Forcing a hypothesis → check → evidence loop keeps the investigation grounded.

**Example:** For intermittent timeouts after a deploy, the model listed connection pool exhaustion, a slow new query, and DNS issues. Checking pool metrics confirmed exhaustion caused by a missing connection release in a new error path.

**Trade-offs and pitfalls:** Pasting production logs may leak PII or secrets — redact first and use approved tools only.

**Remember:** Hypotheses from AI, confirmation from evidence.

## Q4. How can AI help juniors without stunting their growth?

**Short answer:** Use AI as a tutor: explanations, hints, and review feedback rather than finished solutions for learning tasks. Require juniors to explain their code in review, pair on AI-assisted work, and reserve some tasks for doing without AI to build fundamentals. Seniors should model good verification habits.

**How it works:** Skill atrophy risk is real when people accept code they do not understand; the mitigation is making understanding a review requirement. See [validation and human oversight](./05-validation-and-human-oversight.md).

**Example:** A team's onboarding plan uses the mentor-mode prompt above for the first month, with weekly pairing sessions where the junior explains an AI-assisted change end to end.

**Trade-offs and pitfalls:** Banning AI for juniors entirely is hard to enforce and leaves them unprepared; structured use is better.

**Remember:** Explain-every-line is the rule that protects learning.

## Practical checklist

- [ ] Asked for questions and a plan before code
- [ ] Each change is small and has a clear definition of done
- [ ] Tests written or updated and shown to fail without the change
- [ ] Type checks, linters and full test suite pass
- [ ] Every line of the diff read and understood
- [ ] No secrets, PII or restricted data pasted into prompts
- [ ] PR description states what was verified and how

## References

Reviewed 2026-09.

- Anthropic documentation (prompt engineering, Claude Code): https://docs.anthropic.com/
- GitHub Copilot documentation: https://docs.github.com/en/copilot
- Cursor documentation: https://docs.cursor.com/
- OpenAI platform documentation (prompting guides): https://platform.openai.com/docs
- Related: [Automated review process](../../leadership/code-reviews/automated-review-process.md)
