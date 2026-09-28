---
sidebar_label: "Architecture & Patterns"
---
# 🏗️ 5. Architecture & Patterns (Q38–48)

> **Reviewed:** 2026-09 · Modernized for Next.js 15/16 App Router. Legacy (Pages Router) topics are labeled.

---

## Q38. ▲ ▲ ▲ Structuring a scalable Next.js project

Organize with `app/` directory for modern Next.js structure, co-located components (keep related files together), and proper separation of concerns (UI, logic, data) - structure for growth and maintenance. Use route groups `(group)` for organization (and separate root layouts) without URL impact, `_private` folders for non-routable code, a server-only data access layer (`lib/dal.ts` with `import 'server-only'`) that every Server Component and Server Action goes through, and colocated `actions.ts` files for Server Actions.

- **Trade-offs**: The catch is co-location keeps related files together and makes code easier to find, but watch out - structure for growth and maintenance, and use route groups to organize without affecting URLs, which helps with large projects.

Example:

```javascript
// Project structure
// src/
//   ├── app/
//   │   ├── (marketing)/          // route group, own layout
//   │   │   └── pricing/page.tsx
//   │   ├── (auth)/
//   │   │   ├── login/page.tsx
//   │   │   └── register/page.tsx
//   │   ├── dashboard/
//   │   │   ├── _components/      // private, not routable
//   │   │   ├── actions.ts        // 'use server'
//   │   │   ├── loading.tsx
//   │   │   └── page.tsx
//   │   └── api/webhooks/route.ts
//   ├── components/ui/            // shared client/server UI
//   └── lib/
//       ├── dal.ts                // import 'server-only'; auth + data access
//       └── db.ts
// proxy.ts                        // Next 16 (middleware.ts before)

```

---

## Q39. 🔐 Implementing authentication in Next.js

Use an auth library (Auth.js / NextAuth v5, Clerk, Better Auth, WorkOS, a hosted IdP) or a well-reviewed session implementation, store sessions in **httpOnly, Secure, SameSite** cookies (JWT or database sessions), and enforce auth in layers: an optional **optimistic** check in middleware/`proxy.ts` to redirect signed-out users early, and **authoritative** checks close to the data - in a server-only data access layer used by Server Components, Server Actions, and Route Handlers. Auth.js v5 exposes a single `auth()` helper that works in all of those places.

- **Trade-offs**: The catch is libraries handle OAuth flows, CSRF, and cookie security for you, but watch out - layout-level checks aren't enough (layouts don't re-run on every navigation, and Server Actions can be called directly), and middleware-only protection was shown to be bypassable on unpatched versions (CVE-2025-29927). JWT sessions scale without a DB lookup but are hard to revoke; database sessions are revocable but cost a query.

Example:

```javascript
// auth.ts - Auth.js (NextAuth v5)
import NextAuth from 'next-auth';
import GitHub from 'next-auth/providers/github';

export const { handlers, auth, signIn, signOut } = NextAuth({
  providers: [GitHub],
  session: { strategy: 'jwt' },
});

// app/api/auth/[...nextauth]/route.ts
import { handlers } from '@/auth';
export const { GET, POST } = handlers;

// app/dashboard/page.tsx - authoritative check where data is read
import { auth } from '@/auth';
import { redirect } from 'next/navigation';
export default async function Dashboard() {
  const session = await auth();
  if (!session) redirect('/login');
  return <h1>Welcome {session.user?.name}</h1>;
}

```

> **Legacy note (2026):** NextAuth v4 used `authOptions` + `getServerSession(authOptions)` and `pages/api/auth/[...nextauth].js`. You'll still see it in many codebases; v5 (Auth.js) replaces it with the universal `auth()` helper.

---

## Q40. 📦 Handling global state management

In the App Router, much of what used to be "global state" is really **server data** - fetch it in Server Components and pass it down, or put UI state in the **URL** (`searchParams`) so it's shareable and server-renderable. For genuine client state use Context for simple, rarely changing values, Zustand/Jotai for more complex client state, and TanStack Query for client-driven server state (polling, infinite lists). Providers must live in a `'use client'` component rendered from the root layout.

