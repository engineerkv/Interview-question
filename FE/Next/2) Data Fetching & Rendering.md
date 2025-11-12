# 📡 2. Data Fetching & Rendering (Q11–20)

---

## 🧩 Q11. What are the different rendering strategies in Next.js?

### 🧠 Concept

SSR renders on server, SSG pre-renders at build time, ISR updates static content, and CSR renders in browser. Choose strategy based on data freshness and performance needs.

---

### 💡 Example

```javascript
// SSR - Server Side Rendering
export async function getServerSideProps() {
  const res = await fetch('https://api.example.com/data');
  const data = await res.json();
  return { props: { data } };
}
```

---

### 🔍 Deep Insights

* **Rule:** SSR (good for dynamic content, SEO, but slower than SSG), SSG (fastest, good for static content, but data can be stale).
* **Use Case:** ISR (best of both worlds - fast with fresh data).
* **Common Mistake:** CSR (fastest initial load, but poor SEO and accessibility).
* **Pro Tip:** Use different strategies for different parts of app (hybrid).

---

### ⭐ Senior Takeaway

Choose strategy based on data freshness and performance needs.

---

## 🧩 Q12. What is the difference between `getStaticProps` and `getServerSideProps`?

### 🧠 Concept

These functions fetch data at build time (SSG) or request time (SSR) in the Pages Router. These are Pages Router specific, App Router uses different patterns.

---

### 💡 Example

```javascript
// getStaticProps - runs at build time
export async function getStaticProps() {
  const posts = await fetch('https://api.example.com/posts');
  const data = await posts.json();
  return { props: { data } };
}
```

---

### 🔍 Deep Insights

* **Rule:** getStaticProps (runs at build time, good for static content), getServerSideProps (runs on every request, good for dynamic content).
* **Use Case:** getStaticPaths (defines which dynamic routes to pre-render).
* **Common Mistake:** Fallback controls behavior for non-pre-rendered paths.
* **Pro Tip:** getServerSideProps receives request context.

---

### ⭐ Senior Takeaway

These are Pages Router specific, App Router uses different patterns.

---

## 🧩 Q13. What is `getStaticPaths` and when do you use it?

### 🧠 Concept

`getStaticPaths` defines which dynamic routes to pre-render at build time. Use it with `getStaticProps` for static generation of dynamic pages.

---

### 💡 Example

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

### 🔍 Deep Insights

* **Rule:** Defines which dynamic routes to pre-render at build time.
* **Use Case:** Use with `getStaticProps` for static generation of dynamic pages.
* **Common Mistake:** Fallback controls behavior for non-pre-rendered paths.
* **Pro Tip:** Required for dynamic routes with SSG.

---

### ⭐ Senior Takeaway

Required for dynamic routes with SSG.

---

## 🧩 Q14. How do you implement data fetching in App Router?

### 🧠 Concept

Server components can use async functions and `fetch` directly, while client components use `useEffect` and state. Server components reduce JavaScript bundle size (performance).

---

### 💡 Example

```javascript
// Server Component - can use async and fetch directly
async function ServerComponent() {
  const res = await fetch('https://api.example.com/data');
  const data = await res.json();
  return <div>{data.message}</div>;
}
```

---

### 🔍 Deep Insights

* **Rule:** Server components run on server, can use async/await.
* **Use Case:** Client components run in browser, use hooks and state.
* **Common Mistake:** Server components reduce JavaScript bundle size (performance).
* **Pro Tip:** Server components fetch data during rendering.

---

### ⭐ Senior Takeaway

Client components need to be hydrated.

---

## 🧩 Q15. What are React Server Components (RSC)?

### 🧠 Concept

RSC run on the server, can't use browser APIs, and don't re-render, while client components run in the browser. Only client components can handle user interactions (interactivity).

---

### 💡 Example

