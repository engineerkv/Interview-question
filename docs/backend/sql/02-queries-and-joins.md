---
sidebar_label: "Queries & Joins"
---
# 🔍 2. Queries & Joins (Q11–20)

---

## Q11. 🗄️ Different types of JOINs in SQL

Joins combine data from multiple tables based on related columns, with different types returning different sets of matching and non-matching records. INNER JOIN returns only matching records, LEFT JOIN returns all left table records plus matches, RIGHT JOIN returns all right table records plus matches, FULL OUTER JOIN returns all records from both tables, and CROSS JOIN returns the Cartesian product (every row from first table with every row from second).

- **Trade-offs**: INNER JOIN is typically fastest due to smaller result sets, while LEFT JOIN is most common for optional relationships. RIGHT JOIN is rarely used (just flip the tables and use LEFT), and CROSS JOIN can create huge result sets—use it carefully. FULL OUTER JOIN is useful for finding mismatches but can be slow.

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

-- CROSS JOIN - Cartesian product
SELECT e.name, d.department_name
FROM employees e
CROSS JOIN departments d;

```

---

## Q12. 🤔 Difference between INNER JOIN and LEFT JOIN

INNER JOIN returns only matching records from both tables, while LEFT JOIN returns all records from the left table and matching records from the right table. INNER JOIN excludes records without matches (smaller result set), while LEFT JOIN includes all left table records with NULLs for non-matching right table columns.

- **Trade-offs**: INNER JOIN is typically faster due to smaller result sets and is best for strict relationships where you only want matching data. LEFT JOIN is most common for optional relationships where you want all records from the left table even if there's no match—use it when you need to see all employees even if they don't have a department assigned.

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

```

---

## Q13. 🔗 ⏰ Self-join and when to use it

A self-join is when a table is joined with itself, useful for finding relationships within the same table like employee-manager hierarchies. You use table aliases to reference the same table multiple times, which is perfect for organizational charts, category hierarchies, and parent-child relationships.

- **Trade-offs**: Self-joins are essential for hierarchical data but can be expensive on large tables—proper indexing on the join columns is crucial. You must use different aliases to distinguish between the two instances, and they're common for employee-manager relationships, product categories, and comment threads.

Example:

```sql
-- Find employees and their managers
SELECT
    e1.employee_name AS employee,
    e2.employee_name AS manager
FROM employees e1
LEFT JOIN employees e2 ON e1.manager_id = e2.employee_id;

```

---

## Q14. 🤔 Difference between UNION and UNION ALL

UNION removes duplicate rows, while UNION ALL keeps all rows including duplicates. To remove duplicates the database has to sort or hash the combined result, so UNION ALL is faster; use it when duplicates are acceptable or impossible. Note that neither guarantees any output order - the result of UNION may *look* sorted when the engine used a sort to de-duplicate, but only an explicit `ORDER BY` guarantees order.

- **Trade-offs**: UNION gives you unique results but is slower due to duplicate removal (sort or hash). UNION ALL is much faster and should be your default choice unless you specifically need unique results—all SELECT statements must have the same number of columns with compatible types.

Example:

```sql
-- UNION - removes duplicates (order not guaranteed without ORDER BY)
SELECT name FROM employees
UNION
SELECT name FROM contractors;

-- UNION ALL - keeps all rows, no de-duplication (faster)
SELECT name FROM employees
UNION ALL
SELECT name FROM contractors;

-- UNION with different columns
SELECT name, 'Employee' as type FROM employees
UNION
SELECT name, 'Contractor' as type FROM contractors;

```

---

## Q15. 🔧 Subqueries and how to use them

A subquery is a query nested inside another query. Non-correlated subqueries execute independently (run once, better performance), while correlated subqueries reference columns from the outer query (execute once for each row, can be slower but more flexible).

- **Trade-offs**: Non-correlated subqueries are generally faster because they execute once before the outer query, perfect for simple comparisons. Correlated subqueries provide more flexibility for row-specific conditions but can be slow on large datasets—consider rewriting them as JOINs when possible for better performance.

Example:

