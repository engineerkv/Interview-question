# ⚛️ React.js Interview Notes (2025 Edition)

## 📊 Section 5 — Core Web Vitals, Profiling & Optimization — Q91-Q110

---

### 91. 📊 What are Core Web Vitals, and why are they important?

**🧠 Concept**

Core Web Vitals are Google's metrics that measure how fast and smooth your website feels to users.

**💻 Example**

```jsx
// Core Web Vitals metrics
const webVitals = {
  LCP: 2.5, // Largest Contentful Paint (loading)
  FID: 100, // First Input Delay (interactivity) 
  CLS: 0.1  // Cumulative Layout Shift (stability)
};
```

**💬 Explanation + Insight**

- **Google Ranking** - Affects your website's search ranking
- **User Experience** - Measures loading speed, interactivity, and visual stability
- **Business Impact** - Better scores = better user experience
- **Performance Budget** - Set performance limits for your app
- **Monitoring** - Track these metrics continuously

---

### 92. 📊 What is Largest Contentful Paint (LCP)?

**🧠 Concept**

LCP measures how long it takes for the largest content element to load and become visible to users.

**💻 Example**

```jsx
// Optimize LCP with image preloading
function HeroSection() {
  return (
    <div>
      <img 
        src="/hero-image.jpg" 
        alt="Hero" 
        loading="eager"
        fetchPriority="high"
      />
    </div>
  );
}
```

**💬 Explanation + Insight**

- **Target Time** - LCP should be under 2.5 seconds
- **Largest Element** - Usually hero images or main content
- **Optimization** - Preload critical resources, optimize images
- **Server Response** - Fast server response improves LCP
- **Critical Path** - Optimize the critical rendering path

---

### 93. 📊 What is First Input Delay (FID)?

**🧠 Concept**

FID measures how long it takes for the browser to respond to the first user interaction.

**💻 Example**

```jsx
// Optimize FID by reducing JavaScript execution
function OptimizedComponent() {
  const [data, setData] = useState(null);
  
  useEffect(() => {
    // Defer non-critical operations
    setTimeout(() => {
      setData(heavyComputation());
    }, 0);
  }, []);
  
  return <div>{data}</div>;
}
```

**💬 Explanation + Insight**

- **Target Time** - FID should be under 100 milliseconds
- **JavaScript Blocking** - Long-running JS blocks user interactions
- **Code Splitting** - Split JavaScript into smaller chunks
- **Lazy Loading** - Load non-critical code later
- **Web Workers** - Move heavy computations to web workers

---

### 94. 📊 What is Cumulative Layout Shift (CLS)?

**🧠 Concept**

CLS measures how much the page layout shifts during loading, causing visual instability.

**💻 Example**

```jsx
// Prevent CLS with proper image dimensions
function StableImage({ src, alt }) {
  return (
    <img 
      src={src} 
      alt={alt}
      width={400}
      height={300}
      style={{ aspectRatio: '4/3' }}
    />
  );
}
```

**💬 Explanation + Insight**

- **Target Score** - CLS should be under 0.1
- **Layout Stability** - Prevent unexpected layout shifts
- **Image Dimensions** - Always specify image dimensions
- **Font Loading** - Use font-display: swap
- **Dynamic Content** - Reserve space for dynamic content

---

### 95. 📊 What is Interaction to Next Paint (INP)?

**🧠 Concept**

INP measures how quickly the page responds to user interactions, replacing FID as a Core Web Vital.

**💻 Example**

```jsx
// Optimize INP with debounced handlers
function SearchInput() {
  const [query, setQuery] = useState('');
  
  const debouncedSearch = useCallback(
    debounce((searchQuery) => {
      performSearch(searchQuery);
    }, 300),
    []
  );
  
  return (
    <input 
      value={query}
      onChange={(e) => {
        setQuery(e.target.value);
        debouncedSearch(e.target.value);
      }}
    />
  );
}
```

**💬 Explanation + Insight**

- **Interaction Responsiveness** - Measures how quickly page responds to clicks, taps, and keyboard input
- **Target Time** - INP should be under 200 milliseconds
- **Event Handling** - Optimize event handlers for performance
- **Debouncing** - Use debouncing for search and input handlers
- **Animation Performance** - Ensure smooth animations

---

### 96. 📊 How do you measure Core Web Vitals in React?

**🧠 Concept**

Measure Core Web Vitals using the web-vitals library and React's built-in performance monitoring.

**💻 Example**

