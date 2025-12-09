# 📊 Logging & Monitoring

---

## 📍 Navigation

<div align="center">

[← Previous: Database & Caching](19%29%20Database%20%26%20Caching.md) • [Home: Questions Index](question.md) • [Next: Accessibility →](21%29%20Accessibility.md)

[📋 Cheatsheet](FE-System-Design%20Interview%20Cheatsheet.md)

</div>

---

---

## Q89. Telemetry

Telemetry is the automatic collection of metrics, logs, and traces from your application so you can understand how it behaves in real usage. For frontend systems, it's your eyes and ears in production. Proper telemetry implementation helps you understand user behavior, identify issues quickly, and make data-driven decisions about your application.

---

## 1. What to collect

### 🔹 Metrics

* Web Vitals (LCP, INP, CLS)

* Error rates

* API latency and failure rates

### 🔹 Events

* User actions (clicks on key CTAs, form submissions)

* Page views / route changes

* Feature usage (which components/flows are actually used)

📌 **In simple terms**: Telemetry is “numbers and events from real users that tell you how the app is doing.”

---

## 2. Frontend implementation

* Use a telemetry SDK (Sentry, Datadog, OpenTelemetry, custom)

* Standardize an event schema:
  * `event_name`, `user_id` (anonymized), `page`, `version`, `tags`

* Batch and throttle events to reduce network overhead

---

## ⭐ Summary — 10-second Interview Version

> "Telemetry collects metrics and events from real users so we can see performance, errors, and feature usage. On the frontend I instrument key flows and send structured, privacy-aware events."

---

## ⭐ Extra Points (If Interviewer Asks More)

### How do you avoid noisy telemetry?

Define a small set of important events and metrics, sample high-volume data, and regularly clean up unused events.

---

## Q90. Alerting

Alerting turns telemetry signals into notifications for humans when something goes wrong or drifts from expected behavior. Good alerts are rare, actionable, and clearly owned.

---

## 1. What to alert on

* Error rate spikes (JS errors, failed API calls)

* Performance regressions (LCP above target, timeouts)

* Availability issues (uptime checks failing)

📌 **In simple terms**: Alerts are “wake-up calls” based on telemetry when users are having a bad experience.

---

## 2. Designing good alerts

* Tie each alert to:
  * **Owner** (team/on-call)
  * **Channel** (Slack, PagerDuty, email)
  * **Runbook** (what to check, how to mitigate)

* Avoid alert fatigue:
  * Use thresholds and time windows
  * Deduplicate and group similar alerts

---

## ⭐ Summary — 10-second Interview Version

> "Alerting watches metrics like error rate and performance and notifies the right team when thresholds are breached. Good alerts are owned, rare, and come with a clear runbook."

---

## ⭐ Extra Points (If Interviewer Asks More)

### Example alert you’d set for frontend?

An alert when JS error rate or failed API calls exceed a threshold for more than 5 minutes on a key route.

---

## Q91. Fixing Performance and Error Issues

Fixing issues is about turning telemetry and alerts into concrete improvements. It requires a repeatable workflow from detection to verification.

---

## 1. Debugging workflow

### 🔹 For errors

1. Inspect error logs and stack traces (Sentry/console)

2. Reproduce locally using same route, device, or feature flag

3. Fix root cause (null checks, correct API usage, race conditions)

4. Add or improve tests to prevent regressions

### 🔹 For performance issues

1. Identify slow pages/routes via Web Vitals

2. Use DevTools/Lighthouse to find heavy components or requests

3. Apply optimizations (code splitting, memoization, caching)

4. Re-measure and compare before/after

📌 **In simple terms**: Use telemetry to find where users hurt the most, then reproduce, fix, and verify with new data.

---

## 2. Closing the loop

* Link issues to alerts and dashboards

* Document fixes and patterns so the team learns

* Tune alert thresholds if needed

---

## ⭐ Summary — 10-second Interview Version

> "To fix issues I use logs and metrics to find the biggest problems, reproduce them, apply targeted fixes, add tests, and then verify improvements in telemetry dashboards."

---

## ⭐ Extra Points (If Interviewer Asks More)

### How do you prioritize what to fix first?

Look at impact: number of users affected, business-critical flows, and trend (getting worse or stable).

---

---

## 📍 Navigation

<div align="center">

[15) Database & Caching.md](15%29%20Database%20&%20Caching.md) • [Questions Index](question.md) • [17) Accessibility.md →](17%29%20Accessibility.md)

[FE-System-Design Cheatsheet](FE-System-Design%20Interview%20Cheatsheet.md]

</div>

---
