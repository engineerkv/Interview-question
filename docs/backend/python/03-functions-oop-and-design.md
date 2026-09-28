---
sidebar_label: "Functions, OOP and Design"
description: "First-class functions, closures, decorators, context managers, classes, MRO, ABCs vs Protocols, slots, descriptors, metaclasses and SOLID in Python."
---

# Python Functions, OOP and Design (Q27-Q40)

> **Reviewed:** 2026-09 · **Level:** Senior · **Type:** Foundational

## Q27. Functions are first-class objects

Functions in Python are objects: you can assign them to variables, store them in dicts, pass them as arguments and return them from other functions. This enables strategy tables, callbacks and higher-order utilities without extra class hierarchies. `lambda` creates small anonymous single-expression functions, but named `def` functions are preferred for anything non-trivial because they show up clearly in tracebacks.

- **Trade-offs**:
  - Lightweight strategy/dispatch patterns versus harder static analysis when functions are chosen dynamically.

**Example:**

```python
from typing import Callable

def to_json(data: dict) -> str: ...
def to_csv(data: dict) -> str: ...

EXPORTERS: dict[str, Callable[[dict], str]] = {"json": to_json, "csv": to_csv}

def export(data: dict, fmt: str) -> str:
    try:
        return EXPORTERS[fmt](data)      # dispatch table instead of if/elif chain
    except KeyError:
        raise ValueError(f"unsupported format {fmt}")
```

**Remember:** Functions are values; dispatch tables beat long `if/elif` chains.

## Q28. Closures, scope (LEGB) and `nonlocal`

Name lookup follows LEGB: Local, Enclosing, Global, Built-in. A closure is an inner function that captures variables from its enclosing scope; captured variables are looked up when the inner function runs (late binding), not when it is defined. To rebind an enclosing variable you need `nonlocal`; for module globals you need `global`.

- **Trade-offs**:
  - Closures give lightweight private state (counters, configured handlers) but late binding in loops is a common bug; bind via default args or `functools.partial`.

**Example:**

```python
def make_counter():
    count = 0
    def inc() -> int:
        nonlocal count          # rebind enclosing variable
        count += 1
        return count
    return inc

c = make_counter(); c(); print(c())   # 2

handlers = [lambda: i for i in range(3)]
print([h() for h in handlers])        # [2, 2, 2]  late binding
handlers = [lambda i=i: i for i in range(3)]
print([h() for h in handlers])        # [0, 1, 2]
```

**Remember:** Closures capture variables, not values; use `nonlocal` to rebind.

## Q29. Decorators and `functools.wraps`

A decorator is a callable that takes a function and returns a replacement, applied with `@decorator` syntax, which is just `f = decorator(f)`. They are used for cross-cutting concerns: logging, timing, retries, caching, auth checks and route registration (`@app.get`). Always use `functools.wraps` so the wrapper keeps the original `__name__`, `__doc__` and signature metadata that frameworks like FastAPI and tools rely on.

- **Trade-offs**:
  - Clean separation of concerns versus hidden control flow and extra stack frames; stacking many decorators obscures behaviour.
  - Sync decorators on `async def` functions must themselves be async-aware.

**Example:**

```python
import functools, time, logging

log = logging.getLogger(__name__)

def timed(func):
    @functools.wraps(func)                 # preserve name/doc/signature
    def wrapper(*args, **kwargs):
        start = time.perf_counter()
        try:
            return func(*args, **kwargs)
        finally:
            log.info("%s took %.3fs", func.__name__, time.perf_counter() - start)
    return wrapper

@timed
def load_report(report_id: int) -> dict: ...

print(load_report.__name__)   # 'load_report', not 'wrapper'
```

**Remember:** `@d` means `f = d(f)`; always `@functools.wraps`.

## Q30. Decorators with arguments

A decorator that accepts arguments is a factory: a function that takes the config and returns the actual decorator, giving three levels of nesting. This is how `@retry(times=3)` or `@app.get("/path")` work. For async functions, check `inspect.iscoroutinefunction` and produce an `async def` wrapper.

- **Trade-offs**:
  - Configurable reuse versus nesting complexity; for very complex behaviour a class-based decorator can be clearer.

**Example:**

