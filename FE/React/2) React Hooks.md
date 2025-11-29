<div align="center">

**[← Previous: React Fundamentals](1%29%20React%20Fundamentals.md)** | **[Next: State Management →](3%29%20State%20Management.md)**

</div>

# 2. React Hooks (Q18–38)

---

## Q18. React Hooks and why they were introduced

Hooks let functional components use state and lifecycle features without classes - they solve class component complexity and enable better code reuse through custom hooks. Custom hooks let you share stateful logic across components easily, replacing HOCs and render props.

- **Trade-offs**: The catch is calling hooks inside loops, conditions, or nested functions breaks React's rules - extract logic into custom hooks instead of HOCs or render props to avoid "wrapper hell." Hooks solve the "wrapper hell" problem from HOCs and make code more readable and maintainable, but watch out - you must follow the rules of hooks or React will break.

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

---

## Q19. How `useState` works internally

useState returns state value and setter - React tracks hooks in a linked list per component, maintaining order between renders to ensure consistency. Hooks must be called in same order every render, no conditional hooks.

- **Trade-offs**: The catch is calling hooks conditionally or in loops breaks React's internal tracking - pass function to useState for expensive initial values: `useState(() => expensive())`. React uses a linked list to track hooks, which is why order matters and hooks must be unconditional, but watch out - this is why you can't call hooks conditionally.

Example:

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

## Q20. `useEffect` and how to use it

useEffect runs side effects after render - the dependency array controls when it runs: empty means once on mount, missing means every render, with dependencies means when they change. Effect runs after DOM updates complete, not during render.

- **Trade-offs**: The catch is missing dependencies causes stale closures and bugs - return function from effect to clean up subscriptions, timers, or listeners. useEffect is "componentDidMount + componentDidUpdate + componentWillUnmount" in one hook, but watch out - the dependency array is easy to get wrong, which can cause bugs.

Example:

```jsx
const [user, setUser] = useState(null);
useEffect(() => {
  fetchUser(userId).then(setUser);
}, [userId]);
return <div>{user ? user.name : 'Loading...'}</div>;
```

---

## Q21. `useEffect` vs `useLayoutEffect`

useEffect runs after paint, useLayoutEffect runs before paint - use useLayoutEffect to prevent visual flicker when you need DOM measurements. useLayoutEffect blocks paint, useEffect doesn't.

- **Trade-offs**: The catch is using useLayoutEffect for everything slows down rendering unnecessarily - default to useEffect, only use useLayoutEffect when you see visual flicker. useLayoutEffect can block rendering, so use sparingly, only when visual consistency matters, but watch out - blocking paint can make your app feel slow.

Example:

```jsx
const [position, setPosition] = useState({ top: 0, left: 0 });
const tooltipRef = useRef();
useLayoutEffect(() => {
  const rect = tooltipRef.current.getBoundingClientRect();
  setPosition({ top: rect.bottom + 8, left: rect.left });
}, [children]);
```

---

## Q22. `useRef` and how to use it

useRef returns a mutable object that persists across renders - use it for DOM access and values that don't need re-renders when they change. Changing `.current` doesn't trigger re-renders, unlike state.

- **Trade-offs**: The catch is using refs for values that should trigger UI updates - use state instead. Refs are perfect for values that change but don't need to re-render component, but watch out - refs are "state that doesn't cause re-renders" for DOM access and mutable values, so don't use them when you need UI updates.

Example:

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

## Q23. Refs vs state in React

State changes trigger re-renders, while refs don't trigger re-renders but persist across renders - making them perfect for values that change but shouldn't update UI. State changes cause UI updates, ref changes don't.

- **Trade-offs**: The catch is using state for values that don't need UI updates wastes performance - use refs for values that change but shouldn't trigger re-renders. Refs are like "state that doesn't cause re-renders" for performance optimization, but watch out - if you need the UI to update when a value changes, you must use state.

Example:

```jsx
const [count, setCount] = useState(0);
const renderCount = useRef(0);
useEffect(() => { renderCount.current += 1; });
return <div>Renders: {renderCount.current} Count: {count}</div>;
```

---

## Q24. `useCallback` and when to use it

useCallback memoizes a function so it only changes when dependencies change - use it to prevent child re-renders when passing callbacks to memoized components. useCallback memoizes function references to prevent unnecessary child re-renders.

- **Trade-offs**: The catch is using useCallback everywhere - it adds overhead without benefit if not needed, only use when you have performance issues with child re-renders. useCallback is about reference equality, not function execution, so use only when needed, but watch out - it doesn't help if the component receiving the callback isn't memoized.

Example:

```jsx
const [count, setCount] = useState(0);
const [name, setName] = useState('');
const onIncrement = useCallback(() => setCount(c => c + 1), []);
return <Child onIncrement={onIncrement} name={name} />;
```

---

## Q25. `useMemo` and when to use it

useMemo caches a computed value, recalculating only when dependencies change - use it for expensive calculations to avoid recomputing on every render. useMemo memoizes expensive calculations to avoid recomputing on every render.

