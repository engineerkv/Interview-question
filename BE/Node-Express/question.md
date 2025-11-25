# 🚀 Node.js & Express Interview Questions

99 carefully curated questions covering Node.js and Express.js fundamentals to advanced concepts.

## 📋 Quick Navigation

| Section | Topic | Questions | Difficulty |
|---------|-------|-----------|------------|
| [1️⃣](#1-nodejs-fundamentals--modules) | Node.js Fundamentals & Modules | Q1–19 | ⭐⭐ |
| [2️⃣](#2-asynchronous-patterns--event-emitter) | Asynchronous Patterns & Event Emitter | Q20–29 | ⭐⭐⭐ |
| [3️⃣](#3-streams--buffers) | Streams & Buffers | Q30–39 | ⭐⭐⭐ |
| [4️⃣](#4-nodejs-internals--performance) | Node.js Internals & Performance | Q40–50 | ⭐⭐⭐⭐ |
| [5️⃣](#5-expressjs-core-concepts) | Express.js Core Concepts | Q51–60 | ⭐⭐⭐ |
| [6️⃣](#6-rest-apis--practical-server-scenarios) | REST APIs & Practical Server Scenarios | Q61–70 | ⭐⭐⭐ |
| [7️⃣](#7-authentication-security--encryption) | Authentication, Security & Encryption | Q71–80 | ⭐⭐⭐⭐ |
| [8️⃣](#8-performance-optimization-scaling--monitoring) | Performance, Optimization, Scaling & Monitoring | Q81–89 | ⭐⭐⭐⭐ |
| [9️⃣](#9-testing-debugging--deployment) | Testing, Debugging & Deployment | Q90–99 | ⭐⭐⭐⭐ |

## 🚀 1. Node.js Fundamentals & Modules

1. Node.js and what problem it solves
2. Why Node.js is single-threaded and how it handles concurrency
3. Event Loop: its role and how it processes asynchronous tasks
4. V8 engine and how it works with Node.js
5. Non-blocking I/O and how it works in Node.js
6. Process object: what it is in Node.js
7. `process.exit()` vs `process.kill()`
8. `process.nextTick()`, `setImmediate()`, and `setTimeout()`: differences
9. CommonJS vs ES Modules
10. Handling errors in Node.js applications
11. How `require()` works in Node.js
12. `import` vs `require()`
13. `exports` vs `module.exports`
14. Handling circular dependencies in Node.js
15. Structuring a Node.js project and best practices
16. Handling environment variables in Node.js
17. Managing secrets and configuration in Node.js
18. Implementing logging in Node.js applications
19. Handling graceful shutdown in Node.js

## ⚡ 2. Asynchronous Patterns & Event Emitter

20. Callback hell and how to avoid it
21. Promises and how to use them in Node.js
22. Async/await and how it works
23. Handling errors in async/await
24. Event Emitter pattern and how to use it
25. Creating custom event emitters
26. Handling concurrent I/O operations
27. Async iterators and generators
28. Implementing retry logic with async/await
29. Handling timeouts in async operations

## 🌊 3. Streams & Buffers

30. Streams in Node.js and why they're useful
31. Different types of streams
32. Backpressure and how to handle it
33. Buffers and how to use them
34. Piping streams together
35. Handling file operations with streams
36. Implementing compression with streams
37. Handling encoding and decoding with streams
38. `highWaterMark` option in streams
39. Creating custom streams

## ⚙️ 4. Node.js Internals & Performance

40. Libuv and how it works with Node.js
41. Thread Pool: what it is and how it works in Node.js
42. Clustering in Node.js and how to implement it
43. Worker Threads and when to use them
44. Implementing IPC (Inter-Process Communication)
45. Identifying and fixing memory leaks in Node.js
46. Using Node.js Inspector for debugging
47. Profiling Node.js applications
48. Generating diagnostic reports in Node.js
49. Optimizing Node.js for latency vs throughput
50. Performance characteristics of Node.js

## 🌐 5. Express.js Core Concepts

51. Express.js and how it works
52. Middleware and how to use it
53. `next()` function in middleware
54. `app.use()` vs `app.METHOD()`
55. Implementing routing in Express.js
56. Serving static files with Express.js
57. Parsing JSON and form data in Express.js
58. Handling errors in Express.js
59. Application-level vs router-level middleware
60. Integrating Express.js with the HTTP module

## 🔌 6. REST APIs & Practical Server Scenarios

61. RESTful APIs and how to design them
62. Implementing input validation and sanitization
63. Implementing pagination in REST APIs
64. PUT vs PATCH vs POST
65. Implementing proper HTTP status codes
66. Handling file uploads with multer
67. Implementing streamed downloads
68. Implementing rate limiting in Express.js
69. Implementing logging with morgan or pino
70. Implementing API versioning and documentation

## 🔐 7. Authentication, Security & Encryption

71. Session-based vs token-based authentication
72. Implementing JWT authentication in Express.js
73. Implementing route guards and middleware
74. Implementing HTTP-only cookies for security
75. Implementing OAuth 2.0 in Express.js
76. Implementing CORS in Express.js
77. Implementing security headers with Helmet
78. Preventing SQL injection, XSS, and CSRF attacks
79. Implementing password hashing with bcrypt or argon2
80. Managing secrets and API keys securely

## ⚡ 8. Performance, Optimization, Scaling & Monitoring

81. Identifying performance bottlenecks in Node.js applications
82. Optimizing middleware for performance
83. Optimizing database queries in Node.js
84. Implementing clustering with PM2
85. Implementing horizontal scaling in Node.js
86. Implementing caching with Redis or LRU
87. Optimizing API response times
88. Implementing monitoring and alerting
89. Implementing connection pooling and batching

## 🧪 9. Testing, Debugging & Deployment

90. Writing unit tests with Jest or Mocha
91. Testing API endpoints with Supertest
92. Mocking API calls in tests
93. Debugging Node.js applications with VS Code
94. Debugging with Chrome DevTools
95. Implementing CI/CD for Node.js applications
96. Containerizing Node.js applications with Docker
97. Implementing graceful shutdowns in production
98. Handling environment configurations
99. Deploying Node.js applications to the cloud

---

## 📖 Complete Answer Guide

- [1) Node.js Fundamentals & Modules](1%20Node.js%20Fundamentals.md) - Q1-19
- [2) Asynchronous Patterns & Event Emitter](2%20Asynchronous%20Patterns%20%26%20Event%20Emitter.md) - Q20-29
- [3) Streams & Buffers](3%20Streams%20%26%20Buffers.md) - Q30-39
- [4) Node.js Internals & Performance](4%20Node.js%20Internals%20%26%20Performance.md) - Q40-50
- [5) Express.js Core Concepts](5%20Express.js%20Core%20Concepts.md) - Q51-60
- [6) REST APIs & Practical Server Scenarios](6%20REST%20APIs%20%26%20Practical%20Server%20Scenarios.md) - Q61-70
- [7) Authentication, Security & Encryption](7%20Authentication%20Security%20%26%20Encryption.md) - Q71-80
- [8) Performance, Optimization, Scaling & Monitoring](8%20Performance%20Optimization%20Scaling%20%26%20Monitoring.md) - Q81-89
- [9) Testing, Debugging & Deployment](9%20Testing%20Debugging%20%26%20Deployment.md) - Q90-99

## 📝 Cheatsheet

[Node-Express Interview Cheatsheet](Node-Express%20Interview%20Cheatsheet.md) - Quick reference guide