```python
import asyncio, functools, inspect

def retry(times: int = 3, delay: float = 0.1, exceptions=(Exception,)):
    def decorator(func):
        if inspect.iscoroutinefunction(func):
            @functools.wraps(func)
            async def async_wrapper(*args, **kwargs):
                for attempt in range(1, times + 1):
                    try:
                        return await func(*args, **kwargs)
                    except exceptions:
                        if attempt == times:
                            raise
                        await asyncio.sleep(delay * 2 ** attempt)  # non-blocking backoff
            return async_wrapper

        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            for attempt in range(1, times + 1):
                try:
                    return func(*args, **kwargs)
                except exceptions:
                    if attempt == times:
                        raise
        return wrapper
    return decorator

@retry(times=5, exceptions=(ConnectionError,))
async def fetch_rates() -> dict: ...
```

**Remember:** Decorator with args = factory returning a decorator.

## Q31. `*args`, `**kwargs`, keyword-only and positional-only parameters

`*args` collects extra positional arguments into a tuple and `**kwargs` collects extra keyword arguments into a dict; the same symbols unpack sequences and mappings at call sites. Parameters after a bare `*` are keyword-only, which prevents ambiguous boolean flags; parameters before `/` are positional-only (3.8+). Using these deliberately makes public APIs safer to evolve.

- **Trade-offs**:
  - Flexible forwarding (wrappers, decorators) versus losing type information and discoverability if overused; prefer explicit parameters in public APIs.

**Example:**

```python
def create_user(email: str, /, *, is_admin: bool = False, **extra) -> dict:
    # email positional-only, is_admin keyword-only
    return {"email": email, "is_admin": is_admin, **extra}

create_user("a@x.io", is_admin=True, team="core")
# create_user("a@x.io", True)      -> TypeError, forces clarity

def log_call(func, *args, **kwargs):
    print(func.__name__, args, kwargs)
    return func(*args, **kwargs)   # forward everything
```

**Remember:** `*` for keyword-only, `/` for positional-only, `*args/**kwargs` for forwarding.

## Q32. Context managers and the `with` statement

A context manager guarantees setup and teardown around a block via `__enter__`/`__exit__`, even when exceptions occur. It is the Pythonic replacement for `try/finally` when handling files, locks, DB transactions, and temporary state. `contextlib.contextmanager` builds one from a generator, and `async with` uses `__aenter__`/`__aexit__` for async resources like HTTP clients and DB sessions.

- **Trade-offs**:
  - Deterministic cleanup and readable scoping; `__exit__` returning `True` swallows exceptions, which is rarely what you want.

**Example:**

```python
from contextlib import contextmanager, ExitStack
import time

@contextmanager
def timer(label: str):
    start = time.perf_counter()
    try:
        yield                      # body of the `with` runs here
    finally:
        print(label, time.perf_counter() - start)

with timer("import"), open("data.csv") as f:
    rows = f.readlines()

# Dynamic number of resources
with ExitStack() as stack:
    files = [stack.enter_context(open(p)) for p in ["a.txt", "b.txt"]]
```

**Remember:** `with` = guaranteed cleanup; use it for every resource.

## Q33. Classes, instance vs class attributes

A class defines behaviour; `__init__` initialises an already-created instance (`__new__` creates it). Attributes set on `self` are per-instance, while attributes defined in the class body are shared by all instances, so a mutable class attribute is shared state. Python has no enforced private members: `_name` is a convention and `__name` triggers name mangling to avoid subclass clashes.

- **Trade-offs**:
  - Simple, flexible objects; but lack of access control relies on discipline, and shared mutable class attributes cause cross-request leaks in web apps.

**Example:**

```python
class Service:
    retries = 3                 # class attribute, shared (immutable: fine)
    registry: list = []         # shared mutable: dangerous

    def __init__(self, name: str):
        self.name = name        # instance attribute
        self._cache: dict = {}  # "internal" by convention

a, b = Service("a"), Service("b")
a.registry.append("x")
print(b.registry)               # ['x']  shared across instances
```

**Remember:** Instance state on `self`; class-body attributes are shared.

## Q34. `@classmethod`, `@staticmethod` and `@property`

