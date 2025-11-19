# 🚀 Node.js + Express.js Interview Cheatsheet

> **⏱️ Review Time: 20-25 minutes** | **Priority: ⭐⭐⭐ Critical** | Essential Node.js and Express.js concepts for interviews
> 
> **Coverage: Q1-Q100** (100 questions across 10 topics)

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

---

## 📋 **Question Coverage**

- **Q1-Q10**: Node.js Fundamentals
- **Q11-Q20**: Modules and Project Architecture
- **Q21-Q30**: Asynchronous Patterns & Event Emitter
- **Q31-Q40**: Streams & Buffers
- **Q41-Q50**: Node.js Internals & Performance
- **Q51-Q60**: Express.js Core Concepts
- **Q61-Q70**: REST APIs & Practical Server Scenarios
- **Q71-Q80**: Authentication, Security & Encryption
- **Q81-Q90**: Performance, Optimization, Scaling & Monitoring
- **Q91-Q100**: Testing, Debugging & Deployment

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
- [Common Patterns](#common-patterns)

---

## Node.js Fundamentals

### Event Loop Phases
```javascript
// 1. Timers (setTimeout, setInterval)
// 2. Pending callbacks (I/O callbacks)
// 3. Idle, prepare (internal use)
// 4. Poll (fetch new I/O events)
// 5. Check (setImmediate callbacks)
// 6. Close callbacks (close events)
```

### Process vs Worker Threads
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
```javascript
// CommonJS
const fs = require('fs');
module.exports = { readFile: fs.readFile };

// ES Modules
import fs from 'fs';
export { readFile: fs.readFile };
```

### Module Resolution
```javascript
// Resolution order:
// 1. Core modules (fs, http, path)
// 2. Local files (./utils, ../config)
// 3. node_modules directories
// 4. package.json main field
```

### Project Structure
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
```

---

## Security & Authentication

### JWT Authentication
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
  
  jwt.verify(token, process.env.JWT_SECRET, (err, user) => {
    if (err) return res.sendStatus(403);
    req.user = user;
    next();
  });
}
```

### Password Hashing
```javascript
const bcrypt = require('bcrypt');

// Hash password
const saltRounds = 12;
const hashedPassword = await bcrypt.hash(password, saltRounds);

// Verify password
const isValid = await bcrypt.compare(password, hashedPassword);
```

### Security Headers
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
  max: 100 // limit each IP to 100 requests per windowMs
});
app.use('/api/', limiter);
```

---

## Performance & Optimization

### Caching
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

// Redis cache
const redis = require('redis');
const client = redis.createClient();

app.get('/api/users/:id', async (req, res) => {
  const userId = req.params.id;
  const cached = await client.get(`user:${userId}`);
  
  if (cached) {
    return res.json(JSON.parse(cached));
  }
  
  const user = await getUserById(userId);
  await client.setex(`user:${userId}`, 300, JSON.stringify(user));
  res.json(user);
});
```

### Database Optimization
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
```javascript
const cluster = require('cluster');
const numCPUs = require('os').cpus().length;

if (cluster.isMaster) {
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
```dockerfile
FROM node:18-alpine
WORKDIR /app
COPY package*.json ./
RUN npm ci --only=production
COPY . .
USER node
EXPOSE 3000
CMD ["npm", "start"]
```

### Environment Configuration
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
```javascript
// Global error handler
app.use((err, req, res, next) => {
  console.error(err.stack);
  res.status(500).json({
    error: 'Something went wrong!',
    message: process.env.NODE_ENV === 'development' ? err.message : 'Internal Server Error'
  });
});

// Async error handling
app.get('/api/data', async (req, res, next) => {
  try {
    const data = await fetchData();
    res.json(data);
  } catch (error) {
    next(error);
  }
});
```

### Graceful Shutdown
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
| Validation | express-validator | Input validation |
| Authentication | jsonwebtoken | JWT tokens |
| Password Hashing | bcrypt | Password hashing |
| Security | helmet | Security headers |
| CORS | cors | Cross-origin requests |
| Rate Limiting | express-rate-limit | Request limiting |
| Logging | morgan | HTTP request logging |
| Testing | jest | Testing framework |
| API Testing | supertest | HTTP testing |
| Caching | redis | In-memory database |
| Process Manager | pm2 | Production process manager |

---

*This cheatsheet covers the most important concepts for Node.js and Express.js interviews. Practice implementing these patterns and understand the underlying principles!*
