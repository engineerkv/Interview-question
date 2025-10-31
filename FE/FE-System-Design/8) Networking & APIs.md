# 8) Networking & APIs (Q85–105)

---

## 85) How does the internet work, and how do DNS and IP addresses work together?

Concept:
The internet is a global network of interconnected devices communicating via standardized protocols. DNS (Domain Name System) translates human-readable domain names (like example.com) into IP addresses (like 192.0.2.1), which routers use to route data packets across networks to their destination.

Example:
```javascript
// DNS Resolution Process
// 1. Browser checks local cache
// 2. OS resolver queries root DNS server
// 3. Root server directs to TLD (.com) server
// 4. TLD server directs to authoritative server
// 5. Authoritative server returns IP address

// Simulating DNS lookup
async function resolveDNS(hostname) {
  // Browser or OS DNS resolver
  const ip = await dns.lookup(hostname);
  console.log(`${hostname} resolves to ${ip}`);
  
  // Then TCP connection to IP
  const socket = new Socket();
  socket.connect(80, ip);
}

// IP Packet Routing
// Each packet contains:
// - Source IP (your device)
// - Destination IP (server)
// - Data payload
// Routers use routing tables to forward packets
// toward destination based on IP address
```

Deep Insight:
- DNS provides human-friendly names; IP addresses are the actual network identifiers
- DNS caching happens at multiple levels (browser, OS, ISP, root servers)
- IPv4 uses 32-bit addresses (4.3 billion possible); IPv6 uses 128-bit (virtually unlimited)
- DNS resolution typically adds 20-120ms latency; consider preconnect/dns-prefetch
- IP routing is stateless; each packet routed independently toward destination
- TTL (Time To Live) in DNS records controls caching duration

---

## 86) What are internet protocols, and what is the difference between HTTP and HTTPS?

Concept:
Protocols are standardized rules for communication between devices. HTTP (Hypertext Transfer Protocol) is the foundation of web communication, while HTTPS adds encryption via TLS/SSL, ensuring data confidentiality and integrity between client and server.

Example:
```javascript
// HTTP Request (unencrypted)
fetch('http://example.com/api/data')
  .then(res => res.json());

// HTTPS Request (encrypted)
fetch('https://example.com/api/data')
  .then(res => res.json());

// Key Protocols Stack
// Application Layer: HTTP, HTTPS, FTP, SMTP
// Transport Layer: TCP (reliable), UDP (fast)
// Network Layer: IP (routing), ICMP (error messages)
// Link Layer: Ethernet, WiFi

// TLS Handshake (HTTPS)
// 1. Client sends supported cipher suites
// 2. Server responds with certificate and chosen cipher
// 3. Client validates certificate
// 4. Both parties generate session keys
// 5. Encrypted communication begins

// HTTP/1.1 vs HTTP/2 vs HTTP/3
// HTTP/1.1: One request per connection
// HTTP/2: Multiplexing, header compression, server push
// HTTP/3: QUIC protocol, faster handshake, better for mobile
```

Deep Insight:
- HTTP is unencrypted; data can be intercepted and modified (man-in-the-middle attacks)
- HTTPS encrypts data in transit, authenticates server identity, and prevents tampering
- TLS handshake adds initial latency (~100-300ms) but enables secure communication
- Modern browsers mark HTTP sites as "Not Secure" and restrict features
- Always use HTTPS for authentication, payments, and sensitive data
- HTTP/2 and HTTP/3 provide multiplexing and faster connection establishment
- Common protocols: TCP (reliable, ordered), UDP (fast, best-effort), DNS (name resolution), TLS (encryption)

---

## 87) What is REST, and what are the key principles of RESTful API design?

Concept:
REST (Representational State Transfer) is an architectural style for designing web services. RESTful APIs use standard HTTP methods, stateless requests, resource-oriented URLs, and support caching to create scalable, maintainable APIs.