`@classmethod` receives the class (`cls`) and is used for alternative constructors like `from_dict` that work correctly with subclasses. `@staticmethod` receives nothing implicit; it is just a function namespaced in the class, often better as a module-level function. `@property` exposes a computed or validated attribute with attribute syntax, letting you add logic later without changing callers.

- **Trade-offs**:
  - Properties keep APIs stable but hide cost; do not put slow I/O behind a property.
  - Static methods add little value over module functions, use them only for tight cohesion.

**Example:**

```python
class Temperature:
    def __init__(self, celsius: float):
        self.celsius = celsius

    @classmethod
    def from_fahrenheit(cls, f: float) -> "Temperature":
        return cls((f - 32) * 5 / 9)       # works for subclasses too

    @staticmethod
    def is_valid(c: float) -> bool:
        return c >= -273.15

    @property
    def celsius(self) -> float:
        return self._c

    @celsius.setter
    def celsius(self, value: float) -> None:
        if not self.is_valid(value):
            raise ValueError("below absolute zero")
        self._c = value
```

**Remember:** classmethod for constructors, property for computed or validated attributes.

## Q35. MRO, `super()` and multiple inheritance

Python supports multiple inheritance and resolves attribute lookup with the C3 linearisation, visible as `Class.__mro__`. `super()` calls the next class in the MRO, not necessarily the direct parent, which is what makes cooperative mixins work as long as every class calls `super()` and accepts `**kwargs`. Use mixins for small orthogonal behaviours and prefer composition for everything else.

- **Trade-offs**:
  - Mixins give reuse (Django class-based views rely heavily on them) versus hard-to-trace behaviour when the MRO gets deep.

**Example:**

```python
class Base:
    def save(self): print("Base.save")

class TimestampMixin(Base):
    def save(self):
        print("set updated_at"); super().save()

class AuditMixin(Base):
    def save(self):
        print("write audit log"); super().save()

class Order(TimestampMixin, AuditMixin):
    pass

Order().save()
# set updated_at -> write audit log -> Base.save
print([c.__name__ for c in Order.__mro__])
# ['Order', 'TimestampMixin', 'AuditMixin', 'Base', 'object']
```

**Remember:** `super()` follows the MRO; mixins must cooperate.

## Q36. Abstract base classes vs Protocols

An `abc.ABC` with `@abstractmethod` defines nominal interfaces: subclasses must inherit and implement abstract methods or instantiation fails at runtime. A `typing.Protocol` defines structural interfaces: any class with matching methods satisfies it, checked by mypy/pyright (duck typing made explicit, similar to TypeScript interfaces). Protocols are great for ports/adapters and test doubles without coupling to a base class.

- **Trade-offs**:
  - ABCs give runtime enforcement and shared implementation; Protocols give loose coupling but only static checking (unless `@runtime_checkable`, which only checks method presence).

**Example:**

```python
from abc import ABC, abstractmethod
from typing import Protocol

class PaymentGateway(ABC):
    @abstractmethod
    def charge(self, cents: int) -> str: ...

class Notifier(Protocol):
    def send(self, to: str, body: str) -> None: ...

class SmsClient:                      # no inheritance needed
    def send(self, to: str, body: str) -> None: ...

def notify(n: Notifier) -> None:
    n.send("+100", "hi")

notify(SmsClient())                   # OK for type checker
# PaymentGateway()                    -> TypeError: can't instantiate abstract class
```

**Remember:** ABC = inherit and enforce at runtime; Protocol = structural, checked statically.

## Q37. `__slots__` for memory and attribute control

Defining `__slots__` replaces the per-instance `__dict__` with fixed storage for the listed attributes, reducing memory and slightly speeding attribute access. It also prevents creating arbitrary new attributes, which catches typos. It matters when you create millions of small objects; `@dataclass(slots=True)` is the easy way to get it.

- **Trade-offs**:
  - Lower memory versus less flexibility: no dynamic attributes, more care with inheritance, and some libraries expecting `__dict__` may break.

**Example:**

```python
class Point:
    __slots__ = ("x", "y")
    def __init__(self, x: float, y: float):
        self.x, self.y = x, y

p = Point(1, 2)
# p.z = 3        -> AttributeError
# p.__dict__     -> AttributeError

from dataclasses import dataclass
@dataclass(slots=True)
class Tick:
    ts: float
    price: float
```

