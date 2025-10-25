# ⚛️ Next.js Interview Notes (2025 Edition)

## 🟣 Section 8 — Deployment, Edge & CI/CD — Q86-Q95

---

### 86. 🟣 How do you deploy a Next.js 14 app to Vercel?

**🧠 Concept**

Vercel deployment for Next.js 14 involves connecting your repository, configuring build settings, and leveraging Vercel's automatic optimizations for production deployment.

**💻 Example**

```bash
# Install Vercel CLI
npm i -g vercel

# Deploy to Vercel
vercel

# Production deployment
vercel --prod
```

**💬 Explanation + Insight**

- **Automatic Detection** - Vercel detects Next.js and configures build settings
- **Zero Configuration** - Deploy without additional configuration
- **Edge Functions** - Automatic edge function deployment
- **Environment Variables** - Secure environment variable management
- **Preview Deployments** - Automatic previews for pull requests

---

### 87. 🟣 What's the difference between Node.js and Edge deployments?

**🧠 Concept**

Node.js deployments run on traditional serverless functions, while Edge deployments use the Edge Runtime for faster cold starts and global distribution.

**💻 Example**

```jsx
// Node.js runtime (default)
export async function GET() {
  const fs = require('fs');
  return Response.json({ runtime: 'nodejs' });
}

// Edge runtime
export const runtime = 'edge';
export async function GET() {
  return Response.json({ runtime: 'edge' });
}
```

**💬 Explanation + Insight**

- **Cold Start** - Edge has faster cold starts (~0ms vs ~100ms)
- **Memory** - Edge has limited memory (128MB vs 1GB)
- **APIs** - Edge has limited Node.js APIs available
- **Global Distribution** - Edge runs closer to users worldwide
- **Use Cases** - Edge for simple logic, Node.js for complex operations

---

### 88. 🟣 How does Next.js use serverless functions in production?

**🧠 Concept**

Next.js automatically converts API routes and Server Components into serverless functions, enabling automatic scaling and pay-per-use pricing.

**💻 Example**

```jsx
// API route becomes serverless function
export async function GET() {
  return Response.json({ message: 'Serverless function' });
}

// Server Component with serverless execution
export default async function Page() {
  const data = await fetch('https://api.example.com/data');
  return <div>{data.title}</div>;
}
```

**💬 Explanation + Insight**

- **Automatic Conversion** - API routes become serverless functions
- **Scaling** - Functions scale automatically with traffic
- **Pricing** - Pay only for actual usage
- **Cold Starts** - Functions may have cold start delays
- **Stateless** - Functions must be stateless for proper scaling

---

### 89. 🟣 How do you deploy to AWS Lambda or CloudFront?

**🧠 Concept**

AWS deployment involves using the Serverless Framework or AWS CDK to package Next.js apps for Lambda functions and CloudFront distribution.

**💻 Example**

```yaml
# serverless.yml
service: nextjs-app
provider:
  name: aws
  runtime: nodejs18.x
functions:
  app:
    handler: index.handler
    events:
      - http: ANY /
      - http: ANY /{proxy+}
```

**💬 Explanation + Insight**

- **Serverless Framework** - Use serverless.yml for configuration
- **Lambda Functions** - Deploy as Lambda functions
- **CloudFront** - Use CloudFront for global CDN
- **Build Process** - Custom build process for AWS deployment
- **Environment Variables** - Configure AWS-specific environment variables

---

### 90. 🟣 How do you Dockerize a Next.js app?

**🧠 Concept**

Dockerizing Next.js involves creating a Dockerfile with multi-stage builds, optimizing for production, and configuring for containerized deployment.

**💻 Example**

```dockerfile
FROM node:18-alpine AS base
WORKDIR /app
COPY package*.json ./
RUN npm ci --only=production

FROM base AS build
RUN npm ci
COPY . .
RUN npm run build

FROM base AS runner
COPY --from=build /app/.next ./.next
EXPOSE 3000
CMD ["npm", "start"]
```

**💬 Explanation + Insight**

- **Multi-stage Builds** - Separate build and runtime stages
- **Alpine Linux** - Use lightweight Alpine images
- **Production Optimization** - Only include production dependencies
- **Layer Caching** - Optimize Docker layer caching
- **Security** - Use non-root user for security

