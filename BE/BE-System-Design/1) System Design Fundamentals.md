# 1) System Design Fundamentals (Q1–10)

## 1) What is system design, and why is it critical for backend engineers?

Concept: System design is the process of defining the architecture, components, and interfaces of a system to meet specific requirements, ensuring scalability, reliability, and maintainability.

Example:
```javascript
// System design example: API Gateway
const express = require('express');
const rateLimit = require('express-rate-limit');
const helmet = require('helmet');

const app = express();
app.use(helmet());
app.use(rateLimit({ windowMs: 15 * 60 * 1000, max: 100 }));

app.use('/api/users', require('./routes/users'));
app.use('/api/orders', require('./routes/orders'));
app.listen(3000);
```

Deep Insight:
- System design ensures scalability and performance at scale
- Helps identify bottlenecks and optimization opportunities
- Enables better communication between teams and stakeholders
- Critical for making informed technology choices
- Essential for building maintainable and reliable systems

## 2) Explain monolithic vs microservices architectures.

Concept: Monolithic architecture has all components in a single application, while microservices split functionality into independent services that communicate over networks.

Example:
```javascript
// Monolithic approach
const app = express();
app.use('/users', userRoutes);
app.use('/orders', orderRoutes);
app.use('/payments', paymentRoutes);

// Microservices approach
const userService = express();
userService.use('/users', userRoutes);
userService.listen(3001);

const orderService = express();
orderService.use('/orders', orderRoutes);
orderService.listen(3002);
```

Deep Insight:
- Monoliths: Easier to develop, deploy, and debug initially
- Microservices: Better scalability, technology diversity, and fault isolation
- Monoliths: Can become complex and difficult to scale
- Microservices: Require more operational overhead and complexity
- Choose based on team size, complexity, and scalability requirements

## 3) What is the difference between functional and non-functional requirements?

Concept: Functional requirements define what the system does, while non-functional requirements define how well it performs in terms of quality attributes.

Example:
```javascript
// Functional requirement: User authentication
const authenticateUser = async (credentials) => {
  const user = await User.findOne({ email: credentials.email });
  const isValid = await bcrypt.compare(credentials.password, user.password);
  return isValid ? user : null;
};

// Non-functional requirement: Response time < 200ms
const rateLimiter = rateLimit({
  windowMs: 15 * 60 * 1000,
  max: 100,
  message: 'Too many requests'
});
```

Deep Insight:
- Functional: Features, user stories, business logic
- Non-functional: Performance, security, scalability, availability
- Both are equally important for system success
- Non-functional requirements often drive architectural decisions
- Should be measurable and testable

## 4) What is horizontal scaling vs vertical scaling?

Concept: Horizontal scaling adds more machines to handle increased load, while vertical scaling adds more power (CPU, RAM) to existing machines.

Example:
```javascript
// Horizontal scaling: Load balancer distributing requests
const loadBalancer = (servers) => {
  let currentServer = 0;
  return (req, res) => {
    const server = servers[currentServer % servers.length];
    currentServer++;
    proxy.web(req, res, { target: server });
  };
};

// Vertical scaling: Single powerful server
const server = express();
server.listen(3000, () => {
  console.log('Server running on powerful machine');
});
```

Deep Insight:
- Horizontal: Better for high availability and fault tolerance
- Vertical: Simpler to implement but has hardware limits
- Horizontal: Requires load balancing and data consistency
- Vertical: Can be more cost-effective for smaller systems
- Most systems use a combination of both approaches

## 5) What is load balancing, and what are common algorithms (Round Robin, Least Connections)?

Concept: Load balancing distributes incoming requests across multiple servers using various algorithms to improve performance and availability.

Example:
```javascript
// Round Robin Load Balancer
class RoundRobinBalancer {
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

// Least Connections Load Balancer
class LeastConnectionsBalancer {
  constructor(servers) {
    this.servers = servers.map(server => ({ ...server, connections: 0 }));
  }
  
  getNextServer() {
    return this.servers.reduce((min, server) => 
      server.connections < min.connections ? server : min
    );
  }
}
```

Deep Insight:
- Round Robin: Simple, fair distribution but doesn't consider server load
- Least Connections: Considers current load but requires connection tracking
- Weighted algorithms: Account for server capacity differences
- Health checks: Essential for removing failed servers
- Session affinity: May be needed for stateful applications

## 6) What is caching, and where can it be applied (client, CDN, app, database)?

Concept: Caching stores frequently accessed data in faster storage to improve performance and reduce latency at multiple system layers.

