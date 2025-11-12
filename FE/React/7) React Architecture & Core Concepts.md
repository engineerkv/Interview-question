# 🧠 7. React Architecture & Core Concepts (Q59–66)

---

## 🧩 Q59. What is React Fiber and how does it work?

### 🧠 Concept

React Fiber is a rewrite of React's reconciliation engine. It enables interruptible, prioritized work for better performance, enabling concurrent rendering and keeping UI responsive.

---

### 💡 Example

```jsx
const [isPending, startTransition] = useTransition();
const [count, setCount] = useState(0);
return (
  <button onClick={() => startTransition(() => setCount(c => c + 1))}>
    {isPending ? 'Updating...' : count}
  </button>
);
```

---

### 🔍 Deep Insights

* **Rule:** Fiber introduces virtual call stack enabling work to be split, prioritized, and interrupted.
* **Use Case:** Enables concurrent rendering, keeping UI responsive during heavy operations.
* **Common Mistake:** Old reconciliation was synchronous and blocking, Fiber enables async rendering.
* **Pro Tip:** Existing code works without changes, new features are opt-in.

---

### ⭐ Senior Takeaway

Fiber enables React 18+ features like Suspense and Transitions.

---

## 🧩 Q60. How does Fiber improve reconciliation and rendering?

### 🧠 Concept

Fiber breaks rendering into small interruptible units. It can pause and resume work based on priority, using browser idle time for better performance.

---

### 💡 Example

```jsx
function workLoop(deadline) {
  while (nextUnitOfWork && !shouldYield()) {
    nextUnitOfWork = performUnitOfWork(nextUnitOfWork);
  }
  if (nextUnitOfWork) requestIdleCallback(workLoop);
}
```

---

### 🔍 Deep Insights

* **Rule:** Breaks rendering into small chunks that can be interrupted and resumed.
* **Use Case:** Uses browser idle time (requestIdleCallback) for better performance.
* **Common Mistake:** Different update types have different priorities (user input > background updates).
* **Pro Tip:** Can render parts of tree incrementally, not all at once.

---

### ⭐ Senior Takeaway

Fiber enables React to keep UI responsive during expensive operations.

---

## 🧩 Q61. What is React Fiber and how does it improve reconciliation?

### 🧠 Concept

React Fiber is a reimplementation of React's reconciliation algorithm that enables incremental rendering, allowing React to split work into chunks and prioritize updates. Fiber enables features like concurrent rendering and time-slicing.

---

### 💡 Example

```jsx
// Fiber enables concurrent features
import { startTransition } from 'react';

function App() {
  const [isPending, startTransition] = useTransition();
  const [input, setInput] = useState('');
  const [list, setList] = useState([]);
  
  const handleChange = (e) => {
    setInput(e.target.value); // Urgent update
    startTransition(() => {
      setList(expensiveFilter(e.target.value)); // Non-urgent update
    });
  };
  
  return (
    <div>
      <input value={input} onChange={handleChange} />
      {isPending && <span>Updating...</span>}
      <List items={list} />
    </div>
  );
}
```

---

### 🔍 Deep Insights

* **Rule:** Fiber breaks work into units that can be paused, resumed, or aborted.
* **Use Case:** Enables concurrent rendering, time-slicing, and priority-based updates.
* **Common Mistake:** Fiber doesn't change React's API, it's an internal implementation detail.
* **Pro Tip:** Use `startTransition` and `useDeferredValue` to leverage Fiber's capabilities.

---

### ⭐ Senior Takeaway

Fiber enables React to be more responsive by prioritizing urgent updates over non-urgent ones.

---

## 🧩 Q62. What are React Portals and when do you use them?

### 🧠 Concept

React Portals render children into a DOM node outside the parent component. Use them for modals, tooltips, and overlays that need to escape parent z-index constraints.

---

### 💡 Example

```jsx
import { createPortal } from 'react-dom';

function Modal({ isOpen, onClose, children }) {
  if (!isOpen) return null;
  return createPortal(
    <div className="modal-overlay" onClick={onClose}>
      <div className="modal-content" onClick={e => e.stopPropagation()}>
        {children}
      </div>
    </div>,
    document.body
  );
}
```

---

### 🔍 Deep Insights

* **Rule:** Render children into different DOM node while keeping React tree structure.
* **Use Case:** Modals, tooltips, overlays, or any UI that needs to escape parent z-index.
* **Common Mistake:** Events still bubble through React component tree, not DOM tree.
* **Pro Tip:** Solves z-index stacking context issues with parent components.

---

### ⭐ Senior Takeaway

Portals solve the "modal needs to be at root level" problem elegantly.

