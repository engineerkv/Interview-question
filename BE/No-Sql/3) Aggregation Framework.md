# 📊 3. Aggregation Framework (Q30–41)

---

## 📍 Navigation

<div align="center">

[Indexing & Query Optimization](2%29%20Indexing%20%26%20Query%20Optimization.md) • [Home: Question List](question.md) • [Data Modeling & Schema Design →](4%29%20Data%20Modeling%20%26%20Schema%20Design.md)

[📋 Cheatsheet](MongoDB%20Interview%20Cheatsheet.md]

</div>

---

---

## Q30. 📊 MongoDB aggregation pipeline

The aggregation pipeline allows you to process documents through multiple stages that filter, group, reshape, and transform data—MongoDB does all the work on the server side, so you can build complex data transformations without multiple round trips to the database.

- **Trade-offs**: Pipelines keep logic close to the data and avoid multiple round trips, which is great for performance. The catch is each stage costs CPU and RAM, so complex pipelines can hog (too many) resources if you're not careful—always test with real data volumes and use indexes on early `$match` stages.

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

## Q31. 📊 Main stages in the aggregation pipeline

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

## Q32. 🤔 Difference between `$match` and `$group` stages

`$match` filters documents (like WHERE in SQL), while `$group` aggregates documents by grouping them by a key and computing values like sums, averages, or counts—place `$match` early to reduce data before grouping.

- **Trade-offs**: `$match` should come early in pipelines to reduce data volume and can use indexes, while `$group` is memory-intensive and processes all input documents. Combining them efficiently (match first, then group) is key to performance—grouping large datasets without filtering first can cause memory issues.

Example:

```javascript
db.orders.aggregate([
  // $match: Filter documents early
  { $match: { status: "completed", amount: { $gte: 100 } } },
  // $group: Aggregate by customer
  { $group: {
    _id: "$customerId",
    totalSpent: { $sum: "$amount" },
    orderCount: { $sum: 1 }
  } }
]);

```

---

## Q33. 📊 Using `$sort` and `$limit` in aggregation

`$sort` orders documents by specified fields, while `$limit` restricts the number of documents passed to the next stage—use them together to get top N results efficiently, and place `$limit` after `$sort` to avoid sorting unnecessary documents.

- **Trade-offs**: `$sort` can be memory-intensive on large datasets and may require `allowDiskUse: true` if it exceeds RAM. Placing `$limit` after `$sort` helps, but for better performance, use indexes to support sorting or limit data volume with early `$match` stages.

Example:

```javascript
db.orders.aggregate([
  { $match: { status: "completed" } },
  // Sort by amount descending
  { $sort: { amount: -1 } },
  // Limit to top 10
  { $limit: 10 }
]);

// For better performance, use index
db.orders.createIndex({ status: 1, amount: -1 });

```

---

## Q34. 🔧 `$project` stage and how to use it

`$project` reshapes documents by including, excluding, or transforming fields—use it to select specific fields, rename them, add computed fields, or reshape the output structure.

- **Trade-offs**: `$project` reduces data size early in pipelines (improving performance) but can increase document size if you add computed fields. Use it strategically—include only needed fields early to reduce memory, or use it late to format final output, and be careful with `_id` as it's included by default unless explicitly excluded.

Example:

```javascript
// Project with field selection and computed fields
db.users.aggregate([
  {
    $project: {
      name: 1,
      email: 1,
      age: 1,
      _id: 0  // Exclude _id
    }
  }
]);

// Project with computed fields
db.products.aggregate([
  {
    $project: {
      name: 1,
      price: 1,
      discountedPrice: { $multiply: ["$price", 0.9] }
    }
  }
]);

```

---

## Q35. ⏰ `$unwind` and when to use it

`$unwind` deconstructs an array field, creating one document per array element—use it when you need to process individual array items, filter by array values, or group by array elements.

