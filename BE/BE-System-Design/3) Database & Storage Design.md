# 3) Database & Storage Design (Q21–30)

## 21) What's the difference between SQL and NoSQL databases?

Concept: SQL databases are relational with ACID properties, while NoSQL databases are non-relational and more flexible, each suited for different use cases.

Example:
```javascript
// SQL database (PostgreSQL)
const createUser = async (userData) => {
  const query = `
    INSERT INTO users (name, email, created_at) 
    VALUES ($1, $2, $3) 
    RETURNING *
  `;
  return await db.query(query, [userData.name, userData.email, new Date()]);
};

// NoSQL database (MongoDB)
const createUser = async (userData) => {
  return await db.collection('users').insertOne({
    name: userData.name,
    email: userData.email,
    createdAt: new Date()
  });
};
```

Deep Insight:
- SQL: ACID compliance, complex queries, structured data
- NoSQL: Flexible schema, horizontal scaling, document/key-value storage
- SQL: Better for complex relationships and transactions
- NoSQL: Better for rapid development and large-scale data
- Choose based on data structure and query patterns

## 22) What are indexes, and how do they improve performance?

Concept: Indexes are data structures that speed up data retrieval by creating pointers to data locations, similar to a book's index.

Example:
```javascript
// Creating indexes
const createIndexes = async () => {
  // Single field index
  await db.collection('users').createIndex({ email: 1 });
  
  // Compound index
  await db.collection('orders').createIndex({ userId: 1, createdAt: -1 });
  
  // Text index for search
  await db.collection('products').createIndex({ name: 'text', description: 'text' });
};

// Query with index
const findUserByEmail = async (email) => {
  return await db.collection('users').findOne({ email });
  // Uses email index for fast lookup
};
```

Deep Insight:
- Dramatically improve query performance for large datasets
- Trade-off between read speed and write performance
- Compound indexes support multi-field queries
- Consider index selectivity and query patterns
- Monitor index usage and remove unused indexes

## 23) What is sharding, and how do you pick a shard key?

Concept: Sharding splits data across multiple databases, with shard keys determining data distribution and affecting query performance.

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
- Enables horizontal scaling of databases
- Shard key should distribute data evenly
- Avoid hotspots by choosing high-cardinality keys
- Consider query patterns when selecting shard key
- Cross-shard queries are expensive and should be avoided

## 24) What's the role of read replicas?

Concept: Read replicas are copies of the primary database used for read operations to improve performance and distribute load.

Example:
```javascript
// Read replica setup
const masterDB = await connectToMaster();
const readReplicas = await connectToReadReplicas();

const writeData = async (data) => {
  // Write to master
  await masterDB.insert(data);
  // Replication happens automatically
};

const readData = async (query) => {
  // Read from replica for better performance
  const replica = getRandomReplica();
  return await replica.query(query);
};

const getRandomReplica = () => {
  const index = Math.floor(Math.random() * readReplicas.length);
  return readReplicas[index];
};
```

Deep Insight:
- Improves read performance by distributing load
- Provides fault tolerance and high availability
- Can have slight replication lag
- Different consistency models available
- Essential for read-heavy applications

## 25) How does replication lag impact consistency?

Concept: Replication lag creates temporary inconsistency between primary and replica databases, affecting data freshness and consistency.

Example:
```javascript
// Handling replication lag
const writeAndRead = async (data) => {
  // Write to master
  await masterDB.insert(data);
  
  // Read from replica immediately (might be stale)
  const staleData = await readReplica.query(data.id);
  
  // Wait for replication or read from master
  await waitForReplication(data.id);
  const freshData = await readReplica.query(data.id);
};

const waitForReplication = async (id) => {
  const maxWait = 5000; // 5 seconds
  const start = Date.now();
  
  while (Date.now() - start < maxWait) {
    const data = await readReplica.query(id);
    if (data) return;
    await new Promise(resolve => setTimeout(resolve, 100));
  }
};
```

Deep Insight:
- Can cause stale reads and consistency issues
- Depends on network latency and database load
- Can be mitigated with read-after-write consistency
- Consider eventual consistency for non-critical data
- Monitor replication lag and set appropriate timeouts

## 26) What is the write-ahead log (WAL)?

Concept: WAL is a logging technique that ensures data durability by writing changes to a log before applying them to the database.

Example:
```javascript
// WAL implementation concept
class WriteAheadLog {
  constructor() {
    this.log = [];
    this.data = new Map();
  }
  
  async write(key, value) {
    const logEntry = {
      operation: 'write',
      key,
      value,
      timestamp: Date.now()
    };
    
    // Write to log first
    await this.appendToLog(logEntry);
    
    // Then apply to data
    this.data.set(key, value);
  }
  
  async appendToLog(entry) {
    // Ensure log is written to disk
    await fs.appendFile('wal.log', JSON.stringify(entry) + '\n');
  }
}
```

