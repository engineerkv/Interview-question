# 🧰 8. Practical JavaScript Questions (Q82–110)

---

## 82) Write a debounce function.

Debouncing delays function execution until after a period of inactivity, preventing rapid repeated calls.

```js
const debounce = (fn, delay) => {
  let timeoutId;
  return (...args) => {
    clearTimeout(timeoutId);
    timeoutId = setTimeout(() => fn(...args), delay);
  };
};
```

- **Core Logic**: Clear previous timeout on each call, only execute after delay period of inactivity
- **Real-World Use**: Useful for search inputs and resize events
- **Common Mistake**: Not returning cleanup function for manual cancellation
- **Advanced Feature**: Consider immediate execution option for first call
- **Interview Tip**: Explain that debounce prevents rapid repeated function calls

---

## 83) Write a custom `bind()` polyfill.

`bind()` creates a new function with `this` bound and optional partial arguments.

```js
Function.prototype.bind = function(context, ...args) {
  const fn = this;
  return function(...moreArgs) {
    return fn.apply(context, [...args, ...moreArgs]);
  };
};
```

- **Core Logic**: Store original function and bound context, return new function that calls original with `apply`
- **Real-World Use**: Merge bound arguments with new arguments
- **Common Mistake**: Not preserving function properties or handling edge cases like `new` operator
- **Advanced Feature**: Handle edge cases like `new` operator
- **Interview Tip**: Explain that bind enables partial application and context binding

---

## 84) Implement your own `Promise.all()` polyfill.

`Promise.all()` resolves when all promises fulfill or rejects on first failure.

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

- **Core Logic**: Handle non-promise values with `Promise.resolve`, preserve order of results array
- **Real-World Use**: Reject immediately on first failure, count completions to know when done
- **Common Mistake**: Not handling empty input (return empty array)
- **Optimization**: Return empty array for empty input
- **Interview Tip**: Explain that Promise.all is fail-fast on first rejection

---

## 85) Write a throttle function.

Throttle limits function execution to once per specified time period.

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

- **Core Logic**: Track last execution time, execute immediately if enough time passed
- **Real-World Use**: Drop calls that come too soon, useful for scroll and mouse move events
- **Common Mistake**: Not considering leading/trailing edge options
- **Advanced Feature**: Consider leading/trailing edge options for different behaviors
- **Interview Tip**: Explain that throttle guarantees execution at most once per period

---

## 86) Flatten a deeply nested array.

Recursively flatten arrays to any depth, handling nested structures.

```js
const flatten = arr => arr.reduce((acc, val) => 
  Array.isArray(val) ? acc.concat(flatten(val)) : acc.concat(val), []);
flatten([1, [2, [3, 4]], 5]); // [1, 2, 3, 4, 5]
```

- **Core Logic**: Use recursion to handle arbitrary depth, check `Array.isArray` for nested arrays
- **Real-World Use**: Use `reduce` for functional approach
- **Common Mistake**: Not considering depth limit to prevent stack overflow
- **Optimization**: Handle edge cases like empty arrays
- **Interview Tip**: Explain that recursive approach handles any nesting depth

---

## 87) Memoize a given function to cache results.

Memoization caches function results based on arguments to avoid repeated computation.

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

- **Core Logic**: Use Map for O(1) cache lookups, serialize arguments for cache keys
- **Real-World Use**: Works best with pure functions
- **Common Mistake**: Not considering memory limits and cache eviction
- **Advanced Feature**: Handle edge cases like circular references
- **Interview Tip**: Explain that memoization improves performance for expensive computations

---

## 88) Implement a custom event emitter (pub/sub).

Event emitter allows objects to subscribe to and emit events with data.

```js
class EventEmitter {
  constructor() { this.events = {}; }
  on(event, fn) { (this.events[event] ||= []).push(fn); }
  emit(event, data) { (this.events[event] || []).forEach(fn => fn(data)); }
  off(event, fn) { this.events[event] = (this.events[event] || []).filter(f => f !== fn); }
}
```

- **Core Design**: Store event handlers in object/Map, support multiple listeners per event
- **Real-World Use**: Provide `on`, `emit`, and `off` methods
- **Common Mistake**: Not handling error cases and edge scenarios
- **Advanced Feature**: Consider `once` method for single-use listeners
- **Interview Tip**: Explain that event emitters enable decoupled communication

---

## 89) Implement a retry mechanism for a failed promise.

Retry failed operations with exponential backoff and maximum attempt limits.

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

- **Core Strategy**: Use exponential backoff to prevent thundering herd
- **Real-World Use**: Add jitter to distribute retry timing, consider circuit breakers for cascading failures
- **Common Mistake**: Not setting reasonable limits to avoid infinite loops
- **Advanced Feature**: Log retries for observability
- **Interview Tip**: Explain that retry improves reliability for transient failures

