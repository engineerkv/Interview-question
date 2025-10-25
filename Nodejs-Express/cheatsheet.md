# 🚀 Node.js + Express.js Cheatsheet (2025 Edition)

## 📋 Quick Reference Guide

### 🔧 Node.js Fundamentals
```javascript
// Event Loop
process.nextTick(() => console.log('nextTick'));
setImmediate(() => console.log('immediate'));

// Streams
const fs = require('fs');
const stream = fs.createReadStream('file.txt');
stream.pipe(process.stdout);

// Clustering
const cluster = require('cluster');
if (cluster.isMaster) {
  for (let i = 0; i < require('os').cpus().length; i++) {
    cluster.fork();
  }
}
```

### ⚙️ Express.js Core
```javascript
const express = require('express');
const app = express();

// Middleware
app.use(express.json());
app.use(express.static('public'));

// Routes
app.get('/api/users', (req, res) => {
  res.json({ users: [] });
});

// Error handling
app.use((err, req, res, next) => {
  res.status(500).json({ error: err.message });
});
```

### 🔐 Security Essentials
```javascript
const helmet = require('helmet');
const rateLimit = require('express-rate-limit');

// Security headers
app.use(helmet());

// Rate limiting
const limiter = rateLimit({
  windowMs: 15 * 60 * 1000,
  max: 100
});
app.use('/api/', limiter);
```

### 🚀 Performance & Scaling
```javascript
// Caching with Redis
const redis = require('redis');
const client = redis.createClient();

const cache = (duration) => (req, res, next) => {
  const key = req.originalUrl;
  client.get(key, (err, data) => {
    if (data) {
      res.json(JSON.parse(data));
    } else {
      res.sendResponse = res.json;
      res.json = (body) => {
        client.setex(key, duration, JSON.stringify(body));
        res.sendResponse(body);
      };
      next();
    }
  });
};
```

### 🔄 Async Patterns
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

### 🌐 WebSockets
```javascript
const WebSocket = require('ws');
const wss = new WebSocket.Server({ port: 8080 });

wss.on('connection', (ws) => {
  ws.on('message', (message) => {
    wss.clients.forEach(client => {
      if (client !== ws && client.readyState === WebSocket.OPEN) {
        client.send(message);
      }
    });
  });
});
```

### 📊 Monitoring & Logging
```javascript
const winston = require('winston');

const logger = winston.createLogger({
  level: 'info',
  format: winston.format.json(),
  transports: [
    new winston.transports.File({ filename: 'error.log', level: 'error' }),
    new winston.transports.File({ filename: 'combined.log' })
  ]
});
```

### 🐳 Docker
```dockerfile
FROM node:18-alpine
WORKDIR /app
COPY package*.json ./
RUN npm ci --only=production
COPY . .
EXPOSE 3000
CMD ["node", "app.js"]
```

### 🔧 PM2 Commands
```bash
pm2 start app.js
pm2 start app.js -i 4
pm2 restart app
pm2 stop app
pm2 delete app
pm2 monit
pm2 logs app
```

### 🧪 Testing
```javascript
const request = require('supertest');
const app = require('../app');

test('GET /api/users', async () => {
  const response = await request(app)
    .get('/api/users')
    .expect(200);
  
  expect(response.body).toHaveProperty('users');
});
```

### 📈 Performance Tips
- Use `lean()` for Mongoose queries
- Implement caching with Redis
- Use compression middleware
- Optimize database queries
- Monitor memory usage
- Use worker threads for CPU-intensive tasks

### 🛡️ Security Checklist
- Use Helmet for security headers
- Implement rate limiting
- Validate and sanitize input
- Use HTTPS in production
- Keep dependencies updated
- Implement proper authentication
- Use environment variables for secrets

### 🚀 Deployment Checklist
- Set up health checks
- Implement graceful shutdown
- Configure logging
- Set up monitoring
- Use process managers (PM2)
- Implement CI/CD pipeline
- Use containerization (Docker)

---

*This cheatsheet provides quick reference for Node.js and Express.js development, covering fundamentals, security, performance, and deployment best practices.*
