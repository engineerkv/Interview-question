# 6) Express.js Core Concepts (Q51–60)

## 51) What is Express.js, and why is it popular for Node.js apps?

Concept: Express.js is a minimal, unopinionated web framework for Node.js that provides essential features for building web applications and APIs, making it popular due to its simplicity and flexibility.

Example:
```javascript
const express = require('express');
const app = express();

app.get('/', (req, res) => {
  res.send('Hello World!');
});

app.listen(3000, () => {
  console.log('Server running on port 3000');
});
```

Deep Insight:
- Minimal and unopinionated framework
- Built on top of Node.js HTTP module
- Provides routing, middleware, and templating
- Large ecosystem of middleware and plugins
- Easy to learn and quick to set up

## 52) What is middleware in Express, and how does it work internally?

Concept: Middleware are functions that execute during the request-response cycle, with access to request, response, and next function, allowing you to modify requests, responses, or end the cycle.

Example:
```javascript
const express = require('express');
const app = express();

// Custom middleware
app.use((req, res, next) => {
  console.log('Request received:', req.method, req.url);
  next(); // Pass control to next middleware
});

app.get('/', (req, res) => {
  res.send('Hello World!');
});
```

Deep Insight:
- Functions that run between request and response
- Access to req, res, and next parameters
- Execute in order they are defined
- Can modify request/response objects
- Must call next() to continue or send response to end

## 53) What is the role of next() in Express middleware?

Concept: The next() function passes control to the next middleware in the stack, allowing middleware to be chained together and enabling conditional execution flow.

Example:
```javascript
// Authentication middleware
function authenticate(req, res, next) {
  const token = req.headers.authorization;
  if (token) {
    req.user = { id: 1, name: 'John' };
    next(); // Continue to next middleware
  } else {
    res.status(401).json({ error: 'Unauthorized' });
    // Don't call next() - end the request
  }
}

app.use(authenticate);
app.get('/protected', (req, res) => {
  res.json({ user: req.user });
});
```

Deep Insight:
- Passes control to next middleware in stack
- Must be called to continue request processing
- Can pass errors to error handling middleware
- Optional parameter for error handling
- Not calling next() ends the request-response cycle

## 54) What is the difference between app.use() and app.METHOD()?

Concept: app.use() applies middleware to all routes or specific paths, while app.METHOD() (get, post, etc.) defines route handlers for specific HTTP methods and paths.

Example:
```javascript
const express = require('express');
const app = express();

// Middleware for all routes
app.use(express.json());
app.use('/api', (req, res, next) => {
  console.log('API request');
  next();
});

// Route handlers for specific methods
app.get('/users', (req, res) => {
  res.json({ users: [] });
});

app.post('/users', (req, res) => {
  res.json({ message: 'User created' });
});
```

Deep Insight:
- app.use(): Middleware for all routes or specific paths
- app.METHOD(): Route handlers for specific HTTP methods
- Middleware runs before route handlers
- Can chain multiple middleware with app.use()
- Route handlers are also middleware functions

## 55) How do you structure routes in a modular Express app?

Concept: Organize routes into separate modules using Express Router, creating a clean, maintainable structure with route-specific middleware and handlers.

Example:
```javascript
// routes/users.js
const express = require('express');
const router = express.Router();

router.get('/', (req, res) => {
  res.json({ users: [] });
});

router.post('/', (req, res) => {
  res.json({ message: 'User created' });
});

module.exports = router;

// app.js
const userRoutes = require('./routes/users');
app.use('/api/users', userRoutes);
```

Deep Insight:
- Use Express Router for modular route organization
- Separate routes into different files
- Apply middleware at router level
- Mount routers with app.use()
- Keep route handlers focused and single-purpose

## 56) How do you serve static files in Express.js?

Concept: Use express.static() middleware to serve static files like HTML, CSS, JavaScript, and images from a specified directory.

Example:
```javascript
const express = require('express');
const path = require('path');
const app = express();

// Serve static files from public directory
app.use(express.static('public'));

// Serve static files with custom path
app.use('/static', express.static('public'));

// Serve files from multiple directories
app.use(express.static('public'));
app.use(express.static('uploads'));
```

Deep Insight:
- express.static() serves files from specified directory
- Files are served from root path by default
- Can specify custom mount path
- Serves files in order of middleware definition
- Automatically handles MIME types and caching headers

## 57) How do you handle JSON and form data parsing in Express v5?

Concept: Express v5 includes built-in JSON and form data parsing middleware, eliminating the need for body-parser dependency.

Example:
```javascript
const express = require('express');
const app = express();

// Built-in JSON parsing
app.use(express.json());

// Built-in URL-encoded form parsing
app.use(express.urlencoded({ extended: true }));

app.post('/api/data', (req, res) => {
  console.log('JSON data:', req.body);
  res.json({ received: req.body });
});
```

Deep Insight:
- express.json() parses JSON request bodies
- express.urlencoded() parses form data
- extended: true allows nested objects
- Built-in middleware in Express v5
- No need for body-parser dependency

## 58) How do you implement global error handling middleware in Express?

Concept: Error handling middleware has four parameters (err, req, res, next) and should be defined after all other middleware and routes to catch errors.

Example:
```javascript
const express = require('express');
const app = express();

// Error handling middleware
app.use((err, req, res, next) => {
  console.error(err.stack);
  res.status(500).json({
    error: 'Something went wrong!',
    message: process.env.NODE_ENV === 'development' ? err.message : 'Internal Server Error'
  });
});

// Async error handling
app.get('/async-route', async (req, res, next) => {
  try {
    const data = await someAsyncOperation();
    res.json(data);
  } catch (error) {
    next(error); // Pass error to error handling middleware
  }
});
```

Deep Insight:
- Must have four parameters: err, req, res, next
- Defined after all other middleware and routes
- Can handle both sync and async errors
- Use next(error) to pass errors to error handler
- Can have multiple error handling middleware

## 59) What is the difference between application-level and router-level middleware?

Concept: Application-level middleware applies to all routes, while router-level middleware applies only to routes defined on that specific router instance.

Example:
```javascript
const express = require('express');
const app = express();
const router = express.Router();

// Application-level middleware
app.use((req, res, next) => {
  console.log('App middleware');
  next();
});

// Router-level middleware
router.use((req, res, next) => {
  console.log('Router middleware');
  next();
});

router.get('/users', (req, res) => {
  res.json({ users: [] });
});

app.use('/api', router);
```

Deep Insight:
- Application-level: Applies to all routes on the app
- Router-level: Applies only to routes on that router
- Router middleware runs after app middleware
- Can have different middleware for different route groups
- Useful for organizing related routes with shared middleware

## 60) How does Express.js integrate with Node's HTTP module under the hood?

Concept: Express.js is built on top of Node's HTTP module, providing a higher-level abstraction with routing, middleware, and request/response enhancements.

Example:
```javascript
// Raw Node.js HTTP
const http = require('http');
const server = http.createServer((req, res) => {
  if (req.url === '/' && req.method === 'GET') {
    res.writeHead(200, {'Content-Type': 'text/plain'});
    res.end('Hello World!');
  }
});

// Express.js (built on HTTP module)
const express = require('express');
const app = express();
app.get('/', (req, res) => {
  res.send('Hello World!');
});
```

Deep Insight:
- Express wraps Node.js HTTP module
- Provides higher-level API for web development
- Adds routing, middleware, and templating
- Enhances request and response objects
- Maintains compatibility with Node.js HTTP features
