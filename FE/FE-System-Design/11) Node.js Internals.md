# 🟢 Node.js Internals

---

## 📍 Navigation

<div align="center">

[← Previous: Next.js Internals](10%29%20Next.js%20Internals.md) • [Home: Questions Index](question.md) • [Next: React Native Internals →](12%29%20React%20Native%20Internals.md)

[📋 Cheatsheet](FE-System-Design%20Interview%20Cheatsheet.md)

</div>

---

---

## Q19. How Node.js Works Internally

Node.js is a JavaScript runtime built on Chrome's V8 engine. Understanding how Node.js works under the hood helps you write efficient applications, debug performance issues, and make better architectural decisions. When you run Node.js, it uses V8 for JavaScript execution, libuv for async I/O, an event loop for coordination, and handles modules, streams, buffers, and clustering. This knowledge is crucial for senior developers - it helps you understand why certain patterns work better, how to optimize Node.js applications, and how to debug complex issues.

---

## 1. Node.js Architecture

### 🔹 Components

Node.js is built from three main pieces:

* **V8 Engine**: Google's JavaScript engine from Chrome - compiles JavaScript to machine code, handles JavaScript execution, and manages memory

* **libuv**: A C++ library that provides asynchronous I/O - implements the event loop, manages a thread pool for blocking operations, and handles file system, DNS, and network operations

* **Core Modules**: Built-in Node.js modules like fs, http, path, crypto - written in both JavaScript and C++

### 🔹 Architecture Layers

Node.js has a layered architecture:

* **Application Layer**: Your JavaScript code runs here

* **Node.js API**: Core modules like fs, http that you use in your code

* **V8**: Executes your JavaScript code

* **libuv**: Handles the event loop and all I/O operations

### 🔹 Single-Threaded Event Loop

Node.js uses a single-threaded event loop model:

* JavaScript runs on one main thread - this simplifies programming (no race conditions)

* The event loop handles async operations - coordinates when callbacks run

* libuv uses a thread pool for blocking operations - file I/O, crypto, etc. run in separate threads

* I/O operations don't block the main thread - this is what makes Node.js fast

📌 **In simple terms**: Node.js combines V8 (JavaScript engine), libuv (async I/O library), and core modules. JavaScript runs on a single thread with an event loop, but blocking operations use a thread pool. This enables non-blocking, asynchronous operations that keep the main thread free.

---

## 2. Event Loop in Node.js

### 🔹 Event Loop Phases

The Node.js event loop has several phases that run in a specific order. Understanding these phases helps you understand when your callbacks execute.

**1. Timers Phase:**

* Executes callbacks scheduled by `setTimeout` and `setInterval`

* Checks if any timers are ready to fire (their delay has elapsed)

* Only executes timers whose delay has passed

* Example:

```javascript
setTimeout(() => console.log('Timer'), 100);
// This callback runs in the timers phase after 100ms

```

**2. Pending Callbacks Phase:**

* Executes I/O callbacks that were deferred to the next loop iteration

* Handles system operation callbacks (like TCP errors)

* Usually executes very few callbacks

* Most I/O callbacks are handled in the poll phase

**3. Idle, Prepare Phase:**

* Internal use only - not something you interact with in application code

* Used internally by libuv for preparation

**4. Poll Phase:**

* Fetches new I/O events and executes I/O-related callbacks

* This is where most of your async work happens (file I/O, network I/O)

* Can block if there are no callbacks to execute (waits for I/O events)

* If poll queue is empty:
  * If there are `setImmediate` callbacks, move to check phase
  * If there are timers ready, move to timers phase
  * Otherwise, wait for I/O events

* Example:

```javascript
fs.readFile('file.txt', (err, data) => {
  // This callback runs in the poll phase
});

```

**5. Check Phase:**

* Executes `setImmediate` callbacks

* Runs after the poll phase completes

* Example:

```javascript
setImmediate(() => {
  console.log('setImmediate callback');
});

```

**6. Close Callbacks Phase:**

* Executes close callbacks like `socket.on('close')`

* Handles cleanup operations

* Example:

```javascript
socket.on('close', () => {
  // This callback runs in the close callbacks phase
});

```

**Event Loop Flow:**

```

1. Timers Phase

2. Pending Callbacks Phase

3. Idle, Prepare Phase

4. Poll Phase (can block here)

5. Check Phase

6. Close Callbacks Phase
→ Repeat

```

