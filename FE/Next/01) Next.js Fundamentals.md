# ⚛️ 1. Next.js Fundamentals (Q1–10)

---

## 📍 Navigation

<div align="center">

[Home: README](../README.md) • [Next: Data Fetching & Rendering →](02%29%20Data%20Fetching%20%26%20Rendering.md)

[📋 Cheatsheet](Next.js%20Interview%20Cheatsheet.md)

</div>

---

---

## Q1. ⚛️ Next.js and how it differs from React

Next.js is a React framework that provides server-side rendering, static site generation, and other production-ready features out of the box - React is just a UI library for building components, while Next.js is a full framework with routing, SSR, API routes, and built-in optimizations.

- **Trade-offs**: The catch is Next.js works out of the box with sensible defaults (zero config) and includes built-in optimizations for images, fonts, and code splitting, but watch out - it's more opinionated than plain React and includes everything needed for production, which can be overkill for simple projects.

Example:

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

---

## Q2. ▲ ▲ ▲ Core features of Next.js (SSR, SSG, ISR, App Router, Edge)

Next.js provides SSR (renders pages on server for each request), SSG (pre-renders pages at build time for better performance), ISR (updates static content without rebuilding), App Router (modern routing with Server Components), Edge Rendering (runs at edge locations for low latency), API routes, and automatic code splitting - choose rendering strategy based on use case and performance needs.

- **Trade-offs**: The catch is App Router is the modern approach with Server Components and layouts, while Edge Rendering runs at edge locations for low latency, but watch out - you need to understand when to use each rendering strategy (SSR for dynamic content, SSG for static content, ISR for best of both worlds).

Example:

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

---

## Q3. ▲ ▲ ▲ Creating a new Next.js project

Use `npx create-next-app@latest` to create a new Next.js project with the latest features - interactive setup prompts for TypeScript, ESLint, Tailwind, etc. Always use `@latest` for newest features, and App Router is the default in Next 13+.

- **Trade-offs**: The catch is App Router is the recommended approach for new projects and TypeScript is recommended for better development experience, but watch out - the interactive setup can be overwhelming with many options, so choose based on your project needs.

Example:

```bash
npx create-next-app@latest my-app
npx create-next-app@latest my-app --typescript

```

---

## Q4. ➖ Difference between Pages Router and App Router

Pages Router uses `pages/` directory and is the legacy routing system (still supported), while App Router uses `app/` directory with improved routing, Server Components, and layouts - App Router is the recommended approach for new projects.

- **Trade-offs**: The catch is App Router has better performance and more features like Server Components and nested layouts, and you can migrate gradually from Pages to App Router, but watch out - different directory structure and naming conventions require learning new patterns.

Example:

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

---

## Q5. ▲ ▲ ▲ File-based routing in Next.js

App Router uses `page.js` files and nested folders, while Pages Router uses `index.js` files and direct file mapping - App Router provides more routing flexibility with nested layouts, route groups (parentheses for organization without affecting URL), and special files like `layout.js`, `loading.js`, `error.js`, and `not-found.js`.

- **Trade-offs**: The catch is App Router supports deeper nesting with folders and provides more routing flexibility, but watch out - the file-based routing can be confusing at first, especially with route groups and special file names that have specific purposes.

Example:

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

---

## Q6. ⚡ Dynamic and catch-all routes

Dynamic routes use `[id]` for single parameters, while catch-all routes use `[...slug]` for multiple path segments - access via `params` prop in page components. Catch-all routes are useful for documentation sites, and optional catch-all use `[...slug]` for optional segments.

- **Trade-offs**: The catch is use TypeScript for better parameter typing and type safety, but watch out - catch-all routes can match more than you expect, so be careful with route ordering and parameter handling.

Example:

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
// app/shop/[...slug]/page.js
export default function Shop({ params }) {
  return <h1>Shop: {params.slug?.join('/') || 'home'}</h1>;
}

```

---

## Q7. 📐 Purpose of `_app.tsx`, `_document.tsx`, and `layout.tsx`

`_app.tsx` is the global wrapper for all pages in Pages Router, `_document.tsx` customizes HTML document structure, and `layout.tsx` provides shared UI in App Router with nested layout support - layouts are more powerful in App Router and can be Server Components for better performance.

- **Trade-offs**: The catch is App Router supports multiple layout levels (nested layouts) and layouts can be Server Components for better performance, but watch out - `_app.tsx` and `_document.tsx` are Pages Router specific, while `layout.tsx` is App Router specific, so you can't mix them.

Example:

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

---

## Q8. 💡 `public/` folder and its usage

The `public/` folder contains static assets that are served directly from the root URL without processing - files in `public/` are served from root URL (direct access). Place `robots.txt`, `sitemap.xml` in public folder, and use `next/image` for automatic optimization instead of direct image files.

- **Trade-offs**: The catch is static assets are served as-is with no processing, which is fast but means you should use `next/image` for automatic optimization, but watch out - be careful with sensitive files in public folder since everything is publicly accessible (security risk).

Example:

```javascript
// public/ folder structure
// public/logo.png -> /logo.png
// public/images/hero.jpg -> /images/hero.jpg

// In components
<img src="/logo.png" alt="Logo" />
<Image src="/images/hero.jpg" alt="Hero" width={800} height={600} />

```

---

## Q9. ▲ ▲ ▲ `next/link` prefetching

`next/link` automatically prefetches linked pages in the background when these come into view - improves perceived performance by loading pages early. Prefetching happens automatically for visible links, only when connection allows (bandwidth), and when route parameters are known for dynamic routes.

- **Trade-offs**: The catch is prefetching improves perceived performance by loading pages early, but watch out - use `prefetch={false}` prop to disable prefetching when needed (e.g., for expensive pages or when bandwidth is limited).

Example:

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

---

## Q10. ▲ ▲ ▲ Handling environment variables in Next.js

Environment variables are loaded from `.env.local` files with file priority: `.env.local` > `.env.development` > `.env.production` - variables with `NEXT_PUBLIC_` prefix are available in the browser, while others are server-side only. Use `process.env` to access variables at runtime.

- **Trade-offs**: The catch is environment variables are embedded at build time, and only `NEXT_PUBLIC_` variables are available in browser, but watch out - never expose secrets with `NEXT_PUBLIC_` prefix since these are publicly accessible in the client bundle (security risk).

Example:

```javascript
// .env.local
DATABASE_URL=postgresql://localhost:5432/mydb
NEXT_PUBLIC_API_URL=https://api.example.com
SECRET_KEY=my-secret-key

// In code
const apiUrl = process.env.NEXT_PUBLIC_API_URL; // Available in browser
const dbUrl = process.env.DATABASE_URL; // Server-side only

```

---

---

## 📍 Navigation

<div align="center">

[Home: README](../README.md) • [Next: Data Fetching & Rendering →](02%29%20Data%20Fetching%20%26%20Rendering.md)

[📋 Cheatsheet](Next.js%20Interview%20Cheatsheet.md)

</div>

---
