# 🌐 9. Web Workers & Service Workers (Q111–120)

---

## 111) What are Web Workers and how do they work?

Web Workers run JavaScript in background threads, enabling CPU-intensive tasks without blocking the main thread.

```js
const worker = new Worker('worker.js');
worker.postMessage({ data: [1, 2, 3, 4, 5] });
worker.onmessage = e => console.log(e.data);
```

- **Core Concept**: Run in separate thread with own global scope, communicate via `postMessage` and `onmessage`
- **Real-World Use**: Great for heavy computations and data processing
- **Common Mistake**: Can't access DOM or `window` object
- **Advanced Feature**: Use `terminate()` to stop workers
- **Interview Tip**: Explain that workers prevent blocking the main thread

---

## 112) What can't you access inside a Web Worker?

Web Workers can't access DOM, `window` object, or parent page's variables due to security and threading constraints.

```js
// worker.js - These will cause errors:
// document.getElementById('id'); // ReferenceError
// window.location; // ReferenceError
// parent.someVariable; // ReferenceError
```

- **Core Limitation**: No DOM access (document, window, parent), no direct access to parent page variables
- **Real-World Impact**: Can't modify UI directly, limited to `self` global scope
- **Common Mistake**: Must use `postMessage` for communication
- **Advanced Feature**: Workers run in isolated context for security
- **Interview Tip**: Explain that isolation prevents race conditions and security issues

---

## 113) How do you communicate between the main thread and a Web Worker?

Use `postMessage()` to send data and `onmessage` to receive responses between threads.

```js
worker.postMessage({ type: 'CALCULATE', data: numbers });
worker.onmessage = e => { if (e.data.type === 'RESULT') console.log(e.data.result); };
worker.onerror = e => console.error('Worker error:', e);
```

- **Core Method**: Data is copied, not shared (structured cloning), use message types for different operations
- **Real-World Use**: Handle errors with `onerror` event
- **Common Mistake**: Consider transferable objects for large data
- **Advanced Feature**: Messages are queued if worker is busy
- **Interview Tip**: Explain that structured cloning ensures data safety across threads

---

## 114) What are Shared Workers?

Shared Workers can be accessed by multiple browser contexts (tabs, windows) and persist across page loads.

```js
const sharedWorker = new SharedWorker('shared-worker.js');
sharedWorker.port.onmessage = e => console.log(e.data);
sharedWorker.port.postMessage({ message: 'hello' });
```

- **Core Concept**: Shared across multiple browser contexts, use `MessagePort` for communication
- **Real-World Use**: Persist until all connections close, great for shared state and coordination
- **Common Mistake**: More complex than dedicated workers
- **Advanced Feature**: Can coordinate state across multiple tabs
- **Interview Tip**: Explain that shared workers enable cross-tab communication

---

## 115) What are Service Workers?

Service Workers are background scripts that act as network proxies, enabling offline functionality and push notifications.

```js
self.addEventListener('install', e => {
  e.waitUntil(caches.open('v1').then(cache => cache.addAll(['/', '/styles.css', '/script.js'])));
});
```

- **Core Purpose**: Act as network proxy between app and network, enable offline functionality with caching
- **Real-World Use**: Support push notifications and background sync
- **Common Mistake**: Must be served over HTTPS
- **Advanced Feature**: Lifecycle: install → activate → fetch
- **Interview Tip**: Explain that service workers enable Progressive Web Apps (PWAs)

---

## 116) What are the lifecycle events of a Service Worker (install, activate, fetch)?

Service Workers have three main lifecycle events: install (setup), activate (cleanup), and fetch (handle requests).

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

- **Core Events**: Install: runs once when SW is first registered, Activate: runs when SW takes control, Fetch: runs for every network request
- **Real-World Use**: Use `waitUntil()` for async operations
- **Common Mistake**: Skip waiting forces immediate activation
- **Advanced Feature**: Lifecycle events enable proper cache management
- **Interview Tip**: Explain that understanding lifecycle is crucial for SW implementation

---

## 117) How do Service Workers enable offline caching?

Service Workers intercept network requests and serve cached responses when offline.

```js
self.addEventListener('fetch', e => {
  e.respondWith(caches.match(e.request).then(response => response || fetch(e.request).then(fetchResponse => {
    caches.open('v1').then(cache => cache.put(e.request, fetchResponse.clone())); return fetchResponse;
  })));
});
```

- **Core Strategy**: Intercept all network requests, check cache first, fallback to network
- **Real-World Use**: Cache responses for future use, use cache strategies (cache-first, network-first)
- **Common Mistake**: Handle cache updates and versioning
- **Advanced Feature**: Different caching strategies optimize performance
- **Interview Tip**: Explain that caching strategies balance freshness and speed

---

## 118) What is the difference between Web Workers and Service Workers?

Web Workers run background tasks. Service Workers act as network proxies for offline functionality.

```js
// Web Worker - background computation
const worker = new Worker('compute.js');
worker.postMessage(data);

// Service Worker - network proxy
navigator.serviceWorker.register('sw.js');
```

- **Core Difference**: Web Workers: CPU tasks, one-to-one communication; Service Workers: network proxy, one-to-many
- **Real-World Use**: Web Workers: dedicated or shared; Service Workers: persistent, event-driven
- **Common Mistake**: Different use cases and capabilities
- **Advanced Feature**: Each serves different purposes in web apps
- **Interview Tip**: Explain that choose based on use case: computation vs. network/caching

---

## 119) How do you handle background sync or push notifications?

Use Service Worker events for background sync and push notifications when the app isn't active.

```js
self.addEventListener('sync', e => { if (e.tag === 'background-sync') e.waitUntil(doBackgroundWork()); });
self.addEventListener('push', e => { const data = e.data.json(); self.registration.showNotification(data.title, { body: data.body }); });
```

- **Core Features**: Background sync runs when connection restored, push events trigger when server sends notification
- **Real-World Use**: Use `waitUntil()` for async operations, handle user interactions with notification clicks
- **Common Mistake**: Consider user permissions and preferences
- **Advanced Feature**: Push notifications enable real-time updates
- **Interview Tip**: Explain that background sync improves offline experience

---

## 120) How do you unregister a Service Worker?

Use `navigator.serviceWorker.getRegistrations()` to find and unregister Service Workers.

```js
navigator.serviceWorker.getRegistrations().then(regs => regs.forEach(reg => reg.unregister()));
```

- **Core Method**: `unregister()` returns a promise, removes SW from browser's registry
- **Real-World Use**: May take time to fully remove
- **Common Mistake**: Consider user confirmation before unregistering
- **Advanced Feature**: Test unregistration in different scenarios
- **Interview Tip**: Explain that unregistering is needed for updates and debugging

---
