# 🧠 5. Architecture & Best Practices (Q38–48)

---

## 38) How do you structure a scalable Next.js App Router project (folders, modules, context)?

Organize with `app/` directory, co-located components, and proper separation of concerns.

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

- **Core Structure**: Use `app/` for modern Next.js structure (app directory)
- **Real-World Use**: Use `(group)` for organization without URL impact (route groups)
- **Common Practice**: Keep related files together (co-location)
- **Advanced Feature**: Separate concerns (UI, logic, data)
- **Interview Tip**: Explain that structure for growth and maintenance (scalability)

---

## 39) What are best practices for data fetching in server components (avoid N+1 requests)?

Fetch data at the layout level and pass down to avoid N+1 queries.

```javascript
// ❌ Anti-pattern: N+1 queries
export default async function PostsList() {
  const posts = await fetch('https://api.example.com/posts');
  const postsData = await posts.json();
  
  return (
    <div>
      {postsData.map(post => (
        <PostDetails key={post.id} postId={post.id} />
      ))}
    </div>
  );
}

// ✅ Better: Fetch all data at once
```

- **Core Problem**: Avoid fetching related data in loops (N+1 problem)
- **Real-World Solution**: Fetch all needed data at once (batch queries)
- **Common Practice**: Use database relationships efficiently (database joins)
- **Advanced Feature**: Cache frequently accessed data
- **Interview Tip**: Explain that reduces database round trips (performance)

---

## 40) How do you handle authentication (NextAuth.js, middleware, cookies, JWT)?

Use NextAuth.js for authentication, middleware for protection, and secure cookies for sessions.

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

- **Core Library**: NextAuth.js is popular authentication library for Next.js
- **Real-World Use**: Protect routes at the edge (middleware)
- **Common Practice**: Stateless authentication tokens (JWT)
- **Advanced Feature**: Secure session storage (cookies)
- **Interview Tip**: Explain that support for multiple authentication providers

---

## 41) How do you implement role-based access or route protection in middleware?

Use middleware to check authentication and roles before allowing access to routes.

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

- **Core Purpose**: First line of defense for route protection (middleware)
- **Real-World Use**: Check user roles for access control (role-based)
- **Common Practice**: Redirect unauthorized users to login (redirects)
- **Advanced Feature**: Protect API routes as well
- **Interview Tip**: Explain that additional protection in components (client-side)

---

## 42) What are recommended strategies for error handling (error boundaries, error.tsx)?

Use `error.tsx` for route-level errors and error boundaries for component errors.

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

- **Core File**: `error.tsx` handles route-level error handling
- **Real-World Use**: Different error handling per route (nested errors)
- **Common Practice**: Component-level error handling (error boundaries)
- **Advanced Feature**: Provide ways to recover from errors (recovery)
- **Interview Tip**: Explain that log errors for debugging

---

## 43) How do you handle global state in Next.js 14 (Context, Zustand, React Query)?

Use Context for simple state, Zustand for complex state, and React Query for server state.

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

- **Core Approaches**: Context (good for simple, rarely changing state), Zustand (lightweight state management library), React Query (excellent for server state management)
- **Real-World Use**: Choose based on complexity and needs (performance)
- **Common Consideration**: Consider SSR/hydration issues (hydration)
- **Advanced Feature**: Different tools for different use cases
- **Interview Tip**: Explain that choose based on state complexity

---

## 44) What is the difference between client-side and server-side state management in the App Router?

Server state is managed by Server Components, while client state uses hooks and context.

```javascript
// Server Component - server-side state
async function ServerComponent() {
  const posts = await fetch('https://api.example.com/posts');
  const data = await posts.json();
  return <PostsList posts={data} />;
}

// Client Component - client-side state
'use client';
function ClientComponent() {
  const [count, setCount] = useState(0);
  return <button onClick={() => setCount(count + 1)}>{count}</button>;
}
```

- **Core Difference**: Server state is fetched on server, no JavaScript needed; Client state is interactive state, requires JavaScript
- **Real-World Impact**: Server state is faster for initial load (performance)
- **Common Use**: Client state enables user interactions (interactivity)
- **Advanced Approach**: Combine both for optimal performance (hybrid)
- **Interview Tip**: Explain that use server state for data, client state for UI

---

## 45) How do you integrate GraphQL (Apollo, URQL) with server components vs client components?

Use GraphQL in Server Components for initial data and client components for mutations.

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

- **Core Use**: Server components use for initial data fetching
- **Real-World Use**: Client components use for mutations and real-time updates
- **Common Libraries**: Apollo (popular GraphQL client with Next.js support), URQL (lightweight alternative to Apollo)
- **Advanced Feature**: GraphQL clients provide sophisticated caching
- **Interview Tip**: Explain that GraphQL integrates well with Next.js

---

## 46) How do you secure API routes and server actions (CSRF, auth headers, cookies)?

Implement CSRF protection, validate authentication, and sanitize inputs.

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

- **Core Security**: Always validate user sessions (authentication)
- **Real-World Practice**: Validate and sanitize all inputs (input validation)
- **Common Protection**: Prevent cross-site request forgery (CSRF protection)
- **Advanced Feature**: Implement rate limiting for API routes
- **Interview Tip**: Explain that use security headers for protection

---

## 47) What is the difference between middleware vs edge functions in terms of lifecycle?

Middleware runs on every request, while edge functions run on specific routes.

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

- **Core Difference**: Middleware runs on every request, good for global logic; Edge functions run on specific routes, good for API endpoints
- **Real-World Use**: Edge functions run closer to users (performance)
- **Common Limitation**: Edge functions have limited APIs
- **Advanced Use Cases**: Middleware for auth/redirects, Edge for APIs
- **Interview Tip**: Explain that choose based on use case

---

## 48) How can you combine SSR + ISR + CSR in hybrid rendering strategies?

Use different rendering strategies for different parts of the application based on data requirements.

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

- **Core Strategies**: SSR (for dynamic, user-specific content), ISR (for content that changes occasionally), CSR (for interactive, client-side features)
- **Real-World Approach**: Combine strategies for optimal performance (hybrid)
- **Common Pattern**: Use Suspense for progressive loading
- **Advanced Feature**: Different strategies for different components
- **Interview Tip**: Explain that choose rendering strategy per component

---
