# 🔄 5. Transactions & Concurrency (Q41–50)

---

## 📍 Navigation

<div align="center">

[← Previous: Design & Performance](04%29%20Design%20%26%20Performance.md) • [Home: Question List](question.md)

[📋 Cheatsheet](SQL%20Interview%20Cheatsheet.md)

</div>

---

---

## Q41. 🗄️ Transaction in SQL

A transaction is a sequence of operations treated as a single unit that ensures data consistency and reliability through ACID properties. Atomicity means all operations succeed or all fail (all-or-nothing), Consistency ensures the database remains in a valid state, Isolation prevents concurrent transactions from interfering, and Durability ensures committed changes persist even after system failure.

- **Trade-offs**: Transactions provide data integrity and reliability, but these can lock resources and reduce concurrency. BEGIN, COMMIT, and ROLLBACK define transaction scope—keep transactions short to minimize lock time and improve performance. The ACID properties ensure data reliability but come with performance costs.

Example:

```sql
BEGIN TRANSACTION;
UPDATE accounts SET balance = balance - 1000 WHERE account_id = 1;
UPDATE accounts SET balance = balance + 1000 WHERE account_id = 2;
COMMIT;

-- If any operation fails, ROLLBACK is automatic

```

---

## Q42. 🔄 ACID properties of transactions

COMMIT saves all changes permanently and makes them visible to other transactions, ROLLBACK undoes all changes since the last COMMIT, and SAVEPOINT creates a named point to rollback to within a transaction. You can rollback to specific savepoints without ending the transaction, which is useful for partial error recovery.

- **Trade-offs**: COMMIT makes changes permanent, so use it carefully. ROLLBACK undoes everything since the last commit, while SAVEPOINT allows partial rollbacks within a transaction. Proper use prevents resource locks and improves performance—commit frequently to release locks, but use savepoints for complex operations that might need partial rollback.

Example:

```sql
BEGIN TRANSACTION;
INSERT INTO orders (order_id, customer_id) VALUES (1, 100);
SAVEPOINT sp1;
INSERT INTO order_items (order_id, product_id) VALUES (1, 200);
-- If this fails, rollback to sp1
SAVEPOINT sp2;
INSERT INTO payments (order_id, amount) VALUES (1, 100.00);
COMMIT;

-- Or rollback to savepoint if needed
-- ROLLBACK TO sp1;

```

---

---

## Q43. 🤔 Difference between COMMIT and ROLLBACK

Isolation levels control how transactions interact with each other, balancing data consistency with performance by controlling what data changes are visible to concurrent transactions. READ UNCOMMITTED is lowest (allows dirty reads, fastest), READ COMMITTED prevents dirty reads, REPEATABLE READ prevents dirty and non-repeatable reads, and SERIALIZABLE is highest (prevents all anomalies, slowest).

- **Trade-offs**: Higher isolation means better consistency but lower concurrency and slower performance. READ COMMITTED is the default in most databases and balances consistency with performance. Use SERIALIZABLE only when you absolutely need perfect isolation—it can cause significant performance degradation and deadlocks.

Example:

```sql
-- Set isolation level for current session
SET TRANSACTION ISOLATION LEVEL READ COMMITTED;

-- Or for specific transaction
BEGIN TRANSACTION ISOLATION LEVEL SERIALIZABLE;
SELECT * FROM accounts WHERE account_id = 1;
COMMIT;

```

---

---

## Q44. 🗄️ Isolation levels in SQL

A deadlock occurs when two or more transactions wait indefinitely for each other to release locks, creating a circular dependency that prevents any transaction from completing. The database automatically detects and resolves deadlocks by choosing one transaction as a victim and rolling it back.

- **Trade-offs**: Deadlocks are automatically detected and resolved, but they cause transaction failures. Always acquire locks in the same order across transactions to prevent deadlocks—if Transaction 1 locks account A then B, Transaction 2 should also lock A then B, not B then A. Use system views to monitor lock contention and deadlock frequency.

Example:

```sql
-- Transaction 1
BEGIN TRANSACTION;
UPDATE accounts SET balance = balance - 100 WHERE account_id = 1;
-- Waits for account 2
UPDATE accounts SET balance = balance + 100 WHERE account_id = 2;
COMMIT;

-- Transaction 2 (causes deadlock - locks in different order)
BEGIN TRANSACTION;
UPDATE accounts SET balance = balance - 50 WHERE account_id = 2;
UPDATE accounts SET balance = balance + 50 WHERE account_id = 1;
COMMIT;

```

---

---

## Q45. 🔄 Deadlock and how to prevent it

Phantom reads occur when a transaction sees different sets of rows in repeated queries, while dirty reads occur when a transaction reads uncommitted data from another transaction. Non-repeatable reads happen when the same row has different values in repeated reads. Higher isolation levels prevent these anomalies but require more locking and reduce concurrency.

- **Trade-offs**: READ UNCOMMITTED allows dirty reads (fastest but risky), READ COMMITTED prevents dirty reads, REPEATABLE READ prevents dirty and non-repeatable reads, and SERIALIZABLE prevents all anomalies including phantom reads. Preventing anomalies requires more locking which reduces concurrency—choose the lowest isolation level that meets your consistency needs.

Example:

```sql
-- Dirty Read Example (READ UNCOMMITTED)
-- Transaction 1
BEGIN TRANSACTION;
UPDATE accounts SET balance = 1000 WHERE account_id = 1;
-- Transaction 2 reads this uncommitted data
-- Transaction 1 rolls back, but Transaction 2 already used the data
ROLLBACK;

-- Transaction 2 (reads uncommitted data - dirty read)
SELECT balance FROM accounts WHERE account_id = 1; -- Reads 1000 (dirty read)

```

---

---

## Q46. 🤔 Difference between optimistic and pessimistic locking

Optimistic locking assumes no conflicts and checks at commit time (using version/timestamp), while pessimistic locking acquires locks immediately to prevent conflicts during transaction execution. Optimistic is better for read-heavy workloads with low conflict probability, while pessimistic is better for write-heavy workloads.

- **Trade-offs**: Optimistic locking has better concurrency but requires retry logic when conflicts occur. Pessimistic locking blocks immediately and has predictable behavior but reduces concurrency. Use optimistic locking for web apps where conflicts are rare, and pessimistic locking for critical financial systems where you can't afford conflicts.

Example:

```sql
-- Optimistic Locking (using version/timestamp)
UPDATE products
SET name = 'New Name', version = version + 1
WHERE product_id = 1 AND version = 5; -- Check version hasn't changed

-- Pessimistic Locking (explicit locks)
SELECT * FROM products WHERE product_id = 1 FOR UPDATE;
UPDATE products SET stock = stock - 1 WHERE product_id = 1;
COMMIT;

```

---

---

## Q47. 🔧 Stored procedures and how to create them

A trigger is a stored procedure that automatically executes in response to specific database events (INSERT, UPDATE, DELETE) on a table, useful for audit trails and business logic. Triggers fire automatically on specified events and are perfect for tracking data changes and maintaining history.

- **Trade-offs**: Triggers are great for audit trails and enforcing business rules at the database level, but these can slow down DML operations and can be difficult to debug and maintain. Use them sparingly—these are hidden logic that can surprise developers, so prefer application-level logic when possible. Use triggers for audit trails, data validation, and maintaining denormalized data.

Example:

```sql
-- Create audit trigger
CREATE TRIGGER tr_employee_audit
ON employees
AFTER INSERT, UPDATE, DELETE
AS
BEGIN
    INSERT INTO employee_audit (action, employee_id, old_salary, new_salary, change_date)
    SELECT 'INSERT', inserted.id, NULL, inserted.salary, GETDATE()
    FROM inserted
    WHERE NOT EXISTS (SELECT 1 FROM deleted);

    -- Handle UPDATE operations
    INSERT INTO employee_audit (action, employee_id, old_salary, new_salary, change_date)
    SELECT 'UPDATE', inserted.id, deleted.salary, inserted.salary, GETDATE()
    FROM inserted
    INNER JOIN deleted ON inserted.id = deleted.id;
END;

```

