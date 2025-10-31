# 🔁 3. Promises, Async/Await & Event Loop (Q21–46)

---

## 21) What are Promises in JavaScript?

Concept:
A Promise is a placeholder for a future value that can be pending, fulfilled, or rejected. It helps handle async operations cleanly.

Example:
```js
const getData = () => fetch('/api').then(r => r.json());
getData().then(data => console.log(data));
```

Deep Insight:
- **Core rule:** Promises have three states: pending, fulfilled, or rejected
- **Real-world use:** Perfect for API calls, file operations, and async data loading
- **Common mistake:** Forgetting to return promises in chains
- **Advanced point:** Promise handlers run as microtasks in the event loop
- **Interview tip:** Always mention the three states and error handling

---

## 22) How do promises differ from callbacks?

Concept:
Promises make async code easier to read and handle errors better than callbacks. They avoid callback hell.

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

Deep Insight:
- **Core rule:** Promises chain flatly instead of nesting callbacks
- **Real-world use:** API calls, database operations, and file handling
- **Common mistake:** Mixing callbacks and promises in the same code
- **Advanced point:** Promises always execute asynchronously via microtasks
- **Interview tip:** Show how promises solve the pyramid of doom problem

---

## 23) What is promise chaining?

Concept:
Promise chaining lets you pass data from one async operation to the next using `.then()` methods.

Example:
```js
fetch('/user')
  .then(response => response.json())
  .then(user => fetch(`/posts/${user.id}`))
  .then(response => response.json())
  .then(posts => console.log(posts));
```

Deep Insight:
- **Core rule:** Each `.then()` receives the return value from the previous one
- **Real-world use:** Building complex async workflows step by step
- **Common mistake:** Forgetting to return values in `.then()` handlers
- **Advanced point:** You can return promises or regular values
- **Interview tip:** Show how data flows through the chain

---

## 24) How do you return values through a promise chain?

Concept:
To pass data through a promise chain, return values from each `.then()` handler.

Example:
```js
Promise.resolve(5)
  .then(x => x * 2)
  .then(y => y + 3)
  .then(result => console.log(result)); // 13
```

Deep Insight:
- **Core rule:** Always return something from `.then()` to pass data forward
- **Real-world use:** Transforming data through multiple async steps
- **Common mistake:** Forgetting return statements breaks the chain
- **Advanced point:** Return promises for async operations, values for sync
- **Interview tip:** Demonstrate with a simple math example

---

## 25) How do you handle errors in a promise chain?

Concept:
Use `.catch()` to handle errors in promise chains. It catches both thrown errors and rejected promises.

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

Deep Insight:
- **Core rule:** `.catch()` handles any error in the chain above it
- **Real-world use:** API error handling, fallback data, user notifications
- **Common mistake:** Swallowing errors without proper handling
- **Advanced point:** You can recover from errors and continue the chain
- **Interview tip:** Show error handling with a real API example

---

## 26) What happens if you return a promise inside `.then()`?

Concept:
When you return a promise inside `.then()`, the outer promise waits for the inner one to complete.

Example:
```js
Promise.resolve(5)
  .then(id => fetch(`/user/${id}`))
  .then(response => response.json())
  .then(user => console.log(user.name));
```

Deep Insight:
- **Core rule:** Returning a promise makes the chain wait for it
- **Real-world use:** Chaining dependent API calls and database operations
- **Common mistake:** Nesting `.then()` instead of returning promises
- **Advanced point:** Errors in inner promises bubble up to outer chains
- **Interview tip:** Show how this enables clean async workflows

---

## 27) What happens if you forget to `return` inside `.then()`?

Concept:
If you forget to return from `.then()`, the next `.then()` gets `undefined` instead of your data.

Example:
```js
Promise.resolve(5)
  .then(x => { x * 2; }) // Missing return!
  .then(result => console.log(result)); // undefined
```

Deep Insight:
- **Core rule:** Always return something from `.then()` handlers
- **Real-world use:** This mistake breaks data flow in async chains
- **Common mistake:** Forgetting return statements is very common
- **Advanced point:** Use arrow functions with implicit returns when possible
- **Interview tip:** Show the difference between with and without return

---

## 28) How does promise resolution work internally?

Concept:
Promises use the microtask queue to run handlers after the current code finishes, not immediately.

