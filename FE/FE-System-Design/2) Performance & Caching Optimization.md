# 2. Performance & Caching Optimization (Q10–23)

<div align="center">

**[← Previous: UI-UX Architecture & State Management](1%29%20UI-UX%20Architecture%20%26%20State%20Management.md)** | **[Next: Micro-Frontends vs Monolithic SPAs →](3%29%20Micro-Frontends%20vs%20Monolithic%20SPAs.md)**

</div>

---

## Q10. Performance overview

Performance optimization improves user experience by reducing load times, improving interactivity, and ensuring smooth rendering. Performance directly impacts user satisfaction, conversion rates, SEO rankings, and business metrics—slow sites lose users and revenue.

- **Trade-offs**: Performance optimization requires balancing multiple factors: bundle size, network requests, rendering speed, and runtime efficiency. The catch is optimizing one area can impact another—measure first, optimize based on real data, and set performance budgets to prevent regressions.

Example:

```javascript
// Performance optimization checklist
// 1. Measure Core Web Vitals
// 2. Optimize bundle size (code splitting, tree shaking)
// 3. Optimize images (format, size, lazy loading)
// 4. Minimize network requests
// 5. Optimize rendering (critical path, avoid layout shifts)
// 6. Implement caching strategies
// 7. Monitor and iterate
```

---

## Q11. Performance importance

Performance directly impacts user experience, conversion rates, SEO rankings, and business metrics—slow sites lose users and revenue. Every 100ms delay can reduce conversion rates by 1%, and 53% of mobile users abandon sites that take longer than 3 seconds to load.

- **Trade-offs**: Performance improvements can increase development time and complexity, but the catch is poor performance costs more in lost users and revenue. Mobile performance is especially critical since mobile users often have slower connections and less powerful devices—optimize for mobile-first to ensure good experience across all devices.

Example:

```javascript
// Performance impact metrics
// - 1s delay = 7% reduction in conversions
// - 3s delay = 53% mobile abandonment
// - Core Web Vitals affect SEO rankings
// - Performance budgets prevent regressions

// Set performance budgets
const performanceBudget = {
  bundleSize: 200 * 1024, // 200KB
  imageSize: 100 * 1024, // 100KB per image
  totalRequests: 50,
  lcp: 2500, // 2.5s
  fid: 100, // 100ms
  cls: 0.1
};
```

---

## Q12. Performance monitoring

Performance monitoring tracks Core Web Vitals, custom metrics, and user experience metrics to identify performance issues and optimize accordingly. Monitor both Real User Monitoring (RUM) and Synthetic Monitoring for comprehensive coverage.

- **Trade-offs**: RUM provides real user data but requires sufficient traffic, while synthetic monitoring tests specific scenarios but may not reflect real conditions. The catch is monitoring adds overhead—use efficient collection methods and sample data appropriately. Set up alerts for performance regressions and track trends over time.

Example:

```javascript
// Performance monitoring with Web Vitals
import { getCLS, getFID, getLCP, getFCP, getTTFB } from 'web-vitals';

function sendToAnalytics(metric) {
  analytics.track('web-vital', {
    name: metric.name,
    value: metric.value,
    id: metric.id,
    delta: metric.delta
  });
}

getCLS(sendToAnalytics);
getFID(sendToAnalytics);
getLCP(sendToAnalytics);
getFCP(sendToAnalytics);
getTTFB(sendToAnalytics);

// Custom performance marks
performance.mark('app-start');
performance.mark('app-ready');
performance.measure('app-init', 'app-start', 'app-ready');
```

---

## Q13. Performance tools

Performance tools help measure, analyze, and optimize web performance through profiling, bundle analysis, and runtime monitoring. Use browser DevTools, Lighthouse, WebPageTest, and bundle analyzers to identify bottlenecks.

- **Trade-offs**: Different tools serve different purposes—Lighthouse for audits, DevTools for debugging, bundle analyzers for size optimization. The catch is tools can give conflicting results—use multiple tools and focus on real user metrics. Learn to interpret results correctly and prioritize fixes based on impact.

Example:

```javascript
// Lighthouse CI integration
// npm install -g @lhci/cli
// lhci autorun

// Bundle analysis
// webpack-bundle-analyzer
const BundleAnalyzerPlugin = require('webpack-bundle-analyzer').BundleAnalyzerPlugin;
module.exports = {
  plugins: [new BundleAnalyzerPlugin()]
};

// Performance API
const observer = new PerformanceObserver((list) => {
  for (const entry of list.getEntries()) {
    console.log(entry.name, entry.duration);
  }
});
observer.observe({ entryTypes: ['measure', 'navigation'] });
```

---

## Q14. Network optimization

Network optimization reduces latency and bandwidth usage through techniques like compression, HTTP/2, CDN usage, resource hints, and minimizing requests. Network is often the biggest performance bottleneck, especially on mobile.

- **Trade-offs**: Compression reduces size but adds CPU overhead, HTTP/2 enables multiplexing but requires HTTPS. The catch is too many optimizations can complicate architecture—focus on high-impact changes first: enable compression, use CDN, minimize requests, and leverage HTTP/2. Resource hints (preconnect, dns-prefetch) help but use them strategically.

Example:

```javascript
// Resource hints for network optimization
<link rel="preconnect" href="https://api.example.com" />
<link rel="dns-prefetch" href="https://cdn.example.com" />
<link rel="preload" href="/critical.css" as="style" />
<link rel="prefetch" href="/next-page.js" as="script" />

// HTTP/2 server push (server-side)
// Push critical resources with initial response

// Compression
// Enable gzip/Brotli on server
// Content-Encoding: gzip or br

// Minimize requests
// Combine CSS/JS files
// Use sprites for images
// Inline critical CSS
```

---

## Q15. Build optimization

Build optimization reduces bundle size and improves load time through techniques like minification, tree shaking, code splitting, and dead code elimination. Build tools like Webpack, Vite, and esbuild apply these optimizations automatically.

- **Trade-offs**: Aggressive optimization can break code or make debugging harder—use source maps in production (hidden) for debugging. The catch is optimization adds build time—balance optimization level with build speed. Tree shaking removes unused code but requires ES modules, code splitting improves initial load but can increase total bundle size.

Example:

```javascript
// Webpack optimization
module.exports = {
  optimization: {
    minimize: true,
    splitChunks: {
      chunks: 'all',
      cacheGroups: {
        vendor: {
          test: /[\\/]node_modules[\\/]/,
          name: 'vendors',
          chunks: 'all'
        }
      }
    },
    usedExports: true, // Tree shaking
    sideEffects: false
  }
};

// Vite (uses esbuild for fast builds)
export default {
  build: {
    minify: 'esbuild',
    rollupOptions: {
      output: {
        manualChunks: {
          vendor: ['react', 'react-dom']
        }
      }
    }
  }
};
```

---

## Q16. Core Web Vitals and how to optimize them

Core Web Vitals are key metrics that measure user experience: LCP (Largest Contentful Paint), FID (First Input Delay), and CLS (Cumulative Layout Shift), which directly impact SEO and user satisfaction. LCP measures loading performance (should be < 2.5s), FID measures interactivity (should be < 100ms), CLS measures visual stability (should be < 0.1).

- **Trade-offs**: Optimizing Core Web Vitals requires balancing multiple factors—optimize images and fonts for LCP, reduce JavaScript execution for FID, avoid layout shifts for CLS. The catch is these metrics are interconnected—improving one can impact another, so measure and optimize systematically.

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

## Q17. Implementing code splitting and lazy loading

Code splitting breaks the application into smaller chunks that are loaded on-demand, reducing initial bundle size and improving performance through lazy loading. Use route and component-level splitting.

- **Trade-offs**: Code splitting improves initial load time, but the catch is too many chunks can increase HTTP overhead—prefer dynamic import() for better cacheability, share common chunks, and avoid vendor bloat. Analyze bundle split with tools (webpack-bundle-analyzer, rollup visualizer) to find the right balance.

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

## Q18. Optimizing images for web performance

Image optimization includes format selection (WebP, AVIF), responsive images, lazy loading, and proper sizing to reduce bandwidth and improve loading performance. Use modern formats and responsive images.

- **Trade-offs**: Modern formats (WebP, AVIF) provide better compression but require fallbacks for older browsers. The catch is implement lazy loading for below-the-fold images—provide responsive images with srcset, and optimize image dimensions and compression. Use appropriate formats based on image type and browser support.

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

## Q19. Optimizing bundle size

Bundle size optimization includes tree shaking, code splitting, removing unused dependencies, and analyzing bundle composition. Monitor bundle size and set performance budgets.

- **Trade-offs**: Tree shaking removes unused code but requires ES modules, code splitting improves initial load but can increase total bundle size. The catch is split vendor bundles from application code—remove unused dependencies, and use bundle analyzers to identify large dependencies.

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

## Q20. Implementing resource hints

Resource hints (preload, prefetch, preconnect, dns-prefetch) optimize resource loading by providing hints to the browser about important resources. Use resource hints strategically for critical resources.

- **Trade-offs**: Resource hints improve perceived performance but can waste bandwidth if overused. The catch is use preload for critical resources—use prefetch for likely next-page resources, use preconnect for critical third-party domains, and use dns-prefetch for external domains.

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

## Q21. Optimizing font loading

Font optimization includes font-display strategies, subsetting, preloading, and using system fonts to improve loading performance. Use font-display: swap to prevent invisible text.

- **Trade-offs**: Font-display: swap improves perceived performance but can cause flash of unstyled text (FOUT). The catch is preload critical fonts—subset fonts to reduce file size, and use system fonts as fallback. Balance between custom fonts and performance.

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

## Q22. Implementing CDN caching

CDN caching distributes content across multiple edge locations, reducing latency and server load by serving cached content from locations closer to users. Configure CDN caching based on content type.

- **Trade-offs**: CDN caching improves performance globally but requires proper cache invalidation. The catch is use CDN for static assets and API responses—configure different cache times for different content types, and monitor CDN hit rates and performance.

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

## Q23. Optimizing critical rendering path

Critical rendering path optimization minimizes render-blocking resources, inlines critical CSS, defers non-critical JavaScript, and optimizes resource loading order. Optimize above-the-fold content first.

- **Trade-offs**: Inlining critical CSS improves initial render but increases HTML size, deferring JavaScript improves interactivity but can delay functionality. The catch is minimize render-blocking resources—inline critical CSS and defer non-critical styles, use preload hints for important resources, and defer non-critical JavaScript.

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

<div align="center">

**[← Previous: UI-UX Architecture & State Management](1%29%20UI-UX%20Architecture%20%26%20State%20Management.md)** | **[Next: Micro-Frontends vs Monolithic SPAs →](3%29%20Micro-Frontends%20vs%20Monolithic%20SPAs.md)**

</div>
