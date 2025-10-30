# 2) Querying & Joins (Q11–20)

## 11) What are the different types of joins (INNER, LEFT, RIGHT, FULL, CROSS)?

Concept:
Joins combine data from multiple tables based on related columns, with different types returning different sets of matching and non-matching records.

Example:
```sql
-- INNER JOIN - only matching records
SELECT e.name, d.department_name
FROM employees e
INNER JOIN departments d ON e.dept_id = d.dept_id;

-- LEFT JOIN - all left table records + matches
SELECT e.name, d.department_name
FROM employees e
LEFT JOIN departments d ON e.dept_id = d.dept_id;

-- RIGHT JOIN - all right table records + matches
SELECT e.name, d.department_name
FROM employees e
RIGHT JOIN departments d ON e.dept_id = d.dept_id;

-- FULL OUTER JOIN - all records from both tables
SELECT e.name, d.department_name
FROM employees e
FULL OUTER JOIN departments d ON e.dept_id = d.dept_id;
```

Deep Insight:
- **INNER JOIN**: Returns only records that have matching values in both tables
- **LEFT JOIN**: Returns all records from left table and matching records from right table
- **RIGHT JOIN**: Returns all records from right table and matching records from left table
- **FULL JOIN**: Returns all records when there's a match in either table
- **CROSS JOIN**: Returns Cartesian product of both tables (every row from first table with every row from second)

## 12) What is a **self-join**? Provide a practical example.

Concept:
A self-join is when a table is joined with itself, useful for finding relationships within the same table like employee-manager hierarchies.

Example:
```sql
-- Find employees and their managers
SELECT 
    e1.employee_name AS employee,
    e2.employee_name AS manager
FROM employees e1
LEFT JOIN employees e2 ON e1.manager_id = e2.employee_id;
```

Deep Insight:
- **Same Table**: Uses table aliases to reference the same table multiple times
- **Hierarchical Data**: Perfect for organizational charts, category hierarchies, and parent-child relationships
- **Performance**: Can be expensive on large tables, proper indexing is crucial
- **Aliases Required**: Must use different aliases to distinguish between the two instances
- **Common Use Cases**: Employee-manager relationships, product categories, comment threads

## 13) What's the difference between `INNER JOIN` and `LEFT JOIN`?

Concept:
INNER JOIN returns only matching records from both tables, while LEFT JOIN returns all records from the left table and matching records from the right table.

Example:
```sql
-- INNER JOIN - only employees with departments
SELECT e.name, d.department_name
FROM employees e
INNER JOIN departments d ON e.dept_id = d.dept_id;

-- LEFT JOIN - all employees, even without departments
SELECT e.name, d.department_name
FROM employees e
LEFT JOIN departments d ON e.dept_id = d.dept_id;

-- RIGHT JOIN - all departments, even without employees
SELECT e.name, d.department_name
FROM employees e
RIGHT JOIN departments d ON e.dept_id = d.dept_id;
```

Deep Insight:
- **INNER JOIN**: Excludes records without matches, smaller result set
- **LEFT JOIN**: Includes all left table records, larger result set with NULLs for non-matches
- **Performance**: INNER JOIN is typically faster due to smaller result set
- **Use Cases**: INNER for strict relationships, LEFT for optional relationships
- **NULL Handling**: LEFT JOIN produces NULL values for non-matching right table columns

## 14) What's the difference between `UNION` and `UNION ALL`?

Concept:
UNION removes duplicate rows and sorts results, while UNION ALL keeps all rows including duplicates and doesn't sort.

Example:
```sql
-- UNION - removes duplicates, sorts results
SELECT name FROM employees
UNION
SELECT name FROM contractors;

-- UNION ALL - keeps all rows, no sorting
SELECT name FROM employees
UNION ALL
SELECT name FROM contractors;

-- UNION with different columns
SELECT name, 'Employee' as type FROM employees
UNION
SELECT name, 'Contractor' as type FROM contractors;
```

Deep Insight:
- **UNION**: Eliminates duplicates, sorts results, slower performance
- **UNION ALL**: Preserves duplicates, no sorting, faster performance
- **Column Matching**: All SELECT statements must have same number of columns with compatible types
- **Use Cases**: UNION for unique results, UNION ALL for performance when duplicates are acceptable
- **Performance**: UNION ALL is significantly faster as it doesn't need to remove duplicates

## 15) What is a subquery, and what's the difference between correlated and non-correlated subqueries?

Concept:
A subquery is a query nested inside another query. Non-correlated subqueries execute independently, while correlated subqueries reference columns from the outer query.

Example:
```sql
-- Non-correlated subquery
SELECT name, salary
FROM employees
WHERE salary > (SELECT AVG(salary) FROM employees);

-- Correlated subquery
SELECT e1.name, e1.salary
FROM employees e1
WHERE e1.salary > (SELECT AVG(e2.salary) FROM employees e2 WHERE e2.department_id = e1.department_id);
```

Deep Insight:
- **Non-correlated**: Executes once, independent of outer query, better performance
- **Correlated**: Executes once for each row of outer query, can be slower
- **Execution Order**: Non-correlated runs first, correlated runs for each outer row
- **Use Cases**: Non-correlated for simple comparisons, correlated for row-specific conditions
- **Performance**: Non-correlated is generally faster, but correlated provides more flexibility

