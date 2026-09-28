---
sidebar_label: "Web APIs & Real-World Topics"
---
# 🔌 7. Web APIs & Real-World Topics (Q128–147, Q208–212)

> **Reviewed:** 2026-09 · Modernized; legacy topics are labeled.

---

## Q128. 👷 Web Workers and how they work

Web Workers run JavaScript in background threads, enabling CPU-intensive tasks without blocking the main thread - they run in separate thread with own global scope and communicate via `postMessage` and `onmessage`. Great for heavy computations and data processing where you need to keep the UI responsive.

- **Trade-offs**: The catch is these can't access DOM or `window` object - you must use `postMessage` for communication. Workers prevent blocking the main thread, keeping UI responsive, but watch out - use `terminate()` to stop workers when you're done to free up resources.

Example:

```js
// Create Web Worker: runs JavaScript in background thread
const worker = new Worker('worker.js'); // Load worker script
// Send data to worker (data is copied, not shared)
worker.postMessage({ data: [1, 2, 3, 4, 5] });
// Receive response from worker
worker.onmessage = e => console.log(e.data); // e.data contains worker's response

// Modern: module workers can use import/export, and bundlers understand this pattern
const moduleWorker = new Worker(new URL('./worker.js', import.meta.url), { type: 'module' });

```

---

## Q129. 👷 What can't be accessed inside a Web Worker

Web Workers can't access DOM, `window` object, or parent page's variables due to security and threading constraints - they run in isolated context for security. You can't modify UI directly and are limited to `self` global scope.

- **Trade-offs**: The catch is you must use `postMessage` for communication - there's no direct access to parent page variables. Isolation prevents race conditions and security issues in multi-threaded code, but it means you need to structure your communication carefully.

Example:

```js
// worker.js - These will cause errors:
// document.getElementById('id'); // ReferenceError
// window.location; // ReferenceError
// parent.someVariable; // ReferenceError

```

---

## Q130. 👷 Communicating between the main thread and a Web Worker

Use `postMessage()` to send data and `onmessage` to receive responses between threads - data is copied, not shared (structured cloning), ensuring data safety across threads. Use message types for different operations and handle errors with `onerror` event.

- **Trade-offs**: The catch is considering transferable objects for large data - structured cloning can be slow for big objects. Messages are queued if worker is busy, which ensures data safety across threads without shared memory issues, but watch out for performance with large payloads.

Example:

```js
// Send message to worker with type and data
worker.postMessage({ type: 'CALCULATE', data: numbers }); // Structured cloning

// Handle messages from worker
worker.onmessage = e => {
  if (e.data.type === 'RESULT') console.log(e.data.result); // Process result
};

// Handle errors in worker
worker.onerror = e => console.error('Worker error:', e); // Error handling

```

---

## Q131. 👷 Shared Workers

Shared Workers can be accessed by multiple browser contexts (tabs, windows) and persist across page loads - they use `MessagePort` for communication and can coordinate state across multiple tabs. They persist until all connections close, great for shared state and coordination.

- **Trade-offs**: The catch is they're more complex than dedicated workers - you need to manage `MessagePort` connections. They enable cross-tab communication and shared state management, but watch out - coordinating state across multiple tabs can get tricky.

Example:

```js
const sharedWorker = new SharedWorker('shared-worker.js');
sharedWorker.port.onmessage = e => console.log(e.data);
sharedWorker.port.postMessage({ message: 'hello' });

```

---

## Q132. 👷 Service Workers

Service Workers are background scripts that act as network proxies, enabling offline functionality and push notifications - they act as network proxy between app and network, enabling offline functionality with caching. They support push notifications and background sync, with lifecycle: install → activate → fetch.

- **Trade-offs**: The catch is they require a secure context - HTTPS in production, though `http://localhost` is treated as secure so local development works without certificates. Service workers enable Progressive Web Apps (PWAs) with offline capabilities, but watch out - the lifecycle can be complex to manage properly.

Example:

```js
self.addEventListener('install', e => {
  e.waitUntil(caches.open('v1').then(cache =>
    cache.addAll(['/', '/styles.css', '/script.js'])));
});

```

---

## Q133. 🔄 Lifecycle events of a Service Worker (install, activate, fetch)

Service Workers have three main lifecycle events: install (setup), activate (cleanup), and fetch (handle requests) - install runs once when SW is first registered, activate runs when SW takes control, fetch runs for every network request. Use `waitUntil()` for async operations in these events.

