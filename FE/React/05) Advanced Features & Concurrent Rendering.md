# 🆕 5. Advanced Features & Concurrent Rendering (Q60–66)

---

## 📍 Navigation

<div align="center">

[← Previous: Data Fetching & Server State](04%29%20Data%20Fetching%20%26%20Server%20State.md) • [Home: README](../README.md) • [Next: Performance & Optimization →](06%29%20Performance%20%26%20Optimization.md)

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

### React 15 (April 2016) - "Performance & Developer Experience" Release

**Major Features:**

- **Performance Enhancements**: Significant improvements in rendering efficiency and update performance
  - Reduced reconciliation overhead
  - Faster component updates
  - Better memory management

- **Improved Error Messages**: Enhanced developer experience with clearer, more actionable error messages
  - Better stack traces
  - Component tree information in errors
  - Helpful suggestions for common mistakes

- **Stateless Functional Components**: Support for simpler components without state or lifecycle methods

  ```jsx
  // Before: Required class components
  class Welcome extends React.Component {
    render() {
      return <h1>Hello, {this.props.name}</h1>;
    }
  }

  // After: Functional components
  function Welcome({ name }) {
    return <h1>Hello, {name}</h1>;
  }
  ```

- **Improved DOM Rendering**: Better handling of DOM nodes and attributes
  - Support for custom attributes
  - Better SVG support
  - Improved handling of data attributes

- **React Perf Addon**: Performance measurement tools for identifying bottlenecks

**Key Focus:**

- Foundation for modern React patterns
- Improved performance baseline
- Better developer tooling

---

### React 16 (September 2017) - "Fiber" Release

**Major Features:**

- **Fiber Architecture**: Complete rewrite of React's reconciliation algorithm
  - **Incremental Rendering**: Ability to split rendering work into chunks and spread it over multiple frames
  - **Priority-based Updates**: Can prioritize certain updates (like user input) over others
  - **Interruptible Rendering**: Can pause, abort, or reuse work as new updates come in
  - **Better Error Handling**: Improved error recovery and boundaries
  - **Performance**: Up to 2x faster rendering in some scenarios

  ```jsx
  // Fiber enables concurrent rendering (fully enabled in React 18)
  // Components can be paused and resumed during rendering
  ```

- **Error Boundaries**: Components that catch JavaScript errors anywhere in child component tree

  ```jsx
  class ErrorBoundary extends React.Component {
    constructor(props) {
      super(props);
      this.state = { hasError: false };
    }

    static getDerivedStateFromError(error) {
      return { hasError: true };
    }

    componentDidCatch(error, errorInfo) {
      console.error('Error caught:', error, errorInfo);
    }

    render() {
      if (this.state.hasError) {
        return <h1>Something went wrong.</h1>;
      }
      return this.props.children;
    }
  }
  ```

- **Portals**: Render children into a DOM node outside parent hierarchy

  ```jsx
  // Useful for modals, tooltips, popovers
  function Modal({ children }) {
    return ReactDOM.createPortal(
      children,
      document.body
    );
  }
  ```

- **Fragments**: Group multiple elements without adding extra DOM nodes

  ```jsx
  // Before: Required wrapper div
  return (
    <div>
      <ChildA />
      <ChildB />
    </div>
  );

  // After: No wrapper needed
  return (
    <>
      <ChildA />
      <ChildB />
    </>
  );
  ```

- **Return Arrays and Strings**: Components can return arrays and strings directly

  ```jsx
  function List() {
    return [
      <li key="1">Item 1</li>,
      <li key="2">Item 2</li>
    ];
  }

  function Greeting() {
    return 'Hello, World!';
  }
  ```

- **Better Server-Side Rendering**: Improved SSR performance and hydration
  - Faster initial render
  - Better hydration performance
  - Improved error handling during SSR
  - Support for streaming SSR (foundation)

- **New Context API**: Modern Context API replacing legacy context

  ```jsx
  // Create context
  const ThemeContext = React.createContext('light');

  // Provide value
  <ThemeContext.Provider value="dark">
    <App />
  </ThemeContext.Provider>

  // Consume value
  const theme = useContext(ThemeContext);
  ```

