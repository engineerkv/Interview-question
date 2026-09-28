---
sidebar_label: "Cheatsheet"
sidebar_position: 100
---
# ⚛️ **React Interview Cheatsheet**

> **⏱️ Review Time: 15-20 minutes** | **Priority: ⭐⭐⭐ High** | Quick reference for React interviews

**Quick Review Checklist:**

- [ ] React Basics (Components, JSX, Props, State, Virtual DOM)

- [ ] Hooks (useState, useEffect, useRef, useMemo, useCallback)

- [ ] State Management (Context API, Redux Toolkit)

- [ ] Performance (React.memo, Code Splitting, Virtualization)

- [ ] React 18+ Features (Concurrent, Suspense, Transitions)

- [ ] Testing (React Testing Library, Custom Hooks)

- [ ] React Internals (Fiber, Reconciliation, Commit Phase)

---

## 📋 **React Basics**

| Concept | Description | Example |
|---------|-------------|---------|
| **Component** | Reusable UI piece that can be composed together | `function Button() { return <button>Click</button>; }` |
| **JSX** | HTML-like syntax compiled to React.createElement() calls | `<h1>Hello {name}</h1>` |
| **Props** | Read-only data passed from parent to child components | `<Button text="Click me" />` |
| **State** | Mutable data inside a component that triggers re-renders | `const [count, setCount] = useState(0)` |
| **Virtual DOM** | JavaScript representation of DOM for efficient diffing | React's diffing algorithm |

---

## 🪝 **React Hooks**

### **useState**

**Definition:** Hook that manages component state, returns current state value and setter function to update state and trigger re-renders.

```jsx
const [state, setState] = useState(initialValue);
const [count, setCount] = useState(0);

// Functional updates
setCount(prev => prev + 1);

// Object state
const [user, setUser] = useState({ name: '', email: '' });
setUser(prev => ({ ...prev, name: 'John' }));

```

### **useEffect**

**Definition:** Hook for side effects (API calls, subscriptions, DOM manipulation) that runs after render, with optional cleanup and dependency array.

```jsx
// Run on every render
useEffect(() => {
  console.log('Component rendered');
});

// Run once (on mount)
useEffect(() => {
  fetchData();
}, []);

// Run when dependencies change
useEffect(() => {
  fetchUser(userId);
}, [userId]);

// Cleanup
useEffect(() => {
  const timer = setInterval(() => {}, 1000);
  return () => clearInterval(timer);
}, []);

```

### **useRef**

**Definition:** Hook that returns mutable ref object persisting across renders, used for DOM access or storing values without causing re-renders.

```jsx
const inputRef = useRef();
const [count, setCount] = useState(0);
const countRef = useRef(0);

// DOM access
inputRef.current.focus();

// Mutable value (no re-render)
countRef.current += 1;

```

### **useMemo & useCallback**

**Definition:** Performance hooks: useMemo caches computed values; useCallback caches function references to prevent unnecessary re-renders of child components.

```jsx
// Memoize expensive calculations
const expensiveValue = useMemo(() => {
  return heavyCalculation(data);
}, [data]);

// Memoize callback functions
const handleClick = useCallback(() => {
  doSomething();
}, [dependency]);

```

---

## 🔄 **Component Lifecycle**

| Class Lifecycle | Hook Equivalent |
|----------------|-----------------|
| `componentDidMount` | `useEffect(() => {}, [])` |
| `componentDidUpdate` | `useEffect(() => {}, [deps])` |
| `componentWillUnmount` | `useEffect(() => { return () => {} }, [])` |

---

## 🧩 **State Management**

### **Context API**

```jsx
const ThemeContext = createContext();

function ThemeProvider({ children }) {
  const [theme, setTheme] = useState('light');
  return (
    <ThemeContext.Provider value={{ theme, setTheme }}>
      {children}
    </ThemeContext.Provider>
  );
}

function ThemedButton() {
  const { theme, setTheme } = useContext(ThemeContext);
  return <button onClick={() => setTheme('dark')}>{theme}</button>;
}

```

### **Redux Toolkit**

```jsx
import { createSlice, configureStore } from '@reduxjs/toolkit';

const counterSlice = createSlice({
  name: 'counter',
  initialState: { count: 0 },
  reducers: {
    increment: (state) => { state.count += 1; },
    decrement: (state) => { state.count -= 1; }
  }
});

const store = configureStore({
  reducer: { counter: counterSlice.reducer }
});

function Counter() {
  const count = useSelector(state => state.counter.count);
  const dispatch = useDispatch();
  return <button onClick={() => dispatch(increment())}>{count}</button>;
}

```

