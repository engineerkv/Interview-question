# 🏗️ Frontend System Design Interview Notes (2025 Edition)

## ⚡ Section 7 — Real-World System Design Scenarios — Q136-Q150

---

### 136. ⚡ Design a high-performance dashboard that updates in real-time.

**🧠 Concept**

Real-time dashboards require efficient data streaming, optimized rendering, and smart caching to handle continuous updates without performance degradation.

**💻 Example**

```javascript
// Real-time dashboard architecture
const Dashboard = () => {
  const [data, setData] = useState({});
  const [isConnected, setIsConnected] = useState(false);
  
  useEffect(() => {
    const ws = new WebSocket('wss://api.example.com/dashboard');
    
    ws.onmessage = (event) => {
      const newData = JSON.parse(event.data);
      setData(prevData => ({
        ...prevData,
        ...newData
      }));
    };
    
    ws.onopen = () => setIsConnected(true);
    ws.onclose = () => setIsConnected(false);
    
    return () => ws.close();
  }, []);
  
  return (
    <div className="dashboard">
      <ConnectionStatus connected={isConnected} />
      <MetricsGrid data={data} />
      <Charts data={data} />
    </div>
  );
};
```

**💬 Explanation + Insight**

- **WebSocket Connection** - Real-time data streaming
- **State Management** - Efficient state updates
- **Performance** - Optimize rendering for real-time updates
- **Caching** - Smart caching for historical data
- **User Experience** - Smooth real-time updates

---

### 137. ⚡ Design an offline-first PWA for a global user base.

**🧠 Concept**

Offline-first PWAs provide seamless user experience regardless of network connectivity, using service workers and local storage.

**💻 Example**

```javascript
// Service worker for offline support
self.addEventListener('fetch', event => {
  event.respondWith(
    caches.match(event.request)
      .then(response => {
        if (response) {
          return response; // Serve from cache
        }
        return fetch(event.request)
          .then(fetchResponse => {
            const responseClone = fetchResponse.clone();
            caches.open('v1').then(cache => {
              cache.put(event.request, responseClone);
            });
            return fetchResponse;
          });
      })
  );
});

// Offline-first data management
const OfflineManager = {
  async getData(key) {
    try {
      const response = await fetch(`/api/${key}`);
      const data = await response.json();
      localStorage.setItem(key, JSON.stringify(data));
      return data;
    } catch (error) {
      return JSON.parse(localStorage.getItem(key) || '{}');
    }
  }
};
```

**💬 Explanation + Insight**

- **Service Workers** - Enable offline functionality
- **Caching Strategy** - Cache resources for offline use
- **Data Synchronization** - Sync data when online
- **User Experience** - Seamless offline experience
- **Global Reach** - Work across different network conditions

---

### 138. ⚡ Architect a multi-tenant SaaS using Next.js and React.

**🧠 Concept**

Multi-tenant SaaS architecture requires tenant isolation, shared infrastructure, and scalable design to serve multiple customers efficiently.

**💻 Example**

```javascript
// Multi-tenant architecture
const TenantProvider = ({ children }) => {
  const [tenant, setTenant] = useState(null);
  
  useEffect(() => {
    const subdomain = window.location.hostname.split('.')[0];
    loadTenant(subdomain).then(setTenant);
  }, []);
  
  return (
    <TenantContext.Provider value={tenant}>
      {children}
    </TenantContext.Provider>
  );
};

// Tenant-specific routing
const App = () => {
  const { tenant } = useTenant();
  
  return (
    <Router>
      <Routes>
        <Route path="/dashboard" element={<Dashboard />} />
        <Route path="/settings" element={<Settings />} />
        {tenant?.features?.analytics && (
          <Route path="/analytics" element={<Analytics />} />
        )}
      </Routes>
    </Router>
  );
};
```

**💬 Explanation + Insight**

- **Tenant Isolation** - Separate data and configuration
- **Shared Infrastructure** - Efficient resource utilization
- **Scalability** - Scale across multiple tenants
- **Customization** - Per-tenant branding and features
- **Security** - Ensure tenant data isolation

