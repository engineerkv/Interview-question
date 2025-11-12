# 🚀 2. Performance & Caching Optimization (Q11–27)

---

## 🧩 Q11. What are the Core Web Vitals and how do you improve them?

### 🧠 Concept

Core Web Vitals are key metrics that measure user experience: LCP (Largest Contentful Paint), FID (First Input Delay), and CLS (Cumulative Layout Shift), which directly impact SEO and user satisfaction. Core Web Vitals directly affect SEO rankings.

---

### 💡 Example

```javascript
import { getCLS, getFID, getLCP } from 'web-vitals';

getCLS(console.log);
getFID(console.log);
getLCP(console.log);

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

---

### 🔍 Deep Insights

* **Rule:** LCP measures loading performance (should be < 2.5s), FID measures interactivity (should be < 100ms), CLS measures visual stability (should be < 0.1).
* **Use Case:** Optimize images, fonts, and critical resources.
* **Common Mistake:** Use performance budgets and monitoring tools.
* **Pro Tip:** Measure and optimize each metric systematically.

---

### ⭐ Senior Takeaway

Core Web Vitals directly affect SEO rankings.

---

## 🧩 Q12. How do you implement code splitting and lazy loading?

### 🧠 Concept

Code splitting breaks the application into smaller chunks that are loaded on-demand, reducing initial bundle size and improving performance through lazy loading. Code splitting improves initial load time.

---

### 💡 Example

```javascript
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
```

---

### 🔍 Deep Insights

* **Rule:** Use route and component-level splitting.
* **Use Case:** Prefer dynamic import() for better cacheability.
* **Common Mistake:** Share common chunks; avoid vendor bloat.
* **Pro Tip:** Analyze bundle split with tools (webpack-bundle-analyzer, rollup visualizer).

---

### ⭐ Senior Takeaway

Code splitting improves initial load time.

---

## 🧩 Q13. What is minification and how do you enable it?

### 🧠 Concept

Minification removes unnecessary characters (whitespace, comments), shortens identifiers, and applies safe code transformations to reduce asset size for faster downloads and execution. Measure impact with bundle analyzers and performance budgets.

---

### 💡 Example

```javascript
// Webpack (JS minification via Terser)
module.exports = {
  mode: 'production',
  optimization: {
    minimize: true,
    minimizer: [
      new TerserPlugin({
        terserOptions: {
          compress: { drop_console: true, passes: 2 },
          mangle: true,
          format: { comments: false }
        }
      })
    ]
  }
};