---

## 🧩 Q63. What are Error Boundaries and how do you implement them?

### 🧠 Concept

Error Boundaries catch JavaScript errors in child components and display fallback UI. Only class components can be Error Boundaries currently, though hooks support is coming.

---

### 💡 Example

```jsx
class ErrorBoundary extends React.Component {
  constructor(props) {
    super(props);
    this.state = { hasError: false, error: null };
  }
  static getDerivedStateFromError(error) {
    return { hasError: true, error };
  }
  componentDidCatch(error, errorInfo) {
    console.error('Error caught:', error, errorInfo);
  }
  render() {
    if (this.state.hasError) {
      return <div>Something went wrong.</div>;
    }
    return this.props.children;
  }
}
```

---

### 🔍 Deep Insights

* **Rule:** Catch errors in child component tree and prevent entire app from crashing.
* **Use Case:** Wrap app sections to gracefully handle errors and show fallback UI.
* **Common Mistake:** Only catches errors in render, lifecycle, and constructors—not event handlers or async code.
* **Pro Tip:** Currently only class components can be Error Boundaries (hooks coming).

---

### ⭐ Senior Takeaway

Error Boundaries are React's try-catch for component trees.

---

## 🧩 Q64. What are Higher-Order Components (HOCs) and Render Props?

### 🧠 Concept

HOCs are functions that take a component and return an enhanced component. Render Props use a function prop to share code. Both are legacy patterns replaced by custom hooks.

---

### 💡 Example

```jsx
// Higher-Order Component
function withLoading(WrappedComponent) {
  return function WithLoadingComponent({ isLoading, ...props }) {
    if (isLoading) {
      return <div>Loading...</div>;
    }
    return <WrappedComponent {...props} />;
  };
}

// Render Props
function DataFetcher({ render }) {
  const [data, setData] = useState(null);
  useEffect(() => {
    fetch('/api/data').then(r => r.json()).then(setData);
  }, []);
  return render(data);
}
```

---

### 🔍 Deep Insights

* **Rule:** HOCs enhance components with additional functionality (legacy pattern).
* **Use Case:** Render Props use function props to share code between components (legacy pattern).
* **Common Mistake:** Custom hooks replace both patterns for sharing logic.
* **Pro Tip:** Still see HOCs in older codebases, hooks are preferred now.

---

### ⭐ Senior Takeaway

Hooks are the modern way to share logic, replacing HOCs and Render Props.

---

## 🧩 Q65. What are refs and how is ref forwarding implemented?

### 🧠 Concept

Refs access DOM elements or component instances. Ref forwarding lets parents access child component refs using forwardRef, enabling imperative operations when declarative isn't enough.

---

### 💡 Example

```jsx
import { forwardRef, useRef } from 'react';

const FancyInput = forwardRef((props, ref) => {
  return <input ref={ref} {...props} />;
});

function App() {
  const inputRef = useRef();
  const focusInput = () => {
    inputRef.current?.focus();
  };
  return (
    <div>
      <FancyInput ref={inputRef} placeholder="Type here..." />
      <button onClick={focusInput}>Focus Input</button>
    </div>
  );
}
```

---

### 🔍 Deep Insights

* **Rule:** Refs access DOM elements directly or component instances (imperative API).
* **Use Case:** Ref forwarding lets parent components access child component refs.
* **Common Mistake:** Use for focus management, animations, third-party libraries, or imperative operations.
* **Pro Tip:** useImperativeHandle customizes what ref exposes to parent (advanced use).

---

### ⭐ Senior Takeaway

Refs are for imperative operations when declarative isn't enough.

---

## 🧩 Q66. What is the React Profiler API and when is it used?

### 🧠 Concept

React Profiler API measures component rendering performance programmatically. Use it to identify slow components and optimize rendering in development or production.

---

### 💡 Example

```jsx
import { Profiler } from 'react';

function onRenderCallback(id, phase, actualDuration, baseDuration, startTime, commitTime) {
  console.log('Profiler:', {
    id,
    phase,
    actualDuration,
    baseDuration
  });
}

function App() {
  return (
    <Profiler id="App" onRender={onRenderCallback}>
      <MyComponent />
    </Profiler>
  );
}
```

---

### 🔍 Deep Insights

* **Rule:** Profiler API measures component render times programmatically.
* **Use Case:** Identify performance bottlenecks in production or development.
* **Common Mistake:** Primarily used during development for optimization.
* **Pro Tip:** Can be used in production to track performance metrics.

---

### ⭐ Senior Takeaway

Profiler API is for programmatic performance measurement, while DevTools is for visual analysis.

---
