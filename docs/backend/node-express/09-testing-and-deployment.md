---
sidebar_label: "Testing & Deployment"
---
# 🧪 9. Testing & Deployment (Q89–103)

> **Reviewed:** 2026-09 · Modernized; legacy topics are labeled.

---

## Q89. 🧪 Writing unit tests with Jest or Mocha

Testing frameworks provide tools for writing and running tests - Jest is popular for React/Node.js with built-in mocking, Mocha is flexible with many plugins, and Supertest is specialized for HTTP API testing. Choose based on project requirements and team preferences, and consider testing pyramid: unit > integration > e2e.

- **Trade-offs**: Jest: popular for React/Node.js with built-in mocking - Mocha: flexible testing framework with many plugins. Supertest: specialized for HTTP API testing - choose based on project requirements and team preferences. Consider testing pyramid: unit > integration > e2e - Jest is great for all-in-one, Mocha is more flexible, but watch out - too many tests can slow development, so focus on critical paths.

Example:

```javascript
const request = require('supertest');
const app = require('../app');

describe('User API', () => {
  test('GET /api/users should return users', async () => {
    const response = await request(app)
      .get('/api/users')
      .expect(200);

    expect(response.body).toHaveProperty('users');
    expect(Array.isArray(response.body.users)).toBe(true);
  });

  test('POST /api/users should create user', async () => {
    const userData = { name: 'John', email: 'john@example.com' };
    const response = await request(app)
      .post('/api/users')
      .send(userData)
      .expect(201);

    expect(response.body).toHaveProperty('id');
    expect(response.body.name).toBe(userData.name);
  });
});

```

**2026 view:** Node now ships a stable built-in test runner, `node:test` (stable since Node 20), with `describe`/`it`, hooks, mocking (`mock.fn`, `mock.method`, mock timers), watch mode (`node --test --watch`) and several reporters - so small and medium backends often need no test framework dependency at all. **Vitest** is popular for ESM/TypeScript projects because it's fast and Jest-compatible. Jest is still widespread, but its ESM support has historically needed extra configuration. See Q99 for a `node:test` example.

## Q90. 🧪 Testing API endpoints with Supertest

Supertest allows testing Express applications by making HTTP requests and asserting responses - test middleware in isolation, test both success and error cases, use proper HTTP status code assertions, test request/response modifications, and consider edge cases and error scenarios. Tests both routes and middleware behavior.

- **Trade-offs**: Test middleware in isolation - test both success and error cases. Use proper HTTP status code assertions - test request/response modifications. Consider edge cases and error scenarios - makes API testing easy, but watch out - tests should be independent and not rely on shared state.

Example:

```javascript
const request = require('supertest');
const express = require('express');

function authMiddleware(req, res, next) {
  if (req.headers.authorization) {
    req.user = { id: 1, name: 'John' };
    next();
  } else {
    res.status(401).json({ error: 'Unauthorized' });
  }
}

describe('Auth Middleware', () => {
  test('should allow access with valid token', async () => {
    const app = express();
    app.get('/protected', authMiddleware, (req, res) => {
      res.json({ user: req.user });
    });

    const response = await request(app)
      .get('/protected')
      .set('Authorization', 'Bearer token')
      .expect(200);

    expect(response.body.user).toBeDefined();
  });

  test('should reject access without token', async () => {
    const app = express();
    app.get('/protected', authMiddleware, (req, res) => {
      res.json({ user: req.user });
    });

    await request(app)
      .get('/protected')
      .expect(401);
  });
});

```

## Q91. 🧪 Mocking API calls in tests

Mocking external API calls prevents tests from making real network requests - mock external dependencies to isolate units under test, use jest.mock() for automatic mocking, test both success and error scenarios, verify mock calls with correct parameters, and consider using MSW for more realistic API mocking. Makes tests faster, more reliable, and independent of external services.

- **Trade-offs**: Mock external dependencies to isolate units under test - use jest.mock() for automatic mocking. Test both success and error scenarios - verify mock calls with correct parameters. Consider using MSW for more realistic API mocking - essential for unit tests, but watch out - mocks can drift from real APIs, so update them when APIs change.

Example:

