# ⚛️ React Internals

---

## 📍 Navigation

<div align="center">

[← Previous: TypeScript Internals](08%29%20TypeScript%20Internals.md) • [Home: Questions Index](question.md) • [Next: Next.js Internals →](10%29%20Next.js%20Internals.md)

[📋 Cheatsheet](FE-System-Design%20Interview%20Cheatsheet.md)

</div>

---

---

## 1. ⚛️ How React.js Works Internally

React is a library for building user interfaces. Understanding how React works under the hood helps you write better code, debug tricky issues, and optimize performance. When you use React, it handles Virtual DOM, reconciliation, Fiber architecture, hooks, state management, event system, and performance optimizations behind the scenes. This knowledge is crucial for senior developers - it helps you understand why certain patterns work better, how to optimize React applications, and how to debug complex issues.

---

### 🔹 ⚛️ React Architecture

### 🔹 Core Concepts

React is built on three fundamental principles that make it powerful and predictable:

**Component-Based Architecture:**

* You build UI from reusable, composable components

* Components are just functions or classes that return JSX

* Each component can have its own state and receive props from parents

* Components can be nested and composed together

* This promotes code reuse, separation of concerns, and maintainability

* Example: A `Button` component can be reused throughout your app with different props

**Declarative Programming:**

* You describe what the UI should look like, not how to update it

* React figures out how to update the DOM efficiently

* You don't manually manipulate the DOM (no `document.getElementById`, `appendChild`, etc.)

* React handles all the DOM updates for you

* This makes code more predictable and easier to reason about

* Example: You write `<button onClick={handleClick}>Click me</button>`, React handles the DOM updates

**Unidirectional Data Flow:**

* Data flows down from parent to child through props (one-way)

* Events flow up from child to parent through callbacks

* This makes the data flow predictable and easier to debug

* You always know where data comes from and where it goes

* Prevents common bugs like two-way data binding issues

* Example: Parent passes `count` as prop, child calls `onIncrement` callback to update parent's state

### 🔹 Architecture Layers

React has three main layers:

* **React Core**: Handles component definitions, transforms JSX, manages component lifecycle, and handles state management

* **React Renderer**: React DOM for web, React Native for mobile - converts React elements into platform-specific code (DOM nodes or native components)

* **Scheduler**: Prioritizes which updates to process first, schedules when rendering happens, handles concurrent features, and manages work priorities

### 🔹 JSX Transformation

When you write JSX, it gets transformed behind the scenes by a transpiler (like Babel). Understanding this transformation helps you understand how React works.

**What is JSX:**

* JSX is syntactic sugar - it looks like HTML but is actually JavaScript

* Gets transpiled to `React.createElement` calls during build time

* Makes writing React components more intuitive and readable

* Not required - you can write React without JSX, but it's much more verbose

**Transformation Process:**

* Babel (or another transpiler) converts JSX to `React.createElement` calls

* Happens at build time, not runtime

* The transformed code is what actually runs in the browser

**Example - Simple Element:**

```javascript
// JSX (what you write)
const element = <h1 className="title">Hello World</h1>;

// Transformed to (what actually runs)
const element = React.createElement(
  'h1',
  { className: 'title' },
  'Hello World'
);

// Creates React element (plain JavaScript object)
{
  type: 'h1',
  props: {
    className: 'title',
    children: 'Hello World'
  }
}

```

**Example - Component with Children:**

```javascript
// JSX
const element = (
  <div className="container">
    <h1>Title</h1>
    <p>Description</p>
  </div>
);

// Transformed to
const element = React.createElement(
  'div',
  { className: 'container' },
  React.createElement('h1', null, 'Title'),
  React.createElement('p', null, 'Description')
);

```

**Example - Component Function:**

```javascript
// JSX
function Greeting({ name }) {
  return <h1>Hello, {name}!</h1>;
}

// Transformed to
function Greeting({ name }) {
  return React.createElement('h1', null, 'Hello, ', name, '!');
}

```

**React Elements vs Components:**

* **React Element**: A plain JavaScript object that describes what to render
  * Has `type` (string for DOM elements, function/class for components)
  * Has `props` (properties and children)
  * Immutable - once created, you don't modify it

* **Component**: A function or class that returns React elements
  * Can have state, props, lifecycle methods
  * Can be reused with different props

**Why This Matters:**

* React elements are lightweight objects (cheap to create)

* React can compare elements efficiently (for reconciliation)

* Elements describe the desired UI state, not the actual DOM

* This is the foundation of React's declarative model

📌 **In simple terms**: React is component-based and declarative. It has three layers: Core (components, JSX), Renderer (DOM/Native), and Scheduler (updates). JSX gets transformed to React.createElement calls that create plain objects describing what to render.

---

### 🔹 👻 Virtual DOM & Reconciliation

### 🔹 Virtual DOM

The Virtual DOM is React's JavaScript representation of the real DOM. It's a key innovation that makes React fast and efficient.

**What is Virtual DOM:**

* A lightweight JavaScript object tree that represents the DOM structure

* Much faster to create and update than the real DOM

* React keeps this as its internal representation of what the UI should look like

* It's a "virtual" representation - not the actual DOM nodes

**Why Virtual DOM Exists:**

* **Performance**: DOM manipulation is slow - creating/updating DOM nodes is expensive

