# 🎯 25 Most Asked Interview Questions for JavaScript Devs in 2025

**For Frontend, Backend & Full-stack Interviews**

---

## 💅 Frontend Interview Questions (Q1–8)

### Q1) What's the difference between 'async' and 'defer' attributes when applied to a `<script/>` tag?

Concept:
Both 'async' and 'defer' download scripts in parallel with HTML parsing, but 'async' executes immediately after download while 'defer' waits for HTML parsing to complete.

Example:
```html
<!-- async - executes immediately after download -->
<script src="analytics.js" async></script>

<!-- defer - executes after HTML parsing -->
<script src="app.js" defer></script>
```

Deep Insight:
- **async**: Best for independent scripts like analytics that don't need DOM
- **defer**: Perfect for scripts that need DOM access like React rendering
- **Blocking**: Regular scripts block HTML parsing until execution completes
- **Order**: 'defer' maintains script execution order, 'async' doesn't
- **Performance**: Both improve page load performance by non-blocking downloads

---

### Q2) JavaScript is a pass-by-reference or pass-by-value language?

Concept:
JavaScript is pass-by-value, but objects create confusion because we pass a copy of the reference pointer, not the object itself.

Example:
```javascript
function modifyValue(primitive, object) {
  primitive = 100; // Won't affect original
  object.name = "Changed"; // Will affect original
}

let num = 5;
let obj = { name: "Original" };
modifyValue(num, obj);
console.log(num); // Still 5
console.log(obj.name); // "Changed"
```

Deep Insight:
- **Primitives**: Always passed by value (copied)
- **Objects**: Reference pointer is copied, but still points to same object
- **Confusion**: Objects appear pass-by-reference but it's actually pass-by-value of reference
- **Memory**: Each function call gets its own copy of parameters
- **Mutation**: Object properties can be changed, but reassignment won't affect original

---

### Q3) Using closures makes JavaScript consume more?

Concept:
Closures consume more memory because they prevent garbage collection of variables in their lexical scope, keeping them in memory as long as the function exists.

Example:
```javascript
function createCounter() {
  let count = 0; // This stays in memory
  return function() {
    count++; // Closure keeps 'count' alive
    return count;
  };
}
const counter = createCounter();
// 'count' variable cannot be garbage collected
```

Deep Insight:
- **Memory Pressure**: Closures prevent garbage collection of referenced variables
- **Lexical Scope**: Functions remember their creation environment
- **Heap Memory**: Variables stay in RAM until closure is released
- **Memory Leaks**: Unintended closures can cause memory leaks
- **Performance**: More closures = more memory usage, not CPU or disk

---

### Q4) How can you improve a bad CLS (Cumulative Layout Shift)?

Concept:
CLS happens when elements shift during page load due to late-loading content. Fix by reserving space and optimizing loading order.

Example:
```html
<!-- Reserve space for images -->
<img src="hero.jpg" width="800" height="400" alt="Hero">

<!-- Extract critical CSS -->
<style>
  .hero { height: 400px; width: 800px; }
</style>

<!-- Use skeleton loading -->
<div class="skeleton">Loading...</div>
```

Deep Insight:
- **Critical CSS**: Extract above-the-fold styles to prevent layout shifts
- **Image Dimensions**: Always specify width/height attributes
- **Skeleton Loading**: Use placeholders for dynamic content
- **Font Loading**: Use font-display: swap to prevent text shifts
- **Measurement**: CLS score should be under 0.1 for good UX

---

### Q5) Which web performance metric is most affected by excessive re-renders?

Concept:
Excessive re-renders primarily impact INP (Interaction to Next Paint) because they delay the time from user interaction to visual response.

Example:
```javascript
// Bad - causes excessive re-renders
function BadComponent() {
  const [count, setCount] = useState(0);
  const expensiveValue = heavyCalculation(); // Runs on every render
  
  return <div onClick={() => setCount(count + 1)}>{expensiveValue}</div>;
}

// Good - optimized with memoization
function GoodComponent() {
  const [count, setCount] = useState(0);
  const expensiveValue = useMemo(() => heavyCalculation(), []);
  
  return <div onClick={() => setCount(count + 1)}>{expensiveValue}</div>;
}
```

