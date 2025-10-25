# ⚡ Asynchronous JavaScript — Q66-Q85

---

## 1️⃣ What is the Event Loop?

**🧠 Concept**

The event loop continuously checks if the call stack is empty, and if so, it pushes callbacks from the queue into the stack for execution.

**💻 Example**
```js
console.log("Start");
setTimeout(() => console.log("Timeout"), 0);
Promise.resolve().then(() => console.log("Promise"));
console.log("End");
```

**💬 Explanation + Insight**

- **Event Loop Management** - The event loop manages asynchronous operations in JavaScript
- **Continuous Checking** - It continuously checks if the call stack is empty
- **Queue Processing** - When empty, it moves callbacks from queues to the stack
- **Priority System** - Microtasks (Promises) have higher priority than macrotasks (setTimeout)
- **Debugging Tool** - Understanding the event loop helps debug async code
🕒 Event Loop cycle starts:
1️⃣ Microtask Queue runs  "Promise"
2️⃣ Macrotask Queue runs  "Timeout"

Output:
Start
End
Promise
Timeout
```

**💬 Explanation + Insight**



* JS is **single-threaded**.
* Event loop coordinates **asynchronous execution**.
* Order of execution:
  🧩 **Call Stack  Microtask Queue  Macrotask Queue**

---

## 2️⃣ What are Microtask and Macrotask Queues?

**🧠 Concept**



* **Microtasks**: Promises, queueMicrotask(), MutationObserver.
* **Macrotasks**: setTimeout, setInterval, setImmediate, I/O callbacks.

**💻 Example**

```js
setTimeout(() => console.log("Macrotask"));
Promise.resolve().then(() => console.log("Microtask"));
```

🧠 **Timeline:**

```
Microtasks always run before Macrotasks:
 Output: Microtask  Macrotask
```

**💬 Explanation + Insight**


After every task (from the stack), the event loop **empties all microtasks first** before running the next macrotask.

---

## 3️⃣ What is the Call Stack and how does it interact with the Event Loop?

**🧠 Concept**


The call stack runs synchronous code; async callbacks wait in queues until the stack is empty.

**💻 Example**

```js
function first() { second(); }
function second() { console.log("Second"); }
first();
```

🧠 **Diagram:**

```
Call Stack:
1️⃣ first()
2️⃣ second()
3️⃣ console.log()
⬇️ executes  unwinds  stack empty
```

**💬 Explanation + Insight**



* Event Loop only moves queued tasks into the stack when it's empty.
* Prevents blocking UI — that's why async exists.

---

## 4️⃣ What's the difference between `setTimeout()` and `setImmediate()`?

**🧠 Concept**



* `setTimeout(fn, 0)`  schedules after current macrotask completes.
* `setImmediate(fn)`  executes immediately after the current event loop phase (Node.js only).

💻 **Example (Node.js):**

```js
setTimeout(() => console.log("Timeout"), 0);
setImmediate(() => console.log("Immediate"));
```

🧠 **Diagram:**

```
Macrotask Queue:
 Timeout and Immediate are queued
Timing order depends on event loop phase
```

**💬 Explanation + Insight**



* In browsers: only `setTimeout`.
* In Node.js: `setImmediate` fires *after I/O events* (faster in some cases).

---

## 5️⃣ What's the difference between Promises and Callbacks?

**🧠 Concept**



* **Callbacks:** functions passed to handle async results.
* **Promises:** objects that represent future values — chainable and cleaner.

**💻 Example**

```js
// Callback
getData((data) => console.log(data));

// Promise
getData()
  .then(data => console.log(data))
  .catch(err => console.error(err));
```

🧠 **Diagram:**

```
Promise  [pending]  [fulfilled/rejected]  .then/.catch
```

**💬 Explanation + Insight**


Promises solve **callback hell** and allow **error propagation** through chains.

---

## 6️⃣ What is a Promise Chain?

**🧠 Concept**


Promise chaining allows sequencing async operations where each `.then()` passes results to the next.

**💻 Example**

```js
fetchUser()
  .then(user => fetchPosts(user.id))
  .then(posts => console.log(posts))
  .catch(err => console.error(err));
