# 🍃 MongoDB Interview Cheatsheet

> **⏱️ Review Time: 15-20 minutes** | **Priority: ⭐⭐⭐ High** | Essential MongoDB concepts for interviews
> 
> **Coverage: Q1-Q57** (57 questions across 4 topics + Mongoose + Connection Pooling)

**Quick Review Checklist:**
- [ ] MongoDB Fundamentals (Documents, Collections, BSON, CRUD)
- [ ] Indexing & Query Optimization (Single, Compound, Multikey, Text, Geospatial)
- [ ] Aggregation Framework (Pipeline Stages, $match, $group, $lookup)
- [ ] Data Modeling (Embedding vs Referencing, Sharding, Replication)
- [ ] Mongoose ODM (Schemas, Models, Validation, Middleware, Population)

---

## 📋 **Question Coverage**

- **Q1-Q16**: MongoDB Fundamentals (includes Q12-16 Mongoose Basics & Connection Pooling)
- **Q17-Q29**: Indexing & Query Optimization (includes Q27-29 Mongoose Indexing)
- **Q30-Q41**: Aggregation Framework (includes Q40-41 Mongoose Aggregation)
- **Q42-Q57**: Data Modeling & Schema Design (includes Q52-57 Mongoose Schema Design)

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

## 🔎 **Text Search Queries**

### **Text Index & Search**
```javascript
// Create text index
db.articles.createIndex({ title: "text", content: "text" });

// Basic text search
db.articles.find({ $text: { $search: "mongodb tutorial" } });

// Text search with language
db.articles.find({ 
  $text: { 
    $search: "mongodb tutorial",
    $language: "en"
  } 
});

// Text search with score
db.articles.find(
  { $text: { $search: "mongodb" } },
  { score: { $meta: "textScore" } }
).sort({ score: { $meta: "textScore" } });

// Text search with case sensitivity (using regex)
db.articles.find({ title: { $regex: /MongoDB/i } });
```

### **Text Search Operators**
| Operator | Description | Example |
|----------|-------------|---------|
| **$text** | Full-text search | `{ $text: { $search: "mongodb" } }` |
| **$regex** | Pattern matching | `{ name: { $regex: /^J/i } }` |
| **$meta: "textScore"** | Relevance score | `{ score: { $meta: "textScore" } }` |

---

## 📄 **Pagination**

### **Offset-Based Pagination**
```javascript
// Basic pagination
const page = 2;
const limit = 10;
const skip = (page - 1) * limit;

db.products.find({ category: "electronics" })
  .sort({ createdAt: -1 })
  .skip(skip)
  .limit(limit);

// With aggregation
db.products.aggregate([
  { $match: { category: "electronics" } },
  { $sort: { createdAt: -1 } },
  { $skip: 20 },
  { $limit: 10 }
]);
```

### **Cursor-Based Pagination (Better Performance)**
```javascript
// Cursor-based pagination
const lastId = ObjectId("...");
const limit = 10;

db.products.find({ 
  _id: { $gt: lastId },
  category: "electronics"
})
.sort({ _id: 1 })
.limit(limit);

// Date-based cursor
const lastCreatedAt = new Date("2023-12-01");
db.products.find({
  category: "electronics",
  createdAt: { $lt: lastCreatedAt }
})
.sort({ createdAt: -1 })
.limit(10);
```

### **Pagination with Aggregation**
```javascript
db.products.aggregate([
  { $match: { category: "electronics" } },
  { $sort: { createdAt: -1 } },
  { $facet: {
    metadata: [{ $count: "total" }],
    data: [{ $skip: 20 }, { $limit: 10 }]
  }}
]);
```

---

## ⚡ **Optimization Techniques**

### **Query Optimization**
```javascript
// 1. Use indexes for filtered queries
db.users.find({ email: "john@example.com" }); // Requires index on email

// 2. Use projection to limit fields
db.users.find({}, { name: 1, email: 1, _id: 0 });

// 3. Use limit to reduce result size
db.users.find().limit(100);

// 4. Use covered queries (all fields in index)
db.users.find(
  { name: "John", age: { $gte: 25 } },
  { name: 1, age: 1, email: 1, _id: 0 }
); // Requires index: { name: 1, age: 1, email: 1 }

// 5. Use hint to force specific index
db.users.find({ name: "John" }).hint({ name: 1, age: -1 });

// 6. Use lean() in Mongoose for faster queries
const users = await User.find().lean();
```

### **Index Optimization**
```javascript
// 1. Create compound indexes for common query patterns
db.orders.createIndex({ customerId: 1, createdAt: -1 });

// 2. Use sparse indexes for optional fields
db.users.createIndex({ email: 1 }, { sparse: true });

// 3. Use partial indexes for filtered queries
db.orders.createIndex(
  { customerId: 1 },
  { partialFilterExpression: { status: "active" } }
);

// 4. Monitor index usage
db.orders.aggregate([{ $indexStats: {} }]);

// 5. Remove unused indexes
db.users.dropIndex({ unusedField: 1 });
```

