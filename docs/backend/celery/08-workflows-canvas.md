---
sidebar_label: "Workflows (Canvas)"
description: "Composing Celery tasks with chain, group and chord, and the pitfalls that make canvas workflows fragile."
---

# Workflows with Canvas (Q30-Q33)

> **Reviewed:** 2026-09 · **Level:** Senior · **Type:** Foundational

## Q30. A chain runs tasks in sequence, passing each result to the next

`chain(a.s(x), b.s(), c.s())` (or `a.s(x) | b.s() | c.s()`) runs `a`, then calls `b` with `a`'s return value as its first argument, then `c` with `b`'s. Each step is a separate message, so steps can run on different workers and queues.

**Example:**

```python
from celery import chain

workflow = chain(
    download_video.s(video_id),        # returns object key
    transcode.s(),                     # receives key
    generate_thumbnails.s(),
    notify_user.si(user_id),           # .si = immutable: ignore previous result
)
workflow.apply_async()
```

**Trade-offs and pitfalls:**

- If any step fails, later steps do not run; the chain has no built-in compensation.
- Use `.si()` when a step should not receive the previous result, or you get surprising argument errors.
- Pass keys between steps, not large data; results go through the broker and backend.

**Remember:** Chain = sequential pipeline, one message per step.

## Q31. A group runs tasks in parallel; a chord adds a callback when all finish

A group fans out: `group(resize.s(i) for i in ids)` publishes all at once. A chord is a group (the header) plus a callback (the body) that receives the list of all header results once every header task succeeds. Chords need a result backend because something must track completion.

**Example:**

```python
from celery import group, chord

# Fan-out only
group(resize.s(img_id) for img_id in image_ids).apply_async()

# Fan-out + fan-in (map-reduce)
chord(
    (score_chunk.s(chunk_id) for chunk_id in chunk_ids),
    merge_scores.s(report_id),     # called with [result1, result2, ...] as first arg
).apply_async()
```

**Trade-offs and pitfalls:**

- If one header task fails, the callback does not run (the chord errors). Decide whether header tasks should catch errors and return a status instead.
- Very large groups (tens of thousands of tasks) create many messages and backend entries at once; batch with `chunks` or a two-level fan-out.
- Results of all header tasks are held for the callback; keep them small.

**Remember:** Group = fan-out; chord = fan-out + fan-in, and it needs a backend.

## Q32. Never block on another task's result inside a task

Calling `result.get()` inside a task waits for a task that needs a free worker slot. Under load, all slots can be waiting on each other: deadlock. Celery raises an error by default if you try (`disable_sync_subtasks`). The fix is to express the dependency as a chain or chord, so the orchestration happens via messages.

**Example:**

```python
# Bad
@app.task
def parent(x):
    return child.delay(x).get()    # blocks a worker slot waiting for another slot

# Good
(child.s(x) | finish.s()).apply_async()
```

**Trade-offs and pitfalls:**

- Chords implemented via backend polling (some backends) add load; Redis backends handle chord counting efficiently.
- Workflows defined in code are hard to observe; log a workflow id and pass it through every step.

**Remember:** Compose with canvas; do not `.get()` inside tasks.

## Q33. Canvas is fine for short workflows; long-running business processes need durable orchestration

Canvas has no persisted workflow state beyond individual task messages and results. If a multi-day onboarding flow or a payment saga depends on it, you cannot easily answer "where is this order in the process?", resume after a code change, or run compensations. For those, store the process state in your database (a state machine updated by each task) or use a workflow engine like Temporal.

**How it works:**

| Need | Canvas | DB state machine + tasks | Workflow engine |
|---|---|---|---|
| Short pipeline (seconds to minutes) | Good | Overkill | Overkill |
| Visibility of each instance | Weak | Good | Good |
| Long timers (days) | Poor | Good with a poller | Native |
| Compensation / sagas | Manual | Manual but explicit | First-class patterns |

**Trade-offs and pitfalls:**

- Result expiry can break chords whose headers take longer than `result_expires`.
- Changing a chain's signature while messages are in flight breaks in-flight workflows; version task names or arguments.

**Remember:** Canvas for pipelines; a state machine or workflow engine for business processes.

## References

- [Celery documentation: canvas](https://docs.celeryq.dev/en/stable/)
- [System design case studies (this site)](../../case-studies/index.md)
