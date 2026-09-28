---
sidebar_label: "Fundamentals and Runtime"
description: "How CPython runs your code, the GIL, object identity and mutability, memory management, packaging, typing and dunder methods."
---

# Python Fundamentals and Runtime (Q1-Q14)

> **Reviewed:** 2026-09 · **Level:** Senior · **Type:** Foundational

## Q1. How CPython executes a Python program

CPython is the reference implementation of Python, written in C. When you run a module it is parsed into an AST, compiled to bytecode (cached as `.pyc` files in `__pycache__`), and that bytecode is executed by a stack-based virtual machine loop. There is no JIT in the classic model, which is why pure-Python hot loops are slower than V8-optimised JavaScript; recent versions add a specialising adaptive interpreter (3.11+) and an experimental JIT (3.13+, Emerging).

- **Trade-offs**:
  - Simple, predictable runtime and a huge C-extension ecosystem (NumPy, psycopg, orjson) versus slower raw loop performance.
  - Alternatives exist (PyPy with a JIT), but C-extension compatibility usually keeps production backends on CPython.

**Example:**

```python
import dis

def add(a, b):
    return a + b

# Show the bytecode CPython's VM will execute
dis.dis(add)
# LOAD_FAST a, LOAD_FAST b, BINARY_OP (+), RETURN_VALUE
```

> **Interview tip:** Contrast with Node: V8 JIT-compiles hot JS to machine code; CPython interprets bytecode and relies on C extensions for heavy lifting.

**Remember:** Source to AST to bytecode to VM loop; speed comes from C extensions, not the interpreter.

## Q2. The GIL and when it matters

The Global Interpreter Lock is a mutex in CPython that allows only one thread to execute Python bytecode at a time within a process. It makes reference counting and interpreter internals thread-safe cheaply, but it means threads do not give you CPU parallelism for pure-Python code. The GIL is released during blocking I/O and by many C extensions, so threads still work well for I/O-bound work.

- **Trade-offs**:
  - Simpler, faster single-threaded code and safe C extensions versus no multi-core scaling for CPU-bound Python threads.
  - Workarounds: `multiprocessing`/process pools, C extensions that release the GIL, or free-threaded builds (see Q54).

**Example:**

```python
import threading, time

def cpu_bound():
    # Pure Python loop holds the GIL; two threads will not run this in parallel
    sum(i * i for i in range(10_000_000))

def io_bound():
    # time.sleep releases the GIL, so threads overlap nicely
    time.sleep(1)

threads = [threading.Thread(target=io_bound) for _ in range(10)]
[t.start() for t in threads]; [t.join() for t in threads]  # ~1s total, not 10s
```

<details>
<summary>Follow-up questions</summary>

- Does the GIL make my code thread-safe? No. It protects interpreter internals, not your invariants; `counter += 1` is several bytecodes and can interleave.
- How do web servers scale then? Multiple worker processes (gunicorn/uvicorn workers), each with its own GIL.

</details>

**Remember:** GIL blocks CPU parallelism in threads, not I/O concurrency.

## Q3. Everything is an object: identity, type and value

Every Python value is an object with an identity (`id()`, stable for its lifetime), a type, and a value. Variables are names bound to objects, not boxes holding values. Assignment never copies; it just binds another name to the same object.

- **Trade-offs**:
  - Uniform model makes introspection and metaprogramming easy, at the cost of per-object memory overhead (headers, refcount, type pointer).

**Example:**

```python
a = [1, 2, 3]
b = a            # b is another name for the same list
b.append(4)
print(a)         # [1, 2, 3, 4]
print(id(a) == id(b), type(a))  # True <class 'list'>
```

**Remember:** Names point to objects; assignment binds, it never copies.

## Q4. Mutable vs immutable types

Immutable objects (`int`, `float`, `str`, `bytes`, `tuple`, `frozenset`) cannot change after creation; "modifying" them creates a new object. Mutable objects (`list`, `dict`, `set`, most class instances) change in place, so every name referencing them sees the change. Only hashable (typically immutable) objects can be dict keys or set members.

