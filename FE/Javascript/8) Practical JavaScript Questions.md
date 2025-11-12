# 🧰 8. Practical JavaScript Questions (Q82–170)

---

## 🧩 Q82. Write a debounce function.

### 🧠 Concept

Debouncing delays function execution until after a period of inactivity, preventing rapid repeated calls. It clears the previous timeout on each call and only executes after the delay period.

---

### 💡 Example

```js
const debounce = (fn, delay) => {
  let timeoutId;
  return (...args) => {
    clearTimeout(timeoutId);
    timeoutId = setTimeout(() => fn(...args), delay);
  };
};
```

---

### 🔍 Deep Insights

* **Rule:** Clear previous timeout on each call, only execute after delay period of inactivity.
* **Use Case:** Useful for search inputs and resize events.
* **Common Mistake:** Not returning cleanup function for manual cancellation.
* **Pro Tip:** Consider immediate execution option for first call.

---

### ⭐ Senior Takeaway

Debounce prevents rapid repeated function calls, improving performance and UX.

---

## 🧩 Q83. Write a custom `bind()` polyfill.

### 🧠 Concept

`bind()` creates a new function with `this` bound and optional partial arguments. Store the original function and bound context, return a new function that calls the original with `apply`.

---

### 💡 Example

```js
Function.prototype.bind = function(context, ...args) {
  const fn = this;
  return function(...moreArgs) {
    return fn.apply(context, [...args, ...moreArgs]);
  };
};
```

---

### 🔍 Deep Insights

* **Rule:** Store original function and bound context, return new function that calls original with `apply`.
* **Use Case:** Merge bound arguments with new arguments.
* **Common Mistake:** Not preserving function properties or handling edge cases like `new` operator.
* **Pro Tip:** Handle edge cases like `new` operator for complete implementation.

---

### ⭐ Senior Takeaway

Bind enables partial application and context binding, making functions more flexible.

---

## 🧩 Q84. Implement your own `Promise.all()` polyfill.

### 🧠 Concept

`Promise.all()` resolves when all promises fulfill or rejects on first failure. Handle non-promise values with `Promise.resolve`, preserve order of results array, and count completions to know when done.

---

### 💡 Example

```js
Promise.all = function(promises) {
  return new Promise((resolve, reject) => {
    const results = []; let completed = 0;
    promises.forEach((p, i) => {
      Promise.resolve(p).then(val => {
        results[i] = val; completed++;
        if (completed === promises.length) resolve(results);
      }).catch(reject);
    });
  });
};
```

---

### 🔍 Deep Insights

* **Rule:** Handle non-promise values with `Promise.resolve`, preserve order of results array.
* **Use Case:** Reject immediately on first failure, count completions to know when done.
* **Common Mistake:** Not handling empty input (return empty array).
* **Pro Tip:** Return empty array for empty input to match native behavior.

---

### ⭐ Senior Takeaway

Promise.all is fail-fast on first rejection, making error handling predictable.

---

## 🧩 Q85. Implement your own `Promise.race()` polyfill.

### 🧠 Concept

`Promise.race()` resolves or rejects as soon as the first promise settles. Return the first settled promise's result, whether it fulfills or rejects. Handle non-promise values with `Promise.resolve`.

---

### 💡 Example

```js
Promise.race = function(promises) {
  return new Promise((resolve, reject) => {
    if (!promises.length) return;
    promises.forEach(p => {
      Promise.resolve(p).then(resolve).catch(reject);
    });
  });
};

// Usage
const p1 = new Promise(resolve => setTimeout(() => resolve('First'), 100));
const p2 = new Promise(resolve => setTimeout(() => resolve('Second'), 200));
Promise.race([p1, p2]).then(console.log); // 'First'
```

---

### 🔍 Deep Insights

* **Rule:** Return the first settled promise's result, whether it fulfills or rejects.
* **Use Case:** Useful for timeouts, racing multiple API calls, or implementing cancellation.
* **Common Mistake:** Not handling empty input array (should remain pending).
* **Pro Tip:** Handle non-promise values with `Promise.resolve` to normalize input.

---

### ⭐ Senior Takeaway

Promise.race returns the first settled promise, useful for timeouts and cancellation patterns.

---

## 🧩 Q86. Implement your own `Promise.any()` polyfill.

### 🧠 Concept

`Promise.any()` resolves with the first fulfilled promise, or rejects with an AggregateError if all promises reject. Track rejections and only reject when all promises have rejected.

---

### 💡 Example

```js
Promise.any = function(promises) {
  return new Promise((resolve, reject) => {
    if (!promises.length) {
      reject(new AggregateError([], 'All promises were rejected'));
      return;
    }
    const errors = [];
    let rejectedCount = 0;
    promises.forEach((p, i) => {
      Promise.resolve(p).then(resolve).catch(err => {
        errors[i] = err;
        rejectedCount++;
        if (rejectedCount === promises.length) {
          reject(new AggregateError(errors, 'All promises were rejected'));
        }
      });
    });
  });
};

// Usage
const p1 = Promise.reject('Error 1');
const p2 = Promise.resolve('Success');
const p3 = Promise.reject('Error 2');
Promise.any([p1, p2, p3]).then(console.log); // 'Success'
```

---

### 🔍 Deep Insights

* **Rule:** Resolve with first fulfilled promise, reject with AggregateError if all reject.
* **Use Case:** Useful when you need any successful result from multiple attempts.
* **Common Mistake:** Not handling empty input (should reject with AggregateError).
* **Pro Tip:** AggregateError contains all rejection reasons for debugging.

---

### ⭐ Senior Takeaway

Promise.any succeeds if any promise fulfills, opposite of Promise.all's fail-fast behavior.

---

## 🧩 Q87. Implement your own `Promise.allSettled()` polyfill.

### 🧠 Concept

`Promise.allSettled()` waits for all promises to settle (fulfill or reject) and returns an array of results with status and value/reason. Never rejects, always resolves with all outcomes.

---

### 💡 Example

```js
Promise.allSettled = function(promises) {
  return Promise.all(
    promises.map(p => 
      Promise.resolve(p)
        .then(value => ({ status: 'fulfilled', value }))
        .catch(reason => ({ status: 'rejected', reason }))
    )
  );
};

// Usage
const p1 = Promise.resolve('Success');
const p2 = Promise.reject('Error');
const p3 = Promise.resolve('Another success');
Promise.allSettled([p1, p2, p3]).then(results => {
  console.log(results);
  // [
  //   { status: 'fulfilled', value: 'Success' },
  //   { status: 'rejected', reason: 'Error' },
  //   { status: 'fulfilled', value: 'Another success' }
  // ]
});
```

---

### 🔍 Deep Insights

* **Rule:** Always resolves with array of results, never rejects.
* **Use Case:** Useful when you need all outcomes regardless of success or failure.
* **Common Mistake:** Not preserving order of results array.
* **Pro Tip:** Each result has `status: 'fulfilled'` or `'rejected'` with corresponding `value` or `reason`.

---

### ⭐ Senior Takeaway

Promise.allSettled provides complete outcome information for all promises, useful for batch operations.

---

## 🧩 Q88. Write a throttle function.

### 🧠 Concept

Throttle limits function execution to once per specified time period. Track last execution time and execute immediately if enough time has passed.

---

### 💡 Example

```js
const throttle = (fn, delay) => {
  let lastCall = 0;
  return (...args) => {
    const now = Date.now();
    if (now - lastCall >= delay) {
      lastCall = now;
      fn(...args);
    }
  };
};
```

---

### 🔍 Deep Insights

* **Rule:** Track last execution time, execute immediately if enough time passed.
* **Use Case:** Drop calls that come too soon, useful for scroll and mouse move events.
* **Common Mistake:** Not considering leading/trailing edge options.
* **Pro Tip:** Consider leading/trailing edge options for different behaviors.

---

### ⭐ Senior Takeaway

Throttle guarantees execution at most once per period, preventing excessive calls.

---

## 🧩 Q170. Flatten a deeply nested array.

### 🧠 Concept

Recursively flatten arrays to any depth, handling nested structures. Use recursion to handle arbitrary depth and check `Array.isArray` for nested arrays.

---

### 💡 Example

```js
const flatten = arr => arr.reduce((acc, val) => 
  Array.isArray(val) ? acc.concat(flatten(val)) : acc.concat(val), []);
flatten([1, [2, [3, 4]], 5]); // [1, 2, 3, 4, 5]
```

---

### 🔍 Deep Insights

* **Rule:** Use recursion to handle arbitrary depth, check `Array.isArray` for nested arrays.
* **Use Case:** Use `reduce` for functional approach.
* **Common Mistake:** Not considering depth limit to prevent stack overflow.
* **Pro Tip:** Handle edge cases like empty arrays.

---

### ⭐ Senior Takeaway

Recursive approach handles any nesting depth, making it flexible but watch for stack overflow.

---

## 🧩 Q168. Memoize a given function to cache results.

### 🧠 Concept

Memoization caches function results based on arguments to avoid repeated computation. Use Map for O(1) cache lookups and serialize arguments for cache keys.

---

### 💡 Example

```js
const memoize = fn => {
  const cache = new Map();
  return (...args) => {
    const key = JSON.stringify(args);
    if (cache.has(key)) return cache.get(key);
    const result = fn(...args);
    cache.set(key, result);
    return result;
  };
};
```

---

### 🔍 Deep Insights

* **Rule:** Use Map for O(1) cache lookups, serialize arguments for cache keys.
* **Use Case:** Works best with pure functions.
* **Common Mistake:** Not considering memory limits and cache eviction.
* **Pro Tip:** Handle edge cases like circular references.

---

### ⭐ Senior Takeaway

Memoization improves performance for expensive computations by avoiding repeated work.

---

## 🧩 Q169. Implement a custom event emitter (pub/sub).

### 🧠 Concept

Event emitter allows objects to subscribe to and emit events with data. Store event handlers in object/Map and support multiple listeners per event.

---

### 💡 Example

```js
class EventEmitter {
  constructor() { this.events = {}; }
  on(event, fn) { (this.events[event] ||= []).push(fn); }
  emit(event, data) { (this.events[event] || []).forEach(fn => fn(data)); }
  off(event, fn) { this.events[event] = (this.events[event] || []).filter(f => f !== fn); }
}
```

---

### 🔍 Deep Insights

* **Rule:** Store event handlers in object/Map, support multiple listeners per event.
* **Use Case:** Provide `on`, `emit`, and `off` methods.
* **Common Mistake:** Not handling error cases and edge scenarios.
* **Pro Tip:** Consider `once` method for single-use listeners.

---

### ⭐ Senior Takeaway

Event emitters enable decoupled communication between components.

---

## 🧩 Q170. Implement a retry mechanism for a failed promise.

### 🧠 Concept

Retry failed operations with exponential backoff and maximum attempt limits. Use exponential backoff to prevent thundering herd and add jitter to distribute retry timing.

---

### 💡 Example

```js
const retry = (fn, maxAttempts = 3, delay = 1000) => 
  fn().catch(err => 
    maxAttempts > 0 ? 
      new Promise(resolve => 
        setTimeout(() => resolve(retry(fn, maxAttempts - 1, delay * 2)), delay)
      ) : 
      Promise.reject(err)
  );
```

---

### 🔍 Deep Insights

* **Rule:** Use exponential backoff to prevent thundering herd.
* **Use Case:** Add jitter to distribute retry timing, consider circuit breakers for cascading failures.
* **Common Mistake:** Not setting reasonable limits to avoid infinite loops.
* **Pro Tip:** Log retries for observability.

---

### ⭐ Senior Takeaway

Retry improves reliability for transient failures with proper backoff strategy.

---

## 🧩 Q168. Write a function to compose multiple functions (`compose(f,g,h)` style).

### 🧠 Concept

Function composition applies functions from right to left, creating a pipeline. Use `reduceRight` for right-to-left application, each function receives result of previous.

---

### 💡 Example

```js
const compose = (...fns) => x => fns.reduceRight((acc, fn) => fn(acc), x);
const add1 = x => x + 1;
const double = x => x * 2;
compose(console.log, add1, double)(5); // 11
```

---

### 🔍 Deep Insights

* **Rule:** Use `reduceRight` for right-to-left application, each function receives result of previous.
* **Use Case:** Great for data transformation pipelines.
* **Common Mistake:** Not considering `pipe` (left-to-right) alternative.
* **Pro Tip:** Works well with curried functions.

---

### ⭐ Senior Takeaway

Composition enables functional programming patterns for clean data transformations.

---

## 🧩 Q169. Implement a custom `map()` method for arrays.

### 🧠 Concept

`map()` creates new array by applying function to each element. Create new array, don't modify original, and pass element, index, and array to callback.

---

### 💡 Example

```js
Array.prototype.map = function(fn, thisArg) {
  const result = [];
  for (let i = 0; i < this.length; i++) {
    result[i] = fn.call(thisArg, this[i], i, this);
  }
  return result;
};
```

---

### 🔍 Deep Insights