Deep Insight:
- **INP Impact**: Re-renders delay interaction response time
- **Target**: INP should be under 200ms for good UX
- **Optimization**: Use React.memo, useMemo, useCallback
- **Early Returns**: Prevent unnecessary renders with early return patterns
- **Profiling**: Use React DevTools to identify re-render causes

---

### Q6) Give an example of something you can do with Class Components that you cannot do with Functional Components in React.

Concept:
Class Components can implement error boundaries using lifecycle methods like componentDidCatch and getDerivedStateFromError, which Functional Components cannot do directly.

Example:
```javascript
class ErrorBoundary extends React.Component {
  constructor(props) {
    super(props);
    this.state = { hasError: false };
  }

  static getDerivedStateFromError(error) {
    return { hasError: true };
  }

  componentDidCatch(error, errorInfo) {
    console.log('Error caught:', error, errorInfo);
  }

  render() {
    if (this.state.hasError) {
      return <h1>Something went wrong.</h1>;
    }
    return this.props.children;
  }
}
```

Deep Insight:
- **Error Boundaries**: Only Class Components can catch errors in child components
- **Lifecycle Methods**: componentDidCatch and getDerivedStateFromError are exclusive
- **Error Logging**: Libraries like react-sentry use Class Components for error boundaries
- **Functional Alternative**: Use libraries or wrapper components for error handling
- **React Future**: Error boundaries might be added to Functional Components later

---

### Q7) Which Web Performance Metric improves most with Server-Side Rendering?

Concept:
SSR improves LCP (Largest Contentful Paint) most because the server pre-renders content, allowing the browser to paint the largest element immediately upon receiving the HTML.

Example:
```javascript
// SSR - Server pre-renders HTML
export async function getServerSideProps() {
  const data = await fetch('https://api.example.com/posts');
  return { props: { posts: await data.json() } };
}

// Client receives pre-rendered HTML
function Blog({ posts }) {
  return (
    <div>
      <h1>Latest Posts</h1> {/* LCP element */}
      {posts.map(post => <Post key={post.id} post={post} />)}
    </div>
  );
}
```

Deep Insight:
- **LCP Improvement**: Pre-rendered content paints immediately
- **FCP**: Also improves as first content appears faster
- **CLS**: Reduces layout shifts with pre-rendered dimensions
- **TTFB**: May increase due to server processing time
- **FID**: Not directly affected by SSR

---

### Q8) What are TypeScript Generics? Give an example of when you should use them.

Concept:
Generics provide type flexibility while maintaining strict type checking by allowing functions and classes to work with different types.

Example:
```typescript
// Generic function
function identity<T>(arg: T): T {
  return arg;
}

// Usage with different types
const stringResult = identity<string>("hello");
const numberResult = identity<number>(42);

// React useState with generics
const [count, setCount] = useState<number>(0);
const [user, setUser] = useState<User | null>(null);
```

Deep Insight:
- **Type Safety**: Maintains type checking while providing flexibility
- **Reusability**: Write once, use with multiple types
- **React Integration**: useState, useRef, and other hooks use generics
- **API Responses**: Perfect for API response typing
- **Constraints**: Can limit generic types with extends keyword

---

## 🛠 Full-stack Interview Questions (Q9–16)

### Q9) What's the difference between git rebase and git merge?

Concept:
Both merge branches, but rebase rewrites history to place commits at the top of the branch, while merge creates a merge commit preserving the original history.

Example:
```bash
# Merge - creates merge commit
git checkout main
git merge feature-branch

# Rebase - rewrites history
git checkout feature-branch
git rebase main
git checkout main
git merge feature-branch
```

