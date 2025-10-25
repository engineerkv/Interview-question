# ⚛️ Next.js Cheatsheet - Interview Quick Reference

## 🚀 Quick Reference Guide

### 🟢 Next.js Fundamentals
- **App Router**: New routing system with `app/` directory
- **Server Components**: Components that run on the server by default
- **Client Components**: Use `"use client"` directive for browser-only code
- **File-based Routing**: Automatic routing based on file structure

### 🟡 Rendering Strategies
- **SSR**: Server-Side Rendering with `getServerSideProps`
- **SSG**: Static Site Generation with `getStaticProps`
- **ISR**: Incremental Static Regeneration
- **CSR**: Client-Side Rendering (default behavior)

### 🔴 Performance Optimization
- **Image Optimization**: `next/image` component with automatic optimization
- **Font Optimization**: `next/font` for automatic font loading
- **Code Splitting**: Automatic route-based code splitting
- **Bundle Analysis**: `next build --analyze` for bundle analysis

### 🟠 Data Fetching
- **Server Actions**: Server-side functions for mutations
- **fetch() API**: Enhanced fetch with caching
- **revalidate**: Cache revalidation strategies
- **Streaming**: Partial rendering with Suspense

### 🟣 Routing & Navigation
- **Link Component**: `<Link href="/path">` for navigation
- **useRouter**: `const router = useRouter()` for programmatic navigation
- **Dynamic Routes**: `[id].js` for dynamic segments
- **Parallel Routes**: `@folder` for parallel layouts

### 🔵 Middleware & Edge
- **Middleware**: `middleware.js` for request/response handling
- **Edge Runtime**: Faster cold starts
- **Authentication**: Auth middleware patterns
- **Rate Limiting**: Request throttling

### 🟤 API Routes
- **Route Handlers**: `route.js` files for API endpoints
- **HTTP Methods**: GET, POST, PUT, DELETE handlers
- **Request/Response**: Standard Web API interfaces
- **Error Handling**: Try-catch patterns

### 🟢 Deployment
- **Vercel**: Optimized deployment platform
- **Docker**: Containerization support
- **Environment Variables**: `.env.local` for secrets
- **Build Optimization**: Production builds

### 🟡 Security
- **CSRF Protection**: Built-in CSRF tokens
- **CORS**: Cross-origin resource sharing
- **Authentication**: NextAuth.js integration
- **Environment Secrets**: Secure configuration

### 🔴 Real-World Patterns
- **CMS Integration**: Headless CMS setup
- **E-commerce**: Product pages and cart
- **Blog**: MDX content management
- **Multi-tenant**: SaaS application patterns

## 📝 Common Interview Questions

### Core Concepts
1. **What is Next.js?** - React framework with SSR, SSG, and optimization
2. **App Router vs Pages Router?** - New routing system with better performance
3. **Server vs Client Components?** - Server runs on server, client runs in browser
4. **What is hydration?** - Process of making server-rendered content interactive

### Performance
5. **How does Next.js optimize performance?** - Automatic code splitting, image optimization, font optimization
6. **What are Core Web Vitals?** - LCP, FID, CLS metrics for user experience
7. **How to optimize bundle size?** - Dynamic imports, tree shaking, bundle analysis
8. **What is ISR?** - Incremental Static Regeneration for dynamic content

### Data Fetching
9. **Server Actions vs API Routes?** - Server Actions for mutations, API Routes for endpoints
10. **How does caching work?** - Built-in fetch caching with revalidate options
11. **What is streaming?** - Partial rendering for better perceived performance
12. **How to handle errors?** - Error boundaries and error.js files

### Deployment
13. **How to deploy Next.js?** - Vercel, Docker, or any Node.js hosting
14. **Environment variables?** - `.env.local` for development, platform settings for production
15. **Build optimization?** - Production builds with optimizations
16. **Monitoring?** - Vercel Analytics, custom monitoring solutions

## 🎯 Quick Commands

```bash
# Development
npm run dev          # Start development server
npm run build        # Build for production
npm run start        # Start production server
npm run lint         # Run ESLint

# Analysis
npm run build --analyze  # Bundle analysis
npx next info        # System information
```

## 🔧 Configuration

### next.config.js
```javascript
/** @type {import('next').NextConfig} */
const nextConfig = {
  experimental: {
    appDir: true,
  },
  images: {
    domains: ['example.com'],
  },
  env: {
    CUSTOM_KEY: process.env.CUSTOM_KEY,
  },
}

module.exports = nextConfig
```

### tsconfig.json
```json
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
```

## 📚 Best Practices

### Performance
- Use `next/image` for images
- Use `next/font` for fonts
- Implement code splitting
- Optimize bundle size

### SEO
- Use semantic HTML
- Implement meta tags
- Use structured data
- Optimize for Core Web Vitals

### Security
- Validate inputs
- Use HTTPS
- Implement CSRF protection
- Secure environment variables

### Development
- Use TypeScript
- Implement error boundaries
- Use proper file structure
- Follow naming conventions
