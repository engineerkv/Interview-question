---
sidebar_label: "Filtering & Aggregation"
---
# 📊 3. Filtering & Aggregation (Q21–30)

---

## Q21. 🤔 Difference between WHERE and HAVING clauses

WHERE filters rows before grouping, while HAVING filters groups after GROUP BY. WHERE cannot use aggregate functions, HAVING can. WHERE executes before GROUP BY and is more efficient because it filters data before grouping, while HAVING executes after GROUP BY for group-level filtering.

- **Trade-offs**: WHERE is more efficient as it filters data before grouping, so use it whenever possible. HAVING is necessary when you need to filter based on aggregate results—you can use both WHERE and HAVING in the same query, with WHERE filtering rows first and HAVING filtering groups after aggregation.

Example:

```sql
-- WHERE filters individual rows
SELECT name, salary, department_id
FROM employees
WHERE salary > 50000;

-- HAVING filters groups after GROUP BY
SELECT department_id, AVG(salary) as avg_salary
FROM employees
GROUP BY department_id
HAVING AVG(salary) > 50000;

-- Using both WHERE and HAVING
SELECT department_id, AVG(salary) as avg_salary
FROM employees
WHERE salary > 30000  -- Filter rows first
GROUP BY department_id
HAVING AVG(salary) > 50000;  -- Then filter groups

```

---

## Q22. 🗄️ Handling NULL values in SQL

NULL values require special handling in SQL using IS NULL for checking (not = or !=), COALESCE for providing defaults (returns first non-NULL value), and NULLIF for conditional NULL conversion. Most aggregate functions ignore NULL values automatically, and NULL comparisons return UNKNOWN, not TRUE or FALSE.

- **Trade-offs**: Always use IS NULL/IS NOT NULL to check for NULL values—never use = or != because NULL comparisons return UNKNOWN. COALESCE is great for defaults, and NULLIF is useful for data cleaning, but remember that aggregate functions ignore NULLs which can affect calculations.

Example:

```sql
-- Check for NULL values
SELECT name, salary
FROM employees
WHERE salary IS NULL;

-- Provide default values with COALESCE
SELECT name, COALESCE(salary, 0) as salary
FROM employees;

-- NULLIF converts specific values to NULL
SELECT name, NULLIF(salary, 0) as salary  -- Converts 0 to NULL
FROM employees;

```

---

## Q23. 🤔 Difference between IN, EXISTS, and ANY operators

IN checks if value exists in a list, EXISTS checks if subquery returns any rows (stops at first match), and ANY checks if any value in subquery meets a condition. IN is best for fixed lists, EXISTS is best for correlated subqueries, and ANY is more flexible with comparison operators.

- **Trade-offs**: EXISTS is often faster than IN for large datasets because it short-circuits at the first match, while IN must check all values. IN returns UNKNOWN if the list contains NULL, but EXISTS ignores NULLs. Use IN for simple value lists, EXISTS for correlated subqueries, and ANY when you need comparison operators.

Example:

```sql
-- IN operator - check if value in list
SELECT name, department_id
FROM employees
WHERE department_id IN (1, 2, 3);

-- EXISTS operator - check if subquery returns rows (faster for large datasets)
SELECT name, department_id
FROM employees e
WHERE EXISTS (SELECT 1 FROM departments d WHERE d.dept_id = e.department_id);

-- ANY operator - check if any value meets condition
SELECT name, salary
FROM employees
WHERE salary > ANY (SELECT salary FROM employees WHERE department_id = 1);

```

---

## Q24. 🔧 GROUP BY and how to use it

Use GROUP BY with department column and SUM() aggregate function to calculate total salary per department. GROUP BY groups rows with the same values in specified columns, and all non-aggregate columns in SELECT must be in GROUP BY.

- **Trade-offs**: GROUP BY can be expensive on large datasets, so proper indexing helps. GROUP BY treats NULL values as a single group, and you can use other aggregate functions like COUNT, AVG, MIN, MAX on grouped data—just remember that non-aggregate columns in SELECT must be in GROUP BY.

Example:

```sql
-- Basic department-wise total salary
SELECT department_id, SUM(salary) as total_salary
FROM employees
GROUP BY department_id;

-- With department names using JOIN
SELECT d.department_name, SUM(e.salary) as total_salary
FROM employees e
JOIN departments d ON e.department_id = d.department_id
GROUP BY d.department_name;

```

