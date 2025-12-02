<div align="center">

**[← Previous: How React Native Works Internally](06%29%20How%20React%20Native%20Works%20Internally.md)** | **[Next: High Level Design (HLD) →](08%29%20High%20Level%20Design%20%28HLD%29.md)**

</div>

# 🌐 Important Browser APIs

---

## Q21. DOM API

The DOM (Document Object Model) API allows you to interact with HTML elements, manipulate the document structure, and handle events. It's how JavaScript talks to your HTML page. Understanding the DOM API is fundamental to web development - it's the bridge between your JavaScript code and the actual HTML elements users see and interact with.

---

## 1. DOM Manipulation

### 🔹 Selecting Elements

Selecting elements is the first step to manipulating the DOM. Different methods have different use cases and performance characteristics.

**Single Element Selection:**

**getElementById(id):**
* Fastest method for selecting by ID
* Returns a single element or null
* ID must be unique in the document
* Example:
```javascript
const element = document.getElementById('myId');
if (element) {
  // Element exists
}
```

**querySelector(selector):**
* Uses CSS selector syntax
* Returns first matching element or null
* More flexible than getElementById
* Slower than getElementById (but usually fine)
* Example:
```javascript
const element = document.querySelector('.myClass');
const element = document.querySelector('#myId');
const element = document.querySelector('div.container > p');
```

**Multiple Element Selection:**

**getElementsByClassName(className):**
* Returns a live HTMLCollection (updates automatically)
* Fast for class selection
* Returns array-like object (not a real array)
* Example:
```javascript
const elements = document.getElementsByClassName('myClass');
// elements is HTMLCollection, updates when DOM changes
```

