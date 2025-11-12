# 🌐 8. Networking & APIs (Q85–105)

---

## 🧩 Q85. How does the internet work, and how do DNS and IP addresses work together?

### 🧠 Concept

The internet is a global network of interconnected devices communicating via standardized protocols. DNS (Domain Name System) translates human-readable domain names (like example.com) into IP addresses (like 192.0.2.1), which routers use to route data packets across networks to their destination. IP routing is stateless; each packet routed independently toward destination.

---

### 💡 Example

```javascript
// DNS Resolution Process
async function resolveDNS(hostname) {
  const ip = await dns.lookup(hostname);
  console.log(`${hostname} resolves to ${ip}`);
  
  // Then TCP connection to IP
  const socket = new Socket();
  socket.connect(80, ip);
}
```

---

### 🔍 Deep Insights

* **Rule:** DNS provides human-friendly names; IP addresses are the actual network identifiers.
* **Use Case:** DNS caching happens at multiple levels (browser, OS, ISP, root servers).
* **Common Mistake:** IPv4 uses 32-bit addresses (4.3 billion possible); IPv6 uses 128-bit (virtually unlimited).
* **Pro Tip:** DNS resolution typically adds 20-120ms latency; consider preconnect/dns-prefetch.

---

### ⭐ Senior Takeaway

IP routing is stateless; each packet routed independently toward destination.

---

## 🧩 Q86. What are internet protocols, and what is the difference between HTTP and HTTPS?

### 🧠 Concept

Protocols are standardized rules for communication between devices. HTTP (Hypertext Transfer Protocol) is the foundation of web communication, while HTTPS adds encryption via TLS/SSL, ensuring data confidentiality and integrity between client and server. Always use HTTPS for authentication, payments, and sensitive data.

---

### 💡 Example

```javascript
// HTTP Request (unencrypted)
fetch('http://example.com/api/data')
  .then(res => res.json());

// HTTPS Request (encrypted)
fetch('https://example.com/api/data')
  .then(res => res.json());
```

---

### 🔍 Deep Insights

* **Rule:** HTTP is unencrypted; data can be intercepted and modified (man-in-the-middle attacks).
* **Use Case:** HTTPS encrypts data in transit, authenticates server identity, and prevents tampering.
* **Common Mistake:** TLS handshake adds initial latency (~100-300ms) but enables secure communication.
* **Pro Tip:** HTTP/2 and HTTP/3 provide multiplexing and faster connection establishment.

---

### ⭐ Senior Takeaway

Always use HTTPS for authentication, payments, and sensitive data.

---

## 🧩 Q87. What is REST, and what are the key principles of RESTful API design?

### 🧠 Concept

REST (Representational State Transfer) is an architectural style for designing web services. RESTful APIs use standard HTTP methods, stateless requests, resource-oriented URLs, and support caching to create scalable, maintainable APIs. REST works best with standard HTTP caching mechanisms.

---

### 💡 Example

```javascript
// Resource-Based URLs
fetch('/api/users/123', { method: 'GET' });

fetch('/api/users', {
  method: 'POST',
  headers: { 'Content-Type': 'application/json' },
  body: JSON.stringify({ name: 'John', email: 'john@example.com' })
});

fetch('/api/users/123', {
  method: 'PUT',
  headers: { 'Content-Type': 'application/json' },
  body: JSON.stringify({ name: 'John Doe', email: 'john@example.com' })
});

fetch('/api/users/123', { method: 'DELETE' });
```

---

### 🔍 Deep Insights

* **Rule:** Statelessness enables horizontal scaling and better caching.
* **Use Case:** Resource-oriented design (nouns in URLs, verbs in HTTP methods) improves clarity.
* **Common Mistake:** Cacheability: GET requests should be cacheable; POST/PUT/DELETE typically not.
* **Pro Tip:** HATEOAS (Hypermedia as the Engine of Application State) - optional but powerful.

---

### ⭐ Senior Takeaway

REST works best with standard HTTP caching mechanisms.

---

## 🧩 Q88. What are HTTP methods, status codes, and headers?

### 🧠 Concept

HTTP methods define operations on resources, status codes communicate request outcomes, and headers provide metadata about requests/responses. Together, they form the foundation of RESTful API communication. Cache-Control header is crucial for browser and CDN caching strategies.

