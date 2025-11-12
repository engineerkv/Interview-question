# 🧠 5. Architecture & Best Practices (Q38–48)

---

## 🧩 Q38. How do you structure a scalable Next.js project?

### 🧠 Concept

Organize with `app/` directory, co-located components, and proper separation of concerns. Structure for growth and maintenance (scalability).

---

### 💡 Example

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

### 🔍 Deep Insights

* **Rule:** Use `app/` for modern Next.js structure (app directory).
* **Use Case:** Use `(group)` for organization without URL impact (route groups).
* **Common Mistake:** Keep related files together (co-location).
* **Pro Tip:** Separate concerns (UI, logic, data).

---

### ⭐ Senior Takeaway

Structure for growth and maintenance (scalability).

---

## 🧩 Q39. How do you implement authentication in Next.js?

### 🧠 Concept

Use NextAuth.js for authentication, middleware for protection, and secure cookies for sessions. Support for multiple authentication providers.

---

### 💡 Example

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

### 🔍 Deep Insights

* **Rule:** NextAuth.js is popular authentication library for Next.js.
* **Use Case:** Protect routes at the edge (middleware).
* **Common Mistake:** Stateless authentication tokens (JWT).
* **Pro Tip:** Secure session storage (cookies).

---

### ⭐ Senior Takeaway

Support for multiple authentication providers.

---

## 🧩 Q40. How do you handle global state management?

### 🧠 Concept

Use Context for simple state, Zustand for complex state, and React Query for server state. Choose based on state complexity.

---

### 💡 Example

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

### 🔍 Deep Insights

* **Rule:** Context (good for simple, rarely changing state), Zustand (lightweight state management library), React Query (excellent for server state management).
* **Use Case:** Choose based on complexity and needs (performance).
* **Common Mistake:** Consider SSR/hydration issues (hydration).
* **Pro Tip:** Different tools for different use cases.

---

### ⭐ Senior Takeaway

Choose based on state complexity.

---

## 🧩 Q41. How do you implement error handling and error boundaries?

### 🧠 Concept

Use `error.tsx` for route-level errors and error boundaries for component errors. Log errors for debugging.

---

### 💡 Example

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

### 🔍 Deep Insights

* **Rule:** `error.tsx` handles route-level error handling.
* **Use Case:** Different error handling per route (nested errors).
* **Common Mistake:** Component-level error handling (error boundaries).
* **Pro Tip:** Provide ways to recover from errors (recovery).

---

### ⭐ Senior Takeaway

Log errors for debugging.

---

## 🧩 Q42. How do you handle side effects in Next.js?

### 🧠 Concept

Use Server Components for data fetching, client components for user interactions, and hooks for side effects. Handle side effects appropriately based on context.

---

### 💡 Example

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

### 🔍 Deep Insights

* **Rule:** Server Components for data fetching, client components for interactions.
* **Use Case:** Use hooks for side effects in client components.
* **Common Mistake:** Avoid side effects in Server Components.
* **Pro Tip:** Handle side effects appropriately based on context.

---

### ⭐ Senior Takeaway

Handle side effects appropriately based on context.

---

## 🧩 Q43. How do you implement role-based access control?

### 🧠 Concept

Use middleware to check authentication and roles before allowing access to routes. Additional protection in components (client-side).

---

### 💡 Example

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

### 🔍 Deep Insights

* **Rule:** First line of defense for route protection (middleware).
* **Use Case:** Check user roles for access control (role-based).
* **Common Mistake:** Redirect unauthorized users to login (redirects).
* **Pro Tip:** Protect API routes as well.

---

### ⭐ Senior Takeaway

Additional protection in components (client-side).

---

## 🧩 Q44. How do you integrate GraphQL with Next.js?

### 🧠 Concept

Use GraphQL in Server Components for initial data and client components for mutations. GraphQL integrates well with Next.js.

---

### 💡 Example

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

### 🔍 Deep Insights

* **Rule:** Server components use for initial data fetching.
* **Use Case:** Client components use for mutations and real-time updates.
* **Common Mistake:** Apollo (popular GraphQL client with Next.js support), URQL (lightweight alternative to Apollo).
* **Pro Tip:** GraphQL clients provide sophisticated caching.

---

### ⭐ Senior Takeaway

GraphQL integrates well with Next.js.

---

## 🧩 Q45. How do you secure API routes and Server Actions?

### 🧠 Concept

Implement CSRF protection, validate authentication, and sanitize inputs. Use security headers for protection.

---

### 💡 Example

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

### 🔍 Deep Insights

* **Rule:** Always validate user sessions (authentication).
* **Use Case:** Validate and sanitize all inputs (input validation).
* **Common Mistake:** Prevent cross-site request forgery (CSRF protection).
* **Pro Tip:** Implement rate limiting for API routes.

---

### ⭐ Senior Takeaway

Use security headers for protection.

---

## 🧩 Q46. How do you implement middleware vs edge functions?

### 🧠 Concept

Middleware runs on every request, while edge functions run on specific routes. Choose based on use case.

---

### 💡 Example

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

### 🔍 Deep Insights

* **Rule:** Middleware runs on every request, good for global logic; Edge functions run on specific routes, good for API endpoints.
* **Use Case:** Edge functions run closer to users (performance).
* **Common Mistake:** Edge functions have limited APIs.
* **Pro Tip:** Middleware for auth/redirects, Edge for APIs.

---

### ⭐ Senior Takeaway

Choose based on use case.

---

## 🧩 Q47. How do you implement hybrid rendering strategies?

### 🧠 Concept

Use different rendering strategies for different parts of the application based on data requirements. Choose rendering strategy per component.

---

### 💡 Example

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

### 🔍 Deep Insights

* **Rule:** SSR (for dynamic, user-specific content), ISR (for content that changes occasionally), CSR (for interactive, client-side features).
* **Use Case:** Combine strategies for optimal performance (hybrid).
* **Common Mistake:** Use Suspense for progressive loading.
* **Pro Tip:** Different strategies for different components.

---

### ⭐ Senior Takeaway

Choose rendering strategy per component.

---

## 🧩 Q48. What are common Next.js anti-patterns to avoid?

### 🧠 Concept

Avoid mixing Pages and App Router, overusing client components, and blocking SSR calls. Follow Next.js best practices for optimal performance.

---

### 💡 Example

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

### 🔍 Deep Insights

* **Rule:** Avoid mixing Pages and App Router, overusing client components, blocking SSR calls.
* **Use Case:** Use Server Components when possible (reduce client-side JS).
* **Common Mistake:** Not using proper caching strategies.
* **Pro Tip:** Follow Next.js best practices for optimal performance.

---

### ⭐ Senior Takeaway

Follow Next.js best practices for optimal performance.

---
