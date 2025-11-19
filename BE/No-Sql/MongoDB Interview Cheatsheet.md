# 🍃 MongoDB Interview Cheatsheet

> **⏱️ Review Time: 15-20 minutes** | **Priority: ⭐⭐⭐ High** | Essential MongoDB concepts for interviews
> 
> **Coverage: Q1-Q40** (40 questions across 4 topics)

**Quick Review Checklist:**
- [ ] MongoDB Fundamentals (Documents, Collections, BSON, CRUD)
- [ ] Indexing & Query Optimization (Single, Compound, Multikey, Text, Geospatial)
- [ ] Aggregation Framework (Pipeline Stages, $match, $group, $lookup)
- [ ] Data Modeling (Embedding vs Referencing, Sharding, Replication)

---

## 📋 **Question Coverage**

- **Q1-Q10**: MongoDB Fundamentals
- **Q11-Q20**: Indexing & Query Optimization
- **Q21-Q30**: Aggregation Framework
- **Q31-Q40**: Data Modeling & Schema Design

---

## 📋 **MongoDB Basics**

| Concept | Description | Example |
|---------|-------------|---------|
| **Document** | Basic unit of data storage | `{ name: "John", age: 30 }` |
| **Collection** | Group of documents | `db.users` |
| **Database** | Container for collections | `use myapp` |
| **BSON** | Binary JSON format | `{ _id: ObjectId("...") }` |

---

## 🔧 **CRUD Operations**

### **Create**
```javascript
// Insert single document
db.users.insertOne({ name: "John", age: 30 });

// Insert multiple documents
db.users.insertMany([
  { name: "Alice", age: 25 },
  { name: "Bob", age: 35 }
]);
```

### **Read**
```javascript
// Find single document
db.users.findOne({ name: "John" });

// Find multiple documents
db.users.find({ age: { $gte: 25 } });

// Find with projection
db.users.find({}, { name: 1, age: 1, _id: 0 });
```

### **Update**
```javascript
// Update single document
db.users.updateOne(
  { name: "John" },
  { $set: { age: 31 } }
);

// Update multiple documents
db.users.updateMany(
  { age: { $lt: 18 } },
  { $set: { status: "minor" } }
);
```

### **Delete**
```javascript
// Delete single document
db.users.deleteOne({ name: "John" });

// Delete multiple documents
db.users.deleteMany({ age: { $lt: 18 } });
```

---

## 🔍 **Query Operators**

| Operator | Description | Example |
|----------|-------------|---------|
| **$eq** | Equal | `{ age: { $eq: 30 } }` |
| **$ne** | Not equal | `{ age: { $ne: 30 } }` |
| **$gt** | Greater than | `{ age: { $gt: 25 } }` |
| **$gte** | Greater than or equal | `{ age: { $gte: 25 } }` |
| **$lt** | Less than | `{ age: { $lt: 50 } }` |
| **$lte** | Less than or equal | `{ age: { $lte: 50 } }` |
| **$in** | In array | `{ age: { $in: [25, 30, 35] } }` |
| **$nin** | Not in array | `{ age: { $nin: [25, 30, 35] } }` |
| **$exists** | Field exists | `{ email: { $exists: true } }` |
| **$regex** | Regular expression | `{ name: { $regex: /^J/ } }` |

---

## 📊 **Aggregation Pipeline**

### **Common Stages**
```javascript
db.orders.aggregate([
  { $match: { status: "completed" } },    // Filter
  { $group: { _id: "$customerId", total: { $sum: "$amount" } } }, // Group
  { $sort: { total: -1 } },               // Sort
  { $limit: 10 },                         // Limit
  { $project: { customerId: "$_id", total: 1 } } // Project
]);
```

### **Key Operators**
| Operator | Description | Example |
|----------|-------------|---------|
| **$sum** | Sum values | `{ $sum: "$amount" }` |
| **$avg** | Average values | `{ $avg: "$price" }` |
| **$min** | Minimum value | `{ $min: "$age" }` |
| **$max** | Maximum value | `{ $max: "$age" }` |
| **$count** | Count documents | `{ $count: "total" }` |
| **$push** | Add to array | `{ $push: "$name" }` |
| **$addToSet** | Add unique to array | `{ $addToSet: "$category" }` |

---

## 🗂️ **Indexing**

### **Index Types**
```javascript
// Single field index
db.users.createIndex({ email: 1 });

// Compound index
db.users.createIndex({ name: 1, age: -1 });

// Text index
db.articles.createIndex({ title: "text", content: "text" });

// Geospatial index
db.locations.createIndex({ location: "2dsphere" });

// TTL index
db.sessions.createIndex({ createdAt: 1 }, { expireAfterSeconds: 3600 });
```