```javascript
const axios = require('axios');
const { getWeatherData } = require('../services/weather');

jest.mock('axios');
const mockedAxios = axios;

describe('Weather Service', () => {
  beforeEach(() => {
    jest.clearAllMocks();
  });

  test('should fetch weather data', async () => {
    const mockWeatherData = {
      temperature: 25,
      condition: 'sunny'
    };

    mockedAxios.get.mockResolvedValue({
      data: mockWeatherData
    });

    const result = await getWeatherData('London');

    expect(mockedAxios.get).toHaveBeenCalledWith(
      'https://api.weather.com/v1/current',
      { params: { city: 'London' } }
    );
    expect(result).toEqual(mockWeatherData);
  });

  test('should handle API errors', async () => {
    mockedAxios.get.mockRejectedValue(new Error('API Error'));

    await expect(getWeatherData('London')).rejects.toThrow('API Error');
  });
});

```

If your code uses the built-in `fetch` instead of axios, `jest.mock('axios')` doesn't apply. Options: **MSW** (Mock Service Worker, which intercepts requests at the network layer in Node too), undici's `MockAgent`, or stubbing `globalThis.fetch` with `mock.method(globalThis, 'fetch', ...)` from `node:test`. Network-level mocking is less brittle because it doesn't care which HTTP client you use.

## Q92. 🐛 Debugging Node.js applications with VS Code

Debugging Node.js applications involves setting breakpoints, inspecting variables, and stepping through code - use --inspect flag to enable debugging, set breakpoints in VS Code or Chrome DevTools, use debugger statement for programmatic breakpoints, inspect variables and call stack, and debug async code and promises. Use integrated debuggers in VS Code or Chrome DevTools.

- **Trade-offs**: Use --inspect flag to enable debugging - set breakpoints in VS Code or Chrome DevTools. Use debugger statement for programmatic breakpoints - inspect variables and call stack. Debug async code and promises - powerful debugging tools, but watch out - debugging adds overhead, so don't use in production unless necessary.

Example:

```javascript
const express = require('express');
const app = express();

app.get('/api/users', (req, res) => {
  const userId = req.query.id;

  debugger;

  if (!userId) {
    return res.status(400).json({ error: 'User ID required' });
  }

  console.log('User ID:', userId);

  const user = getUserById(userId);

  res.json({ user });
});

function getUserById(id) {
  debugger;
  return { id, name: 'John Doe' };
}

```

In VS Code, the quickest route is a **JavaScript Debug Terminal** (or the "Auto Attach" setting): any `node` command you run there attaches automatically, including test runners and `node --watch`. For TypeScript, make sure source maps are enabled (`--enable-source-maps`) so breakpoints map to `.ts` files.

## Q93. 🐛 Debugging with Chrome DevTools

Chrome DevTools can attach to a Node process over the inspector protocol - start Node with `--inspect` (or `--inspect-brk` to pause on the first line), open `chrome://inspect`, and click "inspect" on your target. You get the same tools as for the browser: breakpoints and conditional breakpoints, async stack traces, the console in the process context, the **Performance** panel for CPU profiles, and the **Memory** panel for heap snapshots and allocation timelines.

- **Trade-offs**: Great for CPU profiling and memory leak hunting, because heap snapshot comparison makes it easy to see what keeps growing. The inspector listens on `127.0.0.1:9229` by default - never bind it to `0.0.0.0` on a public host, since anyone who can reach the port can run code in your process. In containers or remote servers, use an SSH tunnel or `kubectl port-forward`. Heap snapshots pause the process and can use a lot of memory, so be careful in production.

Example:

```bash
# Start with the inspector (pause before the first line)
node --inspect-brk server.js

# Attach to an already-running process (Linux/macOS)
kill -USR1 <pid>

# Remote container: forward the port instead of exposing it
kubectl port-forward pod/api-7f9c 9229:9229

# Non-interactive alternatives
node --cpu-prof server.js      # writes a .cpuprofile you can load in DevTools
node --heapsnapshot-signal=SIGUSR2 server.js
```

---

## Q94. 🔧 Implementing CI/CD for Node.js applications

CI/CD pipelines automate testing, building, and deploying Node.js applications - automate testing on every commit, test against multiple Node.js versions, run linting and security checks, deploy only after successful tests, and use environment-specific configurations. Ensures code quality and consistent deployments.

- **Trade-offs**: Automate testing on every commit - test against multiple Node.js versions. Run linting and security checks - deploy only after successful tests. Use environment-specific configurations - essential for quality, but watch out - CI/CD can be slow, so optimize pipeline speed and use caching.

Example:

