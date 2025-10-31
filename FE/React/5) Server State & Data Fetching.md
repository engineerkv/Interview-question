# 🌐 5. Server State & Data Fetching (Q41–50)

---

## 41) What is server state in React applications?

Concept:
Server state is data that comes from external sources like APIs, managed separately from client state, often cached and synchronized with the server.

Example:
```jsx
// Server state - data from API
function UserProfile({ userId }) {
  const [user, setUser] = useState(null);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState(null);
  
  useEffect(() => {
    let active = true;
    (async () => {
      try {
        const res = await fetch(`/api/users/${userId}`);
        const data = await res.json();
        if (active) setUser(data);
      } catch (e) {
        if (active) setError(e);
      } finally {
        if (active) setLoading(false);
      }
    })();
    return () => { active = false; };
  }, [userId]);
  
  if (loading) return <div>Loading...</div>;
  if (error) return <div>Error</div>;
  return <div>{user.name}</div>;
}
```

Deep Insight:
- **External Source**: Data comes from APIs, databases, or external services
- **Caching**: Often cached to improve performance and reduce API calls
- **Synchronization**: Needs to be kept in sync with server data
- **Loading States**: Requires handling of loading, error, and success states
- **Stale Data**: Can become stale and needs refresh strategies

---

## 42) How does React Query manage server state?

Concept:
React Query provides caching, background updates, and synchronization for server state, handling loading states, errors, and data freshness automatically.

Example:
```jsx
import { useQuery, useMutation, useQueryClient } from 'react-query';

function UserProfile({ userId }) {
  const { data: user, isLoading, error } = useQuery({
    queryKey: ['user', userId],
    queryFn: () => fetch(`/api/users/${userId}`).then(res => res.json()),
    staleTime: 60_000
  });
  if (isLoading) return <div>Loading...</div>;
  if (error) return <div>Error</div>;
  return <div>{user.name}</div>;
}
```

Deep Insight:
- **Automatic Caching**: Caches data by query key automatically
- **Background Updates**: Refetches data in background when stale
- **Loading States**: Provides isLoading, isError, isSuccess states
- **Cache Management**: Automatic cache invalidation and updates
- **DevTools**: Excellent debugging experience with React Query DevTools

---

## 43) What are the differences between React Query and Redux Toolkit Query (RTK Query)?

Concept:
React Query is framework-agnostic with more features, while RTK Query is Redux-specific with better integration but fewer caching options.

Example:
```jsx
// React Query
import { useQuery } from 'react-query';

function UserProfile({ userId }) {
  const { data: user, isLoading } = useQuery({
    queryKey: ['user', userId],
    queryFn: () => fetch(`/api/users/${userId}`).then(r => r.json())
  });
  return isLoading ? <div>Loading...</div> : <div>{user.name}</div>;
}

// RTK Query
import { createApi, fetchBaseQuery } from '@reduxjs/toolkit/query/react';

const api = createApi({
  reducerPath: 'api',
  baseQuery: fetchBaseQuery({ baseUrl: '/api' }),
  endpoints: (builder) => ({
    getUser: builder.query({
      query: (id) => `users/${id}`
    })
  })
});

function UserProfile({ userId }) {
  const { data: user, isLoading } = api.useGetUserQuery(userId);
  return isLoading ? <div>Loading...</div> : <div>{user.name}</div>;
}
```

Deep Insight:
- **Framework Support**: React Query works with any framework, RTK Query is Redux-specific
- **Features**: React Query has more caching and synchronization features
- **Integration**: RTK Query integrates better with Redux store
- **Learning Curve**: RTK Query easier if already using Redux
- **Performance**: Both provide excellent performance optimizations

---

## 44) What is the difference between REST and GraphQL APIs?

Concept:
REST uses multiple endpoints with fixed data structures, while GraphQL uses a single endpoint with flexible queries that specify exactly what data is needed.

Example:
```jsx
// REST API - multiple endpoints
const fetchUser = async (userId) => {
  const response = await fetch(`/api/users/${userId}`);
  return response.json();
};
// GraphQL - single endpoint with query
const query = `query($id: ID!){ user(id:$id){ id name } }`;
const fetchGraphQLUser = async (id) => {
  const res = await fetch('/graphql', {
    method: 'POST', headers: { 'Content-Type': 'application/json' },
    body: JSON.stringify({ query, variables: { id } })
  });
  const { data } = await res.json();
  return data.user;
};
```

Deep Insight:
- **REST**: Multiple endpoints, fixed data structures, over-fetching common
- **GraphQL**: Single endpoint, flexible queries, fetch exactly what you need
- **Over-fetching**: REST often fetches more data than needed
- **Under-fetching**: REST may require multiple requests for related data
- **Type Safety**: GraphQL provides better type safety and documentation

---

## 45) What is Apollo Client and how does it integrate with GraphQL?

Concept:
Apollo Client is a GraphQL client that provides caching, state management, and real-time subscriptions, with excellent React integration.

Example:
```jsx
import { ApolloProvider, useQuery, gql } from '@apollo/client';
import { ApolloClient, InMemoryCache } from '@apollo/client';

const client = new ApolloClient({
  uri: 'http://localhost:4000/graphql',
  cache: new InMemoryCache()
});

const USER = gql`query($id: ID!){ user(id:$id){ id name } }`;

function User({ id }) {
  const { data, loading, error } = useQuery(USER, { variables: { id } });
  if (loading) return <div>Loading...</div>;
  if (error) return <div>Error</div>;
  return <div>{data.user.name}</div>;
}

function App(){ return (<ApolloProvider client={client}><User id="1" /></ApolloProvider>); }
```

