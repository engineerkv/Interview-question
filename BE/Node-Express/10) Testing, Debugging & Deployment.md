# 10) Testing, Debugging & Deployment (Q91–100)

## 91) What are the most common testing frameworks (Jest, Mocha, Supertest)?

Concept: Testing frameworks provide tools for writing and running tests, with Jest being popular for unit tests, Mocha for flexible testing, and Supertest for API testing.

Example:
```javascript
// Jest testing
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

Deep Insight:
- Jest: Popular for React/Node.js with built-in mocking
- Mocha: Flexible testing framework with many plugins
- Supertest: Specialized for HTTP API testing
- Choose based on project requirements and team preferences
- Consider testing pyramid: unit > integration > e2e

## 92) How do you test Express routes and middleware using Supertest?

Concept: Supertest allows testing Express applications by making HTTP requests and asserting responses, testing both routes and middleware behavior.

Example:
```javascript
const request = require('supertest');
const express = require('express');

// Test middleware
function authMiddleware(req, res, next) {
  if (req.headers.authorization) {
    req.user = { id: 1, name: 'John' };
    next();
  } else {
    res.status(401).json({ error: 'Unauthorized' });
  }
}

// Test routes
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

Deep Insight:
- Test middleware in isolation
- Test both success and error cases
- Use proper HTTP status code assertions
- Test request/response modifications
- Consider edge cases and error scenarios

## 93) How do you mock external API calls in unit tests?

Concept: Mocking external API calls prevents tests from making real network requests, making tests faster, more reliable, and independent of external services.

Example:
```javascript
const axios = require('axios');
const { getWeatherData } = require('../services/weather');

// Mock axios
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

Deep Insight:
- Mock external dependencies to isolate units under test
- Use jest.mock() for automatic mocking
- Test both success and error scenarios
- Verify mock calls with correct parameters
- Consider using MSW for more realistic API mocking

## 94) How do you debug Node.js applications using VS Code or Chrome DevTools?

Concept: Debugging Node.js applications involves setting breakpoints, inspecting variables, and stepping through code using integrated debuggers in VS Code or Chrome DevTools.

Example:
```javascript
// Start with --inspect flag
// node --inspect app.js
// node --inspect-brk app.js (break on start)

const express = require('express');
const app = express();

app.get('/api/users', (req, res) => {
  const userId = req.query.id;
  
  // Set breakpoint here
  debugger;
  
  if (!userId) {
    return res.status(400).json({ error: 'User ID required' });
  }
  
  // Debug variables
  console.log('User ID:', userId);
  
  // Simulate database query
  const user = getUserById(userId);
  
  res.json({ user });
});

function getUserById(id) {
  // Another breakpoint
  debugger;
  return { id, name: 'John Doe' };
}
```

Deep Insight:
- Use --inspect flag to enable debugging
- Set breakpoints in VS Code or Chrome DevTools
- Use debugger statement for programmatic breakpoints
- Inspect variables and call stack
- Debug async code and promises

## 95) How do you set up CI/CD pipelines for Node.js (GitHub Actions, Jenkins)?

Concept: CI/CD pipelines automate testing, building, and deploying Node.js applications, ensuring code quality and consistent deployments.

Example:
```yaml
# .github/workflows/ci.yml
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
        # Add deployment commands
```

Deep Insight:
- Automate testing on every commit
- Test against multiple Node.js versions
- Run linting and security checks
- Deploy only after successful tests
- Use environment-specific configurations

## 96) How do you containerize Node.js apps using Docker?

Concept: Docker containers package Node.js applications with their dependencies, ensuring consistent deployment across different environments.

Example:
```dockerfile
# Dockerfile
FROM node:18-alpine

# Set working directory
WORKDIR /app

# Copy package files
COPY package*.json ./

# Install dependencies
RUN npm ci --only=production

# Copy application code
COPY . .

# Create non-root user
RUN addgroup -g 1001 -S nodejs
RUN adduser -S nextjs -u 1001
USER nextjs

# Expose port
EXPOSE 3000

