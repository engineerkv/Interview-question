# 🧰 8. Practical JavaScript Questions (Q78–108)

---

## 78) Implement function currying manually.

Concept:
Currying transforms a multi-argument function into a chain of single-argument functions.

Example:
```js
const curry = fn => (...args) =>
  args.length >= fn.length ? fn(...args) : (...more) => curry(fn)(...args, ...more);
const add = (a, b, c) => a + b + c;
curry(add)(1)(2)(3); // 6
```

Deep Insight:
- Check arity (`fn.length`) to determine when to execute
- Return new curried function for partial application
- Preserve `this` context if needed
- Useful for partial application and composition
- Consider placeholder support for advanced use cases

---

## 79) Write a custom `bind()` polyfill.

Concept:
`bind()` creates a new function with `this` bound and optional partial arguments.

Example:
```js
Function.prototype.bind = function(context, ...args) {
  const fn = this;
  return function(...moreArgs) {
    return fn.apply(context, [...args, ...moreArgs]);
  };
};
```

Deep Insight:
- Store original function and bound context
- Return new function that calls original with `apply`
- Merge bound arguments with new arguments
- Preserve function properties if needed
- Handle edge cases like `new` operator

---

## 80) Implement your own `Promise.all()` polyfill.

Concept:
`Promise.all()` resolves when all promises fulfill or rejects on first failure.

Example:
```js
Promise.all = function(promises) {
  return new Promise((resolve, reject) => {
    const results = [];
    let completed = 0;
    promises.forEach((p, i) => {
      Promise.resolve(p).then(val => {
        results[i] = val;
        completed++;
        if (completed === promises.length) resolve(results);
      }).catch(reject);
    });
  });
};
```

Deep Insight:
- Handle non-promise values with `Promise.resolve`
- Preserve order of results array
- Reject immediately on first failure
- Count completions to know when done
- Return empty array for empty input

---

## 81) Write a debounce function.

Concept:
Debounce delays function execution until after a specified time has passed since last call.

Example:
```js
const debounce = (fn, delay) => {
  let timeoutId;
  return (...args) => {
    clearTimeout(timeoutId);
    timeoutId = setTimeout(() => fn(...args), delay);
  };
```

Deep Insight:
- Clear previous timeout on each call
- Only execute after delay period of inactivity
- Useful for search inputs and resize events
- Consider immediate execution option
- Return cleanup function for manual cancellation

---

## 82) Write a throttle function.

Concept:
Throttle limits function execution to once per specified time period.

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

Deep Insight:
- Track last execution time
- Execute immediately if enough time passed
- Drop calls that come too soon
- Useful for scroll and mouse move events
- Consider leading/trailing edge options

---

## 83) Flatten a deeply nested array.

Concept:
Recursively flatten arrays to any depth, handling nested structures.

Example:
```js
const flatten = arr => arr.reduce((acc, val) => 
  Array.isArray(val) ? acc.concat(flatten(val)) : acc.concat(val), []);
flatten([1, [2, [3, 4]], 5]); // [1, 2, 3, 4, 5]
```

Deep Insight:
- Use recursion to handle arbitrary depth
- Check `Array.isArray` for nested arrays
- Use `reduce` for functional approach
- Consider depth limit to prevent stack overflow
- Handle edge cases like empty arrays

---

## 84) Implement a deep clone function without JSON.

Concept:
Recursively clone objects and arrays, handling different data types appropriately.

Example:
```js
const deepClone = obj => {
  if (obj === null || typeof obj !== 'object') return obj;
  if (obj instanceof Date) return new Date(obj);
  if (obj instanceof Array) return obj.map(deepClone);
  return Object.fromEntries(
    Object.entries(obj).map(([k, v]) => [k, deepClone(v)])
  );
};
```

Deep Insight:
- Handle primitives, dates, arrays, and objects
- Use `Object.fromEntries` for object cloning
- Watch for circular references (use WeakMap)
- Preserve constructor chains when possible
- Consider `structuredClone` for modern environments

---

## 85) Memoize a given function to cache results.

Concept:
Memoization caches function results based on arguments to avoid repeated computation.

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

Deep Insight:
- Use Map for O(1) cache lookups
- Serialize arguments for cache keys
- Consider memory limits and cache eviction
- Works best with pure functions
- Handle edge cases like circular references

---

## 86) Implement a custom event emitter (pub/sub).

Concept:
Event emitter allows objects to subscribe to and emit events with data.