```sql
-- Non-correlated subquery (executes once)
SELECT name, salary
FROM employees
WHERE salary > (SELECT AVG(salary) FROM employees);

-- Correlated subquery (executes for each row)
SELECT e1.name, e1.salary
FROM employees e1
WHERE e1.salary > (SELECT AVG(e2.salary) FROM employees e2 WHERE e2.department_id = e1.department_id);

```

---

## Q16. 🤔 Difference between correlated and non-correlated subqueries

A **non-correlated** subquery doesn't reference the outer query, so it can be evaluated once and its result reused (e.g. "salary above the company average"). A **correlated** subquery references a column from the outer query, so logically it is evaluated once per outer row (e.g. "salary above *their department's* average"). That per-row model is the conceptual difference - but modern optimizers often rewrite correlated subqueries, especially `EXISTS` / `NOT EXISTS`, into semi-joins or anti-joins, so "correlated means slow" is not automatically true.

- **Trade-offs**: Non-correlated subqueries are simple and cheap when the inner result is small. Correlated subqueries express row-specific conditions naturally; `EXISTS` is often the clearest and fastest way to say "has at least one related row". When a correlated scalar subquery really runs per row, rewrite it as a JOIN to a grouped derived table, a window function, or a `LATERAL` join (PostgreSQL, MySQL 8.0.14+; `CROSS APPLY` in SQL Server). Check with `EXPLAIN` rather than guessing. Beware `NOT IN` with a subquery that can return NULL - it returns no rows; prefer `NOT EXISTS`.

Example:

```sql
-- Non-correlated: inner query runs independently
SELECT name, salary
FROM employees
WHERE salary > (SELECT AVG(salary) FROM employees);

-- Correlated: inner query references e.department_id
SELECT e.name, e.salary
FROM employees e
WHERE e.salary > (
    SELECT AVG(e2.salary) FROM employees e2
    WHERE e2.department_id = e.department_id
);

-- Same result with a window function (single pass)
SELECT name, salary
FROM (
    SELECT name, salary,
           AVG(salary) OVER (PARTITION BY department_id) AS dept_avg
    FROM employees
) t
WHERE salary > dept_avg;

-- Correlated EXISTS: usually planned as a semi-join
SELECT d.department_name
FROM departments d
WHERE EXISTS (SELECT 1 FROM employees e WHERE e.department_id = d.department_id);
```

---

## Q17. 🔧 CTEs (Common Table Expressions) and how to use them

A CTE is a temporary named result set that exists only for the duration of a single query, useful for complex queries and recursive operations. It makes complex queries more readable and maintainable, and you can define multiple CTEs in a single query.

- **Trade-offs**: CTEs improve readability for complex logic, and a CTE *can* be referenced multiple times within the single statement that defines it - but it disappears when that statement ends, unlike a temporary table. Performance depends on the engine: since PostgreSQL 12, non-recursive CTEs referenced once are inlined like subqueries (use `MATERIALIZED` / `NOT MATERIALIZED` to control this; before v12 they were always an "optimization fence"). SQL Server always inlines CTEs, and MySQL 8.0+ may merge or materialize them. `WITH RECURSIVE` is perfect for hierarchical data such as org charts, category trees or graph walks.

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

-- Recursive CTE: walk a manager hierarchy
WITH RECURSIVE reports AS (
    SELECT id, name, manager_id, 1 AS depth
    FROM employees WHERE id = 1              -- anchor: the CEO
    UNION ALL
    SELECT e.id, e.name, e.manager_id, r.depth + 1
    FROM employees e
    JOIN reports r ON e.manager_id = r.id    -- recursive step
)
SELECT * FROM reports ORDER BY depth;

-- PostgreSQL 12+: force materialization when a CTE is expensive and reused
WITH totals AS MATERIALIZED (
    SELECT dept_id, SUM(salary) AS total FROM employees GROUP BY dept_id
)
SELECT * FROM totals t1 JOIN totals t2 ON t1.total > t2.total;

