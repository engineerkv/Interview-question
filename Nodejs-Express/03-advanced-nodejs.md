# ⚙️ Node.js + Express.js Interview Notes (2025 Edition)

## 🔵 Section 3 — Advanced Node.js Concepts — Q61-Q100

---

### 61. 🔵 What is blocking vs non-blocking code?

**🧠 Concept**

Blocking code stops execution until an operation completes, while non-blocking code allows other operations to run while waiting for I/O operations.

**💻 Example**

```javascript
// Blocking code
const fs = require('fs');
const data = fs.readFileSync('file.txt'); // Blocks until file is read
console.log(data);

// Non-blocking code
fs.readFile('file.txt', (err, data) => {
  console.log(data); // Executes when file is read
});
console.log('This runs immediately');
```

**💬 Explanation + Insight**

- **Blocking** - Stops execution until operation completes
- **Non-blocking** - Allows other operations to run
- **Performance** - Non-blocking is better for I/O operations
- **Event Loop** - Non-blocking uses event loop for concurrency
- **Use Cases** - Use non-blocking for I/O, blocking for CPU tasks

---

### 62. 🔵 Callbacks vs Promises vs async/await — pros and cons.

**🧠 Concept**

Callbacks are the original async pattern, Promises provide better error handling, and async/await makes async code look synchronous.

**💻 Example**

```javascript
// Callbacks
fs.readFile('file.txt', (err, data) => {
  if (err) throw err;
  console.log(data);
});

// Promises
fs.promises.readFile('file.txt')
  .then(data => console.log(data))
  .catch(err => console.error(err));

// async/await
async function readFile() {
  try {
    const data = await fs.promises.readFile('file.txt');
    console.log(data);
  } catch (err) {
    console.error(err);
  }
}
```

**💬 Explanation + Insight**

- **Callbacks** - Original pattern, can lead to callback hell
- **Promises** - Better error handling, chainable
- **async/await** - Cleaner syntax, easier to read
- **Error Handling** - async/await has better error handling
- **Performance** - All have similar performance characteristics

---

### 63. 🔵 How to handle uncaught exceptions safely.

**🧠 Concept**

Uncaught exceptions are handled using process event listeners to prevent application crashes and provide graceful error handling.

**💻 Example**

```javascript
// Handle uncaught exceptions
process.on('uncaughtException', (err) => {
  console.error('Uncaught Exception:', err);
  // Log error and exit gracefully
  process.exit(1);
});

// Handle unhandled promise rejections
process.on('unhandledRejection', (reason, promise) => {
  console.error('Unhandled Rejection:', reason);
  // Log error and exit gracefully
  process.exit(1);
});
```

**💬 Explanation + Insight**

- **uncaughtException** - Handle synchronous errors
- **unhandledRejection** - Handle promise rejections
- **Graceful Shutdown** - Exit gracefully after logging
- **Logging** - Log errors for debugging
- **Prevention** - Prevent application crashes

---

### 64. 🔵 Difference between uncaughtException and unhandledRejection.

**🧠 Concept**

uncaughtException handles synchronous errors, while unhandledRejection handles promise rejections that aren't caught.

**💻 Example**

```javascript
// uncaughtException - synchronous errors
process.on('uncaughtException', (err) => {
  console.error('Sync error:', err);
});

// unhandledRejection - promise rejections
process.on('unhandledRejection', (reason, promise) => {
  console.error('Promise rejection:', reason);
});

// Example of uncaughtException
throw new Error('Sync error');

// Example of unhandledRejection
Promise.reject('Promise error');
```

**💬 Explanation + Insight**

- **uncaughtException** - Synchronous errors not caught by try/catch
- **unhandledRejection** - Promise rejections not caught by .catch()
- **Error Types** - Different types of errors
- **Handling** - Both need proper error handling
- **Prevention** - Use try/catch and .catch() to prevent these

---

### 65. 🔵 What are process signals like SIGINT and SIGTERM?

**🧠 Concept**

Process signals are software interrupts sent to processes, with SIGINT (Ctrl+C) and SIGTERM being common termination signals.

**💻 Example**

```javascript
// Handle SIGINT (Ctrl+C)
process.on('SIGINT', () => {
  console.log('Received SIGINT, shutting down gracefully');
  process.exit(0);
});

// Handle SIGTERM
process.on('SIGTERM', () => {
  console.log('Received SIGTERM, shutting down gracefully');
  process.exit(0);
});

// Handle SIGHUP (hangup)
process.on('SIGHUP', () => {
  console.log('Received SIGHUP, reloading configuration');
});
```

