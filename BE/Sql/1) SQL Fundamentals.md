# 1) SQL Fundamentals (Q1–10)

## 1) What is SQL, and what are its main sublanguages (DDL, DML, DCL, TCL)?

Concept:
SQL (Structured Query Language) is a standard language for managing relational databases with four main sublanguages that handle different aspects of database operations.

Example:
```sql
-- DDL: Create table structure
CREATE TABLE employees (
    id INT PRIMARY KEY,
    name VARCHAR(100) NOT NULL,
    salary DECIMAL(10,2)
);
```

Deep Insight:
- **DDL (Data Definition Language)**: Creates and modifies database structure (CREATE, ALTER, DROP, TRUNCATE)
- **DML (Data Manipulation Language)**: Manages data within tables (SELECT, INSERT, UPDATE, DELETE)
- **DCL (Data Control Language)**: Controls access and permissions (GRANT, REVOKE, DENY)
- **TCL (Transaction Control Language)**: Manages transactions (COMMIT, ROLLBACK, SAVEPOINT)
- **Standard Compliance**: SQL follows ANSI standards but each RDBMS has proprietary extensions

## 2) What is the difference between SQL and MySQL/PostgreSQL/SQL Server?

Concept:
SQL is the standard language specification, while MySQL, PostgreSQL, and SQL Server are specific database management systems (RDBMS) that implement SQL with their own extensions and features.

Example:
```sql
-- Standard SQL (works across most databases)
SELECT name, salary FROM employees WHERE salary > 50000;

-- MySQL specific
SELECT name, salary FROM employees WHERE salary > 50000 LIMIT 10;

```

Deep Insight:
- **SQL Standard**: ANSI SQL provides common syntax and features across databases
- **RDBMS Implementations**: Each database system adds proprietary features and optimizations
- **Syntax Differences**: LIMIT vs TOP, different data types, and function names
- **Performance Variations**: Each RDBMS has different query optimization strategies
- **Feature Sets**: Advanced features like window functions, CTEs vary by database version

## 3) What is a database schema?

Concept:
A database schema is the logical structure that defines how data is organized, including tables, views, indexes, constraints, and relationships between database objects.

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

Deep Insight:
- **Logical Organization**: Schema provides namespace separation and logical grouping of related objects
- **Security Boundary**: Schemas can have different access permissions and security policies
- **Object Management**: Tables, views, functions, and procedures are organized within schemas
- **Naming Convention**: Schema.object_name provides unique identification of database objects
- **Multi-tenancy**: Schemas enable multiple applications to share the same database safely

## 4) What is the difference between a table and a view?

Concept:
A table stores actual data physically, while a view is a virtual table based on the result of a SQL query that doesn't store data but provides a way to access and manipulate data from underlying tables.

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

Deep Insight:
- **Data Storage**: Tables store physical data, views store only the query definition
- **Performance**: Views don't improve performance by themselves, but can simplify complex queries
- **Security**: Views can restrict access to specific columns or rows of underlying tables
- **Maintainability**: Views provide abstraction layer, making schema changes easier to manage
- **Updatability**: Views can be updated only if they meet specific criteria (single table, no aggregates, etc.)

## 5) What are constraints in SQL (NOT NULL, CHECK, DEFAULT, etc.)?

Concept:
Constraints are rules applied to table columns to ensure data integrity, consistency, and validity by restricting the type of data that can be stored.

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

Deep Insight:
- **NOT NULL**: Prevents NULL values, ensures required data is always provided
- **CHECK**: Validates data against specified conditions, maintains business rules
- **DEFAULT**: Provides fallback values when no value is specified during insertion
- **UNIQUE**: Ensures uniqueness of values, can allow one NULL value
- **PRIMARY KEY**: Combines NOT NULL and UNIQUE, uniquely identifies each row
- **FOREIGN KEY**: Maintains referential integrity between related tables

## 6) What is the difference between a **Primary Key**, **Foreign Key**, and **Unique Key**?

Concept:
Primary Key uniquely identifies each row and cannot be NULL, Foreign Key references another table's primary key, and Unique Key ensures uniqueness but allows NULL values.

