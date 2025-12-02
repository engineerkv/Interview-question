<div align="center">

**[← Previous: README](../README.md)** | **[Next: Querying & Joins →](2%29%20Querying%20%26%20Joins.md)**

</div>

# 🗄️ 1. SQL Fundamentals (Q1–10)

---

## Q1. 🗄️ SQL and what it stands for

SQL stands for Structured Query Language - it's a standard language for managing relational databases with four main sublanguages: DDL creates and modifies database structure (CREATE, ALTER, DROP), DML manages data (SELECT, INSERT, UPDATE, DELETE), DCL controls access (GRANT, REVOKE), and TCL manages transactions (COMMIT, ROLLBACK, SAVEPOINT). Standard language for managing relational databases, enables data manipulation and structure management.

- **Trade-offs**: SQL follows ANSI standards but each RDBMS adds proprietary extensions, so code isn't always portable—features like LIMIT vs TOP or window functions vary by database version.

Example:

```sql
-- DDL: Create table structure
CREATE TABLE employees (
    id INT PRIMARY KEY,
    name VARCHAR(100) NOT NULL,
    salary DECIMAL(10,2)
);

-- DML: Insert data
INSERT INTO employees VALUES (1, 'John', 50000);

-- TCL: Transaction control
BEGIN TRANSACTION;
UPDATE employees SET salary = 55000 WHERE id = 1;
COMMIT;

```

---

## Q2. 🗄️ Difference between SQL and MySQL/PostgreSQL/SQL Server

SQL is the standard language specification, while MySQL, PostgreSQL, and SQL Server are specific database management systems (RDBMS) that implement SQL with their own extensions and features. Each RDBMS adds proprietary syntax, data types, and optimizations on top of the SQL standard.

- **Trade-offs**: ANSI SQL provides common syntax across databases, but each RDBMS has different performance characteristics, feature sets, and syntax quirks—LIMIT vs TOP, different function names, and advanced features like window functions vary by database version.

Example:

```sql
-- Standard SQL (works across most databases)
SELECT name, salary FROM employees WHERE salary > 50000;

-- MySQL specific
SELECT name, salary FROM employees WHERE salary > 50000 LIMIT 10;

-- SQL Server specific
SELECT TOP 10 name, salary FROM employees WHERE salary > 50000;

```

---

## Q3. 🗄️ Database schema

A database schema is the logical structure that defines how data is organized, including tables, views, indexes, constraints, and relationships between database objects. It provides namespace separation and logical grouping of related objects.

- **Trade-offs**: Schemas provide security boundaries with different access permissions and make object management easier, but they can complicate naming and require schema.object_name references—they're great for multi-tenancy where multiple applications share the same database safely.

Example:

```sql
-- Create a database schema
CREATE SCHEMA hr;

-- Create tables within the schema
CREATE TABLE hr.employees (
    employee_id INT PRIMARY KEY,
    name VARCHAR(100),
    salary DECIMAL(10,2)
);

```

---

## Q4. 🤔 Difference between a table and a view

A table stores actual data physically, while a view is a virtual table based on the result of a SQL query that doesn't store data but provides a way to access and manipulate data from underlying tables. Views store only the query definition, not the data itself.

- **Trade-offs**: Views simplify complex queries and provide security by restricting access to specific columns or rows, but they don't improve performance by themselves—they can be updated only if they meet specific criteria (single table, no aggregates), and complex views can actually slow down queries.

Example:

```sql
-- Create a table (stores actual data)
CREATE TABLE employees (
    id INT PRIMARY KEY,
    name VARCHAR(100),
    department_id INT,
    salary DECIMAL(10,2)
);

-- Create a view (virtual table)
CREATE VIEW high_earners AS
SELECT id, name, salary FROM employees WHERE salary > 50000;

```

---

## Q5. 🗄️ Constraints in SQL and examples

Constraints are rules applied to table columns to ensure data integrity, consistency, and validity by restricting the type of data that can be stored. NOT NULL prevents NULL values, CHECK validates against conditions, DEFAULT provides fallback values, UNIQUE ensures uniqueness, and PRIMARY KEY combines NOT NULL and UNIQUE.

- **Trade-offs**: Constraints enforce data quality at the database level and prevent invalid data, but they can slow down INSERT/UPDATE operations and make schema changes more complex—use them to catch errors early, but balance strictness with flexibility.

