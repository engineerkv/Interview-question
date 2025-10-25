
# ⚛️ React.js Interview Notes (2025 Edition)

## 🟢 Section 1 — React Fundamentals (Basics  Intermediate)

---

### 1. 🧠 What is React, and why is it used for building UI?

**🧠 Concept**

React is a JavaScript library for building user interfaces. It uses reusable components that update automatically when data changes.

**💻 Example**
```jsx
function App() {
  return <h1>Hello React!</h1>;
}
```

**💬 Explanation + Insight**

- **UI Library** - React is just for building user interfaces
- **Virtual DOM** - Uses Virtual DOM to make updates fast
- **Reusable Components** - Components are like LEGO blocks
- **Declarative** - You describe what you want, React figures out how to do it
- **Automatic Updates** - No need to manually update the DOM

---

### 2. 🧠 What problems does React solve compared to vanilla JS or jQuery?

**🧠 Concept**

React makes DOM updates easier and faster compared to vanilla JS or jQuery by handling updates automatically.

**💻 Example**
```js
// jQuery - manual DOM updates
$('#msg').text('Hello, World!');

// React - automatic updates
function Message() {
  return <h1>Hello, World!</h1>;
}
```

**💬 Explanation + Insight**


- **Manual DOM Updates** - Vanilla JS/jQuery: you manually change the DOM
- **Automatic Updates** - React: you just change data, React updates DOM for you
- **Performance** - React is faster because it only changes what actually changed
- **Fewer Bugs** - Less bugs because you don't touch the DOM directly
- **No jQuery Mixing** - Don't mix jQuery with React - it causes problems

---

### 3. 🧠 What is the Virtual DOM, and how does React use it?

**🧠 Concept**

The Virtual DOM is a copy of the real DOM that React keeps in memory to make updates faster.

**💻 Example**
```jsx
setCount(count + 1); // React compares old vs new and updates only what changed
```

**💬 Explanation + Insight**

- Virtual DOM is like a draft of your webpage in memory
- React compares old draft vs new draft
- Only changes the real webpage where needed
- Much faster than changing the real DOM directly
- Uses more memory but makes updates much faster

---

### 4. 🧠 What is JSX, and how does it differ from HTML?

**🧠 Concept**

JSX lets you write HTML-like code inside JavaScript files. It gets converted to regular JavaScript.

**💻 Example**
```jsx
const heading = <h1 className="title">Welcome!</h1>;
// Becomes:
React.createElement('h1', { className: 'title' }, 'Welcome!');
```

**💬 Explanation + Insight**

- JSX looks like HTML but it's actually JavaScript
- Use `className` instead of `class` (because class is a reserved word)
- Use `onClick` instead of `onclick` (camelCase)
- You can put JavaScript inside {} curly braces
- Babel converts JSX to regular JavaScript before running

---

### 5. 🧠 What are components in React?

**🧠 Concept**

Components are like LEGO blocks - reusable pieces of UI that you can combine to build bigger things.

**💻 Example**
```jsx
function Button({ label }) {
  return <button>{label}</button>;
}
```

**💬 Explanation + Insight**

- Components are just functions that return JSX
- You can reuse the same component many times
- Pass different data to the same component (like different button labels)
- Build big apps by combining small components
- Each component does one thing well

---

### 6. 🧠 Difference between functional and class components

**🧠 Concept**

Functional components are simple functions, while class components use the `class` keyword and are more complex.

**💻 Example**
```jsx
// Functional - simple function
function Welcome() { return <h1>Hello</h1>; }

// Class - uses class keyword
class Welcome extends React.Component {
  render() { return <h1>Hello</h1>; }
}
```

**💬 Explanation + Insight**

- Functional components are just functions that return JSX
- Class components use `class` and have a `render()` method
- Functional components are easier to write and understand
- Everyone uses functional components now (with hooks)
- Class components are old but still work

---

### 7. 🧠 What are props, and how are they passed between components?

**🧠 Concept**

Props are like function parameters - they let you pass data from parent components to child components.

**💻 Example**
```jsx
function Greeting({ name }) {
  return <p>Hello, {name}</p>;
}
<Greeting name="Kamal" />
```

**💬 Explanation + Insight**

- Props are data you pass down from parent to child
- Child components can't change props (they're read-only)
- Like passing arguments to a function
- Makes components reusable with different data
- Data flows down from parent to child

---

### 8. 🧠 What is state in React, and how does it differ from props?

**🧠 Concept**

State is data that belongs to a component and can change, while props are data passed from outside that can't be changed.

**💻 Example**
```jsx
function Counter() {
  const [count, setCount] = useState(0);
  return <button onClick={() => setCount(count + 1)}>{count}</button>;
}
```

**💬 Explanation + Insight**

- State: data that the component owns and can change
- Props: data passed from parent that component can't change
- When state changes, the component re-renders
- Use state for things that change (like counters, form inputs)
- Use props for data that comes from outside

