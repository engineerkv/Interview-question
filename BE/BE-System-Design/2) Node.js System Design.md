# 7. Node.js System Design (Q131–150)

---

## Q131. 🔄 How Node.js handles concurrency

Node.js handles concurrency using an event loop that processes I/O operations asynchronously - when you make a database query or file read, Node.js doesn't wait for it to finish, it registers a callback and moves on to handle other requests. The event loop checks for completed I/O operations and runs their callbacks, letting a single thread handle thousands of concurrent connections.

- **Trade-offs**: This non-blocking I/O model is super efficient for I/O-heavy workloads like APIs and web servers because one thread can handle way more requests than blocking I/O would allow. The catch is CPU-intensive tasks block the event loop and hurt performance for all requests, which is why you need worker threads or separate processes for heavy computation.

Example:

```javascript
// Non-blocking I/O - Node.js handles multiple requests concurrently
app.get('/users/:id', async (req, res) => {
  // This doesn't block - Node.js can handle other requests while waiting
  const user = await db.users.findById(req.params.id);
  const orders = await db.orders.find({ userId: user.id });
  res.json({ user, orders });
});

// While waiting for the database, Node.js can handle other requests
// This is why one thread can handle thousands of concurrent connections
```

---

## Q132. ⚙️ Node.js event loop phases

The Node.js event loop has six phases that run in order: timers (runs setTimeout/setInterval callbacks), pending callbacks (runs I/O callbacks deferred from previous iteration), idle/prepare (internal use), poll (fetches new I/O events and runs their callbacks), check (runs setImmediate callbacks), and close callbacks (runs socket close callbacks). After each phase, it runs microtasks (promises and process.nextTick) before moving to the next phase.

- **Trade-offs**: Understanding phases helps you predict when callbacks run and optimize performance, but the catch is the order can be confusing - setImmediate runs in the check phase after poll, but process.nextTick runs between every phase, which can cause unexpected ordering. The tricky part is long-running callbacks in any phase block the entire loop, so you need to keep callbacks short and defer heavy work.

Example:

```javascript
// Event loop phase execution order
console.log('1. Start');

setTimeout(() => console.log('2. Timer'), 0);
setImmediate(() => console.log('3. Immediate'));

Promise.resolve().then(() => console.log('4. Promise'));

process.nextTick(() => console.log('5. NextTick'));

console.log('6. End');

// Output order:
// 1. Start
// 6. End
// 5. NextTick (runs between every phase)
// 4. Promise (microtask)
// 2. Timer (timers phase)
// 3. Immediate (check phase, after poll)
```

---

## Q133. 🧵 When to use worker threads

Use worker threads when you have CPU-intensive tasks that would block the event loop - like image processing, data encryption, or complex calculations. Worker threads run JavaScript in parallel on separate threads with their own V8 instance, so they can do heavy computation without blocking the main thread that handles I/O.

- **Trade-offs**: Worker threads allow you to do CPU work in parallel without blocking the main thread, which is great for performance, but the catch is they have overhead - each thread has its own memory space and V8 instance, so creating too many can use a lot of memory. The tricky part is communication between threads uses message passing which adds latency, so they're not great for tasks that need frequent back-and-forth communication.

Example:

```javascript
// main.js - Main thread
const { Worker } = require('worker_threads');

function processImage(imageData) {
  return new Promise((resolve, reject) => {
    const worker = new Worker('./image-processor.js', {
      workerData: { imageData }
    });
    
    worker.on('message', resolve);
    worker.on('error', reject);
  });
}

// image-processor.js - Worker thread
const { parentPort, workerData } = require('worker_threads');

// CPU-intensive image processing
const processed = heavyImageProcessing(workerData.imageData);
parentPort.postMessage(processed);
```

---

## Q134. 💪 Handling CPU-heavy tasks in Node.js

Handle CPU-heavy tasks by offloading them to worker threads, child processes, or external services - like using worker threads for image processing, spawning child processes for heavy computations, or calling a microservice that handles the work. You can also break work into smaller chunks and use setImmediate to yield back to the event loop between chunks.

