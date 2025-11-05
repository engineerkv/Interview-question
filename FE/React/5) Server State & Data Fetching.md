# 🌐 5. Server State & Data Fetching (Q41–50)

---

## 41) What is server state in React applications?

Server state comes from external APIs or databases. It's separate from client state and needs caching and synchronization.

```jsx
function UserProfile({ userId }) {
  const [user, setUser] = useState(null);
  const [loading, setLoading] = useState(true);
  useEffect(() => {
    fetch(`/api/users/${userId}`).then(r => r.json()).then(data => { setUser(data); setLoading(false); });
  }, [userId]);
  if (loading) return <div>Loading...</div>;
  return <div>{user?.name}</div>;
}
```

- **Core Concept**: Data from external sources that needs to stay in sync with server
- **Real-World Challenge**: Server state can become stale and needs refresh strategies
- **Common Mistake**: Managing server state like client state - it needs different handling
- **Best Practice**: Use libraries like React Query to handle caching and synchronization automatically
- **Interview Tip**: Explain the difference between server state (external, async) and client state (local, sync)

---

## 42) How does React Query manage server state?

React Query automatically caches and synchronizes server state. It handles loading, errors, and data freshness without manual management.

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

- **Core Benefit**: Automatic caching, background updates, and error handling
- **Real-World Use**: Eliminates boilerplate for loading states, error handling, and cache management
- **Common Mistake**: Not using query keys properly - keys must be unique and stable
- **Optimization**: Configure staleTime and cacheTime to balance freshness and performance
- **Interview Tip**: Explain how React Query solves the "loading, error, cache" problem automatically

---

## 43) What are the differences between React Query and Redux Toolkit Query (RTK Query)?

React Query is framework-agnostic with more features. RTK Query is Redux-specific with better integration.

```jsx
// React Query
const { data: user, isLoading } = useQuery({
  queryKey: ['user', userId],
  queryFn: () => fetch(`/api/users/${userId}`).then(r => r.json())
});

// RTK Query
const api = createApi({
  reducerPath: 'api',
  baseQuery: fetchBaseQuery({ baseUrl: '/api' }),
  endpoints: (b) => ({ getUser: b.query({ query: (id) => `users/${id}` }) })
});
const { data: user, isLoading } = api.useGetUserQuery(userId);
```

- **Key Difference**: React Query works with any framework, RTK Query requires Redux
- **Real-World Choice**: Use RTK Query if already using Redux, React Query if not
- **Feature Comparison**: React Query has more caching features, RTK Query integrates with Redux store
- **Learning Curve**: RTK Query easier if you know Redux, React Query simpler for new projects
- **Interview Tip**: Explain trade-offs - React Query is more flexible, RTK Query is better integrated with Redux

---

## 44) What is the difference between REST and GraphQL APIs?

REST uses multiple endpoints with fixed data. GraphQL uses one endpoint with flexible queries.

