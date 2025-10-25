# ⚛️ React.js Interview Notes (2025 Edition)

## ⚡ Section 4 — Rendering, Lifecycle & Performance — Q71-Q90

---

### 71. ⚡ What triggers a re-render in React?

**🧠 Concept**

A re-render happens when React needs to update the UI because state, props, or context values changed.

**💻 Example**
```jsx
function Counter() {
  const [count, setCount] = useState(0); // State change triggers re-render
  const [name, setName] = useState(''); // This also triggers re-render
  
  return (
    <div>
      <button onClick={() => setCount(count + 1)}>{count}</button>
      <input value={name} onChange={e => setName(e.target.value)} />
    </div>
  );
}
```

📝 **Deeper Insight**

Re-renders are triggered by:
- **State changes** (`useState`, `useReducer`)
- **Props changes** (parent re-renders)
- **Context changes** (provider value updates)
- **Parent re-renders** (cascading effect)
- **Force updates** (`this.forceUpdate()` in class components)

---

### 72. ⚡ How does React determine which components to re-render?

🧠 **Concept**

React uses a **reconciliation algorithm** to compare the previous and current virtual DOM trees and determine what needs updating.

💻 **Example**

```jsx
// React compares these trees:
// Previous: <div><h1>Hello</h1></div>
// Current:  <div><h1>Hello World</h1></div>
// Result: Only the h1 text content updates
```

📝 **Deeper Insight**

React's reconciliation process:
1. **Diffing algorithm** compares virtual DOM trees
2. **Component type comparison** (same type = reuse, different = replace)
3. **Key prop optimization** for lists
4. **Shallow comparison** for props and state
5. **Batching** multiple updates into single render

---

### 73. ⚡ What is `React.memo()` and how does it work?

🧠 **Concept**

`React.memo()` is a **higher-order component** that prevents unnecessary re-renders by memoizing the component based on props.

💻 **Example**

```jsx
const ExpensiveComponent = React.memo(({ name, age }) => {
  console.log('Rendering ExpensiveComponent');
  return <div>{name} is {age} years old</div>;
});

// Only re-renders if name or age props change
<ExpensiveComponent name="John" age={25} />
```

📝 **Deeper Insight**

`React.memo()` performs **shallow comparison** of props by default.
You can provide a custom comparison function:
```jsx
const MyComponent = React.memo(Component, (prevProps, nextProps) => {
  return prevProps.id === nextProps.id; // Custom comparison
});
```

---

### 74. ⚡ What is the difference between `React.memo()` and `useMemo()`?

🧠 **Concept**

- **`React.memo()`**  memoizes entire components
- **`useMemo()`**  memoizes computed values within components

💻 **Example**

```jsx
// React.memo - memoizes component
const ExpensiveComponent = React.memo(({ data }) => {
  return <div>{data.name}</div>;
});

// useMemo - memoizes value
function MyComponent({ items }) {
  const expensiveValue = useMemo(() => {
    return items.reduce((sum, item) => sum + item.value, 0);
  }, [items]);
  
  return <div>Total: {expensiveValue}</div>;
}
```

📝 **Deeper Insight**

- **`React.memo()`**  prevents component re-renders
- **`useMemo()`**  prevents expensive recalculations
- **`useCallback()`**  prevents function recreation (related to `useMemo`)

---

### 75. ⚡ What is `React.PureComponent` and how does it differ?

🧠 **Concept**

`PureComponent` is the **class component equivalent** of `React.memo()` - it performs shallow comparison of props and state to prevent unnecessary re-renders.

💻 **Example**

```jsx
// Class component with PureComponent
class MyComponent extends React.PureComponent {
  render() {
    return <div>{this.props.name}</div>;
  }
}

// Functional equivalent with React.memo
const MyComponent = React.memo(({ name }) => {
  return <div>{name}</div>;
});
```

📝 **Deeper Insight**

`PureComponent` differences:
- **Class-based** (vs functional with `React.memo`)
- **Shallow comparison** of both props AND state
- **Legacy approach** (hooks are preferred now)
- **Performance optimization** for class components

---

### 76. ⚡ How do you prevent unnecessary re-renders?

🧠 **Concept**

Prevent unnecessary re-renders by optimizing component updates, memoization, and proper state management.

💻 **Example**