---

### 💡 Example

```javascript
async function fetchUser(id) {
  const response = await fetch(`/api/users/${id}`, {
    method: 'GET',
    headers: {
      'Accept': 'application/json',
      'Authorization': `Bearer ${token}`
    }
  });
  
  if (response.status === 200) {
    return await response.json();
  } else if (response.status === 404) {
    throw new Error('User not found');
  } else if (response.status === 401) {
    throw new Error('Authentication required');
  }
}
```

---

### 🔍 Deep Insights

* **Rule:** Idempotent methods (GET, PUT, DELETE, PATCH) can be safely retried without side effects.
* **Use Case:** POST is not idempotent; multiple identical requests may create multiple resources.
* **Common Mistake:** Status codes should accurately reflect request outcome; don't use 200 for errors.
* **Pro Tip:** Headers provide rich metadata: content negotiation, caching, authentication, CORS.

---

### ⭐ Senior Takeaway

Cache-Control header is crucial for browser and CDN caching strategies.

---

## 🧩 Q89. What is GraphQL, and how does it solve over-fetching and under-fetching issues?

### 🧠 Concept

GraphQL is a query language and runtime for APIs that allows clients to request exactly the data they need. Unlike REST, which returns fixed data structures, GraphQL lets clients specify field selection, solving over-fetching (getting unnecessary data) and under-fetching (needing multiple requests) problems. Best for complex UIs with varying data needs, mobile apps with bandwidth constraints.

---

### 💡 Example

```javascript
// REST - Under-fetching example
const user = await fetch('/api/users/123');
const posts = await fetch('/api/users/123/posts');
const friends = await fetch('/api/users/123/friends');

// GraphQL - Request exactly what you need
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

### 🔍 Deep Insights

* **Rule:** GraphQL schema serves as contract between client and server, enabling strong typing.
* **Use Case:** Field resolvers allow combining data from multiple sources (databases, APIs, services).
* **Common Mistake:** Batching with DataLoader prevents N+1 query problems.
* **Pro Tip:** GraphQL can fetch related data in single request, reducing round trips.

---

### ⭐ Senior Takeaway

Best for complex UIs with varying data needs, mobile apps with bandwidth constraints.

---

## 🧩 Q90. How do you choose between REST and GraphQL?

### 🧠 Concept

Choose REST for simple CRUD operations, when HTTP caching is critical, or when working with public APIs. Choose GraphQL when you need flexible data fetching, have complex relationships, or want to reduce over-fetching/under-fetching. API versioning: REST uses URL versioning; GraphQL uses schema evolution.

---

### 💡 Example

```javascript
// REST is better when:
// 1. Simple CRUD operations
fetch('/api/users', { method: 'GET' });
fetch('/api/users', { method: 'POST', body: {...} });

// 2. HTTP caching is critical
// CDN can cache GET /api/users easily
// GraphQL POST requests aren't easily cacheable

// GraphQL is better when:
// 1. Complex data relationships
const query = `
  query GetDashboard {
    user {
      profile { name, avatar }
      posts { title, comments { author, text } }
      friends { name, mutualFriends { name } }
    }
  }
`;
```

---

### 🔍 Deep Insights

* **Rule:** REST advantages (simplicity, HTTP caching, wide tooling support, easier debugging), GraphQL advantages (flexible queries, reduced round trips, strong typing, better for complex UIs).
* **Use Case:** Consider team expertise, infrastructure, and long-term maintenance.
* **Common Mistake:** Many companies use hybrid: REST for simple operations, GraphQL for complex queries.
* **Pro Tip:** REST caching leverages CDN and browser caching; GraphQL caching requires application-level strategies.

---

### ⭐ Senior Takeaway

API versioning: REST uses URL versioning; GraphQL uses schema evolution.

---

## 🧩 Q91. What is gRPC, and how does it differ from REST APIs?

### 🧠 Concept

gRPC (gRPC Remote Procedure Calls) is a high-performance RPC framework using Protocol Buffers for serialization and HTTP/2 for transport. It differs from REST by using binary protocols, code generation, streaming, and strong typing. Better for microservices communication, high-performance APIs, real-time systems.

---

### 💡 Example

```javascript
// REST API Example
fetch('https://api.example.com/users', {
  method: 'POST',
  headers: { 'Content-Type': 'application/json' },
  body: JSON.stringify({ name: 'John', email: 'john@example.com' })
});