Deep Insight:
- Ensures data durability even during crashes
- Enables crash recovery and point-in-time recovery
- Can be used for replication and backup
- Adds overhead but provides reliability
- Essential for ACID compliance

## 27) What is data denormalization, and when is it beneficial?

Concept: Denormalization adds redundant data to improve read performance at the cost of storage and consistency complexity.

Example:
```javascript
// Normalized data
const normalizedUser = {
  id: 1,
  name: 'John Doe',
  email: 'john@example.com'
};

const normalizedOrder = {
  id: 1,
  userId: 1,
  productId: 1,
  amount: 100
};

// Denormalized data for better read performance
const denormalizedOrder = {
  id: 1,
  userId: 1,
  userName: 'John Doe',
  userEmail: 'john@example.com',
  productId: 1,
  productName: 'Laptop',
  amount: 100
};
```

Deep Insight:
- Improves read performance by reducing joins
- Increases storage requirements and complexity
- Can lead to data inconsistency
- Beneficial for read-heavy workloads
- Requires careful update strategies

## 28) How do you handle transactions across multiple microservices (2PC, Saga)?

Concept: Distributed transactions use patterns like 2PC or Saga to maintain consistency across services, each with different trade-offs.

Example:
```javascript
// Saga pattern implementation
class OrderSaga {
  async processOrder(orderData) {
    const steps = [
      () => this.reserveInventory(orderData.productId),
      () => this.processPayment(orderData.paymentInfo),
      () => this.createOrder(orderData),
      () => this.sendConfirmation(orderData.userId)
    ];
    
    const compensations = [
      () => this.releaseInventory(orderData.productId),
      () => this.refundPayment(orderData.paymentInfo),
      () => this.cancelOrder(orderData.id),
      () => this.cancelConfirmation(orderData.userId)
    ];
    
    try {
      for (let i = 0; i < steps.length; i++) {
        await steps[i]();
      }
    } catch (error) {
      // Compensate for completed steps
      for (let i = steps.length - 1; i >= 0; i--) {
        await compensations[i]();
      }
      throw error;
    }
  }
}
```

Deep Insight:
- 2PC: Strong consistency but can block on failures
- Saga: Better performance but eventual consistency
- Choose based on consistency requirements
- Consider compensation strategies
- Monitor and handle failures gracefully

## 29) What is a distributed cache and its use cases?

Concept: A distributed cache stores data across multiple nodes to improve performance and availability in distributed systems.

Example:
```javascript
// Redis distributed cache
const redis = require('redis');
const client = redis.createClient({
  host: 'redis-cluster.example.com',
  port: 6379
});

const cacheService = {
  async get(key) {
    return await client.get(key);
  },
  
  async set(key, value, ttl = 3600) {
    return await client.setex(key, ttl, JSON.stringify(value));
  },
  
  async del(key) {
    return await client.del(key);
  },
  
  async invalidatePattern(pattern) {
    const keys = await client.keys(pattern);
    if (keys.length > 0) {
      await client.del(...keys);
    }
  }
};
```

Deep Insight:
- Improves performance by reducing database load
- Provides high availability through replication
- Can be used for session storage and data caching
- Requires careful cache invalidation strategies
- Consider memory usage and eviction policies

## 30) How do you ensure data consistency in distributed databases?

Concept: Data consistency in distributed databases is ensured through techniques like consensus algorithms, replication, and conflict resolution.

Example:
```javascript
// Vector clocks for conflict resolution
class VectorClock {
  constructor(nodeId) {
    this.nodeId = nodeId;
    this.clock = new Map();
  }
  
  increment() {
    const current = this.clock.get(this.nodeId) || 0;
    this.clock.set(this.nodeId, current + 1);
  }
  
  update(otherClock) {
    for (const [node, time] of otherClock.clock) {
      const current = this.clock.get(node) || 0;
      this.clock.set(node, Math.max(current, time));
    }
  }
  
  compare(otherClock) {
    // Returns: 'before', 'after', 'concurrent', or 'equal'
    let thisGreater = false;
    let otherGreater = false;
    
    for (const [node, time] of this.clock) {
      const otherTime = otherClock.clock.get(node) || 0;
      if (time > otherTime) thisGreater = true;
      if (time < otherTime) otherGreater = true;
    }
    
    if (thisGreater && !otherGreater) return 'after';
    if (!thisGreater && otherGreater) return 'before';
    if (thisGreater && otherGreater) return 'concurrent';
    return 'equal';
  }
}
```

Deep Insight:
- Use consensus algorithms like Raft or PBFT
- Implement conflict resolution strategies
- Consider different consistency models
- Monitor and handle network partitions
- Balance consistency with availability and performance