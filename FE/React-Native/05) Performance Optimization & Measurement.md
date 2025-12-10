# 5. Performance Optimization & Measurement (Q41–50)

---

## 📍 Navigation

<div align="center">

[Navigation & Lifecycle](04%29%20Navigation%20%26%20Lifecycle.md) • [Home: README](../README.md) • [State Management & Data Handling →](06%29%20State%20Management%20%26%20Data%20Handling.md)

[📋 Cheatsheet](React%20Native%20Interview%20Cheatsheet.md)

</div>

---

---

## Q41. ⚡ Common performance issues in React Native

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

## Q42. ⚡ Hermes engine and how it improves performance

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

## Q43. ⚡ Measuring performance in React Native apps

Use Flipper, React Native Profiler, and performance monitoring tools to measure and analyze app performance - use multiple tools for comprehensive analysis. Flipper (comprehensive debugging and performance monitoring), React Native Profiler (built-in performance profiling).

- **Trade-offs**: The catch is track memory usage and leaks (memory monitoring) - monitor network performance (network monitoring). Use multiple tools for comprehensive analysis, but watch out - high-resolution timing measurements (performance.now()).

Example:

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

---

## Q44. 🐛 Using Flipper for debugging React Native apps

Virtualization renders only visible items in FlatList, improving performance by reducing memory usage and rendering overhead - works on both iOS and Android (platform support). Only renders items currently visible (visible items only).

- **Trade-offs**: The catch is improves scrolling performance (performance) - various props to optimize virtualization (configuration). Works on both iOS and Android (platform support), but watch out - reduces memory usage for large lists (memory efficiency).

Example:

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

---

## Q45. 💡 Optimizing FlatList for large datasets

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

## Q46. 🤔 Difference between FlatList and ScrollView

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

## Q47. 📱 Implementing virtualization in React Native

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

## Q48. 🔧 Optimizing `renderItem` functions

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

## Q49. 🔧 Implementing pagination with `onEndReached`

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

## Q50. ⚡ Using `removeClippedSubviews` for performance

Fabric provides synchronous rendering, better performance, and improved debugging capabilities - Fabric is the future of React Native rendering. Enables synchronous UI updates (synchronous rendering), improved rendering performance (better performance).

- **Trade-offs**: The catch is part of React Native's new architecture (new architecture) - foundation for future React Native features (future-proof). Fabric is the future of React Native rendering, but watch out - better debugging capabilities (debugging).

Example:

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

---

---

## 📍 Navigation

<div align="center">

[Navigation & Lifecycle](04%29%20Navigation%20%26%20Lifecycle.md) • [Home: README](../README.md) • [State Management & Data Handling →](06%29%20State%20Management%20%26%20Data%20Handling.md)

[📋 Cheatsheet](React%20Native%20Interview%20Cheatsheet.md)

</div>

---
