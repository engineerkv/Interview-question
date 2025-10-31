# 🚀 5. Performance Optimization & Measurement (Q41–50)

---

## 41) What are the most common causes of React Native performance issues?

Concept:
Common causes include unnecessary re-renders, heavy operations on the main thread, memory leaks, and inefficient list rendering.

Example:
```jsx
// ❌ Performance issues
function BadList({ data }) {
  return (
    <ScrollView>
      {data.map(item => (
        <View key={item.id}>
```

Deep Insight:
- **Unnecessary Re-renders**: Components re-rendering when they shouldn't
- **Main Thread Blocking**: Heavy operations blocking the UI thread
- **Memory Leaks**: Objects not being properly cleaned up
- **Inefficient Lists**: Using ScrollView instead of FlatList for large lists
- **Image Loading**: Not optimizing image loading and caching

---

## 42) How does the **Hermes engine** improve runtime performance?

Concept:
Hermes is a JavaScript engine optimized for mobile, providing faster startup times and reduced memory usage.

Example:
```jsx
// Hermes configuration in metro.config.js
module.exports = {
  transformer: {
    getTransformOptions: async () => ({
      transform: {
        experimentalImportSupport: false,
```

Deep Insight:
- **Faster Startup**: Optimized for mobile app startup
- **Memory Efficiency**: Reduced memory usage compared to V8
- **Bytecode Compilation**: Pre-compiles JavaScript to bytecode
- **Garbage Collection**: Optimized garbage collection for mobile
- **Bundle Size**: Smaller bundle sizes with Hermes

---

## 43) How can you measure app performance (Flipper, Profiler, Perf Monitor)?

Concept:
Use Flipper, React Native Profiler, and performance monitoring tools to measure and analyze app performance.

Example:
```jsx
// Performance monitoring
import { Performance } from 'react-native-performance';

function MyComponent() {
  useEffect(() => {
    const startTime = Performance.now();
```

Deep Insight:
- **Flipper**: Comprehensive debugging and performance monitoring
- **React Native Profiler**: Built-in performance profiling
- **Performance.now()**: High-resolution timing measurements
- **Memory Monitoring**: Track memory usage and leaks
- **Network Monitoring**: Monitor network performance

---

## 44) What is **virtualization** in FlatList, and how does it work?

Concept:
Virtualization renders only visible items in FlatList, improving performance by reducing memory usage and rendering overhead.

Example:
```jsx
function VirtualizedList({ data }) {
  const renderItem = useCallback(({ item }) => (
    <View style={styles.item}>
      <Text>{item.title}</Text>
    </View>
  ), []);
```

Deep Insight:
- **Visible Items Only**: Only renders items currently visible
- **Memory Efficiency**: Reduces memory usage for large lists
- **Performance**: Improves scrolling performance
- **Configuration**: Various props to optimize virtualization
- **Platform Support**: Works on both iOS and Android

---

## 45) What is the difference between **FlatList** and **ScrollView**?

Concept:
FlatList is optimized for large lists with virtualization, while ScrollView renders all children and is better for small, static content.

Example:
```jsx
// ScrollView - renders all children
function ScrollViewExample({ data }) {
  return (
    <ScrollView>
      {data.map(item => (
        <View key={item.id}>
```

Deep Insight:
- **ScrollView**: Renders all children, good for small lists
- **FlatList**: Virtualized rendering, good for large lists
- **Performance**: FlatList is more performant for large datasets
- **Memory Usage**: FlatList uses less memory for large lists
- **Use Cases**: Choose based on data size and performance requirements

---

## 46) How do `getItemLayout`, `initialNumToRender`, and `windowSize` affect FlatList performance?

Concept:
These props optimize FlatList rendering by providing layout information, controlling initial render count, and setting the render window size.

Example:
```jsx
function OptimizedFlatList({ data }) {
  const getItemLayout = useCallback((data, index) => ({
    length: ITEM_HEIGHT,
    offset: ITEM_HEIGHT * index,
    index,
  }), []);
```

Deep Insight:
- **getItemLayout**: Provides item dimensions for better performance
- **initialNumToRender**: Controls how many items render initially
- **windowSize**: Sets the render window size
- **Performance Impact**: These props significantly impact performance
- **Optimization**: Use these props to optimize for your specific use case

---

## 47) How can you prevent unnecessary re-renders inside a FlatList's `renderItem`?

Concept:
Use React.memo, useMemo, and useCallback to optimize renderItem functions and prevent unnecessary re-renders.

Example:
```jsx
const ListItem = React.memo(({ item, onPress }) => {
  const handlePress = useCallback(() => {
    onPress(item.id);
  }, [item.id, onPress]);
  
  return (
```

Deep Insight:
- **React.memo**: Prevents re-renders when props haven't changed
- **useCallback**: Memoizes callback functions
- **useMemo**: Memoizes expensive calculations
- **Performance**: These optimizations improve FlatList performance
- **Best Practices**: Use these patterns for FlatList optimization

---

## 48) How do you implement pagination with `onEndReached` in FlatList?

Concept:
Use onEndReached to detect when user reaches the end of the list and load more data.

Example:
```jsx
function PaginatedList() {
  const [data, setData] = useState([]);
  const [loading, setLoading] = useState(false);
  const [page, setPage] = useState(1);
  
  const loadMoreData = useCallback(async () => {
```

Deep Insight:
- **onEndReached**: Triggered when user reaches the end
- **onEndReachedThreshold**: Controls when onEndReached is triggered
- **Loading States**: Handle loading states during pagination
- **Data Management**: Append new data to existing data
- **User Experience**: Provide smooth pagination experience

---

## 49) How does `removeClippedSubviews` improve memory usage in lists?

Concept:
removeClippedSubviews removes off-screen views from the native view hierarchy, reducing memory usage.

Example:
```jsx
function MemoryOptimizedList({ data }) {
  return (
    <FlatList
      data={data}
      renderItem={renderItem}
      keyExtractor={item => item.id}
```

Deep Insight:
- **Memory Reduction**: Removes off-screen views from native hierarchy
- **Performance**: Improves memory usage and performance
- **Platform Support**: Works on both iOS and Android
- **Trade-offs**: May cause slight delays when scrolling back
- **Use Cases**: Especially useful for large lists with complex items

---

## 50) What are the benefits of using **Fabric Renderer** for UI performance?

Concept:
Fabric provides synchronous rendering, better performance, and improved debugging capabilities.

Example:
```jsx
// Fabric enables synchronous rendering
function FabricComponent() {
  const [count, setCount] = useState(0);
  
  const handlePress = () => {
    setCount(count + 1);
```

Deep Insight:
- **Synchronous Rendering**: Enables synchronous UI updates
- **Better Performance**: Improved rendering performance
- **Debugging**: Better debugging capabilities
- **New Architecture**: Part of React Native's new architecture
- **Future-Proof**: Foundation for future React Native features

---