```jsx
import { getCLS, getFID, getFCP, getLCP, getTTFB } from 'web-vitals';

function reportWebVitals(metric) {
  console.log(metric);
  // Send to analytics service
}

// Measure all Core Web Vitals
getCLS(reportWebVitals);
getFID(reportWebVitals);
getFCP(reportWebVitals);
getLCP(reportWebVitals);
getTTFB(reportWebVitals);
```

**💬 Explanation + Insight**

- **Web Vitals Library** - Use Google's web-vitals library
- **Real User Monitoring** - Measure actual user experience
- **Analytics Integration** - Send metrics to monitoring services
- **Performance Budgets** - Set and monitor performance limits
- **Continuous Monitoring** - Track performance over time

---

### 97. 📊 How do you optimize React apps for Core Web Vitals?

**🧠 Concept**

Optimize React apps by implementing code splitting, lazy loading, image optimization, and performance best practices.

**💻 Example**

```jsx
// Code splitting and lazy loading
const LazyComponent = lazy(() => import('./LazyComponent'));

function App() {
  return (
    <Suspense fallback={<div>Loading...</div>}>
      <LazyComponent />
    </Suspense>
  );
}
```

**💬 Explanation + Insight**

- **Code Splitting** - Split code into smaller chunks
- **Lazy Loading** - Load components only when needed
- **Image Optimization** - Use optimized images and lazy loading
- **Bundle Analysis** - Analyze and optimize bundle size
- **Performance Monitoring** - Continuously monitor performance

---

### 98. 📊 How do you use React Profiler for performance optimization?

**🧠 Concept**

Use React Profiler to identify performance bottlenecks and optimize component rendering.

**💻 Example**

```jsx
import { Profiler } from 'react';

function onRenderCallback(id, phase, actualDuration) {
  console.log('Component:', id, 'Phase:', phase, 'Duration:', actualDuration);
}

function App() {
  return (
    <Profiler id="App" onRender={onRenderCallback}>
      <ExpensiveComponent />
    </Profiler>
  );
}
```

**💬 Explanation + Insight**

- **Performance Profiling** - Identify slow components
- **Render Timing** - Measure component render times
- **Optimization Targets** - Find components to optimize
- **Development Tool** - Use in development for optimization
- **Production Monitoring** - Monitor performance in production

---

### 99. 📊 How do you implement performance budgets in React?

**🧠 Concept**

Implement performance budgets to monitor and enforce performance limits during development.

**💻 Example**

```jsx
// Performance budget configuration
const performanceBudget = {
  bundleSize: '250KB',
  lcp: 2500, // 2.5 seconds
  cls: 0.1,
  fid: 100
};

// Check performance budget
function checkPerformanceBudget(metrics) {
  if (metrics.lcp > performanceBudget.lcp) {
    console.warn('LCP exceeds budget');
  }
}
```

**💬 Explanation + Insight**

- **Bundle Size Limits** - Set maximum bundle sizes
- **Performance Metrics** - Monitor Core Web Vitals
- **Build-time Checks** - Fail builds if limits exceeded
- **Team Accountability** - Ensure performance standards
- **Continuous Monitoring** - Track performance over time

---

### 100. 📊 How do you optimize images in React for Core Web Vitals?

**🧠 Concept**

Optimize images using lazy loading, proper dimensions, and modern image formats to improve Core Web Vitals.

**💻 Example**

```jsx
// Optimized image component
function OptimizedImage({ src, alt, width, height }) {
  const [isLoaded, setIsLoaded] = useState(false);
  
  return (
    <div style={{ width, height }}>
      <img
        src={src}
        alt={alt}
        width={width}
        height={height}
        loading="lazy"
        onLoad={() => setIsLoaded(true)}
        style={{ opacity: isLoaded ? 1 : 0 }}
      />
    </div>
  );
}
```

**💬 Explanation + Insight**

- **Lazy Loading** - Load images only when needed
- **Proper Dimensions** - Specify width and height
- **Modern Formats** - Use WebP and AVIF formats
- **Responsive Images** - Use srcset for different screen sizes
- **Placeholder** - Show placeholder while loading

---

### 101. 📊 How do you optimize fonts in React for Core Web Vitals?

**🧠 Concept**

Optimize fonts using font-display: swap, preloading, and proper font loading strategies.

**💻 Example**

```jsx
// Font optimization
function FontOptimized() {
  return (
    <div>
      <link
        rel="preload"
        href="/fonts/custom-font.woff2"
        as="font"
        type="font/woff2"
        crossOrigin="anonymous"
      />
      <style>
        {`
          @font-face {
            font-family: 'CustomFont';
            src: url('/fonts/custom-font.woff2') format('woff2');
            font-display: swap;
          }
        `}
      </style>
    </div>
  );
}
```