```jsx
// REST
const fetchUser = async (id) => (await fetch(`/api/users/${id}`)).json();

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

- **Core Difference**: REST has multiple endpoints, GraphQL has one endpoint with queries
- **Real-World Impact**: REST often over-fetches or under-fetches, GraphQL fetches exactly what you need
- **Common Mistake**: Using GraphQL for simple apps - REST is simpler for basic CRUD
- **Performance**: GraphQL reduces over-fetching but adds complexity, REST is simpler but less efficient
- **Interview Tip**: Explain when to use each - REST for simple apps, GraphQL for complex data requirements

---

## 45) What is Apollo Client and how does it integrate with GraphQL?

Apollo Client is a GraphQL client with caching, state management, and real-time subscriptions for React.

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

- **Core Purpose**: Manages GraphQL queries, caching, and subscriptions in React apps
- **Real-World Use**: Can replace Redux for GraphQL data, provides normalized caching
- **Key Feature**: Automatic cache normalization and updates, real-time subscriptions
- **DevTools**: Excellent debugging with Apollo DevTools for queries and cache
- **Interview Tip**: Explain how Apollo Client handles GraphQL complexity automatically

---

## 46) What are optimistic updates and when should you use them?

Optimistic updates change UI immediately before server confirmation. They improve UX but need rollback for failures.

```jsx
function TodoList() {
  const [todos, setTodos] = useState([]);
  const addTodo = async (text) => {
    const newTodo = { id: Date.now(), text, done: false };
    setTodos(prev => [newTodo, ...prev]);
    try {
      await fetch('/api/todos', { method: 'POST', body: JSON.stringify(newTodo) });
    } catch (e) {
      setTodos(prev => prev.filter(t => t.id !== newTodo.id));
    }
  };
  return <button onClick={() => addTodo('Task')}>Add</button>;
}
```

- **Core Benefit**: Instant UI feedback makes apps feel more responsive
- **Real-World Use**: Good for actions that usually succeed like likes, comments, or simple updates
- **Common Mistake**: Not implementing rollback - failures must revert optimistic changes
- **Best Practice**: Use for high-success-rate actions, avoid for critical financial operations
- **Interview Tip**: Explain the trade-off between better UX and added complexity

---

## 47) What is caching in React Query and how is it configured?

React Query caches data by query key. Configure staleTime and cacheTime to control freshness and retention.

```jsx
const { data: user, isLoading } = useQuery({
  queryKey: ['user', userId],
  queryFn: () => fetchUser(userId),
  staleTime: 30000,
  cacheTime: 300000
});
return isLoading ? <div>Loading...</div> : <div>{user?.name}</div>;
```

- **Core Mechanism**: Query keys identify cached data, must be unique and stable
- **Stale Time**: How long data stays fresh before refetching
- **Cache Time**: How long data stays in cache after component unmounts
- **Real-World Tuning**: Balance staleTime for freshness vs performance
- **Interview Tip**: Explain that staleTime controls freshness, cacheTime controls memory usage

---

## 48) What are query invalidations and refetching strategies?

Query invalidation marks cached data as stale, triggering refetches. Use it after mutations to keep data fresh.

```jsx
const queryClient = useQueryClient();
const { data: user } = useQuery({
  queryKey: ['user', userId],
  queryFn: () => fetch(`/api/users/${userId}`).then(r => r.json())
});
const updateUser = useMutation({
  mutationFn: (payload) => fetch(`/api/users/${userId}`, { method: 'PUT', body: JSON.stringify(payload) }),
  onSuccess: () => queryClient.invalidateQueries({ queryKey: ['user', userId] })
});
return <button onClick={() => updateUser.mutate({ name: 'New' })}>Update</button>;
```

- **Core Purpose**: Keep cache in sync with server after mutations
- **Real-World Pattern**: Invalidate queries after create/update/delete operations
- **Strategies**: Manual invalidation, automatic refetch, or direct cache updates
- **Optimization**: Use selective invalidation to avoid unnecessary refetches
- **Interview Tip**: Explain that invalidation is key to keeping server state synchronized

---

## 49) How do you handle background fetching and stale data in React Query?

Background fetching updates data silently while showing cached data. Configure staleTime to control when data becomes stale.

```jsx
const { data: user, isLoading, isStale } = useQuery({
  queryKey: ['user', userId],
  queryFn: () => fetchUser(userId),
  staleTime: 300000,
  refetchOnWindowFocus: true
});
return isLoading ? <div>Loading...</div> : <div>{user?.name}{isStale ? ' (stale)' : ''}</div>;
```

- **Core Feature**: Shows cached data immediately, fetches fresh data in background
- **Real-World Benefit**: Users see content instantly, updates happen seamlessly
- **Configuration**: Set staleTime to balance freshness vs number of requests
- **User Experience**: Better than showing loading states for every refetch
- **Interview Tip**: Explain how background fetching improves perceived performance

---

## 50) How would you manage pagination or infinite scrolling using React Query?

Use useInfiniteQuery for infinite scrolling. It automatically manages pages and caches each page separately.

```jsx
const { data, fetchNextPage, hasNextPage, isFetchingNextPage } = useInfiniteQuery({
  queryKey: ['posts'],
  queryFn: ({ pageParam = 1 }) => fetch(`/api/posts?page=${pageParam}`).then(r => r.json()),
  getNextPageParam: (lastPage) => lastPage.nextPage ?? false
});
return (
  <div>
    {data?.pages.flatMap(p => p.items).map(post => <div key={post.id}>{post.title}</div>)}
    <button disabled={!hasNextPage || isFetchingNextPage} onClick={() => fetchNextPage()}>
      {isFetchingNextPage ? 'Loading...' : hasNextPage ? 'Load More' : 'No More'}
    </button>
  </div>
);
```

- **Core Purpose**: Handle paginated data with automatic page management
- **Real-World Use**: Infinite scroll feeds, paginated tables, or any chunked data
- **Performance**: Only loads pages as needed, caches each page separately
- **User Experience**: Smooth scrolling with loading states for next pages
- **Interview Tip**: Explain how useInfiniteQuery simplifies pagination logic

---