```yaml
name: CI/CD Pipeline

on:
  push:
    branches: [ main, develop ]
  pull_request:
    branches: [ main ]

jobs:
  test:
    runs-on: ubuntu-latest
    strategy:
      matrix:
        node-version: [22.x, 24.x] # supported LTS lines (Node 16/18/20 are end-of-life)
    steps:
    - uses: actions/checkout@v4
    - name: Use Node.js ${{ matrix.node-version }}
      uses: actions/setup-node@v4
      with:
        node-version: ${{ matrix.node-version }}
        cache: 'npm'
    - name: Install dependencies
      run: npm ci
    - name: Run tests
      run: npm test
    - name: Run linting
      run: npm run lint
    - name: Build application
      run: npm run build

  deploy:
    needs: test
    runs-on: ubuntu-latest
    if: github.ref == 'refs/heads/main'
    steps:
    - uses: actions/checkout@v4
    - name: Deploy to production
      run: |
        echo "Deploying to production..."

```

Modern additions worth mentioning: run `npm audit` or a dependency scanner (Dependabot, Renovate, Snyk), generate an SBOM and sign images for supply-chain security, deploy with OIDC-federated cloud credentials instead of long-lived secrets, and roll out gradually (canary or blue-green) with automatic rollback on failing health checks. See the DevOps section's [Git, Docker, CI/CD, Tooling](../../devops/ci-cd-and-releases/01-git-docker-ci-cd-tooling.md) chapter for more.

## Q95. 💡 Containerizing Node.js applications with Docker

Docker containers package Node.js applications with their dependencies - use multi-stage builds for smaller images, use .dockerignore to exclude unnecessary files, run as non-root user for security, implement health checks, and use specific Node.js versions for consistency. Ensures consistent deployment across different environments.

- **Trade-offs**: Use multi-stage builds for smaller images - use .dockerignore to exclude unnecessary files. Run as non-root user for security - implement health checks. Use specific Node.js versions for consistency - makes deployment consistent, but watch out - Docker adds complexity, so use it when you need consistency across environments.

Example:

```dockerfile
FROM node:24-alpine

WORKDIR /app

COPY package*.json ./

RUN npm ci --omit=dev

COPY . .

# The official node image already ships a non-root "node" user
USER node

EXPOSE 3000

# Alpine images don't include curl by default; use Node itself for the check
HEALTHCHECK --interval=30s --timeout=3s --start-period=5s --retries=3 \
  CMD node -e "fetch('http://localhost:3000/health').then(r=>process.exit(r.ok?0:1)).catch(()=>process.exit(1))"

# Run node directly (not npm start) so SIGTERM reaches your process
CMD ["node", "app.js"]

```

In more detail: Docker containerization packages Node.js applications with all dependencies into portable containers - create Dockerfile with Node.js base image, copy application files, install dependencies, expose ports, and set startup command. Enables consistent deployments across environments and simplifies deployment process.

- **Trade-offs**: Packages app with all dependencies - enables consistent deployments across environments. Simplifies deployment process - containers are portable and isolated. Easy to scale and manage - great for CI/CD pipelines, but watch out - Docker images can be large, so use multi-stage builds and .dockerignore to optimize size. Pin the base image to a supported LTS line (`node:24-alpine` or `node:22-slim`; ideally pin by digest), since Node 18 and 20 are end-of-life. `npm ci --only=production` is the old flag - use `--omit=dev`.

Example:

```dockerfile

# Dockerfile

FROM node:24-alpine

WORKDIR /app

# Copy package files

COPY package*.json ./

# Install dependencies

RUN npm ci --omit=dev

# Copy application files

COPY . .

# Create non-root user

RUN addgroup -g 1001 -S nodejs && \
    adduser -S nodejs -u 1001
USER nodejs

# Expose port

EXPOSE 3000

# Health check

HEALTHCHECK --interval=30s --timeout=3s \
  CMD node healthcheck.js

# Start application

CMD ["node", "app.js"]

```

```dockerfile

# .dockerignore

node_modules
npm-debug.log
.git
.env
coverage

```

```bash

# Build image

docker build -t myapp:latest .

# Run container

docker run -p 3000:3000 --env-file .env myapp:latest

# Multi-stage build for smaller images

FROM node:24-alpine AS builder
WORKDIR /app
COPY package*.json ./
RUN npm ci
COPY . .
RUN npm run build

FROM node:24-alpine
ENV NODE_ENV=production
WORKDIR /app
COPY package*.json ./
RUN npm ci --omit=dev
COPY --from=builder /app/dist ./dist
USER node
CMD ["node", "dist/app.js"]

```

