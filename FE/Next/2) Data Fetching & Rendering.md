# 📡 2. Data Fetching & Rendering (Q11–20)

---

## 11) What are the rendering strategies in Next.js — SSR, SSG, ISR, and CSR?

Concept:
SSR renders on server, SSG pre-renders at build time, ISR updates static content, and CSR renders in browser.

Example:
```javascript
// SSR - Server Side Rendering
export async function getServerSideProps() {
  const res = await fetch('https://api.example.com/data');
  const data = await res.json();
  
  return { props: { data } };
```

Deep Insight:
- **SSR**: Good for dynamic content, SEO, but slower than SSG
- **SSG**: Fastest, good for static content, but data can be stale
- **ISR**: Best of both worlds - fast with fresh data
- **CSR**: Fastest initial load, but poor SEO and accessibility
- **Hybrid**: Use different strategies for different parts of app

---

## 12) How do `getStaticProps`, `getServerSideProps`, and `getStaticPaths` work? (**⚙️ Pages Router only**)

Concept:
These functions fetch data at build time (SSG) or request time (SSR) in the Pages Router.

Example:
```javascript
// getStaticProps - runs at build time
export async function getStaticProps() {
  const posts = await fetch('https://api.example.com/posts');
  const data = await posts.json();
  
  return {
```

Deep Insight:
- **getStaticProps**: Runs at build time, good for static content
- **getServerSideProps**: Runs on every request, good for dynamic content
- **getStaticPaths**: Defines which dynamic routes to pre-render
- **Fallback**: Controls behavior for non-pre-rendered paths
- **Context**: getServerSideProps receives request context

---

## 13) How do you fetch data in **App Router 🚀** using server components (async components, `fetch`) vs client components?

Concept:
Server components can use async functions and `fetch` directly, while client components use `useEffect` and state.

Example:
```javascript
// Server Component - can use async and fetch directly
async function ServerComponent() {
  const res = await fetch('https://api.example.com/data');
  const data = await res.json();
  
  return <div>{data.message}</div>;
}
```

Deep Insight:
- **Server Components**: Run on server, can use async/await
- **Client Components**: Run in browser, use hooks and state
- **Performance**: Server components reduce JavaScript bundle size
- **Data Fetching**: Server components fetch data during rendering
- **Hydration**: Client components need to be hydrated

---

## 14) What are **React Server Components (RSC)** in Next.js and how do they differ from client components? (**🚀 introduced in 13**)

Concept:
RSC run on the server, can't use browser APIs, and don't re-render, while client components run in the browser.

Example:
```javascript
// Server Component - runs on server
async function ServerComponent() {
  const data = await fetch('https://api.example.com/data');
  const posts = await data.json();
  
  return (
```

Deep Insight:
- **Server Components**: Run on server, no JavaScript sent to client
- **Client Components**: Run in browser, can use hooks and state
- **Bundle Size**: Server components reduce client bundle size
- **Browser APIs**: Server components can't use window, document, etc.
- **Interactivity**: Only client components can handle user interactions

---

## 15) How does caching and revalidation work using `fetch()` options like `{ next: { revalidate: 10 } }`? (**🚀 Next 14**)

Concept:
The `revalidate` option caches data for the specified seconds before revalidating.

Example:
```javascript
// Cache for 60 seconds
async function getData() {
  const res = await fetch('https://api.example.com/data', {
    next: { revalidate: 60 }
  });
  return res.json();
```

Deep Insight:
- **Revalidate**: Time in seconds before cache expires
- **Tags**: Allow targeted cache invalidation
- **False**: Cache forever until manual revalidation
- **Automatic**: Next.js handles caching automatically
- **Performance**: Reduces database and API calls

---

## 16) What are revalidation tags and on-demand revalidation (`revalidateTag`, `revalidatePath`)? (**🚀 Next 14**)

Concept:
Revalidation tags allow targeted cache invalidation, while `revalidatePath` invalidates specific routes.

Example:
```javascript
// Fetch with tags
async function getPosts() {
  const res = await fetch('https://api.example.com/posts', {
    next: { 
      revalidate: 3600,
      tags: ['posts', 'content']
```

Deep Insight:
- **Tags**: Group related data for targeted invalidation
- **revalidateTag**: Invalidates all data with specific tag
- **revalidatePath**: Invalidates specific routes
- **Granular**: More precise than global revalidation
- **Performance**: Only revalidates what's necessary

---

## 17) What is the fallback mechanism in `getStaticPaths` (`false`, `true`, `blocking`)? (**⚙️ old SSG**)

Concept:
Fallback controls how Next.js handles pages not generated at build time.

Example:
```javascript
// fallback: false - only pre-rendered paths work
export async function getStaticPaths() {
  return {
    paths: [
      { params: { id: '1' } },
      { params: { id: '2' } }
```

Deep Insight:
- **false**: Only pre-rendered paths work, 404 for others
- **true**: Show loading for non-pre-rendered paths
- **blocking**: Wait for generation, then render
- **Performance**: false is fastest, blocking is slowest
- **UX**: true provides better user experience

---

## 18) What are API routes and how do they differ from server actions?

Concept:
API routes are REST endpoints, while Server Actions are functions that run on the server.

Example:
```javascript
// API Route - REST endpoint
// pages/api/posts.js or app/api/posts/route.js
export async function GET() {
  const posts = await fetch('https://api.example.com/posts');
  const data = await posts.json();
  
```

Deep Insight:
- **API Routes**: Traditional REST endpoints, good for external APIs
- **Server Actions**: Functions that run on server, good for forms
- **Performance**: Server Actions are more efficient for simple operations
- **Caching**: Server Actions integrate better with Next.js caching
- **Type Safety**: Server Actions provide better TypeScript support

---

## 19) What are Server Actions (`"use server"`) in App Router and how do they replace API routes for mutations? (**🚀 Next 14**)

Concept:
Server Actions are server-side functions marked with `"use server"` that can be called from client components.

Example:
```javascript
// Server Action
'use server';

export async function createUser(formData) {
  const name = formData.get('name');
  const email = formData.get('email');
```

Deep Insight:
- **"use server"**: Marks function as Server Action
- **Form Integration**: Can be used directly in forms
- **Type Safety**: Better TypeScript support than API routes
- **Caching**: Integrates with Next.js caching system
- **Performance**: More efficient than API routes for simple operations

---

## 20) What are edge functions and the Edge Runtime, and when should you use them? (**🚀**)

Concept:
Edge functions run at the edge for low latency, ideal for simple transformations and redirects.

Example:
```javascript
// Edge Runtime API route
export const runtime = 'edge';

export async function GET(request) {
  const { searchParams } = new URL(request.url);
  const name = searchParams.get('name') || 'World';
```

Deep Insight:
- **Edge Runtime**: Runs at edge locations for low latency
- **Limitations**: Can't use Node.js APIs, limited to Web APIs
- **Use Cases**: Redirects, A/B testing, simple transformations
- **Performance**: Faster than Node.js runtime for simple operations
- **Global**: Runs closer to users worldwide

---
