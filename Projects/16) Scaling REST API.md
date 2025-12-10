# Scaling REST API Architecture

> **Project Type:** System Design
> **Scale:** Handle 1B+ requests per day, scale horizontally, maintain low latency
> **Tech Stack:** Load Balancer, Caching, Database Scaling, CDN

# 1) Problem Statement

Design and implement strategies to scale a REST API that addresses the following challenges:

- **Core Functionality**: Scale REST API from handling millions to billions of requests per day while maintaining low latency and high availability
- **Scale Requirements**: Handle 1B+ requests per day, millions of concurrent requests, traffic spikes (10x normal), and growing user base
- **Performance**: API latency < 200ms (p95), fast response times, efficient request processing, low overhead
- **Horizontal Scaling**: Scale horizontally across multiple servers, implement auto-scaling capabilities, handle traffic distribution
- **Caching Strategy**: Implement multi-layer caching (application cache, CDN, database cache), optimize cache hit rates, reduce database load
- **Database Scaling**: Optimize database performance through read replicas and sharding, handle database bottlenecks, maintain data consistency
- **Traffic Management**: Handle traffic spikes gracefully, implement rate limiting, prevent overload, maintain service availability
- **Data Consistency**: Maintain data consistency across distributed systems, handle concurrent requests reliably, ensure accurate responses

---

# 2) High Level Design (HLD)

## a) Requirements

### i) Functional Requirements

- RESTful API endpoints

- Authentication and authorization

- Request validation

- Error handling

- API versioning

### ii) Non-Functional Requirements

- API latency < 200ms (p95)

- 99.9% availability

- Handle traffic spikes (10x normal)

- Horizontal scaling

---

## b) Scope and Priority

### Phase 1: MVP (Must Have) - Priority 1

- Core functionality

- Basic features

### Phase 2: Enhanced Features - Priority 2

- Additional capabilities

- Performance improvements

### Phase 2: Enhanced Features - Priority 2

- Advanced caching strategies

- Database read replicas and sharding

- Auto-scaling implementation

- Advanced monitoring and alerting

- Performance optimization techniques

---

## c) Technology Choices

### Backend Framework

- **Node.js with Express.js** - Scalable API server

### Load Balancing

- **Load Balancer** - Distribute traffic across servers

### Database

- **Database with Read Replicas** - Scale read operations

- **Database Sharding** - Horizontal scaling

### Caching

- **Redis** - Multi-layer caching strategy

- **CDN** - Cache static responses

---

---

## Architecture Overview

```

┌─────────────┐
│   Client    │
└──────┬──────┘
       │
       ▼
┌─────────────────┐
│  Load Balancer  │
└──────┬──────────┘
       │
   ┌───┴───┐
   ▼       ▼
┌──────┐ ┌──────┐
│Server│ │Server│
└──┬───┘ └──┬───┘
   │        │
   └───┬────┘
       ▼
┌─────────────────┐
│  Database       │
└─────────────────┘

```

---

## Key Design Decisions

1. **Load Balancing:** Distribute requests across multiple servers

2. **Caching:** Cache responses to reduce database load

3. **Database Optimization:** Read replicas, connection pooling, indexing

4. **CDN:** Use CDN for static content

5. **Rate Limiting:** Prevent API abuse

---

# 3) Low Level Design (LLD)

---

## Component Architecture

### Service Components

```typescript
class Service {
  async processRequest(data: any) {
    // Implementation details
  }
}

```

---

## Frontend Design

### Component Architecture

Think of the frontend as a tree of React components - each component handles a specific part of the UI, and they work together to create the complete user experience.

**Component Hierarchy:**

