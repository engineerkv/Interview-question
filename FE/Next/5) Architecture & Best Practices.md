<div align="center">

**[← Previous: Performance & Optimization](4%29%20Performance%20%26%20Optimization.md)** | **[Next: Deployment & Tooling →](6%29%20Deployment%20%26%20Tooling.md)**

</div>

# 🏗️ 5. Architecture & Best Practices (Q38–48)

---

## Q38. 💡 Structuring a scalable Next.js project

Organize with `app/` directory, co-located components, and proper separation of concerns - structure for growth and maintenance (scalability). Use `app/` for modern Next.js structure (app directory).

- **Trade-offs**: The catch is keep related files together (co-location) - separate concerns (UI, logic, data). Structure for growth and maintenance (scalability), but watch out - use `(group)` for organization without URL impact (route groups).

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

Use NextAuth.js for authentication, middleware for protection, and secure cookies for sessions - support for multiple authentication providers. NextAuth.js is popular authentication library for Next.js.

- **Trade-offs**: The catch is stateless authentication tokens (JWT) - secure session storage (cookies). Support for multiple authentication providers, but watch out - protect routes at the edge (middleware).

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

## Q40. 📊 Handling global state management

Use Context for simple state, Zustand for complex state, and React Query for server state - choose based on state complexity. Context (good for simple, rarely changing state), Zustand (lightweight state management library), React Query (excellent for server state management).

- **Trade-offs**: The catch is consider SSR/hydration issues (hydration) - different tools for different use cases. Choose based on state complexity, but watch out - choose based on complexity and needs (performance).

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

## Q41. ⚠️ Implementing error handling and error boundaries

Use `error.tsx` for route-level errors and error boundaries for component errors - log errors for debugging. `error.tsx` handles route-level error handling.

- **Trade-offs**: The catch is component-level error handling (error boundaries) - provide ways to recover from errors (recovery). Log errors for debugging, but watch out - different error handling per route (nested errors).

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

## Q42. 💡 Handling side effects in Next.js

Use Server Components for data fetching, client components for user interactions, and hooks for side effects - handle side effects appropriately based on context. Server Components for data fetching, client components for interactions.

- **Trade-offs**: The catch is avoid side effects in Server Components - handle side effects appropriately based on context. Handle side effects appropriately based on context, but watch out - use hooks for side effects in client components.

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

## Q43. 🔧 Implementing role-based access control

Use middleware to check authentication and roles before allowing access to routes - additional protection in components (client-side). First line of defense for route protection (middleware).

- **Trade-offs**: The catch is redirect unauthorized users to login (redirects) - protect API routes as well. Additional protection in components (client-side), but watch out - check user roles for access control (role-based).

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

## Q44. 🔀 Integrating GraphQL with Next.js

Use GraphQL in Server Components for initial data and client components for mutations - GraphQL integrates well with Next.js. Server components use for initial data fetching.

- **Trade-offs**: The catch is Apollo (popular GraphQL client with Next.js support), URQL (lightweight alternative to Apollo) - GraphQL clients provide sophisticated caching. GraphQL integrates well with Next.js, but watch out - client components use for mutations and real-time updates.

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

## Q45. 🔌 Securing API routes and Server Actions

Implement CSRF protection, validate authentication, and sanitize inputs - use security headers for protection. Always validate user sessions (authentication).

- **Trade-offs**: The catch is prevent cross-site request forgery (CSRF protection) - implement rate limiting for API routes. Use security headers for protection, but watch out - validate and sanitize all inputs (input validation).

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

## Q46. 🔧 Implementing middleware vs edge functions

Middleware runs on every request, while edge functions run on specific routes - choose based on use case. Middleware runs on every request, good for global logic; Edge functions run on specific routes, good for API endpoints.

- **Trade-offs**: The catch is edge functions have limited APIs - middleware for auth/redirects, Edge for APIs. Choose based on use case, but watch out - edge functions run closer to users (performance).

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

## Q47. 🔧 Implementing hybrid rendering strategies

Use different rendering strategies for different parts of the application based on data requirements - choose rendering strategy per component. SSR (for dynamic, user-specific content), ISR (for content that changes occasionally), CSR (for interactive, client-side features).

- **Trade-offs**: The catch is use Suspense for progressive loading - different strategies for different components. Choose rendering strategy per component, but watch out - combine strategies for optimal performance (hybrid).

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

## Q48. 🎯 Common Next.js anti-patterns to avoid

Avoid mixing Pages and App Router, overusing client components, and blocking SSR calls - follow Next.js best practices for optimal performance. Avoid mixing Pages and App Router, overusing client components, blocking SSR calls.

- **Trade-offs**: The catch is not using proper caching strategies - follow Next.js best practices for optimal performance. Follow Next.js best practices for optimal performance, but watch out - use Server Components when possible (reduce client-side JS).

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

<div align="center">

**[← Previous: Performance & Optimization](4%29%20Performance%20%26%20Optimization.md)** | **[Next: Deployment & Tooling →](6%29%20Deployment%20%26%20Tooling.md)**

</div>

