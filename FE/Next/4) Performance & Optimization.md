# ⚙️ 4. Performance & Optimization (Q28–37)

---

## 28) How does the `next/image` component optimize images?

`next/image` provides automatic optimization, lazy loading, and responsive images.

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

- **Core Features**: Automatic optimization converts images to modern formats, lazy loading loads images only when in viewport
- **Real-World Use**: Serves appropriate size for device (responsive)
- **Common Practice**: Above-fold images load immediately (priority)
- **Advanced Feature**: Shows blur while loading (placeholder)
- **Interview Tip**: Explain that next/image significantly improves performance

---

## 29) How does code splitting and lazy loading work (`next/dynamic`)?

`next/dynamic` enables code splitting and lazy loading of components.

```javascript
import dynamic from 'next/dynamic';

const LazyComponent = dynamic(() => import('./HeavyComponent'), {
  loading: () => <p>Loading...</p>,
  ssr: false
});
```

- **Core Feature**: Automatically splits code into chunks (code splitting)
- **Real-World Use**: Components load only when needed (lazy loading)
- **Common Configuration**: Can disable SSR for client-only components
- **Advanced Feature**: Show loading UI while component loads (loading states)
- **Interview Tip**: Explain that reduces initial bundle size (performance)

---

## 30) What is the purpose of the `next/script` component and strategy options?

`next/script` optimizes third-party script loading with different strategies.

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

- **Core Strategies**: `afterInteractive` (loads after page becomes interactive), `beforeInteractive` (loads before page becomes interactive), `lazyOnload` (loads when browser is idle)
- **Real-World Use**: `worker` strategy loads in web worker
- **Common Benefit**: Optimizes script loading for better performance
- **Advanced Feature**: Different strategies for different use cases
- **Interview Tip**: Explain that choose strategy based on script importance

---

## 31) How do you optimize Core Web Vitals (LCP, FID, CLS) in Next.js?

Optimize LCP with images and fonts, FID with code splitting, and CLS with proper sizing.

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

- **Core Metrics**: LCP (optimize largest content element, usually images), FID (reduce JavaScript execution time), CLS (prevent layout shifts with proper sizing)
- **Real-World Practice**: Load critical resources first (priority)
- **Common Technique**: Show loading states to prevent shifts (skeleton)
- **Advanced Feature**: Use next/image and next/font for optimization
- **Interview Tip**: Explain that Core Web Vitals affect SEO and user experience

---

## 32) What is SWC and how does it improve compilation and minification performance?

SWC is a fast Rust-based compiler that replaces Babel for faster builds.

```javascript
// next.config.js
const nextConfig = {
  swcMinify: true, // Enabled by default in Next.js 12+
};
```

- **Core Technology**: Rust-based compiler, much faster than Babel
- **Real-World Benefit**: Enabled by default in Next.js 12+
- **Common Advantage**: Better minification than Terser
- **Advanced Feature**: Supports SWC plugins
- **Interview Tip**: Explain that significantly faster builds (performance)

---

## 33) What is streaming in SSR and how does Next 14 leverage it for faster TTFB? (**🚀**)

Streaming sends HTML chunks as they're ready, improving Time to First Byte.

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

- **Core Concept**: Sends HTML chunks as they're ready (streaming)
- **Real-World Benefit**: Improves Time to First Byte (TTFB)
- **Common Use**: Enables streaming with fallbacks (Suspense)
- **Advanced Feature**: Page loads progressively
- **Interview Tip**: Explain that better perceived performance

---

## 34) How do you implement caching strategies with ISR and edge caching?

Use ISR for static content with revalidation and edge caching for global performance.

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

- **Core Strategies**: ISR (Incremental Static Regeneration for static content), Edge caching (cache at edge locations for global performance)
- **Real-World Use**: Update cache at specified intervals (revalidation)
- **Common Practice**: Target specific cache entries for invalidation (tags)
- **Advanced Feature**: Control caching behavior with headers
- **Interview Tip**: Explain that caching improves performance significantly

---

## 35) How can you optimize fonts and CSS in Next.js (`next/font`, critical CSS, font display)?

Use `next/font` for font optimization and critical CSS for faster rendering.

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

- **Core Feature**: `next/font` optimizes Google Fonts automatically
- **Real-World Use**: Controls font loading behavior (font-display)
- **Common Practice**: Inline critical CSS for faster rendering
- **Advanced Feature**: Preload important fonts
- **Interview Tip**: Explain that reduces layout shifts and improves loading (performance)

---

## 36) How do you monitor performance in production (Vercel Analytics, Google Analytics, Sentry)?

Use Vercel Analytics for Core Web Vitals and Sentry for error monitoring.

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

- **Core Tools**: Vercel Analytics (built-in Core Web Vitals monitoring), Google Analytics (comprehensive web analytics), Sentry (error tracking and performance monitoring)
- **Real-World Use**: Track actual user experience (real user monitoring)
- **Common Practice**: Set and monitor performance targets (performance budgets)
- **Advanced Feature**: Monitor Core Web Vitals in production
- **Interview Tip**: Explain that performance monitoring is essential for optimization

---

## 37) What are common performance anti-patterns in Next.js (blocking SSR calls, large bundles)?

Avoid blocking SSR calls, large bundles, and unnecessary client-side JavaScript.

```javascript
// ❌ Anti-pattern: Blocking SSR calls
export async function getServerSideProps() {
  const slowData = await fetch('https://slow-api.com/data');
  const data = await slowData.json();
  return { props: { data } };
}

// ✅ Better: Use streaming with Suspense
```

- **Common Anti-patterns**: Blocking SSR (avoid slow server-side operations), large bundles (use code splitting for heavy libraries)
- **Real-World Impact**: Use Server Components when possible (reduce client-side JS)
- **Common Mistake**: Unnecessary re-renders (optimize with React.memo and useMemo)
- **Advanced Practice**: Monitor bundle size and performance metrics (performance budgets)
- **Interview Tip**: Explain that avoid these patterns for better performance

---
