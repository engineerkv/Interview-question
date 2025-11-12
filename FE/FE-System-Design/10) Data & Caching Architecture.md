# 💾 10. Data & Caching Architecture (Q121–138)

---

## 🧩 Q121. What is data normalization in frontend apps and why is it important?

### 🧠 Concept

Normalization flattens nested API responses into entity maps keyed by IDs, storing relationships by references. It prevents duplication, simplifies updates, and avoids inconsistent UI state. Normalize at the boundary: on fetch or in state adapters.

---

### 💡 Example

```javascript
// Raw nested API response
const response = {
  id: 'post-1',
  title: 'Hello',
  author: { id: 'user-1', name: 'Ada' },
  comments: [
    { id: 'c-1', text: 'Nice', author: { id: 'user-2', name: 'Lin' }},
    { id: 'c-2', text: 'Wow', author: { id: 'user-1', name: 'Ada' }}
  ]
};

// Normalized state
const entities = {
  users: {
    'user-1': { id: 'user-1', name: 'Ada' },
    'user-2': { id: 'user-2', name: 'Lin' }
  },
  comments: {
    'c-1': { id: 'c-1', text: 'Nice', authorId: 'user-2' },
    'c-2': { id: 'c-2', text: 'Wow', authorId: 'user-1' }
  },
  posts: {
    'post-1': { id: 'post-1', title: 'Hello', authorId: 'user-1', commentIds: ['c-1', 'c-2'] }
  }
};
```

---

### 🔍 Deep Insights

* **Rule:** Eliminates duplication, enabling single-source-of-truth updates.
* **Use Case:** Improves rendering performance (smaller diffs, memoized selectors).
* **Common Mistake:** Works well with entity adapters (Redux Toolkit `createEntityAdapter`).
* **Pro Tip:** Use selectors to re-compose nested shapes for views.

---

### ⭐ Senior Takeaway

Normalize at the boundary: on fetch or in state adapters.

---

## 🧩 Q122. How does normalization improve efficiency and maintainability?

### 🧠 Concept

It reduces redundant data, minimizes re-renders, and simplifies updates by changing a single entity rather than multiple locations holding the same data. Normalization reduces memory usage and improves performance.

---

### 💡 Example

```javascript
// Update user name once; reflected across all posts/comments
dispatch(usersSlice.actions.userUpdated({ id: 'user-1', changes: { name: 'Ada Lovelace' } }));
```

---

### 🔍 Deep Insights

* **Rule:** Fewer state writes → fewer component updates.
* **Use Case:** Predictable updates: IDs + references make diffs trivial.
* **Common Mistake:** Easier cache invalidation: invalidate by entity type/id.
* **Pro Tip:** Single update propagates to all references automatically.

---

### ⭐ Senior Takeaway

Normalization reduces memory usage and improves performance.

---

## 🧩 Q123. Local state vs global state: when to use each?

### 🧠 Concept

Local state (component-level) is ideal for UI concerns (inputs, toggles). Global state manages cross-cutting concerns (auth, user profile), shared data (entities), and server cache. Start with local state, move to global only when needed.

---

### 💡 Example

```javascript
// Local state for form input
function SearchBox() {
  const [query, setQuery] = useState('');
  return <input value={query} onChange={e => setQuery(e.target.value)} />;
}

// Global state for current user
const user = useSelector(state => state.auth.user);
```

---

### 🔍 Deep Insights

* **Rule:** Prefer local state by default; promote to global only when truly shared.
* **Use Case:** Server cache (React Query/RTK Query) is not the same as app state.
* **Common Mistake:** Avoid over-globalizing (causes needless re-renders and coupling).
* **Pro Tip:** Use local state for UI, global state for business logic and shared data.

---

### ⭐ Senior Takeaway

Start with local state, move to global only when needed.

---

## 🧩 Q124. Pros and cons of state management libraries (Redux, Vuex, etc.)

### 🧠 Concept

Libraries provide structure, tooling (DevTools), and performance patterns (memoization, entity adapters), but add boilerplate and learning curve. Choose based on app complexity and team preferences.

---

### 💡 Example

```javascript
// Redux Toolkit example
const usersAdapter = createEntityAdapter();
const usersSlice = createSlice({
  name: 'users',
  initialState: usersAdapter.getInitialState(),
  reducers: {
    userAdded: usersAdapter.addOne,
    userUpdated: usersAdapter.updateOne,
    usersReceived: usersAdapter.setAll
  }
});
```

---

### 🔍 Deep Insights

