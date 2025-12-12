# 🌐 2. Data Fetching & Rendering (Q11–20)

---

## 📍 Navigation

<div align="center">

[← Previous: Fundamentals & Setup](01%29%20Fundamentals%20%26%20Setup.md) • [Home: README](../README.md) • [Next: Routing & Navigation →](03%29%20Routing%20%26%20Navigation.md)

[📋 Cheatsheet](Next.js%20Interview%20Cheatsheet.md)

</div>

---

---

## Q11. 🎨 Different rendering strategies in Next.js

Next.js offers multiple rendering strategies across two routing paradigms: **Pages Router** (traditional) and **App Router** (Next.js 13+, recommended). The framework supports SSR (renders on server for each request - good for dynamic content and SEO, but slower than SSG), SSG (pre-renders at build time - fastest initial load, good for static content, but data can be stale), ISR (updates static content without rebuilding - best of both worlds), CSR (renders in browser - slower initial load due to JS execution and client-side data fetching, but poor SEO), **Streaming SSR** (sends HTML progressively), **React Server Components** (default in App Router - reduces client bundle), and **Partial Prerendering** (PPR - Next.js 15+, combines static shell with dynamic content). Choose strategy based on data freshness, performance needs, and SEO requirements, and use different strategies for different parts of your app (hybrid approach).

- **Trade-offs**: The catch is each strategy trades off between performance, SEO, and data freshness - SSR is slower but great for dynamic content, SSG is fastest but data can be stale, ISR balances both, Streaming improves perceived performance, Server Components reduce bundle size, but watch out - CSR has poor SEO and accessibility, so use it sparingly for interactive components only. App Router (Next.js 13+) is the modern approach with Server Components as default, while Pages Router uses data fetching functions.

### 📋 Rendering Strategies Overview

#### **1. Static Site Generation (SSG)**

- **When**: Content known at build time (blogs, documentation, marketing pages)
- **Performance**: Fastest (pre-rendered HTML, CDN-friendly)
- **SEO**: Excellent
- **Data Freshness**: Stale until rebuild

**Pages Router:**

```javascript
// Pre-renders at build time
export async function getStaticProps() {
  const res = await fetch('https://api.example.com/posts');
  const posts = await res.json();
  return { props: { posts } };
}

export default function Blog({ posts }) {
  return (
    <div>
      {posts.map(post => <article key={post.id}>{post.title}</article>)}
    </div>
  );
}
```

**App Router (Next.js 13+):**

```javascript
// Default behavior - static rendering
// app/blog/page.js
async function BlogPage() {
  const res = await fetch('https://api.example.com/posts', {
    cache: 'force-cache' // or omit for default static
  });
  const posts = await res.json();

  return (
    <div>
      {posts.map(post => <article key={post.id}>{post.title}</article>)}
    </div>
  );
}

export default BlogPage;
```

#### **2. Server-Side Rendering (SSR)**

- **When**: Dynamic, personalized content (user dashboards, real-time data)
- **Performance**: Slower (renders on each request)
- **SEO**: Excellent
- **Data Freshness**: Always fresh

**Pages Router:**

```javascript
// Runs on every request
export async function getServerSideProps(context) {
  const { req, res } = context;
  const user = await getUserFromCookie(req.cookies);

  const data = await fetch(`https://api.example.com/user/${user.id}/dashboard`);
  const dashboard = await data.json();

  return { props: { dashboard } };
}

export default function Dashboard({ dashboard }) {
  return <div>{/* Dashboard content */}</div>;
}
```

**App Router (Next.js 13+):**

```javascript
// app/dashboard/page.js
// Force dynamic rendering
export const dynamic = 'force-dynamic';

async function DashboardPage() {
  const user = await getCurrentUser(); // Access cookies, headers
  const dashboard = await fetch(`https://api.example.com/user/${user.id}/dashboard`, {
    cache: 'no-store' // No caching
  });
  const data = await dashboard.json();

  return <div>{/* Dashboard content */}</div>;
}

