# 🧭 3. Routing & Navigation (Q21–33)

---

## 📍 Navigation

<div align="center">

[← Previous: Data Fetching & Rendering](02%29%20Data%20Fetching%20%26%20Rendering.md) • [Home: README](../README.md) • [Next: Performance & Optimization →](04%29%20Performance%20%26%20Optimization.md)

[📋 Cheatsheet](Next.js%20Interview%20Cheatsheet.md)

</div>

---

---

## Q21. 🗺️ Nested routing in App Router

Nested routes create layouts that wrap child pages, with `layout.js` files defining shared UI - each folder can have its own layout, and layouts compose together for complex UIs. Common elements like navigation stay in place, and layouts don't re-render on navigation.

- **Trade-offs**: The catch is layouts persist across route changes, which provides better UX, but watch out - layouts compose together, so make sure your layout structure makes sense and doesn't create unnecessary nesting.

Example:

```javascript
// app/layout.js - root layout
export default function RootLayout({ children }) {
  return (
    <html>
      <body>
        <header>My App</header>
        {children}
      </body>
    </html>
  );
}

```

---

## Q22. 💡 Parallel Routes and how to use them

Parallel routes render multiple pages simultaneously in the same layout using the `@` prefix for route slots - great for complex dashboard layouts where you need multiple panels. Intercepting routes show pages in modals or overlays without changing the URL.

- **Trade-offs**: The catch is parallel routes enable complex dashboard layouts and provide better UX with parallel content, but watch out - use the `@` prefix for parallel route slots, and make sure your layout can handle multiple parallel routes.

Example:

```javascript
// Parallel Routes
// app/dashboard/@analytics/page.js
export default function Analytics() {
  return <div>Analytics Panel</div>;
}

```

---

## Q23. 💡 Intercepting Routes and how to use them

Intercepting routes show pages in modals or overlays without changing the URL - great for modal dialogs and overlays. Use `(.)` prefix for same-level intercepting, `(..)` for parent level, and it works with parallel routes for complex layouts.

- **Trade-offs**: The catch is the URL doesn't change, which provides better UX for modals, but watch out - shows content in modal without navigation, so users might be confused about the current route if not handled properly.

Example:

```javascript
// Intercepting route
// app/(.)photos/[id]/page.js
export default function PhotoModal({ params }) {
  return <div>Photo {params.id}</div>;
}

```

---

## Q24. 💡 Handling `not-found.tsx` and `error.tsx`

`not-found.tsx` handles 404 errors and missing pages, `error.tsx` handles runtime errors and exceptions (must be client components), and `loading.tsx` shows loading states during navigation - these special files improve error handling and UX. You can have different error/loading states per route with nested files.

- **Trade-offs**: The catch is error boundaries must be client components, and these files provide better UX, but watch out - you can have different error/loading states per route, which is powerful but can be confusing if overused.

Example:

```javascript
// app/not-found.tsx - 404 page
export default function NotFound() {
  return (
    <div>
      <h1>404 - Page Not Found</h1>
      <p>The page you're looking for doesn't exist.</p>
    </div>
  );
}

// app/error.tsx - error boundary
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

## Q25. 📦 Using `loading.tsx` for loading states

`loading.tsx` shows loading states during navigation automatically - provides better UX during route transitions and works with Suspense for progressive loading. Automatically shows during route transitions, and you can have different loading states per route.

- **Trade-offs**: The catch is loading states improve perceived performance and work with Suspense for progressive loading, but watch out - can have different loading states per route, which is useful but can be inconsistent if not managed well.

Example:

```javascript
// app/loading.tsx
export default function Loading() {
  return <div>Loading...</div>;
}

```

---

## Q26. 💡 Using `useRouter()` and `router.push()`

Use `useRouter()` to get the router object and call `push()` to navigate programmatically - `push()` navigates to a new page and adds to history, while `replace()` navigates without adding to history. `back()/forward()` navigate through history, and `refresh()` reloads the current page.

- **Trade-offs**: The catch is router provides navigation control for client-side navigation, but watch out - `push()` adds to history (users can go back), while `replace()` doesn't (useful for redirects or when you don't want back navigation).

Example:

```javascript
'use client';
import { useRouter } from 'next/navigation';

export default function Navigation() {
  const router = useRouter();

  return (
    <button onClick={() => router.push('/about')}>
      Go to About
    </button>
  );
}