Example:
```javascript
// RESTful API Design Principles

// 1. Resource-Based URLs
// Good: /api/users/123
// Bad: /api/getUser?id=123

// 2. HTTP Methods
// GET: Retrieve resource
fetch('/api/users/123', { method: 'GET' });

// POST: Create new resource
fetch('/api/users', {
  method: 'POST',
  headers: { 'Content-Type': 'application/json' },
  body: JSON.stringify({ name: 'John', email: 'john@example.com' })
});

// PUT: Replace entire resource
fetch('/api/users/123', {
  method: 'PUT',
  headers: { 'Content-Type': 'application/json' },
  body: JSON.stringify({ name: 'John Doe', email: 'john@example.com' })
});

// PATCH: Partial update
fetch('/api/users/123', {
  method: 'PATCH',
  headers: { 'Content-Type': 'application/json' },
  body: JSON.stringify({ name: 'John Doe' })
});

// DELETE: Remove resource
fetch('/api/users/123', { method: 'DELETE' });

// 3. Statelessness
// Each request contains all information needed
// Server doesn't store client session state

// 4. Status Codes
// 200 OK - Success
// 201 Created - Resource created
// 204 No Content - Success, no response body
// 400 Bad Request - Client error
// 401 Unauthorized - Authentication required
// 403 Forbidden - Access denied
// 404 Not Found - Resource doesn't exist
// 409 Conflict - Resource conflict
// 500 Internal Server Error - Server error

// 5. Uniform Interface
// Consistent naming, HTTP methods, status codes
```

Deep Insight:
- Statelessness enables horizontal scaling and better caching
- Resource-oriented design (nouns in URLs, verbs in HTTP methods) improves clarity
- Cacheability: GET requests should be cacheable; POST/PUT/DELETE typically not
- Layered system: Client doesn't need to know if server uses proxies, load balancers
- HATEOAS (Hypermedia as the Engine of Application State) - optional but powerful
- REST works best with standard HTTP caching mechanisms
- Version APIs carefully: URL versioning (/v1/), header versioning, or query params

---

## 88) What are HTTP methods, status codes, and headers, and how are they used in RESTful APIs?

Concept:
HTTP methods define operations on resources, status codes communicate request outcomes, and headers provide metadata about requests/responses. Together, they form the foundation of RESTful API communication.

Example:
```javascript
// HTTP Methods
const methods = {
  GET: 'Retrieve resource (idempotent, cacheable)',
  POST: 'Create resource or perform action (not idempotent)',
  PUT: 'Replace entire resource (idempotent)',
  PATCH: 'Partial update (idempotent)',
  DELETE: 'Remove resource (idempotent)',
  HEAD: 'Get headers only (cacheable)',
  OPTIONS: 'Get allowed methods (CORS preflight)',
  TRACE: 'Echo request (debugging, rarely used)'
};

// Status Code Examples
const statusCodes = {
  // 2xx Success
  200: 'OK - Standard success response',
  201: 'Created - Resource created successfully',
  204: 'No Content - Success, no response body',
  
  // 3xx Redirection
  301: 'Moved Permanently - Use new URL',
  302: 'Found - Temporary redirect',
  304: 'Not Modified - Use cached version',
  
  // 4xx Client Error
  400: 'Bad Request - Invalid request syntax',
  401: 'Unauthorized - Authentication required',
  403: 'Forbidden - Access denied',
  404: 'Not Found - Resource not found',
  409: 'Conflict - Resource conflict',
  429: 'Too Many Requests - Rate limit exceeded',
  
  // 5xx Server Error
  500: 'Internal Server Error - Server error',
  502: 'Bad Gateway - Upstream server error',
  503: 'Service Unavailable - Server overloaded'
};

// Important HTTP Headers
const headers = {
  // Request Headers
  'Content-Type': 'application/json', // Request body format
  'Accept': 'application/json', // Desired response format
  'Authorization': 'Bearer token123', // Authentication
  'User-Agent': 'Mozilla/5.0...', // Client identification
  'If-None-Match': 'etag-value', // Conditional request
  
  // Response Headers
  'Cache-Control': 'max-age=3600', // Caching directives
  'ETag': 'version-123', // Entity tag for caching
  'Location': '/new-url', // Redirect target
  'Set-Cookie': 'session=abc123; HttpOnly; Secure', // Cookie setting
  
  // CORS Headers
  'Access-Control-Allow-Origin': '*',
  'Access-Control-Allow-Methods': 'GET, POST, PUT',
  'Access-Control-Allow-Headers': 'Content-Type'
};

// Practical Example
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

Deep Insight:
- Idempotent methods (GET, PUT, DELETE, PATCH) can be safely retried without side effects
- POST is not idempotent; multiple identical requests may create multiple resources
- Status codes should accurately reflect request outcome; don't use 200 for errors
- Headers provide rich metadata: content negotiation, caching, authentication, CORS
- Cache-Control header is crucial for browser and CDN caching strategies
- Use appropriate status codes for better API usability and error handling
- Content-Type header ensures proper parsing of request/response bodies

---

## 89) What is GraphQL, and how does it solve over-fetching and under-fetching issues?

Concept:
GraphQL is a query language and runtime for APIs that allows clients to request exactly the data they need. Unlike REST, which returns fixed data structures, GraphQL lets clients specify field selection, solving over-fetching (getting unnecessary data) and under-fetching (needing multiple requests) problems.

Example:
```javascript
// REST - Over-fetching example
// GET /api/users/123
// Returns entire user object with all fields
{
  id: 123,
  name: "John",
  email: "john@example.com",
  address: "...", // Not needed
  phone: "...", // Not needed
  preferences: {...}, // Not needed
  // Many more fields client doesn't need
}

