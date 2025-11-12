# 🌐 9. Web Workers, Service Workers & Real-World Topics (Q171–190)

---

## 🧩 Q189. What are Web Workers and how do they work?

### 🧠 Concept

Web Workers run JavaScript in background threads, enabling CPU-intensive tasks without blocking the main thread. They run in separate thread with own global scope and communicate via `postMessage` and `onmessage`.

---

### 💡 Example

```js
const worker = new Worker('worker.js');
worker.postMessage({ data: [1, 2, 3, 4, 5] });
worker.onmessage = e => console.log(e.data);
```

---

### 🔍 Deep Insights

* **Rule:** Run in separate thread with own global scope, communicate via `postMessage` and `onmessage`.
* **Use Case:** Great for heavy computations and data processing.
* **Common Mistake:** Can't access DOM or `window` object.
* **Pro Tip:** Use `terminate()` to stop workers.

---

### ⭐ Senior Takeaway

Workers prevent blocking the main thread, keeping UI responsive.

---

## 🧩 Q190. What can't you access inside a Web Worker?

### 🧠 Concept

Web Workers can't access DOM, `window` object, or parent page's variables due to security and threading constraints. They run in isolated context for security.

---

### 💡 Example

```js
// worker.js - These will cause errors:
// document.getElementById('id'); // ReferenceError
// window.location; // ReferenceError
// parent.someVariable; // ReferenceError
```

---

### 🔍 Deep Insights

* **Rule:** No DOM access (document, window, parent), no direct access to parent page variables.
* **Use Case:** Can't modify UI directly, limited to `self` global scope.
* **Common Mistake:** Must use `postMessage` for communication.
* **Pro Tip:** Workers run in isolated context for security.

---

### ⭐ Senior Takeaway

Isolation prevents race conditions and security issues in multi-threaded code.

---

## 🧩 Q189. How do you communicate between the main thread and a Web Worker?

### 🧠 Concept

Use `postMessage()` to send data and `onmessage` to receive responses between threads. Data is copied, not shared (structured cloning), ensuring data safety across threads.

---

### 💡 Example

```js
worker.postMessage({ type: 'CALCULATE', data: numbers });
worker.onmessage = e => { 
  if (e.data.type === 'RESULT') console.log(e.data.result); 
};
worker.onerror = e => console.error('Worker error:', e);
```

---

### 🔍 Deep Insights

* **Rule:** Data is copied, not shared (structured cloning), use message types for different operations.
* **Use Case:** Handle errors with `onerror` event.
* **Common Mistake:** Consider transferable objects for large data.
* **Pro Tip:** Messages are queued if worker is busy.

---

### ⭐ Senior Takeaway

Structured cloning ensures data safety across threads without shared memory issues.

---

## 🧩 Q190. What are Shared Workers?

### 🧠 Concept

Shared Workers can be accessed by multiple browser contexts (tabs, windows) and persist across page loads. They use `MessagePort` for communication and can coordinate state across multiple tabs.

---

### 💡 Example

```js
const sharedWorker = new SharedWorker('shared-worker.js');
sharedWorker.port.onmessage = e => console.log(e.data);
sharedWorker.port.postMessage({ message: 'hello' });
```

---

### 🔍 Deep Insights

* **Rule:** Shared across multiple browser contexts, use `MessagePort` for communication.
* **Use Case:** Persist until all connections close, great for shared state and coordination.
* **Common Mistake:** More complex than dedicated workers.
* **Pro Tip:** Can coordinate state across multiple tabs.

---

### ⭐ Senior Takeaway

Shared workers enable cross-tab communication and shared state management.

---

## 🧩 Q189. What are Service Workers?

### 🧠 Concept

Service Workers are background scripts that act as network proxies, enabling offline functionality and push notifications. They act as network proxy between app and network, enabling offline functionality with caching.

---

### 💡 Example

```js
self.addEventListener('install', e => {
  e.waitUntil(caches.open('v1').then(cache => 
    cache.addAll(['/', '/styles.css', '/script.js'])));
});
```

---

### 🔍 Deep Insights

* **Rule:** Act as network proxy between app and network, enable offline functionality with caching.
* **Use Case:** Support push notifications and background sync.
* **Common Mistake:** Must be served over HTTPS.
* **Pro Tip:** Lifecycle: install → activate → fetch.

---

### ⭐ Senior Takeaway