```jsx
// ❌ Causes unnecessary re-renders
function Parent() {
  const [count, setCount] = useState(0);
  const [name, setName] = useState('');
  
  return (
    <div>
      <button onClick={() => setCount(count + 1)}>{count}</button>
      <ExpensiveChild name={name} /> {/* Re-renders when count changes */}
    </div>
  );
}

// ✅ Optimized
function Parent() {
  const [count, setCount] = useState(0);
  const [name, setName] = useState('');
  
  return (
    <div>
      <button onClick={() => setCount(count + 1)}>{count}</button>
      <ExpensiveChildMemo name={name} /> {/* Only re-renders when name changes */}
    </div>
  );
}

const ExpensiveChildMemo = React.memo(ExpensiveChild);
```

📝 **Deeper Insight**

Optimization strategies:
- **`React.memo()`** for component memoization
- **`useMemo()`** for expensive calculations
- **`useCallback()`** for stable function references
- **State splitting** to minimize re-render scope
- **Context optimization** with multiple contexts

---

### 77. ⚡ What is code splitting, and how does React support it?

🧠 **Concept**

Code splitting is the practice of **dividing your bundle into smaller chunks** that are loaded on-demand, improving initial load time.

💻 **Example**

```jsx
import { lazy, Suspense } from 'react';

// Lazy load components
const LazyComponent = lazy(() => import('./LazyComponent'));
const AnotherLazy = lazy(() => import('./AnotherLazy'));

function App() {
  return (
    <Suspense fallback={<div>Loading...</div>}>
      <LazyComponent />
      <AnotherLazy />
    </Suspense>
  );
}
```

📝 **Deeper Insight**

React supports code splitting through:
- **`React.lazy()`** for component-level splitting
- **`Suspense`** for loading states
- **Dynamic imports** with `import()`
- **Route-based splitting** (React Router)
- **Bundle analysis** tools (webpack-bundle-analyzer)

---

### 78. ⚡ What is lazy loading, and how is it implemented in React?

🧠 **Concept**

Lazy loading **defers loading** of components, routes, or resources until they're actually needed, reducing initial bundle size.

💻 **Example**

```jsx
import { lazy, Suspense } from 'react';
import { BrowserRouter, Routes, Route } from 'react-router-dom';

// Lazy load route components
const Home = lazy(() => import('./pages/Home'));
const About = lazy(() => import('./pages/About'));
const Contact = lazy(() => import('./pages/Contact'));

function App() {
  return (
    <BrowserRouter>
      <Suspense fallback={<div>Loading page...</div>}>
        <Routes>
          <Route path="/" element={<Home />} />
          <Route path="/about" element={<About />} />
          <Route path="/contact" element={<Contact />} />
        </Routes>
      </Suspense>
    </BrowserRouter>
  );
}
```

📝 **Deeper Insight**

Lazy loading benefits:
- **Faster initial load** (smaller bundle)
- **Better user experience** (progressive loading)
- **Reduced memory usage** (load on demand)
- **Network optimization** (fewer requests initially)

---

### 79. ⚡ What is `React.lazy()` and Suspense?

🧠 **Concept**

`React.lazy()` creates a **dynamically imported component**, while `Suspense` provides a **fallback UI** while the component loads.

💻 **Example**

```jsx
import { lazy, Suspense } from 'react';

const LazyChart = lazy(() => import('./Chart'));

function Dashboard() {
  return (
    <div>
      <h1>Dashboard</h1>
      <Suspense fallback={<div>Loading chart...</div>}>
        <LazyChart data={chartData} />
      </Suspense>
    </div>
  );
}
```

📝 **Deeper Insight**

- **`React.lazy()`** requires default exports
- **`Suspense`** can wrap multiple lazy components
- **Error boundaries** should wrap Suspense for error handling
- **Nested Suspense** allows granular loading states

---

### 80. ⚡ What are Suspense boundaries?

🧠 **Concept**

Suspense boundaries are **error-like components** that catch loading states and display fallback UI while async operations complete.

💻 **Example**

```jsx
function App() {
  return (
    <div>
      <Header />
      <Suspense fallback={<PageSkeleton />}>
        <MainContent />
        <Suspense fallback={<SidebarSkeleton />}>
          <Sidebar />
        </Suspense>
      </Suspense>
      <Footer />
    </div>
  );
}
```

📝 **Deeper Insight**

Suspense boundaries:
- **Catch loading states** from lazy components
- **Display fallback UI** during loading
- **Can be nested** for granular control
- **Work with data fetching** (React Query, SWR)

---

### 81. ⚡ What are transitions in React 18, and how do they work?

🧠 **Concept**

Transitions let you **mark updates as non-urgent**, allowing React to keep the UI responsive during expensive operations.

💻 **Example**

