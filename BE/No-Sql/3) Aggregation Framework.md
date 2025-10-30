# 📊 3. Aggregation Framework (Q21–30)

---

## 21) What is the **aggregation pipeline**, and how does it work?

Concept:
The aggregation pipeline is a framework for data processing that transforms documents through a sequence of stages, each performing specific operations on the data.

Example:
```javascript
// Basic aggregation pipeline
db.orders.aggregate([
  { $match: { status: "completed" } },
  { $group: { _id: "$customerId", total: { $sum: "$amount" } } },
  { $sort: { total: -1 } },
  { $limit: 10 }
```

Deep Insight:
- **Stage-based**: Data flows through sequential stages
- **Streaming**: Processes documents one at a time
- **Flexible**: Can combine multiple operations in single query
- **Memory Efficient**: Processes data in batches
- **Optimizable**: MongoDB optimizes pipeline execution

---

## 22) What are the key stages in an aggregation pipeline (match, group, sort, project, limit, unwind)?

Concept:
Key stages include `$match` (filtering), `$group` (grouping), `$sort` (sorting), `$project` (field selection), `$limit` (result limiting), and `$unwind` (array deconstruction).

Example:
```javascript
db.products.aggregate([
  // $match: Filter documents
  { $match: { category: "electronics", price: { $gte: 100 } } },
  
  // $unwind: Deconstruct array
  { $unwind: "$tags" },
```

Deep Insight:
- **$match**: Filters documents early, reduces data volume
- **$group**: Groups documents and performs aggregations
- **$sort**: Sorts results, can use indexes if early in pipeline
- **$project**: Reshapes documents, includes/excludes fields
- **$limit**: Reduces output size, should be used after sorting
- **$unwind**: Deconstructs arrays for processing individual elements

---

## 23) What is the difference between the **aggregation framework** and **MapReduce**?

Concept:
The aggregation framework is declarative and easier to use for most operations, while MapReduce is more flexible but complex, suitable for custom data processing logic.

Example:
```javascript
// Aggregation Framework (preferred)
db.orders.aggregate([
  { $match: { status: "completed" } },
  { $group: { 
    _id: "$customerId", 
    totalSpent: { $sum: "$amount" },
```

Deep Insight:
- **Aggregation**: Declarative, easier to read and maintain
- **MapReduce**: Imperative, more flexible but complex
- **Performance**: Aggregation framework is generally faster
- **Use Cases**: Aggregation for most operations, MapReduce for custom logic
- **Deprecation**: MapReduce is deprecated in favor of aggregation

---

## 24) How do `$lookup` and `$unwind` help with data joins in MongoDB?

Concept:
`$lookup` performs left outer joins between collections, while `$unwind` deconstructs arrays to enable processing of array elements in aggregation pipelines.

Example:
```javascript
// $lookup: Join collections
db.orders.aggregate([
  {
    $lookup: {
      from: "customers",
      localField: "customerId",
```

Deep Insight:
- **$lookup**: Performs left outer joins between collections
- **$unwind**: Deconstructs arrays for individual element processing
- **Performance**: $lookup can be expensive on large datasets
- **Memory**: $unwind can increase memory usage significantly
- **Use Cases**: $lookup for joins, $unwind for array processing

---

## 25) What is the `$facet` stage, and how can it be used for complex analytics queries?

Concept:
The `$facet` stage allows multiple aggregation pipelines to run in parallel on the same input, useful for generating multiple analytics views in a single query.

Example:
```javascript
db.orders.aggregate([
  {
    $facet: {
      // Sales by month
      monthlySales: [
        {
```

Deep Insight:
- **Parallel Processing**: Multiple pipelines run simultaneously
- **Single Query**: Reduces network round trips
- **Analytics**: Perfect for dashboard and reporting queries
- **Memory Usage**: Can be memory intensive
- **Performance**: Generally faster than separate queries

---

## 26) How do you optimize aggregation pipelines for performance?

Concept:
Optimize by using `$match` early, proper indexing, limiting data with `$limit`, using `$project` to reduce data, and avoiding expensive operations like `$lookup`.

Example:
```javascript
// Optimized pipeline
db.orders.aggregate([
  // 1. Filter early to reduce data volume
  { $match: { 
    status: "completed",
    date: { $gte: new Date("2023-01-01") }
```

Deep Insight:
- **Early Filtering**: Use $match early to reduce data volume
- **Index Usage**: Ensure sort operations can use indexes
- **Field Selection**: Use $project to reduce data transfer
- **Avoid Expensive Operations**: Minimize $lookup and $unwind usage
- **Memory Management**: Use $limit and $skip appropriately

---

## 27) What are **pipeline operators**, and how do you use `$addFields`, `$group`, and `$project` effectively?

Concept:
Pipeline operators transform data: `$addFields` adds new fields, `$group` groups and aggregates data, and `$project` reshapes documents by including/excluding fields.

Example:
```javascript
db.products.aggregate([
  // $addFields: Add computed fields
  {
    $addFields: {
      discountPrice: { $multiply: ["$price", 0.9] },
      isExpensive: { $gt: ["$price", 100] },
```

Deep Insight:
- **$addFields**: Adds computed fields without removing existing ones
- **$group**: Groups documents and performs aggregations
- **$project**: Reshapes documents, controls field visibility
- **Field References**: Use $fieldName to reference field values
- **Computed Fields**: Can use expressions and operators for calculations

---

## 28) How can you paginate results efficiently using the aggregation framework?

Concept:
Use `$skip` and `$limit` stages for pagination, but for large datasets, consider cursor-based pagination using `$sort` with unique fields for better performance.

Example:
```javascript
// Offset-based pagination (simple but can be slow)
db.products.aggregate([
  { $match: { category: "electronics" } },
  { $sort: { createdAt: -1 } },
  { $skip: 20 },  // Skip first 20 documents
  { $limit: 10 }  // Return next 10 documents
```

Deep Insight:
- **Offset Pagination**: Simple but slow for large offsets
- **Cursor Pagination**: More efficient for large datasets
- **Sorting**: Ensure consistent sort order for pagination
- **Indexes**: Use indexes on sort fields for better performance
- **Memory**: Cursor-based pagination uses less memory

---

## 29) What is the `$merge` stage used for in aggregation pipelines?

Concept:
The `$merge` stage writes aggregation results to a collection, useful for creating materialized views, data warehousing, and complex data transformations.

Example:
```javascript
// Create materialized view
db.orders.aggregate([
  {
    $group: {
      _id: {
        year: { $year: "$date" },
```

Deep Insight:
- **Materialized Views**: Pre-computed aggregation results
- **Performance**: Faster than real-time aggregation
- **Storage**: Results stored in separate collection
- **Updates**: Can replace, merge, or insert based on conditions
- **Use Cases**: Reporting, analytics, data warehousing

---

## 30) What are **collations** in MongoDB, and how do they affect sorting and comparisons?

Concept:
Collations define language-specific rules for string comparison and sorting, affecting how text is processed in queries, indexes, and aggregation operations.

Example:
```javascript
// Create collection with collation
db.createCollection("users", {
  collation: {
    locale: "en_US",
    strength: 2,  // Case insensitive
    numericOrdering: true
```

Deep Insight:
- **Locale Support**: Language-specific sorting and comparison rules
- **Case Sensitivity**: Control case-sensitive comparisons
- **Numeric Ordering**: Proper numeric sorting within strings
- **Index Compatibility**: Collations affect index usage
- **Performance**: Collation-aware operations may be slower

---
