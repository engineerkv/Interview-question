# 6. Deployment & Tooling (Q49–60)

---

## Q49. Deploying Next.js applications to Vercel

Vercel automatically optimizes images, enables edge functions, and provides analytics - Vercel provides zero-config deployment. Automatic deployments on git push, automatic image optimization.

- **Trade-offs**: The catch is global content delivery (CDN) - built-in performance monitoring (analytics). Vercel provides zero-config deployment, but watch out - runs at edge locations (edge functions).

Example:

```javascript
// vercel.json configuration
{
  "framework": "nextjs",
  "buildCommand": "npm run build",
  "outputDirectory": ".next"
}
```

<div align="center">

**[← Previous: Architecture & Best Practices](5%29%20Architecture%20%26%20Best%20Practices.md)** | **[Next: Question List →](question.md)**

</div>

---

## Q50. Creating custom servers for Next.js

Create a custom server using `next()` function with Express or Node.js - not recommended for new projects (legacy). Only needed for specific requirements (custom server).

- **Trade-offs**: The catch is use Node.js for custom server logic - may impact performance optimizations (performance). Not recommended for new projects (legacy), but watch out - use Express for custom middleware (Express integration).

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

## Q51. Different build output types

Different build outputs for different deployment targets and optimization levels - choose output type based on deployment target. Standalone (self-contained build for Docker), Export (static files for static hosting), Default (optimized for Vercel deployment).

- **Trade-offs**: The catch is standalone output works well with containers (Docker) - different outputs for different deployment targets. Choose output type based on deployment target, but watch out - edge bundles optimized for edge runtime.

Example:

```javascript
// next.config.js
const nextConfig = {
  output: 'standalone', // Self-contained build for Docker
};
```

---

## Q52. Handling environment-specific settings

Use different `.env` files and environment variables for different deployment stages - set environment variables in deployment pipeline (CI/CD). Use different `.env` files for different stages (environment files).

- **Trade-offs**: The catch is different configs per environment - never commit secrets to version control (security). Set environment variables in deployment pipeline (CI/CD), but watch out - validate environment variables.

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

## Q53. Integrating ESLint and TypeScript

Install ESLint and TypeScript packages and configure them for Next.js - better IDE support and error detection (development). TypeScript provides type safety and better development experience.

- **Trade-offs**: The catch is proper configuration is important - can fail builds on type/ESLint errors (build integration). Better IDE support and error detection (development), but watch out - ESLint catches code quality issues and enforces best practices.

Example:

```bash
npm install --save-dev typescript @types/react @types/node
npm install --save-dev eslint eslint-config-next
```

---

## Q54. Setting up CI/CD for Next.js applications

Next.js works with various CI/CD platforms for automated deployment - CI/CD improves development workflow. GitHub Actions (popular CI/CD platform), Vercel (automatic deployments from Git), Docker (containerized deployment).

- **Trade-offs**: The catch is fail builds on errors (quality gates) - automated testing and deployment. CI/CD improves development workflow, but watch out - run tests in CI pipeline (testing).

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

## Q55. Implementing static export with `exportPathMap`

Static export generates static HTML files for deployment to any static hosting - good for SEO-friendly sites (SEO). Generates static HTML files (static export).

- **Trade-offs**: The catch is no server-side features - very fast loading (performance). Good for SEO-friendly sites (SEO), but watch out - can be hosted on any static hosting (no server).

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

## Q56. Debugging and profiling Next.js applications

Use browser DevTools, React Profiler, and Next.js built-in analyzers - debugging tools improve development experience. Use browser DevTools for debugging, React Profiler for component performance, Bundle Analyzer for bundle size.

- **Trade-offs**: The catch is monitor Core Web Vitals (performance) - use Next.js built-in analyzers. Debugging tools improve development experience, but watch out - enable source maps for better debugging.

Example:

```javascript
// next.config.js
const nextConfig = {
  productionBrowserSourceMaps: true,
};
```

---

## Q57. Implementing partial prerendering and streaming

Partial prerendering combines static and dynamic content for optimal performance - page loads progressively. Combines static and dynamic content (partial prerendering).

- **Trade-offs**: The catch is better perceived performance - improves Time to First Byte (TTFB). Page loads progressively, but watch out - sends HTML chunks as they're ready (streaming).

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

## Q58. Using Turbopack for faster development

Turbopack is a faster bundler written in Rust, replacing Webpack for development - will replace Webpack for production builds (future). Rust-based bundler, much faster than Webpack.

- **Trade-offs**: The catch is compatible with most Webpack loaders - significantly faster builds (performance). Will replace Webpack for production builds (future), but watch out - currently for development only.

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

## Q59. Migrating from Next.js 12 to Next.js 14

Migrate gradually by moving pages to App Router and updating data fetching patterns - mark interactive components with 'use client' (client components). Migrate page by page (gradual migration).

- **Trade-offs**: The catch is move data fetching to server (Server Components) - update to new route format (API routes). Mark interactive components with 'use client' (client components), but watch out - modern routing with better performance (App Router).

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

## Q60. Best practices for Next.js deployment

Use proper build configuration, optimize assets, enable caching, and monitor performance - follow deployment best practices for production readiness. Use proper build configuration, optimize assets, enable caching.

- **Trade-offs**: The catch is enable compression and caching - follow deployment best practices for production readiness. Follow deployment best practices for production readiness, but watch out - monitor performance in production.

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

<div align="center">

**[← Previous: Architecture & Best Practices](5%29%20Architecture%20%26%20Best%20Practices.md)** | **[Next: Question List →](question.md)**

</div>
