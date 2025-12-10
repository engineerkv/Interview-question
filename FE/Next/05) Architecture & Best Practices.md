# 🏗️ 5. Architecture & Best Practices (Q38–48)

---

## 📍 Navigation

<div align="center">

[← Previous: Performance & Optimization](04%29%20Performance%20%26%20Optimization.md) • [Home: README](../README.md) • [Next: Deployment & Tooling →](06%29%20Deployment%20%26%20Tooling.md)

[📋 Cheatsheet](Next.js%20Interview%20Cheatsheet.md)

</div>

---

---

## Q38. ▲ ▲ ▲ Structuring a scalable Next.js project

Organize with `app/` directory for modern Next.js structure, co-located components (keep related files together), and proper separation of concerns (UI, logic, data) - structure for growth and maintenance. Use route groups `(group)` for organization without URL impact.

- **Trade-offs**: The catch is co-location keeps related files together and makes code easier to find, but watch out - structure for growth and maintenance, and use route groups to organize without affecting URLs, which helps with large projects.

Example:

```javascript
// Project structure
// app/
//   ├── (auth)/
//   │   ├── login/page.js
//   │   └── register/page.js
//   ├── dashboard/
//   │   └── page.js
//   └── components/

```

---

## Q39. 🔐 Implementing authentication in Next.js

Use NextAuth.js (popular authentication library) for authentication with support for multiple providers, middleware for route protection at the edge, and secure cookies for session storage - use stateless authentication tokens (JWT) for scalability.

- **Trade-offs**: The catch is NextAuth.js supports multiple authentication providers and provides secure session storage with cookies, but watch out - protect routes at the edge with middleware for better performance, and use JWT for stateless authentication when needed.

Example:

```javascript
import NextAuth from 'next-auth';
import CredentialsProvider from 'next-auth/providers/credentials';

export const authOptions = {
  providers: [
    CredentialsProvider({
      credentials: {
        email: { type: 'email' },
        password: { type: 'password' }
      },
      async authorize(credentials) {
        // Verify credentials
        return { id: '1', email: credentials.email };
      }
    })
  ]
};

export default NextAuth(authOptions);

```

---

## Q40. 📦 Handling global state management

Use Context for simple, rarely changing state, Zustand (lightweight state management library) for complex client state, and React Query for server state management - choose based on state complexity and needs. Consider SSR/hydration issues when using client-side state.

- **Trade-offs**: The catch is different tools for different use cases (Context for simple state, Zustand for complex state, React Query for server state), but watch out - consider SSR/hydration issues, and choose based on complexity and performance needs.

Example:

```javascript
'use client';
import { createContext, useContext, useState } from 'react';

const ThemeContext = createContext();

export function ThemeProvider({ children }) {
  const [theme, setTheme] = useState('light');
  return (
    <ThemeContext.Provider value={{ theme, setTheme }}>
      {children}
    </ThemeContext.Provider>
  );
}

```

---

## Q41. 💡 Implementing error handling and error boundaries

Use `error.tsx` for route-level error handling (must be client components) and error boundaries for component-level errors - provide ways to recover from errors with reset functions, and log errors for debugging. You can have different error handling per route with nested error files.

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

Use Server Components for data fetching (avoid side effects), client components for user interactions, and hooks (useEffect, etc.) for side effects in client components - handle side effects appropriately based on context. Server Components run on server, so no browser APIs or side effects.

- **Trade-offs**: The catch is avoid side effects in Server Components since they run on the server, but watch out - use hooks for side effects in client components, and handle side effects appropriately based on context (server vs client).

Example:

```javascript
// Server Component - data fetching
async function ServerComponent() {
  const data = await fetch('https://api.example.com/data');
  return <div>{data}</div>;
}

// Client Component - user interactions
'use client';
function ClientComponent() {
  useEffect(() => {
    // Side effect
  }, []);
  return <button>Click me</button>;
}

```

---

## Q43. 💡 Implementing role-based access control

Use middleware as the first line of defense to check authentication and roles before allowing access to routes, and add additional protection in components (client-side) - redirect unauthorized users to login, and protect API routes as well. Check user roles for access control.

- **Trade-offs**: The catch is middleware provides route protection at the edge and redirects unauthorized users, but watch out - add additional protection in components for client-side checks, and always protect API routes as well since client-side checks can be bypassed.

Example:

```javascript
import { withAuth } from 'next-auth/middleware';

export default withAuth(
  function middleware(req) {
    const { pathname } = req.nextUrl;
    const token = req.nextauth.token;

    if (pathname.startsWith('/admin') && token?.role !== 'admin') {
      return Response.redirect(new URL('/unauthorized', req.url));
    }
  }
);

export const config = {
  matcher: ['/admin/:path*']
};

```

