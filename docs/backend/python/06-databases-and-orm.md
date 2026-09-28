---
sidebar_label: "Databases and ORM"
description: "SQLAlchemy Core vs ORM, sessions, N+1 queries, pooling, transactions, locking, migrations, async drivers, raw SQL trade-offs and Redis from Python."
---

# Python Databases and ORM (Q67-Q76)

> **Reviewed:** 2026-09 · **Level:** Senior · **Type:** Foundational

## Q67. SQLAlchemy Core vs ORM

SQLAlchemy has two layers. Core is a SQL expression language plus engine and connection management: you build `select()`, `insert()` and `update()` statements as Python objects and get rows back. The ORM maps classes to tables, tracks object state in a Session, and handles relationships and unit of work. In SQLAlchemy 2.0 both share the same `select()` API, so you can mix them: ORM for domain writes, Core for bulk or reporting queries.

- **Trade-offs**:
  - Core: explicit, fast, close to SQL, but no identity map or relationship loading.
  - ORM: productive domain modelling, but hidden queries (lazy loading) and overhead per object.

**Example:**

```python
from sqlalchemy import ForeignKey, String, create_engine, select, insert
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column, relationship, Session

class Base(DeclarativeBase): pass

class User(Base):
    __tablename__ = "users"
    id: Mapped[int] = mapped_column(primary_key=True)
    email: Mapped[str] = mapped_column(String(255), unique=True)
    orders: Mapped[list["Order"]] = relationship(back_populates="user")

class Order(Base):
    __tablename__ = "orders"
    id: Mapped[int] = mapped_column(primary_key=True)
    user_id: Mapped[int] = mapped_column(ForeignKey("users.id"))
    total_cents: Mapped[int]
    user: Mapped[User] = relationship(back_populates="orders")

engine = create_engine("postgresql+psycopg://app@db/app")

# Core-style bulk insert
with engine.begin() as conn:
    conn.execute(insert(Order), [{"user_id": 1, "total_cents": 500}, {"user_id": 1, "total_cents": 900}])

# ORM-style query returning objects
with Session(engine) as session:
    user = session.scalars(select(User).where(User.email == "a@x.io")).one()
```

**Remember:** Core = SQL as Python; ORM = objects plus unit of work; mix them freely.

## Q68. Sessions and the unit of work pattern

A SQLAlchemy `Session` is a unit of work: it tracks new, modified and deleted objects and flushes them as SQL in the right order when you `flush()` or `commit()`. It also keeps an identity map, so the same primary key returns the same Python object within a session. Use one session per request or per task, never share one across threads or concurrent requests, and close it deterministically.

- **Trade-offs**:
  - Automatic change tracking and batching versus surprises: autoflush can emit queries before a `select`, and expired attributes after commit trigger reloads (hence `expire_on_commit=False` in async apps).

**Example:**

```python
from sqlalchemy.orm import sessionmaker

SessionLocal = sessionmaker(bind=engine, expire_on_commit=False)

def transfer_order(order_id: int, new_user_id: int) -> None:
    with SessionLocal() as session, session.begin():   # commit or rollback automatically
        order = session.get(Order, order_id)            # identity map lookup first
        order.user_id = new_user_id                     # tracked as dirty
        session.add(Order(user_id=new_user_id, total_cents=0))  # tracked as new
        # on exit: flush UPDATE + INSERT in one transaction, then COMMIT
```

**Remember:** One session per unit of work; it tracks changes and commits them together.

## Q69. The N+1 query problem and eager loading

N+1 happens when you load N parent rows and then lazily trigger one extra query per row to fetch a relationship, which is a classic cause of slow endpoints. In SQLAlchemy, fix it with `selectinload` (a second `IN` query, good for collections) or `joinedload` (a JOIN, good for many-to-one); set `lazy="raise"` to make accidental lazy loads fail loudly. In Django, use `select_related` for foreign keys and `prefetch_related` for reverse and many-to-many relations.

- **Trade-offs**:
  - `joinedload` on collections duplicates parent rows; `selectinload` adds a round trip but scales better. Over-eager loading fetches data you do not use.

**Example:**

```python
from sqlalchemy import select
from sqlalchemy.orm import selectinload, joinedload

# N+1: 1 query for users + 1 per user for orders
users = session.scalars(select(User)).all()
for u in users:
    print(len(u.orders))        # lazy load each time

# Fixed: 2 queries total
users = session.scalars(select(User).options(selectinload(User.orders))).all()

# Many-to-one via JOIN
orders = session.scalars(select(Order).options(joinedload(Order.user))).all()

# Django equivalents:
# Order.objects.select_related("user")
# User.objects.prefetch_related("orders")
```

> **Interview tip:** Say how you would detect it: SQL logging (`echo=True`), query counting in tests, or APM traces showing many identical queries per request.

**Remember:** Eager load deliberately; make lazy loads raise in API code.

## Q70. Connection pooling

Opening a DB connection is expensive (TCP, TLS, auth), so SQLAlchemy engines keep a pool (`QueuePool` by default) with `pool_size` persistent connections plus `max_overflow` extras. Use `pool_pre_ping` to detect dead connections and `pool_recycle` to avoid server-side idle timeouts. Remember the total: pool size times worker processes times replicas must stay below the database's connection limit, which is why PgBouncer is common in front of Postgres.

