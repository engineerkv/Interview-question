# 🚀 5. HTML5 Features & APIs (Q61–75)

---

## 🧩 Q61. What are the new semantic elements in HTML5?

### 🧠 Concept

HTML5 introduced semantic elements that provide meaning to document structure, improving accessibility and SEO. Semantic HTML5 elements replace generic divs with meaningful structure.

---

### 💡 Example

```html
<body>
  <header>
    <h1>Site Title</h1>
  </header>
  <nav>
    <ul>
      <li><a href="/">Home</a></li>
      <li><a href="/about">About</a></li>
    </ul>
  </nav>
  <main>
    <article>
      <h2>Article Title</h2>
      <p>Content...</p>
    </article>
  </main>
  <footer>
    <p>Copyright 2024</p>
  </footer>
</body>
```

---

### 🔍 Deep Insights

* **Rule:** header, nav, main, article, section, aside, footer provide semantic meaning.
* **Use Case:** Better accessibility for screen readers, enhanced SEO through content hierarchy.
* **Common Mistake:** Creates navigable regions for screen reader users.
* **Pro Tip:** Provides default styling and behavior, works with CSS.

---

### ⭐ Senior Takeaway

Semantic HTML5 elements replace generic divs with meaningful structure.

---

## 🧩 Q62. What is the Canvas API and how do you use it?

### 🧠 Concept

Canvas API provides a 2D drawing surface for creating graphics, animations, and interactive content. Canvas is for pixel-based graphics, SVG is for vector graphics.

---

### 💡 Example

```html
<canvas id="myCanvas" width="400" height="200"></canvas>
<script>
const canvas = document.getElementById('myCanvas');
const ctx = canvas.getContext('2d');
ctx.fillStyle = 'blue';
ctx.fillRect(10, 10, 100, 50);
</script>
```

---

### 🔍 Deep Insights

* **Rule:** 2D drawing surface for graphics, animations, games, or visualizations.
* **Use Case:** Games, charts, image editing, or any pixel-based graphics.
* **Common Mistake:** Requires JavaScript for drawing, no direct HTML drawing.
* **Pro Tip:** Performance depends on canvas size and complexity of drawings.

---

### ⭐ Senior Takeaway

Canvas is for pixel-based graphics, SVG is for vector graphics.

---

## 🧩 Q63. What is the Drag and Drop API?

### 🧠 Concept

HTML5 Drag and Drop API allows elements to be draggable and provides events for drop handling. Drag and drop requires JavaScript event handling.

---

### 💡 Example

```html
<div id="drag-source" draggable="true" ondragstart="dragStart(event)">Drag me!</div>
<div id="drop-target" ondrop="drop(event)" ondragover="allowDrop(event)">Drop here</div>
<script>
function dragStart(e) { 
  e.dataTransfer.setData('text', e.target.id); 
}
function allowDrop(e) { 
  e.preventDefault(); 
}
function drop(e) { 
  e.preventDefault(); 
  var data = e.dataTransfer.getData('text'); 
}
</script>
```

---

### 🔍 Deep Insights

* **Rule:** Set `draggable="true"`, handle `dragstart`, `dragover`, and `drop` events.
* **Use Case:** File uploads, drag-and-drop interfaces, or reorderable lists.
* **Common Mistake:** Use `dataTransfer` to pass data between drag source and drop target.
* **Pro Tip:** Prevent default behavior for drop zones, provide visual feedback.

---

### ⭐ Senior Takeaway

Drag and drop requires JavaScript event handling.

---

## 🧩 Q64. What is the Geolocation API?

### 🧠 Concept

Geolocation API provides access to device location information with user permission. Geolocation requires HTTPS in production, respects user privacy.

---

### 💡 Example

```html
<button onclick="getLocation()">Get My Location</button>
<div id="location"></div>
<script>
function getLocation() {
  if (navigator.geolocation) {
    navigator.geolocation.getCurrentPosition((pos) => {
      document.getElementById('location').textContent = 
        `Lat: ${pos.coords.latitude}, Lon: ${pos.coords.longitude}`;
    });
  }
}
</script>
```