```
App (Admin Dashboard)
├── Header
│   ├── Logo
│   ├── Navigation
│   └── UserMenu (Profile, Settings, Sign out)
├── MainContent
│   ├── DashboardPage
│   │   ├── MetricsOverview
│   │   │   ├── RequestRateChart
│   │   │   ├── LatencyChart (p50, p95, p99)
│   │   │   ├── ErrorRateChart
│   │   │   ├── ThroughputChart
│   │   │   └── ActiveConnections
│   │   ├── ServerStatusGrid
│   │   │   └── ServerCard
│   │   │       ├── ServerName
│   │   │       ├── HealthStatus
│   │   │       ├── CPUUsage
│   │   │       ├── MemoryUsage
│   │   │       └── RequestCount
│   │   └── AlertsPanel
│   ├── PerformancePage
│   │   ├── LatencyBreakdown
│   │   ├── CacheHitRate
│   │   ├── DatabaseQueryPerformance
│   │   └── CDNPerformance
│   ├── ScalingPage
│   │   ├── AutoScalingConfig
│   │   │   ├── MinInstances
│   │   │   ├── MaxInstances
│   │   │   ├── ScaleUpThreshold
│   │   │   └── ScaleDownThreshold
│   │   ├── CurrentInstances
│   │   └── ScalingHistory
│   ├── CacheManagementPage
│   │   ├── CacheStats
│   │   ├── CacheKeysList
│   │   └── CacheInvalidationControls
│   └── DatabasePage
│       ├── DatabaseConnections
│       ├── QueryPerformance
│       ├── ReplicationStatus
│       └── ShardingStatus
└── Footer

```

### Key React Components

**Frontend Implementation:**

```typescript
// Metrics Overview Component
const MetricsOverview: React.FC = () => {
  const { data: metrics } = useMetrics();

  return (
    <div className="metrics-overview">
      <MetricCard
        title="Request Rate"
        value={metrics?.requestRate}
        unit="req/s"
        chart={<RequestRateChart data={metrics?.requestRateHistory} />}
      />
      <MetricCard
        title="P95 Latency"
        value={metrics?.p95Latency}
        unit="ms"
        chart={<LatencyChart data={metrics?.latencyHistory} />}
      />
      <MetricCard
        title="Error Rate"
        value={metrics?.errorRate}
        unit="%"
        chart={<ErrorRateChart data={metrics?.errorRateHistory} />}
      />
    </div>
  );
};

// Auto Scaling Configuration Component
const AutoScalingConfig: React.FC = () => {
  const [config, setConfig] = useState<ScalingConfig>({
    minInstances: 2,
    maxInstances: 10,
    scaleUpThreshold: 80,
    scaleDownThreshold: 30
  });
  const saveConfigMutation = useSaveScalingConfig();

  const handleSave = () => {
    saveConfigMutation.mutate(config);
  };

  return (
    <div className="auto-scaling-config">
      <h3>Auto Scaling Configuration</h3>
      <div className="config-form">
        <label>
          Min Instances:
          <input
            type="number"
            value={config.minInstances}
            onChange={(e) => setConfig({ ...config, minInstances: Number(e.target.value) })}
          />
        </label>
        <label>
          Max Instances:
          <input
            type="number"
            value={config.maxInstances}
            onChange={(e) => setConfig({ ...config, maxInstances: Number(e.target.value) })}
          />
        </label>
        <label>
          Scale Up Threshold (% CPU):
          <input
            type="number"
            value={config.scaleUpThreshold}
            onChange={(e) => setConfig({ ...config, scaleUpThreshold: Number(e.target.value) })}
          />
        </label>
        <label>
          Scale Down Threshold (% CPU):
          <input
            type="number"
            value={config.scaleDownThreshold}
            onChange={(e) => setConfig({ ...config, scaleDownThreshold: Number(e.target.value) })}
          />
        </label>
        <button onClick={handleSave}>Save Configuration</button>
      </div>
    </div>
  );
};

```

### State Management

**State Management Strategy:**

- **Local State (useState)**: Form inputs, UI state (loading, errors, filters, selected time range)
- **Component State**: Each component manages its own UI state
- **API State**: React Query or SWR for server state (metrics, server status, scaling config) - caching, refetching
- **Global State (Redux Toolkit)**: User authentication, dashboard preferences, selected metrics

**Frontend Implementation:**

```typescript
// Using React Query for API state management
import { useQuery, useMutation, useQueryClient } from '@tanstack/react-query';

const useMetrics = (timeRange: string = '1h') => {
  return useQuery({
    queryKey: ['metrics', timeRange],
    queryFn: async () => {
      const response = await axios.get('/api/v1/metrics', { params: { timeRange } });
      return response.data;
    },
    refetchInterval: 10000 // Refetch every 10 seconds for real-time updates
  });
};

const useSaveScalingConfig = () => {
  const queryClient = useQueryClient();
  
  return useMutation({
    mutationFn: async (config: ScalingConfig) => {
      const response = await axios.post('/api/v1/scaling/config', config);
      return response.data;
    },
    onSuccess: () => {
      // Invalidate scaling config
      queryClient.invalidateQueries({ queryKey: ['scaling-config'] });
    }
  });
};

```

