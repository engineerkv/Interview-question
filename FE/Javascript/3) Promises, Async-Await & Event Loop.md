# 🔁 3. Promises, Async/Await & Event Loop (Q26–51)

---

## 🧩 Q26. What are Promises in JavaScript?

### 🧠 Concept

A Promise is a placeholder for a future value that can be pending, fulfilled, or rejected. It helps handle async operations cleanly without callback nesting.

---

### 💡 Example

```js
const getData = () => fetch('/api').then(r => r.json());
getData().then(data => console.log(data));
```

---

### 🔍 Deep Insights

* **Rule:** Promises have three states: pending, fulfilled, or rejected.
* **Use Case:** Perfect for API calls, file operations, and async data loading.
* **Common Mistake:** Forgetting to return promises in chains breaks data flow.
* **Pro Tip:** Promise handlers run as microtasks in the event loop.

---

### ⭐ Senior Takeaway

Always mention the three states and error handling when explaining promises.

---

## 🧩 Q27. How do promises differ from callbacks?

### 🧠 Concept

Promises make async code easier to read and handle errors better than callbacks. They avoid callback hell by chaining instead of nesting.

---

### 💡 Example

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

### 🔍 Deep Insights

* **Rule:** Promises chain flatly instead of nesting callbacks.
* **Use Case:** API calls, database operations, and file handling.
* **Common Mistake:** Mixing callbacks and promises in the same code.
* **Pro Tip:** Promises always execute asynchronously via microtasks.

---

### ⭐ Senior Takeaway

Promises solve the pyramid of doom problem with flat, readable chains.

---

## 🧩 Q28. What is promise chaining?

### 🧠 Concept

Promise chaining lets you pass data from one async operation to the next using `.then()` methods. Each step receives the result from the previous one.

---

### 💡 Example

```js
fetch('/user')
  .then(response => response.json())
  .then(user => fetch(`/posts/${user.id}`))
  .then(response => response.json())
  .then(posts => console.log(posts));
```

---

### 🔍 Deep Insights

* **Rule:** Each `.then()` receives the return value from the previous one.
* **Use Case:** Building complex async workflows step by step.
* **Common Mistake:** Forgetting to return values in `.then()` handlers.
* **Pro Tip:** You can return promises or regular values.

---

### ⭐ Senior Takeaway

Show how data flows through the chain when explaining promise chaining.

---

## 🧩 Q29. How do you return values through a promise chain?

### 🧠 Concept

To pass data through a promise chain, return values from each `.then()` handler. The returned value becomes the input for the next `.then()`.

---

### 💡 Example

```js
Promise.resolve(5)
  .then(x => x * 2)
  .then(y => y + 3)
  .then(result => console.log(result)); // 13
```

---

### 🔍 Deep Insights

* **Rule:** Always return something from `.then()` to pass data forward.
* **Use Case:** Transforming data through multiple async steps.
* **Common Mistake:** Forgetting return statements breaks the chain.
* **Pro Tip:** Return promises for async operations, values for sync.

---

### ⭐ Senior Takeaway

Demonstrate with a simple math example to show data flow.

---

## 🧩 Q30. How do you handle errors in a promise chain?

### 🧠 Concept

Use `.catch()` to handle errors in promise chains. It catches both thrown errors and rejected promises, allowing you to recover or handle failures gracefully.

---

### 💡 Example

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

### 🔍 Deep Insights

* **Rule:** `.catch()` handles any error in the chain above it.
* **Use Case:** API error handling, fallback data, user notifications.
* **Common Mistake:** Swallowing errors without proper handling.
* **Pro Tip:** You can recover from errors and continue the chain.

---

### ⭐ Senior Takeaway

Show error handling with a real API example to demonstrate practical use.

---

## 🧩 Q31. What happens if you return a promise inside `.then()`?

### 🧠 Concept

When you return a promise inside `.then()`, the outer promise waits for the inner one to complete. This enables chaining dependent async operations.

---

### 💡 Example

