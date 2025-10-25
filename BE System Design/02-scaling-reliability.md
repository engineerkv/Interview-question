# ⚙️ Backend System Design Interview Notes (2025 Edition)

## 🟤 Section 2 — Database Deep Dive (MongoDB + SQL) — Q26-Q60

---

### 26. 🟤 How does a database execute a query internally?

**🧠 Concept**

Database query execution involves parsing, optimization, and execution phases with query planner choosing optimal execution strategy.

**💻 Example**

```sql
-- Query execution phases
SELECT u.name, o.total 
FROM users u 
JOIN orders o ON u.id = o.user_id 
WHERE u.status = 'active';

-- 1. Parse: Convert SQL to parse tree
-- 2. Optimize: Choose join order, indexes
-- 3. Execute: Run optimized plan
```

**💬 Explanation + Insight**

- **Parse Phase** - Convert SQL to internal representation
- **Optimization** - Query planner chooses best execution strategy
- **Execution** - Database engine runs optimized plan
- **Index Usage** - Planner decides which indexes to use
- **Cost Estimation** - Choose plan with lowest estimated cost

---

### 27. 🟤 What is a query execution plan (EXPLAIN)?

**🧠 Concept**

Query execution plan shows how database will execute a query, including operations, indexes used, and estimated costs.

**💻 Example**

```sql
-- PostgreSQL EXPLAIN
EXPLAIN (ANALYZE, BUFFERS) 
SELECT * FROM users WHERE email = 'user@example.com';

-- Output shows:
-- Seq Scan on users (cost=0.00..1000.00 rows=1 width=64)
-- Filter: (email = 'user@example.com'::text)
-- Planning Time: 0.123 ms
-- Execution Time: 0.456 ms
```

**💬 Explanation + Insight**

- **Cost Estimation** - Shows estimated cost of operations
- **Index Usage** - Indicates which indexes are used
- **Join Strategy** - Shows how tables are joined
- **Performance Tuning** - Identify bottlenecks and optimizations
- **Query Optimization** - Use plans to improve query performance

---

### 28. 🟤 How does MongoDB's query planner choose indexes?

**🧠 Concept**

MongoDB query planner evaluates multiple execution plans, runs them in parallel, and chooses the most efficient one based on performance.

**💻 Example**

```javascript
// MongoDB query with multiple possible indexes
db.users.find({ 
  status: 'active', 
  age: { $gte: 18 },
  city: 'New York' 
});

// Query planner evaluates:
// 1. Index on { status: 1, age: 1, city: 1 }
// 2. Index on { status: 1, city: 1 }
// 3. Index on { age: 1, status: 1 }
// 4. Collection scan
```

**💬 Explanation + Insight**

- **Plan Evaluation** - Test multiple execution strategies
- **Parallel Execution** - Run plans simultaneously
- **Performance Metrics** - Choose fastest plan
- **Index Selection** - Prefer index scans over collection scans
- **Adaptive Planning** - Learn from execution statistics

---

### 29. 🟤 What are B-trees and how are they used in indexing?

**🧠 Concept**

B-trees are balanced tree data structures that maintain sorted data and enable efficient search, insertion, and deletion operations.

**💻 Example**

```javascript
// B-tree structure for database index
class BTreeNode {
  constructor() {
    this.keys = [];      // [10, 20, 30]
    this.children = [];  // [left, middle, right]
    this.isLeaf = false;
  }
}

// B-tree search operation
function search(node, key) {
  let i = 0;
  while (i < node.keys.length && key > node.keys[i]) {
    i++;
  }
  if (i < node.keys.length && key === node.keys[i]) {
    return node; // Found
  }
  if (node.isLeaf) {
    return null; // Not found
  }
  return search(node.children[i], key);
}
```

**💬 Explanation + Insight**

- **Balanced Structure** - All leaves at same level
- **Sorted Keys** - Maintains sorted order for range queries
- **Efficient Search** - O(log n) search time
- **Disk-Friendly** - Optimized for disk storage
- **Range Queries** - Efficient for range operations

