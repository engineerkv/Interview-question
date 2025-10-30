# 6) Practical System Design Scenarios (Q51–70)

## 51) Design a URL Shortener (like Bitly).

Concept: A URL shortener takes long URLs and makes them short and easy to share. It needs to be fast, reliable, and handle lots of users.

Example:
```javascript
// Simple URL shortener
const express = require('express');
const redis = require('redis');
const app = express();

const redisClient = redis.createClient();
const chars = '0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz';

// Generate short code (6 characters)
function generateShortCode() {
  let result = '';
  for (let i = 0; i < 6; i++) {
    result += chars[Math.floor(Math.random() * 62)];
  }
  return result;
}

// Store URL and get short code
app.post('/shorten', async (req, res) => {
  const { url } = req.body;
  
  if (!isValidUrl(url)) {
    return res.status(400).json({ error: 'Invalid URL' });
  }
  
  const normalizedUrl = normalizeUrl(url);
  let shortCode = generateShortCode();
  
  // Check if code exists, try again if it does
  let exists = await redisClient.get(shortCode);
  while (exists) {
    shortCode = generateShortCode();
    exists = await redisClient.get(shortCode);
  }
  
  // Store in Redis with 24 hour expiry
  await redisClient.setex(shortCode, 86400, normalizedUrl);
  
  res.json({
    shortUrl: `https://short.ly/${shortCode}`,
    originalUrl: normalizedUrl
  });
});

// Redirect to original URL
app.get('/:shortCode', async (req, res) => {
  const { shortCode } = req.params;
  const originalUrl = await redisClient.get(shortCode);
  
  if (originalUrl) {
    res.redirect(301, originalUrl);
  } else {
    res.status(404).json({ error: 'URL not found' });
  }
});

app.listen(3000);
```

Deep Insight:
- **Architecture**: Simple service with Redis caching for fast lookups
- **Storage**: Redis for short-term storage, can add database for persistence
- **Caching**: Redis with TTL for automatic cleanup
- **Analytics**: Can add click tracking and user metrics
- **Scalability**: Horizontal scaling with load balancer
- **Security**: URL validation and rate limiting
- **Monitoring**: Basic error handling and logging

## 52) Design a Social Media Feed System (like Twitter or Instagram).

Concept: A social media feed system displays personalized content feeds to users with real-time updates, scalability, and efficient content ranking.

Example:
```javascript
// Feed generation service
const generateFeed = async (userId, page = 1, limit = 20) => {
  // Get user's follow list
  const following = await getFollowing(userId);
  
  // Get recent posts from followed users
  const posts = await Post.find({
    userId: { $in: following },
    createdAt: { $gte: new Date(Date.now() - 7 * 24 * 60 * 60 * 1000) }
  })
  .sort({ createdAt: -1 })
  .skip((page - 1) * limit)
  .limit(limit);
  
  // Rank posts by engagement and recency
  const rankedPosts = await rankPosts(posts, userId);
  
  return rankedPosts;
};

// Real-time feed updates
const io = require('socket.io')(server);
io.on('connection', (socket) => {
  socket.on('subscribe', (userId) => {
    socket.join(`user:${userId}`);
  });
});

const notifyNewPost = (post) => {
  const followers = getFollowers(post.userId);
  followers.forEach(followerId => {
    io.to(`user:${followerId}`).emit('new_post', post);
  });
};
```

Deep Insight:
- Use push/pull hybrid model for feed generation
- Implement caching for frequently accessed feeds
- Consider pre-computing feeds for popular users
- Use message queues for real-time updates
- Implement proper ranking algorithms for content relevance

## 53) Design a Real-Time Chat Application (like WhatsApp or Slack).

Concept: A real-time chat application supports instant messaging between users with high availability, message persistence, and real-time delivery.

Example:
```javascript
// Chat service with WebSocket
const io = require('socket.io')(server);
const redis = require('redis');

const redisClient = redis.createClient();
const messageQueue = new Map();

io.on('connection', (socket) => {
  socket.on('join_room', (roomId) => {
    socket.join(roomId);
  });
  
  socket.on('send_message', async (data) => {
    const { roomId, message, userId } = data;
    
    // Store message in database
    const messageDoc = await Message.create({
      roomId,
      userId,
      content: message,
      timestamp: new Date()
    });
    
    // Broadcast to room
    io.to(roomId).emit('new_message', messageDoc);
    
    // Store in Redis for offline users
    await redisClient.lpush(`messages:${roomId}`, JSON.stringify(messageDoc));
  });
  
  socket.on('get_messages', async (roomId) => {
    const messages = await redisClient.lrange(`messages:${roomId}`, 0, 50);
    socket.emit('message_history', messages.map(JSON.parse));
  });
});
```

Deep Insight:
- Use WebSockets for real-time communication
- Implement message persistence and offline support
- Consider message ordering and delivery guarantees
- Use Redis for fast message storage and retrieval
- Implement proper authentication and authorization

## 54) Design a Video Streaming Platform (like YouTube or Netflix).

Concept: A video streaming platform delivers video content to users with high quality, low latency, and global scalability through CDN and adaptive streaming.

Example:
```javascript
// Video streaming service
const express = require('express');
const app = express();

