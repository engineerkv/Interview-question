# ⚡ 6. Performance Optimization (Q63–76)

---

## 📍 Navigation

<div align="center">

[← Previous: React Latest Features](5%29%20React%20Latest%20Features.md) • [Home: README](../README.md) • [Next: Testing & Debugging →](7%29%20Testing%20%26%20Debugging.md)

[📋 Cheatsheet](React%20Interview%20Cheatsheet.md)

</div>

---

---

## Q63. 🔄 Causes of re-renders in React and how to prevent them

Common causes include state changes, prop changes, parent re-renders, context changes, and creating objects in render - prevent them with memoization and avoiding object creation in render. Any state change triggers component re-render.

- **Trade-offs**: The catch is creating objects or functions in render causes child re-renders - parent re-render causes all children to re-render by default. Context value changes cause all consumers to re-render, so use wisely, but watch out - new prop values cause child components to re-render.

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

## Q64. 💡 Memoization and `React.memo`

Memoization caches values and prevents unnecessary re-renders - React.memo prevents re-render if props haven't changed using shallow comparison. React.memo prevents re-render if props haven't changed (shallow comparison).

- **Trade-offs**: The catch is useCallback memoizes callback functions to prevent child re-renders - use memoization for expensive components or when profiling shows issues. Memoization is a trade-off, adds overhead, so use only when needed, but watch out - useMemo memoizes expensive calculations to avoid recomputing on every render.

Example:

```jsx
const ExpensiveChild = React.memo(({ user, onUpdate }) => {
  const expensiveValue = useMemo(() => {
    return expensiveCalculation(user);
  }, [user]);
  return <div>{expensiveValue}</div>;
});

```

---

## Q65. 🤔 `useMemo` vs `useCallback`

useMemo caches computed values, useCallback caches function references - both prevent unnecessary re-renders but optimize different things: values vs functions. useMemo memoizes computed values based on dependencies.

- **Trade-offs**: The catch is React.memo memoizes component based on props (shallow comparison) - memoization is about reference equality, not just performance. useMemo caches values, useCallback caches functions, both prevent re-renders, but watch out - useCallback memoizes function references based on dependencies.

Example:

```jsx
const ExpensiveComponent = React.memo(({ data, onUpdate }) => {
  const processedData = useMemo(() => {
    return data.map(item => ({
      id: item.id,
      name: item.name.toUpperCase()
    }));
  }, [data]);
  const handleUpdate = useCallback(
    () => onUpdate(processedData),
    [onUpdate, processedData]
  );
  return <button onClick={handleUpdate}>Update</button>;
});

```

---

## Q66. 💡 Code splitting with `React.lazy()`

Code-splitting loads code on demand - use React.lazy() for dynamic imports and Suspense for loading states, reducing initial bundle size. React.lazy creates dynamic imports that return promises.

- **Trade-offs**: The catch is Suspense provides loading UI while code is being loaded - reduces initial bundle size by loading code only when needed. Code-splitting improves initial load time and user experience, but watch out - good for route-based splitting, feature-based splitting, or heavy components.

Example:

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

---

## Q67. 🔧 Tree shaking and how to implement it

Tree-shaking removes unused code from bundles - React supports it through ES6 modules and named exports, enabling static analysis. Static analysis removes dead code from bundles.

- **Trade-offs**: The catch is reduces bundle size by removing unused code - Webpack, Rollup, and other bundlers support tree-shaking. Named exports are tree-shakeable, default exports may not be, but watch out - named exports enable tree-shaking through static analysis.

Example:

```jsx
// ✅ Tree-shakeable imports
import { useState, useEffect } from 'react';
import { debounce } from 'lodash-es';

// ❌ Non-tree-shakeable imports
import * as React from 'react';

```

---

## Q68. ⚡ Using React Profiler to identify performance issues

Use React Profiler API or DevTools to measure component render times and identify slow components - Profiler API is programmatic, DevTools is visual. Profiler API measures component render times programmatically.

- **Trade-offs**: The catch is React DevTools Profiler provides visual analysis - provides detailed timing information for optimization. Profiler API is for programmatic measurement, DevTools for visual analysis, but watch out - identify performance bottlenecks in development or production.

Example:

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

---

## Q69. ⚡ Core Web Vitals and how to optimize them

Core Web Vitals are LCP, INP, and CLS metrics measuring user experience - optimize with lazy loading, code splitting, proper sizing, and keeping the main thread responsive. LCP (Largest Contentful Paint) measures loading performance, INP (Interaction to Next Paint) measures interactivity and replaced FID in 2024, and CLS (Cumulative Layout Shift) measures visual stability. FID (First Input Delay) was the previous interactivity metric that measured time until the browser responds to the first user interaction.

- **Trade-offs**: The catch is CLS requires setting image dimensions and avoiding dynamic content shifts, INP requires keeping main thread responsive with code splitting and avoiding long tasks - these metrics affect SEO and user experience. Core Web Vitals are Google's ranking factors, so optimize them, but watch out - INP replaced FID in 2024 and measures all interactions (not just the first), providing a more comprehensive view of interactivity.

