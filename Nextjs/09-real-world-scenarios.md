# ⚛️ Next.js Interview Notes (2025 Edition)

## ⚙️ Section 9 — Real-World Scenarios & System Design — Q96-Q100

---

### 96. ⚙️ How would you design a CMS or blog using MDX and App Router?

**🧠 Concept**

Building a CMS with MDX involves creating a content management system that processes Markdown with JSX components, using Next.js App Router for dynamic routing and content rendering.

**💻 Example**

```jsx
// app/blog/[slug]/page.js
import { MDXRemote } from 'next-mdx-remote/rsc';

export default async function BlogPost({ params }) {
  const { content, frontmatter } = await getPost(params.slug);
  
  return (
    <article>
      <h1>{frontmatter.title}</h1>
      <MDXRemote source={content} />
    </article>
  );
}
```

**💬 Explanation + Insight**

- **MDX Processing** - Use next-mdx-remote for server-side MDX rendering
- **Dynamic Routing** - Use [slug] routes for blog posts
- **Frontmatter** - Extract metadata from Markdown frontmatter
- **Component Integration** - Embed React components in Markdown
- **SEO Optimization** - Generate meta tags from frontmatter data

---

### 97. ⚙️ How would you handle image uploads and optimization in production?

**🧠 Concept**

Production image handling involves secure upload endpoints, image processing, optimization, and storage solutions with proper validation and security measures.

**💻 Example**

```jsx
// app/api/upload/route.js
export async function POST(request) {
  const formData = await request.formData();
  const file = formData.get('image');
  
  const buffer = await file.arrayBuffer();
  const optimized = await sharp(buffer)
    .resize(1200, 800)
    .webp()
    .toBuffer();
    
  await uploadToS3(optimized);
}
```

**💬 Explanation + Insight**

- **File Validation** - Check file type, size, and security
- **Image Processing** - Use Sharp for optimization and resizing
- **Storage Solutions** - Upload to S3, Cloudinary, or similar services
- **CDN Integration** - Serve images through CDN for performance
- **Security** - Scan for malware and validate file contents

---

### 98. ⚙️ How would you build a multi-tenant SaaS with Next.js (domain/path-based)?

**🧠 Concept**

Multi-tenant SaaS architecture involves tenant isolation, shared infrastructure, and proper data separation using domain-based or path-based tenant identification.

**💻 Example**

```jsx
// middleware.js
export function middleware(request) {
  const hostname = request.headers.get('host');
  const tenant = getTenantFromDomain(hostname);
  
  request.headers.set('x-tenant', tenant);
  return NextResponse.next();
}

// app/dashboard/page.js
export default async function Dashboard() {
  const tenant = headers().get('x-tenant');
  const data = await getTenantData(tenant);
  return <div>Tenant: {tenant}</div>;
}
```

**💬 Explanation + Insight**

- **Tenant Identification** - Use domain or subdomain for tenant detection
- **Data Isolation** - Separate data per tenant in database
- **Middleware** - Add tenant context to all requests
- **Shared Resources** - Use shared infrastructure with tenant isolation
- **Custom Domains** - Support custom domains for enterprise customers

---

### 99. ⚙️ How would you stream or chunk large file downloads?

**🧠 Concept**

Large file streaming involves breaking files into chunks, using streaming responses, and implementing proper download progress tracking for better user experience.

**💻 Example**

```jsx
// app/api/download/route.js
export async function GET(request) {
  const filePath = request.nextUrl.searchParams.get('file');
  
  const stream = new ReadableStream({
    start(controller) {
      const fileStream = fs.createReadStream(filePath);
      fileStream.on('data', chunk => controller.enqueue(chunk));
      fileStream.on('end', () => controller.close());
    }
  });
  
  return new Response(stream);
}
```

**💬 Explanation + Insight**

- **Streaming Responses** - Use ReadableStream for large file handling
- **Chunk Processing** - Break files into manageable chunks
- **Progress Tracking** - Implement download progress indicators
- **Memory Efficiency** - Avoid loading entire files into memory
- **Resume Support** - Support resumable downloads with range requests

---

### 100. ⚙️ What's your deployment and performance checklist for a Next.js app in 2025?

**🧠 Concept**

A comprehensive checklist ensures production readiness with performance optimization, security measures, monitoring, and deployment best practices for Next.js applications.

**💻 Example**

```jsx
// Performance checklist implementation
const checklist = {
  build: ['npm run build', 'bundle analysis', 'lighthouse audit'],
  security: ['env validation', 'auth setup', 'CORS config'],
  monitoring: ['error tracking', 'performance metrics', 'uptime checks']
};
```

**💬 Explanation + Insight**

- **Build Optimization** - Bundle analysis, code splitting, and tree shaking
- **Security Measures** - Authentication, HTTPS, and input validation
- **Performance** - Core Web Vitals, caching, and CDN configuration
- **Monitoring** - Error tracking, performance monitoring, and alerts
- **Deployment** - CI/CD pipeline, environment management, and rollback strategies

---

*This comprehensive real-world scenarios section covers advanced Next.js system design patterns, production challenges, and best practices for building scalable applications.*