Service workers enable Progressive Web Apps (PWAs) with offline capabilities.

---

## 🧩 Q190. What are the lifecycle events of a Service Worker (install, activate, fetch)?

### 🧠 Concept

Service Workers have three main lifecycle events: install (setup), activate (cleanup), and fetch (handle requests). Install runs once when SW is first registered, Activate runs when SW takes control, Fetch runs for every network request.

---

### 💡 Example

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

### 🔍 Deep Insights

* **Rule:** Install: runs once when SW is first registered, Activate: runs when SW takes control, Fetch: runs for every network request.
* **Use Case:** Use `waitUntil()` for async operations.
* **Common Mistake:** Skip waiting forces immediate activation.
* **Pro Tip:** Lifecycle events enable proper cache management.

---

### ⭐ Senior Takeaway

Understanding lifecycle is crucial for SW implementation and cache management.

---

## 🧩 Q189. How do Service Workers enable offline caching?

### 🧠 Concept

Service Workers intercept network requests and serve cached responses when offline. Intercept all network requests, check cache first, fallback to network.

---

### 💡 Example

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

### 🔍 Deep Insights

* **Rule:** Intercept all network requests, check cache first, fallback to network.
* **Use Case:** Cache responses for future use, use cache strategies (cache-first, network-first).
* **Common Mistake:** Handle cache updates and versioning.
* **Pro Tip:** Different caching strategies optimize performance.

---

### ⭐ Senior Takeaway

Caching strategies balance freshness and speed for optimal user experience.

---

## 🧩 Q190. What is the difference between Web Workers and Service Workers?

### 🧠 Concept

Web Workers run background tasks. Service Workers act as network proxies for offline functionality. Web Workers: CPU tasks, one-to-one communication; Service Workers: network proxy, one-to-many.

---

### 💡 Example

```js
// Web Worker - background computation
const worker = new Worker('compute.js');
worker.postMessage(data);

// Service Worker - network proxy
navigator.serviceWorker.register('sw.js');
```

---

### 🔍 Deep Insights

* **Rule:** Web Workers: CPU tasks, one-to-one communication; Service Workers: network proxy, one-to-many.
* **Use Case:** Web Workers: dedicated or shared; Service Workers: persistent, event-driven.
* **Common Mistake:** Different use cases and capabilities.
* **Pro Tip:** Each serves different purposes in web apps.

---

### ⭐ Senior Takeaway

Choose based on use case: computation vs. network/caching needs.

---

## 🧩 Q189. How do you handle background sync or push notifications?

### 🧠 Concept

Use Service Worker events for background sync and push notifications when the app isn't active. Background sync runs when connection restored, push events trigger when server sends notification.

---

### 💡 Example

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

### 🔍 Deep Insights

* **Rule:** Background sync runs when connection restored, push events trigger when server sends notification.
* **Use Case:** Use `waitUntil()` for async operations, handle user interactions with notification clicks.
* **Common Mistake:** Consider user permissions and preferences.
* **Pro Tip:** Push notifications enable real-time updates.

---

### ⭐ Senior Takeaway

Background sync improves offline experience by queuing actions for later.

---

## 🧩 Q190. How do you unregister a Service Worker?

### 🧠 Concept

Use `navigator.serviceWorker.getRegistrations()` to find and unregister Service Workers. `unregister()` returns a promise and removes SW from browser's registry.

---

### 💡 Example

```js
navigator.serviceWorker.getRegistrations().then(regs => 
  regs.forEach(reg => reg.unregister()));
```

---

### 🔍 Deep Insights

* **Rule:** `unregister()` returns a promise, removes SW from browser's registry.
* **Use Case:** May take time to fully remove.
* **Common Mistake:** Consider user confirmation before unregistering.
* **Pro Tip:** Test unregistration in different scenarios.

---

### ⭐ Senior Takeaway

Unregistering is needed for updates and debugging Service Worker issues.

---

---

---

## 🧩 Q189. What is event delegation?

### 🧠 Concept

Event delegation attaches a single event listener to a parent element to handle events from child elements. It reduces memory usage and improves performance, working with dynamically added elements.

---

### 💡 Example

```js
document.addEventListener('click', e => {
  if (e.target.matches('.button')) {
    console.log('Button clicked:', e.target.textContent);
  }
});
```

---

### 🔍 Deep Insights