export default DashboardPage;
```

#### **3. Incremental Static Regeneration (ISR)**

- **When**: Large sites with frequently updated content (e-commerce, news sites)
- **Performance**: Fast (static with background updates)
- **SEO**: Excellent
- **Data Freshness**: Configurable freshness window

**Pages Router:**

```javascript
// Regenerates every 60 seconds if requested
export async function getStaticProps() {
  const res = await fetch('https://api.example.com/products');
  const products = await res.json();

  return {
    props: { products },
    revalidate: 60 // Regenerate every 60 seconds
  };
}

// For dynamic routes - on-demand ISR
export async function getStaticPaths() {
  return {
    paths: [], // Don't pre-render any paths
    fallback: 'blocking' // Generate on-demand, then cache
  };
}
```

**App Router (Next.js 13+):**

```javascript
// app/products/page.js
async function ProductsPage() {
  const res = await fetch('https://api.example.com/products', {
    next: { revalidate: 60 } // ISR: revalidate every 60 seconds
  });
  const products = await res.json();

  return (
    <div>
      {products.map(product => <div key={product.id}>{product.name}</div>)}
    </div>
  );
}

export default ProductsPage;
```

#### **4. Client-Side Rendering (CSR)**

- **When**: Interactive components, dashboards behind auth (no SEO needed)
- **Performance**: Slower initial load (waits for JS)
- **SEO**: Poor (content not in HTML)
- **Data Freshness**: Always fresh (fetched client-side)

**Pages Router:**

```javascript
// No data fetching functions = CSR
import { useState, useEffect } from 'react';

export default function ClientComponent() {
  const [data, setData] = useState(null);

  useEffect(() => {
    fetch('https://api.example.com/data')
      .then(res => res.json())
      .then(setData);
  }, []);

  if (!data) return <div>Loading...</div>;
  return <div>{data.message}</div>;
}
```

**App Router (Next.js 13+):**

```javascript
// app/interactive/page.js
'use client'; // Client Component directive

import { useState, useEffect } from 'react';

export default function InteractivePage() {
  const [data, setData] = useState(null);

  useEffect(() => {
    fetch('https://api.example.com/data')
      .then(res => res.json())
      .then(setData);
  }, []);

  if (!data) return <div>Loading...</div>;
  return <div>{data.message}</div>;
}
```

#### **5. Streaming SSR (Next.js 13+)**

- **When**: Pages with slow data sources, large content
- **Performance**: Fast TTFB (Time to First Byte), progressive rendering
- **SEO**: Excellent
- **Data Freshness**: Always fresh

**App Router:**

```javascript
// app/dashboard/page.js
import { Suspense } from 'react';

async function SlowData() {
  await new Promise(resolve => setTimeout(resolve, 2000));
  const data = await fetch('https://api.example.com/slow-data', {
    cache: 'no-store'
  });
  return <div>{/* Slow data content */}</div>;
}

async function FastData() {
  const data = await fetch('https://api.example.com/fast-data', {
    cache: 'no-store'
  });
  return <div>{/* Fast data content */}</div>;
}

export default function DashboardPage() {
  return (
    <div>
      <FastData />
      <Suspense fallback={<div>Loading slow data...</div>}>
        <SlowData />
      </Suspense>
    </div>
  );
}
```

#### **6. React Server Components (RSC) - App Router Default**

- **When**: Default in App Router, use for data fetching and non-interactive UI
- **Performance**: Reduces client bundle (no JS sent to client)
- **SEO**: Excellent
- **Data Freshness**: Depends on caching strategy

**App Router:**

```javascript
// app/posts/page.js
// Server Component (default - no 'use client')
async function PostsPage() {
  // Direct database access, no API needed
  const posts = await db.posts.findMany();

  return (
    <div>
      {posts.map(post => (
        <PostCard key={post.id} post={post} />
      ))}
    </div>
  );
}

