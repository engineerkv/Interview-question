# 🧩 1. Next.js Fundamentals (Q1–10)

---

## 1) What is Next.js and how does it differ from React?

Next.js is a React framework that provides server-side rendering, static site generation, and other production-ready features out of the box.

```javascript
// React - just a library
function App() {
  return <h1>Hello World</h1>;
}

// Next.js - full framework
export default function Home() {
  return <h1>Hello World</h1>;
}
```

- **Core Difference**: React is just a UI library for building components, Next.js is a full framework with routing, SSR, API routes, optimization
- **Real-World Advantage**: Next.js includes everything needed for production (production ready)
- **Common Benefit**: Works out of the box with sensible defaults (zero config)
- **Advanced Feature**: Built-in optimizations for images, fonts, and code splitting (performance)
- **Interview Tip**: Explain that Next.js extends React with framework features

---

## 2) What are the core features of Next.js (SSR, SSG, ISR, App Router, Edge Rendering)?

Next.js provides SSR, SSG, ISR, App Router, Edge Rendering, API routes, and automatic code splitting.

```javascript
// SSR - Server Side Rendering
export async function getServerSideProps() {
  const data = await fetch('https://api.example.com/data');
  return { props: { data } };
}

// SSG - Static Site Generation
export async function getStaticProps() {
  return { props: { data: 'static' } };
}
```

- **Core Features**: SSR (renders pages on server for each request), SSG (pre-renders pages at build time for better performance)
- **Real-World Use**: ISR (updates static content without rebuilding entire site)
- **Advanced Features**: App Router (modern routing with Server Components and layouts), Edge Rendering (runs at edge locations for low latency)
- **Common Advantage**: API routes and automatic code splitting included
- **Interview Tip**: Explain that choose rendering strategy based on use case

---

## 3) How do you create a new Next.js project using `create-next-app`?

Use `npx create-next-app@latest` to create a new Next.js project with the latest features.

```bash
npx create-next-app@latest my-app
npx create-next-app@latest my-app --typescript
```

- **Core Command**: Always use `@latest` for newest features
- **Real-World Use**: Interactive setup prompts for TypeScript, ESLint, Tailwind, etc.
- **Common Recommendation**: App Router is default in Next 13+, better than Pages Router
- **Advanced Feature**: TypeScript recommended for better development experience
- **Interview Tip**: Explain that Tailwind is a popular CSS framework that works well with Next.js

---

## 4) What is the difference between the **Pages Router ⚙️ (legacy)** and the **App Router 🚀 (Next 13/14)**?

Pages Router uses `pages/` directory, while App Router uses `app/` directory with improved routing and Server Components.

```javascript
// Pages Router (legacy)
// pages/index.js
export default function Home() {
  return <h1>Home Page</h1>;
}

// App Router (modern)
// app/page.js
export default function Home() {
  return <h1>Home Page</h1>;
}

// app/layout.js
export default function RootLayout({ children }) {
  return (
    <html>
      <body>{children}</body>
    </html>
  );
}
```

- **Core Difference**: Pages Router is legacy routing system, still supported; App Router is modern routing with Server Components and layouts
- **Real-World Impact**: Different directory structure and naming conventions
- **Common Advantage**: App Router has better performance and more features
- **Advanced Feature**: Can migrate gradually from Pages to App Router
- **Interview Tip**: Explain that App Router is the recommended approach for new projects

---

## 5) How does file-based routing work in the App Router compared to the Pages Router?

App Router uses `page.js` files and nested folders, while Pages Router uses `index.js` files and direct file mapping.

```javascript
// Pages Router
// pages/index.js -> /
// pages/about.js -> /about
// pages/blog/[slug].js -> /blog/[slug]

// App Router
// app/page.js -> /
// app/about/page.js -> /about
// app/blog/[slug]/page.js -> /blog/[slug]
// app/layout.js -> Root layout for all pages
```

- **Core Difference**: App Router uses `page.js`, Pages Router uses `index.js`
- **Real-World Advantage**: App Router supports deeper nesting with folders
- **Advanced Features**: Use parentheses for organization without affecting URL (route groups), App Router has `layout.js` for shared UI
- **Special Files**: `loading.js`, `error.js`, `not-found.js` for special states
- **Interview Tip**: Explain that App Router provides more routing flexibility

---

## 6) What are dynamic routes (`[id]`) and catch-all routes (`[...slug]`)?

Dynamic routes use `[id]` for single parameters, while catch-all routes use `[...slug]` for multiple path segments.