* **Batching**: Allows React to batch multiple DOM updates together (more efficient)

* **Diffing**: React can compare Virtual DOM trees to find what changed (only update what actually changed)

* **Abstraction**: Work with JavaScript objects instead of DOM directly (easier, cross-platform)

* **Consistency**: Use the same logic for web (React DOM) and native (React Native)

**How Virtual DOM Works:**

* When you render a component, React creates a Virtual DOM tree

* This tree is just JavaScript objects (cheap to create)

* React compares the new Virtual DOM with the previous one (reconciliation)

* Only the differences are applied to the real DOM (efficient updates)

**Example:**

```javascript
// Component renders
function App() {
  return (
    <div>
      <h1>Hello</h1>
      <p>World</p>
    </div>
  );
}

// React creates Virtual DOM tree (JavaScript objects)
{
  type: 'div',
  props: {
    children: [
      { type: 'h1', props: { children: 'Hello' } },
      { type: 'p', props: { children: 'World' } }
    ]
  }
}

// React converts this to real DOM nodes
// <div>
//   <h1>Hello</h1>
//   <p>World</p>
// </div>

```

**Virtual DOM vs Real DOM:**

* **Virtual DOM**: JavaScript objects, fast to create/update, lightweight

* **Real DOM**: Actual browser DOM nodes, slow to create/update, heavy

* React uses Virtual DOM to minimize real DOM operations

### 🔹 Reconciliation Process

Reconciliation happens in two phases:

* **Render Phase**: Your component renders (returns JSX), React creates a new Virtual DOM tree, compares it with the previous Virtual DOM tree (this is called diffing), and identifies exactly what changed

* **Commit Phase**: React updates the real DOM based on what changed, calls lifecycle methods, updates refs, and runs effects

### 🔹 Diffing Algorithm

React's diffing algorithm is how React determines what changed between renders. It's optimized for common use cases and makes assumptions to be fast.

**How Diffing Works:**

**1. Same Element Type:**

* If the element type is the same (e.g., both are `<div>`), React updates the props and keeps the DOM node

* More efficient - React doesn't need to destroy and recreate the node

* Only updates the changed attributes

* Example:

```javascript
// Before
<div className="old">Content</div>

// After
<div className="new">Content</div>

// React: Updates className attribute, keeps the same DOM node

```

**2. Different Element Type:**

* If the element type changed (e.g., `<div>` to `<span>`), React replaces the entire subtree

* Faster than trying to update - assumes the structure is different

* Old subtree is unmounted, new subtree is mounted

* Example:

```javascript
// Before
<div>
  <Child />
</div>

// After
<span>
  <Child />
</span>

// React: Unmounts entire <div> subtree, mounts new <span> subtree
// Child component is recreated (loses state if not preserved)

```

**3. Keys in Lists:**

* Keys help React identify which items in a list changed, were added, or removed

* Must be unique among siblings

