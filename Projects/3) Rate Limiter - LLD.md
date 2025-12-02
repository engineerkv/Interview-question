# Rate Limiter - Low Level Design (LLD)

> **Project Type:** Full-Stack System Component (MERN Stack)  
> **Tech Stack:** 
> - **Backend:** Node.js, Express.js, Redis, TypeScript
> - **Frontend:** React.js (optional admin dashboard)

---

## 3. Component Architecture

**Think of this as the building blocks - how rate limiting components are organized**

### Rate Limiter Middleware Structure

```
RateLimiterMiddleware
├── IdentifierExtractor
│   ├── ExtractIP (from request)
│   ├── ExtractUserID (from JWT token)
│   └── ExtractAPIKey (from headers)
├── RateLimitChecker
│   ├── RedisClient
│   ├── Algorithm (FixedWindow, SlidingWindow, TokenBucket)
│   └── LimitConfig (limits per endpoint)
├── ResponseHandler
│   ├── AllowRequest (pass to next middleware)
│   ├── RejectRequest (return 429)
│   └── AddHeaders (rate limit info in response)
└── MetricsCollector
    ├── TrackHits
    ├── TrackRejects
    └── TrackErrors
```

**How components work together:**
- **IdentifierExtractor** - Gets unique identifier (IP, user ID) from request
- **RateLimitChecker** - Checks current count against limit using Redis
- **ResponseHandler** - Allows or rejects request, adds headers
- **MetricsCollector** - Tracks rate limit metrics for monitoring

---

## 4. Data Models

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

## 5. Implementation Details

### Fixed Window Algorithm

**How it works:**
- Divide time into fixed windows (e.g., 1 minute windows)
- Count requests in current window
- Reset counter at window boundary

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

**Pros:**
- Simple to implement
- Low memory usage
- Fast (single Redis operation)

**Cons:**
- Can allow bursts at window boundaries
- Less accurate than sliding window

### Sliding Window Algorithm

**How it works:**
- Track requests in a sliding time window
- Count requests in last N seconds
- More accurate than fixed window

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

**Pros:**
- More accurate - prevents bursts at boundaries
- Smooth rate limiting

**Cons:**
- More memory usage (stores all requests)
- More Redis operations (slower)

### Token Bucket Algorithm

**How it works:**
- Bucket has tokens (capacity)
- Tokens refill at constant rate
- Request consumes one token
- If bucket empty, request rejected

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

**Pros:**
- Allows bursts (if tokens available)
- Smooths out traffic
- Good for variable traffic patterns

**Cons:**
- More complex to implement
- More Redis operations

---

## 6. Express Middleware Implementation

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

## 7. Distributed Rate Limiting

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

## 8. Advanced Features

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

## 9. Monitoring and Metrics

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

## 10. Error Handling

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

