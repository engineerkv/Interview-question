# 🚀 6. Deployment & Tooling (Q49–60)

---

## 49) How do you deploy a Next.js 14 app to Vercel and what automatic optimizations does it apply?

Vercel automatically optimizes images, enables edge functions, and provides analytics.

```javascript
// vercel.json configuration
{
  "framework": "nextjs",
  "buildCommand": "npm run build",
  "outputDirectory": ".next"
}
```

- **Core Features**: Automatic deployments on git push, automatic image optimization
- **Real-World Use**: Runs at edge locations (edge functions)
- **Common Benefit**: Global content delivery (CDN)
- **Advanced Feature**: Built-in performance monitoring (analytics)
- **Interview Tip**: Explain that Vercel provides zero-config deployment

---

## 50) How do you set up a custom server for Next.js (Node.js or Express integration)? (**⚙️ legacy**)

Create a custom server using `next()` function with Express or Node.js.

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

- **Core Purpose**: Only needed for specific requirements (custom server)
- **Real-World Use**: Use Express for custom middleware (Express integration)
- **Common Practice**: Use Node.js for custom server logic
- **Important Note**: May impact performance optimizations (performance)
- **Interview Tip**: Explain that not recommended for new projects (legacy)

---

## 51) What are build output types (`standalone`, `app-dir`, edge bundles) in Next.js 14? (**🚀**)

Different build outputs for different deployment targets and optimization levels.

```javascript
// next.config.js
const nextConfig = {
  output: 'standalone', // Self-contained build for Docker
};
```

- **Core Types**: Standalone (self-contained build for Docker), Export (static files for static hosting), Default (optimized for Vercel deployment)
- **Real-World Use**: Edge bundles optimized for edge runtime
- **Common Practice**: Standalone output works well with containers (Docker)
- **Advanced Feature**: Different outputs for different deployment targets
- **Interview Tip**: Explain that choose output type based on deployment target

---

## 52) How does the new `app/` directory change build and routing compared to `pages/`? (**🚀**)

App directory enables Server Components, improved routing, and better performance.

```javascript
// pages/ directory (legacy)
// pages/index.js
export default function Home() {
  return <h1>Home</h1>;
}

// app/ directory (modern)
// app/page.js
export default function Home() {
  return <h1>Home</h1>;
}
```

- **Core Changes**: App directory supports RSC (Server Components), better layout composition (layouts)
- **Real-World Impact**: Different file structure (API routes)
- **Common Advantage**: Better performance with App Router (performance)
- **Advanced Feature**: Can migrate gradually from Pages Router (migration)
- **Interview Tip**: Explain that App Router is the modern approach

---

## 53) How do you configure environment-specific settings for staging vs production?

Use different `.env` files and environment variables for different deployment stages.

```javascript
// .env.local (local development)
NEXT_PUBLIC_API_URL=http://localhost:3000/api
DATABASE_URL=postgresql://localhost:5432/dev_db

// .env.staging (staging environment)
NEXT_PUBLIC_API_URL=https://staging-api.example.com

// .env.production (production)
NEXT_PUBLIC_API_URL=https://api.example.com
```

- **Core Practice**: Use different `.env` files for different stages (environment files)
- **Real-World Use**: Validate environment variables
- **Common Configuration**: Different configs per environment
- **Important Security**: Never commit secrets to version control (security)
- **Interview Tip**: Explain that set environment variables in deployment pipeline (CI/CD)

---

## 54) How do you add ESLint and TypeScript to an existing Next.js project?

Install ESLint and TypeScript packages and configure them for Next.js.

```bash
npm install --save-dev typescript @types/react @types/node
npm install --save-dev eslint eslint-config-next
```

- **Core Benefits**: TypeScript provides type safety and better development experience
- **Real-World Use**: ESLint catches code quality issues and enforces best practices
- **Common Configuration**: Proper configuration is important
- **Advanced Feature**: Can fail builds on type/ESLint errors (build integration)
- **Interview Tip**: Explain that better IDE support and error detection (development)

---

## 55) How does Next.js integrate with CI/CD pipelines (Vercel, GitHub Actions, Docker)?

Next.js works with various CI/CD platforms for automated deployment.

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

- **Core Platforms**: GitHub Actions (popular CI/CD platform), Vercel (automatic deployments from Git), Docker (containerized deployment)
- **Real-World Use**: Run tests in CI pipeline (testing)
- **Common Practice**: Fail builds on errors (quality gates)
- **Advanced Feature**: Automated testing and deployment
- **Interview Tip**: Explain that CI/CD improves development workflow

---

## 56) What are `exportPathMap` and static export (`next export`)? (**⚙️ old static export**)

Static export generates static HTML files for deployment to any static hosting.

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

- **Core Purpose**: Generates static HTML files (static export)
- **Real-World Use**: Can be hosted on any static hosting (no server)
- **Common Limitation**: No server-side features
- **Advanced Feature**: Very fast loading (performance)
- **Interview Tip**: Explain that good for SEO-friendly sites (SEO)

---

## 57) How do you debug and profile a Next.js app locally? (DevTools, React Profiler, Next Analyzer)

Use browser DevTools, React Profiler, and Next.js built-in analyzers.

```javascript
// next.config.js
const nextConfig = {
  productionBrowserSourceMaps: true,
};
```

- **Core Tools**: Use browser DevTools for debugging, React Profiler for component performance, Bundle Analyzer for bundle size
- **Real-World Use**: Enable source maps for better debugging
- **Common Practice**: Monitor Core Web Vitals (performance)
- **Advanced Feature**: Use Next.js built-in analyzers
- **Interview Tip**: Explain that debugging tools improve development experience

---

## 58) What are the advantages of Next 14's partial prerendering and streaming? (**🚀**)

Partial prerendering combines static and dynamic content for optimal performance.

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

- **Core Concept**: Combines static and dynamic content (partial prerendering)
- **Real-World Benefit**: Sends HTML chunks as they're ready (streaming)
- **Common Advantage**: Better perceived performance
- **Advanced Feature**: Improves Time to First Byte (TTFB)
- **Interview Tip**: Explain that page loads progressively

---

## 59) What is the new Turbopack bundler and how does it differ from Webpack? (**🚀 Next 14**)

Turbopack is a faster bundler written in Rust, replacing Webpack for development.

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

- **Core Technology**: Rust-based bundler, much faster than Webpack
- **Real-World Status**: Currently for development only
- **Common Compatibility**: Compatible with most Webpack loaders
- **Advanced Feature**: Significantly faster builds (performance)
- **Interview Tip**: Explain that will replace Webpack for production builds (future)

---

## 60) How do you migrate an older project from Next 12 (Pages Router) to Next 14 (App Router, RSC, Server Actions)? (**🧭 transitional 13 → 14**)

Migrate gradually by moving pages to App Router and updating data fetching patterns.

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

- **Core Strategy**: Migrate page by page (gradual migration)
- **Real-World Approach**: Modern routing with better performance (App Router)
- **Common Practice**: Move data fetching to server (Server Components)
- **Advanced Feature**: Update to new route format (API routes)
- **Interview Tip**: Explain that mark interactive components with 'use client' (client components)

---