---

### 🔍 Deep Insights

* **Rule:** Get user's geographic location with permission.
* **Use Case:** Location-based services, maps, weather apps, or nearby searches.
* **Common Mistake:** Requires user permission, important for privacy considerations.
* **Pro Tip:** Provides latitude, longitude, accuracy, and optional altitude.

---

### ⭐ Senior Takeaway

Geolocation requires HTTPS in production, respects user privacy.

---

## 🧩 Q65. What is Web Storage (localStorage and sessionStorage)?

### 🧠 Concept

Web Storage API provides local storage (persistent) and session storage (temporary) for client-side data. localStorage is synchronous, sessionStorage is tab-specific.

---

### 💡 Example

```html
<input type="text" id="username" placeholder="Enter username">
<button onclick="saveData()">Save</button>
<button onclick="loadData()">Load</button>
<script>
function saveData() { 
  localStorage.setItem('username', document.getElementById('username').value); 
}
function loadData() { 
  document.getElementById('username').value = localStorage.getItem('username') || ''; 
}
</script>
```

---

### 🔍 Deep Insights

* **Rule:** `localStorage` persists across sessions, `sessionStorage` clears when tab closes.
* **Use Case:** User preferences, form data, or any client-side data storage.
* **Common Mistake:** 5-10MB per origin, data stored as strings (use JSON for objects).
* **Pro Tip:** Blocks main thread, consider using IndexedDB for large data.

---

### ⭐ Senior Takeaway

localStorage is synchronous, sessionStorage is tab-specific.

---

## 🧩 Q66. What is the History API?

### 🧠 Concept

History API allows manipulation of browser history for single-page applications and custom navigation. History API enables SPAs with proper browser navigation.

---

### 💡 Example

```html
<button onclick="goToPage('/home')">Home</button>
<button onclick="goBack()">Back</button>
<div id="content">Home Page Content</div>
<script>
function goToPage(page) {
  history.pushState({page}, '', page);
  document.getElementById('content').textContent = page + ' Page Content';
}
function goBack() { 
  history.back(); 
}
window.addEventListener('popstate', (e) => {
  document.getElementById('content').textContent = e.state?.page + ' Page Content';
});
</script>
```

---

### 🔍 Deep Insights

* **Rule:** Manipulate browser history without page reloads.
* **Use Case:** Single-page applications, custom navigation, or bookmarkable URLs.
* **Common Mistake:** `pushState()` adds history entry, `replaceState()` modifies current entry.
* **Pro Tip:** `popstate` event handles back/forward button navigation.

---

### ⭐ Senior Takeaway

History API enables SPAs with proper browser navigation.

---

## 🧩 Q67. What are Offline Web Apps?

### 🧠 Concept

Use Service Workers and Cache API to create web applications that work offline by caching resources. Service Workers require HTTPS, enable offline-first apps.

---

### 💡 Example

```html
<script>
if ('serviceWorker' in navigator) {
  navigator.serviceWorker.register('/sw.js')
    .then(reg => console.log('SW registered'))
    .catch(err => console.log('SW registration failed'));
}
</script>
```

---

### 🔍 Deep Insights

* **Rule:** Service Workers run in background, Cache API stores resources.
* **Use Case:** Offline functionality, faster loading, or reduced server load.
* **Common Mistake:** Install event caches resources, fetch event serves cached content.
* **Pro Tip:** Falls back to network when cache misses, improves reliability.

---

### ⭐ Senior Takeaway

Service Workers require HTTPS, enable offline-first apps.

---

## 🧩 Q68. What are Web Workers?

### 🧠 Concept

Web Workers allow JavaScript to run in background threads, preventing UI blocking for heavy computations. Web Workers are for CPU-intensive tasks, not DOM manipulation.

