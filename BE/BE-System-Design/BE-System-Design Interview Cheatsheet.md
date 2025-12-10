# 🏗️ Backend System Design Interview Cheatsheet

> **⏱️ Review Time: 60-75 minutes** | **Priority: ⭐⭐⭐ Critical** | Essential backend system design concepts for interviews
>
> **Coverage: Q1-Q224** (224 questions across 12 topics)

**Quick Review Checklist:**

- [ ] System Design Fundamentals (Q1-Q25)

- [ ] Communication Protocols (Q26-Q40)

- [ ] REST vs GraphQL (Q41-Q50)

- [ ] API Scaling (Q51-Q65)

- [ ] Messaging Systems (Q66-Q94)

- [ ] AWS Cloud Architecture (Q95-Q119)

- [ ] Observability (Q120-Q134)

- [ ] Database Design (Q135-Q169)

- [ ] Node.js System Design (Q170-Q189)

- [ ] Git, Docker, CI/CD, Tooling (Q190-Q209)

- [ ] Code Quality + Debugging (Q210-Q219)

- [ ] AI Tools (Q220-Q224)

---

## 📋 **Question Coverage**

- **Q1-Q25**: System Design Fundamentals

- **Q26-Q40**: Communication Protocols

- **Q41-Q50**: REST vs GraphQL

- **Q51-Q65**: API Scaling

- **Q66-Q94**: Messaging Systems

- **Q95-Q119**: AWS Cloud Architecture

- **Q120-Q134**: Observability

- **Q135-Q169**: Database Design

- **Q170-Q189**: Node.js System Design

- **Q190-Q209**: Git, Docker, CI/CD, Tooling

- **Q210-Q219**: Code Quality + Debugging

- **Q220-Q224**: AI Tools

**Total: 224 questions across 12 topics**

---

## 📋 Table of Contents

