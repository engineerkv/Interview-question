# 🏗️ Frontend System Design Cheatsheet - Interview Quick Reference

## 🚀 Quick Reference Guide

### 🌐 Web Architecture & Rendering
- **Client-Server Flow**: DNS  TCP  HTTP  Rendering
- **Rendering Strategies**: SSR, CSR, ISR, SSG
- **CDN**: Content delivery networks for global performance
- **Core Web Vitals**: LCP, CLS, INP, FID, TTFB

### 🏗️ Application Architecture
- **MVC/MVVM**: Model-View-Controller/ViewModel patterns
- **Micro-frontends**: Independent deployable frontend modules
- **Module Federation**: Shared dependencies and code splitting
- **Design Systems**: Component libraries and design tokens

### 📊 Data Fetching & Caching
- **REST vs GraphQL**: API design patterns
- **Caching Strategies**: Browser, CDN, application-level caching
- **State Management**: Redux, Zustand, Context API
- **Real-time Data**: WebSockets, SSE, long polling

### ⚡ Performance & Metrics
- **Core Web Vitals**: LCP < 2.5s, CLS < 0.1, INP < 200ms
- **Bundle Optimization**: Code splitting, tree shaking, lazy loading
- **Image Optimization**: WebP, lazy loading, responsive images
- **Monitoring**: RUM, synthetic monitoring, performance budgets

### 🚀 Infrastructure & CI/CD
- **Deployment Strategies**: Blue-green, canary, rolling updates
- **Environment Management**: Staging, production, feature flags
- **Build Optimization**: Incremental builds, caching, parallelization
- **Security**: CSP, HTTPS, authentication, authorization

### 🎨 UX & Design Systems
- **Accessibility**: WCAG guidelines, ARIA attributes, keyboard navigation
- **Design Tokens**: Colors, typography, spacing, breakpoints
- **Component Architecture**: Atomic design, reusable components
- **Cross-browser**: Compatibility, progressive enhancement

## 🎯 System Design Patterns

### High-Performance Dashboard
```javascript
// Component architecture
const Dashboard = () => {
  const [data, setData] = useState(null);
  const [loading, setLoading] = useState(true);
  
  useEffect(() => {
    // Lazy load heavy components
    import('./Charts').then(module => {
      setCharts(module.default);
    });
  }, []);
  
  return (
    <Suspense fallback={<Skeleton />}>
      <DataGrid data={data} />
      <Charts />
    </Suspense>
  );
};
```

### Offline-First PWA
```javascript
// Service worker registration
if ('serviceWorker' in navigator) {
  navigator.serviceWorker.register('/sw.js')
    .then(registration => {
      console.log('SW registered');
    });
}

// Offline data handling
const useOfflineData = () => {
  const [isOnline, setIsOnline] = useState(navigator.onLine);
  
  useEffect(() => {
    const handleOnline = () => setIsOnline(true);
    const handleOffline = () => setIsOnline(false);
    
    window.addEventListener('online', handleOnline);
    window.addEventListener('offline', handleOffline);
    
    return () => {
      window.removeEventListener('online', handleOnline);
      window.removeEventListener('offline', handleOffline);
    };
  }, []);
  
  return isOnline;
};
```

### Micro-frontend Architecture
```javascript
// Module Federation configuration
const ModuleFederationPlugin = require('@module-federation/webpack');

module.exports = {
  plugins: [
    new ModuleFederationPlugin({
      name: 'shell',
      remotes: {
        'user-app': 'userApp@http://localhost:3001/remoteEntry.js',
        'product-app': 'productApp@http://localhost:3002/remoteEntry.js',
      },
      shared: {
        react: { singleton: true },
        'react-dom': { singleton: true },
      },
    }),
  ],
};
```

### Real-time Data Sync
```javascript
// WebSocket connection management
class WebSocketManager {
  constructor(url) {
    this.url = url;
    this.ws = null;
    this.reconnectAttempts = 0;
    this.maxReconnectAttempts = 5;
  }
  
  connect() {
    this.ws = new WebSocket(this.url);
    
    this.ws.onopen = () => {
      console.log('Connected');
      this.reconnectAttempts = 0;
    };
    
    this.ws.onclose = () => {
      this.handleReconnect();
    };
    
    this.ws.onerror = (error) => {
      console.error('WebSocket error:', error);
    };
  }
  
  handleReconnect() {
    if (this.reconnectAttempts < this.maxReconnectAttempts) {
      setTimeout(() => {
        this.reconnectAttempts++;
        this.connect();
      }, 1000 * this.reconnectAttempts);
    }
  }
}
```

