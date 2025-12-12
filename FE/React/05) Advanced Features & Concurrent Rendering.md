# 🆕 5. Advanced Features & Concurrent Rendering (Q60–66)

---

## 📍 Navigation

<div align="center">

[← Previous: Data Fetching & Server State](04%29%20Data Fetching%20%26%20Server State.md) • [Home: README](../README.md) • [Next: Performance & Optimization →](06%29%20Performance%20%26%20Optimization.md)

[📋 Cheatsheet](React%20Interview%20Cheatsheet.md)

</div>

---

---

## Q60. 💡 Concurrent Rendering in React 18

Concurrent Rendering allows React to interrupt rendering work to handle urgent updates - it keeps UI responsive during heavy operations by prioritizing user interactions over background work. React can pause and resume rendering work based on priority.

- **Trade-offs**: The catch is higher priority updates interrupt lower priority ones automatically - existing code works without changes, new features are opt-in. Concurrent rendering enables React 18+ features like Suspense and Transitions, but watch out - UI stays responsive during expensive operations like filtering large lists.

Example:

```jsx
// useTransition: marks state updates as non-urgent (can be interrupted)
const [isPending, startTransition] = useTransition(); // isPending: true during transition
const [results, setResults] = useState([]);

// Wrap expensive operation in startTransition
const onSearch = (q) =>
  startTransition(() => setResults(bigList.filter(item => item.includes(q)))); // Non-urgent update

return (
  <button onClick={() => onSearch(query)}>
    {isPending ? 'Searching...' : 'Search'} {/* Show pending state during transition */}
  </button>
);

```

## Q61. 🔧 Suspense and how to use it

Suspense allows components to wait for something before rendering - use it for loading states with lazy components or data fetching, replacing manual loading state management. Suspense declaratively handles loading states for async operations.

- **Trade-offs**: The catch is can have multiple Suspense boundaries for granular loading states - combine with Error Boundaries for complete async error handling. Suspense replaces loading state management with declarative boundaries, but watch out - good for code splitting with lazy(), data fetching with React Query, or any async component.

Example:

```jsx
// lazy(): code-split component, loads only when needed
const LazyComponent = lazy(() => import('./LazyComponent')); // Dynamic import

function App() {
  return (
    // Suspense: shows fallback while lazy component loads
    <Suspense fallback={<div>Loading...</div>}>
      <LazyComponent /> {/* Component loads asynchronously */}
    </Suspense>
  );
}

```

---

## Q62. 💡 Transitions in React 18

Transitions mark state updates as non-urgent - React keeps UI responsive by interrupting heavy work to handle user input, prioritizing interactions over background updates. Transitions mark updates that can be interrupted, keeping urgent updates responsive.

- **Trade-offs**: The catch is useDeferredValue defers value updates to show stale data while computing fresh data - prevents UI freezing during expensive operations. Transitions prioritize user interactions over background work, but watch out - good for search results, filtering, or any heavy computation triggered by user input.

Example:

```jsx
const [isPending, startTransition] = useTransition(); // Track transition state
const [input, setInput] = useState(''); // Urgent: input updates immediately
const [list, setList] = useState([]); // Non-urgent: can be deferred
const deferredInput = useDeferredValue(input); // Deferred value: shows stale value during updates

const update = (value) => {
  setInput(value); // Urgent update: input responds immediately
  startTransition(() => setList(new Array(5000).fill(value))); // Non-urgent: can be interrupted
};

return (
  <div>
    <input value={input} onChange={e => update(e.target.value)} /> {/* Always responsive */}
    {isPending ? 'Updating…' : // Show pending state
     list.slice(0,5).map((_, i) => <div key={i}>{deferredInput}</div>)} {/* Use deferred value */}
  </div>
);

```

---

## Q63. 🤔 Strict Mode and why it's important

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

## Q64. 💡 New features in React 19

React 19 introduces Actions for forms, Resource API with use() hook, useOptimistic for optimistic updates, ref as prop, document metadata support, and enhanced Suspense - it builds on React 18's concurrent rendering with better developer experience and performance optimizations. React 19 focuses on simplifying common patterns like form handling and data fetching.

- **Trade-offs**: The catch is React 19 requires React 18+ features as foundation - Actions replace manual form state management, use() hook simplifies promise handling with Suspense. React 19 reduces boilerplate significantly, but watch out - some features like Server Components require Next.js or similar frameworks, not available in plain React.

Example:

