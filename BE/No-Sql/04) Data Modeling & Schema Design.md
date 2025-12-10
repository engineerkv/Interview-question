# 🏗️ 4. Data Modeling & Schema Design (Q42–57)

---

## 📍 Navigation

<div align="center">

[Aggregation Framework](03%29%20Aggregation%20Framework.md) • [Home: Question List](question.md)

[📋 Cheatsheet](MongoDB%20Interview%20Cheatsheet.md)

</div>

---

---

## Q42. 💡 Designing schemas in MongoDB

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

## Q43. 🤔 Difference between embedding and referencing documents

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

## Q44. 💡 Modeling one-to-many relationships

For one-to-many: embed for small arrays, reference for large arrays. For many-to-many: use arrays of references or separate junction collections. Design based on your most common query patterns and how frequently data changes.

- **Trade-offs**: Embedding small arrays keeps related data together for fast reads, but large arrays can hit the 16MB document limit. Referencing scales better but requires joins—for many-to-many, arrays work for simple cases, but junction collections handle complex relationships better.

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

## Q45. 💡 Modeling many-to-many relationships

Many-to-many relationships in MongoDB are modeled using arrays of ObjectIds in both documents, or more commonly with a separate junction/join collection that stores pairs of references. Use arrays when relationships are simple and bounded, use junction collections when relationships have attributes or need to scale.

- **Trade-offs**: Arrays of references are simple and work well for small, bounded relationships (like user tags), but these can grow large and make queries complex. Junction collections scale better, allow relationship attributes (like quantity, date), and enable efficient queries in both directions—use junction collections for e-commerce (users-products), social networks (users-friends), or any relationship with metadata.

Example:

```javascript
// Option 1: Arrays of references (simple, bounded relationships)
// users collection
{ _id: ObjectId("..."), name: "John", tagIds: [ObjectId("..."), ObjectId("...")] }
// tags collection
{ _id: ObjectId("..."), name: "javascript" }

// Option 2: Junction collection (scalable, with attributes)
// users collection
{ _id: ObjectId("..."), name: "John" }
// products collection
{ _id: ObjectId("..."), name: "Laptop" }
// user_products collection (junction)
{
  userId: ObjectId("..."),
  productId: ObjectId("..."),
  quantity: 2,
  addedAt: new Date()
}

```

---

## Q46. 🍃 ⏰ When to denormalize data in MongoDB

Denormalization involves storing redundant data to improve read performance, beneficial when read operations significantly outnumber write operations. It speeds up queries by avoiding joins and keeping related data together, but requires updating multiple documents when data changes.

- **Trade-offs**: Denormalization gives you faster reads with embedded data, but updates require modifying multiple documents which increases write overhead. You also pay a storage cost for data duplication and risk inconsistency across documents—use it for read-heavy applications, reporting, analytics, or when embedding small, frequently accessed data that changes infrequently. Avoid denormalization when data changes frequently or when consistency is critical.

Example:

```javascript
// Denormalized approach for read optimization
// Orders collection with embedded customer data (read-heavy)
{
  _id: ObjectId("..."),
  orderNumber: "ORD001",
  customer: {
    name: "John Doe",
    email: "john@example.com"
  },
  amount: 100
}

// Use when: reads >> writes, data changes infrequently
// Avoid when: data changes frequently, consistency is critical

```

---

## Q47. 🔧 Implementing schema validation in MongoDB

Schema validation rules enforce data structure and content constraints using JSON Schema, ensuring data quality and consistency at the database level. You can set validation to strict (reject invalid docs) or moderate (warn but allow), and update rules without downtime.

- **Trade-offs**: Validation ensures consistent data structure and provides clear error messages, but has minimal impact on write performance. The catch is you need to design schemas carefully—too strict and you'll block legitimate data, too loose and you lose the benefits. Use `validationLevel: "strict"` for production data quality, `"moderate"` for gradual enforcement, and `validationAction: "error"` to reject invalid documents.

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

## Q48. 🔧 Sharding in MongoDB and how it works

Sharding distributes data across multiple servers for horizontal scaling, with shard keys determining data distribution and affecting query performance. MongoDB automatically manages data chunks, but poor shard key selection can cause uneven distribution and slow queries.

