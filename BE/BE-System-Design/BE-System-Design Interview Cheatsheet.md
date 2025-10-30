# 🏗️ Backend System Design Interview Cheatsheet

> **Quick reference guide for backend system design interviews**

## 📋 Table of Contents

- [System Design Fundamentals](#system-design-fundamentals)
- [Architecture Patterns](#architecture-patterns)
- [Database & Storage](#database--storage)
- [Performance & Scalability](#performance--scalability)
- [Reliability & Monitoring](#reliability--monitoring)
- [Real-World Scenarios](#real-world-scenarios)
- [Common Patterns](#common-patterns)

---

## System Design Fundamentals

### Monolithic vs Microservices
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

## Architecture Patterns

### Message Queues
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

---

## Performance & Scalability

### Rate Limiting
```javascript
// Token bucket rate limiter
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

// Sliding window rate limiter
class SlidingWindow {
  constructor(windowSize, maxRequests) {
    this.windowSize = windowSize;
    this.maxRequests = maxRequests;
    this.requests = [];
  }
  
  allowRequest() {
    const now = Date.now();
    const windowStart = now - this.windowSize;
    
    this.requests = this.requests.filter(time => time > windowStart);
    
    if (this.requests.length < this.maxRequests) {
      this.requests.push(now);
      return true;
    }
    return false;
  }
}
```

### Connection Pooling
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

### Asynchronous Processing
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
