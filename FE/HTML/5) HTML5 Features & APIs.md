# 🚀 5. HTML5 Features & APIs (Q61–75)

---

## 📍 Navigation

<div align="center">

[Accessibility (A11y)](4%29%20Accessibility%20%28A11y%29.md) • [Home: README](../README.md) • [Media Elements →](6%29%20Media%20Elements.md)

[📋 Cheatsheet](HTML%20Interview%20Cheatsheet.md)

</div>

---

---

## Q61. 📄 New semantic elements in HTML5

HTML5 introduced semantic elements that provide meaning to document structure, improving accessibility and SEO - semantic HTML5 elements replace generic divs with meaningful structure. header, nav, main, article, section, aside, footer provide semantic meaning.

- **Trade-offs**: The catch is creates navigable regions for screen reader users - provides default styling and behavior, works with CSS. Semantic HTML5 elements replace generic divs with meaningful structure, but watch out - better accessibility for screen readers, enhanced SEO through content hierarchy.

Example:

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

## Q62. 🔌 Canvas API and how to use it

Canvas API provides a 2D drawing surface for creating graphics, animations, and interactive content - canvas is for pixel-based graphics, SVG is for vector graphics. 2D drawing surface for graphics, animations, games, or visualizations.

- **Trade-offs**: The catch is requires JavaScript for drawing, no direct HTML drawing - performance depends on canvas size and complexity of drawings. Canvas is for pixel-based graphics, SVG is for vector graphics, but watch out - good for games, charts, image editing, or any pixel-based graphics.

Example:

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

## Q63. 🔌 Drag and Drop API

HTML5 Drag and Drop API allows elements to be draggable and provides events for drop handling - drag and drop requires JavaScript event handling. Set `draggable="true"`, handle `dragstart`, `dragover`, and `drop` events.

- **Trade-offs**: The catch is use `dataTransfer` to pass data between drag source and drop target - prevent default behavior for drop zones, provide visual feedback. Drag and drop requires JavaScript event handling, but watch out - good for file uploads, drag-and-drop interfaces, or reorderable lists.

Example:

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

## Q64. 🔌 Geolocation API

Geolocation API provides access to device location information with user permission - geolocation requires HTTPS in production, respects user privacy. Get user's geographic location with permission.

- **Trade-offs**: The catch is requires user permission, important for privacy considerations - provides latitude, longitude, accuracy, and optional altitude. Geolocation requires HTTPS in production, respects user privacy, but watch out - good for location-based services, maps, weather apps, or nearby searches.

Example:

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

## Q65. 💡 Web Storage (localStorage and sessionStorage)

Web Storage API provides local storage (persistent) and session storage (temporary) for client-side data - localStorage is synchronous, sessionStorage is tab-specific. `localStorage` persists across sessions, `sessionStorage` clears when tab closes.

- **Trade-offs**: The catch is 5-10MB per origin, data stored as strings (use JSON for objects) - blocks main thread, consider using IndexedDB for large data. localStorage is synchronous, sessionStorage is tab-specific, but watch out - good for user preferences, form data, or any client-side data storage.

Example:

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

## Q66. 🔌 History API

History API allows manipulation of browser history for single-page applications and custom navigation - history API enables SPAs with proper browser navigation. Manipulate browser history without page reloads.

- **Trade-offs**: The catch is `pushState()` adds history entry, `replaceState()` modifies current entry - `popstate` event handles back/forward button navigation. History API enables SPAs with proper browser navigation, but watch out - good for single-page applications, custom navigation, or bookmarkable URLs.

Example:

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

## Q67. 💡 Offline Web Apps

Use Service Workers and Cache API to create web applications that work offline by caching resources - service workers require HTTPS, enable offline-first apps. Service Workers run in background, Cache API stores resources.

- **Trade-offs**: The catch is install event caches resources, fetch event serves cached content - falls back to network when cache misses, improves reliability. Service Workers require HTTPS, enable offline-first apps, but watch out - good for offline functionality, faster loading, or reduced server load.

Example:

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

## Q68. 👷 Web Workers

Web Workers allow JavaScript to run in background threads, preventing UI blocking for heavy computations - web workers are for CPU-intensive tasks, not DOM manipulation. Run JavaScript in background threads, keep UI responsive.

