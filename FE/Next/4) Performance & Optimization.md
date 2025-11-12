# ⚙️ 4. Performance & Optimization (Q28–37)

---

## 🧩 Q28. How do you optimize images with `next/image`?

### 🧠 Concept

`next/image` provides automatic optimization, lazy loading, and responsive images. Next/image significantly improves performance.

---

### 💡 Example

```javascript
import Image from 'next/image';

export default function OptimizedImage() {
  return (
    <Image
      src="/hero.jpg"
      alt="Hero"
      width={800}
      height={600}
      priority
      placeholder="blur"
    />
  );
}
```

---

### 🔍 Deep Insights

* **Rule:** Automatic optimization converts images to modern formats, lazy loading loads images only when in viewport.
* **Use Case:** Serves appropriate size for device (responsive).
* **Common Mistake:** Above-fold images load immediately (priority).
* **Pro Tip:** Shows blur while loading (placeholder).

---

### ⭐ Senior Takeaway

Next-image significantly improves performance.

---

## 🧩 Q29. How do you implement code splitting and lazy loading?

### 🧠 Concept

`next/dynamic` enables code splitting and lazy loading of components. Reduces initial bundle size (performance).

---

### 💡 Example

```javascript
import dynamic from 'next/dynamic';

const LazyComponent = dynamic(() => import('./HeavyComponent'), {
  loading: () => <p>Loading...</p>,
  ssr: false
});
```

---

### 🔍 Deep Insights

* **Rule:** Automatically splits code into chunks (code splitting).
* **Use Case:** Components load only when needed (lazy loading).
* **Common Mistake:** Can disable SSR for client-only components.
* **Pro Tip:** Show loading UI while component loads (loading states).

---

### ⭐ Senior Takeaway

Reduces initial bundle size (performance).

---

## 🧩 Q30. How do you use `next/script` for third-party scripts?

### 🧠 Concept

`next/script` optimizes third-party script loading with different strategies. Choose strategy based on script importance.

---

### 💡 Example

```javascript
import Script from 'next/script';

export default function Page() {
  return (
    <div>
      <Script
        src="https://example.com/script.js"
        strategy="afterInteractive"
      />
    </div>
  );
}
```

---

### 🔍 Deep Insights

* **Rule:** `afterInteractive` (loads after page becomes interactive), `beforeInteractive` (loads before page becomes interactive), `lazyOnload` (loads when browser is idle).
* **Use Case:** `worker` strategy loads in web worker.
* **Common Mistake:** Optimizes script loading for better performance.
* **Pro Tip:** Different strategies for different use cases.

---

### ⭐ Senior Takeaway

Choose strategy based on script importance.

---

## 🧩 Q31. What are Core Web Vitals and how do you optimize them?

### 🧠 Concept

Optimize LCP with images and fonts, FID with code splitting, and CLS with proper sizing. Core Web Vitals affect SEO and user experience.

---

### 💡 Example

```javascript
import Image from 'next/image';

export default function Hero() {
  return (
    <div>
      <Image
        src="/hero.jpg"
        alt="Hero"
        width={1200}
        height={600}
        priority
      />
    </div>
  );
}
```

---

### 🔍 Deep Insights

* **Rule:** LCP (optimize largest content element, usually images), FID (reduce JavaScript execution time), CLS (prevent layout shifts with proper sizing).
* **Use Case:** Load critical resources first (priority).
* **Common Mistake:** Show loading states to prevent shifts (skeleton).
* **Pro Tip:** Use next/image and next/font for optimization.

---

### ⭐ Senior Takeaway

Core Web Vitals affect SEO and user experience.

---

## 🧩 Q32. How does SWC improve build performance?

### 🧠 Concept

SWC is a fast Rust-based compiler that replaces Babel for faster builds. Significantly faster builds (performance).

---

### 💡 Example

```javascript
// next.config.js
const nextConfig = {
  swcMinify: true, // Enabled by default in Next.js 12+
};
```

---

### 🔍 Deep Insights

* **Rule:** Rust-based compiler, much faster than Babel.
* **Use Case:** Enabled by default in Next.js 12+.
* **Common Mistake:** Better minification than Terser.
* **Pro Tip:** Supports SWC plugins.

---

### ⭐ Senior Takeaway

Significantly faster builds (performance).

---

## 🧩 Q33. How do you implement streaming in SSR?

### 🧠 Concept

