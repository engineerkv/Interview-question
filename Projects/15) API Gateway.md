# API Gateway

> **Project Type:** System Design
> **Scale:** Handle 1B+ requests per day, route to 100+ microservices
> **Tech Stack:** Node.js, Load Balancer, Service Discovery, Redis

# 1) Problem Statement

Design and implement an API Gateway that addresses the following challenges:

- **Core Functionality**: Act as a single entry point for all client requests, route them to appropriate microservices, and provide cross-cutting concerns like authentication, rate limiting, request/response transformation, and monitoring
- **Scale Requirements**: Handle 1B+ requests per day, route to 100+ microservices, millions of concurrent requests, and traffic spikes
- **Performance**: Minimal latency overhead (< 10ms), fast request routing, efficient request/response transformation
- **Request Routing**: Route requests to appropriate microservices based on URL patterns, support service discovery, handle load balancing
- **Security**: Implement authentication and authorization, enforce rate limiting, protect against DDoS attacks, validate requests
- **API Management**: Support API versioning, request/response transformation, protocol translation (HTTP, gRPC, WebSocket)
- **Monitoring**: Provide comprehensive logging and monitoring, track latency and error rates, support distributed tracing
- **Reliability**: 99.9% availability, handle service failures gracefully, implement circuit breakers, prevent cascading failures

---

# 2) High Level Design (HLD)

## a) Requirements

### i) Functional Requirements

- Request routing to microservices

- Authentication and authorization

- Rate limiting

- Request/response transformation

- API versioning

- Request logging and monitoring

### ii) Non-Functional Requirements

- Latency overhead < 10ms

- 99.9% availability

- Support multiple protocols (HTTP, gRPC, WebSocket)

---

## b) Scope and Priority

### Phase 1: MVP (Must Have) - Priority 1

- Core functionality

- Basic features

### Phase 2: Enhanced Features - Priority 2

- Additional capabilities

- Performance improvements

### Phase 2: Enhanced Features - Priority 2

- Advanced rate limiting strategies

- Request/response caching

- API analytics and reporting

- Advanced security features (WAF, DDoS protection)

- Service mesh integration

---

## c) Technology Choices

### Backend Framework

- **Node.js with Express.js** - Request routing and transformation

### Service Discovery

- **Service Registry** - Dynamic service discovery

- **Load Balancer** - Distribute requests to backend services

### Caching

- **Redis** - Cache responses and rate limit data

### Additional Services

- **Circuit Breaker** - Prevent cascading failures

- **Monitoring** - Track latency and error rates

---

## d) Capacity Estimation

### Throughput Requirements

- **Total Requests per Day**: 1 billion requests
- **Peak Traffic**: 3x average during peak hours (3 billion requests per day)
- **Microservices**: 100+ microservices
- **Average Requests per Service**: 10 million requests per day per service
- **Read:Write Ratio**: 10:1 (read requests vs write requests)

**Calculations:**
- **Average Requests Per Second (RPS)**: 1B requests / 86,400 seconds ≈ 11,574 RPS
- **Peak RPS**: 11,574 × 3 = 34,722 RPS
- **Concurrent Connections**: 1 million concurrent connections
- **Requests per Microservice**: 11,574 / 100 ≈ 116 RPS per service (average)

### Storage Estimation

**Storage per Request:**
- Request log: 500 bytes (method, path, headers, timestamp)
- Response log: 500 bytes (status, headers, timestamp)
- **Total per Request**: ~1 KB

**Storage Requirements:**
- **Requests per Year**: 1B requests/day × 365 = 365 billion requests
- **Log Storage**: 365B × 1 KB ≈ 365 TB per year
- **Configuration Data**: 100 services × 10 KB ≈ 1 MB
- **Rate Limit Data**: 1B users × 100 bytes ≈ 100 GB
- **Total Storage**: ~365 TB (logs) + 1 MB (config) + 100 GB (rate limits) ≈ 365.1 TB/year

### Bandwidth Estimation

- **Average Request Size**: 2 KB per request
- **Average Response Size**: 5 KB per response
- **Daily Bandwidth**: 1B requests × (2 KB + 5 KB) = 7 TB/day
- **Peak Bandwidth**: 7 TB × 3 = 21 TB/day during peak hours
- **Average Bandwidth**: 7 TB / 86,400 seconds ≈ 81 MB/s
- **Peak Bandwidth**: 81 MB/s × 3 ≈ 243 MB/s

### Caching Estimation

Following the **80-20 rule** where 20% of requests generate 80% of traffic:
- **Cache 20% of popular requests**: 1B × 0.2 = 200M requests
- **Cache memory required**: 200M × 5 KB (response) = 1 TB (distributed across Redis cluster)
- **Cache hit ratio**: 50% (50% of requests served from cache)
- **Requests hitting Backend**: 11,574 × 0.50 ≈ 5,787 RPS (manageable with load balancing)

