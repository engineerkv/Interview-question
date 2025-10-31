# 1) UI/UX Architecture & State Management (Q1–10)

## 1) What are the main principles of scalable front-end architecture?

Concept: Scalable front-end architecture follows principles of modularity, separation of concerns, reusability, and maintainability to support growth and team collaboration.

Example:
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

Deep Insight:
- Modular design enables independent development and testing
- Clear separation of concerns improves maintainability
- Reusable components reduce code duplication
- Consistent patterns across the application
- Feature-based organization scales with team size

## 2) How do you design a large React/Vue/Angular app to remain modular over time?

Concept: Design large applications with clear boundaries, consistent patterns, and proper dependency management to maintain modularity as the codebase grows.

Example:
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

Deep Insight:
- Use barrel exports for clean import statements
- Implement dependency injection for services
- Define clear module boundaries and interfaces
- Avoid circular dependencies between modules
- Use consistent naming conventions and folder structure

## 3) What is atomic design, and how does it help build design systems?

Concept: Atomic design is a methodology that breaks UI components into atoms, molecules, organisms, templates, and pages, creating a systematic approach to building design systems.

Example:
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

Deep Insight:
- Creates consistent and reusable component hierarchy
- Enables systematic design system development
- Improves component reusability and maintainability
- Facilitates team collaboration and design consistency
- Scales from simple atoms to complex page layouts

## 4) What are container vs presentational components, and why separate them?

Concept: Container components handle data and logic, while presentational components focus on UI rendering, creating clear separation of concerns and improved testability.

Example:
```javascript
// Presentational component (pure UI)
const UserList = ({ users, onUserSelect, loading }) => (
  <div className="user-list">
    {loading ? (
      <Spinner />
    ) : (
      users.map(user => (
        <UserCard
          key={user.id}
          user={user}
          onClick={() => onUserSelect(user)}
        />
      ))
    )}
  </div>
);

// Container component (data and logic)
const UserListContainer = () => {
  const [users, setUsers] = useState([]);
  const [loading, setLoading] = useState(true);
  
  useEffect(() => {
    fetchUsers().then(setUsers).finally(() => setLoading(false));
  }, []);
  
  const handleUserSelect = (user) => {
    navigate(`/users/${user.id}`);
  };
  
  return (
    <UserList
      users={users}
      onUserSelect={handleUserSelect}
      loading={loading}
    />
  );
};
```

Deep Insight:
- Separates business logic from presentation logic
- Makes components more reusable and testable
- Enables easier refactoring and maintenance
- Improves code organization and readability
- Facilitates team collaboration between developers and designers

## 5) How do you design a reusable component library or design system?

Concept: Design systems provide consistent, reusable components with clear APIs, comprehensive documentation, and proper theming support for scalable front-end development.

Example:
```javascript
// Design system component with theming
const Button = forwardRef(({ 
  variant = 'primary', 
  size = 'medium', 
  children, 
  ...props 
}, ref) => {
  const theme = useTheme();
  const className = cn(
    'button',
    `button--${variant}`,
    `button--${size}`,
    props.className
  );
  
  return (
    <button
      ref={ref}
      className={className}
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

// Usage with TypeScript
interface ButtonProps {
  variant?: 'primary' | 'secondary' | 'danger';
  size?: 'small' | 'medium' | 'large';
  children: React.ReactNode;
}
```

Deep Insight:
- Provide clear, consistent APIs for all components
- Include comprehensive TypeScript definitions
- Support theming and customization
- Document usage examples and best practices
- Version components and maintain backward compatibility

## 6) How do you manage global state across micro-frontends or large SPAs?

Concept: Global state management in large applications requires centralized state, event-driven communication, and proper state synchronization across different parts of the application.

Example:
```javascript
// Global state with context and reducer
const AppStateContext = createContext();

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

// Custom hook for state access
export const useAppState = () => {
  const context = useContext(AppStateContext);
  if (!context) {
    throw new Error('useAppState must be used within AppStateProvider');
  }
  return context;
};
```

Deep Insight:
- Use context API for simple global state
- Implement Redux or Zustand for complex state management
- Consider state normalization for large datasets
- Implement proper state persistence and hydration
- Use event-driven communication for micro-frontends

## 7) How would you design an application supporting multi-theme and dark mode toggling?

