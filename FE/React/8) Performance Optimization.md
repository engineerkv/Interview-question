# 🚀 8. Performance Optimization (Q67–80)

---

## 67) What are the most common causes of re-renders in React?

Concept:
Common causes include state changes, prop changes, parent re-renders, context value changes, and unnecessary effect dependencies.

Example:
```jsx
function App() {
  const [count, setCount] = useState(0);
  const [name, setName] = useState('');
  
  // ❌ Causes re-render on every render
  const expensiveValue = expensiveCalculation();
  return <div>{expensiveValue} {name} {count}</div>;
}
```

Deep Insight:
- **State Changes**: Any state change triggers re-render
- **Prop Changes**: New prop values cause child re-renders
- **Parent Re-renders**: Parent re-render causes all children to re-render
- **Context Changes**: Context value changes cause all consumers to re-render
- **Object Creation**: Creating objects/functions in render causes re-renders

---

## 82) How do you prevent unnecessary re-renders in React components?

Concept:
Use React.memo, useMemo, useCallback, proper dependency arrays, and avoid creating objects/functions in render methods.

Example:
```jsx
// ✅ Optimized component
const ExpensiveChild = React.memo(({ user, onUpdate }) => {
  const expensiveValue = useMemo(() => {
    return expensiveCalculation(user);
  }, [user]);
  return <div>{expensiveValue}</div>;
});
```

Deep Insight:
- **React.memo**: Prevents re-render if props haven't changed
- **useMemo**: Memoizes expensive calculations
- **useCallback**: Memoizes callback functions
- **Dependency Arrays**: Proper dependencies prevent unnecessary effects
- **Object Creation**: Avoid creating objects/functions in render

---

## 82) What is memoization in React (`React.memo`, `useMemo`, `useCallback`)?

Concept:
Memoization is a technique to cache expensive calculations and prevent unnecessary re-renders by remembering previous results.

Example:
```jsx
// React.memo - memoizes component
const ExpensiveComponent = React.memo(({ data, onUpdate }) => {
  // useMemo - memoizes expensive calculation
  const processedData = useMemo(() => {
    console.log('Processing data...');
    return data.map(item => ({ id: item.id, name: item.name.toUpperCase() }));
  }, [data]);
  
  // useCallback - memoizes callback
  const handleUpdate = useCallback(() => onUpdate(processedData), [onUpdate, processedData]);
  
  return <button onClick={handleUpdate}>Update</button>;
});
```

Deep Insight:
- **React.memo**: Memoizes component based on props
- **useMemo**: Memoizes computed values based on dependencies
- **useCallback**: Memoizes callback functions based on dependencies
- **Performance**: Prevents unnecessary calculations and re-renders
- **Overuse**: Don't memoize everything, only when needed

---

## 82) What is code-splitting and how is it implemented using `React.lazy()` and `Suspense`?

Concept:
Code-splitting splits code into smaller chunks loaded on demand, implemented with React.lazy() for dynamic imports and Suspense for loading states.

Example:
```jsx
import { Suspense, lazy } from 'react';

// Lazy load components
const LazyComponent = lazy(() => import('./LazyComponent'));
const AnotherLazyComponent = lazy(() => import('./AnotherLazyComponent'));
 
function App() {
  return (
    <Suspense fallback={<div>Loading...</div>}>
      <LazyComponent />
      <AnotherLazyComponent />
    </Suspense>
  );
}
```

Deep Insight:
- **Dynamic Imports**: Code is loaded only when needed
- **Bundle Splitting**: Reduces initial bundle size
- **Loading States**: Suspense provides loading UI
- **Performance**: Improves initial page load time
- **Use Cases**: Route-based splitting, feature-based splitting

---

## 82) What is tree-shaking and how does React support it?

Concept:
Tree-shaking removes unused code from bundles, supported by React's modular architecture and ES6 module system.

Example:
```jsx
// ✅ Tree-shakeable imports
import { useState, useEffect } from 'react';
import { debounce } from 'lodash-es';

// ❌ Non-tree-shakeable imports
import * as React from 'react';
```

