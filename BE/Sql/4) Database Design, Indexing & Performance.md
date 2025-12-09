# ⚡ 4. Database Design, Indexing & Performance (Q31–40)

---

## 📍 Navigation

<div align="center">

[Filtering, Grouping & Aggregation](3%29%20Filtering%2C%20Grouping%20%26%20Aggregation.md) • [Home: Question List](question.md) • [Transactions, Concurrency & Stored Logic →](5%29%20Transactions%2C%20Concurrency%20%26%20Stored%20Logic.md)

[📋 Cheatsheet](SQL%20Interview%20Cheatsheet.md]

</div>

---

---

## Q31. 🗄️ Database normalization and why it's important

Normalization is the process of organizing data to reduce redundancy and improve data integrity by eliminating duplicate data and ensuring data dependencies make sense. 1NF eliminates duplicate columns and ensures atomic values, 2NF removes partial dependencies, 3NF removes transitive dependencies, and BCNF ensures every determinant is a candidate key (stronger than 3NF).

- **Trade-offs**: Normalization reduces redundancy and improves data integrity, but may require more joins for queries which can impact performance. Normalized databases use less storage and are easier to maintain, but denormalized databases may have faster read operations—balance normalization with performance needs.

Example:

```sql
-- Before normalization (redundant data)
CREATE TABLE orders (
    order_id INT PRIMARY KEY,
    customer_name VARCHAR(100),
    customer_email VARCHAR(100),
    product_name VARCHAR(100),
    quantity INT,
    price DECIMAL(10,2)
);

-- After normalization (1NF, 2NF, 3NF)
CREATE TABLE customers (
    customer_id INT PRIMARY KEY,
    customer_name VARCHAR(100),
    customer_email VARCHAR(100)
);

CREATE TABLE products (
    product_id INT PRIMARY KEY,
    product_name VARCHAR(100),
    price DECIMAL(10,2)
);

CREATE TABLE orders (
    order_id INT PRIMARY KEY,
    customer_id INT,
    product_id INT,
    quantity INT,
    FOREIGN KEY (customer_id) REFERENCES customers(customer_id),
    FOREIGN KEY (product_id) REFERENCES products(product_id)
);

```

---

## Q32. 📝 Different normal forms (1NF, 2NF, 3NF, BCNF)

Normalization reduces data redundancy and improves data integrity, but can increase query complexity and potentially impact performance due to more joins. Normalized databases use less storage space and are easier to maintain, but denormalized databases may have faster read operations.

- **Trade-offs**: Normalization reduces redundancy and saves storage, but requires more joins which can slow down queries. The key is balancing normalization with performance—use normalization for transactional systems where data integrity matters, and consider denormalization for read-heavy reporting systems where speed is critical.

Example:

```sql
-- Normalized structure (more tables, more joins)
SELECT c.customer_name, p.product_name, o.quantity
FROM customers c
JOIN orders o ON c.customer_id = o.customer_id
JOIN products p ON o.product_id = p.product_id
WHERE c.customer_id = 1;

```

---

## Q33. ⏰ Denormalization and when to use it

Denormalization intentionally introduces redundancy to improve query performance, especially useful for read-heavy applications and reporting systems. It reduces joins and pre-calculates values, making queries significantly faster for complex analytical queries.

- **Trade-offs**: Denormalization improves query performance but increases storage and data redundancy, and makes updates more complex. It requires careful handling of data consistency—use it for data warehouses, reporting systems, and read-heavy applications where reads far outnumber writes.

Example:

```sql
-- Denormalized table for reporting
CREATE TABLE sales_summary (
    product_id INT,
    product_name VARCHAR(100),
    category_name VARCHAR(50),
    total_sales DECIMAL(15,2),
    PRIMARY KEY (product_id)
);

```

---

## Q34. ⚡ Indexes and how they improve performance