### Component Interactions

**Data Flow:**

1. **Dashboard Loading** → DashboardPage fetches metrics and server status
2. **Metrics Display** → Metrics displayed in charts with real-time updates
3. **Scaling Configuration** → Admin configures auto-scaling rules
4. **Cache Management** → Admin views cache stats and invalidates cache
5. **Database Monitoring** → Admin monitors database performance and connections

**Event Handling:**

- Time range changes refetch metrics
- Scaling configuration saves to backend
- Cache invalidation triggers cache refresh
- Real-time metrics updates via polling or WebSocket
- Server status updates automatically

### UI/UX Considerations

- **Loading States**: Show skeleton loaders for metrics, spinners for actions
- **Error Handling**: Display user-friendly error messages with retry options
- **Validation**: Client-side validation for scaling configuration values
- **Responsive Design**: Desktop-optimized layout for admin dashboard
- **Accessibility**: ARIA labels, keyboard navigation, screen reader support
- **Performance**: Efficient chart rendering, real-time updates via WebSocket or polling, data aggregation for large datasets

---

## Data Models

### Model Interface

```typescript
interface Model {
  id: string;
  // Model fields
  createdAt: Date;
  updatedAt: Date;
}

```

---

## Data APIs

**Note:** This section describes the REST API endpoints that are scaled. The actual endpoints depend on the application being scaled.

### Example API Endpoints

### GET /api/v1/users

- **URL:** `/api/v1/users?page=1&limit=20`

- **Method:** GET

- **Description:** Get list of users with pagination

- **Response:**

  ```json
  {
    "success": true,
    "data": {
      "users": [...],
      "pagination": {
        "page": 1,
        "limit": 20,
        "total": 1000,
        "totalPages": 50
      }
    }
  }

  ```

- **Status Codes:** 200 (Success)

### GET /api/v1/users/:userId

- **URL:** `/api/v1/users/:userId`

- **Method:** GET

- **Response:**

  ```json
  {
    "success": true,
    "data": {
      "userId": "user123",
      "name": "John Doe",
      "email": "john@example.com"
    }
  }

  ```

- **Status Codes:** 200 (Success), 404 (Not Found)

---

## Backend Implementation Details

### Express.js Server Structure

```

server/
├── routes/
├── controllers/
├── services/
└── models/

```

### API Service

```typescript
class APIService {
  async getUsers(page: number, limit: number): Promise<User[]> {
    // Query database with pagination
    // Apply caching
    // Return users
  }

  async getUserById(userId: string): Promise<User> {
    // Check cache first
    // Query database if not cached
    // Return user
  }
}

```

---

## Scaling Strategies

### Horizontal Scaling

- Multiple API servers behind load balancer

- Auto-scaling based on CPU/memory metrics

- Stateless servers for easy scaling

### Database Scaling

- Read replicas for read-heavy workloads

- Database sharding for write scaling

- Connection pooling

## Protocols

### REST API Protocol

- **Protocol:** REST (Representational State Transfer)

- **Data Format:** JSON

- **Authentication:** JWT Bearer token

### Additional Protocols

- **WebSocket** - For real-time features (if applicable)

- **Message Queue** - For async processing (if applicable)

---

---

## Implementation Details

### Core Implementation

**Note:** Implementation details focus on backend (Node.js/Express.js) scaling strategies.

### Caching Strategy

**Backend Implementation:** Express.js middleware implements multi-layer caching

- **Strategy:** Multi-layer caching with Redis and CDN - like having multiple storage layers, cache at different levels for maximum performance

- **Cache Layers:** Application cache (Redis), CDN cache (CloudFront), database query cache

**Backend (Express.js):**

```typescript
// Backend: middleware/cacheMiddleware.ts
import redis from '../config/redis';

export const cacheMiddleware = (ttl: number = 300) => {
  return async (req: Request, res: Response, next: NextFunction) => {
    // Only cache GET requests
    if (req.method !== 'GET') {
      return next();
    }

    const cacheKey = `cache:${req.originalUrl}`;

    try {
      // Check cache
      const cached = await redis.get(cacheKey);
      if (cached) {
        return res.json(JSON.parse(cached));
      }

      // Store original res.json
      const originalJson = res.json.bind(res);

      // Override res.json to cache response
      res.json = function(body: any) {
        // Cache response
        redis.setex(cacheKey, ttl, JSON.stringify(body));
        return originalJson(body);
      };

      next();
    } catch (error) {
      // Fail-open: continue without caching
      next();
    }
  };
};

// Usage
app.get('/api/v1/users', cacheMiddleware(300), userController.getUsers);

```

