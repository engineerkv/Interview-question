---
sidebar_label: "Patterns"
---
# 🎯 Patterns

---

## 1. 🎨 Rendering Patterns

Rendering patterns determine when and where your application generates HTML and sends it to the browser. Different patterns offer different trade-offs between performance, SEO, user experience, and complexity. Understanding these patterns helps you choose the right approach for your application and optimize for your specific use case.

### 🔹 Client-Side Rendering (CSR)

CSR renders content entirely in the browser using JavaScript after the initial HTML page loads. This is the traditional SPA (Single Page Application) approach where the server sends a minimal HTML shell and JavaScript handles all rendering.

### 🔹 How CSR Works - Detailed Flow

**Step 1: Initial HTML Request**

* Browser requests the page URL
* Server responds with minimal HTML shell (usually just a `<div id="root">` and script tags)
* HTML contains links to JavaScript bundles (main.js, vendor.js, etc.)

**Step 2: JavaScript Download**

* Browser downloads JavaScript bundles in parallel
* Bundles are typically large (can be 200KB-2MB+ depending on app size)
* Download time depends on network speed and bundle size

**Step 3: JavaScript Execution**

* JavaScript executes in the browser
* Framework (React/Vue/Angular) initializes
* Router determines which component to render
* Application state is initialized

**Step 4: Data Fetching**

* Components mount and trigger data fetching (via `useEffect`, `componentDidMount`, etc.)
* API calls are made to backend services
* Data is fetched asynchronously

**Step 5: DOM Generation**

* Framework generates virtual DOM from component tree
* Virtual DOM is reconciled and converted to real DOM
* Browser paints the page

**Step 6: Interactivity**

* Event listeners are attached
* Page becomes fully interactive
* Subsequent navigations happen client-side (no full page reload)

### 🔹 Performance Characteristics

**Metrics:**

* **Time to First Byte (TTFB)**: Very fast (~50-200ms) - just serving static HTML
* **First Contentful Paint (FCP)**: Slow (2-5+ seconds) - waits for JS download and execution
* **Time to Interactive (TTI)**: Slow (3-8+ seconds) - waits for JS + data fetching
* **Largest Contentful Paint (LCP)**: Slow - depends on when data loads and renders

**Performance Bottlenecks:**

* Large JavaScript bundles (main bottleneck)
* Multiple round trips for data fetching
* JavaScript parsing and execution time
* Network latency for API calls

**Optimization Strategies:**

* Code splitting (route-based, component-based)
* Lazy loading of components
* Bundle optimization (tree shaking, minification)
* Prefetching data and routes
* Service workers for caching
* CDN for static assets

### 🔹 SEO Considerations

**Challenges:**

* Search engines historically didn't execute JavaScript (Google now does, but with limitations)
* Initial HTML is empty - no content for crawlers
* Social media crawlers (Facebook, Twitter) may not execute JavaScript
* Slower indexing of content

**Solutions:**

* Use pre-rendering services (Prerender.io, Puppeteer)
* Implement server-side rendering for public pages
* Use dynamic rendering (serve SSR to bots, CSR to users)
* Ensure critical content is in initial HTML

### 🔹 Characteristics

**Advantages:**

* **Fast Navigation**: Subsequent page changes are instant (no full page reload)
* **Rich Interactivity**: Full SPA experience with smooth transitions
* **Reduced Server Load**: Server only serves static files, no rendering needed
* **Offline Support**: Can work offline with service workers
* **Simple Deployment**: Can deploy to static hosting (Netlify, Vercel, S3)

**Disadvantages:**

* **Slow Initial Load**: User sees blank screen until JavaScript loads and executes
* **SEO Challenges**: Search engines may not execute JavaScript (though modern crawlers do)
* **API Dependency**: Requires separate API endpoints
* **Large Bundle Size**: All JavaScript must be downloaded upfront
* **Poor Performance on Slow Devices**: JavaScript execution can be slow on low-end devices

### 🔹 Use Cases

* **Dashboards**: Admin panels, analytics tools (SEO not needed, fast navigation important)
* **Authenticated Apps**: Apps behind login (SEO not critical, user experience is priority)
* **Highly Interactive Apps**: Real-time apps, games, complex UIs (need client-side interactivity)
* **Mobile Apps**: React Native, PWAs (native-like experience)
* **Internal Tools**: Company tools where SEO doesn't matter

### 🔹 Implementation Examples

**Basic CSR with React:**

```javascript
// CSR - React app
function App() {
  const [data, setData] = useState(null);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState(null);

  useEffect(() => {
    fetch('/api/data')
      .then(res => {
        if (!res.ok) throw new Error('Failed to fetch');
        return res.json();
      })
      .then(setData)
      .catch(setError)
      .finally(() => setLoading(false));
  }, []);

  if (loading) return <div>Loading...</div>;
  if (error) return <div>Error: {error.message}</div>;
  return <div>{data.content}</div>;
}
```

**CSR with Code Splitting:**

```javascript
// Lazy load components for better performance
import { lazy, Suspense } from 'react';

const HeavyComponent = lazy(() => import('./HeavyComponent'));

function App() {
  return (
    <Suspense fallback={<div>Loading component...</div>}>
      <HeavyComponent />
    </Suspense>
  );
}
```

**CSR with Client-Side Routing:**

```javascript
// React Router example
import { BrowserRouter, Routes, Route } from 'react-router-dom';

function App() {
  return (
    <BrowserRouter>
      <Routes>
        <Route path="/" element={<Home />} />
        <Route path="/about" element={<About />} />
        <Route path="/contact" element={<Contact />} />
      </Routes>
    </BrowserRouter>
  );
}
```

### 🔹 When to Choose CSR

**Choose CSR when:**

* SEO is not a priority (authenticated apps, dashboards)
* You need fast client-side navigation
* App is highly interactive
* You want simple deployment (static hosting)
* Initial load time is acceptable for your users

**Avoid CSR when:**

* SEO is critical (public-facing content)
* Initial load performance is important
* Users have slow devices or networks
* Social media sharing is important

📌 **In simple terms**: CSR is like ordering food at a restaurant - you get an empty table (HTML shell), then the waiter brings everything (JavaScript renders content). Fast for navigation, but slow initial experience. Best for authenticated apps and dashboards where SEO doesn't matter.

---

### 🔹 Server-Side Rendering (SSR)

SSR generates HTML on the server for each request and sends fully rendered HTML to the browser. The server executes your React/Vue/Angular code, fetches data, and sends complete HTML to the client.

### 🔹 How SSR Works - Detailed Flow

**Step 1: Request Arrives**

* User requests a page (e.g., `/products/123`)
* Request includes cookies, headers, query parameters
* Server receives the request

**Step 2: Server-Side Data Fetching**

* Server executes data fetching functions (`getServerSideProps`, Server Components, etc.)
* Can access request context (cookies, headers, user session)
* Fetches data from databases, APIs, or other services
* Data fetching happens on server (faster, no CORS issues)

**Step 3: Server-Side Rendering**

* Server runs React/Vue/Angular code
* Components render to HTML string
* All data is already available (no loading states needed)
* HTML includes all content, styles, and initial state

**Step 4: HTML Response**

* Server sends complete HTML to browser
* HTML includes rendered content, inline styles, and script tags
* Browser can start parsing and rendering immediately

**Step 5: Client-Side Hydration**

* JavaScript bundles download in parallel
* Framework "hydrates" the HTML (attaches event listeners)
* React/Vue matches virtual DOM to existing HTML
* Page becomes interactive

**Step 6: Subsequent Navigation**

* Can use client-side routing (Next.js Link, React Router)
* Or full page reloads (traditional SSR)

### 🔹 Performance Characteristics

**Metrics:**

* **Time to First Byte (TTFB)**: Slower (200-1000ms+) - server must process request
* **First Contentful Paint (FCP)**: Fast (500-1500ms) - HTML arrives with content
* **Time to Interactive (TTI)**: Moderate (1-3 seconds) - waits for hydration
* **Largest Contentful Paint (LCP)**: Fast - content is in initial HTML

**Performance Bottlenecks:**

* Server processing time (data fetching + rendering)
* Server CPU and memory usage
* Database query time
* Network latency for server requests
* Hydration time on client

**Optimization Strategies:**

* Cache rendered pages (Redis, in-memory cache)
* Optimize database queries
* Use CDN for static assets
* Implement streaming SSR (send HTML progressively)
* Reduce JavaScript bundle size (affects hydration time)
* Use edge computing (render closer to users)

### 🔹 Server Load Considerations

**Resource Usage:**

* Each request requires CPU for rendering
* Memory usage for React component trees
* Database connections for data fetching
* Network bandwidth for responses

**Scaling Challenges:**

* Need more server resources as traffic grows
* Can't use static hosting (requires Node.js server)
* Higher infrastructure costs
* Need load balancing for high traffic

**Solutions:**