```

---

## Q27. 💡 Implementing redirects and rewrites

Configure redirects (permanent 301 or temporary 302), rewrites (internal URL rewriting without changing browser URL), and headers (security headers and CORS) in `next.config.js` - important for security, SEO, and routing. Use path patterns for flexible matching.

- **Trade-offs**: The catch is these configs affect routing and security, and you can configure complex routing and security rules, but watch out - use path patterns for flexible matching, and test thoroughly since misconfigured redirects can break your app.

Example:

```javascript
// next.config.js
const nextConfig = {
  async redirects() {
    return [
      { source: '/old', destination: '/new', permanent: true }
    ];
  },
  async rewrites() {
    return [
      { source: '/api/:path*', destination: '/api-proxy/:path*' }
    ];
  },
  async headers() {
    return [
      {
        source: '/:path*',
        headers: [
          { key: 'X-Frame-Options', value: 'DENY' }
        ]
      }
    ];
  }
};

```

---

## Q28. 🔧 What is Next.js middleware and how does it work

Middleware runs before a request is completed, allowing you to modify the request/response, redirect, rewrite URLs, or add headers - runs on the Edge Runtime for better performance and executes before rendering. Use it for authentication, logging, A/B testing, or request modification.

- **Trade-offs**: The catch is middleware runs on Edge Runtime for better performance and executes before rendering, but watch out - middleware runs on every matching request, so keep it lightweight and avoid heavy computations, and it has limited APIs compared to Node.js runtime.

Example:

```javascript
// middleware.js (root of project)
import { NextResponse } from 'next/server';
import type { NextRequest } from 'next/server';

export function middleware(request: NextRequest) {
  // Modify request
  const requestHeaders = new Headers(request.headers);
  requestHeaders.set('x-pathname', request.nextUrl.pathname);
  
  return NextResponse.next({
    request: {
      headers: requestHeaders,
    },
  });
}

export const config = {
  matcher: '/:path*',
};

```

---

## Q29. 🔧 Using middleware for authentication and route protection

Middleware intercepts requests before rendering, allowing you to check authentication tokens/cookies and redirect unauthorized users - runs on Edge Runtime for fast authentication checks. Use `NextResponse.redirect()` to send users to login, and check tokens/cookies from request headers.

- **Trade-offs**: The catch is middleware provides fast authentication checks at the edge before rendering, but watch out - always validate tokens properly and don't trust client-side data, and combine with server-side checks for sensitive routes since middleware can be bypassed if misconfigured.

Example:

```javascript
// middleware.js
import { NextResponse } from 'next/server';
import type { NextRequest } from 'next/server';

export function middleware(request: NextRequest) {
  const token = request.cookies.get('auth-token')?.value;
  const { pathname } = request.nextUrl;
  
  // Protect admin routes
  if (pathname.startsWith('/admin') && !token) {
    return NextResponse.redirect(new URL('/login', request.url));
  }
  
  // Redirect authenticated users away from login
  if (pathname === '/login' && token) {
    return NextResponse.redirect(new URL('/dashboard', request.url));
  }
  
  return NextResponse.next();
}

export const config = {
  matcher: ['/admin/:path*', '/login', '/dashboard/:path*'],
};

```

---

## Q30. 🔧 Middleware matcher configuration and path matching

The `matcher` config controls which routes middleware runs on - use path patterns, regex, or arrays to match specific routes. Matcher runs before middleware executes, improving performance by skipping unnecessary middleware execution. Use negative lookahead to exclude paths.

- **Trade-offs**: The catch is matcher improves performance by only running middleware on matching routes, but watch out - use specific matchers to avoid running middleware on every request (like static files), and test your matcher patterns thoroughly since incorrect patterns can break routing.

Example:

```javascript
// middleware.js
import { NextResponse } from 'next/server';
import type { NextRequest } from 'next/server';

export function middleware(request: NextRequest) {
  // Your middleware logic
  return NextResponse.next();
}

export const config = {
  // Match specific paths
  matcher: '/about/:path*',
  
  // Or use array for multiple paths
  // matcher: ['/admin/:path*', '/dashboard/:path*'],
  
  // Or use regex for complex patterns
  // matcher: [
  //   '/((?!api|_next/static|_next/image|favicon.ico).*)',
  // ],
};

