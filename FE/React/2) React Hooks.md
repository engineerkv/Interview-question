# 🪝 2. React Hooks (Q11–27)

---

## 11) What are React Hooks and why were they introduced?

Hooks let functional components use state and lifecycle features. They solve class component problems and enable code reuse.

```jsx
function Counter() {
  const [count, setCount] = useState(0);
  useEffect(() => {
    document.title = `Count: ${count}`;
  });
  return <button onClick={() => setCount(c => c + 1)}>Count: {count}</button>;
}
```

- **Core Purpose**: Bring state and lifecycle to functional components without classes
- **Real-World Benefit**: Custom hooks let you share stateful logic across components easily
- **Common Mistake**: Calling hooks inside loops, conditions, or nested functions breaks React's rules
- **Code Reuse**: Extract logic into custom hooks instead of HOCs or render props
- **Interview Tip**: Explain that hooks solve the "wrapper hell" problem from HOCs and make code more readable

---

## 12) Explain how `useState` works internally.

useState returns state value and setter. React tracks hooks in a linked list, maintaining order between renders.

```jsx
const [count, setCount] = useState(0);
const [name, setName] = useState('');
return <div><div>{count}</div><input value={name} onChange={e => setName(e.target.value)} /></div>;
```

- **Internal Mechanism**: React stores hooks in a linked list per component, order must stay consistent
- **Real-World Implication**: Hooks must be called in same order every render, no conditional hooks
- **Common Mistake**: Calling hooks conditionally or in loops breaks React's internal tracking
- **Optimization**: Pass function to useState for expensive initial values: useState(() => expensive())
- **Interview Tip**: Explain that React uses a linked list to track hooks, which is why order matters

---

## 13) How does `useEffect` work and what is the role of its dependency array?

useEffect runs side effects after render. The dependency array controls when it runs: empty means once, missing means every render.

```jsx
const [user, setUser] = useState(null);
useEffect(() => { fetchUser(userId).then(setUser); }, [userId]);
return <div>{user ? user.name : 'Loading...'}</div>;
```

- **Execution Timing**: Runs after DOM updates complete, not during render
- **Dependency Array**: Effect re-runs when dependencies change, empty array means mount only
- **Common Mistake**: Missing dependencies causes stale closures and bugs
- **Cleanup Function**: Return function from effect to clean up subscriptions, timers, or listeners
- **Interview Tip**: Explain useEffect as "componentDidMount + componentDidUpdate + componentWillUnmount" in one hook

---

## 14) What is the difference between `useEffect` and `useLayoutEffect`?

useEffect runs after paint, useLayoutEffect runs before paint. Use useLayoutEffect to prevent visual flicker.

```jsx
const [position, setPosition] = useState({ top: 0, left: 0 });
const tooltipRef = useRef();
useLayoutEffect(() => {
  const rect = tooltipRef.current.getBoundingClientRect();
  setPosition({ top: rect.bottom + 8, left: rect.left });
}, [children]);
```

- **Key Difference**: useLayoutEffect blocks paint, useEffect doesn't
- **Real-World Use**: useLayoutEffect for DOM measurements before user sees the screen
- **Common Mistake**: Using useLayoutEffect for everything slows down rendering unnecessarily
- **Performance Trade-off**: useLayoutEffect can block rendering, use sparingly
- **Interview Tip**: Default to useEffect, only use useLayoutEffect when you see visual flicker

---

## 15) What is `useRef` and what are its common use cases?

useRef returns a mutable object that persists across renders. Use it for DOM access and values that don't need re-renders.

```jsx
const inputRef = useRef();
const countRef = useRef(0);
const [count, setCount] = useState(0);
return <div><input ref={inputRef} /><button onClick={() => inputRef.current.focus()}>Focus</button></div>;
```

- **Core Feature**: Changing .current doesn't trigger re-renders, unlike state
- **Real-World Use**: DOM element access, storing previous values, timer IDs, or any mutable value
- **Common Mistake**: Using refs for values that should trigger UI updates (use state instead)
- **Optimization**: Refs are perfect for values that change but don't need to re-render component
- **Interview Tip**: Explain refs as "state that doesn't cause re-renders" for DOM access and mutable values

---

## 16) What is the difference between refs and state?

State changes trigger re-renders. Refs don't trigger re-renders but persist across renders.

```jsx
const [count, setCount] = useState(0);
const renderCount = useRef(0);
useEffect(() => { renderCount.current += 1; });
return <div>Renders: {renderCount.current} Count: {count}</div>;
```

- **Key Difference**: State changes cause UI updates, ref changes don't
- **Real-World Use**: State for UI data, refs for DOM access, timers, or previous values
- **Common Mistake**: Using state for values that don't need UI updates wastes performance
- **Optimization**: Use refs for values that change but shouldn't trigger re-renders
- **Interview Tip**: Explain that refs are like "state that doesn't cause re-renders" for performance optimization

