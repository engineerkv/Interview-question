# 5) Node.js Internals & Performance (Q41–50)

## Q41. What is Libuv, and what role does it play in Node.js?

Libuv is a C library that provides the event loop and handles asynchronous I/O operations, serving as the foundation for Node.js's non-blocking capabilities - it's a cross-platform asynchronous I/O library that provides event loop implementation, handles file system, network, and timer operations, and abstracts platform differences (Windows, Unix). Enables Node.js's single-threaded, non-blocking model.

- **Trade-offs**: Cross-platform asynchronous I/O library - provides event loop implementation. Handles file system, network, and timer operations - abstracts platform differences (Windows, Unix). Enables Node.js's single-threaded, non-blocking model - essential for Node.js performance, but watch out - understanding libuv helps debug async issues.

Example:

```javascript
const fs = require('fs');
const http = require('http');

fs.readFile('file.txt', (err, data) => {
  console.log(data);
});

http.createServer((req, res) => {
  res.end('Hello');
}).listen(3000);
```

## Q42. What is the difference between Clusters and Worker Threads?

Clusters create separate processes for CPU-intensive tasks (no shared memory, better isolation), while Worker Threads create separate threads within the same process for CPU-intensive tasks with shared memory (better performance). Use clusters for better fault tolerance and web servers, worker threads for CPU-intensive tasks with shared data and computations.

- **Trade-offs**: Clusters: separate processes, no shared memory, better isolation - Worker Threads: same process, shared memory, better performance. Use clusters for better fault tolerance - use worker threads for CPU-intensive tasks with shared data. Clusters are better for web servers, worker threads for computations - choose based on your use case and isolation needs.

Example:

```javascript
const cluster = require('cluster');
if (cluster.isMaster) {
  for (let i = 0; i < 4; i++) {
    cluster.fork();
  }
} else {
  require('./app.js');
}

const { Worker } = require('worker_threads');
const worker = new Worker('./cpu-intensive-task.js');
```

## Q43. How do you use the Cluster module to utilize multi-core CPUs?

The Cluster module allows Node.js to create multiple worker processes that share the same port, enabling utilization of all CPU cores for better performance - it creates separate processes for each CPU core, workers share the same port using round-robin load balancing, and master process manages worker lifecycle. Workers can be restarted on failure, improving performance for CPU-intensive applications.

- **Trade-offs**: Creates separate processes for each CPU core - workers share the same port using round-robin load balancing. Master process manages worker lifecycle - workers can be restarted on failure. Improves performance for CPU-intensive applications - great for utilizing all CPU cores, but watch out - each worker is a separate process with its own memory, so memory usage multiplies.

Example:

```javascript
const cluster = require('cluster');
const numCPUs = require('os').cpus().length;

if (cluster.isMaster) {
  console.log(`Master ${process.pid} is running`);
  for (let i = 0; i < numCPUs; i++) {
    cluster.fork();
  }
  cluster.on('exit', (worker) => {
    console.log(`Worker ${worker.process.pid} died`);
    cluster.fork();
  });
} else {
  require('./app.js');
}
```

## Q44. When should you prefer Worker Threads over Child Processes?

Use Worker Threads for CPU-intensive tasks that need shared memory and faster communication (same process), while Child Processes are better for isolation and fault tolerance (separate process, isolated memory, slower communication). Worker Threads are more efficient for frequent communication and CPU tasks with shared data.

- **Trade-offs**: Worker Threads: shared memory, faster communication, same process - Child Processes: isolated memory, slower communication, separate process. Use Worker Threads for CPU tasks with shared data - use Child Processes for better isolation and fault tolerance. Worker Threads are more efficient for frequent communication - choose based on whether you need isolation or performance.

Example:

```javascript
const { Worker, isMainThread, parentPort } = require('worker_threads');

if (isMainThread) {
  const worker = new Worker(__filename);
  worker.postMessage({ data: largeArray });
  worker.on('message', (result) => {
    console.log('Result:', result);
  });
} else {
  parentPort.on('message', ({ data }) => {
    const result = data.map(x => x * 2);
    parentPort.postMessage(result);
  });
}
```

## Q45. What is IPC (Inter-Process Communication) in Node.js?

IPC enables communication between different Node.js processes, allowing them to exchange messages, share data, and coordinate operations - it uses message passing for data exchange, supports JSON-serializable data only, and is essential for cluster and child process coordination. Can be used for distributed computing scenarios.

- **Trade-offs**: Enables communication between parent and child processes - uses message passing for data exchange. Supports JSON-serializable data only - essential for cluster and child process coordination. Can be used for distributed computing scenarios - makes it easy to coordinate multiple processes, but watch out - message passing has overhead, so avoid sending large objects frequently.

Example:

```javascript
const { spawn } = require('child_process');
const child = spawn('node', ['worker.js']);

child.send({ message: 'Hello from parent' });
child.on('message', (data) => {
  console.log('From child:', data);
});

process.on('message', (data) => {
  console.log('From parent:', data);
  process.send({ response: 'Hello from child' });
});
```

