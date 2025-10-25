# ⚛️ React.js Interview Notes (2025 Edition)

## 🧠 Section 2 — React Hooks (Part 1: Q26–35)

---

### 26. 🧠 What are React Hooks, and why were they introduced?

**🧠 Concept**

Hooks are special functions that let you use state and other React features in functional components without writing class components.

**💻 Example**
```jsx
import { useState } from 'react';

function Counter() {
  const [count, setCount] = useState(0);
  return <button onClick={() => setCount(count + 1)}>{count}</button>;
}
```

**💬 Explanation + Insight**

- **Functional Components** - Hooks let you use state in functional components (before you needed classes)
- **Simpler Code** - Makes code simpler and easier to understand
- **Reusable Logic** - You can share logic between components with custom hooks
- **Modern Standard** - Everyone uses functional components with hooks now
- **Better Testing** - Hooks make React code more reusable and testable

---

### 27. 🧠 What are the rules of Hooks?

**🧠 Concept**

Hooks have two important rules: always call them at the top level of your component, and only call them from React functions.

**💻 Example**
```jsx
// ✅ Correct
function App() {
  const [count, setCount] = useState(0);
}

// ❌ Wrong
if (condition) {
  const [count, setCount] = useState(0);
}
```

**💬 Explanation + Insight**

- **Top Level Only** - Always call hooks at the top of your component (not inside if statements or loops)
- **React Components** - Only call hooks from React components or custom hooks
- **Same Order** - React needs to call hooks in the same order every time
- **ESLint Plugin** - ESLint plugin helps catch these mistakes automatically
- **Bug Prevention** - Breaking these rules causes bugs and crashes

---

### 28. 🧠 What does `useState()` do?

**🧠 Concept**

`useState` lets you add state (data that can change) to functional components.

**💻 Example**
```jsx
const [count, setCount] = useState(0);
```

**💬 Explanation + Insight**

- **Array Return** - Returns an array: `[currentValue, setterFunction]`
- **Re-rendering** - When you call the setter, the component re-renders
- **Batched Updates** - React groups multiple updates together for better performance
- **State Persistence** - State stays the same between renders until you change it
- **Interactivity** - This is how you make components interactive

---

### 29. 🧠 How does React batch updates inside `useState`?

**🧠 Concept**

React groups multiple state updates together and only re-renders once to make your app faster.

**💻 Example**
```jsx
setCount(count + 1);
setCount(count + 1);
// React batches  only one re-render happens
```

**💬 Explanation + Insight**

- React groups multiple setState calls into one update
- Before React 18: only worked in event handlers
- React 18+: works everywhere (timeouts, promises, etc.)
- Prevents unnecessary re-renders and makes app faster
- You don't need to do anything - React handles it automatically

---

### 30. 🧠 What is the difference between `useState` and `useReducer`?

**🧠 Concept**

`useState` is for simple state, while `useReducer` is for complex state that needs more control.

**💻 Example**
```jsx
const [state, dispatch] = useReducer(reducer, { count: 0 });

function reducer(state, action) {
  switch (action.type) {
    case 'inc': return { count: state.count + 1 };
  }
}
```

**💬 Explanation + Insight**

- Use `useState` for simple state (like a counter or form input)
- Use `useReducer` for complex state (like a form with many fields)
- `useReducer` is like Redux but for one component
- Better for state that depends on previous values
- Makes complex state logic easier to manage

---

### 31. 🧠 What is `useEffect()` used for?

**🧠 Concept**

`useEffect` lets you do things after your component renders, like fetching data or setting up timers.

**💻 Example**
```jsx
useEffect(() => {
  document.title = `Count: ${count}`;
}, [count]);
```

**💬 Explanation + Insight**

- Runs after every render by default
- Empty array `[]` means run only once (like componentDidMount)
- Array with values `[count]` means run when count changes
- Return a function to clean up (like removing event listeners)
- Essential for data fetching, timers, and subscriptions

---

