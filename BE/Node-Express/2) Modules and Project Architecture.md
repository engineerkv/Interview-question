# 2) Modules and Project Architecture (Q11–20)

## 11) What are modules in Node.js, and what types exist (core, local, third-party)?

Concept: Modules are reusable pieces of code that can be imported and used in other parts of an application, with three main types: core modules (built-in), local modules (project files), and third-party modules (npm packages).

Example:
```javascript
// Core module
const fs = require('fs');
// Local module
const utils = require('./utils');
// Third-party module
const express = require('express');
```

Deep Insight:
- Core modules: Built into Node.js (fs, http, path, crypto)
- Local modules: Files in your project (./utils, ../config)
- Third-party modules: Installed via npm (express, lodash, mongoose)
- Module resolution follows specific algorithm
- Each module has its own scope and exports

## 12) What is the difference between require() and import?

Concept: require() is CommonJS synchronous loading, while import is ES Modules asynchronous loading with static analysis and better tree-shaking capabilities.

Example:
```javascript
// CommonJS with require
const express = require('express');
const { readFile } = require('fs');

// ES Modules with import
import express from 'express';
import { readFile } from 'fs';
```

Deep Insight:
- require(): Synchronous, runtime resolution, dynamic
- import: Asynchronous, compile-time resolution, static
- ES Modules support tree-shaking for smaller bundles
- require() can be used conditionally, import cannot
- ES Modules have better optimization and dead code elimination

## 13) How does Node's module resolution algorithm work?

Concept: Node.js follows a specific algorithm to resolve module paths: core modules first, then local files, then node_modules directories, with specific file extensions and package.json main field handling.

Example:
```javascript
// Resolution order
require('fs'); // Core module
require('./utils'); // Local file
require('express'); // Third-party from node_modules
require('lodash/map'); // Specific file in package
```

Deep Insight:
- Checks core modules first (fs, http, path)
- Looks for local files with extensions (.js, .json, .node)
- Searches node_modules directories up the directory tree
- Checks package.json main field for entry point
- Handles index.js as default when directory is required

## 14) What is the difference between exports and module.exports?

Concept: exports is a reference to module.exports, but reassigning exports breaks the reference, while module.exports is the actual object returned by require().

Example:
```javascript
// Using exports (reference)
exports.name = 'John';
exports.age = 30;

// Using module.exports (direct assignment)
module.exports = {
  name: 'John',
  age: 30
};
```

Deep Insight:
- exports is shorthand for module.exports
- Reassigning exports breaks the reference
- module.exports is the actual returned object
- Can mix both but exports must come first
- Common mistake: exports = {} doesn't work

## 15) What are circular dependencies, and how can they be avoided?

Concept: Circular dependencies occur when two or more modules require each other directly or indirectly, which can cause undefined exports and should be avoided through proper architecture.

Example:
```javascript
// fileA.js
const fileB = require('./fileB');
module.exports = { name: 'A', b: fileB };

// fileB.js
const fileA = require('./fileA'); // Circular dependency
module.exports = { name: 'B', a: fileA };
```

Deep Insight:
- Can cause undefined exports during module loading
- Node.js handles them but exports may be incomplete
- Solution: Restructure code to avoid mutual dependencies
- Use dependency injection or event emitters
- Extract shared functionality to separate modules

## 16) How do you structure a large-scale Node.js project (modular architecture)?

Concept: Large Node.js projects should follow modular architecture with clear separation of concerns, organized folder structure, and proper dependency management.

Example:
```javascript
// Project structure
src/
  controllers/
    userController.js
  models/
    User.js
  services/
    userService.js
  middleware/
    auth.js
  routes/
    userRoutes.js
  utils/
    helpers.js
  config/
    database.js
```

Deep Insight:
- Separate concerns: controllers, models, services, middleware
- Use barrel files for clean imports
- Implement dependency injection
- Follow consistent naming conventions
- Use environment-based configuration
- Implement proper error handling and logging

## 17) What are environment-based configurations (.env, process.env)?

Concept: Environment-based configuration allows applications to use different settings for different environments (development, staging, production) using environment variables and .env files.

Example:
```javascript
// .env file
NODE_ENV=development
PORT=3000
DB_HOST=localhost
DB_PASSWORD=secret

// Using in code
const config = {
  port: process.env.PORT || 3000,
  dbHost: process.env.DB_HOST,
  nodeEnv: process.env.NODE_ENV
};
```

Deep Insight:
- .env files store environment variables locally
- process.env provides access to environment variables
- Different configs for different environments
- Never commit .env files to version control
- Use libraries like dotenv for .env file loading

## 18) How do you manage secrets and API keys securely in Node.js apps?

Concept: Secrets should be stored in environment variables, never in code, with proper access controls, encryption for sensitive data, and secure key management practices.

Example:
```javascript
// Secure secret management
const crypto = require('crypto');
const secretKey = process.env.SECRET_KEY;
const encryptedData = crypto.encrypt(data, secretKey);

// Using environment variables
const config = {
  jwtSecret: process.env.JWT_SECRET,
  dbPassword: process.env.DB_PASSWORD,
  apiKey: process.env.API_KEY
};
```

Deep Insight:
- Store secrets in environment variables, not code
- Use different secrets for different environments
- Implement proper access controls and permissions
- Consider using secret management services (AWS Secrets Manager)
- Encrypt sensitive data at rest and in transit
- Rotate secrets regularly

## 19) What are barrel files, and how can they simplify imports?

Concept: Barrel files are index.js files that re-export multiple modules from a directory, providing a single entry point and simplifying import statements.

Example:
```javascript
// utils/index.js (barrel file)
module.exports = {
  ...require('./helpers'),
  ...require('./validators'),
  ...require('./formatters')
};

// Usage
const { validateEmail, formatDate, sanitizeInput } = require('./utils');
```

Deep Insight:
- Single entry point for multiple related modules
- Simplifies import statements and reduces coupling
- Makes refactoring easier by centralizing exports
- Can impact bundle size if not tree-shakeable
- Common pattern in large applications

## 20) What is the difference between a monolith and microservices architecture in Node.js?

Concept: Monolith is a single deployable application with all functionality, while microservices split functionality into independent, loosely coupled services that communicate over networks.

Example:
```javascript
// Monolith - single app
const express = require('express');
const app = express();
app.use('/users', userRoutes);
app.use('/orders', orderRoutes);
app.use('/payments', paymentRoutes);

// Microservice - user service
const userService = express();
userService.use('/users', userRoutes);
// Separate deployment and database
```

Deep Insight:
- Monolith: Single codebase, shared database, easier development
- Microservices: Independent services, separate databases, better scalability
- Monolith: Simpler deployment, harder to scale individual components
- Microservices: Complex deployment, better fault isolation
- Choose based on team size, complexity, and scalability needs
