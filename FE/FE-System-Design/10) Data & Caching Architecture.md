# 10) Data & Caching Architecture (Q121–138)

---

## 121) What is data normalization in frontend apps and why is it important?

Normalization flattens nested API responses into entity maps keyed by IDs, storing relationships by references. It prevents duplication, simplifies updates, and avoids inconsistent UI state.

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

- **Core Benefit**: Eliminates duplication, enabling single-source-of-truth updates
- **Real-World Advantage**: Improves rendering performance (smaller diffs, memoized selectors)
- **Common Practice**: Works well with entity adapters (Redux Toolkit `createEntityAdapter`)
- **Advanced Feature**: Use selectors to re-compose nested shapes for views
- **Interview Tip**: Explain that normalize at the boundary: on fetch or in state adapters

---

## 122) How does normalization improve efficiency and maintainability?

It reduces redundant data, minimizes re-renders, and simplifies updates by changing a single entity rather than multiple locations holding the same data.

```javascript
// Update user name once; reflected across all posts/comments
dispatch(usersSlice.actions.userUpdated({ id: 'user-1', changes: { name: 'Ada Lovelace' } }));
```

- **Core Advantage**: Fewer state writes → fewer component updates
- **Real-World Benefit**: Predictable updates: IDs + references make diffs trivial
- **Common Practice**: Easier cache invalidation: invalidate by entity type/id
- **Advanced Feature**: Single update propagates to all references automatically
- **Interview Tip**: Explain that normalization reduces memory usage and improves performance

---

## 123) Local state vs global state: when to use each?

Local state (component-level) is ideal for UI concerns (inputs, toggles). Global state manages cross-cutting concerns (auth, user profile), shared data (entities), and server cache.

```javascript
// Local state for form input
function SearchBox() {
  const [query, setQuery] = useState('');
  return <input value={query} onChange={e => setQuery(e.target.value)} />;
}

// Global state for current user
const user = useSelector(state => state.auth.user);
```

- **Core Principle**: Prefer local state by default; promote to global only when truly shared
- **Real-World Distinction**: Server cache (React Query/RTK Query) is not the same as app state
- **Common Mistake**: Avoid over-globalizing (causes needless re-renders and coupling)
- **Advanced Strategy**: Use local state for UI, global state for business logic and shared data
- **Interview Tip**: Explain that start with local state, move to global only when needed

---

## 124) Pros and cons of state management libraries (Redux, Vuex, etc.)

Libraries provide structure, tooling (DevTools), and performance patterns (memoization, entity adapters), but add boilerplate and learning curve.

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

- **Core Advantage**: Use RTK/RTK Query to reduce boilerplate, enforce good patterns
- **Real-World Choice**: Choose simpler stores (Zustand, Jotai) for small apps
- **Common Practice**: Keep server cache in a dedicated tool (React Query/RTK Query)
- **Advanced Feature**: DevTools provide time-travel debugging and state inspection
- **Interview Tip**: Explain that choose based on app complexity and team preferences

---

## 125) What is HTTP caching and why does it matter?

HTTP caching stores responses to serve subsequent requests faster. It reduces latency, bandwidth, and server load.

```http
Cache-Control: public, max-age=3600
ETag: "abc123"
Last-Modified: Wed, 21 Oct 2025 07:28:00 GMT
```

- **Core Benefit**: Leverage immutable asset versioning: `/main.8fd2a.js` → `Cache-Control: max-age=31536000, immutable`
- **Real-World Use**: Use `ETag`/`If-None-Match` for validation
- **Common Practice**: Prefer CDN caching for public GET endpoints
- **Advanced Feature**: HTTP caching reduces server load and improves user experience
- **Interview Tip**: Explain that caching is crucial for performance at scale

---

## 126) What do common caching headers do (Cache-Control, ETag, Last-Modified, Expires)?

They control freshness and validation of cached responses.

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

- **Core Strategy**: Prefer `Cache-Control` over `Expires`
- **Real-World Use**: Combine `stale-while-revalidate` for better UX
- **Common Practice**: Use validators to avoid transferring large payloads when unchanged
- **Advanced Feature**: `stale-while-revalidate` serves stale content while fetching fresh data
- **Interview Tip**: Explain that caching headers control browser and CDN behavior

