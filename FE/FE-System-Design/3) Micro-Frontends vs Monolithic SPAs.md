# 3) Micro-Frontends vs Monolithic SPAs (Q24–33)

## 24) What is a micro-frontend, and what problems does it solve?

Concept: Micro-frontends are an architectural approach where frontend applications are composed of independent, loosely coupled modules that can be developed, deployed, and scaled independently.

Example:
```javascript
// Micro-frontend shell application
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
        script.id = scriptId;
        script.src = `${host}${manifest.files['main.js']}`;
        script.onload = () => renderMicroFrontend(name, history);
        document.head.appendChild(script);
      });
  }, [name, host, history]);
  
  return <div id={`${name}-container`} />;
};

// Usage in shell app
const App = () => (
  <Router>
    <Routes>
      <Route path="/dashboard/*" element={<MicroFrontend name="Dashboard" host="http://localhost:3001" />} />
      <Route path="/profile/*" element={<MicroFrontend name="Profile" host="http://localhost:3002" />} />
    </Routes>
  </Router>
);
```

Deep Insight:
- Enables independent team development and deployment
- Reduces coordination overhead between teams
- Allows technology diversity across frontend modules
- Improves scalability and maintainability
- Enables gradual migration from monolithic applications

## 25) What are the trade-offs between monolithic SPAs and micro-frontends?

Concept: Monolithic SPAs offer simplicity and consistency but can become unwieldy, while micro-frontends provide flexibility and independence at the cost of complexity and potential inconsistency.

Example:
```javascript
// Monolithic SPA - simple but can become large
const MonolithicApp = () => (
  <div className="app">
    <Header />
    <Sidebar />
    <main>
      <Dashboard />
      <Profile />
      <Settings />
    </main>
    <Footer />
  </div>
);

// Micro-frontend - more complex but modular
const MicroFrontendApp = () => (
  <div className="app">
    <Header />
    <Sidebar />
    <main>
      <MicroFrontend name="Dashboard" host="http://localhost:3001" />
      <MicroFrontend name="Profile" host="http://localhost:3002" />
      <MicroFrontend name="Settings" host="http://localhost:3003" />
    </main>
    <Footer />
  </div>
);
```

Deep Insight:
- Monolithic: Simpler deployment, consistent UX, shared dependencies
- Micro-frontends: Independent deployment, technology diversity, team autonomy
- Consider team size, application complexity, and organizational structure
- Balance between simplicity and flexibility
- Evaluate long-term maintenance and scaling requirements

## 26) How do you manage shared dependencies across multiple front-end apps?

Concept: Shared dependency management in micro-frontends requires careful coordination to avoid version conflicts while maintaining consistency and reducing bundle size.

Example:
```javascript
// Shared dependency configuration
const sharedDependencies = {
  react: {
    singleton: true,
    requiredVersion: '^18.0.0'
  },
  'react-dom': {
    singleton: true,
    requiredVersion: '^18.0.0'
  },
  'react-router-dom': {
    singleton: true,
    requiredVersion: '^6.0.0'
  }
};

// Webpack Module Federation configuration
const ModuleFederationPlugin = require('@module-federation/webpack');

module.exports = {
  plugins: [
    new ModuleFederationPlugin({
      name: 'shell',
      remotes: {
        dashboard: 'dashboard@http://localhost:3001/remoteEntry.js',
        profile: 'profile@http://localhost:3002/remoteEntry.js'
      },
      shared: sharedDependencies
    })
  ]
};
```

Deep Insight:
- Use Module Federation for shared dependency management
- Define clear version constraints and compatibility rules
- Implement shared component libraries for consistency
- Consider CDN delivery for common dependencies
- Monitor bundle size and dependency conflicts

## 27) How do you ensure seamless navigation across micro-frontends?

Concept: Seamless navigation requires shared routing state, consistent navigation patterns, and proper handling of deep linking and browser history across micro-frontend boundaries.

Example:
```javascript
// Shared routing context
const RoutingContext = createContext();

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

// Micro-frontend navigation hook
export const useMicroFrontendNavigation = () => {
  const { navigate } = useContext(RoutingContext);
  
  const navigateToMicroFrontend = (microFrontend, path) => {
    const fullPath = `/${microFrontend}${path}`;
    navigate(fullPath);
  };
  
  return { navigateToMicroFrontend };
};
```

