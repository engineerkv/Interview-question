# 🎯 Patterns

---

## 📍 Navigation

<div align="center">

[← Previous: Offline Support](22%29%20Offline%20Support.md) • [Home: Questions Index](question.md) • [Next: Microfrontend →](24%29%20Microfrontend.md)

[📋 Cheatsheet](FE-System-Design%20Interview%20Cheatsheet.md)

</div>

---

---

## Q100. 🎨 Rendering Patterns

Rendering patterns determine when and where your application generates HTML and sends it to the browser. Different patterns offer different trade-offs between performance, SEO, user experience, and complexity. Understanding these patterns helps you choose the right approach for your application and optimize for your specific use case.

---

## 1. 🎨 Client-Side Rendering (CSR)

CSR renders content entirely in the browser using JavaScript after the initial HTML page loads.

### 🔹 How CSR Works

* **Initial Load**: Browser receives minimal HTML shell with JavaScript bundle

* **JavaScript Execution**: React/Vue/Angular runs in browser, fetches data via API

* **DOM Generation**: Framework generates DOM from JavaScript

* **Hydration**: Framework attaches event listeners and makes page interactive

### 🔹 Characteristics

* **Fast Navigation**: Subsequent page changes are instant (no full page reload)

* **Rich Interactivity**: Full SPA experience with smooth transitions

* **SEO Challenges**: Search engines may not execute JavaScript (though modern crawlers do)

* **Slow Initial Load**: User sees blank screen until JavaScript loads and executes

* **API Dependency**: Requires separate API endpoints

### 🔹 Use Cases

* **Dashboards**: Admin panels, analytics tools

* **Authenticated Apps**: Apps behind login (SEO not critical)

* **Highly Interactive Apps**: Real-time apps, games, complex UIs

* **Mobile Apps**: React Native, PWAs

### 🔹 Example

```javascript
// CSR - React app
function App() {
  const [data, setData] = useState(null);

  useEffect(() => {
    fetch('/api/data')
      .then(res => res.json())
      .then(setData);
  }, []);

  if (!data) return <div>Loading...</div>;
  return <div>{data.content}</div>;
}

```

📌 **In simple terms**: CSR is like ordering food at a restaurant - you get an empty table (HTML shell), then the waiter brings everything (JavaScript renders content). Fast for navigation, but slow initial experience.

---

## 2. 🎨 Server-Side Rendering (SSR)

SSR generates HTML on the server for each request and sends fully rendered HTML to the browser.

### 🔹 How SSR Works

* **Request**: User requests a page

* **Server Processing**: Server runs React/Vue code, fetches data, generates HTML

* **Response**: Browser receives complete HTML with content

* **Hydration**: JavaScript loads and "hydrates" the HTML (attaches event listeners)

### 🔹 Characteristics

* **Fast Initial Load**: User sees content immediately

* **SEO Friendly**: Search engines get fully rendered HTML

* **Server Load**: Each request requires server processing

* **Slower Navigation**: Full page reloads (unless using client-side routing)

* **TTFB Impact**: Time to First Byte depends on server processing time

### 🔹 Use Cases

* **Content Sites**: Blogs, news sites, marketing pages

* **E-commerce**: Product pages, category pages

* **Public-Facing Sites**: Sites where SEO is critical

* **Social Media**: Posts, profiles (need fast initial render)

### 🔹 Example

```javascript
// SSR - Next.js
export async function getServerSideProps(context) {
  const data = await fetch('https://api.example.com/data');
  return {
    props: { data: await data.json() }
  };
}

export default function Page({ data }) {
  return <div>{data.content}</div>;
}

```

📌 **In simple terms**: SSR is like a restaurant that brings your food ready to eat - you get everything immediately, but each new order takes time to prepare.

---

## 3. 📄 Static Site Generation (SSG)

SSG pre-renders pages at build time, generating static HTML files that are served directly.

### 🔹 How SSG Works

* **Build Time**: During build, framework generates HTML for all pages

* **Static Files**: HTML files are stored (can be on CDN)

* **Request**: Browser requests page, gets pre-generated HTML instantly

* **No Server Processing**: No server-side code execution per request

