---
sidebar_label: "Question Index"
sidebar_position: 0
---
# ⚛️ Next.js Interview Questions

> **Reviewed:** 2026-09 · Modernized for Next.js 15/16 App Router. Legacy (Pages Router) topics are labeled.

68 carefully curated questions covering Next.js fundamentals to advanced deployment strategies. App Router + React Server Components is the default mental model; Pages Router answers are kept (and labeled) because many production apps still use it. Q61–68 are new 2026 additions covering Server/Client boundaries, Server Action security, caching layers, async request APIs, streaming, middleware/`proxy.ts`, PPR/Cache Components, and Pages → App Router migration.

## 📋 Quick Navigation

| Section | Topic | Questions | Difficulty |
|---------|-------|-----------|------------|
| [1️⃣](#1-fundamentals) | Fundamentals & Setup | Q1–10 | ⭐⭐ |
| [2️⃣](#2-data-fetching--rendering) | Data Fetching & Rendering | Q11–20, Q61–64 | ⭐⭐⭐ |
| [3️⃣](#3-routing--navigation) | Routing & Navigation | Q21–27, Q65–66 | ⭐⭐⭐ |
| [4️⃣](#4-performance--optimization) | Performance & Optimization | Q28–37, Q67 | ⭐⭐⭐⭐ |
| [5️⃣](#5-architecture--best-practices) | Architecture & Patterns | Q38–48 | ⭐⭐⭐⭐ |
| [6️⃣](#6-deployment--tooling) | Deployment & DevOps | Q49–60, Q68 | ⭐⭐⭐⭐⭐ |

## ⚛️ 1. Fundamentals & Setup

1. Next.js and how it differs from React

2. Core features of Next.js (SSR, SSG, ISR, App Router, Edge)

3. Creating a new Next.js project

4. Difference between Pages Router and App Router

5. File-based routing in Next.js

6. Dynamic and catch-all routes

7. Purpose of `_app.tsx`, `_document.tsx` (legacy), and `layout.tsx`

8. `public/` folder and its usage

9. `next/link` prefetching

10. Handling environment variables in Next.js

## 🌐 2. Data Fetching & Rendering

11. Different rendering strategies in Next.js

12. Difference between `getStaticProps` and `getServerSideProps` (Pages Router, legacy)

13. `getStaticPaths` and when to use it (Pages Router, legacy)

14. Implementing data fetching in App Router

15. React Server Components (RSC)

16. Caching and revalidation with `fetch()`

17. Revalidation tags and how to use them

18. Implementing on-demand revalidation

19. Fallback mechanism in ISR (Pages Router, legacy)

20. Difference between API routes and Server Actions

**New (2026):**

61. 🆕 Server vs Client Component boundaries (`'use client'`)

62. 🆕 Server Actions and security

63. 🆕 Caching layers in the App Router (and what changed in Next 15/16)

64. 🆕 Async Request APIs in Next.js 15+ (`params`, `searchParams`, `cookies()`, `headers()`)

## 🧭 3. Routing & Navigation

21. Nested routing in App Router

22. Parallel Routes and how to use them

23. Intercepting Routes and how to use them

24. Handling `not-found.tsx` and `error.tsx`

25. Using `loading.tsx` for loading states

26. Using `useRouter()` and `router.push()`

27. Implementing redirects and rewrites

**New (2026):**

65. 🆕 Streaming with `loading.tsx` and Suspense boundaries

66. 🆕 Middleware (`proxy.ts`) vs Route Handlers

## ⚡ 4. Performance & Optimization

28. Optimizing images with `next/image`

29. Implementing code splitting and lazy loading

30. Using `next/script` for third-party scripts

31. Core Web Vitals and how to optimize them

32. How SWC improves build performance

33. Implementing streaming in SSR

34. Different caching strategies in Next.js

35. Optimizing fonts and CSS in Next.js

36. Monitoring performance in Next.js applications

37. Common performance anti-patterns to avoid

**New (2026):**

67. 🆕 Partial Prerendering (PPR) and Cache Components

## 🏗️ 5. Architecture & Patterns

38. Structuring a scalable Next.js project

39. Implementing authentication in Next.js

40. Handling global state management

41. Implementing error handling and error boundaries

42. Handling side effects in Next.js

43. Implementing role-based access control

44. Integrating GraphQL with Next.js

45. Securing API routes and Server Actions

46. Implementing middleware vs edge functions

47. Implementing hybrid rendering strategies

48. Common Next.js anti-patterns to avoid

## 🚀 6. Deployment & DevOps

49. Deploying Next.js applications to Vercel

50. Creating custom servers for Next.js

51. Different build output types

52. Handling environment-specific settings

53. Integrating ESLint and TypeScript

54. Setting up CI/CD for Next.js applications

55. Implementing static export (`output: 'export'`; `exportPathMap` is legacy)

56. Debugging and profiling Next.js applications

57. Implementing partial prerendering and streaming

58. Using Turbopack for faster development

59. Migrating from Next.js 12 to Next.js 14

60. Best practices for Next.js deployment

**New (2026):**

68. 🆕 Migrating from Pages Router to App Router

---

## 📖 Complete Answer Guide

- [1) Fundamentals & Setup](./01-fundamentals-and-setup.md) - Q1-10

- [2) Data Fetching & Rendering](./02-data-fetching-and-rendering.md) - Q11-20, Q61-64

- [3) Routing & Navigation](./03-routing-and-navigation.md) - Q21-27, Q65-66

- [4) Performance & Optimization](./04-performance-and-optimization.md) - Q28-37, Q67

- [5) Architecture & Best Practices](./05-architecture-and-patterns.md) - Q38-48

- [6) Deployment & Tooling](./06-deployment-and-devops.md) - Q49-60, Q68

For how Next.js works under the hood, see [Next.js Internals](../architecture/10-next-js-internals.md).

## 📝 Cheatsheet

[Next.js Interview Cheatsheet](./cheatsheet.md) - Quick reference guide