## 📊 Performance Optimization

### Bundle Analysis
```javascript
// Webpack bundle analyzer
const BundleAnalyzerPlugin = require('webpack-bundle-analyzer').BundleAnalyzerPlugin;

module.exports = {
  plugins: [
    new BundleAnalyzerPlugin({
      analyzerMode: 'static',
      openAnalyzer: false,
    }),
  ],
};
```

### Code Splitting
```javascript
// Route-based code splitting
const Home = lazy(() => import('./pages/Home'));
const About = lazy(() => import('./pages/About'));
const Contact = lazy(() => import('./pages/Contact'));

// Component-based code splitting
const HeavyComponent = lazy(() => import('./HeavyComponent'));

const App = () => (
  <Router>
    <Suspense fallback={<Loading />}>
      <Routes>
        <Route path="/" element={<Home />} />
        <Route path="/about" element={<About />} />
        <Route path="/contact" element={<Contact />} />
      </Routes>
    </Suspense>
  </Router>
);
```

### Image Optimization
```javascript
// Responsive images with lazy loading
const OptimizedImage = ({ src, alt, sizes }) => {
  const [isLoaded, setIsLoaded] = useState(false);
  const [isInView, setIsInView] = useState(false);
  const imgRef = useRef();
  
  useEffect(() => {
    const observer = new IntersectionObserver(
      ([entry]) => {
        if (entry.isIntersecting) {
          setIsInView(true);
          observer.disconnect();
        }
      },
      { threshold: 0.1 }
    );
    
    if (imgRef.current) {
      observer.observe(imgRef.current);
    }
    
    return () => observer.disconnect();
  }, []);
  
  return (
    <div ref={imgRef} className="image-container">
      {isInView && (
        <img
          src={src}
          alt={alt}
          sizes={sizes}
          onLoad={() => setIsLoaded(true)}
          className={`lazy-image ${isLoaded ? 'loaded' : ''}`}
        />
      )}
    </div>
  );
};
```

## 🎨 Design System Architecture

### Component Library
```javascript
// Design system component
const Button = ({ variant, size, children, ...props }) => {
  const baseStyles = {
    padding: size === 'large' ? '12px 24px' : '8px 16px',
    borderRadius: '4px',
    border: 'none',
    cursor: 'pointer',
    fontSize: size === 'large' ? '16px' : '14px',
  };
  
  const variantStyles = {
    primary: { backgroundColor: '#007bff', color: 'white' },
    secondary: { backgroundColor: '#6c757d', color: 'white' },
    outline: { backgroundColor: 'transparent', border: '1px solid #007bff', color: '#007bff' },
  };
  
  return (
    <button
      style={{ ...baseStyles, ...variantStyles[variant] }}
      {...props}
    >
      {children}
    </button>
  );
};
```

### Theme System
```javascript
// Theme provider
const ThemeContext = createContext();

const ThemeProvider = ({ children }) => {
  const [theme, setTheme] = useState('light');
  
  const toggleTheme = () => {
    setTheme(prev => prev === 'light' ? 'dark' : 'light');
  };
  
  return (
    <ThemeContext.Provider value={{ theme, toggleTheme }}>
      <div className={`theme-${theme}`}>
        {children}
      </div>
    </ThemeContext.Provider>
  );
};

// CSS variables for theming
:root {
  --primary-color: #007bff;
  --background-color: #ffffff;
  --text-color: #333333;
}

[data-theme="dark"] {
  --primary-color: #0d6efd;
  --background-color: #212529;
  --text-color: #ffffff;
}
```

## 🚀 Interview Scenarios

### High-Traffic E-commerce Site
- **CDN Strategy**: Global content delivery
- **Caching**: Multi-level caching (browser, CDN, application)
- **Performance**: Core Web Vitals optimization
- **Scalability**: Micro-frontend architecture

### Real-time Collaboration App
- **WebSockets**: Real-time communication
- **Conflict Resolution**: Operational transforms
- **Offline Support**: Local storage and sync
- **Security**: Authentication and authorization

### Multi-tenant SaaS Platform
- **Theme System**: Dynamic styling per tenant
- **Feature Flags**: Tenant-specific features
- **Data Isolation**: Secure multi-tenancy
- **Performance**: Tenant-specific optimizations

---

*This cheatsheet covers essential frontend system design concepts for interview preparation, including architecture patterns, performance optimization, and real-world scenarios.*