- **Trade-offs**: Offloading keeps your main thread responsive, but the catch is each approach has trade-offs - worker threads share memory but have overhead, child processes are more isolated but heavier, and external services add network latency. The tricky part is deciding which to use - worker threads for parallel JavaScript work, child processes for running other programs or when you need more isolation, and external services when you need to scale beyond one machine.

---

## Q135. 🔀 Node clustering and how it works

Node clustering creates multiple worker processes that share the same server port - the master process listens on the port and distributes incoming connections to worker processes using round-robin by default. Each worker runs your application code in its own process with its own event loop, so you can utilize multiple CPU cores.

- **Trade-offs**: Clustering allows you to use all CPU cores which improves performance for CPU-bound work, and if one worker crashes, others keep running. The catch is workers don't share memory, so you can't share in-memory state between them - you need Redis or a database for shared state. The tricky part is load balancing is simple round-robin by default, which doesn't account for worker load, so you might want a smarter load balancer in front.

Example:

```javascript
const cluster = require('cluster');
const os = require('os');

if (cluster.isMaster) {
  // Master process - create workers
  const numWorkers = os.cpus().length;
  console.log(`Master ${process.pid} starting ${numWorkers} workers`);
  
  for (let i = 0; i < numWorkers; i++) {
    cluster.fork();
  }
  
  cluster.on('exit', (worker) => {
    console.log(`Worker ${worker.process.pid} died, restarting...`);
    cluster.fork();
  });
} else {
  // Worker process - run your app
  const express = require('express');
  const app = express();
  
  app.get('/', (req, res) => {
    res.send(`Hello from worker ${process.pid}`);
  });
  
  app.listen(3000);
}
```

---

## Q136. 📈 Scaling Node.js horizontally

Scale Node.js horizontally by running multiple instances behind a load balancer - like running your app on 5 servers and using Nginx or AWS ALB to distribute traffic. Make sure your app is stateless so any instance can handle any request, use shared storage like Redis for sessions, and use a message queue for communication between instances.

- **Trade-offs**: Horizontal scaling allows you to handle way more traffic than vertical scaling and improves fault tolerance, but the catch is you need to design for it - stateless apps, shared storage, and proper load balancing. The tricky part is some things are harder to scale horizontally - like WebSocket connections need sticky sessions or a shared pub/sub system, and real-time features need careful architecture.

---

## Q137. 🔌 Designing WebSocket-based systems

Design WebSocket systems by using a message broker like Redis pub/sub to share connections across servers - when a message comes in on server A, it publishes to Redis, and all servers subscribed to that channel broadcast to their connected clients. Use connection pooling, implement reconnection logic, and handle backpressure when clients can't keep up with message rates.

- **Trade-offs**: WebSockets give you real-time bidirectional communication which is great for chat, notifications, or live updates, but the catch is they're harder to scale horizontally because connections are stateful. The tricky part is you need a pub/sub system to share messages across servers, and you have to handle connection failures, reconnections, and message ordering carefully.

Example:

```javascript
// WebSocket server with Redis pub/sub for scaling
const WebSocket = require('ws');
const redis = require('redis');

const wss = new WebSocket.Server({ port: 8080 });
const redisClient = redis.createClient();
const redisSubscriber = redis.createClient();

const clients = new Map(); // userId -> WebSocket

// Subscribe to Redis channel
redisSubscriber.subscribe('messages');

// When message received from Redis, broadcast to local clients
redisSubscriber.on('message', (channel, message) => {
  const { userId, data } = JSON.parse(message);
  const client = clients.get(userId);
  if (client && client.readyState === WebSocket.OPEN) {
    client.send(data);
  }
});

wss.on('connection', (ws, req) => {
  const userId = getUserIdFromRequest(req);
  clients.set(userId, ws);
  
  ws.on('message', (message) => {
    // Publish to Redis so other servers can broadcast
    redisClient.publish('messages', JSON.stringify({
      userId,
      data: message.toString()
    }));
  });
  
  ws.on('close', () => {
    clients.delete(userId);
  });
});
```

---

## Q138. 🌊 Streaming large files in Node.js

Stream large files using Node.js streams instead of loading the entire file into memory - like using fs.createReadStream() to read a file in chunks and pipe it to the response, or using transform streams to process data as it flows. This allows you to handle files larger than available memory without crashing.