// Vite (uses esbuild for minify by default)
export default defineConfig({
  build: {
    minify: 'esbuild',
    terserOptions: { compress: { drop_console: true } }
  }
});
```

---

### 🔍 Deep Insights

* **Rule:** Minify all text assets: JS, CSS, HTML; combine with compression (gzip/Brotli) for best results.
* **Use Case:** Prefer source maps in production (hidden) to debug minified code.
* **Common Mistake:** Safe transforms: dead-code elimination, constant folding, boolean/if simplification.
* **Pro Tip:** Drop debug statements (`console.*`, `debugger`) to shrink bundles.

---

### ⭐ Senior Takeaway

Measure impact with bundle analyzers and performance budgets.

---

## 🧩 Q14. What is code obfuscation and when should you use it?

### 🧠 Concept

Code obfuscation transforms code to a functionally equivalent but hard-to-read form to make reverse-engineering more difficult. For strong protection, rely on server-side enforcement, licensing, watermarking.

---

### 💡 Example

```javascript
// obfuscator.json
{
  "compact": true,
  "controlFlowFlattening": true,
  "deadCodeInjection": true,
  "stringArray": true,
  "stringArrayEncoding": ["rc4"],
  "renameGlobals": true,
  "disableConsoleOutput": true
}
```

---

### 🔍 Deep Insights

* **Rule:** Obfuscation ≠ Security: It's defense-in-depth, not a replacement for proper security.
* **Use Case:** Larger bundles, slower runtime, harder debugging, potential compatibility issues.
* **Common Mistake:** Consider obfuscating only sensitive modules (license checks, proprietary algorithms) rather than full app.
* **Pro Tip:** Do not ship public readable maps for obfuscated bundles; keep private maps securely.

---

### ⭐ Senior Takeaway

For strong protection, rely on server-side enforcement, licensing, watermarking.

---

## 🧩 Q15. How do you implement caching strategies?

### 🧠 Concept

Caching strategies include browser caching, service worker caching, CDN caching, and API response caching to improve performance and reduce server load. Choose strategy based on content type and update frequency.

---

### 💡 Example

```javascript
// Service Worker caching strategies
self.addEventListener('fetch', (event) => {
  const { request } = event;
  
  // Cache first for static assets
  if (request.url.includes('/static/')) {
    event.respondWith(cacheFirst(request));
  }
  // Network first for API calls
  else if (request.url.includes('/api/')) {
    event.respondWith(networkFirst(request));
  }
  // Stale while revalidate for dynamic content
  else {
    event.respondWith(staleWhileRevalidate(request));
  }
});
```

---

### 🔍 Deep Insights

* **Rule:** Cache first for static assets, network first for dynamic content.
* **Use Case:** Stale while revalidate for frequently updated content.
* **Common Mistake:** Implement proper cache invalidation strategies.
* **Pro Tip:** Use ETags and cache headers for HTTP caching.

---

### ⭐ Senior Takeaway

Choose strategy based on content type and update frequency.

---

## 🧩 Q16. How do you optimize images for web performance?

### 🧠 Concept

Image optimization includes format selection (WebP, AVIF), responsive images, lazy loading, and proper sizing to reduce bandwidth and improve loading performance. Use modern formats and responsive images.

---

### 💡 Example

```javascript
// Responsive images with modern formats
const OptimizedImage = ({ src, alt }) => (
  <picture>
    <source srcSet={`${src}.avif`} type="image/avif" />
    <source srcSet={`${src}.webp`} type="image/webp" />
    <img src={`${src}.jpg`} alt={alt} loading="lazy" />
  </picture>
);
```

---

### 🔍 Deep Insights

* **Rule:** Use modern formats (WebP, AVIF) for better compression.
* **Use Case:** Implement lazy loading for below-the-fold images.
* **Common Mistake:** Provide responsive images with srcset.
* **Pro Tip:** Optimize image dimensions and compression.

---

### ⭐ Senior Takeaway

Use modern formats and responsive images.

---

## 🧩 Q17. How do you implement HTTP caching?

### 🧠 Concept

HTTP caching uses cache headers (Cache-Control, ETag, Last-Modified) to control how browsers and CDNs cache resources, reducing server load and improving performance. Use appropriate cache headers for different resource types.

---

### 💡 Example

```javascript
// Cache-Control headers
const cacheHeaders = {
  static: 'Cache-Control: public, max-age=31536000, immutable',
  dynamic: 'Cache-Control: public, max-age=3600, must-revalidate',
  api: 'Cache-Control: private, max-age=0, must-revalidate'
};
```

---

### 🔍 Deep Insights

* **Rule:** Use long cache times for static assets with immutable flag.
* **Use Case:** Use shorter cache times for dynamic content.
* **Common Mistake:** Implement proper cache invalidation.
* **Pro Tip:** Use ETags for conditional requests.

---

### ⭐ Senior Takeaway

Use appropriate cache headers for different resource types.

---

## 🧩 Q18. How do you implement service worker caching?

### 🧠 Concept

Service worker caching enables offline functionality and improves performance by caching resources and API responses. Test offline functionality thoroughly.

---

### 💡 Example

```javascript
// Service Worker caching
self.addEventListener('install', (event) => {
  event.waitUntil(
    caches.open('v1').then((cache) => {
      return cache.addAll(['/', '/static/js/bundle.js', '/static/css/main.css']);
    })
  );
});

self.addEventListener('fetch', (event) => {
  event.respondWith(
    caches.match(event.request).then((response) => {
      return response || fetch(event.request);
    })
  );
});
```

---

### 🔍 Deep Insights

* **Rule:** Cache static assets on install.
* **Use Case:** Use network-first or cache-first strategies.
* **Common Mistake:** Implement proper cache invalidation.
* **Pro Tip:** Update service worker for cache updates.

---

### ⭐ Senior Takeaway

Test offline functionality thoroughly.

---

## 🧩 Q19. How do you optimize bundle size?

### 🧠 Concept

Bundle size optimization includes tree shaking, code splitting, removing unused dependencies, and analyzing bundle composition. Monitor bundle size and set performance budgets.

---

### 💡 Example

```javascript
// Tree shaking with ES modules
import { debounce } from 'lodash-es'; // Only imports debounce