---

## 🌐 **Data Fetching**

### **React Query**

```jsx
import { useQuery, useMutation } from 'react-query';

function UserProfile({ userId }) {
  const { data: user, isLoading, error } = useQuery({
    queryKey: ['user', userId],
    queryFn: () => fetchUser(userId)
  });

  const updateUser = useMutation({
    mutationFn: updateUser,
    onSuccess: () => {
      queryClient.invalidateQueries(['user', userId]);
    }
  });

  if (isLoading) return <div>Loading...</div>;
  if (error) return <div>Error: {error.message}</div>;

  return <div>{user.name}</div>;
}

```

### **RTK Query**

```jsx
import { createApi, fetchBaseQuery } from '@reduxjs/toolkit/query/react';
export const api = createApi({
  baseQuery: fetchBaseQuery({ baseUrl: '/api' }),
  endpoints: (b) => ({ getUser: b.query({ query: (id) => `users/${id}` }) })
});
function Profile({ id }){
  const { data, isLoading } = api.useGetUserQuery(id);
  return isLoading ? 'Loading' : data.name;
}

```

### **Infinite Query**

```jsx
const { data, fetchNextPage, hasNextPage } = useInfiniteQuery({
  queryKey: ['posts'],
  queryFn: ({ pageParam = 1 }) => fetch(`/api/posts?page=${pageParam}`).then(r=>r.json()),
  getNextPageParam: (last) => last.nextPage ?? false
});

```

---

## ⚙️ **React 18+ Features**

### **Concurrent Rendering**

```jsx
import { useTransition, useDeferredValue } from 'react';

function App() {
  const [isPending, startTransition] = useTransition();
  const [count, setCount] = useState(0);

  const handleClick = () => {
    startTransition(() => {
      setCount(count + 1);
    });
  };

  return (
    <div>
      <button onClick={handleClick}>Count: {count}</button>
      {isPending && <div>Updating...</div>}
    </div>
  );
}

```

### **Suspense**

```jsx
import { Suspense, lazy } from 'react';

const LazyComponent = lazy(() => import('./LazyComponent'));

function App() {
  return (
    <Suspense fallback={<div>Loading...</div>}>
      <LazyComponent />
    </Suspense>
  );
}

```

### **Transitions & Deferred Value**

```jsx
const [isPending, startTransition] = useTransition();
const [q, setQ] = useState('');
const dq = useDeferredValue(q);
startTransition(() => setQ('next')); // mark non-urgent

```

### **React 19 Actions (forms)**

```jsx
function ContactForm(){
  const [isPending, startTransition] = useTransition();
  const submit = (fd) => startTransition(() => fetch('/api/contact',{ method:'POST', body:fd }));
  return <form onSubmit={(e)=>{e.preventDefault(); submit(new FormData(e.currentTarget));}}>{isPending?'...':<button>Send</button>}</form>;
}

```

---

## 🚀 **Performance Optimization**

### **React.memo**

```jsx
const ExpensiveComponent = React.memo(({ data }) => {
  return <div>{data.map(item => <div key={item.id}>{item.name}</div>)}</div>;
});

```

### **Code Splitting**

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

### **Virtualization**

```jsx
import { FixedSizeList as List } from 'react-window';

function VirtualizedList({ items }) {
  const Row = ({ index, style }) => (
    <div style={style}>{items[index].name}</div>
  );

  return (
    <List
      height={600}
      itemCount={items.length}
      itemSize={50}
    >
      {Row}
    </List>
  );
}

```

### **Core Web Vitals (LCP)**

```jsx
function OptimizedImage({ src, alt }){
  return <img src={src} alt={alt} loading="eager" width={800} height={600} />;
}

```

---

## 🧪 **Testing**

### **React Testing Library**

```jsx
import { render, screen, fireEvent } from '@testing-library/react';
import userEvent from '@testing-library/user-event';

test('user can submit form', async () => {
  const user = userEvent.setup();
  render(<ContactForm />);

  await user.type(screen.getByLabelText('Name'), 'John Doe');
  await user.type(screen.getByLabelText('Email'), 'john@example.com');
  await user.click(screen.getByRole('button', { name: 'Submit' }));

  expect(screen.getByText('Thank you, John Doe!')).toBeInTheDocument();
});

```

### **Custom Hooks Testing**

