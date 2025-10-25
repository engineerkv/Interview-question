# ⚙️ Backend System Design Interview Notes (2025 Edition)

## 🟡 Section 3 — Scaling, Performance & Queues — Q61-Q95

---

### 61. 🟡 How would you design a system to handle millions of requests per second?

**🧠 Concept**

Design horizontally scalable system with load balancers, microservices, caching, and database sharding to handle massive traffic.

**💻 Example**

```javascript
// System architecture for millions of RPS
const systemDesign = {
  loadBalancers: ['ALB-1', 'ALB-2', 'ALB-3'],
  apiGateways: ['API-GW-1', 'API-GW-2'],
  microservices: {
    userService: ['instance-1', 'instance-2', 'instance-3'],
    orderService: ['instance-1', 'instance-2', 'instance-3']
  },
  caches: ['Redis-Cluster-1', 'Redis-Cluster-2'],
  databases: {
    primary: 'DB-Master',
    replicas: ['DB-Replica-1', 'DB-Replica-2', 'DB-Replica-3']
  }
};
```

**💬 Explanation + Insight**

- **Horizontal Scaling** - Add more servers to handle load
- **Load Balancing** - Distribute traffic across multiple servers
- **Caching** - Reduce database load with Redis/Memcached
- **Database Sharding** - Distribute data across multiple databases
- **Microservices** - Independent scaling of different services

---

### 62. 🟡 What is rate limiting and how can you build one?

**🧠 Concept**

Rate limiting controls request frequency per user/IP to prevent abuse and ensure fair resource usage.

**💻 Example**

```javascript
// Token bucket rate limiter
class RateLimiter {
  constructor(capacity, refillRate) {
    this.capacity = capacity;
    this.tokens = capacity;
    this.lastRefill = Date.now();
    this.refillRate = refillRate;
  }
  
  isAllowed() {
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
    const tokensToAdd = (timePassed / 1000) * this.refillRate;
    this.tokens = Math.min(this.capacity, this.tokens + tokensToAdd);
    this.lastRefill = now;
  }
}
```

**💬 Explanation + Insight**

- **Token Bucket** - Refill tokens at fixed rate
- **Sliding Window** - Track requests in time window
- **Fixed Window** - Simple but can have bursts
- **Distributed** - Use Redis for shared rate limiting
- **Use Cases** - API protection, DDoS prevention

---

### 63. 🟡 What are token bucket and leaky bucket algorithms?

**🧠 Concept**

Token bucket adds tokens at fixed rate, leaky bucket processes requests at fixed rate - both control request flow.

**💻 Example**

```javascript
// Token bucket implementation
class TokenBucket {
  constructor(capacity, refillRate) {
    this.capacity = capacity;
    this.tokens = capacity;
    this.refillRate = refillRate;
    this.lastRefill = Date.now();
  }
  
  consume(tokens = 1) {
    this.refill();
    if (this.tokens >= tokens) {
      this.tokens -= tokens;
      return true;
    }
    return false;
  }
}

// Leaky bucket implementation
class LeakyBucket {
  constructor(capacity, leakRate) {
    this.capacity = capacity;
    this.leakRate = leakRate;
    this.queue = [];
    this.lastLeak = Date.now();
  }
  
  add(request) {
    if (this.queue.length < this.capacity) {
      this.queue.push(request);
      return true;
    }
    return false;
  }
}
```

**💬 Explanation + Insight**

- **Token Bucket** - Allows bursts, refills tokens
- **Leaky Bucket** - Smooths traffic, fixed output rate
- **Burst Handling** - Token bucket allows bursts, leaky bucket doesn't
- **Use Cases** - Token bucket for APIs, leaky bucket for traffic shaping
- **Implementation** - Both can be implemented with Redis

---

### 64. 🟡 What is a circuit breaker and why is it useful?

**🧠 Concept**

Circuit breaker prevents cascading failures by stopping calls to failing services and allowing them to recover.

**💻 Example**

```javascript
class CircuitBreaker {
  constructor(threshold, timeout) {
    this.threshold = threshold;
    this.timeout = timeout;
    this.failureCount = 0;
    this.lastFailureTime = null;
    this.state = 'CLOSED'; // CLOSED, OPEN, HALF_OPEN
  }
  
  async call(fn) {
    if (this.state === 'OPEN') {
      if (Date.now() - this.lastFailureTime > this.timeout) {
        this.state = 'HALF_OPEN';
      } else {
        throw new Error('Circuit breaker is OPEN');
      }
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
    this.lastFailureTime = Date.now();
    if (this.failureCount >= this.threshold) {
      this.state = 'OPEN';
    }
  }
}
```

