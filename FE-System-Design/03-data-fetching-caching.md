# 🏗️ Frontend System Design Interview Notes (2025 Edition)

## 🧠 Section 3 — Data Fetching, Caching & APIs — Q41-Q60

---

### 41. 🧠 How do REST and GraphQL differ in frontend system design?

**🧠 Concept**

REST uses multiple endpoints for different resources, while GraphQL provides a single endpoint with flexible querying capabilities.

**💻 Example**

```javascript
// REST API
GET /api/users/1
GET /api/users/1/posts
GET /api/users/1/posts/1/comments

// GraphQL API
query {
  user(id: 1) {
    name
    posts {
      title
      comments {
        content
      }
    }
  }
}
```

**💬 Explanation + Insight**

- **REST** - Multiple endpoints, over-fetching/under-fetching
- **GraphQL** - Single endpoint, precise data fetching
- **Flexibility** - GraphQL more flexible for complex queries
- **Caching** - REST easier to cache, GraphQL more complex
- **Use Cases** - REST for simple APIs, GraphQL for complex data

---

### 42. 🧠 What are the pros and cons of GraphQL in large-scale applications?

**🧠 Concept**

GraphQL provides flexible querying and type safety but can be complex to implement and cache effectively.

**💻 Example**

```javascript
// GraphQL pros and cons
Pros:
- Flexible querying
- Type safety
- Single endpoint
- Real-time subscriptions
- Introspection

Cons:
- Complex caching
- N+1 query problems
- Learning curve
- Over-engineering for simple cases
- Security considerations
```

**💬 Explanation + Insight**

- **Flexibility** - Query exactly what you need
- **Type Safety** - Strong typing and validation
- **Caching** - Complex caching strategies needed
- **Performance** - Can lead to N+1 query problems
- **Use Cases** - Complex data relationships, real-time apps

---

### 43. 🧠 What is gRPC, and is it suitable for frontend communication?

**🧠 Concept**

gRPC is a high-performance RPC framework using HTTP/2 and Protocol Buffers, but requires additional tooling for frontend integration.

**💻 Example**

```javascript
// gRPC for frontend
// Requires gRPC-Web or gRPC-Gateway
const client = new UserServiceClient('https://api.example.com');

const request = new GetUserRequest();
request.setId(1);

client.getUser(request, {}, (err, response) => {
  if (err) {
    console.error(err);
  } else {
    console.log(response.getUser());
  }
});
```

**💬 Explanation + Insight**

- **Performance** - High-performance binary protocol
- **Type Safety** - Strong typing with Protocol Buffers
- **Frontend Integration** - Requires gRPC-Web or gateway
- **HTTP/2** - Leverages HTTP/2 multiplexing
- **Use Cases** - Microservices, high-performance APIs

---

### 44. 🧠 How do you design caching for REST and GraphQL APIs?

**🧠 Concept**

REST caching uses HTTP cache headers and CDN caching, while GraphQL requires application-level caching strategies.

**💻 Example**

```javascript
// REST caching
// HTTP headers
Cache-Control: max-age=3600
ETag: "abc123"
Last-Modified: Wed, 21 Oct 2015 07:28:00 GMT

// GraphQL caching
const cache = new InMemoryCache({
  typePolicies: {
    User: {
      fields: {
        posts: {
          merge(existing, incoming) {
            return [...existing, ...incoming];
          }
        }
      }
    }
  }
});
```

**💬 Explanation + Insight**

- **REST Caching** - HTTP cache headers, CDN caching
- **GraphQL Caching** - Application-level caching
- **Cache Invalidation** - REST easier, GraphQL complex
- **Performance** - Both improve performance significantly
- **Strategies** - Different approaches for different APIs

---

### 45. 🧠 What is stale-while-revalidate (SWR), and when should you use it?

**🧠 Concept**

SWR serves stale data immediately while fetching fresh data in the background, providing fast user experience with up-to-date data.

**💻 Example**

