<div align="center">

**[← Previous: Web Workers, Service Workers & Real-World Topics](6%29%20Web%20Workers%2C%20Service%20Workers%20%26%20Real-World%20Topics.md)** | **[Next: JavaScript Output Questions →](8%29%20JavaScript%20Output%20Questions.md)**

</div>

# 💼 7. Practical JavaScript Questions (Q81–127)

---

## Q81. 🔧 Write a debounce function.

Debouncing delays function execution until after a period of inactivity, preventing rapid repeated calls. It clears the previous timeout on each call and only executes after the delay period.

- **Trade-offs**: The catch is not returning cleanup function for manual cancellation. - Consider immediate execution option for first call.

Example:

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

## Q82. 💡 Write a custom `bind()` polyfill.

`bind()` creates a new function with `this` bound and optional partial arguments. Store the original function and bound context, return a new function that calls the original with `apply`.

- **Trade-offs**: The catch is not preserving function properties or handling edge cases like `new` operator. - Handle edge cases like `new` operator for complete implementation.

Example:

```js
Function.prototype.bind = function(context, ...args) {
  const fn = this;
  return function(...moreArgs) {
    return fn.apply(context, [...args, ...moreArgs]);
  };
};

```

---

## Q83. 🔧 Implement your own `call()` polyfill

`call()` invokes a function with a specific `this` context and arguments passed individually. It allows you to borrow methods from other objects and explicitly set the `this` binding.

- **Trade-offs**: The catch is `call()` takes arguments individually (fn.call(obj, arg1, arg2)), making it more readable for fixed arguments. `call()` enables method borrowing and explicit `this` binding, but watch out - use `Symbol` to avoid property name conflicts when attaching function to context object.

Example:

```js
// Custom call() polyfill
Function.prototype.call = function(context, ...args) {
  context = context || globalThis; // Use globalThis as fallback
  const uniqueKey = Symbol('fn'); // Create unique key to avoid conflicts
  context[uniqueKey] = this; // Attach function to context
  const result = context[uniqueKey](...args); // Call function with context
  delete context[uniqueKey]; // Clean up
  return result;
};

// Usage examples
const person1 = { name: 'John', age: 30 };
const person2 = { name: 'Jane', age: 25 };

function greet(greeting, punctuation) {
  return `${greeting}, I'm ${this.name}${punctuation}`;
}

// Using call() - arguments passed individually
console.log(greet.call(person1, 'Hello', '!')); 
// "Hello, I'm John!"

// Method borrowing example
const numbers = [5, 6, 2, 3, 7];
const max = Math.max.call(null, ...numbers);
console.log(max); // 7

```

---

## Q84. 🔧 Implement your own `apply()` polyfill

`apply()` invokes a function with a specific `this` context and arguments passed as an array. It's essential when you have a dynamic number of arguments or an array to pass, enabling method borrowing and explicit `this` binding.

- **Trade-offs**: The catch is `apply()` takes arguments as an array (fn.apply(obj, [arg1, arg2])), making it essential for dynamic arguments. `apply()` enables method borrowing and explicit `this` binding, but watch out - `apply()` is deprecated in favor of spread operator with `call()` in modern JavaScript (fn.call(obj, ...args)). Use `Symbol` to avoid property name conflicts when attaching function to context object.

Example:

```js
// Custom apply() polyfill
Function.prototype.apply = function(context, argsArray) {
  context = context || globalThis; // Use globalThis as fallback
  const uniqueKey = Symbol('fn'); // Create unique key to avoid conflicts
  context[uniqueKey] = this; // Attach function to context
  const result = context[uniqueKey](...(argsArray || [])); // Call with spread array
  delete context[uniqueKey]; // Clean up
  return result;
};

// Usage examples
const person1 = { name: 'John', age: 30 };
const person2 = { name: 'Jane', age: 25 };

function greet(greeting, punctuation) {
  return `${greeting}, I'm ${this.name}${punctuation}`;
}

// Using apply() - arguments passed as array
console.log(greet.apply(person2, ['Hi', '.'])); 
// "Hi, I'm Jane."

