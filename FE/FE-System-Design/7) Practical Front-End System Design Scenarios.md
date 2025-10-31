# 7) Practical Front-End System Design Scenarios (Q65–84)

## 65) How would you design a news feed UI (e.g., Instagram or Twitter) with infinite scroll and real-time updates?

Concept: A news feed requires efficient data management, virtual scrolling for performance, real-time updates via WebSockets, and proper state synchronization across components.

Example:
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

Deep Insight:
- Use virtual scrolling to handle thousands of posts efficiently
- Implement optimistic updates for better user experience
- Use WebSocket connections for real-time updates
- Cache posts locally and implement offline support
- Consider pagination strategies and data freshness

## 66) How would you design an autocomplete / type-ahead search component?

Concept: Autocomplete requires debounced input handling, efficient search algorithms, caching of results, and proper keyboard navigation for accessibility.

Example:
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

Deep Insight:
- Implement debouncing to avoid excessive API calls
- Use keyboard navigation for accessibility
- Cache search results to improve performance
- Handle loading states and error scenarios
- Consider fuzzy matching and search suggestions

## 67) How would you design a large data table with sorting, filtering, pagination, and virtualization?

Concept: Large data tables require virtualization for performance, efficient sorting algorithms, client-side filtering, and proper state management for complex interactions.

Example:
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

Deep Insight:
- Use virtualization to handle large datasets efficiently
- Implement client-side sorting and filtering for better performance
- Provide clear visual feedback for sort and filter states
- Consider server-side pagination for very large datasets
- Ensure accessibility with proper ARIA attributes

## 68) How would you design a real-time chat interface (presence, offline caching, delivery states)?

Concept: Real-time chat requires WebSocket connections, message queuing, offline storage, delivery status tracking, and proper state synchronization.

Example:
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

Deep Insight:
- Implement WebSocket connections for real-time communication
- Use optimistic updates for better user experience
- Store messages locally for offline access
- Handle connection failures and reconnection logic
- Implement proper message delivery status tracking

## 69) How would you design a media-rich gallery for images and videos with lazy loading and responsive layouts?

Concept: Media galleries require lazy loading, responsive image sizing, progressive loading, and efficient memory management for large collections.

Example:
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

Deep Insight:
- Use Intersection Observer for efficient lazy loading
- Implement responsive image sizing with srcset
- Consider progressive loading for better perceived performance
- Use virtual scrolling for very large galleries
- Implement proper error handling and fallbacks

## 70) How would you design an e-commerce shopping cart & checkout UI that works offline and across devices?

Concept: Shopping cart requires offline storage, cross-device synchronization, optimistic updates, and proper state management for complex business logic.

Example:
```javascript
const ShoppingCart = () => {
  const [cart, setCart] = useState([]);
  const [isOnline, setIsOnline] = useState(navigator.onLine);
  
  useEffect(() => {
    // Load cart from localStorage
    const savedCart = localStorage.getItem('cart');
    if (savedCart) {
      setCart(JSON.parse(savedCart));
    }
    
    // Sync with server when online
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
      // Handle offline scenario
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

Deep Insight:
- Use localStorage for offline cart persistence
- Implement cross-device synchronization via user accounts
- Handle offline scenarios gracefully with proper messaging
- Use optimistic updates for better user experience
- Consider inventory management and stock validation

## 71) How would you design a collaborative editor (e.g., Google Docs) from the front-end side?

Concept: Collaborative editing requires real-time synchronization, conflict resolution, operational transforms, and proper cursor/selection management.

Example:
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
      <div className="toolbar">
        <button onClick={() => applyFormat('bold')}>Bold</button>
        <button onClick={() => applyFormat('italic')}>Italic</button>
      </div>
      <div className="editor-content">
        <RichTextEditor
          value={content}
          onChange={handleContentChange}
          cursors={cursors}
        />
      </div>
    </div>
  );
};
```