### Infrastructure Sizing

- **API Gateway Instances**: 1,000-2,000 instances behind load balancer, each handling 20-50 RPS
- **Load Balancer**: Multiple load balancers for high availability
- **Service Discovery**: Consul/Eureka cluster with 5-10 nodes
- **Cache Layer**: Redis cluster with 50-100 nodes for high availability and performance
- **Monitoring**: Prometheus/Grafana for metrics and monitoring
- **Logging**: ELK stack (Elasticsearch, Logstash, Kibana) for log aggregation

---

## e) Architecture Overview

The system follows an API Gateway architecture with request routing, authentication, rate limiting, and distributed service management. Here's how the complete system works:

### Frontend Architecture

**Frontend Layers:**

1. **Presentation Layer (React Components)**
   - **UI Components**: Reusable components (APIExplorer, RequestBuilder, ResponseViewer, MonitoringDashboard)
   - **Feature Components**: APIDocumentation, RequestTester, AnalyticsDashboard, LogViewer
   - **Layout Components**: Header, Sidebar, Navigation, MainLayout
   - **Page Components**: DashboardPage, APIPage, MonitoringPage, LogsPage

2. **State Management Layer**
   - **Local State (useState)**: Component-specific UI state (request inputs, loading, errors)
   - **Server State (Redux Toolkit)**: Global state for API configurations, monitoring data
   - **API State (React Query)**: API response caching, refetching

3. **API Integration Layer**
   - **API Client**: Axios instance with interceptors for auth, error handling
   - **Redux Thunks**: Async actions for API operations (testAPI, getMetrics, getLogs)
   - **Request/Response Transformation**: Data normalization and error handling

4. **Routing Layer (React Router)**
   - **Route Configuration**: Define routes and protected routes
   - **Navigation**: Programmatic and declarative navigation
   - **Route Guards**: Authentication and authorization checks

5. **Build & Deployment Layer**
   - **Build Process**: Webpack/Vite bundling with code splitting
   - **Static Assets**: Served from CDN (CloudFront/Cloudflare)
   - **Environment Configuration**: Environment-specific API endpoints and configs

**Frontend Request Flow:**

1. **User Interaction** → User makes API request or views monitoring dashboard
2. **State Update** → Redux action dispatched or React Query mutation triggered
3. **API Call** → Axios makes HTTP request to API Gateway
4. **Response Handling** → Success/error state updates Redux store or React Query cache
5. **UI Update** → Components re-render with new data

### Backend Architecture

**Backend Layers:**

1. **Load Balancer Layer** - Distributes incoming requests across API Gateway instances
2. **API Gateway Layer** - Request routing, authentication, rate limiting, transformation
3. **Service Discovery Layer** - Dynamic service discovery and health checking
4. **Routing Layer** - Route requests to appropriate microservices
5. **Middleware Layer** - Authentication, authorization, rate limiting, logging
6. **Cache Layer** - In-memory caching for responses and rate limit data
7. **Monitoring Layer** - Metrics collection, logging, distributed tracing

### Complete Request Flow

**Request Routing Flow:**
1. **Client**: Sends HTTP request to API Gateway
2. **Load Balancer**: Distributes request to available API Gateway instance
3. **Authentication**: Validate JWT token or API key
4. **Rate Limiting**: Check rate limits for client
5. **Routing**: Determine target microservice based on URL pattern
6. **Service Discovery**: Find healthy instance of target microservice
7. **Request Transformation**: Transform request if needed
8. **Forward Request**: Forward request to microservice
9. **Response Transformation**: Transform response if needed
10. **Logging**: Log request and response
11. **Response**: Return response to client

**Service Discovery Flow:**
1. **Service Registration**: Microservice registers with service registry
2. **Health Checks**: Service registry performs health checks
3. **Service Lookup**: API Gateway queries service registry for available instances
4. **Load Balancing**: Select instance using load balancing algorithm
5. **Request Forwarding**: Forward request to selected instance

**Circuit Breaker Flow:**
1. **Monitor**: Monitor error rates and latency for each service
2. **Threshold**: If error rate exceeds threshold, open circuit breaker
3. **Fail Fast**: Return error immediately without calling service
4. **Recovery**: Periodically attempt to close circuit breaker
5. **Half-Open**: Test service with limited requests
6. **Close**: If successful, close circuit breaker and resume normal operation

### Key Components

- **Frontend (React.js)**: Single-page application for API management, component-based architecture, Redux for state management
- **Load Balancer**: Distributes requests across API Gateway instances, SSL/TLS termination
- **API Gateway Instances**: Stateless design for horizontal scaling, handle request routing, authentication, rate limiting
- **Service Discovery**: Consul/Eureka for dynamic service discovery, health checking, load balancing
- **Middleware**: Authentication middleware, rate limiting middleware, logging middleware, transformation middleware
- **Cache Layer (Redis)**: In-memory cache for responses (20% of traffic), rate limit data, service registry cache
- **Monitoring**: Prometheus for metrics, ELK stack for logging, distributed tracing for request tracking
- **Microservices**: 100+ backend microservices handling business logic