// REST - Under-fetching example
// Need multiple requests
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

// GraphQL Schema Definition
const schema = `
  type User {
    id: ID!
    name: String!
    email: String!
    posts: [Post!]!
  }
  
  type Post {
    id: ID!
    title: String!
    content: String!
    createdAt: String!
    author: User!
  }
  
  type Query {
    user(id: ID!): User
    posts(limit: Int): [Post!]!
  }
  
  type Mutation {
    createUser(name: String!, email: String!): User!
    updateUser(id: ID!, name: String): User!
  }
`;

// GraphQL Mutation Example
const mutation = `
  mutation CreateUser($name: String!, $email: String!) {
    createUser(name: $name, email: $email) {
      id
      name
      email
    }
  }
`;

// GraphQL Batching with DataLoader
// Without batching: N+1 queries
users.forEach(async (user) => {
  const posts = await getPostsForUser(user.id); // Separate query each time
});

// With DataLoader batching: Single query
const postLoader = new DataLoader(async (userIds) => {
  // Single query fetching all posts at once
  const posts = await db.posts.find({ userId: { $in: userIds } });
  return userIds.map(id => posts.filter(p => p.userId === id));
});
```

Deep Insight:
- GraphQL schema serves as contract between client and server, enabling strong typing
- Field resolvers allow combining data from multiple sources (databases, APIs, services)
- Batching with DataLoader prevents N+1 query problems
- GraphQL can fetch related data in single request, reducing round trips
- Introspection enables automatic documentation and tooling (GraphQL Playground)
- GraphQL queries are composable; can query nested relationships in one request
- Trade-offs: More complex than REST, harder to cache at HTTP level, requires understanding of resolvers
- Best for: Complex UIs with varying data needs, mobile apps with bandwidth constraints, aggregate APIs

---

## 90) How do you choose between REST and GraphQL based on project requirements?

Concept:
Choose REST for simple CRUD operations, when HTTP caching is critical, or when working with public APIs. Choose GraphQL when you need flexible data fetching, have complex relationships, or want to reduce over-fetching/under-fetching.

Example:
```javascript
// REST is better when:
// 1. Simple CRUD operations
fetch('/api/users', { method: 'GET' });
fetch('/api/users', { method: 'POST', body: {...} });
fetch('/api/users/123', { method: 'PUT', body: {...} });
fetch('/api/users/123', { method: 'DELETE' });

// 2. HTTP caching is critical
// CDN can cache GET /api/users easily
// GraphQL POST requests aren't easily cacheable

// 3. Public API with wide compatibility
// REST works everywhere, GraphQL requires specific client libraries

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

// 2. Mobile app with limited bandwidth
// Fetch only needed fields, not entire objects

// 3. Rapidly changing UI requirements
// No need to modify backend for new data needs

// Hybrid Approach
// Use REST for simple operations
fetch('/api/users/123', { method: 'DELETE' });