// Video upload and processing
app.post('/upload', upload.single('video'), async (req, res) => {
  const video = req.file;
  
  // Process video into different qualities
  const qualities = ['240p', '480p', '720p', '1080p'];
  const processedVideos = await Promise.all(
    qualities.map(quality => processVideo(video, quality))
  );
  
  // Store video metadata
  const videoDoc = await Video.create({
    title: req.body.title,
    userId: req.user.id,
    qualities: processedVideos,
    thumbnail: await generateThumbnail(video)
  });
  
  res.json({ videoId: videoDoc.id });
});

// Video streaming endpoint
app.get('/stream/:videoId', (req, res) => {
  const { videoId } = req.params;
  const { quality = '720p' } = req.query;
  
  const videoPath = getVideoPath(videoId, quality);
  const stat = fs.statSync(videoPath);
  const fileSize = stat.size;
  const range = req.headers.range;
  
  if (range) {
    const parts = range.replace(/bytes=/, "").split("-");
    const start = parseInt(parts[0], 10);
    const end = parts[1] ? parseInt(parts[1], 10) : fileSize - 1;
    const chunksize = (end - start) + 1;
    const file = fs.createReadStream(videoPath, { start, end });
    
    res.writeHead(206, {
      'Content-Range': `bytes ${start}-${end}/${fileSize}`,
      'Accept-Ranges': 'bytes',
      'Content-Length': chunksize,
      'Content-Type': 'video/mp4'
    });
    
    file.pipe(res);
  } else {
    res.writeHead(200, {
      'Content-Length': fileSize,
      'Content-Type': 'video/mp4'
    });
    fs.createReadStream(videoPath).pipe(res);
  }
});
```

Deep Insight:
- Use adaptive bitrate streaming for different network conditions
- Implement CDN for global content delivery
- Consider video transcoding and multiple quality levels
- Use range requests for video seeking and buffering
- Implement proper caching and content distribution strategies

## 55) Design an E-commerce System (product catalog, cart, checkout).

Concept: An e-commerce system manages products, shopping carts, and checkout processes with inventory management, payment processing, and order fulfillment.

Example:
```javascript
// E-commerce service
const express = require('express');
const app = express();

// Product catalog
app.get('/products', async (req, res) => {
  const { category, page = 1, limit = 20 } = req.query;
  const products = await Product.find(category ? { category } : {})
    .skip((page - 1) * limit)
    .limit(limit);
  res.json(products);
});

// Shopping cart
app.post('/cart/add', async (req, res) => {
  const { productId, quantity, userId } = req.body;
  
  // Check inventory
  const product = await Product.findById(productId);
  if (product.stock < quantity) {
    return res.status(400).json({ error: 'Insufficient stock' });
  }
  
  // Add to cart
  await Cart.findOneAndUpdate(
    { userId },
    { $push: { items: { productId, quantity } } },
    { upsert: true }
  );
  
  res.json({ message: 'Item added to cart' });
});

// Checkout process
app.post('/checkout', async (req, res) => {
  const { userId, paymentInfo } = req.body;
  
  // Get cart items
  const cart = await Cart.findOne({ userId });
  if (!cart.items.length) {
    return res.status(400).json({ error: 'Cart is empty' });
  }
  
  // Process payment
  const payment = await processPayment(paymentInfo, cart.total);
  if (!payment.success) {
    return res.status(400).json({ error: 'Payment failed' });
  }
  
  // Create order
  const order = await Order.create({
    userId,
    items: cart.items,
    total: cart.total,
    paymentId: payment.id,
    status: 'confirmed'
  });
  
  // Update inventory
  await updateInventory(cart.items);
  
  // Clear cart
  await Cart.deleteOne({ userId });
  
  res.json({ orderId: order.id });
});
```

Deep Insight:
- Implement proper inventory management and stock checking
- Use transactions for order processing and inventory updates
- Consider payment processing and fraud detection
- Implement proper error handling and rollback mechanisms
- Use caching for product catalog and search functionality

## 56) Design a Rate Limiter for APIs.

Concept: A rate limiter controls the number of requests a client can make within a specific time window to prevent abuse and ensure fair resource usage.

Example:
```javascript
// Rate limiter implementation
class RateLimiter {
  constructor(maxRequests, windowMs) {
    this.maxRequests = maxRequests;
    this.windowMs = windowMs;
    this.requests = new Map();
  }
  
  isAllowed(clientId) {
    const now = Date.now();
    const clientRequests = this.requests.get(clientId) || [];
    
    // Remove old requests outside the window
    const validRequests = clientRequests.filter(
      timestamp => now - timestamp < this.windowMs
    );
    
    if (validRequests.length >= this.maxRequests) {
      return false;
    }
    
    // Add current request
    validRequests.push(now);
    this.requests.set(clientId, validRequests);
    
    return true;
  }
}