### **Aggregation Optimization**
```javascript
// 1. Use $match early to reduce documents
db.orders.aggregate([
  { $match: { status: "completed", date: { $gte: startDate } } },
  { $group: { _id: "$customerId", total: { $sum: "$amount" } } }
]);

// 2. Use $project to limit fields early
db.orders.aggregate([
  { $match: { status: "completed" } },
  { $project: { customerId: 1, amount: 1 } },
  { $group: { _id: "$customerId", total: { $sum: "$amount" } } }
]);

// 3. Use allowDiskUse for large sorts
db.orders.aggregate([
  { $sort: { createdAt: -1 } }
], { allowDiskUse: true });

// 4. Use indexes on $match stages
db.orders.createIndex({ status: 1, date: 1 });
```

### **Write Optimization**
```javascript
// 1. Use bulk operations
db.products.insertMany([...], { ordered: false });

// 2. Use update operators instead of replacing
db.users.updateOne(
  { name: "John" },
  { $set: { age: 31 } } // Not: { name: "John", age: 31 }
);

// 3. Use write concern for performance
db.orders.insertOne(
  { orderId: "ORD001" },
  { writeConcern: { w: 1 } } // Faster, less durable
);
```

### **Connection & Pooling Optimization**
```javascript
// 1. Configure connection pool size
mongoose.connect('mongodb://localhost:27017/myapp', {
  maxPoolSize: 10,
  minPoolSize: 2,
  maxIdleTimeMS: 30000
});

// 2. Use read preferences for read scaling
db.orders.find().readPref("secondary");

// 3. Use connection string options
mongodb://host:27017/db?maxPoolSize=10&minPoolSize=2
```

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

---

## 🍃 **Mongoose ODM**

### **Connection & Setup**
```javascript
const mongoose = require('mongoose');
mongoose.connect('mongodb://localhost:27017/myapp', {
  useNewUrlParser: true,
  useUnifiedTopology: true
});
```

### **Connection Pooling**
```javascript
// Mongoose with pool options
mongoose.connect('mongodb://localhost:27017/myapp', {
  maxPoolSize: 10,        // Maximum connections
  minPoolSize: 2,         // Minimum connections
  maxIdleTimeMS: 30000    // Close idle after 30s
});

// Native driver with pool options
const { MongoClient } = require('mongodb');
const client = new MongoClient('mongodb://localhost:27017', {
  maxPoolSize: 10,
  minPoolSize: 2,
  maxIdleTimeMS: 30000
});
```

### **Schemas & Models**
```javascript
const userSchema = new mongoose.Schema({
  name: { type: String, required: true },
  email: { type: String, required: true, unique: true },
  age: { type: Number, min: 0, default: 0 }
}, {
  timestamps: true
});
const User = mongoose.model('User', userSchema);
```

### **CRUD Operations**
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

### **Indexes in Mongoose**
```javascript
userSchema.index({ email: 1, name: 1 }); // Compound index
userSchema.index({ email: 'text' }); // Text index
```

### **Query Methods**
```javascript
const users = await User.find({ age: { $gte: 18 } })
  .select('name email')
  .sort({ age: -1 })
  .limit(10)
  .lean(); // Returns plain objects
```

### **Validation**
```javascript
const userSchema = new mongoose.Schema({
  email: { 
    type: String, 
    required: true,
    match: /^[\w.%+-]+@[\w.-]+\.[A-Za-z]{2,}$/
  },
  age: { type: Number, min: 0, max: 120 },
  role: { type: String, enum: ['user', 'admin'] }
});
```

### **Virtuals**
```javascript
userSchema.virtual('fullName').get(function() {
  return `${this.firstName} ${this.lastName}`;
});
userSchema.set('toJSON', { virtuals: true });
```

### **Methods**
```javascript
// Instance method
userSchema.methods.getAge = function() {
  return new Date().getFullYear() - this.birthYear;
};
// Static method
userSchema.statics.findByEmail = function(email) {
  return this.findOne({ email: email.toLowerCase() });
};
```

### **Middleware (Hooks)**
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

### **Population**
```javascript
const orderSchema = new mongoose.Schema({
  customerId: { type: mongoose.Schema.Types.ObjectId, ref: 'User' }
});
const order = await Order.findOne().populate('customerId');
```

### **Aggregation**
```javascript
const results = await User.aggregate([
  { $match: { age: { $gte: 18 } } },
  { $group: { _id: '$department', count: { $sum: 1 } } }
]);
```

---

*Remember: Practice with real data, understand your use cases, and always consider performance implications!*
