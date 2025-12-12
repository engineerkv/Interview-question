# 🧭 3. Routing & Navigation (Q21–27)

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
// app/layout.js - root layout (wraps all pages)
export default function RootLayout({ children }) {
  return (
    <html>
      <body>
        <header>My App</header> {/* Shared header across all pages */}
        {children} {/* Child pages render here, layout persists on navigation */}
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

## 📍 Navigation

<div align="center">

[← Previous: Data Fetching & Rendering](02%29%20Data%20Fetching%20%26%20Rendering.md) • [Home: README](../README.md) • [Next: Performance & Optimization →](04%29%20Performance%20%26%20Optimization.md)

[📋 Cheatsheet](Next.js%20Interview%20Cheatsheet.md)

</div>

---