### 🔹 Priority Order

Callbacks execute in a specific priority order. Understanding this helps you predict execution order and debug timing issues.

**Priority Order (Highest to Lowest):**

**1. process.nextTick (Highest Priority):**

* Runs before any event loop phase

* Executes immediately after the current operation completes

* Can starve the event loop if used excessively

* Example:

```javascript
process.nextTick(() => {
  console.log('nextTick'); // Runs before any event loop phase
});

```

**2. Microtasks:**

* Promises and `queueMicrotask` callbacks

* Run after process.nextTick but before event loop phases

* All microtasks are processed before moving to next phase

* Example:

```javascript
Promise.resolve().then(() => {
  console.log('Promise'); // Runs after nextTick, before event loop
});

```

**3. Event Loop Phases:**

* Timers, I/O (poll), check, close phases

* Run in order: timers → pending → poll → check → close

* Each phase processes all callbacks in its queue before moving to next

**4. setImmediate:**

* Runs in the check phase (after poll phase)

* Lower priority than timers in some cases

* Example:

```javascript
setImmediate(() => {
  console.log('setImmediate'); // Runs in check phase
});

```

**Detailed Example:**

```javascript
console.log('1'); // Synchronous - runs first

setTimeout(() => console.log('2'), 0); // Timer phase
setImmediate(() => console.log('3')); // Check phase
process.nextTick(() => console.log('4')); // nextTick (highest priority)
Promise.resolve().then(() => console.log('5')); // Microtask

console.log('6'); // Synchronous - runs second

// Output: 1, 6, 4, 5, 2, 3

```

**Why This Order?**

1. Synchronous code (1, 6) runs first (immediate execution)

2. process.nextTick (4) runs next (highest priority, before event loop)

3. Microtasks (5) run next (promises, after nextTick)

4. Event loop phases start: Timers (2) runs

5. Check phase (3) runs after poll phase

**Important Notes:**

* `process.nextTick` has highest priority - can block event loop if overused

* Microtasks run before event loop phases

* `setTimeout(fn, 0)` and `setImmediate` can have different order depending on context

* In I/O callbacks, `setImmediate` runs before `setTimeout`

📌 **In simple terms**: The event loop has phases that execute different types of callbacks in order. Priority is: nextTick (highest) > microtasks > event loop phases. The poll phase is where most I/O callbacks run, and it can block if there's nothing to do.

---

## 3. V8 Engine

### 🔹 V8 Components

V8 has several components that work together:

* **Parser**: Reads your JavaScript code and converts it to an Abstract Syntax Tree (AST) - also checks for syntax errors

* **Ignition (Interpreter)**: Executes bytecode immediately - fast startup, and it generates profiling data about which code runs frequently

* **TurboFan (Compiler)**: Takes frequently executed code (hot code) and optimizes it to machine code - uses the profiling data from Ignition to know what to optimize

* **Orinoco (Garbage Collector)**: Manages memory automatically - uses generational garbage collection to minimize pauses

### 🔹 V8 Optimization

V8 optimizes your code in several ways:

* **Inline Caching**: Caches property access patterns - assumes object shapes don't change, which makes property access very fast

* **Hidden Classes**: Objects with the same structure share a hidden class - this optimizes property access, but the catch is you should avoid changing object structure after creation

* **Compilation Pipeline**: Ignition interprets bytecode and profiles which code runs frequently, identifies hot code, TurboFan optimizes and compiles it, and if assumptions are wrong, it deoptimizes back to interpreted code

**Example:**

```javascript
// ✅ Good: Consistent object structure
function createUser(name, age) {
  return { name, age }; // Same structure every time
}

// ❌ Bad: Changing structure
const obj = {};
obj.name = 'John';  // Hidden class 1
obj.age = 30;       // Hidden class 2 (changed!)

```

📌 **In simple terms**: V8 uses Ignition (interpreter) for fast startup and TurboFan (compiler) for optimizing hot code. It uses inline caching and hidden classes to optimize property access. Write code with consistent object structures for better performance - avoid adding properties after object creation.

---

## 4. libuv & Asynchronous I/O

### 🔹 What is libuv?

libuv is a C++ library that provides Node.js with asynchronous I/O capabilities:

