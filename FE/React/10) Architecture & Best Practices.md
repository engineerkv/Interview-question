# 🧭 10. Architecture & Best Practices (Q91–100)

---

## 🧩 Q91. How do you structure a scalable React project?

### 🧠 Concept

Organize by features, separate concerns, use consistent naming, and manage dependencies properly. Feature-based organization scales better than type-based.

---

### 💡 Example

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

---

### 🔍 Deep Insights

* **Rule:** Organize by features rather than file types for better scalability.
* **Use Case:** Keep UI, logic, and data separate for maintainability.
* **Common Mistake:** Use consistent naming conventions across the project.
* **Pro Tip:** Manage dependencies properly to avoid conflicts.

---

### ⭐ Senior Takeaway

Feature-based organization scales better than type-based.

---

## 🧩 Q92. What are the best practices for component composition?

### 🧠 Concept

Component composition combines components to create complex UIs. It's more flexible than inheritance and aligns with React's component-based architecture.

---

### 💡 Example

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

### 🔍 Deep Insights

* **Rule:** Compose simple components into complex UIs, avoid inheritance.
* **Use Case:** More flexible and reusable than inheritance patterns.
* **Common Mistake:** Aligns with React's component-based architecture.
* **Pro Tip:** Easier to maintain and modify composed components.

---

### ⭐ Senior Takeaway

Composition is preferred over inheritance in React.

---

## 🧩 Q93. How do you implement global configuration in React?

### 🧠 Concept

Use environment variables, configuration files, and context providers for global configuration. Environment variables are build-time configuration.

---

### 💡 Example

```jsx
// .env
REACT_APP_API_URL=https://api.example.com
REACT_APP_APP_NAME=My App
REACT_APP_DEBUG=true

// usage
const api = fetch(`${process.env.REACT_APP_API_URL}/status`);
```

---

### 🔍 Deep Insights

* **Rule:** Use .env files for different environments (dev, staging, prod).
* **Use Case:** API URLs, feature flags, debug settings, or app configuration.
* **Common Mistake:** Use TypeScript for configuration types and validation.
* **Pro Tip:** Never commit secrets, use environment variables for sensitive data.

---

### ⭐ Senior Takeaway

Environment variables are build-time configuration.

---

## 🧩 Q94. What is the difference between container and presentational components?

### 🧠 Concept

Container components handle logic and state. Presentational components handle UI. Still relevant but patterns evolved with hooks—custom hooks can replace container components.

---

### 💡 Example

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

### 🔍 Deep Insights

* **Rule:** Container components handle logic, state, and side effects (data fetching).
* **Use Case:** Presentational components handle UI rendering and user interactions.
* **Common Mistake:** Custom hooks can replace container components.
* **Pro Tip:** Still useful for complex components that mix logic and UI.

---

### ⭐ Senior Takeaway

Custom hooks modernize the container/presentational pattern.

---

## 🧩 Q95. How do you handle errors in React applications?

### 🧠 Concept

Use Error Boundaries, proper error states, logging, user-friendly messages, and graceful degradation. Error Boundaries are React's try-catch for components.

---

### 💡 Example

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

### 🔍 Deep Insights

* **Rule:** Error Boundaries catch JavaScript errors in component tree, prevent app crashes.
* **Use Case:** Wrap app sections to gracefully handle errors and show fallback UI.
* **Common Mistake:** Handle loading, error, and success states in components.
* **Pro Tip:** Log errors for debugging and monitoring (Sentry, logging services).

---

### ⭐ Senior Takeaway

Error Boundaries are React's try-catch for components.

---

## 🧩 Q96. How do you manage side effects in React?

### 🧠 Concept

Use custom hooks for reusable side effects, middleware for cross-cutting concerns, and proper separation. Custom hooks are the modern way to share side effect logic.

---

### 💡 Example

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

### 🔍 Deep Insights

* **Rule:** Extract and reuse side effect logic across components.
* **Use Case:** Data fetching, authentication, analytics, or any reusable side effects.
* **Common Mistake:** Handle cross-cutting concerns like logging, error handling.
* **Pro Tip:** Easier to test side effects in isolation with custom hooks.

---

### ⭐ Senior Takeaway

Custom hooks are the modern way to share side effect logic.

---

## 🧩 Q97. How do you implement authentication and authorization?

### 🧠 Concept

Use context providers, protected routes, token management, and proper state management for auth. Context API is good for auth, but consider Redux for complex auth flows.

---

### 💡 Example

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

### 🔍 Deep Insights

* **Rule:** Manage authentication state globally across the app.
* **Use Case:** Control access to specific routes based on authentication.
* **Common Mistake:** Handle JWT tokens securely (httpOnly cookies preferred over localStorage).
* **Pro Tip:** Implement role-based authorization for different user types.

---

### ⭐ Senior Takeaway

Context API is good for auth, but consider Redux for complex auth flows.

---

## 🧩 Q98. How do you handle environment variables in React?

### 🧠 Concept

Use .env files, build-time configuration, and proper secret management for different environments. Environment variables are embedded at build time in React.

---

### 💡 Example

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

### 🔍 Deep Insights

* **Rule:** Use .env files for different environments (dev, staging, prod).
* **Use Case:** Configuration is set at build time, not runtime.
* **Common Mistake:** Never commit secrets to version control, use CI/CD secrets.
* **Pro Tip:** Validate configuration values at startup to catch errors early.

---

### ⭐ Senior Takeaway

Environment variables are embedded at build time in React.

---

## 🧩 Q99. What are common React anti-patterns to avoid?

### 🧠 Concept

Common anti-patterns include prop drilling, mutating state, unnecessary re-renders, and poor component design. Anti-patterns usually indicate missing state management or poor architecture.

---

### 💡 Example

```jsx
// ❌ Anti-pattern: Prop drilling
function App() {
  const [user, setUser] = useState(null);
  return (
    <div>
      <Toolbar user={user} onLogout={() => setUser(null)} />
    </div>
  );
}

// ✅ Use Context instead
const UserContext = createContext();
function Toolbar() {
  const { user } = useContext(UserContext);
  return <div>{user?.name}</div>;
}
```

---

### 🔍 Deep Insights

* **Rule:** Avoid passing props through multiple levels—use Context or state management.
* **Use Case:** Never mutate state directly—always return new state objects.
* **Common Mistake:** Avoid creating objects/functions in render—use useMemo/useCallback.
* **Pro Tip:** Keep components focused and single-purpose.

---

### ⭐ Senior Takeaway

Anti-patterns usually indicate missing state management or poor architecture.

---

## 🧩 Q100. How do you profile and optimize React applications?

### 🧠 Concept

Use monitoring tools, performance budgets, regular profiling, and user feedback for continuous optimization. Continuous optimization requires monitoring and data-driven decisions.

---

### 💡 Example

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

### 🔍 Deep Insights

* **Rule:** Use tools like Lighthouse, Web Vitals, or RUM tools.
* **Use Case:** Set performance budgets and monitor them in CI/CD.
* **Common Mistake:** Profile performance regularly to catch regressions early.
* **Pro Tip:** Use user feedback and analytics to identify performance issues.

---

### ⭐ Senior Takeaway

Continuous optimization requires monitoring and data-driven decisions.

---