- **Lifecycle Methods**: New lifecycle methods for better control
  - `getDerivedStateFromProps()`: Called before every render, for state updates based on props
  - `getSnapshotBeforeUpdate()`: Called right before DOM updates, for capturing scroll position, etc.

  ```jsx
  class ScrollList extends React.Component {
    getSnapshotBeforeUpdate(prevProps, prevState) {
      if (prevProps.list.length < this.props.list.length) {
        const list = this.listRef.current;
        return list.scrollHeight - list.scrollTop;
      }
      return null;
    }

    componentDidUpdate(prevProps, prevState, snapshot) {
      if (snapshot !== null) {
        const list = this.listRef.current;
        list.scrollTop = list.scrollHeight - snapshot;
      }
    }
  }
  ```

- **Pointer Events**: Support for pointer events API (unified mouse, touch, pen events)

- **Profiler Component**: React DevTools Profiler for performance analysis

  ```jsx
  <Profiler id="App" onRender={onRenderCallback}>
    <App />
  </Profiler>
  ```

- **Reduced Bundle Size**: Smaller core library size despite new features

**Breaking Changes:**

- `componentWillMount`, `componentWillReceiveProps`, `componentWillUpdate` deprecated (removed in React 17)
- `ReactDOM.render()` return value changed (now returns null for stateless components)
- Error boundaries catch errors in more places (including event handlers)
- `setState(null)` no longer triggers an update
- `setState` callback fires immediately after state is applied (not after commit)

**Migration Notes:**

- Most code works without changes
- Update lifecycle methods if using deprecated ones
- Error boundaries recommended for better error handling

---

### React 17 (October 2020) - "No New Features" Release

**Major Features:**

- **New JSX Transform**: Automatic JSX runtime eliminates need to import React

  ```jsx
  // Before: Required React import
  import React from 'react';
  function App() {
    return <h1>Hello</h1>;
  }

  // After: No import needed (automatic)
  function App() {
    return <h1>Hello</h1>;
  }

  // Behind the scenes: Automatically uses new jsx() function
  // import { jsx as _jsx } from 'react/jsx-runtime';
  ```

  - **Benefits**: Smaller bundle size, cleaner code, better performance
  - **Backward Compatible**: Old transform still works

- **Event Delegation Changes**: Events now attach to root container instead of document

  ```jsx
  // Before: Events attached to document
  // document.addEventListener('click', ...)

  // After: Events attached to root
  // rootContainer.addEventListener('click', ...)
  ```

  - **Benefits**:
    - Enables gradual React upgrades (multiple versions can coexist)
    - Better isolation between React trees
    - Easier to embed React in other frameworks
  - **No Behavior Changes**: Event bubbling works the same for developers

- **Effect Cleanup Timing**: Effects cleanup runs asynchronously after paint

  ```jsx
  useEffect(() => {
    // Setup
    return () => {
      // Cleanup now runs asynchronously after paint
      // Better for performance, UI updates aren't blocked
    };
  });
  ```

  - **Benefits**: Better performance, smoother UI updates
  - **Timing**: Cleanup runs after browser has painted the screen

- **Removed Event Pooling**: Synthetic events no longer pooled

  ```jsx
  // Before: Events were pooled, couldn't access after async
  function handleClick(e) {
    setTimeout(() => {
      console.log(e.type); // Error: SyntheticEvent was pooled
    }, 100);
  }

  // After: Events persist, can access anytime
  function handleClick(e) {
    setTimeout(() => {
      console.log(e.type); // Works! Event persists
    }, 100);
  }
  ```

  - **Benefits**: More intuitive behavior, better performance
  - **Migration**: Most code works without changes, some edge cases fixed

- **Consistent Errors**: Better error messages for undefined components

  ```jsx
  // Before: Cryptic error messages
  // After: Clear error: "Element type is invalid: expected a string..."
  ```

- **Native Component Stack**: Better stack traces in error messages
  - Shows actual component names in stack traces
  - Easier debugging in production
  - Better integration with browser DevTools

- **Lazy Loading Improvements**: Better support for Suspense with code splitting

  ```jsx
  const LazyComponent = React.lazy(() => import('./Component'));

  function App() {
    return (
      <Suspense fallback={<div>Loading...</div>}>
        <LazyComponent />
      </Suspense>
    );
  }
  ```

  - More reliable Suspense behavior
  - Better error handling for lazy components

