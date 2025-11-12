# 🎨 1. UI/UX Architecture & State Management (Q1–10)

---

## 🧩 Q1. What are the main principles of scalable front-end architecture?

### 🧠 Concept

Scalable front-end architecture follows principles of modularity, separation of concerns, reusability, and maintainability to support growth and team collaboration. Feature-based organization scales with team size.

---

### 💡 Example

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

### 🔍 Deep Insights

* **Rule:** Modular design enables independent development and testing.
* **Use Case:** Clear separation of concerns improves maintainability.
* **Common Mistake:** Reusable components reduce code duplication.
* **Pro Tip:** Consistent patterns across the application.

---

### ⭐ Senior Takeaway

Feature-based organization scales with team size.

---

## 🧩 Q2. How do you design a large React/Vue/Angular app to remain modular over time?

### 🧠 Concept

Design large applications with clear boundaries, consistent patterns, and proper dependency management to maintain modularity as the codebase grows. Use consistent naming conventions and folder structure.

---

### 💡 Example

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

### 🔍 Deep Insights

* **Rule:** Use barrel exports for clean import statements.
* **Use Case:** Implement dependency injection for services.
* **Common Mistake:** Define clear module boundaries and interfaces.
* **Pro Tip:** Avoid circular dependencies between modules.

---

### ⭐ Senior Takeaway

Use consistent naming conventions and folder structure.

---

## 🧩 Q3. What is atomic design and how does it help build design systems?

### 🧠 Concept

Atomic design is a methodology that breaks UI components into atoms, molecules, organisms, templates, and pages, creating a systematic approach to building design systems. Scales from simple atoms to complex page layouts.

---

### 💡 Example

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

### 🔍 Deep Insights

* **Rule:** Creates consistent and reusable component hierarchy.
* **Use Case:** Enables systematic design system development.
* **Common Mistake:** Improves component reusability and maintainability.
* **Pro Tip:** Facilitates team collaboration and design consistency.

---

### ⭐ Senior Takeaway

Scales from simple atoms to complex page layouts.

---

## 🧩 Q4. What are container vs presentational components?

### 🧠 Concept

Container components handle data and logic, while presentational components focus on UI rendering, creating clear separation of concerns and improved testability. Facilitates team collaboration between developers and designers.

---

### 💡 Example

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

### 🔍 Deep Insights

* **Rule:** Separates business logic from presentation logic.
* **Use Case:** Makes components more reusable and testable.
* **Common Mistake:** Enables easier refactoring and maintenance.
* **Pro Tip:** Improves code organization and readability.

---

### ⭐ Senior Takeaway

Facilitates team collaboration between developers and designers.

---

## 🧩 Q5. How do you design a reusable component library or design system?

### 🧠 Concept

Design systems provide consistent, reusable components with clear APIs, comprehensive documentation, and proper theming support for scalable front-end development. Version components and maintain backward compatibility.

---

### 💡 Example

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

### 🔍 Deep Insights

* **Rule:** Provide clear, consistent APIs for all components.
* **Use Case:** Include comprehensive TypeScript definitions.
* **Common Mistake:** Support theming and customization.
* **Pro Tip:** Document usage examples and best practices.

---

### ⭐ Senior Takeaway

Version components and maintain backward compatibility.

---

## 🧩 Q6. How do you manage global state across micro-frontends or large SPAs?

### 🧠 Concept

Global state management in large applications requires centralized state, event-driven communication, and proper state synchronization across different parts of the application. Use event-driven communication for micro-frontends.

---

### 💡 Example

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

### 🔍 Deep Insights

* **Rule:** Use context API for simple global state.
* **Use Case:** Implement Redux or Zustand for complex state management.
* **Common Mistake:** Consider state normalization for large datasets.
* **Pro Tip:** Implement proper state persistence and hydration.

---

### ⭐ Senior Takeaway

Use event-driven communication for micro-frontends.

---

## 🧩 Q7. What is the difference between CSR, SSR, SSG, and ISR?

### 🧠 Concept

These are different rendering strategies: CSR (Client-Side Rendering), SSR (Server-Side Rendering), SSG (Static Site Generation), and ISR (Incremental Static Regeneration) each with different performance and SEO characteristics. Each strategy has trade-offs between build time, runtime, server load, and SEO.

---

### 💡 Example

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

### 🔍 Deep Insights

* **Rule:** CSR (fast interactions, poor SEO, requires JavaScript), SSR (good SEO, slower initial load, requires server).
* **Use Case:** SSG (fastest loading, excellent SEO, build-time generation), ISR (combines SSG benefits with dynamic updates).
* **Common Mistake:** Choose based on content type and performance requirements.
* **Pro Tip:** Mix strategies for different parts of the app. See Q64 for advanced patterns (Streaming SSR, Partial Hydration, Islands Architecture).

---

### ⭐ Senior Takeaway

Each strategy has trade-offs. Choose based on content type, SEO needs, and performance requirements.

---

## 🧩 Q8. How do you implement feature-based modularity in frontend apps?

### 🧠 Concept

Feature-based modularity organizes code by business features rather than technical layers, improving maintainability and enabling independent development. Group related functionality together, keep features independent and loosely coupled.

---

### 💡 Example

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

### 🔍 Deep Insights

* **Rule:** Group related functionality together, use barrel exports for clean imports.
* **Use Case:** Keep features independent and loosely coupled, share common utilities through shared folder.
* **Common Mistake:** Mixing feature code with shared code causes tight coupling.
* **Pro Tip:** Enable parallel development by different team members.

---

### ⭐ Senior Takeaway

Feature-based organization scales with team size and improves code discoverability.

---

## 🧩 Q9. What are the best practices for component composition?

### 🧠 Concept

Component composition builds complex UIs from smaller, reusable components using patterns like children props, render props, and compound components. Prefer composition over inheritance for flexible and maintainable code.

---

### 💡 Example

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

### 🔍 Deep Insights

* **Rule:** Use children props for flexible content injection, render props for data sharing.
* **Use Case:** Compound components provide related functionality through composition.
* **Common Mistake:** Over-nesting components reduces readability.
* **Pro Tip:** Prefer composition over inheritance for flexible and maintainable code.

---

### ⭐ Senior Takeaway

Composition enables reusable, flexible components that adapt to different use cases.

---

## 🧩 Q10. How do you handle internationalization (i18n) in large applications?

### 🧠 Concept

Internationalization (i18n) enables applications to support multiple languages and locales through translation management, locale detection, and formatting utilities. Use libraries like react-i18next or react-intl for comprehensive i18n support.

---

### 💡 Example

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

### 🔍 Deep Insights

* **Rule:** Store translations in JSON files, detect user locale from browser or preferences.
* **Use Case:** Format dates, numbers, and currencies based on locale.
* **Common Mistake:** Hardcoding text strings prevents localization.
* **Pro Tip:** Use translation keys with namespaces for organization.

---

### ⭐ Senior Takeaway

Internationalization enables global reach by supporting multiple languages and cultural formats.

---
