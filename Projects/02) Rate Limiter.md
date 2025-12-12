# Rate Limiter

> **Project Type:** Full-Stack System Component (MERN Stack)
> **Scale:** Handle millions of requests per second, < 10ms latency overhead per request
> **Tech Stack:** Node.js, Express.js, Redis, React.js

# 1) Problem Statement

Design and implement a distributed rate limiting system that addresses the following challenges:

- **Core Functionality**: Protect APIs from abuse by limiting requests per user, IP, or endpoint with configurable thresholds
- **Scale Requirements**: Handle millions of requests per second across distributed servers with minimal latency overhead (< 10ms per request)
- **Performance**: Rate limiting checks must be fast and efficient without significantly impacting API response times
- **Multiple Algorithms**: Support different rate limiting strategies (token bucket, sliding window, fixed window) for various use cases
- **Distributed Architecture**: Work seamlessly across multiple servers with shared state using Redis
- **Configurability**: Allow dynamic configuration of limits per endpoint, user tier, or IP without code changes
- **Monitoring & Analytics**: Provide real-time monitoring, metrics, and alerting for rate limit violations and abuse patterns
- **High Availability**: Maintain 99.9% uptime with fail-open strategy to prevent system-wide failures

---

# 2) High Level Design (HLD)

## a) Requirements

### i) Functional Requirements

- **Generate rate limit checks** for incoming API requests based on identifier (IP, user ID, API key)
- **Support multiple algorithms** - Fixed window, sliding window, and token bucket algorithms for different use cases
- **Per-user rate limiting** - Limit requests per authenticated user ID
- **Per-IP rate limiting** - Limit requests per IP address for anonymous users
- **Per-endpoint rate limiting** - Different limits for different API endpoints (e.g., login: 5/15min, search: 100/min)
- **Configurable limits** - Easy to adjust limits without code changes via admin API
- **Whitelist/Blacklist** - Allow or block specific IPs/users regardless of rate limits
- **Rate limit metrics** - Track how many requests are being limited, rejected, and allowed
- **Alerting** - Alert when rate limits are hit frequently or abuse patterns detected
- **Logging** - Log rate limit violations for analysis and security auditing

### ii) Non-Functional Requirements

