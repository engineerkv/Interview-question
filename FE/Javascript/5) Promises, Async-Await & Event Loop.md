<div align="center">

**[← Previous: ES6+ Features](4%29%20ES6%2B%20Features.md)** | **[Next: Web Workers, Service Workers & Real-World Topics →](6%29%20Web%20Workers%2C%20Service%20Workers%20%26%20Real-World%20Topics.md)**

</div>

# 🔄 5. Promises, Async/Await & Event Loop (Q55–80)

---

## Q55. ⚡ Promises in JavaScript

A Promise is a placeholder for a future value that can be pending, fulfilled, or rejected - it helps handle async operations cleanly without callback nesting. Promises have three states: pending (initial state), fulfilled (success), or rejected (failure) - once settled, they can't change state. Perfect for API calls, file operations, and async data loading.

- **Trade-offs**: Promise handlers run as microtasks in the event loop - they execute after the current code but before the next macrotask, which ensures predictable execution order, but too many microtasks can starve the browser's rendering and make the UI feel unresponsive.

Example:

```js
const getData = () => fetch('/api').then(r => r.json());
getData().then(data => console.log(data));

```

---

## Q56. ⚡ Callbacks vs Promises

Callbacks are functions passed as arguments to other functions that get executed when an async operation completes - they're the traditional way to handle async code in JavaScript. Promises are objects representing the eventual completion or failure of an async operation - they provide a cleaner way to handle async code with better error handling and avoid callback hell.

- **Trade-offs**: Callbacks are simple and work everywhere, but they lead to deeply nested code (callback hell) and inconsistent error handling. Promises chain flatly instead of nesting, provide centralized error handling with `.catch()`, and always execute asynchronously via microtasks. The catch is promises always execute asynchronously via microtasks, which can be confusing if you expect immediate execution. Mixing callbacks and promises in the same code can lead to inconsistent patterns - stick to one approach.

Example:

```js
// Callback style (nested, error-prone)
getData((err, data) => {
  if (err) return handleError(err);
  processData(data, (err, result) => {
    if (err) return handleError(err);
    saveData(result, (err) => {
      if (err) return handleError(err);
      console.log('done');
    });
  });
});

// Promise style (flat, better error handling)
getData()
  .then(processData)
  .then(saveData)
  .then(() => console.log('done'))
  .catch(handleError);

```

---

## Q57. ⚡ Chaining Promises

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

## Q58. ⚡ Async/await: what it is and how it works

`async/await` is syntactic sugar on top of promises that lets you write asynchronous steps in a top-to-bottom style. Marking a function as `async` makes it return a promise automatically, and every `await` pauses the function until the awaited promise settles, then resumes with the resolved value (or throws if it rejected).

- **Trade-offs**: `await` does not block the thread—it schedules the rest of the function as a microtask. Forgetting to use `await` is the most common mistake; you end up passing raw promises around. Mix async/await for sequential flows and fall back to promise combinators when you truly need parallelism.

Example:

```js
async function getUserData(id) {
  const response = await fetch(`/user/${id}`);
  const user = await response.json();
  return user;
}

```

---

## Q59. ⚡ `Promise.resolve()` vs `new Promise()`

Use `Promise.resolve(value)` when you already have the value (or a thenable) and just want a settled promise. Use `new Promise((resolve, reject) => { ... })` when you need to wrap callback-based APIs or control when the promise settles by calling `resolve`/`reject` yourself.

- **Trade-offs**: `Promise.resolve()` is eager and great for normalizing values, but it can’t express asynchronous work. Building new promises unnecessarily (`new Promise(async () => {})`) adds complexity and hides errors; only construct a new promise when you truly need manual control.

Example:

```js
const immediate = Promise.resolve(42); // already settled
const delayed = new Promise(resolve => {
  setTimeout(() => resolve(42), 1000);
}); // manual settlement

```

---

## Q60. ⚡ Handling errors in Promises

Attach `.catch()` to the end (or anywhere in the chain) to catch both thrown errors and rejected promises. You can recover by returning a fallback value or rethrow to propagate the failure further down the chain.

