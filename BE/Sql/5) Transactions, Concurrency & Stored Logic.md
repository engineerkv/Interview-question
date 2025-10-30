# 5) Transactions, Concurrency & Stored Logic (Q41–50)

---

## 41) What is a transaction in SQL, and what are the **ACID properties**?

Concept:
A transaction is a sequence of operations treated as a single unit that ensures data consistency and reliability through ACID properties.

Example:
```sql
BEGIN TRANSACTION;
UPDATE accounts SET balance = balance - 1000 WHERE account_id = 1;
UPDATE accounts SET balance = balance + 1000 WHERE account_id = 2;
COMMIT;

-- If any operation fails, ROLLBACK is automatic
```

Deep Insight:
- **Atomicity**: All operations succeed or all fail (all-or-nothing)
- **Consistency**: Database remains in valid state before and after transaction
- **Isolation**: Concurrent transactions don't interfere with each other
- **Durability**: Committed changes persist even after system failure
- **Transaction Boundaries**: BEGIN, COMMIT, ROLLBACK define transaction scope

---

## 42) What's the difference between `COMMIT`, `ROLLBACK`, and `SAVEPOINT`?

Concept:
COMMIT saves all changes permanently, ROLLBACK undoes all changes since last commit, and SAVEPOINT creates a point to rollback to within a transaction.

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
```

Deep Insight:
- **COMMIT**: Makes all changes permanent and visible to other transactions
- **ROLLBACK**: Undoes all changes since the last COMMIT
- **SAVEPOINT**: Creates named points within a transaction for partial rollbacks
- **Nested Rollbacks**: Can rollback to specific savepoints without ending transaction
- **Resource Management**: Proper use prevents resource locks and improves performance

---

## 43) What are **isolation levels** (READ UNCOMMITTED, READ COMMITTED, REPEATABLE READ, SERIALIZABLE)?

Concept:
Isolation levels control how transactions interact with each other, balancing data consistency with performance by controlling what data changes are visible to concurrent transactions.

Example:
```sql
-- Set isolation level for current session
SET TRANSACTION ISOLATION LEVEL READ COMMITTED;

-- Or for specific transaction
BEGIN TRANSACTION ISOLATION LEVEL SERIALIZABLE;
SELECT * FROM accounts WHERE account_id = 1;
COMMIT;
```

Deep Insight:
- **READ UNCOMMITTED**: Lowest isolation, allows dirty reads, fastest performance
- **READ COMMITTED**: Prevents dirty reads, allows non-repeatable reads
- **REPEATABLE READ**: Prevents dirty and non-repeatable reads, allows phantom reads
- **SERIALIZABLE**: Highest isolation, prevents all anomalies, slowest performance
- **Trade-offs**: Higher isolation = better consistency but lower concurrency

---

## 44) What is a **deadlock**, and how can you detect and resolve it?

Concept:
A deadlock occurs when two or more transactions wait indefinitely for each other to release locks, creating a circular dependency that prevents any transaction from completing.

Example:
```sql
-- Transaction 1
BEGIN TRANSACTION;
UPDATE accounts SET balance = balance - 100 WHERE account_id = 1;
-- Waits for account 2
UPDATE accounts SET balance = balance + 100 WHERE account_id = 2;
COMMIT;

-- Transaction 2 (causes deadlock)
BEGIN TRANSACTION;
UPDATE accounts SET balance = balance - 50 WHERE account_id = 2;
UPDATE accounts SET balance = balance + 50 WHERE account_id = 1;
COMMIT;
```

Deep Insight:
- **Circular Wait**: Two or more transactions wait for each other's resources
- **Detection**: Database automatically detects and resolves deadlocks
- **Resolution**: One transaction is chosen as victim and rolled back
- **Prevention**: Always acquire locks in the same order across transactions
- **Monitoring**: Use system views to monitor lock contention and deadlock frequency

---

## 45) What are **phantom reads** and **dirty reads**, and how do isolation levels prevent them?

Concept:
Phantom reads occur when a transaction sees different sets of rows in repeated queries, while dirty reads occur when a transaction reads uncommitted data from another transaction.

Example:
```sql
-- Dirty Read Example (READ UNCOMMITTED)
-- Transaction 1
BEGIN TRANSACTION;
UPDATE accounts SET balance = 1000 WHERE account_id = 1;
-- Transaction 2 reads this uncommitted data
-- Transaction 1 rolls back, but Transaction 2 already used the data
ROLLBACK;

