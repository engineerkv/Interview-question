# 🚀 8. Performance Optimization (Q67–80)

---

## 🧩 Q67. What causes re-renders in React and how do you prevent them?

### 🧠 Concept

Common causes include state changes, prop changes, parent re-renders, context changes, and creating objects in render. Prevent them with memoization and avoiding object creation in render.

---

### 💡 Example

```jsx
function App() {
  const [count, setCount] = useState(0);
  const [name, setName] = useState('');
  // ❌ Causes re-render on every render
  const expensiveValue = expensiveCalculation();
  return <div>{expensiveValue} {name} {count}</div>;
}
```

---

### 🔍 Deep Insights

* **Rule:** Any state change triggers component re-render.
* **Use Case:** New prop values cause child components to re-render.
* **Common Mistake:** Creating objects or functions in render causes child re-renders.
* **Pro Tip:** Parent re-render causes all children to re-render by default.

---

### ⭐ Senior Takeaway

Context value changes cause all consumers to re-render—use wisely.

---

## 🧩 Q68. What is memoization and how do you use `React.memo`?

### 🧠 Concept

Memoization caches values and prevents unnecessary re-renders. React.memo prevents re-render if props haven't changed using shallow comparison.

---

### 💡 Example

```jsx
const ExpensiveChild = React.memo(({ user, onUpdate }) => {
  const expensiveValue = useMemo(() => {
    return expensiveCalculation(user);
  }, [user]);
  return <div>{expensiveValue}</div>;
});
```

---

### 🔍 Deep Insights

* **Rule:** React.memo prevents re-render if props haven't changed (shallow comparison).
* **Use Case:** useMemo memoizes expensive calculations to avoid recomputing on every render.
* **Common Mistake:** useCallback memoizes callback functions to prevent child re-renders.
* **Pro Tip:** Use memoization for expensive components or when profiling shows issues.

---

### ⭐ Senior Takeaway

Memoization is a trade-off—adds overhead, use only when needed.

---

## 🧩 Q69. What is the difference between `useMemo` and `useCallback`?

### 🧠 Concept

useMemo caches computed values, useCallback caches function references. Both prevent unnecessary re-renders but optimize different things—values vs functions.

---

### 💡 Example

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

### 🔍 Deep Insights

* **Rule:** useMemo memoizes computed values based on dependencies.
* **Use Case:** useCallback memoizes function references based on dependencies.
* **Common Mistake:** React.memo memoizes component based on props (shallow comparison).
* **Pro Tip:** Memoization is about reference equality, not just performance.

---

### ⭐ Senior Takeaway

useMemo caches values, useCallback caches functions—both prevent re-renders.

---

## 🧩 Q70. How do you implement code splitting with `React.lazy()`?

### 🧠 Concept

Code-splitting loads code on demand. Use React.lazy() for dynamic imports and Suspense for loading states, reducing initial bundle size.

---

### 💡 Example

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

### 🔍 Deep Insights

* **Rule:** React.lazy creates dynamic imports that return promises.
* **Use Case:** Route-based splitting, feature-based splitting, or heavy components.
* **Common Mistake:** Suspense provides loading UI while code is being loaded.
* **Pro Tip:** Reduces initial bundle size by loading code only when needed.

---

### ⭐ Senior Takeaway

Code-splitting improves initial load time and user experience.

---

## 🧩 Q71. What is tree shaking and how do you implement it?

### 🧠 Concept

Tree-shaking removes unused code from bundles. React supports it through ES6 modules and named exports, enabling static analysis.

---

### 💡 Example

```jsx
// ✅ Tree-shakeable imports
import { useState, useEffect } from 'react';
import { debounce } from 'lodash-es';

// ❌ Non-tree-shakeable imports
import * as React from 'react';
```

---

### 🔍 Deep Insights

* **Rule:** Static analysis removes dead code from bundles.
* **Use Case:** Named exports enable tree-shaking through static analysis.
* **Common Mistake:** Reduces bundle size by removing unused code.
* **Pro Tip:** Webpack, Rollup, and other bundlers support tree-shaking.

---

### ⭐ Senior Takeaway

Named exports are tree-shakeable, default exports may not be.

---

## 🧩 Q72. How do you use React Profiler to identify performance issues?

### 🧠 Concept

Use React Profiler API or DevTools to measure component render times and identify slow components. Profiler API is programmatic, DevTools is visual.

---

### 💡 Example

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

### 🔍 Deep Insights

* **Rule:** Profiler API measures component render times programmatically.
* **Use Case:** Identify performance bottlenecks in development or production.
* **Common Mistake:** React DevTools Profiler provides visual analysis.
* **Pro Tip:** Provides detailed timing information for optimization.

---

### ⭐ Senior Takeaway

Profiler API is for programmatic measurement, DevTools for visual analysis.

---

## 🧩 Q73. What are Core Web Vitals and how do you optimize them?

### 🧠 Concept

Core Web Vitals are LCP, FID, and CLS metrics measuring user experience. Optimize with lazy loading, code splitting, and proper sizing.

---

### 💡 Example

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

### 🔍 Deep Insights

