---
sidebar_label: "Core Concepts & Components"
---
# ⚛️ 1. Core Concepts & Components (Q1–17)

> **Reviewed:** 2026-09 · Modernized for React 19. Legacy topics (class components, `forwardRef`) are labeled.

---

## Q1. 💡 React and its purpose

React is a JavaScript library for building user interfaces using reusable components and a virtual DOM - it simplifies UI development by allowing you to write declarative code instead of manually manipulating the browser's DOM. React uses a component-based architecture where UI is built by composing reusable pieces, and the virtual DOM compares trees in memory before touching the real DOM, making updates fast and predictable.

- **Trade-offs**: The catch is trying to manipulate DOM directly defeats React's purpose - allow React to handle updates through state changes. React's declarative approach simplifies UI updates compared to imperative DOM manipulation, especially in complex apps, but it trades direct DOM control for predictable, maintainable UI development at scale.

Example:

```jsx
function App() {
  return <div><h1>Hello, React!</h1></div>;
}

```

---

## Q2. 🔧 React components: functional vs class components

React components are reusable UI pieces that return JSX - functional components use functions and hooks, while class components use ES6 classes with lifecycle methods. Functional components with hooks are the recommended approach since React 16.8, and every React 19 feature (Actions, `use`, `useOptimistic`, Server Components, the React Compiler) targets function components. In frameworks like Next.js, function components can also be **Server Components** (async, run only on the server) or **Client Components**.

- **Trade-offs**: The catch is creating new class components when functional components with hooks would work better - use class components only when you need Error Boundaries (or use the `react-error-boundary` package), everything else works great with functional components. Functional components with hooks are simpler, more testable, and the future of React, but watch out - you'll still see class components in older codebases.

> **Legacy note (2026):** Class components are still fully supported in React 19 and still come up in interviews and older codebases; for new work prefer function components.

Example:

```jsx
function Welcome({ name }) {
  return <h1>Hello, {name}!</h1>;
}

```

---

## Q3. 🔧 JSX and how it works

JSX allows you to write HTML-like syntax in JavaScript - a compiler (Babel, SWC, esbuild, or TypeScript) turns it into function calls. Since React 17's **automatic JSX runtime**, `<div />` compiles to `jsx('div', …)` imported from `react/jsx-runtime`, so you no longer need `import React` in every file; the classic transform compiled to `React.createElement()`. JSX must have one root element or use Fragments, and JavaScript expressions go inside curly braces.

- **Trade-offs**: The catch is forgetting camelCase for attributes (className not class, onClick not onclick) - JSX is syntactic sugar that makes React code more maintainable than raw createElement calls, but watch out - it's not HTML, so some attributes and behaviors are different. JSX bridges HTML familiarity with JavaScript power, making React code intuitive, but you need to remember the differences.

Example:

```jsx
function UserProfile({ user, isLoggedIn }) {
  return (
    <div>
      <h1>{user.name}</h1>
      {isLoggedIn ? <p>Welcome back!</p> : <p>Please log in</p>}
    </div>
  );
}

// Compiled output (automatic runtime, React 17+):
// import { jsx as _jsx, jsxs as _jsxs } from 'react/jsx-runtime';
// _jsxs('div', { children: [_jsx('h1', { children: user.name }), ...] });

```

---

## Q4. 🤔 Virtual DOM vs Real DOM

Virtual DOM is React's lightweight JavaScript representation of the Real DOM - React compares virtual trees to update only what changed, minimizing expensive browser operations. Real DOM is the browser's actual HTML structure that triggers expensive reflows, repaints, and layout recalculations when changed, blocking the main thread. Virtual DOM is fast to compare in JavaScript, Real DOM is slow to change.

- **Trade-offs**: The catch is thinking virtual DOM is faster than direct DOM manipulation - it's not always faster, but it's smarter and more predictable. React batches state updates and uses heuristics to minimize diff calculations, which trades memory for predictability and performance in complex apps. Real DOM manipulation is expensive because browsers optimize for rendering, not frequent updates. Virtual DOM batches changes and calculates minimal updates before touching real DOM, but watch out - for simple apps, the virtual DOM overhead might not be worth it. Sometimes you need direct DOM access for things like focus management or third-party libraries.

Example:

```jsx
// Virtual DOM representation
const virtualElement = {
  type: 'div',
  props: { className: 'container', children: 'Hello World' }
};

// React compares virtual trees and applies minimal changes
function Counter({ count }) {
  return (
    <div>
      <h2>Count: {count}</h2>
      <button>Increment</button>
    </div>
  );
}

```