**💬 Explanation + Insight**

- **Three States** - Closed (normal), Open (failing), Half-open (testing)
- **Failure Threshold** - Open circuit after threshold failures
- **Timeout** - Try again after timeout period
- **Cascading Failures** - Prevents one service failure from affecting others
- **Use Cases** - Essential for microservices resilience

---

### 65. 🟡 What is retry with exponential backoff?

**🧠 Concept**

Retry failed requests with increasing delays to handle temporary failures while avoiding overwhelming failing services.

**💻 Example**

```javascript
async function retryWithBackoff(fn, maxRetries = 3, baseDelay = 1000) {
  for (let attempt = 0; attempt <= maxRetries; attempt++) {
    try {
      return await fn();
    } catch (error) {
      if (attempt === maxRetries) {
        throw error;
      }
      
      const delay = baseDelay * Math.pow(2, attempt) + Math.random() * 1000;
      await new Promise(resolve => setTimeout(resolve, delay));
    }
  }
}

// Usage
const result = await retryWithBackoff(async () => {
  return await fetch('/api/data');
});
```

**💬 Explanation + Insight**

- **Exponential Backoff** - Delay increases exponentially
- **Jitter** - Add randomness to prevent thundering herd
- **Max Retries** - Limit number of retry attempts
- **Transient Failures** - Handle temporary network issues
- **Use Cases** - API calls, database connections, external services

---

### 66. 🟡 What is load shedding and when to use it?

**🧠 Concept**

Load shedding drops requests when system is overloaded to maintain service stability and prevent complete failure.

**💻 Example**

```javascript
class LoadShedder {
  constructor(maxLoad = 0.8) {
    this.maxLoad = maxLoad;
    this.currentLoad = 0;
  }
  
  shouldShedLoad() {
    return this.currentLoad > this.maxLoad;
  }
  
  handleRequest(req, res) {
    if (this.shouldShedLoad()) {
      res.status(503).json({ error: 'Service overloaded' });
      return;
    }
    
    // Process request
    this.currentLoad += 0.1;
    // ... process request
    this.currentLoad -= 0.1;
  }
}
```

**💬 Explanation + Insight**

- **Overload Protection** - Drop requests when system is overloaded
- **Graceful Degradation** - Maintain core functionality
- **Load Monitoring** - Track system load metrics
- **Priority Handling** - Drop low-priority requests first
- **Use Cases** - High-traffic systems, resource-constrained environments

---

### 67. 🟡 How do you implement distributed caching (Redis / Memcached)?

**🧠 Concept**

Distributed caching stores data across multiple cache nodes with consistent hashing for high availability and performance.

**💻 Example**

```javascript
// Redis cluster configuration
const redis = require('redis');
const cluster = new redis.Cluster([
  { host: 'redis-1', port: 6379 },
  { host: 'redis-2', port: 6379 },
  { host: 'redis-3', port: 6379 }
]);

// Cache implementation
class DistributedCache {
  constructor(redisCluster) {
    this.redis = redisCluster;
  }
  
  async get(key) {
    try {
      const value = await this.redis.get(key);
      return value ? JSON.parse(value) : null;
    } catch (error) {
      console.error('Cache get error:', error);
      return null;
    }
  }
  
  async set(key, value, ttl = 3600) {
    try {
      await this.redis.setex(key, ttl, JSON.stringify(value));
    } catch (error) {
      console.error('Cache set error:', error);
    }
  }
}
```

**💬 Explanation + Insight**

- **Consistent Hashing** - Distribute keys across cache nodes
- **Replication** - Multiple copies for fault tolerance
- **Failover** - Automatic failover when nodes fail
- **Performance** - Sub-millisecond access times
- **Use Cases** - Session storage, database caching, API responses

---

### 68. 🟡 What is TTL and LRU cache eviction?

**🧠 Concept**

TTL (Time To Live) expires data after time, LRU (Least Recently Used) evicts least recently accessed data when cache is full.

**💻 Example**