```js
Promise.resolve(5)
  .then(id => fetch(`/user/${id}`))
  .then(response => response.json())
  .then(user => console.log(user.name));
```

---

### 🔍 Deep Insights

* **Rule:** Returning a promise makes the chain wait for it.
* **Use Case:** Chaining dependent API calls and database operations.
* **Common Mistake:** Nesting `.then()` instead of returning promises.
* **Pro Tip:** Errors in inner promises bubble up to outer chains.

---

### ⭐ Senior Takeaway

This enables clean async workflows without nested callbacks.

---

## 🧩 Q32. What happens if you forget to `return` inside `.then()`?

### 🧠 Concept

If you forget to return from `.then()`, the next `.then()` gets `undefined` instead of your data. This breaks the data flow in the chain.

---

### 💡 Example

```js
Promise.resolve(5)
  .then(x => { x * 2; }) // Missing return!
  .then(result => console.log(result)); // undefined
```

---

### 🔍 Deep Insights

* **Rule:** Always return something from `.then()` handlers.
* **Use Case:** This mistake breaks data flow in async chains.
* **Common Mistake:** Forgetting return statements is very common.
* **Pro Tip:** Use arrow functions with implicit returns when possible.

---

### ⭐ Senior Takeaway

Show the difference between with and without return to highlight the issue.

---

## 🧩 Q33. How does promise resolution work internally?

### 🧠 Concept

Promises use the microtask queue to run handlers after the current code finishes, not immediately. This ensures predictable async behavior.

---

### 💡 Example

```js
console.log('First');
Promise.resolve().then(() => console.log('Second'));
console.log('Third');
// Output: First, Third, Second
```

---

### 🔍 Deep Insights

* **Rule:** Promise handlers always run after the current code stack.
* **Use Case:** This ensures predictable async behavior.
* **Common Mistake:** Expecting promises to run immediately.
* **Pro Tip:** Microtasks run before the next macrotask.

---

### ⭐ Senior Takeaway

Explain the event loop order: stack → microtasks → macrotasks.

---

## 🧩 Q34. What is the difference between `Promise.resolve()` and `new Promise()`?

### 🧠 Concept

`Promise.resolve()` creates a resolved promise immediately, while `new Promise()` lets you control when it resolves. Use the first for values, the second for async work.

---

### 💡 Example

```js
const p1 = Promise.resolve(42); // Immediate resolution
const p2 = new Promise(resolve => {
  setTimeout(() => resolve(42), 1000);
}); // Manual control
```

---

### 🔍 Deep Insights

* **Rule:** Use `Promise.resolve()` for values, `new Promise()` for async work.
* **Use Case:** Wrapping old callback APIs into promises.
* **Common Mistake:** Using `new Promise()` when `Promise.resolve()` would work.
* **Pro Tip:** Avoid the `new Promise(async ...)` anti-pattern.

---

### ⭐ Senior Takeaway

Show when to use each approach based on your needs.

---

## 🧩 Q35. How do you avoid callback hell using Promises?

### 🧠 Concept

Avoid callback hell by chaining promises instead of nesting callbacks. Keep each step simple and readable.

---

### 💡 Example

```js
getUser(id)
  .then(user => getPosts(user.id))
  .then(posts => getComments(posts[0].id))
  .then(comments => console.log(comments));
```

---

### 🔍 Deep Insights

* **Rule:** Chain promises instead of nesting callbacks.
* **Use Case:** API workflows, database operations, file processing.
* **Common Mistake:** Mixing callbacks and promises in the same code.
* **Pro Tip:** Use `Promise.all()` for parallel operations.

---

### ⭐ Senior Takeaway

Show the before/after of callback hell to demonstrate improvement.

---

## 🧩 Q36. How does `async/await` work under the hood?

### 🧠 Concept

`async/await` makes promises easier to read by letting you write async code that looks like regular code. It's syntactic sugar over promises.

---

### 💡 Example

```js
async function getUserData(id) {
  const response = await fetch(`/user/${id}`);
  const user = await response.json();
  return user;
}
```

---

### 🔍 Deep Insights