// Method borrowing example
const numbers = [5, 6, 2, 3, 7];
const max = Math.max.apply(null, numbers);
console.log(max); // 7

```

---

## Q85. ⚡ Implement your own `Promise.all()` polyfill.

`Promise.all()` resolves when all promises fulfill or rejects on first failure. Handle non-promise values with `Promise.resolve`, preserve order of results array, and count completions to know when done.

- **Trade-offs**: The catch is not handling empty input (return empty array). - Return empty array for empty input to match native behavior.

Example:

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

## Q86. ⚡ Implement your own `Promise.race()` polyfill.

`Promise.race()` resolves or rejects as soon as the first promise settles. Return the first settled promise's result, whether it fulfills or rejects. Handle non-promise values with `Promise.resolve`.

- **Trade-offs**: The catch is not handling empty input array (should remain pending). - Handle non-promise values with `Promise.resolve` to normalize input.

Example:

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

## Q87. ⚡ Implement your own `Promise.any()` polyfill.

`Promise.any()` resolves with the first fulfilled promise, or rejects with an AggregateError if all promises reject. Track rejections and only reject when all promises have rejected.

- **Trade-offs**: The catch is not handling empty input (should reject with aggregateerror). - AggregateError contains all rejection reasons for debugging.

Example:

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

## Q88. ⚡ Implement your own `Promise.allSettled()` polyfill.

`Promise.allSettled()` waits for all promises to settle (fulfill or reject) and returns an array of results with status and value/reason. Never rejects, always resolves with all outcomes.

- **Trade-offs**: The catch is not preserving order of results array. - Each result has `status: 'fulfilled'` or `'rejected'` with corresponding `value` or `reason`.

Example:

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

## Q89. 🔧 Write a throttle function.

Throttle limits function execution to once per specified time period. Track last execution time and execute immediately if enough time has passed.

- **Trade-offs**: The catch is not considering leading/trailing edge options. - Consider leading/trailing edge options for different behaviors.

Example:

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

## Q90. 💡 Flatten a deeply nested array.

Recursively flatten arrays to any depth, handling nested structures. Use recursion to handle arbitrary depth and check `Array.isArray` for nested arrays.

- **Trade-offs**: The catch is not considering depth limit to prevent stack overflow. - Handle edge cases like empty arrays.

Example:

```js
const flatten = arr => arr.reduce((acc, val) => 
  Array.isArray(val) ? acc.concat(flatten(val)) : acc.concat(val), []);
flatten([1, [2, [3, 4]], 5]); // [1, 2, 3, 4, 5]

```

---

## Q91. 🔧 Memoize a given function to cache results.

Memoization caches function results based on arguments to avoid repeated computation. Use Map for O(1) cache lookups and serialize arguments for cache keys.

- **Trade-offs**: The catch is not considering memory limits and cache eviction. - Handle edge cases like circular references.

Example:

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

## Q92. 🔄 Implement a custom event emitter (pub/sub).

Event emitter allows objects to subscribe to and emit events with data. Store event handlers in object/Map and support multiple listeners per event.

- **Trade-offs**: The catch is not handling error cases and edge scenarios. - Consider `once` method for single-use listeners.

Example:

```js
class EventEmitter {
  constructor() { this.events = {}; }
  on(event, fn) { (this.events[event] ||= []).push(fn); }
  emit(event, data) { (this.events[event] || []).forEach(fn => fn(data)); }
  off(event, fn) { this.events[event] = (this.events[event] || []).filter(f => f !== fn); }
}

```

---

## Q93. ⚡ Implement a retry mechanism for a failed promise.

Retry failed operations with exponential backoff and maximum attempt limits. Use exponential backoff to prevent thundering herd and add jitter to distribute retry timing.

- **Trade-offs**: The catch is not setting reasonable limits to avoid infinite loops. - Log retries for observability.

Example:

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

## Q94. 🔧 Write a function to compose multiple functions (`compose(f,g,h)` style).

Function composition applies functions from right to left, creating a pipeline. Use `reduceRight` for right-to-left application, each function receives result of previous.

- **Trade-offs**: The catch is not considering `pipe` (left-to-right) alternative. - Works well with curried functions.

Example:

```js
const compose = (...fns) => x => fns.reduceRight((acc, fn) => fn(acc), x);
const add1 = x => x + 1;
const double = x => x * 2;
compose(console.log, add1, double)(5); // 11