**💬 Explanation + Insight**

- **SIGINT** - Interrupt signal (Ctrl+C)
- **SIGTERM** - Termination signal
- **SIGHUP** - Hangup signal (reload configuration)
- **Graceful Shutdown** - Handle signals for graceful shutdown
- **Process Management** - Used by process managers like PM2

---

### 66. 🔵 How to implement graceful shutdown.

**🧠 Concept**

Graceful shutdown involves handling process signals, closing connections, and cleaning up resources before exiting.

**💻 Example**

```javascript
const server = require('http').createServer();

// Graceful shutdown
function gracefulShutdown(signal) {
  console.log(`Received ${signal}, shutting down gracefully`);
  
  server.close(() => {
    console.log('HTTP server closed');
    process.exit(0);
  });
  
  // Force close after timeout
  setTimeout(() => {
    console.log('Force closing server');
    process.exit(1);
  }, 10000);
}

process.on('SIGTERM', () => gracefulShutdown('SIGTERM'));
process.on('SIGINT', () => gracefulShutdown('SIGINT'));
```

**💬 Explanation + Insight**

- **Signal Handling** - Handle SIGTERM and SIGINT signals
- **Resource Cleanup** - Close connections and clean up resources
- **Timeout** - Force close after timeout
- **Process Management** - Work with process managers
- **Zero Downtime** - Enable zero-downtime deployments

---

### 67. 🔵 What is the EventEmitter class?

**🧠 Concept**

EventEmitter is a Node.js class that provides event-driven programming capabilities, allowing objects to emit and listen for events.

**💻 Example**

```javascript
const EventEmitter = require('events');

class MyEmitter extends EventEmitter {}
const myEmitter = new MyEmitter();

// Listen for events
myEmitter.on('event', (data) => {
  console.log('Event received:', data);
});

// Emit events
myEmitter.emit('event', 'Hello World');
```

**💬 Explanation + Insight**

- **Event-driven** - Enables event-driven programming
- **on()** - Listen for events
- **emit()** - Emit events with data
- **Inheritance** - Can be extended by other classes
- **Built-in** - Many Node.js modules inherit from EventEmitter

---

### 68. 🔵 How do you create custom event emitters?

**🧠 Concept**

Custom event emitters are created by extending the EventEmitter class and implementing custom event logic.

**💻 Example**

```javascript
const EventEmitter = require('events');

class UserService extends EventEmitter {
  constructor() {
    super();
  }
  
  createUser(userData) {
    // Simulate user creation
    const user = { id: 1, ...userData };
    this.emit('userCreated', user);
    return user;
  }
  
  deleteUser(userId) {
    this.emit('userDeleted', userId);
  }
}

const userService = new UserService();
userService.on('userCreated', (user) => {
  console.log('User created:', user);
});
```

**💬 Explanation + Insight**

- **Inheritance** - Extend EventEmitter class
- **Custom Events** - Define custom events for your application
- **Event Logic** - Implement event logic in methods
- **Decoupling** - Decouple event emitters from listeners
- **Reusability** - Create reusable event-driven components

---

### 69. 🔵 Difference between EventEmitter and Pub/Sub patterns.

**🧠 Concept**

EventEmitter is a simple event system, while Pub/Sub is a messaging pattern that decouples publishers from subscribers.

**💻 Example**

```javascript
// EventEmitter
const EventEmitter = require('events');
const emitter = new EventEmitter();

emitter.on('message', (data) => {
  console.log('Received:', data);
});
emitter.emit('message', 'Hello');

// Pub/Sub with Redis
const redis = require('redis');
const publisher = redis.createClient();
const subscriber = redis.createClient();

subscriber.on('message', (channel, message) => {
  console.log('Received:', message);
});
subscriber.subscribe('channel');
publisher.publish('channel', 'Hello');
```

**💬 Explanation + Insight**

- **EventEmitter** - Simple event system within application
- **Pub/Sub** - Messaging pattern for distributed systems
- **Decoupling** - Pub/Sub provides better decoupling
- **Scalability** - Pub/Sub scales better across services
- **Use Cases** - EventEmitter for local events, Pub/Sub for distributed events

---

### 70. 🔵 How is process.env used for config management?

**🧠 Concept**

process.env provides access to environment variables, allowing you to manage configuration across different environments.

**💻 Example**

