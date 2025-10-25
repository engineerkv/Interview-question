# ⚛️ Next.js Interview Notes (2025 Edition)

## 🟢 Section 1 — Core Concepts & Rendering — Q1-Q15

---

### 1. 🟢 What problems does Next.js solve compared to plain React apps?

**🧠 Concept**

Next.js solves SEO challenges, performance issues, and complex build configurations by providing server-side rendering, automatic optimization, and opinionated conventions.

**💻 Example**

```jsx
// Plain React SPA - SEO issues
function App() {
  const [data, setData] = useState(null);
  useEffect(() => {
    fetch('/api/data').then(res => res.json()).then(setData);
  }, []);
  return <div>{data ? data.title : 'Loading...'}</div>;
}

// Next.js solution - Server-side rendering
export default async function HomePage() {
  const data = await fetch('https://api.example.com/data');
  return <div>{data.title}</div>;
}
```

**💬 Explanation + Insight**

- **Server-side Rendering** - Better SEO compared to client-side React apps
- **Automatic Optimization** - Code splitting and image optimization out of the box
- **File-based Routing** - Eliminates complex routing configuration
- **Full-stack Development** - API routes without separate backend setup
- **Performance Benefits** - Faster initial page loads and better Core Web Vitals

---

### 2. 🟢 What is the App Router in Next.js 14, and how does it differ from the old Pages Router?

**🧠 Concept**

The App Router is Next.js 14's new routing system using React Server Components, nested layouts, and special files like `layout.js`, `page.js`, and `loading.js`.

**💻 Example**

```jsx
// Pages Router (old) - /pages/index.js
export default function HomePage() {
  return <div>Home Page</div>;
}

// App Router (new) - /app/page.js
export default function HomePage() {
  return <div>Home Page</div>;
}

// App Router with layout - /app/layout.js
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

- **Server Components** - Default server-side rendering
- **Nested Layouts** - Shared layouts without prop drilling
- **Loading States** - Built-in loading.js files
- **Error Boundaries** - Automatic error.js handling
- **Parallel Routes** - Simultaneous route rendering

---

### 3. 🟢 What are React Server Components (RSC), and why are they important?

**🧠 Concept**

React Server Components run on the server during build or request time, allowing direct database access, reduced bundle size, and improved performance.

**💻 Example**

```jsx
// Server Component (default in App Router)
async function UserProfile({ userId }) {
  const user = await db.user.findUnique({ where: { id: userId } });
  return (
    <div>
      <h1>{user.name}</h1>
      <p>{user.email}</p>
    </div>
  );
}

// Client Component (when interactivity needed)
'use client';
function InteractiveButton() {
  const [count, setCount] = useState(0);
  return <button onClick={() => setCount(count + 1)}>Count: {count}</button>;
}
```

**💬 Explanation + Insight**

- **Zero Bundle Size** - Server-only code not sent to client
- **Direct Database Access** - No API layer needed
- **Better Performance** - Reduced JavaScript bundle
- **SEO Friendly** - Server-rendered content
- **Security** - Sensitive logic stays on server

---

### 4. 🟢 What are Client Components, and when should they be used?

**🧠 Concept**

Client Components run in the browser and enable interactivity, state management, and browser APIs. They're marked with "use client" directive.

**💻 Example**

```jsx
// Server Component (default)
async function ProductList() {
  const products = await fetch('https://api.example.com/products');
  return <div>{products.map(p => <ProductCard key={p.id} product={p} />)}</div>;
}

// Client Component for interactivity
'use client';
function ProductCard({ product }) {
  const [isLiked, setIsLiked] = useState(false);
  return (
    <div>
      <h3>{product.name}</h3>
      <button onClick={() => setIsLiked(!isLiked)}>
        {isLiked ? '❤️' : '🤍'}
      </button>
    </div>
  );
}
```

**💬 Explanation + Insight**

- **Interactivity** - Click handlers, form inputs, and user interactions
- **State Management** - useState, useReducer for component state
- **Browser APIs** - localStorage, geolocation, and window object
- **Third-party Libraries** - React Query, Zustand, and other client libraries
- **Performance Impact** - Increases bundle size, use sparingly

---

### 5. 🟢 What is the "use client" directive, and what does it control?

**🧠 Concept**

The "use client" directive marks the boundary between server and client components, creating a client component bundle and enabling browser-specific features.

**💻 Example**

```jsx
// Server Component (default)
async function ServerComponent() {
  const data = await fetch('https://api.example.com/data');
  return <div>{data.title}</div>;
}