---

## Q5. 📊 Props vs state in React

Props are read-only data passed from parent to child, while state is mutable data inside a component that triggers re-renders when changed - props flow down, events flow up. State belongs to the component that owns it, use props for configuration, state for interactivity and user input.

- **Trade-offs**: The catch is trying to mutate props directly or lifting state too high in the component tree - memoize props with useMemo/useCallback to prevent unnecessary child re-renders. Unidirectional data flow (props down, callbacks up, state stays local) keeps React predictable, but watch out - prop drilling can get annoying in deep component trees, consider context or state management libraries.

Example:

```jsx
function App() {
  const [count, setCount] = useState(0); // State: owned by App component
  // Props: count passed down, onIncrement callback passed down
  return <Counter count={count} onIncrement={() => setCount(count + 1)} />;
}

```

---

## Q6. 💡 Keys in React and their importance

Keys help React track which list items changed, were added, or removed during reconciliation - they give React stable identity for efficient updates instead of re-rendering everything. Without keys, React re-renders all items when list changes, causing performance issues.

- **Trade-offs**: The catch is using array index as key breaks when items are reordered, added, or removed - use unique, stable IDs from your data, never index for dynamic lists. Keys enable React to efficiently update only changed items instead of recreating the entire list, but watch out - missing or duplicate keys can cause bugs and performance issues.

Example:

```jsx
function TodoList({ todos }) {
  return (
    <ul>
      {todos.map(todo => <li key={todo.id}>{todo.text}</li>)}
    </ul>
  );
}

```

---

## Q7. 🧩 Controlled vs uncontrolled components

Controlled components use React state for form values, giving React full control, while uncontrolled components use DOM refs to read values, letting the DOM own the state. Controlled means React owns the value, uncontrolled means DOM owns it.

- **Trade-offs**: The catch is mixing controlled and uncontrolled patterns in the same form - prefer controlled components, these are easier to test, validate, and integrate with React's ecosystem. Controlled components give React full control, making forms predictable and testable, but watch out - these require more code and state management compared to uncontrolled components.

Example:

```jsx
function ControlledForm() {
  const [value, setValue] = useState(''); // React owns the value
  // Input value controlled by React state, onChange updates state
  return <input value={value} onChange={(e) => setValue(e.target.value)} />;
}

```

---

## Q8. ⚛️ ⏰ React Fragments and when to use them

Fragments let you group multiple elements without adding extra DOM nodes - they solve React's "components must return one element" limitation without breaking CSS layouts. Fragments return multiple elements without wrapper divs that break CSS layouts.

- **Trade-offs**: The catch is wrapping everything in divs when Fragments would preserve layout - use React.Fragment with key prop for lists, `<>` doesn't support keys. Fragments solve the "one element" limitation elegantly without polluting the DOM, but watch out - you can't style or add event handlers to Fragments since these don't render anything.

Example:

```jsx
function Component() {
  return (
    <>
      <h1>Title</h1>
      <p>Description</p>
    </>
  );
}

```

---

## Q9. 💡 Reconciliation in React

Reconciliation is React's algorithm comparing virtual DOM trees to decide what DOM changes are needed - it uses heuristics and keys to efficiently find differences and update only changed nodes.

- **Trade-offs**: The catch is not understanding that reconciliation re-runs for a component's whole subtree whenever it re-renders, even if the child props didn't change - React uses two heuristics (different element types produce different trees; keys identify children) to diff in roughly O(n) instead of the O(n³) generic tree-diff worst case. Reconciliation is React's "smart diffing" that makes virtual DOM practical and performant, but watch out - reconciliation still has overhead, so avoid unnecessary re-renders with memoization when needed.

Example:

```jsx
function App() {
  const [count, setCount] = useState(0);
  return (
    <div>
      <h1>Count: {count}</h1>
      <button onClick={() => setCount(count + 1)}>Increment</button>
    </div>
  );
}

```

---

## Q10. 🧩 Lifecycle methods in class components

Class components have lifecycle methods across three phases: mounting (constructor → getDerivedStateFromProps → render → componentDidMount), updating (getDerivedStateFromProps → shouldComponentUpdate → render → getSnapshotBeforeUpdate → componentDidUpdate), and unmounting (componentWillUnmount). Error boundaries use getDerivedStateFromError and componentDidCatch. The legacy methods componentWillMount, componentWillReceiveProps, and componentWillUpdate were renamed with an `UNSAFE_` prefix in React 16.3 because they're unsafe with async/concurrent rendering; the unprefixed names log warnings - avoid both forms in new code.

