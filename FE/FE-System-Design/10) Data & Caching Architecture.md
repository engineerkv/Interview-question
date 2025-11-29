<div align="center">

**[← Previous: Real-time Communication Protocols](9%29%20Real-time%20Communication%20Protocols.md)** | **[Next: Security →](11%29%20Security.md)**

</div>

# 10. Data & Caching Architecture (Q118–131)

---

## Q118. Data normalization in frontend apps and why it's important

Normalization flattens nested API responses into entity maps keyed by IDs, storing relationships by references—it prevents duplication, simplifies updates, and avoids inconsistent UI state. Normalize at the boundary: on fetch or in state adapters.

- **Trade-offs**: Eliminates duplication, enabling single-source-of-truth updates—improves rendering performance (smaller diffs, memoized selectors). Works well with entity adapters (Redux Toolkit `createEntityAdapter`)—use selectors to re-compose nested shapes for views.

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

## Q119. Local Storage

LocalStorage is a synchronous key-value storage API (~5–10MB per origin), good for small, non-sensitive preferences and settings. It persists across browser sessions and is origin-scoped.

- **Trade-offs**: Not for secrets (readable by any script on origin)—avoid large writes/reads (blocks main thread). Prefer JSON.stringify but handle errors—use for small, non-sensitive user preferences like theme, language, or UI state. Keep data under 5MB to avoid performance issues.

Example:

```javascript
localStorage.setItem('theme', 'dark');
localStorage.setItem('userPrefs', JSON.stringify({ lang: 'en', notifications: true }));
const theme = localStorage.getItem('theme') || 'light';
const prefs = JSON.parse(localStorage.getItem('userPrefs') || '{}');
```

---

## Q120. Session Storage

Session Storage persists per-tab until the tab is closed; it's synchronous and origin-scoped like LocalStorage but with tab-level isolation. Use it for temporary, tab-specific data.

- **Trade-offs**: Use Session Storage for per-tab state (wizards, multi-tab isolation, draft forms)—use LocalStorage for stable preferences. Both are synchronous and origin-scoped—Session Storage is cleared when tab closes, LocalStorage persists. Perfect for preventing data leakage between tabs.

Example:

```javascript
sessionStorage.setItem('draft', JSON.stringify({ title: '...', content: '...' }));
sessionStorage.setItem('wizardStep', '3');
const draft = JSON.parse(sessionStorage.getItem('draft') || 'null');
```

---

## Q121. Cookie Storage

Cookies store small pieces of data sent with every HTTP request—use for session IDs and authentication tokens, not bulk data. Cookies are automatically sent with requests, making them ideal for server-side session management.

- **Trade-offs**: Use HttpOnly + Secure + SameSite to protect against XSS/CSRF—keep cookies small (<4KB) to avoid bloat on every request. Prefer server-managed, rotating session tokens—cookies are automatically sent with every request, so minimize their size and number.

Example:

```http
Set-Cookie: sid=abc123; HttpOnly; Secure; SameSite=Lax; Path=/; Max-Age=1209600
```

```javascript
// Reading cookies (if not HttpOnly)
document.cookie.split('; ').find(row => row.startsWith('theme='));
```

---

## Q122. IndexedDB

IndexedDB is an async, transactional NoSQL database in the browser, suitable for large, structured data and offline apps. It supports indexes, transactions, and can store hundreds of MBs of data.

- **Trade-offs**: Best for offline-first apps, large datasets, complex queries—wrap with libraries (idb, Dexie.js) for ergonomic API. Consider storage quotas and eviction policies—IndexedDB supports transactions and indexes for efficient queries, but the API is complex without libraries.

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

## Q123. LocalStorage vs Session Storage vs IndexedDB

LocalStorage is simple key-value sync storage (~5–10MB), Session Storage is tab-scoped sync storage, and IndexedDB is async structured storage (hundreds of MBs). Choose based on data size, persistence needs, and access patterns.

- **Trade-offs**: LocalStorage for small preferences (<5MB, sync access)—Session Storage for tab-specific temporary data—IndexedDB for large structured data and offline apps. LocalStorage and Session Storage are synchronous (block main thread), IndexedDB is async—avoid storing secrets in any client-side storage.

Example:

```javascript
// LocalStorage - small, persistent preferences
localStorage.setItem('theme', 'dark');

// Session Storage - tab-specific temporary data
sessionStorage.setItem('draft', '...');

// IndexedDB - large structured data
await db.put('posts', { id: 1, title: 'Hello', content: '...' });
```

---

## Q124. API caching strategies

API caching stores API responses to reduce redundant network requests and improve performance. Use client-side libraries like React Query or RTK Query for intelligent caching with automatic invalidation.

- **Trade-offs**: Strategies balance freshness and speed: cache-first (fast), network-first (fresh), stale-while-revalidate (best perceived performance). For public data: cache-first/SWR, for user-specific data: network-first with background refresh—tune `staleTime` based on data volatility.

Example:

```javascript
const { data, isFetching } = useQuery(['posts'], fetchPosts, {
  staleTime: 60_000, // Consider fresh for 1 minute
  cacheTime: 5 * 60_000, // Keep in cache for 5 minutes
  refetchOnWindowFocus: true
});
```

---

## Q125. State management in frontend applications

Local state (component-level) is ideal for UI concerns (inputs, toggles)—global state manages cross-cutting concerns (auth, user profile), shared data (entities), and server cache. Start with local state, move to global only when needed.