---

### 91. 🟣 What's the difference between standalone and default Next.js builds?

**🧠 Concept**

Standalone builds create a self-contained application with all dependencies, while default builds require Node.js and dependencies to be installed separately.

**💻 Example**

```js
// next.config.js
const nextConfig = {
  output: 'standalone',
  experimental: {
    outputFileTracingRoot: path.join(__dirname, '../../'),
  },
}
```

**💬 Explanation + Insight**

- **Self-contained** - Standalone includes all dependencies
- **Docker Optimization** - Better for containerized deployments
- **File Size** - Standalone creates larger but complete builds
- **Deployment** - Easier deployment without dependency management
- **Performance** - Faster startup with pre-bundled dependencies

---

### 92. 🟣 How do you manage environment variables securely across environments?

**🧠 Concept**

Environment variable management involves using different values for development, staging, and production with secure storage and access controls.

**💻 Example**

```bash
# .env.local
DATABASE_URL=postgresql://localhost:5432/myapp
NEXTAUTH_SECRET=development-secret

# .env.production
DATABASE_URL=postgresql://prod-server:5432/myapp
NEXTAUTH_SECRET=production-secret
```

**💬 Explanation + Insight**

- **Environment Files** - Use .env files for different environments
- **Secret Management** - Use services like AWS Secrets Manager
- **Access Control** - Limit access to production secrets
- **Validation** - Validate required environment variables
- **Rotation** - Regularly rotate sensitive secrets

---

### 93. 🟣 What are typical CI/CD stages for a Next.js project?

**🧠 Concept**

CI/CD pipelines for Next.js include build, test, lint, security scanning, and deployment stages with proper quality gates and automation.

**💻 Example**

```yaml
# .github/workflows/deploy.yml
name: Deploy
on: [push]
jobs:
  build:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v3
      - uses: actions/setup-node@v3
      - run: npm ci
      - run: npm run build
      - run: npm run test
```

**💬 Explanation + Insight**

- **Build Stage** - Compile and bundle the application
- **Test Stage** - Run unit and integration tests
- **Lint Stage** - Code quality and style checking
- **Security Scan** - Vulnerability scanning
- **Deploy Stage** - Automated deployment to production

---

### 94. 🟣 How do you trigger ISR revalidation in production?

**🧠 Concept**

ISR revalidation can be triggered on-demand through API routes, webhooks, or scheduled jobs to update static content when data changes.

**💻 Example**

```jsx
// app/api/revalidate/route.js
export async function POST(request) {
  const { secret, path } = await request.json();
  
  if (secret !== process.env.REVALIDATE_SECRET) {
    return Response.json({ error: 'Invalid secret' }, { status: 401 });
  }
  
  await revalidatePath(path);
  return Response.json({ revalidated: true });
}
```

**💬 Explanation + Insight**

- **On-demand Revalidation** - Trigger revalidation via API calls
- **Webhook Integration** - Use webhooks from CMS or database
- **Scheduled Jobs** - Use cron jobs for regular revalidation
- **Selective Revalidation** - Revalidate specific pages or paths
- **Performance** - Balance between freshness and performance

---

### 95. 🟣 How do you integrate observability tools like Sentry, Datadog, or LogRocket?

**🧠 Concept**

Observability integration involves adding monitoring, logging, and error tracking to Next.js applications for production monitoring and debugging.

**💻 Example**

```jsx
// sentry.client.config.js
import * as Sentry from '@sentry/nextjs';

Sentry.init({
  dsn: process.env.SENTRY_DSN,
  tracesSampleRate: 1.0,
});

// Error boundary
export default function Error({ error, reset }) {
  Sentry.captureException(error);
  return <div>Something went wrong!</div>;
}
```

**💬 Explanation + Insight**

- **Error Tracking** - Capture and track application errors
- **Performance Monitoring** - Monitor Core Web Vitals and performance
- **User Sessions** - Track user interactions and sessions
- **Custom Metrics** - Add custom business metrics
- **Alerting** - Set up alerts for critical errors and performance issues

---

*This comprehensive deployment section covers all essential Next.js deployment concepts, CI/CD practices, and production monitoring for building scalable applications.*