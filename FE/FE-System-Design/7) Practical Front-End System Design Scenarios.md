# 7) Practical Front-End System Design Scenarios (Q65–84)

---

## 65) How would you design a news feed UI (e.g., Instagram or Twitter) with infinite scroll and real-time updates?

A news feed requires efficient data management, virtual scrolling for performance, real-time updates via WebSockets, and proper state synchronization across components.

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

- **Core Technique**: Use virtual scrolling to handle thousands of posts efficiently
- **Real-World Use**: Implement optimistic updates for better user experience
- **Common Practice**: Use WebSocket connections for real-time updates
- **Advanced Feature**: Cache posts locally and implement offline support
- **Interview Tip**: Explain that consider pagination strategies and data freshness

---

## 66) How would you design an autocomplete / type-ahead search component?

Autocomplete requires debounced input handling, efficient search algorithms, caching of results, and proper keyboard navigation for accessibility.

```javascript
const Autocomplete = ({ onSelect, searchFn }) => {
  const [query, setQuery] = useState('');
  const [results, setResults] = useState([]);
  const [selectedIndex, setSelectedIndex] = useState(-1);
  
  const debouncedSearch = useCallback(
    debounce(async (searchQuery) => {
      if (searchQuery.length > 2) {
        const searchResults = await searchFn(searchQuery);
        setResults(searchResults);
      }
    }, 300),
    [searchFn]
  );
  
  return (
    <div className="autocomplete">
      <input
        value={query}
        onChange={(e) => {
          setQuery(e.target.value);
          debouncedSearch(e.target.value);
        }}
        onKeyDown={handleKeyDown}
      />
      {results.length > 0 && (
        <ul className="results">
          {results.map((result, index) => (
            <li
              key={result.id}
              className={index === selectedIndex ? 'selected' : ''}
              onClick={() => handleSelect(result)}
            >
              {result.title}
            </li>
          ))}
        </ul>
      )}
    </div>
  );
};
```

- **Core Requirement**: Implement debouncing to avoid excessive API calls
- **Real-World Use**: Use keyboard navigation for accessibility
- **Common Practice**: Cache search results to improve performance
- **Advanced Feature**: Handle loading states and error scenarios
- **Interview Tip**: Explain that consider fuzzy matching and search suggestions

---

## 67) How would you design a large data table with sorting, filtering, pagination, and virtualization?

Large data tables require virtualization for performance, efficient sorting algorithms, client-side filtering, and proper state management for complex interactions.

```javascript
const DataTable = ({ data, columns }) => {
  const [sortConfig, setSortConfig] = useState({ key: null, direction: 'asc' });
  const [filters, setFilters] = useState({});
  const [currentPage, setCurrentPage] = useState(1);
  
  const filteredData = useMemo(() => {
    return data.filter(row => 
      Object.entries(filters).every(([key, value]) => 
        row[key].toLowerCase().includes(value.toLowerCase())
      )
    );
  }, [data, filters]);
  
  const sortedData = useMemo(() => {
    if (!sortConfig.key) return filteredData;
    return [...filteredData].sort((a, b) => {
      const aVal = a[sortConfig.key];
      const bVal = b[sortConfig.key];
      return sortConfig.direction === 'asc' ? 
        aVal.localeCompare(bVal) : bVal.localeCompare(aVal);
    });
  }, [filteredData, sortConfig]);
  
  return (
    <VirtualizedTable
      data={sortedData}
      columns={columns}
      onSort={setSortConfig}
      onFilter={setFilters}
      pagination={{ currentPage, setCurrentPage }}
    />
  );
};
```

- **Core Technique**: Use virtualization to handle large datasets efficiently
- **Real-World Use**: Implement client-side sorting and filtering for better performance
- **Common Practice**: Provide clear visual feedback for sort and filter states
- **Advanced Feature**: Consider server-side pagination for very large datasets
- **Interview Tip**: Explain that ensure accessibility with proper ARIA attributes

---

## 68) How would you design a real-time chat interface (presence, offline caching, delivery states)?

