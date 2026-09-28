---
sidebar_label: "Cheatsheet"
sidebar_position: 100
---
# ⚛️ Next.js Interview Cheatsheet

> **Reviewed:** 2026-09 · Modernized for Next.js 15/16 App Router. Legacy (Pages Router) topics are labeled.

> **⏱️ Review Time: 15-20 minutes** | **Priority: ⭐⭐ Medium** | Quick reference for Next.js interviews
>
> **Coverage: Q1-Q68** (68 questions across 6 topics)

**Quick Review Checklist:**

- [ ] Next.js Basics (App Router, Server/Client Components)

- [ ] Data Fetching (Server Components, `fetch` caching, `"use cache"`, revalidation)

- [ ] Caching layers & Next 15 defaults (nothing cached unless you opt in)

- [ ] Routing & Navigation (async `params`, `next/navigation`, streaming, parallel/intercepting routes)

- [ ] Performance (Image Optimization, Code Splitting, Scripts, PPR)

- [ ] Route Handlers & Server Actions (validate + authorize inside every action)

- [ ] Authentication (Auth.js v5 `auth()`, data access layer, `proxy.ts` as optimistic check only)

- [ ] Deployment (Vercel, Docker standalone, Turbopack, build output)

---

## 📋 **Question Coverage**

- **Q1-Q10**: Fundamentals

- **Q11-Q20, Q61-Q64**: Data Fetching & Rendering (boundaries, Server Action security, caching layers, async request APIs)

- **Q21-Q27, Q65-Q66**: Routing & Navigation (streaming, middleware/`proxy.ts` vs Route Handlers)

- **Q28-Q37, Q67**: Performance & Optimization (PPR / Cache Components)

- **Q38-Q48**: Architecture & Best Practices

- **Q49-Q60, Q68**: Deployment & Tooling (Pages → App Router migration)

---

## 📋 **Next.js Basics**

| Concept | Description | Example |
|---------|-------------|---------|
| **App Router** | Modern routing system (default since 13.4) | `app/page.js` → `/` |
| **Server Components** | Default; run on server, their code isn't shipped to the client | `async function Component()` |
| **Client Components** | SSR'd, then hydrated; use hooks/events | `'use client'` |
| **SSR** | Render per request | App: read `cookies()`/uncached data · Pages (legacy): `getServerSideProps` |
| **SSG** | Prerender at build | App: static route / `generateStaticParams` · Pages (legacy): `getStaticProps` |
| **ISR** | Regenerate in background | `export const revalidate = 60` / `next: { revalidate: 60 }` |
| **Server Actions** | Server mutations called from forms/components | `'use server'` |
| **Caching (15+)** | `fetch`, GET Route Handlers, client page segments uncached by default | `cache: 'force-cache'`, `"use cache"` (16) |
| **PPR** | Static shell + streamed dynamic holes | Next 16: `cacheComponents: true` |

---

## 🏗️ **Project Structure**

### **App Router Structure**

**Definition:** Next.js 13+ App Router uses file-based routing with app directory, supports layouts, route groups, and nested routes for modern React Server Components architecture.

```javascript
// app/
//   ├── layout.js          // Root layout
//   ├── page.js            // Home page
//   ├── (auth)/            // Route group
//   │   ├── login/
//   │   │   └── page.js
//   │   └── register/
//   │       └── page.js
//   ├── dashboard/
//   │   ├── layout.js      // Nested layout
//   │   ├── page.js
//   │   └── settings/
//   │       └── page.js
//   ├── api/
//   │   └── users/
//   │       └── route.js
//   ├── components/
//   │   └── ui/
//   │       └── Button.js
//   └── lib/
//       └── auth.js

```

### **Pages Router Structure (Legacy)**

```javascript
// pages/
//   ├── _app.js            // App wrapper
//   ├── _document.js       // HTML document
//   ├── index.js           // Home page
//   ├── about.js           // About page
//   ├── blog/
//   │   ├── index.js
//   │   └── [slug].js      // Dynamic route
//   └── api/
//       └── users.js

```

---

## 🔄 **Data Fetching**

### **App Router (Modern)**

**Definition:** Server Components are async functions that fetch data on the server, reducing client bundle size and improving performance by eliminating unnecessary JavaScript.

```javascript
// Server Component - async function
async function ServerComponent() {
  const data = await fetch('https://api.example.com/data', {
    next: { revalidate: 3600, tags: ['posts'] }, // opt in: uncached by default in Next 15+
  });
  const posts = await data.json();

  return (
    <div>
      {posts.map(post => (
        <div key={post.id}>{post.title}</div>
      ))}
    </div>
  );
}

// Next 16 (cacheComponents): cache any async work
async function getCategories() {
  'use cache';
  cacheLife('days');       // from 'next/cache'
  cacheTag('categories');
  return db.category.findMany();
}

// Client Component - client-driven data via TanStack Query (not ad-hoc useEffect)
'use client';

import { useQuery } from '@tanstack/react-query';

function ClientComponent() {
  const { data } = useQuery({
    queryKey: ['data'],
    queryFn: () => fetch('/api/data').then(res => res.json()),
  });
  return <div>{data?.message}</div>;
}

```