---

### 139. ⚡ Design a CDN caching strategy for a content-heavy web app.

**🧠 Concept**

CDN caching strategy optimizes content delivery through edge caching, cache invalidation, and content optimization.

**💻 Example**

```javascript
// CDN caching configuration
const cacheConfig = {
  static: {
    '*.css': { ttl: '1y', cacheControl: 'public, immutable' },
    '*.js': { ttl: '1y', cacheControl: 'public, immutable' },
    '*.png': { ttl: '1y', cacheControl: 'public, immutable' }
  },
  dynamic: {
    '/api/data': { ttl: '1h', cacheControl: 'public, max-age=3600' },
    '/api/user': { ttl: '5m', cacheControl: 'private, max-age=300' }
  }
};

// Cache invalidation
const invalidateCache = (pattern) => {
  fetch('/api/cache/invalidate', {
    method: 'POST',
    body: JSON.stringify({ pattern })
  });
};
```

**💬 Explanation + Insight**

- **Edge Caching** - Cache content at edge locations
- **Cache Invalidation** - Invalidate stale content
- **Performance** - Reduce latency and bandwidth
- **Scalability** - Handle high traffic loads
- **Cost Optimization** - Reduce origin server load

---

### 140. ⚡ Architect a micro-frontend setup using Module Federation.

**🧠 Concept**

Micro-frontend architecture using Module Federation enables independent development and deployment of frontend applications.

**💻 Example**

```javascript
// Module Federation configuration
// webpack.config.js
const ModuleFederationPlugin = require('@module-federation/webpack');

module.exports = {
  plugins: [
    new ModuleFederationPlugin({
      name: 'shell',
      remotes: {
        userApp: 'userApp@http://localhost:3001/remoteEntry.js',
        productApp: 'productApp@http://localhost:3002/remoteEntry.js'
      },
      shared: {
        react: { singleton: true },
        'react-dom': { singleton: true }
      }
    })
  ]
};

// Remote component usage
const RemoteComponent = React.lazy(() => 
  import('userApp/UserProfile')
);
```

**💬 Explanation + Insight**

- **Independent Development** - Teams work autonomously
- **Shared Dependencies** - Share common libraries
- **Runtime Integration** - Load modules at runtime
- **Scalability** - Scale development across teams
- **Technology Diversity** - Different tech stacks per micro-frontend

---

### 141. ⚡ Design an analytics dashboard that tracks Core Web Vitals.

**🧠 Concept**

Analytics dashboards for Core Web Vitals require real-time data collection, visualization, and alerting for performance monitoring.

**💻 Example**

```javascript
// Core Web Vitals tracking
import { getCLS, getFID, getFCP, getLCP, getTTFB } from 'web-vitals';

const trackWebVitals = () => {
  getCLS(sendToAnalytics);
  getFID(sendToAnalytics);
  getFCP(sendToAnalytics);
  getLCP(sendToAnalytics);
  getTTFB(sendToAnalytics);
};

const sendToAnalytics = (metric) => {
  gtag('event', metric.name, {
    value: Math.round(metric.value),
    event_category: 'Web Vitals',
    event_label: metric.id
  });
};

// Analytics dashboard
const AnalyticsDashboard = () => {
  const [metrics, setMetrics] = useState({});
  
  return (
    <div className="dashboard">
      <MetricsChart data={metrics} />
      <AlertsPanel metrics={metrics} />
      <PerformanceTrends data={metrics} />
    </div>
  );
};
```

**💬 Explanation + Insight**

- **Real-time Tracking** - Monitor performance metrics
- **Data Visualization** - Present metrics clearly
- **Alerting** - Notify on performance issues
- **Trend Analysis** - Track performance over time
- **User Experience** - Improve based on metrics

---

### 142. ⚡ Build an accessible design system for enterprise teams.

**🧠 Concept**

Enterprise design systems require comprehensive accessibility, documentation, and governance to ensure consistent, accessible user experiences.

**💻 Example**

