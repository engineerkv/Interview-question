# 🚀 6. Deployment & Tooling (Q49–60)

---

## 49) How do you deploy a Next.js 14 app to Vercel and what automatic optimizations does it apply?

Concept:
Vercel automatically optimizes images, enables edge functions, and provides analytics.

Example:
```javascript
// vercel.json configuration
{
  "framework": "nextjs",
  "buildCommand": "npm run build",
  "outputDirectory": ".next",
  "functions": {
```

Deep Insight:
- **Automatic Deployments**: Deploys on git push
- **Image Optimization**: Automatic image optimization
- **Edge Functions**: Runs at edge locations
- **CDN**: Global content delivery
- **Analytics**: Built-in performance monitoring

---

## 50) How do you set up a custom server for Next.js (Node.js or Express integration)? (**⚙️ legacy**)

Concept:
Create a custom server using `next()` function with Express or Node.js.

Example:
```javascript
// server.js - Custom Express server
const express = require('express');
const next = require('next');

const dev = process.env.NODE_ENV !== 'production';
const app = next({ dev });
```

Deep Insight:
- **Custom Server**: Only needed for specific requirements
- **Express Integration**: Use Express for custom middleware
- **Node.js**: Use Node.js for custom server logic
- **Performance**: May impact performance optimizations
- **Legacy**: Not recommended for new projects

---

## 51) What are build output types (`standalone`, `app-dir`, edge bundles) in Next.js 14? (**🚀**)

Concept:
Different build outputs for different deployment targets and optimization levels.

Example:
```javascript
// next.config.js
/** @type {import('next').NextConfig} */
const nextConfig = {
  // Standalone output for Docker
  output: 'standalone',
  
```

Deep Insight:
- **Standalone**: Self-contained build for Docker
- **Export**: Static files for static hosting
- **Default**: Optimized for Vercel deployment
- **Edge Bundles**: Optimized for edge runtime
- **Docker**: Standalone output works well with containers

---

## 52) How does the new `app/` directory change build and routing compared to `pages/`? (**🚀**)

Concept:
App directory enables Server Components, improved routing, and better performance.

Example:
```javascript
// pages/ directory (legacy)
// pages/index.js
export default function Home() {
  return <h1>Home</h1>;
}

```

Deep Insight:
- **Server Components**: App directory supports RSC
- **Layouts**: Better layout composition
- **API Routes**: Different file structure
- **Performance**: Better performance with App Router
- **Migration**: Can migrate gradually from Pages Router

---

## 53) How do you configure environment-specific settings for staging vs production?

Concept:
Use different `.env` files and environment variables for different deployment stages.

Example:
```javascript
// .env.local (local development)
NEXT_PUBLIC_API_URL=http://localhost:3000/api
DATABASE_URL=postgresql://localhost:5432/dev_db
SECRET_KEY=dev-secret-key

// .env.staging (staging environment)
```

Deep Insight:
- **Environment Files**: Use different `.env` files for different stages
- **Validation**: Validate environment variables
- **Configuration**: Different configs per environment
- **Security**: Never commit secrets to version control
- **CI/CD**: Set environment variables in deployment pipeline

---

## 54) How do you add ESLint and TypeScript to an existing Next.js project?

Concept:
Install ESLint and TypeScript packages and configure them for Next.js.

Example:
```bash
# Install TypeScript
npm install --save-dev typescript @types/react @types/node

# Install ESLint
npm install --save-dev eslint eslint-config-next

```

```javascript
// tsconfig.json
{
  "compilerOptions": {
    "target": "es5",
    "lib": ["dom", "dom.iterable", "es6"],
    "allowJs": true,
    "skipLibCheck": true,
    "strict": true,
    "forceConsistentCasingInFileNames": true,
    "noEmit": true,
    "esModuleInterop": true,
    "module": "esnext",
    "moduleResolution": "node",
    "resolveJsonModule": true,
    "isolatedModules": true,
    "jsx": "preserve",
    "incremental": true,
    "plugins": [
      {
        "name": "next"
      }
    ],
    "paths": {
      "@/*": ["./*"]
    }
  },
  "include": ["next-env.d.ts", "**/*.ts", "**/*.tsx", ".next/types/**/*.ts"],
  "exclude": ["node_modules"]
}

// .eslintrc.json
{
  "extends": [
    "next/core-web-vitals",
    "@typescript-eslint/recommended"
  ],
  "parser": "@typescript-eslint/parser",
  "plugins": ["@typescript-eslint"],
  "rules": {
    "@typescript-eslint/no-unused-vars": "error",
    "@typescript-eslint/no-explicit-any": "warn"
  }
}

// next.config.js
/** @type {import('next').NextConfig} */
const nextConfig = {
  typescript: {
    // Dangerously allow production builds to successfully complete even if
    // your project has type errors.
    ignoreBuildErrors: false,
  },
  eslint: {
    // Warning: This allows production builds to successfully complete even if
    // your project has ESLint errors.
    ignoreDuringBuilds: false,
  },
};

module.exports = nextConfig;
```