```jsx
// React 19 introduces multiple new features
import { use, useActionState, useOptimistic } from 'react';

// 1. Actions with useActionState
function ContactForm() {
  const [state, formAction, isPending] = useActionState(async (prevState, formData) => {
    const result = await submitForm(formData);
    return { message: result.message };
  }, null);

  return (
    <form action={formAction}>
      <input name="email" />
      <button disabled={isPending}>Submit</button>
      {state?.message && <p>{state.message}</p>}
    </form>
  );
}

// 2. use() hook for promises
function UserProfile({ userPromise }) {
  const user = use(userPromise);
  return <div>{user.name}</div>;
}

// 3. useOptimistic for instant UI updates
function TodoList({ todos }) {
  const [optimisticTodos, addOptimistic] = useOptimistic(
    todos,
    (state, newTodo) => [...state, { ...newTodo, pending: true }]
  );
  return optimisticTodos.map(todo => <Todo key={todo.id} {...todo} />);
}

```

---

## Q65. 🔌 React 19 Actions and Resource API

React 19 Actions provide built-in form handling with useActionState() managing form state and pending status automatically, while useFormStatus() gives child components access to form submission status. The use() hook (Resource API) unwraps promises and context values directly in render, integrating with Suspense for automatic loading states - Actions simplify form handling, use() simplifies data fetching.

- **Trade-offs**: The catch is useActionState replaces useFormState and works with native form actions - automatically handles pending states, errors, and form data serialization. The use() hook must be called unconditionally and works with Suspense boundaries - throws promise to Suspense during loading, unwraps value when resolved. Actions and Resource API simplify common patterns significantly, but watch out - useFormStatus only works inside form elements, use() can't be called conditionally, must be wrapped in Suspense for loading states.

Example:

```jsx
import { useActionState, useFormStatus, use, Suspense } from 'react';

// Actions: useActionState and useFormStatus
async function submitContact(prevState, formData) {
  const email = formData.get('email');
  try {
    await fetch('/api/contact', { method: 'POST', body: JSON.stringify({ email }) });
    return { success: true, message: 'Message sent!' };
  } catch (error) {
    return { success: false, message: 'Failed to send message' };
  }
}

function ContactForm() {
  const [state, formAction, isPending] = useActionState(submitContact, null);
  return (
    <form action={formAction}>
      <input name="email" type="email" required />
      <SubmitButton />
      {state?.message && <p>{state.message}</p>}
    </form>
  );
}

function SubmitButton() {
  const { pending } = useFormStatus(); // Access form status from parent
  return <button type="submit" disabled={pending}>{pending ? 'Sending...' : 'Send'}</button>;
}

// Resource API: use() hook for promises and context
function UserProfile({ userPromise }) {
  const user = use(userPromise); // Unwraps promise, integrates with Suspense
  return <div><h1>{user.name}</h1><p>{user.email}</p></div>;
}

function App() {
  const userPromise = fetch('/api/user').then(res => res.json());
  return (
    <Suspense fallback={<div>Loading...</div>}>
      <UserProfile userPromise={userPromise} />
    </Suspense>
  );
}

```

---

## Q66. 🧩 React Server Components (RSC) and how they work

React Server Components render on the server and send zero JavaScript to the client - they reduce bundle size and improve performance by keeping heavy logic on the server. Server Components render on server, send HTML not JavaScript, reducing bundle size.

- **Trade-offs**: The catch is can't use hooks, browser APIs, or event handlers - use Client Components for interactivity, needs Next.js App Router, Remix, or similar, not available in plain React. RSC is a paradigm shift enabling server-side rendering with React components, but watch out - can access databases directly, no API routes needed, smaller client bundles.

Example:

```jsx
// Server Component (no 'use client')
async function BlogPost({ postId }) {
  const post = await db.posts.findById(postId); // Direct database access
  return (
    <article>
      <h1>{post.title}</h1>
      <LikeButton postId={postId} /> {/* Client Component for interactivity */}
    </article>
  );
}

// Client Component ('use client' required for interactivity)
'use client';
function LikeButton({ postId }) {
  const [likes, setLikes] = useState(0); // Can use hooks
  return <button onClick={() => setLikes(likes + 1)}>Like ({likes})</button>;
}

```

---

## React Version Major Features Summary

### React 16 (2017) - "Fiber" Release

**Major Features:**

- **Fiber Architecture**: Complete rewrite of React's reconciliation algorithm for better performance

- **Error Boundaries**: `componentDidCatch()` and `static getDerivedStateFromError()` for error handling

- **Portals**: `ReactDOM.createPortal()` for rendering children outside DOM hierarchy

- **Fragments**: `<>...</>` or `<React.Fragment>` to group elements without wrapper divs

- **Return Arrays and Strings**: Components can return arrays and strings directly

