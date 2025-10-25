# ⚛️ Next.js Interview Notes (2025 Edition)

## 🔵 Section 3 — Data Fetching & Server Actions — Q26-Q40

---

### 26. 🔵 How do you fetch data using the new fetch() in App Router?

**🧠 Concept**

Next.js 14 extends the native fetch() API with automatic caching, request deduplication, and server-side optimizations for data fetching.

**💻 Example**

```jsx
// Basic data fetching
async function getPosts() {
  const response = await fetch('https://api.example.com/posts');
  return response.json();
}

// With caching options
async function getPost(id) {
  const response = await fetch(`https://api.example.com/posts/${id}`, {
    next: { revalidate: 3600 } // Cache for 1 hour
  });
  return response.json();
}

// Component usage
export default async function BlogPage() {
  const posts = await getPosts();
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

- **Automatic Caching** - Built-in request caching and deduplication
- **Server-side Optimization** - Runs on server for better performance
- **Cache Control** - Use next.revalidate for cache management
- **Request Deduplication** - Multiple requests for same data are deduplicated
- **Type Safety** - Full TypeScript support with proper typing

---

### 27. 🔵 How does automatic caching work with fetch() in Next.js 14?

**🧠 Concept**

Next.js 14 provides intelligent caching for fetch requests with automatic request deduplication, persistent caching, and configurable revalidation strategies.

**💻 Example**

```jsx
// Automatic caching (default behavior)
async function getData() {
  const response = await fetch('https://api.example.com/data');
  return response.json();
}

// Cache with revalidation
async function getCachedData() {
  const response = await fetch('https://api.example.com/data', {
    next: { revalidate: 60 } // Revalidate every 60 seconds
  });
  return response.json();
}

// Disable caching
async function getFreshData() {
  const response = await fetch('https://api.example.com/data', {
    cache: 'no-store' // Always fetch fresh data
  });
  return response.json();
}
```

**💬 Explanation + Insight**

- **Request Deduplication** - Multiple components requesting same data share single request
- **Persistent Caching** - Cache persists across requests and builds
- **Revalidation** - Configurable cache invalidation strategies
- **Performance** - Reduces server load and improves response times
- **Flexibility** - Fine-grained cache control per request

---

### 28. 🔵 How do you disable caching for specific fetch requests?

**🧠 Concept**

You can disable caching for specific fetch requests using cache options to ensure fresh data for dynamic content or real-time updates.

**💻 Example**

```jsx
// Disable caching completely
async function getFreshData() {
  const response = await fetch('https://api.example.com/data', {
    cache: 'no-store'
  });
  return response.json();
}

// Disable caching and revalidate
async function getDynamicData() {
  const response = await fetch('https://api.example.com/data', {
    cache: 'no-store',
    next: { revalidate: 0 }
  });
  return response.json();
}
```

**💬 Explanation + Insight**

- **cache: 'no-store'** - Completely disable caching
- **revalidate: 0** - Disable revalidation
- **Dynamic Content** - Use for real-time data that changes frequently
- **Performance Impact** - May increase server load
- **Use Cases** - User-specific data, real-time updates

---

### 29. 🔵 What is the difference between server-side and client-side fetching?

**🧠 Concept**

Server-side fetching runs on the server during rendering for SEO and performance, while client-side fetching runs in the browser for interactive updates.

**💻 Example**

```jsx
// Server-side fetching (default in Server Components)
async function ServerComponent() {
  const data = await fetch('https://api.example.com/data');
  return <div>{data.title}</div>;
}

// Client-side fetching
'use client';
function ClientComponent() {
  const [data, setData] = useState(null);
  
  useEffect(() => {
    fetch('https://api.example.com/data')
      .then(res => res.json())
      .then(setData);
  }, []);
  
  return <div>{data?.title}</div>;
}
```

**💬 Explanation + Insight**

- **Server-side** - Better SEO, faster initial load, no loading states
- **Client-side** - Interactive updates, loading states, user-specific data
- **Performance** - Server-side reduces JavaScript bundle size
- **SEO** - Server-side content is crawlable by search engines
- **Use Cases** - Server for static data, client for dynamic interactions

---

### 30. 🔵 What are revalidate, revalidateTag, and revalidatePath used for?

**🧠 Concept**

These functions control cache invalidation: revalidate for time-based invalidation, revalidateTag for tag-based invalidation, and revalidatePath for path-based invalidation.

**💻 Example**

```jsx
// Time-based revalidation
export async function getStaticProps() {
  return {
    props: { data },
    revalidate: 3600 // Revalidate every hour
  };
}

// Tag-based revalidation
async function updatePost(id, data) {
  await db.post.update({ where: { id }, data });
  revalidateTag('posts');
}

// Path-based revalidation
async function createPost(data) {
  const post = await db.post.create({ data });
  revalidatePath('/posts');
  return post;
}
```

**💬 Explanation + Insight**

- **revalidate** - Time-based cache invalidation
- **revalidateTag** - Invalidate cache by tags
- **revalidatePath** - Invalidate cache by path
- **Selective Invalidation** - Only invalidate what changed
- **Performance** - Avoid full cache rebuilds

---

### 31. 🔵 What is tag-based caching, and how does it help cache invalidation?

**🧠 Concept**

Tag-based caching allows you to group related cache entries with tags and invalidate them selectively, providing fine-grained cache control.

**💻 Example**

```jsx
// Fetch with tags
async function getPosts() {
  const response = await fetch('https://api.example.com/posts', {
    next: { tags: ['posts', 'content'] }
  });
  return response.json();
}

// Invalidate by tag
async function updatePost(id, data) {
  await db.post.update({ where: { id }, data });
  revalidateTag('posts'); // Invalidates all posts cache
}

// Multiple tags
async function getUserPosts(userId) {
  const response = await fetch(`https://api.example.com/users/${userId}/posts`, {
    next: { tags: ['posts', `user-${userId}`] }
  });
  return response.json();
}
```

**💬 Explanation + Insight**

- **Selective Invalidation** - Invalidate only related cache entries
- **Tag Grouping** - Group related data with tags
- **Performance** - Avoid invalidating unrelated cache
- **Flexibility** - Multiple tags per request
- **Maintenance** - Easier cache management

---

### 32. 🔵 What are Server Actions, and how are they different from API routes?

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

**💬 Explanation + Insight**

- **Direct Function Calls** - No need for fetch() or API routes
- **Type Safety** - Full TypeScript support
- **Progressive Enhancement** - Works without JavaScript
- **Simplified Architecture** - Fewer moving parts
- **Better DX** - Easier to maintain and test

---

### 33. 🔵 How do you enable Server Actions in Next.js 14?

**🧠 Concept**

Server Actions are enabled by default in Next.js 14, but you need to mark functions with 'use server' directive and configure them properly.

**💻 Example**

```jsx
// Enable Server Actions in next.config.js
const nextConfig = {
  experimental: {
    serverActions: true
  }
};

