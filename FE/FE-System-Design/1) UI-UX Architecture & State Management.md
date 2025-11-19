# 1. UI/UX Architecture & State Management (Q1–10)

---

## Q1. What are the main principles of scalable front-end architecture?

Scalable front-end architecture follows principles of modularity, separation of concerns, reusability, and maintainability to support growth and team collaboration - feature-based organization scales with team size. Modular design enables independent development and testing.

- **Trade-offs**: The catch is clear separation of concerns improves maintainability - reusable components reduce code duplication. Feature-based organization scales with team size, but watch out - consistent patterns across the application.

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

---

## Q2. How do you design a large React/Vue/Angular app to remain modular over time?

Design large applications with clear boundaries, consistent patterns, and proper dependency management to maintain modularity as the codebase grows - use consistent naming conventions and folder structure. Use barrel exports for clean import statements.

- **Trade-offs**: The catch is implement dependency injection for services - define clear module boundaries and interfaces. Use consistent naming conventions and folder structure, but watch out - avoid circular dependencies between modules.

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

---

## Q3. What is atomic design and how does it help build design systems?

Atomic design is a methodology that breaks UI components into atoms, molecules, organisms, templates, and pages, creating a systematic approach to building design systems - scales from simple atoms to complex page layouts. Creates consistent and reusable component hierarchy.

- **Trade-offs**: The catch is enables systematic design system development - improves component reusability and maintainability. Scales from simple atoms to complex page layouts, but watch out - facilitates team collaboration and design consistency.

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

---

## Q4. What are container vs presentational components?

Container components handle data and logic, while presentational components focus on UI rendering, creating clear separation of concerns and improved testability - facilitates team collaboration between developers and designers. Separates business logic from presentation logic.

- **Trade-offs**: The catch is makes components more reusable and testable - enables easier refactoring and maintenance. Facilitates team collaboration between developers and designers, but watch out - improves code organization and readability.

Example:

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

---

## Q5. How do you design a reusable component library or design system?

Design systems provide consistent, reusable components with clear APIs, comprehensive documentation, and proper theming support for scalable front-end development - version components and maintain backward compatibility. Provide clear, consistent APIs for all components.

- **Trade-offs**: The catch is include comprehensive TypeScript definitions - support theming and customization. Version components and maintain backward compatibility, but watch out - document usage examples and best practices.

Example:

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

---

## Q6. How do you manage global state across micro-frontends or large SPAs?

Global state management in large applications requires centralized state, event-driven communication, and proper state synchronization across different parts of the application - use event-driven communication for micro-frontends. Use context API for simple global state.

- **Trade-offs**: The catch is implement Redux or Zustand for complex state management - consider state normalization for large datasets. Use event-driven communication for micro-frontends, but watch out - implement proper state persistence and hydration.

Example:

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

---

## Q7. What is the difference between CSR, SSR, SSG, and ISR?

These are different rendering strategies: CSR (Client-Side Rendering), SSR (Server-Side Rendering), SSG (Static Site Generation), and ISR (Incremental Static Regeneration) each with different performance and SEO characteristics - each strategy has trade-offs between build time, runtime, server load, and SEO. CSR (fast interactions, poor SEO, requires JavaScript), SSR (good SEO, slower initial load, requires server).

- **Trade-offs**: The catch is SSG (fastest loading, excellent SEO, build-time generation), ISR (combines SSG benefits with dynamic updates) - choose based on content type and performance requirements. Each strategy has trade-offs, but watch out - mix strategies for different parts of the app.

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

// SSG - Static Site Generation
export async function getStaticProps() {
  const posts = await fetch('https://api.example.com/posts');
  return { props: { posts: await posts.json() } };
}

// ISR - Incremental Static Regeneration
export async function getStaticProps() {
  return {
    props: { data },
    revalidate: 3600 // Revalidate every hour
  };
}
```

---

## Q8. How do you implement feature-based modularity in frontend apps?

Feature-based modularity organizes code by business features rather than technical layers, improving maintainability and enabling independent development - group related functionality together, keep features independent and loosely coupled. Group related functionality together, use barrel exports for clean imports.

- **Trade-offs**: The catch is keep features independent and loosely coupled, share common utilities through shared folder - mixing feature code with shared code causes tight coupling. Feature-based organization scales with team size and improves code discoverability, but watch out - enable parallel development by different team members.

Example:

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

---

## Q9. What are the best practices for component composition?

Component composition builds complex UIs from smaller, reusable components using patterns like children props, render props, and compound components - prefer composition over inheritance for flexible and maintainable code. Use children props for flexible content injection, render props for data sharing.

- **Trade-offs**: The catch is compound components provide related functionality through composition - over-nesting components reduces readability. Prefer composition over inheritance for flexible and maintainable code, but watch out - composition enables reusable, flexible components that adapt to different use cases.

Example:

```javascript
// Children composition
const Card = ({ children, title }) => (
  <div className="card">
    {title && <h2>{title}</h2>}
    {children}
  </div>
);

// Render props pattern
const DataFetcher = ({ url, children }) => {
  const [data, setData] = useState(null);
  useEffect(() => {
    fetch(url).then(res => res.json()).then(setData);
  }, [url]);
  return children(data);
};

// Compound components
const Tabs = ({ children }) => {
  const [activeTab, setActiveTab] = useState(0);
  return <div>{children(activeTab, setActiveTab)}</div>;
};
```

---

## Q10. How do you handle internationalization (i18n) in large applications?

Internationalization (i18n) enables applications to support multiple languages and locales through translation management, locale detection, and formatting utilities - use libraries like react-i18next or react-intl for comprehensive i18n support. Store translations in JSON files, detect user locale from browser or preferences.

- **Trade-offs**: The catch is format dates, numbers, and currencies based on locale - hardcoding text strings prevents localization. Internationalization enables global reach by supporting multiple languages and cultural formats, but watch out - use translation keys with namespaces for organization.

Example:

```javascript
// i18n setup
import i18n from 'i18next';
import { initReactI18next } from 'react-i18next';

i18n.use(initReactI18next).init({
  resources: {
    en: { translation: { welcome: 'Welcome' } },
    es: { translation: { welcome: 'Bienvenido' } }
  },
  lng: 'en',
  fallbackLng: 'en'
});

// Component usage
const Welcome = () => {
  const { t } = useTranslation();
  return <h1>{t('welcome')}</h1>;
};
```

---
