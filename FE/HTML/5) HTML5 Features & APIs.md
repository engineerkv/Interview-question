# 🚀 5. HTML5 Features & APIs (Q61–75)

---

## 61) What are the new semantic elements in HTML5?

HTML5 introduced semantic elements that provide meaning to document structure, improving accessibility and SEO.

```html
<body>
  <header><h1>Site Title</h1></header>
  <nav><ul><li><a href="/">Home</a></li><li><a href="/about">About</a></li></ul></nav>
  <main><article><h2>Article Title</h2><p>Content...</p></article></main>
  <footer><p>Copyright 2024</p></footer>
</body>
```

- **Core Elements**: header, nav, main, article, section, aside, footer provide semantic meaning
- **Real-World Impact**: Better accessibility for screen readers, enhanced SEO through content hierarchy
- **Landmark Regions**: Creates navigable regions for screen reader users
- **Default Styling**: Provides default styling and behavior, works with CSS
- **Interview Tip**: Explain that semantic HTML5 elements replace generic divs with meaningful structure

---

## 62) What is the Canvas API and how do you use it?

Canvas API provides a 2D drawing surface for creating graphics, animations, and interactive content.

```html
<canvas id="myCanvas" width="400" height="200"></canvas>
<script>
const canvas = document.getElementById('myCanvas');
const ctx = canvas.getContext('2d');
ctx.fillStyle = 'blue';
ctx.fillRect(10, 10, 100, 50);
</script>
```

- **Core Purpose**: 2D drawing surface for graphics, animations, games, or visualizations
- **Real-World Use**: Games, charts, image editing, or any pixel-based graphics
- **JavaScript Required**: Requires JavaScript for drawing, no direct HTML drawing
- **Performance**: Performance depends on canvas size and complexity of drawings
- **Interview Tip**: Explain that Canvas is for pixel-based graphics, SVG is for vector graphics

---

## 63) How do you create drag and drop functionality?

HTML5 Drag and Drop API allows elements to be draggable and provides events for drop handling.

```html
<div id="drag-source" draggable="true" ondragstart="dragStart(event)">Drag me!</div>
<div id="drop-target" ondrop="drop(event)" ondragover="allowDrop(event)">Drop here</div>
<script>
function dragStart(e) { e.dataTransfer.setData('text', e.target.id); }
function allowDrop(e) { e.preventDefault(); }
function drop(e) { e.preventDefault(); var data = e.dataTransfer.getData('text'); }
</script>
```

- **Core Steps**: Set `draggable="true"`, handle `dragstart`, `dragover`, and `drop` events
- **Real-World Use**: File uploads, drag-and-drop interfaces, or reorderable lists
- **Data Transfer**: Use `dataTransfer` to pass data between drag source and drop target
- **Best Practice**: Prevent default behavior for drop zones, provide visual feedback
- **Interview Tip**: Explain that drag and drop requires JavaScript event handling

---

## 64) What is the Geolocation API?

Geolocation API provides access to device location information with user permission.

```html
<button onclick="getLocation()">Get My Location</button>
<div id="location"></div>
<script>
function getLocation() {
  if (navigator.geolocation) {
    navigator.geolocation.getCurrentPosition((pos) => {
      document.getElementById('location').textContent = `Lat: ${pos.coords.latitude}, Lon: ${pos.coords.longitude}`;
    });
  }
}
</script>
```

- **Core Purpose**: Get user's geographic location with permission
- **Real-World Use**: Location-based services, maps, weather apps, or nearby searches
- **Privacy**: Requires user permission, important for privacy considerations
- **Data Provided**: Provides latitude, longitude, accuracy, and optional altitude
- **Interview Tip**: Explain that geolocation requires HTTPS in production, respects user privacy

---

## 65) How do you use the Web Storage API?

Web Storage API provides local storage (persistent) and session storage (temporary) for client-side data.

```html
<input type="text" id="username" placeholder="Enter username">
<button onclick="saveData()">Save</button>
<button onclick="loadData()">Load</button>
<script>
function saveData() { localStorage.setItem('username', document.getElementById('username').value); }
function loadData() { document.getElementById('username').value = localStorage.getItem('username') || ''; }
</script>
```

