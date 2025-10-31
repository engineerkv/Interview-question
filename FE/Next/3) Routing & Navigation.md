# 🧭 3. Routing & Navigation (Q21–27)

---

## 21) How does nested routing and layout composition work in the App Router? (**🚀 Next 14**)

Concept:
Nested routes create layouts that wrap child pages, with `layout.js` files defining shared UI.

Example:
```javascript
// app/layout.js - root layout
export default function RootLayout({ children }) {
  return (
    <html>
      <body>
        <header>My App</header>
```

Deep Insight:
- **Nested Layouts**: Each folder can have its own layout
- **Layout Persistence**: Layouts persist across route changes
- **Shared UI**: Common elements like navigation stay in place
- **Performance**: Layouts don't re-render on navigation
- **Composition**: Layouts compose together for complex UIs

---

## 22) What are **Parallel Routes** and **Intercepting Routes** and when would you use them? (**🚀**)

Concept:
Parallel routes render multiple pages simultaneously, while intercepting routes show pages in modals.

Example:
```javascript
// Parallel Routes
// app/dashboard/@analytics/page.js
export default function Analytics() {
  return <div>Analytics Panel</div>;
}

```

Deep Insight:
- **Parallel Routes**: Render multiple pages in same layout
- **Intercepting Routes**: Show pages in modals or overlays
- **Slots**: Use `@` prefix for parallel route slots
- **Modals**: Great for modal dialogs and overlays
- **UX**: Better user experience with parallel content

---

## 23) What is the difference between `not-found.tsx`, `error.tsx`, and `loading.tsx` files? (**🚀**)

Concept:
These files handle 404 errors, runtime errors, and loading states respectively in the App Router.

Example:
```javascript
// app/not-found.tsx - 404 page
export default function NotFound() {
  return (
    <div>
      <h1>404 - Page Not Found</h1>
      <p>The page you're looking for doesn't exist.</p>
```

Deep Insight:
- **not-found.tsx**: Handles 404 errors and missing pages
- **error.tsx**: Handles runtime errors and exceptions
- **loading.tsx**: Shows loading states during navigation
- **Nested**: Can have different error/loading states per route
- **Client Components**: Error boundaries must be client components

---

## 24) How do you perform navigation using the `useRouter()` hook and `router.push()`?

Concept:
Use `useRouter()` to get the router object and call `push()` to navigate programmatically.

Example:
```javascript
'use client';

import { useRouter } from 'next/navigation';

export default function Navigation() {
  const router = useRouter();
```

Deep Insight:
- **useRouter**: Hook for programmatic navigation
- **push()**: Navigate to new page, adds to history
- **replace()**: Navigate without adding to history
- **back()/forward()**: Navigate through history
- **refresh()**: Reload current page

---

## 25) How do you implement route groups (`(marketing)`, `(auth)`) in App Router? (**🚀**)

Concept:
Route groups use parentheses to organize routes without affecting the URL structure.

Example:
```javascript
// app/(marketing)/about/page.js -> /about
export default function About() {
  return <h1>About Us</h1>;
}

// app/(marketing)/contact/page.js -> /contact
```

Deep Insight:
- **Route Groups**: Use parentheses to organize routes
- **No URL Impact**: Groups don't affect the URL structure
- **Layouts**: Each group can have its own layout
- **Organization**: Better project structure and organization
- **Multiple Groups**: Can have multiple groups in same app

---

## 26) What is the purpose of the `Link` and `usePathname()` hook in navigation? (**🚀**)

Concept:
`Link` provides client-side navigation, while `usePathname()` gets the current pathname.

Example:
```javascript
import Link from 'next/link';
import { usePathname } from 'next/navigation';

export default function Navigation() {
  const pathname = usePathname();
  
```

Deep Insight:
- **Link**: Provides client-side navigation with prefetching
- **usePathname**: Gets current pathname for active states
- **Prefetching**: Automatically prefetches linked pages
- **External Links**: Use `target="_blank"` for external links
- **Performance**: Better than `window.location` for navigation

---

## 27) How do you handle redirects, rewrites, and headers in `next.config.js`?

Concept:
Configure redirects, rewrites, and headers in the `next.config.js` file for routing and security.

Example:
```javascript
// next.config.js
/** @type {import('next').NextConfig} */
const nextConfig = {
  // Redirects
  async redirects() {
    return [
```

Deep Insight:
- **Redirects**: Permanent (301) or temporary (302) redirects
- **Rewrites**: Internal URL rewriting without changing browser URL
- **Headers**: Security headers and CORS configuration
- **Patterns**: Use path patterns for flexible matching
- **Security**: Important for security and SEO

---
