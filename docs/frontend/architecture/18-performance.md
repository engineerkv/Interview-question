---
sidebar_label: "Performance"
---
# ⚡ Performance
> **Reviewed:** 2026-09 · Modernized; legacy topics are labeled.

---

## 1. ⚡ Performance Monitoring

Performance monitoring is about continuously measuring how real users experience your app in production. It helps you catch regressions early and prioritize the fixes that matter most. Understanding performance metrics and how to monitor them effectively is crucial for keeping your app fast and responsive. For performance testing methodology, see [Performance Testing](./17-testing.md#6-performance-testing).

### 🔹 What to Monitor

### 🔹 Core Web Vitals

* **LCP (Largest Contentful Paint)** – loading speed - how fast the main content appears

* **INP (Interaction to Next Paint)** – interactivity - how responsive the page feels when you click (INP replaced **FID** as a Core Web Vital in March 2024; FID is legacy)

* **CLS (Cumulative Layout Shift)** – visual stability - how much things jump around while loading

### 🔹 Other useful metrics

* Time to First Byte (TTFB) - how fast the server responds

* First Contentful Paint (FCP) - when users first see something on screen

* JavaScript errors, slow API calls, long tasks - things that make the app feel slow

📌 **In simple terms**: Performance monitoring tells you “how fast is the app for real users right now?”

---

### 🔹 💡 How to implement (frontend view)

* Use Real User Monitoring (RUM) tools (e.g., browser APIs + custom beacons, or vendors like New Relic/Datadog/Sentry) - these collect data from real users

* Collect:
  * Web Vitals via `web-vitals` library - track LCP, INP, CLS automatically
  * Errors via `window.onerror` / `unhandledrejection` - catch JavaScript errors

* Tag events with:
  * User/device info (anonymized) - know what devices/browsers are slow
  * Page/route, release version, experiment flags - see which pages or versions are slow

---

### 🔹 📊 Core Web Vitals

Core Web Vitals are a set of metrics that measure real-world user experience on your website. Google uses these metrics as ranking factors, and they directly impact how users perceive your site's performance. Understanding each metric in detail helps you optimize the right things and improve both user experience and SEO.

---

### 🔹 LCP (Largest Contentful Paint)

LCP measures loading performance - specifically, how long it takes for the largest content element visible in the viewport to render.

### 🔹 What is LCP?

LCP marks the point when the largest text or image element becomes visible to the user. This is a key indicator of perceived load speed - users care about when they see the main content, not just when the page technically "loads."

**What counts as LCP element:**

* `<img>` elements
* `<image>` elements inside `<svg>`
* `<video>` elements (uses poster image)
* Elements with background images loaded via `url()`
* Block-level elements containing text nodes

### 🔹 LCP Thresholds

* **Good**: ≤ 2.5 seconds
* **Needs Improvement**: 2.5 - 4.0 seconds
* **Poor**: > 4.0 seconds

### 🔹 How LCP is Measured

The browser tracks candidate LCP elements as the page loads. The LCP is the render time of the largest element that was visible in the viewport.

**LCP Timeline:**

1. **0ms**: Page navigation starts
2. **200ms**: First image starts loading
3. **800ms**: Image finishes loading
4. **850ms**: Image is rendered (LCP)

### 🔹 Common LCP Issues

**1. Slow Server Response Time (TTFB)**

* **Problem**: Server takes too long to respond
* **Impact**: Delays when resources can start loading
* **Solution**: Optimize server, use CDN, enable caching, use edge computing

**2. Render-Blocking Resources**

* **Problem**: CSS and JavaScript block rendering
* **Impact**: Browser can't render content until resources load
* **Solution**: Inline critical CSS, defer non-critical CSS, use async/defer for scripts

**3. Slow Resource Load Times**

* **Problem**: Images, fonts, or other resources load slowly
* **Impact**: LCP element takes too long to appear
* **Solution**: Optimize images (WebP/AVIF), use CDN, preload critical resources, optimize fonts

**4. Client-Side Rendering**

* **Problem**: Content rendered by JavaScript (CSR)
* **Impact**: LCP delayed until JavaScript executes
* **Solution**: Use SSR or SSG, optimize JavaScript bundle, reduce JavaScript execution time

### 🔹 Optimizing LCP

**Server-Side Optimizations:**

```javascript
// Optimize TTFB
// Use CDN, edge computing, caching
res.setHeader('Cache-Control', 'public, max-age=3600');

// Enable compression
app.use(compression());
```

**Image Optimizations:**

```html
<!-- Use modern formats -->
<img src="hero.webp" alt="Hero" loading="eager" fetchpriority="high">

<!-- Preload critical images -->
<link rel="preload" as="image" href="hero.webp">

<!-- Responsive images -->
<img
  srcset="hero-small.webp 640w, hero-large.webp 1920w"
  sizes="(max-width: 640px) 640px, 1920px"
  src="hero-large.webp"
  alt="Hero"
>
```

**CSS Optimizations:**

```html
<!-- Inline critical CSS -->
<style>
  /* Critical above-the-fold styles */
  .hero { ... }
</style>

<!-- Defer non-critical CSS -->
<link rel="preload" href="styles.css" as="style" onload="this.onload=null;this.rel='stylesheet'">
```

**JavaScript Optimizations:**

```html
<!-- Defer non-critical JavaScript -->
<script defer src="analytics.js"></script>

<!-- Use async for independent scripts -->
<script async src="widget.js"></script>
```

### 🔹 Measuring LCP

**Using web-vitals library:**

```javascript
import { onLCP } from 'web-vitals';

onLCP((metric) => {
  console.log('LCP:', metric.value); // Value in milliseconds
  console.log('LCP Element:', metric.entries[0].element);

  // Send to analytics
  sendToAnalytics('LCP', metric.value);
});
```

**Using Performance Observer:**

```javascript
const observer = new PerformanceObserver((list) => {
  const entries = list.getEntries();
  const lastEntry = entries[entries.length - 1];

  console.log('LCP:', lastEntry.renderTime || lastEntry.loadTime);
  console.log('LCP Element:', lastEntry.element);
});

observer.observe({ entryTypes: ['largest-contentful-paint'] });
```

**In Chrome DevTools:**

* Open Performance panel
* Record page load
* Look for "LCP" marker in timeline
* Hover to see LCP element and time

📌 **In simple terms**: LCP measures when the largest content element appears. Optimize by improving server response time, optimizing images, reducing render-blocking resources, and minimizing JavaScript execution time. Target: < 2.5 seconds.

---

### 🔹 INP (Interaction to Next Paint)

INP measures interactivity - how responsive your page feels when users interact with it. It replaced FID (First Input Delay) as a more comprehensive metric that measures the entire interaction latency.

### 🔹 What is INP?

INP measures the latency of all user interactions (clicks, taps, keyboard presses) throughout the page lifecycle. It captures the time from when a user interacts with the page until the next frame is painted.

**INP Components:**

1. **Input Delay**: Time from user action until event handler starts
2. **Processing Time**: Time event handler takes to execute
3. **Presentation Delay**: Time from handler completion until next frame paints

**INP = Input Delay + Processing Time + Presentation Delay**

### 🔹 INP Thresholds

* **Good**: ≤ 200 milliseconds
* **Needs Improvement**: 200 - 500 milliseconds
* **Poor**: > 500 milliseconds

### 🔹 How INP is Measured

The browser tracks all user interactions and measures the total latency. INP is the worst interaction (highest latency) or a high percentile of interactions.

**Example Interaction:**

1. **0ms**: User clicks button
2. **50ms**: Event handler starts (input delay)
3. **200ms**: Event handler completes (processing time)
4. **250ms**: Next frame paints (presentation delay)
5. **INP = 250ms** (total latency)

### 🔹 Common INP Issues

**1. Long Tasks Blocking Main Thread**

* **Problem**: JavaScript tasks > 50ms block the main thread
* **Impact**: User interactions are delayed
* **Solution**: Break up long tasks, use Web Workers, optimize JavaScript

**2. Heavy JavaScript Execution**

* **Problem**: Event handlers do too much work
* **Impact**: Slow response to user actions
* **Solution**: Optimize event handlers, debounce/throttle, use requestIdleCallback

**3. Large JavaScript Bundles**

* **Problem**: Too much JavaScript to parse and execute
* **Impact**: Slow initial interactivity
* **Solution**: Code splitting, lazy loading, reduce bundle size

**4. Layout Thrashing**

* **Problem**: Reading and writing layout properties causes reflows
* **Impact**: Slow rendering after interactions
* **Solution**: Batch DOM reads/writes, use CSS transforms

### 🔹 Optimizing INP

**Break Up Long Tasks:**

```javascript
// ❌ Bad: Long task blocks main thread
function processData(data) {
  for (let i = 0; i < 1000000; i++) {
    // Heavy computation
  }
}

// ✅ Good: Break into smaller chunks
function processData(data) {
  let index = 0;

  function processChunk() {
    const end = Math.min(index + 1000, data.length);
    for (let i = index; i < end; i++) {
      // Process chunk
    }
    index = end;

    if (index < data.length) {
      // Yield to browser
      setTimeout(processChunk, 0);
    }
  }

  processChunk();
}
```

**Optimize Event Handlers:**

```javascript
// ❌ Bad: Heavy work in event handler
button.addEventListener('click', () => {
  // Heavy computation blocks interaction
  processLargeDataset();
  updateUI();
});

// ✅ Good: Defer heavy work
button.addEventListener('click', () => {
  // Immediate feedback
  updateUI();

  // Defer heavy work
  requestIdleCallback(() => {
    processLargeDataset();
  });
});
```

**Use Web Workers:**

```javascript
// main.js
const worker = new Worker('worker.js');

button.addEventListener('click', () => {
  // Offload heavy computation
  worker.postMessage({ data: largeDataset });

  worker.onmessage = (e) => {
    updateUI(e.data.result);
  };
});

// worker.js
self.onmessage = (e) => {
  const result = heavyComputation(e.data.data);
  self.postMessage({ result });
};
```

**Debounce and Throttle:**

```javascript
// Debounce: Wait for pause in events
function debounce(func, wait) {
  let timeout;
  return function executedFunction(...args) {
    const later = () => {
      clearTimeout(timeout);
      func(...args);
    };
    clearTimeout(timeout);
    timeout = setTimeout(later, wait);
  };
}

// Throttle: Limit execution frequency
function throttle(func, limit) {
  let inThrottle;
  return function(...args) {
    if (!inThrottle) {
      func.apply(this, args);
      inThrottle = true;
      setTimeout(() => inThrottle = false, limit);
    }
  };
}

// Usage
const handleSearch = debounce((query) => {
  searchAPI(query);
}, 300);
```

**Optimize Layout:**

```javascript
// ❌ Bad: Causes layout thrashing
elements.forEach(el => {
  el.style.width = calculateWidth(el) + 'px'; // Write
  const height = el.offsetHeight; // Read (forces layout)
});

// ✅ Good: Batch reads and writes
// Read all first
const measurements = elements.map(el => ({
  element: el,
  width: calculateWidth(el),
  height: el.offsetHeight
}));

// Then write all
measurements.forEach(({ element, width }) => {
  element.style.width = width + 'px';
});
```

### 🔹 Measuring INP

**Using web-vitals library:**

```javascript
import { onINP } from 'web-vitals';

onINP((metric) => {
  console.log('INP:', metric.value); // Value in milliseconds
  console.log('Interaction Type:', metric.name); // 'click', 'keydown', etc.
  console.log('Target Element:', metric.entries[0].target);

  // Send to analytics
  sendToAnalytics('INP', metric.value);
});
```

**Using Performance Observer:**

```javascript
const observer = new PerformanceObserver((list) => {
  for (const entry of list.getEntries()) {
    if (entry.entryType === 'event') {
      const inp = entry.processingStart - entry.startTime +
                  entry.duration;
      console.log('INP:', inp);
    }
  }
});

observer.observe({
  entryTypes: ['event'],
  buffered: true
});
```

📌 **In simple terms**: INP measures how responsive your page feels. Optimize by breaking up long tasks, optimizing event handlers, using Web Workers, and avoiding layout thrashing. Target: < 200ms.

---

### 🔹 CLS (Cumulative Layout Shift)

CLS measures visual stability - how much content shifts around as the page loads. Unexpected layout shifts create a poor user experience and can cause users to click the wrong thing.

### 🔹 What is CLS?

CLS quantifies how much visible content shifts during page load. Each layout shift is scored based on the impact fraction (how much of the viewport was affected) and the distance fraction (how far elements moved).

**CLS Score = Impact Fraction × Distance Fraction**

**Impact Fraction**: Proportion of viewport affected by the shift
**Distance Fraction**: Largest distance any element moved (as a fraction of viewport)

### 🔹 CLS Thresholds

* **Good**: ≤ 0.1
* **Needs Improvement**: 0.1 - 0.25
* **Poor**: > 0.25

### 🔹 How CLS is Measured

The browser tracks layout shifts throughout the page lifecycle. CLS is the sum of all individual layout shift scores.

**Example Layout Shift:**

1. Page loads, content renders
2. Image loads without dimensions → pushes content down
3. Impact Fraction: 0.5 (half the viewport affected)
4. Distance Fraction: 0.3 (content moved 30% of viewport height)
5. Layout Shift Score: 0.5 × 0.3 = 0.15

### 🔹 Common CLS Issues

**1. Images Without Dimensions**

* **Problem**: Images load without width/height attributes
* **Impact**: Layout shifts when images load
* **Solution**: Always specify width and height, use aspect-ratio CSS

**2. Ads, Embeds, and iframes**

* **Problem**: Third-party content loads and shifts layout
* **Impact**: Unexpected layout shifts
* **Solution**: Reserve space, use aspect-ratio, lazy load

**3. Dynamically Injected Content**

* **Problem**: Content added after initial render
* **Impact**: Layout shifts when content appears
* **Solution**: Reserve space, use skeleton screens, pre-allocate space

**4. Web Fonts Causing FOIT/FOUT**

* **Problem**: Fonts load and change text size
* **Impact**: Text reflows and shifts layout
* **Solution**: Use font-display: optional, preload fonts, use system fonts

**5. Animations and Transitions**

* **Problem**: Animations that trigger layout changes
* **Impact**: Layout shifts during animations
* **Solution**: Use transform and opacity (don't trigger layout)

### 🔹 Optimizing CLS

**Images with Dimensions:**

```html
<!-- ✅ Good: Specify dimensions -->
<img
  src="hero.jpg"
  alt="Hero"
  width="1920"
  height="1080"
  loading="lazy"
>

<!-- ✅ Good: Use aspect-ratio CSS -->
<img
  src="hero.jpg"
  alt="Hero"
  style="aspect-ratio: 16/9; width: 100%;"
>
```

**Reserve Space for Dynamic Content:**

```html
<!-- ✅ Good: Reserve space for ad -->
<div class="ad-container" style="min-height: 250px;">
  <div id="ad-slot"></div>
</div>

<!-- ✅ Good: Skeleton screen -->
<div class="content-skeleton">
  <div class="skeleton-line"></div>
  <div class="skeleton-line"></div>
</div>
```

**Font Loading:**

```html
<!-- ✅ Good: Preload critical fonts -->
<link rel="preload" href="font.woff2" as="font" type="font/woff2" crossorigin>

<!-- ✅ Good: Use font-display -->
<style>
  @font-face {
    font-family: 'Custom Font';
    src: url('font.woff2') format('woff2');
    font-display: optional; /* Prevents layout shift */
  }
</style>
```

**CSS Transform Instead of Layout Properties:**

```css
/* ❌ Bad: Triggers layout */
.element {
  top: 100px; /* Causes layout shift */
}

/* ✅ Good: Uses compositor */
.element {
  transform: translateY(100px); /* Doesn't trigger layout */
}
```

**Aspect Ratio for Responsive Elements:**

```css
/* ✅ Good: Maintain aspect ratio */
.image-container {
  aspect-ratio: 16 / 9;
  width: 100%;
}

.video-container {
  aspect-ratio: 16 / 9;
  width: 100%;
}
```

### 🔹 Measuring CLS

**Using web-vitals library:**

```javascript
import { onCLS } from 'web-vitals';

onCLS((metric) => {
  console.log('CLS:', metric.value); // Cumulative score
  console.log('Entries:', metric.entries); // Individual shifts

  // Send to analytics
  sendToAnalytics('CLS', metric.value);
});
```

**Using Performance Observer:**

```javascript
let clsValue = 0;
let clsEntries = [];

const observer = new PerformanceObserver((list) => {
  for (const entry of list.getEntries()) {
    // Only count if element was visible
    if (!entry.hadRecentInput) {
      const firstSessionEntry = clsEntries[0];
      const lastSessionEntry = clsEntries[clsEntries.length - 1];

      // Only count if shift happened within 1 second
      if (sessionEntry &&
          entry.startTime - lastSessionEntry.startTime < 1000 &&
          entry.startTime - firstSessionEntry.startTime < 5000) {
        clsValue += entry.value;
        clsEntries.push(entry);
      } else {
        clsValue = entry.value;
        clsEntries = [entry];
      }
    }
  }

  console.log('CLS:', clsValue);
});

observer.observe({ entryTypes: ['layout-shift'], buffered: true });
```

**In Chrome DevTools:**

* Open Performance panel
* Enable "Web Vitals" overlay
* Record page load
* Look for red layout shift markers
* Click markers to see what shifted

📌 **In simple terms**: CLS measures visual stability. Optimize by specifying image dimensions, reserving space for dynamic content, optimizing font loading, and using CSS transforms instead of layout properties. Target: < 0.1.

---

### 🔹 Other Important Metrics

### 🔹 TTFB (Time to First Byte)

TTFB measures server responsiveness - how long it takes for the browser to receive the first byte of the response.

**Thresholds:**

* **Good**: ≤ 800ms
* **Needs Improvement**: 800ms - 1.8s
* **Poor**: > 1.8s

**Optimization:**

* Use CDN
* Enable caching
* Optimize server response time
* Use edge computing
* Reduce server processing time

### 🔹 FCP (First Contentful Paint)

FCP measures when the first content (text, image, canvas, SVG) is painted to the screen.

**Thresholds:**

* **Good**: ≤ 1.8s
* **Needs Improvement**: 1.8s - 3.0s
* **Poor**: > 3.0s

**Optimization:**

* Minimize render-blocking resources
* Inline critical CSS
* Optimize server response time
* Preload critical resources

### 🔹 TTI (Time to Interactive)

TTI measures when the page becomes fully interactive - when the main thread is quiet enough to handle user input.

> **Legacy note (2026):** TTI was removed from Lighthouse scoring in Lighthouse 10 (2023) because it was sensitive to outliers. Prefer **TBT** (Total Blocking Time) in the lab and **INP** in the field.

**Thresholds:**

* **Good**: ≤ 3.8s
* **Needs Improvement**: 3.8s - 7.3s
* **Poor**: > 7.3s

**Optimization:**

* Reduce JavaScript execution time
* Code splitting
* Minimize main thread work
* Optimize third-party scripts

---

### 🔹 Implementing Web Vitals Monitoring

### 🔹 Using web-vitals Library

```javascript
import { onLCP, onINP, onCLS } from 'web-vitals';

function sendToAnalytics(metric) {
  // Send to your analytics service
  const body = JSON.stringify(metric);

  // Use sendBeacon for reliability
  if ('sendBeacon' in navigator) {
    navigator.sendBeacon('/analytics', body);
  } else {
    fetch('/analytics', { body, method: 'POST', keepalive: true });
  }
}

// Measure all Core Web Vitals
onLCP(sendToAnalytics);
onINP(sendToAnalytics);
onCLS(sendToAnalytics);
```

### 🔹 Custom Implementation

```javascript
// Custom Web Vitals tracker
class WebVitalsTracker {
  constructor() {
    this.metrics = {};
    this.setupObservers();
  }

  setupObservers() {
    // LCP
    new PerformanceObserver((list) => {
      const entries = list.getEntries();
      const lastEntry = entries[entries.length - 1];
      this.metrics.lcp = lastEntry.renderTime || lastEntry.loadTime;
      this.report();
    }).observe({ entryTypes: ['largest-contentful-paint'] });

    // INP
    new PerformanceObserver((list) => {
      for (const entry of list.getEntries()) {
        if (entry.entryType === 'event') {
          const inp = entry.processingStart - entry.startTime + entry.duration;
          if (!this.metrics.inp || inp > this.metrics.inp) {
            this.metrics.inp = inp;
          }
        }
      }
      this.report();
    }).observe({ entryTypes: ['event'], buffered: true });

    // CLS
    let clsValue = 0;
    new PerformanceObserver((list) => {
      for (const entry of list.getEntries()) {
        if (!entry.hadRecentInput) {
          clsValue += entry.value;
        }
      }
      this.metrics.cls = clsValue;
      this.report();
    }).observe({ entryTypes: ['layout-shift'], buffered: true });
  }

  report() {
    // Report when all metrics are collected
    if (this.metrics.lcp && this.metrics.inp && this.metrics.cls) {
      console.log('Web Vitals:', this.metrics);
      // Send to analytics
    }
  }
}

// Initialize
new WebVitalsTracker();
```

### 🔹 Real User Monitoring (RUM)

```javascript
// Send to RUM service
function sendToRUM(metric) {
  const data = {
    name: metric.name,
    value: metric.value,
    id: metric.id,
    delta: metric.delta,
    rating: metric.rating, // 'good', 'needs-improvement', 'poor'
    navigationType: metric.navigationType,
    url: window.location.href,
    timestamp: Date.now(),
    userAgent: navigator.userAgent,
    connection: navigator.connection?.effectiveType
  };

  // Send to your RUM service
  fetch('/api/rum', {
    method: 'POST',
    headers: { 'Content-Type': 'application/json' },
    body: JSON.stringify(data),
    keepalive: true
  });
}

onLCP(sendToRUM);
onINP(sendToRUM);
onCLS(sendToRUM);
```

---

### 🔹 ⚡ Performance Tools

Performance tools help you analyze where time is spent so you can target optimizations effectively. Different tools answer different questions - think of them as different lenses to look at performance.

### 🔹 Key Tools and When to Use Them

### 🔹 Lighthouse

* High-level audits (performance, accessibility, best practices, SEO) - gives you a score and recommendations

* Great for **lab measurements** and budgets - test in controlled conditions and set performance goals

### 🔹 Chrome DevTools

* **Performance panel** – CPU, rendering, long tasks - see what's blocking the main thread

* **Network panel** – request waterfall, caching headers, payload sizes - see what's slow to download

* **Coverage** – unused JS/CSS - find code you're shipping but not using

### 🔹 WebPageTest

* Detailed network waterfalls from real devices and locations - see how your app loads from different places

* Compare before/after runs visually - see if your changes actually improved things

📌 **In simple terms**: Use Lighthouse for overview, DevTools for deep debugging, and WebPageTest for real-world waterfalls.

---

### 🔹 💡 Network Optimization

Network optimization reduces the cost and latency of downloading resources. It's often the biggest win for first load performance - you can see huge improvements just by optimizing how resources are delivered.

### 🔹 Techniques

### 🔹 Reduce bytes

* Compress assets (gzip/Brotli) - make files smaller before sending them

* Optimize images (WebP/AVIF, responsive images, lazy loading) - use modern formats and only load what's needed

* Remove unused code (tree shaking, dead code elimination) - don't ship code you're not using

### 🔹 Reduce round trips

* HTTP/2 or HTTP/3 for multiplexing - send multiple requests at once over one connection

* Combine small requests where sensible - fewer requests means less overhead

* Use CDNs close to users - serve files from servers near your users

### 🔹 Resource hints

* `dns-prefetch`, `preconnect`, `prefetch`, `preload` - tell the browser to start loading resources early

📌 **In simple terms**: Make files smaller, send fewer of them, and deliver them from servers closer to the user.

---

### 🔹 🎨 Rendering Patterns

Rendering patterns describe where and when HTML is generated: in the browser, on the server, or ahead of time. Choosing the right pattern balances performance, SEO, and complexity - each pattern has trade-offs you need to consider. For comprehensive details on rendering patterns, see [Rendering Patterns](./23-patterns.md#q100-rendering-patterns).

### 🔹 Common Patterns

### 🔹 CSR (Client-Side Rendering)

* Browser downloads a bare HTML shell + JS bundle - just the skeleton and JavaScript

* JS builds UI at runtime - JavaScript creates everything after it loads

* Good for rich apps, but slower first paint - users see a blank screen longer

### 🔹 SSR (Server-Side Rendering)

* Server renders HTML for each request - server creates the full HTML

* Browser hydrates JS on top - JavaScript makes it interactive after HTML loads

* Faster first paint, better SEO - users see content faster, search engines can read it

### 🔹 SSG / ISR (Static Site Generation / Incremental Static Regeneration)

* HTML prebuilt at build time (or periodically) - generate pages ahead of time

* Very fast and cache-friendly - can serve from CDN, super fast

📌 **In simple terms**: CSR renders everything in the browser, SSR renders on the server per request, and SSG/ISR pre-renders ahead of time.

---

### 🔹 Choosing a Pattern

* SEO-critical + dynamic → SSR / ISR - need SEO but data changes, use server rendering

* Mostly static marketing content → SSG - pre-generate everything, super fast

* Heavy interactive dashboard behind auth → CSR + API calls - no SEO needed, focus on interactivity

---

### 🔹 💡 Build Optimization

Build optimization reduces JavaScript bundle size and improves how code is delivered to the browser. It directly affects load time and interactivity - smaller bundles mean faster downloads and quicker page loads.

### 🔹 Techniques

### 🔹 Code splitting

* Split bundles by route or feature - break up your JavaScript into smaller pieces

* Load only what the current page needs - don't download code for pages the user isn't on

### 🔹 Tree shaking and dead code elimination

* Use ES modules so bundlers can drop unused exports - bundlers can see what you're actually using

* Avoid barrel files that hide usage - barrel files make it hard for bundlers to know what's used

### 🔹 Minification and compression

* Minify JS/CSS (Terser, esbuild) - remove whitespace and shorten variable names

* Gzip/Brotli at server level - compress files when sending them over the network

📌 **In simple terms**: Ship less JavaScript, and only when it’s needed.

---

### 🔹 Frontend Workflow

* Run bundle analyzers (Webpack Bundle Analyzer, Source Map Explorer) - see what's making your bundles big

* Identify heavy dependencies and lazy-load where possible - load big libraries only when needed

* Use modern build tools (Vite/Next/Rollup) with sensible defaults - these tools optimize automatically

---

## ⭐ Summary — 10-second Interview Version

> "Performance optimization includes monitoring (RUM, Web Vitals), using tools (Lighthouse, DevTools, WebPageTest), network optimization (compression, CDNs, HTTP/2/3), choosing rendering patterns (CSR, SSR, SSG, ISR), and build optimization (code splitting, tree shaking, minification). Measure first, then optimize based on data."

---

