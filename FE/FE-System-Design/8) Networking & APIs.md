<div align="center">

**[← Previous: Practical Front-End System Design Scenarios](7%29%20Practical%20Front-End%20System%20Design%20Scenarios.md)** | **[Next: Real-time Communication Protocols →](9%29%20Real-time%20Communication%20Protocols.md)**

</div>

# 8. Networking & APIs (Q84–101)

---

## Q84. How the internet works and how DNS and IP addresses work together

The internet is a global network of interconnected devices communicating via standardized protocols. DNS (Domain Name System) translates human-readable domain names like example.com into IP addresses like 192.0.2.1, which routers use to route data packets across networks to their destination - IP routing is stateless, so each packet is routed independently toward its destination.

- **Trade-offs**: DNS provides human-friendly names while IP addresses are the actual network identifiers - DNS caching happens at multiple levels (browser, OS, ISP, root servers) which speeds things up, but DNS resolution typically adds 20-120ms latency, so consider preconnect/dns-prefetch. IPv4 uses 32-bit addresses (4.3 billion possible) while IPv6 uses 128-bit (virtually unlimited).

Example:

```javascript
async function resolveDNS(hostname) {
  const ip = await dns.lookup(hostname);
  console.log(`${hostname} resolves to ${ip}`);
  const socket = new Socket();
  socket.connect(80, ip);
}
```

---

## Q85. HTTP and how it works

Protocols are standardized rules for communication between devices. HTTP (Hypertext Transfer Protocol) is the foundation of web communication, while HTTPS adds encryption via TLS/SSL, ensuring data confidentiality and integrity between client and server - always use HTTPS for authentication, payments, and sensitive data.

- **Trade-offs**: HTTP is unencrypted so data can be intercepted and modified (man-in-the-middle attacks), while HTTPS encrypts data in transit, authenticates server identity, and prevents tampering. The catch is TLS handshake adds initial latency (~100-300ms) but enables secure communication - HTTP/2 and HTTP/3 provide multiplexing and faster connection establishment.

Example:

```javascript
fetch('http://example.com/api/data').then(res => res.json());
fetch('https://example.com/api/data').then(res => res.json());
```

---

## Q86. HTTP methods and when to use each

HTTP methods define operations on resources: GET retrieves data (idempotent, cacheable), POST creates resources or submits data (not idempotent), PUT updates entire resources (idempotent), PATCH partially updates resources (idempotent), DELETE removes resources (idempotent). Use GET for reading, POST for creating, PUT/PATCH for updating, DELETE for removing.

- **Trade-offs**: Idempotent methods (GET, PUT, DELETE, PATCH) can be safely retried without side effects, but POST is not idempotent - multiple identical requests may create multiple resources. GET requests should be cacheable while POST/PUT/DELETE typically aren't - use appropriate methods for semantic correctness and HTTP caching benefits.

Example:

```javascript
// GET - retrieve data (idempotent, cacheable)
fetch('/api/users/123', { method: 'GET' });

// POST - create new resource (not idempotent)
fetch('/api/users', {
  method: 'POST',
  headers: { 'Content-Type': 'application/json' },
  body: JSON.stringify({ name: 'John', email: 'john@example.com' })
});

// PUT - update entire resource (idempotent)
fetch('/api/users/123', { 
  method: 'PUT', 
  body: JSON.stringify({ name: 'John Doe', email: 'john@example.com' }) 
});

// PATCH - partial update (idempotent)
fetch('/api/users/123', { 
  method: 'PATCH', 
  body: JSON.stringify({ name: 'John Doe' }) 
});

// DELETE - remove resource (idempotent)
fetch('/api/users/123', { method: 'DELETE' });
```

---

## Q87. HTTP status codes and what they mean

HTTP status codes communicate request outcomes: 2xx (success - 200 OK, 201 Created, 204 No Content), 3xx (redirection - 301 Moved Permanently, 304 Not Modified), 4xx (client errors - 400 Bad Request, 401 Unauthorized, 403 Forbidden, 404 Not Found), 5xx (server errors - 500 Internal Server Error, 502 Bad Gateway, 503 Service Unavailable). Use appropriate status codes to accurately reflect request outcome.

