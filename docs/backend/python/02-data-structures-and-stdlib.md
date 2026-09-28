---
sidebar_label: "Data Structures and Stdlib"
description: "Complexity of core containers, comprehensions, iterators and generators, itertools and collections, dataclasses, copying and sorting."
---

# Python Data Structures and Standard Library (Q15-Q26)

> **Reviewed:** 2026-09 · **Level:** Senior · **Type:** Foundational

## Q15. Lists, tuples and slicing complexity

A `list` is a dynamic array of references: indexing and `append` are O(1) (amortised), while `insert(0, x)`, `pop(0)` and `x in lst` are O(n). A `tuple` is an immutable fixed-size sequence, slightly smaller and hashable if its items are, so it suits records and dict keys. Slicing `lst[a:b:step]` always creates a new shallow copy costing O(k) for k elements.

- **Trade-offs**:
  - Lists are flexible but front operations are slow (use `deque`); tuples signal "fixed shape" and are safe to share.
  - Large slices copy memory; use `itertools.islice` or `memoryview` when you only need to iterate.

**Example:**

```python
items = [10, 20, 30, 40, 50]
print(items[1:4])    # [20, 30, 40]  new list
print(items[::-1])   # reversed copy
print(items[-2:])    # last two

point = (3, 4)       # hashable record
seen = {point}       # usable in sets/dict keys

# O(n) membership on list vs O(1) average on set
ids = list(range(1_000_000))
ids_set = set(ids)
999_999 in ids_set   # fast
```

**Remember:** List ends are cheap, list front and membership are O(n); slices copy.

## Q16. Dicts and sets: hash tables and complexity

`dict` and `set` are hash tables, giving average O(1) lookup, insert and delete, degrading to O(n) only under pathological hash collisions. Keys must be hashable and their hash must not change while stored, which is why mutable objects cannot be keys. Sets support fast algebra (`|`, `&`, `-`) useful for diffing IDs or permissions.

- **Trade-offs**:
  - Fast lookups at the cost of higher memory than lists.
  - Custom `__hash__`/`__eq__` must be consistent: equal objects must have equal hashes.

**Example:**

```python
user_roles = {"alice": {"admin", "dev"}, "bob": {"dev"}}

required = {"admin"}
print(required <= user_roles["alice"])   # subset check: True

old_ids, new_ids = {1, 2, 3}, {2, 3, 4}
to_add, to_remove = new_ids - old_ids, old_ids - new_ids   # {4}, {1}

cfg = {"timeout": 5}
timeout = cfg.get("retries", 3)          # default without KeyError
```

**Remember:** Hash tables: O(1) average, keys must be hashable and stable.

## Q17. Dict insertion ordering

Since Python 3.7, dicts are guaranteed by the language to preserve insertion order (it was a CPython 3.6 implementation detail first). Iteration, `keys()`, `values()` and JSON serialisation follow insertion order, and re-assigning an existing key keeps its original position. `OrderedDict` is still useful for `move_to_end` and order-sensitive equality, e.g. building a simple LRU.

- **Trade-offs**:
  - Predictable output (stable JSON, logs) without extra types; but do not treat dicts as sorted, and `OrderedDict` equality differs from `dict` equality.

**Example:**

```python
from collections import OrderedDict

d = {"b": 1, "a": 2}
d["b"] = 3
print(list(d))          # ['b', 'a']  order kept

lru = OrderedDict()
lru["x"] = 1; lru["y"] = 2
lru.move_to_end("x")    # mark as recently used
lru.popitem(last=False) # evict oldest -> ('y', 2)
```

**Remember:** Dicts keep insertion order (3.7+); `OrderedDict` adds reordering helpers.

## Q18. Comprehensions and generator expressions

List, dict and set comprehensions build collections in one readable expression and are typically faster than an equivalent `for` loop with `append`. A generator expression (parentheses) produces items lazily, so it uses constant memory and is ideal when feeding `sum`, `any`, `max` or streaming pipelines. Keep comprehensions simple; nested logic belongs in a regular loop or helper function.

- **Trade-offs**:
  - Concise and fast versus unreadable when nesting multiple `for`/`if` clauses.
  - Generator expressions can only be consumed once.

**Example:**

```python
orders = [{"id": 1, "total": 50, "paid": True}, {"id": 2, "total": 20, "paid": False}]

paid_ids = [o["id"] for o in orders if o["paid"]]         # list
by_id = {o["id"]: o for o in orders}                       # dict index
revenue = sum(o["total"] for o in orders if o["paid"])     # lazy, no temp list
has_unpaid = any(not o["paid"] for o in orders)            # short-circuits
```

