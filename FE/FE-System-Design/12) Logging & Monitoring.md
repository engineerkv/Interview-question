<div align="center">

**[← Previous: Security](11%29%20Security.md)** | **[Next: Question List →](question.md)**

</div>

# 12. Logging & Monitoring (Q147–151)

---

## Q147. Logging and monitoring overview

Logging captures application events and errors for debugging and analysis, while monitoring tracks application health, performance, and user experience in real-time. Together they provide visibility into application behavior, help identify issues quickly, and enable data-driven optimization.

- **Trade-offs**: Comprehensive logging and monitoring improve reliability and debugging but add overhead and storage costs. The catch is too much logging can impact performance and make it hard to find important information—use structured logging, appropriate log levels, and sample high-volume events. Balance detail with performance and cost.

Example:

```javascript
// Logging and monitoring strategy
// 1. Structured logging (JSON format)
// 2. Log levels (error, warn, info, debug)
// 3. Error tracking (Sentry, LogRocket)
// 4. Performance monitoring (Web Vitals, custom metrics)
// 5. User analytics (page views, interactions)
// 6. Real-time alerts for critical issues
```

---

## Q148. Telemetry

Telemetry collects and transmits data about application performance, errors, and user behavior from client to server for analysis. It includes metrics, traces, logs, and events that help understand application health and user experience.

- **Trade-offs**: Telemetry provides valuable insights but can impact performance and privacy. The catch is collect only necessary data, batch telemetry events to reduce network overhead, and respect user privacy preferences. Use sampling for high-volume events and implement data retention policies to manage costs.

Example:

```javascript
// Telemetry collection
class Telemetry {
  constructor() {
    this.events = [];
    this.batchSize = 10;
    this.flushInterval = 5000;
  }
  
  track(event, properties) {
    this.events.push({
      event,
      properties,
      timestamp: Date.now(),
      userId: getUserId(),
      sessionId: getSessionId()
    });
    
    if (this.events.length >= this.batchSize) {
      this.flush();
    }
  }
  
  flush() {
    if (this.events.length === 0) return;
    
    fetch('/api/telemetry', {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify({ events: this.events })
    });
    
    this.events = [];
  }
}

// Auto-flush periodically
setInterval(() => telemetry.flush(), telemetry.flushInterval);
```

---

## Q149. Alerting

Alerting notifies teams when application issues, errors, or performance degradation occur, enabling rapid response to problems. Alerts should be actionable, have appropriate thresholds, and avoid alert fatigue.

- **Trade-offs**: Alerts enable quick response to issues but too many alerts cause fatigue and important alerts get ignored. The catch is set appropriate thresholds, use different severity levels, and group related alerts—only alert on actionable issues that require immediate attention. Use alerting rules that reduce false positives.

Example:

```javascript
// Alerting configuration
const alertingRules = {
  errorRate: {
    threshold: 0.05, // 5% error rate
    window: '5m',
    severity: 'critical',
    notify: ['oncall', 'slack']
  },
  responseTime: {
    threshold: 2000, // 2 seconds
    percentile: 95,
    severity: 'warning',
    notify: ['slack']
  },
  availability: {
    threshold: 0.99, // 99% uptime
    window: '1h',
    severity: 'critical',
    notify: ['oncall', 'pagerduty']
  }
};

// Check metrics and trigger alerts
function checkAlerts(metrics) {
  if (metrics.errorRate > alertingRules.errorRate.threshold) {
    sendAlert({
      severity: 'critical',
      message: `Error rate ${metrics.errorRate} exceeds threshold`,
      channel: 'oncall'
    });
  }
}
```

---

## Q150. Fixing performance and error issues

Fixing issues involves identifying root causes through logs and monitoring, prioritizing fixes based on impact, and implementing solutions. Use structured debugging workflows: reproduce, isolate, fix, verify, and monitor.

- **Trade-offs**: Quick fixes resolve immediate issues but may not address root causes—take time to understand the problem fully before fixing. The catch is prioritize fixes based on impact (user count, severity, business impact) and always verify fixes don't introduce new issues. Monitor after fixes to ensure problems are resolved.

Example:

```javascript
// Error tracking and fixing workflow
// 1. Capture errors with context
window.addEventListener('error', (event) => {
  errorTracker.capture({
    message: event.message,
    stack: event.error?.stack,
    url: event.filename,
    line: event.lineno,
    column: event.colno,
    userAgent: navigator.userAgent,
    userId: getUserId()
  });
});

// 2. Analyze error patterns
// Group by error type, frequency, affected users

// 3. Reproduce and debug
// Use source maps, logs, and monitoring data

// 4. Fix and deploy
// Implement fix, add tests, deploy gradually

// 5. Verify and monitor
// Check error rates decrease, monitor for regressions
```

---

## Q151. Performance monitoring and error tracking

Performance monitoring tracks metrics like Core Web Vitals, custom performance marks, and resource timing, while error tracking captures and analyzes application errors. Combine Real User Monitoring (RUM) with error tracking for comprehensive coverage.

- **Trade-offs**: RUM provides real user data but requires sufficient traffic, error tracking helps identify issues quickly but needs proper context. The catch is monitoring adds overhead—use efficient collection methods, sample data appropriately, and set up dashboards to visualize trends. Focus on metrics that impact user experience and prioritize critical errors.

Example:

```javascript
// Performance monitoring
import { getCLS, getFID, getLCP } from 'web-vitals';

function sendToAnalytics(metric) {
  performanceAPI.track({
    name: metric.name,
    value: metric.value,
    id: metric.id,
    delta: metric.delta,
    rating: metric.rating
  });
}

getCLS(sendToAnalytics);
getFID(sendToAnalytics);
getLCP(sendToAnalytics);

// Error tracking
window.addEventListener('error', (event) => {
  errorTracker.capture({
    message: event.message,
    stack: event.error?.stack,
    url: event.filename,
    line: event.lineno,
    column: event.colno
  });
});
```

---