* **Rule:** Use RTK/RTK Query to reduce boilerplate, enforce good patterns.
* **Use Case:** Choose simpler stores (Zustand, Jotai) for small apps.
* **Common Mistake:** Keep server cache in a dedicated tool (React Query/RTK Query).
* **Pro Tip:** DevTools provide time-travel debugging and state inspection.

---

### ⭐ Senior Takeaway

Choose based on app complexity and team preferences.

---

## 🧩 Q125. What is HTTP caching and why does it matter?

### 🧠 Concept

HTTP caching stores responses to serve subsequent requests faster. It reduces latency, bandwidth, and server load. Caching is crucial for performance at scale.

---

### 💡 Example

```http
Cache-Control: public, max-age=3600
ETag: "abc123"
Last-Modified: Wed, 21 Oct 2025 07:28:00 GMT
```

---

### 🔍 Deep Insights

* **Rule:** Leverage immutable asset versioning: `/main.8fd2a.js` → `Cache-Control: max-age=31536000, immutable`.
* **Use Case:** Use `ETag`/`If-None-Match` for validation.
* **Common Mistake:** Prefer CDN caching for public GET endpoints.
* **Pro Tip:** HTTP caching reduces server load and improves user experience.

---

### ⭐ Senior Takeaway

Caching is crucial for performance at scale.

---

## 🧩 Q126. What do common caching headers do?

### 🧠 Concept

They control freshness and validation of cached responses. Caching headers control browser and CDN behavior.

---

### 💡 Example

```http
// Freshness
Cache-Control: max-age=600, stale-while-revalidate=60

// Validation
ETag: "v1"
If-None-Match: "v1"

Last-Modified: Wed, 21 Oct 2025 07:28:00 GMT
If-Modified-Since: Wed, 21 Oct 2025 07:28:00 GMT

// Legacy
Expires: Wed, 22 Oct 2025 07:28:00 GMT
```

---

### 🔍 Deep Insights

* **Rule:** Prefer `Cache-Control` over `Expires`.
* **Use Case:** Combine `stale-while-revalidate` for better UX.
* **Common Mistake:** Use validators to avoid transferring large payloads when unchanged.
* **Pro Tip:** `stale-while-revalidate` serves stale content while fetching fresh data.

---

### ⭐ Senior Takeaway

Caching headers control browser and CDN behavior.

---

## 🧩 Q127. How do you implement API caching strategies?

### 🧠 Concept

Strategies balance freshness and speed: cache-first (fast), network-first (fresh), stale-while-revalidate (best perceived performance). Choose strategy based on data freshness requirements.

---

### 💡 Example

```javascript
// Stale-While-Revalidate with React Query
const { data, isFetching } = useQuery(['posts'], fetchPosts, {
  staleTime: 60_000, // 1 minute
  cacheTime: 5 * 60_000, // 5 minutes
});
```

---

### 🔍 Deep Insights

* **Rule:** For public data: cache-first/SWR, For user-specific data: network-first with background refresh.
* **Use Case:** Tune `staleTime` based on data volatility.
* **Common Mistake:** Use stale-while-revalidate for best perceived performance.
* **Pro Tip:** Cache-first for static data, network-first for dynamic data.

---

### ⭐ Senior Takeaway

Choose strategy based on data freshness requirements.

---

## 🧩 Q128. Cache invalidation and expiration: how to approach?

### 🧠 Concept

Expiration sets time-based freshness; invalidation proactively removes/updates cache when data changes. Invalidate only what changed, not everything.

---

### 💡 Example

```javascript
// React Query invalidation
queryClient.invalidateQueries(['posts']);

// RTK Query
api.util.invalidateTags([{ type: 'Post', id: 'LIST' }]);
```

---

### 🔍 Deep Insights

* **Rule:** Prefer tag-based invalidation to target minimal subsets.
* **Use Case:** Emit domain events to trigger invalidations after mutations.
* **Common Mistake:** Avoid global cache clears (hurts UX).
* **Pro Tip:** Tag-based invalidation allows fine-grained cache control.

---

### ⭐ Senior Takeaway

Invalidate only what changed, not everything.

---

## 🧩 Q129. What is a service worker and how can it be used for caching?

### 🧠 Concept

A Service Worker is a background script that intercepts network requests, enabling offline caching, background sync, and push notifications. Service workers run in background, separate from main thread.

---

### 💡 Example

```javascript
// Basic SW install + precache
self.addEventListener('install', (event) => {
  event.waitUntil(
    caches.open('app-v1').then((cache) => cache.addAll([
      '/', '/index.html', '/styles.css', '/main.js'
    ]))
  );
});

// Fetch handler: cache-first
self.addEventListener('fetch', (event) => {
  event.respondWith(
    caches.match(event.request).then((cached) => cached || fetch(event.request))
  );
});
```