Deep Insight:
- **History**: Rebase creates linear history, merge preserves branching
- **Commits**: Rebase rewrites commit hashes, merge preserves them
- **Conflicts**: Rebase requires resolving conflicts per commit
- **Team Work**: Rebase can cause issues with shared branches
- **Clean History**: Rebase creates cleaner, more readable history

---

### Q10) Which HTTP Status Code represents Forbidden Access?

Concept:
403 Forbidden means the client provided credentials but lacks permission to access the specific resource, while 401 means no credentials were provided.

Example:
```javascript
// 401 Unauthorized - no credentials
if (!req.headers.authorization) {
  return res.status(401).json({ error: 'No token provided' });
}

// 403 Forbidden - has credentials but no permission
if (!user.hasPermission('admin')) {
  return res.status(403).json({ error: 'Insufficient permissions' });
}
```

Deep Insight:
- **401**: Authentication required but not provided
- **403**: Authentication provided but authorization denied
- **4xx**: Client-side errors (400-499 range)
- **Security**: 403 is more specific than 401
- **Headers**: 401 should include WWW-Authenticate header

---

### Q11) What is a preflight request in the context of HTTP?

Concept:
A preflight request is an OPTIONS request sent by browsers before certain cross-origin requests to check CORS permissions with the server.

Example:
```javascript
// Browser automatically sends preflight for this request
fetch('https://api.example.com/data', {
  method: 'POST',
  headers: {
    'Content-Type': 'application/json',
    'Authorization': 'Bearer token'
  },
  body: JSON.stringify({ data: 'value' })
});

// Server must respond to OPTIONS request
app.options('/data', (req, res) => {
  res.header('Access-Control-Allow-Origin', '*');
  res.header('Access-Control-Allow-Methods', 'POST');
  res.header('Access-Control-Allow-Headers', 'Content-Type, Authorization');
  res.send();
});
```

Deep Insight:
- **Automatic**: Browsers send preflight automatically for certain requests
- **OPTIONS**: Always an OPTIONS request, not the actual request
- **CORS**: Checks if cross-origin request is allowed
- **Headers**: Triggered by custom headers or non-simple methods
- **Caching**: Preflight responses can be cached by browsers

---

### Q12) Content Negotiation is a mechanism used to...

Concept:
Content negotiation allows servers to serve the same resource in different formats (compressed, different languages, etc.) based on client preferences in HTTP headers.

Example:
```javascript
// Client request with Accept headers
fetch('/api/data', {
  headers: {
    'Accept': 'application/json, application/xml;q=0.9',
    'Accept-Encoding': 'gzip, deflate, br',
    'Accept-Language': 'en-US, en;q=0.9'
  }
});

// Server response based on client preferences
app.get('/api/data', (req, res) => {
  const accepts = req.headers.accept;
  if (accepts.includes('application/json')) {
    res.json(data);
  } else if (accepts.includes('application/xml')) {
    res.xml(data);
  }
});
```

Deep Insight:
- **Client Preference**: Server chooses format based on Accept headers
- **Compression**: Enables gzip/brotli compression automatically
- **Language**: Supports multiple languages for same content
- **Quality Values**: q=0.9 indicates preference weight
- **Performance**: Reduces bandwidth through compression

---

### Q13) Which of the following are valid ways to version an API?

Concept:
API versioning can be done through URI paths, query parameters, or Accept headers, with URI versioning being most common due to better separation of concerns.

Example:
```javascript
// URI versioning (most common)
app.use('/api/v1', v1Routes);
app.use('/api/v2', v2Routes);

// Query parameter versioning
app.get('/api/users', (req, res) => {
  const version = req.query.version || 'v1';
  // Handle version logic
});

// Header versioning
app.get('/api/users', (req, res) => {
  const version = req.headers['api-version'] || 'v1';
  // Handle version logic
});
```

Deep Insight:
- **URI Versioning**: Most common, clear separation, easy to cache
- **Query Parameters**: Flexible but can cause caching issues
- **Headers**: Clean URLs but less discoverable
- **Breaking Changes**: Version when making incompatible changes
- **Deprecation**: Plan for deprecating old versions

---