```javascript
// Access environment variables
const port = process.env.PORT || 3000;
const dbUrl = process.env.DATABASE_URL;
const nodeEnv = process.env.NODE_ENV;

// Configuration object
const config = {
  port: process.env.PORT || 3000,
  database: {
    url: process.env.DATABASE_URL,
    host: process.env.DB_HOST || 'localhost',
    port: process.env.DB_PORT || 5432
  },
  jwt: {
    secret: process.env.JWT_SECRET,
    expiresIn: process.env.JWT_EXPIRES_IN || '1h'
  }
};
```

**💬 Explanation + Insight**

- **Environment Variables** - Access system environment variables
- **Configuration** - Manage different configs for different environments
- **Security** - Keep sensitive data out of code
- **Default Values** - Provide default values for missing variables
- **Validation** - Validate required environment variables

---

### 71. 🔵 Difference between process.argv and process.env.

**🧠 Concept**

process.argv contains command-line arguments, while process.env contains environment variables.

**💻 Example**

```javascript
// process.argv - command line arguments
console.log(process.argv);
// node app.js arg1 arg2
// ['node', 'app.js', 'arg1', 'arg2']

// process.env - environment variables
console.log(process.env.NODE_ENV);
console.log(process.env.PORT);

// Parse command line arguments
const args = process.argv.slice(2);
const command = args[0];
const options = args.slice(1);
```

**💬 Explanation + Insight**

- **process.argv** - Command-line arguments passed to script
- **process.env** - Environment variables from system
- **Parsing** - Parse command-line arguments for CLI tools
- **Configuration** - Use environment variables for configuration
- **Security** - Environment variables are more secure

---

### 72. 🔵 What is the crypto module used for?

**🧠 Concept**

The crypto module provides cryptographic functionality including hashing, encryption, decryption, and secure random number generation.

**💻 Example**

```javascript
const crypto = require('crypto');

// Hash data
const hash = crypto.createHash('sha256');
hash.update('Hello World');
console.log(hash.digest('hex'));

// Generate random bytes
const randomBytes = crypto.randomBytes(16);
console.log(randomBytes.toString('hex'));

// Encrypt data
const cipher = crypto.createCipher('aes192', 'password');
let encrypted = cipher.update('Hello World', 'utf8', 'hex');
encrypted += cipher.final('hex');
```

**💬 Explanation + Insight**

- **Hashing** - Create hash digests of data
- **Encryption** - Encrypt and decrypt data
- **Random Generation** - Generate cryptographically secure random data
- **Security** - Essential for secure applications
- **Performance** - Optimized for cryptographic operations

---

### 73. 🔵 How to hash passwords securely in Node.

**🧠 Concept**

Passwords are hashed securely using bcrypt, which provides salt and cost parameters for secure password storage.

**💻 Example**

```javascript
const bcrypt = require('bcrypt');

// Hash password
const hashPassword = async (password) => {
  const saltRounds = 10;
  return await bcrypt.hash(password, saltRounds);
};

// Verify password
const verifyPassword = async (password, hash) => {
  return await bcrypt.compare(password, hash);
};

// Usage
const password = 'userpassword';
const hashedPassword = await hashPassword(password);
const isValid = await verifyPassword(password, hashedPassword);
```

**💬 Explanation + Insight**

- **bcrypt** - Industry standard for password hashing
- **Salt** - Automatic salt generation for security
- **Cost Factor** - Configurable cost for hashing
- **Security** - Protects against rainbow table attacks
- **Performance** - Configurable performance vs security trade-off

---

### 74. 🔵 Difference between bcrypt and crypto hashing.

**🧠 Concept**

bcrypt is designed for password hashing with salt and cost factors, while crypto provides general-purpose hashing functions.

**💻 Example**

```javascript
const crypto = require('crypto');
const bcrypt = require('bcrypt');

// crypto hashing
const hash = crypto.createHash('sha256');
hash.update('password');
const cryptoHash = hash.digest('hex');

// bcrypt hashing
const bcryptHash = await bcrypt.hash('password', 10);
```

**💬 Explanation + Insight**

- **bcrypt** - Designed for passwords, includes salt and cost
- **crypto** - General-purpose hashing, no salt by default
- **Security** - bcrypt is more secure for passwords
- **Performance** - bcrypt is slower by design
- **Use Cases** - bcrypt for passwords, crypto for general hashing

---

### 75. 🔵 How to implement JWT authentication securely.

**🧠 Concept**

JWT authentication involves creating, signing, and verifying JSON Web Tokens for stateless authentication.

**💻 Example**

