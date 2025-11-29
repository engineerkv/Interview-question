<div align="center">

**[← Previous: Next.js Fundamentals](1%29%20Next.js%20Fundamentals.md)** | **[Next: Routing & Navigation →](3%29%20Routing%20%26%20Navigation.md)**

</div>

# 2. Data Fetching & Rendering (Q11–20)

---

## Q11. Different rendering strategies in Next.js

SSR renders on server, SSG pre-renders at build time, ISR updates static content, and CSR renders in browser - choose strategy based on data freshness and performance needs. SSR (good for dynamic content, SEO, but slower than SSG), SSG (fastest, good for static content, but data can be stale).

- **Trade-offs**: The catch is CSR (fastest initial load, but poor SEO and accessibility) - use different strategies for different parts of app (hybrid). Choose strategy based on data freshness and performance needs, but watch out - ISR (best of both worlds - fast with fresh data).

Example:

```javascript
// SSR - Server Side Rendering
export async function getServerSideProps() {
  const res = await fetch('https://api.example.com/data');
  const data = await res.json();
  return { props: { data } };
}
```

---

## Q12. Difference between `getStaticProps` and `getServerSideProps`

These functions fetch data at build time (SSG) or request time (SSR) in the Pages Router - these are Pages Router specific, App Router uses different patterns. getStaticProps (runs at build time, good for static content), getServerSideProps (runs on every request, good for dynamic content).

- **Trade-offs**: The catch is fallback controls behavior for non-pre-rendered paths - getServerSideProps receives request context. These are Pages Router specific, App Router uses different patterns, but watch out - getStaticPaths (defines which dynamic routes to pre-render).

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

## Q13. `getStaticPaths` and when to use it

`getStaticPaths` defines which dynamic routes to pre-render at build time - use it with `getStaticProps` for static generation of dynamic pages. Defines which dynamic routes to pre-render at build time.

- **Trade-offs**: The catch is fallback controls behavior for non-pre-rendered paths - required for dynamic routes with SSG. Required for dynamic routes with SSG, but watch out - use with `getStaticProps` for static generation of dynamic pages.

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

## Q14. Implementing data fetching in App Router

Server components can use async functions and `fetch` directly, while client components use `useEffect` and state - server components reduce JavaScript bundle size (performance). Server components run on server, can use async/await.

- **Trade-offs**: The catch is server components reduce JavaScript bundle size (performance) - server components fetch data during rendering. Client components need to be hydrated, but watch out - client components run in browser, use hooks and state.

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

## Q15. React Server Components (RSC)

RSC run on the server, can't use browser APIs, and don't re-render, while client components run in the browser - only client components can handle user interactions (interactivity). Server components run on server, no JavaScript sent to client.

- **Trade-offs**: The catch is server components reduce client bundle size - server components can't use window, document, etc. (browser APIs). Only client components can handle user interactions (interactivity), but watch out - client components run in browser, can use hooks and state.

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

## Q16. Caching and revalidation with `fetch()`

The `revalidate` option caches data for the specified seconds before revalidating - reduces database and API calls (performance). Revalidate time in seconds before cache expires.

- **Trade-offs**: The catch is false caches forever until manual revalidation - Next.js handles caching automatically. Reduces database and API calls (performance), but watch out - tags allow targeted cache invalidation.

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

## Q17. Revalidation tags and how to use them

Revalidation tags allow targeted cache invalidation, while `revalidatePath` invalidates specific routes - only revalidates what's necessary (performance). Tags group related data for targeted invalidation.

- **Trade-offs**: The catch is `revalidatePath` invalidates specific routes - more precise than global revalidation (granular). Only revalidates what's necessary (performance), but watch out - `revalidateTag` invalidates all data with specific tag.

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

## Q18. Implementing on-demand revalidation

On-demand revalidation allows you to manually invalidate cached data using `revalidateTag` or `revalidatePath` - use it when data changes outside of the normal revalidation cycle. `revalidateTag` invalidates all data with specific tag.

- **Trade-offs**: The catch is use after data mutations to keep cache fresh - more precise than global revalidation (granular). Use after data mutations to keep cache fresh, but watch out - `revalidatePath` invalidates specific routes.

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

## Q19. Fallback mechanism in ISR

Fallback controls how Next.js handles pages not generated at build time - choose based on build time vs runtime needs. False (only pre-rendered paths work, 404 for others), True (show loading for non-pre-rendered paths), Blocking (wait for generation, then render).

- **Trade-offs**: The catch is false is fastest, blocking is slowest (performance) - fallback affects how dynamic routes are handled. Choose based on build time vs runtime needs, but watch out - true provides better user experience (UX).

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

## Q20. Difference between API routes and Server Actions

API routes are REST endpoints, while Server Actions are functions that run on the server - server actions provide better TypeScript support (type safety). API routes are traditional REST endpoints, good for external APIs.

- **Trade-offs**: The catch is server actions are more efficient for simple operations (performance) - server actions integrate better with Next.js caching. Server actions provide better TypeScript support (type safety), but watch out - server actions are functions that run on server, good for forms.

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

