---
sidebar_position: 2
sidebar_label: "Vector Search, Hybrid & Reranking"
description: "Vector databases, ANN indexes like HNSW, hybrid BM25 plus vector search, reranking and metadata filtering."
---

# Vector Search, Hybrid Search and Reranking

> **Reviewed:** 2026-09 · **Level:** Senior / Tech Lead · **Type:** Foundational

This page covers the "retrieve" and "rerank" stages: how similarity search scales, why pure vector search is not enough, and how to get precise results.

## Q1. Vector databases store embeddings and answer nearest-neighbour queries fast

**Short answer:** A vector store holds embeddings plus metadata and answers "find the k vectors most similar to this query vector". At scale, exact search over millions of vectors is too slow, so they use Approximate Nearest Neighbour (ANN) indexes that trade a little recall for large speed gains. Options range from dedicated vector databases to vector extensions in existing databases (for example, Postgres with a vector extension) and search engines with vector support.

**How it works:** Key capabilities to evaluate: ANN index types, metadata filtering, hybrid (keyword + vector) search, multi-tenancy, updates and deletes, backup, and operational maturity.

**Example:** A team with a few hundred thousand chunks and an existing Postgres stack used a vector extension there — one fewer system to operate, transactional consistency with metadata, and familiar backups. They planned to revisit only if latency or scale demanded it.

**Trade-offs and pitfalls:**

- Adding a new database has operational cost; start with what you run unless requirements say otherwise.
- Check how filtering interacts with ANN — some implementations filter after retrieval and return too few results.

**Remember:** Choose the store on filtering, hybrid support, scale and ops fit — not hype.

## Q2. HNSW is a graph-based ANN index that navigates from coarse to fine

**Short answer:** HNSW (Hierarchical Navigable Small World) builds a multi-layer graph: upper layers have few nodes with long-range links, lower layers have all nodes with local links. A search starts at the top, greedily moves toward the query, then descends layers to refine. It gives high recall at low latency, at the cost of memory and slower inserts.

**How it works:** Intuition: like finding a street by first navigating between cities on highways, then local roads. Tunable parameters control graph connectivity (more links = better recall, more memory) and search breadth at query time (wider = better recall, slower). Other families include inverted-file (IVF) indexes that cluster vectors and search only nearby clusters, often combined with quantization to reduce memory.

**Example:** Recall on the eval set was lower than expected; increasing the query-time search breadth parameter improved recall@10 with a modest latency increase — a knob to tune with measurement, not guesswork.

**Trade-offs and pitfalls:**

- HNSW indexes are memory-hungry; quantization reduces memory at some accuracy cost.
- Heavy delete/update workloads can degrade graph quality; plan periodic rebuilds.

**Remember:** HNSW = layered graph, highways then local roads. Tune recall vs latency vs memory.

## Q3. Hybrid search combines keyword (BM25) and vector search

**Short answer:** Vector search captures meaning but misses exact tokens like error codes, product names and IDs. BM25 keyword search nails exact terms but misses paraphrases. Hybrid search runs both and fuses results — commonly with Reciprocal Rank Fusion (RRF) or weighted scores — and is a strong default for production RAG.

**How it works:** BM25 scores documents by term frequency weighted by term rarity, normalized for length. RRF combines ranked lists by summing `1 / (k + rank)` for each document across lists, which avoids comparing incompatible score scales.

**Example:** Query: "ERR_4012 when exporting invoices". Vector search returns general export-troubleshooting pages; BM25 finds the one page mentioning `ERR_4012`. Hybrid puts that page first.

```python
def rrf(result_lists, k=60):
    scores = {}
    for results in result_lists:
        for rank, doc_id in enumerate(results, start=1):
            scores[doc_id] = scores.get(doc_id, 0) + 1 / (k + rank)
    return sorted(scores, key=scores.get, reverse=True)
```

**Trade-offs and pitfalls:** Two indexes to maintain and keep in sync; fusion weights need tuning on your eval set.

**Remember:** Keywords for exactness, vectors for meaning, fuse the rankings.

## Q4. Reranking improves precision by scoring query and document together

**Short answer:** First-stage retrieval (bi-encoder embeddings, BM25) is fast but coarse because query and document are encoded separately. A reranker — typically a cross-encoder or an LLM — reads the query and each candidate together and produces a more accurate relevance score. Retrieve broadly (for example top 50), rerank, then send only the best few to the LLM.

**How it works:** Cross-encoders are too slow to run on the whole corpus but fine on tens of candidates. This two-stage design is standard in search engineering.

**Example:** A legal-docs assistant retrieved 40 hybrid candidates, reranked them, and passed the top 5 to the generator. Answers improved because the generator saw fewer near-miss chunks, and token cost dropped.

**Trade-offs and pitfalls:**

- Reranking adds latency per request — budget for it, and cache for repeated queries.
- A reranker cannot recover documents the first stage never retrieved; measure first-stage recall separately.

**Remember:** Retrieve for recall, rerank for precision.

## Q5. Metadata filtering enforces scope, freshness and access control

**Short answer:** Filters on metadata (tenant, product, language, document type, ACL groups, date) restrict retrieval to the chunks a user is allowed and expected to see. Access control belongs in retrieval filters — never rely on the LLM to withhold content it was given.

**How it works:** Store ACL identifiers (for example allowed group IDs) with each chunk; at query time, filter by the authenticated user's groups. Pre-filtering (filter then search) guarantees scope; post-filtering (search then filter) can return too few results.

**Example:** In a multi-tenant SaaS, every chunk carries `tenant_id`. The retrieval service injects `tenant_id = current_user.tenant` server-side, so a prompt cannot override it.

**Trade-offs and pitfalls:**

- ACL changes must propagate to the index quickly; stale permissions are a data leak.
- Per-tenant indexes give stronger isolation but cost more to operate than shared indexes with filters.

**Remember:** Filters are for security and scope; enforce them server-side.

## References

Reviewed 2026-09.

- OpenAI platform documentation (embeddings and retrieval): https://platform.openai.com/docs
- Anthropic documentation (retrieval patterns): https://docs.anthropic.com/
- Previous: [RAG Pipeline and Chunking](./01-rag-pipeline-and-chunking.md) · Next: [Retrieval Evaluation, Grounding and Freshness](./03-evaluation-grounding-freshness.md)
