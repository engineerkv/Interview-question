---
sidebar_position: 1
sidebar_label: "Tokens, Context & Sampling"
description: "How LLMs see text as tokens, what a context window really is, and how temperature and top-p shape output."
---

# Tokens, Context Windows and Sampling

> **Reviewed:** 2026-09 · **Level:** Senior / Tech Lead · **Type:** Foundational

These are the mechanics behind almost every practical LLM decision: cost, latency, truncation bugs, and "why did it answer differently this time?". Interviewers use them to check whether you understand the model as a system component rather than a magic box.

## Q1. LLMs operate on tokens, not characters or words

**Short answer:** A model never sees raw text. A tokenizer splits text into sub-word units called tokens, maps each to an integer ID, and the model predicts the next token ID one step at a time. Pricing, context limits and latency are all measured in tokens, so understanding tokenization explains why some inputs are unexpectedly expensive or truncated.

**How it works:** Most modern models use a sub-word scheme such as Byte-Pair Encoding (BPE) or a variant. Common words become a single token; rare words, code identifiers, non-English text and long numbers get split into several. As a rough intuition for English prose, a token is a few characters, but this varies by tokenizer and language — always measure with the provider's tokenizer rather than guessing.

**Example:** A team estimating cost for a multilingual support bot assumed "1 token per word". Their Japanese and Hindi tickets used noticeably more tokens per message than English, and JSON-heavy tool payloads added overhead from braces, quotes and keys. They fixed their budget by counting tokens on a real sample of production traffic.

```python
# Illustrative: count tokens with the provider's tokenizer before sending
tokens = tokenizer.encode(prompt)
if len(tokens) > MAX_INPUT_TOKENS:
    prompt = truncate_or_summarize(prompt, MAX_INPUT_TOKENS)
```

**Trade-offs and pitfalls:**

- Different model families use different tokenizers; a token count from one is not valid for another.
- Tokenization explains odd weaknesses: character-level tasks (counting letters, reversing strings) are hard because the model sees chunks, not characters.
- Whitespace, formatting and verbose JSON consume tokens; compact formats save money.

**Remember:** Tokens are the unit of cost, limits and latency. Measure them with the real tokenizer.

## Q2. The context window is the model's entire working memory for one request

**Short answer:** The context window is the maximum number of tokens the model can attend to in a single call — system prompt, conversation history, retrieved documents, tool definitions *and* the generated output combined. The model has no memory between calls; anything it "remembers" is something your application re-sent.

**How it works:** Each request is stateless. Chat applications simulate memory by resending prior turns. When history grows past the limit you must truncate, summarize, or retrieve selectively. Output tokens usually share the budget, so a huge input can leave little room for the answer.

**Example:** A code-review bot that pasted entire diffs plus full files hit the limit on large PRs and silently lost the end of the diff. The fix was to send only changed hunks with surrounding context, plus a summary of unchanged files, and to fail loudly when the budget was exceeded.

**Trade-offs and pitfalls:**

- Bigger is not automatically better: long contexts cost more, increase latency, and models can attend less reliably to information buried in the middle of very long inputs ("lost in the middle" effect has been reported in research; degree varies by model).
- Silent truncation is a classic production bug — log token counts and alert on overflow.
- Putting critical instructions at the start (system prompt) and restating key constraints near the end can help.

<details>
<summary>Follow-up questions</summary>

- *How would you handle a chat that runs for hours?* Rolling summary of older turns, keep recent turns verbatim, store facts in a retrievable memory store.
- *Does a 1M-token window remove the need for RAG?* No — cost, latency, freshness, access control and citation still favour retrieval for most use cases.

</details>

**Remember:** Context = everything in one request, including the answer. Stateless by default.

## Q3. Temperature controls randomness when choosing the next token

**Short answer:** At each step the model produces a probability distribution over possible next tokens. Temperature rescales that distribution: low temperature sharpens it (more deterministic, picks the likely tokens), high temperature flattens it (more diverse, more risk of nonsense). For extraction, classification and code, use low temperature; for brainstorming, moderate.

