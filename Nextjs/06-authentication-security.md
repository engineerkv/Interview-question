# ⚛️ Next.js Interview Notes (2025 Edition)

## 🔴 Section 6 — Authentication & Security — Q66-Q75

---

### 66. 🔴 How do you implement authentication in Next.js 14?

**🧠 Concept**

Implement authentication using NextAuth.js v5 (Auth.js) with secure session management and protected routes.

**💻 Example**

```jsx
// app/api/auth/[...nextauth]/route.js
import NextAuth from 'next-auth';
import CredentialsProvider from 'next-auth/providers/credentials';

export const { handlers, auth, signIn, signOut } = NextAuth({
  providers: [
    CredentialsProvider({
      name: 'credentials',
      credentials: {
        email: { label: 'Email', type: 'email' },
        password: { label: 'Password', type: 'password' }
      },
      async authorize(credentials) {
        // Validate credentials
        const user = await validateUser(credentials);
        return user;
      }
    })
  ]
});
```

**💬 Explanation + Insight**

- **NextAuth.js v5** - Modern authentication library for Next.js
- **Session Management** - Secure server-side session handling
- **Provider Support** - Multiple authentication providers
- **Middleware Protection** - Protect routes with middleware
- **Type Safety** - Full TypeScript support

---

### 67. 🔴 How do you protect routes in Next.js?

**🧠 Concept**

Protect routes using middleware, server-side authentication checks, and client-side route guards.

**💻 Example**

```jsx
// middleware.js
import { auth } from '@/auth';

export default auth((req) => {
  if (!req.auth && req.nextUrl.pathname.startsWith('/dashboard')) {
    return Response.redirect(new URL('/login', req.url));
  }
});

// Protected page
import { auth } from '@/auth';

export default async function Dashboard() {
  const session = await auth();
  
  if (!session) {
    redirect('/login');
  }
  
  return <div>Dashboard Content</div>;
}
```

**💬 Explanation + Insight**

- **Middleware Protection** - Server-side route protection
- **Session Validation** - Check authentication status
- **Redirect Handling** - Redirect unauthenticated users
- **Server Components** - Use server-side auth checks
- **Client Protection** - Additional client-side guards

---

### 68. 🔴 How do you implement role-based access control (RBAC)?

**🧠 Concept**

Implement RBAC by checking user roles and permissions in middleware and server components.

**💻 Example**

```jsx
// middleware.js
export default auth((req) => {
  if (req.nextUrl.pathname.startsWith('/admin')) {
    if (!req.auth?.user?.role?.includes('admin')) {
      return Response.redirect(new URL('/unauthorized', req.url));
    }
  }
});

// Role-based component
export default async function AdminPanel() {
  const session = await auth();
  
  if (!session?.user?.role?.includes('admin')) {
    return <div>Access Denied</div>;
  }
  
  return <div>Admin Panel</div>;
}
```

**💬 Explanation + Insight**

- **Role Checking** - Validate user roles in middleware
- **Permission-based Access** - Check specific permissions
- **Server-side Validation** - Validate on server side
- **Client-side Guards** - Additional client-side checks
- **Error Handling** - Proper unauthorized access handling

---

### 69. 🔴 How do you secure API routes in Next.js?

**🧠 Concept**

Secure API routes using authentication middleware, input validation, and proper error handling.

**💻 Example**

```jsx
// app/api/protected/route.js
import { auth } from '@/auth';
import { z } from 'zod';

const schema = z.object({
  name: z.string().min(1),
  email: z.string().email()
});

export async function POST(request) {
  const session = await auth();
  
  if (!session) {
    return Response.json({ error: 'Unauthorized' }, { status: 401 });
  }
  
  const body = await request.json();
  const validatedData = schema.parse(body);
  
  return Response.json({ success: true });
}
```

**💬 Explanation + Insight**

- **Authentication Checks** - Verify user authentication
- **Input Validation** - Validate and sanitize inputs
- **Error Handling** - Proper error responses
- **Rate Limiting** - Implement rate limiting
- **CORS Configuration** - Configure cross-origin requests

---

### 70. 🔴 How do you implement secure cookie storage?

**🧠 Concept**

Implement secure cookie storage using NextAuth.js configuration with proper security settings.

**💻 Example**

```jsx
// auth.config.js
export default {
  session: {
    strategy: 'jwt',
    maxAge: 30 * 24 * 60 * 60 // 30 days
  },
  cookies: {
    sessionToken: {
      name: 'next-auth.session-token',
      options: {
        httpOnly: true,
        sameSite: 'lax',
        path: '/',
        secure: process.env.NODE_ENV === 'production'
      }
    }
  }
};
```

**💬 Explanation + Insight**

- **HTTP-only Cookies** - Prevent XSS attacks
- **Secure Flags** - Use secure flag in production
- **SameSite Policy** - Prevent CSRF attacks
- **Session Strategy** - Choose JWT or database sessions
- **Expiration** - Set appropriate session timeouts

---

### 71. 🔴 How do you prevent CSRF attacks in Next.js?