Deep Insight:
- **Caching**: Automatic caching with normalized cache
- **State Management**: Can replace Redux for GraphQL data
- **Real-time**: Built-in support for subscriptions
- **DevTools**: Excellent debugging with Apollo DevTools
- **React Integration**: Hooks-based API for React components

---

## 46) What are optimistic updates and when should you use them?

Concept:
Optimistic updates immediately update the UI before server confirmation, providing better user experience but requiring rollback mechanisms for failures.

Example:
```jsx
function TodoList() {
  const [todos, setTodos] = useState([]);
  
  const addTodo = async (text) => {
    const newTodo = {
      id: Date.now(),
      text,
      done: false
    };
    // Optimistic update
    setTodos(prev => [newTodo, ...prev]);
    try {
      await fetch('/api/todos', { method: 'POST', body: JSON.stringify(newTodo) });
    } catch (e) {
      // Rollback on error
      setTodos(prev => prev.filter(t => t.id !== newTodo.id));
    }
  };
  
  return <button onClick={() => addTodo('Task')}>Add</button>;
}
```

Deep Insight:
- **Immediate Feedback**: UI updates instantly for better UX
- **Rollback Strategy**: Must handle failures and revert changes
- **Use Cases**: Good for actions that usually succeed
- **Complexity**: Adds complexity to error handling
- **User Experience**: Provides more responsive feel to users

---

## 47) What is caching in React Query and how is it configured?

Concept:
React Query caches data by query key, with configurable stale time, cache time, and refetch intervals to balance performance and data freshness.

Example:
```jsx
import { useQuery } from 'react-query';

function UserProfile({ userId }) {
  const { data: user, isLoading } = useQuery({
    queryKey: ['user', userId],
    queryFn: () => fetchUser(userId),
    staleTime: 30_000,
    cacheTime: 5 * 60_000
  });
  return isLoading ? <div>Loading...</div> : <div>{user.name}</div>;
}
```

Deep Insight:
- **Query Keys**: Unique identifiers for cached data
- **Stale Time**: How long data is considered fresh
- **Cache Time**: How long data stays in cache after component unmounts
- **Refetch Strategies**: Control when data is refetched
- **Retry Logic**: Automatic retry for failed requests

---

## 48) What are query invalidations and refetching strategies?

Concept:
Query invalidation marks cached data as stale, triggering refetches, with strategies like manual invalidation, automatic refetching, and background updates.

Example:
```jsx
import { useQuery, useMutation, useQueryClient } from 'react-query';

function UserProfile({ userId }) {
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
}
```

Deep Insight:
- **Invalidation**: Marks queries as stale to trigger refetch
- **Direct Updates**: Update cache directly for immediate UI updates
- **Selective Invalidation**: Can invalidate specific queries or all queries
- **Background Refetch**: Refetch data in background while showing cached data
- **Optimistic Updates**: Combine with optimistic updates for better UX

---

## 49) How do you handle background fetching and stale data in React Query?

Concept:
Background fetching updates data in the background while showing cached data, with stale time configuration to control when data becomes stale.

Example:
```jsx
function UserProfile({ userId }) {
  const { data: user, isLoading, isStale } = useQuery({
    queryKey: ['user', userId],
    queryFn: () => fetchUser(userId),
    staleTime: 5 * 60 * 1000, // Data fresh for 5 minutes
    refetchOnWindowFocus: true, // Refetch when window gains focus
  });
  return isLoading ? <div>Loading...</div> : <div>{user.name}{isStale ? ' (stale)' : ''}</div>;
}
```

Deep Insight:
- **Stale Data**: Data that's older than staleTime
- **Background Updates**: Refetch data without showing loading state
- **User Experience**: Show cached data while fetching fresh data
- **Configuration**: Fine-tune when and how data is refetched
- **Performance**: Balance between data freshness and performance

---

## 50) How would you manage pagination or infinite scrolling using React Query?

Concept:
Use useInfiniteQuery for infinite scrolling or useQuery with offset/limit for pagination, with proper key management and cache invalidation.

Example:
```jsx
import { useInfiniteQuery } from 'react-query';

function InfinitePostList() {
  const {
    data,
    fetchNextPage,
    hasNextPage,
    isFetchingNextPage
  } = useInfiniteQuery({
    queryKey: ['posts'],
    queryFn: ({ pageParam = 1 }) => fetch(`/api/posts?page=${pageParam}`).then(r => r.json()),
    getNextPageParam: (lastPage) => lastPage.nextPage ?? false
  });
  
  return (
    <div>
      {data?.pages.flatMap(p => p.items).map(post => (
        <div key={post.id}>{post.title}</div>
      ))}
      <button disabled={!hasNextPage || isFetchingNextPage} onClick={() => fetchNextPage()}>
        {isFetchingNextPage ? 'Loading...' : hasNextPage ? 'Load More' : 'No More'}
      </button>
    </div>
  );
}
```

Deep Insight:
- **useInfiniteQuery**: Designed for infinite scrolling scenarios
- **Page Management**: Automatically manages page parameters
- **Cache Strategy**: Each page is cached separately
- **Performance**: Only loads data as needed
- **User Experience**: Smooth infinite scrolling with loading states

---
