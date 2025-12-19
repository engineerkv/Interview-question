# 📱 Offline Support

---

## 📍 Navigation

<div align="center">

[← Previous: Accessibility](21%29%20Accessibility.md) • [Home: Questions Index](question.md) • [Next: Patterns →](23%29%20Patterns.md)

[📋 Cheatsheet](FE-System-Design%20Interview%20Cheatsheet.md)

</div>

---

---

## 1. 💡 Service Workers

Service workers are background scripts that run separately from your web page and can intercept network requests, cache resources, and handle push notifications. Service workers are the core building block for offline-first web apps. Understanding service workers is essential for building Progressive Web Apps (PWAs) and providing reliable experiences even when network connectivity is poor.

### 🔹 How Service Workers Work

### 🔹 Lifecycle

1. **Register** from the page:

   ```javascript
   navigator.serviceWorker.register('/sw.js');

   ```

2. **Install** – cache initial assets in `install` event

3. **Activate** – clean up old caches in `activate` event

4. **Fetch** – intercept network requests and respond from cache or network

📌 **In simple terms**: A service worker is a programmable proxy between your app and the network for your origin.

### 🔹 Common Strategies

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

### 🔹 💡 Progressive Web Applications (PWAs)

Progressive Web Apps are web apps that use modern capabilities like service workers and manifests to deliver an app-like experience: installable, offline-capable, and fast.

---

### 🔹 💡 Core requirements

* **HTTPS** – secure origin

* **Service worker** – offline and caching

* **Web App Manifest** – metadata (name, icons, theme color, start URL)

* **Responsive design** – works across devices

📌 **In simple terms**: A PWA is a website that behaves like a native app—installable, offline-aware, and fast.

### 🔹 UX Characteristics

* Installable icon on home screen / app launcher

* Fullscreen or standalone window

* Works offline or on flaky networks for key flows

* Fast startup thanks to caching

---

## ⭐ Summary — 10-second Interview Version

> "Offline support includes service workers (background scripts that intercept network requests and cache resources) and PWAs (installable web apps with offline capabilities). Service workers enable caching strategies (cache-first, network-first, stale-while-revalidate) and offline functionality. PWAs require HTTPS, service worker, web app manifest, and responsive design to deliver app-like experiences."

---

---

## 📍 Navigation

<div align="center">

[← Previous: Accessibility](21%29%20Accessibility.md) • [Home: Questions Index](question.md) • [Next: Patterns →](23%29%20Patterns.md)

[📋 Cheatsheet](FE-System-Design%20Interview%20Cheatsheet.md)

</div>

---