**🧠 Concept**

Prevent CSRF attacks using SameSite cookies, CSRF tokens, and proper request validation.

**💻 Example**

```jsx
// CSRF protection middleware
export function csrfProtection(req, res, next) {
  if (req.method === 'POST') {
    const token = req.headers['x-csrf-token'];
    const sessionToken = req.cookies['csrf-token'];
    
    if (!token || token !== sessionToken) {
      return res.status(403).json({ error: 'CSRF token mismatch' });
    }
  }
  next();
}

// Client-side CSRF token
const csrfToken = document.querySelector('meta[name="csrf-token"]').content;
fetch('/api/data', {
  method: 'POST',
  headers: {
    'X-CSRF-Token': csrfToken
  }
});
```

**💬 Explanation + Insight**

- **SameSite Cookies** - Prevent cross-site request forgery
- **CSRF Tokens** - Validate request authenticity
- **Request Validation** - Check token in requests
- **Header Validation** - Validate custom headers
- **Origin Checking** - Verify request origin

---

### 72. 🔴 How do you implement rate limiting in Next.js?

**🧠 Concept**

Implement rate limiting using middleware, Redis, or third-party services to prevent abuse.

**💻 Example**

```jsx
// Rate limiting middleware
import { Ratelimit } from '@upstash/ratelimit';
import { Redis } from '@upstash/redis';

const ratelimit = new Ratelimit({
  redis: Redis.fromEnv(),
  limiter: Ratelimit.slidingWindow(10, '1 m')
});

export async function middleware(request) {
  const ip = request.ip ?? '127.0.0.1';
  const { success } = await ratelimit.limit(ip);
  
  if (!success) {
    return new Response('Too Many Requests', { status: 429 });
  }
}
```

**💬 Explanation + Insight**

- **Request Limiting** - Limit requests per time window
- **IP-based Limiting** - Track requests by IP
- **User-based Limiting** - Track requests by user
- **Redis Storage** - Use Redis for distributed rate limiting
- **Sliding Window** - Implement sliding window algorithm

---

### 73. 🔴 How do you implement input validation and sanitization?

**🧠 Concept**

Implement input validation using Zod or similar libraries to validate and sanitize user inputs.

**💻 Example**

```jsx
import { z } from 'zod';

const userSchema = z.object({
  name: z.string().min(1).max(100),
  email: z.string().email(),
  age: z.number().min(0).max(120)
});

export async function POST(request) {
  try {
    const body = await request.json();
    const validatedData = userSchema.parse(body);
    
    // Process validated data
    return Response.json({ success: true });
  } catch (error) {
    return Response.json({ error: 'Invalid input' }, { status: 400 });
  }
}
```

**💬 Explanation + Insight**

- **Schema Validation** - Define validation schemas
- **Type Safety** - Ensure type safety with validation
- **Error Handling** - Handle validation errors
- **Sanitization** - Clean and sanitize inputs
- **XSS Prevention** - Prevent cross-site scripting

---

### 74. 🔴 How do you implement secure file uploads?

**🧠 Concept**

Implement secure file uploads with validation, virus scanning, and proper storage.

**💻 Example**

```jsx
// Secure file upload
import { writeFile } from 'fs/promises';
import { join } from 'path';

export async function POST(request) {
  const formData = await request.formData();
  const file = formData.get('file');
  
  if (!file || file.size > 5 * 1024 * 1024) {
    return Response.json({ error: 'File too large' }, { status: 400 });
  }
  
  const bytes = await file.arrayBuffer();
  const buffer = Buffer.from(bytes);
  
  const path = join(process.cwd(), 'uploads', file.name);
  await writeFile(path, buffer);
  
  return Response.json({ success: true });
}
```

**💬 Explanation + Insight**

- **File Validation** - Validate file type and size
- **Virus Scanning** - Scan uploaded files for malware
- **Secure Storage** - Store files securely
- **Path Traversal** - Prevent directory traversal attacks
- **Content Type** - Validate file content types

---

### 75. 🔴 How do you implement security headers in Next.js?

**🧠 Concept**

Implement security headers using Next.js configuration to protect against common attacks.

**💻 Example**

```jsx
// next.config.js
const nextConfig = {
  async headers() {
    return [
      {
        source: '/(.*)',
        headers: [
          {
            key: 'X-Frame-Options',
            value: 'DENY'
          },
          {
            key: 'X-Content-Type-Options',
            value: 'nosniff'
          },
          {
            key: 'Referrer-Policy',
            value: 'origin-when-cross-origin'
          }
        ]
      }
    ];
  }
};
```

**💬 Explanation + Insight**

- **X-Frame-Options** - Prevent clickjacking attacks
- **X-Content-Type-Options** - Prevent MIME sniffing
- **Referrer-Policy** - Control referrer information
- **Content Security Policy** - Prevent XSS attacks
- **HSTS** - Force HTTPS connections

---

*This comprehensive authentication and security section covers essential Next.js security practices including authentication, authorization, input validation, and security headers for building secure applications.*