---

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

1. **Load Balancing:** Route requests to healthy service instances

2. **Circuit Breaker:** Prevent cascading failures

3. **Caching:** Cache responses to reduce backend load

4. **Service Discovery:** Dynamic service discovery

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
│   │   │   ├── LatencyChart
│   │   │   ├── ErrorRateChart
│   │   │   └── ServiceHealthStatus
│   │   └── RecentActivity
│   ├── RoutesPage
│   │   ├── RouteList
│   │   │   └── RouteCard
│   │   │       ├── RoutePath
│   │   │       ├── TargetService
│   │   │       ├── Method
│   │   │       └── Actions (Edit, Delete)
│   │   └── CreateRouteButton
│   ├── RouteConfigurationPage
│   │   ├── RouteForm
│   │   │   ├── PathInput
│   │   │   ├── MethodSelector
│   │   │   ├── TargetServiceSelector
│   │   │   ├── AuthenticationToggle
│   │   │   ├── RateLimitConfig
│   │   │   └── SaveButton
│   │   └── AdvancedOptions
│   ├── RateLimitsPage
│   │   ├── RateLimitList
│   │   │   └── RateLimitCard
│   │   │       ├── RoutePath
│   │   │       ├── Limit
│   │   │       ├── Window
│   │   │       └── Actions
│   │   └── CreateRateLimitButton
│   ├── ServicesPage
│   │   ├── ServiceList
│   │   │   └── ServiceCard
│   │   │       ├── ServiceName
│   │   │       ├── HealthStatus
│   │   │       ├── InstanceCount
│   │   │       └── Metrics
│   │   └── ServiceDiscoveryStatus
│   └── AnalyticsPage
│       ├── RequestLogs
│       ├── ErrorLogs
│       └── PerformanceMetrics
└── Footer

```

### Key React Components

**Frontend Implementation:**

```typescript
// Route Configuration Component
const RouteConfigurationPage: React.FC<{ routeId?: string }> = ({ routeId }) => {
  const [routeConfig, setRouteConfig] = useState<RouteConfig>({
    path: '',
    method: 'GET',
    targetService: '',
    requiresAuth: false,
    rateLimit: { limit: 100, window: '1m' }
  });
  const saveRouteMutation = useSaveRoute();

  const handleSave = () => {
    saveRouteMutation.mutate(routeConfig);
  };

  return (
    <div className="route-configuration">
      <RouteForm
        config={routeConfig}
        onChange={setRouteConfig}
      />
      <button onClick={handleSave} disabled={saveRouteMutation.isLoading}>
        {saveRouteMutation.isLoading ? 'Saving...' : 'Save Route'}
      </button>
    </div>
  );
};

// Service Health Card Component
const ServiceCard: React.FC<{ service: Service }> = ({ service }) => {
  return (
    <div className="service-card">
      <div className="service-header">
        <h3>{service.name}</h3>
        <span className={`health-status ${service.health}`}>{service.health}</span>
      </div>
      <div className="service-info">
        <div>Instances: {service.instanceCount}</div>
        <div>Requests/min: {service.requestRate}</div>
        <div>Avg Latency: {service.avgLatency}ms</div>
      </div>
    </div>
  );
};

```

### State Management

**State Management Strategy:**

- **Local State (useState)**: Form inputs, UI state (loading, errors, filters)
- **Component State**: Each component manages its own UI state
- **API State**: React Query or SWR for server state (routes, services, metrics) - caching, refetching
- **Global State (Redux Toolkit)**: User authentication, dashboard preferences

**Frontend Implementation:**

```typescript
// Using React Query for API state management
import { useQuery, useMutation, useQueryClient } from '@tanstack/react-query';

const useRoutes = () => {
  return useQuery({
    queryKey: ['routes'],
    queryFn: async () => {
      const response = await axios.get('/api/v1/gateway/routes');
      return response.data;
    },
    staleTime: 30 * 1000 // Cache for 30 seconds
  });
};

const useSaveRoute = () => {
  const queryClient = useQueryClient();
  
  return useMutation({
    mutationFn: async (routeConfig: RouteConfig) => {
      const response = await axios.post('/api/v1/gateway/routes', routeConfig);
      return response.data;
    },
    onSuccess: () => {
      // Invalidate routes list
      queryClient.invalidateQueries({ queryKey: ['routes'] });
    }
  });
};