// PostCard can also be Server Component
async function PostCard({ post }) {
  const author = await db.users.findById(post.authorId);
  return (
    <article>
      <h2>{post.title}</h2>
      <p>By {author.name}</p>
    </article>
  );
}

export default PostsPage;
```

#### **7. Partial Prerendering (PPR) - Next.js 15+**

- **When**: Pages with mix of static and dynamic content
- **Performance**: Fast initial load (static shell) + streaming dynamic parts
- **SEO**: Excellent
- **Data Freshness**: Dynamic parts always fresh

**App Router (Next.js 15+):**

```javascript
// next.config.js
const nextConfig = {
  experimental: {
    ppr: 'incremental', // Enable PPR
  },
};

// app/product/[id]/page.js
import { Suspense } from 'react';

export const experimental_ppr = true; // Enable PPR for this route

// Static shell - pre-rendered at build time
function ProductShell() {
  return (
    <div>
      <nav>Navigation</nav>
      <header>Product Header</header>
    </div>
  );
}

// Dynamic content - rendered on request
async function ProductDetails({ id }) {
  const product = await fetch(`https://api.example.com/products/${id}`, {
    cache: 'no-store'
  });
  const data = await product.json();
  return <div>{data.name} - ${data.price}</div>;
}

export default function ProductPage({ params }) {
  return (
    <>
      <ProductShell />
      <Suspense fallback={<div>Loading product...</div>}>
        <ProductDetails id={params.id} />
      </Suspense>
    </>
  );
}
```

#### **8. Edge Runtime**

- **When**: Low-latency requirements, simple logic (A/B testing, redirects, auth)
- **Performance**: Fastest (runs at edge locations)
- **Limitations**: Limited Node.js APIs, smaller runtime

**App Router:**

```javascript
// app/api/hello/route.js
export const runtime = 'edge';

export async function GET(request) {
  return Response.json({
    message: 'Hello from Edge!',
    region: request.geo?.region
  });
}
```

### 🎯 Strategy Selection Guide

| Strategy | Use Case | Performance | SEO | Data Freshness |
|----------|----------|-------------|-----|----------------|
| **SSG** | Blogs, docs, marketing | ⭐⭐⭐⭐⭐ | ✅ | Build time |
| **SSR** | User dashboards, real-time | ⭐⭐⭐ | ✅ | Always fresh |
| **ISR** | E-commerce, news sites | ⭐⭐⭐⭐ | ✅ | Configurable |
| **CSR** | Interactive apps (no SEO) | ⭐⭐ | ❌ | Always fresh |
| **Streaming** | Slow data sources | ⭐⭐⭐⭐ | ✅ | Always fresh |
| **RSC** | Default (App Router) | ⭐⭐⭐⭐⭐ | ✅ | Configurable |
| **PPR** | Mixed static/dynamic | ⭐⭐⭐⭐⭐ | ✅ | Dynamic parts fresh |

### 🔄 Hybrid Approach

Use different strategies for different parts of your app:

```javascript
// app/layout.js - Static
export default function RootLayout({ children }) {
  return (
    <html>
      <body>
        <StaticHeader /> {/* Static */}
        {children}
        <StaticFooter /> {/* Static */}
      </body>
    </html>
  );
}

// app/dashboard/page.js - Dynamic SSR
export const dynamic = 'force-dynamic';
export default async function Dashboard() {
  const user = await getCurrentUser();
  return <UserDashboard user={user} />;
}

// app/blog/page.js - Static with ISR
export default async function Blog() {
  const posts = await fetch('https://api.example.com/posts', {
    next: { revalidate: 3600 } // ISR: 1 hour
  });
  return <BlogList posts={await posts.json()} />;
}