### 32. 🧠 What is the cleanup function in `useEffect()`?

**🧠 Concept**
A cleanup function is what you return from `useEffect` to clean up things like timers or event listeners.

**💻 Example**
```jsx
useEffect(() => {
  const timer = setInterval(() => console.log('tick'), 1000);
  return () => clearInterval(timer); // cleanup
}, []);
```

**💬 Explanation + Insight**

- Return a function from useEffect to clean up
- React calls it before the next effect or when component unmounts
- Prevents memory leaks from timers and event listeners
- Always clean up what you set up
- Essential for preventing bugs and crashes

---

### 33. 🧠 How do dependency arrays work in `useEffect()`?

**🧠 Concept**
The dependency array tells React when to re-run the effect.

**💻 Example**
```jsx
useEffect(() => {
  console.log('Runs when count changes');
}, [count]);
```

**💬 Explanation + Insight**

- Empty array `[]` means run only once (when component mounts)
- No array means run after every render
- Array with values `[count]` means run when count changes
- React compares values shallowly (objects/arrays need to be new references)
- Be careful with objects and arrays in dependencies

---

### 34. 🧠 What is the difference between `useEffect` and `useLayoutEffect`?

**🧠 Concept**
Both run after render, but `useEffect` runs after the browser paints, while `useLayoutEffect` runs before the browser paints.

**💻 Example**
```jsx
useLayoutEffect(() => {
  // Runs before browser paints
  console.log('Layout effect');
});
```

**💬 Explanation + Insight**

- Use `useLayoutEffect` when you need to measure DOM before browser paints
- Good for animations and layout adjustments
- Don't use it too much - it can slow down your app
- Use `useEffect` for most cases
- Only use `useLayoutEffect` when you really need it

---

### 35. 🧠 What is `useRef()`, and what are its common use cases?

**🧠 Concept**

`useRef` creates a reference that persists across renders and doesn't cause re-renders when you change it.

**💻 Example**
```jsx
const inputRef = useRef();

useEffect(() => {
  inputRef.current.focus();
}, []);
```

**💬 Explanation + Insight**

- Like a box that keeps the same value between renders
- Perfect for accessing DOM elements directly
- Good for storing timers, previous values
- Doesn't cause re-renders when you change it
- Use it when you need to store something that doesn't affect the UI


### 36. 🧠 What is `useMemo()` used for?

**🧠 Concept**

`useMemo` caches expensive calculations and only recalculates when dependencies change.

**💻 Example**
```jsx
const expensiveResult = useMemo(() => computeHeavy(value), [value]);
```

**💬 Explanation + Insight**

- Like a smart calculator that remembers the answer
- Only recalculates when dependencies actually change
- Use only for expensive calculations (not simple math)
- Don't overuse it - can make code slower if used wrong
- Returns the cached value, not a function

---

### 37. 🧠 What is the difference between `useMemo()` and `useCallback()`?

**🧠 Concept**

`useMemo` caches values, while `useCallback` caches functions.

**💻 Example**
```jsx
const memoizedFn = useCallback(() => doSomething(dep), [dep]);
const memoizedValue = useMemo(() => compute(dep), [dep]);
```

**💬 Explanation + Insight**

- `useMemo` caches the result of a calculation
- `useCallback` caches the function itself
- Use `useCallback` when passing functions as props
- Prevents unnecessary re-renders of child components
- Both help optimize performance when used correctly

---

### 38. 🧠 What is `useContext()` and when should you use Context API?

🧠 **Concept**

`useContext` allows components to **consume shared data** from a React Context without prop drilling.

💻 **Example**

```jsx
const ThemeContext = createContext('light');
const theme = useContext(ThemeContext);
```

📝 **Deeper Insight**

Avoids passing props manually through every level of the component tree.
Best for **global data** like theme, auth, or language.
Note: frequent context updates can trigger re-renders — use memoization or splitting contexts for optimization.

---

### 39. 🧠 What are custom hooks, and why use them?

**🧠 Concept**

