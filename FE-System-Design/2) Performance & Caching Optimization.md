# 2) Performance & Caching Optimization (Q11–20)

## 11) What are the Core Web Vitals, and how do you improve them?

Concept: Core Web Vitals are key metrics that measure user experience: LCP (Largest Contentful Paint), FID (First Input Delay), and CLS (Cumulative Layout Shift), which directly impact SEO and user satisfaction.

Example:
```javascript
// Measuring Core Web Vitals
import { getCLS, getFID, getFCP, getLCP, getTTFB } from 'web-vitals';

getCLS(console.log);
getFID(console.log);
getFCP(console.log);
getLCP(console.log);
getTTFB(console.log);

// Optimizing LCP with image preloading
const ImageComponent = ({ src, alt }) => {
  useEffect(() => {
    const link = document.createElement('link');
    link.rel = 'preload';
    link.as = 'image';
    link.href = src;
    document.head.appendChild(link);
  }, [src]);
  
  return <img src={src} alt={alt} loading="eager" />;
};
```

Deep Insight:
- LCP measures loading performance (should be < 2.5s)
- FID measures interactivity (should be < 100ms)
- CLS measures visual stability (should be < 0.1)
- Optimize images, fonts, and critical resources
- Use performance budgets and monitoring tools

## 12) How do you implement code splitting and lazy loading with React/Vue?

Concept: Code splitting breaks the application into smaller chunks that are loaded on-demand, reducing initial bundle size and improving performance through lazy loading.

Example:
```javascript
// React lazy loading with Suspense
import { lazy, Suspense } from 'react';

const LazyComponent = lazy(() => import('./HeavyComponent'));

const App = () => (
  <Suspense fallback={<div>Loading...</div>}>
    <LazyComponent />
  </Suspense>
);

// Route-based code splitting
const Home = lazy(() => import('./pages/Home'));
const About = lazy(() => import('./pages/About'));

const App = () => (
  <Router>
    <Suspense fallback={<div>Loading...</div>}>
      <Routes>
        <Route path="/" element={<Home />} />
        <Route path="/about" element={<About />} />
      </Routes>
    </Suspense>
  </Router>
);
```

Deep Insight:
- Split code at route and component levels
- Use dynamic imports for on-demand loading
- Implement proper loading states and error boundaries
- Consider bundle analysis to identify splitting opportunities
- Balance between too many small chunks and too few large chunks

## 13) What are service workers, and how do they improve app caching?

Concept: Service workers are background scripts that enable offline functionality, push notifications, and advanced caching strategies by intercepting network requests.

Example:
```javascript
// Service worker registration
if ('serviceWorker' in navigator) {
  navigator.serviceWorker.register('/sw.js')
    .then(registration => console.log('SW registered'))
    .catch(error => console.log('SW registration failed'));
}

// Service worker implementation
self.addEventListener('fetch', event => {
  if (event.request.url.includes('/api/')) {
    event.respondWith(
      caches.open('api-cache').then(cache => {
        return cache.match(event.request).then(response => {
          if (response) {
            return response;
          }
          return fetch(event.request).then(fetchResponse => {
            cache.put(event.request, fetchResponse.clone());
            return fetchResponse;
          });
        });
      })
    );
  }
});
```

Deep Insight:
- Enable offline functionality and background sync
- Implement different caching strategies (cache-first, network-first)
- Provide push notifications and background updates
- Improve performance by serving cached content
- Require HTTPS in production environments

## 14) How would you design a caching strategy for static and dynamic assets?

Concept: Effective caching strategies balance performance and freshness by using different approaches for static assets (long-term caching) and dynamic content (shorter TTL with revalidation).

Example:
```javascript
// Cache configuration
const cacheConfig = {
  static: {
    maxAge: 31536000, // 1 year
    immutable: true
  },
  dynamic: {
    maxAge: 300, // 5 minutes
    staleWhileRevalidate: 3600 // 1 hour
  }
};

// Service worker caching strategy
self.addEventListener('fetch', event => {
  const url = new URL(event.request.url);
  
  if (url.pathname.startsWith('/static/')) {
    // Cache-first for static assets
    event.respondWith(cacheFirst(event.request));
  } else if (url.pathname.startsWith('/api/')) {
    // Stale-while-revalidate for API calls
    event.respondWith(staleWhileRevalidate(event.request));
  } else {
    // Network-first for HTML pages
    event.respondWith(networkFirst(event.request));
  }
});
```