Example:
```js
console.log('First');
Promise.resolve().then(() => console.log('Second'));
console.log('Third');
// Output: First, Third, Second
```

Deep Insight:
- **Core rule:** Promise handlers always run after the current code stack
- **Real-world use:** This ensures predictable async behavior
- **Common mistake:** Expecting promises to run immediately
- **Advanced point:** Microtasks run before the next macrotask
- **Interview tip:** Explain the event loop order: stack → microtasks → macrotasks

---

## 29) What is the difference between `Promise.resolve()` and `new Promise()`?

Concept:
`Promise.resolve()` creates a resolved promise immediately, while `new Promise()` lets you control when it resolves.

Example:
```js
// Immediate resolution
const p1 = Promise.resolve(42);

// Manual control
const p2 = new Promise(resolve => {
  setTimeout(() => resolve(42), 1000);
});
```

Deep Insight:
- **Core rule:** Use `Promise.resolve()` for values, `new Promise()` for async work
- **Real-world use:** Wrapping old callback APIs into promises
- **Common mistake:** Using `new Promise()` when `Promise.resolve()` would work
- **Advanced point:** Avoid the `new Promise(async ...)` anti-pattern
- **Interview tip:** Show when to use each approach

---

## 30) How do you avoid callback hell using Promises?

Concept:
Avoid callback hell by chaining promises instead of nesting callbacks. Keep each step simple.

Example:
```js
// Instead of nested callbacks:
// getUser(id, user => {
//   getPosts(user.id, posts => {
//     getComments(posts[0].id, comments => {
//       // callback hell!
//     });
//   });
// });

// Use promise chaining:
getUser(id)
  .then(user => getPosts(user.id))
  .then(posts => getComments(posts[0].id))
  .then(comments => console.log(comments));
```

Deep Insight:
- **Core rule:** Chain promises instead of nesting callbacks
- **Real-world use:** API workflows, database operations, file processing
- **Common mistake:** Mixing callbacks and promises in the same code
- **Advanced point:** Use `Promise.all()` for parallel operations
- **Interview tip:** Show the before/after of callback hell

---

## 31) How does `async/await` work under the hood?

Concept:
`async/await` makes promises easier to read by letting you write async code that looks like regular code.

Example:
```js
async function getUserData(id) {
  const response = await fetch(`/user/${id}`);
  const user = await response.json();
  return user;
}
```

Deep Insight:
- **Core rule:** `async` functions always return promises, `await` pauses execution
- **Real-world use:** API calls, database operations, file handling
- **Common mistake:** Forgetting `await` keyword
- **Advanced point:** `async/await` is just syntactic sugar over promises
- **Interview tip:** Show how it makes code more readable than promise chains

---

## 32) What happens if you don’t `await` an async function?

Concept:
If you call an async function without `await`, you get a promise object instead of the actual result.

Example:
```js
async function getData() {
  const response = await fetch('/api');
  return response.json();
}

// Without await - returns a promise
const promise = getData();
console.log(promise); // Promise object

// With await - returns the actual data
const data = await getData();
console.log(data); // Actual data
```

Deep Insight:
- **Core rule:** Always use `await` when you need the result, not the promise
- **Real-world use:** This mistake causes bugs where you expect data but get promises
- **Common mistake:** Forgetting `await` is the #1 async/await mistake
- **Advanced point:** You can return promises from async functions for chaining
- **Interview tip:** Show the difference between with and without `await`

---

## 33) What is the difference between microtasks and macrotasks?

Concept:
Microtasks (promises, queueMicrotask) run before the next macrotask (setTimeout, I/O) at microtask checkpoints.

Example:
```js
setTimeout(() => console.log('macro'));
Promise.resolve().then(() => console.log('micro'));
// micro logs before macro
```

Deep Insight:
- **Core rule:** Microtasks run before macrotasks in the event loop
- **Real-world use:** Promise handlers, queueMicrotask, async/await
- **Common mistake:** Expecting setTimeout to run before promises
- **Advanced point:** Overusing microtasks can starve rendering
- **Interview tip:** Explain the event loop order: stack → microtasks → macrotasks

---

## 34) How does the event loop handle Promises and async/await?

Concept:
Promise handlers run as microtasks; `await` schedules continuation as a microtask after the current turn.

