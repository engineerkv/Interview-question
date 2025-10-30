# 5) Node.js Internals & Performance (Q41–50)

## 41) What is Libuv, and what role does it play in Node.js?

Concept: Libuv is a C library that provides the event loop and handles asynchronous I/O operations, serving as the foundation for Node.js's non-blocking capabilities.

Example:
```javascript
// Libuv handles these operations
const fs = require('fs');
const http = require('http');

// File I/O (handled by libuv)
fs.readFile('file.txt', (err, data) => {
  console.log(data);
});

// Network I/O (handled by libuv)
http.createServer((req, res) => {
  res.end('Hello');
}).listen(3000);
```

Deep Insight:
- Cross-platform asynchronous I/O library
- Provides event loop implementation
- Handles file system, network, and timer operations
- Abstracts platform differences (Windows, Unix)
- Enables Node.js's single-threaded, non-blocking model

## 42) What is the difference between Clusters and Worker Threads?

Concept: Clusters create separate processes for CPU-intensive tasks, while Worker Threads create separate threads within the same process for CPU-intensive tasks with shared memory.

Example:
```javascript
// Cluster - separate processes
const cluster = require('cluster');
if (cluster.isMaster) {
  for (let i = 0; i < 4; i++) {
    cluster.fork();
  }
} else {
  // Worker process
  require('./app.js');
}

// Worker Threads - separate threads
const { Worker } = require('worker_threads');
const worker = new Worker('./cpu-intensive-task.js');
```

Deep Insight:
- Clusters: Separate processes, no shared memory, better isolation
- Worker Threads: Same process, shared memory, better performance
- Use clusters for better fault tolerance
- Use worker threads for CPU-intensive tasks with shared data
- Clusters are better for web servers, worker threads for computations

## 43) How do you use the Cluster module to utilize multi-core CPUs?

Concept: The Cluster module allows Node.js to create multiple worker processes that share the same port, enabling utilization of all CPU cores for better performance.

Example:
```javascript
const cluster = require('cluster');
const numCPUs = require('os').cpus().length;

if (cluster.isMaster) {
  console.log(`Master ${process.pid} is running`);
  
  // Fork workers
  for (let i = 0; i < numCPUs; i++) {
    cluster.fork();
  }
  
  cluster.on('exit', (worker) => {
    console.log(`Worker ${worker.process.pid} died`);
    cluster.fork(); // Restart worker
  });
} else {
  // Worker processes
  require('./app.js');
}
```

Deep Insight:
- Creates separate processes for each CPU core
- Workers share the same port using round-robin load balancing
- Master process manages worker lifecycle
- Workers can be restarted on failure
- Improves performance for CPU-intensive applications

## 44) When should you prefer Worker Threads over Child Processes?

Concept: Use Worker Threads for CPU-intensive tasks that need shared memory and faster communication, while Child Processes are better for isolation and fault tolerance.

Example:
```javascript
// Worker Threads for CPU-intensive tasks
const { Worker, isMainThread, parentPort } = require('worker_threads');

if (isMainThread) {
  const worker = new Worker(__filename);
  worker.postMessage({ data: largeArray });
  worker.on('message', (result) => {
    console.log('Result:', result);
  });
} else {
  parentPort.on('message', ({ data }) => {
    const result = data.map(x => x * 2); // CPU-intensive
    parentPort.postMessage(result);
  });
}
```

Deep Insight:
- Worker Threads: Shared memory, faster communication, same process
- Child Processes: Isolated memory, slower communication, separate process
- Use Worker Threads for CPU tasks with shared data
- Use Child Processes for better isolation and fault tolerance
- Worker Threads are more efficient for frequent communication

## 45) What is IPC (Inter-Process Communication) in Node.js?

Concept: IPC enables communication between different Node.js processes, allowing them to exchange messages, share data, and coordinate operations.

