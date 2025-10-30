# 🪝 2. React Hooks (Q11–27)

---

## 11) What are React Hooks and why were they introduced?

Concept:
React Hooks are functions that allow you to use state and other React features in functional components, introduced to solve problems with class components and enable better code reuse.

Example:
```jsx
function Counter() {
  const [count, setCount] = useState(0);
  useEffect(() => {
    document.title = `Count: ${count}`;
  });
  return <button onClick={() => setCount(c => c + 1)}>Count: {count}</button>;
}
```

Deep Insight:
- **Functional Components**: Enable state and lifecycle in functional components
- **Code Reuse**: Allow sharing stateful logic between components
- **Simpler Logic**: Easier to understand and test than class components
- **No Classes**: Eliminate need for class components in most cases
- **Rules**: Must be called at top level, not inside loops or conditions

---

## 12) Explain how `useState` works internally.

Concept:
`useState` is a Hook that returns an array with the current state value and a setter function, using a linked list to track state updates in functional components.

Example:
```jsx
function Counter() {
  const [count, setCount] = useState(0);
  const [name, setName] = useState('');
  
  return (
    <div>
      <div>{count}</div>
      <input value={name} onChange={e => setName(e.target.value)} />
    </div>
  );
}
```

Deep Insight:
- **Linked List**: React uses linked list to track hooks in order
- **State Array**: Each component has its own state array
- **Setter Function**: Returns same function reference on re-renders
- **Batching**: Multiple setState calls are batched together
- **Lazy Initialization**: Can pass function to useState for expensive initial values

---

## 13) How does `useEffect` work and what is the role of its dependency array?

Concept:
`useEffect` runs side effects after render, with a dependency array controlling when the effect runs - empty array means run once, no array means run every render.

Example:
```jsx
function UserProfile({ userId }) {
  const [user, setUser] = useState(null);
  
  // Runs only once (on mount)
  useEffect(() => {
    fetchUser(userId).then(setUser);
  }, [userId]);
  return <div>{user ? user.name : 'Loading...'}</div>;
}
```

Deep Insight:
- **After Render**: Runs after DOM updates are committed
- **Dependency Array**: Controls when effect runs based on dependencies
- **Cleanup**: Can return cleanup function to prevent memory leaks
- **Async Effects**: Can use async functions inside useEffect
- **Multiple Effects**: Can have multiple useEffect hooks in one component

---

## 14) What is the difference between `useEffect` and `useLayoutEffect`?

Concept:
`useEffect` runs asynchronously after paint, while `useLayoutEffect` runs synchronously before paint, useful for DOM measurements and preventing visual flicker.

Example:
```jsx
function Tooltip({ children, text }) {
  const [position, setPosition] = useState({ top: 0, left: 0 });
  const tooltipRef = useRef();
  
  useLayoutEffect(() => {
    const rect = tooltipRef.current.getBoundingClientRect();
    setPosition({ top: rect.bottom + 8, left: rect.left });
  }, [children]);
  
  return (
    <div ref={tooltipRef} style={{ position: 'absolute', top: position.top, left: position.left }}>
      {text}
    </div>
  );
}
```

Deep Insight:
- **Timing**: useLayoutEffect runs before paint, useEffect after
- **Synchronous**: useLayoutEffect blocks paint until it completes
- **Use Cases**: useLayoutEffect for DOM measurements, useEffect for side effects
- **Performance**: useLayoutEffect can block rendering if not careful
- **Server Rendering**: Both work the same way during SSR

---

## 15) What is `useRef` and what are its common use cases?

Concept:
`useRef` returns a mutable ref object that persists across renders, commonly used for accessing DOM elements, storing previous values, and avoiding re-renders.

Example:
```jsx
function FocusInput() {
  const inputRef = useRef();
  const countRef = useRef(0);
  const [count, setCount] = useState(0);
  
  return (
    <div>
      <input ref={inputRef} />
      <button onClick={() => inputRef.current.focus()}>Focus</button>
      <button onClick={() => { countRef.current++; setCount(c => c + 1); }}>Inc</button>
      <div>Clicked: {countRef.current}</div>
    </div>
  );
}
```

Deep Insight:
- **Mutable Object**: Can mutate .current property without re-renders
- **Persistent**: Ref object persists across component re-renders
- **DOM Access**: Primary use case for accessing DOM elements
- **Previous Values**: Can store previous values for comparison
- **No Re-renders**: Changing .current doesn't trigger component re-render

---

## 16) What is the difference between refs and state?

Concept:
Refs don't trigger re-renders when changed and persist across renders, while state triggers re-renders and can be used to store data that affects the UI.

Example:
```jsx
function Counter() {
  const [count, setCount] = useState(0);
  const renderCount = useRef(0);
  
  useEffect(() => { renderCount.current += 1; });
  
  return <div>Renders: {renderCount.current} Count: {count}</div>;
}
```

