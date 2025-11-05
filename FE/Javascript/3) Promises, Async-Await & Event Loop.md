# 🔁 3. Promises, Async/Await & Event Loop (Q26–51)

---

## 26) What are Promises in JavaScript?

A Promise is a placeholder for a future value that can be pending, fulfilled, or rejected. It helps handle async operations cleanly.

```js
const getData = () => fetch('/api').then(r => r.json());
getData().then(data => console.log(data));
```

- **Core Concept**: Promises have three states: pending, fulfilled, or rejected
- **Real-World Use**: Perfect for API calls, file operations, and async data loading
- **Common Mistake**: Forgetting to return promises in chains
- **Advanced Feature**: Promise handlers run as microtasks in the event loop
- **Interview Tip**: Explain that always mention the three states and error handling

---

## 27) How do promises differ from callbacks?

Promises make async code easier to read and handle errors better than callbacks. They avoid callback hell.

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

- **Core Advantage**: Promises chain flatly instead of nesting callbacks
- **Real-World Use**: API calls, database operations, and file handling
- **Common Mistake**: Mixing callbacks and promises in the same code
- **Advanced Feature**: Promises always execute asynchronously via microtasks
- **Interview Tip**: Explain that show how promises solve the pyramid of doom problem

---

## 28) What is promise chaining?

Promise chaining lets you pass data from one async operation to the next using `.then()` methods.

```js
fetch('/user')
  .then(response => response.json())
  .then(user => fetch(`/posts/${user.id}`))
  .then(response => response.json())
  .then(posts => console.log(posts));
```

- **Core Rule**: Each `.then()` receives the return value from the previous one
- **Real-World Use**: Building complex async workflows step by step
- **Common Mistake**: Forgetting to return values in `.then()` handlers
- **Advanced Feature**: You can return promises or regular values
- **Interview Tip**: Explain that show how data flows through the chain

---

## 29) How do you return values through a promise chain?

To pass data through a promise chain, return values from each `.then()` handler.

```js
Promise.resolve(5)
  .then(x => x * 2)
  .then(y => y + 3)
  .then(result => console.log(result)); // 13
```

- **Core Rule**: Always return something from `.then()` to pass data forward
- **Real-World Use**: Transforming data through multiple async steps
- **Common Mistake**: Forgetting return statements breaks the chain
- **Advanced Feature**: Return promises for async operations, values for sync
- **Interview Tip**: Explain that demonstrate with a simple math example

---

## 30) How do you handle errors in a promise chain?

Use `.catch()` to handle errors in promise chains. It catches both thrown errors and rejected promises.

```js
fetch('/api/data')
  .then(response => {
    if (!response.ok) throw new Error('Failed');
    return response.json();
  })
  .catch(error => ({ error: true }))
  .then(data => console.log(data));
```

- **Core Rule**: `.catch()` handles any error in the chain above it
- **Real-World Use**: API error handling, fallback data, user notifications
- **Common Mistake**: Swallowing errors without proper handling
- **Advanced Feature**: You can recover from errors and continue the chain
- **Interview Tip**: Explain that show error handling with a real API example

---

## 31) What happens if you return a promise inside `.then()`?

When you return a promise inside `.then()`, the outer promise waits for the inner one to complete.

```js
Promise.resolve(5)
  .then(id => fetch(`/user/${id}`))
  .then(response => response.json())
  .then(user => console.log(user.name));
```

- **Core Rule**: Returning a promise makes the chain wait for it
- **Real-World Use**: Chaining dependent API calls and database operations
- **Common Mistake**: Nesting `.then()` instead of returning promises
- **Advanced Feature**: Errors in inner promises bubble up to outer chains
- **Interview Tip**: Explain that show how this enables clean async workflows

---

## 32) What happens if you forget to `return` inside `.then()`?

If you forget to return from `.then()`, the next `.then()` gets `undefined` instead of your data.

```js
Promise.resolve(5)
  .then(x => { x * 2; }) // Missing return!
  .then(result => console.log(result)); // undefined
```

