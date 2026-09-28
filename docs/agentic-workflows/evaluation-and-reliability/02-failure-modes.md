---
sidebar_position: 2
sidebar_label: "Failure Modes Catalog"
description: "Catalogs common agent failure modes such as loops, tool hallucination, wrong tool, partial completion, and silent failure, with detection and mitigation."
---

# Agent Failure Modes Catalog

> **Reviewed:** 2026-09 · **Level:** Senior / Tech Lead · **Type:** Foundational

These failure modes are observed widely across agent systems. The mitigations are mostly established engineering techniques; the exact frequency of each failure depends heavily on model, task, and tool design, so measure your own.

## Q1. Know the core failure modes and how to detect each

**Short answer:** The recurring failures are: loops (repeating the same action), tool hallucination (calling tools or arguments that do not exist, or inventing tool results), wrong tool selection, partial completion reported as success, silent failure (errors swallowed and not surfaced), goal drift (solving a different problem), and unsafe actions. Each needs a detection signal in traces and a mitigation in the harness.

**How it works:**

| Failure mode | Detection signal | Mitigation |
|---|---|---|
| Loops | Same call and args repeated; no new info over N steps | Repeat detector, step budget, force re-plan |
| Tool hallucination | Unknown tool name; schema validation failure; claims results not in trace | Strict schemas, reject unknown tools, cross-check claims against trace |
| Wrong tool | Trajectory grader; tool not in expected set for task type | Better names and descriptions, fewer overlapping tools, phase-based tool filtering |
| Partial completion | Plan items open at finish; verifier fails | Completion checklist, verifier step, explicit status codes |
| Silent failure | Errors in tool spans but success status; empty results after denial | Structured errors, fail loudly, status must reflect worst step |
| Goal drift | Final output does not address original task | Pin original goal, final self-check against task |
| Unsafe action | Policy violation in trace | Least privilege, approvals, deny-by-default policy |

**Example:** A migration agent reports "all files migrated" but its own progress file shows three failures. A deterministic final check — compile plus a grep for the old API — catches it and flips the status to `partial`.

**Trade-offs and pitfalls:**

- Detection only in offline evaluation misses production drift; run lightweight checks online too.
- Adding many checks increases latency; prioritize by impact.

**Remember:** Every failure mode needs a trace signal and a harness mitigation, not just a prompt instruction.

## Q2. Silent failure and false success are the most dangerous

**Short answer:** A loud failure costs a retry; a false success costs trust and sometimes an incident, because downstream people or systems act on it. Agents are prone to false success because models tend to produce confident final summaries even when steps failed. Make success a verified property: the harness computes status from checks and step outcomes, not from the model's final message.

**How it works:**

- Status is derived: `success` only if verifier passes and no step ended in unresolved error.
- The final report lists what was done, what failed, and what was skipped, with links to evidence.
- Claims in summaries are checked against trace facts where possible (for example, "tests passed" requires a passing test tool result in the trace).

**Example:**

```typescript
// Harness computes status; the model's summary is attached but not trusted for status.
function computeStatus(trace: Trace, verifier: VerifierResult): RunStatus {
  if (trace.steps.some((s) => s.error && !s.recovered)) return "failed_step";
  if (!verifier.passed) return "unverified";
  if (trace.plan.some((p) => p.state !== "done")) return "partial";
  return "success";
}
```

**Trade-offs and pitfalls:**

- Some tasks lack a cheap verifier; mark them "unverified" rather than "success" and route to review.
- Users learn to ignore statuses if they are noisy; keep them accurate and few.

**Remember:** The harness decides success from evidence. The model's confidence is not a status.

## Q3. Error compounding and recovery design

**Short answer:** Early mistakes (misreading a log, picking the wrong service) propagate: later steps build on them and the final answer can be confidently wrong. Reduce compounding by verifying intermediate conclusions, keeping chains short, checkpointing so you can back up, and encouraging the agent to state and test hypotheses rather than commit to the first one.

**How it works:**

- **Intermediate verification:** after key steps, check facts with a second, independent query.
- **Hypothesis tracking:** keep a list of hypotheses with supporting and contradicting evidence.
- **Backtracking:** allow re-planning from a checkpoint when evidence contradicts the plan.
- **Decomposition:** independent subtasks limit how far an error spreads.

**Example:** An investigation agent concludes "database is the bottleneck" from one slow-query log. A required verification step checks database CPU and connection pool metrics in the same window; they are normal, so the hypothesis is downgraded and the agent looks at the upstream cache instead.

**Trade-offs and pitfalls:**

- Verification steps add cost; apply them at decision points, not everywhere.
- Models can rationalize contradicting evidence; structured hypothesis records help make contradictions explicit.

**Remember:** Verify at decision points, track hypotheses, and make backtracking cheap.

## References

Reviewed 2026-09.

- [Anthropic — Building effective agents](https://www.anthropic.com/engineering/building-effective-agents)
- [ReAct: Synergizing Reasoning and Acting in Language Models (arXiv)](https://arxiv.org/abs/2210.03629)
- [OWASP Top 10 for LLM Applications](https://owasp.org/www-project-top-10-for-large-language-model-applications/)