- **Trade-offs**: The catch is memoizing simple values - the overhead isn't worth it for primitives, only use when calculation is expensive or creates new object references. useMemo is about computation cost, not just preventing re-renders, so measure before optimizing, but watch out - premature optimization can make code harder to read.

Example:

```jsx
const filteredItems = useMemo(() => {
  return items.filter(item => 
    item.name.toLowerCase().includes(filter.toLowerCase())
  );
}, [items, filter]);
return <ul>{filteredItems.map(i => <li key={i.id}>{i.name}</li>)}</ul>;
```

---

## Q26. `useReducer` vs `useState`

useReducer manages complex state with a reducer function - better than useState when state logic is complex or involves multiple related values. useReducer manages complex state with predictable updates through reducer pattern.

- **Trade-offs**: The catch is using useReducer for simple state - useState is simpler when you don't need reducers. Reducer functions are pure and easy to test in isolation, but watch out - useReducer is like useState but for complex state logic, similar to Redux pattern, so it adds complexity that might not be needed for simple state.

Example:

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

## Q27. `useContext` and how to use it

useContext reads context values in functional components - it works with Context.Provider to share data without prop drilling through multiple levels. useContext consumes context values without prop drilling through multiple components.

- **Trade-offs**: The catch is creating new context values every render causes all consumers to re-render - memoize context value with useMemo to prevent unnecessary re-renders. Context solves prop drilling but can cause performance issues if overused, so use wisely, but watch out - context updates cause all consumers to re-render, which can be expensive.

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

---

## Q28. `useImperativeHandle` and when to use it

useImperativeHandle customizes what ref exposes to parent components - must be used with forwardRef to create controlled APIs for parent components. useImperativeHandle exposes specific methods to parent instead of entire DOM element.

- **Trade-offs**: The catch is using when declarative props would work better - prefer declarative approach. This hook hides internal implementation while exposing controlled API, but watch out - this hook is for imperative APIs when declarative isn't enough, so use sparingly.

Example:

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

## Q29. `useDebugValue` and when to use it

useDebugValue adds labels to custom hooks in React DevTools - only visible during development, automatically stripped in production builds. useDebugValue displays helpful labels in DevTools for custom hooks.

- **Trade-offs**: The catch is using for production code - it's automatically stripped in production, pass function for expensive debug values: `useDebugValue(() => expensive())`. This is a development tool only, helps debug custom hooks in DevTools, but watch out - it doesn't affect production code at all.

Example:

```jsx
function useCounter(initialValue = 0) {
  const [count, setCount] = useState(initialValue);
  useDebugValue(count > 10 ? 'High' : 'Low');
  const increment = useCallback(() => setCount(c => c + 1), []);
  return { count, increment };
}
```

---

## Q30. Creating custom hooks

Custom hooks are functions using other hooks, named with "use" - extract reusable stateful logic to share between components without HOCs or render props. Custom hooks share stateful logic between components without HOCs or render props.

- **Trade-offs**: The catch is not following "use" naming convention breaks React's rules - can combine multiple hooks to create powerful abstractions. Custom hooks are the modern way to share logic, replacing HOCs and render props, but watch out - they must follow the rules of hooks just like regular hooks.

Example:

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

## Q31. `useTransition` and `useDeferredValue`

useTransition marks updates as non-urgent, useDeferredValue defers value updates - both keep UI responsive during heavy updates by prioritizing user interactions. These hooks keep UI responsive during heavy updates by marking them as low priority.

- **Trade-offs**: The catch is using for urgent updates - they're meant for non-urgent background work, allows React to interrupt heavy work and respond to user input. These hooks enable concurrent rendering in React 18+ by prioritizing user interactions, but watch out - they're only available in React 18+, so make sure you're using the right version.

Example:

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

## Q32. `useId` and when to use it

useId generates unique IDs stable across server and client - essential for accessibility and form labels in SSR applications to prevent hydration mismatches. useId generates stable, unique IDs for form labels and ARIA attributes.

- **Trade-offs**: The catch is using Math.random() or Date.now() breaks with SSR and hydration - ensures same ID on server and client, preventing hydration mismatches. useId solves the ID generation problem in SSR applications safely, but watch out - it's only needed when you have SSR, for client-only apps you can use other methods.

Example:

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

## Q33. `useSyncExternalStore` and when to use it

useSyncExternalStore subscribes to external stores safely during concurrent rendering - prevents hydration mismatches and ensures consistent reads in React 18+. useSyncExternalStore safely subscribes to external stores during concurrent rendering.

- **Trade-offs**: The catch is using regular hooks with external stores causes hydration mismatches in SSR - ensures consistent reads during React's concurrent rendering. This hook is what libraries like Redux use internally for React 18+ compatibility, but watch out - it's mainly for library authors, not everyday app code.

Example:

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

## Q34. `useInsertionEffect` and when to use it

useInsertionEffect runs before DOM mutations, earlier than useLayoutEffect - used by CSS-in-JS libraries to inject styles before layout calculations. useInsertionEffect injects styles before DOM mutations to prevent visual flicker.

