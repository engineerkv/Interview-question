---
sidebar_position: 2
sidebar_label: "Tools Landscape"
description: "A vendor-neutral map of AI developer tool categories, their capabilities, and how to evaluate them."
---

# AI Developer Tools Landscape

> **Reviewed:** 2026-09 · **Level:** Senior / Tech Lead · **Type:** Emerging — this landscape changes quickly; products move between categories and add features every few months.

This page describes **capability categories**, not products. Named tools are examples of a category at the time of review, not endorsements or feature claims. Before adopting anything, check current documentation, data-handling terms and your organization's policies.

## Categories at a glance

| Category | Typical examples (at review time) | Where it runs | Typical capabilities | Best for |
| --- | --- | --- | --- | --- |
| Inline assistants | GitHub Copilot code completion, IDE autocomplete features | In the editor, as you type | Next-line / multi-line completions, small inline edits | Boilerplate, idiomatic snippets, staying in flow |
| IDE agents | Cursor agent mode, agent modes in other IDEs and extensions | In the editor with workspace access | Multi-file edits, codebase search, running terminal commands with approval, applying diffs | Features, refactors, debugging within a repo |
| Terminal / CLI agents | Claude Code and similar CLI agents | In a shell, in the repo | Reading and editing files, running commands and tests, git operations, scriptable/headless use | Larger tasks, automation, CI use, terminal-centric developers |
| PR review bots | AI review features in code hosts and third-party review apps | On pull requests | PR summaries, inline review comments, finding likely bugs, policy checks | First-pass review, consistency, catching obvious issues |
| Chat assistants | General-purpose chat apps, IDE chat panels | Browser, desktop or IDE panel | Q&A, explanations, design discussion, drafting docs | Learning, design exploration, writing |
| Background / cloud agents (Emerging) | Hosted agents that work on a branch asynchronously | Provider or company cloud sandbox | Take a ticket, produce a branch or PR, run tests in a sandbox | Well-scoped tasks, parallel work, maintenance chores |

Categories overlap: many products now offer completion, chat, agent mode and review in one. Evaluate the capability you need, not the brand.

## Q1. What are the main categories of AI coding tools and when would you use each?

**Short answer:** Inline assistants complete code as you type — low friction, small scope. IDE agents make multi-file changes in your workspace with your review. Terminal agents do the same from the command line and can be scripted into automation. PR review bots give a first-pass review on pull requests. Chat assistants help with explanation, design and learning. I pick by task size and how much autonomy is appropriate: completion for flow, agents for scoped multi-file tasks, review bots as an extra reviewer, chat for thinking.

**How it works:** The key differences are *context access* (current file vs whole repo vs external systems), *action scope* (suggest vs edit vs run commands), and *autonomy* (every step approved vs runs to completion).

**Example:** A developer uses inline completion while writing a handler, asks an IDE agent to update all call sites after changing a function signature, runs a terminal agent to fix a batch of lint warnings across packages, and gets a review bot's summary on the PR before a colleague reviews it.

**Trade-offs and pitfalls:**

- More autonomy means more verification burden and more security surface (command execution, network access).
- Tool sprawl: multiple overlapping tools with different data terms complicate governance.

**Remember:** Choose by context access, action scope and autonomy.

## Q2. How do you evaluate an AI coding tool for your team?

**Short answer:** Evaluate on your own codebase and tasks during a time-boxed pilot, against criteria agreed in advance: output quality on representative tasks, fit with your languages and workflows, context handling (large repo, monorepo), controls (approval of commands, sandboxing), data handling and retention terms, admin features (SSO, policy, audit logs), cost model, and developer experience. Vendor demos and public benchmarks are not a substitute.

**How it works:** Evaluation criteria:

| Criterion | Questions to ask |
| --- | --- |
| Quality on our tasks | Does it handle our languages, frameworks and repo size? |
| Context | Can it use repository rules/instruction files? How does it retrieve relevant files? |
| Safety controls | Can command execution require approval? Is there sandboxing? Can we restrict network access? |
| Data handling | Is code retained? Used for training? Where is it processed? Enterprise controls? |
| Admin and compliance | SSO, seat management, usage policies, audit logs |
| Integration | IDEs we use, CI, code host, MCP or other tool integrations |
| Cost | Seat vs usage pricing, predictability, overage controls |
| Exit | How hard is it to switch? Are our rules/prompts portable? |

**Example:** A team compares two tools over the same four weeks: each pilot group does the same categories of tickets; the team collects cycle-time data, review comments per PR, and a short developer survey, and security reviews both vendors' data terms.

**Trade-offs and pitfalls:** Novelty effects inflate early satisfaction; run pilots long enough to see steady-state behaviour.

**Remember:** Pilot on your code, with pre-agreed criteria, including security and data terms.

## Q3. What are the risks specific to agents that can run commands?

**Short answer:** Agents that execute shell commands can delete files, modify git history, install malicious dependencies, leak secrets through network calls, or act on injected instructions found in repository content. Mitigate with approval for commands (or allowlists), sandboxed environments or containers, restricted network egress, no production credentials in the environment, and review of all changes before merge.

**How it works:** The risk is excessive agency combined with prompt injection (see [security, privacy and licensing](./06-security-privacy-licensing.md)).

**Example:** A team allows agents to run tests and linters automatically but requires approval for any command that installs packages, touches git remotes, or uses the network, and runs background agents only in ephemeral containers without cloud credentials.

**Trade-offs and pitfalls:** Approving every command causes fatigue and rubber-stamping; use allowlists for safe, frequent commands.

**Remember:** Sandbox, allowlist, no prod credentials, human review before merge.

## Q4. Should a team standardize on one tool?

**Short answer:** Standardize on a small approved set, not necessarily one. Standardization simplifies security review, data governance, training and shared rules files. Allow a controlled process for evaluating new tools because the landscape changes quickly. Keep team conventions (rules, prompt templates, review standards) tool-agnostic where possible so switching is cheap.

**How it works:** An approved-tools list with data classification guidance ("tool X approved for internal code; not for customer data"), plus an evaluation path for new tools.

**Example:** Engineering approves one IDE agent and one PR review bot with enterprise data terms, keeps an `AGENTS.md`-style instructions file that multiple tools can read, and reviews the list twice a year.

**Trade-offs and pitfalls:** Over-restrictive policies push engineers to unapproved personal tools — a worse security outcome.

**Remember:** Small approved set, portable conventions, a path to evaluate new tools.

## Practical checklist

- [ ] Categories needed identified (completion, agent, review, chat)
- [ ] Data handling and retention terms reviewed by security/legal
- [ ] Command execution controls and sandboxing understood
- [ ] Pilot on real tasks with pre-agreed criteria and baseline
- [ ] Approved-tools list and data classification guidance published
- [ ] Conventions kept portable across tools

## References

Reviewed 2026-09.

- GitHub Copilot documentation: https://docs.github.com/en/copilot
- Cursor documentation: https://docs.cursor.com/
- Anthropic documentation (including Claude Code): https://docs.anthropic.com/
- OpenAI platform documentation: https://platform.openai.com/docs
- Related: [Automated review process](../../leadership/code-reviews/automated-review-process.md) · [Agentic Workflows](../../agentic-workflows/index.md)
