# 🧭 3. Routing & Navigation (Q21–27)

---

## 🧩 Q21. How does nested routing work in App Router?

### 🧠 Concept

Nested routes create layouts that wrap child pages, with `layout.js` files defining shared UI. Layouts compose together for complex UIs (composition).

---

### 💡 Example

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

### 🔍 Deep Insights

* **Rule:** Each folder can have its own layout (nested layouts).
* **Use Case:** Layouts persist across route changes (layout persistence).
* **Common Mistake:** Common elements like navigation stay in place (shared UI).
* **Pro Tip:** Layouts don't re-render on navigation.

---

### ⭐ Senior Takeaway

Layouts compose together for complex UIs (composition).

---

## 🧩 Q22. What are Parallel Routes and how do you use them?

### 🧠 Concept

Parallel routes render multiple pages simultaneously, while intercepting routes show pages in modals. Parallel routes enable complex dashboard layouts.

---

### 💡 Example

```javascript
// Parallel Routes
// app/dashboard/@analytics/page.js
export default function Analytics() {
  return <div>Analytics Panel</div>;
}
```

---

### 🔍 Deep Insights

* **Rule:** Parallel routes render multiple pages in same layout, intercepting routes show pages in modals or overlays.
* **Use Case:** Use `@` prefix for parallel route slots.
* **Common Mistake:** Great for modal dialogs and overlays (modals).
* **Pro Tip:** Better user experience with parallel content (UX).

---

### ⭐ Senior Takeaway

Parallel routes enable complex dashboard layouts.

---

## 🧩 Q23. What are Intercepting Routes and how do you use them?

### 🧠 Concept

Intercepting routes show pages in modals or overlays without changing the URL. Great for modal dialogs and overlays (modals).

---

### 💡 Example

```javascript
// Intercepting route
// app/(.)photos/[id]/page.js
export default function PhotoModal({ params }) {
  return <div>Photo {params.id}</div>;
}
```

---

### 🔍 Deep Insights

* **Rule:** Use `(.)` prefix for same-level intercepting, `(..)` for parent level.
* **Use Case:** Shows content in modal without navigation.
* **Common Mistake:** URL doesn't change, better UX.
* **Pro Tip:** Works with parallel routes for complex layouts.

---

### ⭐ Senior Takeaway

Intercepting routes provide better UX for modals.

---

## 🧩 Q24. How do you handle `not-found.tsx` and `error.tsx`?

### 🧠 Concept

These files handle 404 errors, runtime errors, and loading states respectively in the App Router. These files improve error handling and loading states.

---

### 💡 Example

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

### 🔍 Deep Insights

* **Rule:** `not-found.tsx` handles 404 errors and missing pages, `error.tsx` handles runtime errors and exceptions, `loading.tsx` shows loading states during navigation.
* **Use Case:** Can have different error/loading states per route (nested).
* **Common Mistake:** Error boundaries must be client components.
* **Pro Tip:** These special files provide better UX.

---

### ⭐ Senior Takeaway

These files improve error handling and loading states.

---

## 🧩 Q25. How do you use `loading.tsx` for loading states?

### 🧠 Concept

`loading.tsx` shows loading states during navigation automatically. Provides better UX during route transitions.

---

### 💡 Example

```javascript
// app/loading.tsx
export default function Loading() {
  return <div>Loading...</div>;
}
```

---

### 🔍 Deep Insights

* **Rule:** Automatically shows during route transitions.
* **Use Case:** Can have different loading states per route (nested).
* **Common Mistake:** Works with Suspense for progressive loading.
* **Pro Tip:** Provides better perceived performance.

---

### ⭐ Senior Takeaway

Loading states improve perceived performance.

---

## 🧩 Q26. How do you use `useRouter()` and `router.push()`?

### 🧠 Concept

Use `useRouter()` to get the router object and call `push()` to navigate programmatically. Use router for client-side navigation.

---

### 💡 Example

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

### 🔍 Deep Insights

* **Rule:** `useRouter` hook for programmatic navigation.
* **Use Case:** `push()` navigates to new page, adds to history; `replace()` navigates without adding to history.
* **Common Mistake:** `back()/forward()` navigate through history, `refresh()` reloads current page.
* **Pro Tip:** Router provides navigation control.

---

### ⭐ Senior Takeaway

Use router for client-side navigation.

---

## 🧩 Q27. How do you implement redirects and rewrites?

### 🧠 Concept

Configure redirects, rewrites, and headers in the `next.config.js` file for routing and security. These configs affect routing and security.

---

### 💡 Example

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

### 🔍 Deep Insights

* **Rule:** Redirects (permanent (301) or temporary (302) redirects), Rewrites (internal URL rewriting without changing browser URL), Headers (security headers and CORS configuration).
* **Use Case:** Use path patterns for flexible matching.
* **Common Mistake:** Important for security and SEO.
* **Pro Tip:** Configure complex routing and security rules.

---

### ⭐ Senior Takeaway

These configs affect routing and security.

---