- **Trade-offs**:
  - Bigger pools reduce wait time but can overwhelm the DB; small pools queue requests under load (tune `pool_timeout`).
  - Pools are per process; create the engine after forking or dispose it in the child.

**Example:**

```python
from sqlalchemy import create_engine

engine = create_engine(
    "postgresql+psycopg://app@db/app",
    pool_size=10,          # steady-state connections per process
    max_overflow=5,        # burst capacity
    pool_timeout=5,        # seconds to wait for a free connection
    pool_pre_ping=True,    # validate before use
    pool_recycle=1800,     # seconds; avoid stale connections
)

# 4 gunicorn workers x 3 pods x (10 + 5) = up to 180 connections: check max_connections
```

**Remember:** Pools are per process; multiply by workers and replicas.

## Q71. Transactions and isolation levels

A transaction groups statements so they commit or roll back atomically; in SQLAlchemy use `with session.begin():` or `engine.begin()`, and in Django `transaction.atomic()`. Isolation levels (READ COMMITTED, REPEATABLE READ, SERIALIZABLE) control which anomalies can occur between concurrent transactions; Postgres defaults to READ COMMITTED. Keep transactions short and never hold one open across a network call to another service.

- **Trade-offs**:
  - Stronger isolation prevents more anomalies but causes serialization failures that you must retry.
  - Long transactions hold locks and bloat MVCC history.

**Example:**

```python
from sqlalchemy import create_engine, text
from sqlalchemy.exc import OperationalError

serializable_engine = engine.execution_options(isolation_level="SERIALIZABLE")

def book_seat(seat_id: int, user_id: int, attempts: int = 3) -> None:
    for attempt in range(attempts):
        try:
            with serializable_engine.begin() as conn:
                taken = conn.execute(text("SELECT 1 FROM bookings WHERE seat_id = :s"), {"s": seat_id}).first()
                if taken:
                    raise ValueError("seat taken")
                conn.execute(text("INSERT INTO bookings (seat_id, user_id) VALUES (:s, :u)"),
                             {"s": seat_id, "u": user_id})
            return
        except OperationalError:            # serialization failure: retry
            if attempt == attempts - 1:
                raise
```

See the [SQL question index](../sql/question-index.md) for isolation anomalies in depth.

**Remember:** Short transactions; stronger isolation means retrying on conflict.

## Q72. Pessimistic and optimistic locking

Pessimistic locking uses `SELECT ... FOR UPDATE` (`with_for_update()` in SQLAlchemy, `select_for_update()` in Django) to lock rows until the transaction ends, suitable for hot contention like inventory or balances. Optimistic locking adds a version column and updates `WHERE id = ? AND version = ?`, failing if someone else changed the row, which suits low-contention edits. Often the simplest correct option is a single atomic `UPDATE` with a condition plus a unique constraint.

- **Trade-offs**:
  - Pessimistic: correctness under contention, but lock waits and deadlock risk.
  - Optimistic: no locks held, but conflicts surface as errors the client must retry.

**Example:**

```python
from sqlalchemy import select, update

# Pessimistic
with SessionLocal() as s, s.begin():
    acct = s.scalars(select(Account).where(Account.id == 1).with_for_update()).one()
    acct.balance -= 100

# Optimistic via version column
with SessionLocal() as s, s.begin():
    result = s.execute(
        update(Account)
        .where(Account.id == 1, Account.version == 7)
        .values(balance=Account.balance - 100, version=Account.version + 1)
    )
    if result.rowcount == 0:
        raise RuntimeError("concurrent modification, retry")

# SQLAlchemy can manage this automatically: __mapper_args__ = {"version_id_col": version}
```

**Remember:** FOR UPDATE for hot rows, version checks for rare conflicts.

## Q73. Database migrations with Alembic and Django

Schema changes should be versioned, reviewed and applied automatically: Alembic does this for SQLAlchemy (`alembic revision --autogenerate`, `alembic upgrade head`), and Django has `makemigrations` and `migrate`. Always review autogenerated migrations, since they can miss renames or produce destructive drops. For zero-downtime deploys, use expand-and-contract: add nullable columns, backfill in batches, deploy code that uses both, then drop the old column later.

- **Trade-offs**:
  - Automatic generation is fast but not always safe; large-table changes (adding indexes, rewriting columns) may need `CREATE INDEX CONCURRENTLY` and separate steps.

**Example:**

```python
# alembic/versions/20260901_add_status.py
from alembic import op
import sqlalchemy as sa

revision = "a1b2c3"
down_revision = "9f8e7d"

def upgrade() -> None:
    op.add_column("orders", sa.Column("status", sa.String(20), nullable=True))  # expand
    with op.get_context().autocommit_block():
        op.create_index("ix_orders_status", "orders", ["status"], postgresql_concurrently=True)

def downgrade() -> None:
    op.drop_index("ix_orders_status", table_name="orders")
    op.drop_column("orders", "status")

# Django: python manage.py makemigrations && python manage.py migrate
```

