
⚛️ Next.js 14.x Senior Developer Interview Handbook (2025 Edition)

🟢 1. Core Concepts & Rendering (1–15)
Focus: App Router, React Server Components, Rendering Models
What problems does Next.js solve compared to plain React apps?


What is the App Router in Next.js 14, and how does it differ from the old Pages Router?


What are React Server Components (RSC), and why are they important?


What are Client Components, and when should they be used?


What is the "use client" directive, and what does it control?


What is pre-rendering, and how does it improve SEO and performance?


What is the difference between Static Generation (SSG) and Server-Side Rendering (SSR)?


What is Incremental Static Regeneration (ISR), and how does it work?


What is Streaming SSR, and how does it differ from traditional SSR?


What is Partial Rendering, and how does it improve UX?


How does Next.js decide when to render on the server vs client?


What is Turbopack, and how does it improve build performance?


What are React Server Actions, and how do they replace traditional API routes?


How does Next.js handle component-level caching?


How does the React Compiler optimize Next.js rendering?



🟡 2. Routing & Navigation (16–25)
Focus: App Router structure, layouts, segments, nested routing
How does file-based routing work in the App Router?


What are route segments, and how do they work?


What is the purpose of layout.js, template.js, and page.js files?


What are parallel routes, and how do you use them?


What are intercepting routes, and how do they enable modals or drawers?


What is the difference between nested layouts and templates?


How do you navigate between routes using <Link> and useRouter()?


What is the difference between not-found.js and error.js?


How do you pass data between routes without using query params?


What is dynamic routing, and how do you implement [slug] routes?



🔵 3. Data Fetching & Server Actions (26–40)
Focus: Fetching, caching, mutations, and server data handling
How do you fetch data using the new fetch() in App Router?


How does automatic caching work with fetch() in Next.js 14?


How do you disable caching for specific fetch requests?


What is the difference between server-side and client-side fetching?


What are revalidate, revalidateTag, and revalidatePath used for?


What is tag-based caching, and how does it help cache invalidation?


What are Server Actions, and how are they different from API routes?


How do you enable Server Actions in Next.js 14?


How do you handle form submissions using Server Actions?


How do you perform database mutations with Server Actions?


How do Server Actions compare to API routes?


What is cache() from React, and how is it used in Next.js?


How do you handle errors in server-side data fetching?


How does data streaming work between the server and client?


How do you upload files using Server Actions?



🟣 4. Middleware & Edge Functions (41–50)
Focus: Edge runtime, request interception, custom logic
What is Middleware in Next.js 14?


How does Middleware run before a request completes?


What’s the difference between Middleware and Route Handlers?


What is the Edge Runtime, and why is it faster?


How do you write Middleware for authentication or redirects?


How do you read cookies and headers inside Middleware?


How do you protect specific routes using Middleware logic?


How do you implement rate limiting at the Edge?


How do you serve geo-targeted or A/B content with Middleware?


How does the Edge Runtime differ from Node.js runtime?



🟠 5. Performance & Optimization (51–65)
Focus: Speed, bundling, Core Web Vitals, and resource optimization
How does Next.js automatically optimize performance?


What are Core Web Vitals (LCP, CLS, INP, FID, TTFB)?


How do you measure Core Web Vitals in a Next.js app?


How do you analyze bundle size and reduce JavaScript bloat?


What are render-blocking scripts, and how can you prevent them?


How does next/image optimize image delivery?


What is the difference between <Image> and <img>?


How does next/font improve font loading?


What is code splitting, and how does Next.js handle it?


How do you cache static assets efficiently in production?


What are prefetching and prerendering, and how do they differ?


How does lazy loading work for components and images?


How can you optimize large third-party libraries?


How do you use Lighthouse and React Profiler with Next.js?


How do you enforce performance budgets in CI/CD?



🔴 6. Authentication & Security (66–75)
Focus: Auth.js, RBAC, CSRF, cookies, and best practices
How do you implement authentication in Next.js 14?


What is Auth.js v5, and how does it integrate with App Router?


How do you protect server and client components based on user roles?


How do you secure API routes and Server Actions?


How do you safely store and read cookies on the server?


What is CSRF, and how do you prevent it in Next.js?


How do you configure CORS in Route Handlers or Middleware?


How do you use JWT tokens securely in Next.js?


How do you handle RBAC (Role-Based Access Control)?


How do you safely store environment secrets and API keys?



🧠 7. API Routes & Route Handlers (76–85)
Focus: Custom server logic, streaming, and data APIs
What are Route Handlers, and how do they replace /pages/api?


How do you define GET, POST, PUT, and DELETE handlers?


How do you send JSON or custom responses from a Route Handler?


How do you handle file uploads in Route Handlers?


How do you stream responses or use Server-Sent Events (SSE)?


How do you handle API errors and exceptions?


How do you connect to a database inside a Route Handler?


How do you validate and sanitize input data in APIs?


How do you organize API logic for large projects?


How do you enable CORS or rate limiting for specific routes?



🟣 8. Deployment, Edge & CI/CD (86–95)
Focus: hosting, scaling, observability, automation
How do you deploy a Next.js 14 app to Vercel?


What’s the difference between Node.js and Edge deployments?


How does Next.js use serverless functions in production?


How do you deploy to AWS Lambda or CloudFront?


How do you Dockerize a Next.js app?


What’s the difference between standalone and default Next.js builds?


How do you manage environment variables securely across environments?


What are typical CI/CD stages for a Next.js project?


How do you trigger ISR revalidation in production?


How do you integrate observability tools like Sentry, Datadog, or LogRocket?



⚙️ 9. Real-World Scenarios & System Design (96–100)
Focus: architecture, scalability, production readiness
How would you design a CMS or blog using MDX and App Router?


How would you handle image uploads and optimization in production?


How would you build a multi-tenant SaaS with Next.js (domain/path-based)?


How would you stream or chunk large file downloads?


What’s your deployment and performance checklist for a Next.js app in 2025?



✅ Final Summary — Next.js 14.x Interview Master List (2025 Edition)
Category
Focus
Questions
Core Concepts & Rendering
App Router, Server Components, SSR, ISR
1–15
Routing & Navigation
Layouts, Segments, Parallel Routes
16–25
Data Fetching & Server Actions
Caching, Mutations, Revalidation
26–40
Middleware & Edge
Interception, Runtime, Redirects
41–50
Performance
Optimization, Web Vitals, Code Splitting
51–65
Authentication & Security
Auth.js, RBAC, CSRF
66–75
API & Handlers
REST, Streaming, Validation
76–85
Deployment & CI/CD
Edge, Cloud, Automation
86–95
Real-World & System Design
Scalable architecture
96–100




