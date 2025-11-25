# Section 2: Node.js System Design (Q26-Q45)

---

## Q26. How Node.js handles concurrency

Node.js handles concurrency using an event loop that processes I/O operations asynchronously - when you make a database query or file read, Node.js doesn't wait for it to finish, it registers a callback and moves on to handle other requests. The event loop checks for completed I/O operations and runs their callbacks, letting a single thread handle thousands of concurrent connections.

- **Trade-offs**: This non-blocking I/O model is super efficient for I/O-heavy workloads like APIs and web servers because one thread can handle way more requests than blocking I/O would allow. The catch is CPU-intensive tasks block the event loop and hurt performance for all requests, which is why you need worker threads or separate processes for heavy computation.

<div align="center">

**[← Previous: System Design Fundamentals](1%29%20System%20Design%20Fundamentals.md)** | **[Next: Database Design →](3%29%20Database%20Design.md)**

</div>

---

## Q27. Node.js event loop phases

The Node.js event loop has six phases that run in order: timers (runs setTimeout/setInterval callbacks), pending callbacks (runs I/O callbacks deferred from previous iteration), idle/prepare (internal use), poll (fetches new I/O events and runs their callbacks), check (runs setImmediate callbacks), and close callbacks (runs socket close callbacks). After each phase, it runs microtasks (promises and process.nextTick) before moving to the next phase.

- **Trade-offs**: Understanding phases helps you predict when callbacks run and optimize performance, but the catch is the order can be confusing - setImmediate runs in the check phase after poll, but process.nextTick runs between every phase, which can cause unexpected ordering. The tricky part is long-running callbacks in any phase block the entire loop, so you need to keep callbacks short and defer heavy work.

---

## Q28. When to use worker threads

Use worker threads when you have CPU-intensive tasks that would block the event loop - like image processing, data encryption, or complex calculations. Worker threads run JavaScript in parallel on separate threads with their own V8 instance, so they can do heavy computation without blocking the main thread that handles I/O.

- **Trade-offs**: Worker threads allow you to do CPU work in parallel without blocking the main thread, which is great for performance, but the catch is they have overhead - each thread has its own memory space and V8 instance, so creating too many can use a lot of memory. The tricky part is communication between threads uses message passing which adds latency, so they're not great for tasks that need frequent back-and-forth communication.

---

## Q29. Handling CPU-heavy tasks in Node.js

Handle CPU-heavy tasks by offloading them to worker threads, child processes, or external services - like using worker threads for image processing, spawning child processes for heavy computations, or calling a microservice that handles the work. You can also break work into smaller chunks and use setImmediate to yield back to the event loop between chunks.

- **Trade-offs**: Offloading keeps your main thread responsive, but the catch is each approach has trade-offs - worker threads share memory but have overhead, child processes are more isolated but heavier, and external services add network latency. The tricky part is deciding which to use - worker threads for parallel JavaScript work, child processes for running other programs or when you need more isolation, and external services when you need to scale beyond one machine.

---

## Q30. Node clustering and how it works

Node clustering creates multiple worker processes that share the same server port - the master process listens on the port and distributes incoming connections to worker processes using round-robin by default. Each worker runs your application code in its own process with its own event loop, so you can utilize multiple CPU cores.

- **Trade-offs**: Clustering allows you to use all CPU cores which improves performance for CPU-bound work, and if one worker crashes, others keep running. The catch is workers don't share memory, so you can't share in-memory state between them - you need Redis or a database for shared state. The tricky part is load balancing is simple round-robin by default, which doesn't account for worker load, so you might want a smarter load balancer in front.

---

## Q31. Scaling Node.js horizontally

Scale Node.js horizontally by running multiple instances behind a load balancer - like running your app on 5 servers and using Nginx or AWS ALB to distribute traffic. Make sure your app is stateless so any instance can handle any request, use shared storage like Redis for sessions, and use a message queue for communication between instances.

- **Trade-offs**: Horizontal scaling allows you to handle way more traffic than vertical scaling and improves fault tolerance, but the catch is you need to design for it - stateless apps, shared storage, and proper load balancing. The tricky part is some things are harder to scale horizontally - like WebSocket connections need sticky sessions or a shared pub/sub system, and real-time features need careful architecture.

---

## Q32. Designing WebSocket-based systems

Design WebSocket systems by using a message broker like Redis pub/sub to share connections across servers - when a message comes in on server A, it publishes to Redis, and all servers subscribed to that channel broadcast to their connected clients. Use connection pooling, implement reconnection logic, and handle backpressure when clients can't keep up with message rates.