// app/interactive/page.js - Client Component
'use client';
export default function Interactive() {
  return <InteractiveChart />; // Needs browser APIs
}
```

### 📌 Key Differences: Pages Router vs App Router

- **Pages Router**: Uses `getStaticProps`, `getServerSideProps`, `getStaticPaths`
- **App Router**: Uses Server Components (default), `fetch` with caching options, `'use client'` directive
- **App Router Benefits**: Smaller bundles, better performance, simpler data fetching, built-in streaming
- **Migration**: App Router is recommended for new projects (Next.js 13+)

### ⚠️ Important Notes

- **Next.js 13+**: App Router is recommended, Server Components are default
- **Next.js 15+**: Partial Prerendering (PPR) available for hybrid rendering
- **Next.js 16+**: Cache Components with `"use cache"` directive for explicit caching
- **Edge Runtime**: Use for low-latency, simple operations (limited Node.js APIs)
- **Streaming**: Requires React 18+ Suspense boundaries
- **CSR**: Use sparingly - only for interactive components that need browser APIs

---

## Q12. 📤 Difference between `getStaticProps` and `getServerSideProps`

`getStaticProps` runs at build time (SSG, good for static content), while `getServerSideProps` runs on every request (SSR, good for dynamic content) - these are Pages Router specific, App Router uses different patterns. `getServerSideProps` receives request context, and `getStaticPaths` defines which dynamic routes to pre-render with `getStaticProps`.

- **Trade-offs**: The catch is `getStaticProps` is faster but data can be stale, while `getServerSideProps` is slower but always fresh, but watch out - these are Pages Router specific, so if you're using App Router, you'll use Server Components and async components instead.

Example:

```javascript
// getStaticProps - runs at build time
export async function getStaticProps() {
  const posts = await fetch('https://api.example.com/posts');
  const data = await posts.json();
  return { props: { data } };
}

```

---

## Q13. 💡 `getStaticPaths` and when to use it

`getStaticPaths` defines which dynamic routes to pre-render at build time - use it with `getStaticProps` for static generation of dynamic pages. Required for dynamic routes with SSG, and fallback controls behavior for non-pre-rendered paths.

- **Trade-offs**: The catch is you need to define all paths upfront or use fallback to handle unknown paths, but watch out - if you have many dynamic routes, pre-rendering all of them can slow down your build time significantly.

Example:

```javascript
export async function getStaticPaths() {
  return {
    paths: [
      { params: { id: '1' } },
      { params: { id: '2' } }
    ],
    fallback: false
  };
}

```

---

## Q14. 💡 Implementing data fetching in App Router

Server components can use async functions and `fetch` directly (run on server, fetch data during rendering), while client components use `useEffect` and state (run in browser, use hooks) - server components reduce JavaScript bundle size since they don't need to be sent to the client.

- **Trade-offs**: The catch is server components reduce JavaScript bundle size and fetch data during rendering, but watch out - client components need to be hydrated and run in browser, so use server components for data fetching when possible and only use client components when you need interactivity.

Example:

```javascript
// Server Component - can use async and fetch directly
async function ServerComponent() {
  const res = await fetch('https://api.example.com/data');
  const data = await res.json();
  return <div>{data.message}</div>;
}

```

---

## Q15. ⚛️ React Server Components (RSC)

RSC run on the server, can't use browser APIs (no window, document, etc.), and don't re-render, while client components run in the browser and can handle user interactions - server components reduce client bundle size since no JavaScript is sent to client.

- **Trade-offs**: The catch is server components reduce client bundle size and improve performance, but watch out - server components can't use browser APIs or handle user interactions, so you need client components (marked with 'use client') for anything interactive or that needs browser APIs.

Example:

```javascript
// Server Component - runs on server
async function ServerComponent() {
  const data = await fetch('https://api.example.com/data');
  const posts = await data.json();
  return <div>{posts.map(p => <p key={p.id}>{p.title}</p>)}</div>;
}

