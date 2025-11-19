# 3) Asynchronous Patterns & Event Emitter (Q21–30)

## Q21. What is callback hell, and how do you avoid it?

Callback hell occurs when multiple nested callbacks create deeply indented, hard-to-read code that's difficult to maintain and debug - it results from deeply nested asynchronous operations. Solutions: use Promises, async/await, named functions, or libraries like async.js for complex flows, and break down complex operations into smaller functions.

- **Trade-offs**: Makes code hard to read, debug, and maintain - results from deeply nested asynchronous operations. Solutions: Promises, async/await, named functions - use libraries like async.js for complex flows. Break down complex operations into smaller functions - async/await is the cleanest solution for most cases.

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

## Q22. How do Promises work internally in Node.js?

Promises are objects representing eventual completion of asynchronous operations, with three states: pending, fulfilled, or rejected - they use the microtask queue for execution (higher priority than callbacks). Promise constructor executes immediately, and .then() and .catch() return new promises that can be chained for sequential operations.

- **Trade-offs**: Three states: pending, fulfilled, rejected - executed in microtask queue (higher priority than callbacks). .then() and .catch() return new promises - Promise constructor executes immediately. Can be chained for sequential operations, but watch out - unhandled promise rejections can cause issues, so always use .catch() or try/catch with async/await.

Example:

```javascript
const promise = new Promise((resolve, reject) => {
  setTimeout(() => resolve('Success!'), 1000);
});

promise.then(result => console.log(result))
       .catch(error => console.error(error));
```

## Q23. What is the difference between Promise.all(), Promise.any(), and Promise.allSettled()?

Promise.all() waits for all promises to resolve or any to reject (fails fast), Promise.any() resolves when any promise resolves (succeeds fast), and Promise.allSettled() waits for all promises to complete regardless of outcome. Use Promise.all() for dependent operations, Promise.any() for fallback scenarios.

- **Trade-offs**: Promise.all() fails fast if any promise rejects - Promise.any() succeeds fast if any promise resolves. Promise.allSettled() always waits for all promises - use Promise.all() for dependent operations. Use Promise.any() for fallback scenarios - Promise.allSettled() is useful when you need all results even if some fail.

Example:

```javascript
const promises = [promise1, promise2, promise3];

Promise.all(promises).then(results => console.log(results));
Promise.any(promises).then(result => console.log(result));
Promise.allSettled(promises).then(results => console.log(results));
```

## Q24. How does async/await improve asynchronous code readability?

async/await provides syntactic sugar over Promises, making asynchronous code look and behave like synchronous code - it eliminates callback nesting and promise chaining, uses try/catch for error handling, and makes code more readable and maintainable. async functions always return promises, and you can use await only inside async functions.

- **Trade-offs**: Eliminates callback nesting and promise chaining - uses try/catch for error handling. Makes code more readable and maintainable - async functions always return promises. Can use await only inside async functions - makes debugging easier with stack traces, but watch out - forgetting await can cause unexpected behavior.

Example:

```javascript
getData()
  .then(data => processData(data))
  .then(result => saveData(result))
  .catch(error => handleError(error));

try {
  const data = await getData();
  const result = await processData(data);
  await saveData(result);
} catch (error) {
  handleError(error);
}
```

## Q25. How do you handle errors in async functions properly?

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
```

## Q26. What is an EventEmitter, and how do you use it to build custom events?

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

## Q27. How does Node.js handle multiple concurrent I/O operations efficiently?

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

## Q28. What is the difference between parallel and sequential async processing?

Parallel processing executes multiple async operations simultaneously (faster but uses more resources), while sequential processing waits for each operation to complete before starting the next one (slower but uses less resources). Use sequential when operations depend on each other, parallel when operations are independent, and consider resource limits and rate limiting.

- **Trade-offs**: Sequential: slower but uses less resources - parallel: faster but uses more resources. Use sequential when operations depend on each other - use parallel when operations are independent. Consider resource limits and rate limiting - parallel processing can overwhelm systems if not controlled, so use Promise.all() carefully.

Example:

```javascript
async function sequential() {
  const result1 = await operation1();
  const result2 = await operation2();
  const result3 = await operation3();
  return [result1, result2, result3];
}

async function parallel() {
  const [result1, result2, result3] = await Promise.all([
    operation1(), operation2(), operation3()
  ]);
  return [result1, result2, result3];
}
```

## Q29. What are async iterators and generators, and when should you use them?

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

## Q30. How can you create a custom Promise-based API in Node.js?

Wrap callback-based APIs with Promises using the Promise constructor, handling both success and error cases properly - use Promise constructor to wrap callbacks, handle both resolve and reject cases, and consider using util.promisify for simple cases. Can be combined with async/await for cleaner code.

- **Trade-offs**: Use Promise constructor to wrap callbacks - handle both resolve and reject cases. Consider using util.promisify for simple cases - maintain error handling consistency. Can be combined with async/await for cleaner code - makes callback-based APIs easier to use, but watch out - make sure to handle all error cases properly.

Example:

```javascript
function readFilePromise(filename) {
  return new Promise((resolve, reject) => {
    fs.readFile(filename, 'utf8', (err, data) => {
      if (err) reject(err);
      else resolve(data);
    });
  });
}

readFilePromise('data.txt')
  .then(data => console.log(data))
  .catch(err => console.error(err));
```
