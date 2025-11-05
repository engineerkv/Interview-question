# 3) Micro-Frontends vs Monolithic SPAs (Q24–33)

---

## 24) What is a micro-frontend, and what problems does it solve?

Micro-frontends are an architectural approach where frontend applications are composed of independent, loosely coupled modules that can be developed, deployed, and scaled independently.

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

- **Core Benefit**: Enables independent team development and deployment
- **Real-World Advantage**: Reduces coordination overhead between teams
- **Common Use Case**: Allows technology diversity across frontend modules
- **Advanced Feature**: Improves scalability and maintainability
- **Interview Tip**: Explain that enables gradual migration from monolithic applications

---

## 25) What are the trade-offs between monolithic SPAs and micro-frontends?

Monolithic SPAs offer simplicity and consistency but can become unwieldy, while micro-frontends provide flexibility and independence at the cost of complexity and potential inconsistency.

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

- **Core Differences**: Monolithic (simpler deployment, consistent UX, shared dependencies), Micro-frontends (independent deployment, technology diversity, team autonomy)
- **Real-World Consideration**: Consider team size, application complexity, and organizational structure
- **Common Trade-off**: Balance between simplicity and flexibility
- **Advanced Evaluation**: Evaluate long-term maintenance and scaling requirements
- **Interview Tip**: Explain that choose based on organizational needs

---

## 26) How do you manage shared dependencies across multiple front-end apps?

Shared dependency management in micro-frontends requires careful coordination to avoid version conflicts while maintaining consistency and reducing bundle size.

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

- **Core Approach**: Use Module Federation for shared dependency management
- **Real-World Use**: Define clear version constraints and compatibility rules
- **Common Practice**: Implement shared component libraries for consistency
- **Advanced Strategy**: Consider CDN delivery for common dependencies
- **Interview Tip**: Explain that monitor bundle size and dependency conflicts

---

## 27) How do you ensure seamless navigation across micro-frontends?

Seamless navigation requires shared routing state, consistent navigation patterns, and proper handling of deep linking and browser history across micro-frontend boundaries.

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

- **Core Requirement**: Implement shared routing state and navigation context
- **Real-World Use**: Use consistent URL patterns and deep linking
- **Common Practice**: Handle browser back/forward navigation properly
- **Advanced Feature**: Consider single-page application routing patterns
- **Interview Tip**: Explain that ensure proper state management across boundaries

---

## 28) How do you deploy and version micro-frontends independently?

Independent deployment requires proper versioning strategies, backward compatibility, and coordination mechanisms to ensure smooth updates without breaking the overall application.

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

- **Core Strategy**: Implement semantic versioning for micro-frontends
- **Real-World Use**: Use feature flags for gradual rollouts
- **Common Practice**: Maintain backward compatibility during transitions
- **Advanced Feature**: Implement proper error handling and fallbacks
- **Interview Tip**: Explain that consider blue-green deployment strategies

---

## 29) What are tools and strategies for building micro-frontends (Webpack Module Federation, Single-SPA, NX)?

Different tools provide various approaches to micro-frontend architecture, each with specific strengths for different use cases and organizational needs.

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

- **Core Tools**: Module Federation (best for webpack-based applications), Single-SPA (framework-agnostic, good for mixed technology stacks), NX (excellent for monorepo management and code sharing)
- **Real-World Choice**: Choose based on existing technology stack and team preferences
- **Common Consideration**: Consider long-term maintenance and team expertise
- **Advanced Strategy**: Evaluate tools based on specific requirements
- **Interview Tip**: Explain that each tool has different strengths

---

## 30) How do you handle authentication and routing in a micro-frontend setup?

Authentication and routing in micro-frontends require shared state management, consistent security policies, and proper token handling across different modules.

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

- **Core Approach**: Implement shared authentication state and context
- **Real-World Use**: Use consistent token management and refresh strategies
- **Common Practice**: Implement role-based access control across micro-frontends
- **Advanced Feature**: Handle authentication errors and token expiration
- **Interview Tip**: Explain that consider single sign-on (SSO) integration

---

## 31) How would you migrate a large monolithic React app to micro-frontends?

Migration to micro-frontends should be gradual, starting with identifying boundaries, extracting modules, and implementing shared infrastructure while maintaining system stability.

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

- **Core Strategy**: Start with identifying clear module boundaries
- **Real-World Use**: Use feature flags for gradual migration
- **Common Practice**: Extract shared dependencies and utilities first
- **Advanced Approach**: Implement proper testing and validation
- **Interview Tip**: Explain that consider team structure and ownership, plan for rollback strategies

---

## 32) How do you enforce consistent UI/UX across multiple micro-frontends?

Consistent UI/UX requires shared design systems, component libraries, and design tokens that can be consumed across different micro-frontends.

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

- **Core Solution**: Create shared design system and component library
- **Real-World Use**: Use design tokens for consistent styling
- **Common Practice**: Implement shared theme and branding
- **Advanced Feature**: Establish design guidelines and standards
- **Interview Tip**: Explain that regular design reviews and audits

---

## 33) How do you debug and monitor performance across micro-frontends?

Debugging and monitoring micro-frontends requires distributed tracing, centralized logging, and performance monitoring across the entire application ecosystem.

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

- **Core Approach**: Implement distributed tracing for request flow
- **Real-World Use**: Use centralized logging and monitoring
- **Common Practice**: Track performance metrics across micro-frontends
- **Advanced Feature**: Implement error tracking and alerting
- **Interview Tip**: Explain that consider observability tools and dashboards

---
