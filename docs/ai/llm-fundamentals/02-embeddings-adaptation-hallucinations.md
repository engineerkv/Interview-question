---
sidebar_position: 2
sidebar_label: "Embeddings, Adaptation & Hallucinations"
description: "Embeddings, choosing between prompting, RAG and fine-tuning, and why LLMs hallucinate."
---

# Embeddings, Adaptation and Hallucinations

> **Reviewed:** 2026-09 · **Level:** Senior / Tech Lead · **Type:** Foundational

This page covers how models represent meaning, how you adapt a general model to your domain, and the failure mode every interviewer will ask about: hallucination.

## Q1. Embeddings turn text into vectors where similar meaning means nearby points

**Short answer:** An embedding model maps a piece of text to a fixed-length vector of numbers. Texts with similar meaning land close together, measured by cosine similarity or dot product. Embeddings power semantic search, RAG retrieval, clustering, deduplication and recommendation — they are a representation, not a generator.

**How it works:** The embedding model is trained so that related pairs (a question and its answer, paraphrases) end up close in vector space. You embed your documents once, store the vectors, then embed each query and find the nearest neighbours.

**Example:** "How do I reset my password?" and "I forgot my login credentials" share few keywords but embed close together, so a semantic search finds the right help article where keyword search might miss it.

**Trade-offs and pitfalls:**

- Query and documents must be embedded with the **same model and version**; changing models requires re-embedding the whole corpus.
- Embeddings are weak at exact matches (error codes, SKUs, names) — combine with keyword search (see [hybrid search](../rag-and-retrieval/02-vector-search-hybrid-reranking.md)).
- Embeddings can leak information about the source text; treat them as sensitive as the text itself.

**Remember:** Embeddings = meaning as coordinates. Same model for query and corpus.

## Q2. Prompting, RAG and fine-tuning solve different problems

**Short answer:** Prompting changes *instructions*, RAG changes *knowledge available at request time*, and fine-tuning changes *behaviour learned in the weights*. Start with prompting, add RAG when the model needs your private or fresh data, and consider fine-tuning only when you need consistent style, format or a narrow skill that prompting cannot deliver reliably — or to make a smaller model match a larger one on a narrow task.

**How it works:**

| Approach | Changes | Good for | Weak for |
| --- | --- | --- | --- |
| Prompting (incl. few-shot) | Instructions and examples | Fast iteration, most tasks | Large knowledge, very long rules |
| RAG | Retrieved context per request | Private, changing, citable knowledge | Teaching new skills or style |
| Fine-tuning | Model weights | Consistent format/tone, narrow tasks, cost reduction via smaller model | Injecting facts that change often |

**Example:** An internal policy assistant needs to answer from HR documents that change monthly and must cite sources — that is RAG. A ticket classifier that must emit a company-specific taxonomy at high volume and low cost may justify fine-tuning a small model after prompting a large one produced the training labels.

**Trade-offs and pitfalls:**

- Fine-tuning to "teach facts" is a common mistake: facts go stale, cannot be cited, and cannot respect per-user access control.
- Fine-tuning needs a quality dataset, an eval set, and a retraining process — it is an ongoing commitment.
- Combining is normal: a fine-tuned model can still use RAG.

**Remember:** Prompt first, RAG for knowledge, fine-tune for behaviour. Evaluate before and after each step.

## Q3. Hallucinations happen because the model predicts plausible text, not verified truth

**Short answer:** A hallucination is fluent output that is false or unsupported. It happens because the model is trained to produce likely continuations, not to check facts; when it lacks the information it still produces something that *sounds* right. It is a property of the technique, so you manage it with grounding, constraints, verification and UX — you do not eliminate it.

**How it works:** Contributing causes include: missing or outdated knowledge, ambiguous questions, prompts that pressure the model to always answer, retrieval returning irrelevant chunks, long contexts where relevant facts are missed, and training that rewarded confident answers.

**Example mitigations:**

- Ground answers in retrieved sources and require citations; reject answers whose citations do not support the claim.
- Explicitly allow "I don't know" and test that the model uses it.
- Use structured outputs and validate against real data (does this API method, SKU, or customer ID exist?).
- For code: compile, type-check and run tests — a hallucinated API fails fast.

