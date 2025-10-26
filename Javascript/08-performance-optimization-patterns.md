# 💻 JavaScript Interview Notes (2025 Edition)

## 🟠 Section 8 — Performance, Optimization & Patterns — Q146-Q165

---

### 146. 🟠 What is Memoization and when should you use it?

**🧠 Concept**


Memoization caches expensive function results so repeated inputs return instantly without re-computing.

**💻 Example**

```js
function memoize(fn) {
  const cache = new Map();
  return (...args) => {
    const key = JSON.stringify(args);
    if (cache.has(key)) return cache.get(key);
    const res = fn(...args);
    cache.set(key, res);
    return res;
  };
}
```

📊 **UML Diagram (Conceptual):**

```
Client  MemoizedFn  Cache(Map)
                    ↳ OriginalFn (only if miss)
```

**💬 Explanation + Insight**


✅ Use for pure functions (fib, search results).
⚠️ Avoid on large mutable inputs  memory bloat.

---

## 2️⃣ Observer Pattern

**🧠 Concept**


Allows objects (Observers) to subscribe to another object (Subject) for state changes.

**💻 Example**

```js
class Subject {
  constructor(){ this.subs=[]; }
  subscribe(fn){ this.subs.push(fn); }
  notify(data){ this.subs.forEach(fn=>fn(data)); }
}
const news = new Subject();
news.subscribe(msg=>console.log("Listener1:",msg));
news.notify("New Article Published!");
```

📊 **UML Diagram:**

```
+----------------+
|   Subject      |
|----------------|
| +subscribe()   |
| +notify()      |
+----------------+
        |
        |  notifies
        v
+----------------+
|   Observer     |
|----------------|
| +update()      |
+----------------+
```

**💬 Explanation + Insight**


✅ Foundation of EventEmitter, RxJS, and Redux middleware.
⚡ Loose coupling between publisher and subscribers.

---

## 3️⃣ Module Pattern

**🧠 Concept**


Encapsulates private data and exposes a public API.

**💻 Example**

```js
const CounterModule = (function(){
  let count = 0;
  return {
    inc: ()=>++count,
    get: ()=>count
  };
})();
```

📊 **UML Diagram:**

```
Module (IIFE)
 ├─ Private scope
 └─ Public methods returned
```

**💬 Explanation + Insight**


✅ Mimics namespace or singleton behavior.
⚡ Still useful in non-module browser scripts.

---

## 4️⃣ Singleton Pattern

**🧠 Concept**


Ensures only one instance of a class exists.

**💻 Example**

```js
class DBConnection {
  constructor(){
    if(DBConnection.instance) return DBConnection.instance;
    this.id = Math.random();
    DBConnection.instance = this;
  }
}
```

📊 **UML Diagram:**

```
+---------------+
|  Singleton    |
|---------------|
| -instance     |
| +getInstance()|
+---------------+
```

**💬 Explanation + Insight**


✅ Used for configs, logging, caches.
⚠️ Testability suffers  mock carefully.

---

## 5️⃣ Factory Pattern

**🧠 Concept**


Creates objects without specifying exact class type.

**💻 Example**

```js
class Car { drive(){ console.log("Car"); } }
class Truck { drive(){ console.log("Truck"); } }

function VehicleFactory(type){
  return type==="car"? new Car() : new Truck();
}
```

📊 **UML Diagram:**

```
Client  Factory  (Car|Truck)
```

**💬 Explanation + Insight**


✅ Centralized object creation.
⚡ Useful for abstracting API clients or UI widgets.

---

## 6️⃣ Proxy Pattern

**🧠 Concept**


Proxy acts as a wrapper to control access to another object.

**💻 Example**

```js
const api = { get:()=>console.log("Real API call") };
const proxy = new Proxy(api, {
  get(target,prop){
    console.log("Intercept:",prop);
    return target[prop];
  }
});
proxy.get();
```

📊 **UML Diagram:**

```
Client  Proxy  RealSubject
```

**💬 Explanation + Insight**


✅ Used for logging, access control, virtualization.
⚡ Core of Vue3 reactivity system.

---

## 7️⃣ Decorator Pattern

**🧠 Concept**


Adds extra behavior to objects without modifying their structure.

**💻 Example**

```js
function withTimestamp(fn){
  return (...args)=>{
    console.log("⏱",new Date());
    return fn(...args);
  };
}
const greet = name => console.log("Hello",name);
const timedGreet = withTimestamp(greet);
timedGreet("Kamal");
```

