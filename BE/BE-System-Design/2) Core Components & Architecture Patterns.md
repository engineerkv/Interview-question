# 2) Core Components & Architecture Patterns (Q11–20)

## 11) What is a message queue, and why is it used (Kafka, RabbitMQ, SQS)?

Concept: Message queues enable asynchronous communication between services by storing and forwarding messages, decoupling producers from consumers.

Example:
```javascript
// RabbitMQ implementation
const amqp = require('amqplib');
const connection = await amqp.connect('amqp://localhost');
const channel = await connection.createChannel();

// Producer
const publishMessage = async (queue, message) => {
  await channel.assertQueue(queue);
  channel.sendToQueue(queue, Buffer.from(JSON.stringify(message)));
};

// Consumer
const consumeMessages = async (queue) => {
  await channel.assertQueue(queue);
  channel.consume(queue, (msg) => {
    if (msg) {
      console.log('Received:', JSON.parse(msg.content));
      channel.ack(msg);
    }
  });
};
```

Deep Insight:
- Decouples services and improves system resilience
- Enables asynchronous processing and better scalability
- Provides message persistence and delivery guarantees
- Different queues have different characteristics (Kafka: high throughput, RabbitMQ: reliability)
- Essential for event-driven architectures and microservices

## 12) What is event-driven architecture?

Concept: Event-driven architecture uses events to trigger and communicate between decoupled services, enabling loose coupling and better scalability.

Example:
```javascript
// Event-driven system
class EventBus {
  constructor() {
    this.listeners = new Map();
  }
  
  on(event, callback) {
    if (!this.listeners.has(event)) {
      this.listeners.set(event, []);
    }
    this.listeners.get(event).push(callback);
  }
  
  emit(event, data) {
    if (this.listeners.has(event)) {
      this.listeners.get(event).forEach(callback => callback(data));
    }
  }
}

// Usage
const eventBus = new EventBus();
eventBus.on('user.created', (user) => {
  sendWelcomeEmail(user);
  createUserProfile(user);
});
```

Deep Insight:
- Enables loose coupling between services
- Improves scalability and fault tolerance
- Supports both synchronous and asynchronous processing
- Events can be stored for replay and debugging
- Requires careful event schema design and versioning

## 13) What is a content delivery network (CDN)?

Concept: A CDN is a distributed network of servers that deliver content to users based on geographic proximity, reducing latency and improving performance.

Example:
```javascript
// CDN integration
const express = require('express');
const app = express();

// Serve static assets through CDN
app.use('/static', express.static('public', {
  maxAge: '1y',
  setHeaders: (res, path) => {
    res.setHeader('Cache-Control', 'public, max-age=31536000');
  }
}));

// Dynamic content with CDN caching
app.get('/api/data', (req, res) => {
  res.setHeader('Cache-Control', 'public, max-age=300');
  res.json({ data: 'cached for 5 minutes' });
});
```

Deep Insight:
- Reduces latency by serving content from edge locations
- Offloads traffic from origin servers
- Improves user experience globally
- Can cache both static and dynamic content
- Requires careful cache invalidation strategies

## 14) What's the difference between a proxy and a load balancer?

Concept: A proxy forwards requests between clients and servers, while a load balancer distributes requests across multiple servers for scalability and availability.

Example:
```javascript
// Simple proxy
const { createProxyMiddleware } = require('http-proxy-middleware');
app.use('/api', createProxyMiddleware({
  target: 'http://localhost:3001',
  changeOrigin: true
}));

// Load balancer
class LoadBalancer {
  constructor(servers) {
    this.servers = servers;
    this.currentIndex = 0;
  }
  
  getNextServer() {
    const server = this.servers[this.currentIndex];
    this.currentIndex = (this.currentIndex + 1) % this.servers.length;
    return server;
  }
}
```

Deep Insight:
- Proxy: Single point of communication, can add functionality
- Load balancer: Distributes load across multiple servers
- Both can provide caching, SSL termination, and security
- Load balancers are essential for horizontal scaling
- Can be combined for complex routing scenarios

## 15) What is circuit breaker pattern, and how does it improve reliability?

Concept: The circuit breaker pattern prevents cascading failures by stopping requests to failing services and providing fallback mechanisms.

Example:
```javascript
class CircuitBreaker {
  constructor(threshold = 5, timeout = 60000) {
    this.threshold = threshold;
    this.timeout = timeout;
    this.failureCount = 0;
    this.state = 'CLOSED';
    this.nextAttempt = Date.now();
  }
  
  async call(fn) {
    if (this.state === 'OPEN') {
      if (Date.now() < this.nextAttempt) {
        throw new Error('Circuit breaker is OPEN');
      }
      this.state = 'HALF_OPEN';
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
  
  onSuccess() {
    this.failureCount = 0;
    this.state = 'CLOSED';
  }
  
  onFailure() {
    this.failureCount++;
    if (this.failureCount >= this.threshold) {
      this.state = 'OPEN';
      this.nextAttempt = Date.now() + this.timeout;
    }
  }
}
```

Deep Insight:
- Prevents cascading failures in distributed systems
- Provides fast failure detection and recovery
- Can be implemented at different levels (service, database, external API)
- Requires careful tuning of thresholds and timeouts
- Essential for building resilient microservices

## 16) What is a service registry in microservice discovery?

Concept: A service registry maintains a list of available services and their locations, enabling service discovery and dynamic routing in microservices.