---

### 🔍 Deep Insights

* **Rule:** Choose strategy per route (HTML: network-first; assets: cache-first).
* **Use Case:** Version and cleanup old caches on `activate`.
* **Common Mistake:** Use Workbox to manage complex strategies safely.
* **Pro Tip:** Service workers enable offline functionality and background sync.

---

### ⭐ Senior Takeaway

Service workers run in background, separate from main thread.

---

## 🧩 Q130. Service worker caching vs traditional browser caching

### 🧠 Concept

Browser caching obeys HTTP headers, SW caching gives app-controlled policies independent of headers and supports offline. Service workers enable offline-first applications.

---

### 💡 Example

```javascript
// Workbox runtime caching (NetworkFirst)
workbox.routing.registerRoute(
  ({ request }) => request.destination === 'document',
  new workbox.strategies.NetworkFirst({
    cacheName: 'pages',
    plugins: [new workbox.expiration.ExpirationPlugin({ maxEntries: 50 })]
  })
);
```

---

### 🔍 Deep Insights

* **Rule:** SW can cache POST results and custom responses.
* **Use Case:** Beware of stale HTML—use network-first for documents.
* **Common Mistake:** Always handle SW updates to avoid stuck old versions.
* **Pro Tip:** Service workers provide programmatic cache control.

---

### ⭐ Senior Takeaway

Service workers enable offline-first applications.

---

## 🧩 Q131. Designing SW caching strategies (precache vs runtime)

### 🧠 Concept

Precache static assets at build; runtime-cache dynamic requests with strategy per route. Precache for static assets, runtime cache for dynamic content.

---

### 💡 Example

```javascript
// Precache manifest generated at build
workbox.precaching.precacheAndRoute(self.__WB_MANIFEST);

// Runtime caching for images (CacheFirst)
workbox.routing.registerRoute(
  ({ request }) => request.destination === 'image',
  new workbox.strategies.CacheFirst({
    cacheName: 'images',
    plugins: [new workbox.expiration.ExpirationPlugin({ maxEntries: 200, maxAgeSeconds: 7*24*3600 })]
  })
);
```

---

### 🔍 Deep Insights

* **Rule:** Documents/network-first; APIs/SWR or network-first; images/cache-first; fonts/cache-first + long TTL.
* **Use Case:** Use revisioned filenames to enable immutable caching.
* **Common Mistake:** Precache critical assets at build time.
* **Pro Tip:** Runtime caching handles dynamic requests with appropriate strategies.

---

### ⭐ Senior Takeaway

Precache for static assets, runtime cache for dynamic content.

---

## 🧩 Q132. What is LocalStorage and when to use it?

### 🧠 Concept

Key-value synchronous storage (~5–10MB). Good for small, non-sensitive preferences. Blocks main thread on large operations. LocalStorage is synchronous, so keep data small.

---

### 💡 Example

```javascript
localStorage.setItem('theme', 'dark');
const theme = localStorage.getItem('theme') || 'light';
```

---

### 🔍 Deep Insights

* **Rule:** Not for secrets (readable by any script on origin).
* **Use Case:** Avoid large writes/reads (blocks).
* **Common Mistake:** Prefer JSON.stringify but handle errors.
* **Pro Tip:** Use for small, non-sensitive user preferences.

---

### ⭐ Senior Takeaway

LocalStorage is synchronous, so keep data small.

---

## 🧩 Q133. Session Storage vs LocalStorage: differences and use cases

### 🧠 Concept

Session Storage persists per-tab until closed; LocalStorage persists across sessions. Both are synchronous and origin-scoped. Choose based on persistence requirements.

---

### 💡 Example

```javascript
sessionStorage.setItem('draft', '...');
```

---

### 🔍 Deep Insights

* **Rule:** Use Session Storage for per-tab state (wizards, multi-tab isolation).
* **Use Case:** Use LocalStorage for stable preferences.
* **Common Mistake:** Both are synchronous and origin-scoped.
* **Pro Tip:** Session Storage is cleared when tab closes, LocalStorage persists.

---

### ⭐ Senior Takeaway

Choose based on persistence requirements.

---

## 🧩 Q134. Cookies: storage usage and security

### 🧠 Concept

Cookies store small pieces of data sent with every HTTP request. Use for session IDs, not bulk data. Use cookies for session management, not large data.

---

### 💡 Example

```http
Set-Cookie: sid=abc123; HttpOnly; Secure; SameSite=Lax; Path=/; Max-Age=1209600
```