```javascript
// Dynamic route - single parameter
// app/posts/[id]/page.js
export default function Post({ params }) {
  return <h1>Post {params.id}</h1>;
}

// Catch-all route - multiple segments
// app/docs/[...slug]/page.js
export default function Docs({ params }) {
  return <h1>Docs: {params.slug.join('/')}</h1>;
}

// Optional catch-all - optional segments
// app/shop/[[...slug]]/page.js
export default function Shop({ params }) {
  return <h1>Shop: {params.slug?.join('/') || 'home'}</h1>;
}
```

- **Core Patterns**: Dynamic routes use `[param]` for single dynamic segments, catch-all use `[...slug]` for multiple segments
- **Real-World Use**: Optional catch-all use `[[...slug]]` for optional segments
- **Common Access**: Access via `params` prop in page components
- **Advanced Feature**: Use TypeScript for better parameter typing (type safety)
- **Interview Tip**: Explain that catch-all routes are useful for documentation sites

---

## 7) What is the purpose of `_app.tsx`, `_document.tsx` (**⚙️ old Pages Router**) and `layout.tsx` (**🚀 App Router**)?

`_app.tsx` wraps all pages, `_document.tsx` customizes HTML structure, and `layout.tsx` provides shared UI in App Router.

```javascript
// Pages Router
// pages/_app.tsx - wraps all pages
function MyApp({ Component, pageProps }) {
  return (
    <div>
      <Header />
      <Component {...pageProps} />
    </div>
  );
}

// App Router
// app/layout.js - root layout
export default function RootLayout({ children }) {
  return (
    <html>
      <body>
        <Header />
        {children}
      </body>
    </html>
  );
}
```

- **Core Files**: `_app.tsx` is global wrapper for all pages in Pages Router, `_document.tsx` customizes HTML document structure
- **Real-World Use**: `layout.js` provides shared UI in App Router, can be nested
- **Advanced Feature**: App Router supports multiple layout levels (nested layouts)
- **Performance**: Layouts can be Server Components for better performance
- **Interview Tip**: Explain that layouts are more powerful in App Router

---

## 8) What is the role of the `public/` folder and how are static assets served?

The `public/` folder contains static assets that are served directly from the root URL without processing.

```javascript
// public/ folder structure
// public/logo.png -> /logo.png
// public/images/hero.jpg -> /images/hero.jpg

// In components
<img src="/logo.png" alt="Logo" />
<Image src="/images/hero.jpg" alt="Hero" width={800} height={600} />
```

- **Core Purpose**: Files in `public/` are served from root URL (direct access)
- **Real-World Use**: Static assets are served as-is (no processing)
- **Common Practice**: Use `next/image` for automatic optimization (performance)
- **SEO Use**: Place `robots.txt`, `sitemap.xml` in public folder
- **Interview Tip**: Explain that be careful with sensitive files in public folder (security)

---

## 9) How does prefetching work automatically with the `next/link` component?

`next/link` automatically prefetches linked pages in the background when they come into view.

```javascript
import Link from 'next/link';

export default function Navigation() {
  return (
    <nav>
      <Link href="/">Home</Link>
      <Link href="/about">About</Link>
      <Link href="/blog" prefetch={false}>Blog</Link>
    </nav>
  );
}
```

- **Core Feature**: Prefetching happens automatically for visible links
- **Real-World Benefit**: Improves perceived performance by loading pages early
- **Common Optimization**: Only prefetches when connection allows (bandwidth)
- **Advanced Feature**: Prefetches when route parameters are known (dynamic routes)
- **Interview Tip**: Explain that use `prefetch` prop to control behavior

---

## 10) How do environment variables work in Next.js (`.env.local`, `NEXT_PUBLIC_` prefix)?

Environment variables are loaded from `.env.local` files, with `NEXT_PUBLIC_` prefix making them available in the browser.

```javascript
// .env.local
DATABASE_URL=postgresql://localhost:5432/mydb
NEXT_PUBLIC_API_URL=https://api.example.com
SECRET_KEY=my-secret-key

// In code
const apiUrl = process.env.NEXT_PUBLIC_API_URL; // Available in browser
const dbUrl = process.env.DATABASE_URL; // Server-side only
```

- **Core Rule**: File priority: `.env.local` > `.env.development` > `.env.production`
- **Real-World Use**: Only `NEXT_PUBLIC_` variables are available in browser (client access)
- **Common Mistake**: Never expose secrets with `NEXT_PUBLIC_` prefix (security)
- **Advanced Feature**: Environment variables are embedded at build time
- **Interview Tip**: Explain that use `process.env` to access variables at runtime

---
