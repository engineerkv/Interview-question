# 🎯 Backend System Design Interview Questions

214 carefully curated questions covering backend system design fundamentals to real-world scenarios, including API scaling, REST vs GraphQL, communication protocols, database design, Node.js system design, AWS cloud architecture, observability, and more.

## 📋 Quick Navigation

| Section | Topic | Questions | Difficulty |
|---------|-------|-----------|------------|
| [1️⃣](#1-system-design-fundamentals) | System Design Fundamentals | Q1–25 | ⭐⭐ |
| [2️⃣](#2-communication-protocols) | Communication Protocols | Q26–40 | ⭐⭐⭐⭐ |
| [3️⃣](#3-rest-vs-graphql) | REST vs GraphQL | Q41–50 | ⭐⭐⭐ |
| [4️⃣](#4-api-scaling) | API Scaling | Q51–63 | ⭐⭐⭐⭐ |
| [5️⃣](#5-messaging-systems) | Messaging Systems | Q66–94 | ⭐⭐⭐⭐ |
| [6️⃣](#6-aws-cloud-architecture) | AWS Cloud Architecture | Q95–117 | ⭐⭐⭐⭐ |
| [7️⃣](#7-observability) | Observability | Q120–134 | ⭐⭐⭐⭐ |
| [8️⃣](#8-database-design) | Database Design | Q135–168 | ⭐⭐⭐ |
| [9️⃣](#9-nodejs-system-design) | Node.js System Design | Q170–188 | ⭐⭐⭐ |
| [🔟](#10-git-docker-cicd-tooling) | Git, Docker, CI/CD, Tooling | Q190–209 | ⭐⭐⭐ |
| [1️⃣1️⃣](#11-code-quality--debugging) | Code Quality + Debugging | Q210–219 | ⭐⭐⭐⭐ |

---

## 🟦 1. System Design Fundamentals

1. 📋 Functional vs non-functional requirements

2. 🌐 Distributed system

3. 📈 Vertical vs horizontal scaling

4. ⚡ Latency vs throughput

5. ✅ High availability

6. 🛡️ Fault tolerance

7. 📊 CAP theorem with real-world examples

8. 🔄 Difference between consistency, availability, and durability

9. 📊 Sharding and when to apply it

10. 🔄 Replication and why it's important

11. ⚡ How caching improves system performance

12. 🌐 CDN vs reverse proxy

13. 🔌 Circuit breaker pattern

14. 🚢 Bulkhead pattern

15. 🚦 Rate limiting

16. ⏳ Eventual consistency

17. 🔒 Strong consistency

18. 🔍 Identifying bottlenecks in distributed systems

19. ⏸️ Backpressure and how to handle it

20. 🔄 Distributed transaction

21. 📖 Saga pattern

22. 📉 Graceful degradation

23. 🔄 Failover vs fallback

24. 📦 Stateless vs stateful design

25. 📊 P99 latency

---

## 🟩 2. Communication Protocols

26. 🌐 HTTP/1.1 vs HTTP/2 vs HTTP/3

27. ⚡ gRPC vs REST and when to use

28. 🔌 WebSockets vs SSE vs Long Polling

29. 🔌 TCP vs UDP trade-offs

30. ⚡ QUIC and why it's fast

31. 📦 Binary vs text protocols

32. 📡 MQTT use cases

33. ⚡ Protocol overhead and latency

34. 🌐 DNS resolution flow

35. 🔒 TLS handshake

36. 🔄 TLS session resumption

37. 🔗 API communication patterns (request/response vs streaming)

38. 🔐 MTLS mutual TLS use cases

39. 🔗 HTTP keep-alive

40. 🔀 Connection multiplexing in HTTP/2

---

## 🟦 3. REST vs GraphQL

41. 🔗 REST vs GraphQL and when to choose which

42. 📊 Overfetching vs underfetching in REST vs GraphQL

43. 🔢 N+1 problem in GraphQL

44. 💾 GraphQL caching challenges

45. 📐 GraphQL schema design best practices

46. ⚡ GraphQL vs gRPC for backend services

47. ⚠️ Error handling differences between REST and GraphQL

48. 🔢 Versioning in REST vs GraphQL

49. 🔐 Authentication differences between REST and GraphQL

50. ⚡ Performance differences at scale

---

## 🟫 4. API Scaling

51. 📦 Stateless API design for scaling

52. ⚖️ Scaling APIs using ALB/NLB

53. 🚪 Scaling API Gateway

54. 🌐 How CDNs reduce API load

55. 🌍 Multi-region API scaling strategies

56. ⚡ High-throughput API design patterns

57. 🔥 Avoiding API hotspots

58. 🚦 API throttling vs rate limiting

59. 💾 Scaling APIs with caching layers

60. 📄 Efficient pagination strategies for large APIs

61. 📊 Reducing DB load via query batching

62. 🔗 Hypermedia-driven API design

63. 🪝 Scaling webhooks API endpoints

---

## 🟨 5. Messaging Systems

66. 📬 Message queues vs event streams

67. ⚡ Kafka vs RabbitMQ vs SQS vs Redis Streams

68. 📊 Kafka partitions and how they scale

69. 👥 Kafka consumer groups internals

70. 📍 Kafka offset management

71. ⏰ Kafka retention policy

72. 🔄 Kafka replication mechanism

73. ✅ Exactly-once semantics in Kafka

74. ⏳ Kafka consumer lag handling

75. 🔀 RabbitMQ exchange types

76. ✅ RabbitMQ acks and redeliveries

77. 💾 RabbitMQ durable queues

78. 📬 SQS Standard vs FIFO

79. ⏱️ SQS Visibility Timeout full flow

80. 📮 SQS DLQ architecture

81. 🔑 FIFO deduplication logic

82. 📈 Scaling SQS consumers

83. 🌊 Redis Streams internals

84. 📢 SNS + SQS fan-out pattern

85. 🌊 Backpressure in Kafka consumers

86. 🌊 Backpressure in RabbitMQ consumers

87. ☠️ Poison message handling

88. 📤 Outbox pattern

89. 📐 Schema evolution in event-driven systems

90. 🔑 Idempotency in event consumers

91. 🔗 Event chaining in microservices

92. 🔀 Multi-topic event pipelines

93. 🎯 Choosing the right messaging system

94. 📊 Ensuring event ordering at scale

---

## 🟧 6. AWS Cloud Architecture

95. ☁️ EC2 vs Lambda and when to choose

96. 📈 Auto Scaling Groups internal flow

97. 🔐 IAM Users vs Roles vs Policies

98. 🌐 VPC architecture

99. 🛡️ NACLs vs Security Groups

100. ✅ Designing highly available AWS systems

101. 💾 S3 vs EFS vs EBS

102. 💰 S3 lifecycle and cost optimization

103. 🌐 Route53 routing policies

104. 🔒 Securing S3 buckets

105. 🚀 Deployment architecture for React + Node

106. 🔄 CI/CD pipelines for microservices

107. 🌐 CloudFront + S3 architecture

108. 🔗 S3 pre-signed URL flow

109. 🔐 Handling secrets with AWS Secrets Manager

110. 💰 AWS cost optimization best practices

111. 💾 RDS vs DynamoDB vs Mongo Atlas

112. 🔑 DynamoDB partition key design

113. ⚠️ DynamoDB throttling prevention

114. 🔄 Multi-AZ replication in RDS

115. 📖 RDS read replicas

116. 🌍 DynamoDB Global Tables

117. ⚡ On-demand vs provisioned capacity

---

## 🟪 7. Observability

120. 📊 CloudWatch Metrics vs Logs vs Events

121. 📈 Creating custom CloudWatch metrics

122. 📊 CloudWatch dashboards

123. 🚨 Setting alarms for auto-scaling

124. 🐛 Debugging Lambda using CloudWatch

125. 💰 Cost optimization of CloudWatch logs

126. 🔍 AWS X-Ray full tracing pipeline

127. 🔗 Distributed tracing concepts

128. ⚠️ Detecting throttling via CloudWatch Metrics

129. 📊 New Relic APM

130. 📈 Monitoring Node.js with New Relic

131. 🔍 New Relic distributed tracing

132. 🗄️ Database query monitoring with New Relic

133. 🚨 Alerting best practices in New Relic

134. 📝 CloudWatch Logs vs New Relic Logs

---

## 🟥 8. Database Design

135. 💾 SQL vs NoSQL and when to choose which

136. 🔒 ACID properties with examples

137. 🔄 How SQL transactions work

138. 🔒 Deadlock avoidance strategies

139. 🏊 Connection pool

140. 📖 Using read replicas for scaling read-heavy workloads

141. 📊 SQL sharding patterns

142. 🔍 Indexing strategy for large databases

143. 📇 Covering index

144. ⚡ Query optimization best practices

145. 📊 Table partitioning and where to use it

146. 📝 Write-ahead log internals

147. 🌐 Schema federation vs centralized DB

148. 🛒 Designing relational schema for e-commerce

149. 📦 Archival strategies for SQL databases

150. 📄 Embed vs reference decision rules

151. 📋 MongoDB replica set architecture

152. 🔑 Choosing the right shard key

153. ⚡ Aggregation pipeline performance rules

154. ✍️ Designing high-write workloads

155. 🔄 MongoDB multi-document transactions

156. 📇 Indexing best practices in Mongo

157. 📊 Time-series schema design

158. ⚡ Mongo high-throughput strategies

159. 🌊 Change streams use cases

160. ❌ MongoDB anti-patterns

161. 💾 Redis architecture

162. 💾 Redis AOF vs RDB persistence

163. 📢 Redis pub/sub pros and cons

164. 🔀 Redis clustering and how it works

165. 🔒 Distributed locking with Redis

166. 🗑️ Cache invalidation best practices

167. 💾 Avoiding memory eviction issues

168. 🔀 Redis vs Memcached differences

---

## 🟩 9. Node.js System Design

170. ⚡ How Node.js handles concurrency

171. ⚙️ Node.js event loop phases

172. 🧵 When to use worker threads

173. 💪 Handling CPU-heavy tasks in Node.js

174. 🔀 Node clustering and how it works

175. 📈 Scaling Node.js horizontally

176. 🔌 Designing WebSocket-based systems

177. 🌊 Streaming large files in Node.js

178. 🚦 Designing a rate limiter in Node.js

179. 🏗️ Large-scale Node.js project structure

180. 🔁 Retry and exponential backoff

181. 🔑 Idempotent API design in Node.js

182. 🔐 JWT authentication architecture

183. 🛡️ Preventing brute-force attacks

184. 🛑 Graceful shutdown and why it's important

185. 📝 Logging architecture for Node.js services

186. 🛠️ Handling partial failures in Node.js

187. ☁️ Designing Node.js + S3 upload flow

188. ⚙️ Handling environment configs in Node.js microservices

---

## 🟥 10. Git, Docker, CI/CD, Tooling

190. 🔀 Git merge vs rebase

191. 🍒 Git cherry-pick

192. 🔧 Fixing merge conflicts

193. 🌳 GitFlow vs trunk-based development

194. 🐳 Docker image vs container

195. 🏗️ Docker multi-stage builds

196. 📦 Reducing Docker image size

197. 🔧 Docker Compose use cases

198. 🔐 Securing secrets in Docker

199. ☸️ Kubernetes vs Docker differences

200. 🔄 CI/CD pipeline stages

201. 🔄 Blue-green vs canary deployments

202. ⚡ Zero-downtime deployment techniques

203. 🧪 Postman automated testing

204. 📦 npm vs Yarn differences

205. 🔒 package-lock.json vs yarn.lock

206. 👥 Peer dependencies in npm

207. 🔧 Solving dependency conflicts

208. 🐛 Node.js performance debugging tools

209. 🌍 Postman environments vs globals

---

## 🟨 11. Code Quality + Debugging

210. ✅ Code review checklist

211. 🐛 Debugging memory leaks

212. ⚡ Debugging high CPU usage

213. 🔍 Static code analysis tools

214. 🎨 ESLint vs Prettier

215. 🔍 Root cause analysis workflow

216. 📝 Logging best practices

217. ⚠️ Handling production errors

218. 🧪 Preventing flaky tests

219. 📊 Measuring code quality KPIs

---

## 📖 Complete Answer Guide

- [1) System Design Fundamentals](01%29%20System%20Design%20Fundamentals.md) - Q1-25

- [2) Communication Protocols](02%29%20Communication%20Protocols.md) - Q26-40

- [3) REST vs GraphQL](03%29%20REST%20vs%20GraphQL.md) - Q41-50

- [4) API Scaling](04%29%20API%20Scaling.md) - Q51-63

- [5) Messaging Systems](05%29%20Messaging%20Systems.md) - Q66-94

- [6) AWS Cloud Architecture](06%29%20AWS%20Cloud%20Architecture.md) - Q95-117

- [7) Observability](07%29%20Observability.md) - Q120-134

- [8) Database Design](08%29%20Database%20Design.md) - Q135-169

- [9) Node.js System Design](09%29%20Node.js%20System%20Design.md) - Q170-188

- [10) Git, Docker, CI-CD, Tooling](10%29%20Git%2C%20Docker%2C%20CI-CD%2C%20Tooling.md) - Q190-209

- [11) Code Quality + Debugging](11%29%20Code%20Quality%20%2B%20Debugging.md) - Q210-219

## 📝 Cheatsheet

[BE-System-Design Interview Cheatsheet](BE-System-Design%20Interview%20Cheatsheet.md) - Quick reference guide

---
