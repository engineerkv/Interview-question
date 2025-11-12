# 🪝 2. React Hooks (Q12–28)

---

## 🧩 Q12. What are React Hooks and why were they introduced?

### 🧠 Concept

Hooks let functional components use state and lifecycle features without classes. They solve class component complexity and enable better code reuse through custom hooks.

---

### 💡 Example

```jsx
function Counter() {
  const [count, setCount] = useState(0);
  useEffect(() => {
    document.title = `Count: ${count}`;
  });
  return <button onClick={() => setCount(c => c + 1)}>Count: {count}</button>;
}
```

---

### 🔍 Deep Insights

* **Rule:** Hooks bring state and lifecycle to functional components without classes.
* **Use Case:** Custom hooks let you share stateful logic across components easily, replacing HOCs and render props.
* **Common Mistake:** Calling hooks inside loops, conditions, or nested functions breaks React's rules.
* **Pro Tip:** Extract logic into custom hooks instead of HOCs or render props to avoid "wrapper hell."

---

### ⭐ Senior Takeaway

Hooks solve the "wrapper hell" problem from HOCs and make code more readable and maintainable.

---

## 🧩 Q13. Explain how `useState` works internally.

### 🧠 Concept

useState returns state value and setter. React tracks hooks in a linked list per component, maintaining order between renders to ensure consistency.

---

### 💡 Example

```jsx
const [count, setCount] = useState(0);
const [name, setName] = useState('');
return (
  <div>
    <div>{count}</div>
    <input value={name} onChange={e => setName(e.target.value)} />
  </div>
);
```

---

### 🔍 Deep Insights

* **Rule:** React stores hooks in a linked list per component, order must stay consistent.
* **Use Case:** Hooks must be called in same order every render, no conditional hooks.
* **Common Mistake:** Calling hooks conditionally or in loops breaks React's internal tracking.
* **Pro Tip:** Pass function to useState for expensive initial values: `useState(() => expensive())`.

---

### ⭐ Senior Takeaway

React uses a linked list to track hooks, which is why order matters and hooks must be unconditional.

---

## 🧩 Q14. How does `useEffect` work and what is the role of its dependency array?

### 🧠 Concept

useEffect runs side effects after render. The dependency array controls when it runs: empty means once on mount, missing means every render, with dependencies means when they change.

---

### 💡 Example

```jsx
const [user, setUser] = useState(null);
useEffect(() => {
  fetchUser(userId).then(setUser);
}, [userId]);
return <div>{user ? user.name : 'Loading...'}</div>;
```

---

### 🔍 Deep Insights

* **Rule:** Effect runs after DOM updates complete, not during render.
* **Use Case:** Dependency array controls re-runs—empty array means mount only, missing means every render.
* **Common Mistake:** Missing dependencies causes stale closures and bugs.
* **Pro Tip:** Return function from effect to clean up subscriptions, timers, or listeners.

---

### ⭐ Senior Takeaway

useEffect is "componentDidMount + componentDidUpdate + componentWillUnmount" in one hook.

---

## 🧩 Q15. What is the difference between `useEffect` and `useLayoutEffect`?

### 🧠 Concept

useEffect runs after paint, useLayoutEffect runs before paint. Use useLayoutEffect to prevent visual flicker when you need DOM measurements.

---

### 💡 Example

```jsx
const [position, setPosition] = useState({ top: 0, left: 0 });
const tooltipRef = useRef();
useLayoutEffect(() => {
  const rect = tooltipRef.current.getBoundingClientRect();
  setPosition({ top: rect.bottom + 8, left: rect.left });
}, [children]);
```

---

### 🔍 Deep Insights

* **Rule:** useLayoutEffect blocks paint, useEffect doesn't.
* **Use Case:** useLayoutEffect for DOM measurements before user sees the screen.
* **Common Mistake:** Using useLayoutEffect for everything slows down rendering unnecessarily.
* **Pro Tip:** Default to useEffect, only use useLayoutEffect when you see visual flicker.

---

### ⭐ Senior Takeaway

