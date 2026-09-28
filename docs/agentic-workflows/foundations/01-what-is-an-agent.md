---
sidebar_position: 1
sidebar_label: "What Is an Agent"
description: "Defines an AI agent as an LLM plus tools, a loop, and state, and contrasts agents with deterministic workflows and chatbots."
---

# What Is an Agent

> **Reviewed:** 2026-09 · **Level:** Senior / Tech Lead · **Type:** Foundational

The word "agent" is used loosely in industry. For interviews, anchor on a precise, engineering-oriented definition and be explicit about where the terminology is still settling. The model-side ideas are covered in the [AI section](../../ai/index.md); this page focuses on the **system** around the model.

## Q1. An agent is an LLM, a set of tools, a control loop, and state

**Short answer:** An agent is a system where a language model decides, step by step, which action to take next — usually a tool call — observes the result, and repeats until a goal is met or a stop condition fires. The four parts are: the model (decision-making), tools (ability to act on the world), the loop (the harness that executes calls and feeds results back), and state (what the agent knows so far: messages, scratchpad, retrieved memory). The defining property is that the model controls the control flow, not just the text.

**How it works:**

- **Model:** stateless function from context to next output (text or a structured tool call).
- **Tools:** typed functions the harness exposes (search, read file, run query, open PR).
- **Loop / harness:** deterministic code that sends context to the model, executes requested tool calls, appends results, enforces budgets and permissions.
- **State:** conversation history, intermediate artifacts, task plan, long-term memory lookups.

**Example:**

```typescript
// Minimal agent loop. The model decides; the harness executes and enforces limits.
type ToolCall = { name: string; args: Record<string, unknown> };
type ModelTurn = { text?: string; toolCalls: ToolCall[] };

async function runAgent(goal: string, maxSteps = 10): Promise<string> {
  const messages: unknown[] = [{ role: "user", content: goal }];
  for (let step = 0; step < maxSteps; step++) {
    const turn: ModelTurn = await callModel(messages, toolSchemas);
    messages.push({ role: "assistant", ...turn });
    if (turn.toolCalls.length === 0) return turn.text ?? ""; // model says it is done
    for (const call of turn.toolCalls) {
      const result = await executeTool(call); // permission checks live here, not in the prompt
      messages.push({ role: "tool", name: call.name, content: result });
    }
  }
  throw new Error("Step budget exhausted"); // explicit stop condition
}
```

**Trade-offs and pitfalls:**

- Calling a single prompt with retrieval an "agent" inflates expectations; be precise in design reviews.
- The harness is where reliability lives. Teams that treat the model as the whole system skip budgets, permissions, and tracing.
- State grows every step; without management, cost and latency grow and quality degrades.

**Remember:** Agent = model chooses the next action in a loop. The harness, not the model, owns safety and limits.

## Q2. Agent vs deterministic workflow vs chatbot

**Short answer:** A chatbot answers in turns and does not act on external systems (or only in trivial ways). A deterministic workflow uses LLM calls as steps inside code paths you wrote — the control flow is fixed. An agent lets the model choose the control flow dynamically. Anthropic's "Building effective agents" guidance draws this workflow-vs-agent line, and it is a useful interview framing: prefer workflows when the steps are knowable in advance.

**How it works:**

| Property | Chatbot | LLM workflow | Agent |
|---|---|---|---|
| Who decides next step | User | Your code | Model (within harness limits) |
| Acts on systems | Rarely | Yes, at fixed points | Yes, dynamically |
| Predictability | High | High | Lower |
| Debuggability | Easy | Easy | Needs tracing |
| Best for | Q&A, drafting | Known multi-step processes | Open-ended tasks with unknown step count |

**Example:** "Summarize every new support ticket and tag it" is a workflow: classify, then summarize, then write tags — fixed steps. "Investigate why checkout latency spiked" is agent-shaped: the number and order of queries to metrics, logs, and deploy history is not known up front.

**Trade-offs and pitfalls:**

- Many "agent" projects are better as workflows; they become cheaper, faster, and testable.
- Hybrid is normal: a deterministic outer workflow with a bounded agent inside one step.
- Labels differ by vendor; describe behavior (who owns control flow) rather than arguing names.

**Remember:** If you can draw the flowchart ahead of time, build a workflow. Reach for an agent when you cannot.

## Q3. Autonomy is a spectrum, not a switch

**Short answer:** Autonomy levels range from "model suggests, human does everything" to "model acts end-to-end without review." A practical ladder is: suggest only, act on read-only tools, act with approval for writes, act autonomously within a sandbox, act autonomously in production with post-hoc audit. Senior engineers pick the lowest level that delivers value and raise it only with evidence from evaluation and incident history.