### Q14) Which of the following methods are idempotent in REST?

Concept:
GET, PUT, and DELETE are idempotent because repeating the same request multiple times produces the same result, while POST and PATCH are not idempotent.

Example:
```javascript
// Idempotent - same result every time
GET /api/users/123        // Always returns same user
PUT /api/users/123        // Always updates to same state
DELETE /api/users/123     // Always deletes (or returns 404)

// Not idempotent - different results
POST /api/users           // Creates new user each time
PATCH /api/users/123      // May have different effects
```

Deep Insight:
- **Idempotency**: Same request = same result, regardless of repetitions
- **Network Issues**: Important for retry logic in unreliable networks
- **Microservices**: Critical for distributed systems
- **Caching**: Idempotent requests are safe to cache
- **Error Handling**: Retry idempotent requests safely

---

### Q15) What's the difference between Web Sockets and Server Sent Events?

Concept:
WebSockets enable bidirectional communication between client and server, while Server-Sent Events provide unidirectional communication from server to client only.

Example:
```javascript
// WebSocket - bidirectional
const ws = new WebSocket('ws://localhost:8080');
ws.onopen = () => ws.send('Hello Server');
ws.onmessage = (event) => console.log(event.data);

// Server-Sent Events - unidirectional
const eventSource = new EventSource('/events');
eventSource.onmessage = (event) => console.log(event.data);
// Cannot send data back to server
```

Deep Insight:
- **WebSockets**: Full duplex, real-time chat, gaming
- **SSE**: One-way, live updates, notifications
- **Reconnection**: SSE has built-in reconnection
- **Protocol**: WebSockets use ws://, SSE uses HTTP
- **Browser Support**: Both have excellent modern browser support

---

### Q16) Can you define Cyclomatic Complexity?

Concept:
Cyclomatic complexity measures the number of linearly independent paths through code, helping identify overly complex functions that are hard to test and maintain.

Example:
```javascript
// Complexity = 1 (simple path)
function simple() {
  return x + y;
}

// Complexity = 3 (if + else + default)
function complex(score) {
  if (score >= 90) return 'A';
  else if (score >= 80) return 'B';
  else return 'C';
}

// Complexity = 4 (if + else + for + while)
function veryComplex(data) {
  if (data.length === 0) return [];
  
  for (let i = 0; i < data.length; i++) {
    while (data[i] > 0) {
      data[i]--;
    }
  }
  return data;
}
```

Deep Insight:
- **Measurement**: Counts decision points (if, for, while, switch)
- **Target**: Keep complexity under 10 for maintainability
- **Testing**: Higher complexity = more test cases needed
- **Refactoring**: Break complex functions into smaller ones
- **Tools**: SonarQube, ESLint can measure complexity

---

## ⚙️ Backend Interview Questions (Q17–25)

### Q17) A database index makes database queries faster by...

Concept:
Indexes create B-tree data structures that enable logarithmic time O(log n) lookups instead of linear time O(n) full table scans, dramatically improving query performance.

Example:
```sql
-- Create index on frequently queried column
CREATE INDEX idx_user_email ON users(email);

-- Query uses index for fast lookup
SELECT * FROM users WHERE email = 'user@example.com';

-- Without index: O(n) - scans all rows
-- With index: O(log n) - binary search in B-tree
```

Deep Insight:
- **B-tree Structure**: Enables logarithmic search time
- **Performance**: 1M rows = 19 lookups vs 1M scans
- **Trade-off**: Faster reads, slower writes (index maintenance)
- **Memory**: Indexes consume RAM for faster access
- **Selectivity**: More unique values = better index performance

---

### Q18) Which of the following will prevent a DDoS attack?

Concept:
Load balancers with traffic filtering are most effective against DDoS attacks because they can block malicious IPs and distribute legitimate traffic across multiple servers.