**Related follow-up — filtering groups with HAVING:**

Use HAVING clause after GROUP BY to filter groups based on aggregate function results, unlike WHERE which filters individual rows. HAVING executes after GROUP BY and aggregate calculations, and you can combine multiple conditions with AND/OR.

- **Trade-offs**: HAVING can use aggregate functions while WHERE cannot, but HAVING can be expensive because it processes grouped data. Use WHERE to filter rows first (more efficient), then HAVING to filter groups after aggregation—this reduces the data that needs to be grouped.

Example:

```sql
-- Find departments with more than 5 employees
SELECT department_id, COUNT(*) as emp_count
FROM employees
GROUP BY department_id
HAVING COUNT(*) > 5;

-- Find departments with average salary > 60000
SELECT department_id, AVG(salary) as avg_salary
FROM employees
GROUP BY department_id
HAVING AVG(salary) > 60000;

```

---

## Q25. 🔧 Aggregate functions in SQL

Aggregate functions perform calculations on a set of values and return a single result, commonly used with GROUP BY to analyze data across groups. COUNT counts rows or non-NULL values, SUM/AVG work with numeric data, and MIN/MAX work with any data type—most ignore NULL values except COUNT(*).

- **Trade-offs**: Aggregates are powerful for analysis but can be expensive on large datasets, especially with GROUP BY. COUNT(*) counts all rows including NULLs, while COUNT(column) counts only non-NULL values—use HAVING to filter groups based on aggregate conditions, unlike WHERE which filters rows.

Example:

```sql
-- Basic aggregate functions
SELECT
    COUNT(*) AS total_employees,
    COUNT(salary) AS employees_with_salary,
    SUM(salary) AS total_payroll,
    AVG(salary) AS average_salary,
    MIN(salary) AS min_salary,
    MAX(salary) AS max_salary
FROM employees;

-- With GROUP BY
SELECT
    department_id,
    COUNT(*) AS emp_count,
    AVG(salary) AS avg_salary
FROM employees
GROUP BY department_id
HAVING COUNT(*) > 5;

```

---

## Q26. 🤔 Difference between COUNT(*) and COUNT(column_name)

__NEW_Q26__

---

## Q27. 📊 Using conditional aggregation with CASE statements

CASE expressions provide conditional logic similar to if-else statements, useful for data transformation and conditional aggregation. Simple CASE compares an expression to multiple values (like a switch statement), while searched CASE evaluates multiple conditions (like an if-else chain).

- **Trade-offs**: CASE is powerful for conditional counting and summing in aggregations, and it's great for creating derived columns and categories. The catch is CASE expressions are evaluated for each row, so these can impact performance on large datasets—use them when you need conditional logic, but be mindful of the cost.

Example:

```sql
-- Searched CASE expression (if-else chain)
SELECT name, salary,
       CASE
           WHEN salary > 80000 THEN 'High'
           WHEN salary > 50000 THEN 'Medium'
           ELSE 'Low'
       END as salary_category
FROM employees;

-- CASE in aggregation (conditional counting)
SELECT
    department_id,
    SUM(CASE WHEN salary > 50000 THEN 1 ELSE 0 END) as high_earners,
    SUM(CASE WHEN salary <= 50000 THEN 1 ELSE 0 END) as low_earners
FROM employees
GROUP BY department_id;

```

---

## Q28. 🔧 Window functions and how to use them

Window functions perform calculations across a set of rows related to the current row, while aggregate functions collapse rows into a single result. Window functions keep all rows and require an OVER clause that defines the window frame, while aggregate functions reduce rows to one per group.

- **Trade-offs**: Window functions are powerful for ranking, running totals, and comparing rows without losing detail, but these can be expensive on large datasets. PARTITION BY divides rows into groups, ORDER BY defines ordering, and ROWS/RANGE specifies which rows to include—use them when you need row-level calculations without grouping.

Example:

```sql
-- Window functions - keep all rows
SELECT name, salary, department_id,
       ROW_NUMBER() OVER (ORDER BY salary DESC) as salary_rank,
       AVG(salary) OVER (PARTITION BY department_id) as dept_avg_salary,
       SUM(salary) OVER (ORDER BY salary ROWS UNBOUNDED PRECEDING) as running_total
FROM employees;

```

---

## Q29. 🤔 Difference between ROW_NUMBER, RANK, and DENSE_RANK