Real-time chat requires WebSocket connections, message queuing, offline storage, delivery status tracking, and proper state synchronization.

```javascript
const ChatInterface = () => {
  const [messages, setMessages] = useState([]);
  const [onlineUsers, setOnlineUsers] = useState([]);
  const [typingUsers, setTypingUsers] = useState([]);
  
  useEffect(() => {
    const ws = new WebSocket('ws://localhost:8080/chat');
    ws.onmessage = (event) => {
      const data = JSON.parse(event.data);
      switch (data.type) {
        case 'message':
          setMessages(prev => [...prev, { ...data.message, status: 'delivered' }]);
          break;
        case 'typing':
          setTypingUsers(data.users);
          break;
        case 'presence':
          setOnlineUsers(data.users);
          break;
      }
    };
    return () => ws.close();
  }, []);
  
  const sendMessage = async (text) => {
    const message = { id: Date.now(), text, status: 'sending' };
    setMessages(prev => [...prev, message]);
    try {
      await sendMessageToServer(message);
      setMessages(prev => prev.map(m => 
        m.id === message.id ? { ...m, status: 'delivered' } : m
      ));
    } catch (error) {
      setMessages(prev => prev.map(m => 
        m.id === message.id ? { ...m, status: 'failed' } : m
      ));
    }
  };
  
  return (
    <div className="chat">
      <UserList users={onlineUsers} />
      <MessageList messages={messages} />
      <TypingIndicator users={typingUsers} />
      <MessageInput onSend={sendMessage} />
    </div>
  );
};
```

- **Core Approach**: Implement WebSocket connections for real-time communication
- **Real-World Use**: Use optimistic updates for better user experience
- **Common Practice**: Store messages locally for offline access
- **Advanced Feature**: Handle connection failures and reconnection logic
- **Interview Tip**: Explain that implement proper message delivery status tracking

---

## 69) How would you design a media-rich gallery for images and videos with lazy loading and responsive layouts?

Media galleries require lazy loading, responsive image sizing, progressive loading, and efficient memory management for large collections.

```javascript
const MediaGallery = ({ media }) => {
  const [visibleItems, setVisibleItems] = useState(new Set());
  const observerRef = useRef();
  
  useEffect(() => {
    const observer = new IntersectionObserver(
      (entries) => {
        entries.forEach(entry => {
          if (entry.isIntersecting) {
            setVisibleItems(prev => new Set([...prev, entry.target.dataset.id]));
          }
        });
      },
      { threshold: 0.1 }
    );
    observerRef.current = observer;
    return () => observer.disconnect();
  }, []);
  
  return (
    <div className="gallery">
      {media.map((item, index) => (
        <div
          key={item.id}
          ref={(el) => {
            if (el) observerRef.current?.observe(el);
          }}
          data-id={item.id}
          className="gallery-item"
        >
          {visibleItems.has(item.id) ? (
            <MediaItem item={item} />
          ) : (
            <div className="placeholder" style={{ aspectRatio: item.aspectRatio }} />
          )}
        </div>
      ))}
    </div>
  );
};
```

- **Core Technique**: Use Intersection Observer for efficient lazy loading
- **Real-World Use**: Implement responsive image sizing with srcset
- **Common Practice**: Consider progressive loading for better perceived performance
- **Advanced Feature**: Use virtual scrolling for very large galleries
- **Interview Tip**: Explain that implement proper error handling and fallbacks

---

## 70) How would you design an e-commerce shopping cart & checkout UI that works offline and across devices?

Shopping cart requires offline storage, cross-device synchronization, optimistic updates, and proper state management for complex business logic.