* **Rule:** Create new array, don't modify original, pass element, index, and array to callback.
* **Use Case:** Handle sparse arrays correctly, support `thisArg` for context binding.
* **Common Mistake:** Not considering edge cases like undefined elements.
* **Pro Tip:** Consider edge cases like undefined elements for complete implementation.

---

### ⭐ Senior Takeaway

Map creates new array without mutating original, enabling functional programming.

---

## 🧩 Q170. Implement a `once()` function that executes only once.

### 🧠 Concept

`once()` ensures a function can only be called once, returning the same result on subsequent calls. Track if function has been called and cache result for subsequent calls.

---

### 💡 Example

```js
const once = fn => {
  let called = false, result;
  return (...args) => {
    if (!called) {
      called = true;
      result = fn(...args);
    }
    return result;
  };
};
```

---

### 🔍 Deep Insights

* **Rule:** Track if function has been called, cache result for subsequent calls.
* **Use Case:** Useful for initialization and setup.
* **Common Mistake:** Not considering error handling for failed calls.
* **Pro Tip:** Works with both sync and async functions.

---

### ⭐ Senior Takeaway

Once prevents duplicate initialization or setup, ensuring single execution.

---

## 🧩 Q168. Convert callback-based code to a promise-based version.

### 🧠 Concept

Wrap callback-based functions in promises using the Promise constructor. Use Promise constructor for one-time operations and handle both success and error cases.

---

### 💡 Example

```js
const readFile = path => new Promise((resolve, reject) => {
  fs.readFile(path, (err, data) => {
    if (err) reject(err);
    else resolve(data);
  });
});
```

---

### 🔍 Deep Insights

* **Rule:** Use Promise constructor for one-time operations, handle both success and error cases.
* **Use Case:** Consider promisify utilities for Node.js.
* **Common Mistake:** Not maintaining same error handling patterns.
* **Pro Tip:** Test thoroughly with edge cases.

---

### ⭐ Senior Takeaway

Promises improve async code readability and error handling over callbacks.

---

## 🧩 Q169. Write a function to limit the number of concurrent promises.

### 🧠 Concept

Control concurrency by limiting how many promises can run simultaneously. Track running and completed tasks, queue tasks when limit reached.

---

### 💡 Example

```js
const limitConcurrency = (tasks, limit) => {
  const results = []; let running = 0, index = 0;
  return new Promise(resolve => {
    const runNext = () => {
      if (index >= tasks.length && running === 0) return resolve(results);
      if (running >= limit || index >= tasks.length) return;
      running++; const task = tasks[index++];
      task().then(result => { results[index - 1] = result; running--; runNext(); });
    }; runNext();
  });
};
```

---

### 🔍 Deep Insights

* **Rule:** Track running and completed tasks, queue tasks when limit reached.
* **Use Case:** Preserve result order in output array, useful for API rate limiting.
* **Common Mistake:** Not handling errors appropriately.
* **Pro Tip:** Handle errors appropriately for robust implementation.

---

### ⭐ Senior Takeaway

Concurrency limiting prevents resource exhaustion and rate limit issues.

---

## 🧩 Q170. Write a function that returns a promise resolved after a delay.

### 🧠 Concept

Create a promise that resolves after a specified time delay. Use `setTimeout` with Promise constructor and return promise for chaining.

---

### 💡 Example

```js
const delay = ms => new Promise(resolve => setTimeout(resolve, ms));
delay(1000).then(() => console.log('1 second later'));
```

---

### 🔍 Deep Insights

* **Rule:** Use `setTimeout` with Promise constructor, return promise for chaining.
* **Use Case:** Useful for testing and rate limiting.
* **Common Mistake:** Not considering cancellation with AbortController.
* **Pro Tip:** Can be used with async/await.

---

### ⭐ Senior Takeaway

Delay is useful for testing and timing control in async code.

---

## 🧩 Q168. Implement a chainable calculator API (`calc.add(5).multiply(2).value()`).

### 🧠 Concept

Create a fluent interface where methods return the object for chaining. Return `this` from methods for chaining and store state in the object.

---

### 💡 Example

```js
const calc = {
  value: 0,
  add(n) { this.value += n; return this; },
  multiply(n) { this.value *= n; return this; },
  getValue() { return this.value; }
};
calc.add(5).multiply(2).getValue(); // 10
```

---

### 🔍 Deep Insights

* **Rule:** Return `this` from methods for chaining, store state in the object.
* **Use Case:** Use getter for final value access, great for builder patterns.
* **Common Mistake:** Not considering immutable alternatives.
* **Pro Tip:** Consider immutable alternatives for functional style.

---

### ⭐ Senior Takeaway

Method chaining enables fluent APIs that are readable and expressive.

---

## 🧩 Q169. Implement a simple version of `setInterval` using `setTimeout`.

### 🧠 Concept

Use recursive `setTimeout` calls to create interval-like behavior. Recursive calls create repeating behavior, return cleanup function for cancellation.

---

### 💡 Example

```js
const setInterval = (fn, delay) => {
  const run = () => {
    fn();
    setTimeout(run, delay);
  };
  setTimeout(run, delay);
};
```

---

### 🔍 Deep Insights

* **Rule:** Recursive calls create repeating behavior, return cleanup function for cancellation.
* **Use Case:** More flexible than native `setInterval`.
* **Common Mistake:** Not considering drift correction for precise timing.
* **Pro Tip:** Handle errors to prevent stopping.

---

### ⭐ Senior Takeaway

Recursive setTimeout is more flexible than setInterval for custom timing needs.

---

## 🧩 Q170. Write a function to shuffle an array randomly.

### 🧠 Concept

Randomly reorder array elements using Fisher-Yates shuffle algorithm. Use Fisher-Yates for uniform distribution and work backwards through array.

---

### 💡 Example

```js
const shuffle = arr => {
  const result = [...arr];
  for (let i = result.length - 1; i > 0; i--) {
    const j = Math.floor(Math.random() * (i + 1));
    [result[i], result[j]] = [result[j], result[i]];
  }
  return result;
};
```

---

### 🔍 Deep Insights

* **Rule:** Use Fisher-Yates for uniform distribution, work backwards through array.
* **Use Case:** Swap elements randomly, create copy to avoid mutating original.
* **Common Mistake:** Not creating copy, mutating original array.
* **Pro Tip:** Consider seeded random for testing.

---

### ⭐ Senior Takeaway

Fisher-Yates ensures uniform random distribution, making it the standard algorithm.

---

## 🧩 Q168. Implement your own version of `debounce + immediate` combined logic.

### 🧠 Concept

Combine debounce with immediate execution option for first call. Execute immediately on first call if enabled, clear timeout on subsequent calls.

---

### 💡 Example

```js
const debounceImmediate = (fn, delay, immediate = false) => {
  let timeoutId;
  return (...args) => {
    const callNow = immediate && !timeoutId;
    clearTimeout(timeoutId);
    timeoutId = setTimeout(() => {
      timeoutId = null;
      if (!immediate) fn(...args);
    }, delay);
    if (callNow) fn(...args);
  };
};
```

---

### 🔍 Deep Insights

* **Rule:** Execute immediately on first call if enabled, clear timeout on subsequent calls.
* **Use Case:** Reset timeout flag after execution, useful for search with immediate feedback.
* **Common Mistake:** Not considering both leading and trailing options.
* **Pro Tip:** Consider both leading and trailing options for different behaviors.

---

### ⭐ Senior Takeaway

Immediate option provides instant feedback while still debouncing subsequent calls.

---

## 🧩 Q169. How do you implement useMemo from scratch?

### 🧠 Concept

`useMemo` caches the result of a computation and only recalculates when dependencies change. Store previous dependencies for comparison and only recalculate when dependencies change.

---

### 💡 Example

```js
const useMemo = (computeFn, deps) => {
  const [memoizedValue, setMemoizedValue] = useState(() => computeFn());
  const [prevDeps, setPrevDeps] = useState(deps);
  useEffect(() => {
    const hasChanged = !deps || deps.some((dep, i) => dep !== prevDeps[i]);
    if (hasChanged) { setMemoizedValue(computeFn()); setPrevDeps(deps); }
  }, deps);
  return memoizedValue;
};
```

---

### 🔍 Deep Insights

* **Rule:** Store previous dependencies for comparison, only recalculate when dependencies change.
* **Use Case:** Use shallow comparison for dependency checking, return cached value when dependencies unchanged.
* **Common Mistake:** Not considering cleanup for expensive computations.
* **Pro Tip:** Consider cleanup for expensive computations.

---

### ⭐ Senior Takeaway

UseMemo prevents unnecessary recalculations, improving React performance.

---

## 🧩 Q170. How do you implement useCallback from scratch?

### 🧠 Concept

`useCallback` returns a memoized version of a function that only changes when dependencies change. Memoize function reference, not execution, to prevent unnecessary re-renders.

---

### 💡 Example

```js
const useCallback = (callback, deps) => {
  const [memoizedCallback, setMemoizedCallback] = useState(() => callback);
  const [prevDeps, setPrevDeps] = useState(deps);
  useEffect(() => {
    const hasChanged = !deps || deps.some((dep, i) => dep !== prevDeps[i]);
    if (hasChanged) { setMemoizedCallback(() => callback); setPrevDeps(deps); }
  }, deps);
  return memoizedCallback;
};
```

---

### 🔍 Deep Insights

* **Rule:** Memoize function reference, not execution, prevent unnecessary re-renders in child components.
* **Use Case:** Use shallow comparison for dependency arrays, return same function reference when deps unchanged.
* **Common Mistake:** Essential for performance optimization in React.
* **Pro Tip:** Essential for performance optimization in React.

---

### ⭐ Senior Takeaway

UseCallback prevents function recreation on every render, optimizing React performance.

---

## 🧩 Q168. What is Compact Number (Intl.NumberFormat)?

### 🧠 Concept

Compact Number formatting displays large numbers in a shortened, human-readable format using locale-specific abbreviations. Uses `Intl.NumberFormat` with `notation: 'compact'` option.

---

### 💡 Example

```js
const formatter = new Intl.NumberFormat('en-US', { notation: 'compact' });
console.log(formatter.format(1000)); // "1K"
console.log(formatter.format(1000000)); // "1M"
```

---

### 🔍 Deep Insights

* **Rule:** Uses `Intl.NumberFormat` with `notation: 'compact'` option.
* **Use Case:** Supports different locales for localized formatting, handles various compact notation styles (K, M, B, T).
* **Common Mistake:** Useful for displaying large numbers in UI components.
* **Pro Tip:** Can be customized with additional formatting options.

---

### ⭐ Senior Takeaway

Compact notation improves readability for large numbers in UI components.

---

## 🧩 Q169. What are JavaScript object property flags and descriptors?

### 🧠 Concept

Property descriptors define the characteristics of object properties, including configurability, enumerability, writability, and value. Use `Object.defineProperty` to set custom descriptors.

---

### 💡 Example

```js
const obj = {};
Object.defineProperty(obj, 'name', {
  value: 'John',
  writable: false,
  enumerable: true,
  configurable: false
});
console.log(Object.getOwnPropertyDescriptor(obj, 'name'));
```

---

### 🔍 Deep Insights