* Horizontal scaling (multiple servers)
* Caching strategies (page-level, component-level)
* Edge rendering (render at CDN edge)
* Hybrid approach (SSR for some pages, SSG for others)

### 🔹 Characteristics

**Advantages:**

* **Fast Initial Load**: User sees content immediately (no blank screen)
* **SEO Friendly**: Search engines get fully rendered HTML with all content
* **Social Media Sharing**: Open Graph tags work perfectly (content in HTML)
* **Personalization**: Can customize content per user (cookies, headers)
* **Always Fresh Data**: Data is fetched on each request

**Disadvantages:**

* **Server Load**: Each request requires server processing (higher costs)
* **Slower TTFB**: Server must process before sending response
* **Infrastructure Complexity**: Need Node.js server (can't use static hosting)
* **Slower Navigation**: Full page reloads (unless using client-side routing)
* **Hydration Overhead**: JavaScript must hydrate HTML (adds to TTI)

### 🔹 Use Cases

* **Content Sites**: Blogs, news sites, marketing pages (SEO critical)
* **E-commerce**: Product pages, category pages (need SEO + personalization)
* **Public-Facing Sites**: Sites where SEO is critical
* **Social Media**: Posts, profiles (need fast initial render + SEO)
* **User-Generated Content**: Forums, comments (dynamic, personalized)

### 🔹 Implementation Examples

**SSR with Next.js (Pages Router):**

```javascript
// pages/products/[id].js
export async function getServerSideProps(context) {
  const { id } = context.params;
  const { req, res } = context;

  // Access cookies, headers
  const userId = req.cookies.userId;

  // Fetch data on server
  const product = await fetchProduct(id);
  const user = await fetchUser(userId);

  // Can set response headers
  res.setHeader('Cache-Control', 'public, s-maxage=60, stale-while-revalidate=120');

  return {
    props: {
      product,
      user,
      // Data is available immediately, no loading state needed
    }
  };
}

export default function ProductPage({ product, user }) {
  return (
    <div>
      <h1>{product.name}</h1>
      <p>{product.description}</p>
      {/* Content is already in HTML, no loading spinner */}
    </div>
  );
}
```

**SSR with Next.js (App Router - Server Components):**

```javascript
// app/products/[id]/page.js
// Server Component by default (no 'use client')
async function ProductPage({ params }) {
  // This runs on server
  const product = await fetchProduct(params.id);

  // Can access headers, cookies directly
  const headersList = headers();
  const userAgent = headersList.get('user-agent');

  return (
    <div>
      <h1>{product.name}</h1>
      <p>{product.description}</p>
      {/* Client Component for interactivity */}
      <AddToCartButton productId={product.id} />
    </div>
  );
}

// app/components/AddToCartButton.js
'use client'; // Client Component
import { useState } from 'react';

export function AddToCartButton({ productId }) {
  const [loading, setLoading] = useState(false);

  const handleClick = async () => {
    setLoading(true);
    await addToCart(productId);
    setLoading(false);
  };

  return (
    <button onClick={handleClick} disabled={loading}>
      Add to Cart
    </button>
  );
}
```

**SSR with Express + React:**

```javascript
// server.js
import express from 'express';
import React from 'react';
import { renderToString } from 'react-dom/server';
import App from './App';

const app = express();

app.get('*', async (req, res) => {
  // Fetch data on server
  const data = await fetchData(req.url);

  // Render React to HTML string
  const html = renderToString(<App data={data} />);

  // Send complete HTML
  res.send(`
    <!DOCTYPE html>
    <html>
      <head><title>My App</title></head>
      <body>
        <div id="root">${html}</div>
        <script src="/client.js"></script>
      </body>
    </html>
  `);
});
```

### 🔹 Streaming SSR

Modern SSR can stream HTML progressively:

```javascript
// Next.js App Router with Streaming
import { Suspense } from 'react';

async function Page() {
  return (
    <div>
      <Header /> {/* Renders immediately */}
      <Suspense fallback={<div>Loading posts...</div>}>
        <Posts /> {/* Streams when ready */}
      </Suspense>
      <Suspense fallback={<div>Loading comments...</div>}>
        <Comments /> {/* Streams when ready */}
      </Suspense>
    </div>
  );
}
```

**Benefits of Streaming:**

* Faster Time to First Byte (TTFB)
* User sees content progressively
* Better perceived performance
* Can show loading states for slow parts

### 🔹 When to Choose SSR

**Choose SSR when:**

* SEO is critical (public-facing content)
* You need personalized content per user
* Social media sharing is important
* Initial load performance matters
* Content changes frequently

**Avoid SSR when:**

* You want simple deployment (static hosting)
* Server costs are a concern
* Most content is static
* You don't need SEO (authenticated apps)

📌 **In simple terms**: SSR is like a restaurant that brings your food ready to eat - you get everything immediately, but each new order takes time to prepare. Best for content sites and e-commerce where SEO and initial load performance matter.

---

### 🔹 Static Site Generation (SSG)

SSG pre-renders pages at build time, generating static HTML files that are served directly. This is the fastest rendering pattern because HTML is generated once and served from a CDN.

### 🔹 How SSG Works - Detailed Flow

**Step 1: Build Time**

* Developer runs build command (`next build`, `gatsby build`, etc.)
* Framework analyzes all pages and routes
* Identifies which pages need static generation

**Step 2: Data Fetching at Build**

* For each page, executes data fetching functions (`getStaticProps`, `getStaticPaths`)
* Fetches data from APIs, databases, CMS, or file system
* Data is fetched once during build (not per request)

**Step 3: HTML Generation**

* Framework renders each page to HTML
* All React/Vue components are executed
* Complete HTML is generated with all content
* HTML files are saved to disk

**Step 4: Static File Storage**

* Generated HTML files are stored in build output directory
* Can be deployed to CDN (Cloudflare, CloudFront, etc.)
* Can be deployed to static hosting (Netlify, Vercel, GitHub Pages)

**Step 5: Request Handling**

* User requests a page
* CDN or static host serves pre-generated HTML file
* No server processing needed
* Response is instant (served from CDN edge)

**Step 6: Client-Side Hydration**

* JavaScript bundles download
* Framework hydrates the static HTML
* Page becomes interactive

### 🔹 Performance Characteristics

**Metrics:**

* **Time to First Byte (TTFB)**: Very fast (10-100ms) - served from CDN edge
* **First Contentful Paint (FCP)**: Very fast (200-500ms) - HTML arrives immediately
* **Time to Interactive (TTI)**: Fast (500-1500ms) - only waits for hydration
* **Largest Contentful Paint (LCP)**: Very fast - content is in initial HTML

**Why SSG is Fastest:**

* No server processing per request
* Served from CDN (geographically distributed)
* Can use HTTP/2 and HTTP/3
* Browser caching works perfectly
* No database queries per request

**Performance Bottlenecks:**

* Build time (can be slow for many pages)
* Hydration time (still needs JavaScript)
* Large HTML files (if pages are very large)

### 🔹 Build Process Deep Dive

**Static Path Generation:**

```javascript
// Next.js - Generate static paths for dynamic routes
export async function getStaticPaths() {
  // Fetch all possible paths
  const products = await fetchAllProducts();

  return {
    paths: products.map(product => ({
      params: { id: product.id.toString() }
    })),
    // fallback: false - 404 if path not pre-rendered
    // fallback: 'blocking' - generate on-demand (ISR)
    // fallback: true - show loading, then generate
    fallback: false
  };
}

export async function getStaticProps({ params }) {
  const product = await fetchProduct(params.id);
  return {
    props: { product },
    // Optional: revalidate for ISR
    // revalidate: 3600
  };
}
```

**Build Time Considerations:**

* Build time increases with number of pages
* Large sites may take minutes to build
* Can parallelize page generation
* Can use incremental builds (only rebuild changed pages)

### 🔹 Characteristics

**Advantages:**

* **Fastest Performance**: Pre-generated HTML served from CDN (10-100ms TTFB)
* **Excellent SEO**: Fully rendered HTML available immediately
* **Scalability**: Can serve millions of requests (CDN handles it)
* **Low Cost**: No server needed (static hosting is cheap/free)
* **Security**: No server-side code execution (reduces attack surface)
* **Reliability**: Static files are highly available
* **Global Distribution**: CDN serves from edge locations worldwide

**Disadvantages:**

* **Build Time Data**: Content must be known at build time
* **Rebuild Required**: Content changes require rebuilding and redeploying
* **No Personalization**: Same HTML for all users (unless using client-side JS)
* **Build Time**: Can be slow for sites with many pages
* **No Request Context**: Can't access cookies, headers, query params at build time

### 🔹 Use Cases

* **Documentation**: Technical docs, API docs (content changes infrequently)
* **Blogs**: Personal blogs, company blogs (content updates periodically)
* **Marketing Sites**: Landing pages, product pages (mostly static content)
* **Portfolios**: Personal portfolios, showcase sites (rarely changes)
* **Documentation Sites**: Docusaurus, GitBook (content from markdown)
* **E-commerce Catalogs**: Product listings (if prices don't change frequently)

### 🔹 Implementation Examples

**Basic SSG:**

```javascript
// pages/blog/[slug].js
export async function getStaticPaths() {
  const posts = await getAllPostSlugs();

  return {
    paths: posts.map(slug => ({ params: { slug } })),
    fallback: false
  };
}

export async function getStaticProps({ params }) {
  const post = await getPostBySlug(params.slug);

  return {
    props: { post }
  };
}

export default function BlogPost({ post }) {
  return (
    <article>
      <h1>{post.title}</h1>
      <div dangerouslySetInnerHTML={{ __html: post.content }} />
    </article>
  );
}
```

**SSG with Multiple Data Sources:**

```javascript
export async function getStaticProps() {
  // Fetch from multiple sources in parallel
  const [posts, categories, authors] = await Promise.all([
    fetchPosts(),
    fetchCategories(),
    fetchAuthors()
  ]);

  return {
    props: {
      posts,
      categories,
      authors
    }
  };
}
```

**SSG with Markdown Files:**

```javascript
import fs from 'fs';
import path from 'path';
import matter from 'gray-matter';

export async function getStaticProps() {
  const postsDirectory = path.join(process.cwd(), 'posts');
  const filenames = fs.readdirSync(postsDirectory);

  const posts = filenames.map(filename => {
    const filePath = path.join(postsDirectory, filename);
    const fileContents = fs.readFileSync(filePath, 'utf8');
    const { data, content } = matter(fileContents);

    return {
      slug: filename.replace(/\.md$/, ''),
      title: data.title,
      content
    };
  });

  return {
    props: { posts }
  };
}
```

### 🔹 Deployment Strategies

**Static Hosting:**

* Netlify, Vercel, GitHub Pages
* Automatic builds on git push
* Free tier available
* Easy deployment

**CDN Deployment:**

* Cloudflare Pages, AWS CloudFront
* Global distribution
* High performance
* Custom domains

**Hybrid Approach:**

* Some pages SSG, others SSR
* Use SSG for static content
* Use SSR for dynamic content

### 🔹 When to Choose SSG

**Choose SSG when:**

* Content is mostly static
* SEO is critical
* You want fastest performance
* You want low hosting costs
* Content doesn't change frequently
* You can rebuild on content updates

**Avoid SSG when:**

* Content changes very frequently
* You need per-user personalization
* You need real-time data
* Build time would be too long (millions of pages)

📌 **In simple terms**: SSG is like a vending machine - everything is prepared in advance, you get it instantly, but you can't customize it per customer. Best for blogs, documentation, and marketing sites where content is mostly static.

---

### 🔹 Incremental Static Regeneration (ISR)

ISR combines SSG with on-demand regeneration - pages are pre-rendered but can be regenerated in the background. This gives you the performance of SSG with the freshness of SSR.

### 🔹 How ISR Works - Detailed Flow

**Step 1: Initial Build (Optional)**

* Pages can be pre-rendered at build time (like SSG)
* Or pages can be generated on-demand (no pre-rendering)
* Build time is faster (don't need to generate all pages)

**Step 2: First Request**

* User requests a page
* If page exists (pre-rendered), serve it immediately
* If page doesn't exist, generate it on-demand (blocking)
* Page is cached after generation

**Step 3: Subsequent Requests (Within Revalidation Window)**

* User requests page
* Check if page is stale (older than `revalidate` time)
* If fresh, serve cached version immediately
* No regeneration needed

**Step 4: Stale Request (After Revalidation Window)**

* User requests stale page
* Serve stale cached version immediately (fast response)
* Trigger background regeneration
* Regeneration happens asynchronously

**Step 5: Regeneration Complete**

* New HTML is generated with fresh data
* New version is cached
* Next request gets fresh version

**Step 6: On-Demand Revalidation**

* Can trigger regeneration manually (webhook, API call)
* Useful when content is updated (CMS, database)
* Immediate regeneration (not waiting for revalidate time)

### 🔹 Revalidation Strategies

**Time-Based Revalidation:**

```javascript
export async function getStaticProps() {
  const data = await fetchData();

  return {
    props: { data },
    // Regenerate page if it's older than 60 seconds
    revalidate: 60
  };
}
```

**How it works:**

* Page is considered "fresh" for 60 seconds
* After 60 seconds, page is "stale"
* Stale pages are served immediately, then regenerated in background
* Next user gets fresh version

**On-Demand Revalidation:**

```javascript
// pages/api/revalidate.js
export default async function handler(req, res) {
  // Verify webhook secret
  if (req.query.secret !== process.env.REVALIDATE_SECRET) {
    return res.status(401).json({ message: 'Invalid token' });
  }

  try {
    // Revalidate specific path
    await res.revalidate('/products/123');

    // Or revalidate by tag
    revalidateTag('products');

    return res.json({ revalidated: true });
  } catch (err) {
    return res.status(500).send('Error revalidating');
  }
}
```

**Tag-Based Revalidation:**

```javascript
// Fetch with tag
export async function getStaticProps() {
  const data = await fetch('https://api.example.com/products', {
    next: { tags: ['products'] }
  });

  return {
    props: { products: await data.json() },
    revalidate: 3600
  };
}

// Revalidate by tag (invalidates all pages using this data)
revalidateTag('products');
```

### 🔹 Fallback Strategies

**fallback: false**

```javascript
export async function getStaticPaths() {
  return {
    paths: [
      { params: { id: '1' } },
      { params: { id: '2' } }
    ],
    fallback: false // 404 for any path not in paths array
  };
}
```

* Only pre-rendered paths are available
* Other paths return 404
* Use when you know all paths at build time

**fallback: 'blocking'**

```javascript
export async function getStaticPaths() {
  return {
    paths: [],
    fallback: 'blocking' // Generate on-demand, user waits
  };
}
```

* Paths not pre-rendered are generated on first request
* User waits for generation (like SSR)
* Page is cached after generation
* Use when you want to generate pages on-demand

**fallback: true**

```javascript
export async function getStaticPaths() {
  return {
    paths: [],
    fallback: true // Show loading state, generate in background
  };
}
```

* Show loading/fallback UI while generating
* Page is generated in background
* Better UX than blocking
* Requires handling loading state in component

### 🔹 Performance Characteristics

**Metrics:**

* **Time to First Byte (TTFB)**: Very fast (10-100ms) - served from cache
* **First Contentful Paint (FCP)**: Very fast - cached HTML
* **Stale Content**: Users may see slightly stale content (within revalidate window)
* **Background Regeneration**: Happens asynchronously (doesn't block requests)

**Performance Benefits:**

* Fast like SSG (served from cache)
* Fresh like SSR (regenerates periodically)
* No server load for most requests (served from cache)
* Can handle millions of pages (generate on-demand)

**Trade-offs:**

* Slight delay for first request after revalidation
* Users may see stale content (within revalidate window)
* More complex than pure SSG or SSR

### 🔹 Characteristics

**Advantages:**

* **Best of Both Worlds**: Fast like SSG, fresh like SSR
* **Stale-While-Revalidate**: Users get fast response, content updates in background
* **Build Time Flexibility**: Can have some pages pre-rendered, others on-demand
* **Scalability**: Can handle millions of pages (generate on-demand)
* **Cost Effective**: Most requests served from cache (low server load)

**Disadvantages:**

* **Complexity**: More complex than pure SSG or SSR
* **Stale Content**: Users may see slightly stale content
* **First Request Delay**: On-demand generation can delay first request
* **Cache Management**: Need to manage revalidation strategy

### 🔹 Use Cases

* **E-commerce**: Product pages (thousands of products, can't pre-render all)
* **Content Sites**: News sites, blogs with frequent updates
* **Hybrid Apps**: Mix of static and dynamic content
* **Large Sites**: Sites with too many pages to pre-render
* **CMS-Driven Sites**: Content updates from CMS, need freshness

### 🔹 Implementation Examples

**ISR with Time-Based Revalidation:**

```javascript
// pages/products/[id].js
export async function getStaticPaths() {
  // Pre-render top 100 products
  const topProducts = await getTopProducts(100);

  return {
    paths: topProducts.map(product => ({
      params: { id: product.id.toString() }
    })),
    fallback: 'blocking' // Generate others on-demand
  };
}

export async function getStaticProps({ params }) {
  const product = await fetchProduct(params.id);

  if (!product) {
    return { notFound: true };
  }

  return {
    props: { product },
    // Regenerate every 60 seconds
    revalidate: 60
  };
}
```

**ISR with On-Demand Revalidation:**

```javascript
// pages/api/revalidate-product.js
import { revalidatePath } from 'next/cache';

export default async function handler(req, res) {
  if (req.method !== 'POST') {
    return res.status(405).json({ message: 'Method not allowed' });
  }

  const { productId } = req.body;

  try {
    // Revalidate specific product page
    revalidatePath(`/products/${productId}`);

    // Or revalidate all product pages
    revalidatePath('/products');

    return res.json({
      revalidated: true,
      productId
    });
  } catch (err) {
    return res.status(500).json({
      message: 'Error revalidating',
      error: err.message
    });
  }
}

// Call from CMS webhook or after database update
// POST /api/revalidate-product
// { "productId": "123" }
```

**ISR with Tag-Based Revalidation:**

```javascript
// pages/products/[id].js
export async function getStaticProps({ params }) {
  const product = await fetch('https://api.example.com/products/' + params.id, {
    next: {
      tags: ['products', `product-${params.id}`],
      revalidate: 3600
    }
  });

  return {
    props: { product: await product.json() }
  };
}

// pages/api/revalidate.js
import { revalidateTag } from 'next/cache';

export default async function handler(req, res) {
  const { tag } = req.query;

  // Revalidate all pages using this tag
  revalidateTag(tag);

  return res.json({ revalidated: true, tag });
}

// Revalidate all products: /api/revalidate?tag=products
// Revalidate specific product: /api/revalidate?tag=product-123
```

**ISR with Fallback UI:**

```javascript
import { useRouter } from 'next/router';

export async function getStaticPaths() {
  return {
    paths: [],
    fallback: true // Show loading state
  };
}

export default function ProductPage({ product }) {
  const router = useRouter();

  // Show loading state while generating
  if (router.isFallback) {
    return <div>Loading product...</div>;
  }

  return (
    <div>
      <h1>{product.name}</h1>
      <p>{product.description}</p>
    </div>
  );
}
```

### 🔹 When to Choose ISR

**Choose ISR when:**

* You have too many pages to pre-render at build time
* Content updates periodically (not real-time)
* You want fast performance (cached pages)
* You need some freshness (periodic updates)
* You have a CMS or content that updates

**Avoid ISR when:**

* Content must be real-time (use SSR)
* All pages can be pre-rendered (use SSG)
* You need per-user personalization (use SSR)
* Revalidation complexity isn't worth it

📌 **In simple terms**: ISR is like a restaurant with pre-made meals that get refreshed - you get food fast, but it's always fresh because the kitchen makes new batches in the background. Best for e-commerce and content sites with many pages that update periodically.

---

### 🔹 Streaming SSR

Streaming SSR sends HTML to the browser progressively as it's generated, rather than waiting for the entire page. This improves perceived performance by showing content as soon as it's ready.

### 🔹 How Streaming SSR Works - Detailed Flow

**Step 1: Request Arrives**

* User requests a page
* Server starts processing immediately

**Step 2: Initial HTML Stream**

* Server sends HTML headers and initial structure
* Browser can start parsing immediately
* Fast Time to First Byte (TTFB)

**Step 3: Progressive HTML Streaming**

* Server renders components as they become ready
* HTML is sent in chunks as it's generated
* Browser renders HTML progressively as it arrives

**Step 4: Suspense Boundaries**

* React Suspense allows streaming parts independently
* Fast parts render first, slow parts stream later
* Loading states shown for parts that aren't ready

**Step 5: Complete Rendering**

* All parts eventually stream and render
* Page becomes fully interactive after hydration

### 🔹 React Suspense for Streaming

**Basic Streaming with Suspense:**

```javascript
// Next.js App Router (React 18+)
import { Suspense } from 'react';

async function Page() {
  return (
    <div>
      {/* This renders immediately */}
      <Header />

      {/* This streams when ready */}
      <Suspense fallback={<div>Loading posts...</div>}>
        <Posts /> {/* Slow data fetch */}
      </Suspense>

      {/* This also streams independently */}
      <Suspense fallback={<div>Loading comments...</div>}>
        <Comments /> {/* Another slow data fetch */}
      </Suspense>
    </div>
  );
}

async function Posts() {
  // This might take 2 seconds
  const posts = await fetchPosts();
  return <div>{/* render posts */}</div>;
}

async function Comments() {
  // This might take 3 seconds
  const comments = await fetchComments();
  return <div>{/* render comments */}</div>;
}
```

**How it works:**

* Header renders immediately (no Suspense)
* Posts and Comments stream independently
* User sees header first, then posts, then comments
* Better perceived performance than waiting for everything

### 🔹 Performance Characteristics

**Metrics:**

* **Time to First Byte (TTFB)**: Very fast (50-200ms) - starts sending immediately
* **First Contentful Paint (FCP)**: Fast - content appears progressively
* **Largest Contentful Paint (LCP)**: Depends on when main content streams
* **Time to Interactive (TTI)**: Similar to regular SSR

**Performance Benefits:**

* Faster perceived performance (content appears sooner)
* Better user experience (progressive loading)
* Can show loading states for slow parts
* Doesn't block on slow data sources

**Trade-offs:**

* More complex implementation
* Requires React 18+ and framework support
* Layout shifts possible (content appears progressively)

### 🔹 Characteristics

**Advantages:**

* **Fast Initial Paint**: User sees content start appearing quickly
* **Progressive Enhancement**: Page becomes interactive as parts load
* **Better Perceived Performance**: Feels faster even if total time is same
* **Non-Blocking**: Slow parts don't block fast parts
* **Better UX**: Can show loading states for specific sections

**Disadvantages:**

* **Complex Implementation**: Requires framework support (React 18+)
* **Layout Shifts**: Content appearing progressively can cause layout shifts
* **Hydration Complexity**: More complex hydration process
* **Browser Support**: Requires modern browsers

### 🔹 Use Cases

* **Large Pages**: Pages with lots of content (stream parts independently)
* **Slow Data Sources**: When some data loads slowly (don't block on it)
* **Modern React Apps**: Apps using React 18+ Suspense
* **Dashboard Pages**: Multiple independent data sources
* **Content-Heavy Pages**: Blog posts with multiple sections

### 🔹 Implementation Examples

**Streaming with Multiple Data Sources:**

```javascript
async function Dashboard() {
  return (
    <div>
      <Suspense fallback={<HeaderSkeleton />}>
        <Header />
      </Suspense>

      <div className="grid">
        <Suspense fallback={<StatsSkeleton />}>
          <Stats /> {/* Fast - 200ms */}
        </Suspense>

        <Suspense fallback={<ChartSkeleton />}>
          <Chart /> {/* Slow - 2s */}
        </Suspense>

        <Suspense fallback={<TableSkeleton />}>
          <DataTable /> {/* Very slow - 5s */}
        </Suspense>
      </div>
    </div>
  );
}
```

**Streaming with Error Boundaries:**

```javascript
import { Suspense } from 'react';
import { ErrorBoundary } from 'react-error-boundary';

function ErrorFallback({ error }) {
  return <div>Error loading content: {error.message}</div>;
}

async function Page() {
  return (
    <ErrorBoundary FallbackComponent={ErrorFallback}>
      <Suspense fallback={<div>Loading...</div>}>
        <Content />
      </Suspense>
    </ErrorBoundary>
  );
}
```

📌 **In simple terms**: Streaming SSR is like a buffet that starts serving as soon as some dishes are ready - you don't wait for everything, you start eating while more food arrives. Best for pages with multiple independent data sources where some load faster than others.

---

### 🔹 Partial Hydration

Partial Hydration only hydrates parts of the page that need interactivity, leaving static parts as plain HTML. This reduces JavaScript bundle size and improves performance.

### 🔹 How Partial Hydration Works - Detailed Flow

**Step 1: Server-Side Rendering**

* Server renders entire page to HTML
* All content is in the HTML (including static parts)

**Step 2: HTML Delivery**

* Complete HTML is sent to browser
* Browser can render everything immediately
* No JavaScript needed for static parts

**Step 3: Selective Hydration**

* Only interactive components are hydrated
* Static components remain as plain HTML
* JavaScript is only downloaded for interactive parts

**Step 4: Event Handling**

* Only hydrated components can handle events
* Static parts remain static (no event listeners)
* Smaller JavaScript bundle (only interactive code)

### 🔹 Implementation Approaches

**React Islands Pattern:**

```javascript
// Static HTML (no hydration)
<div class="blog-post">
  <h1>My Blog Post</h1>
  <p>This is static content...</p>
</div>

// Interactive island (hydrated)
<div id="comment-section" data-island="CommentSection">
  {/* This gets hydrated */}
</div>

// JavaScript only for islands
import { hydrateIsland } from 'react-islands';
hydrateIsland('CommentSection', CommentSectionComponent);
```

**Astro Islands (Example):**

```astro
---
// Server Component (runs on server)
const posts = await fetchPosts();
---

<!-- Static HTML (no JavaScript) -->
<div>
  {posts.map(post => (
    <article>
      <h2>{post.title}</h2>
      <p>{post.content}</p>
    </article>
  ))}
</div>

<!-- Interactive Island (hydrated) -->
<CommentSection client:load />
```

### 🔹 Performance Characteristics

**Metrics:**

* **JavaScript Bundle Size**: Significantly smaller (only interactive code)
* **Time to Interactive (TTI)**: Faster (less JavaScript to parse)
* **First Contentful Paint (FCP)**: Fast (HTML has all content)
* **Hydration Time**: Faster (only hydrates interactive parts)

**Performance Benefits:**

* Smaller JavaScript bundles (50-80% reduction possible)
* Faster page load (less JavaScript to download)
* Faster interactivity (less JavaScript to parse)
* Better performance on low-end devices

**Trade-offs:**

* More complex architecture
* Requires framework support
* Static parts can't become interactive later
* Need to identify which parts need interactivity

### 🔹 Characteristics

**Advantages:**

* **Reduced JavaScript**: Smaller bundles, faster load times
* **Better Performance**: Less JavaScript to parse and execute
* **Selective Interactivity**: Only what needs to be interactive gets hydrated
* **Better Mobile Performance**: Less JavaScript = better on slow devices
* **Lower Bandwidth**: Smaller bundles = less data transfer

**Disadvantages:**

* **Framework Support**: Requires framework features (React Islands, Astro, etc.)
* **Complexity**: More complex than full hydration
* **Static Limitations**: Static parts can't become interactive later
* **Architecture**: Need to carefully design which parts are interactive

### 🔹 Use Cases

* **Content-Heavy Sites**: Blogs, documentation (mostly static, few interactive parts)
* **Marketing Sites**: Landing pages (mostly static, few forms/widgets)
* **E-commerce Product Pages**: Product info static, cart/add-to-cart interactive
* **News Sites**: Articles static, comments/interactions interactive
* **Performance-Critical Apps**: Where JavaScript size matters

### 🔹 Implementation Examples

**Identifying Interactive Parts:**

```javascript
// Static component (no hydration)
function BlogPost({ post }) {
  return (
    <article>
      <h1>{post.title}</h1>
      <p>{post.content}</p>
      {/* Static - no JavaScript needed */}
    </article>
  );
}

// Interactive component (needs hydration)
'use client'; // Mark as client component
function CommentSection({ postId }) {
  const [comments, setComments] = useState([]);

  useEffect(() => {
    fetchComments(postId).then(setComments);
  }, [postId]);

  return (
    <div>
      {comments.map(comment => (
        <Comment key={comment.id} comment={comment} />
      ))}
    </div>
  );
}

// Page combines both
function PostPage({ post }) {
  return (
    <div>
      <BlogPost post={post} /> {/* Static */}
      <CommentSection postId={post.id} /> {/* Interactive */}
    </div>
  );
}
```

**Progressive Enhancement:**

```javascript
// Start with static HTML
<div class="product-card">
  <h2>Product Name</h2>
  <p>Description</p>
  <button class="add-to-cart">Add to Cart</button>
</div>

// Enhance with JavaScript (if needed)
if ('interactive' in document.body.dataset) {
  hydrateComponent('add-to-cart', AddToCartButton);
}
```

📌 **In simple terms**: Partial hydration is like only adding batteries to toys that need them - most of the page is just static HTML, only interactive parts get JavaScript. Best for content-heavy sites where most content is static and only a few parts need interactivity.

---

### 🔹 Rendering Pattern Comparison

### 🔹 Performance Comparison

| Pattern | TTFB | FCP | TTI | SEO | Server Load | Bundle Size |
|---------|------|-----|-----|-----|-------------|-------------|
| **CSR** | ⚡⚡⚡ Very Fast | 🐌 Slow | 🐌 Slow | ❌ Poor | ✅ None | ❌ Large |
| **SSR** | 🐌 Slow | ⚡⚡ Fast | ⚡ Moderate | ✅ Excellent | ❌ High | ⚡ Moderate |
| **SSG** | ⚡⚡⚡ Very Fast | ⚡⚡⚡ Very Fast | ⚡⚡ Fast | ✅ Excellent | ✅ None | ⚡ Moderate |
| **ISR** | ⚡⚡⚡ Very Fast | ⚡⚡⚡ Very Fast | ⚡⚡ Fast | ✅ Excellent | ⚡ Low | ⚡ Moderate |
| **Streaming SSR** | ⚡⚡⚡ Very Fast | ⚡⚡ Fast | ⚡ Moderate | ✅ Excellent | ❌ High | ⚡ Moderate |
| **Partial Hydration** | ⚡⚡⚡ Very Fast | ⚡⚡⚡ Very Fast | ⚡⚡⚡ Very Fast | ✅ Excellent | Varies | ✅ Small |

### 🔹 Use Case Matrix

| Use Case | Recommended Pattern | Why |
|----------|-------------------|-----|
| **Blog/Content Site** | SSG or ISR | Mostly static, SEO important |
| **E-commerce Product Pages** | ISR or SSR | Many pages, need freshness |
| **Dashboard/Admin Panel** | CSR | SEO not needed, fast navigation |
| **Marketing Landing Page** | SSG | Static, SEO critical |
| **Social Media Feed** | SSR or Streaming SSR | Dynamic, personalized |
| **Documentation Site** | SSG | Static, SEO important |
| **News Site** | ISR or Streaming SSR | Frequent updates, SEO critical |
| **Real-time App** | CSR | Highly interactive, real-time data |

### 🔹 Decision Tree

```
Do you need SEO?
├─ No → Use CSR (authenticated apps, dashboards)
└─ Yes → Continue
    │
    Is content mostly static?
    ├─ Yes → Use SSG (blogs, docs)
    └─ No → Continue
        │
        Do you have too many pages to pre-render?
        ├─ Yes → Use ISR (e-commerce, large sites)
        └─ No → Continue
            │
            Does content change frequently?
            ├─ Yes → Use SSR or Streaming SSR
            └─ No → Use SSG
```

### 🔹 Hybrid Approaches

**Mix Patterns in One App:**

```javascript
// Next.js example - different patterns for different pages

// SSG for blog posts
// pages/blog/[slug].js
export async function getStaticProps() { /* ... */ }

// SSR for user dashboard
// pages/dashboard.js
export async function getServerSideProps() { /* ... */ }

// CSR for admin panel
// pages/admin.js (no data fetching, client-side only)

// ISR for product pages
// pages/products/[id].js
export async function getStaticProps() {
  return { props: {}, revalidate: 60 };
}
```

**Benefits of Hybrid:**

* Use best pattern for each page
* Optimize performance per route
* Balance SEO, performance, and cost
* Flexibility to change patterns per page

---

## ⭐ Summary — 10-second Interview Version

> "CSR renders in browser (fast nav, slow initial load, poor SEO). SSR renders on server (fast initial, SEO friendly, high server load). SSG pre-renders at build (fastest, best SEO, static only). ISR combines SSG with background updates (fast + fresh). Streaming SSR sends HTML progressively (better perceived performance). Partial hydration only hydrates interactive parts (smaller bundles). Choose based on SEO needs, update frequency, performance requirements, and server costs."

---

## ⭐ Extra Points (If Interviewer Asks More)

### When to use each pattern?

**CSR**: Use for authenticated apps, dashboards, and highly interactive applications where SEO is not a priority. Best when you need fast client-side navigation and rich interactivity.

**SSR**: Use for content sites, e-commerce product pages, and public-facing sites where SEO is critical. Best when you need personalized content per user and always-fresh data.

**SSG**: Use for blogs, documentation sites, marketing pages, and portfolios where content is mostly static. Best when you want the fastest performance and excellent SEO with minimal server costs.

**ISR**: Use for e-commerce sites, news sites, and large content sites with many pages that update periodically. Best when you have too many pages to pre-render but want fast performance.

**Streaming SSR**: Use for large pages with multiple independent data sources where some load faster than others. Best when you want to improve perceived performance by showing content progressively.

**Partial Hydration**: Use for content-heavy sites where most content is static and only a few parts need interactivity. Best when JavaScript bundle size is a concern.

### What is hydration?

Hydration is the process of attaching JavaScript event listeners and making server-rendered HTML interactive. The HTML is already there (from SSR or SSG), and JavaScript "wakes it up" by:

1. **Matching Virtual DOM**: React/Vue matches its virtual DOM to the existing HTML
2. **Attaching Event Listeners**: Event handlers are attached to DOM elements
3. **Initializing State**: Component state is initialized
4. **Making Interactive**: Page becomes fully interactive

**Hydration Mismatch**: If server-rendered HTML doesn't match what client renders, you get a hydration error. Common causes:

* Using browser-only APIs during SSR
* Random values or timestamps
* Different data between server and client

### What's the difference between SSG, SSR, and ISR?

**SSG (Static Site Generation)**:

* Pre-renders at build time
* Same HTML for all users
* Fastest performance (served from CDN)
* Content can be stale (requires rebuild)
* Best for static content

**SSR (Server-Side Rendering)**:

* Renders on each request
* Can personalize per user
* Fresh data always
* Slower TTFB (server processing)
* Higher server costs
* Best for dynamic, personalized content

**ISR (Incremental Static Regeneration)**:

* Pre-renders at build time (like SSG)
* Regenerates in background when stale
* Fast performance (served from cache)
* Fresh data (periodic updates)
* Best of both worlds
* Best for sites with many pages that update occasionally

### How do you optimize rendering performance?

**For CSR:**

* Code splitting (route-based, component-based)
* Lazy loading components
* Bundle optimization (tree shaking, minification)
* Prefetching routes and data
* Service workers for caching

**For SSR:**

* Cache rendered pages (Redis, in-memory)
* Optimize database queries
* Use CDN for static assets
* Implement streaming SSR
* Reduce JavaScript bundle size
* Use edge computing

**For SSG:**

* Optimize build time (parallel page generation)
* Use incremental builds
* Optimize images and assets
* Minimize HTML size
* Use CDN effectively

**For ISR:**

* Choose appropriate revalidate time
* Use on-demand revalidation for critical updates
* Implement tag-based revalidation
* Cache data fetching
* Optimize regeneration time

### What are the trade-offs between patterns?

**Performance vs. Freshness:**

* SSG: Best performance, but stale content
* SSR: Fresh content, but slower performance
* ISR: Good performance + periodic freshness

**SEO vs. Complexity:**

* CSR: Poor SEO, simple implementation
* SSR/SSG: Excellent SEO, more complex
* ISR: Excellent SEO, most complex

**Cost vs. Performance:**

* SSG: Low cost (static hosting), best performance
* SSR: High cost (server needed), good performance
* ISR: Moderate cost, excellent performance

**Scalability vs. Personalization:**

* SSG: Excellent scalability, no personalization
* SSR: Limited scalability, full personalization
* ISR: Good scalability, limited personalization

### How do you handle authentication with different patterns?

**CSR:**

* Token stored in localStorage/sessionStorage
* API calls include token in headers
* Client-side route protection
* Simple implementation

**SSR:**

* Token in cookies (httpOnly for security)
* Server checks authentication
* Can personalize content per user
* Server-side route protection

**SSG:**

* Static pages can't check auth at build time
* Use client-side auth check
* Or use SSR for authenticated pages
* Hybrid approach recommended

**ISR:**

* Similar to SSG for auth
* Use SSR for personalized pages
* ISR for public pages
* Hybrid approach

### What about edge rendering?

Edge rendering runs your rendering code at CDN edge locations (closer to users):

**Benefits:**

* Lower latency (closer to users)
* Better global performance
* Reduced server load
* Faster TTFB

**Limitations:**

* Limited runtime (Edge Runtime)
* Smaller execution time limits
* Limited Node.js APIs
* More constraints

**Use Cases:**

* Middleware (authentication, redirects)
* Edge API routes
* Edge SSR (Next.js Edge Runtime)
* A/B testing at edge

### How do you measure rendering performance?

**Key Metrics:**

* **TTFB (Time to First Byte)**: Time until first byte of response
* **FCP (First Contentful Paint)**: Time until first content appears
* **LCP (Largest Contentful Paint)**: Time until largest content appears
* **TTI (Time to Interactive)**: Time until page is interactive
* **CLS (Cumulative Layout Shift)**: Visual stability
* **FID (First Input Delay)**: Time until first interaction

**Tools:**

* Lighthouse (Chrome DevTools)
* WebPageTest
* Chrome User Experience Report
* Real User Monitoring (RUM)
* Core Web Vitals

### What are common pitfalls?

**CSR Pitfalls:**

* Large JavaScript bundles
* Poor SEO
* Slow initial load
* Blank screen during load

**SSR Pitfalls:**

* High server costs
* Slow TTFB if not optimized
* Hydration mismatches
* Server overload

**SSG Pitfalls:**

* Stale content
* Long build times
* Can't personalize
* Rebuild required for updates

**ISR Pitfalls:**

* Stale content within revalidation window
* Complex cache invalidation
* First request delay (on-demand)
* Cache management complexity

---

### 🔹 ⚛️ Anti-React Patterns

Anti-patterns in React are common mistakes that lead to poor performance, bugs, or hard-to-maintain code. Recognizing and avoiding these patterns is crucial for building quality React applications.

### 🔹 Direct DOM Manipulation

Manipulating the DOM directly bypasses React's virtual DOM and can cause inconsistencies.

### 🔹 The Problem

```javascript
// ❌ Anti-pattern: Direct DOM manipulation
function Component() {
  useEffect(() => {
    document.getElementById('myDiv').innerHTML = 'Updated';
  }, []);

  return <div id="myDiv">Original</div>;
}

```

**Issues:**

* React doesn't know about the change

* Next render will overwrite your changes

* Breaks React's reconciliation

* Can cause state inconsistencies

### 🔹 The Solution

```javascript
// ✅ Correct: Use React state
function Component() {
  const [content, setContent] = useState('Original');

  useEffect(() => {
    setContent('Updated');
  }, []);

  return <div>{content}</div>;
}

```

📌 **In simple terms**: Always allow React to manage the DOM. Direct manipulation breaks React's understanding of what the DOM should look like.

---

### 🔹 Mutating State Directly

Mutating state directly instead of creating new objects/arrays breaks React's change detection.

### 🔹 The Problem

```javascript
// ❌ Anti-pattern: Mutating state
function Component() {
  const [items, setItems] = useState([1, 2, 3]);

  const addItem = () => {
    items.push(4); // Mutating array directly
    setItems(items); // React won't detect change
  };

  return <button onClick={addItem}>Add</button>;
}

```

**Issues:**

* React uses reference equality to detect changes

* Mutating doesn't change the reference

* Component won't re-render

* Can cause stale UI

### 🔹 The Solution

```javascript
// ✅ Correct: Create new array
function Component() {
  const [items, setItems] = useState([1, 2, 3]);

  const addItem = () => {
    setItems([...items, 4]); // New array reference
  };

  return <button onClick={addItem}>Add</button>;
}

```

📌 **In simple terms**: Always create new objects/arrays when updating state. React needs to see a new reference to know something changed.

---

### 🔹 Using Index as Key

Using array index as key can cause bugs when list items are reordered, added, or removed.

### 🔹 The Problem

```javascript
// ❌ Anti-pattern: Index as key
function TodoList({ todos }) {
  return (
    <ul>
      {todos.map((todo, index) => (
        <TodoItem key={index} todo={todo} />
      ))}
    </ul>
  );
}

```

**Issues:**

* Keys should be stable and unique

* Index changes when items are reordered

* React may reuse wrong component instance

* Can cause state bugs and performance issues

### 🔹 The Solution

```javascript
// ✅ Correct: Use stable, unique ID
function TodoList({ todos }) {
  return (
    <ul>
      {todos.map(todo => (
        <TodoItem key={todo.id} todo={todo} />
      ))}
    </ul>
  );
}

```

📌 **In simple terms**: Keys help React identify which items changed. Using index breaks this when items move around. Always use stable, unique IDs.

---

### 🔹 Creating Functions/Objects in Render

Creating new functions or objects in render causes unnecessary re-renders of child components.

### 🔹 The Problem

```javascript
// ❌ Anti-pattern: New function/object in render
function Parent({ items }) {
  return (
    <div>
      {items.map(item => (
        <Child
          onClick={() => handleClick(item)} // New function every render
          style={{ color: 'red' }} // New object every render
        />
      ))}
    </div>
  );
}

```

**Issues:**

* New reference every render

* Child components think props changed

* Causes unnecessary re-renders

* Breaks memoization (React.memo, useMemo)

### 🔹 The Solution

```javascript
// ✅ Correct: Memoize callbacks and objects
function Parent({ items }) {
  const handleClick = useCallback((item) => {
    // Handle click
  }, []);

  const itemStyle = useMemo(() => ({ color: 'red' }), []);

  return (
    <div>
      {items.map(item => (
        <Child
          onClick={() => handleClick(item)}
          style={itemStyle}
        />
      ))}
    </div>
  );
}

```

📌 **In simple terms**: Creating new functions/objects in render breaks memoization. Use useCallback and useMemo to keep stable references.

---

### 🔹 Prop Drilling

Passing props through many component layers makes code hard to maintain.

### 🔹 The Problem

```javascript
// ❌ Anti-pattern: Prop drilling
function App() {
  const user = { name: 'John' };
  return <Page user={user} />;
}

function Page({ user }) {
  return <Header user={user} />;
}

function Header({ user }) {
  return <Profile user={user} />;
}

function Profile({ user }) {
  return <div>{user.name}</div>;
}

```

**Issues:**

* Components in middle don't need the prop

* Hard to refactor

* Makes components less reusable

* Clutters component signatures

### 🔹 The Solution

```javascript
// ✅ Correct: Use Context API
const UserContext = createContext();

function App() {
  const user = { name: 'John' };
  return (
    <UserContext.Provider value={user}>
      <Page />
    </UserContext.Provider>
  );
}

function Profile() {
  const user = useContext(UserContext);
  return <div>{user.name}</div>;
}

```

📌 **In simple terms**: When props need to go through many layers, use Context API instead of passing them through every component.

---

### 🔹 useEffect Without Dependencies

Missing or incorrect dependency arrays in useEffect can cause bugs or infinite loops.

### 🔹 The Problem

```javascript
// ❌ Anti-pattern: Missing dependencies
function Component({ userId }) {
  const [user, setUser] = useState(null);

  useEffect(() => {
    fetchUser(userId).then(setUser);
  }, []); // Missing userId dependency

  return <div>{user?.name}</div>;
}

```

**Issues:**

* Effect doesn't run when dependencies change

* Stale closures (uses old values)

* Can cause bugs and inconsistencies

### 🔹 The Solution

```javascript
// ✅ Correct: Include all dependencies
function Component({ userId }) {
  const [user, setUser] = useState(null);

  useEffect(() => {
    fetchUser(userId).then(setUser);
  }, [userId]); // Include userId

  return <div>{user?.name}</div>;
}

```

📌 **In simple terms**: Always include all values from component scope that the effect uses. ESLint's exhaustive-deps rule helps catch this.

---

### 🔹 Not Cleaning Up Effects

Not cleaning up effects (subscriptions, timers, event listeners) causes memory leaks.

### 🔹 The Problem

```javascript
// ❌ Anti-pattern: No cleanup
function Component() {
  useEffect(() => {
    const interval = setInterval(() => {
      console.log('Tick');
    }, 1000);
    // No cleanup - interval keeps running after unmount
  }, []);

  return <div>Component</div>;
}

```

**Issues:**

* Memory leaks

* Unnecessary work after component unmounts

* Can cause errors if trying to update unmounted component

### 🔹 The Solution

```javascript
// ✅ Correct: Cleanup in return function
function Component() {
  useEffect(() => {
    const interval = setInterval(() => {
      console.log('Tick');
    }, 1000);

    return () => clearInterval(interval); // Cleanup
  }, []);

  return <div>Component</div>;
}

```

📌 **In simple terms**: Always return a cleanup function from useEffect to cancel subscriptions, clear timers, and remove event listeners.

---

## ⭐ Summary — 10-second Interview Version

> "Common React anti-patterns: direct DOM manipulation (use state), mutating state (create new objects), index as key (use stable IDs), functions/objects in render (use useCallback/useMemo), prop drilling (use Context), missing useEffect dependencies (include all), not cleaning up effects (return cleanup function)."

---

## ⭐ Extra Points (If Interviewer Asks More)

### How to avoid these patterns?

Use ESLint with React hooks plugin, follow React best practices, use TypeScript for type safety, and review code regularly. Most modern React tooling will warn about these issues.

### What's the performance impact?

These patterns can cause unnecessary re-renders, memory leaks, and bugs. Following best practices helps you build better performance and maintainability.

---

### 🔹 💡 Anti-JavaScript Patterns

Anti-patterns in JavaScript are common mistakes that lead to bugs, poor performance, or hard-to-maintain code. Understanding these helps write better JavaScript.

### 🔹 Using var Instead of let/const

Using `var` has function scope and hoisting issues that can cause bugs.

### 🔹 The Problem

```javascript
// ❌ Anti-pattern: Using var
for (var i = 0; i < 3; i++) {
  setTimeout(() => {
    console.log(i); // Prints 3, 3, 3 (not 0, 1, 2)
  }, 100);
}

```

**Issues:**

* Function scope (not block scope)

* Hoisted to top of function

* Can be redeclared

* No temporal dead zone

### 🔹 The Solution

```javascript
// ✅ Correct: Use let or const
for (let i = 0; i < 3; i++) {
  setTimeout(() => {
    console.log(i); // Prints 0, 1, 2
  }, 100);
}

```

📌 **In simple terms**: Always use `let` or `const`. `var` has confusing scoping rules that cause bugs. Use `const` by default, `let` when you need to reassign.

---

### 🔹 Not Handling Async Errors

Not handling promise rejections or async errors can cause silent failures.

### 🔹 The Problem

```javascript
// ❌ Anti-pattern: Unhandled promise rejection
async function fetchData() {
  const data = await fetch('/api/data'); // No error handling
  return data.json();
}

fetchData(); // Unhandled rejection if fetch fails

```

**Issues:**

* Errors are swallowed

* Hard to debug

* Can crash Node.js applications

* Poor user experience

### 🔹 The Solution

```javascript
// ✅ Correct: Handle errors
async function fetchData() {
  try {
    const response = await fetch('/api/data');
    if (!response.ok) throw new Error('Failed to fetch');
    return await response.json();
  } catch (error) {
    console.error('Error:', error);
    throw error; // Re-throw or handle appropriately
  }
}

fetchData().catch(error => {
  // Handle error
});

```

📌 **In simple terms**: Always handle async errors with try/catch or .catch(). Unhandled promise rejections can cause issues.

---

### 🔹 Using == Instead of ===

Using loose equality (`==`) can cause unexpected type coercion bugs.

### 🔹 The Problem

```javascript
// ❌ Anti-pattern: Loose equality
if (0 == false) { // true (unexpected!)
  console.log('This runs');
}

if ('' == 0) { // true (unexpected!)
  console.log('This also runs');
}

if (null == undefined) { // true (unexpected!)
  console.log('This too');
}

```

**Issues:**

* Type coercion can cause unexpected results

* Hard to predict behavior

* Can hide bugs

### 🔹 The Solution

```javascript
// ✅ Correct: Strict equality
if (0 === false) { // false (expected)
  // Doesn't run
}

if ('' === 0) { // false (expected)
  // Doesn't run
}

if (null === undefined) { // false (expected)
  // Doesn't run
}

```

📌 **In simple terms**: Always use `===` (strict equality) instead of `==`. It's more predictable and prevents type coercion bugs.

---

### 🔹 Modifying Objects You Don't Own

Modifying built-in prototypes or objects you don't control can cause conflicts.

### 🔹 The Problem

```javascript
// ❌ Anti-pattern: Modifying prototypes
Array.prototype.last = function() {
  return this[this.length - 1];
};

// Can conflict with future JavaScript features
// Can break libraries that expect standard behavior

```

**Issues:**

* Can conflict with future language features

* Can break third-party libraries

* Makes code unpredictable

* Hard to debug

### 🔹 The Solution

```javascript
// ✅ Correct: Create utility functions
function last(array) {
  return array[array.length - 1];
}

// Or use a utility library like Lodash
import { last } from 'lodash';

```

📌 **In simple terms**: Don't modify built-in prototypes. Create utility functions or use libraries instead.

---

### 🔹 Not Using Optional Chaining

Not using optional chaining can cause verbose null/undefined checks.

### 🔹 The Problem

```javascript
// ❌ Anti-pattern: Verbose null checks
function getName(user) {
  if (user && user.profile && user.profile.name) {
    return user.profile.name;
  }
  return 'Unknown';
}

```

**Issues:**

* Verbose and repetitive

* Easy to miss a check

* Hard to read

### 🔹 The Solution

```javascript
// ✅ Correct: Optional chaining
function getName(user) {
  return user?.profile?.name ?? 'Unknown';
}

```

📌 **In simple terms**: Use optional chaining (`?.`) and nullish coalescing (`??`) to safely access nested properties and provide defaults.

---

### 🔹 Creating Functions in Loops

Creating functions in loops without proper closure handling causes bugs.

### 🔹 The Problem

```javascript
// ❌ Anti-pattern: Functions in loops
const buttons = document.querySelectorAll('button');
for (var i = 0; i < buttons.length; i++) {
  buttons[i].addEventListener('click', function() {
    console.log(i); // Always logs buttons.length (wrong!)
  });
}

```

**Issues:**

* All functions share the same variable

* Closure captures the final value

* Doesn't work as expected

### 🔹 The Solution

```javascript
// ✅ Correct: Use let or IIFE
// Option 1: Use let
for (let i = 0; i < buttons.length; i++) {
  buttons[i].addEventListener('click', function() {
    console.log(i); // Correct index
  });
}

// Option 2: Use forEach
buttons.forEach((button, i) => {
  button.addEventListener('click', function() {
    console.log(i); // Correct index
  });
});

```

📌 **In simple terms**: When creating functions in loops, use `let` (creates new binding each iteration) or use `forEach`/`map` which handle this correctly.

---

### 🔹 Not Using Destructuring

Not using destructuring makes code verbose and harder to read.

### 🔹 The Problem

```javascript
// ❌ Anti-pattern: Verbose property access
function processUser(user) {
  const name = user.name;
  const email = user.email;
  const age = user.age;
  // ... many lines
}

```

**Issues:**

* Verbose and repetitive

* Harder to see what properties are used

* More typing

### 🔹 The Solution

```javascript
// ✅ Correct: Use destructuring
function processUser(user) {
  const { name, email, age } = user;
  // ... cleaner code
}

// Or destructure in parameters
function processUser({ name, email, age }) {
  // ... even cleaner
}

```

📌 **In simple terms**: Use destructuring to extract properties from objects and arrays. It's cleaner and more readable.

---

## ⭐ Summary — 10-second Interview Version

> "Common JavaScript anti-patterns: using var (use let/const), not handling async errors (use try/catch), using == (use ===), modifying prototypes (create utilities), verbose null checks (use ?. and ??), functions in loops (use let or forEach), not using destructuring (extract properties cleanly)."

---

## ⭐ Extra Points (If Interviewer Asks More)

### How to avoid these patterns?

Use modern JavaScript features (ES6+), enable strict mode, use linters (ESLint), and follow best practices. Most of these are caught by modern tooling.

### What's the performance impact?

Some patterns (like modifying prototypes) can affect performance. Others mainly affect code quality and maintainability.

---

### 🔹 🟢 Anti-Node.js Patterns

Anti-patterns in Node.js are common mistakes that lead to poor performance, bugs, or security issues. Understanding these helps build better Node.js applications.

### 🔹 Blocking the Event Loop

Running CPU-intensive or synchronous operations blocks the event loop.

### 🔹 The Problem

```javascript
// ❌ Anti-pattern: Blocking operations
app.get('/process', (req, res) => {
  // Synchronous file read blocks event loop
  const data = fs.readFileSync('large-file.txt', 'utf8');

  // CPU-intensive operation blocks event loop
  const result = heavyComputation(data);

  res.json(result);
});

```

**Issues:**

* Blocks entire event loop

* No other requests can be processed

* Poor performance and scalability

* Can cause timeouts

### 🔹 The Solution

```javascript
// ✅ Correct: Use async operations and worker threads
app.get('/process', async (req, res) => {
  // Async file read doesn't block
  const data = await fs.promises.readFile('large-file.txt', 'utf8');

  // CPU-intensive work in worker thread
  const result = await runInWorkerThread(heavyComputation, data);

  res.json(result);
});

```

📌 **In simple terms**: Never block the event loop with synchronous or CPU-intensive operations. Use async I/O and worker threads for heavy computation.

---

### 🔹 Not Handling Errors in Async Code

Not handling errors in async operations can crash your application.

### 🔹 The Problem

```javascript
// ❌ Anti-pattern: Unhandled promise rejection
app.get('/data', (req, res) => {
  fetchData() // No error handling
    .then(data => res.json(data));
  // If fetchData rejects, app crashes
});

```

**Issues:**

* Unhandled promise rejections can crash Node.js

* Poor error handling

* Hard to debug

* Bad user experience

### 🔹 The Solution

```javascript
// ✅ Correct: Always handle errors
app.get('/data', async (req, res) => {
  try {
    const data = await fetchData();
    res.json(data);
  } catch (error) {
    console.error('Error:', error);
    res.status(500).json({ error: 'Internal server error' });
  }
});

```

📌 **In simple terms**: Always handle errors in async code. Use try/catch with async/await or .catch() with promises.

---

### 🔹 Callback Hell

Nesting callbacks deeply makes code hard to read and maintain.

### 🔹 The Problem

```javascript
// ❌ Anti-pattern: Callback hell
fs.readFile('file1.txt', (err, data1) => {
  if (err) return console.error(err);
  fs.readFile('file2.txt', (err, data2) => {
    if (err) return console.error(err);
    fs.writeFile('output.txt', data1 + data2, (err) => {
      if (err) return console.error(err);
      console.log('Done');
    });
  });
});

```

**Issues:**

* Hard to read and maintain

* Error handling is repetitive

* Difficult to debug

* Hard to add more operations

### 🔹 The Solution

```javascript
// ✅ Correct: Use async/await
async function processFiles() {
  try {
    const data1 = await fs.promises.readFile('file1.txt');
    const data2 = await fs.promises.readFile('file2.txt');
    await fs.promises.writeFile('output.txt', data1 + data2);
    console.log('Done');
  } catch (error) {
    console.error('Error:', error);
  }
}

```

📌 **In simple terms**: Use async/await instead of nested callbacks. It's much cleaner and easier to read.

---

### 🔹 Not Using Streams for Large Files

Loading entire files into memory can cause memory issues with large files.

### 🔹 The Problem

```javascript
// ❌ Anti-pattern: Loading entire file
app.get('/download', (req, res) => {
  fs.readFile('large-file.zip', (err, data) => {
    if (err) return res.status(500).send('Error');
    res.send(data); // Entire file in memory
  });
});

```

**Issues:**

* High memory usage

* Can cause out-of-memory errors

* Slow for large files

* Poor performance

### 🔹 The Solution

```javascript
// ✅ Correct: Use streams
app.get('/download', (req, res) => {
  const stream = fs.createReadStream('large-file.zip');
  stream.pipe(res); // Streams data, doesn't load all in memory
});

```

📌 **In simple terms**: Use streams for large files. Streams process data in chunks instead of loading everything into memory.

---

### 🔹 Not Using Environment Variables

Hardcoding configuration values makes code inflexible and insecure.

### 🔹 The Problem

```javascript
// ❌ Anti-pattern: Hardcoded values
const dbConfig = {
  host: 'localhost',
  port: 5432,
  password: 'secret123', // Security risk!
  database: 'myapp'
};

```

**Issues:**

* Can't change config per environment

* Security risk (secrets in code)

* Hard to manage different environments

* Committing secrets to version control

### 🔹 The Solution

```javascript
// ✅ Correct: Use environment variables
require('dotenv').config();

const dbConfig = {
  host: process.env.DB_HOST || 'localhost',
  port: parseInt(process.env.DB_PORT) || 5432,
  password: process.env.DB_PASSWORD, // From .env file
  database: process.env.DB_NAME
};

```

📌 **In simple terms**: Always use environment variables for configuration. Never hardcode secrets or environment-specific values.

---

### 🔹 Not Implementing Graceful Shutdown

Not handling shutdown signals can cause data loss or incomplete operations.

### 🔹 The Problem

```javascript
// ❌ Anti-pattern: No graceful shutdown
const server = app.listen(3000, () => {
  console.log('Server running');
});

// If process is killed, connections are closed abruptly
// Ongoing requests may be lost

```

**Issues:**

* Abrupt shutdown

* Ongoing requests may be lost

* Database connections not closed

* Can cause data corruption

### 🔹 The Solution

```javascript
// ✅ Correct: Graceful shutdown
const server = app.listen(3000, () => {
  console.log('Server running');
});

function gracefulShutdown(signal) {
  console.log(`Received ${signal}, shutting down gracefully`);

  server.close(() => {
    console.log('HTTP server closed');
    // Close database connections, cleanup, etc.
    process.exit(0);
  });

  // Force shutdown after timeout
  setTimeout(() => {
    console.error('Forced shutdown');
    process.exit(1);
  }, 10000);
}

process.on('SIGTERM', () => gracefulShutdown('SIGTERM'));
process.on('SIGINT', () => gracefulShutdown('SIGINT'));

```

📌 **In simple terms**: Always implement graceful shutdown. Close servers and connections properly when the process receives termination signals.

---

### 🔹 Not Using Connection Pooling

Creating new database connections for each request is inefficient.

### 🔹 The Problem

```javascript
// ❌ Anti-pattern: New connection per request
app.get('/users', async (req, res) => {
  const client = new Client(); // New connection
  await client.connect();
  const result = await client.query('SELECT * FROM users');
  await client.end(); // Close connection
  res.json(result.rows);
});

```

**Issues:**

* Inefficient (connection overhead)

* Can exhaust connection limits

* Slow performance

* Poor scalability

### 🔹 The Solution

```javascript
// ✅ Correct: Use connection pool
const pool = new Pool({
  host: process.env.DB_HOST,
  database: process.env.DB_NAME,
  max: 20, // Maximum connections
  idleTimeoutMillis: 30000
});

app.get('/users', async (req, res) => {
  const result = await pool.query('SELECT * FROM users');
  res.json(result.rows);
  // Connection automatically returned to pool
});

```

📌 **In simple terms**: Use connection pooling for databases. It reuses connections instead of creating new ones for each request.

---

## ⭐ Summary — 10-second Interview Version

> "Common Node.js anti-patterns: blocking event loop (use async/worker threads), not handling async errors (use try/catch), callback hell (use async/await), not using streams (use for large files), hardcoded config (use env vars), no graceful shutdown (handle signals), no connection pooling (reuse connections)."

---

## ⭐ Extra Points (If Interviewer Asks More)

### How to identify these patterns?

Use linters, code reviews, and monitoring. Tools like ESLint can catch many of these. Monitor event loop lag and memory usage.

### What's the performance impact?

These patterns can significantly impact performance, scalability, and reliability. Following best practices helps you build better applications.

---