Deep Insight:
- **ES6 Modules**: Enables tree-shaking through static analysis
- **Named Exports**: Better for tree-shaking than default exports
- **Dead Code Elimination**: Removes unused code from bundles
- **Bundle Size**: Reduces final bundle size
- **Build Tools**: Webpack, Rollup, and other bundlers support tree-shaking

---

## 82) How do you measure performance using the React Profiler?

Concept:
Use the React Profiler in DevTools to measure component render times, identify slow components, and analyze performance bottlenecks.

Example:
```jsx
import { Profiler } from 'react';

function onRenderCallback(id, phase, actualDuration, baseDuration, startTime, commitTime) {
  console.log('Profiler:', {
    id,
    phase,
    actualDuration,
    baseDuration,
    startTime,
    commitTime
  });
}

function App() {
  return (
    <Profiler id="App" onRender={onRenderCallback}>
      <div>App</div>
    </Profiler>
  );
}
```

Deep Insight:
- **Performance Measurement**: Measures component render times
- **Development Tool**: Primarily used during development
- **Optimization**: Helps identify performance bottlenecks
- **Profiling Data**: Provides detailed timing information
- **Production**: Can be used in production for monitoring

---

## 82) How do you measure app performance using Chrome DevTools (Performance, Memory tab)?

Concept:
Use Chrome DevTools Performance tab for runtime analysis and Memory tab for memory usage patterns and leak detection.

Example:
```jsx
// Performance measurement
function measurePerformance() {
  const start = performance.now();
  
  // Your code here
  expensiveOperation();
  const end = performance.now();
  console.log(`Operation took ${end - start}ms`);
}
```

Deep Insight:
- **Performance Tab**: Analyze runtime performance and bottlenecks
- **Memory Tab**: Detect memory leaks and usage patterns
- **Heap Snapshots**: Compare memory usage over time
- **Timeline**: Track performance metrics over time
- **Best Practices**: Use for identifying and fixing performance issues

---

## 82) What are Core Web Vitals and how can you improve them in React apps?

Concept:
Core Web Vitals are LCP, FID, and CLS metrics that measure user experience, improved through performance optimization and best practices.

Example:
```jsx
// Optimize LCP (Largest Contentful Paint)
function OptimizedImage({ src, alt }) {
  return (
    <img
      src={src}
      alt={alt}
      loading="eager"
      width={800}
      height={600}
    />
  );
}
```

Deep Insight:
- **LCP**: Largest Contentful Paint - load critical content quickly
- **FID**: First Input Delay - keep main thread responsive
- **CLS**: Cumulative Layout Shift - prevent unexpected layout shifts
- **Optimization**: Use lazy loading, code splitting, and proper sizing
- **Monitoring**: Use tools like Lighthouse and Web Vitals

---

## 82) How do Lighthouse and Web Vitals metrics (TTFB, LCP, FID, CLS) apply to React?

Concept:
These metrics measure different aspects of performance, with React-specific optimizations for each metric to improve user experience.

Example:
```jsx
// TTFB (Time to First Byte) optimization
function App() {
  const [data, setData] = useState(null);
  
  useEffect(() => {
    // Preload critical data
    fetch('/api/critical-data').then(r => r.json()).then(setData);
  }, []);
  
  return <div>{data ? data.title : 'Loading...'}</div>;
}
```

Deep Insight:
- **TTFB**: Server response time - optimize API calls and server performance
- **LCP**: Largest content paint - optimize critical rendering path
- **FID**: First input delay - keep main thread responsive
- **CLS**: Layout shift - prevent unexpected layout changes
- **React Specific**: Use React features like Suspense, lazy loading, and memoization

---

## 82) How can you monitor real-user metrics (RUM) using tools like Sentry, Google Analytics, or New Relic?

Concept:
RUM tools collect performance data from real users, providing insights into actual user experience and performance issues.

Example:
```jsx
// Sentry performance monitoring
import * as Sentry from '@sentry/react';

function App() {
  useEffect(() => {
    // Track page load performance
    Sentry.addBreadcrumb({ message: 'App loaded' });
  }, []);
  
  return <div>App</div>;
}
```

Deep Insight:
- **Real User Data**: Collect performance data from actual users
- **Production Monitoring**: Monitor performance in production environment
- **Error Tracking**: Track errors and performance issues
- **User Experience**: Understand actual user experience
- **Continuous Improvement**: Use data to continuously improve performance

