# ⚛️ React Native Interview Notes (2025 Edition)

## ⚙️ Section 4 — Performance Optimization & Memory Management — Q91-Q110

---

## **Q91. What are the main performance bottlenecks in React Native?**

**🧠 Concept**

The main performance bottlenecks in React Native include JavaScript thread blocking, bridge communication overhead, memory leaks, and inefficient rendering.

**💻 Example**
```javascript
// Bad: Blocking JavaScript thread
const processLargeData = (data) => {
  for (let i = 0; i < 1000000; i++) {
    // Heavy computation blocks UI
  }
};

// Good: Use background thread
const processLargeData = async (data) => {
  return new Promise((resolve) => {
    setTimeout(() => {
      // Process data in background
      resolve(processedData);
    }, 0);
  });
};
```

**💬 Explanation + Insight**

- JavaScript thread: Heavy computations block the UI thread
- Bridge overhead: Communication between JS and native has cost
- Memory leaks: Unused objects cause memory issues
- Re-renders: Unnecessary component re-renders hurt performance
- List performance: Large lists without optimization are slow

---

## **Q92. How do you profile React Native performance?**

**🧠 Concept**

React Native performance can be profiled using Flipper, Chrome DevTools, and native profiling tools to identify bottlenecks and optimize performance.

**💻 Example**
```javascript
// Performance profiling
import { Performance } from 'react-native';

const measurePerformance = () => {
  const startTime = Performance.now();
  
  // Your code here
  performOperation();
  
  const endTime = Performance.now();
  console.log(`Operation took ${endTime - startTime} milliseconds`);
};
```

**💬 Explanation + Insight**

- Flipper: Use Flipper for comprehensive debugging
- Chrome DevTools: Use Chrome DevTools for JavaScript profiling
- Native tools: Use Xcode/Android Studio for native profiling
- Performance.now: Measure execution time
- Memory profiling: Check for memory leaks

---

## **Q93. What is Hermes and how does it optimize performance?**

**🧠 Concept**

Hermes is a JavaScript engine optimized for React Native that provides faster app startup, reduced memory usage, and better performance.

**💻 Example**
```javascript
// Hermes configuration in metro.config.js
module.exports = {
  transformer: {
    hermesParser: true,
  },
  resolver: {
    hermesParser: true,
  },
};
```

**💬 Explanation + Insight**

- Faster startup: Hermes reduces app startup time
- Memory efficiency: Uses less memory than other engines
- Bytecode: Pre-compiles JavaScript to bytecode
- Bundle size: Reduces bundle size
- Performance: Better overall performance

---

## **Q94. How do you optimize FlatList performance in React Native?**

**🧠 Concept**

FlatList performance can be optimized using getItemLayout, keyExtractor, removeClippedSubviews, and proper data structure.

**💻 Example**
```javascript
const MyFlatList = () => {
  const renderItem = ({ item }) => (
    <View style={styles.item}>
      <Text>{item.title}</Text>
    </View>
  );

  return (
    <FlatList
      data={data}
      renderItem={renderItem}
      keyExtractor={(item) => item.id}
      getItemLayout={(data, index) => ({
        length: ITEM_HEIGHT,
        offset: ITEM_HEIGHT * index,
        index,
      })}
      removeClippedSubviews={true}
      maxToRenderPerBatch={10}
      windowSize={10}
    />
  );
};
```

**💬 Explanation + Insight**

- getItemLayout: Provides exact item dimensions for better performance
- keyExtractor: Unique keys help React identify items
- removeClippedSubviews: Removes off-screen items from memory
- maxToRenderPerBatch: Controls how many items render at once
- windowSize: Controls how many items to keep in memory

---

## **Q95. What is getItemLayout and why is it important?**

**🧠 Concept**

getItemLayout is a FlatList prop that provides exact item dimensions, enabling better performance by avoiding layout calculations.

**💻 Example**
```javascript
const getItemLayout = (data, index) => ({
  length: ITEM_HEIGHT,
  offset: ITEM_HEIGHT * index,
  index,
});

<FlatList
  data={data}
  getItemLayout={getItemLayout}
  renderItem={renderItem}
/>
```

**💬 Explanation + Insight**

- Performance: Eliminates layout calculations for better performance
- Scrolling: Enables smooth scrolling
- Memory: Reduces memory usage
- Required: Essential for large lists
- Dimensions: Must provide exact item dimensions

---

## **Q96. How do you prevent unnecessary re-renders in React Native?**

**🧠 Concept**

Unnecessary re-renders can be prevented using React.memo, useMemo, useCallback, and proper state management.

