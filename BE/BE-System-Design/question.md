# 🎯 Backend System Design Interview Questions

240 carefully curated questions covering backend system design fundamentals to real-world scenarios, including API scaling, REST vs GraphQL, and communication protocols.

## 📋 Quick Navigation

| Section | Topic | Questions | Difficulty |
|---------|-------|-----------|------------|
| [1️⃣](#1-system-design-fundamentals) | System Design Fundamentals | Q1–25 | ⭐⭐ |
| [2️⃣](#2-database-design) | Database Design | Q26–60 | ⭐⭐⭐ |
| [3️⃣](#3-communication-protocols) | Communication Protocols | Q61–75 | ⭐⭐⭐⭐ |
| [4️⃣](#4-rest-vs-graphql) | REST vs GraphQL | Q76–85 | ⭐⭐⭐ |
| [5️⃣](#5-api-scaling) | API Scaling | Q86–100 | ⭐⭐⭐⭐ |
| [6️⃣](#6-messaging-systems) | Messaging Systems | Q101–130 | ⭐⭐⭐⭐ |
| [7️⃣](#7-nodejs-system-design) | Node.js System Design | Q131–150 | ⭐⭐⭐ |
| [8️⃣](#8-aws-cloud-architecture) | AWS Cloud Architecture | Q151–175 | ⭐⭐⭐⭐ |
| [9️⃣](#9-observability) | Observability | Q176–190 | ⭐⭐⭐⭐ |
| [🔟](#10-git-docker-cicd-tooling) | Git, Docker, CI/CD, Tooling | Q191–210 | ⭐⭐⭐ |
| [1️⃣1️⃣](#11-code-quality--debugging) | Code Quality + Debugging | Q211–220 | ⭐⭐⭐⭐ |
| [1️⃣2️⃣](#12-ai-tools) | AI Tools | Q221–225 | ⭐⭐ |
| [1️⃣3️⃣](#13-real-system-design-scenarios) | Real System Design Scenarios | Q226–240 | ⭐⭐⭐⭐⭐ |

---

## 🟦 1. System Design Fundamentals

1. Functional vs non-functional requirements
2. Distributed system
3. Vertical vs horizontal scaling
4. Latency vs throughput
5. High availability
6. Fault tolerance
7. CAP theorem with real-world examples
8. Difference between consistency, availability, and durability
9. Sharding and when to apply it
10. Replication and why it's important
11. How caching improves system performance
12. CDN vs reverse proxy
13. Circuit breaker pattern
14. Bulkhead pattern
15. Rate limiting
16. Eventual consistency
17. Strong consistency
18. Identifying bottlenecks in distributed systems
19. Backpressure and how to handle it
20. Distributed transaction
21. Saga pattern
22. Graceful degradation
23. Failover vs fallback
24. Stateless vs stateful design
25. P99 latency

---

## 🟥 2. Database Design

### SQL (15)

26. SQL vs NoSQL and when to choose which
27. ACID properties with examples
28. How SQL transactions work
29. Deadlock avoidance strategies
30. Connection pool
31. Using read replicas for scaling read-heavy workloads
32. SQL sharding patterns
33. Indexing strategy for large databases
34. Covering index
35. Query optimization best practices
36. Table partitioning and where to use it
37. Write-ahead log internals
38. Schema federation vs centralized DB
39. Designing relational schema for e-commerce
40. Archival strategies for SQL databases

### MongoDB (12)

41. Embed vs reference decision rules
42. MongoDB replica set architecture
43. Choosing the right shard key
44. Aggregation pipeline performance rules
45. Designing high-write workloads
46. MongoDB multi-document transactions
47. Indexing best practices in Mongo
48. TTL index use cases
49. Time-series schema design
50. Mongo high-throughput strategies
51. Change streams use cases
52. MongoDB anti-patterns

### Redis (8)

53. Redis architecture
54. Redis AOF vs RDB persistence
55. Redis pub/sub pros and cons
56. Redis clustering and how it works
57. Distributed locking with Redis
58. Cache invalidation best practices
59. Avoiding memory eviction issues
60. Redis vs Memcached differences

---

## 🟩 3. Communication Protocols

61. HTTP/1.1 vs HTTP/2 vs HTTP/3
62. gRPC vs REST and when to use
63. WebSockets vs SSE vs Long Polling
64. TCP vs UDP trade-offs
65. QUIC and why it's fast
66. Binary vs text protocols
67. MQTT use cases
68. Protocol overhead and latency
69. DNS resolution flow
70. TLS handshake
71. TLS session resumption
72. API communication patterns (request/response vs streaming)
73. MTLS mutual TLS use cases
74. HTTP keep-alive
75. Connection multiplexing in HTTP/2

---

## 🟦 4. REST vs GraphQL

76. REST vs GraphQL and when to choose which
77. Overfetching vs underfetching in REST vs GraphQL
78. N+1 problem in GraphQL
79. GraphQL caching challenges
80. GraphQL schema design best practices
81. GraphQL vs gRPC for backend services
82. Error handling differences between REST and GraphQL
83. Versioning in REST vs GraphQL
84. Authentication differences between REST and GraphQL
85. Performance differences at scale

---

## 🟫 5. API Scaling

86. Vertical vs horizontal API scaling
87. Stateless API design for scaling
88. Scaling APIs using ALB/NLB
89. Scaling API Gateway
90. How CDNs reduce API load
91. Token Bucket vs Leaky Bucket algorithms
92. Multi-region API scaling strategies
93. High-throughput API design patterns
94. Avoiding API hotspots
95. API throttling vs rate limiting
96. Scaling APIs with caching layers
97. Efficient pagination strategies for large APIs
98. Reducing DB load via query batching
99. Hypermedia-driven API design
100. Scaling webhooks API endpoints

---

## 🟨 6. Messaging Systems

101. Message queues vs event streams
102. Kafka vs RabbitMQ vs SQS vs Redis Streams
103. Kafka partitions and how they scale
104. Kafka consumer groups internals
105. Kafka offset management
106. Kafka retention policy
107. Kafka replication mechanism
108. Exactly-once semantics in Kafka
109. Kafka consumer lag handling
110. RabbitMQ exchange types
111. RabbitMQ acks and redeliveries
112. RabbitMQ durable queues
113. SQS Standard vs FIFO
114. SQS Visibility Timeout full flow
115. SQS DLQ architecture
116. Long polling vs short polling
117. FIFO deduplication logic
118. Scaling SQS consumers
119. Redis Streams internals
120. SNS + SQS fan-out pattern
121. Backpressure in Kafka consumers
122. Backpressure in RabbitMQ consumers
123. Poison message handling
124. Outbox pattern
125. Schema evolution in event-driven systems
126. Idempotency in event consumers
127. Event chaining in microservices
128. Multi-topic event pipelines
129. Choosing the right messaging system
130. Ensuring event ordering at scale

---

## 🟩 7. Node.js System Design

131. How Node.js handles concurrency
132. Node.js event loop phases
133. When to use worker threads
134. Handling CPU-heavy tasks in Node.js
135. Node clustering and how it works
136. Scaling Node.js horizontally
137. Designing WebSocket-based systems
138. Streaming large files in Node.js
139. Designing a rate limiter in Node.js
140. Large-scale Node.js project structure
141. Connection pooling strategies
142. Retry and exponential backoff
143. Idempotent API design in Node.js
144. JWT authentication architecture
145. Preventing brute-force attacks
146. Graceful shutdown and why it's important
147. Logging architecture for Node.js services
148. Handling partial failures in Node.js
149. Designing Node.js + S3 upload flow
150. Handling environment configs in Node.js microservices

---

## 🟧 8. AWS Cloud Architecture

### Core AWS (10)

151. EC2 vs Lambda and when to choose
152. Auto Scaling Groups internal flow
153. IAM Users vs Roles vs Policies
154. VPC architecture
155. NACLs vs Security Groups
156. Designing highly available AWS systems
157. S3 vs EFS vs EBS
158. S3 lifecycle and cost optimization
159. Route53 routing policies
160. Securing S3 buckets

### Deployment (8)

161. Deployment architecture for React + Node
162. CI/CD pipelines for microservices
163. Blue-green deployment
164. Rolling updates with zero downtime
165. CloudFront + S3 architecture
166. S3 pre-signed URL flow
167. Handling secrets with AWS Secrets Manager
168. AWS cost optimization best practices

### Database (7)

169. RDS vs DynamoDB vs Mongo Atlas
170. DynamoDB partition key design
171. DynamoDB throttling prevention
172. Multi-AZ replication in RDS
173. RDS read replicas
174. DynamoDB Global Tables
175. On-demand vs provisioned capacity

---

## 🟪 9. Observability

176. CloudWatch Metrics vs Logs vs Events
177. Creating custom CloudWatch metrics
178. CloudWatch dashboards
179. Setting alarms for auto-scaling
180. Debugging Lambda using CloudWatch
181. Cost optimization of CloudWatch logs
182. AWS X-Ray full tracing pipeline
183. Distributed tracing concepts
184. Detecting throttling via CloudWatch Metrics
185. New Relic APM
186. Monitoring Node.js with New Relic
187. New Relic distributed tracing
188. Database query monitoring with New Relic
189. Alerting best practices in New Relic
190. CloudWatch Logs vs New Relic Logs

---

## 🟥 10. Git, Docker, CI/CD, Tooling

191. Git merge vs rebase
192. Git cherry-pick
193. Fixing merge conflicts
194. GitFlow vs trunk-based development
195. Docker image vs container
196. Docker multi-stage builds
197. Reducing Docker image size
198. Docker Compose use cases
199. Securing secrets in Docker
200. Kubernetes vs Docker differences
201. CI/CD pipeline stages
202. Blue-green vs canary deployments
203. Zero-downtime deployment techniques
204. Postman automated testing
205. npm vs Yarn differences
206. package-lock.json vs yarn.lock
207. Peer dependencies in npm
208. Solving dependency conflicts
209. Node.js performance debugging tools
210. Postman environments vs globals

---

## 🟨 11. Code Quality + Debugging

211. Code review checklist
212. Debugging memory leaks
213. Debugging high CPU usage
214. Static code analysis tools
215. ESLint vs Prettier
216. Root cause analysis workflow
217. Logging best practices
218. Handling production errors
219. Preventing flaky tests
220. Measuring code quality KPIs

---

## 🟧 12. AI Tools

221. Using GitHub Copilot effectively
222. Risks of AI-generated code
223. Reviewing AI-generated code securely
224. Cursor productivity benefits
225. Using AI for refactoring safely

---

## 🟩 13. Real System Design Scenarios

226. Designing a URL shortener
227. Designing WhatsApp chat architecture
228. Designing Twitter feed system
229. Designing YouTube video streaming
230. Designing Uber backend
231. Designing a payment system
232. Designing an e-commerce platform
233. Designing a food delivery platform
234. Designing a distributed cache system
235. Designing a notification system
236. Designing a social media recommendation engine
237. Designing a search engine
238. Designing a large-scale file storage system
239. Designing a real-time analytics system
240. Designing disaster recovery architecture

---

## 📖 Complete Answer Guide

- [1) System Design Fundamentals](1%20System%20Design%20Fundamentals.md) - Q1-25
- [2) Database Design](3%20Database%20Design.md) - Q26-60
- [3) Communication Protocols](9%20Communication%20Protocols.md) - Q61-75
- [4) REST vs GraphQL](8%20REST%20vs%20GraphQL.md) - Q76-85
- [5) API Scaling](7%20API%20Scaling.md) - Q86-100
- [6) Messaging Systems](6%20Messaging%20Systems.md) - Q101-130
- [7) Node.js System Design](2%20Node.js%20System%20Design.md) - Q131-150
- [8) AWS Cloud Architecture](4%20AWS%20Cloud%20Architecture.md) - Q151-175
- [9) Observability](5%20Observability.md) - Q176-190
- [10) Git, Docker, CI-CD, Tooling](10%20Git%2C%20Docker%2C%20CI-CD%2C%20Tooling.md) - Q191-210
- [11) Code Quality + Debugging](12%20Code%20Quality%20%2B%20Debugging.md) - Q211-220
- [12) AI Tools](11%20AI%20Tools.md) - Q221-225
- [13) Real System Design Scenarios](13%20Real%20System%20Design%20Scenarios.md) - Q226-240

## 📝 Cheatsheet

[BE-System-Design Interview Cheatsheet](BE-System-Design%20Interview%20Cheatsheet.md) - Quick reference guide

---