### 🔹 Characteristics

* **Fastest Performance**: Pre-generated HTML served from CDN

* **Excellent SEO**: Fully rendered HTML available immediately

* **Build Time Data**: Content must be known at build time

* **Rebuild Required**: Content changes require rebuilding

* **Scalability**: Can serve millions of requests (CDN handles it)

### 🔹 Use Cases

* **Documentation**: Technical docs, API docs

* **Blogs**: Personal blogs, company blogs

* **Marketing Sites**: Landing pages, product pages

* **Portfolios**: Personal portfolios, showcase sites

### 🔹 Example

```javascript
// SSG - Next.js
export async function getStaticProps() {
  const data = await fetch('https://api.example.com/posts');
  return {
    props: { posts: await data.json() },
    revalidate: 3600 // Revalidate every hour
  };
}

export default function Blog({ posts }) {
  return (
    <div>
      {posts.map(post => <article key={post.id}>{post.title}</article>)}
    </div>
  );
}

```

📌 **In simple terms**: SSG is like a vending machine - everything is prepared in advance, you get it instantly, but you can't customize it per customer.

---

## 4. 🔄 Incremental Static Regeneration (ISR)

ISR combines SSG with on-demand regeneration - pages are pre-rendered but can be regenerated in the background.

### 🔹 How ISR Works

* **Initial Build**: Pages pre-rendered at build time

* **Request**: User requests page, gets cached HTML

* **Background Regeneration**: If page is stale, serve cached version and regenerate in background

* **Next Request**: Updated page served to next user

### 🔹 Characteristics

* **Best of Both Worlds**: Fast like SSG, fresh like SSR

* **Stale-While-Revalidate**: Users get fast response, content updates in background

* **Build Time Flexibility**: Can have some pages pre-rendered, others on-demand

* **Complexity**: More complex than pure SSG or SSR

### 🔹 Use Cases

