---
sidebar_label: "HTML5 & Modern APIs"
---
# 🚀 5. HTML5 & Modern APIs (Q61–74)
> **Reviewed:** 2026-09 · Modernized; legacy topics are labeled.

---

## Q61. 🔌 Canvas API and how to use it

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

## Q62. 🔌 Drag and Drop API

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
  e.currentTarget.appendChild(document.getElementById(data));
}
</script>

```

- **2026 notes**: native HTML5 drag and drop has weak touch-device and keyboard support, so production reorderable lists usually use a library built on pointer events (e.g. dnd-kit) with keyboard support. WCAG 2.2 **2.5.7 Dragging Movements** requires a non-drag alternative (e.g. "Move up/Move down" buttons). For file drops, still handle `dragover`/`drop` but also offer an `<input type="file">`.

---

## Q63. 🔌 Geolocation API

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

## Q64. 💡 Web Storage (localStorage and sessionStorage)

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

- **Security & modern alternatives**: anything in `localStorage` is readable by any script on the page, so an XSS bug exposes it — **don't store auth tokens there**; prefer `HttpOnly`, `Secure`, `SameSite` cookies. `localStorage` isn't available in service workers or web workers. For larger or structured data use **IndexedDB** (async); for large files, the **Origin Private File System (OPFS)**. Check quota with `navigator.storage.estimate()`.

---

## Q65. 🔌 History API

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

- **2026 note**: the newer **Navigation API** (`navigation.addEventListener('navigate', e => e.intercept({ handler }))`) centralizes SPA navigation handling (links, forms, back/forward) in one event. It shipped in Chromium first and other engines have been adding it more recently — check current Baseline status and keep a History API fallback. Most apps use a router (React Router, Next.js, TanStack Router) that wraps these APIs. For accessibility, after a client-side navigation update `document.title` and move focus to the new page's heading.

---

## Q66. 💡 Offline Web Apps

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

> **Legacy note (2026):** The old **Application Cache** (`<html manifest="cache.appcache">`) is removed from all major browsers — never recommend it. Service workers + Cache API (often via **Workbox**) replaced it, with **IndexedDB** for offline data. For caching strategies, background sync, and conflict resolution, see the [Offline Support deep dive](../architecture/22-offline-support.md).

---

## Q67. 👷 Web Workers

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

## Q68. 🔌 Intersection Observer API

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

## Q69. 🧩 Web Components

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

- **Watch out**: interpolating attributes into `innerHTML` (as above) is an XSS risk if the values can come from users — set `textContent` or build elements instead. The spec also recommends not reading attributes or children in the `constructor`; do setup in `connectedCallback`. Custom elements' shadow DOM needs extra work for forms (`ElementInternals` + `static formAssociated = true`) and for ARIA references across shadow boundaries.

- **2026 notes**: **Declarative Shadow DOM** (`<template shadowrootmode="open">`, Baseline 2024) lets servers render shadow roots in HTML, so Web Components can be SSR'd without JavaScript. React 19 supports custom elements properly (properties and custom events), which makes design systems built with Lit or Stencil easier to consume from React.

```html
<my-card>
  <template shadowrootmode="open">
    <style>:host { display: block; border: 1px solid #ccc; }</style>
    <slot></slot>
  </template>
  Server-rendered content
</my-card>
```

---

## Q70. 💡 Custom Elements

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

## Q71. 💡 Shadow DOM

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

## Q72. 💡 WebRTC

WebRTC enables real-time peer-to-peer communication between browsers for video, audio, and data sharing without plugins - it establishes direct connections between browsers using ICE, STUN, and TURN servers. WebRTC handles media capture, encoding, and peer connection establishment, making it ideal for video calling, screen sharing, and real-time collaboration.

- **Trade-offs**: The catch is requires HTTPS in production (except localhost), complex setup with signaling server for connection negotiation, and NAT traversal can be challenging - WebRTC needs a signaling server (WebSocket/HTTP) to exchange connection metadata, but actual media flows peer-to-peer. WebRTC is for peer-to-peer communication, not server-based, but watch out - good for low-latency video calling, screen sharing, or real-time collaboration, but requires proper signaling infrastructure.

Example:

```html
<video id="localVideo" autoplay muted></video>
<video id="remoteVideo" autoplay></video>
<button onclick="startCall()">Start Call</button>
<script>
let localStream;
let peerConnection;

// Get user media (camera and microphone)
async function startCall() {
  try {
    // Request access to user's camera and microphone
    localStream = await navigator.mediaDevices.getUserMedia({
      video: true,
      audio: true
    });

    // Display local video stream
    document.getElementById('localVideo').srcObject = localStream;

    // Create RTCPeerConnection (simplified - real implementation needs signaling)
    const configuration = {
      iceServers: [{ urls: 'stun:stun.l.google.com:19302' }] // STUN server for NAT traversal
    };
    peerConnection = new RTCPeerConnection(configuration);

    // Add local stream tracks to peer connection
    localStream.getTracks().forEach(track => {
      peerConnection.addTrack(track, localStream); // Add each track (video/audio) to connection
    });

    // Handle remote stream when received
    peerConnection.ontrack = (event) => {
      document.getElementById('remoteVideo').srcObject = event.streams[0]; // Display remote video
    };

    // Handle ICE candidates (network information for connection)
    peerConnection.onicecandidate = (event) => {
      if (event.candidate) {
        // Send candidate to remote peer via signaling server (not shown here)
        console.log('ICE candidate:', event.candidate);
      }
    };

  } catch (error) {
    console.error('Error accessing media devices:', error);
  }
}
</script>

```

---

## Q73. 💬 Popover API and when to use it

The **Popover API** turns any element into a popover with just HTML: add the `popover` attribute to the content and `popovertarget="id"` to a button. You get **top-layer rendering** (above everything, no `z-index`), **light dismiss** (click outside or press Escape closes it), correct toggling from the invoking button, and basic accessibility wiring (the button gets an expanded/collapsed state). The `popover` attribute has been **Baseline since 2024** (Firefox 125 was the last engine).

- **Variants**:
  - `popover` / `popover="auto"` – light-dismissable; opening one auto popover closes other non-nested auto popovers (menus, pickers)
  - `popover="manual"` – no light dismiss; you control open/close (toasts, persistent panels)
  - `popover="hint"` – for tooltips that don't close other popovers — **newer, not Baseline** at the time of review
  - JS API: `el.showPopover()`, `el.hidePopover()`, `el.togglePopover()`, plus `beforetoggle`/`toggle` events

- **Trade-offs**: The catch is a popover is **not modal** — focus isn't trapped and the page isn't inert; use `<dialog>` + `showModal()` for that (Q74). The popover attribute doesn't assign a role — add the right semantics yourself (e.g. `role="menu"` needs the full APG keyboard pattern, or just use a list of links/buttons). Positioning next to the trigger needs **CSS anchor positioning** (Chromium-first, still reaching other engines — emerging) or a JS library like Floating UI as fallback. Animating open/close uses `@starting-style` and `transition-behavior: allow-discrete` (newer).

Example:

```html
<button popovertarget="account-menu">Account</button>

<div id="account-menu" popover>
  <a href="/profile">Profile</a>
  <a href="/settings">Settings</a>
  <button popovertarget="account-menu" popovertargetaction="hide">Close</button>
</div>

<div id="toast" popover="manual" role="status">Saved!</div>
<script>
  const toast = document.getElementById('toast');
  function showToast() {
    toast.showPopover();
    setTimeout(() => toast.hidePopover(), 3000);
  }
</script>

```

```css
[popover] {
  transition: opacity 150ms, display 150ms allow-discrete, overlay 150ms allow-discrete;
  opacity: 0;
}
[popover]:popover-open { opacity: 1; }
@starting-style { [popover]:popover-open { opacity: 0; } }
```

---

## Q74. 🪟 `<dialog>` vs popover vs custom overlay

Both `<dialog>` and popovers render in the top layer, but they solve different problems. Pick based on whether the user **must** deal with the overlay before continuing.

- **`<dialog>` + `showModal()`** – *modal*: page behind becomes inert, focus moves inside, Escape closes, `::backdrop` available. Use for confirmations, forms that block the flow, critical alerts. (Baseline since 2022.)
- **`<dialog>` + `show()`** – *non-modal* dialog; stays open while the user interacts with the page (e.g. a find/replace panel).
- **`popover`** – *non-modal, light-dismissable* overlay: menus, pickers, disclosure panels, teaching bubbles, toasts (`manual`).
- **Custom `div` overlays** – **legacy** default; only needed for unusual requirements or very old browser support. You must re-implement focus trap, Escape, inert background, scroll lock, and ARIA.

- **Trade-offs**: The catch is `<dialog>` without `showModal()` isn't modal, and `form method="dialog"` closes the dialog without a network submit (the button `value` becomes `dialog.returnValue`). Opening dialogs declaratively without JS is possible with **invoker commands** (`<button commandfor="d" command="show-modal">`) — newer, check Baseline status before relying on it. Always label with `aria-labelledby`, and prevent background scroll with `body:has(dialog[open]) { overflow: hidden; }`.

Example:

```html
<button onclick="confirmDelete.showModal()">Delete project</button>

<dialog id="confirmDelete" aria-labelledby="del-title">
  <h2 id="del-title">Delete this project?</h2>
  <p>This can't be undone.</p>
  <form method="dialog">
    <button value="cancel" autofocus>Cancel</button>
    <button value="delete">Delete</button>
  </form>
</dialog>

```

```css
dialog::backdrop { background: rgb(0 0 0 / 0.5); }
body:has(dialog[open]) { overflow: hidden; }
```

---

## References

* [MDN — Popover API](https://developer.mozilla.org/en-US/docs/Web/API/Popover_API)
* [MDN — The Dialog element](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/dialog)
* [MDN — Declarative Shadow DOM (template shadowrootmode)](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/template)
* [MDN — Navigation API](https://developer.mozilla.org/en-US/docs/Web/API/Navigation_API)
* [web.dev — Baseline](https://web.dev/baseline)

