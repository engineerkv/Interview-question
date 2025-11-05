# ⚛️ 1. React Fundamentals (Q1–11)

---

## 1) What is React and why is it used?

React is a JavaScript library for building user interfaces using components and virtual DOM.

```jsx
function App() {
  return <div><h1>Hello, React!</h1></div>;
}
```

- **Component-Based Architecture**: Build UI by composing reusable components, just like LEGO blocks
- **Virtual DOM**: React compares virtual trees in memory before touching the real DOM, making updates fast
- **Common Mistake**: Trying to manipulate DOM directly instead of letting React handle updates
- **Performance**: Batching multiple updates into single DOM operations prevents expensive reflows
- **Interview Tip**: Explain how React's declarative approach simplifies UI updates compared to imperative DOM manipulation

---

## 2) What are React components? Explain functional vs class components.

React components are reusable UI pieces. Functional components use functions and hooks, while class components use ES6 classes.

```jsx
function Welcome({ name }) {
  return <h1>Hello, {name}!</h1>;
}
```

- **Modern Standard**: Functional components with hooks are the recommended approach since React 16.8
- **Real-World Use**: Most new projects use functional components for cleaner, simpler code
- **Common Mistake**: Creating new class components when functional components with hooks would work better
- **Performance**: Functional components compile to less code and have better optimization potential
- **Interview Tip**: Know when to use class components (Error Boundaries) vs functional components (everything else)

---

## 3) What is JSX and how does it differ from HTML?

JSX lets you write HTML-like syntax in JavaScript. It gets compiled to React.createElement() calls.

```jsx
function UserProfile({ user, isLoggedIn }) {
  return <div><h1>{user.name}</h1>{isLoggedIn ? <p>Welcome back!</p> : <p>Please log in</p>}</div>;
}
```

- **Key Rule**: JSX must have one root element or use Fragments, and expressions go inside curly braces
- **Real-World Use**: JSX makes templates readable while keeping JavaScript logic close to markup
- **Common Mistake**: Forgetting camelCase for attributes (className not class, onClick not onclick)
- **Compilation**: Babel converts JSX to React.createElement() calls before browser execution
- **Interview Tip**: Explain that JSX is syntactic sugar that makes React code more maintainable than raw createElement calls

---

## 4) What is the Virtual DOM and how does it improve performance?

Virtual DOM is React's JavaScript copy of the real DOM. React compares virtual trees to update only what changed.

```jsx
function Counter({ count }) {
  return <div><h2>Count: {count}</h2><button>Increment</button></div>;
}
```

- **Core Idea**: React creates virtual trees, compares them, and applies minimal real DOM changes
- **Real-World Benefit**: Prevents layout thrashing by batching updates instead of updating DOM immediately
- **Common Mistake**: Thinking virtual DOM is faster than direct DOM manipulation (it's not, but it's smarter)
- **Optimization**: React batches state updates and uses heuristics to minimize diff calculations
- **Interview Tip**: Explain that virtual DOM trades memory for predictability and performance in complex apps

---

## 5) What is the difference between real DOM and virtual DOM?

Real DOM is the browser's actual HTML structure. Virtual DOM is React's lightweight JavaScript copy used for comparisons.

```jsx
const virtualElement = {
  type: 'div',
  props: { className: 'container', children: 'Hello World' }
};
```

- **Key Difference**: Real DOM is slow to change, virtual DOM is fast to compare in JavaScript
- **Real-World Impact**: Virtual DOM lets React update UI efficiently without expensive browser reflows
- **Common Mistake**: Assuming virtual DOM is always faster (it adds memory overhead for small apps)
- **Optimization**: React uses virtual DOM to batch and minimize real DOM operations
- **Interview Tip**: Explain that virtual DOM is a performance optimization for complex UIs, not always needed for simple apps

---

## 6) What is Real DOM and why is it expensive to manipulate?

Real DOM is the browser's actual HTML structure. Changing it triggers layout recalculation, repainting, and reflows.