```

---

## Q18. 🔧 Temporary tables and how to create them

Temporary tables are real tables that live for the session (or the transaction, with `ON COMMIT DROP` in PostgreSQL) and are visible only to the session that created them, so they can be reused across many statements. CTEs exist only for the duration of a single statement (they can be referenced several times *within* that statement). Temp tables are materialized and can have their own indexes and statistics; CTEs may be inlined or materialized depending on the engine.

- **Trade-offs**: CTEs need no cleanup and are great for readable single-statement logic. Temp tables use temporary storage and are materialized, making them better when several statements reuse an expensive intermediate result, or when you want to index it. Watch out: temp tables are session-scoped, which interacts badly with transaction-mode connection poolers like PgBouncer (the next transaction may run on a different server connection) - see Q52.

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

---

## Q19. 💡 Finding duplicate records in a table

Use GROUP BY with HAVING COUNT(*) > 1 to find duplicate records, or window functions like ROW_NUMBER() to identify and remove duplicates. GROUP BY is simple and effective for finding duplicate groups, while window functions are more flexible for complex duplicate detection logic.

- **Trade-offs**: GROUP BY is faster for simple cases, while window functions work better for complex scenarios. Always backup before deleting duplicates, and use UNIQUE constraints to prevent duplicates at the database level—prevention is better than cleanup.

Example:

```sql
-- Find duplicate records by name
SELECT name, COUNT(*) as duplicate_count
FROM employees
GROUP BY name
HAVING COUNT(*) > 1;

-- Using window functions to identify duplicates
SELECT name, ROW_NUMBER() OVER (PARTITION BY name ORDER BY id) as rn
FROM employees
WHERE ROW_NUMBER() OVER (PARTITION BY name ORDER BY id) > 1;

```

---

## Q20. 💡 Finding the second-highest salary from a table

Use window functions like ROW_NUMBER() or DENSE_RANK(), or subqueries with LIMIT/OFFSET to find the second-highest salary. ROW_NUMBER() assigns unique sequential numbers (skips ranks for ties), while DENSE_RANK() assigns ranks without gaps (same rank for ties).

- **Trade-offs**: Window functions are generally more efficient than subqueries and handle edge cases better. ROW_NUMBER() gives you a unique second row even with ties, while DENSE_RANK() treats ties as the same rank—choose based on whether you want to handle ties. Always handle cases where there might be fewer than 2 distinct salaries.

Example:

```sql
-- Using ROW_NUMBER() (unique second row, even with ties)
SELECT salary
FROM (
    SELECT salary, ROW_NUMBER() OVER (ORDER BY salary DESC) as rn
    FROM employees
) ranked
WHERE rn = 2;

-- Using DENSE_RANK() (handles ties as same rank)
SELECT salary
FROM (
    SELECT salary, DENSE_RANK() OVER (ORDER BY salary DESC) as dr
    FROM employees
) ranked
WHERE dr = 2;

-- Using subquery with LIMIT/OFFSET (simpler but less flexible)
SELECT salary
FROM employees
ORDER BY salary DESC
LIMIT 1 OFFSET 1;

```

**Related follow-up — pagination:**

Pagination divides large result sets into smaller pages using LIMIT/OFFSET for simple cases, or ROW_NUMBER() for more complex scenarios with consistent ordering. FETCH NEXT is the modern SQL standard and more readable than LIMIT/OFFSET.

- **Trade-offs**: LIMIT/OFFSET is simple but can be slow on large datasets with high offsets because it still scans skipped rows. ROW_NUMBER() ensures consistent results even with data changes and works better for complex sorting. Always use indexed columns for ORDER BY to improve pagination performance—cursor-based pagination (using WHERE with last seen value) is fastest for large datasets.

Example:

```sql
-- Simple pagination with LIMIT/OFFSET (Page 3, 10 records per page)
SELECT name, salary
FROM employees
ORDER BY salary DESC
LIMIT 10 OFFSET 20;

-- Using ROW_NUMBER() for consistent pagination
SELECT name, salary
FROM (
    SELECT name, salary, ROW_NUMBER() OVER (ORDER BY salary DESC) as rn
    FROM employees
) ranked
WHERE rn BETWEEN 21 AND 30;

-- Using FETCH NEXT (SQL standard)
SELECT name, salary
FROM employees
ORDER BY salary DESC
OFFSET 20 ROWS
FETCH NEXT 10 ROWS ONLY;

```

---