Example:
```javascript
// Load balancer configuration
const express = require('express');
const rateLimit = require('express-rate-limit');

const app = express();

// Rate limiting (helps but not primary DDoS defense)
app.use(rateLimit({
  windowMs: 15 * 60 * 1000, // 15 minutes
  max: 100 // limit each IP to 100 requests per windowMs
}));

// Traffic filtering at load balancer level
// - Block known malicious IPs
// - Geographic filtering
// - Request pattern analysis
```

Deep Insight:
- **Load Balancers**: Primary defense against DDoS
- **Traffic Filtering**: Block malicious IPs and patterns
- **Rate Limiting**: Helps but not effective against distributed attacks
- **CDN**: Can absorb and filter traffic before reaching origin
- **Scaling**: Auto-scaling can handle traffic spikes

---

### Q19) In the context of Open-Closed Principle, which best explains what "closed" means?

Concept:
The Open-Closed Principle states that classes should be closed for modification but open for extension, meaning you can add new behavior without changing existing code.

Example:
```javascript
// Closed for modification, open for extension
class PaymentProcessor {
  processPayment(amount, paymentMethod) {
    return paymentMethod.process(amount);
  }
}

// Extend without modifying PaymentProcessor
class CreditCardPayment {
  process(amount) {
    return `Processing $${amount} via credit card`;
  }
}

class PayPalPayment {
  process(amount) {
    return `Processing $${amount} via PayPal`;
  }
}
```

Deep Insight:
- **Closed**: No changes to existing code
- **Open**: New functionality through extension
- **SOLID**: Part of SOLID principles for maintainable code
- **Polymorphism**: Use interfaces/abstract classes for extension points
- **React**: Props and composition enable open-closed principle

---

### Q20) Which deployment has zero downtime?

Concept:
Blue/Green deployment achieves zero downtime by maintaining two identical environments and switching traffic only after the new environment is fully tested and ready.

Example:
```yaml
# Blue/Green deployment process
# 1. Deploy to Green environment
# 2. Run health checks
# 3. Switch load balancer to Green
# 4. Keep Blue for rollback

version: '3.8'
services:
  app-blue:
    image: myapp:v1.0
    ports: ["3000:3000"]
  
  app-green:
    image: myapp:v1.1
    ports: ["3001:3000"]
  
  load-balancer:
    image: nginx
    # Switch between blue and green
```

Deep Insight:
- **Zero Downtime**: No service interruption during deployment
- **Two Environments**: Blue (current) and Green (new)
- **Health Checks**: Verify new environment before switch
- **Rollback**: Keep old environment for quick rollback
- **Cost**: Requires double infrastructure during deployment

---

### Q21) To prevent a Man-in-the-Middle Attack, we have to...

Concept:
Use TLS (HTTPS) to encrypt communication between client and server, preventing attackers from intercepting and reading data in transit.

Example:
```javascript
// HTTPS server with TLS encryption
const https = require('https');
const fs = require('fs');

const options = {
  key: fs.readFileSync('private-key.pem'),
  cert: fs.readFileSync('certificate.pem')
};

https.createServer(options, (req, res) => {
  res.writeHead(200);
  res.end('Secure connection!');
}).listen(443);
```

Deep Insight:
- **TLS Encryption**: End-to-end encryption of data in transit
- **Certificate Validation**: Verify server identity
- **HTTPS Everywhere**: Use HTTPS for all communications
- **HSTS**: HTTP Strict Transport Security prevents downgrade attacks
- **Perfect Forward Secrecy**: Use ephemeral keys for additional security

---

### Q22) Which of the following qualify as reverse proxy?

Concept:
Load balancers, CDNs, and API Gateways are reverse proxies because they act on behalf of the server to handle client requests, while VPNs and client-side caches act on behalf of the client.

Example:
```javascript
// API Gateway as reverse proxy
const express = require('express');
const { createProxyMiddleware } = require('http-proxy-middleware');

const app = express();

// Route requests to different services
app.use('/api/users', createProxyMiddleware({
  target: 'http://user-service:3001',
  changeOrigin: true
}));

app.use('/api/orders', createProxyMiddleware({
  target: 'http://order-service:3002',
  changeOrigin: true
}));
```

