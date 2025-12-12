# 6. Performance & Profiling (Q52–66)

---

## 📍 Navigation

<div align="center">

[Platform-Specific Development](05%29%20Platform-Specific%20Development.md) • [Home: README](../README.md) • [Animations & Graphics →](07%29%20Animations%20%26%20Graphics.md)

[📋 Cheatsheet](React%20Native%20Interview%20Cheatsheet.md)

</div>

---

---

## Q52. 💡 Optimizing FlatList for large datasets

FlatList is optimized for large lists with virtualization, while ScrollView renders all children and is better for small, static content - FlatList is preferred for dynamic lists. ScrollView renders all children, good for small lists; FlatList uses virtualized rendering, good for large lists.

- **Trade-offs**: The catch is FlatList uses less memory for large lists (memory usage) - choose based on data size and performance requirements (use cases). FlatList is preferred for dynamic lists, but watch out - FlatList is more performant for large datasets (performance).

Example:

```jsx
// ScrollView - renders all children
function ScrollViewExample({ data }) {
  return (
    <ScrollView>
      {data.map(item => (
        <View key={item.id}>
          <Text>{item.name}</Text>
        </View>
      ))}
    </ScrollView>
  );
}

// FlatList - virtualized rendering
function FlatListExample({ data }) {
  return (
    <FlatList
      data={data}
      renderItem={({ item }) => <Text>{item.name}</Text>}
      keyExtractor={item => item.id}
    />
  );
}

```

---

## Q53. 🤔 Difference between FlatList and ScrollView

Props like `getItemLayout`, `initialNumToRender`, and `windowSize` optimize FlatList rendering by providing layout information, controlling initial render count, and setting the render window size - these props are key to FlatList optimization. `getItemLayout` provides item dimensions for better performance, `initialNumToRender` controls how many items render initially, `windowSize` sets the render window size.

- **Trade-offs**: The catch is use these props to optimize for your specific use case (optimization) - fine-tune rendering for best performance. These props are key to FlatList optimization, but watch out - these props significantly impact performance (performance impact).

Example:

```jsx
function OptimizedFlatList({ data }) {
  const getItemLayout = useCallback((data, index) => ({
    length: ITEM_HEIGHT,
    offset: ITEM_HEIGHT * index,
    index,
  }), []);

  return (
    <FlatList
      data={data}
      getItemLayout={getItemLayout}
      initialNumToRender={10}
      windowSize={5}
      renderItem={renderItem}
    />
  );
}

```

---

## Q54. 📱 Implementing virtualization in React Native

Use React.memo, useMemo, and useCallback to optimize renderItem functions and prevent unnecessary re-renders - memoization is critical for FlatList performance. React.memo prevents re-renders when props haven't changed, useCallback memoizes callback functions, useMemo memoizes expensive calculations.

- **Trade-offs**: The catch is use these patterns for FlatList optimization (best practices) - combine multiple optimizations for best results. Memoization is critical for FlatList performance, but watch out - these optimizations improve FlatList performance (performance).

Example:

```jsx
const ListItem = React.memo(({ item, onPress }) => {
  const handlePress = useCallback(() => {
    onPress(item.id);
  }, [item.id, onPress]);

  return (
    <TouchableOpacity onPress={handlePress}>
      <Text>{item.title}</Text>
    </TouchableOpacity>
  );
});

```

---

## Q55. 🔧 Optimizing `renderItem` functions

Use onEndReached to detect when user reaches the end of the list and load more data - provide smooth pagination experience (user experience). Triggered when user reaches the end (onEndReached).

- **Trade-offs**: The catch is handle loading states during pagination (loading states) - append new data to existing data (data management). Provide smooth pagination experience (user experience), but watch out - controls when onEndReached is triggered (onEndReachedThreshold).

Example:

```jsx
function PaginatedList() {
  const [data, setData] = useState([]);
  const [loading, setLoading] = useState(false);
  const [page, setPage] = useState(1);

  const loadMoreData = useCallback(async () => {
    if (loading) return;
    setLoading(true);
    const newData = await fetchData(page);
    setData(prev => [...prev, ...newData]);
    setPage(prev => prev + 1);
    setLoading(false);
  }, [page, loading]);

  return (
    <FlatList
      data={data}
      renderItem={renderItem}
      onEndReached={loadMoreData}
      onEndReachedThreshold={0.5}
    />
  );
}

```

---

