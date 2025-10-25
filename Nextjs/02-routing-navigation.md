# ⚛️ Next.js Interview Notes (2025 Edition)

## 🟡 Section 2 — Routing & Navigation — Q16-Q25

---

### 16. 🟡 How does file-based routing work in the App Router?

**🧠 Concept**

File-based routing in the App Router uses the file system structure to define routes, with special files like `page.js`, `layout.js`, and `loading.js` creating the routing hierarchy automatically.

**💻 Example**

```
app/
├── page.js                 # / (home page)
├── layout.js              # Root layout
├── about/
│   └── page.js            # /about
└── blog/
    ├── page.js            # /blog
    └── [slug]/
        └── page.js        # /blog/[slug]
```

```jsx
// app/page.js - Home page
export default function HomePage() {
  return <h1>Welcome to Next.js</h1>;
}

// app/layout.js - Root layout
export default function RootLayout({ children }) {
  return (
    <html lang="en">
      <body>
        <nav>Navigation</nav>
        {children}
        <footer>Footer</footer>
      </body>
    </html>
  );
}
```

**💬 Explanation + Insight**

- **Automatic Route Generation** - File structure creates routes automatically
- **Special Files** - page.js for routes, layout.js for shared layouts
- **Dynamic Routes** - Use [param] syntax for dynamic segments
- **Nested Layouts** - Hierarchical layout composition
- **Performance** - Automatic code splitting per route

---

### 17. 🟡 What are route segments, and how do they work?

**🧠 Concept**

Route segments are the individual parts of a URL path that correspond to folder names in the file system, creating a hierarchical structure for navigation and layout composition.

**💻 Example**

```jsx
// URL: /dashboard/settings/profile
// Segments: ['dashboard', 'settings', 'profile']

// app/dashboard/layout.js - Dashboard segment layout
export default function DashboardLayout({ children }) {
  return (
    <div className="dashboard">
      <aside>Dashboard Sidebar</aside>
      <main>{children}</main>
    </div>
  );
}

// app/dashboard/settings/layout.js - Settings segment layout
export default function SettingsLayout({ children }) {
  return (
    <div className="settings">
      <nav>Settings Navigation</nav>
      {children}
    </div>
  );
}
```

**💬 Explanation + Insight**

- **Hierarchical Structure** - URL segments map to folder structure
- **Layout Composition** - Each segment can have its own layout
- **Nested Routes** - Child routes inherit parent layouts
- **Code Splitting** - Each segment can be split into separate chunks
- **Navigation** - Segments enable programmatic navigation

---

### 18. 🟡 What is the purpose of layout.js, template.js, and page.js files?

**🧠 Concept**

These special files serve different purposes: layout.js for shared layouts, template.js for re-rendering on navigation, and page.js for route content.

**💻 Example**

```jsx
// app/layout.js - Root layout (persists across navigation)
export default function RootLayout({ children }) {
  return (
    <html lang="en">
      <body>
        <nav>Global Navigation</nav>
        {children}
        <footer>Global Footer</footer>
      </body>
    </html>
  );
}

// app/template.js - Template (re-renders on navigation)
export default function Template({ children }) {
  return (
    <div className="template">
      <div className="fade-in">{children}</div>
    </div>
  );
}

// app/page.js - Page content
export default function HomePage() {
  return <h1>Home Page Content</h1>;
}
```

**💬 Explanation + Insight**

- **layout.js** - Shared layouts that persist across navigation
- **template.js** - Re-renders on every navigation for animations
- **page.js** - Defines the actual route content
- **Nesting** - Layouts and templates can be nested
- **Performance** - Layouts are shared, templates re-render

---

### 19. 🟡 What are parallel routes, and how do you use them?

**🧠 Concept**

Parallel routes allow you to render multiple pages simultaneously in the same layout, enabling complex UI patterns like dashboards with multiple panels.

**💻 Example**

```jsx
// app/dashboard/layout.js
export default function DashboardLayout({ children, analytics, notifications }) {
  return (
    <div className="dashboard">
      <aside>
        <nav>Navigation</nav>
        {analytics}
      </aside>
      <main>{children}</main>
      <aside>{notifications}</aside>
    </div>
  );
}

// app/dashboard/analytics/page.js
export default function Analytics() {
  return <div>Analytics Widget</div>;
}

// app/dashboard/notifications/page.js
export default function Notifications() {
  return <div>Notifications Panel</div>;
}
```

**💬 Explanation + Insight**

- **Simultaneous Rendering** - Multiple pages render at the same time
- **Slot-based Architecture** - Use @folder syntax for parallel routes
- **Independent Loading** - Each parallel route loads independently
- **Complex UIs** - Enable dashboard and panel-based interfaces
- **Performance** - Only re-render changed parallel routes

---

### 20. 🟡 What are intercepting routes, and how do they enable modals or drawers?

**🧠 Concept**

Intercepting routes allow you to show a different UI for the same route, enabling modal overlays, drawers, and other overlay patterns without changing the URL.

**💻 Example**

```jsx
// app/dashboard/@modal/(..)photo/[id]/page.js
export default function PhotoModal({ params }) {
  return (
    <div className="modal">
      <h2>Photo {params.id}</h2>
      <button>Close</button>
    </div>
  );
}

// app/dashboard/layout.js
export default function Layout({ children, modal }) {
  return (
    <div>
      {children}
      {modal}
    </div>
  );
}

// app/dashboard/photos/[id]/page.js
export default function PhotoPage({ params }) {
  return <div>Photo {params.id} - Full Page</div>;
}
```

**💬 Explanation + Insight**

