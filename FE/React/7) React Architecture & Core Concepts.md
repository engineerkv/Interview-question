# 🧠 7. React Architecture & Core Concepts (Q57–66)

---

## 57) What is the React Fiber architecture and why was it introduced?

Concept:
React Fiber architecture is a complete rewrite of React's reconciliation engine that introduces a virtual call stack, enabling work to be split into chunks, prioritized, and interrupted/resumed for better performance and user experience.

Example:
```jsx
// Fiber enables concurrent features
function App() {
  const [isPending, startTransition] = useTransition();
  const [count, setCount] = useState(0);
  
  const handleClick = () => {
    startTransition(() => {
      setCount(c => c + 1);
    });
  };
  return <button onClick={handleClick}>{isPending ? 'Updating...' : count}</button>;
}
```

Deep Insight:
- **Concurrent Rendering**: Enables interruptible and resumable work
- **Priority-based**: Higher priority updates can interrupt lower priority ones
- **Better Performance**: Improves app responsiveness and performance
- **Backwards Compatible**: Existing code works without changes
- **Future-proof**: Enables new features like Suspense and Transitions

---

## 68) How does Fiber improve reconciliation and rendering?

Concept:
Fiber breaks work into small units that can be interrupted, prioritized, and resumed, enabling concurrent features and better performance.

Example:
```jsx
// Fiber work loop (simplified)
function workLoop(deadline) {
  while (nextUnitOfWork && !shouldYield()) {
    nextUnitOfWork = performUnitOfWork(nextUnitOfWork);
  }
  if (nextUnitOfWork) {
    requestIdleCallback(workLoop);
  }
}
```

Deep Insight:
- **Work Units**: Breaks work into small, interruptible units
- **Time Slicing**: Uses requestIdleCallback for better performance
- **Priority System**: Different priorities for different types of updates
- **Incremental Rendering**: Can render parts of the tree incrementally
- **Better UX**: Keeps UI responsive during heavy operations

---

## 68) What is reconciliation and how does React decide what to re-render?

Concept:
Reconciliation is React's algorithm for comparing the current and previous virtual DOM trees to determine what changes need to be made to the real DOM.

Example:
```jsx
// Before update
const oldVDOM = {
  type: 'div',
  props: { className: 'container' },
  children: [
    { type: 'h1', props: { children: 'Hello' } }
  ]
};

// After update
const newVDOM = {
  type: 'div',
  props: { className: 'container' },
  children: [
    { type: 'h1', props: { children: 'Hello World' } }
  ]
};
```

Deep Insight:
- **Diffing Algorithm**: Compares virtual DOM trees to find differences
- **Minimal Updates**: Only updates the parts that actually changed
- **Key Optimization**: Uses keys to optimize list updates
- **Batched Updates**: Groups multiple updates into single DOM operation
- **Performance**: Enables React's high performance despite frequent updates

---

## 68) What are React Portals and when should you use them?

Concept:
React Portals allow rendering children into a DOM node outside the parent component, commonly used for modals, tooltips, and overlays.

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

Deep Insight:
- **DOM Rendering**: Renders children into different DOM node
- **Event Bubbling**: Events still bubble up through React component tree
- **Use Cases**: Modals, tooltips, overlays, notifications
- **Z-index Issues**: Solves z-index and positioning problems
- **Accessibility**: Better for screen readers and keyboard navigation

---

## 68) What are Error Boundaries and how do they work?

Concept:
Error Boundaries are React components that catch JavaScript errors anywhere in the child component tree, log errors, and display fallback UI.

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
```

Deep Insight:
- **Error Catching**: Catch JavaScript errors in child components
- **Fallback UI**: Display fallback UI when errors occur
- **Error Logging**: Log errors for debugging and monitoring
- **Class Components**: Only class components can be error boundaries
- **Limitations**: Don't catch errors in event handlers, async code, or during rendering

---

## 68) What are Higher-Order Components (HOCs) and Render Props?

Concept:
HOCs are functions that take a component and return a new component, while Render Props use a function prop to share code between components.

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

// Usage
function App() {
  return (
    <DataFetcher 
      render={(data) => data ? <div>{data.name}</div> : <div>Loading...</div>} 
    />
  );
}
```

Deep Insight:
- **HOCs**: Functions that enhance components with additional functionality
- **Render Props**: Pattern using function props to share code
- **Code Reuse**: Both patterns enable code reuse between components
- **Composition**: Render props are more flexible and composable
- **Hooks**: Modern alternative to both patterns

---

## 68) What is the purpose of Strict Mode in debugging React applications?

Concept:
Strict Mode is a development tool that double-renders components to detect side effects, helping identify issues that might cause problems in production.

Example:
```jsx
import { StrictMode } from 'react';

function App() {
  return (
    <StrictMode>
      <MyComponent />
    </StrictMode>
  );
}
```

Deep Insight:
- **Development Only**: Only affects development builds
- **Double Rendering**: Components render twice to detect side effects
- **Side Effect Detection**: Helps find issues with effects and state
- **Production Safe**: No impact on production builds
- **Best Practices**: Encourages writing side-effect-free components

---

## 68) What are refs and how is ref forwarding implemented?

Concept:
Refs provide access to DOM elements or component instances, with ref forwarding allowing parent components to access child component refs.

Example:
```jsx
import { forwardRef, useRef } from 'react';

// Ref forwarding
const FancyInput = forwardRef((props, ref) => {
  return <input ref={ref} {...props} />;
});

// Usage
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

Deep Insight:
- **DOM Access**: Access DOM elements directly
- **Ref Forwarding**: Pass refs through component boundaries
- **useImperativeHandle**: Customize ref value exposed to parent
- **Use Cases**: Focus management, animations, third-party libraries
- **Performance**: Avoid overusing refs, prefer declarative approaches

---

## 68) What is the difference between controlled and uncontrolled components?

Concept:
Controlled components have their value managed by React state, while uncontrolled components have their value managed directly by the DOM, with refs used to access the current value.

Example:
```jsx
// Controlled component - value managed by React state
function ControlledInput() {
  const [value, setValue] = useState('');
  
  const handleChange = (e) => {
    setValue(e.target.value);
  };
  
  return <input value={value} onChange={handleChange} />;
}

// Uncontrolled component - value managed by DOM
function UncontrolledInput() {
  const inputRef = useRef();
  
  const handleClick = () => {
    console.log(inputRef.current.value);
  };
  
  return <input ref={inputRef} defaultValue="hello" onClick={handleClick} />;
}
```

Deep Insight:
- **Controlled**: Value controlled by React state, single source of truth
- **Uncontrolled**: Value managed by DOM, accessed via refs
- **Use Cases**: Controlled for forms, uncontrolled for simple inputs
- **Validation**: Controlled components enable easier validation
- **Performance**: Uncontrolled can be more performant for simple cases

---

## 68) What is the React Profiler API and when is it used?

Concept:
The React Profiler API measures component rendering performance, helping identify slow components and optimize React applications.

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

Deep Insight:
- **Performance Measurement**: Measures component render times
- **Development Tool**: Primarily used during development
- **Optimization**: Helps identify performance bottlenecks
- **Profiling Data**: Provides detailed timing information
- **Production**: Can be used in production for monitoring

---