**💻 Example**
```javascript
const MyComponent = React.memo(({ data, onPress }) => {
  const processedData = useMemo(() => {
    return data.map(item => item.value * 2);
  }, [data]);

  const handlePress = useCallback(() => {
    onPress(processedData);
  }, [onPress, processedData]);

  return (
    <TouchableOpacity onPress={handlePress}>
      <Text>{processedData.length}</Text>
    </TouchableOpacity>
  );
});
```

**💬 Explanation + Insight**

- React.memo: Prevents re-renders when props haven't changed
- useMemo: Memoizes expensive calculations
- useCallback: Memoizes functions to prevent re-creation
- State management: Proper state management prevents unnecessary updates
- Performance: Reduces CPU usage and improves performance

---

## **Q97. How do you debug performance issues with Flipper?**

**🧠 Concept**

Flipper provides debugging tools for React Native performance including network inspection, layout debugging, and performance profiling.

**💻 Example**
```javascript
// Flipper integration
import { Flipper } from 'react-native-flipper';

const App = () => {
  useEffect(() => {
    Flipper.addPlugin({
      getId() {
        return 'PerformancePlugin';
      },
      onConnect(connection) {
        connection.send('performance', { 
          timestamp: Date.now(),
          memory: performance.memory?.usedJSHeapSize 
        });
      },
    });
  }, []);

  return <MyApp />;
};
```

**💬 Explanation + Insight**

- Network inspection: Monitor network requests and responses
- Layout debugging: Debug layout and styling issues
- Performance profiling: Profile app performance
- Memory usage: Monitor memory usage and leaks
- Real-time: Real-time debugging and monitoring

---

## **Q98. How do you identify and fix memory leaks in React Native?**

**🧠 Concept**

Memory leaks can be identified using profiling tools and fixed by properly cleaning up resources, event listeners, and subscriptions.

**💻 Example**
```javascript
const MyComponent = () => {
  const [data, setData] = useState([]);

  useEffect(() => {
    const subscription = eventEmitter.addListener('data', (newData) => {
      setData(newData);
    });

    // Cleanup to prevent memory leak
    return () => {
      subscription.remove();
    };
  }, []);

  useEffect(() => {
    const timer = setInterval(() => {
      // Some operation
    }, 1000);

    // Cleanup timer
    return () => {
      clearInterval(timer);
    };
  }, []);

  return <View>{/* Component content */}</View>;
};
```

**💬 Explanation + Insight**

- Event listeners: Always remove event listeners
- Timers: Clear timers and intervals
- Subscriptions: Remove subscriptions
- Resources: Clean up native resources
- Profiling: Use profiling tools to identify leaks

---

## **Q99. How do you optimize bundle size in React Native?**

**🧠 Concept**

Bundle size can be optimized by removing unused code, using dynamic imports, and configuring Metro bundler for better tree shaking.

**💻 Example**
```javascript
// Dynamic imports
const LazyComponent = React.lazy(() => import('./LazyComponent'));

const App = () => {
  return (
    <Suspense fallback={<Loading />}>
      <LazyComponent />
    </Suspense>
  );
};

// Metro configuration
module.exports = {
  transformer: {
    minifierConfig: {
      keep_fnames: true,
      mangle: {
        keep_fnames: true,
      },
    },
  },
};
```

**💬 Explanation + Insight**

- Tree shaking: Remove unused code
- Dynamic imports: Load code only when needed
- Minification: Minify JavaScript code
- Dependencies: Remove unused dependencies
- Assets: Optimize images and assets

---

## **Q100. How do you optimize image loading in React Native?**

**🧠 Concept**

Image loading can be optimized by using appropriate image formats, lazy loading, caching, and proper image sizing.

**💻 Example**
```javascript
import FastImage from 'react-native-fast-image';

const OptimizedImage = ({ uri, style }) => (
  <FastImage
    source={{
      uri,
      priority: FastImage.priority.normal,
      cache: FastImage.cacheControl.immutable,
    }}
    style={style}
    resizeMode={FastImage.resizeMode.cover}
  />
);
```

**💬 Explanation + Insight**

- FastImage: Better performance than default Image component
- Caching: Use appropriate caching strategies
- Lazy loading: Load images only when needed
- Formats: Use appropriate image formats
- Sizing: Optimize image dimensions

---

## **Q101. How do you handle background tasks in React Native?**

**🧠 Concept**

Background tasks in React Native are handled using background services, task queues, and proper lifecycle management.