- [System Design Fundamentals](#system-design-fundamentals)

- [Communication Protocols](#communication-protocols)

- [API Design & Scaling](#api-design--scaling)

- [Messaging Systems](#messaging-systems)

- [Database & Storage](#database--storage)

- [AWS Cloud Architecture](#aws-cloud-architecture)

- [Observability](#observability)

- [Node.js System Design](#nodejs-system-design)

- [Performance & Scalability](#performance--scalability)

- [Reliability & Monitoring](#reliability--monitoring)

- [Common Patterns](#common-patterns)

---

## System Design Fundamentals

### Monolithic vs Microservices

**Definition:** Monolithic architecture runs all services in one application, while microservices split functionality into independent, deployable services that communicate via APIs.

```javascript
// Monolithic
const app = express();
app.use('/users', userRoutes);
app.use('/orders', orderRoutes);
app.use('/payments', paymentRoutes);

// Microservices
const userService = express();
userService.use('/users', userRoutes);
userService.listen(3001);

const orderService = express();
orderService.use('/orders', orderRoutes);
orderService.listen(3002);

```

### Load Balancing

**Definition:** Distributes incoming network traffic across multiple servers to ensure no single server is overwhelmed, improving availability and response times.

```javascript
// Round Robin
class RoundRobinBalancer {
  constructor(servers) {
    this.servers = servers;
    this.currentIndex = 0;
  }

  getNextServer() {
    const server = this.servers[this.currentIndex];
    this.currentIndex = (this.currentIndex + 1) % this.servers.length;
    return server;
  }
}

// Least Connections
class LeastConnectionsBalancer {
  constructor(servers) {
    this.servers = servers.map(server => ({ ...server, connections: 0 }));
  }

  getNextServer() {
    return this.servers.reduce((min, server) =>
      server.connections < min.connections ? server : min
    );
  }
}

```

### Caching Strategies

**Definition:** Multi-level caching stores frequently accessed data in faster storage layers (memory → Redis → database) to reduce latency and database load.

```javascript
// Multi-level caching
const getData = async (key) => {
  // L1: Memory cache
  let data = memoryCache.get(key);
  if (data) return data;

  // L2: Redis cache
  data = await redis.get(key);
  if (data) {
    memoryCache.set(key, data, 300);
    return data;
  }

  // L3: Database
  data = await database.get(key);
  await redis.set(key, data, 3600);
  memoryCache.set(key, data, 300);
  return data;
};

```

---

## Communication Protocols

### HTTP/1.0 vs HTTP/1.1 vs HTTP/2 vs HTTP/3

**Definition:** HTTP/1.0 requires a new connection per request; HTTP/1.1 uses persistent connections (one request per connection, but connection reuse); HTTP/2 adds multiplexing and header compression; HTTP/3 uses QUIC over UDP for faster handshakes and built-in encryption.

```javascript
// HTTP/1.1 - One request per connection
const http1 = require('http');
const req = http1.request('http://api.example.com/data', (res) => {
  res.on('data', (chunk) => console.log(chunk));
});

// HTTP/2 - Multiplexing, header compression
const http2 = require('http2');
const client = http2.connect('https://api.example.com');
const req = client.request({ ':path': '/data' });

// HTTP/3 - QUIC protocol, faster handshake
// Uses UDP instead of TCP, built-in encryption

```

### WebSockets vs SSE vs Long Polling vs Short Polling

**Definition:** WebSockets enable bidirectional real-time communication; SSE streams server-to-client events over HTTP; Long Polling keeps requests open until data is available; Short Polling repeatedly requests server at fixed intervals.

```javascript
// WebSocket - Full duplex
const io = require('socket.io')(server);
io.on('connection', (socket) => {
  socket.emit('message', 'Hello');
  socket.on('message', (data) => console.log(data));
});

// SSE - Server to client only
app.get('/events', (req, res) => {
  res.setHeader('Content-Type', 'text/event-stream');
  setInterval(() => {
    res.write(`data: ${JSON.stringify({ time: Date.now() })}\n\n`);
  }, 1000);
});

// Long Polling - Request waits for response
app.get('/poll', async (req, res) => {
  const data = await waitForData();
  res.json(data);
});

// Short Polling - Repeated requests at fixed intervals
setInterval(async () => {
  const response = await fetch('/status');
  const data = await response.json();
  updateUI(data);
}, 5000); // Poll every 5 seconds

```

### gRPC vs REST

**Definition:** REST uses JSON over HTTP for human-readable APIs; gRPC uses Protocol Buffers (binary) for efficient inter-service communication with streaming support.

```javascript
// REST - JSON over HTTP
app.get('/api/users/:id', async (req, res) => {
  const user = await getUser(req.params.id);
  res.json(user);
});

// gRPC - Protocol Buffers, binary format
// proto file defines service and messages
// Faster, more efficient for inter-service communication

```

---

## API Design & Scaling

### REST vs GraphQL

**Definition:** REST uses multiple endpoints with fixed responses; GraphQL provides a single endpoint where clients specify exactly what data they need, reducing over-fetching.

```javascript
// REST - Multiple endpoints
app.get('/users/:id', getUser);
app.get('/users/:id/posts', getUserPosts);
app.get('/users/:id/friends', getUserFriends);

// GraphQL - Single endpoint, flexible queries
const typeDefs = `
  type User {
    id: ID!
    name: String!
    posts: [Post!]!
  }
`;
const resolvers = {
  Query: {
    user: (_, { id }) => getUser(id)
  }
};

```

### Rate Limiting

**Definition:** Controls the number of requests a client can make within a time window to prevent abuse, ensure fair usage, and protect system resources.

```javascript
// Token bucket implementation
class TokenBucket {
  constructor(capacity, refillRate) {
    this.capacity = capacity;
    this.tokens = capacity;
    this.refillRate = refillRate;
    this.lastRefill = Date.now();
  }

  allowRequest() {
    this.refill();
    if (this.tokens > 0) {
      this.tokens--;
      return true;
    }
    return false;
  }

  refill() {
    const now = Date.now();
    const timePassed = now - this.lastRefill;
    const tokensToAdd = Math.floor(timePassed * this.refillRate / 1000);
    this.tokens = Math.min(this.capacity, this.tokens + tokensToAdd);
    this.lastRefill = now;
  }
}

// Express middleware
const rateLimiter = (req, res, next) => {
  const bucket = getBucketForUser(req.userId);
  if (bucket.allowRequest()) {
    next();
  } else {
    res.status(429).json({ error: 'Rate limit exceeded' });
  }
};

```

---

## Messaging Systems

### Kafka vs RabbitMQ vs SQS

**Definition:** Kafka is a distributed event streaming platform for high-throughput event logs; RabbitMQ is a message broker for task queues; SQS is AWS's managed message queue service.

```javascript
// Kafka - Event streaming
const { Kafka } = require('kafkajs');
const kafka = new Kafka({ brokers: ['localhost:9092'] });
const producer = kafka.producer();
await producer.send({
  topic: 'user-events',
  messages: [{ value: JSON.stringify(event) }]
});

// RabbitMQ - Message queue
const amqp = require('amqplib');
const connection = await amqp.connect('amqp://localhost');
const channel = await connection.createChannel();
await channel.assertQueue('tasks');
channel.sendToQueue('tasks', Buffer.from(JSON.stringify(task)));

// SQS - AWS managed queue
const AWS = require('aws-sdk');
const sqs = new AWS.SQS();
await sqs.sendMessage({
  QueueUrl: 'https://sqs.region.amazonaws.com/account/queue',
  MessageBody: JSON.stringify(message)
}).promise();

```

---

## AWS Cloud Architecture

### Message Queues

**Definition:** Asynchronous messaging systems that decouple producers and consumers, allowing services to communicate without waiting for immediate responses.

```javascript
// RabbitMQ implementation
const amqp = require('amqplib');

const publishMessage = async (queue, message) => {
  const connection = await amqp.connect('amqp://localhost');
  const channel = await connection.createChannel();

  await channel.assertQueue(queue);
  channel.sendToQueue(queue, Buffer.from(JSON.stringify(message)));

  await channel.close();
  await connection.close();
};

const consumeMessages = async (queue, handler) => {
  const connection = await amqp.connect('amqp://localhost');
  const channel = await connection.createChannel();

  await channel.assertQueue(queue);
  channel.consume(queue, (msg) => {
    if (msg) {
      handler(JSON.parse(msg.content));
      channel.ack(msg);
    }
  });
};

```

### Circuit Breaker

**Definition:** A design pattern that prevents cascading failures by stopping requests to a failing service and allowing it time to recover before retrying.

```javascript
class CircuitBreaker {
  constructor(threshold = 5, timeout = 60000) {
    this.threshold = threshold;
    this.timeout = timeout;
    this.failureCount = 0;
    this.state = 'CLOSED';
    this.nextAttempt = Date.now();
  }

  async call(fn) {
    if (this.state === 'OPEN') {
      if (Date.now() < this.nextAttempt) {
        throw new Error('Circuit breaker is OPEN');
      }
      this.state = 'HALF_OPEN';
    }

    try {
      const result = await fn();
      this.onSuccess();
      return result;
    } catch (error) {
      this.onFailure();
      throw error;
    }
  }

  onSuccess() {
    this.failureCount = 0;
    this.state = 'CLOSED';
  }

  onFailure() {
    this.failureCount++;
    if (this.failureCount >= this.threshold) {
      this.state = 'OPEN';
      this.nextAttempt = Date.now() + this.timeout;
    }
  }
}

```

### Event-Driven Architecture

**Definition:** Architecture pattern where services communicate through events, enabling loose coupling and asynchronous processing of business logic.

```javascript
class EventBus {
  constructor() {
    this.listeners = new Map();
  }

  on(event, callback) {
    if (!this.listeners.has(event)) {
      this.listeners.set(event, []);
    }
    this.listeners.get(event).push(callback);
  }

  emit(event, data) {
    if (this.listeners.has(event)) {
      this.listeners.get(event).forEach(callback => callback(data));
    }
  }
}

// Usage
const eventBus = new EventBus();
eventBus.on('user.created', (user) => {
  sendWelcomeEmail(user);
  createUserProfile(user);
});

```

---

## Database & Storage

### SQL vs NoSQL

**Definition:** SQL databases use structured schemas with ACID transactions for relational data; NoSQL databases offer flexible schemas and horizontal scaling for unstructured data.

```javascript
// SQL (PostgreSQL)
const createUser = async (userData) => {
  const query = `
    INSERT INTO users (name, email, created_at)
    VALUES ($1, $2, $3)
    RETURNING *
  `;
  return await db.query(query, [userData.name, userData.email, new Date()]);
};

// NoSQL (MongoDB)
const createUser = async (userData) => {
  return await db.collection('users').insertOne({
    name: userData.name,
    email: userData.email,
    createdAt: new Date()
  });
};

```

### Sharding

**Definition:** Horizontal partitioning of data across multiple databases to distribute load and enable scaling beyond single database limits.

```javascript
// Sharding by user ID
const getShard = (userId) => {
  const shardCount = 4;
  const shardId = userId % shardCount;
  return `shard_${shardId}`;
};

const getUser = async (userId) => {
  const shard = getShard(userId);
  const db = await connectToShard(shard);
  return await db.users.findOne({ id: userId });
};

// Range-based sharding
const getShardByRange = (userId) => {
  if (userId < 1000) return 'shard_0';
  if (userId < 5000) return 'shard_1';
  return 'shard_2';
};

```

### Read Replicas

**Definition:** Copies of the primary database that handle read queries, reducing load on the master and improving read performance and availability.

```javascript
// Read replica setup
const masterDB = await connectToMaster();
const readReplicas = await connectToReadReplicas();

const writeData = async (data) => {
  await masterDB.insert(data);
  // Replication happens automatically
};

const readData = async (query) => {
  const replica = getRandomReplica();
  return await replica.query(query);
};

```

### EC2 vs Lambda

**Definition:** EC2 provides virtual servers for long-running applications; Lambda runs code in response to events without managing servers (serverless).

```javascript
// EC2 - Long-running processes
const express = require('express');
const app = express();
app.listen(3000);

// Lambda - Event-driven, serverless
exports.handler = async (event) => {
  const result = await processEvent(event);
  return { statusCode: 200, body: JSON.stringify(result) };
};

```

### S3 Operations

**Definition:** AWS S3 provides object storage for files; pre-signed URLs allow temporary, secure access to upload/download objects without exposing credentials.

```javascript
// S3 upload
const AWS = require('aws-sdk');
const s3 = new AWS.S3();
await s3.putObject({
  Bucket: 'my-bucket',
  Key: 'file.jpg',
  Body: fileBuffer
}).promise();

// Pre-signed URL
const url = s3.getSignedUrl('putObject', {
  Bucket: 'my-bucket',
  Key: 'file.jpg',
  Expires: 3600
});

```

### DynamoDB

**Definition:** AWS's NoSQL database service with automatic scaling, single-digit millisecond latency, and key-value/document data models for high-performance applications.

```javascript
const dynamodb = new AWS.DynamoDB.DocumentClient();
await dynamodb.put({
  TableName: 'Users',
  Item: { id: '123', name: 'John', email: 'john@example.com' }
}).promise();

// Query with partition key
const result = await dynamodb.query({
  TableName: 'Users',
  KeyConditionExpression: 'id = :id',
  ExpressionAttributeValues: { ':id': '123' }
}).promise();

```

---

## Observability

### CloudWatch Metrics

**Definition:** AWS service for monitoring and collecting metrics, logs, and events from AWS resources and applications for performance tracking and alerting.

```javascript
const cloudwatch = new AWS.CloudWatch();
await cloudwatch.putMetricData({
  Namespace: 'MyApp',
  MetricData: [{
    MetricName: 'RequestCount',
    Value: 100,
    Unit: 'Count',
    Timestamp: new Date()
  }]
}).promise();

```

### Distributed Tracing

**Definition:** Tracks requests across multiple services to identify bottlenecks, latency issues, and dependencies in microservices architectures.

```javascript
const AWSXRay = require('aws-xray-sdk-core');
const AWS = AWSXRay.captureAWS(require('aws-sdk'));

// Manual segment
const segment = AWSXRay.getSegment();
const subsegment = segment.addNewSubsegment('database-query');
await database.query('SELECT * FROM users');
subsegment.close();

```

---

## Node.js System Design

### Event Loop & Concurrency

**Definition:** Node.js uses a single-threaded event loop with non-blocking I/O to handle thousands of concurrent connections efficiently; worker threads handle CPU-intensive tasks.

```javascript
// Node.js handles concurrency via event loop
// Single-threaded but non-blocking I/O
const fs = require('fs').promises;

// Non-blocking I/O
const data = await fs.readFile('file.txt');
console.log(data);

// Worker threads for CPU-intensive tasks
const { Worker } = require('worker_threads');
const worker = new Worker('./cpu-intensive-task.js');
worker.postMessage({ data: largeDataSet });

```

### Clustering

**Definition:** Creates multiple Node.js processes (one per CPU core) to utilize all available CPU cores and improve application performance and reliability.

```javascript
const cluster = require('cluster');
const os = require('os');

if (cluster.isMaster) {
  const numCPUs = os.cpus().length;
  for (let i = 0; i < numCPUs; i++) {
    cluster.fork();
  }
} else {
  const app = require('./app');
  app.listen(3000);
}

```

### Graceful Shutdown

**Definition:** Allows the application to finish processing current requests, close connections, and clean up resources before terminating, preventing data loss.

```javascript
process.on('SIGTERM', async () => {
  console.log('SIGTERM received, shutting down gracefully');
  server.close(() => {
    console.log('HTTP server closed');
    database.close(() => {
      console.log('Database closed');
      process.exit(0);
    });
  });
});

```

### Database Connection Pooling

**Definition:** Maintains a cache of database connections that can be reused, reducing connection overhead and improving application performance.

```javascript
// Connection pool setup
const { Pool } = require('pg');
const pool = new Pool({
  host: 'localhost',
  database: 'mydb',
  user: 'user',
  password: 'password',
  max: 20, // Maximum connections
  min: 5,  // Minimum connections
  idleTimeoutMillis: 30000,
  connectionTimeoutMillis: 2000
});

// Using connection pool
const getUsers = async () => {
  const client = await pool.connect();
  try {
    const result = await client.query('SELECT * FROM users');
    return result.rows;
  } finally {
    client.release();
  }
};

```

### Async Processing & Job Queues

**Definition:** Offloads time-consuming tasks to background workers via message queues, keeping API responses fast and improving user experience.

```javascript
// Message queue for async processing
const processOrder = async (orderData) => {
  const order = await Order.create(orderData);

  // Queue slow operations
  await messageQueue.publish('order.created', {
    orderId: order.id,
    userId: order.userId,
    items: order.items
  });

  return order;
};

// Background job processor
const processOrderJob = async (jobData) => {
  const { orderId, userId, items } = jobData;

  await emailService.sendConfirmation(userId, orderId);
  await inventoryService.updateStock(items);
  await invoiceService.generateInvoice(orderId);
};

```

---

## Reliability & Monitoring

### Health Checks

**Definition:** Endpoints that report application status (liveness: is it running? readiness: can it handle traffic?) for load balancers and orchestration systems.

```javascript
// Health check implementation
const healthCheck = {
  liveness: (req, res) => {
    res.json({ status: 'alive', timestamp: new Date().toISOString() });
  },

  readiness: async (req, res) => {
    const checks = {
      database: await checkDatabase(),
      redis: await checkRedis(),
      external_api: await checkExternalAPI()
    };

    const allHealthy = Object.values(checks).every(check => check.status === 'healthy');

    res.status(allHealthy ? 200 : 503).json({
      status: allHealthy ? 'ready' : 'not ready',
      checks,
      timestamp: new Date().toISOString()
    });
  }
};

```

### Monitoring

**Definition:** Collects metrics, logs, and traces to track application performance, detect issues, and trigger alerts for proactive problem resolution.

```javascript
// Metrics collection
const monitoring = {
  recordMetric: (name, value, tags = {}) => {
    metrics.histogram(name, value, tags);
  },

  log: (level, message, context = {}) => {
    logger.log(level, message, {
      timestamp: new Date().toISOString(),
      service: 'user-service',
      ...context
    });
  },

  alert: (severity, message, context = {}) => {
    alerting.send({
      severity,
      message,
      context,
      timestamp: new Date().toISOString()
    });
  }
};

```

### Fault Tolerance

**Definition:** System's ability to continue operating when components fail, using techniques like fallbacks, retries with exponential backoff, and circuit breakers.

```javascript
// Fault-tolerant service call
const callServiceWithFallback = async (serviceUrl, fallbackUrl) => {
  try {
    const response = await fetch(serviceUrl, { timeout: 5000 });
    if (response.ok) return await response.json();
    throw new Error('Service returned error');
  } catch (error) {
    console.log('Primary service failed, trying fallback');
    try {
      const response = await fetch(fallbackUrl, { timeout: 5000 });
      return await response.json();
    } catch (fallbackError) {
      throw new Error('All services failed');
    }
  }
};

// Retry with exponential backoff
const retryWithBackoff = async (fn, maxRetries = 3) => {
  for (let i = 0; i < maxRetries; i++) {
    try {
      return await fn();
    } catch (error) {
      if (i === maxRetries - 1) throw error;
      await new Promise(resolve =>
        setTimeout(resolve, Math.pow(2, i) * 1000)
      );
    }
  }
};

```

---

## Real-World Scenarios

### URL Shortener

**Definition:** Service that converts long URLs into short, shareable links using base62 encoding and stores mappings in Redis for fast lookups.

```javascript
// URL shortener service
const express = require('express');
const redis = require('redis');
const app = express();

const redisClient = redis.createClient();
const base62 = '0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz';

const generateShortCode = () => {
  let result = '';
  for (let i = 0; i < 6; i++) {
    result += base62[Math.floor(Math.random() * 62)];
  }
  return result;
};

app.post('/shorten', async (req, res) => {
  const { url } = req.body;
  const shortCode = generateShortCode();

  await redisClient.setex(shortCode, 86400, url);
  res.json({ shortUrl: `https://short.ly/${shortCode}` });
});

app.get('/:shortCode', async (req, res) => {
  const { shortCode } = req.params;
  const originalUrl = await redisClient.get(shortCode);

  if (originalUrl) {
    res.redirect(originalUrl);
  } else {
    res.status(404).json({ error: 'URL not found' });
  }
});

```

### Real-Time Chat

**Definition:** Bidirectional communication system using WebSockets for instant messaging, with Redis for message persistence and room-based message broadcasting.

```javascript
// Chat service with WebSocket
const io = require('socket.io')(server);
const redis = require('redis');

const redisClient = redis.createClient();

io.on('connection', (socket) => {
  socket.on('join_room', (roomId) => {
    socket.join(roomId);
  });

  socket.on('send_message', async (data) => {
    const { roomId, message, userId } = data;

    const messageDoc = await Message.create({
      roomId,
      userId,
      content: message,
      timestamp: new Date()
    });

    io.to(roomId).emit('new_message', messageDoc);

    await redisClient.lpush(`messages:${roomId}`, JSON.stringify(messageDoc));
  });
});

```

### E-commerce System

**Definition:** Online shopping platform handling cart management, inventory checks, payment processing, and order fulfillment with transactional integrity.

```javascript
// E-commerce service
const express = require('express');
const app = express();

app.post('/cart/add', async (req, res) => {
  const { productId, quantity, userId } = req.body;

  const product = await Product.findById(productId);
  if (product.stock < quantity) {
    return res.status(400).json({ error: 'Insufficient stock' });
  }

  await Cart.findOneAndUpdate(
    { userId },
    { $push: { items: { productId, quantity } } },
    { upsert: true }
  );

  res.json({ message: 'Item added to cart' });
});

app.post('/checkout', async (req, res) => {
  const { userId, paymentInfo } = req.body;

  const cart = await Cart.findOne({ userId });
  if (!cart.items.length) {
    return res.status(400).json({ error: 'Cart is empty' });
  }

  const payment = await processPayment(paymentInfo, cart.total);
  if (!payment.success) {
    return res.status(400).json({ error: 'Payment failed' });
  }

  const order = await Order.create({
    userId,
    items: cart.items,
    total: cart.total,
    paymentId: payment.id,
    status: 'confirmed'
  });

  await updateInventory(cart.items);
  await Cart.deleteOne({ userId });

  res.json({ orderId: order.id });
});

```

---

## Common Patterns

### Idempotency

**Definition:** Property where performing the same operation multiple times produces the same result, preventing duplicate processing in distributed systems.

```javascript
// Idempotent API endpoint
const processPayment = async (req, res) => {
  const { idempotencyKey, amount, userId } = req.body;

  const existingPayment = await Payment.findOne({ idempotencyKey });
  if (existingPayment) {
    return res.json(existingPayment);
  }

  const payment = await Payment.create({
    idempotencyKey,
    amount,
    userId,
    status: 'completed'
  });

  res.json(payment);
};

```

### Event Sourcing

**Definition:** Stores all changes as a sequence of events rather than current state, enabling audit trails, time travel, and event replay for system reconstruction.

```javascript
// Event sourcing pattern
class EventStore {
  constructor() {
    this.events = [];
  }

  append(streamId, event) {
    this.events.push({
      streamId,
      event,
      timestamp: new Date(),
      version: this.events.length + 1
    });
  }

  getEvents(streamId) {
    return this.events.filter(e => e.streamId === streamId);
  }
}

// Aggregate reconstruction
const reconstructAggregate = (events) => {
  return events.reduce((aggregate, event) => {
    return applyEvent(aggregate, event);
  }, {});
};

```

### CQRS (Command Query Responsibility Segregation)

**Definition:** Separates read and write operations into different models, allowing independent optimization of read and write performance and scalability.

```javascript
// Command side
class CommandHandler {
  async handle(command) {
    const aggregate = await this.loadAggregate(command.aggregateId);
    aggregate.execute(command);
    await this.saveAggregate(aggregate);
  }
}

// Query side
class QueryHandler {
  async handle(query) {
    return await this.readModel.find(query.criteria);
  }
}

```

---

## 🎯 Quick Tips

- **Think in systems** - Consider scalability, performance, and maintainability

- **Draw diagrams** - Visualize architecture and data flow

- **Consider trade-offs** - Every decision has pros and cons

- **Focus on user experience** - Performance and reliability matter

- **Stay current** - Keep up with modern system design trends

- **Test thoroughly** - Use automated and manual testing

- **Monitor performance** - Use real user monitoring

- **Plan for scale** - Design for growth from the start

- **Document decisions** - Explain architectural choices

- **Iterate and improve** - Continuously optimize and refactor

---

## 📚 Key Technologies

| Category | Technology | Use Case |
|----------|------------|----------|
| **Load Balancing** | Nginx, HAProxy, AWS ALB | Traffic distribution |
| **Caching** | Redis, Memcached, CDN | Performance optimization |
| **Message Queues** | Kafka, RabbitMQ, SQS | Asynchronous processing |
| **Databases** | PostgreSQL, MongoDB, DynamoDB | Data storage |
| **Monitoring** | Prometheus, Grafana, ELK | Observability |
| **Containerization** | Docker, Kubernetes | Deployment |
| **Cloud** | AWS, GCP, Azure | Infrastructure |
| **APIs** | REST, GraphQL, gRPC | Service communication |
| **Security** | OAuth, JWT, HTTPS | Authentication |
| **Testing** | Jest, Mocha, Load Testing | Quality assurance |

---

## 🔧 Common Interview Questions

### System Design Process

1. **Requirements** - Functional and non-functional

2. **Capacity** - Estimate traffic and storage

3. **API Design** - Define endpoints and data flow

4. **Database Design** - Choose and design schema

5. **High-Level Design** - Draw system architecture

6. **Detailed Design** - Deep dive into components

7. **Scaling** - Handle increased load

8. **Trade-offs** - Discuss pros and cons

### Key Metrics

- **Latency** - Response time for requests

- **Throughput** - Requests per second

- **Availability** - Uptime percentage

- **Consistency** - Data accuracy

- **Scalability** - Ability to handle growth

### Design Principles

- **Simplicity** - Start simple, add complexity gradually

- **Modularity** - Break into independent components

- **Scalability** - Design for growth

- **Reliability** - Handle failures gracefully

- **Performance** - Optimize for speed and efficiency

---

*This cheatsheet covers the most important concepts for backend system design interviews. Practice implementing these patterns and understand the underlying principles!*
