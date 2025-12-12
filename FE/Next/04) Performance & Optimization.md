# ⚡ 4. Performance & Optimization (Q28–37)

---

## 📍 Navigation

<div align="center">

[← Previous: Routing & Navigation](03%29%20Routing%20%26%20Navigation.md) • [Home: README](../README.md) • [Next: Architecture & Best Practices →](05%29%20Architecture%20%26%20Best%20Practices.md)

[📋 Cheatsheet](Next.js%20Interview%20Cheatsheet.md)

</div>

---

---

## Q28. ▲ ▲ ▲ Optimizing images with `next/image`

`next/image` provides automatic optimization (converts to modern formats), lazy loading (loads only when in viewport), and responsive images (serves appropriate size for device) - significantly improves performance. Use `priority` for above-fold images to load immediately, and `placeholder="blur"` to show blur while loading.

- **Trade-offs**: The catch is `next/image` significantly improves performance with automatic optimization and lazy loading, but watch out - you need to provide width and height for proper layout, and external images need to be configured in `next.config.js`.

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

## Q29. 💡 Implementing code splitting and lazy loading

`next/dynamic` enables code splitting (automatically splits code into chunks) and lazy loading of components (loads only when needed) - reduces initial bundle size and improves performance. You can disable SSR for client-only components with `ssr: false`, and show loading UI while component loads.

- **Trade-offs**: The catch is code splitting reduces initial bundle size and components load only when needed, but watch out - you need to provide loading states for better UX, and disabling SSR means the component won't be server-rendered.

Example:

```javascript
import dynamic from 'next/dynamic';

const LazyComponent = dynamic(() => import('./HeavyComponent'), {
  loading: () => <p>Loading...</p>,
  ssr: false
});

```

---

## Q30. ▲ ▲ ▲ Using `next/script` for third-party scripts

`next/script` optimizes third-party script loading with different strategies - `afterInteractive` (loads after page becomes interactive), `beforeInteractive` (loads before page becomes interactive), `lazyOnload` (loads when browser is idle), or `worker` (loads in web worker). Choose strategy based on script importance.

- **Trade-offs**: The catch is `next/script` optimizes script loading for better performance with different strategies for different use cases, but watch out - `beforeInteractive` can block page rendering, so use it sparingly for critical scripts only.

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

## Q31. 💡 Core Web Vitals and how to optimize them

Optimize LCP (Largest Contentful Paint) with `next/image` and `next/font`, FID (First Input Delay) with code splitting to reduce JavaScript execution time, and CLS (Cumulative Layout Shift) with proper sizing and loading states - Core Web Vitals affect SEO and user experience. Load critical resources first with `priority`, and show loading states to prevent layout shifts.

- **Trade-offs**: The catch is Core Web Vitals affect SEO and user experience, and you should use `next/image` and `next/font` for optimization, but watch out - monitor Core Web Vitals in production and set performance budgets to track improvements.

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

SWC is a fast Rust-based compiler that replaces Babel for faster builds - significantly faster builds and better minification than Terser. Enabled by default in Next.js 12+, and supports SWC plugins for customization.

- **Trade-offs**: The catch is SWC provides significantly faster builds and better minification, but watch out - it's enabled by default, so you don't need to configure it, but if you need custom Babel plugins, you might need to use SWC plugins instead.

Example:

```javascript
// next.config.js
const nextConfig = {
  swcMinify: true, // Enabled by default in Next.js 12+
};

```

---

## Q33. 🌊 Implementing streaming in SSR

Streaming sends HTML chunks as they're ready, improving Time to First Byte (TTFB) and providing better perceived performance - page loads progressively. Use Suspense with fallbacks to enable streaming, allowing slow components to load separately.

- **Trade-offs**: The catch is streaming improves TTFB and provides better perceived performance with progressive loading, but watch out - you need to wrap slow components in Suspense with fallbacks, and not all components can be streamed (client components need hydration).

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

Use ISR (Incremental Static Regeneration) for static content with revalidation, edge caching for global performance, and revalidation tags for targeted cache invalidation - caching improves performance significantly. Control caching behavior with headers, and update cache at specified intervals with revalidation.

- **Trade-offs**: The catch is caching improves performance significantly, and you can target specific cache entries for invalidation with tags, but watch out - you need to understand when to use each strategy (ISR for static content, edge caching for global performance, tags for targeted invalidation).

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

Use `next/font` for font optimization (optimizes Google Fonts automatically) and inline critical CSS for faster rendering - reduces layout shifts and improves loading performance. Preload important fonts, and control font loading behavior with `font-display` option.

- **Trade-offs**: The catch is `next/font` reduces layout shifts and improves loading performance, but watch out - you need to configure `font-display` properly (use 'swap' for better UX), and inline critical CSS can increase HTML size slightly.

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

Use Vercel Analytics for Core Web Vitals monitoring, Google Analytics for comprehensive web analytics, and Sentry for error tracking and performance monitoring - performance monitoring is essential for optimization. Set and monitor performance targets (performance budgets), and track actual user experience with real user monitoring.

- **Trade-offs**: The catch is performance monitoring is essential for optimization, and you should monitor Core Web Vitals in production, but watch out - different tools provide different insights, so choose based on your needs (Vercel Analytics for Next.js-specific metrics, Sentry for errors and performance).

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

Avoid blocking SSR calls (use streaming with Suspense), large bundles (use code splitting for heavy libraries), unnecessary client-side JavaScript (use Server Components when possible), and unnecessary re-renders (optimize with React.memo and useMemo) - monitor bundle size and performance metrics with performance budgets.

- **Trade-offs**: The catch is avoid these patterns for better performance, and use Server Components when possible to reduce client-side JS, but watch out - over-optimization can make code harder to maintain, so optimize based on actual performance metrics, not assumptions.

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

---

## 📍 Navigation

<div align="center">

[← Previous: Routing & Navigation](03%29%20Routing%20%26%20Navigation.md) • [Home: README](../README.md) • [Next: Architecture & Best Practices →](05%29%20Architecture%20%26%20Best%20Practices.md)

[📋 Cheatsheet](Next.js%20Interview%20Cheatsheet.md)

</div>

---