### Database Connection Pooling

**Backend Implementation:** Express.js uses connection pooling for database connections

- **Strategy:** Connection pooling - like a taxi stand, maintains a pool of ready connections instead of creating new ones

- **Pool Size:** Configure pool size based on server capacity and expected load

**Backend (Express.js):**

```typescript
// Backend: config/database.ts
import mongoose from 'mongoose';

mongoose.connect(process.env.MONGODB_URI!, {
  maxPoolSize: 10, // Maximum number of connections in pool
  minPoolSize: 5,  // Minimum number of connections in pool
  serverSelectionTimeoutMS: 5000,
  socketTimeoutMS: 45000,
});

// PostgreSQL connection pooling
import { Pool } from 'pg';

const pool = new Pool({
  host: process.env.DB_HOST,
  port: parseInt(process.env.DB_PORT || '5432'),
  database: process.env.DB_NAME,
  user: process.env.DB_USER,
  password: process.env.DB_PASSWORD,
  max: 20, // Maximum pool size
  idleTimeoutMillis: 30000,
  connectionTimeoutMillis: 2000,
});

```

### Load Balancing

**Backend Implementation:** Nginx/HAProxy load balancer distributes requests

- **Strategy:** Round-robin or least connections - like distributing customers to multiple cashiers, balances load across servers

- **Health Checks:** Monitor server health, remove unhealthy servers from pool

**Nginx Configuration:**

```nginx
upstream api_servers {
    least_conn;  # Use least connections algorithm
    server api1.example.com:3000;
    server api2.example.com:3000;
    server api3.example.com:3000;
}

server {
    listen 80;

    location /api/ {
        proxy_pass http://api_servers;
        proxy_set_header Host $host;
        proxy_set_header X-Real-IP $remote_addr;

        # Health check
        health_check interval=10s fails=3 passes=2;
    }
}

```

### Error Handling

**Backend Implementation:** Express.js middleware handles errors and returns proper status codes

**Backend (Express.js):**

```typescript
// Backend: middleware/errorHandler.ts
export const errorHandler = (err: Error, req: Request, res: Response, next: NextFunction) => {
  console.error('API Error:', err);

  if (err.name === 'ValidationError') {
    return res.status(400).json({ error: 'Validation failed', details: err.message });
  }

  if (err.message === 'Database connection failed') {
    return res.status(503).json({ error: 'Service temporarily unavailable' });
  }

  if (err.name === 'TimeoutError') {
    return res.status(504).json({ error: 'Request timeout' });
  }

  res.status(500).json({ error: 'Internal server error' });
};

```

**Error Scenarios:**

- **Database Errors:** Handle connection failures, query timeouts - implement connection pooling, retry logic, circuit breaker

- **Cache Errors:** Handle Redis failures - fail-open strategy, continue without cache

- **Load Balancer Errors:** Handle server failures - health checks, automatic failover, remove unhealthy servers

- **Timeout Errors:** Handle request timeouts - configure appropriate timeouts, return 504 status

---

# 3) Interview Answers

---

## Q1. 🔀 Scaling a REST API to handle 1B+ requests per day

**Situation:** Need to scale REST API from handling 1M requests/day to 1B+ requests/day while maintaining < 200ms latency and 99.9% availability.

**Action:** I implemented comprehensive scaling strategies:

- **Horizontal Scaling:** Deploy multiple API servers behind load balancer, auto-scale based on metrics

- **Caching:** Implement multi-layer caching (Redis for API responses, CDN for static content)

- **Database Optimization:** Use read replicas for read queries, connection pooling, proper indexing

- **Database Sharding:** Shard database by user ID for write scaling

- **Rate Limiting:** Implement rate limiting to prevent abuse and ensure fair usage

- **Async Processing:** Move heavy operations to background jobs (message queue)

- **CDN:** Use CDN for static assets to reduce server load

- **Monitoring:** Implement comprehensive monitoring and alerting

