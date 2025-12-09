# 🍃 1. MongoDB Fundamentals (Q1–16)

---

## 📍 Navigation

<div align="center">

[Home: Question List](question.md) • [Indexing & Query Optimization →](2%29%20Indexing%20%26%20Query%20Optimization.md)

[📋 Cheatsheet](MongoDB%20Interview%20Cheatsheet.md]

</div>

---

---

## Q1. 🗄️ MongoDB and what type of NoSQL database it is

MongoDB is a document-oriented NoSQL database that stores data as flexible BSON documents in collections, allowing each record to have different fields without requiring schema changes. Unlike relational databases with fixed tables, MongoDB allows documents to evolve independently, making it perfect for handling varied or rapidly changing data structures.

- **Trade-offs**: Works great for rapid development and handling heterogeneous data, but the catch is you lose automatic foreign key constraints and need careful design for multi-document transactions. Avoid it when you need strict relational integrity or complex cross-document transactions.

Example:

```javascript
{
  _id: ObjectId("507f1f77bcf86cd799439011"),
  name: "John Doe",
  age: 30,
  address: { city: "NYC", country: "USA" }
}

```

---

## Q2. 🗄️ Key differences between MongoDB and relational databases like MySQL

MongoDB stores flexible JSON-like documents in collections without fixed schemas, while MySQL uses structured tables with fixed rows and columns. MongoDB queries with JSON-like syntax and scales horizontally through sharding, while MySQL uses SQL with JOINs and typically scales vertically. MongoDB allows you to embed related data in documents or reference other documents via ObjectIds, while MySQL enforces foreign keys and automatic JOINs.

- **Trade-offs**: MongoDB gains agility and horizontal scaling by relaxing schema and relationships, but the catch is you lose automatic foreign keys, multi-table transactions by default, and well-known SQL tooling. MySQL provides strong consistency, mature tooling, and familiar SQL, but requires schema migrations and struggles with horizontal scaling.

Example:

```javascript
db.users.insertOne({
  name: "John",
  age: 30,
  address: { city: "NYC", country: "USA" },
  hobbies: ["reading", "gaming"]
});

```

---

## Q3. 💡 Collections and documents in MongoDB

Collections are logical groupings of documents (equivalent to tables) with no fixed schema, and documents are BSON objects (equivalent to rows) stored within collections, so structures can differ per document.

- **Trade-offs**: Flexibility makes evolving models easy, but the catch is inconsistent shapes can complicate analytics and validation—use schema validation when you need guardrails.

Example:

```javascript
db.users.insertMany([
  { name: "Alice", email: "alice@example.com" },
  { name: "Bob", phone: "123-456-7890", address: { city: "LA" } }
]);

```

---

## Q4. 🔧 BSON and how it differs from JSON

BSON is MongoDB's binary JSON that adds data types such as ObjectId, Date, and Decimal128, enabling faster parsing and richer data than plain JSON strings.

- **Trade-offs**: Extended types and binary encoding improve storage and speed, but the catch is payloads are slightly larger and require MongoDB drivers to interpret them.

Example:

```javascript
{
  name: "John",
  age: 30,
  date: new Date("2023-12-01T10:30:00Z"),
  _id: ObjectId("507f1f77bcf86cd799439011")
}

```

---

## Q5. ❓ What it means for MongoDB to be schema-less

Schema-less stores don't force predefined columns, so you can insert documents with new fields anytime, accelerating prototyping and heterogeneous data ingestion.

- **Trade-offs**: Flexibility speeds delivery, but the catch is you must actively prevent inconsistency, enforce validation rules, and design queries carefully to avoid performance surprises.

Example:

```javascript
db.products.insertMany([
  { name: "Laptop", price: 999.99, specs: { ram: "16GB" } },
  { name: "Book", price: 19.99, author: "John Smith" }
]);

```

---

## Q6. 🤔 Difference between embedded(denormalized) and referenced(normalized) data models

Embedded (denormalized) documents store related data inside a single document for fast reads, while referenced (normalized) models link to other documents via ObjectIds.

- **Trade-offs**: Embed when the relationship is tight and read-heavy, but the catch is you can't share subdocuments and updates require rewriting the parent. Reference when subdocuments grow independently or need reuse, but watch out for needing multiple queries or aggregation pipelines for joins.

Example:

```javascript
// Embedded
{ name: "John", address: { street: "123 Main", city: "NYC" } }

// Referenced
{ name: "John", addressId: ObjectId("...") }

```

---

## Q7. 💡 CRUD operations in MongoDB

CRUD maps to insertOne/insertMany for create, find/findOne for read, updateOne/updateMany for update, and deleteOne/deleteMany for delete—all using JSON-like filters. `insertOne()` inserts a single document and returns the inserted document's `_id`, `insertMany()` inserts multiple documents and returns an array of `_id`s, while `insert()` is deprecated. `updateOne()` updates the first matching document, `updateMany()` updates all matches, while `update()` is deprecated. `deleteOne()` deletes the first match, `deleteMany()` deletes all matches, while `delete()` is deprecated.