- **Trade-offs**:
  - Immutables are safe to share across threads and as cache keys; mutables avoid copying but invite aliasing bugs.
  - A tuple containing a list is not truly immutable and is not hashable.

**Example:**

```python
s = "abc"
t = s
s += "d"          # new str object; t still "abc"

def bad(item, bucket=[]):   # default evaluated ONCE at def time
    bucket.append(item)
    return bucket

def good(item, bucket=None):
    bucket = [] if bucket is None else bucket
    bucket.append(item)
    return bucket
```

> **Interview tip:** The mutable default argument bug is the classic Python gotcha. Mention it proactively.

**Remember:** Immutables rebind on change; mutables change in place for every reference.

## Q5. `is` vs `==`

`==` compares values by calling `__eq__`; `is` compares identity (same object in memory). Use `is` only for singletons such as `None`, `True`/`False` and sentinel objects. Small integers and some strings are cached (interned) by CPython, which makes `is` appear to work by accident, so never rely on it for values.

- **Trade-offs**:
  - `is` is fast and cannot be overridden; `==` is semantic and customisable but can be expensive for big structures.

**Example:**

```python
a = [1, 2]; b = [1, 2]
print(a == b, a is b)    # True False

x = None
if x is None:            # correct idiom (PEP 8)
    ...

_MISSING = object()      # sentinel, compare with `is`
def get(key, default=_MISSING): ...
```

**Remember:** `is` for identity and `None`; `==` for values.

## Q6. Pass-by-object-reference (call by sharing)

Python passes references to objects into functions. The function parameter is a new name bound to the same object, so mutating a mutable argument is visible to the caller, but rebinding the parameter is not. This is neither pure pass-by-value nor pass-by-reference; it is the same model as JavaScript objects.

- **Trade-offs**:
  - No hidden copies (fast), but functions that mutate inputs surprise callers; prefer returning new values or documenting mutation.

**Example:**

```python
def mutate(items):
    items.append(99)   # caller sees this

def rebind(items):
    items = [0]        # local rebinding; caller unaffected

data = [1]
mutate(data); rebind(data)
print(data)            # [1, 99]
```

**Remember:** Mutation leaks to the caller; rebinding does not.

## Q7. Reference counting and the garbage collector

CPython frees most objects deterministically via reference counting: when an object's refcount hits zero it is deallocated immediately. A supplemental cyclic garbage collector (`gc` module, generational) finds reference cycles that refcounting cannot reclaim. Objects with `__del__` in cycles, global caches and lingering references are the usual sources of "leaks".

- **Trade-offs**:
  - Deterministic cleanup (files close promptly) versus refcount overhead on every assignment and the need for a cycle collector.
  - Do not rely on `__del__` for resource cleanup; use context managers.

**Example:**

```python
import sys, gc, weakref

a = []
print(sys.getrefcount(a))   # includes the temporary arg reference

class Node:
    def __init__(self): self.other = None

n1, n2 = Node(), Node()
n1.other, n2.other = n2, n1  # cycle
del n1, n2
gc.collect()                 # cycle collector reclaims them

cache = weakref.WeakValueDictionary()  # does not keep values alive
```

**Remember:** Refcount frees most objects instantly; the GC handles cycles.

## Q8. Virtual environments and dependency isolation

A virtual environment (`python -m venv .venv`) is an isolated directory with its own interpreter link and `site-packages`, so each project has its own dependency versions. It is the Python equivalent of a project-local `node_modules`, except you must activate it or call its interpreter explicitly. Never install project dependencies into the system Python.

- **Trade-offs**:
  - Isolation and reproducibility versus managing one env per project; tools like `uv` and Poetry create and manage envs automatically.

**Example:**

```python
# Shell (shown as comments):
# python -m venv .venv
# source .venv/bin/activate          # Windows: .venv\Scripts\activate
# python -m pip install -r requirements.txt

import sys
print(sys.prefix != sys.base_prefix)  # True when running inside a venv
```

