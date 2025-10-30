# 9) Performance, Optimization, Scaling & Monitoring (Q81–90)

## 81) What are common Node.js performance bottlenecks, and how can they be fixed?

Concept: Common bottlenecks include blocking I/O operations, memory leaks, inefficient algorithms, and event loop blocking, which can be addressed through proper async patterns and optimization techniques.

Example:
```javascript
// Bad: Blocking I/O
app.get('/data', (req, res) => {
  const data = fs.readFileSync('large-file.txt'); // Blocks event loop
  res.json({ data });
});

// Good: Non-blocking I/O
app.get('/data', (req, res) => {
  fs.readFile('large-file.txt', (err, data) => {
    if (err) return res.status(500).json({ error: err.message });
    res.json({ data });
  });
});

// Better: Streaming
app.get('/data', (req, res) => {
  const stream = fs.createReadStream('large-file.txt');
  stream.pipe(res);
});
```

Deep Insight:
- Avoid synchronous operations in request handlers
- Use streaming for large data processing
- Implement proper error handling
- Monitor event loop lag
- Profile CPU and memory usage regularly

## 82) How do you optimize Express middleware performance (limit heavy middleware, compression, caching)?

Concept: Optimize middleware by reducing heavy operations, implementing compression, caching, and ordering middleware efficiently to minimize request processing time.

Example:
```javascript
const compression = require('compression');
const helmet = require('helmet');

// Order middleware efficiently
app.use(helmet()); // Security headers first
app.use(compression()); // Compression early
app.use(express.json({ limit: '10mb' })); // Body parsing

// Conditional heavy middleware
app.use('/api', (req, res, next) => {
  if (req.path.startsWith('/admin')) {
    return heavyAuthMiddleware(req, res, next);
  }
  next();
});

// Caching middleware
const cache = new Map();
app.use('/api/data', (req, res, next) => {
  const cacheKey = req.originalUrl;
  if (cache.has(cacheKey)) {
    return res.json(cache.get(cacheKey));
  }
  next();
});
```

Deep Insight:
- Order middleware by frequency of use
- Use compression for text responses
- Implement caching for expensive operations
- Avoid heavy middleware on all routes
- Monitor middleware execution time

## 83) How do you optimize database queries and prevent blocking in Node.js?

Concept: Optimize database performance by using connection pooling, query optimization, indexing, and async database operations to prevent blocking the event loop.

Example:
```javascript
const mysql = require('mysql2/promise');

// Connection pool
const pool = mysql.createPool({
  host: 'localhost',
  user: 'root',
  password: 'password',
  database: 'mydb',
  connectionLimit: 10,
  acquireTimeout: 60000,
  timeout: 60000
});

// Optimized query with connection pooling
app.get('/api/users', async (req, res) => {
  try {
    const connection = await pool.getConnection();
    const [rows] = await connection.execute(
      'SELECT id, name, email FROM users WHERE active = ? LIMIT ?',
      [1, 100]
    );
    connection.release();
    res.json(rows);
  } catch (error) {
    res.status(500).json({ error: error.message });
  }
});
```

Deep Insight:
- Use connection pooling for database connections
- Optimize queries with proper indexing
- Use prepared statements to prevent SQL injection
- Implement query caching for frequently accessed data
- Monitor database performance and slow queries

## 84) What is PM2, and how does it help manage and optimize production processes?

Concept: PM2 is a process manager for Node.js applications that provides clustering, monitoring, logging, and automatic restarts for production deployments.

Example:
```javascript
// PM2 ecosystem file (ecosystem.config.js)
module.exports = {
  apps: [{
    name: 'my-app',
    script: './app.js',
    instances: 'max',
    exec_mode: 'cluster',
    env: {
      NODE_ENV: 'production',
      PORT: 3000
    },
    env_production: {
      NODE_ENV: 'production',
      PORT: 3000
    },
    max_memory_restart: '1G',
    error_file: './logs/err.log',
    out_file: './logs/out.log',
    log_file: './logs/combined.log',
    time: true
  }]
};
```

Deep Insight:
- Provides process clustering and load balancing
- Automatic restarts on crashes
- Built-in monitoring and logging
- Zero-downtime deployments
- Memory and CPU monitoring

## 85) How do you scale a Node.js application horizontally (Cluster, Load Balancer, Containers)?

Concept: Horizontal scaling involves running multiple instances of the application across different processes, machines, or containers, with load balancing to distribute requests.

Example:
```javascript
const cluster = require('cluster');
const numCPUs = require('os').cpus().length;

if (cluster.isMaster) {
  console.log(`Master ${process.pid} is running`);
  
  // Fork workers
  for (let i = 0; i < numCPUs; i++) {
    cluster.fork();
  }
  
  cluster.on('exit', (worker, code, signal) => {
    console.log(`Worker ${worker.process.pid} died`);
    cluster.fork(); // Restart worker
  });
} else {
  // Worker processes
  const express = require('express');
  const app = express();
  
  app.get('/', (req, res) => {
    res.json({ 
      message: 'Hello World!', 
      pid: process.pid 
    });
  });
  
  app.listen(3000, () => {
    console.log(`Worker ${process.pid} started`);
  });
}
```

Deep Insight:
- Use clustering for multi-core utilization
- Implement load balancing for multiple servers
- Use containers (Docker) for consistent deployments
- Consider microservices architecture
- Implement health checks and monitoring

## 86) How do you implement in-memory and distributed caching (Redis, LRU)?

Concept: Caching stores frequently accessed data in fast storage (memory or Redis) to reduce database load and improve response times.