-- Transaction 2 (reads uncommitted data)
SELECT balance FROM accounts WHERE account_id = 1; -- Reads 1000 (dirty read)
```

Deep Insight:
- **Dirty Read**: Reading uncommitted data that may be rolled back
- **Phantom Read**: Seeing different sets of rows in repeated queries
- **Non-repeatable Read**: Same row has different values in repeated reads
- **Isolation Prevention**: Higher isolation levels prevent these anomalies
- **Performance Impact**: Preventing anomalies requires more locking and reduces concurrency

---

## 46) What's the difference between **optimistic** and **pessimistic** locking?

Concept:
Optimistic locking assumes no conflicts and checks at commit time, while pessimistic locking acquires locks immediately to prevent conflicts during transaction execution.

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

Deep Insight:
- **Optimistic**: Better for read-heavy workloads, assumes low conflict probability
- **Pessimistic**: Better for write-heavy workloads, prevents conflicts upfront
- **Conflict Resolution**: Optimistic requires retry logic, pessimistic blocks immediately
- **Performance**: Optimistic has better concurrency, pessimistic has predictable behavior
- **Use Cases**: Optimistic for web apps, pessimistic for critical financial systems

---

## 47) What is a **trigger**, and when should you use one?

Concept:
A trigger is a stored procedure that automatically executes in response to specific database events (INSERT, UPDATE, DELETE) on a table, useful for audit trails and business logic.

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

Deep Insight:
- **Automatic Execution**: Triggers fire automatically on specified events
- **Audit Trails**: Perfect for tracking data changes and maintaining history
- **Business Rules**: Enforce complex business logic at database level
- **Performance Impact**: Triggers can slow down DML operations
- **Debugging**: Can be difficult to debug and maintain, use sparingly

---

## 48) What is a **stored procedure**, and how does it differ from a function?

Concept:
A stored procedure is a precompiled collection of SQL statements that can accept parameters and return result sets, while a function returns a single value and can be used in expressions.

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
```

Deep Insight:
- **Stored Procedures**: Can return multiple result sets, support output parameters
- **Functions**: Must return a single value, can be used in SELECT statements
- **Performance**: Stored procedures are precompiled and cached for better performance
- **Security**: Both provide security benefits by encapsulating business logic
- **Maintenance**: Centralized logic makes maintenance easier but creates database dependency

---

## 49) What are the benefits and drawbacks of stored procedures for business logic?

Concept:
Stored procedures centralize business logic in the database, providing performance benefits and security, but create database dependency and can complicate application maintenance.

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

Deep Insight:
- **Benefits**: Better performance, security, centralized logic, reduced network traffic
- **Drawbacks**: Database dependency, harder to version control, limited debugging tools
- **Performance**: Precompiled and cached, faster than dynamic SQL
- **Maintenance**: Changes require database deployment, harder to test
- **Best Practices**: Use for data-intensive operations, avoid complex business logic

---

## 50) What are best practices for **query optimization** in SQL (indexes, caching, query plans, avoiding subqueries, using CTEs)?

Concept:
Query optimization involves using proper indexing, efficient query structure, avoiding performance anti-patterns, and leveraging database features to achieve optimal performance.

Example:
```sql
-- Poor query
SELECT * FROM employees e, departments d
WHERE e.department_id = d.department_id
AND e.salary > (SELECT AVG(salary) FROM employees)
ORDER BY e.name;

-- Optimized query
SELECT e.name, e.salary, d.department_name
FROM employees e
INNER JOIN departments d ON e.department_id = d.department_id
WHERE e.salary > (SELECT AVG(salary) FROM employees)
ORDER BY e.name;
```

Deep Insight:
- **Indexing**: Create indexes on frequently queried columns and join conditions
- **Query Structure**: Use INNER JOIN instead of WHERE clauses, avoid SELECT *
- **Subquery Alternatives**: Use CTEs or JOINs instead of correlated subqueries
- **Query Plans**: Use EXPLAIN/EXECUTION PLAN to identify bottlenecks
- **Caching**: Leverage query result caching and connection pooling for better performance

---
