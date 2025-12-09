# 🌐 6. REST APIs & Practical Server Scenarios (Q60–69)

---

## 📍 Navigation

<div align="center">

[← Previous: Express.js Core Concepts](5%29%20Express.js%20Core%20Concepts.md) • [Home: Question List](question.md) • [Next: Authentication, Security & Encryption →](7%29%20Authentication%2C%20Security%20%26%20Encryption.md)

[📋 Cheatsheet](Node-Express%20Interview%20Cheatsheet.md)

</div>

---

## Q60. 🔌 RESTful APIs and how to design them

RESTful APIs follow REST principles using HTTP methods to perform CRUD operations on resources - use HTTP methods for different operations (GET, POST, PUT, DELETE), use resource-based URLs (/api/users, /api/users/:id), return appropriate HTTP status codes, use JSON for request/response data, and follow consistent naming conventions. Express provides simple routing and middleware for implementation.

- **Trade-offs**: Use HTTP methods for different operations (GET, POST, PUT, DELETE) - use resource-based URLs (/api/users, /api/users/:id). Return appropriate HTTP status codes - use JSON for request/response data. Follow consistent naming conventions - makes APIs intuitive and predictable, but watch out - REST is a style, not a strict standard, so be consistent within your API.

Example:

```javascript
const express = require('express');
const app = express();

app.get('/api/users', (req, res) => {
  res.json({ users: [] });
});

app.get('/api/users/:id', (req, res) => {
  res.json({ user: { id: req.params.id } });
});

app.post('/api/users', (req, res) => {
  res.json({ message: 'User created' });
});

app.put('/api/users/:id', (req, res) => {
  res.json({ message: 'User updated' });
});

app.delete('/api/users/:id', (req, res) => {
  res.json({ message: 'User deleted' });
});

```

## Q61. ⌨️ Implementing input validation and sanitization

Input validation ensures data integrity and security by checking data format, type, and constraints before processing - validate input data before processing, sanitize data to prevent XSS attacks, use middleware for reusable validation, return clear error messages for invalid data, and consider using Joi for complex validation schemas. Use libraries like express-validator or Joi.

- **Trade-offs**: Validate input data before processing - sanitize data to prevent XSS attacks. Use middleware for reusable validation - return clear error messages for invalid data. Consider using Joi for complex validation schemas - essential for security, but watch out - validation can be verbose, so create reusable validation middleware.

Example:

```javascript
const { body, validationResult } = require('express-validator');

const validateUser = [
  body('email').isEmail().normalizeEmail(),
  body('age').isInt({ min: 0, max: 120 }),
  body('name').trim().isLength({ min: 2, max: 50 }),
  (req, res, next) => {
    const errors = validationResult(req);
    if (!errors.isEmpty()) {
      return res.status(400).json({ errors: errors.array() });
    }
    next();
  }
];

app.post('/api/users', validateUser, (req, res) => {
  res.json({ message: 'User created', user: req.body });
});

```

## Q62. 🔌 Implementing pagination in REST APIs

Pagination limits the number of results returned per request, while filtering allows clients to specify criteria - use query parameters for page and limit, calculate offset for database queries, include pagination metadata in response, implement filtering with search parameters, and consider cursor-based pagination for large datasets. Both improve performance and user experience.

- **Trade-offs**: Use query parameters for page and limit - calculate offset for database queries. Include pagination metadata in response - implement filtering with search parameters. Consider cursor-based pagination for large datasets - essential for large datasets, but watch out - offset-based pagination can be slow for large offsets, so consider cursor-based for better performance.

Example:

```javascript
app.get('/api/users', (req, res) => {
  const page = parseInt(req.query.page) || 1;
  const limit = parseInt(req.query.limit) || 10;
  const offset = (page - 1) * limit;
  const search = req.query.search || '';

  const users = getUsers({ search, limit, offset });
  const total = getTotalUsers({ search });

  res.json({
    data: users,
    pagination: {
      page,
      limit,
      total,
      pages: Math.ceil(total / limit)
    }
  });
});

```

