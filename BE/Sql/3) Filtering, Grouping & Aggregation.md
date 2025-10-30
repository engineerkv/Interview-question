# 3) Filtering, Grouping & Aggregation (Q21–30)

## 21) What's the difference between `WHERE` and `HAVING` clauses?

Concept:
WHERE filters rows before grouping, while HAVING filters groups after GROUP BY. WHERE cannot use aggregate functions, HAVING can.

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
```

Deep Insight:

- Execution Order: WHERE executes before GROUP BY, HAVING executes after GROUP BY
- Aggregate Functions: WHERE cannot use aggregate functions, HAVING can use them
- Performance: WHERE is more efficient as it filters data before grouping
- Use Cases: WHERE for row-level filtering, HAVING for group-level filtering
- Combination: Can use both WHERE and HAVING in the same query

## 22) How do you handle NULL values in SQL (e.g., `IS NULL`, `COALESCE`, `NULLIF`)?

Concept:
NULL values require special handling in SQL using IS NULL for checking, COALESCE for providing defaults, and NULLIF for conditional NULL conversion.

Example:
```sql
-- Check for NULL values
SELECT name, salary
FROM employees
WHERE salary IS NULL;

-- Provide default values with COALESCE
SELECT name, COALESCE(salary, 0) as salary
FROM employees;
```

Deep Insight:

- **IS NULL/IS NOT NULL**: Use these operators to check for NULL values, not = or !=
- **COALESCE**: Returns first non-NULL value from a list, useful for defaults
- **NULLIF**: Converts specific values to NULL, useful for data cleaning
- **Aggregate Functions**: Most aggregate functions ignore NULL values automatically
- **Three-Valued Logic**: NULL comparisons return UNKNOWN, not TRUE or FALSE

## 23) What's the difference between `IN`, `EXISTS`, and `ANY` operators?

Concept:
IN checks if value exists in a list, EXISTS checks if subquery returns any rows, and ANY checks if any value in subquery meets a condition.

Example:
```sql
-- IN operator - check if value in list
SELECT name, department_id
FROM employees
WHERE department_id IN (1, 2, 3);

-- EXISTS operator - check if subquery returns rows
SELECT name, department_id
FROM employees e
WHERE EXISTS (SELECT 1 FROM departments d WHERE d.dept_id = e.department_id);

-- ANY operator - check if any value meets condition
SELECT name, salary
FROM employees
WHERE salary > ANY (SELECT salary FROM employees WHERE department_id = 1);
```

Deep Insight:

- **IN**: Best for checking against a fixed list of values, very efficient
- **EXISTS**: Best for correlated subqueries, stops at first match (short-circuit)
- **ANY**: More flexible than IN, can use comparison operators with subqueries
- **Performance**: EXISTS is often faster than IN for large datasets
- **NULL Handling**: IN returns UNKNOWN if list contains NULL, EXISTS ignores NULLs

## 24) How do you calculate department-wise total salary using `GROUP BY`?

Concept:
Use GROUP BY with department column and SUM() aggregate function to calculate total salary per department.

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

Deep Insight:

- **GROUP BY**: Groups rows with same values in specified columns
- **Aggregate Functions**: SUM, COUNT, AVG, MIN, MAX work on grouped data
- **SELECT Columns**: Non-aggregate columns in SELECT must be in GROUP BY
- **Performance**: GROUP BY can be expensive, proper indexing helps
- **NULL Handling**: GROUP BY treats NULL values as a single group

## 25) How do you filter groups based on aggregate conditions (`HAVING COUNT(*) > 1`)?

Concept:
Use HAVING clause after GROUP BY to filter groups based on aggregate function results, unlike WHERE which filters individual rows.

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

Deep Insight:

- **HAVING vs WHERE**: HAVING filters groups, WHERE filters individual rows
- **Aggregate Functions**: HAVING can use aggregate functions, WHERE cannot
- **Execution Order**: HAVING executes after GROUP BY and aggregate calculations
- **Performance**: HAVING can be expensive as it processes grouped data
- **Multiple Conditions**: Can combine multiple conditions with AND/OR in HAVING

## 26) How do you use `CASE` expressions for conditional logic?

Concept:
CASE expressions provide conditional logic similar to if-else statements, useful for data transformation and conditional aggregation.

Example:
```sql
-- Simple CASE expression
SELECT name, salary,
       CASE 
           WHEN salary > 80000 THEN 'High'
           WHEN salary > 50000 THEN 'Medium'
           ELSE 'Low'
       END as salary_category