```

🧠 **Diagram:**

```
fetchUser  Promise  fetchPosts  Promise  console.log()
```

**💬 Explanation + Insight**


Each `.then()` returns a **new promise**, enabling sequential async flow.

---

## 7️⃣ What is `async/await` and how does it simplify asynchronous code?

**🧠 Concept**


`async/await` makes async code look synchronous — built on top of Promises.

**💻 Example**

```js
async function getData() {
  const user = await fetchUser();
  const posts = await fetchPosts(user.id);
  console.log(posts);
}
```

🧠 **Diagram:**

```
await pauses function execution
↓
Event loop continues other tasks
↓
Resumes when promise resolves
```

**💬 Explanation + Insight**



* Cleaner than `.then()` chains.
* Inside an async function, `await` unwraps the resolved value of a promise.

---

## 8️⃣ How do you handle errors with `async/await`?

**🧠 Concept**


Use `try...catch` to catch rejected promises inside async functions.

**💻 Example**

```js
async function getUser() {
  try {
    const data = await fetch("/user");
    return await data.json();
  } catch (err) {
    console.error("Error:", err);
  }
}
```

🧠 **Diagram:**

```
Promise rejected  jumps to catch block
```

**💬 Explanation + Insight**



* Equivalent to `.catch()` in Promises.
* Can combine `Promise.allSettled()` for multiple async error handling.

---

## 9️⃣ What is `Promise.all()` used for?

**🧠 Concept**


Runs multiple promises in parallel and resolves when **all succeed**, or rejects if **any fail**.

**💻 Example**

```js
Promise.all([
  fetch("/user"),
  fetch("/posts")
])
  .then(([u, p]) => console.log("Both done"))
  .catch(err => console.error("One failed", err));
```

🧠 **Diagram:**

```
All promises  parallel
 one fails  entire chain rejects
```

**💬 Explanation + Insight**


Perfect for batch API calls, image preloading, etc.

---

## 🔟 What are `Promise.race()`, `Promise.any()`, and `Promise.allSettled()`?

**🧠 Concept**



| Method         | Resolves When                  | Rejects When  |
| -------------- | ------------------------------ | ------------- |
| `race()`       | First settles (resolve/reject) | —             |
| `any()`        | First fulfilled                | All reject    |
| `allSettled()` | All settle                     | Never rejects |

**💻 Example**

```js
Promise.race([p1, p2]);
Promise.any([p1, p2]);
Promise.allSettled([p1, p2]);
```

🧠 **Diagram Summary:**

```
race()  fastest result
any()   first success only
allSettled()  results of all promises (status + value)
```

**💬 Explanation + Insight**



* `race()` is great for timeouts.
* `any()` introduced in ES2021 — perfect for redundant API calls.
* `allSettled()` ensures you always get an array of outcomes.

---

## 🧠 **Visual Summary — Async JavaScript Timeline**

```
┌──────────────────────────────────────────────┐
│              EVENT LOOP FLOW                 │
├──────────────────────────────────────────────┤
│ 1️⃣ Synchronous Code (Call Stack executes)    │
│ 2️⃣ Macrotasks (setTimeout, setInterval)     │
│ 3️⃣ Microtasks (Promises, queueMicrotask)     │
│ 4️⃣ Re-render / Next Event Loop Cycle         │
└──────────────────────────────────────────────┘
```

**Example Execution Order:**

```
console.log("1");
setTimeout(() => console.log("2"), 0);
Promise.resolve().then(() => console.log("3"));
console.log("4");

Output:
1
4
3
2
```

---

## ⚠️ **Interview Gotchas & Quick Tips (Async JS)**

1. 🔄 **Order trap:**

   ```js
   setTimeout(..., 0) < Promise.then() < synchronous code
   ```

2. 🧩 **Async/Await = Promise sugar:**
   Every `await` pauses the function but **doesn't block the event loop**.

3. ⚡ **Error handling:**

   * `try...catch` works only **inside async functions**.
   * For parallel tasks: use `Promise.allSettled()`.

4. 🧱 **Promise chain mistake:**
   Forgetting `return` in `.then()`  next `.then()` gets `undefined`.

5. 🕳️ **Event loop misunderstanding:**
   Microtasks (Promises) always flush before macrotasks (setTimeout).

6. 🪄 **Async pitfalls:**
   Mixing `await` in loops causes serial execution — use `Promise.all()` for concurrency.

7. 🧠 **Node.js event loop has extra phases:** timers  I/O  poll  check  close.

8. ⚔️ **Never block the event loop:**
   Heavy CPU tasks (like loops or parsing) freeze the UI.
   Use **Web Workers** for parallelism.

9. 🧩 **Promise.all()** fails fast — one rejection cancels the rest.

10. ⚡ **queueMicrotask(fn)** executes before next macrotask, useful for precise timing adjustments.

---

## 11️⃣ What is Event-Driven Architecture?

**🧠 Concept**


Event-driven architecture (EDA) means the program's flow is controlled by **events** (like clicks, I/O, network requests), not a linear sequence of instructions.

**💻 Example**

```js
const EventEmitter = require("events");
const emitter = new EventEmitter();