Example:
```javascript
const redis = require('redis');
const client = redis.createClient();

// In-memory LRU cache
const LRU = require('lru-cache');
const cache = new LRU({ max: 100, ttl: 1000 * 60 * 5 }); // 5 minutes

// Redis caching
app.get('/api/users/:id', async (req, res) => {
  const userId = req.params.id;
  
  // Check cache first
  const cached = await client.get(`user:${userId}`);
  if (cached) {
    return res.json(JSON.parse(cached));
  }
  
  // Fetch from database
  const user = await getUserById(userId);
  
  // Cache for 5 minutes
  await client.setex(`user:${userId}`, 300, JSON.stringify(user));
  
  res.json(user);
});

// In-memory caching
app.get('/api/stats', (req, res) => {
  const cacheKey = 'stats';
  let stats = cache.get(cacheKey);
  
  if (!stats) {
    stats = calculateStats();
    cache.set(cacheKey, stats);
  }
  
  res.json(stats);
});
```

Deep Insight:
- Use Redis for distributed caching
- Implement cache invalidation strategies
- Consider cache warming for critical data
- Monitor cache hit rates
- Use appropriate TTL values

## 87) What are effective techniques for optimizing API response time?

Concept: Optimize API response times through caching, database optimization, compression, CDN usage, and efficient data processing.

Example:
```javascript
const compression = require('compression');
const rateLimit = require('express-rate-limit');

// Enable compression
app.use(compression());

// Rate limiting
const limiter = rateLimit({
  windowMs: 15 * 60 * 1000, // 15 minutes
  max: 100 // limit each IP to 100 requests per windowMs
});
app.use('/api/', limiter);

// Optimized API endpoint
app.get('/api/users', async (req, res) => {
  const { page = 1, limit = 10 } = req.query;
  
  // Use database pagination
  const users = await User.find()
    .select('id name email') // Only select needed fields
    .limit(limit * 1)
    .skip((page - 1) * limit)
    .lean(); // Return plain objects for better performance
  
  res.json({
    users,
    pagination: { page, limit, total: await User.countDocuments() }
  });
});
```

Deep Insight:
- Use database pagination instead of loading all data
- Select only necessary fields
- Implement proper indexing
- Use compression for text responses
- Consider CDN for static assets

## 88) How do you use monitoring tools like New Relic, Sentry, or Datadog?

Concept: Monitoring tools provide real-time insights into application performance, errors, and user experience, enabling proactive issue detection and resolution.

Example:
```javascript
// New Relic
const newrelic = require('newrelic');

// Custom metrics
app.get('/api/users', (req, res) => {
  newrelic.recordMetric('Custom/UsersEndpoint', 1);
  // ... endpoint logic
});

// Sentry error tracking
const Sentry = require('@sentry/node');
Sentry.init({ dsn: process.env.SENTRY_DSN });

app.use(Sentry.requestHandler());
app.use(Sentry.errorHandler());

// Custom error reporting
app.get('/api/data', async (req, res) => {
  try {
    const data = await fetchData();
    res.json(data);
  } catch (error) {
    Sentry.captureException(error);
    res.status(500).json({ error: 'Internal server error' });
  }
});
```

Deep Insight:
- Monitor key performance metrics
- Set up alerts for critical issues
- Track user experience metrics
- Monitor database and external service performance
- Use distributed tracing for microservices

## 89) How do you identify and fix memory leaks (Heap snapshots, Node --inspect)?

Concept: Memory leaks occur when objects are not properly garbage collected, identified through heap snapshots and profiling tools.

Example:
```javascript
// Memory leak example
const leakyArray = [];
setInterval(() => {
  leakyArray.push(new Array(1000).fill('leak'));
}, 1000);

// Memory monitoring
setInterval(() => {
  const usage = process.memoryUsage();
  console.log('Memory usage:', {
    rss: Math.round(usage.rss / 1024 / 1024) + ' MB',
    heapTotal: Math.round(usage.heapTotal / 1024 / 1024) + ' MB',
    heapUsed: Math.round(usage.heapUsed / 1024 / 1024) + ' MB'
  });
}, 5000);

// Fix memory leak
let intervalId;
function startProcess() {
  intervalId = setInterval(() => {
    // Process data
  }, 1000);
}

function stopProcess() {
  if (intervalId) {
    clearInterval(intervalId);
    intervalId = null;
  }
}
```

Deep Insight:
- Use --inspect flag for debugging
- Take heap snapshots to identify leaks
- Monitor memory usage over time
- Clear timers and event listeners
- Use weak references for large objects

## 90) What are key strategies for performance optimization (profiling, batching, async iteration, compression, connection pooling)?

Concept: Performance optimization involves profiling to identify bottlenecks, implementing efficient patterns like batching and async iteration, and optimizing resource usage.

Example:
```javascript
// Profiling with performance hooks
const { performance, PerformanceObserver } = require('perf_hooks');

const obs = new PerformanceObserver((list) => {
  list.getEntries().forEach((entry) => {
    console.log(`${entry.name}: ${entry.duration}ms`);
  });
});
obs.observe({ entryTypes: ['measure'] });

// Batching operations
async function batchProcess(items) {
  const batchSize = 100;
  const batches = [];
  
  for (let i = 0; i < items.length; i += batchSize) {
    batches.push(items.slice(i, i + batchSize));
  }
  
  for (const batch of batches) {
    await Promise.all(batch.map(processItem));
  }
}

// Async iteration
async function processLargeDataset() {
  const stream = fs.createReadStream('large-file.txt');
  for await (const chunk of stream) {
    await processChunk(chunk);
  }
}
```

Deep Insight:
- Profile before optimizing
- Use batching for bulk operations
- Implement async iteration for large datasets
- Use connection pooling for databases
- Monitor and measure improvements
