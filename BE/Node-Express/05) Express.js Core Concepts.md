# 🚂 5. Express.js Core Concepts (Q50–59)

---

## 📍 Navigation

<div align="center">

[← Previous: Node.js Internals & Performance](04%29%20Node.js%20Internals%20%26%20Performance.md) • [Home: Question List](question.md) • [Next: REST APIs & Practical Server Scenarios →](06%29%20REST%20APIs%20%26%20Practical%20Server%20Scenarios.md)

[📋 Cheatsheet](Node-Express%20Interview%20Cheatsheet.md)

</div>

---

## Q50. ❓ Express.js and how it works

Express.js is a minimal, unopinionated web framework for Node.js that provides essential features for building web applications and APIs - it's built on top of Node.js HTTP module, provides routing, middleware, and templating, has a large ecosystem of middleware and plugins, and is easy to learn and quick to set up. Popular due to its simplicity and flexibility.

- **Trade-offs**: Minimal and unopinionated framework - built on top of Node.js HTTP module. Provides routing, middleware, and templating - large ecosystem of middleware and plugins. Easy to learn and quick to set up - great for rapid development, but watch out - being unopinionated means you need to make more architectural decisions yourself.

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

## Q51. ❓ Middleware and how to use it

Middleware are functions that execute during the request-response cycle, with access to request, response, and next function - these run between request and response, execute in order these are defined, can modify request/response objects, and must call next() to continue or send response to end. Allows you to modify requests, responses, or end the cycle.

- **Trade-offs**: Functions that run between request and response - access to req, res, and next parameters. Execute in order these are defined - can modify request/response objects. Must call next() to continue or send response to end - powerful for cross-cutting concerns, but watch out - middleware order matters, so place these carefully.

Example:

```javascript
const express = require('express');
const app = express();

app.use((req, res, next) => {
  console.log('Request received:', req.method, req.url);
  next();
});

app.get('/', (req, res) => {
  res.send('Hello World!');
});

```

## Q52. 🔧 `next()` function in middleware

The next() function passes control to the next middleware in the stack, allowing middleware to be chained together and enabling conditional execution flow - it must be called to continue request processing, can pass errors to error handling middleware (optional parameter for error handling), and not calling next() ends the request-response cycle.

- **Trade-offs**: Passes control to next middleware in stack - must be called to continue request processing. Can pass errors to error handling middleware - optional parameter for error handling. Not calling next() ends the request-response cycle - essential for middleware flow control, but watch out - forgetting to call next() can cause requests to hang.

Example:

```javascript
function authenticate(req, res, next) {
  const token = req.headers.authorization;
  if (token) {
    req.user = { id: 1, name: 'John' };
    next();
  } else {
    res.status(401).json({ error: 'Unauthorized' });
  }
}

app.use(authenticate);
app.get('/protected', (req, res) => {
  res.json({ user: req.user });
});

```

## Q53. 🤔 `app.use()` vs `app.METHOD()`

app.use() applies middleware to all routes or specific paths, while app.METHOD() (get, post, etc.) defines route handlers for specific HTTP methods and paths - middleware runs before route handlers, you can chain multiple middleware with app.use(), and route handlers are also middleware functions.

- **Trade-offs**: app.use(): middleware for all routes or specific paths - app.METHOD(): route handlers for specific HTTP methods. Middleware runs before route handlers - can chain multiple middleware with app.use(). Route handlers are also middleware functions - use app.use() for cross-cutting concerns, app.METHOD() for specific routes.

Example:

```javascript
const express = require('express');
const app = express();

app.use(express.json());
app.use('/api', (req, res, next) => {
  console.log('API request');
  next();
});

app.get('/users', (req, res) => {
  res.json({ users: [] });
});

app.post('/users', (req, res) => {
  res.json({ message: 'User created' });
});

```

## Q54. 🛣️ Implementing routing in Express.js

Organize routes into separate modules using Express Router, creating a clean, maintainable structure with route-specific middleware and handlers - use Express Router for modular route organization, separate routes into different files, apply middleware at router level, mount routers with app.use(), and keep route handlers focused and single-purpose.

- **Trade-offs**: Use Express Router for modular route organization - separate routes into different files. Apply middleware at router level - mount routers with app.use(). Keep route handlers focused and single-purpose - makes code more maintainable, but watch out - too many route files can make navigation harder, so balance modularity with simplicity.

Example:

```javascript
const express = require('express');
const router = express.Router();

router.get('/', (req, res) => {
  res.json({ users: [] });
});

router.post('/', (req, res) => {
  res.json({ message: 'User created' });
});

module.exports = router;

const userRoutes = require('./routes/users');
app.use('/api/users', userRoutes);

```

## Q55. 💡 Serving static files with Express.js

