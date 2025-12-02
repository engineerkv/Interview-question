<div align="center">

**[← Previous: Testing](11%29%20Testing.md)** | **[Next: Database & Caching →](13%29%20Database%20%26%20Caching.md)**

</div>

# ⚡ Performance

---

## Q75. Performance Monitoring

Performance monitoring is about continuously measuring how real users experience your app in production. It helps you catch regressions early and prioritize the fixes that matter most. Understanding performance metrics and how to monitor them effectively is crucial for keeping your app fast and responsive. For performance testing methodology, see [Q73. Performance Testing](11%29%20Testing.md#q73-performance-testing).

---

## 1. What to monitor

### 🔹 Core Web Vitals

* **LCP (Largest Contentful Paint)** – loading speed - how fast the main content appears
* **FID/INP (First Input Delay / Interaction to Next Paint)** – interactivity - how responsive the page feels when you click
* **CLS (Cumulative Layout Shift)** – visual stability - how much things jump around while loading

### 🔹 Other useful metrics

* Time to First Byte (TTFB) - how fast the server responds
* First Contentful Paint (FCP) - when users first see something on screen
* JavaScript errors, slow API calls, long tasks - things that make the app feel slow

📌 **In simple terms**: Performance monitoring tells you “how fast is the app for real users right now?”

---

## 2. How to implement (frontend view)

* Use Real User Monitoring (RUM) tools (e.g., browser APIs + custom beacons, or vendors like New Relic/Datadog/Sentry) - these collect data from real users
* Collect:
  * Web Vitals via `web-vitals` library - track LCP, INP, CLS automatically
  * Errors via `window.onerror` / `unhandledrejection` - catch JavaScript errors
* Tag events with:
  * User/device info (anonymized) - know what devices/browsers are slow
  * Page/route, release version, experiment flags - see which pages or versions are slow

---

## ⭐ Summary — 10-second Interview Version

> "Performance monitoring collects Web Vitals and other metrics from real users so we know how the app behaves in production. I integrate RUM, track LCP/INP/CLS, and use that data to guide optimizations."

---

## ⭐ Extra Points (If Interviewer Asks More)

### How do you avoid privacy issues?

Anonymize user IDs, avoid logging PII, and aggregate metrics rather than storing raw user data.

---

## Q76. Performance Tools

Performance tools help you analyze where time is spent so you can target optimizations effectively. Different tools answer different questions - think of them as different lenses to look at performance.

---

## 1. Key tools and when to use them

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

## ⭐ Summary — 10-second Interview Version

> "I use Lighthouse for quick audits, DevTools for detailed CPU/network profiling, and WebPageTest for realistic page load analysis. Together these tools show me where to optimize."

---

## ⭐ Extra Points (If Interviewer Asks More)

### How do you share results with the team?

Save Lighthouse reports, screenshot key DevTools traces, and track WebPageTest links in tickets or documentation.

---

## Q77. Network Optimization

Network optimization reduces the cost and latency of downloading resources. It's often the biggest win for first load performance - you can see huge improvements just by optimizing how resources are delivered.

---

## 1. Techniques

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

## ⭐ Summary — 10-second Interview Version

> "Network optimization is about shipping fewer, smaller, and closer resources—compression, CDNs, HTTP/2/3, and smart resource hints."

---

## ⭐ Extra Points (If Interviewer Asks More)

### How do you pick what to preload?

Preload only the resources that block rendering of above-the-fold content (critical CSS, main bundle, key fonts).

---

## Q78. Rendering Patterns

Rendering patterns describe where and when HTML is generated: in the browser, on the server, or ahead of time. Choosing the right pattern balances performance, SEO, and complexity - each pattern has trade-offs you need to consider.

---

## 1. Common patterns

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

## 2. Choosing a pattern

* SEO-critical + dynamic → SSR / ISR - need SEO but data changes, use server rendering
* Mostly static marketing content → SSG - pre-generate everything, super fast
* Heavy interactive dashboard behind auth → CSR + API calls - no SEO needed, focus on interactivity

---

## ⭐ Summary — 10-second Interview Version

> "CSR builds UI in the browser, SSR renders HTML on each request, and SSG/ISR pre-generates pages. I mix them based on SEO needs, data freshness, and complexity."

---

## ⭐ Extra Points (If Interviewer Asks More)

### Where do streaming and partial hydration fit?

Streaming and partial hydration are advanced SSR techniques that allow you to start streaming HTML early and hydrate only parts of the page to reduce JS cost.

---

## Q79. Build Optimization

Build optimization reduces JavaScript bundle size and improves how code is delivered to the browser. It directly affects load time and interactivity - smaller bundles mean faster downloads and quicker page loads.

---

## 1. Techniques

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

## 2. Frontend workflow

* Run bundle analyzers (Webpack Bundle Analyzer, Source Map Explorer) - see what's making your bundles big
* Identify heavy dependencies and lazy-load where possible - load big libraries only when needed
* Use modern build tools (Vite/Next/Rollup) with sensible defaults - these tools optimize automatically

---

## ⭐ Summary — 10-second Interview Version

> "Build optimization focuses on shrinking and splitting bundles so the browser downloads less JS upfront. I use code splitting, tree shaking, and bundle analysis to keep first load fast."

---

## ⭐ Extra Points (If Interviewer Asks More)

### Example trade-off?

Too much code splitting can increase the number of network requests and hurt performance on slow networks; you need a balance.

---

<div align="center">

**[← Previous: Testing](11%29%20Testing.md)** | **[Next: Database & Caching →](13%29%20Database%20%26%20Caching.md)**

</div>