- **Trade-offs**: Prefer local state by default; promote to global only when truly shared—server cache (React Query/RTK Query) is not the same as app state. Avoid over-globalizing (causes needless re-renders and coupling)—use local state for UI, global state for business logic and shared data.

Example:

```javascript
// Local state for UI
function SearchBox() {
  const [query, setQuery] = useState('');
  return <input value={query} onChange={e => setQuery(e.target.value)} />;
}

// Global state for shared data
const user = useSelector(state => state.auth.user);
const posts = useSelector(state => state.posts.entities);
```

---

## Q126. Handling cache invalidation

Cache invalidation proactively removes or updates cache when data changes—invalidate only what changed, not everything. Use tag-based invalidation to target minimal subsets.

- **Trade-offs**: Prefer tag-based invalidation to target minimal subsets—emit domain events to trigger invalidations after mutations. Avoid global cache clears (hurts UX)—tag-based invalidation allows fine-grained cache control and better performance.

Example:

```javascript
// React Query - invalidate by query key
queryClient.invalidateQueries(['posts']);

// RTK Query - invalidate by tags
api.util.invalidateTags([{ type: 'Post', id: 'LIST' }]);

// After mutation
mutatePost({ id: 1, title: 'Updated' });
queryClient.invalidateQueries(['post', 1]);
```

---

## Q127. Implementing caching layers in frontend applications

Use layered caching with clear boundaries: server cache/CDN → HTTP cache → SW cache → API client cache → normalized app state → local storage/IndexedDB for persistence. Persist only necessary state (e.g., auth, preferences, small caches).

- **Trade-offs**: Choose the lowest layer that can satisfy data (cheapest, fastest)—normalize at app state; hydrate from API cache/storage on startup. Service worker for offline + pre-cache shell and critical assets—use tag-based invalidation to propagate changes upwards through layers.

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

## Q128. Best practices for data caching

Cache strategies should balance freshness, performance, and user experience—choose the right strategy per data type and use case. Monitor cache hit rates and adjust strategies based on actual usage patterns.

- **Trade-offs**: For static assets: cache-first with long TTL—for dynamic data: network-first or stale-while-revalidate. Use versioning for immutable assets—implement proper cache invalidation to prevent stale data. Always have a fallback strategy when cache fails.

Example:

```javascript
// Cache-first for static assets
workbox.strategies.CacheFirst({ cacheName: 'static-assets' });

// Stale-while-revalidate for dynamic content
workbox.strategies.StaleWhileRevalidate({ cacheName: 'api-cache' });

// Network-first for critical data
workbox.strategies.NetworkFirst({ cacheName: 'critical-data' });
```

---

## Q129. Optimizing data fetching and caching strategies

Optimize data fetching by reducing redundant requests, implementing proper caching, and using techniques like request deduplication and prefetching. Combine multiple strategies for optimal performance.

- **Trade-offs**: Request deduplication prevents duplicate simultaneous requests—prefetching improves perceived performance but uses bandwidth. Use pagination and infinite scroll for large datasets—implement proper loading states and error handling. Balance between freshness and performance based on data volatility.

Example:

```javascript
// Request deduplication (React Query does this automatically)
const { data } = useQuery(['user', userId], fetchUser); // Multiple components can use same query

// Prefetching
queryClient.prefetchQuery(['posts'], fetchPosts);

// Pagination
const { data, fetchNextPage } = useInfiniteQuery(['posts'], fetchPosts, {
  getNextPageParam: (lastPage) => lastPage.nextCursor
});
```

---

## Q130. Storage quotas and eviction policies

Browser storage has quotas that vary by browser, device, and user settings—IndexedDB may be evicted under storage pressure. Request persistent storage where appropriate and monitor usage.

- **Trade-offs**: Quotas vary by browser, device, and user settings—IndexedDB may be evicted under storage pressure (persistent storage API helps). Request persistent storage with `navigator.storage.persist()` where appropriate—monitor storage usage and handle quota exceeded errors gracefully.

Example:

```javascript
// Check storage quota
const estimate = await navigator.storage.estimate();
console.log(`Quota: ${estimate.quota}, Usage: ${estimate.usage}`);

// Request persistent storage
const isPersistent = await navigator.storage.persist();
console.log(`Persistent: ${isPersistent}`);

// Handle quota exceeded
try {
  await db.put('data', largeObject);
} catch (error) {
  if (error.name === 'QuotaExceededError') {
    // Handle quota exceeded
  }
}
```

---

## Q131. Integrating normalization, HTTP caching, SW caching, API caching, state, and storage into a cohesive architecture

Integrate all caching layers with clear boundaries and data flow—normalize at app state, hydrate from storage on startup, and use tag-based invalidation to propagate changes. Design a cohesive architecture that leverages each layer's strengths.

- **Trade-offs**: Each layer serves a specific purpose—CDN for global distribution, HTTP cache for browser-level caching, SW for offline, API cache for request deduplication, normalized state for UI, and storage for persistence. The catch is managing invalidation across layers—use event-driven invalidation and clear data flow patterns.

Example:

```javascript
// Complete caching architecture
// 1. CDN/Edge Cache → Static assets, public API responses
// 2. HTTP Cache → Browser-level, respects Cache-Control headers
// 3. Service Worker → Offline support, programmatic caching
// 4. API Client Cache → React Query/RTK Query, request deduplication
// 5. Normalized State → Redux/Zustand, single source of truth
// 6. Persistence → LocalStorage/IndexedDB, survive page reloads

// Data flow: CDN → HTTP → SW → API Cache → State → Storage
// Invalidation: Storage → State → API Cache → SW → HTTP → CDN
```

---

