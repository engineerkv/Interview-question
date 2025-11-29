<div align="center">

**[← Previous: Browser Internals & Rendering](6%29%20Browser%20Internals%20%26%20Rendering.md)** | **[Next: Networking & APIs →](8%29%20Networking%20%26%20APIs.md)**

</div>

# 7. Practical Front-End System Design Scenarios (Q65–83)

---

## Q65. Designing a news feed UI like Facebook or Twitter

A news feed requires efficient data management, virtual scrolling for performance, real-time updates via WebSockets, and proper state synchronization across components - consider pagination strategies and data freshness. Use virtual scrolling to handle thousands of posts efficiently.

- **Trade-offs**: The catch is implement optimistic updates for better user experience - use WebSocket connections for real-time updates. Consider pagination strategies and data freshness, but watch out - cache posts locally and implement offline support.

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

---

## Q66. Designing an autocomplete search component

Autocomplete requires debounced input handling, efficient search algorithms, caching of results, and proper keyboard navigation for accessibility - consider fuzzy matching and search suggestions. Implement debouncing to avoid excessive API calls.

- **Trade-offs**: The catch is use keyboard navigation for accessibility - cache search results to improve performance. Consider fuzzy matching and search suggestions, but watch out - handle loading states and error scenarios.

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

---

## Q67. Designing a large data table with sorting and filtering

Large data tables require virtualization for performance, efficient sorting algorithms, client-side filtering, and proper state management for complex interactions - ensure accessibility with proper ARIA attributes. Use virtualization to handle large datasets efficiently.

- **Trade-offs**: The catch is implement client-side sorting and filtering for better performance - provide clear visual feedback for sort and filter states. Ensure accessibility with proper ARIA attributes, but watch out - consider server-side pagination for very large datasets.

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

---

## Q68. Designing a real-time chat interface

Real-time chat requires WebSocket connections, message queuing, offline storage, delivery status tracking, and proper state synchronization - implement proper message delivery status tracking. Implement WebSocket connections for real-time communication.

- **Trade-offs**: The catch is use optimistic updates for better user experience - store messages locally for offline access. Implement proper message delivery status tracking, but watch out - handle connection failures and reconnection logic.

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

---

## Q69. Designing a media gallery with lazy loading

Media galleries require lazy loading, responsive image sizing, progressive loading, and efficient memory management for large collections - implement proper error handling and fallbacks. Use Intersection Observer for efficient lazy loading.

- **Trade-offs**: The catch is implement responsive image sizing with srcset - consider progressive loading for better perceived performance. Implement proper error handling and fallbacks, but watch out - use virtual scrolling for very large galleries.

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

---

## Q70. Designing an e-commerce shopping cart

Shopping cart requires offline storage, cross-device synchronization, optimistic updates, and proper state management for complex business logic - consider inventory management and stock validation. Use localStorage for offline cart persistence.

- **Trade-offs**: The catch is implement cross-device synchronization via user accounts - handle offline scenarios gracefully with proper messaging. Consider inventory management and stock validation, but watch out - use optimistic updates for better user experience.

Example:

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

---

## Q71. Designing a collaborative text editor

Collaborative editing requires real-time synchronization, conflict resolution, operational transforms, and proper cursor/selection management - consider performance optimization for large documents. Implement operational transforms for conflict resolution.

- **Trade-offs**: The catch is use WebSocket connections for real-time synchronization - handle cursor and selection management across users. Consider performance optimization for large documents, but watch out - implement proper undo/redo functionality.

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
      <RichTextEditor
        value={content}
        onChange={handleContentChange}
        cursors={cursors}
      />
    </div>
  );
};
```

---

## Q72. Designing a map-based interface with markers

Map-based UIs require efficient rendering of large datasets, real-time location updates, smooth animations, and proper handling of map interactions - optimize rendering performance for mobile devices. Use efficient clustering for large numbers of markers.

- **Trade-offs**: The catch is implement smooth animations for location updates - consider offline map functionality. Optimize rendering performance for mobile devices, but watch out - handle different map providers and APIs.

Example:

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

---

## Q73. Designing a dashboard with real-time data

Real-time dashboards require efficient data visualization, WebSocket connections for live updates, responsive layouts, and proper state management for complex metrics - implement proper error handling and fallbacks. Use efficient charting libraries for real-time updates.

- **Trade-offs**: The catch is implement proper data aggregation and sampling - handle connection failures and reconnection logic. Implement proper error handling and fallbacks, but watch out - consider performance optimization for large datasets.

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
  );
};
```