```javascript
const ShoppingCart = () => {
  const [cart, setCart] = useState([]);
  const [isOnline, setIsOnline] = useState(navigator.onLine);
  
  useEffect(() => {
    const savedCart = localStorage.getItem('cart');
    if (savedCart) {
      setCart(JSON.parse(savedCart));
    }
    if (isOnline) {
      syncCartWithServer();
    }
  }, [isOnline]);
  
  const addToCart = (product) => {
    const newCart = [...cart, { ...product, id: Date.now() }];
    setCart(newCart);
    localStorage.setItem('cart', JSON.stringify(newCart));
    if (isOnline) {
      syncCartWithServer();
    }
  };
  
  const checkout = async () => {
    try {
      const order = await createOrder(cart);
      setCart([]);
      localStorage.removeItem('cart');
      navigate(`/confirmation/${order.id}`);
    } catch (error) {
      if (!isOnline) {
        showOfflineMessage();
      }
    }
  };
  
  return (
    <div className="cart">
      <CartItems items={cart} onUpdate={setCart} />
      <CartSummary total={calculateTotal(cart)} />
      <CheckoutButton onClick={checkout} disabled={cart.length === 0} />
    </div>
  );
};
```

- **Core Strategy**: Use localStorage for offline cart persistence
- **Real-World Use**: Implement cross-device synchronization via user accounts
- **Common Practice**: Handle offline scenarios gracefully with proper messaging
- **Advanced Feature**: Use optimistic updates for better user experience
- **Interview Tip**: Explain that consider inventory management and stock validation

---

## 71) How would you design a collaborative editor (e.g., Google Docs) from the front-end side?

Collaborative editing requires real-time synchronization, conflict resolution, operational transforms, and proper cursor/selection management.

```javascript
const CollaborativeEditor = () => {
  const [content, setContent] = useState('');
  const [cursors, setCursors] = useState({});
  const [isConnected, setIsConnected] = useState(false);
  
  useEffect(() => {
    const ws = new WebSocket('ws://localhost:8080/editor');
    ws.onmessage = (event) => {
      const data = JSON.parse(event.data);
      switch (data.type) {
        case 'content':
          setContent(data.content);
          break;
        case 'cursor':
          setCursors(prev => ({ ...prev, [data.userId]: data.position }));
          break;
        case 'operation':
          applyOperation(data.operation);
          break;
      }
    };
    return () => ws.close();
  }, []);
  
  const handleContentChange = (newContent) => {
    const operation = createOperation(content, newContent);
    setContent(newContent);
    if (isConnected) {
      ws.send(JSON.stringify({ type: 'operation', operation }));
    }
  };
  
  return (
    <div className="editor">
      <RichTextEditor
        value={content}
        onChange={handleContentChange}
        cursors={cursors}
      />
    </div>
  );
};
```

- **Core Technique**: Implement operational transforms for conflict resolution
- **Real-World Use**: Use WebSocket connections for real-time synchronization
- **Common Practice**: Handle cursor and selection management across users
- **Advanced Feature**: Implement proper undo/redo functionality
- **Interview Tip**: Explain that consider performance optimization for large documents

---

## 72) How would you design a map or geo-based UI (e.g., Uber-style tracking)?

Map-based UIs require efficient rendering of large datasets, real-time location updates, smooth animations, and proper handling of map interactions.

```javascript
const MapInterface = () => {
  const [map, setMap] = useState(null);
  const [userLocation, setUserLocation] = useState(null);
  const [markers, setMarkers] = useState([]);
  
  useEffect(() => {
    const mapInstance = new Map('map-container', {
      center: [0, 0],
      zoom: 10
    });
    setMap(mapInstance);
    
    navigator.geolocation.getCurrentPosition((position) => {
      const { latitude, longitude } = position.coords;
      setUserLocation({ lat: latitude, lng: longitude });
      mapInstance.setCenter([longitude, latitude]);
    });
  }, []);
  
  const trackUser = () => {
    const watchId = navigator.geolocation.watchPosition((position) => {
      const { latitude, longitude } = position.coords;
      setUserLocation({ lat: latitude, lng: longitude });
      map.setCenter([longitude, latitude]);
    });
    return () => navigator.geolocation.clearWatch(watchId);
  };
  
  return (
    <div className="map-container">
      <div id="map-container" style={{ width: '100%', height: '400px' }} />
      <button onClick={trackUser}>Track Location</button>
    </div>
  );
};
```