useLayoutEffect can block rendering—use sparingly, only when visual consistency matters.

---

## 🧩 Q16. What is `useRef` and what are its common use cases?

### 🧠 Concept

useRef returns a mutable object that persists across renders. Use it for DOM access and values that don't need re-renders when they change.

---

### 💡 Example

```jsx
const inputRef = useRef();
const countRef = useRef(0);
return (
  <div>
    <input ref={inputRef} />
    <button onClick={() => inputRef.current.focus()}>Focus</button>
  </div>
);
```

---

### 🔍 Deep Insights

* **Rule:** Changing `.current` doesn't trigger re-renders, unlike state.
* **Use Case:** DOM element access, storing previous values, timer IDs, or any mutable value.
* **Common Mistake:** Using refs for values that should trigger UI updates—use state instead.
* **Pro Tip:** Refs are perfect for values that change but don't need to re-render component.

---

### ⭐ Senior Takeaway

Refs are "state that doesn't cause re-renders" for DOM access and mutable values.

---

## 🧩 Q17. What is the difference between refs and state?

### 🧠 Concept

State changes trigger re-renders. Refs don't trigger re-renders but persist across renders, making them perfect for values that change but shouldn't update UI.

---

### 💡 Example

```jsx
const [count, setCount] = useState(0);
const renderCount = useRef(0);
useEffect(() => { renderCount.current += 1; });
return <div>Renders: {renderCount.current} Count: {count}</div>;
```

---

### 🔍 Deep Insights

* **Rule:** State changes cause UI updates, ref changes don't.
* **Use Case:** State for UI data, refs for DOM access, timers, or previous values.
* **Common Mistake:** Using state for values that don't need UI updates wastes performance.
* **Pro Tip:** Use refs for values that change but shouldn't trigger re-renders.

---

### ⭐ Senior Takeaway

Refs are like "state that doesn't cause re-renders" for performance optimization.

---

## 🧩 Q18. What is `useCallback` and when should you use it?

### 🧠 Concept

useCallback memoizes a function so it only changes when dependencies change. Use it to prevent child re-renders when passing callbacks to memoized components.

---

### 💡 Example

```jsx
const [count, setCount] = useState(0);
const [name, setName] = useState('');
const onIncrement = useCallback(() => setCount(c => c + 1), []);
return <Child onIncrement={onIncrement} name={name} />;
```

---

### 🔍 Deep Insights

* **Rule:** useCallback memoizes function references to prevent unnecessary child re-renders.
* **Use Case:** Pass callbacks to React.memo components or as dependencies to other hooks.
* **Common Mistake:** Using useCallback everywhere—it adds overhead without benefit if not needed.
* **Pro Tip:** Only use when you have performance issues with child re-renders.

---

### ⭐ Senior Takeaway

useCallback is about reference equality, not function execution—use only when needed.

---

## 🧩 Q19. What is `useMemo` and how does it help with performance?

### 🧠 Concept

useMemo caches a computed value, recalculating only when dependencies change. Use it for expensive calculations to avoid recomputing on every render.

---

### 💡 Example

```jsx
const filteredItems = useMemo(() => {
  return items.filter(item => 
    item.name.toLowerCase().includes(filter.toLowerCase())
  );
}, [items, filter]);
return <ul>{filteredItems.map(i => <li key={i.id}>{i.name}</li>)}</ul>;
```

---

### 🔍 Deep Insights

* **Rule:** useMemo memoizes expensive calculations to avoid recomputing on every render.
* **Use Case:** Filtering large lists, complex calculations, or creating new objects/arrays.
* **Common Mistake:** Memoizing simple values—the overhead isn't worth it for primitives.
* **Pro Tip:** Only use when calculation is expensive or creates new object references.

---

### ⭐ Senior Takeaway

useMemo is about computation cost, not just preventing re-renders—measure before optimizing.

---

## 🧩 Q20. What is `useReducer` and when is it better than `useState`?

### 🧠 Concept

useReducer manages complex state with a reducer function. Better than useState when state logic is complex or involves multiple related values.