```javascript
const jwt = require('jsonwebtoken');

// Generate JWT
const generateToken = (userId) => {
  return jwt.sign({ userId }, process.env.JWT_SECRET, {
    expiresIn: '1h'
  });
};

// Verify JWT
const verifyToken = (token) => {
  return jwt.verify(token, process.env.JWT_SECRET);
};

// Middleware
const authenticateToken = (req, res, next) => {
  const token = req.headers.authorization?.split(' ')[1];
  if (!token) return res.status(401).json({ error: 'No token' });
  
  try {
    const decoded = verifyToken(token);
    req.userId = decoded.userId;
    next();
  } catch (err) {
    res.status(403).json({ error: 'Invalid token' });
  }
};
```

**💬 Explanation + Insight**

- **JWT Creation** - Sign tokens with secret key
- **Token Verification** - Verify tokens on each request
- **Expiration** - Set token expiration times
- **Security** - Use strong secrets and HTTPS
- **Stateless** - No server-side session storage

---

### 76. 🔵 What is rate limiting, and why is it important?

**🧠 Concept**

Rate limiting controls the number of requests a client can make within a time period, preventing abuse and ensuring fair resource usage.

**💻 Example**

```javascript
const rateLimit = require('express-rate-limit');

// Basic rate limiting
const limiter = rateLimit({
  windowMs: 15 * 60 * 1000, // 15 minutes
  max: 100, // limit each IP to 100 requests per windowMs
  message: 'Too many requests from this IP'
});

app.use('/api/', limiter);

// Custom rate limiting
const customLimiter = rateLimit({
  windowMs: 60 * 1000, // 1 minute
  max: 5, // 5 requests per minute
  keyGenerator: (req) => req.ip,
  skip: (req) => req.ip === '127.0.0.1'
});
```

**💬 Explanation + Insight**

- **Abuse Prevention** - Prevent API abuse and DDoS attacks
- **Resource Protection** - Protect server resources
- **Fair Usage** - Ensure fair resource usage
- **Configuration** - Configurable limits and time windows
- **IP-based** - Can be IP-based or user-based

---

### 77. 🔵 How to implement rate limiting in Express (Redis or in-memory).

**🧠 Concept**

Rate limiting can be implemented using in-memory storage for single instances or Redis for distributed applications.

**💻 Example**

```javascript
// In-memory rate limiting
const rateLimit = require('express-rate-limit');

const limiter = rateLimit({
  windowMs: 15 * 60 * 1000,
  max: 100,
  store: new MemoryStore()
});

// Redis rate limiting
const RedisStore = require('rate-limit-redis');
const redis = require('redis');

const redisClient = redis.createClient();
const redisLimiter = rateLimit({
  store: new RedisStore({
    client: redisClient
  }),
  windowMs: 15 * 60 * 1000,
  max: 100
});
```

**💬 Explanation + Insight**

- **In-memory** - Simple for single instances
- **Redis** - Better for distributed applications
- **Persistence** - Redis provides persistence across restarts
- **Scalability** - Redis scales better across multiple servers
- **Configuration** - Different storage options for different needs

---

### 78. 🔵 What are WebSockets, and how do they differ from HTTP?

**🧠 Concept**

WebSockets provide full-duplex communication between client and server, while HTTP is request-response based.

**💻 Example**

```javascript
const WebSocket = require('ws');
const wss = new WebSocket.Server({ port: 8080 });

wss.on('connection', (ws) => {
  console.log('Client connected');
  
  ws.on('message', (message) => {
    console.log('Received:', message);
    ws.send('Echo: ' + message);
  });
  
  ws.on('close', () => {
    console.log('Client disconnected');
  });
});
```

**💬 Explanation + Insight**

- **Full-duplex** - Bidirectional communication
- **Persistent** - Maintains connection between client and server
- **Real-time** - Low latency for real-time applications
- **Protocol** - Different protocol from HTTP
- **Use Cases** - Chat, gaming, real-time updates

---

### 79. 🔵 Difference between WebSockets and Server-Sent Events (SSE).

**🧠 Concept**

WebSockets provide bidirectional communication, while SSE provides unidirectional server-to-client communication.

**💻 Example**

```javascript
// WebSocket - bidirectional
const WebSocket = require('ws');
const ws = new WebSocket('ws://localhost:8080');
ws.send('Hello Server');

// SSE - unidirectional
app.get('/events', (req, res) => {
  res.writeHead(200, {
    'Content-Type': 'text/event-stream',
    'Cache-Control': 'no-cache',
    'Connection': 'keep-alive'
  });
  
  res.write('data: Hello Client\n\n');
});
```

**💬 Explanation + Insight**