### **Index Properties**
| Property | Description | Example |
|----------|-------------|---------|
| **1** | Ascending | `{ name: 1 }` |
| **-1** | Descending | `{ age: -1 }` |
| **"text"** | Text search | `{ title: "text" }` |
| **"2dsphere"** | Geospatial | `{ location: "2dsphere" }` |

---

## 🏗️ **Schema Design Patterns**

### **Embedding vs Referencing**
```javascript
// Embedded (denormalized)
{
  _id: ObjectId("..."),
  name: "John",
  address: {
    street: "123 Main St",
    city: "NYC"
  }
}

// Referenced (normalized)
{
  _id: ObjectId("..."),
  name: "John",
  addressId: ObjectId("...")
}
```

### **One-to-Many Relationships**
```javascript
// Small arrays: Embed
{
  _id: ObjectId("..."),
  name: "John",
  orders: [
    { orderId: "ORD001", amount: 99.99 },
    { orderId: "ORD002", amount: 149.99 }
  ]
}

// Large arrays: Reference
{
  _id: ObjectId("..."),
  name: "John",
  orderIds: [ObjectId("..."), ObjectId("...")]
}
```

---

## 🔧 **Performance Optimization**

### **Query Optimization**
```javascript
// Use indexes
db.users.find({ email: "john@example.com" });

// Use projection
db.users.find({}, { name: 1, email: 1, _id: 0 });

// Use limit
db.users.find().limit(100);

// Use explain()
db.users.find({ email: "john@example.com" }).explain("executionStats");
```

### **Index Optimization**
```javascript
// Create compound indexes
db.orders.createIndex({ customerId: 1, createdAt: -1 });

// Use covered queries
db.orders.find(
  { customerId: "CUST001" },
  { orderId: 1, amount: 1, _id: 0 }
);

// Monitor index usage
db.orders.getIndexes();
```

---

## 📈 **Aggregation Examples**

### **Sales Analysis**
```javascript
db.orders.aggregate([
  { $match: { status: "completed" } },
  { $group: {
    _id: { $dateToString: { format: "%Y-%m", date: "$createdAt" } },
    totalSales: { $sum: "$amount" },
    orderCount: { $sum: 1 }
  }},
  { $sort: { _id: 1 } }
]);
```

### **Top Customers**
```javascript
db.orders.aggregate([
  { $group: {
    _id: "$customerId",
    totalSpent: { $sum: "$amount" },
    orderCount: { $sum: 1 }
  }},
  { $sort: { totalSpent: -1 } },
  { $limit: 10 }
]);
```

---

## 🔐 **Replication & Sharding**

### **Replica Set**
```javascript
// Write concern
db.orders.insertOne(
  { orderId: "ORD001" },
  { writeConcern: { w: "majority", j: true } }
);

// Read preference
db.orders.find().readPref("secondary");
```

### **Sharding**
```javascript
// Enable sharding
sh.enableSharding("myapp");

// Shard collection
sh.shardCollection("myapp.orders", { customerId: 1, createdAt: 1 });
```

---

## 🛠️ **Common Commands**

### **Database Operations**
```javascript
// Show databases
show dbs

// Use database
use myapp

// Show collections
show collections

// Drop database
db.dropDatabase()
```

### **Collection Operations**
```javascript
// Create collection
db.createCollection("users");

// Drop collection
db.users.drop();

// Rename collection
db.users.renameCollection("customers");
```

### **Index Operations**
```javascript
// List indexes
db.users.getIndexes();

// Drop index
db.users.dropIndex({ email: 1 });

// Rebuild indexes
db.users.reIndex();
```

---

## 📊 **Monitoring & Debugging**

### **Explain Plans**
```javascript
// Basic explain
db.users.find({ name: "John" }).explain();

// Execution stats
db.users.find({ name: "John" }).explain("executionStats");

// All plans
db.users.find({ name: "John" }).explain("allPlansExecution");
```

### **Performance Metrics**
```javascript
// Server status
db.serverStatus();

// Collection stats
db.users.stats();

// Index usage
db.users.aggregate([{ $indexStats: {} }]);
```

---

## 🎯 **Interview Tips**

### **Common Questions**
1. **MongoDB vs SQL** - Document vs relational model
2. **Indexing Strategy** - Single field, compound, multikey indexes
3. **Schema Design** - Embedding vs referencing
4. **Aggregation Pipeline** - Stages and operators
5. **Performance Optimization** - Query analysis and indexing

### **Key Concepts**
- **Document Model**: Flexible schema, BSON format
- **Indexing**: B-tree indexes, compound indexes, covered queries
- **Aggregation**: Pipeline stages, operators, optimization
- **Sharding**: Horizontal scaling, shard keys
- **Replication**: High availability, write/read concerns

### **Best Practices**
- Design schemas based on query patterns
- Use proper indexing strategies
- Optimize aggregation pipelines
- Monitor performance metrics
- Plan for scalability and growth

---

*Remember: Practice with real data, understand your use cases, and always consider performance implications!*