ROW_NUMBER assigns unique sequential numbers (always unique, no ties), RANK assigns ranks with gaps for ties (skips next ranks), and DENSE_RANK assigns ranks without gaps for ties. ROW_NUMBER is useful for pagination and top-N queries, RANK for competition rankings, and DENSE_RANK for percentile calculations.

- **Trade-offs**: ROW_NUMBER gives you unique numbers even with ties, perfect for pagination. RANK shows ties but skips ranks (1, 2, 2, 4), while DENSE_RANK shows ties without gaps (1, 2, 2, 3). PARTITION BY is essential for ranking within groups—use ROW_NUMBER when you need unique identifiers, RANK for competition-style rankings, and DENSE_RANK when gaps don't make sense.

Example:

```sql
-- ROW_NUMBER - unique sequential numbers (useful for pagination)
SELECT name, salary,
       ROW_NUMBER() OVER (ORDER BY salary DESC) as row_num
FROM employees;

-- RANK - ranks with gaps for ties (useful for competition rankings)
SELECT name, salary,
       RANK() OVER (ORDER BY salary DESC) as rank_num
FROM employees;

-- DENSE_RANK - ranks without gaps for ties (useful for percentiles)
SELECT name, salary,
       DENSE_RANK() OVER (ORDER BY salary DESC) as dense_rank_num
FROM employees;

-- Practical use case: Top 3 employees per department
SELECT name, department_id, salary, row_num
FROM (
    SELECT name, department_id, salary,
           ROW_NUMBER() OVER (PARTITION BY department_id ORDER BY salary DESC) as row_num
    FROM employees
) ranked
WHERE row_num <= 3;

```

**Related follow-up — LEAD() and LAG():**

LEAD() accesses data from following rows (looks forward), while LAG() accesses data from preceding rows (looks backward), both useful for comparing current row with adjacent rows. You can specify an offset parameter to look multiple rows ahead/behind, and provide a default value when no previous/next row exists.

- **Trade-offs**: LAG is great for trend analysis and calculating differences (like month-over-month growth), while LEAD is useful for forecasting and gap analysis. These are perfect for time series analysis, but remember these require ORDER BY in the OVER clause—use them when you need to compare rows with their neighbors.

Example:

```sql
-- LAG - access previous row data (useful for trend analysis)
SELECT name, salary,
       LAG(salary) OVER (ORDER BY salary) as previous_salary,
       salary - LAG(salary) OVER (ORDER BY salary) as salary_difference
FROM employees
ORDER BY salary;

-- LEAD - access next row data (useful for forecasting)
SELECT name, salary,
       LEAD(salary) OVER (ORDER BY salary) as next_salary,
       LEAD(salary) OVER (ORDER BY salary) - salary as salary_increase
FROM employees
ORDER BY salary;

```

---

## Q30. 🗄️ Creating pivot tables in SQL

A pivot table transforms rows into columns, converting data from long format to wide format, useful for creating cross-tabulations and summary reports. You can use CASE statements with GROUP BY (universal approach) or the PIVOT operator (SQL Server, Oracle) for cleaner code.

- **Trade-offs**: CASE method works everywhere but is verbose, while PIVOT operator is cleaner but database-specific. Dynamic pivoting requires dynamic SQL when column values are unknown, which adds complexity. Pivot operations can be expensive on large datasets—use them for reporting and analysis, but be mindful of performance.

Example:

```sql
-- Using CASE statements for pivot (universal approach)
SELECT
    department_id,
    SUM(CASE WHEN EXTRACT(YEAR FROM hire_date) = 2020 THEN 1 ELSE 0 END) as hires_2020,
    SUM(CASE WHEN EXTRACT(YEAR FROM hire_date) = 2021 THEN 1 ELSE 0 END) as hires_2021,
    SUM(CASE WHEN EXTRACT(YEAR FROM hire_date) = 2022 THEN 1 ELSE 0 END) as hires_2022
FROM employees
GROUP BY department_id;

-- Using PIVOT operator (SQL Server, Oracle)
SELECT department_id, [2020] as hires_2020, [2021] as hires_2021, [2022] as hires_2022
FROM (
    SELECT department_id, EXTRACT(YEAR FROM hire_date) as hire_year
    FROM employees
) src
PIVOT (
    COUNT(hire_year) FOR hire_year IN ([2020], [2021], [2022])
) pvt;

```

---