**Trade-offs and pitfalls:**

- Stronger models hallucinate less on average but still do, and confidently.
- Low temperature reduces randomness, not hallucination caused by missing knowledge.
- Over-constraining ("only answer if 100% sure") can make the product refuse too often — measure both error and refusal rates.

<details>
<summary>Follow-up questions</summary>

- *How do you measure hallucination rate?* A golden dataset with known answers plus a faithfulness check (is every claim supported by the provided context?), using human labels to calibrate any automated judge.
- *Who is accountable when a hallucination reaches a customer?* The product team — which is why high-risk outputs need human review or hard validation.

</details>

**Remember:** Hallucination is expected behaviour of a next-token predictor. Ground, validate, allow abstention, measure.

## Q4. Few-shot examples are often the cheapest quality improvement

**Short answer:** Including a handful of input/output examples in the prompt shows the model the exact format, tone and edge-case handling you want. It is usually faster and cheaper than fine-tuning and should be tried before it.

**How it works:** Models are good at pattern continuation. Examples disambiguate instructions that are hard to express in words ("be concise" means different things to different people).

**Example:**

```text
Classify the severity of each incident report.

Report: "Checkout page returns 500 for all users"
Severity: SEV1

Report: "Typo on the pricing page footer"
Severity: SEV4

Report: "{{new_report}}"
Severity:
```

**Trade-offs and pitfalls:**

- Examples cost tokens on every call (prompt caching can help — see [model routing and cost](../ai-assisted-development/04-model-routing-and-cost.md)).
- The model may over-copy examples; vary them and include edge cases.
- Keep examples in version control and in your eval set so changes are tested.

**Remember:** Show, don't just tell — but pay for it in tokens.

## Q5. Knowledge cutoff and staleness are separate from hallucination

**Short answer:** A model's training data stops at some date, so it may not know recent library versions, APIs or events. It will often answer confidently from older knowledge. For anything time-sensitive, supply current information through retrieval or tools rather than trusting the model's memory.

**How it works:** The model has no clock and no awareness of what changed after training unless you tell it. Passing the current date and relevant up-to-date docs in context is a simple fix.

**Example:** An assistant generated code using a deprecated framework API because that was common in its training data. The team added the current framework version and a link-retrieved docs snippet to the context, and CI caught the remaining cases.

**Trade-offs and pitfalls:**

- "The model knows library X" is not a reason to skip docs retrieval for version-sensitive work.
- Pinning model versions gives reproducibility but freezes knowledge.

**Remember:** Models are frozen in time. Supply fresh facts; don't assume them.

## Q6. Reasoning models trade latency and cost for better multi-step problem solving

> **Type:** Emerging — capabilities and pricing change frequently.

**Short answer:** "Reasoning" models are trained or configured to spend extra tokens thinking through a problem before answering. They tend to do better on multi-step logic, math, planning and complex debugging, but are slower and more expensive per request. Use them where correctness on hard problems matters, not for simple classification or autocomplete.

**How it works:** The model generates intermediate reasoning (sometimes hidden, sometimes summarized) and may let you set a reasoning effort or thinking budget. Those tokens are typically billed.

**Example:** A team routes "explain this production stack trace across three services" to a reasoning model and "rename this variable" or "classify this ticket" to a small fast model.

**Trade-offs and pitfalls:**

- Reasoning does not fix missing context — a model reasoning over the wrong files still reaches the wrong conclusion.
- Hidden reasoning tokens make cost less predictable; set budgets and monitor.

**Remember:** Pay for reasoning where the problem is genuinely hard.

## References

Reviewed 2026-09.

- OpenAI platform documentation (embeddings, fine-tuning, reasoning models): https://platform.openai.com/docs
- Anthropic documentation (prompt engineering, reducing hallucinations): https://docs.anthropic.com/
- Previous: [Tokens, Context and Sampling](./01-tokens-context-sampling.md) · Next: [Models, Cost and Structured Outputs](./03-models-cost-structured-outputs.md)