```jsx
import { useTransition, startTransition } from 'react';

function SearchResults() {
  const [isPending, startTransition] = useTransition();
  const [query, setQuery] = useState('');
  const [results, setResults] = useState([]);

  const handleSearch = (newQuery) => {
    setQuery(newQuery);
    startTransition(() => {
      setResults(expensiveSearch(newQuery));
    });
  };

  return (
    <div>
      <input value={query} onChange={e => handleSearch(e.target.value)} />
      {isPending && <div>Searching...</div>}
      <ResultsList results={results} />
    </div>
  );
}
```

📝 **Deeper Insight**

Transitions enable:
- **Concurrent rendering** (non-blocking updates)
- **Priority-based updates** (urgent vs non-urgent)
- **Better user experience** (responsive UI)
- **Automatic batching** of updates

---

### 82. ⚡ What is concurrent rendering, and how is it different from synchronous rendering?

🧠 **Concept**

Concurrent rendering allows React to **interrupt and resume work**, keeping the UI responsive, while synchronous rendering blocks until complete.

💻 **Example**

```jsx
// Synchronous (React 17 and earlier)
function App() {
  const [count, setCount] = useState(0);
  
  const handleClick = () => {
    setCount(count + 1); // Blocks UI until complete
    setCount(count + 1); // Blocks UI until complete
  };
  
  return <button onClick={handleClick}>{count}</button>;
}

// Concurrent (React 18+)
function App() {
  const [count, setCount] = useState(0);
  
  const handleClick = () => {
    startTransition(() => {
      setCount(count + 1); // Can be interrupted
      setCount(count + 1); // Can be interrupted
    });
  };
  
  return <button onClick={handleClick}>{count}</button>;
}
```

📝 **Deeper Insight**

Concurrent rendering benefits:
- **Non-blocking updates** (UI stays responsive)
- **Priority-based rendering** (urgent updates first)
- **Automatic batching** (multiple updates batched)
- **Time slicing** (work is divided into chunks)

---

### 83. ⚡ What is the difference between hydration and rehydration?

🧠 **Concept**

- **Hydration**  React takes over server-rendered HTML
- **Rehydration**  React re-establishes component state after hydration

💻 **Example**

```jsx
// Server-side rendering
function App() {
  return <div>Hello World</div>;
}

// Client-side hydration
const root = createRoot(document.getElementById('root'));
root.hydrate(<App />); // Takes over existing HTML

// Rehydration (if needed)
// React re-establishes event listeners, state, etc.
```

📝 **Deeper Insight**

- **Hydration**  attaching React to existing DOM
- **Rehydration**  restoring component state and event handlers
- **Hydration mismatches**  server/client HTML differences
- **Selective hydration**  hydrate only visible components

---

### 84. ⚡ What is the difference between blocking and concurrent rendering?

🧠 **Concept**

- **Blocking rendering**  React must finish all work before showing updates
- **Concurrent rendering**  React can interrupt and resume work, showing partial updates

💻 **Example**

```jsx
// Blocking (React 17)
function App() {
  const [items, setItems] = useState([]);
  
  const loadItems = () => {
    // This blocks the UI until complete
    const newItems = expensiveComputation();
    setItems(newItems);
  };
  
  return (
    <div>
      <button onClick={loadItems}>Load Items</button>
      <ItemList items={items} />
    </div>
  );
}

// Concurrent (React 18)
function App() {
  const [items, setItems] = useState([]);
  const [isPending, startTransition] = useTransition();
  
  const loadItems = () => {
    startTransition(() => {
      // This can be interrupted, UI stays responsive
      const newItems = expensiveComputation();
      setItems(newItems);
    });
  };
  
  return (
    <div>
      <button onClick={loadItems}>Load Items</button>
      {isPending && <div>Loading...</div>}
      <ItemList items={items} />
    </div>
  );
}
```

📝 **Deeper Insight**

Concurrent rendering advantages:
- **Non-blocking updates** (UI responsiveness)
- **Priority-based work** (urgent updates first)
- **Automatic batching** (multiple updates together)
- **Time slicing** (work divided into chunks)

---

### 85. ⚡ How does React handle batching updates?

🧠 **Concept**

React **batches multiple state updates** into a single re-render to improve performance and prevent unnecessary DOM updates.

💻 **Example**

```jsx
function App() {
  const [count, setCount] = useState(0);
  const [name, setName] = useState('');
  
  const handleClick = () => {
    setCount(count + 1); // Batched
    setName('Updated');   // Batched
    setCount(count + 1); // Batched
    // Only one re-render happens
  };
  
  return (
    <div>
      <button onClick={handleClick}>Update</button>
      <div>Count: {count}, Name: {name}</div>
    </div>
  );
}
```