- **Core Technique**: Use efficient clustering for large numbers of markers
- **Real-World Use**: Implement smooth animations for location updates
- **Common Practice**: Consider offline map functionality
- **Advanced Feature**: Handle different map providers and APIs
- **Interview Tip**: Explain that optimize rendering performance for mobile devices

---

## 73) How would you design a Progressive Web App (PWA) with offline mode, push notifications, and installability?

PWAs require service workers for offline functionality, web app manifests for installability, push notification APIs, and proper caching strategies.

```javascript
const PWAApp = () => {
  const [isOnline, setIsOnline] = useState(navigator.onLine);
  const [deferredPrompt, setDeferredPrompt] = useState(null);
  
  useEffect(() => {
    const handleOnline = () => setIsOnline(true);
    const handleOffline = () => setIsOnline(false);
    window.addEventListener('online', handleOnline);
    window.addEventListener('offline', handleOffline);
    
    window.addEventListener('beforeinstallprompt', (e) => {
      e.preventDefault();
      setDeferredPrompt(e);
    });
    
    return () => {
      window.removeEventListener('online', handleOnline);
      window.removeEventListener('offline', handleOffline);
    };
  }, []);
  
  const handleInstall = async () => {
    if (deferredPrompt) {
      deferredPrompt.prompt();
      const { outcome } = await deferredPrompt.userChoice;
      setDeferredPrompt(null);
    }
  };
  
  return (
    <div className="pwa-app">
      {!isOnline && <div className="offline-indicator">Offline</div>}
      {deferredPrompt && (
        <button onClick={handleInstall}>Install App</button>
      )}
      <Content />
    </div>
  );
};
```

- **Core Features**: Implement service workers for offline functionality
- **Real-World Use**: Use web app manifest for installability
- **Common Practice**: Handle push notifications with proper permissions
- **Advanced Feature**: Implement proper caching strategies
- **Interview Tip**: Explain that test across different browsers and devices

---

## 74) How would you design a dashboard UI with real-time charts and metrics for multiple users?

Real-time dashboards require efficient data visualization, WebSocket connections for live updates, responsive layouts, and proper state management for complex metrics.

```javascript
const Dashboard = () => {
  const [metrics, setMetrics] = useState({});
  const [charts, setCharts] = useState([]);
  const [isConnected, setIsConnected] = useState(false);
  
  useEffect(() => {
    const ws = new WebSocket('ws://localhost:8080/dashboard');
    ws.onmessage = (event) => {
      const data = JSON.parse(event.data);
      setMetrics(prev => ({ ...prev, ...data.metrics }));
      setCharts(prev => prev.map(chart => 
        chart.id === data.chartId ? { ...chart, data: data.chartData } : chart
      ));
    };
    ws.onopen = () => setIsConnected(true);
    ws.onclose = () => setIsConnected(false);
    return () => ws.close();
  }, []);
  
  return (
    <div className="dashboard">
      <div className={`status ${isConnected ? 'connected' : 'disconnected'}`}>
        {isConnected ? 'Live' : 'Offline'}
      </div>
      <div className="metrics-grid">
        {Object.entries(metrics).map(([key, value]) => (
          <MetricCard key={key} title={key} value={value} />
        ))}
      </div>
      <div className="charts-container">
        {charts.map(chart => (
          <Chart key={chart.id} data={chart.data} type={chart.type} />
        ))}
      </div>
    </div>
  );
};
```

- **Core Approach**: Use efficient charting libraries for real-time updates
- **Real-World Use**: Implement proper data aggregation and sampling
- **Common Practice**: Handle connection failures and reconnection logic
- **Advanced Feature**: Consider performance optimization for large datasets
- **Interview Tip**: Explain that implement proper error handling and fallbacks

---

## 75) How would you design a front-end that dynamically loads micro-frontends, handles versioning, and supports independent deployment?

Dynamic micro-frontend loading requires proper module federation, version management, fallback strategies, and independent deployment coordination.

