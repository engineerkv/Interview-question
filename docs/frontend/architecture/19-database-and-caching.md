---
sidebar_label: "Database & Caching"
---
# 💾 Database & Caching

---

## 1. 💡 Local Storage

Local Storage is a browser API that allows you to store data in the user's browser that persists even after you close the tab or browser. It's like a permanent sticky note that stays until you explicitly delete it or the user clears their browser data. Understanding when and how to use local storage effectively is important for building applications that provide a good user experience.

### 🔹 How It Works

* **Persistent storage**: Data stays even after browser closes

* **Domain-specific**: Each website has its own storage - site A can't access site B's data

* **Key-value pairs**: Store data as strings (you need to JSON.stringify/parse for objects)

* **Size limit**: Usually 5-10MB per domain (varies by browser)

### 🔹 When to Use

* **User preferences**: Theme, language, settings

* **Cached data**: API responses you want to keep for a while

* **Draft content**: Save form data so users don't lose work

* **Shopping cart**: Keep items even if user closes browser

### 🔹 Example

```javascript
// Save data
localStorage.setItem('theme', 'dark');
localStorage.setItem('userPrefs', JSON.stringify({ language: 'en', notifications: true }));

// Read data
const theme = localStorage.getItem('theme'); // 'dark'
const prefs = JSON.parse(localStorage.getItem('userPrefs')); // { language: 'en', notifications: true }

// Remove data
localStorage.removeItem('theme');
localStorage.clear(); // Remove everything

```

📌 **In simple terms**: Local Storage is permanent browser storage for your site. Use it for user preferences, cached data, or anything that should persist across sessions.

---

### 🔹 💡 Session Storage

Session Storage is like Local Storage, but it only lasts for the current browser tab session. Close the tab, and the data is gone. It's perfect for temporary data that you only need while the user is actively using your site.

### 🔹 How It Works

* **Temporary storage**: Data is cleared when the tab/window closes

* **Tab-specific**: Each tab has its own session storage - open two tabs, and you'll have separate data in each

* **Same API as Local Storage**: `setItem`, `getItem`, `removeItem`, `clear`

* **Size limit**: Usually 5-10MB per domain

### 🔹 When to Use

* **Form data**: Save progress while user fills out a multi-step form

* **Temporary state**: Shopping cart items, filters, search history for current session

* **Tab-specific data**: Data that shouldn't persist across sessions

* **Sensitive data**: Tokens or data you don't want to persist

### 🔹 Example

```javascript
// Save temporary data
sessionStorage.setItem('formStep', '3');
sessionStorage.setItem('cart', JSON.stringify([{ id: 1, name: 'Product' }]));

// Read data
const step = sessionStorage.getItem('formStep'); // '3'

// Data is automatically cleared when tab closes

```

📌 **In simple terms**: Session Storage is temporary browser storage that only lasts for the current tab session. Use it for temporary data, form progress, or anything that shouldn't persist.

---

### 🔹 💡 Cookie Storage

Cookies are small pieces of data that browsers send to the server with every request. Cookies are the oldest browser storage mechanism and are still widely used for authentication, tracking, and storing small amounts of data.

### 🔹 How Cookies Work

* **Sent with requests**: Browser automatically includes cookies in HTTP headers

* **Server and client accessible**: Can be set by server (Set-Cookie header) or client (document.cookie)

* **Size limit**: Very small - only 4KB per cookie

* **Expiration**: Can have expiration date or be session-only

* **Domain/path scoped**: Can restrict which pages can access the cookie

### 🔹 When to Use

* **Authentication tokens**: Session IDs, JWT tokens (though httpOnly cookies are safer)

* **Server-side needs**: When server needs to read the data

* **Tracking**: Analytics, user preferences (with consent)

* **Small data**: User preferences, theme, language

### 🔹 Example

```javascript
// Set cookie (client-side)
document.cookie = 'theme=dark; expires=Thu, 18 Dec 2025 12:00:00 UTC; path=/';

// Read cookies
const cookies = document.cookie; // 'theme=dark; language=en'
// Need to parse manually or use a library

// Delete cookie (set expiration in past)
document.cookie = 'theme=; expires=Thu, 01 Jan 1970 00:00:00 UTC; path=/';

```