---

## 82) What is virtualization (e.g., `react-window`, `react-virtualized`) and why use it?

Concept:
Virtualization renders only visible items in large lists, improving performance by reducing DOM nodes and memory usage.

Example:
```jsx
import { FixedSizeList as List } from 'react-window';

function VirtualizedList({ items }) {
  const Row = ({ index, style }) => (
    <div style={style}>
      {items[index].name}
    </div>
  );
  
  return <List height={400} itemCount={items.length} itemSize={50}>{Row}</List>;
}
```

Deep Insight:
- **Performance**: Renders only visible items, reducing DOM nodes
- **Memory Usage**: Lower memory usage for large lists
- **Smooth Scrolling**: Maintains smooth scrolling performance
- **Use Cases**: Large lists, tables, grids, infinite scrolling
- **Libraries**: react-window, react-virtualized, react-window-infinite-loader

---

## 82) How can you optimize image loading and rendering in React?

Concept:
Use lazy loading, responsive images, WebP format, proper sizing, and modern image components for better performance.

Example:
```jsx
// Optimized image component
function OptimizedImage({ src, alt, width, height }) {
  const [isLoaded, setIsLoaded] = useState(false);
  const [isInView, setIsInView] = useState(false);
  const imgRef = useRef();
  
  useEffect(() => {
    const observer = new IntersectionObserver(([entry]) => {
      if (entry.isIntersecting) setIsInView(true);
    });
    if (imgRef.current) observer.observe(imgRef.current);
    return () => observer.disconnect();
  }, []);
  
  return (
    <div ref={imgRef} style={{ width, height }}>
      {isInView && (
        <img
          src={src}
          alt={alt}
          onLoad={() => setIsLoaded(true)}
          style={{ opacity: isLoaded ? 1 : 0 }}
        />
      )}
    </div>
  );
}
```

Deep Insight:
- **Lazy Loading**: Load images only when they come into view
- **Responsive Images**: Use different sizes for different screen sizes
- **WebP Format**: Use modern image formats for better compression
- **Proper Sizing**: Set width and height to prevent layout shift
- **Intersection Observer**: Use for efficient lazy loading

---

## 82) What is bundle splitting and how does it affect performance?

Concept:
Bundle splitting divides code into smaller chunks loaded on demand, reducing initial bundle size and improving loading performance.

Example:
```jsx
// Route-based splitting
import { lazy, Suspense } from 'react';
import { BrowserRouter, Routes, Route } from 'react-router-dom';

const Home = lazy(() => import('./pages/Home'));
const About = lazy(() => import('./pages/About'));

function App() {
  return (
    <BrowserRouter>
      <Suspense fallback={<div>Loading...</div>}>
        <Routes>
          <Route path="/" element={<Home />} />
          <Route path="/about" element={<About />} />
        </Routes>
      </Suspense>
    </BrowserRouter>
  );
}
```

Deep Insight:
- **Initial Bundle**: Reduces size of initial JavaScript bundle
- **Lazy Loading**: Load code only when needed
- **Performance**: Improves initial page load time
- **Caching**: Better caching strategy for different chunks
- **Use Cases**: Route-based, feature-based, vendor splitting

---

## 82) What is lazy component initialization and when to use it?

Concept:
Lazy initialization delays component creation until needed, useful for expensive components or components with heavy dependencies.

Example:
```jsx
// Lazy component initialization
function ExpensiveComponent({ data }) {
  const [processedData, setProcessedData] = useState(null);
  
  useEffect(() => {
    // Lazy initialization - only process when component is visible
    const processData = async () => {
      const result = await heavyProcessing(data);
      setProcessedData(result);
    };
    processData();
  }, [data]);
  
  return <div>{processedData || 'Processing...'}</div>;
}
```

Deep Insight:
- **Performance**: Delays expensive operations until needed
- **Memory Usage**: Reduces initial memory usage
- **User Experience**: Improves initial page load time
- **Use Cases**: Heavy components, large libraries, expensive calculations
- **Implementation**: Use useEffect, dynamic imports, or React.lazy

---
