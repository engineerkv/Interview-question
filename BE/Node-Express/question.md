# 🚀 Node.js & Express Interview Questions

98 carefully curated questions covering Node.js and Express.js fundamentals to advanced concepts.

## 📋 Quick Navigation

| Section | Topic | Questions | Difficulty |
|---------|-------|-----------|------------|
| [1️⃣](#1-nodejs-fundamentals--modules) | Node.js Fundamentals & Modules | Q1–18 | ⭐⭐ |
| [2️⃣](#2-asynchronous-patterns--event-emitter) | Asynchronous Patterns & Event Emitter | Q19–28 | ⭐⭐⭐ |
| [3️⃣](#3-streams--buffers) | Streams & Buffers | Q29–38 | ⭐⭐⭐ |
| [4️⃣](#4-nodejs-internals--performance) | Node.js Internals & Performance | Q39–49 | ⭐⭐⭐⭐ |
| [5️⃣](#5-expressjs-core-concepts) | Express.js Core Concepts | Q50–59 | ⭐⭐⭐ |
| [6️⃣](#6-rest-apis--practical-server-scenarios) | REST APIs & Practical Server Scenarios | Q60–69 | ⭐⭐⭐ |
| [7️⃣](#7-authentication-security--encryption) | Authentication, Security & Encryption | Q70–79 | ⭐⭐⭐⭐ |
| [8️⃣](#8-performance-optimization-scaling--monitoring) | Performance, Optimization, Scaling & Monitoring | Q80–88 | ⭐⭐⭐⭐ |
| [9️⃣](#9-testing-debugging--deployment) | Testing, Debugging & Deployment | Q89–98 | ⭐⭐⭐⭐ |

## 🚀 1. Node.js Fundamentals & Modules

1. Node.js and what problem it solves

2. Event Loop: its role and how it processes asynchronous tasks

3. V8 engine and how it works with Node.js

4. Non-blocking I/O and how it works in Node.js

5. Process object: what it is in Node.js

6. `process.exit()` vs `process.kill()`

7. `process.nextTick()`, `setImmediate()`, and `setTimeout()`: differences

8. CommonJS vs ES Modules

9. Handling errors in Node.js applications

10. How `require()` works in Node.js

11. `import` vs `require()`

12. `exports` vs `module.exports`

13. Handling circular dependencies in Node.js

14. Structuring a Node.js project and best practices

15. Handling environment variables in Node.js

16. Managing secrets and configuration in Node.js

17. Implementing logging in Node.js applications

18. Handling graceful shutdown in Node.js

## ⚡ 2. Asynchronous Patterns & Event Emitter

19. Callback hell and how to avoid it

20. Promises and how to use them in Node.js

21. Async/await and how it works

22. Handling errors in async/await

23. Event Emitter pattern and how to use it

24. Creating custom event emitters

25. Handling concurrent I/O operations

26. Async iterators and generators

27. Implementing retry logic with async/await

28. Handling timeouts in async operations

## 🌊 3. Streams & Buffers

29. Streams in Node.js and why they're useful

30. Different types of streams

31. Backpressure and how to handle it

32. Buffers and how to use them

33. Piping streams together

34. Handling file operations with streams

35. Implementing compression with streams

36. Handling encoding and decoding with streams

37. `highWaterMark` option in streams

38. Creating custom streams

## ⚙️ 4. Node.js Internals & Performance

39. Libuv and how it works with Node.js

40. Thread Pool: what it is and how it works in Node.js

41. Clustering in Node.js and how to implement it

42. Worker Threads and when to use them

43. Implementing IPC (Inter-Process Communication)

44. Identifying and fixing memory leaks in Node.js

45. Using Node.js Inspector for debugging

46. Profiling Node.js applications

47. Generating diagnostic reports in Node.js

48. Optimizing Node.js for latency vs throughput

49. Performance characteristics of Node.js

## 🌐 5. Express.js Core Concepts

50. Express.js and how it works

51. Middleware and how to use it

52. `next()` function in middleware

53. `app.use()` vs `app.METHOD()`

54. Implementing routing in Express.js

55. Serving static files with Express.js

56. Parsing JSON and form data in Express.js

57. Handling errors in Express.js

58. Application-level vs router-level middleware

59. Integrating Express.js with the HTTP module

## 🔌 6. REST APIs & Practical Server Scenarios

60. RESTful APIs and how to design them

61. Implementing input validation and sanitization

62. Implementing pagination in REST APIs

63. PUT vs PATCH vs POST

64. Implementing proper HTTP status codes

65. Handling file uploads with multer

66. Implementing streamed downloads

67. Implementing rate limiting in Express.js

68. Implementing logging with morgan or pino

69. Implementing API versioning and documentation

## 🔐 7. Authentication, Security & Encryption

70. Session-based vs token-based authentication

71. Implementing JWT authentication in Express.js

72. Implementing route guards and middleware

73. Implementing HTTP-only cookies for security

74. Implementing OAuth 2.0 in Express.js

75. Implementing CORS in Express.js

76. Implementing security headers with Helmet

77. Preventing SQL injection, XSS, and CSRF attacks

78. Implementing password hashing with bcrypt or argon2

79. Managing secrets and API keys securely

## ⚡ 8. Performance, Optimization, Scaling & Monitoring

80. Identifying performance bottlenecks in Node.js applications

81. Optimizing middleware for performance

82. Optimizing database queries in Node.js

83. Implementing clustering with PM2

84. Implementing horizontal scaling in Node.js

85. Implementing caching with Redis or LRU

86. Optimizing API response times

87. Implementing monitoring and alerting

88. Implementing connection pooling and batching

## 🧪 9. Testing, Debugging & Deployment

89. Writing unit tests with Jest or Mocha

90. Testing API endpoints with Supertest

91. Mocking API calls in tests

92. Debugging Node.js applications with VS Code

93. Debugging with Chrome DevTools

94. Implementing CI/CD for Node.js applications

95. Containerizing Node.js applications with Docker

96. Implementing graceful shutdowns in production

97. Handling environment configurations

98. Deploying Node.js applications to the cloud

---

## 📖 Complete Answer Guide

- [1) Node.js Fundamentals](1%29%20Node.js%20Fundamentals.md) - Q1-18

- [2) Asynchronous Patterns & Event Emitter](2%29%20Asynchronous%20Patterns%20%26%20Event%20Emitter.md) - Q19-28

- [3) Streams & Buffers](3%29%20Streams%20%26%20Buffers.md) - Q29-38

- [4) Node.js Internals & Performance](4%29%20Node.js%20Internals%20%26%20Performance.md) - Q39-49

- [5) Express.js Core Concepts](5%29%20Express.js%20Core%20Concepts.md) - Q50-59

- [6) REST APIs & Practical Server Scenarios](6%29%20REST%20APIs%20%26%20Practical%20Server%20Scenarios.md) - Q60-69

- [7) Authentication, Security & Encryption](7%29%20Authentication%2C%20Security%20%26%20Encryption.md) - Q70-79

- [8) Performance, Optimization, Scaling & Monitoring](8%29%20Performance%2C%20Optimization%2C%20Scaling%20%26%20Monitoring.md) - Q80-88

- [9) Testing, Debugging & Deployment](9%29%20Testing%2C%20Debugging%20%26%20Deployment.md) - Q89-98

## 📝 Cheatsheet

[Node-Express Interview Cheatsheet](Node-Express%20Interview%20Cheatsheet.md) - Quick reference guide