---

### 💡 Example

```jsx
const reducer = (state, action) => {
  switch (action.type) {
    case 'increment': 
      return { ...state, count: state.count + state.step };
    default: 
      return state;
  }
};
const [state, dispatch] = useReducer(reducer, { count: 0, step: 1 });
return <button onClick={() => dispatch({ type: 'increment' })}>Count: {state.count}</button>;
```

---

### 🔍 Deep Insights

* **Rule:** useReducer manages complex state with predictable updates through reducer pattern.
* **Use Case:** Forms with multiple fields, state machines, or complex state transitions.
* **Common Mistake:** Using useReducer for simple state—useState is simpler when you don't need reducers.
* **Pro Tip:** Reducer functions are pure and easy to test in isolation.

---

### ⭐ Senior Takeaway

useReducer is like useState but for complex state logic, similar to Redux pattern.

---

## 🧩 Q21. What is the `useContext` hook and how does it relate to the Context API?

### 🧠 Concept

useContext reads context values in functional components. It works with Context.Provider to share data without prop drilling through multiple levels.

---

### 💡 Example

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

---

### 🔍 Deep Insights

* **Rule:** useContext consumes context values without prop drilling through multiple components.
* **Use Case:** Themes, user data, language settings, or any global app state.
* **Common Mistake:** Creating new context values every render causes all consumers to re-render.
* **Pro Tip:** Memoize context value with useMemo to prevent unnecessary re-renders.

---

### ⭐ Senior Takeaway

Context solves prop drilling but can cause performance issues if overused—use wisely.

---

## 🧩 Q22. What is `useImperativeHandle` and where is it used?

### 🧠 Concept

useImperativeHandle customizes what ref exposes to parent components. Must be used with forwardRef to create controlled APIs for parent components.

---

### 💡 Example

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

---

### 🔍 Deep Insights

* **Rule:** useImperativeHandle exposes specific methods to parent instead of entire DOM element.
* **Use Case:** Form libraries, animation controls, or custom input components.
* **Common Mistake:** Using when declarative props would work better—prefer declarative approach.
* **Pro Tip:** Hides internal implementation while exposing controlled API.

---

### ⭐ Senior Takeaway

This hook is for imperative APIs when declarative isn't enough—use sparingly.

---

## 🧩 Q23. What is `useDebugValue` and what is it used for?

### 🧠 Concept

useDebugValue adds labels to custom hooks in React DevTools. Only visible during development, automatically stripped in production builds.

---

### 💡 Example

```jsx
function useCounter(initialValue = 0) {
  const [count, setCount] = useState(initialValue);
  useDebugValue(count > 10 ? 'High' : 'Low');
  const increment = useCallback(() => setCount(c => c + 1), []);
  return { count, increment };
}
```

---

### 🔍 Deep Insights

* **Rule:** useDebugValue displays helpful labels in DevTools for custom hooks.
* **Use Case:** Debugging complex custom hooks with multiple states.
* **Common Mistake:** Using for production code—it's automatically stripped in production.
* **Pro Tip:** Pass function for expensive debug values: `useDebugValue(() => expensive())`.

---

### ⭐ Senior Takeaway

This is a development tool only—helps debug custom hooks in DevTools.

---

## 🧩 Q24. What are custom hooks and why would you create one?

### 🧠 Concept

Custom hooks are functions using other hooks, named with "use". Extract reusable stateful logic to share between components without HOCs or render props.

---

### 💡 Example

```jsx
function useApi(url) {
  const [data, setData] = useState(null);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState(null);
  useEffect(() => {
    fetch(url)
      .then(r => r.json())
      .then(data => { setData(data); setLoading(false); })
      .catch(e => { setError(e); setLoading(false); });
  }, [url]);
  return { data, loading, error };
}
```

---

### 🔍 Deep Insights

* **Rule:** Custom hooks share stateful logic between components without HOCs or render props.
* **Use Case:** Data fetching, form handling, authentication, or any repeated logic.
* **Common Mistake:** Not following "use" naming convention breaks React's rules.
* **Pro Tip:** Can combine multiple hooks to create powerful abstractions.