* **Rule:** `writable` (can property value be changed), `enumerable` (shows up in `for...in` loops), `configurable` (can descriptor be modified or property deleted), `value` (the property's value).
* **Use Case:** Use `Object.defineProperty` to set custom descriptors.
* **Common Mistake:** Not understanding how property flags affect object behavior.
* **Pro Tip:** Property descriptors enable fine-grained control over object properties.

---

### ⭐ Senior Takeaway

Descriptors control property behavior and access, enabling advanced object manipulation.

---

## 🧩 Q170. What are server-sent events?

### 🧠 Concept

Server-Sent Events (SSE) enable servers to push data to web pages in real-time using a unidirectional connection. Unidirectional: Server to client only, built on HTTP, simpler than WebSockets.

---

### 💡 Example

```js
const eventSource = new EventSource('/events');
eventSource.onmessage = event => console.log('Received:', event.data);
```

---

### 🔍 Deep Insights

* **Rule:** Unidirectional: Server to client only, built on HTTP, simpler than WebSockets.
* **Use Case:** Automatic reconnection on connection loss, use `text/event-stream` MIME type.
* **Common Mistake:** Good for live updates, notifications, real-time data.
* **Pro Tip:** Simpler than WebSockets for one-way communication.

---

### ⭐ Senior Takeaway

SSE is ideal for server-to-client streaming without WebSocket complexity.

---

## 🧩 Q168. What are proxies in JavaScript used for?

### 🧠 Concept

Proxies allow you to intercept and customize operations performed on objects, enabling meta-programming capabilities. Intercept fundamental operations (get, set, has, delete).

---

### 💡 Example

```js
const handler = { 
  get: (t, p) => (console.log(`Accessing: ${p}`), t[p]), 
  set: (t, p, v) => (t[p] = v, true) 
};
const proxy = new Proxy({}, handler);
proxy.name = 'John'; console.log(proxy.name); // Logs then "John"
```

---

### 🔍 Deep Insights

* **Rule:** Intercept fundamental operations (get, set, has, delete).
* **Use Case:** Enable validation, logging, and virtual properties, used in frameworks for reactivity.
* **Common Mistake:** Can create virtual objects that don't exist.
* **Pro Tip:** Powerful tool for creating advanced abstractions.

---

### ⭐ Senior Takeaway

Proxies enable meta-programming and object interception for advanced patterns.

---

## 🧩 Q169. What are some tools that can be used to measure and analyze JavaScript performance?

### 🧠 Concept

Various tools help measure and analyze JavaScript performance, from browser dev tools to specialized profiling tools. Chrome DevTools, Performance API, and third-party tools provide comprehensive analysis.

---

### 💡 Example

```js
const start = performance.now(); 
/* ... operation ... */ 
const end = performance.now();
console.log(`Operation took ${end - start}ms`);
console.log(performance.memory);
```

---

### 🔍 Deep Insights

* **Rule:** Chrome DevTools (Performance tab, Memory tab, Lighthouse), Performance API (`performance.now()`, `performance.memory`).
* **Use Case:** Web Vitals (LCP, FID, CLS measurements), Profiling (CPU profiling, memory profiling).
* **Common Mistake:** Third-party: New Relic, DataDog, Sentry for production monitoring.
* **Pro Tip:** Use multiple tools for comprehensive performance analysis.

---

### ⭐ Senior Takeaway

Performance monitoring is essential for optimization and debugging.

---

## 🧩 Q170. Explain the concept of a microtask queue?

### 🧠 Concept

The microtask queue processes high-priority tasks that should execute before the next task in the main queue, including Promise callbacks and queueMicrotask. Microtasks have higher priority than macrotasks.

---

### 💡 Example

```js
console.log('1');
setTimeout(() => console.log('2'), 0);
Promise.resolve().then(() => console.log('3'));
queueMicrotask(() => console.log('4'));
console.log('5');
// Output: 1, 5, 3, 4, 2
```

---

### 🔍 Deep Insights

* **Rule:** Microtasks have higher priority than macrotasks, processed after current execution stack is empty.
* **Use Case:** Includes Promise callbacks and `queueMicrotask`.
* **Common Mistake:** Can starve the main queue if not managed properly.
* **Pro Tip:** Essential for understanding async JavaScript execution order.

---

### ⭐ Senior Takeaway

Microtasks run before macrotasks in the event loop, ensuring promise callbacks execute first.

---

## 🧩 Q168. How do you check HTTP status codes in axios and fetch API?

### 🧠 Concept

Fetch requires manual status checking with `response.ok`, while axios automatically rejects on 4xx/5xx status codes. Fetch only rejects on network errors, not HTTP errors.

---

### 💡 Example

```js
fetch('/api/data').then(response => {
  if (!response.ok) throw new Error(`Status: ${response.status}`);
  return response.json();
});

axios.get('/api/data').then(res => res.data)
  .catch(err => console.error('Status:', err.response?.status));
```

---

### 🔍 Deep Insights

* **Rule:** Fetch only rejects on network errors, not HTTP errors—must check `response.ok` or `response.status` manually.
* **Use Case:** Axios automatically rejects promises for status codes >= 400, throwing errors you can catch.
* **Common Mistake:** Remember that `fetch` doesn't throw on 4xx/5xx—this is a common mistake.
* **Pro Tip:** Consider response interceptors in axios for global status code handling.

---

### ⭐ Senior Takeaway

Always handle both network errors and HTTP status errors in API calls.

---

## 🧩 Q169. How can you optimize DOM manipulation for better performance?

### 🧠 Concept

Optimize DOM manipulation by minimizing reflows, using efficient selectors, and leveraging modern APIs for better performance. Minimize reflows and repaints, use `DocumentFragment` for multiple insertions.

---

### 💡 Example

```js
const elements = document.querySelectorAll('.item');
const fragment = document.createDocumentFragment();
items.forEach(item => { 
  const li = document.createElement('li'); 
  li.textContent = item.name; 
  fragment.appendChild(li); 
});
list.appendChild(fragment);
```

---

### 🔍 Deep Insights

* **Rule:** Minimize reflows and repaints, use `DocumentFragment` for multiple insertions.
* **Use Case:** Cache DOM queries and reuse elements, use `requestAnimationFrame` for smooth animations.
* **Common Mistake:** Not batching DOM changes, causing multiple reflows.
* **Pro Tip:** Consider virtual DOM libraries for complex UIs.

---

### ⭐ Senior Takeaway

DOM optimization significantly improves rendering performance in web applications.

---

## 🧩 Q170. Implement `Promise.all()` with a concurrency limit.

### 🧠 Concept

Concurrency limit controls how many promises execute simultaneously, preventing resource exhaustion. Use a pool of active promises and queue remaining ones, starting new promises as others complete.

---

### 💡 Example

```js
const promiseAllWithLimit = async (promises, limit) => {
  const results = [];
  const executing = [];
  
  for (const promise of promises) {
    const p = Promise.resolve(promise).then(result => {
      executing.splice(executing.indexOf(p), 1);
      return result;
    });
    
    results.push(p);
    
    if (executing.length >= limit) {
      await Promise.race(executing);
    }
    
    executing.push(p);
  }
  
  return Promise.all(results);
};

// Usage
const tasks = [1, 2, 3, 4, 5].map(n => 
  () => fetch(`/api/data/${n}`)
);
const results = await promiseAllWithLimit(tasks, 2);
```

---

### 🔍 Deep Insights

* **Rule:** Maintain active pool of promises, start new ones as others complete.
* **Use Case:** Prevents overwhelming APIs or resources with too many concurrent requests.
* **Common Mistake:** Not properly tracking executing promises can cause limit violations.
* **Pro Tip:** Use `Promise.race()` to wait for any promise to complete before starting next.

---

### ⭐ Senior Takeaway

Concurrency limits prevent resource exhaustion while maintaining performance.

---

## 🧩 Q168. Implement a deep clone function for objects.

### 🧠 Concept

Deep cloning creates a completely independent copy of an object, including nested objects and arrays. Handle primitives, objects, arrays, dates, and circular references for a complete solution.

---

### 💡 Example

```js
const deepClone = (obj, visited = new WeakMap()) => {
  if (obj === null || typeof obj !== 'object') return obj;
  if (obj instanceof Date) return new Date(obj);
  if (obj instanceof RegExp) return new RegExp(obj);
  
  if (visited.has(obj)) return visited.get(obj);
  
  const clone = Array.isArray(obj) ? [] : {};
  visited.set(obj, clone);
  
  for (const key in obj) {
    if (obj.hasOwnProperty(key)) {
      clone[key] = deepClone(obj[key], visited);
    }
  }
  
  return clone;
};

// Using structuredClone (modern browsers)
const deepClone = (obj) => structuredClone(obj);
```

---

### 🔍 Deep Insights

* **Rule:** Handle primitives, objects, arrays, dates, and circular references.
* **Use Case:** Essential for immutable state updates and preventing unintended mutations.
* **Common Mistake:** Not handling circular references causes stack overflow.
* **Pro Tip:** `structuredClone()` is native but doesn't support functions or symbols.

---

### ⭐ Senior Takeaway

Deep cloning prevents unintended mutations but requires careful handling of edge cases.

---

## 🧩 Q169. Implement a `groupBy` function that groups array items by a key.

### 🧠 Concept

Grouping organizes array items into objects keyed by a property or computed value. Use `reduce()` to build the grouped object, handling both string keys and computed keys from functions.

---

### 💡 Example

```js
// Group by property
const groupBy = (arr, key) => {
  return arr.reduce((acc, item) => {
    const groupKey = typeof key === 'function' ? key(item) : item[key];
    if (!acc[groupKey]) acc[groupKey] = [];
    acc[groupKey].push(item);
    return acc;
  }, {});
};

// Usage
const users = [
  { name: 'John', age: 25, city: 'NYC' },
  { name: 'Jane', age: 30, city: 'NYC' },
  { name: 'Bob', age: 25, city: 'LA' }
];

groupBy(users, 'age');
// { 25: [{name: 'John', ...}, {name: 'Bob', ...}], 30: [{name: 'Jane', ...}] }

groupBy(users, user => user.city);
// { NYC: [...], LA: [...] }
```

---

### 🔍 Deep Insights

* **Rule:** Support both string keys and function-based key computation.
* **Use Case:** Organize data for display, aggregation, or filtering operations.
* **Common Mistake:** Not initializing arrays for new keys causes undefined errors.
* **Pro Tip:** Use `Map` for better performance with non-string keys.

---

### ⭐ Senior Takeaway

Grouping transforms flat arrays into organized structures for easier data manipulation.

---

## 🧩 Q170. Implement an LRU (Least Recently Used) cache.

### 🧠 Concept

LRU cache evicts least recently used items when capacity is reached. Use a combination of `Map` (for O(1) access) and doubly-linked list (for O(1) insertion/deletion) or leverage `Map`'s insertion order.

---

### 💡 Example

```js
class LRUCache {
  constructor(capacity) {
    this.capacity = capacity;
    this.cache = new Map();
  }
  
  get(key) {
    if (!this.cache.has(key)) return -1;
    const value = this.cache.get(key);
    this.cache.delete(key);
    this.cache.set(key, value);
    return value;
  }
  
  put(key, value) {
    if (this.cache.has(key)) {
      this.cache.delete(key);
    } else if (this.cache.size >= this.capacity) {
      const firstKey = this.cache.keys().next().value;
      this.cache.delete(firstKey);
    }
    this.cache.set(key, value);
  }
}
```

---

### 🔍 Deep Insights

* **Rule:** Move accessed items to end, remove from front when capacity exceeded.
* **Use Case:** Cache frequently accessed data with memory constraints.
* **Common Mistake:** Not updating access order on `get()` operations.
* **Pro Tip:** `Map` maintains insertion order, making it perfect for LRU implementation.

---

### ⭐ Senior Takeaway

LRU cache balances memory usage with access performance for frequently used data.

---

## 🧩 Q168. Create a task scheduler that handles dependencies between tasks.

### 🧠 Concept

Task scheduling with dependencies requires topological sorting to determine execution order. Use graph algorithms to detect cycles and order tasks so dependencies execute before dependents.

---

### 💡 Example

```js
// Approach 1: DFS with Cycle Detection (Recommended)
class TaskSchedulerWithDependencies {
  constructor() {
    this.taskList = new Map();
  }

  addTask(taskId, dependencies) {
    this.taskList.set(taskId, dependencies);
  }

  execute() {
    const visited = new Set();
    const visiting = new Set();
    const result = [];

    const dfs = (taskId) => {
      if (visited.has(taskId)) return;
      
      if (visiting.has(taskId)) {
        throw new Error(`Cycle detected involving task: ${taskId}`);
      }

      visiting.add(taskId);
      const deps = this.taskList.get(taskId) || [];

      for (const dep of deps) {
        if (!this.taskList.has(dep)) {
          throw new Error(`Dependency ${dep} not found for task ${taskId}`);
        }
        dfs(dep);
      }

      visiting.delete(taskId);
      visited.add(taskId);
      result.push(taskId);
    };

    for (let taskId of this.taskList.keys()) {
      if (!visited.has(taskId)) {
        dfs(taskId);
      }
    }
    return result;
  }
}

// Approach 2: Kahn's Algorithm (In-degree based)
class TaskScheduler {
  constructor() {
    this.graph = new Map();
    this.inDegree = new Map();
  }
  
  addTask(task, dependencies = []) {
    this.graph.set(task, dependencies);
    this.inDegree.set(task, dependencies.length);
  }
  
  schedule() {
    const queue = [];
    const result = [];
    
    for (const [task, degree] of this.inDegree) {
      if (degree === 0) queue.push(task);
    }
    
    while (queue.length) {
      const task = queue.shift();
      result.push(task);
      
      for (const [t, deps] of this.graph) {
        if (deps.includes(task)) {
          const newDegree = this.inDegree.get(t) - 1;
          this.inDegree.set(t, newDegree);
          if (newDegree === 0) queue.push(t);
        }
      }
    }
    
    if (result.length !== this.graph.size) {
      throw new Error('Circular dependency detected');
    }
    
    return result;
  }
}

// Usage
const scheduler = new TaskSchedulerWithDependencies();
scheduler.addTask("A", ["B", "C"]);
scheduler.addTask("B", ["D"]);
scheduler.addTask("C", []);
scheduler.addTask("D", []);
const result = scheduler.execute();
console.log('result->', result); // ['D', 'B', 'C', 'A']
```

---

### 🔍 Deep Insights

* **Rule:** DFS approach uses `visiting` set to detect cycles during traversal, `visited` set to avoid reprocessing.
* **Use Case:** Build systems, package managers, workflow orchestration, and CI/CD pipelines.
* **Common Mistake:** Not detecting circular dependencies causes infinite loops or stack overflow.
* **Pro Tip:** DFS provides clear cycle detection; Kahn's algorithm is more efficient for large graphs.

---

### ⭐ Senior Takeaway

Dependency resolution ensures correct execution order in complex systems.

---
## 🧩 Q169. What will be the output of the following code?

### 🧠 Concept

This tests event loop execution order: synchronous code runs first, then microtasks (Promises, queueMicrotask), then macrotasks (setTimeout). Understanding this order is crucial for async JavaScript.

---

### 💡 Example

```js
console.log('Start');
setTimeout(() => console.log('Timeout'), 0);
Promise.resolve().then(() => console.log('Promise'));
queueMicrotask(() => console.log('Microtask'));
console.log('End');
```

---

### 🔍 Deep Insights

* **Rule:** Synchronous code runs first (`Start`, `End`), then microtasks, then macrotasks.
* **Use Case:** Microtasks (Promises and `queueMicrotask`) run before macrotasks (setTimeout).
* **Common Mistake:** Expecting setTimeout to run before promises.
* **Pro Tip:** Microtasks execute in order they were queued (`Promise` before `Microtask`).

**Output:** `Start`, `End`, `Promise`, `Microtask`, `Timeout`

---

### ⭐ Senior Takeaway

Microtasks always run before macrotasks, ensuring promise callbacks execute first.

---

## 🧩 Q170. What will be the output of the following code?

### 🧠 Concept

This tests async/await execution order and how `await` pauses execution, queuing the rest as a microtask. Synchronous code continues while async code waits.

---

### 💡 Example

```js
async function async1() {
  console.log('async1 start');
  await async2();
  console.log('async1 end');
}

async function async2() {
  console.log('async2');
}

console.log('script start');
setTimeout(() => console.log('setTimeout'), 0);
async1();
new Promise(resolve => {
  console.log('promise1');
  resolve();
}).then(() => console.log('promise2'));
console.log('script end');
```

---

### 🔍 Deep Insights

* **Rule:** Synchronous code runs first, `await` pauses execution and returns control.
* **Use Case:** The promise after `await` is queued as a microtask.
* **Common Mistake:** Expecting async code to block synchronous execution.
* **Pro Tip:** All microtasks run before macrotasks.

**Output:** `script start`, `async1 start`, `async2`, `promise1`, `script end`, `promise2`, `async1 end`, `setTimeout`

---

### ⭐ Senior Takeaway

`await` pauses execution but doesn't block—synchronous code continues running.

---

## 🧩 Q168. What will be the output of the following code?

### 🧠 Concept

This tests property descriptors and how `configurable: false` prevents deletion. Getters and setters can transform values, and non-configurable properties can't be deleted.

---

### 💡 Example

```js
const obj = {};
Object.defineProperty(obj, 'prop', {
  get() { return this._value; },
  set(value) { this._value = value * 2; },
  enumerable: true,
  configurable: false
});

obj.prop = 10;
console.log(obj.prop);
delete obj.prop;
console.log(obj.prop);
```

---

### 🔍 Deep Insights

* **Rule:** The setter multiplies by 2, `delete` fails silently because `configurable: false`.
* **Use Case:** Property descriptors control property behavior and access.
* **Common Mistake:** Expecting `delete` to work on non-configurable properties.
* **Pro Tip:** The property remains, so `obj.prop` still returns the value.

**Output:** `20`, `20`

---

### ⭐ Senior Takeaway

Non-configurable properties can't be deleted, making them permanent once set.

---

## 🧩 Q169. What will be the output of the following code?

### 🧠 Concept

This tests prototype chain and how deleting own properties doesn't affect prototype methods. Only deleting from the prototype removes the method for all instances.

---

### 💡 Example

```js
function Person(name) {
  this.name = name;
}

Person.prototype.greet = function() {
  console.log(`Hello, ${this.name}`);
};

const person = new Person('John');
person.greet();

delete person.greet;
person.greet();

delete Person.prototype.greet;
person.greet();
```

---

### 🔍 Deep Insights

* **Rule:** Deleting `person.greet` doesn't remove it from the prototype—the method still exists on the prototype chain.
* **Use Case:** Only deleting from the prototype removes the method for all instances.
* **Common Mistake:** Thinking deleting an instance property removes the prototype method.
* **Pro Tip:** Own properties can shadow prototype properties, but deletion only affects own properties.

**Output:** `Hello, John`, `Hello, John`, `TypeError: person.greet is not a function`

---

### ⭐ Senior Takeaway

Deleting own properties doesn't affect prototype methods—only prototype deletion removes them.

---

## 🧩 Q170. What will be the output of the following code?

### 🧠 Concept

This tests prototype inheritance and how `hasOwnProperty()` distinguishes own vs inherited properties. Deleting inherited properties fails silently.

---

### 💡 Example

```js
const parent = { a: 1 };
const child = Object.create(parent);
child.b = 2;

console.log(child.a);
console.log(child.b);
console.log(child.hasOwnProperty('a'));
console.log(child.hasOwnProperty('b'));

delete child.a;
console.log(child.a);

delete child.b;
console.log(child.b);
```

---

### 🔍 Deep Insights

* **Rule:** `child.a` comes from the prototype, `hasOwnProperty('a')` returns `false` because it's not on `child`.
* **Use Case:** Deleting `child.a` fails silently (it's on the prototype), deleting `child.b` succeeds because it's an own property.
* **Common Mistake:** Expecting to delete inherited properties.
* **Pro Tip:** Use `hasOwnProperty()` to check if a property is own or inherited.

**Output:** `1`, `2`, `false`, `true`, `1`, `undefined`

---

### ⭐ Senior Takeaway

You can only delete own properties, not inherited ones from the prototype.

---

## 🧩 Q168. What will be the output of the following code?

### 🧠 Concept

This tests `Object.freeze()` and how it prevents adding, modifying, or deleting properties. Assignments fail silently in non-strict mode.

---

### 💡 Example

```js
const obj = { a: 1 };
Object.freeze(obj);
obj.a = 2;
obj.b = 3;

console.log(obj.a);
console.log(obj.b);

const arr = [1, 2, 3];
Object.freeze(arr);
arr[0] = 10;
arr.push(4);

console.log(arr);
```

---

### 🔍 Deep Insights

* **Rule:** `Object.freeze()` prevents adding, modifying, or deleting properties.
* **Use Case:** Assignments fail silently in non-strict mode, throws in strict mode.
* **Common Mistake:** `arr.push()` throws in strict mode (TypeError), but in non-strict mode it fails silently.
* **Pro Tip:** Freeze creates truly immutable objects for data protection.

**Output:** `1`, `undefined`, `[1, 2, 3]`

---

### ⭐ Senior Takeaway

`Object.freeze()` creates immutable objects, preventing all property changes.

---

## 🧩 Q169. What will be the output of the following code?

### 🧠 Concept

This tests closures and how all functions sharing the same closure share the same variable reference. Each call increments the shared variable.

---

### 💡 Example

```js
function outer() {
  let count = 0;
  return function inner() {
    count++;
    console.log(count);
    return function innermost() {
      count++;
      console.log(count);
    };
  };
}

const fn = outer();
const innerFn = fn();
innerFn();
fn();
```

---

### 🔍 Deep Insights

* **Rule:** All three functions share the same `count` variable from the closure.
* **Use Case:** Each call increments the shared `count`, the closure persists across all returned functions.
* **Common Mistake:** Thinking each function gets its own copy of the variable.
* **Pro Tip:** Closures capture variables by reference, not by value.

**Output:** `1`, `2`, `3`

---

### ⭐ Senior Takeaway

Closures share variable references, not copies, enabling shared state across functions.

---

## 🧩 Q170. What will be the output of the following code?

### 🧠 Concept

This tests `var` vs `let` scoping in loops and how closures capture variables. `var` is function-scoped, `let` is block-scoped, affecting closure behavior.

---

### 💡 Example

```js
for (var i = 0; i < 3; i++) {
  setTimeout(() => console.log(i), 0);
}

for (let j = 0; j < 3; j++) {
  setTimeout(() => console.log(j), 0);
}
```

---

### 🔍 Deep Insights

* **Rule:** `var` is function-scoped, so there's one `i` shared across iterations—by the time callbacks run, `i` is `3`.
* **Use Case:** `let` is block-scoped, so each iteration creates a new `j` captured by the closure.
* **Common Mistake:** Expecting `var` to work like `let` in loops with closures.
* **Pro Tip:** Always use `let` in loops to avoid closure issues.

**Output:** `3`, `3`, `3`, `0`, `1`, `2`

---

### ⭐ Senior Takeaway

Use `let` in loops to create proper closures—`var` causes shared variable issues.

---

## 🧩 Q168. What will be the output of the following code?

### 🧠 Concept

This tests `this` binding: regular functions have dynamic `this`, arrow functions have lexical `this`. Extracting methods loses `this` binding.

---

### 💡 Example

```js
const obj = {
  value: 10,
  getValue: function() { return this.value; },
  getValueArrow: () => { return this.value; }
};

console.log(obj.getValue());
console.log(obj.getValueArrow());

const extracted = obj.getValue;
console.log(extracted());
```

---

### 🔍 Deep Insights

* **Rule:** Regular functions have dynamic `this` (bound to `obj` when called as a method).
* **Use Case:** Arrow functions have lexical `this` (from outer scope, likely `undefined` in strict mode).
* **Common Mistake:** Extracting a method loses its `this` binding.
* **Pro Tip:** Use `.bind()` or arrow functions to preserve `this` when extracting methods.

**Output:** `10`, `undefined`, `undefined`

---

### ⭐ Senior Takeaway

Extracting methods loses `this` binding—use `.bind()` or arrow functions to preserve it.

---

## 🧩 Q169. What will be the output of the following code?

### 🧠 Concept

This tests class inheritance and `super()`, and how extracting methods loses `this` binding. `super()` calls the parent constructor, but extracted methods lose context.

---

### 💡 Example

```js
class Parent {
  constructor() { this.name = 'Parent'; }
  getName() { return this.name; }
}

class Child extends Parent {
  constructor() {
    super();
    this.name = 'Child';
  }
}

const child = new Child();
console.log(child.getName());

const extracted = child.getName;
console.log(extracted());
```

---

### 🔍 Deep Insights

* **Rule:** `super()` calls the parent constructor, `child.getName()` works because `this` is `child`.
* **Use Case:** Extracting the method loses `this` binding, causing `this` to be `undefined` in strict mode.
* **Common Mistake:** Expecting extracted class methods to maintain `this` binding.
* **Pro Tip:** Use arrow functions or `.bind()` to preserve `this` when extracting methods.

**Output:** `Child`, `TypeError: Cannot read property 'name' of undefined`

---

### ⭐ Senior Takeaway

Extracting class methods loses `this` binding—bind them if you need to extract.

---

## 🧩 Q170. What will be the output of the following code?

### 🧠 Concept

This tests `this` binding in different function types: regular methods, arrow functions, and nested arrow functions. Arrow functions inherit `this` from enclosing scope.

---

### 💡 Example

```js
const obj = {
  a: 1,
  b: function() { console.log(this.a); },
  c: () => { console.log(this.a); },
  d() {
    const nested = () => { console.log(this.a); };
    nested();
  }
};

obj.b();
obj.c();
obj.d();

const extracted = obj.b;
extracted();
```

---

### 🔍 Deep Insights

* **Rule:** Regular methods have `this` bound to the object, arrow functions have lexical `this`.
* **Use Case:** Nested arrow functions inherit `this` from the enclosing method.
* **Common Mistake:** Extracted methods lose `this` binding.
* **Pro Tip:** Arrow functions capture `this` from outer scope, making them useful for callbacks.

**Output:** `1`, `undefined`, `1`, `undefined`

---

### ⭐ Senior Takeaway

Arrow functions preserve `this` from lexical scope, making them ideal for nested callbacks.

---

## 🧩 Q168. What will be the output of the following code?

### 🧠 Concept

This tests async/await execution order: `await` pauses execution and queues the rest as a microtask. Synchronous code continues while async code waits.

---

### 💡 Example

```js
async function test() {
  console.log('1');
  await Promise.resolve();
  console.log('2');
  return Promise.resolve('3');
}

test().then(console.log);
console.log('4');
```

---

### 🔍 Deep Insights

* **Rule:** `await` pauses execution and queues the rest as a microtask.
* **Use Case:** Synchronous code continues (`4`), after the promise resolves execution continues (`2`).
* **Common Mistake:** Expecting async code to block synchronous execution.
* **Pro Tip:** The returned promise resolves with `'3'`, so `.then()` executes.

**Output:** `1`, `4`, `2`, `3`

---

### ⭐ Senior Takeaway

`await` pauses execution but doesn't block—synchronous code continues running.

---

## 🧩 Q169. What will be the output of the following code?

### 🧠 Concept

This tests promise unwrapping: returning a promise from `.then()` unwraps it, adding another microtask. This affects execution order.

---

### 💡 Example

```js
Promise.resolve()
  .then(() => {
    console.log('1');
    return Promise.resolve('2');
  })
  .then(res => {
    console.log(res);
    return Promise.resolve('3');
  })
  .then(console.log);

Promise.resolve().then(() => console.log('4'));
```

---

### 🔍 Deep Insights

* **Rule:** Returning a promise from a `.then()` unwraps it, adding another microtask.
* **Use Case:** Both promise chains run, but microtasks interleave.
* **Common Mistake:** Expecting promises to execute in strict sequential order.
* **Pro Tip:** The unwrapping adds a delay, so `4` appears before `2`.

**Output:** `1`, `4`, `2`, `3`

---

### ⭐ Senior Takeaway

Promise unwrapping adds microtask delays, affecting execution order.

---

## 🧩 Q170. What will be the output of the following code?

### 🧠 Concept

This tests async error handling: `await` on a rejected promise throws an error that can be caught. The `catch` block catches it and returns a value.

---

### 💡 Example

```js
async function test() {
  try {
    return await Promise.reject('Error');
  } catch (e) {
    return 'Caught';
  }
}

test().then(console.log).catch(console.error);
```

---

### 🔍 Deep Insights

* **Rule:** `await` on a rejected promise throws an error.
* **Use Case:** The `catch` block catches it and returns `'Caught'`.
* **Common Mistake:** The function returns a resolved promise with `'Caught'`, so `.then()` executes.
* **Pro Tip:** Always use `await` with rejected promises to catch errors properly.

**Output:** `Caught`

---

### ⭐ Senior Takeaway

`await` converts rejected promises into thrown errors that can be caught.

---

## 🧩 Q168. What will be the output of the following code?

### 🧠 Concept

This tests async error handling without `await`: without `await`, rejected promises are returned directly and can't be caught by try/catch.

---

### 💡 Example

```js
async function test() {
  try {
    return Promise.reject('Error');
  } catch (e) {
    return 'Caught';
  }
}

test().then(console.log).catch(console.error);
```

---

### 🔍 Deep Insights

* **Rule:** Without `await`, the rejected promise is returned directly.
* **Use Case:** The `catch` block doesn't catch it because the error isn't thrown.
* **Common Mistake:** Expecting try/catch to catch unawaited rejected promises.
* **Pro Tip:** The returned promise is rejected, so `.catch()` executes.

**Output:** `Error`

---

### ⭐ Senior Takeaway

Always `await` rejected promises to catch errors—unawaited rejections bypass try/catch.

---

## 🧩 Q169. What will be the output of the following code?

### 🧠 Concept

This tests WeakMap behavior: `delete obj` only removes the reference, not the object itself. WeakMap holds weak references until garbage collection.

---

### 💡 Example

```js
const map = new WeakMap();
const obj = {};

map.set(obj, 'value');
console.log(map.get(obj));

delete obj;
console.log(map.get(obj));
```

---

### 🔍 Deep Insights

* **Rule:** `delete obj` only removes the reference, not the object itself.
* **Use Case:** WeakMap holds weak references, the object becomes eligible for garbage collection when no other references exist.
* **Common Mistake:** The WeakMap entry remains until garbage collection occurs.
* **Pro Tip:** WeakMap keys must be objects and don't prevent garbage collection.

**Output:** `value`, `value`

---

### ⭐ Senior Takeaway

WeakMap entries persist until garbage collection, not until variable deletion.

---

## 🧩 Q170. What will be the output of the following code?

### 🧠 Concept

This tests Symbol uniqueness: each `Symbol()` call creates a unique symbol, even with the same description. Symbols are not enumerable.

---

### 💡 Example

```js
const sym1 = Symbol('id');
const sym2 = Symbol('id');
const obj = {
  [sym1]: 'value1',
  [sym2]: 'value2'
};

console.log(obj[sym1]);
console.log(obj[sym2]);
console.log(sym1 === sym2);
console.log(Object.keys(obj).length);
```

---

### 🔍 Deep Insights

* **Rule:** Each `Symbol()` call creates a unique symbol, even with the same description.
* **Use Case:** Symbols are not enumerable, so `Object.keys()` doesn't include them.
* **Common Mistake:** Thinking symbols with the same description are equal.
* **Pro Tip:** Use `Object.getOwnPropertySymbols()` to get symbols.

**Output:** `value1`, `value2`, `false`, `0`

---

### ⭐ Senior Takeaway

Symbols are always unique—same description doesn't mean same symbol.

---

## 🧩 Q168. What will be the output of the following code?

### 🧠 Concept

This tests Proxy interception: proxies intercept `get` and `set` operations, allowing custom behavior. The proxy modifies values on get and set.

---

### 💡 Example

```js
const target = { a: 1 };
const handler = {
  get(target, prop) {
    return prop in target ? target[prop] * 2 : 0;
  },
  set(target, prop, value) {
    target[prop] = value * 2;
    return true;
  }
};

const proxy = new Proxy(target, handler);
proxy.b = 5;
console.log(proxy.a);
console.log(proxy.b);
console.log(proxy.c);
console.log(target.a);
console.log(target.b);
```

---

### 🔍 Deep Insights

* **Rule:** The proxy intercepts `get` and `set` operations, getting `a` returns `1 * 2 = 2`.
* **Use Case:** Setting `b = 5` stores `5 * 2 = 10` in the target, getting `c` (not in target) returns `0`.
* **Common Mistake:** The target object is modified by the proxy.
* **Pro Tip:** Proxies enable meta-programming and object interception.

**Output:** `2`, `10`, `0`, `1`, `10`

---

### ⭐ Senior Takeaway

Proxies intercept operations and can modify behavior while still affecting the target.

---

## 🧩 Q169. What will be the output of the following code?

### 🧠 Concept

This tests generator behavior: each `next()` call resumes the generator. `yield` pauses and returns a value, `return` ends the generator.

---

### 💡 Example

```js
function* generator() {
  yield 1;
  yield 2;
  yield 3;
  return 4;
}

const gen = generator();
console.log(gen.next());
console.log(gen.next());
console.log(gen.next());
console.log(gen.next());
console.log(gen.next());
```

---

### 🔍 Deep Insights

* **Rule:** Each `next()` call resumes the generator, `yield` pauses and returns a value.
* **Use Case:** `return` ends the generator, after `done: true` subsequent calls return `{ value: undefined, done: true }`.
* **Common Mistake:** Expecting generators to continue after `return`.
* **Pro Tip:** Generators can pause and resume, making them useful for lazy evaluation.

**Output:** `{ value: 1, done: false }`, `{ value: 2, done: false }`, `{ value: 3, done: false }`, `{ value: 4, done: true }`, `{ value: undefined, done: true }`

---

### ⭐ Senior Takeaway

Generators pause at `yield` and resume at `next()`, enabling lazy evaluation.

---

## 🧩 Q170. What will be the output of the following code?

### 🧠 Concept

This tests async generators: `for await...of` automatically awaits each yielded promise. The async generator yields promises, which are unwrapped.

---

### 💡 Example

```js
async function* asyncGenerator() {
  yield Promise.resolve(1);
  yield Promise.resolve(2);
  yield Promise.resolve(3);
}

(async () => {
  for await (const value of asyncGenerator()) {
    console.log(value);
  }
})();
```

---

### 🔍 Deep Insights

* **Rule:** `for await...of` automatically awaits each yielded promise.
* **Use Case:** The async generator yields promises, which are unwrapped by `for await...of`.
* **Common Mistake:** Expecting to manually await each value.
* **Pro Tip:** Async generators enable streaming data from async sources.

**Output:** `1`, `2`, `3`

---

### ⭐ Senior Takeaway

`for await...of` automatically unwraps promises from async generators.

---

## 🧩 Q168. What will be the output of the following code?

### 🧠 Concept

This tests sparse arrays: setting an index beyond length creates a sparse array with empty slots. `map()` skips empty slots but preserves structure.

---

### 💡 Example

```js
const arr = [1, 2, 3];
arr[10] = 10;

console.log(arr.length);
console.log(arr[5]);
console.log(arr);

const mapped = arr.map(x => x * 2);
console.log(mapped);
```

---

### 🔍 Deep Insights

* **Rule:** Setting an index beyond length creates a sparse array, empty slots are `undefined`.
* **Use Case:** `map()` skips empty slots but preserves the array structure with empty slots.
* **Common Mistake:** Expecting `map()` to fill empty slots.
* **Pro Tip:** Sparse arrays have `undefined` values in empty slots.

**Output:** `11`, `undefined`, `[1, 2, 3, <7 empty items>, 10]`, `[2, 4, 6, <7 empty items>, 20]`

---

### ⭐ Senior Takeaway

Sparse arrays preserve empty slots—`map()` skips them but keeps the structure.

---

## 🧩 Q169. What will be the output of the following code?

### 🧠 Concept

This tests array length manipulation: setting `length` to a larger value extends the array with empty slots, setting it smaller truncates the array.

---

### 💡 Example

```js
const arr = [1, 2, 3];
arr.length = 10;
console.log(arr);
console.log(arr.length);

arr.length = 2;
console.log(arr);
console.log(arr.length);
```

---

### 🔍 Deep Insights

* **Rule:** Setting `length` to a larger value extends the array with empty slots.
* **Use Case:** Setting `length` to a smaller value truncates the array, removing elements beyond the new length.
* **Common Mistake:** Expecting length changes to preserve all elements.
* **Pro Tip:** Array length is mutable and directly affects array contents.

**Output:** `[1, 2, 3, <7 empty items>]`, `10`, `[1, 2]`, `2`

---

### ⭐ Senior Takeaway

Array length is mutable—increasing creates empty slots, decreasing truncates.

---

## 🧩 Q170. What will be the output of the following code?

### 🧠 Concept

This tests Set and Map behavior: Sets store unique values (duplicates ignored), Maps store unique keys (duplicate keys overwrite). The last value for a key is kept.

---

### 💡 Example

```js
const set = new Set([1, 2, 3, 3, 2, 1]);
console.log(set.size);
console.log([...set]);

const map = new Map([
  ['a', 1],
  ['b', 2],
  ['a', 3]
]);
console.log(map.size);
console.log([...map]);
```

---

### 🔍 Deep Insights

* **Rule:** Sets store unique values, duplicates are ignored.
* **Use Case:** Maps store unique keys, duplicate keys overwrite previous values.
* **Common Mistake:** Expecting Maps to keep all values for duplicate keys.
* **Pro Tip:** The last value for a key is kept in Maps.

**Output:** `3`, `[1, 2, 3]`, `2`, `[['a', 3], ['b', 2]]`

---

### ⭐ Senior Takeaway

Sets remove duplicates, Maps overwrite duplicate keys with the last value.

---

## 🧩 Q168. What will be the output of the following code?

### 🧠 Concept

This tests object key enumeration methods: `Object.keys()` returns enumerable string keys, `Object.getOwnPropertySymbols()` returns symbol keys, `Reflect.ownKeys()` returns all keys.

---

### 💡 Example

```js
const obj = {
  a: 1,
  b: 2,
  [Symbol('c')]: 3
};

console.log(Object.keys(obj));
console.log(Object.getOwnPropertyNames(obj));
console.log(Object.getOwnPropertySymbols(obj));
console.log(Reflect.ownKeys(obj));
```

---

### 🔍 Deep Insights

* **Rule:** `Object.keys()` returns enumerable string keys, `Object.getOwnPropertyNames()` returns all string keys (enumerable or not).
* **Use Case:** `Object.getOwnPropertySymbols()` returns symbol keys, `Reflect.ownKeys()` returns all keys (strings and symbols).
* **Common Mistake:** Expecting `Object.keys()` to include symbols.
* **Pro Tip:** Use `Reflect.ownKeys()` to get all keys including symbols.

**Output:** `['a', 'b']`, `['a', 'b']`, `[Symbol(c)]`, `['a', 'b', Symbol(c)]`

---

### ⭐ Senior Takeaway

Different key methods return different subsets—use `Reflect.ownKeys()` for all keys.

---

## 🧩 Q169. What will be the output of the following code?

### 🧠 Concept

This tests getters and setters: getters run when reading, setters run when writing. The getter returns computed value, setter transforms input.

---

### 💡 Example

```js
const obj = {
  a: 1,
  get b() { return this.a * 2; },
  set b(value) { this.a = value / 2; }
};

console.log(obj.b);
obj.b = 10;
console.log(obj.a);
console.log(obj.b);
```

---

### 🔍 Deep Insights

* **Rule:** The getter returns `this.a * 2` (1 * 2 = 2).
* **Use Case:** The setter sets `this.a = value / 2` (10 / 2 = 5).
* **Common Mistake:** The getter then returns `5 * 2 = 10`.
* **Pro Tip:** Getters and setters enable computed properties and validation.

**Output:** `2`, `5`, `10`

---

### ⭐ Senior Takeaway

Getters and setters transform values on read/write, enabling computed properties.

---

## 🧩 Q170. What will be the output of the following code?

### 🧠 Concept

This tests prototype inheritance: `foo.a` is an own property, `foo.b` comes from the prototype. Changing the prototype affects all instances.

---

### 💡 Example

```js
function Foo() {
  this.a = 1;
}

Foo.prototype.b = 2;

const foo = new Foo();
console.log(foo.a);
console.log(foo.b);
console.log(foo.hasOwnProperty('a'));
console.log(foo.hasOwnProperty('b'));

Foo.prototype.b = 3;
console.log(foo.b);
```

---

### 🔍 Deep Insights

* **Rule:** `foo.a` is an own property, `foo.b` comes from the prototype.
* **Use Case:** Changing `Foo.prototype.b` affects all instances because they share the prototype.
* **Common Mistake:** Expecting instance properties to be independent of prototype changes.
* **Pro Tip:** Prototype changes affect all instances that inherit from it.

**Output:** `1`, `2`, `true`, `false`, `3`

---

### ⭐ Senior Takeaway

Prototype changes affect all instances—they share the same prototype object.

---

## 🧩 Q168. What will be the output of the following code?

### 🧠 Concept

This tests `Object.create(null)`: creates an object without a prototype, so it has no inherited methods like `toString()` or `hasOwnProperty()`.

---

### 💡 Example

```js
const obj = Object.create(null);
obj.a = 1;

console.log(obj.a);
console.log(obj.toString);
console.log(obj.hasOwnProperty('a'));
```

---

### 🔍 Deep Insights

* **Rule:** `Object.create(null)` creates an object without a prototype.
* **Use Case:** It has no inherited methods like `toString()` or `hasOwnProperty()`.
* **Common Mistake:** Expecting standard object methods on prototype-less objects.
* **Pro Tip:** Use `Object.prototype.hasOwnProperty.call(obj, 'a')` instead.

**Output:** `1`, `undefined`, `TypeError: obj.hasOwnProperty is not a function`

---

### ⭐ Senior Takeaway

Prototype-less objects have no inherited methods—use `Object.prototype` methods directly.

---

## 🧩 Q169. What will be the output of the following code?

### 🧠 Concept

This tests `Object.seal()`: prevents adding or deleting properties but allows modifying existing ones. Assignments to existing properties succeed.

---

### 💡 Example

```js
const obj = { a: 1 };
Object.seal(obj);
obj.a = 2;
obj.b = 3;
delete obj.a;

console.log(obj.a);
console.log(obj.b);
console.log(Object.isSealed(obj));
```

---

### 🔍 Deep Insights

* **Rule:** `Object.seal()` prevents adding or deleting properties but allows modifying existing ones.
* **Use Case:** `obj.a = 2` succeeds, `obj.b = 3` fails (silently), `delete obj.a` fails (silently).
* **Common Mistake:** Expecting `seal()` to prevent all modifications.
* **Pro Tip:** Seal allows property value changes but prevents structural changes.

**Output:** `2`, `undefined`, `true`

---

### ⭐ Senior Takeaway

`Object.seal()` allows value changes but prevents adding or deleting properties.

---

## 🧩 Q170. What will be the output of the following code?

### 🧠 Concept

This tests `Object.preventExtensions()`: prevents adding new properties but allows modifying or deleting existing ones. More permissive than `seal()`.

---

### 💡 Example

```js
const obj = { a: 1 };
Object.preventExtensions(obj);
obj.a = 2;
obj.b = 3;

console.log(obj.a);
console.log(obj.b);
console.log(Object.isExtensible(obj));
```

---

### 🔍 Deep Insights

* **Rule:** `Object.preventExtensions()` prevents adding new properties but allows modifying or deleting existing ones.
* **Use Case:** `obj.a = 2` succeeds, `obj.b = 3` fails (silently).
* **Common Mistake:** Expecting it to prevent all modifications like `freeze()`.
* **Pro Tip:** Less restrictive than `seal()` or `freeze()`—only prevents new properties.

**Output:** `2`, `undefined`, `false`

---

### ⭐ Senior Takeaway

`Object.preventExtensions()` only prevents new properties, not value changes.

---

## 🧩 Q168. What will be the output of the following code?

### 🧠 Concept

This tests tagged template literals: they call the function with an array of strings and an array of interpolated values. The function can process and return a custom result.

---

### 💡 Example

```js
function tag(strings, ...values) {
  console.log(strings);
  console.log(values);
  return strings[0] + values[0] + strings[1] + values[1];
}

const name = 'John';
const age = 30;
const result = tag`Hello ${name}, you are ${age}!`;
console.log(result);
```

---

### 🔍 Deep Insights

* **Rule:** Tagged template literals call the function with an array of strings and an array of interpolated values.
* **Use Case:** The strings array contains the text between interpolations.
* **Common Mistake:** The function can process and return a custom result.
* **Pro Tip:** Tagged templates enable custom string processing and sanitization.

**Output:** `['Hello ', ', you are ', '!']`, `['John', 30]`, `Hello John, you are 30!`

---

### ⭐ Senior Takeaway

Tagged templates enable custom string processing with access to raw strings and values.

---

## 🧩 Q169. What will be the output of the following code?

### 🧠 Concept

This tests nullish coalescing (`??`) and optional chaining (`?.`): `??` only checks null/undefined, not falsy values. `?.` safely accesses nested properties.

---

### 💡 Example

```js
const obj = {
  a: null,
  b: undefined,
  c: 0,
  d: false,
  e: ''
};

console.log(obj.a ?? 'default');
console.log(obj.b ?? 'default');
console.log(obj.c ?? 'default');
console.log(obj.d ?? 'default');
console.log(obj.e ?? 'default');

console.log(obj.a?.prop?.nested);
console.log(obj.b?.prop);
console.log(obj.f?.prop);
```

---

### 🔍 Deep Insights

* **Rule:** Nullish coalescing (`??`) only uses the default for `null` or `undefined`, not for other falsy values like `0`, `false`, or `''`.
* **Use Case:** Optional chaining (`?.`) safely accesses nested properties, returning `undefined` if any part is `null` or `undefined`.
* **Common Mistake:** Using `??` when you want to check for falsy values.
* **Pro Tip:** `??` is stricter than `||`—only checks nullish values.

**Output:** `default`, `default`, `0`, `false`, `''`, `undefined`, `undefined`, `undefined`

---

### ⭐ Senior Takeaway

`??` only checks null/undefined, not falsy values—use `||` for falsy checks.

---

## 🧩 Q170. What will be the output of the following code?

### 🧠 Concept

This tests `Symbol.toPrimitive`: controls how an object is converted to a primitive. The `hint` parameter indicates the preferred type (number, string, default).

---

### 💡 Example

```js
const obj = {
  value: 10,
  [Symbol.toPrimitive](hint) {
    if (hint === 'number') return 42;
    if (hint === 'string') return 'hello';
    return 'default';
  }
};

console.log(+obj);
console.log(String(obj));
console.log(obj + '');
console.log(obj == 'default');
console.log(obj * 2);
```

---

### 🔍 Deep Insights

* **Rule:** `Symbol.toPrimitive` controls how an object is converted to a primitive.
* **Use Case:** The `hint` parameter indicates the preferred type: `'number'` for numeric operations, `'string'` for string operations, `'default'` for equality comparisons.
* **Common Mistake:** `+obj` uses `'number'`, `String(obj)` uses `'string'`, `obj + ''` uses `'string'`, `==` uses `'default'`.
* **Pro Tip:** `Symbol.toPrimitive` enables custom type conversion behavior.

**Output:** `42`, `hello`, `hello`, `true`, `84`

---

### ⭐ Senior Takeaway

`Symbol.toPrimitive` enables custom type conversion based on operation context.

---

## 🧩 Q168. What will be the output of the following code?

### 🧠 Concept

This tests BigInt behavior: operations with BigInt return BigInt. Strict equality compares type and value, loose equality allows type coercion.

---

### 💡 Example

```js
const a = 10n;
const b = 20n;

console.log(a + b);
console.log(typeof (a + b));
console.log(a === 10);
console.log(a == 10);
console.log(a > 5);
console.log(Number(a) + 5);
```

---

### 🔍 Deep Insights

* **Rule:** BigInt is a primitive for arbitrary-precision integers, operations with BigInt return BigInt.
* **Use Case:** `typeof` returns `'bigint'`, strict equality (`===`) compares type and value, so `a === 10` is `false`.
* **Common Mistake:** Loose equality (`==`) allows type coercion, so `a == 10` is `true`.
* **Pro Tip:** BigInt can be compared with numbers and converted with `Number()`.

**Output:** `30n`, `bigint`, `false`, `true`, `true`, `15`

---

### ⭐ Senior Takeaway

BigInt operations return BigInt—strict equality requires matching types.

---

## 🧩 Q169. What will be the output of the following code?

### 🧠 Concept

This tests `bind()` permanence: `bind()` creates a new function with permanently bound `this`. Once bound, the `this` value cannot be changed with `call()` or `apply()`.

---

### 💡 Example

```js
function greet() {
  return this.name;
}

const obj1 = { name: 'John' };
const obj2 = { name: 'Jane' };

const boundGreet1 = greet.bind(obj1);
const boundGreet2 = greet.bind(obj2);

console.log(boundGreet1());
console.log(boundGreet2());
console.log(boundGreet1.call(obj2));
console.log(boundGreet2.apply(obj1));
```

---

### 🔍 Deep Insights

* **Rule:** `bind()` creates a new function with permanently bound `this`.
* **Use Case:** Once bound, the `this` value cannot be changed with `call()` or `apply()`.
* **Common Mistake:** Expecting `call()` or `apply()` to override bound `this`.
* **Pro Tip:** The bound function always uses the original bound context.

**Output:** `John`, `Jane`, `John`, `Jane`

---

### ⭐ Senior Takeaway

Bound `this` is permanent—`call()` and `apply()` can't override it.

---

## 🧩 Q170. What will be the output of the following code?

### 🧠 Concept

This tests destructuring defaults: default values only apply when the property is `undefined`. `null`, `0`, and `false` are not `undefined`, so they are used as-is.

---

### 💡 Example

```js
const obj = { a: undefined, b: null, c: 0, d: false };

const { a = 'defaultA', b = 'defaultB', c = 'defaultC', d = 'defaultD', e = 'defaultE' } = obj;

console.log(a, b, c, d, e);
```

---

### 🔍 Deep Insights

* **Rule:** In destructuring, default values only apply when the property is `undefined`.
* **Use Case:** `null`, `0`, and `false` are not `undefined`, so they are used as-is.
* **Common Mistake:** Expecting defaults to work with `null` or falsy values.
* **Pro Tip:** Missing properties use default values.

**Output:** `defaultA`, `null`, `0`, `false`, `defaultE`

---

### ⭐ Senior Takeaway

Destructuring defaults only work with `undefined`, not other falsy values.

---

## 🧩 Q168. What will be the output of the following code?

### 🧠 Concept

This tests variable shadowing: inner scopes can declare variables with the same name as outer scopes, creating new bindings. Each scope has its own variable.

---

### 💡 Example

```js
let x = 1;
let y = 2;

function outer() {
  let x = 10;
  
  function inner() {
    let x = 100;
    console.log(x, y);
  }
  
  inner();
  console.log(x, y);
}

outer();
console.log(x, y);
```

---

### 🔍 Deep Insights

* **Rule:** Variable shadowing occurs when inner scopes declare variables with the same name as outer scopes.
* **Use Case:** Each scope has its own `x`, `y` is not shadowed, so all functions access the global `y = 2`.
* **Common Mistake:** Expecting shadowed variables to affect outer scopes.
* **Pro Tip:** Shadowing creates new bindings that don't affect outer scopes.

**Output:** `100 2`, `10 2`, `1 2`

---

### ⭐ Senior Takeaway

Variable shadowing creates new bindings—outer variables remain unchanged.

---

## 🧩 Q169. What will be the output of the following code?

### 🧠 Concept

This tests `this` in strict mode: `this` is `undefined` for regular functions called without context. Inner functions don't inherit `this` from outer functions.

---

### 💡 Example

```js
'use strict';

function test() {
  console.log(this);
}

const obj = {
  test: function() {
    console.log(this);
    function inner() {
      console.log(this);
    }
    inner();
  }
};

test();
obj.test();
```

---

### 🔍 Deep Insights

* **Rule:** In strict mode, `this` is `undefined` for regular functions called without context.
* **Use Case:** When called as a method, `this` refers to the object.
* **Common Mistake:** Inner functions don't inherit `this` from outer functions—they have their own `this` (undefined in strict mode).
* **Pro Tip:** Use arrow functions to preserve `this` from outer scope.

**Output:** `undefined`, `{ test: [Function: test] }`, `undefined`

---

### ⭐ Senior Takeaway

In strict mode, bare function calls have `undefined` `this`—use arrow functions to preserve context.

---

## 🧩 Q170. What will be the output of the following code?

### 🧠 Concept

This tests Proxy traps: proxies intercept `get`, `has`, and `ownKeys` operations. Accessing non-existent properties through proxy can return transformed values.

---

### 💡 Example

```js
const handler = {
  get(target, prop) {
    if (prop === 'constructor') return target.constructor;
    return target[prop] * 2;
  },
  has(target, prop) {
    return prop in target;
  },
  ownKeys(target) {
    return Object.keys(target);
  }
};

const target = { a: 1, b: 2 };
const proxy = new Proxy(target, handler);

console.log(proxy.a);
console.log('a' in proxy);
console.log(Object.keys(proxy));
console.log(proxy.c);
```

---

### 🔍 Deep Insights

* **Rule:** The Proxy intercepts `get`, returning `target[prop] * 2`.
* **Use Case:** Accessing `proxy.a` returns `1 * 2 = 2`, the `has` trap returns `true` for existing properties.
* **Common Mistake:** `ownKeys` returns the target's keys, accessing a non-existent property returns `undefined * 2 = NaN`.
* **Pro Tip:** Proxies can create virtual properties that don't exist on the target.

**Output:** `2`, `true`, `['a', 'b']`, `NaN`

---

### ⭐ Senior Takeaway

Proxies can intercept and transform property access, enabling virtual properties.

---

## 🧩 Q168. What will be the output of the following code?

### 🧠 Concept

This tests generator error handling: generators can use try/catch blocks. Errors thrown in generators can be caught and the generator can continue yielding.

---

### 💡 Example

```js
function* generator() {
  try {
    yield 1;
    yield 2;
    throw new Error('Error');
    yield 3;
  } catch (e) {
    yield 4;
  }
  yield 5;
}

const gen = generator();
console.log(gen.next());
console.log(gen.next());
console.log(gen.next());
console.log(gen.next());
console.log(gen.next());
```

---

### 🔍 Deep Insights

* **Rule:** The generator yields `1` and `2`, the error is thrown and caught by the `catch` block, which yields `4`.
* **Use Case:** Execution continues and yields `5`, the generator completes after `5`.
* **Common Mistake:** Expecting generators to stop after errors.
* **Pro Tip:** Generators can recover from errors and continue execution.

**Output:** `{ value: 1, done: false }`, `{ value: 2, done: false }`, `{ value: 4, done: false }`, `{ value: 5, done: false }`, `{ value: undefined, done: true }`

---

### ⭐ Senior Takeaway

Generators can catch errors and continue, making them resilient to failures.

---

## 🧩 Q169. What will be the output of the following code?

### 🧠 Concept

This tests `this` binding in nested functions: regular methods have `this` bound to the object, arrow functions have lexical `this`. Nested arrow functions inherit `this` from enclosing method.

---

### 💡 Example

```js
const obj = {
  a: 1,
  b() { return this.a; },
  c: () => { return this.a; },
  d: function() {
    const self = this;
    return {
      e: () => this.a,
      f: function() { return self.a; }
    };
  }
};

console.log(obj.b());
console.log(obj.c());
console.log(obj.d().e());
console.log(obj.d().f());
```

---

### 🔍 Deep Insights

* **Rule:** Regular methods have `this` bound to the object, arrow functions have lexical `this`.
* **Use Case:** The arrow function in `d()` captures `this` from `obj.d()`, so it works.
* **Common Mistake:** The regular function in `d()` uses `self` to capture `this`.
* **Pro Tip:** Arrow functions preserve `this` from outer scope, making them useful for nested callbacks.

**Output:** `1`, `undefined`, `1`, `1`

---

### ⭐ Senior Takeaway

Arrow functions preserve `this` from lexical scope, solving nested callback `this` issues.

---

## 🧩 Q170. What will be the output of the following code?

### 🧠 Concept

This tests `Symbol()` vs `Symbol.for()`: `Symbol()` creates unique symbols, `Symbol.for()` creates/retrieves symbols from a global registry. Same description doesn't mean same symbol.

---

### 💡 Example

```js
const obj = {
  [Symbol('a')]: 1,
  [Symbol('b')]: 2,
  c: 3
};

const sym1 = Symbol.for('shared');
const sym2 = Symbol.for('shared');

obj[sym1] = 'shared1';
obj[sym2] = 'shared2';

console.log(obj[Symbol('a')]);
console.log(obj[sym1]);
console.log(obj[sym2]);
console.log(Symbol('a') === Symbol('a'));
console.log(Symbol.for('shared') === Symbol.for('shared'));
```

---

### 🔍 Deep Insights

* **Rule:** `Symbol()` creates unique symbols; `Symbol('a') !== Symbol('a')`.
* **Use Case:** `Symbol.for()` creates/retrieves symbols from a global registry; `Symbol.for('shared') === Symbol.for('shared')`.
* **Common Mistake:** Accessing with a different `Symbol('a')` returns `undefined` because it's a different symbol.
* **Pro Tip:** `sym1` and `sym2` reference the same symbol, so both return `'shared2'` (the last assigned value).

**Output:** `undefined`, `shared2`, `shared2`, `false`, `true`

---

### ⭐ Senior Takeaway

`Symbol()` creates unique symbols, `Symbol.for()` creates shared symbols from a registry.

---

## 🧩 Q168. What will be the output of the following code?

### 🧠 Concept

This tests method chaining: each method returns `this` for chaining. Method chaining works because each method returns the object.

---

### 💡 Example

```js
const obj = {
  value: 1,
  increment() {
    this.value++;
    return this;
  },
  add(n) {
    this.value += n;
    return this;
  },
  getValue() {
    return this.value;
  }
};

console.log(obj.increment().add(5).getValue());
```

---

### 🔍 Deep Insights

* **Rule:** Method chaining works because each method returns `this`.
* **Use Case:** `increment()` makes `value = 2`, `add(5)` makes `value = 7`, `getValue()` returns `7`.
* **Common Mistake:** Forgetting to return `this` breaks chaining.
* **Pro Tip:** Returning `this` enables fluent APIs and method chaining.

**Output:** `7`

---

### ⭐ Senior Takeaway

Return `this` from methods to enable fluent method chaining.

---

## 🧩 Q169. What will be the output of the following code?

### 🧠 Concept

This tests infinite generators: generators can run indefinitely with `while (true)`. Each `next()` call resumes execution, computes the next value, and yields it.

---

### 💡 Example

```js
function* fibonacci() {
  let [prev, curr] = [0, 1];
  while (true) {
    yield curr;
    [prev, curr] = [curr, prev + curr];
  }
}

const gen = fibonacci();
console.log(gen.next().value);
console.log(gen.next().value);
console.log(gen.next().value);
console.log(gen.next().value);
```

---

### 🔍 Deep Insights

* **Rule:** The generator yields Fibonacci numbers, each `next()` call resumes execution.
* **Use Case:** Computes the next number and yields it, the generator can run indefinitely.
* **Common Mistake:** Expecting generators to have a fixed length.
* **Pro Tip:** Generators enable lazy evaluation of infinite sequences.

**Output:** `1`, `1`, `2`, `3`

---

### ⭐ Senior Takeaway

Generators enable lazy evaluation of infinite sequences efficiently.

---

## 🧩 Q170. What will be the output of the following code?

### 🧠 Concept

This tests closure vs `this` capture: `self` captures `this` from the outer function (`obj`). The inner function has its own `this` (global/undefined).

---

### 💡 Example

```js
const obj = {
  a: 1,
  b: function() {
    const self = this;
    return function() {
      console.log(self.a);
      console.log(this.a);
    };
  }
};

const fn = obj.b();
fn();
```

---

### 🔍 Deep Insights

* **Rule:** `self` captures `this` from the outer function (`obj`).
* **Use Case:** The inner function has its own `this` (global/undefined).
* **Common Mistake:** `self.a` is `1`, `this.a` is `undefined` because `this` is not `obj`.
* **Pro Tip:** Use closures or arrow functions to preserve `this` in nested functions.

**Output:** `1`, `undefined`

---

### ⭐ Senior Takeaway

Closures capture variables, but `this` is dynamic—use closures or arrows to preserve it.

---

## 🧩 Q168. What will be the output of the following code?

### 🧠 Concept

This tests arrow function `this` capture: arrow functions capture `this` from the enclosing scope. When `obj.b()` is called, `this` is `obj`, so the arrow captures `obj`.

---

### 💡 Example

```js
const obj = {
  a: 1,
  b: function() {
    return () => { console.log(this.a); };
  }
};

const fn = obj.b();
fn();

const extracted = obj.b;
const fn2 = extracted();
fn2();
```

---

### 🔍 Deep Insights

* **Rule:** Arrow functions capture `this` from the enclosing scope.
* **Use Case:** When `obj.b()` is called, `this` is `obj`, so the arrow function captures `obj`.
* **Common Mistake:** When `extracted()` is called, `this` is `undefined` (strict mode), so the arrow function captures `undefined`.
* **Pro Tip:** Arrow functions preserve `this` from where they're defined, not where they're called.

**Output:** `1`, `undefined`

---

### ⭐ Senior Takeaway

Arrow functions capture `this` from definition context, not call context.

---

## 🧩 Q169. What will be the output of the following code?

### 🧠 Concept

This tests promise error handling: errors in promise chains are caught by `.catch()`, which can return a value to continue the chain. The chain continues after error handling.

---

### 💡 Example

```js
Promise.resolve(1)
  .then(val => {
    console.log(val);
    return val + 1;
  })
  .then(val => {
    console.log(val);
    throw new Error('Error');
  })
  .then(val => {
    console.log('Not reached');
  })
  .catch(err => {
    console.log(err.message);
    return 10;
  })
  .then(val => {
    console.log(val);
  });
```

---

### 🔍 Deep Insights

* **Rule:** The first `.then()` logs `1` and returns `2`, the second `.then()` logs `2` and throws.
* **Use Case:** The error is caught by `.catch()`, which logs the message and returns `10`.
* **Common Mistake:** The final `.then()` receives `10`.
* **Pro Tip:** `.catch()` can recover from errors and continue the promise chain.

**Output:** `1`, `2`, `Error`, `10`

---

### ⭐ Senior Takeaway

`.catch()` can recover from errors and continue the promise chain with a return value.

---

## 🧩 Q170. What will be the output of the following code?

### 🧠 Concept

This tests Map reference equality: Maps use reference equality for keys. `obj1` and `obj2` are different objects, so they create separate entries.

---

### 💡 Example

```js
const map = new Map();
const obj1 = { a: 1 };
const obj2 = { a: 1 };

map.set(obj1, 'value1');
map.set(obj2, 'value2');

console.log(map.get(obj1));
console.log(map.get(obj2));
console.log(map.size);

map.set(obj1, 'value3');
console.log(map.get(obj1));
console.log(map.size);
```

---

### 🔍 Deep Insights

* **Rule:** Maps use reference equality for keys.
* **Use Case:** `obj1` and `obj2` are different objects, so they create separate entries.
* **Common Mistake:** Setting the same key again overwrites the value but doesn't change the size.
* **Pro Tip:** Maps compare keys by reference, not by value.

**Output:** `value1`, `value2`, `2`, `value3`, `2`

---

### ⭐ Senior Takeaway

Maps use reference equality for keys—same content doesn't mean same key.

---

## 🧩 Q168. What will be the output of the following code?

### 🧠 Concept

This tests Set uniqueness: Sets store unique values. Adding `3` again doesn't change the set. `delete(2)` removes `2`.

---

### 💡 Example

```js
const set = new Set([1, 2, 3]);
set.add(3);
set.add(4);
set.delete(2);

console.log(set.size);
console.log([...set]);
console.log(set.has(2));
console.log(set.has(4));
```

---

### 🔍 Deep Insights

* **Rule:** Sets store unique values, adding `3` again doesn't change the set.
* **Use Case:** `delete(2)` removes `2`, `has(2)` returns `false`, `has(4)` returns `true`.
* **Common Mistake:** Expecting `add()` to create duplicates.
* **Pro Tip:** Sets automatically remove duplicates, making them useful for unique collections.

**Output:** `3`, `[1, 3, 4]`, `false`, `true`

---

### ⭐ Senior Takeaway

Sets automatically enforce uniqueness—duplicates are ignored.

---

## 🧩 Q169. What will be the output of the following code?

### 🧠 Concept

This tests custom iterators: the `Symbol.iterator` method makes the object iterable. The spread operator and `Array.from()` consume the iterator.

---

### 💡 Example

```js
const obj = {
  *[Symbol.iterator]() {
    yield 1;
    yield 2;
    yield 3;
  }
};

console.log([...obj]);
console.log(Array.from(obj));

for (const val of obj) {
  console.log(val);
}
```

---

### 🔍 Deep Insights

* **Rule:** The `Symbol.iterator` method makes the object iterable.
* **Use Case:** The spread operator and `Array.from()` consume the iterator.
* **Common Mistake:** `for...of` also iterates over the values.
* **Pro Tip:** Custom iterators enable objects to work with iteration protocols.

**Output:** `[1, 2, 3]`, `[1, 2, 3]`, `1`, `2`, `3`

---

### ⭐ Senior Takeaway

`Symbol.iterator` enables custom iteration behavior for any object.

---

## 🧩 Q170. What will be the output of the following code?

### 🧠 Concept

This tests async generators: the async generator yields values after delays. `for await...of` automatically awaits each yielded promise.

---

### 💡 Example

```js
async function* asyncGen() {
  for (let i = 0; i < 3; i++) {
    await new Promise(resolve => setTimeout(resolve, 100));
    yield i;
  }
}

(async () => {
  for await (const val of asyncGen()) {
    console.log(val);
  }
  console.log('Done');
})();
```

---

### 🔍 Deep Insights

* **Rule:** The async generator yields values after delays.
* **Use Case:** `for await...of` automatically awaits each yielded promise.
* **Common Mistake:** The sequence completes, then `'Done'` is logged.
* **Pro Tip:** Async generators enable streaming data from async sources.

**Output:** `0`, `1`, `2`, `Done`

---

### ⭐ Senior Takeaway

Async generators enable streaming async data with automatic promise unwrapping.

---

## 🧩 Q168. Write a function to chunk an array into smaller arrays of a specified size.

### 🧠 Concept

Array chunking splits an array into smaller sub-arrays of a specified size. Iterate through the array, collect elements into a temporary array, and push it to the result when it reaches the target size. Handle the remaining elements if the array length isn't divisible by the chunk size.

---

### 💡 Example

```js
function chunkArray(arr, n) {
  if (n <= 0) return [];
  const ans = [];
  let curr = [];
  for (let i = 0; i < arr.length; i++) {
    curr.push(arr[i]);
    if (curr.length === n) {
      ans.push(curr);
      curr = [];
    }
  }
  if (curr.length) ans.push(curr);
  return ans;
}

const result = chunkArray([1, 2, 3], 5);
console.log('result ->', result); // [[1, 2, 3]]
module.exports = chunkArray;
```

---

### 🔍 Deep Insights

* **Rule:** Return empty array for invalid chunk size, collect elements until chunk size reached, then push to result.
* **Use Case:** Useful for pagination, batch processing, and dividing data into manageable chunks.
* **Common Mistake:** Forgetting to push the last incomplete chunk when array length isn't divisible by chunk size.
* **Pro Tip:** Can be optimized using `slice()` method for cleaner implementation: `arr.slice(i, i + n)`.

---

### ⭐ Senior Takeaway

Array chunking enables efficient batch processing and pagination by dividing large datasets into manageable pieces.

---

## 🧩 Q169. Implement a WorkerPool class that manages concurrent task execution with a maximum worker limit.

### 🧠 Concept

A WorkerPool limits concurrent task execution to prevent resource exhaustion. It maintains a queue of pending tasks and executes them as workers become available, ensuring no more than the maximum number of workers run simultaneously.

---

### 💡 Example

```js
class WorkerPool {
  constructor(maxWorkers) {
    this.maxWorkers = maxWorkers;   // Max concurrent workers allowed
    this.activeWorkers = 0;         // Count of currently running tasks
    this.queue = [];                // FIFO queue for pending tasks
  }

  run(taskFunction) {
    return new Promise((resolve, reject) => {
      const executeTask = async () => {
        this.activeWorkers++;
        try {
          const result = await taskFunction();
          resolve(result);
        } catch (error) {
          reject(error);
        } finally {
          this.activeWorkers--;
          if (this.queue.length > 0) {
            const nextTask = this.queue.shift();
            nextTask();
          }
        }
      };

      if (this.activeWorkers < this.maxWorkers) {
        executeTask();
      } else {
        this.queue.push(executeTask);
      }
    });
  }
}

// Usage
const pool = new WorkerPool(3);
pool.run(() => fetch('/api/1'));
pool.run(() => fetch('/api/2'));
pool.run(() => fetch('/api/3'));
pool.run(() => fetch('/api/4')); // Queued until a worker is free
```

---

### 🔍 Deep Insights

* **Rule:** Track active workers and queue tasks when limit is reached, execute queued tasks when workers become available.
* **Use Case:** Prevents overwhelming APIs or resources with too many concurrent requests.
* **Common Mistake:** Not properly decrementing `activeWorkers` in the `finally` block can cause deadlocks.
* **Pro Tip:** Use FIFO queue to ensure fair task execution order.

---

### ⭐ Senior Takeaway

Worker pools balance performance with resource constraints, preventing system overload.

---

## 🧩 Q170. Write a function to flatten a nested object.

### 🧠 Concept

Flattening a nested object converts a hierarchical structure into a single-level object with dot-notation keys. Recursively traverse the object, building full keys by concatenating parent keys, and handle null values and arrays appropriately.

---

### 💡 Example

```js
function flattenObject(obj, parentKey, ans = {}) {
  for (let key in obj) {
    if (obj.hasOwnProperty(key)) {
      const value = obj[key];
      const fullKey = parentKey ? `${parentKey}.${key}` : `${key}`;
      
      if (typeof value === 'object' && value != null && !Array.isArray(value)) {
        flattenObject(value, fullKey, ans);
      } else {
        ans[fullKey] = value;
      }
    }
  }
  return ans;
}

// For the purpose of user debugging.
const res = flattenObject({ a: null, b: { c: undefined } });
console.log('res 1->', res); // { a: null, 'b.c': undefined }
module.exports = flattenObject;
```

---

### 🔍 Deep Insights

* **Rule:** Recursively traverse nested objects, build dot-notation keys by concatenating parent and current keys, handle null and arrays as leaf values.
* **Use Case:** Useful for converting nested configurations to flat structures, API response transformation, and data normalization.
* **Common Mistake:** Not checking for `null` (which is an object in JavaScript) or not handling arrays correctly can cause infinite recursion or incorrect flattening.
* **Pro Tip:** Use `hasOwnProperty` to avoid iterating over prototype properties, handle `null` explicitly since `typeof null === 'object'`.

---

### ⭐ Senior Takeaway

Flattening nested objects enables easier data manipulation and transformation by converting hierarchical structures into flat key-value pairs.

---

## 🧩 Q171. Implement a garbage collector function that marks and returns only reachable nodes from roots.

### 🧠 Concept

Garbage collection identifies and retains only nodes reachable from root nodes using depth-first search. Unreachable nodes are considered garbage and excluded from the result.

---

### 💡 Example

```js
function garbageCollector(graph, roots) {
    const visited = new Set();
    
    function dfs(node) {
        if (!graph[node] || visited.has(node)) return;
        visited.add(node);
        for (let dep of graph[node]) {
            dfs(dep);
        }
    }
    
    for (let r of roots) {
        dfs(r);
    }
    
    const reachable = {};
    for (let node of visited) {
        reachable[node] = graph[node];
    }
    
    return reachable;
}

// For the purpose of user debugging.
// pass your graph and root in function call
const graph = {
    A: ['B'],
    B: ['C'],
    C: [],
    D: []
};
const roots = ['A'];
const res = garbageCollector(graph, roots);
console.log('res-> ', res);
module.exports = garbageCollector;
```

---

### 🔍 Deep Insights

* **Rule:** Use DFS to mark all nodes reachable from roots, build result object with only visited nodes.
* **Use Case:** Memory management, dependency cleanup, and removing orphaned references in graph structures.
* **Common Mistake:** Not checking if node exists in graph before accessing dependencies can cause errors.
* **Pro Tip:** Use `Set` for O(1) visited checks, iterate over visited set to build result efficiently.

---

### ⭐ Senior Takeaway

Garbage collection ensures only reachable nodes are retained, preventing memory leaks and maintaining clean graph structures.

---

## 🧩 Q172. Implement an AutocompleteSystem class using a Trie data structure.

### 🧠 Concept

Autocomplete uses a Trie (prefix tree) to efficiently store and search words by prefix. Each node represents a character, and paths from root to leaf nodes form complete words.

---

### 💡 Example

```js
class AutocompleteSystem {
    constructor() {
        this.root = {}; // Root is a plain object
    }

    insert(word) {
        let node = this.root;
        for (let char of word) {
            if (!node[char]) node[char] = {};
            node = node[char];
        }
        node.isEnd = true;
        node.word = word;
    }

    search(prefix) {
        let node = this.root;
        for (let char of prefix) {
            if (!node[char]) return [];
            node = node[char];
        }
        const results = [];
        const dfs = (n) => {
            if (n.isEnd) results.push(n.word);
            for (let key in n) {
                if (key !== 'isEnd' && key !== 'word') dfs(n[key]);
            }
        };
        dfs(node);
        return results;
    }
}

module.exports = AutocompleteSystem;
```

---

### 🔍 Deep Insights

* **Rule:** Build trie by creating nodes for each character, mark word endings with `isEnd` flag, traverse to prefix then DFS to collect words.
* **Use Case:** Search engines, IDE autocomplete, contact search, and any prefix-based word lookup.
* **Common Mistake:** Not storing the complete word at end nodes makes it harder to retrieve results.
* **Pro Tip:** Use `isEnd` flag to mark word boundaries, store word at end node for easy retrieval during DFS.

---

### ⭐ Senior Takeaway

Trie-based autocomplete provides O(m) prefix search time where m is prefix length, making it efficient for real-time suggestions.

---

## 🧩 Q173. Implement a deepOmit function that recursively removes specified keys from objects and arrays.

### 🧠 Concept

Deep omit recursively removes specified keys from objects at all nested levels. It handles arrays by mapping over items and objects by filtering out omitted keys, preserving the structure while removing unwanted properties.

---

### 💡 Example

```js
function deepOmit(obj, keysToOmit) {
    if (!obj || typeof obj != 'object') return obj;
    
    if (Array.isArray(obj)) {
        return obj.map((item) => {
            return deepOmit(item, keysToOmit);
        });
    }
    
    const ans = {};
    for (let key in obj) {
        if (!keysToOmit.includes(key)) {
            ans[key] = deepOmit(obj[key], keysToOmit);
        }
    }
    return ans;
}

// For the purpose of user debugging.
// pass your object and keys in function call
const obj = [{ "a": 1 }, { "c": 4 }];
const result = deepOmit(obj, ['c']);
console.log('result ', result);
module.exports = deepOmit;
```

---

### 🔍 Deep Insights

* **Rule:** Return primitives as-is, map over arrays recursively, filter keys from objects and recurse on values.
* **Use Case:** Data sanitization, API response filtering, removing sensitive fields, and transforming nested structures.
* **Common Mistake:** Not handling arrays separately can cause issues, forgetting to recurse on object values.
* **Pro Tip:** Use `typeof obj != 'object'` to catch primitives and null, check `Array.isArray` before object handling.

---

### ⭐ Senior Takeaway

Deep omit enables clean data transformation by recursively removing unwanted keys while preserving nested structure.

---

## 🧩 Q174. Write a reverseWords function that reverses each word while keeping delimiters intact.

### 🧠 Concept

Reverse each alphanumeric word individually while preserving original spacing and punctuation by scanning the string, collecting characters, and reversing them when hitting a delimiter.

---

### 💡 Example

```js
function reverseWords(sentence) {
    const regex = /[a-zA-Z0-9]/;
    function reverse(str) {
        let res = '';
        for (let i = str.length - 1; i >= 0; i--) {
            res += str[i];
        }
        return res;
    }
    let result = '';
    let currentWord = '';
    for (let i = 0; i < sentence.length; i++) {
        const char = sentence[i];
        if (regex.test(char)) {
            currentWord += char;
        } else {
            result += reverse(currentWord) + char;
            currentWord = '';
        }
    }
    result += reverse(currentWord);
    return result;
}

console.log(reverseWords("Hello  World"));
console.log(reverseWords("Hello, World!"));
reverseWords("Hello  World");
module.exports = reverseWords;
```

---

### 🔍 Deep Insights

* **Rule:** Scan characters, accumulate alphanumerics, reverse on delimiter, append delimiter untouched.
* **Use Case:** Formatting text where punctuation must remain but words need reversing for ciphers or UX.
* **Common Mistake:** Failing to flush last word after loop causes missing output.
* **Pro Tip:** Regex guards against punctuation; customize pattern for locale-specific characters.

---

### ⭐ Senior Takeaway

Per-character scanning lets you reverse words while leaving whitespace and punctuation exactly as written.

---

## 🧩 Q175. Implement a customAssign function that mimics Object.assign behavior.

### 🧠 Concept

Custom assign copies enumerable own properties from source objects to a target object. It processes sources in order, overwriting target properties with later source values, and returns the modified target.

---

### 💡 Example

```js
function customAssign(target, ...sources) {
    if (target == null) {
        throw new TypeError('Cannot convert undefined or null to object');
    }
    
    const result = Object(target);
    
    for (const source of sources) {
        if (source == null) continue;
        
        for (const key in source) {
            if (Object.prototype.hasOwnProperty.call(source, key)) {
                result[key] = source[key];
            }
        }
    }
    
    return result;
}

// For the purpose of user debugging.
// pass appropriate input in below function call
customAssign({}, { a: 1 }, { b: 2 });
module.exports = customAssign;
```

---

### 🔍 Deep Insights

* **Rule:** Convert target to object, iterate sources in order, copy only own enumerable properties, later sources overwrite earlier values.
* **Use Case:** Merging configurations, creating object copies with overrides, and combining multiple data sources.
* **Common Mistake:** Not checking for null/undefined sources, copying inherited properties instead of own properties.
* **Pro Tip:** Use `Object.prototype.hasOwnProperty.call()` for safe property checking, handle null sources gracefully.

---

### ⭐ Senior Takeaway

Custom assign enables flexible object merging by copying properties in order, with later sources taking precedence over earlier ones.

---