Custom hooks are reusable functions that use other hooks to share logic between components.

**💻 Example**
```jsx
function useWindowWidth() {
  const [width, setWidth] = useState(window.innerWidth);
  useEffect(() => {
    const onResize = () => setWidth(window.innerWidth);
    window.addEventListener('resize', onResize);
    return () => window.removeEventListener('resize', onResize);
  }, []);
  return width;
}
```

**💬 Explanation + Insight**

- Like creating your own reusable hook
- Share logic between components without duplicating code
- Must start with "use" so React knows it's a hook
- Makes code more organized and easier to test
- Perfect for complex logic you use in multiple places

---

### 40. 🧠 What is `useImperativeHandle()` used for?

**🧠 Concept**

Used with `forwardRef` to control what a parent component can access through a child's ref.

**💻 Example**
```jsx
const Input = forwardRef((props, ref) => {
  const inputRef = useRef();
  useImperativeHandle(ref, () => ({
    focus: () => inputRef.current.focus(),
  }));
  return <input ref={inputRef} />;
});
```

**💬 Explanation + Insight**

- Like creating a controlled interface for parent components
- Parent can only access what you allow them to
- Good for building reusable input or modal components
- Keeps internal implementation hidden
- Use with `forwardRef` to pass refs to child components

---

### 41. 🧠 What is `useTransition()` and how does it improve performance?

🧠 **Concept**

`useTransition` lets you **mark state updates as non-urgent**, allowing React to keep the UI responsive during expensive updates.

💻 **Example**

```jsx
const [isPending, startTransition] = useTransition();

startTransition(() => {
  setFilteredItems(filterItems(query));
});
```

📝 **Deeper Insight**

Introduced in **React 18 Concurrent Mode**.
It helps React **defer low-priority updates** (like filtering) without blocking urgent ones (like typing).
Improves **perceived performance** and user experience.

---

### 42. 🧠 What is `useDeferredValue()` used for?

🧠 **Concept**

`useDeferredValue` lets React **delay updating** a value until higher-priority work (like user input) finishes.

💻 **Example**

```jsx
const deferredQuery = useDeferredValue(query);
const filtered = useMemo(() => filterList(deferredQuery), [deferredQuery]);
```

📝 **Deeper Insight**

Useful for **search inputs**, **typeahead UIs**, and **large data lists**.
`useDeferredValue` is **value-based**, while `useTransition` is **update-based**.

---

### 43. 🧠 What is `useSyncExternalStore()` and when to use it?

🧠 **Concept**

It’s a low-level hook for **subscribing to external data sources** (like Redux or custom stores) safely with concurrent rendering.

💻 **Example**

```jsx
const state = useSyncExternalStore(store.subscribe, store.getSnapshot);
```

📝 **Deeper Insight**

Introduced in **React 18** to ensure consistent behavior between concurrent renders.
It’s the basis for libraries like **Redux v8**, ensuring React doesn’t read stale data during updates.

---

### 44. 🧠 What is `useInsertionEffect()`?

🧠 **Concept**

A special hook that runs **synchronously before DOM mutations** — mainly for CSS-in-JS libraries.

💻 **Example**

```jsx
useInsertionEffect(() => {
  injectStyle('.btn { color: red }');
}, []);
```

📝 **Deeper Insight**

Used internally by style libraries (Emotion, Styled Components) to insert styles **before layout effects** run, preventing visual flicker.
Avoid for general side effects — use `useEffect` or `useLayoutEffect` instead.

---

### 45. 🧠 What is `useId()`, and why was it added?

🧠 **Concept**

`useId` generates **unique, stable IDs** across renders and server/client (SSR) for accessibility attributes or list items.

💻 **Example**

```jsx
const id = useId();
<label htmlFor={id}>Email</label>
<input id={id} />
```

📝 **Deeper Insight**

Added in **React 18** for **SSR hydration consistency**.
Unlike random IDs, `useId` ensures identical values between server-rendered and client-rendered output.