```javascript
// Accessible component example
const Button = ({ children, variant, size, disabled, ...props }) => {
  return (
    <button
      className={`btn btn-${variant} btn-${size}`}
      disabled={disabled}
      aria-disabled={disabled}
      {...props}
    >
      {children}
    </button>
  );
};

// Design system documentation
const DesignSystem = {
  components: {
    Button: {
      accessibility: {
        keyboard: true,
        screenReader: true,
        colorContrast: 'AA'
      },
      variants: ['primary', 'secondary', 'danger'],
      sizes: ['sm', 'md', 'lg']
    }
  }
};
```

**💬 Explanation + Insight**

- **Accessibility Standards** - Meet WCAG guidelines
- **Documentation** - Comprehensive component documentation
- **Governance** - Establish design system governance
- **Consistency** - Ensure consistent accessible experiences
- **Enterprise Scale** - Scale across large organizations

---

### 143. ⚡ Architect a large e-commerce site with localized content.

**🧠 Concept**

E-commerce localization requires content management, currency handling, language support, and region-specific features.

**💻 Example**

```javascript
// Localization architecture
const LocalizationProvider = ({ children }) => {
  const [locale, setLocale] = useState('en-US');
  const [currency, setCurrency] = useState('USD');
  
  const contextValue = {
    locale,
    currency,
    setLocale,
    setCurrency,
    t: (key) => translations[locale][key],
    formatPrice: (amount) => formatCurrency(amount, currency)
  };
  
  return (
    <LocalizationContext.Provider value={contextValue}>
      {children}
    </LocalizationContext.Provider>
  );
};

// Localized content
const ProductCard = ({ product }) => {
  const { t, formatPrice } = useLocalization();
  
  return (
    <div className="product-card">
      <h3>{product.name[locale]}</h3>
      <p>{formatPrice(product.price)}</p>
      <button>{t('addToCart')}</button>
    </div>
  );
};
```

**💬 Explanation + Insight**

- **Content Localization** - Translate content for different regions
- **Currency Handling** - Support multiple currencies
- **Regional Features** - Region-specific functionality
- **User Experience** - Localized user experience
- **Scalability** - Scale across global markets

---

### 144. ⚡ Design a dark/light mode theming system with persistence.

**🧠 Concept**

Theme systems provide user preference persistence, smooth transitions, and consistent theming across applications.

**💻 Example**

```javascript
// Theme system implementation
const ThemeProvider = ({ children }) => {
  const [theme, setTheme] = useState(() => {
    const saved = localStorage.getItem('theme');
    return saved || 'light';
  });
  
  useEffect(() => {
    localStorage.setItem('theme', theme);
    document.documentElement.setAttribute('data-theme', theme);
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

// Theme-aware components
const ThemedButton = styled.button`
  background-color: ${props => props.theme.colors.primary};
  color: ${props => props.theme.colors.text};
  transition: all 0.3s ease;
`;
```

**💬 Explanation + Insight**

- **User Preference** - Respect user theme preferences
- **Persistence** - Save theme choice across sessions
- **Smooth Transitions** - Animate theme changes
- **Consistency** - Consistent theming across components
- **Accessibility** - Support high contrast and dark modes

---

### 145. ⚡ Build a front-end system for 10M daily users — what bottlenecks arise?

**🧠 Concept**

High-traffic frontend systems face bottlenecks in rendering, data fetching, caching, and user experience that require optimization.

**💻 Example**

```javascript
// High-traffic optimization strategies
const HighTrafficApp = () => {
  // Code splitting
  const LazyComponent = React.lazy(() => import('./HeavyComponent'));
  
  // Virtual scrolling for large lists
  const VirtualList = ({ items }) => {
    const [visibleItems, setVisibleItems] = useState([]);
    // Virtual scrolling implementation
  };
  
  // Aggressive caching
  const useCachedData = (key) => {
    const [data, setData] = useState(null);
    const [loading, setLoading] = useState(true);
    
    useEffect(() => {
      const cached = sessionStorage.getItem(key);
      if (cached) {
        setData(JSON.parse(cached));
        setLoading(false);
      } else {
        fetchData(key).then(result => {
          setData(result);
          sessionStorage.setItem(key, JSON.stringify(result));
          setLoading(false);
        });
      }
    }, [key]);
    
    return { data, loading };
  };
};
```

