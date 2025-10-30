# ⚙️ 2. Indexing & Query Optimization (Q11–20)

---

## 11) What is an index in MongoDB, and how does it improve performance?

Concept:
An index is a data structure that improves query performance by providing fast access to documents based on indexed field values, similar to an index in a book.

Example:
```javascript
// Create index on name field
db.users.createIndex({ name: 1 });

// Query using index
db.users.find({ name: "John" }).explain("executionStats");
```

Deep Insight:
- **B-Tree Structure**: Most indexes use B-trees for logarithmic search time
- **Query Speed**: Reduces full collection scans from O(n) to O(log n)
- **Memory Usage**: Indexes consume RAM for faster access
- **Write Overhead**: Indexes slow down insert/update operations
- **Selectivity**: More selective fields make better indexes

---

## 12) What are the types of indexes available in MongoDB (single field, compound, multikey, text, geo)?

Concept:
MongoDB supports single field, compound, multikey (for arrays), text (for full-text search), geospatial, and specialized indexes like TTL and partial indexes.

Example:
```javascript
// Single field index
db.users.createIndex({ email: 1 });

// Compound index
db.users.createIndex({ name: 1, age: -1 });
```

Deep Insight:
- **Single Field**: Most common, indexes one field
- **Compound**: Multiple fields, order matters for query optimization
- **Multikey**: Automatically created for array fields
- **Text**: Full-text search capabilities
- **Geospatial**: Location-based queries and calculations
- **Specialized**: TTL, partial, sparse indexes for specific use cases

---

## 13) What is a **compound index**, and how does the field order affect query optimization?

Concept:
A compound index is an index on multiple fields where field order matters for query performance - queries must use the leftmost fields to benefit from the index.

Example:
```javascript
// Create compound index
db.users.createIndex({ name: 1, age: -1, city: 1 });

// These queries can use the index
db.users.find({ name: "John" });
db.users.find({ name: "John", age: { $gte: 25 } });
```

Deep Insight:
- **Leftmost Prefix Rule**: Queries must include leftmost fields to use compound index
- **Field Order**: Most selective fields should come first
- **Query Patterns**: Design indexes based on actual query patterns
- **Index Intersection**: MongoDB can use multiple indexes for complex queries
- **Memory Usage**: Compound indexes use more memory than single field indexes

---

## 14) What is a **multikey index**, and when is it automatically created?

Concept:
A multikey index is automatically created when indexing an array field, creating separate index entries for each array element to enable efficient array queries.

Example:
```javascript
// Document with array field
{
  _id: ObjectId("..."),
  name: "John",
  hobbies: ["reading", "gaming", "cooking"]
}
```

Deep Insight:
- **Automatic Creation**: Created automatically when indexing array fields
- **Array Elements**: Each array element gets separate index entry
- **Query Support**: Enables efficient queries on array contents
- **Performance**: Can be slower than single-value indexes
- **Limitations**: Cannot create compound index with multiple array fields

---

## 15) What is a **covered query**, and how can you identify one using `explain()`?

Concept:
A covered query is one where all requested fields are included in the index, eliminating the need to examine documents, identified by "indexOnly: true" in explain output.

Example:
```javascript
// Create compound index
db.users.createIndex({ name: 1, age: 1, email: 1 });

// Covered query - only uses index
db.users.find(
  { name: "John", age: { $gte: 25 } },
```

Deep Insight:
- **Index Only**: Query results come entirely from index, not documents
- **Performance**: Fastest possible query execution
- **Memory Efficient**: No need to load documents into memory
- **Field Selection**: Only indexed fields can be returned
- **ID Field**: Must exclude _id field or include it in index

---

## 16) What is the difference between **ascending** and **descending** indexes?

Concept:
Ascending indexes (1) sort values from lowest to highest, while descending indexes (-1) sort from highest to lowest, affecting query performance and sort operations.

Example:
```javascript
// Ascending index
db.users.createIndex({ age: 1 });

// Descending index
db.users.createIndex({ age: -1 });

```

Deep Insight:
- **Sort Direction**: 1 for ascending, -1 for descending
- **Query Performance**: Matching sort direction uses index efficiently
- **Mixed Sorts**: Compound indexes can handle mixed sort directions
- **Memory Usage**: Both types use similar memory
- **Query Planner**: MongoDB chooses optimal index direction automatically

---

## 17) What is an **index intersection**, and how does MongoDB use multiple indexes for a query?

Concept:
Index intersection occurs when MongoDB uses multiple indexes to satisfy a query, combining results from different indexes to improve performance for complex queries.

Example:
```javascript
// Create separate indexes
db.users.createIndex({ name: 1 });
db.users.createIndex({ age: 1 });
db.users.createIndex({ city: 1 });

// Query that can use index intersection
```

Deep Insight:
- **Multiple Indexes**: MongoDB can use multiple indexes for single query
- **Set Intersection**: Combines results from different indexes
- **Performance**: Can be faster than single compound index for some queries
- **Memory Usage**: Requires more memory to maintain multiple indexes
- **Query Planner**: Automatically chooses best index combination

---

## 18) What is a **TTL (Time-To-Live)** index, and when should you use it?

Concept:
A TTL index automatically removes documents after a specified time period, useful for session data, logs, temporary data, and cache expiration.

Example:
```javascript
// Create TTL index (expires after 1 hour)
db.sessions.createIndex(
  { createdAt: 1 },
  { expireAfterSeconds: 3600 }
);

```

Deep Insight:
- **Automatic Cleanup**: Documents are removed by background process
- **Time Field**: Must be Date or BSON Date type
- **Background Process**: Runs every 60 seconds
- **Use Cases**: Sessions, logs, temporary data, cache expiration
- **Performance**: Minimal impact on write performance

---

## 19) What is the purpose of the `$hint` operator, and when should you use it for optimization?

Concept:
The `$hint` operator forces MongoDB to use a specific index, useful when the query planner chooses a suboptimal index or for testing different index strategies.

Example:
```javascript
// Force use of specific index
db.users.find({ name: "John", age: 25 })
  .hint({ name: 1, age: 1 });

// Force collection scan (no index)
db.users.find({ name: "John" })
```

Deep Insight:
- **Index Selection**: Forces specific index usage
- **Testing**: Useful for comparing different index strategies
- **Query Planner**: Overrides automatic index selection
- **Performance**: Can improve or degrade performance
- **Best Practice**: Use sparingly, prefer proper index design

---

## 20) How do you use the **`explain()` method** to analyze query performance and execution plans?

Concept:
The `explain()` method shows query execution statistics, index usage, and performance metrics to help identify bottlenecks and optimize query performance.

Example:
```javascript
// Basic explain
db.users.find({ name: "John" }).explain();

// Detailed execution stats
db.users.find({ name: "John" }).explain("executionStats");

```

Deep Insight:
- **Execution Stats**: Shows actual performance metrics
- **Index Usage**: Identifies which indexes are used
- **Document Examination**: Shows how many documents were examined
- **Query Stages**: Breaks down query execution into stages
- **Optimization**: Helps identify performance bottlenecks and optimization opportunities

---