- **useEffect Cleanup**: Improved cleanup function behavior
  - Cleanup functions can be async
  - Better handling of cleanup timing

- **Strict Mode**: Enhanced Strict Mode warnings
  - Warns about unsafe lifecycle methods
  - Warns about legacy string refs
  - Warns about deprecated findDOMNode usage

**Key Focus:**

- **Gradual Upgrades**: Designed to enable gradual React upgrades
  - Multiple React versions can coexist on the same page
  - Easier migration path for large codebases
  - Foundation for future React features

- **No Breaking Changes**: Focused on making future upgrades easier
  - All existing code continues to work
  - Smooth upgrade path to React 18
  - Better foundation for concurrent features

- **Developer Experience**: Improved tooling and error messages
  - Better debugging experience
  - Clearer error messages
  - Improved DevTools integration

**Migration Notes:**

- Drop-in replacement for React 16
- Update JSX transform for smaller bundles (optional)
- No code changes required for most apps

---

### React 18 (March 2022) - "Concurrent React" Release

**Major Features:**

- **Concurrent Rendering**: Interruptible rendering for better responsiveness
  - **What it is**: React can interrupt, pause, resume, or abandon work
  - **Benefits**: UI stays responsive during heavy rendering work
  - **How it works**: React prepares multiple versions of UI simultaneously, prioritizing urgent updates

  ```jsx
  // React can interrupt heavy rendering to handle urgent updates
  // User clicks button → React pauses list rendering → Updates button → Resumes list
  ```

  - **Opt-in**: Most features are opt-in, existing code works without changes
  - **Foundation**: Enables Suspense, Transitions, and other concurrent features

- **Automatic Batching**: Automatic batching of state updates

  ```jsx
  // Before: Only batched in React event handlers
  function handleClick() {
    setCount(c => c + 1); // Batched
    setFlag(f => !f);     // Batched
  }

  // After: Batched everywhere (promises, timeouts, native handlers)
  function handleClick() {
    setTimeout(() => {
      setCount(c => c + 1); // Now batched!
      setFlag(f => !f);     // Now batched!
      // Only one re-render instead of two
    }, 1000);
  }

  fetch('/api').then(() => {
    setCount(c => c + 1); // Batched!
    setFlag(f => !f);     // Batched!
  });
  ```

  - **Benefits**: Fewer re-renders, better performance
  - **Automatic**: Works by default, no code changes needed
  - **Opt-out**: Use `flushSync()` to opt-out if needed

- **Transitions**: Mark updates as non-urgent to keep UI responsive

  ```jsx
  import { useTransition, startTransition } from 'react';

  function SearchResults() {
    const [isPending, startTransition] = useTransition();
    const [input, setInput] = useState('');
    const [results, setResults] = useState([]);

    const handleSearch = (value) => {
      setInput(value); // Urgent: input updates immediately
      startTransition(() => {
        // Non-urgent: can be interrupted
        setResults(expensiveFilter(value));
      });
    };

    return (
      <>
        <input value={input} onChange={e => handleSearch(e.target.value)} />
        {isPending && <Spinner />}
        <ResultsList results={results} />
      </>
    );
  }
  ```

  - **Use cases**: Search, filtering, tab switching
  - **Benefits**: Input stays responsive during heavy operations
  - **Visual feedback**: `isPending` flag for loading states

- **Deferred Values**: Defer expensive value updates

  ```jsx
  import { useDeferredValue } from 'react';

  function ProductList({ products }) {
    const deferredProducts = useDeferredValue(products);
    // Shows stale value while new value is computing
    // Automatically updates when ready

    return (
      <ul>
        {deferredProducts.map(product => (
          <li key={product.id}>{product.name}</li>
        ))}
      </ul>
    );
  }
  ```

  - **Use cases**: Expensive filtering, sorting, transformations
  - **Benefits**: UI shows stale data immediately, updates when ready
  - **Works with**: Transitions and Suspense