- **Trade-offs**: Status codes should accurately reflect request outcome - don't use 200 for errors or 404 for authentication failures. 4xx indicates client errors (fix the request), 5xx indicates server errors (server needs fixing) - proper status codes help with debugging, caching, and error handling.

Example:

```javascript
async function fetchUser(id) {
  const response = await fetch(`/api/users/${id}`, {
    method: 'GET',
    headers: { 'Accept': 'application/json', 'Authorization': `Bearer ${token}` }
  });
  
  if (response.status === 200) return await response.json();
  if (response.status === 201) return await response.json(); // Created
  if (response.status === 204) return null; // No Content
  if (response.status === 304) return cachedData; // Not Modified
  if (response.status === 400) throw new Error('Bad Request');
  if (response.status === 401) throw new Error('Unauthorized');
  if (response.status === 403) throw new Error('Forbidden');
  if (response.status === 404) throw new Error('User not found');
  if (response.status === 500) throw new Error('Internal Server Error');
  if (response.status === 503) throw new Error('Service Unavailable');
}
```

---

## Q88. HTTP headers and how to use them

HTTP headers provide metadata about requests and responses, controlling caching, authentication, content negotiation, CORS, and security. Common headers: Content-Type (MIME type), Authorization (credentials), Cache-Control (caching directives), Accept (content negotiation), CORS headers (Access-Control-Allow-Origin), security headers (X-Frame-Options, CSP). Headers enable fine-grained control over HTTP communication.

- **Trade-offs**: Headers provide rich metadata for content negotiation, caching, authentication, and CORS, but the catch is too many headers increase request size and complexity. Cache-Control header is crucial for browser and CDN caching strategies - use appropriate headers for security, performance, and functionality.

Example:

```javascript
// Request headers
fetch('/api/users', {
  method: 'POST',
  headers: {
    'Content-Type': 'application/json',
    'Authorization': 'Bearer token123',
    'Accept': 'application/json',
    'Accept-Language': 'en-US,en;q=0.9',
    'Cache-Control': 'no-cache'
  },
  body: JSON.stringify({ name: 'John' })
});

// Response headers (server sets)
// Content-Type: application/json
// Cache-Control: public, max-age=3600
// Access-Control-Allow-Origin: https://example.com
// X-Frame-Options: DENY
// Content-Security-Policy: default-src 'self'

// Reading response headers
const response = await fetch('/api/users');
const contentType = response.headers.get('Content-Type');
const cacheControl = response.headers.get('Cache-Control');
```

---

## Q89. Difference between HTTP/1.1 and HTTP/2

HTTP/1.1 sends one request per connection and requires multiple connections for parallelism, which causes head-of-line blocking. HTTP/2 multiplexes multiple requests over a single connection, uses header compression (HPACK), and supports server push, which improves performance significantly. HTTP/2 maintains backward compatibility with HTTP/1.1 semantics while improving efficiency.

- **Trade-offs**: HTTP/2 improves performance significantly over HTTP/1.1, but the catch is it still uses TCP which can cause head-of-line blocking. HTTP/3 uses QUIC over UDP to eliminate TCP's head-of-line blocking. HTTP/2's server push can waste bandwidth if resources are already cached - use HTTP/2 for better performance, HTTP/3 for even better performance on unreliable networks.

- **Trade-offs**: REST advantages include simplicity, HTTP caching, wide tooling support, and easier debugging - GraphQL advantages include flexible queries, reduced round trips, strong typing, and better for complex UIs. Consider team expertise, infrastructure, and long-term maintenance - many companies use hybrid: REST for simple operations, GraphQL for complex queries. REST caching leverages CDN and browser caching while GraphQL caching requires application-level strategies.

Example:

```javascript
fetch('/api/users', { method: 'GET' });
const query = `
  query GetDashboard {
    user {
      profile { name, avatar }
      posts { title, comments { author, text } }
    }
  }
`;
```

---

## Q90. REST and how to design RESTful APIs

REST (Representational State Transfer) is an architectural style for designing web services - RESTful APIs use standard HTTP methods, stateless requests, resource-oriented URLs, and support caching to create scalable, maintainable APIs. Design RESTful APIs with resource-based URLs (nouns, not verbs), use HTTP methods for actions, return appropriate status codes, and support content negotiation.

- **Trade-offs**: Statelessness enables horizontal scaling and better caching - resource-oriented design (nouns in URLs, verbs in HTTP methods) improves clarity, but watch out - GET requests should be cacheable while POST/PUT/DELETE typically aren't. REST works best with standard HTTP caching mechanisms - HATEOAS (Hypermedia as the Engine of Application State) is optional but powerful.

Example:

```javascript
// RESTful API design
// GET /api/users - list users
// GET /api/users/123 - get user
// POST /api/users - create user
// PUT /api/users/123 - update user
// DELETE /api/users/123 - delete user

// Resource-based URLs (nouns)
fetch('/api/users', { method: 'GET' });
fetch('/api/users/123', { method: 'GET' });
fetch('/api/users', {
  method: 'POST',
  headers: { 'Content-Type': 'application/json' },
  body: JSON.stringify({ name: 'John', email: 'john@example.com' })
});
fetch('/api/users/123', { 
  method: 'PUT', 
  body: JSON.stringify({ name: 'John Doe' }) 
});
fetch('/api/users/123', { method: 'DELETE' });
```

---

## Q91. GraphQL and how it differs from REST

GraphQL is a query language and runtime for APIs that allows clients to request exactly the data they need - unlike REST which returns fixed data structures, GraphQL allows clients to specify field selection, solving over-fetching (getting unnecessary data) and under-fetching (needing multiple requests) problems. Best for complex UIs with varying data needs and mobile apps with bandwidth constraints.

- **Trade-offs**: GraphQL schema serves as contract between client and server, enabling strong typing - field resolvers allow combining data from multiple sources (databases, APIs, services), but watch out - batching with DataLoader prevents N+1 query problems. GraphQL can fetch related data in single request, reducing round trips - REST caching leverages CDN and browser caching while GraphQL caching requires application-level strategies.

Example:

```javascript
// GraphQL query - client specifies exact fields needed
const query = `
  query GetUser($id: ID!) {
    user(id: $id) {
      id
      name
      email
      posts { 
        title
        createdAt
      }
    }
  }
`;

const response = await fetch('/graphql', {
  method: 'POST',
  headers: { 'Content-Type': 'application/json' },
  body: JSON.stringify({ query, variables: { id: '123' } })
});

// REST equivalent would require multiple requests:
// GET /api/users/123
// GET /api/users/123/posts
  string email = 3;
}
const Person = require('./generated/Person_pb');
const person = new Person.Person();
person.setId(123);
const bytes = person.serializeBinary();
```

---

## Q92. gRPC and when to use it

gRPC (gRPC Remote Procedure Calls) is a high-performance RPC framework using Protocol Buffers for serialization and HTTP/2 for transport - it differs from REST by using binary protocols, code generation, streaming, and strong typing. Better for microservices communication, high-performance APIs, and real-time systems where low latency and efficiency matter.

- **Trade-offs**: gRPC uses Protocol Buffers (protobuf) - binary format that's 3-10x smaller than JSON - code generation from .proto files ensures type safety and reduces boilerplate. HTTP/2 support enables multiplexing, header compression, and server push - streaming support includes unary (request-response), server streaming, client streaming, and bidirectional. Use gRPC for internal microservices, high-performance APIs, or when you need streaming - use REST for public APIs or when HTTP caching is critical.

Example:

```javascript
const client = new UserServiceClient('https://api.example.com');
Promise.all([
  client.getUser({ id: 1 }),
  client.getUser({ id: 2 }),
  client.getUser({ id: 3 })
]);
```