// Use GraphQL for complex queries
fetch('/graphql', {
  method: 'POST',
  body: JSON.stringify({ query: complexQuery })
});

// Decision Matrix
const decisionMatrix = {
  useREST: [
    'Simple CRUD operations',
    'HTTP caching is critical',
    'Public API with wide compatibility',
    'File uploads/downloads',
    'Team familiar with REST'
  ],
  useGraphQL: [
    'Complex data relationships',
    'Mobile app with bandwidth constraints',
    'Rapidly changing UI requirements',
    'Need for real-time subscriptions',
    'Team comfortable with GraphQL'
  ]
};
```

Deep Insight:
- REST advantages: Simplicity, HTTP caching, wide tooling support, easier debugging
- GraphQL advantages: Flexible queries, reduced round trips, strong typing, better for complex UIs
- Consider team expertise, infrastructure, and long-term maintenance
- Many companies use hybrid: REST for simple operations, GraphQL for complex queries
- REST caching: Leverage CDN and browser caching for static/public data
- GraphQL caching: Requires application-level caching strategies
- API versioning: REST uses URL versioning; GraphQL uses schema evolution

---

## 91) What is gRPC, and how does it differ from REST APIs?

Concept:
gRPC (gRPC Remote Procedure Calls) is a high-performance RPC framework using Protocol Buffers for serialization and HTTP/2 for transport. It differs from REST by using binary protocols, code generation, streaming, and strong typing.

Example:
```javascript
// REST API Example
// Request: POST /api/users
// Headers: Content-Type: application/json
// Body: {"name": "John", "email": "john@example.com"}

// Response: 201 Created
// Body: {"id": 123, "name": "John", "email": "john@example.com"}

// gRPC Example
// Protocol Buffer Definition (.proto)
syntax = "proto3";

message User {
  int32 id = 1;
  string name = 2;
  string email = 3;
}

message CreateUserRequest {
  string name = 1;
  string email = 2;
}

message CreateUserResponse {
  User user = 1;
}

service UserService {
  rpc CreateUser(CreateUserRequest) returns (CreateUserResponse);
  rpc GetUser(GetUserRequest) returns (User);
  rpc ListUsers(ListUsersRequest) returns (stream User); // Streaming
}

// Client-side (generated from .proto)
const client = new UserServiceClient('https://api.example.com');
const request = new CreateUserRequest();
request.setName('John');
request.setEmail('john@example.com');

const response = await client.createUser(request, {});
const user = response.getUser();

// Server-side streaming
const stream = client.listUsers(request);
stream.on('data', (user) => {
  console.log('User:', user.toObject());
});

// Bidirectional streaming
const stream = client.chat();
stream.write({ message: 'Hello' });
stream.on('data', (message) => {
  console.log('Received:', message.toObject());
});
```

Deep Insight:
- gRPC uses Protocol Buffers (protobuf) - binary format, 3-10x smaller than JSON
- Code generation from .proto files ensures type safety and reduces boilerplate
- HTTP/2 support enables multiplexing, header compression, server push
- Streaming support: Unary (request-response), server streaming, client streaming, bidirectional
- Strong typing through protobuf schemas prevents runtime errors
- Better for: Microservices communication, high-performance APIs, real-time systems
- Limitations: Browser support requires gRPC-Web proxy, less human-readable than JSON
- Use gRPC for: Service-to-service communication, internal APIs, performance-critical systems
- Use REST for: Public APIs, browser clients, when simplicity is priority

---

## 92) What are Protocol Buffers (protobuf), and what are their benefits in gRPC?

Concept:
Protocol Buffers are a language-neutral, platform-neutral serialization format developed by Google. They define data structures in .proto files, which are compiled to generate code in various languages, providing efficient binary serialization for gRPC.

Example:
```javascript
// .proto file definition
syntax = "proto3";

message Person {
  int32 id = 1;
  string name = 2;
  string email = 3;
  repeated string phone_numbers = 4;
  Address address = 5;
  
  enum PhoneType {
    MOBILE = 0;
    HOME = 1;
    WORK = 2;
  }
  
  message PhoneNumber {
    string number = 1;
    PhoneType type = 2;
  }
}

