# 🚀 5. Performance Optimization & Measurement (Q41–50)

---

## 41) What are the most common causes of React Native performance issues?

Common causes include unnecessary re-renders, heavy operations on the main thread, memory leaks, and inefficient list rendering.

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

- **Common Issues**: Components re-rendering when they shouldn't (unnecessary re-renders), heavy operations blocking the UI thread (main thread blocking)
- **Real-World Problems**: Objects not being properly cleaned up (memory leaks), using ScrollView instead of FlatList for large lists (inefficient lists)
- **Common Mistake**: Not optimizing image loading and caching (image loading)
- **Advanced Issue**: Bridge communication bottlenecks
- **Interview Tip**: Explain that identify and fix these issues systematically

---

## 42) How does the **Hermes engine** improve runtime performance?

Hermes is a JavaScript engine optimized for mobile, providing faster startup times and reduced memory usage.

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

- **Core Benefit**: Optimized for mobile app startup (faster startup)
- **Real-World Impact**: Reduced memory usage compared to V8 (memory efficiency)
- **Common Advantage**: Pre-compiles JavaScript to bytecode (bytecode compilation)
- **Advanced Feature**: Optimized garbage collection for mobile (garbage collection)
- **Interview Tip**: Explain that smaller bundle sizes with Hermes

---

## 43) How can you measure app performance (Flipper, Profiler, Perf Monitor)?

Use Flipper, React Native Profiler, and performance monitoring tools to measure and analyze app performance.

```jsx
import { Performance } from 'react-native-performance';

function MyComponent() {
  useEffect(() => {
    const startTime = Performance.now();
    // Operation
    const endTime = Performance.now();
    console.log(`Operation took ${endTime - startTime}ms`);
  }, []);
}
```

- **Core Tools**: Flipper (comprehensive debugging and performance monitoring), React Native Profiler (built-in performance profiling)
- **Real-World Use**: High-resolution timing measurements (performance.now())
- **Common Practice**: Track memory usage and leaks (memory monitoring)
- **Advanced Feature**: Monitor network performance (network monitoring)
- **Interview Tip**: Explain that use multiple tools for comprehensive analysis

---

## 44) What is **virtualization** in FlatList, and how does it work?

Virtualization renders only visible items in FlatList, improving performance by reducing memory usage and rendering overhead.

```jsx
function VirtualizedList({ data }) {
  const renderItem = useCallback(({ item }) => (
    <View style={styles.item}>
      <Text>{item.title}</Text>
    </View>
  ), []);
  
  return (
    <FlatList
      data={data}
      renderItem={renderItem}
      keyExtractor={item => item.id}
    />
  );
}
```

- **Core Concept**: Only renders items currently visible (visible items only)
- **Real-World Benefit**: Reduces memory usage for large lists (memory efficiency)
- **Common Advantage**: Improves scrolling performance (performance)
- **Advanced Feature**: Various props to optimize virtualization (configuration)
- **Interview Tip**: Explain that works on both iOS and Android (platform support)

---

## 45) What is the difference between **FlatList** and **ScrollView**?

FlatList is optimized for large lists with virtualization, while ScrollView renders all children and is better for small, static content.

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

- **Core Difference**: ScrollView renders all children, good for small lists; FlatList uses virtualized rendering, good for large lists
- **Real-World Impact**: FlatList is more performant for large datasets (performance)
- **Common Advantage**: FlatList uses less memory for large lists (memory usage)
- **Advanced Feature**: Choose based on data size and performance requirements (use cases)
- **Interview Tip**: Explain that FlatList is preferred for dynamic lists

---

## 46) How do `getItemLayout`, `initialNumToRender`, and `windowSize` affect FlatList performance?

These props optimize FlatList rendering by providing layout information, controlling initial render count, and setting the render window size.

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

- **Core Props**: `getItemLayout` provides item dimensions for better performance, `initialNumToRender` controls how many items render initially, `windowSize` sets the render window size
- **Real-World Impact**: These props significantly impact performance (performance impact)
- **Common Practice**: Use these props to optimize for your specific use case (optimization)
- **Advanced Feature**: Fine-tune rendering for best performance
- **Interview Tip**: Explain that these props are key to FlatList optimization

---

## 47) How can you prevent unnecessary re-renders inside a FlatList's `renderItem`?

Use React.memo, useMemo, and useCallback to optimize renderItem functions and prevent unnecessary re-renders.

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

- **Core Optimizations**: React.memo prevents re-renders when props haven't changed, useCallback memoizes callback functions, useMemo memoizes expensive calculations
- **Real-World Impact**: These optimizations improve FlatList performance (performance)
- **Common Practice**: Use these patterns for FlatList optimization (best practices)
- **Advanced Feature**: Combine multiple optimizations for best results
- **Interview Tip**: Explain that memoization is critical for FlatList performance

---

## 48) How do you implement pagination with `onEndReached` in FlatList?

Use onEndReached to detect when user reaches the end of the list and load more data.

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

- **Core Feature**: Triggered when user reaches the end (onEndReached)
- **Real-World Use**: Controls when onEndReached is triggered (onEndReachedThreshold)
- **Common Practice**: Handle loading states during pagination (loading states)
- **Advanced Feature**: Append new data to existing data (data management)
- **Interview Tip**: Explain that provide smooth pagination experience (user experience)

---

## 49) How does `removeClippedSubviews` improve memory usage in lists?

removeClippedSubviews removes off-screen views from the native view hierarchy, reducing memory usage.

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

- **Core Feature**: Removes off-screen views from native hierarchy (memory reduction)
- **Real-World Benefit**: Improves memory usage and performance (performance)
- **Common Advantage**: Works on both iOS and Android (platform support)
- **Trade-off**: May cause slight delays when scrolling back
- **Interview Tip**: Explain that especially useful for large lists with complex items (use cases)

---

## 50) What are the benefits of using **Fabric Renderer** for UI performance?

Fabric provides synchronous rendering, better performance, and improved debugging capabilities.

```jsx
// Fabric enables synchronous rendering
function FabricComponent() {
  const [count, setCount] = useState(0);
  
  const handlePress = () => {
    setCount(count + 1);
    // UI updates synchronously with Fabric
  };
  
  return (
    <View>
      <Text>{count}</Text>
      <Button title="Increment" onPress={handlePress} />
    </View>
  );
}
```

- **Core Benefits**: Enables synchronous UI updates (synchronous rendering), improved rendering performance (better performance)
- **Real-World Advantage**: Better debugging capabilities (debugging)
- **Advanced Feature**: Part of React Native's new architecture (new architecture)
- **Future**: Foundation for future React Native features (future-proof)
- **Interview Tip**: Explain that Fabric is the future of React Native rendering

---