* Should be stable (don't change between renders)

* **Don't use index as key** if items can reorder (causes bugs and performance issues)

* Use stable IDs instead (from your data)

* Example:

```javascript
// Bad - using index as key
{items.map((item, index) => (
  <Item key={index} data={item} />
))}
// Problem: If items reorder, React thinks items changed when these items didn't actually change

// Good - using stable ID
{items.map(item => (
  <Item key={item.id} data={item} />
))}
// React knows which item is which, even if order changes

```

**4. Heuristic Assumptions:**

* React assumes the tree structure is similar between renders

* If you change the structure dramatically, React will replace more

* React compares elements at the same position in the tree

* This is why keys are important for lists - keys help React identify elements

**Example - List Reordering:**

```javascript
// Initial render
[
  <Item key="1" name="A" />,
  <Item key="2" name="B" />,
  <Item key="3" name="C" />
]

// After reordering (B moved to top)
[
  <Item key="2" name="B" />,  // React knows this is the same item
  <Item key="1" name="A" />,  // React knows this is the same item
  <Item key="3" name="C" />   // React knows this is the same item
]

// Without keys, React would think all items changed
// With keys, React just moves the DOM nodes (efficient!)

```

**Performance Implications:**

* Diffing is fast because it's optimized for common patterns

* Keys are crucial for list performance

* Avoid changing element types unnecessarily

* Keep component structure stable when possible

📌 **In simple terms**: Virtual DOM is React's JavaScript copy of the real DOM. Reconciliation compares the old and new Virtual DOM (diffing), then updates only what changed in the real DOM. Keys help React identify which list items changed so it can update efficiently.

---

### 🔹 🧩 Component Lifecycle & Hooks

### 🔹 Class Component Lifecycle

Class components have lifecycle methods that let you hook into different phases of a component's life. Understanding these helps you understand how React works and when to use hooks equivalents.

**Mounting Phase (Component is being created and inserted into DOM):**

**constructor(props):**

* Called before the component is mounted

* Initialize state here (don't call `setState` - use `this.state = {}`)

* Bind event handlers if needed

* Don't cause side effects here (no API calls, subscriptions)

* Example:

```javascript
constructor(props) {
  super(props);
  this.state = { count: 0 };
  this.handleClick = this.handleClick.bind(this);
}

```

**componentDidMount():**

* Called after the component is mounted (inserted into DOM)

* Good place for API calls, subscriptions, setting up timers

* Can call `setState` here (triggers a re-render)

* Example:

```javascript
componentDidMount() {
  // Fetch data
  fetch('/api/data')
    .then(res => res.json())
    .then(data => this.setState({ data }));

  // Subscribe to events
  this.subscription = subscribeToUpdates(this.handleUpdate);
}

```

**Updating Phase (Component is being re-rendered):**

**componentDidUpdate(prevProps, prevState):**

* Called after the component updates (re-renders)

* Good place to compare props/state and perform side effects

* Can call `setState` here, but must guard against infinite loops

* Example:

```javascript
componentDidUpdate(prevProps, prevState) {
  if (prevProps.userId !== this.props.userId) {
    // User changed, fetch new data
    this.fetchUserData(this.props.userId);
  }
}

```

**shouldComponentUpdate(nextProps, nextState):**

* Called before re-rendering

* Return `false` to prevent re-render (performance optimization)

* Compare current props/state with next props/state

* Similar to `React.memo` for function components

* Example:

```javascript
shouldComponentUpdate(nextProps, nextState) {
  // Only re-render if count changed
  return nextState.count !== this.state.count;
}

```

**Unmounting Phase (Component is being removed from DOM):**

**componentWillUnmount():**

* Called before the component is unmounted (removed from DOM)

* Perfect place for cleanup: remove event listeners, cancel requests, clear timers

* Don't call `setState` here (component is being destroyed)

* Example:

```javascript
componentWillUnmount() {
  // Cleanup
  this.subscription.unsubscribe();
  clearInterval(this.timer);
  cancelRequest(this.requestId);
}

```

**Lifecycle Flow:**

```

Mounting: constructor → render → componentDidMount
Updating: shouldComponentUpdate → render → componentDidUpdate
Unmounting: componentWillUnmount

```

### 🔹 Hooks in Function Components

Hooks allow function components to use state and lifecycle features that were previously only available in class components. Hooks are the modern way to write React components.

**useState - Managing State:**

* Manages component state - equivalent to `this.state` in class components

* Returns an array: `[state, setState]`

* State updates trigger re-renders

* Can have multiple `useState` calls in one component

* Example:

```javascript
function Counter() {
  const [count, setCount] = useState(0);
  const [name, setName] = useState('John');

  return (
    <div>
      <p>{name}: {count}</p>
      <button onClick={() => setCount(count + 1)}>Increment</button>
    </div>
  );
}

```

**useEffect - Side Effects:**

* Runs after render - combines `componentDidMount`, `componentDidUpdate`, and `componentWillUnmount`

* The dependency array controls when it runs

* Return a cleanup function for cleanup logic

* Example:

```javascript
function UserProfile({ userId }) {
  const [user, setUser] = useState(null);

  useEffect(() => {
    // Runs after render, and when userId changes
    fetchUser(userId).then(setUser);

    return () => {
      // Cleanup: runs on unmount or before next effect
      cancelRequest();
    };
  }, [userId]); // Dependency array: only run when userId changes

  // Different effect for different purpose
  useEffect(() => {
    // Runs on every render (no dependency array)
    document.title = user ? `${user.name}'s Profile` : 'Profile';
  }); // No dependency array = runs every render

  // Effect that runs only once (like componentDidMount)
  useEffect(() => {
    console.log('Component mounted');
  }, []); // Empty array = runs only once
}

```

**useMemo - Memoizing Values:**

* Memoizes a value - only recomputes if dependencies change

* Useful for expensive calculations

* Returns the memoized value

* Example:

```javascript
function ExpensiveComponent({ items, filter }) {
  // Expensive calculation - only recompute when items or filter changes
  const filteredItems = useMemo(() => {
    return items.filter(item => item.category === filter);
  }, [items, filter]);

  return <List items={filteredItems} />;
}

```

**useCallback - Memoizing Functions:**

* Memoizes a function - prevents creating new function references on every render

* Useful when passing functions as props to memoized components

* Returns the memoized function

* Example:

```javascript
function Parent() {
  const [count, setCount] = useState(0);
  const [name, setName] = useState('John');

  // Without useCallback: new function on every render
  // const handleClick = () => console.log('clicked');

  // With useCallback: same function reference (unless dependencies change)
  const handleClick = useCallback(() => {
    console.log('clicked');
  }, []); // Empty array = function never changes

  return (
    <div>
      <ExpensiveChild onClick={handleClick} />
      {/* ExpensiveChild won't re-render unnecessarily */}
    </div>
  );
}

```

**Other Important Hooks:**

* **useRef**: Access DOM nodes or store mutable values that don't trigger re-renders

* **useContext**: Access React context values

* **useReducer**: Alternative to useState for complex state logic

* **useLayoutEffect**: Like useEffect but runs synchronously after DOM mutations

### 🔹 Hook Rules

Hooks have strict rules that must be followed. Breaking these rules causes bugs and unpredictable behavior.

**Rule 1: Only Call Hooks at the Top Level**

* Don't call hooks inside loops, conditions, or nested functions

* Always call them at the top level of your component

* This ensures hooks are called in the same order every render

* Example - Wrong:

```javascript
function Component({ condition }) {
  if (condition) {
    const [state, setState] = useState(0); // ❌ Wrong!
  }

  for (let i = 0; i < 10; i++) {
    useEffect(() => {}); // ❌ Wrong!
  }
}

