# 🚀 6. Deployment & Tooling (Q49–60)

---

## 📍 Navigation

<div align="center">

[← Previous: Architecture & Best Practices](05%29%20Architecture%20%26%20Best%20Practices.md) • [Home: README](../README.md)

[📋 Cheatsheet](Next.js%20Interview%20Cheatsheet.md)

</div>

---

---

## Q49. ▲ ▲ ▲ Deploying Next.js applications to Vercel

Vercel provides zero-config deployment with automatic deployments on git push, automatic image optimization, edge functions that run at edge locations, global content delivery via CDN, and built-in performance monitoring with analytics - optimized for Next.js.

- **Trade-offs**: The catch is Vercel provides zero-config deployment and runs at edge locations for better performance, but watch out - it's optimized for Next.js, so if you need custom server configurations, you might need other platforms.

Example:

```javascript
// vercel.json configuration
{
  "framework": "nextjs",
  "buildCommand": "npm run build",
  "outputDirectory": ".next"
}

```

---

## Q50. 🖥️ Creating custom servers for Next.js

Create a custom server using `next()` function with Express or Node.js - only needed for specific requirements like custom middleware or server logic. Not recommended for new projects since it may impact performance optimizations.

- **Trade-offs**: The catch is custom servers allow Express integration and custom middleware, but watch out - not recommended for new projects as it may impact performance optimizations, and most use cases can be handled with Next.js built-in features.

Example:

```javascript
const express = require('express');
const next = require('next');

const dev = process.env.NODE_ENV !== 'production';
const app = next({ dev });
const handle = app.getRequestHandler();

app.prepare().then(() => {
  const server = express();
  server.get('*', (req, res) => handle(req, res));
  server.listen(3000);
});

```

---

## Q51. 🏷️ Different build output types

Different build outputs for different deployment targets - standalone (self-contained build for Docker), export (static files for static hosting), default (optimized for Vercel deployment), and edge bundles (optimized for edge runtime). Choose output type based on deployment target.

- **Trade-offs**: The catch is different outputs for different deployment targets (standalone for Docker, export for static hosting, default for Vercel), but watch out - edge bundles are optimized for edge runtime, so choose based on where you're deploying.

Example:

```javascript
// next.config.js
const nextConfig = {
  output: 'standalone', // Self-contained build for Docker
};

```

---

## Q52. 💡 Handling environment-specific settings

Use different `.env` files for different stages (`.env.local` for development, `.env.production` for production) and set environment variables in deployment pipeline (CI/CD) - never commit secrets to version control. Validate environment variables to ensure required ones are present.

- **Trade-offs**: The catch is different configs per environment and set environment variables in CI/CD pipeline, but watch out - never commit secrets to version control, and always validate environment variables to catch missing ones early.

Example:

```javascript
// .env.local (local development)
NEXT_PUBLIC_API_URL=http://localhost:3000/api
DATABASE_URL=postgresql://localhost:5432/dev_db

// .env.staging (staging environment)
NEXT_PUBLIC_API_URL=https://staging-api.example.com

// .env.production (production)
NEXT_PUBLIC_API_URL=https://api.example.com

```

---

## Q53. 📘 Integrating ESLint and TypeScript

Install ESLint and TypeScript packages and configure them for Next.js - TypeScript provides type safety and better development experience, while ESLint catches code quality issues and enforces best practices. Can fail builds on type/ESLint errors for build integration.

- **Trade-offs**: The catch is better IDE support and error detection during development, and can fail builds on errors for quality gates, but watch out - proper configuration is important, and make sure your team understands the rules to avoid build failures.

Example:

```bash
npm install --save-dev typescript @types/react @types/node
npm install --save-dev eslint eslint-config-next

```

---

## Q54. ▲ ▲ ▲ Setting up CI/CD for Next.js applications

Next.js works with various CI/CD platforms - GitHub Actions (popular CI/CD platform), Vercel (automatic deployments from Git), Docker (containerized deployment) - CI/CD improves development workflow with automated testing and deployment. Fail builds on errors for quality gates.

- **Trade-offs**: The catch is CI/CD improves development workflow with automated testing and deployment, but watch out - run tests in CI pipeline, and fail builds on errors to catch issues early before deployment.