### **Pages Router (Legacy)**

> **Legacy note (2026):** Still supported and common in production apps; for new work prefer the App Router patterns above (see Q12, Q68).

```javascript
// SSG - Static Site Generation
export async function getStaticProps() {
  const data = await fetch('https://api.example.com/data');
  const posts = await data.json();

  return {
    props: { posts },
    revalidate: 3600 // ISR
  };
}

// SSR - Server Side Rendering
export async function getServerSideProps() {
  const data = await fetch('https://api.example.com/data');
  const posts = await data.json();

  return { props: { posts } };
}

// Dynamic routes
export async function getStaticPaths() {
  const posts = await fetch('https://api.example.com/posts');
  const data = await posts.json();

  const paths = data.map(post => ({
    params: { id: post.id.toString() }
  }));

  return { paths, fallback: 'blocking' };
}

```

---

## 🧭 **Routing & Navigation**

### **App Router Navigation**

```javascript
import Link from 'next/link';
import { useRouter } from 'next/navigation';

// Link component (the old `as` prop is a Pages Router legacy; not needed)
<Link href="/about">About</Link>
<Link href={`/blog/${slug}`}>My Post</Link>

// Programmatic navigation (Client Component)
const router = useRouter();
router.push('/about');
router.replace('/login');
router.back();
router.refresh(); // re-fetch Server Components for current route

// Server-side (Server Components / Actions)
import { redirect, notFound } from 'next/navigation';

```

### **Dynamic Routes**

```javascript
// app/blog/[slug]/page.js - params is a Promise in Next 15+
export default async function BlogPost({ params }) {
  const { slug } = await params;
  return <h1>Post: {slug}</h1>;
}

// app/blog/[...slug]/page.js - Catch-all
export default async function BlogCatchAll({ params }) {
  const { slug } = await params;
  return <h1>Blog: {slug.join('/')}</h1>;
}

// app/blog/[[...slug]]/page.js - Optional catch-all (double brackets)
export default async function BlogOptional({ params }) {
  const { slug } = await params;
  return <h1>{slug ? `Blog: ${slug.join('/')}` : 'Blog Home'}</h1>;
}

// Prerender known params (replaces getStaticPaths)
export async function generateStaticParams() {
  return (await getSlugs()).map(slug => ({ slug }));
}

```

---

## ⚡ **Performance Optimization**

### **Image Optimization**

**Definition:** Next.js Image component automatically optimizes images with lazy loading, responsive sizing, modern formats (WebP/AVIF), and CDN delivery for better performance.

```javascript
import Image from 'next/image';

// Basic usage
<Image
  src="/hero.jpg"
  alt="Hero image"
  width={800}
  height={600}
/>

// Responsive image
<Image
  src="/responsive.jpg"
  alt="Responsive"
  width={800}
  height={600}
  sizes="(max-width: 768px) 100vw, 50vw"
/>

// Priority loading for the LCP image (Next 16: `preload` replaces `priority`)
<Image
  src="/above-fold.jpg"
  alt="Above fold"
  width={800}
  height={600}
  priority
/>

// Remote images: allow-list with images.remotePatterns (images.domains is deprecated)

```

### **Code Splitting**

```javascript
import dynamic from 'next/dynamic';

// Lazy loading
const LazyComponent = dynamic(() => import('./HeavyComponent'));

// With loading state
const LazyComponent = dynamic(
  () => import('./HeavyComponent'),
  { loading: () => <p>Loading...</p> }
);

// Disable SSR - App Router: only allowed inside a 'use client' file
const ClientOnlyComponent = dynamic(
  () => import('./ClientOnlyComponent'),
  { ssr: false }
);

```

### **Script Optimization**

```javascript
import Script from 'next/script';

// After interactive
<Script
  src="https://www.googletagmanager.com/gtag/js?id=GA_MEASUREMENT_ID"
  strategy="afterInteractive"
/>

// Before interactive (root layout only; truly critical scripts)
// Note: avoid the polyfill.io CDN - the domain was compromised in a 2024 supply-chain attack
<Script
  src="/scripts/consent-manager.js"
  strategy="beforeInteractive"
/>

// Lazy onload
<Script
  src="https://example.com/analytics.js"
  strategy="lazyOnload"
/>

```

---

## 🔧 **API Routes**

### **App Router API Routes**