emitter.on("login", user => console.log(`${user} logged in`));
emitter.emit("login", "Kamal");
```

🧠 **Diagram:**

```
[Event Source]  emits  [Event Queue]  handled by  [Event Listener]
```

**💬 Explanation + Insight**



* Node.js and browsers both use event-driven patterns.
* Decouples producers (emitters) from consumers (listeners).
* Foundation for **Pub/Sub systems**, **Microservices**, and **WebSocket servers**.

---

## 12️⃣ How does Node.js handle asynchronous operations internally?

**🧠 Concept**


Node.js uses **libuv**, a C library that manages the **thread pool** and **event loop**, to perform non-blocking I/O operations efficiently.

**💻 Example**

```js
const fs = require("fs");
fs.readFile("data.txt", "utf8", () => console.log("File read complete"));
console.log("Reading file...");
```

🧠 **Node.js Event Loop Phases:**

```
┌───────────────────────────────────────────────────┐
│                 NODE.JS EVENT LOOP                │
├───────────────────────────────────────────────────┤
│ 1️⃣ timers         setTimeout(), setInterval()   │
│ 2️⃣ pending I/O    old or deferrable callbacks    │
│ 3️⃣ poll           new I/O events (fs, sockets)   │
│ 4️⃣ check          setImmediate() callbacks       │
│ 5️⃣ close          cleanup, close events          │
└───────────────────────────────────────────────────┘
```

**💬 Explanation + Insight**



* Async tasks offloaded to libuv's thread pool.
* When they finish, callbacks are queued into event loop phases.
* Ensures **non-blocking I/O** even on a single thread.

---

## 13️⃣ How do you handle multiple asynchronous calls sequentially?

**🧠 Concept**


Use **chained Promises** or **async/await** with `for...of` to handle tasks in order.

**💻 Example**

```js
async function processItems(items) {
  for (const item of items) {
    await process(item);
  }
  console.log("Done!");
}
```

🧠 **Diagram:**

```
process(item1)
  ↓ await
process(item2)
  ↓ await
process(item3)
```

**💬 Explanation + Insight**



* `Promise.all()` runs tasks concurrently.
* Sequential handling ensures **order-dependent consistency** but slower performance.

---

## 14️⃣ How do you cancel a Promise in JavaScript?

**🧠 Concept**


Promises themselves can't be canceled natively — but you can use **AbortController** or **custom cancellation logic**.

**💻 Example**

```js
const controller = new AbortController();

fetch("/api/data", { signal: controller.signal });
setTimeout(() => controller.abort(), 1000);
```

🧠 **Diagram:**

```
fetch()  waiting
AbortController  abort()  cancels request
```

**💬 Explanation + Insight**



* AbortController works with `fetch()`.
* For custom promises, use flags or wrappers to ignore results after cancel.

---

## 15️⃣ What are Web Workers and how do they improve performance?

**🧠 Concept**


Web Workers run JavaScript code **in background threads**, off the main UI thread, preventing blocking.

**💻 Example**

```js
// worker.js
self.onmessage = e => self.postMessage(e.data * 2);

// main.js
const worker = new Worker("worker.js");
worker.postMessage(5);
worker.onmessage = e => console.log(e.data); // 10
```

🧠 **Diagram:**

```
Main Thread  ⇄  Worker Thread
     |                |
     | postMessage()  |
     | ← onmessage()  |
```

**💬 Explanation + Insight**



* Workers can't access DOM directly.
* Used for **CPU-heavy tasks** (e.g., image processing, encryption).
* Each has its own event loop.

---

## 16️⃣ What are Service Workers and how are they different?

**🧠 Concept**


Service Workers act as **network proxies** in the browser, intercepting requests and enabling offline caching and background sync.

**💻 Example**

```js
self.addEventListener("fetch", e => {
  e.respondWith(fetch(e.request).catch(() => caches.match(e.request)));
});
```

🧠 **Diagram:**

```
Browser Request  Service Worker  Cache  Network
```

**💬 Explanation + Insight**



* Run even when page is closed.
* Key to **Progressive Web Apps (PWAs)**.
* Lifecycle: install  activate  fetch.

---

## 17️⃣ What's the difference between `fetch()` and `XMLHttpRequest`?

**🧠 Concept**


`fetch()` is modern, Promise-based, and cleaner than `XMLHttpRequest` (XHR), which is callback-based.

**💻 Example**

```js
// Fetch
fetch("/api").then(res => res.json()).then(console.log);

