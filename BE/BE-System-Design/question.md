# 🎯 Backend System Design Interview Questions

225 carefully curated questions covering backend system design fundamentals to real-world scenarios, including API scaling, REST vs GraphQL, communication protocols, database design, Node.js system design, AWS cloud architecture, observability, and more.

## 📋 Quick Navigation

| Section | Topic | Questions | Difficulty |
|---------|-------|-----------|------------|
| [1️⃣](#1-system-design-fundamentals) | System Design Fundamentals | Q1–25 | ⭐⭐ |
| [2️⃣](#2-communication-protocols) | Communication Protocols | Q26–40 | ⭐⭐⭐⭐ |
| [3️⃣](#3-rest-vs-graphql) | REST vs GraphQL | Q41–50 | ⭐⭐⭐ |
| [4️⃣](#4-api-scaling) | API Scaling | Q51–65 | ⭐⭐⭐⭐ |
| [5️⃣](#5-messaging-systems) | Messaging Systems | Q66–80 | ⭐⭐⭐⭐ |
| [6️⃣](#6-aws-cloud-architecture) | AWS Cloud Architecture | Q81–105 | ⭐⭐⭐⭐ |
| [7️⃣](#7-observability) | Observability | Q106–120 | ⭐⭐⭐⭐ |
| [8️⃣](#8-database-design) | Database Design | Q121–155 | ⭐⭐⭐ |
| [9️⃣](#9-nodejs-system-design) | Node.js System Design | Q156–175 | ⭐⭐⭐ |
| [🔟](#10-git-docker-cicd-tooling) | Git, Docker, CI/CD, Tooling | Q191–210 | ⭐⭐⭐ |
| [1️⃣1️⃣](#11-code-quality--debugging) | Code Quality + Debugging | Q211–220 | ⭐⭐⭐⭐ |
| [1️⃣2️⃣](#12-ai-tools) | AI Tools | Q221–225 | ⭐⭐ |

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

## 🟩 2. Communication Protocols

26. HTTP/1.1 vs HTTP/2 vs HTTP/3

27. gRPC vs REST and when to use

28. WebSockets vs SSE vs Long Polling

29. TCP vs UDP trade-offs

30. QUIC and why it's fast

31. Binary vs text protocols

32. MQTT use cases

33. Protocol overhead and latency

34. DNS resolution flow

35. TLS handshake

36. TLS session resumption

37. API communication patterns (request/response vs streaming)

38. MTLS mutual TLS use cases

39. HTTP keep-alive

40. Connection multiplexing in HTTP/2

---

## 🟦 3. REST vs GraphQL

41. REST vs GraphQL and when to choose which

42. Overfetching vs underfetching in REST vs GraphQL

43. N+1 problem in GraphQL

44. GraphQL caching challenges

45. GraphQL schema design best practices

46. GraphQL vs gRPC for backend services

47. Error handling differences between REST and GraphQL

48. Versioning in REST vs GraphQL

49. Authentication differences between REST and GraphQL

50. Performance differences at scale

---

## 🟫 4. API Scaling

51. Vertical vs horizontal API scaling

52. Stateless API design for scaling

53. Scaling APIs using ALB/NLB

54. Scaling API Gateway

55. How CDNs reduce API load

56. Token Bucket vs Leaky Bucket algorithms

57. Multi-region API scaling strategies

58. High-throughput API design patterns

59. Avoiding API hotspots

60. API throttling vs rate limiting

61. Scaling APIs with caching layers

62. Efficient pagination strategies for large APIs

63. Reducing DB load via query batching

64. Hypermedia-driven API design

65. Scaling webhooks API endpoints

---

## 🟨 5. Messaging Systems

66. Message queues vs event streams

67. Kafka vs RabbitMQ vs SQS vs Redis Streams

68. Kafka partitions and how they scale

69. Kafka consumer groups internals

70. Kafka offset management

71. Kafka retention policy

72. Kafka replication mechanism

73. Exactly-once semantics in Kafka

74. Kafka consumer lag handling

75. RabbitMQ exchange types

76. RabbitMQ acks and redeliveries

77. RabbitMQ durable queues

78. SQS Standard vs FIFO

79. SQS Visibility Timeout full flow

80. SQS DLQ architecture

---

## 🟧 6. AWS Cloud Architecture

81. EC2 vs Lambda and when to choose

82. Auto Scaling Groups internal flow

83. IAM Users vs Roles vs Policies

84. VPC architecture

85. NACLs vs Security Groups

86. Designing highly available AWS systems

87. S3 vs EFS vs EBS

88. S3 lifecycle and cost optimization

89. Route53 routing policies

90. Securing S3 buckets

91. Deployment architecture for React + Node

92. CI/CD pipelines for microservices

93. Blue-green deployment

94. Rolling updates with zero downtime

95. CloudFront + S3 architecture

96. S3 pre-signed URL flow

97. Handling secrets with AWS Secrets Manager

98. AWS cost optimization best practices

99. RDS vs DynamoDB vs Mongo Atlas

100. DynamoDB partition key design

101. DynamoDB throttling prevention

102. Multi-AZ replication in RDS

103. RDS read replicas

104. DynamoDB Global Tables

105. On-demand vs provisioned capacity

---

## 🟪 7. Observability

106. CloudWatch Metrics vs Logs vs Events

107. Creating custom CloudWatch metrics

108. CloudWatch dashboards

109. Setting alarms for auto-scaling

110. Debugging Lambda using CloudWatch

111. Cost optimization of CloudWatch logs

112. AWS X-Ray full tracing pipeline

113. Distributed tracing concepts

114. Detecting throttling via CloudWatch Metrics

115. New Relic APM

116. Monitoring Node.js with New Relic

117. New Relic distributed tracing

118. Database query monitoring with New Relic

119. Alerting best practices in New Relic

120. CloudWatch Logs vs New Relic Logs

---

## 🟥 8. Database Design

121. SQL vs NoSQL and when to choose which

122. ACID properties with examples

123. How SQL transactions work

124. Deadlock avoidance strategies

125. Connection pool

126. Using read replicas for scaling read-heavy workloads

127. SQL sharding patterns

128. Indexing strategy for large databases

129. Covering index

130. Query optimization best practices

131. Table partitioning and where to use it

132. Write-ahead log internals

133. Schema federation vs centralized DB

134. Designing relational schema for e-commerce

135. Archival strategies for SQL databases

136. Embed vs reference decision rules

137. MongoDB replica set architecture

138. Choosing the right shard key

139. Aggregation pipeline performance rules

140. Designing high-write workloads

141. MongoDB multi-document transactions

142. Indexing best practices in Mongo

143. TTL index use cases

144. Time-series schema design

145. Mongo high-throughput strategies

146. Change streams use cases

147. MongoDB anti-patterns

148. Redis architecture

149. Redis AOF vs RDB persistence

150. Redis pub/sub pros and cons

151. Redis clustering and how it works

152. Distributed locking with Redis

153. Cache invalidation best practices

154. Avoiding memory eviction issues

155. Redis vs Memcached differences

---

## 🟩 9. Node.js System Design

156. How Node.js handles concurrency

157. Node.js event loop phases

158. When to use worker threads

159. Handling CPU-heavy tasks in Node.js

160. Node clustering and how it works

161. Scaling Node.js horizontally

162. Designing WebSocket-based systems

163. Streaming large files in Node.js

164. Designing a rate limiter in Node.js

165. Large-scale Node.js project structure

166. Connection pooling strategies

167. Retry and exponential backoff

168. Idempotent API design in Node.js

169. JWT authentication architecture

170. Preventing brute-force attacks

171. Graceful shutdown and why it's important

172. Logging architecture for Node.js services

173. Handling partial failures in Node.js

174. Designing Node.js + S3 upload flow

175. Handling environment configs in Node.js microservices

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

## 📖 Complete Answer Guide

- [1) System Design Fundamentals](01%29%20System%20Design%20Fundamentals.md) - Q1-25

- [2) Communication Protocols](02%29%20Communication%20Protocols.md) - Q26-40

- [3) REST vs GraphQL](03%29%20REST%20vs%20GraphQL.md) - Q41-50

- [4) API Scaling](04%29%20API%20Scaling.md) - Q51-65

- [5) Messaging Systems](05%29%20Messaging%20Systems.md) - Q66-80

- [6) AWS Cloud Architecture](06%29%20AWS%20Cloud%20Architecture.md) - Q81-105

- [7) Observability](07%29%20Observability.md) - Q106-120

- [8) Database Design](08%29%20Database%20Design.md) - Q121-155

- [9) Node.js System Design](09%29%20Node.js%20System%20Design.md) - Q156-175

- [10) Git, Docker, CI-CD, Tooling](10%29%20Git%2C%20Docker%2C%20CI-CD%2C%20Tooling.md) - Q191-210

- [11) Code Quality + Debugging](11%29%20Code%20Quality%20%2B%20Debugging.md) - Q211-220

- [12) AI Tools](12%29%20AI%20Tools.md) - Q221-225

## 📝 Cheatsheet

[BE-System-Design Interview Cheatsheet](BE-System-Design%20Interview%20Cheatsheet.md) - Quick reference guide

---