**How it works:**

1. **L0 Suggest:** drafts text or plans; human executes.
2. **L1 Read-only:** agent queries systems (logs, metrics, code search) and reports.
3. **L2 Gated writes:** agent proposes writes; human approves each one.
4. **L3 Sandboxed autonomy:** full action within an isolated environment (branch, container, staging).
5. **L4 Production autonomy:** acts on live systems within policy; humans audit afterward.

This ladder is a teaching device, not an industry standard; different organizations define levels differently.

**Example:** A coding agent at L3 can edit files and run tests in a container on a branch, but merging (an L4 action) requires human review through the normal code review process.

**Trade-offs and pitfalls:**

- Autonomy should be scoped **per action**, not per agent. The same agent can be L4 for reading logs and L2 for restarting services.
- Raising autonomy without reversibility (rollback, undo, dry-run) is the main source of serious incidents.
- Approval fatigue at L2 can silently turn into rubber-stamping, which is effectively L4 without the controls.

**Remember:** Grant autonomy per action, proportional to reversibility and blast radius.

## Q4. When agents help and when they hurt

**Short answer:** Agents help when the task is open-ended, the value of a correct result is high, success is verifiable (tests pass, query returns expected shape), and mistakes are cheap to reverse. They hurt when latency budgets are tight, the process is already well defined, errors are expensive or irreversible, or success cannot be checked. The core mechanical risk is error compounding: every step has some chance of going wrong, and long chains multiply that risk.

**How it works:**

- **Cost:** each loop iteration re-sends growing context; token cost grows faster than linearly with step count unless context is managed.
- **Latency:** sequential model calls plus tool calls; multi-minute runs are common for non-trivial tasks.
- **Reliability:** if each step succeeds independently with probability p, an n-step chain succeeds with roughly p to the power n. Even high per-step accuracy decays over long chains. (Steps are not truly independent, but the intuition holds.)
- **Verification:** tasks with automatic checks (compilers, tests, schema validation) let the agent self-correct; tasks without them hide errors.

**Example:** Code migration across 200 files is a good fit: each file change is verifiable by compile and tests, reversible via git, and tedious for humans. Auto-approving refunds from customer emails is a poor fit: irreversible, adversarial input, and hard to verify.

**Trade-offs and pitfalls:**

- Demos use short, happy-path tasks; production traffic has long tails.
- "It works 80% of the time" is only acceptable if the 20% fails loudly and cheaply.
- Agents shift cost from engineering time to compute and review time; measure both.

<details>
<summary>Follow-up questions</summary>

- **How do you reduce error compounding?** Shorten chains, add verification between steps, checkpoint and resume, and break the task into independently verifiable subtasks.
- **What is a good first agent project for a team?** Read-only investigation or drafting tasks where a human already reviews the output, such as incident summaries or PR descriptions.

</details>

**Remember:** Good agent tasks are open-ended, verifiable, and reversible. Missing any one of those three calls for more human gates.

## Q5. Established principles vs emerging practice

**Short answer:** Most of what makes agents safe is not new: least privilege, idempotency, timeouts, retries with backoff, observability, audit logging, and human approval for irreversible actions are long-established distributed-systems and security principles. What is emerging is the model-specific layer: tool-description design, protocols like MCP, prompt-injection defenses, and agent evaluation methodology. In interviews, lead with the established principles and label the emerging parts honestly.

**How it works:**

- **Established:** treat the model like an untrusted, fallible client of your APIs. Everything you would do for a junior contractor with API credentials applies.
- **Emerging:** how to phrase tool descriptions, how much autonomy to grant, how to evaluate trajectories, standard protocols, and multi-agent coordination.
- **Speculative:** claims about fully autonomous engineering teams or agents that reliably run for days unattended.

**Example:** "We scoped the agent's database credential to read-only on replicas" is established practice. "We tuned the tool description so the model stops calling the wrong search tool" is emerging practice — valid, but expect it to change with each model release.

**Trade-offs and pitfalls:**

- Over-indexing on framework features ages quickly; principles do not.
- Vendor claims about reliability are rarely reproducible on your tasks; build your own evaluation.

**Remember:** Treat the model as an untrusted client. Classic engineering controls do most of the safety work.

## References

Reviewed 2026-09.

- [Anthropic — Building effective agents](https://www.anthropic.com/engineering/building-effective-agents)
- [ReAct: Synergizing Reasoning and Acting in Language Models (arXiv)](https://arxiv.org/abs/2210.03629)
- [OpenAI — Function calling guide](https://platform.openai.com/docs/guides/function-calling)
- [OWASP Top 10 for LLM Applications](https://owasp.org/www-project-top-10-for-large-language-model-applications/)