Example:
```js
(async () => {
  console.log('A');
  await 0;
  console.log('B');
})();
// A then B
```

Deep Insight:
- **Core rule:** `await` pauses execution and schedules continuation as a microtask
- **Real-world use:** This is how async/await works under the hood
- **Common mistake:** Not understanding that `await` doesn't block the thread
- **Advanced point:** Continuations run after other microtasks queued earlier
- **Interview tip:** Explain how `await` transforms functions into microtasks

---

## 35) How do you handle multiple promises concurrently?

Concept:
Use combinators to run tasks together and aggregate results or outcomes.

Example:
```js
const a = fetch('/a');
const b = fetch('/b');
const [ra, rb] = await Promise.all([a, b]);
```

Deep Insight:
- **Core rule:** Start all promises before awaiting to run them in parallel
- **Real-world use:** Loading multiple API endpoints, database queries
- **Common mistake:** Awaiting promises one by one instead of in parallel
- **Advanced point:** Use `Promise.all()`, `allSettled()`, `race()`, or `any()` for different needs
- **Interview tip:** Show the difference between sequential and parallel execution

---

## 36) What is `Promise.all()` and when should you use it?

Concept:
`Promise.all()` waits for all promises to fulfill or fails fast on first rejection.

Example:
```js
const [user, posts] = await Promise.all([
  fetch('/user').then(r => r.json()),
  fetch('/posts').then(r => r.json())
]);
```

Deep Insight:
- **Core rule:** `Promise.all()` waits for all promises or fails fast on first rejection
- **Real-world use:** Loading user data and posts together, multiple API calls
- **Common mistake:** Using it when some promises might fail
- **Advanced point:** Results array matches input order, not completion order
- **Interview tip:** Show when to use `all()` vs `allSettled()` vs `race()`

---

## 37) What is `Promise.allSettled()`?

Concept:
`Promise.allSettled()` waits for all promises to complete regardless of success/failure.

Example:
```js
const results = await Promise.allSettled([
  fetch('/a'), fetch('/b'), fetch('/c')
]);
const successes = results.filter(r => r.status === 'fulfilled');
```

Deep Insight:
- **Core rule:** `allSettled()` never rejects, always returns results with status
- **Real-world use:** Batch operations where some might fail, retry logic
- **Common mistake:** Using `all()` when you need partial success
- **Advanced point:** Each result has `status` and `value`/`reason` properties
- **Interview tip:** Show how to filter successful vs failed results

---

## 38) What is `Promise.any()` and how is it different from `Promise.race()`?

Concept:
`Promise.any()` resolves with first successful promise; `race()` resolves with first to settle (success or failure).

Example:
```js
const fast = await Promise.any([
  slowApi(), fastApi(), backupApi()
]);
// vs race: first to complete (even if error)
```

Deep Insight:
- **Core rule:** `any()` waits for first success, `race()` takes first completion
- **Real-world use:** `any()` for failover, `race()` for timeouts
- **Common mistake:** Using `race()` when you need success only
- **Advanced point:** `any()` ignores rejections until all promises fail
- **Interview tip:** Show the difference with real examples

---

## 39) What is `Promise.race()`?

Concept:
`Promise.race()` resolves with the first promise to settle (fulfill or reject).

Example:
```js
const timeout = new Promise((_, reject) => 
  setTimeout(() => reject(new Error('timeout')), 5000)
);
const data = await Promise.race([fetch('/data'), timeout]);
```

Deep Insight:
- **Core rule:** `race()` returns the first promise to complete (success or failure)
- **Real-world use:** Timeouts, cancellation, first-available service
- **Common mistake:** Expecting only successful results from `race()`
- **Advanced point:** Other promises continue running in the background
- **Interview tip:** Show timeout pattern with `race()`

---

## 40) How do you implement retry logic using Promises?

Concept:
Wrap async operations in retry loops with exponential backoff and max attempts.

Example:
```js
const retry = (fn, max = 3) => 
  fn().catch(err => max > 0 ? retry(fn, max - 1) : Promise.reject(err));
```

Deep Insight:
- **Core rule:** Retry with exponential backoff to avoid overwhelming services
- **Real-world use:** API calls, network requests, database operations
- **Common mistake:** Retrying too aggressively without backoff
- **Advanced point:** Use jitter to distribute retry timing across clients
- **Interview tip:** Show how to implement retry with max attempts