📌 **In simple terms**: Cookies are small data pieces sent to the server with every request. Use them when the server needs the data, for authentication, or for small preferences. Limited to 4KB.

---

### 🔹 📇 IndexedDB

IndexedDB is a powerful browser database that can store large amounts of structured data. Think of it as a full database in the browser - it supports indexes, transactions, and can store complex objects, files, and blobs.

### 🔹 How It Works

* **Large storage**: Can store much more than Local Storage (hundreds of MB or more)

* **Structured data**: Stores objects with indexes for fast queries

* **Asynchronous API**: Uses promises or callbacks (not synchronous like Local Storage)

* **Transactions**: Supports ACID-like transactions for data integrity

* **Indexes**: Can create indexes on object properties for fast lookups

### 🔹 When to Use

* **Large datasets**: Storing lots of data (cached API responses, offline data)

* **Complex queries**: Need to search, filter, or sort data

* **Files and blobs**: Store images, videos, or other binary data

* **Offline-first apps**: Store data for offline access

### 🔹 Example

```javascript
// Open database
const request = indexedDB.open('MyDB', 1);

request.onsuccess = (event) => {
  const db = event.target.result;

  // Create transaction
  const transaction = db.transaction(['users'], 'readwrite');
  const store = transaction.objectStore('users');

  // Add data
  store.add({ id: 1, name: 'John', email: 'john@example.com' });

  // Query data
  const getRequest = store.get(1);
  getRequest.onsuccess = () => {
    console.log(getRequest.result); // { id: 1, name: 'John', ... }
  };
};

```

📌 **In simple terms**: IndexedDB is a full database in the browser for storing large amounts of structured data. Use it when you need to store lots of data, query it efficiently, or work offline.

---

### 🔹 💡 Data Normalization

Normalization is organizing your data so you don't store the same information in multiple places. It's about having one source of truth for each piece of data, which makes updates easier and prevents inconsistencies.

### 🔹 The Problem

When data is nested or duplicated, you end up with problems:

```javascript
// ❌ Nested structure - data is duplicated
{
  users: [
    {
      id: '1',
      name: 'John',
      posts: [
        { id: '1', title: 'Post 1', author: 'John' }, // John's name duplicated
        { id: '2', title: 'Post 2', author: 'John' }  // John's name duplicated again
      ]
    }
  ]
}

```

### 🔹 The Solution

Store each type of data separately and reference them:

```javascript
// ✅ Normalized structure - single source of truth
{
  users: {
    '1': { id: '1', name: 'John' } // John's data in one place
  },
  posts: {
    '1': { id: '1', title: 'Post 1', userId: '1' }, // Reference to user
    '2': { id: '2', title: 'Post 2', userId: '1' }  // Reference to user
  }
}

```

### 🔹 Benefits

* **No duplication**: Store data once, reference it everywhere

* **Easier updates**: Change John's name in one place, it updates everywhere

* **Better performance**: No deep object traversal, faster lookups

* **Consistent data**: Can't have John's name be different in different places

📌 **In simple terms**: Normalization means storing each piece of data once and referencing it, instead of duplicating it. Makes updates easier and data more consistent.

---

### 🔹 🌐 HTTP Caching

HTTP caching uses browser and server mechanisms to store responses so you don't have to fetch the same data repeatedly. It's one of the most effective ways to make your app faster.

### 🔹 Browser Cache

* **Automatic**: Browser automatically caches responses based on headers

* **Fast**: Served from memory/disk, no network request

* **Controlled by headers**: `Cache-Control`, `ETag`, `Last-Modified`

### 🔹 Cache Headers

* **Cache-Control**: Tells browser how long to cache
  * `max-age=3600` - Cache for 1 hour
  * `no-cache` - Must revalidate with server
  * `no-store` - Don't cache at all

* **ETag**: Unique identifier for resource version

* **Last-Modified**: When resource was last changed

### 🔹 When to Use

* **Static assets**: Images, CSS, JS files - cache aggressively

* **API responses**: Cache GET requests that don't change often

* **Public data**: Data that's the same for all users

### 🔹 Example

```javascript
// Server sets cache headers
res.setHeader('Cache-Control', 'public, max-age=3600'); // Cache for 1 hour
res.setHeader('ETag', 'abc123');

// Browser automatically caches and reuses
fetch('/api/users'); // First request - goes to server
fetch('/api/users'); // Second request - served from cache (if within max-age)

```

