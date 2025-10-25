
🏗️ Frontend System Design & Architecture Interview Master List (2025 Edition)

🌐 1. Web Architecture & Rendering (1–20)
Focus: Client-server flow, SSR/CSR/ISR, CDN, and rendering pipelines.
What happens when you type a URL into a browser?

Explain the full rendering pipeline — from DNS lookup to pixel paint.

What is DNS, and how does it resolve a domain to an IP?

What is TCP, and what is a TCP 3-way handshake?

How does HTTPS ensure secure data transfer?

Difference between HTTP/1.1, HTTP/2, and HTTP/3.

What is latency, and how can it be minimized in web applications?

What is a CDN, and how does it improve web performance?

What is edge caching, and how does it differ from traditional CDN caching?

What are the different rendering models — CSR, SSR, SSG, ISR, and streaming SSR?

How do you decide between client-side and server-side rendering?

How do browsers parse, construct, and render HTML, CSS, and JS?

What is critical rendering path optimization?

How do prefetch, preload, and preconnect improve performance?

What are Core Web Vitals, and why do they matter in architecture decisions?

What is hydration, and how does it work in SSR frameworks like React/Next.js?

What are edge functions and edge rendering?

What is speculative parsing, and how do browsers use it?

What is TTFB (Time to First Byte), and how can you reduce it?

How does a service worker impact rendering and caching?

⚙️ 2. Application Architecture & Scalability (21–40)
Focus: modularization, code splitting, and scalability.
What are common frontend architecture patterns (MVC, MVVM, Flux)?

How does React’s architecture differ from Angular or Vue?

What is a monolithic frontend, and when does it fail to scale?

What are micro-frontends, and how do they work?

What are the trade-offs of micro-frontends?

How can Module Federation help build scalable frontend systems?

How do you manage shared dependencies in micro-frontends?

What is code splitting, and why is it critical in large apps?

What is lazy loading, and how do you implement it efficiently?

What are bundle splitting and dynamic imports?

What are runtime vs build-time integrations in frontend systems?

What is tree shaking, and how do bundlers (Webpack, Turbopack) handle it?

What is the difference between SPA and MPA architectures?

What are the pros and cons of using an SPA?

What are edge-side includes (ESI), and how do they work?

How would you design a multi-tenant frontend system?

How do you organize a monorepo for multiple frontend projects?

What tools (Nx, Turborepo) help with scalable frontend monorepos?

What are the trade-offs of server components (RSC) in scalability?

What is the role of a design system in scalable architectures?

🧠 3. Data Fetching, Caching & APIs (41–60)
Focus: API strategy, caching, synchronization, and data freshness.
How do REST and GraphQL differ in frontend system design?

What are the pros and cons of GraphQL in large-scale applications?

What is gRPC, and is it suitable for frontend communication?

How do you design caching for REST and GraphQL APIs?

What is stale-while-revalidate (SWR), and when should you use it?

What are cache invalidation strategies (time-based, tag-based)?

How do you handle optimistic updates in data fetching?

How does React Query or SWR improve API caching?

What are edge caches, and how do they differ from browser caches?

How do you handle API retries, rate limiting, and backoff?

What is ETag, and how does conditional caching work?

What is the difference between CDN caching and browser caching?

How do you cache GraphQL queries efficiently?

What is HTTP caching vs application-level caching?

What is the role of service workers in offline-first caching?

How would you implement delta (incremental) data fetching?

How do you cache POST or mutation results securely?

How do you synchronize real-time data between multiple tabs?

What are long polling, Server-Sent Events (SSE), and WebSockets?

How do you ensure consistency between server and client cache layers?

📊 4. Performance, Metrics & Observability (61–85)
Focus: Core Web Vitals, profiling, monitoring, and alerting.
What are the key metrics for frontend performance monitoring?

What are LCP, CLS, INP, FID, and TTFB?

How do you measure Core Web Vitals in production (RUM)?

What are field data vs lab data in performance testing?

How do you set up automated Lighthouse audits in CI/CD?

What is React Profiler, and how does it measure render performance?

What is the Memory tab used for in browser DevTools?

What are long tasks, and how do you identify them?

How do you use the Performance tab in DevTools effectively?

What are performance budgets, and how do you enforce them?

How do you detect memory leaks in React or RN apps?

What is bundle analysis, and how do you optimize bundle size?

What is code coverage, and why does it matter for performance?

How do you measure and fix layout shifts (CLS)?

What are preconnect, preload, and dns-prefetch optimizations?

How do you measure FPS drops and jank?

What is lazy hydration, and how does it help UX?

What tools do you use for frontend observability (Sentry, Datadog, LogRocket)?

