<div align="center">

**[← Previous: Testing & Debugging](7%29%20Testing%20%26%20Debugging.md)** | **[Next: Question List →](question.md)**

</div>

# 🏗️ 8. Architecture & Best Practices (Q87–96)

---

## Q87. 💡 Structuring a scalable React project

Organize by features, separate concerns, use consistent naming, and manage dependencies properly - feature-based organization scales better than type-based. Organize by features rather than file types for better scalability.

- **Trade-offs**: The catch is use consistent naming conventions across the project - manage dependencies properly to avoid conflicts. Feature-based organization scales better than type-based, but watch out - keep UI, logic, and data separate for maintainability.

Example:

```
src/
├── components/           # Reusable UI components
│   ├── Button/
│   │   ├── Button.jsx
│   │   ├── Button.test.jsx
│   │   └── index.js
├── features/            # Feature-based organization
│   ├── auth/
│   ├── dashboard/
└── hooks/               # Shared hooks

```

## Q88. 🧩 Best practices for component composition

Component composition combines components to create complex UIs - it's more flexible than inheritance and aligns with React's component-based architecture. Compose simple components into complex UIs, avoid inheritance.

- **Trade-offs**: The catch is aligns with React's component-based architecture - easier to maintain and modify composed components. Composition is preferred over inheritance in React, but watch out - more flexible and reusable than inheritance patterns.

Example:

```jsx
function Card({ children, variant = 'default' }) {
  return (
    <div className={`card card--${variant}`}>
      {children}
    </div>
  );
}

function App() {
  return (
    <Card variant="primary">
      <button>Action</button>
    </Card>
  );
}

```

---

## Q89. 🔧 Implementing global configuration in React

Use environment variables, configuration files, and context providers for global configuration - environment variables are build-time configuration. Use .env files for different environments (dev, staging, prod).

- **Trade-offs**: The catch is use TypeScript for configuration types and validation - never commit secrets, use environment variables for sensitive data. Environment variables are build-time configuration, but watch out - good for API URLs, feature flags, debug settings, or app configuration.

Example:

```jsx
// .env
REACT_APP_API_URL=https://api.example.com
REACT_APP_APP_NAME=My App
REACT_APP_DEBUG=true

// usage
const api = fetch(`${process.env.REACT_APP_API_URL}/status`);

```

---

## Q90. 🧩 Container vs presentational components

Container components handle logic and state, while presentational components handle UI - still relevant but patterns evolved with hooks, custom hooks can replace container components. Container components handle logic, state, and side effects (data fetching).

- **Trade-offs**: The catch is custom hooks can replace container components - still useful for complex components that mix logic and UI. Custom hooks modernize the container/presentational pattern, but watch out - presentational components handle UI rendering and user interactions.

Example:

```jsx
// Container component (logic)
function UserListContainer() {
  const [users, setUsers] = useState([]);
  const [loading, setLoading] = useState(true);
  
  useEffect(() => {
    fetch('/api/users')
      .then(r => r.json())
      .then(d => { setUsers(d); setLoading(false); });
  }, []);
  return <UserList users={users} loading={loading} />;
}

// Presentational component (UI)
function UserList({ users, loading }) {
  if (loading) return <div>Loading...</div>;
  return (
    <ul>
      {users.map(u => <li key={u.id}>{u.name}</li>)}
    </ul>
  );
}

```

---

## Q91. ⚠️ Handling errors in React applications

Use Error Boundaries, proper error states, logging, user-friendly messages, and graceful degradation - Error Boundaries are React's try-catch for components. Error Boundaries catch JavaScript errors in component tree, prevent app crashes.

- **Trade-offs**: The catch is handle loading, error, and success states in components - log errors for debugging and monitoring (Sentry, logging services). Error Boundaries are React's try-catch for components, but watch out - wrap app sections to gracefully handle errors and show fallback UI.

Example:

```jsx
class ErrorBoundary extends React.Component {
  constructor(props) {
    super(props);
    this.state = { hasError: false, error: null };
  }
  static getDerivedStateFromError(error) {
    return { hasError: true, error };
  }
  componentDidCatch(error, info) {
    console.error(error, info);
  }
  render() {
    if (this.state.hasError) return <div>Something went wrong.</div>;
    return this.props.children;
  }
}

```

---

## Q92. 💡 Managing side effects in React

Use custom hooks for reusable side effects, middleware for cross-cutting concerns, and proper separation - custom hooks are the modern way to share side effect logic. Extract and reuse side effect logic across components.

- **Trade-offs**: The catch is handle cross-cutting concerns like logging, error handling - easier to test side effects in isolation with custom hooks. Custom hooks are the modern way to share side effect logic, but watch out - good for data fetching, authentication, analytics, or any reusable side effects.

Example:

```jsx
function useApi(url) {
  const [data, setData] = useState(null);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState(null);
  
  useEffect(() => {
    let active = true;
    (async () => {
      try {
        const res = await fetch(url);
        const json = await res.json();
        if (active) setData(json);
      } catch (e) {
        if (active) setError(e);
      } finally {
        if (active) setLoading(false);
      }
    })();
    return () => { active = false; };
  }, [url]);
  return { data, loading, error };
}

```