```

---

## Q95. 🔧 Implement a custom `map()` method for arrays.

`map()` creates new array by applying function to each element. Create new array, don't modify original, and pass element, index, and array to callback.

- **Trade-offs**: The catch is not considering edge cases like undefined elements. - Consider edge cases like undefined elements for complete implementation.

Example:

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

## Q96. 🔧 Implement a `once()` function that executes only once.

`once()` ensures a function can only be called once, returning the same result on subsequent calls. Track if function has been called and cache result for subsequent calls.

- **Trade-offs**: The catch is not considering error handling for failed calls. - Works with both sync and async functions.

Example:

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

## Q97. ⚡ Convert callback-based code to a promise-based version.

Wrap callback-based functions in promises using the Promise constructor. Use Promise constructor for one-time operations and handle both success and error cases.

- **Trade-offs**: The catch is not maintaining same error handling patterns. - Test thoroughly with edge cases.

Example:

```js
const readFile = path => new Promise((resolve, reject) => {
  fs.readFile(path, (err, data) => {
    if (err) reject(err);
    else resolve(data);
  });
});

```

---

## Q98. ⚡ Write a function to limit the number of concurrent promises.

Control concurrency by limiting how many promises can run simultaneously. Track running and completed tasks, queue tasks when limit reached.

- **Trade-offs**: The catch is not handling errors appropriately. - Handle errors appropriately for robust implementation.

Example:

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

## Q99. ⚡ Write a function that returns a promise resolved after a delay.

Create a promise that resolves after a specified time delay. Use `setTimeout` with Promise constructor and return promise for chaining.

- **Trade-offs**: The catch is not considering cancellation with abortcontroller. - Can be used with async/await.

Example:

```js
const delay = ms => new Promise(resolve => setTimeout(resolve, ms));
delay(1000).then(() => console.log('1 second later'));

```

---

## Q100. 🔌 Implement a chainable calculator API (`calc.add(5).multiply(2).value()`).

Create a fluent interface where methods return the object for chaining. Return `this` from methods for chaining and store state in the object.

- **Trade-offs**: The catch is not considering immutable alternatives. - Consider immutable alternatives for functional style.

Example:

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

## Q101. 🔧 Implement a simple version of `setInterval` using `setTimeout`.

Use recursive `setTimeout` calls to create interval-like behavior. Recursive calls create repeating behavior, return cleanup function for cancellation.

- **Trade-offs**: The catch is not considering drift correction for precise timing. - Handle errors to prevent stopping.

Example:

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

## Q102. 🔧 Write a function to shuffle an array randomly.

Randomly reorder array elements using Fisher-Yates shuffle algorithm. Use Fisher-Yates for uniform distribution and work backwards through array.

- **Trade-offs**: The catch is not creating copy, mutating original array. - Consider seeded random for testing.

Example:

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

## Q103. 🎬 Implement your own version of `debounce + immediate` combined logic.

Combine debounce with immediate execution option for first call. Execute immediately on first call if enabled, clear timeout on subsequent calls.

- **Trade-offs**: The catch is not considering both leading and trailing options. - Consider both leading and trailing options for different behaviors.

Example:

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

## Q104. 🔧 Implementing `useMemo` in vanilla JavaScript

`useMemo`-style helpers cache the result of a computation and only recompute when the dependency list changes. Track the last dependencies and value in a closure so future calls can reuse the cached result if every dependency matches.

- **Trade-offs**: Relies on shallow comparison of dependencies – nested objects still change by reference. - Cache grows with every instance, so release it when no longer needed. - Works best for deterministic, pure compute functions. - Always recompute immediately when any dependency reference changes. - Requires callers to manage the cache object that persists between invocations.

Example:

```js
const createUseMemo = () => {
  let deps = null, value;
  return (compute, nextDeps = []) => {
    const unchanged = deps && nextDeps.every((dep, i) => dep === deps[i]);
    if (!unchanged) {
      value = compute();
      deps = nextDeps;
    }
    return value;
  };
};

