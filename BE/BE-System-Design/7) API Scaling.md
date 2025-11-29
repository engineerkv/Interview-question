# 4. API Scaling (Q51–65)

---

## Q51. Vertical vs horizontal API scaling

Vertical API scaling means adding more resources to your existing servers - like upgrading from 2 CPU cores to 8 cores or increasing memory. Horizontal API scaling means adding more servers to handle more requests - like going from 2 API servers to 10 servers behind a load balancer. Choose vertical when you have a single server bottleneck and it's cheaper to upgrade, choose horizontal when you need to scale beyond one server's limits or want better fault tolerance.

- **Trade-offs**: Vertical scaling is simpler because you don't need to change your architecture, but there's a hard limit - you can only make a server so powerful and it's expensive. Horizontal scaling can scale almost infinitely and is more fault-tolerant, but the catch is you need stateless APIs and proper load balancing, which requires architectural changes.

---

## Q52. Stateless API design for scaling

Stateless APIs don't store session data on the server - each request contains all the information needed to process it, like authentication tokens or request context. This enables horizontal scaling because any server can handle any request, and you can add or remove servers without worrying about where previous requests went. Store session data in shared storage like Redis or databases, not in server memory.

- **Trade-offs**: Stateless design enables easy horizontal scaling and improves fault tolerance, but the catch is you have to send more data with each request, and you can't use server-side sessions easily. The tricky part is handling authentication - you need tokens or signed cookies instead of server-side sessions, which adds complexity.

---

## Q53. Scaling APIs using ALB/NLB

Application Load Balancer (ALB) distributes HTTP/HTTPS traffic across multiple API servers using health checks and routing rules - it supports path-based and host-based routing, SSL termination, and integrates with AWS services. Network Load Balancer (NLB) operates at layer 4 and handles TCP/UDP traffic with lower latency - use it for high-performance scenarios. Both enable horizontal scaling by distributing load across multiple instances.

- **Trade-offs**: ALB provides advanced routing and integrates well with AWS services, but the catch is it has higher latency than NLB. NLB has lower latency and handles millions of requests per second, but the tricky part is it doesn't support path-based routing or advanced features. Choose ALB for HTTP APIs, NLB for high-performance TCP/UDP.

---

## Q54. Scaling API Gateway

API Gateway scales automatically to handle traffic spikes, but you can optimize scaling by using caching to reduce backend load, enabling throttling to protect backends, using regional endpoints for lower latency, and configuring proper stage variables. For very high traffic, use multiple API Gateway instances in different regions, or use CloudFront in front of API Gateway for global distribution.

- **Trade-offs**: API Gateway auto-scales, which is convenient, but the catch is it has per-account limits and can throttle if you exceed them. The tricky part is caching - API Gateway caching reduces backend load, but you need to invalidate cache when data changes, and cache misses still hit your backend.

---

## Q55. How CDNs reduce API load

CDNs cache API responses at edge locations close to users, so requests are served from the CDN instead of your origin server - this reduces load on your API servers, improves response times, and handles traffic spikes better. Use CDNs for GET requests with cacheable responses, and configure cache headers to control how long responses are cached.

- **Trade-offs**: CDNs dramatically reduce API load and improve performance, but the catch is they only work for cacheable GET requests - POST, PUT, DELETE requests still hit your origin. The tricky part is cache invalidation - when data changes, you need to invalidate CDN cache, which takes time and can be expensive.

---

## Q56. Token Bucket vs Leaky Bucket algorithms

Token Bucket allows bursts by accumulating tokens over time - you have a bucket that fills with tokens at a steady rate, and each request consumes a token. If tokens are available, requests are allowed immediately, enabling bursts. Leaky Bucket processes requests at a constant rate like a leaky bucket - requests are queued and processed at a fixed rate, smoothing out bursts.

- **Trade-offs**: Token Bucket allows bursts which is good for handling traffic spikes, but the catch is bursts can overwhelm downstream systems if not controlled. Leaky Bucket smooths traffic which protects downstream systems, but the tricky part is it can cause delays during traffic spikes. Choose Token Bucket when you want to allow bursts, Leaky Bucket when you need constant rate limiting.

---

## Q57. Multi-region API scaling strategies

Scale APIs across multiple regions by deploying API servers in each region, using Route53 latency-based routing to send users to the nearest region, and replicating data across regions. Use global load balancers or DNS-based routing to distribute traffic, and design stateless APIs so any region can handle any request. Consider data consistency - use eventual consistency for better performance, or strong consistency if needed.

- **Trade-offs**: Multi-region deployment provides low latency worldwide and disaster recovery, but the catch is it costs more and adds complexity - you need to manage deployments, data replication, and routing across regions. The tricky part is data consistency - eventual consistency is faster but users might see stale data, strong consistency is slower but guarantees fresh data.

---

## Q58. High-throughput API design patterns