---

### 🔍 Deep Insights

* **Rule:** Use HttpOnly + Secure + SameSite to protect against XSS/CSRF.
* **Use Case:** Keep cookies small (<4KB) to avoid bloat on every request.
* **Common Mistake:** Prefer server-managed, rotating session tokens.
* **Pro Tip:** Cookies are automatically sent with every request.

---

### ⭐ Senior Takeaway

Use cookies for session management, not large data.

---

## 🧩 Q135. What is IndexedDB and when to use it?

### 🧠 Concept

IndexedDB is an async, transactional NoSQL DB in the browser, suitable for large, structured data and offline apps. Use for large data that needs persistence and offline access.

---

### 💡 Example

```javascript
import { openDB } from 'idb';

const db = await openDB('app-db', 1, {
  upgrade(db) {
    db.createObjectStore('todos', { keyPath: 'id' });
    db.createObjectStore('users', { keyPath: 'id' });
  }
});

await db.put('todos', { id: 't-1', text: 'Learn IDB' });
const todo = await db.get('todos', 't-1');
```

---

### 🔍 Deep Insights

* **Rule:** Best for offline-first, large datasets, complex queries.
* **Use Case:** Wrap with libraries (idb) for ergonomic API.
* **Common Mistake:** Consider storage quotas and eviction policies.
* **Pro Tip:** IndexedDB supports transactions and indexes for efficient queries.

---

### ⭐ Senior Takeaway

Use for large data that needs persistence and offline access.

---

## 🧩 Q136. LocalStorage vs IndexedDB: compare capabilities

### 🧠 Concept

LocalStorage is simple key-value and sync; IndexedDB is structured and async with indexes and transactions. IndexedDB is async, LocalStorage is sync.

---

### 💡 Example

```javascript
// LocalStorage: quick preference
localStorage.setItem('lang', 'en');

// IndexedDB: cache API results
await db.put('posts', { id: 1, title: 'Hello' });
```

---

### 🔍 Deep Insights

* **Rule:** Choose LocalStorage for tiny preferences/settings, Choose IndexedDB for caches and domain data.
* **Use Case:** Avoid storing secrets in either.
* **Common Mistake:** LocalStorage for <5MB, IndexedDB for larger structured data.
* **Pro Tip:** IndexedDB supports complex queries and transactions.

---

### ⭐ Senior Takeaway

IndexedDB is async, LocalStorage is sync.

---

## 🧩 Q137. What are typical size limits for LocalStorage and IndexedDB?

### 🧠 Concept

LocalStorage: ~5–10MB per origin. IndexedDB: much larger (hundreds of MBs+), browser- and device-dependent, subject to quota and eviction. Storage limits are browser and device dependent.

---

### 💡 Example

```javascript
// Estimating usage (rough)
function approximateSizeKB(obj) {
  return new Blob([JSON.stringify(obj)]).size / 1024;
}
```

---

### 🔍 Deep Insights

* **Rule:** Quotas vary by browser, device, and user settings.
* **Use Case:** IndexedDB may be evicted under storage pressure (persistent storage API helps).
* **Common Mistake:** Request persistent storage with `navigator.storage.persist()` where appropriate.
* **Pro Tip:** Monitor storage usage and handle quota exceeded errors.

---

### ⭐ Senior Takeaway

Storage limits are browser and device dependent.

---

## 🧩 Q138. How do you integrate normalization, HTTP caching, SW caching, API caching, state, and storage into a cohesive architecture?

### 🧠 Concept

Use layered caching with clear boundaries: server cache/CDN → HTTP cache → SW cache → API client cache → normalized app state → local storage/IndexedDB for persistence. Persist only necessary state (e.g., auth, preferences, small caches).

---

### 💡 Example

```javascript
// Layered caching architecture
// 1. CDN/Edge Cache (fastest, shared)
// 2. HTTP Cache (browser, respects headers)
// 3. Service Worker Cache (offline, programmatic)
// 4. API Client Cache (React Query/RTK Query)
// 5. Normalized App State (Redux/Zustand)
// 6. Persistence (LocalStorage/IndexedDB)
```

---

### 🔍 Deep Insights

* **Rule:** Choose the lowest layer that can satisfy data (cheapest, fastest).
* **Use Case:** Normalize at app state; hydrate from API cache/storage on startup.
* **Common Mistake:** Service worker for offline + pre-cache shell and critical assets.
* **Pro Tip:** Use tag-based invalidation to propagate changes upwards.

---

### ⭐ Senior Takeaway

Persist only necessary state (e.g., auth, preferences, small caches).

---