- **Overlay Patterns** - Enable modals, drawers, and overlays
- **URL Preservation** - Same URL, different UI presentation
- **Route Interception** - Intercept navigation to show overlay
- **Back Navigation** - Proper back button behavior
- **Accessibility** - Maintain focus management and keyboard navigation

---

### 21. 🟡 What is the difference between nested layouts and templates?

**🧠 Concept**

Nested layouts persist across navigation and are shared, while templates re-render on every navigation and are used for animations and transitions.

**💻 Example**

```jsx
// app/dashboard/layout.js - Nested layout (persists)
export default function DashboardLayout({ children }) {
  return (
    <div className="dashboard">
      <aside>Sidebar</aside>
      <main>{children}</main>
    </div>
  );
}

// app/dashboard/template.js - Template (re-renders)
export default function DashboardTemplate({ children }) {
  return (
    <div className="fade-in">
      {children}
    </div>
  );
}

// app/dashboard/page.js - Page content
export default function Dashboard() {
  return <h1>Dashboard Content</h1>;
}
```

**💬 Explanation + Insight**

- **Layouts** - Persist across navigation, shared state
- **Templates** - Re-render on every navigation
- **Animations** - Templates enable page transitions
- **Performance** - Layouts are more efficient
- **Use Cases** - Layouts for structure, templates for effects

---

### 22. 🟡 How do you navigate between routes using <Link> and useRouter()?

**🧠 Concept**

Next.js provides <Link> component for declarative navigation and useRouter() hook for programmatic navigation with client-side routing.

**💻 Example**

```jsx
import Link from 'next/link';
import { useRouter } from 'next/navigation';

// Declarative navigation with Link
export default function Navigation() {
  return (
    <nav>
      <Link href="/dashboard">Dashboard</Link>
      <Link href="/profile">Profile</Link>
      <Link href="/settings">Settings</Link>
    </nav>
  );
}

// Programmatic navigation with useRouter
'use client';
import { useRouter } from 'next/navigation';

export default function LoginForm() {
  const router = useRouter();
  
  const handleLogin = async () => {
    // Login logic
    router.push('/dashboard');
  };
  
  return <button onClick={handleLogin}>Login</button>;
}
```

**💬 Explanation + Insight**

- **Link Component** - Declarative navigation with prefetching
- **useRouter Hook** - Programmatic navigation and route manipulation
- **Client-side Routing** - Fast navigation without page reloads
- **Prefetching** - Automatic prefetching of linked routes
- **Back/Forward** - Proper browser history support

---

### 23. 🟡 What is the difference between not-found.js and error.js?

**🧠 Concept**

not-found.js handles 404 errors for missing routes, while error.js handles runtime errors and provides error boundaries for the route segment.

**💻 Example**

```jsx
// app/not-found.js - 404 page
export default function NotFound() {
  return (
    <div>
      <h2>Not Found</h2>
      <p>Could not find requested resource</p>
      <Link href="/">Return Home</Link>
    </div>
  );
}

// app/error.js - Error boundary
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

**💬 Explanation + Insight**

- **not-found.js** - Handles 404 errors for missing routes
- **error.js** - Handles runtime errors and exceptions
- **Error Boundaries** - Isolate errors to specific route segments
- **Recovery** - Provide reset functionality for error recovery
- **User Experience** - Better error handling and user feedback

---

### 24. 🟡 How do you pass data between routes without using query params?

**🧠 Concept**

Next.js provides several ways to pass data between routes including server actions, cookies, headers, and state management libraries.

**💻 Example**

```jsx
// Using server actions to pass data
async function createUser(formData) {
  'use server';
  const user = await db.user.create({ data: formData });
  redirect(`/users/${user.id}`);
}

// Using cookies for persistent data
import { cookies } from 'next/headers';

export async function setUserPreference(preference) {
  cookies().set('user-preference', preference);
}

// Using headers for temporary data
import { headers } from 'next/headers';

export async function getRequestData() {
  const headersList = headers();
  return headersList.get('x-user-data');
}
```

**💬 Explanation + Insight**

- **Server Actions** - Direct data passing with redirects
- **Cookies** - Persistent data across requests
- **Headers** - Temporary data for single request
- **State Management** - Zustand, Redux for complex state
- **URL State** - Use query params for shareable state

---

### 25. 🟡 What is dynamic routing, and how do you implement [slug] routes?

**🧠 Concept**

Dynamic routing allows you to create routes with variable segments using bracket notation, enabling parameterized routes for dynamic content.

**💻 Example**

```jsx
// app/blog/[slug]/page.js - Dynamic route
export default async function BlogPost({ params }) {
  const post = await fetch(`https://api.example.com/posts/${params.slug}`);
  return (
    <article>
      <h1>{post.title}</h1>
      <p>{post.content}</p>
    </article>
  );
}

// app/shop/[...slug]/page.js - Catch-all route
export default function ShopPage({ params }) {
  const category = params.slug?.[0] || 'all';
  return <div>Shop Category: {category}</div>;
}

// app/docs/[[...slug]]/page.js - Optional catch-all
export default function DocsPage({ params }) {
  const page = params.slug?.[0] || 'index';
  return <div>Documentation: {page}</div>;
}
```

**💬 Explanation + Insight**

- **Dynamic Segments** - Use [param] for single parameters
- **Catch-all Routes** - Use [...param] for multiple segments
- **Optional Routes** - Use [[...param]] for optional segments
- **Parameter Access** - Access via params object in components
- **SEO** - Generate static params for better SEO

---

*This comprehensive routing section covers all essential Next.js App Router concepts, navigation patterns, and advanced routing features for building complex applications.*