**Remember:** `__slots__` trades flexibility for memory; use it for many small objects.

## Q38. Descriptors (light overview)

A descriptor is an object defining `__get__`, `__set__` or `__delete__` that controls attribute access when placed on a class. `property`, `classmethod`, `staticmethod`, bound methods, and ORM columns (SQLAlchemy, Django fields) are all built on descriptors. You rarely write them directly, but knowing they exist explains how `Model.field` and `instance.field` behave differently.

- **Trade-offs**:
  - Reusable attribute logic (validation, lazy loading) versus indirection that surprises readers; `property` covers most needs.

**Example:**

```python
class Positive:
    def __set_name__(self, owner, name):
        self.private = "_" + name
    def __get__(self, obj, objtype=None):
        if obj is None:
            return self                    # accessed on the class
        return getattr(obj, self.private)
    def __set__(self, obj, value):
        if value <= 0:
            raise ValueError("must be positive")
        setattr(obj, self.private, value)

class Product:
    price = Positive()                     # reusable validated attribute
    def __init__(self, price: float):
        self.price = price
```

**Remember:** Descriptors power properties, methods and ORM fields.

## Q39. Metaclasses and when NOT to use them

A metaclass is the class of a class (`type` by default); it can customise class creation, which is how Django models and some ORMs register fields. In application code you almost never need one: class decorators, `__init_subclass__`, and descriptors solve registration and validation with far less magic. Reaching for a metaclass in an interview answer should come with a justification.

- **Trade-offs**:
  - Powerful framework-level hooks versus conflicts (a class cannot easily combine two unrelated metaclasses) and code that is hard to debug.

**Example:**

```python
# Prefer __init_subclass__ for plugin registration
class Handler:
    registry: dict[str, type["Handler"]] = {}

    def __init_subclass__(cls, *, event: str, **kwargs):
        super().__init_subclass__(**kwargs)
        Handler.registry[event] = cls

class OrderCreated(Handler, event="order.created"):
    def handle(self, payload: dict) -> None: ...

print(Handler.registry)   # {'order.created': <class 'OrderCreated'>}
```

> **Interview tip:** Say "I would use `__init_subclass__` or a class decorator first; metaclasses are for framework authors."

**Remember:** Metaclasses are a last resort; `__init_subclass__` covers most cases.

## Q40. SOLID principles in Python

SOLID applies to Python but looks lighter than in Java. Single responsibility means small modules and functions; open/closed is often achieved with dispatch tables or plugins; Liskov still applies to subclasses; interface segregation maps naturally to small Protocols; dependency inversion means depending on Protocols and injecting implementations (FastAPI `Depends`, constructor args) rather than importing concrete clients everywhere.

- **Trade-offs**:
  - Clean seams for testing and swapping infrastructure versus over-abstraction; Python favours simple functions and composition until a second implementation actually appears.

**Example:**

```python
from typing import Protocol

class OrderRepo(Protocol):                 # small interface (ISP)
    def save(self, order: dict) -> None: ...

class EventBus(Protocol):
    def publish(self, topic: str, payload: dict) -> None: ...

class PlaceOrder:                          # single responsibility use case
    def __init__(self, repo: OrderRepo, bus: EventBus):   # DIP via injection
        self.repo, self.bus = repo, bus

    def __call__(self, order: dict) -> None:
        self.repo.save(order)
        self.bus.publish("order.created", order)

# Tests pass in fakes; production passes SQLAlchemy repo and RabbitMQ bus
```

**Remember:** Inject Protocol-typed dependencies; do not build hierarchies you do not need.

## References

- [Defining functions](https://docs.python.org/3/tutorial/controlflow.html#defining-functions)
- [functools module](https://docs.python.org/3/library/functools.html)
- [contextlib module](https://docs.python.org/3/library/contextlib.html)
- [Classes tutorial](https://docs.python.org/3/tutorial/classes.html)
- [abc module](https://docs.python.org/3/library/abc.html)
- [Descriptor HowTo Guide](https://docs.python.org/3/howto/descriptor.html)
- [Data model: customizing class creation](https://docs.python.org/3/reference/datamodel.html#customizing-class-creation)
- [typing.Protocol](https://docs.python.org/3/library/typing.html#typing.Protocol)