- **Trade-offs**: `$unwind` multiplies documents (one per array element), which can explode memory usage on large arrays. Always use `$match` before `$unwind` to reduce data volume, and consider `$limit` after unwinding—beware of empty arrays (they're removed by default unless you use `preserveNullAndEmptyArrays: true`).

Example:

```javascript
// Document with array
{
  _id: ObjectId("..."),
  name: "John",
  hobbies: ["reading", "gaming", "cooking"]
}

// Unwind array
db.users.aggregate([
  { $unwind: "$hobbies" }
]);
// Results in 3 documents, one per hobby

// Unwind with preserveNullAndEmptyArrays
db.users.aggregate([
  { $unwind: { path: "$hobbies", preserveNullAndEmptyArrays: true } }
]);

```

---

## Q36. 🔗 `$lookup` and how to perform joins

`$lookup` performs left-outer joins between collections, matching documents from the "from" collection with the input documents based on specified fields, and adding matched documents as an array field.

- **Trade-offs**: `$lookup` enables joins but can be expensive on large collections without supporting indexes. It always produces an array of matches (even if empty), so use `$unwind` to flatten single matches—for better performance, ensure the foreign field in the "from" collection is indexed.

Example:

```javascript
// Basic $lookup
db.orders.aggregate([
  {
    $lookup: {
      from: "customers",
      localField: "customerId",
      foreignField: "_id",
      as: "customer"
    }
  },
  { $unwind: "$customer" }  // Flatten single match
]);

// $lookup with pipeline (MongoDB 3.6+)
db.orders.aggregate([
  {
    $lookup: {
      from: "customers",
      let: { custId: "$customerId" },
      pipeline: [
        { $match: { $expr: { $eq: ["$_id", "$$custId"] } } },
        { $project: { name: 1, email: 1 } }
      ],
      as: "customer"
    }
  }
]);

```

---

## Q37. 🔧 `$facet` and how to use it for analytics

`$facet` splits the input into multiple sub-pipelines that run in parallel, generating multiple result sets from a single aggregation—ideal for dashboards that need multiple metrics or segments computed from the same dataset.

- **Trade-offs**: `$facet` reduces round trips by computing multiple aggregations in one pass, but it keeps all intermediate documents in memory for all sub-pipelines. Use it when you truly need parallel computations, but combine with `$limit` or early `$match` stages to cap data volume—memory usage can be high since each sub-pipeline processes the full input.

Example:

```javascript
db.orders.aggregate([
  { $match: { status: "completed" } },
  {
    $facet: {
      // Sales by month
      monthlySales: [
        { $group: {
          _id: { $month: "$date" },
          total: { $sum: "$amount" }
        } },
        { $sort: { _id: 1 } }
      ],
      // Top customers
      topCustomers: [
        { $group: {
          _id: "$customerId",
          total: { $sum: "$amount" }
        } },
        { $sort: { total: -1 } },
        { $limit: 5 }
      ],
      // Average order value
      avgOrderValue: [
        { $group: { _id: null, avg: { $avg: "$amount" } } }
      ]
    }
  }
]);

```

---

## Q38. 🔧 `$merge` and how to use it for data processing

`$merge` allows you to persist aggregation results into a collection (insert, replace, merge, or keep existing), enabling materialized views or nightly rollups without extra client code.

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

## Q39. 📊 Implementing pagination with aggregation

Pagination in aggregation uses `$skip` and `$limit` for offset-based pagination, or cursor-based pagination with `$match` on a sort field for better performance on large datasets.

- **Trade-offs**: Offset pagination (`$skip` + `$limit`) is simple but gets slower as offsets grow because MongoDB scans skipped documents. Cursor-based pagination (using `$match` with a sort field like `createdAt`) keeps performance constant but requires clients to track the last seen value—prefer cursor-based for large datasets.

Example:

```javascript
// Offset-based pagination (simple but slow for large offsets)
db.products.aggregate([
  { $match: { category: "electronics" } },
  { $sort: { createdAt: -1 } },
  { $skip: 20 },  // Skip first 20 documents
  { $limit: 10 }  // Return next 10 documents
]);

// Cursor-based pagination (better performance)
const lastCreatedAt = new Date("2023-12-01");
db.products.aggregate([
  { $match: {
    category: "electronics",
    createdAt: { $lt: lastCreatedAt }  // Cursor
  } },
  { $sort: { createdAt: -1 } },
  { $limit: 10 }
]);

```

---

## Q40. 📊 Using aggregation with Mongoose models

Mongoose models provide an `aggregate()` method that works exactly like MongoDB's native aggregation, allowing you to build pipelines with the same stages and operators while maintaining Mongoose's connection handling.

- **Trade-offs**: Mongoose aggregation is a thin wrapper around MongoDB aggregation, so performance is identical, but the catch is you don't get Mongoose document instances in results (they're plain objects). Use `Model.aggregate()` for complex data processing, and combine with `$lookup` for joins—remember that aggregation results bypass Mongoose middleware and validation.

Example:

```javascript
const results = await User.aggregate([
  { $match: { age: { $gte: 18 } } },
  { $group: { _id: '$department', count: { $sum: 1 } } },
  { $sort: { count: -1 } }
]);

```

---

## Q41. 📊 Mongoose aggregation with populate alternative

While `populate()` is convenient for simple references, aggregation with `$lookup` is more powerful for complex joins, filtering, and transformations that `populate()` can't handle efficiently.

- **Trade-offs**: `populate()` is easier to use for simple references but can cause N+1 queries and doesn't support complex filtering. Aggregation with `$lookup` gives you full control over joins and filtering, but the catch is it's more verbose and returns plain objects—use `$lookup` when you need to filter, transform, or aggregate joined data.

Example:

```javascript
const orders = await Order.aggregate([
  {
    $lookup: {
      from: 'users',
      localField: 'customerId',
      foreignField: '_id',
      as: 'customer'
    }
  },
  { $unwind: '$customer' },
  { $match: { 'customer.status': 'active' } }
]);

```

---

---

## 📍 Navigation

<div align="center">

[Indexing & Query Optimization](2%29%20Indexing%20%26%20Query%20Optimization.md) • [Home: Question List](question.md) • [Data Modeling & Schema Design →](4%29%20Data%20Modeling%20%26%20Schema%20Design.md)

[📋 Cheatsheet](MongoDB%20Interview%20Cheatsheet.md]

</div>

---