- **Better Server-Side Rendering**: Improved SSR performance and hydration

- **New Context API**: `React.createContext()` for better prop drilling solution

- **Lifecycle Methods**: New `getDerivedStateFromProps()` and `getSnapshotBeforeUpdate()`

- **Pointer Events**: Support for pointer events API

- **Profiler Component**: React DevTools Profiler for performance analysis

**Breaking Changes:**

- `componentWillMount`, `componentWillReceiveProps`, `componentWillUpdate` deprecated (removed in React 17)

---

### React 17 (2020) - "No New Features" Release

**Major Features:**

- **New JSX Transform**: No need to import React in every file using JSX

- **Event Delegation Changes**: Events attached to root instead of document

- **Effect Cleanup Timing**: Effects cleanup runs asynchronously after paint

- **Removed Event Pooling**: Synthetic events no longer pooled (performance improvement)

- **Consistent Errors**: Better error messages for undefined components

- **Native Component Stack**: Better stack traces in error messages

- **Lazy Loading Improvements**: Better support for Suspense with code splitting

**Key Focus:**

- **Gradual Upgrades**: Designed to enable gradual React upgrades (multiple versions in one app)

- **No Breaking Changes**: Focused on making future upgrades easier

---

### React 18 (2022) - "Concurrent React" Release

**Major Features:**

- **Concurrent Rendering**: Interruptible rendering for better responsiveness

- **Automatic Batching**: Automatic batching of state updates (including in promises, timeouts, native handlers)

- **Transitions**: `useTransition()` and `startTransition()` for non-urgent updates

- **Suspense Improvements**: Full support for Suspense in data fetching (not just code splitting)

- **New Hooks**:
  - `useTransition()`: Mark updates as non-urgent
  - `useDeferredValue()`: Defer expensive value updates
  - `useId()`: Generate unique IDs for accessibility
  - `useSyncExternalStore()`: Subscribe to external stores
  - `useInsertionEffect()`: For CSS-in-JS libraries

- **New Root API**: `createRoot()` replaces `ReactDOM.render()`

- **Strict Mode**: Double-invokes effects in development to catch bugs

- **Server Components Support**: Foundation for React Server Components (Next.js 13+)

- **Improved Hydration**: Better error messages for hydration mismatches

**Breaking Changes:**

- `ReactDOM.render()` deprecated in favor of `createRoot()`

- `ReactDOM.hydrate()` deprecated in favor of `hydrateRoot()`

---

### React 19 (2024) - "Actions & Resources" Release

**Major Features:**

- **Actions**: Built-in form handling with `useActionState()` and `useFormStatus()` for async form submissions

- **Resource API**: New `use()` hook for data fetching with automatic Suspense integration

- **useOptimistic Hook**: Optimistic UI updates for instant feedback on async operations

- **Enhanced Suspense**: Better error boundaries and loading states with improved error handling

- **Document Metadata**: Built-in support for `<title>`, `<meta>`, `<link>` tags that auto-hoist to document head

- **Ref as a Prop**: Can pass refs as regular props without `forwardRef()` wrapper

- **Context as a Provider**: Context can be used directly as a provider component (`<Context value="..." />`)

- **Improved Hydration**: Better hydration performance and clearer error messages

- **Compiler Optimizations**: React Compiler (experimental) for automatic memoization and optimization

- **Better TypeScript Support**: Improved type inference and error messages for new hooks

- **Web Components Support**: Better integration with Web Components and custom elements

**New Hooks:**

- `use()`: Unwrap promises and context values with Suspense integration

- `useActionState()`: Manage form actions with automatic pending states and error handling

- `useFormStatus()`: Access form submission status from child components

- `useOptimistic()`: Manage optimistic UI updates for better perceived performance

**Key Focus:**

- **Better DX**: Improved developer experience with built-in form handling and less boilerplate

- **Performance**: React Compiler for automatic optimizations, better hydration performance

- **Simplified APIs**: Less boilerplate for common patterns like forms, refs, and context

- **Modern Patterns**: Better support for Server Components, async operations, and modern web standards

**Breaking Changes:**

- `useFormState` renamed to `useActionState`

- Some deprecated lifecycle methods removed

- Improved error messages for common mistakes

---

---

## 📍 Navigation

<div align="center">

[← Previous: Data Fetching & Server State](04%29%20Data Fetching%20%26%20Server State.md) • [Home: README](../README.md) • [Next: Performance & Optimization →](06%29%20Performance%20%26%20Optimization.md)

[📋 Cheatsheet](React%20Interview%20Cheatsheet.md)

</div>

---