Example:
```javascript
// Parent process
const { spawn } = require('child_process');
const child = spawn('node', ['worker.js']);

child.send({ message: 'Hello from parent' });
child.on('message', (data) => {
  console.log('From child:', data);
});

// Child process (worker.js)
process.on('message', (data) => {
  console.log('From parent:', data);
  process.send({ response: 'Hello from child' });
});
```

Deep Insight:
- Enables communication between parent and child processes
- Uses message passing for data exchange
- Supports JSON-serializable data only
- Essential for cluster and child process coordination
- Can be used for distributed computing scenarios

## 46) How do you detect and handle memory leaks in Node.js?

Concept: Memory leaks occur when objects are not properly garbage collected, and can be detected using heap snapshots, monitoring tools, and proper coding practices.

Example:
```javascript
// Memory leak example
const leakyArray = [];
setInterval(() => {
  leakyArray.push(new Array(1000).fill('leak'));
  console.log('Memory usage:', process.memoryUsage());
}, 1000);

// Proper cleanup
const cleanup = () => {
  leakyArray.length = 0;
  clearInterval(interval);
};
```

Deep Insight:
- Use process.memoryUsage() to monitor memory
- Take heap snapshots with --inspect flag
- Avoid global variables and closures
- Clear timers and event listeners
- Use weak references for large objects

## 47) What is the Node.js Inspector, and how do you debug with it?

Concept: The Node.js Inspector is a debugging interface that allows you to debug Node.js applications using Chrome DevTools, providing breakpoints, profiling, and memory analysis.

Example:
```javascript
// Start with inspector
// node --inspect app.js
// node --inspect-brk app.js (break on start)

const debugPort = process.debugPort;
console.log(`Debugger listening on port ${debugPort}`);

// Add debugger statements
function processData(data) {
  debugger; // Breakpoint
  return data.map(item => item * 2);
}
```

Deep Insight:
- Start with --inspect or --inspect-brk flags
- Connect Chrome DevTools to debugger
- Set breakpoints and step through code
- Profile CPU and memory usage
- Debug async code and promises

## 48) How do you profile CPU usage and detect performance bottlenecks?

Concept: Use profiling tools like the built-in profiler, Chrome DevTools, and monitoring libraries to identify CPU-intensive operations and optimize performance.

Example:
```javascript
// CPU profiling
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

Deep Insight:
- Use --prof flag for CPU profiling
- Analyze with --prof-process flag
- Use Chrome DevTools for visual profiling
- Monitor event loop lag
- Identify hot spots and optimize algorithms

## 49) What are diagnostic reports, and how can they help in production debugging?

Concept: Diagnostic reports are detailed snapshots of Node.js application state that help debug issues in production by capturing memory, CPU, and system information.

Example:
```javascript
// Generate diagnostic report
process.report.writeReport('error-report.json');

// Or trigger on specific events
process.on('uncaughtException', () => {
  process.report.writeReport();
});

// Configure report options
process.report.reportOnFatalError = true;
process.report.reportOnSignal = true;
```

Deep Insight:
- Capture application state at specific moments
- Include memory usage, CPU usage, and stack traces
- Helpful for debugging production issues
- Can be triggered on errors or signals
- Use for post-mortem analysis

## 50) How do you optimize Node.js applications for low latency and high throughput (event loop tuning, async improvements, caching)?

Concept: Optimize Node.js applications by tuning the event loop, improving async patterns, implementing caching strategies, and monitoring performance metrics.

Example:
```javascript
// Event loop monitoring
const { performance, PerformanceObserver } = require('perf_hooks');

const obs = new PerformanceObserver((list) => {
  const entries = list.getEntries();
  entries.forEach((entry) => {
    console.log(`Event loop lag: ${entry.duration}ms`);
  });
});
obs.observe({ entryTypes: ['measure'] });

// Caching example
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

Deep Insight:
- Monitor event loop lag and CPU usage
- Use clustering for CPU-intensive tasks
- Implement caching for frequently accessed data
- Optimize database queries and connections
- Use streaming for large data processing