**Remember:** Comprehension for a collection, generator expression for a stream.

## Q19. The iterator protocol

An iterable has `__iter__` returning an iterator; an iterator has `__next__` that returns the next item or raises `StopIteration`. `for` loops, unpacking, `list()`, and `in` all use this protocol. Iterators are single-pass and stateful, which matters when you pass the same iterator to two consumers.

- **Trade-offs**:
  - Lazy, memory-efficient processing versus single-use semantics that can silently yield nothing on a second pass.

**Example:**

```python
class Countdown:
    def __init__(self, start: int):
        self.current = start
    def __iter__(self):
        return self
    def __next__(self) -> int:
        if self.current <= 0:
            raise StopIteration
        self.current -= 1
        return self.current + 1

it = iter([1, 2, 3])
print(next(it), list(it), list(it))  # 1 [2, 3] []  exhausted
print(list(Countdown(3)))            # [3, 2, 1]
```

**Remember:** Iterables make iterators; iterators are one-shot.

## Q20. Generators and `yield`

A generator function contains `yield`; calling it returns a generator object that runs lazily, pausing at each `yield` and resuming on `next()`. This is the idiomatic way to stream large files, paginated API results or DB rows without loading everything into memory. `yield from` delegates to a sub-iterator, and generators were the foundation that `async`/`await` coroutines grew out of.

- **Trade-offs**:
  - Constant memory and composable pipelines versus harder debugging and single-pass consumption; exceptions surface at consumption time, not creation.

**Example:**

```python
from typing import Iterator
import httpx

def read_lines(path: str) -> Iterator[str]:
    with open(path) as f:           # file stays open until generator finishes
        for line in f:
            yield line.rstrip("\n")

def paginate(client: httpx.Client, url: str) -> Iterator[dict]:
    while url:
        page = client.get(url).json()
        yield from page["items"]    # delegate item by item
        url = page.get("next")

errors = (l for l in read_lines("app.log") if "ERROR" in l)  # pipeline stage
```

> **Interview tip:** Node analogy: generators are like JS generators/async iterators; a Python generator reading a file line by line is similar to consuming a Node readable stream.

**Remember:** `yield` gives lazy, resumable streams with constant memory.

## Q21. itertools for efficient iteration

`itertools` provides fast, lazy building blocks: `chain`, `islice`, `groupby`, `product`, `accumulate`, `pairwise` (3.10+), and `batched` (3.12+). They avoid intermediate lists and express common backend tasks such as batching inserts or grouping sorted rows. Note that `groupby` only groups consecutive equal keys, so sort first.

- **Trade-offs**:
  - Very efficient and composable, but dense chains can hurt readability; name intermediate steps.

**Example:**

```python
from itertools import batched, chain, groupby, islice
from operator import itemgetter

rows = [{"team": "a", "n": 1}, {"team": "a", "n": 2}, {"team": "b", "n": 3}]

for team, group in groupby(sorted(rows, key=itemgetter("team")), key=itemgetter("team")):
    print(team, sum(r["n"] for r in group))

for batch in batched(range(10_000), 500):   # bulk insert 500 at a time
    ...  # db.execute(insert_stmt, [{"id": i} for i in batch])

first_ten = list(islice(chain([1, 2], range(100)), 10))
```

**Remember:** itertools = lazy pipelines; sort before `groupby`.

## Q22. collections: defaultdict and Counter

`defaultdict(factory)` creates missing keys on first access, removing boilerplate when grouping or building adjacency lists. `Counter` is a dict subclass for counting hashables, with `most_common()` and arithmetic between counters. Both are standard, fast, and read better than manual `if key not in d` logic.

- **Trade-offs**:
  - `defaultdict` silently inserts keys on read, which can hide typos or bloat memory; convert to a plain dict before returning from APIs.

**Example:**

```python
from collections import defaultdict, Counter

events = [("u1", "login"), ("u2", "login"), ("u1", "purchase")]

by_user: defaultdict[str, list[str]] = defaultdict(list)
for user, action in events:
    by_user[user].append(action)

counts = Counter(action for _, action in events)
print(counts.most_common(1))   # [('login', 2)]
print(dict(by_user))           # plain dict for serialisation
```

**Remember:** `defaultdict` for grouping, `Counter` for counting.

## Q23. deque, namedtuple and heapq

`collections.deque` is a double-ended queue with O(1) append/pop at both ends and an optional `maxlen` that makes it a ring buffer, ideal for sliding windows and BFS. `namedtuple` (or `typing.NamedTuple`) gives lightweight immutable records with field names. `heapq` implements a min-heap on a list for priority queues and top-k problems.

