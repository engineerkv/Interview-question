# 📡 2. Data Fetching & Rendering (Q11–20)

---

## 11) What are the rendering strategies in Next.js — SSR, SSG, ISR, and CSR?

SSR renders on server, SSG pre-renders at build time, ISR updates static content, and CSR renders in browser.

```javascript
// SSR - Server Side Rendering
export async function getServerSideProps() {
  const res = await fetch('https://api.example.com/data');
  const data = await res.json();
  return { props: { data } };
}
```

- **Core Strategies**: SSR (good for dynamic content, SEO, but slower than SSG), SSG (fastest, good for static content, but data can be stale)
- **Real-World Use**: ISR (best of both worlds - fast with fresh data)
- **Common Pattern**: CSR (fastest initial load, but poor SEO and accessibility)
- **Advanced Approach**: Use different strategies for different parts of app (hybrid)
- **Interview Tip**: Explain that choose strategy based on data freshness and performance needs

---

## 12) How do `getStaticProps`, `getServerSideProps`, and `getStaticPaths` work? (**⚙️ Pages Router only**)

These functions fetch data at build time (SSG) or request time (SSR) in the Pages Router.

```javascript
// getStaticProps - runs at build time
export async function getStaticProps() {
  const posts = await fetch('https://api.example.com/posts');
  const data = await posts.json();
  return { props: { data } };
}
```

- **Core Functions**: getStaticProps (runs at build time, good for static content), getServerSideProps (runs on every request, good for dynamic content)
- **Real-World Use**: getStaticPaths (defines which dynamic routes to pre-render)
- **Common Configuration**: Fallback controls behavior for non-pre-rendered paths
- **Advanced Feature**: getServerSideProps receives request context
- **Interview Tip**: Explain that these are Pages Router specific, App Router uses different patterns

---

## 13) How do you fetch data in **App Router 🚀** using server components (async components, `fetch`) vs client components?

Server components can use async functions and `fetch` directly, while client components use `useEffect` and state.

```javascript
// Server Component - can use async and fetch directly
async function ServerComponent() {
  const res = await fetch('https://api.example.com/data');
  const data = await res.json();
  return <div>{data.message}</div>;
}
```

- **Core Difference**: Server components run on server, can use async/await
- **Real-World Use**: Client components run in browser, use hooks and state
- **Common Advantage**: Server components reduce JavaScript bundle size (performance)
- **Advanced Feature**: Server components fetch data during rendering
- **Interview Tip**: Explain that client components need to be hydrated

---

## 14) What are **React Server Components (RSC)** in Next.js and how do they differ from client components? (**🚀 introduced in 13**)

RSC run on the server, can't use browser APIs, and don't re-render, while client components run in the browser.

```javascript
// Server Component - runs on server
async function ServerComponent() {
  const data = await fetch('https://api.example.com/data');
  const posts = await data.json();
  return <div>{posts.map(p => <p key={p.id}>{p.title}</p>)}</div>;
}
```

- **Core Concept**: Server components run on server, no JavaScript sent to client
- **Real-World Use**: Client components run in browser, can use hooks and state
- **Common Advantage**: Server components reduce client bundle size
- **Important Limitation**: Server components can't use window, document, etc. (browser APIs)
- **Interview Tip**: Explain that only client components can handle user interactions (interactivity)

---

## 15) How does caching and revalidation work using `fetch()` options like `{ next: { revalidate: 10 } }`? (**🚀 Next 14**)

The `revalidate` option caches data for the specified seconds before revalidating.

```javascript
// Cache for 60 seconds
async function getData() {
  const res = await fetch('https://api.example.com/data', {
    next: { revalidate: 60 }
  });
  return res.json();
}
```

- **Core Option**: Revalidate time in seconds before cache expires
- **Real-World Use**: Tags allow targeted cache invalidation
- **Common Settings**: False caches forever until manual revalidation
- **Advanced Feature**: Next.js handles caching automatically
- **Interview Tip**: Explain that reduces database and API calls (performance)

---

## 16) What are revalidation tags and on-demand revalidation (`revalidateTag`, `revalidatePath`)? (**🚀 Next 14**)

Revalidation tags allow targeted cache invalidation, while `revalidatePath` invalidates specific routes.

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

- **Core Concept**: Tags group related data for targeted invalidation
- **Real-World Use**: `revalidateTag` invalidates all data with specific tag
- **Common Practice**: `revalidatePath` invalidates specific routes
- **Advanced Feature**: More precise than global revalidation (granular)
- **Interview Tip**: Explain that only revalidates what's necessary (performance)

---

## 17) What is the fallback mechanism in `getStaticPaths` (`false`, `true`, `blocking`)? (**⚙️ old SSG**)

Fallback controls how Next.js handles pages not generated at build time.

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

- **Core Options**: False (only pre-rendered paths work, 404 for others), True (show loading for non-pre-rendered paths), Blocking (wait for generation, then render)
- **Real-World Trade-offs**: False is fastest, blocking is slowest (performance)
- **Common Choice**: True provides better user experience (UX)
- **Advanced Feature**: Fallback affects how dynamic routes are handled
- **Interview Tip**: Explain that choose based on build time vs runtime needs

---

## 18) What are API routes and how do they differ from server actions?

API routes are REST endpoints, while Server Actions are functions that run on the server.

```javascript
// API Route - REST endpoint
// pages/api/posts.js or app/api/posts/route.js
export async function GET() {
  const posts = await fetch('https://api.example.com/posts');
  const data = await posts.json();
  return Response.json(data);
}
```

- **Core Difference**: API routes are traditional REST endpoints, good for external APIs
- **Real-World Use**: Server actions are functions that run on server, good for forms
- **Common Advantage**: Server actions are more efficient for simple operations (performance)
- **Advanced Feature**: Server actions integrate better with Next.js caching
- **Interview Tip**: Explain that server actions provide better TypeScript support (type safety)

---

## 19) What are Server Actions (`"use server"`) in App Router and how do they replace API routes for mutations? (**🚀 Next 14**)

Server Actions are server-side functions marked with `"use server"` that can be called from client components.

```javascript
// Server Action
'use server';

export async function createUser(formData) {
  const name = formData.get('name');
  const email = formData.get('email');
  // Save to database
  return { success: true };
}
```

- **Core Feature**: "use server" marks function as Server Action
- **Real-World Use**: Can be used directly in forms (form integration)
- **Common Advantage**: Better TypeScript support than API routes (type safety)
- **Advanced Feature**: Integrates with Next.js caching system
- **Interview Tip**: Explain that more efficient than API routes for simple operations (performance)

---

## 20) What are edge functions and the Edge Runtime, and when should you use them? (**🚀**)

Edge functions run at the edge for low latency, ideal for simple transformations and redirects.

```javascript
// Edge Runtime API route
export const runtime = 'edge';

export async function GET(request) {
  const { searchParams } = new URL(request.url);
  const name = searchParams.get('name') || 'World';
  return Response.json({ message: `Hello ${name}` });
}
```

- **Core Concept**: Edge runtime runs at edge locations for low latency
- **Real-World Limitations**: Can't use Node.js APIs, limited to Web APIs
- **Common Use Cases**: Redirects, A/B testing, simple transformations
- **Advanced Feature**: Faster than Node.js runtime for simple operations (performance)
- **Interview Tip**: Explain that runs closer to users worldwide (global)

---
