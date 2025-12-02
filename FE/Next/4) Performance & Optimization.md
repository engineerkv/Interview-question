<div align="center">

**[← Previous: Routing & Navigation](3%29%20Routing%20%26%20Navigation.md)** | **[Next: Architecture & Best Practices →](5%29%20Architecture%20%26%20Best%20Practices.md)**

</div>

# ⚡ 4. Performance & Optimization (Q28–37)

---

## Q28. 💡 Optimizing images with `next/image`

`next/image` provides automatic optimization, lazy loading, and responsive images - next/image significantly improves performance. Automatic optimization converts images to modern formats, lazy loading loads images only when in viewport.

- **Trade-offs**: The catch is above-fold images load immediately (priority) - shows blur while loading (placeholder). Next-image significantly improves performance, but watch out - serves appropriate size for device (responsive).

Example:

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

## Q29. 🔧 Implementing code splitting and lazy loading

`next/dynamic` enables code splitting and lazy loading of components - reduces initial bundle size (performance). Automatically splits code into chunks (code splitting).

- **Trade-offs**: The catch is can disable SSR for client-only components - show loading UI while component loads (loading states). Reduces initial bundle size (performance), but watch out - components load only when needed (lazy loading).

Example:

```javascript
import dynamic from 'next/dynamic';

const LazyComponent = dynamic(() => import('./HeavyComponent'), {
  loading: () => <p>Loading...</p>,
  ssr: false
});

```

---

## Q30. 💡 Using `next/script` for third-party scripts

`next/script` optimizes third-party script loading with different strategies - choose strategy based on script importance. `afterInteractive` (loads after page becomes interactive), `beforeInteractive` (loads before page becomes interactive), `lazyOnload` (loads when browser is idle).

- **Trade-offs**: The catch is optimizes script loading for better performance - different strategies for different use cases. Choose strategy based on script importance, but watch out - `worker` strategy loads in web worker.

Example:

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

## Q31. ⚡ Core Web Vitals and how to optimize them

Optimize LCP with images and fonts, FID with code splitting, and CLS with proper sizing - Core Web Vitals affect SEO and user experience. LCP (optimize largest content element, usually images), FID (reduce JavaScript execution time), CLS (prevent layout shifts with proper sizing).

- **Trade-offs**: The catch is show loading states to prevent shifts (skeleton) - use next/image and next/font for optimization. Core Web Vitals affect SEO and user experience, but watch out - load critical resources first (priority).

Example:

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

## Q32. ⚡ How SWC improves build performance

SWC is a fast Rust-based compiler that replaces Babel for faster builds - significantly faster builds (performance). Rust-based compiler, much faster than Babel.

- **Trade-offs**: The catch is better minification than Terser - supports SWC plugins. Significantly faster builds (performance), but watch out - enabled by default in Next.js 12+.

Example:

```javascript
// next.config.js
const nextConfig = {
  swcMinify: true, // Enabled by default in Next.js 12+
};

```

---

## Q33. 🌊 Implementing streaming in SSR

Streaming sends HTML chunks as they're ready, improving Time to First Byte - better perceived performance. Sends HTML chunks as they're ready (streaming).

- **Trade-offs**: The catch is enables streaming with fallbacks (Suspense) - page loads progressively. Better perceived performance, but watch out - improves Time to First Byte (TTFB).

Example:

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

## Q34. 💾 Different caching strategies in Next.js

Use ISR for static content with revalidation and edge caching for global performance - caching improves performance significantly. ISR (Incremental Static Regeneration for static content), Edge caching (cache at edge locations for global performance).

- **Trade-offs**: The catch is target specific cache entries for invalidation (tags) - control caching behavior with headers. Caching improves performance significantly, but watch out - update cache at specified intervals (revalidation).

Example:

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

## Q35. 🎨 Optimizing fonts and CSS in Next.js

Use `next/font` for font optimization and critical CSS for faster rendering - reduces layout shifts and improves loading (performance). `next/font` optimizes Google Fonts automatically.

- **Trade-offs**: The catch is inline critical CSS for faster rendering - preload important fonts. Reduces layout shifts and improves loading (performance), but watch out - controls font loading behavior (font-display).

Example:

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

## Q36. ⚡ Monitoring performance in Next.js applications

Use Vercel Analytics for Core Web Vitals and Sentry for error monitoring - performance monitoring is essential for optimization. Vercel Analytics (built-in Core Web Vitals monitoring), Google Analytics (comprehensive web analytics), Sentry (error tracking and performance monitoring).

- **Trade-offs**: The catch is set and monitor performance targets (performance budgets) - monitor Core Web Vitals in production. Performance monitoring is essential for optimization, but watch out - track actual user experience (real user monitoring).

Example:

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

## Q37. ⚡ Common performance anti-patterns to avoid

Avoid blocking SSR calls, large bundles, and unnecessary client-side JavaScript - avoid these patterns for better performance. Blocking SSR (avoid slow server-side operations), large bundles (use code splitting for heavy libraries).

- **Trade-offs**: The catch is unnecessary re-renders (optimize with React.memo and useMemo) - monitor bundle size and performance metrics (performance budgets). Avoid these patterns for better performance, but watch out - use Server Components when possible (reduce client-side JS).

Example:

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

<div align="center">

**[← Previous: Routing & Navigation](3%29%20Routing%20%26%20Navigation.md)** | **[Next: Architecture & Best Practices →](5%29%20Architecture%20%26%20Best%20Practices.md)**

</div>