// Express middleware
const rateLimiter = new RateLimiter(100, 60000); // 100 requests per minute

app.use((req, res, next) => {
  const clientId = req.ip || req.headers['x-forwarded-for'];
  
  if (!rateLimiter.isAllowed(clientId)) {
    return res.status(429).json({
      error: 'Too many requests',
      retryAfter: 60
    });
  }
  
  next();
});
```

Deep Insight:
- Implement different rate limiting algorithms (fixed window, sliding window, token bucket)
- Consider distributed rate limiting for microservices
- Use Redis for shared rate limiting state
- Implement different limits for different endpoints and users
- Monitor and alert on rate limiting violations

## 57) Design a Notification System (real-time + scheduled).

Concept: A notification system sends messages to users through multiple channels with reliability, scheduling, and delivery tracking capabilities.

Example:
```javascript
// Notification service
const notificationService = {
  // Send immediate notification
  sendImmediate: async (userId, message, channels = ['email', 'push']) => {
    const notification = await Notification.create({
      userId,
      message,
      channels,
      status: 'pending',
      scheduledFor: new Date()
    });
    
    // Queue for processing
    await messageQueue.publish('notification.send', notification);
  },
  
  // Schedule notification
  schedule: async (userId, message, scheduledFor, channels = ['email']) => {
    const notification = await Notification.create({
      userId,
      message,
      channels,
      status: 'scheduled',
      scheduledFor
    });
    
    // Schedule job
    await jobScheduler.schedule('notification.send', scheduledFor, notification);
  },
  
  // Process notification
  process: async (notification) => {
    const user = await User.findById(notification.userId);
    
    for (const channel of notification.channels) {
      try {
        await this.sendToChannel(user, notification.message, channel);
        await this.updateDeliveryStatus(notification.id, channel, 'delivered');
      } catch (error) {
        await this.updateDeliveryStatus(notification.id, channel, 'failed');
      }
    }
  }
};
```

Deep Insight:
- Implement multiple delivery channels (email, SMS, push, in-app)
- Use message queues for reliable delivery
- Implement retry mechanisms and dead letter queues
- Consider user preferences and opt-out mechanisms
- Monitor delivery rates and user engagement

## 58) Design a Search Autocomplete System (like Google search box).

Concept: A search autocomplete system provides real-time search suggestions as users type, requiring fast response times and relevant results.

Example:
```javascript
// Autocomplete service
const autocompleteService = {
  // Build search index
  buildIndex: async () => {
    const products = await Product.find({});
    const index = new Map();
    
    products.forEach(product => {
      const words = product.name.toLowerCase().split(' ');
      words.forEach(word => {
        if (!index.has(word)) {
          index.set(word, []);
        }
        index.get(word).push({
          id: product.id,
          name: product.name,
          score: 1
        });
      });
    });
    
    return index;
  },
  
  // Search suggestions
  search: async (query, limit = 10) => {
    const words = query.toLowerCase().split(' ');
    const suggestions = new Map();
    
    words.forEach(word => {
      const matches = searchIndex.get(word) || [];
      matches.forEach(match => {
        const key = match.id;
        if (suggestions.has(key)) {
          suggestions.get(key).score += match.score;
        } else {
          suggestions.set(key, match);
        }
      });
    });
    
    return Array.from(suggestions.values())
      .sort((a, b) => b.score - a.score)
      .slice(0, limit);
  }
};

// Express endpoint
app.get('/autocomplete', async (req, res) => {
  const { q } = req.query;
  if (!q || q.length < 2) {
    return res.json([]);
  }
  
  const suggestions = await autocompleteService.search(q);
  res.json(suggestions);
});
```

Deep Insight:
- Use efficient data structures like tries or inverted indexes
- Implement caching for frequently searched terms
- Consider fuzzy matching and typo tolerance
- Use analytics to improve suggestion relevance
- Implement debouncing to reduce server load

## 59) Design an Online Code Execution Platform (like LeetCode or Replit).

Concept: An online code execution platform safely executes user code in isolated environments with proper security, resource limits, and result handling.

Example:
```javascript
// Code execution service
const docker = require('dockerode');
const fs = require('fs').promises;

class CodeExecutor {
  constructor() {
    this.docker = new docker();
  }
  
  async execute(code, language, input = '') {
    const containerName = `exec-${Date.now()}`;
    
    try {
      // Create container with resource limits
      const container = await this.docker.createContainer({
        Image: this.getImage(language),
        name: containerName,
        Cmd: this.getCommand(language),
        WorkingDir: '/app',
        HostConfig: {
          Memory: 128 * 1024 * 1024, // 128MB
          CpuPeriod: 100000,
          CpuQuota: 50000, // 50% CPU
          NetworkMode: 'none' // No network access
        }
      });
      
      // Start container
      await container.start();
      
      // Copy code to container
      await this.copyCode(container, code, language);
      
      // Execute with timeout
      const result = await this.runWithTimeout(container, 5000);
      
      // Clean up
      await container.remove({ force: true });
      
      return result;
    } catch (error) {
      // Clean up on error
      try {
        const container = this.docker.getContainer(containerName);
        await container.remove({ force: true });
      } catch (e) {}
      
      throw error;
    }
  }
  
