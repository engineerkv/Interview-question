# 🔄 2. Async Patterns & Events (Q19–28)

---

## 📍 Navigation

<div align="center">

[← Previous: Node.js Fundamentals](01%29%20Node.js%20Fundamentals.md) • [Home: Question List](question.md) • [Next: Streams & Buffers →](03%29%20Streams%20%26%20Buffers.md)

[📋 Cheatsheet](Node-Express%20Interview%20Cheatsheet.md)

</div>

---

## Q19. 🔧 Callback hell and how to avoid it

Callback hell happens when you nest multiple callbacks inside each other, creating deeply nested code that's really hard to read and debug - it's like a pyramid of doom where each async operation needs another callback. The best way to avoid it is using async/await, which makes your code look like regular synchronous code, or Promises with .then() chains, or breaking things into named functions instead of inline callbacks.

- **Trade-offs**: The catch is nested callbacks make code hard to follow and debug - when you have 3-4 levels of nesting, it becomes a nightmare to maintain. Async/await is the cleanest solution for most cases - it reads like normal code and handles errors with try/catch, but watch out - you can still create callback hell if you nest too many async operations without breaking them into smaller functions.

Example:

```javascript
getData((err, data) => {
  if (err) return handleError(err);
  processData(data, (err, result) => {
    if (err) return handleError(err);
    saveData(result, (err, saved) => {
      if (err) return handleError(err);
      console.log('Done!');
    });
  });
});

```

## Q20. ⚡ Promises and how to use them in Node.js

A Promise is a placeholder for a value that you'll get later from an async operation - it can be in three states: pending (waiting), fulfilled (success), or rejected (error). When you create a promise, it runs immediately, and you use .then() to handle success and .catch() for errors - both return new promises so you can chain them together for sequential operations.

- **Trade-offs**: Promises run in the microtask queue, which means they execute before regular callbacks - this gives you predictable execution order. The catch is if you don't handle rejections with .catch() or try/catch, unhandled promise rejections can crash your app, so always make sure to catch errors somewhere in your promise chain.

Example:

```javascript
const promise = new Promise((resolve, reject) => {
  setTimeout(() => resolve('Success!'), 1000);
});

promise.then(result => console.log(result))
       .catch(error => console.error(error));

```

## Q21. ⚡ Async/await and how it works

async/await provides syntactic sugar over Promises, making asynchronous code look and behave like synchronous code - it eliminates callback nesting and promise chaining, uses try/catch for error handling, and makes code more readable and maintainable. async functions always return promises, and you can use await only inside async functions.

- **Trade-offs**: Eliminates callback nesting and promise chaining - uses try/catch for error handling. Makes code more readable and maintainable - async functions always return promises. Can use await only inside async functions - makes debugging easier with stack traces, but watch out - forgetting await can cause unexpected behavior.

Example:

```javascript
// Before async/await (Promise chaining)
getData()
  .then(data => processData(data)) // Chain promises
  .then(result => saveData(result))
  .catch(error => handleError(error)); // Single error handler

// With async/await: sequential async operations in synchronous style
async function processDataFlow() {
  try {
    const data = await getData(); // Wait for getData to complete
    const result = await processData(data); // Wait for processData
    await saveData(result); // Wait for saveData
    return result;
  } catch (error) {
    handleError(error); // Handle any errors in the chain
    throw error;
  }
}

// async functions always return promises
async function fetchUser(id) {
  return { id, name: 'John' }; // Automatically wrapped in Promise
}
const userPromise = fetchUser(1); // Returns a Promise (not unwrapped)
const user = await fetchUser(1); // Unwraps the Promise, gets the value

```

## Q22. ⚡ Handling errors in async/await

Error handling in async functions should use try/catch blocks around await expressions, proper error propagation, and consider both synchronous and asynchronous errors. Don't forget to throw or return errors, consider error boundaries and global error handlers, and log errors with context for debugging.

