# 1) Node.js Fundamentals (Q1–10)

## Q1. What is Node.js, and what problem does it solve?

Node.js is a JavaScript runtime built on Chrome's V8 engine that enables server-side JavaScript execution - it solves the problem of using JavaScript for both frontend and backend development, enabling JavaScript everywhere with the same language. Perfect for real-time applications, APIs, and microservices.

- **Trade-offs**: Enables JavaScript everywhere - same language for frontend and backend - non-blocking I/O model makes it efficient for I/O-heavy applications. Large ecosystem with npm package manager - single-threaded event loop handles thousands of concurrent connections, but watch out - CPU-intensive tasks can block the event loop.

Example:

```javascript
const http = require('http');
const server = http.createServer((req, res) => {
  res.writeHead(200, {'Content-Type': 'text/plain'});
  res.end('Hello World!');
});
server.listen(3000, () => console.log('Server running on port 3000'));
```

## Q2. Why is Node.js single-threaded, and how does it handle concurrency?

Node.js uses a single-threaded event loop to avoid context switching overhead and memory issues - it handles concurrency through non-blocking I/O operations and the event loop, allowing the thread to handle other requests while waiting for I/O to complete.

- **Trade-offs**: Single thread eliminates thread synchronization complexity - event loop processes multiple operations concurrently. Non-blocking I/O allows thread to handle other requests while waiting - worker threads available for CPU-intensive tasks. Memory efficient compared to traditional thread-per-request model, but watch out - CPU-intensive tasks can block the event loop.

Example:

```javascript
const fs = require('fs');
console.log('Start');
fs.readFile('large-file.txt', (err, data) => {
  console.log('File read complete');
});
console.log('End');
```

## Q3. What is the role of the Event Loop, and how does it process asynchronous tasks?

The Event Loop is Node.js's core mechanism that continuously monitors the call stack and callback queue, executing callbacks when the stack is empty - it has six phases (timers, pending callbacks, idle/prepare, poll, check, close callbacks) that process different types of operations. Enables non-blocking behavior in single-threaded environment.

- **Trade-offs**: Microtasks (process.nextTick, Promises) have higher priority than macrotasks - poll phase handles I/O events and timers. Event loop continues until no more callbacks to execute, but watch out - too many microtasks can starve the event loop and block I/O operations.

Example:

```javascript
console.log('1');
setTimeout(() => console.log('2'), 0);
setImmediate(() => console.log('3'));
process.nextTick(() => console.log('4'));
console.log('5');
// Output: 1, 5, 4, 2, 3
```

## Q4. Explain the difference between the call stack, callback queue, and microtask queue.

The call stack executes synchronous code (LIFO structure), the callback queue holds I/O callbacks (FIFO queue), and the microtask queue processes Promises and process.nextTick callbacks with higher priority - event loop processes microtasks before macrotasks, with process.nextTick having highest priority.

- **Trade-offs**: Call stack handles synchronous code execution - callback queue handles I/O and timer callbacks. Microtask queue has higher priority than callback queue - process.nextTick has highest priority in microtask queue, but watch out - too many microtasks can starve the event loop.

Example:

```javascript
console.log('1');
setTimeout(() => console.log('2'), 0);
Promise.resolve().then(() => console.log('3'));
process.nextTick(() => console.log('4'));
console.log('5');
// Output: 1, 5, 4, 3, 2
```

## Q5. What is non-blocking I/O, and why is it central to Node.js performance?

Non-blocking I/O allows Node.js to initiate I/O operations and continue executing other code without waiting for the operation to complete - I/O operations are delegated to system kernel, and callbacks execute when I/O completes. Core reason for Node.js's scalability and performance, enabling handling thousands of concurrent connections with single thread.

- **Trade-offs**: Prevents thread blocking during I/O operations - dramatically improves performance for I/O-heavy applications. Enables handling thousands of concurrent connections with single thread, but watch out - CPU-intensive operations still block the event loop.

Example:

```javascript
const fs = require('fs');
fs.readFile('data.txt', 'utf8', (err, data) => {
  if (err) throw err;
  console.log(data);
});
console.log('This runs immediately, not waiting for file read');
```

## Q6. What are the phases of the Event Loop in Node.js?

The Event Loop has six distinct phases that execute in order: timers (setTimeout/setInterval), pending callbacks (deferred I/O callbacks), idle/prepare (internal use), poll (fetches I/O events), check (setImmediate callbacks), and close callbacks (close events) - each phase handles specific types of operations.

- **Trade-offs**: Timers execute setTimeout and setInterval callbacks - poll phase fetches new I/O events and executes I/O callbacks. Check phase executes setImmediate callbacks - close callbacks execute close event callbacks. The catch is understanding phase order is crucial for debugging async behavior.

Example:

```javascript
setTimeout(() => console.log('Timer phase'), 0);
setImmediate(() => console.log('Check phase'));
process.nextTick(() => console.log('Microtask - highest priority'));
```

## Q7. What is the difference between process.nextTick(), setImmediate(), and setTimeout()?

process.nextTick() executes in the current phase (highest priority), setImmediate() executes in the check phase (after I/O events), and setTimeout() executes in the timers phase (minimum 1ms delay) - they have different priorities and timing, with process.nextTick having highest priority.

- **Trade-offs**: process.nextTick executes before any other phase - setImmediate executes in check phase, after I/O events. setTimeout executes in timers phase with minimum 1ms delay - setImmediate more efficient for I/O-heavy applications, but watch out - process.nextTick can starve the event loop if used excessively.

Example:

```javascript
setTimeout(() => console.log('setTimeout'), 0);
setImmediate(() => console.log('setImmediate'));
process.nextTick(() => console.log('process.nextTick'));
// Output: process.nextTick, setTimeout, setImmediate
```

## Q8. What is the process object, and how can it be used to access environment information?

The process object is a global Node.js object that provides information about the current Node.js process and allows interaction with the operating system - it gives you access to process ID, environment variables, command line arguments, memory usage, and current working directory.

- **Trade-offs**: process.pid gives current process ID - process.env provides environment variables object. process.argv contains command line arguments array - process.memoryUsage() shows memory consumption information. process.cwd() returns current working directory - useful for configuration and debugging.

Example:

```javascript
console.log('Process ID:', process.pid);
console.log('Node version:', process.version);
console.log('Platform:', process.platform);
console.log('Environment:', process.env.NODE_ENV);
console.log('Memory usage:', process.memoryUsage());
```

## Q9. What is the difference between CommonJS and ES Modules in Node.js?

CommonJS uses require() and module.exports for synchronous loading (runtime resolution, dynamic imports), while ES Modules use import/export for asynchronous loading with static analysis capabilities (compile-time resolution, static imports). ES Modules support tree-shaking and better optimization.

- **Trade-offs**: CommonJS is synchronous with runtime resolution - ES Modules are asynchronous with compile-time resolution. ES Modules support tree-shaking and better optimization - CommonJS still default in Node.js, ES Modules require .mjs or package.json type. Can mix both but with limitations and performance considerations.

Example:

```javascript
// CommonJS
const fs = require('fs');
module.exports = { readFile: fs.readFile };

// ES Modules
import fs from 'fs';
export { readFile: fs.readFile };
```

## Q10. What is the role of the V8 engine in Node.js execution?

V8 is Google's JavaScript engine that compiles JavaScript to optimized machine code using just-in-time (JIT) compilation - it provides the runtime environment, garbage collection, memory management, and performance optimizations for Node.js applications. Enables features like async/await and Promises.

- **Trade-offs**: Compiles JavaScript to optimized machine code - implements just-in-time (JIT) compilation for better performance. Provides garbage collection and memory management - enables features like async/await and Promises. Performance improvements directly benefit Node.js applications - V8 optimizations like inline caching improve hot code paths.

Example:

```javascript
function optimizeMe(a, b) {
  return a + b;
}
for (let i = 0; i < 1000000; i++) {
  optimizeMe(1, 2);
}
```
