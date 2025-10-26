# 💻 JavaScript Interview Notes (2025 Edition)

## 🟣 Section 7 — Real-World Practical Coding Questions — Q126-Q145

---

### 126. 🟣 Implement a `bind()` polyfill

🧠 **Concept:**
`bind()` returns a new function with a permanently bound `this` context and optional preset arguments.

💬 **Step-by-Step:**

1. Start with a wrapper that stores `this` and arguments.
2. Return a function that applies the original with those values.

💻 **Implementation:**

```js
Function.prototype.myBind = function(context, ...args1) {
  const fn = this;
  return function(...args2) {
    return fn.apply(context, [...args1, ...args2]);
  };
};
```

📝 **Optimization Notes:**
✅ Works with partial application.
⚠ Doesn't handle `new` keyword use (advanced polyfill can mimic that using `instanceof`).

---

## 2️⃣ Implement a `call()` polyfill

🧠 **Concept:**
`call()` invokes a function immediately with a given `this`.

💬 **Step-by-Step:**

1. Temporarily assign the function to the context.
2. Invoke, then remove.

💻 **Implementation:**

```js
Function.prototype.myCall = function(context, ...args) {
  context = context || globalThis;
  const fnSymbol = Symbol();
  context[fnSymbol] = this;
  const result = context[fnSymbol](...args);
  delete context[fnSymbol];
  return result;
};
```

📝 **Optimization Notes:**
✅ Symbol prevents key collision.
⚡ Works even if context is null or undefined.

---

## 3️⃣ Implement a `debounce()` function

🧠 **Concept:**
Debouncing delays function execution until a certain period of inactivity.

💬 **Step-by-Step:**

1. Track a timer ID.
2. Reset timer on each call.
3. Only execute when timer completes.

💻 **Implementation:**

```js
function debounce(fn, delay) {
  let timer;
  return function(...args) {
    clearTimeout(timer);
    timer = setTimeout(() => fn.apply(this, args), delay);
  };
}
```

📝 **Optimization Notes:**
✅ Ideal for resize, search input events.
⚡ Add `immediate` flag if you need leading execution.

---

## 4️⃣ Implement a `throttle()` function

🧠 **Concept:**
Throttle ensures a function executes at most once every X ms.

💬 **Step-by-Step:**

1. Store last call time.
2. Ignore subsequent calls within threshold.

💻 **Implementation:**

```js
function throttle(fn, limit) {
  let inThrottle = false;
  return function(...args) {
    if (!inThrottle) {
      fn.apply(this, args);
      inThrottle = true;
      setTimeout(() => (inThrottle = false), limit);
    }
  };
}
```

📝 **Optimization Notes:**
✅ Used in scroll handlers.
⚡ For smoother throttling, track timestamps instead of booleans.

---

## 5️⃣ Implement a `deepClone()` utility

🧠 **Concept:**
Create a full recursive copy of an object/array.

💬 **Step-by-Step:**

1. Handle primitives directly.
2. Detect Array vs Object.
3. Recurse through keys.

💻 **Implementation:**

```js
function deepClone(value) {
  if (value === null || typeof value !== "object") return value;
  if (Array.isArray(value)) return value.map(deepClone);
  const copy = {};
  for (const key in value) copy[key] = deepClone(value[key]);
  return copy;
}
```

📝 **Optimization Notes:**
✅ Handles nested structures.
⚠ Loses methods/symbols — use `structuredClone()` if available.

---

## 6️⃣ Implement a `curry()` function

🧠 **Concept:**
Transforms a function of n args into chained calls of 1 arg each.

💬 **Step-by-Step:**

1. Capture function length.
2. Return a function collecting args until count met.
3. Execute once all received.

💻 **Implementation:**

```js
function curry(fn) {
  return function curried(...args) {
    if (args.length >= fn.length) return fn(...args);
    return (...next) => curried(...args, ...next);
  };
}
```

📝 **Optimization Notes:**
✅ Great for functional pipelines.
⚡ Use for pre-filled configurations (e.g., `logger(level)(msg)`).

---

## 7️⃣ Implement an `EventEmitter` class

🧠 **Concept:**
Implements pub/sub — register, emit, and remove listeners.

💻 **Implementation:**

```js
class EventEmitter {
  constructor() { this.events = {}; }
  on(event, listener) {
    (this.events[event] ||= []).push(listener);
  }
  emit(event, ...args) {
    (this.events[event] || []).forEach(fn => fn(...args));
  }
  off(event, listener) {
    this.events[event] = (this.events[event] || []).filter(fn => fn !== listener);
  }
}
```

📝 **Optimization Notes:**
✅ Core of Node.js event model.
⚡ Extendable for once-listeners and wildcard events.

---

## 8️⃣ Implement a `Promise.all()` polyfill

🧠 **Concept:**
Resolves when *all* promises fulfill; rejects if *any* reject.

💻 **Implementation:**

