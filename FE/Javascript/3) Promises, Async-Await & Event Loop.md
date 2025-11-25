# 5. Promises, Async/Await & Event Loop (Q56–81)

<div align="center">

**[← Previous: ES6+ Features](6%29%20ES6%2B%20Features.md)** | **[Next: Practical JavaScript Questions →](9%29%20Practical%20JavaScript%20Questions.md)**

</div>

---

## Q56. Promises in JavaScript

A Promise is a placeholder for a future value that can be pending, fulfilled, or rejected - it helps handle async operations cleanly without callback nesting. Promises have three states: pending (initial state), fulfilled (success), or rejected (failure) - once settled, they can't change state. Perfect for API calls, file operations, and async data loading.

- **Trade-offs**: Promise handlers run as microtasks in the event loop - they execute after the current code but before the next macrotask, which ensures predictable execution order, but too many microtasks can starve the browser's rendering and make the UI feel unresponsive.

Example:

```js
const getData = () => fetch('/api').then(r => r.json());
getData().then(data => console.log(data));
```

---

## Q57. Callbacks vs Promises

Promises make async code easier to read and handle errors better than callbacks - they avoid callback hell by chaining instead of nesting. Promises chain flatly instead of nesting callbacks, making code more readable and maintainable.

- **Trade-offs**: The catch is promises always execute asynchronously via microtasks, which can be confusing if you expect immediate execution. Mixing callbacks and promises in the same code can lead to inconsistent patterns - stick to one approach.

Example:

```js
// Callback style (nested)
getData(data => {
  processData(data, result => {
    saveData(result, () => console.log('done'));
  });
});

// Promise style (flat)
getData().then(processData).then(saveData);
```

---

## Q58. Chaining Promises

Promise chaining allows you to pass data from one async operation to the next using `.then()` methods - each step receives the result from the previous one. You can return promises or regular values, and the chain waits for promises to resolve before moving to the next step.

- **Trade-offs**: The tricky part is forgetting to return values in `.then()` handlers breaks the data flow - the next `.then()` gets `undefined` instead of your data. Use arrow functions with implicit returns when possible to avoid this common mistake.

Example:

```js
fetch('/user')
  .then(response => response.json())
  .then(user => fetch(`/posts/${user.id}`))
  .then(response => response.json())
  .then(posts => console.log(posts));
```

---

## Q59. Async/await: what it is and how it works

`Promise.resolve()` creates a resolved promise immediately, while `new Promise()` allows you to control when it resolves - use the first for values, the second for async work. `Promise.resolve()` is great for wrapping values or converting thenables, while `new Promise()` is for wrapping callback-based APIs.

- **Trade-offs**: Watch out for the `new Promise(async ...)` anti-pattern - it's redundant and can cause issues. Use `Promise.resolve()` when you already have a value, and `new Promise()` only when you need to wrap callbacks or control resolution timing.

Example:

```js
const p1 = Promise.resolve(42); // Immediate resolution
const p2 = new Promise(resolve => {
  setTimeout(() => resolve(42), 1000);
}); // Manual control
```

---

## Q60. `Promise.resolve()` vs `new Promise()`

Use `.catch()` to handle errors in promise chains - it catches both thrown errors and rejected promises, allowing you to recover or handle failures gracefully. You can recover from errors and continue the chain, or handle them at the end.

- **Trade-offs**: The catch is swallowing errors without proper handling can hide bugs - always log or handle errors appropriately. You can place `.catch()` anywhere in the chain, but it only catches errors from handlers above it.

Example:

```js
fetch('/api/data')
  .then(response => {
    if (!response.ok) throw new Error('Failed');
    return response.json();
  })
  .catch(error => ({ error: true }))
  .then(data => console.log(data));
```

---

## Q61. Handling errors in Promises

When you return a promise inside `.then()`, the outer promise waits for the inner one to complete - this enables chaining dependent async operations. Errors in inner promises bubble up to outer chains, so you can handle them at any level.

- **Trade-offs**: This is the key to clean async workflows without nested callbacks, but watch out - nesting `.then()` instead of returning promises breaks the chain and makes code harder to read.

Example:

```js
Promise.resolve(5)
  .then(id => fetch(`/user/${id}`))
  .then(response => response.json())
  .then(user => console.log(user.name));
```

---

## Q62. Callback hell: what it is and how to avoid it