```javascript
const MicroFrontendLoader = ({ name, version, fallback }) => {
  const [Component, setComponent] = useState(null);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState(null);
  
  useEffect(() => {
    const loadMicroFrontend = async () => {
      try {
        const module = await System.import(`${name}@${version}/remoteEntry.js`);
        setComponent(() => module.default);
      } catch (err) {
        if (fallback) {
          const fallbackModule = await System.import(`${name}@${fallback}/remoteEntry.js`);
          setComponent(() => fallbackModule.default);
        } else {
          setError(err);
        }
      } finally {
        setLoading(false);
      }
    };
    loadMicroFrontend();
  }, [name, version, fallback]);
  
  if (loading) return <div>Loading {name}...</div>;
  if (error) return <div>Error loading {name}</div>;
  if (!Component) return <div>Component not found</div>;
  
  return <Component />;
};
```

- **Core Strategy**: Implement proper version management and fallback strategies
- **Real-World Use**: Use module federation for dynamic loading
- **Common Practice**: Handle independent deployment and version conflicts
- **Advanced Feature**: Implement proper error boundaries and fallbacks
- **Interview Tip**: Explain that consider performance implications of dynamic loading

---

## 76) How would you design a high-performance image carousel for web and mobile with memory optimization?

High-performance image carousels require lazy loading, memory management, smooth animations, and responsive design for optimal user experience.

```javascript
const ImageCarousel = ({ images }) => {
  const [currentIndex, setCurrentIndex] = useState(0);
  const [loadedImages, setLoadedImages] = useState(new Set());
  const [visibleRange, setVisibleRange] = useState({ start: 0, end: 2 });
  
  const loadImage = useCallback((index) => {
    if (!loadedImages.has(index)) {
      const img = new Image();
      img.src = images[index].src;
      img.onload = () => {
        setLoadedImages(prev => new Set([...prev, index]));
      };
    }
  }, [images, loadedImages]);
  
  const updateVisibleRange = useCallback((index) => {
    const start = Math.max(0, index - 1);
    const end = Math.min(images.length - 1, index + 1);
    setVisibleRange({ start, end });
    for (let i = start; i <= end; i++) {
      loadImage(i);
    }
  }, [images.length, loadImage]);
  
  useEffect(() => {
    updateVisibleRange(currentIndex);
  }, [currentIndex, updateVisibleRange]);
  
  return (
    <div className="carousel">
      {images.map((image, index) => (
        <div
          key={index}
          className={`carousel-item ${index === currentIndex ? 'active' : ''}`}
          style={{ transform: `translateX(${(index - currentIndex) * 100}%)` }}
        >
          {loadedImages.has(index) ? (
            <img src={image.src} alt={image.alt} />
          ) : (
            <div className="placeholder" />
          )}
        </div>
      ))}
    </div>
  );
};
```

- **Core Technique**: Implement lazy loading for memory efficiency
- **Real-World Use**: Use CSS transforms for smooth animations
- **Common Practice**: Manage visible range to optimize performance
- **Advanced Feature**: Implement proper image preloading strategies
- **Interview Tip**: Explain that consider responsive design and touch gestures

---

## 77) How would you design accessible UI components (screen readers, keyboard navigation, color modes)?

Accessible UI components require proper ARIA attributes, keyboard navigation support, color contrast compliance, and screen reader compatibility.

```javascript
const AccessibleButton = ({ children, onClick, disabled, ...props }) => {
  const [isPressed, setIsPressed] = useState(false);
  
  const handleKeyDown = (e) => {
    if (e.key === 'Enter' || e.key === ' ') {
      e.preventDefault();
      if (!disabled) {
        setIsPressed(true);
        onClick();
      }
    }
  };
  
  const handleKeyUp = (e) => {
    if (e.key === 'Enter' || e.key === ' ') {
      setIsPressed(false);
    }
  };
  
  return (
    <button
      onClick={onClick}
      onKeyDown={handleKeyDown}
      onKeyUp={handleKeyUp}
      disabled={disabled}
      aria-pressed={isPressed}
      aria-disabled={disabled}
      className={`accessible-button ${isPressed ? 'pressed' : ''} ${disabled ? 'disabled' : ''}`}
      {...props}
    >
      {children}
    </button>
  );
};
```

