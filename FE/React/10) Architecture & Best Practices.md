# 🧭 10. Architecture & Best Practices (Q91–100)

---

## 91) What are the key principles for structuring a scalable React project?

Organize by features, separate concerns, use consistent naming, and manage dependencies properly.

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

- **Feature-Based**: Organize by features rather than file types for better scalability
- **Separation of Concerns**: Keep UI, logic, and data separate for maintainability
- **Consistent Naming**: Use consistent naming conventions across the project
- **Dependency Management**: Manage dependencies properly to avoid conflicts
- **Interview Tip**: Explain that feature-based organization scales better than type-based

---

## 92) What is component composition and why is it preferred over inheritance?

Component composition combines components to create complex UIs. It's more flexible than inheritance.

```jsx
function Card({ children, variant = 'default' }) {
  return (
    <div className={`card card--${variant}`}>
      {children}
    </div>
  );
}

function App() {
  return <Card variant="primary"><button>Action</button></Card>;
}
```

- **Core Concept**: Compose simple components into complex UIs, avoid inheritance
- **Real-World Benefit**: More flexible and reusable than inheritance patterns
- **React Philosophy**: Aligns with React's component-based architecture
- **Maintainability**: Easier to maintain and modify composed components
- **Interview Tip**: Explain that composition is preferred over inheritance in React

---

## 93) How do you handle global configuration (environment variables, API URLs)?

Use environment variables, configuration files, and context providers for global configuration.

```jsx
// .env
REACT_APP_API_URL=https://api.example.com
REACT_APP_APP_NAME=My App
REACT_APP_DEBUG=true

// usage
const api = fetch(`${process.env.REACT_APP_API_URL}/status`);
```

- **Environment Variables**: Use .env files for different environments (dev, staging, prod)
- **Real-World Use**: API URLs, feature flags, debug settings, or app configuration
- **Type Safety**: Use TypeScript for configuration types and validation
- **Security**: Never commit secrets, use environment variables for sensitive data
- **Interview Tip**: Explain that environment variables are build-time configuration

---

## 94) What are "container" and "presentational" components and are they still relevant?

Container components handle logic and state. Presentational components handle UI. Still relevant but patterns evolved with hooks.

```jsx
// Container component (logic)
function UserListContainer() {
  const [users, setUsers] = useState([]);
  const [loading, setLoading] = useState(true);
  
  useEffect(() => {
    fetch('/api/users').then(r => r.json()).then(d => { setUsers(d); setLoading(false); });
  }, []);
  return <UserList users={users} loading={loading} />;
}

// Presentational component (UI)
function UserList({ users, loading }) {
  if (loading) return <div>Loading...</div>;
  return <ul>{users.map(u => <li key={u.id}>{u.name}</li>)}</ul>;
}
```

- **Container Components**: Handle logic, state, and side effects (data fetching)
- **Presentational Components**: Handle UI rendering and user interactions
- **Hooks Evolution**: Custom hooks can replace container components
- **Real-World Use**: Still useful for complex components that mix logic and UI
- **Interview Tip**: Explain that custom hooks modernize the container/presentational pattern

---

## 95) What are the best practices for error handling in React apps?

Use Error Boundaries, proper error states, logging, user-friendly messages, and graceful degradation.

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

- **Error Boundaries**: Catch JavaScript errors in component tree, prevent app crashes
- **Real-World Use**: Wrap app sections to gracefully handle errors and show fallback UI
- **Error States**: Handle loading, error, and success states in components
- **Logging**: Log errors for debugging and monitoring (Sentry, logging services)
- **Interview Tip**: Explain that Error Boundaries are React's try-catch for components

---

## 96) How do you handle side effects in large React apps (middleware, custom hooks)?

Use custom hooks for reusable side effects, middleware for cross-cutting concerns, and proper separation.

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