```javascript
// TTL cache implementation
class TTLCache {
  constructor() {
    this.cache = new Map();
  }
  
  set(key, value, ttl = 3600000) {
    const expiry = Date.now() + ttl;
    this.cache.set(key, { value, expiry });
  }
  
  get(key) {
    const item = this.cache.get(key);
    if (!item) return null;
    
    if (Date.now() > item.expiry) {
      this.cache.delete(key);
      return null;
    }
    
    return item.value;
  }
}

// LRU cache implementation
class LRUCache {
  constructor(capacity) {
    this.capacity = capacity;
    this.cache = new Map();
  }
  
  get(key) {
    if (this.cache.has(key)) {
      const value = this.cache.get(key);
      this.cache.delete(key);
      this.cache.set(key, value);
      return value;
    }
    return null;
  }
  
  set(key, value) {
    if (this.cache.has(key)) {
      this.cache.delete(key);
    } else if (this.cache.size >= this.capacity) {
      const firstKey = this.cache.keys().next().value;
      this.cache.delete(firstKey);
    }
    this.cache.set(key, value);
  }
}
```

**💬 Explanation + Insight**

- **TTL** - Automatic expiration based on time
- **LRU** - Evicts least recently used items
- **Memory Management** - Prevents cache from growing indefinitely
- **Performance** - O(1) operations for both TTL and LRU
- **Use Cases** - TTL for temporary data, LRU for memory-constrained systems

---

### 69. 🟡 What is connection pooling and why does it reduce latency?

**🧠 Concept**

Connection pooling reuses database connections instead of creating new ones, reducing connection overhead and latency.

**💻 Example**

```javascript
// Connection pool configuration
const pool = new Pool({
  host: 'localhost',
  port: 5432,
  database: 'myapp',
  user: 'username',
  password: 'password',
  max: 20,        // Maximum connections
  min: 5,         // Minimum connections
  idle: 10000,    // Idle timeout
  acquire: 30000  // Acquire timeout
});

// Using connection pool
async function getUsers() {
  const client = await pool.connect();
  try {
    const result = await client.query('SELECT * FROM users');
    return result.rows;
  } finally {
    client.release(); // Return to pool
  }
}
```

**💬 Explanation + Insight**

- **Connection Reuse** - Reuse existing connections
- **Latency Reduction** - Avoid connection establishment overhead
- **Resource Management** - Limit number of connections
- **Performance** - Significant latency improvement
- **Use Cases** - High-traffic applications, database connections

---

### 70. 🟡 How do you optimize slow SQL and MongoDB queries?

**🧠 Concept**

Optimize queries by adding indexes, rewriting queries, using query hints, and analyzing execution plans.

**💻 Example**

```sql
-- Slow query
SELECT * FROM users u 
JOIN orders o ON u.id = o.user_id 
WHERE u.status = 'active' 
AND o.created_at > '2023-01-01';

-- Optimized query with indexes
CREATE INDEX idx_users_status ON users(status);
CREATE INDEX idx_orders_user_created ON orders(user_id, created_at);

-- Rewritten query
SELECT u.id, u.name, o.total 
FROM users u 
JOIN orders o ON u.id = o.user_id 
WHERE u.status = 'active' 
AND o.created_at > '2023-01-01';
```

**💬 Explanation + Insight**

- **Index Analysis** - Identify missing indexes
- **Query Rewriting** - Simplify complex queries
- **Execution Plans** - Use EXPLAIN to analyze performance
- **Selective Queries** - Use WHERE clauses to limit data
- **Use Cases** - Essential for database performance

---

### 71. 🟡 What is batching and why does it improve performance?

**🧠 Concept**

Batching groups multiple operations together, reducing network overhead and improving throughput.

**💻 Example**

```javascript
// Without batching - individual requests
async function processUsers(users) {
  for (const user of users) {
    await updateUser(user.id, user.data);
  }
}

// With batching - batch requests
async function processUsersBatch(users) {
  const batchSize = 100;
  for (let i = 0; i < users.length; i += batchSize) {
    const batch = users.slice(i, i + batchSize);
    await updateUsersBatch(batch);
  }
}

async function updateUsersBatch(users) {
  const query = 'UPDATE users SET name = $1, email = $2 WHERE id = $3';
  const values = users.map(user => [user.name, user.email, user.id]);
  await db.query(query, values);
}
```

**💬 Explanation + Insight**

- **Network Efficiency** - Reduce number of network calls
- **Database Performance** - Batch operations are faster
- **Memory Usage** - Process data in chunks
- **Error Handling** - Handle batch failures gracefully
- **Use Cases** - Bulk operations, data processing

---

### 72. 🟡 What's the difference between offset and cursor-based pagination?

**🧠 Concept**

Offset pagination uses LIMIT/OFFSET, cursor pagination uses last seen value for better performance on large datasets.

**💻 Example**