// Server Action with 'use server' directive
async function updateUser(formData) {
  'use server';
  const name = formData.get('name');
  const email = formData.get('email');
  
  const user = await db.user.update({
    where: { id: formData.get('id') },
    data: { name, email }
  });
  
  revalidatePath('/users');
  return user;
}
```

**💬 Explanation + Insight**

- **'use server' Directive** - Marks functions as Server Actions
- **Automatic Serialization** - Handles data conversion automatically
- **Form Integration** - Works seamlessly with HTML forms
- **Security** - Server-side validation and sanitization
- **Performance** - Optimized for server-side execution

---

### 34. 🔵 How do you handle form submissions using Server Actions?

**🧠 Concept**

Server Actions integrate seamlessly with HTML forms, providing progressive enhancement and automatic form handling without JavaScript.

**💻 Example**

```jsx
// Server Action for form handling
async function createUser(formData) {
  'use server';
  const name = formData.get('name');
  const email = formData.get('email');
  
  const user = await db.user.create({ data: { name, email } });
  redirect(`/users/${user.id}`);
}

// Form using Server Action
export default function UserForm() {
  return (
    <form action={createUser}>
      <input name="name" type="text" required />
      <input name="email" type="email" required />
      <button type="submit">Create User</button>
    </form>
  );
}
```

**💬 Explanation + Insight**

- **Progressive Enhancement** - Works without JavaScript
- **Automatic Handling** - No need for event handlers
- **FormData API** - Access form data directly
- **Validation** - Server-side validation and error handling
- **Redirects** - Automatic redirects after form submission

---

### 35. 🔵 How do you perform database mutations with Server Actions?

**🧠 Concept**

Server Actions provide a secure way to perform database mutations with server-side validation, error handling, and automatic cache invalidation.

**💻 Example**

```jsx
async function updatePost(id, formData) {
  'use server';
  
  try {
    const title = formData.get('title');
    const content = formData.get('content');
    
    const post = await db.post.update({
      where: { id },
      data: { title, content }
    });
    
    revalidatePath('/posts');
    return { success: true, post };
  } catch (error) {
    return { success: false, error: error.message };
  }
}
```

**💬 Explanation + Insight**

- **Server-side Security** - Database operations run on server
- **Error Handling** - Proper error handling and user feedback
- **Cache Invalidation** - Automatic cache updates after mutations
- **Validation** - Server-side data validation
- **Transactions** - Support for database transactions

---

### 36. 🔵 How do Server Actions compare to API routes?

**🧠 Concept**

Server Actions are simpler than API routes for form handling and mutations, while API routes are better for external integrations and complex request handling.

**💻 Example**

```jsx
// Server Action (simpler)
async function createPost(formData) {
  'use server';
  const post = await db.post.create({ data: formData });
  revalidatePath('/posts');
  return post;
}