- **Trade-offs**: WebSockets give you real-time bidirectional communication which is great for chat, notifications, or live updates, but the catch is they're harder to scale horizontally because connections are stateful. The tricky part is you need a pub/sub system to share messages across servers, and you have to handle connection failures, reconnections, and message ordering carefully.

---

## Q33. Streaming large files in Node.js

Stream large files using Node.js streams instead of loading the entire file into memory - like using fs.createReadStream() to read a file in chunks and pipe it to the response, or using transform streams to process data as it flows. This allows you to handle files larger than available memory without crashing.

- **Trade-offs**: Streaming uses constant memory regardless of file size, which is essential for large files, and it starts sending data to clients immediately instead of waiting for the whole file to load. The catch is you need to handle backpressure - if the client can't receive data fast enough, you need to pause the stream. The tricky part is error handling is more complex because errors can happen at any point in the stream, and you need to clean up properly.

---

## Q34. Designing a rate limiter in Node.js

Design a rate limiter using Redis to track request counts per user or IP - like storing a key with the user ID and incrementing a counter, setting expiration, and rejecting requests when the limit is exceeded. Use sliding window or token bucket algorithms, and consider different limits for different endpoints or user tiers.

- **Trade-offs**: Rate limiting protects your API from abuse and prevents one user from overwhelming your servers, but the catch is you need Redis or similar shared storage if you're running multiple instances, otherwise each instance tracks limits separately. The tricky part is choosing the right algorithm - sliding window is more accurate but uses more memory, token bucket is simpler but can allow bursts that might overwhelm your system.

---

## Q35. Large-scale Node.js project structure

Structure large Node.js projects by feature or domain - like organizing by modules (users, orders, payments) where each module has its own routes, controllers, services, and models. Use dependency injection, separate concerns (routing, business logic, data access), and keep shared utilities in a common folder. Consider microservices if modules are truly independent.

- **Trade-offs**: Feature-based structure makes it easier to find code and understand what each part does, and it scales better as your team grows because different people can work on different features. The catch is you need clear boundaries and shared utilities can become a dumping ground. The tricky part is deciding when to split into microservices - too early and you add complexity, too late and refactoring is painful.

---

## Q36. Connection pooling strategies

Connection pooling maintains a pool of reusable database connections instead of creating a new connection for each query - like keeping 10 connections open and reusing them, creating new ones only when the pool is exhausted. Configure pool size based on your database's max connections and your app's concurrency, and set timeouts to close idle connections.

- **Trade-offs**: Connection pooling reduces the overhead of creating connections which is expensive, and it limits the number of connections to prevent overwhelming your database. The catch is you need to size the pool correctly - too small and requests wait for available connections, too large and you waste resources or hit database limits. The tricky part is handling connection failures - you need to detect dead connections and replace them in the pool.

---

## Q37. Retry and exponential backoff

Retry with exponential backoff means waiting longer between each retry attempt - like retrying after 1 second, then 2 seconds, then 4 seconds, up to a max delay. This gives transient failures time to recover while avoiding hammering a down service. Use jitter to add randomness and prevent thundering herd problems.

- **Trade-offs**: Retries handle transient failures like network hiccups or temporary service overloads, which improves reliability, but the catch is you need to distinguish between transient and permanent failures - don't retry on 404 errors. The tricky part is setting good limits - too many retries wastes time and resources, too few and you give up on recoverable failures. Exponential backoff prevents overwhelming a recovering service, but adds latency.

---

## Q38. Idempotent API design in Node.js

Design idempotent APIs by using idempotency keys - clients send a unique key with requests, and if you've seen that key before, you return the previous response instead of processing again. Store keys in Redis with a TTL, and make sure your operations are truly idempotent - like using upsert instead of insert, or checking state before processing.

- **Trade-offs**: Idempotency prevents duplicate operations from retries or network issues, which is critical for things like payments or order creation, but the catch is you need to store idempotency keys somewhere accessible to all your instances. The tricky part is making operations truly idempotent - GET and PUT are naturally idempotent, but POST operations need careful design, and you need to handle the case where the first request is still processing when a retry comes in.

---

## Q39. JWT authentication architecture

JWT authentication works by issuing a token after login that contains user info and expiration - the client sends this token with each request, and the server validates it without needing to check a database. Use refresh tokens for long-lived sessions, store them securely, and implement token rotation for better security.

