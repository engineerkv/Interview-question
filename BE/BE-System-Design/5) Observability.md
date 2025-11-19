# Section 5: Observability (Q106-Q120)

---

## Q106. CloudWatch Metrics vs Logs vs Events.

CloudWatch Metrics are numeric data points over time - like CPU usage, request count, or error rate - stored as time-series data that you can graph and alarm on. CloudWatch Logs are text log files from your applications or AWS services - like application logs, access logs, or error messages. CloudWatch Events (now EventBridge) are notifications about state changes - like when an EC2 instance starts or an S3 object is created.

- **Trade-offs**: Metrics are great for monitoring performance and setting alarms, but the catch is they only store numeric data. Logs give you detailed information for debugging, but the tricky part is they can be expensive at scale and hard to search without proper indexing. Events enable event-driven architectures, but you need to configure rules and targets.

---

## Q107. Creating custom CloudWatch metrics.

Create custom metrics by using the CloudWatch API to send data points with PutMetricData - you define a metric name, namespace, dimensions, and value. Use dimensions to filter and aggregate metrics - like tracking metrics per user, per service, or per environment. Custom metrics allow you to track business metrics like orders per minute, user signups, or API response times.

- **Trade-offs**: Custom metrics give you visibility into your application's behavior, which is essential for monitoring, but the catch is they cost money per metric and data point. The tricky part is choosing good metric names and dimensions - too many dimensions and costs add up, too few and you can't drill down into issues.

Example:

```javascript
const cloudwatch = new AWS.CloudWatch();
await cloudwatch.putMetricData({
  Namespace: 'MyApp/API',
  MetricData: [{
    MetricName: 'RequestCount',
    Value: 1,
    Dimensions: [
      { Name: 'Endpoint', Value: '/users' },
      { Name: 'Status', Value: '200' }
    ],
    Timestamp: new Date()
  }]
}).promise();
```

---

## Q108. CloudWatch dashboards.

CloudWatch dashboards are customizable pages that display multiple metrics and logs in one view - you add widgets like line graphs, numbers, or logs, and refresh them automatically. Use dashboards to monitor your system's health, track key performance indicators, and visualize trends over time. You can create multiple dashboards for different teams or use cases.

- **Trade-offs**: Dashboards give you a single view of your system's health, which is great for monitoring, but the catch is they only show data from CloudWatch - you can't easily combine data from other sources. The tricky part is keeping dashboards relevant - they can become outdated as your system evolves, so you need to update them regularly.

---

## Q109. Setting alarms for auto-scaling.

Set CloudWatch alarms on metrics like CPU utilization or request count, and configure them to trigger Auto Scaling actions - when CPU goes above 70%, the alarm triggers a scale-out policy to add instances, and when it drops below 30%, it triggers a scale-in policy to remove instances. Use step scaling for gradual adjustments or simple scaling for immediate changes.

- **Trade-offs**: Alarms enable automatic scaling based on actual load, which keeps costs down and performance up, but the catch is there's a delay between detecting the need and scaling - typically 1-5 minutes. The tricky part is tuning alarm thresholds - too sensitive and you'll scale constantly, too conservative and you'll be slow to respond to traffic changes.

---

## Q110. Debugging Lambda using CloudWatch.

Debug Lambda functions by viewing CloudWatch Logs for execution logs, errors, and print statements - each invocation creates a log stream with execution details. Use X-Ray for distributed tracing to see the full request path, check CloudWatch Metrics for invocation counts and errors, and use CloudWatch Insights to query logs with SQL-like syntax. Enable detailed logging and include request IDs in your logs for easier debugging.

- **Trade-offs**: CloudWatch Logs give you visibility into Lambda execution, which is essential for debugging, but the catch is logs can be expensive at scale and there's a delay before logs appear. The tricky part is finding the right log entry among thousands - use structured logging and CloudWatch Insights queries to filter and search efficiently.

---

## Q111. Cost optimization of CloudWatch logs.

Optimize CloudWatch Logs costs by setting log retention periods to automatically delete old logs, filtering logs before sending them to CloudWatch, using log sampling for high-volume logs, and compressing logs before sending. Use CloudWatch Logs Insights only when needed since queries cost money, and consider exporting logs to S3 for long-term storage which is cheaper.

- **Trade-offs**: Cost optimization reduces spending, but the catch is shorter retention means you lose historical data for debugging, and filtering logs might remove important information. The tricky part is balancing cost with observability - you need enough logs to debug issues, but not so many that costs spiral out of control.

---

## Q112. AWS X-Ray — full tracing pipeline.

X-Ray traces requests as they travel through your distributed system - you instrument your code to send trace data, X-Ray collects segments from each service, and assembles them into a complete trace showing the full request path. You can see which services a request hit, how long each service took, and where errors occurred. Enable X-Ray on API Gateway, Lambda, EC2, and other services to get end-to-end visibility.

- **Trade-offs**: X-Ray provides complete visibility into distributed systems, which is great for debugging performance issues, but the catch is it adds overhead and costs money per trace. The tricky part is instrumenting all your services - missing instrumentation means blind spots in your traces, and you need to handle sampling to control costs.