- **Trade-offs**: Streaming uses constant memory regardless of file size, which is essential for large files, and it starts sending data to clients immediately instead of waiting for the whole file to load. The catch is you need to handle backpressure - if the client can't receive data fast enough, you need to pause the stream. The tricky part is error handling is more complex because errors can happen at any point in the stream, and you need to clean up properly.

Example:

```javascript
const fs = require('fs');
const { Transform } = require('stream');

// Stream large file without loading into memory
app.get('/download/:filename', (req, res) => {
  const fileStream = fs.createReadStream(`./files/${req.params.filename}`);
  
  // Transform stream to add processing
  const transform = new Transform({
    transform(chunk, encoding, callback) {
      // Process chunk (e.g., encrypt, compress)
      const processed = processChunk(chunk);
      callback(null, processed);
    }
  });
  
  fileStream
    .pipe(transform)
    .pipe(res)
    .on('error', (err) => {
      console.error('Stream error:', err);
      res.status(500).end();
    });
});
```

---

## Q139. 🚦 Designing a rate limiter in Node.js

Design a rate limiter using Redis to track request counts per user or IP - like storing a key with the user ID and incrementing a counter, setting expiration, and rejecting requests when the limit is exceeded. Use sliding window or token bucket algorithms, and consider different limits for different endpoints or user tiers.

- **Trade-offs**: Rate limiting protects your API from abuse and prevents one user from overwhelming your servers, but the catch is you need Redis or similar shared storage if you're running multiple instances, otherwise each instance tracks limits separately. The tricky part is choosing the right algorithm - sliding window is more accurate but uses more memory, token bucket is simpler but can allow bursts that might overwhelm your system.

Example:

```javascript
const redis = require('redis');
const client = redis.createClient();

async function rateLimit(userId, limit = 100, window = 60) {
  const key = `rate_limit:${userId}`;
  const current = await client.incr(key);
  
  if (current === 1) {
    await client.expire(key, window); // Set expiration on first request
  }
  
  if (current > limit) {
    return { allowed: false, remaining: 0 };
  }
  
  return { allowed: true, remaining: limit - current };
}

// Middleware
app.use(async (req, res, next) => {
  const userId = req.user?.id || req.ip;
  const result = await rateLimit(userId, 100, 60); // 100 req/min
  
  if (!result.allowed) {
    return res.status(429).json({ error: 'Rate limit exceeded' });
  }
  
  res.set('X-RateLimit-Remaining', result.remaining);
  next();
});
```

---

## Q140. 🏗️ Large-scale Node.js project structure

Structure large Node.js projects by feature or domain - like organizing by modules (users, orders, payments) where each module has its own routes, controllers, services, and models. Use dependency injection, separate concerns (routing, business logic, data access), and keep shared utilities in a common folder. Consider microservices if modules are truly independent.

- **Trade-offs**: Feature-based structure makes it easier to find code and understand what each part does, and it scales better as your team grows because different people can work on different features. The catch is you need clear boundaries and shared utilities can become a dumping ground. The tricky part is deciding when to split into microservices - too early and you add complexity, too late and refactoring is painful.

---

## Q141. 🏊 Connection pooling strategies

Connection pooling maintains a pool of reusable database connections instead of creating a new connection for each query - like keeping 10 connections open and reusing them, creating new ones only when the pool is exhausted. Configure pool size based on your database's max connections and your app's concurrency, and set timeouts to close idle connections.

- **Trade-offs**: Connection pooling reduces the overhead of creating connections which is expensive, and it limits the number of connections to prevent overwhelming your database. The catch is you need to size the pool correctly - too small and requests wait for available connections, too large and you waste resources or hit database limits. The tricky part is handling connection failures - you need to detect dead connections and replace them in the pool.

Example:

```javascript
const { Pool } = require('pg');

// Connection pool with configuration
const pool = new Pool({
  host: 'localhost',
  database: 'mydb',
  user: 'user',
  password: 'password',
  max: 20, // Maximum pool size
  min: 5,  // Minimum pool size
  idleTimeoutMillis: 30000, // Close idle connections after 30s
  connectionTimeoutMillis: 2000, // Timeout when acquiring connection
});

// Reuse connections from pool
async function getUsers() {
  const client = await pool.connect();
  try {
    const result = await client.query('SELECT * FROM users');
    return result.rows;
  } finally {
    client.release(); // Return connection to pool
  }
}
```