- **Trade-offs**: JWTs are stateless which makes them great for horizontal scaling since you don't need shared session storage, and they're fast because validation doesn't require database lookups. The catch is you can't revoke tokens easily until they expire, and if a token is stolen, it's valid until expiration. The tricky part is balancing security and user experience - short expiration improves security but requires frequent re-authentication, refresh tokens help but add complexity.

---

## Q40. Preventing brute-force attacks

Prevent brute-force attacks by rate limiting login attempts - like allowing 5 failed attempts per IP or email, then requiring a CAPTCHA or temporary lockout. Track attempts in Redis with expiration, use account lockouts for repeated failures, and consider progressive delays that increase with each failed attempt.

- **Trade-offs**: Rate limiting stops automated attacks effectively, but the catch is you need to balance security with user experience - too strict and legitimate users get locked out, too lenient and attacks succeed. The tricky part is distinguishing between attacks and legitimate users who forgot their password - IP-based limits can block shared networks, and account lockouts can be used for denial of service attacks.

---

## Q41. Graceful shutdown and why it's important

Graceful shutdown allows your server to finish processing current requests before shutting down - like stopping to accept new connections, waiting for existing requests to complete, closing database connections, and then exiting. This prevents data corruption, incomplete operations, and poor user experience from abrupt shutdowns.

- **Trade-offs**: Graceful shutdown prevents data loss and ensures requests complete properly, which is essential for production, but the catch is you need to set timeouts - if a request takes too long, you should force shutdown anyway. The tricky part is handling different types of work - HTTP requests, background jobs, WebSocket connections - each needs different shutdown logic, and you need to coordinate shutdown across multiple services.

---

## Q42. Logging architecture for Node.js services

Design logging by using structured logging with consistent formats - like JSON logs with timestamps, log levels, request IDs, and context. Send logs to a centralized system like ELK stack or CloudWatch, use appropriate log levels (error, warn, info, debug), and include correlation IDs to trace requests across services.

- **Trade-offs**: Centralized logging gives you visibility across all services which is essential for debugging distributed systems, but the catch is it can be expensive at scale and adds network overhead. The tricky part is balancing detail with performance - too much logging slows things down and costs money, too little and you can't debug issues. Structured logs are easier to query and analyze, but require discipline to maintain consistent formats.

---

## Q43. Handling partial failures in Node.js

Handle partial failures by using circuit breakers, timeouts, fallbacks, and bulkheads - like if a database query times out, return cached data or a default response instead of failing the entire request. Use health checks to detect failing dependencies, implement retries with backoff for transient failures, and design your system to degrade gracefully.

- **Trade-offs**: Handling partial failures keeps your system working even when dependencies are down, which improves reliability, but the catch is you need fallbacks for every dependency which adds complexity. The tricky part is deciding what to do when things fail - return stale data, show an error, or queue for later processing - each has different user experience implications. Circuit breakers help by failing fast, but you need to handle the open state gracefully.

---

## Q44. Designing Node.js + S3 upload flow

Design S3 uploads by generating pre-signed URLs on your server - clients request upload URLs, your server generates time-limited signed URLs from S3, clients upload directly to S3, then notify your server when done. For large files, use multipart uploads, and validate file types and sizes on both client and server.

- **Trade-offs**: Pre-signed URLs allow clients to upload directly to S3 which reduces load on your server and is faster, but the catch is you lose control over the upload process - you can't validate files before they're uploaded. The tricky part is handling large files - multipart uploads are more complex but necessary for files over 5GB, and you need to handle partial uploads and cleanup if uploads fail. Server-side validation after upload adds a step but provides security.

---

<div align="center">

**[← Previous: System Design Fundamentals](1%29%20System%20Design%20Fundamentals.md)** | **[Next: Database Design →](3%29%20Database%20Design.md)**

</div>

## Q45. Handling environment configs in Node.js microservices

Handle environment configs by using environment variables for secrets and configuration - like using dotenv for local development, AWS Secrets Manager or similar for production secrets, and config files for non-sensitive settings. Use different configs per environment (dev, staging, prod), validate required configs on startup, and never commit secrets to code.

- **Trade-offs**: Environment variables keep secrets out of code and make it easy to change configs without redeploying, but the catch is you need to manage them carefully - use secret management services in production, not plain environment variables. The tricky part is coordinating configs across multiple services - consider a config service or infrastructure as code, and make sure config changes don't break running services. Validation on startup catches missing configs early, but adds startup time.