**Result:** API scales to handle 1B+ requests/day. P95 latency < 200ms. 99.9% availability. Handles 10x traffic spikes without degradation.

**Takeaway:** Horizontal scaling is essential. Caching reduces database load significantly. Database optimization is critical for performance.

---

## Q2. 📊 Handling database scaling

**Situation:** Single database cannot handle 1B+ requests/day, need to scale database.

**Action:** I implemented database scaling:

- **Read Replicas:** Deploy read replicas, route read queries to replicas

- **Connection Pooling:** Use connection pooling to manage database connections efficiently

- **Indexing:** Add proper indexes on frequently queried columns

- **Query Optimization:** Optimize slow queries, use EXPLAIN to analyze query plans

- **Database Sharding:** Shard database by user ID, route queries to appropriate shard

- **Caching:** Cache frequently accessed data in Redis to reduce database load

- **Partitioning:** Partition large tables by date or other criteria

**Result:** Database handles 1B+ requests/day. Read replicas distribute read load. Sharding enables write scaling. Query latency reduced by 80%.

**Takeaway:** Read replicas scale read operations. Sharding scales write operations. Caching reduces database load.

---

## Q3. 💡 Handling traffic spikes

**Situation:** Traffic suddenly increases 10x during peak hours, need to handle without degradation.

**Action:** I implemented traffic spike handling:

- **Auto-scaling:** Auto-scale servers based on CPU/memory metrics

- **Caching:** Aggressive caching to reduce backend load during spikes

- **Rate Limiting:** Implement rate limiting to prevent abuse

- **Queue System:** Queue non-critical requests during spikes

- **Circuit Breaker:** Open circuit for failing services to prevent cascading failures

- **Load Shedding:** Drop low-priority requests during extreme spikes

- **Monitoring:** Real-time monitoring to detect spikes early

**Result:** System handles 10x traffic spikes without degradation. Auto-scaling adds servers within 2 minutes. 99.9% availability maintained.

**Takeaway:** Auto-scaling is essential for handling traffic spikes. Caching and queue systems help absorb spikes.

---

## Q4. 💾 Implementing caching strategies

**Situation:** Database load is too high, need to reduce database queries by implementing effective caching strategies.

**Action:** I implemented multi-layer caching:

- **Application Cache (Redis):** Cache API responses, user sessions, frequently accessed data
- **CDN Cache:** Cache static assets and API responses at edge locations
- **Database Query Cache:** Cache query results for frequently executed queries
- **Cache Invalidation:** Implement cache invalidation strategies (TTL, event-based, manual)
- **Cache Warming:** Pre-load cache with popular data during low-traffic periods
- **Cache Patterns:** Use cache-aside pattern for flexibility, write-through for consistency
- **Cache Monitoring:** Monitor cache hit rates, adjust TTL based on access patterns

**Result:** Cache hit rate of 80%+ for frequently accessed endpoints. Database load reduced by 70%. API response times improved by 60%.

**Takeaway:** Multi-layer caching significantly reduces database load. Cache invalidation is critical for data consistency. Monitor cache performance to optimize.

---

## Q5. ⚡ Monitoring and optimizing API performance

**Situation:** Need to monitor API performance and identify bottlenecks to optimize.

**Action:** I implemented comprehensive monitoring and optimization:

- **APM Tools:** Use Application Performance Monitoring (New Relic, Datadog) to track latency, throughput, errors
- **Metrics Collection:** Track p50, p95, p99 latencies, request rates, error rates, database query times
- **Distributed Tracing:** Implement distributed tracing (Jaeger, Zipkin) to track requests across services
- **Logging:** Structured logging with correlation IDs for request tracking
- **Alerting:** Set up alerts for high latency, high error rates, low availability
- **Performance Profiling:** Profile slow endpoints, identify bottlenecks (database queries, external API calls)
- **Optimization:** Optimize slow queries, add indexes, implement caching, optimize code paths

**Result:** Identified and fixed 10+ performance bottlenecks. P95 latency reduced from 500ms to 150ms. Error rate reduced by 90%. System performance improved significantly.

**Takeaway:** Monitoring is essential for identifying bottlenecks. Distributed tracing helps track request flow. Continuous optimization improves performance.

---

# 4) Algorithms

## Consistent Hashing Algorithm

**Purpose:** Distribute requests evenly across multiple servers and minimize data movement when servers are added or removed.