Example:
```js
class EventEmitter {
  constructor() { this.events = {}; }
  on(event, fn) { (this.events[event] ||= []).push(fn); }
  emit(event, data) { (this.events[event] || []).forEach(fn => fn(data)); }
  off(event, fn) { this.events[event] = (this.events[event] || []).filter(f => f !== fn); }
}
```

Deep Insight:
- Store event handlers in object/Map
- Support multiple listeners per event
- Provide `on`, `emit`, and `off` methods
- Consider `once` method for single-use listeners
- Handle error cases and edge scenarios

---

## 87) Implement a retry mechanism for a failed promise.

Concept:
Retry failed operations with exponential backoff and maximum attempt limits.

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

Deep Insight:
- Use exponential backoff to prevent thundering herd
- Add jitter to distribute retry timing
- Consider circuit breakers for cascading failures
- Log retries for observability
- Set reasonable limits to avoid infinite loops

---

## 88) Write a function to compose multiple functions (`compose(f,g,h)` style).

Concept:
Function composition applies functions from right to left, creating a pipeline.

Example:
```js
const compose = (...fns) => x => fns.reduceRight((acc, fn) => fn(acc), x);
const add1 = x => x + 1;
const double = x => x * 2;
compose(console.log, add1, double)(5); // 11
```

Deep Insight:
- Use `reduceRight` for right-to-left application
- Each function receives result of previous
- Great for data transformation pipelines
- Consider `pipe` (left-to-right) alternative
- Works well with curried functions

---

## 89) Implement a custom `map()` method for arrays.

Concept:
`map()` creates new array by applying function to each element.

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

Deep Insight:
- Create new array, don't modify original
- Pass element, index, and array to callback
- Handle sparse arrays correctly
- Support `thisArg` for context binding
- Consider edge cases like undefined elements

---

## 90) Implement a `once()` function that executes only once.

Concept:
`once()` ensures a function can only be called once, returning the same result on subsequent calls.

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

Deep Insight:
- Track if function has been called
- Cache result for subsequent calls
- Useful for initialization and setup
- Consider error handling for failed calls
- Works with both sync and async functions

---

## 91) Convert callback-based code to a promise-based version.

Concept:
Wrap callback-based functions in promises using the Promise constructor.

Example:
```js
const readFile = path => new Promise((resolve, reject) => {
  fs.readFile(path, (err, data) => {
    if (err) reject(err);
    else resolve(data);
  });
});
```

Deep Insight:
- Use Promise constructor for one-time operations
- Handle both success and error cases
- Consider promisify utilities for Node.js
- Maintain same error handling patterns
- Test thoroughly with edge cases

---

## 92) Write a function to limit the number of concurrent promises.

Concept:
Control concurrency by limiting how many promises can run simultaneously.

Example:
```js
const limitConcurrency = (tasks, limit) => {
  const results = [];
  let running = 0, index = 0;
  return new Promise(resolve => {
    const runNext = () => {
      if (index >= tasks.length && running === 0) return resolve(results);
      if (running >= limit || index >= tasks.length) return;
      running++;
      const task = tasks[index++];
      task().then(result => {
        results[index - 1] = result;
        running--;
        runNext();
      });
    };
    runNext();
  });
};
```

Deep Insight:
- Track running and completed tasks
- Queue tasks when limit reached
- Preserve result order in output array
- Handle errors appropriately
- Useful for API rate limiting

---

## 93) Write a function that returns a promise resolved after a delay.

Concept:
Create a promise that resolves after a specified time delay.

Example:
```js
const delay = ms => new Promise(resolve => setTimeout(resolve, ms));
delay(1000).then(() => console.log('1 second later'));
```

Deep Insight:
- Use `setTimeout` with Promise constructor
- Return promise for chaining
- Useful for testing and rate limiting
- Consider cancellation with AbortController
- Can be used with async/await

---

## 94) Implement a chainable calculator API (`calc.add(5).multiply(2).value()`).

Concept:
Create a fluent interface where methods return the object for chaining.

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

Deep Insight:
- Return `this` from methods for chaining
- Store state in the object
- Use getter for final value access
- Consider immutable alternatives
- Great for builder patterns

---

## 95) Implement a simple version of `setInterval` using `setTimeout`.

Concept:
Use recursive `setTimeout` calls to create interval-like behavior.

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

Deep Insight:
- Recursive calls create repeating behavior
- Return cleanup function for cancellation
- More flexible than native `setInterval`
- Consider drift correction for precise timing
- Handle errors to prevent stopping

---

## 96) Write a function to shuffle an array randomly.

Concept:
Randomly reorder array elements using Fisher-Yates shuffle algorithm.