---

### 30. 🟤 What's the difference between sequential scan and index scan?

**🧠 Concept**

Sequential scan reads entire table row by row, while index scan uses index to jump directly to relevant rows.

**💻 Example**

```sql
-- Sequential scan (slow)
SELECT * FROM users WHERE age > 25;
-- Database reads every row in users table

-- Index scan (fast)
CREATE INDEX idx_users_age ON users(age);
SELECT * FROM users WHERE age > 25;
-- Database uses index to find relevant rows directly
```

**💬 Explanation + Insight**

- **Sequential Scan** - Reads entire table, O(n) time
- **Index Scan** - Uses index to find rows, O(log n) time
- **Performance** - Index scan much faster for selective queries
- **Memory Usage** - Index scan uses less memory
- **Use Cases** - Index scan for selective queries, sequential for full table

---

### 31. 🟤 When should you normalize vs denormalize data?

**🧠 Concept**

Normalization reduces redundancy but increases joins, while denormalization reduces joins but increases storage and update complexity.

**💻 Example**

```sql
-- Normalized (3NF)
CREATE TABLE users (
  id INT PRIMARY KEY,
  name VARCHAR(100),
  email VARCHAR(100)
);

CREATE TABLE orders (
  id INT PRIMARY KEY,
  user_id INT,
  total DECIMAL(10,2),
  FOREIGN KEY (user_id) REFERENCES users(id)
);

-- Denormalized
CREATE TABLE orders_denormalized (
  id INT PRIMARY KEY,
  user_name VARCHAR(100),
  user_email VARCHAR(100),
  total DECIMAL(10,2)
);
```

**💬 Explanation + Insight**

- **Normalization** - Reduces redundancy, more joins
- **Denormalization** - Reduces joins, more storage
- **Read Performance** - Denormalized faster for reads
- **Write Performance** - Normalized faster for writes
- **Use Cases** - Normalize for OLTP, denormalize for OLAP

---

### 32. 🟤 Embedded vs referenced documents in MongoDB — when to use each?

**🧠 Concept**

Embedded documents store related data in same document, while referenced documents store references to other documents.

**💻 Example**

```javascript
// Embedded documents (1:1, 1:few)
const user = {
  _id: ObjectId(),
  name: 'John Doe',
  email: 'john@example.com',
  address: {           // Embedded
    street: '123 Main St',
    city: 'New York',
    zip: '10001'
  }
};

// Referenced documents (1:many, many:many)
const user = {
  _id: ObjectId(),
  name: 'John Doe',
  orders: [ObjectId(), ObjectId()] // References to orders
};
```

**💬 Explanation + Insight**

- **Embedded** - Good for 1:1, 1:few relationships
- **Referenced** - Good for 1:many, many:many relationships
- **Query Performance** - Embedded faster for single queries
- **Update Complexity** - Referenced easier to update
- **Use Cases** - Embed for small, stable data; reference for large, changing data

---

### 33. 🟤 How to model one-to-many and many-to-many relationships in MongoDB?

**🧠 Concept**

One-to-many uses array of references, while many-to-many uses separate collection with references to both entities.

**💻 Example**

```javascript
// One-to-many: User has many orders
const user = {
  _id: ObjectId(),
  name: 'John Doe',
  orders: [ObjectId(), ObjectId(), ObjectId()]
};

// Many-to-many: Users and products
const userProduct = {
  _id: ObjectId(),
  userId: ObjectId(),
  productId: ObjectId(),
  quantity: 2,
  createdAt: new Date()
};
```

**💬 Explanation + Insight**

- **One-to-Many** - Store array of references in parent document
- **Many-to-Many** - Use separate junction collection
- **Query Patterns** - Design based on how data is accessed
- **Performance** - Consider query performance vs storage
- **Use Cases** - One-to-many for user orders, many-to-many for user products