**Algorithm:**
1. Create a hash ring (circular space) from 0 to 2^64 - 1
2. Hash each server to multiple points on the ring (virtual nodes)
3. Hash the request key to a point on the ring
4. Find the first server clockwise from the key's position

**Implementation:**

```typescript
import crypto from 'crypto';

class ConsistentHash {
  private ring: Map<number, string> = new Map();
  private sortedKeys: number[] = [];
  private virtualNodes: number = 150;
  
  addServer(serverId: string): void {
    for (let i = 0; i < this.virtualNodes; i++) {
      const hash = this.hash(`${serverId}-${i}`);
      this.ring.set(hash, serverId);
      this.sortedKeys.push(hash);
    }
    this.sortedKeys.sort((a, b) => a - b);
  }
  
  removeServer(serverId: string): void {
    for (let i = 0; i < this.virtualNodes; i++) {
      const hash = this.hash(`${serverId}-${i}`);
      this.ring.delete(hash);
      const index = this.sortedKeys.indexOf(hash);
      if (index > -1) {
        this.sortedKeys.splice(index, 1);
      }
    }
  }
  
  getServer(key: string): string {
    if (this.ring.size === 0) {
      throw new Error('No servers available');
    }
    
    const hash = this.hash(key);
    
    for (const ringKey of this.sortedKeys) {
      if (ringKey >= hash) {
        return this.ring.get(ringKey)!;
      }
    }
    
    return this.ring.get(this.sortedKeys[0])!;
  }
  
  private hash(key: string): number {
    const hash = crypto.createHash('md5').update(key).digest();
    return hash.readUInt32BE(0);
  }
}

```

**Complexity:**
- Time: O(log n) for server lookup where n is number of virtual nodes
- Space: O(v * s) where v is virtual nodes, s is number of servers
- **Data Movement:** Only ~1/n of data moves when adding/removing servers

---

## Cache Eviction Algorithm (LRU)

**Purpose:** Manage Redis cache efficiently by evicting least recently used items when cache is full.

**Algorithm:**
1. Maintain a doubly-linked list of cached items ordered by access time
2. Use a hash map for O(1) lookup
3. On access: move item to front (most recently used)
4. On eviction: remove item from back (least recently used)

**Implementation:**

```typescript
class LRUCache {
  private capacity: number;
  private cache: Map<string, { value: any; node: Node }> = new Map();
  private head: Node;
  private tail: Node;
  
  constructor(capacity: number) {
    this.capacity = capacity;
    this.head = new Node('', '');
    this.tail = new Node('', '');
    this.head.next = this.tail;
    this.tail.prev = this.head;
  }
  
  get(key: string): any {
    const item = this.cache.get(key);
    
    if (!item) {
      return null;
    }
    
    this.moveToFront(item.node);
    return item.value;
  }
  
  put(key: string, value: any): void {
    const existing = this.cache.get(key);
    
    if (existing) {
      existing.value = value;
      this.moveToFront(existing.node);
      return;
    }
    
    if (this.cache.size >= this.capacity) {
      this.evictLRU();
    }
    
    const node = new Node(key, value);
    this.addToFront(node);
    this.cache.set(key, { value, node });
  }
  
  private moveToFront(node: Node): void {
    this.removeNode(node);
    this.addToFront(node);
  }
  
  private addToFront(node: Node): void {
    node.prev = this.head;
    node.next = this.head.next;
    this.head.next!.prev = node;
    this.head.next = node;
  }
  
  private removeNode(node: Node): void {
    node.prev!.next = node.next;
    node.next!.prev = node.prev;
  }
  
  private evictLRU(): void {
    const lru = this.tail.prev!;
    this.removeNode(lru);
    this.cache.delete(lru.key);
  }
}

class Node {
  key: string;
  value: any;
  prev: Node | null = null;
  next: Node | null = null;
  
  constructor(key: string, value: any) {
    this.key = key;
    this.value = value;
  }
}

```

**Complexity:**
- Time: O(1) for get and put operations
- Space: O(capacity)

---

# 5) Data Models

## API Request Log (MongoDB)

