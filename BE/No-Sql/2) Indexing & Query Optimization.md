# 2. Indexing & Query Optimization (Q11–20)

---

## Q11. What is an index in MongoDB, and how does it improve performance?

An index is a B-tree structure that lets MongoDB jump directly to matching keys instead of scanning the whole collection, cutting lookups from O(n) scans to O(log n) seeks.

- **Trade-offs**: Indexes speed reads and sorts but consume RAM/disk and slow writes because each insert/update must update the index—only create indexes that match real query patterns.

Example:
```javascript
// Create index on name field
db.users.createIndex({ name: 1 });

// Query using index
db.users.find({ name: "John" }).explain("executionStats");
```

---

## Q12. What types of indexes does MongoDB provide (single, compound, multikey, text, geo, TTL, partial)?

MongoDB offers single-field, compound, multikey (arrays), text search, geospatial, hashed, TTL, sparse, and partial indexes so you can tailor the data structure to your workload.

- **Trade-offs**: Specialized indexes solve niche problems (full-text, geo, expiring docs) but each one increases storage and slows writes; audit unused indexes to avoid bloat.

Example:
```javascript
// Single field index
db.users.createIndex({ email: 1 });

// Compound index
db.users.createIndex({ name: 1, age: -1 });
```

---

## Q13. What is a compound index, and how does field order affect queries?

A compound index stores multiple fields in one key; MongoDB can only use it when queries reference the leftmost prefix, so order must match your most common filters.

- **Trade-offs**: Place equality and highly selective fields first to maximize usefulness, but remember compound indexes are larger and only help for the prefixes you plan for.

Example:
```javascript
// Create compound index
db.users.createIndex({ name: 1, age: -1, city: 1 });

// These queries can use the index
db.users.find({ name: "John" });
db.users.find({ name: "John", age: { $gte: 25 } });
```

---

## Q14. What is a multikey index, and when is it automatically created?

Whenever you index a field that contains arrays, MongoDB automatically converts the index to multikey, indexing each array element so queries can match inside arrays.

- **Trade-offs**: Multikey indexes are vital for arrays but become larger and slower than scalar indexes, and MongoDB forbids compound indexes with more than one array field.

Example:
```javascript
// Document with array field
{
  _id: ObjectId("..."),
  name: "John",
  hobbies: ["reading", "gaming", "cooking"]
}
```

---

## Q15. What is a covered query, and how can you spot one with `explain()`?

A query is covered when the index contains every field needed for the filter and projection, so MongoDB never reads the documents—`explain("executionStats")` shows `indexOnly: true`.

- **Trade-offs**: Covered queries are the fastest possible, but you must design indexes that include projection fields (or exclude `_id`); otherwise MongoDB has to fetch documents.

Example:
```javascript
// Create compound index
db.users.createIndex({ name: 1, age: 1, email: 1 });

// Covered query - only uses index
db.users.find(
  { name: "John", age: { $gte: 25 } },
  { name: 1, age: 1, email: 1, _id: 0 }
);
```

---

## Q16. What’s the difference between ascending and descending indexes?

Index keys can be ascending (1) or descending (-1); MongoDB uses the stored order to satisfy sorts without in-memory work, especially in compound indexes with mixed directions.

- **Trade-offs**: Match index direction to how you sort—misaligned sorts may trigger an extra SORT stage and more memory usage, especially on large result sets.

Example:
```javascript
// Ascending index
db.users.createIndex({ age: 1 });

// Descending index
db.users.createIndex({ age: -1 });
```

---

## Q17. What is index intersection, and how does MongoDB use multiple indexes?

Index intersection lets MongoDB combine the results of multiple single-field indexes (e.g., `{name:1}` and `{age:1}`) to satisfy a query without maintaining every possible compound index.

- **Trade-offs**: Intersection can rescue queries when a perfect compound index doesn’t exist, but it’s usually slower than a dedicated compound index and can use more memory.

Example:

```javascript
db.users.createIndex({ name: 1 });
db.users.createIndex({ age: 1 });
db.users.find({ name: "John", age: { $gte: 30 } }).explain();
```

---

## Q18. What is a TTL (Time-To-Live) index, and when should you apply it?

TTL indexes automatically delete documents after a specified age by watching a Date field—ideal for session tokens, logs, cache entries, or any data that expires naturally.

- **Trade-offs**: Cleanup runs every ~60 seconds and only works on Date fields; don’t rely on TTL when you might need data later, because deletions are irreversible.

Example:
```javascript
// Create TTL index (expires after 1 hour)
db.sessions.createIndex(
  { createdAt: 1 },
  { expireAfterSeconds: 3600 }
);
```

---

## Q19. What does the `$hint` operator do, and when should you use it?

`$hint` forces MongoDB to use a specific index instead of relying on the planner—handy for testing or working around bad plan choices, but dangerous if data patterns change.

- **Trade-offs**: A hint can stabilize performance but can also lock you into a poor plan later; prefer fixing index design or analyzing plans before shipping hints to production.

Example:
```javascript
// Force use of specific index
db.users.find({ name: "John", age: 25 })
  .hint({ name: 1, age: 1 });

// Force collection scan (no index)
db.users.find({ name: "John" }).hint({ $natural: 1 });
```

---

## Q20. How do you use `explain()` to analyze query performance and execution plans?

`explain()` reveals whether a query used an index or collection scan, how many docs it examined, and which stages (IXSCAN, FETCH, SORT) were executed so you can tune queries.

- **Trade-offs**: `explain("executionStats")` gives real numbers but actually runs the query; `allPlansExecution` helps catch unstable plans but is heavier—use carefully on production data.

Example:
```javascript
// Basic explain
db.users.find({ name: "John" }).explain();

// Detailed execution stats
db.users.find({ name: "John" }).explain("executionStats");
```