Perfect ⚛️ Kamal — let’s wrap up the **React Hooks** section with
the final batch: **Q46–50 (React 19 Hooks + Core Concepts)**

Then I’ll compile all 25 (Q26–50) into a complete, formatted `react-hooks.md` file — same as your Fundamentals one.

---

# ⚛️ React.js Interview Notes (2025 Edition)

## 🧠 Section 2 — React Hooks (Part 3: Q46–50)

---

### 46. 🧠 What is `useOptimistic()` (React 19)?

🧠 **Concept**

`useOptimistic` allows you to **optimistically update the UI** before a server action completes — improving perceived speed and responsiveness.

💻 **Example**

```jsx
const [optimisticTodos, addOptimisticTodo] = useOptimistic(todos);

function handleAdd(text) {
  addOptimisticTodo([...optimisticTodos, { text, pending: true }]);
  saveTodoToServer(text);
}
```

📝 **Deeper Insight**

Introduced in **React 19**, it integrates with **React Actions** to manage **transient, optimistic states** automatically.
It’s like `useState`, but for **optimistic UIs** — React will reconcile once the server response returns.

---

### 47. 🧠 What is `useFormStatus()` (React 19)?

🧠 **Concept**

`useFormStatus` provides **real-time feedback about form submissions**, such as whether the form is currently submitting or idle.

💻 **Example**

```jsx
function SubmitButton() {
  const { pending } = useFormStatus();
  return <button disabled={pending}>{pending ? 'Submitting…' : 'Submit'}</button>;
}
```

📝 **Deeper Insight**

Used inside **React Server Actions** and `<form action={...}>` handlers.
Gives access to form-level state like:

* `pending`
* `data`
* `method`
  Improves UX by enabling **loading indicators** and **disabled buttons** during async submissions.

---

### 48. 🧠 What is `useActionState()` (React 19)?

🧠 **Concept**

`useActionState` helps track and manage **server action results** (success or failure) and their **pending state**.

💻 **Example**

```jsx
const [state, formAction, isPending] = useActionState(async (prev, formData) => {
  const result = await saveToDB(formData);
  return result;
});
<form action={formAction}>
  <button disabled={isPending}>Save</button>
</form>
```

📝 **Deeper Insight**

`useActionState` integrates **client + server state** seamlessly.
It’s React’s modern replacement for manually handling loading states, errors, and data submission feedback — a big step toward **declarative async UIs**.

---

### 49. 🧠 How do Hooks replace lifecycle methods in class components?

🧠 **Concept**

Hooks replicate the behavior of lifecycle methods using combinations of `useEffect`, `useLayoutEffect`, and others.

💻 **Example**

| Class Lifecycle            | Hook Equivalent                   |
| -------------------------- | --------------------------------- |
| `componentDidMount`        | `useEffect(() => {...}, [])`      |
| `componentDidUpdate`       | `useEffect(() => {...}, [deps])`  |
| `componentWillUnmount`     | Cleanup in `useEffect`            |
| `shouldComponentUpdate`    | `React.memo()` or `useMemo()`     |
| `getDerivedStateFromProps` | `useEffect` with props comparison |

📝 **Deeper Insight**

Hooks unify lifecycle logic — instead of spreading across multiple methods, related logic stays **together in one place**.
They also reduce bugs by removing reliance on `this` and implicit class context.

---

### 50. 🧠 Why can’t Hooks be called conditionally or inside loops?

🧠 **Concept**

React must call hooks in the **exact same order** every render to correctly associate state and effects with the right components.

💻 **Example**

```jsx
// ❌ Wrong
if (condition) useState(0);

// ✅ Correct
const [count, setCount] = useState(0);
if (condition) console.log(count);
```

📝 **Deeper Insight**

Hooks rely on **call order indexing** internally.
If you call them conditionally or inside loops, React loses track of which state belongs to which hook — causing runtime errors.
React’s Hook Rules ESLint plugin enforces this to ensure reliability.


