# 9) Performance, Optimization, Scaling & Monitoring (Q81–90)

## Q81. What are common Node.js performance bottlenecks, and how can they be fixed?

Common bottlenecks include blocking I/O operations, memory leaks, inefficient algorithms, and event loop blocking - avoid synchronous operations in request handlers, use streaming for large data processing, implement proper error handling, monitor event loop lag, and profile CPU and memory usage regularly. Can be addressed through proper async patterns and optimization techniques.

- **Trade-offs**: Avoid synchronous operations in request handlers - use streaming for large data processing. Implement proper error handling - monitor event loop lag. Profile CPU and memory usage regularly - identify bottlenecks first, but watch out - premature optimization can add complexity, so measure before optimizing.

Example:

```javascript
app.get('/data', (req, res) => {
  const data = fs.readFileSync('large-file.txt');
  res.json({ data });
});

app.get('/data', (req, res) => {
  fs.readFile('large-file.txt', (err, data) => {
    if (err) return res.status(500).json({ error: err.message });
    res.json({ data });
  });
});

app.get('/data', (req, res) => {
  const stream = fs.createReadStream('large-file.txt');
  stream.pipe(res);
});
```

## Q82. How do you optimize Express middleware performance (limit heavy middleware, compression, caching)?

Optimize middleware by reducing heavy operations, implementing compression, caching, and ordering middleware efficiently - order middleware by frequency of use, use compression for text responses, implement caching for expensive operations, avoid heavy middleware on all routes, and monitor middleware execution time. Minimizes request processing time.

- **Trade-offs**: Order middleware by frequency of use - use compression for text responses. Implement caching for expensive operations - avoid heavy middleware on all routes. Monitor middleware execution time - middleware order matters for performance, but watch out - too much caching can cause stale data, so balance freshness with performance.

Example:

```javascript
const compression = require('compression');
const helmet = require('helmet');

app.use(helmet());
app.use(compression());
app.use(express.json({ limit: '10mb' }));

app.use('/api', (req, res, next) => {
  if (req.path.startsWith('/admin')) {
    return heavyAuthMiddleware(req, res, next);
  }
  next();
});

const cache = new Map();
app.use('/api/data', (req, res, next) => {
  const cacheKey = req.originalUrl;
  if (cache.has(cacheKey)) {
    return res.json(cache.get(cacheKey));
  }
  next();
});
```

## Q83. How do you optimize database queries and prevent blocking in Node.js?

Optimize database performance by using connection pooling, query optimization, indexing, and async database operations - use connection pooling for database connections, optimize queries with proper indexing, use prepared statements to prevent SQL injection, implement query caching for frequently accessed data, and monitor database performance and slow queries. Prevents blocking the event loop.

- **Trade-offs**: Use connection pooling for database connections - optimize queries with proper indexing. Use prepared statements to prevent SQL injection - implement query caching for frequently accessed data. Monitor database performance and slow queries - essential for performance, but watch out - connection pools need proper sizing, too many connections can overwhelm the database.

Example:

```javascript
const mysql = require('mysql2/promise');

const pool = mysql.createPool({
  host: 'localhost',
  user: 'root',
  password: 'password',
  database: 'mydb',
  connectionLimit: 10,
  acquireTimeout: 60000,
  timeout: 60000
});

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

## Q84. What is PM2, and how does it help manage and optimize production processes?

PM2 is a process manager for Node.js applications that provides clustering, monitoring, logging, and automatic restarts for production deployments - it provides process clustering and load balancing, automatic restarts on crashes, built-in monitoring and logging, zero-downtime deployments, and memory and CPU monitoring.

- **Trade-offs**: Provides process clustering and load balancing - automatic restarts on crashes. Built-in monitoring and logging - zero-downtime deployments. Memory and CPU monitoring - essential for production, but watch out - PM2 adds overhead, so consider alternatives like Docker for containerized deployments.

Example:

```javascript
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

## Q85. How do you scale a Node.js application horizontally (Cluster, Load Balancer, Containers)?

Horizontal scaling involves running multiple instances of the application across different processes, machines, or containers, with load balancing to distribute requests - use clustering for multi-core utilization, implement load balancing for multiple servers, use containers (Docker) for consistent deployments, consider microservices architecture, and implement health checks and monitoring.

- **Trade-offs**: Use clustering for multi-core utilization - implement load balancing for multiple servers. Use containers (Docker) for consistent deployments - consider microservices architecture. Implement health checks and monitoring - essential for scale, but watch out - horizontal scaling adds complexity, so start with clustering before moving to multiple servers.

Example:

```javascript
const cluster = require('cluster');
const numCPUs = require('os').cpus().length;

if (cluster.isMaster) {
  console.log(`Master ${process.pid} is running`);
  for (let i = 0; i < numCPUs; i++) {
    cluster.fork();
  }
  cluster.on('exit', (worker, code, signal) => {
    console.log(`Worker ${worker.process.pid} died`);
    cluster.fork();
  });
} else {
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

## Q86. How do you implement in-memory and distributed caching (Redis, LRU)?

Caching stores frequently accessed data in fast storage (memory or Redis) to reduce database load and improve response times - use Redis for distributed caching, implement cache invalidation strategies, consider cache warming for critical data, monitor cache hit rates, and use appropriate TTL values.

- **Trade-offs**: Use Redis for distributed caching - implement cache invalidation strategies. Consider cache warming for critical data - monitor cache hit rates. Use appropriate TTL values - essential for performance, but watch out - cache invalidation is tricky, so use TTLs and event-based invalidation carefully.

Example:

```javascript
const redis = require('redis');
const client = redis.createClient();

const LRU = require('lru-cache');
const cache = new LRU({ max: 100, ttl: 1000 * 60 * 5 });

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

## Q87. What are effective techniques for optimizing API response time?

Optimize API response times through caching, database optimization, compression, CDN usage, and efficient data processing - use database pagination instead of loading all data, select only necessary fields, implement proper indexing, use compression for text responses, and consider CDN for static assets.

- **Trade-offs**: Use database pagination instead of loading all data - select only necessary fields. Implement proper indexing - use compression for text responses. Consider CDN for static assets - multiple techniques work together, but watch out - over-optimization can add complexity, so measure and optimize based on actual bottlenecks.

Example:

```javascript
const compression = require('compression');
const rateLimit = require('express-rate-limit');

app.use(compression());

const limiter = rateLimit({
  windowMs: 15 * 60 * 1000,
  max: 100
});
app.use('/api/', limiter);

app.get('/api/users', async (req, res) => {
  const { page = 1, limit = 10 } = req.query;
  
  const users = await User.find()
    .select('id name email')
    .limit(limit * 1)
    .skip((page - 1) * limit)
    .lean();
  
  res.json({
    users,
    pagination: { page, limit, total: await User.countDocuments() }
  });
});
```

## Q88. How do you use monitoring tools like New Relic, Sentry, or Datadog?

Monitoring tools provide real-time insights into application performance, errors, and user experience - monitor key performance metrics, set up alerts for critical issues, track user experience metrics, monitor database and external service performance, and use distributed tracing for microservices. Enables proactive issue detection and resolution.

- **Trade-offs**: Monitor key performance metrics - set up alerts for critical issues. Track user experience metrics - monitor database and external service performance. Use distributed tracing for microservices - essential for production, but watch out - monitoring adds overhead, so use sampling for high-traffic applications.

Example:

```javascript
const newrelic = require('newrelic');

app.get('/api/users', (req, res) => {
  newrelic.recordMetric('Custom/UsersEndpoint', 1);
});

const Sentry = require('@sentry/node');
Sentry.init({ dsn: process.env.SENTRY_DSN });

app.use(Sentry.requestHandler());
app.use(Sentry.errorHandler());

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

## Q89. How do you identify and fix memory leaks (Heap snapshots, Node --inspect)?

Memory leaks occur when objects are not properly garbage collected, identified through heap snapshots and profiling tools - use --inspect flag for debugging, take heap snapshots to identify leaks, monitor memory usage over time, clear timers and event listeners, and use weak references for large objects.

- **Trade-offs**: Use --inspect flag for debugging - take heap snapshots to identify leaks. Monitor memory usage over time - clear timers and event listeners. Use weak references for large objects - essential for long-running apps, but watch out - memory leaks can be subtle, so use heap snapshots to identify what's holding references.

Example:

```javascript
const leakyArray = [];
setInterval(() => {
  leakyArray.push(new Array(1000).fill('leak'));
}, 1000);

setInterval(() => {
  const usage = process.memoryUsage();
  console.log('Memory usage:', {
    rss: Math.round(usage.rss / 1024 / 1024) + ' MB',
    heapTotal: Math.round(usage.heapTotal / 1024 / 1024) + ' MB',
    heapUsed: Math.round(usage.heapUsed / 1024 / 1024) + ' MB'
  });
}, 5000);

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

## Q90. What are key strategies for performance optimization (profiling, batching, async iteration, compression, connection pooling)?

Performance optimization involves profiling to identify bottlenecks, implementing efficient patterns like batching and async iteration, and optimizing resource usage - profile before optimizing, use batching for bulk operations, implement async iteration for large datasets, use connection pooling for databases, and monitor and measure improvements.

- **Trade-offs**: Profile before optimizing - use batching for bulk operations. Implement async iteration for large datasets - use connection pooling for databases. Monitor and measure improvements - multiple strategies work together, but watch out - optimization should be data-driven, so measure before and after changes.

Example:

```javascript
const { performance, PerformanceObserver } = require('perf_hooks');

const obs = new PerformanceObserver((list) => {
  list.getEntries().forEach((entry) => {
    console.log(`${entry.name}: ${entry.duration}ms`);
  });
});
obs.observe({ entryTypes: ['measure'] });

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

async function processLargeDataset() {
  const stream = fs.createReadStream('large-file.txt');
  for await (const chunk of stream) {
    await processChunk(chunk);
  }
}
```