---

## 127) How do you implement API caching strategies (cache-first, network-first, SWR)?

Strategies balance freshness and speed: cache-first (fast), network-first (fresh), stale-while-revalidate (best perceived performance).

```javascript
// Stale-While-Revalidate with React Query
const { data, isFetching } = useQuery(['posts'], fetchPosts, {
  staleTime: 60_000, // 1 minute
  cacheTime: 5 * 60_000, // 5 minutes
});
```

- **Core Strategies**: For public data: cache-first/SWR, For user-specific data: network-first with background refresh
- **Real-World Use**: Tune `staleTime` based on data volatility
- **Common Practice**: Use stale-while-revalidate for best perceived performance
- **Advanced Feature**: Cache-first for static data, network-first for dynamic data
- **Interview Tip**: Explain that choose strategy based on data freshness requirements

---

## 128) Cache invalidation and expiration: how to approach?

Expiration sets time-based freshness; invalidation proactively removes/updates cache when data changes.

```javascript
// React Query invalidation
queryClient.invalidateQueries(['posts']);

// RTK Query
api.util.invalidateTags([{ type: 'Post', id: 'LIST' }]);
```

- **Core Strategy**: Prefer tag-based invalidation to target minimal subsets
- **Real-World Use**: Emit domain events to trigger invalidations after mutations
- **Common Mistake**: Avoid global cache clears (hurts UX)
- **Advanced Feature**: Tag-based invalidation allows fine-grained cache control
- **Interview Tip**: Explain that invalidate only what changed, not everything

---

## 129) What is a service worker and how can it be used for caching?

A Service Worker is a background script that intercepts network requests, enabling offline caching, background sync, and push notifications.

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

- **Core Strategy**: Choose strategy per route (HTML: network-first; assets: cache-first)
- **Real-World Use**: Version and cleanup old caches on `activate`
- **Common Practice**: Use Workbox to manage complex strategies safely
- **Advanced Feature**: Service workers enable offline functionality and background sync
- **Interview Tip**: Explain that service workers run in background, separate from main thread

---

## 130) Service worker caching vs traditional browser caching

Browser caching obeys HTTP headers, SW caching gives app-controlled policies independent of headers and supports offline.

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

- **Core Difference**: SW can cache POST results and custom responses
- **Real-World Consideration**: Beware of stale HTML—use network-first for documents
- **Common Requirement**: Always handle SW updates to avoid stuck old versions
- **Advanced Feature**: Service workers provide programmatic cache control
- **Interview Tip**: Explain that service workers enable offline-first applications

---

## 131) Designing SW caching strategies (precache vs runtime)

Precache static assets at build; runtime-cache dynamic requests with strategy per route.

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

- **Core Strategy**: Documents/network-first; APIs/SWR or network-first; images/cache-first; fonts/cache-first + long TTL
- **Real-World Use**: Use revisioned filenames to enable immutable caching
- **Common Practice**: Precache critical assets at build time
- **Advanced Feature**: Runtime caching handles dynamic requests with appropriate strategies
- **Interview Tip**: Explain that precache for static assets, runtime cache for dynamic content

---

## 132) What is LocalStorage and when to use it?

Key-value synchronous storage (~5–10MB). Good for small, non-sensitive preferences. Blocks main thread on large operations.

```javascript
localStorage.setItem('theme', 'dark');
const theme = localStorage.getItem('theme') || 'light';
```

- **Core Limitation**: Not for secrets (readable by any script on origin)
- **Real-World Use**: Avoid large writes/reads (blocks)
- **Common Practice**: Prefer JSON.stringify but handle errors
- **Advanced Feature**: Use for small, non-sensitive user preferences
- **Interview Tip**: Explain that localStorage is synchronous, so keep data small

---

## 133) Session Storage vs LocalStorage: differences and use cases

Session Storage persists per-tab until closed; LocalStorage persists across sessions. Both are synchronous and origin-scoped.

```javascript
sessionStorage.setItem('draft', '...');
```