- **Trade-offs**: The catch is less client state means less hydration and fewer sync bugs, but watch out - module-level stores (e.g. a global Zustand store created at import time) are **shared across requests on the server**, leaking data between users; create stores per request inside a provider. Also avoid reading `localStorage` during render (hydration mismatch).

Example:

```javascript
'use client';
import { createContext, useContext, useState } from 'react';

const ThemeContext = createContext(null);

export function ThemeProvider({ children }) {
  const [theme, setTheme] = useState('light');
  // React 19: <Context value> works as a provider (.Provider still supported)
  return (
    <ThemeContext value={{ theme, setTheme }}>
      {children}
    </ThemeContext>
  );
}

// URL as state - app/products/page.tsx (Server Component)
export default async function Products({ searchParams }) {
  const { sort = 'price' } = await searchParams;
  const products = await getProducts({ sort });
  return <ProductList products={products} />; // <Link href="?sort=name"> changes it
}

```

---

## Q41. 💡 Implementing error handling and error boundaries

Separate **expected** errors from **unexpected** ones. Expected errors (validation failures, "not found", permission denied) are modeled as return values - Server Actions return `{ error }` consumed via `useActionState`, and pages call `notFound()`. Unexpected errors are thrown and caught by `error.tsx` (route-level boundary, must be a Client Component), `global-error.tsx` for the root layout, and component-level boundaries (e.g. `react-error-boundary`) for widgets. Log server errors centrally with `onRequestError` in `instrumentation.ts`.

- **Trade-offs**: The catch is `error.tsx` provides route-level error handling and you can have nested errors for different routes, but watch out - error boundaries must be client components, and always provide recovery mechanisms like reset functions.

Example:

```javascript
'use client';

export default function Error({ error, reset }) {
  return (
    <div>
      <h2>Something went wrong!</h2>
      <button onClick={() => reset()}>Try again</button>
    </div>
  );
}

```

---

## Q42. ▲ ▲ ▲ Handling side effects in Next.js

Keep rendering pure and put side effects where they belong: **reads** in Server Components; **writes** (DB mutations, emails, payments) in Server Actions or Route Handlers - never during render, since a render can run multiple times or be prerendered at build; **post-response work** (analytics, logging, cache warming) in `after()` from `next/server` (stable since Next 15.1), which runs after the response is sent; and **browser side effects** (subscriptions, DOM APIs, third-party widgets) in `useEffect` inside Client Components.

- **Trade-offs**: The catch is clear placement makes behavior predictable under prerendering, streaming, and retries, but watch out - a "harmless" write in a Server Component (e.g. incrementing a view counter) may run at build time or be cached; move it to `after()` or an action. In Client Components, prefer event handlers over effects for user-triggered work.

Example:

```javascript
// Server Component - reads + post-response side effect
import { after } from 'next/server';

export default async function Article({ params }) {
  const { slug } = await params;
  const article = await getArticle(slug);
  after(() => recordView(slug)); // runs after the response is sent
  return <article>{article.body}</article>;
}

// Client Component - browser side effect
'use client';
import { useEffect } from 'react';
export function ChatWidget() {
  useEffect(() => {
    const widget = loadChatWidget();
    return () => widget.destroy(); // cleanup
  }, []);
  return null;
}

```

---

## Q43. 💡 Implementing role-based access control

Enforce roles **on the server, next to the data**: a data access layer function like `requireRole('admin')` called from every Server Component, Server Action, and Route Handler that touches protected data. Middleware/`proxy.ts` can do a fast optimistic redirect based on a role claim in the session cookie, and Client Components can hide buttons the user can't use - but both are UX conveniences, not security.

- **Trade-offs**: The catch is centralizing checks in one server-only module makes RBAC auditable and testable, but watch out - hiding a button doesn't stop a direct Server Action call, middleware can be misconfigured or (on unpatched versions) bypassed, and role claims baked into long-lived JWTs go stale when roles change; re-check critical permissions against the database.

Example:

```javascript
// lib/dal.ts
import 'server-only';
import { cache } from 'react';
import { redirect } from 'next/navigation';
import { auth } from '@/auth';

export const requireRole = cache(async (role: 'admin' | 'editor') => {
  const session = await auth();
  if (!session) redirect('/login');
  if (session.user.role !== role) redirect('/unauthorized');
  return session.user;
});

// app/admin/page.tsx
export default async function AdminPage() {
  await requireRole('admin');                 // authoritative check
  const users = await db.user.findMany();
  return <UserTable users={users} />;
}

// app/admin/actions.ts
'use server';
export async function deleteUser(id: string) {
  await requireRole('admin');                 // check again: actions are public endpoints
  await db.user.delete({ where: { id } });
}

```

---

## Q44. 🕸️ Integrating GraphQL with Next.js

Use GraphQL in Server Components for initial data fetching - often a plain `fetch` POST (which participates in Next.js caching/tags) or a server-side client - and a client library in Client Components for interactive queries, mutations, and subscriptions. Apollo's App Router integration (`@apollo/client-integration-nextjs`, formerly `@apollo/experimental-nextjs-app-support`) provides `registerApolloClient` for RSC and a provider for streaming SSR in Client Components; URQL and Relay are alternatives. For mutations from your own UI, a Server Action that calls the GraphQL API is often simpler than a client mutation.

- **Trade-offs**: The catch is GraphQL integrates well with Next.js, and GraphQL clients provide sophisticated caching, but watch out - you now have two caches (the GraphQL client's normalized cache and Next.js's server caches) that must be invalidated consistently, and a per-request client must be created on the server to avoid leaking data between users.

Example:

```javascript
// lib/apollo-rsc.ts
import { registerApolloClient, ApolloClient, InMemoryCache } from '@apollo/client-integration-nextjs';
import { HttpLink, gql } from '@apollo/client';

export const { getClient } = registerApolloClient(() =>
  new ApolloClient({ cache: new InMemoryCache(), link: new HttpLink({ uri: process.env.GRAPHQL_URL }) })
);

const GET_POSTS = gql`
  query GetPosts {
    posts {
      id
      title
    }
  }
`;

// app/posts/page.tsx - Server Component
export default async function PostsPage() {
  const { data } = await getClient().query({ query: GET_POSTS });
  return <PostsList posts={data.posts} />;
}

```

---

## Q45. 🖥️ Securing API routes and Server Actions

Treat Route Handlers and Server Actions the same way: authenticate the session, authorize the specific resource, validate input with a schema, return minimal data, and rate-limit expensive or abusable endpoints. Server Actions get built-in CSRF mitigation (POST-only + `Origin`/`Host` comparison); Route Handlers that accept cookies-based auth for state-changing requests need your own CSRF defense (SameSite cookies, origin checks, or tokens). Add security headers (CSP, `X-Frame-Options`/`frame-ancestors`, HSTS) in `next.config` or middleware/proxy, keep secrets in `server-only` modules, and consider React's taint APIs (`experimental.taint`) to block specific sensitive objects from being passed to Client Components. See Q62 for a full Server Action example.

- **Trade-offs**: The catch is use security headers for protection and implement rate limiting to prevent abuse, but watch out - always validate and sanitize all inputs, and never trust client-side data, since it can be manipulated. Keep Next.js patched: framework-level advisories (like the 2025 middleware bypass) are fixed in point releases.

Example:

```javascript
// app/api/projects/[id]/route.ts
import { auth } from '@/auth';
import { z } from 'zod';

const Body = z.object({ name: z.string().min(1).max(100) });

export async function PATCH(request: Request, { params }: { params: Promise<{ id: string }> }) {
  const session = await auth();
  if (!session) return Response.json({ error: 'Unauthorized' }, { status: 401 });

  const { id } = await params;
  const project = await db.project.findUnique({ where: { id } });
  if (project?.ownerId !== session.user.id) {
    return Response.json({ error: 'Forbidden' }, { status: 403 });
  }

  const parsed = Body.safeParse(await request.json());
  if (!parsed.success) return Response.json({ error: 'Invalid body' }, { status: 400 });

  const updated = await db.project.update({ where: { id }, data: parsed.data });
  return Response.json({ id: updated.id, name: updated.name }); // minimal response
}

```