If you forget to return from `.then()`, the next `.then()` gets `undefined` instead of your data - this breaks the data flow in the chain. This is one of the most common promise mistakes and can be hard to debug.

- **Trade-offs**: Always return something from `.then()` handlers to pass data forward - use arrow functions with implicit returns when possible to avoid this mistake. Linters can catch missing returns, but it's easy to miss in complex chains.

Example:

```js
Promise.resolve(5)
  .then(x => { x * 2; }) // Missing return!
  .then(result => console.log(result)); // undefined
```

---

## Q63. Event Loop in JavaScript

The event loop is JavaScript's way of handling async operations - it continuously checks the call stack, and when it's empty, it processes tasks from the microtask queue first, then one task from the macrotask queue, and repeats this cycle. Promise callbacks run as microtasks, so they execute right after the current code finishes but before any `setTimeout` or other macrotasks.

- **Trade-offs**: This order gives you predictable async behavior, but the catch is promises don't run immediately even though they might seem like they should - they always wait until the current code stack is completely done. Since microtasks have priority over macrotasks, promise handlers will always run before `setTimeout` callbacks, which can be surprising if you're not aware of this.

Example:

```js
console.log('First');
Promise.resolve().then(() => console.log('Second'));
console.log('Third');
// Output: First, Third, Second
```

---

## Q64. Microtasks vs macrotasks

Microtasks (promises, queueMicrotask) run before the next macrotask (setTimeout, I/O) at microtask checkpoints - this ensures promises execute before timers. The event loop processes all microtasks before moving to the next macrotask.

- **Trade-offs**: The catch is overusing microtasks can starve rendering and make the UI feel unresponsive - use them wisely. Expecting `setTimeout` to run before promises is a common mistake because microtasks always run first.

Example:

```js
setTimeout(() => console.log('macro'));
Promise.resolve().then(() => console.log('micro'));
// micro logs before macro
```

---

## Q65. Running Promises concurrently

Avoid callback hell by chaining promises instead of nesting callbacks - keep each step simple and readable. Use `Promise.all()` for parallel operations, and chain dependent operations sequentially.

- **Trade-offs**: The catch is mixing callbacks and promises in the same code creates inconsistent patterns - stick to one approach. Promise chains are more readable than nested callbacks, but they can still get long - consider breaking them into smaller functions.

Example:

```js
getUser(id)
  .then(user => getPosts(user.id))
  .then(posts => getComments(posts[0].id))
  .then(comments => console.log(comments));
```

---

## Q66. `Promise.all()`: what it is and when to use it

`async/await` makes promises easier to read by letting you write async code that looks like regular code - it's syntactic sugar over promises. `async` functions always return promises, and `await` pauses execution until the promise settles, then resumes with the result.

- **Trade-offs**: The catch is forgetting the `await` keyword is the #1 async/await mistake - you get a promise object instead of the actual result. `async/await` is just syntactic sugar, so it compiles to similar code as promise chains, but it's much more readable for sequential async operations.

Example:

```js
async function getUserData(id) {
  const response = await fetch(`/user/${id}`);
  const user = await response.json();
  return user;
}
```

---

## Q67. `Promise.race()`: what it is and when to use it

If you call an async function without `await`, you get a promise object instead of the actual result - this causes bugs where you expect data but get promises. This is the most common async/await mistake and can be confusing to debug.

- **Trade-offs**: Always use `await` when you need the result, not the promise - but you can return promises from async functions for chaining if that's what you want. The tricky part is sometimes you intentionally want the promise for parallel execution, so be clear about your intent.

Example:

```js
async function getData() {
  const response = await fetch('/api');
  return response.json();
}

const promise = getData(); // Without await - returns a promise
const data = await getData(); // With await - returns the actual data
```

---

## Q68. `Promise.allSettled()`: what it is and when to use it

Promise handlers run as microtasks, and `await` schedules continuation as a microtask after the current turn - this is how async/await works under the hood. The event loop processes all microtasks before moving to the next macrotask, ensuring predictable execution order.

- **Trade-offs**: The catch is `await` doesn't block the thread - it pauses execution and schedules continuation as a microtask, which can be confusing if you expect blocking behavior. Continuations run after other microtasks queued earlier, so the order matters.

Example:

```js
(async () => {
  console.log('A');
  await 0;
  console.log('B');
})();
// A then B
```

---

## Q69. `Promise.any()`: what it is and when to use it

Start all promises before awaiting to run them in parallel - use combinators like `Promise.all()`, `allSettled()`, `race()`, or `any()` to aggregate results. This is much faster than awaiting promises one by one.