**Remember:** One venv per project; `python -m pip` targets the active interpreter.

## Q9. Packaging with pyproject.toml, pip, uv and Poetry

`pyproject.toml` (PEP 518/621) is the standard place for project metadata, dependencies and tool config (ruff, pytest, mypy), roughly Python's `package.json`. `pip` installs packages; lock files for reproducible deploys come from tools such as `uv` (fast resolver/installer and project manager), Poetry, or `pip-tools`. For services, pin exact versions via a lock file and install from it in CI and Docker.

- **Trade-offs**:
  - Plain `pip` + `requirements.txt` is universal but lacks first-class locking; `uv`/Poetry add locking and env management at the cost of another tool in the chain.

**Example:**

```python
# pyproject.toml (TOML shown as comments)
# [project]
# name = "orders-service"
# version = "1.4.0"
# requires-python = ">=3.12"
# dependencies = ["fastapi>=0.110", "sqlalchemy>=2.0", "pydantic>=2"]
#
# [project.optional-dependencies]
# dev = ["pytest", "ruff", "mypy"]
#
# [tool.ruff]
# line-length = 100

# uv add httpx        -> updates pyproject.toml and uv.lock
# uv sync --frozen    -> reproducible install in CI/Docker
```

> **Interview tip:** Map it to Node: `pyproject.toml` ~ `package.json`, `uv.lock`/`poetry.lock` ~ `package-lock.json`, venv ~ `node_modules`.

**Remember:** Declare in `pyproject.toml`, lock with a tool, install frozen in CI.

## Q10. Type hints and static typing overview

Type hints (PEP 484) are annotations that the runtime ignores but static checkers (mypy, pyright) and frameworks use. FastAPI and Pydantic read them at runtime to drive validation and serialization, which is a key difference from TypeScript where types vanish. Modern syntax includes `list[int]`, `X | None`, `TypedDict`, `Protocol`, generics, and (3.12+) the `type` alias statement and `def f[T](x: T)` syntax.

- **Trade-offs**:
  - Better tooling and refactoring safety versus annotation effort; hints are not enforced at runtime unless a library validates them.

**Example:**

```python
from typing import TypedDict, Protocol

class UserDict(TypedDict):
    id: int
    email: str

class Repo(Protocol):
    def get(self, user_id: int) -> UserDict | None: ...

def first[T](items: list[T]) -> T | None:   # PEP 695 generics (3.12+)
    return items[0] if items else None

def handler(repo: Repo, user_id: int) -> str:
    user = repo.get(user_id)
    return user["email"] if user else "missing"
```

**Remember:** Hints are for checkers and frameworks; runtime ignores them unless something validates.

## Q11. Dunder (magic) methods and the data model

Dunder methods like `__init__`, `__repr__`, `__eq__`, `__hash__`, `__len__`, `__iter__`, `__enter__`/`__exit__` let your classes plug into Python syntax and built-ins. `len(x)` calls `x.__len__()`, `a + b` calls `a.__add__(b)`, `with x:` calls `__enter__`/`__exit__`. Implementing them makes domain objects feel native, which is the "Pythonic" way instead of custom method names.

- **Trade-offs**:
  - Expressive APIs versus surprising behaviour if you overload operators unintuitively.
  - If you define `__eq__`, you must think about `__hash__` (it becomes `None` by default, making instances unhashable).

**Example:**

```python
class Money:
    def __init__(self, cents: int, currency: str):
        self.cents, self.currency = cents, currency

    def __repr__(self) -> str:                 # debugging/logs
        return f"Money({self.cents}, {self.currency!r})"

    def __eq__(self, other: object) -> bool:
        return isinstance(other, Money) and (self.cents, self.currency) == (other.cents, other.currency)

    def __hash__(self) -> int:
        return hash((self.cents, self.currency))

    def __add__(self, other: "Money") -> "Money":
        assert self.currency == other.currency
        return Money(self.cents + other.cents, self.currency)
```