* It's cross-platform (works on Windows, Linux, macOS), implements the event loop, manages a thread pool, and handles file system, DNS, and network operations

* **Features**: Non-blocking I/O (operations don't block the event loop), thread pool (handles blocking operations in separate threads), event loop (coordinates async operations), cross-platform (same code works everywhere)

### 🔹 Thread Pool

libuv uses a thread pool for blocking operations. This is crucial for understanding Node.js performance.

**Default Size:**

* 4 threads by default

* You can change this with the `UV_THREADPOOL_SIZE` environment variable

* Example: `UV_THREADPOOL_SIZE=8 node app.js` (use 8 threads)

* More threads = more concurrent blocking operations, but more memory usage

**Operations Using Thread Pool:**

* **File system operations** (fs module): `fs.readFile`, `fs.writeFile`, `fs.stat`, etc.

* **DNS lookups** (`dns.lookup`): Synchronous DNS resolution

* **Crypto operations**: `crypto.pbkdf2`, `crypto.randomBytes`, `crypto.scrypt`

* **Zlib compression**: `zlib.gzip`, `zlib.deflate`

* These are blocking operations that would freeze the main thread if run synchronously

**Operations NOT Using Thread Pool:**

* **Network I/O**: Handled by the OS (epoll on Linux, kqueue on macOS, IOCP on Windows)

* **setTimeout/setInterval**: Handled by the event loop (timers phase)

* **Most async operations**: Already non-blocking at the OS level

* **dns.resolve**: Uses OS async DNS resolution (not thread pool)

**Why Thread Pool Matters:**

* If you have 4 file operations and thread pool size is 4, these operations run in parallel

* If you have 5 file operations and thread pool size is 4, the 5th waits

* Increasing thread pool size can improve performance for I/O-bound operations

* But too many threads can hurt performance (context switching overhead)

**Example:**

```javascript
const fs = require('fs');

// These 4 operations run in parallel (thread pool size = 4)
fs.readFile('file1.txt', () => {});
fs.readFile('file2.txt', () => {});
fs.readFile('file3.txt', () => {});
fs.readFile('file4.txt', () => {});

// This 5th operation waits for a thread to become available
fs.readFile('file5.txt', () => {});

```

**Performance Implications:**

* Thread pool size affects concurrent blocking operations

* For I/O-heavy apps, consider increasing `UV_THREADPOOL_SIZE`

* Network I/O doesn't use thread pool (handled by OS)

* CPU-intensive operations should use worker threads or child processes

### 🔹 Asynchronous I/O Flow

Here's what happens when you do async I/O:

1. You call an operation like `fs.readFile`

2. libuv queues the operation to the thread pool

3. A thread performs the operation (this is blocking, but it's in a separate thread)

4. When complete, the callback gets queued to the event loop

5. The event loop executes the callback in the poll phase

**Example:**

```javascript
const fs = require('fs');

fs.readFile('file.txt', (err, data) => {
  // This callback runs in the poll phase
  // The file reading happened in a thread pool thread
});

```

📌 **In simple terms**: libuv provides async I/O for Node.js. It uses a thread pool (4 threads by default) for blocking operations like file system, DNS, and crypto. Network I/O is handled by the OS and doesn't use the thread pool. This keeps the main thread free for JavaScript execution.

---

## 5. Modules & require()

### 🔹 CommonJS Modules

Node.js uses CommonJS for modules:

* **Exporting**: Use `module.exports` or `exports` to export - modules load synchronously

* **Importing**: Use `require()` to import modules - this is synchronous, so it blocks until the module is loaded

### 🔹 Module Loading Process

When you `require()` a module, Node.js does this:

1. **Resolve**: Finds the module file (checks core modules, local files, node_modules)

2. **Load**: Reads and parses the file

3. **Wrap**: Wraps the code in a function that provides `exports`, `require`, `module`, `__filename`, `__dirname`

4. **Evaluate**: Executes the wrapped code

5. **Cache**: Stores the module in the cache so subsequent `require()` calls return the cached version

**Example:**

```javascript
// module.js
module.exports = {
  name: 'Module',
  greet: function() {
    console.log('Hello');
  }
};

// app.js
const module = require('./module'); // Loads, wraps, executes, caches
module.greet(); // "Hello"

```

### 🔹 Module Cache

Modules are cached after the first load:

* Subsequent `require()` calls return the cached version - the module code doesn't execute again

* This prevents re-execution and allows modules to share state

* The catch is if you modify `module.exports` after the first require, other files won't see the changes

### 🔹 Module Resolution

Node.js resolves modules in this order:

* **Core Modules**: `require('fs')` - built-in Node.js modules

* **Local Modules**: `require('./module')` (relative), `require('../module')` (relative), `require('/absolute/path')` (absolute)

* **node_modules**: `require('lodash')` - searches node_modules, walking up the directory tree until it finds it

📌 **In simple terms**: CommonJS uses `module.exports` to export and `require()` to import. Module loading: resolve (find file), load (read file), wrap (wrap in function), evaluate (execute), cache (store). Modules are cached after first load. Resolution order: core modules → local files → node_modules (walks up directory tree).

---

## 6. Streams

### 🔹 Stream Types

Streams handle data in chunks instead of loading everything into memory:

* **Readable**: You can read data from it - examples: reading a file, HTTP request - emits 'data', 'end', 'error' events

* **Writable**: You can write data to it - examples: writing to a file, HTTP response - has write() and end() methods

* **Duplex**: Both readable and writable - examples: TCP socket - you can read and write

* **Transform**: A duplex stream that transforms data as it flows - examples: gzip compression, encryption - data comes in, gets transformed, goes out

**Example:**

```javascript
const fs = require('fs');

// Readable stream
const readable = fs.createReadStream('input.txt');
readable.on('data', (chunk) => {
  console.log(chunk);
});

// Writable stream
const writable = fs.createWriteStream('output.txt');
writable.write('Hello');
writable.end('World');

```

### 🔹 Stream Benefits

Streams are useful because:

* **Memory efficient**: Process data in chunks instead of loading everything into memory at once - great for large files

* **Time efficient**: Start processing data before all of it arrives - don't have to wait for the entire file

* **Composable**: You can pipe streams together to create data pipelines

* **Backpressure**: Automatically handles slow consumers - if the writable stream is slow, the readable stream pauses

### 🔹 Piping Streams

You can pipe streams together to create data pipelines:

* Use `.pipe()` to connect a readable stream to a writable stream

* You can chain multiple streams together

* Backpressure is handled automatically - if the destination is slow, the source pauses

**Example:**

```javascript
const fs = require('fs');
const zlib = require('zlib');

// Pipe readable → transform → writable
fs.createReadStream('file.txt')
  .pipe(zlib.createGzip())        // Transform: compress
  .pipe(fs.createWriteStream('file.txt.gz')); // Write compressed file

```

📌 **In simple terms**: Streams handle data in chunks instead of loading everything into memory. Readable streams allow you to read data, writable streams allow you to write data, duplex streams do both, and transform streams modify data as it flows. Streams are memory efficient, composable with pipe(), and handle backpressure automatically. Perfect for large files and real-time data.

---

## 7. Buffer & Binary Data

### 🔹 What is a Buffer?

Buffers are Node.js's way of handling binary data:

* Buffers are fixed-size chunks of memory for handling binary data

* Array-like structure - you can access bytes like an array

* Efficient for I/O operations - file reading, network operations, crypto

### 🔹 Creating Buffers

You can create buffers in several ways:

* **From string**: `Buffer.from('Hello')` - converts string to bytes

* **From array**: `Buffer.from([1, 2, 3])` - creates buffer from byte array

* **Allocate empty**: `Buffer.alloc(10)` - creates a buffer initialized to zero (safe, but slower)

* **Allocate unsafe**: `Buffer.allocUnsafe(10)` - faster but may contain old data (only use if you'll overwrite all data)

**Example:**

```javascript
// From string
const buf1 = Buffer.from('Hello');

// From array
const buf2 = Buffer.from([72, 101, 108, 108, 111]);

// Allocate empty (safe)
const buf3 = Buffer.alloc(10); // All zeros

// Allocate unsafe (faster)
const buf4 = Buffer.allocUnsafe(10); // May contain old data

```

### 🔹 Buffer Operations

You can work with buffers like arrays:

* **Read**: `buf[0]` gets a byte, `buf.toString()` converts to string

* **Write**: `buf[0] = 74` sets a byte

* **Slice**: `buf.slice(0, 2)` creates a view (shares memory, doesn't copy)

**Example:**

```javascript
const buf = Buffer.from('Hello');
console.log(buf[0]);        // 72 (H)
console.log(buf.toString()); // "Hello"

buf[0] = 74; // 'J'
console.log(buf.toString()); // "Jello"

```

### 🔹 Buffer vs String

* **Buffer**: Handles binary data (bytes) - used for file I/O, network, crypto

* **String**: Handles text data (characters) - JavaScript strings are UTF-16

* **Conversion**: Convert between Buffer and String with encoding (UTF-8, ASCII, etc.)

**Example:**

```javascript
// String to Buffer
const buf = Buffer.from('Hello', 'utf8');

// Buffer to String
const str = buf.toString('utf8');

```

📌 **In simple terms**: Buffers handle binary data in Node.js - these are fixed-size chunks of memory with an array-like interface. Create with Buffer.from() or Buffer.alloc(). Convert to/from strings with encoding (usually UTF-8). Use buffers for file I/O, network operations, and crypto.

---

## 8. Cluster & Child Processes

### 🔹 Cluster Module

The cluster module allows you to utilize multiple CPU cores:

* **Purpose**: Create multiple worker processes (one per CPU core), share the same server port, load balance requests, and manage processes

* **Basic Usage**: The master process creates workers, workers share the same server port, and the master manages workers (restarts workers if workers crash)

**Example:**

```javascript
const cluster = require('cluster');
const os = require('os');

if (cluster.isMaster) {
  // Master process - create workers
  const numCPUs = os.cpus().length;
  for (let i = 0; i < numCPUs; i++) {
    cluster.fork(); // Create worker
  }

  cluster.on('exit', (worker) => {
    console.log('Worker died, restarting...');
    cluster.fork(); // Restart worker
  });
} else {
  // Worker process - runs your server
  const http = require('http');
  http.createServer((req, res) => {
    res.writeHead(200);
    res.end('Hello from worker');
  }).listen(8000);
}

```

### 🔹 Child Processes

Child processes run separate processes:

* **spawn()**: Spawns a new process and streams data - good for long-running processes where you want to stream output

* **exec()**: Executes a command and buffers the output - good for short commands where you want all output at once

* **fork()**: Special spawn for Node.js processes - enables IPC (Inter-Process Communication) so processes can send messages to each other

**Example:**

```javascript
const { spawn, exec, fork } = require('child_process');

// spawn - stream output
const ls = spawn('ls', ['-la']);
ls.stdout.on('data', (data) => {
  console.log(data.toString());
});

// exec - buffer output
exec('ls -la', (error, stdout, stderr) => {
  console.log(stdout);
});

// fork - Node.js process with IPC
const child = fork('child.js');
child.on('message', (msg) => {
  console.log('Message from child:', msg);
});

```

### 🔹 When to Use

* **Cluster**: Use for web servers to utilize multiple CPU cores, load balance requests across workers, and provide high availability (workers restart if workers crash)

* **Child Processes**: Use for CPU-intensive tasks (run in separate process so these tasks don't block main thread), system commands (execute shell commands), and long-running tasks (isolate from main process)

📌 **In simple terms**: The cluster module creates multiple worker processes (one per CPU core) that share the same server port - the master process manages them. Child processes (spawn, exec, fork) run completely separate processes. Use cluster for web servers to utilize multiple cores, use child processes for CPU-intensive tasks or system commands.

---

## ⭐ Summary — 10-second Interview Version

> "Node.js combines V8 (JavaScript engine), libuv (async I/O library), and core modules. JavaScript runs on a single thread with an event loop, but blocking operations use a thread pool. The event loop has phases: timers, pending callbacks, poll, check, close. Priority: nextTick > microtasks > event loop phases. V8 uses JIT compilation to optimize hot code. libuv provides async I/O with a thread pool for blocking operations. CommonJS modules use require() and module.exports, and are cached after first load. Streams handle data in chunks for efficiency. Buffers handle binary data. Cluster and child processes allow utilizing multiple CPU cores."

---

---

## 📍 Navigation

<div align="center">

[06) React Internals.md](06%29%20React%20Internals.md) • [Questions Index](question.md) • [08) React Native Internals.md →](08%29%20React%20Native%20Internals.md)

[FE-System-Design Cheatsheet](FE-System-Design%20Interview%20Cheatsheet.md]

</div>

---