```

### Component Interactions

**Data Flow:**

1. **Dashboard Loading** → DashboardPage fetches metrics and service health
2. **Route Management** → Admin creates/edits routes, saves configuration
3. **Rate Limit Configuration** → Admin sets rate limits for routes
4. **Service Monitoring** → Service health and metrics displayed in real-time
5. **Analytics Viewing** → Admin views request logs and performance metrics

**Event Handling:**

- Route configuration saves to backend
- Service health updates via polling or WebSocket
- Metrics refresh automatically
- Route changes trigger service discovery updates

### UI/UX Considerations

- **Loading States**: Show skeleton loaders for routes and services, spinners for actions
- **Error Handling**: Display user-friendly error messages with retry options
- **Validation**: Client-side validation for route paths and configurations
- **Responsive Design**: Desktop-optimized layout for admin dashboard
- **Accessibility**: ARIA labels, keyboard navigation, screen reader support
- **Performance**: Efficient metrics rendering, real-time updates via WebSocket or polling

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

**Note:** API Gateway routes requests to backend microservices. These are the gateway endpoints that handle routing, authentication, and rate limiting.

### Request Routing

The API Gateway routes requests based on path patterns to different microservices:

- **User Service:** `/api/v1/users/*` → Routes to user-service

- **Order Service:** `/api/v1/orders/*` → Routes to order-service

- **Product Service:** `/api/v1/products/*` → Routes to product-service

### Gateway Configuration Endpoint (Admin)

### GET /api/gateway/routes

- **URL:** `/api/gateway/routes`

- **Method:** GET

- **Description:** Get all configured routes (Admin only)

- **Response:**

  ```json
  {
    "success": true,
    "data": {
      "routes": [
        {
          "path": "/api/v1/users/*",
          "targetService": "user-service",
          "method": "ALL",
          "rateLimit": {
            "windowMs": 60000,
            "maxRequests": 100
          }
        }
      ]
    }
  }

  ```

- **Status Codes:** 200 (Success), 401 (Unauthorized), 403 (Forbidden)

### POST /api/gateway/routes

- **URL:** `/api/gateway/routes`

- **Method:** POST

- **Description:** Configure a new route (Admin only)

- **Request Body:**

  ```json
  {
    "path": "/api/v1/users/*",
    "targetService": "user-service",
    "method": "ALL",
    "rateLimit": {
      "windowMs": 60000,
      "maxRequests": 100
    }
  }

  ```

- **Response:**

  ```json
  {
    "success": true,
    "data": {
      "routeId": "route_abc123",
      "path": "/api/v1/users/*",
      "targetService": "user-service",
      "createdAt": "2024-01-15T10:30:00Z"
    }
  }

  ```

- **Status Codes:** 201 (Created), 400 (Validation Error), 401 (Unauthorized), 403 (Forbidden)

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

### API Gateway Service

```typescript
class APIGatewayService {
  async routeRequest(req: Request): Promise<Response> {
    // Authenticate request
    // Apply rate limiting
    // Find target service
    // Forward request
    // Transform response
    // Return response
  }

  async findTargetService(path: string): Promise<string> {
    // Match path pattern to service
    // Return service URL
  }
}

```

---

## Request Flow

1. Client sends request to API Gateway

2. Authenticate and authorize

3. Apply rate limiting

4. Route to appropriate microservice

5. Transform request if needed

6. Forward to service

7. Transform response

8. Return to client

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

**Note:** Implementation details focus on backend (Node.js/Express.js) as API Gateway is a backend infrastructure component.

### Request Routing and Service Discovery

**Backend Implementation:** Express.js middleware handles request routing and service discovery

- **Strategy:** Path-based routing with service discovery - like a traffic controller, routes requests to the right microservice based on URL patterns

- **Service Discovery:** Dynamic service discovery using Consul/etcd or Kubernetes service discovery

**Backend (Express.js):**

```typescript
// Backend: services/APIGatewayService.ts
import axios from 'axios';
import { ServiceRegistry } from './ServiceRegistry';

class APIGatewayService {
  private serviceRegistry: ServiceRegistry;
  private routeConfig: Map<string, RouteConfig>;

  constructor() {
    this.serviceRegistry = new ServiceRegistry();
    this.routeConfig = new Map();
    this.loadRouteConfig();
  }

  async routeRequest(req: Request, res: Response, next: NextFunction) {
    const path = req.path;
    const method = req.method;

    // Find matching route
    const route = this.findRoute(path);
    if (!route) {
      return res.status(404).json({ error: 'Route not found' });
    }

    // Get service instance from registry
    const serviceUrl = await this.serviceRegistry.getServiceUrl(route.targetService);
    if (!serviceUrl) {
      return res.status(503).json({ error: 'Service unavailable' });
    }

    try {
      // Forward request to microservice
      const response = await axios({
        method,
        url: `${serviceUrl}${req.path}`,
        data: req.body,
        headers: {
          ...req.headers,
          'x-forwarded-for': req.ip,
          'x-user-id': req.user?.id
        },
        timeout: 30000
      });

      // Return response
      res.status(response.status).json(response.data);
    } catch (error) {
      if (error.response) {
        // Forward error response from service
        res.status(error.response.status).json(error.response.data);
      } else {
        // Gateway error
        res.status(503).json({ error: 'Service unavailable' });
      }
    }
  }

  private findRoute(path: string): RouteConfig | null {
    for (const [pattern, config] of this.routeConfig.entries()) {
      if (this.matchPath(pattern, path)) {
        return config;
      }
    }
    return null;
  }

  private matchPath(pattern: string, path: string): boolean {
    // Convert pattern to regex (e.g., "/api/v1/users/*" -> "/api/v1/users/.*")
    const regex = new RegExp('^' + pattern.replace(/\*/g, '.*') + '$');
    return regex.test(path);
  }

  private loadRouteConfig() {
    // Load routes from database or config file
    this.routeConfig.set('/api/v1/users/*', {
      targetService: 'user-service',
      rateLimit: { windowMs: 60000, maxRequests: 100 }
    });
    this.routeConfig.set('/api/v1/orders/*', {
      targetService: 'order-service',
      rateLimit: { windowMs: 60000, maxRequests: 200 }
    });
  }
}