- **Core Rule**: Always return something from `.then()` handlers
- **Real-World Impact**: This mistake breaks data flow in async chains
- **Common Mistake**: Forgetting return statements is very common
- **Optimization**: Use arrow functions with implicit returns when possible
- **Interview Tip**: Explain that show the difference between with and without return

---

## 33) How does promise resolution work internally?

Promises use the microtask queue to run handlers after the current code finishes, not immediately.

```js
console.log('First');
Promise.resolve().then(() => console.log('Second'));
console.log('Third');
// Output: First, Third, Second
```

- **Core Rule**: Promise handlers always run after the current code stack
- **Real-World Impact**: This ensures predictable async behavior
- **Common Mistake**: Expecting promises to run immediately
- **Advanced Feature**: Microtasks run before the next macrotask
- **Interview Tip**: Explain that explain the event loop order: stack → microtasks → macrotasks

---

## 34) What is the difference between `Promise.resolve()` and `new Promise()`?

`Promise.resolve()` creates a resolved promise immediately, while `new Promise()` lets you control when it resolves.

```js
const p1 = Promise.resolve(42); // Immediate resolution
const p2 = new Promise(resolve => {
  setTimeout(() => resolve(42), 1000);
}); // Manual control
```

- **Core Difference**: Use `Promise.resolve()` for values, `new Promise()` for async work
- **Real-World Use**: Wrapping old callback APIs into promises
- **Common Mistake**: Using `new Promise()` when `Promise.resolve()` would work
- **Advanced Feature**: Avoid the `new Promise(async ...)` anti-pattern
- **Interview Tip**: Explain that show when to use each approach

---

## 35) How do you avoid callback hell using Promises?

Avoid callback hell by chaining promises instead of nesting callbacks. Keep each step simple.

```js
getUser(id)
  .then(user => getPosts(user.id))
  .then(posts => getComments(posts[0].id))
  .then(comments => console.log(comments));
```

- **Core Strategy**: Chain promises instead of nesting callbacks
- **Real-World Use**: API workflows, database operations, file processing
- **Common Mistake**: Mixing callbacks and promises in the same code
- **Advanced Feature**: Use `Promise.all()` for parallel operations
- **Interview Tip**: Explain that show the before/after of callback hell

---

## 36) How does `async/await` work under the hood?

`async/await` makes promises easier to read by letting you write async code that looks like regular code.

```js
async function getUserData(id) {
  const response = await fetch(`/user/${id}`);
  const user = await response.json();
  return user;
}
```

- **Core Concept**: `async` functions always return promises, `await` pauses execution
- **Real-World Use**: API calls, database operations, file handling
- **Common Mistake**: Forgetting `await` keyword
- **Advanced Feature**: `async/await` is just syntactic sugar over promises
- **Interview Tip**: Explain that show how it makes code more readable than promise chains

---

## 37) What happens if you don't `await` an async function?

If you call an async function without `await`, you get a promise object instead of the actual result.

```js
async function getData() {
  const response = await fetch('/api');
  return response.json();
}

const promise = getData(); // Without await - returns a promise
const data = await getData(); // With await - returns the actual data
```

- **Core Rule**: Always use `await` when you need the result, not the promise
- **Real-World Impact**: This mistake causes bugs where you expect data but get promises
- **Common Mistake**: Forgetting `await` is the #1 async/await mistake
- **Advanced Feature**: You can return promises from async functions for chaining
- **Interview Tip**: Explain that show the difference between with and without `await`

---

## 38) What is the difference between microtasks and macrotasks?

Microtasks (promises, queueMicrotask) run before the next macrotask (setTimeout, I/O) at microtask checkpoints.

```js
setTimeout(() => console.log('macro'));
Promise.resolve().then(() => console.log('micro'));
// micro logs before macro
```

- **Core Rule**: Microtasks run before macrotasks in the event loop
- **Real-World Use**: Promise handlers, queueMicrotask, async/await
- **Common Mistake**: Expecting setTimeout to run before promises
- **Advanced Feature**: Overusing microtasks can starve rendering
- **Interview Tip**: Explain that explain the event loop order: stack → microtasks → macrotasks