**💬 Explanation + Insight**

- **Font Display** - Use font-display: swap
- **Preloading** - Preload critical fonts
- **Font Subsetting** - Load only needed characters
- **Fallback Fonts** - Use system fonts as fallbacks
- **Layout Stability** - Prevent layout shifts during font loading

---

### 102. 📊 How do you implement virtual scrolling for performance?

**🧠 Concept**

Implement virtual scrolling to render only visible items in large lists, improving performance and Core Web Vitals.

**💻 Example**

```jsx
// Virtual scrolling
function VirtualList({ items, itemHeight }) {
  const [scrollTop, setScrollTop] = useState(0);
  const containerHeight = 400;
  const visibleItems = Math.ceil(containerHeight / itemHeight);
  
  const startIndex = Math.floor(scrollTop / itemHeight);
  const endIndex = Math.min(startIndex + visibleItems, items.length);
  
  return (
    <div 
      style={{ height: containerHeight, overflow: 'auto' }}
      onScroll={(e) => setScrollTop(e.target.scrollTop)}
    >
      {items.slice(startIndex, endIndex).map((item, index) => (
        <div key={startIndex + index} style={{ height: itemHeight }}>
          {item}
        </div>
      ))}
    </div>
  );
}
```

**💬 Explanation + Insight**

- **Large Lists** - Handle thousands of items efficiently
- **DOM Optimization** - Render only visible items
- **Memory Usage** - Reduce memory consumption
- **Scroll Performance** - Smooth scrolling experience
- **Bundle Size** - Use lightweight virtual scrolling libraries

---

### 103. 📊 How do you optimize React components for performance?

**🧠 Concept**

Optimize React components using memo, useMemo, useCallback, and other performance optimization techniques.

**💻 Example**

```jsx
// Optimized component
const ExpensiveComponent = memo(({ data, onUpdate }) => {
  const processedData = useMemo(() => {
    return data.map(item => expensiveCalculation(item));
  }, [data]);
  
  const handleClick = useCallback(() => {
    onUpdate(processedData);
  }, [processedData, onUpdate]);
  
  return <div onClick={handleClick}>{processedData.length}</div>;
});
```

**💬 Explanation + Insight**

- **Memoization** - Use memo to prevent unnecessary re-renders
- **useMemo** - Memoize expensive calculations
- **useCallback** - Memoize event handlers
- **Dependency Arrays** - Properly manage dependencies
- **Performance Profiling** - Use React Profiler to identify issues

---

### 104. 📊 How do you implement performance monitoring in React?

**🧠 Concept**

Implement performance monitoring using React Profiler, web-vitals library, and custom performance metrics.

**💻 Example**

```jsx
// Performance monitoring
function PerformanceMonitor() {
  useEffect(() => {
    const observer = new PerformanceObserver((list) => {
      list.getEntries().forEach((entry) => {
        if (entry.entryType === 'measure') {
          console.log(`${entry.name}: ${entry.duration}ms`);
        }
      });
    });
    
    observer.observe({ entryTypes: ['measure'] });
    
    return () => observer.disconnect();
  }, []);
  
  return <div>Performance monitoring active</div>;
}
```

**💬 Explanation + Insight**

- **Performance Observer** - Monitor performance metrics
- **Custom Metrics** - Track application-specific metrics
- **Real User Monitoring** - Monitor actual user experience
- **Analytics Integration** - Send metrics to monitoring services
- **Performance Budgets** - Set and monitor performance limits

---

### 105. 📊 How do you optimize React apps for mobile performance?

**🧠 Concept**

Optimize React apps for mobile by implementing touch-friendly interfaces, responsive design, and mobile-specific optimizations.

**💻 Example**

```jsx
// Mobile-optimized component
function MobileOptimized() {
  const [isMobile, setIsMobile] = useState(false);
  
  useEffect(() => {
    const checkMobile = () => {
      setIsMobile(window.innerWidth < 768);
    };
    
    checkMobile();
    window.addEventListener('resize', checkMobile);
    
    return () => window.removeEventListener('resize', checkMobile);
  }, []);
  
  return (
    <div style={{ 
      fontSize: isMobile ? '14px' : '16px',
      padding: isMobile ? '10px' : '20px'
    }}>
      Mobile optimized content
    </div>
  );
}
```

**💬 Explanation + Insight**