## Q96. 🔧 Implementing graceful shutdowns in production

Graceful shutdowns ensure applications close properly by handling termination signals, cleaning up resources, and finishing ongoing requests - handle SIGTERM and SIGINT signals, close HTTP server and database connections, set timeout for forced shutdown, log shutdown process for debugging, and test graceful shutdown in production.

- **Trade-offs**: Handle SIGTERM and SIGINT signals - close HTTP server and database connections. Set timeout for forced shutdown - log shutdown process for debugging. Test graceful shutdown in production - essential for production, but watch out - graceful shutdown can take time, so set appropriate timeouts.

Example:

```javascript
const express = require('express');
const app = express();

let server;

function gracefulShutdown(signal) {
  console.log(`Received ${signal}. Starting graceful shutdown...`);

  server.close(() => {
    console.log('HTTP server closed');

    if (db) {
      db.close(() => {
        console.log('Database connection closed');
        process.exit(0);
      });
    } else {
      process.exit(0);
    }
  });

  // Force shutdown after timeout
  setTimeout(() => {
    console.error('Could not close connections in time, forcefully shutting down');
    process.exit(1);
  }, 30000);
}

process.on('SIGTERM', () => gracefulShutdown('SIGTERM'));
process.on('SIGINT', () => gracefulShutdown('SIGINT'));

server = app.listen(3000, () => {
  console.log('Server running on port 3000');
});

```

## Q97. 💡 Handling environment configurations

Environment-specific configurations ensure applications behave correctly across different environments - use environment variables for sensitive data, provide default values for development, validate required environment variables, use different configurations per environment, and never commit secrets to version control. Use environment variables and configuration files.

- **Trade-offs**: Use environment variables for sensitive data - provide default values for development. Validate required environment variables - use different configurations per environment. Never commit secrets to version control - essential for multi-environment deployments, but watch out - managing configs can be complex, so use tools like dotenv and config validation.

Example:

```javascript
// Legacy: require('dotenv').config();  Modern: node --env-file=.env app.js

const config = {
  development: {
    port: process.env.PORT || 3000,
    db: {
      host: process.env.DB_HOST || 'localhost',
      port: process.env.DB_PORT || 5432,
      name: process.env.DB_NAME || 'myapp_dev'
    },
    jwt: {
      secret: process.env.JWT_SECRET || 'dev-secret',
      expiresIn: '24h'
    }
  },

  production: {
    port: process.env.PORT,
    db: {
      host: process.env.DB_HOST,
      port: process.env.DB_PORT,
      name: process.env.DB_NAME
    },
    jwt: {
      secret: process.env.JWT_SECRET,
      expiresIn: '1h'
    }
  }
};

// Validate required environment variables
const requiredEnvVars = ['DB_HOST', 'DB_PORT', 'JWT_SECRET'];
requiredEnvVars.forEach(varName => {
  if (!process.env[varName] && process.env.NODE_ENV === 'production') {
    throw new Error(`Missing required environment variable: ${varName}`);
  }
});

const env = process.env.NODE_ENV || 'development';
module.exports = config[env];

```

A more robust modern pattern is to validate the whole config once at startup with a schema, so missing or malformed values fail fast with a clear message and the result is typed:

```javascript
import { z } from 'zod';

const Env = z.object({
  NODE_ENV: z.enum(['development', 'test', 'production']).default('development'),
  PORT: z.coerce.number().int().default(3000),
  DATABASE_URL: z.string().url(),
  JWT_SECRET: z.string().min(32),
});

export const env = Env.parse(process.env); // throws on startup if invalid
```

Also avoid fallback secrets like `'dev-secret'` that can silently reach production.

## Q98. 💡 Deploying Node.js applications to the cloud

Cloud deployment involves packaging applications, configuring infrastructure, and using platform-specific services - choose platform based on requirements, configure environment variables, set up proper build and start commands, consider serverless vs traditional hosting, and implement health checks and monitoring. For hosting Node.js applications.

- **Trade-offs**: Choose platform based on requirements - configure environment variables. Set up proper build and start commands - consider serverless vs traditional hosting. Implement health checks and monitoring - many options available, but watch out - each platform has different requirements, so choose based on your needs and budget.

