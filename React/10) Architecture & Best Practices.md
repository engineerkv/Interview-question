# 🧭 10. Architecture & Best Practices (Q91–100)

---

## 91) What are the key principles for structuring a scalable React project?

Concept:
Key principles include feature-based organization, separation of concerns, consistent naming conventions, and proper dependency management.

Example:
```
src/
├── components/           # Reusable UI components
│   ├── Button/
│   │   ├── Button.jsx
│   │   ├── Button.test.jsx
│   │   └── index.js
```

Deep Insight:
- **Feature-based**: Organize by features rather than file types
- **Separation of Concerns**: Keep UI, logic, and data separate
- **Consistent Naming**: Use consistent naming conventions
- **Dependency Management**: Manage dependencies properly
- **Scalability**: Structure for growth and team collaboration

---

## 92) What is component composition and why is it preferred over inheritance?

Concept:
Component composition combines components to create complex UIs, providing better flexibility and reusability than inheritance.

Example:
```jsx
// Composition - preferred approach
function Card({ children, variant = 'default' }) {
  return (
    <div className={`card card--${variant}`}>
      {children}
    </div>
  );
}

function App(){
  return <Card variant="primary"><button>Action</button></Card>;
}
```

Deep Insight:
- **Flexibility**: Composition is more flexible than inheritance
- **Reusability**: Components can be reused in different combinations
- **Maintainability**: Easier to maintain and modify
- **React Philosophy**: Aligns with React's component-based architecture
- **Avoid Inheritance**: React doesn't recommend inheritance patterns

---

## 93) How do you handle global configuration (environment variables, API URLs)?

Concept:
Use environment variables, configuration files, and context providers to manage global configuration across the application.

Example:
```jsx
// Environment configuration
// .env
REACT_APP_API_URL=https://api.example.com
REACT_APP_APP_NAME=My App
REACT_APP_DEBUG=true

// usage
const api = fetch(`${process.env.REACT_APP_API_URL}/status`);
```

Deep Insight:
- **Environment Variables**: Use .env files for configuration
- **Configuration Files**: Centralize configuration in config files
- **Context Providers**: Use context for dynamic configuration
- **Type Safety**: Use TypeScript for configuration types
- **Validation**: Validate configuration values at startup

---

## 94) What are "container" and "presentational" components and are they still relevant?

Concept:
Container components handle logic and state, while presentational components handle UI, still relevant but patterns have evolved with hooks.

Example:
```jsx
// Container component (logic)
function UserListContainer() {
  const [users, setUsers] = useState([]);
  const [loading, setLoading] = useState(true);
  
  useEffect(() => {
    fetch('/api/users').then(r=>r.json()).then(d=>{setUsers(d); setLoading(false);});
  }, []);
  return <UserList users={users} loading={loading} />;
}

// Presentational component (UI)
function UserList({ users, loading }){
  if (loading) return <div>Loading...</div>;
  return <ul>{users.map(u=> <li key={u.id}>{u.name}</li>)}</ul>;
}
```

Deep Insight:
- **Container Components**: Handle logic, state, and side effects
- **Presentational Components**: Handle UI rendering and user interactions
- **Separation of Concerns**: Keep logic and UI separate
- **Hooks Evolution**: Custom hooks can replace container components
- **Still Relevant**: Pattern is still useful for complex components

---

## 95) What are the best practices for error handling in React apps?

Concept:
Use Error Boundaries, proper error states, logging, user-friendly error messages, and graceful degradation for better error handling.

Example:
```jsx
// Error Boundary
class ErrorBoundary extends React.Component {
  constructor(props) {
    super(props);
    this.state = { hasError: false, error: null };
  }
  static getDerivedStateFromError(error){ return { hasError: true, error }; }
  componentDidCatch(error, info){ console.error(error, info); }
  render(){
    if (this.state.hasError) return <div>Something went wrong.</div>;
    return this.props.children;
  }
}

// usage
// <ErrorBoundary><MyWidget /></ErrorBoundary>
```

Deep Insight:
- **Error Boundaries**: Catch JavaScript errors in component tree
- **Error States**: Handle loading, error, and success states
- **User-friendly Messages**: Show helpful error messages to users
- **Logging**: Log errors for debugging and monitoring
- **Graceful Degradation**: Provide fallback UI when errors occur