Deep Insight:
- Use long-term caching for static assets with content hashing
- Implement stale-while-revalidate for dynamic content
- Consider cache invalidation strategies
- Monitor cache hit rates and performance
- Use CDN for global asset distribution

## 15) How do you optimize images and videos for performance (responsive, AVIF, WebP)?

Concept: Image and video optimization involves using modern formats, responsive sizing, lazy loading, and proper compression to reduce bandwidth and improve loading performance.

Example:
```javascript
// Responsive image component
const ResponsiveImage = ({ src, alt, sizes }) => {
  const [imageSrc, setImageSrc] = useState('');
  
  useEffect(() => {
    const supportsWebP = document.createElement('canvas')
      .toDataURL('image/webp').indexOf('data:image/webp') === 0;
    
    const format = supportsWebP ? 'webp' : 'jpeg';
    setImageSrc(`${src}.${format}`);
  }, [src]);
  
  return (
    <picture>
      <source srcSet={`${src}.avif`} type="image/avif" />
      <source srcSet={`${src}.webp`} type="image/webp" />
      <img
        src={imageSrc}
        alt={alt}
        loading="lazy"
        sizes={sizes}
        srcSet={`
          ${src}-320w.${format} 320w,
          ${src}-640w.${format} 640w,
          ${src}-1280w.${format} 1280w
        `}
      />
    </picture>
  );
};
```

Deep Insight:
- Use modern formats (AVIF, WebP) with fallbacks
- Implement responsive images with srcset
- Apply lazy loading for below-the-fold content
- Optimize compression and quality settings
- Consider progressive loading for large images

## 16) How do you reduce bundle size (tree-shaking, compression, CDN)?

Concept: Bundle size reduction involves eliminating unused code, compressing assets, and optimizing delivery through techniques like tree-shaking, code splitting, and CDN usage.

Example:
```javascript
// Tree-shaking friendly imports
import { debounce } from 'lodash-es'; // Instead of import _ from 'lodash'
import { Button } from '@mui/material'; // Instead of import * as MUI

// Webpack bundle analyzer
const BundleAnalyzerPlugin = require('webpack-bundle-analyzer').BundleAnalyzerPlugin;

module.exports = {
  plugins: [
    new BundleAnalyzerPlugin({
      analyzerMode: 'static',
      openAnalyzer: false
    })
  ],
  optimization: {
    usedExports: true,
    sideEffects: false,
    splitChunks: {
      chunks: 'all',
      cacheGroups: {
        vendor: {
          test: /[\\/]node_modules[\\/]/,
          name: 'vendors',
          chunks: 'all'
        }
      }
    }
  }
};
```

Deep Insight:
- Use ES modules for better tree-shaking
- Implement code splitting at route and component levels
- Analyze bundle composition regularly
- Use compression (gzip, brotli) for assets
- Consider CDN for global content delivery

## 17) What are the differences between cache-first, stale-while-revalidate, and network-first?

Concept: These are different caching strategies that determine when to serve cached content versus fetching fresh data, each optimized for different use cases and performance requirements.

Example:
```javascript
// Cache-first strategy
const cacheFirst = async (request) => {
  const cachedResponse = await caches.match(request);
  if (cachedResponse) {
    return cachedResponse;
  }
  const networkResponse = await fetch(request);
  const cache = await caches.open('v1');
  cache.put(request, networkResponse.clone());
  return networkResponse;
};

// Stale-while-revalidate strategy
const staleWhileRevalidate = async (request) => {
  const cache = await caches.open('v1');
  const cachedResponse = await cache.match(request);
  
  const fetchPromise = fetch(request).then(networkResponse => {
    cache.put(request, networkResponse.clone());
    return networkResponse;
  });
  
  return cachedResponse || fetchPromise;
};

// Network-first strategy
const networkFirst = async (request) => {
  try {
    const networkResponse = await fetch(request);
    const cache = await caches.open('v1');
    cache.put(request, networkResponse.clone());
    return networkResponse;
  } catch (error) {
    return await caches.match(request);
  }
};
```