```javascript
// app/api/users/route.js
export async function GET() {
  const users = await getUsers();
  return Response.json(users);
}

export async function POST(request) {
  const body = await request.json();
  const user = await createUser(body);
  return Response.json(user, { status: 201 });
}

// Dynamic segment - params is a Promise (Next 15+)
// app/api/users/[id]/route.js
export async function GET(request, { params }) {
  const { id } = await params;
  return Response.json(await getUser(id));
}

// Edge runtime (opt-in; Node.js is the default)
export const runtime = 'edge';

// Note: GET handlers are NOT cached by default in Next 15+
// (opt in with `export const dynamic = 'force-static'`)

```

### **Pages Router API Routes (Legacy)**

```javascript
// pages/api/users.js
export default function handler(req, res) {
  if (req.method === 'GET') {
    res.json({ users: [] });
  } else if (req.method === 'POST') {
    res.status(201).json({ message: 'User created' });
  }
}

```

---

## 🎯 **Server Actions**

```javascript
// app/posts/actions.js - Server Action (a public POST endpoint!)
'use server';
import { revalidatePath } from 'next/cache';
import { z } from 'zod';

const PostSchema = z.object({ title: z.string().min(1), content: z.string().min(1) });

export async function createPost(prevState, formData) {
  const session = await auth();                         // authenticate
  if (!session) return { error: 'Unauthorized' };
  const parsed = PostSchema.safeParse(Object.fromEntries(formData)); // validate
  if (!parsed.success) return { error: 'Invalid input' };

  await db.posts.create({ ...parsed.data, authorId: session.user.id });
  revalidatePath('/posts');
  return { ok: true };                                  // minimal response
}

// app/posts/new/form.js - Client Component with React 19 hooks
'use client';
import { useActionState } from 'react';
import { createPost } from '../actions';

export default function CreatePostForm() {
  const [state, formAction, isPending] = useActionState(createPost, null);
  return (
    <form action={formAction}>
      <input name="title" placeholder="Title" required />
      <textarea name="content" placeholder="Content" required />
      {state?.error && <p role="alert">{state.error}</p>}
      <button type="submit" disabled={isPending}>Create Post</button>
    </form>
  );
}

```

---

## 🎨 **Styling**

### **CSS Modules**

```javascript
// styles.module.css
.container {
  max-width: 1200px;
  margin: 0 auto;
}

// Component
import styles from './styles.module.css';

export default function Component() {
  return <div className={styles.container}>Content</div>;
}

```

### **Styled JSX**

```javascript
export default function Component() {
  return (
    <div>
      <style jsx>{`
        .container {
          max-width: 1200px;
          margin: 0 auto;
        }
      `}</style>
      <div className="container">Content</div>
    </div>
  );
}

```

### **Tailwind CSS**

```javascript
export default function Component() {
  return (
    <div className="max-w-4xl mx-auto p-4">
      <h1 className="text-2xl font-bold">Title</h1>
    </div>
  );
}

```

---

## 🔐 **Authentication**

### **Auth.js (NextAuth v5)**

```javascript
// auth.js
import NextAuth from 'next-auth';
import Credentials from 'next-auth/providers/credentials';

export const { handlers, auth, signIn, signOut } = NextAuth({
  providers: [
    Credentials({
      credentials: { email: {}, password: {} },
      authorize: async (credentials) => validateUser(credentials), // return user or null
    }),
  ],
  callbacks: {
    jwt({ token, user }) { if (user) token.id = user.id; return token; },
    session({ session, token }) { session.user.id = token.id; return session; },
  },
});

// app/api/auth/[...nextauth]/route.js
import { handlers } from '@/auth';
export const { GET, POST } = handlers;

// Anywhere on the server: Server Components, Server Actions, Route Handlers
const session = await auth();

```

> **Legacy note (2026):** NextAuth v4 (`authOptions`, `getServerSession`, `withAuth` from `next-auth/middleware`) is still widespread; v5 unifies everything behind `auth()`.

### **Middleware / Proxy Protection (optimistic only)**

```javascript
// proxy.js (Next 16) — middleware.js with `export function middleware` in Next ≤15
import { NextResponse } from 'next/server';

export function proxy(request) {
  if (!request.cookies.has('authjs.session-token')) {
    return NextResponse.redirect(new URL('/login', request.url));
  }
  return NextResponse.next();
}

export const config = {
  matcher: ['/dashboard/:path*', '/admin/:path*']
};

// ⚠️ Always re-check auth where data is read/mutated (DAL, Server Actions, Route Handlers)

```

---

## 📊 **State Management**

### **Context API**