---

## 41) How do you cancel a Promise in JavaScript?

Concept:
Use `AbortController` for fetch requests or custom cancellation tokens for other async work.

Example:
```js
const controller = new AbortController();
fetch('/data', { signal: controller.signal });
controller.abort(); // cancels request
```

Deep Insight:
- **Core rule:** Use `AbortController` for cancelling fetch requests
- **Real-world use:** User navigation, timeout handling, cleanup
- **Common mistake:** Not cleaning up cancelled requests
- **Advanced point:** Cancellation is cooperative, not preemptive
- **Interview tip:** Show how to implement custom cancellation tokens

---

## 42) How do you sequentially execute multiple promises?

Concept:
Use `for...of` loops or `reduce()` to await promises one at a time instead of parallel execution.

Example:
```js
const results = [];
for (const url of urls) {
  const data = await fetch(url).then(r => r.json());
  results.push(data);
}
```

Deep Insight:
- **Core rule:** Use sequential execution when order matters or resources are limited
- **Real-world use:** Database operations, file processing, API rate limits
- **Common mistake:** Using parallel when sequential is needed
- **Advanced point:** Sequential is slower but more predictable and resource-friendly
- **Interview tip:** Show the difference between sequential and parallel execution

---

## 43) How do you handle progress updates in long-running async operations?

Concept:
Emit progress events through callbacks or custom event systems during async work.

Example:
```js
const process = async (items, onProgress) => {
  for (let i = 0; i < items.length; i++) {
    await work(items[i]);
    onProgress((i + 1) / items.length);
  }
};
```

Deep Insight:
- **Core rule:** Provide progress feedback for long-running operations
- **Real-world use:** File uploads, data processing, batch operations
- **Common mistake:** Not debouncing progress updates
- **Advanced point:** Use Web Workers for CPU-intensive tasks
- **Interview tip:** Show how to implement progress callbacks

---

## 44) What is `Promise.finally()` used for?

Concept:
`Promise.finally()` runs cleanup code regardless of whether the promise fulfills or rejects.

Example:
```js
let loading = true;
fetch('/data')
  .then(handleData)
  .catch(handleError)
  .finally(() => { loading = false; });
```

Deep Insight:
- **Core rule:** `finally()` runs cleanup code regardless of success or failure
- **Real-world use:** Hide loading spinners, close connections, reset state
- **Common mistake:** Expecting `finally()` to receive or pass values
- **Advanced point:** `finally()` runs after all `then`/`catch` handlers
- **Interview tip:** Show cleanup patterns with `finally()`

---

## 45) Can you mix Promises and async/await syntax safely?

Concept:
Yes, they're fully compatible; `await` works with any thenable, and async functions return promises.

Example:
```js
async function mixed() {
  const p = Promise.resolve(1);
  const a = await p;
  return p.then(x => x + 1);
}
```

Deep Insight:
- **Core rule:** `await` works with any promise-like object (thenable)
- **Real-world use:** Migrating from callbacks to promises, mixing old and new code
- **Common mistake:** Inconsistent mixing without understanding compatibility
- **Advanced point:** Both async/await and promises compile to similar code
- **Interview tip:** Show how they work together seamlessly

---

## 46) How does the fetch Promise work internally in V8?

Concept:
When V8 encounters a fetch call, it creates a Promise, queues the networking task, and sets up the resolution mechanism through the event loop and microtask queue.

Example:
```js
// V8's internal processing of fetch Promise
const promise = fetch('/api/data');

// Internally V8 does:
// 1. Creates Promise object with pending state
// 2. Queues networking task in browser's task queue
// 3. Returns Promise immediately to JavaScript
// 4. When response arrives, queues microtask to resolve Promise
// 5. Event loop processes microtask and calls .then() handlers

promise.then(response => {
  // This runs when V8 processes the microtask
  console.log('Response received');
});
```

Deep Insight:
- **Core rule:** V8 returns a Promise immediately and handles the request asynchronously
- **Real-world use:** Understanding how network requests work under the hood
- **Common mistake:** Thinking fetch blocks until the request completes
- **Advanced point:** The actual network work happens in the browser's task queue
- **Interview tip:** Explain the V8 event loop and microtask processing