- **Trade-offs**:
  - `deque` indexing in the middle is O(n); `heapq` is min-only (negate keys for a max-heap) and not thread-safe; use `queue.PriorityQueue` across threads.

**Example:**

```python
from collections import deque
from typing import NamedTuple
import heapq

recent = deque(maxlen=100)          # keeps last 100 latencies
recent.append(12.5)

class Job(NamedTuple):
    priority: int
    name: str

jobs: list[Job] = []
heapq.heappush(jobs, Job(2, "email"))
heapq.heappush(jobs, Job(1, "payment"))
print(heapq.heappop(jobs).name)      # payment (lowest priority value first)
print(heapq.nlargest(2, [5, 1, 9, 3]))
```

**Remember:** deque for both ends, heapq for priorities, NamedTuple for tiny records.

## Q24. Dataclasses

`@dataclass` generates `__init__`, `__repr__` and `__eq__` from annotated fields, with options like `frozen=True` (immutable and hashable), `slots=True` (3.10+, less memory), `kw_only=True` and `field(default_factory=list)` for mutable defaults. They are ideal for internal domain objects and DTOs. Unlike Pydantic models, dataclasses do not validate or coerce types at runtime.

- **Trade-offs**:
  - Zero-dependency and fast versus no validation; use Pydantic at trust boundaries (HTTP input, config) and dataclasses internally.

**Example:**

```python
from dataclasses import dataclass, field, asdict

@dataclass(frozen=True, slots=True)
class OrderLine:
    sku: str
    qty: int
    price_cents: int

@dataclass(kw_only=True)
class Order:
    id: int
    lines: list[OrderLine] = field(default_factory=list)  # never `= []`

    @property
    def total(self) -> int:
        return sum(l.qty * l.price_cents for l in self.lines)

o = Order(id=1, lines=[OrderLine("A1", 2, 500)])
print(o.total, asdict(o))
OrderLine("A1", "2", 500)   # no error: dataclasses do not validate
```

**Remember:** Dataclasses remove boilerplate; they do not validate.

## Q25. Shallow copy vs deep copy

A shallow copy (`copy.copy`, `list(x)`, `x[:]`, `dict.copy()`) creates a new container that still references the same inner objects. `copy.deepcopy` recursively copies nested objects, handling cycles via a memo dict. Deep copies are expensive and can copy things you did not intend (clients, locks), so prefer immutable data or explicit construction.

- **Trade-offs**:
  - Shallow is cheap but shares nested state; deep is safe but slow and may fail on non-copyable objects (sockets, locks).

**Example:**

```python
import copy

config = {"db": {"host": "a"}, "tags": ["x"]}
shallow = copy.copy(config)
deep = copy.deepcopy(config)

shallow["db"]["host"] = "b"
print(config["db"]["host"])  # 'b'  shared inner dict
print(deep["db"]["host"])    # 'a'  independent

grid = [[0] * 3] * 3         # trap: 3 references to the same row
grid = [[0] * 3 for _ in range(3)]  # correct
```

**Remember:** Shallow copies the box, deep copies the contents.

## Q26. Sorting with key functions

`sorted()` returns a new list and `list.sort()` sorts in place; both use Timsort, which is O(n log n) and stable. Pass `key=` to sort by a derived value (computed once per element), and use tuples for multi-level sorts. Stability lets you sort by secondary key first, then primary key.

- **Trade-offs**:
  - `key` is faster and clearer than old-style comparators; use `functools.cmp_to_key` only when a pairwise comparison is unavoidable.

**Example:**

```python
from operator import attrgetter, itemgetter

users = [{"name": "bo", "age": 30}, {"name": "al", "age": 30}, {"name": "cy", "age": 25}]

by_age_then_name = sorted(users, key=itemgetter("age", "name"))
newest_first = sorted(users, key=lambda u: (-u["age"], u["name"]))  # mixed direction

# top 3 without a full sort
import heapq
top3 = heapq.nlargest(3, users, key=itemgetter("age"))
```

**Remember:** Use `key=`, tuples for multi-field, and rely on sort stability.

## References

- [Built-in types](https://docs.python.org/3/library/stdtypes.html)
- [collections module](https://docs.python.org/3/library/collections.html)
- [itertools module](https://docs.python.org/3/library/itertools.html)
- [heapq module](https://docs.python.org/3/library/heapq.html)
- [dataclasses module](https://docs.python.org/3/library/dataclasses.html)
- [copy module](https://docs.python.org/3/library/copy.html)
- [Sorting HOW TO](https://docs.python.org/3/howto/sorting.html)
- [Pydantic documentation](https://docs.pydantic.dev/)