// Client Component boundary
'use client';
function ClientComponent({ data }) {
  const [count, setCount] = useState(0);
  useEffect(() => {
    document.title = data.title;
  }, [data.title]);
  return <button onClick={() => setCount(count + 1)}>Count: {count}</button>;
}
```

**💬 Explanation + Insight**

- **Boundary Creation** - Marks client component entry point
- **Bundle Splitting** - Creates separate client bundle
- **Browser APIs** - Enables window, document, localStorage
- **Interactivity** - Event handlers and state management
- **Performance** - Only use when necessary to avoid bundle bloat

---

### 6. 🟢 What is pre-rendering, and how does it improve SEO and performance?

**🧠 Concept**

Pre-rendering generates HTML pages at build time or request time, providing faster loading, better SEO, and improved user experience.

**💻 Example**

```jsx
// Static Generation (SSG) - Build time
export async function getStaticProps() {
  const data = await fetch('https://api.example.com/posts');
  return { props: { posts: data }, revalidate: 3600 };
}

export default function BlogPage({ posts }) {
  return (
    <div>
      {posts.map(post => (
        <article key={post.id}>
          <h2>{post.title}</h2>
          <p>{post.excerpt}</p>
        </article>
      ))}
    </div>
  );
}
```

**💬 Explanation + Insight**

- **SEO Benefits** - Search engines can crawl pre-rendered content
- **Performance** - Faster initial page load with pre-generated HTML
- **User Experience** - No loading states for content
- **Core Web Vitals** - Better LCP, CLS scores
- **Caching** - CDN-friendly static content

---

### 7. 🟢 What is the difference between Static Generation (SSG) and Server-Side Rendering (SSR)?

**🧠 Concept**

SSG pre-builds pages at build time for maximum performance, while SSR generates pages on each request for dynamic content.

**💻 Example**

```jsx
// Static Generation (SSG) - Build time
export async function generateStaticParams() {
  const posts = await fetch('https://api.example.com/posts');
  return posts.map(post => ({ slug: post.slug }));
}

export default async function PostPage({ params }) {
  const post = await fetch(`https://api.example.com/posts/${params.slug}`);
  return <article><h1>{post.title}</h1><p>{post.content}</p></article>;
}

// Server-Side Rendering (SSR) - Request time
export default async function DynamicPage({ searchParams }) {
  const data = await fetch(`https://api.example.com/search?q=${searchParams.q}`, {
    cache: 'no-store'
  });
  return <div>{data.results.map(r => <div key={r.id}>{r.title}</div>)}</div>;
}
```

**💬 Explanation + Insight**

- **SSG** - Faster, CDN-friendly, build-time data
- **SSR** - Dynamic, real-time data, server load
- **Performance** - SSG faster, SSR slower
- **Scalability** - SSG scales better, SSR needs more servers
- **Use Cases** - SSG for blogs, SSR for dashboards

---

### 8. 🟢 What is Incremental Static Regeneration (ISR), and how does it work?

**🧠 Concept**

ISR allows you to update static pages after build time by revalidating them on-demand or on a schedule, combining static generation with dynamic content updates.

**💻 Example**

```jsx
// ISR with time-based revalidation
export async function getStaticProps() {
  const data = await fetch('https://api.example.com/posts');
  return {
    props: { posts: data },
    revalidate: 60 // Revalidate every 60 seconds
  };
}

