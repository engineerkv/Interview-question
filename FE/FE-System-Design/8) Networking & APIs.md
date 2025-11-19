# 8. Networking & APIs (Q85–105)

---

## Q85. How does the internet work, and how do DNS and IP addresses work together?

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

## Q86. What are internet protocols, and what is the difference between HTTP and HTTPS?

Protocols are standardized rules for communication between devices. HTTP (Hypertext Transfer Protocol) is the foundation of web communication, while HTTPS adds encryption via TLS/SSL, ensuring data confidentiality and integrity between client and server - always use HTTPS for authentication, payments, and sensitive data.

- **Trade-offs**: HTTP is unencrypted so data can be intercepted and modified (man-in-the-middle attacks), while HTTPS encrypts data in transit, authenticates server identity, and prevents tampering. The catch is TLS handshake adds initial latency (~100-300ms) but enables secure communication - HTTP/2 and HTTP/3 provide multiplexing and faster connection establishment.

Example:

```javascript
fetch('http://example.com/api/data').then(res => res.json());
fetch('https://example.com/api/data').then(res => res.json());
```

---

## Q87. What is REST, and what are the key principles of RESTful API design?

REST (Representational State Transfer) is an architectural style for designing web services - RESTful APIs use standard HTTP methods, stateless requests, resource-oriented URLs, and support caching to create scalable, maintainable APIs. REST works best with standard HTTP caching mechanisms.

- **Trade-offs**: Statelessness enables horizontal scaling and better caching - resource-oriented design (nouns in URLs, verbs in HTTP methods) improves clarity, but watch out - GET requests should be cacheable while POST/PUT/DELETE typically aren't. HATEOAS (Hypermedia as the Engine of Application State) is optional but powerful.

Example:

```javascript
fetch('/api/users/123', { method: 'GET' });
fetch('/api/users', {
  method: 'POST',
  headers: { 'Content-Type': 'application/json' },
  body: JSON.stringify({ name: 'John', email: 'john@example.com' })
});
fetch('/api/users/123', { method: 'PUT', body: JSON.stringify({ name: 'John Doe' }) });
fetch('/api/users/123', { method: 'DELETE' });
```

---

## Q88. What are HTTP methods, status codes, and headers?

HTTP methods define operations on resources, status codes communicate request outcomes, and headers provide metadata about requests/responses - together they form the foundation of RESTful API communication. Cache-Control header is crucial for browser and CDN caching strategies.

- **Trade-offs**: Idempotent methods (GET, PUT, DELETE, PATCH) can be safely retried without side effects, but POST is not idempotent - multiple identical requests may create multiple resources. Status codes should accurately reflect request outcome - don't use 200 for errors. Headers provide rich metadata for content negotiation, caching, authentication, and CORS.

Example:

```javascript
async function fetchUser(id) {
  const response = await fetch(`/api/users/${id}`, {
    method: 'GET',
    headers: { 'Accept': 'application/json', 'Authorization': `Bearer ${token}` }
  });
  if (response.status === 200) return await response.json();
  if (response.status === 404) throw new Error('User not found');
  if (response.status === 401) throw new Error('Authentication required');
}
```

---

## Q89. What is GraphQL, and how does it solve over-fetching and under-fetching issues?

GraphQL is a query language and runtime for APIs that allows clients to request exactly the data they need - unlike REST which returns fixed data structures, GraphQL lets clients specify field selection, solving over-fetching (getting unnecessary data) and under-fetching (needing multiple requests) problems. Best for complex UIs with varying data needs and mobile apps with bandwidth constraints.

- **Trade-offs**: GraphQL schema serves as contract between client and server, enabling strong typing - field resolvers allow combining data from multiple sources (databases, APIs, services), but watch out - batching with DataLoader prevents N+1 query problems. GraphQL can fetch related data in single request, reducing round trips.

Example:

```javascript
const query = `
  query GetUser($id: ID!) {
    user(id: $id) {
      id
      name
      email
      posts { title, createdAt }
    }
  }
`;
const response = await fetch('/graphql', {
  method: 'POST',
  headers: { 'Content-Type': 'application/json' },
  body: JSON.stringify({ query, variables: { id: '123' } })
});
```

---

## Q90. How do you choose between REST and GraphQL?

Choose REST for simple CRUD operations, when HTTP caching is critical, or when working with public APIs. Choose GraphQL when you need flexible data fetching, have complex relationships, or want to reduce over-fetching/under-fetching - API versioning differs: REST uses URL versioning while GraphQL uses schema evolution.

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

## Q91. What is gRPC, and how does it differ from REST APIs?

gRPC (gRPC Remote Procedure Calls) is a high-performance RPC framework using Protocol Buffers for serialization and HTTP/2 for transport - it differs from REST by using binary protocols, code generation, streaming, and strong typing. Better for microservices communication, high-performance APIs, and real-time systems.

- **Trade-offs**: gRPC uses Protocol Buffers (protobuf) - binary format that's 3-10x smaller than JSON - code generation from .proto files ensures type safety and reduces boilerplate. HTTP/2 support enables multiplexing, header compression, and server push - streaming support includes unary (request-response), server streaming, client streaming, and bidirectional.

Example:

```javascript
syntax = "proto3";
message User {
  int32 id = 1;
  string name = 2;
  string email = 3;
}
service UserService {
  rpc CreateUser(CreateUserRequest) returns (User);
}
```

---

## Q92. What are Protocol Buffers (protobuf), and what are their benefits?

Protocol Buffers are a language-neutral, platform-neutral serialization format developed by Google - they define data structures in .proto files, which are compiled to generate code in various languages, providing efficient binary serialization for gRPC. Faster serialization/deserialization compared to JSON parsing.

