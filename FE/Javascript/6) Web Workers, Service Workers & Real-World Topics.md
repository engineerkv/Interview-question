# 🔌 6. Web Workers, Service Workers & Real-World Topics (Q170–189)

---

## 📍 Navigation

<div align="center">

[Promises, Async-Await & Event Loop](5%29%20Promises%2C%20Async-Await%20%26%20Event%20Loop.md) • [Home: README](../README.md) • [Practical JavaScript Questions →](7%29%20Practical%20JavaScript%20Questions.md)

[📋 Cheatsheet](JavaScript%20Interview%20Cheatsheet.md]

</div>

---

---

## Q170. 👷 Web Workers and how they work

Web Workers run JavaScript in background threads, enabling CPU-intensive tasks without blocking the main thread - they run in separate thread with own global scope and communicate via `postMessage` and `onmessage`. Great for heavy computations and data processing where you need to keep the UI responsive.

- **Trade-offs**: The catch is they can't access DOM or `window` object - you must use `postMessage` for communication. Workers prevent blocking the main thread, keeping UI responsive, but watch out - use `terminate()` to stop workers when you're done to free up resources.

Example:

```js
const worker = new Worker('worker.js');
worker.postMessage({ data: [1, 2, 3, 4, 5] });
worker.onmessage = e => console.log(e.data);

```

---

## Q171. 👷 What can't be accessed inside a Web Worker

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

## Q172. 👷 Communicating between the main thread and a Web Worker

Use `postMessage()` to send data and `onmessage` to receive responses between threads - data is copied, not shared (structured cloning), ensuring data safety across threads. Use message types for different operations and handle errors with `onerror` event.

- **Trade-offs**: The catch is considering transferable objects for large data - structured cloning can be slow for big objects. Messages are queued if worker is busy, which ensures data safety across threads without shared memory issues, but watch out for performance with large payloads.

Example:

```js
worker.postMessage({ type: 'CALCULATE', data: numbers });
worker.onmessage = e => {
  if (e.data.type === 'RESULT') console.log(e.data.result);
};
worker.onerror = e => console.error('Worker error:', e);

```

---

## Q173. 👷 Shared Workers

Shared Workers can be accessed by multiple browser contexts (tabs, windows) and persist across page loads - they use `MessagePort` for communication and can coordinate state across multiple tabs. They persist until all connections close, great for shared state and coordination.

- **Trade-offs**: The catch is they're more complex than dedicated workers - you need to manage `MessagePort` connections. They enable cross-tab communication and shared state management, but watch out - coordinating state across multiple tabs can get tricky.

Example:

```js
const sharedWorker = new SharedWorker('shared-worker.js');
sharedWorker.port.onmessage = e => console.log(e.data);
sharedWorker.port.postMessage({ message: 'hello' });

```

---

## Q174. 👷 Service Workers

Service Workers are background scripts that act as network proxies, enabling offline functionality and push notifications - they act as network proxy between app and network, enabling offline functionality with caching. They support push notifications and background sync, with lifecycle: install → activate → fetch.

- **Trade-offs**: The catch is they must be served over HTTPS - you can't use them on localhost without HTTPS. Service workers enable Progressive Web Apps (PWAs) with offline capabilities, but watch out - the lifecycle can be complex to manage properly.

Example:

```js
self.addEventListener('install', e => {
  e.waitUntil(caches.open('v1').then(cache =>
    cache.addAll(['/', '/styles.css', '/script.js'])));
});

```

---

## Q175. 🔄 Lifecycle events of a Service Worker (install, activate, fetch)

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

## Q176. 👷 How Service Workers enable offline caching

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

## Q177. 👷 Difference between Web Workers and Service Workers

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

## Q178. 🔔 Handling background sync or push notifications

Use Service Worker events for background sync and push notifications when the app isn't active - background sync runs when connection restored, push events trigger when server sends notification. Use `waitUntil()` for async operations and handle user interactions with notification clicks.

- **Trade-offs**: The catch is considering user permissions and preferences - push notifications enable real-time updates, but users need to grant permission first. Background sync improves offline experience by queuing actions for later, but watch out - sync events might not fire immediately if the browser is closed.

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

## Q179. 👷 Unregistering a Service Worker

Use `navigator.serviceWorker.getRegistrations()` to find and unregister Service Workers - `unregister()` returns a promise and removes SW from browser's registry. It may take time to fully remove, so consider user confirmation before unregistering.

- **Trade-offs**: The catch is it may take time to fully remove - test unregistration in different scenarios to make sure it works properly. Unregistering is needed for updates and debugging Service Worker issues, but watch out - unregistering doesn't immediately stop the service worker if it's handling requests.

Example:

```js
navigator.serviceWorker.getRegistrations().then(regs =>
  regs.forEach(reg => reg.unregister()));

```

---

## Q180. 🔄 Event delegation

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

## Q181. 🔄 Event bubbling and capturing

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

## Q182. 💡 Shadow DOM

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