## Q52. 🔧 Implementing pagination with `onEndReached`

removeClippedSubviews removes off-screen views from the native view hierarchy, reducing memory usage - especially useful for large lists with complex items (use cases). Removes off-screen views from native hierarchy (memory reduction).

- **Trade-offs**: The catch is works on both iOS and Android (platform support) - may cause slight delays when scrolling back. Especially useful for large lists with complex items (use cases), but watch out - improves memory usage and performance (performance).

Example:

```jsx
function MemoryOptimizedList({ data }) {
  return (
    <FlatList
      data={data}
      renderItem={renderItem}
      keyExtractor={item => item.id}
      removeClippedSubviews={true}
    />
  );
}

```

---

## Q53. ⚡ Using `removeClippedSubviews` for performance

removeClippedSubviews removes off-screen views from the native view hierarchy, reducing memory usage - especially useful for large lists with complex items (use cases). Removes off-screen views from native hierarchy (memory reduction).

- **Trade-offs**: The catch is works on both iOS and Android (platform support) - may cause slight delays when scrolling back. Especially useful for large lists with complex items (use cases), but watch out - improves memory usage and performance (performance).

Example:

```jsx
function MemoryOptimizedList({ data }) {
  return (
    <FlatList
      data={data}
      renderItem={renderItem}
      keyExtractor={item => item.id}
      removeClippedSubviews={true}
    />
  );
}

```

---

## Q54. 🔍 Using Xcode Instruments for iOS performance profiling

Xcode Instruments provides tools like Time Profiler, Allocations, and Leaks to analyze iOS app performance - essential for identifying performance bottlenecks on iOS. Time Profiler (identifies CPU bottlenecks), Allocations (tracks memory allocations), Leaks (detects memory leaks).

- **Trade-offs**: The catch is requires macOS and Xcode (platform requirement) - provides detailed performance insights (detailed analysis). Essential for identifying performance bottlenecks on iOS, but watch out - use Instruments to profile React Native apps (React Native profiling).

Example:

```bash
# Using Xcode Instruments
# 6. Open Xcode
# 6. Product > Profile (Cmd+I)
# 6. Select Time Profiler or Allocations
# 6. Record and analyze performance data

# Time Profiler shows:
# - CPU usage by function
# - Call tree with time spent
# - Hot spots in JavaScript and native code

# Allocations shows:
# - Memory allocations over time
# - Object retention
# - Memory growth patterns
```

---

## Q55. 🔍 Using Android Studio Profiler for Android performance profiling

Android Studio Profiler provides CPU, Memory, and Network profiling tools to analyze Android app performance - essential for identifying performance bottlenecks on Android. CPU Profiler (identifies CPU bottlenecks), Memory Profiler (tracks memory usage), Network Profiler (monitors network activity).

- **Trade-offs**: The catch is requires Android Studio (platform requirement) - provides real-time performance data (real-time analysis). Essential for identifying performance bottlenecks on Android, but watch out - use Profiler to profile React Native apps (React Native profiling).

Example:

```bash
# Using Android Studio Profiler
# 6. Open Android Studio
# 6. View > Tool Windows > Profiler
# 6. Select CPU, Memory, or Network
# 6. Record and analyze performance data

# CPU Profiler shows:
# - CPU usage by thread
# - Method call traces
# - JavaScript and native thread activity

# Memory Profiler shows:
# - Heap allocations
# - Object references
# - Memory leaks detection
```

---

## Q52. 🐛 Profiling memory leaks in React Native apps

Use profiling tools to identify memory leaks by tracking object retention, analyzing heap dumps, and monitoring memory growth over time - memory leaks cause app crashes and poor performance. Track object retention (object retention), Analyze heap dumps (heap analysis), Monitor memory growth (memory monitoring).

- **Trade-offs**: The catch is use Xcode Instruments Leaks tool for iOS (iOS profiling) - use Android Studio Memory Profiler for Android (Android profiling). Memory leaks cause app crashes and poor performance, but watch out - identify common leak patterns (leak patterns).

Example:

```jsx
// Common memory leak patterns to avoid
function LeakyComponent() {
  const [data, setData] = useState([]);

  useEffect(() => {
    // ❌ Leak: Event listener not cleaned up
    const subscription = EventEmitter.addListener('event', handleEvent);
    // Missing cleanup
    return () => subscription.remove(); // ✅ Cleanup
  }, []);

  useEffect(() => {
    // ❌ Leak: Timer not cleared
    const timer = setInterval(() => {
      // Do something
    }, 1000);
    return () => clearInterval(timer); // ✅ Cleanup
  }, []);
}

```