```

### Authentication and Authorization

**Backend Implementation:** Express.js middleware handles JWT authentication and authorization

- **Strategy:** JWT token validation - like a bouncer checking IDs, validates tokens before allowing requests

- **Token Validation:** Validate JWT tokens, extract user info, check permissions

**Backend (Express.js):**

```typescript
// Backend: middleware/authMiddleware.ts
import jwt from 'jsonwebtoken';

export const authMiddleware = async (req: Request, res: Response, next: NextFunction) => {
  try {
    const token = req.headers.authorization?.replace('Bearer ', '');

    if (!token) {
      return res.status(401).json({ error: 'Authentication required' });
    }

    // Verify JWT token
    const decoded = jwt.verify(token, process.env.JWT_SECRET!) as any;

    // Attach user info to request
    req.user = {
      id: decoded.userId,
      email: decoded.email,
      roles: decoded.roles
    };

    next();
  } catch (error) {
    return res.status(401).json({ error: 'Invalid token' });
  }
};

export const authorize = (requiredRoles: string[]) => {
  return (req: Request, res: Response, next: NextFunction) => {
    if (!req.user) {
      return res.status(401).json({ error: 'Authentication required' });
    }

    const hasRole = requiredRoles.some(role => req.user.roles.includes(role));
    if (!hasRole) {
      return res.status(403).json({ error: 'Insufficient permissions' });
    }

    next();
  };
};

```

### Rate Limiting

**Backend Implementation:** Express.js middleware applies rate limiting per client

- **Strategy:** Redis-based rate limiting - like limiting how many times someone can knock on a door per minute

- **Rate Limit:** Per IP or per user, configurable per route

**Backend (Express.js):**

```typescript
// Backend: middleware/rateLimiter.ts
import redis from '../config/redis';

export const rateLimiter = (config: { windowMs: number; maxRequests: number }) => {
  return async (req: Request, res: Response, next: NextFunction) => {
    const identifier = req.user?.id || req.ip;
    const key = `rate_limit:${identifier}:${req.path}`;

    try {
      const current = await redis.incr(key);

      if (current === 1) {
        await redis.expire(key, Math.ceil(config.windowMs / 1000));
      }

      if (current > config.maxRequests) {
        return res.status(429).json({
          error: 'Rate limit exceeded',
          retryAfter: await redis.ttl(key)
        });
      }

      // Add rate limit headers
      res.setHeader('X-RateLimit-Limit', config.maxRequests);
      res.setHeader('X-RateLimit-Remaining', Math.max(0, config.maxRequests - current));
      res.setHeader('X-RateLimit-Reset', new Date(Date.now() + config.windowMs).toISOString());

      next();
    } catch (error) {
      // Fail-open: allow request if Redis is down
      console.error('Rate limiter error:', error);
      next();
    }
  };
};

```

### Error Handling

**Backend Implementation:** Express.js middleware handles errors and returns proper status codes

**Backend (Express.js):**

```typescript
// Backend: middleware/errorHandler.ts
export const errorHandler = (err: Error, req: Request, res: Response, next: NextFunction) => {
  console.error('API Gateway Error:', err);

  if (err.name === 'UnauthorizedError') {
    return res.status(401).json({ error: 'Authentication required' });
  }

  if (err.message === 'Service unavailable') {
    return res.status(503).json({ error: 'Service temporarily unavailable' });
  }

  if (err.message === 'Route not found') {
    return res.status(404).json({ error: 'Route not found' });
  }

  if (err.name === 'TimeoutError') {
    return res.status(504).json({ error: 'Gateway timeout' });
  }

  res.status(500).json({ error: 'Internal gateway error' });
};