Example:

```javascript
// AWS Lambda (Serverless)
const serverless = require('serverless-http');
const express = require('express');
const app = express();

app.get('/api/users', (req, res) => {
  res.json({ users: [] });
});

module.exports.handler = serverless(app);

// Heroku (package.json)
{
  "scripts": {
    "start": "node app.js",
    "build": "npm install"
  },
  "engines": {
    "node": "24.x"
  }
}

// Vercel (vercel.json) - legacy "builds" config; current Vercel projects
// usually rely on zero-config detection instead
{
  "version": 2,
  "builds": [
    {
      "src": "app.js",
      "use": "@vercel/node"
    }
  ],
  "routes": [
    {
      "src": "/(.*)",
      "dest": "app.js"
    }
  ]
}

// Health check endpoint
app.get('/health', (req, res) => {
  const health = {
    status: 'OK',
    timestamp: new Date().toISOString(),
    uptime: process.uptime(),
    memory: process.memoryUsage(),
    version: process.version
  };

  res.json(health);
});

app.use((req, res, next) => {
  const start = Date.now();

  res.on('finish', () => {
    const duration = Date.now() - start;
    console.log(`${req.method} ${req.url} ${res.statusCode} ${duration}ms`);
  });

  next();
});

process.on('uncaughtException', (error) => {
  console.error('Uncaught Exception:', error);
  process.exit(1);
});

process.on('unhandledRejection', (reason, promise) => {
  console.error('Unhandled Rejection:', reason);
});

```

Deployment notes for 2026: common targets are containers on a managed platform (ECS/Fargate, Cloud Run, Kubernetes, Fly.io, Render, Railway) or serverless functions (AWS Lambda has Node 22 and 24 runtimes). Heroku's free tier was removed in 2022, so it's no longer the default "hello world" host. Keep `/health` cheap and don't expose memory details publicly - split **liveness** (process is up) from **readiness** (dependencies reachable). For AWS specifics see [AWS Cloud Architecture](../../devops/cloud/01-aws-cloud-architecture.md).

---

## Q99. 🧪 Using the built-in `node:test` runner

Node ships a built-in test runner in the `node:test` module (stable since Node 20), so you can write and run tests with zero dependencies - `node --test` finds files like `*.test.js` / `test/**`, runs them in parallel processes, and prints TAP or spec output. It includes `describe`/`it`/`test`, `before`/`after` hooks, subtests, `mock.fn()` / `mock.method()` / mock timers, `--test-only`, `--test-name-pattern`, and watch mode. Pair it with `node:assert/strict` for assertions.

- **Trade-offs**: No install, no config, fast startup and native ESM support - great for libraries and backend services. Compared with Jest or Vitest, the ecosystem (matchers, snapshot tooling, IDE integrations) is smaller, and some features such as coverage (`--experimental-test-coverage`) have carried an experimental label - check the docs for your Node version. Supertest works with it unchanged, since Supertest is framework-agnostic.

Example:

```javascript
// test/users.test.js
import { describe, it, before, mock } from 'node:test';
import assert from 'node:assert/strict';
import request from 'supertest';
import { buildApp } from '../src/app.js';

describe('GET /api/users/:id', () => {
  let app;
  before(() => { app = buildApp({ userRepo: { findById: mock.fn(async (id) => ({ id, name: 'Ada' })) } }); });

  it('returns the user', async () => {
    const res = await request(app).get('/api/users/42').expect(200);
    assert.deepEqual(res.body, { id: '42', name: 'Ada' });
  });

  it('uses fake timers', (t) => {
    t.mock.timers.enable({ apis: ['setTimeout'] });
    let fired = false;
    setTimeout(() => { fired = true; }, 1000);
    t.mock.timers.tick(1000);
    assert.equal(fired, true);
  });
});
```

```bash
node --test                     # run all tests
node --test --watch             # re-run on change
node --test --test-reporter=spec --test-name-pattern="returns"
```

---

## Q100. ⚡ Modern Node.js runtime features that replace common dependencies

Node 22 and 24 (the current LTS lines in 2026; Node 20 reached end-of-life in April 2026) include features that used to need third-party packages. Know which ones are stable, because interviewers like to probe that.

