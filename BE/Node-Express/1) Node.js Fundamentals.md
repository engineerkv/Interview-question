# 1) Node.js Fundamentals (Q1–10)

## 1) What is Node.js, and what problem does it solve?

Concept:
Node.js is a JavaScript runtime built on Chrome's V8 engine that enables server-side JavaScript execution, solving the problem of using JavaScript for both frontend and backend development.

Example:
```javascript
// Simple HTTP server
const http = require('http');
const server = http.createServer((req, res) => {
  res.writeHead(200, {'Content-Type': 'text/plain'});
  res.end('Hello World!');
});
server.listen(3000, () => console.log('Server running on port 3000'));
```

Deep Insight:
- Enables JavaScript everywhere - same language for frontend and backend
- Non-blocking I/O model makes it efficient for I/O-heavy applications
- Large ecosystem with npm package manager
- Single-threaded event loop handles thousands of concurrent connections
- Perfect for real-time applications, APIs, and microservices

## 2) Why is Node.js single-threaded, and how does it handle concurrency?

Concept: Node.js uses a single-threaded event loop to avoid context switching overhead and memory issues, handling concurrency through non-blocking I/O operations and the event loop.

Example:
```javascript
// Non-blocking operations
const fs = require('fs');
console.log('Start');
fs.readFile('large-file.txt', (err, data) => {
  console.log('File read complete');
});
console.log('End'); // This runs before file reading completes
```

Deep Insight:
- Single thread eliminates thread synchronization complexity
- Event loop processes multiple operations concurrently
- Non-blocking I/O allows thread to handle other requests while waiting
- Worker threads available for CPU-intensive tasks
- Memory efficient compared to traditional thread-per-request model

## 3) What is the role of the Event Loop, and how does it process asynchronous tasks?

Concept: The Event Loop is Node.js's core mechanism that continuously monitors the call stack and callback queue, executing callbacks when the stack is empty.

Example:
```javascript
console.log('1');
setTimeout(() => console.log('2'), 0);
setImmediate(() => console.log('3'));
process.nextTick(() => console.log('4'));
console.log('5');
// Output: 1, 5, 4, 2, 3
```

Deep Insight:
- Six phases: timers, pending callbacks, idle/prepare, poll, check, close callbacks
- Microtasks (process.nextTick, Promises) have higher priority than macrotasks
- Poll phase handles I/O events and timers
- Event loop continues until no more callbacks to execute
- Enables non-blocking behavior in single-threaded environment

## 4) Explain the difference between the call stack, callback queue, and microtask queue.

Concept: The call stack executes synchronous code, the callback queue holds I/O callbacks, and the microtask queue processes Promises and process.nextTick callbacks with higher priority.

Example:
```javascript
console.log('1'); // Call stack
setTimeout(() => console.log('2'), 0); // Callback queue
Promise.resolve().then(() => console.log('3')); // Microtask queue
process.nextTick(() => console.log('4')); // Microtask queue
console.log('5'); // Call stack
// Output: 1, 5, 4, 3, 2
```

Deep Insight:
- Call stack: LIFO structure for synchronous code execution
- Callback queue: FIFO queue for I/O and timer callbacks
- Microtask queue: Higher priority than callback queue
- process.nextTick has highest priority in microtask queue
- Event loop processes microtasks before macrotasks

## 5) What is non-blocking I/O, and why is it central to Node.js performance?

Concept: Non-blocking I/O allows Node.js to initiate I/O operations and continue executing other code without waiting for the operation to complete, dramatically improving performance for I/O-heavy applications.

Example:
```javascript
const fs = require('fs');
// Non-blocking file read
fs.readFile('data.txt', 'utf8', (err, data) => {
  if (err) throw err;
  console.log(data);
});
console.log('This runs immediately, not waiting for file read');
```

Deep Insight:
- Enables handling thousands of concurrent connections with single thread
- I/O operations are delegated to system kernel
- Callback executed when I/O completes
- Prevents thread blocking during I/O operations
- Core reason for Node.js's scalability and performance

## 6) What are the phases of the Event Loop in Node.js?

Concept: The Event Loop has six distinct phases that execute in order: timers, pending callbacks, idle/prepare, poll, check, and close callbacks, each handling specific types of operations.

Example:
```javascript
// Demonstrates different phases
setTimeout(() => console.log('Timer phase'), 0);
setImmediate(() => console.log('Check phase'));
process.nextTick(() => console.log('Microtask - highest priority'));
```

Deep Insight:
- Timers: Executes setTimeout and setInterval callbacks
- Pending callbacks: Executes I/O callbacks deferred to next loop iteration
- Idle/Prepare: Internal use only
- Poll: Fetches new I/O events and executes I/O callbacks
- Check: Executes setImmediate callbacks
- Close callbacks: Executes close event callbacks

## 7) What is the difference between process.nextTick(), setImmediate(), and setTimeout()?

Concept: process.nextTick() executes in the current phase, setImmediate() executes in the check phase, and setTimeout() executes in the timers phase, with different priorities and timing.

Example:
```javascript
setTimeout(() => console.log('setTimeout'), 0);
setImmediate(() => console.log('setImmediate'));
process.nextTick(() => console.log('process.nextTick'));
// Output: process.nextTick, setTimeout, setImmediate
```

Deep Insight:
- process.nextTick: Highest priority, executes before any other phase
- setImmediate: Executes in check phase, after I/O events
- setTimeout: Executes in timers phase, minimum 1ms delay
- process.nextTick can starve the event loop if used excessively
- setImmediate more efficient for I/O-heavy applications

## 8) What is the process object, and how can it be used to access environment information?

Concept: The process object is a global Node.js object that provides information about the current Node.js process and allows interaction with the operating system.

Example:
```javascript
console.log('Process ID:', process.pid);
console.log('Node version:', process.version);
console.log('Platform:', process.platform);
console.log('Environment:', process.env.NODE_ENV);
console.log('Memory usage:', process.memoryUsage());
```

Deep Insight:
- process.pid: Current process ID
- process.env: Environment variables object
- process.argv: Command line arguments array
- process.memoryUsage(): Memory consumption information
- process.cwd(): Current working directory

## 9) What is the difference between CommonJS and ES Modules in Node.js?

Concept: CommonJS uses require() and module.exports for synchronous loading, while ES Modules use import/export for asynchronous loading with static analysis capabilities.

Example:
```javascript
// CommonJS
const fs = require('fs');
module.exports = { readFile: fs.readFile };

// ES Modules
import fs from 'fs';
export { readFile: fs.readFile };
```

Deep Insight:
- CommonJS: Synchronous, runtime resolution, dynamic imports
- ES Modules: Asynchronous, compile-time resolution, static imports
- ES Modules support tree-shaking and better optimization
- CommonJS still default in Node.js, ES Modules require .mjs or package.json type
- Can mix both but with limitations and performance considerations

## 10) What is the role of the V8 engine in Node.js execution?

Concept: V8 is Google's JavaScript engine that compiles JavaScript to machine code, providing the runtime environment and performance optimizations for Node.js applications.

Example:
```javascript
// V8 optimizations in action
function optimizeMe(a, b) {
  return a + b; // V8 optimizes this with inline caching
}
// Repeated calls with same types trigger optimization
for (let i = 0; i < 1000000; i++) {
  optimizeMe(1, 2);
}
```

Deep Insight:
- Compiles JavaScript to optimized machine code
- Implements just-in-time (JIT) compilation
- Provides garbage collection and memory management
- Enables features like async/await and Promises
- Performance improvements directly benefit Node.js applications