**💻 Example**
```javascript
import BackgroundJob from 'react-native-background-job';

const startBackgroundTask = () => {
  BackgroundJob.start({
    jobKey: 'myJob',
    period: 15000, // 15 seconds
    requiredNetworkType: 'wifi',
  });
};

const stopBackgroundTask = () => {
  BackgroundJob.stop({ jobKey: 'myJob' });
};
```

**💬 Explanation + Insight**

- Background services: Use background services for long-running tasks
- Task queues: Queue tasks for background execution
- Lifecycle: Manage app lifecycle properly
- Permissions: Handle background permissions
- Performance: Consider performance impact

---

## **Q102. How do you optimize animations in React Native?**

**🧠 Concept**

Animations can be optimized by using native driver, avoiding JavaScript thread, and using appropriate animation libraries.

**💻 Example**
```javascript
import { Animated } from 'react-native';

const MyAnimatedComponent = () => {
  const animatedValue = useRef(new Animated.Value(0)).current;

  const startAnimation = () => {
    Animated.timing(animatedValue, {
      toValue: 1,
      duration: 1000,
      useNativeDriver: true, // Use native driver
    }).start();
  };

  return (
    <Animated.View
      style={{
        opacity: animatedValue,
        transform: [{
          translateY: animatedValue.interpolate({
            inputRange: [0, 1],
            outputRange: [0, 100],
          }),
        }],
      }}
    >
      <Text>Animated Content</Text>
    </Animated.View>
  );
};
```

**💬 Explanation + Insight**

- Native driver: Use native driver for better performance
- JavaScript thread: Avoid blocking JavaScript thread
- Libraries: Use optimized animation libraries
- Performance: Monitor animation performance
- Smooth: Ensure smooth animations

---

## **Q103. How do you use React Query for data fetching optimization?**

**🧠 Concept**

React Query provides caching, background updates, and optimistic updates for better data fetching performance.

**💻 Example**
```javascript
import { useQuery, useMutation, useQueryClient } from 'react-query';

const MyComponent = () => {
  const queryClient = useQueryClient();

  const { data, isLoading, error } = useQuery('users', fetchUsers, {
    staleTime: 5 * 60 * 1000, // 5 minutes
    cacheTime: 10 * 60 * 1000, // 10 minutes
  });

  const mutation = useMutation(updateUser, {
    onSuccess: () => {
      queryClient.invalidateQueries('users');
    },
  });

  if (isLoading) return <Loading />;
  if (error) return <Error />;

  return <UserList data={data} />;
};
```

**💬 Explanation + Insight**

- Caching: Automatic caching of API responses
- Background updates: Updates data in background
- Optimistic updates: Updates UI before server response
- Performance: Reduces unnecessary API calls
- User experience: Better user experience

---

## **Q104. How do you use SWR for data fetching optimization?**

**🧠 Concept**

SWR provides data fetching with caching, revalidation, and error handling for better performance.

**💻 Example**
```javascript
import useSWR from 'swr';

const MyComponent = () => {
  const { data, error, mutate } = useSWR('/api/users', fetcher, {
    revalidateOnFocus: true,
    revalidateOnReconnect: true,
    dedupingInterval: 2000,
  });

  if (error) return <Error />;
  if (!data) return <Loading />;

  return <UserList data={data} />;
};
```

**💬 Explanation + Insight**

- Caching: Automatic caching of data
- Revalidation: Revalidates data when needed
- Error handling: Built-in error handling
- Performance: Reduces unnecessary requests
- Simplicity: Simple API for data fetching

---

## **Q105. How do you optimize SectionList performance?**

**🧠 Concept**

SectionList performance can be optimized using getItemLayout, keyExtractor, and proper data structure.

**💻 Example**
```javascript
const MySectionList = () => {
  const renderItem = ({ item }) => (
    <View style={styles.item}>
      <Text>{item.title}</Text>
    </View>
  );

  const renderSectionHeader = ({ section }) => (
    <View style={styles.sectionHeader}>
      <Text>{section.title}</Text>
    </View>
  );

  return (
    <SectionList
      sections={data}
      renderItem={renderItem}
      renderSectionHeader={renderSectionHeader}
      keyExtractor={(item) => item.id}
      getItemLayout={(data, index) => ({
        length: ITEM_HEIGHT,
        offset: ITEM_HEIGHT * index,
        index,
      })}
      removeClippedSubviews={true}
    />
  );
};
```

**💬 Explanation + Insight**

- getItemLayout: Provides exact item dimensions
- keyExtractor: Unique keys for better performance
- removeClippedSubviews: Removes off-screen items
- Data structure: Optimize data structure
- Performance: Better scrolling performance

---

## **Q106. How do you handle large datasets in React Native?**

