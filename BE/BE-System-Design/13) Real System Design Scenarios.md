# Section 13: Real System Design Scenarios (Q226-Q240)

---

## Q226. Design a URL shortener.

Design a URL shortener by generating short codes (like base62 encoding of a counter or hash), storing mappings in a database (short code -> long URL), and redirecting requests from short URLs to long URLs. Use a distributed ID generator for unique codes, cache frequently accessed mappings in Redis, and use a CDN for global distribution. Handle scale by sharding the database by short code and using consistent hashing.

- **Trade-offs**: Simple design works for basic requirements, but the catch is you need to handle collisions, scale the database, and manage cache invalidation. The tricky part is generating unique codes at scale - you need distributed ID generation or hash-based approaches with collision handling.

---

## Q227. Design WhatsApp chat architecture.

Design WhatsApp chat by using message queues to deliver messages, storing messages in a database sharded by chat ID, using WebSockets or long polling for real-time delivery, and using a message broker to route messages between users. Store chat metadata separately from messages, use read receipts to track delivery status, and implement message synchronization for offline users. Scale by sharding messages and using distributed message queues.

- **Trade-offs**: Real-time messaging requires low latency and high reliability, but the catch is you need to handle millions of concurrent connections, message ordering, and offline message delivery. The tricky part is ensuring message delivery and ordering at scale - you need reliable message queues and careful design to handle network failures and reconnections.

---

## Q228. Design Twitter feed system.

Design Twitter feed by storing tweets in a database, maintaining user timelines (home feed) using either pull model (fetch tweets from followed users on read) or push model (pre-compute timelines on write), and using caching to serve feeds quickly. For scale, use hybrid approach - push for active users, pull for inactive users. Store tweets, user relationships, and timelines, and use message queues for real-time updates.

- **Trade-offs**: Push model provides fast reads but slow writes and high storage costs. Pull model provides fast writes but slow reads for users following many people. Hybrid approach balances both, but the catch is it's more complex to implement and maintain. The tricky part is handling celebrity users with millions of followers - pushing to all followers is expensive, so you need special handling.

---

## Q229. Design YouTube video streaming.

Design YouTube video streaming by storing videos in object storage (like S3), using CDN to cache and serve videos from edge locations, encoding videos into multiple quality levels (1080p, 720p, 480p), and using adaptive bitrate streaming to adjust quality based on network conditions. Store video metadata in a database, use video processing pipelines to encode videos, and serve video chunks via HTTP range requests.

- **Trade-offs**: CDN caching reduces origin load and improves performance, but the catch is you need to handle cache invalidation when videos are updated or deleted. The tricky part is video encoding - it's CPU-intensive and time-consuming, so you need distributed encoding pipelines and storage for multiple quality versions.

---

## Q230. Design Uber backend.

Design Uber backend by using geolocation services to track drivers and riders, matching algorithms to assign nearby drivers to ride requests, using message queues for real-time updates, and storing trip data in databases. Use Redis for real-time location tracking, implement trip state machines, and use event streaming for analytics. Scale by sharding data by region and using distributed systems for matching.

- **Trade-offs**: Real-time matching requires low latency and high availability, but the catch is you need to handle millions of location updates per second and match drivers to riders quickly. The tricky part is ensuring data consistency across services - trip state needs to be consistent across matching, payment, and tracking services.

---

## Q231. Design a payment system.

Design a payment system by using idempotent APIs to prevent duplicate charges, storing transactions in a database with ACID guarantees, integrating with payment gateways (like Stripe or PayPal), and implementing reconciliation to match transactions. Use message queues for async processing, implement retry logic with exponential backoff, and use distributed transactions or sagas for multi-step payments. Ensure strong consistency for financial data.

- **Trade-offs**: Payment systems require strong consistency and reliability, which is critical, but the catch is this limits scalability and requires careful transaction handling. The tricky part is handling failures - payments can fail at various stages, and you need to ensure money isn't lost or double-charged, which requires idempotency and careful error handling.

---

## Q232. Design an e-commerce platform.

Design an e-commerce platform with separate services for products, inventory, orders, payments, and shipping. Use databases for transactional data (orders, payments), caches for frequently accessed data (product catalogs), message queues for async processing (order fulfillment, notifications), and search engines for product search. Implement inventory management to prevent overselling, use distributed transactions or sagas for order processing, and cache product data aggressively.

- **Trade-offs**: E-commerce requires handling high traffic, inventory consistency, and complex workflows, but the catch is you need to balance performance with data consistency. The tricky part is inventory management - you need to prevent overselling while handling concurrent orders, which requires careful locking or optimistic concurrency control.

---

## Q233. Design a food delivery platform.

Design a food delivery platform with services for restaurants, orders, delivery tracking, and payments. Use geolocation to track delivery drivers, match orders to nearby drivers, and estimate delivery times. Store orders in databases, use message queues for order processing and notifications, and implement real-time tracking using WebSockets or server-sent events. Scale by sharding data by region and using distributed matching algorithms.