```

**Error Scenarios:**

- **Service Unavailable:** Handle microservice downtime - return 503, implement circuit breaker pattern, retry with fallback

- **Authentication Errors:** Handle invalid tokens, expired tokens - return 401, clear invalid tokens

- **Rate Limit Errors:** Handle rate limit exceeded - return 429 with retry-after header, log for monitoring

- **Timeout Errors:** Handle service timeouts - return 504, implement timeout configuration, retry with exponential backoff

---

# 4) Algorithms

## Consistent Hashing Algorithm

**Purpose:** Distribute requests evenly across multiple service instances and minimize data movement when instances are added or removed.

**Algorithm:**
1. Create a hash ring (circular space) from 0 to 2^64 - 1
2. Hash each service instance to multiple points on the ring (virtual nodes)
3. Hash the request key (user ID, API key) to a point on the ring
4. Find the first instance clockwise from the key's position

**Implementation:**

```typescript
import crypto from 'crypto';

class ConsistentHash {
  private ring: Map<number, string> = new Map();
  private sortedKeys: number[] = [];
  private virtualNodes: number = 150;
  
  addInstance(instanceId: string): void {
    for (let i = 0; i < this.virtualNodes; i++) {
      const hash = this.hash(`${instanceId}-${i}`);
      this.ring.set(hash, instanceId);
      this.sortedKeys.push(hash);
    }
    this.sortedKeys.sort((a, b) => a - b);
  }
  
  removeInstance(instanceId: string): void {
    for (let i = 0; i < this.virtualNodes; i++) {
      const hash = this.hash(`${instanceId}-${i}`);
      this.ring.delete(hash);
      const index = this.sortedKeys.indexOf(hash);
      if (index > -1) {
        this.sortedKeys.splice(index, 1);
      }
    }
  }
  
