# 🚀 5. HTML5 Features & APIs (Q61–75)

---

## 61) What are the new semantic elements in HTML5?

Concept:
HTML5 introduced semantic elements that provide meaning to document structure, improving accessibility and SEO.

Example:
```html
<body>
  <header>
    <h1>Site Title</h1>
    <nav>
      <ul>
        <li><a href="/">Home</a></li>
```

Deep Insight:
- Semantic elements improve document structure
- Better accessibility for screen readers
- Enhanced SEO through content hierarchy
- Provides default styling and behavior
- Creates landmark regions for navigation

---

## 62) What is the Canvas API and how do you use it?

Concept:
Canvas API provides a 2D drawing surface for creating graphics, animations, and interactive content.

Example:
```html
<canvas id="myCanvas" width="400" height="200"></canvas>

<script>
const canvas = document.getElementById('myCanvas');
const ctx = canvas.getContext('2d');

```

Deep Insight:
- Requires JavaScript for drawing
- Pixel-based 2D graphics
- Great for games and visualizations
- Can export as images
- Performance depends on canvas size

---

## 63) How do you create drag and drop functionality?

Concept:
HTML5 Drag and Drop API allows elements to be draggable and provides events for drop handling.

Example:
```html
<div id="drag-source" draggable="true" ondragstart="dragStart(event)">
  Drag me!
</div>

<div id="drop-target" ondrop="drop(event)" ondragover="allowDrop(event)">
  Drop here
```

Deep Insight:
- Use `draggable="true"` to make elements draggable
- Handle `dragstart`, `dragover`, and `drop` events
- Use `dataTransfer` to pass data
- Prevent default behavior for drop zones
- Visual feedback improves user experience

---

## 64) What is the Geolocation API?

Concept:
Geolocation API provides access to device location information with user permission.

Example:
```html
<button onclick="getLocation()">Get My Location</button>
<div id="location"></div>

<script>
function getLocation() {
  if (navigator.geolocation) {
```

Deep Insight:
- Requires user permission
- Provides latitude, longitude, and accuracy
- Can watch position changes
- Privacy considerations important
- Fallback for unsupported browsers

---

## 65) How do you use the Web Storage API?

Concept:
Web Storage API provides local storage (persistent) and session storage (temporary) for client-side data.

Example:
```html
<input type="text" id="username" placeholder="Enter username">
<button onclick="saveData()">Save</button>
<button onclick="loadData()">Load</button>
<button onclick="clearData()">Clear</button>

<script>
```

Deep Insight:
- `localStorage` persists across browser sessions
- `sessionStorage` clears when tab closes
- Data stored as strings (JSON for objects)
- 5-10MB storage limit per origin
- Synchronous API (blocks main thread)

---

## 66) What is the History API and how do you use it?

Concept:
History API allows manipulation of browser history for single-page applications and custom navigation.

Example:
```html
<button onclick="goToPage('/home')">Home</button>
<button onclick="goToPage('/about')">About</button>
<button onclick="goBack()">Back</button>
<div id="content">Home Page Content</div>

<script>
```

Deep Insight:
- `pushState()` adds new history entry
- `replaceState()` modifies current entry
- `popstate` event handles back/forward
- Enables single-page application navigation
- URLs remain bookmarkable and shareable

---

## 67) How do you create offline web applications?

Concept:
Use Service Workers and Cache API to create web applications that work offline by caching resources.

Example:
```html
<!-- Service Worker registration -->
<script>
if ('serviceWorker' in navigator) {
  navigator.serviceWorker.register('/sw.js')
    .then(registration => console.log('SW registered'))
    .catch(error => console.log('SW registration failed'));
```

Deep Insight:
- Service Workers run in background
- Cache API stores resources offline
- Install event caches initial resources
- Fetch event serves cached content
- Fallback to network when cache misses

---

## 68) What is the Web Workers API?

Concept:
Web Workers allow JavaScript to run in background threads, preventing UI blocking for heavy computations.