Indexes are data structures that speed up data retrieval by providing quick access to specific rows, similar to a book's index. Most indexes use B-tree structures that provide logarithmic search time, reducing query time from seconds to milliseconds.

- **Trade-offs**: Indexes dramatically speed up SELECT queries but require additional storage space and slow down INSERT, UPDATE, DELETE operations because each change must update the index. More selective columns make better indexes—create indexes on frequently queried columns, but don't over-index because each index adds write overhead.

Example:

```sql
-- Create indexes for better performance
CREATE INDEX idx_employee_name ON employees(name);
CREATE INDEX idx_employee_dept ON employees(department_id);
CREATE INDEX idx_employee_salary ON employees(salary);

-- Query uses index for fast lookup
SELECT * FROM employees WHERE name = 'John Doe';

```

---

## Q35. 📇 Difference between clustered and non-clustered indexes

Clustered indexes determine the physical order of data storage and there can only be one per table, while non-clustered indexes are separate structures that point to data and multiple can exist per table. The clustered index is the table itself (very fast for primary key lookups), while non-clustered indexes are separate structures (require index lookup plus table access).

- **Trade-offs**: Clustered indexes are fastest for primary key lookups and range scans because data is physically ordered, but these can become fragmented affecting performance. Non-clustered indexes are slower for range queries but you can have multiple—the primary key automatically creates a clustered index in most databases, so choose it wisely.

Example:

```sql
-- Clustered index (determines physical order)
CREATE TABLE employees (
    employee_id INT PRIMARY KEY,  -- Automatically creates clustered index
    name VARCHAR(100),
    salary DECIMAL(10,2)
);

-- Non-clustered index (separate structure)
CREATE INDEX idx_employee_name ON employees(name);
CREATE INDEX idx_employee_salary ON employees(salary);

-- Clustered index query (very fast - direct data access)
SELECT * FROM employees WHERE employee_id = 123;

-- Non-clustered index query (requires index lookup + table access)
SELECT * FROM employees WHERE name = 'John Doe';

```

---

## Q36. 📇 Composite indexes and when to use them

Composite indexes are indexes on multiple columns where column order significantly affects query performance, with the most selective columns typically placed first. The leftmost rule means queries must use leftmost columns of the composite index to be effective.

- **Trade-offs**: Composite indexes can cover more queries than single-column indexes, but they require more storage and have higher maintenance overhead for updates. Place the most selective columns first and match column order to your most common query patterns—queries that skip leftmost columns can't use the index effectively.

Example:

```sql
-- Composite index with optimal column order
CREATE INDEX idx_dept_salary_name ON employees(department_id, salary, name);

-- Efficient queries (use leftmost columns)
SELECT * FROM employees WHERE department_id = 5;
SELECT * FROM employees WHERE department_id = 5 AND salary > 50000;

-- Inefficient query (skips leftmost column, can't use index effectively)
SELECT * FROM employees WHERE salary > 50000;  -- Won't use index

```

---

## Q37. 📇 Index fragmentation and how to fix it

A covering index includes all columns needed for a query, eliminating the need to access the actual table data and significantly improving query performance. It includes all columns needed for SELECT, WHERE, and ORDER BY clauses, making it the fastest possible query execution.

- **Trade-offs**: Covering indexes eliminate table lookups and are significantly faster than regular indexes, but these require more storage space due to additional columns and have higher overhead for INSERT, UPDATE, DELETE operations. Use them for frequently executed queries with specific column requirements—these are perfect when you know exactly which columns you'll query.

Example:

```sql
-- Regular index (requires table lookup)
CREATE INDEX idx_employee_dept ON employees(department_id);

-- Covering index (includes all needed columns)
CREATE INDEX idx_employee_dept_covering ON employees(department_id, name, salary);

-- Query uses covering index (no table lookup needed)
SELECT name, salary FROM employees WHERE department_id = 5;

```

---

## Q38. ⚡ Using EXPLAIN/EXPLAIN ANALYZE to optimize queries