FROM employees;
```

Deep Insight:

- **Simple CASE**: Compares expression to multiple values, like switch statement
- **Searched CASE**: Evaluates multiple conditions, like if-else chain
- **Aggregation**: CASE is powerful for conditional counting and summing
- **Data Transformation**: Useful for creating derived columns and categories
- **Performance**: CASE expressions are evaluated for each row

## 27) What are **window functions**, and how do they differ from aggregate functions?

Concept:
Window functions perform calculations across a set of rows related to the current row, while aggregate functions collapse rows into a single result.

Example:
```sql
-- Window functions - keep all rows
SELECT name, salary, department_id,
       ROW_NUMBER() OVER (ORDER BY salary DESC) as salary_rank,
       AVG(salary) OVER (PARTITION BY department_id) as dept_avg_salary,
       SUM(salary) OVER (ORDER BY salary ROWS UNBOUNDED PRECEDING) as running_total
FROM employees;
```

Deep Insight:

- **Row Preservation**: Window functions keep all rows, aggregate functions reduce rows
- **OVER Clause**: Required for window functions, defines the window frame
- **PARTITION BY**: Divides rows into groups for window calculations
- **ORDER BY**: Defines ordering within window frame
- **Frame Specification**: ROWS/RANGE defines which rows to include in calculation

## 28) Explain practical use cases of `ROW_NUMBER`, `RANK`, and `DENSE_RANK`.

Concept:
ROW_NUMBER assigns unique sequential numbers, RANK assigns ranks with gaps for ties, and DENSE_RANK assigns ranks without gaps for ties.

Example:
```sql
-- ROW_NUMBER - unique sequential numbers
SELECT name, salary,
       ROW_NUMBER() OVER (ORDER BY salary DESC) as row_num
FROM employees;

-- RANK - ranks with gaps for ties
SELECT name, salary,
       RANK() OVER (ORDER BY salary DESC) as rank_num
FROM employees;

-- DENSE_RANK - ranks without gaps for ties
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

Deep Insight:

- **ROW_NUMBER**: Always unique, no ties, useful for pagination and top-N queries
- **RANK**: Same rank for ties, skips next ranks, useful for competition rankings
- **DENSE_RANK**: Same rank for ties, no gaps, useful for percentile calculations
- **PARTITION BY**: Essential for ranking within groups (departments, categories)
- **Performance**: Window functions can be expensive on large datasets

## 29) What's the difference between `LEAD()` and `LAG()` functions?

Concept:
LEAD() accesses data from following rows, while LAG() accesses data from preceding rows in the result set, both useful for comparing current row with adjacent rows.

Example:
```sql
-- LAG - access previous row data
SELECT name, salary,
       LAG(salary) OVER (ORDER BY salary) as previous_salary,
       salary - LAG(salary) OVER (ORDER BY salary) as salary_difference
FROM employees
ORDER BY salary;
```

Deep Insight:

- **LEAD**: Looks forward to next rows, useful for forecasting and gap analysis
- **LAG**: Looks backward to previous rows, useful for trend analysis and comparisons
- **Offset Parameter**: Can specify how many rows ahead/behind to look
- **Default Value**: Can provide default value when no previous/next row exists
- **Use Cases**: Time series analysis, calculating differences, finding patterns

## 30) What's a **pivot table**, and how can you create one in SQL?

Concept:
A pivot table transforms rows into columns, converting data from long format to wide format, useful for creating cross-tabulations and summary reports.

Example:
```sql
-- Using CASE statements for pivot
SELECT 
    department_id,
    SUM(CASE WHEN EXTRACT(YEAR FROM hire_date) = 2020 THEN 1 ELSE 0 END) as hires_2020,
    SUM(CASE WHEN EXTRACT(YEAR FROM hire_date) = 2021 THEN 1 ELSE 0 END) as hires_2021,
    SUM(CASE WHEN EXTRACT(YEAR FROM hire_date) = 2022 THEN 1 ELSE 0 END) as hires_2022
FROM employees
GROUP BY department_id;
```

Deep Insight:

- **CASE Method**: Universal approach using CASE statements with GROUP BY
- **PIVOT Operator**: Database-specific syntax (SQL Server, Oracle) for cleaner code
- **Dynamic Pivoting**: Requires dynamic SQL when column values are unknown
- **Use Cases**: Cross-tabulations, summary reports, data analysis
- **Performance**: Pivot operations can be expensive on large datasets