---

### 34. 🟤 How does $lookup differ from SQL joins?

**🧠 Concept**

MongoDB's $lookup performs left outer join between collections, while SQL joins can be inner, left, right, or full outer joins.

**💻 Example**

```javascript
// MongoDB $lookup (left outer join)
db.orders.aggregate([
  {
    $lookup: {
      from: 'users',
      localField: 'userId',
      foreignField: '_id',
      as: 'user'
    }
  }
]);

// SQL equivalent
SELECT o.*, u.name, u.email 
FROM orders o 
LEFT JOIN users u ON o.userId = u.id;
```

**💬 Explanation + Insight**

- **$lookup** - Only left outer join in MongoDB
- **SQL Joins** - Multiple join types available
- **Performance** - $lookup can be slower than SQL joins
- **Use Cases** - $lookup for document relationships
- **Alternatives** - Consider embedding for better performance

---

### 35. 🟤 What are compound indexes and when should you use them?

**🧠 Concept**

Compound indexes use multiple fields and are most effective when query patterns match the index field order.

**💻 Example**

```javascript
// Compound index
db.users.createIndex({ status: 1, age: 1, city: 1 });

// Effective queries (use prefix)
db.users.find({ status: 'active' });
db.users.find({ status: 'active', age: { $gte: 18 } });
db.users.find({ status: 'active', age: 18, city: 'NYC' });

// Ineffective query (skips status)
db.users.find({ age: 18, city: 'NYC' }); // Won't use index
```

**💬 Explanation + Insight**

- **Field Order** - Most selective field first
- **Prefix Rule** - Index works for queries using field prefixes
- **Query Patterns** - Design based on common query patterns
- **Performance** - Compound indexes faster than multiple single indexes
- **Use Cases** - Use for multi-field queries

---

### 36. 🟤 How do indexes affect write performance?

**🧠 Concept**

Indexes improve read performance but slow down write operations because each write must update all relevant indexes.

**💻 Example**

```javascript
// Without indexes - fast writes
db.users.insertOne({
  name: 'John',
  email: 'john@example.com',
  age: 30
}); // Fast insert

// With indexes - slower writes
db.users.createIndex({ email: 1 });
db.users.createIndex({ age: 1 });
db.users.createIndex({ name: 1, email: 1 });

db.users.insertOne({
  name: 'John',
  email: 'john@example.com',
  age: 30
}); // Slower insert - must update 3 indexes
```

**💬 Explanation + Insight**

- **Write Overhead** - Each write updates all relevant indexes
- **Index Maintenance** - Database must maintain index consistency
- **Storage Cost** - Indexes consume additional storage space
- **Memory Usage** - Indexes consume memory for caching
- **Trade-offs** - Balance read performance vs write performance

---

### 37. 🟤 Clustered vs non-clustered indexes — key difference.

**🧠 Concept**

Clustered indexes determine physical storage order of data, while non-clustered indexes are separate structures pointing to data.

**💻 Example**

```sql
-- Clustered index (determines storage order)
CREATE CLUSTERED INDEX idx_users_id ON users(id);
-- Data is physically sorted by id

-- Non-clustered index (separate structure)
CREATE NONCLUSTERED INDEX idx_users_email ON users(email);
-- Index points to data rows
```

**💬 Explanation + Insight**

- **Clustered Index** - Only one per table, determines physical order
- **Non-clustered Index** - Multiple allowed, separate structure
- **Performance** - Clustered index faster for range queries
- **Storage** - Clustered index doesn't use extra storage
- **Use Cases** - Clustered for primary key, non-clustered for other fields

---

### 38. 🟤 What are partial, sparse, and TTL indexes?

**🧠 Concept**

Partial indexes include only documents matching filter, sparse indexes exclude null values, and TTL indexes automatically delete documents after expiration.

**💻 Example**

