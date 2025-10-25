# ⚛️ Next.js Interview Notes (2025 Edition)

## 🟣 Section 4 — Middleware & Edge Functions — Q41-Q50

---

### 41. 🟣 What is Middleware in Next.js 14?

**🧠 Concept**

Middleware in Next.js 14 runs before a request completes, allowing you to modify requests, redirect users, and add custom logic at the edge.

**💻 Example**

```jsx
// middleware.js
import { NextResponse } from 'next/server';

export function middleware(request) {
  const pathname = request.nextUrl.pathname;
  const token = request.cookies.get('auth-token');
  
  if (!token && pathname.startsWith('/dashboard')) {
    return NextResponse.redirect(new URL('/login', request.url));
  }
  
  return NextResponse.next();
}

export const config = {
  matcher: ['/dashboard/:path*', '/api/:path*']
};
```

**💬 Explanation + Insight**

- **Request Interception** - Runs before requests reach your application
- **Authentication** - Check tokens and redirect unauthenticated users
- **A/B Testing** - Serve different content based on user segments
- **Geo-targeting** - Redirect users based on location
- **Performance** - Runs at the edge for faster response times

---

### 42. 🟣 How does Middleware run before a request completes?

**🧠 Concept**

Middleware executes in the Edge Runtime before the request reaches your application, allowing you to intercept, modify, and redirect requests at the network level.

**💻 Example**

```jsx
export function middleware(request) {
  const { pathname } = request.nextUrl;
  
  // Authentication check
  if (pathname.startsWith('/admin')) {
    const token = request.cookies.get('admin-token');
    if (!token) {
      return NextResponse.redirect(new URL('/login', request.url));
    }
  }
  
  // A/B testing
  if (pathname === '/') {
    const variant = Math.random() > 0.5 ? 'A' : 'B';
    const response = NextResponse.next();
    response.cookies.set('ab-variant', variant);
    return response;
  }
  
  return NextResponse.next();
}
```

**💬 Explanation + Insight**

- **Edge Runtime** - Runs closer to users for faster response
- **Request Modification** - Modify headers, cookies, and redirects
- **Early Interception** - Handle requests before they reach your app
- **Performance** - Faster than Node.js runtime
- **Global Distribution** - Runs on edge locations worldwide

---

### 43. 🟣 What's the difference between Middleware and Route Handlers?

**🧠 Concept**

Middleware runs before requests reach your application for authentication and redirects, while Route Handlers are API endpoints that handle specific requests.

**💻 Example**

```jsx
// Middleware - runs before requests
export function middleware(request) {
  const token = request.cookies.get('auth-token');
  if (!token && request.nextUrl.pathname.startsWith('/dashboard')) {
    return NextResponse.redirect(new URL('/login', request.url));
  }
  return NextResponse.next();
}

// Route Handler - handles specific requests
export async function GET(request) {
  const users = await db.user.findMany();
  return Response.json(users);
}
```

**💬 Explanation + Insight**

- **Middleware** - Request interception and modification
- **Route Handlers** - API endpoints for specific requests
- **Execution Order** - Middleware runs before Route Handlers
- **Use Cases** - Middleware for cross-cutting concerns, Route Handlers for business logic
- **Performance** - Middleware is faster, Route Handlers are more flexible

---

### 44. 🟣 What is the Edge Runtime, and why is it faster?

**🧠 Concept**

The Edge Runtime is a lightweight JavaScript runtime optimized for speed and performance, running closer to users with faster cold starts.

**💻 Example**

```jsx
// Edge Runtime configuration
export const config = {
  runtime: 'edge',
  matcher: ['/api/edge/:path*']
};

export default async function handler(request) {
  // ✅ Available in Edge Runtime
  const url = new URL(request.url);
  const headers = request.headers;
  
  // ❌ Not available in Edge Runtime
  // const fs = require('fs');
  // const crypto = require('crypto');
  
  return new Response(JSON.stringify({ message: 'Edge Runtime' }));
}
```