* **Rule:** `async` functions always return promises, `await` pauses execution.
* **Use Case:** API calls, database operations, file handling.
* **Common Mistake:** Forgetting `await` keyword.
* **Pro Tip:** `async/await` is just syntactic sugar over promises.

---

### ⭐ Senior Takeaway

Show how it makes code more readable than promise chains.

---

## 🧩 Q37. What happens if you don't `await` an async function?

### 🧠 Concept

If you call an async function without `await`, you get a promise object instead of the actual result. This causes bugs where you expect data but get promises.

---

### 💡 Example

```js
async function getData() {
  const response = await fetch('/api');
  return response.json();
}

const promise = getData(); // Without await - returns a promise
const data = await getData(); // With await - returns the actual data
```

---

### 🔍 Deep Insights

* **Rule:** Always use `await` when you need the result, not the promise.
* **Use Case:** This mistake causes bugs where you expect data but get promises.
* **Common Mistake:** Forgetting `await` is the #1 async/await mistake.
* **Pro Tip:** You can return promises from async functions for chaining.

---

### ⭐ Senior Takeaway

Show the difference between with and without `await` to highlight the issue.

---

## 🧩 Q38. What is the difference between microtasks and macrotasks?

### 🧠 Concept

Microtasks (promises, queueMicrotask) run before the next macrotask (setTimeout, I/O) at microtask checkpoints. This ensures promises execute before timers.

---

### 💡 Example

```js
setTimeout(() => console.log('macro'));
Promise.resolve().then(() => console.log('micro'));
// micro logs before macro
```

---

### 🔍 Deep Insights

* **Rule:** Microtasks run before macrotasks in the event loop.
* **Use Case:** Promise handlers, queueMicrotask, async/await.
* **Common Mistake:** Expecting setTimeout to run before promises.
* **Pro Tip:** Overusing microtasks can starve rendering.

---

### ⭐ Senior Takeaway

Explain the event loop order: stack → microtasks → macrotasks.

---

## 🧩 Q39. How does the event loop handle Promises and async/await?

### 🧠 Concept

Promise handlers run as microtasks. `await` schedules continuation as a microtask after the current turn, which is how async/await works under the hood.

---

### 💡 Example

```js
(async () => {
  console.log('A');
  await 0;
  console.log('B');
})();
// A then B
```

---

### 🔍 Deep Insights

* **Rule:** `await` pauses execution and schedules continuation as a microtask.
* **Use Case:** This is how async/await works under the hood.
* **Common Mistake:** Not understanding that `await` doesn't block the thread.
* **Pro Tip:** Continuations run after other microtasks queued earlier.

---

### ⭐ Senior Takeaway

Explain how `await` transforms functions into microtasks.

---

## 🧩 Q40. How do you handle multiple promises concurrently?

### 🧠 Concept

Use combinators to run tasks together and aggregate results or outcomes. Start all promises before awaiting to run them in parallel.

---

### 💡 Example

```js
const a = fetch('/a');
const b = fetch('/b');
const [ra, rb] = await Promise.all([a, b]);
```

---

### 🔍 Deep Insights

* **Rule:** Start all promises before awaiting to run them in parallel.
* **Use Case:** Loading multiple API endpoints, database queries.
* **Common Mistake:** Awaiting promises one by one instead of in parallel.
* **Pro Tip:** Use `Promise.all()`, `allSettled()`, `race()`, or `any()` for different needs.

---

### ⭐ Senior Takeaway

Show the difference between sequential and parallel execution.

---

## 🧩 Q41. What is `Promise.all()` and when should you use it?

### 🧠 Concept

`Promise.all()` waits for all promises to fulfill or fails fast on first rejection. Use it when you need all results or want to fail quickly.

---

### 💡 Example

```js
const [user, posts] = await Promise.all([
  fetch('/user').then(r => r.json()),
  fetch('/posts').then(r => r.json())
]);
```

---

### 🔍 Deep Insights

* **Rule:** `Promise.all()` waits for all promises or fails fast on first rejection.
* **Use Case:** Loading user data and posts together, multiple API calls.
* **Common Mistake:** Using it when some promises might fail.
* **Pro Tip:** Results array matches input order, not completion order.