Use express.static() middleware to serve static files like HTML, CSS, JavaScript, and images from a specified directory - it serves files from root path by default, can specify custom mount path, serves files in order of middleware definition, and automatically handles MIME types and caching headers.

- **Trade-offs**: express.static() serves files from specified directory - files are served from root path by default. Can specify custom mount path - serves files in order of middleware definition. Automatically handles MIME types and caching headers - simple and efficient, but watch out - serving static files from Express is fine for development, but use a reverse proxy like nginx for production.

Example:

```javascript
const express = require('express');
const path = require('path');
const app = express();

app.use(express.static('public'));
app.use('/static', express.static('public'));
app.use(express.static('public'));
app.use(express.static('uploads'));

```

## Q56. 📝 Parsing JSON and form data in Express.js

Express v5 includes built-in JSON and form data parsing middleware, eliminating the need for body-parser dependency - express.json() parses JSON request bodies, express.urlencoded() parses form data, extended: true allows nested objects, and it's built-in middleware in Express v5.

- **Trade-offs**: express.json() parses JSON request bodies - express.urlencoded() parses form data. extended: true allows nested objects - built-in middleware in Express v5. No need for body-parser dependency - simpler setup, but watch out - in Express v4, you needed body-parser, so check your Express version.

Example:

```javascript
const express = require('express');
const app = express();

app.use(express.json());
app.use(express.urlencoded({ extended: true }));

app.post('/api/data', (req, res) => {
  console.log('JSON data:', req.body);
  res.json({ received: req.body });
});

```

## Q57. ⚠️ Handling errors in Express.js

Error handling middleware has four parameters (err, req, res, next) and should be defined after all other middleware and routes to catch errors - it can handle both sync and async errors, use next(error) to pass errors to error handler, and you can have multiple error handling middleware.

- **Trade-offs**: Must have four parameters: err, req, res, next - defined after all other middleware and routes. Can handle both sync and async errors - use next(error) to pass errors to error handler. Can have multiple error handling middleware - essential for production apps, but watch out - error middleware order matters, so place it last.

Example:

```javascript
const express = require('express');
const app = express();

app.use((err, req, res, next) => {
  console.error(err.stack);
  res.status(500).json({
    error: 'Something went wrong!',
    message: process.env.NODE_ENV === 'development' ? err.message : 'Internal Server Error'
  });
});

app.get('/async-route', async (req, res, next) => {
  try {
    const data = await someAsyncOperation();
    res.json(data);
  } catch (error) {
    next(error);
  }
});

```

## Q58. 🤔 Application-level vs router-level middleware

Application-level middleware applies to all routes, while router-level middleware applies only to routes defined on that specific router instance - router middleware runs after app middleware, you can have different middleware for different route groups, and it's useful for organizing related routes with shared middleware.

- **Trade-offs**: Application-level: applies to all routes on the app - router-level: applies only to routes on that router. Router middleware runs after app middleware - can have different middleware for different route groups. Useful for organizing related routes with shared middleware - use app-level for global concerns, router-level for route-specific logic.

Example:

```javascript
const express = require('express');
const app = express();
const router = express.Router();

app.use((req, res, next) => {
  console.log('App middleware');
  next();
});

router.use((req, res, next) => {
  console.log('Router middleware');
  next();
});

router.get('/users', (req, res) => {
  res.json({ users: [] });
});

app.use('/api', router);

```

## Q59. 🧩 Integrating Express.js with the HTTP module

Express.js is built on top of Node's HTTP module, providing a higher-level abstraction with routing, middleware, and request/response enhancements - Express wraps Node.js HTTP module, provides higher-level API for web development, adds routing, middleware, and templating, enhances request and response objects, and maintains compatibility with Node.js HTTP features.

- **Trade-offs**: Express wraps Node.js HTTP module - provides higher-level API for web development. Adds routing, middleware, and templating - enhances request and response objects. Maintains compatibility with Node.js HTTP features - makes web development easier, but watch out - understanding the underlying HTTP module helps debug issues.

Example:

```javascript
const http = require('http');
const server = http.createServer((req, res) => {
  if (req.url === '/' && req.method === 'GET') {
    res.writeHead(200, {'Content-Type': 'text/plain'});
    res.end('Hello World!');
  }
});

const express = require('express');
const app = express();
app.get('/', (req, res) => {
  res.send('Hello World!');
});

```

---

## 📍 Navigation

<div align="center">

[← Previous: Node.js Internals & Performance](04%29%20Node.js%20Internals%20%26%20Performance.md) • [Home: Question List](question.md) • [Next: REST APIs & Practical Server Scenarios →](06%29%20REST%20APIs%20%26%20Practical%20Server%20Scenarios.md)

[📋 Cheatsheet](Node-Express%20Interview%20Cheatsheet.md)

</div>

---