// XHR
const xhr = new XMLHttpRequest();
xhr.onload = () => console.log(xhr.responseText);
xhr.open("GET", "/api");
xhr.send();
```

🧠 **Diagram:**

```
fetch()  Promise
XHR()    Event-based
```

**💬 Explanation + Insight**



* `fetch` cannot track upload progress natively.
* `fetch` fails only on network errors, not HTTP errors (must check `res.ok`).

---

## 18️⃣ What's the difference between `fetch()` and `Axios`?

**🧠 Concept**


Axios is a **wrapper library** around XHR with easier syntax and more features.

**💻 Example**

```js
// Fetch
fetch("/api", { method: "POST", body: JSON.stringify(data) });

// Axios
axios.post("/api", data);
```

🧠 **Diagram:**

```
Axios  Simplifies HTTP with interceptors, defaults, JSON parsing
```

**💬 Explanation + Insight**



* Axios auto-converts data & headers.
* Supports request cancellation, interceptors, and timeouts natively.
* Great for production-level HTTP management.

---

## 19️⃣ How does async iteration (`for await...of`) work?

**🧠 Concept**


It allows looping over **asynchronous iterables**, waiting for each Promise to resolve.

**💻 Example**

```js
async function* fetchData() {
  yield Promise.resolve("A");
  yield Promise.resolve("B");
}

for await (const item of fetchData()) {
  console.log(item);
}
```

🧠 **Diagram:**

```
yield A  await resolve  yield B  await resolve
```

**💬 Explanation + Insight**



* Used in **streaming APIs** and paginated fetches.
* Handles async data sources cleanly in loops.

---

## 20️⃣ What's the difference between synchronous and asynchronous loops?

**🧠 Concept**


Synchronous loops block until all iterations finish; asynchronous loops let other operations run between iterations.

**💻 Example**

```js
// Sync
for (let i = 0; i < 3; i++) console.log(i);

// Async
for (let i = 0; i < 3; i++) setTimeout(() => console.log(i), 0);
```

🧠 **Timeline:**

```
Sync  0,1,2 immediately
Async  scheduled in macrotasks  runs later
```

**💬 Explanation + Insight**



* Async loops use timers, Promises, or async/await.
* Prevent blocking UI and keep event loop responsive.

---

## 🧭 Node.js Event Loop — Full Phase Diagram

```
┌──────────────────────────────────────────────┐
│           Node.js Event Loop Phases          │
├──────────────────────────────────────────────┤
│ 1️⃣ timers           setTimeout, setInterval │
│ 2️⃣ pending I/O      deferred system callbacks│
│ 3️⃣ idle/prepare     internal maintenance     │
│ 4️⃣ poll             new I/O events, execute  │
│ 5️⃣ check            setImmediate callbacks   │
│ 6️⃣ close callbacks  close events, sockets    │
└──────────────────────────────────────────────┘

Microtasks (Promises) run *after each phase* but before the next macrotask.
```

🧠 **Visual Flow Summary:**

```
Call Stack
   ↓
Microtask Queue (Promises)
   ↓
Timer Phase (setTimeout)
   ↓
Poll Phase (I/O)
   ↓
Check Phase (setImmediate)
   ↓
Close Callbacks
```

---

## ⚠️ Interview Gotchas & Quick Tips (Async Internals)

1. 🧩 **Node.js vs Browser:**
   Browser: no `setImmediate()`
   Node.js: `setImmediate()` runs *after* I/O phase.

2. 🕒 **Microtasks always before next phase:**
   `Promise.then()` callbacks flush between each phase.

3. ⚡ **AbortController only cancels fetch** — not general promises unless you design them to respond to abort signals.

4. 🧠 **Avoid `await` in loops** for concurrent requests — use `Promise.all()` instead.

5. 🧵 **Web Workers:** run in separate threads (for CPU tasks).
   **Service Workers:** run as background network proxies.

6. 💥 **Memory leaks:** forgetting to `terminate()` a Worker keeps it alive.

7. 🧱 **EventEmitter memory limit:**
   Node warns after >10 listeners  use `setMaxListeners()` if needed.

8. 🔄 **Promise.race()** for request timeout logic:

   ```js
   Promise.race([fetch(url), timeoutPromise(3000)]);
   ```

9. 🪄 **Event loop starvation:**
   Too many microtasks (e.g., infinite Promise recursion) block UI despite being "async".

10. 🧩 **Service Worker caching pattern:**

    * Cache-first  offline-first apps
    * Network-first  live data priority

---

*This section covers all aspects of asynchronous JavaScript - from basic concepts like event loops and promises to advanced topics like Web Workers and Service Workers.*