---

### ⭐ Senior Takeaway

Show when to use `all()` vs `allSettled()` vs `race()`.

---

## 🧩 Q42. What is `Promise.allSettled()`?

### 🧠 Concept

`Promise.allSettled()` waits for all promises to complete regardless of success/failure. It never rejects and always returns results with status.

---

### 💡 Example

```js
const results = await Promise.allSettled([
  fetch('/a'), fetch('/b'), fetch('/c')
]);
const successes = results.filter(r => r.status === 'fulfilled');
```

---

### 🔍 Deep Insights

* **Rule:** `allSettled()` never rejects, always returns results with status.
* **Use Case:** Batch operations where some might fail, retry logic.
* **Common Mistake:** Using `all()` when you need partial success.
* **Pro Tip:** Each result has `status` and `value`/`reason` properties.

---

### ⭐ Senior Takeaway

Show how to filter successful vs failed results.

---

## 🧩 Q43. What is `Promise.any()` and how is it different from `Promise.race()`?

### 🧠 Concept

`Promise.any()` resolves with first successful promise. `race()` resolves with first to settle (success or failure). Use `any()` for failover, `race()` for timeouts.

---

### 💡 Example

```js
const fast = await Promise.any([
  slowApi(), fastApi(), backupApi()
]);
// vs race: first to complete (even if error)
```

---

### 🔍 Deep Insights

* **Rule:** `any()` waits for first success, `race()` takes first completion.
* **Use Case:** `any()` for failover, `race()` for timeouts.
* **Common Mistake:** Using `race()` when you need success only.
* **Pro Tip:** `any()` ignores rejections until all promises fail.

---

### ⭐ Senior Takeaway

Show the difference with real examples to clarify use cases.

---

## 🧩 Q44. What is `Promise.race()`?

### 🧠 Concept

`Promise.race()` resolves with the first promise to settle (fulfill or reject). Use it for timeouts, cancellation, or first-available service patterns.

---

### 💡 Example

```js
const timeout = new Promise((_, reject) => 
  setTimeout(() => reject(new Error('timeout')), 5000)
);
const data = await Promise.race([fetch('/data'), timeout]);
```

---

### 🔍 Deep Insights

* **Rule:** `race()` returns the first promise to complete (success or failure).
* **Use Case:** Timeouts, cancellation, first-available service.
* **Common Mistake:** Expecting only successful results from `race()`.
* **Pro Tip:** Other promises continue running in the background.

---

### ⭐ Senior Takeaway

Show timeout pattern with `race()` to demonstrate practical use.

---

## 🧩 Q45. How do you implement retry logic using Promises?

### 🧠 Concept

Wrap async operations in retry loops with exponential backoff and max attempts. This improves reliability for transient failures.

---

### 💡 Example

```js
const retry = (fn, max = 3) => 
  fn().catch(err => max > 0 ? retry(fn, max - 1) : Promise.reject(err));
```

---

### 🔍 Deep Insights

* **Rule:** Retry with exponential backoff to avoid overwhelming services.
* **Use Case:** API calls, network requests, database operations.
* **Common Mistake:** Retrying too aggressively without backoff.
* **Pro Tip:** Use jitter to distribute retry timing across clients.

---

### ⭐ Senior Takeaway

Show how to implement retry with max attempts and backoff.

---

## 🧩 Q46. How do you cancel a Promise in JavaScript?

### 🧠 Concept

Use `AbortController` for fetch requests or custom cancellation tokens for other async work. Cancellation is cooperative, not preemptive.

---

### 💡 Example

```js
const controller = new AbortController();
fetch('/data', { signal: controller.signal });
controller.abort(); // cancels request
```

---

### 🔍 Deep Insights

* **Rule:** Use `AbortController` for cancelling fetch requests.
* **Use Case:** User navigation, timeout handling, cleanup.
* **Common Mistake:** Not cleaning up cancelled requests.
* **Pro Tip:** Cancellation is cooperative, not preemptive.