## Q46. How do you detect and handle memory leaks in Node.js?

Memory leaks occur when objects are not properly garbage collected, and can be detected using heap snapshots, monitoring tools, and proper coding practices - use process.memoryUsage() to monitor memory, take heap snapshots with --inspect flag, avoid global variables and closures, clear timers and event listeners, and use weak references for large objects.

- **Trade-offs**: Use process.memoryUsage() to monitor memory - take heap snapshots with --inspect flag. Avoid global variables and closures - clear timers and event listeners. Use weak references for large objects - monitoring helps catch leaks early, but watch out - memory leaks can be subtle, so use heap snapshots to identify what's holding references.

Example:

```javascript
const leakyArray = [];
setInterval(() => {
  leakyArray.push(new Array(1000).fill('leak'));
  console.log('Memory usage:', process.memoryUsage());
}, 1000);

const cleanup = () => {
  leakyArray.length = 0;
  clearInterval(interval);
};
```

## Q47. What is the Node.js Inspector, and how do you debug with it?

The Node.js Inspector is a debugging interface that allows you to debug Node.js applications using Chrome DevTools, providing breakpoints, profiling, and memory analysis - start with --inspect or --inspect-brk flags, connect Chrome DevTools to debugger, set breakpoints and step through code, profile CPU and memory usage, and debug async code and promises.

- **Trade-offs**: Start with --inspect or --inspect-brk flags - connect Chrome DevTools to debugger. Set breakpoints and step through code - profile CPU and memory usage. Debug async code and promises - powerful debugging tool, but watch out - inspector adds overhead, so don't use in production unless necessary.

Example:

```javascript
const debugPort = process.debugPort;
console.log(`Debugger listening on port ${debugPort}`);

function processData(data) {
  debugger;
  return data.map(item => item * 2);
}
```

## Q48. How do you profile CPU usage and detect performance bottlenecks?

Use profiling tools like the built-in profiler, Chrome DevTools, and monitoring libraries to identify CPU-intensive operations and optimize performance - use --prof flag for CPU profiling, analyze with --prof-process flag, use Chrome DevTools for visual profiling, monitor event loop lag, and identify hot spots and optimize algorithms.

- **Trade-offs**: Use --prof flag for CPU profiling - analyze with --prof-process flag. Use Chrome DevTools for visual profiling - monitor event loop lag. Identify hot spots and optimize algorithms - profiling helps find bottlenecks, but watch out - profiling adds overhead, so use it during development, not production.

Example:

```javascript
const { performance } = require('perf_hooks');

function cpuIntensiveTask() {
  const start = performance.now();
  let result = 0;
  for (let i = 0; i < 1000000; i++) {
    result += Math.sqrt(i);
  }
  const end = performance.now();
  console.log(`Task took ${end - start} milliseconds`);
  return result;
}
```

## Q49. What are diagnostic reports, and how can they help in production debugging?

Diagnostic reports are detailed snapshots of Node.js application state that help debug issues in production by capturing memory, CPU, and system information - they capture application state at specific moments, include memory usage, CPU usage, and stack traces, and can be triggered on errors or signals. Use for post-mortem analysis.

- **Trade-offs**: Capture application state at specific moments - include memory usage, CPU usage, and stack traces. Helpful for debugging production issues - can be triggered on errors or signals. Use for post-mortem analysis - great for debugging production issues, but watch out - reports can be large, so configure when they're generated to avoid filling disk space.

Example:

```javascript
process.report.writeReport('error-report.json');

process.on('uncaughtException', () => {
  process.report.writeReport();
});

process.report.reportOnFatalError = true;
process.report.reportOnSignal = true;
```

## Q50. How do you optimize Node.js applications for low latency and high throughput (event loop tuning, async improvements, caching)?

Optimize Node.js applications by tuning the event loop, improving async patterns, implementing caching strategies, and monitoring performance metrics - monitor event loop lag and CPU usage, use clustering for CPU-intensive tasks, implement caching for frequently accessed data, optimize database queries and connections, and use streaming for large data processing.

- **Trade-offs**: Monitor event loop lag and CPU usage - use clustering for CPU-intensive tasks. Implement caching for frequently accessed data - optimize database queries and connections. Use streaming for large data processing - multiple optimization strategies work together, but watch out - over-optimization can add complexity, so measure first and optimize based on actual bottlenecks.

Example:

```javascript
const { performance, PerformanceObserver } = require('perf_hooks');

const obs = new PerformanceObserver((list) => {
  const entries = list.getEntries();
  entries.forEach((entry) => {
    console.log(`Event loop lag: ${entry.duration}ms`);
  });
});
obs.observe({ entryTypes: ['measure'] });

const cache = new Map();
function getCachedData(key) {
  if (cache.has(key)) {
    return cache.get(key);
  }
  const data = expensiveOperation();
  cache.set(key, data);
  return data;
}
```
