# ⚛️ Next.js Interview Cheatsheet

> **⏱️ Review Time: 15-20 minutes** | **Priority: ⭐⭐ Medium** | Quick reference for Next.js interviews
> 
> **Coverage: Q1-Q60** (60 questions across 6 topics)

**Quick Review Checklist:**
- [ ] Next.js Basics (App Router, Server/Client Components)
- [ ] Data Fetching (SSR, SSG, ISR, Server Components)
- [ ] Routing & Navigation (Dynamic Routes, Link Component)
- [ ] Performance (Image Optimization, Code Splitting, Scripts)
- [ ] API Routes & Server Actions
- [ ] Authentication (NextAuth.js, Middleware)
- [ ] Deployment (Vercel, Docker, Build Output)

---

## 📋 **Question Coverage**

- **Q1-Q10**: Fundamentals
- **Q11-Q20**: Data Fetching & Rendering
- **Q21-Q27**: Routing & Navigation
- **Q28-Q37**: Performance & Optimization
- **Q38-Q48**: Architecture & Best Practices
- **Q49-Q60**: Deployment & Tooling

---

## 📋 **Next.js Basics**

| Concept | Description | Example |
|---------|-------------|---------|
| **App Router** | Modern routing system (Next 13+) | `app/page.js` → `/` |
| **Server Components** | Run on server, no JavaScript sent | `async function Component()` |
| **Client Components** | Run in browser, use hooks | `'use client'` |
| **SSR** | Server-side rendering | `getServerSideProps` |
| **SSG** | Static site generation | `getStaticProps` |
| **ISR** | Incremental static regeneration | `revalidate: 60` |

---

## 🏗️ **Project Structure**

### **App Router Structure**
```javascript
// app/
//   ├── layout.js          // Root layout
//   ├── page.js            // Home page
//   ├── (auth)/            // Route group
//   │   ├── login/
//   │   │   └── page.js
//   │   └── register/
//   │       └── page.js
//   ├── dashboard/
//   │   ├── layout.js      // Nested layout
//   │   ├── page.js
//   │   └── settings/
//   │       └── page.js
//   ├── api/
//   │   └── users/
//   │       └── route.js
//   ├── components/
//   │   └── ui/
//   │       └── Button.js
//   └── lib/
//       └── auth.js
```

### **Pages Router Structure (Legacy)**
```javascript
// pages/
//   ├── _app.js            // App wrapper
//   ├── _document.js       // HTML document
//   ├── index.js           // Home page
//   ├── about.js           // About page
//   ├── blog/
//   │   ├── index.js
//   │   └── [slug].js      // Dynamic route
//   └── api/
//       └── users.js
```

---

## 🔄 **Data Fetching**

### **App Router (Modern)**
```javascript
// Server Component - async function
async function ServerComponent() {
  const data = await fetch('https://api.example.com/data');
  const posts = await data.json();
  
  return (
    <div>
      {posts.map(post => (
        <div key={post.id}>{post.title}</div>
      ))}
    </div>
  );
}

// Client Component - useEffect
'use client';

import { useState, useEffect } from 'react';

function ClientComponent() {
  const [data, setData] = useState(null);
  
  useEffect(() => {
    fetch('/api/data')
      .then(res => res.json())
      .then(setData);
  }, []);
  
  return <div>{data?.message}</div>;
}
```

### **Pages Router (Legacy)**
```javascript
// SSG - Static Site Generation
export async function getStaticProps() {
  const data = await fetch('https://api.example.com/data');
  const posts = await data.json();
  
  return {
    props: { posts },
    revalidate: 3600 // ISR
  };
}

// SSR - Server Side Rendering
export async function getServerSideProps() {
  const data = await fetch('https://api.example.com/data');
  const posts = await data.json();
  
  return { props: { posts } };
}

// Dynamic routes
export async function getStaticPaths() {
  const posts = await fetch('https://api.example.com/posts');
  const data = await posts.json();
  
  const paths = data.map(post => ({
    params: { id: post.id.toString() }
  }));
  
  return { paths, fallback: 'blocking' };
}
```

---

## 🧭 **Routing & Navigation**

### **App Router Navigation**
```javascript
import Link from 'next/link';
import { useRouter } from 'next/navigation';

// Link component
<Link href="/about">About</Link>
<Link href="/blog/[slug]" as="/blog/my-post">My Post</Link>

// Programmatic navigation
const router = useRouter();
router.push('/about');
router.replace('/login');
router.back();
```