  getImage(language) {
    const images = {
      'javascript': 'node:alpine',
      'python': 'python:alpine',
      'java': 'openjdk:alpine'
    };
    return images[language] || 'node:alpine';
  }
}
```

Deep Insight:
- Use containerization for security and isolation
- Implement resource limits (CPU, memory, execution time)
- Disable network access and file system writes
- Use sandboxing and proper user permissions
- Implement proper cleanup and error handling

## 60) Design a News Feed Ranking Algorithm (Facebook/LinkedIn feed).

Concept: A news feed ranking algorithm determines the order of content in user feeds based on relevance, engagement, and user preferences.

Example:
```javascript
// News feed ranking algorithm
class FeedRanker {
  constructor() {
    this.weights = {
      recency: 0.3,
      engagement: 0.4,
      relevance: 0.3
    };
  }
  
  async rankPosts(posts, userId) {
    const user = await User.findById(userId);
    const userInterests = await this.getUserInterests(userId);
    
    const rankedPosts = posts.map(post => {
      const score = this.calculateScore(post, user, userInterests);
      return { ...post, score };
    });
    
    return rankedPosts.sort((a, b) => b.score - a.score);
  }
  
  calculateScore(post, user, userInterests) {
    const recencyScore = this.getRecencyScore(post.createdAt);
    const engagementScore = this.getEngagementScore(post);
    const relevanceScore = this.getRelevanceScore(post, userInterests);
    
    return (
      recencyScore * this.weights.recency +
      engagementScore * this.weights.engagement +
      relevanceScore * this.weights.relevance
    );
  }
  
  getRecencyScore(createdAt) {
    const hoursAgo = (Date.now() - createdAt.getTime()) / (1000 * 60 * 60);
    return Math.exp(-hoursAgo / 24); // Exponential decay
  }
  
  getEngagementScore(post) {
    const likes = post.likes || 0;
    const comments = post.comments || 0;
    const shares = post.shares || 0;
    
    return (likes * 1 + comments * 2 + shares * 3) / 100;
  }
  
  getRelevanceScore(post, userInterests) {
    const postTags = post.tags || [];
    const commonTags = postTags.filter(tag => userInterests.includes(tag));
    return commonTags.length / Math.max(postTags.length, 1);
  }
}
```

Deep Insight:
- Use machine learning for better relevance scoring
- Consider user behavior and interaction history
- Implement A/B testing for algorithm improvements
- Use real-time data for dynamic ranking
- Balance different signals (recency, engagement, relevance)

## 61) Design a File Storage System (like Google Drive / Dropbox).

Concept: A file storage system stores and serves files with high availability, scalability, and proper access control for cloud storage applications.

Example:
```javascript
// File storage service
const multer = require('multer');
const AWS = require('aws-sdk');

const s3 = new AWS.S3();
const upload = multer({ storage: multer.memoryStorage() });

// File upload
app.post('/upload', upload.single('file'), async (req, res) => {
  const { file } = req;
  const { userId, folderId } = req.body;
  
  // Generate unique file key
  const fileKey = `${userId}/${folderId}/${Date.now()}-${file.originalname}`;
  
  // Upload to S3
  const uploadParams = {
    Bucket: 'my-storage-bucket',
    Key: fileKey,
    Body: file.buffer,
    ContentType: file.mimetype,
    Metadata: {
      userId,
      originalName: file.originalname
    }
  };
  
  const result = await s3.upload(uploadParams).promise();
  
  // Store file metadata in database
  const fileDoc = await File.create({
    userId,
    folderId,
    name: file.originalname,
    size: file.size,
    type: file.mimetype,
    s3Key: fileKey,
    s3Url: result.Location
  });
  
  res.json({ fileId: fileDoc.id, url: result.Location });
});

// File download
app.get('/download/:fileId', async (req, res) => {
  const { fileId } = req.params;
  const file = await File.findById(fileId);
  
  if (!file) {
    return res.status(404).json({ error: 'File not found' });
  }
  
  // Generate signed URL for secure download
  const signedUrl = s3.getSignedUrl('getObject', {
    Bucket: 'my-storage-bucket',
    Key: file.s3Key,
    Expires: 3600 // 1 hour
  });
  
  res.redirect(signedUrl);
});
```

Deep Insight:
- Use cloud storage services for scalability and durability
- Implement proper access control and permissions
- Consider file versioning and conflict resolution
- Use CDN for global file delivery
- Implement proper backup and disaster recovery

## 62) Design a Distributed Cache System (like Redis or Memcached).

Concept: A distributed cache system provides fast data access across multiple nodes with consistency, fault tolerance, and scalability.

Example:
```javascript
// Distributed cache implementation
class DistributedCache {
  constructor(nodes) {
    this.nodes = nodes;
    this.consistentHash = new ConsistentHash();
    this.nodes.forEach(node => this.consistentHash.addNode(node));
  }
  