- **Suspense Improvements**: Full support for Suspense in data fetching

  ```jsx
  // Before: Only worked with React.lazy()
  // After: Works with any async operation

  function ProfilePage() {
    return (
      <Suspense fallback={<ProfileSkeleton />}>
        <ProfileDetails />
        <Suspense fallback={<PostsSkeleton />}>
          <ProfilePosts />
        </Suspense>
      </Suspense>
    );
  }

  // Works with libraries like React Query, SWR, Relay
  function ProfileDetails() {
    const { data } = useQuery('profile', fetchProfile);
    return <div>{data.name}</div>;
  }
  ```

  - **Benefits**: Declarative loading states, better UX
  - **Nested Suspense**: Multiple Suspense boundaries for granular loading
  - **Error Boundaries**: Combine with Error Boundaries for complete async handling

- **New Hooks**:

  - **`useTransition()`**: Mark updates as non-urgent

    ```jsx
    const [isPending, startTransition] = useTransition();
    ```

  - **`useDeferredValue()`**: Defer expensive value updates

    ```jsx
    const deferredValue = useDeferredValue(value);
    ```

  - **`useId()`**: Generate unique IDs for accessibility

    ```jsx
    function Checkbox() {
      const id = useId(); // Stable across renders, unique per instance
      return (
        <>
          <input id={id} type="checkbox" />
          <label htmlFor={id}>Check me</label>
        </>
      );
    }
    ```

    - **Benefits**: Stable IDs for SSR, no hydration mismatches
    - **Use cases**: Form labels, ARIA attributes

  - **`useSyncExternalStore()`**: Subscribe to external stores

    ```jsx
    import { useSyncExternalStore } from 'react';

    function useStore(store) {
      return useSyncExternalStore(
        store.subscribe,
        store.getSnapshot
      );
    }
    ```

    - **Benefits**: Proper concurrent rendering support for external stores
    - **Use cases**: Redux, Zustand, other state management libraries

  - **`useInsertionEffect()`**: For CSS-in-JS libraries

    ```jsx
    import { useInsertionEffect } from 'react';

    function useCSS(rule) {
      useInsertionEffect(() => {
        // Inject styles before DOM mutations
        const style = document.createElement('style');
        style.textContent = rule;
        document.head.appendChild(style);
        return () => style.remove();
      });
    }
    ```

    - **Benefits**: Prevents visual glitches during rendering
    - **Use cases**: styled-components, emotion, other CSS-in-JS libraries

- **New Root API**: `createRoot()` replaces `ReactDOM.render()`

  ```jsx
  // Before: ReactDOM.render()
  import ReactDOM from 'react-dom';
  ReactDOM.render(<App />, document.getElementById('root'));

  // After: createRoot()
  import { createRoot } from 'react-dom/client';
  const root = createRoot(document.getElementById('root'));
  root.render(<App />);

  // Benefits:
  // - Enables concurrent features
  // - Better error handling
  // - Cleaner API
  // - Supports concurrent rendering
  ```

  - **Hydration**: `hydrateRoot()` for SSR

  ```jsx
  import { hydrateRoot } from 'react-dom/client';
  hydrateRoot(document.getElementById('root'), <App />);
  ```

- **Strict Mode**: Double-invokes effects in development

  ```jsx
  useEffect(() => {
    console.log('Effect runs'); // Logs twice in development
    return () => console.log('Cleanup runs'); // Also runs twice
  });
  ```

  - **Purpose**: Catch bugs that might only appear in production
  - **Development only**: No impact on production builds
  - **Helps find**: Side effects in render, missing cleanup, etc.

- **Server Components Support**: Foundation for React Server Components
  - **Next.js 13+**: Full RSC support in Next.js App Router
  - **Benefits**: Smaller bundles, faster loads, direct database access
  - **Foundation**: React 18 provides the core infrastructure

- **Improved Hydration**: Better error messages for hydration mismatches

  ```jsx
  // Before: Cryptic hydration errors
  // After: Clear messages showing exactly what mismatched
  // "Hydration failed because the server rendered HTML didn't match the client..."
  ```

  - **Better debugging**: Shows component tree, attribute differences
  - **Suppression**: `suppressHydrationWarning` for intentional differences

- **New Suspense Features**:
  - **Streaming SSR**: Server can stream HTML as components render
  - **Selective Hydration**: Hydrate components as they become ready
  - **Better Error Handling**: Improved error boundaries with Suspense

**Breaking Changes:**