```javascript
// SWR implementation
import useSWR from 'swr';

function Profile() {
  const { data, error } = useSWR('/api/user', fetcher, {
    revalidateOnFocus: true,
    revalidateOnReconnect: true,
    dedupingInterval: 2000
  });

  if (error) return <div>Failed to load</div>;
  if (!data) return <div>Loading...</div>;
  
  return <div>Hello {data.name}!</div>;
}
```

**💬 Explanation + Insight**

- **Fast Response** - Serve stale data immediately
- **Background Updates** - Fetch fresh data in background
- **User Experience** - Fast perceived performance
- **Data Freshness** - Balance between speed and freshness
- **Use Cases** - Real-time data, user profiles, dashboards

---

### 46. 🧠 What are cache invalidation strategies (time-based, tag-based)?

**🧠 Concept**

Cache invalidation removes stale data using time-based expiration or tag-based invalidation for more precise control.

**💻 Example**

```javascript
// Time-based invalidation
const cache = new Map();
const TTL = 5 * 60 * 1000; // 5 minutes

function getCachedData(key) {
  const item = cache.get(key);
  if (item && Date.now() - item.timestamp < TTL) {
    return item.data;
  }
  return null;
}

// Tag-based invalidation
const tags = new Map();
function invalidateByTag(tag) {
  const keys = tags.get(tag) || [];
  keys.forEach(key => cache.delete(key));
}
```

**💬 Explanation + Insight**

- **Time-based** - Simple expiration-based invalidation
- **Tag-based** - Precise invalidation by content tags
- **Performance** - Balance between cache hit rate and freshness
- **Complexity** - Tag-based more complex but more precise
- **Use Cases** - Time-based for simple cases, tag-based for complex

---

### 47. 🧠 How do you handle optimistic updates in data fetching?

**🧠 Concept**

Optimistic updates immediately update the UI before server confirmation, providing instant feedback while handling potential failures.

**💻 Example**

```javascript
// Optimistic update
const [todos, setTodos] = useState([]);

const addTodo = async (text) => {
  const tempId = Date.now();
  const newTodo = { id: tempId, text, completed: false };
  
  // Optimistic update
  setTodos(prev => [...prev, newTodo]);
  
  try {
    const response = await fetch('/api/todos', {
      method: 'POST',
      body: JSON.stringify({ text })
    });
    const savedTodo = await response.json();
    
    // Replace with server response
    setTodos(prev => prev.map(todo => 
      todo.id === tempId ? savedTodo : todo
    ));
  } catch (error) {
    // Rollback on error
    setTodos(prev => prev.filter(todo => todo.id !== tempId));
  }
};
```

**💬 Explanation + Insight**

- **Immediate Feedback** - Update UI before server response
- **Error Handling** - Rollback on failure
- **User Experience** - Perceived performance improvement
- **Complexity** - Requires careful state management
- **Use Cases** - Forms, real-time updates, user interactions

---

### 48. 🧠 How does React Query or SWR improve API caching?

**🧠 Concept**

React Query and SWR provide intelligent caching, background updates, and synchronization for better API data management.

**💻 Example**

```javascript
// React Query
import { useQuery, useMutation, useQueryClient } from 'react-query';

function Users() {
  const queryClient = useQueryClient();
  
  const { data, isLoading } = useQuery('users', fetchUsers, {
    staleTime: 5 * 60 * 1000, // 5 minutes
    cacheTime: 10 * 60 * 1000, // 10 minutes
  });
  
  const mutation = useMutation(createUser, {
    onSuccess: () => {
      queryClient.invalidateQueries('users');
    }
  });
  
  return <div>{/* Render users */}</div>;
}
```

**💬 Explanation + Insight**

- **Intelligent Caching** - Automatic cache management
- **Background Updates** - Keep data fresh automatically
- **Synchronization** - Sync data across components
- **Performance** - Reduce unnecessary API calls
- **Developer Experience** - Simplified data fetching