---

## Q142. 🔁 Retry and exponential backoff

Retry with exponential backoff means waiting longer between each retry attempt - like retrying after 1 second, then 2 seconds, then 4 seconds, up to a max delay. This gives transient failures time to recover while avoiding hammering a down service. Use jitter to add randomness and prevent thundering herd problems.

- **Trade-offs**: Retries handle transient failures like network hiccups or temporary service overloads, which improves reliability, but the catch is you need to distinguish between transient and permanent failures - don't retry on 404 errors. The tricky part is setting good limits - too many retries wastes time and resources, too few and you give up on recoverable failures. Exponential backoff prevents overwhelming a recovering service, but adds latency.

Example:

```javascript
async function retryWithBackoff(fn, maxRetries = 3, baseDelay = 1000) {
  for (let attempt = 0; attempt < maxRetries; attempt++) {
    try {
      return await fn();
    } catch (error) {
      // Don't retry on permanent failures
      if (error.status === 404 || error.status === 400) {
        throw error;
      }
      
      if (attempt === maxRetries - 1) throw error;
      
      // Exponential backoff with jitter
      const delay = baseDelay * Math.pow(2, attempt);
      const jitter = Math.random() * 0.3 * delay; // 30% jitter
      await sleep(delay + jitter);
    }
  }
}

// Usage
const result = await retryWithBackoff(
  () => fetch('https://api.example.com/data'),
  3,
  1000 // Start with 1 second
);
```

---

## Q143. 🔑 Idempotent API design in Node.js

Design idempotent APIs by using idempotency keys - clients send a unique key with requests, and if you've seen that key before, you return the previous response instead of processing again. Store keys in Redis with a TTL, and make sure your operations are truly idempotent - like using upsert instead of insert, or checking state before processing.

- **Trade-offs**: Idempotency prevents duplicate operations from retries or network issues, which is critical for things like payments or order creation, but the catch is you need to store idempotency keys somewhere accessible to all your instances. The tricky part is making operations truly idempotent - GET and PUT are naturally idempotent, but POST operations need careful design, and you need to handle the case where the first request is still processing when a retry comes in.

Example:

```javascript
const redis = require('redis');
const client = redis.createClient();

async function handleIdempotentRequest(req, res, next) {
  const idempotencyKey = req.headers['idempotency-key'];
  if (!idempotencyKey) {
    return res.status(400).json({ error: 'Missing idempotency-key header' });
  }
  
  // Check if we've seen this key
  const cached = await client.get(`idempotency:${idempotencyKey}`);
  if (cached) {
    return res.json(JSON.parse(cached)); // Return previous response
  }
  
  // Store key to prevent duplicate processing
  await client.setex(`idempotency:${idempotencyKey}`, 3600, 'processing');
  
  // Process request and store response
  const originalJson = res.json.bind(res);
  res.json = function(data) {
    client.setex(`idempotency:${idempotencyKey}`, 3600, JSON.stringify(data));
    return originalJson(data);
  };
  
  next();
}

// Usage
app.post('/orders', handleIdempotentRequest, async (req, res) => {
  // Use upsert to make operation idempotent
  const order = await db.orders.findOneAndUpdate(
    { idempotencyKey: req.headers['idempotency-key'] },
    { $setOnInsert: req.body },
    { upsert: true, new: true }
  );
  res.json(order);
});
```

---

## Q144. 🔐 JWT authentication architecture

JWT authentication works by issuing a token after login that contains user info and expiration - the client sends this token with each request, and the server validates it without needing to check a database. Use refresh tokens for long-lived sessions, store them securely, and implement token rotation for better security.

- **Trade-offs**: JWTs are stateless which makes them great for horizontal scaling since you don't need shared session storage, and they're fast because validation doesn't require database lookups. The catch is you can't revoke tokens easily until they expire, and if a token is stolen, it's valid until expiration. The tricky part is balancing security and user experience - short expiration improves security but requires frequent re-authentication, refresh tokens help but add complexity.

