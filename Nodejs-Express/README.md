
⚙️ Node.js + Express.js Senior Developer Interview Handbook (2025 Edition)
🧠 150 Clean, Non-Overlapping Questions

🟢 1. Node.js Fundamentals (1–30)
Focus: Core architecture, event loop, streams, scaling.
What is Node.js, and why was it created?

How does Node.js differ from browser JavaScript?

What is the V8 engine, and how does Node use it?

What is event-driven architecture?

How does the Node.js event loop work?

What are the main phases of the event loop?

Difference between process.nextTick() and setImmediate().

What are microtasks and macrotasks?

What is non-blocking I/O, and why is it important?

How does Node handle many requests on one thread?

What are streams in Node.js?

What are the 4 types of streams?

What are Buffers, and how do they differ from Streams?

What is backpressure, and how do you handle it?

How does .pipe() simplify stream handling?

What is the cluster module, and when should you use it?

Difference between worker_threads and child_process.

How does Node scale across multiple CPU cores?

What is the REPL in Node.js?

Difference between CommonJS and ES Modules.

What is semantic versioning (semver)?

What is the purpose of package-lock.json?

What are peerDependencies?

What is dotenv, and how does it manage environment variables?

Difference between global variables and environment variables.

What is nvm, and how do you manage multiple Node versions?

How do you debug Node apps using VS Code or Chrome?

What does the Node.js inspector do?

How does Node handle memory management?

What are best practices for optimizing Node performance?

🟡 2. Express.js Core Concepts (31–60)
Focus: Middleware, routing, requests, sessions, and APIs.
What is Express.js, and why is it popular?

Difference between Node.js and Express.js.

What are middlewares in Express?

What are the types of middleware (app, router, built-in)?

How to write custom middleware.

What is error-handling middleware?

How does middleware chaining work?

What is express.Router() and why use it?

Difference between app.use() and app.all().

Difference between req.params, req.query, and req.body.

Difference between res.send(), res.json(), and res.end().

How do you serve static files in Express?

How to set custom HTTP headers.

How does Express handle content negotiation?

How do you handle file uploads?

What is Multer used for?

How do cookies work in Express?

What is express-session, and how does it handle sessions?

Difference between JWT-based and session-based auth.

How do you enable CORS in Express?

Difference between manual CORS headers and cors middleware.

What is Helmet, and why use it?

What is Morgan, and how does it help logging?

How to stream responses in Express.

How do you handle large file uploads efficiently?

What is res.write() and when is it used?

How to implement authentication in Express securely.

How to modularize routes and controllers properly.

How to organize middleware for scalability.

What are common anti-patterns in Express apps?

🔵 3. Advanced Node.js Concepts (61–100)
Focus: Async flow, events, streams, WebSockets, workers, and caching.
What is blocking vs non-blocking code?

Callbacks vs Promises vs async/await — pros and cons.

How to handle uncaught exceptions safely.

Difference between uncaughtException and unhandledRejection.

What are process signals like SIGINT and SIGTERM?

How to implement graceful shutdown.

What is the EventEmitter class?

How do you create custom event emitters?

Difference between EventEmitter and Pub/Sub patterns.

How is process.env used for config management?

Difference between process.argv and process.env.

What is the crypto module used for?

How to hash passwords securely in Node.

Difference between bcrypt and crypto hashing.

How to implement JWT authentication securely.

What is rate limiting, and why is it important?

How to implement rate limiting in Express (Redis or in-memory).

What are WebSockets, and how do they differ from HTTP?

Difference between WebSockets and Server-Sent Events (SSE).

How to build a real-time app using Socket.IO.

How to scale WebSockets across multiple servers.

How does Redis Pub/Sub help real-time scaling?

How to use Redis for caching and session storage.

Difference between in-memory and distributed caching.

How to integrate GraphQL with Express.

What is Apollo Server?

How to stream files using fs.createReadStream().

Difference between fs.readFile() and streams.

What is backpressure in file streaming?

What are worker_threads, and how do they improve performance?

Difference between spawn and exec in child_process.

What is clustering, and how does PM2 manage it?

Difference between PM2 and nodemon.

How does hot reloading work in Node apps?

How is concurrency handled by the event loop?

What causes memory leaks in Node, and how to fix them?

How to profile memory usage in Node (clinic.js, Chrome).

What is load testing, and how to perform it?

How to handle CPU-heavy tasks efficiently.

Best practices for large-scale Node.js app structure.

🟠 4. Security, Scaling & Deployment (101–130)
Focus: Security, performance tuning, CI/CD, and observability.
How to prevent SQL injection in Node.

How to prevent XSS and CSRF in Express.

How to store secrets securely (dotenv, Vault, AWS Secrets).

How to secure REST APIs with auth middleware.

Difference between authentication and authorization.

How to implement Role-Based Access Control (RBAC).

What are OWASP best practices for Node apps?

How to use Helmet and rate limiting for API protection.

How to monitor Node apps in production.

What is PM2, and how does it manage processes?

What’s the difference between nodemon and PM2?

How to load balance Node.js applications.

Difference between sticky sessions and JWT.

What are horizontal vs vertical scaling?

How to detect and fix memory leaks in production.

How to containerize Node apps using Docker.

How to deploy Node apps to AWS or GCP.

What is a CI/CD pipeline, and how do you set it up?

Difference between Blue-Green, Rolling, and Canary deployments.

How to handle high-traffic spikes gracefully.

How does rate limiting prevent DDoS attacks?

What is an API Gateway, and why use it?

How does NGINX act as a reverse proxy?

What are the benefits of CDNs for APIs?

What is a service mesh (e.g., Istio)?

How to achieve zero-downtime deployments.

What is chaos engineering, and why is it useful?

What are logs, metrics, and traces — and why do they matter?

What is distributed tracing (Jaeger, OpenTelemetry)?

How to set up observability for Node microservices.

🛠 5. Practical Node.js & Express.js Challenges (131–150)
Focus: Hands-on coding and architectural implementation.
Build a simple REST API using Express.

Implement a custom EventEmitter class.

Implement JWT authentication middleware.

Create a rate limiter using Redis.

Build a WebSocket chat server using Socket.IO.

Implement Redis caching for an API.

Stream large files with Node streams.

Parse and process large CSV files using streams.

Create centralized error-handling middleware.

Implement a request logging middleware.

Build a GraphQL API using Apollo Server and Express.

Create role-based access control middleware.

Implement cron jobs using node-cron.

Build a background job queue using Bull + Redis.

Implement graceful shutdown for an Express server.

Create a /health check endpoint.

Implement broadcast messaging with Socket.IO.

Implement a load balancer using round-robin logic.

Add input validation middleware with Zod or Joi.

Set up structured logging and tracing for Express requests.

✅ Final Summary (2025 Edition)
Section
Focus
Questions
🟢 Fundamentals
Event Loop, Streams, Scaling
30
🟡 Express Core
Middleware, Routing, APIs
30
🔵 Advanced Node
Async, Workers, WebSockets, Redis
40
🟠 Security & Scaling
Security, CI/CD, Cloud
30
🛠 Practical
Hands-on Implementations
20
Total
Comprehensive Node.js + Express.js Mastery
150 ✅