**💬 Explanation + Insight**

- **Faster Cold Starts** - ~0ms vs ~100ms for Node.js
- **Global Distribution** - Runs closer to users worldwide
- **Limited APIs** - No Node.js APIs, smaller memory footprint
- **Performance** - Optimized for speed and efficiency
- **Use Cases** - Authentication, redirects, simple data processing

---

### 45. 🟣 How do you write Middleware for authentication or redirects?

**🧠 Concept**

Authentication middleware involves checking tokens, validating user sessions, and redirecting unauthenticated users, while redirect middleware handles URL changes.

**💻 Example**

```jsx
export async function middleware(request) {
  const { pathname } = request.nextUrl;
  
  // Public routes that don't require authentication
  const publicRoutes = ['/login', '/register', '/'];
  if (publicRoutes.includes(pathname)) {
    return NextResponse.next();
  }
  
  // Check authentication
  const token = request.cookies.get('auth-token');
  if (!token) {
    return NextResponse.redirect(new URL('/login', request.url));
  }
  
  // Add user to headers for the application
  const response = NextResponse.next();
  response.headers.set('x-user-id', token.value);
  return response;
}
```

**💬 Explanation + Insight**

- **Authentication Checks** - Verify tokens and user sessions
- **Redirect Logic** - Redirect unauthenticated users to login
- **Header Modification** - Add user information to headers
- **Route Protection** - Protect specific routes based on authentication
- **Session Management** - Handle session validation and renewal

---

### 46. 🟣 How do you read cookies and headers inside Middleware?

**🧠 Concept**

Middleware can access cookies and headers from incoming requests to make authentication decisions, user targeting, and request modification.

**💻 Example**

```jsx
export function middleware(request) {
  // Get specific cookie
  const authToken = request.cookies.get('auth-token');
  const userPreferences = request.cookies.get('user-preferences');
  
  // Get specific headers
  const userAgent = request.headers.get('user-agent');
  const acceptLanguage = request.headers.get('accept-language');
  
  // Mobile detection
  if (userAgent?.includes('Mobile')) {
    const response = NextResponse.redirect(new URL('/mobile', request.url));
    return response;
  }
  
  // Language detection
  const language = acceptLanguage?.split(',')[0] || 'en';
  const response = NextResponse.next();
  response.headers.set('x-language', language);
  
  return response;
}
```

**💬 Explanation + Insight**

- **Cookie Access** - Read authentication tokens and user preferences
- **Header Access** - Get user agent, language, and other request headers
- **User Targeting** - Make decisions based on user data
- **Request Modification** - Add custom headers to responses
- **Security** - Validate tokens and user sessions

---

### 47. 🟣 How do you protect specific routes using Middleware logic?

**🧠 Concept**

Route protection in middleware involves checking authentication, user roles, and permissions before allowing access to specific routes.

**💻 Example**

```jsx
export function middleware(request) {
  const { pathname } = request.nextUrl;
  const userRole = request.cookies.get('user-role');
  
  // Protected routes
  const protectedRoutes = ['/dashboard', '/admin', '/profile'];
  const isProtected = protectedRoutes.some(route => pathname.startsWith(route));
  
  if (isProtected) {
    const token = request.cookies.get('auth-token');
    if (!token) {
      return NextResponse.redirect(new URL('/login', request.url));
    }
  }
  
  // Admin routes
  if (pathname.startsWith('/admin') && userRole !== 'admin') {
    return NextResponse.redirect(new URL('/unauthorized', request.url));
  }
  
  return NextResponse.next();
}
```

**💬 Explanation + Insight**

- **Route Protection** - Check authentication before allowing access
- **Role-based Access** - Verify user roles and permissions
- **Redirect Logic** - Redirect unauthorized users
- **Security** - Protect sensitive routes and data
- **Performance** - Early authentication checks at the edge

---

### 48. 🟣 How do you implement rate limiting at the Edge?