**💬 Explanation + Insight**

- **Rendering Performance** - Optimize rendering for large user base
- **Data Management** - Efficient data fetching and caching
- **Code Splitting** - Load only necessary code
- **Caching Strategy** - Aggressive caching for performance
- **Scalability** - Design for high traffic loads

---

### 146. ⚡ Design a deployment strategy for low-downtime React apps.

**🧠 Concept**

Low-downtime deployment strategies ensure continuous availability through blue-green deployments, feature flags, and rollback capabilities.

**💻 Example**

```javascript
// Blue-green deployment strategy
const DeploymentStrategy = {
  // Blue environment (current)
  blue: {
    url: 'https://blue.example.com',
    status: 'active'
  },
  // Green environment (new)
  green: {
    url: 'https://green.example.com',
    status: 'inactive'
  },
  
  // Switch traffic
  switchTraffic: () => {
    // Update load balancer to point to green
    updateLoadBalancer('green');
    // Monitor green environment
    monitorHealth('green');
  },
  
  // Rollback if issues
  rollback: () => {
    updateLoadBalancer('blue');
  }
};

// Feature flags for gradual rollout
const FeatureFlag = ({ flag, children }) => {
  const { flags } = useFeatureFlags();
  return flags[flag] ? children : null;
};
```

**💬 Explanation + Insight**

- **Blue-Green Deployment** - Switch between environments
- **Feature Flags** - Gradual feature rollouts
- **Health Monitoring** - Monitor deployment health
- **Rollback Strategy** - Quick rollback on issues
- **Zero Downtime** - Maintain service availability

---

### 147. ⚡ Build an observability setup for frontend performance alerts.

**🧠 Concept**

Frontend observability requires comprehensive monitoring, alerting, and debugging capabilities for production applications.

**💻 Example**

```javascript
// Performance monitoring setup
const PerformanceMonitor = {
  // Core Web Vitals tracking
  trackWebVitals: () => {
    getCLS(sendMetric);
    getFID(sendMetric);
    getLCP(sendMetric);
  },
  
  // Custom performance marks
  markStart: (name) => {
    performance.mark(`${name}-start`);
  },
  
  markEnd: (name) => {
    performance.mark(`${name}-end`);
    performance.measure(name, `${name}-start`, `${name}-end`);
  },
  
  // Error tracking
  trackError: (error, context) => {
    console.error('Error:', error, context);
    // Send to monitoring service
    sendToMonitoring('error', { error, context });
  }
};

// Alerting configuration
const alertConfig = {
  thresholds: {
    LCP: 2500, // 2.5 seconds
    FID: 100,  // 100ms
    CLS: 0.1   // 0.1
  },
  channels: ['email', 'slack', 'pagerduty']
};
```

**💬 Explanation + Insight**

- **Performance Monitoring** - Track key performance metrics
- **Error Tracking** - Monitor and debug errors
- **Alerting** - Notify on performance issues
- **Debugging** - Comprehensive debugging information
- **Production Insights** - Real-world performance data

---

### 148. ⚡ Architect an edge-rendered global app with Cloudflare Workers.

**🧠 Concept**

Edge rendering with Cloudflare Workers enables global performance through distributed rendering and edge computing.

**💻 Example**

```javascript
// Cloudflare Worker for edge rendering
export default {
  async fetch(request, env) {
    const url = new URL(request.url);
    
    // Check if page should be rendered at edge
    if (shouldRenderAtEdge(url)) {
      const html = await renderPage(url);
      return new Response(html, {
        headers: {
          'Content-Type': 'text/html',
          'Cache-Control': 'public, max-age=3600'
        }
      });
    }
    
    // Fallback to origin
    return fetch(request);
  }
};

// Edge rendering logic
const renderPage = async (url) => {
  const { renderToString } = await import('react-dom/server');
  const App = await import('./App');
  
  const html = renderToString(<App />);
  return `
    <!DOCTYPE html>
    <html>
      <head>
        <title>Edge Rendered App</title>
      </head>
      <body>
        <div id="root">${html}</div>
        <script src="/client.js"></script>
      </body>
    </html>
  `;
};
```