Example:

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

---

## Q70. 🔧 Implementing virtualization for large lists

Virtualization renders only visible items in large lists - use it for performance with thousands of items, reducing DOM nodes and memory usage. Only renders visible items, reducing DOM nodes and memory usage.

- **Trade-offs**: The catch is maintains smooth scrolling with thousands of items - libraries: react-window, react-virtualized, react-window-infinite-loader. Virtualization is essential for large lists, but watch out - good for large lists, tables, grids, or infinite scrolling scenarios.

Example:

```jsx
import { FixedSizeList as List } from 'react-window';

function VirtualizedList({ items }) {
  const Row = ({ index, style }) => (
    <div style={style}>{items[index].name}</div>
  );
  return (
    <List height={400} itemCount={items.length} itemSize={50}>
      {Row}
    </List>
  );
}

```

---

## Q71. 💡 Optimizing images in React applications

Use lazy loading, responsive images, WebP format, proper sizing, and Intersection Observer for efficient image loading and better Core Web Vitals. Lazy loading loads images only when these come into view (Intersection Observer).

- **Trade-offs**: The catch is set width and height to prevent layout shift (CLS) - image optimization significantly improves Core Web Vitals. Image optimization is crucial for performance and user experience, but watch out - use srcset for different screen sizes, WebP or AVIF for better compression.

Example:

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

---

## Q72. 🔧 Implementing bundle splitting

Bundle splitting divides code into smaller chunks loaded on demand - it reduces initial bundle size and improves load time, with better caching strategies. Reduces initial bundle size, improves first contentful paint.

- **Trade-offs**: The catch is better caching strategy - changes to one chunk don't invalidate others, improves initial page load time and user experience. Bundle splitting is essential for large React apps, but watch out - good for route-based, feature-based, or vendor splitting.

Example:

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

---

## Q73. 💡 Optimizing React applications for mobile

Optimize for mobile with code splitting, lazy loading, responsive images, touch-friendly interactions, and reduced bundle sizes for slower networks. Use code splitting and lazy loading for smaller initial bundles.

- **Trade-offs**: The catch is reduced bundle sizes help with slower mobile networks - test on real devices, not just emulators. Mobile optimization requires different strategies than desktop, but watch out - responsive images and touch-friendly interactions improve mobile UX.

Example:

```jsx
function MobileOptimizedApp() {
  const [isMobile, setIsMobile] = useState(false);
  useEffect(() => {
    setIsMobile(window.innerWidth < 768);
  }, []);
  return (
    <div>
      {isMobile ? <MobileView /> : <DesktopView />}
    </div>
  );
}

```

---

## Q74. 🧩 Implementing lazy loading for components

Lazy loading delays component creation until needed - use React.lazy() with Suspense for code splitting, or useEffect for expensive operations. Delay expensive operations until component is actually needed.

- **Trade-offs**: The catch is use useEffect, dynamic imports, or React.lazy - reduces initial memory usage and improves load time. Lazy loading is about deferring work, not just code splitting, but watch out - good for heavy components, large libraries, or expensive calculations.

Example:

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

---

## Q75. 🔍 Optimizing React applications for SEO

Optimize for SEO with server-side rendering, proper meta tags, semantic HTML, fast loading times, and structured data - use Next.js or similar for SSR. Server-side rendering helps search engines index content.

- **Trade-offs**: The catch is fast loading times and structured data help rankings - use Next.js or similar frameworks for built-in SEO support. SEO requires server-side rendering and proper meta tags, but watch out - proper meta tags and semantic HTML improve SEO.

Example:

```jsx
function SEOOptimizedPage({ title, description }) {
  return (
    <>
      <Helmet>
        <title>{title}</title>
        <meta name="description" content={description} />
      </Helmet>
      <main>
        <h1>{title}</h1>
        <p>{description}</p>
      </main>
    </>
  );
}

```

---

## Q76. ⚡ Best practices for React performance

Best practices include memoization when needed, code splitting, lazy loading, virtualization for lists, image optimization, and profiling before optimizing. Profile before optimizing, don't guess what's slow.

- **Trade-offs**: The catch is virtualization for lists, image optimization for media - measure performance in production, not just development. Profile first, optimize second, measure don't guess, but watch out - use memoization, code splitting, and lazy loading strategically.

Example:

```jsx
// Profile first, then optimize
const MemoizedComponent = React.memo(({ data }) => {
  const processed = useMemo(() => expensive(data), [data]);
  return <div>{processed}</div>;
});

```

---

---

## 📍 Navigation

<div align="center">

[5) React Latest Features.md](5%29%20React%20Latest%20Features.md) • [Home: README](../README.md) • [7) Testing & Debugging.md →](7%29%20Testing%20&%20Debugging.md)

[📋 Cheatsheet](React%20Interview%20Cheatsheet.md]

</div>

---
