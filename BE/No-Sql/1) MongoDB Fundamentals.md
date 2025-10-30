# 🍃 1. MongoDB Fundamentals (Q1–10)

---

## 1) What is MongoDB, and what type of NoSQL database is it?

Concept:
MongoDB is a document-oriented NoSQL database that stores data in flexible, JSON-like documents with dynamic schemas, classified as a document database.

Example:
```javascript
// MongoDB document example
{
  _id: ObjectId("507f1f77bcf86cd799439011"),
  name: "John Doe",
  age: 30,
  email: "john@example.com",
  address: { city: "NYC", country: "USA" }
}
```

Deep Insight:
- **Document Database**: Stores data as BSON documents instead of tables and rows
- **Schema Flexibility**: No fixed schema required, documents can have different structures
- **JSON-like**: Uses BSON (Binary JSON) for efficient storage and querying
- **Horizontal Scaling**: Designed for distributed systems and sharding
- **Rich Queries**: Supports complex queries, indexing, and aggregation

---

## 2) What are the key differences between MongoDB and relational databases like MySQL?

Concept:
MongoDB uses collections and documents instead of tables and rows, has dynamic schemas, supports horizontal scaling, and uses BSON instead of SQL for queries.

Example:
```javascript
// MongoDB (NoSQL)
db.users.insertOne({
  name: "John",
  age: 30,
  address: { city: "NYC", country: "USA" }
});
```

Deep Insight:
- **Data Model**: Collections vs Tables, Documents vs Rows
- **Schema**: Dynamic vs Fixed schema requirements
- **Query Language**: MongoDB Query Language vs SQL
- **Scaling**: Horizontal vs Vertical scaling approach
- **ACID Properties**: Eventual consistency vs Strong consistency

---

## 3) What are documents and collections in MongoDB?

Concept:
Documents are the basic unit of data storage (similar to rows in SQL), while collections are groups of documents (similar to tables in SQL) that don't require a fixed schema.

Example:
```javascript
// Collection: users
// Document 1
{
  _id: ObjectId("507f1f77bcf86cd799439011"),
  name: "Alice",
  email: "alice@example.com",
  age: 25
}

// Document 2 (different structure)
{
  _id: ObjectId("507f1f77bcf86cd799439012"),
  name: "Bob",
  phone: "123-456-7890",
  address: { city: "LA", state: "CA" }
}
```

Deep Insight:
- **Documents**: BSON objects containing field-value pairs
- **Collections**: Logical grouping of documents, similar to SQL tables
- **Schema Flexibility**: Documents in same collection can have different structures
- **Unique IDs**: Each document has a unique `_id` field
- **Nested Data**: Documents can contain arrays and embedded documents

---

## 4) What is BSON, and how is it different from JSON?

Concept:
BSON (Binary JSON) is a binary-encoded serialization format used by MongoDB that extends JSON with additional data types like Date, ObjectId, and Binary data for better performance and storage efficiency.

Example:
```javascript
// JSON
{
  "name": "John",
  "age": 30,
  "date": "2023-12-01T10:30:00Z"
}

// BSON (MongoDB)
{
  name: "John",
  age: 30,
  date: new Date("2023-12-01T10:30:00Z"),
  _id: ObjectId("507f1f77bcf86cd799439011")
}
```

Deep Insight:
- **Binary Format**: More efficient than JSON for storage and parsing
- **Extended Types**: Supports Date, ObjectId, Binary, Decimal128, etc.
- **Performance**: Faster serialization/deserialization than JSON
- **Size**: Generally larger than JSON due to type information
- **MongoDB Native**: Optimized for MongoDB's internal operations

---

## 5) What is a schema-less database, and what are its advantages and drawbacks?

Concept:
A schema-less database doesn't require a predefined structure, allowing flexible data storage but potentially leading to data inconsistency and performance issues without proper design.

Example:
```javascript
// Same collection, different document structures
db.products.insertMany([
  {
    name: "Laptop",
    price: 999.99,
    specs: { ram: "16GB", storage: "512GB" }
  },
  {
    name: "Book",
    price: 19.99,
    author: "John Smith",
    pages: 300
  }
]);
```

Deep Insight:
- **Flexibility**: Easy to add new fields without schema changes
- **Rapid Development**: Faster iteration and prototyping
- **Data Variety**: Can store different data types in same collection
- **Consistency Risk**: No built-in data validation or constraints
- **Performance Impact**: Poor design can lead to inefficient queries

---

## 6) What are the differences between embedded (denormalized) and referenced (normalized) data models in MongoDB?

