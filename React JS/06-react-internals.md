# ⚛️ React.js Interview Notes (2025 Edition)

## 🧩 Section 6 — React Internals (Fiber, Diffing, Rendering) — Q111-Q130

---

### 111. 🧩 What is React Fiber architecture?

**🧠 Concept**

React Fiber is the new engine that lets React work in small chunks, pause when needed, and prioritize important updates for better performance.

**💻 Example**
```jsx
// Fiber enables concurrent features
function App() {
  const [count, setCount] = useState(0);
  
  const handleClick = () => {
    // Fiber can interrupt this work if needed
    setCount(count + 1);
    setCount(count + 1);
    setCount(count + 1);
  };
  
  return <button onClick={handleClick}>{count}</button>;
}
```

📝 **Deeper Insight**

Fiber architecture benefits:
- **Concurrent rendering** (non-blocking updates)
- **Priority-based work** (urgent updates first)
- **Time slicing** (work divided into chunks)
- **Interruption and resumption** (responsive UI)

---

### 112. 🧩 What problem did Fiber solve over the old stack reconciler?

🧠 **Concept**

The old stack reconciler was **synchronous and blocking**, causing UI freezes during expensive operations. Fiber made it **asynchronous and interruptible**.

💻 **Example**

```jsx
// Old stack reconciler (blocking)
function OldReconciler() {
  // This would block the UI until complete
  const expensiveOperation = () => {
    for (let i = 0; i < 1000000; i++) {
      // Heavy computation
    }
  };
  
  return <div>{expensiveOperation()}</div>;
}

// Fiber reconciler (non-blocking)
function FiberReconciler() {
  const [data, setData] = useState(null);
  
  useEffect(() => {
    // This can be interrupted by user interactions
    const expensiveOperation = async () => {
      const result = await heavyComputation();
      setData(result);
    };
    
    expensiveOperation();
  }, []);
  
  return <div>{data}</div>;
}
```

📝 **Deeper Insight**

Fiber solved:
- **UI blocking** during expensive operations
- **Poor user experience** with unresponsive interfaces
- **Limited concurrency** in rendering
- **No priority-based updates**

---

### 113. 🧩 How does React's diffing algorithm work?

🧠 **Concept**

React's diffing algorithm **compares virtual DOM trees** to determine the minimal changes needed to update the real DOM.

💻 **Example**

```jsx
// Previous virtual DOM
const previousVDOM = {
  type: 'div',
  props: { className: 'container' },
  children: [
    { type: 'h1', props: {}, children: ['Hello'] },
    { type: 'p', props: {}, children: ['World'] }
  ]
};

// Current virtual DOM
const currentVDOM = {
  type: 'div',
  props: { className: 'container' },
  children: [
    { type: 'h1', props: {}, children: ['Hello'] },
    { type: 'p', props: {}, children: ['React'] } // Changed from 'World' to 'React'
  ]
};

// Diffing result: Only update the text content of the <p> element
```

📝 **Deeper Insight**

Diffing algorithm rules:
- **Same type**  update props and children
- **Different type**  replace entire subtree
- **Keys**  help identify which items changed
- **Shallow comparison**  for props and state

---

### 114. 🧩 What is the work-in-progress tree in React Fiber?

🧠 **Concept**

The work-in-progress tree is a **mutable copy** of the current tree that Fiber builds during the render phase, allowing for interruption and resumption.

💻 **Example**

```jsx
// Current tree (immutable)
const currentTree = {
  type: 'div',
  props: { className: 'container' },
  children: [
    { type: 'h1', props: {}, children: ['Hello'] }
  ]
};

// Work-in-progress tree (mutable)
const workInProgressTree = {
  type: 'div',
  props: { className: 'container' },
  children: [
    { type: 'h1', props: {}, children: ['Hello World'] } // Being updated
  ]
};

// Fiber can pause here and resume later
```

📝 **Deeper Insight**