```javascript
// Partial index - only active users
db.users.createIndex(
  { email: 1 },
  { partialFilterExpression: { status: 'active' } }
);

// Sparse index - exclude null values
db.users.createIndex(
  { phone: 1 },
  { sparse: true }
);

// TTL index - auto-delete after 30 days
db.sessions.createIndex(
  { createdAt: 1 },
  { expireAfterSeconds: 2592000 } // 30 days
);
```

**💬 Explanation + Insight**

- **Partial Index** - Smaller, faster, only relevant documents
- **Sparse Index** - Excludes null values, saves space
- **TTL Index** - Automatic cleanup, good for temporary data
- **Storage** - Partial and sparse indexes use less storage
- **Use Cases** - Partial for filtered queries, TTL for temporary data

---

### 39. 🟤 How do you optimize pagination queries efficiently?

**🧠 Concept**

Use cursor-based pagination with indexed fields instead of OFFSET for better performance on large datasets.

**💻 Example**

```javascript
// Inefficient pagination (OFFSET)
db.users.find().skip(10000).limit(20); // Slow for large offsets

// Efficient pagination (cursor-based)
db.users.find({ _id: { $gt: lastId } }).limit(20);

// Or with indexed field
db.users.find({ createdAt: { $lt: lastCreatedAt } })
  .sort({ createdAt: -1 })
  .limit(20);
```

**💬 Explanation + Insight**

- **Cursor-based** - Use last seen value instead of offset
- **Indexed Fields** - Use indexed fields for cursor
- **Performance** - Constant time regardless of position
- **Consistency** - Handle new records during pagination
- **Use Cases** - Essential for large datasets

---

### 40. 🟤 What is index selectivity and why does it matter?

**🧠 Concept**

Index selectivity measures how unique values are in an indexed field, affecting query performance and index effectiveness.

**💻 Example**

```javascript
// High selectivity (unique values)
db.users.createIndex({ email: 1 }); // email is unique
// Query: db.users.find({ email: 'user@example.com' })
// Returns 1 document, very efficient

// Low selectivity (few unique values)
db.users.createIndex({ status: 1 }); // status has few values
// Query: db.users.find({ status: 'active' })
// Returns many documents, less efficient
```

**💬 Explanation + Insight**

- **High Selectivity** - Few duplicates, better performance
- **Low Selectivity** - Many duplicates, worse performance
- **Query Efficiency** - High selectivity reduces result set
- **Index Design** - Choose fields with high selectivity
- **Use Cases** - Prefer unique or near-unique fields

---

### 41. 🟤 How do you detect and remove unused indexes?

**🧠 Concept**

Monitor index usage statistics and remove indexes that are not being used to improve write performance and reduce storage.

**💻 Example**

```javascript
// Check index usage statistics
db.users.aggregate([
  { $indexStats: {} }
]);

// Output shows:
// {
//   "name": "email_1",
//   "accesses": { "ops": 1000, "since": ISODate("2023-01-01") }
// }

// Remove unused index
db.users.dropIndex({ email: 1 });
```

**💬 Explanation + Insight**

- **Usage Statistics** - Monitor which indexes are used
- **Performance Impact** - Unused indexes slow down writes
- **Storage Cost** - Unused indexes waste storage space
- **Regular Cleanup** - Periodically review and remove unused indexes
- **Use Cases** - Essential for maintaining optimal performance

---

### 42. 🟤 What is ACID and how does MongoDB support transactions (v4.0+)?

**🧠 Concept**

ACID ensures database transactions are Atomic, Consistent, Isolated, and Durable. MongoDB supports multi-document transactions since v4.0.

**💻 Example**

```javascript
// MongoDB transaction
const session = client.startSession();
try {
  await session.withTransaction(async () => {
    await users.insertOne({ name: 'John' }, { session });
    await orders.insertOne({ userId: 'john_id', total: 100 }, { session });
  });
} finally {
  await session.endSession();
}
```

**💬 Explanation + Insight**