```

* Example - Correct:

```javascript
function Component({ condition }) {
  const [state, setState] = useState(0); // ✅ Correct

  useEffect(() => {
    if (condition) {
      // Use condition inside effect, not to conditionally call hook
    }
  }, [condition]);
}

```

**Rule 2: Only Call Hooks from React Functions**

* Hooks only work in function components or custom hooks

* Don't call hooks from regular JavaScript functions

* Example - Wrong:

```javascript
function regularFunction() {
  const [state, setState] = useState(0); // ❌ Wrong!
}

function Component() {
  regularFunction(); // This will error
}

```

* Example - Correct:

```javascript
function useCustomHook() { // ✅ Custom hook (starts with "use")
  const [state, setState] = useState(0);
  return state;
}

function Component() {
  const value = useCustomHook(); // ✅ Correct
}

```

**Why These Rules Exist:**

* React relies on hooks being called in the same order every render

* React stores hook state in an array internally

* If hooks are called conditionally, the order changes, and React gets confused

* This is why you can't conditionally call hooks

**Example - How React Tracks Hooks:**

```javascript
// First render
function Component() {
  useState(0);  // Hook 1
  useState(''); // Hook 2
  useEffect(() => {}); // Hook 3
}

// Second render (hooks called in same order)
function Component() {
  useState(0);  // Hook 1 (same)
  useState(''); // Hook 2 (same)
  useEffect(() => {}); // Hook 3 (same)
}

// If order changes, React gets confused!
function Component({ condition }) {
  if (condition) {
    useState(0);  // Hook 1 (sometimes)
  }
  useState(''); // Hook 2 (or Hook 1 if condition is false!)
  // React can't match hooks correctly!
}

```

📌 **In simple terms**: Class components have lifecycle methods like componentDidMount. Hooks give function components the same functionality - useState for state, useEffect for side effects, useMemo and useCallback for optimization. The catch is you must follow the rules: call hooks at the top level and in the same order every render.

---

### 🔹 💡 Fiber Architecture

Fiber Architecture is React’s new reconciliation engine introduced in React 16 that allows React to break rendering work into small units, pause, resume, and prioritize updates, and keep the UI smooth and responsive.

### 🔹 Fiber Node

A Fiber Node is the basic unit of work in React Fiber architecture.
It represents one React component (or element) and stores everything React needs to manage rendering, updates, and scheduling for that component.

**What is a Fiber Node:**

* Each component or DOM node is represented as a fiber node

* It's the unit of work in React - React works on one fiber at a time

* A fiber node contains:
  * Component info (type, props, state)
  * Links to other fibers (parent, child, sibling)
  * Work information (what needs to be done)
  * Priority information (how urgent the work is)

* Forms a tree structure (fiber tree)

**Fiber Node Structure:**

```javascript
// Simplified fiber node structure
{
  type: Component,           // Component function/class
  props: {...},              // Component props
  state: {...},              // Component state
  child: Fiber,              // First child fiber
  sibling: Fiber,            // Next sibling fiber
  return: Fiber,             // Parent fiber
  alternate: Fiber,          // Link to other tree
  effectTag: 'UPDATE',       // What needs to be done
  expirationTime: 1000,      // Priority/urgency
  // ... more fields
}

```

**Why Fiber Matters:**

* Allows React to pause and resume work (interruptible rendering)

* Enables priority-based scheduling (important work first)

* Makes React more responsive (doesn't block the main thread)

* Foundation for concurrent features (React 18+)

### 🔹 Fiber Tree

The Fiber Tree is a tree of Fiber Nodes that represents the entire React component hierarchy, including each component’s state, props, effects, and priority.

React maintains two fiber trees simultaneously. This is a double buffering technique that enables concurrent rendering.

**Current Tree (What's on Screen):**

* Represents what's currently rendered on screen

* This is the "committed" tree - the DOM matches this tree

* Users see the UI based on this tree

* Stable - doesn't change during render phase

**WorkInProgress Tree (What React is Building):**

* What React is building during the render phase

* React creates this tree while working on updates

* Not yet committed to the DOM

* Can be discarded if a higher priority update comes in

**Double Buffering:**

* React can work on the new tree while the current one is displayed

* Similar to video game rendering (render next frame while showing current frame)

* Allows React to pause and resume work without affecting what's on screen

* When work is complete, trees swap (workInProgress becomes current)

**Example:**

```javascript
// Initial render
// Current tree: [App] -> [Header] -> [Content]
// WorkInProgress tree: (none, or same as current)

// User clicks button, state updates
// Current tree: [App] -> [Header] -> [Content] (still showing this)
// WorkInProgress tree: [App] -> [Header] -> [Content (updated)] (building this)

// Render phase completes
// Current tree: [App] -> [Header] -> [Content (old)]
// WorkInProgress tree: [App] -> [Header] -> [Content (new)]

// Commit phase - swap trees
// Current tree: [App] -> [Header] -> [Content (new)] (now showing this)
// WorkInProgress tree: (becomes new current, or discarded)

