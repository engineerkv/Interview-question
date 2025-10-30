# 7) REST APIs & Practical Server Scenarios (Q61–70)

## 61) What are RESTful APIs, and how do you implement them in Express?

Concept: RESTful APIs follow REST principles using HTTP methods to perform CRUD operations on resources, with Express providing simple routing and middleware for implementation.

Example:
```javascript
const express = require('express');
const app = express();

// RESTful routes
app.get('/api/users', (req, res) => {
  res.json({ users: [] }); // GET - Read all
});

app.get('/api/users/:id', (req, res) => {
  res.json({ user: { id: req.params.id } }); // GET - Read one
});

app.post('/api/users', (req, res) => {
  res.json({ message: 'User created' }); // POST - Create
});

app.put('/api/users/:id', (req, res) => {
  res.json({ message: 'User updated' }); // PUT - Update
});

app.delete('/api/users/:id', (req, res) => {
  res.json({ message: 'User deleted' }); // DELETE - Delete
});
```

Deep Insight:
- Use HTTP methods for different operations (GET, POST, PUT, DELETE)
- Use resource-based URLs (/api/users, /api/users/:id)
- Return appropriate HTTP status codes
- Use JSON for request/response data
- Follow consistent naming conventions

## 62) How do you validate and sanitize input data (express-validator, Joi)?

Concept: Input validation ensures data integrity and security by checking data format, type, and constraints before processing, using libraries like express-validator or Joi.

Example:
```javascript
const { body, validationResult } = require('express-validator');

// Validation middleware
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

Deep Insight:
- Validate input data before processing
- Sanitize data to prevent XSS attacks
- Use middleware for reusable validation
- Return clear error messages for invalid data
- Consider using Joi for complex validation schemas

## 63) How do you implement pagination and filtering efficiently in API responses?

Concept: Pagination limits the number of results returned per request, while filtering allows clients to specify criteria, both improving performance and user experience.

Example:
```javascript
app.get('/api/users', (req, res) => {
  const page = parseInt(req.query.page) || 1;
  const limit = parseInt(req.query.limit) || 10;
  const offset = (page - 1) * limit;
  const search = req.query.search || '';
  
  // Simulate database query with pagination and filtering
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

Deep Insight:
- Use query parameters for page and limit
- Calculate offset for database queries
- Include pagination metadata in response
- Implement filtering with search parameters
- Consider cursor-based pagination for large datasets

## 64) What's the difference between PUT, PATCH, and POST?

Concept: PUT replaces the entire resource, PATCH updates specific fields, and POST creates new resources, each serving different purposes in RESTful APIs.

Example:
```javascript
// POST - Create new resource
app.post('/api/users', (req, res) => {
  const newUser = createUser(req.body);
  res.status(201).json(newUser);
});

// PUT - Replace entire resource
app.put('/api/users/:id', (req, res) => {
  const updatedUser = replaceUser(req.params.id, req.body);
  res.json(updatedUser);
});

// PATCH - Update specific fields
app.patch('/api/users/:id', (req, res) => {
  const updatedUser = updateUserFields(req.params.id, req.body);
  res.json(updatedUser);
});
```

Deep Insight:
- POST: Creates new resources, not idempotent
- PUT: Replaces entire resource, idempotent
- PATCH: Updates specific fields, not idempotent
- Use appropriate HTTP status codes (201 for POST)
- Consider idempotency for PUT operations

## 65) How do you send appropriate HTTP status codes and error responses?

Concept: HTTP status codes communicate the result of API requests, with 2xx for success, 4xx for client errors, and 5xx for server errors, providing clear feedback to clients.

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

Deep Insight:
- Use 2xx for successful operations
- Use 4xx for client errors (400, 401, 403, 404)
- Use 5xx for server errors (500, 502, 503)
- Include error details in response body
- Use consistent error response format

## 66) How do you handle file uploads in Express (multer)?

Concept: File uploads require multipart/form-data parsing, handled by middleware like multer, which processes uploaded files and provides access to file information.

Example:
```javascript
const multer = require('multer');
const upload = multer({ 
  dest: 'uploads/',
  limits: { fileSize: 5 * 1024 * 1024 }, // 5MB limit
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

Deep Insight:
- Use multer for handling multipart/form-data
- Set file size limits and file type filters
- Store files securely with unique names
- Validate file types and sizes
- Consider cloud storage for production

## 67) How do you serve streamed file downloads efficiently?

Concept: Streaming file downloads allows clients to start receiving data before the entire file is ready, improving performance and memory usage for large files.

Example:
```javascript
const fs = require('fs');
const path = require('path');

app.get('/api/download/:filename', (req, res) => {
  const filename = req.params.filename;
  const filePath = path.join(__dirname, 'uploads', filename);
  
  // Check if file exists
  if (!fs.existsSync(filePath)) {
    return res.status(404).json({ error: 'File not found' });
  }
  
  // Set appropriate headers
  res.setHeader('Content-Disposition', `attachment; filename="${filename}"`);
  res.setHeader('Content-Type', 'application/octet-stream');
  
  // Stream the file
  const fileStream = fs.createReadStream(filePath);
  fileStream.pipe(res);
});
```

Deep Insight:
- Use streams for large file downloads
- Set appropriate Content-Disposition headers
- Handle file not found errors
- Consider resumable downloads for large files
- Monitor download progress and errors

## 68) How do you implement rate limiting for API endpoints (express-rate-limit)?

Concept: Rate limiting controls the number of requests a client can make within a time period, preventing abuse and ensuring fair resource usage.

Example:
```javascript
const rateLimit = require('express-rate-limit');

// General rate limiting
const limiter = rateLimit({
  windowMs: 15 * 60 * 1000, // 15 minutes
  max: 100, // limit each IP to 100 requests per windowMs
  message: 'Too many requests from this IP'
});

app.use('/api/', limiter);

// Specific endpoint rate limiting
const strictLimiter = rateLimit({
  windowMs: 60 * 1000, // 1 minute
  max: 5, // limit each IP to 5 requests per minute
  message: 'Too many login attempts'
});

app.post('/api/login', strictLimiter, (req, res) => {
  // Login logic
});
```

Deep Insight:
- Implement rate limiting to prevent abuse
- Use different limits for different endpoints
- Consider IP-based and user-based limiting
- Store rate limit data in Redis for distributed systems
- Provide clear error messages for rate limit exceeded

## 69) How do you implement logging for HTTP requests (morgan, pino)?

Concept: HTTP request logging captures request details, response status, and timing information, essential for monitoring, debugging, and analytics.

Example:
```javascript
const morgan = require('morgan');
const pino = require('pino');

// Morgan logging
app.use(morgan('combined'));

// Pino logging
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

Deep Insight:
- Use morgan for HTTP request logging
- Use pino for structured JSON logging
- Log important events and errors
- Consider log levels (info, warn, error)
- Use log aggregation tools for production

## 70) How do you version and document REST APIs (Swagger, OpenAPI)?

Concept: API versioning allows backward compatibility, while documentation helps developers understand and use APIs effectively.

Example:
```javascript
const swaggerJsdoc = require('swagger-jsdoc');
const swaggerUi = require('swagger-ui-express');

// Swagger configuration
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

// API versioning
app.use('/api/v1', v1Routes);
app.use('/api/v2', v2Routes);
```

Deep Insight:
- Use URL versioning (/api/v1, /api/v2)
- Document APIs with OpenAPI/Swagger
- Maintain backward compatibility
- Use semantic versioning for API versions
- Provide interactive API documentation