message Address {
  string street = 1;
  string city = 2;
  string state = 3;
  string zip = 4;
}

// After compilation, generates code:
// Person.js (JavaScript)
// Person.java (Java)
// Person.py (Python)
// etc.

// Usage in JavaScript
const Person = require('./generated/Person_pb');

const person = new Person.Person();
person.setId(123);
person.setName('John Doe');
person.setEmail('john@example.com');

// Serialize to binary
const bytes = person.serializeBinary();

// Deserialize from binary
const deserialized = Person.Person.deserializeBinary(bytes);

// Schema Evolution (backward compatible)
// Old schema
message User {
  int32 id = 1;
  string name = 2;
}

// New schema (add field, keep old ones)
message User {
  int32 id = 1;
  string name = 2;
  string email = 3; // New field, optional
}

// Old clients can still read new messages (new fields ignored)
// New clients can read old messages (new fields have default values)
```

Deep Insight:
- Binary format is 3-10x smaller than JSON, reducing network bandwidth
- Strong typing catches errors at compile time, not runtime
- Schema evolution allows adding fields without breaking existing clients
- Code generation reduces boilerplate and ensures consistency across languages
- Faster serialization/deserialization compared to JSON parsing
- Cross-language support: Same .proto file generates code for many languages
- Field numbers (not names) are used in binary format for efficiency
- Default values ensure backward compatibility when adding new fields
- Use for: High-performance APIs, microservices, when type safety matters
- Trade-off: Requires compilation step and less human-readable than JSON

---

## 93) How does gRPC leverage HTTP/2, and what advantages does this bring over HTTP/1.1?

Concept:
gRPC uses HTTP/2 as its transport protocol, which provides multiplexing, header compression, server push, and binary framing. These features enable multiple simultaneous requests over a single connection, reducing latency and improving efficiency compared to HTTP/1.1.

Example:
```javascript
// HTTP/1.1 Limitations
// - One request per connection (or multiple connections needed)
// - Headers sent in plain text (repetitive)
// - No server-initiated communication

// Request 1
fetch('/api/user/1'); // Opens connection, waits for response, closes

// Request 2
fetch('/api/user/2'); // Opens new connection, waits for response, closes

// Request 3
fetch('/api/user/3'); // Opens new connection, waits for response, closes
// Total: 3 connections, sequential execution

// HTTP/2 Advantages (used by gRPC)
// - Multiplexing: Multiple requests over single connection
// - Header compression: HPACK reduces header size
// - Binary framing: More efficient than text-based HTTP/1.1
// - Server push: Server can send resources proactively

// gRPC with HTTP/2 (simultaneous requests)
const client = new UserServiceClient('https://api.example.com');

// All requests use same HTTP/2 connection
Promise.all([
  client.getUser({ id: 1 }),
  client.getUser({ id: 2 }),
  client.getUser({ id: 3 }),
  client.getUser({ id: 4 }),
  client.getUser({ id: 5 })
]);
// Single connection, parallel execution

// HTTP/2 Features in gRPC

// 1. Multiplexing
// Multiple streams (requests) over single TCP connection
// Each stream is independent, doesn't block others

// 2. Header Compression (HPACK)
// HTTP/1.1: Headers sent in full each time (repetitive)
// HTTP/2: Headers compressed and indexed, significant reduction

// 3. Binary Framing
// HTTP/1.1: Text-based protocol
// HTTP/2: Binary protocol, faster parsing

// 4. Server Push
// Server can proactively send resources
// Example: Server pushes related data client will likely need