> **Legacy note (2026):** Class components still work in React 19, but some class-era APIs were removed in React 19: string refs (`ref="input"`), legacy context (`contextTypes`/`getChildContext`), `propTypes` checking, and `defaultProps` on function components (still supported on classes). Interviews still ask about lifecycles to test your mental model — map them to hooks in Q11.

- **Trade-offs**: The catch is forgetting to clean up subscriptions or timers in componentWillUnmount, and using deprecated methods causes warnings. Use shouldComponentUpdate to prevent unnecessary re-renders, but lifecycle methods are being replaced by hooks in modern React - prefer functional components, but watch out - you'll still see class components in older codebases.

Example:

```jsx
class UserProfile extends React.Component {
  constructor(props) {
    super(props);
    this.state = { user: null, loading: true };
  }

  static getDerivedStateFromProps(props, state) {
    // Update state based on props
    return null;
  }

  shouldComponentUpdate(nextProps, nextState) {
    // Return false to prevent re-render
    return nextState.loading !== this.state.loading;
  }

  componentDidMount() {
    fetch('/api/user')
      .then(r => r.json())
      .then(user => this.setState({ user, loading: false }));
  }

  getSnapshotBeforeUpdate(prevProps, prevState) {
    // Capture info before DOM updates
    return null;
  }

  componentDidUpdate(prevProps, prevState, snapshot) {
    // Run after update completes
  }

  componentWillUnmount() {
    // Cleanup subscriptions, timers
  }

  static getDerivedStateFromError(error) {
    // Update state to show error UI
    return { hasError: true };
  }

  componentDidCatch(error, errorInfo) {
    // Log error to error reporting service
    console.error('Error caught:', error, errorInfo);
  }

  render() {
    if (this.state.hasError) {
      return <div>Something went wrong</div>;
    }
    return this.state.loading ? null : <div>{this.state.user.name}</div>;
  }
}

```

---

## Q11. 🔧 Converting class components to functional components with hooks

useEffect replaces lifecycle methods: empty array equals componentDidMount, dependencies equal componentDidUpdate, cleanup return equals componentWillUnmount - one hook handles all lifecycle needs. useEffect([]) equals mount, useEffect([deps]) equals update, return function equals unmount.

- **Trade-offs**: The catch is trying to replicate exact lifecycle behavior - hooks work differently, multiple useEffect hooks separate concerns better than one lifecycle method. Think "synchronize with an external system" rather than "run on mount": in development Strict Mode React mounts, unmounts, and re-mounts components to verify your cleanup is correct. Also, `componentDidMount` data fetching usually shouldn't become a `useEffect` fetch in modern code - use a framework loader/Server Component or TanStack Query (see Q20, Q50).

Example:

```jsx
// Class: componentDidMount + componentWillUnmount
// Hooks: one effect per concern, with cleanup
function ChatRoom({ roomId }) {
  useEffect(() => {
    const connection = createConnection(roomId);
    connection.connect();
    return () => connection.disconnect(); // runs before re-sync and on unmount
  }, [roomId]); // re-syncs when roomId changes (componentDidUpdate equivalent)
  return <h1>Room {roomId}</h1>;
}

// Class: getDerivedStateFromProps / derived state -> just compute during render
function Cart({ items }) {
  const total = items.reduce((sum, i) => sum + i.price, 0); // no state/effect needed
  return <p>Total: {total}</p>;
}

```

---

## Q12. 🔧 React Fiber and how it improves reconciliation

React Fiber is a rewrite of React's reconciliation engine that enables interruptible, prioritized work for better performance - it introduces a virtual call stack that allows work to be split into small units, prioritized, paused, and resumed. Fiber improves reconciliation by enabling incremental rendering, allowing React to split work into chunks and prioritize updates (user input > background updates), which enables concurrent rendering, time-slicing, and keeps UI responsive during heavy operations.

- **Trade-offs**: The catch is old reconciliation was synchronous and blocking, Fiber enables async rendering - existing code works without changes, new features are opt-in. Fiber enables React 18+ features like Suspense and Transitions, but watch out - use `startTransition` and `useDeferredValue` to leverage Fiber's capabilities. A common misconception is that React uses `requestIdleCallback`: it uses its own `scheduler` package (built on `MessageChannel` macrotasks) that works in roughly 5ms slices and yields back to the browser between them.

