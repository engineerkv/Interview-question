# 4) Database Design, Indexing & Performance (Q31–40)

## 31) What is **normalization**? Explain 1NF, 2NF, 3NF, and BCNF with examples.

Concept:
Normalization is the process of organizing data to reduce redundancy and improve data integrity by eliminating duplicate data and ensuring data dependencies make sense.

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
```

Deep Insight:

- **1NF**: Eliminates duplicate columns and ensures atomic values (no repeating groups)
- **2NF**: Removes partial dependencies (non-key attributes depend on entire primary key)
- **3NF**: Removes transitive dependencies (non-key attributes don't depend on other non-key attributes)
- **BCNF**: Every determinant is a candidate key (stronger than 3NF)
- **Trade-offs**: Normalization reduces redundancy but may require more joins for queries

## 32) What are the advantages and disadvantages of normalization?

Concept:
Normalization reduces data redundancy and improves data integrity, but can increase query complexity and potentially impact performance due to more joins.

Example:
```sql
-- Normalized structure (more tables, more joins)
SELECT c.customer_name, p.product_name, o.quantity
FROM customers c
JOIN orders o ON c.customer_id = o.customer_id
JOIN products p ON o.product_id = p.product_id
WHERE c.customer_id = 1;
```

Deep Insight:

- **Advantages**: Reduces redundancy, improves data integrity, saves storage space, easier maintenance
- **Disadvantages**: More complex queries, potential performance impact, more joins required
- **Storage**: Normalized databases typically use less storage space
- **Performance**: Denormalized databases may have faster read operations
- **Maintenance**: Normalized databases are easier to maintain and update

## 33) What is **denormalization**, and when is it beneficial?

Concept:
Denormalization intentionally introduces redundancy to improve query performance, especially useful for read-heavy applications and reporting systems.

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

Deep Insight:

- **Purpose**: Improves query performance by reducing joins and pre-calculating values
- **Use Cases**: Data warehouses, reporting systems, read-heavy applications
- **Trade-offs**: Increased storage, data redundancy, more complex updates
- **Maintenance**: Requires careful handling of data consistency
- **Performance**: Significantly faster for complex analytical queries

## 34) What are **indexes**, and how do they improve query performance?

Concept:
Indexes are data structures that speed up data retrieval by providing quick access to specific rows, similar to a book's index that helps you find pages quickly.

Example:
```sql
-- Create indexes for better performance
CREATE INDEX idx_employee_name ON employees(name);
CREATE INDEX idx_employee_dept ON employees(department_id);
CREATE INDEX idx_employee_salary ON employees(salary);

-- Query uses index for fast lookup
SELECT * FROM employees WHERE name = 'John Doe';
```

Deep Insight:

- **B-Tree Structure**: Most common index type, provides logarithmic search time
- **Query Speed**: Indexes can reduce query time from seconds to milliseconds
- **Storage Cost**: Indexes require additional storage space
- **Maintenance**: Indexes slow down INSERT, UPDATE, DELETE operations
- **Selectivity**: More selective columns make better indexes

## 35) What's the difference between **clustered** and **non-clustered** indexes?

Concept:
Clustered indexes determine the physical order of data storage and there can only be one per table, while non-clustered indexes are separate structures that point to data and multiple can exist per table.

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

Deep Insight:

- **Clustered Index**: Only one per table, determines physical data order, very fast for range queries
- **Non-clustered Index**: Multiple per table, separate structure, slower than clustered for range queries
- **Storage**: Clustered index is the table itself, non-clustered indexes are separate structures
- **Performance**: Clustered index is fastest for primary key lookups and range scans
- **Fragmentation**: Clustered indexes can become fragmented, affecting performance

## 36) What are **composite indexes**, and how does column order affect performance?

Concept:
Composite indexes are indexes on multiple columns where column order significantly affects query performance, with the most selective columns typically placed first.

Example:
```sql
-- Composite index with optimal column order
CREATE INDEX idx_dept_salary_name ON employees(department_id, salary, name);