Example:

```sql
CREATE TABLE products (
    product_id INT PRIMARY KEY,
    product_name VARCHAR(100) NOT NULL,
    price DECIMAL(10,2) CHECK (price > 0),
    category VARCHAR(50) DEFAULT 'General',
    email VARCHAR(100) UNIQUE
);

```

---

## Q6. 🤔 Difference between primary key and foreign key

Primary Key uniquely identifies each row and cannot be NULL (only one per table), Foreign Key references another table's primary key to maintain referential integrity, and Unique Key ensures uniqueness but allows NULL values (multiple allowed per table). Primary and unique keys automatically create indexes for performance.

- **Trade-offs**: Primary keys create clustered indexes automatically which speeds up lookups, but composite primary keys can affect join performance. Foreign keys maintain data consistency but can slow down inserts and require careful cascade rules. Unique keys provide flexibility but can allow one NULL value which might not be what you want.

Example:

```sql
CREATE TABLE departments (
    dept_id INT PRIMARY KEY,           -- Primary Key
    dept_name VARCHAR(100) NOT NULL,
    email VARCHAR(100) UNIQUE          -- Unique Key
);

CREATE TABLE employees (
    emp_id INT PRIMARY KEY,
    name VARCHAR(100),
    dept_id INT,
    FOREIGN KEY (dept_id) REFERENCES departments(dept_id)  -- Foreign Key
);

```

---

## Q7. 🔧 Unique constraint and how it differs from primary key

Composite keys are primary keys made up of multiple columns when no single column can uniquely identify a row, but a combination of columns can. They often represent natural business relationships, but column order matters for query performance.

- **Trade-offs**: Composite keys are natural for relationships like order_items (order_id + product_id), but they can affect join performance and make foreign key references more complex—sometimes artificial single-column surrogate keys are preferred for performance, even though they're less intuitive.

Example:

```sql
-- Order items table - no single column can uniquely identify a row
CREATE TABLE order_items (
    order_id INT,
    product_id INT,
    quantity INT NOT NULL,
    price DECIMAL(10,2),
    PRIMARY KEY (order_id, product_id)  -- Composite key
);

```

---

## Q8. 💡 Composite key

DELETE removes specific rows and can be rolled back (triggers fire, can use WHERE clause), TRUNCATE removes all rows quickly but cannot be rolled back (no triggers, table-level operation), and DROP removes the entire table structure and data permanently. TRUNCATE is fastest for removing all data, DELETE is slowest for large datasets.

- **Trade-offs**: DELETE gives you control with WHERE clauses and transaction support, but it's slow for large datasets because it's row-by-row. TRUNCATE is much faster and immediately frees space, but you can't roll it back and it doesn't fire triggers. DROP is irreversible—use it only when you're sure you want to remove everything.

Example:

```sql
-- DELETE - removes specific rows, can be rolled back
DELETE FROM employees WHERE department_id = 5;
DELETE FROM employees WHERE salary < 30000;

-- TRUNCATE - removes all rows, faster than DELETE
TRUNCATE TABLE temp_data;

-- DROP - removes entire table structure
DROP TABLE old_table;

```

---

## Q9. 🤔 Difference between DELETE, TRUNCATE, and DROP

Aliases provide temporary names for tables or columns, making queries more readable, enabling shorter references, and allowing for self-joins and complex queries. They're essential for joining a table with itself and preventing ambiguity when multiple tables have the same column names.

- **Trade-offs**: Aliases make complex queries more readable and maintainable, and shorter aliases can slightly improve query performance, but use meaningful aliases that reflect table purpose (like 'e' for employees) rather than random letters—clarity matters more than saving a few characters.

Example:

```sql
-- Column aliases
SELECT 
    employee_id AS emp_id,
    first_name AS fname,
    last_name AS lname,
    salary * 12 AS annual_salary
FROM employees;

-- Table aliases for self-join
SELECT 
    e1.employee_name AS employee,
    e2.employee_name AS manager
FROM employees e1
LEFT JOIN employees e2 ON e1.manager_id = e2.employee_id;

```

---

## Q10. 🗄️ Aliases in SQL and how to use them

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

<div align="center">

**[← Previous: README](../README.md)** | **[Next: Querying & Joins →](2%29%20Querying%20%26%20Joins.md)**

</div>

