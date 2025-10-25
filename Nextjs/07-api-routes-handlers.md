# ⚛️ Next.js Interview Notes (2025 Edition)

## 🧠 Section 7 — API Routes & Route Handlers — Q76-Q85

---

### 76. 🧠 What are Route Handlers, and how do they replace /pages/api?

**🧠 Concept**

Route Handlers are the App Router's replacement for /pages/api, using file-based routing in the app directory with improved performance and better integration with Server Components.

**💻 Example**

```jsx
// app/api/users/route.js
export async function GET() {
  return Response.json({ users: [] });
}

export async function POST(request) {
  const data = await request.json();
  return Response.json({ created: data });
}
```

**💬 Explanation + Insight**

- **File-based Routing** - API routes defined by file structure in app/api
- **HTTP Methods** - Export functions named after HTTP methods (GET, POST, etc.)
- **Better Performance** - Improved over /pages/api with better caching
- **Server Components** - Seamless integration with App Router features
- **TypeScript Support** - Full type safety with Request and Response objects

---

### 77. 🧠 How do you define GET, POST, PUT, and DELETE handlers?

**🧠 Concept**

Route Handlers export functions named after HTTP methods, each handling specific request types with proper request parsing and response formatting.

**💻 Example**

```jsx
// app/api/posts/route.js
export async function GET(request) {
  const posts = await db.post.findMany();
  return Response.json(posts);
}

export async function POST(request) {
  const data = await request.json();
  const post = await db.post.create({ data });
  return Response.json(post, { status: 201 });
}
```

**💬 Explanation + Insight**

- **Named Exports** - Export functions with HTTP method names
- **Request Parsing** - Use request.json() for POST/PUT data
- **Response Formatting** - Return Response.json() with proper status codes
- **Database Integration** - Direct database access in route handlers
- **Error Handling** - Proper HTTP status codes for different scenarios

---

### 78. 🧠 How do you send JSON or custom responses from a Route Handler?

**🧠 Concept**

Route Handlers use the Response API to send JSON data, custom headers, and different content types with proper HTTP status codes.

**💻 Example**

```jsx
// JSON response
export async function GET() {
  return Response.json({ message: 'Success' });
}

// Custom response with headers
export async function POST(request) {
  const data = await request.json();
  return new Response(JSON.stringify(data), {
    status: 201,
    headers: { 'Content-Type': 'application/json' }
  });
}
```

**💬 Explanation + Insight**

- **Response.json()** - Convenient method for JSON responses
- **Custom Headers** - Set headers for CORS, caching, etc.
- **Status Codes** - Use appropriate HTTP status codes
- **Content Types** - Specify correct content-type headers
- **Error Responses** - Return proper error responses with status codes

---

### 79. 🧠 How do you handle file uploads in Route Handlers?

**🧠 Concept**

File uploads in Route Handlers use FormData parsing to handle multipart/form-data requests and process uploaded files with proper validation.

**💻 Example**

```jsx
export async function POST(request) {
  const formData = await request.formData();
  const file = formData.get('file');
  
  if (!file) {
    return Response.json({ error: 'No file' }, { status: 400 });
  }
  
  const buffer = await file.arrayBuffer();
  // Process file...
}
```

**💬 Explanation + Insight**

- **FormData Parsing** - Use request.formData() for file uploads
- **File Validation** - Check file type, size, and existence
- **Buffer Processing** - Convert files to buffers for processing
- **Storage Options** - Save to filesystem, cloud storage, or database
- **Security** - Validate file types and scan for malware

---

### 80. 🧠 How do you stream responses or use Server-Sent Events (SSE)?

**🧠 Concept**

Streaming responses and SSE enable real-time data delivery using ReadableStream and proper headers for continuous data transmission.

**💻 Example**

```jsx
export async function GET() {
  const stream = new ReadableStream({
    start(controller) {
      const interval = setInterval(() => {
        controller.enqueue(`data: ${Date.now()}\n\n`);
      }, 1000);
    }
  });
  
  return new Response(stream, {
    headers: { 'Content-Type': 'text/event-stream' }
  });
}
```

**💬 Explanation + Insight**

- **ReadableStream** - Create streaming responses for real-time data
- **SSE Headers** - Use text/event-stream content type
- **Data Format** - Follow SSE format with "data:" prefix
- **Connection Management** - Handle client disconnections gracefully
- **Performance** - Efficient for real-time updates and large datasets

---

### 81. 🧠 How do you handle API errors and exceptions?