// gRPC Example
// Protocol Buffer Definition (.proto)
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

### 🔍 Deep Insights

* **Rule:** gRPC uses Protocol Buffers (protobuf) - binary format, 3-10x smaller than JSON.
* **Use Case:** Code generation from .proto files ensures type safety and reduces boilerplate.
* **Common Mistake:** HTTP/2 support enables multiplexing, header compression, server push.
* **Pro Tip:** Streaming support: Unary (request-response), server streaming, client streaming, bidirectional.

---

### ⭐ Senior Takeaway

Better for microservices communication, high-performance APIs, real-time systems.

---

## 🧩 Q92. What are Protocol Buffers (protobuf), and what are their benefits?

### 🧠 Concept

Protocol Buffers are a language-neutral, platform-neutral serialization format developed by Google. They define data structures in .proto files, which are compiled to generate code in various languages, providing efficient binary serialization for gRPC. Faster serialization/deserialization compared to JSON parsing.

---

### 💡 Example

```javascript
// .proto file definition
syntax = "proto3";
message Person {
  int32 id = 1;
  string name = 2;
  string email = 3;
  repeated string phone_numbers = 4;
}

// After compilation, generates code:
// Person.js (JavaScript), Person.java (Java), Person.py (Python)

// Usage in JavaScript
const Person = require('./generated/Person_pb');
const person = new Person.Person();
person.setId(123);
person.setName('John Doe');

// Serialize to binary
const bytes = person.serializeBinary();
```

---

### 🔍 Deep Insights

* **Rule:** Binary format is 3-10x smaller than JSON, reducing network bandwidth.
* **Use Case:** Strong typing catches errors at compile time, not runtime.
* **Common Mistake:** Schema evolution allows adding fields without breaking existing clients.
* **Pro Tip:** Code generation reduces boilerplate and ensures consistency across languages.

---

### ⭐ Senior Takeaway

Faster serialization/deserialization compared to JSON parsing.

---

## 🧩 Q93. How does gRPC leverage HTTP/2, and what advantages does this bring?

### 🧠 Concept

gRPC uses HTTP/2 as its transport protocol, which provides multiplexing, header compression, server push, and binary framing. These features enable multiple simultaneous requests over a single connection, reducing latency and improving efficiency compared to HTTP/1.1. Server push enables proactive data delivery, reducing round trips.

---

### 💡 Example

```javascript
// HTTP/1.1 Limitations
// - One request per connection (or multiple connections needed)
// - Headers sent in plain text (repetitive)
// - No server-initiated communication

// Request 1
fetch('/api/user/1'); // Opens connection, waits for response, closes

// Request 2
fetch('/api/user/2'); // Opens new connection, waits for response, closes

// gRPC with HTTP/2 (simultaneous requests)
const client = new UserServiceClient('https://api.example.com');
Promise.all([
  client.getUser({ id: 1 }),
  client.getUser({ id: 2 }),
  client.getUser({ id: 3 })
]);
// Single connection, parallel execution
```

---

### 🔍 Deep Insights

* **Rule:** HTTP/2 multiplexing allows multiple requests/responses simultaneously without blocking.
* **Use Case:** HPACK header compression reduces overhead, especially important for small requests.
* **Common Mistake:** Single persistent connection reduces TCP handshake overhead.
* **Pro Tip:** Binary framing enables faster parsing and more efficient processing.

---

### ⭐ Senior Takeaway

Server push enables proactive data delivery, reducing round trips.

---

## 🧩 Q94. Compare RESTful APIs and gRPC: strengths, weaknesses, and when to use each.

### 🧠 Concept

REST uses HTTP with JSON, is simple and widely compatible. gRPC uses HTTP/2 with Protocol Buffers, offering high performance and strong typing. Choose based on use case: REST for public APIs and simplicity, gRPC for performance-critical internal services. Consider team expertise and learning curve when choosing.

---

### 💡 Example

