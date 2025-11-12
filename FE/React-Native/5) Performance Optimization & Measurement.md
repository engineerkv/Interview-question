# 🚀 5. Performance Optimization & Measurement (Q41–50)

---

## 🧩 Q41. What are the most common causes of React Native performance issues?

### 🧠 Concept

Common causes include unnecessary re-renders, heavy operations on the main thread, memory leaks, and inefficient list rendering. Identify and fix these issues systematically.

---

### 💡 Example

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

### 🔍 Deep Insights

* **Rule:** Components re-rendering when they shouldn't (unnecessary re-renders), heavy operations blocking the UI thread (main thread blocking).
* **Use Case:** Objects not being properly cleaned up (memory leaks), using ScrollView instead of FlatList for large lists (inefficient lists).
* **Common Mistake:** Not optimizing image loading and caching (image loading).
* **Pro Tip:** Bridge communication bottlenecks.

---

### ⭐ Senior Takeaway

Identify and fix these issues systematically.

---

## 🧩 Q42. How does the Hermes engine improve runtime performance?

### 🧠 Concept

Hermes is a JavaScript engine optimized for mobile, providing faster startup times and reduced memory usage. Smaller bundle sizes with Hermes.

---

### 💡 Example

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

### 🔍 Deep Insights

* **Rule:** Optimized for mobile app startup (faster startup).
* **Use Case:** Reduced memory usage compared to V8 (memory efficiency).
* **Common Mistake:** Pre-compiles JavaScript to bytecode (bytecode compilation).
* **Pro Tip:** Optimized garbage collection for mobile (garbage collection).

---

### ⭐ Senior Takeaway

Smaller bundle sizes with Hermes.

---

## 🧩 Q43. How can you measure app performance?

### 🧠 Concept

Use Flipper, React Native Profiler, and performance monitoring tools to measure and analyze app performance. Use multiple tools for comprehensive analysis.

---

### 💡 Example

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

### 🔍 Deep Insights

* **Rule:** Flipper (comprehensive debugging and performance monitoring), React Native Profiler (built-in performance profiling).
* **Use Case:** High-resolution timing measurements (performance.now()).
* **Common Mistake:** Track memory usage and leaks (memory monitoring).
* **Pro Tip:** Monitor network performance (network monitoring).

---

### ⭐ Senior Takeaway

Use multiple tools for comprehensive analysis.

---

## 🧩 Q44. What is virtualization in FlatList and how does it work?

### 🧠 Concept

Virtualization renders only visible items in FlatList, improving performance by reducing memory usage and rendering overhead. Works on both iOS and Android (platform support).

---

### 💡 Example

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

### 🔍 Deep Insights

* **Rule:** Only renders items currently visible (visible items only).
* **Use Case:** Reduces memory usage for large lists (memory efficiency).
* **Common Mistake:** Improves scrolling performance (performance).
* **Pro Tip:** Various props to optimize virtualization (configuration).

---

### ⭐ Senior Takeaway

Works on both iOS and Android (platform support).

---

## 🧩 Q45. What is the difference between FlatList and ScrollView?

### 🧠 Concept

FlatList is optimized for large lists with virtualization, while ScrollView renders all children and is better for small, static content. FlatList is preferred for dynamic lists.

---

### 💡 Example

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

### 🔍 Deep Insights

* **Rule:** ScrollView renders all children, good for small lists; FlatList uses virtualized rendering, good for large lists.
* **Use Case:** FlatList is more performant for large datasets (performance).
* **Common Mistake:** FlatList uses less memory for large lists (memory usage).
* **Pro Tip:** Choose based on data size and performance requirements (use cases).

---

### ⭐ Senior Takeaway

FlatList is preferred for dynamic lists.

---

## 🧩 Q46. How do FlatList optimization props work?

### 🧠 Concept

Props like `getItemLayout`, `initialNumToRender`, and `windowSize` optimize FlatList rendering by providing layout information, controlling initial render count, and setting the render window size. These props are key to FlatList optimization.

---

### 💡 Example

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

### 🔍 Deep Insights

* **Rule:** `getItemLayout` provides item dimensions for better performance, `initialNumToRender` controls how many items render initially, `windowSize` sets the render window size.
* **Use Case:** These props significantly impact performance (performance impact).
* **Common Mistake:** Use these props to optimize for your specific use case (optimization).
* **Pro Tip:** Fine-tune rendering for best performance.

---

### ⭐ Senior Takeaway

These props are key to FlatList optimization.

---

## 🧩 Q47. How can you prevent unnecessary re-renders in FlatList?

### 🧠 Concept

Use React.memo, useMemo, and useCallback to optimize renderItem functions and prevent unnecessary re-renders. Memoization is critical for FlatList performance.

---

### 💡 Example

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

### 🔍 Deep Insights

* **Rule:** React.memo prevents re-renders when props haven't changed, useCallback memoizes callback functions, useMemo memoizes expensive calculations.
* **Use Case:** These optimizations improve FlatList performance (performance).
* **Common Mistake:** Use these patterns for FlatList optimization (best practices).
* **Pro Tip:** Combine multiple optimizations for best results.

---

### ⭐ Senior Takeaway

Memoization is critical for FlatList performance.

---

## 🧩 Q48. How do you implement pagination with `onEndReached`?

### 🧠 Concept

Use onEndReached to detect when user reaches the end of the list and load more data. Provide smooth pagination experience (user experience).

---

### 💡 Example

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

### 🔍 Deep Insights

* **Rule:** Triggered when user reaches the end (onEndReached).
* **Use Case:** Controls when onEndReached is triggered (onEndReachedThreshold).
* **Common Mistake:** Handle loading states during pagination (loading states).
* **Pro Tip:** Append new data to existing data (data management).

---

### ⭐ Senior Takeaway

Provide smooth pagination experience (user experience).

---

## 🧩 Q49. How does `removeClippedSubviews` improve memory usage?

### 🧠 Concept

removeClippedSubviews removes off-screen views from the native view hierarchy, reducing memory usage. Especially useful for large lists with complex items (use cases).

---

### 💡 Example

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

### 🔍 Deep Insights

* **Rule:** Removes off-screen views from native hierarchy (memory reduction).
* **Use Case:** Improves memory usage and performance (performance).
* **Common Mistake:** Works on both iOS and Android (platform support).
* **Pro Tip:** May cause slight delays when scrolling back.

---

### ⭐ Senior Takeaway

Especially useful for large lists with complex items (use cases).

---

## 🧩 Q50. What are the benefits of using Fabric Renderer?

### 🧠 Concept

Fabric provides synchronous rendering, better performance, and improved debugging capabilities. Fabric is the future of React Native rendering.

---

### 💡 Example

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

### 🔍 Deep Insights

* **Rule:** Enables synchronous UI updates (synchronous rendering), improved rendering performance (better performance).
* **Use Case:** Better debugging capabilities (debugging).
* **Common Mistake:** Part of React Native's new architecture (new architecture).
* **Pro Tip:** Foundation for future React Native features (future-proof).

---

### ⭐ Senior Takeaway

Fabric is the future of React Native rendering.

---