Example:

```jsx
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

## Q13. ❓ React Portals and when to use them

React Portals render children into a DOM node outside the parent component - use them for modals, tooltips, and overlays that need to escape parent z-index constraints. Render children into different DOM node while keeping React tree structure.

- **Trade-offs**: The catch is events still bubble through React component tree, not DOM tree - solves z-index stacking context issues with parent components. Portals solve the "modal needs to be at root level" problem elegantly, but watch out - good for modals, tooltips, overlays, or any UI that needs to escape parent z-index.

Example:

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

## Q14. ⚠️ Error Boundaries and how to implement them

Error Boundaries catch JavaScript errors thrown while rendering child components and display fallback UI. As of React 19 there is still **no built-in hook** for this - a boundary must be a class component with `getDerivedStateFromError`/`componentDidCatch`, which is why most apps use the `react-error-boundary` package (`<ErrorBoundary fallbackRender>` + `useErrorBoundary`). React 19 also added root-level `onCaughtError` / `onUncaughtError` / `onRecoverableError` options on `createRoot` for centralized logging. Frameworks provide file-based boundaries (e.g. Next.js `error.tsx`).

- **Trade-offs**: The catch is only catches errors in render, lifecycle methods, and constructors (and rejected promises read via `use()` / Suspense) - not event handlers, timers, or other async code, which you handle with try/catch or by rethrowing through `useErrorBoundary().showBoundary(error)`. Error Boundaries are React's try-catch for component trees, but watch out - wrap app sections to gracefully handle errors and show fallback UI.

Example:

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

// Common modern usage: react-error-boundary
import { ErrorBoundary } from 'react-error-boundary';

<ErrorBoundary
  fallbackRender={({ error, resetErrorBoundary }) => (
    <div role="alert">
      <p>{error.message}</p>
      <button onClick={resetErrorBoundary}>Retry</button>
    </div>
  )}
  onError={(error, info) => reportError(error, info.componentStack)}
>
  <Dashboard />
</ErrorBoundary>

// React 19 root-level error reporting
createRoot(container, {
  onUncaughtError: (error, info) => reportError(error, info.componentStack),
  onCaughtError: (error, info) => reportError(error, info.componentStack),
}).render(<App />);

```

---

## Q15. 🧩 Higher-Order Components (HOCs) vs Render Props

HOCs are functions that take a component and return an enhanced component, while Render Props use a function prop to share code - both are legacy patterns replaced by custom hooks. HOCs enhance components with additional functionality (legacy pattern).

- **Trade-offs**: The catch is custom hooks replace both patterns for sharing logic - still see HOCs in older codebases, hooks are preferred now. Hooks are the modern way to share logic, replacing HOCs and Render Props, but watch out - Render Props use function props to share code between components (legacy pattern).

Example:

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

## Q16. 💡 Refs and ref forwarding in React

Refs give you direct access to DOM nodes (or an imperative handle) for things declarative props can't express. **In React 19, function components receive `ref` as a regular prop**, so you just destructure it and pass it to the underlying element - no wrapper needed. Before React 19 you had to wrap the component in `forwardRef`, which still works but is on the path to deprecation. React 19 also lets **callback refs return a cleanup function**, which runs when the node is detached.

- **Trade-offs**: The catch is use for focus management, measuring layout, animations, third-party libraries, or other imperative operations - `useImperativeHandle` customizes what the ref exposes (Q28). Refs are an escape hatch, but watch out - reading/writing `ref.current` during render breaks purity, and exposing raw DOM nodes from design-system components couples consumers to your markup.

Example:

```jsx
import { useRef } from 'react';

// React 19: ref is just a prop
function FancyInput({ ref, ...props }) {
  return <input ref={ref} {...props} />;
}

// Callback ref with cleanup (React 19)
function Measured() {
  return (
    <div
      ref={(node) => {
        const observer = new ResizeObserver(() => console.log(node.getBoundingClientRect()));
        observer.observe(node);
        return () => observer.disconnect(); // cleanup when detached
      }}
    />
  );
}

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

## Q17. 🔌 React Profiler API and when to use it

React Profiler API measures component rendering performance programmatically - use it to identify slow components and optimize rendering in development or production. Profiler API measures component render times programmatically.

- **Trade-offs**: The catch is primarily used during development for optimization - can be used in production to track performance metrics. Profiler API is for programmatic performance measurement, while DevTools is for visual analysis, but watch out - identify performance bottlenecks in production or development.

Example:

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