  getInstance(key: string): string {
    if (this.ring.size === 0) {
      throw new Error('No instances available');
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
- Time: O(log n) for instance lookup where n is number of virtual nodes
- Space: O(v * s) where v is virtual nodes, s is number of instances
- **Load Distribution:** Only ~1/n of requests move when adding/removing instances

---

## Circuit Breaker Algorithm

**Purpose:** Prevent cascading failures by opening circuit when service fails repeatedly.

**Algorithm:**
1. Track service call failures and successes
2. If failure rate exceeds threshold, open circuit
3. When circuit open, reject requests immediately (fail-fast)
4. After timeout, move to half-open state
5. In half-open, allow test requests
6. If test succeeds, close circuit; if fails, reopen

**Implementation:**

```typescript
enum CircuitState {
  CLOSED = 'closed',
  OPEN = 'open',
  HALF_OPEN = 'half-open'
}

class CircuitBreaker {
  private state: CircuitState = CircuitState.CLOSED;
  private failureCount: number = 0;
  private successCount: number = 0;
  private lastFailureTime: number = 0;
  private failureThreshold: number = 5;
  private successThreshold: number = 2;
  private timeout: number = 30000; // 30 seconds
  
  async execute<T>(fn: () => Promise<T>): Promise<T> {
    if (this.state === CircuitState.OPEN) {
      if (Date.now() - this.lastFailureTime > this.timeout) {
        this.state = CircuitState.HALF_OPEN;
        this.successCount = 0;
      } else {
        throw new Error('Circuit breaker is open');
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
  
  private onSuccess(): void {
    this.failureCount = 0;
    
    if (this.state === CircuitState.HALF_OPEN) {
      this.successCount++;
      if (this.successCount >= this.successThreshold) {
        this.state = CircuitState.CLOSED;
      }
    }
  }
  
  private onFailure(): void {
    this.failureCount++;
    this.lastFailureTime = Date.now();
    
    if (this.failureCount >= this.failureThreshold) {
      this.state = CircuitState.OPEN;
    }
  }
}

```

**Complexity:**
- Time: O(1) for state checks
- Space: O(1) for state tracking
- **Failure Prevention:** Circuit breaker prevents cascading failures

---

# 5) Data Models

## Request Logs Collection (MongoDB)

```javascript
{
  _id: ObjectId,
  requestId: String,        // Unique request ID, indexed
  method: String,           // HTTP method
  path: String,            // API path, indexed
  service: String,          // Target microservice, indexed
  statusCode: Number,       // Response status code
  latency: Number,         // Response time in ms
  userId: ObjectId,        // User reference (optional)
  ipAddress: String,       // Client IP
  userAgent: String,       // Client user agent
  timestamp: Date,         // Request timestamp, indexed
  responseSize: Number     // Response size in bytes
}

// Indexes:
// - { requestId: 1 } (unique)
// - { timestamp: -1 } (for time-based queries)
// - { service: 1, timestamp: -1 } (compound)
// - { path: 1, timestamp: -1 } (compound)
// - { statusCode: 1, timestamp: -1 } (compound)

```

## Service Registry Collection (MongoDB/Consul)

```javascript
{
  _id: ObjectId,
  serviceId: String,        // Service identifier, indexed
  serviceName: String,      // Service name, indexed
  instances: [Object],      // Array of service instances
  healthCheck: Object,      // Health check configuration
  lastHealthCheck: Date,    // Last health check timestamp
  status: String,          // healthy, unhealthy, unknown
  createdAt: Date,
  updatedAt: Date
}

// Indexes:
// - { serviceId: 1 } (unique)
// - { serviceName: 1, status: 1 } (compound)

```

---

# 6) Database Transactions and Consistency

### MongoDB Transactions

**Transaction Usage:**
- **Multi-Document Transactions** - For operations requiring ACID guarantees
- **Example:** Request logging + metric update in single transaction
- **Session Management:** Use MongoDB sessions for transaction control

**Example:**

```typescript
const session = await mongoose.startSession();
session.startTransaction();
try {
  await RequestLog.create([logData], { session });
  await Metric.updateOne({ metricId }, { $inc: { requestCount: 1 } }, { session });
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
- **Request Logging:** Use transactions for request logging to ensure consistency
- **Service Registry:** Accept eventual consistency for service registry (services may appear/disappear with slight delay)
- **Cache Consistency:** Invalidate cache when service configuration changes

---

# 7) Protocols

### REST API Protocol

- **Protocol:** REST (Representational State Transfer)
- **Data Format:** JSON
- **HTTP Methods:** GET, POST, PUT, DELETE, PATCH
- **Status Codes:** 200 (Success), 201 (Created), 400 (Bad Request), 401 (Unauthorized), 404 (Not Found), 429 (Rate Limited), 503 (Service Unavailable), 504 (Gateway Timeout)
- **Authentication:** JWT Bearer token in Authorization header

### Service Discovery Protocol

- **Protocol:** HTTP REST or gRPC
- **Service Registry:** Consul, Eureka, or custom service registry
- **Health Checks:** HTTP health check endpoints
- **Use Case:** Dynamic service discovery and routing

---

# 8) API Design

### GET /api/v1/health

- **URL:** `/api/v1/health`
- **Method:** GET
- **Description:** Health check endpoint for load balancer
- **Response:**

  ```json
  {
    "status": "healthy",
    "timestamp": "2024-01-15T10:30:00Z",
    "services": {
      "user-service": "healthy",
      "order-service": "healthy"
    }
  }

  ```
- **Status Codes:** 200 (Healthy), 503 (Unhealthy)

### GET /api/v1/services

- **URL:** `/api/v1/services`
- **Method:** GET
- **Description:** Get list of registered services (Admin only)
- **Response:**

  ```json
  {
    "success": true,
    "data": {
      "services": [
        {
          "serviceId": "user-service-1",
          "serviceName": "user-service",
          "status": "healthy",
          "instances": 3,
          "lastHealthCheck": "2024-01-15T10:30:00Z"
        }
      ]
    }
  }

  ```
- **Status Codes:** 200 (Success), 401 (Unauthorized), 403 (Forbidden)

---

# 9) Caching Strategy

### Redis Cache

**Cache Strategy:**
- **Key Format:** `cache:response:{path}:{params}`, `service:registry:{serviceName}`
- **Value:** Serialized JSON (API responses, service registry data)
- **TTL:** 
  - API responses: 60 seconds (configurable per endpoint)
  - Service registry: 30 seconds (frequently updated)
- **Eviction Policy:** LRU (Least Recently Used)

**Cache Patterns:**
- **Cache-Aside Pattern:** Check cache first, if miss route to service and update cache
- **Write-Through Pattern:** Update cache when service responses change
- **Cache Invalidation:** Invalidate cache on service configuration changes

---

# 10) Error Handling

### Error Scenarios and Responses

**Edge Cases Handling:**
- **Service Unavailable:** Return 503 Service Unavailable when target service is down
- **Route Not Found:** Return 404 Not Found when route doesn't match any service
- **Authentication Failure:** Return 401 Unauthorized when token is invalid
- **Rate Limit Exceeded:** Return 429 Too Many Requests with Retry-After header
- **Gateway Timeout:** Return 504 Gateway Timeout when service exceeds timeout
- **Circuit Breaker Open:** Return 503 Service Unavailable when circuit is open

**Error Response Format:**

```json
{
  "error": {
    "code": "SERVICE_UNAVAILABLE",
    "message": "Service temporarily unavailable",
    "details": "user-service is currently unavailable",
    "retryAfter": 30
  }
}

```

---

# 11) Deployment and DevOps

### Scalability

**API Gateway Layer:**
- Deploy API Gateway across multiple instances behind load balancer
- Use auto-scaling based on CPU/memory metrics
- Stateless design allows horizontal scaling

**Service Discovery:**
- **Service Registry:** Deploy service registry cluster (Consul/Eureka)
- **Health Checks:** Configure health check intervals and timeouts
- **Dynamic Updates:** Update routing table automatically when services change

**Caching:**
- Distributed Redis cluster for high availability
- Cache API responses and service registry data
- Reduces backend load significantly

### Availability

**Replication:**
- Service registry replication ensures availability
- Multi-region replication for disaster recovery

**Failover:**
- Automated failover mechanisms for API Gateway and service registry
- Health checks and monitoring for proactive failover
- Circuit breaker pattern to prevent cascading failures

**Geo-Distributed Deployment:**
- Deploy API Gateway across multiple geographical regions
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
- **Health Checks:** Verify API Gateway endpoints are healthy
- **Blue-Green Deployment:** Maintain two identical production environments

### Database Deployment

**MongoDB Setup:**
- **MongoDB Atlas** - Managed MongoDB service with automatic backups
- **Backup Strategy:** Daily automated backups with point-in-time recovery
- **Indexing:** Proper indexes on requestId, timestamp, service, path
- **Replication:** Replica sets for high availability

**Redis Setup:**
- **Redis Cloud / AWS ElastiCache** - Managed Redis service
- **Cluster Mode:** Redis cluster for high availability and performance
- **Persistence:** RDB snapshots and AOF for data durability

---

# 12) Security Considerations

### Rate Limiting

- Implement rate limiting at API Gateway layer to prevent abuse
- Limit number of requests per user/IP/API key per minute/hour
- Use Redis for distributed rate limiting across multiple gateway instances

### Input Validation

- Validate all API requests before routing to services
- Sanitize user input to prevent injection attacks
- Validate request size to prevent DoS attacks

### HTTPS/TLS

- All communication between clients and API Gateway encrypted using HTTPS
- Prevents eavesdropping and man-in-the-middle attacks
- SSL/TLS certificates for secure connections

### Authentication and Authorization

- **JWT Tokens:** Validate JWT tokens before routing requests
- **Token Expiration:** Check token expiration and reject expired tokens
- **API Keys:** Support API key authentication for service-to-service communication
- **OAuth:** Support OAuth 2.0 for third-party authentication

### Monitoring and Alerts

- Set up monitoring for unusual request patterns
- Trigger alerts for potential DDoS attacks or abuse
- Track metrics: request rates, error rates, latency, service health
- Log all requests for security auditing

---

# 3) Interview Answers

---

## Q1. 🔌 Designing an API Gateway

**Situation:** Need to design an API Gateway that routes 1B+ requests per day to 100+ microservices with authentication, rate limiting, and monitoring.

**Action:** I designed an API Gateway:

- **Request Routing:** Route requests to appropriate microservices based on path/domain

- **Load Balancing:** Distribute requests across service instances using round-robin/consistent hashing

- **Authentication:** Validate JWT tokens, OAuth tokens, API keys

- **Rate Limiting:** Implement rate limiting per user/API key using Redis

- **Circuit Breaker:** Prevent cascading failures by opening circuit when service fails

- **Request/Response Transformation:** Transform requests/responses between different formats

- **Caching:** Cache responses to reduce backend load (Redis)

- **Service Discovery:** Integrate with service registry (Consul, Eureka) for dynamic routing

- **Monitoring:** Log all requests, track metrics (latency, error rate)

**Result:** API Gateway handles 1B+ requests per day with < 10ms latency overhead. 99.9% availability. Rate limiting prevents abuse.

**Takeaway:** API Gateway centralizes cross-cutting concerns. Circuit breaker prevents cascading failures. Caching reduces backend load.

---

## Q2. 💡 Implementing service discovery

**Situation:** Microservices scale dynamically, need to route requests to available instances.

**Action:** I implemented service discovery:

- **Service Registry:** Use Consul/Eureka to maintain service registry

- **Health Checks:** Services register with health check endpoints

- **Dynamic Updates:** Update routing table when services register/deregister

- **Load Balancing:** Distribute requests across healthy instances

- **Caching:** Cache service registry locally, refresh periodically

- **Fallback:** Fallback to cached registry if service discovery fails

**Result:** Services scale dynamically without manual configuration. Requests routed to healthy instances. Zero downtime during service updates.

**Takeaway:** Service discovery enables dynamic scaling. Health checks ensure only healthy instances receive traffic.

---

## Q3. 💡 Handling circuit breaker pattern

**Situation:** When microservice fails, prevent cascading failures to other services.

**Action:** I implemented circuit breaker:

- **Three States:** Closed (normal), Open (failing), Half-Open (testing)

- **Failure Threshold:** Open circuit when error rate > 50% in 1 minute

- **Timeout:** Keep circuit open for 30 seconds, then move to half-open

- **Test Requests:** Send test requests in half-open state, close if successful

- **Fallback:** Return cached response or error message when circuit open

- **Monitoring:** Track circuit state changes for alerting

**Result:** Circuit breaker prevents cascading failures. System recovers automatically when service recovers. 99.9% availability maintained.

**Takeaway:** Circuit breaker is essential for microservices. Prevents one failing service from bringing down entire system.
