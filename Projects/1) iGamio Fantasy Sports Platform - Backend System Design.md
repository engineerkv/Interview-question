# iGamio Fantasy Sports Platform - Backend System Design

> **Backend Type:** RESTful API Server  
> **Tech Stack:** Node.js, Express.js, MongoDB, Redis, Socket.io  
> **Deployment:** AWS (EC2, RDS, ElastiCache, S3, CloudFront)

---

## 1. System Architecture

### High-Level Architecture

```
┌─────────────────────────────────────────────────────────┐
│                    Client Applications                   │
│  ┌──────────────┐  ┌──────────────┐  ┌──────────────┐  │
│  │  Web (React) │  │ Mobile (RN)  │  │  B2B Portal  │  │
│  └──────────────┘  └──────────────┘  └──────────────┘  │
└─────────────────────────────────────────────────────────┘
                        │
                        ▼
┌─────────────────────────────────────────────────────────┐
│                    Load Balancer (ALB)                   │
│              Health Checks & SSL Termination             │
└─────────────────────────────────────────────────────────┘
                        │
        ┌───────────────┼───────────────┐
        ▼               ▼               ▼
┌──────────────┐ ┌──────────────┐ ┌──────────────┐
│  API Server  │ │  API Server  │ │  API Server  │
│  Instance 1  │ │  Instance 2  │ │  Instance 3  │
└──────────────┘ └──────────────┘ └──────────────┘
        │               │               │
        └───────────────┼───────────────┘
                        ▼
        ┌───────────────────────────────┐
        │      API Gateway Layer        │
        │  - Authentication             │
        │  - Rate Limiting              │
        │  - Request Validation         │
        └───────────────────────────────┘
                        │
        ┌───────────────┼───────────────┐
        ▼               ▼               ▼
┌──────────────┐ ┌──────────────┐ ┌──────────────┐
│   Auth       │ │   Match      │ │   Contest    │
│   Service    │ │   Service    │ │   Service    │
└──────────────┘ └──────────────┘ └──────────────┘
        │               │               │
        └───────────────┼───────────────┘
                        ▼
        ┌───────────────────────────────┐
        │      Data Layer               │
        │  ┌──────────┐  ┌──────────┐  │
        │  │ MongoDB  │  │  Redis   │  │
        │  │ (Primary)│  │ (Cache)  │  │
        │  └──────────┘  └──────────┘  │
        └───────────────────────────────┘
                        │
        ┌───────────────┼───────────────┐
        ▼               ▼               ▼
┌──────────────┐ ┌──────────────┐ ┌──────────────┐
│   Payment    │ │   KYC        │ │   Real-time  │
│   Gateway    │ │   Service    │ │   Service    │
│  (Cashfree)  │ │              │ │  (Socket.io) │
└──────────────┘ └──────────────┘ └──────────────┘
```

---

## 2. Technology Stack

### Core Technologies
- **Runtime:** Node.js (v18+)
- **Framework:** Express.js
- **Language:** JavaScript/TypeScript

### Database
- **Primary Database:** MongoDB (Document Store)
  - User data, matches, contests, teams
  - Flexible schema for different sports
  - Horizontal scaling with sharding
- **Cache:** Redis
  - Session storage
  - API response caching
  - Real-time match data
  - Rate limiting counters

### External Services
- **Payment Gateway:** Cashfree API
- **File Storage:** AWS S3 (KYC documents, images)
- **CDN:** CloudFront (static assets)
- **Monitoring:** CloudWatch, New Relic
- **Logging:** Winston, CloudWatch Logs

### Infrastructure
- **Compute:** AWS EC2 (Auto Scaling Groups)
- **Load Balancer:** Application Load Balancer (ALB)
- **Database:** MongoDB Atlas / AWS DocumentDB
- **Cache:** AWS ElastiCache (Redis)
- **Storage:** AWS S3
- **CDN:** CloudFront

---

## 3. API Architecture

### RESTful API Design

#### Base URL Structure
```
https://api.igamio.com/v1/
```

#### API Endpoints

**Authentication**
- `POST /api/v1/auth/register` - User registration
- `POST /api/v1/auth/login` - User login
- `POST /api/v1/auth/refresh` - Refresh token
- `POST /api/v1/auth/logout` - User logout

**Matches**
- `GET /api/v1/matches` - Get matches list (with filters)
- `GET /api/v1/matches/:matchId` - Get match details
- `GET /api/v1/matches/:matchId/players` - Get players for match
- `GET /api/v1/matches/:matchId/score` - Get live score

**Contests**
- `GET /api/v1/contests` - Get contests list
- `GET /api/v1/contests/:contestId` - Get contest details
- `POST /api/v1/contests/:contestId/join` - Join contest
- `GET /api/v1/contests/:contestId/leaderboard` - Get leaderboard