- **Trade-offs**: Sharding enables horizontal scaling and distributes load, but shard key selection is critical—queries with the shard key are efficient (targeted to specific shards), while queries without it must hit all shards (scatter-gather). The catch is you can't change the shard key after sharding, so choose carefully.

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

## Q49. 🔧 Shard keys and how to choose them

Shard keys determine how data is distributed across shards—choose keys with high cardinality, even distribution, and that match your query patterns. Good shard keys prevent hotspots and enable targeted queries to specific shards.

- **Trade-offs**: Shard keys can't be changed after sharding, so choose carefully. Keys with low cardinality cause uneven distribution, while keys that don't match query patterns force scatter-gather queries across all shards—ideal shard keys have high cardinality, even distribution, and appear in most queries.

Example:

```javascript
// Good shard key: high cardinality, even distribution
sh.shardCollection("ecommerce.orders", { customerId: 1, orderDate: 1 });

// Bad shard key: low cardinality (only a few values)
sh.shardCollection("ecommerce.orders", { status: 1 });  // Only: pending, completed, cancelled

// Compound shard key for better distribution
sh.shardCollection("ecommerce.orders", {
  customerId: 1,  // High cardinality
  orderDate: 1    // Time-based for even distribution
});

```

---

## Q50. 🔧 Replication in MongoDB and how it works

Replication creates multiple copies of data across different servers in a replica set, ensuring high availability, data redundancy, and automatic failover. One node serves as primary (handles writes), while secondaries replicate data and can handle reads or become primary if the primary fails.

- **Trade-offs**: Replication provides high availability and prevents data loss, but you need at least 3 nodes for a proper replica set. Write concern controls acknowledgment requirements (more nodes = better durability but slower writes), and read preference allows you to control which replica set member to read from—balance consistency needs with performance.

Example:

```javascript
// Replica set configuration
{
  _id: "rs0",
  members: [
    { _id: 0, host: "mongodb1:27017", priority: 2 },  // Primary
    { _id: 1, host: "mongodb2:27017", priority: 1 },  // Secondary
    { _id: 2, host: "mongodb3:27017", priority: 1 }   // Secondary
  ]
}

// Read from secondary for read scaling
db.orders.find().readPref("secondary");

```

---

## Q51. 💡 Write concern and read concern in MongoDB

Write concern controls acknowledgment requirements for write operations (how many nodes must confirm the write), while read concern determines data consistency guarantees for reads (what version of data you see). Both affect performance and reliability—higher concerns mean better consistency but slower performance.

- **Trade-offs**: Write concern `w: 1` (primary only) is fast but risks data loss if primary crashes before replication, while `w: "majority"` is safer but slower. Read concern `"local"` is fast but may return uncommitted data, while `"majority"` ensures committed data but is slower—choose based on your consistency needs versus performance.

Example:

```javascript
// Write concern levels
db.orders.insertOne(
  { orderId: "ORD001" },
  { writeConcern: { w: 1 } }  // Acknowledge from primary only (fast)
);

db.orders.insertOne(
  { orderId: "ORD002" },
  { writeConcern: { w: "majority", j: true } }  // Majority + journal (safer)
);

// Read concern
db.orders.find({ orderId: "ORD001" })
  .readConcern("local");  // Fast, may return uncommitted

db.orders.find({ orderId: "ORD001" })
  .readConcern("majority");  // Slower, ensures committed data

```

---

## Q52. 📝 Mongoose schema types and validation

Mongoose schemas support various types (String, Number, Date, Boolean, Array, ObjectId, Mixed) and built-in validators (required, min, max, enum, match, custom) that enforce data integrity at the application level.

- **Trade-offs**: Schema validation prevents bad data from entering the database, which is great for data quality, but the catch is validation only runs when using Mongoose methods (not direct MongoDB operations). Built-in validators are convenient, but custom validators give you full control—always validate at both schema and application levels for critical data.

Example:

```javascript
const userSchema = new mongoose.Schema({
  name: { type: String, required: true, trim: true },
  age: { type: Number, min: 0, max: 120 },
  email: {
    type: String,
    required: true,
    match: /^[\w.%+-]+@[\w.-]+\.[A-Za-z]{2,}$/
  },
  role: { type: String, enum: ['user', 'admin'], default: 'user' }
});

```

---

## Q53. 💡 Mongoose virtuals and computed properties

