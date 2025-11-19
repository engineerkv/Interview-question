# 2) Modules and Project Architecture (Q11–20)

## Q11. What are modules in Node.js, and what types exist (core, local, third-party)?

Modules are reusable pieces of code that can be imported and used in other parts of an application - there are three main types: core modules (built-in like fs, http, path), local modules (project files like ./utils), and third-party modules (npm packages like express, lodash). Each module has its own scope and exports.

- **Trade-offs**: Core modules are built into Node.js and don't need installation - local modules are files in your project that you can organize however you want. Third-party modules are installed via npm and provide additional functionality - module resolution follows specific algorithm, but watch out - too many dependencies can bloat your project and create security vulnerabilities.

Example:

```javascript
const fs = require('fs');
const utils = require('./utils');
const express = require('express');
```

## Q12. What is the difference between require() and import?

require() is CommonJS synchronous loading (runtime resolution, dynamic), while import is ES Modules asynchronous loading with static analysis and better tree-shaking capabilities (compile-time resolution, static). ES Modules support tree-shaking for smaller bundles and have better optimization.

- **Trade-offs**: require() is synchronous with runtime resolution - import is asynchronous with compile-time resolution. ES Modules support tree-shaking for smaller bundles - require() can be used conditionally, import cannot. ES Modules have better optimization and dead code elimination, but watch out - mixing both can cause issues and requires careful configuration.

Example:

```javascript
const express = require('express');
const { readFile } = require('fs');

import express from 'express';
import { readFile } from 'fs';
```

## Q13. How does Node's module resolution algorithm work?

Node.js follows a specific algorithm to resolve module paths: checks core modules first (fs, http, path), then looks for local files with extensions (.js, .json, .node), then searches node_modules directories up the directory tree. Checks package.json main field for entry point and handles index.js as default when directory is required.

- **Trade-offs**: Checks core modules first - looks for local files with extensions. Searches node_modules directories up the directory tree - checks package.json main field for entry point. Handles index.js as default when directory is required, but watch out - deep node_modules searches can be slow, and resolution order matters for performance.

Example:

```javascript
require('fs');
require('./utils');
require('express');
require('lodash/map');
```

## Q14. What is the difference between exports and module.exports?

exports is a reference to module.exports, but reassigning exports breaks the reference - module.exports is the actual object returned by require(). You can mix both but exports must come first, and the common mistake is that `exports = {}` doesn't work.

- **Trade-offs**: exports is shorthand for module.exports - reassigning exports breaks the reference. module.exports is the actual returned object - can mix both but exports must come first. Common mistake: `exports = {}` doesn't work - always use module.exports for direct assignment.

Example:

```javascript
exports.name = 'John';
exports.age = 30;

module.exports = {
  name: 'John',
  age: 30
};
```

## Q15. What are circular dependencies, and how can they be avoided?

Circular dependencies occur when two or more modules require each other directly or indirectly, which can cause undefined exports during module loading - Node.js handles them but exports may be incomplete. Solution: restructure code to avoid mutual dependencies, use dependency injection or event emitters, or extract shared functionality to separate modules.

- **Trade-offs**: Can cause undefined exports during module loading - Node.js handles them but exports may be incomplete. Solution: restructure code to avoid mutual dependencies - use dependency injection or event emitters. Extract shared functionality to separate modules - proper architecture prevents circular dependencies from the start.

Example:

```javascript
// fileA.js
const fileB = require('./fileB');
module.exports = { name: 'A', b: fileB };

// fileB.js
const fileA = require('./fileA');
module.exports = { name: 'B', a: fileA };
```

## Q16. How do you structure a large-scale Node.js project (modular architecture)?

Large Node.js projects should follow modular architecture with clear separation of concerns (controllers, models, services, middleware), organized folder structure, and proper dependency management. Use barrel files for clean imports, implement dependency injection, follow consistent naming conventions, and use environment-based configuration.

- **Trade-offs**: Separate concerns: controllers, models, services, middleware - use barrel files for clean imports. Implement dependency injection - follow consistent naming conventions. Use environment-based configuration - implement proper error handling and logging. The catch is over-engineering can slow development, so balance structure with practicality.

Example:

```javascript
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

## Q17. What are environment-based configurations (.env, process.env)?

Environment-based configuration allows applications to use different settings for different environments (development, staging, production) using environment variables and .env files - .env files store environment variables locally, and process.env provides access to them. Never commit .env files to version control, and use libraries like dotenv for .env file loading.

- **Trade-offs**: .env files store environment variables locally - process.env provides access to environment variables. Different configs for different environments - never commit .env files to version control. Use libraries like dotenv for .env file loading - makes it easy to switch between environments, but watch out - forgetting to set environment variables can cause runtime errors.

Example:

```javascript
NODE_ENV=development
PORT=3000
DB_HOST=localhost
DB_PASSWORD=secret

const config = {
  port: process.env.PORT || 3000,
  dbHost: process.env.DB_HOST,
  nodeEnv: process.env.NODE_ENV
};
```

## Q18. How do you manage secrets and API keys securely in Node.js apps?

Secrets should be stored in environment variables, never in code, with proper access controls, encryption for sensitive data, and secure key management practices. Use different secrets for different environments, consider using secret management services (AWS Secrets Manager), encrypt sensitive data at rest and in transit, and rotate secrets regularly.

- **Trade-offs**: Store secrets in environment variables, not code - use different secrets for different environments. Implement proper access controls and permissions - consider using secret management services (AWS Secrets Manager). Encrypt sensitive data at rest and in transit - rotate secrets regularly, but watch out - managing secrets across multiple environments can be complex.

Example:

```javascript
const crypto = require('crypto');
const secretKey = process.env.SECRET_KEY;
const encryptedData = crypto.encrypt(data, secretKey);

const config = {
  jwtSecret: process.env.JWT_SECRET,
  dbPassword: process.env.DB_PASSWORD,
  apiKey: process.env.API_KEY
};
```

## Q19. What are barrel files, and how can they simplify imports?

Barrel files are index.js files that re-export multiple modules from a directory, providing a single entry point and simplifying import statements - they make refactoring easier by centralizing exports and reduce coupling. Common pattern in large applications, but can impact bundle size if not tree-shakeable.

- **Trade-offs**: Single entry point for multiple related modules - simplifies import statements and reduces coupling. Makes refactoring easier by centralizing exports - can impact bundle size if not tree-shakeable. Common pattern in large applications, but watch out - can lead to importing more than you need if not careful.

Example:

```javascript
module.exports = {
  ...require('./helpers'),
  ...require('./validators'),
  ...require('./formatters')
};

const { validateEmail, formatDate, sanitizeInput } = require('./utils');
```

## Q20. What is the difference between a monolith and microservices architecture in Node.js?

Monolith is a single deployable application with all functionality (single codebase, shared database, easier development), while microservices split functionality into independent, loosely coupled services that communicate over networks (separate databases, better scalability). Choose based on team size, complexity, and scalability needs.

- **Trade-offs**: Monolith: single codebase, shared database, easier development - simpler deployment, but harder to scale individual components. Microservices: independent services, separate databases, better scalability - complex deployment, but better fault isolation. Choose based on team size, complexity, and scalability needs - monoliths are easier to start, microservices are better for large teams and scale.

Example:

```javascript
const express = require('express');
const app = express();
app.use('/users', userRoutes);
app.use('/orders', orderRoutes);
app.use('/payments', paymentRoutes);

const userService = express();
userService.use('/users', userRoutes);
```