Example:

```javascript
const jwt = require('jsonwebtoken');
const bcrypt = require('bcrypt');

// Login - issue access and refresh tokens
app.post('/login', async (req, res) => {
  const { email, password } = req.body;
  const user = await db.users.findOne({ email });
  
  if (!user || !await bcrypt.compare(password, user.password)) {
    return res.status(401).json({ error: 'Invalid credentials' });
  }
  
  // Short-lived access token
  const accessToken = jwt.sign(
    { userId: user.id, email: user.email },
    process.env.JWT_SECRET,
    { expiresIn: '15m' }
  );
  
  // Long-lived refresh token (stored in database)
  const refreshToken = jwt.sign(
    { userId: user.id },
    process.env.REFRESH_SECRET,
    { expiresIn: '7d' }
  );
  
  await db.refreshTokens.insertOne({ userId: user.id, token: refreshToken });
  
  res.json({ accessToken, refreshToken });
});

// Middleware to verify JWT
function authenticateToken(req, res, next) {
  const token = req.headers['authorization']?.split(' ')[1];
  if (!token) return res.status(401).json({ error: 'No token' });
  
  jwt.verify(token, process.env.JWT_SECRET, (err, user) => {
    if (err) return res.status(403).json({ error: 'Invalid token' });
    req.user = user;
    next();
  });
}
```

---

## Q145. 🛡️ Preventing brute-force attacks

Prevent brute-force attacks by rate limiting login attempts - like allowing 5 failed attempts per IP or email, then requiring a CAPTCHA or temporary lockout. Track attempts in Redis with expiration, use account lockouts for repeated failures, and consider progressive delays that increase with each failed attempt.

- **Trade-offs**: Rate limiting stops automated attacks effectively, but the catch is you need to balance security with user experience - too strict and legitimate users get locked out, too lenient and attacks succeed. The tricky part is distinguishing between attacks and legitimate users who forgot their password - IP-based limits can block shared networks, and account lockouts can be used for denial of service attacks.

Example:

```javascript
const redis = require('redis');
const client = redis.createClient();

async function checkBruteForce(email, ip) {
  const emailKey = `login_attempts:email:${email}`;
  const ipKey = `login_attempts:ip:${ip}`;
  
  const emailAttempts = await client.incr(emailKey);
  const ipAttempts = await client.incr(ipKey);
  
  if (emailAttempts === 1) await client.expire(emailKey, 900); // 15 min
  if (ipAttempts === 1) await client.expire(ipKey, 900);
  
  // Lock account after 5 failed attempts
  if (emailAttempts >= 5) {
    await client.setex(`locked:${email}`, 3600, '1'); // Lock for 1 hour
    return { allowed: false, reason: 'account_locked' };
  }
  
  // Progressive delay after 3 attempts
  if (emailAttempts >= 3) {
    const delay = Math.min(emailAttempts * 1000, 10000); // Max 10s
    await sleep(delay);
  }
  
  return { allowed: true, attempts: emailAttempts };
}

app.post('/login', async (req, res) => {
  const { email, password } = req.body;
  const ip = req.ip;
  
  // Check if account is locked
  const locked = await client.get(`locked:${email}`);
  if (locked) {
    return res.status(429).json({ error: 'Account temporarily locked' });
  }
  
  const check = await checkBruteForce(email, ip);
  if (!check.allowed) {
    return res.status(429).json({ error: 'Too many attempts' });
  }
  
  // ... login logic ...
  
  // Reset attempts on successful login
  await client.del(`login_attempts:email:${email}`);
});
```

---

## Q146. 🛑 Graceful shutdown and why it's important

Graceful shutdown allows your server to finish processing current requests before shutting down - like stopping to accept new connections, waiting for existing requests to complete, closing database connections, and then exiting. This prevents data corruption, incomplete operations, and poor user experience from abrupt shutdowns.

- **Trade-offs**: Graceful shutdown prevents data loss and ensures requests complete properly, which is essential for production, but the catch is you need to set timeouts - if a request takes too long, you should force shutdown anyway. The tricky part is handling different types of work - HTTP requests, background jobs, WebSocket connections - each needs different shutdown logic, and you need to coordinate shutdown across multiple services.