---

### 49. 🧠 What are edge caches, and how do they differ from browser caches?

**🧠 Concept**

Edge caches are distributed CDN caches closer to users, while browser caches are local to each user's device.

**💻 Example**

```javascript
// Edge cache configuration
// CDN edge locations
- US East: cache.example.com
- EU West: cache-eu.example.com
- Asia Pacific: cache-ap.example.com

// Browser cache
// Local to user's device
- Memory cache
- Disk cache
- Service worker cache
```

**💬 Explanation + Insight**

- **Edge Caches** - Distributed, shared across users
- **Browser Caches** - Local, user-specific
- **Performance** - Edge caches reduce latency globally
- **Storage** - Different storage characteristics
- **Use Cases** - Edge for global content, browser for personal data

---

### 50. 🧠 How do you handle API retries, rate limiting, and backoff?

**🧠 Concept**

API error handling includes retry logic with exponential backoff, rate limiting compliance, and graceful degradation.

**💻 Example**

```javascript
// Retry with exponential backoff
async function fetchWithRetry(url, options = {}, maxRetries = 3) {
  for (let i = 0; i < maxRetries; i++) {
    try {
      const response = await fetch(url, options);
      if (response.ok) return response;
      
      if (response.status === 429) { // Rate limited
        const retryAfter = response.headers.get('Retry-After');
        await delay(parseInt(retryAfter) * 1000);
        continue;
      }
      
      throw new Error(`HTTP ${response.status}`);
    } catch (error) {
      if (i === maxRetries - 1) throw error;
      await delay(Math.pow(2, i) * 1000); // Exponential backoff
    }
  }
}
```

**💬 Explanation + Insight**

- **Retry Logic** - Handle temporary failures
- **Exponential Backoff** - Avoid overwhelming servers
- **Rate Limiting** - Respect API rate limits
- **Error Handling** - Graceful degradation
- **Use Cases** - Unreliable networks, rate-limited APIs

---

### 51. 🧠 What is ETag, and how does conditional caching work?

**🧠 Concept**

ETag provides conditional caching by comparing resource versions, enabling efficient cache validation and updates.

**💻 Example**

```javascript
// ETag conditional request
// First request
GET /api/data
Response: ETag: "abc123"

// Subsequent request
GET /api/data
If-None-Match: "abc123"

// If unchanged, server returns 304 Not Modified
// If changed, server returns new data with new ETag
```

**💬 Explanation + Insight**

- **Version Control** - Track resource versions
- **Efficient Updates** - Only fetch when changed
- **Bandwidth Savings** - Reduce unnecessary data transfer
- **Cache Validation** - Validate cache freshness
- **Use Cases** - Dynamic content, API responses

---

### 52. 🧠 What is the difference between CDN caching and browser caching?

**🧠 Concept**

CDN caching distributes content globally, while browser caching stores content locally on user devices.

**💻 Example**

```javascript
// CDN caching
- Global distribution
- Shared across users
- Geographic optimization
- Origin server protection

// Browser caching
- Local to device
- User-specific
- Offline capability
- Personal data storage
```

**💬 Explanation + Insight**

- **CDN Caching** - Global, shared, geographic distribution
- **Browser Caching** - Local, personal, offline capability
- **Performance** - Both improve performance differently
- **Storage** - Different storage characteristics
- **Use Cases** - CDN for global content, browser for personal data

---

### 53. 🧠 How do you cache GraphQL queries efficiently?

**🧠 Concept**

GraphQL caching requires normalized caching, field-level caching, and careful cache invalidation strategies.

**💻 Example**

```javascript
// GraphQL normalized caching
const cache = new InMemoryCache({
  typePolicies: {
    User: {
      keyFields: ["id"],
      fields: {
        posts: {
          merge(existing = [], incoming) {
            return [...existing, ...incoming];
          }
        }
      }
    },
    Post: {
      keyFields: ["id"]
    }
  }
});
```