- **Custom Hooks**: Extract and reuse side effect logic across components
- **Real-World Use**: Data fetching, authentication, analytics, or any reusable side effects
- **Middleware Pattern**: Handle cross-cutting concerns like logging, error handling
- **Testing**: Easier to test side effects in isolation with custom hooks
- **Interview Tip**: Explain that custom hooks are the modern way to share side effect logic

---

## 97) How do you handle authentication and authorization in React?

Use context providers, protected routes, token management, and proper state management for auth.

```jsx
const AuthContext = createContext();

export function AuthProvider({ children }) {
  const [user, setUser] = useState(null);
  const [loading, setLoading] = useState(true);
  useEffect(() => { setLoading(false); }, []);
  const login = async (creds) => { /* auth */ setUser({ id: 1, name: 'User' }); };
  const logout = () => setUser(null);
  return <AuthContext.Provider value={{ user, login, logout, loading }}>{children}</AuthContext.Provider>;
}

function Protected({ children }) {
  const { user, loading } = useContext(AuthContext);
  if (loading) return <div>Loading...</div>;
  return user ? children : <div>Unauthorized</div>;
}
```

- **Context Providers**: Manage authentication state globally across the app
- **Protected Routes**: Control access to specific routes based on authentication
- **Token Management**: Handle JWT tokens securely (httpOnly cookies preferred over localStorage)
- **Role-Based Access**: Implement role-based authorization for different user types
- **Interview Tip**: Explain that Context API is good for auth, but consider Redux for complex auth flows

---

## 98) How do you manage environment variables and configuration for multiple environments?

Use .env files, build-time configuration, and proper secret management for different environments.

```jsx
// .env.development
REACT_APP_API_URL=http://localhost:3001
REACT_APP_DEBUG=true
REACT_APP_LOG_LEVEL=debug

// runtime usage
const base = process.env.REACT_APP_API_URL;
fetch(`${base}/health`);
```

- **Environment Files**: Use .env files for different environments (dev, staging, prod)
- **Build-Time Configuration**: Configuration is set at build time, not runtime
- **Secret Management**: Never commit secrets to version control, use CI/CD secrets
- **Validation**: Validate configuration values at startup to catch errors early
- **Interview Tip**: Explain that environment variables are embedded at build time in React

---

## 99) What are common React anti-patterns and how can they be avoided?

Common anti-patterns include prop drilling, mutating state, unnecessary re-renders, and poor component design.

```jsx
// ❌ Anti-pattern: Prop drilling
function App() {
  const [user, setUser] = useState(null);
  return <div><Toolbar user={user} onLogout={() => setUser(null)} /></div>;
}

// ✅ Use Context instead
const UserContext = createContext();
function Toolbar() {
  const { user } = useContext(UserContext);
  return <div>{user?.name}</div>;
}
```

- **Prop Drilling**: Avoid passing props through multiple levels - use Context or state management
- **State Mutation**: Never mutate state directly - always return new state objects
- **Unnecessary Re-renders**: Avoid creating objects/functions in render - use useMemo/useCallback
- **Poor Component Design**: Keep components focused and single-purpose
- **Interview Tip**: Explain that anti-patterns usually indicate missing state management or poor architecture

---

## 100) How do you approach performance profiling and continuous optimization in production?

Use monitoring tools, performance budgets, regular profiling, and user feedback for continuous optimization.

```jsx
function usePerformanceMonitor(componentName) {
  const renderCount = useRef(0);
  const startTime = useRef();
  
  useEffect(() => {
    renderCount.current += 1;
    startTime.current = performance.now();
    return () => {
      const duration = performance.now() - startTime.current;
      console.log(componentName, { renders: renderCount.current, duration });
    };
  });
  return renderCount.current;
}
```

- **Performance Monitoring**: Use tools like Lighthouse, Web Vitals, or RUM tools
- **Real-World Use**: Set performance budgets and monitor them in CI/CD
- **Regular Profiling**: Profile performance regularly to catch regressions early
- **User Feedback**: Use user feedback and analytics to identify performance issues
- **Interview Tip**: Explain that continuous optimization requires monitoring and data-driven decisions

---