---

## Q93. Handling API authentication and authorization

API authentication verifies user identity (who you are), while authorization determines what actions you can perform (what you can do). Common authentication methods include API keys, OAuth 2.0, JWT tokens, and session-based auth. Authorization uses role-based access control (RBAC) or permission-based systems to enforce access rules.

- **Trade-offs**: JWT tokens are stateless and scalable but can't be revoked easily - session-based auth is easier to revoke but requires server-side storage. OAuth 2.0 is complex but provides secure third-party access - API keys are simple but less secure. Always use HTTPS for authentication, implement token expiration and refresh, and validate permissions on every request.

Example:

```javascript
// JWT Authentication
const token = localStorage.getItem('token');
fetch('/api/users', {
  headers: {
    'Authorization': `Bearer ${token}`,
    'Content-Type': 'application/json'
  }
});

// OAuth 2.0 flow
const authUrl = `https://oauth.provider.com/authorize?client_id=${clientId}&redirect_uri=${redirectUri}&response_type=code`;
window.location.href = authUrl;

// API Key authentication
fetch('/api/data', {
  headers: {
    'X-API-Key': apiKey
  }
});

// Role-based authorization check
function canAccess(user, resource, action) {
  return user.roles.some(role => 
    role.permissions.some(p => 
      p.resource === resource && p.actions.includes(action)
    )
  );
}
```

---

## Q94. Implementing API rate limiting

API rate limiting restricts the number of requests a client can make within a time period - front-end implementation involves tracking request counts, handling rate limit responses, and providing user feedback. Provide clear user feedback when rate limits are hit.

- **Trade-offs**: Rate limiting prevents API abuse and ensures fair resource usage - track request counts and handle 429 (Too Many Requests) responses. Use rate limit headers (X-RateLimit-Remaining, X-RateLimit-Reset) for user feedback - implement exponential backoff for retries after rate limit errors.

Example:

```javascript
class RateLimiter {
  constructor(maxRequests, windowMs) {
    this.maxRequests = maxRequests;
    this.windowMs = windowMs;
    this.requests = [];
  }
  canMakeRequest() {
    const now = Date.now();
    this.requests = this.requests.filter(time => now - time < this.windowMs);
    if (this.requests.length < this.maxRequests) {
      this.requests.push(now);
      return true;
    }
    return false;
  }
}
const limiter = new RateLimiter(10, 60000);
async function fetchWithRateLimit(url) {
  if (!limiter.canMakeRequest()) throw new Error('Rate limit exceeded');
  const response = await fetch(url);
  if (response.status === 429) {
    const retryAfter = response.headers.get('Retry-After');
    console.warn(`Rate limited. Retry after ${retryAfter} seconds`);
  }
  return response.json();
}
```

---

## Q95. API documentation and how to create it

API authentication verifies the identity of clients making requests - common methods include JWT tokens, OAuth 2.0, and API keys, each with different security levels and use cases. Choose authentication method based on security requirements and use case.

- **Trade-offs**: JWT is stateless and scalable, OAuth 2.0 is secure and standardized, API keys are simple but less secure - JWT works well for stateless authentication, OAuth for third-party integrations. Store tokens securely (httpOnly cookies for refresh tokens, secure storage for access tokens) - implement token refresh logic to handle expired tokens automatically.

Example:

```javascript
const token = localStorage.getItem('authToken');
fetch('/api/users', {
  headers: { 'Authorization': `Bearer ${token}` }
});
const authUrl = 'https://auth.example.com/authorize?client_id=client123&redirect_uri=https://app.example.com/callback&response_type=code';
const code = new URLSearchParams(window.location.search).get('code');
const response = await fetch('https://auth.example.com/token', {
  method: 'POST',
  body: JSON.stringify({ grant_type: 'authorization_code', code, client_id: 'client123' })
});
const { access_token } = await response.json();
```

---

## Q96. Handling API errors and retries

Request/response interceptors allow you to modify requests before they're sent and responses before they're processed - they're useful for adding authentication headers, handling errors globally, and logging. Interceptors reduce boilerplate and provide consistent error handling.

- **Trade-offs**: Interceptors provide centralized request/response handling - add authentication headers, handle token refresh, log requests. Use interceptors for error handling, retries, and request transformation - implement retry logic with exponential backoff in interceptors.

Example:

```javascript
axios.interceptors.request.use((config) => {
    const token = localStorage.getItem('authToken');
  if (token) config.headers.Authorization = `Bearer ${token}`;
    return config;
});