```

**Benefits:**

* Can pause work for high-priority updates

* Can discard work if it becomes stale

* Keeps UI responsive (always showing stable current tree)

* Enables concurrent features

### 🔹 Fiber Features

Fiber enables several powerful features that make React more responsive and performant:

**Incremental Rendering:**

* React can split work into small chunks (fiber nodes)

* Can pause work for high-priority updates (like user input)

* Can resume work later where it left off

* Keeps the UI responsive - doesn't block the main thread

* Example: User types in input while React is rendering a large list - React pauses list rendering, handles input, then resumes list rendering

**Priority Scheduling:**

* React prioritizes work based on urgency

* **High Priority**: User input, animations, interactions (must be immediate)

* **Medium Priority**: Data fetching, updates from network (important but not urgent)

* **Low Priority**: Offscreen updates, background work (can wait)

* Important work gets done first, less important work can be interrupted

* Example: User clicks button (high priority) interrupts background data fetch (medium priority)

**Time Slicing:**

* React works in small time slices (typically 5ms)

* Works on a few fibers, then checks for high-priority work

* If high-priority work exists, pauses current work and handles it

* Keeps the UI responsive - prevents long-running renders from blocking

* Example: Rendering 1000 components - React renders 10, checks for input, renders 10 more, checks again, etc.

**Concurrent Features (React 18+):**

* **useTransition**: Mark updates as non-urgent

* **useDeferredValue**: Defer updating a value

* **Suspense**: Better loading states

* All built on top of Fiber's ability to pause and resume work

### 🔹 Fiber Work Phases

Fiber work happens in two distinct phases. Understanding these phases helps you understand when things happen in React.

**Render Phase (Interruptible):**

* React builds the workInProgress tree

* Determines what changed (reconciliation, diffing)

* Can be interrupted for higher priority work

* No side effects yet - doesn't update DOM, doesn't run effects

* Pure computation - can be paused and resumed

* Can be discarded if a higher priority update comes in

* Example: User clicks button while React is in render phase - React pauses render, handles click, then resumes render

**Commit Phase (Synchronous, Cannot be Interrupted):**

* React updates the DOM based on workInProgress tree

* Runs effects (useEffect, componentDidMount, etc.)

* Updates refs

* All side effects happen here

* Must be synchronous - can't be interrupted

* Happens quickly (usually < 16ms for 60fps)

* Example: After render phase completes, commit phase updates DOM and runs effects

**Why Two Phases:**

* Render phase can be interrupted (keeps UI responsive)

* Commit phase must be synchronous (ensures consistency)

* Separates computation (render) from side effects (commit)

* Enables concurrent features (interruptible rendering)

**Example Flow:**

```javascript
// User clicks button
// 1. Render Phase (interruptible)
//    - Build workInProgress tree
//    - Determine what changed
//    - Can be interrupted if higher priority work comes in

// 2. Commit Phase (synchronous)
//    - Update DOM
//    - Run useEffect callbacks
//    - Update refs
//    - Cannot be interrupted

```

📌 **In simple terms**: Fiber is React's reconciliation engine. Each component is a fiber node in a tree. This allows React to pause and resume work, prioritize important updates, and keep the UI responsive. Work is split into render phase (interruptible, no side effects) and commit phase (synchronous, updates DOM).

---

### 🔹 📦 State Management & Updates

### 🔹 State Updates

React batches state updates for performance:

* **setState (Class Components)**: Multiple setState calls in the same event handler get batched together into one re-render - you can also use functional updates when the new state depends on the previous state

* **useState (Function Components)**: Same batching behavior in React 18+ - multiple useState updates in the same event handler result in one re-render

### 🔹 State Update Batching

React batches state updates for performance. Understanding batching helps you write more efficient code.

**Automatic Batching (React 18+):**

* All state updates are automatically batched together

* Works in event handlers, promises, setTimeout, native event handlers, etc.

* You get one re-render instead of multiple

* More efficient - fewer renders, better performance

* Example:

```javascript
function handleClick() {
  setCount(c => c + 1);  // Update 1
  setFlag(f => !f);      // Update 2
  setName('John');       // Update 3
  // All three updates batched into one re-render
}

```

**Manual Batching (React 17 and earlier):**

* Only updates in React event handlers were batched

* Async updates (promises, setTimeout) weren't batched

* Had to use `ReactDOM.unstable_batchedUpdates()` to batch manually

* Example (React 17):

```javascript
// Not batched in React 17
setTimeout(() => {
  setCount(c => c + 1);  // Re-render 1
  setFlag(f => !f);      // Re-render 2
}, 1000);

// Had to manually batch
setTimeout(() => {
  ReactDOM.unstable_batchedUpdates(() => {
    setCount(c => c + 1);  // Batched
    setFlag(f => !f);      // Batched
  });
}, 1000);

```

**React 18 Improvement:**

* Automatic batching everywhere

* No need for `unstable_batchedUpdates`

* Better performance out of the box

* More predictable behavior

### 🔹 State Update Flow

Here's what happens when you update state:

1. You call setState or useState setter (state update gets queued)

2. React batches multiple updates together (if these updates are in the same event handler)

3. React schedules a re-render

4. Render phase runs (component re-renders, creates new Virtual DOM)

5. Commit phase runs (DOM gets updated with the changes)

**Example:**

```javascript
function handleClick() {
  setCount(c => c + 1);  // These get batched
  setFlag(f => !f);      // into one re-render
  // Only one re-render happens, not two
}

