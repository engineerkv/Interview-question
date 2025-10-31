# 10) Data & Caching Architecture (Q121–138)

---

## 121) What is data normalization in frontend apps and why is it important?

Concept:
Normalization flattens nested API responses into entity maps keyed by IDs, storing relationships by references. It prevents duplication, simplifies updates, and avoids inconsistent UI state.

Example:
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

Deep Insight:
- Eliminates duplication, enabling single-source-of-truth updates
- Improves rendering performance (smaller diffs, memoized selectors)
- Works well with entity adapters (Redux Toolkit `createEntityAdapter`)
- Use selectors to re-compose nested shapes for views
- Normalize at the boundary: on fetch or in state adapters

---

## 122) How does normalization improve efficiency and maintainability?

Concept:
It reduces redundant data, minimizes re-renders, and simplifies updates by changing a single entity rather than multiple locations holding the same data.

Example:
```javascript
// Update user name once; reflected across all posts/comments
dispatch(usersSlice.actions.userUpdated({ id: 'user-1', changes: { name: 'Ada Lovelace' } }));
```

Deep Insight:
- Fewer state writes → fewer component updates
- Predictable updates: IDs + references make diffs trivial
- Easier cache invalidation: invalidate by entity type/id

---

## 123) Local state vs global state: when to use each?

Concept:
Local state (component-level) is ideal for UI concerns (inputs, toggles). Global state manages cross-cutting concerns (auth, user profile), shared data (entities), and server cache.

Example:
```javascript
// Local state for form input
function SearchBox() {
  const [query, setQuery] = useState('');
  return <input value={query} onChange={e => setQuery(e.target.value)} />;
}

// Global state for current user
const user = useSelector(state => state.auth.user);
```

Deep Insight:
- Prefer local state by default; promote to global only when truly shared
- Server cache (React Query/RTK Query) is not the same as app state
- Avoid over-globalizing (causes needless re-renders and coupling)

---

## 124) Pros and cons of state management libraries (Redux, Vuex, etc.)

Concept:
Libraries provide structure, tooling (DevTools), and performance patterns (memoization, entity adapters), but add boilerplate and learning curve.

Example:
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

Deep Insight:
- Use RTK/RTK Query to reduce boilerplate, enforce good patterns
- Choose simpler stores (Zustand, Jotai) for small apps
- Keep server cache in a dedicated tool (React Query/RTK Query)

---

## 125) What is HTTP caching and why does it matter?

Concept:
HTTP caching stores responses to serve subsequent requests faster. It reduces latency, bandwidth, and server load.

Example:
```http
Cache-Control: public, max-age=3600
ETag: "abc123"
Last-Modified: Wed, 21 Oct 2025 07:28:00 GMT
```

Deep Insight:
- Leverage immutable asset versioning: `/main.8fd2a.js` → `Cache-Control: max-age=31536000, immutable`
- Use `ETag`/`If-None-Match` for validation
- Prefer CDN caching for public GET endpoints

---

## 126) What do common caching headers do (Cache-Control, ETag, Last-Modified, Expires)?

Concept:
They control freshness and validation of cached responses.

Example:
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

Deep Insight:
- Prefer `Cache-Control` over `Expires`
- Combine `stale-while-revalidate` for better UX
- Use validators to avoid transferring large payloads when unchanged

---

## 127) How do you implement API caching strategies (cache-first, network-first, SWR)?

Concept:
Strategies balance freshness and speed: cache-first (fast), network-first (fresh), stale-while-revalidate (best perceived performance).

Example:
```javascript
// Stale-While-Revalidate with React Query
const { data, isFetching } = useQuery(['posts'], fetchPosts, {
  staleTime: 60_000, // 1 minute
  cacheTime: 5 * 60_000, // 5 minutes
});
```

Deep Insight:
- For public data: cache-first/SWR
- For user-specific data: network-first with background refresh
- Tune `staleTime` based on data volatility

---

## 128) Cache invalidation and expiration: how to approach?

Concept:
Expiration sets time-based freshness; invalidation proactively removes/updates cache when data changes.

Example:
```javascript
// React Query invalidation
queryClient.invalidateQueries(['posts']);

// RTK Query
api.util.invalidateTags([{ type: 'Post', id: 'LIST' }]);
```

Deep Insight:
- Prefer tag-based invalidation to target minimal subsets
- Emit domain events to trigger invalidations after mutations
- Avoid global cache clears (hurts UX)

---

## 129) What is a service worker and how can it be used for caching?

Concept:
A Service Worker is a background script that intercepts network requests, enabling offline caching, background sync, and push notifications.

Example:
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