Deep Insight:
- Implement operational transforms for conflict resolution
- Use WebSocket connections for real-time synchronization
- Handle cursor and selection management across users
- Implement proper undo/redo functionality
- Consider performance optimization for large documents

## 72) How would you design a map or geo-based UI (e.g., Uber-style tracking)?

Concept: Map-based UIs require efficient rendering of large datasets, real-time location updates, smooth animations, and proper handling of map interactions.

Example:
```javascript
const MapInterface = () => {
  const [map, setMap] = useState(null);
  const [userLocation, setUserLocation] = useState(null);
  const [markers, setMarkers] = useState([]);
  
  useEffect(() => {
    // Initialize map
    const mapInstance = new Map('map-container', {
      center: [0, 0],
      zoom: 10
    });
    setMap(mapInstance);
    
    // Get user location
    navigator.geolocation.getCurrentPosition((position) => {
      const { latitude, longitude } = position.coords;
      setUserLocation({ lat: latitude, lng: longitude });
      mapInstance.setCenter([longitude, latitude]);
    });
  }, []);
  
  const addMarker = (location) => {
    const marker = new Marker({
      position: [location.lng, location.lat],
      map: map
    });
    setMarkers(prev => [...prev, marker]);
  };
  
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
      <div className="map-controls">
        <button onClick={trackUser}>Track Location</button>
        <button onClick={() => addMarker(userLocation)}>Add Marker</button>
      </div>
    </div>
  );
};
```

Deep Insight:
- Use efficient clustering for large numbers of markers
- Implement smooth animations for location updates
- Consider offline map functionality
- Handle different map providers and APIs
- Optimize rendering performance for mobile devices

## 73) How would you design a Progressive Web App (PWA) with offline mode, push notifications, and installability?

Concept: PWAs require service workers for offline functionality, web app manifests for installability, push notification APIs, and proper caching strategies.

Example:
```javascript
const PWAApp = () => {
  const [isOnline, setIsOnline] = useState(navigator.onLine);
  const [deferredPrompt, setDeferredPrompt] = useState(null);
  
  useEffect(() => {
    // Handle online/offline status
    const handleOnline = () => setIsOnline(true);
    const handleOffline = () => setIsOnline(false);
    
    window.addEventListener('online', handleOnline);
    window.addEventListener('offline', handleOffline);
    
    // Handle install prompt
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
      console.log(`User response: ${outcome}`);
      setDeferredPrompt(null);
    }
  };
  
  return (
    <div className="pwa-app">
      <header>
        <h1>My PWA</h1>
        {!isOnline && <div className="offline-indicator">Offline</div>}
        {deferredPrompt && (
          <button onClick={handleInstall}>Install App</button>
        )}
      </header>
      <main>
        <Content />
      </main>
    </div>
  );
};
```

Deep Insight:
- Implement service workers for offline functionality
- Use web app manifest for installability
- Handle push notifications with proper permissions
- Implement proper caching strategies
- Test across different browsers and devices

## 74) How would you design a dashboard UI with real-time charts and metrics for multiple users?

Concept: Real-time dashboards require efficient data visualization, WebSocket connections for live updates, responsive layouts, and proper state management for complex metrics.

Example:
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
      <header>
        <h1>Analytics Dashboard</h1>
        <div className={`status ${isConnected ? 'connected' : 'disconnected'}`}>
          {isConnected ? 'Live' : 'Offline'}
        </div>
      </header>
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

Deep Insight:
- Use efficient charting libraries for real-time updates
- Implement proper data aggregation and sampling
- Handle connection failures and reconnection logic
- Consider performance optimization for large datasets
- Implement proper error handling and fallbacks

## 75) How would you design a front-end that dynamically loads micro-frontends, handles versioning, and supports independent deployment?

Concept: Dynamic micro-frontend loading requires proper module federation, version management, fallback strategies, and independent deployment coordination.

