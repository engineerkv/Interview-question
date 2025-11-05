# 🧭 3. Routing & Navigation (Q21–27)

---

## 21) How does nested routing and layout composition work in the App Router? (**🚀 Next 14**)

Nested routes create layouts that wrap child pages, with `layout.js` files defining shared UI.

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

- **Core Concept**: Each folder can have its own layout (nested layouts)
- **Real-World Benefit**: Layouts persist across route changes (layout persistence)
- **Common Advantage**: Common elements like navigation stay in place (shared UI)
- **Performance**: Layouts don't re-render on navigation
- **Interview Tip**: Explain that layouts compose together for complex UIs (composition)

---

## 22) What are **Parallel Routes** and **Intercepting Routes** and when would you use them? (**🚀**)

Parallel routes render multiple pages simultaneously, while intercepting routes show pages in modals.

```javascript
// Parallel Routes
// app/dashboard/@analytics/page.js
export default function Analytics() {
  return <div>Analytics Panel</div>;
}
```

- **Core Features**: Parallel routes render multiple pages in same layout, intercepting routes show pages in modals or overlays
- **Real-World Use**: Use `@` prefix for parallel route slots
- **Common Use Case**: Great for modal dialogs and overlays (modals)
- **Advanced Feature**: Better user experience with parallel content (UX)
- **Interview Tip**: Explain that parallel routes enable complex dashboard layouts

---

## 23) What is the difference between `not-found.tsx`, `error.tsx`, and `loading.tsx` files? (**🚀**)

These files handle 404 errors, runtime errors, and loading states respectively in the App Router.

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
```

- **Core Files**: `not-found.tsx` handles 404 errors and missing pages, `error.tsx` handles runtime errors and exceptions, `loading.tsx` shows loading states during navigation
- **Real-World Use**: Can have different error/loading states per route (nested)
- **Important Rule**: Error boundaries must be client components
- **Advanced Feature**: These special files provide better UX
- **Interview Tip**: Explain that these files improve error handling and loading states

---

## 24) How do you perform navigation using the `useRouter()` hook and `router.push()`?

Use `useRouter()` to get the router object and call `push()` to navigate programmatically.

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

- **Core Hook**: `useRouter` hook for programmatic navigation
- **Real-World Methods**: `push()` navigates to new page, adds to history; `replace()` navigates without adding to history
- **Common Navigation**: `back()/forward()` navigate through history, `refresh()` reloads current page
- **Advanced Feature**: Router provides navigation control
- **Interview Tip**: Explain that use router for client-side navigation

---

## 25) How do you implement route groups (`(marketing)`, `(auth)`) in App Router? (**🚀**)

Route groups use parentheses to organize routes without affecting the URL structure.

```javascript
// app/(marketing)/about/page.js -> /about
export default function About() {
  return <h1>About Us</h1>;
}

// app/(marketing)/contact/page.js -> /contact
```

- **Core Syntax**: Use parentheses to organize routes (route groups)
- **Real-World Benefit**: Groups don't affect the URL structure (no URL impact)
- **Common Use**: Each group can have its own layout (layouts)
- **Advanced Feature**: Better project structure and organization
- **Interview Tip**: Explain that can have multiple groups in same app

---

## 26) What is the purpose of the `Link` and `usePathname()` hook in navigation? (**🚀**)

`Link` provides client-side navigation, while `usePathname()` gets the current pathname.

```javascript
import Link from 'next/link';
import { usePathname } from 'next/navigation';

export default function Navigation() {
  const pathname = usePathname();
  
  return (
    <nav>
      <Link href="/" className={pathname === '/' ? 'active' : ''}>
        Home
      </Link>
    </nav>
  );
}
```

- **Core Components**: Link provides client-side navigation with prefetching, `usePathname` gets current pathname for active states
- **Real-World Benefit**: Automatically prefetches linked pages (prefetching)
- **Common Use**: Use `target="_blank"` for external links
- **Performance**: Better than `window.location` for navigation
- **Interview Tip**: Explain that Link improves performance with prefetching

---

## 27) How do you handle redirects, rewrites, and headers in `next.config.js`?

Configure redirects, rewrites, and headers in the `next.config.js` file for routing and security.

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

- **Core Features**: Redirects (permanent (301) or temporary (302) redirects), Rewrites (internal URL rewriting without changing browser URL), Headers (security headers and CORS configuration)
- **Real-World Use**: Use path patterns for flexible matching
- **Common Practice**: Important for security and SEO
- **Advanced Feature**: Configure complex routing and security rules
- **Interview Tip**: Explain that these configs affect routing and security

---
