---
sidebar_position: 0
sidebar_label: "Question Index"
description: "All 100 Python backend interview questions grouped by topic, with links to each section."
---

# Python Backend Interview Questions: Index

> **Reviewed:** 2026-09 · **Level:** Senior · **Type:** Foundational

100 questions for senior backend interviews in Python, numbered continuously across nine files. Start with the [Overview](./index.md) for the learning order, and use the [Cheatsheet](./cheatsheet.md) for last-minute revision.

| Section | Topic | Questions |
|---------|-------|-----------|
| 1 | [Fundamentals and Runtime](./01-fundamentals-and-runtime.md) | Q1-Q14 |
| 2 | [Data Structures and Stdlib](./02-data-structures-and-stdlib.md) | Q15-Q26 |
| 3 | [Functions, OOP and Design](./03-functions-oop-and-design.md) | Q27-Q40 |
| 4 | [Async and Concurrency](./04-async-and-concurrency.md) | Q41-Q54 |
| 5 | [Web Frameworks](./05-web-frameworks.md) | Q55-Q66 |
| 6 | [Databases and ORM](./06-databases-and-orm.md) | Q67-Q76 |
| 7 | [APIs, Auth and Security](./07-apis-auth-and-security.md) | Q77-Q84 |
| 8 | [Testing and Tooling](./08-testing-and-tooling.md) | Q85-Q92 |
| 9 | [Performance and Production](./09-performance-and-production.md) | Q93-Q100 |

## 1. [Fundamentals and Runtime](./01-fundamentals-and-runtime.md) (Q1-Q14)

1. How CPython executes a Python program
2. The GIL and when it matters
3. Everything is an object: identity, type and value
4. Mutable vs immutable types
5. `is` vs `==`
6. Pass-by-object-reference (call by sharing)
7. Reference counting and the garbage collector
8. Virtual environments and dependency isolation
9. Packaging with pyproject.toml, pip, uv and Poetry
10. Type hints and static typing overview
11. Dunder (magic) methods and the data model
12. `__repr__` vs `__str__`
13. Modules, imports and `if __name__ == "__main__"`
14. Python version awareness for backend work

## 2. [Data Structures and Stdlib](./02-data-structures-and-stdlib.md) (Q15-Q26)

15. Lists, tuples and slicing complexity
16. Dicts and sets: hash tables and complexity
17. Dict insertion ordering
18. Comprehensions and generator expressions
19. The iterator protocol
20. Generators and `yield`
21. itertools for efficient iteration
22. collections: defaultdict and Counter
23. deque, namedtuple and heapq
24. Dataclasses
25. Shallow copy vs deep copy
26. Sorting with key functions

## 3. [Functions, OOP and Design](./03-functions-oop-and-design.md) (Q27-Q40)

27. Functions are first-class objects
28. Closures, scope (LEGB) and `nonlocal`
29. Decorators and `functools.wraps`
30. Decorators with arguments
31. `*args`, `**kwargs`, keyword-only and positional-only parameters
32. Context managers and the `with` statement
33. Classes, instance vs class attributes
34. `@classmethod`, `@staticmethod` and `@property`
35. MRO, `super()` and multiple inheritance
36. Abstract base classes vs Protocols
37. `__slots__` for memory and attribute control
38. Descriptors (light overview)
39. Metaclasses and when NOT to use them
40. SOLID principles in Python

## 4. [Async and Concurrency](./04-async-and-concurrency.md) (Q41-Q54)

41. Threading vs multiprocessing vs asyncio
42. CPU-bound vs I/O-bound work and when the GIL matters
43. The asyncio event loop
44. Coroutines, `async` and `await`
45. Tasks and `asyncio.create_task`
46. `asyncio.gather` vs `TaskGroup`
47. Timeouts and cancellation in asyncio
48. Blocking calls inside async code
49. `concurrent.futures`: ThreadPoolExecutor and ProcessPoolExecutor
50. Race conditions and thread locks
51. asyncio synchronisation: Lock and Semaphore
52. Producer-consumer with queues
53. asyncio compared with the Node.js event loop
54. Free-threaded Python (PEP 703) (Emerging)

## 5. [Web Frameworks](./05-web-frameworks.md) (Q55-Q66)

55. WSGI vs ASGI
56. Django vs FastAPI vs Flask
57. How FastAPI uses type hints
58. FastAPI dependency injection with `Depends`
59. Pydantic validation (v2)
60. Configuration with pydantic-settings
61. Middleware in Django and FastAPI
62. Request lifecycle in a FastAPI app
63. Django ORM and admin strengths
64. Background tasks vs Celery
65. Serving with gunicorn and uvicorn workers
66. Lifespan events and app-scoped resources

## 6. [Databases and ORM](./06-databases-and-orm.md) (Q67-Q76)

67. SQLAlchemy Core vs ORM
68. Sessions and the unit of work pattern
69. The N+1 query problem and eager loading
70. Connection pooling
71. Transactions and isolation levels
72. Pessimistic and optimistic locking
73. Database migrations with Alembic and Django
74. Async database drivers
75. Raw SQL vs ORM trade-offs
76. Using Redis from Python

## 7. [APIs, Auth and Security](./07-apis-auth-and-security.md) (Q77-Q84)

77. REST API design in Python
78. Pagination strategies
79. Idempotency keys for safe retries
80. JWT vs server-side sessions
81. OAuth2 flows in FastAPI
82. Password hashing with bcrypt and Argon2
83. Common vulnerabilities: injection, SSRF and unsafe deserialisation
84. Secrets and configuration (12-factor)

## 8. [Testing and Tooling](./08-testing-and-tooling.md) (Q85-Q92)

85. pytest fixtures and parametrize
86. Mocking with unittest.mock and "patch where it is used"
87. Testing async code
88. Testing FastAPI and Django endpoints
89. Code coverage
90. Linting and formatting with ruff and black
91. Static type checking with mypy and pyright
92. pre-commit hooks

## 9. [Performance and Production](./09-performance-and-production.md) (Q93-Q100)

93. Profiling with cProfile and py-spy
94. Finding and fixing memory leaks
95. Caching with functools and Redis
96. Scaling Python workers
97. Logging and structured logs
98. Dockerizing Python apps
99. Observability hooks: metrics, traces and health
100. Choosing Python vs Node.js for a service