```jsx
import { renderHook, act } from '@testing-library/react';

test('useCounter hook', () => {
  const { result } = renderHook(() => useCounter(0));

  expect(result.current.count).toBe(0);

  act(() => {
    result.current.increment();
  });

  expect(result.current.count).toBe(1);
});

```

---

## 🧭 **Architecture Patterns**

### **Component Composition**

```jsx
function Card({ children, variant = 'default' }) {
  return <div className={`card card--${variant}`}>{children}</div>;
}

function CardHeader({ children }) {
  return <div className="card__header">{children}</div>;
}

function CardBody({ children }) {
  return <div className="card__body">{children}</div>;
}

// Usage
<Card variant="elevated">
  <CardHeader><h3>Title</h3></CardHeader>
  <CardBody><p>Content</p></CardBody>
</Card>

```

### **Custom Hooks**

```jsx
function useApi(url) {
  const [data, setData] = useState(null);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState(null);

  useEffect(() => {
    fetch(url)
      .then(res => res.json())
      .then(data => {
        setData(data);
        setLoading(false);
      })
      .catch(error => {
        setError(error);
        setLoading(false);
      });
  }, [url]);

  return { data, loading, error };
}

```

### **Jest Config & Fetch Mock**

```jsx
module.exports = { testEnvironment: 'jsdom', setupFilesAfterEnv: ['<rootDir>/src/setupTests.js'] };
global.fetch = jest.fn().mockResolvedValue({ ok:true, json: async () => ({ ok:true }) });

```

### **React Query Test Provider**

```jsx
const qc = new QueryClient();
render(<QueryClientProvider client={qc}><UserProfile userId={1} /></QueryClientProvider>);

```

### **Ref Forwarding & Portals**

```jsx
const FancyInput = forwardRef((p, ref) => <input ref={ref} {...p} />);
createPortal(<Modal/>, document.body);

```

### **Error Boundary (class)**

```jsx
class ErrorBoundary extends React.Component{ static getDerivedStateFromError(){return{hasError:true}}; render(){return this.state?.hasError? 'Oops' : this.props.children;}}

```

---

## 🔧 **Common Patterns**

### **Controlled Components**

```jsx
function ControlledInput() {
  const [value, setValue] = useState('');

  return (
    <input
      value={value}
      onChange={(e) => setValue(e.target.value)}
    />
  );
}

```

### **Uncontrolled Components**

```jsx
function UncontrolledInput() {
  const inputRef = useRef();

  const handleSubmit = () => {
    console.log(inputRef.current.value);
  };

  return (
    <div>
      <input ref={inputRef} />
      <button onClick={handleSubmit}>Submit</button>
    </div>
  );
}

```

### **Error Boundaries**

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
    console.error('Error:', error, errorInfo);
  }

  render() {
    if (this.state.hasError) {
      return <h2>Something went wrong.</h2>;
    }

    return this.props.children;
  }
}

```

---

## 📊 **Performance Metrics**

| Metric | Description | Target |
|--------|-------------|--------|
| **LCP** | Largest Contentful Paint | < 2.5s |
| **FID** | First Input Delay | < 100ms |
| **CLS** | Cumulative Layout Shift | < 0.1 |
| **TTFB** | Time to First Byte | < 600ms |

---

## 🎯 **Interview Tips**

### **Common Questions**

1. **React vs Vue/Angular** - Component-based vs framework differences

2. **Hooks vs Class Components** - Modern vs legacy patterns

3. **State Management** - When to use Redux vs Context

4. **Performance** - How to optimize React apps

5. **Testing** - How to test React components

### **Key Concepts**

- **Virtual DOM**: Efficient diffing and updates

- **Component Lifecycle**: Mount, update, unmount phases

- **State Management**: Local vs global state

- **Performance**: Memoization, code splitting, virtualization

- **Testing**: Unit, integration, and E2E testing

### **Best Practices**

- Use functional components with hooks

- Keep components small and focused

- Use proper state management

- Optimize for performance

- Write comprehensive tests

---

## ⚡ **Last-Minute Review (5 minutes)**

### **Must-Know Concepts**

- **Virtual DOM**: JS representation for efficient diffing

- **Reconciliation**: React's diffing algorithm (Fiber in React 16+)

- **Hooks Rules**: Only call at top level, only in React functions

- **useState**: Returns [state, setState], triggers re-render

- **useEffect**: Runs after render, cleanup on unmount/deps change

- **useMemo/useCallback**: Memoize expensive calculations/functions

- **React.memo**: Prevents re-render if props unchanged

### **Quick Code Snippets**

```jsx
// useState
const [count, setCount] = useState(0);