Deep Insight:
- **TypeScript**: Provides type safety and better development experience
- **ESLint**: Catches code quality issues and enforces best practices
- **Configuration**: Proper configuration is important
- **Build Integration**: Can fail builds on type/ESLint errors
- **Development**: Better IDE support and error detection

---

## 55) How does Next.js integrate with CI/CD pipelines (Vercel, GitHub Actions, Docker)?

Concept:
Next.js works with various CI/CD platforms for automated deployment.

Example:
```yaml
# .github/workflows/deploy.yml
name: Deploy to Vercel

on:
  push:
    branches: [main]
```

```dockerfile
# Dockerfile
FROM node:18-alpine AS base
WORKDIR /app
COPY package*.json ./
RUN npm ci --only=production

FROM base AS deps
RUN npm ci

FROM base AS builder
COPY . .
COPY --from=deps /app/node_modules ./node_modules
RUN npm run build

FROM base AS runner
ENV NODE_ENV production
COPY --from=builder /app/.next/standalone ./
COPY --from=builder /app/.next/static ./.next/static
COPY --from=builder /app/public ./public

EXPOSE 3000
CMD ["node", "server.js"]
```

Deep Insight:
- **GitHub Actions**: Popular CI/CD platform
- **Vercel**: Automatic deployments from Git
- **Docker**: Containerized deployment
- **Testing**: Run tests in CI pipeline
- **Quality Gates**: Fail builds on errors

---

## 56) What are `exportPathMap` and static export (`next export`)? (**⚙️ old static export**)

Concept:
Static export generates static HTML files for deployment to any static hosting.

Example:
```javascript
// next.config.js
/** @type {import('next').NextConfig} */
const nextConfig = {
  output: 'export',
  trailingSlash: true,
  images: {
```

Deep Insight:
- **Static Export**: Generates static HTML files
- **No Server**: Can be hosted on any static hosting
- **Limitations**: No server-side features
- **Performance**: Very fast loading
- **SEO**: Good for SEO-friendly sites

---

## 57) How do you debug and profile a Next.js app locally? (DevTools, React Profiler, Next Analyzer)

Concept:
Use browser DevTools, React Profiler, and Next.js built-in analyzers.

Example:
```javascript
// next.config.js - Enable debugging
/** @type {import('next').NextConfig} */
const nextConfig = {
  // Enable source maps in development
  productionBrowserSourceMaps: true,
  
```

Deep Insight:
- **DevTools**: Use browser DevTools for debugging
- **React Profiler**: Profile component performance
- **Bundle Analyzer**: Analyze bundle size
- **Source Maps**: Enable for better debugging
- **Performance**: Monitor Core Web Vitals

---

## 58) What are the advantages of Next 14's partial prerendering and streaming? (**🚀**)

Concept:
Partial prerendering combines static and dynamic content for optimal performance.

Example:
```javascript
// Partial prerendering with streaming
export default function Page() {
  return (
    <div>
      {/* Static content - prerendered */}
      <header>
```

Deep Insight:
- **Partial Prerendering**: Combines static and dynamic content
- **Streaming**: Sends HTML chunks as they're ready
- **Performance**: Better perceived performance
- **TTFB**: Improves Time to First Byte
- **Progressive**: Page loads progressively

---

## 59) What is the new Turbopack bundler and how does it differ from Webpack? (**🚀 Next 14**)

Concept:
Turbopack is a faster bundler written in Rust, replacing Webpack for development.

Example:
```javascript
// next.config.js - Enable Turbopack
/** @type {import('next').NextConfig} */
const nextConfig = {
  experimental: {
    // Enable Turbopack for development
    turbo: {
```

Deep Insight:
- **Rust-based**: Much faster than Webpack
- **Development**: Currently for development only
- **Compatibility**: Compatible with most Webpack loaders
- **Performance**: Significantly faster builds
- **Future**: Will replace Webpack for production builds

---

## 60) How do you migrate an older project from Next 12 (Pages Router) to Next 14 (App Router, RSC, Server Actions)? (**🧭 transitional 13 → 14**)

Concept:
Migrate gradually by moving pages to App Router and updating data fetching patterns.

Example:
```javascript
// Step 1: Update Next.js version
// package.json
{
  "dependencies": {
    "next": "14.0.0",
    "react": "18.0.0",
```

Deep Insight:
- **Gradual Migration**: Migrate page by page
- **App Router**: Modern routing with better performance
- **Server Components**: Move data fetching to server
- **API Routes**: Update to new route format
- **Client Components**: Mark interactive components with 'use client'

---
