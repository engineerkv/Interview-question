# 4) Scalability, Performance & Optimization (Q31–40)

## 31) What are common bottlenecks in large systems?

Concept: Common bottlenecks include database queries, network I/O, CPU processing, and memory usage, each requiring specific optimization strategies.

Example:
```javascript
// Database bottleneck - N+1 query problem
const getUsersWithOrders = async () => {
  const users = await User.findAll();
  // N+1 problem: one query for users, N queries for orders
  for (const user of users) {
    user.orders = await Order.findAll({ where: { userId: user.id } });
  }
  return users;
};

// Optimized with eager loading
const getUsersWithOrdersOptimized = async () => {
  return await User.findAll({
    include: [{ model: Order, as: 'orders' }]
  });
};
```

Deep Insight:
- Database queries are often the primary bottleneck
- Network I/O can be optimized with connection pooling
- CPU bottlenecks require algorithm optimization
- Memory issues need proper garbage collection and caching
- Monitor and profile to identify specific bottlenecks

## 32) What are cache invalidation strategies?

Concept: Cache invalidation strategies include TTL, write-through, write-behind, and cache-aside patterns, each with different trade-offs.

Example:
```javascript
// Cache-aside pattern
const cacheService = {
  async get(key) {
    let data = await cache.get(key);
    if (!data) {
      data = await database.get(key);
      await cache.set(key, data, 3600); // TTL: 1 hour
    }
    return data;
  },
  
  async set(key, value) {
    await database.set(key, value);
    await cache.del(key); // Invalidate cache
  }
};

// Write-through pattern
const writeThroughCache = {
  async set(key, value) {
    await database.set(key, value);
    await cache.set(key, value, 3600);
  }
};
```

Deep Insight:
- TTL: Simple but can serve stale data
- Write-through: Ensures consistency but slower writes
- Write-behind: Fast writes but risk of data loss
- Cache-aside: Flexible but requires careful invalidation
- Choose based on consistency and performance requirements

## 33) How do you handle cache stampede and cache penetration?

Concept: Cache stampede is handled with locks, while cache penetration is prevented with null value caching and proper key design.

Example:
```javascript
// Cache stampede prevention
const getDataWithLock = async (key) => {
  const lockKey = `lock:${key}`;
  const lock = await redis.set(lockKey, '1', 'EX', 10, 'NX');
  
  if (lock) {
    try {
      const data = await database.get(key);
      await cache.set(key, data, 3600);
      return data;
    } finally {
      await redis.del(lockKey);
    }
  } else {
    // Wait for other process to complete
    await new Promise(resolve => setTimeout(resolve, 100));
    return await cache.get(key);
  }
};

// Cache penetration prevention
const getDataWithNullCache = async (key) => {
  let data = await cache.get(key);
  if (data === null) {
    return null; // Cached null value
  }
  if (!data) {
    data = await database.get(key);
    await cache.set(key, data || null, 300); // Cache null for 5 minutes
  }
  return data;
};
```

Deep Insight:
- Cache stampede: Multiple processes try to refresh cache simultaneously
- Cache penetration: Queries for non-existent data bypass cache
- Use distributed locks for stampede prevention
- Cache null values to prevent penetration
- Consider using Bloom filters for existence checks

## 34) What are lazy loading and eager loading?

Concept: Lazy loading loads data when needed, while eager loading loads all data upfront, each with different performance characteristics.

Example:
```javascript
// Lazy loading
class User {
  constructor(id) {
    this.id = id;
    this._orders = null;
  }
  
  async getOrders() {
    if (!this._orders) {
      this._orders = await Order.findByUserId(this.id);
    }
    return this._orders;
  }
}

// Eager loading
const getUserWithOrders = async (userId) => {
  return await User.findById(userId, {
    include: [{ model: Order, as: 'orders' }]
  });
};

// Pagination for large datasets
const getUsersPaginated = async (page, limit) => {
  const offset = (page - 1) * limit;
  return await User.findAll({
    limit,
    offset,
    order: [['createdAt', 'DESC']]
  });
};
```

Deep Insight:
- Lazy loading: Reduces initial load time and memory usage
- Eager loading: Reduces database queries but increases memory usage
- Use lazy loading for optional or large data
- Use eager loading for frequently accessed data
- Consider pagination for large datasets

## 35) How do you reduce latency in high-traffic systems?

Concept: Latency is reduced through caching, CDNs, database optimization, and asynchronous processing strategies.

Example:
```javascript
// Multi-level caching
const getData = async (key) => {
  // L1: In-memory cache
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

// Connection pooling
const pool = new Pool({
  host: 'localhost',
  database: 'mydb',
  max: 20, // Maximum connections
  idleTimeoutMillis: 30000,
  connectionTimeoutMillis: 2000
});
```