- **Trade-offs**: The catch is skip waiting forces immediate activation - understanding lifecycle is crucial for SW implementation and cache management. Lifecycle events enable proper cache management, but watch out - the timing of install and activate can affect when your service worker takes control.

Example:

```js
self.addEventListener('install', e => {
  console.log('Installing...');
  e.waitUntil(doInstallWork());
});

self.addEventListener('activate', e => {
  console.log('Activating...');
  e.waitUntil(doActivateWork());
});

self.addEventListener('fetch', e => {
  console.log('Fetching:', e.request.url);
});

```

---

## Q134. 👷 How Service Workers enable offline caching

Service Workers intercept network requests and serve cached responses when offline - intercept all network requests, check cache first, fallback to network. Cache responses for future use and use cache strategies (cache-first, network-first) to optimize performance.

- **Trade-offs**: The catch is handling cache updates and versioning - different caching strategies optimize performance, but you need to manage cache invalidation carefully. Caching strategies balance freshness and speed for optimal user experience, but watch out - stale cache can cause issues.

Example:

```js
self.addEventListener('fetch', e => {
  e.respondWith(caches.match(e.request).then(response =>
    response || fetch(e.request).then(fetchResponse => {
      caches.open('v1').then(cache =>
        cache.put(e.request, fetchResponse.clone()));
      return fetchResponse;
    })));
});

```

---

## Q136. 🔔 Handling background sync or push notifications

Use Service Worker events for background sync and push notifications when the app isn't active - background sync runs when connection restored, push events trigger when server sends notification. Use `waitUntil()` for async operations and handle user interactions with notification clicks.

- **Trade-offs**: The catch is considering user permissions and preferences - push notifications enable real-time updates, but users need to grant permission first. Background sync improves offline experience by queuing actions for later, but watch out - sync events might not fire immediately if the browser is closed, and the Background Sync API is currently Chromium-only, so feature-detect (`'sync' in registration`) and fall back to retrying on the next page load. Web Push works across modern browsers, including Safari (on iOS only for PWAs added to the Home Screen).

Example:

```js
self.addEventListener('sync', e => {
  if (e.tag === 'background-sync') e.waitUntil(doBackgroundWork());
});
self.addEventListener('push', e => {
  const data = e.data.json();
  self.registration.showNotification(data.title, { body: data.body });
});

```

---

## Q137. 👷 Unregistering a Service Worker

Use `navigator.serviceWorker.getRegistrations()` to find and unregister Service Workers - `unregister()` returns a promise and removes SW from browser's registry. It may take time to fully remove, so consider user confirmation before unregistering.

- **Trade-offs**: The catch is it may take time to fully remove - test unregistration in different scenarios to make sure it works properly. Unregistering is needed for updates and debugging Service Worker issues, but watch out - unregistering doesn't immediately stop the service worker if it's handling requests.

Example:

```js
navigator.serviceWorker.getRegistrations().then(regs =>
  regs.forEach(reg => reg.unregister()));

```

---

## Q135. 👷 Difference between Web Workers and Service Workers

Web Workers run background tasks for CPU-intensive work, while Service Workers act as network proxies for offline functionality - Web Workers handle CPU tasks with one-to-one communication, Service Workers handle network proxy with one-to-many communication. Web Workers can be dedicated or shared, Service Workers are persistent and event-driven.

- **Trade-offs**: The catch is they have different use cases and capabilities - choose based on use case: computation vs. network/caching needs. Each serves different purposes in web apps, but watch out - don't confuse them - use Web Workers for heavy computation, Service Workers for network and caching.

Example:

```js
// Web Worker - background computation
const worker = new Worker('compute.js');
worker.postMessage(data);

// Service Worker - network proxy
navigator.serviceWorker.register('sw.js');

```

---

## Q138. 🔄 Event delegation

Event delegation attaches a single event listener to a parent element to handle events from child elements - it reduces memory usage and improves performance, working with dynamically added elements. Use `e.target` to identify the actual clicked element, great for lists and tables with many interactive elements.

- **Trade-offs**: The catch is considering event bubbling vs capturing - single listener handles multiple child elements, but you need to check which element was actually clicked. Event delegation is more efficient than multiple listeners for dynamic content, but watch out - you need to filter events to only handle the ones you care about.