---

---

## Q48. 💡 ⏰ Triggers and when to use them

A stored procedure is a precompiled collection of SQL statements that can accept parameters and return result sets (can return multiple result sets, support output parameters), while a function returns a single value and can be used in SELECT statements. Stored procedures are precompiled and cached for better performance.

- **Trade-offs**: Stored procedures provide better performance and security by encapsulating business logic, but they create database dependency and can be harder to version control and test. Functions are more flexible (can be used in expressions) but are more limited. Use stored procedures for complex operations, and functions for calculations and transformations.

Example:

```sql
-- Stored Procedure
CREATE PROCEDURE GetEmployeeByDepartment
    @dept_id INT,
    @min_salary DECIMAL(10,2) = 0
AS
BEGIN
    SELECT name, salary, hire_date
    FROM employees
    WHERE department_id = @dept_id
    AND salary >= @min_salary
    ORDER BY salary DESC;
END;

-- Function (returns single value)
CREATE FUNCTION GetEmployeeCount(@dept_id INT)
RETURNS INT
AS
BEGIN
    RETURN (SELECT COUNT(*) FROM employees WHERE department_id = @dept_id);
END;

```

---

---

## Q49. 🔧 User-defined functions in SQL

Stored procedures centralize business logic in the database, providing better performance (precompiled and cached), security, and reduced network traffic, but they create database dependency and can complicate application maintenance. Changes require database deployment and are harder to version control and test.

- **Trade-offs**: Stored procedures are faster than dynamic SQL and provide security benefits, but they tie your application to the database and make it harder to test and deploy. Use them for data-intensive operations and avoid putting complex business logic in stored procedures—keep business logic in application code where it's easier to test and maintain.

Example:

```sql
-- Complex business logic in stored procedure
CREATE PROCEDURE ProcessOrder
    @customer_id INT,
    @product_id INT,
    @quantity INT
AS
BEGIN
    DECLARE @price DECIMAL(10,2);
    SELECT @price = price FROM products WHERE product_id = @product_id;

    INSERT INTO orders (customer_id, product_id, quantity, total_price)
    VALUES (@customer_id, @product_id, @quantity, @price * @quantity);

    UPDATE products SET stock = stock - @quantity WHERE product_id = @product_id;
END;

```

---

---

## Q50. 🗄️ Best practices for writing efficient SQL queries

Query optimization involves using proper indexing, efficient query structure, avoiding performance anti-patterns, and leveraging database features. Create indexes on frequently queried columns and join conditions, use INNER JOIN instead of WHERE clauses, avoid SELECT *, use CTEs or JOINs instead of correlated subqueries, and use EXPLAIN/EXECUTION PLAN to identify bottlenecks.

- **Trade-offs**: Proper indexing dramatically speeds up queries but slows down writes. Use CTEs for readability and better performance than subqueries, leverage query result caching and connection pooling, and always measure with EXPLAIN before optimizing. The key is to measure first, then optimize—don't guess what's slow.

Example:

```sql
-- Poor query (SELECT *, implicit join, correlated subquery)
SELECT * FROM employees e, departments d
WHERE e.department_id = d.department_id
AND e.salary > (SELECT AVG(salary) FROM employees)
ORDER BY e.name;

-- Optimized query (specific columns, explicit JOIN, CTE)
WITH avg_salary AS (
    SELECT AVG(salary) as avg_sal FROM employees
)
SELECT e.name, e.salary, d.department_name
FROM employees e
INNER JOIN departments d ON e.department_id = d.department_id
CROSS JOIN avg_salary
WHERE e.salary > avg_salary.avg_sal
ORDER BY e.name;

```

---

<div align="center">

**[← Previous: Design & Performance](04%29%20Design%20%26%20Performance.md)** | **[Next: Question List →](question.md)**

</div>

---

---

## 📍 Navigation

<div align="center">

[← Previous: Design & Performance](04%29%20Design%20%26%20Performance.md) • [Home: Question List](question.md)

[📋 Cheatsheet](SQL%20Interview%20Cheatsheet.md)

</div>

---