Example:
```js
const shuffle = arr => {
  const result = [...arr];
  for (let i = result.length - 1; i > 0; i--) {
    const j = Math.floor(Math.random() * (i + 1));
    [result[i], result[j]] = [result[j], result[i]];
  }
```

Deep Insight:
- Use Fisher-Yates for uniform distribution
- Work backwards through array
- Swap elements randomly
- Create copy to avoid mutating original
- Consider seeded random for testing

---

## 97) Implement your own version of `debounce + immediate` combined logic.

Concept:
Combine debounce with immediate execution option for first call.

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

Deep Insight:
- Execute immediately on first call if enabled
- Clear timeout on subsequent calls
- Reset timeout flag after execution
- Useful for search with immediate feedback
- Consider both leading and trailing options

---

## 98) How do you implement useMemo from scratch?

Concept:
`useMemo` caches the result of a computation and only recalculates when dependencies change.

Example:
```js
const useMemo = (computeFn, deps) => {
  const [memoizedValue, setMemoizedValue] = useState(() => computeFn());
  const [prevDeps, setPrevDeps] = useState(deps);
  
  useEffect(() => {
    const hasChanged = !deps || deps.some((dep, i) => dep !== prevDeps[i]);
    if (hasChanged) {
      setMemoizedValue(computeFn());
      setPrevDeps(deps);
    }
  }, deps);
  
  return memoizedValue;
};
```

Deep Insight:
- Store previous dependencies for comparison
- Only recalculate when dependencies change
- Use shallow comparison for dependency checking
- Return cached value when dependencies unchanged
- Consider cleanup for expensive computations

---

## 99) How do you implement useCallback from scratch?

Concept:
`useCallback` returns a memoized version of a function that only changes when dependencies change.

Example:
```js
const useCallback = (callback, deps) => {
  const [memoizedCallback, setMemoizedCallback] = useState(() => callback);
  const [prevDeps, setPrevDeps] = useState(deps);
  
  useEffect(() => {
    const hasChanged = !deps || deps.some((dep, i) => dep !== prevDeps[i]);
    if (hasChanged) {
      setMemoizedCallback(() => callback);
      setPrevDeps(deps);
    }
  }, deps);
  
  return memoizedCallback;
};
```

Deep Insight:
- Memoize function reference, not execution
- Prevent unnecessary re-renders in child components
- Use shallow comparison for dependency arrays
- Return same function reference when deps unchanged
- Essential for performance optimization in React

---

## 100) What is Compact Number (Intl.NumberFormat)?

Concept:
Compact Number formatting displays large numbers in a shortened, human-readable format using locale-specific abbreviations.

Example:
```js
const formatter = new Intl.NumberFormat('en-US', { notation: 'compact' });
console.log(formatter.format(1000)); // "1K"
console.log(formatter.format(1000000)); // "1M"
console.log(formatter.format(1500000)); // "1.5M"
```

Deep Insight:
- Uses `Intl.NumberFormat` with `notation: 'compact'` option
- Supports different locales for localized formatting
- Handles various compact notation styles (K, M, B, T)
- Useful for displaying large numbers in UI components
- Can be customized with additional formatting options

---

## 101) Explain why the following doesn't work as an IIFE: function foo(){ }();. What needs to be changed to properly make it an IIFE?

Concept:
The issue is that `function foo(){ }()` is parsed as a function declaration followed by a grouping operator, not as a function expression.

Example:
```js
// This doesn't work - parsed as function declaration + grouping
function foo(){ }(); // SyntaxError

// These work - function expressions
(function foo(){ })();
(function foo(){ }());
!function foo(){ }();
+function foo(){ }();
```

Deep Insight:
- Function declarations can't be immediately invoked
- Need parentheses to make it a function expression
- Various operators can force expression context
- IIFE creates isolated scope for variables
- Common pattern for modules and avoiding global pollution

---

## 102) What are JavaScript object property flags and descriptors?

Concept:
Property descriptors define the characteristics of object properties, including configurability, enumerability, writability, and value.

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
// { value: 'John', writable: false, enumerable: true, configurable: false }
```

Deep Insight:
- `writable`: Can property value be changed
- `enumerable`: Shows up in `for...in` loops
- `configurable`: Can descriptor be modified or property deleted
- `value`: The property's value
- Use `Object.defineProperty` to set custom descriptors

---

## 103) What are server-sent events?

Concept:
Server-Sent Events (SSE) enable servers to push data to web pages in real-time using a unidirectional connection.

Example:
```js
// Client-side
const eventSource = new EventSource('/events');
eventSource.onmessage = function(event) {
  console.log('Received:', event.data);
};

