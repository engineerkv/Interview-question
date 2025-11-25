# 5. React Latest Features (Q57–63)

---

## Q58. Concurrent Rendering in React 18

Concurrent Rendering allows React to interrupt rendering work to handle urgent updates - it keeps UI responsive during heavy operations by prioritizing user interactions over background work. React can pause and resume rendering work based on priority.

- **Trade-offs**: The catch is higher priority updates interrupt lower priority ones automatically - existing code works without changes, new features are opt-in. Concurrent rendering enables React 18+ features like Suspense and Transitions, but watch out - UI stays responsive during expensive operations like filtering large lists.

Example:

```jsx
const [isPending, startTransition] = useTransition();
const [results, setResults] = useState([]);
const onSearch = (q) => 
  startTransition(() => setResults(bigList.filter(item => item.includes(q))));
return (
  <button onClick={() => onSearch(query)}>
    {isPending ? 'Searching...' : 'Search'}
  </button>
);
```

<div align="center">

**[← Previous: Server State & Data Fetching](4%29%20Server%20State%20%26%20Data%20Fetching.md)** | **[Next: Performance Optimization →](6%29%20Performance%20Optimization.md)**

</div>

---

## Q59. Suspense and how to use it

Suspense allows components to wait for something before rendering - use it for loading states with lazy components or data fetching, replacing manual loading state management. Suspense declaratively handles loading states for async operations.

- **Trade-offs**: The catch is can have multiple Suspense boundaries for granular loading states - combine with Error Boundaries for complete async error handling. Suspense replaces loading state management with declarative boundaries, but watch out - good for code splitting with lazy(), data fetching with React Query, or any async component.

Example:

```jsx
const LazyComponent = lazy(() => import('./LazyComponent'));
function App() {
  return (
    <Suspense fallback={<div>Loading...</div>}>
      <LazyComponent />
    </Suspense>
  );
}
```

---

## Q60. Transitions in React 18

Transitions mark state updates as non-urgent - React keeps UI responsive by interrupting heavy work to handle user input, prioritizing interactions over background updates. Transitions mark updates that can be interrupted, keeping urgent updates responsive.

- **Trade-offs**: The catch is useDeferredValue defers value updates to show stale data while computing fresh data - prevents UI freezing during expensive operations. Transitions prioritize user interactions over background work, but watch out - good for search results, filtering, or any heavy computation triggered by user input.

Example:

```jsx
const [isPending, startTransition] = useTransition();
const [input, setInput] = useState('');
const [list, setList] = useState([]);
const deferredInput = useDeferredValue(input);
const update = (value) => {
  setInput(value);
  startTransition(() => setList(new Array(5000).fill(value)));
};
return (
  <div>
    <input value={input} onChange={e => update(e.target.value)} />
    {isPending ? 'Updating…' : 
     list.slice(0,5).map((_, i) => <div key={i}>{deferredInput}</div>)}
  </div>
);
```

---

## Q61. Strict Mode and why it's important

Strict Mode double-renders components in development to detect side effects - it helps find bugs before production by exposing issues that might only appear in production. Development tool that helps identify side effects and bugs.

- **Trade-offs**: The catch is catches bugs like using state in render or not cleaning up effects - only affects development builds, no performance impact in production. Double rendering helps catch bugs that might only appear in production, but watch out - components render twice to expose side effects in render phase.

Example:

```jsx
function App() {
  return (
    <StrictMode>
      <MyComponent />
    </StrictMode>
  );
}
```

---

## Q62. New features in React 19

React 19 adds Actions for forms, Resource API for data fetching, and enhanced Suspense with better error handling - it continues React 18's concurrent rendering improvements. Actions provide built-in form handling with useTransition for async form submissions.

- **Trade-offs**: The catch is enhanced Suspense offers better error boundaries and loading states - improved performance and developer experience over React 18. React 19 continues React 18's concurrent rendering improvements with better DX, but watch out - Resource API introduces new use() hook for data fetching with Suspense integration.

Example:

```jsx
const [isPending, startTransition] = useTransition();
const handleSubmit = async (formData) => 
  startTransition(async () => 
    await fetch('/api/contact', { 
      method: 'POST', 
      body: formData 
    })
  );
return (
  <form onSubmit={(e) => { 
    e.preventDefault(); 
    handleSubmit(new FormData(e.currentTarget)); 
  }}>
    {isPending ? 'Submitting…' : <button type="submit">Send</button>}
  </form>
);
```

---

## Q63. React 19 Actions and Resource API

React 19 Actions handle form submissions with built-in async support, while Resource API uses the use() hook for data fetching with automatic Suspense integration. Actions simplify form handling with automatic pending states and error handling.

- **Trade-offs**: The catch is use() can unwrap promises and context values automatically - better integration between data fetching and React's rendering model. Actions and Resource API simplify async operations in React 19, but watch out - Resource API's use() hook works seamlessly with Suspense boundaries.

Example:

```jsx
async function fetchUser(id) {
  const res = await fetch(`/api/users/${id}`);
  return res.json();
}

function UserProfile({ userId }) {
  const user = use(fetchUser(userId));
  return <div>{user.name}</div>;
}
```

---

## Q64. React Server Components (RSC) and how they work

React Server Components render on the server and send zero JavaScript to the client - they reduce bundle size and improve performance by keeping heavy logic on the server. Server Components render on server, send HTML not JavaScript, reducing bundle size.

- **Trade-offs**: The catch is can't use hooks, browser APIs, or event handlers - use Client Components for interactivity, needs Next.js App Router, Remix, or similar, not available in plain React. RSC is a paradigm shift enabling server-side rendering with React components, but watch out - can access databases directly, no API routes needed, smaller client bundles.

Example:

```jsx
// Server Component (no 'use client')
async function BlogPost({ postId }) {
  const post = await db.posts.findById(postId);
  return (
    <article>
      <h1>{post.title}</h1>
      <LikeButton postId={postId} />
    </article>
  );
}

// Client Component ('use client' required)
'use client';
function LikeButton({ postId }) {
  const [likes, setLikes] = useState(0);
  return <button onClick={() => setLikes(likes + 1)}>Like ({likes})</button>;
}
```

---

<div align="center">

**[← Previous: Server State & Data Fetching](4%29%20Server%20State%20%26%20Data%20Fetching.md)** | **[Next: Performance Optimization →](6%29%20Performance%20Optimization.md)**

</div>