// Trigger revalidation via API route
export default async function handler(req, res) {
  const { secret, path } = req.query;
  if (secret !== process.env.REVALIDATE_SECRET) {
    return res.status(401).json({ message: 'Invalid secret' });
  }
  await res.revalidate(path);
  return res.json({ revalidated: true });
}
```

**💬 Explanation + Insight**

- **Performance** - Static page speed with dynamic updates
- **Scalability** - Reduced server load
- **Fresh Content** - Automatic content updates
- **Fallback** - Serves stale content while revalidating
- **Selective** - Revalidate specific pages only

---

### 9. 🟢 What is Streaming SSR, and how does it differ from traditional SSR?

**🧠 Concept**

Streaming SSR sends HTML to the browser as it's generated, allowing users to see content faster while the page is still being rendered.

**💻 Example**

```jsx
// Traditional SSR - Wait for everything
export default async function TraditionalPage() {
  const user = await fetchUser(); // Slow
  const posts = await fetchPosts(); // Slow
  return <div><UserProfile user={user} /><PostsList posts={posts} /></div>;
}

// Streaming SSR - Send parts as ready
import { Suspense } from 'react';
export default function StreamingPage() {
  return (
    <div>
      <Suspense fallback={<UserProfileSkeleton />}>
        <UserProfile />
      </Suspense>
      <Suspense fallback={<PostsSkeleton />}>
        <PostsList />
      </Suspense>
    </div>
  );
}
```

**💬 Explanation + Insight**

- **Faster Time to First Byte** - Start sending HTML immediately
- **Better UX** - Progressive loading with skeletons
- **Parallel Data Fetching** - Independent component loading
- **Error Isolation** - One component error doesn't break others
- **Perceived Performance** - Users see content faster

---

### 10. 🟢 What is Partial Rendering, and how does it improve UX?

**🧠 Concept**

Partial Rendering updates only the parts of a page that have changed, reducing data transfer and improving user experience by maintaining state.

**💻 Example**

```jsx
// Partial rendering with parallel routes
// app/dashboard/layout.js
export default function DashboardLayout({ children, analytics, notifications }) {
  return (
    <div className="dashboard">
      <aside>{analytics}</aside>
      <main>{children}</main>
      <aside>{notifications}</aside>
    </div>
  );
}

// Intercepting routes for partial updates
// app/dashboard/@modal/page.js
export default function Modal() {
  return (
    <div className="modal">
      <h2>Quick Edit</h2>
      <form><input type="text" /><button type="submit">Save</button></form>
    </div>
  );
}
```

**💬 Explanation + Insight**

- **Reduced Data Transfer** - Only changed content sent
- **State Preservation** - Maintains component state
- **Faster Updates** - No full page reload
- **Better UX** - Smoother interactions
- **Bandwidth Savings** - Less data usage

---

### 11. 🟢 How does Next.js decide when to render on the server vs client?

**🧠 Concept**

Next.js uses component type (Server vs Client), data fetching methods, and user interactions to determine rendering location for optimal performance.

**💻 Example**

```jsx
// Server Component (default) - Renders on server
async function ServerComponent() {
  const data = await fetch('https://api.example.com/data');
  return <div>{data.title}</div>;
}

// Client Component - Renders on client
'use client';
function ClientComponent() {
  const [count, setCount] = useState(0);
  return <button onClick={() => setCount(count + 1)}>{count}</button>;
}

// Hybrid approach
export default function Page() {
  return (
    <div>
      <ServerComponent />
      <ClientComponent />
    </div>
  );
}
```

**💬 Explanation + Insight**

- **Server Components** - Server-side by default
- **Client Components** - Client-side with "use client"
- **Data Fetching** - Server-side with fetch()
- **User Interactions** - Client-side with event handlers
- **Navigation** - Client-side with Link component

---

### 12. 🟢 What is Turbopack, and how does it improve build performance?

**🧠 Concept**

Turbopack is Next.js's new bundler written in Rust that provides significantly faster build times, hot reloading, and development experience compared to Webpack.

**💻 Example**

```bash
# Using Turbopack for development
npm run dev --turbo

