---
sidebar_label: "Fundamentals & Setup"
---
# ⚛️ 1. Fundamentals & Setup (Q1–10)

> **Reviewed:** 2026-09 · Modernized for Next.js 15/16 App Router. Legacy (Pages Router) topics are labeled.

---

## Q1. ⚛️ Next.js and how it differs from React

Next.js is a full-stack React framework - React is the UI library (components, hooks, and since React 19 the primitives for Server Components and Actions), while Next.js adds the pieces React deliberately leaves out: file-system routing, a server that renders React Server Components, streaming SSR, static prerendering, caching, Server Actions, Route Handlers, and built-in image/font/script optimization. In the App Router, components are **Server Components by default**, so the mental model is "render on the server, ship JavaScript only for the interactive islands you mark with `'use client'`."

- **Trade-offs**: The catch is Next.js gives you production defaults (routing, bundling, code splitting, optimization) without wiring them yourself, but watch out - it's opinionated, needs a Node.js (or compatible) server for anything dynamic, and its caching model changes between major versions. For a purely client-side SPA (internal dashboard, no SEO) plain React + Vite is often simpler.

Example:

```javascript
// Plain React (e.g. Vite SPA) - everything runs in the browser
function App() {
  const [user, setUser] = useState(null);
  useEffect(() => { fetch('/api/me').then(r => r.json()).then(setUser); }, []);
  return <h1>Hello {user?.name}</h1>;
}

// Next.js App Router - Server Component by default, data fetched on the server
// app/page.tsx
export default async function Home() {
  const user = await getCurrentUser(); // direct DB/API access, no client JS for this
  return <h1>Hello {user.name}</h1>;
}

```

---

## Q2. ▲ ▲ ▲ Core features of Next.js (SSR, SSG, ISR, App Router, Edge)

Next.js provides SSR (render per request), SSG (prerender at build time), ISR (regenerate static output in the background), the App Router (React Server Components, nested layouts, streaming), Server Actions (server mutations callable from forms/components), Route Handlers, an optional Edge runtime, and automatic code splitting. In the App Router you don't pick SSR/SSG with special functions - Next.js decides **per route** whether it can be prerendered (static) or must render per request (dynamic, e.g. it reads `cookies()`/`headers()` or uncached data), and you tune it with `fetch` options, `revalidate`, and (Next 16) `"use cache"`.

- **Trade-offs**: The catch is the App Router unifies these strategies under one component model, but watch out - "static vs dynamic" is now inferred from what your code touches, so one `cookies()` call can make a whole route dynamic. Understanding the caching defaults for your Next.js version (Q34, Q63) matters more than memorizing SSR/SSG function names.

Example:

```javascript
// App Router (modern) - app/products/page.tsx
export const revalidate = 3600; // ISR-style: regenerate at most hourly

export default async function Products() {
  const res = await fetch('https://api.example.com/products', {
    next: { revalidate: 3600, tags: ['products'] },
  });
  const products = await res.json();
  return <ProductList products={products} />;
}

// Dynamic per request - reading cookies opts the route into dynamic rendering
import { cookies } from 'next/headers';
export async function Greeting() {
  const theme = (await cookies()).get('theme')?.value; // async in Next 15+
  return <p data-theme={theme}>Welcome back</p>;
}

```

> **Legacy note (2026):** Pages Router uses `getServerSideProps` (SSR) and `getStaticProps`/`getStaticPaths` (SSG/ISR). It's still supported and common in production apps; for new work prefer App Router — see Q12 and Q68.

---

## Q3. ▲ ▲ ▲ Creating a new Next.js project

Use `npx create-next-app@latest` - the interactive prompts default to TypeScript, the App Router, Tailwind, and a `src/` option, and recent versions scaffold with Turbopack (the default bundler for `next dev` and `next build` in Next.js 16). App Router has been the default since Next 13.4.

