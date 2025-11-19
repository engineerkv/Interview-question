# Section 1: System Design Fundamentals (Q1-Q25)

---

## Q1. What are functional vs non-functional requirements?

Functional requirements describe what the system should do - like "users can create accounts" or "the system processes payments". Non-functional requirements describe how well the system should perform - like "response time under 200ms" or "99.9% uptime". Functional tells you the features, non-functional tells you the quality standards.

- **Trade-offs**: Functional requirements are easier to test, but non-functional requirements are trickier because you can only measure performance and reliability under real load. The catch is non-functional requirements cost more but they're what separates a working system from a production-ready one.

---

## Q2. What is a distributed system?

A distributed system is a collection of independent computers that work together and appear as a single system to users - like when your app runs on multiple servers across different data centers but users just see one service. The computers communicate over a network and coordinate to achieve a common goal, which allows you to scale beyond what a single machine can handle.

- **Trade-offs**: Distributed systems handle way more load and are more fault-tolerant, but the tricky part is they're way more complex - you have to deal with network failures, data consistency, and coordination which can cause weird bugs that are hard to debug.

---

## Q3. Vertical vs horizontal scaling – which to choose?

Vertical scaling means adding more power to your existing server - like upgrading from 4GB to 16GB RAM. Horizontal scaling means adding more servers - like going from 1 server to 10 servers. Choose vertical when you have a single machine bottleneck and it's cheaper to upgrade, choose horizontal when you need to scale beyond one machine's limits or want better fault tolerance.

- **Trade-offs**: Vertical scaling is simpler but has a hard limit and gets expensive. Horizontal scaling can scale almost infinitely and is more fault-tolerant, but the catch is you need to design for multiple machines with load balancing, data distribution, and state management.

---

## Q4. What is latency vs throughput?

Latency is how long it takes for one request to complete - like 50ms for a single API call. Throughput is how many requests you can handle per second - like 1000 requests per second. Latency is about speed of individual operations, throughput is about total capacity.

- **Trade-offs**: Low latency means fast responses, but optimizing for latency can reduce throughput. High throughput handles more users, but if latency is high, each user still has a slow experience. The tricky part is they're often related - optimizing for one might hurt the other.

---

## Q5. What is high availability?

High availability means your system stays up and running even when things break - like when a server crashes or a database goes down, users don't notice because other servers take over. It's usually measured as uptime percentage - like 99.9% means your system is down less than 9 hours per year.

- **Trade-offs**: High availability requires redundancy which costs more money and complexity. The catch is you need to design for failure from the start - health checks, automatic failover, and data replication - which adds operational overhead.

---

## Q6. What is fault tolerance?

Fault tolerance is your system's ability to keep working when components fail - like if a database server crashes, the system automatically switches to a backup without users noticing. It's about designing your system to expect failures and handle them gracefully instead of crashing.

- **Trade-offs**: Fault tolerance requires redundancy and error handling everywhere which adds complexity and cost, but your system stays up even when things break. The tricky part is you have to think about all the ways things can fail and handle each one.

---

## Q7. Explain CAP theorem with real-world examples.