  async get(key) {
    const node = this.consistentHash.getNode(key);
    try {
      return await this.getFromNode(node, key);
    } catch (error) {
      // Try backup nodes
      const backupNodes = this.consistentHash.getBackupNodes(key);
      for (const backupNode of backupNodes) {
        try {
          return await this.getFromNode(backupNode, key);
        } catch (e) {
          continue;
        }
      }
      throw error;
    }
  }
  
  async set(key, value, ttl = 3600) {
    const node = this.consistentHash.getNode(key);
    const backupNodes = this.consistentHash.getBackupNodes(key);
    
    // Write to primary node
    await this.setToNode(node, key, value, ttl);
    
    // Write to backup nodes
    await Promise.all(
      backupNodes.map(backupNode => 
        this.setToNode(backupNode, key, value, ttl)
      )
    );
  }
  
  async getFromNode(node, key) {
    const response = await fetch(`http://${node.host}:${node.port}/get/${key}`);
    if (response.ok) {
      return await response.json();
    }
    throw new Error('Node unavailable');
  }
  
  async setToNode(node, key, value, ttl) {
    const response = await fetch(`http://${node.host}:${node.port}/set`, {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify({ key, value, ttl })
    });
    
    if (!response.ok) {
      throw new Error('Failed to set value');
    }
  }
}
```

Deep Insight:
- Use consistent hashing for data distribution
- Implement replication for fault tolerance
- Consider different eviction policies (LRU, LFU, TTL)
- Use gossip protocols for cluster management
- Monitor cache hit rates and performance metrics

## 63) Design a Logging and Analytics System (like ELK or Splunk).

Concept: A logging and analytics system collects, stores, and analyzes logs from multiple services for monitoring, debugging, and business intelligence.

Example:
```javascript
// Logging service
const winston = require('winston');
const { ElasticsearchTransport } = require('winston-elasticsearch');

const logger = winston.createLogger({
  level: 'info',
  format: winston.format.combine(
    winston.format.timestamp(),
    winston.format.errors({ stack: true }),
    winston.format.json()
  ),
  transports: [
    new winston.transports.Console(),
    new ElasticsearchTransport({
      level: 'info',
      clientOpts: { node: 'http://elasticsearch:9200' },
      index: 'application-logs'
    })
  ]
});

// Log aggregation
const logAggregator = {
  collectLogs: async (serviceName, logs) => {
    const processedLogs = logs.map(log => ({
      ...log,
      service: serviceName,
      timestamp: new Date().toISOString(),
      level: log.level || 'info'
    }));
    
    await logger.info('Logs collected', { logs: processedLogs });
  },
  
  searchLogs: async (query, filters = {}) => {
    const searchQuery = {
      index: 'application-logs',
      body: {
        query: {
          bool: {
            must: [
              { match: { message: query } },
              ...Object.entries(filters).map(([field, value]) => ({
                match: { [field]: value }
              }))
            ]
          }
        },
        sort: [{ timestamp: { order: 'desc' } }],
        size: 100
      }
    };
    
    const response = await elasticsearch.search(searchQuery);
    return response.body.hits.hits.map(hit => hit._source);
  }
};
```

Deep Insight:
- Use structured logging with consistent formats
- Implement log aggregation and search capabilities
- Consider log retention and storage costs
- Use real-time log analysis for monitoring
- Implement proper log rotation and archival

## 64) Design a Metrics Collection System (like Prometheus).

Concept: A metrics collection system gathers and stores metrics from various services for monitoring, alerting, and performance analysis.

Example:
```javascript
// Metrics collection service
class MetricsCollector {
  constructor() {
    this.metrics = new Map();
    this.collectors = [];
  }
  
  // Counter metric
  incrementCounter(name, labels = {}) {
    const key = this.getKey(name, labels);
    const current = this.metrics.get(key) || 0;
    this.metrics.set(key, current + 1);
  }
  
  // Gauge metric
  setGauge(name, value, labels = {}) {
    const key = this.getKey(name, labels);
    this.metrics.set(key, value);
  }
  
  // Histogram metric
  observeHistogram(name, value, labels = {}) {
    const key = this.getKey(name, labels);
    if (!this.metrics.has(key)) {
      this.metrics.set(key, []);
    }
    this.metrics.get(key).push(value);
  }
  
  // Export metrics
  exportMetrics() {
    const result = {};
    for (const [key, value] of this.metrics) {
      const [name, labels] = this.parseKey(key);
      if (!result[name]) {
        result[name] = [];
      }
      result[name].push({ labels, value });
    }
    return result;
  }
  
  getKey(name, labels) {
    const labelString = Object.entries(labels)
      .map(([k, v]) => `${k}="${v}"`)
      .join(',');
    return `${name}{${labelString}}`;
  }
}

// Express middleware for metrics
const metricsCollector = new MetricsCollector();