```js
Promise.myAll = function(promises) {
  return new Promise((resolve, reject) => {
    const results = [];
    let completed = 0;
    promises.forEach((p, i) =>
      Promise.resolve(p).then(val => {
        results[i] = val;
        if (++completed === promises.length) resolve(results);
      }, reject)
    );
  });
};
```

📝 **Optimization Notes:**
✅ Handles mixed promise/non-promise inputs.
⚠ Rejects fast on first failure.

---

## 9️⃣ Implement a `Promise.race()` polyfill

🧠 **Concept:**
Resolves/rejects with the *first* settled promise.

💻 **Implementation:**

```js
Promise.myRace = function(promises) {
  return new Promise((resolve, reject) =>
    promises.forEach(p => Promise.resolve(p).then(resolve, reject))
  );
};
```

📝 **Optimization Notes:**
✅ Useful for timeout races or first-response wins.

---

## 🔟 Implement a custom `memoize()` function

🧠 **Concept:**
Caches function results based on inputs.

💬 **Step-by-Step:**

1. Maintain a cache Map.
2. Stringify or hash arguments as keys.
3. Return cached value if available.

💻 **Implementation:**

```js
function memoize(fn) {
  const cache = new Map();
  return function(...args) {
    const key = JSON.stringify(args);
    if (cache.has(key)) return cache.get(key);
    const result = fn(...args);
    cache.set(key, result);
    return result;
  };
}
```

📝 **Optimization Notes:**
✅ Boosts performance for pure deterministic functions.
⚡ Use WeakMap for object args to avoid memory bloat.

---

## 11️⃣ Implement a `compose()` function

🧠 **Concept:** Compose executes functions **right-to-left** (`compose(f,g)(x)`  `f(g(x))`).

💬 **Evolution:**
1️⃣ Naïve: nested calls  `f(g(h(x)))`
2️⃣ Optimized: reduceRight loop  scalable
3️⃣ Production: handle async fns with `await`

💻 **Code:**

```js
const compose =
  (...fns) =>
  x =>
    fns.reduceRight((acc, fn) => fn(acc), x);
```

📝 **Insight:**
 Functional programming core.
 Async version wraps reducer in `Promise.resolve(acc)`.

---

## 12️⃣ Implement a `pipe()` function

🧠 **Concept:** Opposite of compose — left-to-right (`pipe(f,g)(x)`  `g(f(x))`).

💻 **Code:**

```js
const pipe =
  (...fns) =>
  x =>
    fns.reduce((acc, fn) => fn(acc), x);
```

🧠 **Diagram:**

```
input  f1  f2  f3  output
```

📝 **Insight:**
 Used heavily in RxJS, Redux middleware.
 Readable chaining for transformations.

---

## 13️⃣ Implement a retry mechanism for failed API calls

🧠 **Concept:** Retry an async operation N times with delay.

💬 **Evolution:**
1️⃣ Basic: manual loop of fetch()
2️⃣ Improved: recursive with delay
3️⃣ Final: configurable retries & backoff

💻 **Code:**

```js
async function retry(fn, retries = 3, delay = 500) {
  try {
    return await fn();
  } catch (err) {
    if (retries === 0) throw err;
    await new Promise(res => setTimeout(res, delay));
    return retry(fn, retries - 1, delay * 2); // exponential backoff
  }
}
```

📝 **Insight:**
✅ Used for flaky APIs.
⚡ Add jitter (random ± 10%) to avoid request storms.

---

## 14️⃣ Implement a function to flatten an object

🧠 **Concept:** Turn nested object into dot-notation keys.

💻 **Code:**

```js
function flatten(obj, parent = "", res = {}) {
  for (let [key, val] of Object.entries(obj)) {
    const path = parent ? `${parent}.${key}` : key;
    typeof val === "object" && val !== null
      ? flatten(val, path, res)
      : (res[path] = val);
  }
  return res;
}
```

🧠 **Diagram:**

```
{a:{b:1,c:{d:2}}}  {"a.b":1,"a.c.d":2}
```

📝 **Insight:**
✅ Great for Mongo update payloads or query serializers.

---

## 15️⃣ Implement a function to merge two sorted arrays

🧠 **Concept:** Classic O(n+m) two-pointer merge.

💻 **Code:**

```js
function mergeSorted(a, b) {
  const res = [];
  let i = 0, j = 0;
  while (i < a.length && j < b.length)
    res.push(a[i] < b[j] ? a[i++] : b[j++]);
  return res.concat(a.slice(i), b.slice(j));
}
```

🧠 **Diagram:**

```
[1,3,5] + [2,4,6]  [1,2,3,4,5,6]
```

📝 **Insight:**
✅ Basis of merge sort, merge-join in databases.

---

## 16️⃣ Implement your own `instanceof` operator

🧠 **Concept:** Walk prototype chain to check match.

💻 **Code:**

```js
function myInstanceOf(obj, ctor) {
  let proto = Object.getPrototypeOf(obj);
  while (proto) {
    if (proto === ctor.prototype) return true;
    proto = Object.getPrototypeOf(proto);
  }
  return false;
}
```

🧠 **Diagram:**