Streaming sends HTML chunks as they're ready, improving Time to First Byte. Better perceived performance.

---

### 💡 Example

```javascript
import { Suspense } from 'react';

export default async function Page() {
  return (
    <div>
      <h1>Page Title</h1>
      <Suspense fallback={<p>Loading...</p>}>
        <SlowComponent />
      </Suspense>
    </div>
  );
}
```

---

### 🔍 Deep Insights

* **Rule:** Sends HTML chunks as they're ready (streaming).
* **Use Case:** Improves Time to First Byte (TTFB).
* **Common Mistake:** Enables streaming with fallbacks (Suspense).
* **Pro Tip:** Page loads progressively.

---

### ⭐ Senior Takeaway

Better perceived performance.

---

## 🧩 Q34. What are the different caching strategies in Next.js?

### 🧠 Concept

Use ISR for static content with revalidation and edge caching for global performance. Caching improves performance significantly.

---

### 💡 Example

```javascript
// ISR with revalidation
export async function getStaticProps() {
  const posts = await fetch('https://api.example.com/posts');
  const data = await posts.json();
  
  return {
    props: { data },
    revalidate: 60
  };
}
```

---

### 🔍 Deep Insights

* **Rule:** ISR (Incremental Static Regeneration for static content), Edge caching (cache at edge locations for global performance).
* **Use Case:** Update cache at specified intervals (revalidation).
* **Common Mistake:** Target specific cache entries for invalidation (tags).
* **Pro Tip:** Control caching behavior with headers.

---

### ⭐ Senior Takeaway

Caching improves performance significantly.

---

## 🧩 Q35. How do you optimize fonts and CSS in Next.js?

### 🧠 Concept

Use `next/font` for font optimization and critical CSS for faster rendering. Reduces layout shifts and improves loading (performance).

---

### 💡 Example

```javascript
import { Inter } from 'next/font/google';

const inter = Inter({
  subsets: ['latin'],
  display: 'swap',
});

export default function RootLayout({ children }) {
  return (
    <html className={inter.className}>
      <body>{children}</body>
    </html>
  );
}
```

---

### 🔍 Deep Insights

* **Rule:** `next/font` optimizes Google Fonts automatically.
* **Use Case:** Controls font loading behavior (font-display).
* **Common Mistake:** Inline critical CSS for faster rendering.
* **Pro Tip:** Preload important fonts.

---

### ⭐ Senior Takeaway

Reduces layout shifts and improves loading (performance).

---

## 🧩 Q36. How do you monitor performance in Next.js applications?

### 🧠 Concept

Use Vercel Analytics for Core Web Vitals and Sentry for error monitoring. Performance monitoring is essential for optimization.

---

### 💡 Example

```javascript
import { Analytics } from '@vercel/analytics/react';

export default function RootLayout({ children }) {
  return (
    <html>
      <body>
        {children}
        <Analytics />
      </body>
    </html>
  );
}
```

---

### 🔍 Deep Insights

* **Rule:** Vercel Analytics (built-in Core Web Vitals monitoring), Google Analytics (comprehensive web analytics), Sentry (error tracking and performance monitoring).
* **Use Case:** Track actual user experience (real user monitoring).
* **Common Mistake:** Set and monitor performance targets (performance budgets).
* **Pro Tip:** Monitor Core Web Vitals in production.

---

### ⭐ Senior Takeaway

Performance monitoring is essential for optimization.

---

## 🧩 Q37. What are common performance anti-patterns to avoid?

### 🧠 Concept

Avoid blocking SSR calls, large bundles, and unnecessary client-side JavaScript. Avoid these patterns for better performance.

---

### 💡 Example

```javascript
// ❌ Anti-pattern: Blocking SSR calls
export async function getServerSideProps() {
  const slowData = await fetch('https://slow-api.com/data');
  const data = await slowData.json();
  return { props: { data } };
}

// ✅ Better: Use streaming with Suspense
```

---

### 🔍 Deep Insights

* **Rule:** Blocking SSR (avoid slow server-side operations), large bundles (use code splitting for heavy libraries).
* **Use Case:** Use Server Components when possible (reduce client-side JS).
* **Common Mistake:** Unnecessary re-renders (optimize with React.memo and useMemo).
* **Pro Tip:** Monitor bundle size and performance metrics (performance budgets).

---

### ⭐ Senior Takeaway

Avoid these patterns for better performance.

---
