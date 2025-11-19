# 10. Data & Caching Architecture (Q121–138)

---

## Q121. What is data normalization in frontend apps and why is it important?

Normalization flattens nested API responses into entity maps keyed by IDs, storing relationships by references - it prevents duplication, simplifies updates, and avoids inconsistent UI state. Normalize at the boundary: on fetch or in state adapters.

- **Trade-offs**: Eliminates duplication, enabling single-source-of-truth updates - improves rendering performance (smaller diffs, memoized selectors). Works well with entity adapters (Redux Toolkit `createEntityAdapter`) - use selectors to re-compose nested shapes for views.

Example:

```javascript
const response = {
  id: 'post-1',
  title: 'Hello',
  author: { id: 'user-1', name: 'Ada' },
  comments: [
    { id: 'c-1', text: 'Nice', author: { id: 'user-2', name: 'Lin' }},
    { id: 'c-2', text: 'Wow', author: { id: 'user-1', name: 'Ada' }}
  ]
};
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

## Q122. How does normalization improve efficiency and maintainability?

It reduces redundant data, minimizes re-renders, and simplifies updates by changing a single entity rather than multiple locations holding the same data. Normalization reduces memory usage and improves performance.

- **Trade-offs**: Fewer state writes → fewer component updates - predictable updates: IDs + references make diffs trivial. Easier cache invalidation: invalidate by entity type/id - single update propagates to all references automatically.

Example:

```javascript
dispatch(usersSlice.actions.userUpdated({ id: 'user-1', changes: { name: 'Ada Lovelace' } }));
```

---

## Q123. Local state vs global state: when to use each?

Local state (component-level) is ideal for UI concerns (inputs, toggles) - global state manages cross-cutting concerns (auth, user profile), shared data (entities), and server cache. Start with local state, move to global only when needed.

- **Trade-offs**: Prefer local state by default; promote to global only when truly shared - server cache (React Query/RTK Query) is not the same as app state. Avoid over-globalizing (causes needless re-renders and coupling) - use local state for UI, global state for business logic and shared data.

Example:

```javascript
function SearchBox() {
  const [query, setQuery] = useState('');
  return <input value={query} onChange={e => setQuery(e.target.value)} />;
}
const user = useSelector(state => state.auth.user);
```

---

## Q124. Pros and cons of state management libraries (Redux, Vuex, etc.)

Libraries provide structure, tooling (DevTools), and performance patterns (memoization, entity adapters), but add boilerplate and learning curve. Choose based on app complexity and team preferences.

- **Trade-offs**: Use RTK/RTK Query to reduce boilerplate, enforce good patterns - choose simpler stores (Zustand, Jotai) for small apps. Keep server cache in a dedicated tool (React Query/RTK Query) - DevTools provide time-travel debugging and state inspection.

Example:

```javascript
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

## Q125. What is HTTP caching and why does it matter?

HTTP caching stores responses to serve subsequent requests faster - it reduces latency, bandwidth, and server load. Caching is crucial for performance at scale.

- **Trade-offs**: Leverage immutable asset versioning: `/main.8fd2a.js` → `Cache-Control: max-age=31536000, immutable` - use `ETag`/`If-None-Match` for validation. Prefer CDN caching for public GET endpoints - HTTP caching reduces server load and improves user experience.

Example:

```http
Cache-Control: public, max-age=3600
ETag: "abc123"
Last-Modified: Wed, 21 Oct 2025 07:28:00 GMT
```

---

## Q126. What do common caching headers do?

They control freshness and validation of cached responses - caching headers control browser and CDN behavior.

- **Trade-offs**: Prefer `Cache-Control` over `Expires` - combine `stale-while-revalidate` for better UX. Use validators to avoid transferring large payloads when unchanged - `stale-while-revalidate` serves stale content while fetching fresh data.

Example:

```http
Cache-Control: max-age=600, stale-while-revalidate=60
ETag: "v1"
If-None-Match: "v1"
Last-Modified: Wed, 21 Oct 2025 07:28:00 GMT
If-Modified-Since: Wed, 21 Oct 2025 07:28:00 GMT
```

---

## Q127. How do you implement API caching strategies?

Strategies balance freshness and speed: cache-first (fast), network-first (fresh), stale-while-revalidate (best perceived performance). Choose strategy based on data freshness requirements.

- **Trade-offs**: For public data: cache-first/SWR, for user-specific data: network-first with background refresh - tune `staleTime` based on data volatility. Use stale-while-revalidate for best perceived performance - cache-first for static data, network-first for dynamic data.

Example:

```javascript
const { data, isFetching } = useQuery(['posts'], fetchPosts, {
  staleTime: 60_000,
  cacheTime: 5 * 60_000,
});
```

---

## Q128. Cache invalidation and expiration: how to approach?

Expiration sets time-based freshness; invalidation proactively removes/updates cache when data changes. Invalidate only what changed, not everything.

- **Trade-offs**: Prefer tag-based invalidation to target minimal subsets - emit domain events to trigger invalidations after mutations. Avoid global cache clears (hurts UX) - tag-based invalidation allows fine-grained cache control.

Example:

```javascript
queryClient.invalidateQueries(['posts']);
api.util.invalidateTags([{ type: 'Post', id: 'LIST' }]);
```

---

## Q129. What is a service worker and how can it be used for caching?

A Service Worker is a background script that intercepts network requests, enabling offline caching, background sync, and push notifications. Service workers run in background, separate from main thread.

- **Trade-offs**: Choose strategy per route (HTML: network-first; assets: cache-first) - version and cleanup old caches on `activate`. Use Workbox to manage complex strategies safely - service workers enable offline functionality and background sync.

Example:

```javascript
self.addEventListener('install', (event) => {
  event.waitUntil(
    caches.open('app-v1').then((cache) => cache.addAll([
      '/', '/index.html', '/styles.css', '/main.js'
    ]))
  );
});
self.addEventListener('fetch', (event) => {
  event.respondWith(
    caches.match(event.request).then((cached) => cached || fetch(event.request))
  );
});
```

---

## Q130. Service worker caching vs traditional browser caching

Browser caching obeys HTTP headers, SW caching gives app-controlled policies independent of headers and supports offline. Service workers enable offline-first applications.

- **Trade-offs**: SW can cache POST results and custom responses - beware of stale HTML, use network-first for documents. Always handle SW updates to avoid stuck old versions - service workers provide programmatic cache control.

Example:

```javascript
workbox.routing.registerRoute(
  ({ request }) => request.destination === 'document',
  new workbox.strategies.NetworkFirst({
    cacheName: 'pages',
    plugins: [new workbox.expiration.ExpirationPlugin({ maxEntries: 50 })]
  })
);
```

---

## Q131. Designing SW caching strategies (precache vs runtime)

Precache static assets at build; runtime-cache dynamic requests with strategy per route. Precache for static assets, runtime cache for dynamic content.

- **Trade-offs**: Documents/network-first; APIs/SWR or network-first; images/cache-first; fonts/cache-first + long TTL - use revisioned filenames to enable immutable caching. Precache critical assets at build time - runtime caching handles dynamic requests with appropriate strategies.

Example:

```javascript
workbox.precaching.precacheAndRoute(self.__WB_MANIFEST);
workbox.routing.registerRoute(
  ({ request }) => request.destination === 'image',
  new workbox.strategies.CacheFirst({
    cacheName: 'images',
    plugins: [new workbox.expiration.ExpirationPlugin({ maxEntries: 200, maxAgeSeconds: 7*24*3600 })]
  })
);
```

---

## Q132. What is LocalStorage and when to use it?

Key-value synchronous storage (~5–10MB), good for small, non-sensitive preferences - blocks main thread on large operations. LocalStorage is synchronous, so keep data small.

- **Trade-offs**: Not for secrets (readable by any script on origin) - avoid large writes/reads (blocks). Prefer JSON.stringify but handle errors - use for small, non-sensitive user preferences.

Example:

```javascript
localStorage.setItem('theme', 'dark');
const theme = localStorage.getItem('theme') || 'light';
```

---

## Q133. Session Storage vs LocalStorage: differences and use cases

Session Storage persists per-tab until closed; LocalStorage persists across sessions - both are synchronous and origin-scoped. Choose based on persistence requirements.

- **Trade-offs**: Use Session Storage for per-tab state (wizards, multi-tab isolation) - use LocalStorage for stable preferences. Both are synchronous and origin-scoped - Session Storage is cleared when tab closes, LocalStorage persists.

Example:

```javascript
sessionStorage.setItem('draft', '...');
```

---

## Q134. Cookies: storage usage and security

Cookies store small pieces of data sent with every HTTP request - use for session IDs, not bulk data. Use cookies for session management, not large data.

- **Trade-offs**: Use HttpOnly + Secure + SameSite to protect against XSS/CSRF - keep cookies small (<4KB) to avoid bloat on every request. Prefer server-managed, rotating session tokens - cookies are automatically sent with every request.

Example:

```http
Set-Cookie: sid=abc123; HttpOnly; Secure; SameSite=Lax; Path=/; Max-Age=1209600
```

---

## Q135. What is IndexedDB and when to use it?

IndexedDB is an async, transactional NoSQL DB in the browser, suitable for large, structured data and offline apps. Use for large data that needs persistence and offline access.

- **Trade-offs**: Best for offline-first, large datasets, complex queries - wrap with libraries (idb) for ergonomic API. Consider storage quotas and eviction policies - IndexedDB supports transactions and indexes for efficient queries.

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

---

## Q136. LocalStorage vs IndexedDB: compare capabilities

LocalStorage is simple key-value and sync; IndexedDB is structured and async with indexes and transactions. IndexedDB is async, LocalStorage is sync.

- **Trade-offs**: Choose LocalStorage for tiny preferences/settings, choose IndexedDB for caches and domain data - avoid storing secrets in either. LocalStorage for <5MB, IndexedDB for larger structured data - IndexedDB supports complex queries and transactions.

Example:

```javascript
localStorage.setItem('lang', 'en');
await db.put('posts', { id: 1, title: 'Hello' });
```

---

## Q137. What are typical size limits for LocalStorage and IndexedDB?

LocalStorage: ~5–10MB per origin. IndexedDB: much larger (hundreds of MBs+), browser- and device-dependent, subject to quota and eviction. Storage limits are browser and device dependent.

- **Trade-offs**: Quotas vary by browser, device, and user settings - IndexedDB may be evicted under storage pressure (persistent storage API helps). Request persistent storage with `navigator.storage.persist()` where appropriate - monitor storage usage and handle quota exceeded errors.

Example:

```javascript
function approximateSizeKB(obj) {
  return new Blob([JSON.stringify(obj)]).size / 1024;
}
```

---

## Q138. How do you integrate normalization, HTTP caching, SW caching, API caching, state, and storage into a cohesive architecture?

Use layered caching with clear boundaries: server cache/CDN → HTTP cache → SW cache → API client cache → normalized app state → local storage/IndexedDB for persistence. Persist only necessary state (e.g., auth, preferences, small caches).

- **Trade-offs**: Choose the lowest layer that can satisfy data (cheapest, fastest) - normalize at app state; hydrate from API cache/storage on startup. Service worker for offline + pre-cache shell and critical assets - use tag-based invalidation to propagate changes upwards.

Example:

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