- **Trade-offs**: The catch is awaiting promises one by one instead of in parallel is a common mistake that makes code slower - always start all promises first, then await them together. Use the right combinator for your needs - `all()` for all results, `allSettled()` for partial success, `race()` for timeouts, `any()` for failover.

Example:

```js
const a = fetch('/a');
const b = fetch('/b');
const [ra, rb] = await Promise.all([a, b]);
```

---

## Q70. Implementing retry logic with Promises

`Promise.all()` waits for all promises to fulfill or fails fast on first rejection - use it when you need all results or want to fail quickly. Results array matches input order, not completion order, which makes it easy to map results back to inputs.

- **Trade-offs**: The catch is `Promise.all()` fails fast if any promise rejects, so you lose all results if one fails, which might not be what you want - use `Promise.allSettled()` if you need partial success. It's perfect when you need all results, but watch out for using it when some promises might fail.

Example:

```js
const [user, posts] = await Promise.all([
  fetch('/user').then(r => r.json()),
  fetch('/posts').then(r => r.json())
]);
```

---

## Q71. Promise cancellation: what it is and how to implement it

`Promise.race()` resolves with the first promise to settle (fulfill or reject) - use it for timeouts, cancellation, or first-available service patterns. It returns the first promise to complete, whether success or failure.

- **Trade-offs**: The catch is expecting only successful results from `race()` - it returns the first to complete, even if it's a rejection. Other promises continue running in the background, so be careful about resource usage. Use `Promise.any()` if you need the first success only.

Example:

```js
const timeout = new Promise((_, reject) => 
  setTimeout(() => reject(new Error('timeout')), 5000)
);
const data = await Promise.race([fetch('/data'), timeout]);
```

---

## Q72. Running Promises sequentially

`Promise.allSettled()` waits for all promises to complete regardless of success/failure - it never rejects and always returns results with status. Each result has `status` and `value`/`reason` properties, so you can filter successful vs failed results.

- **Trade-offs**: The catch is using `Promise.all()` when you need partial success - `allSettled()` is better for batch operations where some might fail. It's perfect for retry logic and operations where you want to know what succeeded and what failed, but you need to manually filter results.

Example:

```js
const results = await Promise.allSettled([
  fetch('/a'), fetch('/b'), fetch('/c')
]);
const successes = results.filter(r => r.status === 'fulfilled');
```

---

## Q73. Implementing progress updates with Promises

`Promise.any()` resolves with the first successful promise, while `race()` resolves with the first to settle (success or failure) - use `any()` for failover, `race()` for timeouts. `any()` ignores rejections until all promises fail, then rejects with an AggregateError.

- **Trade-offs**: The catch is using `race()` when you need success only - `any()` is better for failover scenarios where you want the first working service. It's perfect when you have multiple options and want the first one that succeeds, but watch out - if all fail, you get an AggregateError with all rejection reasons.

Example:

```js
const fast = await Promise.any([
  slowApi(), fastApi(), backupApi()
]);
// vs race: first to complete (even if error)
```

---

## Q74. `Promise.finally()`: what it is and when to use it

Wrap async operations in retry loops with exponential backoff and max attempts - this improves reliability for transient failures. Use jitter to distribute retry timing across clients and avoid overwhelming services.

- **Trade-offs**: The catch is retrying too aggressively without backoff can overwhelm services and make problems worse - always use exponential backoff. Retry logic is great for transient failures, but watch out for infinite retries on permanent failures - always set a max attempts limit.

Example:

```js
const retry = (fn, max = 3) => 
  fn().catch(err => max > 0 ? retry(fn, max - 1) : Promise.reject(err));
```

---

## Q75. Promise vs async/await: differences and mixing them

Use `AbortController` for fetch requests or custom cancellation tokens for other async work - cancellation is cooperative, not preemptive. The request checks the abort signal and stops when cancelled.

- **Trade-offs**: The catch is not cleaning up cancelled requests can leak resources - always handle cleanup properly. Cancellation is cooperative, so the async operation needs to check the signal and stop itself - it won't magically stop mid-execution. Use custom cancellation tokens for non-fetch async work.

Example:

```js
const controller = new AbortController();
fetch('/data', { signal: controller.signal });
controller.abort(); // cancels request
```

---

## Q76. Handling multiple async operations