// Bundle analysis
const analyzeBundle = () => {
  const stats = require('./bundle-stats.json');
  console.log('Bundle size:', stats.totalSize);
  console.log('Largest chunks:', stats.chunks.sort((a, b) => b.size - a.size));
};
```

---

### 🔍 Deep Insights

* **Rule:** Use tree shaking to remove unused code.
* **Use Case:** Split vendor bundles from application code.
* **Common Mistake:** Remove unused dependencies.
* **Pro Tip:** Use bundle analyzers to identify large dependencies.

---

### ⭐ Senior Takeaway

Monitor bundle size and set performance budgets.

---

## 🧩 Q20. How do you implement resource hints?

### 🧠 Concept

Resource hints (preload, prefetch, preconnect, dns-prefetch) optimize resource loading by providing hints to the browser about important resources. Use resource hints strategically for critical resources.

---

### 💡 Example

```javascript
// Resource hints
const ResourceHints = () => (
  <>
    <link rel="preconnect" href="https://api.example.com" />
    <link rel="dns-prefetch" href="https://cdn.example.com" />
    <link rel="preload" href="/critical.css" as="style" />
    <link rel="prefetch" href="/next-page.js" as="script" />
  </>
);
```

---

### 🔍 Deep Insights

* **Rule:** Use preconnect for critical third-party domains.
* **Use Case:** Use preload for critical resources.
* **Common Mistake:** Use prefetch for likely next-page resources.
* **Pro Tip:** Use dns-prefetch for external domains.

---

### ⭐ Senior Takeaway

Use resource hints strategically for critical resources.

---

## 🧩 Q21. How do you optimize font loading?

### 🧠 Concept

Font optimization includes font-display strategies, subsetting, preloading, and using system fonts to improve loading performance. Use font-display: swap for better perceived performance.

---

### 💡 Example

```javascript
// Font optimization
const FontOptimization = () => (
  <>
    <link rel="preload" href="/fonts/main.woff2" as="font" type="font/woff2" crossOrigin />
    <style>
      {`
        @font-face {
          font-family: 'Main';
          src: url('/fonts/main.woff2') format('woff2');
          font-display: swap;
        }
      `}
    </style>
  </>
);
```

---

### 🔍 Deep Insights

* **Rule:** Use font-display: swap to prevent invisible text.
* **Use Case:** Preload critical fonts.
* **Common Mistake:** Subset fonts to reduce file size.
* **Pro Tip:** Use system fonts as fallback.

---

### ⭐ Senior Takeaway

Use font-display: swap for better perceived performance.

---

## 🧩 Q22. How do you implement CDN caching?

### 🧠 Concept

CDN caching distributes content across multiple edge locations, reducing latency and server load by serving cached content from locations closer to users. Configure CDN caching based on content type.

---

### 💡 Example

```javascript
// CDN cache configuration
const cdnConfig = {
  static: {
    cacheControl: 'public, max-age=31536000, immutable',
    edgeCacheTTL: 31536000
  },
  dynamic: {
    cacheControl: 'public, max-age=3600',
    edgeCacheTTL: 3600
  }
};
```

---

### 🔍 Deep Insights

* **Rule:** Configure different cache times for different content types.
* **Use Case:** Use CDN for static assets and API responses.
* **Common Mistake:** Implement proper cache invalidation.
* **Pro Tip:** Monitor CDN hit rates and performance.

---

### ⭐ Senior Takeaway

Configure CDN caching based on content type.

---

## 🧩 Q23. How do you optimize API response caching?

### 🧠 Concept

API response caching includes client-side caching, HTTP caching, and service worker caching to reduce API calls and improve performance. Implement proper cache invalidation for dynamic data.

---

### 💡 Example

```javascript
// API response caching
const apiCache = new Map();

const fetchWithCache = async (url, options = {}) => {
  const cacheKey = `${url}-${JSON.stringify(options)}`;
  
  if (apiCache.has(cacheKey)) {
    const cached = apiCache.get(cacheKey);
    if (Date.now() - cached.timestamp < 60000) { // 1 minute cache
      return cached.data;
    }
  }
  
  const response = await fetch(url, options);
  const data = await response.json();
  apiCache.set(cacheKey, { data, timestamp: Date.now() });
  return data;
};
```

---

### 🔍 Deep Insights

* **Rule:** Cache API responses with appropriate TTL.
* **Use Case:** Use HTTP cache headers for API responses.
* **Common Mistake:** Implement proper cache invalidation.
* **Pro Tip:** Use service worker for offline API caching.

---

### ⭐ Senior Takeaway

Implement proper cache invalidation for dynamic data.

---

## 🧩 Q24. How do you implement memory caching?

### 🧠 Concept

Memory caching stores frequently accessed data in memory for fast retrieval, reducing computation and API calls. Use memory caching for expensive computations and frequently accessed data.

---

### 💡 Example

```javascript
// Memory cache implementation
const memoryCache = new Map();