- **Core Types**: `localStorage` persists across sessions, `sessionStorage` clears when tab closes
- **Real-World Use**: User preferences, form data, or any client-side data storage
- **Storage Limit**: 5-10MB per origin, data stored as strings (use JSON for objects)
- **Synchronous API**: Blocks main thread, consider using IndexedDB for large data
- **Interview Tip**: Explain that localStorage is synchronous, sessionStorage is tab-specific

---

## 66) What is the History API and how do you use it?

History API allows manipulation of browser history for single-page applications and custom navigation.

```html
<button onclick="goToPage('/home')">Home</button>
<button onclick="goBack()">Back</button>
<div id="content">Home Page Content</div>
<script>
function goToPage(page) {
  history.pushState({page}, '', page);
  document.getElementById('content').textContent = page + ' Page Content';
}
function goBack() { history.back(); }
window.addEventListener('popstate', (e) => {
  document.getElementById('content').textContent = e.state?.page + ' Page Content';
});
</script>
```

- **Core Purpose**: Manipulate browser history without page reloads
- **Real-World Use**: Single-page applications, custom navigation, or bookmarkable URLs
- **Methods**: `pushState()` adds history entry, `replaceState()` modifies current entry
- **Events**: `popstate` event handles back/forward button navigation
- **Interview Tip**: Explain that History API enables SPAs with proper browser navigation

---

## 67) How do you create offline web applications?

Use Service Workers and Cache API to create web applications that work offline by caching resources.

```html
<script>
if ('serviceWorker' in navigator) {
  navigator.serviceWorker.register('/sw.js')
    .then(reg => console.log('SW registered'))
    .catch(err => console.log('SW registration failed'));
}
</script>
```

- **Core Technologies**: Service Workers run in background, Cache API stores resources
- **Real-World Use**: Offline functionality, faster loading, or reduced server load
- **Lifecycle**: Install event caches resources, fetch event serves cached content
- **Fallback Strategy**: Falls back to network when cache misses, improves reliability
- **Interview Tip**: Explain that Service Workers require HTTPS, enable offline-first apps

---

## 68) What is the Web Workers API?

Web Workers allow JavaScript to run in background threads, preventing UI blocking for heavy computations.

```html
<button onclick="startWorker()">Start Heavy Task</button>
<div id="result"></div>
<script>
let worker;
function startWorker() {
  worker = new Worker('worker.js');
  worker.onmessage = (e) => document.getElementById('result').textContent = e.data;
  worker.postMessage('start');
}
</script>
```

- **Core Purpose**: Run JavaScript in background threads, keep UI responsive
- **Real-World Use**: Heavy computations, image processing, or data parsing
- **Limitations**: Can't access DOM or window object, communicate via postMessage
- **Performance**: Prevents UI blocking, improves user experience
- **Interview Tip**: Explain that Web Workers are for CPU-intensive tasks, not DOM manipulation

---

## 69) How do you use the Intersection Observer API?

Intersection Observer API efficiently detects when elements enter or exit the viewport.

```html
<div class="section">Section 1</div>
<div class="section">Section 2</div>
<script>
const observer = new IntersectionObserver((entries) => {
  entries.forEach(entry => {
    if (entry.isIntersecting) entry.target.style.backgroundColor = 'yellow';
  });
}, { threshold: 0.5 });
document.querySelectorAll('.section').forEach(section => observer.observe(section));
</script>
```

- **Core Purpose**: Efficiently detect when elements enter or exit viewport
- **Real-World Use**: Lazy loading images, infinite scrolling, or scroll animations
- **Performance**: More efficient than scroll event listeners, better performance
- **Configuration**: Configurable root margin and threshold for fine-tuned detection
- **Interview Tip**: Explain that Intersection Observer is better than scroll events for performance

---

## 70) What is the Web Components standard?

Web Components are a set of web platform APIs that allow creating reusable custom elements.

```html
<my-button text="Click me!" color="blue"></my-button>
<script>
class MyButton extends HTMLElement {
  constructor() {
    super();
    this.attachShadow({ mode: 'open' }).innerHTML = `<button style="color: ${this.getAttribute('color')}">${this.getAttribute('text')}</button>`;
  }
}
customElements.define('my-button', MyButton);
</script>
```

