# 1) UI/UX Architecture & State Management (Q1–10)

---

## 1) What are the main principles of scalable front-end architecture?

Scalable front-end architecture follows principles of modularity, separation of concerns, reusability, and maintainability to support growth and team collaboration.

```javascript
// Feature-based architecture
src/
  features/
    auth/
      components/
      hooks/
      services/
      types/
    dashboard/
      components/
      hooks/
      services/
  shared/
    components/
    hooks/
    utils/
    types/
```

- **Core Principle**: Modular design enables independent development and testing
- **Real-World Benefit**: Clear separation of concerns improves maintainability
- **Common Advantage**: Reusable components reduce code duplication
- **Advanced Practice**: Consistent patterns across the application
- **Interview Tip**: Explain that feature-based organization scales with team size

---

## 2) How do you design a large React/Vue/Angular app to remain modular over time?

Design large applications with clear boundaries, consistent patterns, and proper dependency management to maintain modularity as the codebase grows.

```javascript
// Barrel exports for clean imports
// features/auth/index.js
export { LoginForm } from './components/LoginForm';
export { useAuth } from './hooks/useAuth';
export { authService } from './services/authService';

// Dependency injection for services
const AuthContext = createContext();
export const AuthProvider = ({ children }) => {
  const authService = useAuthService();
  return (
    <AuthContext.Provider value={authService}>
      {children}
    </AuthContext.Provider>
  );
};
```

- **Core Practice**: Use barrel exports for clean import statements
- **Real-World Use**: Implement dependency injection for services
- **Common Approach**: Define clear module boundaries and interfaces
- **Advanced Practice**: Avoid circular dependencies between modules
- **Interview Tip**: Explain that use consistent naming conventions and folder structure

---

## 3) What is atomic design, and how does it help build design systems?

Atomic design is a methodology that breaks UI components into atoms, molecules, organisms, templates, and pages, creating a systematic approach to building design systems.

```javascript
// Atoms (basic building blocks)
const Button = ({ variant, size, children }) => (
  <button className={`btn btn-${variant} btn-${size}`}>
    {children}
  </button>
);

// Molecules (simple combinations)
const SearchInput = () => (
  <div className="search-input">
    <Input placeholder="Search..." />
    <Button variant="primary">Search</Button>
  </div>
);

// Organisms (complex components)
const Header = () => (
  <header className="header">
    <Logo />
    <SearchInput />
    <UserMenu />
  </header>
);
```

- **Core Concept**: Creates consistent and reusable component hierarchy
- **Real-World Use**: Enables systematic design system development
- **Common Benefit**: Improves component reusability and maintainability
- **Advanced Feature**: Facilitates team collaboration and design consistency
- **Interview Tip**: Explain that scales from simple atoms to complex page layouts

---

## 4) What are container vs presentational components, and why separate them?

Container components handle data and logic, while presentational components focus on UI rendering, creating clear separation of concerns and improved testability.

```javascript
// Presentational component (pure UI)
const UserList = ({ users, onUserSelect, loading }) => (
  <div className="user-list">
    {loading ? <Spinner /> : users.map(user => (
      <UserCard key={user.id} user={user} onClick={() => onUserSelect(user)} />
    ))}
  </div>
);

// Container component (data and logic)
const UserListContainer = () => {
  const [users, setUsers] = useState([]);
  const [loading, setLoading] = useState(true);
  
  useEffect(() => {
    fetchUsers().then(setUsers).finally(() => setLoading(false));
  }, []);
  
  return <UserList users={users} onUserSelect={handleUserSelect} loading={loading} />;
};
```

- **Core Separation**: Separates business logic from presentation logic
- **Real-World Benefit**: Makes components more reusable and testable
- **Common Advantage**: Enables easier refactoring and maintenance
- **Advanced Feature**: Improves code organization and readability
- **Interview Tip**: Explain that facilitates team collaboration between developers and designers

---

## 5) How do you design a reusable component library or design system?

Design systems provide consistent, reusable components with clear APIs, comprehensive documentation, and proper theming support for scalable front-end development.

```javascript
const Button = forwardRef(({ 
  variant = 'primary', 
  size = 'medium', 
  children, 
  ...props 
}, ref) => {
  const theme = useTheme();
  return (
    <button
      ref={ref}
      className={`button button--${variant} button--${size}`}
      style={{
        '--button-bg': theme.colors[variant],
        '--button-padding': theme.spacing[size]
      }}
      {...props}
    >
      {children}
    </button>
  );
});
```

- **Core Requirement**: Provide clear, consistent APIs for all components
- **Real-World Use**: Include comprehensive TypeScript definitions
- **Common Feature**: Support theming and customization
- **Advanced Practice**: Document usage examples and best practices
- **Interview Tip**: Explain that version components and maintain backward compatibility

---

## 6) How do you manage global state across micro-frontends or large SPAs?

Global state management in large applications requires centralized state, event-driven communication, and proper state synchronization across different parts of the application.

