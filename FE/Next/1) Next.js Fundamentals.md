# 🧩 1. Next.js Fundamentals (Q1–10)

---

## 🧩 Q1. What is Next.js and how does it differ from React?

### 🧠 Concept

Next.js is a React framework that provides server-side rendering, static site generation, and other production-ready features out of the box. React is just a UI library, while Next.js is a full framework with routing, SSR, API routes, and optimizations.

---

### 💡 Example

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

### 🔍 Deep Insights

* **Rule:** React is just a UI library for building components, Next.js is a full framework with routing, SSR, API routes, optimization.
* **Use Case:** Next.js includes everything needed for production (production ready).
* **Common Mistake:** Works out of the box with sensible defaults (zero config).
* **Pro Tip:** Built-in optimizations for images, fonts, and code splitting (performance).

---

### ⭐ Senior Takeaway

Next.js extends React with framework features for production-ready apps.

---

## 🧩 Q2. What are the core features of Next.js (SSR, SSG, ISR, App Router, Edge)?

### 🧠 Concept

Next.js provides SSR, SSG, ISR, App Router, Edge Rendering, API routes, and automatic code splitting. Choose rendering strategy based on use case.

---

### 💡 Example

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

### 🔍 Deep Insights

* **Rule:** SSR (renders pages on server for each request), SSG (pre-renders pages at build time for better performance).
* **Use Case:** ISR (updates static content without rebuilding entire site).
* **Common Mistake:** App Router (modern routing with Server Components and layouts), Edge Rendering (runs at edge locations for low latency).
* **Pro Tip:** API routes and automatic code splitting included.

---

### ⭐ Senior Takeaway

Choose rendering strategy based on use case and performance needs.

---

## 🧩 Q3. How do you create a new Next.js project?

### 🧠 Concept

Use `npx create-next-app@latest` to create a new Next.js project with the latest features. Interactive setup prompts for TypeScript, ESLint, Tailwind, etc.

---

### 💡 Example

```bash
npx create-next-app@latest my-app
npx create-next-app@latest my-app --typescript
```

---

### 🔍 Deep Insights

* **Rule:** Always use `@latest` for newest features.
* **Use Case:** Interactive setup prompts for TypeScript, ESLint, Tailwind, etc.
* **Common Mistake:** App Router is default in Next 13+, better than Pages Router.
* **Pro Tip:** TypeScript recommended for better development experience.

---

### ⭐ Senior Takeaway

App Router is the recommended approach for new projects.

---

## 🧩 Q4. What is the difference between Pages Router and App Router?

### 🧠 Concept

Pages Router uses `pages/` directory, while App Router uses `app/` directory with improved routing and Server Components. App Router is the recommended approach for new projects.

---

### 💡 Example

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

### 🔍 Deep Insights

* **Rule:** Pages Router is legacy routing system, still supported; App Router is modern routing with Server Components and layouts.
* **Use Case:** Different directory structure and naming conventions.
* **Common Mistake:** App Router has better performance and more features.
* **Pro Tip:** Can migrate gradually from Pages to App Router.

---

### ⭐ Senior Takeaway

App Router is the recommended approach for new projects.

---

## 🧩 Q5. How does file-based routing work in Next.js?

### 🧠 Concept

App Router uses `page.js` files and nested folders, while Pages Router uses `index.js` files and direct file mapping. App Router provides more routing flexibility.

---

### 💡 Example

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

### 🔍 Deep Insights

* **Rule:** App Router uses `page.js`, Pages Router uses `index.js`.
* **Use Case:** App Router supports deeper nesting with folders.
* **Common Mistake:** Use parentheses for organization without affecting URL (route groups), App Router has `layout.js` for shared UI.
* **Pro Tip:** `loading.js`, `error.js`, `not-found.js` for special states.

---

### ⭐ Senior Takeaway

App Router provides more routing flexibility with nested layouts.

---

## 🧩 Q6. What are dynamic and catch-all routes?

### 🧠 Concept

Dynamic routes use `[id]` for single parameters, while catch-all routes use `[...slug]` for multiple path segments. Catch-all routes are useful for documentation sites.

---

### 💡 Example

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

### 🔍 Deep Insights

* **Rule:** Dynamic routes use `[param]` for single dynamic segments, catch-all use `[...slug]` for multiple segments.
* **Use Case:** Optional catch-all use `[[...slug]]` for optional segments.
* **Common Mistake:** Access via `params` prop in page components.
* **Pro Tip:** Use TypeScript for better parameter typing (type safety).

---

### ⭐ Senior Takeaway

Catch-all routes are useful for documentation sites.

---

## 🧩 Q7. What is the purpose of `_app.tsx`, `_document.tsx`, and `layout.tsx`?

### 🧠 Concept

`_app.tsx` wraps all pages, `_document.tsx` customizes HTML structure, and `layout.tsx` provides shared UI in App Router. Layouts are more powerful in App Router.

---

### 💡 Example

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

### 🔍 Deep Insights

* **Rule:** `_app.tsx` is global wrapper for all pages in Pages Router, `_document.tsx` customizes HTML document structure.
* **Use Case:** `layout.js` provides shared UI in App Router, can be nested.
* **Common Mistake:** App Router supports multiple layout levels (nested layouts).
* **Pro Tip:** Layouts can be Server Components for better performance.

---

### ⭐ Senior Takeaway

Layouts are more powerful in App Router with nested support.

---

## 🧩 Q8. What is the `public/` folder used for?

### 🧠 Concept

The `public/` folder contains static assets that are served directly from the root URL without processing. Be careful with sensitive files in public folder (security).

---

### 💡 Example

```javascript
// public/ folder structure
// public/logo.png -> /logo.png
// public/images/hero.jpg -> /images/hero.jpg

// In components
<img src="/logo.png" alt="Logo" />
<Image src="/images/hero.jpg" alt="Hero" width={800} height={600} />
```

---

### 🔍 Deep Insights

* **Rule:** Files in `public/` are served from root URL (direct access).
* **Use Case:** Static assets are served as-is (no processing).
* **Common Mistake:** Use `next/image` for automatic optimization (performance).
* **Pro Tip:** Place `robots.txt`, `sitemap.xml` in public folder.

---

### ⭐ Senior Takeaway

Be careful with sensitive files in public folder (security).

---

## 🧩 Q9. How does `next/link` prefetching work?

### 🧠 Concept

`next/link` automatically prefetches linked pages in the background when they come into view. Improves perceived performance by loading pages early.

---

### 💡 Example

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

### 🔍 Deep Insights

* **Rule:** Prefetching happens automatically for visible links.
* **Use Case:** Improves perceived performance by loading pages early.
* **Common Mistake:** Only prefetches when connection allows (bandwidth).
* **Pro Tip:** Prefetches when route parameters are known (dynamic routes).

---

### ⭐ Senior Takeaway

Use `prefetch` prop to control behavior when needed.

---

## 🧩 Q10. How do you handle environment variables in Next.js?

### 🧠 Concept

Environment variables are loaded from `.env.local` files, with `NEXT_PUBLIC_` prefix making them available in the browser. Never expose secrets with `NEXT_PUBLIC_` prefix (security).

---

### 💡 Example

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

### 🔍 Deep Insights

* **Rule:** File priority: `.env.local` > `.env.development` > `.env.production`.
* **Use Case:** Only `NEXT_PUBLIC_` variables are available in browser (client access).
* **Common Mistake:** Never expose secrets with `NEXT_PUBLIC_` prefix (security).
* **Pro Tip:** Environment variables are embedded at build time.

---

### ⭐ Senior Takeaway

Use `process.env` to access variables at runtime.

---