Deep Insight:
- Cache-first: Best for static assets, fastest response
- Stale-while-revalidate: Good for dynamic content, balances speed and freshness
- Network-first: Best for critical data, ensures freshness
- Choose strategy based on content type and user experience requirements
- Consider fallback mechanisms for offline scenarios

## 18) What are critical rendering paths, and how can you optimize them?

Concept: The critical rendering path is the sequence of steps browsers take to convert HTML, CSS, and JavaScript into pixels, which can be optimized to improve initial page load performance.

Example:
```javascript
// Critical CSS inlining
const criticalCSS = `
  .header { display: flex; justify-content: space-between; }
  .hero { background: linear-gradient(45deg, #ff6b6b, #4ecdc4); }
`;

// Inline critical CSS
const App = () => (
  <div>
    <style dangerouslySetInnerHTML={{ __html: criticalCSS }} />
    <Header />
    <Hero />
    <LazyComponent />
  </div>
);

// Resource hints for optimization
const Head = () => (
  <head>
    <link rel="preconnect" href="https://fonts.googleapis.com" />
    <link rel="dns-prefetch" href="https://api.example.com" />
    <link rel="preload" href="/critical.css" as="style" />
    <link rel="preload" href="/hero-image.jpg" as="image" />
  </head>
);
```

Deep Insight:
- Minimize render-blocking resources
- Inline critical CSS and defer non-critical styles
- Use resource hints (preconnect, dns-prefetch, preload)
- Optimize JavaScript execution and parsing
- Prioritize above-the-fold content

## 19) How do you measure front-end performance (Lighthouse, Web Vitals API, RUM)?

Concept: Performance measurement involves using various tools and APIs to collect metrics, analyze performance, and identify optimization opportunities.

Example:
```javascript
// Web Vitals measurement
import { getCLS, getFID, getFCP, getLCP, getTTFB } from 'web-vitals';

function sendToAnalytics(metric) {
  // Send to analytics service
  gtag('event', metric.name, {
    value: Math.round(metric.value),
    event_label: metric.id,
    non_interaction: true
  });
}

getCLS(sendToAnalytics);
getFID(sendToAnalytics);
getFCP(sendToAnalytics);
getLCP(sendToAnalytics);
getTTFB(sendToAnalytics);

// Performance Observer for custom metrics
const observer = new PerformanceObserver((list) => {
  for (const entry of list.getEntries()) {
    console.log('Performance entry:', entry);
  }
});

observer.observe({ entryTypes: ['measure', 'navigation'] });
```

Deep Insight:
- Use Lighthouse for comprehensive performance audits
- Implement Web Vitals API for real user monitoring
- Set up Real User Monitoring (RUM) for production insights
- Monitor performance budgets and regression
- Use performance profiling tools for deep analysis

## 20) How would you approach performance optimization for React 19 concurrent rendering?

Concept: React 19's concurrent rendering enables better user experience through features like time slicing, suspense, and automatic batching, requiring optimization strategies that leverage these capabilities.

Example:
```javascript
// Concurrent features in React 19
import { startTransition, useDeferredValue, useTransition } from 'react';

const SearchResults = ({ query }) => {
  const [isPending, startTransition] = useTransition();
  const [results, setResults] = useState([]);
  
  const deferredQuery = useDeferredValue(query);
  
  useEffect(() => {
    if (deferredQuery) {
      startTransition(() => {
        // This update can be interrupted
        setResults(performSearch(deferredQuery));
      });
    }
  }, [deferredQuery]);
  
  return (
    <div>
      {isPending && <Spinner />}
      <ResultsList results={results} />
    </div>
  );
};

// Automatic batching
const handleClick = () => {
  setCount(c => c + 1);
  setFlag(f => !f);
  // These updates are automatically batched
};
```

Deep Insight:
- Use startTransition for non-urgent updates
- Leverage useDeferredValue for expensive computations
- Implement proper Suspense boundaries
- Take advantage of automatic batching
- Consider concurrent features when designing component architecture