Example:

```javascript
const express = require('express');
const app = express();

let server;
let isShuttingDown = false;

// Graceful shutdown handler
function gracefulShutdown(signal) {
  console.log(`Received ${signal}, starting graceful shutdown...`);
  isShuttingDown = true;
  
  // Stop accepting new connections
  server.close(() => {
    console.log('HTTP server closed');
    
    // Close database connections
    db.close(() => {
      console.log('Database connections closed');
      
      // Close Redis connections
      redisClient.quit(() => {
        console.log('Redis connections closed');
        process.exit(0);
      });
    });
  });
  
  // Force shutdown after timeout
  setTimeout(() => {
    console.error('Forced shutdown after timeout');
    process.exit(1);
  }, 10000); // 10 second timeout
}

// Middleware to reject new requests during shutdown
app.use((req, res, next) => {
  if (isShuttingDown) {
    res.status(503).json({ error: 'Server is shutting down' });
    return;
  }
  next();
});

server = app.listen(3000, () => {
  console.log('Server started');
});

process.on('SIGTERM', () => gracefulShutdown('SIGTERM'));
process.on('SIGINT', () => gracefulShutdown('SIGINT'));
```

---

## Q147. 📝 Logging architecture for Node.js services

Design logging by using structured logging with consistent formats - like JSON logs with timestamps, log levels, request IDs, and context. Send logs to a centralized system like ELK stack or CloudWatch, use appropriate log levels (error, warn, info, debug), and include correlation IDs to trace requests across services.

- **Trade-offs**: Centralized logging gives you visibility across all services which is essential for debugging distributed systems, but the catch is it can be expensive at scale and adds network overhead. The tricky part is balancing detail with performance - too much logging slows things down and costs money, too little and you can't debug issues. Structured logs are easier to query and analyze, but require discipline to maintain consistent formats.

Example:

```javascript
const winston = require('winston');
const { v4: uuidv4 } = require('uuid');

// Structured logger with correlation IDs
const logger = winston.createLogger({
  format: winston.format.combine(
    winston.format.timestamp(),
    winston.format.json()
  ),
  transports: [
    new winston.transports.Console(),
    new winston.transports.File({ filename: 'error.log', level: 'error' })
  ]
});

// Middleware to add correlation ID
function correlationIdMiddleware(req, res, next) {
  req.correlationId = req.headers['x-correlation-id'] || uuidv4();
  res.setHeader('x-correlation-id', req.correlationId);
  next();
}

// Logging helper
function log(level, message, context = {}) {
  logger[level]({
    message,
    correlationId: context.correlationId,
    userId: context.userId,
    ...context
  });
}

// Usage
app.use(correlationIdMiddleware);
app.get('/users/:id', async (req, res) => {
  log('info', 'Fetching user', { 
    correlationId: req.correlationId, 
    userId: req.params.id 
  });
  
  try {
    const user = await db.users.findById(req.params.id);
    log('info', 'User fetched', { correlationId: req.correlationId });
    res.json(user);
  } catch (error) {
    log('error', 'Failed to fetch user', { 
      correlationId: req.correlationId, 
      error: error.message 
    });
    res.status(500).json({ error: 'Internal server error' });
  }
});
```

---

## Q148. 🛠️ Handling partial failures in Node.js

Handle partial failures by using circuit breakers, timeouts, fallbacks, and bulkheads - like if a database query times out, return cached data or a default response instead of failing the entire request. Use health checks to detect failing dependencies, implement retries with backoff for transient failures, and design your system to degrade gracefully.

- **Trade-offs**: Handling partial failures keeps your system working even when dependencies are down, which improves reliability, but the catch is you need fallbacks for every dependency which adds complexity. The tricky part is deciding what to do when things fail - return stale data, show an error, or queue for later processing - each has different user experience implications. Circuit breakers help by failing fast, but you need to handle the open state gracefully.

---

## Q149. ☁️ Designing Node.js + S3 upload flow

Design S3 uploads by generating pre-signed URLs on your server - clients request upload URLs, your server generates time-limited signed URLs from S3, clients upload directly to S3, then notify your server when done. For large files, use multipart uploads, and validate file types and sizes on both client and server.