---

### ⭐ Senior Takeaway

Show how to implement custom cancellation tokens for other async work.

---

## 🧩 Q47. How do you sequentially execute multiple promises?

### 🧠 Concept

Use `for...of` loops or `reduce()` to await promises one at a time instead of parallel execution. Use this when order matters or resources are limited.

---

### 💡 Example

```js
const results = [];
for (const url of urls) {
  const data = await fetch(url).then(r => r.json());
  results.push(data);
}
```

---

### 🔍 Deep Insights

* **Rule:** Use sequential execution when order matters or resources are limited.
* **Use Case:** Database operations, file processing, API rate limits.
* **Common Mistake:** Using parallel when sequential is needed.
* **Pro Tip:** Sequential is slower but more predictable and resource-friendly.

---

### ⭐ Senior Takeaway

Show the difference between sequential and parallel execution.

---

## 🧩 Q48. How do you handle progress updates in long-running async operations?

### 🧠 Concept

Emit progress events through callbacks or custom event systems during async work. This provides feedback for long-running operations.

---

### 💡 Example

```js
const process = async (items, onProgress) => {
  for (let i = 0; i < items.length; i++) {
    await work(items[i]);
    onProgress((i + 1) / items.length);
  }
};
```

---

### 🔍 Deep Insights

* **Rule:** Provide progress feedback for long-running operations.
* **Use Case:** File uploads, data processing, batch operations.
* **Common Mistake:** Not debouncing progress updates.
* **Pro Tip:** Use Web Workers for CPU-intensive tasks.

---

### ⭐ Senior Takeaway

Show how to implement progress callbacks for better UX.

---

## 🧩 Q49. What is `Promise.finally()` used for?

### 🧠 Concept

`Promise.finally()` runs cleanup code regardless of whether the promise fulfills or rejects. Use it for hide loading spinners, close connections, or reset state.

---

### 💡 Example

```js
let loading = true;
fetch('/data')
  .then(handleData)
  .catch(handleError)
  .finally(() => { loading = false; });
```

---

### 🔍 Deep Insights

* **Rule:** `finally()` runs cleanup code regardless of success or failure.
* **Use Case:** Hide loading spinners, close connections, reset state.
* **Common Mistake:** Expecting `finally()` to receive or pass values.
* **Pro Tip:** `finally()` runs after all `then`/`catch` handlers.

---

### ⭐ Senior Takeaway

Show cleanup patterns with `finally()` to demonstrate practical use.

---

## 🧩 Q50. Can you mix Promises and async/await syntax safely?

### 🧠 Concept

Yes, they're fully compatible. `await` works with any thenable, and async functions return promises, so you can mix them seamlessly.

---

### 💡 Example

```js
async function mixed() {
  const p = Promise.resolve(1);
  const a = await p;
  return p.then(x => x + 1);
}
```

---

### 🔍 Deep Insights

* **Rule:** `await` works with any promise-like object (thenable).
* **Use Case:** Migrating from callbacks to promises, mixing old and new code.
* **Common Mistake:** Inconsistent mixing without understanding compatibility.
* **Pro Tip:** Both async/await and promises compile to similar code.

---

### ⭐ Senior Takeaway

Show how they work together seamlessly in real code.

---

## 🧩 Q51. How does the fetch Promise work internally in V8?

### 🧠 Concept

When V8 encounters a fetch call, it creates a Promise, queues the networking task, and sets up the resolution mechanism through the event loop and microtask queue.

---

### 💡 Example

```js
const promise = fetch('/api/data');
promise.then(response => {
  console.log('Response received');
});
```

---

### 🔍 Deep Insights

* **Rule:** V8 returns a Promise immediately and handles the request asynchronously.
* **Use Case:** Understanding how network requests work under the hood.
* **Common Mistake:** Thinking fetch blocks until the request completes.
* **Pro Tip:** The actual network work happens in the browser's task queue.

---

### ⭐ Senior Takeaway

Explain the V8 event loop and microtask processing for fetch.

---