- **Trade-offs**: Food delivery requires real-time tracking and matching, which needs low latency, but the catch is you need to handle location updates, order state changes, and driver availability in real-time. The tricky part is matching algorithms - you need to match orders to drivers efficiently while considering distance, driver availability, and delivery time estimates.

---

## Q234. Design a distributed cache system.

Design a distributed cache by using consistent hashing to distribute data across cache nodes, implementing replication for fault tolerance, using cache eviction policies (like LRU), and handling cache invalidation. Use a distributed hash table to route requests to the right node, implement gossip protocols for node discovery, and use versioning or timestamps for cache coherence. Scale by adding nodes and rehashing data.

- **Trade-offs**: Distributed caching improves performance and reduces database load, but the catch is you need to handle cache coherence, node failures, and data distribution. The tricky part is cache invalidation - when data changes, you need to invalidate or update cache across all nodes, which requires coordination and can be complex.

---

## Q235. Design a notification system.

Design a notification system by using message queues to decouple notification generation from delivery, supporting multiple channels (email, SMS, push), using templates for different notification types, and implementing retry logic for failed deliveries. Store notification preferences and history, use worker pools to process notifications, and rate limit to prevent spam. Scale by sharding queues and using distributed workers.

- **Trade-offs**: Notification systems need to be reliable and handle high volume, but the catch is different channels have different delivery guarantees and costs. The tricky part is handling failures - notifications can fail to deliver, and you need retry logic, but you also need to avoid spamming users with retries.

---

## Q236. Design a social media recommendation engine.

Design a recommendation engine by collecting user behavior data (likes, views, interactions), using machine learning models to generate recommendations, storing user preferences and item features, and serving recommendations in real-time. Use collaborative filtering (users who liked X also liked Y) or content-based filtering (items similar to what you liked), and cache recommendations to reduce computation. Update models periodically and serve from cache.

- **Trade-offs**: Recommendation engines improve user engagement, but the catch is they require significant computation and data processing. The tricky part is balancing accuracy with performance - more accurate recommendations require more computation, but you need to serve recommendations quickly, so you often pre-compute and cache them.

---

## Q237. Design a search engine.

Design a search engine by crawling and indexing web pages, building an inverted index (word -> list of documents containing it), ranking results using algorithms (like PageRank or relevance scoring), and serving search results. Use distributed systems for crawling and indexing, store indexes across multiple nodes, and use caching for popular queries. Implement ranking algorithms to order results by relevance.

- **Trade-offs**: Search engines need to index billions of pages and serve results quickly, but the catch is indexing is computationally expensive and requires massive storage. The tricky part is ranking - you need algorithms that return relevant results, which requires understanding user intent and content relevance, and you need to update indexes as content changes.

---

## Q238. Design a large-scale file storage system.

Design large-scale file storage by splitting files into chunks, storing chunks across multiple storage nodes with replication, using a metadata service to track file locations, and implementing redundancy for fault tolerance. Use consistent hashing to distribute chunks, replicate chunks across multiple nodes, and implement repair mechanisms to restore lost chunks. Scale by adding storage nodes and rebalancing data.

- **Trade-offs**: Distributed file storage provides scalability and fault tolerance, but the catch is you need to handle data distribution, replication, and consistency across nodes. The tricky part is ensuring data durability - you need enough replicas to survive node failures, but more replicas mean more storage costs.

---

## Q239. Design a real-time analytics system.

Design a real-time analytics by ingesting events in real-time using message queues or streams, processing events using stream processing frameworks (like Kafka Streams or Flink), aggregating data in time windows, and serving results via APIs or dashboards. Use time-series databases for storing metrics, implement sliding windows for aggregations, and use caching for frequently accessed analytics. Scale by partitioning streams and using distributed processing.

- **Trade-offs**: Real-time analytics provide immediate insights, which is valuable, but the catch is they require significant infrastructure for stream processing and storage. The tricky part is handling late-arriving data and out-of-order events - you need to decide how to handle events that arrive after their time window has closed.

---

## Q240. Design disaster recovery architecture.

Design disaster recovery by replicating data across multiple regions, implementing automated failover to backup regions, maintaining backup systems that can take over quickly, and regularly testing failover procedures. Use database replication, backup storage systems, and DNS failover to route traffic to backup regions. Implement RTO (Recovery Time Objective) and RPO (Recovery Point Objective) based on business requirements.

- **Trade-offs**: Disaster recovery ensures business continuity, which is critical, but the catch is it requires significant infrastructure and costs - you need duplicate systems in multiple regions. The tricky part is balancing cost with recovery objectives - faster recovery (lower RTO) and less data loss (lower RPO) require more infrastructure and more frequent replication, which costs more.