- **Atomicity** - All operations succeed or fail together
- **Consistency** - Database remains in valid state
- **Isolation** - Concurrent transactions don't interfere
- **Durability** - Committed changes persist
- **Use Cases** - Critical for financial and inventory systems

---

### 43. 🟤 What are isolation levels in SQL and why do they matter?

**🧠 Concept**

Isolation levels control how transactions interact with each other, balancing consistency and performance.

**💻 Example**

```sql
-- Read Committed (default)
SET TRANSACTION ISOLATION LEVEL READ COMMITTED;
BEGIN;
SELECT * FROM users WHERE id = 1;
-- Can see committed changes from other transactions
COMMIT;

-- Serializable (highest isolation)
SET TRANSACTION ISOLATION LEVEL SERIALIZABLE;
BEGIN;
SELECT * FROM users WHERE id = 1;
-- No other transactions can modify data
COMMIT;
```

**💬 Explanation + Insight**

- **Read Uncommitted** - Lowest isolation, can see uncommitted data
- **Read Committed** - Default level, sees committed data
- **Repeatable Read** - Consistent reads within transaction
- **Serializable** - Highest isolation, prevents all anomalies
- **Performance** - Higher isolation = lower performance

---

### 44. 🟤 Optimistic vs pessimistic locking — when to use each.

**🧠 Concept**

Optimistic locking assumes conflicts are rare and checks at commit, while pessimistic locking locks resources during transaction.

**💻 Example**

```javascript
// Optimistic locking
const user = await User.findById(id);
user.balance -= amount;
if (user.version !== expectedVersion) {
  throw new Error('Concurrent modification');
}
user.version++;
await user.save();

// Pessimistic locking
const user = await User.findById(id).selectForUpdate();
user.balance -= amount;
await user.save();
```

**💬 Explanation + Insight**

- **Optimistic** - Better for low-conflict scenarios
- **Pessimistic** - Better for high-conflict scenarios
- **Performance** - Optimistic generally faster
- **Deadlocks** - Pessimistic can cause deadlocks
- **Use Cases** - Optimistic for reads, pessimistic for writes

---

### 45. 🟤 How does MongoDB achieve document-level concurrency?

**🧠 Concept**

MongoDB uses document-level locking, allowing concurrent operations on different documents while serializing operations on the same document.

**💻 Example**

```javascript
// Concurrent operations on different documents
// Thread 1
db.users.updateOne({ _id: 1 }, { $set: { name: 'John' } });

// Thread 2 (can run concurrently)
db.users.updateOne({ _id: 2 }, { $set: { name: 'Jane' } });

// Operations on same document are serialized
// Thread 1
db.users.updateOne({ _id: 1 }, { $set: { name: 'John' } });

// Thread 2 (waits for Thread 1 to complete)
db.users.updateOne({ _id: 1 }, { $set: { age: 30 } });
```

**💬 Explanation + Insight**

- **Document-level Locking** - Lock individual documents, not entire collection
- **Concurrency** - Multiple operations on different documents
- **Serialization** - Operations on same document are serialized
- **Performance** - Better than table-level locking
- **Use Cases** - Enables high concurrency for document databases

---

### 46. 🟤 What is replication and how do replica sets work?

**🧠 Concept**

Replication creates multiple copies of data across different servers for high availability, fault tolerance, and read scaling.

**💻 Example**

```javascript
// MongoDB replica set configuration
{
  "_id": "rs0",
  "members": [
    { "_id": 0, "host": "mongodb1:27017", "priority": 1 },
    { "_id": 1, "host": "mongodb2:27017", "priority": 1 },
    { "_id": 2, "host": "mongodb3:27017", "priority": 1, "arbiterOnly": true }
  ]
}

// Read from secondary
db.users.find().readPref("secondary");
```

**💬 Explanation + Insight**

