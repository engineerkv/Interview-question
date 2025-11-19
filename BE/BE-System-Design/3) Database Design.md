# Section 3: Database Design (Q46-Q80)

---

## Q46. SQL vs NoSQL – when to choose which?

Choose SQL when you need structured data with relationships, ACID transactions, and complex queries with joins - like banking systems or e-commerce where data integrity is critical. Choose NoSQL when you need flexible schemas, horizontal scaling, and high write throughput - like social media feeds, IoT data, or content management where data structure changes frequently.

- **Trade-offs**: SQL gives you strong consistency and powerful querying but is harder to scale horizontally and requires schema migrations. NoSQL scales easily and handles unstructured data well, but the catch is you lose joins, complex transactions, and have to manage consistency yourself - hybrid approaches are common where you use SQL for transactional data and NoSQL for analytics or caching.

---

## Q47. ACID properties with examples.

ACID stands for Atomicity (all operations succeed or all fail), Consistency (data stays valid), Isolation (concurrent transactions don't interfere), and Durability (committed data survives crashes). Like when you transfer money - both accounts update together or neither does, balances stay correct, other transactions see consistent state, and once committed, the transfer survives a server crash.

- **Trade-offs**: ACID guarantees make data reliable and predictable, which is essential for financial systems, but the catch is they require coordination which slows down writes and limits scalability. The tricky part is you often relax ACID for performance - like using eventual consistency for non-critical data, or accepting weaker isolation levels for better throughput.

Example:

```sql
BEGIN TRANSACTION;
  UPDATE accounts SET balance = balance - 100 WHERE id = 1;
  UPDATE accounts SET balance = balance + 100 WHERE id = 2;
COMMIT;
-- If either update fails, both roll back (Atomicity)
-- Balances always sum correctly (Consistency)
-- Other transactions see consistent state (Isolation)
-- Changes persist even if server crashes (Durability)
```

---

## Q48. How do SQL transactions work?

SQL transactions group multiple operations into a single unit that either all succeed or all fail - you start with BEGIN, execute your queries, then COMMIT to save changes or ROLLBACK to undo everything. The database locks affected rows to prevent other transactions from seeing partial changes, ensuring data stays consistent.

- **Trade-offs**: Transactions guarantee data integrity which is critical for operations like payments or inventory updates, but the catch is locks can cause contention - if one transaction holds a lock, others have to wait, which can slow things down or cause deadlocks. The tricky part is choosing the right isolation level - stricter isolation prevents issues but reduces concurrency, while weaker isolation improves performance but can cause weird bugs.

Example:

```sql
BEGIN TRANSACTION;
  INSERT INTO orders (user_id, total) VALUES (123, 99.99);
  UPDATE inventory SET quantity = quantity - 1 WHERE product_id = 456;
  -- If inventory update fails, order insert also rolls back
COMMIT;
```

---

## Q49. Deadlock avoidance strategies.

Avoid deadlocks by always acquiring locks in the same order across transactions, using timeouts so transactions don't wait forever, keeping transactions short to reduce lock time, and using lower isolation levels when possible. Deadlocks happen when two transactions each hold a lock the other needs - like transaction A locks row 1 and waits for row 2, while transaction B locks row 2 and waits for row 1.

- **Trade-offs**: Lock ordering prevents deadlocks but requires discipline and can be hard to enforce across a large codebase. Timeouts prevent infinite waits but can cause legitimate transactions to fail, and shorter transactions reduce deadlock risk but might require breaking up logical operations - the tricky part is deadlocks are rare but hard to debug when they happen, so you need good monitoring to catch them.

---

## Q50. What is a connection pool?

A connection pool maintains a set of reusable database connections instead of creating a new one for each query - like keeping 10 connections open and reusing them, only creating new ones when all are busy. This avoids the overhead of establishing connections which involves network handshakes and authentication.

- **Trade-offs**: Connection pooling dramatically improves performance by reusing expensive connections, but the catch is you need to size the pool correctly - too small and requests wait for available connections, too large and you waste resources or hit database connection limits. The tricky part is handling connection failures - dead connections need to be detected and replaced, and you need to handle connection timeouts gracefully.

Example:

```javascript
// Connection pool with 10 connections
const pool = mysql.createPool({
  connectionLimit: 10,
  host: 'localhost',
  user: 'root',
  password: 'password',
  database: 'mydb'
});

// Reuses connections from pool
pool.query('SELECT * FROM users', (err, results) => {
  // Connection automatically returned to pool
});
```

---

## Q51. Using read replicas for scaling read-heavy workloads.

Read replicas are copies of your database that handle read queries while the primary handles writes - you send SELECT queries to replicas and INSERT/UPDATE/DELETE to the primary, which distributes load and allows you to scale reads horizontally. The primary replicates changes to replicas asynchronously, so there's a small delay before reads see the latest data.

- **Trade-offs**: Read replicas allow you to scale reads almost infinitely by adding more replicas, and they provide redundancy if the primary fails, but the catch is you get eventual consistency - reads might see slightly stale data. The tricky part is routing queries correctly - you need application logic or a proxy to send reads to replicas and writes to primary, and you need to handle replica lag when you need fresh data.

---

## Q52. SQL sharding patterns.

SQL sharding splits your database across multiple servers by a shard key - like sharding users by user_id so users 1-1000 go to server A, 1001-2000 to server B. Common patterns include range-based (split by ID ranges), hash-based (hash the key to determine shard), or directory-based (lookup table maps keys to shards).

- **Trade-offs**: Sharding allows you to scale beyond one machine's limits and can speed up queries by reducing data per server, but the catch is cross-shard queries become complex and slow - you might need to query multiple shards and combine results. The tricky part is choosing a good shard key - if you pick wrong, you get hot shards with all the traffic while others sit idle, and rebalancing shards when you add servers is painful.

Example:

```sql
-- Hash-based sharding: hash(user_id) % 4 determines shard
-- User 123 -> hash(123) % 4 = 2 -> shard_2
-- User 456 -> hash(456) % 4 = 0 -> shard_0

-- Range-based sharding
-- Shard 1: user_id 1-1000000
-- Shard 2: user_id 1000001-2000000
```

---

## Q53. Indexing strategy for large databases.

Index strategically by creating indexes on columns used in WHERE clauses, JOIN conditions, and ORDER BY - but only where queries actually benefit, since indexes slow down writes and use storage. For large databases, use composite indexes that match common query patterns, monitor index usage to remove unused ones, and consider partial indexes for filtered queries.

- **Trade-offs**: Good indexes make queries fast - turning full table scans into index seeks - but the catch is each index slows down INSERT/UPDATE/DELETE because the database must update the index. The tricky part is balancing read performance with write performance - too many indexes and writes become slow, too few and reads become slow. For large tables, index maintenance can become a bottleneck.

Example:

```sql
-- Composite index matching common query pattern
CREATE INDEX idx_user_status_created ON orders(user_id, status, created_at);

-- ---

## Query can use this index efficiently
SELECT * FROM orders 
WHERE user_id = 123 AND status = 'pending' 
ORDER BY created_at DESC;
```

---

## Q54. What is a covering index?

A covering index contains all the columns needed for a query, so the database never needs to read the actual table - it gets everything from the index. Like if you query user_id and email, and you have an index on (user_id, email), the database can return results directly from the index without touching the table.

- **Trade-offs**: Covering indexes make queries super fast because they avoid table lookups entirely, but the catch is they're larger and slower to maintain since they contain more columns. The tricky part is they only help specific queries - if your query needs different columns, the covering index doesn't help, so you need to balance index size with query patterns.

Example:

```sql
-- Covering index includes all columns needed by query
CREATE INDEX idx_covering ON users(user_id, email, name);

-- ---

## Query uses only index, never touches table
SELECT user_id, email, name FROM users WHERE user_id = 123;
-- explain shows: "Using index" (covering query)
```

---

## Q55. ---

## Query optimization best practices.

Optimize queries by using indexes on filtered columns, avoiding SELECT * to reduce data transfer, using LIMIT to restrict result sets, writing efficient JOINs with proper indexes, and analyzing query plans with EXPLAIN. Avoid N+1 queries by using JOINs or batch loading, and use prepared statements to avoid parsing overhead.

- **Trade-offs**: ---

## Query optimization improves performance and reduces database load, but the catch is it requires understanding your query patterns and database internals. The tricky part is premature optimization - you might add indexes that don't help or complicate queries unnecessarily. Always measure before and after to ensure optimizations actually help.

---

## Q56. Table partitioning – where to use?

Use table partitioning when you have very large tables that can be split logically - like partitioning orders by date so each month is a separate partition, or by region so each region is separate. Partitioning allows you to query only relevant partitions, drop old partitions easily, and can improve maintenance operations.

- **Trade-offs**: Partitioning can dramatically speed up queries that filter by the partition key and makes managing large tables easier, but the catch is it adds complexity - you need to choose partition keys carefully, and cross-partition queries can be slower. The tricky part is it's hard to change partitioning strategy later, so you need to plan ahead based on your query patterns.

Example:

```sql
-- Partition orders table by date (monthly partitions)
CREATE TABLE orders (
  id INT,
  user_id INT,
  created_at DATE,
  total DECIMAL
) PARTITION BY RANGE (YEAR(created_at) * 100 + MONTH(created_at)) (
  PARTITION p202401 VALUES LESS THAN (202402),
  PARTITION p202402 VALUES LESS THAN (202403),
  PARTITION p202403 VALUES LESS THAN (202404)
);

-- ---

## Query only scans relevant partition
SELECT * FROM orders WHERE created_at BETWEEN '2024-01-01' AND '2024-01-31';
```

---

## Q57. Write-ahead log internals.

Write-ahead log (WAL) records all changes to a log file before applying them to the database - when you update a row, the change is written to the WAL first, then to the actual data file. This ensures durability - if the server crashes, the database can replay the WAL to recover all committed transactions.

- **Trade-offs**: WAL provides durability and allows faster commits since writes are sequential, but the catch is it adds write overhead - every change is written twice (WAL and data file). The tricky part is WAL files grow and need to be checkpointed periodically to prevent them from getting too large, and recovery time depends on WAL size.

---

## Q58. Schema federation vs centralized DB.

Schema federation splits your database into multiple databases by domain or service - like having separate databases for users, orders, and products, each managed by different teams. Centralized DB keeps everything in one database with shared schemas. Choose federation when teams need independence and different scaling needs, choose centralized when you need strong consistency and complex joins.

- **Trade-offs**: Federation gives teams autonomy and allows you to scale databases independently, but the catch is cross-database queries become impossible and you lose referential integrity. Centralized DB makes joins and transactions easy, but the tricky part is it becomes a bottleneck as you scale, and schema changes require coordination across teams.

---

## Q59. Designing relational schema for e-commerce.

Design e-commerce schema with separate tables for users, products, orders, order_items, payments, and inventory - use foreign keys to maintain relationships, normalize to reduce redundancy, but denormalize where reads are frequent. Include indexes on foreign keys and commonly queried fields, and consider separate tables for product variants, reviews, and shipping addresses.

- **Trade-offs**: Normalized schema reduces data duplication and maintains integrity, but the catch is it requires JOINs for common queries which can be slow. Denormalizing improves read performance but makes updates more complex - if product price changes, you might need to update multiple places. The tricky part is balancing normalization with performance based on your access patterns.

Example:

```sql
-- Core e-commerce schema
CREATE TABLE users (id INT PRIMARY KEY, email VARCHAR, name VARCHAR);
CREATE TABLE products (id INT PRIMARY KEY, name VARCHAR, price DECIMAL);
CREATE TABLE orders (
  id INT PRIMARY KEY, 
  user_id INT REFERENCES users(id),
  total DECIMAL,
  created_at TIMESTAMP
);
CREATE TABLE order_items (
  id INT PRIMARY KEY,
  order_id INT REFERENCES orders(id),
  product_id INT REFERENCES products(id),
  quantity INT,
  price DECIMAL  -- Denormalized for historical accuracy
);
```

---

## Q60. Archival strategies for SQL databases.

Archive old data by moving it to separate archive tables or databases, using partitioning to isolate old partitions, or exporting to cold storage like S3. Keep recent data in the main database for fast queries, and archive data older than a threshold - like moving orders older than 2 years to an archive database.

- **Trade-offs**: Archiving keeps your main database small and fast, but the catch is accessing archived data requires different queries or restoring from backup. The tricky part is deciding what to archive and when - archive too aggressively and you lose useful data, archive too late and your database becomes slow. Consider legal requirements for data retention.

---

## Q61. Embed vs reference – decision rules.

Embed related data in the same document when the relationship is one-to-few, data is accessed together, and child data doesn't grow independently - like embedding addresses in a user document. Reference with ObjectIds when relationships are one-to-many, child data is large or accessed separately, or when the same child is referenced by multiple parents - like referencing products in order items.

- **Trade-offs**: Embedding makes reads fast since you get everything in one query, but the catch is documents can become large and you can't query embedded data efficiently. Referencing keeps documents small and allows independent updates, but the tricky part is you need multiple queries or $lookup to get related data, which is slower. The key is matching the pattern to your access patterns.

Example:

```javascript
// Embedding: User with addresses (one-to-few, accessed together)
{
  _id: ObjectId("..."),
  name: "John",
  addresses: [
    { street: "123 Main", city: "NYC" },
    { street: "456 Oak", city: "LA" }
  ]
}

// Referencing: Order with products (one-to-many, products accessed separately)
{
  _id: ObjectId("..."),
  user_id: ObjectId("..."),
  items: [
    { product_id: ObjectId("..."), quantity: 2 },
    { product_id: ObjectId("..."), quantity: 1 }
  ]
}
```

---

## Q62. MongoDB replica set – architecture.

A MongoDB replica set has one primary node that handles all writes and multiple secondary nodes that replicate data from the primary - clients read from primary by default but can read from secondaries for read scaling. If the primary fails, secondaries automatically elect a new primary through consensus, providing high availability.

- **Trade-offs**: Replica sets provide redundancy and automatic failover, which is great for availability, but the catch is you get eventual consistency - reads from secondaries might see stale data. The tricky part is replica lag - there's a delay between writes to primary and replication to secondaries, so if you need fresh data, you must read from primary.

---

## Q63. Choosing the right shard key.

Choose a shard key that distributes data evenly across shards, matches your query patterns, and avoids hotspots - like sharding users by user_id hash for even distribution, or by region if queries are region-specific. Avoid shard keys with low cardinality or that create hotspots - like sharding by boolean fields or timestamps that cluster writes.

- **Trade-offs**: A good shard key enables horizontal scaling and keeps queries fast by limiting which shards need to be queried, but the catch is you can't change the shard key later without migrating data. The tricky part is balancing even distribution with query locality - you want even distribution to avoid hotspots, but you also want queries to hit as few shards as possible.

Example:

```javascript
// Good shard key: user_id (high cardinality, even distribution)
sh.shardCollection("mydb.orders", { user_id: 1 });

// Bad shard key: status (low cardinality, creates hotspots)
// All "pending" orders go to one shard
sh.shardCollection("mydb.orders", { status: 1 });

// Good compound shard key: region + user_id
sh.shardCollection("mydb.orders", { region: 1, user_id: 1 });
```

---

## Q64. Aggregation pipeline performance rules.

Optimize aggregation pipelines by putting $match early to filter data, using $project to reduce data size, creating indexes on $match fields, using $limit to restrict results, and avoiding $unwind on large arrays. Use $lookup sparingly since it's expensive, and consider allowingDiskUse for large result sets.

- **Trade-offs**: Well-optimized pipelines are fast and efficient, but the catch is complex pipelines can consume lots of memory and CPU. The tricky part is the order of stages matters - filtering early reduces data flowing through later stages, but you need to understand how each stage works to optimize effectively.

---

## Q65. Designing high-write workloads.

Design for high writes by using write concerns that don't wait for replication, batching writes together, using unordered bulk operations, avoiding indexes on frequently updated fields, and sharding to distribute writes. Consider using change streams or TTL indexes to automatically clean up old data.

- **Trade-offs**: Optimizing for writes improves throughput, but the catch is you might sacrifice durability or consistency - lower write concerns mean faster writes but risk of data loss if primary crashes. The tricky part is balancing write performance with read performance - removing indexes helps writes but hurts reads, so you need to understand your access patterns.

---

## Q66. MongoDB multi-document transactions.

Multi-document transactions allow you to perform multiple operations across documents atomically - like updating an order and inventory in the same transaction, ensuring both succeed or both fail. They use snapshot isolation and require replica sets with WiredTiger storage engine.

- **Trade-offs**: Transactions provide ACID guarantees across documents which is great for data integrity, but the catch is they have performance overhead and can cause contention - long-running transactions hold locks and block other operations. The tricky part is they're slower than single-document operations, so use them only when you need cross-document consistency.

Example:

```javascript
const session = client.startSession();
session.startTransaction();
try {
  await orders.insertOne({ user_id: 123, total: 99.99 }, { session });
  await inventory.updateOne(
    { product_id: 456 },
    { $inc: { quantity: -1 } },
    { session }
  );
  await session.commitTransaction();
} catch (error) {
  await session.abortTransaction();
} finally {
  session.endSession();
}
```

---

## Q67. Indexing best practices in Mongo.

Create indexes on fields used in queries, use compound indexes that match query patterns, create indexes in the order of equality, sort, then range, and monitor index usage to remove unused ones. Use partial indexes for filtered queries, sparse indexes for optional fields, and TTL indexes for expiring data.

- **Trade-offs**: Good indexes make queries fast, but the catch is each index slows down writes and uses storage - MongoDB must update indexes on every insert/update. The tricky part is compound index field order matters - put equality fields first, then sort, then range, to maximize index usage.

---

## Q68. TTL index use cases.

Use TTL indexes to automatically delete documents after a time period - like expiring sessions after 24 hours, or cleaning up temporary data. MongoDB automatically deletes documents when the indexed date field is older than the TTL value, running a background task every 60 seconds.

- **Trade-offs**: TTL indexes automate data cleanup which is convenient, but the catch is deletion isn't immediate - there's up to 60 seconds delay, and the background task adds overhead. The tricky part is you can only have one TTL index per collection, and it only works on date fields, so you need to design your schema accordingly.

Example:

```javascript
// Create TTL index on created_at field, expire after 3600 seconds (1 hour)
db.sessions.createIndex({ created_at: 1 }, { expireAfterSeconds: 3600 });

// Documents automatically deleted when created_at is older than 1 hour
db.sessions.insertOne({ 
  user_id: 123, 
  created_at: new Date() 
});
```

---

## Q69. Time-series schema design.

Design time-series data with a document per time point, using compound indexes on time and tags, and bucketing multiple measurements into single documents when possible. Store metadata separately from measurements, use appropriate data types, and consider pre-aggregation for common queries.

- **Trade-offs**: Time-series schemas optimize for writes and time-range queries, but the catch is they're not great for complex analytics without aggregation. The tricky part is choosing the right granularity - too fine and you get too many documents, too coarse and you lose detail. Bucketing helps but adds complexity.

---

## Q70. Mongo high-throughput strategies.

Achieve high throughput by sharding to distribute load, using write concerns that don't wait for acknowledgment, batching operations, avoiding unnecessary indexes, and using connection pooling. Consider using change streams for real-time processing instead of polling, and use bulk operations for batch inserts.

- **Trade-offs**: These strategies improve throughput significantly, but the catch is you might sacrifice durability or consistency - lower write concerns mean faster writes but risk of data loss. The tricky part is balancing throughput with other requirements - you might need to accept eventual consistency or reduced durability for maximum throughput.

---

## Q71. Change streams use cases.

Use change streams to react to database changes in real-time - like updating a search index when documents change, sending notifications when orders are created, or syncing data to a cache. Change streams provide a stream of change events that your application can process as they happen.

- **Trade-offs**: Change streams enable real-time processing which is great for keeping systems in sync, but the catch is they add complexity and you need to handle reconnection and resume tokens. The tricky part is they only work on replica sets or sharded clusters, and processing changes adds load to your application.

Example:

```javascript
// Watch for changes to orders collection
const changeStream = db.orders.watch();

changeStream.on('change', (change) => {
  if (change.operationType === 'insert') {
    // New order created, update inventory
    updateInventory(change.fullDocument);
  }
});
```

---

## Q72. MongoDB anti-patterns.

Common anti-patterns include creating indexes on every field, using $lookup excessively, storing large arrays that grow unbounded, embedding when you should reference, using _id for business logic, and not using connection pooling. Avoid these by understanding your access patterns and MongoDB's strengths.

- **Trade-offs**: Avoiding anti-patterns keeps your database performant and maintainable, but the catch is some patterns seem convenient initially - like embedding everything to avoid joins. The tricky part is recognizing when you're hitting an anti-pattern - performance degradation might be gradual, so you need good monitoring.

---

## Q73. Redis architecture.

Redis is an in-memory data store that keeps all data in RAM for fast access, with optional persistence to disk using RDB snapshots or AOF logs. It supports various data structures like strings, hashes, lists, sets, and sorted sets, and can be deployed as a single instance, master-replica for read scaling, or clustered for horizontal scaling.

- **Trade-offs**: In-memory storage makes Redis extremely fast but limits capacity to available RAM, and data is lost on restart unless you use persistence. The catch is persistence options trade off between performance and durability - RDB is fast but might lose recent data, AOF is durable but slower. The tricky part is Redis is single-threaded for commands, so CPU-intensive operations block everything.

---

## Q74. Redis AOF vs RDB persistence.

RDB creates point-in-time snapshots of your dataset at intervals, which is fast and compact but might lose data since the last snapshot. AOF logs every write operation and replays them on startup, which is more durable but larger and slower. Use RDB for backups and fast restarts, use AOF when you need maximum durability.

- **Trade-offs**: RDB is fast and creates small files, but the catch is you might lose data written since the last snapshot if Redis crashes. AOF guarantees durability but uses more disk space and can be slower on restarts since it replays all operations. The tricky part is you can use both - RDB for backups, AOF for durability - but it uses more resources.

Example:

```redis
# RDB configuration - snapshot every 5 minutes if at least 1000 keys changed
save 300 1000

# AOF configuration - log every write
appendonly yes
appendfsync everysec  # Balance between performance and durability
```

---

## Q75. Redis pub/sub – pros & cons.

Redis pub/sub allows publishers to send messages to channels and subscribers receive them in real-time - like broadcasting notifications or coordinating between services. It's simple and fast, but messages are fire-and-forget with no persistence, so subscribers miss messages if they're not connected.

- **Trade-offs**: Pub/sub is great for real-time messaging and decoupling services, but the catch is it's unreliable - if a subscriber is down, it misses messages, and there's no message queuing. The tricky part is it doesn't scale well - each message is sent to all subscribers, so adding subscribers increases load on the publisher. Use it for notifications or events where losing messages is acceptable.

Example:

```javascript
// Publisher
redis.publish('notifications', JSON.stringify({ user_id: 123, message: 'Hello' }));

// Subscriber
redis.subscribe('notifications');
redis.on('message', (channel, message) => {
  const data = JSON.parse(message);
  sendNotification(data.user_id, data.message);
});
```

---

## Q76. Redis clustering — how it works.

Redis clustering distributes data across multiple nodes using hash slots - the key space is divided into 16384 slots, each assigned to a node, and keys are mapped to slots using CRC16 hash. Clients connect to any node, which redirects to the correct node if needed, and nodes monitor each other for failover.

- **Trade-offs**: Clustering enables horizontal scaling beyond single-machine memory limits and provides high availability through replication, but the catch is it adds complexity - you need at least 3 master nodes, and some operations like multi-key operations are limited to keys on the same node. The tricky part is rebalancing when you add or remove nodes requires moving hash slots, which can be disruptive.

---

## Q77. Distributed locking with Redis.

Use Redis for distributed locking by having clients try to set a key with a unique value and expiration - if the key doesn't exist, the client acquires the lock, otherwise it's held by another client. Use SET with NX and EX options atomically, and always release locks using the value to ensure you only release your own lock.

- **Trade-offs**: Redis locks are fast and simple, but the catch is they're not perfect - if a client crashes while holding a lock, the lock expires automatically, but there's a window where the lock might be held longer than intended. The tricky part is handling lock renewal for long operations and ensuring atomicity of lock acquisition and release.

Example:

```javascript
// Acquire lock with 10 second expiration
const lockKey = 'resource:123';
const lockValue = generateUniqueId();
const acquired = await redis.set(lockKey, lockValue, 'EX', 10, 'NX');

if (acquired) {
  try {
    // Do work
    await processResource(123);
  } finally {
    // Release only if we still own the lock
    const script = `
      if redis.call("get", KEYS[1]) == ARGV[1] then
        return redis.call("del", KEYS[1])
      else
        return 0
      end
    `;
    await redis.eval(script, 1, lockKey, lockValue);
  }
}
```

---

## Q78. Cache invalidation best practices.

Invalidate cache by deleting keys when underlying data changes, using TTLs for time-based expiration, using cache tags to invalidate related keys together, or using versioned keys that change when data updates. Choose invalidation strategy based on how often data changes and how critical freshness is.

- **Trade-offs**: Immediate invalidation ensures cache stays fresh but requires coordination between cache and database updates. TTL-based expiration is simple but might serve stale data. The tricky part is cache stampede - if cache expires and many requests come in, they all hit the database simultaneously. Use techniques like cache warming or probabilistic early expiration to avoid this.

Example:

```javascript
// Invalidate on update
async function updateUser(userId, data) {
  await db.users.update(userId, data);
  await redis.del(`user:${userId}`); // Invalidate cache
}

// TTL-based expiration
await redis.setex(`user:${userId}`, 3600, userData); // Expires in 1 hour

// Versioned keys
const version = await getDataVersion(userId);
await redis.set(`user:${userId}:v${version}`, userData);
```

---

## Q79. Avoiding memory eviction issues.

Avoid eviction by monitoring memory usage, setting appropriate maxmemory policy (like allkeys-lru for cache, noeviction for critical data), using TTLs to expire old data automatically, and sizing your Redis instance correctly. Monitor eviction metrics to catch issues early, and consider using Redis Cluster to distribute memory across nodes.

- **Trade-offs**: Proper memory management prevents unexpected evictions, but the catch is you need to understand your data access patterns to choose the right eviction policy. The tricky part is balancing memory usage with performance - too little memory and you evict frequently, too much and you waste resources. Use maxmemory-policy carefully based on whether you're using Redis as cache or primary storage.

---

## Q80. Redis vs Memcached differences.

Redis is a data structure server with persistence, replication, and complex data types like sorted sets and pub/sub, while Memcached is a simple key-value cache with no persistence or replication. Choose Redis when you need advanced features, persistence, or complex data structures. Choose Memcached when you need a simple, high-performance cache and don't need persistence.

- **Trade-offs**: Redis is more feature-rich and can be used for more than caching, but the catch is it's more complex and uses more memory per key due to metadata. Memcached is simpler and slightly faster for basic operations, but the tricky part is it's purely a cache - data can be evicted or lost on restart, and it only supports simple key-value operations. For most modern applications, Redis is the better choice unless you have specific performance requirements.