### **Dynamic Routes**
```javascript
// app/blog/[slug]/page.js
export default function BlogPost({ params }) {
  return <h1>Post: {params.slug}</h1>;
}

// app/blog/[...slug]/page.js - Catch-all
export default function BlogCatchAll({ params }) {
  return <h1>Blog: {params.slug.join('/')}</h1>;
}

// app/blog/[[...slug]]/page.js - Optional catch-all
export default function BlogOptional({ params }) {
  if (params.slug) {
    return <h1>Blog: {params.slug.join('/')}</h1>;
  }
  return <h1>Blog Home</h1>;
}
```

---

## ⚡ **Performance Optimization**

### **Image Optimization**
```javascript
import Image from 'next/image';

// Basic usage
<Image
  src="/hero.jpg"
  alt="Hero image"
  width={800}
  height={600}
/>

// Responsive image
<Image
  src="/responsive.jpg"
  alt="Responsive"
  width={800}
  height={600}
  sizes="(max-width: 768px) 100vw, 50vw"
/>

// Priority loading
<Image
  src="/above-fold.jpg"
  alt="Above fold"
  width={800}
  height={600}
  priority
/>
```

### **Code Splitting**
```javascript
import dynamic from 'next/dynamic';

// Lazy loading
const LazyComponent = dynamic(() => import('./HeavyComponent'));

// With loading state
const LazyComponent = dynamic(
  () => import('./HeavyComponent'),
  { loading: () => <p>Loading...</p> }
);

// Disable SSR
const ClientOnlyComponent = dynamic(
  () => import('./ClientOnlyComponent'),
  { ssr: false }
);
```

### **Script Optimization**
```javascript
import Script from 'next/script';

// After interactive
<Script
  src="https://www.googletagmanager.com/gtag/js?id=GA_MEASUREMENT_ID"
  strategy="afterInteractive"
/>

// Before interactive
<Script
  src="https://polyfill.io/v3/polyfill.min.js"
  strategy="beforeInteractive"
/>

// Lazy onload
<Script
  src="https://example.com/analytics.js"
  strategy="lazyOnload"
/>
```

---

## 🔧 **API Routes**

### **App Router API Routes**
```javascript
// app/api/users/route.js
export async function GET() {
  const users = await getUsers();
  return Response.json(users);
}

export async function POST(request) {
  const body = await request.json();
  const user = await createUser(body);
  return Response.json(user, { status: 201 });
}

// Edge runtime
export const runtime = 'edge';

export async function GET() {
  return Response.json({ message: 'Hello from edge!' });
}
```

### **Pages Router API Routes (Legacy)**
```javascript
// pages/api/users.js
export default function handler(req, res) {
  if (req.method === 'GET') {
    res.json({ users: [] });
  } else if (req.method === 'POST') {
    res.status(201).json({ message: 'User created' });
  }
}
```

---

## 🎯 **Server Actions**

```javascript
// Server Action
'use server';

export async function createPost(formData) {
  const title = formData.get('title');
  const content = formData.get('content');
  
  const post = await db.posts.create({
    title,
    content
  });
  
  revalidatePath('/posts');
  return post;
}

// Using Server Action
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

---

## 🎨 **Styling**

### **CSS Modules**
```javascript
// styles.module.css
.container {
  max-width: 1200px;
  margin: 0 auto;
}

// Component
import styles from './styles.module.css';

export default function Component() {
  return <div className={styles.container}>Content</div>;
}
```

### **Styled JSX**
```javascript
export default function Component() {
  return (
    <div>
      <style jsx>{`
        .container {
          max-width: 1200px;
          margin: 0 auto;
        }
      `}</style>
      <div className="container">Content</div>
    </div>
  );
}
```

### **Tailwind CSS**
```javascript
export default function Component() {
  return (
    <div className="max-w-4xl mx-auto p-4">
      <h1 className="text-2xl font-bold">Title</h1>
    </div>
  );
}
```

---

## 🔐 **Authentication**

### **NextAuth.js**
```javascript
// lib/auth.js
import NextAuth from 'next-auth';
import CredentialsProvider from 'next-auth/providers/credentials';