```javascript
// Server Component - runs on server
async function ServerComponent() {
  const data = await fetch('https://api.example.com/data');
  const posts = await data.json();
  return <div>{posts.map(p => <p key={p.id}>{p.title}</p>)}</div>;
}
```

---

### 🔍 Deep Insights

* **Rule:** Server components run on server, no JavaScript sent to client.
* **Use Case:** Client components run in browser, can use hooks and state.
* **Common Mistake:** Server components reduce client bundle size.
* **Pro Tip:** Server components can't use window, document, etc. (browser APIs).

---

### ⭐ Senior Takeaway

Only client components can handle user interactions (interactivity).

---

## 🧩 Q16. How does caching and revalidation work with `fetch()`?

### 🧠 Concept

The `revalidate` option caches data for the specified seconds before revalidating. Reduces database and API calls (performance).

---

### 💡 Example

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

### 🔍 Deep Insights

* **Rule:** Revalidate time in seconds before cache expires.
* **Use Case:** Tags allow targeted cache invalidation.
* **Common Mistake:** False caches forever until manual revalidation.
* **Pro Tip:** Next.js handles caching automatically.

---

### ⭐ Senior Takeaway

Reduces database and API calls (performance).

---

## 🧩 Q17. What are revalidation tags and how do you use them?

### 🧠 Concept

Revalidation tags allow targeted cache invalidation, while `revalidatePath` invalidates specific routes. Only revalidates what's necessary (performance).

---

### 💡 Example

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

### 🔍 Deep Insights

* **Rule:** Tags group related data for targeted invalidation.
* **Use Case:** `revalidateTag` invalidates all data with specific tag.
* **Common Mistake:** `revalidatePath` invalidates specific routes.
* **Pro Tip:** More precise than global revalidation (granular).

---

### ⭐ Senior Takeaway

Only revalidates what's necessary (performance).

---

## 🧩 Q18. How do you implement on-demand revalidation?

### 🧠 Concept

On-demand revalidation allows you to manually invalidate cached data using `revalidateTag` or `revalidatePath`. Use it when data changes outside of the normal revalidation cycle.

---

### 💡 Example

```javascript
import { revalidateTag } from 'next/cache';

export async function POST() {
  // Update data
  revalidateTag('posts');
  return Response.json({ revalidated: true });
}
```

---

### 🔍 Deep Insights

* **Rule:** `revalidateTag` invalidates all data with specific tag.
* **Use Case:** `revalidatePath` invalidates specific routes.
* **Common Mistake:** Use after data mutations to keep cache fresh.
* **Pro Tip:** More precise than global revalidation (granular).

---

### ⭐ Senior Takeaway

Use after data mutations to keep cache fresh.

---

## 🧩 Q19. What is the fallback mechanism in ISR?

### 🧠 Concept

Fallback controls how Next.js handles pages not generated at build time. Choose based on build time vs runtime needs.

---

### 💡 Example

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

### 🔍 Deep Insights

* **Rule:** False (only pre-rendered paths work, 404 for others), True (show loading for non-pre-rendered paths), Blocking (wait for generation, then render).
* **Use Case:** False is fastest, blocking is slowest (performance).
* **Common Mistake:** True provides better user experience (UX).
* **Pro Tip:** Fallback affects how dynamic routes are handled.

---

### ⭐ Senior Takeaway

Choose based on build time vs runtime needs.

---

## 🧩 Q20. What is the difference between API routes and Server Actions?

### 🧠 Concept

API routes are REST endpoints, while Server Actions are functions that run on the server. Server actions provide better TypeScript support (type safety).

---

### 💡 Example

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

### 🔍 Deep Insights

* **Rule:** API routes are traditional REST endpoints, good for external APIs.
* **Use Case:** Server actions are functions that run on server, good for forms.
* **Common Mistake:** Server actions are more efficient for simple operations (performance).
* **Pro Tip:** Server actions integrate better with Next.js caching.

---

### ⭐ Senior Takeaway

Server actions provide better TypeScript support (type safety).

---