- **Trade-offs**: Swallowing errors without logging hides bugs; always surface unexpected failures. Each `.catch()` only sees errors from the handlers above it, so place it where it makes sense or keep a final catch at the end of the chain for last-resort handling.

Example:

```js
fetch('/api/data')
  .then(r => {
    if (!r.ok) throw new Error('Failed');
    return r.json();
  })
  .catch(err => ({ error: true, message: err.message }))
  .then(console.log);

```

---

## Q61. ❓ Callback hell: what it is and how to avoid it

“Callback hell” is the messy pyramid created when you nest callbacks for every async step (`doA(() => doB(() => doC(...)))`). Control flow and error handling become unreadable. Flatten the code by returning promises, using async/await, or breaking the work into named functions.

- **Trade-offs**: Promises/async make dependency chains clearer, but you still need to think about sequencing vs parallelism. If you must stick with callbacks, use named functions or helper utilities to keep indentation shallow and errors centralized.

Example:

```js
// Callback hell
getUser(id, user => {
  getPosts(user.id, posts => {
    save(posts, () => console.log('done'));
  });
});

// Promise chain
getUser(id)
  .then(user => getPosts(user.id))
  .then(save)
  .then(() => console.log('done'));

```

---

## Q62. 🔄 Event Loop in JavaScript

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

## Q63. 🤔 Microtasks vs macrotasks

Microtasks (promises, queueMicrotask) run before the next macrotask (setTimeout, I/O) at microtask checkpoints - this ensures promises execute before timers. The event loop processes all microtasks before moving to the next macrotask.

- **Trade-offs**: The catch is overusing microtasks can starve rendering and make the UI feel unresponsive - use them wisely. Expecting `setTimeout` to run before promises is a common mistake because microtasks always run first.

Example:

```js
setTimeout(() => console.log('macro'));
Promise.resolve().then(() => console.log('micro'));
// micro logs before macro

```

---

## Q64. ⚡ Running Promises concurrently

Start all asynchronous tasks first, then `await` them together so work happens in parallel. Fire the operations, keep the promises, and combine them with helpers like `Promise.all`, `allSettled`, `race`, or `any` depending on how you want to aggregate the outcomes.

- **Trade-offs**: Awaiting each promise in a loop forces sequential execution and wastes time. Running too many tasks in parallel can hammer APIs or exhaust resources, so use pools or batching when needed.

Example:

```js
const userPromise = fetch('/user');
const postsPromise = fetch('/posts');
const [user, posts] = await Promise.all([
  userPromise.then(r => r.json()),
  postsPromise.then(r => r.json())
]);

```

---

## Q65. ⚡ `Promise.all()`: what it is and when to use it

`Promise.all(iterable)` waits for every promise to fulfill and resolves with an array of results in the same order as the inputs. If any promise rejects, the whole thing rejects immediately with that reason—perfect when you need every result or want to fail fast.

- **Trade-offs**: Because it fails fast, partial successes are lost; use `Promise.allSettled()` if you need to inspect successes and failures together. Long-running promises hold up the group, so consider breaking large batches into chunks.

Example:

```js
const [user, posts] = await Promise.all([
  fetch('/user').then(r => r.json()),
  fetch('/posts').then(r => r.json())
]);

```

---

## Q66. ⚡ `Promise.race()`: what it is and when to use it

`Promise.race(iterable)` settles as soon as the first promise settles (fulfills or rejects) and adopts that outcome. Use it for implementing timeouts, picking the fastest mirror, or reacting to whichever async task finishes first.

- **Trade-offs**: The other promises keep running even after the race finishes, so cancel them manually if they do expensive work. Because rejections also win, don't expect `race()` to return only successes—use `Promise.any()` if you want the first fulfillment instead.

Example:

```js
const timeout = new Promise((_, reject) =>
  setTimeout(() => reject(new Error('timeout')), 5000)
);
const result = await Promise.race([fetch('/data'), timeout]);

```

---

## Q67. ⚡ `Promise.allSettled()`: what it is and when to use it