- **Trade-offs**: The catch is can't access DOM or window object, communicate via postMessage - prevents UI blocking, improves user experience. Web Workers are for CPU-intensive tasks, not DOM manipulation, but watch out - good for heavy computations, image processing, or data parsing.

Example:

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

## Q69. 🔌 Intersection Observer API

Intersection Observer API efficiently detects when elements enter or exit the viewport - intersection observer is better than scroll events for performance. Efficiently detect when elements enter or exit viewport.

- **Trade-offs**: The catch is more efficient than scroll event listeners, better performance - configurable root margin and threshold for fine-tuned detection. Intersection Observer is better than scroll events for performance, but watch out - good for lazy loading images, infinite scrolling, or scroll animations.

Example:

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

## Q70. 🧩 Web Components

Web Components are a set of web platform APIs that allow creating reusable custom elements - web components are the native browser standard for components. Custom Elements, Shadow DOM, HTML Templates.

- **Trade-offs**: The catch is encapsulated styling and behavior, prevents style conflicts - native browser support, works with any framework or vanilla JS. Web Components are the native browser standard for components, but watch out - good for reusable components, component libraries, or framework-agnostic UI.

Example:

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

## Q71. 💡 Custom Elements

Custom elements extend HTML with new tags that have their own behavior and styling - custom elements are the foundation of Web Components. Extend HTMLElement class, use Shadow DOM, define with customElements.define().

- **Trade-offs**: The catch is lifecycle callbacks: connectedCallback, disconnectedCallback, attributeChangedCallback - watch attribute changes and react accordingly. Custom elements are the foundation of Web Components, but watch out - good for reusable components, custom widgets, or framework-agnostic components.

Example:

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

## Q72. 💡 Shadow DOM

Shadow DOM provides encapsulation for DOM and CSS, creating isolated components - shadow DOM is essential for component encapsulation. Encapsulate DOM and CSS, prevent style conflicts.

- **Trade-offs**: The catch is `mode: 'open'` allows external access, `mode: 'closed'` prevents access - styles don't leak in or out, creates true component isolation. Shadow DOM is essential for component encapsulation, but watch out - good for component libraries, isolated widgets, or style encapsulation.

Example:

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

## Q73. 💡 WebRTC

WebRTC enables real-time communication between browsers for video, audio, and data sharing - WebRTC is for peer-to-peer communication, not server-based. Peer-to-peer real-time communication for video, audio, and data.

- **Trade-offs**: The catch is requires HTTPS in production, complex setup with signaling server - handles video, audio, and data channels between peers. WebRTC is for peer-to-peer communication, not server-based, but watch out - good for video calling, screen sharing, or real-time collaboration.

Example:

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

## Q74. 👷 Service Workers

Service Workers are background scripts that act as network proxies, enabling offline functionality and push notifications - service workers require HTTPS, enable PWAs. Background scripts that act as network proxies.

- **Trade-offs**: The catch is install, activate, fetch events control behavior - intercepts network requests, can serve cached content. Service Workers require HTTPS, enable PWAs, but watch out - good for offline functionality, push notifications, or background sync.

Example:

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

## Q75. 💡 Progressive Web Apps (PWAs)

PWAs combine web technologies with native app features like offline functionality, push notifications, and app-like experience - PWAs bridge web and native apps, require Service Worker. HTTPS, Service Worker, Web App Manifest.

- **Trade-offs**: The catch is Web App Manifest defines app metadata, icons, theme colors, display mode - app-like experience, installable, works offline. PWAs bridge web and native apps, require Service Worker, but watch out - good for offline functionality, push notifications, installable on devices.

Example:

```html
<link rel="manifest" href="/manifest.json">
<meta name="theme-color" content="#000000">
<meta name="apple-mobile-web-app-capable" content="yes">

```

---

---

## 📍 Navigation

<div align="center">

[Accessibility (A11y)](4%29%20Accessibility%20%28A11y%29.md) • [Home: README](../README.md) • [Media Elements →](6%29%20Media%20Elements.md)

[📋 Cheatsheet](HTML%20Interview%20Cheatsheet.md)

</div>

---