📊 **UML Diagram:**

```
Component ← Decorator(Component)
```

**💬 Explanation + Insight**


✅ Used for logging, validation, caching wrappers.
⚡ Composable behavior enhancement.

---

## 8️⃣ Lazy Evaluation Pattern

**🧠 Concept**


Delays computation until the value is actually needed.

**💻 Example**

```js
function lazy(fn){
  let evaluated=false, result;
  return ()=> evaluated? result : (evaluated=true, result=fn());
}
const getData = lazy(()=>fetch("/data"));
```

📊 **UML Diagram:**

```
Client  LazyWrapper  computes once  caches
```

**💬 Explanation + Insight**


✅ Prevents redundant API calls.
⚡ Core idea in React Suspense & Next.js data fetching.

---

## 9️⃣ Preventing Layout Thrashing

**🧠 Concept**


Layout thrashing occurs when JS reads and writes DOM styles interleaved, forcing multiple reflows.

💻 **Example (Avoid):**

```js
// ❌
for(let el of items){ el.style.height = el.offsetHeight+"px"; }
```

💻 **Fix:**

```js
const heights = items.map(el=>el.offsetHeight);
items.forEach((el,i)=> el.style.height = heights[i]+"px");
```

📊 **Flow Diagram:**

```
BAD: readwritereadwrite
GOOD: read…readwrite…write
```

**💬 Explanation + Insight**


✅ Batch DOM reads/writes.
⚡ Use `requestAnimationFrame()` or `documentFragment`.

---

## 🔟 Using `requestIdleCallback()` for background tasks

**🧠 Concept**


Schedules non-urgent tasks when the main thread is idle.

**💻 Example**

```js
requestIdleCallback(deadline=>{
  while(deadline.timeRemaining()>0 && tasks.length)
    perform(tasks.shift());
});
```

📊 **UML/Flow:**

```
Main Thread Busy  (Idle Period)  Background Tasks
```

**💬 Explanation + Insight**


✅ Improves perceived performance.
⚡ Combine with throttling for smooth UIs.

---

## 11️⃣ Microtasks vs Macrotasks

**🧠 Concept**


Microtasks run *immediately after the current JS stack* before the next render; macrotasks run *after rendering* (e.g., `setTimeout`).

**💻 Example**

```js
console.log("1");
setTimeout(()=>console.log("2"));
Promise.resolve().then(()=>console.log("3"));
console.log("4");
```

🕒 **Timeline Diagram:**

```
Call Stack  Microtask Queue  Render  Macrotask Queue
1  4  (Promise then: 3)  (setTimeout: 2)
```

📝 **Insight:**
✅ Promises & MutationObservers  microtasks
✅ Timers  macrotasks
⚡ Chain microtasks for micro-batching (React Fiber style).

---

## 12️⃣ Offloading heavy computations with Web Workers

**🧠 Concept**


Workers run JS in background threads — freeing the main thread for UI.

**💻 Example**

```js
// worker.js
self.onmessage = e => self.postMessage(e.data ** 2);

// main.js
const w = new Worker("worker.js");
w.onmessage = e => console.log("Result:", e.data);
w.postMessage(5);
```

🕒 **Timeline:**

```
Main Thread ⟷ Worker Thread
          (non-blocking message passing)
```

📝 **Insight:**
✅ Ideal for CPU-heavy tasks
⚡ Transfer structured clones or ArrayBuffers for zero-copy messaging.

---

## 13️⃣ Profiling DOM Reflow & Repaint

**🧠 Concept**


Each style/layout change may trigger reflow (layout) or repaint (visual update).

💻 **Measurement:**
Open **DevTools  Performance  Record** and watch layout/paint bars.

🕒 **Timeline:**

```
JS   Style  Layout(Reflow)  Paint  Composite
```

📝 **Insight:**
✅ Batch DOM changes
✅ Avoid reading layout values (`offsetHeight`) between writes.

---

## 14️⃣ Async Generators for Streaming Data

**🧠 Concept**


Async generators yield data chunks over time for streaming or pagination.

**💻 Example**

```js
async function* fetchPages() {
  let page = 1;
  while(true) {
    const data = await fetch(`/api?page=${page++}`).then(r=>r.json());
    if(!data.length) break;
    yield data;
  }
}
for await (const items of fetchPages()) console.log(items);
```

🕒 **Diagram:**

```
fetch  yield  consume  repeat
```

📝 **Insight:**
✅ Memory-efficient for large datasets
⚡ Backbone of Node.js streams & browser ReadableStreams.