---

## Q59. 🔍 Analyzing native crash logs and stack traces

Native crashes require analyzing platform-specific crash logs, symbolication, and understanding native stack traces - critical for debugging native module issues. Android crash logs (logcat and crash reports), iOS crash logs (crash reports and symbolicated logs), Symbolication (converting addresses to readable function names).

- **Trade-offs**: The catch is requires understanding native code (native knowledge) - different tools for iOS and Android (platform differences). Critical for debugging native module issues, but watch out - use crash reporting tools like Sentry (crash reporting).

Example:

```bash
# Android crash log analysis
adb logcat | grep -i "fatal\|crash\|exception"

# iOS crash log analysis
# 6. Xcode > Window > Devices and Simulators
# 6. Select device > View Device Logs
# 6. Find crash report and symbolicate

# Common native crash causes:
# - Null pointer exceptions
# - Memory access violations
# - Native module errors
# - Threading issues
```

---

## Q60. ⚡ Optimizing JavaScript bundle size and startup time

Use code splitting, tree shaking, Hermes bytecode compilation, and lazy loading to reduce bundle size and improve startup time - smaller bundles load faster. Code splitting (split code into smaller chunks), Tree shaking (remove unused code), Hermes bytecode (pre-compiled JavaScript), Lazy loading (load code on demand).

- **Trade-offs**: The catch is analyze bundle size with Metro bundler (bundle analysis) - use Hermes for better startup performance (Hermes). Smaller bundles load faster, but watch out - balance between bundle size and runtime performance (performance balance).

Example:

```jsx
// Lazy loading components
const LazyComponent = React.lazy(() => import('./LazyComponent'));

function App() {
  return (
    <Suspense fallback={<Loading />}>
      <LazyComponent />
    </Suspense>
  );
}

// Metro config for bundle optimization
// metro.config.js
module.exports = {
  transformer: {
    getTransformOptions: async () => ({
      transform: {
        experimentalImportSupport: false,
        inlineRequires: true, // Reduces bundle size
      },
    }),
  },
};

```

---

## Q61. ⚡ Common performance issues in React Native

Common causes include unnecessary re-renders, heavy operations on the main thread, memory leaks, and inefficient list rendering - identify and fix these issues systematically. Components re-rendering when they shouldn't (unnecessary re-renders), heavy operations blocking the UI thread (main thread blocking).

- **Trade-offs**: The catch is not optimizing image loading and caching (image loading) - bridge communication bottlenecks. Identify and fix these issues systematically, but watch out - objects not being properly cleaned up (memory leaks), using ScrollView instead of FlatList for large lists (inefficient lists).

Example:

```jsx
// ❌ Performance issues
function BadList({ data }) {
  return (
    <ScrollView>
      {data.map(item => (
        <View key={item.id}>
          <Text>{item.name}</Text>
        </View>
      ))}
    </ScrollView>
  );
}

// ✅ Better: Use FlatList
function GoodList({ data }) {
  return (
    <FlatList
      data={data}
      renderItem={({ item }) => <Text>{item.name}</Text>}
      keyExtractor={item => item.id}
    />
  );
}

```

---

## Q62. ⚡ Hermes engine and how it improves performance

Hermes is a JavaScript engine optimized for mobile, providing faster startup times and reduced memory usage - smaller bundle sizes with Hermes. Optimized for mobile app startup (faster startup).

- **Trade-offs**: The catch is pre-compiles JavaScript to bytecode (bytecode compilation) - optimized garbage collection for mobile (garbage collection). Smaller bundle sizes with Hermes, but watch out - reduced memory usage compared to V8 (memory efficiency).

Example:

```jsx
// Hermes configuration in metro.config.js
module.exports = {
  transformer: {
    getTransformOptions: async () => ({
      transform: {
        experimentalImportSupport: false,
        inlineRequires: true,
      },
    }),
  },
};

```

---

---

## 📍 Navigation

<div align="center">

[Platform-Specific Development](05%29%20Platform-Specific%20Development.md) • [Home: README](../README.md) • [Animations & Graphics →](07%29%20Animations%20%26%20Graphics.md)

[📋 Cheatsheet](React%20Native%20Interview%20Cheatsheet.md)

</div>

---