---

### 9. 🧠 What is one-way data flow in React?

**🧠 Concept**

Data flows in one direction: from parent components down to child components. Children can't change parent data directly.

**💻 Example**
```jsx
function Parent() {
  const [name, setName] = useState('Kamal');
  return <Child name={name} onChange={setName} />;
}
```

**💬 Explanation + Insight**

- Data flows down: parent  child
- Child can't change parent's data directly
- Child can ask parent to change data (using callbacks)
- Like a waterfall - data flows down, requests flow up
- Makes code easier to understand and debug

---

### 10. 🧠 What are controlled and uncontrolled components?

**🧠 Concept**

Controlled components let React manage form inputs, while uncontrolled components let the browser manage them.

**💻 Example**
```jsx
// Controlled - React manages the value
<input value={name} onChange={e => setName(e.target.value)} />

// Uncontrolled - browser manages the value
<input ref={inputRef} />
```

**💬 Explanation + Insight**

- Controlled: React knows the value and controls it
- Uncontrolled: browser handles the value, React doesn't know it
- Controlled is usually better - easier to work with
- Use controlled for forms you need to validate
- Use uncontrolled only when you need to access the DOM directly


### 11. 🧠 What is the `key` prop, and why is it important in lists?

**🧠 Concept**

The `key` prop helps React identify which items in a list have changed, been added, or removed.

**💻 Example**
```jsx
{users.map(user => (
  <li key={user.id}>{user.name}</li>
))}
```

**💬 Explanation + Insight**

- Keys are like name tags for list items
- React uses keys to track which items changed
- Without keys, React gets confused and re-renders everything
- Use unique IDs as keys (like user.id)
- Don't use array index as key - it causes bugs when items move

---

### 12. 🧠 What are fragments, and when should you use them?

**🧠 Concept**

Fragments let you group multiple elements together without adding an extra wrapper element to the DOM.

**💻 Example**
```jsx
return (
  <>
    <h1>Title</h1>
    <p>Description</p>
  </>
);
```

**💬 Explanation + Insight**

- React normally requires one parent element
- Fragments let you group elements without extra `<div>`
- Use `<>` and `</>` for simple cases
- Use `<React.Fragment>` when you need to add keys
- Keeps your HTML clean without extra wrapper divs

---

### 13. 🧠 What is reconciliation in React?

**🧠 Concept**

Reconciliation is how React figures out what changed and updates only those parts of the webpage.

**💻 Example**
```jsx
setCount(count + 1); // React figures out what changed and updates it
```

**💬 Explanation + Insight**

- React compares old webpage with new webpage
- Only changes the parts that are different
- Skips parts that didn't change (saves time)
- Like a smart diff tool for webpages
- Makes React much faster than updating everything

---

### 14. 🧠 What is `React.StrictMode` used for?

**🧠 Concept**

`StrictMode` is like a helpful teacher that finds problems in your code during development.

**💻 Example**
```jsx
<React.StrictMode>
  <App />
</React.StrictMode>
```

**💬 Explanation + Insight**

- Only works when developing, not in production
- Runs your components twice to catch bugs
- Warns you about unsafe code
- Helps you write better React code
- Always use it when building your app

---

### 15. 🧠 What is a synthetic event in React?

**🧠 Concept**

Synthetic events are React's way of making browser events work the same across all browsers.

**💻 Example**
```jsx
function handleClick(e) {
  console.log(e.nativeEvent); // access the real browser event
}
<button onClick={handleClick}>Click</button>
```

**💬 Explanation + Insight**

- React wraps browser events to make them consistent
- Works the same in Chrome, Firefox, Safari, etc.
- React reuses event objects to save memory
- Call `e.persist()` if you need the event later
- Makes cross-browser development easier

---

### 16. 🧠 What are portals, and when are they useful?

**🧠 Concept**

Portals let you render a component somewhere else in the DOM, not where it normally would be.

**💻 Example**
```jsx
ReactDOM.createPortal(
  <ModalContent />,
  document.getElementById('modal-root')
);
```

**💬 Explanation + Insight**

- Like teleporting a component to a different place
- Useful for modals, tooltips, dropdowns
- Helps when parent CSS is hiding your component
- Component still behaves like a normal React component
- Events still work normally even though it's rendered elsewhere

---

### 17. 🧠 What are render props?

**🧠 Concept**

Render props are functions you pass to components that control how the component displays content.

**💻 Example**
```jsx
function DataProvider({ render }) {
  return render('Hello from render prop!');
}

<DataProvider render={data => <p>{data}</p>} />;
```

**💬 Explanation + Insight**

- Parent component passes a function to child
- Child component calls that function to render content
- Used for sharing code between components
- Now mostly replaced by custom hooks (which are easier)
- Still useful for some special cases

---

### 18. 🧠 What are higher-order components (HOCs)?

**🧠 Concept**

