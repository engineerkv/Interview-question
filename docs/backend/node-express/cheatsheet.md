---
sidebar_label: "Cheatsheet"
sidebar_position: 100
---
# 🚀 Node.js + Express.js Interview Cheatsheet

> **Reviewed:** 2026-09 · Modernized; legacy topics are labeled.

> **⏱️ Review Time: 20-25 minutes** | **Priority: ⭐⭐⭐ Critical** | Essential Node.js and Express.js concepts for interviews
>
> **Coverage: Q1-Q103** (103 questions across 9 topics)

**Quick Review Checklist:**

- [ ] Node.js Fundamentals (Event Loop, V8, Non-blocking I/O)

- [ ] Modules & Architecture (CommonJS vs ES Modules, Project Structure)

- [ ] Asynchronous Patterns (Promises, Async/Await, Event Emitter)

- [ ] Streams & Buffers (Types, Backpressure, Piping)

- [ ] Express.js Core (Middleware, Routing, Error Handling)

- [ ] REST APIs (Validation, Pagination, File Uploads)

- [ ] Security & Authentication (JWT, OAuth, CORS, Helmet)

- [ ] Performance & Optimization (Clustering, Caching, Monitoring)

- [ ] Testing & Debugging (Jest, Supertest, Chrome DevTools)

- [ ] Deployment (Docker, CI/CD, Cloud Deployment)

- [ ] Modern Node (node:test, --watch, --env-file, permission model, Express 5)

---

## 📋 **Question Coverage**

- **Q1-Q18**: Node.js Fundamentals & Modules

- **Q19-Q28**: Asynchronous Patterns & Event Emitter

- **Q29-Q38**: Streams & Buffers

- **Q39-Q49**: Node.js Internals & Performance

- **Q50-Q59**: Express.js Core Concepts

- **Q60-Q69**: REST APIs & Practical Server Scenarios

- **Q70-Q79**: Authentication, Security & Encryption

- **Q80-Q88**: Performance, Optimization, Scaling & Monitoring

- **Q89-Q98**: Testing, Debugging & Deployment

- **Q99-Q103**: Modern Node & Express (node:test, runtime built-ins, permission model, Express 5 migration, security baseline)

---

## 📋 Table of Contents