---

### ⭐ Senior Takeaway

Custom hooks are the modern way to share logic, replacing HOCs and render props.

---

## 🧩 Q25. What are `useTransition` and `useDeferredValue` used for in concurrent rendering?

### 🧠 Concept

useTransition marks updates as non-urgent. useDeferredValue defers value updates. Both keep UI responsive during heavy updates by prioritizing user interactions.

---

### 💡 Example

```jsx
const [isPending, startTransition] = useTransition();
const deferredQuery = useDeferredValue(query);
useEffect(() => {
  if (deferredQuery) {
    startTransition(() => setResults(expensiveSearch(deferredQuery)));
  }
}, [deferredQuery]);
```

---

### 🔍 Deep Insights

* **Rule:** These hooks keep UI responsive during heavy updates by marking them as low priority.
* **Use Case:** Search results, filtering large lists, or any expensive rendering.
* **Common Mistake:** Using for urgent updates—they're meant for non-urgent background work.
* **Pro Tip:** Allows React to interrupt heavy work and respond to user input.

---

### ⭐ Senior Takeaway

These hooks enable concurrent rendering in React 18+ by prioritizing user interactions.

---

## 🧩 Q26. What is `useId` and when is it helpful?

### 🧠 Concept

useId generates unique IDs stable across server and client. Essential for accessibility and form labels in SSR applications to prevent hydration mismatches.

---

### 💡 Example

```jsx
const id = useId();
return (
  <div>
    <label htmlFor={id}>{label}</label>
    <input id={id} type={type} />
  </div>
);
```

---

### 🔍 Deep Insights

* **Rule:** useId generates stable, unique IDs for form labels and ARIA attributes.
* **Use Case:** Form inputs, accessibility attributes, or any place needing unique IDs.
* **Common Mistake:** Using Math.random() or Date.now() breaks with SSR and hydration.
* **Pro Tip:** Ensures same ID on server and client, preventing hydration mismatches.

---

### ⭐ Senior Takeaway

useId solves the ID generation problem in SSR applications safely.

---

## 🧩 Q27. What is `useSyncExternalStore` and what problem does it solve?

### 🧠 Concept

useSyncExternalStore subscribes to external stores safely during concurrent rendering. Prevents hydration mismatches and ensures consistent reads in React 18+.

---

### 💡 Example

```jsx
function useLocalStorage(key, defaultValue) {
  return useSyncExternalStore(
    (callback) => {
      window.addEventListener('storage', callback);
      return () => window.removeEventListener('storage', callback);
    },
    () => localStorage.getItem(key) 
      ? JSON.parse(localStorage.getItem(key)) 
      : defaultValue,
    () => defaultValue
  );
}
```

---

### 🔍 Deep Insights

* **Rule:** useSyncExternalStore safely subscribes to external stores during concurrent rendering.
* **Use Case:** State management libraries, browser APIs, or any external data source.
* **Common Mistake:** Using regular hooks with external stores causes hydration mismatches in SSR.
* **Pro Tip:** Ensures consistent reads during React's concurrent rendering.

---

### ⭐ Senior Takeaway

This hook is what libraries like Redux use internally for React 18+ compatibility.

---

## 🧩 Q28. What is `useInsertionEffect` and how does it differ from `useLayoutEffect`?

### 🧠 Concept

useInsertionEffect runs before DOM mutations, earlier than useLayoutEffect. Used by CSS-in-JS libraries to inject styles before layout calculations.

---

### 💡 Example

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

---

### 🔍 Deep Insights

* **Rule:** useInsertionEffect injects styles before DOM mutations to prevent visual flicker.
* **Use Case:** CSS-in-JS libraries like styled-components, emotion, or any style injection.
* **Common Mistake:** Using for regular effects—this is specialized for style injection.
* **Pro Tip:** Runs synchronously before layout to ensure styles are ready.

---

### ⭐ Senior Takeaway

This hook is mainly for library authors, not everyday use—rarely needed in apps.

---