Example:
```javascript
const MicroFrontendLoader = ({ name, version, fallback }) => {
  const [Component, setComponent] = useState(null);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState(null);
  
  useEffect(() => {
    const loadMicroFrontend = async () => {
      try {
        const module = await System.import(`${name}@${version}/remoteEntry.js`);
        const component = module.default;
        setComponent(() => component);
      } catch (err) {
        console.error(`Failed to load ${name}@${version}:`, err);
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

Deep Insight:
- Implement proper version management and fallback strategies
- Use module federation for dynamic loading
- Handle independent deployment and version conflicts
- Implement proper error boundaries and fallbacks
- Consider performance implications of dynamic loading

## 76) How would you design a high-performance image carousel for web and mobile with memory optimization?

Concept: High-performance image carousels require lazy loading, memory management, smooth animations, and responsive design for optimal user experience.

Example:
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
    
    // Load visible images
    for (let i = start; i <= end; i++) {
      loadImage(i);
    }
  }, [images.length, loadImage]);
  
  useEffect(() => {
    updateVisibleRange(currentIndex);
  }, [currentIndex, updateVisibleRange]);
  
  return (
    <div className="carousel">
      <div className="carousel-container">
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
      <div className="carousel-controls">
        <button onClick={() => setCurrentIndex(prev => Math.max(0, prev - 1))}>
          Previous
        </button>
        <button onClick={() => setCurrentIndex(prev => Math.min(images.length - 1, prev + 1))}>
          Next
        </button>
      </div>
    </div>
  );
};
```

Deep Insight:
- Implement lazy loading for memory efficiency
- Use CSS transforms for smooth animations
- Manage visible range to optimize performance
- Implement proper image preloading strategies
- Consider responsive design and touch gestures

## 77) How would you design accessible UI components (screen readers, keyboard navigation, color modes)?

Concept: Accessible UI components require proper ARIA attributes, keyboard navigation support, color contrast compliance, and screen reader compatibility.

Example:
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

Deep Insight:
- Implement proper ARIA attributes and roles
- Support keyboard navigation and focus management
- Ensure color contrast meets WCAG standards
- Test with screen readers and assistive technologies
- Provide multiple ways to convey information

## 78) How would you design a global theme switcher (dark/light modes) that persists across sessions?

Concept: Global theme switching requires centralized theme management, persistent storage, smooth transitions, and proper CSS variable handling.

Example:
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