---

## 90) Write a function to compose multiple functions (`compose(f,g,h)` style).

Function composition applies functions from right to left, creating a pipeline.

```js
const compose = (...fns) => x => fns.reduceRight((acc, fn) => fn(acc), x);
const add1 = x => x + 1;
const double = x => x * 2;
compose(console.log, add1, double)(5); // 11
```

- **Core Logic**: Use `reduceRight` for right-to-left application, each function receives result of previous
- **Real-World Use**: Great for data transformation pipelines
- **Common Mistake**: Not considering `pipe` (left-to-right) alternative
- **Advanced Feature**: Works well with curried functions
- **Interview Tip**: Explain that composition enables functional programming patterns

---

## 91) Implement a custom `map()` method for arrays.

`map()` creates new array by applying function to each element.

```js
Array.prototype.map = function(fn, thisArg) {
  const result = [];
  for (let i = 0; i < this.length; i++) {
    result[i] = fn.call(thisArg, this[i], i, this);
  }
  return result;
};
```

- **Core Logic**: Create new array, don't modify original, pass element, index, and array to callback
- **Real-World Use**: Handle sparse arrays correctly, support `thisArg` for context binding
- **Common Mistake**: Not considering edge cases like undefined elements
- **Optimization**: Consider edge cases like undefined elements
- **Interview Tip**: Explain that map creates new array without mutating original

---

## 92) Implement a `once()` function that executes only once.

`once()` ensures a function can only be called once, returning the same result on subsequent calls.

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

- **Core Logic**: Track if function has been called, cache result for subsequent calls
- **Real-World Use**: Useful for initialization and setup
- **Common Mistake**: Not considering error handling for failed calls
- **Advanced Feature**: Works with both sync and async functions
- **Interview Tip**: Explain that once prevents duplicate initialization or setup

---

## 93) Convert callback-based code to a promise-based version.

Wrap callback-based functions in promises using the Promise constructor.

```js
const readFile = path => new Promise((resolve, reject) => {
  fs.readFile(path, (err, data) => {
    if (err) reject(err);
    else resolve(data);
  });
});
```

- **Core Strategy**: Use Promise constructor for one-time operations, handle both success and error cases
- **Real-World Use**: Consider promisify utilities for Node.js
- **Common Mistake**: Not maintaining same error handling patterns
- **Advanced Feature**: Test thoroughly with edge cases
- **Interview Tip**: Explain that promises improve async code readability

---

## 94) Write a function to limit the number of concurrent promises.

Control concurrency by limiting how many promises can run simultaneously.

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

- **Core Strategy**: Track running and completed tasks, queue tasks when limit reached
- **Real-World Use**: Preserve result order in output array, useful for API rate limiting
- **Common Mistake**: Not handling errors appropriately
- **Optimization**: Handle errors appropriately
- **Interview Tip**: Explain that concurrency limiting prevents resource exhaustion

---

## 95) Write a function that returns a promise resolved after a delay.

Create a promise that resolves after a specified time delay.

```js
const delay = ms => new Promise(resolve => setTimeout(resolve, ms));
delay(1000).then(() => console.log('1 second later'));
```

- **Core Logic**: Use `setTimeout` with Promise constructor, return promise for chaining
- **Real-World Use**: Useful for testing and rate limiting
- **Common Mistake**: Not considering cancellation with AbortController
- **Advanced Feature**: Can be used with async/await
- **Interview Tip**: Explain that delay is useful for testing and timing control

---

## 96) Implement a chainable calculator API (`calc.add(5).multiply(2).value()`).

Create a fluent interface where methods return the object for chaining.

```js
const calc = {
  value: 0,
  add(n) { this.value += n; return this; },
  multiply(n) { this.value *= n; return this; },
  getValue() { return this.value; }
};
calc.add(5).multiply(2).getValue(); // 10
```

- **Core Pattern**: Return `this` from methods for chaining, store state in the object
- **Real-World Use**: Use getter for final value access, great for builder patterns
- **Common Mistake**: Not considering immutable alternatives
- **Advanced Feature**: Consider immutable alternatives
- **Interview Tip**: Explain that method chaining enables fluent APIs

---

## 97) Implement a simple version of `setInterval` using `setTimeout`.

Use recursive `setTimeout` calls to create interval-like behavior.

```js
const setInterval = (fn, delay) => {
  const run = () => {
    fn();
    setTimeout(run, delay);
  };
  setTimeout(run, delay);
};
```

