# 9) Testing, Debugging & Deployment (Q90–99)

<div align="center">

**[← Previous: Performance, Optimization, Scaling & Monitoring](8%29%20Performance%2C%20Optimization%2C%20Scaling%20%26%20Monitoring.md)** | **[Next: Question List →](question.md)**

</div>
## Q90. Writing unit tests with Jest or Mocha

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

## Q91. Testing API endpoints with Supertest

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

## Q92. Mocking API calls in tests

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

## Q93. Debugging Node.js applications with VS Code

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

## Q94. Debugging with Chrome DevTools

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
        node-version: [16.x, 18.x, 20.x]
    steps:
    - uses: actions/checkout@v3
    - name: Use Node.js ${{ matrix.node-version }}
      uses: actions/setup-node@v3
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
    - uses: actions/checkout@v3
    - name: Deploy to production
      run: |
        echo "Deploying to production..."
```

## Q95. Implementing CI/CD for Node.js applications

Docker containers package Node.js applications with their dependencies - use multi-stage builds for smaller images, use .dockerignore to exclude unnecessary files, run as non-root user for security, implement health checks, and use specific Node.js versions for consistency. Ensures consistent deployment across different environments.

- **Trade-offs**: Use multi-stage builds for smaller images - use .dockerignore to exclude unnecessary files. Run as non-root user for security - implement health checks. Use specific Node.js versions for consistency - makes deployment consistent, but watch out - Docker adds complexity, so use it when you need consistency across environments.

Example:

```dockerfile
FROM node:18-alpine

WORKDIR /app

COPY package*.json ./

RUN npm ci --only=production

COPY . .

RUN addgroup -g 1001 -S nodejs
RUN adduser -S nextjs -u 1001
USER nextjs

EXPOSE 3000

HEALTHCHECK --interval=30s --timeout=3s --start-period=5s --retries=3 \
  CMD curl -f http://localhost:3000/health || exit 1

CMD ["npm", "start"]
```

## Q96. Containerizing Node.js applications with Docker

Docker containerization packages Node.js applications with all dependencies into portable containers - create Dockerfile with Node.js base image, copy application files, install dependencies, expose ports, and set startup command. Enables consistent deployments across environments and simplifies deployment process.

- **Trade-offs**: Packages app with all dependencies - enables consistent deployments across environments. Simplifies deployment process - containers are portable and isolated. Easy to scale and manage - great for CI/CD pipelines, but watch out - Docker images can be large, so use multi-stage builds and .dockerignore to optimize size.

Example:

```dockerfile
# Dockerfile
FROM node:18-alpine

WORKDIR /app

# Copy package files
COPY package*.json ./

# Install dependencies
RUN npm ci --only=production

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
FROM node:18-alpine AS builder
WORKDIR /app
COPY package*.json ./
RUN npm ci
COPY . .
RUN npm run build

FROM node:18-alpine
WORKDIR /app
COPY --from=builder /app/dist ./dist
COPY package*.json ./
RUN npm ci --only=production
CMD ["node", "dist/app.js"]
```

## Q97. Implementing graceful shutdowns in production

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

## Q98. Handling environment configurations

Environment-specific configurations ensure applications behave correctly across different environments - use environment variables for sensitive data, provide default values for development, validate required environment variables, use different configurations per environment, and never commit secrets to version control. Use environment variables and configuration files.

- **Trade-offs**: Use environment variables for sensitive data - provide default values for development. Validate required environment variables - use different configurations per environment. Never commit secrets to version control - essential for multi-environment deployments, but watch out - managing configs can be complex, so use tools like dotenv and config validation.

Example:

```javascript
require('dotenv').config();

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

## Q99. Deploying Node.js applications to the cloud

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
    "node": "18.x"
  }
}

// Vercel (vercel.json)
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