- **Trade-offs**: Use try/catch blocks around await expressions - handle both synchronous and asynchronous errors. Don't forget to throw or return errors - consider error boundaries and global error handlers. Log errors with context for debugging - unhandled promise rejections can crash your app, so always catch errors at the top level.

Example:

```javascript
async function handleAsyncOperation() {
  try {
    const data = await fetchData();
    const result = await processData(data);
    return result;
  } catch (error) {
    console.error('Operation failed:', error.message);
    throw new Error(`Processing failed: ${error.message}`);
  }
}

// Handling errors in async route handlers
app.get('/api/data', async (req, res, next) => {
  try {
    const data = await fetchData();
    res.json(data);
  } catch (error) {
    next(error); // Pass to error handler
  }
});

// Global error handler for unhandled rejections
process.on('unhandledRejection', (reason, promise) => {
  console.error('Unhandled Rejection:', reason);
  // Log to error tracking service
});

```

## Q23. 🔄 Event Emitter pattern and how to use it

Event Emitter is a Node.js pattern that allows objects to emit named events and register listeners for those events - it enables event-driven programming where components communicate through events instead of direct function calls. You use .on() to listen for events, .emit() to trigger events, and .off() to remove listeners - perfect for decoupling components and handling asynchronous events like file reads, HTTP requests, or custom application events.

- **Trade-offs**: Great for decoupling components - objects don't need direct references to each other. Supports multiple listeners for the same event - can pass data with events. Used by many Node.js core modules (fs, http) - makes code more flexible and maintainable, but watch out - too many event listeners can make code hard to follow and debug, and memory leaks can happen if you forget to remove listeners.

Example:

```javascript
const EventEmitter = require('events');
const emitter = new EventEmitter();

emitter.on('user-login', (user) => {
  console.log(`User ${user.name} logged in`);
});

emitter.on('user-login', (user) => {
  // Multiple listeners can handle same event
  updateUserActivity(user.id);
});

emitter.emit('user-login', { id: 1, name: 'John' });

```

## Q24. 🔄 Creating custom event emitters

EventEmitter is a Node.js class that enables objects to emit and listen for custom events, providing a foundation for event-driven programming - objects can emit custom events and listen for them, supports multiple listeners for same event, and can pass data with events. Used by many Node.js core modules (fs, http).

- **Trade-offs**: Enables event-driven programming patterns - objects can emit custom events and listen for them. Supports multiple listeners for same event - can pass data with events. Used by many Node.js core modules (fs, http) - great for decoupling components, but watch out - too many event listeners can make code hard to follow and debug.

Example:

```javascript
const EventEmitter = require('events');
class MyEmitter extends EventEmitter {}

const myEmitter = new MyEmitter();
myEmitter.on('data', (data) => {
  console.log('Received data:', data);
});
myEmitter.emit('data', 'Hello World!');

```

## Q25. 💡 Handling concurrent I/O operations

Node.js uses the event loop and non-blocking I/O to handle thousands of concurrent operations with a single thread - I/O operations are non-blocking and delegated to the operating system kernel, and the event loop processes completed operations. Can handle thousands of concurrent connections and is memory efficient compared to thread-per-request model.

- **Trade-offs**: Single thread handles all operations - I/O operations are non-blocking and delegated to OS. Event loop processes completed operations - can handle thousands of concurrent connections. Memory efficient compared to thread-per-request model, but watch out - CPU-intensive operations can block the event loop and hurt performance.

Example:

```javascript
const fs = require('fs');
const operations = ['file1.txt', 'file2.txt', 'file3.txt'];

operations.forEach(file => {
  fs.readFile(file, (err, data) => {
    if (err) throw err;
    console.log(`${file} read: ${data.length} bytes`);
  });
});
console.log('All operations initiated');

```

## Q26. ⚡ Async iterators and generators