```javascript
// Offset pagination (inefficient for large datasets)
function getUsersOffset(page, limit) {
  const offset = page * limit;
  return db.query('SELECT * FROM users ORDER BY id LIMIT ? OFFSET ?', [limit, offset]);
}

// Cursor-based pagination (efficient)
function getUsersCursor(lastId, limit) {
  return db.query('SELECT * FROM users WHERE id > ? ORDER BY id LIMIT ?', [lastId, limit]);
}

// Usage
const users = await getUsersCursor(100, 20); // Get 20 users after ID 100
const nextCursor = users[users.length - 1].id;
```

**💬 Explanation + Insight**

- **Offset Pagination** - Simple but slow for large offsets
- **Cursor Pagination** - Fast regardless of position
- **Consistency** - Cursor pagination handles new records better
- **Performance** - Cursor pagination is O(log n) vs O(n)
- **Use Cases** - Cursor for large datasets, offset for small datasets

---

### 73. 🟡 How do you implement asynchronous task queues (BullMQ, Kafka, RabbitMQ)?

**🧠 Concept**

Task queues process jobs asynchronously, providing reliability, scalability, and fault tolerance for background processing.

**💻 Example**

```javascript
// BullMQ implementation
const Queue = require('bull');
const emailQueue = new Queue('email processing');

// Producer - add jobs
emailQueue.add('send-welcome-email', {
  userId: 123,
  email: 'user@example.com'
});

// Consumer - process jobs
emailQueue.process('send-welcome-email', async (job) => {
  const { userId, email } = job.data;
  await sendEmail(email, 'Welcome!');
});

// Kafka implementation
const kafka = require('kafkajs');
const producer = kafka.producer();
await producer.send({
  topic: 'user-events',
  messages: [{ value: JSON.stringify({ userId: 123, event: 'created' }) }]
});
```

**💬 Explanation + Insight**

- **Asynchronous Processing** - Non-blocking background tasks
- **Reliability** - Jobs are persisted and retried on failure
- **Scalability** - Multiple workers can process jobs
- **Error Handling** - Built-in retry and dead letter queues
- **Use Cases** - Email sending, image processing, data synchronization

---

### 74. 🟡 Kafka vs RabbitMQ vs AWS SQS — which to choose and when?

**🧠 Concept**

Kafka for high-throughput streaming, RabbitMQ for complex routing, SQS for simple queuing with AWS integration.

**💻 Example**

```javascript
// Kafka - high throughput streaming
const kafka = require('kafkajs');
const consumer = kafka.consumer({ groupId: 'my-group' });
await consumer.subscribe({ topic: 'events' });

// RabbitMQ - complex routing
const amqp = require('amqplib');
const connection = await amqp.connect('amqp://localhost');
const channel = await connection.createChannel();
await channel.assertExchange('events', 'topic');

// AWS SQS - simple queuing
const AWS = require('aws-sdk');
const sqs = new AWS.SQS();
await sqs.sendMessage({
  QueueUrl: 'https://sqs.us-east-1.amazonaws.com/123456789012/my-queue',
  MessageBody: JSON.stringify({ userId: 123 })
});
```

**💬 Explanation + Insight**

- **Kafka** - High throughput, streaming, log-based
- **RabbitMQ** - Complex routing, message patterns, AMQP
- **SQS** - Simple, managed, AWS integration
- **Use Cases** - Kafka for analytics, RabbitMQ for microservices, SQS for simple tasks
- **Performance** - Kafka fastest, SQS simplest

---

### 75. 🟡 What are dead-letter queues (DLQs) and why are they important?

**🧠 Concept**

Dead-letter queues store failed messages for analysis and reprocessing, preventing message loss and enabling error handling.

**💻 Example**

```javascript
// Dead letter queue configuration
const queue = new Queue('email-processing', {
  defaultJobOptions: {
    attempts: 3,
    backoff: {
      type: 'exponential',
      delay: 2000
    }
  }
});

// Process jobs with DLQ
queue.process('send-email', async (job) => {
  try {
    await sendEmail(job.data);
  } catch (error) {
    if (job.attemptsMade >= job.opts.attempts) {
      // Move to dead letter queue
      await queue.add('dlq-email', job.data);
    }
    throw error;
  }
});
```

**💬 Explanation + Insight**

- **Error Handling** - Store failed messages for analysis
- **Message Recovery** - Reprocess messages after fixing issues
- **Monitoring** - Track failed messages and error patterns
- **Debugging** - Analyze failed messages to identify issues
- **Use Cases** - Essential for reliable message processing

---

*This comprehensive scaling and performance section covers essential concepts including rate limiting, caching, connection pooling, query optimization, pagination, message queues, and performance monitoring for building high-performance backend systems.*