Deep Insight:
- **Reverse Proxy**: Acts on behalf of server
- **Load Balancer**: Distributes traffic across multiple servers
- **CDN**: Caches content closer to users
- **API Gateway**: Routes and manages API requests
- **Benefits**: Load balancing, caching, SSL termination, security

---

### Q23) Which is a disadvantage of Round Robin algorithm in Load Balancers?

Concept:
Round Robin assumes all servers are equally performant and all requests consume the same resources, leading to unfair load distribution when servers have different capacities.

Example:
```javascript
// Round Robin - simple but unfair
class RoundRobinBalancer {
  constructor(servers) {
    this.servers = servers;
    this.currentIndex = 0;
  }

  getNextServer() {
    const server = this.servers[this.currentIndex];
    this.currentIndex = (this.currentIndex + 1) % this.servers.length;
    return server; // Ignores server load/capacity
  }
}

// Better: Least Connections
class LeastConnectionsBalancer {
  getNextServer() {
    return this.servers.reduce((min, server) => 
      server.connections < min.connections ? server : min
    );
  }
}
```

Deep Insight:
- **Unfair Distribution**: Doesn't consider server capacity or current load
- **Server Differences**: Servers may have different CPU, memory, or processing power
- **Better Algorithms**: Least Connections, Weighted Round Robin, APM-based
- **Monitoring**: Use metrics to make informed load balancing decisions
- **Health Checks**: Ensure servers are healthy before routing traffic

---

### Q24) The so-called Microservices Tax refers to...

Concept:
Microservices Tax refers to the additional complexity and overhead required to implement and maintain a microservices architecture compared to a monolithic system.

Example:
```javascript
// Monolith - simple communication
const userService = require('./services/user');
const orderService = require('./services/order');

// Microservices - complex communication
const userService = require('user-service-client');
const orderService = require('order-service-client');

// Additional complexity:
// - Service discovery
// - Circuit breakers
// - Distributed logging
// - Inter-service authentication
// - Network latency
// - Data consistency
```

Deep Insight:
- **Complexity**: More moving parts and failure points
- **Networking**: Inter-service communication overhead
- **Data Management**: Distributed data consistency challenges
- **Monitoring**: Need distributed tracing and logging
- **Team Structure**: Requires different organizational approach

---

### Q25) Which statements about garbage collection and memory leaks are true?

Concept:
Memory leaks can still occur in garbage-collected languages due to closures and circular references, which prevent the garbage collector from reclaiming memory.

Example:
```javascript
// Memory leak - closure keeps reference
function createLeak() {
  const largeData = new Array(1000000).fill('data');
  
  return function() {
    // This closure keeps 'largeData' in memory
    console.log('Closure executed');
  };
}

// Memory leak - circular reference
let obj1 = { name: 'obj1' };
let obj2 = { name: 'obj2' };
obj1.ref = obj2;
obj2.ref = obj1; // Circular reference
// Both objects cannot be garbage collected
```

Deep Insight:
- **Garbage Collection**: Automatically frees unused memory
- **Memory Leaks**: Can still occur in GC languages
- **Closures**: Keep references to outer scope variables
- **Circular References**: Prevent GC from reclaiming memory
- **Not Real-time**: GC runs periodically, not immediately

---

## 📊 Summary

These 25 questions cover the most frequently asked topics in JavaScript developer interviews for 2025, spanning:

- **Frontend**: Performance, React, TypeScript, Web APIs
- **Full-stack**: HTTP, Git, APIs, Real-time communication
- **Backend**: Databases, Security, Architecture, Deployment

Each question includes a clear concept explanation, practical code example, and deep insights covering core rules, real-world applications, common mistakes, advanced concepts, and interview tips.

**Preparation Strategy:**
1. Understand the core concepts thoroughly
2. Practice coding examples from memory
3. Be ready to explain trade-offs and alternatives
4. Connect concepts to real-world scenarios
5. Prepare follow-up questions for deeper discussion