* **Rule:** Reduces memory usage and improves performance, works with dynamically added elements.
* **Use Case:** Use `e.target` to identify the actual clicked element, great for lists and tables with many interactive elements.
* **Common Mistake:** Consider event bubbling vs capturing.
* **Pro Tip:** Single listener handles multiple child elements.

---

### ⭐ Senior Takeaway

Event delegation is more efficient than multiple listeners for dynamic content.

---

## 🧩 Q190. What are event bubbling and capturing?

### 🧠 Concept

Event bubbling propagates from child to parent; capturing propagates from parent to child. Three phases: capture → target → bubble.

---

### 💡 Example

```js
// Capturing phase (parent to child)
element.addEventListener('click', handler, true);

// Bubbling phase (child to parent) - default
element.addEventListener('click', handler, false);
```

---

### 🔍 Deep Insights

* **Rule:** Three phases: capture → target → bubble.
* **Use Case:** Use `e.stopPropagation()` to stop propagation, use `e.stopImmediatePropagation()` to stop all handlers.
* **Common Mistake:** Capturing is less commonly used.
* **Pro Tip:** Event delegation relies on bubbling.

---

### ⭐ Senior Takeaway

Understanding propagation helps with event handling and delegation patterns.

---

## 🧩 Q189. What is a shadow DOM?

### 🧠 Concept

Shadow DOM encapsulates DOM and CSS, creating isolated components that don't interfere with the main document. It creates encapsulated DOM subtree, styles don't leak out or in.

---

### 💡 Example

```js
const host = document.getElementById('host');
const shadow = host.attachShadow({ mode: 'open' });
shadow.innerHTML = `
  <style>p { color: red; }</style>
  <p>This is isolated from main document</p>
`;
```

---

### 🔍 Deep Insights

* **Rule:** Creates encapsulated DOM subtree, styles don't leak out or in.
* **Use Case:** Used by Web Components, `mode: 'open'` allows external access.
* **Common Mistake:** Great for reusable component libraries.
* **Pro Tip:** Enables true component encapsulation.

---

### ⭐ Senior Takeaway

Shadow DOM prevents style conflicts and enables true component isolation.

---

## 🧩 Q190. What is the difference between `innerHTML`, `textContent`, and `innerText`?

### 🧠 Concept

`innerHTML` includes HTML tags; `textContent` gets all text; `innerText` gets visible text respecting CSS. Choose based on need: HTML vs text vs visible text.

---

### 💡 Example

```js
const div = document.createElement('div');
div.innerHTML = '<p>Hello <span style="display:none">hidden</span> World</p>';
div.innerHTML; // '<p>Hello <span style="display:none">hidden</span> World</p>'
div.textContent; // 'Hello hidden World'
div.innerText; // 'Hello World'
```

---

### 🔍 Deep Insights

* **Rule:** `innerHTML`: includes HTML markup, can execute scripts; `textContent`: all text content, safer, faster; `innerText`: visible text only, respects CSS, slower.
* **Use Case:** Use `textContent` for security and performance.
* **Common Mistake:** `innerHTML` can cause XSS if not sanitized.
* **Pro Tip:** Prefer `textContent` to avoid XSS attacks.

---

### ⭐ Senior Takeaway

Choose based on need: HTML vs text vs visible text, prioritizing security.

---

## 🧩 Q189. What is the difference between `for...in` and `for...of`?

### 🧠 Concept

`for...in` iterates over enumerable property names; `for...of` iterates over iterable values. `for...in`: property names, includes inherited properties; `for...of`: values, works with iterables.

---

### 💡 Example

```js
const arr = [1, 2, 3];
arr.custom = 'property';

for (let key in arr) console.log(key); // '0', '1', '2', 'custom'
for (let value of arr) console.log(value); // 1, 2, 3
```

---

### 🔍 Deep Insights

* **Rule:** `for...in`: property names, includes inherited properties; `for...of`: values, works with iterables (arrays, strings, maps).
* **Use Case:** Use `for...of` for arrays and iterables, use `for...in` with `hasOwnProperty` for object properties.
* **Common Mistake:** `for...of` is generally preferred for arrays.
* **Pro Tip:** `for...of` is more efficient for arrays.

---

### ⭐ Senior Takeaway

Choose based on whether you need keys or values from your data structure.

---

## 🧩 Q190. What is a polyfill and when would you use one?

### 🧠 Concept

