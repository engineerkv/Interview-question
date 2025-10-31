# 🧠 5. Architecture & Best Practices (Q38–48)

---

## 38) How do you structure a scalable Next.js App Router project (folders, modules, context)?

Concept:
Organize with `app/` directory, co-located components, and proper separation of concerns.

Example:
```javascript
// Project structure
// app/
//   ├── (auth)/
//   │   ├── login/
//   │   │   └── page.js
//   │   └── register/
```

Deep Insight:
- **App Directory**: Use `app/` for modern Next.js structure
- **Route Groups**: Use `(group)` for organization without URL impact
- **Co-location**: Keep related files together
- **Separation**: Separate concerns (UI, logic, data)
- **Scalability**: Structure for growth and maintenance

---

## 39) What are best practices for data fetching in server components (avoid N+1 requests)?

Concept:
Fetch data at the layout level and pass down to avoid N+1 queries.

Example:
```javascript
// ❌ Anti-pattern: N+1 queries
export default async function PostsList() {
  const posts = await fetch('https://api.example.com/posts');
  const postsData = await posts.json();
  
  return (
```

Deep Insight:
- **N+1 Problem**: Avoid fetching related data in loops
- **Batch Queries**: Fetch all needed data at once
- **Database Joins**: Use database relationships efficiently
- **Caching**: Cache frequently accessed data
- **Performance**: Reduce database round trips

---

## 40) How do you handle authentication (NextAuth.js, middleware, cookies, JWT)?

Concept:
Use NextAuth.js for authentication, middleware for protection, and secure cookies for sessions.

Example:
```javascript
// lib/auth.js
import NextAuth from 'next-auth';
import CredentialsProvider from 'next-auth/providers/credentials';

export const authOptions = {
  providers: [
```

Deep Insight:
- **NextAuth.js**: Popular authentication library for Next.js
- **Middleware**: Protect routes at the edge
- **JWT**: Stateless authentication tokens
- **Cookies**: Secure session storage
- **Providers**: Support for multiple authentication providers

---

## 41) How do you implement role-based access or route protection in middleware?

Concept:
Use middleware to check authentication and roles before allowing access to routes.

Example:
```javascript
// middleware.js
import { withAuth } from 'next-auth/middleware';

export default withAuth(
  function middleware(req) {
    const { pathname } = req.nextUrl;
```

Deep Insight:
- **Middleware**: First line of defense for route protection
- **Role-based**: Check user roles for access control
- **Redirects**: Redirect unauthorized users to login
- **API Protection**: Protect API routes as well
- **Client-side**: Additional protection in components

---

## 42) What are recommended strategies for error handling (error boundaries, error.tsx)?

Concept:
Use `error.tsx` for route-level errors and error boundaries for component errors.

Example:
```javascript
// app/error.tsx - route-level error boundary
'use client';

export default function Error({ error, reset }) {
  return (
    <div>
```

Deep Insight:
- **error.tsx**: Route-level error handling
- **Nested Errors**: Different error handling per route
- **Error Boundaries**: Component-level error handling
- **Recovery**: Provide ways to recover from errors
- **Logging**: Log errors for debugging

---

## 43) How do you handle global state in Next.js 14 (Context, Zustand, React Query)?

Concept:
Use Context for simple state, Zustand for complex state, and React Query for server state.

Example:
```javascript
// Context for simple state
'use client';

import { createContext, useContext, useState } from 'react';

const ThemeContext = createContext();
```

Deep Insight:
- **Context**: Good for simple, rarely changing state
- **Zustand**: Lightweight state management library
- **React Query**: Excellent for server state management
- **Performance**: Choose based on complexity and needs
- **Hydration**: Consider SSR/hydration issues

---

## 44) What is the difference between client-side and server-side state management in the App Router?

Concept:
Server state is managed by Server Components, while client state uses hooks and context.

Example:
```javascript
// Server Component - server-side state
async function ServerComponent() {
  // This data is fetched on the server
  const posts = await fetch('https://api.example.com/posts');
  const data = await posts.json();
  
```

Deep Insight:
- **Server State**: Fetched on server, no JavaScript needed
- **Client State**: Interactive state, requires JavaScript
- **Performance**: Server state is faster for initial load
- **Interactivity**: Client state enables user interactions
- **Hybrid**: Combine both for optimal performance

---

## 45) How do you integrate GraphQL (Apollo, URQL) with server components vs client components?

Concept:
Use GraphQL in Server Components for initial data and client components for mutations.

Example:
```javascript
// Server Component with GraphQL
import { getClient } from '@apollo/experimental-nextjs-app-support/ssr';
import { gql } from '@apollo/client';

const GET_POSTS = gql`
  query GetPosts {
```

Deep Insight:
- **Server Components**: Use for initial data fetching
- **Client Components**: Use for mutations and real-time updates
- **Apollo**: Popular GraphQL client with Next.js support
- **URQL**: Lightweight alternative to Apollo
- **Caching**: GraphQL clients provide sophisticated caching

---

## 46) How do you secure API routes and server actions (CSRF, auth headers, cookies)?

Concept:
Implement CSRF protection, validate authentication, and sanitize inputs.

Example:
```javascript
// API route with security
import { getServerSession } from 'next-auth';
import { authOptions } from '../auth';

export async function GET(request) {
  const session = await getServerSession(authOptions);
```

Deep Insight:
- **Authentication**: Always validate user sessions
- **Input Validation**: Validate and sanitize all inputs
- **CSRF Protection**: Prevent cross-site request forgery
- **Rate Limiting**: Implement rate limiting for API routes
- **Headers**: Use security headers for protection

---

## 47) What is the difference between middleware vs edge functions in terms of lifecycle?

Concept:
Middleware runs on every request, while edge functions run on specific routes.

Example:
```javascript
// Middleware - runs on every request
import { NextResponse } from 'next/server';

export function middleware(request) {
  const { pathname } = request.nextUrl;
  
```

Deep Insight:
- **Middleware**: Runs on every request, good for global logic
- **Edge Functions**: Run on specific routes, good for API endpoints
- **Performance**: Edge functions run closer to users
- **Limitations**: Edge functions have limited APIs
- **Use Cases**: Middleware for auth/redirects, Edge for APIs

---

## 48) How can you combine SSR + ISR + CSR in hybrid rendering strategies?

Concept:
Use different rendering strategies for different parts of the application based on data requirements.

Example:
```javascript
// Hybrid rendering strategy
export default function HybridPage() {
  return (
    <div>
      {/* Static content - SSG */}
      <header>
```

Deep Insight:
- **SSR**: For dynamic, user-specific content
- **ISR**: For content that changes occasionally
- **CSR**: For interactive, client-side features
- **Hybrid**: Combine strategies for optimal performance
- **Suspense**: Use for progressive loading

---