**Teams**
- `POST /api/v1/teams` - Create team
- `PUT /api/v1/teams/:teamId` - Update team
- `GET /api/v1/teams/:teamId` - Get team details
- `GET /api/v1/users/:userId/teams` - Get user's teams

**Wallet & Payments**
- `GET /api/v1/wallet/balance` - Get wallet balance
- `POST /api/v1/wallet/deposit` - Initiate deposit
- `POST /api/v1/wallet/withdraw` - Request withdrawal
- `GET /api/v1/wallet/transactions` - Get transaction history
- `POST /api/v1/payments/cashfree/webhook` - Payment webhook

**KYC**
- `POST /api/v1/kyc/upload` - Upload KYC document
- `GET /api/v1/kyc/status` - Get KYC status
- `POST /api/v1/kyc/verify` - Verify document (Cashfree API)

**B2B**
- `POST /api/v1/b2b/contests` - Create custom contest
- `GET /api/v1/b2b/analytics` - Get analytics
- `GET /api/v1/b2b/users` - Get B2B users

---

## 4. Database Schema Design

### MongoDB Collections

#### Users Collection
```javascript
{
  _id: ObjectId,
  email: String (unique, indexed),
  phone: String (unique, indexed),
  password: String (hashed),
  name: String,
  userType: String, // 'B2C' | 'B2B'
  kycStatus: String, // 'pending' | 'verified' | 'rejected'
  walletBalance: Number,
  createdAt: Date,
  updatedAt: Date,
  lastLogin: Date
}
```

#### Matches Collection
```javascript
{
  _id: ObjectId,
  sport: String, // 'cricket' | 'football' | 'kabaddi'
  teamA: {
    id: String,
    name: String,
    players: [Player]
  },
  teamB: {
    id: String,
    name: String,
    players: [Player]
  },
  status: String, // 'scheduled' | 'live' | 'completed'
  scheduledAt: Date,
  startedAt: Date,
  completedAt: Date,
  venue: String,
  score: {
    teamA: Number,
    teamB: Number
  },
  createdAt: Date,
  updatedAt: Date
}
```

#### Contests Collection
```javascript
{
  _id: ObjectId,
  matchId: ObjectId (indexed),
  name: String,
  type: String, // 'free' | 'paid' | 'private' | 'public'
  entryFee: Number,
  prizePool: Number,
  maxParticipants: Number,
  currentParticipants: Number,
  prizeDistribution: [{
    rank: Number,
    prize: Number
  }],
  participants: [{
    userId: ObjectId,
    teamId: ObjectId,
    rank: Number,
    points: Number
  }],
  status: String, // 'open' | 'full' | 'live' | 'completed'
  startTime: Date,
  endTime: Date,
  createdAt: Date,
  updatedAt: Date
}
```

#### Teams Collection
```javascript
{
  _id: ObjectId,
  userId: ObjectId (indexed),
  matchId: ObjectId (indexed),
  players: [{
    playerId: ObjectId,
    isCaptain: Boolean,
    isViceCaptain: Boolean
  }],
  totalPoints: Number,
  rank: Number,
  createdAt: Date,
  updatedAt: Date,
  version: Number // For optimistic locking
}
```

#### Transactions Collection
```javascript
{
  _id: ObjectId,
  userId: ObjectId (indexed),
  type: String, // 'deposit' | 'withdraw' | 'contest_join' | 'contest_win'
  amount: Number,
  status: String, // 'pending' | 'success' | 'failed'
  paymentId: String,
  paymentGateway: String, // 'cashfree'
  contestId: ObjectId,
  metadata: Object,
  createdAt: Date,
  updatedAt: Date
}
```

### Redis Keys Structure

```
sessions:{userId} - User session data
match:{matchId} - Match data cache (TTL: 5 min)
contest:{contestId} - Contest data cache (TTL: 2 min)
leaderboard:{contestId} - Leaderboard cache (TTL: 30 sec)
rate_limit:{userId}:{endpoint} - Rate limiting counter
```

---

## 5. Service Architecture

### Microservices Structure

#### 1. Authentication Service
- User registration and login
- JWT token generation and validation
- Session management
- Password hashing (bcrypt)

#### 2. Match Service
- Match data management
- Live score updates
- Player statistics
- Match scheduling

#### 3. Contest Service
- Contest creation and management
- Contest joining logic
- Leaderboard calculation
- Prize distribution

#### 4. Team Service
- Team creation and validation
- Team update with deadline checking
- Team composition validation
- Points calculation

#### 5. Payment Service
- Payment gateway integration (Cashfree)
- Transaction processing
- Webhook handling
- Wallet management

#### 6. KYC Service
- Document upload and storage (S3)
- KYC verification (Cashfree API)
- Status tracking
- Document validation