Index fragmentation occurs when data pages are not contiguous due to frequent updates, causing performance degradation that can be fixed through rebuild or reorganize operations. Frequent INSERT, UPDATE, DELETE operations cause page splits and fragmentation, which slows down query performance and wastes storage space.

- **Trade-offs**: REBUILD is more thorough but resource-intensive—use it for high fragmentation (>30%). REORGANIZE is less resource-intensive—use it for moderate fragmentation (10-30%). Monitor fragmentation levels regularly using system views, and schedule maintenance during low-traffic periods to minimize impact.

Example:

```sql
-- Check index fragmentation (SQL Server)
SELECT
    object_name(ips.object_id) as table_name,
    i.name as index_name,
    ips.avg_fragmentation_in_percent,
    ips.page_count
FROM sys.dm_db_index_physical_stats(DB_ID(), NULL, NULL, NULL, 'DETAILED') ips
JOIN sys.indexes i ON ips.object_id = i.object_id AND ips.index_id = i.index_id;

-- Rebuild index (for high fragmentation)
ALTER INDEX idx_employee_name ON employees REBUILD;

-- Reorganize index (for moderate fragmentation)
ALTER INDEX idx_employee_name ON employees REORGANIZE;

```

---

## Q39. ⚡ Common query optimization techniques

EXPLAIN shows the query execution plan, while EXPLAIN ANALYZE also shows actual execution statistics and timing, helping identify performance bottlenecks. The execution plan shows how the database will execute the query (Index Scan, Hash Join, etc.), reveals whether indexes are being used effectively, and shows which join algorithms are being used.

- **Trade-offs**: EXPLAIN shows the planned execution without running the query, while EXPLAIN ANALYZE actually runs the query and shows real statistics—use EXPLAIN for quick checks, and EXPLAIN ANALYZE when you need actual timing and row counts. This is an essential tool for query optimization and troubleshooting—always check the execution plan before optimizing.

Example:

```sql
-- Basic EXPLAIN (shows execution plan without running query)
EXPLAIN SELECT e.name, d.department_name
FROM employees e
JOIN departments d ON e.department_id = d.department_id
WHERE e.salary > 50000;

-- EXPLAIN ANALYZE (runs query and shows actual execution stats)
EXPLAIN ANALYZE SELECT e.name, e.salary
FROM employees e
WHERE e.department_id = 5;

```

---

## Q40. 💡 Identifying and fixing slow queries

Query optimization involves using proper indexing, efficient joins, avoiding unnecessary operations, and writing queries that leverage database features effectively. Create appropriate indexes on frequently queried columns, use INNER JOIN instead of WHERE clauses, avoid SELECT *, and use indexed columns in WHERE conditions.

- **Trade-offs**: Proper indexing dramatically speeds up queries but slows down writes. Avoid functions on columns in WHERE clauses (they prevent index usage), and write queries that can leverage indexes to avoid full table scans. Use EXPLAIN to verify your optimizations are working—measure first, optimize second.

Example:

```sql
-- Poor query (SELECT *, implicit join, no index usage)
SELECT * FROM employees e, departments d
WHERE e.department_id = d.department_id
AND e.salary > 50000
ORDER BY e.name;

-- Optimized query (specific columns, explicit JOIN, indexed columns)
SELECT e.name, e.salary, d.department_name
FROM employees e
INNER JOIN departments d ON e.department_id = d.department_id
WHERE e.salary > 50000
ORDER BY e.name;

```

---

---

## 📍 Navigation

<div align="center">

[Filtering, Grouping & Aggregation](3%29%20Filtering%2C%20Grouping%20%26%20Aggregation.md) • [Home: Question List](question.md) • [Transactions, Concurrency & Stored Logic →](5%29%20Transactions%2C%20Concurrency%20%26%20Stored%20Logic.md)

[📋 Cheatsheet](SQL%20Interview%20Cheatsheet.md]

</div>

---