**💬 Explanation + Insight**

- **Normalized Caching** - Store entities by ID
- **Field-level Caching** - Cache individual fields
- **Cache Invalidation** - Complex invalidation strategies
- **Performance** - Significant performance improvements
- **Use Cases** - Complex data relationships, real-time updates

---

### 54. 🧠 What is HTTP caching vs application-level caching?

**🧠 Concept**

HTTP caching uses browser and CDN caches, while application-level caching stores data in memory or databases.

**💻 Example**

```javascript
// HTTP caching
Cache-Control: max-age=3600
ETag: "abc123"

// Application-level caching
const cache = new Map();
function getCachedData(key) {
  if (cache.has(key)) {
    return cache.get(key);
  }
  const data = fetchFromDatabase(key);
  cache.set(key, data);
  return data;
}
```

**💬 Explanation + Insight**

- **HTTP Caching** - Browser and CDN level
- **Application Caching** - Application memory/database
- **Performance** - Both improve performance
- **Complexity** - Application caching more complex
- **Use Cases** - HTTP for static content, application for dynamic

---

### 55. 🧠 What is the role of service workers in offline-first caching?

**🧠 Concept**

Service workers enable offline functionality by intercepting network requests and serving cached content when offline.

**💻 Example**

```javascript
// Service worker caching
self.addEventListener('fetch', event => {
  event.respondWith(
    caches.match(event.request)
      .then(response => {
        if (response) {
          return response; // Serve from cache
        }
        return fetch(event.request); // Fetch from network
      })
  );
});

// Cache-first strategy
self.addEventListener('fetch', event => {
  event.respondWith(
    caches.open('my-cache').then(cache => {
      return cache.match(event.request).then(response => {
        return response || fetch(event.request).then(fetchResponse => {
          cache.put(event.request, fetchResponse.clone());
          return fetchResponse;
        });
      });
    })
  );
});
```

**💬 Explanation + Insight**

- **Offline Support** - Work without network connection
- **Cache Interception** - Intercept and modify requests
- **Background Sync** - Sync when connection restored
- **User Experience** - Seamless offline experience
- **Use Cases** - PWAs, offline-first applications

---

### 56. 🧠 How would you implement delta (incremental) data fetching?

**🧠 Concept**

Delta fetching only retrieves changed data since the last fetch, reducing bandwidth and improving performance.

**💻 Example**

```javascript
// Delta fetching implementation
const lastSync = localStorage.getItem('lastSync');
const deltaUrl = `/api/data/delta?since=${lastSync}`;

async function fetchDeltaData() {
  const response = await fetch(deltaUrl);
  const { changes, timestamp } = await response.json();
  
  // Apply changes to local data
  changes.forEach(change => {
    if (change.type === 'create') {
      localData.push(change.data);
    } else if (change.type === 'update') {
      const index = localData.findIndex(item => item.id === change.id);
      localData[index] = change.data;
    } else if (change.type === 'delete') {
      localData = localData.filter(item => item.id !== change.id);
    }
  });
  
  localStorage.setItem('lastSync', timestamp);
}
```

**💬 Explanation + Insight**

- **Bandwidth Efficiency** - Only fetch changed data
- **Performance** - Faster updates and synchronization
- **Complexity** - Requires change tracking
- **Use Cases** - Real-time updates, large datasets
- **Implementation** - Server-side change tracking needed

---

### 57. 🧠 How do you cache POST or mutation results securely?

**🧠 Concept**

POST results require careful caching strategies considering security, data freshness, and cache invalidation.

**💻 Example**

```javascript
// Secure POST result caching
const cache = new Map();
const TTL = 5 * 60 * 1000; // 5 minutes

function cachePostResult(key, data, userContext) {
  const cacheKey = `${key}-${userContext.userId}`;
  const cacheItem = {
    data,
    timestamp: Date.now(),
    userContext
  };
  cache.set(cacheKey, cacheItem);
}

function getCachedPostResult(key, userContext) {
  const cacheKey = `${key}-${userContext.userId}`;
  const item = cache.get(cacheKey);
  
  if (item && Date.now() - item.timestamp < TTL) {
    return item.data;
  }
  return null;
}
```

