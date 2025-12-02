<div align="center">

**[← Previous: README](../README.md)** | **[Next: Data Fetching & Rendering →](2%29%20Data%20Fetching%20%26%20Rendering.md)**

</div>

# ⚛️ 1. Next.js Fundamentals (Q1–10)

---

## Q1. 🔧 Next.js and how it differs from React

Next.js is a React framework that provides server-side rendering, static site generation, and other production-ready features out of the box - React is just a UI library, while Next.js is a full framework with routing, SSR, API routes, and optimizations. React is just a UI library for building components, Next.js is a full framework with routing, SSR, API routes, optimization.

- **Trade-offs**: The catch is works out of the box with sensible defaults (zero config) - built-in optimizations for images, fonts, and code splitting (performance). Next.js extends React with framework features for production-ready apps, but watch out - Next.js includes everything needed for production (production ready).

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

## Q2. 💡 Core features of Next.js (SSR, SSG, ISR, App Router, Edge)

Next.js provides SSR, SSG, ISR, App Router, Edge Rendering, API routes, and automatic code splitting - choose rendering strategy based on use case. SSR (renders pages on server for each request), SSG (pre-renders pages at build time for better performance).

- **Trade-offs**: The catch is App Router (modern routing with Server Components and layouts), Edge Rendering (runs at edge locations for low latency) - API routes and automatic code splitting included. Choose rendering strategy based on use case and performance needs, but watch out - ISR (updates static content without rebuilding entire site).

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

## Q3. 💡 Creating a new Next.js project

Use `npx create-next-app@latest` to create a new Next.js project with the latest features - interactive setup prompts for TypeScript, ESLint, Tailwind, etc. Always use `@latest` for newest features.

- **Trade-offs**: The catch is App Router is default in Next 13+, better than Pages Router - TypeScript recommended for better development experience. App Router is the recommended approach for new projects, but watch out - interactive setup prompts for TypeScript, ESLint, Tailwind, etc.

Example:

```bash
npx create-next-app@latest my-app
npx create-next-app@latest my-app --typescript

```

---

## Q4. 🤔 Difference between Pages Router and App Router

Pages Router uses `pages/` directory, while App Router uses `app/` directory with improved routing and Server Components - App Router is the recommended approach for new projects. Pages Router is legacy routing system, still supported; App Router is modern routing with Server Components and layouts.

- **Trade-offs**: The catch is App Router has better performance and more features - can migrate gradually from Pages to App Router. App Router is the recommended approach for new projects, but watch out - different directory structure and naming conventions.

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

## Q5. 🛣️ File-based routing in Next.js

App Router uses `page.js` files and nested folders, while Pages Router uses `index.js` files and direct file mapping - App Router provides more routing flexibility. App Router uses `page.js`, Pages Router uses `index.js`.

- **Trade-offs**: The catch is use parentheses for organization without affecting URL (route groups), App Router has `layout.js` for shared UI - `loading.js`, `error.js`, `not-found.js` for special states. App Router provides more routing flexibility with nested layouts, but watch out - App Router supports deeper nesting with folders.

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

## Q6. 💡 Dynamic and catch-all routes

Dynamic routes use `[id]` for single parameters, while catch-all routes use `[...slug]` for multiple path segments - catch-all routes are useful for documentation sites. Dynamic routes use `[param]` for single dynamic segments, catch-all use `[...slug]` for multiple segments.

- **Trade-offs**: The catch is access via `params` prop in page components - use TypeScript for better parameter typing (type safety). Catch-all routes are useful for documentation sites, but watch out - optional catch-all use `[[...slug]]` for optional segments.

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
// app/shop/[[...slug]]/page.js
export default function Shop({ params }) {
  return <h1>Shop: {params.slug?.join('/') || 'home'}</h1>;
}

```

---

## Q7. 💡 Purpose of `_app.tsx`, `_document.tsx`, and `layout.tsx`

`_app.tsx` wraps all pages, `_document.tsx` customizes HTML structure, and `layout.tsx` provides shared UI in App Router - layouts are more powerful in App Router. `_app.tsx` is global wrapper for all pages in Pages Router, `_document.tsx` customizes HTML document structure.

- **Trade-offs**: The catch is App Router supports multiple layout levels (nested layouts) - layouts can be Server Components for better performance. Layouts are more powerful in App Router with nested support, but watch out - `layout.js` provides shared UI in App Router, can be nested.

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

The `public/` folder contains static assets that are served directly from the root URL without processing - be careful with sensitive files in public folder (security). Files in `public/` are served from root URL (direct access).

- **Trade-offs**: The catch is use `next/image` for automatic optimization (performance) - place `robots.txt`, `sitemap.xml` in public folder. Be careful with sensitive files in public folder (security), but watch out - static assets are served as-is (no processing).

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

## Q9. 💡 `next/link` prefetching

`next/link` automatically prefetches linked pages in the background when they come into view - improves perceived performance by loading pages early. Prefetching happens automatically for visible links.

- **Trade-offs**: The catch is only prefetches when connection allows (bandwidth) - prefetches when route parameters are known (dynamic routes). Use `prefetch` prop to control behavior when needed, but watch out - improves perceived performance by loading pages early.

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

## Q10. 💡 Handling environment variables in Next.js

Environment variables are loaded from `.env.local` files, with `NEXT_PUBLIC_` prefix making them available in the browser - never expose secrets with `NEXT_PUBLIC_` prefix (security). File priority: `.env.local` > `.env.development` > `.env.production`.

- **Trade-offs**: The catch is never expose secrets with `NEXT_PUBLIC_` prefix (security) - environment variables are embedded at build time. Use `process.env` to access variables at runtime, but watch out - only `NEXT_PUBLIC_` variables are available in browser (client access).

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

<div align="center">

**[← Previous: README](../README.md)** | **[Next: Data Fetching & Rendering →](2%29%20Data%20Fetching%20%26%20Rendering.md)**

</div>

