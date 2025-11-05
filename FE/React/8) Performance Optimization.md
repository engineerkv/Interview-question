# 🚀 8. Performance Optimization (Q67–80)

---

## 67) What are the most common causes of re-renders in React?

Common causes include state changes, prop changes, parent re-renders, context changes, and creating objects in render.

```jsx
function App() {
  const [count, setCount] = useState(0);
  const [name, setName] = useState('');
  // ❌ Causes re-render on every render
  const expensiveValue = expensiveCalculation();
  return <div>{expensiveValue} {name} {count}</div>;
}
```

- **State Changes**: Any state change triggers component re-render
- **Prop Changes**: New prop values cause child components to re-render
- **Parent Re-renders**: Parent re-render causes all children to re-render by default
- **Context Changes**: Context value changes cause all consumers to re-render
- **Common Mistake**: Creating objects or functions in render causes child re-renders

---

## 68) How do you prevent unnecessary re-renders in React components?

Use React.memo, useMemo, useCallback, and avoid creating objects in render to prevent unnecessary re-renders.

```jsx
const ExpensiveChild = React.memo(({ user, onUpdate }) => {
  const expensiveValue = useMemo(() => {
    return expensiveCalculation(user);
  }, [user]);
  return <div>{expensiveValue}</div>;
});
```

- **React.memo**: Prevents re-render if props haven't changed (shallow comparison)
- **useMemo**: Memoizes expensive calculations to avoid recomputing on every render
- **useCallback**: Memoizes callback functions to prevent child re-renders
- **Real-World Use**: Use memoization for expensive components or when profiling shows issues
- **Interview Tip**: Explain that memoization is a trade-off - adds overhead, use only when needed

---

## 69) What is memoization in React (`React.memo`, `useMemo`, `useCallback`)?

Memoization caches values and prevents unnecessary re-renders. Use React.memo for components, useMemo for values, useCallback for functions.

```jsx
const ExpensiveComponent = React.memo(({ data, onUpdate }) => {
  const processedData = useMemo(() => {
    return data.map(item => ({ id: item.id, name: item.name.toUpperCase() }));
  }, [data]);
  const handleUpdate = useCallback(() => onUpdate(processedData), [onUpdate, processedData]);
  return <button onClick={handleUpdate}>Update</button>;
});
```

- **Core Concept**: Cache values or references to avoid unnecessary work
- **React.memo**: Memoizes component based on props (shallow comparison)
- **useMemo**: Memoizes computed values based on dependencies
- **useCallback**: Memoizes function references based on dependencies
- **Interview Tip**: Explain that memoization is about reference equality, not just performance

---

## 70) What is code-splitting and how is it implemented using `React.lazy()` and `Suspense`?

Code-splitting loads code on demand. Use React.lazy() for dynamic imports and Suspense for loading states.

```jsx
import { Suspense, lazy } from 'react';

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

- **Core Benefit**: Reduces initial bundle size by loading code only when needed
- **Real-World Use**: Route-based splitting, feature-based splitting, or heavy components
- **React.lazy**: Creates dynamic imports that return promises
- **Suspense**: Provides loading UI while code is being loaded
- **Interview Tip**: Explain that code-splitting improves initial load time and user experience

---

## 71) What is tree-shaking and how does React support it?

Tree-shaking removes unused code from bundles. React supports it through ES6 modules and named exports.

```jsx
// ✅ Tree-shakeable imports
import { useState, useEffect } from 'react';
import { debounce } from 'lodash-es';

// ❌ Non-tree-shakeable imports
import * as React from 'react';
```

- **Core Concept**: Static analysis removes dead code from bundles
- **ES6 Modules**: Named exports enable tree-shaking through static analysis
- **Real-World Impact**: Reduces bundle size by removing unused code
- **Build Tools**: Webpack, Rollup, and other bundlers support tree-shaking
- **Interview Tip**: Explain that named exports are tree-shakeable, default exports may not be

---

## 72) How do you measure performance using the React Profiler?

Use React Profiler API or DevTools to measure component render times and identify slow components.

```jsx
import { Profiler } from 'react';

function onRenderCallback(id, phase, actualDuration, baseDuration, startTime, commitTime) {
  console.log('Profiler:', {
    id,
    phase,
    actualDuration,
    baseDuration
  });
}

function App() {
  return (
    <Profiler id="App" onRender={onRenderCallback}>
      <MyComponent />
    </Profiler>
  );
}
```

- **Core Purpose**: Measure component render times programmatically
- **Real-World Use**: Identify performance bottlenecks in development or production
- **DevTools**: React DevTools Profiler provides visual analysis
- **Profiling Data**: Provides detailed timing information for optimization
- **Interview Tip**: Explain that Profiler API is for programmatic measurement, DevTools for visual analysis

---

## 73) How do you measure app performance using Chrome DevTools (Performance, Memory tab)?

Use Chrome DevTools Performance tab for runtime analysis and Memory tab for memory leak detection.

```jsx
function measurePerformance() {
  const start = performance.now();
  expensiveOperation();
  const end = performance.now();
  console.log(`Operation took ${end - start}ms`);
}
```

- **Performance Tab**: Analyze runtime performance, identify bottlenecks, and frame rates
- **Memory Tab**: Detect memory leaks, compare heap snapshots, and track memory usage
- **Real-World Use**: Profile production-like scenarios to find performance issues
- **Heap Snapshots**: Compare memory usage over time to find leaks
- **Interview Tip**: Explain that DevTools profiling helps identify real-world performance issues

---

## 74) What are Core Web Vitals and how can you improve them in React apps?

Core Web Vitals are LCP, FID, and CLS metrics measuring user experience. Optimize with lazy loading, code splitting, and proper sizing.

```jsx
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