app.use((req, res, next) => {
  const start = Date.now();
  
  res.on('finish', () => {
    const duration = Date.now() - start;
    metricsCollector.incrementCounter('http_requests_total', {
      method: req.method,
      status: res.statusCode
    });
    metricsCollector.observeHistogram('http_request_duration_ms', duration);
  });
  
  next();
});
```

Deep Insight:
- Use different metric types (counter, gauge, histogram, summary)
- Implement proper labeling and aggregation
- Consider metric cardinality and storage costs
- Use time-series databases for efficient storage
- Implement proper metric naming conventions

## 65) Design a Real-Time Collaborative Document Editor (like Google Docs).

Concept: A collaborative document editor allows multiple users to edit documents simultaneously in real-time with conflict resolution and synchronization.

Example:
```javascript
// Collaborative document editor
const io = require('socket.io')(server);
const redis = require('redis');

const redisClient = redis.createClient();
const documents = new Map();

io.on('connection', (socket) => {
  socket.on('join_document', async (documentId) => {
    socket.join(documentId);
    
    // Send current document state
    const document = await getDocument(documentId);
    socket.emit('document_state', document);
  });
  
  socket.on('edit_operation', async (data) => {
    const { documentId, operation, userId } = data;
    
    // Apply operation to document
    const document = await applyOperation(documentId, operation);
    
    // Broadcast to other users
    socket.to(documentId).emit('remote_operation', {
      operation,
      userId,
      timestamp: Date.now()
    });
    
    // Store in Redis for persistence
    await redisClient.setex(`document:${documentId}`, 3600, JSON.stringify(document));
  });
  
  socket.on('cursor_position', (data) => {
    const { documentId, position, userId } = data;
    socket.to(documentId).emit('cursor_update', { position, userId });
  });
});

// Operational Transform for conflict resolution
class OperationalTransform {
  transform(op1, op2) {
    // Transform operation op1 against op2
    // This is a simplified version
    if (op1.type === 'insert' && op2.type === 'insert') {
      if (op1.position <= op2.position) {
        return { ...op1, position: op1.position };
      } else {
        return { ...op1, position: op1.position + op2.text.length };
      }
    }
    return op1;
  }
}
```

Deep Insight:
- Use operational transforms for conflict resolution
- Implement proper cursor and selection management
- Consider document versioning and history
- Use WebSocket connections for real-time updates
- Implement proper user presence and permissions

## 66) Design a Job Queue System (like Celery, Kafka, SQS).

Concept: A job queue system processes background jobs asynchronously with reliability, scalability, and proper error handling.

Example:
```javascript
// Job queue system
class JobQueue {
  constructor() {
    this.queues = new Map();
    this.workers = new Map();
  }
  
  // Add job to queue
  async addJob(queueName, jobData, options = {}) {
    const job = {
      id: this.generateJobId(),
      data: jobData,
      status: 'pending',
      createdAt: new Date(),
      attempts: 0,
      maxAttempts: options.maxAttempts || 3,
      delay: options.delay || 0
    };
    
    if (job.delay > 0) {
      // Schedule delayed job
      setTimeout(() => {
        this.addToQueue(queueName, job);
      }, job.delay);
    } else {
      await this.addToQueue(queueName, job);
    }
    
    return job.id;
  }
  
  // Process jobs
  async processQueue(queueName, processor) {
    const queue = this.queues.get(queueName) || [];
    
    while (true) {
      const job = queue.shift();
      if (!job) {
        await new Promise(resolve => setTimeout(resolve, 1000));
        continue;
      }
      
      try {
        job.status = 'processing';
        job.attempts++;
        
        await processor(job.data);
        
        job.status = 'completed';
        job.completedAt = new Date();
      } catch (error) {
        job.status = 'failed';
        job.error = error.message;
        
        if (job.attempts < job.maxAttempts) {
          // Retry job
          job.status = 'pending';
          queue.push(job);
        }
      }
    }
  }
  
  async addToQueue(queueName, job) {
    if (!this.queues.has(queueName)) {
      this.queues.set(queueName, []);
    }
    this.queues.get(queueName).push(job);
  }
}
```

Deep Insight:
- Use message queues for reliable job processing
- Implement proper retry mechanisms and dead letter queues
- Consider job prioritization and scheduling
- Use monitoring and alerting for job failures
- Implement proper cleanup and job lifecycle management

## 67) Design a Payment Processing System (like Stripe / PayPal).

Concept: A payment processing system handles financial transactions securely with compliance, fraud detection, and proper error handling.

Example:
```javascript
// Payment processing service
class PaymentProcessor {
  constructor() {
    this.providers = {
      stripe: new StripeProvider(),
      paypal: new PayPalProvider()
    };
  }
  
