# 🚀 6. Deployment & Tooling (Q49–60)

---

## 🧩 Q49. How do you deploy Next.js applications to Vercel?

### 🧠 Concept

Vercel automatically optimizes images, enables edge functions, and provides analytics. Vercel provides zero-config deployment.

---

### 💡 Example

```javascript
// vercel.json configuration
{
  "framework": "nextjs",
  "buildCommand": "npm run build",
  "outputDirectory": ".next"
}
```

---

### 🔍 Deep Insights

* **Rule:** Automatic deployments on git push, automatic image optimization.
* **Use Case:** Runs at edge locations (edge functions).
* **Common Mistake:** Global content delivery (CDN).
* **Pro Tip:** Built-in performance monitoring (analytics).

---

### ⭐ Senior Takeaway

Vercel provides zero-config deployment.

---

## 🧩 Q50. How do you create custom servers for Next.js?

### 🧠 Concept

Create a custom server using `next()` function with Express or Node.js. Not recommended for new projects (legacy).

---

### 💡 Example

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

### 🔍 Deep Insights

* **Rule:** Only needed for specific requirements (custom server).
* **Use Case:** Use Express for custom middleware (Express integration).
* **Common Mistake:** Use Node.js for custom server logic.
* **Pro Tip:** May impact performance optimizations (performance).

---

### ⭐ Senior Takeaway

Not recommended for new projects (legacy).

---

## 🧩 Q51. What are the different build output types?

### 🧠 Concept

Different build outputs for different deployment targets and optimization levels. Choose output type based on deployment target.

---

### 💡 Example

```javascript
// next.config.js
const nextConfig = {
  output: 'standalone', // Self-contained build for Docker
};
```

---

### 🔍 Deep Insights

* **Rule:** Standalone (self-contained build for Docker), Export (static files for static hosting), Default (optimized for Vercel deployment).
* **Use Case:** Edge bundles optimized for edge runtime.
* **Common Mistake:** Standalone output works well with containers (Docker).
* **Pro Tip:** Different outputs for different deployment targets.

---

### ⭐ Senior Takeaway

Choose output type based on deployment target.

---

## 🧩 Q52. How do you handle environment-specific settings?

### 🧠 Concept

Use different `.env` files and environment variables for different deployment stages. Set environment variables in deployment pipeline (CI/CD).

---

### 💡 Example

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

### 🔍 Deep Insights

* **Rule:** Use different `.env` files for different stages (environment files).
* **Use Case:** Validate environment variables.
* **Common Mistake:** Different configs per environment.
* **Pro Tip:** Never commit secrets to version control (security).

---

### ⭐ Senior Takeaway

Set environment variables in deployment pipeline (CI/CD).

---

## 🧩 Q53. How do you integrate ESLint and TypeScript?

### 🧠 Concept

Install ESLint and TypeScript packages and configure them for Next.js. Better IDE support and error detection (development).

---

### 💡 Example

```bash
npm install --save-dev typescript @types/react @types/node
npm install --save-dev eslint eslint-config-next
```

---

### 🔍 Deep Insights

* **Rule:** TypeScript provides type safety and better development experience.
* **Use Case:** ESLint catches code quality issues and enforces best practices.
* **Common Mistake:** Proper configuration is important.
* **Pro Tip:** Can fail builds on type/ESLint errors (build integration).

---

### ⭐ Senior Takeaway

Better IDE support and error detection (development).

---

## 🧩 Q54. How do you set up CI/CD for Next.js applications?

### 🧠 Concept

Next.js works with various CI/CD platforms for automated deployment. CI/CD improves development workflow.

---

### 💡 Example

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

### 🔍 Deep Insights

* **Rule:** GitHub Actions (popular CI/CD platform), Vercel (automatic deployments from Git), Docker (containerized deployment).
* **Use Case:** Run tests in CI pipeline (testing).
* **Common Mistake:** Fail builds on errors (quality gates).
* **Pro Tip:** Automated testing and deployment.

---

### ⭐ Senior Takeaway

CI/CD improves development workflow.

---

## 🧩 Q55. How do you implement static export with `exportPathMap`?

### 🧠 Concept

Static export generates static HTML files for deployment to any static hosting. Good for SEO-friendly sites (SEO).

---

### 💡 Example

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

### 🔍 Deep Insights

* **Rule:** Generates static HTML files (static export).
* **Use Case:** Can be hosted on any static hosting (no server).
* **Common Mistake:** No server-side features.
* **Pro Tip:** Very fast loading (performance).

---

### ⭐ Senior Takeaway

Good for SEO-friendly sites (SEO).

---

## 🧩 Q56. How do you debug and profile Next.js applications?

### 🧠 Concept

Use browser DevTools, React Profiler, and Next.js built-in analyzers. Debugging tools improve development experience.

---

### 💡 Example

```javascript
// next.config.js
const nextConfig = {
  productionBrowserSourceMaps: true,
};
```

---

### 🔍 Deep Insights

* **Rule:** Use browser DevTools for debugging, React Profiler for component performance, Bundle Analyzer for bundle size.
* **Use Case:** Enable source maps for better debugging.
* **Common Mistake:** Monitor Core Web Vitals (performance).
* **Pro Tip:** Use Next.js built-in analyzers.

---

### ⭐ Senior Takeaway

Debugging tools improve development experience.

---

## 🧩 Q57. How do you implement partial prerendering and streaming?

### 🧠 Concept

Partial prerendering combines static and dynamic content for optimal performance. Page loads progressively.

---

### 💡 Example

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

### 🔍 Deep Insights

* **Rule:** Combines static and dynamic content (partial prerendering).
* **Use Case:** Sends HTML chunks as they're ready (streaming).
* **Common Mistake:** Better perceived performance.
* **Pro Tip:** Improves Time to First Byte (TTFB).

---

### ⭐ Senior Takeaway

Page loads progressively.

---

## 🧩 Q58. How do you use Turbopack for faster development?

### 🧠 Concept

Turbopack is a faster bundler written in Rust, replacing Webpack for development. Will replace Webpack for production builds (future).

---

### 💡 Example

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

### 🔍 Deep Insights

* **Rule:** Rust-based bundler, much faster than Webpack.
* **Use Case:** Currently for development only.
* **Common Mistake:** Compatible with most Webpack loaders.
* **Pro Tip:** Significantly faster builds (performance).

---

### ⭐ Senior Takeaway

Will replace Webpack for production builds (future).

---

## 🧩 Q59. How do you migrate from Next.js 12 to Next.js 14?

### 🧠 Concept

Migrate gradually by moving pages to App Router and updating data fetching patterns. Mark interactive components with 'use client' (client components).

---

### 💡 Example

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

### 🔍 Deep Insights

* **Rule:** Migrate page by page (gradual migration).
* **Use Case:** Modern routing with better performance (App Router).
* **Common Mistake:** Move data fetching to server (Server Components).
* **Pro Tip:** Update to new route format (API routes).

---

### ⭐ Senior Takeaway

Mark interactive components with 'use client' (client components).

---

## 🧩 Q60. What are the best practices for Next.js deployment?

### 🧠 Concept

Use proper build configuration, optimize assets, enable caching, and monitor performance. Follow deployment best practices for production readiness.

---

### 💡 Example

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

### 🔍 Deep Insights

* **Rule:** Use proper build configuration, optimize assets, enable caching.
* **Use Case:** Monitor performance in production.
* **Common Mistake:** Enable compression and caching.
* **Pro Tip:** Follow deployment best practices for production readiness.

---

### ⭐ Senior Takeaway

Follow deployment best practices for production readiness.

---