Virtuals are document properties that aren't stored in MongoDB but computed on-the-fly from other fields, useful for formatting, combining fields, or creating derived values without duplicating data.

- **Trade-offs**: Virtuals keep your data normalized while providing convenient computed properties, but the catch is these are not queryable (can't use them in `find()` filters) and add slight overhead. Use them for display formatting, full names, or calculated fields—remember to include them in JSON output with `toJSON: { virtuals: true }` if needed.

Example:

```javascript
userSchema.virtual('fullName').get(function() {
  return `${this.firstName} ${this.lastName}`;
});
userSchema.set('toJSON', { virtuals: true });
const user = await User.findOne();
console.log(user.fullName); // "John Doe"

```

---

## Q54. 💡 Mongoose instance methods and static methods

Instance methods are defined on the schema and called on document instances (e.g., `user.save()`), while static methods are called on the model itself (e.g., `User.findByEmail()`), allowing you to encapsulate business logic within your models.

- **Trade-offs**: Methods keep logic close to data and improve code organization, but the catch is these are only available when using Mongoose (not with raw MongoDB queries). Instance methods work on single documents, static methods work on collections—use instance methods for document-specific logic, static methods for collection-level operations or custom finders.

Example:

```javascript
userSchema.methods.getAge = function() {
  return new Date().getFullYear() - this.birthYear;
};
userSchema.statics.findByEmail = function(email) {
  return this.findOne({ email: email.toLowerCase() });
};
const user = await User.findByEmail('john@example.com');
const age = user.getAge();

```

---

## Q55. 🪝 🪝 🪝 🪝 Mongoose middleware (pre/post hooks)

Mongoose middleware hooks allow you to execute functions before or after specific operations (save, validate, remove, init) on documents, enabling cross-cutting concerns like password hashing, timestamps, or logging.

- **Trade-offs**: Middleware provides powerful hooks for common operations, but the catch is these can make code harder to debug and add overhead if overused. Pre hooks can modify documents or cancel operations, post hooks run after operations complete—use them for authentication, logging, or data transformation, but avoid complex async operations that could slow down saves.

Example:

```javascript
userSchema.pre('save', async function(next) {
  if (this.isModified('password')) {
    this.password = await bcrypt.hash(this.password, 10);
  }
  next();
});
userSchema.post('save', function(doc) {
  console.log(`User ${doc.name} saved`);
});

```

---

## Q56. 💡 Mongoose population and referencing documents

Population automatically replaces ObjectId references with the actual documents from other collections using `populate()`, making it easy to work with related data without manual joins.

- **Trade-offs**: Population is convenient for simple references and reads like SQL JOINs, but the catch is it can cause N+1 query problems and doesn't support complex filtering like aggregation. Use `populate()` for simple one-to-many or many-to-one relationships, but prefer aggregation with `$lookup` for complex joins or when you need to filter populated data—always be mindful of performance with deeply nested populations.

Example:

```javascript
const orderSchema = new mongoose.Schema({
  customerId: { type: mongoose.Schema.Types.ObjectId, ref: 'User' },
  items: [{ productId: { type: mongoose.Schema.Types.ObjectId, ref: 'Product' } }]
});
const order = await Order.findOne().populate('customerId').populate('items.productId');

```

---

## Q57. 💡 Mongoose schema options and configuration

Mongoose schemas support various options like `timestamps`, `versionKey`, `strict`, `collection`, and `id` that control behavior, automatic fields, and how documents are stored and retrieved.

- **Trade-offs**: Schema options provide convenient defaults and behavior control, but the catch is some options (like `strict: false`) can lead to unexpected data if not used carefully. `timestamps` automatically adds `createdAt` and `updatedAt`, `versionKey` adds `__v` for optimistic concurrency, `strict` prevents undefined fields—use options wisely based on your needs, and prefer explicit over implicit behavior in production.

Example:

```javascript
const userSchema = new mongoose.Schema({
  name: String,
  email: String
}, {
  timestamps: true, // Adds createdAt, updatedAt
  versionKey: false, // Removes __v
  strict: true, // Only save defined fields
  collection: 'users' // Custom collection name
});

```

---

---

## 📍 Navigation

<div align="center">

[Aggregation Framework](03%29%20Aggregation%20Framework.md) • [Home: Question List](question.md)

[📋 Cheatsheet](MongoDB%20Interview%20Cheatsheet.md)

</div>

---
