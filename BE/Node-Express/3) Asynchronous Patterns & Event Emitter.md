# 3) Asynchronous Patterns & Event Emitter (Q21–30)

## 21) What is callback hell, and how do you avoid it?

Concept: Callback hell occurs when multiple nested callbacks create deeply indented, hard-to-read code that's difficult to maintain and debug.

Example:
```javascript
// Callback hell
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

Deep Insight:
- Results from deeply nested asynchronous operations
- Makes code hard to read, debug, and maintain
- Solutions: Promises, async/await, named functions
- Use libraries like async.js for complex flows
- Break down complex operations into smaller functions

## 22) How do Promises work internally in Node.js?

Concept: Promises are objects representing eventual completion of asynchronous operations, with three states: pending, fulfilled, or rejected, and they use the microtask queue for execution.

Example:
```javascript
// Promise creation and usage
const promise = new Promise((resolve, reject) => {
  setTimeout(() => resolve('Success!'), 1000);
});

promise.then(result => console.log(result))
       .catch(error => console.error(error));
```

Deep Insight:
- Three states: pending, fulfilled, rejected
- Executed in microtask queue (higher priority than callbacks)
- .then() and .catch() return new promises
- Promise constructor executes immediately
- Can be chained for sequential operations

## 23) What is the difference between Promise.all(), Promise.any(), and Promise.allSettled()?

Concept: Promise.all() waits for all promises to resolve or any to reject, Promise.any() resolves when any promise resolves, and Promise.allSettled() waits for all promises to complete regardless of outcome.

Example:
```javascript
const promises = [promise1, promise2, promise3];

// All must succeed
Promise.all(promises).then(results => console.log(results));

// Any can succeed
Promise.any(promises).then(result => console.log(result));

// All complete regardless of outcome
Promise.allSettled(promises).then(results => console.log(results));
```

Deep Insight:
- Promise.all(): Fails fast if any promise rejects
- Promise.any(): Succeeds fast if any promise resolves
- Promise.allSettled(): Always waits for all promises
- Use Promise.all() for dependent operations
- Use Promise.any() for fallback scenarios

## 24) How does async/await improve asynchronous code readability?

Concept: async/await provides syntactic sugar over Promises, making asynchronous code look and behave like synchronous code, improving readability and error handling.

Example:
```javascript
// With Promises
getData()
  .then(data => processData(data))
  .then(result => saveData(result))
  .catch(error => handleError(error));

// With async/await
try {
  const data = await getData();
  const result = await processData(data);
  await saveData(result);
} catch (error) {
  handleError(error);
}
```

Deep Insight:
- Eliminates callback nesting and promise chaining
- Uses try/catch for error handling
- Makes code more readable and maintainable
- async functions always return promises
- Can use await only inside async functions

## 25) How do you handle errors in async functions properly?

Concept: Error handling in async functions should use try/catch blocks, proper error propagation, and consider both synchronous and asynchronous errors.

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

Deep Insight:
- Use try/catch blocks around await expressions
- Handle both synchronous and asynchronous errors
- Don't forget to throw or return errors
- Consider error boundaries and global error handlers
- Log errors with context for debugging

## 26) What is an EventEmitter, and how do you use it to build custom events?

Concept: EventEmitter is a Node.js class that enables objects to emit and listen for custom events, providing a foundation for event-driven programming.

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

Deep Insight:
- Enables event-driven programming patterns
- Objects can emit custom events and listen for them
- Supports multiple listeners for same event
- Can pass data with events
- Used by many Node.js core modules (fs, http)

## 27) How does Node.js handle multiple concurrent I/O operations efficiently?

Concept: Node.js uses the event loop and non-blocking I/O to handle thousands of concurrent operations with a single thread, delegating I/O to the operating system kernel.

Example:
```javascript
// Multiple concurrent operations
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

Deep Insight:
- Single thread handles all operations
- I/O operations are non-blocking and delegated to OS
- Event loop processes completed operations
- Can handle thousands of concurrent connections
- Memory efficient compared to thread-per-request model

## 28) What is the difference between parallel and sequential async processing?

Concept: Parallel processing executes multiple async operations simultaneously, while sequential processing waits for each operation to complete before starting the next one.

Example:
```javascript
// Sequential processing
async function sequential() {
  const result1 = await operation1();
  const result2 = await operation2();
  const result3 = await operation3();
  return [result1, result2, result3];
}

// Parallel processing
async function parallel() {
  const [result1, result2, result3] = await Promise.all([
    operation1(), operation2(), operation3()
  ]);
  return [result1, result2, result3];
}
```

Deep Insight:
- Sequential: Slower but uses less resources
- Parallel: Faster but uses more resources
- Use sequential when operations depend on each other
- Use parallel when operations are independent
- Consider resource limits and rate limiting

## 29) What are async iterators and generators, and when should you use them?

Concept: Async iterators and generators provide a way to iterate over asynchronous data sources, useful for processing large datasets or streaming data without loading everything into memory.

Example:
```javascript
// Async generator
async function* asyncGenerator() {
  for (let i = 0; i < 5; i++) {
    await new Promise(resolve => setTimeout(resolve, 100));
    yield i;
  }
}

// Using async iterator
(async () => {
  for await (const value of asyncGenerator()) {
    console.log(value);
  }
})();
```

Deep Insight:
- Process data as it becomes available
- Memory efficient for large datasets
- Useful for streaming and real-time data
- Can pause and resume execution
- Combine with for-await-of loops

## 30) How can you create a custom Promise-based API in Node.js?

Concept: Wrap callback-based APIs with Promises using the Promise constructor, handling both success and error cases properly.

Example:
```javascript
// Wrapping callback-based API
function readFilePromise(filename) {
  return new Promise((resolve, reject) => {
    fs.readFile(filename, 'utf8', (err, data) => {
      if (err) reject(err);
      else resolve(data);
    });
  });
}

// Using the Promise-based API
readFilePromise('data.txt')
  .then(data => console.log(data))
  .catch(err => console.error(err));
```

Deep Insight:
- Use Promise constructor to wrap callbacks
- Handle both resolve and reject cases
- Consider using util.promisify for simple cases
- Maintain error handling consistency
- Can be combined with async/await for cleaner code