```

---

## Q16. 💾 Caching and revalidation with `fetch()`

The `revalidate` option caches data for the specified seconds before revalidating - reduces database and API calls and improves performance. Set revalidate time in seconds before cache expires, or use `false` to cache forever until manual revalidation.

- **Trade-offs**: The catch is Next.js handles caching automatically, and tags allow targeted cache invalidation, but watch out - `false` caches forever until manual revalidation, which can lead to stale data if you forget to invalidate.

Example:

```javascript
// Cache for 60 seconds
async function getData() {
  const res = await fetch('https://api.example.com/data', {
    next: { revalidate: 60 }
  });
  return res.json();
}

```

---

## Q17. ✅ Revalidation tags and how to use them

Revalidation tags allow targeted cache invalidation by grouping related data, while `revalidatePath` invalidates specific routes - only revalidates what's necessary for better performance. Use tags to group related data, then call `revalidateTag` to invalidate all data with that tag.

- **Trade-offs**: The catch is `revalidatePath` invalidates specific routes and is more precise than global revalidation, but watch out - `revalidateTag` invalidates all data with a specific tag, so organize your tags carefully to avoid invalidating too much.

Example:

```javascript
// Fetch with tags
async function getPosts() {
  const res = await fetch('https://api.example.com/posts', {
    next: {
      revalidate: 3600,
      tags: ['posts', 'content']
    }
  });
  return res.json();
}

```

---

## Q18. ✅ Implementing on-demand revalidation

On-demand revalidation allows you to manually invalidate cached data using `revalidateTag` or `revalidatePath` - use it when data changes outside of the normal revalidation cycle, like after data mutations. `revalidateTag` invalidates all data with a specific tag, while `revalidatePath` invalidates specific routes.

- **Trade-offs**: The catch is use after data mutations to keep cache fresh, and it's more precise than global revalidation, but watch out - you need to remember to call revalidation after mutations, or your cache will become stale.

Example:

```javascript
import { revalidateTag } from 'next/cache';

export async function POST() {
  // Update data
  revalidateTag('posts');
  return Response.json({ revalidated: true });
}

```

---

## Q19. 🔄 Fallback mechanism in ISR

Fallback controls how Next.js handles pages not generated at build time - `false` (only pre-rendered paths work, 404 for others), `true` (show loading for non-pre-rendered paths), or `blocking` (wait for generation, then render). Choose based on build time vs runtime needs.

- **Trade-offs**: The catch is `false` is fastest but provides worst UX, `blocking` is slowest but ensures content is ready, but watch out - `true` provides better user experience by showing loading states, but requires handling loading UI.

Example:

```javascript
// fallback: false - only pre-rendered paths work
export async function getStaticPaths() {
  return {
    paths: [
      { params: { id: '1' } },
      { params: { id: '2' } }
    ],
    fallback: false
  };
}

```

---

## Q20. 🖥️ Difference between API routes and Server Actions

API routes are traditional REST endpoints (good for external APIs), while Server Actions are functions that run on the server (good for forms and mutations) - server actions provide better TypeScript support and integrate better with Next.js caching. Server actions are more efficient for simple operations.

- **Trade-offs**: The catch is server actions provide better TypeScript support and integrate better with Next.js caching, but watch out - API routes are better for external APIs and when you need standard REST endpoints, while server actions are better for form submissions and mutations.

Example:

```javascript
// API Route - REST endpoint
// pages/api/posts.js or app/api/posts/route.js
export async function GET() {
  const posts = await fetch('https://api.example.com/posts');
  const data = await posts.json();
  return Response.json(data);
}

// Server Action
'use server';
export async function createUser(formData) {
  const name = formData.get('name');
  // Save to database
  return { success: true };
}

```

---

---

## 📍 Navigation

<div align="center">

[← Previous: Fundamentals & Setup](01%29%20Fundamentals%20%26%20Setup.md) • [Home: README](../README.md) • [Next: Routing & Navigation →](03%29%20Routing%20%26%20Navigation.md)

[📋 Cheatsheet](Next.js%20Interview%20Cheatsheet.md)

</div>

---