- **Core Logic**: Recursive calls create repeating behavior, return cleanup function for cancellation
- **Real-World Use**: More flexible than native `setInterval`
- **Common Mistake**: Not considering drift correction for precise timing
- **Advanced Feature**: Handle errors to prevent stopping
- **Interview Tip**: Explain that recursive setTimeout is more flexible than setInterval

---

## 98) Write a function to shuffle an array randomly.

Randomly reorder array elements using Fisher-Yates shuffle algorithm.

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

- **Core Algorithm**: Use Fisher-Yates for uniform distribution, work backwards through array
- **Real-World Use**: Swap elements randomly, create copy to avoid mutating original
- **Common Mistake**: Not creating copy, mutating original array
- **Advanced Feature**: Consider seeded random for testing
- **Interview Tip**: Explain that Fisher-Yates ensures uniform random distribution

---

## 99) Implement your own version of `debounce + immediate` combined logic.

Combine debounce with immediate execution option for first call.

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

- **Core Logic**: Execute immediately on first call if enabled, clear timeout on subsequent calls
- **Real-World Use**: Reset timeout flag after execution, useful for search with immediate feedback
- **Common Mistake**: Not considering both leading and trailing options
- **Advanced Feature**: Consider both leading and trailing options
- **Interview Tip**: Explain that immediate option provides instant feedback

---

## 100) How do you implement useMemo from scratch?

`useMemo` caches the result of a computation and only recalculates when dependencies change.

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

- **Core Logic**: Store previous dependencies for comparison, only recalculate when dependencies change
- **Real-World Use**: Use shallow comparison for dependency checking, return cached value when dependencies unchanged
- **Common Mistake**: Not considering cleanup for expensive computations
- **Advanced Feature**: Consider cleanup for expensive computations
- **Interview Tip**: Explain that useMemo prevents unnecessary recalculations

---

## 101) How do you implement useCallback from scratch?

`useCallback` returns a memoized version of a function that only changes when dependencies change.

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

- **Core Logic**: Memoize function reference, not execution, prevent unnecessary re-renders in child components
- **Real-World Use**: Use shallow comparison for dependency arrays, return same function reference when deps unchanged
- **Common Mistake**: Essential for performance optimization in React
- **Advanced Feature**: Essential for performance optimization in React
- **Interview Tip**: Explain that useCallback prevents function recreation on every render

---

## 102) What is Compact Number (Intl.NumberFormat)?

Compact Number formatting displays large numbers in a shortened, human-readable format using locale-specific abbreviations.

```js
const formatter = new Intl.NumberFormat('en-US', { notation: 'compact' });
console.log(formatter.format(1000)); // "1K"
console.log(formatter.format(1000000)); // "1M"
```

- **Core Purpose**: Uses `Intl.NumberFormat` with `notation: 'compact'` option
- **Real-World Use**: Supports different locales for localized formatting, handles various compact notation styles (K, M, B, T)
- **Common Mistake**: Useful for displaying large numbers in UI components
- **Advanced Feature**: Can be customized with additional formatting options
- **Interview Tip**: Explain that compact notation improves readability for large numbers

---

## 103) What are JavaScript object property flags and descriptors?

Property descriptors define the characteristics of object properties, including configurability, enumerability, writability, and value.

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