const useMemo = createUseMemo();
const heavyValue = useMemo(() => expensiveFn(data), [data.id, data.count]);

```

---

## Q105. 🔧 Implementing `useCallback` in vanilla JavaScript

`useCallback` memoizes a function reference so the same function instance is returned until dependencies change. Reuse the `useMemo` helper to store the callback itself instead of a computed value.

- **Trade-offs**: Still needs dependency tracking discipline; pass stable references to avoid unnecessary regenerations. - The memoized function closes over the environment when first created, so stale closures can appear if dependencies are wrong. - Returns the exact same function reference between unchanged calls. - Works for non-React code like custom event systems or templating engines. - Requires manual cleanup if you store many different callbacks.

Example:

```js
const createUseMemo = () => {
  let deps = null, value;
  return (compute, nextDeps = []) => {
    const unchanged = deps && nextDeps.every((dep, i) => dep === deps[i]);
    if (!unchanged) {
      value = compute();
      deps = nextDeps;
    }
    return value;
  };
};

// Implementation using useMemo
const createUseCallback = () => {
  const memo = createUseMemo();
  return (fn, deps = []) => {
    return memo(() => fn, deps);
  };
};

// Alternative direct implementation
const createUseCallbackDirect = () => {
  let cachedFn = null;
  let cachedDeps = null;
  return (fn, deps = []) => {
    const unchanged = cachedDeps && deps.length === cachedDeps.length && 
                      deps.every((dep, i) => dep === cachedDeps[i]);
    if (!unchanged) {
      cachedFn = fn;
      cachedDeps = deps;
    }
    return cachedFn;
  };
};

const useCallback = createUseCallback();
const stableHandler = useCallback(() => api.save(formData), [formData.id]);
button.addEventListener('click', stableHandler);
// later: button.removeEventListener('click', stableHandler);

```

---

## Q106. 📝 Compact Number (Intl.NumberFormat)

Compact Number formatting displays large numbers in a shortened, human-readable format using locale-specific abbreviations. Uses `Intl.NumberFormat` with `notation: 'compact'` option.

- **Trade-offs**: The catch is useful for displaying large numbers in ui components. - Can be customized with additional formatting options.

Example:

```js
const formatter = new Intl.NumberFormat('en-US', { notation: 'compact' });
console.log(formatter.format(1000)); // "1K"
console.log(formatter.format(1000000)); // "1M"

```

---

## Q107. 📦 JavaScript object property flags and descriptors

Property descriptors define the characteristics of object properties, including configurability, enumerability, writability, and value. Use `Object.defineProperty` to set custom descriptors.

- **Trade-offs**: The catch is not understanding how property flags affect object behavior. - Property descriptors enable fine-grained control over object properties.

Example:

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

## Q108. 🔄 Server-sent events

Server-Sent Events (SSE) enable servers to push data to web pages in real-time using a unidirectional connection. Unidirectional: Server to client only, built on HTTP, simpler than WebSockets.

- **Trade-offs**: The catch is good for live updates, notifications, real-time data. - Simpler than WebSockets for one-way communication.

Example:

```js
const eventSource = new EventSource('/events');
eventSource.onmessage = event => console.log('Received:', event.data);

```

---

## Q109. ⏰ Proxies in JavaScript and their use cases

Proxies allow you to intercept and customize operations performed on objects, enabling meta-programming capabilities. Intercept fundamental operations (get, set, has, delete).

- **Trade-offs**: The catch is can create virtual objects that don't exist. - Powerful tool for creating advanced abstractions.

Example:

```js
const handler = { 
  get: (t, p) => (console.log(`Accessing: ${p}`), t[p]), 
  set: (t, p, v) => (t[p] = v, true) 
};
const proxy = new Proxy({}, handler);
proxy.name = 'John'; console.log(proxy.name); // Logs then "John"