// Server-side (Node.js)
app.get('/events', (req, res) => {
  res.writeHead(200, {
    'Content-Type': 'text/event-stream',
    'Cache-Control': 'no-cache',
    'Connection': 'keep-alive'
  });
  res.write('data: Hello World\n\n');
});
```

Deep Insight:
- Unidirectional: Server to client only
- Built on HTTP, simpler than WebSockets
- Automatic reconnection on connection loss
- Use `text/event-stream` MIME type
- Good for live updates, notifications, real-time data

---

## 104) What are proxies in JavaScript used for?

Concept:
Proxies allow you to intercept and customize operations performed on objects, enabling meta-programming capabilities.

Example:
```js
const handler = {
  get(target, prop) {
    console.log(`Accessing property: ${prop}`);
    return target[prop];
  },
  set(target, prop, value) {
    console.log(`Setting ${prop} to ${value}`);
    target[prop] = value;
    return true;
  }
};

const proxy = new Proxy({}, handler);
proxy.name = 'John'; // "Setting name to John"
console.log(proxy.name); // "Accessing property: name" then "John"
```

Deep Insight:
- Intercept fundamental operations (get, set, has, delete)
- Enable validation, logging, and virtual properties
- Used in frameworks for reactivity and data binding
- Can create virtual objects that don't exist
- Powerful tool for creating advanced abstractions

---

## 105) What are some techniques for reducing reflows and repaints?

Concept:
Reflows and repaints are expensive browser operations; minimize them by batching changes and using efficient DOM manipulation.

Example:
```js
// Bad - causes multiple reflows
element.style.width = '100px';
element.style.height = '100px';
element.style.margin = '10px';

// Good - batch changes
element.style.cssText = 'width: 100px; height: 100px; margin: 10px;';

// Better - use classes
element.className = 'new-style';

// Best - use DocumentFragment
const fragment = document.createDocumentFragment();
fragment.appendChild(newElement);
container.appendChild(fragment);
```

Deep Insight:
- Batch DOM changes to minimize reflows
- Use `DocumentFragment` for multiple insertions
- Change classes instead of individual styles
- Use `transform` and `opacity` for animations
- Measure elements before making changes

---

## 106) What are some tools that can be used to measure and analyze JavaScript performance?

Concept:
Various tools help measure and analyze JavaScript performance, from browser dev tools to specialized profiling tools.

Example:
```js
// Performance API
const start = performance.now();
// ... expensive operation
const end = performance.now();
console.log(`Operation took ${end - start} milliseconds`);

// Memory usage
console.log(performance.memory);
// { usedJSHeapSize: 1000000, totalJSHeapSize: 2000000, jsHeapSizeLimit: 4000000 }
```

Deep Insight:
- **Chrome DevTools**: Performance tab, Memory tab, Lighthouse
- **Performance API**: `performance.now()`, `performance.memory`
- **Web Vitals**: LCP, FID, CLS measurements
- **Profiling**: CPU profiling, memory profiling
- **Third-party**: New Relic, DataDog, Sentry for production monitoring

---

## 107) Explain the concept of a microtask queue?

Concept:
The microtask queue processes high-priority tasks that should execute before the next task in the main queue, including Promise callbacks and queueMicrotask.

Example:
```js
console.log('1');
setTimeout(() => console.log('2'), 0);
Promise.resolve().then(() => console.log('3'));
queueMicrotask(() => console.log('4'));
console.log('5');
// Output: 1, 5, 3, 4, 2
```

Deep Insight:
- Microtasks have higher priority than macrotasks
- Processed after current execution stack is empty
- Includes Promise callbacks and `queueMicrotask`
- Can starve the main queue if not managed properly
- Essential for understanding async JavaScript execution order

---

## 119) How can you optimize DOM manipulation for better performance?

Concept:
Optimize DOM manipulation by minimizing reflows, using efficient selectors, and leveraging modern APIs for better performance.

Example:
```js
// Use efficient selectors
const elements = document.querySelectorAll('.item'); // Better than getElementsByClassName

// Batch DOM changes
const fragment = document.createDocumentFragment();
items.forEach(item => {
  const li = document.createElement('li');
  li.textContent = item.name;
  fragment.appendChild(li);
});
list.appendChild(fragment);

// Use requestAnimationFrame for animations
function animate() {
  element.style.transform = `translateX(${position}px)`;
  position += 1;
  if (position < 1000) {
    requestAnimationFrame(animate);
  }
}
```

Deep Insight:
- Minimize reflows and repaints
- Use `DocumentFragment` for multiple insertions
- Cache DOM queries and reuse elements
- Use `requestAnimationFrame` for smooth animations
- Consider virtual DOM libraries for complex UIs
