# 🧠 7. React Architecture & Core Concepts (Q57–64)

---

## 57) What is the React Fiber architecture and why was it introduced?

React Fiber is a rewrite of React's reconciliation engine. It enables interruptible, prioritized work for better performance.

```jsx
const [isPending, startTransition] = useTransition();
const [count, setCount] = useState(0);
return <button onClick={() => startTransition(() => setCount(c => c + 1))}>{isPending ? 'Updating...' : count}</button>;
```

- **Core Innovation**: Introduces virtual call stack enabling work to be split, prioritized, and interrupted
- **Real-World Benefit**: Enables concurrent rendering, keeping UI responsive during heavy operations
- **Why Needed**: Old reconciliation was synchronous and blocking, Fiber enables async rendering
- **Backwards Compatible**: Existing code works without changes, new features are opt-in
- **Interview Tip**: Explain that Fiber enables React 18+ features like Suspense and Transitions

---

## 58) How does Fiber improve reconciliation and rendering?

Fiber breaks rendering into small interruptible units. It can pause and resume work based on priority.

```jsx
function workLoop(deadline) {
  while (nextUnitOfWork && !shouldYield()) {
    nextUnitOfWork = performUnitOfWork(nextUnitOfWork);
  }
  if (nextUnitOfWork) requestIdleCallback(workLoop);
}
```

- **Work Units**: Breaks rendering into small chunks that can be interrupted and resumed
- **Time Slicing**: Uses browser idle time (requestIdleCallback) for better performance
- **Priority System**: Different update types have different priorities (user input > background updates)
- **Incremental Rendering**: Can render parts of tree incrementally, not all at once
- **Interview Tip**: Explain that Fiber enables React to keep UI responsive during expensive operations

---

## 59) What is reconciliation and how does React decide what to re-render?

Reconciliation is React's algorithm comparing virtual DOM trees to decide what DOM changes are needed.

```jsx
// Virtual DOM comparison
const oldVDOM = { type: 'div', props: { className: 'container' }, children: [{ type: 'h1', props: { children: 'Hello' } }] };
const newVDOM = { type: 'div', props: { className: 'container' }, children: [{ type: 'h1', props: { children: 'Hello World' } }] };
// React compares and updates only changed text
```

- **Core Process**: Compares old and new virtual DOM trees to find differences
- **Diffing Algorithm**: Uses heuristics and keys to efficiently find changes
- **Minimal Updates**: Only updates DOM nodes that actually changed
- **Key Optimization**: Keys help React identify which items changed in lists
- **Interview Tip**: Explain that reconciliation is the "smart diffing" that makes React efficient

---

## 60) What are React Portals and when should you use them?

React Portals render children into a DOM node outside the parent component. Use them for modals, tooltips, and overlays.

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

- **Core Purpose**: Render children into different DOM node while keeping React tree structure
- **Real-World Use**: Modals, tooltips, overlays, or any UI that needs to escape parent z-index
- **Event Bubbling**: Events still bubble through React component tree, not DOM tree
- **Z-index Solution**: Solves z-index stacking context issues with parent components
- **Interview Tip**: Explain that Portals solve the "modal needs to be at root level" problem

---

## 61) What are Error Boundaries and how do they work?

Error Boundaries catch JavaScript errors in child components and display fallback UI. Only class components can be Error Boundaries.

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

- **Core Purpose**: Catch errors in child component tree and prevent entire app from crashing
- **Real-World Use**: Wrap app sections to gracefully handle errors and show fallback UI
- **Limitations**: Only catches errors in render, lifecycle, and constructors - not event handlers or async code
- **Class Components Only**: Currently only class components can be Error Boundaries (hooks coming)
- **Interview Tip**: Explain that Error Boundaries are React's try-catch for component trees

---

## 62) What are Higher-Order Components (HOCs) and Render Props?

HOCs are functions that take a component and return an enhanced component. Render Props use a function prop to share code.

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

- **HOCs**: Functions that enhance components with additional functionality (legacy pattern)
- **Render Props**: Pattern using function props to share code between components (legacy pattern)
- **Modern Alternative**: Custom hooks replace both patterns for sharing logic
- **Real-World Use**: Still see HOCs in older codebases, hooks are preferred now
- **Interview Tip**: Explain that hooks are the modern way to share logic, replacing HOCs and Render Props

---

## 63) What are refs and how is ref forwarding implemented?

Refs access DOM elements or component instances. Ref forwarding lets parents access child component refs.

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

- **Core Purpose**: Access DOM elements directly or component instances (imperative API)
- **Ref Forwarding**: forwardRef lets parent components access child component refs
- **Real-World Use**: Focus management, animations, third-party libraries, or imperative operations
- **useImperativeHandle**: Customize what ref exposes to parent (advanced use)
- **Interview Tip**: Explain that refs are for imperative operations when declarative isn't enough

---

## 64) What is the React Profiler API and when is it used?

React Profiler API measures component rendering performance. Use it to identify slow components and optimize rendering.

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

- **Core Purpose**: Measure component render times programmatically
- **Real-World Use**: Identify performance bottlenecks in production or development
- **Development Tool**: Primarily used during development for optimization
- **Production Monitoring**: Can be used in production to track performance metrics
- **Interview Tip**: Explain that Profiler API is for programmatic performance measurement, while DevTools is for visual analysis

---

**Note**: Questions about Controlled/Uncontrolled components (Q9), Strict Mode (Q54), and basic Reconciliation (Q11) are covered in other sections. This section focuses on advanced architecture concepts.

---