```

---

## Q110. ⚡ Tools for measuring and analyzing JavaScript performance

Various tools help measure and analyze JavaScript performance, from browser dev tools to specialized profiling tools. Chrome DevTools, Performance API, and third-party tools provide comprehensive analysis.

- **Trade-offs**: The catch is third-party: new relic, datadog, sentry for production monitoring. - Use multiple tools for comprehensive performance analysis.

Example:

```js
const start = performance.now(); 
/* ... operation ... */ 
const end = performance.now();
console.log(`Operation took ${end - start}ms`);
console.log(performance.memory);

```

---

## Q111. ❓ Explain the concept of a microtask queue?

The microtask queue processes high-priority tasks that should execute before the next task in the main queue, including Promise callbacks and queueMicrotask. Microtasks have higher priority than macrotasks.

- **Trade-offs**: The catch is can starve the main queue if not managed properly. - Essential for understanding async JavaScript execution order.

Example:

```js
console.log('1');
setTimeout(() => console.log('2'), 0);
Promise.resolve().then(() => console.log('3'));
queueMicrotask(() => console.log('4'));
console.log('5');
// Output: 1, 5, 3, 4, 2

```

---

## Q112. 🔌 Checking HTTP status codes in axios and fetch API

Fetch requires manual status checking with `response.ok`, while axios automatically rejects on 4xx/5xx status codes. Fetch only rejects on network errors, not HTTP errors.

- **Trade-offs**: The catch is remember that `fetch` doesn't throw on 4xx/5xx—this is a common mistake. - Consider response interceptors in axios for global status code handling.

Example:

```js
fetch('/api/data').then(response => {
  if (!response.ok) throw new Error(`Status: ${response.status}`);
  return response.json();
});

axios.get('/api/data').then(res => res.data)
  .catch(err => console.error('Status:', err.response?.status));

```

---

## Q113. ⚡ Optimizing DOM manipulation for better performance

Optimize DOM manipulation by minimizing reflows, using efficient selectors, and leveraging modern APIs for better performance. Minimize reflows and repaints, use `DocumentFragment` for multiple insertions.

- **Trade-offs**: The catch is not batching dom changes, causing multiple reflows. - Consider virtual DOM libraries for complex UIs.

Example:

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

## Q114. ⚡ Implement `Promise.all()` with a concurrency limit.

Concurrency limit controls how many promises execute simultaneously, preventing resource exhaustion. Use a pool of active promises and queue remaining ones, starting new promises as others complete.

- **Trade-offs**: The catch is not properly tracking executing promises can cause limit violations. - Use `Promise.race()` to wait for any promise to complete before starting next.

Example:

```js
const promiseAllWithLimit = (taskFns, limit) => new Promise((resolve, reject) => {
  const results = Array(taskFns.length);
  let nextIndex = 0;
  let active = 0;
  
  const launchNext = () => {
    if (nextIndex === taskFns.length && active === 0) {
      resolve(results);
      return;
    }
    while (active < limit && nextIndex < taskFns.length) {
      const current = nextIndex++;
      active++;
      Promise.resolve()
        .then(() => taskFns[current]())
        .then(value => {
          results[current] = value;
          active--;
          launchNext();
        })
        .catch(err => reject(err));
    }
  };
  
  if (taskFns.length === 0) resolve([]);
  else launchNext();
});

// Usage
const tasks = [1, 2, 3, 4, 5].map(n => () => fetch(`/api/data/${n}`));
const results = await promiseAllWithLimit(tasks, 2);