- **Core Requirement**: Implement proper ARIA attributes and roles
- **Real-World Use**: Support keyboard navigation and focus management
- **Common Practice**: Ensure color contrast meets WCAG standards
- **Advanced Feature**: Test with screen readers and assistive technologies
- **Interview Tip**: Explain that provide multiple ways to convey information

---

## 78) How would you design a global theme switcher (dark/light modes) that persists across sessions?

Global theme switching requires centralized theme management, persistent storage, smooth transitions, and proper CSS variable handling.

```javascript
const ThemeProvider = ({ children }) => {
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
```

- **Core Technique**: Use CSS custom properties for theme values
- **Real-World Use**: Implement smooth transitions between themes
- **Common Practice**: Persist theme preferences across sessions
- **Advanced Feature**: Consider system theme detection
- **Interview Tip**: Explain that test with different color schemes and contrast ratios

---

## 79) How would you design routing architecture for a SPA with SEO support and fast transitions?

SPA routing requires client-side navigation, SEO optimization, fast transitions, and proper state management for complex applications.

```javascript
const AppRouter = () => {
  const [currentRoute, setCurrentRoute] = useState(window.location.pathname);
  const [isLoading, setIsLoading] = useState(false);
  
  useEffect(() => {
    const handleRouteChange = (path) => {
      setIsLoading(true);
      setCurrentRoute(path);
      window.history.pushState({}, '', path);
      import(`./pages${path}`).then(() => {
        setIsLoading(false);
      });
    };
    
    window.addEventListener('popstate', () => {
      setCurrentRoute(window.location.pathname);
    });
    
    return () => {
      window.removeEventListener('popstate', handleRouteChange);
    };
  }, []);
  
  const RouteComponent = lazy(() => import(`./pages${currentRoute}`));
  
  return (
    <div className="app">
      <Navigation onRouteChange={setCurrentRoute} />
      <Suspense fallback={<div>Loading...</div>}>
        {isLoading ? <div>Loading...</div> : <RouteComponent />}
      </Suspense>
    </div>
  );
};
```

- **Core Approach**: Implement client-side routing with proper history management
- **Real-World Use**: Use code splitting for better performance
- **Common Practice**: Consider SEO implications and meta tag management
- **Advanced Feature**: Implement proper loading states and error handling
- **Interview Tip**: Explain that test navigation across different browsers and devices

---

## 80) How would you design a file upload system with progress tracking, resumable uploads, and mobile fallback?

File upload systems require progress tracking, chunked uploads for resumability, mobile optimization, and proper error handling for various scenarios.

```javascript
const FileUpload = () => {
  const [files, setFiles] = useState([]);
  const [uploadProgress, setUploadProgress] = useState({});
  
  const uploadFile = async (file) => {
    const chunkSize = 1024 * 1024; // 1MB chunks
    const totalChunks = Math.ceil(file.size / chunkSize);
    
    for (let i = 0; i < totalChunks; i++) {
      const start = i * chunkSize;
      const end = Math.min(start + chunkSize, file.size);
      const chunk = file.slice(start, end);
      
      try {
        await uploadChunk(file.name, i, chunk, totalChunks);
        setUploadProgress(prev => ({
          ...prev,
          [file.name]: ((i + 1) / totalChunks) * 100
        }));
      } catch (error) {
        console.error('Upload failed:', error);
        break;
      }
    }
  };
  
  return (
    <div className="file-upload">
      <input
        type="file"
        multiple
        onChange={(e) => {
          const selectedFiles = Array.from(e.target.files);
          setFiles(prev => [...prev, ...selectedFiles]);
          selectedFiles.forEach(file => uploadFile(file));
        }}
      />
      {files.map(file => (
        <div key={file.name} className="upload-item">
          <span>{file.name}</span>
          <div className="progress-bar">
            <div 
              className="progress-fill"
              style={{ width: `${uploadProgress[file.name] || 0}%` }}
            />
          </div>
        </div>
      ))}
    </div>
  );
};
```