A polyfill is code that implements a feature in older browsers that don't natively support it. It provides missing functionality in older browsers.

---

### 💡 Example

```js
// Polyfill for Array.includes
if (!Array.prototype.includes) {
  Array.prototype.includes = function(searchElement, fromIndex) {
    return this.indexOf(searchElement, fromIndex) !== -1;
  };
}
```

---

### 🔍 Deep Insights

* **Rule:** Provides missing functionality in older browsers.
* **Use Case:** Use feature detection before adding polyfills, consider bundle size impact.
* **Common Mistake:** Use tools like Babel and core-js for automatic polyfilling.
* **Pro Tip:** Test thoroughly in target browsers.

---

### ⭐ Senior Takeaway

Polyfills enable backward compatibility for modern JavaScript features.

---

## 🧩 Q189. What are data attributes and how do you access them in JavaScript?

### 🧠 Concept

Data attributes store custom data on HTML elements using `data-*` attributes. Use `dataset` property to access data attributes, kebab-case becomes camelCase.

---

### 💡 Example

```js
// HTML: <div data-user-id="123" data-role="admin"></div>
const element = document.querySelector('div');
const userId = element.dataset.userId; // '123'
const role = element.dataset.role; // 'admin'
element.dataset.status = 'active'; // Sets data-status="active"
```

---

### 🔍 Deep Insights

* **Rule:** Use `dataset` property to access data attributes, kebab-case becomes camelCase (`data-user-id` → `userId`).
* **Use Case:** Values are always strings, great for storing component state and configuration.
* **Common Mistake:** Avoid storing complex data, use JSON if needed.
* **Pro Tip:** Data attributes are part of HTML5 spec.

---

### ⭐ Senior Takeaway

Data attributes enable custom metadata on elements for component configuration.

---

## 🧩 Q190. What are pure functions and side effects?

### 🧠 Concept

Pure functions always return the same output for the same input and have no side effects. They're predictable and testable, making code easier to reason about.

---

### 💡 Example

```js
// Pure function
const add = (a, b) => a + b;

// Impure function (has side effects)
let counter = 0;
const increment = () => ++counter;
```

---

### 🔍 Deep Insights

* **Rule:** Pure functions are predictable and testable.
* **Use Case:** Side effects include: DOM manipulation, API calls, console.log.
* **Common Mistake:** Prefer pure functions when possible.
* **Pro Tip:** Use pure functions for reducers and transformations, side effects are necessary but should be isolated.

---

### ⭐ Senior Takeaway

Pure functions are easier to test and reason about than impure functions.

---

## 🧩 Q189. What is a memory leak and how can you detect it?

### 🧠 Concept

Memory leaks occur when objects remain in memory but are no longer needed, preventing garbage collection. Use browser dev tools Memory tab to detect leaks, look for growing heap size over time.

---

### 💡 Example

```js
// Memory leak example
const leaks = [];
setInterval(() => {
  leaks.push(new Array(1000000)); // Growing array
}, 1000);
```

---

### 🔍 Deep Insights

* **Rule:** Use browser dev tools Memory tab to detect leaks, look for growing heap size over time.
* **Use Case:** Common causes: event listeners, closures, timers.
* **Common Mistake:** Use `performance.memory` API for monitoring.
* **Pro Tip:** Test with long-running applications.

---

### ⭐ Senior Takeaway

Memory leaks cause performance degradation over time, requiring careful cleanup.

---

## 🧩 Q190. How does JavaScript handle tail call optimization (TCO)?

### 🧠 Concept

TCO optimizes recursive function calls by reusing the current stack frame instead of creating new ones. Only works with tail calls (last operation is the recursive call).

---

### 💡 Example

```js
// Tail recursive function
const factorial = (n, acc = 1) => 
  n <= 1 ? acc : factorial(n - 1, n * acc);

// Non-tail recursive (not optimized)
const factorialBad = n => 
  n <= 1 ? 1 : n * factorialBad(n - 1);
```

---

### 🔍 Deep Insights

* **Rule:** Only works with tail calls (last operation is the recursive call).
* **Use Case:** Prevents stack overflow for deep recursion.
* **Common Mistake:** Not widely implemented in JavaScript engines.
* **Pro Tip:** Use iteration or trampolines as alternatives.

---

### ⭐ Senior Takeaway

Consider the recursive pattern carefully for optimization, prefer iteration when TCO isn't available.

---