```javascript
// REST API Example
// Simple, human-readable, easy to debug
fetch('https://api.example.com/users/123', {
  method: 'GET',
  headers: { 'Accept': 'application/json' }
})
  .then(res => res.json())
  .then(data => console.log(data));

// gRPC Example
// High performance, type-safe, efficient
const client = new UserServiceClient('https://api.example.com');
const user = await client.getUser({ id: 123 });
```

---

### 🔍 Deep Insights

* **Rule:** REST is universal (works with any HTTP client, easy to test), gRPC is performant (binary format and HTTP/2 provide significant performance benefits).
* **Use Case:** Choose REST for public APIs, browser clients, when simplicity and caching matter.
* **Common Mistake:** Many organizations use both: REST for public APIs, gRPC for internal services.
* **Pro Tip:** Can evolve REST APIs to gRPC gradually for specific services.

---

### ⭐ Senior Takeaway

Consider team expertise and learning curve when choosing.

---

## 🧩 Q95. What is API versioning, and what are the different strategies?

### 🧠 Concept

API versioning allows you to evolve APIs without breaking existing clients. Common strategies include URL versioning, header versioning, and query parameter versioning, each with different trade-offs. Choose based on caching needs, URL cleanliness, and team preferences.

---

### 💡 Example

```javascript
// 1. URL Versioning (Most Common)
fetch('/api/v1/users/123');
fetch('/api/v2/users/123');

// 2. Header Versioning
fetch('/api/users/123', {
  headers: {
    'Accept': 'application/vnd.api.v1+json'
  }
});

// 3. Query Parameter Versioning
fetch('/api/users/123?version=1');
```

---

### 🔍 Deep Insights

* **Rule:** URL versioning is most explicit and cacheable, but requires URL changes.
* **Use Case:** Header versioning maintains clean URLs but requires custom headers.
* **Common Mistake:** Query parameter versioning is simple but less cacheable.
* **Pro Tip:** Media type versioning follows content negotiation principles.

---

### ⭐ Senior Takeaway

Choose based on caching needs, URL cleanliness, and team preferences.

---

## 🧩 Q96. What is CORS, and how do you handle cross-origin requests securely?

### 🧠 Concept

CORS (Cross-Origin Resource Sharing) is a security mechanism that allows web pages to make requests to a different domain than the one serving the web page. It requires proper configuration on the server to allow specific origins, methods, and headers. Configure CORS properly to prevent security vulnerabilities.

---

### 💡 Example

```javascript
// Simple Request (no preflight)
fetch('https://api.example.com/users', {
  method: 'GET',
  headers: { 'Accept': 'application/json' }
});

// Preflight Request (for complex requests)
fetch('https://api.example.com/users', {
  method: 'POST',
  headers: {
    'Content-Type': 'application/json',
    'Authorization': 'Bearer token123'
  },
  body: JSON.stringify({ name: 'John' })
});
```

---

### 🔍 Deep Insights

* **Rule:** CORS prevents unauthorized cross-origin requests while allowing legitimate ones.
* **Use Case:** Preflight requests check permissions before actual requests.
* **Common Mistake:** Use specific origins instead of wildcard (*) for security.
* **Pro Tip:** Access-Control-Allow-Credentials allows cookies and auth headers.

---

### ⭐ Senior Takeaway

Configure CORS properly to prevent security vulnerabilities.

---

## 🧩 Q97. What is API rate limiting, and how do you implement it on the front-end?

### 🧠 Concept

API rate limiting restricts the number of requests a client can make within a time period. Front-end implementation involves tracking request counts, handling rate limit responses, and providing user feedback. Provide clear user feedback when rate limits are hit.

---

### 💡 Example

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

const limiter = new RateLimiter(10, 60000); // 10 requests per minute