Concept: Multi-theme support requires a centralized theme system with CSS custom properties, theme context, and persistent theme preferences.

Example:
```javascript
// Theme context and provider
const ThemeContext = createContext();

export const ThemeProvider = ({ children }) => {
  const [theme, setTheme] = useState(() => {
    const saved = localStorage.getItem('theme');
    return saved || 'light';
  });
  
  useEffect(() => {
    document.documentElement.setAttribute('data-theme', theme);
    localStorage.setItem('theme', theme);
  }, [theme]);
  
  const toggleTheme = () => {
    setTheme(prev => prev === 'light' ? 'dark' : 'light');
  };
  
  return (
    <ThemeContext.Provider value={{ theme, toggleTheme }}>
      {children}
    </ThemeContext.Provider>
  );
};

// CSS with custom properties
const themeStyles = `
  :root {
    --bg-primary: #ffffff;
    --text-primary: #000000;
  }
  
  [data-theme="dark"] {
    --bg-primary: #1a1a1a;
    --text-primary: #ffffff;
  }
`;
```

Deep Insight:
- Use CSS custom properties for theme values
- Implement theme persistence with localStorage
- Provide system theme detection
- Support theme transitions and animations
- Consider accessibility and color contrast requirements

## 8) What is the difference between CSR, SSR, SSG, and ISR (Next.js)?

Concept: These are different rendering strategies: CSR (Client-Side Rendering), SSR (Server-Side Rendering), SSG (Static Site Generation), and ISR (Incremental Static Regeneration) each with different performance and SEO characteristics.

Example:
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

// SSG - Static site generation
export async function getStaticProps() {
  const data = await fetch('https://api.example.com/data');
  return {
    props: { data: await data.json() },
    revalidate: 3600 // Revalidate every hour
  };
}
```

Deep Insight:
- CSR: Fast interactions, poor SEO, requires JavaScript
- SSR: Good SEO, slower initial load, server required
- SSG: Fastest loading, excellent SEO, build-time generation
- ISR: Combines SSG benefits with dynamic updates
- Choose based on content type and performance requirements

## 9) What architectural patterns scale best in React (Hooks, Context API, Redux, Zustand)?

Concept: Different state management patterns have different trade-offs for scalability, with hooks and context for simple cases, Redux for complex applications, and Zustand for modern React applications.

Example:
```javascript
// Hooks pattern for local state
const useCounter = (initialValue = 0) => {
  const [count, setCount] = useState(initialValue);
  const increment = useCallback(() => setCount(c => c + 1), []);
  const decrement = useCallback(() => setCount(c => c - 1), []);
  return { count, increment, decrement };
};

// Zustand for global state
const useStore = create((set) => ({
  count: 0,
  increment: () => set((state) => ({ count: state.count + 1 })),
  decrement: () => set((state) => ({ count: state.count - 1 })),
}));

// Redux for complex state
const counterSlice = createSlice({
  name: 'counter',
  initialState: { value: 0 },
  reducers: {
    increment: (state) => { state.value += 1; },
    decrement: (state) => { state.value -= 1; },
  },
});
```

Deep Insight:
- Hooks: Best for component-level state and simple logic
- Context API: Good for app-wide state with minimal complexity
- Redux: Excellent for complex state with time-travel debugging
- Zustand: Modern alternative with less boilerplate
- Choose based on complexity and team preferences

## 10) How do you organize code for feature-based modularity?

Concept: Feature-based modularity organizes code by business features rather than technical layers, improving maintainability and enabling independent development.

Example:
```javascript
// Feature-based folder structure
src/
  features/
    authentication/
      components/
        LoginForm.jsx
        SignupForm.jsx
      hooks/
        useAuth.js
        useLogin.js
      services/
        authService.js
      types/
        auth.types.js
      index.js
    dashboard/
      components/
        Dashboard.jsx
        StatsCard.jsx
      hooks/
        useDashboard.js
      services/
        dashboardService.js
      types/
        dashboard.types.js
      index.js
  shared/
    components/
    hooks/
    utils/
    types/
```

Deep Insight:
- Group related functionality together
- Use barrel exports for clean imports
- Keep features independent and loosely coupled
- Share common utilities through shared folder
- Enable parallel development by different team members