**Remember:** Dunders connect your objects to Python syntax; pair `__eq__` with `__hash__`.

## Q12. `__repr__` vs `__str__`

`__repr__` should be an unambiguous developer-facing representation (ideally something that could recreate the object) and is used in the REPL, logs of containers, and debuggers. `__str__` is the user-friendly form used by `print()` and `str()`, falling back to `__repr__` if not defined. In backend code, a good `__repr__` on models makes logs and tracebacks far more useful.

- **Trade-offs**:
  - Detailed reprs help debugging, but never include secrets (passwords, tokens) since reprs end up in logs and error trackers.

**Example:**

```python
class User:
    def __init__(self, id: int, email: str, password_hash: str):
        self.id, self.email, self._pw = id, email, password_hash

    def __repr__(self) -> str:
        return f"User(id={self.id!r}, email={self.email!r})"  # no secrets

    def __str__(self) -> str:
        return self.email

u = User(1, "a@x.io", "hash")
print(u, [u])   # a@x.io [User(id=1, email='a@x.io')]
```

**Remember:** `repr` for developers, `str` for users; keep secrets out of both.

## Q13. Modules, imports and `if __name__ == "__main__"`

A module is a `.py` file; a package is a directory of modules (usually with `__init__.py`). Imports execute the module once and cache it in `sys.modules`, so module-level code runs only on first import. The `__name__ == "__main__"` guard lets a file act as both an importable module and a script, and it is required with `multiprocessing` on spawn-based platforms.

- **Trade-offs**:
  - Module-level singletons (config, clients) are convenient but make testing harder and can cause circular imports; prefer factory functions or dependency injection.

**Example:**

```python
# app/config.py
import os
DATABASE_URL = os.environ.get("DATABASE_URL", "sqlite:///dev.db")  # runs once per process

# app/cli.py
from app.config import DATABASE_URL

def main() -> None:
    print("connecting to", DATABASE_URL)

if __name__ == "__main__":   # only when run as `python -m app.cli`
    main()
```

**Remember:** Imports run once and are cached; guard script entry points.

## Q14. Python version awareness for backend work

Know roughly what each recent release brought, because interviewers check that you use modern idioms. 3.8 added the walrus operator; 3.9 built-in generics (`list[int]`); 3.10 `match` statements and `X | Y` unions; 3.11 big interpreter speedups, `ExceptionGroup` and `asyncio.TaskGroup`; 3.12 PEP 695 generics syntax and better f-strings; 3.13 an experimental free-threaded build and JIT (Emerging). Check the official "What's New" pages and your framework's supported versions before upgrading.

- **Trade-offs**:
  - Newer versions are faster and nicer, but C extensions and platform images may lag; pin `requires-python` and test upgrades in CI.

**Example:**

```python
# 3.10+ structural pattern matching for event routing
def handle(event: dict) -> str:
    match event:
        case {"type": "order.created", "id": int(order_id)}:
            return f"create {order_id}"
        case {"type": "order.cancelled", "id": order_id}:
            return f"cancel {order_id}"
        case _:
            return "ignored"

# 3.8+ walrus operator
if (n := len(data := [1, 2, 3])) > 2:
    print(n, data)
```

**Remember:** Target a supported 3.x, use modern syntax, and verify extension compatibility before upgrades.

## References

- [Python documentation](https://docs.python.org/3/)
- [Python data model](https://docs.python.org/3/reference/datamodel.html)
- [dis module](https://docs.python.org/3/library/dis.html)
- [gc module](https://docs.python.org/3/library/gc.html)
- [venv module](https://docs.python.org/3/library/venv.html)
- [typing module](https://docs.python.org/3/library/typing.html)
- [What's New in Python](https://docs.python.org/3/whatsnew/index.html)
- [PEP 703 - Making the GIL optional](https://peps.python.org/pep-0703/)