Async iterators and generators provide a way to iterate over asynchronous data sources, useful for processing large datasets or streaming data without loading everything into memory - they process data as it becomes available, are memory efficient for large datasets, and can pause and resume execution. Combine with for-await-of loops.

- **Trade-offs**: Process data as it becomes available - memory efficient for large datasets. Useful for streaming and real-time data - can pause and resume execution. Combine with for-await-of loops - great for handling large files or streams, but watch out - error handling can be tricky with async iterators.

Example:

```javascript
async function* asyncGenerator() {
  for (let i = 0; i < 5; i++) {
    await new Promise(resolve => setTimeout(resolve, 100));
    yield i;
  }
}

(async () => {
  for await (const value of asyncGenerator()) {
    console.log(value);
  }
})();

```

## Q27. ⚡ Implementing retry logic with async/await

Retry logic allows you to automatically retry failed async operations with configurable attempts, delays, and backoff strategies - useful for handling transient failures like network timeouts or temporary service unavailability. You can implement it with a loop that catches errors and retries, or use exponential backoff to gradually increase delay between retries.

- **Trade-offs**: Handles transient failures automatically - can configure max attempts and delays. Exponential backoff reduces load on failing services - useful for network requests and external APIs. Can add jitter to prevent thundering herd problem, but watch out - retrying too many times or too quickly can overwhelm services, and some errors shouldn't be retried (like authentication failures).

Example:

```javascript
async function retryOperation(operation, maxAttempts = 3, delay = 1000) {
  for (let attempt = 1; attempt <= maxAttempts; attempt++) {
    try {
      return await operation();
    } catch (error) {
      if (attempt === maxAttempts) throw error;
      await new Promise(resolve => setTimeout(resolve, delay * attempt));
    }
  }
}

// With exponential backoff
async function retryWithBackoff(operation, maxAttempts = 3) {
  for (let attempt = 1; attempt <= maxAttempts; attempt++) {
    try {
      return await operation();
    } catch (error) {
      if (attempt === maxAttempts) throw error;
      const delay = Math.pow(2, attempt) * 1000; // Exponential backoff
      await new Promise(resolve => setTimeout(resolve, delay));
    }
  }
}

```

## Q28. ⚡ Handling timeouts in async operations

Timeouts prevent async operations from hanging indefinitely by rejecting or canceling them after a specified duration - useful for network requests, file operations, or any async task that might take too long. You can implement timeouts using Promise.race() with a timeout promise, or use AbortController for fetch requests.

- **Trade-offs**: Prevents operations from hanging indefinitely - useful for network requests and external APIs. Promise.race() is simple for basic timeouts - AbortController gives more control for canceling operations. Can combine with retry logic for robust error handling, but watch out - setting timeouts too short can cause false failures, and some operations can't be cleanly canceled.

Example:

```javascript
// Using Promise.race() for timeout
async function fetchWithTimeout(url, timeout = 5000) {
  const fetchPromise = fetch(url);
  const timeoutPromise = new Promise((_, reject) =>
    setTimeout(() => reject(new Error('Request timeout')), timeout)
  );
  return Promise.race([fetchPromise, timeoutPromise]);
}

// Using AbortController for fetch
async function fetchWithAbort(url, timeout = 5000) {
  const controller = new AbortController();
  const timeoutId = setTimeout(() => controller.abort(), timeout);
  try {
    const response = await fetch(url, { signal: controller.signal });
    clearTimeout(timeoutId);
    return response;
  } catch (error) {
    clearTimeout(timeoutId);
    if (error.name === 'AbortError') {
      throw new Error('Request timeout');
    }
    throw error;
  }
}

```

---

## 📍 Navigation

<div align="center">

[← Previous: Node.js Fundamentals](01%29%20Node.js%20Fundamentals.md) • [Home: Question List](question.md) • [Next: Streams & Buffers →](03%29%20Streams%20%26%20Buffers.md)

[📋 Cheatsheet](Node-Express%20Interview%20Cheatsheet.md)

</div>

---