Deep Insight:
- Use multiple levels of caching
- Implement connection pooling for databases
- Use CDNs for static content
- Optimize database queries and indexes
- Consider asynchronous processing for non-critical operations

## 36) How do you implement asynchronous processing for slow operations?

Concept: Asynchronous processing uses message queues, background jobs, and event-driven patterns to handle slow operations without blocking.

Example:
```javascript
// Message queue for async processing
const processOrder = async (orderData) => {
  // Quick response to user
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
  
  // Send confirmation email
  await emailService.sendConfirmation(userId, orderId);
  
  // Update inventory
  await inventoryService.updateStock(items);
  
  // Generate invoice
  await invoiceService.generateInvoice(orderId);
};
```

Deep Insight:
- Improves user experience by providing quick responses
- Enables better resource utilization and scalability
- Requires proper error handling and retry mechanisms
- Consider job prioritization and scheduling
- Monitor queue depth and processing times

## 37) What is load shedding, and when should you use it?

Concept: Load shedding drops requests when the system is overloaded to maintain stability and prevent cascading failures.

Example:
```javascript
// Load shedding implementation
class LoadShedder {
  constructor(maxLoad = 0.8, windowSize = 60000) {
    this.maxLoad = maxLoad;
    this.windowSize = windowSize;
    this.requestCounts = [];
    this.currentLoad = 0;
  }
  
  shouldShedLoad() {
    const now = Date.now();
    this.requestCounts = this.requestCounts.filter(
      time => now - time < this.windowSize
    );
    
    this.currentLoad = this.requestCounts.length / this.windowSize;
    return this.currentLoad > this.maxLoad;
  }
  
  handleRequest(req, res, next) {
    if (this.shouldShedLoad()) {
      return res.status(503).json({ error: 'Service temporarily unavailable' });
    }
    
    this.requestCounts.push(Date.now());
    next();
  }
}
```

Deep Insight:
- Prevents system overload and cascading failures
- Should be used as a last resort when scaling isn't possible
- Consider different shedding strategies (random, priority-based)
- Monitor and alert on load shedding events
- Implement graceful degradation when possible

## 38) What is connection pooling, and why is it important?

Concept: Connection pooling reuses database connections to improve performance and resource utilization, reducing connection overhead.

Example:
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

Deep Insight:
- Reduces connection establishment overhead
- Limits resource usage and prevents connection exhaustion
- Improves performance for high-concurrency applications
- Requires proper connection management and cleanup
- Monitor pool usage and adjust size based on load

## 39) How do you use CDNs and edge caching to improve performance?

Concept: CDNs cache content at edge locations to reduce latency and improve user experience by serving content from geographically closer servers.

Example:
```javascript
// CDN integration
const express = require('express');
const app = express();

// Static assets with CDN
app.use('/static', express.static('public', {
  maxAge: '1y',
  setHeaders: (res, path) => {
    res.setHeader('Cache-Control', 'public, max-age=31536000');
  }
}));

// Dynamic content with edge caching
app.get('/api/products', (req, res) => {
  res.setHeader('Cache-Control', 'public, max-age=300');
  res.setHeader('CDN-Cache-Control', 'max-age=600');
  res.json(products);
});

// Cache invalidation
const invalidateCDN = async (path) => {
  await cdnClient.purge(path);
};
```

Deep Insight:
- Reduces latency by serving content from edge locations
- Offloads traffic from origin servers
- Improves global user experience
- Can cache both static and dynamic content
- Requires careful cache invalidation strategies

## 40) How do you measure and optimize P99 latency (tail latency)?

Concept: P99 latency is optimized by identifying and eliminating the slowest 1% of requests through monitoring, profiling, and targeted optimizations.

Example:
```javascript
// Latency monitoring
const measureLatency = (req, res, next) => {
  const start = Date.now();
  
  res.on('finish', () => {
    const duration = Date.now() - start;
    metrics.histogram('request_duration', duration, {
      method: req.method,
      route: req.route?.path,
      status: res.statusCode
    });
  });
  
  next();
};

// P99 optimization
const optimizeSlowQueries = async () => {
  const slowQueries = await database.query(`
    SELECT query, mean_time, calls
    FROM pg_stat_statements
    WHERE mean_time > 1000
    ORDER BY mean_time DESC
  `);
  
  // Add indexes for slow queries
  for (const query of slowQueries) {
    await addIndexForQuery(query);
  }
};
```

Deep Insight:
- P99 latency represents the worst 1% of user experience
- Focus on eliminating outliers and slow paths
- Use monitoring and profiling to identify bottlenecks
- Consider caching, indexing, and algorithm optimization
- Monitor and alert on P99 latency thresholds