Design high-throughput APIs by using async processing for long-running tasks, batching multiple operations into single requests, using connection pooling, implementing efficient caching, and optimizing database queries. Use message queues for background processing, return job IDs for async operations, and design APIs to minimize round trips.

- **Trade-offs**: High-throughput patterns improve performance and capacity, but the catch is they add complexity - async processing requires job tracking, batching requires careful design. The tricky part is balancing throughput with latency - some optimizations improve throughput but add latency, so you need to choose based on your requirements.

---

## Q59. Avoiding API hotspots

Avoid API hotspots by using consistent hashing for load distribution, avoiding sequential IDs that create hot partitions, using random or UUID-based identifiers, and distributing load evenly across shards or partitions. Monitor API usage patterns to identify hotspots, and use rate limiting or throttling to prevent single users or endpoints from overwhelming the system.

- **Trade-offs**: Avoiding hotspots ensures even load distribution, which improves performance and prevents overload, but the catch is you need to design your data model and routing carefully. The tricky part is identifying hotspots - they might not be obvious until you're at scale, so you need good monitoring to catch them early.

---

## Q60. API throttling vs rate limiting

Rate limiting restricts how many requests a user or IP can make in a time window - like 100 requests per minute per user. Throttling slows down requests when limits are exceeded instead of rejecting them - like allowing requests but processing them at a reduced rate. Both protect your API from overload, but rate limiting is simpler while throttling provides better user experience.

- **Trade-offs**: Rate limiting is simple and prevents overload, but the catch is rejected requests provide poor user experience. Throttling provides better UX by slowing requests instead of rejecting them, but the tricky part is it's more complex to implement and can still cause timeouts if throttling is too aggressive.

---

## Q61. Scaling APIs with caching layers

Add caching layers at multiple levels - use CDN caching for static responses, API Gateway caching for frequently accessed data, application-level caching with Redis for dynamic data, and database query caching. Cache at the edge for global distribution, cache at the API layer for frequently accessed endpoints, and cache database queries to reduce database load.

- **Trade-offs**: Caching dramatically improves performance and reduces backend load, but the catch is you need to manage cache invalidation - when data changes, you need to update or invalidate cache, otherwise users see stale data. The tricky part is cache strategy - what to cache, how long to cache, and when to invalidate - requires understanding your access patterns.

---

## Q62. Efficient pagination strategies for large APIs

Use cursor-based pagination for large datasets - instead of offset/limit which gets slower as offset increases, use a cursor (like last item ID) to fetch the next page. For smaller datasets, offset/limit is fine. Use keyset pagination for databases by using indexed columns, and avoid total count queries which are expensive for large tables.

- **Trade-offs**: Cursor-based pagination performs consistently regardless of position in the dataset, which is great for large datasets, but the catch is it's more complex to implement and doesn't support jumping to arbitrary pages. Offset/limit is simple but gets slower as you paginate deeper. The tricky part is choosing the right strategy based on dataset size and access patterns.

Example:

```javascript
// Cursor-based pagination
GET /api/users?cursor=123&limit=20
// Returns users after ID 123, with next cursor

// Offset-based pagination (for smaller datasets)
GET /api/users?offset=0&limit=20
```

---

## Q63. Reducing DB load via query batching

Reduce database load by batching multiple queries into single requests - instead of making 100 separate queries, combine them into one query or use batch operations. Use database connection pooling to reuse connections, implement query result caching, and use bulk operations for inserts and updates. Design APIs to accept batch requests when possible.

- **Trade-offs**: Query batching reduces database round trips and improves performance, but the catch is it adds complexity - you need to handle partial failures, validate batch requests, and design batch APIs. The tricky part is batch size - too small and you don't get benefits, too large and you risk timeouts or memory issues.

---

## Q64. Hypermedia-driven API design

Hypermedia APIs include links in responses that tell clients what actions are available - like including a "next" link for pagination or "update" link for editing. This enables clients to discover available actions dynamically instead of hardcoding URLs, making APIs more flexible and easier to evolve. Use formats like HAL or JSON-LD to include links in responses.

- **Trade-offs**: Hypermedia APIs are more flexible and self-documenting, which is great for API evolution, but the catch is they're more complex to implement and clients need to parse links. The tricky part is adoption - many clients ignore links and hardcode URLs anyway, so you might not get the benefits unless clients are designed for hypermedia.

---

## Q65. Scaling webhooks API endpoints

Scale webhook endpoints by using message queues to decouple webhook delivery from processing - when a webhook event occurs, publish it to a queue, and workers process webhooks asynchronously. Use exponential backoff for retries, implement idempotency to handle duplicate deliveries, and use webhook signatures to verify authenticity. Scale workers horizontally to handle webhook volume.

- **Trade-offs**: Queuing webhooks enables reliable delivery and horizontal scaling, but the catch is it adds latency - webhooks aren't delivered immediately. The tricky part is handling failures - webhook endpoints might be down, so you need retry logic with backoff, and you need to handle duplicate deliveries since webhooks might be retried.