- **WebSockets** - Bidirectional, full-duplex communication
- **SSE** - Unidirectional, server-to-client only
- **Protocol** - WebSockets use different protocol, SSE uses HTTP
- **Use Cases** - WebSockets for chat, SSE for notifications
- **Complexity** - SSE is simpler to implement

---

### 80. 🔵 How to build a real-time app using Socket.IO.

**🧠 Concept**

Socket.IO provides real-time bidirectional communication with fallbacks for older browsers and automatic reconnection.

**💻 Example**

```javascript
const express = require('express');
const http = require('http');
const socketIo = require('socket.io');

const app = express();
const server = http.createServer(app);
const io = socketIo(server);

io.on('connection', (socket) => {
  console.log('User connected');
  
  socket.on('chat message', (msg) => {
    io.emit('chat message', msg);
  });
  
  socket.on('disconnect', () => {
    console.log('User disconnected');
  });
});

server.listen(3000);
```

**💬 Explanation + Insight**

- **Real-time** - Bidirectional real-time communication
- **Fallbacks** - Automatic fallbacks for older browsers
- **Reconnection** - Automatic reconnection on connection loss
- **Rooms** - Support for rooms and namespaces
- **Ecosystem** - Rich ecosystem of plugins and middleware

---

### 81. 🔵 How to scale WebSockets across multiple servers.

**🧠 Concept**

WebSocket scaling involves using Redis Pub/Sub or message queues to broadcast messages across multiple server instances.

**💻 Example**

```javascript
const redis = require('redis');
const adapter = require('socket.io-redis');

// Configure Redis adapter
io.adapter(adapter({
  host: 'localhost',
  port: 6379
}));

// Broadcast to all clients
io.emit('message', 'Hello all clients');

// Broadcast to specific room
io.to('room1').emit('message', 'Hello room1');
```

**💬 Explanation + Insight**

- **Redis Pub/Sub** - Use Redis for message broadcasting
- **Adapter** - Socket.IO Redis adapter for scaling
- **Load Balancing** - Use sticky sessions for load balancing
- **Message Queues** - Alternative to Redis for message queuing
- **Performance** - Redis provides high-performance message broadcasting

---

### 82. 🔵 How does Redis Pub/Sub help real-time scaling?

**🧠 Concept**

Redis Pub/Sub enables message broadcasting across multiple server instances, allowing real-time applications to scale horizontally.

**💻 Example**

```javascript
const redis = require('redis');
const publisher = redis.createClient();
const subscriber = redis.createClient();

// Publisher
publisher.publish('channel', 'Hello World');

// Subscriber
subscriber.on('message', (channel, message) => {
  console.log('Received:', message);
});
subscriber.subscribe('channel');
```

**💬 Explanation + Insight**

- **Message Broadcasting** - Broadcast messages to all subscribers
- **Horizontal Scaling** - Scale across multiple server instances
- **Decoupling** - Decouple publishers from subscribers
- **Performance** - High-performance message delivery
- **Reliability** - Redis provides reliable message delivery

---

### 83. 🔵 How to use Redis for caching and session storage.

**🧠 Concept**

Redis is used for caching frequently accessed data and storing session data, providing fast access and persistence.

**💻 Example**

```javascript
const redis = require('redis');
const client = redis.createClient();

// Caching
const cacheData = async (key, data, ttl = 3600) => {
  await client.setex(key, ttl, JSON.stringify(data));
};

const getCachedData = async (key) => {
  const data = await client.get(key);
  return data ? JSON.parse(data) : null;
};

// Session storage
const storeSession = async (sessionId, sessionData) => {
  await client.setex(`session:${sessionId}`, 3600, JSON.stringify(sessionData));
};
```

**💬 Explanation + Insight**

- **Caching** - Store frequently accessed data in Redis
- **Session Storage** - Store session data in Redis
- **Performance** - Fast access to cached data
- **Persistence** - Redis provides data persistence
- **TTL** - Set expiration times for cached data

---

### 84. 🔵 Difference between in-memory and distributed caching.

**🧠 Concept**

In-memory caching stores data in application memory, while distributed caching stores data in external systems like Redis.

**💻 Example**

```javascript
// In-memory caching
const cache = new Map();
const getCachedData = (key) => {
  return cache.get(key);
};

// Distributed caching with Redis
const redis = require('redis');
const client = redis.createClient();
const getCachedData = async (key) => {
  return await client.get(key);
};
```

**💬 Explanation + Insight**

- **In-memory** - Fast but limited to single instance
- **Distributed** - Shared across multiple instances
- **Scalability** - Distributed caching scales better
- **Persistence** - Distributed caching can persist data
- **Use Cases** - In-memory for single instance, distributed for multiple instances