---

### 💡 Example

```html
<button onclick="startWorker()">Start Heavy Task</button>
<div id="result"></div>
<script>
let worker;
function startWorker() {
  worker = new Worker('worker.js');
  worker.onmessage = (e) => 
    document.getElementById('result').textContent = e.data;
  worker.postMessage('start');
}
</script>
```

---

### 🔍 Deep Insights

* **Rule:** Run JavaScript in background threads, keep UI responsive.
* **Use Case:** Heavy computations, image processing, or data parsing.
* **Common Mistake:** Can't access DOM or window object, communicate via postMessage.
* **Pro Tip:** Prevents UI blocking, improves user experience.

---

### ⭐ Senior Takeaway

Web Workers are for CPU-intensive tasks, not DOM manipulation.

---

## 🧩 Q69. What is the Intersection Observer API?

### 🧠 Concept

Intersection Observer API efficiently detects when elements enter or exit the viewport. Intersection Observer is better than scroll events for performance.

---

### 💡 Example

```html
<div class="section">Section 1</div>
<div class="section">Section 2</div>
<script>
const observer = new IntersectionObserver((entries) => {
  entries.forEach(entry => {
    if (entry.isIntersecting) 
      entry.target.style.backgroundColor = 'yellow';
  });
}, { threshold: 0.5 });
document.querySelectorAll('.section').forEach(section => 
  observer.observe(section)
);
</script>
```

---

### 🔍 Deep Insights

* **Rule:** Efficiently detect when elements enter or exit viewport.
* **Use Case:** Lazy loading images, infinite scrolling, or scroll animations.
* **Common Mistake:** More efficient than scroll event listeners, better performance.
* **Pro Tip:** Configurable root margin and threshold for fine-tuned detection.

---

### ⭐ Senior Takeaway

Intersection Observer is better than scroll events for performance.

---

## 🧩 Q70. What are Web Components?

### 🧠 Concept

Web Components are a set of web platform APIs that allow creating reusable custom elements. Web Components are the native browser standard for components.

---

### 💡 Example

```html
<my-button text="Click me!" color="blue"></my-button>
<script>
class MyButton extends HTMLElement {
  constructor() {
    super();
    this.attachShadow({ mode: 'open' }).innerHTML = 
      `<button style="color: ${this.getAttribute('color')}">${this.getAttribute('text')}</button>`;
  }
}
customElements.define('my-button', MyButton);
</script>
```

---

### 🔍 Deep Insights

* **Rule:** Custom Elements, Shadow DOM, HTML Templates.
* **Use Case:** Reusable components, component libraries, or framework-agnostic UI.
* **Common Mistake:** Encapsulated styling and behavior, prevents style conflicts.
* **Pro Tip:** Native browser support, works with any framework or vanilla JS.

---

### ⭐ Senior Takeaway

Web Components are the native browser standard for components.

---

## 🧩 Q71. What are Custom Elements?

### 🧠 Concept

Custom elements extend HTML with new tags that have their own behavior and styling. Custom elements are the foundation of Web Components.

---

### 💡 Example

```html
<user-card name="John Doe" email="john@example.com"></user-card>
<script>
class UserCard extends HTMLElement {
  constructor() {
    super();
    this.attachShadow({ mode: 'open' }).innerHTML = 
      `<div>
        <h3>${this.getAttribute('name')}</h3>
        <p>${this.getAttribute('email')}</p>
      </div>`;
  }
}
customElements.define('user-card', UserCard);
</script>
```

---

### 🔍 Deep Insights

* **Rule:** Extend HTMLElement class, use Shadow DOM, define with customElements.define().
* **Use Case:** Reusable components, custom widgets, or framework-agnostic components.
* **Common Mistake:** Lifecycle callbacks: connectedCallback, disconnectedCallback, attributeChangedCallback.
* **Pro Tip:** Watch attribute changes and react accordingly.

---