## Q183. 📄 Difference between `innerHTML`, `textContent`, and `innerText`

`innerHTML` includes HTML tags, `textContent` gets all text, and `innerText` gets visible text respecting CSS - choose based on need: HTML vs text vs visible text. `innerHTML` includes HTML markup and can execute scripts, `textContent` gets all text content and is safer and faster, `innerText` gets visible text only and respects CSS but is slower.

- **Trade-offs**: The catch is `innerHTML` can cause XSS if not sanitized - prefer `textContent` to avoid XSS attacks. Use `textContent` for security and performance, but watch out - `innerText` is slower because it has to calculate what's visible, so use it only when you need visible text specifically.

Example:

```js
const div = document.createElement('div');
div.innerHTML = '<p>Hello <span style="display:none">hidden</span> World</p>';
div.innerHTML; // '<p>Hello <span style="display:none">hidden</span> World</p>'
div.textContent; // 'Hello hidden World'
div.innerText; // 'Hello World'

```

---

## Q184. 🤔 Difference between `for...in` and `for...of`

`for...in` iterates over enumerable property names, while `for...of` iterates over iterable values - `for...in` gives property names and includes inherited properties, `for...of` gives values and works with iterables (arrays, strings, maps). Use `for...of` for arrays and iterables, use `for...in` with `hasOwnProperty` for object properties.

- **Trade-offs**: The catch is `for...of` is generally preferred for arrays - it's more efficient and gives you values directly. Choose based on whether you need keys or values from your data structure, but watch out - `for...in` on arrays includes custom properties you might not expect.

Example:

```js
const arr = [1, 2, 3];
arr.custom = 'property';

for (let key in arr) console.log(key); // '0', '1', '2', 'custom'
for (let value of arr) console.log(value); // 1, 2, 3

```

---

## Q185. ⏰ Polyfill and when to use one

A polyfill is code that implements a feature in older browsers that don't natively support it - it provides missing functionality in older browsers. Use feature detection before adding polyfills and consider bundle size impact.

- **Trade-offs**: The catch is using tools like Babel and core-js for automatic polyfilling - test thoroughly in target browsers to make sure polyfills work correctly. Polyfills enable backward compatibility for modern JavaScript features, but watch out - they add to your bundle size, so only include what you need.

Example:

```js
// Polyfill for Array.includes
if (!Array.prototype.includes) {
  Array.prototype.includes = function(searchElement, fromIndex) {
    return this.indexOf(searchElement, fromIndex) !== -1;
  };
}

```

---

## Q186. 🔧 Data attributes and how to access them in JavaScript

Data attributes store custom data on HTML elements using `data-*` attributes - use `dataset` property to access data attributes, where kebab-case becomes camelCase (`data-user-id` → `userId`). Values are always strings, great for storing component state and configuration.

- **Trade-offs**: The catch is avoiding storing complex data - use JSON if needed, since values are always strings. Data attributes enable custom metadata on elements for component configuration, but watch out - they're part of the HTML5 spec, so older browsers might need polyfills.

Example:

```js
// HTML: <div data-user-id="123" data-role="admin"></div>
const element = document.querySelector('div');
const userId = element.dataset.userId; // '123'
const role = element.dataset.role; // 'admin'
element.dataset.status = 'active'; // Sets data-status="active"

```

---

## Q187. 🔧 Pure functions and side effects

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

## Q188. 🔧 Memory leak and how to detect it

Memory leaks occur when objects remain in memory but are no longer needed, preventing garbage collection - use browser dev tools Memory tab to detect leaks, look for growing heap size over time. Common causes include event listeners, closures, and timers that aren't cleaned up.

- **Trade-offs**: The catch is using `performance.memory` API for monitoring - test with long-running applications to catch leaks early. Memory leaks cause performance degradation over time, requiring careful cleanup, but watch out - some leaks are subtle and only show up after extended use.

Example:

```js
// Memory leak example
const leaks = [];
setInterval(() => {
  leaks.push(new Array(1000000)); // Growing array
}, 1000);

```

---

## Q189. ⚡ How JavaScript handles tail call optimization (TCO)

TCO optimizes recursive function calls by reusing the current stack frame instead of creating new ones - it only works with tail calls where the last operation is the recursive call. It prevents stack overflow for deep recursion, but it's not widely implemented in JavaScript engines.

- **Trade-offs**: The catch is it's not widely implemented in JavaScript engines - use iteration or trampolines as alternatives when TCO isn't available. Consider the recursive pattern carefully for optimization, but watch out - most JavaScript engines don't support TCO, so prefer iteration for deep recursion to avoid stack overflow.

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

---

## 📍 Navigation

<div align="center">

[Promises, Async-Await & Event Loop](5%29%20Promises%2C%20Async-Await%20%26%20Event%20Loop.md) • [Home: README](../README.md) • [Practical JavaScript Questions →](7%29%20Practical%20JavaScript%20Questions.md)

[📋 Cheatsheet](JavaScript%20Interview%20Cheatsheet.md]

</div>

---