* **E-commerce**: Product pages (thousands of products, can't pre-render all)

* **Content Sites**: News sites, blogs with frequent updates

* **Hybrid Apps**: Mix of static and dynamic content

### 🔹 Example

```javascript
// ISR - Next.js
export async function getStaticProps({ params }) {
  const product = await fetchProduct(params.id);
  return {
    props: { product },
    revalidate: 60 // Regenerate every 60 seconds if requested
  };
}

export async function getStaticPaths() {
  return {
    paths: [], // Don't pre-render any paths
    fallback: 'blocking' // Generate on-demand
  };
}

```

📌 **In simple terms**: ISR is like a restaurant with pre-made meals that get refreshed - you get food fast, but it's always fresh because the kitchen makes new batches in the background.

---

## 5. 🌊 Streaming SSR

Streaming SSR sends HTML to the browser progressively as it's generated, rather than waiting for the entire page.

### 🔹 How Streaming SSR Works

* **Streaming Response**: Server starts sending HTML immediately

* **Progressive Rendering**: Browser renders HTML as it arrives

* **Suspense Boundaries**: React Suspense allows streaming parts of the page

* **Fast TTFB**: Time to First Byte is very fast

### 🔹 Characteristics

* **Fast Initial Paint**: User sees content start appearing quickly

* **Progressive Enhancement**: Page becomes interactive as parts load

* **Better Perceived Performance**: Feels faster even if total time is same

* **Complex Implementation**: Requires framework support (React 18+)

### 🔹 Use Cases

* **Large Pages**: Pages with lots of content

* **Slow Data Sources**: When some data loads slowly

* **Modern React Apps**: Apps using React 18+ Suspense

📌 **In simple terms**: Streaming SSR is like a buffet that starts serving as soon as some dishes are ready - you don't wait for everything, you start eating while more food arrives.

---

## 6. 💡 Partial Hydration

Partial Hydration only hydrates parts of the page that need interactivity, leaving static parts as plain HTML.

### 🔹 How Partial Hydration Works

* **Selective Hydration**: Only interactive components get JavaScript

* **Static HTML**: Non-interactive parts remain as static HTML

* **Smaller Bundle**: Less JavaScript to download and execute

* **Faster Interactivity**: Only necessary parts become interactive

### 🔹 Characteristics

* **Reduced JavaScript**: Smaller bundles, faster load times

* **Better Performance**: Less JavaScript to parse and execute

* **Selective Interactivity**: Only what needs to be interactive gets hydrated

* **Framework Support**: Requires framework features (React Islands, etc.)

📌 **In simple terms**: Partial hydration is like only adding batteries to toys that need them - most of the page is just static HTML, only interactive parts get JavaScript.

---

## ⭐ Summary — 10-second Interview Version

> "CSR renders in browser (fast nav, slow initial load). SSR renders on server (fast initial, SEO friendly). SSG pre-renders at build (fastest, best SEO). ISR combines SSG with background updates. Streaming SSR sends HTML progressively. Partial hydration only hydrates interactive parts. Choose based on SEO needs, update frequency, and performance requirements."

---

## ⭐ Extra Points (If Interviewer Asks More)

### When to use each pattern?

Use CSR for authenticated apps and dashboards. Use SSR for content sites needing SEO. Use SSG for static content like blogs. Use ISR for sites with many pages that update occasionally. Use streaming SSR for large pages with slow data.

### What is hydration?

Hydration is the process of attaching JavaScript event listeners and making server-rendered HTML interactive. The HTML is already there, JavaScript just "wakes it up."

---

## Q101. ⚛️ Anti-React Patterns

Anti-patterns in React are common mistakes that lead to poor performance, bugs, or hard-to-maintain code. Recognizing and avoiding these patterns is crucial for building quality React applications.

---

## 1. 💡 Direct DOM Manipulation

Manipulating the DOM directly bypasses React's virtual DOM and can cause inconsistencies.

### 🔹 The Problem

```javascript
// ❌ Anti-pattern: Direct DOM manipulation
function Component() {
  useEffect(() => {
    document.getElementById('myDiv').innerHTML = 'Updated';
  }, []);

  return <div id="myDiv">Original</div>;
}

```

**Issues:**

* React doesn't know about the change

* Next render will overwrite your changes

* Breaks React's reconciliation

* Can cause state inconsistencies

### 🔹 The Solution

```javascript
// ✅ Correct: Use React state
function Component() {
  const [content, setContent] = useState('Original');

  useEffect(() => {
    setContent('Updated');
  }, []);

  return <div>{content}</div>;
}

```

📌 **In simple terms**: Always allow React to manage the DOM. Direct manipulation breaks React's understanding of what the DOM should look like.

---

## 2. 📦 Mutating State Directly

Mutating state directly instead of creating new objects/arrays breaks React's change detection.

### 🔹 The Problem

```javascript
// ❌ Anti-pattern: Mutating state
function Component() {
  const [items, setItems] = useState([1, 2, 3]);

  const addItem = () => {
    items.push(4); // Mutating array directly
    setItems(items); // React won't detect change
  };

  return <button onClick={addItem}>Add</button>;
}

```

**Issues:**

* React uses reference equality to detect changes

* Mutating doesn't change the reference

* Component won't re-render

* Can cause stale UI

### 🔹 The Solution

```javascript
// ✅ Correct: Create new array
function Component() {
  const [items, setItems] = useState([1, 2, 3]);

  const addItem = () => {
    setItems([...items, 4]); // New array reference
  };

  return <button onClick={addItem}>Add</button>;
}

```

📌 **In simple terms**: Always create new objects/arrays when updating state. React needs to see a new reference to know something changed.

---

## 3. 📇 Using Index as Key

Using array index as key can cause bugs when list items are reordered, added, or removed.

### 🔹 The Problem

```javascript
// ❌ Anti-pattern: Index as key
function TodoList({ todos }) {
  return (
    <ul>
      {todos.map((todo, index) => (
        <TodoItem key={index} todo={todo} />
      ))}
    </ul>
  );
}

```

**Issues:**

* Keys should be stable and unique

* Index changes when items are reordered

* React may reuse wrong component instance

* Can cause state bugs and performance issues

### 🔹 The Solution

```javascript
// ✅ Correct: Use stable, unique ID
function TodoList({ todos }) {
  return (
    <ul>
      {todos.map(todo => (
        <TodoItem key={todo.id} todo={todo} />
      ))}
    </ul>
  );
}

```

📌 **In simple terms**: Keys help React identify which items changed. Using index breaks this when items move around. Always use stable, unique IDs.

---

## 4. ⚙️ Creating Functions/Objects in Render

Creating new functions or objects in render causes unnecessary re-renders of child components.

### 🔹 The Problem

```javascript
// ❌ Anti-pattern: New function/object in render
function Parent({ items }) {
  return (
    <div>
      {items.map(item => (
        <Child
          onClick={() => handleClick(item)} // New function every render
          style={{ color: 'red' }} // New object every render
        />
      ))}
    </div>
  );
}

```

**Issues:**

* New reference every render

* Child components think props changed

* Causes unnecessary re-renders

* Breaks memoization (React.memo, useMemo)

### 🔹 The Solution

```javascript
// ✅ Correct: Memoize callbacks and objects
function Parent({ items }) {
  const handleClick = useCallback((item) => {
    // Handle click
  }, []);

  const itemStyle = useMemo(() => ({ color: 'red' }), []);

  return (
    <div>
      {items.map(item => (
        <Child
          onClick={() => handleClick(item)}
          style={itemStyle}
        />
      ))}
    </div>
  );
}

```

📌 **In simple terms**: Creating new functions/objects in render breaks memoization. Use useCallback and useMemo to keep stable references.

---

## 5. 💡 Prop Drilling

Passing props through many component layers makes code hard to maintain.

### 🔹 The Problem

```javascript
// ❌ Anti-pattern: Prop drilling
function App() {
  const user = { name: 'John' };
  return <Page user={user} />;
}

function Page({ user }) {
  return <Header user={user} />;
}

function Header({ user }) {
  return <Profile user={user} />;
}

function Profile({ user }) {
  return <div>{user.name}</div>;
}

```

**Issues:**

* Components in middle don't need the prop

* Hard to refactor

* Makes components less reusable

* Clutters component signatures

### 🔹 The Solution

```javascript
// ✅ Correct: Use Context API
const UserContext = createContext();

function App() {
  const user = { name: 'John' };
  return (
    <UserContext.Provider value={user}>
      <Page />
    </UserContext.Provider>
  );
}

function Profile() {
  const user = useContext(UserContext);
  return <div>{user.name}</div>;
}

```

📌 **In simple terms**: When props need to go through many layers, use Context API instead of passing them through every component.

---

## 6. 💡 useEffect Without Dependencies

Missing or incorrect dependency arrays in useEffect can cause bugs or infinite loops.

### 🔹 The Problem

```javascript
// ❌ Anti-pattern: Missing dependencies
function Component({ userId }) {
  const [user, setUser] = useState(null);

  useEffect(() => {
    fetchUser(userId).then(setUser);
  }, []); // Missing userId dependency

  return <div>{user?.name}</div>;
}

```

**Issues:**

* Effect doesn't run when dependencies change

* Stale closures (uses old values)

* Can cause bugs and inconsistencies

### 🔹 The Solution

```javascript
// ✅ Correct: Include all dependencies
function Component({ userId }) {
  const [user, setUser] = useState(null);

  useEffect(() => {
    fetchUser(userId).then(setUser);
  }, [userId]); // Include userId

  return <div>{user?.name}</div>;
}

```

📌 **In simple terms**: Always include all values from component scope that the effect uses. ESLint's exhaustive-deps rule helps catch this.

---

## 7. 💡 Not Cleaning Up Effects

Not cleaning up effects (subscriptions, timers, event listeners) causes memory leaks.

### 🔹 The Problem

```javascript
// ❌ Anti-pattern: No cleanup
function Component() {
  useEffect(() => {
    const interval = setInterval(() => {
      console.log('Tick');
    }, 1000);
    // No cleanup - interval keeps running after unmount
  }, []);

  return <div>Component</div>;
}

```

**Issues:**

* Memory leaks

* Unnecessary work after component unmounts

* Can cause errors if trying to update unmounted component

### 🔹 The Solution

```javascript
// ✅ Correct: Cleanup in return function
function Component() {
  useEffect(() => {
    const interval = setInterval(() => {
      console.log('Tick');
    }, 1000);

    return () => clearInterval(interval); // Cleanup
  }, []);

  return <div>Component</div>;
}

```

📌 **In simple terms**: Always return a cleanup function from useEffect to cancel subscriptions, clear timers, and remove event listeners.

---

## ⭐ Summary — 10-second Interview Version

> "Common React anti-patterns: direct DOM manipulation (use state), mutating state (create new objects), index as key (use stable IDs), functions/objects in render (use useCallback/useMemo), prop drilling (use Context), missing useEffect dependencies (include all), not cleaning up effects (return cleanup function)."

---

## ⭐ Extra Points (If Interviewer Asks More)

### How to avoid these patterns?

Use ESLint with React hooks plugin, follow React best practices, use TypeScript for type safety, and review code regularly. Most modern React tooling will warn about these issues.

### What's the performance impact?

These patterns can cause unnecessary re-renders, memory leaks, and bugs. Following best practices helps you build better performance and maintainability.

---

## Q102. 💡 Anti-JavaScript Patterns

Anti-patterns in JavaScript are common mistakes that lead to bugs, poor performance, or hard-to-maintain code. Understanding these helps write better JavaScript.

---

## 1. 💡 Using var Instead of let/const

Using `var` has function scope and hoisting issues that can cause bugs.

### 🔹 The Problem

```javascript
// ❌ Anti-pattern: Using var
for (var i = 0; i < 3; i++) {
  setTimeout(() => {
    console.log(i); // Prints 3, 3, 3 (not 0, 1, 2)
  }, 100);
}

```

**Issues:**

* Function scope (not block scope)

* Hoisted to top of function

* Can be redeclared

* No temporal dead zone

### 🔹 The Solution

```javascript
// ✅ Correct: Use let or const
for (let i = 0; i < 3; i++) {
  setTimeout(() => {
    console.log(i); // Prints 0, 1, 2
  }, 100);
}

```

📌 **In simple terms**: Always use `let` or `const`. `var` has confusing scoping rules that cause bugs. Use `const` by default, `let` when you need to reassign.

---

## 2. ⏳ ⏳ Not Handling Async Errors

Not handling promise rejections or async errors can cause silent failures.

### 🔹 The Problem

```javascript
// ❌ Anti-pattern: Unhandled promise rejection
async function fetchData() {
  const data = await fetch('/api/data'); // No error handling
  return data.json();
}

fetchData(); // Unhandled rejection if fetch fails

```

**Issues:**

* Errors are swallowed

* Hard to debug

* Can crash Node.js applications

* Poor user experience

### 🔹 The Solution

```javascript
// ✅ Correct: Handle errors
async function fetchData() {
  try {
    const response = await fetch('/api/data');
    if (!response.ok) throw new Error('Failed to fetch');
    return await response.json();
  } catch (error) {
    console.error('Error:', error);
    throw error; // Re-throw or handle appropriately
  }
}

fetchData().catch(error => {
  // Handle error
});

```

📌 **In simple terms**: Always handle async errors with try/catch or .catch(). Unhandled promise rejections can cause issues.

---

## 3. 💡 Using == Instead of ===

Using loose equality (`==`) can cause unexpected type coercion bugs.

### 🔹 The Problem

```javascript
// ❌ Anti-pattern: Loose equality
if (0 == false) { // true (unexpected!)
  console.log('This runs');
}

if ('' == 0) { // true (unexpected!)
  console.log('This also runs');
}

if (null == undefined) { // true (unexpected!)
  console.log('This too');
}

```

**Issues:**

* Type coercion can cause unexpected results

* Hard to predict behavior

* Can hide bugs

### 🔹 The Solution

```javascript
// ✅ Correct: Strict equality
if (0 === false) { // false (expected)
  // Doesn't run
}

if ('' === 0) { // false (expected)
  // Doesn't run
}

if (null === undefined) { // false (expected)
  // Doesn't run
}

```

📌 **In simple terms**: Always use `===` (strict equality) instead of `==`. It's more predictable and prevents type coercion bugs.

---

## 4. 💡 Modifying Objects You Don't Own

Modifying built-in prototypes or objects you don't control can cause conflicts.

### 🔹 The Problem

```javascript
// ❌ Anti-pattern: Modifying prototypes
Array.prototype.last = function() {
  return this[this.length - 1];
};

// Can conflict with future JavaScript features
// Can break libraries that expect standard behavior

```

**Issues:**

* Can conflict with future language features

* Can break third-party libraries

* Makes code unpredictable

* Hard to debug

### 🔹 The Solution

```javascript
// ✅ Correct: Create utility functions
function last(array) {
  return array[array.length - 1];
}

// Or use a utility library like Lodash
import { last } from 'lodash';

```

📌 **In simple terms**: Don't modify built-in prototypes. Create utility functions or use libraries instead.

---

## 5. 💡 Not Using Optional Chaining

Not using optional chaining can cause verbose null/undefined checks.

### 🔹 The Problem

```javascript
// ❌ Anti-pattern: Verbose null checks
function getName(user) {
  if (user && user.profile && user.profile.name) {
    return user.profile.name;
  }
  return 'Unknown';
}

```

**Issues:**

* Verbose and repetitive

* Easy to miss a check

* Hard to read

### 🔹 The Solution

```javascript
// ✅ Correct: Optional chaining
function getName(user) {
  return user?.profile?.name ?? 'Unknown';
}

```

📌 **In simple terms**: Use optional chaining (`?.`) and nullish coalescing (`??`) to safely access nested properties and provide defaults.

---

## 6. ⚙️ Creating Functions in Loops

Creating functions in loops without proper closure handling causes bugs.

### 🔹 The Problem

```javascript
// ❌ Anti-pattern: Functions in loops
const buttons = document.querySelectorAll('button');
for (var i = 0; i < buttons.length; i++) {
  buttons[i].addEventListener('click', function() {
    console.log(i); // Always logs buttons.length (wrong!)
  });
}

```

**Issues:**

* All functions share the same variable

* Closure captures the final value

* Doesn't work as expected

### 🔹 The Solution

```javascript
// ✅ Correct: Use let or IIFE
// Option 1: Use let
for (let i = 0; i < buttons.length; i++) {
  buttons[i].addEventListener('click', function() {
    console.log(i); // Correct index
  });
}

// Option 2: Use forEach
buttons.forEach((button, i) => {
  button.addEventListener('click', function() {
    console.log(i); // Correct index
  });
});

```

📌 **In simple terms**: When creating functions in loops, use `let` (creates new binding each iteration) or use `forEach`/`map` which handle this correctly.

---

## 7. 💡 Not Using Destructuring

Not using destructuring makes code verbose and harder to read.

### 🔹 The Problem

```javascript
// ❌ Anti-pattern: Verbose property access
function processUser(user) {
  const name = user.name;
  const email = user.email;
  const age = user.age;
  // ... many lines
}

```

**Issues:**

* Verbose and repetitive

* Harder to see what properties are used

* More typing

### 🔹 The Solution

```javascript
// ✅ Correct: Use destructuring
function processUser(user) {
  const { name, email, age } = user;
  // ... cleaner code
}

// Or destructure in parameters
function processUser({ name, email, age }) {
  // ... even cleaner
}

```

📌 **In simple terms**: Use destructuring to extract properties from objects and arrays. It's cleaner and more readable.

---

## ⭐ Summary — 10-second Interview Version

> "Common JavaScript anti-patterns: using var (use let/const), not handling async errors (use try/catch), using == (use ===), modifying prototypes (create utilities), verbose null checks (use ?. and ??), functions in loops (use let or forEach), not using destructuring (extract properties cleanly)."

---

## ⭐ Extra Points (If Interviewer Asks More)

### How to avoid these patterns?

Use modern JavaScript features (ES6+), enable strict mode, use linters (ESLint), and follow best practices. Most of these are caught by modern tooling.

### What's the performance impact?

Some patterns (like modifying prototypes) can affect performance. Others mainly affect code quality and maintainability.

---

## Q103. 🟢 Anti-Node.js Patterns

Anti-patterns in Node.js are common mistakes that lead to poor performance, bugs, or security issues. Understanding these helps build better Node.js applications.

---

## 1. 🎯 Blocking the Event Loop

Running CPU-intensive or synchronous operations blocks the event loop.

### 🔹 The Problem

```javascript
// ❌ Anti-pattern: Blocking operations
app.get('/process', (req, res) => {
  // Synchronous file read blocks event loop
  const data = fs.readFileSync('large-file.txt', 'utf8');

  // CPU-intensive operation blocks event loop
  const result = heavyComputation(data);

  res.json(result);
});

```

**Issues:**

* Blocks entire event loop

* No other requests can be processed

* Poor performance and scalability

* Can cause timeouts

### 🔹 The Solution

```javascript
// ✅ Correct: Use async operations and worker threads
app.get('/process', async (req, res) => {
  // Async file read doesn't block
  const data = await fs.promises.readFile('large-file.txt', 'utf8');

  // CPU-intensive work in worker thread
  const result = await runInWorkerThread(heavyComputation, data);

  res.json(result);
});

```

📌 **In simple terms**: Never block the event loop with synchronous or CPU-intensive operations. Use async I/O and worker threads for heavy computation.

---

## 2. ⏳ ⏳ Not Handling Errors in Async Code

Not handling errors in async operations can crash your application.

### 🔹 The Problem

```javascript
// ❌ Anti-pattern: Unhandled promise rejection
app.get('/data', (req, res) => {
  fetchData() // No error handling
    .then(data => res.json(data));
  // If fetchData rejects, app crashes
});

```

**Issues:**

* Unhandled promise rejections can crash Node.js

* Poor error handling

* Hard to debug

* Bad user experience

### 🔹 The Solution

```javascript
// ✅ Correct: Always handle errors
app.get('/data', async (req, res) => {
  try {
    const data = await fetchData();
    res.json(data);
  } catch (error) {
    console.error('Error:', error);
    res.status(500).json({ error: 'Internal server error' });
  }
});

```

📌 **In simple terms**: Always handle errors in async code. Use try/catch with async/await or .catch() with promises.

---

## 3. 📞 Callback Hell

Nesting callbacks deeply makes code hard to read and maintain.

### 🔹 The Problem

```javascript
// ❌ Anti-pattern: Callback hell
fs.readFile('file1.txt', (err, data1) => {
  if (err) return console.error(err);
  fs.readFile('file2.txt', (err, data2) => {
    if (err) return console.error(err);
    fs.writeFile('output.txt', data1 + data2, (err) => {
      if (err) return console.error(err);
      console.log('Done');
    });
  });
});

```

**Issues:**

* Hard to read and maintain

* Error handling is repetitive

* Difficult to debug

* Hard to add more operations

### 🔹 The Solution

```javascript
// ✅ Correct: Use async/await
async function processFiles() {
  try {
    const data1 = await fs.promises.readFile('file1.txt');
    const data2 = await fs.promises.readFile('file2.txt');
    await fs.promises.writeFile('output.txt', data1 + data2);
    console.log('Done');
  } catch (error) {
    console.error('Error:', error);
  }
}

```

📌 **In simple terms**: Use async/await instead of nested callbacks. It's much cleaner and easier to read.

---

## 4. 🌊 Not Using Streams for Large Files

Loading entire files into memory can cause memory issues with large files.

### 🔹 The Problem

```javascript
// ❌ Anti-pattern: Loading entire file
app.get('/download', (req, res) => {
  fs.readFile('large-file.zip', (err, data) => {
    if (err) return res.status(500).send('Error');
    res.send(data); // Entire file in memory
  });
});

```

**Issues:**

* High memory usage

* Can cause out-of-memory errors

* Slow for large files

* Poor performance

### 🔹 The Solution

```javascript
// ✅ Correct: Use streams
app.get('/download', (req, res) => {
  const stream = fs.createReadStream('large-file.zip');
  stream.pipe(res); // Streams data, doesn't load all in memory
});

```

📌 **In simple terms**: Use streams for large files. Streams process data in chunks instead of loading everything into memory.

---

## 5. 💡 Not Using Environment Variables

Hardcoding configuration values makes code inflexible and insecure.

### 🔹 The Problem

```javascript
// ❌ Anti-pattern: Hardcoded values
const dbConfig = {
  host: 'localhost',
  port: 5432,
  password: 'secret123', // Security risk!
  database: 'myapp'
};

```

**Issues:**

* Can't change config per environment

* Security risk (secrets in code)

* Hard to manage different environments

* Committing secrets to version control

### 🔹 The Solution

```javascript
// ✅ Correct: Use environment variables
require('dotenv').config();

const dbConfig = {
  host: process.env.DB_HOST || 'localhost',
  port: parseInt(process.env.DB_PORT) || 5432,
  password: process.env.DB_PASSWORD, // From .env file
  database: process.env.DB_NAME
};

```

📌 **In simple terms**: Always use environment variables for configuration. Never hardcode secrets or environment-specific values.

---

## 6. 💡 Not Implementing Graceful Shutdown

Not handling shutdown signals can cause data loss or incomplete operations.

### 🔹 The Problem

```javascript
// ❌ Anti-pattern: No graceful shutdown
const server = app.listen(3000, () => {
  console.log('Server running');
});

// If process is killed, connections are closed abruptly
// Ongoing requests may be lost

```

**Issues:**

* Abrupt shutdown

* Ongoing requests may be lost

* Database connections not closed

* Can cause data corruption

### 🔹 The Solution

```javascript
// ✅ Correct: Graceful shutdown
const server = app.listen(3000, () => {
  console.log('Server running');
});

function gracefulShutdown(signal) {
  console.log(`Received ${signal}, shutting down gracefully`);

  server.close(() => {
    console.log('HTTP server closed');
    // Close database connections, cleanup, etc.
    process.exit(0);
  });

  // Force shutdown after timeout
  setTimeout(() => {
    console.error('Forced shutdown');
    process.exit(1);
  }, 10000);
}

process.on('SIGTERM', () => gracefulShutdown('SIGTERM'));
process.on('SIGINT', () => gracefulShutdown('SIGINT'));

```

📌 **In simple terms**: Always implement graceful shutdown. Close servers and connections properly when the process receives termination signals.

---

## 7. 💡 Not Using Connection Pooling

Creating new database connections for each request is inefficient.

### 🔹 The Problem

```javascript
// ❌ Anti-pattern: New connection per request
app.get('/users', async (req, res) => {
  const client = new Client(); // New connection
  await client.connect();
  const result = await client.query('SELECT * FROM users');
  await client.end(); // Close connection
  res.json(result.rows);
});

```

**Issues:**

* Inefficient (connection overhead)

* Can exhaust connection limits

* Slow performance

* Poor scalability

### 🔹 The Solution

```javascript
// ✅ Correct: Use connection pool
const pool = new Pool({
  host: process.env.DB_HOST,
  database: process.env.DB_NAME,
  max: 20, // Maximum connections
  idleTimeoutMillis: 30000
});

app.get('/users', async (req, res) => {
  const result = await pool.query('SELECT * FROM users');
  res.json(result.rows);
  // Connection automatically returned to pool
});

```

📌 **In simple terms**: Use connection pooling for databases. It reuses connections instead of creating new ones for each request.

---

## ⭐ Summary — 10-second Interview Version

> "Common Node.js anti-patterns: blocking event loop (use async/worker threads), not handling async errors (use try/catch), callback hell (use async/await), not using streams (use for large files), hardcoded config (use env vars), no graceful shutdown (handle signals), no connection pooling (reuse connections)."

---

## ⭐ Extra Points (If Interviewer Asks More)

### How to identify these patterns?

Use linters, code reviews, and monitoring. Tools like ESLint can catch many of these. Monitor event loop lag and memory usage.

### What's the performance impact?

These patterns can significantly impact performance, scalability, and reliability. Following best practices helps you build better applications.

---

---

## 📍 Navigation

<div align="center">

[← Previous: Offline Support](22%29%20Offline%20Support.md) • [Home: Questions Index](question.md) • [Next: Microfrontend →](24%29%20Microfrontend.md)

[📋 Cheatsheet](FE-System-Design%20Interview%20Cheatsheet.md)

</div>

---