- **Trade-offs**: Single-document operations are atomic, but the catch is multi-document writes aren't (unless you use transactions), so model data to keep critical updates within one doc. Modern methods (`insertOne`/`insertMany`, `updateOne`/`updateMany`, `deleteOne`/`deleteMany`) are explicit and safer, but watch out for `insertMany()` being slower on large arrays, update operations requiring operators like `$set` or you'll replace the entire document, and `deleteMany()` without a filter deleting all documents.

Example:

```javascript
// Create
const result = db.users.insertOne({ name: "John", age: 30 });
const results = db.users.insertMany([
  { name: "Alice", age: 25 },
  { name: "Bob", age: 35 }
]);

// Read
db.users.find({ age: { $gt: 25 } });
db.users.findOne({ name: "John" });

// Update
db.users.updateOne({ name: "John" }, { $set: { age: 31 } });
db.users.updateMany({ age: { $lt: 18 } }, { $set: { status: "minor" } });

// Delete
db.users.deleteOne({ name: "John" });
db.users.deleteMany({ age: { $lt: 18 } });

```

---

## Q8. 📝 MongoDB operators and their types

MongoDB operators are special keywords prefixed with `$` that perform specific operations—query operators filter documents (`$lt`, `$gt`, `$in`, `$exists`), update operators modify fields (`$set`, `$inc`, `$push`, `$pull`), logical operators combine conditions (`$and`, `$or`, `$not`), and array operators manipulate arrays (`$addToSet`, `$pop`, `$slice`).

- **Trade-offs**: Operators make queries and updates powerful and flexible, but the catch is you must use update operators in update operations (like `$set`) or you'll replace the entire document. Query operators are intuitive once you learn them, but mixing them incorrectly can lead to unexpected results—always test complex queries.

Example:

```javascript
// Query operators - filter documents
db.users.find({ age: { $lt: 30, $gte: 18 } });  // Less than 30, >= 18
db.users.find({ name: { $in: ["John", "Alice"] } });  // In array
db.users.find({ email: { $exists: true } });  // Field exists
db.users.find({ age: { $ne: 25 } });  // Not equal
db.users.find({ name: { $regex: /^J/ } });  // Pattern match

// Logical operators - combine conditions
db.users.find({ $or: [{ age: { $lt: 18 } }, { status: "inactive" }] });
db.users.find({ $and: [{ age: { $gte: 18 } }, { age: { $lte: 65 } }] });

// Update operators - modify fields
db.users.updateOne({ name: "John" }, { $set: { age: 31 } });  // Set value
db.users.updateOne({ name: "John" }, { $inc: { loginCount: 1 } });  // Increment
db.users.updateOne({ name: "John" }, { $push: { hobbies: "reading" } });  // Add to array
db.users.updateOne({ name: "John" }, { $pull: { hobbies: "gaming" } });  // Remove from array
db.users.updateOne({ name: "John" }, { $unset: { tempField: "" } });  // Remove field
db.users.updateOne({ name: "John" }, { $addToSet: { tags: "vip" } });  // Add unique to array

```

---

## Q9. 🔧 How MongoDB ensures data consistency

Consistency comes from application-side validation, built-in JSON schema validators, and disciplined data modeling—MongoDB enforces whatever rules you configure.

- **Trade-offs**: Gives teams control over rules per collection, but the catch is missing validators or sloppy modeling quickly lead to messy data—always pair validation with indexes.

Example:

```javascript
db.createCollection("users", {
  validator: {
    $jsonSchema: {
      bsonType: "object",
      required: ["name", "email"],
      properties: {
        name: { bsonType: "string" },
        email: { bsonType: "string", pattern: "^[\\w.%+-]+@[\\w.-]+\\.[A-Za-z]{2,}$" }
      }
    }
  }
});

```

---

## Q10. 💡 Capped collections in MongoDB

Capped collections are fixed-size, circular buffers that overwrite the oldest documents when reaching their byte or count limit—perfect for logs and real-time feeds.

- **Trade-offs**: Writes are blazing fast and storage bounded, but the catch is you can't remove individual docs or grow past the cap—use them only when FIFO behavior is acceptable.

Example:

```javascript
db.createCollection("logs", {
  capped: true,
  size: 1_000_000,
  max: 1000
});

```

---

## Q11. 📊 Difference between `findOne()`, `find()`, and aggregation

`findOne()` fetches a single document, `find()` returns a cursor you can iterate, and aggregation pipelines process documents through multiple stages that filter, group, reshape, and transform data.

- **Trade-offs**: Use findOne for keyed lookups when you need a single document, find works great for filtered lists with sorting and limits, and aggregation is perfect for analytics or joins. The catch is aggregations can be resource-heavy without proper indexes, so always check your query plans.

Example:

```javascript
const user = db.users.findOne({ name: "John" });
const users = db.users.find({ age: { $gte: 25 } }).limit(10);
db.users.aggregate([
  { $match: { age: { $gte: 25 } } },
  { $group: { _id: "$department", count: { $sum: 1 } } }
]);

```

---

## Q12. 🔧 Mongoose and how it works with MongoDB

Mongoose is an ODM (Object Document Mapper) for MongoDB in Node.js that provides schema-based modeling, validation, middleware hooks, and type casting, making it easier to work with MongoDB in JavaScript applications.

- **Trade-offs**: Mongoose adds structure and validation to MongoDB's flexibility, which speeds development and prevents errors, but the catch is it adds overhead and learning curve compared to the native driver. Use it when you need schema enforcement, validation, and middleware—skip it for simple scripts or when you need maximum performance with raw queries.

Example:

```javascript
const mongoose = require('mongoose');
const userSchema = new mongoose.Schema({
  name: { type: String, required: true },
  age: { type: Number, min: 0 }
});
const User = mongoose.model('User', userSchema);

```

---

## Q13. 💡 Connecting to MongoDB using Mongoose

Mongoose connects to MongoDB using `mongoose.connect()` with a connection string, and manages connection state, retries, and connection pooling automatically.

- **Trade-offs**: Mongoose handles connection management and pooling well, but the catch is you need to handle connection errors and close connections properly in production. Always use connection options like `useNewUrlParser` and `useUnifiedTopology`, and handle `disconnected` and `error` events for reliability.

Example:

```javascript
mongoose.connect('mongodb://localhost:27017/myapp', {
  useNewUrlParser: true,
  useUnifiedTopology: true
});
mongoose.connection.on('connected', () => console.log('Connected'));
mongoose.connection.on('error', (err) => console.error(err));

```

---

## Q14. 💡 Connection pooling in MongoDB

Connection pooling maintains a cache of database connections that can be reused across multiple requests, avoiding the overhead of creating and destroying connections for each operation. MongoDB drivers automatically manage connection pools, allowing you to configure pool size, max idle time, and connection timeouts.

- **Trade-offs**: Connection pooling improves performance by reusing connections, but the catch is you need to configure pool size based on your application's concurrency needs—too small and you'll have connection wait times, too large and you'll waste resources. Default pool sizes work for most apps, but high-traffic applications need tuning—monitor connection pool metrics to find the right balance.

Example:

```javascript
// Mongoose connection with pool options
mongoose.connect('mongodb://localhost:27017/myapp', {
  maxPoolSize: 10,        // Maximum connections in pool
  minPoolSize: 2,         // Minimum connections to maintain
  maxIdleTimeMS: 30000,   // Close idle connections after 30s
  serverSelectionTimeoutMS: 5000
});

// Native MongoDB driver with pool options
const { MongoClient } = require('mongodb');
const client = new MongoClient('mongodb://localhost:27017', {
  maxPoolSize: 10,
  minPoolSize: 2,
  maxIdleTimeMS: 30000
});

```

---

## Q15. 💡 Mongoose schemas and models

Schemas define the structure, types, and validation rules for documents, while models are constructors compiled from schemas that provide methods to interact with MongoDB collections.

- **Trade-offs**: Schemas enforce structure and validation at the application level, which prevents bad data, but the catch is they add overhead and can feel restrictive if you need true schema flexibility. Models provide convenient methods like `save()`, `find()`, and `findOne()`, but remember they're just wrappers around MongoDB operations—use them when you need validation and structure.

Example:

```javascript
const userSchema = new mongoose.Schema({
  name: String,
  email: { type: String, required: true, unique: true },
  age: { type: Number, default: 0 }
});
const User = mongoose.model('User', userSchema);
const user = new User({ name: 'John', email: 'john@example.com' });

```

---

## Q16. 💡 Mongoose CRUD operations

Mongoose provides instance methods (`save()`, `remove()`) for document operations and static methods (`create()`, `find()`, `findOne()`, `updateOne()`, `deleteOne()`) for collection operations, all with built-in validation and type casting.

- **Trade-offs**: Mongoose methods are convenient and include validation, but the catch is they add overhead compared to native driver methods. Instance methods work on document instances (after `new Model()` or `findOne()`), while static methods work directly on the model—use instance methods when you need to modify a specific document, static methods for bulk operations.

Example:

```javascript
// Create
const user = await User.create({ name: 'John', email: 'john@example.com' });
// Read
const users = await User.find({ age: { $gte: 18 } });
const user = await User.findOne({ email: 'john@example.com' });
// Update
await User.updateOne({ name: 'John' }, { $set: { age: 31 } });
// Delete
await User.deleteOne({ name: 'John' });

```

---

---

## 📍 Navigation

<div align="center">

[Home: Question List](question.md) • [Indexing & Query Optimization →](2%29%20Indexing%20%26%20Query%20Optimization.md)

[📋 Cheatsheet](MongoDB%20Interview%20Cheatsheet.md]

</div>

---