## Q63. 🤔 PUT vs PATCH vs POST

PUT replaces the entire resource (idempotent), PATCH updates specific fields (not idempotent), and POST creates new resources (not idempotent) - use appropriate HTTP status codes (201 for POST), and consider idempotency for PUT operations. Each serves different purposes in RESTful APIs.

- **Trade-offs**: POST: creates new resources, not idempotent - PUT: replaces entire resource, idempotent. PATCH: updates specific fields, not idempotent - use appropriate HTTP status codes (201 for POST). Consider idempotency for PUT operations - choose the right method based on your use case, but watch out - PUT requires sending the entire resource, PATCH is more efficient for partial updates.

Example:

```javascript
app.post('/api/users', (req, res) => {
  const newUser = createUser(req.body);
  res.status(201).json(newUser);
});

app.put('/api/users/:id', (req, res) => {
  const updatedUser = replaceUser(req.params.id, req.body);
  res.json(updatedUser);
});

app.patch('/api/users/:id', (req, res) => {
  const updatedUser = updateUserFields(req.params.id, req.body);
  res.json(updatedUser);
});

```

## Q64. 🔧 Implementing proper HTTP status codes

HTTP status codes communicate the result of API requests - use 2xx for successful operations, 4xx for client errors (400, 401, 403, 404), 5xx for server errors (500, 502, 503), include error details in response body, and use consistent error response format. Provides clear feedback to clients.

- **Trade-offs**: Use 2xx for successful operations - use 4xx for client errors (400, 401, 403, 404). Use 5xx for server errors (500, 502, 503) - include error details in response body. Use consistent error response format - helps clients handle errors properly, but watch out - don't expose sensitive information in error messages.

Example:

```javascript
app.get('/api/users/:id', (req, res) => {
  const user = getUserById(req.params.id);

  if (!user) {
    return res.status(404).json({
      error: 'User not found',
      code: 'USER_NOT_FOUND'
    });
  }

  res.json(user);
});

app.post('/api/users', (req, res) => {
  try {
    const user = createUser(req.body);
    res.status(201).json(user);
  } catch (error) {
    res.status(400).json({
      error: 'Invalid user data',
      details: error.message
    });
  }
});

```

## Q65. 💡 Handling file uploads with multer

File uploads require multipart/form-data parsing, handled by middleware like multer - use multer for handling multipart/form-data, set file size limits and file type filters, store files securely with unique names, validate file types and sizes, and consider cloud storage for production. Multer processes uploaded files and provides access to file information.

- **Trade-offs**: Use multer for handling multipart/form-data - set file size limits and file type filters. Store files securely with unique names - validate file types and sizes. Consider cloud storage for production - essential for file uploads, but watch out - file uploads can be a security risk, so validate and sanitize file names and content.

Example:

```javascript
const multer = require('multer');
const upload = multer({
  dest: 'uploads/',
  limits: { fileSize: 5 * 1024 * 1024 },
  fileFilter: (req, file, cb) => {
    if (file.mimetype.startsWith('image/')) {
      cb(null, true);
    } else {
      cb(new Error('Only images allowed'));
    }
  }
});

app.post('/api/upload', upload.single('image'), (req, res) => {
  res.json({
    message: 'File uploaded',
    filename: req.file.filename,
    originalName: req.file.originalname
  });
});

```

## Q66. 🌊 Implementing streamed downloads

Streaming file downloads allows clients to start receiving data before the entire file is ready - use streams for large file downloads, set appropriate Content-Disposition headers, handle file not found errors, consider resumable downloads for large files, and monitor download progress and errors. Improves performance and memory usage for large files.

- **Trade-offs**: Use streams for large file downloads - set appropriate Content-Disposition headers. Handle file not found errors - consider resumable downloads for large files. Monitor download progress and errors - essential for large files, but watch out - streaming requires proper error handling to avoid hanging connections.

Example:

```javascript
const fs = require('fs');
const path = require('path');

app.get('/api/download/:filename', (req, res) => {
  const filename = req.params.filename;
  const filePath = path.join(__dirname, 'uploads', filename);

  if (!fs.existsSync(filePath)) {
    return res.status(404).json({ error: 'File not found' });
  }

  res.setHeader('Content-Disposition', `attachment; filename="${filename}"`);
  res.setHeader('Content-Type', 'application/octet-stream');

  const fileStream = fs.createReadStream(filePath);
  fileStream.pipe(res);
});

```

## Q67. 🔧 Implementing rate limiting in Express.js

Rate limiting controls the number of requests a client can make within a time period - implement rate limiting to prevent abuse, use different limits for different endpoints, consider IP-based and user-based limiting, store rate limit data in Redis for distributed systems, and provide clear error messages for rate limit exceeded. Prevents abuse and ensures fair resource usage.

- **Trade-offs**: Implement rate limiting to prevent abuse - use different limits for different endpoints. Consider IP-based and user-based limiting - store rate limit data in Redis for distributed systems. Provide clear error messages for rate limit exceeded - essential for production APIs, but watch out - rate limiting can block legitimate users if set too strict.

Example:

```javascript
const rateLimit = require('express-rate-limit');

const limiter = rateLimit({
  windowMs: 15 * 60 * 1000,
  max: 100,
  message: 'Too many requests from this IP'
});

app.use('/api/', limiter);

const strictLimiter = rateLimit({
  windowMs: 60 * 1000,
  max: 5,
  message: 'Too many login attempts'
});

app.post('/api/login', strictLimiter, (req, res) => {
  // Login logic
});

```

## Q68. 📝 Implementing logging with morgan or pino

HTTP request logging captures request details, response status, and timing information - use morgan for HTTP request logging, use pino for structured JSON logging, log important events and errors, consider log levels (info, warn, error), and use log aggregation tools for production. Essential for monitoring, debugging, and analytics.

- **Trade-offs**: Use morgan for HTTP request logging - use pino for structured JSON logging. Log important events and errors - consider log levels (info, warn, error). Use log aggregation tools for production - essential for debugging, but watch out - too much logging can impact performance, so use appropriate log levels.

Example:

```javascript
const morgan = require('morgan');
const pino = require('pino');

app.use(morgan('combined'));

const logger = pino();
app.use((req, res, next) => {
  req.logger = logger;
  next();
});

app.get('/api/users', (req, res) => {
  req.logger.info('Fetching users');
  res.json({ users: [] });
});

```

## Q69. 🔌 Implementing API versioning and documentation

API versioning allows backward compatibility, while documentation helps developers understand and use APIs effectively - use URL versioning (/api/v1, /api/v2), document APIs with OpenAPI/Swagger, maintain backward compatibility, use semantic versioning for API versions, and provide interactive API documentation.

- **Trade-offs**: Use URL versioning (/api/v1, /api/v2) - document APIs with OpenAPI/Swagger. Maintain backward compatibility - use semantic versioning for API versions. Provide interactive API documentation - essential for API adoption, but watch out - maintaining multiple API versions can be complex, so plan your versioning strategy carefully.

Example:

```javascript
const swaggerJsdoc = require('swagger-jsdoc');
const swaggerUi = require('swagger-ui-express');

const swaggerOptions = {
  definition: {
    openapi: '3.0.0',
    info: {
      title: 'User API',
      version: '1.0.0',
      description: 'A simple User API'
    },
    servers: [{ url: 'http://localhost:3000' }]
  },
  apis: ['./routes/*.js']
};

const specs = swaggerJsdoc(swaggerOptions);
app.use('/api-docs', swaggerUi.serve, swaggerUi.setup(specs));

app.use('/api/v1', v1Routes);
app.use('/api/v2', v2Routes);

```

---

## 📍 Navigation

<div align="center">

[5) Express.js Core Concepts.md](5%29%20Express.js%20Core%20Concepts.md) • [Home: Question List](question.md) • [7) Authentication, Security & Encryption.md →](7%29%20Authentication,%20Security%20&%20Encryption.md)

[📋 Cheatsheet](Node-Express%20Interview%20Cheatsheet.md]

</div>

---