- **Trade-offs**: Binary format is 3-10x smaller than JSON, reducing network bandwidth - strong typing catches errors at compile time, not runtime. Schema evolution allows adding fields without breaking existing clients - code generation reduces boilerplate and ensures consistency across languages.

Example:

```javascript
syntax = "proto3";
message Person {
  int32 id = 1;
  string name = 2;
  string email = 3;
}
const Person = require('./generated/Person_pb');
const person = new Person.Person();
person.setId(123);
const bytes = person.serializeBinary();
```

---

## Q93. How does gRPC leverage HTTP/2, and what advantages does this bring?

gRPC uses HTTP/2 as its transport protocol, which provides multiplexing, header compression, server push, and binary framing - these features enable multiple simultaneous requests over a single connection, reducing latency and improving efficiency compared to HTTP/1.1. Server push enables proactive data delivery, reducing round trips.

- **Trade-offs**: HTTP/2 multiplexing allows multiple requests/responses simultaneously without blocking - HPACK header compression reduces overhead, especially important for small requests. Single persistent connection reduces TCP handshake overhead - binary framing enables faster parsing and more efficient processing.

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

## Q94. Compare RESTful APIs and gRPC: strengths, weaknesses, and when to use each.

REST uses HTTP with JSON, is simple and widely compatible - gRPC uses HTTP/2 with Protocol Buffers, offering high performance and strong typing. Choose based on use case: REST for public APIs and simplicity, gRPC for performance-critical internal services - consider team expertise and learning curve when choosing.

- **Trade-offs**: REST is universal (works with any HTTP client, easy to test) while gRPC is performant (binary format and HTTP/2 provide significant performance benefits). Choose REST for public APIs, browser clients, when simplicity and caching matter - many organizations use both: REST for public APIs, gRPC for internal services. Can evolve REST APIs to gRPC gradually for specific services.

Example:

```javascript
fetch('https://api.example.com/users/123', {
  method: 'GET',
  headers: { 'Accept': 'application/json' }
}).then(res => res.json());

const client = new UserServiceClient('https://api.example.com');
const user = await client.getUser({ id: 123 });
```

---

## Q95. What is API versioning, and what are the different strategies?

API versioning allows you to evolve APIs without breaking existing clients - common strategies include URL versioning, header versioning, and query parameter versioning, each with different trade-offs. Choose based on caching needs, URL cleanliness, and team preferences.

- **Trade-offs**: URL versioning is most explicit and cacheable, but requires URL changes - header versioning maintains clean URLs but requires custom headers. Query parameter versioning is simple but less cacheable - media type versioning follows content negotiation principles.

Example:

```javascript
fetch('/api/v1/users/123');
fetch('/api/users/123', {
  headers: { 'Accept': 'application/vnd.api.v1+json' }
});
fetch('/api/users/123?version=1');
```

---

## Q96. What is CORS, and how do you handle cross-origin requests securely?

CORS (Cross-Origin Resource Sharing) is a security mechanism that allows web pages to make requests to a different domain than the one serving the web page - it requires proper configuration on the server to allow specific origins, methods, and headers. Configure CORS properly to prevent security vulnerabilities.

- **Trade-offs**: CORS prevents unauthorized cross-origin requests while allowing legitimate ones - preflight requests check permissions before actual requests. Use specific origins instead of wildcard (*) for security - Access-Control-Allow-Credentials allows cookies and auth headers.

Example:

```javascript
fetch('https://api.example.com/users', {
  method: 'GET',
  headers: { 'Accept': 'application/json' }
});
fetch('https://api.example.com/users', {
  method: 'POST',
  headers: { 'Content-Type': 'application/json', 'Authorization': 'Bearer token123' },
  body: JSON.stringify({ name: 'John' })
});
```

---

## Q97. What is API rate limiting, and how do you implement it on the front-end?

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

## Q98. What is API authentication, and what are common authentication methods?

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

## Q99. What are request/response interceptors, and how do you use them?

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

## Q100. What is API error handling, and how do you handle different types of errors gracefully?

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

## Q101. What is API pagination, and what are different pagination strategies?

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

## Q102. What is API request batching, and how do you implement it?

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

## Q103. What is API request deduplication, and how do you prevent duplicate requests?

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

## Q104. What is API response caching, and how do you implement client-side caching?

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

## Q105. What is API request retry logic, and how do you implement exponential backoff?

API request retry logic automatically retries failed requests with increasing delays between attempts - exponential backoff doubles the delay after each retry, preventing server overload and improving success rates for transient failures. Set maximum retry attempts and maximum delay to prevent infinite retries.

- **Trade-offs**: Exponential backoff doubles delay after each retry, preventing server overload - retry transient failures (network errors, 5xx server errors) with exponential backoff. Add jitter (random variation) to prevent multiple clients retrying simultaneously - use different retry strategies for different error types (network, server, timeout).

Example:

```javascript
async function fetchWithRetry(url, options = {}, maxRetries = 3) {
  let lastError;
  for (let attempt = 0; attempt <= maxRetries; attempt++) {
    try {
      const response = await fetch(url, options);
      if (!response.ok && response.status >= 500) {
        throw new Error(`Server error: ${response.status}`);
      }
      return await response.json();
    } catch (error) {
      lastError = error;
      if (attempt < maxRetries) {
        const delay = Math.min(1000 * Math.pow(2, attempt), 30000);
        await new Promise(resolve => setTimeout(resolve, delay));
      }
    }
  }
  throw lastError;
}
function calculateBackoff(attempt, baseDelay = 1000, maxDelay = 30000) {
  const exponentialDelay = Math.min(baseDelay * Math.pow(2, attempt), maxDelay);
  const jitter = Math.random() * 0.3 * exponentialDelay;
  return exponentialDelay + jitter;
}
```

---
