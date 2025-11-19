# 4. Data Modeling & Schema Design (Q31–40)

---

## Q31. What is schema design in MongoDB, and why is it critical for performance?

Schema design determines how data is organized and stored, directly impacting query performance, storage efficiency, and application scalability in MongoDB. Good schema design enables efficient queries, reduces storage costs, and supports horizontal scaling.

- **Trade-offs**: Well-designed schemas are easier to maintain and optimize, but poor schema choices can lead to slow queries, wasted storage, and scaling bottlenecks—always design based on your actual query patterns, not theoretical ideals.

Example:
```javascript
// Good schema design for e-commerce
// Products collection
{
  _id: ObjectId("..."),
  name: "Laptop",
  price: 999.99,
  category: "electronics",
  inStock: true
}
```

---

## Q32. What are the trade-offs between embedding and referencing documents?

Embedding provides faster reads and atomic updates but can lead to large documents, while referencing offers better data consistency but requires multiple queries. Embed for small, frequently accessed data that changes together; reference for large or independently changing data.

- **Trade-offs**: Embedding keeps related data together for fast single-document reads, but MongoDB has a 16MB document size limit and updates can bloat documents. Referencing keeps documents smaller and more consistent, but requires joins via `$lookup` which can be slower—choose based on your query patterns and update frequency.

Example:
```javascript
// Embedded approach (denormalized)
{
  _id: ObjectId("..."),
  name: "John Doe",
  email: "john@example.com",
  address: {
    street: "123 Main St",
    city: "New York",
    zip: "10001"
  }
}

// Referenced approach
{
  _id: ObjectId("..."),
  name: "John Doe",
  email: "john@example.com",
  addressId: ObjectId("...")
}
```

---

## Q33. How do you design a schema for a one-to-many and many-to-many relationship in MongoDB?

For one-to-many: embed for small arrays, reference for large arrays. For many-to-many: use arrays of references or separate junction collections. Design based on your most common query patterns and how frequently data changes.

- **Trade-offs**: Embedding small arrays keeps related data together for fast reads, but large arrays can hit the 16MB document limit. Referencing scales better but requires joins. For many-to-many, arrays work for simple cases, but junction collections handle complex relationships better—plan for future growth and data volume.

Example:
```javascript
// One-to-Many: User to Orders
// Option 1: Embed (for small number of orders)
{
  _id: ObjectId("..."),
  name: "John",
  orders: [
    { orderId: "ORD001", amount: 100 },
    { orderId: "ORD002", amount: 200 }
  ]
}

// Option 2: Reference (for large number of orders)
{
  _id: ObjectId("..."),
  name: "John",
  orderIds: [ObjectId("..."), ObjectId("...")]
}

// Many-to-Many: Users to Products (junction collection)
// users collection
{ _id: ObjectId("..."), name: "John" }
// products collection
{ _id: ObjectId("..."), name: "Laptop" }
// user_products collection (junction)
{ userId: ObjectId("..."), productId: ObjectId("..."), quantity: 2 }
```

---

## Q34. What is data denormalization, and when is it beneficial in MongoDB?

Denormalization involves storing redundant data to improve read performance, beneficial when read operations significantly outnumber write operations. It speeds up queries by avoiding joins, but requires updating multiple documents when data changes.

- **Trade-offs**: Denormalization gives you faster reads with embedded data, but updates require modifying multiple documents which increases write overhead. You also pay a storage cost for data duplication and risk inconsistency across documents—use it for read-heavy applications, reporting, and analytics where reads far outnumber writes.

Example:
```javascript
// Denormalized approach for read optimization
// Orders collection with embedded customer data
{
  _id: ObjectId("..."),
  orderNumber: "ORD001",
  customer: {
    name: "John Doe",
    email: "john@example.com"
  },
  amount: 100
}
```

---

## Q35. What are schema validation rules, and how can you enforce them using JSON Schema?

Schema validation rules enforce data structure and content constraints using JSON Schema, ensuring data quality and consistency at the database level. You can set validation to strict (reject invalid docs) or moderate (warn but allow), and update rules without downtime.

- **Trade-offs**: Validation ensures consistent data structure and provides clear error messages, but has minimal impact on write performance. The catch is you need to design schemas carefully—too strict and you'll block legitimate data, too loose and you lose the benefits.

Example:
```javascript
// Create collection with schema validation
db.createCollection("users", {
  validator: {
    $jsonSchema: {
      bsonType: "object",
      required: ["name", "email", "age"],
      properties: {
        name: { bsonType: "string" },
        email: { bsonType: "string", pattern: "^.+@.+$" },
        age: { bsonType: "int", minimum: 0 }
      }
    }
  },
  validationLevel: "strict",
  validationAction: "error"
});
```

