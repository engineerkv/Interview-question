---
sidebar_label: "Fundamentals & Basics"
---
# 🗄️ 1. Fundamentals & Basics (Q1–10)

> **Reviewed:** 2026-09 · Modernized; legacy topics are labeled.

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

-- MySQL / PostgreSQL / SQLite
SELECT name, salary FROM employees WHERE salary > 50000 LIMIT 10;

-- SQL standard (PostgreSQL, Oracle 12c+, SQL Server 2012+ with ORDER BY ... OFFSET)
SELECT name, salary FROM employees WHERE salary > 50000
ORDER BY salary DESC FETCH FIRST 10 ROWS ONLY;

-- SQL Server specific
SELECT TOP 10 name, salary FROM employees WHERE salary > 50000;

```

---

## Q3. 🗄️ Database schema

A database schema is the logical structure that defines how data is organized, including tables, views, indexes, constraints, and relationships between database objects. It provides namespace separation and logical grouping of related objects.

- **Trade-offs**: Schemas provide security boundaries with different access permissions and make object management easier, but these can complicate naming and require schema.object_name references—these are great for multi-tenancy where multiple applications share the same database safely.

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

- **Trade-offs**: Views simplify complex queries and provide security by restricting access to specific columns or rows, but these don't improve performance by themselves—these can be updated only if these meet specific criteria (single table, no aggregates), and complex views can actually slow down queries.

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

- **Trade-offs**: Constraints enforce data quality at the database level and prevent invalid data, but these can slow down INSERT/UPDATE operations and make schema changes more complex—use them to catch errors early, but balance strictness with flexibility.

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

- **Trade-offs**: Primary keys always get a unique index; in SQL Server (by default) and MySQL InnoDB that index is also the clustered index, while PostgreSQL stores tables as heaps and has no persistent clustered index. Composite primary keys can affect join performance. Foreign keys maintain data consistency but can slow down inserts and require careful cascade rules - and most databases (PostgreSQL, SQL Server) do *not* index the referencing column automatically, so add an index on the foreign key column yourself (MySQL InnoDB does create one). Unique keys allow NULLs; how many depends on the database (see Q7).

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

A UNIQUE constraint guarantees that no two rows share the same value (or combination of values) in the constrained columns, just like a primary key - but a table can have many UNIQUE constraints and only one primary key, and UNIQUE columns may contain NULLs. The primary key is the row's main identity (what foreign keys usually reference); UNIQUE constraints protect other business keys like `email` or `(tenant_id, slug)`.

- **Trade-offs**: Both are enforced with a unique index, so both speed up lookups and add write overhead. NULL handling differs by database: PostgreSQL, MySQL and Oracle treat NULLs as distinct, so a UNIQUE column can hold many NULLs (PostgreSQL 15+ adds `UNIQUE NULLS NOT DISTINCT` to allow only one); SQL Server allows just one NULL in a UNIQUE constraint unless you use a filtered unique index. Foreign keys can reference either a primary key or a UNIQUE constraint.

Example:

```sql
CREATE TABLE users (
    user_id   BIGINT GENERATED ALWAYS AS IDENTITY PRIMARY KEY, -- one per table, NOT NULL
    email     VARCHAR(255) NOT NULL UNIQUE,                    -- business key
    tenant_id INT NOT NULL,
    username  VARCHAR(50),
    CONSTRAINT uq_tenant_username UNIQUE (tenant_id, username) -- composite unique
);

-- PostgreSQL: case-insensitive uniqueness via a unique expression index
CREATE UNIQUE INDEX uq_users_email_lower ON users (lower(email));
```

---

## Q8. 💡 Composite key

Composite keys are primary keys made up of multiple columns when no single column can uniquely identify a row, but a combination of columns can. They often represent natural business relationships, but column order matters for query performance.

- **Trade-offs**: Composite keys are natural for relationships like order_items (order_id + product_id), but these can affect join performance and make foreign key references more complex—sometimes artificial single-column surrogate keys are preferred for performance, even though these are less intuitive.

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

## Q9. 🤔 Difference between DELETE, TRUNCATE, and DROP

DELETE removes specific rows and can be rolled back (triggers fire, can use WHERE clause), TRUNCATE removes all rows quickly as a table-level operation (row-level DELETE triggers don't fire), and DROP removes the entire table structure and data. TRUNCATE is fastest for removing all data, DELETE is slowest for large datasets.

- **Trade-offs**: DELETE gives you control with WHERE clauses and transaction support, but it's slow for large datasets because it's row-by-row. TRUNCATE is much faster and frees space immediately. Whether TRUNCATE can be rolled back depends on the database: in **PostgreSQL** and **SQL Server** it is transactional and can be rolled back inside an explicit transaction; in **MySQL** and **Oracle** it is DDL with an implicit commit, so it can't. TRUNCATE also fails if other tables reference this one via foreign keys (PostgreSQL has `TRUNCATE ... CASCADE`). DROP is effectively irreversible outside a transaction (PostgreSQL even allows transactional DROP)—use it only when you're sure.

Example:

```sql
-- DELETE - removes specific rows, can be rolled back
DELETE FROM employees WHERE department_id = 5;
DELETE FROM employees WHERE salary < 30000;

-- TRUNCATE - removes all rows, faster than DELETE
TRUNCATE TABLE temp_data;

-- PostgreSQL / SQL Server: TRUNCATE can be rolled back in a transaction
BEGIN;
TRUNCATE TABLE temp_data;
ROLLBACK; -- rows are back

-- DROP - removes entire table structure
DROP TABLE old_table;

```

---

## Q10. 🗄️ Aliases in SQL and how to use them

Aliases provide temporary names for tables or columns, making queries more readable, enabling shorter references, and allowing for self-joins and complex queries. These are essential for joining a table with itself and preventing ambiguity when multiple tables have the same column names.

- **Trade-offs**: Aliases make complex queries more readable and maintainable (they have no effect on query performance), but use meaningful aliases that reflect table purpose (like 'e' for employees) rather than random letters—clarity matters more than saving a few characters.

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