```

---

## Q115. 🔧 Implement a deep clone function for objects.

Deep cloning creates a completely independent copy of an object, including nested objects and arrays. Handle primitives, objects, arrays, dates, and circular references for a complete solution.

- **Trade-offs**: The catch is not handling circular references causes stack overflow. - `structuredClone()` is native but doesn't support functions or symbols.

Example:

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

## Q116. 🔧 Implement a `groupBy` function that groups array items by a key.

Grouping organizes array items into objects keyed by a property or computed value. Use `reduce()` to build the grouped object, handling both string keys and computed keys from functions.

- **Trade-offs**: The catch is not initializing arrays for new keys causes undefined errors. - Use `Map` for better performance with non-string keys.

Example:

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

## Q117. 💾 Implement an LRU (Least Recently Used) cache.

LRU cache evicts least recently used items when capacity is reached. Use a combination of `Map` (for O(1) access) and doubly-linked list (for O(1) insertion/deletion) or leverage `Map`'s insertion order.

- **Trade-offs**: The catch is not updating access order on `get()` operations. - `Map` maintains insertion order, making it perfect for LRU implementation.

Example:

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

## Q118. 💡 Create a task scheduler that handles dependencies between tasks.

Task scheduling with dependencies requires topological sorting to determine execution order. Use graph algorithms to detect cycles and order tasks so dependencies execute before dependents.

- **Trade-offs**: The catch is not detecting circular dependencies causes infinite loops or stack overflow. - DFS provides clear cycle detection; Kahn's algorithm is more efficient for large graphs.

Example:

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

## Q119. 🔧 Write a function to chunk an array into smaller arrays of a specified size.

Array chunking splits an array into smaller sub-arrays of a specified size. Iterate through the array, collect elements into a temporary array, and push it to the result when it reaches the target size. Handle the remaining elements if the array length isn't divisible by the chunk size.

- **Trade-offs**: The catch is forgetting to push the last incomplete chunk when array length isn't divisible by chunk size. - Can be optimized using `slice()` method for cleaner implementation: `arr.slice(i, i + n)`.

Example:

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

## Q120. 👷 Implement a WorkerPool class that manages concurrent task execution with a maximum worker limit.

A WorkerPool limits concurrent task execution to prevent resource exhaustion. It maintains a queue of pending tasks and executes them as workers become available, ensuring no more than the maximum number of workers run simultaneously.

- **Trade-offs**: The catch is not properly decrementing `activeworkers` in the `finally` block can cause deadlocks. - Use FIFO queue to ensure fair task execution order.

Example:

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

## Q121. 🔧 Write a function to flatten a nested object.

Flattening a nested object converts a hierarchical structure into a single-level object with dot-notation keys. Recursively traverse the object, building full keys by concatenating parent keys, and handle null values and arrays appropriately.

- **Trade-offs**: The catch is not checking for `null` (which is an object in javascript) or not handling arrays correctly can cause infinite recursion or incorrect flattening. - Use `hasOwnProperty` to avoid iterating over prototype properties, handle `null` explicitly since `typeof null === 'object'`.

Example:

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

## Q122. 🔧 Implement a garbage collector function that marks and returns only reachable nodes from roots.

Garbage collection identifies and retains only nodes reachable from root nodes using depth-first search. Unreachable nodes are considered garbage and excluded from the result.

- **Trade-offs**: The catch is not checking if node exists in graph before accessing dependencies can cause errors. - Use `Set` for O(1) visited checks, iterate over visited set to build result efficiently.

Example:

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

## Q123. 🏛️ Implement an AutocompleteSystem class using a Trie data structure.

Autocomplete uses a Trie (prefix tree) to efficiently store and search words by prefix. Each node represents a character, and paths from root to leaf nodes form complete words.

- **Trade-offs**: The catch is not storing the complete word at end nodes makes it harder to retrieve results. - Use `isEnd` flag to mark word boundaries, store word at end node for easy retrieval during DFS.

Example:

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

## Q124. 🔧 Implement a deepOmit function that recursively removes specified keys from objects and arrays.

Deep omit recursively removes specified keys from objects at all nested levels. It handles arrays by mapping over items and objects by filtering out omitted keys, preserving the structure while removing unwanted properties.

- **Trade-offs**: The catch is not handling arrays separately can cause issues, forgetting to recurse on object values. - Use `typeof obj != 'object'` to catch primitives and null, check `Array.isArray` before object handling.

Example:

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

## Q125. 🎯 Common JavaScript anti-patterns to avoid

Common anti-patterns include modifying prototypes, using `var` instead of `let/const`, relying on type coercion with `==`, creating global variables, using `eval()`, callback hell, and mutating function parameters - these lead to bugs, security issues, and hard-to-maintain code. Avoid modifying built-in prototypes, always use strict mode, and prefer explicit over implicit behavior.

- **Trade-offs**: The catch is modifying prototypes pollutes global scope and can break libraries - using `var` causes hoisting issues and function scope leaks. Type coercion with `==` leads to surprise bugs, global variables cause namespace pollution, and `eval()` is a security risk. Anti-patterns usually indicate missing understanding of JavaScript fundamentals, but watch out - callback hell makes code unreadable, mutating parameters causes side effects, and missing error handling leads to silent failures.

Example:

```js
// ❌ Anti-pattern: Modifying prototypes
Array.prototype.last = function() { return this[this.length - 1]; };