  async processPayment(paymentData) {
    const { amount, currency, paymentMethod, provider } = paymentData;
    
    // Validate payment data
    await this.validatePayment(paymentData);
    
    // Check fraud
    const fraudScore = await this.checkFraud(paymentData);
    if (fraudScore > 0.8) {
      throw new Error('Payment flagged as potential fraud');
    }
    
    // Process payment
    const provider = this.providers[paymentData.provider];
    const result = await provider.charge({
      amount,
      currency,
      paymentMethod,
      metadata: paymentData.metadata
    });
    
    // Store transaction
    const transaction = await Transaction.create({
      id: result.id,
      amount,
      currency,
      status: result.status,
      provider,
      userId: paymentData.userId
    });
    
    return transaction;
  }
  
  async refundPayment(transactionId, amount) {
    const transaction = await Transaction.findById(transactionId);
    const provider = this.providers[transaction.provider];
    
    const result = await provider.refund({
      transactionId: transaction.id,
      amount
    });
    
    // Update transaction
    transaction.status = 'refunded';
    transaction.refundedAt = new Date();
    await transaction.save();
    
    return result;
  }
  
  async checkFraud(paymentData) {
    // Implement fraud detection logic
    const riskFactors = [];
    
    if (paymentData.amount > 10000) riskFactors.push(0.3);
    if (paymentData.ipCountry !== paymentData.billingCountry) riskFactors.push(0.2);
    if (paymentData.cardType === 'prepaid') riskFactors.push(0.1);
    
    return riskFactors.reduce((sum, factor) => sum + factor, 0);
  }
}
```

Deep Insight:
- Implement proper security and encryption
- Use PCI DSS compliance for card data
- Implement fraud detection and risk assessment
- Consider different payment methods and currencies
- Use proper error handling and transaction logging

## 68) Design a Ride-Sharing Platform (like Uber).

Concept: A ride-sharing platform matches riders with drivers in real-time using location services, pricing algorithms, and efficient matching.

Example:
```javascript
// Ride-sharing platform
class RideSharingPlatform {
  constructor() {
    this.drivers = new Map();
    this.rides = new Map();
    this.riders = new Map();
  }
  
  // Request ride
  async requestRide(riderId, pickup, destination) {
    const ride = {
      id: this.generateRideId(),
      riderId,
      pickup,
      destination,
      status: 'requested',
      requestedAt: new Date()
    };
    
    // Find nearby drivers
    const nearbyDrivers = await this.findNearbyDrivers(pickup);
    
    // Match with best driver
    const driver = await this.matchDriver(ride, nearbyDrivers);
    
    if (driver) {
      ride.driverId = driver.id;
      ride.status = 'matched';
      ride.estimatedArrival = this.calculateETA(pickup, driver.location);
      ride.price = this.calculatePrice(pickup, destination);
      
      // Notify driver
      await this.notifyDriver(driver.id, ride);
    }
    
    this.rides.set(ride.id, ride);
    return ride;
  }
  
  // Find nearby drivers
  async findNearbyDrivers(pickup, radius = 5) {
    const drivers = Array.from(this.drivers.values());
    return drivers.filter(driver => {
      const distance = this.calculateDistance(pickup, driver.location);
      return distance <= radius && driver.status === 'available';
    });
  }
  
  // Match driver with ride
  async matchDriver(ride, drivers) {
    if (drivers.length === 0) return null;
    
    // Score drivers based on distance, rating, and other factors
    const scoredDrivers = drivers.map(driver => ({
      driver,
      score: this.calculateDriverScore(ride, driver)
    }));
    
    // Return best driver
    scoredDrivers.sort((a, b) => b.score - a.score);
    return scoredDrivers[0].driver;
  }
  
  // Calculate price
  calculatePrice(pickup, destination) {
    const distance = this.calculateDistance(pickup, destination);
    const basePrice = 2.0;
    const perMilePrice = 1.5;
    const surgeMultiplier = this.getSurgeMultiplier(pickup);
    
    return (basePrice + distance * perMilePrice) * surgeMultiplier;
  }
}
```

Deep Insight:
- Use real-time location tracking and matching algorithms
- Implement dynamic pricing and surge pricing
- Consider driver availability and demand patterns
- Use efficient data structures for location-based queries
- Implement proper ride tracking and status updates

## 69) Design a Food Delivery System (like Zomato / DoorDash).

Concept: A food delivery system manages orders, delivery tracking, and restaurant partnerships with real-time updates and efficient logistics.

Example:
```javascript
// Food delivery system
class FoodDeliverySystem {
  constructor() {
    this.orders = new Map();
    this.restaurants = new Map();
    this.deliveryPartners = new Map();
  }
  
  // Place order
  async placeOrder(orderData) {
    const { userId, restaurantId, items, deliveryAddress } = orderData;
    
    // Validate restaurant and items
    const restaurant = await this.validateRestaurant(restaurantId);
    const validatedItems = await this.validateItems(restaurantId, items);
    
    // Calculate pricing
    const subtotal = this.calculateSubtotal(validatedItems);
    const deliveryFee = this.calculateDeliveryFee(deliveryAddress);
    const total = subtotal + deliveryFee;
    
    // Create order
    const order = {
      id: this.generateOrderId(),
      userId,
      restaurantId,
      items: validatedItems,
      deliveryAddress,
      subtotal,
      deliveryFee,
      total,
      status: 'placed',
      placedAt: new Date()
    };
    
    // Assign delivery partner
    const deliveryPartner = await this.assignDeliveryPartner(deliveryAddress);
    if (deliveryPartner) {
      order.deliveryPartnerId = deliveryPartner.id;
      order.status = 'assigned';
    }
    
    this.orders.set(order.id, order);
    
    // Notify restaurant
    await this.notifyRestaurant(restaurantId, order);
    
    return order;
  }
  