---

## 17) What is `useCallback` and when should you use it?

useCallback memoizes a function so it only changes when dependencies change. Use it to prevent child re-renders.

```jsx
const [count, setCount] = useState(0);
const [name, setName] = useState('');
const onIncrement = useCallback(() => setCount(c => c + 1), []);
return <Child onIncrement={onIncrement} name={name} />;
```

- **Core Purpose**: Memoize function references to prevent unnecessary child re-renders
- **Real-World Use**: Pass callbacks to React.memo components or as dependencies to other hooks
- **Common Mistake**: Using useCallback everywhere - it adds overhead without benefit if not needed
- **Optimization**: Only use when you have performance issues with child re-renders
- **Interview Tip**: Explain that useCallback is about reference equality, not function execution

---

## 18) What is `useMemo` and how does it help with performance?

useMemo caches a computed value, recalculating only when dependencies change. Use it for expensive calculations.

```jsx
const filteredItems = useMemo(() => {
  return items.filter(item => item.name.toLowerCase().includes(filter.toLowerCase()));
}, [items, filter]);
return <ul>{filteredItems.map(i => <li key={i.id}>{i.name}</li>)}</ul>;
```

- **Core Purpose**: Memoize expensive calculations to avoid recomputing on every render
- **Real-World Use**: Filtering large lists, complex calculations, or creating new objects/arrays
- **Common Mistake**: Memoizing simple values - the overhead isn't worth it for primitives
- **Optimization**: Only use when calculation is expensive or creates new object references
- **Interview Tip**: Explain that useMemo is about computation cost, not just preventing re-renders

---

## 19) What is `useReducer` and when is it better than `useState`?

useReducer manages complex state with a reducer function. Better than useState when state logic is complex.

```jsx
const reducer = (state, action) => {
  switch (action.type) {
    case 'increment': return { ...state, count: state.count + state.step };
    default: return state;
  }
};
const [state, dispatch] = useReducer(reducer, { count: 0, step: 1 });
return <button onClick={() => dispatch({ type: 'increment' })}>Count: {state.count}</button>;
```

- **Core Purpose**: Manage complex state with predictable updates through reducer pattern
- **Real-World Use**: Forms with multiple fields, state machines, or complex state transitions
- **Common Mistake**: Using useReducer for simple state - useState is simpler when you don't need reducers
- **Testing Benefit**: Reducer functions are pure and easy to test in isolation
- **Interview Tip**: Explain that useReducer is like useState but for complex state logic, similar to Redux pattern

---

## 20) What is the `useContext` hook and how does it relate to the Context API?

useContext reads context values in functional components. It works with Context.Provider to share data.

```jsx
const ThemeContext = createContext();
function ThemeProvider({ children }) {
  const [theme, setTheme] = useState('light');
  return <ThemeContext.Provider value={{ theme, setTheme }}>{children}</ThemeContext.Provider>;
}
function ThemedButton() {
  const { theme, setTheme } = useContext(ThemeContext);
  return <button onClick={() => setTheme(theme === 'light' ? 'dark' : 'light')}>Toggle Theme</button>;
}
```

- **Core Purpose**: Consume context values without prop drilling through multiple components
- **Real-World Use**: Themes, user data, language settings, or any global app state
- **Common Mistake**: Creating new context values every render causes all consumers to re-render
- **Optimization**: Memoize context value with useMemo to prevent unnecessary re-renders
- **Interview Tip**: Explain that Context solves prop drilling but can cause performance issues if overused

---

## 21) What is `useImperativeHandle` and where is it used?

useImperativeHandle customizes what ref exposes to parent components. Must be used with forwardRef.

```jsx
const FancyInput = forwardRef((props, ref) => {
  const inputRef = useRef();
  useImperativeHandle(ref, () => ({
    focus: () => inputRef.current.focus(),
    clear: () => inputRef.current.value = ''
  }));
  return <input ref={inputRef} {...props} />;
});
```

- **Core Purpose**: Expose specific methods to parent instead of entire DOM element
- **Real-World Use**: Form libraries, animation controls, or custom input components
- **Common Mistake**: Using when declarative props would work better - prefer declarative approach
- **Encapsulation**: Hides internal implementation while exposing controlled API
- **Interview Tip**: Explain that this hook is for imperative APIs when declarative isn't enough

---

## 22) What is `useDebugValue` and what is it used for?

useDebugValue adds labels to custom hooks in React DevTools. Only visible during development.

```jsx
function useCounter(initialValue = 0) {
  const [count, setCount] = useState(initialValue);
  useDebugValue(count > 10 ? 'High' : 'Low');
  const increment = useCallback(() => setCount(c => c + 1), []);
  return { count, increment };
}
```