Work-in-progress tree benefits:
- **Mutable during render** (can be modified)
- **Interruptible** (can pause and resume)
- **Incremental updates** (work in chunks)
- **Priority-based** (urgent work first)

---

### 115. 🧩 What is React's render phase and commit phase?

🧠 **Concept**

React rendering has two phases:
- **Render phase**  creating virtual DOM (can be interrupted)
- **Commit phase**  updating real DOM (synchronous)

💻 **Example**

```jsx
// Render phase (interruptible)
function Component() {
  const [count, setCount] = useState(0);
  
  // This phase can be interrupted
  return <div>{count}</div>;
}

// Commit phase (synchronous)
// React updates the actual DOM
// Calls lifecycle methods
// Runs effects
```

📝 **Deeper Insight**

Render vs Commit phases:
- **Render phase**  pure computation, can be interrupted
- **Commit phase**  side effects, synchronous
- **Concurrent features** work in render phase
- **Lifecycle methods** run in commit phase

---

### 116. 🧩 What are lanes and priorities in React Fiber?

🧠 **Concept**

Lanes are **priority levels** that help React Fiber determine which updates to process first, ensuring urgent updates get priority.

💻 **Example**

```jsx
// Lane priorities (conceptual)
const lanes = {
  SyncLane: 1,           // Synchronous updates
  InputContinuousLane: 4, // User input
  DefaultLane: 16,       // Default updates
  IdleLane: 32           // Low priority
};

// React uses lanes internally
function handleClick() {
  // High priority update
  setCount(count + 1);
}

function handleScroll() {
  // Low priority update
  setScrollPosition(scrollY);
}
```

📝 **Deeper Insight**

Lane system benefits:
- **Priority-based updates** (urgent first)
- **Concurrent rendering** (non-blocking)
- **Automatic batching** (similar priority updates)
- **Interruption handling** (higher priority interrupts lower)

---

### 117. 🧩 How does React handle interruptions during rendering?

🧠 **Concept**

React Fiber can **pause and resume work** by maintaining the work-in-progress tree and using the scheduler to prioritize updates.

💻 **Example**

```jsx
// React can interrupt this work
function ExpensiveComponent() {
  const [data, setData] = useState(null);
  
  useEffect(() => {
    // This can be interrupted by user interactions
    const processData = async () => {
      for (let i = 0; i < 1000000; i++) {
        // Heavy computation
        // React can pause here if user clicks a button
      }
      setData(processedData);
    };
    
    processData();
  }, []);
  
  return <div>{data}</div>;
}
```

📝 **Deeper Insight**

Interruption handling:
- **Work-in-progress tree** (preserves state)
- **Scheduler** (manages priorities)
- **Time slicing** (work in chunks)
- **Resumption** (continues where left off)

---

### 118. 🧩 What is time slicing?

🧠 **Concept**

Time slicing **divides work into small chunks** that can be processed within a single frame, keeping the UI responsive.

💻 **Example**

```jsx
// Time slicing in action
function processLargeDataset(data) {
  // Instead of processing all at once:
  // for (let i = 0; i < data.length; i++) {
  //   processItem(data[i]);
  // }
  
  // Process in chunks:
  const processChunk = (startIndex) => {
    const endIndex = Math.min(startIndex + 100, data.length);
    
    for (let i = startIndex; i < endIndex; i++) {
      processItem(data[i]);
    }
    
    if (endIndex < data.length) {
      // Schedule next chunk
      requestIdleCallback(() => processChunk(endIndex));
    }
  };
  
  processChunk(0);
}
```

📝 **Deeper Insight**