**🧠 Concept**

Proper error handling in Route Handlers involves try-catch blocks, custom error classes, and appropriate HTTP status codes for different error scenarios.

**💻 Example**

```jsx
export async function POST(request) {
  try {
    const data = await request.json();
    const result = await processData(data);
    return Response.json(result);
  } catch (error) {
    if (error.name === 'ValidationError') {
      return Response.json({ error: error.message }, { status: 400 });
    }
    return Response.json({ error: 'Internal error' }, { status: 500 });
  }
}
```

**💬 Explanation + Insight**

- **Try-Catch Blocks** - Wrap async operations in error handling
- **Custom Errors** - Create specific error types for different scenarios
- **HTTP Status Codes** - Use appropriate status codes (400, 401, 500)
- **Error Logging** - Log errors for debugging and monitoring
- **User-Friendly Messages** - Return meaningful error messages

---

### 82. 🧠 How do you connect to a database inside a Route Handler?

**🧠 Concept**

Database connections in Route Handlers use connection pooling, proper error handling, and environment variables for secure database access.

**💻 Example**

```jsx
import { PrismaClient } from '@prisma/client';

const prisma = new PrismaClient();

export async function GET() {
  try {
    const users = await prisma.user.findMany();
    return Response.json(users);
  } catch (error) {
    return Response.json({ error: 'Database error' }, { status: 500 });
  }
}
```

**💬 Explanation + Insight**

- **Connection Pooling** - Use connection pools for better performance
- **Environment Variables** - Store database URLs in environment variables
- **Error Handling** - Handle database connection errors gracefully
- **Query Optimization** - Use proper indexing and query optimization
- **Security** - Use parameterized queries to prevent SQL injection

---

### 83. 🧠 How do you validate and sanitize input data in APIs?

**🧠 Concept**

Input validation and sanitization prevent security vulnerabilities by validating data types, formats, and sanitizing user input before processing.

**💻 Example**

```jsx
import { z } from 'zod';

const userSchema = z.object({
  name: z.string().min(1).max(100),
  email: z.string().email()
});

export async function POST(request) {
  const data = await request.json();
  const validatedData = userSchema.parse(data);
  // Process validated data...
}
```

**💬 Explanation + Insight**

- **Schema Validation** - Use Zod or similar libraries for validation
- **Input Sanitization** - Clean and sanitize user input
- **Type Safety** - Ensure data types match expectations
- **Security** - Prevent injection attacks and malicious input
- **Error Messages** - Provide clear validation error messages

---

### 84. 🧠 How do you organize API logic for large projects?

**🧠 Concept**

Large API projects require proper organization with service layers, middleware, shared utilities, and clear separation of concerns for maintainability.

**💻 Example**

```jsx
// lib/services/userService.js
export class UserService {
  static async createUser(data) {
    return await db.user.create({ data });
  }
}

// app/api/users/route.js
import { UserService } from '@/lib/services/userService';

export async function POST(request) {
  const data = await request.json();
  const user = await UserService.createUser(data);
  return Response.json(user);
}
```

**💬 Explanation + Insight**

- **Service Layer** - Separate business logic from route handlers
- **Shared Utilities** - Create reusable functions and utilities
- **Middleware** - Use middleware for common functionality
- **Error Handling** - Centralized error handling and logging
- **Testing** - Organize code for easier unit testing

---

### 85. 🧠 How do you enable CORS or rate limiting for specific routes?

**🧠 Concept**

CORS and rate limiting protect APIs by controlling cross-origin access and limiting request frequency using middleware and configuration.

**💻 Example**

```jsx
// middleware.js
export function middleware(request) {
  const response = NextResponse.next();
  response.headers.set('Access-Control-Allow-Origin', '*');
  return response;
}

// Rate limiting
const rateLimit = new Map();
export async function GET(request) {
  const ip = request.ip;
  if (rateLimit.get(ip) > 100) {
    return Response.json({ error: 'Rate limited' }, { status: 429 });
  }
}
```

**💬 Explanation + Insight**

- **CORS Headers** - Set appropriate CORS headers for cross-origin requests
- **Rate Limiting** - Implement request frequency limits per IP/user
- **Middleware** - Use middleware for cross-cutting concerns
- **Security** - Protect against abuse and unauthorized access
- **Configuration** - Make CORS and rate limits configurable

---

*This comprehensive API routes section covers all essential Next.js Route Handler concepts, HTTP methods, and best practices for building robust APIs.*