---

## Q74. Designing a dynamic micro-frontend architecture

Dynamic micro-frontend loading requires proper module federation, version management, fallback strategies, and independent deployment coordination - consider performance implications of dynamic loading. Implement proper version management and fallback strategies.

- **Trade-offs**: The catch is use module federation for dynamic loading - handle independent deployment and version conflicts. Consider performance implications of dynamic loading, but watch out - implement proper error boundaries and fallbacks.

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

---

## Q75. Designing a high-performance image carousel

High-performance image carousels require lazy loading, memory management, smooth animations, and responsive design for optimal user experience - consider responsive design and touch gestures. Implement lazy loading for memory efficiency.

- **Trade-offs**: The catch is use CSS transforms for smooth animations - manage visible range to optimize performance. Consider responsive design and touch gestures, but watch out - implement proper image preloading strategies.

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

---

## Q76. Designing an accessible UI component library

Accessible UI components require proper ARIA attributes, keyboard navigation support, color contrast compliance, and screen reader compatibility - provide multiple ways to convey information. Implement proper ARIA attributes and roles.

- **Trade-offs**: The catch is support keyboard navigation and focus management - ensure color contrast meets WCAG standards. Provide multiple ways to convey information, but watch out - test with screen readers and assistive technologies.

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

---

## Q77. Designing a global theme switching system

Global theme switching requires centralized theme management, persistent storage, smooth transitions, and proper CSS variable handling - test with different color schemes and contrast ratios. Use CSS custom properties for theme values.

- **Trade-offs**: The catch is implement smooth transitions between themes - persist theme preferences across sessions. Test with different color schemes and contrast ratios, but watch out - consider system theme detection.

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
```

---

## Q78. Designing a routing architecture for a large SPA

SPA routing requires client-side navigation, SEO optimization, fast transitions, and proper state management for complex applications - test navigation across different browsers and devices. Implement client-side routing with proper history management.

- **Trade-offs**: The catch is use code splitting for better performance - consider SEO implications and meta tag management. Test navigation across different browsers and devices, but watch out - implement proper loading states and error handling.

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

---

## Q79. Designing a file upload system with progress tracking

File upload systems require progress tracking, chunked uploads for resumability, mobile optimization, and proper error handling for various scenarios - consider file validation and security measures. Implement chunked uploads for large files.

- **Trade-offs**: The catch is use progress tracking for better user experience - handle network failures and resume functionality. Consider file validation and security measures, but watch out - optimize for mobile devices and touch interfaces.

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
      ))}
    </div>
  );
};
```

---

## Q80. Designing a feature flag and A/B testing system

Feature flags require dynamic configuration, A/B testing capabilities, user segmentation, and proper analytics integration for data-driven decisions - implement proper fallback strategies. Implement dynamic feature flag configuration.

- **Trade-offs**: The catch is use proper user segmentation for A/B testing - integrate with analytics for data collection. Implement proper fallback strategies, but watch out - consider performance implications of feature flags.

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
```

---

## Q81. Designing a notification system for web apps

Notification systems require multiple delivery channels, user preferences, analytics tracking, and proper state management for complex notification flows - implement proper notification management and cleanup. Implement multiple notification channels.

- **Trade-offs**: The catch is use user preferences for personalized delivery - track analytics for notification effectiveness. Implement proper notification management and cleanup, but watch out - consider notification frequency and timing.

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

---

## Q82. Designing a search results UI with faceted search

Search results require efficient data management, client-side caching, infinite scrolling, and proper filter handling for optimal user experience - implement proper loading states and error handling. Implement client-side caching for better performance.

- **Trade-offs**: The catch is use infinite scrolling for large result sets - handle filter combinations efficiently. Implement proper loading states and error handling, but watch out - consider search result ranking and relevance.

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

---

## Q83. Designing a live streaming video interface

Live streaming UIs require real-time video/audio handling, low-latency optimization, proper buffering management, and intuitive streaming controls - implement proper error handling and reconnection logic. Implement low-latency streaming protocols.

- **Trade-offs**: The catch is use proper buffering management for smooth playback - handle different quality levels and adaptive streaming. Implement proper error handling and reconnection logic, but watch out - consider mobile optimization and touch controls.

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
  );
};
```

---