**querySelectorAll(selector):**
* Uses CSS selector syntax
* Returns a static NodeList (snapshot, doesn't update)
* More flexible than getElementsByClassName
* Returns array-like object (can use Array.from() to convert)
* Example:
```javascript
const elements = document.querySelectorAll('.myClass');
const elements = document.querySelectorAll('div.container p');
// elements is NodeList, static snapshot
```

**Performance Considerations:**
* `getElementById` is fastest (use when possible)
* `querySelector` is slower but more flexible
* `querySelectorAll` returns static list (better for iteration)
* `getElementsByClassName` returns live collection (updates automatically)

### 🔹 Creating Elements

```javascript
// Create element
const div = document.createElement('div');
div.textContent = 'Hello World';
div.className = 'container';

// Append to DOM
document.body.appendChild(div);
```

### 🔹 Modifying Elements

```javascript
// Change content
element.textContent = 'New text';
element.innerHTML = '<strong>Bold text</strong>';

// Change attributes
element.setAttribute('id', 'newId');
element.className = 'new-class';
element.style.color = 'red';
```

📌 **In simple terms**: The DOM API allows you to select, create, modify, and remove HTML elements using JavaScript - it's your way of changing what's on the page.

---

## 2. Event Handling

### 🔹 Event Listeners

```javascript
// Add event listener
element.addEventListener('click', (event) => {
  console.log('Clicked!', event);
});

// Remove event listener
const handler = () => console.log('Clicked');
element.addEventListener('click', handler);
element.removeEventListener('click', handler);
```

### 🔹 Event Delegation

Event delegation is a powerful pattern that improves performance and works with dynamic content.

**What is Event Delegation:**
* Attach event listener to parent element instead of each child
* Events bubble up from child to parent
* Check event.target to determine which child was clicked
* More efficient than attaching listeners to every child

**Why Use Event Delegation:**
* **Performance**: One listener instead of many
* **Dynamic content**: Works with elements added after page load
* **Memory**: Less memory usage (fewer listeners)
* **Simpler code**: Easier to manage

**Example:**
```javascript
// Without delegation - attach to each button
const buttons = document.querySelectorAll('.button');
buttons.forEach(button => {
  button.addEventListener('click', handleClick);
});
// Problem: New buttons added later won't have listeners

// With delegation - attach to parent
document.addEventListener('click', (event) => {
  if (event.target.matches('.button')) {
    handleClick(event);
  }
});
// Works with buttons added dynamically
```

**Advanced Example:**
```javascript
// Handle clicks on any button in a list
document.getElementById('list').addEventListener('click', (event) => {
  // Check if clicked element is a button
  if (event.target.matches('button')) {
    const button = event.target;
    const listItem = button.closest('li');
    console.log('Button clicked in:', listItem);
  }
  
  // Or check for specific class
  if (event.target.classList.contains('delete-button')) {
    deleteItem(event.target);
  }
});
```

**When to Use:**
* Lists with many items
* Dynamic content (elements added/removed)
* When you want fewer event listeners
* When child elements share similar behavior

---

## 3. DOM Traversal

```javascript
// Parent/child navigation
element.parentElement;
element.children;
element.firstElementChild;
element.lastElementChild;
element.nextElementSibling;
element.previousElementSibling;
```

---

## ⭐ Summary — 10-second Interview Version

> "DOM API provides methods to select, create, modify, and remove HTML elements. Use addEventListener for events, and event delegation for dynamic content. DOM traversal methods navigate parent/child relationships."

---

## ⭐ Extra Points (If Interviewer Asks More)

### What's the difference between textContent and innerHTML?

textContent sets plain text (safe from XSS). innerHTML sets HTML (can execute scripts, use with caution and sanitization).

### What is event delegation?

Attaching event listener to parent element instead of each child. Useful for dynamic content and better performance.

---

## Q22. Fetch API

The Fetch API is the modern way to make HTTP requests from JavaScript. It's simpler and cleaner than the old XMLHttpRequest, and it uses promises which makes handling async operations much easier. Fetch is built into modern browsers and provides a more intuitive API for making network requests.

---

## 1. Basic Fetch

### 🔹 GET Request

```javascript
fetch('https://api.example.com/users')
  .then(response => response.json())
  .then(data => console.log(data))
  .catch(error => console.error('Error:', error));
```

### 🔹 POST Request

```javascript
fetch('https://api.example.com/users', {
  method: 'POST',
  headers: {
    'Content-Type': 'application/json'
  },
  body: JSON.stringify({
    name: 'John',
    email: 'john@example.com'
  })
})
  .then(response => response.json())
  .then(data => console.log(data));
```

### 🔹 With Async/Await

Async/await makes fetch code cleaner and easier to read. It's the recommended way to use fetch in modern JavaScript.

**Basic Example:**
```javascript
async function fetchUser(userId) {
  try {
    const response = await fetch(`/api/users/${userId}`);
    if (!response.ok) {
      throw new Error(`HTTP error! status: ${response.status}`);
    }
    const user = await response.json();
    return user;
  } catch (error) {
    console.error('Error fetching user:', error);
    throw error; // Re-throw to let caller handle
  }
}
```

**Error Handling:**
* Fetch only rejects on network errors, not HTTP errors
* Always check `response.ok` or `response.status`
* Handle different error types appropriately
* Example:
```javascript
async function fetchData(url) {
  try {
    const response = await fetch(url);
    
    if (!response.ok) {
      if (response.status === 404) {
        throw new Error('Resource not found');
      } else if (response.status === 500) {
        throw new Error('Server error');
      } else {
        throw new Error(`HTTP error! status: ${response.status}`);
      }
    }
    
    return await response.json();
  } catch (error) {
    if (error.name === 'TypeError') {
      // Network error (no internet, CORS, etc.)
      console.error('Network error:', error);
    } else {
      // HTTP error or other error
      console.error('Error:', error);
    }
    throw error;
  }
}
```

**Multiple Requests:**
```javascript
// Sequential requests
async function fetchUserAndPosts(userId) {
  const user = await fetchUser(userId);
  const posts = await fetchPosts(userId);
  return { user, posts };
}

// Parallel requests (faster)
async function fetchUserAndPosts(userId) {
  const [user, posts] = await Promise.all([
    fetchUser(userId),
    fetchPosts(userId)
  ]);
  return { user, posts };
}
```

📌 **In simple terms**: Fetch is like a modern, promise-based way to talk to servers. It's much simpler than the old XMLHttpRequest - you just call `fetch()` with a URL and handle the response with `.then()` or `async/await`.

---

## 2. Request Options

### 🔹 Headers

```javascript
fetch(url, {
  headers: {
    'Content-Type': 'application/json',
    'Authorization': 'Bearer token123'
  }
});
```

### 🔹 Credentials

```javascript
fetch(url, {
  credentials: 'include' // Include cookies
});
```

### 🔹 Abort Controller

AbortController allows you to cancel fetch requests. This is useful for canceling requests when they're no longer needed (e.g., user navigates away, component unmounts).

**Basic Usage:**
```javascript
const controller = new AbortController();
const signal = controller.signal;

fetch(url, { signal })
  .then(response => response.json())
  .catch(error => {
    if (error.name === 'AbortError') {
      console.log('Request aborted');
    } else {
      console.error('Other error:', error);
    }
  });

// Abort request
controller.abort();
```

**Real-world Example - Cancel on Component Unmount:**
```javascript
function UserProfile({ userId }) {
  useEffect(() => {
    const controller = new AbortController();
    
    async function fetchUser() {
      try {
        const response = await fetch(`/api/users/${userId}`, {
          signal: controller.signal
        });
        const user = await response.json();
        setUser(user);
      } catch (error) {
        if (error.name !== 'AbortError') {
          console.error('Error:', error);
        }
      }
    }
    
    fetchUser();
    
    // Cleanup: abort request if component unmounts
    return () => {
      controller.abort();
    };
  }, [userId]);
}
```

**Timeout Example:**
```javascript
function fetchWithTimeout(url, timeout = 5000) {
  const controller = new AbortController();
  const timeoutId = setTimeout(() => controller.abort(), timeout);
  
  return fetch(url, { signal: controller.signal })
    .then(response => {
      clearTimeout(timeoutId);
      return response.json();
    })
    .catch(error => {
      clearTimeout(timeoutId);
      if (error.name === 'AbortError') {
        throw new Error('Request timeout');
      }
      throw error;
    });
}
```

---

## 3. Response Handling

```javascript
// Check status
if (response.ok) {
  // Handle success
}

// Different response types
const text = await response.text();
const json = await response.json();
const blob = await response.blob();
const arrayBuffer = await response.arrayBuffer();
```

---

## ⭐ Summary — 10-second Interview Version

> "Fetch API makes HTTP requests using promises. Supports GET, POST, and other methods. Use async/await for cleaner code. Can set headers, credentials, and abort requests with AbortController."

---

## ⭐ Extra Points (If Interviewer Asks More)

### How does fetch differ from XMLHttpRequest?

Fetch is promise-based, simpler API, and uses streams. XMLHttpRequest is callback-based and older. Fetch doesn't reject on HTTP error status codes (need to check response.ok).

### How do you handle errors in fetch?

Check response.ok, handle network errors in catch, and check response status codes for different error types.

---

## Q23. Web Storage APIs

Web Storage APIs let you store data directly in the user's browser. Think of them as different types of storage boxes - some keep data forever, some clear when you close the tab, and some can store huge amounts of structured data.

---

## 1. localStorage

### 🔹 What is localStorage?

localStorage is like a permanent storage box in your browser. When you save something to localStorage, it stays there even after you close the browser and come back later. It's perfect for things like user preferences, theme settings, or anything you want to remember about the user.

Think of it like a drawer in your desk - you put things in it, and these items stay there until you take them out. Each website has its own drawer, so one website can't see what another website stored.

### 🔹 Basic Usage

```javascript
// Set item
localStorage.setItem('username', 'john');
localStorage.setItem('user', JSON.stringify({ id: 1, name: 'John' }));

// Get item
const username = localStorage.getItem('username');
const user = JSON.parse(localStorage.getItem('user'));

// Remove item
localStorage.removeItem('username');

// Clear all
localStorage.clear();

// Get key by index
const key = localStorage.key(0);
```

### 🔹 Characteristics

* **Persistent**: Data persists after browser closes
* **Domain-specific**: Each origin has separate storage
* **Synchronous**: Blocking operations
* **Size limit**: ~5-10MB per origin
* **String storage**: Must stringify objects

📌 **In simple terms**: localStorage is like a permanent storage box in the browser - data stays there even after you close the browser, until you explicitly delete it or clear browser data.

---

## 2. sessionStorage

### 🔹 What is sessionStorage?

sessionStorage is like a temporary storage box that only exists while you have the browser tab open. As soon as you close the tab, everything in sessionStorage gets thrown away. It's perfect for temporary things like form drafts or data you only need while the user is on that page.

Think of it like a sticky note on your desk - it's useful while you're working, but you throw it away when you're done. Each browser tab has its own sticky note, so these notes don't interfere with each other.

### 🔹 Basic Usage

```javascript
// Same API as localStorage
sessionStorage.setItem('tempData', 'value');
const data = sessionStorage.getItem('tempData');
sessionStorage.removeItem('tempData');
```

### 🔹 Characteristics

* **Session-only**: Data cleared when tab closes
* **Tab-specific**: Each tab has separate storage
* **Same API**: Identical to localStorage
* **Size limit**: ~5-10MB per origin

📌 **In simple terms**: sessionStorage is like a temporary storage box - it's perfect for data you only need while the user has the tab open, like form drafts or temporary UI state.

---

## 3. IndexedDB

### 🔹 What is IndexedDB?

IndexedDB is like having a full database right in your browser. Unlike localStorage which is just simple key-value storage, IndexedDB can store complex data, create indexes for fast searching, and handle huge amounts of data. It's like the difference between a simple filing cabinet (localStorage) and a full library system (IndexedDB).

Think of it like a database on your computer - you can store thousands of records, search through them quickly, and organize them in different ways. It's more complex to use than localStorage, but much more powerful when you need to store and query large amounts of data.

### 🔹 Basic Usage

```javascript
// Open database
const request = indexedDB.open('MyDB', 1);

request.onupgradeneeded = (event) => {
  const db = event.target.result;
  const objectStore = db.createObjectStore('users', { keyPath: 'id' });
};

request.onsuccess = (event) => {
  const db = event.target.result;
  
  // Add data
  const transaction = db.transaction(['users'], 'readwrite');
  const store = transaction.objectStore('users');
  store.add({ id: 1, name: 'John' });
  
  // Get data
  const getRequest = store.get(1);
  getRequest.onsuccess = () => {
    console.log(getRequest.result);
  };
};
```

### 🔹 Characteristics

* **Large storage**: Can store much more than localStorage
* **Structured data**: Stores objects, files, blobs
* **Asynchronous**: Non-blocking operations
* **Indexed**: Can query and search data
* **Complex**: More complex API than localStorage

📌 **In simple terms**: IndexedDB is a powerful database in the browser for storing large amounts of structured data.

---

## ⭐ Summary — 10-second Interview Version

> "Web Storage includes localStorage (persistent, ~5-10MB), sessionStorage (session-only, ~5-10MB), and IndexedDB (large structured data, async). localStorage and sessionStorage use simple key-value API, IndexedDB is more complex but powerful."

---

## ⭐ Extra Points (If Interviewer Asks More)

### When to use localStorage vs sessionStorage?

Use localStorage for data that should persist (user preferences, theme). Use sessionStorage for temporary data (form drafts, temporary state).

### What are the limitations of localStorage?

Size limit (~5-10MB), synchronous (blocks main thread), string-only (must stringify), and no expiration (must manage manually).

---

## Q24. Geolocation API

The Geolocation API allows web applications to access the user's geographic location.

---

## 1. Getting Location

### 🔹 Basic Usage

```javascript
if ('geolocation' in navigator) {
  navigator.geolocation.getCurrentPosition(
    (position) => {
      console.log('Latitude:', position.coords.latitude);
      console.log('Longitude:', position.coords.longitude);
      console.log('Accuracy:', position.coords.accuracy);
    },
    (error) => {
      console.error('Error:', error.message);
    }
  );
} else {
  console.log('Geolocation not supported');
}
```

### 🔹 Options

```javascript
navigator.geolocation.getCurrentPosition(
  successCallback,
  errorCallback,
  {
    enableHighAccuracy: true,  // Use GPS if available
    timeout: 10000,            // Timeout in milliseconds
    maximumAge: 60000          // Cache age in milliseconds
  }
);
```

📌 **In simple terms**: Geolocation API gets user's location (latitude/longitude) with user permission.

---

## 2. Watching Position

```javascript
const watchId = navigator.geolocation.watchPosition(
  (position) => {
    console.log('Position updated:', position.coords);
  },
  (error) => {
    console.error('Error:', error);
  }
);

// Stop watching
navigator.geolocation.clearWatch(watchId);
```

---

## 3. Privacy & Permissions

* **User consent required**: Browser prompts for permission
* **HTTPS required**: Most browsers require HTTPS
* **Privacy**: Users can deny or revoke permission
* **Accuracy**: Varies (GPS, WiFi, IP-based)

---

## ⭐ Summary — 10-second Interview Version

> "Geolocation API gets user's location with getCurrentPosition or watchPosition. Requires user permission and HTTPS. Returns latitude, longitude, and accuracy."

---

## ⭐ Extra Points (If Interviewer Asks More)

### What happens if user denies permission?

Error callback is called with error.code === 1 (PERMISSION_DENIED). Handle gracefully and provide fallback options.

### How accurate is geolocation?

GPS: ~10-20 meters. WiFi: ~50-100 meters. IP-based: city-level. Enable highAccuracy option for better precision.

---

## Q25. Canvas API

The Canvas API provides methods to draw graphics, animations, and images on a canvas element.

---

## 1. Basic Drawing

### 🔹 Setup

```javascript
const canvas = document.getElementById('myCanvas');
const ctx = canvas.getContext('2d');
```

### 🔹 Drawing Shapes

```javascript
// Rectangle
ctx.fillStyle = 'red';
ctx.fillRect(10, 10, 100, 100);

// Circle
ctx.beginPath();
ctx.arc(150, 150, 50, 0, Math.PI * 2);
ctx.fillStyle = 'blue';
ctx.fill();

// Line
ctx.beginPath();
ctx.moveTo(0, 0);
ctx.lineTo(200, 200);
ctx.strokeStyle = 'green';
ctx.lineWidth = 5;
ctx.stroke();
```

### 🔹 Text

```javascript
ctx.font = '30px Arial';
ctx.fillStyle = 'black';
ctx.fillText('Hello Canvas', 10, 50);
```

📌 **In simple terms**: Canvas API draws graphics on a canvas element using JavaScript, useful for games, charts, and animations.

---

## 2. Images

```javascript
const img = new Image();
img.onload = () => {
  ctx.drawImage(img, 0, 0);
};
img.src = 'image.jpg';
```

---

## 3. Animations

```javascript
function animate() {
  ctx.clearRect(0, 0, canvas.width, canvas.height);
  
  // Draw frame
  ctx.fillRect(x, y, 50, 50);
  
  // Update position
  x += 1;
  
  requestAnimationFrame(animate);
}
animate();
```

---

## ⭐ Summary — 10-second Interview Version

> "Canvas API draws graphics using 2D context. Draw shapes, text, images. Use requestAnimationFrame for smooth animations. Clear canvas between frames."

---

## ⭐ Extra Points (If Interviewer Asks More)

### What's the difference between Canvas and SVG?

Canvas is pixel-based (raster), good for games and complex graphics. SVG is vector-based, good for scalable graphics and interactivity.

### How do you optimize canvas performance?

Use requestAnimationFrame, minimize redraws, use offscreen canvas for complex operations, and batch drawing operations.

---

## Q26. Web Workers API

Web Workers allow running JavaScript in background threads, preventing blocking of the main thread.

---

## 1. Creating a Worker

### 🔹 Worker File (worker.js)

```javascript
// worker.js
self.onmessage = (event) => {
  const data = event.data;
  
  // Heavy computation
  const result = performHeavyCalculation(data);
  
  // Send result back
  self.postMessage(result);
};

function performHeavyCalculation(data) {
  // Long-running task
  return data * 2;
}
```

### 🔹 Main Thread

```javascript
// Create worker
const worker = new Worker('worker.js');

// Send message to worker
worker.postMessage(100);

// Receive message from worker
worker.onmessage = (event) => {
  console.log('Result:', event.data);
};

// Handle errors
worker.onerror = (error) => {
  console.error('Worker error:', error);
};

// Terminate worker
worker.terminate();
```

📌 **In simple terms**: Web Workers run JavaScript in background threads, keeping the main thread responsive during heavy computations.

---

## 2. Shared Workers

```javascript
// Shared worker (shared-worker.js)
self.onconnect = (event) => {
  const port = event.ports[0];
  port.onmessage = (event) => {
    port.postMessage('Response from shared worker');
  };
};

// Multiple pages can connect
const worker = new SharedWorker('shared-worker.js');
worker.port.onmessage = (event) => {
  console.log(event.data);
};
worker.port.postMessage('Hello');
```

---

## 3. Limitations

* **No DOM access**: Workers can't access DOM
* **Limited APIs**: Can't use most browser APIs
* **Message passing**: Communicate via postMessage
* **Separate context**: Different global scope

---

## ⭐ Summary — 10-second Interview Version

> "Web Workers run JavaScript in background threads. Use for heavy computations to avoid blocking main thread. Communicate via postMessage. No DOM access. Use SharedWorker for multiple page connections."

---

## ⭐ Extra Points (If Interviewer Asks More)

### When should you use Web Workers?

Use for CPU-intensive tasks (image processing, data parsing, calculations) that would block the UI. Don't use for simple operations (overhead not worth it).

### How do you share data between main thread and worker?

Use postMessage to send data (structured clone algorithm). For large data, use Transferable Objects to transfer ownership without copying.

---

## Q27. Intersection Observer API

The Intersection Observer API detects when elements enter or leave the viewport, useful for lazy loading, infinite scroll, and animations.

---

## 1. Basic Usage

```javascript
const observer = new IntersectionObserver((entries) => {
  entries.forEach(entry => {
    if (entry.isIntersecting) {
      // Element is visible
      entry.target.classList.add('visible');
    } else {
      // Element is not visible
      entry.target.classList.remove('visible');
    }
  });
}, {
  root: null,           // Viewport
  rootMargin: '0px',    // Margin around root
  threshold: 0.5        // Trigger when 50% visible
});

// Observe element
const element = document.querySelector('.lazy-image');
observer.observe(element);
```

📌 **In simple terms**: Intersection Observer detects when elements become visible, perfect for lazy loading images and triggering animations.

---

## 2. Lazy Loading Images

```javascript
const imageObserver = new IntersectionObserver((entries) => {
  entries.forEach(entry => {
    if (entry.isIntersecting) {
      const img = entry.target;
      img.src = img.dataset.src;
      img.classList.remove('lazy');
      imageObserver.unobserve(img);
    }
  });
});

document.querySelectorAll('img.lazy').forEach(img => {
  imageObserver.observe(img);
});
```

---

## 3. Infinite Scroll

```javascript
const sentinel = document.querySelector('#sentinel');
const observer = new IntersectionObserver((entries) => {
  if (entries[0].isIntersecting) {
    loadMoreItems();
  }
});

observer.observe(sentinel);
```

---

## ⭐ Summary — 10-second Interview Version

> "Intersection Observer detects when elements enter/leave viewport. Use for lazy loading images, infinite scroll, and scroll animations. More efficient than scroll event listeners."

---

## ⭐ Extra Points (If Interviewer Asks More)

### Why use Intersection Observer instead of scroll events?

Intersection Observer is more performant (runs on separate thread), easier to use, and handles edge cases better. Scroll events fire frequently and can cause performance issues.

### What is the threshold option?

Threshold (0-1) determines when callback fires. 0 = any visibility, 0.5 = 50% visible, 1 = fully visible. Can be array: [0, 0.5, 1].

---

## Q28. Notification API

The Notification API displays system notifications to users, even when the browser is not in focus.

---

## 1. Requesting Permission

```javascript
// Check if supported
if ('Notification' in window) {
  // Request permission
  Notification.requestPermission().then(permission => {
    if (permission === 'granted') {
      showNotification();
    }
  });
}
```

---

## 2. Showing Notifications

```javascript
function showNotification() {
  const notification = new Notification('Title', {
    body: 'Notification body text',
    icon: '/icon.png',
    badge: '/badge.png',
    tag: 'notification-id',  // Replace previous with same tag
    requireInteraction: true, // Stay until user interacts
    data: { url: '/page' }    // Custom data
  });
  
  notification.onclick = () => {
    window.focus();
    notification.close();
  };
}
```

📌 **In simple terms**: Notification API shows system notifications. Requires user permission. Useful for alerts, messages, and reminders.

---

## 3. Service Worker Notifications

```javascript
// In service worker
self.registration.showNotification('Title', {
  body: 'Body',
  icon: '/icon.png',
  actions: [
    { action: 'view', title: 'View' },
    { action: 'close', title: 'Close' }
  ]
});

// Handle actions
self.addEventListener('notificationclick', (event) => {
  event.notification.close();
  if (event.action === 'view') {
    event.waitUntil(clients.openWindow('/page'));
  }
});
```

---

## ⭐ Summary — 10-second Interview Version

> "Notification API shows system notifications. Request permission first. Can show from main thread or service worker. Handle click events to open pages or perform actions."

---

## ⭐ Extra Points (If Interviewer Asks More)

### What's the difference between main thread and service worker notifications?

Service worker notifications work even when page is closed, support actions, and are better for background notifications. Main thread notifications only work when page is open.

### How do you handle notification permissions?

Check current permission (Notification.permission: 'default', 'granted', 'denied'). Request only when needed. Handle denied gracefully with fallback UI.

---

## Q29. Media APIs

Media APIs include APIs for accessing camera, microphone, and playing audio/video.

---

## 1. MediaDevices API (Camera/Microphone)

```javascript
// Request camera/microphone access
navigator.mediaDevices.getUserMedia({
  video: true,
  audio: true
})
  .then(stream => {
    const video = document.querySelector('video');
    video.srcObject = stream;
    video.play();
  })
  .catch(error => {
    console.error('Error accessing media:', error);
  });
```

### 🔹 Constraints

```javascript
navigator.mediaDevices.getUserMedia({
  video: {
    width: { ideal: 1280 },
    height: { ideal: 720 },
    facingMode: 'user'  // or 'environment'
  },
  audio: {
    echoCancellation: true,
    noiseSuppression: true
  }
});
```

📌 **In simple terms**: MediaDevices API accesses camera and microphone with user permission. Returns media stream that can be displayed in video element.

---

## 2. MediaRecorder API

```javascript
let mediaRecorder;
let recordedChunks = [];

navigator.mediaDevices.getUserMedia({ video: true, audio: true })
  .then(stream => {
    mediaRecorder = new MediaRecorder(stream);
    
    mediaRecorder.ondataavailable = (event) => {
      recordedChunks.push(event.data);
    };
    
    mediaRecorder.onstop = () => {
      const blob = new Blob(recordedChunks, { type: 'video/webm' });
      const url = URL.createObjectURL(blob);
      // Download or upload blob
    };
    
    mediaRecorder.start();
  });

// Stop recording
mediaRecorder.stop();
```

---

## 3. Audio/Video Elements

```javascript
const video = document.querySelector('video');

// Play/pause
video.play();
video.pause();

// Events
video.addEventListener('loadedmetadata', () => {
  console.log('Duration:', video.duration);
});

video.addEventListener('timeupdate', () => {
  console.log('Current time:', video.currentTime);
});
```

---

## ⭐ Summary — 10-second Interview Version

> "Media APIs include getUserMedia (camera/microphone), MediaRecorder (record media), and audio/video elements. Require user permission. Use constraints to specify quality and settings."

---

## ⭐ Extra Points (If Interviewer Asks More)

### How do you handle different browser support?

Check for API support (if ('mediaDevices' in navigator)), provide fallbacks, and use polyfills if needed. Test across browsers.

### What are the privacy considerations?

Always request permission, explain why you need access, allow users to revoke, and handle denied permissions gracefully.

---

## Q30. File API

The File API allows reading files selected by users through file input elements.

---

## 1. Reading Files

```javascript
const input = document.querySelector('input[type="file"]');

input.addEventListener('change', (event) => {
  const file = event.target.files[0];
  
  if (file) {
    const reader = new FileReader();
    
    // Read as text
    reader.readAsText(file);
    reader.onload = (e) => {
      console.log(e.target.result);
    };
    
    // Read as data URL (base64)
    reader.readAsDataURL(file);
    reader.onload = (e) => {
      const image = document.createElement('img');
      image.src = e.target.result;
      document.body.appendChild(image);
    };
    
    // Read as array buffer
    reader.readAsArrayBuffer(file);
  }
});
```

📌 **In simple terms**: File API reads files selected by users. Use FileReader to read as text, data URL, or array buffer.

---

## 2. File Information

```javascript
const file = event.target.files[0];
console.log('Name:', file.name);
console.log('Size:', file.size);
console.log('Type:', file.type);
console.log('Last modified:', file.lastModified);
```

---

## 3. Drag and Drop

```javascript
const dropZone = document.querySelector('.drop-zone');

dropZone.addEventListener('dragover', (e) => {
  e.preventDefault();
  dropZone.classList.add('dragover');
});

dropZone.addEventListener('drop', (e) => {
  e.preventDefault();
  const files = e.dataTransfer.files;
  handleFiles(files);
});
```

---

## ⭐ Summary — 10-second Interview Version

> "File API reads files using FileReader (readAsText, readAsDataURL, readAsArrayBuffer). Access file info (name, size, type). Support drag and drop for file selection."

---

## ⭐ Extra Points (If Interviewer Asks More)

### How do you validate file types and sizes?

Check file.type and file.size before processing. Validate on client (UX) and server (security). Show user-friendly error messages.

### What's the difference between readAsText and readAsDataURL?

readAsText reads file as string (for text files). readAsDataURL reads as base64 data URL (for images, can use directly in img src).

---

## Q31. History API

The History API allows manipulating the browser history and URL without page reloads, enabling single-page application navigation.

---

## 1. Basic Navigation

```javascript
// Push new state
history.pushState({ page: 'about' }, 'About', '/about');

// Replace current state
history.replaceState({ page: 'home' }, 'Home', '/home');

// Go back/forward
history.back();
history.forward();
history.go(-2); // Go back 2 pages
```

📌 **In simple terms**: History API changes URL and browser history without reloading page, essential for SPAs.

---

## 2. Popstate Event

```javascript
window.addEventListener('popstate', (event) => {
  const state = event.state;
  // Handle navigation based on state
  renderPage(state.page);
});
```

---

## 3. SPA Routing

```javascript
// Navigate
function navigate(path) {
  history.pushState({ path }, '', path);
  renderPage(path);
}

// Handle browser back/forward
window.addEventListener('popstate', (event) => {
  renderPage(event.state?.path || window.location.pathname);
});

// Handle link clicks
document.addEventListener('click', (e) => {
  if (e.target.matches('a[href^="/"]')) {
    e.preventDefault();
    navigate(e.target.getAttribute('href'));
  }
});
```

---

## ⭐ Summary — 10-second Interview Version

> "History API manipulates browser history with pushState/replaceState. Listen to popstate for back/forward. Essential for SPA routing without page reloads."

---

## ⭐ Extra Points (If Interviewer Asks More)

### What's the difference between pushState and replaceState?

pushState adds new history entry (back button works). replaceState replaces current entry (no new history entry). Use pushState for navigation, replaceState for redirects.

### How do you handle deep linking in SPAs?

On page load, check window.location.pathname and render appropriate page. Ensure server serves index.html for all routes (or use hash routing).

---

## Q32. WebSocket API

The WebSocket API provides full-duplex communication between client and server, enabling real-time data exchange.

---

## 1. Creating WebSocket Connection

```javascript
// Create connection
const socket = new WebSocket('wss://example.com/socket');

// Connection opened
socket.addEventListener('open', (event) => {
  console.log('Connected');
  socket.send('Hello Server!');
});

// Listen for messages
socket.addEventListener('message', (event) => {
  console.log('Message from server:', event.data);
});

// Connection closed
socket.addEventListener('close', (event) => {
  console.log('Connection closed');
});

// Handle errors
socket.addEventListener('error', (error) => {
  console.error('WebSocket error:', error);
});
```

📌 **In simple terms**: WebSocket creates persistent connection for real-time bidirectional communication, perfect for chat, live updates, and gaming.

---

## 2. Sending Data

```javascript
// Send text
socket.send('Hello');

// Send JSON
socket.send(JSON.stringify({ type: 'message', data: 'Hello' }));

// Send binary
const buffer = new ArrayBuffer(8);
socket.send(buffer);
```

---

## 3. Connection States

```javascript
// Check connection state
if (socket.readyState === WebSocket.OPEN) {
  socket.send('Message');
}

// States:
// WebSocket.CONNECTING (0)
// WebSocket.OPEN (1)
// WebSocket.CLOSING (2)
// WebSocket.CLOSED (3)
```

---

## ⭐ Summary — 10-second Interview Version

> "WebSocket API creates persistent connection for real-time communication. Use wss:// for secure connections. Send/receive messages, handle open/close/error events. Check readyState before sending."

---

## ⭐ Extra Points (If Interviewer Asks More)

### How do you handle reconnection?

Implement exponential backoff, store messages while disconnected, and reconnect on close event. Use libraries like Socket.io for built-in reconnection.

### What's the difference between WebSocket and HTTP polling?

WebSocket maintains persistent connection (lower latency, less overhead). HTTP polling makes repeated requests (simpler but less efficient). Use WebSocket for real-time needs.

---

## Q16. Socket.io Internal Working

Socket.io is a library that provides real-time bidirectional communication between client and server. It's built on top of WebSockets but adds fallback options, automatic reconnection, and room-based messaging. Understanding how Socket.io works internally helps you build reliable real-time applications like chat apps, live games, and collaborative tools.

---

## 1. What is Socket.io

### 🔹 Core Concept

Socket.io is like a smart wrapper around WebSockets that makes real-time communication more reliable and easier to use. It automatically handles connection issues, provides fallbacks, and adds useful features like rooms and namespaces.

**Key Features:**
* **WebSocket with fallbacks** - Uses WebSocket when available, falls back to polling if blocked
* **Automatic reconnection** - Reconnects automatically if connection drops
* **Room-based messaging** - Send messages to specific groups of clients
* **Event-based** - Send and receive custom events (not just messages)
* **Cross-browser** - Works on all browsers, even old ones

📌 **In simple terms**: Socket.io is like a walkie-talkie that automatically reconnects if the signal drops, and you can talk to specific groups of people.

---

## 2. Socket.io Architecture

### 🔹 Client-Server Model

**Client Side:**
* Socket.io client library connects to server
* Creates WebSocket connection (or falls back to polling)
* Listens for events and sends events

**Server Side:**
* Socket.io server listens for connections
* Manages all connected clients
* Routes events to right clients/rooms

**Connection Flow:**
```
Client → HTTP Upgrade Request → Server
Client ← WebSocket Connection ← Server
(Or falls back to polling if WebSocket fails)
```

### 🔹 Transport Layer

Socket.io uses multiple transport methods:

**1. WebSocket (Primary)**
* Full-duplex connection
* Low latency
* Efficient (no HTTP overhead after handshake)

**2. Long Polling (Fallback)**
* If WebSocket is blocked or unavailable
* Client sends request, server holds it open
* Server sends response when data available
* Client immediately sends new request

**3. Short Polling (Last Resort)**
* Regular HTTP requests at intervals
* Less efficient but works everywhere

**How Socket.io chooses:**
* Tries WebSocket first
* If blocked, falls back to long polling
* If that fails, uses short polling

---

## 3. Connection Establishment

### 🔹 Step 1: HTTP Handshake

When client connects:

* Client sends HTTP request to Socket.io server
* Request includes upgrade header (wants WebSocket)
* Server responds with connection details
* Includes session ID, transport method, heartbeat interval

**Handshake Request:**
```
GET /socket.io/?EIO=4&transport=polling
Host: example.com
Upgrade: websocket
Connection: Upgrade
```

**Handshake Response:**
```json
{
  "sid": "session_id_here",
  "upgrades": ["websocket"],
  "pingInterval": 25000,
  "pingTimeout": 20000
}
```

### 🔹 Step 2: Transport Upgrade

**If WebSocket available:**
* Client sends WebSocket upgrade request
* Server upgrades connection
* Now using WebSocket (faster, more efficient)

**If WebSocket blocked:**
* Stays on long polling
* Client sends periodic requests
* Server responds when data available

### 🔹 Step 3: Connection Established

* Client and server are now connected
* Both can send/receive events
* Heartbeat mechanism starts (keeps connection alive)

---

## 4. Event-Based Communication

### 🔹 How Events Work

Socket.io uses events instead of just sending raw messages:

**Client sends event:**
```javascript
socket.emit('chat-message', { text: 'Hello', user: 'John' });
```

**Server receives event:**
```javascript
socket.on('chat-message', (data) => {
  console.log(data.text); // 'Hello'
});
```

**Server sends event:**
```javascript
io.emit('user-joined', { username: 'John' });
```

**Client receives event:**
```javascript
socket.on('user-joined', (data) => {
  console.log(data.username); // 'John'
});
```

### 🔹 Event Types

**Built-in Events:**
* `connect` - Connection established
* `disconnect` - Connection lost
* `error` - Error occurred
* `reconnect` - Reconnected after disconnect

**Custom Events:**
* You define your own events
* Like `chat-message`, `player-action`, `game-update`
* More semantic than just "message"

---

## 5. Room-Based Messaging

### 🔹 What are Rooms

Rooms are like channels or groups. You can send messages to all clients in a room, not just one client.

**Use cases:**
* **Chat rooms** - Send message to everyone in room
* **Game rooms** - Send game update to all players
* **Private rooms** - Send to specific user

### 🔹 How Rooms Work

**Client joins room:**
```javascript
socket.join('room-123');
```

**Server sends to room:**
```javascript
io.to('room-123').emit('message', 'Hello room!');
```

**Only clients in room-123 receive the message**

**Client leaves room:**
```javascript
socket.leave('room-123');
```

### 🔹 Namespaces

Namespaces are like separate Socket.io instances:

* `/` - Default namespace
* `/admin` - Admin namespace
* `/game` - Game namespace

**Use cases:**
* Separate different parts of app
* Different authentication per namespace
* Different rooms per namespace

---

## 6. Automatic Reconnection

### 🔹 How Reconnection Works

**When connection drops:**
* Socket.io detects disconnection
* Automatically tries to reconnect
* Uses exponential backoff (waits longer each time)

**Reconnection attempts:**
* First attempt: immediate
* Second attempt: wait 1 second
* Third attempt: wait 2 seconds
* Fourth attempt: wait 4 seconds
* And so on...

**Maximum attempts:**
* Default: unlimited (keeps trying)
* Can configure max attempts

### 🔹 Reconnection Events

**Client side:**
```javascript
socket.on('disconnect', () => {
  console.log('Disconnected');
});

socket.on('reconnect', (attemptNumber) => {
  console.log('Reconnected after', attemptNumber, 'attempts');
});

socket.on('reconnect_attempt', () => {
  console.log('Trying to reconnect...');
});
```

---

## 7. Heartbeat Mechanism

### 🔹 Why Heartbeat

Socket.io uses heartbeat to detect if connection is still alive:

* **Ping** - Server sends ping to client
* **Pong** - Client responds with pong
* If no pong received, connection is dead

**How it works:**
* Server sends ping every `pingInterval` (default 25 seconds)
* Client must respond with pong within `pingTimeout` (default 20 seconds)
* If no pong, server considers connection dead

**Benefits:**
* Detects dead connections quickly
* Cleans up disconnected clients
* Keeps connection alive (prevents timeout)

---

## 8. Socket.io vs WebSocket

### 🔹 What Socket.io Adds

**WebSocket:**
* Raw WebSocket connection
* No automatic reconnection
* No fallback options
* No room support
* Just send/receive messages

**Socket.io:**
* WebSocket + fallbacks
* Automatic reconnection
* Room-based messaging
* Event-based (not just messages)
* Namespaces
* Heartbeat mechanism

**When to use WebSocket:**
* Simple use case
* Don't need fallbacks
* Want minimal overhead

**When to use Socket.io:**
* Need reliability (reconnection)
* Need to support old browsers
* Want room-based messaging
* Want easier API

---

---

## 9. Frontend Implementation (React.js)

### 🔹 Socket.io Client Setup

**Basic Connection:**

```javascript
// Frontend: hooks/useSocket.ts
import { useEffect, useState } from 'react';
import { io, Socket } from 'socket.io-client';

const useSocket = (userId: string) => {
  const [socket, setSocket] = useState<Socket | null>(null);
  const [isConnected, setIsConnected] = useState(false);
  
  useEffect(() => {
    const token = localStorage.getItem('accessToken');
    
    // Create Socket.io connection
    const newSocket = io(process.env.REACT_APP_SOCKET_URL, {
      auth: {
        token // Send JWT token for authentication
      },
      transports: ['websocket', 'polling'], // Try WebSocket first, fallback to polling
      reconnection: true,
      reconnectionDelay: 1000,
      reconnectionDelayMax: 5000,
      reconnectionAttempts: Infinity
    });
    
    // Connection events
    newSocket.on('connect', () => {
      console.log('Connected to server');
      setIsConnected(true);
      
      // Join user's notification room
      newSocket.emit('join-room', `user:${userId}`);
    });
    
    newSocket.on('disconnect', () => {
      console.log('Disconnected from server');
      setIsConnected(false);
    });
    
    newSocket.on('connect_error', (error) => {
      console.error('Connection error:', error);
    });
    
    newSocket.on('reconnect', (attemptNumber) => {
      console.log(`Reconnected after ${attemptNumber} attempts`);
    });
    
    newSocket.on('reconnect_attempt', () => {
      console.log('Attempting to reconnect...');
    });
    
    setSocket(newSocket);
    
    // Cleanup on unmount
    return () => {
      newSocket.close();
    };
  }, [userId]);
  
  return { socket, isConnected };
};
```

**Receiving Events:**

```javascript
// Frontend: components/NotificationComponent.tsx
const NotificationComponent: React.FC = () => {
  const { socket } = useSocket(userId);
  const [notifications, setNotifications] = useState<Notification[]>([]);
  
  useEffect(() => {
    if (!socket) return;
    
    // Listen for notification event
    socket.on('notification', (notification: Notification) => {
      setNotifications(prev => [notification, ...prev]);
      
      // Show browser notification
      if ('Notification' in window && Notification.permission === 'granted') {
        new Notification(notification.title, {
          body: notification.message,
          icon: '/icon.png'
        });
      }
    });
    
    // Listen for custom events
    socket.on('message', (data) => {
      console.log('Received message:', data);
    });
    
    // Cleanup listeners
    return () => {
      socket.off('notification');
      socket.off('message');
    };
  }, [socket]);
  
  return <div>{/* Render notifications */}</div>;
};
```

**Sending Events:**

```javascript
// Frontend: components/ChatComponent.tsx
const ChatComponent: React.FC = () => {
  const { socket } = useSocket(userId);
  
  const sendMessage = (message: string) => {
    if (!socket || !socket.connected) {
      console.error('Socket not connected');
      return;
    }
    
    // Emit custom event
    socket.emit('chat-message', {
      roomId: 'room-123',
      message,
      userId,
      timestamp: Date.now()
    });
  };
  
  return <input onKeyPress={(e) => {
    if (e.key === 'Enter') {
      sendMessage(e.currentTarget.value);
    }
  }} />;
};
```

---

## 10. Backend Implementation (Node.js/Express.js)

### 🔹 Socket.io Server Setup

**Basic Server:**

```javascript
// Backend: server.js
import { Server } from 'socket.io';
import { createServer } from 'http';
import express from 'express';

const app = express();
const httpServer = createServer(app);

const io = new Server(httpServer, {
  cors: {
    origin: process.env.FRONTEND_URL,
    methods: ['GET', 'POST']
  },
  transports: ['websocket', 'polling']
});

// Authentication middleware
io.use(async (socket, next) => {
  const token = socket.handshake.auth.token;
  
  try {
    // Verify JWT token
    const decoded = jwt.verify(token, process.env.JWT_SECRET);
    const user = await User.findById(decoded.userId);
    
    if (!user) {
      return next(new Error('User not found'));
    }
    
    // Attach user to socket
    socket.data.userId = user.id;
    socket.data.user = user;
    
    next();
  } catch (error) {
    next(new Error('Authentication failed'));
  }
});

// Handle connections
io.on('connection', (socket) => {
  const userId = socket.data.userId;
  console.log(`User ${userId} connected`);
  
  // Join user's notification room
  socket.join(`user:${userId}`);
  
  // Handle room joining
  socket.on('join-room', (roomId: string) => {
    socket.join(roomId);
    console.log(`User ${userId} joined room ${roomId}`);
    
    // Notify others in room
    socket.to(roomId).emit('user-joined', { userId });
  });
  
  // Handle room leaving
  socket.on('leave-room', (roomId: string) => {
    socket.leave(roomId);
    socket.to(roomId).emit('user-left', { userId });
  });
  
  // Handle custom events
  socket.on('chat-message', async (data) => {
    const { roomId, message } = data;
    
    // Validate and process message
    // Save to database
    await Message.create({
      roomId,
      userId,
      message,
      createdAt: new Date()
    });
    
    // Broadcast to room
    io.to(roomId).emit('new-message', {
      userId,
      message,
      timestamp: Date.now()
    });
  });
  
  // Handle disconnection
  socket.on('disconnect', () => {
    console.log(`User ${userId} disconnected`);
    // Cleanup, notify others, etc.
  });
});

httpServer.listen(3000);
```

**Redis Adapter for Scaling:**

```javascript
// Backend: server.js
import { createAdapter } from '@socket.io/redis-adapter';
import { createClient } from 'redis';

const pubClient = createClient({ url: process.env.REDIS_URL });
const subClient = pubClient.duplicate();

await Promise.all([pubClient.connect(), subClient.connect()]);

io.adapter(createAdapter(pubClient, subClient));

// Now multiple servers can share Socket.io connections
// When one server emits, Redis broadcasts to all servers
```

---

## ⭐ Summary — 10-second Interview Version

> "Socket.io is a library built on WebSockets that adds automatic reconnection, fallback to polling if WebSocket is blocked, room-based messaging, and event-based communication. It uses HTTP handshake first, then upgrades to WebSocket. Has heartbeat mechanism to detect dead connections. Supports rooms for group messaging and namespaces for separating app parts."

---

## ⭐ Extra Points (If Interviewer Asks More)

### How does Socket.io handle scaling across multiple servers?

Use Redis adapter - all servers connect to Redis, Redis broadcasts events to all servers. When one server receives event, Redis sends it to all other servers, which then send to their connected clients.

### What's the difference between `socket.emit` and `io.emit`?

`socket.emit` sends to one client. `io.emit` sends to all connected clients. `io.to('room').emit` sends to all clients in a room.

### How do you handle authentication with Socket.io?

Send token during handshake, server validates token before accepting connection. Can also use middleware to authenticate each event.

### How do you handle Socket.io reconnection in React?

Use Socket.io's built-in reconnection with exponential backoff. Store messages while disconnected. Show connection status to user. Re-sync state when reconnected.

### What's the difference between Socket.io and native WebSocket?

Socket.io adds automatic reconnection, fallback to polling, room-based messaging, and event-based communication. Native WebSocket is lower-level, requires manual reconnection handling.

---

<div align="center">

**[← Previous: How React Native Works Internally](06%29%20How%20React%20Native%20Works%20Internally.md)** | **[Next: High Level Design (HLD) →](08%29%20High%20Level%20Design%20%28HLD%29.md)**

</div>