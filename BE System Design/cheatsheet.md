# ⚙️ Backend System Design Cheatsheet

## 🚀 Quick Reference for Backend System Design Interviews

---

## 🏗️ **Architecture Patterns**

### **Monolithic vs Microservices**
```javascript
// Monolithic
const app = express();
app.use('/users', userRoutes);
app.use('/orders', orderRoutes);
// All in one codebase

// Microservices
const userService = express();
const orderService = express();
// Independent services
```

### **Scaling Strategies**
- **Vertical Scaling**: Increase server resources (CPU, RAM)
- **Horizontal Scaling**: Add more servers
- **Load Balancing**: Distribute traffic across servers

---

## 🗄️ **Database Design**

### **SQL vs NoSQL**
```sql
-- SQL (ACID, Structured)
CREATE TABLE users (
  id INT PRIMARY KEY,
  name VARCHAR(100),
  email VARCHAR(100)
);

-- NoSQL (Flexible, Scalable)
{
  _id: ObjectId(),
  name: 'John Doe',
  email: 'john@example.com'
}
```

### **Indexing Strategies**
```sql
-- Single column index
CREATE INDEX idx_email ON users(email);

-- Composite index
CREATE INDEX idx_name_email ON users(name, email);

-- Partial index
CREATE INDEX idx_active_users ON users(email) 
WHERE status = 'active';
```

### **Sharding Patterns**
```javascript
// Horizontal sharding
const shardKey = userId % 4;
const shard = `shard_${shardKey}`;

// Vertical sharding
const userShard = 'user_db';
const orderShard = 'order_db';
```

---

## ⚡ **Performance Optimization**

### **Caching Strategies**
```javascript
// Cache-aside pattern
async function getUsers() {
  let users = await cache.get('users');
  if (!users) {
    users = await db.query('SELECT * FROM users');
    await cache.set('users', users, 3600);
  }
  return users;
}

// Write-through pattern
async function updateUser(id, data) {
  await db.update('users', id, data);
  await cache.set(`user_${id}`, data);
}
```

### **Connection Pooling**
```javascript
const pool = new Pool({
  max: 20,
  min: 5,
  idle: 10000
});

async function getUsers() {
  const client = await pool.connect();
  try {
    return await client.query('SELECT * FROM users');
  } finally {
    client.release();
  }
}
```

---

## 🔄 **Message Queues**

### **Queue Patterns**
```javascript
// Producer
queue.add('process-email', {
  userId: 123,
  email: 'user@example.com'
});

// Consumer
queue.process('process-email', async (job) => {
  await sendEmail(job.data.email);
});
```

### **Queue Types**
- **FIFO**: First In, First Out
- **Priority**: High priority first
- **Dead Letter**: Failed messages
- **Delay**: Scheduled processing

---

## 🔒 **Security**

### **Authentication**
```javascript
// JWT Authentication
const token = jwt.sign({ userId: 123 }, secret, { expiresIn: '1h' });

// OAuth2
const authUrl = `https://auth.example.com/authorize?` +
  `client_id=${clientId}&` +
  `redirect_uri=${redirectUri}&` +
  `response_type=code`;
```

### **Security Headers**
```javascript
app.use(helmet({
  contentSecurityPolicy: {
    directives: {
      defaultSrc: ["'self'"],
      scriptSrc: ["'self'", "'unsafe-inline'"]
    }
  }
}));
```

---

## ☁️ **AWS Services**

### **Compute**
- **EC2**: Virtual machines
- **ECS**: Container service
- **Lambda**: Serverless functions
- **EKS**: Kubernetes service

### **Database**
- **RDS**: Managed SQL databases
- **DynamoDB**: NoSQL database
- **ElastiCache**: In-memory cache

### **Storage**
- **S3**: Object storage
- **CloudFront**: CDN
- **EFS**: File system

### **Networking**
- **VPC**: Virtual private cloud
- **ALB**: Application load balancer
- **Route 53**: DNS service

---

## 📊 **Monitoring & Observability**

### **Three Pillars**
1. **Logs**: Event records
2. **Metrics**: Performance measurements
3. **Traces**: Request flows

### **Tools**
- **Prometheus**: Metrics collection
- **Grafana**: Data visualization
- **ELK Stack**: Log analysis
- **Jaeger**: Distributed tracing

---

## 🚦 **Rate Limiting**

### **Algorithms**
```javascript
// Token bucket
class TokenBucket {
  constructor(capacity, refillRate) {
    this.capacity = capacity;
    this.tokens = capacity;
    this.refillRate = refillRate;
  }
  