- **Responsive Design** - Adapt to different screen sizes
- **Touch Optimization** - Optimize for touch interactions
- **Performance** - Optimize for slower mobile connections
- **Bundle Size** - Minimize bundle size for mobile
- **Core Web Vitals** - Ensure good mobile performance scores

---

### 106. 📊 How do you implement performance budgets in React?

**🧠 Concept**

Implement performance budgets to monitor and enforce performance limits during development.

**💻 Example**

```jsx
// Performance budget configuration
const performanceBudget = {
  bundleSize: '250KB',
  lcp: 2500, // 2.5 seconds
  cls: 0.1,
  fid: 100
};

// Check performance budget
function checkPerformanceBudget(metrics) {
  if (metrics.lcp > performanceBudget.lcp) {
    console.warn('LCP exceeds budget');
  }
}
```

**💬 Explanation + Insight**

- **Bundle Size Limits** - Set maximum bundle sizes
- **Performance Metrics** - Monitor Core Web Vitals
- **Build-time Checks** - Fail builds if limits exceeded
- **Team Accountability** - Ensure performance standards
- **Continuous Monitoring** - Track performance over time

---

### 107. 📊 How do you optimize React apps for Core Web Vitals?

**🧠 Concept**

Optimize React apps by implementing code splitting, lazy loading, image optimization, and performance best practices.

**💻 Example**

```jsx
// Code splitting and lazy loading
const LazyComponent = lazy(() => import('./LazyComponent'));

function App() {
  return (
    <Suspense fallback={<div>Loading...</div>}>
      <LazyComponent />
    </Suspense>
  );
}
```

**💬 Explanation + Insight**

- **Code Splitting** - Split code into smaller chunks
- **Lazy Loading** - Load components only when needed
- **Image Optimization** - Use optimized images and lazy loading
- **Bundle Analysis** - Analyze and optimize bundle size
- **Performance Monitoring** - Continuously monitor performance

---

### 108. 📊 How do you use React Profiler for performance optimization?

**🧠 Concept**

Use React Profiler to identify performance bottlenecks and optimize component rendering.

**💻 Example**

```jsx
import { Profiler } from 'react';

function onRenderCallback(id, phase, actualDuration) {
  console.log('Component:', id, 'Phase:', phase, 'Duration:', actualDuration);
}

function App() {
  return (
    <Profiler id="App" onRender={onRenderCallback}>
      <ExpensiveComponent />
    </Profiler>
  );
}
```

**💬 Explanation + Insight**

- **Performance Profiling** - Identify slow components
- **Render Timing** - Measure component render times
- **Optimization Targets** - Find components to optimize
- **Development Tool** - Use in development for optimization
- **Production Monitoring** - Monitor performance in production

---

### 109. 📊 How do you implement performance budgets in React?

**🧠 Concept**

Implement performance budgets to monitor and enforce performance limits during development.

**💻 Example**

```jsx
// Performance budget configuration
const performanceBudget = {
  bundleSize: '250KB',
  lcp: 2500, // 2.5 seconds
  cls: 0.1,
  fid: 100
};

// Check performance budget
function checkPerformanceBudget(metrics) {
  if (metrics.lcp > performanceBudget.lcp) {
    console.warn('LCP exceeds budget');
  }
}
```

**💬 Explanation + Insight**

- **Bundle Size Limits** - Set maximum bundle sizes
- **Performance Metrics** - Monitor Core Web Vitals
- **Build-time Checks** - Fail builds if limits exceeded
- **Team Accountability** - Ensure performance standards
- **Continuous Monitoring** - Track performance over time

---

### 110. 📊 How do you optimize React apps for Core Web Vitals?

**🧠 Concept**

Optimize React apps by implementing code splitting, lazy loading, image optimization, and performance best practices.

**💻 Example**

```jsx
// Code splitting and lazy loading
const LazyComponent = lazy(() => import('./LazyComponent'));

function App() {
  return (
    <Suspense fallback={<div>Loading...</div>}>
      <LazyComponent />
    </Suspense>
  );
}
```

**💬 Explanation + Insight**

- **Code Splitting** - Split code into smaller chunks
- **Lazy Loading** - Load components only when needed
- **Image Optimization** - Use optimized images and lazy loading
- **Bundle Analysis** - Analyze and optimize bundle size
- **Performance Monitoring** - Continuously monitor performance

---

*This comprehensive Core Web Vitals and performance optimization section covers essential React performance techniques including Core Web Vitals optimization, performance monitoring, and React-specific performance best practices.*