Example:

```js
document.addEventListener('click', e => {
  if (e.target.matches('.button')) {
    console.log('Button clicked:', e.target.textContent);
  }
});

```

---

## Q139. 🔄 Event bubbling and capturing

Event bubbling propagates from child to parent, while capturing propagates from parent to child - there are three phases: capture → target → bubble. Use `e.stopPropagation()` to stop propagation, or `e.stopImmediatePropagation()` to stop all handlers.

- **Trade-offs**: The catch is capturing is less commonly used - event delegation relies on bubbling, which is the default behavior. Understanding propagation helps with event handling and delegation patterns, but watch out - stopping propagation can break other event handlers that expect events to bubble.

Example:

```js
// Capturing phase (parent to child)
element.addEventListener('click', handler, true);

// Bubbling phase (child to parent) - default
element.addEventListener('click', handler, false);

```

---

## Q140. 💡 Shadow DOM

Shadow DOM encapsulates DOM and CSS, creating isolated components that don't interfere with the main document - it creates encapsulated DOM subtree where styles don't leak out or in. Used by Web Components, and `mode: 'open'` allows external access.

- **Trade-offs**: The catch is it's great for reusable component libraries - shadow DOM prevents style conflicts and enables true component isolation, but watch out - debugging shadow DOM can be trickier since it's hidden from normal DOM inspection. It enables true component encapsulation, which is powerful but adds complexity.

Example:

```js
const host = document.getElementById('host');
const shadow = host.attachShadow({ mode: 'open' });
shadow.innerHTML = `
  <style>p { color: red; }</style>
  <p>This is isolated from main document</p>
`;

```

---

## Q141. 📄 Difference between `innerHTML`, `textContent`, and `innerText`

`innerHTML` includes HTML tags, `textContent` gets all text, and `innerText` gets visible text respecting CSS - choose based on need: HTML vs text vs visible text. `innerHTML` includes HTML markup and can execute scripts, `textContent` gets all text content and is safer and faster, `innerText` gets visible text only and respects CSS but is slower.

- **Trade-offs**: The catch is `innerHTML` can cause XSS if not sanitized - prefer `textContent` to avoid XSS attacks. Use `textContent` for security and performance, but watch out - `innerText` is slower because it has to calculate what's visible, so use it only when you need visible text specifically.

Example:

```js
const div = document.createElement('div');
div.innerHTML = '<p>Hello <span style="display:none">hidden</span> World</p>';
document.body.append(div); // innerText only respects CSS for rendered elements - on a detached node it behaves like textContent
div.innerHTML; // '<p>Hello <span style="display:none">hidden</span> World</p>'
div.textContent; // 'Hello hidden World'
div.innerText; // 'Hello  World' (hidden span skipped)

```

---

## Q142. 🤔 Difference between `for...in` and `for...of`

`for...in` iterates over enumerable property names, while `for...of` iterates over iterable values - `for...in` gives property names and includes inherited properties, `for...of` gives values and works with iterables (arrays, strings, maps). Use `for...of` for arrays and iterables; for plain objects, modern code usually writes `for (const [key, value] of Object.entries(obj))` (own enumerable only), or `for...in` guarded with `Object.hasOwn`.

- **Trade-offs**: The catch is `for...of` is generally preferred for arrays - it's more efficient and gives you values directly. Choose based on whether you need keys or values from your data structure, but watch out - `for...in` on arrays includes custom properties you might not expect.

Example:

```js
const arr = [1, 2, 3];
arr.custom = 'property';

for (let key in arr) console.log(key); // '0', '1', '2', 'custom'
for (let value of arr) console.log(value); // 1, 2, 3

```

---

## Q143. 💡 ⏰ Polyfill and when to use one

A polyfill is code that implements a feature in older browsers that don't natively support it - it provides missing functionality in older browsers. Use feature detection before adding polyfills and consider bundle size impact.

- **Trade-offs**: The catch is using tools like Babel and core-js for automatic polyfilling - test thoroughly in target browsers to make sure polyfills work correctly. Polyfills enable backward compatibility for modern JavaScript features, but watch out - they add to your bundle size, so only include what you need.

Example:

```js
// Polyfill for Array.prototype.at (ES2022) - feature-detect first
if (!Array.prototype.at) {
  Array.prototype.at = function(index) {
    const n = Math.trunc(index) || 0;
    const i = n < 0 ? this.length + n : n;
    return i >= 0 && i < this.length ? this[i] : undefined;
  };
}

```

> **Legacy note (2026):** The classic `Array.prototype.includes` polyfill built on `indexOf` is subtly wrong - `[NaN].indexOf(NaN)` is `-1` but `[NaN].includes(NaN)` is `true`. That's why teams rely on vetted polyfills (core-js via Babel's `useBuiltIns: 'usage'`) driven by a Browserslist target instead of hand-rolled ones. With evergreen-browser targets, many projects now ship few or no ES polyfills at all.

---

## Q144. 🔧 Data attributes and how to access them in JavaScript

Data attributes store custom data on HTML elements using `data-*` attributes - use `dataset` property to access data attributes, where kebab-case becomes camelCase (`data-user-id` → `userId`). Values are always strings, great for storing component state and configuration.

- **Trade-offs**: The catch is avoiding storing complex data - use JSON if needed, since values are always strings. Data attributes enable custom metadata on elements for component configuration, and `dataset` has been supported in every browser for over a decade, so no polyfill is needed. Don't store secrets there - anything in the DOM is visible to the user.

Example:

```js
// HTML: <div data-user-id="123" data-role="admin"></div>
const element = document.querySelector('div');
const userId = element.dataset.userId; // '123'
const role = element.dataset.role; // 'admin'
element.dataset.status = 'active'; // Sets data-status="active"

```

---

## Q145. 🔧 Pure functions and side effects

Pure functions always return the same output for the same input and have no side effects - they're predictable and testable, making code easier to reason about. Side effects include DOM manipulation, API calls, and console.log.

- **Trade-offs**: The catch is preferring pure functions when possible - use pure functions for reducers and transformations, side effects are necessary but should be isolated. Pure functions are easier to test and reason about than impure functions, but watch out - you can't avoid side effects completely, so isolate them in specific parts of your code.

Example:

```js
// Pure function
const add = (a, b) => a + b;

// Impure function (has side effects)
let counter = 0;
const increment = () => ++counter;

```

---

## Q146. 🔧 Memory leak and how to detect it

Memory leaks occur when objects remain in memory but are no longer needed, preventing garbage collection - use browser dev tools Memory tab to detect leaks, look for growing heap size over time. Common causes include event listeners, closures, and timers that aren't cleaned up.

- **Trade-offs**: The catch is detection is mostly manual: take heap snapshots in DevTools before and after repeating an action and compare retained objects ("Detached" DOM nodes are a classic signal). Avoid the non-standard, Chromium-only `performance.memory`; `performance.measureUserAgentSpecificMemory()` exists but only in cross-origin-isolated pages. For prevention, remove listeners with an `AbortController` signal (`addEventListener(type, fn, { signal })`), clear timers, and use `WeakMap`/`WeakRef` for caches keyed by objects. Memory leaks cause performance degradation over time, requiring careful cleanup, but watch out - some leaks are subtle and only show up after extended use.

Example:

```js
// Memory leak example
const leaks = [];
setInterval(() => {
  leaks.push(new Array(1000000)); // Growing array
}, 1000);

```

---

## Q147. ⚡ How JavaScript handles tail call optimization (TCO)

TCO optimizes recursive function calls by reusing the current stack frame instead of creating new ones - it only works with tail calls where the last operation is the recursive call. It prevents stack overflow for deep recursion. ES2015 actually specifies "proper tail calls" in strict mode, but only Safari's JavaScriptCore ships them - V8 (Chrome, Node, Deno) and SpiderMonkey (Firefox) do not, so you can't rely on it.

- **Trade-offs**: The catch is it's not available in most engines - use iteration or trampolines as alternatives when TCO isn't available. Consider the recursive pattern carefully for optimization, but watch out - most JavaScript engines don't support TCO, so prefer iteration for deep recursion to avoid stack overflow.

Example:

```js
// Tail recursive function
const factorial = (n, acc = 1) =>
  n <= 1 ? acc : factorial(n - 1, n * acc);

// Non-tail recursive (not optimized)
const factorialBad = n =>
  n <= 1 ? 1 : n * factorialBad(n - 1);

```

---

## Q208. 🛑 `AbortController` and cancelling async work