**🧠 Concept**

Large datasets can be handled using pagination, virtualization, and efficient data structures.

**💻 Example**
```javascript
const MyList = () => {
  const [data, setData] = useState([]);
  const [loading, setLoading] = useState(false);
  const [page, setPage] = useState(1);

  const loadMore = async () => {
    if (loading) return;
    
    setLoading(true);
    const newData = await fetchData(page);
    setData(prev => [...prev, ...newData]);
    setPage(prev => prev + 1);
    setLoading(false);
  };

  return (
    <FlatList
      data={data}
      renderItem={renderItem}
      onEndReached={loadMore}
      onEndReachedThreshold={0.5}
      ListFooterComponent={loading ? <Loading /> : null}
    />
  );
};
```

**💬 Explanation + Insight**

- Pagination: Load data in chunks
- Virtualization: Use virtualization for large lists
- Efficient structures: Use efficient data structures
- Memory: Manage memory usage
- Performance: Optimize for performance

---

## **Q107. How do you optimize network requests in React Native?**

**🧠 Concept**

Network requests can be optimized using caching, request batching, and proper error handling.

**💻 Example**
```javascript
const useOptimizedFetch = (url) => {
  const [data, setData] = useState(null);
  const [loading, setLoading] = useState(false);
  const [error, setError] = useState(null);

  const fetchData = useCallback(async () => {
    setLoading(true);
    try {
      const response = await fetch(url, {
        headers: {
          'Cache-Control': 'max-age=300', // 5 minutes cache
        },
      });
      const result = await response.json();
      setData(result);
    } catch (err) {
      setError(err);
    } finally {
      setLoading(false);
    }
  }, [url]);

  return { data, loading, error, fetchData };
};
```

**💬 Explanation + Insight**

- Caching: Use appropriate caching strategies
- Batching: Batch multiple requests
- Error handling: Implement proper error handling
- Performance: Optimize request performance
- User experience: Better user experience

---

## **Q108. How do you monitor app performance in production?**

**🧠 Concept**

App performance can be monitored using analytics tools, crash reporting, and performance monitoring services.

**💻 Example**
```javascript
import crashlytics from '@react-native-firebase/crashlytics';
import analytics from '@react-native-firebase/analytics';

const trackPerformance = (operation, duration) => {
  analytics().logEvent('performance', {
    operation,
    duration,
    timestamp: Date.now(),
  });
};

const trackError = (error) => {
  crashlytics().recordError(error);
};
```

**💬 Explanation + Insight**

- Analytics: Use analytics for performance tracking
- Crash reporting: Monitor crashes and errors
- Performance metrics: Track performance metrics
- Real-time: Monitor performance in real-time
- Optimization: Use data for optimization

---

## **Q109. How do you optimize app startup time?**

**🧠 Concept**

App startup time can be optimized by reducing bundle size, using Hermes, and implementing lazy loading.

**💻 Example**
```javascript
// Lazy loading for better startup
const LazyScreen = React.lazy(() => import('./LazyScreen'));

const App = () => {
  return (
    <Suspense fallback={<Loading />}>
      <LazyScreen />
    </Suspense>
  );
};

// Hermes configuration
module.exports = {
  transformer: {
    hermesParser: true,
  },
};
```

**💬 Explanation + Insight**

- Bundle size: Reduce bundle size
- Hermes: Use Hermes for better performance
- Lazy loading: Load code only when needed
- Startup: Optimize startup process
- Performance: Better overall performance

---

## **Q110. How do you handle memory management in React Native?**

**🧠 Concept**

Memory management involves proper cleanup, avoiding memory leaks, and monitoring memory usage.

**💻 Example**
```javascript
const MyComponent = () => {
  const [data, setData] = useState([]);

  useEffect(() => {
    const subscription = eventEmitter.addListener('data', (newData) => {
      setData(newData);
    });

    return () => {
      subscription.remove();
    };
  }, []);

  useEffect(() => {
    const timer = setInterval(() => {
      // Some operation
    }, 1000);

    return () => {
      clearInterval(timer);
    };
  }, []);

  return <View>{/* Component content */}</View>;
};
```

**💬 Explanation + Insight**

- Cleanup: Always clean up resources
- Memory leaks: Avoid memory leaks
- Monitoring: Monitor memory usage
- Performance: Optimize memory usage
- Best practices: Follow best practices

---

*This section covers performance bottlenecks, profiling, Hermes optimization, FlatList/SectionList performance, getItemLayout, re-render prevention, Flipper debugging, memory leaks, bundle size optimization, image loading, background tasks, animations, and React Query/SWR.*
