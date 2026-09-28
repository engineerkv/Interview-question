---
sidebar_position: 100
sidebar_label: Cheatsheet
description: "One-page revision of LLM fundamentals, RAG, evaluation and safety, AI app architecture and AI-assisted development."
---

# AI Engineering Cheatsheet

> **Reviewed:** 2026-09 · **Level:** Senior / Tech Lead · **Type:** Foundational (Emerging items marked)

## LLM fundamentals

| Concept | One-liner |
| --- | --- |
| Token | Sub-word unit; the unit of cost, limits and latency. Measure with the real tokenizer. |
| Context window | Everything in one request, including output. Stateless between calls. |
| Temperature | Sharpness of the next-token distribution. Low for correctness, higher for variety. |
| Top-p | Sample from the smallest set of tokens covering probability p. Tune one knob at a time. |
| Latency | Time-to-first-token + output tokens × per-token time. Shorter output = faster. |
| Embedding | Text → vector; similar meaning = nearby. Same model for queries and corpus. |
| Prompt vs RAG vs fine-tune | Instructions vs knowledge at request time vs behaviour in weights. |
| Hallucination | Plausible but unsupported output. Ground, validate, allow "I don't know", measure. |
| Reasoning models (Emerging) | Spend extra tokens thinking; better on hard multi-step tasks; slower and costlier. |
| Structured outputs | Schema for shape, code for truth. Check finish reason. |
| Tool calling | Model proposes a call; your code authorizes and executes. |

## RAG

```text
Ingest → Chunk → Embed → Index → (Rewrite) → Retrieve (hybrid + filters) → Rerank → Assemble → Generate with citations → Validate
```

- **Chunk** along document structure; carry title and heading path into each chunk.
- **Hybrid** = BM25 for exact terms + vectors for meaning, fused with RRF.
- **HNSW** = layered graph, highways then local roads; tune recall vs latency vs memory.
- **Rerank** = retrieve broadly for recall, cross-encoder for precision.
- **Filters** enforce tenant and ACL scope server-side — never rely on the model to withhold.
- **Metrics:** recall@k, precision@k, MRR for retrieval; faithfulness and correctness for generation.
- **Freshness:** incremental re-index, fast deletes, blue/green when changing embedding models.
- **Don't use RAG** for structured data or numbers (use tools/SQL), or when the whole doc fits in context.

## Evaluation and safety

- **Golden dataset:** versioned, tagged, includes past failures and adversarial cases.
- **LLM-as-judge:** specific rubric, binary scores, calibrate against humans; biases include length and position.
- **CI gates:** run evals on prompt/model/retrieval changes; per-category thresholds with tolerance.
- **Online:** outcomes (resolution, escalation, retries) + feedback; traces per request.
- **Guardrails:** validate input and output; deterministic where possible; measure over-refusal.
- **Prompt injection:** direct (user) and indirect (docs, tools). No complete fix — least privilege, confirmation, output handling, egress limits.
- **PII:** minimize, redact, know retention, delete everywhere (logs, caches, vector stores).
- **OWASP LLM Top 10:** threat-model agenda — injection, disclosure, supply chain, poisoning, output handling, excessive agency, prompt leakage, vector weaknesses, misinformation, unbounded consumption.
- **Human review** for high-risk outputs; track override rates to detect rubber-stamping.

## AI app architecture

API gateway → orchestration service → (guardrails, retrieval, tools, cache) → model gateway/router → providers; plus tracing, eval pipeline, prompt registry, and a **non-AI fallback**.

- Model gateway: routing, retries, fallbacks, quotas, cost tagging.
- Caching: exact response, prompt caching (stable prefix first), embeddings; never across tenants.
- Trace: prompt version, model, tokens, latency, cost, retrieved IDs, tool calls.

## AI-assisted development

**Principles:** human ownership · same quality bar · context is the product · small verifiable steps · protect data and systems · measure outcomes.

**Workflow:** questions + plan → review plan → small step + tests → run checks → read every line → PR with "what I verified" → human review.

**Tools (Emerging):** inline assistants · IDE agents · terminal agents · PR review bots · chat assistants · background agents. Choose by context access, action scope and autonomy.

**Context engineering:** repository instructions (AGENTS.md / rules / CLAUDE.md / copilot-instructions) · scoped rules · reusable skills · fresh sessions and plan files · stable prefix for caching · MCP servers as privileged integrations.

**Model routing:** fast model for autocomplete/classification; strong model for implementation; reasoning model for design and hard debugging. Cap tokens, iterations and budgets.

**Human-only decisions:** architecture, security, data handling, production changes, incidents, hiring and performance.

**AI code review checklist (short):** APIs exist · edge cases · real error handling · meaningful tests that fail when broken · authz matches neighbours · no secrets · no new deps unreviewed · no suppressions · no unrelated changes · author can explain every line.

**Security:** approved tools with enterprise data terms · no secrets in prompts or agent environments · sandbox and allowlist commands · restrict egress · licence/SCA scanning · treat repo content and tool results as untrusted.

**Metrics:** DORA (deployment frequency, lead time, change failure rate, time to restore) · cycle time · review time · PR size · escaped defects · developer surveys · SPACE dimensions. **Not** lines of code or "% written by AI".

**Pilot:** goals and criteria → baseline → pilot + comparison group → fixed duration → metrics + survey + examples → expand / adjust / stop.

**Rollout:** align → approve tools → guidelines + rules files → baseline → pilot → train → feedback → evaluate → expand → codify standards → monitor.

## Interview one-liners

- "RAG quality problems are usually retrieval problems — I measure recall@k before touching the prompt."
- "The model proposes; my code authorizes and executes."
- "Assume prompt injection sometimes succeeds, and limit what a hijacked model can do."
- "AI speeds up the loop; tests, types, CI and human review still decide what ships."
- "If you can't explain it, you can't own it."
- "I measure outcomes like cycle time and change failure rate, not how much code the AI wrote."

## Links

- [Overview](./index.md) · [LLM Fundamentals](./llm-fundamentals/01-tokens-context-sampling.md) · [RAG](./rag-and-retrieval/01-rag-pipeline-and-chunking.md) · [Evaluation and Safety](./evaluation-and-safety/01-evaluation-and-monitoring.md) · [Architecture](./ai-app-architecture.md) · [AI-Assisted Development](./ai-assisted-development/index.md) · [Agentic Workflows](../agentic-workflows/index.md)

## References

Reviewed 2026-09.

- OpenAI platform documentation: https://platform.openai.com/docs
- Anthropic documentation: https://docs.anthropic.com/
- Model Context Protocol: https://modelcontextprotocol.io/
- OWASP Top 10 for LLM Applications: https://owasp.org/www-project-top-10-for-large-language-model-applications/
- DORA: https://dora.dev/
- The SPACE of Developer Productivity: https://queue.acm.org/detail.cfm?id=3454124