`AbortController` is the standard way to cancel async work in browsers and Node. You create a controller, pass its `signal` to anything that supports cancellation (`fetch`, `addEventListener`, many Node APIs like `fs.readFile` and `timers/promises`), and call `controller.abort()` when you want to stop. The aborted operation rejects with an `AbortError` (or whatever reason you pass to `abort(reason)`).

- **Trade-offs**: Cancellation is cooperative - your own async functions have to check `signal.aborted` / call `signal.throwIfAborted()` or listen for the `abort` event, otherwise nothing actually stops. A controller is single-use: once aborted, create a new one for the next request. The static helpers `AbortSignal.timeout(ms)` and `AbortSignal.any([...signals])` cover most timeout and "cancel on either" cases without manual timers.

Example:

```js
let controller;

async function search(query) {
  controller?.abort(); // cancel the previous in-flight request (typeahead pattern)
  controller = new AbortController();
  const signal = AbortSignal.any([controller.signal, AbortSignal.timeout(5000)]);
  try {
    const res = await fetch(`/search?q=${encodeURIComponent(query)}`, { signal });
    return await res.json();
  } catch (err) {
    if (err.name === 'AbortError' || err.name === 'TimeoutError') return null; // expected
    throw err;
  }
}

// Bonus: one abort() removes every listener registered with the signal
const ui = new AbortController();
window.addEventListener('resize', onResize, { signal: ui.signal });
window.addEventListener('scroll', onScroll, { signal: ui.signal });
ui.abort(); // cleanup on unmount
```

