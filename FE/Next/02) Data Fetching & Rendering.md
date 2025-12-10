# 🌐 2. Data Fetching & Rendering (Q11–20)

---

## 📍 Navigation

<div align="center">

[← Previous: Next.js Fundamentals](01%29%20Next.js%20Fundamentals.md) • [Home: README](../README.md) • [Next: Routing & Navigation →](03%29%20Routing%20%26%20Navigation.md)

[📋 Cheatsheet](Next.js%20Interview%20Cheatsheet.md)

</div>

---

---

## Q11. 🎨 Different rendering strategies in Next.js

Next.js offers four rendering strategies: SSR (renders on server for each request - good for dynamic content and SEO, but slower than SSG), SSG (pre-renders at build time - fastest initial load, good for static content, but data can be stale), ISR (updates static content without rebuilding - best of both worlds), and CSR (renders in browser - slower initial load due to JS execution and client-side data fetching, but poor SEO). Choose strategy based on data freshness and performance needs, and use different strategies for different parts of your app (hybrid approach).

- **Trade-offs**: The catch is each strategy trades off between performance, SEO, and data freshness - SSR is slower but great for dynamic content, SSG is fastest but data can be stale, ISR balances both, but watch out - CSR has poor SEO and accessibility, so use it sparingly for interactive components only.

Example:

```javascript
// SSR - Server Side Rendering
export async function getServerSideProps() {
  const res = await fetch('https://api.example.com/data');
  const data = await res.json();
  return { props: { data } };
}

// SSG - Static Site Generation
export async function getStaticProps() {
  return { props: { data: 'static' } };
}

// ISR - Incremental Static Regeneration
export async function getStaticProps() {
  return { props: { data: 'static' }, revalidate: 60 };
}

```

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

[← Previous: Next.js Fundamentals](01%29%20Next.js%20Fundamentals.md) • [Home: README](../README.md) • [Next: Routing & Navigation →](03%29%20Routing%20%26%20Navigation.md)

[📋 Cheatsheet](Next.js%20Interview%20Cheatsheet.md)

</div>

---