Example:

```yaml

# .github/workflows/deploy.yml

name: Deploy to Vercel
on:
  push:
    branches: [main]
jobs:
  deploy:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v2
      - run: npm install
      - run: npm run build

```

---

## Q55. 💡 Implementing static export with `exportPathMap`

Static export generates static HTML files for deployment to any static hosting - very fast loading and good for SEO-friendly sites. Can be hosted on any static hosting since no server is needed, but no server-side features like API routes or Server Components.

- **Trade-offs**: The catch is very fast loading and good for SEO, and can be hosted on any static hosting, but watch out - no server-side features, so you can't use API routes, Server Components, or dynamic rendering.

Example:

```javascript
// next.config.js
const nextConfig = {
  output: 'export',
  trailingSlash: true,
  images: {
    unoptimized: true
  }
};

```

---

## Q56. 🐛 Debugging and profiling Next.js applications

Use browser DevTools for debugging, React Profiler for component performance, Bundle Analyzer for bundle size, and Next.js built-in analyzers - enable source maps for better debugging and monitor Core Web Vitals for performance.

- **Trade-offs**: The catch is debugging tools improve development experience, and enable source maps for better debugging, but watch out - monitor Core Web Vitals in production, and use Next.js built-in analyzers to identify performance bottlenecks.

Example:

```javascript
// next.config.js
const nextConfig = {
  productionBrowserSourceMaps: true,
};

```

---

## Q57. 🎨 Implementing partial prerendering and streaming

Partial prerendering combines static and dynamic content for optimal performance - page loads progressively by sending HTML chunks as they're ready (streaming), which improves Time to First Byte (TTFB) and provides better perceived performance.

- **Trade-offs**: The catch is page loads progressively and improves TTFB, but watch out - sends HTML chunks as they're ready, so you need to use Suspense with fallbacks to handle streaming properly.

Example:

```javascript
import { Suspense } from 'react';

export default function Page() {
  return (
    <div>
      <header>
        <h1>Static Header</h1>
      </header>
      <Suspense fallback={<p>Loading...</p>}>
        <DynamicContent />
      </Suspense>
    </div>
  );
}

```

---

## Q58. 💡 Using Turbopack for faster development

Turbopack is a faster bundler written in Rust that replaces Webpack for development - significantly faster builds and compatible with most Webpack loaders. Currently for development only, but will replace Webpack for production builds in the future.

- **Trade-offs**: The catch is significantly faster builds and compatible with most Webpack loaders, but watch out - currently for development only, so production builds still use Webpack, but this will change in future Next.js versions.

Example:

```javascript
// next.config.js
const nextConfig = {
  experimental: {
    turbo: {
      // Turbopack configuration
    }
  }
};

```

---

## Q59. ▲ ▲ ▲ Migrating from Next.js 12 to Next.js 14

Migrate gradually by moving pages to App Router page by page, updating data fetching patterns (move to Server Components), marking interactive components with 'use client', and updating to new route format for API routes - modern routing with better performance.

- **Trade-offs**: The catch is modern routing with better performance in App Router, and move data fetching to server with Server Components, but watch out - migrate gradually page by page, and mark interactive components with 'use client' since they need client-side JavaScript.

Example:

```javascript
// Step 1: Update Next.js version
// package.json
{
  "dependencies": {
    "next": "14.0.0",
    "react": "18.0.0"
  }
}

```

---

## Q60. 🚀 Best practices for Next.js deployment

Use proper build configuration, optimize assets, enable compression and caching, disable powered-by header, generate ETags, and monitor performance in production - follow deployment best practices for production readiness.

- **Trade-offs**: The catch is enable compression and caching for better performance, and follow deployment best practices for production readiness, but watch out - always monitor performance in production to catch issues early and ensure optimal user experience.

Example:

```javascript
// next.config.js
const nextConfig = {
  output: 'standalone',
  compress: true,
  poweredByHeader: false,
  generateEtags: true,
};

```

---

---

## 📍 Navigation

<div align="center">

[← Previous: Architecture & Best Practices](05%29%20Architecture%20%26%20Best%20Practices.md) • [Home: README](../README.md)

[📋 Cheatsheet](Next.js%20Interview%20Cheatsheet.md)

</div>

---