const ThemeSwitcher = () => {
  const { theme, toggleTheme } = useContext(ThemeContext);
  
  return (
    <button
      onClick={toggleTheme}
      className="theme-switcher"
      aria-label={`Switch to ${theme === 'light' ? 'dark' : 'light'} mode`}
    >
      {theme === 'light' ? '🌙' : '☀️'}
    </button>
  );
};
```

Deep Insight:
- Use CSS custom properties for theme values
- Implement smooth transitions between themes
- Persist theme preferences across sessions
- Consider system theme detection
- Test with different color schemes and contrast ratios

## 79) How would you design routing architecture for a SPA with SEO support and fast transitions?

Concept: SPA routing requires client-side navigation, SEO optimization, fast transitions, and proper state management for complex applications.

Example:
```javascript
const AppRouter = () => {
  const [currentRoute, setCurrentRoute] = useState(window.location.pathname);
  const [isLoading, setIsLoading] = useState(false);
  
  useEffect(() => {
    const handleRouteChange = (path) => {
      setIsLoading(true);
      setCurrentRoute(path);
      window.history.pushState({}, '', path);
      
      // Preload route component
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

Deep Insight:
- Implement client-side routing with proper history management
- Use code splitting for better performance
- Consider SEO implications and meta tag management
- Implement proper loading states and error handling
- Test navigation across different browsers and devices

## 80) How would you design a file upload system with progress tracking, resumable uploads, and mobile fallback?

Concept: File upload systems require progress tracking, chunked uploads for resumability, mobile optimization, and proper error handling for various scenarios.

Example:
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
  
  const handleFileSelect = (e) => {
    const selectedFiles = Array.from(e.target.files);
    setFiles(prev => [...prev, ...selectedFiles]);
    
    selectedFiles.forEach(file => {
      uploadFile(file);
    });
  };
  
  return (
    <div className="file-upload">
      <input
        type="file"
        multiple
        onChange={handleFileSelect}
        accept="image/*,video/*,application/pdf"
      />
      <div className="upload-list">
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
    </div>
  );
};
```

Deep Insight:
- Implement chunked uploads for large files
- Use progress tracking for better user experience
- Handle network failures and resume functionality
- Optimize for mobile devices and touch interfaces
- Consider file validation and security measures

## 81) How would you design a feature flag / A/B testing framework for front-end experiments?

Concept: Feature flags require dynamic configuration, A/B testing capabilities, user segmentation, and proper analytics integration for data-driven decisions.

Example:
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

const FeatureComponent = ({ flagName, children, fallback }) => {
  const { isFeatureEnabled } = useContext(FeatureFlagContext);
  
  if (isFeatureEnabled(flagName)) {
    return children;
  }
  
  return fallback || null;
};
```

Deep Insight:
- Implement dynamic feature flag configuration
- Use proper user segmentation for A/B testing
- Integrate with analytics for data collection
- Consider performance implications of feature flags
- Implement proper fallback strategies

## 82) How would you design a notification system (toast, in-app, segmented delivery, analytics)?

Concept: Notification systems require multiple delivery channels, user preferences, analytics tracking, and proper state management for complex notification flows.

Example:
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
    
    // Send to different channels based on preferences
    if (preferences.push && notification.priority === 'high') {
      sendPushNotification(notification);
    }
    
    if (preferences.email && notification.type === 'email') {
      sendEmailNotification(notification);
    }
    
    // Track analytics
    trackNotificationSent(notification);
  };
  
  const markAsRead = (id) => {
    setNotifications(prev => 
      prev.map(notif => 
        notif.id === id ? { ...notif, read: true } : notif
      )
    );
  };
  
  return (
    <div className="notification-system">
      <NotificationList 
        notifications={notifications}
        onMarkAsRead={markAsRead}
      />
      <NotificationPreferences 
        preferences={preferences}
        onChange={setPreferences}
      />
    </div>
  );
};
```

Deep Insight:
- Implement multiple notification channels
- Use user preferences for personalized delivery
- Track analytics for notification effectiveness
- Consider notification frequency and timing
- Implement proper notification management and cleanup

## 83) How would you design a search results UI with infinite scrolling, client-side caching, and filters?

Concept: Search results require efficient data management, client-side caching, infinite scrolling, and proper filter handling for optimal user experience.

Example:
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
      <SearchInput 
        value={query}
        onChange={setQuery}
        onSearch={() => performSearch(query, filters)}
      />
      <FilterPanel 
        filters={filters}
        onChange={setFilters}
      />
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

Deep Insight:
- Implement client-side caching for better performance
- Use infinite scrolling for large result sets
- Handle filter combinations efficiently
- Consider search result ranking and relevance
- Implement proper loading states and error handling

## 84) How would you design a live streaming UI (video/audio, low latency, buffering indicators, streaming controls)?

Concept: Live streaming UIs require real-time video/audio handling, low-latency optimization, proper buffering management, and intuitive streaming controls.

Example:
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
  
  const stopStream = () => {
    if (stream) {
      stream.getTracks().forEach(track => track.stop());
      setStream(null);
      setIsPlaying(false);
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
        <button onClick={isPlaying ? stopStream : startStream}>
          {isPlaying ? 'Stop Stream' : 'Start Stream'}
        </button>
        <select value={quality} onChange={(e) => setQuality(e.target.value)}>
          <option value="auto">Auto</option>
          <option value="720p">720p</option>
          <option value="480p">480p</option>
          <option value="360p">360p</option>
        </select>
      </div>
    </div>
  );
};
```

Deep Insight:
- Implement low-latency streaming protocols
- Use proper buffering management for smooth playback
- Handle different quality levels and adaptive streaming
- Consider mobile optimization and touch controls
- Implement proper error handling and reconnection logic