- **Low latency** - Rate limiting check should be fast (< 10ms overhead per request)
- **High throughput** - Handle thousands of requests per second per server
- **Minimal overhead** - Shouldn't slow down API significantly, use Redis pipelining and connection pooling
- **Distributed** - Work across multiple servers with shared state in Redis
- **Horizontal scaling** - Add more servers without issues, stateless design
- **Fail-open strategy** - If rate limiter fails, allow requests (don't block everything)
- **Graceful degradation** - Fallback to in-memory rate limiting if Redis is down
- **High availability** - 99.9% uptime with Redis clustering and failover

---

## b) Scope and Priority

### Phase 1: MVP (Must Have) - Priority 1

- Basic rate limiting with per-IP identification
- Fixed window algorithm for simple time-based limiting
- Redis storage for rate limit counters
- HTTP headers with rate limit information (X-RateLimit-*)
- Performance target: < 10ms overhead per request
- Basic monitoring and logging of rate limit hits

### Phase 2: Enhanced Features - Priority 2

- Multiple algorithms (token bucket, sliding window) for different use cases
- Per-user rate limiting based on authenticated user ID
- Per-endpoint limits with different configurations
- Whitelist/Blacklist functionality for trusted/blocked identifiers
- Advanced monitoring dashboard with metrics and analytics
- Alerting system for high rate limit hits and abuse patterns

---

## c) Technology Choices

### Backend Framework

- **Node.js with Express.js** - Fast, event-driven runtime perfect for high-throughput rate limiting middleware with excellent Redis integration

### Storage

- **Redis** - In-memory data store for rate limit counters
  - **Why Redis?** Think of Redis as a super-fast shared whiteboard that all servers can read and write to instantly - it's perfect for rate limiting because it's in-memory (sub-millisecond access), supports atomic operations (INCR, EXPIRE) that prevent race conditions, and works across distributed servers
  - **Atomic operations** - INCR and EXPIRE commands ensure accurate counting even with concurrent requests
  - **TTL support** - Automatic expiration of counters means no manual cleanup needed
  - **Pub/Sub** - Can sync state across servers if needed for advanced scenarios

### Middleware

- **Express.js Middleware** - Intercept requests before they reach handlers, like a security guard checking IDs before allowing entry
  - Check rate limit before processing expensive operations
  - Return 429 Too Many Requests if limit exceeded
  - Add rate limit headers to response for client transparency

---

## d) Capacity Estimation

### Throughput Requirements

- **Average Requests Per Second**: 10,000 RPS across all servers
- **Peak Traffic**: 50,000 RPS (5x average)
- **Rate Limit Checks Per Request**: 1 check per request
- **Redis Operations Per Check**: 2-3 operations (get, increment, expire)

**Calculations:**

- **Average Redis Operations Per Second**: 10,000 × 2.5 = 25,000 ops/sec
- **Peak Redis Operations Per Second**: 50,000 × 2.5 = 125,000 ops/sec

### Storage Estimation

**Storage per Rate Limit Entry:**

- Redis Key: ~50 bytes (e.g., `rate_limit:ip:192.168.1.1:/api/users`)
- Counter Value: 8 bytes (integer)
- TTL Metadata: 8 bytes
- **Total per Entry**: ~66 bytes

**Storage Requirements:**

- **Active Rate Limit Entries**: 100,000 unique identifiers (IPs/users)
- **Total Storage**: 100,000 × 66 bytes ≈ 6.6 MB
- **With Overhead**: ~10 MB total Redis memory for rate limiting

### Latency Requirements

- **Rate Limit Check Target**: < 10ms per request
- **Redis Operation Latency**: < 5ms (with pipelining)
- **Middleware Overhead**: < 2ms
- **Total Overhead**: < 10ms (meets requirement)

### Infrastructure Sizing

- **API Servers**: 5-10 instances behind load balancer, each handling 1,000-2,000 RPS
- **Redis Cluster**: 3-node cluster for high availability, can handle 100,000+ ops/sec
- **Redis Memory**: 1-2 GB allocated for rate limiting data (with headroom)

---

## e) Architecture Overview

The system follows a middleware-based architecture where rate limiting is transparently applied to API requests. Here's how the complete system works:

### Frontend Architecture

**Frontend Layers:**

1. **Presentation Layer (React Components)**
   - **UI Components**: Reusable components (cards, tables, charts, buttons)
   - **Feature Components**: RateLimitMetricsDashboard, RateLimitConfigPanel, WhitelistBlacklistManager
   - **Layout Components**: Header, Footer, Navigation, MainLayout
   - **Page Components**: DashboardPage, ConfigPage, AnalyticsPage

2. **State Management Layer**
   - **Local State (useState)**: Component-specific UI state (filters, form inputs, selected time ranges)
   - **Server State (React Query)**: API data caching, refetching, optimistic updates for metrics and configs
   - **Global State (Context)**: User authentication, admin permissions, theme preferences

3. **API Integration Layer**
   - **API Client**: Axios instance with interceptors for auth, error handling
   - **React Query Hooks**: Custom hooks for API operations (useRateLimitMetrics, useRateLimitConfigs)
   - **Request/Response Transformation**: Data normalization and error handling

4. **Routing Layer (React Router)**
   - **Route Configuration**: Define routes and protected admin routes
   - **Navigation**: Programmatic and declarative navigation
   - **Route Guards**: Authentication and authorization checks for admin pages

5. **Build & Deployment Layer**
   - **Build Process**: Webpack/Vite bundling with code splitting
   - **Static Assets**: Served from CDN (CloudFront/Cloudflare)
   - **Environment Configuration**: Environment-specific API endpoints and configs

**Frontend Request Flow:**

1. **User Interaction** → Admin views dashboard or creates config
2. **API Call** → React Query mutation/query triggers API request
3. **Loading State** → UI shows loading indicator
4. **Response Handling** → Success/error state updates UI
5. **State Update** → React Query caches response, components re-render
6. **Real-time Updates** → Metrics refresh automatically every 30 seconds

### Backend Architecture

**Backend Layers:**

1. **API Gateway/Load Balancer** - Entry point for all requests
2. **Rate Limiter Middleware Layer** - Intercepts requests before processing
3. **API Server Layer** - Stateless servers handling HTTP requests
4. **Redis Cache Layer** - Shared state storage for rate limit counters
5. **Monitoring & Analytics Layer** - Metrics collection and alerting

### Complete Request Flow

**Rate Limiting Flow:**

1. **Client**: Makes API request to protected endpoint
2. **Load Balancer**: Routes request to available API server
3. **Rate Limiter Middleware**: Intercepts request before handler
4. **Identifier Extraction**: Extracts identifier (IP, user ID, API key) from request
5. **Redis Check**: Queries Redis for current count using algorithm-specific logic
6. **Counter Update**: Atomically increments counter in Redis
7. **Limit Check**: Compares count against configured limit
8. **Decision**: Allows request (pass to handler) or rejects with 429
9. **Headers**: Adds rate limit headers (X-RateLimit-*) to response
10. **Metrics**: Tracks rate limit hit/reject for monitoring

**Admin Dashboard Flow:**

1. **Frontend**: Admin views metrics dashboard
2. **API Request**: React Query fetches metrics from admin API
3. **Backend**: Aggregates metrics from Redis or metrics database
4. **Response**: Returns metrics data (total requests, blocked requests, top violators)
5. **Frontend**: Displays charts and statistics with auto-refresh

**Configuration Flow:**

1. **Frontend**: Admin creates/updates rate limit configuration
2. **API Request**: POST/PUT to admin config API
3. **Backend**: Validates and stores configuration
4. **Redis Update**: Updates rate limit rules (if stored in Redis)
5. **Response**: Returns updated configuration
6. **Frontend**: Updates UI and invalidates cache

**Complete Architecture Diagram:**

```
┌─────────────────────────────────────────────────────────────────────┐
│                        FRONTEND LAYER                                │
│  ┌──────────────────────────────────────────────────────────────┐  │
│  │              Admin Dashboard (React.js)                      │  │
│  │  ┌──────────────┐  ┌──────────────┐  ┌──────────────┐      │  │
│  │  │   React App  │  │  React Query │  │  React Router│      │  │
│  │  │  Components  │  │  (API State) │  │  (Routing)   │      │  │
│  │  └──────────────┘  └──────────────┘  └──────────────┘      │  │
│  │                                                               │  │
│  │  Components: MetricsDashboard, ConfigPanel, Analytics       │  │
│  └───────────────────────┬──────────────────────────────────────┘  │
└──────────────────────────┼──────────────────────────────────────────┘
                           │ HTTPS
                           ▼
┌─────────────────────────────────────────────────────────────────────┐
│                    CDN / EDGE LAYER                                  │
│  ┌──────────────────────────────────────────────────────────────┐  │
│  │         CloudFront / Cloudflare (Global CDN)                 │  │
│  │  - Static assets (JS, CSS, images)                           │  │
│  │  - DDoS protection                                           │  │
│  └───────────────────────┬──────────────────────────────────────┘  │
└──────────────────────────┼──────────────────────────────────────────┘
                           │
                           ▼
┌─────────────────────────────────────────────────────────────────────┐
│                  LOAD BALANCER LAYER                                 │
│  ┌──────────────────────────────────────────────────────────────┐  │
│  │              Nginx / AWS ALB                                  │  │
│  │  - SSL/TLS termination                                        │  │
│  │  - Request routing to API servers                             │  │
│  │  - Health checks and failover                                 │  │
│  └───────────────────────┬──────────────────────────────────────┘  │
└──────────────────────────┼──────────────────────────────────────────┘
                           │
              ┌────────────┴────────────┐
              │                         │
              ▼                         ▼
┌─────────────────────┐    ┌─────────────────────┐
│    API Server 1     │    │    API Server 2     │
│  Node.js/Express.js │    │  Node.js/Express.js │
│                     │    │                     │
│  ┌───────────────┐  │    │  ┌───────────────┐  │
│  │ Rate Limiter  │  │    │  │ Rate Limiter  │  │
│  │  Middleware   │  │    │  │  Middleware   │  │
│  │               │  │    │  │               │  │
│  │ 1. Extract ID │  │    │  │ 1. Extract ID │  │
│  │ 2. Check Redis│  │    │  │ 2. Check Redis│  │
│  │ 3. Increment  │  │    │  │ 3. Increment  │  │
│  │ 4. Allow/Deny │  │    │  │ 4. Allow/Deny │  │
│  └───────┬───────┘  │    │  └───────┬───────┘  │
│          │          │    │          │          │
│          │ Allow    │    │          │ Allow    │
│          ▼          │    │          ▼          │
│  ┌───────────────┐  │    │  ┌───────────────┐  │
│  │ API Handlers  │  │    │  │ API Handlers  │  │
│  └───────────────┘  │    │  └───────────────┘  │
└──────────┬──────────┘    └──────────┬──────────┘
           │                          │
           └────────────┬─────────────┘
                        │
                        ▼
┌─────────────────────────────────────────────────────────────────────┐
│                    REDIS CLUSTER LAYER                               │
│  ┌──────────────┐  ┌──────────────┐  ┌──────────────┐             │
│  │  Redis Node 1│  │  Redis Node 2│  │  Redis Node 3│             │
│  │              │  │              │  │              │             │
│  │ Rate Limit   │  │ Rate Limit   │  │ Rate Limit   │             │
│  │  Counters    │  │  Counters    │  │  Counters    │             │
│  │              │  │              │  │              │             │
│  │ Key: rate_   │  │ Key: rate_   │  │ Key: rate_   │             │
│  │ limit:ip:... │  │ limit:user:..│  │ limit:ip:... │             │
│  │ Value: 45    │  │ Value: 12    │  │ Value: 78    │             │
│  │ TTL: 60s     │  │ TTL: 300s    │  │ TTL: 60s     │             │
│  └──────────────┘  └──────────────┘  └──────────────┘             │
└─────────────────────────────────────────────────────────────────────┘

```

### Key Components

- **Rate Limiter Middleware**: Express.js middleware that intercepts requests, extracts identifiers, checks Redis, and allows/rejects requests
- **Identifier Extractor**: Extracts unique identifier (IP address, user ID, API key) from request for rate limiting
- **Algorithm Implementations**: Fixed window, sliding window, and token bucket algorithms for different rate limiting strategies
- **Redis Client**: Connection pool and pipelining for efficient Redis operations
- **Metrics Collector**: Tracks rate limit hits, rejects, and errors for monitoring
- **Configuration Manager**: Manages rate limit configurations per endpoint, user, or IP

---

# 3) Low Level Design (LLD)

## a) Frontend

### i) Component Architecture

Think of the frontend as a tree of React components - each component handles a specific part of the UI, and they work together to create the complete user experience.

**Component Hierarchy:**

```
App
├── Header
│   ├── Logo
│   └── Navigation
├── MainContent
│   ├── RateLimitMetricsDashboard
│   │   ├── OverviewCards
│   │   │   ├── TotalRequestsCard
│   │   │   ├── BlockedRequestsCard
│   │   │   └── BlockRateCard
│   │   ├── EndpointStatsTable
│   │   │   ├── EndpointRow
│   │   │   └── FilterControls
│   │   ├── TopBlockedIPsChart
│   │   └── RateLimitTrendsChart
│   ├── RateLimitConfigPanel
│   │   ├── ConfigForm
│   │   │   ├── EndpointInput
│   │   │   ├── WindowInput
│   │   │   ├── MaxRequestsInput
│   │   │   └── AlgorithmSelector
│   │   └── ConfigList
│   └── WhitelistBlacklistManager
│       ├── WhitelistTable
│       └── BlacklistTable
└── Footer

```

### Key React Components

**Frontend Implementation:**

```typescript
// Rate Limit Metrics Dashboard Component
const RateLimitMetricsDashboard: React.FC = () => {
  const [timeRange, setTimeRange] = useState('1h');
  const [selectedEndpoint, setSelectedEndpoint] = useState<string | null>(null);

  // Fetch rate limit metrics using React Query
  const { data: metrics, isLoading } = useQuery({
    queryKey: ['rateLimitMetrics', timeRange, selectedEndpoint],
    queryFn: async () => {
      const response = await axios.get('/api/admin/rate-limit/metrics', {
        params: { timeRange, endpoint: selectedEndpoint }
      });
      return response.data.data;
    },
    refetchInterval: 30000 // Refresh every 30 seconds
  });

  if (isLoading) return <LoadingSpinner />;

  return (
    <div className="rate-limit-dashboard">
      <OverviewCards
        totalRequests={metrics.totalRequests}
        blockedRequests={metrics.blockedRequests}
        blockRate={metrics.blockRate}
      />
      <EndpointStatsTable
        endpointStats={metrics.endpointStats}
        onEndpointSelect={setSelectedEndpoint}
      />
      <TopBlockedIPsChart data={metrics.topBlockedIPs} />
      <RateLimitTrendsChart data={metrics.trends} />
    </div>
  );
};

// Rate Limit Configuration Panel Component
const RateLimitConfigPanel: React.FC = () => {
  const [config, setConfig] = useState({
    endpoint: '',
    windowMs: 60000,
    maxRequests: 100,
    algorithm: 'fixed-window' as const,
    identifierType: 'ip' as const
  });

  const { mutate: createConfig, isPending } = useMutation({
    mutationFn: async (configData: typeof config) => {
      const response = await axios.post('/api/admin/rate-limit/config', configData);
      return response.data;
    },
    onSuccess: () => {
      // Invalidate and refetch configs list
      queryClient.invalidateQueries({ queryKey: ['rateLimitConfigs'] });
      }
  });

  const handleSubmit = (e: React.FormEvent) => {
    e.preventDefault();
    createConfig(config);
  };

  return (
    <div className="config-panel">
      <form onSubmit={handleSubmit}>
        <input
          type="text"
          placeholder="Endpoint (e.g., /api/users)"
          value={config.endpoint}
          onChange={(e) => setConfig({ ...config, endpoint: e.target.value })}
        />
        <input
          type="number"
          placeholder="Window (ms)"
          value={config.windowMs}
          onChange={(e) => setConfig({ ...config, windowMs: parseInt(e.target.value) })}
        />
        <input
          type="number"
          placeholder="Max Requests"
          value={config.maxRequests}
          onChange={(e) => setConfig({ ...config, maxRequests: parseInt(e.target.value) })}
        />
        <select
          value={config.algorithm}
          onChange={(e) => setConfig({ ...config, algorithm: e.target.value as any })}
        >
          <option value="fixed-window">Fixed Window</option>
          <option value="sliding-window">Sliding Window</option>
          <option value="token-bucket">Token Bucket</option>
        </select>
        <button type="submit" disabled={isPending}>
          {isPending ? 'Creating...' : 'Create Config'}
        </button>
      </form>
    </div>
  );
};

```

### ii) State Management

**State Management Strategy:**

- **Local State (useState)**: Form inputs, UI filters, selected endpoints, time range selection
- **Component State**: Each component manages its own UI state (loading, errors, selected filters)
- **API State**: React Query or SWR for server state (caching, refetching, optimistic updates) - rate limit metrics, configurations, whitelist/blacklist
- **Global State (Context/Redux)**: User authentication, admin permissions, theme preferences (if needed)

**Frontend Implementation:**

```typescript
// Using React Query for API state management
import { useQuery, useMutation, useQueryClient } from '@tanstack/react-query';

const useRateLimitMetrics = (timeRange: string, endpoint?: string) => {
  return useQuery({
    queryKey: ['rateLimitMetrics', timeRange, endpoint],
    queryFn: async () => {
      const response = await axios.get('/api/admin/rate-limit/metrics', {
        params: { timeRange, endpoint }
      });
      return response.data.data;
    },
    refetchInterval: 30000 // Refetch every 30 seconds for real-time updates
  });
};

const useRateLimitConfigs = () => {
  return useQuery({
    queryKey: ['rateLimitConfigs'],
    queryFn: async () => {
      const response = await axios.get('/api/admin/rate-limit/configs');
      return response.data.data;
    }
  });
};

const useCreateRateLimitConfig = () => {
  const queryClient = useQueryClient();

  return useMutation({
    mutationFn: async (config: RateLimitConfig) => {
      const response = await axios.post('/api/admin/rate-limit/config', config);
      return response.data;
    },
    onSuccess: () => {
      // Invalidate and refetch configs list
      queryClient.invalidateQueries({ queryKey: ['rateLimitConfigs'] });
    }
  });
};

```

### iii) Implementation Details

**Data Flow:**

1. **Dashboard Load** → RateLimitMetricsDashboard fetches metrics from API
2. **Filter Selection** → User selects time range or endpoint, triggers new API call
3. **Config Creation** → Admin creates new rate limit config, updates config list
4. **Real-time Updates** → Metrics refresh automatically every 30 seconds
5. **Whitelist/Blacklist** → Admin adds/removes entries, updates immediately

**Event Handling:**

- Time range selector triggers metrics refresh
- Endpoint filter updates displayed metrics
- Config form submission creates new rate limit rules
- Whitelist/blacklist actions update immediately with optimistic updates

**UI/UX Considerations:**

- **Loading States**: Show spinner during API calls, skeleton loaders for charts
- **Error Handling**: Display user-friendly error messages for failed API calls
- **Real-time Updates**: Auto-refresh metrics every 30 seconds, show last updated time
- **Responsive Design**: Mobile-friendly layout using CSS Grid/Flexbox, collapsible panels
- **Accessibility**: ARIA labels, keyboard navigation, screen reader support for charts and tables

---

## b) Backend

### i) Services

**Rate Limiter Service:**

```typescript
class RateLimiterService {
  async checkRateLimit(
    identifier: string,
    endpoint: string,
    algorithm: string,
    config: RateLimitConfig
  ): Promise<RateLimitResult> {
    // Check whitelist/blacklist first
    if (await this.isWhitelisted(identifier)) {
      return { allowed: true, remaining: Infinity, resetTime: new Date(), totalRequests: 0 };
    }
    if (await this.isBlacklisted(identifier)) {
      return { allowed: false, remaining: 0, resetTime: new Date(), totalRequests: 0 };
    }

    // Check rate limit based on algorithm
    switch (algorithm) {
      case 'fixed-window':
        return await this.checkFixedWindow(identifier, endpoint, config);
      case 'sliding-window':
        return await this.checkSlidingWindow(identifier, endpoint, config);
      case 'token-bucket':
        return await this.checkTokenBucket(identifier, endpoint, config);
      default:
        throw new Error(`Unknown algorithm: ${algorithm}`);
    }
  }

  async isWhitelisted(identifier: string): Promise<boolean> {
    return await redis.sismember('rate_limit:whitelist', identifier) === 1;
  }

  async isBlacklisted(identifier: string): Promise<boolean> {
    return await redis.sismember('rate_limit:blacklist', identifier) === 1;
  }
}

```

**Identifier Extractor Service:**

```typescript
class IdentifierExtractorService {
  extractIdentifier(req: express.Request, type: 'ip' | 'user' | 'api-key'): string {
    switch (type) {
      case 'ip':
        return req.ip || req.socket.remoteAddress || 'unknown';
      case 'user':
        return req.user?.id || req.headers['x-user-id'] || 'anonymous';
      case 'api-key':
        return req.headers['x-api-key'] || 'no-key';
      default:
        return req.ip || 'unknown';
    }
  }
}

```

**Metrics Service:**

```typescript
class MetricsService {
  async trackRateLimit(
    identifier: string,
    endpoint: string,
    allowed: boolean
  ): Promise<void> {
    const key = `metrics:rate_limit:${endpoint}`;
    if (allowed) {
      await redis.incr(`${key}:allowed`);
    } else {
      await redis.incr(`${key}:rejected`);
    }
    await redis.expire(key, 86400); // 24 hours
  }

  async getMetrics(endpoint?: string, timeRange?: string): Promise<MetricsData> {
    // Aggregate metrics from Redis
    // Return total requests, blocked requests, block rate, etc.
  }
}

```

### ii) Server Structure

**Express.js Server Structure:**

```
server/
├── middleware/
│   ├── rateLimiter.js          # Rate limiter middleware
│   ├── identifierExtractor.js  # Extract identifier from request
│   └── errorHandler.js         # Error handling middleware
├── services/
│   ├── RateLimiterService.js   # Core rate limiting logic
│   ├── IdentifierExtractorService.js
│   ├── MetricsService.js       # Metrics tracking
│   └── ConfigService.js        # Configuration management
├── algorithms/
│   ├── FixedWindow.js          # Fixed window algorithm
│   ├── SlidingWindow.js        # Sliding window algorithm
│   └── TokenBucket.js          # Token bucket algorithm
├── routes/
│   ├── api.js                  # API routes
│   └── admin.js                # Admin routes (metrics, config)
├── utils/
│   ├── redis.js                # Redis client and connection
│   └── logger.js               # Logging utilities
└── config/
    └── rateLimitConfig.js      # Default rate limit configurations

```

### iii) Implementation Details

### Rate Limit Configuration

```typescript
interface RateLimitConfig {
  windowMs: number;        // Time window in milliseconds (e.g., 60000 for 1 minute)
  maxRequests: number;     // Maximum requests allowed in window
  algorithm: 'fixed-window' | 'sliding-window' | 'token-bucket';
  identifier: 'ip' | 'user' | 'api-key' | 'custom';
  skipSuccessfulRequests?: boolean;  // Don't count successful requests
  skipFailedRequests?: boolean;      // Don't count failed requests
  message?: string;                  // Custom error message
}

```

### Rate Limit Result

```typescript
interface RateLimitResult {
  allowed: boolean;        // Whether request is allowed
  remaining: number;       // Requests remaining in window
  resetTime: Date;         // When the limit resets
  totalRequests: number;   // Total requests in current window
}

```

### Redis Key Structure

```typescript
// Format: rate_limit:{identifier_type}:{identifier_value}:{endpoint}
// Examples:
// rate_limit:ip:192.168.1.1:/api/users
// rate_limit:user:user123:/api/posts
// rate_limit:api_key:key456:/api/data

```

---

## Data APIs

**Note:** Rate limiter is typically implemented as middleware, but these are the API endpoints for rate limit management and status.

### GET /api/rate-limit/status

- **URL:** `/api/rate-limit/status`

- **Method:** GET

- **Description:** Get current rate limit status for the current user/IP

- **Response:**

  ```json
  {
    "success": true,
    "data": {
      "identifier": "192.168.1.1",
      "remaining": 95,
      "limit": 100,
      "resetTime": "2024-01-15T10:31:00Z",
      "windowMs": 60000
    }
  }

  ```

- **Status Codes:** 200 (Success)

### POST /api/admin/rate-limit/config

- **URL:** `/api/admin/rate-limit/config`

- **Method:** POST

- **Description:** Configure rate limits for specific endpoints (Admin only)

- **Request Body:**

  ```json
  {
    "endpoint": "/api/users",
    "windowMs": 60000,
    "maxRequests": 100,
    "algorithm": "sliding-window",
    "identifierType": "ip"
  }

  ```

- **Response:**

  ```json
  {
    "success": true,
    "data": {
      "endpoint": "/api/users",
      "windowMs": 60000,
      "maxRequests": 100,
      "algorithm": "sliding-window",
      "identifierType": "ip",
      "updatedAt": "2024-01-15T10:30:00Z"
    }
  }

  ```

- **Status Codes:** 200 (Success), 400 (Validation Error), 401 (Unauthorized), 403 (Forbidden)

### GET /api/admin/rate-limit/metrics

- **URL:** `/api/admin/rate-limit/metrics?endpoint=/api/users&timeRange=1h`

- **Method:** GET

- **Description:** Get rate limit metrics and statistics (Admin only)

- **Query Parameters:**
  - `endpoint`: string (optional) - Filter by endpoint
  - `timeRange`: string (optional) - Time range (1h, 24h, 7d)

- **Response:**

  ```json
  {
    "success": true,
    "data": {
      "totalRequests": 125000,
      "blockedRequests": 2500,
      "blockRate": 2.0,
      "topBlockedIPs": [
        { "ip": "192.168.1.100", "blockedCount": 150 },
        { "ip": "192.168.1.101", "blockedCount": 120 }
      ],
      "endpointStats": [
        {
          "endpoint": "/api/users",
          "totalRequests": 50000,
          "blockedRequests": 1000,
          "blockRate": 2.0
        }
      ]
    }
  }

  ```

- **Status Codes:** 200 (Success), 401 (Unauthorized), 403 (Forbidden)

---

## Backend Implementation Details

### Express.js Middleware Structure

The rate limiter is implemented as Express.js middleware that can be applied to routes:

```typescript
// Apply to specific route
app.get('/api/users', rateLimiter({ windowMs: 60000, maxRequests: 100 }), handler);

// Apply globally
app.use(rateLimiter({ windowMs: 60000, maxRequests: 1000 }));

```

### Redis Connection

```typescript
import Redis from 'ioredis';

const redis = new Redis({
  host: process.env.REDIS_HOST,
  port: parseInt(process.env.REDIS_PORT || '6379'),
  password: process.env.REDIS_PASSWORD,
  retryStrategy: (times) => {
    const delay = Math.min(times * 50, 2000);
    return delay;
  }
});

```

---

## Protocols

### Rate Limiting Protocol

**HTTP Headers:**

- `X-RateLimit-Limit`: Maximum requests allowed

- `X-RateLimit-Remaining`: Requests remaining in window

- `X-RateLimit-Reset`: Unix timestamp when limit resets

- `Retry-After`: Seconds to wait before retrying (when rate limited)

**Response Codes:**

- `200 OK`: Request allowed

- `429 Too Many Requests`: Rate limit exceeded

---

# 4) Algorithms

## Fixed Window Algorithm

**Purpose:** Simple time-based rate limiting that divides time into fixed windows and counts requests within each window.

**Algorithm:**

1. Divide time into fixed windows (e.g., 1-minute windows)
2. Count requests in current window using Redis counter
3. Reset counter at window boundary
4. Reject requests if count exceeds limit

**Implementation:**

```typescript
async function checkFixedWindow(
  identifier: string,
  windowMs: number,
  maxRequests: number
): Promise<RateLimitResult> {
  const now = Date.now();
  const windowStart = Math.floor(now / windowMs) * windowMs;
  const key = `rate_limit:fixed:${identifier}:${windowStart}`;

  // Get current count
  const current = await redis.get(key) || 0;
  const count = parseInt(current);

  if (count >= maxRequests) {
    const resetTime = new Date(windowStart + windowMs);
    return {
      allowed: false,
      remaining: 0,
      resetTime,
      totalRequests: count
    };
  }

  // Increment counter
  const newCount = await redis.incr(key);

  // Set TTL if this is first request in window
  if (newCount === 1) {
    await redis.expire(key, Math.ceil(windowMs / 1000));
  }

  return {
    allowed: true,
    remaining: maxRequests - newCount,
    resetTime: new Date(windowStart + windowMs),
    totalRequests: newCount
  };
}

```

**Complexity:**

- Time: O(1) - Single Redis GET and INCR operations
- Space: O(1) - One counter per identifier per window
- **Pros:** Simple to implement, low memory usage, fast (single Redis operation)
- **Cons:** Can allow bursts at window boundaries, less accurate than sliding window

---

## Sliding Window Algorithm

**Purpose:** More accurate rate limiting that tracks requests in a sliding time window, preventing bursts at window boundaries.

**Algorithm:**

1. Track requests in a sliding time window using Redis sorted sets
2. Remove old entries outside the window
3. Count requests in the current window
4. Reject requests if count exceeds limit

**Implementation:**

```typescript
async function checkSlidingWindow(
  identifier: string,
  windowMs: number,
  maxRequests: number
): Promise<RateLimitResult> {
  const now = Date.now();
  const key = `rate_limit:sliding:${identifier}`;

  // Remove old entries (outside window)
  const windowStart = now - windowMs;
  await redis.zremrangebyscore(key, 0, windowStart);

  // Count requests in window
  const count = await redis.zcard(key);

  if (count >= maxRequests) {
    // Get oldest request time to calculate reset time
    const oldest = await redis.zrange(key, 0, 0, 'WITHSCORES');
    const resetTime = new Date(parseInt(oldest[1]) + windowMs);

    return {
      allowed: false,
      remaining: 0,
      resetTime,
      totalRequests: count
    };
  }

  // Add current request
  await redis.zadd(key, now, `${now}-${Math.random()}`);
  await redis.expire(key, Math.ceil(windowMs / 1000));

  return {
    allowed: true,
    remaining: maxRequests - count - 1,
    resetTime: new Date(now + windowMs),
    totalRequests: count + 1
  };
}

```

**Complexity:**

- Time: O(log n) - Redis sorted set operations (zremrangebyscore, zcard, zadd)
- Space: O(n) - Stores all request timestamps in the window
- **Pros:** More accurate - prevents bursts at boundaries, smooth rate limiting
- **Cons:** More memory usage (stores all requests), more Redis operations (slower)

---

## Token Bucket Algorithm

**Purpose:** Rate limiting that allows bursts of traffic by maintaining a bucket of tokens that refill at a constant rate.

**Algorithm:**

1. Maintain a bucket with tokens (capacity)
2. Tokens refill at a constant rate over time
3. Each request consumes one token
4. Reject requests if bucket is empty

**Implementation:**

```typescript
async function checkTokenBucket(
  identifier: string,
  capacity: number,        // Max tokens in bucket
  refillRate: number       // Tokens per second
): Promise<RateLimitResult> {
  const key = `rate_limit:token:${identifier}`;
  const now = Date.now();

  // Get current bucket state
  const bucket = await redis.hmget(key, 'tokens', 'lastRefill');
  let tokens = parseFloat(bucket[0] || capacity);
  const lastRefill = parseInt(bucket[1] || now);

  // Refill tokens based on time passed
  const timePassed = (now - lastRefill) / 1000; // seconds
  tokens = Math.min(capacity, tokens + (timePassed * refillRate));

  if (tokens < 1) {
    // Calculate when next token will be available
    const tokensNeeded = 1 - tokens;
    const waitTime = tokensNeeded / refillRate;
    const resetTime = new Date(now + waitTime * 1000);

    return {
      allowed: false,
      remaining: 0,
      resetTime,
      totalRequests: 0
    };
  }

  // Consume token
  tokens -= 1;
  await redis.hmset(key, 'tokens', tokens, 'lastRefill', now);
  await redis.expire(key, Math.ceil(capacity / refillRate));

  return {
    allowed: true,
    remaining: Math.floor(tokens),
    resetTime: new Date(now + ((capacity - tokens) / refillRate * 1000)),
    totalRequests: 0
  };
}

```

**Complexity:**

- Time: O(1) - Redis hash operations (HMGET, HMSET)
- Space: O(1) - One hash entry per identifier storing tokens and last refill time
- **Pros:** Allows bursts (if tokens available), smooths out traffic, good for variable traffic patterns
- **Cons:** More complex to implement, more Redis operations than fixed window

---

### Basic Rate Limiter Middleware

```typescript
import express from 'express';
import Redis from 'ioredis';

const redis = new Redis(process.env.REDIS_URL);

interface RateLimitOptions {
  windowMs: number;
  maxRequests: number;
  algorithm: 'fixed-window' | 'sliding-window' | 'token-bucket';
  identifier?: (req: express.Request) => string;
  skipSuccessfulRequests?: boolean;
  message?: string;
}

function rateLimiter(options: RateLimitOptions) {
  return async (req: express.Request, res: express.Response, next: express.NextFunction) => {
    try {
      // Extract identifier (IP, user ID, etc.)
      const identifier = options.identifier
        ? options.identifier(req)
        : req.ip || req.socket.remoteAddress || 'unknown';

      // Check rate limit based on algorithm
      let result: RateLimitResult;

      switch (options.algorithm) {
        case 'fixed-window':
          result = await checkFixedWindow(identifier, options.windowMs, options.maxRequests);
          break;
        case 'sliding-window':
          result = await checkSlidingWindow(identifier, options.windowMs, options.maxRequests);
          break;
        case 'token-bucket':
          result = await checkTokenBucket(identifier, options.maxRequests, options.maxRequests / (options.windowMs / 1000));
          break;
      }

      // Add rate limit headers
      res.setHeader('X-RateLimit-Limit', options.maxRequests);
      res.setHeader('X-RateLimit-Remaining', result.remaining);
      res.setHeader('X-RateLimit-Reset', Math.floor(result.resetTime.getTime() / 1000));

      if (!result.allowed) {
        return res.status(429).json({
          error: options.message || 'Too many requests, please try again later',
          retryAfter: Math.ceil((result.resetTime.getTime() - Date.now()) / 1000)
        });
      }

      // Track successful request if needed
      if (options.skipSuccessfulRequests) {
        const originalSend = res.send;
        res.send = function(data) {
          if (res.statusCode < 400) {
            // Don't count successful requests
          }
          return originalSend.call(this, data);
        };
      }

      next();
    } catch (error) {
      // Fail-open: if rate limiter fails, allow request
      console.error('Rate limiter error:', error);
      next(); // Allow request if rate limiter fails
    }
  };
}

// Usage
app.use('/api/users', rateLimiter({
  windowMs: 60000,        // 1 minute
  maxRequests: 100,       // 100 requests per minute
  algorithm: 'fixed-window',
  identifier: (req) => req.user?.id || req.ip
}));

```

### Per-Endpoint Rate Limiting

```typescript
// Different limits for different endpoints
const rateLimitConfig = {
  '/api/login': {
    windowMs: 15 * 60 * 1000,  // 15 minutes
    maxRequests: 5,             // 5 login attempts per 15 minutes
    algorithm: 'sliding-window'
  },
  '/api/posts': {
    windowMs: 60000,            // 1 minute
    maxRequests: 10,            // 10 posts per minute
    algorithm: 'token-bucket'
  },
  '/api/search': {
    windowMs: 60000,            // 1 minute
    maxRequests: 30,            // 30 searches per minute
    algorithm: 'fixed-window'
  }
};

// Apply different limits per endpoint
Object.entries(rateLimitConfig).forEach(([path, config]) => {
  app.use(path, rateLimiter(config));
});

```

---

## Distributed Rate Limiting

### Redis-Based Distributed Limiting

**Challenge:** Multiple servers need to share rate limit state

**Solution:** Use Redis as shared storage

```typescript
// All servers connect to same Redis instance
// Rate limit counters stored in Redis
// All servers see same counts

// Example: Server 1 and Server 2 both check same Redis key
// Server 1: INCR rate_limit:ip:192.168.1.1 → returns 5
// Server 2: INCR rate_limit:ip:192.168.1.1 → returns 6
// Both see accurate count

```

### Redis Cluster for High Availability

```typescript
// Use Redis Cluster for high availability
const redis = new Redis.Cluster([
  { host: 'redis1.example.com', port: 6379 },
  { host: 'redis2.example.com', port: 6379 },
  { host: 'redis3.example.com', port: 6379 }
]);

```

---

## Advanced Features

### Whitelist and Blacklist

```typescript
async function isWhitelisted(identifier: string): Promise<boolean> {
  return await redis.sismember('rate_limit:whitelist', identifier) === 1;
}

async function isBlacklisted(identifier: string): Promise<boolean> {
  return await redis.sismember('rate_limit:blacklist', identifier) === 1;
}

// In middleware
if (await isWhitelisted(identifier)) {
  return next(); // Skip rate limiting
}

if (await isBlacklisted(identifier)) {
  return res.status(403).json({ error: 'Access denied' });
}

```

### Dynamic Rate Limiting

```typescript
// Adjust limits based on system load
async function getDynamicLimit(baseLimit: number): Promise<number> {
  const cpuUsage = await getCPUUsage();
  const memoryUsage = await getMemoryUsage();

  if (cpuUsage > 80 || memoryUsage > 80) {
    // Reduce limit under high load
    return Math.floor(baseLimit * 0.5);
  }

  return baseLimit;
}

```

### Rate Limit Headers

```typescript
// Standard rate limit headers
res.setHeader('X-RateLimit-Limit', maxRequests);        // Total limit
res.setHeader('X-RateLimit-Remaining', remaining);      // Requests left
res.setHeader('X-RateLimit-Reset', resetTimestamp);     // When limit resets
res.setHeader('Retry-After', secondsUntilReset);        // Seconds to wait

```

---

## Monitoring and Metrics

### Track Rate Limit Metrics

```typescript
// Track metrics for monitoring
async function trackRateLimitMetrics(
  identifier: string,
  endpoint: string,
  allowed: boolean
) {
  const key = `metrics:rate_limit:${endpoint}`;

  if (allowed) {
    await redis.incr(`${key}:allowed`);
  } else {
    await redis.incr(`${key}:rejected`);
  }

  // Set TTL for metrics (e.g., 24 hours)
  await redis.expire(key, 86400);
}

```

### Alerting

```typescript
// Alert if too many requests are being rejected
async function checkRateLimitAlerts() {
  const rejected = await redis.get('metrics:rate_limit:/api/login:rejected');
  const allowed = await redis.get('metrics:rate_limit:/api/login:allowed');

  const rejectionRate = rejected / (rejected + allowed);

  if (rejectionRate > 0.1) { // More than 10% rejection
    sendAlert('High rate limit rejection rate detected');
  }
}

```

---

## Error Handling

### Fail-Open Strategy

```typescript
// If Redis is down, allow requests (don't block everything)
try {
  const result = await checkRateLimit(identifier);
  // Process result
} catch (error) {
  console.error('Rate limiter error:', error);
  // Fail-open: allow request
  next();
}

```

### Graceful Degradation

```typescript
// Fallback to in-memory rate limiting if Redis is down
let redisAvailable = true;

async function checkRateLimitWithFallback(identifier: string) {
  try {
    return await checkRateLimitRedis(identifier);
  } catch (error) {
    redisAvailable = false;
    // Fallback to in-memory (per-server, not distributed)
    return checkRateLimitMemory(identifier);
  }
}

```

---

# 5) Data Models

## Rate Limit Config Collection (MongoDB)

```javascript
{
  _id: ObjectId,
  configId: String,        // Unique config ID, indexed
  endpoint: String,        // API endpoint pattern, indexed
  windowMs: Number,        // Time window in milliseconds
  maxRequests: Number,     // Maximum requests allowed
  algorithm: String,       // fixed-window, sliding-window, token-bucket
  identifierType: String,  // ip, user, api-key
  whitelist: [String],     // Array of whitelisted identifiers
  blacklist: [String],     // Array of blacklisted identifiers
  enabled: Boolean,        // Whether config is enabled
  createdAt: Date,
  updatedAt: Date
}

// Indexes:
// - { configId: 1 } (unique)
// - { endpoint: 1 } (indexed)
// - { enabled: 1 } (indexed)

```

## Rate Limit Metrics Collection (MongoDB)

```javascript
{
  _id: ObjectId,
  metricId: String,        // Unique metric ID, indexed
  endpoint: String,        // API endpoint, indexed
  identifier: String,      // IP, user ID, or API key
  timestamp: Date,         // Metric timestamp, indexed
  allowed: Number,         // Number of allowed requests
  rejected: Number,        // Number of rejected requests
  createdAt: Date
}

// Indexes:
// - { metricId: 1 } (unique)
// - { endpoint: 1, timestamp: -1 } (compound)
// - { timestamp: 1 } (indexed for time-based queries)

```

---

# 6) Database Transactions and Consistency

### MongoDB Transactions

**Transaction Usage:**

- **Multi-Document Transactions** - For operations requiring ACID guarantees
- **Example:** Rate limit config update + metrics logging in single transaction
- **Session Management:** Use MongoDB sessions for transaction control

**Example:**

```typescript
const session = await mongoose.startSession();
session.startTransaction();
try {
  await RateLimitConfig.updateOne({ configId }, { $set: { maxRequests: 200 } }, { session });
  await RateLimitMetrics.create([{ endpoint, allowed: 100, rejected: 0 }], { session });
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

- **Config Consistency:** Use transactions for config updates to ensure atomicity
- **Metrics Consistency:** Ensure metrics are logged consistently
- **Redis Consistency:** Redis atomic operations ensure rate limit counter consistency
- **Eventual Consistency:** Accept eventual consistency for metrics aggregation (may update with slight delay)

---

# 7) Protocols

### REST API Protocol

- **Protocol:** REST (Representational State Transfer)
- **Data Format:** JSON
- **HTTP Methods:** GET, POST, PUT, DELETE
- **Status Codes:** 200 (Success), 201 (Created), 400 (Bad Request), 401 (Unauthorized), 403 (Forbidden), 429 (Too Many Requests), 500 (Server Error)
- **Authentication:** JWT Bearer token in Authorization header

### Rate Limiting Headers

- **X-RateLimit-Limit:** Maximum requests allowed
- **X-RateLimit-Remaining:** Requests remaining in window
- **X-RateLimit-Reset:** Unix timestamp when limit resets
- **Retry-After:** Seconds to wait before retrying (when rate limited)

---

# 8) API Design

### GET /api/rate-limit/status

- **URL:** `/api/rate-limit/status?endpoint=/api/users`
- **Method:** GET
- **Description:** Get current rate limit status
- **Response:**

  ```json
  {
    "success": true,
    "data": {
      "identifier": "192.168.1.1",
      "endpoint": "/api/users",
      "remaining": 95,
      "limit": 100,
      "resetTime": "2024-01-15T10:31:00Z",
      "windowMs": 60000
    }
  }

  ```

- **Status Codes:** 200 (Success), 401 (Unauthorized)

### POST /api/admin/rate-limit/config

- **URL:** `/api/admin/rate-limit/config`
- **Method:** POST
- **Description:** Configure rate limits for endpoints (Admin only)
- **Request Body:**

  ```json
  {
    "endpoint": "/api/users",
    "windowMs": 60000,
    "maxRequests": 100,
    "algorithm": "sliding-window",
    "identifierType": "ip"
  }

  ```

- **Response:**

  ```json
  {
    "success": true,
    "data": {
      "configId": "config_abc123",
      "endpoint": "/api/users",
      "windowMs": 60000,
      "maxRequests": 100,
      "algorithm": "sliding-window"
    }
  }

  ```

- **Status Codes:** 201 (Created), 400 (Validation Error), 403 (Forbidden)

---

# 9) Caching Strategy

### Redis Cache

**Cache Strategy:**

- **Key Format:** `rate_limit:fixed:{identifier}:{windowStart}`, `rate_limit:sliding:{identifier}`, `rate_limit:token:{identifier}`
- **Value:** Counter values, sorted sets, hash values
- **TTL:**
  - Fixed window counters: Window duration
  - Sliding window sets: Window duration
  - Token bucket hashes: Calculated based on refill rate
- **Eviction Policy:** TTL-based eviction

**Cache Patterns:**

- **Write-Through Pattern:** Update Redis counters immediately on each request
- **Cache-Aside Pattern:** Check Redis for rate limit status, update on request
- **Cache Invalidation:** Counters expire automatically via TTL

---

# 10) Error Handling

### Error Scenarios and Responses

**Edge Cases Handling:**

- **Redis Connection Failure:** Fail-open strategy - allow requests if Redis is down
- **Invalid Configuration:** Return 400 Bad Request with validation errors
- **Rate Limit Exceeded:** Return 429 Too Many Requests with Retry-After header
- **Unauthorized Access:** Return 403 Forbidden for admin endpoints
- **Invalid Algorithm:** Return 400 Bad Request with supported algorithms list

**Error Response Format:**

```json
{
  "error": {
    "code": "RATE_LIMIT_EXCEEDED",
    "message": "Too many requests",
    "details": "Rate limit of 100 requests per minute exceeded",
    "retryAfter": 30
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

**Redis Scaling:**

- **Redis Cluster:** Use Redis cluster for high availability and performance
- **Connection Pooling:** Use connection pooling to manage Redis connections
- **Pipelining:** Use Redis pipelining to batch operations

**Database Scaling:**

- **Read Replicas:** Deploy read replicas for metrics queries
- **Sharding:** Shard metrics by endpoint or timestamp for write scaling
- **Connection Pooling:** Use connection pooling to manage database connections

**Caching:**

- Distributed Redis cluster for high availability
- Cache rate limit counters and configurations
- Reduces database load significantly

### Availability

**Replication:**

- Redis replication ensures rate limit data availability
- Database replication ensures metrics availability
- Multi-region replication for disaster recovery

**Failover:**

- Automated failover mechanisms for Redis and database
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
- **Health Checks:** Verify rate limit endpoints are healthy
- **Blue-Green Deployment:** Maintain two identical production environments

### Database Deployment

**MongoDB Setup:**

- **MongoDB Atlas** - Managed MongoDB service with automatic backups
- **Backup Strategy:** Daily automated backups with point-in-time recovery
- **Indexing:** Proper indexes on configId, endpoint, timestamp
- **Replication:** Replica sets for high availability

**Redis Setup:**

- **Redis Cloud / AWS ElastiCache** - Managed Redis service
- **Cluster Mode:** Redis cluster for high availability and performance
- **Persistence:** RDB snapshots and AOF for data durability

---

# 12) Security Considerations

### Rate Limiting

- Implement rate limiting on admin endpoints to prevent abuse
- Use Redis for distributed rate limiting across multiple servers
- Monitor and alert on unusual rate limit patterns

### Input Validation

- Validate all API inputs (config data, endpoint patterns)
- Sanitize user input to prevent injection attacks
- Validate rate limit configuration parameters

### HTTPS/TLS

- All communication between clients and API encrypted using HTTPS
- Prevents eavesdropping and man-in-the-middle attacks
- SSL/TLS certificates for secure connections

### Authentication and Authorization

- **JWT Tokens:** Use JWT for stateless authentication
- **Token Expiration:** Set appropriate token expiration times
- **Role-Based Access Control:** Implement RBAC for admin vs user access
- **Admin Access Control:** Verify user has admin role before allowing config changes

### Security Headers

- **Rate Limit Headers:** Include rate limit information in response headers
- **Security Headers:** Set appropriate security headers (X-Content-Type-Options, X-Frame-Options)

### Monitoring and Alerts

- Set up monitoring for unusual rate limit patterns
- Trigger alerts for potential abuse or attacks
- Track metrics: rate limit violations, rejected requests, abuse patterns
- Log all rate limit operations for security auditing

---

# 3) Interview Answers

---

## Q1. 💡 Most complex technical challenge in building the rate limiter

**Situation:** Building a distributed rate limiting system that works across multiple Node.js servers, handles thousands of requests per second, supports multiple algorithms, and ensures accurate rate limiting without significant performance overhead.

**Action:** **Backend (Node.js/Express.js):** The most complex challenge was implementing distributed rate limiting that maintains accuracy across multiple servers while keeping overhead minimal. I implemented a **Redis-based solution** where all servers share rate limit counters in Redis - think of Redis as a shared whiteboard that all servers can read and write to. I used **atomic operations** (INCR, EXPIRE) to ensure accurate counting even with concurrent requests from multiple servers. I implemented **multiple algorithms** - fixed window for simplicity, sliding window for accuracy, and token bucket for burst handling. I created a **middleware architecture** in Express.js that intercepts requests, extracts identifiers (IP, user ID, API key), checks rate limits in Redis, and allows or rejects requests. I implemented **fail-open strategy** - if Redis is down, requests are allowed to prevent system-wide failure. I added **performance optimization** - rate limit check completes in < 10ms using Redis pipelining and connection pooling.

**Result:** Successfully delivered a distributed rate limiting system that handles thousands of requests per second. Rate limiting is 99.9% accurate across multiple servers. Overhead is minimal (< 10ms per request). The system prevents API abuse effectively. Zero false positives or negatives.

**Takeaway:** Distributed rate limiting requires shared state (Redis) with atomic operations. Multiple algorithms serve different use cases. Fail-open strategy prevents system-wide failure. Performance optimization is crucial - use Redis pipelining and connection pooling.

---

## Q2. 🟢 Implementing distributed rate limiting across multiple Node.js servers using Redis

**Situation:** Multiple Express.js servers needed to share rate limit state to ensure accurate rate limiting - if a user makes requests to different servers, they should all count toward the same limit.

**Action:** **Backend (Node.js/Express.js):** I implemented a Redis-based distributed rate limiting solution. I used Redis as shared storage - all Express.js servers connect to the same Redis instance. I implemented atomic operations - used Redis INCR command which is atomic, ensuring accurate counting even with concurrent requests. I created unique keys for each identifier (IP, user ID, endpoint) - format: `rate_limit:${type}:${identifier}:${endpoint}`. I used Redis TTL for automatic expiration - counters expire after the time window, no manual cleanup needed. I implemented Redis pipelining to batch multiple Redis operations and reduce round trips. I used Redis connection pooling for better performance. I added Redis failover handling - if Redis is down, system falls back to in-memory rate limiting (per-server, not distributed) or allows requests (fail-open). **Frontend (React.js):** The frontend remains unchanged as rate limiting is transparent to end users - they only see rate limit headers in API responses.

**Result:** Distributed rate limiting works accurately across multiple servers. All servers see the same rate limit counts. Atomic operations ensure no race conditions. System handles thousands of requests per second. Redis connection pooling improves performance.

**Takeaway:** Redis is ideal for distributed rate limiting due to atomic operations and TTL support. Use atomic operations (INCR) for accurate counting. Implement failover handling for Redis downtime. Connection pooling improves performance.

---

## Q3. ⚙️ Different rate limiting algorithms and when to use each

**Situation:** Different use cases required different rate limiting strategies - some needed simple time-based limits, others needed burst handling, and some needed smooth rate limiting.

**Action:** **Backend (Node.js/Express.js):** I implemented three different algorithms, each with specific use cases:

**1. Fixed Window Algorithm:**

- Divides time into fixed windows (e.g., 1-minute windows)

- Counts requests in current window, resets at window boundary

- **Use case:** Simple rate limiting, low memory usage

- **Pros:** Simple, fast, low memory

- **Cons:** Allows bursts at window boundaries

**2. Sliding Window Algorithm:**

- Tracks requests in a sliding time window

- Uses Redis sorted sets (ZSET) to store request timestamps

- Removes old entries outside window, counts remaining

- **Use case:** More accurate rate limiting, prevents boundary bursts

- **Pros:** Accurate, smooth rate limiting

- **Cons:** More memory usage, more Redis operations

**3. Token Bucket Algorithm:**

- Bucket has tokens (capacity), tokens refill at constant rate

- Request consumes one token, rejected if bucket empty

- Uses Redis hash to store bucket state (tokens, last refill time)

- **Use case:** Allows bursts, smooths out traffic

- **Pros:** Allows bursts, good for variable traffic

- **Cons:** More complex, more Redis operations

I created a **configurable system** where each endpoint can use a different algorithm based on requirements.

**Result:** System supports multiple algorithms for different use cases. Fixed window for simple cases, sliding window for accuracy, token bucket for burst handling. Developers can choose the right algorithm for their needs. All algorithms work accurately in distributed environment.

**Takeaway:** Different algorithms serve different use cases. Fixed window is simple but allows bursts. Sliding window is accurate but uses more memory. Token bucket allows bursts and smooths traffic. Make the system configurable.

---

## Q4. 🔌 Ensuring the rate limiter doesn't slow down API requests significantly

**Situation:** Rate limiting check needed to be fast (< 10ms) to avoid impacting API response times, especially for high-traffic endpoints.

**Action:** **Backend (Node.js/Express.js):** I implemented several performance optimizations. I used **Redis pipelining** to batch multiple Redis operations (get count, increment, set TTL) into a single round trip. I implemented **Redis connection pooling** to reuse connections and avoid connection overhead. I used **atomic Redis operations** (INCR) which are fast and eliminate the need for separate get-increment-set operations. I stored **rate limit data in Redis memory** for sub-millisecond access. I implemented **lazy evaluation** - only check rate limit for protected endpoints, skip for public endpoints. I added **caching** for rate limit configurations to avoid repeated lookups. I used **async/await** properly to avoid blocking the event loop. I implemented **early rejection** - if limit exceeded, reject immediately without additional processing. I added **performance monitoring** to track rate limit check times.

**Result:** Rate limit check completes in < 10ms (average 5-7ms). API response times are not significantly impacted. System handles thousands of requests per second. Performance is consistent under load. Overhead is minimal.

**Takeaway:** Performance is crucial for rate limiting. Use Redis pipelining to reduce round trips. Connection pooling improves performance. Atomic operations are faster than separate operations. Monitor performance metrics.

---

## Q5. 💡 Handling rate limiter failures (fail-open vs fail-closed)

**Situation:** Rate limiter could fail (Redis down, network issues) - system needed to decide whether to allow or reject requests when rate limiter is unavailable.

**Action:** **Backend (Node.js/Express.js):** I implemented a **fail-open strategy** - if rate limiter fails, requests are allowed. I added **error handling** in the middleware - if Redis operation fails, catch the error, log it, and call `next()` to allow the request. I implemented **fallback mechanism** - if Redis is down, fall back to in-memory rate limiting (per-server, not distributed) for basic protection. I added **health checks** to detect Redis availability. I implemented **circuit breaker pattern** - if Redis fails repeatedly, temporarily disable rate limiting and allow requests. I added **monitoring and alerting** to notify when rate limiter fails. I implemented **graceful degradation** - system continues to function even if rate limiting is unavailable.

**Result:** System never blocks all users due to rate limiter failure. Fail-open strategy ensures availability. Fallback provides basic protection. Monitoring alerts on failures. System is resilient to Redis downtime.

**Takeaway:** Fail-open strategy is better for availability - better to allow some extra requests than block all users. Implement fallback mechanisms. Monitor and alert on failures. Circuit breaker prevents cascading failures.