- **`ReactDOM.render()` deprecated**: Use `createRoot()` instead

  ```jsx
  // Old API still works but shows deprecation warning
  ReactDOM.render(<App />, container); // ⚠️ Deprecated
  ```

- **`ReactDOM.hydrate()` deprecated**: Use `hydrateRoot()` instead

- **TypeScript Types**: Some type definitions changed
  - `React.FC` children prop removed by default
  - Better type inference for hooks

- **Automatic Batching**: May change behavior of some edge cases
  - Most apps benefit automatically
  - Use `flushSync()` if you need immediate updates

**Migration Notes:**

- Update root API: `ReactDOM.render()` → `createRoot()`
- Most code works without changes
- Opt-in to concurrent features gradually
- Update TypeScript types if using TypeScript
- Test thoroughly, especially with external state management

---

### React 19 (December 2024) - "Actions & Resources" Release

**Major Features:**

- **Actions**: Built-in form handling with automatic state management

  ```jsx
  import { useActionState, useFormStatus } from 'react';

  // Server Action (or async function)
  async function submitForm(prevState, formData) {
    const email = formData.get('email');
    const result = await saveToDatabase(email);
    if (result.error) {
      return { error: result.error };
    }
    return { success: true, message: 'Saved!' };
  }

  function ContactForm() {
    const [state, formAction, isPending] = useActionState(submitForm, null);

    return (
      <form action={formAction}>
        <input name="email" type="email" />
        <SubmitButton />
        {state?.error && <p className="error">{state.error}</p>}
        {state?.success && <p className="success">{state.message}</p>}
      </form>
    );
  }

  function SubmitButton() {
    const { pending } = useFormStatus(); // Access form status from parent
    return (
      <button type="submit" disabled={pending}>
        {pending ? 'Submitting...' : 'Submit'}
      </button>
    );
  }
  ```

  - **Benefits**:
    - Automatic pending state management
    - Built-in error handling
    - Works with native form actions
    - Progressive enhancement support
  - **Use cases**: Contact forms, search forms, any form with async submission
  - **Progressive Enhancement**: Works without JavaScript (falls back to native form submission)

- **Resource API**: New `use()` hook for data fetching with Suspense integration

  ```jsx
  import { use, Suspense } from 'react';

  // Works with promises
  function UserProfile({ userPromise }) {
    const user = use(userPromise); // Unwraps promise, throws to Suspense if pending
    return (
      <div>
        <h1>{user.name}</h1>
        <p>{user.email}</p>
      </div>
    );
  }

  // Works with Context
  const ThemeContext = createContext();
  function ThemedButton() {
    const theme = use(ThemeContext); // Can use context without Provider wrapper
    return <button className={theme}>Click me</button>;
  }

  // Usage with Suspense
  function App() {
    const userPromise = fetch('/api/user').then(r => r.json());
    return (
      <Suspense fallback={<div>Loading user...</div>}>
        <UserProfile userPromise={userPromise} />
      </Suspense>
    );
  }
  ```

  - **Benefits**:
    - Simplifies promise handling
    - Automatic Suspense integration
    - Works with any promise-returning function
    - Can use context conditionally
  - **Rules**: Must be called unconditionally, can't be called conditionally
  - **Use cases**: Data fetching, context consumption, any async resource

- **useOptimistic Hook**: Optimistic UI updates for instant feedback

  ```jsx
  import { useOptimistic } from 'react';

  function TodoList({ todos }) {
    const [optimisticTodos, addOptimistic] = useOptimistic(
      todos,
      (state, newTodo) => [...state, { ...newTodo, pending: true }]
    );

    async function addTodo(formData) {
      const newTodo = { id: Date.now(), text: formData.get('text') };
      addOptimistic(newTodo); // UI updates immediately
      await saveTodo(newTodo); // Save to server
      // UI automatically syncs when server responds
    }

    return (
      <ul>
        {optimisticTodos.map(todo => (
          <li key={todo.id}>
            {todo.text}
            {todo.pending && <span> (saving...)</span>}
          </li>
        ))}
      </ul>
    );
  }
  ```

  - **Benefits**: Instant UI feedback, better perceived performance
  - **Use cases**: Likes, comments, todos, any optimistic update pattern
  - **Automatic Rollback**: If server request fails, state automatically reverts