- **Trade-offs**: The catch is using for regular effects - this is specialized for style injection, runs synchronously before layout to ensure styles are ready. This hook is mainly for library authors, not everyday use, rarely needed in apps, but watch out - if you're building a CSS-in-JS library, this is essential.

Example:

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

## Q35. `use()` hook and how to use it

The `use()` hook unwraps promises and context values, enabling data fetching with automatic Suspense integration - it can read promises, context, or any value that follows the "useable" protocol. `use()` provides a unified way to consume async data and context values with built-in Suspense support.

- **Trade-offs**: The catch is `use()` must be called unconditionally and can throw promises that Suspense boundaries catch - it works seamlessly with Suspense for loading states and error boundaries for errors. `use()` simplifies data fetching by automatically handling promise states, but watch out - it throws promises that Suspense catches, so you need Suspense boundaries in your component tree.

Example:

```jsx
// Unwrapping promises
function UserProfile({ userId }) {
  const user = use(fetchUser(userId));
  return <div>{user.name}</div>;
}

// Unwrapping context
const ThemeContext = createContext();
function ThemedButton() {
  const theme = use(ThemeContext);
  return <button className={theme}>Click me</button>;
}

// With Suspense
function App() {
  return (
    <Suspense fallback={<div>Loading user...</div>}>
      <UserProfile userId={1} />
    </Suspense>
  );
}
```

---

## Q36. `useActionState()` and how to use it

`useActionState()` manages form actions with built-in pending states and error handling - it's designed for form submissions and async actions, providing automatic state management for pending, error, and success states. `useActionState()` simplifies form handling by managing action state automatically.

- **Trade-offs**: The catch is `useActionState()` is specifically designed for form actions and async operations - it replaces the need for manual pending state management with `useTransition`. `useActionState()` provides better DX for forms compared to manual state management, but watch out - it's React 19+ only, so ensure you're using the correct version.

Example:

```jsx
async function submitForm(prevState, formData) {
  const name = formData.get('name');
  if (!name) {
    return { error: 'Name is required' };
  }
  await fetch('/api/users', {
    method: 'POST',
    body: JSON.stringify({ name })
  });
  return { success: true, message: 'User created!' };
}

function ContactForm() {
  const [state, formAction, isPending] = useActionState(submitForm, null);
  
  return (
    <form action={formAction}>
      <input name="name" placeholder="Name" />
      {state?.error && <p className="error">{state.error}</p>}
      {state?.success && <p className="success">{state.message}</p>}
      <button type="submit" disabled={isPending}>
        {isPending ? 'Submitting...' : 'Submit'}
      </button>
    </form>
  );
}
```

---

## Q37. `useFormStatus()` and how to use it

`useFormStatus()` provides form submission status from the nearest form ancestor - it gives access to pending state, data, method, and action of the form, useful for showing loading states in form buttons or inputs. `useFormStatus()` reads form status from parent form context.

- **Trade-offs**: The catch is `useFormStatus()` must be used within a form component or a component that's a child of a form - it only works with form actions, not manual form handling. `useFormStatus()` enables better UX by showing loading states in form elements, but watch out - it requires the component to be inside a `<form>` element with an action prop.

Example:

```jsx
function SubmitButton() {
  const { pending, data } = useFormStatus();
  
  return (
    <button type="submit" disabled={pending}>
      {pending ? 'Submitting...' : 'Submit'}
    </button>
  );
}

function ContactForm() {
  async function handleSubmit(formData) {
    await fetch('/api/contact', {
      method: 'POST',
      body: formData
    });
  }
  
  return (
    <form action={handleSubmit}>
      <input name="email" type="email" />
      <SubmitButton />
    </form>
  );
}
```

---

## Q38. `useOptimistic()` and how to use it

`useOptimistic()` enables optimistic UI updates by showing immediate feedback before server confirmation - it manages optimistic state that gets reverted if the action fails, providing better perceived performance. `useOptimistic()` shows immediate UI updates while waiting for server response.

- **Trade-offs**: The catch is optimistic updates can be reverted if the action fails - you need to handle rollback logic when the actual server response arrives. `useOptimistic()` improves UX by showing instant feedback, but watch out - you must handle error cases where the optimistic update needs to be reverted.

Example:

```jsx
function TodoList({ todos }) {
  const [optimisticTodos, addOptimisticTodo] = useOptimistic(
    todos,
    (state, newTodo) => [...state, { ...newTodo, id: 'temp-' + Date.now() }]
  );
  
  async function addTodo(formData) {
    const newTodo = { text: formData.get('text') };
    addOptimisticTodo(newTodo);
    
    try {
      const response = await fetch('/api/todos', {
        method: 'POST',
        body: JSON.stringify(newTodo)
      });
      const savedTodo = await response.json();
      // Replace optimistic todo with real one
    } catch (error) {
      // Revert optimistic update on error
    }
  }
  
  return (
    <div>
      {optimisticTodos.map(todo => (
        <div key={todo.id}>{todo.text}</div>
      ))}
      <form action={addTodo}>
        <input name="text" />
        <button type="submit">Add</button>
      </form>
    </div>
  );
}
```

---

