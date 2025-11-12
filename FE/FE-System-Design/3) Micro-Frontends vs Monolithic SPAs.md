# 🧩 3. Micro-Frontends vs Monolithic SPAs (Q24–33)

---

## 🧩 Q24. What is a micro-frontend and what problems does it solve?

### 🧠 Concept

Micro-frontends are an architectural approach where frontend applications are composed of independent, loosely coupled modules that can be developed, deployed, and scaled independently. Enables gradual migration from monolithic applications.

---

### 💡 Example

```javascript
const MicroFrontend = ({ name, host, history }) => {
  useEffect(() => {
    const scriptId = `micro-frontend-script-${name}`;
    if (document.getElementById(scriptId)) {
      renderMicroFrontend(name, history);
      return;
    }
    fetch(`${host}/asset-manifest.json`)
      .then(res => res.json())
      .then(manifest => {
        const script = document.createElement('script');
        script.src = `${host}${manifest.files['main.js']}`;
        script.onload = () => renderMicroFrontend(name, history);
        document.head.appendChild(script);
      });
  }, [name, host, history]);
  return <div id={`${name}-container`} />;
};
```

---

### 🔍 Deep Insights

* **Rule:** Enables independent team development and deployment.
* **Use Case:** Reduces coordination overhead between teams.
* **Common Mistake:** Allows technology diversity across frontend modules.
* **Pro Tip:** Improves scalability and maintainability.

---

### ⭐ Senior Takeaway

Enables gradual migration from monolithic applications.

---

## 🧩 Q25. What are the trade-offs between monolithic SPAs and micro-frontends?

### 🧠 Concept

Monolithic SPAs offer simplicity and consistency but can become unwieldy, while micro-frontends provide flexibility and independence at the cost of complexity and potential inconsistency. Choose based on organizational needs.

---

### 💡 Example

```javascript
// Monolithic SPA - simple but can become large
const MonolithicApp = () => (
  <div className="app">
    <Header />
    <main>
      <Dashboard />
      <Profile />
      <Settings />
    </main>
  </div>
);

// Micro-frontend - more complex but modular
const MicroFrontendApp = () => (
  <div className="app">
    <Header />
    <main>
      <MicroFrontend name="Dashboard" host="http://localhost:3001" />
      <MicroFrontend name="Profile" host="http://localhost:3002" />
    </main>
  </div>
);
```

---

### 🔍 Deep Insights

* **Rule:** Monolithic (simpler deployment, consistent UX, shared dependencies), Micro-frontends (independent deployment, technology diversity, team autonomy).
* **Use Case:** Consider team size, application complexity, and organizational structure.
* **Common Mistake:** Balance between simplicity and flexibility.
* **Pro Tip:** Evaluate long-term maintenance and scaling requirements.

---

### ⭐ Senior Takeaway

Choose based on organizational needs.

---

## 🧩 Q26. How do you manage shared dependencies across multiple front-end apps?

### 🧠 Concept

Shared dependency management in micro-frontends requires careful coordination to avoid version conflicts while maintaining consistency and reducing bundle size. Monitor bundle size and dependency conflicts.

---

### 💡 Example

```javascript
const sharedDependencies = {
  react: { singleton: true, requiredVersion: '^18.0.0' },
  'react-dom': { singleton: true, requiredVersion: '^18.0.0' },
  'react-router-dom': { singleton: true, requiredVersion: '^6.0.0' }
};

module.exports = {
  plugins: [
    new ModuleFederationPlugin({
      name: 'shell',
      remotes: {
        dashboard: 'dashboard@http://localhost:3001/remoteEntry.js'
      },
      shared: sharedDependencies
    })
  ]
};
```

---

### 🔍 Deep Insights

* **Rule:** Use Module Federation for shared dependency management.
* **Use Case:** Define clear version constraints and compatibility rules.
* **Common Mistake:** Implement shared component libraries for consistency.
* **Pro Tip:** Consider CDN delivery for common dependencies.

---

### ⭐ Senior Takeaway

Monitor bundle size and dependency conflicts.

---

## 🧩 Q27. How do you ensure seamless navigation across micro-frontends?

### 🧠 Concept