// useEffect
useEffect(() => { fetchData(); }, [id]);

// useMemo
const value = useMemo(() => expensive(), [dep]);

// React.memo
const Memoized = React.memo(Component);

```

### **Common Anti-Patterns to Avoid**

- ❌ **Prop drilling** - Pass props through many levels (use Context/state management)

- ❌ **Mutating state** - `state.push()`, `state.x = y` (always return new objects/arrays)

- ❌ **Creating objects in render** - `user={{ id }}` causes re-renders (use useMemo)

- ❌ **Missing keys in lists** - Causes reconciliation issues (always provide stable keys)

- ❌ **Conditional hooks** - Breaks React's rules (hooks must be unconditional)

- ❌ **Unnecessary re-renders** - Creating functions in render (use useCallback)

- ❌ **Direct DOM manipulation** - Defeats React's purpose (use state/refs)

- ❌ **Large components** - Hard to maintain (split into smaller components)

### **Common Gotchas**

- Don't mutate state directly (`state.push()` ❌)

- useEffect dependencies must include all used values

- Keys in lists must be stable and unique

- Conditional hooks will break (hooks must be unconditional)

*Remember: Practice with real projects, understand the concepts deeply, and always consider performance implications!*

---

## ⚙️ **React internally working**

Excellent 👏 — this is one of the most powerful topics for a senior front-end or system design interview: “How does React work internally?”

Let’s go deep — beyond the surface — into React’s internal architecture, from JSX → Virtual DOM → Fiber → Rendering → Commit phase.

### 🧠 1️⃣ JSX Compilation

- JSX is compiled by Babel into `React.createElement()` calls.

```jsx
const element = <h1>Hello React</h1>;

```

After compilation:

```js
const element = React.createElement("h1", null, "Hello React");

```

### 🧩 2️⃣ Virtual DOM Creation

- Lightweight, in-memory representation of the DOM that describes the UI.

```js
{
  type: "h1",
  props: { children: "Hello React" },
  key: null,
  ref: null
}

```

### 🧬 3️⃣ Fiber Architecture (React 16+)

- Fiber makes rendering asynchronous, interruptible, and incremental.

- Each Fiber node is a unit of work (linked structure: child, sibling, return, etc.).

```text
Fiber Node:
{ type, key, stateNode, child, sibling, return, pendingProps, memoizedProps, effectTag, alternate }

```

### ⏳ 4️⃣ Reconciliation Phase (Render)

- Diff old vs new trees; mark effects: Placement, Update, Deletion.

- Can be paused/resumed/aborted (cooperative scheduling).

### 🧵 5️⃣ Scheduler & Priority System

- Prioritizes work (inputs/animation high; background low) and yields to the browser to keep 60 FPS when needed.

### 🧮 6️⃣ Commit Phase

- Apply mutations to the real DOM, attach refs, call layout lifecycles.

- Synchronous and blocking until finished.

### 🧰 7️⃣ Hooks System

- Hooks stored as a linked list on each Fiber; order must be stable.

```js
const [count, setCount] = useState(0);
// Hook node stores memoizedState and queue; React walks them in order each render

```

### ⚡ 8️⃣ Re-render & Diffing Cycle

- `setState` creates a work-in-progress tree, diffs with current, commits minimal changes; trees swap (current vs WIP).

### 🧹 9️⃣ Cleanup & Effects

- Runs effects (`useEffect`, mount/update lifecycles), cleans previous ones, releases old fibers.

### 🧠 🔟 Concurrent Features

- Pause/resume (transitions), time slicing, batching, prioritization → non-blocking UX.

### 🔍 Deep Internal Flow Summary

| Stage | Component | Responsibility |
| --- | --- | --- |
| Parse | Babel | JSX → `React.createElement()` |
| Virtual DOM | React | In-memory element tree |
| Fiber Nodes | React | Unit-of-work linked structure |
| Reconciliation | React | Diff old vs new |
| Scheduler | React Fiber | Prioritize/yield work |
| Commit | React DOM | Apply DOM mutations |
| Hooks | React | State/effects per-fiber |
| GC & Cleanup | Browser + React | Free fibers, cleanup effects |

### ⚙️ Performance Optimizations Inside React

- Fiber diffing, key-based list updates, batched updates, lazy initialization, concurrent rendering.

### 💡 Interview Tip

React builds a Virtual DOM, computes minimal changes via the Fiber reconciler, schedules work by priority, and commits synchronously to the browser DOM. Fiber enables concurrent, non-blocking rendering.