### ⭐ Senior Takeaway

Custom elements are the foundation of Web Components.

---

## 🧩 Q72. What is Shadow DOM?

### 🧠 Concept

Shadow DOM provides encapsulation for DOM and CSS, creating isolated components. Shadow DOM is essential for component encapsulation.

---

### 💡 Example

```html
<my-widget></my-widget>
<script>
class MyWidget extends HTMLElement {
  constructor() {
    super();
    const shadow = this.attachShadow({ mode: 'open' });
    shadow.innerHTML = 
      `<style>div { color: blue; }</style>
       <div>Widget Content</div>`;
  }
}
customElements.define('my-widget', MyWidget);
</script>
```

---

### 🔍 Deep Insights

* **Rule:** Encapsulate DOM and CSS, prevent style conflicts.
* **Use Case:** Component libraries, isolated widgets, or style encapsulation.
* **Common Mistake:** `mode: 'open'` allows external access, `mode: 'closed'` prevents access.
* **Pro Tip:** Styles don't leak in or out, creates true component isolation.

---

### ⭐ Senior Takeaway

Shadow DOM is essential for component encapsulation.

---

## 🧩 Q73. What is WebRTC?

### 🧠 Concept

WebRTC enables real-time communication between browsers for video, audio, and data sharing. WebRTC is for peer-to-peer communication, not server-based.

---

### 💡 Example

```html
<video id="localVideo" autoplay muted></video>
<video id="remoteVideo" autoplay></video>
<button onclick="startCall()">Start Call</button>
<script>
async function startCall() {
  const stream = await navigator.mediaDevices.getUserMedia({ 
    video: true, 
    audio: true 
  });
  document.getElementById('localVideo').srcObject = stream;
}
</script>
```

---

### 🔍 Deep Insights

* **Rule:** Peer-to-peer real-time communication for video, audio, and data.
* **Use Case:** Video calling, screen sharing, or real-time collaboration.
* **Common Mistake:** Requires HTTPS in production, complex setup with signaling server.
* **Pro Tip:** Handles video, audio, and data channels between peers.

---

### ⭐ Senior Takeaway

WebRTC is for peer-to-peer communication, not server-based.

---

## 🧩 Q74. What are Service Workers?

### 🧠 Concept

Service Workers are background scripts that act as network proxies, enabling offline functionality and push notifications. Service Workers require HTTPS, enable PWAs.

---

### 💡 Example

```html
<script>
if ('serviceWorker' in navigator) {
  window.addEventListener('load', () => {
    navigator.serviceWorker.register('/sw.js')
      .then(reg => console.log('SW registered'))
      .catch(err => console.log('SW registration failed'));
  });
}
</script>
```

---

### 🔍 Deep Insights

* **Rule:** Background scripts that act as network proxies.
* **Use Case:** Offline functionality, push notifications, or background sync.
* **Common Mistake:** Install, activate, fetch events control behavior.
* **Pro Tip:** Intercepts network requests, can serve cached content.

---

### ⭐ Senior Takeaway

Service Workers require HTTPS, enable PWAs.

---

## 🧩 Q75. What are Progressive Web Apps (PWAs)?

### 🧠 Concept

PWAs combine web technologies with native app features like offline functionality, push notifications, and app-like experience. PWAs bridge web and native apps, require Service Worker.

---

### 💡 Example

```html
<link rel="manifest" href="/manifest.json">
<meta name="theme-color" content="#000000">
<meta name="apple-mobile-web-app-capable" content="yes">
```

---

### 🔍 Deep Insights

* **Rule:** HTTPS, Service Worker, Web App Manifest.
* **Use Case:** Offline functionality, push notifications, installable on devices.
* **Common Mistake:** Web App Manifest defines app metadata, icons, theme colors, display mode.
* **Pro Tip:** App-like experience, installable, works offline.

---

### ⭐ Senior Takeaway

PWAs bridge web and native apps, require Service Worker.

---