HOCs are functions that take a component and give it extra powers, then return the enhanced component.

**💻 Example**
```jsx
function withLogger(WrappedComponent) {
  return function(props) {
    console.log('Props:', props);
    return <WrappedComponent {...props} />;
  };
}
```

**💬 Explanation + Insight**

- Like putting a wrapper around a component
- Used to add logging, permissions, data fetching
- Can get messy with lots of wrappers
- Now mostly replaced by custom hooks (which are cleaner)
- Still useful for some special cases

---

### 19. 🧠 What are `children` in React, and how can you manipulate them?

**🧠 Concept**

`children` is a special prop that lets you put content inside a component, between the opening and closing tags.

**💻 Example**
```jsx
function Card({ children }) {
  return <div className="card">{children}</div>;
}
<Card><p>Inside card</p></Card>;
```

**💬 Explanation + Insight**

- Like putting content inside a box
- Whatever you put between tags becomes `children`
- Use `React.Children.map()` to loop through children
- Use `React.cloneElement()` to change child props
- Essential for layout components like cards, modals

---

### 20. 🧠 How does React handle conditional rendering?

**🧠 Concept**

React uses regular JavaScript to decide what to show - if statements, &&, and ternary operators.

**💻 Example**
```jsx
{isLoggedIn ? <Dashboard /> : <Login />}
{count > 0 && <p>You have {count} items.</p>}
```

**💬 Explanation + Insight**

- Use `if`, `&&`, or `? :` just like regular JavaScript
- React skips `false`, `null`, `undefined` (doesn't render them)
- But renders `0` and empty strings
- No special React syntax needed
- Makes your UI change based on data


### 21. 🧠 What is an Error Boundary?

**🧠 Concept**

Error Boundaries are like safety nets that catch errors in child components and show a fallback UI instead of crashing the whole app.

**💻 Example**
```jsx
class ErrorBoundary extends React.Component {
  state = { hasError: false };

  static getDerivedStateFromError() {
    return { hasError: true };
  }

  componentDidCatch(error, info) {
    console.log('Error:', error, info);
  }

  render() {
    return this.state.hasError ? <h2>Something went wrong.</h2> : this.props.children;
  }
}
```

**💬 Explanation + Insight**

- Like a safety net for your components
- Only catches errors during rendering (not in event handlers)
- Shows a fallback UI when something breaks
- Prevents one broken component from crashing the whole app
- Wrap risky components with Error Boundaries

---

### 22. 🧠 What is the difference between Composition and Inheritance?

**🧠 Concept**

React prefers composition over inheritance — build big components by combining small ones, not by extending them.

**💻 Example**
```jsx
function Card({ header, children }) {
  return (
    <div className="card">
      <h3>{header}</h3>
      <div>{children}</div>
    </div>
  );
}
<Card header="Title">Content here</Card>;
```

**💬 Explanation + Insight**

- Composition: combine small pieces to make big things (like LEGO)
- Inheritance: extend components like in object-oriented programming
- Composition is more flexible and easier to understand
- Inheritance creates tight connections between components
- Use composition with props, children, and context

---

### 23. 🧠 What is React's Declarative Programming Model?

**🧠 Concept**

React uses declarative programming — you describe what you want the UI to look like, and React figures out how to make it happen.

**💻 Example**
```jsx
// Declarative - describe what you want
{isLoggedIn ? <Dashboard /> : <Login />}

// Imperative - describe how to do it
if (isLoggedIn) showDashboard(); else showLogin();
```

**💬 Explanation + Insight**

- Declarative: tell React what you want, not how to do it
- Imperative: give step-by-step instructions
- React handles all the DOM updates for you
- Less bugs because you don't manage the DOM directly
- Code is easier to read and understand

---

### 24. 🧠 What are Pure Components?

**🧠 Concept**

Pure Components are smart components that only re-render when their props or state actually change.

**💻 Example**
```jsx
class MyComponent extends React.PureComponent {
  render() {
    return <h1>{this.props.value}</h1>;
  }
}
```

**💬 Explanation + Insight**

- Like a smart component that doesn't waste time re-rendering
- Only updates when props or state actually change
- Functional equivalent: `React.memo(MyComponent)`
- Be careful with objects - shallow comparison might miss deep changes
- Makes your app faster by avoiding unnecessary updates

---

### 25. 🧠 What is the role of ReactDOM in React apps?

**🧠 Concept**

`ReactDOM` is the bridge between React components and the actual webpage. It puts your React components into the real DOM.

**💻 Example**
```jsx
import ReactDOM from "react-dom/client";
import App from "./App";

const root = ReactDOM.createRoot(document.getElementById("root"));
root.render(<App />);
```

**💬 Explanation + Insight**

- React creates the components, ReactDOM puts them on the webpage
- Like a translator between React and the browser
- `createRoot` is the new way (React 18+)
- Enables better performance with concurrent rendering
- Handles mounting, updating, and unmounting components