**💬 Explanation + Insight**

- **Edge Computing** - Process requests at edge locations
- **Global Performance** - Reduce latency worldwide
- **Distributed Rendering** - Render pages at edge
- **Caching** - Cache rendered pages at edge
- **Scalability** - Scale across global infrastructure

---

### 149. ⚡ Design a feature flag rollout system for frontend releases.

**🧠 Concept**

Feature flag systems enable controlled feature rollouts, A/B testing, and risk mitigation for frontend releases.

**💻 Example**

```javascript
// Feature flag system
const FeatureFlagProvider = ({ children }) => {
  const [flags, setFlags] = useState({});
  
  useEffect(() => {
    // Load feature flags
    loadFeatureFlags().then(setFlags);
    
    // Listen for flag updates
    const eventSource = new EventSource('/api/flags/stream');
    eventSource.onmessage = (event) => {
      const newFlags = JSON.parse(event.data);
      setFlags(prev => ({ ...prev, ...newFlags }));
    };
  }, []);
  
  return (
    <FeatureFlagContext.Provider value={flags}>
      {children}
    </FeatureFlagContext.Provider>
  );
};

// Feature flag usage
const FeatureComponent = ({ flag, children, fallback }) => {
  const flags = useFeatureFlags();
  return flags[flag] ? children : fallback;
};

// Gradual rollout
const GradualRollout = ({ feature, children }) => {
  const { user } = useUser();
  const rolloutPercentage = getRolloutPercentage(feature);
  const shouldShow = hashUserId(user.id) < rolloutPercentage;
  
  return shouldShow ? children : null;
};
```

**💬 Explanation + Insight**

- **Controlled Rollouts** - Gradual feature deployment
- **A/B Testing** - Test different feature versions
- **Risk Mitigation** - Reduce deployment risks
- **User Segmentation** - Target specific user groups
- **Real-time Updates** - Update flags without deployment

---

### 150. ⚡ Optimize a slow SPA — what step-by-step approach do you take?

**🧠 Concept**

SPA optimization requires systematic analysis of performance bottlenecks, followed by targeted optimizations and monitoring.

**💻 Example**

```javascript
// SPA optimization checklist
const SPOptimization = {
  // 1. Bundle analysis
  analyzeBundle: () => {
    // Use webpack-bundle-analyzer
    // Identify large dependencies
    // Find duplicate code
  },
  
  // 2. Code splitting
  implementCodeSplitting: () => {
    const LazyComponent = React.lazy(() => import('./Component'));
    return (
      <Suspense fallback={<Loading />}>
        <LazyComponent />
      </Suspense>
    );
  },
  
  // 3. Image optimization
  optimizeImages: () => {
    // Use next/image or similar
    // Implement lazy loading
    // Use WebP format
  },
  
  // 4. Caching strategy
  implementCaching: () => {
    // Service worker caching
    // HTTP caching headers
    // CDN caching
  },
  
  // 5. Performance monitoring
  monitorPerformance: () => {
    // Track Core Web Vitals
    // Monitor bundle size
    // Alert on regressions
  }
};
```

**💬 Explanation + Insight**

- **Systematic Approach** - Step-by-step optimization
- **Performance Analysis** - Identify bottlenecks
- **Targeted Optimization** - Focus on high-impact changes
- **Monitoring** - Track optimization results
- **Continuous Improvement** - Ongoing performance optimization

---

*This comprehensive real-world scenarios section covers all essential concepts including high-performance dashboards, offline-first PWAs, multi-tenant SaaS, micro-frontends, analytics, accessibility, localization, theming, high-traffic systems, deployment strategies, observability, edge rendering, feature flags, and SPA optimization for building production-ready frontend applications.*