- **LCP**: Largest Contentful Paint - optimize critical content loading
- **FID**: First Input Delay - keep main thread responsive with code splitting
- **CLS**: Cumulative Layout Shift - set image dimensions, avoid dynamic content shifts
- **Real-World Impact**: These metrics affect SEO and user experience
- **Interview Tip**: Explain that Core Web Vitals are Google's ranking factors

---

## 75) How do Lighthouse and Web Vitals metrics (TTFB, LCP, FID, CLS) apply to React?

These metrics measure performance. Optimize with React features like Suspense, lazy loading, and memoization.

```jsx
function App() {
  const [data, setData] = useState(null);
  useEffect(() => {
    fetch('/api/critical-data').then(r => r.json()).then(setData);
  }, []);
  return <div>{data ? data.title : 'Loading...'}</div>;
}
```

- **TTFB**: Time to First Byte - optimize API calls and server response
- **LCP**: Largest Contentful Paint - optimize critical rendering path with Suspense
- **FID**: First Input Delay - use code splitting to keep main thread responsive
- **CLS**: Cumulative Layout Shift - set dimensions, avoid dynamic content shifts
- **Interview Tip**: Explain how React features help optimize each metric

---

## 76) How can you monitor real-user metrics (RUM) using tools like Sentry, Google Analytics, or New Relic?

RUM tools collect performance data from real users in production. Use them to track errors and performance issues.

```jsx
import * as Sentry from '@sentry/react';

function App() {
  useEffect(() => {
    Sentry.addBreadcrumb({ message: 'App loaded' });
  }, []);
  return <div>App</div>;
}
```

- **Core Purpose**: Monitor real user experience in production, not just development
- **Real-World Use**: Track errors, performance issues, and user experience patterns
- **Tools**: Sentry for errors, Google Analytics for traffic, New Relic for performance
- **Continuous Improvement**: Use data to identify and fix production issues
- **Interview Tip**: Explain that RUM provides insights into actual user experience

---

## 77) What is virtualization (e.g., `react-window`, `react-virtualized`) and why use it?

Virtualization renders only visible items in large lists. Use it for performance with thousands of items.

```jsx
import { FixedSizeList as List } from 'react-window';

function VirtualizedList({ items }) {
  const Row = ({ index, style }) => (
    <div style={style}>{items[index].name}</div>
  );
  return <List height={400} itemCount={items.length} itemSize={50}>{Row}</List>;
}
```

- **Core Benefit**: Only renders visible items, reducing DOM nodes and memory usage
- **Real-World Use**: Large lists, tables, grids, or infinite scrolling scenarios
- **Performance**: Maintains smooth scrolling with thousands of items
- **Libraries**: react-window, react-virtualized, react-window-infinite-loader
- **Interview Tip**: Explain that virtualization is essential for large lists

---

## 78) How can you optimize image loading and rendering in React?

Use lazy loading, responsive images, WebP format, proper sizing, and Intersection Observer for efficient image loading.

```jsx
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

- **Lazy Loading**: Load images only when they come into view (Intersection Observer)
- **Responsive Images**: Use srcset for different screen sizes
- **Modern Formats**: Use WebP or AVIF for better compression
- **Proper Sizing**: Set width and height to prevent layout shift (CLS)
- **Interview Tip**: Explain that image optimization significantly improves Core Web Vitals

---

## 79) What is bundle splitting and how does it affect performance?

Bundle splitting divides code into smaller chunks loaded on demand. It reduces initial bundle size and improves load time.

```jsx
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

- **Core Benefit**: Reduces initial bundle size, improves first contentful paint
- **Real-World Use**: Route-based, feature-based, or vendor splitting
- **Caching**: Better caching strategy - changes to one chunk don't invalidate others
- **Performance**: Improves initial page load time and user experience
- **Interview Tip**: Explain that bundle splitting is essential for large React apps

---

## 80) What is lazy component initialization and when to use it?

Lazy initialization delays component creation until needed. Use it for expensive components or heavy dependencies.

```jsx
function ExpensiveComponent({ data }) {
  const [processedData, setProcessedData] = useState(null);
  
  useEffect(() => {
    const processData = async () => {
      const result = await heavyProcessing(data);
      setProcessedData(result);
    };
    processData();
  }, [data]);
  
  return <div>{processedData || 'Processing...'}</div>;
}
```

- **Core Purpose**: Delay expensive operations until component is actually needed
- **Real-World Use**: Heavy components, large libraries, or expensive calculations
- **Implementation**: Use useEffect, dynamic imports, or React.lazy
- **Performance**: Reduces initial memory usage and improves load time
- **Interview Tip**: Explain that lazy initialization is about deferring work, not just code splitting

---