---

## Q113. Distributed tracing concepts.

Distributed tracing follows a request across multiple services by adding a trace ID that gets passed along - each service creates a span showing its part of the request, and all spans are collected into a trace. Use trace IDs to correlate logs across services, identify bottlenecks by seeing which service takes longest, and debug issues by seeing the full request path. Tools like X-Ray, Jaeger, or Zipkin collect and visualize traces.

- **Trade-offs**: Distributed tracing is essential for debugging microservices, but the catch is it requires instrumentation in every service and adds overhead. The tricky part is sampling - you can't trace every request at scale, so you need to sample intelligently to balance visibility with performance and cost.

---

## Q114. Detecting throttling via CloudWatch Metrics.

Detect throttling by monitoring CloudWatch metrics like ThrottledRequests for DynamoDB, ThrottledRequests for API Gateway, or 429 status codes for your APIs. Set up alarms on these metrics to alert when throttling occurs, and use CloudWatch Insights to query logs for throttling patterns. Monitor read and write capacity utilization to predict when throttling might occur.

- **Trade-offs**: Monitoring throttling helps you catch capacity issues early, but the catch is by the time you see throttling metrics, users are already experiencing problems. The tricky part is proactive monitoring - you need to monitor capacity utilization and scale before throttling happens, not after.

---

## Q115. What is New Relic APM?

New Relic APM (Application Performance Monitoring) automatically instruments your applications to track performance, errors, and transactions - it shows you response times, throughput, error rates, and database query performance without requiring code changes. It provides dashboards, alerts, and detailed transaction traces to help you understand application performance and debug issues.

- **Trade-offs**: New Relic APM gives you automatic instrumentation and rich performance data, which is great for monitoring, but the catch is it's a paid service and adds overhead to your application. The tricky part is understanding the data - you get a lot of information, so you need to focus on the metrics that matter for your application.

---

## Q116. Monitoring Node.js with New Relic.

Monitor Node.js applications by installing the New Relic agent, which automatically instruments your code to track transactions, database queries, and external API calls. The agent collects performance data and sends it to New Relic, where you can see response times, error rates, and slow database queries. Configure the agent to ignore health checks, set up custom attributes, and use New Relic's Node.js API for custom instrumentation.

- **Trade-offs**: New Relic provides automatic monitoring with minimal code changes, which is convenient, but the catch is the agent adds overhead and you need to configure it properly. The tricky part is filtering noise - health checks and background jobs can clutter your metrics, so you need to configure the agent to ignore them.

---

## Q117. New Relic distributed tracing.

New Relic distributed tracing automatically traces requests across services by propagating trace context - when a request goes from service A to service B, the trace ID is passed along in headers, and New Relic collects spans from both services into a single trace. You can see the full request path, identify slow services, and debug issues across your microservices architecture.

- **Trade-offs**: Distributed tracing in New Relic works automatically once configured, which is great, but the catch is you need to ensure trace context is propagated correctly between services. The tricky part is sampling - at high volumes, you need to sample traces to control costs and overhead, but you want enough traces to catch issues.

---

## Q118. Database query monitoring with New Relic.

New Relic automatically tracks database queries from your application, showing you query execution times, slow queries, and query patterns. You can see which queries are slowest, how often they're called, and identify N+1 query problems. Use New Relic's database insights to optimize queries, and set up alerts for slow queries or high database time.

- **Trade-offs**: Database monitoring helps you identify performance bottlenecks, which is essential for optimization, but the catch is you need to understand your queries to make sense of the data. The tricky part is distinguishing between slow queries that need optimization and queries that are slow because of database load - you need to look at both query time and database metrics.

---

## Q119. Alerting best practices in New Relic.

Set up alerts on key metrics like error rate, response time, and throughput, using baselines or static thresholds. Configure alert conditions to avoid false positives - use multiple data points, set appropriate time windows, and use anomaly detection for dynamic thresholds. Route alerts to the right teams, use alert fatigue prevention, and create runbooks for common alerts.

- **Trade-offs**: Good alerting helps you catch issues quickly, but the catch is too many alerts cause alert fatigue where people ignore them. The tricky part is setting the right thresholds - too sensitive and you get false alarms, too lenient and you miss real issues. Use baselines and anomaly detection to adapt to changing traffic patterns.

---

## Q120. CloudWatch Logs vs New Relic Logs.

CloudWatch Logs is AWS-native log storage that integrates with other AWS services - it's good for AWS-centric architectures and has tight integration with Lambda, EC2, and other services. New Relic Logs provides log aggregation with better search capabilities, log parsing, and integration with APM data - you can correlate logs with traces and metrics in one place.

- **Trade-offs**: CloudWatch Logs is simpler if you're all-in on AWS and integrates well with other AWS services, but the catch is search capabilities are limited and it can be expensive at scale. New Relic Logs provides better search and correlation with APM data, but the tricky part is it's a separate service that costs money and you need to ship logs there from AWS.