Deep Insight:
- Implement shared routing state and navigation context
- Use consistent URL patterns and deep linking
- Handle browser back/forward navigation properly
- Consider single-page application routing patterns
- Ensure proper state management across boundaries

## 28) How do you deploy and version micro-frontends independently?

Concept: Independent deployment requires proper versioning strategies, backward compatibility, and coordination mechanisms to ensure smooth updates without breaking the overall application.

Example:
```javascript
// Version management for micro-frontends
const microFrontendConfig = {
  dashboard: {
    current: '1.2.0',
    fallback: '1.1.0',
    host: 'https://cdn.example.com/dashboard'
  },
  profile: {
    current: '2.0.0',
    fallback: '1.5.0',
    host: 'https://cdn.example.com/profile'
  }
};

// Dynamic loading with version fallback
const loadMicroFrontend = async (name, version) => {
  try {
    const config = microFrontendConfig[name];
    const script = await loadScript(`${config.host}/${version}/remoteEntry.js`);
    return script;
  } catch (error) {
    console.warn(`Failed to load ${name} v${version}, falling back to v${config.fallback}`);
    return loadScript(`${config.host}/${config.fallback}/remoteEntry.js`);
  }
};
```

Deep Insight:
- Implement semantic versioning for micro-frontends
- Use feature flags for gradual rollouts
- Maintain backward compatibility during transitions
- Implement proper error handling and fallbacks
- Consider blue-green deployment strategies

## 29) What are tools and strategies for building micro-frontends (Webpack Module Federation, Single-SPA, NX)?

Concept: Different tools provide various approaches to micro-frontend architecture, each with specific strengths for different use cases and organizational needs.

Example:
```javascript
// Webpack Module Federation
const ModuleFederationPlugin = require('@module-federation/webpack');

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
import { registerApplication, start } from 'single-spa';

registerApplication({
  name: 'dashboard',
  app: () => System.import('dashboard'),
  activeWhen: '/dashboard'
});

start();

// NX workspace configuration
// nx.json
{
  "projects": {
    "shell": "apps/shell",
    "dashboard": "apps/dashboard",
    "profile": "apps/profile"
  }
}
```

Deep Insight:
- Module Federation: Best for webpack-based applications
- Single-SPA: Framework-agnostic, good for mixed technology stacks
- NX: Excellent for monorepo management and code sharing
- Choose based on existing technology stack and team preferences
- Consider long-term maintenance and team expertise

## 30) How do you handle authentication and routing in a micro-frontend setup?

Concept: Authentication and routing in micro-frontends require shared state management, consistent security policies, and proper token handling across different modules.

Example:
```javascript
// Shared authentication context
const AuthContext = createContext();

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
  
  const logout = () => {
    setUser(null);
    setToken(null);
    localStorage.removeItem('token');
  };
  
  return (
    <AuthContext.Provider value={{ user, token, login, logout }}>
      {children}
    </AuthContext.Provider>
  );
};

// Protected route wrapper
const ProtectedRoute = ({ children, requiredPermissions = [] }) => {
  const { user } = useContext(AuthContext);
  
  if (!user) {
    return <Navigate to="/login" />;
  }
  
  if (requiredPermissions.length > 0) {
    const hasPermission = requiredPermissions.every(permission => 
      user.permissions.includes(permission)
    );
    if (!hasPermission) {
      return <Navigate to="/unauthorized" />;
    }
  }
  
  return children;
};
```

Deep Insight:
- Implement shared authentication state and context
- Use consistent token management and refresh strategies
- Implement role-based access control across micro-frontends
- Handle authentication errors and token expiration
- Consider single sign-on (SSO) integration

## 31) How would you migrate a large monolithic React app to micro-frontends?

Concept: Migration to micro-frontends should be gradual, starting with identifying boundaries, extracting modules, and implementing shared infrastructure while maintaining system stability.