- **Core Technique**: Implement chunked uploads for large files
- **Real-World Use**: Use progress tracking for better user experience
- **Common Practice**: Handle network failures and resume functionality
- **Advanced Feature**: Optimize for mobile devices and touch interfaces
- **Interview Tip**: Explain that consider file validation and security measures

---

## 81) How would you design a feature flag / A/B testing framework for front-end experiments?

Feature flags require dynamic configuration, A/B testing capabilities, user segmentation, and proper analytics integration for data-driven decisions.

```javascript
const FeatureFlagProvider = ({ children }) => {
  const [flags, setFlags] = useState({});
  const [userSegment, setUserSegment] = useState(null);
  
  useEffect(() => {
    const loadFlags = async () => {
      const response = await fetch('/api/feature-flags');
      const data = await response.json();
      setFlags(data.flags);
      setUserSegment(data.userSegment);
    };
    loadFlags();
  }, []);
  
  const isFeatureEnabled = (flagName) => {
    const flag = flags[flagName];
    if (!flag) return false;
    if (flag.type === 'boolean') return flag.value;
    if (flag.type === 'percentage') {
      const hash = hashUserId(userSegment);
      return hash < flag.value;
    }
    if (flag.type === 'segment') {
      return flag.segments.includes(userSegment);
    }
    return false;
  };
  
  return (
    <FeatureFlagContext.Provider value={{ isFeatureEnabled, flags }}>
      {children}
    </FeatureFlagContext.Provider>
  );
};
```

- **Core Strategy**: Implement dynamic feature flag configuration
- **Real-World Use**: Use proper user segmentation for A/B testing
- **Common Practice**: Integrate with analytics for data collection
- **Advanced Feature**: Consider performance implications of feature flags
- **Interview Tip**: Explain that implement proper fallback strategies

---

## 82) How would you design a notification system (toast, in-app, segmented delivery, analytics)?

Notification systems require multiple delivery channels, user preferences, analytics tracking, and proper state management for complex notification flows.

```javascript
const NotificationSystem = () => {
  const [notifications, setNotifications] = useState([]);
  const [preferences, setPreferences] = useState({
    email: true,
    push: true,
    inApp: true
  });
  
  const showNotification = (notification) => {
    const id = Date.now();
    const newNotification = {
      id,
      ...notification,
      timestamp: new Date(),
      read: false
    };
    setNotifications(prev => [newNotification, ...prev]);
    
    if (preferences.push && notification.priority === 'high') {
      sendPushNotification(notification);
    }
    if (preferences.email && notification.type === 'email') {
      sendEmailNotification(notification);
    }
    trackNotificationSent(notification);
  };
  
  return (
    <div className="notification-system">
      <NotificationList 
        notifications={notifications}
        onMarkAsRead={(id) => {
          setNotifications(prev => 
            prev.map(notif => 
              notif.id === id ? { ...notif, read: true } : notif
            )
          );
        }}
      />
      <NotificationPreferences 
        preferences={preferences}
        onChange={setPreferences}
      />
    </div>
  );
};
```

- **Core Approach**: Implement multiple notification channels
- **Real-World Use**: Use user preferences for personalized delivery
- **Common Practice**: Track analytics for notification effectiveness
- **Advanced Feature**: Consider notification frequency and timing
- **Interview Tip**: Explain that implement proper notification management and cleanup

---

## 83) How would you design a search results UI with infinite scrolling, client-side caching, and filters?

Search results require efficient data management, client-side caching, infinite scrolling, and proper filter handling for optimal user experience.