---

### 85. 🔵 How to integrate GraphQL with Express.

**🧠 Concept**

GraphQL integration with Express involves setting up a GraphQL server with resolvers and schema definitions.

**💻 Example**

```javascript
const express = require('express');
const { graphqlHTTP } = require('express-graphql');
const { buildSchema } = require('graphql');

const schema = buildSchema(`
  type Query {
    hello: String
    user(id: ID!): User
  }
  type User {
    id: ID!
    name: String!
  }
`);

const root = {
  hello: () => 'Hello World!',
  user: ({ id }) => ({ id, name: 'John Doe' })
};

app.use('/graphql', graphqlHTTP({
  schema: schema,
  rootValue: root,
  graphiql: true
}));
```

**💬 Explanation + Insight**

- **Schema Definition** - Define GraphQL schema
- **Resolvers** - Implement resolver functions
- **Express Integration** - Use express-graphql middleware
- **GraphiQL** - Interactive GraphQL interface
- **Type Safety** - Strong typing with GraphQL schema

---

### 86. 🔵 What is Apollo Server?

**🧠 Concept**

Apollo Server is a GraphQL server implementation that provides advanced features like caching, subscriptions, and schema federation.

**💻 Example**

```javascript
const { ApolloServer, gql } = require('apollo-server-express');

const typeDefs = gql`
  type Query {
    hello: String
  }
`;

const resolvers = {
  Query: {
    hello: () => 'Hello World!'
  }
};

const server = new ApolloServer({ typeDefs, resolvers });
server.applyMiddleware({ app });
```

**💬 Explanation + Insight**

- **Advanced Features** - Caching, subscriptions, federation
- **Schema Federation** - Combine multiple GraphQL schemas
- **Subscriptions** - Real-time GraphQL subscriptions
- **Caching** - Built-in caching capabilities
- **Ecosystem** - Rich ecosystem of tools and plugins

---

### 87. 🔵 How to stream files using fs.createReadStream().

**🧠 Concept**

File streaming uses fs.createReadStream() to read files in chunks, improving performance for large files.

**💻 Example**

```javascript
const fs = require('fs');
const path = require('path');

app.get('/download/:filename', (req, res) => {
  const filePath = path.join(__dirname, 'uploads', req.params.filename);
  const stream = fs.createReadStream(filePath);
  
  stream.on('error', (err) => {
    res.status(404).send('File not found');
  });
  
  stream.pipe(res);
});
```

**💬 Explanation + Insight**

- **Chunked Reading** - Read files in chunks instead of all at once
- **Memory Efficiency** - Lower memory usage for large files
- **Performance** - Better performance for large file operations
- **Streaming** - Use streams for file operations
- **Error Handling** - Handle file read errors

---

### 88. 🔵 Difference between fs.readFile() and streams.

**🧠 Concept**

fs.readFile() loads entire file into memory, while streams read files in chunks, providing better performance for large files.

**💻 Example**

```javascript
const fs = require('fs');

// fs.readFile() - loads entire file
fs.readFile('large-file.txt', (err, data) => {
  console.log(data.toString());
});

// Streams - read in chunks
const stream = fs.createReadStream('large-file.txt');
stream.on('data', (chunk) => {
  console.log(chunk.toString());
});
```

**💬 Explanation + Insight**

- **Memory Usage** - Streams use less memory
- **Performance** - Streams are better for large files
- **Chunked Processing** - Process data in chunks
- **Backpressure** - Handle backpressure with streams
- **Use Cases** - Use streams for large files, readFile for small files

---

### 89. 🔵 What is backpressure in file streaming?

**🧠 Concept**

Backpressure occurs when data is produced faster than it can be consumed, causing memory issues and performance problems.

**💻 Example**

```javascript
const fs = require('fs');
const stream = fs.createReadStream('large-file.txt');

stream.on('data', (chunk) => {
  // Slow processing
  setTimeout(() => {
    console.log(chunk.toString());
  }, 1000);
});

// Handle backpressure
stream.on('data', (chunk) => {
  if (!stream.paused) {
    stream.pause();
    // Process chunk
    stream.resume();
  }
});
```

**💬 Explanation + Insight**

- **Backpressure** - Producer is faster than consumer
- **Memory Issues** - Can cause memory overflow
- **Pause/Resume** - Use pause() and resume() to handle backpressure
- **Automatic Handling** - Streams handle backpressure automatically
- **Performance** - Prevents memory leaks and improves performance

---

### 90. 🔵 What are worker_threads, and how do they improve performance?