---

## Q36. How do you migrate or refactor schema structures in MongoDB production environments?

Use gradual migration strategies, version fields, backward compatibility, and careful testing to safely update schemas in production without data loss. Migrate data in batches to avoid downtime, and always have a rollback plan for failed migrations.

- **Trade-offs**: Versioning lets you track schema changes and maintain backward compatibility with old data, but you need to thoroughly test migration scripts in staging first. The tricky part is balancing gradual migration (safer but slower) with faster approaches (riskier but less downtime)—always prioritize data safety over speed.

Example:
```javascript
// Add version field to existing documents
db.users.updateMany(
  { version: { $exists: false } },
  { $set: { version: 1 } }
);

// Migrate to new schema version
db.users.updateMany(
  { version: 1 },
  [
    { $set: { version: 2, fullName: { $concat: ["$firstName", " ", "$lastName"] } } }
  ]
);
```

---

## Q37. What are sharding and shard keys, and how do they affect data distribution and performance?

Sharding distributes data across multiple servers for horizontal scaling, with shard keys determining data distribution and affecting query performance. MongoDB automatically manages data chunks, but poor shard key selection can cause uneven distribution and slow queries.

- **Trade-offs**: Sharding enables horizontal scaling and distributes load, but shard key selection is critical—queries with the shard key are efficient (targeted to specific shards), while queries without it must hit all shards (scatter-gather). The catch is you can't change the shard key after sharding, so choose carefully based on your query patterns.

Example:
```javascript
// Enable sharding on database
sh.enableSharding("ecommerce");

// Shard collection with compound shard key
sh.shardCollection("ecommerce.orders", {
  customerId: 1,
  orderDate: 1
});
```

---

## Q38. What is replication, and how does MongoDB ensure high availability and redundancy?

Replication creates multiple copies of data across different servers, ensuring high availability, data redundancy, and automatic failover capabilities. When the primary fails, a secondary automatically becomes primary, and secondary nodes can handle read operations for read scaling.

- **Trade-offs**: Replication provides high availability and prevents data loss, but you need at least 3 nodes for a proper replica set (or use an arbiter for cost savings). Write concern controls acknowledgment requirements (more nodes = better durability but slower writes), and read preference lets you control which replica set member to read from—balance consistency needs with performance.

Example:
```javascript
// Replica set configuration
{
  _id: "rs0",
  members: [
    { _id: 0, host: "mongodb1:27017", priority: 2 },
    { _id: 1, host: "mongodb2:27017", priority: 1 },
    { _id: 2, host: "mongodb3:27017", priority: 1 }
  ]
}
```

---

## Q39. What is write concern and read concern, and how do they affect data consistency and performance?

Write concern controls acknowledgment requirements for write operations (how many nodes must confirm the write), while read concern determines data consistency guarantees for reads (what version of data you see). Both affect performance and reliability—higher concerns mean better consistency but slower performance.

- **Trade-offs**: Write concern `w: 1` (primary only) is fast but risks data loss if primary crashes before replication. `w: "majority"` is safer but slower. Read concern `"local"` is fast but may return uncommitted data, while `"majority"` ensures committed data but is slower—choose based on your application's consistency needs versus performance requirements.

Example:
```javascript
// Write concern levels
db.orders.insertOne(
  { orderId: "ORD001" },
  { writeConcern: { w: 1 } }  // Acknowledge from primary only
);

// Read concern
db.orders.find({ orderId: "ORD001" })
  .readConcern("majority");
```

---

## Q40. What are common techniques to optimize MongoDB queries and indexes for high-performance applications?

Optimize through proper indexing based on query patterns, query analysis with `explain()`, schema design that matches access patterns, connection pooling to reuse connections, application-level caching for hot data, and monitoring performance metrics. Create indexes that match your most common queries, use covered queries when possible, and analyze slow queries regularly.

- **Trade-offs**: Proper indexing dramatically speeds up queries but slows writes and consumes RAM/disk. Connection pooling reduces overhead but requires tuning pool size. Caching improves read performance but adds complexity and can serve stale data. The key is to measure first—use `explain()` and monitoring tools to identify actual bottlenecks before optimizing.

Example:
```javascript
// 1. Create proper indexes
db.orders.createIndex({ customerId: 1, createdAt: -1 });
db.orders.createIndex({ status: 1, createdAt: -1 });

// 2. Use covered queries
db.orders.find(
  { customerId: ObjectId("...") },
  { customerId: 1, createdAt: 1, _id: 0 }
);

// 3. Analyze query performance
db.orders.find({ status: "pending" }).explain("executionStats");
```

---