* **Rule:** LCP (Largest Contentful Paint) optimizes critical content loading.
* **Use Case:** FID (First Input Delay) keeps main thread responsive with code splitting.
* **Common Mistake:** CLS (Cumulative Layout Shift) sets image dimensions, avoids dynamic content shifts.
* **Pro Tip:** These metrics affect SEO and user experience.

---

### ⭐ Senior Takeaway

Core Web Vitals are Google's ranking factors—optimize them.

---

## 🧩 Q74. How do you implement virtualization for large lists?

### 🧠 Concept

Virtualization renders only visible items in large lists. Use it for performance with thousands of items, reducing DOM nodes and memory usage.

---

### 💡 Example

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

### 🔍 Deep Insights

* **Rule:** Only renders visible items, reducing DOM nodes and memory usage.
* **Use Case:** Large lists, tables, grids, or infinite scrolling scenarios.
* **Common Mistake:** Maintains smooth scrolling with thousands of items.
* **Pro Tip:** Libraries: react-window, react-virtualized, react-window-infinite-loader.

---

### ⭐ Senior Takeaway

Virtualization is essential for large lists.

---

## 🧩 Q75. How do you optimize images in React applications?

### 🧠 Concept

Use lazy loading, responsive images, WebP format, proper sizing, and Intersection Observer for efficient image loading and better Core Web Vitals.

---

### 💡 Example

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

### 🔍 Deep Insights

* **Rule:** Lazy loading loads images only when they come into view (Intersection Observer).
* **Use Case:** Use srcset for different screen sizes, WebP or AVIF for better compression.
* **Common Mistake:** Set width and height to prevent layout shift (CLS).
* **Pro Tip:** Image optimization significantly improves Core Web Vitals.

---

### ⭐ Senior Takeaway

Image optimization is crucial for performance and user experience.

---

## 🧩 Q76. How do you implement bundle splitting?

### 🧠 Concept

Bundle splitting divides code into smaller chunks loaded on demand. It reduces initial bundle size and improves load time, with better caching strategies.

---

### 💡 Example

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

### 🔍 Deep Insights

* **Rule:** Reduces initial bundle size, improves first contentful paint.
* **Use Case:** Route-based, feature-based, or vendor splitting.
* **Common Mistake:** Better caching strategy—changes to one chunk don't invalidate others.
* **Pro Tip:** Improves initial page load time and user experience.

---

### ⭐ Senior Takeaway

Bundle splitting is essential for large React apps.

---

## 🧩 Q77. How do you optimize React applications for mobile?

### 🧠 Concept

Optimize for mobile with code splitting, lazy loading, responsive images, touch-friendly interactions, and reduced bundle sizes for slower networks.

---

### 💡 Example

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

### 🔍 Deep Insights

* **Rule:** Use code splitting and lazy loading for smaller initial bundles.
* **Use Case:** Responsive images and touch-friendly interactions improve mobile UX.
* **Common Mistake:** Reduced bundle sizes help with slower mobile networks.
* **Pro Tip:** Test on real devices, not just emulators.

---

### ⭐ Senior Takeaway

Mobile optimization requires different strategies than desktop.

---

## 🧩 Q78. How do you implement lazy loading for components?

### 🧠 Concept

Lazy loading delays component creation until needed. Use React.lazy() with Suspense for code splitting, or useEffect for expensive operations.

---

### 💡 Example

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

### 🔍 Deep Insights

* **Rule:** Delay expensive operations until component is actually needed.
* **Use Case:** Heavy components, large libraries, or expensive calculations.
* **Common Mistake:** Use useEffect, dynamic imports, or React.lazy.
* **Pro Tip:** Reduces initial memory usage and improves load time.

---

### ⭐ Senior Takeaway

Lazy loading is about deferring work, not just code splitting.

---

## 🧩 Q79. How do you optimize React applications for SEO?

### 🧠 Concept

Optimize for SEO with server-side rendering, proper meta tags, semantic HTML, fast loading times, and structured data. Use Next.js or similar for SSR.

---

### 💡 Example

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

### 🔍 Deep Insights

* **Rule:** Server-side rendering helps search engines index content.
* **Use Case:** Proper meta tags and semantic HTML improve SEO.
* **Common Mistake:** Fast loading times and structured data help rankings.
* **Pro Tip:** Use Next.js or similar frameworks for built-in SEO support.

---

### ⭐ Senior Takeaway

SEO requires server-side rendering and proper meta tags.

---

## 🧩 Q80. What are the best practices for React performance?

### 🧠 Concept

Best practices include memoization when needed, code splitting, lazy loading, virtualization for lists, image optimization, and profiling before optimizing.

---

### 💡 Example

```jsx
// Profile first, then optimize
const MemoizedComponent = React.memo(({ data }) => {
  const processed = useMemo(() => expensive(data), [data]);
  return <div>{processed}</div>;
});
```

---

### 🔍 Deep Insights

* **Rule:** Profile before optimizing—don't guess what's slow.
* **Use Case:** Use memoization, code splitting, and lazy loading strategically.
* **Common Mistake:** Virtualization for lists, image optimization for media.
* **Pro Tip:** Measure performance in production, not just development.

---

### ⭐ Senior Takeaway

Profile first, optimize second—measure don't guess.

---
