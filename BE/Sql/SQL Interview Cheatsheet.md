# 🧠 **SQL Interview Cheatsheet**

*Quick reference guide for SQL interview preparation*

---

## 📋 **SQL Sublanguages**

| Sublanguage | Purpose | Commands |
|-------------|---------|----------|
| **DDL** | Data Definition | CREATE, ALTER, DROP, TRUNCATE |
| **DML** | Data Manipulation | SELECT, INSERT, UPDATE, DELETE |
| **DCL** | Data Control | GRANT, REVOKE, DENY |
| **TCL** | Transaction Control | COMMIT, ROLLBACK, SAVEPOINT |

---

## 🔍 **JOIN Types**

| JOIN Type | Description | Use Case |
|-----------|-------------|----------|
| **INNER JOIN** | Only matching records | Strict relationships |
| **LEFT JOIN** | All left + matching right | Optional relationships |
| **RIGHT JOIN** | All right + matching left | Rarely used |
| **FULL JOIN** | All records from both | Complete data analysis |
| **CROSS JOIN** | Cartesian product | Testing, combinations |

---

## 🧮 **Aggregate Functions**

| Function | Purpose | Example |
|----------|---------|---------|
| **COUNT()** | Count rows | `COUNT(*)` or `COUNT(column)` |
| **SUM()** | Sum values | `SUM(salary)` |
| **AVG()** | Average values | `AVG(salary)` |
| **MIN()** | Minimum value | `MIN(salary)` |
| **MAX()** | Maximum value | `MAX(salary)` |

---

## 🎯 **WHERE vs HAVING**

| Clause | When | Aggregate Functions |
|--------|------|-------------------|
| **WHERE** | Before GROUP BY | ❌ Cannot use |
| **HAVING** | After GROUP BY | ✅ Can use |

---

## 📊 **Window Functions**

| Function | Purpose | Example |
|----------|---------|---------|
| **ROW_NUMBER()** | Sequential numbers | `ROW_NUMBER() OVER (ORDER BY salary)` |
| **RANK()** | Ranks with gaps | `RANK() OVER (ORDER BY salary)` |
| **DENSE_RANK()** | Ranks without gaps | `DENSE_RANK() OVER (ORDER BY salary)` |
| **LEAD()** | Next row value | `LEAD(salary) OVER (ORDER BY id)` |
| **LAG()** | Previous row value | `LAG(salary) OVER (ORDER BY id)` |

---

## 🔧 **Index Types**

| Index Type | Description | Count per Table |
|------------|-------------|-----------------|
| **Clustered** | Physical data order | 1 only |
| **Non-clustered** | Separate structure | Multiple |
| **Composite** | Multiple columns | Multiple |
| **Covering** | Includes all needed columns | Multiple |

---

## 🔐 **ACID Properties**

| Property | Description | Example |
|----------|-------------|---------|
| **Atomicity** | All or nothing | Transaction succeeds completely or fails completely |
| **Consistency** | Valid state | Database rules maintained before/after transaction |
| **Isolation** | Concurrent safety | Transactions don't interfere with each other |
| **Durability** | Permanent changes | Committed data survives system failures |

---

## 🚦 **Isolation Levels**

| Level | Dirty Read | Non-repeatable | Phantom Read | Performance |
|-------|------------|----------------|--------------|-------------|
| **READ UNCOMMITTED** | ✅ Allowed | ✅ Allowed | ✅ Allowed | Fastest |
| **READ COMMITTED** | ❌ Prevented | ✅ Allowed | ✅ Allowed | Fast |
| **REPEATABLE READ** | ❌ Prevented | ❌ Prevented | ✅ Allowed | Medium |
| **SERIALIZABLE** | ❌ Prevented | ❌ Prevented | ❌ Prevented | Slowest |

---

## 🎨 **Common Query Patterns**

### **Find Duplicates**
```sql
SELECT column, COUNT(*)
FROM table
GROUP BY column
HAVING COUNT(*) > 1;
```

### **Second Highest Value**
```sql
SELECT MAX(column)
FROM table
WHERE column < (SELECT MAX(column) FROM table);
```

