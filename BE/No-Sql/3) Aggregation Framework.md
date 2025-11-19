# 3. Aggregation Framework (Q21–30)

---

## Q21. What is the aggregation pipeline, and how does it work?

The aggregation pipeline lets you stream documents through staged operators—filter, group, project, sort—so MongoDB transforms data server-side like a mini ETL workflow.

- **Trade-offs**: Pipelines keep logic close to the data and avoid multiple round trips, but each stage costs CPU/RAM; complex pipelines can hog resources if not carefully designed.

Example:
```javascript
// Basic aggregation pipeline
db.orders.aggregate([
  { $match: { status: "completed" } },
  { $group: { _id: "$customerId", total: { $sum: "$amount" } } },
  { $sort: { total: -1 } },
  { $limit: 10 }
]);
```

---

## Q22. What are the key aggregation stages (`$match`, `$group`, `$sort`, `$project`, `$limit`, `$unwind`)?

`$match` filters early, `$group` aggregates, `$sort` orders, `$project` reshapes fields, `$limit` trims output, and `$unwind` explodes arrays into individual documents.

- **Trade-offs**: Put `$match` and `$project` early to shrink data, but beware that `$sort` and `$unwind` can explode memory usage—combine them with indexes or `$limit` to contain cost.

Example:
```javascript
db.products.aggregate([
  // $match: Filter documents
  { $match: { category: "electronics", price: { $gte: 100 } } },
  
  // $unwind: Deconstruct array
  { $unwind: "$tags" },
  // $group: Aggregate by tag
  { $group: { _id: "$tags", count: { $sum: 1 } } }
]);
```

---

## Q23. How does the aggregation framework differ from MapReduce?

Aggregation is declarative, optimized, and supported on sharded clusters; MapReduce requires custom JavaScript map/reduce functions and is largely deprecated for most workloads.

- **Trade-offs**: Aggregation covers 99% of analytics faster and with less code, but if you truly need arbitrary JavaScript transformations, MapReduce or $function may still be necessary.

Example:
```javascript
// Aggregation Framework (preferred)
db.orders.aggregate([
  { $match: { status: "completed" } },
  { $group: { 
    _id: "$customerId", 
    totalSpent: { $sum: "$amount" }
  } }
]);
```

---

## Q24. How do `$lookup` and `$unwind` support joins and array handling?

`$lookup` performs left-outer joins across collections, producing an array of matches; `$unwind` then flattens that array (or any array field) so you can process each element individually.

- **Trade-offs**: `$lookup` on large collections can be expensive without supporting indexes, and `$unwind` multiplies documents—monitor memory and consider `$lookup` with pipelines plus `$limit`.

Example:
```javascript
// $lookup: Join collections
db.orders.aggregate([
  {
    $lookup: {
      from: "customers",
      localField: "customerId",
      foreignField: "_id",
      as: "customer"
    }
  },
  { $unwind: "$customer" }
]);
```

---

## Q25. What is the `$facet` stage, and why use it for analytics?

`$facet` splits the input into multiple sub-pipelines that run in parallel, so a single aggregation can generate multiple metrics/segments for dashboards without multiple DB hits.

- **Trade-offs**: Faceting reduces round trips but keeps all intermediate docs in memory—use only when you truly need parallel computations or combine with `$limit` to cap data.

Example:
```javascript
db.orders.aggregate([
  {
    $facet: {
      // Sales by month
      monthlySales: [
        { $group: { _id: { $month: "$date" }, total: { $sum: "$amount" } } }
      ],
      // Top customers
      topCustomers: [
        { $group: { _id: "$customerId", total: { $sum: "$amount" } } },
        { $sort: { total: -1 } },
        { $limit: 5 }
      ]
    }
  }
]);
```

---

## Q26. How do you optimize aggregation pipelines for performance?

Filter early with `$match`, use indexes on initial stages, `$project` away unused fields, push `$limit`/`$skip` when possible, and avoid heavy `$lookup`/$unwind unless necessary.

- **Trade-offs**: Getting the order right matters; letting `$sort` or `$group` process huge datasets without earlier filters will spike memory and may require allowDiskUse.

Example:
```javascript
// Optimized pipeline
db.orders.aggregate([
  // 1. Filter early to reduce data volume
  { $match: { 
    status: "completed",
    date: { $gte: new Date("2023-01-01") }
  } },
  // 2. Project only needed fields
  { $project: { customerId: 1, amount: 1, date: 1 } },
  // 3. Group and aggregate
  { $group: { _id: "$customerId", total: { $sum: "$amount" } } },
  // 4. Sort and limit
  { $sort: { total: -1 } },
  { $limit: 10 }
]);
```

---

## Q27. How do `$addFields`, `$group`, and `$project` shape documents?

`$addFields` adds computed fields without stripping old ones, `$group` aggregates by `_id` and runs `$sum`, `$avg`, etc., and `$project` reshapes documents or renames fields.

- **Trade-offs**: `$addFields` and `$project` can increase document size, so only compute what you need; `$group` requires enough RAM or `allowDiskUse` when working on big datasets.

Example:
```javascript
db.products.aggregate([
  // $addFields: Add computed fields
  {
    $addFields: {
      discountPrice: { $multiply: ["$price", 0.9] },
      isExpensive: { $gt: ["$price", 100] }
    }
  },
  // $group: Aggregate by category
  { $group: { _id: "$category", avgPrice: { $avg: "$price" } } },
  // $project: Reshape output
  { $project: { category: "$_id", avgPrice: 1, _id: 0 } }
]);
```

---

## Q28. How can you paginate efficiently with aggregation?

Offset pagination uses `$skip` + `$limit`, but for large datasets, prefer cursor-based pagination keyed by a stable sort field (e.g., `$match: { createdAt: { $lt: lastValue } }`).

- **Trade-offs**: `$skip` gets slower as offsets grow because MongoDB still scans skipped docs; cursor pagination keeps performance flat but requires clients to track the last sort key.

Example:
```javascript
// Offset-based pagination (simple but can be slow)
db.products.aggregate([
  { $match: { category: "electronics" } },
  { $sort: { createdAt: -1 } },
  { $skip: 20 },  // Skip first 20 documents
  { $limit: 10 }  // Return next 10 documents
]);
```

---

## Q29. What is the `$merge` stage, and why use it?

`$merge` lets you persist aggregation results into a collection (insert, replace, merge, or keep existing), enabling materialized views or nightly rollups without extra client code.

- **Trade-offs**: Persisting results accelerates reads but duplicates data and requires a refresh strategy; be mindful of write load when running $merge on large result sets.

Example:
```javascript
// Create materialized view
db.orders.aggregate([
  {
    $group: {
      _id: {
        year: { $year: "$date" },
        month: { $month: "$date" }
      },
      totalSales: { $sum: "$amount" }
    }
  },
  {
    $merge: {
      into: "monthly_sales",
      whenMatched: "replace",
      whenNotMatched: "insert"
    }
  }
]);
```

---

## Q30. What are collations, and how do they affect sorting/comparisons?

Collations define locale-specific rules (case sensitivity, accent handling, numeric ordering) for string comparisons in finds, sorts, aggregations, and indexes.

- **Trade-offs**: Collation-aware operations respect linguistic rules but can be slower and require collation-compatible indexes—always create indexes with the same collation you query with.

Example:
```javascript
// Create collection with collation
db.createCollection("users", {
  collation: {
    locale: "en_US",
    strength: 2,  // Case insensitive
    numericOrdering: true
  }
});
```

---
