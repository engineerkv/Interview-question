# 🌐 5. Server State & Data Fetching (Q42–51)

---

## 🧩 Q42. What is server state and how do you manage it?

### 🧠 Concept

Server state comes from external APIs or databases. It's separate from client state and needs caching and synchronization to stay fresh and consistent.

---

### 💡 Example

```jsx
function UserProfile({ userId }) {
  const [user, setUser] = useState(null);
  const [loading, setLoading] = useState(true);
  useEffect(() => {
    fetch(`/api/users/${userId}`)
      .then(r => r.json())
      .then(data => { setUser(data); setLoading(false); });
  }, [userId]);
  if (loading) return <div>Loading...</div>;
  return <div>{user?.name}</div>;
}
```

---

### 🔍 Deep Insights

* **Rule:** Server state is data from external sources that needs to stay in sync with server.
* **Use Case:** Server state can become stale and needs refresh strategies.
* **Common Mistake:** Managing server state like client state—it needs different handling.
* **Pro Tip:** Use libraries like React Query to handle caching and synchronization automatically.

---

### ⭐ Senior Takeaway

Server state (external, async) differs from client state (local, sync)—handle accordingly.

---

## 🧩 Q43. What is React Query and how do you use it?

### 🧠 Concept

React Query automatically caches and synchronizes server state. It handles loading, errors, and data freshness without manual management, eliminating boilerplate.

---

### 💡 Example

```jsx
function UserProfile({ userId }) {
  const { data: user, isLoading } = useQuery({
    queryKey: ['user', userId],
    queryFn: () => fetch(`/api/users/${userId}`).then(r => r.json()),
    staleTime: 60000
  });
  if (isLoading) return <div>Loading...</div>;
  return <div>{user?.name}</div>;
}
```

---

### 🔍 Deep Insights

* **Rule:** Automatic caching, background updates, and error handling eliminate boilerplate.
* **Use Case:** Query keys must be unique and stable—they identify cached data.
* **Common Mistake:** Not using query keys properly causes cache issues.
* **Pro Tip:** Configure staleTime and cacheTime to balance freshness and performance.

---

### ⭐ Senior Takeaway

React Query solves the "loading, error, cache" problem automatically.

---

## 🧩 Q44. What is RTK Query and how does it work?

### 🧠 Concept

RTK Query is Redux Toolkit's solution for server state. It integrates with Redux store and provides automatic caching, similar to React Query but Redux-specific.

---

### 💡 Example

```jsx
const api = createApi({
  reducerPath: 'api',
  baseQuery: fetchBaseQuery({ baseUrl: '/api' }),
  endpoints: (b) => ({
    getUser: b.query({ query: (id) => `users/${id}` })
  })
});
const { data: user, isLoading } = api.useGetUserQuery(userId);
```

---

### 🔍 Deep Insights

* **Rule:** RTK Query requires Redux, React Query works with any framework.
* **Use Case:** Use RTK Query if already using Redux, React Query if not.
* **Common Mistake:** RTK Query integrates with Redux store, React Query has more caching features.
* **Pro Tip:** RTK Query easier if you know Redux, React Query simpler for new projects.

---

### ⭐ Senior Takeaway

RTK Query is better integrated with Redux, React Query is more flexible.

---

## 🧩 Q45. What is the difference between REST and GraphQL?

### 🧠 Concept

REST uses multiple endpoints with fixed data structures. GraphQL uses one endpoint with flexible queries that fetch exactly what you need.

---

### 💡 Example

```jsx
// REST
const fetchUser = async (id) => 
  (await fetch(`/api/users/${id}`)).json();

// GraphQL
const query = `query($id: ID!){ user(id:$id){ id name } }`;
const fetchGraphQLUser = async (id) => {
  const res = await fetch('/graphql', {
    method: 'POST',
    headers: { 'Content-Type': 'application/json' },
    body: JSON.stringify({ query, variables: { id } })
  });
  return (await res.json()).data.user;
};
```

---

### 🔍 Deep Insights

* **Rule:** REST has multiple endpoints, GraphQL has one endpoint with queries.
* **Use Case:** REST often over-fetches or under-fetches, GraphQL fetches exactly what you need.
* **Common Mistake:** Using GraphQL for simple apps—REST is simpler for basic CRUD.
* **Pro Tip:** GraphQL reduces over-fetching but adds complexity, REST is simpler but less efficient.

---

### ⭐ Senior Takeaway

Use REST for simple apps, GraphQL for complex data requirements.

---

## 🧩 Q46. What is Apollo Client and how do you use it?

### 🧠 Concept

Apollo Client is a GraphQL client with caching, state management, and real-time subscriptions for React. It manages GraphQL complexity automatically.

---

### 💡 Example

```jsx
const client = new ApolloClient({
  uri: 'http://localhost:4000/graphql',
  cache: new InMemoryCache()
});
const USER = gql`query($id: ID!){ user(id:$id){ id name } }`;
function User({ id }) {
  const { data, loading } = useQuery(USER, { variables: { id } });
  if (loading) return <div>Loading...</div>;
  return <div>{data?.user?.name}</div>;
}
```

---

### 🔍 Deep Insights

* **Rule:** Apollo Client manages GraphQL queries, caching, and subscriptions in React apps.
* **Use Case:** Can replace Redux for GraphQL data, provides normalized caching.
* **Common Mistake:** Automatic cache normalization and updates, real-time subscriptions.
* **Pro Tip:** Excellent debugging with Apollo DevTools for queries and cache.

---

### ⭐ Senior Takeaway

Apollo Client handles GraphQL complexity automatically with great tooling.

---

## 🧩 Q47. How do you implement optimistic updates?

### 🧠 Concept