async function fetchWithRateLimit(url) {
  if (!limiter.canMakeRequest()) {
    throw new Error('Rate limit exceeded');
  }
  const response = await fetch(url);
  if (response.status === 429) {
    const retryAfter = response.headers.get('Retry-After');
    console.warn(`Rate limited. Retry after ${retryAfter} seconds`);
  }
  return response.json();
}
```

---

### 🔍 Deep Insights

* **Rule:** Rate limiting prevents API abuse and ensures fair resource usage.
* **Use Case:** Track request counts and handle 429 (Too Many Requests) responses.
* **Common Mistake:** Use rate limit headers (X-RateLimit-Remaining, X-RateLimit-Reset) for user feedback.
* **Pro Tip:** Implement exponential backoff for retries after rate limit errors.

---

### ⭐ Senior Takeaway

Provide clear user feedback when rate limits are hit.

---

## 🧩 Q98. What is API authentication, and what are common authentication methods?

### 🧠 Concept

API authentication verifies the identity of clients making requests. Common methods include JWT tokens, OAuth 2.0, and API keys, each with different security levels and use cases. Choose authentication method based on security requirements and use case.

---

### 💡 Example

```javascript
// JWT Authentication
const token = localStorage.getItem('authToken');
fetch('/api/users', {
  headers: {
    'Authorization': `Bearer ${token}`
  }
});

// OAuth 2.0 Flow
// 1. Redirect to authorization server
const authUrl = 'https://auth.example.com/authorize?' +
  'client_id=client123&' +
  'redirect_uri=https://app.example.com/callback&' +
  'response_type=code&' +
  'scope=read write';

// 2. Handle callback and exchange code for token
const code = new URLSearchParams(window.location.search).get('code');
const response = await fetch('https://auth.example.com/token', {
  method: 'POST',
  body: JSON.stringify({
    grant_type: 'authorization_code',
    code: code,
    client_id: 'client123'
  })
});
const { access_token } = await response.json();
```

---

### 🔍 Deep Insights

* **Rule:** JWT (stateless, scalable), OAuth 2.0 (secure, standardized), API keys (simple, less secure).
* **Use Case:** JWT for stateless authentication, OAuth for third-party integrations.
* **Common Mistake:** Store tokens securely (httpOnly cookies for refresh tokens, secure storage for access tokens).
* **Pro Tip:** Implement token refresh logic to handle expired tokens automatically.

---

### ⭐ Senior Takeaway

Choose authentication method based on security requirements and use case.

---

## 🧩 Q99. What are request/response interceptors, and how do you use them?

### 🧠 Concept

Request/response interceptors allow you to modify requests before they're sent and responses before they're processed. They're useful for adding authentication headers, handling errors globally, and logging. Interceptors reduce boilerplate and provide consistent error handling.

---

### 💡 Example

```javascript
import axios from 'axios';

// Request Interceptor
axios.interceptors.request.use(
  (config) => {
    const token = localStorage.getItem('authToken');
    if (token) {
      config.headers.Authorization = `Bearer ${token}`;
    }
    return config;
  },
  (error) => Promise.reject(error)
);