📌 **In simple terms**: HTTP caching stores responses in the browser so repeated requests are served instantly. Control it with Cache-Control headers. Essential for performance.

---

### 🔹 💾 Service Worker Caching

Service Worker caching allows you to programmatically control what gets cached and how it's served. Unlike HTTP caching (which is automatic), you write code to decide caching strategies.

### 🔹 Programmatic Control

* **You decide**: Write code to control what gets cached and when

* **Offline support**: Can serve cached content when offline

* **Flexible strategies**: Cache-first, network-first, stale-while-revalidate

### 🔹 Common Strategies

* **Cache-first**: Check cache first, fallback to network - good for static assets

* **Network-first**: Try network first, fallback to cache - good for dynamic data

* **Stale-while-revalidate**: Serve from cache immediately, update in background

### 🔹 Example

```javascript
// Service Worker
self.addEventListener('fetch', (event) => {
  if (event.request.url.includes('/api/')) {
    // Network-first for API calls
    event.respondWith(
      fetch(event.request)
        .catch(() => caches.match(event.request)) // Fallback to cache
    );
  } else {
    // Cache-first for static assets
    event.respondWith(
      caches.match(event.request)
        .then(response => response || fetch(event.request))
    );
  }
});

```

📌 **In simple terms**: Service Worker caching gives you programmatic control over caching. You write code to decide what to cache and how to serve it, enabling offline support.

---

### 🔹 💾 API Caching

API caching stores API responses so you don't make the same request repeatedly. It reduces server load, improves performance, and can enable offline functionality.

### 🔹 Client-Side Caching

* **In-memory cache**: Store responses in JavaScript (React Query, SWR)

* **Local Storage**: Persist responses across sessions

* **Service Worker**: Cache API responses for offline access

### 🔹 When to Cache

* **Read-heavy data**: Data that doesn't change often (user profile, product catalog)

* **Expensive requests**: Slow or costly API calls

* **Offline support**: Cache critical data for offline access

### 🔹 Cache Invalidation

* **Time-based**: Cache expires after X minutes

* **Event-based**: Invalidate when data changes (user updates profile)

* **Manual**: Clear cache on user action (refresh button)

### 🔹 Example with React Query

```javascript
import { useQuery } from '@tanstack/react-query';

// Automatically caches and deduplicates requests
const { data } = useQuery({
  queryKey: ['user', userId],
  queryFn: () => fetchUser(userId),
  staleTime: 5 * 60 * 1000, // Consider fresh for 5 minutes
  cacheTime: 10 * 60 * 1000, // Keep in cache for 10 minutes
});

```

📌 **In simple terms**: API caching stores API responses to avoid repeated requests. Use tools like React Query or SWR for automatic caching, or implement your own with Local Storage or Service Workers.

---

### 🔹 📦 State Management

State management is how you store and share data across your app. When multiple components need the same data, you need a way to manage it centrally so everything stays in sync.

### 🔹 Local State

* **Component-specific**: Only one component needs it

* **Examples**: Form inputs, modal open/closed, UI state

* **Tools**: `useState` in React

### 🔹 Global State

* **Shared across app**: Multiple components need it

* **Examples**: User info, theme, shopping cart

* **Tools**: Context API, Redux, Zustand

### 🔹 Server State

* **Data from APIs**: Needs caching and synchronization

* **Examples**: API responses, user data, product list

* **Tools**: React Query, SWR

### 🔹 When to Use What

* **Local state**: Component-specific UI state

* **Global state**: Shared app state (user, theme)

* **Server state**: API data (use React Query/SWR)

📌 **In simple terms**: Use local state for component-specific data, global state for shared app data, and server state tools (React Query) for API data with caching.

---

## ⭐ Summary — 10-second Interview Version

> "Browser storage includes localStorage (persistent, 5-10MB), sessionStorage (temporary, tab-specific), cookies (4KB, sent to server), and IndexedDB (large structured data). HTTP caching uses Cache-Control headers. Service Worker caching provides programmatic control. API caching uses React Query/SWR. State management handles local, global, and server state. Normalization prevents data duplication."

---