```

---

## Q31. 🔧 Modifying request and response in middleware

Middleware can modify request headers, add custom headers to response, rewrite URLs internally, or redirect requests - use `NextResponse.next()` to continue, `NextResponse.rewrite()` for internal URL changes, or `NextResponse.redirect()` for external redirects. Headers can be read from request and set on response.

- **Trade-offs**: The catch is middleware provides powerful request/response manipulation before rendering, but watch out - URL rewrites are internal (browser URL doesn't change), while redirects change the browser URL, and modifying headers can affect caching and security, so be careful with security headers.

Example:

```javascript
// middleware.js
import { NextResponse } from 'next/server';
import type { NextRequest } from 'next/server';

export function middleware(request: NextRequest) {
  const { pathname } = request.nextUrl;
  
  // Add custom header to request
  const requestHeaders = new Headers(request.headers);
  requestHeaders.set('x-custom-header', 'value');
  
  // Rewrite URL internally (browser URL stays same)
  if (pathname === '/old-path') {
    return NextResponse.rewrite(new URL('/new-path', request.url));
  }
  
  // Add response headers
  const response = NextResponse.next({
    request: { headers: requestHeaders },
  });
  response.headers.set('x-response-header', 'value');
  
  return response;
}

export const config = {
  matcher: '/:path*',
};

```

---

## Q32. 🔧 Using middleware for A/B testing and feature flags

Middleware can check cookies/headers to determine user segments and rewrite URLs or add headers for A/B testing - runs before rendering so you can serve different content based on user segment. Use cookies to persist user's variant, and rewrite URLs to serve different page versions.

- **Trade-offs**: The catch is middleware enables server-side A/B testing before rendering, which is faster than client-side, but watch out - persist user's variant in cookies to maintain consistency, and make sure your A/B test logic doesn't slow down requests since middleware runs on every matching request.

Example:

```javascript
// middleware.js
import { NextResponse } from 'next/server';
import type { NextRequest } from 'next/server';

export function middleware(request: NextRequest) {
  const { pathname } = request.nextUrl;
  const variant = request.cookies.get('ab-variant')?.value || 
    (Math.random() > 0.5 ? 'a' : 'b');
  
  // Set variant cookie if not exists
  const response = NextResponse.next();
  if (!request.cookies.get('ab-variant')) {
    response.cookies.set('ab-variant', variant, { maxAge: 60 * 60 * 24 * 30 });
  }
  
  // Rewrite to variant-specific page
  if (pathname === '/home' && variant === 'b') {
    return NextResponse.rewrite(new URL('/home-variant-b', request.url));
  }
  
  return response;
}

export const config = {
  matcher: '/home',
};

```

---

## Q33. 🔧 Middleware Edge Runtime limitations and best practices

Middleware runs on Edge Runtime (V8 isolates) which has limited APIs compared to Node.js - no Node.js APIs, limited async operations, and smaller bundle size requirements. Use for lightweight operations like auth checks, redirects, and header manipulation. Avoid heavy computations, file system access, or Node.js-specific APIs.

- **Trade-offs**: The catch is Edge Runtime provides better performance and runs closer to users, but watch out - limited APIs mean you can't use Node.js modules, file system, or heavy computations, so keep middleware lightweight and move complex logic to API routes or server components.

Example:

```javascript
// middleware.js
import { NextResponse } from 'next/server';
import type { NextRequest } from 'next/server';

export function middleware(request: NextRequest) {
  // ✅ Good: Lightweight operations
  const token = request.cookies.get('token')?.value;
  const pathname = request.nextUrl.pathname;
  
  // ✅ Good: Simple redirects
  if (!token && pathname.startsWith('/protected')) {
    return NextResponse.redirect(new URL('/login', request.url));
  }
  
  // ❌ Bad: Can't use Node.js APIs
  // const fs = require('fs'); // Won't work
  // const crypto = require('crypto'); // Use Web Crypto API instead
  
  return NextResponse.next();
}

export const config = {
  matcher: '/:path*',
};

// Edge Runtime is default, but you can specify explicitly
export const runtime = 'edge';

```

---

---

## 📍 Navigation

<div align="center">

[← Previous: Data Fetching & Rendering](02%29%20Data%20Fetching%20%26%20Rendering.md) • [Home: README](../README.md) • [Next: Performance & Optimization →](04%29%20Performance%20%26%20Optimization.md)

[📋 Cheatsheet](Next.js%20Interview%20Cheatsheet.md)

</div>

---