- **Core Technologies**: Custom Elements, Shadow DOM, HTML Templates
- **Real-World Use**: Reusable components, component libraries, or framework-agnostic UI
- **Encapsulation**: Encapsulated styling and behavior, prevents style conflicts
- **Framework-Agnostic**: Native browser support, works with any framework or vanilla JS
- **Interview Tip**: Explain that Web Components are the native browser standard for components

---

## 71) How do you create custom elements?

Custom elements extend HTML with new tags that have their own behavior and styling.

```html
<user-card name="John Doe" email="john@example.com"></user-card>
<script>
class UserCard extends HTMLElement {
  constructor() {
    super();
    this.attachShadow({ mode: 'open' }).innerHTML = `<div><h3>${this.getAttribute('name')}</h3><p>${this.getAttribute('email')}</p></div>`;
  }
}
customElements.define('user-card', UserCard);
</script>
```

- **Core Steps**: Extend HTMLElement class, use Shadow DOM, define with customElements.define()
- **Real-World Use**: Reusable components, custom widgets, or framework-agnostic components
- **Lifecycle Callbacks**: connectedCallback, disconnectedCallback, attributeChangedCallback
- **Observed Attributes**: Watch attribute changes and react accordingly
- **Interview Tip**: Explain that custom elements are the foundation of Web Components

---

## 72) What is the Shadow DOM?

Shadow DOM provides encapsulation for DOM and CSS, creating isolated components.

```html
<my-widget></my-widget>
<script>
class MyWidget extends HTMLElement {
  constructor() {
    super();
    const shadow = this.attachShadow({ mode: 'open' });
    shadow.innerHTML = `<style>div { color: blue; }</style><div>Widget Content</div>`;
  }
}
customElements.define('my-widget', MyWidget);
</script>
```

- **Core Purpose**: Encapsulate DOM and CSS, prevent style conflicts
- **Real-World Use**: Component libraries, isolated widgets, or style encapsulation
- **Modes**: `mode: 'open'` allows external access, `mode: 'closed'` prevents access
- **Style Isolation**: Styles don't leak in or out, creates true component isolation
- **Interview Tip**: Explain that Shadow DOM is essential for component encapsulation

---

## 73) How do you use the WebRTC API?

WebRTC enables real-time communication between browsers for video, audio, and data sharing.

```html
<video id="localVideo" autoplay muted></video>
<video id="remoteVideo" autoplay></video>
<button onclick="startCall()">Start Call</button>
<script>
async function startCall() {
  const stream = await navigator.mediaDevices.getUserMedia({ video: true, audio: true });
  document.getElementById('localVideo').srcObject = stream;
}
</script>
```

- **Core Purpose**: Peer-to-peer real-time communication for video, audio, and data
- **Real-World Use**: Video calling, screen sharing, or real-time collaboration
- **Requirements**: Requires HTTPS in production, complex setup with signaling server
- **Capabilities**: Handles video, audio, and data channels between peers
- **Interview Tip**: Explain that WebRTC is for peer-to-peer communication, not server-based

---

## 74) What is the Service Worker API?

Service Workers are background scripts that act as network proxies, enabling offline functionality and push notifications.

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

- **Core Purpose**: Background scripts that act as network proxies
- **Real-World Use**: Offline functionality, push notifications, or background sync
- **Lifecycle**: Install, activate, fetch events control behavior
- **Network Proxy**: Intercepts network requests, can serve cached content
- **Interview Tip**: Explain that Service Workers require HTTPS, enable PWAs

---

## 75) How do you create progressive web applications?

PWAs combine web technologies with native app features like offline functionality, push notifications, and app-like experience.

```html
<link rel="manifest" href="/manifest.json">
<meta name="theme-color" content="#000000">
<meta name="apple-mobile-web-app-capable" content="yes">
```

- **Core Requirements**: HTTPS, Service Worker, Web App Manifest
- **Real-World Features**: Offline functionality, push notifications, installable on devices
- **Web App Manifest**: Defines app metadata, icons, theme colors, display mode
- **Native-Like Experience**: App-like experience, installable, works offline
- **Interview Tip**: Explain that PWAs bridge web and native apps, require Service Worker

---