Example:
```javascript
// Service registry implementation
class ServiceRegistry {
  constructor() {
    this.services = new Map();
  }
  
  register(serviceName, serviceInfo) {
    this.services.set(serviceName, {
      ...serviceInfo,
      lastHeartbeat: Date.now()
    });
  }
  
  discover(serviceName) {
    const service = this.services.get(serviceName);
    if (!service) return null;
    
    // Check if service is still alive
    if (Date.now() - service.lastHeartbeat > 30000) {
      this.services.delete(serviceName);
      return null;
    }
    
    return service;
  }
  
  heartbeat(serviceName) {
    const service = this.services.get(serviceName);
    if (service) {
      service.lastHeartbeat = Date.now();
    }
  }
}
```

Deep Insight:
- Enables dynamic service discovery and load balancing
- Supports health checks and automatic service removal
- Can be implemented as a separate service or embedded
- Popular implementations: Consul, Eureka, etcd
- Essential for microservices architecture

## 17) What is idempotency, and why is it important in distributed systems?

Concept: Idempotency ensures that performing the same operation multiple times has the same effect as performing it once, critical for reliable distributed systems.

Example:
```javascript
// Idempotent API endpoint
const processPayment = async (req, res) => {
  const { idempotencyKey, amount, userId } = req.body;
  
  // Check if request was already processed
  const existingPayment = await Payment.findOne({ idempotencyKey });
  if (existingPayment) {
    return res.json(existingPayment);
  }
  
  // Process payment
  const payment = await Payment.create({
    idempotencyKey,
    amount,
    userId,
    status: 'completed'
  });
  
  res.json(payment);
};

// Idempotent function
const updateUserBalance = async (userId, amount) => {
  const result = await User.updateOne(
    { _id: userId },
    { $inc: { balance: amount } }
  );
  return result;
};
```

Deep Insight:
- Prevents duplicate operations in distributed systems
- Essential for retry mechanisms and fault tolerance
- Can be achieved through unique keys, versioning, or state checks
- Important for financial and critical operations
- Reduces data inconsistency and errors

## 18) What's the difference between synchronous and asynchronous communication?

Concept: Synchronous communication waits for a response, while asynchronous communication doesn't block waiting for a response, each with different trade-offs.

Example:
```javascript
// Synchronous communication
const syncCall = async () => {
  const user = await userService.getUser(userId);
  const orders = await orderService.getOrders(userId);
  return { user, orders };
};

// Asynchronous communication
const asyncCall = async () => {
  const userPromise = userService.getUser(userId);
  const ordersPromise = orderService.getOrders(userId);
  
  const [user, orders] = await Promise.all([userPromise, ordersPromise]);
  return { user, orders };
};

// Message-based asynchronous
const publishEvent = async (event) => {
  await messageQueue.publish('user.updated', event);
  // Don't wait for processing
};
```

Deep Insight:
- Synchronous: Simpler to implement and debug
- Asynchronous: Better performance and scalability
- Synchronous: Can cause cascading failures
- Asynchronous: Requires message handling and error recovery
- Choose based on requirements and system constraints

## 19) What are rate limiting strategies, and how do you prevent abuse?

Concept: Rate limiting controls the number of requests a client can make within a specific time window to prevent abuse and ensure fair resource usage.

Example:
```javascript
// Token bucket rate limiter
class TokenBucket {
  constructor(capacity, refillRate) {
    this.capacity = capacity;
    this.tokens = capacity;
    this.refillRate = refillRate;
    this.lastRefill = Date.now();
  }
  
  allowRequest() {
    this.refill();
    if (this.tokens > 0) {
      this.tokens--;
      return true;
    }
    return false;
  }
  
  refill() {
    const now = Date.now();
    const timePassed = now - this.lastRefill;
    const tokensToAdd = Math.floor(timePassed * this.refillRate / 1000);
    
    this.tokens = Math.min(this.capacity, this.tokens + tokensToAdd);
    this.lastRefill = now;
  }
}

// Sliding window rate limiter
class SlidingWindow {
  constructor(windowSize, maxRequests) {
    this.windowSize = windowSize;
    this.maxRequests = maxRequests;
    this.requests = [];
  }
  
  allowRequest() {
    const now = Date.now();
    const windowStart = now - this.windowSize;
    
    this.requests = this.requests.filter(time => time > windowStart);
    
    if (this.requests.length < this.maxRequests) {
      this.requests.push(now);
      return true;
    }
    return false;
  }
}
```

Deep Insight:
- Prevents abuse and ensures fair resource usage
- Can be implemented at different levels (API, user, IP)
- Different algorithms: fixed window, sliding window, token bucket
- Should be combined with monitoring and alerting
- Consider distributed rate limiting for microservices

## 20) What is eventual consistency, and when is it acceptable?

Concept: Eventual consistency means the system will become consistent over time, acceptable when immediate consistency isn't critical for the use case.

Example:
```javascript
// Eventual consistency example
const updateUserProfile = async (userId, profileData) => {
  // Update primary database
  await primaryDB.users.update(userId, profileData);
  
  // Asynchronously update search index
  searchIndex.updateUser(userId, profileData).catch(console.error);
  
  // Asynchronously update cache
  cache.set(`user:${userId}`, profileData).catch(console.error);
  
  // Asynchronously notify other services
  eventBus.emit('user.updated', { userId, profileData });
};

// Read with eventual consistency
const getUserProfile = async (userId) => {
  // Try cache first, fallback to database
  let profile = await cache.get(`user:${userId}`);
  if (!profile) {
    profile = await primaryDB.users.findById(userId);
    cache.set(`user:${userId}`, profile);
  }
  return profile;
};
```

Deep Insight:
- Acceptable for non-critical data and read-heavy workloads
- Enables better performance and availability
- Requires conflict resolution strategies
- Common in distributed systems and microservices
- Trade-off between consistency and performance