- **Trade-offs**: Pre-signed URLs allow clients to upload directly to S3 which reduces load on your server and is faster, but the catch is you lose control over the upload process - you can't validate files before they're uploaded. The tricky part is handling large files - multipart uploads are more complex but necessary for files over 5GB, and you need to handle partial uploads and cleanup if uploads fail. Server-side validation after upload adds a step but provides security.

Example:

```javascript
const AWS = require('aws-sdk');
const s3 = new AWS.S3();

// Generate pre-signed URL for upload
app.post('/upload/request', authenticateToken, async (req, res) => {
  const { filename, fileType, fileSize } = req.body;
  
  // Validate file type and size
  const allowedTypes = ['image/jpeg', 'image/png', 'application/pdf'];
  if (!allowedTypes.includes(fileType)) {
    return res.status(400).json({ error: 'Invalid file type' });
  }
  
  if (fileSize > 10 * 1024 * 1024) { // 10MB limit
    return res.status(400).json({ error: 'File too large' });
  }
  
  const key = `uploads/${req.user.userId}/${Date.now()}-${filename}`;
  
  const params = {
    Bucket: 'my-bucket',
    Key: key,
    ContentType: fileType,
    Expires: 3600, // 1 hour
  };
  
  const uploadUrl = s3.getSignedUrl('putObject', params);
  
  res.json({ uploadUrl, key });
});

// Confirm upload completion
app.post('/upload/confirm', authenticateToken, async (req, res) => {
  const { key } = req.body;
  
  // Verify file exists in S3
  try {
    await s3.headObject({ Bucket: 'my-bucket', Key: key }).promise();
    
    // Store file metadata in database
    await db.files.insertOne({
      userId: req.user.userId,
      key,
      uploadedAt: new Date()
    });
    
    res.json({ success: true });
  } catch (error) {
    res.status(404).json({ error: 'File not found' });
  }
});
```

---

## Q150. ⚙️ Handling environment configs in Node.js microservices

Handle environment configs by using environment variables for secrets and configuration - like using dotenv for local development, AWS Secrets Manager or similar for production secrets, and config files for non-sensitive settings. Use different configs per environment (dev, staging, prod), validate required configs on startup, and never commit secrets to code.

- **Trade-offs**: Environment variables keep secrets out of code and make it easy to change configs without redeploying, but the catch is you need to manage them carefully - use secret management services in production, not plain environment variables. The tricky part is coordinating configs across multiple services - consider a config service or infrastructure as code, and make sure config changes don't break running services. Validation on startup catches missing configs early, but adds startup time.

Example:

```javascript
require('dotenv').config(); // Load .env in development
const AWS = require('aws-sdk');

// Config validation
const requiredEnvVars = [
  'DATABASE_URL',
  'REDIS_URL',
  'JWT_SECRET',
  'AWS_REGION'
];

function validateConfig() {
  const missing = requiredEnvVars.filter(key => !process.env[key]);
  if (missing.length > 0) {
    throw new Error(`Missing required environment variables: ${missing.join(', ')}`);
  }
}

// Load secrets from AWS Secrets Manager in production
async function loadSecrets() {
  if (process.env.NODE_ENV === 'production') {
    const secretsManager = new AWS.SecretsManager();
    const secret = await secretsManager.getSecretValue({
      SecretId: process.env.SECRET_NAME
    }).promise();
    
    const secrets = JSON.parse(secret.SecretString);
    Object.assign(process.env, secrets);
  }
}

// Config object
const config = {
  env: process.env.NODE_ENV || 'development',
  port: parseInt(process.env.PORT || '3000'),
  database: {
    url: process.env.DATABASE_URL,
    poolSize: parseInt(process.env.DB_POOL_SIZE || '10')
  },
  redis: {
    url: process.env.REDIS_URL
  },
  jwt: {
    secret: process.env.JWT_SECRET,
    expiresIn: process.env.JWT_EXPIRES_IN || '15m'
  }
};

// Initialize
async function init() {
  await loadSecrets();
  validateConfig();
  console.log('Configuration loaded successfully');
}

init().catch(console.error);
```