CAP theorem says you can only guarantee two out of three: Consistency (all nodes see the same data), Availability (every request gets a response), or Partition tolerance (system works even if nodes can't communicate). Most distributed systems choose AP or CP - like DynamoDB chooses AP (available and partition-tolerant but eventually consistent), while traditional databases choose CP (consistent and partition-tolerant but might reject requests if nodes are down).

- **Trade-offs**: Choosing AP means your system always responds but data might be slightly stale, which works great for social media feeds. Choosing CP means data is always consistent but your system might reject requests during network partitions, which works for banking. The catch is you can't have all three.

---

## Q8. Difference between consistency, availability, and durability.

Consistency means all users see the same data at the same time - like when you update a profile, everyone immediately sees the change. Availability means your system responds to every request even if some parts are down - like if one server crashes, others still handle requests. Durability means once data is written, it survives crashes - like your database writes to disk so you don't lose data if the server restarts.

- **Trade-offs**: Strong consistency requires coordination which can slow things down and reduce availability. High availability needs redundancy which costs more. Durability means writing to disk which is slower but protects against data loss. The tricky part is you often have to trade one for another.

---

## Q9. What is sharding and when do you apply it?

Sharding splits your database into smaller pieces called shards, each stored on different servers - like splitting user data by user ID so users 1-1000 go to server A, 1001-2000 go to server B. You apply it when your database is too big for one machine or when queries are too slow because there's too much data in one place.

- **Trade-offs**: Sharding allows you to scale beyond one machine's limits and speeds up queries, but the catch is cross-shard queries are way more complex and rebalancing is tricky. You also need to pick a good shard key - if you choose wrong, you can end up with hot shards that get all the traffic.

---

## Q10. What is replication and why is it important?

Replication means keeping copies of your data on multiple servers - like having your database on three servers where writes go to one and get copied to the others. It's important because it gives you redundancy if one server crashes, allows you to scale reads by sending queries to different servers, and can improve performance by keeping data closer to users.

- **Trade-offs**: Replication adds complexity because you have to keep copies in sync, and there's always a delay. The catch is you need to decide between synchronous replication (slower writes but guaranteed consistency) or asynchronous replication (faster writes but risk of data loss). More replicas mean better fault tolerance but also more overhead.

---

## Q11. How does caching improve system performance?

Caching stores frequently accessed data in fast memory so you don't have to fetch it from slow databases or compute it every time - like storing user profiles in Redis so you can return them in 1ms instead of querying the database which takes 50ms. It reduces database load, speeds up responses, and can handle way more requests per second.

- **Trade-offs**: Caching makes reads super fast and reduces database load, but the tricky part is keeping cache and database in sync - if you update the database, you need to invalidate the cache, otherwise users see stale data. Memory is expensive so you need smart eviction policies like LRU.

---

## Q12. CDN vs reverse proxy.

A CDN is a network of servers around the world that cache static content close to users - like images and CSS files stored in data centers near each user so they load faster. A reverse proxy sits in front of your servers and handles requests - like routing traffic, load balancing, or adding SSL termination before requests hit your app servers.

- **Trade-offs**: CDNs are great for static content because they reduce latency and take load off your servers, but they're not great for dynamic content. Reverse proxies are flexible and can do load balancing and SSL termination, but they add another hop. The catch is you often use both - CDN for static assets, reverse proxy for dynamic requests.

---

## Q13. What is a circuit breaker pattern?

A circuit breaker stops calling a failing service after too many failures - like if your payment service is down, instead of waiting 30 seconds for each request to timeout, the circuit breaker "opens" and immediately returns an error. After a timeout, it tries again to see if the service recovered, and if it works, it "closes" and starts sending requests again.

- **Trade-offs**: Circuit breakers prevent cascading failures by failing fast, which protects your system when downstream services are down. The catch is you need to handle the "open" state gracefully - maybe return cached data or a default response. The tricky part is tuning the thresholds - too sensitive and you'll open on temporary hiccups, too lenient and you'll keep hammering a dead service.

---

## Q14. What is a bulkhead pattern?

A bulkhead pattern isolates resources so failures in one part don't bring down everything - like having separate thread pools for different services so if one service is slow, it doesn't block requests to other services. It's named after ship bulkheads that prevent water from flooding the entire ship if one compartment leaks.

- **Trade-offs**: Bulkheads prevent one slow component from taking down your entire system, which is great for reliability. The catch is you need to carefully allocate resources - if you give each service its own thread pool, you might waste resources when some services are idle.

---

## Q15. What is rate limiting?

Rate limiting restricts how many requests a user or IP can make in a time window - like allowing 100 requests per minute per user, and blocking or throttling requests after that. It protects your system from abuse, prevents one user from hogging resources, and helps you handle traffic spikes gracefully.

- **Trade-offs**: Rate limiting protects your servers from being overwhelmed and prevents abuse, but the catch is you need to pick good limits - too strict and you'll block legitimate users, too lenient and you won't stop attacks. The tricky part is deciding what to do when limits are hit - return an error, queue the request, or slow it down.

---

## Q16. What is eventual consistency?

Eventual consistency means data will become consistent across all nodes eventually, but not immediately - like when you update your profile, it might take a few seconds for all servers to show the change. It's a trade-off that prioritizes availability and performance over immediate consistency.

- **Trade-offs**: Eventual consistency allows your system to stay available and fast even during network partitions, which works great for systems where slight delays are acceptable. The catch is users might see stale data temporarily, which can be confusing. The tricky part is handling conflicts when the same data is updated in different places at the same time.

---

## Q17. What is strong consistency?

Strong consistency means all nodes see the same data at the same time - like when you update a value, every server immediately reflects that change before any read can happen. It guarantees that reads always return the most recent write, which is important for things like account balances or inventory counts.

- **Trade-offs**: Strong consistency prevents users from seeing stale or conflicting data, which is critical for financial systems. The catch is it requires coordination which slows down writes and can reduce availability during network partitions. The tricky part is it's harder to scale because every write needs to be coordinated across all replicas.

---

## Q18. How do you identify bottlenecks in distributed systems?

You identify bottlenecks by monitoring metrics like response times, throughput, CPU usage, memory, disk I/O, and network latency - when one metric spikes while others are normal, that's usually your bottleneck. Use distributed tracing to follow requests across services and see where they slow down, and look for patterns like one service taking way longer than others or one database shard getting all the traffic.

- **Trade-offs**: Monitoring gives you visibility into what's slow, but the catch is you need good instrumentation everywhere or you'll have blind spots. Distributed tracing shows you the full request path but adds overhead and can be expensive at scale. The tricky part is distinguishing between symptoms and root causes.

---

## Q19. What is backpressure and how to handle it?

Backpressure is when a fast producer overwhelms a slow consumer - like a service sending 1000 messages per second to a database that can only process 100 per second, causing messages to queue up and memory to fill. You handle it by slowing down the producer, buffering with limits, dropping messages, or using flow control mechanisms that tell the producer to slow down.

- **Trade-offs**: Backpressure prevents memory overflow and system crashes by controlling flow, but the catch is you need to decide what to do when backpressure kicks in - slow down, drop messages, or buffer with limits. The tricky part is implementing it correctly - if you slow down too much, you waste resources, if you don't slow down enough, you'll still overwhelm the consumer.

---

## Q20. What is a distributed transaction?

A distributed transaction updates data across multiple databases or services atomically - like transferring money from one bank account to another where both updates must succeed or both must fail. It's tricky because you need to coordinate commits across different systems, which is why two-phase commit exists but it's slow and can block if one system is down.

- **Trade-offs**: Distributed transactions guarantee data consistency across services, which is important for financial operations, but the catch is they're slow because they require coordination and can block if any participant is unavailable. The tricky part is they don't scale well - as you add more services, the chance of one being down increases.

---

## Q21. What is the Saga pattern?

The Saga pattern breaks a distributed transaction into a series of local transactions with compensating actions - like booking a flight, then a hotel, then a car, and if the car booking fails, you cancel the hotel and flight. Each step commits immediately, and if something fails later, you run compensating transactions to undo previous steps.

- **Trade-offs**: Sagas avoid the blocking and coordination overhead of distributed transactions, which makes them faster and more scalable. The catch is you have to write compensating logic for every step, and if a compensation fails, you can end up in an inconsistent state. The tricky part is handling partial failures - you need idempotent operations and careful error handling.

---

## Q22. What is graceful degradation?

Graceful degradation means your system keeps working with reduced functionality when parts fail - like if your recommendation service is down, the product page still loads but without personalized recommendations, or if images fail to load, the page still shows text. It's about prioritizing core features and having fallbacks so users can still accomplish their main goals.

- **Trade-offs**: Graceful degradation keeps your system usable during failures, which is way better than showing an error page, but the catch is you need to design fallbacks for every non-critical feature. The tricky part is deciding what's critical - if you degrade too much, users might as well see an error.

---

## Q23. Failover vs fallback.

Failover automatically switches to a backup system when the primary fails - like if your main database server crashes, traffic automatically routes to a replica. Fallback provides an alternative way to accomplish the same goal when the primary method fails - like if your payment gateway is down, you show users an option to pay later or use a different payment method.

- **Trade-offs**: Failover is automatic and transparent to users, which is great for critical infrastructure, but the catch is you need redundant systems ready to go, which costs money. Fallback gives users options when things break, which improves user experience, but the tricky part is you need to design multiple paths for every feature.

---

## Q24. Stateless vs stateful design.

Stateless design means each request contains all the information needed to process it - like REST APIs where the server doesn't remember previous requests. Stateful design means the server remembers information between requests - like a shopping cart stored in server memory that you add items to across multiple requests.

- **Trade-offs**: Stateless design is easier to scale because you can add servers without worrying about where previous requests went, and if a server crashes, you don't lose session data. The catch is you have to send more data with each request. Stateful design can be more efficient for WebSocket connections, but the tricky part is it's harder to scale because you need sticky sessions or shared state storage.

---

## Q25. What is P99 latency?

P99 latency is the response time that 99% of requests are faster than - like if P99 is 200ms, that means 99 out of 100 requests complete in under 200ms, and 1 request takes longer. It's more useful than average latency because it shows you the worst-case experience for most users, ignoring outliers that might skew the average.

- **Trade-offs**: P99 gives you a better picture of user experience than average because it shows what most users actually experience. The catch is you need to collect latency data for all requests to calculate percentiles accurately. The tricky part is P99 can hide really bad outliers - if 1% of requests take 10 seconds, your P99 might still look good, but those users have a terrible experience.
