# 📱 Offline Support

---

## 📍 Navigation

<div align="center">

[← Previous: Accessibility](21%29%20Accessibility.md) • [Home: Questions Index](question.md) • [Next: Patterns →](23%29%20Patterns.md)

[📋 Cheatsheet](FE-System-Design%20Interview%20Cheatsheet.md)

</div>

---

---

## Q98. Service Workers

Service workers are background scripts that run separately from your web page and can intercept network requests, cache resources, and handle push notifications. Service workers are the core building block for offline-first web apps. Understanding service workers is essential for building Progressive Web Apps (PWAs) and providing reliable experiences even when network connectivity is poor.

---

## 1. How service workers work

### 🔹 Lifecycle

1. **Register** from the page:
   ```javascript
   navigator.serviceWorker.register('/sw.js');
   ```

2. **Install** – cache initial assets in `install` event

3. **Activate** – clean up old caches in `activate` event

4. **Fetch** – intercept network requests and respond from cache or network

📌 **In simple terms**: A service worker is a programmable proxy between your app and the network for your origin.

---

## 2. Common strategies

* **Cache-first** – for static assets (icons, JS, CSS)

* **Network-first** – for dynamic data with offline fallback

* **Stale-while-revalidate** – serve from cache, update in background

---

## ⭐ Summary — 10-second Interview Version

> "Service workers run in the background and intercept fetches so we can cache assets and data, enable offline usage, and control how the app behaves when the network is slow or unavailable."

---

## ⭐ Extra Points (If Interviewer Asks More)

### How do you handle updates?

Use a versioned cache, delete old caches in `activate`, and show a “New version available” toast when a new service worker is ready to take over.

---

## Q99. Progressive Web Applications (PWAs)

Progressive Web Apps are web apps that use modern capabilities like service workers and manifests to deliver an app-like experience: installable, offline-capable, and fast.

---

## 1. Core requirements

* **HTTPS** – secure origin

* **Service worker** – offline and caching

* **Web App Manifest** – metadata (name, icons, theme color, start URL)

* **Responsive design** – works across devices

📌 **In simple terms**: A PWA is a website that behaves like a native app—installable, offline-aware, and fast.

---

## 2. UX characteristics

* Installable icon on home screen / app launcher

* Fullscreen or standalone window

* Works offline or on flaky networks for key flows

* Fast startup thanks to caching

---

## ⭐ Summary — 10-second Interview Version

> "A PWA is a web app that uses HTTPS, a service worker, and a manifest to become installable and offline-capable. It gives users an app-like experience without going through app stores."

---

## ⭐ Extra Points (If Interviewer Asks More)

### How do you decide what to make available offline?

Identify critical user journeys (read last data, create drafts, view cached content) and ensure required assets and API responses are cached and synchronized when back online.

---

---

## 📍 Navigation

<div align="center">

[17) Accessibility.md](17%29%20Accessibility.md) • [Questions Index](question.md) • [19) Patterns.md →](19%29%20Patterns.md)

[FE-System-Design Cheatsheet](FE-System-Design%20Interview%20Cheatsheet.md]

</div>

---