// Response Interceptor
axios.interceptors.response.use(
  (response) => response,
  async (error) => {
    const originalRequest = error.config;
    
    // Handle 401 Unauthorized (token expired)
    if (error.response?.status === 401 && !originalRequest._retry) {
      originalRequest._retry = true;
      
      try {
        // Refresh token
        const refreshToken = localStorage.getItem('refreshToken');
        const response = await axios.post('/api/auth/refresh', { refreshToken });
        const { accessToken } = response.data;
        localStorage.setItem('authToken', accessToken);
        
        // Retry original request with new token
        originalRequest.headers.Authorization = `Bearer ${accessToken}`;
        return axios(originalRequest);
      } catch (refreshError) {
        localStorage.removeItem('authToken');
        window.location.href = '/login';
        return Promise.reject(refreshError);
      }
    }
    
    return Promise.reject(error);
  }
);
```

---

### 🔍 Deep Insights

* **Rule:** Interceptors provide centralized request/response handling.
* **Use Case:** Add authentication headers, handle token refresh, log requests.
* **Common Mistake:** Use interceptors for error handling, retries, and request transformation.
* **Pro Tip:** Implement retry logic with exponential backoff in interceptors.

---

### ⭐ Senior Takeaway

Interceptors reduce boilerplate and provide consistent error handling.

---

## 🧩 Q100. What is API error handling, and how do you handle different types of errors gracefully?

### 🧠 Concept

API error handling involves detecting, categorizing, and responding to different error types (network errors, HTTP errors, validation errors) with appropriate user feedback and recovery strategies. Provide clear, actionable error messages to users.

---

### 💡 Example

```javascript
class APIError extends Error {
  constructor(message, status, code) {
    super(message);
    this.name = 'APIError';
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
        case 400:
          throw new APIError(errorData.message || 'Bad Request', 400, 'BAD_REQUEST');
        case 401:
          throw new APIError('Authentication required', 401, 'UNAUTHORIZED');
        case 403:
          throw new APIError('Access denied', 403, 'FORBIDDEN');
        case 404:
          throw new APIError('Resource not found', 404, 'NOT_FOUND');
        case 429:
          throw new APIError('Too many requests', 429, 'RATE_LIMITED');
        case 500:
          throw new APIError('Server error', 500, 'SERVER_ERROR');
        default:
          throw new APIError(errorData.message || 'An error occurred', response.status, 'UNKNOWN_ERROR');
      }
    }
    
    return await response.json();
  } catch (error) {
    if (error instanceof APIError) {
      throw error;
    }
    
    // Network errors
    if (error.name === 'TypeError' && error.message.includes('fetch')) {
      throw new APIError('Network error. Please check your connection.', 0, 'NETWORK_ERROR');
    }
    
    throw error;
  }
}
```

---

### 🔍 Deep Insights

* **Rule:** Categorize errors by type (network, HTTP, validation) and handle appropriately.
* **Use Case:** Provide user-friendly error messages and recovery options.
* **Common Mistake:** Handle 401 by redirecting to login, 429 with retry logic, network errors with offline indicators.
* **Pro Tip:** Implement retry logic with exponential backoff for transient errors.

---

### ⭐ Senior Takeaway

Provide clear, actionable error messages to users.

---

## 🧩 Q101. What is API pagination, and what are different pagination strategies?

### 🧠 Concept

API pagination breaks large result sets into smaller chunks. Common strategies include offset-based (page numbers), cursor-based (after/before tokens), and keyset-based (last seen ID) pagination, each with different trade-offs. Choose pagination strategy based on data characteristics and use case.

---

### 💡 Example

```javascript
// Offset-Based Pagination
async function fetchUsersWithOffset(page = 1, limit = 20) {
  const response = await fetch(`/api/users?page=${page}&limit=${limit}`);
  const data = await response.json();
  return {
    users: data.items,
    page: data.page,
    totalPages: data.totalPages,
    hasNextPage: data.page < data.totalPages
  };
}

// Cursor-Based Pagination
async function fetchUsersWithCursor(cursor = null, limit = 20) {
  const url = cursor 
    ? `/api/users?cursor=${cursor}&limit=${limit}`
    : `/api/users?limit=${limit}`;
  
  const response = await fetch(url);
  const data = await response.json();
  return {
    users: data.items,
    nextCursor: data.nextCursor,
    hasNextPage: !!data.nextCursor
  };
}
```

---

### 🔍 Deep Insights

* **Rule:** Offset-based (simple, but inefficient for large datasets), Cursor-based (efficient, handles new data well), Keyset-based (efficient, good for sorted data).
* **Use Case:** Cursor-based pagination is best for infinite scroll and real-time data.
* **Common Mistake:** Offset-based is easier to implement but has performance issues with large offsets.
* **Pro Tip:** Keyset-based pagination is most efficient for sorted, indexed data.

---

### ⭐ Senior Takeaway

Choose pagination strategy based on data characteristics and use case.

---

## 🧩 Q102. What is API request batching, and how do you implement it?

### 🧠 Concept

API request batching combines multiple requests into a single request to reduce round trips and improve performance. It's useful when you need to fetch multiple resources simultaneously. Balance batch size with latency - larger batches reduce requests but increase delay.

---

### 💡 Example

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
    const requests = batch.map(item => item.request);
    
    const response = await fetch('/api/batch', {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify({ requests })
    });
    
    const results = await response.json();
    batch.forEach((item, index) => {
      if (results[index].success) {
        item.resolve(results[index].data);
      } else {
        item.reject(new Error(results[index].error));
      }
    });
  }
  
  scheduleBatch() {
    if (this.timeout) clearTimeout(this.timeout);
    this.timeout = setTimeout(() => this.processBatch(), this.delay);
  }
}
```

---

### 🔍 Deep Insights