- **Trade-offs**: The catch is the defaults are good for new projects (TypeScript + App Router), but watch out - check the Node.js minimum for your Next.js major (it rises over time), and if you depend on custom webpack loaders, confirm Turbopack support or opt back into webpack explicitly.

Example:

```bash
npx create-next-app@latest my-app            # interactive, TS + App Router by default
npx create-next-app@latest my-app --yes      # accept recommended defaults
npm run dev                                  # next dev (Turbopack)

```

---

## Q4. ➖ Difference between Pages Router and App Router

Pages Router uses the `pages/` directory, where every component is a Client Component that is SSR'd and hydrated, and data comes from `getServerSideProps`/`getStaticProps`. App Router uses `app/` with React Server Components by default, nested layouts that persist across navigation, streaming via `loading.tsx`/Suspense, Server Actions, the Metadata API (instead of `next/head`), and `next/navigation` hooks (instead of `next/router`). Both are officially supported and can coexist in one app; App Router is the recommended choice for new work.

- **Trade-offs**: The catch is App Router ships less client JavaScript and colocates data fetching with components, and you can migrate route by route (Q68), but watch out - the mental model (server vs client boundary, caching layers) is genuinely different, and some libraries that assume a browser-only React need `'use client'` wrappers.

| Concern | Pages Router (legacy) | App Router (modern) |
|---------|-----------------------|---------------------|
| Data fetching | `getServerSideProps` / `getStaticProps` | `async` Server Components + `fetch` / `"use cache"` |
| Layouts | `_app.tsx` + manual per-page layout | Nested `layout.tsx` |
| Head/SEO | `next/head` | `export const metadata` / `generateMetadata` |
| Navigation hooks | `next/router` | `next/navigation` |
| Mutations | API routes | Server Actions (+ Route Handlers) |

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
    <html lang="en">
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
// app/(marketing)/pricing/page.js -> /pricing (route group, no URL segment)
// app/_components/Nav.js -> private folder, never routable
// app/api/health/route.js -> Route Handler at /api/health

```

> **Legacy note (2026):** In Pages Router every file in `pages/` is a route (`pages/about.js` → `/about`). It's still supported; in App Router only `page.js` and `route.js` make a segment publicly routable, so you can safely colocate components, tests, and styles inside `app/`.

---

## Q6. ⚡ Dynamic and catch-all routes

Dynamic routes use `[id]` for single parameters, catch-all routes use `[...slug]` for multiple segments, and optional catch-all uses `[[...slug]]` (also matches the base path). In Next.js 15+ the `params` (and `searchParams`) prop is a **Promise**, so you `await` it in Server Components or unwrap it with React's `use()` in Client Components. Use `generateStaticParams` to prerender known params at build time (the App Router replacement for `getStaticPaths`).

- **Trade-offs**: The catch is async `params` lets Next.js start rendering before the params are needed, but watch out - Next 15 still allowed synchronous access with a warning as a migration aid, and Next 16 removed it, so old `params.id` code breaks on upgrade. Catch-all routes can also match more than you expect, so validate segments.

Example:

```javascript
// Dynamic route - app/posts/[id]/page.tsx
export async function generateStaticParams() {
  const posts = await getPosts();
  return posts.map(p => ({ id: String(p.id) })); // prerender these at build
}

export default async function Post({ params }: { params: Promise<{ id: string }> }) {
  const { id } = await params; // Next 15+: params is a Promise
  return <h1>Post {id}</h1>;
}

// Catch-all - app/docs/[...slug]/page.tsx
export default async function Docs({ params }) {
  const { slug } = await params; // string[]
  return <h1>Docs: {slug.join('/')}</h1>;
}

// Optional catch-all - app/shop/[[...slug]]/page.tsx
export default async function Shop({ params }) {
  const { slug } = await params;
  return <h1>Shop: {slug?.join('/') ?? 'home'}</h1>;
}