---

## Q44. 🕸️ Integrating GraphQL with Next.js

Use GraphQL in Server Components for initial data fetching, and in client components for mutations and real-time updates - GraphQL integrates well with Next.js. Use Apollo (popular GraphQL client with Next.js support) or URQL (lightweight alternative), and GraphQL clients provide sophisticated caching.

- **Trade-offs**: The catch is GraphQL integrates well with Next.js, and GraphQL clients provide sophisticated caching, but watch out - use Server Components for initial data fetching, and client components for mutations and real-time updates, since they need interactivity.

Example:

```javascript
import { getClient } from '@apollo/experimental-nextjs-app-support/ssr';
import { gql } from '@apollo/client';

const GET_POSTS = gql`
  query GetPosts {
    posts {
      id
      title
    }
  }
`;

async function ServerComponent() {
  const client = getClient();
  const { data } = await client.query({ query: GET_POSTS });
  return <PostsList posts={data.posts} />;
}

```

---

## Q45. 🖥️ Securing API routes and Server Actions

Always validate user sessions for authentication, implement CSRF protection to prevent cross-site request forgery, validate and sanitize all inputs, use security headers for protection, and implement rate limiting for API routes - security is critical for production apps.

- **Trade-offs**: The catch is use security headers for protection and implement rate limiting to prevent abuse, but watch out - always validate and sanitize all inputs, and never trust client-side data, since it can be manipulated.

Example:

```javascript
import { getServerSession } from 'next-auth';
import { authOptions } from '../auth';

export async function GET(request) {
  const session = await getServerSession(authOptions);
  if (!session) {
    return Response.json({ error: 'Unauthorized' }, { status: 401 });
  }
  return Response.json({ data: 'Protected data' });
}

```

---

## Q46. ⚙️ Implementing middleware vs edge functions

Middleware runs on every request (good for global logic like auth/redirects), while edge functions run on specific routes (good for API endpoints) - edge functions run closer to users for better performance, but have limited APIs. Choose based on use case.

- **Trade-offs**: The catch is edge functions run closer to users for better performance, but have limited APIs, but watch out - use middleware for auth/redirects and global logic, and edge functions for specific API endpoints that need low latency.

Example:

```javascript
import { NextResponse } from 'next/server';

export function middleware(request) {
  const { pathname } = request.nextUrl;
  if (pathname.startsWith('/admin')) {
    return NextResponse.redirect(new URL('/login', request.url));
  }
  return NextResponse.next();
}

export const config = {
  matcher: '/admin/:path*'
};

```

---

## Q47. 🎨 Implementing hybrid rendering strategies

Use different rendering strategies for different parts of the application - SSR for dynamic, user-specific content, ISR for content that changes occasionally, and CSR for interactive, client-side features. Use Suspense for progressive loading, and combine strategies for optimal performance.

- **Trade-offs**: The catch is choose rendering strategy per component based on data requirements, and use Suspense for progressive loading, but watch out - combine strategies for optimal performance, since different parts of your app have different needs.

Example:

```javascript
export default function HybridPage() {
  return (
    <div>
      {/* Static content - SSG */}
      <header>
        <h1>Static Header</h1>
      </header>

      {/* Dynamic content - SSR */}
      <ServerComponent />

      {/* Interactive content - CSR */}
      <ClientComponent />
    </div>
  );
}

```

---

## Q48. ▲ ▲ ▲ Common Next.js anti-patterns to avoid

Avoid mixing Pages and App Router, overusing client components (use Server Components when possible), blocking SSR calls (use streaming with Suspense), and not using proper caching strategies - follow Next.js best practices for optimal performance.

- **Trade-offs**: The catch is follow Next.js best practices for optimal performance, and use Server Components when possible to reduce client-side JS, but watch out - avoid these anti-patterns, as these can significantly impact performance and user experience.

Example:

```javascript
// ❌ Anti-pattern: Overusing client components
'use client';
export default function Page() {
  const [data, setData] = useState(null);
  useEffect(() => {
    fetch('/api/data').then(r => r.json()).then(setData);
  }, []);
  return <div>{data}</div>;
}

// ✅ Better: Use Server Component
async function Page() {
  const data = await fetch('https://api.example.com/data');
  return <div>{data}</div>;
}

```

---

---

## 📍 Navigation

<div align="center">

[← Previous: Performance & Optimization](04%29%20Performance%20%26%20Optimization.md) • [Home: README](../README.md) • [Next: Deployment & Tooling →](06%29%20Deployment%20%26%20Tooling.md)

[📋 Cheatsheet](Next.js%20Interview%20Cheatsheet.md)

</div>

---