* **Rule:** Request batching reduces network round trips and improves performance.
* **Use Case:** Useful when fetching multiple related resources simultaneously.
* **Common Mistake:** Batch requests based on size limit or time delay.
* **Pro Tip:** Implement smart batching that groups related requests together.

---

### ⭐ Senior Takeaway

Balance batch size with latency - larger batches reduce requests but increase delay.

---

## 🧩 Q103. What is API request deduplication, and how do you prevent duplicate requests?

### 🧠 Concept

API request deduplication prevents multiple identical requests from being sent simultaneously. It's useful when the same request is triggered multiple times (e.g., rapid button clicks, multiple component renders). Combine with debouncing/throttling for user interactions.

---

### 💡 Example

```javascript
class RequestDeduplicator {
  constructor() {
    this.pendingRequests = new Map();
  }
  
  async deduplicate(key, requestFn) {
    // Check if request is already pending
    if (this.pendingRequests.has(key)) {
      return this.pendingRequests.get(key);
    }
    
    // Create new request
    const promise = requestFn()
      .then(result => {
        this.pendingRequests.delete(key);
        return result;
      })
      .catch(error => {
        this.pendingRequests.delete(key);
        throw error;
      });
    
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

### 🔍 Deep Insights

* **Rule:** Request deduplication prevents unnecessary network requests and reduces server load.
* **Use Case:** Useful when same request triggered multiple times (rapid clicks, multiple renders).
* **Common Mistake:** Use request keys (URL + method + body) to identify duplicate requests.
* **Pro Tip:** Implement request caching with TTL for repeated requests.

---

### ⭐ Senior Takeaway

Combine with debouncing/throttling for user interactions.

---

## 🧩 Q104. What is API response caching, and how do you implement client-side caching?

### 🧠 Concept

API response caching stores responses locally to serve subsequent requests faster. Client-side caching can be implemented using memory cache, localStorage, IndexedDB, or service workers, depending on data size and persistence needs. Consider cache invalidation strategies when data changes.

---

### 💡 Example

```javascript
// Memory Cache Implementation
class MemoryCache {
  constructor(ttl = 60000) {
    this.cache = new Map();
    this.ttl = ttl;
  }
  
  set(key, value) {
    this.cache.set(key, {
      value,
      timestamp: Date.now()
    });
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

// Cached Fetch Implementation
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

### 🔍 Deep Insights

* **Rule:** Cache responses based on URL, method, and request body to identify duplicates.
* **Use Case:** Use memory cache for short-lived data, localStorage/IndexedDB for persistent data.
* **Common Mistake:** Implement TTL (Time To Live) to expire stale cache entries.
* **Pro Tip:** Use service workers for offline caching and background sync.

---

### ⭐ Senior Takeaway

Consider cache invalidation strategies when data changes.

---

## 🧩 Q105. What is API request retry logic, and how do you implement exponential backoff?

### 🧠 Concept

API request retry logic automatically retries failed requests with increasing delays between attempts. Exponential backoff doubles the delay after each retry, preventing server overload and improving success rates for transient failures. Set maximum retry attempts and maximum delay to prevent infinite retries.

---

### 💡 Example

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
        // Calculate exponential backoff delay
        const delay = Math.min(1000 * Math.pow(2, attempt), 30000); // Max 30s
        await new Promise(resolve => setTimeout(resolve, delay));
      }
    }
  }
  
  throw lastError;
}

// Advanced Retry with Jitter
function calculateBackoff(attempt, baseDelay = 1000, maxDelay = 30000) {
  const exponentialDelay = Math.min(
    baseDelay * Math.pow(2, attempt),
    maxDelay
  );
  
  // Add jitter to prevent thundering herd
  const jitter = Math.random() * 0.3 * exponentialDelay; // 30% jitter
  return exponentialDelay + jitter;
}
```

---

### 🔍 Deep Insights

* **Rule:** Exponential backoff doubles delay after each retry, preventing server overload.
* **Use Case:** Retry transient failures (network errors, 5xx server errors) with exponential backoff.
* **Common Mistake:** Add jitter (random variation) to prevent multiple clients retrying simultaneously.
* **Pro Tip:** Use different retry strategies for different error types (network, server, timeout).

---

### ⭐ Senior Takeaway

Set maximum retry attempts and maximum delay to prevent infinite retries.

---
