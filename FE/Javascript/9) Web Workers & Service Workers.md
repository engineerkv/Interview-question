# 🌐 9. Web Workers & Service Workers (Q120–129)

---

## 120) What are Web Workers and how do they work?

Concept:
Web Workers run JavaScript in background threads, enabling CPU-intensive tasks without blocking the main thread.

Example:
```js
// main.js
const worker = new Worker('worker.js');
worker.postMessage({ data: [1, 2, 3, 4, 5] });
worker.onmessage = e => console.log(e.data);

// worker.js
self.onmessage = e => {
  const result = e.data.data.reduce((sum, num) => sum + num, 0);
  self.postMessage({ result });
};
```

Deep Insight:
- Run in separate thread with own global scope
- Communicate via `postMessage` and `onmessage`
- Can't access DOM or `window` object
- Great for heavy computations and data processing
- Use `terminate()` to stop workers

---

## 121) What can't you access inside a Web Worker?

Concept:
Web Workers can't access DOM, `window` object, or parent page's variables due to security and threading constraints.

Example:
```js
// worker.js - These will cause errors:
// document.getElementById('id'); // ReferenceError
// window.location; // ReferenceError
// parent.someVariable; // ReferenceError
```

Deep Insight:
- No DOM access (document, window, parent)
- No direct access to parent page variables
- Can't modify UI directly
- Limited to `self` global scope
- Must use `postMessage` for communication

---

## 122) How do you communicate between the main thread and a Web Worker?

Concept:
Use `postMessage()` to send data and `onmessage` to receive responses between threads.

Example:
```js
// Main thread
worker.postMessage({ type: 'CALCULATE', data: numbers });
worker.onmessage = e => {
  if (e.data.type === 'RESULT') {
    console.log(e.data.result);
  }
```

Deep Insight:
- Data is copied, not shared (structured cloning)
- Use message types for different operations
- Handle errors with `onerror` event
- Consider transferable objects for large data
- Messages are queued if worker is busy

---

## 123) What are Shared Workers?

Concept:
Shared Workers can be accessed by multiple browser contexts (tabs, windows) and persist across page loads.

Example:
```js
// shared-worker.js
let connections = 0;
self.onconnect = e => {
  const port = e.ports[0];
  connections++;
  port.postMessage({ connections });
```

Deep Insight:
- Shared across multiple browser contexts
- Use `MessagePort` for communication
- Persist until all connections close
- Great for shared state and coordination
- More complex than dedicated workers

---

## 124) What are Service Workers?

Concept:
Service Workers are background scripts that act as network proxies, enabling offline functionality and push notifications.

Example:
```js
// sw.js
self.addEventListener('install', e => {
  e.waitUntil(
    caches.open('v1').then(cache => 
      cache.addAll(['/', '/styles.css', '/script.js'])
    )
```

Deep Insight:
- Act as network proxy between app and network
- Enable offline functionality with caching
- Support push notifications and background sync
- Must be served over HTTPS
- Lifecycle: install → activate → fetch

---

## 125) What are the lifecycle events of a Service Worker (install, activate, fetch)?

Concept:
Service Workers have three main lifecycle events: install (setup), activate (cleanup), and fetch (handle requests).

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

Deep Insight:
- Install: runs once when SW is first registered
- Activate: runs when SW takes control
- Fetch: runs for every network request
- Use `waitUntil()` for async operations
- Skip waiting forces immediate activation

---

## 126) How do Service Workers enable offline caching?

Concept:
Service Workers intercept network requests and serve cached responses when offline.

Example:
```js
self.addEventListener('fetch', e => {
  e.respondWith(
    caches.match(e.request)
      .then(response => {
        if (response) return response;
        return fetch(e.request).then(fetchResponse => {
          const responseClone = fetchResponse.clone();
          caches.open('v1').then(cache => {
            cache.put(e.request, responseClone);
          });
          return fetchResponse;
        });
      })
  );
});
```

Deep Insight:
- Intercept all network requests
- Check cache first, fallback to network
- Cache responses for future use
- Use cache strategies (cache-first, network-first)
- Handle cache updates and versioning

---

## 127) What is the difference between Web Workers and Service Workers?

Concept:
Web Workers run background tasks; Service Workers act as network proxies for offline functionality.

Example:
```js
// Web Worker - background computation
const worker = new Worker('compute.js');
worker.postMessage(data);

// Service Worker - network proxy
navigator.serviceWorker.register('sw.js');
```

Deep Insight:
- Web Workers: CPU tasks, one-to-one communication
- Service Workers: network proxy, one-to-many
- Web Workers: dedicated or shared
- Service Workers: persistent, event-driven
- Different use cases and capabilities

---

## 128) How do you handle background sync or push notifications?

Concept:
Use Service Worker events for background sync and push notifications when the app isn't active.

Example:
```js
// Background sync
self.addEventListener('sync', e => {
  if (e.tag === 'background-sync') {
    e.waitUntil(doBackgroundWork());
  }
});
```

Deep Insight:
- Background sync runs when connection restored
- Push events trigger when server sends notification
- Use `waitUntil()` for async operations
- Handle user interactions with notification clicks
- Consider user permissions and preferences

---

## 129) How do you unregister a Service Worker?

Concept:
Use `navigator.serviceWorker.getRegistrations()` to find and unregister Service Workers.

Example:
```js
navigator.serviceWorker.getRegistrations().then(registrations => {
  registrations.forEach(registration => {
    registration.unregister();
  });
});

// Push notifications
self.addEventListener('push', e => {
  const options = {
    body: e.data.text(),
    icon: '/icon.png',
    badge: '/badge.png'
  };
  e.waitUntil(
    self.registration.showNotification('Push Notification', options)
  );
});
```

Deep Insight:
- `unregister()` returns a promise
- Removes SW from browser's registry
- May take time to fully remove
- Consider user confirmation before unregistering
- Test unregistration in different scenarios