**🧠 Concept**

Rate limiting at the edge involves tracking request counts per IP address, implementing time windows, and blocking excessive requests.

**💻 Example**

```jsx
const rateLimitMap = new Map();

export function middleware(request) {
  const ip = request.ip || request.headers.get('x-forwarded-for') || 'unknown';
  const now = Date.now();
  const windowMs = 60 * 1000; // 1 minute
  const maxRequests = 100; // 100 requests per minute
  
  let rateLimit = rateLimitMap.get(ip);
  if (!rateLimit) {
    rateLimit = { count: 0, resetTime: now + windowMs };
    rateLimitMap.set(ip, rateLimit);
  }
  
  if (now > rateLimit.resetTime) {
    rateLimit.count = 0;
    rateLimit.resetTime = now + windowMs;
  }
  
  if (rateLimit.count >= maxRequests) {
    return new Response('Rate limit exceeded', { status: 429 });
  }
  
  rateLimit.count++;
  return NextResponse.next();
}
```

**💬 Explanation + Insight**

- **IP Tracking** - Track requests per IP address
- **Time Windows** - Implement sliding window rate limiting
- **Request Counting** - Count requests within time windows
- **Blocking** - Block excessive requests with 429 status
- **Performance** - Edge-based rate limiting is more efficient

---

### 49. 🟣 How do you serve geo-targeted or A/B content with Middleware?

**🧠 Concept**

Geo-targeting and A/B testing in middleware involve detecting user location, assigning test variants, and serving different content based on user segments.

**💻 Example**

```jsx
export function middleware(request) {
  const { pathname } = request.nextUrl;
  const country = request.geo?.country;
  
  // Geo-targeted redirects
  if (pathname === '/pricing') {
    if (country === 'US') {
      return NextResponse.redirect(new URL('/pricing-us', request.url));
    } else if (country === 'EU') {
      return NextResponse.redirect(new URL('/pricing-eu', request.url));
    }
  }
  
  // A/B testing
  if (pathname === '/') {
    const variant = Math.random() > 0.5 ? 'A' : 'B';
    const response = NextResponse.next();
    response.cookies.set('ab-variant', variant, { maxAge: 60 * 60 * 24 });
    return response;
  }
  
  return NextResponse.next();
}
```

**💬 Explanation + Insight**

- **Geo-targeting** - Serve content based on user location
- **A/B Testing** - Assign users to different test variants
- **Cookie Management** - Store user preferences and test assignments
- **Content Personalization** - Customize content for different users
- **Analytics** - Track user behavior and test results

---

### 50. 🟣 How does the Edge Runtime differ from Node.js runtime?

**🧠 Concept**

The Edge Runtime is optimized for speed and performance, while Node.js runtime provides full Node.js API access but with slower cold starts.

**💻 Example**

```jsx
// Edge Runtime (faster, limited APIs)
export const config = { runtime: 'edge' };
export default async function handler(request) {
  // ✅ Available: fetch, URL, Headers, Response
  const url = new URL(request.url);
  return new Response(JSON.stringify({ runtime: 'edge' }));
}

// Node.js Runtime (slower, full APIs)
export default async function handler(request) {
  // ✅ Available: fs, crypto, child_process, all Node.js APIs
  const fs = require('fs');
  const fileContent = fs.readFileSync('./data.json', 'utf8');
  return new Response(JSON.stringify({ content: fileContent }));
}
```

**💬 Explanation + Insight**

- **Cold Start** - Edge: ~0ms, Node.js: ~100ms
- **Memory** - Edge: 128MB, Node.js: 1024MB
- **APIs** - Edge: Limited, Node.js: Full Node.js APIs
- **Performance** - Edge: Faster, Node.js: More flexible
- **Use Cases** - Edge: Simple logic, Node.js: Complex operations

---

*This comprehensive middleware section covers all essential Next.js middleware concepts, edge functions, and advanced request handling for building secure and performant applications.*