- **Enhanced Suspense**: Better error boundaries and loading states

  ```jsx
  // Better error handling with Suspense
  <ErrorBoundary fallback={<ErrorUI />}>
    <Suspense fallback={<LoadingUI />}>
      <AsyncComponent />
    </Suspense>
  </ErrorBoundary>

  // Improved error messages
  // Clear indication of what failed and where
  ```

  - **Benefits**: Better error messages, clearer loading states
  - **Combines with**: Error Boundaries for complete async handling

- **Document Metadata**: Built-in support for metadata tags

  ```jsx
  // Before: Required libraries like react-helmet
  // After: Native support

  function BlogPost({ post }) {
    return (
      <>
        <title>{post.title}</title>
        <meta name="description" content={post.excerpt} />
        <meta property="og:title" content={post.title} />
        <link rel="canonical" href={post.url} />
        <article>
          <h1>{post.title}</h1>
          <p>{post.content}</p>
        </article>
      </>
    );
  }

  // Tags automatically hoist to <head>
  // Works with Server Components
  // Supports all standard metadata tags
  ```

  - **Benefits**:
    - No need for react-helmet or similar libraries
    - Works with Server Components
    - Automatic hoisting to document head
    - Better SEO support
  - **Supported tags**: `<title>`, `<meta>`, `<link>`, `<script>`, `<style>`

- **Ref as a Prop**: Pass refs as regular props without `forwardRef()`

  ```jsx
  // Before: Required forwardRef
  const Input = forwardRef((props, ref) => {
    return <input {...props} ref={ref} />;
  });

  // After: Just use ref prop directly
  function Input({ ref, ...props }) {
    return <input {...props} ref={ref} />;
  }

  // Usage stays the same
  <Input ref={inputRef} />
  ```

  - **Benefits**: Less boilerplate, simpler component code
  - **Backward Compatible**: `forwardRef()` still works

- **Context as a Provider**: Context can be used directly as provider

  ```jsx
  const ThemeContext = createContext('light');

  // Before: Required separate Provider component
  <ThemeContext.Provider value="dark">
    <App />
  </ThemeContext.Provider>

  // After: Use Context directly
  <ThemeContext value="dark">
    <App />
  </ThemeContext>
  ```

  - **Benefits**: Cleaner syntax, less boilerplate
  - **Backward Compatible**: `.Provider` still works

- **Improved Hydration**: Better performance and error messages

  ```jsx
  // Faster hydration performance
  // Better error messages for mismatches
  // Clearer debugging information
  ```

  - **Performance**: Up to 30% faster hydration in some cases
  - **Error Messages**: Shows exactly what mismatched and where

- **Compiler Optimizations**: React Compiler (experimental) for automatic optimizations

  ```jsx
  // React Compiler automatically:
  // - Memoizes components (like React.memo)
  // - Memoizes values (like useMemo)
  // - Memoizes callbacks (like useCallback)
  // - Optimizes re-renders

  // Before: Manual optimization
  const MemoizedComponent = React.memo(Component);
  const memoizedValue = useMemo(() => expensive(), [deps]);
  const memoizedCallback = useCallback(() => {}, [deps]);

  // After: Automatic (with compiler)
  // Just write normal code, compiler optimizes it
  ```

  - **Status**: Experimental, opt-in
  - **Benefits**: Automatic optimizations, less boilerplate
  - **Future**: May become default in future versions

- **Better TypeScript Support**: Improved type inference

  ```tsx
  // Better type inference for hooks
  // Improved error messages
  // Better support for new features
  ```

- **Web Components Support**: Better integration with Web Components

  ```jsx
  // Better support for custom elements
  // Improved event handling
  // Better attribute handling
  ```

- **New Suspense Features**:
  - **Suspense for Images**: Built-in support for image loading

  ```jsx
  <Suspense fallback={<ImageSkeleton />}>
    <img src="/large-image.jpg" />
  </Suspense>
  ```

  - **Suspense for Scripts**: Support for async script loading
  - **Better Streaming**: Improved streaming SSR performance

- **Performance Improvements**:
  - Faster hydration (up to 30% improvement)
  - Better tree shaking
  - Smaller bundle sizes
  - Improved concurrent rendering performance

**New Hooks:**