  consume(tokens = 1) {
    this.refill();
    if (this.tokens >= tokens) {
      this.tokens -= tokens;
      return true;
    }
    return false;
  }
}
```

### **Rate Limiting Types**
- **Fixed Window**: Requests per time window
- **Sliding Window**: Smooth rate limiting
- **Token Bucket**: Allow bursts
- **Leaky Bucket**: Smooth traffic

---

## 🔄 **Circuit Breaker**

```javascript
class CircuitBreaker {
  constructor(threshold, timeout) {
    this.threshold = threshold;
    this.timeout = timeout;
    this.failureCount = 0;
    this.state = 'CLOSED';
  }
  
  async call(fn) {
    if (this.state === 'OPEN') {
      throw new Error('Circuit breaker is OPEN');
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
}
```

---

## 📈 **Load Testing**

### **Metrics**
- **RPS**: Requests per second
- **Latency**: Response time
- **Throughput**: Data processed
- **Error Rate**: Failed requests

### **Tools**
- **Apache JMeter**: Load testing
- **Artillery**: Node.js load testing
- **k6**: Modern load testing
- **Gatling**: High-performance testing

---

## 🏢 **System Design Patterns**

### **CQRS (Command Query Responsibility Segregation)**
```javascript
// Command side
async function createUser(userData) {
  await commandDb.insert('users', userData);
  await eventBus.publish('user-created', userData);
}

// Query side
async function getUsers() {
  return await queryDb.select('users');
}
```

### **Event Sourcing**
```javascript
// Store events instead of state
const events = [
  { type: 'UserCreated', data: { id: 1, name: 'John' } },
  { type: 'UserUpdated', data: { id: 1, email: 'john@example.com' } }
];

// Rebuild state from events
const user = events.reduce((state, event) => {
  return applyEvent(state, event);
}, {});
```

---

## 🔧 **Common Interview Questions**

### **Design a URL Shortener**
1. **Requirements**: Shorten URLs, redirect, analytics
2. **Database**: Store mappings, use hash for short URL
3. **Caching**: Cache popular URLs
4. **Scaling**: Shard by hash, use CDN

### **Design a Chat System**
1. **Real-time**: WebSockets for bidirectional communication
2. **Storage**: Store messages in database
3. **Scaling**: Use message queues, horizontal scaling
4. **Features**: Presence, typing indicators, file sharing

### **Design a Payment System**
1. **Security**: PCI DSS compliance, encryption
2. **Processing**: Payment gateway integration
3. **Fraud**: Detection and prevention
4. **Compliance**: Regulatory requirements

---

## 📚 **Key Concepts to Remember**

### **CAP Theorem**
- **Consistency**: All nodes see same data
- **Availability**: System remains operational
- **Partition Tolerance**: System continues despite network failures
- **Choose 2 of 3**

### **ACID Properties**
- **Atomicity**: All or nothing
- **Consistency**: Valid state transitions
- **Isolation**: Concurrent transactions don't interfere
- **Durability**: Committed changes persist

### **SOLID Principles**
- **S**: Single Responsibility
- **O**: Open/Closed
- **L**: Liskov Substitution
- **I**: Interface Segregation
- **D**: Dependency Inversion

---

## 🎯 **Interview Tips**

### **System Design Process**
1. **Clarify Requirements**: Ask questions
2. **Estimate Scale**: Users, data, requests
3. **Design Core**: Start with basic design
4. **Scale Up**: Add caching, load balancing
5. **Optimize**: Identify bottlenecks
6. **Discuss Trade-offs**: Pros and cons

### **Common Mistakes**
- Don't jump to microservices immediately
- Consider data consistency requirements
- Think about failure scenarios
- Discuss monitoring and observability
- Consider security from the start

---

## 🔗 **Useful Resources**

### **Books**
- "Designing Data-Intensive Applications" by Martin Kleppmann
- "System Design Interview" by Alex Xu
- "Building Microservices" by Sam Newman

### **Online Resources**
- High Scalability blog
- AWS Architecture Center
- Google Cloud Architecture Center
- Microsoft Azure Architecture Center

---

*This cheatsheet provides a quick reference for backend system design interviews, covering essential concepts, patterns, and best practices for building scalable, reliable, and secure systems.*