`Promise.allSettled(iterable)` waits for every promise to settle (fulfilled or rejected) and always resolves with an array of result objects `{ status, value | reason }`. It never rejects, so you can inspect successes and failures together.

- **Trade-offs**: Because it waits for every promise, slow or hung operations delay the result. You have to filter the array yourself to separate successes from failures, but the extra bookkeeping is worth it when you need a full report.

Example:

```js
const results = await Promise.allSettled([
  fetch('/a'),
  fetch('/b'),
  fetch('/c')
]);
const successes = results.filter(r => r.status === 'fulfilled');

```

---

## Q68. ⚡ `Promise.any()`: what it is and when to use it

`Promise.any(iterable)` resolves with the first fulfilled promise and ignores rejections until every promise fails. It’s ideal for failover scenarios—race multiple services and take the first successful response.

- **Trade-offs**: If every promise rejects, `any()` rejects with an `AggregateError` containing all reasons, so handle that case explicitly. Because rejections are ignored until the end, bugs may hide unless you log failures as they happen.

Example:

```js
const fastest = await Promise.any([
  fetchFromPrimary(),
  fetchFromReplica(),
  fetchFromCache()
]);

```

---

## Q69. ⚡ Implementing retry logic with Promises

Wrap your async function in a helper that retries on failure with exponential backoff and a max-attempts guard. Each retry simply calls the original function again; if it still fails after the allowed attempts, rethrow the last error.

- **Trade-offs**: Retrying too aggressively can amplify outages—always back off (add jitter) and stop after a reasonable number of attempts. Some errors (like 4xx responses) aren’t recoverable, so inspect the error before retrying blindly.

Example:

```js
const retry = async (fn, attempts = 3, delay = 200) => {
  try {
    return await fn();
  } catch (err) {
    if (attempts <= 1) throw err;
    await new Promise(r => setTimeout(r, delay));
    return retry(fn, attempts - 1, delay * 2);
  }
};

```

---

## Q70. ⚡ Promise cancellation: what it is and how to implement it

Promises themselves can’t be forcefully stopped, so cancellation is cooperative. For browser `fetch`, use `AbortController`; for custom async work, pass a token or signal that code checks periodically and bails out if cancellation was requested.

- **Trade-offs**: Forgetting to cancel leaves requests running and leaks resources. Because cancellation is opt-in, ensure every long-running operation observes the signal (e.g., check `signal.aborted` before heavy work).

Example:

```js
const controller = new AbortController();
const request = fetch('/data', { signal: controller.signal });
controller.abort(); // later, cancel the fetch
await request.catch(err => {
  if (err.name !== 'AbortError') throw err;
});

```

---

## Q71. ⚡ Running Promises sequentially

When order matters (or you must respect rate limits), await promises one by one using `for...of`, `reduce`, or recursion. Each loop iteration waits for the previous promise to finish before starting the next.

- **Trade-offs**: Sequential execution is slower because tasks can’t overlap, but it protects shared resources and keeps APIs happy. Consider worker pools if you need a compromise between pure sequential and fully parallel.

Example:

```js
const results = [];
for (const url of urls) {
  const data = await fetch(url).then(r => r.json());
  results.push(data);
}

```

---

## Q72. ⚡ Implementing progress updates with Promises

Promises don’t emit intermediate values, so expose progress via callbacks, events, or `Observable`-like wrappers. Call the progress handler after each step so the UI can display completion percentage or spinner updates.

- **Trade-offs**: Spamming progress updates can thrash the UI; throttle or debounce updates for large loops. Remember to report both success and failure so the UI can stop showing “loading” states.

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

## Q73. ⚡ `Promise.finally()`: what it is and when to use it

`promise.finally(handler)` runs after a promise settles regardless of whether it fulfilled or rejected—perfect for cleanup tasks like hiding loaders or releasing resources. It passes through the original result/rejection unchanged.

- **Trade-offs**: `finally` doesn’t get the resolved value or error (and can’t modify them), so use `then`/`catch` for data work. If the `finally` handler throws, it overrides the original outcome, so keep cleanup code small and safe.

Example:

```js
let loading = true;
fetch('/data')
  .then(handleData)
  .catch(handleError)
  .finally(() => { loading = false; });

```

---

## Q74. ⚡ Promise vs async/await: differences and mixing them

Promises are the underlying primitive; `async/await` is syntax that builds on them. Async functions always return promises, and `await` simply waits for another promise—so you can freely mix chains and `await` inside the same flow.

- **Trade-offs**: Async/await shines for sequential logic, but promise combinators (`all`, `race`, etc.) remain better for parallel orchestration. Mixing styles without understanding them can be confusing; keep a consistent style per module and only drop to raw promises when you need finer control.

Example:

```js
async function example() {
  const value = await fetchData();
  return Promise.resolve(value).then(process);
}

```

---

## Q75. ⚡ Handling multiple async operations

Mix strategies: kick off independent work in parallel with `Promise.all`, but limit fan-out by building a simple worker pool when APIs have rate limits. Decide per task whether it can run concurrently or must await a previous result, then compose the two styles.

- **Trade-offs**: Pure parallelism can overload databases or hit API quotas, while strict sequencing wastes time. A concurrency limiter (e.g., process N tasks at a time) balances throughput and safety but adds complexity.

Example:

```js
const pool = async (items, limit, worker) => {
  const queue = [...items];
  const run = async () => {
    while (queue.length) await worker(queue.shift());
  };
  await Promise.all(Array.from({ length: limit }, run));
};
await pool(urls, 3, async url => { await fetch(url); });

```

---

## Q76. ⚡ Promise vs Observable

Promises represent a single eventual value; Observables (RxJS, etc.) emit zero-to-many values over time and can be cancelled by unsubscribing. Observables support operators like `map`, `filter`, `merge`, and `retry`, giving you reactive streams rather than one-shot results.

- **Trade-offs**: Promises are built-in and simpler for single async operations, while Observables add a larger API but excel at user-input streams, websockets, or repeated events. Don’t use a Promise when you need multiple emissions—wrap in an Observable instead.

Example:

```js
import { fromEvent } from 'rxjs';

const clicks$ = fromEvent(button, 'click'); // many values
clicks$.subscribe(event => console.log(event));

// Promise is single-shot
const once = fetch('/data').then(res => res.json());

```

---

## Q77. ⚡ Implementing timeout with Promises

Wrap the original promise in a `Promise.race` with a timeout promise that rejects after N milliseconds. If the timeout fires first you can abort the underlying request (via `AbortController`) or just handle the rejection.

- **Trade-offs**: Racing alone doesn’t stop the original operation—remember to cancel or ignore it. Pick timeout values carefully; too aggressive and you’ll kill legitimate slow operations, too lax and you aren’t protecting users.

Example:

```js
const withTimeout = (promise, ms) => {
  const timeout = new Promise((_, reject) =>
    setTimeout(() => reject(new Error('Timed out')), ms)
  );
  return Promise.race([promise, timeout]);
};

await withTimeout(fetch('/data'), 3000);

```

---

## Q78. ⚡ Promise vs Generator

Promises represent eventual values and run to completion automatically. Generators (`function*`) produce a sequence of values and pause/resume on `yield`, which is why libraries like `co` can drive generators with promises to mimic async/await behavior.

- **Trade-offs**: Generators require an external runner to drive them and are great for custom async control flows or infinite sequences. Promises are simpler for everyday async tasks but can’t yield multiple values. Use generators when you need pull-based iteration; stick to promises/async when you just need one result.

Example:

```js
function* ids() {
  let id = 0;
  while (true) yield id++;
}

const iterator = ids();
iterator.next().value; // 0
iterator.next().value; // 1

```

---

## Q79. ⚡ How fetch Promise works internally in V8

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

## Q80. ⚡ Promise chaining and error propagation

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

**[← Previous: ES6+ Features](4%29%20ES6%2B%20Features.md)** | **[Next: Web Workers, Service Workers & Real-World Topics →](6%29%20Web%20Workers%2C%20Service%20Workers%20%26%20Real-World%20Topics.md)**

</div>
