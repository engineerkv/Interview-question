# ⚙️ 4. Performance & Optimization (Q28–37)

---

## 28) How does the `next/image` component optimize images?

Concept:
`next/image` provides automatic optimization, lazy loading, and responsive images.

Example:
```javascript
import Image from 'next/image';

export default function OptimizedImage() {
  return (
    <div>
      {/* Basic usage */}
```

Deep Insight:
- **Automatic Optimization**: Converts images to modern formats
- **Lazy Loading**: Images load only when in viewport
- **Responsive**: Serves appropriate size for device
- **Priority**: Above-fold images load immediately
- **Placeholder**: Shows blur while loading

---

## 29) How does code splitting and lazy loading work (`next/dynamic`)?

Concept:
`next/dynamic` enables code splitting and lazy loading of components.

Example:
```javascript
import dynamic from 'next/dynamic';

// Basic lazy loading
const LazyComponent = dynamic(() => import('./HeavyComponent'));

// With loading state
```

Deep Insight:
- **Code Splitting**: Automatically splits code into chunks
- **Lazy Loading**: Components load only when needed
- **SSR Control**: Can disable SSR for client-only components
- **Loading States**: Show loading UI while component loads
- **Performance**: Reduces initial bundle size

---

## 30) What is the purpose of the `next/script` component and strategy options?

Concept:
`next/script` optimizes third-party script loading with different strategies.

Example:
```javascript
import Script from 'next/script';

export default function Page() {
  return (
    <div>
      {/* afterInteractive - after page becomes interactive */}
```

Deep Insight:
- **afterInteractive**: Loads after page becomes interactive
- **beforeInteractive**: Loads before page becomes interactive
- **lazyOnload**: Loads when browser is idle
- **worker**: Loads in web worker
- **Performance**: Optimizes script loading for better performance

---

## 31) How do you optimize Core Web Vitals (LCP, FID, CLS) in Next.js?

Concept:
Optimize LCP with images and fonts, FID with code splitting, and CLS with proper sizing.

Example:
```javascript
// Optimize LCP (Largest Contentful Paint)
import Image from 'next/image';

export default function Hero() {
  return (
    <div>
```

Deep Insight:
- **LCP**: Optimize largest content element (usually images)
- **FID**: Reduce JavaScript execution time
- **CLS**: Prevent layout shifts with proper sizing
- **Priority**: Load critical resources first
- **Skeleton**: Show loading states to prevent shifts

---

## 32) What is SWC and how does it improve compilation and minification performance?

Concept:
SWC is a fast Rust-based compiler that replaces Babel for faster builds.

Example:
```javascript
// next.config.js
/** @type {import('next').NextConfig} */
const nextConfig = {
  // SWC is enabled by default in Next.js 12+
  swcMinify: true,
  
```

Deep Insight:
- **Rust-based**: Much faster than Babel
- **Default**: Enabled by default in Next.js 12+
- **Minification**: Better minification than Terser
- **Plugins**: Supports SWC plugins
- **Performance**: Significantly faster builds

---

## 33) What is streaming in SSR and how does Next 14 leverage it for faster TTFB? (**🚀**)

Concept:
Streaming sends HTML chunks as they're ready, improving Time to First Byte.

Example:
```javascript
// Server Component with streaming
export default async function Page() {
  return (
    <div>
      <h1>Page Title</h1>
      
```

Deep Insight:
- **Streaming**: Sends HTML chunks as they're ready
- **TTFB**: Improves Time to First Byte
- **Suspense**: Enables streaming with fallbacks
- **Progressive**: Page loads progressively
- **Performance**: Better perceived performance

---

## 34) How do you implement caching strategies with ISR and edge caching?

Concept:
Use ISR for static content with revalidation and edge caching for global performance.

Example:
```javascript
// ISR with revalidation
export async function getStaticProps() {
  const posts = await fetch('https://api.example.com/posts');
  const data = await posts.json();
  
  return {
```

Deep Insight:
- **ISR**: Incremental Static Regeneration for static content
- **Edge Caching**: Cache at edge locations for global performance
- **Revalidation**: Update cache at specified intervals
- **Tags**: Target specific cache entries for invalidation
- **Headers**: Control caching behavior with headers

---

## 35) How can you optimize fonts and CSS in Next.js (`next/font`, critical CSS, font display)?

Concept:
Use `next/font` for font optimization and critical CSS for faster rendering.

Example:
```javascript
import { Inter, Roboto } from 'next/font/google';

// Google Fonts optimization
const inter = Inter({
  subsets: ['latin'],
  display: 'swap',
```

Deep Insight:
- **next/font**: Optimizes Google Fonts automatically
- **font-display**: Controls font loading behavior
- **Critical CSS**: Inline critical CSS for faster rendering
- **Preloading**: Preload important fonts
- **Performance**: Reduces layout shifts and improves loading

---

## 36) How do you monitor performance in production (Vercel Analytics, Google Analytics, Sentry)?

Concept:
Use Vercel Analytics for Core Web Vitals and Sentry for error monitoring.

Example:
```javascript
// Vercel Analytics
import { Analytics } from '@vercel/analytics/react';

export default function RootLayout({ children }) {
  return (
    <html>
```

Deep Insight:
- **Vercel Analytics**: Built-in Core Web Vitals monitoring
- **Google Analytics**: Comprehensive web analytics
- **Sentry**: Error tracking and performance monitoring
- **Real User Monitoring**: Track actual user experience
- **Performance Budgets**: Set and monitor performance targets

---

## 37) What are common performance anti-patterns in Next.js (blocking SSR calls, large bundles)?

Concept:
Avoid blocking SSR calls, large bundles, and unnecessary client-side JavaScript.

Example:
```javascript
// ❌ Anti-pattern: Blocking SSR calls
export async function getServerSideProps() {
  // This blocks the entire page
  const slowData = await fetch('https://slow-api.com/data');
  const data = await slowData.json();
  
```

Deep Insight:
- **Blocking SSR**: Avoid slow server-side operations
- **Large Bundles**: Use code splitting for heavy libraries
- **Client-side JS**: Use Server Components when possible
- **Unnecessary Re-renders**: Optimize with React.memo and useMemo
- **Performance Budgets**: Monitor bundle size and performance metrics

---