// ✅ Use utility functions instead
const last = (arr) => arr[arr.length - 1];

// ❌ Anti-pattern: Using var
for (var i = 0; i < 3; i++) {
  setTimeout(() => console.log(i), 100); // Prints 3, 3, 3
}

// ✅ Use let/const
for (let i = 0; i < 3; i++) {
  setTimeout(() => console.log(i), 100); // Prints 0, 1, 2
}

// ❌ Anti-pattern: Type coercion with ==
if (x == null) { } // Can match both null and undefined, but confusing

// ✅ Use === for explicit comparison
if (x === null || x === undefined) { }
// Or: if (x == null) is acceptable for null/undefined check

// ❌ Anti-pattern: Global variables
total = 0; // Creates global variable

// ✅ Use const/let
const total = 0;

// ❌ Anti-pattern: Using eval()
eval('console.log("dangerous")'); // Security risk

// ✅ Use proper parsing/execution
const code = 'console.log("safe")';
// Avoid eval entirely

// ❌ Anti-pattern: Callback hell
getData(function(a) {
  getMoreData(a, function(b) {
    getMoreData(b, function(c) {
      // Nested callbacks
    });
  });
});

// ✅ Use Promises/async-await
const a = await getData();
const b = await getMoreData(a);
const c = await getMoreData(b);

// ❌ Anti-pattern: Mutating function parameters
function updateUser(user) {
  user.name = 'New Name'; // Mutates original
  return user;
}

// ✅ Return new object
function updateUser(user) {
  return { ...user, name: 'New Name' };
}

// ❌ Anti-pattern: Missing error handling
fetch('/api/data').then(data => process(data));

// ✅ Always handle errors
fetch('/api/data')
  .then(data => process(data))
  .catch(error => handleError(error));

```

---

## Q126. 🔧 Write a reverseWords function that reverses each word while keeping delimiters intact.

Reverse each alphanumeric word individually while preserving original spacing and punctuation by scanning the string, collecting characters, and reversing them when hitting a delimiter.

- **Trade-offs**: The catch is failing to flush last word after loop causes missing output. - Regex guards against punctuation; customize pattern for locale-specific characters.

Example:

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

## Q127. 🔧 Implement a customAssign function that mimics Object.assign behavior.

Custom assign copies enumerable own properties from source objects to a target object. It processes sources in order, overwriting target properties with later source values, and returns the modified target.

- **Trade-offs**: The catch is not checking for null/undefined sources, copying inherited properties instead of own properties. - Use `Object.prototype.hasOwnProperty.call()` for safe property checking, handle null sources gracefully.

Example:

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

<div align="center">

**[← Previous: Web Workers, Service Workers & Real-World Topics](6%29%20Web%20Workers%2C%20Service%20Workers%20%26%20Real-World%20Topics.md)** | **[Next: JavaScript Output Questions →](8%29%20JavaScript%20Output%20Questions.md)**

</div>

