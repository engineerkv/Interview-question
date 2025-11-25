# 3. Routing & Navigation (Q21–27)

---

## Q21. Nested routing in App Router

Nested routes create layouts that wrap child pages, with `layout.js` files defining shared UI - layouts compose together for complex UIs (composition). Each folder can have its own layout (nested layouts).

- **Trade-offs**: The catch is common elements like navigation stay in place (shared UI) - layouts don't re-render on navigation. Layouts compose together for complex UIs (composition), but watch out - layouts persist across route changes (layout persistence).

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

<div align="center">

**[← Previous: Data Fetching & Rendering](2%29%20Data%20Fetching%20%26%20Rendering.md)** | **[Next: Performance & Optimization →](4%29%20Performance%20%26%20Optimization.md)**

</div>

---

## Q22. Parallel Routes and how to use them

Parallel routes render multiple pages simultaneously, while intercepting routes show pages in modals - parallel routes enable complex dashboard layouts. Parallel routes render multiple pages in same layout, intercepting routes show pages in modals or overlays.

- **Trade-offs**: The catch is great for modal dialogs and overlays (modals) - better user experience with parallel content (UX). Parallel routes enable complex dashboard layouts, but watch out - use `@` prefix for parallel route slots.

Example:

```javascript
// Parallel Routes
// app/dashboard/@analytics/page.js
export default function Analytics() {
  return <div>Analytics Panel</div>;
}
```

---

## Q23. Intercepting Routes and how to use them

Intercepting routes show pages in modals or overlays without changing the URL - great for modal dialogs and overlays (modals). Use `(.)` prefix for same-level intercepting, `(..)` for parent level.

- **Trade-offs**: The catch is URL doesn't change, better UX - works with parallel routes for complex layouts. Intercepting routes provide better UX for modals, but watch out - shows content in modal without navigation.

Example:

```javascript
// Intercepting route
// app/(.)photos/[id]/page.js
export default function PhotoModal({ params }) {
  return <div>Photo {params.id}</div>;
}
```

---

## Q24. Handling `not-found.tsx` and `error.tsx`

These files handle 404 errors, runtime errors, and loading states respectively in the App Router - these files improve error handling and loading states. `not-found.tsx` handles 404 errors and missing pages, `error.tsx` handles runtime errors and exceptions, `loading.tsx` shows loading states during navigation.

- **Trade-offs**: The catch is error boundaries must be client components - these special files provide better UX. These files improve error handling and loading states, but watch out - can have different error/loading states per route (nested).

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

## Q25. Using `loading.tsx` for loading states

`loading.tsx` shows loading states during navigation automatically - provides better UX during route transitions. Automatically shows during route transitions.

- **Trade-offs**: The catch is works with Suspense for progressive loading - provides better perceived performance. Loading states improve perceived performance, but watch out - can have different loading states per route (nested).

Example:

```javascript
// app/loading.tsx
export default function Loading() {
  return <div>Loading...</div>;
}
```

---

## Q26. Using `useRouter()` and `router.push()`

Use `useRouter()` to get the router object and call `push()` to navigate programmatically - use router for client-side navigation. `useRouter` hook for programmatic navigation.

- **Trade-offs**: The catch is `back()/forward()` navigate through history, `refresh()` reloads current page - router provides navigation control. Use router for client-side navigation, but watch out - `push()` navigates to new page, adds to history; `replace()` navigates without adding to history.

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

## Q27. Implementing redirects and rewrites

Configure redirects, rewrites, and headers in the `next.config.js` file for routing and security - these configs affect routing and security. Redirects (permanent (301) or temporary (302) redirects), Rewrites (internal URL rewriting without changing browser URL), Headers (security headers and CORS configuration).

- **Trade-offs**: The catch is important for security and SEO - configure complex routing and security rules. These configs affect routing and security, but watch out - use path patterns for flexible matching.

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

<div align="center">

**[← Previous: Data Fetching & Rendering](2%29%20Data%20Fetching%20%26%20Rendering.md)** | **[Next: Performance & Optimization →](4%29%20Performance%20%26%20Optimization.md)**

</div>