📝 **Deeper Insight**

React 18 automatic batching:
- **Event handlers** (always batched)
- **Async operations** (promises, timeouts)
- **Native event handlers** (setTimeout, fetch)
- **Manual batching** with `flushSync()` if needed

---

### 86. ⚡ What is the role of the scheduler in React Fiber?

🧠 **Concept**

The scheduler is React Fiber's **task management system** that prioritizes and schedules work to keep the UI responsive.

💻 **Example**

```jsx
// React's internal scheduler prioritizes:
// 1. User interactions (clicks, typing)
// 2. Animation frames
// 3. Data fetching
// 4. Background tasks
```

📝 **Deeper Insight**

Scheduler responsibilities:
- **Work prioritization** (urgent vs non-urgent)
- **Time slicing** (dividing work into chunks)
- **Interruption handling** (pausing/resuming work)
- **Deadline management** (avoiding frame drops)

---

### 87. ⚡ What are the phases of React rendering (render vs commit)?

🧠 **Concept**

React rendering has two main phases:
- **Render phase**  creating virtual DOM (can be interrupted)
- **Commit phase**  updating real DOM (synchronous)

💻 **Example**

```jsx
// Render phase (interruptible)
function Component() {
  const [count, setCount] = useState(0);
  return <div>{count}</div>; // Virtual DOM created
}

// Commit phase (synchronous)
// React updates the actual DOM
// Calls lifecycle methods
// Runs effects
```

📝 **Deeper Insight**

Render phase:
- **Pure computation** (no side effects)
- **Can be interrupted** (concurrent rendering)
- **Creates virtual DOM** tree
- **Determines changes** needed

Commit phase:
- **Updates real DOM** (synchronous)
- **Runs effects** (`useEffect`)
- **Calls lifecycle methods**
- **Cannot be interrupted**

---

### 88. ⚡ How do you handle expensive computations efficiently?

🧠 **Concept**

Use **memoization techniques** to avoid recalculating expensive operations on every render.

💻 **Example**

```jsx
function ExpensiveComponent({ data }) {
  // ❌ Recalculates on every render
  const expensiveValue = data.reduce((sum, item) => {
    return sum + complexCalculation(item);
  }, 0);
  
  // ✅ Memoized calculation
  const expensiveValue = useMemo(() => {
    return data.reduce((sum, item) => {
      return sum + complexCalculation(item);
    }, 0);
  }, [data]);
  
  return <div>Result: {expensiveValue}</div>;
}
```

📝 **Deeper Insight**

Optimization strategies:
- **`useMemo()`** for expensive calculations
- **`useCallback()`** for stable function references
- **`React.memo()`** for component memoization
- **Web Workers** for CPU-intensive tasks
- **Virtualization** for large lists

---

### 89. ⚡ What is windowing (React Window / Virtualized Lists)?

🧠 **Concept**

Windowing renders only **visible items** in large lists, dramatically improving performance by avoiding rendering thousands of DOM nodes.

💻 **Example**

```jsx
import { FixedSizeList as List } from 'react-window';

function VirtualizedList({ items }) {
  const Row = ({ index, style }) => (
    <div style={style}>
      {items[index].name}
    </div>
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

📝 **Deeper Insight**

Windowing benefits:
- **Constant performance** (regardless of list size)
- **Reduced memory usage** (only visible items in DOM)
- **Faster rendering** (fewer DOM nodes)
- **Smooth scrolling** (virtual positioning)

---

### 90. ⚡ How do you measure and fix React performance bottlenecks?

🧠 **Concept**

Use **profiling tools** to identify performance issues and apply appropriate optimization techniques.

💻 **Example**

```jsx
// React DevTools Profiler
import { Profiler } from 'react';

function onRenderCallback(id, phase, actualDuration) {
  console.log('Component:', id, 'Phase:', phase, 'Duration:', actualDuration);
}

function App() {
  return (
    <Profiler id="App" onRender={onRenderCallback}>
      <ExpensiveComponent />
    </Profiler>
  );
}
```

📝 **Deeper Insight**

Performance measurement tools:
- **React DevTools Profiler** (component-level)
- **Chrome DevTools** (overall performance)
- **Lighthouse** (Core Web Vitals)
- **Bundle analyzers** (webpack-bundle-analyzer)
- **Custom profiling** with `Profiler` component

Common fixes:
- **Memoization** (`React.memo`, `useMemo`, `useCallback`)
- **Code splitting** (lazy loading)
- **Virtualization** (windowing)
- **State optimization** (minimal re-renders)
- **Bundle optimization** (tree shaking, compression)

---