  // Track order
  async trackOrder(orderId) {
    const order = this.orders.get(orderId);
    if (!order) {
      throw new Error('Order not found');
    }
    
    const tracking = {
      orderId,
      status: order.status,
      estimatedDelivery: order.estimatedDelivery,
      currentLocation: order.currentLocation,
      deliveryPartner: order.deliveryPartnerId ? 
        this.deliveryPartners.get(order.deliveryPartnerId) : null
    };
    
    return tracking;
  }
  
  // Update order status
  async updateOrderStatus(orderId, status, location = null) {
    const order = this.orders.get(orderId);
    if (!order) {
      throw new Error('Order not found');
    }
    
    order.status = status;
    order.updatedAt = new Date();
    
    if (location) {
      order.currentLocation = location;
    }
    
    // Notify user of status change
    await this.notifyUser(order.userId, {
      orderId,
      status,
      message: this.getStatusMessage(status)
    });
  }
}
```

Deep Insight:
- Implement real-time order tracking and status updates
- Use efficient logistics and delivery partner assignment
- Consider restaurant capacity and delivery time estimates
- Implement proper payment processing and refund handling
- Use location services for accurate delivery tracking

## 70) Design a Recommendation Engine (like Netflix or Amazon).

Concept: A recommendation engine provides personalized content suggestions based on user behavior, preferences, and collaborative filtering algorithms.

Example:
```javascript
// Recommendation engine
class RecommendationEngine {
  constructor() {
    this.userInteractions = new Map();
    this.itemFeatures = new Map();
    this.similarityCache = new Map();
  }
  
  // Record user interaction
  async recordInteraction(userId, itemId, interactionType, rating = null) {
    if (!this.userInteractions.has(userId)) {
      this.userInteractions.set(userId, []);
    }
    
    const interaction = {
      itemId,
      type: interactionType, // 'view', 'like', 'purchase', 'rating'
      rating,
      timestamp: new Date()
    };
    
    this.userInteractions.get(userId).push(interaction);
  }
  
  // Get recommendations
  async getRecommendations(userId, limit = 10) {
    const userInteractions = this.userInteractions.get(userId) || [];
    
    if (userInteractions.length === 0) {
      // Cold start - return popular items
      return await this.getPopularItems(limit);
    }
    
    // Collaborative filtering
    const collaborativeRecs = await this.getCollaborativeRecommendations(userId, limit);
    
    // Content-based filtering
    const contentRecs = await this.getContentBasedRecommendations(userId, limit);
    
    // Hybrid approach
    const recommendations = this.combineRecommendations(collaborativeRecs, contentRecs);
    
    return recommendations.slice(0, limit);
  }
  
  // Collaborative filtering
  async getCollaborativeRecommendations(userId, limit) {
    const userInteractions = this.userInteractions.get(userId) || [];
    const userItems = new Set(userInteractions.map(i => i.itemId));
    
    // Find similar users
    const similarUsers = await this.findSimilarUsers(userId);
    
    // Get items liked by similar users
    const recommendations = new Map();
    
    for (const similarUser of similarUsers) {
      const similarUserInteractions = this.userInteractions.get(similarUser.userId) || [];
      
      for (const interaction of similarUserInteractions) {
        if (!userItems.has(interaction.itemId)) {
          const score = recommendations.get(interaction.itemId) || 0;
          recommendations.set(interaction.itemId, score + similarUser.similarity * interaction.rating);
        }
      }
    }
    
    return Array.from(recommendations.entries())
      .sort((a, b) => b[1] - a[1])
      .slice(0, limit)
      .map(([itemId, score]) => ({ itemId, score }));
  }
  
  // Content-based filtering
  async getContentBasedRecommendations(userId, limit) {
    const userInteractions = this.userInteractions.get(userId) || [];
    const userProfile = await this.buildUserProfile(userId);
    
    const recommendations = new Map();
    
    for (const [itemId, features] of this.itemFeatures) {
      const similarity = this.calculateSimilarity(userProfile, features);
      if (similarity > 0.5) {
        recommendations.set(itemId, similarity);
      }
    }
    
    return Array.from(recommendations.entries())
      .sort((a, b) => b[1] - a[1])
      .slice(0, limit)
      .map(([itemId, score]) => ({ itemId, score }));
  }
}
```

Deep Insight:
- Use collaborative filtering for user-based recommendations
- Implement content-based filtering for item similarity
- Consider hybrid approaches for better accuracy
- Use machine learning for feature extraction and ranking
- Implement proper evaluation metrics and A/B testing