- **`use()`**: Unwrap promises and context values

  ```jsx
  const value = use(promiseOrContext);
  ```

- **`useActionState()`**: Manage form actions (formerly `useFormState`)

  ```jsx
  const [state, formAction, isPending] = useActionState(action, initialState);
  ```

- **`useFormStatus()`**: Access form submission status

  ```jsx
  const { pending, data, method, action } = useFormStatus();
  ```

- **`useOptimistic()`**: Manage optimistic UI updates

  ```jsx
  const [optimisticState, addOptimistic] = useOptimistic(state, updateFn);
  ```

**Key Focus:**

- **Better DX**: Improved developer experience
  - Less boilerplate for common patterns
  - Built-in form handling
  - Simpler APIs for refs and context
  - Better error messages

- **Performance**: Automatic optimizations
  - React Compiler for automatic memoization
  - Faster hydration
  - Better concurrent rendering
  - Smaller bundles

- **Simplified APIs**: Less code for common patterns
  - Forms: Built-in action handling
  - Refs: No need for forwardRef
  - Context: Direct provider syntax
  - Metadata: Native document metadata support

- **Modern Patterns**: Better support for modern web
  - Server Components (Next.js, Remix)
  - Async operations (Actions, use() hook)
  - Progressive enhancement (form actions)
  - Web Components integration

**Breaking Changes:**

- **`useFormState` renamed to `useActionState`**

  ```jsx
  // Old: useFormState (deprecated)
  // New: useActionState
  const [state, action, pending] = useActionState(submitAction, null);
  ```

- **Some deprecated lifecycle methods removed**
  - `componentWillMount`
  - `componentWillReceiveProps`
  - `componentWillUpdate`
  - (Already removed in React 17, but some polyfills may break)

- **Improved error messages**: May surface previously hidden bugs
  - Better error detection
  - Clearer error messages
  - May require fixing previously working code

- **TypeScript changes**: Some type definitions updated
  - Better type inference
  - Some breaking type changes
  - Update TypeScript version recommended

**Migration Notes:**

- Update `useFormState` → `useActionState`
- Update form handling to use Actions API
- Consider using `use()` hook for data fetching
- Update TypeScript types if using TypeScript
- Test thoroughly, especially forms and async operations
- Consider enabling React Compiler (experimental)
- Update to latest React DevTools for best experience

---

## Quick Version Reference

| Version | Release Date | Key Theme | Major Features | Breaking Changes |
|---------|-------------|-----------|----------------|------------------|
| **React 15** | April 2016 | Performance & DX | Functional components, better errors, React Perf | Minimal |
| **React 16** | Sept 2017 | Fiber Architecture | Fiber, Error Boundaries, Portals, Fragments, Context API | Lifecycle deprecations |
| **React 17** | Oct 2020 | No New Features | New JSX transform, event delegation changes, gradual upgrades | None (smooth upgrade) |
| **React 18** | March 2022 | Concurrent React | Concurrent rendering, Automatic batching, Suspense, Transitions | New Root API (`createRoot`) |
| **React 19** | Dec 2024 | Actions & Resources | Actions, `use()` hook, `useOptimistic`, Document metadata | `useFormState` → `useActionState` |

### Version Adoption Recommendations

- **React 15**: Legacy, upgrade recommended
- **React 16**: Still supported but upgrade to 17+ recommended
- **React 17**: Stable, good for gradual upgrades, minimal changes
- **React 18**: **Recommended** - Full concurrent features, stable API
- **React 19**: **Latest** - Best DX, modern patterns, requires React 18 foundation

### Feature Timeline

- **2016**: Functional components, better errors
- **2017**: Fiber architecture, Error Boundaries, Context API
- **2020**: New JSX transform, event delegation improvements
- **2022**: Concurrent rendering, Automatic batching, Suspense for data fetching
- **2024**: Actions, Resource API, Document metadata, React Compiler

---

---

## 📍 Navigation

<div align="center">

[← Previous: Data Fetching & Server State](04%29%20Data%20Fetching%20%26%20Server%20State.md) • [Home: README](../README.md) • [Next: Performance & Optimization →](06%29%20Performance%20%26%20Optimization.md)

[📋 Cheatsheet](React%20Interview%20Cheatsheet.md)

</div>

---
