<div align="center">

**[← Previous: State Management](3%29%20State%20Management.md)** | **[Next: React Latest Features →](5%29%20React%20Latest%20Features.md)**

</div>

# 🌐 4. Server State & Data Fetching (Q46–55)

---

## Q46. 📊 Server state and how to manage it

Server state comes from external APIs or databases - it's separate from client state and needs caching and synchronization to stay fresh and consistent. Server state is data from external sources that needs to stay in sync with server.

- **Trade-offs**: The catch is managing server state like client state - it needs different handling, use libraries like React Query to handle caching and synchronization automatically. Server state (external, async) differs from client state (local, sync), so handle accordingly, but watch out - server state can become stale and needs refresh strategies.

Example:

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

## Q47. 🔍 React Query and how to use it

React Query automatically caches and synchronizes server state - it handles loading, errors, and data freshness without manual management, eliminating boilerplate. Automatic caching, background updates, and error handling eliminate boilerplate.

- **Trade-offs**: The catch is not using query keys properly causes cache issues - configure staleTime and gcTime to balance freshness and performance. React Query solves the "loading, error, cache" problem automatically, but watch out - query keys must be unique and stable, they identify cached data.

Example:

```jsx
const {
  data,
  error,
  isLoading,
  isFetching,
  isError,
  isSuccess,
  refetch,
} = useQuery({
  queryKey: ['user', userId],
  queryFn: () => fetch(`/api/users/${userId}`).then(r => r.json()),
  enabled: !!userId,
  staleTime: 1000 * 60,       // 1 min
  gcTime: 1000 * 60 * 5,      // 5 min
  retry: 2,
  refetchOnWindowFocus: true,
  refetchInterval: false,     // no auto-refetch
  select: (data) => data.user,
  placeholderData: { user: { name: 'Loading...' } },
  onError: err => console.error(err),
  onSuccess: data => console.log('Success', data),
});

```

---

## Q48. 🔍 RTK Query and how it works

RTK Query is Redux Toolkit's solution for server state - it integrates with Redux store and provides automatic caching, similar to React Query but Redux-specific. RTK Query requires Redux, React Query works with any framework.

- **Trade-offs**: The catch is RTK Query integrates with Redux store, React Query has more caching features - RTK Query easier if you know Redux, React Query simpler for new projects. RTK Query is better integrated with Redux, React Query is more flexible, but watch out - use RTK Query if already using Redux, React Query if not.

Example:

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

## Q49. 🌐 REST vs GraphQL

REST uses multiple endpoints with fixed data structures, while GraphQL uses one endpoint with flexible queries that fetch exactly what you need. REST has multiple endpoints, GraphQL has one endpoint with queries.

- **Trade-offs**: The catch is using GraphQL for simple apps - REST is simpler for basic CRUD, GraphQL reduces over-fetching but adds complexity, REST is simpler but less efficient. Use REST for simple apps, GraphQL for complex data requirements, but watch out - REST often over-fetches or under-fetches, GraphQL fetches exactly what you need.

Example:

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

## Q50. 🔧 Apollo Client and how to use it

Apollo Client is a GraphQL client with caching, state management, and real-time subscriptions for React - it manages GraphQL complexity automatically. Apollo Client manages GraphQL queries, caching, and subscriptions in React apps.

- **Trade-offs**: The catch is automatic cache normalization and updates, real-time subscriptions - excellent debugging with Apollo DevTools for queries and cache. Apollo Client handles GraphQL complexity automatically with great tooling, but watch out - it can replace Redux for GraphQL data, provides normalized caching.

Example:

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

## Q51. 🔄 Implementing optimistic updates

Optimistic updates change UI immediately before server confirmation - they improve UX but need rollback for failures to keep data consistent. Instant UI feedback makes apps feel more responsive.

- **Trade-offs**: The catch is not implementing rollback - failures must revert optimistic changes, use for high-success-rate actions, avoid for critical financial operations. Optimistic updates trade complexity for better UX, so use wisely, but watch out - good for actions that usually succeed like likes, comments, or simple updates.

Example:

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

## Q52. 💾 Handling caching in React applications

React Query caches data by query key - configure staleTime and cacheTime to control freshness and retention, balancing performance with data freshness. Query keys identify cached data, must be unique and stable.

- **Trade-offs**: The catch is cacheTime controls how long data stays in cache after component unmounts - balance staleTime for freshness vs performance. staleTime controls freshness, cacheTime controls memory usage, but watch out - staleTime controls how long data stays fresh before refetching.

Example:

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

## Q53. 🔍 Implementing query invalidation

Query invalidation marks cached data as stale, triggering refetches - use it after mutations to keep data fresh and synchronized with the server. Invalidation keeps cache in sync with server after mutations.

- **Trade-offs**: The catch is use selective invalidation to avoid unnecessary refetches - manual invalidation, automatic refetch, or direct cache updates. Invalidation is key to keeping server state synchronized, but watch out - invalidate queries after create/update/delete operations.

Example:

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

## Q54. 🔧 Implementing background fetching

Background fetching updates data silently while showing cached data - configure staleTime to control when data becomes stale and triggers background updates. Shows cached data immediately, fetches fresh data in background.

- **Trade-offs**: The catch is set staleTime to balance freshness vs number of requests - better than showing loading states for every refetch. Background fetching improves perceived performance significantly, but watch out - users see content instantly, updates happen seamlessly.

Example:

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

## Q55. 🔧 Implementing pagination and infinite scrolling

Use useInfiniteQuery for infinite scrolling - it automatically manages pages and caches each page separately, simplifying pagination logic. useInfiniteQuery handles paginated data with automatic page management.

- **Trade-offs**: The catch is only loads pages as needed, caches each page separately - smooth scrolling with loading states for next pages. useInfiniteQuery simplifies pagination logic significantly, but watch out - good for infinite scroll feeds, paginated tables, or any chunked data.

Example:

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

<div align="center">

**[← Previous: State Management](3%29%20State%20Management.md)** | **[Next: React Latest Features →](5%29%20React%20Latest%20Features.md)**

</div>

