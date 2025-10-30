# 🚀 Node.js & Express Interview Questions

100 carefully curated questions covering Node.js and Express.js fundamentals to advanced concepts.

## 📋 Quick Navigation

| Section | Topic | Questions | Difficulty |
|---------|-------|-----------|------------|
| [1️⃣](#1-nodejs-fundamentals) | Node.js Fundamentals | Q1–10 | ⭐⭐ |
| [2️⃣](#2-modules-and-project-architecture) | Modules and Project Architecture | Q11–20 | ⭐⭐ |
| [3️⃣](#3-asynchronous-patterns--event-emitter) | Asynchronous Patterns & Event Emitter | Q21–30 | ⭐⭐⭐ |
| [4️⃣](#4-streams--buffers) | Streams & Buffers | Q31–40 | ⭐⭐⭐ |
| [5️⃣](#5-nodejs-internals--performance) | Node.js Internals & Performance | Q41–50 | ⭐⭐⭐⭐ |
| [6️⃣](#6-expressjs-core-concepts) | Express.js Core Concepts | Q51–60 | ⭐⭐⭐ |
| [7️⃣](#7-rest-apis--practical-server-scenarios) | REST APIs & Practical Server Scenarios | Q61–70 | ⭐⭐⭐ |
| [8️⃣](#8-authentication-security--encryption) | Authentication, Security & Encryption | Q71–80 | ⭐⭐⭐⭐ |
| [9️⃣](#9-performance-optimization-scaling--monitoring) | Performance, Optimization, Scaling & Monitoring | Q81–90 | ⭐⭐⭐⭐ |
| [🔟](#10-testing-debugging--deployment) | Testing, Debugging & Deployment | Q91–100 | ⭐⭐⭐⭐ |

## 🚀 1. Node.js Fundamentals

1. What is Node.js, and what problem does it solve?
2. Why is Node.js single-threaded, and how does it handle concurrency?
3. What is the role of the Event Loop, and how does it process asynchronous tasks?
4. What is the V8 engine, and how does it work with Node.js?
5. What is non-blocking I/O, and how does it work in Node.js?
6. What is the difference between `process.nextTick()` and `setImmediate()`?
7. What is the difference between `setTimeout()` and `setImmediate()`?
8. What is the difference between CommonJS and ES Modules?
9. How do you handle errors in Node.js applications?
10. What is the difference between `process.exit()` and `process.kill()`?

## 📦 2. Modules and Project Architecture

11. How does `require()` work in Node.js?
12. What is the difference between `import` and `require()`?
13. What is the difference between `exports` and `module.exports`?
14. How do you handle circular dependencies in Node.js?
15. How do you structure a Node.js project?
16. How do you handle environment variables in Node.js?
17. How do you manage secrets and configuration in Node.js?
18. How do you implement logging in Node.js applications?
19. How do you handle graceful shutdown in Node.js?
20. What are the best practices for Node.js project structure?

## ⚡ 3. Asynchronous Patterns & Event Emitter

21. What is callback hell, and how do you avoid it?
22. What are Promises, and how do you use them in Node.js?
23. What is async/await, and how does it work?
24. How do you handle errors in async/await?
25. What is the Event Emitter pattern, and how do you use it?
26. How do you create custom event emitters?
27. How do you handle concurrent I/O operations?
28. What are async iterators and generators?
29. How do you implement retry logic with async/await?
30. How do you handle timeouts in async operations?

## 🌊 4. Streams & Buffers

31. What are streams in Node.js, and why are they useful?
32. What are the different types of streams?
33. What is backpressure, and how do you handle it?
34. What are Buffers, and how do you use them?
35. How do you pipe streams together?
36. How do you handle file operations with streams?
37. How do you implement compression with streams?
38. How do you handle encoding and decoding with streams?
39. What is the `highWaterMark` option in streams?
40. How do you create custom streams?

## ⚙️ 5. Node.js Internals & Performance

41. What is Libuv, and how does it work with Node.js?
42. What is clustering in Node.js, and how do you implement it?
43. What are Worker Threads, and when do you use them?
44. How do you implement IPC (Inter-Process Communication)?
45. How do you identify and fix memory leaks in Node.js?
46. How do you use Node.js Inspector for debugging?
47. How do you profile Node.js applications?
48. How do you generate diagnostic reports in Node.js?
49. How do you optimize Node.js for latency vs throughput?
50. What are the performance characteristics of Node.js?

## 🌐 6. Express.js Core Concepts

51. What is Express.js, and how does it work?
52. What is middleware, and how do you use it?
53. What is the `next()` function in middleware?
54. How do you use `app.use()` vs `app.METHOD()`?
55. How do you implement routing in Express.js?
56. How do you serve static files with Express.js?
57. How do you parse JSON and form data in Express.js?
58. How do you handle errors in Express.js?
59. What is the difference between application-level and router-level middleware?
60. How do you integrate Express.js with the HTTP module?

## 🔌 7. REST APIs & Practical Server Scenarios

61. What are RESTful APIs, and how do you design them?
62. How do you implement input validation and sanitization?
63. How do you implement pagination in REST APIs?
64. What is the difference between PUT, PATCH, and POST?
65. How do you implement proper HTTP status codes?
66. How do you handle file uploads with multer?
67. How do you implement streamed downloads?
68. How do you implement rate limiting in Express.js?
69. How do you implement logging with morgan or pino?
70. How do you implement API versioning and documentation?

## 🔐 8. Authentication, Security & Encryption

71. What is the difference between session-based and token-based authentication?
72. How do you implement JWT authentication in Express.js?
73. How do you implement route guards and middleware?
74. How do you implement HTTP-only cookies for security?
75. How do you implement OAuth 2.0 in Express.js?
76. How do you implement CORS in Express.js?
77. How do you implement security headers with Helmet?
78. How do you prevent SQL injection, XSS, and CSRF attacks?
79. How do you implement password hashing with bcrypt or argon2?
80. How do you manage secrets and API keys securely?

## ⚡ 9. Performance, Optimization, Scaling & Monitoring

81. How do you identify performance bottlenecks in Node.js applications?
82. How do you optimize middleware for performance?
83. How do you optimize database queries in Node.js?
84. How do you implement clustering with PM2?
85. How do you implement horizontal scaling in Node.js?
86. How do you implement caching with Redis or LRU?
87. How do you optimize API response times?
88. How do you implement monitoring and alerting?
89. How do you detect and fix memory leaks?
90. How do you implement connection pooling and batching?

## 🧪 10. Testing, Debugging & Deployment

91. How do you write unit tests with Jest or Mocha?
92. How do you test API endpoints with Supertest?
93. How do you mock API calls in tests?
94. How do you debug Node.js applications with VS Code?
95. How do you debug with Chrome DevTools?
96. How do you implement CI/CD for Node.js applications?
97. How do you containerize Node.js applications with Docker?
98. How do you implement graceful shutdowns in production?
99. How do you handle environment configurations?
100. How do you deploy Node.js applications to the cloud?

---

## 📖 Complete Answer Guide

- [1) Node.js Fundamentals](1%20Node.js%20Fundamentals.md) - Q1-10
- [2) Modules and Project Architecture](2%20Modules%20and%20Project%20Architecture.md) - Q11-20
- [3) Asynchronous Patterns & Event Emitter](3%20Asynchronous%20Patterns%20%26%20Event%20Emitter.md) - Q21-30
- [4) Streams & Buffers](4%20Streams%20%26%20Buffers.md) - Q31-40
- [5) Node.js Internals & Performance](5%20Node.js%20Internals%20%26%20Performance.md) - Q41-50
- [6) Express.js Core Concepts](6%20Express.js%20Core%20Concepts.md) - Q51-60
- [7) REST APIs & Practical Server Scenarios](7%20REST%20APIs%20%26%20Practical%20Server%20Scenarios.md) - Q61-70
- [8) Authentication, Security & Encryption](8%20Authentication%20Security%20%26%20Encryption.md) - Q71-80
- [9) Performance, Optimization, Scaling & Monitoring](9%20Performance%20Optimization%20Scaling%20%26%20Monitoring.md) - Q81-90
- [10) Testing, Debugging & Deployment](10%20Testing%20Debugging%20%26%20Deployment.md) - Q91-100

## 📝 Cheatsheet

[Node-Express Interview Cheatsheet](Node-Express%20Interview%20Cheatsheet.md) - Quick reference guide