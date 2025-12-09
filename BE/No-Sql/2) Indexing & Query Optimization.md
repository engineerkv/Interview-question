# ⚡ 2. Indexing & Query Optimization (Q17–29)

---

## 📍 Navigation

<div align="center">

[MongoDB Fundamentals](1%29%20MongoDB%20Fundamentals.md) • [Home: Question List](question.md) • [Aggregation Framework →](3%29%20Aggregation%20Framework.md)

[📋 Cheatsheet](MongoDB%20Interview%20Cheatsheet.md]

</div>

---

---

## Q17. 📇 Indexes in MongoDB and why they're important

An index is a B-tree structure that allows MongoDB to jump directly to matching keys instead of scanning the whole collection, cutting lookups from O(n) scans to O(log n) seeks.

- **Trade-offs**: Indexes speed reads and sorts but consume RAM/disk and slow writes because each insert/update must update the index—only create indexes that match real query patterns.

Example:

```javascript
// Create index on name field
db.users.createIndex({ name: 1 });

// Query using index
db.users.find({ name: "John" }).explain("executionStats");

```

---

## Q18. 📇 Difference between single field and compound indexes

Single-field indexes index one field (e.g., `{email: 1}`), while compound indexes combine multiple fields in one structure (e.g., `{name: 1, age: -1}`) and can satisfy queries on the leftmost prefix.

- **Trade-offs**: Single-field indexes are simple and fast for single-field queries, but compound indexes are more efficient for multi-field queries and sorts. However, compound indexes are larger, slower to maintain, and only help when queries use the leftmost prefix—order matters.

Example:

```javascript
// Single field index
db.users.createIndex({ email: 1 });

// Compound index
db.users.createIndex({ name: 1, age: -1 });

```

---

## Q19. 📇 Multikey indexes and when to use them

Multikey indexes automatically index each element in an array field, allowing queries to match values inside arrays efficiently—MongoDB creates them automatically when you index an array field.

- **Trade-offs**: Multikey indexes are essential for array queries but become larger than scalar indexes and slower to maintain. MongoDB forbids compound indexes with more than one array field, so design carefully when mixing arrays with other fields.

Example:

```javascript
// Document with array field
{
  _id: ObjectId("..."),
  name: "John",
  hobbies: ["reading", "gaming", "cooking"]
}

// Create multikey index (automatic when indexing array)
db.users.createIndex({ hobbies: 1 });

// Query can use multikey index
db.users.find({ hobbies: "gaming" });

```

---

## Q20. 📇 Text indexes and how to create them

Text indexes enable full-text search across string fields, supporting language-specific stemming and stop words—create them with `"text"` type and use `$text` operator for searches.

- **Trade-offs**: Text indexes enable powerful search capabilities but are large, slow to build, and only one text index per collection is allowed. They also ignore case and diacritics by default, which may not match all use cases.

Example:

```javascript
// Create text index on single field
db.articles.createIndex({ title: "text" });

// Create text index on multiple fields
db.articles.createIndex({ title: "text", content: "text" });

// Search using text index
db.articles.find({ $text: { $search: "mongodb tutorial" } });

```

---

## Q21. 📇 Geospatial indexes and how to use them

Geospatial indexes (2dsphere for Earth-like coordinates, 2d for flat planes) enable location-based queries like finding points within a radius or near a location using `$near`, `$geoWithin`, and `$geoIntersects`.

- **Trade-offs**: Geospatial indexes enable powerful location queries but require coordinate data in GeoJSON or legacy coordinate pairs. 2dsphere indexes are more accurate for real-world distances, while 2d is faster for flat surfaces—choose based on your use case.

Example:

```javascript
// Create 2dsphere index
db.places.createIndex({ location: "2dsphere" });

// Document with GeoJSON location
{
  name: "Central Park",
  location: { type: "Point", coordinates: [-73.97, 40.78] }
}

// Find places near a location
db.places.find({
  location: {
    $near: {
      $geometry: { type: "Point", coordinates: [-73.98, 40.77] },
      $maxDistance: 1000  // meters
    }
  }
});

```

---

## Q22. 🔍 Covered query and how to create one