# Or with yarn
yarn dev --turbo
```

```jsx
// Turbopack optimizations
function Component() {
  const [state, setState] = useState(0);
  // Changes to this component reload instantly
  return <div>{state}</div>;
}

// Better tree shaking
import { specificFunction } from 'large-library';
// Only specificFunction is bundled, not the entire library
```

**💬 Explanation + Insight**

- **10x Faster** - Significantly faster than Webpack
- **Rust Performance** - Memory efficient, fast execution
- **Better Caching** - Intelligent cache invalidation
- **Faster HMR** - Hot module replacement
- **Incremental Builds** - Only rebuild what changed

---

### 13. 🟢 What are React Server Actions, and how do they replace traditional API routes?

**🧠 Concept**

Server Actions are functions that run on the server and can be called directly from client components, eliminating the need for separate API routes.

**💻 Example**

```jsx
// Server Action
async function createPost(formData) {
  'use server';
  const title = formData.get('title');
  const content = formData.get('content');
  const post = await db.post.create({ data: { title, content } });
  revalidatePath('/posts');
  redirect(`/posts/${post.id}`);
}

// Using Server Action in component
export default function CreatePostForm() {
  return (
    <form action={createPost}>
      <input name="title" placeholder="Title" required />
      <textarea name="content" placeholder="Content" required />
      <button type="submit">Create Post</button>
    </form>
  );
}
```

**💬 Explanation + Insight**

- **Simplified Architecture** - No separate API routes needed
- **Type Safety** - Full TypeScript support
- **Automatic Serialization** - Handles data conversion
- **Progressive Enhancement** - Works without JavaScript
- **Built-in Validation** - Server-side validation

---

### 14. 🟢 How does Next.js handle component-level caching?

**🧠 Concept**

Next.js provides granular caching at the component level using React's cache() function, allowing you to cache expensive computations and API calls.

**💻 Example**

```jsx
import { cache } from 'react';

// Cached function
const getCachedUser = cache(async (userId) => {
  const user = await fetch(`https://api.example.com/users/${userId}`);
  return user.json();
});

// Component using cached data
async function UserProfile({ userId }) {
  const user = await getCachedUser(userId);
  return (
    <div>
      <h1>{user.name}</h1>
      <p>{user.email}</p>
    </div>
  );
}
```

**💬 Explanation + Insight**

- **Request-scoped** - Cache lasts for single request
- **Automatic Deduplication** - Same calls are deduplicated
- **Memory Efficient** - Garbage collected after request
- **Type Safe** - Full TypeScript support
- **Performance** - Reduces redundant API calls

---

### 15. 🟢 How does the React Compiler optimize Next.js rendering?

**🧠 Concept**

The React Compiler automatically optimizes React components by adding memoization, reducing unnecessary re-renders, and improving performance without manual useMemo or useCallback usage.

**💻 Example**

```jsx
// Before React Compiler - Manual optimization
function ExpensiveComponent({ data, filter }) {
  const filteredData = useMemo(() => {
    return data.filter(item => item.category === filter);
  }, [data, filter]);
  
  const processedData = useMemo(() => {
    return filteredData.map(item => ({ ...item, processed: true }));
  }, [filteredData]);
  
  return <div>{processedData.map(item => <Item key={item.id} data={item} />)}</div>;
}

// After React Compiler - Automatic optimization
function ExpensiveComponent({ data, filter }) {
  // Compiler automatically memoizes these
  const filteredData = data.filter(item => item.category === filter);
  const processedData = filteredData.map(item => ({ ...item, processed: true }));
  return <div>{processedData.map(item => <Item key={item.id} data={item} />)}</div>;
}
```

**💬 Explanation + Insight**

- **Automatic Memoization** - No manual useMemo/useCallback
- **Better Performance** - Reduced unnecessary re-renders
- **Cleaner Code** - Less boilerplate
- **Future Proof** - Optimizes for React updates
- **Bundle Size** - Smaller JavaScript bundles

---

*This comprehensive core concepts section covers all essential Next.js rendering concepts, server components, and performance optimizations for building modern web applications.*