**How it works:** Logits are divided by the temperature before softmax. Temperature near 0 approaches greedy decoding (always the top token). Values above 1 give rare tokens more chance.

**Example:**

| Task | Typical setting | Why |
| --- | --- | --- |
| JSON extraction, classification | Low (0 to 0.2) | Consistency and parseability |
| Code generation | Low to moderate | Correctness over creativity |
| Marketing copy variants | Moderate to higher | Diversity is the goal |

**Trade-offs and pitfalls:**

- Temperature 0 is *not* a guarantee of identical outputs; batching, hardware and provider-side changes can still cause variation.
- Some reasoning models restrict or ignore sampling parameters — check the provider's docs.
- High temperature does not make the model "smarter" or more creative in a useful sense; it makes it less predictable.

**Remember:** Temperature = sharpness of the next-token distribution. Low for correctness, higher for variety.

## Q4. Top-p (nucleus sampling) limits choices to the most probable tokens

**Short answer:** Top-p keeps the smallest set of tokens whose cumulative probability reaches p (for example 0.9) and samples only from that set. It cuts off the long tail of unlikely tokens while keeping flexibility when the model is genuinely uncertain. Top-k is a simpler cousin that keeps a fixed number of candidates.

**How it works:** When the model is confident, the nucleus may contain one or two tokens; when uncertain, it contains many. This adapts better than a fixed top-k. Providers generally recommend tuning temperature *or* top-p, not both aggressively.

**Example:** A summarization service used temperature 0.7 and occasionally produced odd word choices. Setting top-p to 0.9 trimmed the tail and removed most bizarre tokens without making summaries robotic.

**Trade-offs and pitfalls:**

- Tuning both parameters at once makes behaviour hard to reason about.
- Sampling settings are a weak lever compared to better prompts, examples and structured output.

**Remember:** Top-p trims the unlikely tail; tune one knob at a time.

## Q5. Output generation is sequential, which drives latency

**Short answer:** Input tokens are processed in parallel (the "prefill"), but output tokens are generated one at a time (the "decode"). So latency is roughly time-to-first-token plus output length times per-token speed. Long answers are slow; long prompts mainly increase time-to-first-token and cost.

**How it works:** Every output token requires a forward pass conditioned on everything before it. Streaming shows tokens as they are produced, improving perceived latency even though total time is unchanged.

**Example:** A UI that waited for a full 800-token answer felt sluggish. Streaming the response and asking for a concise answer first (with "show more" expanding details) made it feel responsive.

**Trade-offs and pitfalls:**

- Streaming complicates validation: you cannot validate JSON until it is complete — buffer structured outputs server-side.
- Reasoning models generate hidden "thinking" tokens that add latency and cost even if you never see them.

**Remember:** Latency ≈ time-to-first-token + output tokens × per-token time. Shorter outputs are the biggest latency win.

## Q6. Stop sequences, max tokens and system prompts are basic control levers

**Short answer:** `max_tokens` caps output length (and cost), stop sequences end generation when a marker appears, and the system prompt sets persistent role, rules and format. Together they are the first line of control before you reach for fine-tuning.

**How it works:** Hitting `max_tokens` truncates mid-sentence or mid-JSON — the API usually reports a finish reason such as "length" that you should check. The system prompt has higher priority in most chat models' instruction hierarchy, but it is not a security boundary.

**Example:**

```text
System: You are a support classifier. Respond with exactly one label from:
billing, bug, feature_request, account, other. No explanation.
User: I was charged twice this month.
```

**Trade-offs and pitfalls:**

- Always check the finish reason; treat "length" as a failure for structured outputs.
- Never rely on the system prompt alone to protect secrets — anything in the context can potentially be extracted.

**Remember:** Cap output, check finish reason, and treat the system prompt as guidance, not security.

## References

Reviewed 2026-09.

- OpenAI platform documentation (tokens, sampling parameters): https://platform.openai.com/docs
- Anthropic documentation (context windows, system prompts): https://docs.anthropic.com/
- Next: [Embeddings, Adaptation and Hallucinations](./02-embeddings-adaptation-hallucinations.md)