A covered query is satisfied entirely by the index without reading documents—all fields in the filter, sort, and projection must be in the index, and `_id` must be excluded from projection (unless it's in the index).

- **Trade-offs**: Covered queries are the fastest possible reads since they avoid document fetches, but you must design indexes that include all needed fields. This can lead to larger indexes, so balance coverage with index size and write performance.

Example:

```javascript
// Create compound index
db.users.createIndex({ name: 1, age: 1, email: 1 });

// Covered query - only uses index (no document fetch)
db.users.find(
  { name: "John", age: { $gte: 25 } },
  { name: 1, age: 1, email: 1, _id: 0 }
);

// Verify with explain
db.users.find({ name: "John" }, { name: 1, age: 1, _id: 0 })
  .explain("executionStats");  // Check for indexOnly: true

```

---

## Q23. 📇 Difference between ascending and descending indexes

Ascending indexes (1) store keys in ascending order, while descending indexes (-1) store them in reverse—MongoDB can use either direction for equality queries, but sort direction matters for efficient sorting.

- **Trade-offs**: For single-field queries, direction rarely matters, but for compound indexes with sorts, matching index direction to sort order avoids in-memory sorting. Mixed-direction compound indexes (e.g., `{name: 1, age: -1}`) can satisfy both ascending and descending sorts efficiently.

Example:

```javascript
// Ascending index
db.users.createIndex({ age: 1 });
db.users.find().sort({ age: 1 });  // Efficient

// Descending index
db.users.createIndex({ age: -1 });
db.users.find().sort({ age: -1 });  // Efficient

// Compound index with mixed directions
db.users.createIndex({ name: 1, age: -1 });
db.users.find().sort({ name: 1, age: -1 });  // Efficient

```

---

## Q24. 📇 Index intersection and how it works

Index intersection allows MongoDB to combine results from multiple single-field indexes to satisfy a query, avoiding the need for a compound index when queries use different field combinations.

- **Trade-offs**: Intersection can rescue queries when a perfect compound index doesn't exist, but it's usually slower than a dedicated compound index and uses more memory. MongoDB only uses intersection for equality predicates, not ranges or sorts—prefer compound indexes for common query patterns.

Example:

```javascript
// Create separate single-field indexes
db.users.createIndex({ name: 1 });
db.users.createIndex({ age: 1 });

// Query can use index intersection
db.users.find({ name: "John", age: 30 }).explain();
// MongoDB may intersect both indexes

// Better: Create compound index for this pattern
db.users.createIndex({ name: 1, age: 1 });

```

---

## Q25. 📇 TTL indexes and how to use them

TTL (Time-To-Live) indexes automatically delete documents after a specified age by monitoring a Date field—ideal for session tokens, logs, cache entries, or any data that expires naturally.

- **Trade-offs**: Cleanup runs every ~60 seconds and only works on Date fields; don't rely on TTL when you might need data later, because deletions are irreversible. TTL indexes are single-field indexes, so these can't be combined with other fields in compound indexes.

Example:

```javascript
// Create TTL index (expires after 1 hour)
db.sessions.createIndex(
  { createdAt: 1 },
  { expireAfterSeconds: 3600 }
);

// Document will be deleted after 1 hour
{
  _id: ObjectId("..."),
  sessionId: "abc123",
  createdAt: new Date()  // TTL field
}

```

---

## Q26. ⚡ Using `$hint` and `explain()` to optimize queries

`explain()` reveals whether a query used an index or collection scan, how many docs it examined, and which stages (IXSCAN, FETCH, SORT) were executed so you can tune queries. `$hint` forces MongoDB to use a specific index when the query planner might choose a different one, useful when you know a particular index performs better.

- **Trade-offs**: `explain("executionStats")` gives real numbers but actually runs the query, and `allPlansExecution` helps catch unstable plans but is heavier—use carefully on production data. `$hint` can improve performance when the planner picks wrong, but the catch is it bypasses MongoDB's automatic index selection, so you must manually update hints if indexes change—avoid using it unless you've proven the planner is wrong.

Example:

```javascript
// Basic explain
db.users.find({ name: "John" }).explain();

// Detailed execution stats
db.users.find({ name: "John" }).explain("executionStats");

// Force specific index with $hint
db.users.find({ name: "John", age: 30 }).hint({ name: 1, age: 1 });

// Check which index was used
db.users.find({ name: "John" }).hint({ name: 1 }).explain("executionStats");

```

---

## Q27. 📇 Creating indexes in Mongoose schemas

Mongoose allows you to define indexes directly in schema definitions using the `index` option or `schema.index()`, and automatically creates them when the model is first used.

- **Trade-offs**: Schema-level indexes are declarative and easy to maintain, but the catch is these are created on every application startup which can slow initial connections. Use `autoIndex: false` in production to disable automatic index creation, and create indexes manually or via migrations—always monitor index creation time on large collections.

Example:

```javascript
const userSchema = new mongoose.Schema({
  email: { type: String, required: true, unique: true, index: true },
  name: { type: String, index: true },
  age: { type: Number }
});
userSchema.index({ name: 1, age: -1 }); // Compound index
userSchema.index({ email: 'text' }); // Text index

```

---

## Q28. ⚡ Mongoose query methods and optimization

Mongoose provides chainable query methods like `find()`, `where()`, `sort()`, `limit()`, `select()`, and `populate()` that build queries lazily and execute only when you call `.exec()` or use `await`.

- **Trade-offs**: Chainable queries are readable and composable, but the catch is they're lazy (don't execute until awaited), which can lead to confusion. Use `select()` to limit fields (projection), `lean()` to return plain JavaScript objects (faster but no Mongoose features), and `explain()` to analyze query performance—always use indexes for filtered and sorted queries.

Example:

```javascript
const users = await User.find({ age: { $gte: 18 } })
  .select('name email')
  .sort({ age: -1 })
  .limit(10)
  .lean(); // Returns plain objects, faster
const plan = await User.find({ age: { $gte: 18 } })
  .explain('executionStats'); // Query analysis

```

---

## Q29. 🪝 Mongoose query middleware and hooks

Mongoose provides pre and post hooks for queries (`find`, `findOne`, `update`, `delete`) that allow you to intercept and modify queries or results before and after execution.

- **Trade-offs**: Query hooks enable cross-cutting concerns like logging, caching, or data transformation, but the catch is they add overhead and can make debugging harder if overused. Use them sparingly for common operations like soft deletes or audit logging—avoid complex logic in hooks that could slow down queries.

Example:

```javascript
userSchema.pre('find', function() {
  this.where({ deleted: { $ne: true } }); // Soft delete filter
});
userSchema.post('find', function(docs) {
  console.log(`Found ${docs.length} users`);
});

```

---

---

## 📍 Navigation

<div align="center">

[MongoDB Fundamentals](1%29%20MongoDB%20Fundamentals.md) • [Home: Question List](question.md) • [Aggregation Framework →](3%29%20Aggregation%20Framework.md)

[📋 Cheatsheet](MongoDB%20Interview%20Cheatsheet.md]

</div>

---