Example:
```javascript
// Migration strategy: Strangler Fig pattern
const MonolithicApp = () => {
  const [migrationFlags, setMigrationFlags] = useState({
    dashboard: false,
    profile: false,
    settings: false
  });
  
  return (
    <div className="app">
      <Header />
      <Sidebar />
      <main>
        {migrationFlags.dashboard ? (
          <MicroFrontend name="Dashboard" host="http://localhost:3001" />
        ) : (
          <LegacyDashboard />
        )}
        
        {migrationFlags.profile ? (
          <MicroFrontend name="Profile" host="http://localhost:3002" />
        ) : (
          <LegacyProfile />
        )}
      </main>
    </div>
  );
};

// Gradual extraction process
const extractModule = (moduleName, dependencies) => {
  // 1. Identify module boundaries
  // 2. Extract shared dependencies
  // 3. Create micro-frontend shell
  // 4. Implement feature flags
  // 5. Test and validate
  // 6. Deploy and monitor
};
```

Deep Insight:
- Start with identifying clear module boundaries
- Use feature flags for gradual migration
- Extract shared dependencies and utilities first
- Implement proper testing and validation
- Consider team structure and ownership
- Plan for rollback strategies

## 32) How do you enforce consistent UI/UX across multiple micro-frontends?

Concept: Consistent UI/UX requires shared design systems, component libraries, and design tokens that can be consumed across different micro-frontends.

Example:
```javascript
// Shared design system
const DesignSystem = {
  colors: {
    primary: '#007bff',
    secondary: '#6c757d',
    success: '#28a745',
    danger: '#dc3545'
  },
  spacing: {
    xs: '4px',
    sm: '8px',
    md: '16px',
    lg: '24px',
    xl: '32px'
  },
  typography: {
    fontFamily: 'Inter, sans-serif',
    fontSize: {
      sm: '14px',
      md: '16px',
      lg: '18px',
      xl: '24px'
    }
  }
};

// Shared component library
const Button = ({ variant = 'primary', size = 'md', children, ...props }) => (
  <button
    className={`btn btn-${variant} btn-${size}`}
    style={{
      backgroundColor: DesignSystem.colors[variant],
      padding: DesignSystem.spacing[size],
      fontFamily: DesignSystem.typography.fontFamily
    }}
    {...props}
  >
    {children}
  </button>
);

// Usage in micro-frontend
const Dashboard = () => (
  <div>
    <Button variant="primary" size="lg">Dashboard Action</Button>
  </div>
);
```

Deep Insight:
- Create shared design system and component library
- Use design tokens for consistent styling
- Implement shared theme and branding
- Establish design guidelines and standards
- Regular design reviews and audits

## 33) How do you debug and monitor performance across micro-frontends?

Concept: Debugging and monitoring micro-frontends requires distributed tracing, centralized logging, and performance monitoring across the entire application ecosystem.

Example:
```javascript
// Centralized logging service
const Logger = {
  info: (message, context = {}) => {
    console.log(`[${new Date().toISOString()}] INFO: ${message}`, context);
    // Send to centralized logging service
    sendToLoggingService('info', message, context);
  },
  error: (message, error, context = {}) => {
    console.error(`[${new Date().toISOString()}] ERROR: ${message}`, error, context);
    sendToLoggingService('error', message, { ...context, error: error.stack });
  }
};

// Performance monitoring
const PerformanceMonitor = {
  trackMicroFrontendLoad: (name, startTime, endTime) => {
    const loadTime = endTime - startTime;
    Logger.info(`Micro-frontend ${name} loaded in ${loadTime}ms`);
    
    // Send to performance monitoring service
    sendToPerformanceService({
      event: 'micro_frontend_load',
      name,
      loadTime,
      timestamp: Date.now()
    });
  },
  
  trackUserInteraction: (microFrontend, action, duration) => {
    sendToAnalyticsService({
      event: 'user_interaction',
      microFrontend,
      action,
      duration,
      timestamp: Date.now()
    });
  }
};
```

Deep Insight:
- Implement distributed tracing for request flow
- Use centralized logging and monitoring
- Track performance metrics across micro-frontends
- Implement error tracking and alerting
- Consider observability tools and dashboards