export const authOptions = {
  providers: [
    CredentialsProvider({
      name: 'credentials',
      credentials: {
        email: { label: 'Email', type: 'email' },
        password: { label: 'Password', type: 'password' }
      },
      async authorize(credentials) {
        const user = await validateUser(credentials);
        return user;
      }
    })
  ],
  callbacks: {
    async jwt({ token, user }) {
      if (user) token.id = user.id;
      return token;
    },
    async session({ session, token }) {
      session.user.id = token.id;
      return session;
    }
  }
};

export default NextAuth(authOptions);
```

### **Middleware Protection**
```javascript
// middleware.js
import { withAuth } from 'next-auth/middleware';

export default withAuth(
  function middleware(req) {
    // Additional logic
  },
  {
    callbacks: {
      authorized: ({ token }) => !!token
    }
  }
);

export const config = {
  matcher: ['/dashboard/:path*', '/admin/:path*']
};
```

---

## 📊 **State Management**

### **Context API**
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

export function useTheme() {
  return useContext(ThemeContext);
}
```

### **Zustand**
```javascript
import { create } from 'zustand';

const useStore = create((set) => ({
  count: 0,
  increment: () => set((state) => ({ count: state.count + 1 })),
  decrement: () => set((state) => ({ count: state.count - 1 }))
}));

export default function Counter() {
  const { count, increment, decrement } = useStore();
  
  return (
    <div>
      <p>Count: {count}</p>
      <button onClick={increment}>+</button>
      <button onClick={decrement}>-</button>
    </div>
  );
}
```

---

## 🚀 **Deployment**

### **Vercel Deployment**
```bash
# Install Vercel CLI
npm i -g vercel

# Deploy
vercel

# Production deployment
vercel --prod
```

### **Docker Deployment**
```dockerfile
FROM node:18-alpine AS base
WORKDIR /app
COPY package*.json ./
RUN npm ci --only=production

FROM base AS deps
RUN npm ci

FROM base AS builder
COPY . .
COPY --from=deps /app/node_modules ./node_modules
RUN npm run build

FROM base AS runner
ENV NODE_ENV production
COPY --from=builder /app/.next/standalone ./
COPY --from=builder /app/.next/static ./.next/static
COPY --from=builder /app/public ./public

EXPOSE 3000
CMD ["node", "server.js"]
```

---

## 🎯 **Interview Tips**

### **Common Questions**
1. **App Router vs Pages Router** - Modern vs legacy routing
2. **Server Components vs Client Components** - When to use each
3. **Data Fetching** - SSR, SSG, ISR strategies
4. **Performance** - Image optimization, code splitting
5. **Authentication** - NextAuth.js, middleware protection

### **Key Concepts**
- **Server Components**: Run on server, no JavaScript sent
- **Client Components**: Run in browser, use hooks
- **App Router**: Modern routing with better performance
- **Performance**: Image optimization, code splitting, caching
- **Deployment**: Vercel, Docker, static export

### **Best Practices**
- Use Server Components when possible
- Optimize images with next/image
- Implement proper error handling
- Use TypeScript for better development experience
- Follow Next.js conventions and patterns

---

## ⚡ **Last-Minute Review (5 minutes)**

### **Must-Know Concepts**
- **App Router**: Modern routing (Next 13+), file-based routing
- **Server Components**: Run on server, no JavaScript sent (default)
- **Client Components**: Use `'use client'` for hooks, interactivity
- **Data Fetching**: Server Components can be async, fetch directly
- **SSR/SSG/ISR**: Server-side rendering, static generation, incremental regeneration

### **Quick Code Snippets**
```javascript
// Server Component (default)
async function ServerComponent() {
  const data = await fetch('https://api.example.com/data');
  return <div>{data.title}</div>;
}

// Client Component
'use client';
function ClientComponent() {
  const [state, setState] = useState(0);
  return <button onClick={() => setState(s => s + 1)}>{state}</button>;
}

// Image Optimization
<Image src="/hero.jpg" width={800} height={600} alt="Hero" priority />
```

### **Common Gotchas**
- Server Components can't use hooks or browser APIs
- Client Components must have `'use client'` directive
- App Router uses `async` components for data fetching
- Image component requires width/height (or fill with parent)

*Remember: Focus on App Router (Next 13+), Server Components, and modern Next.js features for 2025 interviews!*