```jsx
const [count, setCount] = useState(0);
return <div style={{color: 'red'}}>{count}</div>;
```

- **Why Expensive**: Each DOM change forces browser to recalculate layout and repaint, blocking the main thread
- **Real-World Problem**: Frequent DOM updates cause janky UIs and poor performance in complex apps
- **Common Mistake**: Directly manipulating DOM in React defeats the purpose of React's virtual DOM system
- **React's Solution**: Virtual DOM batches changes and calculates minimal updates before touching real DOM
- **Interview Tip**: Explain that real DOM manipulation is expensive because browsers optimize for rendering, not frequent updates

---

## 7) What are props in React and how are they different from state?

Props are read-only data passed from parent to child. State is mutable data inside a component.

```jsx
function App() {
  const [count, setCount] = useState(0);
  return <Counter count={count} onIncrement={() => setCount(count + 1)} />;
}
```

- **Key Rule**: Props flow down, events flow up. State belongs to the component that owns it
- **Real-World Pattern**: Use props for configuration, state for interactivity and user input
- **Common Mistake**: Trying to mutate props directly or lifting state too high in the component tree
- **Optimization**: Memoize props with useMemo/useCallback to prevent unnecessary child re-renders
- **Interview Tip**: Explain unidirectional data flow - props down, callbacks up, state stays local

---

## 8) What is the purpose of keys in React lists?

Keys help React track which list items changed, were added, or removed for efficient updates.

```jsx
function TodoList({ todos }) {
  return <ul>{todos.map(todo => <li key={todo.id}>{todo.text}</li>)}</ul>;
}
```

- **Core Purpose**: Keys give React stable identity for list items during reconciliation
- **Real-World Impact**: Without keys, React re-renders all items when list changes, causing performance issues
- **Common Mistake**: Using array index as key breaks when items are reordered, added, or removed
- **Best Practice**: Use unique, stable IDs from your data, never index for dynamic lists
- **Interview Tip**: Explain that keys enable React to efficiently update only changed items instead of recreating the entire list

---

## 9) What are controlled vs uncontrolled components in forms?

Controlled components use React state for values. Uncontrolled components use DOM refs to read values.

```jsx
function ControlledForm() {
  const [value, setValue] = useState('');
  return <input value={value} onChange={(e) => setValue(e.target.value)} />;
}
```

- **Key Difference**: Controlled means React owns the value, uncontrolled means DOM owns it
- **Real-World Use**: Controlled for validation and dynamic forms, uncontrolled for simple inputs
- **Common Mistake**: Mixing controlled and uncontrolled patterns in the same form
- **Optimization**: Uncontrolled avoids re-renders but loses React's declarative benefits
- **Interview Tip**: Prefer controlled components for most cases - they're easier to test and validate

---

## 10) What are Fragments and why are they used?

Fragments let you group multiple elements without adding extra DOM nodes.

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

- **Core Purpose**: Return multiple elements without wrapper divs that break CSS layouts
- **Real-World Use**: Essential for table rows, flex layouts, and semantic HTML structures
- **Common Mistake**: Wrapping everything in divs when Fragments would preserve layout
- **Key Prop**: Use React.Fragment with key prop for lists, <> doesn't support keys
- **Interview Tip**: Explain that Fragments solve the "components must return one element" limitation elegantly

---

## 11) What is reconciliation in React?

Reconciliation is React's process of comparing virtual DOM trees to decide what DOM changes are needed.

```jsx
function App() {
  const [count, setCount] = useState(0);
  return <div><h1>Count: {count}</h1><button onClick={() => setCount(count + 1)}>Increment</button></div>;
}
```

- **Core Process**: React compares old and new virtual trees, then applies minimal DOM updates
- **Real-World Benefit**: Enables fast UI updates by updating only what actually changed
- **Common Mistake**: Not understanding that reconciliation happens even when state doesn't change
- **Optimization**: React uses heuristics and keys to make diffing faster than O(n³) worst case
- **Interview Tip**: Explain reconciliation as React's "smart diffing" that makes virtual DOM practical

---