---

## Q93. 🔐 Implementing authentication and authorization

Use context providers, protected routes, token management, and proper state management for auth - Context API is good for auth, but consider Redux for complex auth flows. Manage authentication state globally across the app.

- **Trade-offs**: The catch is handle JWT tokens securely (httpOnly cookies preferred over localStorage) - implement role-based authorization for different user types. Context API is good for auth, but consider Redux for complex auth flows, but watch out - control access to specific routes based on authentication.

Example:

```jsx
const AuthContext = createContext();

export function AuthProvider({ children }) {
  const [user, setUser] = useState(null);
  const [loading, setLoading] = useState(true);
  useEffect(() => { setLoading(false); }, []);
  const login = async (creds) => { 
    /* auth */ 
    setUser({ id: 1, name: 'User' }); 
  };
  const logout = () => setUser(null);
  return (
    <AuthContext.Provider value={{ user, login, logout, loading }}>
      {children}
    </AuthContext.Provider>
  );
}

function Protected({ children }) {
  const { user, loading } = useContext(AuthContext);
  if (loading) return <div>Loading...</div>;
  return user ? children : <div>Unauthorized</div>;
}

```

---

## Q94. 💡 Handling environment variables in React

Use .env files, build-time configuration, and proper secret management for different environments - environment variables are embedded at build time in React. Use .env files for different environments (dev, staging, prod).

- **Trade-offs**: The catch is never commit secrets to version control, use CI/CD secrets - validate configuration values at startup to catch errors early. Environment variables are embedded at build time in React, but watch out - configuration is set at build time, not runtime.

Example:

```jsx
// .env.development
REACT_APP_API_URL=http://localhost:3001
REACT_APP_DEBUG=true
REACT_APP_LOG_LEVEL=debug

// runtime usage
const base = process.env.REACT_APP_API_URL;
fetch(`${base}/health`);

```

---

## Q95. 🎯 Common React anti-patterns to avoid

Common anti-patterns include prop drilling, mutating state directly, creating objects/functions in render, missing keys in lists, conditional hooks, and unnecessary re-renders - these usually indicate missing state management or poor architecture. Avoid passing props through multiple levels, use Context or state management instead.

- **Trade-offs**: The catch is avoid creating objects/functions in render - they cause child re-renders even with React.memo. Never mutate state directly - always return new objects/arrays. Anti-patterns usually indicate missing state management or poor architecture, but watch out - conditional hooks break React's rules, missing keys cause reconciliation issues, and prop drilling makes components tightly coupled.

Example:

```jsx
// ❌ Anti-pattern: Prop drilling
function App() {
  const [user, setUser] = useState(null);
  return <Toolbar user={user} onLogout={() => setUser(null)} />;
}

// ✅ Use Context instead
const UserContext = createContext();
function Toolbar() {
  const { user } = useContext(UserContext);
  return <div>{user?.name}</div>;
}

// ❌ Anti-pattern: Mutating state
const [items, setItems] = useState([1, 2, 3]);
items.push(4); // Wrong - mutates state
setItems(items);

// ✅ Create new array
setItems([...items, 4]);

// ❌ Anti-pattern: Creating objects in render
function Parent({ userId }) {
  return <Child user={{ id: userId }} />; // New object every render
}

// ✅ Use useMemo or move outside
const user = useMemo(() => ({ id: userId }), [userId]);

// ❌ Anti-pattern: Conditional hooks
if (condition) {
  const [state, setState] = useState(0); // Breaks React rules
}

// ✅ Always call hooks unconditionally
const [state, setState] = useState(0);
if (condition) {
  // Use state here
}

// ❌ Anti-pattern: Missing keys in lists
{items.map(item => <Item data={item} />)}

// ✅ Always provide stable keys
{items.map(item => <Item key={item.id} data={item} />)}

```

---

## Q96. 💡 Profiling and optimizing React applications

Use monitoring tools, performance budgets, regular profiling, and user feedback for continuous optimization - continuous optimization requires monitoring and data-driven decisions. Use tools like Lighthouse, Web Vitals, or RUM tools.

- **Trade-offs**: The catch is profile performance regularly to catch regressions early - use user feedback and analytics to identify performance issues. Continuous optimization requires monitoring and data-driven decisions, but watch out - set performance budgets and monitor them in CI/CD.

Example:

```jsx
function usePerformanceMonitor(componentName) {
  const renderCount = useRef(0);
  const startTime = useRef();
  
  useEffect(() => {
    renderCount.current += 1;
    startTime.current = performance.now();
    return () => {
      const duration = performance.now() - startTime.current;
      console.log(componentName, { 
        renders: renderCount.current, 
        duration 
      });
    };
  });
  return renderCount.current;
}

```

---

<div align="center">

**[← Previous: Testing & Debugging](7%29%20Testing%20%26%20Debugging.md)** | **[Next: Question List →](question.md)**

</div>