---

## 15️⃣ Tree-Shaking in Bundlers

**🧠 Concept**


Removes unused code during bundling using static import analysis.

**💻 Example**

```js
// utils.js
export function used() {}
export function unused() {}

// index.js
import { used } from "./utils.js";
```

🕒 **Diagram:**

```
Source  Parser  Dependency Graph  Dead-Code Elimination
```

📝 **Insight:**
✅ Works with ES modules only (`import/export`)
⚡ Use side-effect-free modules for maximum effect.

---

## 16️⃣ Performance Budgets

**🧠 Concept**


Define numeric limits for load size, script time, etc., to keep app fast.

💻 **Example (Lighthouse config):**

```json
"performanceBudget": {
  "resourceSizes": [{ "resourceType": "script", "budget": 300 }]
}
```

🕒 **Diagram:**

```
Budgets  Build checks  Alert if exceeded
```

📝 **Insight:**
✅ Keeps bundle growth in check
⚡ Integrate into CI/CD for regression alerts.

---

## 17️⃣ Measuring Script Parse & Execution Time

**🧠 Concept**


Use `performance.now()` or DevTools Performance panel to time script load/exec.

**💻 Example**

```js
const start = performance.now();
heavyFunction();
console.log("Exec time:", performance.now() - start);
```

🕒 **Timeline:**

```
Parse  Compile  Execute  (measure)
```

📝 **Insight:**
✅ Split long tasks; lazy-load heavy modules.
⚡ Pre-parse frequently used code paths.

---

## 18️⃣ Preventing Main Thread Blocking

**🧠 Concept**


Split big tasks into small chunks to maintain 60 FPS.

**💻 Example**

```js
function chunkedProcess(items) {
  const chunk = ()=> {
    const batch = items.splice(0,100);
    process(batch);
    if(items.length) requestIdleCallback(chunk);
  };
  chunk();
}
```

🕒 **Timeline:**

```
Frame 1: chunk1(2ms)
Frame 2: render
Frame 3: chunk2(3ms)
```

📝 **Insight:**
✅ Keeps UI responsive
⚡ Inspired by React Concurrent Mode scheduling.

---

## 19️⃣ Minimizing Memory Leaks in Large Apps

**🧠 Concept**


Release unused references and event listeners early.

🕒 **Diagram:**

```
Strong Ref  no GC  
Weak Ref  GC eligible  
No Ref  freed
```

📝 **Insight:**
✅ Use WeakMap for DOMdata links
✅ Remove listeners on unmount
⚡ Observe heap snapshots in DevTools  check retained objects.

---

## 20️⃣ Script Loading Optimization (Defer vs Async)

**🧠 Concept**


`defer` loads scripts in order after HTML parse; `async` loads independently (order unreliable).

**💻 Example**

```html
<script src="a.js" defer></script>
<script src="b.js" async></script>
```

🕒 **Timeline:**

```
HTML parse
 ├─ async (a.js)  downloads parallel  executes as soon as ready
 └─ defer (b.js)  downloads parallel  executes after parse
```

📝 **Insight:**
✅ Always prefer `defer` for critical bundles.
⚡ Combine with `preload`/`prefetch` for faster starts.

---

## 🧠 Pattern and Performance Summary

| Category    | Pattern             | Goal                    | Common Use            |
| ----------- | ------------------- | ----------------------- | --------------------- |
| Caching     | Memoization         | Speed up pure functions | Heavy computation     |
| Behavioral  | Observer            | Event systems           | Streams, UI           |
| Structural  | Module / Singleton  | Encapsulation           | Config, utilities     |
| Creational  | Factory             | Object creation         | API client builders   |
| Structural  | Proxy               | Access control          | Virtual DOM, security |
| Structural  | Decorator           | Add behavior            | Logging, validation   |
| Performance | Lazy Eval           | Delay work              | Data fetching         |
| Rendering   | Layout Optimization | Prevent jank            | DOM updates           |
| Scheduling  | requestIdleCallback | Idle tasks              | Analytics, cleanup    |

---

## 🧠 Performance Timeline Summary

```
Frame (≈16.6 ms)
 ├─ JS Task
 │   ├─ Microtasks (Promises)
 │   └─ Macrotasks (setTimeout)
 ├─ Render
 │   ├─ Style
 │   ├─ Layout
 │   └─ Paint
 └─ Composite
```

---

*This section covers performance optimization techniques, design patterns, and advanced JavaScript performance concepts essential for building high-performance applications.*