Example:
```html
<button onclick="startWorker()">Start Heavy Task</button>
<button onclick="stopWorker()">Stop Worker</button>
<div id="result"></div>

<script>
let worker;
```

Deep Insight:
- Workers run in separate thread
- Communicate via postMessage
- Can't access DOM or window object
- Great for heavy computations
- Use terminate() to stop workers

---

## 69) How do you use the Intersection Observer API?

Concept:
Intersection Observer API efficiently detects when elements enter or exit the viewport.

Example:
```html
<div class="section">Section 1</div>
<div class="section">Section 2</div>
<div class="section">Section 3</div>

<script>
const observer = new IntersectionObserver((entries) => {
```

Deep Insight:
- More efficient than scroll events
- Can observe multiple elements
- Configurable root margin and threshold
- Great for lazy loading and animations
- Better performance than scroll listeners

---

## 70) What is the Web Components standard?

Concept:
Web Components are a set of web platform APIs that allow creating reusable custom elements.

Example:
```html
<!-- Custom element usage -->
<my-button text="Click me!" color="blue"></my-button>

<script>
class MyButton extends HTMLElement {
  constructor() {
```

Deep Insight:
- Three main technologies: Custom Elements, Shadow DOM, HTML Templates
- Encapsulated styling and behavior
- Reusable across projects
- Framework-agnostic
- Native browser support

---

## 71) How do you create custom elements?

Concept:
Custom elements extend HTML with new tags that have their own behavior and styling.

Example:
```html
<user-card name="John Doe" email="john@example.com"></user-card>

<script>
class UserCard extends HTMLElement {
  constructor() {
    super();
```

Deep Insight:
- Extend HTMLElement class
- Use Shadow DOM for encapsulation
- Define with customElements.define()
- Lifecycle callbacks: connectedCallback, disconnectedCallback
- Observed attributes trigger attributeChangedCallback

---

## 72) What is the Shadow DOM?

Concept:
Shadow DOM provides encapsulation for DOM and CSS, creating isolated components.

Example:
```html
<my-widget></my-widget>

<script>
class MyWidget extends HTMLElement {
  constructor() {
    super();
```

Deep Insight:
- Encapsulates DOM and CSS
- Styles don't leak in or out
- `mode: 'open'` allows external access
- `mode: 'closed'` prevents external access
- Great for component libraries

---

## 73) How do you use the WebRTC API?

Concept:
WebRTC enables real-time communication between browsers for video, audio, and data sharing.

Example:
```html
<video id="localVideo" autoplay muted></video>
<video id="remoteVideo" autoplay></video>
<button onclick="startCall()">Start Call</button>

<script>
let localStream;
```

Deep Insight:
- Enables peer-to-peer communication
- Requires HTTPS in production
- Handles video, audio, and data channels
- Complex setup with signaling server
- Great for video calling applications

---

## 74) What is the Service Worker API?

Concept:
Service Workers are background scripts that act as network proxies, enabling offline functionality and push notifications.

Example:
```html
<!-- Service Worker registration -->
<script>
if ('serviceWorker' in navigator) {
  window.addEventListener('load', () => {
    navigator.serviceWorker.register('/sw.js')
      .then(registration => {
```

Deep Insight:
- Runs in background thread
- Acts as network proxy
- Enables offline functionality
- Handles push notifications
- Lifecycle: install, activate, fetch

---

## 75) How do you create progressive web applications?

Concept:
PWAs combine web technologies with native app features like offline functionality, push notifications, and app-like experience.

Example:
```html
<!-- Web App Manifest -->
<link rel="manifest" href="/manifest.json">

<!-- Meta tags for PWA -->
<meta name="theme-color" content="#000000">
<meta name="apple-mobile-web-app-capable" content="yes">
```

Deep Insight:
- Combines web and native app features
- Requires HTTPS and Service Worker
- Web App Manifest defines app metadata
- Installable on mobile devices
- Offline functionality and push notifications
