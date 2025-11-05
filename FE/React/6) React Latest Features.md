# ⚙️ 6. React Latest Features (Q51–58)

---

## 51) What is Concurrent Rendering in React 18/19?

Concurrent Rendering lets React interrupt rendering work to handle urgent updates. It keeps UI responsive during heavy operations.

```jsx
const [isPending, startTransition] = useTransition();
const [results, setResults] = useState([]);
const onSearch = (q) => startTransition(() => setResults(bigList.filter(item => item.includes(q))));
return <button onClick={() => onSearch(query)}>{isPending ? 'Searching...' : 'Search'}</button>;
```

- **Core Feature**: React can pause and resume rendering work based on priority
- **Real-World Benefit**: UI stays responsive during expensive operations like filtering large lists
- **How It Works**: Higher priority updates interrupt lower priority ones automatically
- **Backwards Compatible**: Existing code works without changes, new features are opt-in
- **Interview Tip**: Explain that concurrent rendering enables React 18+ features like Suspense and Transitions

---

## 52) What is Suspense in React and how does it work with data fetching?

Suspense lets components wait for something before rendering. Use it for loading states with lazy components or data fetching.

```jsx
const LazyComponent = lazy(() => import('./LazyComponent'));
function App() {
  return <Suspense fallback={<div>Loading...</div>}><LazyComponent /></Suspense>;
}
```

- **Core Purpose**: Declaratively handle loading states for async operations
- **Real-World Use**: Code splitting with lazy(), data fetching with React Query, or any async component
- **Nested Boundaries**: Can have multiple Suspense boundaries for granular loading states
- **Error Handling**: Combine with Error Boundaries for complete async error handling
- **Interview Tip**: Explain that Suspense replaces loading state management with declarative boundaries

---

## 53) What are Transitions and how do they help with UI responsiveness?

Transitions mark state updates as non-urgent. React keeps UI responsive by interrupting heavy work to handle user input.

```jsx
const [isPending, startTransition] = useTransition();
const [input, setInput] = useState('');
const [list, setList] = useState([]);
const deferredInput = useDeferredValue(input);
const update = (value) => {
  setInput(value);
  startTransition(() => setList(new Array(5000).fill(value)));
};
return <div><input value={input} onChange={e => update(e.target.value)} />{isPending ? 'Updating…' : list.slice(0,5).map((_, i) => <div key={i}>{deferredInput}</div>)}</div>;
```

- **Core Purpose**: Mark updates that can be interrupted, keeping urgent updates (like typing) responsive
- **Real-World Use**: Search results, filtering, or any heavy computation triggered by user input
- **useDeferredValue**: Defer value updates to show stale data while computing fresh data
- **User Experience**: Prevents UI freezing during expensive operations
- **Interview Tip**: Explain that transitions prioritize user interactions over background work

---

## 54) What is Strict Mode and what does double rendering mean in development?

Strict Mode double-renders components in development to detect side effects. It helps find bugs before production.

```jsx
function App() {
  return <StrictMode><MyComponent /></StrictMode>;
}
```

- **Core Purpose**: Development tool that helps identify side effects and bugs
- **Double Rendering**: Components render twice to expose side effects in render phase
- **Real-World Benefit**: Catches bugs like using state in render or not cleaning up effects
- **Production Safe**: Only affects development builds, no performance impact in production
- **Interview Tip**: Explain that double rendering helps catch bugs that might only appear in production

---

## 55) What is the difference between blocking rendering and concurrent rendering?

Blocking rendering processes updates synchronously. Concurrent rendering can interrupt and resume work for better UX.

```jsx
// Blocking (React 17)
const handleClick = () => { /* blocking work */ setCount(c => c + 1); };

// Concurrent (React 18+)
const [isPending, startTransition] = useTransition();
return <button onClick={() => startTransition(() => setCount(c => c + 1))}>{isPending ? 'Working…' : `Clicked ${count}`}</button>;
```

- **Blocking**: Updates block UI until complete, can cause janky interactions
- **Concurrent**: Updates can be interrupted, UI stays responsive during heavy work
- **Real-World Impact**: Concurrent rendering enables smooth interactions during expensive operations
- **Backwards Compatible**: Existing code works without changes, new features are opt-in
- **Interview Tip**: Explain that concurrent rendering is the foundation for React 18+ features

---

## 56) What's new in React 19 (Actions, Resource API, Enhanced Suspense)?

React 19 adds Actions for forms, Resource API for data fetching, and enhanced Suspense with better error handling.

```jsx
const [isPending, startTransition] = useTransition();
const handleSubmit = async (formData) => startTransition(async () => await fetch('/api/contact', { method: 'POST', body: formData }));
return <form onSubmit={(e) => { e.preventDefault(); handleSubmit(new FormData(e.currentTarget)); }}>{isPending ? 'Submitting…' : <button type="submit">Send</button>}</form>;
```

- **Actions**: Built-in form handling with useTransition for async form submissions
- **Resource API**: New use() hook for data fetching with Suspense integration
- **Enhanced Suspense**: Better error boundaries and loading states for async operations
- **Performance**: Improved performance and developer experience
- **Interview Tip**: Mention that React 19 continues React 18's concurrent rendering improvements

---

## 58) What are React Server Components (RSC) and how do they work?

React Server Components render on the server and send zero JavaScript to the client. They reduce bundle size and improve performance.

```jsx
// Server Component (no 'use client')
async function BlogPost({ postId }) {
  const post = await db.posts.findById(postId);
  return <article><h1>{post.title}</h1><LikeButton postId={postId} /></article>;
}

// Client Component ('use client' required)
'use client';
function LikeButton({ postId }) {
  const [likes, setLikes] = useState(0);
  return <button onClick={() => setLikes(likes + 1)}>Like ({likes})</button>;
}
```

- **Core Concept**: Server Components render on server, send HTML not JavaScript, reducing bundle size
- **Real-World Benefit**: Can access databases directly, no API routes needed, smaller client bundles
- **Limitations**: Can't use hooks, browser APIs, or event handlers - use Client Components for interactivity
- **Framework Requirement**: Needs Next.js App Router, Remix, or similar - not available in plain React
- **Interview Tip**: Explain that RSC is a paradigm shift enabling server-side rendering with React components

---