#### 7. Real-time Service (Socket.io)
- Live match updates
- Contest leaderboard updates
- Push notifications
- Connection management

---

## 6. API Implementation Details

### Authentication Middleware
```javascript
const authenticate = async (req, res, next) => {
  try {
    const token = req.headers.authorization?.split(' ')[1];
    if (!token) {
      return res.status(401).json({ error: 'No token provided' });
    }
    
    const decoded = jwt.verify(token, process.env.JWT_SECRET);
    const user = await User.findById(decoded.userId);
    
    if (!user) {
      return res.status(401).json({ error: 'User not found' });
    }
    
    req.user = user;
    next();
  } catch (error) {
    res.status(401).json({ error: 'Invalid token' });
  }
};
```

### Rate Limiting
```javascript
const rateLimiter = rateLimit({
  windowMs: 15 * 60 * 1000, // 15 minutes
  max: 100, // 100 requests per window
  keyGenerator: (req) => req.user?.id || req.ip,
  store: new RedisStore({ client: redisClient })
});
```

### Error Handling
```javascript
const errorHandler = (err, req, res, next) => {
  logger.error(err);
  
  if (err.name === 'ValidationError') {
    return res.status(400).json({
      error: 'Validation Error',
      details: err.message
    });
  }
  
  if (err.name === 'UnauthorizedError') {
    return res.status(401).json({
      error: 'Unauthorized'
    });
  }
  
  res.status(500).json({
    error: 'Internal Server Error',
    message: process.env.NODE_ENV === 'development' ? err.message : 'Something went wrong'
  });
};
```

### Caching Strategy
```javascript
const cacheMiddleware = (duration = 300) => {
  return async (req, res, next) => {
    const key = `cache:${req.originalUrl}`;
    const cached = await redis.get(key);
    
    if (cached) {
      return res.json(JSON.parse(cached));
    }
    
    res.sendResponse = res.json;
    res.json = (data) => {
      redis.setex(key, duration, JSON.stringify(data));
      res.sendResponse(data);
    };
    
    next();
  };
};
```

---

## 7. Real-time Updates (Socket.io)

### Socket.io Server Setup
```javascript
const io = require('socket.io')(server, {
  cors: {
    origin: process.env.ALLOWED_ORIGINS.split(','),
    credentials: true
  }
});

io.use(async (socket, next) => {
  const token = socket.handshake.auth.token;
  try {
    const decoded = jwt.verify(token, process.env.JWT_SECRET);
    socket.userId = decoded.userId;
    next();
  } catch (error) {
    next(new Error('Authentication error'));
  }
});

io.on('connection', (socket) => {
  socket.on('subscribe:match', (matchId) => {
    socket.join(`match:${matchId}`);
  });
  
  socket.on('unsubscribe:match', (matchId) => {
    socket.leave(`match:${matchId}`);
  });
});

// Broadcast match update
const broadcastMatchUpdate = (matchId, data) => {
  io.to(`match:${matchId}`).emit('match:update', data);
};
```

---

## 8. Payment Gateway Integration

### Cashfree Integration
```javascript
const cashfree = require('cashfree-sdk');

const initiatePayment = async (userId, amount, paymentMethod) => {
  const orderId = `order_${Date.now()}_${userId}`;
  
  const paymentData = {
    orderId,
    orderAmount: amount,
    orderCurrency: 'INR',
    customerDetails: {
      customerId: userId,
      customerEmail: user.email,
      customerPhone: user.phone
    },
    orderNote: 'Fantasy Sports Contest Entry'
  };
  
  const response = await cashfree.PGCreateOrder(paymentData);
  
  // Store transaction in database
  await Transaction.create({
    userId,
    type: 'deposit',
    amount,
    status: 'pending',
    paymentId: orderId,
    paymentGateway: 'cashfree'
  });
  
  return {
    paymentUrl: response.paymentSessionId,
    orderId
  };
};

// Webhook handler
app.post('/api/v1/payments/cashfree/webhook', async (req, res) => {
  const { orderId, orderStatus, paymentAmount } = req.body;
  
  if (orderStatus === 'PAID') {
    await Transaction.updateOne(
      { paymentId: orderId },
      { status: 'success', updatedAt: new Date() }
    );
    
    // Update wallet balance
    await User.updateOne(
      { _id: transaction.userId },
      { $inc: { walletBalance: paymentAmount } }
    );
  }
  
  res.status(200).json({ status: 'success' });
});
```

---

## 9. Scalability & Performance

### Horizontal Scaling
- **Load Balancer:** Distributes traffic across multiple API server instances
- **Auto Scaling:** Automatically scales instances based on CPU/memory usage
- **Database Sharding:** MongoDB sharding by userId for user-related collections
- **Read Replicas:** MongoDB read replicas for read-heavy operations

