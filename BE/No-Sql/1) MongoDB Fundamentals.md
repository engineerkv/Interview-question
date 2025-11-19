# 1. MongoDB Fundamentals (Q1–10)

---

## Q1. What is MongoDB, and what type of NoSQL database is it?

MongoDB is a document-oriented NoSQL database that stores flexible BSON documents instead of rigid rows, so each record can evolve without schema migrations.

- **Trade-offs**: Handles nested JSON-like structures easily, but lack of rigid schemas means you must enforce consistency yourself. Avoid using it when you need strict relational constraints or cross-document transactions.

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

## Q2. What are the key differences between MongoDB and relational databases like MySQL?

MongoDB stores JSON-like documents inside collections, scales horizontally through sharding, and uses MQL (query documents) instead of SQL joins and rigid schemas.

- **Trade-offs**: Gains agility and scaling by relaxing schema and relationships, but you lose automatic foreign keys, multi-table transactions by default, and well-known SQL tooling.

Example:

```javascript
db.users.insertOne({
  name: "John",
  age: 30,
  address: { city: "NYC", country: "USA" }
});
```

---

## Q3. What are documents and collections in MongoDB?

Documents are BSON objects (equivalent to rows) and collections are logical groupings of documents (equivalent to tables) with no enforced schema, so structures can differ per document.

- **Trade-offs**: Flexibility makes evolving models easy, but inconsistent shapes complicate analytics and validation—use schema validation when you need guardrails.

Example:

```javascript
db.users.insertMany([
  { name: "Alice", email: "alice@example.com" },
  { name: "Bob", phone: "123-456-7890", address: { city: "LA" } }
]);
```

---

## Q4. What is BSON, and how is it different from JSON?

BSON is MongoDB’s binary JSON that adds data types such as ObjectId, Date, Decimal128, enabling faster parsing and richer data than plain JSON strings.

- **Trade-offs**: Extended types and binary encoding improve storage and speed, but payloads are slightly larger and require MongoDB drivers to interpret them.

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

## Q5. What is a schema-less database, and what are its advantages and drawbacks?

Schema-less stores don’t force predefined columns, so you can insert documents with new fields anytime, accelerating prototyping and heterogenous data ingestion.

- **Trade-offs**: Flexibility speeds delivery but you must actively prevent inconsistency, enforce validation rules, and design queries carefully to avoid performance surprises.

Example:

```javascript
db.products.insertMany([
  { name: "Laptop", price: 999.99, specs: { ram: "16GB" } },
  { name: "Book", price: 19.99, author: "John Smith" }
]);
```

---

## Q6. What are the differences between embedded and referenced data models in MongoDB?

Embedded (denormalized) documents store related data inside a single document for fast reads, while referenced (normalized) models link to other documents via ObjectIds.

- **Trade-offs**: Embed when the relationship is tight and read-heavy; reference when subdocuments grow independently, need reuse, or would bloat parent documents.

Example:

```javascript
// Embedded
{ name: "John", address: { street: "123 Main", city: "NYC" } }

// Referenced
{ name: "John", addressId: ObjectId("...") }
```

---

## Q7. What are CRUD operations in MongoDB?

CRUD maps to insertOne/insertMany for create, find/findOne for read, updateOne/updateMany for update, and deleteOne/deleteMany for delete—all using JSON-like filters.

- **Trade-offs**: Single-document operations are atomic, but multi-document writes aren’t (unless you use transactions), so model data to keep critical updates within one doc.

Example:

```javascript
db.users.insertOne({ name: "John", age: 30 });
db.users.find({ age: { $gt: 25 } });
db.users.updateOne({ name: "John" }, { $set: { age: 31 } });
db.users.deleteOne({ name: "John" });
```

---

## Q8. How does MongoDB ensure data consistency without a strict schema?

Consistency comes from application-side validation, built-in JSON schema validators, and disciplined data modeling—MongoDB enforces whatever rules you configure.

- **Trade-offs**: Gives teams control over rules per collection, but missing validators or sloppy modeling quickly lead to messy data; always pair validation with indexes.

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

## Q9. What are capped collections, and when would you use them?

Capped collections are fixed-size, circular buffers that overwrite the oldest documents when reaching their byte or count limit—perfect for logs and real-time feeds.

- **Trade-offs**: Writes are blazing fast and storage bounded, but you can’t remove individual docs or grow past the cap—use them only when FIFO behavior is acceptable.

Example:

```javascript
db.createCollection("logs", {
  capped: true,
  size: 1_000_000,
  max: 1000
});
```

---

## Q10. What is the difference between `findOne()`, `find()`, and aggregation queries?

`findOne()` fetches a single document, `find()` returns a cursor you can iterate, and aggregation pipelines run staged transformations like match, group, and project.

- **Trade-offs**: Use findOne for keyed lookups, find for filtered lists with sorting/limits, and aggregation for analytics or joins—remember aggregations can be heavier without indexes.

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