const getCachedData = (key, fetcher, ttl = 60000) => {
  const cached = memoryCache.get(key);
  if (cached && Date.now() - cached.timestamp < ttl) {
    return cached.data;
  }
  
  const data = fetcher();
  memoryCache.set(key, { data, timestamp: Date.now() });
  return data;
};
```

---

### 🔍 Deep Insights

* **Rule:** Use memory cache for expensive operations.
* **Use Case:** Implement TTL for cache expiration.
* **Common Mistake:** Monitor memory usage and cache size.
* **Pro Tip:** Use LRU cache for bounded memory usage.

---

### ⭐ Senior Takeaway

Use memory caching for expensive computations and frequently accessed data.

---

## 🧩 Q25. How do you optimize critical rendering path?

### 🧠 Concept

Critical rendering path optimization minimizes render-blocking resources, inlines critical CSS, defers non-critical JavaScript, and optimizes resource loading order. Optimize above-the-fold content first.

---

### 💡 Example

```javascript
// Critical rendering path optimization
const optimizeCriticalPath = {
  html: `
    <!DOCTYPE html>
    <html>
      <head>
        <link rel="preload" href="critical.css" as="style">
        <link rel="preload" href="hero-image.jpg" as="image">
        <style>
          /* Inline critical CSS */
          body { margin: 0; font-family: Arial; }
        </style>
      </head>
      <body>
        <div class="hero">
          <img src="hero-image.jpg" alt="Hero">
          <h1>Critical Content</h1>
        </div>
        <script src="non-critical.js" defer></script>
      </body>
    </html>
  `
};
```

---

### 🔍 Deep Insights

* **Rule:** Minimize render-blocking resources.
* **Use Case:** Inline critical CSS and defer non-critical styles.
* **Common Mistake:** Use preload hints for important resources.
* **Pro Tip:** Defer non-critical JavaScript.

---

### ⭐ Senior Takeaway

Optimize above-the-fold content first.

---

## 🧩 Q26. How do you implement performance monitoring?

### 🧠 Concept

Performance monitoring tracks Core Web Vitals, custom metrics, and user experience metrics to identify performance issues and optimize accordingly. Monitor performance continuously and set alerts.

---

### 💡 Example

```javascript
// Performance monitoring
import { getCLS, getFID, getLCP } from 'web-vitals';

const sendToAnalytics = (metric) => {
  // Send to analytics service
  analytics.track('web-vital', {
    name: metric.name,
    value: metric.value,
    id: metric.id
  });
};

getCLS(sendToAnalytics);
getFID(sendToAnalytics);
getLCP(sendToAnalytics);
```

---

### 🔍 Deep Insights

* **Rule:** Track Core Web Vitals and custom metrics.
* **Use Case:** Monitor real user metrics (RUM).
* **Common Mistake:** Set performance budgets and alerts.
* **Pro Tip:** Analyze performance trends over time.

---

### ⭐ Senior Takeaway

Monitor performance continuously and set alerts.

---

## 🧩 Q27. How do you optimize for mobile performance?

### 🧠 Concept

Mobile performance optimization includes reducing bundle size, optimizing images, implementing touch-friendly interactions, and minimizing network requests. Test on real devices and slow networks.

---

### 💡 Example

```javascript
// Mobile optimization
const MobileOptimizations = () => {
  // Reduce bundle size
  const isMobile = window.innerWidth < 768;
  const Component = isMobile ? MobileComponent : DesktopComponent;
  
  // Optimize images
  const imageSrc = isMobile ? 'image-mobile.jpg' : 'image-desktop.jpg';
  
  return <Component imageSrc={imageSrc} />;
};
```

---

### 🔍 Deep Insights

* **Rule:** Reduce bundle size for mobile devices.
* **Use Case:** Optimize images and assets for mobile.
* **Common Mistake:** Implement touch-friendly interactions.
* **Pro Tip:** Minimize network requests and use compression.

---

### ⭐ Senior Takeaway

Test on real devices and slow networks.

---