Seamless navigation requires shared routing state, consistent navigation patterns, and proper handling of deep linking and browser history across micro-frontend boundaries. Ensure proper state management across boundaries.

---

### 💡 Example

```javascript
export const RoutingProvider = ({ children }) => {
  const [currentRoute, setCurrentRoute] = useState('/');
  
  const navigate = useCallback((path) => {
    setCurrentRoute(path);
    window.history.pushState({}, '', path);
    window.dispatchEvent(new PopStateEvent('popstate'));
  }, []);
  
  return (
    <RoutingContext.Provider value={{ currentRoute, navigate }}>
      {children}
    </RoutingContext.Provider>
  );
};
```

---

### 🔍 Deep Insights

* **Rule:** Implement shared routing state and navigation context.
* **Use Case:** Use consistent URL patterns and deep linking.
* **Common Mistake:** Handle browser back/forward navigation properly.
* **Pro Tip:** Consider single-page application routing patterns.

---

### ⭐ Senior Takeaway

Ensure proper state management across boundaries.

---

## 🧩 Q28. How do you deploy and version micro-frontends independently?

### 🧠 Concept

Independent deployment requires proper versioning strategies, backward compatibility, and coordination mechanisms to ensure smooth updates without breaking the overall application. Consider blue-green deployment strategies.

---

### 💡 Example

```javascript
const microFrontendConfig = {
  dashboard: {
    current: '1.2.0',
    fallback: '1.1.0',
    host: 'https://cdn.example.com/dashboard'
  }
};

const loadMicroFrontend = async (name, version) => {
  try {
    const config = microFrontendConfig[name];
    return await loadScript(`${config.host}/${version}/remoteEntry.js`);
  } catch (error) {
    console.warn(`Failed to load ${name} v${version}, falling back`);
    return loadScript(`${config.host}/${config.fallback}/remoteEntry.js`);
  }
};
```

---

### 🔍 Deep Insights

* **Rule:** Implement semantic versioning for micro-frontends.
* **Use Case:** Use feature flags for gradual rollouts.
* **Common Mistake:** Maintain backward compatibility during transitions.
* **Pro Tip:** Implement proper error handling and fallbacks.

---

### ⭐ Senior Takeaway

Consider blue-green deployment strategies.

---

## 🧩 Q29. What are tools and strategies for building micro-frontends?

### 🧠 Concept

Different tools provide various approaches to micro-frontend architecture, each with specific strengths for different use cases and organizational needs. Each tool has different strengths.

---

### 💡 Example

```javascript
// Webpack Module Federation
module.exports = {
  plugins: [
    new ModuleFederationPlugin({
      name: 'shell',
      remotes: {
        dashboard: 'dashboard@http://localhost:3001/remoteEntry.js'
      },
      shared: ['react', 'react-dom']
    })
  ]
};

// Single-SPA configuration
registerApplication({
  name: 'dashboard',
  app: () => System.import('dashboard'),
  activeWhen: '/dashboard'
});
```

---

### 🔍 Deep Insights

* **Rule:** Module Federation (best for webpack-based applications), Single-SPA (framework-agnostic, good for mixed technology stacks), NX (excellent for monorepo management and code sharing).
* **Use Case:** Choose based on existing technology stack and team preferences.
* **Common Mistake:** Consider long-term maintenance and team expertise.
* **Pro Tip:** Evaluate tools based on specific requirements.

---

### ⭐ Senior Takeaway

Each tool has different strengths.

---

## 🧩 Q30. How do you handle authentication and routing in a micro-frontend setup?

### 🧠 Concept

Authentication and routing in micro-frontends require shared state management, consistent security policies, and proper token handling across different modules. Consider single sign-on (SSO) integration.

---

### 💡 Example

```javascript
export const AuthProvider = ({ children }) => {
  const [user, setUser] = useState(null);
  const [token, setToken] = useState(localStorage.getItem('token'));
  
  const login = async (credentials) => {
    const response = await fetch('/api/auth/login', {
      method: 'POST',
      body: JSON.stringify(credentials)
    });
    const { user, token } = await response.json();
    setUser(user);
    setToken(token);
    localStorage.setItem('token', token);
  };
  
  return (
    <AuthContext.Provider value={{ user, token, login, logout }}>
      {children}
    </AuthContext.Provider>
  );
};
```

