# 🎨 Front-End System Design Interview Cheatsheet

> **Quick reference guide for front-end system design interviews**

## 📋 Table of Contents

- [Architecture Patterns](#architecture-patterns)
- [Performance Optimization](#performance-optimization)
- [State Management](#state-management)
- [Micro-Frontends](#micro-frontends)
- [Cross-Platform Development](#cross-platform-development)
- [Accessibility & UX](#accessibility--ux)
- [Browser Internals](#browser-internals)
- [Real-World Scenarios](#real-world-scenarios)
- [Common Patterns](#common-patterns)

---

## Architecture Patterns

### Scalable Front-End Architecture
```javascript
// Feature-based architecture
src/
  features/
    auth/
      components/
      hooks/
      services/
      types/
  shared/
    components/
    hooks/
    utils/
    types/
```

### Component Design Patterns
```javascript
// Container vs Presentational
const UserListContainer = () => {
  const [users, setUsers] = useState([]);
  const [loading, setLoading] = useState(true);
  
  useEffect(() => {
    fetchUsers().then(setUsers).finally(() => setLoading(false));
  }, []);
  
  return <UserList users={users} loading={loading} />;
};

// Atomic Design
const Button = ({ variant, size, children }) => (
  <button className={`btn btn-${variant} btn-${size}`}>
    {children}
  </button>
);
```

### State Management
```javascript
// Context API for global state
const AppStateContext = createContext();

export const AppStateProvider = ({ children }) => {
  const [state, dispatch] = useReducer(appReducer, initialState);
  return (
    <AppStateContext.Provider value={{ state, dispatch }}>
      {children}
    </AppStateContext.Provider>
  );
};

// Custom hooks for state logic
const useAuth = () => {
  const { state, dispatch } = useContext(AuthContext);
  const login = (credentials) => dispatch({ type: 'LOGIN', payload: credentials });
  const logout = () => dispatch({ type: 'LOGOUT' });
  return { user: state.user, login, logout };
};
```

---

## Performance Optimization

### Core Web Vitals
```javascript
// Measuring Core Web Vitals
import { getCLS, getFID, getFCP, getLCP, getTTFB } from 'web-vitals';

getCLS(console.log);
getFID(console.log);
getFCP(console.log);
getLCP(console.log);
getTTFB(console.log);

// LCP optimization
const ImageComponent = ({ src, alt }) => {
  useEffect(() => {
    const link = document.createElement('link');
    link.rel = 'preload';
    link.as = 'image';
    link.href = src;
    document.head.appendChild(link);
  }, [src]);
  
  return <img src={src} alt={alt} loading="eager" />;
};
```

### Code Splitting & Lazy Loading
```javascript
// Route-based code splitting
const Home = lazy(() => import('./pages/Home'));
const About = lazy(() => import('./pages/About'));

const App = () => (
  <Router>
    <Suspense fallback={<div>Loading...</div>}>
      <Routes>
        <Route path="/" element={<Home />} />
        <Route path="/about" element={<About />} />
      </Routes>
    </Suspense>
  </Router>
);

// Component-based code splitting
const LazyComponent = lazy(() => import('./HeavyComponent'));

const ParentComponent = () => (
  <Suspense fallback={<div>Loading...</div>}>
    <LazyComponent />
  </Suspense>
);
```

### Caching Strategies
```javascript
// Service Worker caching
self.addEventListener('fetch', event => {
  const { request } = event;
  const url = new URL(request.url);
  
  if (url.pathname.startsWith('/api/')) {
    event.respondWith(networkFirst(request));
  } else if (url.pathname.startsWith('/static/')) {
    event.respondWith(cacheFirst(request));
  } else {
    event.respondWith(staleWhileRevalidate(request));
  }
});

// Client-side caching
const cache = new Map();

const fetchWithCache = async (url) => {
  if (cache.has(url)) {
    return cache.get(url);
  }
  
  const response = await fetch(url);
  const data = await response.json();
  cache.set(url, data);
  return data;
};
```

---

## State Management

### Context API
```javascript
// Theme context
const ThemeContext = createContext();

export const ThemeProvider = ({ children }) => {
  const [theme, setTheme] = useState('light');
  
  const toggleTheme = () => {
    setTheme(prev => prev === 'light' ? 'dark' : 'light');
  };
  
  return (
    <ThemeContext.Provider value={{ theme, toggleTheme }}>
      {children}
    </ThemeContext.Provider>
  );
};

// Custom hook
export const useTheme = () => {
  const context = useContext(ThemeContext);
  if (!context) {
    throw new Error('useTheme must be used within ThemeProvider');
  }
  return context;
};
```

### Redux Pattern
```javascript
// Redux slice
const counterSlice = createSlice({
  name: 'counter',
  initialState: { value: 0 },
  reducers: {
    increment: (state) => { state.value += 1; },
    decrement: (state) => { state.value -= 1; },
  },
});

// Store configuration
const store = configureStore({
  reducer: {
    counter: counterSlice.reducer,
  },
});

// Component usage
const Counter = () => {
  const count = useSelector(state => state.counter.value);
  const dispatch = useDispatch();
  
  return (
    <div>
      <span>{count}</span>
      <button onClick={() => dispatch(increment())}>+</button>
      <button onClick={() => dispatch(decrement())}>-</button>
    </div>
  );
};
```

---

## Micro-Frontends

### Module Federation
```javascript
// Webpack Module Federation
const ModuleFederationPlugin = require('@module-federation/webpack');

module.exports = {
  plugins: [
    new ModuleFederationPlugin({
      name: 'shell',
      remotes: {
        dashboard: 'dashboard@http://localhost:3001/remoteEntry.js',
        profile: 'profile@http://localhost:3002/remoteEntry.js'
      },
      shared: {
        react: { singleton: true },
        'react-dom': { singleton: true }
      }
    })
  ]
};

// Dynamic loading
const MicroFrontend = ({ name, host }) => {
  useEffect(() => {
    const script = document.createElement('script');
    script.src = `${host}/remoteEntry.js`;
    script.onload = () => {
      window[name].mount(document.getElementById(`${name}-container`));
    };
    document.head.appendChild(script);
  }, [name, host]);
  
  return <div id={`${name}-container`} />;
};
```

### Communication
```javascript
// Event-based communication
const EventBus = {
  events: {},
  on(event, callback) {
    if (!this.events[event]) this.events[event] = [];
    this.events[event].push(callback);
  },
  emit(event, data) {
    if (this.events[event]) {
      this.events[event].forEach(callback => callback(data));
    }
  }
};

// Shared state
const SharedState = {
  state: {},
  listeners: [],
  setState(newState) {
    this.state = { ...this.state, ...newState };
    this.listeners.forEach(listener => listener(this.state));
  },
  subscribe(listener) {
    this.listeners.push(listener);
    return () => {
      this.listeners = this.listeners.filter(l => l !== listener);
    };
  }
};
```

---

## Cross-Platform Development

### Responsive Design
```javascript
// Mobile-first approach
const ResponsiveComponent = () => {
  const [isMobile, setIsMobile] = useState(false);
  
  useEffect(() => {
    const checkScreenSize = () => {
      setIsMobile(window.innerWidth < 768);
    };
    
    checkScreenSize();
    window.addEventListener('resize', checkScreenSize);
    return () => window.removeEventListener('resize', checkScreenSize);
  }, []);
  
  return (
    <div className={isMobile ? 'mobile-layout' : 'desktop-layout'}>
      <Content />
    </div>
  );
};

// CSS Grid responsive
const responsiveStyles = `
  .grid {
    display: grid;
    grid-template-columns: 1fr;
    gap: 1rem;
  }
  
  @media (min-width: 768px) {
    .grid {
      grid-template-columns: repeat(2, 1fr);
    }
  }
  
  @media (min-width: 1024px) {
    .grid {
      grid-template-columns: repeat(3, 1fr);
    }
  }
`;
```

### PWA Features
```javascript
// Service Worker registration
if ('serviceWorker' in navigator) {
  navigator.serviceWorker.register('/sw.js')
    .then(registration => console.log('SW registered'))
    .catch(error => console.log('SW registration failed'));
}

// Install prompt
const InstallPrompt = () => {
  const [deferredPrompt, setDeferredPrompt] = useState(null);
  
  useEffect(() => {
    window.addEventListener('beforeinstallprompt', (e) => {
      e.preventDefault();
      setDeferredPrompt(e);
    });
  }, []);
  
  const handleInstall = async () => {
    if (deferredPrompt) {
      deferredPrompt.prompt();
      const { outcome } = await deferredPrompt.userChoice;
      console.log(`User response: ${outcome}`);
      setDeferredPrompt(null);
    }
  };
  
  return (
    <button onClick={handleInstall} disabled={!deferredPrompt}>
      Install App
    </button>
  );
};
```

---

## Accessibility & UX

### ARIA Implementation
```javascript
// Accessible modal
const AccessibleModal = ({ isOpen, onClose, title, children }) => (
  <div
    className={`modal ${isOpen ? 'open' : ''}`}
    role="dialog"
    aria-modal="true"
    aria-labelledby="modal-title"
    aria-hidden={!isOpen}
  >
    <div className="modal-content">
      <h2 id="modal-title">{title}</h2>
      <button
        onClick={onClose}
        aria-label="Close modal"
        className="close-button"
      >
        ×
      </button>
      {children}
    </div>
  </div>
);

// Keyboard navigation
const KeyboardNavigableList = ({ items, onSelect }) => {
  const [selectedIndex, setSelectedIndex] = useState(-1);
  
  const handleKeyDown = (e) => {
    switch (e.key) {
      case 'ArrowDown':
        e.preventDefault();
        setSelectedIndex(prev => Math.min(prev + 1, items.length - 1));
        break;
      case 'ArrowUp':
        e.preventDefault();
        setSelectedIndex(prev => Math.max(prev - 1, 0));
        break;
      case 'Enter':
        if (selectedIndex >= 0) {
          onSelect(items[selectedIndex]);
        }
        break;
    }
  };
  
  return (
    <ul onKeyDown={handleKeyDown} tabIndex={0}>
      {items.map((item, index) => (
        <li
          key={item.id}
          className={index === selectedIndex ? 'selected' : ''}
          onClick={() => onSelect(item)}
        >
          {item.title}
        </li>
      ))}
    </ul>
  );
};
```

### Focus Management
```javascript
// Focus trap hook
const useFocusTrap = (isActive) => {
  const containerRef = useRef();
  
  useEffect(() => {
    if (!isActive || !containerRef.current) return;
    
    const focusableElements = containerRef.current.querySelectorAll(
      'button, [href], input, select, textarea, [tabindex]:not([tabindex="-1"])'
    );
    
    const firstElement = focusableElements[0];
    const lastElement = focusableElements[focusableElements.length - 1];
    
    const handleTabKey = (e) => {
      if (e.key === 'Tab') {
        if (e.shiftKey) {
          if (document.activeElement === firstElement) {
            e.preventDefault();
            lastElement?.focus();
          }
        } else {
          if (document.activeElement === lastElement) {
            e.preventDefault();
            firstElement?.focus();
          }
        }
      }
    };
    
    document.addEventListener('keydown', handleTabKey);
    firstElement?.focus();
    
    return () => document.removeEventListener('keydown', handleTabKey);
  }, [isActive]);
  
  return containerRef;
};
```

---

## Browser Internals

### Critical Rendering Path
```javascript
// Performance optimization
const optimizeCriticalPath = {
  // Inline critical CSS
  criticalCSS: `
    .hero { display: flex; flex-direction: column; }
    .hero h1 { font-size: 2rem; color: #333; }
  `,
  
  // Preload important resources
  preloadResources: () => {
    const link = document.createElement('link');
    link.rel = 'preload';
    link.href = '/hero-image.jpg';
    link.as = 'image';
    document.head.appendChild(link);
  },
  
  // Defer non-critical JavaScript
  deferJS: () => {
    const script = document.createElement('script');
    script.src = 'non-critical.js';
    script.defer = true;
    document.head.appendChild(script);
  }
};
```

### Event Loop
```javascript
// Event loop demonstration
const eventLoopDemo = () => {
  console.log('1. Synchronous code');
  
  setTimeout(() => console.log('2. setTimeout'), 0);
  Promise.resolve().then(() => console.log('3. Promise'));
  setTimeout(() => console.log('4. setTimeout'), 0);
  Promise.resolve().then(() => console.log('5. Promise'));
  
  console.log('6. Synchronous code');
  // Output: 1, 6, 3, 5, 2, 4
};

// Debouncing and throttling
const debounce = (func, delay) => {
  let timeoutId;
  return (...args) => {
    clearTimeout(timeoutId);
    timeoutId = setTimeout(() => func.apply(null, args), delay);
  };
};

const throttle = (func, delay) => {
  let lastCall = 0;
  return (...args) => {
    const now = Date.now();
    if (now - lastCall >= delay) {
      lastCall = now;
      func.apply(null, args);
    }
  };
};
```

---

## Real-World Scenarios

### News Feed with Infinite Scroll
```javascript
const NewsFeed = () => {
  const [posts, setPosts] = useState([]);
  const [loading, setLoading] = useState(false);
  const [hasMore, setHasMore] = useState(true);
  
  const loadMorePosts = useCallback(async () => {
    if (loading || !hasMore) return;
    setLoading(true);
    const newPosts = await fetchPosts(posts.length);
    setPosts(prev => [...prev, ...newPosts]);
    setHasMore(newPosts.length > 0);
    setLoading(false);
  }, [posts.length, loading, hasMore]);
  
  return (
    <VirtualizedList
      items={posts}
      onLoadMore={loadMorePosts}
      renderItem={({ item }) => <PostCard post={item} />}
    />
  );
};
```

### Real-time Chat
```javascript
const ChatInterface = () => {
  const [messages, setMessages] = useState([]);
  const [ws, setWs] = useState(null);
  
  useEffect(() => {
    const websocket = new WebSocket('ws://localhost:8080/chat');
    
    websocket.onmessage = (event) => {
      const data = JSON.parse(event.data);
      setMessages(prev => [...prev, data.message]);
    };
    
    setWs(websocket);
    return () => websocket.close();
  }, []);
  
  const sendMessage = (text) => {
    if (ws) {
      ws.send(JSON.stringify({ type: 'message', text }));
    }
  };
  
  return (
    <div className="chat">
      <MessageList messages={messages} />
      <MessageInput onSend={sendMessage} />
    </div>
  );
};
```

### E-commerce Cart
```javascript
const ShoppingCart = () => {
  const [cart, setCart] = useState([]);
  const [isOnline, setIsOnline] = useState(navigator.onLine);
  
  useEffect(() => {
    const savedCart = localStorage.getItem('cart');
    if (savedCart) {
      setCart(JSON.parse(savedCart));
    }
  }, []);
  
  const addToCart = (product) => {
    const newCart = [...cart, product];
    setCart(newCart);
    localStorage.setItem('cart', JSON.stringify(newCart));
  };
  
  const checkout = async () => {
    try {
      const order = await createOrder(cart);
      setCart([]);
      localStorage.removeItem('cart');
    } catch (error) {
      if (!isOnline) {
        showOfflineMessage();
      }
    }
  };
  
  return (
    <div className="cart">
      <CartItems items={cart} />
      <CheckoutButton onClick={checkout} />
    </div>
  );
};
```

---

## Common Patterns

### Error Boundaries
```javascript
class ErrorBoundary extends React.Component {
  constructor(props) {
    super(props);
    this.state = { hasError: false };
  }
  
  static getDerivedStateFromError(error) {
    return { hasError: true };
  }
  
  componentDidCatch(error, errorInfo) {
    console.error('Error caught by boundary:', error, errorInfo);
  }
  
  render() {
    if (this.state.hasError) {
      return <h1>Something went wrong.</h1>;
    }
    
    return this.props.children;
  }
}
```

### Custom Hooks
```javascript
// useLocalStorage hook
const useLocalStorage = (key, initialValue) => {
  const [storedValue, setStoredValue] = useState(() => {
    try {
      const item = window.localStorage.getItem(key);
      return item ? JSON.parse(item) : initialValue;
    } catch (error) {
      return initialValue;
    }
  });
  
  const setValue = (value) => {
    try {
      setStoredValue(value);
      window.localStorage.setItem(key, JSON.stringify(value));
    } catch (error) {
      console.error(error);
    }
  };
  
  return [storedValue, setValue];
};

// useDebounce hook
const useDebounce = (value, delay) => {
  const [debouncedValue, setDebouncedValue] = useState(value);
  
  useEffect(() => {
    const handler = setTimeout(() => {
      setDebouncedValue(value);
    }, delay);
    
    return () => {
      clearTimeout(handler);
    };
  }, [value, delay]);
  
  return debouncedValue;
};
```

### Performance Monitoring
```javascript
// Performance observer
const PerformanceMonitor = () => {
  useEffect(() => {
    const observer = new PerformanceObserver((list) => {
      list.getEntries().forEach((entry) => {
        if (entry.entryType === 'longtask') {
          console.warn('Long task detected:', entry.duration);
        }
      });
    });
    
    observer.observe({ entryTypes: ['longtask'] });
    
    return () => observer.disconnect();
  }, []);
  
  return null;
};

// Memory monitoring
const MemoryMonitor = () => {
  useEffect(() => {
    const interval = setInterval(() => {
      if (performance.memory) {
        const memory = performance.memory;
        console.log('Memory usage:', {
          used: Math.round(memory.usedJSHeapSize / 1024 / 1024) + ' MB',
          total: Math.round(memory.totalJSHeapSize / 1024 / 1024) + ' MB'
        });
      }
    }, 5000);
    
    return () => clearInterval(interval);
  }, []);
  
  return null;
};
```

---

## 🎯 Quick Tips

- **Think in systems** - Consider scalability, performance, and maintainability
- **Draw diagrams** - Visualize architecture and data flow
- **Consider trade-offs** - Every decision has pros and cons
- **Focus on user experience** - Performance and accessibility matter
- **Stay current** - Keep up with modern front-end trends
- **Test thoroughly** - Use automated and manual testing
- **Monitor performance** - Use real user monitoring
- **Plan for scale** - Design for growth from the start
- **Document decisions** - Explain architectural choices
- **Iterate and improve** - Continuously optimize and refactor

---

## 📚 Key Technologies

| Category | Technology | Use Case |
|----------|------------|----------|
| **Frameworks** | React, Vue, Angular | UI development |
| **State Management** | Redux, Zustand, Context API | Global state |
| **Routing** | React Router, Vue Router | Client-side routing |
| **Styling** | CSS-in-JS, Tailwind, Styled Components | Component styling |
| **Testing** | Jest, React Testing Library, Cypress | Testing |
| **Build Tools** | Webpack, Vite, Parcel | Bundling |
| **Performance** | Lighthouse, Web Vitals, Bundle Analyzer | Optimization |
| **Accessibility** | axe, WAVE, Screen Readers | A11y testing |
| **PWA** | Service Workers, Web App Manifest | Offline functionality |
| **Micro-Frontends** | Module Federation, Single-SPA | Architecture |

---

*This cheatsheet covers the most important concepts for front-end system design interviews. Practice implementing these patterns and understand the underlying principles!*