**🧠 Concept**

Worker threads allow CPU-intensive tasks to run in separate threads, preventing blocking of the main event loop.

**💻 Example**

```javascript
const { Worker, isMainThread, parentPort } = require('worker_threads');

if (isMainThread) {
  const worker = new Worker(__filename);
  worker.postMessage({ num: 1000000 });
  worker.on('message', (result) => {
    console.log('Result:', result);
  });
} else {
  parentPort.on('message', ({ num }) => {
    let sum = 0;
    for (let i = 0; i < num; i++) {
      sum += i;
    }
    parentPort.postMessage(sum);
  });
}
```

**💬 Explanation + Insight**

- **CPU-intensive Tasks** - Run CPU-intensive tasks in separate threads
- **Non-blocking** - Don't block the main event loop
- **Performance** - Better performance for CPU-intensive operations
- **Shared Memory** - Can share memory between threads
- **Use Cases** - Image processing, data analysis, calculations

---

### 91. 🔵 Difference between spawn and exec in child_process.

**🧠 Concept**

spawn creates a new process with streaming I/O, while exec creates a new process and buffers the output.

**💻 Example**

```javascript
const { spawn, exec } = require('child_process');

// spawn - streaming I/O
const ls = spawn('ls', ['-la']);
ls.stdout.on('data', (data) => {
  console.log(data.toString());
});

// exec - buffered output
exec('ls -la', (error, stdout, stderr) => {
  if (error) {
    console.error(error);
    return;
  }
  console.log(stdout);
});
```

**💬 Explanation + Insight**

- **spawn** - Streaming I/O, better for large outputs
- **exec** - Buffered output, simpler for small outputs
- **Performance** - spawn is better for large data
- **Memory** - exec buffers all output in memory
- **Use Cases** - spawn for large outputs, exec for small outputs

---

### 92. 🔵 What is clustering, and how does PM2 manage it?

**🧠 Concept**

Clustering creates multiple worker processes to utilize all CPU cores, with PM2 providing process management and monitoring.

**💻 Example**

```javascript
const cluster = require('cluster');
const numCPUs = require('os').cpus().length;

if (cluster.isMaster) {
  for (let i = 0; i < numCPUs; i++) {
    cluster.fork();
  }
} else {
  require('./app.js');
}
```

**💬 Explanation + Insight**

- **Multi-core Utilization** - Use all available CPU cores
- **Process Management** - PM2 manages worker processes
- **Load Balancing** - Distribute load across workers
- **Fault Tolerance** - Restart crashed workers
- **Monitoring** - PM2 provides process monitoring

---

### 93. 🔵 Difference between PM2 and nodemon.

**🧠 Concept**

PM2 is a production process manager with clustering and monitoring, while nodemon is a development tool for auto-restarting applications.

**💻 Example**

```bash
# nodemon - development
nodemon app.js

# PM2 - production
pm2 start app.js
pm2 start app.js -i 4  # 4 instances
pm2 monit  # monitoring
```

**💬 Explanation + Insight**

- **nodemon** - Development tool for auto-restart
- **PM2** - Production process manager
- **Clustering** - PM2 provides clustering capabilities
- **Monitoring** - PM2 provides process monitoring
- **Use Cases** - nodemon for development, PM2 for production

---

### 94. 🔵 How does hot reloading work in Node apps?

**🧠 Concept**

Hot reloading automatically restarts the application when file changes are detected, improving development experience.

**💻 Example**

```javascript
// nodemon configuration
{
  "watch": ["src"],
  "ext": "js,json",
  "ignore": ["node_modules"],
  "exec": "node app.js"
}

// PM2 with watch
pm2 start app.js --watch
```

**💬 Explanation + Insight**

- **File Watching** - Watch for file changes
- **Auto-restart** - Automatically restart on changes
- **Development** - Improves development experience
- **Configuration** - Configurable watch patterns
- **Performance** - Minimal performance impact

---

### 95. 🔵 How is concurrency handled by the event loop?

**🧠 Concept**

The event loop handles concurrency through asynchronous I/O operations and the thread pool, allowing Node.js to handle many concurrent operations.

**💻 Example**

```javascript
// Concurrent operations
const fs = require('fs');

// These run concurrently
fs.readFile('file1.txt', (err, data) => {
  console.log('File 1 read');
});

fs.readFile('file2.txt', (err, data) => {
  console.log('File 2 read');
});

fs.readFile('file3.txt', (err, data) => {
  console.log('File 3 read');
});
```

**💬 Explanation + Insight**