```javascript
'use client';

import { createContext, useContext, useState } from 'react';

const ThemeContext = createContext(null);

export function ThemeProvider({ children }) {
  const [theme, setTheme] = useState('light');

  // React 19: <ThemeContext value> (ThemeContext.Provider still works)
  return (
    <ThemeContext value={{ theme, setTheme }}>
      {children}
    </ThemeContext>
  );
}

export function useTheme() {
  return useContext(ThemeContext);
}

```

### **Zustand**

> In the App Router, a module-level store is shared across requests on the server. For per-user data, create the store inside a provider (per request); a global store is fine for purely client-side UI state.

```javascript
'use client';
import { create } from 'zustand';

const useStore = create((set) => ({
  count: 0,
  increment: () => set((state) => ({ count: state.count + 1 })),
  decrement: () => set((state) => ({ count: state.count - 1 }))
}));

export default function Counter() {
  const { count, increment, decrement } = useStore();

  return (
    <div>
      <p>Count: {count}</p>
      <button onClick={increment}>+</button>
      <button onClick={decrement}>-</button>
    </div>
  );
}

```

---

## 🚀 **Deployment**

### **Vercel Deployment**

```bash

# Install Vercel CLI

npm i -g vercel

# Deploy

vercel

# Production deployment

vercel --prod

```

### **Docker Deployment**

```dockerfile
# Requires output: 'standalone' in next.config
FROM node:22-alpine AS base
WORKDIR /app

FROM base AS deps
COPY package*.json ./
RUN npm ci

FROM base AS builder
COPY --from=deps /app/node_modules ./node_modules
COPY . .
RUN npm run build

FROM base AS runner
ENV NODE_ENV=production
COPY --from=builder /app/.next/standalone ./
COPY --from=builder /app/.next/static ./.next/static
COPY --from=builder /app/public ./public

EXPOSE 3000
CMD ["node", "server.js"]

```

---

## 🎯 **Interview Tips**

### **Common Questions**

1. **App Router vs Pages Router** - Modern default vs legacy (still supported)

2. **Server Components vs Client Components** - Where to put the `'use client'` boundary

3. **Data Fetching & Caching** - Next 15 uncached defaults, `revalidate`, tags, `"use cache"` (16)

4. **Server Actions** - Mutations + security (validate, authorize inside the action)

5. **Performance** - Streaming, PPR, image optimization, less client JS

6. **Authentication** - Auth.js `auth()`, data access layer, `proxy.ts` as optimistic gate

### **Key Concepts**

- **Server Components**: Run on server; their code never ships to the browser

- **Client Components**: SSR'd then hydrated; hooks, events, browser APIs

- **App Router**: Nested layouts, streaming, Metadata API, `next/navigation`

- **Caching**: Request memoization, Data Cache, Full Route Cache, Router Cache

- **Deployment**: Vercel, Docker (`standalone`), static export, Turbopack

### **Best Practices**

- Use Server Components by default; keep `'use client'` islands small

- Fetch in parallel and stream slow parts with Suspense

- Decide caching explicitly per data source and invalidate on mutation

- Validate input and check authorization in every Server Action / Route Handler

- Optimize images with next/image and fonts with next/font

- Use TypeScript and run lint as a separate CI step (`next lint` removed in 16)

---

## ⚡ **Last-Minute Review (5 minutes)**

### **Must-Know Concepts**

- **App Router**: Modern routing (Next 13.4+), file-based routing

- **Server Components**: Run on server, component code not sent to client (default)

- **Client Components**: Use `'use client'` for hooks, interactivity

- **Data Fetching**: Server Components can be async, fetch directly; not cached by default (15+)

- **Async request APIs (15+)**: `await params`, `await searchParams`, `await cookies()`, `await headers()`

- **SSR/SSG/ISR**: Inferred per route in App Router; explicit functions only in Pages Router

### **Quick Code Snippets**

```javascript
// Server Component (default)
async function ServerComponent() {
  const data = await fetch('https://api.example.com/data').then(r => r.json());
  return <div>{data.title}</div>;
}

// Client Component
'use client';
function ClientComponent() {
  const [state, setState] = useState(0);
  return <button onClick={() => setState(s => s + 1)}>{state}</button>;
}

// Image Optimization
<Image src="/hero.jpg" width={800} height={600} alt="Hero" priority />

```

### **Common Gotchas**

- Server Components can't use hooks or browser APIs

- Client Components must have `'use client'` directive

- App Router uses `async` components for data fetching

- Image component requires width/height (or fill with parent)

- Upgrading 14 → 15 changes caching defaults silently; 15 → 16 removes sync `params`/`cookies()` access and renames `middleware.ts` to `proxy.ts`

- `ssr: false` in `next/dynamic` only works inside Client Components

*Remember: Focus on App Router, Server Components, Server Actions, and the caching model for 2026 interviews - but be ready to explain Pages Router code you'll meet in existing apps!*