---

## 96) How do you handle side effects in large React apps (middleware, custom hooks)?

Concept:
Use custom hooks for reusable side effects, middleware for cross-cutting concerns, and proper separation of concerns.

Example:
```jsx
// Custom hook for side effects
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
      } catch (e) { if (active) setError(e); }
      finally { if (active) setLoading(false); }
    })();
    return () => { active = false; };
  }, [url]);
  return { data, loading, error };
}
```

Deep Insight:
- **Custom Hooks**: Extract and reuse side effect logic
- **Middleware**: Handle cross-cutting concerns like logging, error handling
- **Separation of Concerns**: Keep side effects separate from UI logic
- **Reusability**: Make side effects reusable across components
- **Testing**: Easier to test side effects in isolation

---

## 97) How do you handle authentication and authorization in React?

Concept:
Use context providers, protected routes, token management, and proper state management for authentication and authorization.

Example:
```jsx
// Authentication context
const AuthContext = createContext();

export function AuthProvider({ children }) {
  const [user, setUser] = useState(null);
  const [loading, setLoading] = useState(true);
  useEffect(()=>{ setLoading(false); },[]);
  const login = async (creds) => { /* auth */ setUser({ id: 1, name: 'User' }); };
  const logout = () => setUser(null);
  return <AuthContext.Provider value={{ user, login, logout, loading }}>{children}</AuthContext.Provider>;
}

// Protected route (example)
function Protected({ children }){
  const { user, loading } = useContext(AuthContext);
  if (loading) return <div>Loading...</div>;
  return user ? children : <div>Unauthorized</div>;
}
```

Deep Insight:
- **Context Providers**: Manage authentication state globally
- **Protected Routes**: Control access to specific routes
- **Token Management**: Handle JWT tokens securely
- **Role-based Access**: Implement role-based authorization
- **Security**: Never store sensitive data in localStorage

---

## 98) How do you manage environment variables and configuration for multiple environments?

Concept:
Use .env files, build-time configuration, and proper secret management for different environments.

Example:
```jsx
// Environment-specific configuration
// .env.development
REACT_APP_API_URL=http://localhost:3001
REACT_APP_DEBUG=true
REACT_APP_LOG_LEVEL=debug

// runtime usage
const base = process.env.REACT_APP_API_URL;
fetch(`${base}/health`);
```

Deep Insight:
- **Environment Files**: Use .env files for different environments
- **Build-time Configuration**: Set configuration at build time
- **Secret Management**: Never commit secrets to version control
- **Validation**: Validate configuration values at startup
- **Fallbacks**: Provide fallback values for missing configuration

---

## 99) What are common React anti-patterns and how can they be avoided?

Concept:
Common anti-patterns include prop drilling, mutating state, unnecessary re-renders, and poor component design, avoided through proper patterns and practices.

Example:
```jsx
// ❌ Anti-pattern: Prop drilling
function App() {
  const [user, setUser] = useState(null);
  
  return (
    <div>
      <Toolbar user={user} onLogout={()=>setUser(null)} />
    </div>
  );
}

// ✅ Use Context instead
const UserContext = createContext();
function Toolbar(){ const { user } = useContext(UserContext); return <div>{user?.name}</div>; }
```

Deep Insight:
- **Prop Drilling**: Avoid passing props through multiple levels
- **State Mutation**: Never mutate state directly
- **Unnecessary Re-renders**: Avoid creating objects/functions in render
- **Poor Component Design**: Keep components focused and single-purpose
- **Best Practices**: Follow React best practices and patterns

---

## 100) How do you approach performance profiling and continuous optimization in production?

Concept:
Use monitoring tools, performance budgets, regular profiling, and user feedback to continuously optimize React applications.

Example:
```jsx
// Performance monitoring
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

Deep Insight:
- **Performance Monitoring**: Use tools like Lighthouse, Web Vitals
- **Performance Budgets**: Set and enforce performance budgets
- **Regular Profiling**: Profile performance regularly
- **User Feedback**: Use user feedback to identify issues
- **Continuous Improvement**: Continuously optimize based on data

---