Reference: [MDN - AbortController](https://developer.mozilla.org/en-US/docs/Web/API/AbortController)

---

## Q209. 📦 `structuredClone()` vs `JSON.parse(JSON.stringify())`

Both make a deep copy, but `structuredClone()` (a web platform API, also in Node 17+ and Deno/Bun) uses the structured clone algorithm - the same one `postMessage` uses - so it understands far more types. The JSON round-trip only works for plain JSON data and silently corrupts everything else.

| Value | `JSON.parse(JSON.stringify(x))` | `structuredClone(x)` |
| --- | --- | --- |
| `Date` | becomes an ISO string | stays a `Date` |
| `Map` / `Set` | becomes `{}` | preserved |
| `undefined` properties | dropped | preserved |
| `NaN` / `Infinity` | becomes `null` | preserved |
| `BigInt` | throws `TypeError` | preserved |
| Circular references | throws `TypeError` | preserved |
| Functions / DOM nodes | dropped / `{}` | throws `DataCloneError` |
| Class instances | plain object | plain object (prototype lost) |

- **Trade-offs**: Use `structuredClone` as the default deep-copy tool. JSON round-tripping is still fine when you're *serializing anyway* (e.g. to send over the network or into `localStorage`). Neither preserves prototypes or getters, so class instances need a custom `clone()` method. `structuredClone` also supports transferring buffers: `structuredClone(obj, { transfer: [buffer] })`.

Example:

```js
const original = { when: new Date(0), tags: new Set(['a']), missing: undefined };
original.self = original; // circular

const copy = structuredClone(original);
copy.when instanceof Date; // true
copy.tags.has('a');        // true
copy.self === copy;        // true - cycle rebuilt inside the copy

JSON.parse(JSON.stringify({ when: new Date(0) })); // { when: '1970-01-01T00:00:00.000Z' }
```

Reference: [MDN - structuredClone()](https://developer.mozilla.org/en-US/docs/Web/API/Window/structuredClone)

---

## Q210. 🧩 ES modules in the browser

Browsers load ES modules natively with `<script type="module">`. Module scripts are **deferred by default** (they download in parallel and execute after the HTML is parsed, in order), run in **strict mode**, have their **own top-level scope** (no accidental globals), are fetched with **CORS**, and execute **once** no matter how many times they're imported. Top-level `await` and dynamic `import()` work natively.

Bare specifiers like `import { debounce } from 'lodash-es'` don't resolve on their own - you either use a bundler (Vite, esbuild, Rollup, webpack) or an **import map** (`<script type="importmap">`), which is supported in all modern browsers.

- **Trade-offs**: Unbundled modules create request waterfalls (the browser discovers dependencies one level at a time), so production apps still usually bundle, or at least add `<link rel="modulepreload">` hints. Opening an HTML file via `file://` fails because modules need CORS - serve it over HTTP. `import.meta.url` gives you the module's own URL for resolving assets.

Example:

```html
<script type="importmap">
  { "imports": { "utils/": "/js/utils/" } }
</script>
<link rel="modulepreload" href="/js/app.js">
<script type="module" src="/js/app.js"></script>
```

```js
// /js/app.js
import { formatDate } from 'utils/date.js'; // resolved through the import map
const config = await fetch('/config.json').then(r => r.json()); // top-level await

button.addEventListener('click', async () => {
  const { openEditor } = await import('./editor.js'); // lazy-load on demand
  openEditor(config);
});
```

> **Legacy note (2026):** The `<script nomodule>` fallback pattern (shipping a separate ES5 bundle for browsers without module support) was needed for IE11-era browsers. With evergreen targets it's rarely worth the extra build.

Reference: [MDN - JavaScript modules](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Guide/Modules)

---

## Q211. 🧵 Web Workers vs the main thread: what goes where?

The main thread runs your JavaScript *and* does style, layout, paint, and input handling. Any JS task that runs long blocks all of that, which users experience as jank and poor INP (Interaction to Next Paint). A Web Worker gives you a separate thread with its own event loop for CPU-heavy work, but no DOM access.

**Keep on the main thread:** DOM reads/writes, event handlers, anything that must touch UI state, and short tasks.
**Move to a worker:** parsing or transforming large data (CSV/JSON), image/audio processing, compression, crypto, search indexing, WASM computation - anything that would otherwise run for more than a few frames.

- **Trade-offs**: Messages are copied via structured clone, so shipping huge objects back and forth can cost more than the work itself - use transferable objects (`ArrayBuffer`, `OffscreenCanvas`, `MessagePort`) to move data without copying. `SharedArrayBuffer` + `Atomics` enables true shared memory but requires cross-origin isolation (COOP/COEP headers). For work that is merely *long* but not CPU-bound, you can also break it up on the main thread and yield between chunks (`scheduler.yield()` where available, otherwise `setTimeout(0)`).

Example:

```js
// main.js
const worker = new Worker(new URL('./parse.worker.js', import.meta.url), { type: 'module' });
const buffer = await file.arrayBuffer();
worker.postMessage(buffer, [buffer]); // transfer: buffer is now detached (byteLength 0) here
worker.onmessage = ({ data }) => renderTable(data.rows); // DOM work stays on main thread

// parse.worker.js
self.onmessage = ({ data }) => {
  const text = new TextDecoder().decode(data);
  const rows = text.split('\n').map(line => line.split(','));
  self.postMessage({ rows });
};
```

Reference: [MDN - Using Web Workers](https://developer.mozilla.org/en-US/docs/Web/API/Web_Workers_API/Using_web_workers)

---

## Q212. ⚡ Event loop ordering with `await` - predict the output

The rule to remember: code before the first `await` in an async function runs **synchronously**. Everything after an `await` is resumed later as a **microtask**, even if you await a non-promise like `null`. All microtasks drain before the next macrotask (like a `setTimeout` callback) runs.

```js
async function task() {
  console.log('A');
  await null;
  console.log('B');
}

console.log('start');
setTimeout(() => console.log('timeout'), 0);
task();
Promise.resolve()
  .then(() => console.log('C'))
  .then(() => console.log('D'));
console.log('end');
```

Output:

```text
start
A
end
B
C
D
timeout
```

Why:

1. `start` - plain synchronous code.
2. `setTimeout` queues `timeout` as a **macrotask**.
3. `task()` runs synchronously up to the `await`, logging `A`; the rest of `task` (microtask 1) is queued.
4. `.then(C)` queues microtask 2. (`D` isn't queued yet - it waits for `C`'s promise.)
5. `end` - the synchronous script finishes, so the call stack is empty.
6. Microtasks drain in FIFO order: `B`, then `C` (which queues `D`), then `D`.
7. Only now does the event loop take the next macrotask: `timeout`.

- **Trade-offs**: This ordering is deterministic and a favourite interview question, but don't design real code around exact tick counts - engine optimizations have changed them before (e.g. returning a promise from an `async` function costs a couple of extra microtask ticks compared with returning a plain value). If ordering matters, make the dependency explicit with `await`.

Reference: [MDN - Using microtasks](https://developer.mozilla.org/en-US/docs/Web/API/HTML_DOM_API/Microtask_guide)

---