**💬 Explanation + Insight**

- **Security** - User-specific caching
- **Data Freshness** - Short TTL for mutations
- **Cache Invalidation** - Invalidate related data
- **Performance** - Reduce repeated API calls
- **Use Cases** - User-specific data, form submissions

---

### 58. 🧠 How do you synchronize real-time data between multiple tabs?

**🧠 Concept**

Tab synchronization uses BroadcastChannel, localStorage events, or WebSocket connections to keep data in sync.

**💻 Example**

```javascript
// BroadcastChannel synchronization
const channel = new BroadcastChannel('data-sync');

// Send updates to other tabs
function updateData(newData) {
  localStorage.setItem('data', JSON.stringify(newData));
  channel.postMessage({ type: 'data-update', data: newData });
}

// Listen for updates from other tabs
channel.addEventListener('message', event => {
  if (event.data.type === 'data-update') {
    updateLocalState(event.data.data);
  }
});

// localStorage synchronization
window.addEventListener('storage', event => {
  if (event.key === 'data') {
    updateLocalState(JSON.parse(event.newValue));
  }
});
```

**💬 Explanation + Insight**

- **Real-time Sync** - Keep tabs synchronized
- **Multiple Methods** - BroadcastChannel, localStorage, WebSocket
- **User Experience** - Consistent data across tabs
- **Performance** - Efficient synchronization
- **Use Cases** - Multi-tab applications, real-time updates

---

### 59. 🧠 What are long polling, Server-Sent Events (SSE), and WebSockets?

**🧠 Concept**

Different real-time communication methods: long polling keeps connections open, SSE provides server-to-client streaming, WebSockets enable bidirectional communication.

**💻 Example**

```javascript
// Long polling
function longPoll() {
  fetch('/api/updates')
    .then(response => response.json())
    .then(data => {
      handleUpdate(data);
      longPoll(); // Poll again
    });
}

// Server-Sent Events
const eventSource = new EventSource('/api/events');
eventSource.onmessage = event => {
  handleUpdate(JSON.parse(event.data));
};

// WebSocket
const ws = new WebSocket('wss://api.example.com/ws');
ws.onmessage = event => {
  handleUpdate(JSON.parse(event.data));
};
```

**💬 Explanation + Insight**

- **Long Polling** - Simple, works with HTTP
- **SSE** - Server-to-client streaming
- **WebSocket** - Bidirectional real-time communication
- **Performance** - WebSocket most efficient
- **Use Cases** - Different real-time requirements

---

### 60. 🧠 How do you ensure consistency between server and client cache layers?

**🧠 Concept**

Cache consistency requires invalidation strategies, versioning, and synchronization mechanisms between server and client caches.

**💻 Example**

```javascript
// Cache consistency strategies
// 1. Version-based invalidation
const cacheVersion = 'v1.2.3';
const cacheKey = `data-${cacheVersion}`;

// 2. Timestamp-based invalidation
const lastModified = response.headers.get('Last-Modified');
if (cachedData.timestamp < lastModified) {
  // Cache is stale, fetch fresh data
}

// 3. Event-based invalidation
const eventBus = new EventBus();
eventBus.on('data-updated', (dataId) => {
  invalidateCache(`data-${dataId}`);
});
```

**💬 Explanation + Insight**

- **Version Control** - Track cache versions
- **Timestamp Validation** - Check data freshness
- **Event-driven** - Invalidate on data changes
- **Synchronization** - Keep caches in sync
- **Use Cases** - Real-time applications, data consistency

---

*This comprehensive data fetching and caching section covers all essential concepts including REST vs GraphQL, caching strategies, optimistic updates, real-time synchronization, and offline-first approaches for building robust frontend applications.*