```

📌 **In simple terms**: React batches state updates automatically. If you call setState multiple times in the same event handler, React combines them into one re-render. Use functional updates (like `setCount(c => c + 1)`) when the new state depends on the previous state. React 18+ batches everywhere automatically.

---

### 🔹 🎯 Event System

### 🔹 SyntheticEvent

React wraps native browser events in SyntheticEvent objects. This provides a consistent event interface across all browsers.

**What is SyntheticEvent:**

* A wrapper around native browser events

* Normalizes differences between browsers (IE vs Chrome vs Firefox)

* Events work the same way everywhere

* Same interface as native events (mostly)

* Example: `onClick`, `onChange`, `onSubmit` all use SyntheticEvent

**Why SyntheticEvent:**

* **Cross-browser consistency**: Events work the same in all browsers

* **Normalization**: Handles browser differences automatically

* **Performance**: Can optimize event handling

* **Event pooling (React 16)**: Reused event objects for performance (removed in React 17+)

**Event Pooling (React 16 and earlier):**

* React reused event objects for performance

* Events were nullified after the event handler finished

* Had to call `event.persist()` to keep the event

* Example (React 16):

```javascript
function handleClick(event) {
  // Event object is pooled
  setTimeout(() => {
    console.log(event.type); // null! Event was nullified
  }, 100);

  // Had to persist
  event.persist();
  setTimeout(() => {
    console.log(event.type); // 'click' - now it works
  }, 100);
}

```

**React 17+ Changes:**

* Removed event pooling - events are no longer nullified

* Events work more like native events

* No need for `event.persist()` anymore

* Better developer experience

**SyntheticEvent Interface:**

* Same methods as native events: `preventDefault()`, `stopPropagation()`, `stopImmediatePropagation()`

* Same properties: `target`, `currentTarget`, `type`, `timeStamp`

* Additional properties: `nativeEvent` (access to native event), `isDefaultPrevented()`, `isPropagationStopped()`

* Example:

```javascript
function handleClick(event) {
  event.preventDefault();        // Prevent default behavior
  event.stopPropagation();       // Stop event bubbling
  console.log(event.target);     // Element that triggered event
  console.log(event.type);       // 'click'
}

```

### 🔹 Event Delegation

React uses event delegation for efficiency. Instead of attaching listeners to every element, React uses a single listener on the root.

**How Event Delegation Works:**

* React attaches one event listener to the root element (usually `#root` or `document`)

* Events bubble up to the root naturally (DOM event bubbling)

* React figures out which handler to call based on where the event came from

* More efficient than attaching individual listeners to every element

**Why Event Delegation:**

* **Performance**: One listener instead of thousands

* **Memory**: Less memory usage (fewer listeners)

* **Dynamic elements**: Works with dynamically added elements automatically

* **Consistency**: All events go through the same system

**Example:**

```javascript
// Without event delegation (what you might do manually)
document.querySelectorAll('button').forEach(button => {
  button.addEventListener('click', handleClick); // Many listeners
});

// With React's event delegation (what React does)
// One listener on root
document.getElementById('root').addEventListener('click', (event) => {
  // React figures out which component's handler to call
  // Based on event.target and component tree
});

```

**How React Determines Handler:**

* React maintains a mapping of event handlers to components

* When event bubbles to root, React checks `event.target`

* Finds the component that should handle the event

* Calls the appropriate handler

* This is why React events work even with dynamic components

### 🔹 Event Handlers

You can write event handlers in different ways:

* **Inline**: `<button onClick={() => console.log('clicked')}>Click</button>`

* **Reference**: `<button onClick={handleClick}>Click</button>`

* **With parameters**: `<button onClick={(e) => handleClick(id, e)}>Click</button>`

📌 **In simple terms**: React wraps native events in SyntheticEvent for consistency across browsers. It uses event delegation - one listener on the root instead of many individual listeners. React 17+ removed event pooling, so events work more like native events now.

---

### 🔹 🎨 Rendering & Batching

### 🔹 Rendering Process

* **Initial Render**: Component renders (returns JSX), creates React elements, builds Virtual DOM tree, reconciles with real DOM, commits changes to DOM

* **Re-render**: State or props change, component re-renders, creates new Virtual DOM tree, diffs with previous tree, updates only changed parts

### 🔹 When Components Re-render

Understanding when components re-render helps you optimize performance and debug issues.

**Triggers for Re-renders:**

**1. State Changes:**

* `setState()` in class components

* `useState` setter in function components

* State update triggers re-render

* Example:

```javascript
function Component() {
  const [count, setCount] = useState(0);

  // This triggers re-render
  setCount(1);
}

```

**2. Props Change:**

* Parent passes new props to child

* Child re-renders with new props

* Even if props are the same (by reference), child re-renders

* Example:

```javascript
function Parent() {
  const [name, setName] = useState('John');

  return <Child name={name} />; // Child re-renders when name changes
}

```

**3. Parent Re-renders:**

* When parent re-renders, all children re-render by default

* Unless child is memoized with `React.memo`

* This is why memoization is important

* Example:

```javascript
function Parent() {
  const [count, setCount] = useState(0);

  return (
    <div>
      <ExpensiveChild /> {/* Re-renders even though props didn't change */}
    </div>
  );
}

// Solution: Memoize
const ExpensiveChild = React.memo(() => {
  // Only re-renders if props change
});

```

**4. Context Changes:**

* Component using context re-renders when context value changes

* All consumers of that context re-render

* This is why context should be used carefully

* Example:

```javascript
const ThemeContext = createContext();

function App() {
  const [theme, setTheme] = useState('light');

  return (
    <ThemeContext.Provider value={theme}>
      <ThemedComponent /> {/* Re-renders when theme changes */}
    </ThemeContext.Provider>
  );
}

```

**5. Force Update:**

* `this.forceUpdate()` in class components

* Forces a re-render even if state/props didn't change

* Should be avoided - usually indicates a design issue

* Example:

```javascript
class Component extends React.Component {
  handleClick = () => {
    this.forceUpdate(); // Forces re-render
  };
}

```

**Important Notes:**

* Re-rendering doesn't mean DOM updates (React is smart about this)

* React only updates DOM if Virtual DOM actually changed

* Memoization prevents unnecessary re-renders

* Understanding re-render triggers helps optimize performance

### 🔹 Preventing Unnecessary Re-renders

You can prevent unnecessary re-renders with memoization:

* **React.memo**: Wraps a component and skips re-rendering if props haven't changed - useful for expensive components

* **useMemo**: Memoizes a value - only recomputes if dependencies change - useful for expensive calculations

* **useCallback**: Memoizes a function - prevents creating new function references on every render - useful when passing functions as props

**Example:**

```javascript
// Memoize component
const MemoizedComponent = React.memo(Component);

// Memoize value
const expensiveValue = useMemo(() => computeValue(a, b), [a, b]);

// Memoize callback
const handleClick = useCallback(() => {
  doSomething(id);
}, [id]);

```

📌 **In simple terms**: When a component renders, it returns JSX, creates a Virtual DOM tree, reconciles with the previous tree, and commits changes to the DOM. Components re-render when state/props change or when the parent re-renders. Use React.memo, useMemo, and useCallback to prevent unnecessary re-renders and expensive recalculations.

---

### 🔹 ⚡ Performance Optimizations

### 🔹 Code Splitting

Code splitting splits your code into smaller chunks that load on demand. This reduces initial bundle size and improves load time.

**Why Code Split:**

* Reduces initial bundle size (faster initial load)

* Only load code when needed (better performance)

* Better user experience (faster Time to Interactive)

* Can split by route, feature, or component

**React.lazy() and Suspense:**

* `React.lazy()` dynamically imports a component

* Component is loaded when it's rendered

* `Suspense` provides fallback UI while loading

* Example:

```javascript
// Lazy load a component
const LazyComponent = React.lazy(() => import('./LazyComponent'));

function App() {
  return (
    <Suspense fallback={<Loading />}>
      <LazyComponent />
    </Suspense>
  );
}

```

**Route-based Code Splitting:**

* Split code by route (most common pattern)

* Each route loads its own bundle

* Example:

```javascript
import { lazy, Suspense } from 'react';
import { BrowserRouter, Routes, Route } from 'react-router-dom';

const Home = lazy(() => import('./pages/Home'));
const About = lazy(() => import('./pages/About'));
const Contact = lazy(() => import('./pages/Contact'));

function App() {
  return (
    <BrowserRouter>
      <Suspense fallback={<div>Loading...</div>}>
        <Routes>
          <Route path="/" element={<Home />} />
          <Route path="/about" element={<About />} />
          <Route path="/contact" element={<Contact />} />
        </Routes>
      </Suspense>
    </BrowserRouter>
  );
}

```

**Component-based Code Splitting:**

* Split large components that aren't always visible

* Example: Modal, drawer, heavy charts

* Example:

```javascript
const HeavyChart = lazy(() => import('./HeavyChart'));

function Dashboard() {
  const [showChart, setShowChart] = useState(false);

  return (
    <div>
      <button onClick={() => setShowChart(true)}>Show Chart</button>
      {showChart && (
        <Suspense fallback={<ChartSkeleton />}>
          <HeavyChart />
        </Suspense>
      )}
    </div>
  );
}

```

**Build Tool Configuration:**

* Webpack automatically splits code when using dynamic imports

* Creates separate chunks for each lazy-loaded component

* Chunks are loaded on demand

* Example output: `main.js`, `Home.chunk.js`, `About.chunk.js`

### 🔹 Memoization

Memoization prevents unnecessary work:

* **React.memo**: Prevents component re-renders if props haven't changed

* **useMemo**: Prevents recalculating expensive values

* **useCallback**: Prevents creating new function references

* **Trade-off**: Uses more memory, but saves CPU time

### 🔹 Virtualization

Virtualization (or windowing) only renders visible items in long lists. This dramatically improves performance for large datasets.

**The Problem:**

* Rendering thousands of list items is slow

* DOM becomes heavy with many elements

* Scrolling becomes laggy

* Memory usage increases

**The Solution:**

* Only render items that are visible (plus a few buffer items)

* As user scrolls, render new items and unmount offscreen items

* Keeps DOM lightweight

* Example: List with 10,000 items, but only 20 are visible - only render 20