Deep Insight:
- **Re-renders**: State changes trigger re-renders, refs don't
- **UI Updates**: State changes cause UI updates, refs don't
- **Persistence**: Both persist across renders
- **Use Cases**: State for UI data, refs for DOM access and non-UI data
- **Performance**: Refs are better for values that don't need UI updates

---

## 17) What is `useCallback` and when should you use it?

Concept:
`useCallback` returns a memoized callback function that only changes if dependencies change, used to prevent unnecessary re-renders of child components.

Example:
```jsx
function Parent() {
  const [count, setCount] = useState(0);
  const [name, setName] = useState('');
  const onIncrement = useCallback(() => setCount(c => c + 1), []);
  return <Child onIncrement={onIncrement} name={name} />;
}
```

Deep Insight:
- **Memoization**: Caches function reference based on dependencies
- **Dependencies**: Function recreates when dependencies change
- **Performance**: Prevents unnecessary re-renders of child components
- **Use Cases**: Callbacks passed to memoized components
- **Overuse**: Don't use unless you have performance issues

---

## 18) What is `useMemo` and how does it help with performance?

Concept:
`useMemo` returns a memoized value that only recalculates when dependencies change, used to optimize expensive calculations and prevent unnecessary computations.

Example:
```jsx
function ExpensiveComponent({ items, filter }) {
  // Expensive calculation - only runs when items or filter change
  const filteredItems = useMemo(() => {
    console.log('Filtering items...');
    return items.filter(item => 
      item.name.toLowerCase().includes(filter.toLowerCase())
    );
  }, [items, filter]);
  return <ul>{filteredItems.map(i => <li key={i.id}>{i.name}</li>)}</ul>;
}
```

Deep Insight:
- **Memoization**: Caches computed value based on dependencies
- **Dependencies**: Value recalculates when dependencies change
- **Performance**: Prevents expensive calculations on every render
- **Use Cases**: Expensive calculations, object/array creation
- **Overuse**: Don't use for simple calculations or primitive values

---

## 19) What is `useReducer` and when is it better than `useState`?

Concept:
`useReducer` is a Hook for managing complex state logic with a reducer function, better than `useState` when state logic is complex or involves multiple sub-values.

Example:
```jsx
const initialState = { count: 0, step: 1 };

function reducer(state, action) {
  switch (action.type) {
    case 'increment':
      return { ...state, count: state.count + state.step };
    default:
      return state;
  }
}

function Counter() {
  const [state, dispatch] = useReducer(reducer, initialState);
  return (
    <button onClick={() => dispatch({ type: 'increment' })}>
      Count: {state.count}
    </button>
  );
}
```

Deep Insight:
- **Complex State**: Better for complex state with multiple sub-values
- **Predictable Updates**: State updates follow reducer pattern
- **Actions**: State changes through action objects
- **Testing**: Reducer functions are easier to test
- **Performance**: Can optimize with useCallback for dispatch

---

## 20) What is the `useContext` hook and how does it relate to the Context API?

Concept:
`useContext` is a Hook that subscribes to React context changes, providing a way to consume context values in functional components without nesting.