- **Asynchronous I/O** - Non-blocking I/O operations
- **Thread Pool** - libuv provides thread pool for I/O
- **Event Loop** - Single thread handles all operations
- **Concurrency** - Handle many concurrent operations
- **Performance** - Efficient concurrency model

---

### 96. 🔵 What causes memory leaks in Node, and how to fix them?

**🧠 Concept**

Memory leaks are caused by circular references, unclosed resources, and global variables, and can be fixed by proper cleanup and monitoring.

**💻 Example**

```javascript
// Memory leak - circular reference
let obj1 = { name: 'obj1' };
let obj2 = { name: 'obj2' };
obj1.ref = obj2;
obj2.ref = obj1;

// Fix - break circular reference
obj1.ref = null;
obj2.ref = null;

// Memory leak - unclosed resources
const fs = require('fs');
const stream = fs.createReadStream('file.txt');
// stream.close(); // Close stream to prevent leak
```

**💬 Explanation + Insight**

- **Circular References** - Objects referencing each other
- **Unclosed Resources** - Streams, timers, event listeners
- **Global Variables** - Accumulating data in global scope
- **Monitoring** - Use tools to detect memory leaks
- **Cleanup** - Proper cleanup of resources

---

### 97. 🔵 How to profile memory usage in Node (clinic.js, Chrome).

**🧠 Concept**

Memory profiling involves using tools like clinic.js and Chrome DevTools to analyze memory usage and identify memory leaks.

**💻 Example**

```bash
# clinic.js profiling
npm install -g clinic
clinic doctor -- node app.js
clinic flame -- node app.js

# Chrome DevTools
node --inspect app.js
# Open chrome://inspect in Chrome
```

**💬 Explanation + Insight**

- **clinic.js** - Node.js performance profiling tool
- **Chrome DevTools** - Use Chrome DevTools for profiling
- **Memory Analysis** - Analyze memory usage patterns
- **Performance** - Identify performance bottlenecks
- **Debugging** - Debug memory leaks and performance issues

---

### 98. 🔵 What is load testing, and how to perform it?

**🧠 Concept**

Load testing involves testing application performance under various load conditions to identify bottlenecks and performance limits.

**💻 Example**

```javascript
// Using artillery for load testing
const artillery = require('artillery');

const config = {
  target: 'http://localhost:3000',
  phases: [
    { duration: 60, arrivalRate: 10 },
    { duration: 120, arrivalRate: 20 },
    { duration: 60, arrivalRate: 10 }
  ]
};

artillery.run(config);
```

**💬 Explanation + Insight**

- **Performance Testing** - Test application under load
- **Bottleneck Identification** - Identify performance bottlenecks
- **Capacity Planning** - Plan for expected load
- **Tools** - Use tools like artillery, k6, JMeter
- **Metrics** - Monitor response times, throughput, errors

---

### 99. 🔵 How to handle CPU-heavy tasks efficiently.

**🧠 Concept**

CPU-heavy tasks are handled efficiently using worker threads, child processes, and task queues to prevent blocking the main event loop.

**💻 Example**

```javascript
const { Worker } = require('worker_threads');

// Offload CPU-heavy task to worker thread
const processData = (data) => {
  return new Promise((resolve, reject) => {
    const worker = new Worker('./worker.js', {
      workerData: data
    });
    
    worker.on('message', resolve);
    worker.on('error', reject);
  });
};
```

**💬 Explanation + Insight**

- **Worker Threads** - Use worker threads for CPU tasks
- **Child Processes** - Use child processes for isolation
- **Task Queues** - Use task queues for background processing
- **Non-blocking** - Prevent blocking the main event loop
- **Performance** - Better performance for CPU-intensive tasks

---

### 100. 🔵 Best practices for large-scale Node.js app structure.

**🧠 Concept**

Large-scale Node.js applications require proper architecture, modular design, and best practices for maintainability and scalability.

**💻 Example**

```javascript
// Project structure
src/
├── controllers/
├── services/
├── models/
├── middleware/
├── routes/
├── utils/
└── config/

// Dependency injection
class UserService {
  constructor(userRepository) {
    this.userRepository = userRepository;
  }
}
```

**💬 Explanation + Insight**

- **Modular Architecture** - Organize code into modules
- **Separation of Concerns** - Separate business logic from presentation
- **Dependency Injection** - Use dependency injection for testability
- **Configuration Management** - Centralize configuration
- **Error Handling** - Implement comprehensive error handling

---

*This comprehensive advanced Node.js section covers all essential concepts including async programming, events, streams, WebSockets, workers, and performance optimization for building scalable applications.*