- **Primary-Secondary** - One primary, multiple secondaries
- **Automatic Failover** - Secondary becomes primary if primary fails
- **Read Scaling** - Distribute reads across secondaries
- **Data Consistency** - Eventually consistent across replicas
- **Use Cases** - High availability and read scaling

---

### 47. 🟤 What is a shard key and why is it critical?

**🧠 Concept**

Shard key determines how data is distributed across shards and affects query performance and data distribution.

**💻 Example**

```javascript
// Good shard key - high cardinality, even distribution
sh.shardCollection("mydb.users", { userId: 1 });

// Bad shard key - low cardinality
sh.shardCollection("mydb.users", { status: 1 }); // Only few values

// Compound shard key
sh.shardCollection("mydb.orders", { userId: 1, orderDate: 1 });
```

**💬 Explanation + Insight**

- **Data Distribution** - Determines which shard stores data
- **Query Performance** - Affects query routing and performance
- **Cardinality** - High cardinality for even distribution
- **Monotonic** - Avoid monotonically increasing keys
- **Use Cases** - Critical for horizontal scaling

---

### 48. 🟤 How does MongoDB balance data across shards?

**🧠 Concept**

MongoDB uses chunk-based sharding where data is divided into chunks and distributed across shards, with automatic rebalancing.

**💻 Example**

```javascript
// Chunk distribution
// Shard 1: chunks [minKey, 1000), [1000, 2000)
// Shard 2: chunks [2000, 3000), [3000, 4000)
// Shard 3: chunks [4000, 5000), [5000, maxKey)

// Automatic rebalancing
// If Shard 1 has too many chunks, MongoDB moves chunks to other shards
```

**💬 Explanation + Insight**

- **Chunk-based** - Data divided into chunks by shard key range
- **Automatic Rebalancing** - MongoDB moves chunks between shards
- **Load Balancing** - Distributes data evenly across shards
- **Chunk Splitting** - Chunks split when they become too large
- **Use Cases** - Essential for horizontal scaling

---

### 49. 🟤 What's the difference between sharding and partitioning?

**🧠 Concept**

Sharding distributes data across multiple servers, while partitioning divides data within a single server for performance.

**💻 Example**

```sql
-- Partitioning (single server)
CREATE TABLE orders (
  id INT,
  order_date DATE,
  amount DECIMAL
) PARTITION BY RANGE (order_date) (
  PARTITION p2023 VALUES LESS THAN ('2024-01-01'),
  PARTITION p2024 VALUES LESS THAN ('2025-01-01')
);

-- Sharding (multiple servers)
-- Shard 1: orders with userId 1-1000
-- Shard 2: orders with userId 1001-2000
-- Shard 3: orders with userId 2001-3000
```

**💬 Explanation + Insight**

- **Sharding** - Multiple servers, horizontal scaling
- **Partitioning** - Single server, vertical organization
- **Scalability** - Sharding provides better scalability
- **Complexity** - Sharding more complex to manage
- **Use Cases** - Sharding for scale, partitioning for performance

---

### 50. 🟤 How to choose an efficient shard key for scalability?

**🧠 Concept**

Choose shard key with high cardinality, even distribution, and good query patterns to avoid hotspots and enable efficient queries.

**💻 Example**

```javascript
// Good shard key
{ userId: 1 } // High cardinality, even distribution

// Bad shard key - creates hotspots
{ createdAt: 1 } // Monotonic, all new data goes to one shard

// Compound shard key
{ userId: 1, orderDate: 1 } // Good for user-specific queries
```

**💬 Explanation + Insight**

- **High Cardinality** - Many unique values for even distribution
- **Even Distribution** - Avoid hotspots and uneven load
- **Query Patterns** - Match common query patterns
- **Avoid Monotonic** - Don't use timestamp or auto-increment
- **Use Cases** - Critical for horizontal scaling

---

*This comprehensive database deep dive section covers essential concepts including query execution, indexing strategies, data modeling, transactions, replication, and sharding for building scalable database systems.*