- **Built-in `fetch`, `Request`, `Response`, `FormData`, `WebSocket` client** - `fetch` is backed by undici and stable since Node 21, replacing `node-fetch`/`request` (the `request` package is deprecated). The global `WebSocket` client is available unflagged since Node 22.
- **`node --watch`** - restarts on file changes; stable since Node 22. Replaces nodemon for most cases.
- **`node --env-file=.env`** and `process.loadEnvFile()` - loads .env files without `dotenv` (added in Node 20.6 / 21.7).
- **`node:test`** - built-in test runner (see Q99).
- **ESM interop** - `require(esm)` works unflagged in Node 22.12+ and 20.19+; `import.meta.dirname` / `import.meta.filename` replace `__dirname` / `__filename` in ESM.
- **TypeScript type stripping** - Node can run `.ts` files directly by stripping type annotations (enabled by default from Node 23.6 and 22.18). It only erases types - no type checking, and syntax that needs code generation (like `enum` or namespaces) requires `--experimental-transform-types` or a build step. Keep running `tsc --noEmit` in CI.
- **Web-standard APIs** - `AbortController`/`AbortSignal.timeout()`, `structuredClone`, `crypto.randomUUID()`, Web Streams, `navigator.hardwareConcurrency`.
- **Promise-based core modules** - `node:fs/promises`, `node:stream/promises` (`pipeline`, `finished`), `node:timers/promises`, `util.parseArgs()`, `util.styleText()`.

- **Trade-offs**: Fewer dependencies means a smaller supply-chain attack surface and fewer upgrades. But built-ins can lag behind specialized libraries in features (e.g. `dotenv-expand`-style variable expansion, axios interceptors), and the stability status of newer flags differs between release lines, so always check the docs for the exact Node version you deploy.

Example:

```json
{
  "type": "module",
  "engines": { "node": ">=22" },
  "scripts": {
    "dev": "node --watch --env-file=.env src/server.js",
    "test": "node --test",
    "start": "node src/server.js"
  }
}
```

---

## Q101. 🔐 The Node.js permission model

The permission model lets you restrict what a Node process can access at runtime. Start Node with `--permission` and, by default, file system reads and writes, child processes, worker threads, native addons and WASI are denied; you then grant specific access with flags like `--allow-fs-read=./config`, `--allow-fs-write=/tmp`, `--allow-child-process` and `--allow-worker`. Code can check access with `process.permission.has('fs.write', '/tmp')`.

Stability: it was introduced as `--experimental-permission` in Node 20 and marked stable (with the flag renamed to `--permission`) in Node 23.5, backported to the 22.x LTS line. Network restrictions have been added more recently and are not available on every release line - check the docs for your version.

- **Trade-offs**: Cheap defense in depth - a compromised dependency can't read `~/.ssh` or spawn a shell if the process wasn't granted that. But the Node docs are explicit that it is a "seat belt", not a sandbox against malicious code: it does not replace container isolation, least-privilege IAM, or OS-level controls, and some paths (for example existing file descriptors and native addons, when allowed) can bypass it. In containers it complements, rather than replaces, a read-only root filesystem and a non-root user.

Example:

```bash
# Allow reading the app and config, writing only to /tmp, nothing else
node --permission \
  --allow-fs-read=/app \
  --allow-fs-write=/tmp \
  src/server.js
```

```javascript
if (!process.permission?.has('fs.write', '/var/log')) {
  console.warn('No write access to /var/log; logging to stdout only');
}
```

---

## Q102. 🚂 Migrating from Express 4 to Express 5

Express 5 was released in October 2024 (after roughly a decade in development), and 5.1 became the default `latest` release on npm in 2025. It requires Node 18+. Most apps migrate with small changes; the Express team publishes a migration guide and codemods.

Key changes to know:

- **Async error handling** - if an async handler or middleware returns a rejected promise, Express 5 calls `next(err)` for you. No more `express-async-errors` or wrapper functions.
- **Path syntax** (`path-to-regexp` v8) - wildcards must be named (`/*splat`), optional params use braces (`/:file{.:ext}`), and regex characters in path strings are no longer supported.
- **Removed or renamed APIs** - `app.del()` → `app.delete()`, `req.param()` removed, `res.send(status)` / `res.json(obj, status)` signatures removed (use `res.status(404).send()`), `res.sendfile()` → `res.sendFile()`, `res.redirect('back')` removed.
- **Body parsing** - `req.body` is `undefined` unless a parser ran, and `express.urlencoded()` defaults to `extended: false`.
- **`req.query`** is a read-only getter, and the default query parser is now "simple" instead of `qs`-extended.