Example:
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
  return (
    <button onClick={() => setTheme(theme === 'light' ? 'dark' : 'light')}>
      Toggle Theme
    </button>
  );
}
```

Deep Insight:
- **Context Consumption**: Easy way to consume context in functional components
- **Re-renders**: Component re-renders when context value changes
- **Multiple Contexts**: Can use multiple useContext hooks
- **Performance**: Can cause unnecessary re-renders if not optimized
- **Provider Pattern**: Works with Context.Provider for value distribution

---

## 21) What is `useImperativeHandle` and where is it used?

Concept:
`useImperativeHandle` customizes the instance value exposed to parent components when using refs, commonly used with `forwardRef` for imperative APIs.

Example:
```jsx
const FancyInput = forwardRef((props, ref) => {
  const inputRef = useRef();
  
  useImperativeHandle(ref, () => ({
    focus: () => {
      inputRef.current.focus();
    },
    clear: () => {
      inputRef.current.value = '';
    }
  }));
  
  return <input ref={inputRef} {...props} />;
});
```

Deep Insight:
- **Imperative API**: Exposes specific methods to parent components
- **forwardRef**: Must be used with forwardRef to work properly
- **Custom Methods**: Can define custom methods beyond DOM methods
- **Encapsulation**: Hides internal implementation details
- **Use Cases**: Form libraries, animation libraries, custom input components

---

## 22) What is `useDebugValue` and what is it used for?

Concept:
`useDebugValue` displays a label for custom hooks in React DevTools, helping with debugging and development of custom hooks.

Example:
```jsx
function useCounter(initialValue = 0) {
  const [count, setCount] = useState(initialValue);
  
  // Only shows in development
  useDebugValue(count > 10 ? 'High' : 'Low');
  
  const increment = useCallback(() => {
    setCount(c => c + 1);
  }, []);
  
  return { count, increment };
}
```

Deep Insight:
- **DevTools**: Only visible in React DevTools during development
- **Custom Hooks**: Primarily used for debugging custom hooks
- **Conditional Values**: Can use functions for expensive debug values
- **Development Only**: Automatically removed in production builds
- **Debugging**: Helps understand hook state and behavior

---

## 23) What are custom hooks and why would you create one?

Concept:
Custom hooks are JavaScript functions that use other hooks, created to extract and reuse stateful logic between components, following the "use" naming convention.

Example:
```jsx
// Custom hook for API data fetching
function useApi(url) {
  const [data, setData] = useState(null);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState(null);
  
  useEffect(() => {
    fetch(url)
      .then(response => response.json())
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

Deep Insight:
- **Logic Reuse**: Extract and share stateful logic between components
- **Naming Convention**: Must start with "use" to follow rules of hooks
- **Composition**: Can use other hooks inside custom hooks
- **Testing**: Easier to test logic in isolation
- **Abstraction**: Hide complex logic behind simple interface

---

## 24) What are `useTransition` and `useDeferredValue` used for in concurrent rendering?

Concept:
`useTransition` marks state updates as non-urgent, while `useDeferredValue` defers updating a value, both used to improve UI responsiveness during heavy updates.

Example:
```jsx
function SearchResults({ query }) {
  const [isPending, startTransition] = useTransition();
  const [results, setResults] = useState([]);
  
  const deferredQuery = useDeferredValue(query);
  
  useEffect(() => {
    if (deferredQuery) {
      startTransition(() => {
        const newResults = expensiveSearch(deferredQuery);
        setResults(newResults);
      });
    }
  }, [deferredQuery]);
  
  return (
    <div>
      {isPending && <div>Searching...</div>}
      {results.map(result => (
        <div key={result.id}>{result.title}</div>
      ))}
    </div>
  );
}
```

Deep Insight:
- **Concurrent Rendering**: Part of React 18's concurrent features
- **Non-blocking**: Allows UI to stay responsive during heavy updates
- **Priority**: useTransition marks updates as low priority
- **Deferred Updates**: useDeferredValue delays value updates
- **User Experience**: Prevents UI from freezing during heavy operations

---

## 25) What is `useId` and when is it helpful?

Concept:
`useId` generates unique IDs that are stable across server and client rendering, helpful for accessibility attributes and form labels.

Example:
```jsx
function FormField({ label, type = "text" }) {
  const id = useId();
  
  return (
    <div>
      <label htmlFor={id}>{label}</label>
      <input id={id} type={type} />
    </div>
  );
}
```

Deep Insight:
- **Unique IDs**: Generates unique, stable IDs for each component instance
- **SSR Safe**: Works correctly with server-side rendering
- **Accessibility**: Essential for proper form labels and ARIA attributes
- **Stable**: IDs remain consistent across re-renders
- **No Conflicts**: Prevents ID conflicts in complex applications

---

## 26) What is `useSyncExternalStore` and what problem does it solve?

Concept:
`useSyncExternalStore` subscribes to external data sources and ensures consistent reads during concurrent rendering, solving hydration mismatches.

Example:
```jsx
function useLocalStorage(key, defaultValue) {
  return useSyncExternalStore(
    // Subscribe function
    (callback) => {
      window.addEventListener('storage', callback);
      return () => window.removeEventListener('storage', callback);
    },
    // Get snapshot function
    () => {
      const value = localStorage.getItem(key);
      return value ? JSON.parse(value) : defaultValue;
    },
    // Server snapshot function
    () => defaultValue
  );
}
```

Deep Insight:
- **External Stores**: Designed for subscribing to external data sources
- **Concurrent Safe**: Ensures consistent reads during concurrent rendering
- **Hydration**: Prevents hydration mismatches between server and client
- **Snapshot Functions**: Provides server and client snapshot functions
- **Third-party Libraries**: Used by libraries like Redux, Zustand

---

## 27) What is `useInsertionEffect` and how does it differ from `useLayoutEffect`?

Concept:
`useInsertionEffect` runs before DOM mutations, while `useLayoutEffect` runs after, commonly used for CSS-in-JS libraries to inject styles.

Example:
```jsx
function StyledComponent({ children, color }) {
  const [styles, setStyles] = useState('');
  
  // Runs before DOM mutations
  useInsertionEffect(() => {
    const styleId = `style-${color}`;
    if (!document.getElementById(styleId)) {
      const style = document.createElement('style');
      style.id = styleId;
      style.textContent = `.styled-${color} { color: ${color}; }`;
      document.head.appendChild(style);
    }
  }, [color]);
  
  return <div className={`styled-${color}`}>{children}</div>;
}
```

Deep Insight:
- **Timing**: Runs before DOM mutations, earlier than useLayoutEffect
- **CSS-in-JS**: Primarily designed for CSS-in-JS libraries
- **Style Injection**: Perfect for injecting styles before DOM updates
- **Performance**: Prevents visual flicker during style updates
- **Use Cases**: Styled-components, emotion, other CSS-in-JS libraries

---