Example:
```sql
CREATE TABLE departments (
    dept_id INT PRIMARY KEY,           -- Primary Key
    dept_name VARCHAR(100) NOT NULL,
    email VARCHAR(100) UNIQUE          -- Unique Key
);

```

Deep Insight:
- **Primary Key**: Only one per table, cannot be NULL, creates clustered index automatically
- **Foreign Key**: Maintains referential integrity, can be NULL, references primary key of another table
- **Unique Key**: Multiple allowed per table, can have one NULL value, creates non-clustered index
- **Referential Integrity**: Foreign keys ensure data consistency across related tables
- **Indexing**: Primary and unique keys automatically create indexes for performance

## 7) What are **composite keys**, and when should you use them?

Concept:
Composite keys are primary keys made up of multiple columns when no single column can uniquely identify a row, but a combination of columns can.

Example:
```sql
-- Order items table - no single column can uniquely identify a row
CREATE TABLE order_items (
    order_id INT,
    product_id INT,
    quantity INT NOT NULL,
    price DECIMAL(10,2),
    PRIMARY KEY (order_id, product_id)
);
```

Deep Insight:
- **Natural Keys**: Composite keys often represent natural business relationships
- **Performance Impact**: Composite keys can affect join performance and index usage
- **Order Matters**: Column order in composite keys affects query performance
- **Surrogate Keys**: Sometimes artificial single-column keys are preferred for performance
- **Referential Integrity**: Foreign keys referencing composite keys must include all columns

## 8) What is the difference between `DELETE`, `TRUNCATE`, and `DROP` commands?

Concept:
DELETE removes specific rows and can be rolled back, TRUNCATE removes all rows quickly but cannot be rolled back, and DROP removes the entire table structure and data.

Example:
```sql
-- DELETE - removes specific rows, can be rolled back
DELETE FROM employees WHERE department_id = 5;
DELETE FROM employees WHERE salary < 30000;

-- TRUNCATE - removes all rows, faster than DELETE
TRUNCATE TABLE temp_data;
```

Deep Insight:
- **DELETE**: Row-by-row operation, triggers fire, can use WHERE clause, slower for large datasets
- **TRUNCATE**: Table-level operation, no triggers, removes all rows, much faster
- **DROP**: Removes table structure completely, all data and metadata lost
- **Transaction Support**: DELETE can be rolled back, TRUNCATE cannot (in most databases)
- **Performance**: TRUNCATE is fastest, DELETE is slowest for large datasets
- **Space Recovery**: TRUNCATE immediately frees space, DELETE may not

## 9) What is the purpose of **aliases** in SQL?

Concept:
Aliases provide temporary names for tables or columns, making queries more readable, enabling shorter references, and allowing for self-joins and complex queries.

Example:
```sql
-- Column aliases
SELECT 
    employee_id AS emp_id,
    first_name AS fname,
    last_name AS lname,
    salary * 12 AS annual_salary
FROM employees;
```

Deep Insight:
- **Readability**: Aliases make complex queries more readable and maintainable
- **Self-Joins**: Essential for joining a table with itself (e.g., employee-manager relationships)
- **Column Clarity**: When multiple tables have same column names, aliases prevent ambiguity
- **Query Optimization**: Shorter aliases can improve query performance slightly
- **Best Practices**: Use meaningful aliases that reflect table purpose (e.g., 'e' for employees)

## 10) What are aggregate functions (COUNT, SUM, AVG, MIN, MAX)?

Concept:
Aggregate functions perform calculations on a set of values and return a single result, commonly used with GROUP BY to analyze data across groups.

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
```

Deep Insight:
- **COUNT**: Counts rows or non-NULL values, COUNT(*) counts all rows including NULLs
- **SUM/AVG**: Work with numeric data, ignore NULL values in calculations
- **MIN/MAX**: Work with any data type, ignore NULL values
- **GROUP BY**: Aggregates are calculated for each group when using GROUP BY
- **HAVING**: Filters groups based on aggregate conditions, unlike WHERE which filters rows
- **NULL Handling**: Most aggregate functions ignore NULL values except COUNT(*)