**How It Works:**

* Calculate which items are visible based on scroll position

* Render only visible items

* Use absolute positioning to maintain scroll height

* As user scrolls, update which items are visible

**Libraries:**

* **react-window**: Lightweight, simple API

* **react-virtualized**: More features, larger bundle

* Example with react-window:

```javascript
import { FixedSizeList } from 'react-window';

function VirtualizedList({ items }) {
  const Row = ({ index, style }) => (
    <div style={style}>
      {items[index].name}
    </div>
  );

  return (
    <FixedSizeList
      height={600}
      itemCount={items.length}
      itemSize={50}
      width="100%"
    >
      {Row}
    </FixedSizeList>
  );
}

```

**When to Use:**

* Lists with hundreds or thousands of items

* Tables with many rows

* Long feeds or timelines

* Any scrollable list with many items

**Benefits:**

* Much better performance (only renders visible items)

* Lower memory usage

* Smooth scrolling

* Works with any number of items

### 🔹 Other Optimizations

**Keys in Lists:**

* Help React identify which items changed

* Use stable IDs, not array indices

* Prevents unnecessary re-renders and DOM updates

* Example:

```javascript
// Bad
{items.map((item, index) => <Item key={index} data={item} />)}

// Good
{items.map(item => <Item key={item.id} data={item} />)}

```

**Avoid Inline Functions/Objects:**

* Creating new functions/objects in render creates new references

* Causes child components to re-render unnecessarily

* Create them outside render or memoize them

* Example:

```javascript
// Bad - new function every render
function Parent() {
  return <Child onClick={() => handleClick()} />;
}

// Good - stable reference
function Parent() {
  const handleClick = useCallback(() => {
    // ...
  }, []);
  return <Child onClick={handleClick} />;
}

```

**useTransition (React 18+):**

* Mark updates as non-urgent

* React can prioritize more important work

* Useful for non-critical updates

* Example:

```javascript
function SearchResults({ query }) {
  const [isPending, startTransition] = useTransition();

  const handleSearch = (newQuery) => {
    startTransition(() => {
      setQuery(newQuery); // Non-urgent update
    });
  };

  return (
    <div>
      {isPending && <Spinner />}
      <Results query={query} />
    </div>
  );
}

```

**useDeferredValue (React 18+):**

* Defer updating a value until React has time

* Useful for search inputs, filters

* Keeps UI responsive

* Example:

```javascript
function SearchInput() {
  const [query, setQuery] = useState('');
  const deferredQuery = useDeferredValue(query);

  return (
    <div>
      <input value={query} onChange={e => setQuery(e.target.value)} />
      <Results query={deferredQuery} /> {/* Updates deferred */}
    </div>
  );
}

```

**Performance Tips:**

* Use React DevTools Profiler to find bottlenecks

* Don't optimize prematurely - measure first

* Memoization has costs (memory) - use wisely

* Code splitting and virtualization have biggest impact

📌 **In simple terms**: Performance optimizations include code splitting (load code on demand), memoization (prevent unnecessary work), virtualization (only render visible items in long lists), proper keys, and avoiding inline functions/objects. Use React DevTools Profiler to find bottlenecks before optimizing.

---

## ⭐ Summary — 10-second Interview Version

> "React is component-based and declarative - you describe what the UI should look like, React handles the DOM updates. Virtual DOM is React's JavaScript copy of the real DOM. Reconciliation compares old and new Virtual DOM (diffing), then updates only what changed in the real DOM. Fiber architecture allows React to pause and resume work, prioritizing important updates. Hooks give function components state and lifecycle features. React batches state updates automatically. Uses SyntheticEvent for cross-browser consistency and event delegation for efficiency. Optimize with code splitting, memoization, and virtualization."

---

## ⭐ Extra Points (If Interviewer Asks More)

### What's the difference between Virtual DOM and Real DOM?

Virtual DOM is React's JavaScript representation of the DOM - it's a lightweight copy that React uses to figure out what changed. The real DOM is the actual browser DOM that users see. React compares the old and new Virtual DOM (reconciliation), then updates only the changed parts in the real DOM. This is faster than directly manipulating the real DOM because Virtual DOM operations are cheap JavaScript operations.

### How does React's reconciliation algorithm work?

React's reconciliation (diffing algorithm) compares the old and new Virtual DOM trees. It assumes elements of the same type in the same position are the same element, so it only updates what changed. Keys help React identify which items changed, were added, or removed in lists. React uses a heuristic algorithm (not perfect diffing) for performance - it's O(n) complexity instead of O(n³) for perfect diffing.

### What's the purpose of React Fiber?

React Fiber is a reimplementation of React's reconciliation algorithm that allows React to pause, abort, or reuse work as priorities change. It enables features like concurrent rendering, where React can interrupt low-priority updates to handle high-priority updates (like user input) immediately. Fiber makes React more responsive and allows features like Suspense and concurrent mode.

---

## 📍 Navigation

<div align="center">

[← Previous: TypeScript Internals](08%29%20TypeScript%20Internals.md) • [Home: Questions Index](question.md) • [Next: Next.js Internals →](10%29%20Next.js%20Internals.md)

[📋 Cheatsheet](FE-System-Design%20Interview%20Cheatsheet.md)

</div>

---