```
obj.__proto__  ctor.prototype  Object.prototype  null
```

📝 **Insight:**
✅ Tests inheritance manually.
⚡ Use `Object.getPrototypeOf` instead of `__proto__`.

---

## 17️⃣ Implement a caching decorator function

🧠 **Concept:** Wrap a function to cache results by arguments.

💻 **Code:**

```js
function cacheDecorator(fn) {
  const cache = new Map();
  return function(...args) {
    const key = JSON.stringify(args);
    if (cache.has(key)) return cache.get(key);
    const res = fn(...args);
    cache.set(key, res);
    return res;
  };
}
```

🧠 **Diagram:**

```
call  check cache  compute  store  return
```

📝 **Insight:**
✅ Use for pure functions (API transformers).
⚡ Swap to WeakMap for object keys to avoid leaks.

---

## 18️⃣ Implement a deep comparison (`isDeepEqual`)

🧠 **Concept:** Recursively compare values and keys.

💻 **Code:**

```js
function isDeepEqual(a, b) {
  if (a === b) return true;
  if (typeof a !== "object" || typeof b !== "object" || !a || !b) return false;
  const keysA = Object.keys(a), keysB = Object.keys(b);
  if (keysA.length !== keysB.length) return false;
  return keysA.every(k => isDeepEqual(a[k], b[k]));
}
```

🧠 **Diagram:**

```
{a:{b:1}} vs {a:{b:1}}  ✅
{a:{b:1}} vs {a:{b:2}}  ❌
```

📝 **Insight:**
✅ Core for React memoization or testing libs.
⚡ Can add `WeakSet` tracking for circular refs.

---

## 19️⃣ Implement a simple LRU Cache

🧠 **Concept:** Least Recently Used cache with O(1) get/set.

💬 **Evolution:**
1️⃣ Map + manual tracking
2️⃣ Final: use Map ordering + delete/reinsert to move recent entries

💻 **Code:**

```js
class LRUCache {
  constructor(limit = 5) {
    this.limit = limit;
    this.map = new Map();
  }
  get(key) {
    if (!this.map.has(key)) return undefined;
    const val = this.map.get(key);
    this.map.delete(key);
    this.map.set(key, val);
    return val;
  }
  set(key, val) {
    if (this.map.has(key)) this.map.delete(key);
    this.map.set(key, val);
    if (this.map.size > this.limit)
      this.map.delete(this.map.keys().next().value);
  }
}
```

🧠 **Diagram:**

```
Recent: [k3,k2,k1]  
 get(k1)  reorder  [k1,k3,k2]  
 insert new  evict oldest
```

📝 **Insight:**
✅ Backbone of HTTP and DB caches.
⚡ Map preserves insertion order  perfect for LRU.

---

## 20️⃣ Implement a function to merge sorted streams (concurrent)

🧠 **Concept:** Combine multiple async streams in sorted order.

💻 **Code:**

```js
async function* mergeAsync(...sources) {
  const readers = sources.map(s => s[Symbol.asyncIterator]());
  while (readers.length) {
    const results = await Promise.all(readers.map(r => r.next()));
    const active = results
      .map((r, i) => ({ ...r, i }))
      .filter(r => !r.done)
      .sort((a, b) => a.value - b.value);
    if (!active.length) break;
    const next = active[0];
    yield next.value;
    readers[next.i].next(); // advance that iterator
  }
}
```

🧠 **Diagram:**

```
Stream A: 1-3-5
Stream B: 2-4-6
 Merged: 1 2 3 4 5 6
```

📝 **Insight:**
✅ Core idea behind async data pipelines & stream processing.
⚡ Handles real-time data merging (queues, sockets).

---

## ⚡ Quick Recap

| Utility          | Core Purpose            | Common Use             |
| ---------------- | ----------------------- | ---------------------- |
| `bind()`         | Context binding         | Event callbacks        |
| `call()`         | Immediate invocation    | Explicit context calls |
| `debounce()`     | Delay execution         | Input/resize events    |
| `throttle()`     | Limit frequency         | Scroll handlers        |
| `deepClone()`    | Recursive copy          | Immutable updates      |
| `curry()`        | Partial application     | Functional pipelines   |
| `EventEmitter`   | Pub/Sub pattern         | Event systems          |
| `Promise.all()`  | Batch parallel promises | Multiple API calls     |
| `Promise.race()` | Compete tasks           | Timeout handling       |
| `memoize()`      | Cache results           | Heavy computations     |

---

## 🧠 Evolution Pattern Summary

| Stage             | Naïve | Optimized         | Production                   |
| ----------------- | ----- | ----------------- | ---------------------------- |
| Basic logic works | ✅     | Reusable, generic | Async/error safe             |
| Performance       | ❌     | ✅ O(1)/O(n) tuned | ✅ memory-friendly            |
| Robustness        | ❌     | Partial           | ✅ full error + edge handling |

---

*This section covers practical coding implementations that are commonly asked in JavaScript interviews, from basic polyfills to advanced data structures and algorithms.*