Use `for...of` loops or `reduce()` to await promises one at a time instead of parallel execution - use this when order matters or resources are limited. Sequential execution is slower but more predictable and resource-friendly.

- **Trade-offs**: The catch is using parallel when sequential is needed - sequential is better for database operations, file processing, and API rate limits. It's slower but more predictable, so use it when order matters or when you need to avoid overwhelming resources.

Example:

```js
const results = [];
for (const url of urls) {
  const data = await fetch(url).then(r => r.json());
  results.push(data);
}
```

---

## Q77. Promise vs Observable

Emit progress events through callbacks or custom event systems during async work - this provides feedback for long-running operations. Call the progress callback after each step to update the UI.

- **Trade-offs**: The catch is not debouncing progress updates can cause performance issues - throttle or debounce updates to avoid overwhelming the UI. Progress callbacks are great for UX, but watch out for too many updates - consider batching or throttling them.

Example:

```js
const process = async (items, onProgress) => {
  for (let i = 0; i < items.length; i++) {
    await work(items[i]);
    onProgress((i + 1) / items.length);
  }
};
```

---

## Q78. Implementing timeout with Promises

`Promise.finally()` runs cleanup code regardless of whether the promise fulfills or rejects - use it for hiding loading spinners, closing connections, or resetting state. It runs after all `then`/`catch` handlers, so it's perfect for cleanup.

- **Trade-offs**: The catch is expecting `finally()` to receive or pass values - it doesn't receive the result or error, and it can't change what gets passed to the next handler. It's perfect for cleanup, but don't try to use it for data transformation - use `then` or `catch` for that.

Example:

```js
let loading = true;
fetch('/data')
  .then(handleData)
  .catch(handleError)
  .finally(() => { loading = false; });
```

---

## Q79. Promise vs Generator

`async/await` is syntactic sugar over promises - it makes async code look like regular code, but under the hood it's still promises. `async` functions always return promises, and `await` pauses execution until the promise settles. They're fully compatible - `await` works with any thenable, and async functions return promises, so you can mix them seamlessly.

- **Trade-offs**: The catch is they compile to similar code, so performance is the same - choose based on readability. `async/await` is better for sequential async operations, while promise chains are better for parallel operations or when you need more control. Inconsistent mixing without understanding compatibility can lead to confusion - both compile to similar code, so they work together fine. It's great for migrating from callbacks to promises, but try to be consistent within a codebase - don't mix styles randomly.

Example:

```js
// async/await is syntactic sugar over promises
async function example() {
  const p = Promise.resolve(1);
  const a = await p; // await works with any thenable
  return p.then(x => x + 1); // can mix both styles
}
```

---

## Q80. How fetch Promise works internally in V8

When you call fetch, V8 creates a Promise right away and hands off the actual network work to the browser's task queue - so the networking happens outside of JavaScript entirely. The Promise sits there waiting, and once the network request finishes, it resolves and your handlers run as microtasks.

- **Trade-offs**: The tricky part is that fetch doesn't block your code - it returns that Promise immediately and does all the network stuff asynchronously in the background. This is why your main thread stays responsive, but you need to remember that the network work is still happening even though your code has already moved on.

Example:

```js
const promise = fetch('/api/data');
promise.then(response => {
  console.log('Response received');
});
```

---

## Q81. Promise chaining and error propagation

Promise chaining allows you to connect multiple async operations sequentially - each `.then()` returns a new promise, which can be chained further. Errors propagate down the chain until caught by a `.catch()` handler - if any promise in the chain rejects, subsequent `.then()` handlers are skipped and the error bubbles to the nearest `.catch()`.

- **Trade-offs**: The catch is forgetting to return a value in `.then()` causes the next handler to receive `undefined` instead of the expected value. Promise chains can become hard to read with many nested operations - consider async/await for complex flows, but promise chaining is still useful for simple sequential operations.

Example:

```js
fetch('/api/user')
  .then(response => response.json())
  .then(user => fetch(`/api/posts/${user.id}`))
  .then(response => response.json())
  .then(posts => console.log(posts))
  .catch(error => console.error('Error:', error));
```

---
<div align="center">

**[← Previous: ES6+ Features](6%29%20ES6%2B%20Features.md)** | **[Next: Practical JavaScript Questions →](9%29%20Practical%20JavaScript%20Questions.md)**

</div>

**[← Previous Section](6%29%20ES6%2B%20Features.md)** | **[Next Section →](9%29%20Practical%20JavaScript%20Questions.md)**