Deep Insight:
- Choose strategy per route (HTML: network-first; assets: cache-first)
- Version and cleanup old caches on `activate`
- Use Workbox to manage complex strategies safely

---

## 130) Service worker caching vs traditional browser caching

Concept:
Browser caching obeys HTTP headers, SW caching gives app-controlled policies independent of headers and supports offline.

Example:
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

Deep Insight:
- SW can cache POST results and custom responses
- Beware of stale HTML—use network-first for documents
- Always handle SW updates to avoid stuck old versions

---

## 131) Designing SW caching strategies (precache vs runtime)

Concept:
Precache static assets at build; runtime-cache dynamic requests with strategy per route.

Example:
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

Deep Insight:
- Documents/network-first; APIs/SWR or network-first; images/cache-first; fonts/cache-first + long TTL
- Use revisioned filenames to enable immutable caching

---

## 132) What is LocalStorage and when to use it?

Concept:
Key-value synchronous storage (~5–10MB). Good for small, non-sensitive preferences. Blocks main thread on large operations.

Example:
```javascript
localStorage.setItem('theme', 'dark');
const theme = localStorage.getItem('theme') || 'light';
```

Deep Insight:
- Not for secrets (readable by any script on origin)
- Avoid large writes/reads (blocks)
- Prefer JSON.stringify but handle errors

---

## 133) Session Storage vs LocalStorage: differences and use cases

Concept:
Session Storage persists per-tab until closed; LocalStorage persists across sessions. Both are synchronous and origin-scoped.

Example:
```javascript
sessionStorage.setItem('draft', '...');
```

Deep Insight:
- Use Session Storage for per-tab state (wizards, multi-tab isolation)
- Use LocalStorage for stable preferences

---

## 134) Cookies: storage usage and security

Concept:
Cookies store small pieces of data sent with every HTTP request. Use for session IDs, not bulk data.

Example:
```http
Set-Cookie: sid=abc123; HttpOnly; Secure; SameSite=Lax; Path=/; Max-Age=1209600
```

Deep Insight:
- Use HttpOnly + Secure + SameSite to protect against XSS/CSRF
- Keep cookies small (<4KB) to avoid bloat on every request
- Prefer server-managed, rotating session tokens

---

## 135) What is IndexedDB and when to use it?

Concept:
IndexedDB is an async, transactional NoSQL DB in the browser, suitable for large, structured data and offline apps.

Example:
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

Deep Insight:
- Best for offline-first, large datasets, complex queries
- Wrap with libraries (idb) for ergonomic API
- Consider storage quotas and eviction policies

---

## 136) LocalStorage vs IndexedDB: compare capabilities

Concept:
LocalStorage is simple key-value and sync; IndexedDB is structured and async with indexes and transactions.

Example:
```javascript
// LocalStorage: quick preference
localStorage.setItem('lang', 'en');

// IndexedDB: cache API results
await db.put('posts', { id: 1, title: 'Hello' });
```

Deep Insight:
- Choose LocalStorage for tiny preferences/settings
- Choose IndexedDB for caches and domain data
- Avoid storing secrets in either

---

## 137) What are typical size limits for LocalStorage and IndexedDB?

Concept:
LocalStorage: ~5–10MB per origin. IndexedDB: much larger (hundreds of MBs+), browser- and device-dependent, subject to quota and eviction.

Example:
```javascript
// Estimating usage (rough)
function approximateSizeKB(obj) {
  return new Blob([JSON.stringify(obj)]).size / 1024;
}
```

Deep Insight:
- Quotas vary by browser, device, and user settings
- IndexedDB may be evicted under storage pressure (persistent storage API helps)
- Request persistent storage with `navigator.storage.persist()` where appropriate

---

## 138) How do you integrate normalization, HTTP caching, SW caching, API caching, state, and storage into a cohesive architecture?

Concept:
Use layered caching with clear boundaries: server cache/CDN → HTTP cache → SW cache → API client cache → normalized app state → local storage/IndexedDB for persistence.

Example:
```mermaid
graph TD;
  A[CDN/Edge Cache] --> B[HTTP Cache (Browser)];
  B --> C[Service Worker Cache];
  C --> D[API Client Cache (React Query/RTK Query)];
  D --> E[Normalized App State (Redux/Zustand)];
  E --> F[Persistence (LocalStorage/IndexedDB)];
```

Deep Insight:
- Choose the lowest layer that can satisfy data (cheapest, fastest)
- Normalize at app state; hydrate from API cache/storage on startup
- Service worker for offline + pre-cache shell and critical assets
- Use tag-based invalidation to propagate changes upwards
- Persist only necessary state (e.g., auth, preferences, small caches)
- Monitor cache hit rates and stale times; iterate based on RUM data