- **Trade-offs**: Removes a whole class of "unhandled rejection hangs the request" bugs and trims legacy APIs. The route-pattern changes are the most common migration work, and some older middleware may assume Express 4 behavior, so run your test suite. If you're choosing a framework for a new service, it's also reasonable to consider **Fastify** (built-in schema validation, fast serialization, encapsulated plugins) or **NestJS** (structured, DI-based, TypeScript-first) - Express 5 remains the simplest, most widely known option.

Example:

```javascript
import express from 'express';
const app = express();
app.use(express.json({ limit: '100kb' }));

// Express 4: '/files/*'   ->  Express 5: named wildcard
app.get('/files/*filepath', (req, res) => {
  res.json({ path: req.params.filepath }); // array of segments in v5
});

// Express 4: '/users/:id?' -> Express 5: optional segment in braces
app.get('/users{/:id}', async (req, res) => {
  const users = await repo.find(req.params.id); // rejection -> error handler
  res.json(users);
});

app.use((err, req, res, next) => {
  res.status(err.status ?? 500).json({ error: err.message });
});
```

---

## Q103. 🛡️ Security baseline for a production Express API in 2026

A solid baseline combines secure defaults at the edge, in middleware, and in how you handle data and secrets. Interviewers want to hear layers, not a single package:

1. **Transport and headers** - TLS everywhere (terminated at the load balancer is fine), `helmet()` for HSTS, CSP, `X-Content-Type-Options`, frame protection; `app.disable('x-powered-by')` (helmet does this too).
2. **Input** - body size limits, schema validation with zod (or Fastify's JSON Schema), reject unknown fields, parameterized queries, and type checks that block NoSQL operator injection.
3. **Abuse control** - rate limiting per IP and per user with a shared store (Redis), stricter limits on login and password reset, `trust proxy` set correctly, and timeouts on every outbound call.
4. **AuthN/AuthZ** - short-lived tokens, HTTP-only `Secure` `SameSite` cookies for browser sessions, CSRF protection for cookie auth, authorization checks on every resource (object-level checks prevent IDOR, the top OWASP API risk).
5. **Secrets and config** - secrets from a secrets manager or platform injection, validated at startup, never logged; rotate regularly.
6. **Dependencies and runtime** - lockfile + `npm ci`, automated dependency updates and audit, minimal non-root container, supported Node LTS, and optionally the permission model (Q101).
7. **Errors and logging** - a central error handler that never leaks stack traces in production, structured logs with redaction, and alerting on auth failures and 5xx spikes.

- **Trade-offs**: Each layer adds a little latency or complexity, and overly strict CSP or rate limits can break legitimate clients - roll out CSP in report-only mode first and tune limits from real traffic. Security middleware doesn't fix logic bugs, so authorization tests are just as important.

Example:

```javascript
import express from 'express';
import helmet from 'helmet';
import { rateLimit } from 'express-rate-limit';
import { z } from 'zod';

const app = express();
app.set('trust proxy', 1);            // behind one load balancer
app.use(helmet());
app.use(express.json({ limit: '100kb' }));
app.use(rateLimit({ windowMs: 60_000, limit: 100, standardHeaders: 'draft-7', legacyHeaders: false }));

const Transfer = z.object({ toAccount: z.string().uuid(), amount: z.number().positive().max(10_000) }).strict();

app.post('/api/transfers', requireAuth, async (req, res) => {
  const body = Transfer.parse(req.body);           // throws -> 400 via error handler
  await assertOwnsAccount(req.user.id, body);      // object-level authorization
  res.status(201).json(await transfers.create(req.user.id, body));
});

app.use((err, req, res, next) => {
  const status = err instanceof z.ZodError ? 400 : err.status ?? 500;
  req.log?.error({ err }, 'request failed');
  res.status(status).json({ error: status === 500 ? 'Internal Server Error' : err.message });
});
```

```mermaid
flowchart LR
    client["Client"] --> edge["CDN / WAF / LB (TLS, coarse rate limits)"]
    edge --> helmetMw["helmet + body limits"]
    helmetMw --> limiter["Rate limiter (Redis store)"]
    limiter --> auth["AuthN + AuthZ checks"]
    auth --> validate["zod validation"]
    validate --> handler["Route handler (parameterized queries)"]
    handler --> errMw["Central error handler (no stack traces)"]
```

---

