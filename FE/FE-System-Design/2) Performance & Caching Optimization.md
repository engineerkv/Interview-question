# 2. Performance & Caching Optimization (Q11–27)

---

## Q11. What are the Core Web Vitals and how do you improve them?

Core Web Vitals are key metrics that measure user experience: LCP (Largest Contentful Paint), FID (First Input Delay), and CLS (Cumulative Layout Shift), which directly impact SEO and user satisfaction - core Web Vitals directly affect SEO rankings. LCP measures loading performance (should be < 2.5s), FID measures interactivity (should be < 100ms), CLS measures visual stability (should be < 0.1).

- **Trade-offs**: The catch is optimize images, fonts, and critical resources - use performance budgets and monitoring tools. Core Web Vitals directly affect SEO rankings, but watch out - measure and optimize each metric systematically.

Example:

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

## Q12. How do you implement code splitting and lazy loading?

Code splitting breaks the application into smaller chunks that are loaded on-demand, reducing initial bundle size and improving performance through lazy loading - code splitting improves initial load time. Use route and component-level splitting.

- **Trade-offs**: The catch is prefer dynamic import() for better cacheability - share common chunks, avoid vendor bloat. Code splitting improves initial load time, but watch out - analyze bundle split with tools (webpack-bundle-analyzer, rollup visualizer).

Example:

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

## Q13. What is minification and how do you enable it?

Minification removes unnecessary characters (whitespace, comments), shortens identifiers, and applies safe code transformations to reduce asset size for faster downloads and execution - measure impact with bundle analyzers and performance budgets. Minify all text assets: JS, CSS, HTML, combine with compression (gzip/Brotli) for best results.

- **Trade-offs**: The catch is prefer source maps in production (hidden) to debug minified code - safe transforms: dead-code elimination, constant folding, boolean/if simplification. Measure impact with bundle analyzers and performance budgets, but watch out - drop debug statements (`console.*`, `debugger`) to shrink bundles.

Example:

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

## Q14. What is code obfuscation and when should you use it?

Code obfuscation transforms code to a functionally equivalent but hard-to-read form to make reverse-engineering more difficult - for strong protection, rely on server-side enforcement, licensing, watermarking. Obfuscation ≠ Security: It's defense-in-depth, not a replacement for proper security.

- **Trade-offs**: The catch is larger bundles, slower runtime, harder debugging, potential compatibility issues - consider obfuscating only sensitive modules (license checks, proprietary algorithms) rather than full app. For strong protection, rely on server-side enforcement, licensing, watermarking, but watch out - do not ship public readable maps for obfuscated bundles, keep private maps securely.

Example:

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

## Q15. How do you implement caching strategies?

Caching strategies include browser caching, service worker caching, CDN caching, and API response caching to improve performance and reduce server load - choose strategy based on content type and update frequency. Cache first for static assets, network first for dynamic content.

- **Trade-offs**: The catch is stale while revalidate for frequently updated content - implement proper cache invalidation strategies. Choose strategy based on content type and update frequency, but watch out - use ETags and cache headers for HTTP caching.

Example:

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

## Q16. How do you optimize images for web performance?

Image optimization includes format selection (WebP, AVIF), responsive images, lazy loading, and proper sizing to reduce bandwidth and improve loading performance - use modern formats and responsive images. Use modern formats (WebP, AVIF) for better compression.

- **Trade-offs**: The catch is implement lazy loading for below-the-fold images - provide responsive images with srcset. Use modern formats and responsive images, but watch out - optimize image dimensions and compression.

Example:

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

## Q17. How do you implement HTTP caching?

HTTP caching uses cache headers (Cache-Control, ETag, Last-Modified) to control how browsers and CDNs cache resources, reducing server load and improving performance - use appropriate cache headers for different resource types. Use long cache times for static assets with immutable flag.

- **Trade-offs**: The catch is use shorter cache times for dynamic content - implement proper cache invalidation. Use appropriate cache headers for different resource types, but watch out - use ETags for conditional requests.

Example:

```javascript
// Cache-Control headers
const cacheHeaders = {
  static: 'Cache-Control: public, max-age=31536000, immutable',
  dynamic: 'Cache-Control: public, max-age=3600, must-revalidate',
  api: 'Cache-Control: private, max-age=0, must-revalidate'
};
```