// API Route (more complex)
export async function POST(request) {
  const data = await request.json();
  const post = await db.post.create({ data });
  return Response.json(post);
}
```

**💬 Explanation + Insight**

- **Server Actions** - Simpler for forms and mutations
- **API Routes** - Better for external integrations
- **Progressive Enhancement** - Server Actions work without JavaScript
- **Type Safety** - Server Actions have better TypeScript support
- **Use Cases** - Server Actions for forms, API routes for external APIs

---

### 37. 🔵 What is cache() from React, and how is it used in Next.js?

**🧠 Concept**

React's cache() function provides request-scoped memoization for expensive computations and API calls, with automatic deduplication within a single request.

**💻 Example**

```jsx
import { cache } from 'react';

// Cached function
const getCachedUser = cache(async (userId) => {
  const user = await fetch(`https://api.example.com/users/${userId}`);
  return user.json();
});

// Multiple components can share cached data
async function UserProfile({ userId }) {
  const user = await getCachedUser(userId);
  return <div>{user.name}</div>;
}

async function UserAvatar({ userId }) {
  const user = await getCachedUser(userId); // Uses cache
  return <img src={user.avatar} alt={user.name} />;
}
```

**💬 Explanation + Insight**

- **Request-scoped** - Cache lasts for single request
- **Automatic Deduplication** - Same calls are deduplicated
- **Memory Efficient** - Garbage collected after request
- **Type Safe** - Full TypeScript support
- **Performance** - Reduces redundant API calls

---

### 38. 🔵 How do you handle errors in server-side data fetching?

**🧠 Concept**

Server-side error handling involves try-catch blocks, proper error boundaries, and user-friendly error messages for better user experience.

**💻 Example**

```jsx
async function getPost(id) {
  try {
    const response = await fetch(`https://api.example.com/posts/${id}`);
    if (!response.ok) {
      throw new Error('Post not found');
    }
    return await response.json();
  } catch (error) {
    console.error('Error fetching post:', error);
    return null;
  }
}

// Error boundary for Server Components
export default async function PostPage({ params }) {
  const post = await getPost(params.id);
  
  if (!post) {
    return <div>Post not found</div>;
  }
  
  return <article>{post.content}</article>;
}
```

**💬 Explanation + Insight**

- **Try-Catch Blocks** - Handle errors gracefully
- **Error Boundaries** - Isolate errors to specific components
- **User Feedback** - Provide meaningful error messages
- **Logging** - Log errors for debugging
- **Fallbacks** - Provide fallback content for errors

---

### 39. 🔵 How does data streaming work between the server and client?

**🧠 Concept**

Data streaming allows you to send data to the client as it becomes available, improving perceived performance and user experience.

**💻 Example**

```jsx
// Streaming response
export async function GET() {
  const stream = new ReadableStream({
    start(controller) {
      const interval = setInterval(() => {
        controller.enqueue(`data: ${Date.now()}\n\n`);
      }, 1000);
      
      setTimeout(() => {
        clearInterval(interval);
        controller.close();
      }, 10000);
    }
  });
  
  return new Response(stream, {
    headers: { 'Content-Type': 'text/event-stream' }
  });
}
```

**💬 Explanation + Insight**

- **ReadableStream** - Create streaming responses
- **Real-time Data** - Send data as it becomes available
- **Performance** - Improve perceived performance
- **User Experience** - Better loading experience
- **Use Cases** - Real-time updates, large data sets

---

### 40. 🔵 How do you upload files using Server Actions?

**🧠 Concept**

File uploads with Server Actions use FormData to handle multipart/form-data requests and process uploaded files with proper validation.

**💻 Example**

```jsx
async function uploadFile(formData) {
  'use server';
  const file = formData.get('file');
  
  if (!file || file.size === 0) {
    throw new Error('No file provided');
  }
  
  const buffer = await file.arrayBuffer();
  const fileName = `${Date.now()}-${file.name}`;
  
  // Save file to storage
  await saveFile(fileName, buffer);
  
  return { success: true, fileName };
}
```

**💬 Explanation + Insight**

- **FormData Handling** - Process multipart form data
- **File Validation** - Check file type, size, and existence
- **Buffer Processing** - Convert files to buffers for processing
- **Storage** - Save to filesystem or cloud storage
- **Security** - Validate file types and scan for malware

---

*This comprehensive data fetching section covers all essential Next.js data fetching concepts, Server Actions, and caching strategies for building performant applications.*