### **Pagination**
```sql
SELECT * FROM table
ORDER BY column
LIMIT 10 OFFSET 20;
```

### **Running Total**
```sql
SELECT column,
       SUM(column) OVER (ORDER BY id ROWS UNBOUNDED PRECEDING) as running_total
FROM table;
```

---

## ⚡ **Performance Tips**

### **Index Best Practices**
- Create indexes on frequently queried columns
- Use composite indexes for multi-column queries
- Most selective columns first in composite indexes
- Avoid indexes on frequently updated columns

### **Query Optimization**
- Use `INNER JOIN` instead of `WHERE` clauses
- Avoid `SELECT *` - specify needed columns
- Use `EXISTS` instead of `IN` for subqueries
- Use `LIMIT` to restrict result sets

### **Common Anti-patterns**
- Functions on indexed columns in WHERE clauses
- Correlated subqueries in SELECT statements
- Missing WHERE clauses causing full table scans
- Using `!=` or `<>` instead of `NOT IN`

---

## 🔍 **Query Analysis**

### **EXPLAIN Keywords**
- **Seq Scan**: Full table scan (slow)
- **Index Scan**: Using index (fast)
- **Hash Join**: Hash-based join
- **Nested Loop**: Nested loop join
- **Sort**: Sorting operation

### **Performance Metrics**
- **Cost**: Estimated execution cost
- **Rows**: Number of rows processed
- **Width**: Average row size
- **Time**: Actual execution time

---

## 🛠️ **Useful Functions**

### **String Functions**
- `CONCAT()` - Concatenate strings
- `SUBSTRING()` - Extract substring
- `UPPER()`, `LOWER()` - Case conversion
- `TRIM()` - Remove whitespace

### **Date Functions**
- `NOW()` - Current timestamp
- `DATE()` - Extract date part
- `YEAR()`, `MONTH()`, `DAY()` - Extract date components
- `DATEDIFF()` - Calculate difference

### **NULL Handling**
- `IS NULL`, `IS NOT NULL` - Check for NULL
- `COALESCE()` - First non-NULL value
- `NULLIF()` - Convert to NULL
- `IFNULL()` - Replace NULL with value

---

## 📝 **Quick Reference Commands**

### **Data Manipulation**
```sql
-- Insert
INSERT INTO table (col1, col2) VALUES (val1, val2);

-- Update
UPDATE table SET col1 = val1 WHERE condition;

-- Delete
DELETE FROM table WHERE condition;

-- Select
SELECT col1, col2 FROM table WHERE condition;
```

### **Table Management**
```sql
-- Create table
CREATE TABLE table (col1 INT, col2 VARCHAR(50));

-- Alter table
ALTER TABLE table ADD COLUMN col3 INT;

-- Drop table
DROP TABLE table;

-- Create index
CREATE INDEX idx_name ON table (column);
```

### **Transaction Control**
```sql
-- Begin transaction
BEGIN TRANSACTION;

-- Commit changes
COMMIT;

-- Rollback changes
ROLLBACK;

-- Create savepoint
SAVEPOINT sp1;

-- Rollback to savepoint
ROLLBACK TO sp1;
```

---

## 🎯 **Interview Tips**

### **Common Questions**
1. **Explain normalization** - 1NF, 2NF, 3NF, BCNF
2. **Difference between WHERE and HAVING** - Row vs group filtering
3. **Types of joins** - INNER, LEFT, RIGHT, FULL, CROSS
4. **ACID properties** - Transaction reliability
5. **Index types** - Clustered vs non-clustered

### **Performance Questions**
1. **Query optimization** - Indexing, query structure
2. **Deadlock prevention** - Lock ordering
3. **Isolation levels** - Concurrency control
4. **Stored procedures vs functions** - When to use each

### **Practical Questions**
1. **Find duplicates** - GROUP BY with HAVING
2. **Second highest value** - Window functions or subqueries
3. **Pagination** - LIMIT/OFFSET or ROW_NUMBER()
4. **Running totals** - Window functions with OVER clause

---

*Remember: Practice with real data, understand the business context, and always consider performance implications!*