- [Node.js Fundamentals](#nodejs-fundamentals)

- [Modules & Architecture](#modules--architecture)

- [Asynchronous Patterns](#asynchronous-patterns)

- [Streams & Buffers](#streams--buffers)

- [Express.js Core](#expressjs-core)

- [REST APIs](#rest-apis)

- [Security & Authentication](#security--authentication)

- [Performance & Optimization](#performance--optimization)

- [Testing & Deployment](#testing--deployment)

- [Modern Node.js (2026)](#modern-nodejs-2026)

- [Common Patterns](#common-patterns)

---

## Node.js Fundamentals

### Event Loop Phases

**Definition:** Node.js event loop processes callbacks in six phases: timers, pending callbacks, idle/prepare, poll, check, and close callbacks, enabling non-blocking I/O.

```javascript
// 1. Timers (setTimeout, setInterval)
// 2. Pending callbacks (I/O callbacks)
// 3. Idle, prepare (internal use)
// 4. Poll (fetch new I/O events)
// 5. Check (setImmediate callbacks)
// 6. Close callbacks (close events)

```

### Process vs Worker Threads

**Definition:** Clusters create separate processes with isolated memory; worker threads share memory within the same process, ideal for CPU-intensive tasks.

```javascript
// Clusters - separate processes
const cluster = require('cluster');
if (cluster.isMaster) {
  cluster.fork();
} else {
  require('./app.js');
}

// Worker Threads - same process
const { Worker } = require('worker_threads');
const worker = new Worker('./cpu-task.js');

```

### Memory Management

**Definition:** Node.js uses V8's garbage collector to manage heap memory; monitor RSS and heap usage to detect memory leaks and optimize performance.

```javascript
// Monitor memory usage
const usage = process.memoryUsage();
console.log({
  rss: Math.round(usage.rss / 1024 / 1024) + ' MB',
  heapUsed: Math.round(usage.heapUsed / 1024 / 1024) + ' MB'
});

// Force garbage collection (if enabled)
if (global.gc) global.gc();

```

---

## Modules & Architecture

### CommonJS vs ES Modules

**Definition:** CommonJS uses require/module.exports for synchronous loading; ES modules use import/export for static analysis and tree-shaking.

```javascript
// CommonJS (legacy default, still everywhere)
const fs = require('node:fs');
module.exports = { readFile: fs.readFile };

// ES Modules (preferred for new code; "type": "module" in package.json)
import { readFile } from 'node:fs/promises';
export { readFile };
// require(esm) works unflagged in Node 22.12+ / 20.19+ (no top-level await)

```

### Module Resolution

**Definition:** Node.js resolves modules in order: core modules, local files, node_modules, and package.json main field, enabling organized code structure.

```javascript
// Resolution order:
// 1. Core modules (fs, http, path)
// 2. Local files (./utils, ../config)
// 3. node_modules directories
// 4. package.json main field

```

### Project Structure

**Definition:** Organize code into controllers (handlers), models (data), services (business logic), middleware, routes, utils, and config for maintainability.

```

src/
  controllers/     # Route handlers
  models/         # Data models
  services/       # Business logic
  middleware/     # Custom middleware
  routes/         # Route definitions
  utils/          # Helper functions
  config/         # Configuration

```

---

## Asynchronous Patterns

### Promises

**Definition:** Promises represent eventual completion of async operations with .then() for success, .catch() for errors, and .finally() for cleanup.

```javascript
// Promise creation
const promise = new Promise((resolve, reject) => {
  setTimeout(() => resolve('Success'), 1000);
});

// Promise chaining
promise
  .then(result => console.log(result))
  .catch(error => console.error(error))
  .finally(() => console.log('Done'));

```

### Async/Await

**Definition:** Syntactic sugar over promises that makes asynchronous code look synchronous, improving readability and error handling with try/catch.

```javascript
async function fetchData() {
  try {
    const data = await fetch('/api/data');
    const result = await data.json();
    return result;
  } catch (error) {
    console.error('Error:', error);
    throw error;
  }
}

```

### Event Emitter

**Definition:** Pattern for emitting and listening to custom events, enabling decoupled communication between components using .on() and .emit().

```javascript
const EventEmitter = require('events');
class MyEmitter extends EventEmitter {}

const myEmitter = new MyEmitter();
myEmitter.on('data', (data) => {
  console.log('Received:', data);
});
myEmitter.emit('data', 'Hello World!');

```

---

## Streams & Buffers

### Stream Types

**Definition:** Streams process data in chunks: Readable (source), Writable (destination), Transform (modify), and Duplex (bidirectional) for efficient I/O.

```javascript
const { Readable, Writable, Transform } = require('stream');

// Readable stream
const readable = new Readable({
  read() { this.push('data'); }
});

// Writable stream
const writable = new Writable({
  write(chunk, encoding, callback) {
    console.log(chunk.toString());
    callback();
  }
});

// Transform stream
const transform = new Transform({
  transform(chunk, encoding, callback) {
    this.push(chunk.toString().toUpperCase());
    callback();
  }
});

```

### File Streaming

**Definition:** Process large files efficiently by reading/writing in chunks using streams, reducing memory usage and enabling real-time processing.

```javascript
const fs = require('fs');

// Copy large file efficiently
fs.createReadStream('input.txt')
  .pipe(fs.createWriteStream('output.txt'));

// With compression
const zlib = require('zlib');
fs.createReadStream('input.txt')
  .pipe(zlib.createGzip())
  .pipe(fs.createWriteStream('output.txt.gz'));

```

### Buffer Operations

**Definition:** Buffers handle binary data in Node.js; convert between encodings (UTF-8, base64, hex) and manipulate raw bytes efficiently.

```javascript
// Create buffer
const buffer = Buffer.from('Hello World', 'utf8');

// Buffer methods
buffer.toString('base64');
buffer.toString('hex');
buffer.length;
buffer.slice(0, 5);

```

---

## Express.js Core

### Basic Setup

**Definition:** Express.js minimal web framework setup with JSON/URL-encoded middleware, route handlers, and server listening on a port.

```javascript
const express = require('express');
const app = express();

// Middleware
app.use(express.json());
app.use(express.urlencoded({ extended: true }));

// Routes
app.get('/', (req, res) => {
  res.json({ message: 'Hello World!' });
});

app.listen(3000, () => {
  console.log('Server running on port 3000');
});

```

### Middleware

**Definition:** Functions that execute between request and response, enabling logging, authentication, error handling, and request modification.

```javascript
// Custom middleware
function logger(req, res, next) {
  console.log(`${req.method} ${req.url}`);
  next();
}

// Error handling middleware
app.use((err, req, res, next) => {
  console.error(err.stack);
  res.status(500).json({ error: 'Something went wrong!' });
});

// Router-level middleware
const router = express.Router();
router.use(logger);

```

### Route Parameters

**Definition:** Extract dynamic values from URL paths (:id) and query strings (?page=1) to handle variable route segments and filtering.

```javascript
// Route parameters
app.get('/users/:id', (req, res) => {
  const userId = req.params.id;
  res.json({ userId });
});

// Query parameters
app.get('/search', (req, res) => {
  const { q, page = 1, limit = 10 } = req.query;
  res.json({ query: q, page, limit });
});

```

---

## REST APIs

### HTTP Methods

**Definition:** RESTful operations: GET (read), POST (create), PUT (update/replace), DELETE (remove) following REST principles for API design.

```javascript
// GET - Read
app.get('/api/users', (req, res) => {
  res.json({ users: [] });
});

// POST - Create
app.post('/api/users', (req, res) => {
  const user = req.body;
  res.status(201).json({ user });
});

// PUT - Update (replace)
app.put('/api/users/:id', (req, res) => {
  const { id } = req.params;
  const user = req.body;
  res.json({ id, user });
});

// DELETE - Delete
app.delete('/api/users/:id', (req, res) => {
  const { id } = req.params;
  res.status(204).send();
});

```

### Status Codes

**Definition:** HTTP status codes indicate request outcome: 2xx (success), 4xx (client errors), 5xx (server errors) for proper API communication.

```javascript
// Success
res.status(200).json(data);  // OK
res.status(201).json(data);  // Created
res.status(204).send();      // No Content

// Client Errors
res.status(400).json({ error: 'Bad Request' });
res.status(401).json({ error: 'Unauthorized' });
res.status(403).json({ error: 'Forbidden' });
res.status(404).json({ error: 'Not Found' });

// Server Errors
res.status(500).json({ error: 'Internal Server Error' });

```

### Input Validation

**Definition:** Validate and sanitize user input using express-validator to prevent injection attacks, ensure data integrity, and provide clear error messages.

```javascript
const { body, validationResult } = require('express-validator');

const validateUser = [
  body('email').isEmail().normalizeEmail(),
  body('age').isInt({ min: 0, max: 120 }),
  body('name').trim().isLength({ min: 2, max: 50 }),
  (req, res, next) => {
    const errors = validationResult(req);
    if (!errors.isEmpty()) {
      return res.status(400).json({ errors: errors.array() });
    }
    next();
  }
];

// Modern schema-first alternative (types + runtime validation)
import { z } from 'zod';
const User = z.object({ email: z.string().email(), age: z.number().int().min(0).max(120) });
const parsed = User.safeParse(req.body); // parsed.success / parsed.data / parsed.error

```

---

## Security & Authentication

### JWT Authentication

**Definition:** Stateless authentication using JSON Web Tokens (JWT) containing user claims, signed with a secret, enabling secure API access without sessions.

```javascript
const jwt = require('jsonwebtoken');

// Generate token
const token = jwt.sign(
  { userId: user.id },
  process.env.JWT_SECRET,
  { expiresIn: '1h' }
);

// Verify token
function authenticateToken(req, res, next) {
  const authHeader = req.headers['authorization'];
  const token = authHeader && authHeader.split(' ')[1];

  if (!token) return res.sendStatus(401);

  // Pin the algorithm; invalid/expired token -> 401 (403 = authenticated but not allowed)
  jwt.verify(token, process.env.JWT_SECRET, { algorithms: ['HS256'] }, (err, user) => {
    if (err) return res.sendStatus(401);
    req.user = user;
    next();
  });
}

```

### Password Hashing

**Definition:** Hash passwords with bcrypt using salt rounds to prevent rainbow table attacks and ensure passwords are never stored in plain text.

```javascript
const bcrypt = require('bcrypt');

// Hash password
const saltRounds = 12;
const hashedPassword = await bcrypt.hash(password, saltRounds);

// Verify password
const isValid = await bcrypt.compare(password, hashedPassword);

```

### Security Headers

**Definition:** Use Helmet for security headers, CORS for cross-origin control, and rate limiting to protect against common web vulnerabilities and abuse.

```javascript
const helmet = require('helmet');
app.use(helmet());

// CORS
const cors = require('cors');
app.use(cors({
  origin: ['https://example.com'],
  credentials: true
}));

// Rate limiting
const rateLimit = require('express-rate-limit');
const limiter = rateLimit({
  windowMs: 15 * 60 * 1000, // 15 minutes
  limit: 100, // v7+ name for `max`; use a Redis store when running multiple instances
  standardHeaders: 'draft-7'
});
app.use('/api/', limiter);
// csurf is deprecated (2022): use SameSite cookies + Origin checks or csrf-csrf

```

---

## Performance & Optimization

### Caching

**Definition:** Store frequently accessed data in memory (Map) or Redis to reduce database queries, improve response times, and lower server load.

```javascript
// In-memory cache
const cache = new Map();
app.get('/api/data', (req, res) => {
  const cacheKey = req.originalUrl;
  if (cache.has(cacheKey)) {
    return res.json(cache.get(cacheKey));
  }

  const data = fetchData();
  cache.set(cacheKey, data);
  res.json(data);
});

// Redis cache (node-redis v4+)
const { createClient } = require('redis');
const client = createClient({ url: process.env.REDIS_URL });
await client.connect();

app.get('/api/users/:id', async (req, res) => {
  const userId = req.params.id;
  const cached = await client.get(`user:${userId}`);

  if (cached) {
    return res.json(JSON.parse(cached));
  }

  const user = await getUserById(userId);
  await client.set(`user:${userId}`, JSON.stringify(user), { EX: 300 });
  res.json(user);
});

```

### Database Optimization

**Definition:** Use connection pooling to reuse database connections, implement pagination with LIMIT/OFFSET, and optimize queries with proper indexing.

```javascript
// Connection pooling
const mysql = require('mysql2/promise');
const pool = mysql.createPool({
  host: 'localhost',
  user: 'root',
  password: 'password',
  database: 'mydb',
  connectionLimit: 10
});

// Optimized query
app.get('/api/users', async (req, res) => {
  const { page = 1, limit = 10 } = req.query;
  const offset = (page - 1) * limit;

  const [rows] = await pool.execute(
    'SELECT id, name, email FROM users WHERE active = ? LIMIT ? OFFSET ?',
    [1, limit, offset]
  );

  res.json({ users: rows });
});

```

### Clustering

**Definition:** Fork multiple Node.js processes (one per CPU core) to utilize all cores, improve performance, and increase application reliability.

```javascript
const cluster = require('cluster');
const numCPUs = require('os').availableParallelism();

// isMaster is deprecated; in containers prefer 1 process per container + more replicas
if (cluster.isPrimary) {
  for (let i = 0; i < numCPUs; i++) {
    cluster.fork();
  }

  cluster.on('exit', (worker) => {
    console.log(`Worker ${worker.process.pid} died`);
    cluster.fork();
  });
} else {
  require('./app.js');
}

```

---

## Testing & Deployment

### Unit Testing

**Definition:** Test API endpoints with Supertest and Jest to verify routes, status codes, response bodies, and error handling for reliable applications.

```javascript
const request = require('supertest');
const app = require('../app');

describe('User API', () => {
  test('GET /api/users should return users', async () => {
    const response = await request(app)
      .get('/api/users')
      .expect(200);

    expect(response.body).toHaveProperty('users');
  });

  test('POST /api/users should create user', async () => {
    const userData = { name: 'John', email: 'john@example.com' };
    const response = await request(app)
      .post('/api/users')
      .send(userData)
      .expect(201);

    expect(response.body).toHaveProperty('id');
  });
});

```

### Docker

**Definition:** Containerize applications with Docker using multi-stage builds, minimal base images, and non-root users for secure, portable deployments.

```dockerfile
FROM node:24-alpine
WORKDIR /app
COPY package*.json ./
RUN npm ci --omit=dev
COPY . .
USER node
EXPOSE 3000
# node directly (not npm start) so SIGTERM reaches the app
CMD ["node", "app.js"]

```

### Environment Configuration

**Definition:** Manage environment-specific settings (dev, staging, production) using environment variables and configuration objects for flexible deployments.

```javascript
const config = {
  development: {
    port: process.env.PORT || 3000,
    db: { host: 'localhost', port: 5432 }
  },
  production: {
    port: process.env.PORT,
    db: { host: process.env.DB_HOST, port: process.env.DB_PORT }
  }
};

const env = process.env.NODE_ENV || 'development';
module.exports = config[env];

```

---

## Common Patterns

### Error Handling

**Definition:** Implement global error handlers and try/catch blocks to gracefully handle errors, log issues, and return appropriate HTTP status codes.

```javascript
// Global error handler
app.use((err, req, res, next) => {
  console.error(err.stack);
  res.status(500).json({
    error: 'Something went wrong!',
    message: process.env.NODE_ENV === 'development' ? err.message : 'Internal Server Error'
  });
});

// Async error handling (Express 4 style)
app.get('/api/data', async (req, res, next) => {
  try {
    const data = await fetchData();
    res.json(data);
  } catch (error) {
    next(error);
  }
});

// Express 5: rejected promises go to the error handler automatically
app.get('/api/data-v5', async (req, res) => {
  res.json(await fetchData());
});

```

### Graceful Shutdown

**Definition:** Handle SIGTERM/SIGINT signals to close server connections, finish processing requests, and clean up resources before termination.

```javascript
let server;

function gracefulShutdown(signal) {
  console.log(`Received ${signal}. Starting graceful shutdown...`);

  server.close(() => {
    console.log('HTTP server closed');
    process.exit(0);
  });

  setTimeout(() => {
    console.error('Could not close connections in time');
    process.exit(1);
  }, 30000);
}

process.on('SIGTERM', () => gracefulShutdown('SIGTERM'));
process.on('SIGINT', () => gracefulShutdown('SIGINT'));

```

### Health Check

**Definition:** Endpoint that reports application status, uptime, and memory usage for monitoring, load balancers, and orchestration systems.

```javascript
app.get('/health', (req, res) => {
  const health = {
    status: 'OK',
    timestamp: new Date().toISOString(),
    uptime: process.uptime(),
    memory: process.memoryUsage()
  };

  res.json(health);
});

```

---

## Modern Node.js (2026)

**Definition:** Node 22/24 LTS built-ins replace many dependencies: `node:test`, `--watch`, `--env-file`, global `fetch`/`WebSocket`, `AbortSignal.timeout()`, `stream/promises`, and the permission model (`--permission`, stable since 23.5 / backported to 22.x). Express 5 forwards async errors automatically and uses stricter route syntax.

```bash
node --watch --env-file=.env src/server.js   # dev loop without nodemon/dotenv
node --test --watch                           # built-in test runner
node --permission --allow-fs-read=/app src/server.js
```

```javascript
import { test } from 'node:test';
import assert from 'node:assert/strict';
import { pipeline } from 'node:stream/promises';

test('adds', () => assert.equal(1 + 1, 2));

const res = await fetch(url, { signal: AbortSignal.timeout(5000) });

// Express 5 routes: named wildcard + optional segment
app.get('/files/*filepath', handler);
app.get('/users{/:id}', handler);
```

---

## 🎯 Quick Tips

- **Always use async/await** for better error handling

- **Implement proper logging** for debugging

- **Use environment variables** for configuration

- **Validate input data** to prevent security issues

- **Implement rate limiting** to prevent abuse

- **Use connection pooling** for database connections

- **Monitor memory usage** to prevent leaks

- **Test error scenarios** not just happy paths

- **Use HTTPS** in production

- **Keep dependencies updated** for security

---

## 📚 Key Libraries

| Purpose | Library | Description |
|---------|---------|-------------|
| Web Framework | Express | Minimal web framework |
| Validation | zod / express-validator | Schema validation / input validation |
| Authentication | jsonwebtoken | JWT tokens |
| Password Hashing | bcrypt | Password hashing |
| Security | helmet | Security headers |
| CORS | cors | Cross-origin requests |
| Rate Limiting | express-rate-limit | Request limiting |
| Logging | pino / morgan | Structured JSON logging / HTTP request logging |
| Testing | node:test / vitest / jest | Built-in runner / Vite-based / classic framework |
| API Testing | supertest | HTTP testing |
| Caching | redis | In-memory database |
| Process Manager | pm2 | Production process manager (legacy on containers; orchestrator handles restarts) |
| Alternative Frameworks | fastify / @nestjs/core | Schema-based, fast / opinionated TypeScript + DI |

---

*This cheatsheet covers the most important concepts for Node.js and Express.js interviews. Practice implementing these patterns and understand the underlying principles!*