```javascript
{
  _id: ObjectId,
  requestId: String,        // Unique request ID
  method: String,           // HTTP method
  path: String,            // API path
  statusCode: Number,       // Response status code
  latency: Number,         // Response time in ms
  userId: ObjectId,        // Optional, indexed
  ipAddress: String,       // Client IP
  userAgent: String,       // Client user agent
  timestamp: Date,         // Request timestamp, indexed
  responseSize: Number     // Response size in bytes
}

// Indexes:
// - { timestamp: -1 } (for time-based queries)
// - { path: 1, timestamp: -1 } (compound, for endpoint analysis)
// - { statusCode: 1, timestamp: -1 } (compound, for error analysis)

```

## Server Metrics (MongoDB)

```javascript
{
  _id: ObjectId,
  serverId: String,        // Server identifier
  timestamp: Date,         // Metric timestamp, indexed
  cpuUsage: Number,       // CPU usage percentage
  memoryUsage: Number,    // Memory usage percentage
  requestCount: Number,   // Requests handled
  errorCount: Number,     // Errors occurred
  avgLatency: Number      // Average latency in ms
}

// Indexes:
// - { serverId: 1, timestamp: -1 } (compound)
// - { timestamp: -1 } (for time-based queries)

```

---

# 6) Database Transactions and Consistency

### MongoDB Transactions

**Transaction Usage:**
- **Multi-Document Transactions** - For operations requiring ACID guarantees
- **Example:** User creation + account initialization in single transaction
- **Session Management:** Use MongoDB sessions for transaction control

**Example:**

```typescript
const session = await mongoose.startSession();
session.startTransaction();
try {
  await User.create([userData], { session });
  await Account.create([accountData], { session });
  await session.commitTransaction();
} catch (error) {
  await session.abortTransaction();
  throw error;
} finally {
  session.endSession();
}

```

### Consistency Strategies

**Data Consistency:**
- **Read Consistency:** Use read replicas for eventual consistency, primary for strong consistency
- **Cache Consistency:** Invalidate cache on data updates to prevent serving stale data
- **Distributed Consistency:** Use distributed locks for critical operations across servers

---

# 7) Protocols

### REST API Protocol

- **Protocol:** REST (Representational State Transfer)
- **Data Format:** JSON
- **HTTP Methods:** GET, POST, PUT, DELETE, PATCH
- **Status Codes:** 200 (Success), 201 (Created), 400 (Bad Request), 401 (Unauthorized), 404 (Not Found), 500 (Server Error)
- **Authentication:** JWT Bearer token in Authorization header

### Health Check Protocol

- **Endpoint:** `/health` or `/healthz`
- **Method:** GET
- **Response:** JSON with service status, dependencies status
- **Use Case:** Load balancer health checks, monitoring

---

# 8) API Design

### GET /api/v1/health

- **URL:** `/api/v1/health`
- **Method:** GET
- **Description:** Health check endpoint for load balancer and monitoring
- **Response:**

  ```json
  {
    "status": "healthy",
    "timestamp": "2024-01-15T10:30:00Z",
    "services": {
      "database": "healthy",
      "cache": "healthy",
      "external": "healthy"
    }
  }

  ```
- **Status Codes:** 200 (Healthy), 503 (Unhealthy)

### GET /api/v1/metrics

- **URL:** `/api/v1/metrics`
- **Method:** GET
- **Description:** Get API performance metrics (Admin only)
- **Query Parameters:**
  - `timeRange`: string (1h, 24h, 7d)
  - `endpoint`: string (optional)
- **Response:**

  ```json
  {
    "success": true,
    "data": {
      "requestRate": 11574,
      "p95Latency": 150,
      "p99Latency": 300,
      "errorRate": 0.1,
      "cacheHitRate": 80
    }
  }

  ```
- **Status Codes:** 200 (Success), 401 (Unauthorized), 403 (Forbidden)

---

# 9) Caching Strategy

### Redis Cache

**Cache Strategy:**
- **Key Format:** `cache:{endpoint}:{params}` or `cache:user:{userId}`
- **Value:** Serialized JSON response
- **TTL:** 5 minutes (configurable per endpoint)
- **Eviction Policy:** LRU (Least Recently Used)

**Cache Patterns:**
- **Cache-Aside Pattern:** Check cache first, if miss query database and update cache
- **Write-Through Pattern:** Write to cache and database simultaneously (for critical data)
- **Cache Warming:** Pre-load cache with popular data during low-traffic periods

### CDN Cache

**Cache Strategy:**
- **Static Assets:** Cache JS, CSS, images with long TTL (1 year)
- **API Responses:** Cache GET responses with short TTL (5 minutes)
- **Cache Headers:** Use Cache-Control headers for cache control
- **Cache Invalidation:** Purge cache on data updates