---

## Q18. How do you implement service worker caching?

Service worker caching enables offline functionality and improves performance by caching resources and API responses - test offline functionality thoroughly. Cache static assets on install.

- **Trade-offs**: The catch is use network-first or cache-first strategies - implement proper cache invalidation. Test offline functionality thoroughly, but watch out - update service worker for cache updates.

Example:

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

## Q19. How do you optimize bundle size?

Bundle size optimization includes tree shaking, code splitting, removing unused dependencies, and analyzing bundle composition - monitor bundle size and set performance budgets. Use tree shaking to remove unused code.

- **Trade-offs**: The catch is split vendor bundles from application code - remove unused dependencies. Monitor bundle size and set performance budgets, but watch out - use bundle analyzers to identify large dependencies.

Example:

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

## Q20. How do you implement resource hints?

Resource hints (preload, prefetch, preconnect, dns-prefetch) optimize resource loading by providing hints to the browser about important resources - use resource hints strategically for critical resources. Use preconnect for critical third-party domains.

- **Trade-offs**: The catch is use preload for critical resources - use prefetch for likely next-page resources. Use resource hints strategically for critical resources, but watch out - use dns-prefetch for external domains.

Example:

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

## Q21. How do you optimize font loading?

Font optimization includes font-display strategies, subsetting, preloading, and using system fonts to improve loading performance - use font-display: swap for better perceived performance. Use font-display: swap to prevent invisible text.

- **Trade-offs**: The catch is preload critical fonts - subset fonts to reduce file size. Use font-display: swap for better perceived performance, but watch out - use system fonts as fallback.

Example:

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

## Q22. How do you implement CDN caching?

CDN caching distributes content across multiple edge locations, reducing latency and server load by serving cached content from locations closer to users - configure CDN caching based on content type. Configure different cache times for different content types.

- **Trade-offs**: The catch is use CDN for static assets and API responses - implement proper cache invalidation. Configure CDN caching based on content type, but watch out - monitor CDN hit rates and performance.

Example:

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

## Q23. How do you optimize API response caching?

API response caching includes client-side caching, HTTP caching, and service worker caching to reduce API calls and improve performance - implement proper cache invalidation for dynamic data. Cache API responses with appropriate TTL.

- **Trade-offs**: The catch is use HTTP cache headers for API responses - implement proper cache invalidation. Implement proper cache invalidation for dynamic data, but watch out - use service worker for offline API caching.

Example:

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

## Q24. How do you implement memory caching?

Memory caching stores frequently accessed data in memory for fast retrieval, reducing computation and API calls - use memory caching for expensive computations and frequently accessed data. Use memory cache for expensive operations.

- **Trade-offs**: The catch is implement TTL for cache expiration - monitor memory usage and cache size. Use memory caching for expensive computations and frequently accessed data, but watch out - use LRU cache for bounded memory usage.

Example:

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

## Q25. How do you optimize critical rendering path?

Critical rendering path optimization minimizes render-blocking resources, inlines critical CSS, defers non-critical JavaScript, and optimizes resource loading order - optimize above-the-fold content first. Minimize render-blocking resources.

- **Trade-offs**: The catch is inline critical CSS and defer non-critical styles - use preload hints for important resources. Optimize above-the-fold content first, but watch out - defer non-critical JavaScript.

Example:

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

## Q26. How do you implement performance monitoring?

Performance monitoring tracks Core Web Vitals, custom metrics, and user experience metrics to identify performance issues and optimize accordingly - monitor performance continuously and set alerts. Track Core Web Vitals and custom metrics.

- **Trade-offs**: The catch is monitor real user metrics (RUM) - set performance budgets and alerts. Monitor performance continuously and set alerts, but watch out - analyze performance trends over time.

Example:

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

## Q27. How do you optimize for mobile performance?

Mobile performance optimization includes reducing bundle size, optimizing images, implementing touch-friendly interactions, and minimizing network requests - test on real devices and slow networks. Reduce bundle size for mobile devices.

- **Trade-offs**: The catch is optimize images and assets for mobile - implement touch-friendly interactions. Test on real devices and slow networks, but watch out - minimize network requests and use compression.

Example:

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
