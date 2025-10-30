# ⚛️ 1. React Fundamentals (Q1–11)

---

## 1) What is React and why is it used?

Concept:
React is a JavaScript library for building user interfaces, particularly single-page applications, using a component-based architecture and virtual DOM for efficient updates.

Example:
```jsx
function App() {
  return (
    <div>
      <h1>Hello, React!</h1>
    </div>
  );
}
```

Deep Insight:
- **Component-Based**: Reusable UI components that can be composed together
- **Virtual DOM**: Efficient diffing algorithm for optimal performance
- **Declarative**: Describe what the UI should look like, not how to update it
- **Unidirectional Data Flow**: Data flows down through props, events flow up
- **Ecosystem**: Large community and rich ecosystem of tools and libraries

---

## 2) What are React components? Explain functional vs class components.

Concept:
React components are reusable pieces of UI that can be either functional (using functions and hooks) or class-based (using ES6 classes and lifecycle methods).

Example:
```jsx
// Functional Component
function Welcome({ name }) {
  return <h1>Hello, {name}!</h1>;
}
```

Deep Insight:
- **Functional Components**: Preferred approach, use hooks for state and lifecycle
- **Class Components**: Legacy approach, use lifecycle methods and this.state
- **Props**: Both receive data through props parameter
- **State Management**: Functional uses hooks, class uses this.state
- **Performance**: Functional components are generally more performant

---

## 3) What is JSX and how does it differ from HTML?

Concept:
JSX is a syntax extension that allows writing HTML-like code in JavaScript, which gets transpiled to React.createElement() calls, enabling dynamic content and JavaScript expressions.

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
```

Deep Insight:
- **JavaScript Expressions**: Use {} to embed JavaScript expressions
- **CamelCase**: HTML attributes become camelCase (className, onClick)
- **Self-Closing Tags**: Must be self-closing (e.g., <img />)
- **Transpilation**: JSX is transpiled to React.createElement() calls
- **Type Safety**: Can be used with TypeScript for better type checking

---

## 4) What is the Virtual DOM and how does it improve performance?

Concept:
The Virtual DOM is a JavaScript representation of the real DOM that React uses to efficiently update the UI by comparing changes and only updating what's necessary.

Example:
```jsx
function Counter({ count }) {
  return (
    <div>
      <h2>Count: {count}</h2>
      <button>Increment</button>
    </div>
  );
}
```

Deep Insight:
- **Diffing Algorithm**: Compares current and previous virtual DOM trees
- **Batched Updates**: Groups multiple updates into single DOM operations
- **Minimal Changes**: Only updates the parts of DOM that actually changed
- **Performance**: Avoids expensive DOM operations and reflows
- **Predictable**: Makes UI updates more predictable and debuggable

---

## 5) What is the difference between real DOM and virtual DOM?

Concept:
Real DOM is the actual browser representation of HTML elements, while Virtual DOM is React's lightweight JavaScript representation used for efficient diffing and updates.

Example:
```jsx
// Virtual DOM (JavaScript objects)
const virtualElement = {
  type: 'div',
  props: { className: 'container', children: 'Hello World' }
};
```

Deep Insight:
- **Real DOM**: Heavy, slow to manipulate, direct browser representation
- **Virtual DOM**: Lightweight, fast to manipulate, JavaScript objects
- **Memory Usage**: Virtual DOM uses more memory but enables faster updates
- **Manipulation**: Virtual DOM changes are batched and optimized
- **Reconciliation**: Process of syncing virtual DOM with real DOM

---

## 6) What is Real DOM and why is it expensive to manipulate?

Concept:
Real DOM is the browser's actual representation of HTML elements in memory, and it's expensive because every change triggers layout calculations, repainting, and potential reflows.

Example:
```jsx
// Direct DOM manipulation (expensive)
document.getElementById('counter').textContent = '5';
document.getElementById('counter').style.color = 'red';

// React approach (efficient)
const [count, setCount] = useState(0);
return <div style={{color: 'red'}}>{count}</div>;
```

Deep Insight:
- **Layout Thrashing**: Every DOM change triggers layout recalculation
- **Repaint/Reflow**: Visual updates require expensive browser operations
- **Synchronous**: DOM operations block the main thread
- **Memory Overhead**: Each DOM node has significant memory footprint
- **Browser Optimization**: Virtual DOM batches changes to minimize real DOM operations

---

## 7) What are props in React and how are they different from state?

Concept:
Props are read-only data passed from parent to child components, while state is mutable data managed within a component that can trigger re-renders when changed.

Example:
```jsx
// Parent passes props down
function App() {
  const [count, setCount] = useState(0);
  return <Counter count={count} onIncrement={() => setCount(count + 1)} />;
}
```

Deep Insight:
- **Props**: Immutable, passed down from parent, cannot be modified by child
- **State**: Mutable, managed within component, triggers re-renders when changed
- **Data Flow**: Props flow down, events flow up through callbacks
- **Re-renders**: Props changes cause child re-renders, state changes cause component re-renders
- **Composition**: Props enable component composition and reusability

---

## 8) What is the purpose of keys in React lists?

Concept:
Keys help React identify which items have changed, been added, or removed, enabling efficient list updates and preventing unnecessary re-renders.

Example:
```jsx
function TodoList({ todos }) {
  return (
    <ul>
      {todos.map(todo => (
        <li key={todo.id}>{todo.text}</li>
      ))}
    </ul>
  );
}
```

Deep Insight:
- **Identity**: Keys help React identify unique list items
- **Performance**: Prevents unnecessary re-renders of unchanged items
- **Stability**: Keys should be stable, unique, and predictable
- **Index Problem**: Using array index as key can cause issues with reordering
- **Best Practice**: Use unique, stable identifiers like IDs for keys

---

## 9) What are controlled vs uncontrolled components in forms?

Concept:
Controlled components have their values controlled by React state, while uncontrolled components manage their own state internally using refs.

Example:
```jsx
// Controlled Component
function ControlledForm() {
  const [value, setValue] = useState('');
  return <input value={value} onChange={(e) => setValue(e.target.value)} />;
}
```

Deep Insight:
- **Controlled**: Value controlled by React state, single source of truth
- **Uncontrolled**: Value managed by DOM, accessed via refs
- **Validation**: Controlled components enable easier validation and error handling
- **Performance**: Uncontrolled components can be more performant for simple forms
- **Best Practice**: Use controlled components for most form scenarios

---

## 10) What are Fragments and why are they used?

Concept:
Fragments allow grouping multiple elements without adding extra DOM nodes, useful when you need to return multiple elements from a component.

Example:
```jsx
// Without Fragment (creates extra div)
function WithoutFragment() {
  return (
    <div>
      <h1>Title</h1>
      <p>Description</p>
    </div>
  );
}
```

Deep Insight:
- **No Extra Nodes**: Fragments don't create additional DOM elements
- **Grouping**: Allow returning multiple elements from components
- **Keys**: Can use key prop with React.Fragment for lists
- **Short Syntax**: <> is shorthand for React.Fragment
- **Cleaner DOM**: Results in cleaner, more semantic HTML structure

---

## 11) What is reconciliation in React?

Concept:
Reconciliation is React's algorithm for determining what changes need to be made to the DOM by comparing the current and previous virtual DOM trees.

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

Deep Insight:
- **Diffing Algorithm**: Compares virtual DOM trees to find differences
- **Efficient Updates**: Only updates changed parts of the DOM
- **Batched Updates**: Groups multiple state changes into single update
- **Heuristic**: Uses heuristics to optimize comparison process
- **Performance**: Enables React's high performance despite frequent updates

---