// Client Component - unwrap with use()
'use client';
import { use } from 'react';
export function PostClient({ params }) {
  const { id } = use(params);
  return <p>{id}</p>;
}

```

---

## Q7. 📐 Purpose of `_app.tsx`, `_document.tsx`, and `layout.tsx`

In the App Router, the root `app/layout.tsx` replaces **both** Pages Router files: it must render `<html>` and `<body>` (the job of `_document.tsx`) and wraps every page with shared UI and providers (the job of `_app.tsx`). Nested `layout.tsx` files add per-segment shells that persist across navigation, and they're Server Components by default. Head tags move to the Metadata API (`export const metadata` or `generateMetadata`) instead of `next/head`.

- **Trade-offs**: The catch is nested layouts remove the "custom per-page layout" hacks from `_app`, but watch out - layouts don't re-render on navigation and don't receive `searchParams`, so anything that must react to the current URL belongs in the page or a Client Component. Context providers need a small `'use client'` wrapper component.

Example:

```javascript
// App Router - app/layout.tsx
import type { Metadata } from 'next';
import { Providers } from './providers'; // 'use client' wrapper for context providers

export const metadata: Metadata = {
  title: { default: 'Acme', template: '%s | Acme' },
  description: 'Acme storefront',
};

export default function RootLayout({ children }: { children: React.ReactNode }) {
  return (
    <html lang="en">
      <body>
        <Providers>
          <Header />
          {children}
        </Providers>
      </body>
    </html>
  );
}

// Legacy Pages Router - pages/_app.tsx (still supported)
import Head from 'next/head';
function MyApp({ Component, pageProps }) {
  return (
    <>
      <Head><title>Acme</title></Head>
      <Header />
      <Component {...pageProps} />
    </>
  );
}

```

> **Legacy note (2026):** `_app.tsx`, `_document.tsx`, and `next/head` are Pages Router APIs. They're still supported and you'll see them in many production apps; they have no effect inside `app/` — see Q68 for migration.

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

`next/link` prefetches routes in the background when links enter the viewport, and only in production builds. In the App Router, static routes are prefetched fully, while dynamic routes are prefetched only down to the nearest `loading.tsx` boundary (so the loading shell appears instantly and the rest streams in). Navigation is client-side and keeps shared layouts mounted.

- **Trade-offs**: The catch is prefetching makes navigation feel instant, but watch out - on pages with hundreds of links it can generate a lot of requests; use `prefetch={false}` for rarely-visited or expensive routes, and remember you won't see prefetching in `next dev`. `prefetch={true}` forces a full prefetch of dynamic routes.

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

Next.js loads `.env*` files in this order, stopping at the first match per variable: real `process.env` → `.env.$(NODE_ENV).local` → `.env.local` (skipped when `NODE_ENV=test`) → `.env.$(NODE_ENV)` → `.env`. Only one of `.env.development`/`.env.production` is loaded, based on `NODE_ENV`. Variables prefixed `NEXT_PUBLIC_` are **inlined into the client bundle at build time**; everything else is server-only and, for dynamically rendered code, read at runtime.

- **Trade-offs**: The catch is `NEXT_PUBLIC_` values are frozen at build time, so one Docker image can't serve different public config per environment without a runtime approach (e.g. reading server-only vars in a Server Component and passing them down), but watch out - never put secrets behind `NEXT_PUBLIC_`, and use the `server-only` package in modules that read secrets so they can't be imported into Client Components by accident.

Example:

```javascript
// .env.local
DATABASE_URL=postgresql://localhost:5432/mydb
NEXT_PUBLIC_API_URL=https://api.example.com
SECRET_KEY=my-secret-key

// In code
const apiUrl = process.env.NEXT_PUBLIC_API_URL; // Inlined into browser bundle at build
const dbUrl = process.env.DATABASE_URL; // Server-side only (undefined in the browser)

// lib/db.ts
import 'server-only'; // build error if a Client Component imports this module

```

---