### Caching Strategy
- **API Response Caching:** Redis cache for frequently accessed data (matches, contests)
- **Session Caching:** Redis for session storage
- **Leaderboard Caching:** Redis sorted sets for real-time leaderboards
- **CDN:** CloudFront for static assets (images, CSS, JS)

### Database Optimization
- **Indexing:** Proper indexes on frequently queried fields
- **Query Optimization:** Aggregation pipelines for complex queries
- **Connection Pooling:** MongoDB connection pooling
- **Read Preferences:** Read from replicas for non-critical queries

### Performance Monitoring
- **APM:** New Relic for application performance monitoring
- **Logging:** Winston for structured logging
- **Metrics:** CloudWatch for system metrics
- **Alerts:** CloudWatch alarms for error rates and latency

---

## 10. Security

### Authentication & Authorization
- **JWT Tokens:** Stateless authentication with refresh tokens
- **Password Hashing:** bcrypt with salt rounds
- **Role-Based Access:** RBAC for B2B vs B2C users
- **API Keys:** For B2B integrations

### Data Security
- **HTTPS:** All API calls over HTTPS
- **Data Encryption:** Sensitive data encrypted at rest
- **Input Validation:** Joi/express-validator for request validation
- **SQL Injection Prevention:** MongoDB parameterized queries
- **XSS Prevention:** Input sanitization

### Rate Limiting
- **Per User:** 100 requests per 15 minutes
- **Per IP:** 1000 requests per hour
- **Per Endpoint:** Different limits for different endpoints
- **Redis-based:** Distributed rate limiting using Redis

---

## 11. Deployment & DevOps

### CI/CD Pipeline
```
Code Push → GitHub Actions → 
  Run Tests → 
  Build Docker Image → 
  Push to ECR → 
  Deploy to ECS/EC2 → 
  Health Check → 
  Rollback if failed
```

### Infrastructure as Code
- **Terraform:** Infrastructure provisioning
- **Docker:** Containerization
- **Kubernetes (Optional):** Container orchestration

### Monitoring & Logging
- **Application Logs:** CloudWatch Logs
- **Error Tracking:** Sentry
- **Performance Monitoring:** New Relic APM
- **Uptime Monitoring:** CloudWatch Alarms

---

## 12. API Response Format

### Success Response
```json
{
  "success": true,
  "data": {
    // Response data
  },
  "pagination": {
    "page": 1,
    "limit": 20,
    "total": 100,
    "totalPages": 5
  }
}
```

### Error Response
```json
{
  "success": false,
  "error": {
    "code": "VALIDATION_ERROR",
    "message": "Invalid input data",
    "details": {
      "field": "email",
      "message": "Email is required"
    }
  }
}
```

---

## 13. Database Indexes

### Critical Indexes
```javascript
// Users
db.users.createIndex({ email: 1 }, { unique: true });
db.users.createIndex({ phone: 1 }, { unique: true });
db.users.createIndex({ userType: 1 });

// Matches
db.matches.createIndex({ sport: 1, status: 1 });
db.matches.createIndex({ scheduledAt: 1 });
db.matches.createIndex({ status: 1, scheduledAt: 1 });

// Contests
db.contests.createIndex({ matchId: 1 });
db.contests.createIndex({ status: 1, startTime: 1 });
db.contests.createIndex({ "participants.userId": 1 });

// Teams
db.teams.createIndex({ userId: 1, matchId: 1 });
db.teams.createIndex({ matchId: 1, createdAt: 1 });

// Transactions
db.transactions.createIndex({ userId: 1, createdAt: -1 });
db.transactions.createIndex({ paymentId: 1 });
db.transactions.createIndex({ status: 1 });
```

---

## 14. Load Balancing Strategy

### Application Load Balancer (ALB)
- **Health Checks:** HTTP health check endpoint `/health`
- **Sticky Sessions:** Session affinity for WebSocket connections
- **SSL Termination:** HTTPS at load balancer level
- **Path-based Routing:** Route different paths to different services

### Auto Scaling
- **Scale-out Trigger:** CPU > 70% for 5 minutes
- **Scale-in Trigger:** CPU < 30% for 15 minutes
- **Min Instances:** 2
- **Max Instances:** 10
- **Desired Capacity:** 3

---

## 15. Disaster Recovery

### Backup Strategy
- **Database Backups:** Daily MongoDB backups, retained for 30 days
- **S3 Backups:** KYC documents backed up to S3 with versioning
- **Configuration Backups:** Infrastructure configuration in version control

### Failover Strategy
- **Multi-AZ Deployment:** Deploy across multiple availability zones
- **Database Replication:** MongoDB replica sets
- **Cache Failover:** Redis cluster with automatic failover
- **CDN Failover:** CloudFront with multiple origins

---