## 16) What is a Common Table Expression (CTE), and when would you use one?

Concept:
A CTE is a temporary named result set that exists only for the duration of a single query, useful for complex queries and recursive operations.

Example:
```sql
-- Simple CTE
WITH high_earners AS (
    SELECT name, salary, dept_id
    FROM employees
    WHERE salary > 75000
)
SELECT h.name, h.salary, d.department_name
FROM high_earners h
JOIN departments d ON h.dept_id = d.dept_id
ORDER BY h.salary DESC;
```

Deep Insight:
- **Temporary Scope**: CTE exists only for the duration of the query that follows it
- **Readability**: Makes complex queries more readable and maintainable
- **Recursive**: Can reference itself for hierarchical data processing
- **Multiple CTEs**: Can define multiple CTEs in a single query
- **Performance**: Generally better than subqueries for complex logic

## 17) What's the difference between a CTE and a temporary table?

Concept:
CTEs exist only for the duration of a single query and cannot be referenced multiple times, while temporary tables persist for the session and can be referenced multiple times.

Example:
```sql
-- CTE - single use
WITH sales_summary AS (
    SELECT product_id, SUM(quantity) as total_sold
    FROM sales
    GROUP BY product_id
)
SELECT p.product_name, s.total_sold
FROM sales_summary s
JOIN products p ON s.product_id = p.product_id
WHERE s.total_sold > 100;

-- Temporary table - multiple uses
CREATE TEMPORARY TABLE temp_sales_summary AS
SELECT product_id, SUM(quantity) as total_sold
FROM sales
GROUP BY product_id;

-- Can reference multiple times
SELECT * FROM temp_sales_summary WHERE total_sold > 100;
SELECT COUNT(*) FROM temp_sales_summary;
```

Deep Insight:
- **Scope**: CTE is query-scoped, temp table is session-scoped
- **Reusability**: CTE can't be referenced multiple times, temp table can
- **Performance**: CTE is recalculated each time, temp table is materialized
- **Storage**: CTE doesn't use disk space, temp table uses temporary storage
- **Use Cases**: CTE for single-use complex logic, temp table for multiple operations

## 18) How do you find duplicate records in a table?

Concept:
Use GROUP BY with HAVING COUNT(*) > 1 to find duplicate records, or window functions like ROW_NUMBER() to identify and remove duplicates.

Example:
```sql
-- Find duplicate records by name
SELECT name, COUNT(*) as duplicate_count
FROM employees
GROUP BY name
HAVING COUNT(*) > 1;

```

Deep Insight:
- **GROUP BY Method**: Simple and effective for finding duplicate groups
- **Window Functions**: More flexible for complex duplicate detection logic
- **Performance**: GROUP BY is faster for simple cases, window functions for complex scenarios
- **Deletion Strategy**: Always backup before deleting duplicates
- **Prevention**: Use UNIQUE constraints to prevent duplicates at the database level

## 19) How would you fetch the **second-highest salary** from an Employee table?

Concept:
Use window functions like ROW_NUMBER() or DENSE_RANK(), or subqueries with LIMIT/OFFSET to find the second-highest salary.

Example:
```sql
-- Using ROW_NUMBER()
SELECT salary
FROM (
    SELECT salary, ROW_NUMBER() OVER (ORDER BY salary DESC) as rn
    FROM employees
) ranked
WHERE rn = 2;

-- Using DENSE_RANK() (handles ties differently)
SELECT salary
FROM (
    SELECT salary, DENSE_RANK() OVER (ORDER BY salary DESC) as dr
    FROM employees
) ranked
WHERE dr = 2;

-- Using subquery with LIMIT/OFFSET
SELECT salary
FROM employees
ORDER BY salary DESC
LIMIT 1 OFFSET 1;
```

Deep Insight:
- **ROW_NUMBER()**: Assigns unique sequential numbers, skips ranks for ties
- **DENSE_RANK()**: Assigns ranks without gaps, same rank for ties
- **RANK()**: Assigns ranks with gaps for ties
- **Performance**: Window functions are generally more efficient than subqueries
- **Edge Cases**: Handle cases where there might be fewer than 2 distinct salaries

## 20) How do you implement **pagination** in SQL (using `LIMIT/OFFSET`, `ROW_NUMBER()`, or `FETCH NEXT`)?

Concept:
Pagination divides large result sets into smaller pages using LIMIT/OFFSET for simple cases, or ROW_NUMBER() for more complex scenarios with consistent ordering.

Example:
```sql
-- Simple pagination with LIMIT/OFFSET
SELECT name, salary
FROM employees
ORDER BY salary DESC
LIMIT 10 OFFSET 20;  -- Page 3, 10 records per page

```

Deep Insight:
- **LIMIT/OFFSET**: Simple but can be slow on large datasets with high offsets
- **ROW_NUMBER()**: More consistent for complex sorting and filtering scenarios
- **FETCH NEXT**: Modern SQL standard, more readable than LIMIT/OFFSET
- **Performance**: Use indexed columns for ORDER BY to improve pagination performance
- **Consistency**: ROW_NUMBER() ensures consistent results even with data changes