axios.interceptors.response.use(
  (response) => response,
  async (error) => {
    if (error.response?.status === 401 && !error.config._retry) {
      error.config._retry = true;
        const refreshToken = localStorage.getItem('refreshToken');
        const response = await axios.post('/api/auth/refresh', { refreshToken });
      localStorage.setItem('authToken', response.data.accessToken);
      error.config.headers.Authorization = `Bearer ${response.data.accessToken}`;
      return axios(error.config);
      }
    return Promise.reject(error);
  }
);
```

---

## Q97. API pagination and how to implement it

API error handling involves detecting, categorizing, and responding to different error types (network errors, HTTP errors, validation errors) with appropriate user feedback and recovery strategies. Provide clear, actionable error messages to users.

- **Trade-offs**: Categorize errors by type (network, HTTP, validation) and handle appropriately - provide user-friendly error messages and recovery options. Handle 401 by redirecting to login, 429 with retry logic, network errors with offline indicators - implement retry logic with exponential backoff for transient errors.

Example:

```javascript
class APIError extends Error {
  constructor(message, status, code) {
    super(message);
    this.status = status;
    this.code = code;
  }
}
async function fetchWithErrorHandling(url, options = {}) {
  try {
    const response = await fetch(url, options);
    if (!response.ok) {
      const errorData = await response.json().catch(() => ({}));
      switch (response.status) {
        case 400: throw new APIError(errorData.message || 'Bad Request', 400, 'BAD_REQUEST');
        case 401: throw new APIError('Authentication required', 401, 'UNAUTHORIZED');
        case 404: throw new APIError('Resource not found', 404, 'NOT_FOUND');
        case 429: throw new APIError('Too many requests', 429, 'RATE_LIMITED');
        case 500: throw new APIError('Server error', 500, 'SERVER_ERROR');
      }
    }
    return await response.json();
  } catch (error) {
    if (error.name === 'TypeError' && error.message.includes('fetch')) {
      throw new APIError('Network error. Please check your connection.', 0, 'NETWORK_ERROR');
    }
    throw error;
  }
}
```

---

## Q98. Optimizing API performance

API pagination breaks large result sets into smaller chunks - common strategies include offset-based (page numbers), cursor-based (after/before tokens), and keyset-based (last seen ID) pagination, each with different trade-offs. Choose pagination strategy based on data characteristics and use case.

- **Trade-offs**: Offset-based is simple but inefficient for large datasets, cursor-based is efficient and handles new data well, keyset-based is efficient and good for sorted data. Cursor-based pagination is best for infinite scroll and real-time data - offset-based is easier to implement but has performance issues with large offsets. Keyset-based pagination is most efficient for sorted, indexed data.

Example:

```javascript
async function fetchUsersWithOffset(page = 1, limit = 20) {
  const response = await fetch(`/api/users?page=${page}&limit=${limit}`);
  const data = await response.json();
  return { users: data.items, page: data.page, hasNextPage: data.page < data.totalPages };
}
async function fetchUsersWithCursor(cursor = null, limit = 20) {
  const url = cursor ? `/api/users?cursor=${cursor}&limit=${limit}` : `/api/users?limit=${limit}`;
  const response = await fetch(url);
  const data = await response.json();
  return { users: data.items, nextCursor: data.nextCursor, hasNextPage: !!data.nextCursor };
}
```

---

## Q99. API caching and how to implement it

API request batching combines multiple requests into a single request to reduce round trips and improve performance - it's useful when you need to fetch multiple resources simultaneously. Balance batch size with latency - larger batches reduce requests but increase delay.

- **Trade-offs**: Request batching reduces network round trips and improves performance - useful when fetching multiple related resources simultaneously. Batch requests based on size limit or time delay - implement smart batching that groups related requests together.

Example:

```javascript
class RequestBatcher {
  constructor(batchSize = 10, delay = 50) {
    this.batchSize = batchSize;
    this.delay = delay;
    this.queue = [];
    this.timeout = null;
  }
  async addRequest(request) {
    return new Promise((resolve, reject) => {
      this.queue.push({ request, resolve, reject });
      if (this.queue.length >= this.batchSize) {
        this.processBatch();
      } else {
        this.scheduleBatch();
      }
    });
  }
  async processBatch() {
    if (this.queue.length === 0) return;
    const batch = this.queue.splice(0, this.batchSize);
    const response = await fetch('/api/batch', {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify({ requests: batch.map(item => item.request) })
    });
    const results = await response.json();
    batch.forEach((item, index) => {
      results[index].success ? item.resolve(results[index].data) : item.reject(new Error(results[index].error));
    });
  }
  scheduleBatch() {
    if (this.timeout) clearTimeout(this.timeout);
    this.timeout = setTimeout(() => this.processBatch(), this.delay);
  }
}
```

---

## Q100. Monitoring and debugging API calls

API request deduplication prevents multiple identical requests from being sent simultaneously - it's useful when the same request is triggered multiple times (e.g., rapid button clicks, multiple component renders). Combine with debouncing/throttling for user interactions.

- **Trade-offs**: Request deduplication prevents unnecessary network requests and reduces server load - useful when same request triggered multiple times (rapid clicks, multiple renders). Use request keys (URL + method + body) to identify duplicate requests - implement request caching with TTL for repeated requests.

Example:

```javascript
class RequestDeduplicator {
  constructor() {
    this.pendingRequests = new Map();
  }
  async deduplicate(key, requestFn) {
    if (this.pendingRequests.has(key)) {
      return this.pendingRequests.get(key);
    }
    const promise = requestFn()
      .then(result => { this.pendingRequests.delete(key); return result; })
      .catch(error => { this.pendingRequests.delete(key); throw error; });
    this.pendingRequests.set(key, promise);
    return promise;
  }
}
const deduplicator = new RequestDeduplicator();
async function fetchUser(id) {
  const key = `user-${id}`;
  return deduplicator.deduplicate(key, async () => {
    const response = await fetch(`/api/users/${id}`);
    return response.json();
  });
}
```

---

## Q101. Best practices for API design

API response caching stores responses locally to serve subsequent requests faster - client-side caching can be implemented using memory cache, localStorage, IndexedDB, or service workers, depending on data size and persistence needs. Consider cache invalidation strategies when data changes.

- **Trade-offs**: Cache responses based on URL, method, and request body to identify duplicates - use memory cache for short-lived data, localStorage/IndexedDB for persistent data. Implement TTL (Time To Live) to expire stale cache entries - use service workers for offline caching and background sync.

Example:

```javascript
class MemoryCache {
  constructor(ttl = 60000) {
    this.cache = new Map();
    this.ttl = ttl;
  }
  set(key, value) {
    this.cache.set(key, { value, timestamp: Date.now() });
  }
  get(key) {
    const item = this.cache.get(key);
    if (!item) return null;
    if (Date.now() - item.timestamp > this.ttl) {
      this.cache.delete(key);
      return null;
    }
    return item.value;
  }
}
const cache = new MemoryCache(60000);
async function fetchWithCache(url, options = {}) {
  const cacheKey = `${url}-${JSON.stringify(options)}`;
  const cached = cache.get(cacheKey);
  if (cached) return cached;
  const response = await fetch(url, options);
  const data = await response.json();
  cache.set(cacheKey, data);
  return data;
}
```

---

---

