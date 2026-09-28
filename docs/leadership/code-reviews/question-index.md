---
sidebar_position: 0
sidebar_label: "Question Index"
description: "Code review interview questions for Senior and Tech Lead roles with short model answers and links to the detailed pages."
---

# Code Review Question Index

> **Reviewed:** 2026-09 · **Level:** Senior / Tech Lead · **Type:** Foundational

Quick-revision list of the code review questions most often asked in Senior, Tech Lead and Engineering Lead interviews. Each answer is a spoken-length model answer; follow the links for depth.

Pages in this section:

1. [Manual review guide](./manual-review-guide.md): what a human reviewer looks for, with frontend examples.
2. [Automated review process](./automated-review-process.md): the end-to-end pipeline, CODEOWNERS, branch protection, bots.
3. [CI quality gates](./03-ci-quality-gates.md): each gate with configs, and legacy rollout.
4. [AI-assisted review](./04-ai-assisted-review.md): where AI fits and where it must not.
5. [Metrics and team adoption](./05-metrics-and-team-adoption.md): measuring review health and rolling out change.

---

## Q1. How would you automate code review for a 20-person team?

**Short answer:** Start with the pain points and a baseline of PR metrics. Then add quick wins: formatter, PR template, CODEOWNERS on team handles with load-balanced auto-assignment. Build a layered CI pipeline from cheap to expensive checks (lint, typecheck, tests, smoke e2e, build, security scans, budgets), run new checks as advisory first, then promote stable ones to required via branch protection. Add advisory AI review, keep human code-owner approval mandatory, and use a merge queue so main stays green.

**How to think about it:** Automate the deterministic, protect human attention for judgment, and roll out incrementally with the team's agreement.

**Example:** See the pipeline diagram and workflow in [automated review process](./automated-review-process.md).

**Trade-offs and pitfalls:** Big-bang enforcement, flaky required checks and noisy bots all erode trust.

**Remember:** Baseline, quick wins, advisory then required, measure.

## Q2. What should never be automated in code review?

**Short answer:** Judgment about whether the change solves the right problem, architecture and boundary decisions, naming and abstraction quality, security design such as the authorization model, the rollout and rollback plan, and the mentoring and knowledge-sharing side of review. Final approval for production code should always be a person who is accountable.

**How to think about it:** Tools see patterns in the diff; humans understand intent, context and consequences.

**Example:** A bot can flag string-built SQL; only a reviewer notices that a new endpoint lets any tenant read another tenant's invoices.

**Trade-offs and pitfalls:** Tools can *support* these areas (dependency rules for architecture, SAST for security) but not own them.

**Remember:** Machines check rules, humans check intent.

## Q3. How do you handle a PR that is too large?

**Short answer:** I do not try to review a huge PR line by line, because quality drops. I talk to the author, acknowledge the work, and help split it: separate refactors from behavior changes, extract preparatory changes, then stack the rest behind a feature flag. If it is urgent, I do a focused review of the riskiest parts with the author walking me through it, and we file follow-ups. Long term, I add a soft size warning and teach stacked PRs.

**How to think about it:** The goal is a reviewable change, not punishing the author. Ask why it got large: unclear scope, missing design review, fear of broken main?

**Example:** A 2,000-line PR becomes: rename refactor, new data model, API behind flag, UI.

**Trade-offs and pitfalls:** Splitting after the fact costs time; the cheaper fix is agreeing on the plan up front.

**Remember:** Split, stack, flag, and fix the upstream cause.

## Q4. What do you look for first when reviewing a PR?

**Short answer:** Context and design before details: read the description and linked issue, check the change solves the right problem in the right place, then correctness and edge cases, security, tests, and operability (logging, flags, migrations, rollback). Style last, and only if the linter does not already cover it.

**How to think about it:** Top-down review avoids polishing code that should not exist in its current shape.

**Example:** See the priorities in [manual review guide](./manual-review-guide.md).

**Trade-offs and pitfalls:** Starting with nits signals the wrong priorities and demotivates authors.

**Remember:** Design, correctness, risk, then style.

## Q5. How do you give review feedback that people actually act on?

**Short answer:** Be specific, explain the why, suggest a fix, and signal weight with prefixes like blocking, suggestion, nit and question. Ask questions when unsure, praise good work, and move long debates to a quick call with a written summary. Critique the code, never the person.

**How to think about it:** Feedback is a conversation between peers; clarity about severity avoids endless rounds.

**Example:** "blocking: this retry loop has no backoff, so a downstream outage would multiply traffic. Could we reuse `retryWithBackoff` from `lib/http`?"

**Trade-offs and pitfalls:** Too soft and important issues get missed; too harsh and people stop asking for review.

**Remember:** Specific, reasoned, weighted, kind.

## Q6. What is CODEOWNERS and how do you set it up well?