> **Legacy note (2026):** NextAuth v4's `getServerSession(authOptions)` and Pages Router `pages/api` handlers are still common; the security rules are identical.

---

## Q46. ⚙️ Implementing middleware vs edge functions

Middleware (renamed **`proxy.ts`** in Next 16) runs before routing for every request that matches its `matcher` - good for rewrites, redirects, headers, and optimistic auth gating. "Edge functions" are just Route Handlers or pages that opt into `export const runtime = 'edge'` - they own a specific URL. Middleware historically ran only on the Edge runtime; newer versions support the Node.js runtime too, and in Next 16 `proxy.ts` runs on Node.js. Choose Edge only when you need its latency profile and your dependencies are Web-API compatible. See Q66 for middleware vs Route Handlers.

- **Trade-offs**: The catch is edge code starts fast and can run near users, but watch out - it can't use most Node APIs or TCP database drivers, and running far from your database adds latency; middleware/proxy is on the hot path of every matched request, so keep it tiny and never rely on it as the only authorization check.

Example:

```javascript
// proxy.ts (Next 16) — in Next ≤15 this is middleware.ts with `export function middleware`
import { NextResponse } from 'next/server';

export function proxy(request) {
  const { pathname } = request.nextUrl;
  if (pathname.startsWith('/admin') && !request.cookies.has('session')) {
    return NextResponse.redirect(new URL('/login', request.url)); // optimistic only
  }
  return NextResponse.next();
}

export const config = {
  matcher: '/admin/:path*'
};

```

---

## Q47. 🎨 Implementing hybrid rendering strategies

In the App Router, hybrid rendering happens **within a single page**, not just across pages: static/cached Server Components for content that rarely changes, request-time Server Components (inside Suspense) for personalized parts, and Client Components for interactivity. With Next 16 Cache Components this becomes explicit - `"use cache"` parts join the prerendered shell and Suspense-wrapped dynamic parts stream in (PPR, Q67). Across routes you still mix fully static pages, ISR-style `revalidate` pages, and fully dynamic pages.

- **Trade-offs**: The catch is choose rendering strategy per component based on data requirements, and use Suspense for progressive loading, but watch out - combine strategies for optimal performance, since different parts of your app have different needs.

Example:

```javascript
import { Suspense } from 'react';

export default function HybridPage() {
  return (
    <div>
      {/* Static / cached content - part of the prerendered shell */}
      <CachedCategoryNav />  {/* 'use cache' inside (Next 16) */}

      {/* Request-time content - streamed */}
      <Suspense fallback={<GreetingSkeleton />}>
        <PersonalizedGreeting /> {/* reads cookies() */}
      </Suspense>

      {/* Interactive island - 'use client', SSR'd then hydrated */}
      <AddToCartButton />
    </div>
  );
}

```

---

## Q48. ▲ ▲ ▲ Common Next.js anti-patterns to avoid

Avoid overusing Client Components (`'use client'` on pages/layouts), `useEffect` fetching for data a Server Component could fetch, calling your own Route Handlers from Server Components, blocking waterfalls instead of streaming, assuming `fetch` is cached (Next 15+ defaults to uncached), auth checks only in layouts or middleware, global mutable stores on the server, and serving the same route from both `pages/` and `app/` (it's a build error). Running Pages and App Router side by side during an incremental migration is supported and fine (Q68).

- **Trade-offs**: The catch is follow Next.js best practices for optimal performance, and use Server Components when possible to reduce client-side JS, but watch out - avoid these anti-patterns, as these can significantly impact performance and user experience.

Example:

```javascript
// ❌ Anti-pattern: Overusing client components
'use client';
import { useState, useEffect } from 'react';
export default function Page() {
  const [data, setData] = useState(null);
  useEffect(() => {
    fetch('/api/data').then(r => r.json()).then(setData);
  }, []);
  return <div>{data}</div>;
}

// ✅ Better: Use Server Component (and parse the response!)
export default async function Page() {
  const data = await fetch('https://api.example.com/data').then(r => r.json());
  return <div>{data.message}</div>;
}

```

---