- **Core Purpose**: Display helpful labels in DevTools for custom hooks
- **Real-World Use**: Debugging complex custom hooks with multiple states
- **Common Mistake**: Using for production code - it's automatically stripped in production
- **Optimization**: Pass function for expensive debug values: useDebugValue(() => expensive())
- **Interview Tip**: Mention that this is a development tool only, helps debug custom hooks

---

## 23) What are custom hooks and why would you create one?

Custom hooks are functions using other hooks, named with "use". Extract reusable stateful logic.

```jsx
function useApi(url) {
  const [data, setData] = useState(null);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState(null);
  useEffect(() => {
    fetch(url).then(r => r.json()).then(data => { setData(data); setLoading(false); }).catch(e => { setError(e); setLoading(false); });
  }, [url]);
  return { data, loading, error };
}
```

- **Core Purpose**: Share stateful logic between components without HOCs or render props
- **Real-World Use**: Data fetching, form handling, authentication, or any repeated logic
- **Common Mistake**: Not following "use" naming convention breaks React's rules
- **Composition**: Can combine multiple hooks to create powerful abstractions
- **Interview Tip**: Explain that custom hooks are the modern way to share logic, replacing HOCs

---

## 24) What are `useTransition` and `useDeferredValue` used for in concurrent rendering?

useTransition marks updates as non-urgent. useDeferredValue defers value updates. Both keep UI responsive.

```jsx
const [isPending, startTransition] = useTransition();
const deferredQuery = useDeferredValue(query);
useEffect(() => {
  if (deferredQuery) startTransition(() => setResults(expensiveSearch(deferredQuery)));
}, [deferredQuery]);
```

- **Core Purpose**: Keep UI responsive during heavy updates by marking them as low priority
- **Real-World Use**: Search results, filtering large lists, or any expensive rendering
- **Common Mistake**: Using for urgent updates - they're meant for non-urgent background work
- **Optimization**: Allows React to interrupt heavy work and respond to user input
- **Interview Tip**: Explain that these hooks enable concurrent rendering in React 18+

---

## 25) What is `useId` and when is it helpful?

useId generates unique IDs stable across server and client. Essential for accessibility and form labels.

```jsx
const id = useId();
return <div><label htmlFor={id}>{label}</label><input id={id} type={type} /></div>;
```

- **Core Purpose**: Generate stable, unique IDs for form labels and ARIA attributes
- **Real-World Use**: Form inputs, accessibility attributes, or any place needing unique IDs
- **Common Mistake**: Using Math.random() or Date.now() breaks with SSR and hydration
- **SSR Safety**: Ensures same ID on server and client, preventing hydration mismatches
- **Interview Tip**: Explain that useId solves the ID generation problem in SSR applications

---

## 26) What is `useSyncExternalStore` and what problem does it solve?

useSyncExternalStore subscribes to external stores safely during concurrent rendering. Prevents hydration mismatches.

```jsx
function useLocalStorage(key, defaultValue) {
  return useSyncExternalStore(
    (callback) => {
      window.addEventListener('storage', callback);
      return () => window.removeEventListener('storage', callback);
    },
    () => localStorage.getItem(key) ? JSON.parse(localStorage.getItem(key)) : defaultValue,
    () => defaultValue
  );
}
```

- **Core Purpose**: Safely subscribe to external stores (Redux, Zustand, localStorage) during concurrent rendering
- **Real-World Use**: State management libraries, browser APIs, or any external data source
- **Common Mistake**: Using regular hooks with external stores causes hydration mismatches in SSR
- **Concurrent Safety**: Ensures consistent reads during React's concurrent rendering
- **Interview Tip**: Explain that this hook is what libraries like Redux use internally for React 18+

---

## 27) What is `useInsertionEffect` and how does it differ from `useLayoutEffect`?

useInsertionEffect runs before DOM mutations, earlier than useLayoutEffect. Used by CSS-in-JS libraries.

```jsx
useInsertionEffect(() => {
  const styleId = `style-${color}`;
  if (!document.getElementById(styleId)) {
    const style = document.createElement('style');
    style.id = styleId;
    style.textContent = `.styled-${color} { color: ${color}; }`;
    document.head.appendChild(style);
  }
}, [color]);
```

- **Core Purpose**: Inject styles before DOM mutations to prevent visual flicker
- **Real-World Use**: CSS-in-JS libraries like styled-components, emotion, or any style injection
- **Common Mistake**: Using for regular effects - this is specialized for style injection
- **Performance**: Runs synchronously before layout to ensure styles are ready
- **Interview Tip**: Explain that this hook is mainly for library authors, not everyday use

---