---

# 10) Error Handling

### Error Scenarios and Responses

**Edge Cases Handling:**
- **Database Connection Failure:** Return 503 Service Unavailable with retry suggestion
- **Cache Failure:** Fail-open, continue without cache (graceful degradation)
- **Timeout Errors:** Return 504 Gateway Timeout when request exceeds timeout
- **Rate Limit Exceeded:** Return 429 Too Many Requests with Retry-After header
- **Invalid Request:** Return 400 Bad Request with validation error details
- **Authentication Failure:** Return 401 Unauthorized
- **Authorization Failure:** Return 403 Forbidden

**Error Response Format:**

```json
{
  "error": {
    "code": "DATABASE_ERROR",
    "message": "Database connection failed",
    "details": "Unable to connect to database",
    "retryAfter": 5
  }
}

```

---

# 11) Deployment and DevOps

### Scalability

**API Layer:**
- Deploy API layer across multiple instances behind load balancer
- Use auto-scaling based on CPU/memory metrics
- Stateless design allows horizontal scaling

**Database Scaling:**
- **Read Replicas:** Deploy read replicas for read-heavy workloads
- **Sharding:** Shard database by user ID for write scaling
- **Connection Pooling:** Use connection pooling to manage database connections

**Caching:**
- Distributed Redis cluster for high availability
- Cache frequently accessed API responses
- Reduces database load significantly

### Availability

**Replication:**
- Database replication ensures data availability
- Multi-region replication for disaster recovery

**Failover:**
- Automated failover mechanisms for API and data store layers
- Health checks and monitoring for proactive failover
- Circuit breaker pattern to prevent cascading failures

**Geo-Distributed Deployment:**
- Deploy service across multiple geographical regions
- Reduces latency for users worldwide
- Improves availability by eliminating single point of failure

### Frontend Deployment

**Build Process:**
- **Production Build:** Optimized bundle with code splitting
- **CDN Deployment:** Deploy static assets to CDN for fast global delivery
- **Environment Variables:** `.env.production` for production config

**Deployment Platforms:**
- **Vercel / Netlify** - Automatic deployments from Git
- **AWS S3 + CloudFront** - Static site hosting with CDN

### Backend Deployment

**Server Setup:**
- **PM2:** Process manager with clustering for Node.js apps
- **Nginx:** Load balancer and reverse proxy with SSL termination
- **Docker:** Containerized deployment for consistency
- **Kubernetes:** Container orchestration for auto-scaling

**CI/CD Pipeline:**
- **Automated Testing:** Run tests before deployment
- **Zero-Downtime:** Rolling deployment strategy
- **Health Checks:** Verify API endpoints are healthy
- **Blue-Green Deployment:** Maintain two identical production environments

### Database Deployment

**MongoDB Setup:**
- **MongoDB Atlas** - Managed MongoDB service with automatic backups
- **Backup Strategy:** Daily automated backups with point-in-time recovery
- **Indexing:** Proper indexes on frequently queried fields
- **Replication:** Replica sets for high availability

**Redis Setup:**
- **Redis Cloud / AWS ElastiCache** - Managed Redis service
- **Cluster Mode:** Redis cluster for high availability and performance
- **Persistence:** RDB snapshots and AOF for data durability

---

# 12) Security Considerations

### Rate Limiting

- Implement rate limiting at API layer to prevent abuse
- Limit number of requests per user/IP per minute/hour
- Use Redis for distributed rate limiting across multiple servers

### Input Validation

- Validate all API inputs to ensure they meet requirements
- Sanitize user input to prevent injection attacks
- Check data types, ranges, and formats

### HTTPS/TLS

- All communication between clients and API encrypted using HTTPS
- Prevents eavesdropping and man-in-the-middle attacks
- SSL/TLS certificates for secure connections

### Authentication and Authorization

- **JWT Tokens:** Use JWT for stateless authentication
- **Token Expiration:** Set appropriate token expiration times
- **Role-Based Access Control:** Implement RBAC for authorization
- **API Keys:** Use API keys for service-to-service authentication

### Monitoring and Alerts

- Set up monitoring for unusual activity patterns
- Trigger alerts for potential DDoS attacks or misuse
- Track metrics: request rates, error rates, response times
- Log all operations for security auditing