**Remember:** Version every schema change; expand, backfill, then contract.

## Q74. Async database drivers

Async frameworks need async drivers, otherwise DB calls block the event loop. Common choices are `asyncpg` or `psycopg` (v3, supports async) for Postgres, used directly or through SQLAlchemy's `AsyncEngine`/`AsyncSession`. With async sessions, lazy loading is effectively unavailable (implicit I/O cannot happen on attribute access), so eager loading and `expire_on_commit=False` become mandatory habits.

- **Trade-offs**:
  - High concurrency per worker versus more complex code and ecosystem gaps; async does not make the database itself faster, and pool limits still apply.

**Example:**

```python
from sqlalchemy import select
from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker
from sqlalchemy.orm import selectinload

engine = create_async_engine("postgresql+asyncpg://app@db/app", pool_size=10)
SessionLocal = async_sessionmaker(engine, expire_on_commit=False)

async def users_with_orders() -> list[User]:
    async with SessionLocal() as session:
        result = await session.scalars(select(User).options(selectinload(User.orders)))
        return list(result)

# Raw asyncpg for hot paths
import asyncpg
async def count_orders(pool: asyncpg.Pool, user_id: int) -> int:
    return await pool.fetchval("SELECT count(*) FROM orders WHERE user_id = $1", user_id)
```

**Remember:** Async app means async driver; eager load because lazy loads cannot await.

## Q75. Raw SQL vs ORM trade-offs

ORMs speed up CRUD, keep models and migrations in one place, and parameterise queries by default. Raw SQL (through `text()` with bound parameters, or a driver directly) is better for complex reporting, window functions, CTEs, bulk operations, and database-specific features where the ORM output is hard to control. Most mature services use both: ORM for the domain, hand-written SQL for the few performance-critical or analytical queries, always with parameters, never string formatting.

- **Trade-offs**:
  - ORM: productivity and safety, but hidden queries and object overhead.
  - Raw SQL: full control and performance, but more code to maintain and no automatic mapping.

**Example:**

```python
from sqlalchemy import text

REVENUE_SQL = text("""
    SELECT date_trunc('day', created_at) AS day,
           sum(total_cents) AS revenue,
           sum(sum(total_cents)) OVER (ORDER BY date_trunc('day', created_at)) AS running
    FROM orders
    WHERE created_at >= :since
    GROUP BY 1
    ORDER BY 1
""")

with engine.connect() as conn:
    rows = conn.execute(REVENUE_SQL, {"since": "2026-09-01"}).mappings().all()   # bound param

# NEVER: conn.execute(text(f"SELECT * FROM users WHERE email = '{email}'"))
```

**Remember:** ORM by default, raw SQL where it earns its keep, parameters always.

## Q76. Using Redis from Python

`redis-py` provides both sync (`redis.Redis`) and async (`redis.asyncio.Redis`) clients with built-in connection pooling. Common backend uses are caching with TTLs, rate limiting with `INCR` plus `EXPIRE`, distributed locks with `SET key value NX PX`, idempotency keys, sessions, pub/sub and as a Celery broker or result backend. Always set TTLs on cache keys, use pipelines to batch round trips, and plan for Redis being unavailable.

- **Trade-offs**:
  - Very fast shared state across workers versus data loss risk (persistence settings), memory limits and cache invalidation complexity.
  - Simple Redis locks are not safe for strict correctness; back critical invariants with DB constraints.

**Example:**

```python
import json
from redis.asyncio import Redis

redis = Redis.from_url("redis://redis:6379/0", decode_responses=True)

async def get_product(product_id: int) -> dict:
    key = f"product:{product_id}"
    if cached := await redis.get(key):
        return json.loads(cached)
    product = await load_product_from_db(product_id)
    await redis.set(key, json.dumps(product), ex=300)       # TTL 5 minutes
    return product

async def allow_request(user_id: int, limit: int = 100) -> bool:
    key = f"rl:{user_id}"
    async with redis.pipeline(transaction=True) as pipe:
        count, _ = await pipe.incr(key).expire(key, 60, nx=True).execute()
    return count <= limit

async def load_product_from_db(product_id: int) -> dict: ...
```

**Remember:** Redis for shared fast state; always TTL, pipeline, and plan for failure.

## References

- [SQLAlchemy documentation](https://docs.sqlalchemy.org/)
- [SQLAlchemy ORM querying guide](https://docs.sqlalchemy.org/en/20/orm/queryguide/index.html)
- [SQLAlchemy relationship loading techniques](https://docs.sqlalchemy.org/en/20/orm/queryguide/relationships.html)
- [SQLAlchemy connection pooling](https://docs.sqlalchemy.org/en/20/core/pooling.html)
- [SQLAlchemy asyncio extension](https://docs.sqlalchemy.org/en/20/orm/extensions/asyncio.html)
- [Django database transactions](https://docs.djangoproject.com/en/stable/topics/db/transactions/)
- [Django migrations](https://docs.djangoproject.com/en/stable/topics/migrations/)
- [Python DB-API 2.0 (PEP 249)](https://peps.python.org/pep-0249/)