# Health check
HEALTHCHECK --interval=30s --timeout=3s --start-period=5s --retries=3 \
  CMD curl -f http://localhost:3000/health || exit 1

# Start application
CMD ["npm", "start"]
```

Deep Insight:
- Use multi-stage builds for smaller images
- Use .dockerignore to exclude unnecessary files
- Run as non-root user for security
- Implement health checks
- Use specific Node.js versions for consistency

## 97) How do you handle graceful shutdowns (SIGTERM, SIGINT)?

Concept: Graceful shutdowns ensure applications close properly by handling termination signals, cleaning up resources, and finishing ongoing requests.

Example:
```javascript
const express = require('express');
const app = express();

// Graceful shutdown handling
let server;

function gracefulShutdown(signal) {
  console.log(`Received ${signal}. Starting graceful shutdown...`);
  
  server.close(() => {
    console.log('HTTP server closed');
    
    // Close database connections
    if (db) {
      db.close(() => {
        console.log('Database connection closed');
        process.exit(0);
      });
    } else {
      process.exit(0);
    }
  });
  
  // Force close after 30 seconds
  setTimeout(() => {
    console.error('Could not close connections in time, forcefully shutting down');
    process.exit(1);
  }, 30000);
}

// Handle termination signals
process.on('SIGTERM', () => gracefulShutdown('SIGTERM'));
process.on('SIGINT', () => gracefulShutdown('SIGINT'));

// Start server
server = app.listen(3000, () => {
  console.log('Server running on port 3000');
});
```

Deep Insight:
- Handle SIGTERM and SIGINT signals
- Close HTTP server and database connections
- Set timeout for forced shutdown
- Log shutdown process for debugging
- Test graceful shutdown in production

## 98) How do you manage different environment configurations (dev, staging, prod)?

Concept: Environment-specific configurations ensure applications behave correctly across different environments using environment variables and configuration files.

Example:
```javascript
// config/index.js
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
    port: process.env.PORT || 3000,
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

const env = process.env.NODE_ENV || 'development';
module.exports = config[env];
```

Deep Insight:
- Use environment variables for sensitive data
- Provide default values for development
- Validate required environment variables
- Use different configurations per environment
- Never commit secrets to version control

## 99) How do you deploy Node + Express apps to cloud providers (AWS, Render, Vercel)?

Concept: Cloud deployment involves packaging applications, configuring infrastructure, and using platform-specific services for hosting Node.js applications.

Example:
```javascript
// AWS Lambda deployment
const serverless = require('serverless-http');
const express = require('express');
const app = express();

app.get('/api/users', (req, res) => {
  res.json({ users: [] });
});

// Export for serverless
module.exports.handler = serverless(app);

// Render deployment
// package.json
{
  "scripts": {
    "start": "node app.js",
    "build": "npm install"
  },
  "engines": {
    "node": "18.x"
  }
}

// Vercel deployment
// vercel.json
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
```

Deep Insight:
- Choose platform based on requirements
- Configure environment variables
- Set up proper build and start commands
- Consider serverless vs traditional hosting
- Implement health checks and monitoring

## 100) What are best practices for monitoring, maintaining, and optimizing production servers (logs, restarts, health checks, alerts)?

Concept: Production server management involves comprehensive monitoring, logging, health checks, and alerting to ensure reliability and performance.

Example:
```javascript
const express = require('express');
const app = express();

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

// Logging middleware
app.use((req, res, next) => {
  const start = Date.now();
  
  res.on('finish', () => {
    const duration = Date.now() - start;
    console.log(`${req.method} ${req.url} ${res.statusCode} ${duration}ms`);
  });
  
  next();
});

// Error monitoring
process.on('uncaughtException', (error) => {
  console.error('Uncaught Exception:', error);
  // Send to monitoring service
  process.exit(1);
});

process.on('unhandledRejection', (reason, promise) => {
  console.error('Unhandled Rejection:', reason);
  // Send to monitoring service
});
```

Deep Insight:
- Implement comprehensive health checks
- Use structured logging with timestamps
- Monitor memory usage and performance
- Set up alerts for critical issues
- Implement proper error handling and reporting