-- Efficient queries (use leftmost columns)
SELECT * FROM employees WHERE department_id = 5;
SELECT * FROM employees WHERE department_id = 5 AND salary > 50000;
```

Deep Insight:

- **Leftmost Rule**: Queries must use leftmost columns of composite index to be effective
- **Column Order**: Most selective columns should come first in composite indexes
- **Coverage**: Composite indexes can cover more queries than single-column indexes
- **Storage**: Composite indexes require more storage than single-column indexes
- **Maintenance**: More columns mean higher maintenance overhead for updates

## 37) What is a **covering index**, and when is it useful?

Concept:
A covering index includes all columns needed for a query, eliminating the need to access the actual table data and significantly improving query performance.

Example:
```sql
-- Regular index (requires table lookup)
CREATE INDEX idx_employee_dept ON employees(department_id);

-- Covering index (includes all needed columns)
CREATE INDEX idx_employee_dept_covering ON employees(department_id, name, salary);

-- Query uses covering index (no table lookup needed)
SELECT name, salary FROM employees WHERE department_id = 5;
```

Deep Insight:

- **Complete Coverage**: Includes all columns needed for SELECT, WHERE, ORDER BY clauses
- **Performance**: Eliminates table lookups, significantly faster than regular indexes
- **Storage**: Requires more storage space due to additional columns
- **Maintenance**: Higher overhead for INSERT, UPDATE, DELETE operations
- **Use Cases**: Perfect for frequently executed queries with specific column requirements

## 38) What is **index fragmentation**, and how do you fix it?

Concept:
Index fragmentation occurs when data pages are not contiguous due to frequent updates, causing performance degradation that can be fixed through rebuild or reorganize operations.

Example:
```sql
-- Check index fragmentation
SELECT 
    object_name(ips.object_id) as table_name,
    i.name as index_name,
    ips.avg_fragmentation_in_percent,
    ips.page_count
FROM sys.dm_db_index_physical_stats(DB_ID(), NULL, NULL, NULL, 'DETAILED') ips
JOIN sys.indexes i ON ips.object_id = i.object_id AND ips.index_id = i.index_id;
```

Deep Insight:

- **Causes**: Frequent INSERT, UPDATE, DELETE operations cause page splits and fragmentation
- **Impact**: Fragmented indexes slow down query performance and waste storage space
- **Detection**: Use system views to monitor fragmentation levels
- **REBUILD**: More thorough but resource-intensive, use for high fragmentation (>30%)
- **REORGANIZE**: Less resource-intensive, use for moderate fragmentation (10-30%)

## 39) How do you analyze a query's performance using **EXPLAIN** or **EXPLAIN ANALYZE**?

Concept:
EXPLAIN shows the query execution plan, while EXPLAIN ANALYZE also shows actual execution statistics and timing, helping identify performance bottlenecks.

Example:
```sql
-- Basic EXPLAIN
EXPLAIN SELECT e.name, d.department_name
FROM employees e
JOIN departments d ON e.department_id = d.department_id
WHERE e.salary > 50000;

-- EXPLAIN ANALYZE (with actual execution stats)
EXPLAIN ANALYZE SELECT e.name, e.salary
FROM employees e
WHERE e.department_id = 5;
```

Deep Insight:

- **Execution Plan**: Shows how database will execute the query (Index Scan, Hash Join, etc.)
- **Cost Analysis**: Helps identify expensive operations and optimization opportunities
- **Index Usage**: Reveals whether indexes are being used effectively
- **Join Strategies**: Shows which join algorithms are being used
- **Performance Tuning**: Essential tool for query optimization and troubleshooting

## 40) What are common **query optimization techniques** (indexing, joins, avoiding SELECT *)?

Concept:
Query optimization involves using proper indexing, efficient joins, avoiding unnecessary operations, and writing queries that leverage database features effectively.

Example:
```sql
-- Poor query
SELECT * FROM employees e, departments d
WHERE e.department_id = d.department_id
AND e.salary > 50000
ORDER BY e.name;

-- Optimized query
SELECT e.name, e.salary, d.department_name
FROM employees e
INNER JOIN departments d ON e.department_id = d.department_id
WHERE e.salary > 50000
ORDER BY e.name;
```

Deep Insight:

- **Indexing**: Create appropriate indexes on frequently queried columns
- **Join Optimization**: Use INNER JOIN instead of WHERE clauses for better performance
- **Column Selection**: Avoid SELECT *, specify only needed columns
- **WHERE Clauses**: Use indexed columns in WHERE conditions, avoid functions on columns
- **Query Structure**: Write queries that can leverage indexes and avoid full table scans