How do you integrate Sentry with React or Next.js?

What is Real User Monitoring (RUM), and how does it differ from synthetic monitoring?

How do you monitor slow API calls and correlate them to UI impact?

What are custom performance marks and measures?

How do you alert on performance regressions?

How do you track memory and network usage in production?

What is the role of analytics and metrics in performance-driven architecture?

🧩 5. Frontend Infrastructure, CI/CD & Delivery (86–110)
Focus: build pipelines, deployments, environments, testing, and automation.
What does a typical frontend CI/CD pipeline look like?

How do you automate builds for multiple environments (dev, staging, prod)?

What is the difference between GitHub Actions, CircleCI, and GitLab CI?

What is Canary vs Blue-Green deployment?

How do you automate rollbacks after failed deployments?

What is the difference between incremental builds and cold builds?

What is code splitting in CI/CD pipelines?

How do you manage environment variables securely in CI?

What are secrets managers (AWS Secrets, Vault), and why use them?

How do you handle versioning for shared UI libraries?

What is semantic versioning (semver)?

How do you automate visual regression testing (Percy, Chromatic)?

How do you run Lighthouse or WebPageTest in pipelines?

What is the difference between static and dynamic site hosting?

How does Vercel, Netlify, or Cloudflare handle edge caching and deployment?

How do you dockerize frontend apps for reproducibility?

How do you perform security scans in CI/CD?

What is feature flagging, and how do you use LaunchDarkly or ConfigCat?

What is progressive rollout, and why is it safer?

How do you automate bundle analysis and regression alerts?

What is an artifact repository, and how is it used in frontend builds?

What is incremental static regeneration (ISR), and how does it fit into CI/CD?

What are best practices for build caching in monorepos?

What are pre-commit hooks, and how do you integrate Husky with lint-staged?

What are common bottlenecks in CI/CD pipelines for frontend teams?

🧱 6. UX, Security & Design Systems (111–135)
Focus: accessibility, security, design tokens, theming, and modularity.
What is accessibility (a11y), and why is it essential in frontend design?

What are ARIA attributes, and how are they used?

How do you make web apps keyboard-navigable?

What are WCAG guidelines, and what levels (A, AA, AAA) mean?

How do you ensure contrast and readability in design systems?

What are design tokens, and how do they unify design and code?

How do you manage color, spacing, and typography tokens in CSS?

How does theming work in design systems?

What is CSS-in-JS vs atomic CSS vs utility-first (Tailwind)?

What are the trade-offs of Tailwind vs Styled Components vs CSS Modules?

How do you scale a design system across multiple projects?

What is Storybook, and how does it help component documentation?

What is component-driven development (CDD)?

What is the role of Figma tokens or style dictionaries in design systems?

How do you enforce consistency and linting in UI components?

How do you version and publish UI components as npm packages?

What is code splitting for design system imports?

How do you handle brand theming for white-label apps?

What is cross-brand tokenization in enterprise design systems?

How do you handle a11y testing (axe-core, jest-axe)?

What is XSS, and how can it affect React/Next.js apps?

What is CSRF, and how do you prevent it on the frontend?

How do you prevent DOM-based XSS vulnerabilities?

How do you securely store auth tokens in SPAs?

What are best practices for Content Security Policy (CSP)?

⚡ 7. Real-World System Design Scenarios (136–150)
Focus: applied architecture, scalability, and real-world decision-making.
Design a high-performance dashboard that updates in real-time.

Design an offline-first PWA for a global user base.

Architect a multi-tenant SaaS using Next.js and React.

Design a CDN caching strategy for a content-heavy web app.

Architect a micro-frontend setup using Module Federation.

Design an analytics dashboard that tracks Core Web Vitals.

Build an accessible design system for enterprise teams.

Architect a large e-commerce site with localized content.

Design a dark/light mode theming system with persistence.

Build a front-end system for 10M daily users — what bottlenecks arise?

Design a deployment strategy for low-downtime React apps.

Build an observability setup for frontend performance alerts.

Architect an edge-rendered global app with Cloudflare Workers.

Design a feature flag rollout system for frontend releases.

Optimize a slow SPA — what step-by-step approach do you take?

✅ Final Summary — Frontend System Design (2025 Edition)
Category
Focus
Questions
Web Architecture
Rendering, Protocols, CDN
1–20
App Architecture
Scalability, Micro-frontends
21–40
Data Fetching
APIs, Caching, Revalidation
41–60
Performance
Metrics, Observability, Monitoring
61–85
CI/CD
Delivery, Deployment, Automation
86–110
UX & Security
Accessibility, Tokens, CSP
111–135
Real-World Design
Practical Architecture Scenarios
136–150