---

## 39) How does the event loop handle Promises and async/await?

Promise handlers run as microtasks. `await` schedules continuation as a microtask after the current turn.

```js
(async () => {
  console.log('A');
  await 0;
  console.log('B');
})();
// A then B
```

- **Core Rule**: `await` pauses execution and schedules continuation as a microtask
- **Real-World Impact**: This is how async/await works under the hood
- **Common Mistake**: Not understanding that `await` doesn't block the thread
- **Advanced Feature**: Continuations run after other microtasks queued earlier
- **Interview Tip**: Explain that explain how `await` transforms functions into microtasks

---

## 40) How do you handle multiple promises concurrently?

Use combinators to run tasks together and aggregate results or outcomes.

```js
const a = fetch('/a');
const b = fetch('/b');
const [ra, rb] = await Promise.all([a, b]);
```

- **Core Strategy**: Start all promises before awaiting to run them in parallel
- **Real-World Use**: Loading multiple API endpoints, database queries
- **Common Mistake**: Awaiting promises one by one instead of in parallel
- **Advanced Feature**: Use `Promise.all()`, `allSettled()`, `race()`, or `any()` for different needs
- **Interview Tip**: Explain that show the difference between sequential and parallel execution

---

## 41) What is `Promise.all()` and when should you use it?

`Promise.all()` waits for all promises to fulfill or fails fast on first rejection.

```js
const [user, posts] = await Promise.all([
  fetch('/user').then(r => r.json()),
  fetch('/posts').then(r => r.json())
]);
```

- **Core Rule**: `Promise.all()` waits for all promises or fails fast on first rejection
- **Real-World Use**: Loading user data and posts together, multiple API calls
- **Common Mistake**: Using it when some promises might fail
- **Advanced Feature**: Results array matches input order, not completion order
- **Interview Tip**: Explain that show when to use `all()` vs `allSettled()` vs `race()`

---

## 42) What is `Promise.allSettled()`?

`Promise.allSettled()` waits for all promises to complete regardless of success/failure.

```js
const results = await Promise.allSettled([
  fetch('/a'), fetch('/b'), fetch('/c')
]);
const successes = results.filter(r => r.status === 'fulfilled');
```

- **Core Rule**: `allSettled()` never rejects, always returns results with status
- **Real-World Use**: Batch operations where some might fail, retry logic
- **Common Mistake**: Using `all()` when you need partial success
- **Advanced Feature**: Each result has `status` and `value`/`reason` properties
- **Interview Tip**: Explain that show how to filter successful vs failed results

---

## 43) What is `Promise.any()` and how is it different from `Promise.race()`?

`Promise.any()` resolves with first successful promise. `race()` resolves with first to settle (success or failure).

```js
const fast = await Promise.any([
  slowApi(), fastApi(), backupApi()
]);
// vs race: first to complete (even if error)
```

- **Core Difference**: `any()` waits for first success, `race()` takes first completion
- **Real-World Use**: `any()` for failover, `race()` for timeouts
- **Common Mistake**: Using `race()` when you need success only
- **Advanced Feature**: `any()` ignores rejections until all promises fail
- **Interview Tip**: Explain that show the difference with real examples

---

## 44) What is `Promise.race()`?

`Promise.race()` resolves with the first promise to settle (fulfill or reject).

```js
const timeout = new Promise((_, reject) => 
  setTimeout(() => reject(new Error('timeout')), 5000)
);
const data = await Promise.race([fetch('/data'), timeout]);
```

- **Core Rule**: `race()` returns the first promise to complete (success or failure)
- **Real-World Use**: Timeouts, cancellation, first-available service
- **Common Mistake**: Expecting only successful results from `race()`
- **Advanced Feature**: Other promises continue running in the background
- **Interview Tip**: Explain that show timeout pattern with `race()`

---

## 45) How do you implement retry logic using Promises?

Wrap async operations in retry loops with exponential backoff and max attempts.

```js
const retry = (fn, max = 3) => 
  fn().catch(err => max > 0 ? retry(fn, max - 1) : Promise.reject(err));
```