Optimistic updates change UI immediately before server confirmation. They improve UX but need rollback for failures to keep data consistent.

---

### 💡 Example

```jsx
function TodoList() {
  const [todos, setTodos] = useState([]);
  const addTodo = async (text) => {
    const newTodo = { id: Date.now(), text, done: false };
    setTodos(prev => [newTodo, ...prev]);
    try {
      await fetch('/api/todos', { 
        method: 'POST', 
        body: JSON.stringify(newTodo) 
      });
    } catch (e) {
      setTodos(prev => prev.filter(t => t.id !== newTodo.id));
    }
  };
  return <button onClick={() => addTodo('Task')}>Add</button>;
}
```

---

### 🔍 Deep Insights

* **Rule:** Instant UI feedback makes apps feel more responsive.
* **Use Case:** Good for actions that usually succeed like likes, comments, or simple updates.
* **Common Mistake:** Not implementing rollback—failures must revert optimistic changes.
* **Pro Tip:** Use for high-success-rate actions, avoid for critical financial operations.

---

### ⭐ Senior Takeaway

Optimistic updates trade complexity for better UX—use wisely.

---

## 🧩 Q48. How do you handle caching in React applications?

### 🧠 Concept

React Query caches data by query key. Configure staleTime and cacheTime to control freshness and retention, balancing performance with data freshness.

---

### 💡 Example

```jsx
const { data: user, isLoading } = useQuery({
  queryKey: ['user', userId],
  queryFn: () => fetchUser(userId),
  staleTime: 30000,
  cacheTime: 300000
});
return isLoading ? <div>Loading...</div> : <div>{user?.name}</div>;
```

---

### 🔍 Deep Insights

* **Rule:** Query keys identify cached data, must be unique and stable.
* **Use Case:** staleTime controls how long data stays fresh before refetching.
* **Common Mistake:** cacheTime controls how long data stays in cache after component unmounts.
* **Pro Tip:** Balance staleTime for freshness vs performance.

---

### ⭐ Senior Takeaway

staleTime controls freshness, cacheTime controls memory usage.

---

## 🧩 Q49. How do you implement query invalidation?

### 🧠 Concept

Query invalidation marks cached data as stale, triggering refetches. Use it after mutations to keep data fresh and synchronized with the server.

---

### 💡 Example

```jsx
const queryClient = useQueryClient();
const { data: user } = useQuery({
  queryKey: ['user', userId],
  queryFn: () => fetch(`/api/users/${userId}`).then(r => r.json())
});
const updateUser = useMutation({
  mutationFn: (payload) => 
    fetch(`/api/users/${userId}`, { 
      method: 'PUT', 
      body: JSON.stringify(payload) 
    }),
  onSuccess: () => 
    queryClient.invalidateQueries({ queryKey: ['user', userId] })
});
return (
  <button onClick={() => updateUser.mutate({ name: 'New' })}>
    Update
  </button>
);
```

---

### 🔍 Deep Insights

* **Rule:** Invalidation keeps cache in sync with server after mutations.
* **Use Case:** Invalidate queries after create/update/delete operations.
* **Common Mistake:** Use selective invalidation to avoid unnecessary refetches.
* **Pro Tip:** Manual invalidation, automatic refetch, or direct cache updates.

---

### ⭐ Senior Takeaway

Invalidation is key to keeping server state synchronized.

---

## 🧩 Q50. How do you implement background fetching?

### 🧠 Concept

Background fetching updates data silently while showing cached data. Configure staleTime to control when data becomes stale and triggers background updates.

---

### 💡 Example

```jsx
const { data: user, isLoading, isStale } = useQuery({
  queryKey: ['user', userId],
  queryFn: () => fetchUser(userId),
  staleTime: 300000,
  refetchOnWindowFocus: true
});
return (
  isLoading ? <div>Loading...</div> : 
  <div>{user?.name}{isStale ? ' (stale)' : ''}</div>
);
```

---

### 🔍 Deep Insights

* **Rule:** Shows cached data immediately, fetches fresh data in background.
* **Use Case:** Users see content instantly, updates happen seamlessly.
* **Common Mistake:** Set staleTime to balance freshness vs number of requests.
* **Pro Tip:** Better than showing loading states for every refetch.

---

### ⭐ Senior Takeaway

Background fetching improves perceived performance significantly.

---

## 🧩 Q51. How do you implement pagination and infinite scrolling?

### 🧠 Concept

Use useInfiniteQuery for infinite scrolling. It automatically manages pages and caches each page separately, simplifying pagination logic.

---

### 💡 Example

```jsx
const { data, fetchNextPage, hasNextPage, isFetchingNextPage } = 
  useInfiniteQuery({
    queryKey: ['posts'],
    queryFn: ({ pageParam = 1 }) => 
      fetch(`/api/posts?page=${pageParam}`).then(r => r.json()),
    getNextPageParam: (lastPage) => lastPage.nextPage ?? false
  });
return (
  <div>
    {data?.pages.flatMap(p => p.items).map(post => 
      <div key={post.id}>{post.title}</div>
    )}
    <button 
      disabled={!hasNextPage || isFetchingNextPage} 
      onClick={() => fetchNextPage()}
    >
      {isFetchingNextPage ? 'Loading...' : 
       hasNextPage ? 'Load More' : 'No More'}
    </button>
  </div>
);
```

---

### 🔍 Deep Insights

* **Rule:** useInfiniteQuery handles paginated data with automatic page management.
* **Use Case:** Infinite scroll feeds, paginated tables, or any chunked data.
* **Common Mistake:** Only loads pages as needed, caches each page separately.
* **Pro Tip:** Smooth scrolling with loading states for next pages.

---

### ⭐ Senior Takeaway

useInfiniteQuery simplifies pagination logic significantly.

---