// Performance Comparison
const comparison = {
  'HTTP/1.1': {
    'Latency': 'Higher (multiple connections, no multiplexing)',
    'Header Overhead': 'High (repetitive headers)',
    'Connection Overhead': 'High (TCP handshake per request)',
    'Concurrent Requests': 'Limited (6 per domain)'
  },
  'HTTP/2': {
    'Latency': 'Lower (multiplexing, single connection)',
    'Header Overhead': 'Low (HPACK compression)',
    'Connection Overhead': 'Low (reused connection)',
    'Concurrent Requests': 'Unlimited (multiple streams)'
  }
};
```

Deep Insight:
- HTTP/2 multiplexing allows multiple requests/responses simultaneously without blocking
- HPACK header compression reduces overhead, especially important for small requests
- Single persistent connection reduces TCP handshake overhead
- Binary framing enables faster parsing and more efficient processing
- Server push enables proactive data delivery, reducing round trips
- HTTP/2 maintains backward compatibility with HTTP/1.1 semantics
- gRPC benefits: Lower latency, higher throughput, better for microservices
- Browser support: gRPC-Web proxy required for browser clients (gRPC uses HTTP/2 but browsers need translation)
- Use HTTP/2/gRPC for: High-performance APIs, microservices, real-time systems
- HTTP/1.1 still common: Public REST APIs, CDN compatibility, legacy systems

---

## 94) Compare RESTful APIs and gRPC: strengths, weaknesses, and when to use each.

Concept:
REST uses HTTP with JSON, is simple and widely compatible. gRPC uses HTTP/2 with Protocol Buffers, offering high performance and strong typing. Choose based on use case: REST for public APIs and simplicity, gRPC for performance-critical internal services.

Example:
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

// Comparison Table

// REST Strengths:
const restStrengths = {
  simplicity: 'Easy to understand and implement',
  compatibility: 'Works everywhere, widely supported',
  caching: 'HTTP caching with CDN and browsers',
  debugging: 'Human-readable JSON, easy to inspect',
  tooling: 'Rich ecosystem (curl, Postman, browser dev tools)',
  publicAPIs: 'Ideal for public-facing APIs'
};

// REST Weaknesses:
const restWeaknesses = {
  performance: 'JSON parsing slower than binary',
  overhead: 'HTTP headers and text format larger',
  typing: 'No built-in type safety',
  streaming: 'Limited streaming support',
  multipleRequests: 'Often requires multiple requests for related data'
};

// gRPC Strengths:
const grpcStrengths = {
  performance: '3-10x faster serialization, smaller payloads',
  typing: 'Strong typing via Protocol Buffers',
  streaming: 'Built-in streaming support (unary, server, client, bidirectional)',
  multiplexing: 'HTTP/2 enables multiple requests over one connection',
  codeGeneration: 'Auto-generated clients reduce boilerplate',
  microservices: 'Excellent for service-to-service communication'
};

// gRPC Weaknesses:
const grpcWeaknesses = {
  browserSupport: 'Requires gRPC-Web proxy for browsers',
  readability: 'Binary format not human-readable',
  caching: 'More complex caching strategies needed',
  learningCurve: 'Requires understanding Protocol Buffers',
  tooling: 'Less tooling than REST ecosystem'
};

// When to Use REST:
const useREST = [
  'Public APIs for web browsers',
  'Simple CRUD operations',
  'When HTTP caching is critical',
  'Team unfamiliar with gRPC',
  'File uploads/downloads',
  'When simplicity is priority'
];

// When to Use gRPC:
const useGRPC = [
  'Microservices communication',
  'High-performance requirements',
  'Real-time streaming needs',
  'Internal service-to-service APIs',
  'When type safety is critical',
  'Mobile apps with bandwidth constraints'
];

// Hybrid Approach
// Use REST for external/public APIs
const publicAPI = 'https://api.example.com/rest';

// Use gRPC for internal microservices
const internalService = new InternalServiceClient('grpc://internal.service');
```

Deep Insight:
- REST is universal: Works with any HTTP client, easy to test with curl/browser
- gRPC is performant: Binary format and HTTP/2 provide significant performance benefits
- Choose REST for: Public APIs, browser clients, when simplicity and caching matter
- Choose gRPC for: Internal services, performance-critical systems, real-time streaming
- Many organizations use both: REST for public APIs, gRPC for internal services
- Migration path: Can evolve REST APIs to gRPC gradually for specific services
- Tooling: REST has better browser/dev tool support; gRPC has better performance tooling
- Team skills: Consider team expertise and learning curve when choosing
- Protocol Buffers enable schema evolution and cross-language type safety
- gRPC-Web allows gRPC in browsers but adds complexity compared to native REST

---