- **Core Strategy**: Retry with exponential backoff to avoid overwhelming services
- **Real-World Use**: API calls, network requests, database operations
- **Common Mistake**: Retrying too aggressively without backoff
- **Advanced Feature**: Use jitter to distribute retry timing across clients
- **Interview Tip**: Explain that show how to implement retry with max attempts

---

## 46) How do you cancel a Promise in JavaScript?

Use `AbortController` for fetch requests or custom cancellation tokens for other async work.

```js
const controller = new AbortController();
fetch('/data', { signal: controller.signal });
controller.abort(); // cancels request
```

- **Core Method**: Use `AbortController` for cancelling fetch requests
- **Real-World Use**: User navigation, timeout handling, cleanup
- **Common Mistake**: Not cleaning up cancelled requests
- **Advanced Feature**: Cancellation is cooperative, not preemptive
- **Interview Tip**: Explain that show how to implement custom cancellation tokens

---

## 47) How do you sequentially execute multiple promises?

Use `for...of` loops or `reduce()` to await promises one at a time instead of parallel execution.

```js
const results = [];
for (const url of urls) {
  const data = await fetch(url).then(r => r.json());
  results.push(data);
}
```

- **Core Strategy**: Use sequential execution when order matters or resources are limited
- **Real-World Use**: Database operations, file processing, API rate limits
- **Common Mistake**: Using parallel when sequential is needed
- **Optimization**: Sequential is slower but more predictable and resource-friendly
- **Interview Tip**: Explain that show the difference between sequential and parallel execution

---

## 48) How do you handle progress updates in long-running async operations?

Emit progress events through callbacks or custom event systems during async work.

```js
const process = async (items, onProgress) => {
  for (let i = 0; i < items.length; i++) {
    await work(items[i]);
    onProgress((i + 1) / items.length);
  }
};
```

- **Core Approach**: Provide progress feedback for long-running operations
- **Real-World Use**: File uploads, data processing, batch operations
- **Common Mistake**: Not debouncing progress updates
- **Advanced Feature**: Use Web Workers for CPU-intensive tasks
- **Interview Tip**: Explain that show how to implement progress callbacks

---

## 49) What is `Promise.finally()` used for?

`Promise.finally()` runs cleanup code regardless of whether the promise fulfills or rejects.

```js
let loading = true;
fetch('/data')
  .then(handleData)
  .catch(handleError)
  .finally(() => { loading = false; });
```

- **Core Purpose**: `finally()` runs cleanup code regardless of success or failure
- **Real-World Use**: Hide loading spinners, close connections, reset state
- **Common Mistake**: Expecting `finally()` to receive or pass values
- **Advanced Feature**: `finally()` runs after all `then`/`catch` handlers
- **Interview Tip**: Explain that show cleanup patterns with `finally()`

---

## 50) Can you mix Promises and async/await syntax safely?

Yes, they're fully compatible. `await` works with any thenable, and async functions return promises.

```js
async function mixed() {
  const p = Promise.resolve(1);
  const a = await p;
  return p.then(x => x + 1);
}
```

- **Core Compatibility**: `await` works with any promise-like object (thenable)
- **Real-World Use**: Migrating from callbacks to promises, mixing old and new code
- **Common Mistake**: Inconsistent mixing without understanding compatibility
- **Advanced Feature**: Both async/await and promises compile to similar code
- **Interview Tip**: Explain that show how they work together seamlessly

---

## 51) How does the fetch Promise work internally in V8?

When V8 encounters a fetch call, it creates a Promise, queues the networking task, and sets up the resolution mechanism through the event loop and microtask queue.

```js
const promise = fetch('/api/data');
promise.then(response => {
  console.log('Response received');
});
```

- **Core Process**: V8 returns a Promise immediately and handles the request asynchronously
- **Real-World Impact**: Understanding how network requests work under the hood
- **Common Mistake**: Thinking fetch blocks until the request completes
- **Advanced Feature**: The actual network work happens in the browser's task queue
- **Interview Tip**: Explain that explain the V8 event loop and microtask processing

---