- **Core Properties**: `writable` (can property value be changed), `enumerable` (shows up in `for...in` loops), `configurable` (can descriptor be modified or property deleted), `value` (the property's value)
- **Real-World Use**: Use `Object.defineProperty` to set custom descriptors
- **Common Mistake**: Not understanding how property flags affect object behavior
- **Advanced Feature**: Property descriptors enable fine-grained control over object properties
- **Interview Tip**: Explain that descriptors control property behavior and access

---

## 104) What are server-sent events?

Server-Sent Events (SSE) enable servers to push data to web pages in real-time using a unidirectional connection.

```js
const eventSource = new EventSource('/events');
eventSource.onmessage = event => console.log('Received:', event.data);
```

- **Core Concept**: Unidirectional: Server to client only, built on HTTP, simpler than WebSockets
- **Real-World Use**: Automatic reconnection on connection loss, use `text/event-stream` MIME type
- **Common Mistake**: Good for live updates, notifications, real-time data
- **Advanced Feature**: Simpler than WebSockets for one-way communication
- **Interview Tip**: Explain that SSE is ideal for server-to-client streaming

---

## 105) What are proxies in JavaScript used for?

Proxies allow you to intercept and customize operations performed on objects, enabling meta-programming capabilities.

```js
const handler = { get: (t, p) => (console.log(`Accessing: ${p}`), t[p]), set: (t, p, v) => (t[p] = v, true) };
const proxy = new Proxy({}, handler);
proxy.name = 'John'; console.log(proxy.name); // Logs then "John"
```

- **Core Purpose**: Intercept fundamental operations (get, set, has, delete)
- **Real-World Use**: Enable validation, logging, and virtual properties, used in frameworks for reactivity
- **Common Mistake**: Can create virtual objects that don't exist
- **Advanced Feature**: Powerful tool for creating advanced abstractions
- **Interview Tip**: Explain that proxies enable meta-programming and object interception

---

## 106) What are some techniques for reducing reflows and repaints?

Reflows and repaints are expensive browser operations. Minimize them by batching changes and using efficient DOM manipulation.

```js
element.style.cssText = 'width: 100px; height: 100px; margin: 10px;';
element.className = 'new-style';
const fragment = document.createDocumentFragment();
fragment.appendChild(newElement); container.appendChild(fragment);
```

- **Core Strategies**: Batch DOM changes to minimize reflows, use `DocumentFragment` for multiple insertions
- **Real-World Use**: Change classes instead of individual styles, use `transform` and `opacity` for animations
- **Common Mistake**: Measure elements before making changes
- **Optimization**: Use `transform` and `opacity` for animations (GPU-accelerated)
- **Interview Tip**: Explain that reducing reflows improves rendering performance

---

## 107) What are some tools that can be used to measure and analyze JavaScript performance?

Various tools help measure and analyze JavaScript performance, from browser dev tools to specialized profiling tools.

```js
const start = performance.now(); /* ... operation ... */ const end = performance.now();
console.log(`Operation took ${end - start}ms`);
console.log(performance.memory);
```

- **Core Tools**: Chrome DevTools (Performance tab, Memory tab, Lighthouse), Performance API (`performance.now()`, `performance.memory`)
- **Real-World Use**: Web Vitals (LCP, FID, CLS measurements), Profiling (CPU profiling, memory profiling)
- **Common Mistake**: Third-party: New Relic, DataDog, Sentry for production monitoring
- **Advanced Feature**: Use multiple tools for comprehensive performance analysis
- **Interview Tip**: Explain that performance monitoring is essential for optimization

---

## 108) Explain the concept of a microtask queue?

The microtask queue processes high-priority tasks that should execute before the next task in the main queue, including Promise callbacks and queueMicrotask.

```js
console.log('1');
setTimeout(() => console.log('2'), 0);
Promise.resolve().then(() => console.log('3'));
queueMicrotask(() => console.log('4'));
console.log('5');
// Output: 1, 5, 3, 4, 2
```

- **Core Concept**: Microtasks have higher priority than macrotasks, processed after current execution stack is empty
- **Real-World Impact**: Includes Promise callbacks and `queueMicrotask`
- **Common Mistake**: Can starve the main queue if not managed properly
- **Advanced Feature**: Essential for understanding async JavaScript execution order
- **Interview Tip**: Explain that microtasks run before macrotasks in the event loop

---

## 109) How do you check HTTP status codes in axios and fetch API?

Fetch requires manual status checking with `response.ok`, while axios automatically rejects on 4xx/5xx status codes.

```js
fetch('/api/data').then(response => {
  if (!response.ok) throw new Error(`Status: ${response.status}`);
  return response.json();
});

axios.get('/api/data').then(res => res.data)
  .catch(err => console.error('Status:', err.response?.status));
```

- **Core Difference**: Fetch only rejects on network errors, not HTTP errors—must check `response.ok` or `response.status` manually
- **Real-World Use**: Axios automatically rejects promises for status codes >= 400, throwing errors you can catch
- **Common Mistake**: Remember that `fetch` doesn't throw on 4xx/5xx—this is a common mistake
- **Advanced Feature**: Consider response interceptors in axios for global status code handling
- **Interview Tip**: Explain that always handle both network errors and HTTP status errors

---

## 110) How can you optimize DOM manipulation for better performance?

Optimize DOM manipulation by minimizing reflows, using efficient selectors, and leveraging modern APIs for better performance.

```js
const elements = document.querySelectorAll('.item');
const fragment = document.createDocumentFragment();
items.forEach(item => { const li = document.createElement('li'); li.textContent = item.name; fragment.appendChild(li); });
list.appendChild(fragment);
```

- **Core Strategies**: Minimize reflows and repaints, use `DocumentFragment` for multiple insertions
- **Real-World Use**: Cache DOM queries and reuse elements, use `requestAnimationFrame` for smooth animations
- **Common Mistake**: Not batching DOM changes, causing multiple reflows
- **Advanced Feature**: Consider virtual DOM libraries for complex UIs
- **Interview Tip**: Explain that DOM optimization significantly improves rendering performance

---