---

### 🔍 Deep Insights

* **Rule:** Implement shared authentication state and context.
* **Use Case:** Use consistent token management and refresh strategies.
* **Common Mistake:** Implement role-based access control across micro-frontends.
* **Pro Tip:** Handle authentication errors and token expiration.

---

### ⭐ Senior Takeaway

Consider single sign-on (SSO) integration.

---

## 🧩 Q31. How would you migrate a large monolithic React app to micro-frontends?

### 🧠 Concept

Migration to micro-frontends should be gradual, starting with identifying boundaries, extracting modules, and implementing shared infrastructure while maintaining system stability. Consider team structure and ownership, plan for rollback strategies.

---

### 💡 Example

```javascript
// Migration strategy: Strangler Fig pattern
const MonolithicApp = () => {
  const [migrationFlags, setMigrationFlags] = useState({
    dashboard: false,
    profile: false
  });
  
  return (
    <div className="app">
      {migrationFlags.dashboard ? (
        <MicroFrontend name="Dashboard" host="http://localhost:3001" />
      ) : (
        <LegacyDashboard />
      )}
    </div>
  );
};
```

---

### 🔍 Deep Insights

* **Rule:** Start with identifying clear module boundaries.
* **Use Case:** Use feature flags for gradual migration.
* **Common Mistake:** Extract shared dependencies and utilities first.
* **Pro Tip:** Implement proper testing and validation.

---

### ⭐ Senior Takeaway

Consider team structure and ownership, plan for rollback strategies.

---

## 🧩 Q32. How do you enforce consistent UI/UX across multiple micro-frontends?

### 🧠 Concept

Consistent UI/UX requires shared design systems, component libraries, and design tokens that can be consumed across different micro-frontends. Regular design reviews and audits.

---

### 💡 Example

```javascript
const DesignSystem = {
  colors: { primary: '#007bff', secondary: '#6c757d' },
  spacing: { xs: '4px', sm: '8px', md: '16px', lg: '24px' },
  typography: { fontFamily: 'Inter, sans-serif' }
};

const Button = ({ variant = 'primary', size = 'md', children }) => (
  <button
    className={`btn btn-${variant} btn-${size}`}
    style={{
      backgroundColor: DesignSystem.colors[variant],
      padding: DesignSystem.spacing[size]
    }}
  >
    {children}
  </button>
);
```

---

### 🔍 Deep Insights

* **Rule:** Create shared design system and component library.
* **Use Case:** Use design tokens for consistent styling.
* **Common Mistake:** Implement shared theme and branding.
* **Pro Tip:** Establish design guidelines and standards.

---

### ⭐ Senior Takeaway

Regular design reviews and audits.

---

## 🧩 Q33. How do you debug and monitor performance across micro-frontends?

### 🧠 Concept

Debugging and monitoring micro-frontends requires distributed tracing, centralized logging, and performance monitoring across the entire application ecosystem. Consider observability tools and dashboards.

---

### 💡 Example

```javascript
const Logger = {
  info: (message, context = {}) => {
    console.log(`[${new Date().toISOString()}] INFO: ${message}`, context);
    sendToLoggingService('info', message, context);
  },
  error: (message, error, context = {}) => {
    console.error(`[${new Date().toISOString()}] ERROR: ${message}`, error);
    sendToLoggingService('error', message, { ...context, error: error.stack });
  }
};

const PerformanceMonitor = {
  trackMicroFrontendLoad: (name, startTime, endTime) => {
    const loadTime = endTime - startTime;
    sendToPerformanceService({
      event: 'micro_frontend_load',
      name,
      loadTime,
      timestamp: Date.now()
    });
  }
};
```

---

### 🔍 Deep Insights

* **Rule:** Implement distributed tracing for request flow.
* **Use Case:** Use centralized logging and monitoring.
* **Common Mistake:** Track performance metrics across micro-frontends.
* **Pro Tip:** Implement error tracking and alerting.

---

### ⭐ Senior Takeaway

Consider observability tools and dashboards.

---