```javascript
const appStateReducer = (state, action) => {
  switch (action.type) {
    case 'SET_USER':
      return { ...state, user: action.payload };
    case 'SET_THEME':
      return { ...state, theme: action.payload };
    default:
      return state;
  }
};

export const AppStateProvider = ({ children }) => {
  const [state, dispatch] = useReducer(appStateReducer, {
    user: null,
    theme: 'light',
    notifications: []
  });
  
  return (
    <AppStateContext.Provider value={{ state, dispatch }}>
      {children}
    </AppStateContext.Provider>
  );
};
```

- **Core Approach**: Use context API for simple global state
- **Real-World Use**: Implement Redux or Zustand for complex state management
- **Common Practice**: Consider state normalization for large datasets
- **Advanced Feature**: Implement proper state persistence and hydration
- **Interview Tip**: Explain that use event-driven communication for micro-frontends

---

## 7) How would you design an application supporting multi-theme and dark mode toggling?

Multi-theme support requires a centralized theme system with CSS custom properties, theme context, and persistent theme preferences.

```javascript
export const ThemeProvider = ({ children }) => {
  const [theme, setTheme] = useState(() => {
    const saved = localStorage.getItem('theme');
    return saved || 'light';
  });
  
  useEffect(() => {
    document.documentElement.setAttribute('data-theme', theme);
    localStorage.setItem('theme', theme);
  }, [theme]);
  
  return (
    <ThemeContext.Provider value={{ theme, toggleTheme }}>
      {children}
    </ThemeContext.Provider>
  );
};
```

- **Core Technique**: Use CSS custom properties for theme values
- **Real-World Use**: Implement theme persistence with localStorage
- **Common Feature**: Provide system theme detection
- **Advanced Feature**: Support theme transitions and animations
- **Interview Tip**: Explain that consider accessibility and color contrast requirements

---

## 8) What is the difference between CSR, SSR, SSG, and ISR (Next.js)?

These are different rendering strategies: CSR (Client-Side Rendering), SSR (Server-Side Rendering), SSG (Static Site Generation), and ISR (Incremental Static Regeneration) each with different performance and SEO characteristics.

```javascript
// CSR - Client-side rendering
const App = () => {
  const [data, setData] = useState(null);
  useEffect(() => {
    fetch('/api/data').then(res => res.json()).then(setData);
  }, []);
  return <div>{data ? data.title : 'Loading...'}</div>;
};

// SSR - Server-side rendering (Next.js)
export async function getServerSideProps() {
  const data = await fetch('https://api.example.com/data');
  return { props: { data: await data.json() } };
}
```

- **Core Differences**: CSR (fast interactions, poor SEO, requires JavaScript), SSR (good SEO, slower initial load, server required)
- **Real-World Use**: SSG (fastest loading, excellent SEO, build-time generation), ISR (combines SSG benefits with dynamic updates)
- **Common Choice**: Choose based on content type and performance requirements
- **Advanced Strategy**: Mix strategies for different parts of the app
- **Interview Tip**: Explain that each strategy has trade-offs

---

## 9) What architectural patterns scale best in React (Hooks, Context API, Redux, Zustand)?

Different state management patterns have different trade-offs for scalability, with hooks and context for simple cases, Redux for complex applications, and Zustand for modern React applications.

```javascript
// Hooks pattern for local state
const useCounter = (initialValue = 0) => {
  const [count, setCount] = useState(initialValue);
  const increment = useCallback(() => setCount(c => c + 1), []);
  return { count, increment };
};

// Zustand for global state
const useStore = create((set) => ({
  count: 0,
  increment: () => set((state) => ({ count: state.count + 1 }))
}));
```

- **Core Patterns**: Hooks (best for component-level state and simple logic), Context API (good for app-wide state with minimal complexity)
- **Real-World Use**: Redux (excellent for complex state with time-travel debugging), Zustand (modern alternative with less boilerplate)
- **Common Choice**: Choose based on complexity and team preferences
- **Advanced Pattern**: Combine patterns for different use cases
- **Interview Tip**: Explain that start simple, scale when needed

---

## 10) How do you organize code for feature-based modularity?

Feature-based modularity organizes code by business features rather than technical layers, improving maintainability and enabling independent development.

```javascript
// Feature-based folder structure
src/
  features/
    authentication/
      components/LoginForm.jsx
      hooks/useAuth.js
      services/authService.js
      types/auth.types.js
      index.js
    dashboard/
      components/Dashboard.jsx
      hooks/useDashboard.js
      services/dashboardService.js
      types/dashboard.types.js
      index.js
  shared/
    components/
    hooks/
    utils/
    types/
```

- **Core Organization**: Group related functionality together
- **Real-World Use**: Use barrel exports for clean imports
- **Common Practice**: Keep features independent and loosely coupled
- **Advanced Feature**: Share common utilities through shared folder
- **Interview Tip**: Explain that enable parallel development by different team members

---