**Short answer:** A file mapping paths to owning users or teams; combined with branch protection it requires owner approval for changes to those paths. I use team handles, keep broad defaults first and specific paths later because the last match wins, protect the CODEOWNERS file and CI workflows themselves, and keep ownership granular enough to be meaningful without requiring many approvals per PR.

**How to think about it:** Ownership encodes accountability and routes reviews automatically.

**Example:** Payments and auth paths also require a security reviewers team.

**Trade-offs and pitfalls:** Individual owners create bottlenecks; overly fine-grained ownership creates approval fatigue.

**Remember:** Teams not people, last match wins, protect the file.

## Q7. Which checks should be required and which advisory?

**Short answer:** Required: deterministic, fast, high-value checks such as typecheck, tests, lint errors, secret scanning, new high-severity vulnerabilities and license violations. Advisory: AI review, style suggestions, complexity warnings, and any new check still being tuned. Budget checks like bundle size can block with a code-owner override.

**How to think about it:** A required check must be trustworthy; otherwise it trains people to bypass.

**Example:** See the fail-closed vs advisory table in [automated review process](./automated-review-process.md).

**Trade-offs and pitfalls:** A required job that sometimes does not report can silently block or leave a gap.

**Remember:** Deterministic blocks, probabilistic advises.

## Q8. How do you introduce quality gates on a legacy codebase?

**Short answer:** Baseline and ratchet. Measure current violations, run the gate advisory, block only new violations, and shrink the baseline through scheduled cleanup until the gate can be fully blocking. For TypeScript strictness, migrate folder by folder; for coverage, gate on changed code.

**How to think about it:** Stop the bleeding first, then pay down the debt visibly.

**Example:** Details in [CI quality gates](./03-ci-quality-gates.md).

**Trade-offs and pitfalls:** Big-bang cleanup PRs conflict with everyone's work and are unreviewable.

**Remember:** Baseline, block new, ratchet.

## Q9. How do you use AI in code review responsibly?

**Short answer:** As an advisory first pass that summarizes and flags likely bugs, configured with repository guidelines so it skips what the linter covers. It never approves, is never a required check, and never triggers auto-merge for production paths. I measure accepted-comment and false-positive rates during a trial and tune or drop it based on data.

**How to think about it:** AI suggests, CI enforces, humans approve.

**Example:** See [AI-assisted review](./04-ai-assisted-review.md).

**Trade-offs and pitfalls:** Rubber-stamping large AI-generated diffs is the biggest new risk.

**Remember:** Advisory, measured, human-approved.

## Q10. Reviews are taking days. How do you fix it?

**Short answer:** First measure where time goes: waiting for first review, many rounds, or slow CI. Then fix the biggest bottleneck: a review SLA for first response, load-balanced assignment, smaller PRs and stacks, faster CI with caching and affected-only runs, and design discussions before code so reviews are not where architecture gets debated.

**How to think about it:** Review delay is usually queueing, not review effort.

**Example:** See [metrics and team adoption](./05-metrics-and-team-adoption.md).

**Trade-offs and pitfalls:** Pushing for speed without depth leads to rubber-stamping; watch escaped defects alongside turnaround.

**Remember:** Measure the queue, then shorten it.

## Q11. How do you handle disagreement in a code review?

**Short answer:** Separate preference from principle. If it is a preference and the code meets the standard, the author's choice wins. If it is a correctness, security or standards issue, explain with evidence. If we still disagree after one or two rounds, move to a call, involve a third person or the code owner if needed, record the decision, and if it keeps recurring, turn it into a written standard or lint rule.

**How to think about it:** Reviews should converge; unresolved debates belong in standards, not individual PRs.

**Example:** Two engineers argue over error-handling style; the Tech Lead proposes a short ADR and a lint rule.

**Trade-offs and pitfalls:** Seniority should not automatically win; data and standards should.

**Remember:** Preference yields, principle is explained, recurring debates become standards.

## Q12. How do you use code review to grow junior engineers?

**Short answer:** Explain the why, link to standards and examples, ask guiding questions instead of dictating fixes, and praise good choices. Pair juniors as second reviewers on senior PRs so they learn by reading good code, and gradually give them primary review ownership of an area.

**How to think about it:** Review is one of the highest-leverage teaching tools a lead has.

**Example:** "What happens here if the request is aborted while the component is unmounting?" instead of "add an AbortController".

**Trade-offs and pitfalls:** Too many teaching comments on an urgent PR slow delivery; move deeper lessons to a pairing session.

**Remember:** Review to teach, not only to gate.

---

## References

- [Google Engineering Practices: Code Review](https://google.github.io/eng-practices/review/)
- [GitHub Docs: About code owners](https://docs.github.com/en/repositories/managing-your-repositorys-settings-and-features/customizing-your-repository/about-code-owners)
- [DORA research](https://dora.dev/)