Example:
```javascript
// Application-level caching
const cache = new Map();
const getCachedData = async (key) => {
  if (cache.has(key)) {
    return cache.get(key);
  }
  const data = await fetchFromDatabase(key);
  cache.set(key, data);
  return data;
};

// Redis distributed cache
const redis = require('redis');
const client = redis.createClient();

const getCachedUser = async (userId) => {
  const cached = await client.get(`user:${userId}`);
  if (cached) return JSON.parse(cached);
  
  const user = await User.findById(userId);
  await client.setex(`user:${userId}`, 3600, JSON.stringify(user));
  return user;
};
```

Deep Insight:
- Client caching: Reduces server load and improves user experience
- CDN caching: Reduces latency for static content globally
- Application caching: Reduces database load and improves response times
- Database caching: Improves query performance
- Cache invalidation: Critical for maintaining data consistency

## 7) What is sharding, and what are its trade-offs?

Concept: Sharding splits data across multiple databases to improve performance and scalability, but requires careful key selection and data distribution.

Example:
```javascript
// Sharding by user ID
const getShard = (userId) => {
  const shardCount = 4;
  const shardId = userId % shardCount;
  return `shard_${shardId}`;
};

const getUser = async (userId) => {
  const shard = getShard(userId);
  const db = await connectToShard(shard);
  return await db.users.findOne({ id: userId });
};

// Range-based sharding
const getShardByRange = (userId) => {
  if (userId < 1000) return 'shard_0';
  if (userId < 5000) return 'shard_1';
  return 'shard_2';
};
```

Deep Insight:
- Improves read/write performance by distributing load
- Enables horizontal scaling of databases
- Requires careful shard key selection to avoid hotspots
- Makes cross-shard queries complex and expensive
- Data rebalancing can be challenging as system grows

## 8) What is replication, and how does it ensure high availability?

Concept: Replication creates copies of data across multiple servers to ensure availability and fault tolerance, with different consistency models.

Example:
```javascript
// Master-slave replication
const masterDB = await connectToMaster();
const slaveDBs = await connectToSlaves();

const writeData = async (data) => {
  await masterDB.insert(data);
  // Asynchronously replicate to slaves
  replicateToSlaves(data);
};

const readData = async (query) => {
  // Read from slave for better performance
  const slave = getRandomSlave();
  return await slave.query(query);
};
```

Deep Insight:
- Provides fault tolerance and high availability
- Enables read scaling by distributing read load
- Different consistency models: strong, eventual, causal
- Replication lag can cause consistency issues
- Requires conflict resolution strategies for writes

## 9) Explain the CAP theorem and real-world trade-offs.

Concept: The CAP theorem states that a distributed system can only guarantee two of: Consistency, Availability, and Partition tolerance.

Example:
```javascript
// CP system: Consistency + Partition tolerance
const cpSystem = {
  write: async (key, value) => {
    // Wait for all replicas to confirm
    await Promise.all(replicas.map(replica => 
      replica.write(key, value)
    ));
  },
  read: async (key) => {
    // Read from majority to ensure consistency
    const results = await Promise.all(replicas.map(r => r.read(key)));
    return getConsensus(results);
  }
};

// AP system: Availability + Partition tolerance
const apSystem = {
  write: async (key, value) => {
    // Write to available nodes, resolve conflicts later
    await Promise.allSettled(replicas.map(replica => 
      replica.write(key, value)
    ));
  },
  read: async (key) => {
    // Read from any available node
    const availableReplicas = replicas.filter(r => r.isAvailable());
    const result = await availableReplicas[0].read(key);
    return result;
  }
};
```

Deep Insight:
- Consistency: All nodes see the same data at the same time
- Availability: System remains operational despite failures
- Partition tolerance: System continues despite network failures
- Most real systems choose AP with eventual consistency
- Trade-offs depend on specific use case requirements

## 10) What is latency vs throughput, and why do both matter?

Concept: Latency is the time for a single request, while throughput is the number of requests processed per unit time, both critical for system performance.

Example:
```javascript
// Measuring latency
const measureLatency = async (operation) => {
  const start = performance.now();
  await operation();
  const end = performance.now();
  return end - start;
};

// Optimizing throughput
const processBatch = async (requests) => {
  const batchSize = 100;
  const batches = chunk(requests, batchSize);
  
  const results = await Promise.all(
    batches.map(batch => processBatch(batch))
  );
  
  return results.flat();
};
```

Deep Insight:
- Latency: Critical for user experience and real-time systems
- Throughput: Important for handling high-volume workloads
- Often trade-offs between low latency and high throughput
- Caching and optimization strategies affect both metrics
- Monitoring both helps identify performance bottlenecks