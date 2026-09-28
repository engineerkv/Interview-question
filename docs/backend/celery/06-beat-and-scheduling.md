---
sidebar_label: "Beat and Scheduling"
description: "How Celery Beat schedules periodic tasks, why exactly one Beat must run, and alternatives for scheduling."
---

# Beat and Scheduling (Q22-Q24)

> **Reviewed:** 2026-09 · **Level:** Senior · **Type:** Foundational

## Q22. Celery Beat is a scheduler that publishes tasks on a timetable; it does not run them

Beat is a separate process that reads a schedule (intervals or crontab expressions) and publishes task messages when they are due. Workers execute them like any other task. Keeping Beat separate from workers means scheduling is independent of how many workers you run.

**Example:**

```python
from celery.schedules import crontab

app.conf.beat_schedule = {
    "expire-sessions-every-10-min": {
        "task": "accounts.tasks.expire_sessions",
        "schedule": 600.0,
    },
    "nightly-report": {
        "task": "reports.tasks.nightly",
        "schedule": crontab(hour=2, minute=0),
        "options": {"queue": "heavy", "expires": 3600},
    },
}
app.conf.timezone = "UTC"
```

```bash
celery -A proj beat --loglevel=info
# Django: store schedules in the DB, editable via admin
celery -A proj beat --scheduler django_celery_beat.schedulers:DatabaseScheduler
```

**Trade-offs and pitfalls:**

- Beat publishes on time; execution depends on worker availability. Add `expires` so a backlog does not run 20 stale copies.
- If a run takes longer than the interval, runs overlap. Guard with a lock or make the task idempotent.
- `celery worker -B` embeds Beat in a worker; fine for development, dangerous when you scale workers to more than one.

**Remember:** Beat only publishes; workers execute.

## Q23. Running more than one Beat duplicates every scheduled task

Standard Beat has no leader election. If you run two replicas (for "high availability") or scale a worker Deployment that uses `-B`, each instance publishes the schedule, and nightly jobs run twice. The standard fix is exactly one Beat replica, deployed with a strategy that never overlaps old and new pods, and scheduled tasks that are idempotent anyway.

**How it works:**

- Kubernetes: a Deployment with `replicas: 1` and `strategy: Recreate`, so a rollout does not briefly run two.
- Beat state (last run times) lives in a local file (`celerybeat-schedule`) or the DB scheduler; losing it may cause a catch-up run or a skip depending on the schedule.

**Trade-offs and pitfalls:**

- A single Beat is a single point of failure for scheduling. The usual mitigation is fast restart plus monitoring "last run" timestamps rather than true HA.
- Locking inside tasks (e.g., DB advisory lock, Redis `SET NX` with expiry) protects against duplicates from any cause.
- Community schedulers such as RedBeat use a Redis lock so only one Beat is active; evaluate maintenance status before adopting.

**Remember:** One Beat, `Recreate` rollouts, idempotent scheduled tasks.

## Q24. Beat is not always the right scheduler

Beat is great when the schedule is part of the app and tasks already live in Celery. Alternatives fit other shapes of problem.

| Option | When it fits | Watch out for |
|---|---|---|
| Celery Beat | App-owned periodic tasks, already on Celery | Single instance; limited visibility of past runs |
| django-celery-beat | Schedules editable by staff at runtime | Still one Beat process; DB load |
| Kubernetes CronJob | Infra-owned batch jobs, container per run | Pod startup cost; set `concurrencyPolicy: Forbid` for no overlap |
| DB "due jobs" table + periodic poller | Per-user schedules (reminders at user-chosen times) | Need `SELECT ... FOR UPDATE SKIP LOCKED` or equivalent |
| Workflow engine (e.g., Temporal) | Long-running, stateful, durable timers | New platform to operate |
| Cloud schedulers (e.g., EventBridge Scheduler) | Managed, serverless targets | Vendor coupling |

**Example:** "Send a reminder 24 hours before each booking" should not be one Beat entry per booking or a 24-hour `eta`. Store `remind_at` on the booking and run a Beat task every minute that claims due rows and enqueues sends.

**Trade-offs and pitfalls:**

- Long `eta` values as a scheduler are fragile (worker memory, visibility timeout, restarts).
- Mixing several schedulers makes "what runs when" hard to answer; document the owner of each job.

**Remember:** Beat for fixed app schedules; a DB table for per-entity schedules; CronJobs or workflow engines for infra and long-lived workflows.

## References

- [Celery documentation: periodic tasks](https://docs.celeryq.dev/en/stable/)
- [Kubernetes and orchestration (this site)](../../devops/orchestration/index.md)