```javascript
const SearchResults = () => {
  const [query, setQuery] = useState('');
  const [results, setResults] = useState([]);
  const [filters, setFilters] = useState({});
  const [hasMore, setHasMore] = useState(true);
  const [loading, setLoading] = useState(false);
  const searchCache = useRef(new Map());
  
  const performSearch = useCallback(async (searchQuery, searchFilters, page = 0) => {
    const cacheKey = `${searchQuery}-${JSON.stringify(searchFilters)}-${page}`;
    if (searchCache.current.has(cacheKey)) {
      return searchCache.current.get(cacheKey);
    }
    setLoading(true);
    try {
      const response = await fetch('/api/search', {
        method: 'POST',
        body: JSON.stringify({ query: searchQuery, filters: searchFilters, page })
      });
      const data = await response.json();
      searchCache.current.set(cacheKey, data);
      return data;
    } finally {
      setLoading(false);
    }
  }, []);
  
  const loadMore = useCallback(async () => {
    if (loading || !hasMore) return;
    const data = await performSearch(query, filters, Math.floor(results.length / 20));
    setResults(prev => [...prev, ...data.results]);
    setHasMore(data.hasMore);
  }, [query, filters, results.length, loading, hasMore, performSearch]);
  
  return (
    <div className="search-results">
      <SearchInput value={query} onChange={setQuery} />
      <FilterPanel filters={filters} onChange={setFilters} />
      <InfiniteScrollList
        items={results}
        onLoadMore={loadMore}
        hasMore={hasMore}
        loading={loading}
        renderItem={({ item }) => <SearchResultItem item={item} />}
      />
    </div>
  );
};
```

- **Core Technique**: Implement client-side caching for better performance
- **Real-World Use**: Use infinite scrolling for large result sets
- **Common Practice**: Handle filter combinations efficiently
- **Advanced Feature**: Consider search result ranking and relevance
- **Interview Tip**: Explain that implement proper loading states and error handling

---

## 84) How would you design a live streaming UI (video/audio, low latency, buffering indicators, streaming controls)?

Live streaming UIs require real-time video/audio handling, low-latency optimization, proper buffering management, and intuitive streaming controls.

```javascript
const LiveStreamingUI = () => {
  const [stream, setStream] = useState(null);
  const [isPlaying, setIsPlaying] = useState(false);
  const [buffering, setBuffering] = useState(false);
  const [quality, setQuality] = useState('auto');
  
  useEffect(() => {
    const video = document.getElementById('video-player');
    const handleLoadStart = () => setBuffering(true);
    const handleCanPlay = () => setBuffering(false);
    const handleWaiting = () => setBuffering(true);
    const handlePlaying = () => setBuffering(false);
    
    video.addEventListener('loadstart', handleLoadStart);
    video.addEventListener('canplay', handleCanPlay);
    video.addEventListener('waiting', handleWaiting);
    video.addEventListener('playing', handlePlaying);
    
    return () => {
      video.removeEventListener('loadstart', handleLoadStart);
      video.removeEventListener('canplay', handleCanPlay);
      video.removeEventListener('waiting', handleWaiting);
      video.removeEventListener('playing', handlePlaying);
    };
  }, []);
  
  const startStream = async () => {
    try {
      const mediaStream = await navigator.mediaDevices.getUserMedia({
        video: true,
        audio: true
      });
      setStream(mediaStream);
      const video = document.getElementById('video-player');
      video.srcObject = mediaStream;
      video.play();
      setIsPlaying(true);
    } catch (error) {
      console.error('Error starting stream:', error);
    }
  };
  
  return (
    <div className="live-streaming">
      <div className="video-container">
        <video
          id="video-player"
          controls
          muted
          autoPlay
          playsInline
        />
        {buffering && <div className="buffering-indicator">Buffering...</div>}
      </div>
      <div className="streaming-controls">
        <button onClick={isPlaying ? () => stopStream() : startStream}>
          {isPlaying ? 'Stop Stream' : 'Start Stream'}
        </button>
        <select value={quality} onChange={(e) => setQuality(e.target.value)}>
          <option value="auto">Auto</option>
          <option value="720p">720p</option>
          <option value="480p">480p</option>
        </select>
      </div>
    </div>
  );
};
```

- **Core Technique**: Implement low-latency streaming protocols
- **Real-World Use**: Use proper buffering management for smooth playback
- **Common Practice**: Handle different quality levels and adaptive streaming
- **Advanced Feature**: Consider mobile optimization and touch controls
- **Interview Tip**: Explain that implement proper error handling and reconnection logic

---
