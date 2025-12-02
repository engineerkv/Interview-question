# Rate Limiter - High Level Design (HLD)

> **Project Type:** Full-Stack System Component (MERN Stack)  
> **Purpose:** Design and implement a rate limiting system to prevent API abuse and ensure fair resource usage  
> **Tech Stack:** 
> - **Backend:** Node.js, Express.js, Redis
> - **Frontend:** React.js (for admin dashboard to view rate limit metrics)
> **Key Features:** Multiple rate limiting algorithms, distributed rate limiting, configurable limits, monitoring dashboard

---

## 1. Requirements

### a) Functional Requirements

#### Rate Limiting Rules
- **Per-user rate limiting** - Limit requests per user/IP address
- **Per-endpoint rate limiting** - Different limits for different API endpoints
- **Global rate limiting** - Overall system-wide limits
- **Configurable limits** - Easy to adjust limits without code changes
- **Multiple algorithms** - Support different rate limiting strategies

#### Rate Limiting Algorithms
- **Token Bucket** - Allows bursts of traffic
- **Sliding Window** - Smooth rate limiting over time window
- **Fixed Window** - Simple time-based window
- **Leaky Bucket** - Smooths out traffic spikes

#### Monitoring & Logging
- **Rate limit metrics** - Track how many requests are being limited
- **Alerting** - Alert when rate limits are hit frequently
- **Logging** - Log rate limit violations for analysis

### b) Non-Functional Requirements

#### Performance
- **Low latency** - Rate limiting check should be fast (< 10ms)
- **High throughput** - Handle thousands of requests per second
- **Minimal overhead** - Shouldn't slow down API significantly

#### Scalability
- **Distributed** - Work across multiple servers
- **Horizontal scaling** - Add more servers without issues
- **Redis-based** - Use Redis for shared state across servers

#### Reliability
- **Fail-open** - If rate limiter fails, allow requests (don't block everything)
- **Graceful degradation** - Fallback if Redis is down
- **High availability** - 99.9% uptime

---

## 2. Scope & Priority

### Phase 1: MVP (Must Have) - Priority 1

#### Functional
- **Basic rate limiting** - Per-IP rate limiting
- **Fixed window algorithm** - Simple time-based window
- **Redis storage** - Store rate limit counters in Redis
- **HTTP headers** - Return rate limit info in response headers

#### Non-Functional
- **Performance** - < 10ms overhead per request
- **Basic monitoring** - Log rate limit hits

### Phase 2: Enhanced Features - Priority 2

#### Functional
- **Multiple algorithms** - Token bucket, sliding window
- **Per-user rate limiting** - Based on user ID, not just IP
- **Per-endpoint limits** - Different limits for different endpoints
- **Whitelist/Blacklist** - Allow/block specific IPs/users

#### Non-Functional
- **Advanced monitoring** - Metrics, dashboards
- **Alerting** - Alert on high rate limit hits

### Phase 3: Advanced Features - Priority 3

#### Functional
- **Dynamic limits** - Adjust limits based on system load
- **Rate limit tiers** - Different limits for different user tiers
- **Distributed rate limiting** - Advanced distributed algorithms

---

## 3. Tech Choices

### Rate Limiting Library
- **express-rate-limit:** Simple Express.js middleware for rate limiting
  - Easy to use, good defaults
  - Redis store support
  - Configurable windows and limits
- **rate-limiter-flexible:** Advanced rate limiting library
  - Multiple algorithms (token bucket, sliding window)
  - Redis support
  - More flexible configuration

### Storage
- **Redis:** In-memory data store for rate limit counters
  - **Why Redis?** Fast (in-memory), supports atomic operations, distributed
  - **Atomic operations** - INCR, EXPIRE for rate limiting
  - **TTL support** - Automatic expiration of counters
  - **Pub/Sub** - Can sync across servers if needed

### Middleware
- **Express middleware:** Intercept requests before they reach handlers
  - Check rate limit before processing request
  - Return 429 Too Many Requests if limit exceeded
  - Add rate limit headers to response

---

## Architecture Overview

```
┌─────────────────────────────────────────────────────────┐
│              Client Requests                             │
└─────────────────────────────────────────────────────────┘
                        │
                        ▼
┌─────────────────────────────────────────────────────────┐
│         Load Balancer / API Gateway                      │
└─────────────────────────────────────────────────────────┘
                        │
                        ▼
┌─────────────────────────────────────────────────────────┐
│         Rate Limiter Middleware                          │
│  ┌──────────────────────────────────────────────────┐   │
│  │  1. Extract Identifier (IP, User ID, API Key)   │   │
│  │  2. Check Rate Limit in Redis                    │   │
│  │  3. Increment Counter                            │   │
│  │  4. Check if Limit Exceeded                      │   │
│  │  5. Allow or Reject Request                      │   │
│  └──────────────────────────────────────────────────┘   │
└─────────────────────────────────────────────────────────┘
        │                                    │
        │ Allow                              │ Reject
        ▼                                    ▼
┌──────────────────┐              ┌──────────────────┐
│  API Handler     │              │  429 Response    │
│  (Process Request)│              │  (Rate Limited)  │
└──────────────────┘              └──────────────────┘
        │
        ▼
┌─────────────────────────────────────────────────────────┐
│              Redis (Rate Limit Storage)                  │
│  ┌──────────────────────────────────────────────────┐   │
│  │  Key: rate_limit:ip:192.168.1.1                 │   │
│  │  Value: 45 (request count)                      │   │
│  │  TTL: 60 seconds                                │   │
│  └──────────────────────────────────────────────────┘   │
└─────────────────────────────────────────────────────────┘
```

**How it works:**
1. **Request comes in** - Client makes API request
2. **Rate limiter intercepts** - Middleware checks before processing
3. **Check Redis** - Look up current count for this identifier (IP/user)
4. **Increment counter** - Add 1 to current count (atomic operation)
5. **Check limit** - If count > limit, reject with 429
6. **Allow request** - If under limit, pass to API handler
7. **Set TTL** - Redis automatically expires counter after time window

---

## Key Design Decisions

1. **Redis for Storage:** Fast in-memory storage with atomic operations - perfect for rate limiting counters
   - Atomic INCR ensures accurate counting even with concurrent requests
   - TTL support automatically cleans up expired counters
   - Distributed - works across multiple servers

2. **Middleware Approach:** Intercept requests before processing - efficient and clean
   - Runs before expensive operations
   - Can reject early, saving resources
   - Easy to add/remove from any endpoint

3. **Multiple Algorithms:** Support different strategies for different use cases
   - **Fixed window** - Simple, good for basic use cases
   - **Sliding window** - More accurate, prevents burst at window boundaries
   - **Token bucket** - Allows bursts, good for variable traffic

4. **Fail-Open Strategy:** If rate limiter fails, allow requests - don't block everything
   - Better to allow some extra requests than block all users
   - Log failures for monitoring
   - Graceful degradation

5. **Per-IP and Per-User:** Support both IP-based and user-based limiting
   - IP-based for anonymous users
   - User-based for authenticated users (more accurate)
   - Can combine both for better protection