Time slicing benefits:
- **Responsive UI** (work divided into frames)
- **Non-blocking** (doesn't freeze interface)
- **Progressive rendering** (content appears gradually)
- **Better user experience** (smooth interactions)

---

### 119. 🧩 How does React batch updates across components?

🧠 **Concept**

React **automatically batches** multiple state updates into a single re-render, improving performance by reducing the number of DOM updates.

💻 **Example**

```jsx
function App() {
  const [count, setCount] = useState(0);
  const [name, setName] = useState('');
  
  const handleClick = () => {
    setCount(count + 1); // Batched
    setName('Updated');   // Batched
    setCount(count + 1); // Batched
    // Only one re-render happens
  };
  
  return (
    <div>
      <button onClick={handleClick}>Update</button>
      <div>Count: {count}, Name: {name}</div>
    </div>
  );
}
```

📝 **Deeper Insight**

Batching benefits:
- **Performance optimization** (fewer re-renders)
- **Consistent state** (updates processed together)
- **Automatic in React 18** (event handlers, async operations)
- **Manual control** with `flushSync()` if needed

---

### 120. 🧩 What happens internally when `setState()` is called?

🧠 **Concept**

When `setState()` is called, React **schedules an update**, compares the new state with the previous state, and triggers a re-render if needed.

💻 **Example**

```jsx
function Component() {
  const [count, setCount] = useState(0);
  
  const handleClick = () => {
    // 1. React schedules an update
    setCount(count + 1);
    
    // 2. React compares new state with previous
    // 3. If different, triggers re-render
    // 4. Creates new virtual DOM
    // 5. Diffs with previous virtual DOM
    // 6. Updates real DOM
  };
  
  return <button onClick={handleClick}>{count}</button>;
}
```

📝 **Deeper Insight**

`setState()` internal process:
1. **Schedule update** (add to update queue)
2. **State comparison** (shallow comparison)
3. **Re-render trigger** (if state changed)
4. **Virtual DOM creation** (render phase)
5. **Diffing algorithm** (compare trees)
6. **DOM updates** (commit phase)

---

### 121. 🧩 How does React schedule and prioritize rendering tasks?

🧠 **Concept**

React uses a **scheduler** to prioritize rendering tasks based on urgency, ensuring user interactions get priority over background updates.

💻 **Example**

```jsx
// React's internal scheduling (conceptual)
const scheduler = {
  // High priority (user interactions)
  scheduleUserInput: (task) => {
    // Process immediately
    task();
  },
  
  // Low priority (background updates)
  scheduleBackground: (task) => {
    // Process when idle
    requestIdleCallback(task);
  }
};

// Usage
function handleClick() {
  // High priority - processed immediately
  setCount(count + 1);
}

function handleScroll() {
  // Low priority - processed when idle
  setScrollPosition(scrollY);
}
```

📝 **Deeper Insight**

Scheduling priorities:
- **User interactions** (clicks, typing)  highest priority
- **Animation frames**  high priority
- **Data fetching**  medium priority
- **Background tasks**  low priority

---

### 122. 🧩 What is the difference between mounting, updating, and unmounting?

🧠 **Concept**

- **Mounting**  component is created and added to DOM
- **Updating**  component re-renders due to state/props changes
- **Unmounting**  component is removed from DOM

💻 **Example**

```jsx
function Component() {
  const [count, setCount] = useState(0);
  
  // Mounting phase
  useEffect(() => {
    console.log('Component mounted');
    return () => console.log('Component unmounted');
  }, []);
  
  // Updating phase
  useEffect(() => {
    console.log('Component updated');
  }, [count]);
  
  return <button onClick={() => setCount(count + 1)}>{count}</button>;
}
```

📝 **Deeper Insight**

Component lifecycle phases:
- **Mounting**  `constructor`, `componentDidMount`, `useEffect(() => {}, [])`
- **Updating**  `componentDidUpdate`, `useEffect(() => {}, [deps])`
- **Unmounting**  `componentWillUnmount`, cleanup in `useEffect`

---

### 123. 🧩 How does React handle concurrent rendering internally?

🧠 **Concept**

Concurrent rendering allows React to **interrupt and resume work** using the work-in-progress tree and scheduler to keep the UI responsive.

💻 **Example**

```jsx
// Concurrent rendering in action
function App() {
  const [count, setCount] = useState(0);
  const [isPending, startTransition] = useTransition();
  
  const handleClick = () => {
    // This can be interrupted by user interactions
    startTransition(() => {
      setCount(count + 1);
      // Heavy computation that can be paused
    });
  };
  
  return (
    <div>
      <button onClick={handleClick}>Count: {count}</button>
      {isPending && <div>Updating...</div>}
    </div>
  );
}
```

📝 **Deeper Insight**

Concurrent rendering features:
- **Interruptible work** (can pause and resume)
- **Priority-based updates** (urgent first)
- **Time slicing** (work in chunks)
- **Automatic batching** (multiple updates together)

---

### 124. 🧩 What are transitions and deferred updates?

🧠 **Concept**

Transitions mark updates as **non-urgent**, allowing React to defer them and keep the UI responsive during expensive operations.

💻 **Example**

```jsx
import { useTransition, startTransition } from 'react';

function App() {
  const [isPending, startTransition] = useTransition();
  const [query, setQuery] = useState('');
  const [results, setResults] = useState([]);
  
  const handleSearch = (newQuery) => {
    setQuery(newQuery);
    
    // Mark as non-urgent transition
    startTransition(() => {
      setResults(expensiveSearch(newQuery));
    });
  };
  
  return (
    <div>
      <input value={query} onChange={e => handleSearch(e.target.value)} />
      {isPending && <div>Searching...</div>}
      <ResultsList results={results} />
    </div>
  );
}
```

📝 **Deeper Insight**

Transitions benefits:
- **Non-blocking updates** (UI stays responsive)
- **Priority-based rendering** (urgent updates first)
- **Better user experience** (smooth interactions)
- **Automatic batching** (similar priority updates)

---

### 125. 🧩 How does React Fiber ensure UI responsiveness?

🧠 **Concept**

React Fiber ensures UI responsiveness through **concurrent rendering**, **priority-based updates**, and **time slicing** that keeps the interface smooth.

💻 **Example**

```jsx
// Fiber keeps UI responsive
function App() {
  const [count, setCount] = useState(0);
  const [isPending, startTransition] = useTransition();
  
  const handleClick = () => {
    // High priority - processed immediately
    setCount(count + 1);
  };
  
  const handleExpensiveUpdate = () => {
    // Low priority - can be interrupted
    startTransition(() => {
      // Heavy computation that won't block UI
      setResults(processLargeDataset());
    });
  };
  
  return (
    <div>
      <button onClick={handleClick}>Count: {count}</button>
      <button onClick={handleExpensiveUpdate}>Process Data</button>
      {isPending && <div>Processing...</div>}
    </div>
  );
}
```

📝 **Deeper Insight**

Fiber responsiveness features:
- **Concurrent rendering** (non-blocking updates)
- **Priority-based work** (urgent updates first)
- **Time slicing** (work divided into chunks)
- **Interruption handling** (pause and resume)

---

### 126. 🧩 How do keys help React's diffing algorithm?

🧠 **Concept**

Keys help React **identify which items have changed** in lists, enabling efficient updates instead of re-rendering entire lists.

💻 **Example**

```jsx
// ❌ Without keys - inefficient
{items.map(item => <li>{item.name}</li>)}

// ✅ With keys - efficient
{items.map(item => <li key={item.id}>{item.name}</li>)}

// React can now:
// - Identify which items changed
// - Reuse existing DOM nodes
// - Only update changed items
// - Maintain component state
```

📝 **Deeper Insight**

Keys optimization benefits:
- **Efficient updates** (only changed items re-render)
- **DOM node reuse** (preserves component state)
- **Performance improvement** (fewer DOM operations)
- **Stable identity** (consistent across renders)

---

### 127. 🧩 How does React manage effect cleanup and commits?

🧠 **Concept**

React manages effect cleanup by **calling cleanup functions** before re-running effects or unmounting components, ensuring proper resource management.

💻 **Example**

```jsx
function Component() {
  const [count, setCount] = useState(0);
  
  useEffect(() => {
    // Effect setup
    const timer = setInterval(() => {
      console.log('Timer tick');
    }, 1000);
    
    // Cleanup function
    return () => {
      clearInterval(timer);
      console.log('Timer cleaned up');
    };
  }, [count]);
  
  return <div>Count: {count}</div>;
}
```

📝 **Deeper Insight**

Effect cleanup process:
- **Before re-run**  cleanup previous effect
- **Before unmount**  cleanup all effects
- **Commit phase**  effects run after DOM updates
- **Cleanup order**  reverse of effect creation

---

### 128. 🧩 What is React's hydration process?

🧠 **Concept**

Hydration is the process where React **takes over server-rendered HTML** and makes it interactive by attaching event listeners and state.

💻 **Example**

```jsx
// Server-rendered HTML
<div id="root">
  <div>Hello World</div>
</div>

// Client-side hydration
import { createRoot } from 'react-dom/client';

function App() {
  return <div>Hello World</div>;
}

const root = createRoot(document.getElementById('root'));
root.hydrate(<App />); // Takes over existing HTML
```

📝 **Deeper Insight**

Hydration process:
- **HTML takeover** (React attaches to existing DOM)
- **Event listener attachment** (makes interactive)
- **State restoration** (re-establishes component state)
- **Mismatch handling** (server/client differences)

---

### 129. 🧩 How does React optimize async rendering?

🧠 **Concept**

React optimizes async rendering through **concurrent features**, **priority-based updates**, and **automatic batching** that improve performance and user experience.

💻 **Example**

```jsx
// Async rendering optimization
function App() {
  const [count, setCount] = useState(0);
  const [isPending, startTransition] = useTransition();
  
  const handleClick = () => {
    // High priority - processed immediately
    setCount(count + 1);
  };
  
  const handleAsyncUpdate = () => {
    // Low priority - optimized for async
    startTransition(() => {
      // This won't block the UI
      setResults(processAsyncData());
    });
  };
  
  return (
    <div>
      <button onClick={handleClick}>Count: {count}</button>
      <button onClick={handleAsyncUpdate}>Process Data</button>
      {isPending && <div>Processing...</div>}
    </div>
  );
}
```

📝 **Deeper Insight**

Async rendering optimizations:
- **Concurrent rendering** (non-blocking updates)
- **Priority-based work** (urgent updates first)
- **Automatic batching** (multiple updates together)
- **Time slicing** (work divided into chunks)

---

### 130. 🧩 How will the React Compiler change re-rendering behavior in React 19+?

🧠 **Concept**

The React Compiler will **automatically optimize** component re-renders by adding memoization and reducing unnecessary updates, improving performance without manual optimization.

💻 **Example**

```jsx
// Before React Compiler (manual optimization)
function ExpensiveComponent({ data }) {
  const expensiveValue = useMemo(() => {
    return data.reduce((sum, item) => sum + item.value, 0);
  }, [data]);
  
  const handleClick = useCallback(() => {
    // Expensive operation
  }, []);
  
  return <div onClick={handleClick}>{expensiveValue}</div>;
}

// After React Compiler (automatic optimization)
function ExpensiveComponent({ data }) {
  const expensiveValue = data.reduce((sum, item) => sum + item.value, 0);
  
  const handleClick = () => {
    // Expensive operation
  };
  
  return <div onClick={handleClick}>{expensiveValue}</div>;
  // Compiler automatically adds memoization
}
```

📝 **Deeper Insight**

React Compiler benefits:
- **Automatic memoization** (no manual `useMemo`, `useCallback`)
- **Performance optimization** (reduced re-renders)
- **Simplified code** (less optimization boilerplate)
- **Future-proof** (works with new React features)

---