- **Core Difference**: Use Session Storage for per-tab state (wizards, multi-tab isolation)
- **Real-World Use**: Use LocalStorage for stable preferences
- **Common Practice**: Both are synchronous and origin-scoped
- **Advanced Feature**: Session Storage is cleared when tab closes, LocalStorage persists
- **Interview Tip**: Explain that choose based on persistence requirements

---

## 134) Cookies: storage usage and security

Cookies store small pieces of data sent with every HTTP request. Use for session IDs, not bulk data.

```http
Set-Cookie: sid=abc123; HttpOnly; Secure; SameSite=Lax; Path=/; Max-Age=1209600
```

- **Core Security**: Use HttpOnly + Secure + SameSite to protect against XSS/CSRF
- **Real-World Limitation**: Keep cookies small (<4KB) to avoid bloat on every request
- **Common Practice**: Prefer server-managed, rotating session tokens
- **Advanced Feature**: Cookies are automatically sent with every request
- **Interview Tip**: Explain that use cookies for session management, not large data

---

## 135) What is IndexedDB and when to use it?

IndexedDB is an async, transactional NoSQL DB in the browser, suitable for large, structured data and offline apps.

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

- **Core Use Case**: Best for offline-first, large datasets, complex queries
- **Real-World Practice**: Wrap with libraries (idb) for ergonomic API
- **Common Consideration**: Consider storage quotas and eviction policies
- **Advanced Feature**: IndexedDB supports transactions and indexes for efficient queries
- **Interview Tip**: Explain that use for large data that needs persistence and offline access

---

## 136) LocalStorage vs IndexedDB: compare capabilities

LocalStorage is simple key-value and sync; IndexedDB is structured and async with indexes and transactions.

```javascript
// LocalStorage: quick preference
localStorage.setItem('lang', 'en');

// IndexedDB: cache API results
await db.put('posts', { id: 1, title: 'Hello' });
```

- **Core Differences**: Choose LocalStorage for tiny preferences/settings, Choose IndexedDB for caches and domain data
- **Real-World Choice**: Avoid storing secrets in either
- **Common Practice**: LocalStorage for <5MB, IndexedDB for larger structured data
- **Advanced Feature**: IndexedDB supports complex queries and transactions
- **Interview Tip**: Explain that IndexedDB is async, LocalStorage is sync

---

## 137) What are typical size limits for LocalStorage and IndexedDB?

LocalStorage: ~5–10MB per origin. IndexedDB: much larger (hundreds of MBs+), browser- and device-dependent, subject to quota and eviction.

```javascript
// Estimating usage (rough)
function approximateSizeKB(obj) {
  return new Blob([JSON.stringify(obj)]).size / 1024;
}
```

- **Core Limitation**: Quotas vary by browser, device, and user settings
- **Real-World Consideration**: IndexedDB may be evicted under storage pressure (persistent storage API helps)
- **Common Practice**: Request persistent storage with `navigator.storage.persist()` where appropriate
- **Advanced Feature**: Monitor storage usage and handle quota exceeded errors
- **Interview Tip**: Explain that storage limits are browser and device dependent

---

## 138) How do you integrate normalization, HTTP caching, SW caching, API caching, state, and storage into a cohesive architecture?

Use layered caching with clear boundaries: server cache/CDN → HTTP cache → SW cache → API client cache → normalized app state → local storage/IndexedDB for persistence.

```javascript
// Layered caching architecture
// 1. CDN/Edge Cache (fastest, shared)
// 2. HTTP Cache (browser, respects headers)
// 3. Service Worker Cache (offline, programmatic)
// 4. API Client Cache (React Query/RTK Query)
// 5. Normalized App State (Redux/Zustand)
// 6. Persistence (LocalStorage/IndexedDB)
```

- **Core Architecture**: Choose the lowest layer that can satisfy data (cheapest, fastest)
- **Real-World Strategy**: Normalize at app state; hydrate from API cache/storage on startup
- **Common Practice**: Service worker for offline + pre-cache shell and critical assets
- **Advanced Feature**: Use tag-based invalidation to propagate changes upwards
- **Interview Tip**: Explain that persist only necessary state (e.g., auth, preferences, small caches)

---