Concept:
Embedded models store related data within the same document for faster reads, while referenced models store references to other documents for better data consistency and smaller document sizes.

Example:
```javascript
// Embedded (Denormalized)
{
  _id: ObjectId("..."),
  name: "John",
  address: {
    street: "123 Main St",
    city: "NYC",
    country: "USA"
  }
}

// Referenced (Normalized)
{
  _id: ObjectId("..."),
  name: "John",
  addressId: ObjectId("...")
}
```

Deep Insight:
- **Embedded**: Faster reads, atomic updates, but larger documents
- **Referenced**: Smaller documents, better consistency, but requires joins
- **Use Cases**: Embed for small, frequently accessed data; reference for large, independent data
- **Query Complexity**: Referenced models require multiple queries or $lookup
- **Update Frequency**: Consider how often related data changes

---

## 7) What are CRUD operations in MongoDB?

Concept:
CRUD operations are Create (insert), Read (find), Update (updateOne/updateMany), and Delete (deleteOne/deleteMany) operations that form the basic data manipulation interface in MongoDB.

Example:
```javascript
// Create
db.users.insertOne({ name: "John", age: 30 });
db.users.insertMany([{ name: "Alice" }, { name: "Bob" }]);

// Read
db.users.findOne({ name: "John" });
db.users.find({ age: { $gt: 25 } });

// Update
db.users.updateOne({ name: "John" }, { $set: { age: 31 } });

// Delete
db.users.deleteOne({ name: "John" });
```

Deep Insight:
- **Create**: insertOne() for single, insertMany() for multiple documents
- **Read**: findOne() for single, find() for multiple documents with filtering
- **Update**: updateOne() for single, updateMany() for multiple with $set, $inc operators
- **Delete**: deleteOne() for single, deleteMany() for multiple documents
- **Atomicity**: Single document operations are atomic, multi-document operations are not

---

## 8) How does MongoDB ensure data consistency without a strict schema?

Concept:
MongoDB ensures consistency through application-level validation, schema validation rules, data modeling best practices, and proper indexing strategies rather than database-level constraints.

Example:
```javascript
// Schema validation
db.createCollection("users", {
  validator: {
    $jsonSchema: {
      bsonType: "object",
      required: ["name", "email"],
      properties: {
        name: { bsonType: "string" },
        email: { bsonType: "string", pattern: "^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\\.[a-zA-Z]{2,}$" }
      }
    }
  }
});
```

Deep Insight:
- **Application Validation**: Client-side validation before database operations
- **Schema Validation**: JSON Schema rules at collection level
- **Data Modeling**: Consistent patterns and naming conventions
- **Indexing**: Proper indexes for data integrity and performance
- **Best Practices**: Code reviews, testing, and documentation

---

## 9) What are capped collections, and when would you use them?

Concept:
Capped collections are fixed-size collections that automatically remove oldest documents when the size limit is reached, useful for logging, caching, and real-time data streams.

Example:
```javascript
// Create capped collection
db.createCollection("logs", {
  capped: true,
  size: 1000000,  // 1MB
  max: 1000       // Max 1000 documents
});
```

Deep Insight:
- **Fixed Size**: Predefined maximum size in bytes or document count
- **FIFO Behavior**: Oldest documents are automatically removed
- **No Deletes**: Cannot delete individual documents from capped collections
- **Use Cases**: Logging, real-time data, caching, temporary data
- **Performance**: Faster writes due to pre-allocated space

---

## 10) What is the difference between `findOne()`, `find()`, and aggregation queries in MongoDB?

Concept:
`findOne()` returns a single document, `find()` returns a cursor for multiple documents, and aggregation queries use a pipeline for complex data processing and transformations.

Example:
```javascript
// findOne() - returns single document or null
const user = db.users.findOne({ name: "John" });

// find() - returns cursor for multiple documents
const users = db.users.find({ age: { $gte: 25 } });

// Aggregation - complex data processing
db.users.aggregate([
  { $match: { age: { $gte: 25 } } },
  { $group: { _id: "$department", count: { $sum: 1 } } }
]);
```

Deep Insight:
- **findOne()**: Single document, returns null if not found, good for unique lookups
- **find()**: Cursor for iteration, supports filtering, sorting, limiting
- **Aggregation**: Pipeline-based processing, supports grouping, joining, complex transformations
- **Performance**: findOne() fastest, aggregation most flexible but potentially slower
- **Use Cases**: findOne() for lookups, find() for lists, aggregation for analytics

---
