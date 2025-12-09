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

## Q1. Scaling a REST API to handle 1B+ requests per day

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

## Q2. Handling database scaling

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

## Q3. Handling traffic spikes

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
