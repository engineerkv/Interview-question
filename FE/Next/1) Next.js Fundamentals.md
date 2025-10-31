# 🧩 1. Next.js Fundamentals (Q1–10)

---

## 1) What is Next.js and how does it differ from React?

Concept:
Next.js is a React framework that provides server-side rendering, static site generation, and other production-ready features out of the box.

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

Deep Insight:
- **React**: Just a UI library for building components
- **Next.js**: Full framework with routing, SSR, API routes, optimization
- **Production Ready**: Next.js includes everything needed for production
- **Zero Config**: Works out of the box with sensible defaults
- **Performance**: Built-in optimizations for images, fonts, and code splitting

---

## 2) What are the core features of Next.js (SSR, SSG, ISR, App Router, Edge Rendering)?

Concept:
Next.js provides SSR, SSG, ISR, App Router, Edge Rendering, API routes, and automatic code splitting.

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

Deep Insight:
- **SSR**: Renders pages on server for each request
- **SSG**: Pre-renders pages at build time for better performance
- **ISR**: Updates static content without rebuilding entire site
- **App Router**: Modern routing with Server Components and layouts
- **Edge Rendering**: Runs at edge locations for low latency

---

## 3) How do you create a new Next.js project using `create-next-app`?

Concept:
Use `npx create-next-app@latest` to create a new Next.js project with the latest features.

Example:
```bash
# Create new Next.js project
npx create-next-app@latest my-app

# With TypeScript
npx create-next-app@latest my-app --typescript

```

Deep Insight:
- **Latest Version**: Always use `@latest` for newest features
- **Interactive Setup**: Prompts for TypeScript, ESLint, Tailwind, etc.
- **App Router**: Default in Next 13+, better than Pages Router
- **TypeScript**: Recommended for better development experience
- **Tailwind**: Popular CSS framework that works well with Next.js

---

## 4) What is the difference between the **Pages Router ⚙️ (legacy)** and the **App Router 🚀 (Next 13/14)**?

Concept:
Pages Router uses `pages/` directory, while App Router uses `app/` directory with improved routing and Server Components.

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

Deep Insight:
- **Pages Router**: Legacy routing system, still supported
- **App Router**: Modern routing with Server Components and layouts
- **File Structure**: Different directory structure and naming conventions
- **Features**: App Router has better performance and more features
- **Migration**: Can migrate gradually from Pages to App Router

---

## 5) How does file-based routing work in the App Router compared to the Pages Router?

Concept:
App Router uses `page.js` files and nested folders, while Pages Router uses `index.js` files and direct file mapping.

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

Deep Insight:
- **Page Files**: App Router uses `page.js`, Pages Router uses `index.js`
- **Nested Routes**: App Router supports deeper nesting with folders
- **Route Groups**: Use parentheses for organization without affecting URL
- **Layouts**: App Router has `layout.js` for shared UI
- **Special Files**: `loading.js`, `error.js`, `not-found.js` for special states

---

## 6) What are dynamic routes (`[id]`) and catch-all routes (`[...slug]`)?

Concept:
Dynamic routes use `[id]` for single parameters, while catch-all routes use `[...slug]` for multiple path segments.

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

Deep Insight:
- **Dynamic Routes**: Use `[param]` for single dynamic segments
- **Catch-all**: Use `[...slug]` for multiple segments
- **Optional Catch-all**: Use `[[...slug]]` for optional segments
- **Params**: Access via `params` prop in page components
- **Type Safety**: Use TypeScript for better parameter typing

---

## 7) What is the purpose of `_app.tsx`, `_document.tsx` (**⚙️ old Pages Router**) and `layout.tsx` (**🚀 App Router**)?

Concept:
`_app.tsx` wraps all pages, `_document.tsx` customizes HTML structure, and `layout.tsx` provides shared UI in App Router.

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

Deep Insight:
- **`_app.tsx`**: Global wrapper for all pages in Pages Router
- **`_document.tsx`**: Customizes HTML document structure
- **`layout.js`**: Shared UI in App Router, can be nested
- **Nested Layouts**: App Router supports multiple layout levels
- **Server Components**: Layouts can be Server Components for better performance

---

## 8) What is the role of the `public/` folder and how are static assets served?

Concept:
The `public/` folder contains static assets that are served directly from the root URL without processing.

Example:
```javascript
// public/ folder structure
// public/
//   ├── favicon.ico
//   ├── images/
//   │   ├── logo.png
//   │   └── hero.jpg
//   └── robots.txt

// Access static assets
// public/logo.png -> /logo.png
// public/images/hero.jpg -> /images/hero.jpg

// In components
<img src="/logo.png" alt="Logo" />
<Image src="/images/hero.jpg" alt="Hero" width={800} height={600} />
```

Deep Insight:
- **Direct Access**: Files in `public/` are served from root URL
- **No Processing**: Static assets are served as-is
- **Performance**: Use `next/image` for automatic optimization
- **SEO**: Place `robots.txt`, `sitemap.xml` in public folder
- **Security**: Be careful with sensitive files in public folder

---

## 9) How does prefetching work automatically with the `next/link` component?

Concept:
`next/link` automatically prefetches linked pages in the background when they come into view.

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

Deep Insight:
- **Automatic**: Prefetching happens automatically for visible links
- **Performance**: Improves perceived performance by loading pages early
- **Bandwidth**: Only prefetches when connection allows
- **Dynamic Routes**: Prefetches when route parameters are known
- **Control**: Use `prefetch` prop to control behavior

---

## 10) How do environment variables work in Next.js (`.env.local`, `NEXT_PUBLIC_` prefix)?

Concept:
Environment variables are loaded from `.env.local` files, with `NEXT_PUBLIC_` prefix making them available in the browser.

Example:
```javascript
// .env.local
DATABASE_URL=postgresql://localhost:5432/mydb
NEXT_PUBLIC_API_URL=https://api.example.com
SECRET_KEY=my-secret-key

// .env.development
NEXT_PUBLIC_API_URL=https://dev-api.example.com

// In code
const apiUrl = process.env.NEXT_PUBLIC_API_URL; // Available in browser
const dbUrl = process.env.DATABASE_URL; // Server-side only
```

Deep Insight:
- **File Priority**: `.env.local` > `.env.development` > `.env.production`
- **Client Access**: Only `NEXT_PUBLIC_` variables are available in browser
- **Security**: Never expose secrets with `NEXT_PUBLIC_` prefix
- **Build Time**: Environment variables are embedded at build time
- **Runtime**: Use `process.env` to access variables

---
