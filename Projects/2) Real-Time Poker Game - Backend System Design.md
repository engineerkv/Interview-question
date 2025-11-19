# Real-Time Poker Game - Backend System Design

> **Backend Type:** Real-time Game Server  
> **Tech Stack:** Node.js, Express.js, Socket.io, MongoDB, Redis  
> **Deployment:** AWS (EC2, RDS, ElastiCache, S3)

---

## 1. System Architecture

### High-Level Architecture

```
┌─────────────────────────────────────────────────────────┐
│                    Client Applications                   │
│  ┌──────────────┐  ┌──────────────┐  ┌──────────────┐  │
│  │  Web (React) │  │ Mobile (RN)  │  │   Admin      │  │
│  └──────────────┘  └──────────────┘  └──────────────┘  │
└─────────────────────────────────────────────────────────┘
                        │
                        ▼
┌─────────────────────────────────────────────────────────┐
│                    Load Balancer (ALB)                   │
│         WebSocket Support & SSL Termination              │
└─────────────────────────────────────────────────────────┘
                        │
        ┌───────────────┼───────────────┐
        ▼               ▼               ▼
┌──────────────┐ ┌──────────────┐ ┌──────────────┐
│ Socket.io    │ │ Socket.io    │ │ Socket.io    │
│ Server 1     │ │ Server 2     │ │ Server 3     │
└──────────────┘ └──────────────┘ └──────────────┘
        │               │               │
        └───────────────┼───────────────┘
                        ▼
        ┌───────────────────────────────┐
        │      Redis Adapter            │
        │  (Shared Socket.io State)     │
        └───────────────────────────────┘
                        │
        ┌───────────────┼───────────────┐
        ▼               ▼               ▼
┌──────────────┐ ┌──────────────┐ ┌──────────────┐
│   Game       │ │   Room       │ │   User       │
│   Engine     │ │   Manager    │ │   Service    │
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
```

---

## 2. Technology Stack

### Core Technologies
- **Runtime:** Node.js (v18+)
- **Framework:** Express.js
- **Real-time:** Socket.io with Redis Adapter
- **Language:** TypeScript

### Database
- **Primary Database:** MongoDB
  - User data, game rooms, game history
  - Player statistics
  - Hand history
- **Cache:** Redis
  - Active game state (in-memory)
  - Room metadata
  - Session storage
  - Rate limiting
  - Socket.io adapter (shared state)

### External Services
- **File Storage:** AWS S3 (avatars, game assets)
- **CDN:** CloudFront (static assets)
- **Monitoring:** CloudWatch, New Relic
- **Logging:** Winston, CloudWatch Logs

### Infrastructure
- **Compute:** AWS EC2 (Auto Scaling Groups)
- **Load Balancer:** Application Load Balancer (ALB) with WebSocket support
- **Database:** MongoDB Atlas / AWS DocumentDB
- **Cache:** AWS ElastiCache (Redis Cluster)
- **Storage:** AWS S3

---

## 3. API Architecture

### RESTful API Endpoints

**Authentication**
- `POST /api/v1/auth/register` - User registration
- `POST /api/v1/auth/login` - User login
- `POST /api/v1/auth/refresh` - Refresh token
- `POST /api/v1/auth/logout` - User logout

**Game Rooms**
- `GET /api/v1/rooms` - Get available rooms
- `POST /api/v1/rooms` - Create new room
- `GET /api/v1/rooms/:roomId` - Get room details
- `POST /api/v1/rooms/:roomId/join` - Join room

**Game State**
- `GET /api/v1/games/:gameId/state` - Get current game state
- `GET /api/v1/games/:gameId/history` - Get hand history

**User**
- `GET /api/v1/users/:userId/stats` - Get user statistics
- `GET /api/v1/users/:userId/history` - Get game history

### WebSocket Events (Socket.io)

**Client → Server**
- `join-room` - Join a game room
- `leave-room` - Leave a game room
- `player-action` - Player game action (fold, call, raise, etc.)
- `send-message` - Send chat message
- `request-game-state` - Request current game state

**Server → Client**
- `room-updated` - Room state updated
- `game-state-updated` - Game state changed
- `player-joined` - New player joined
- `player-left` - Player left room
- `cards-dealt` - Cards dealt to players
- `action-required` - Player's turn to act
- `hand-completed` - Hand finished
- `new-message` - New chat message
- `error` - Error occurred

---

## 4. Database Schema Design

### MongoDB Collections

#### Users Collection
```javascript
{
  _id: ObjectId,
  username: String (unique, indexed),
  email: String (unique, indexed),
  password: String (hashed),
  avatar: String, // S3 URL
  chips: Number, // Virtual chips balance
  stats: {
    gamesPlayed: Number,
    gamesWon: Number,
    gamesLost: Number,
    totalWinnings: Number,
    winRate: Number
  },
  createdAt: Date,
  updatedAt: Date,
  lastLogin: Date
}
```

#### Game Rooms Collection
```javascript
{
  _id: ObjectId,
  name: String,
  type: String, // 'public' | 'private'
  maxPlayers: Number,
  currentPlayers: Number,
  smallBlind: Number,
  bigBlind: Number,
  buyIn: Number,
  status: String, // 'waiting' | 'playing' | 'finished'
  players: [{
    userId: ObjectId,
    seatNumber: Number,
    chips: Number,
    status: String
  }],
  createdAt: Date,
  updatedAt: Date
}
```

#### Game Sessions Collection
```javascript
{
  _id: ObjectId,
  roomId: ObjectId (indexed),
  phase: String, // 'pre-flop' | 'flop' | 'turn' | 'river' | 'showdown'
  communityCards: [Card],
  pot: Number,
  sidePots: [{
    amount: Number,
    eligiblePlayers: [ObjectId]
  }],
  currentBet: Number,
  minimumRaise: Number,
  dealerIndex: Number,
  currentPlayerIndex: Number,
  players: [PlayerState],
  handHistory: [HandHistoryItem],
  startedAt: Date,
  completedAt: Date
}
```

#### Hand History Collection
```javascript
{
  _id: ObjectId,
  gameId: ObjectId (indexed),
  roomId: ObjectId (indexed),
  handNumber: Number,
  phase: String,
  communityCards: [Card],
  players: [{
    userId: ObjectId,
    cards: [Card],
    actions: [PlayerAction],
    finalHand: Hand,
    chipsWon: Number
  }],
  pot: Number,
  winners: [{
    userId: ObjectId,
    hand: Hand,
    prize: Number
  }],
  completedAt: Date
}
```

### Redis Keys Structure

```
game:{gameId} - Active game state (TTL: 1 hour)
room:{roomId} - Room metadata (TTL: 2 hours)
session:{userId} - User session data
socket:{socketId} - Socket connection mapping
rate_limit:{userId}:{event} - Rate limiting counter
leaderboard:global - Global leaderboard (sorted set)
```

---

## 5. Game Engine Architecture

### Game State Machine

```
WAITING → PRE_FLOP → FLOP → TURN → RIVER → SHOWDOWN → FINISHED
   ↑                                                      │
   └──────────────────────────────────────────────────────┘
```

### Game Engine Components

#### 1. Card Dealer
- Shuffles deck
- Deals hole cards
- Deals community cards
- Manages card visibility

#### 2. Hand Evaluator
- Evaluates hand rankings
- Compares hands
- Determines winners
- Calculates side pots

#### 3. Betting Manager
- Validates betting actions
- Manages pot and side pots
- Handles all-in scenarios
- Enforces betting rules

#### 4. Turn Manager
- Manages turn order
- Enforces action timeouts
- Handles player actions
- Transitions game phases

#### 5. Pot Manager
- Calculates main pot
- Calculates side pots
- Distributes winnings
- Tracks chip movements

---

## 6. Socket.io Server Implementation

### Server Setup
```javascript
const io = require('socket.io')(server, {
  cors: {
    origin: process.env.ALLOWED_ORIGINS.split(','),
    credentials: true
  },
  transports: ['websocket', 'polling'],
  adapter: redisAdapter({ host: 'localhost', port: 6379 })
});

// Authentication middleware
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
  console.log(`User ${socket.userId} connected`);
  
  // Join room
  socket.on('join-room', async (roomId) => {
    const room = await Room.findById(roomId);
    if (!room) {
      return socket.emit('error', { message: 'Room not found' });
    }
    
    socket.join(`room:${roomId}`);
    socket.roomId = roomId;
    
    // Add player to room
    await addPlayerToRoom(roomId, socket.userId);
    
    // Broadcast player joined
    io.to(`room:${roomId}`).emit('player-joined', {
      userId: socket.userId,
      room: await getRoomState(roomId)
    });
  });
  
  // Player action
  socket.on('player-action', async (action) => {
    const gameState = await processPlayerAction(
      socket.roomId,
      socket.userId,
      action
    );
    
    // Broadcast updated game state
    io.to(`room:${socket.roomId}`).emit('game-state-updated', gameState);
  });
  
  // Disconnect
  socket.on('disconnect', async () => {
    if (socket.roomId) {
      await handlePlayerDisconnect(socket.roomId, socket.userId);
      io.to(`room:${socket.roomId}`).emit('player-left', {
        userId: socket.userId
      });
    }
  });
});
```

---

## 7. Game Logic Implementation

### Hand Ranking Algorithm
```javascript
const evaluateHand = (holeCards, communityCards) => {
  const allCards = [...holeCards, ...communityCards];
  const combinations = getBestFiveCardCombination(allCards);
  
  // Check for royal flush
  if (isRoyalFlush(combinations)) {
    return { rank: 10, description: 'Royal Flush' };
  }
  
  // Check for straight flush
  if (isStraightFlush(combinations)) {
    return { rank: 9, description: 'Straight Flush' };
  }
  
  // Check for four of a kind
  if (isFourOfAKind(combinations)) {
    return { rank: 8, description: 'Four of a Kind' };
  }
  
  // ... other hand rankings
  
  return { rank: 0, description: 'High Card' };
};
```

### Betting Validation
```javascript
const validateAction = (action, gameState, player) => {
  if (action.action === 'fold') {
    return { valid: true };
  }
  
  if (action.action === 'check') {
    if (gameState.currentBet > player.currentBet) {
      return { valid: false, error: 'Cannot check, must call or fold' };
    }
    return { valid: true };
  }
  
  if (action.action === 'call') {
    const callAmount = gameState.currentBet - player.currentBet;
    if (player.chips < callAmount) {
      return { valid: false, error: 'Insufficient chips' };
    }
    return { valid: true, amount: callAmount };
  }
  
  if (action.action === 'raise') {
    const minRaise = gameState.currentBet * 2;
    if (action.amount < minRaise) {
      return { valid: false, error: `Minimum raise is ${minRaise}` };
    }
    if (player.chips < action.amount) {
      return { valid: false, error: 'Insufficient chips' };
    }
    return { valid: true, amount: action.amount };
  }
  
  return { valid: false, error: 'Invalid action' };
};
```

---

## 8. Room Management

### Room Manager Service
```javascript
class RoomManager {
  async createRoom(roomData) {
    const room = await Room.create({
      ...roomData,
      status: 'waiting',
      currentPlayers: 0,
      players: []
    });
    
    // Store in Redis for quick access
    await redis.setex(`room:${room._id}`, 7200, JSON.stringify(room));
    
    return room;
  }
  
  async addPlayer(roomId, userId, seatNumber) {
    const room = await Room.findById(roomId);
    
    if (room.currentPlayers >= room.maxPlayers) {
      throw new Error('Room is full');
    }
    
    if (room.players.some(p => p.seatNumber === seatNumber)) {
      throw new Error('Seat already taken');
    }
    
    room.players.push({
      userId,
      seatNumber,
      chips: room.buyIn,
      status: 'active'
    });
    
    room.currentPlayers++;
    
    if (room.currentPlayers === room.maxPlayers) {
      room.status = 'playing';
      await this.startGame(roomId);
    }
    
    await room.save();
    await redis.setex(`room:${roomId}`, 7200, JSON.stringify(room));
    
    return room;
  }
  
  async startGame(roomId) {
    const gameState = await GameEngine.initializeGame(roomId);
    await redis.setex(`game:${gameState._id}`, 3600, JSON.stringify(gameState));
    return gameState;
  }
}
```

---

## 9. Scalability & Performance

### Horizontal Scaling with Redis Adapter
- **Redis Adapter:** Socket.io Redis adapter for shared state across servers
- **Sticky Sessions:** Session affinity for WebSocket connections
- **Load Balancing:** ALB with WebSocket support
- **Auto Scaling:** Scale Socket.io servers based on connection count

### Caching Strategy
- **Active Game State:** Redis for in-memory game state (fast access)
- **Room Metadata:** Redis cache for room information
- **Leaderboards:** Redis sorted sets for real-time leaderboards
- **Session Storage:** Redis for user sessions

### Database Optimization
- **Indexing:** Indexes on roomId, userId, gameId
- **Sharding:** MongoDB sharding by roomId for game sessions
- **Read Replicas:** Read replicas for game history queries
- **Connection Pooling:** MongoDB connection pooling

### Performance Monitoring
- **Connection Monitoring:** Track active WebSocket connections
- **Message Latency:** Monitor message delivery time
- **Game State Updates:** Track game state update frequency
- **Error Rates:** Monitor error rates and connection failures

---

## 10. Security

### Authentication & Authorization
- **JWT Tokens:** Stateless authentication for WebSocket connections
- **Socket Authentication:** Verify token on connection
- **Room Authorization:** Verify user can join specific room
- **Action Authorization:** Verify user can perform specific action

### Game Security
- **Server-Authoritative:** All game logic on server
- **Action Validation:** Validate all actions on server
- **State Verification:** Verify game state integrity
- **Anti-cheating:** Rate limiting, action sequence validation

### Rate Limiting
- **Per User:** Limit actions per user per second
- **Per Room:** Limit messages per room
- **Per Event:** Different limits for different events
- **Redis-based:** Distributed rate limiting

---

## 11. Disaster Recovery

### Game State Persistence
- **Redis Persistence:** RDB and AOF for Redis data
- **MongoDB Backups:** Daily backups of game history
- **State Recovery:** Recover game state from Redis/MongoDB
- **Reconnection Handling:** Restore game state on reconnection

### Failover Strategy
- **Multi-AZ Deployment:** Deploy across multiple availability zones
- **Redis Cluster:** Redis cluster with automatic failover
- **Database Replication:** MongoDB replica sets
- **Connection Migration:** Migrate connections on server failure

---

## 12. Monitoring & Logging

### Key Metrics
- **Active Connections:** Number of active WebSocket connections
- **Game Rooms:** Number of active game rooms
- **Message Latency:** Average message delivery time
- **Error Rates:** Error rate by type
- **Game Completion Rate:** Percentage of games completed

### Logging
- **Game Actions:** Log all game actions for audit
- **Connection Events:** Log connection/disconnection events
- **Errors:** Log all errors with stack traces
- **Performance:** Log slow operations

---

## 13. API Response Format

### Success Response
```json
{
  "success": true,
  "data": {
    // Response data
  }
}
```

### Error Response
```json
{
  "success": false,
  "error": {
    "code": "INVALID_ACTION",
    "message": "Cannot check, must call or fold"
  }
}
```

### WebSocket Event Format
```json
{
  "event": "game-state-updated",
  "data": {
    // Game state data
  },
  "timestamp": "2024-01-01T00:00:00Z"
}
```

---

## 14. Database Indexes

### Critical Indexes
```javascript
// Users
db.users.createIndex({ username: 1 }, { unique: true });
db.users.createIndex({ email: 1 }, { unique: true });

// Game Rooms
db.rooms.createIndex({ status: 1, type: 1 });
db.rooms.createIndex({ "players.userId": 1 });

// Game Sessions
db.games.createIndex({ roomId: 1 });
db.games.createIndex({ status: 1, startedAt: -1 });

// Hand History
db.handHistory.createIndex({ gameId: 1, handNumber: 1 });
db.handHistory.createIndex({ "players.userId": 1 });
db.handHistory.createIndex({ completedAt: -1 });
```

---

## 15. Load Balancing Strategy

### Application Load Balancer (ALB)
- **WebSocket Support:** ALB with WebSocket support
- **Sticky Sessions:** Session affinity for WebSocket connections
- **Health Checks:** HTTP health check endpoint `/health`
- **SSL Termination:** HTTPS/WSS at load balancer level

### Auto Scaling
- **Scale-out Trigger:** Connection count > 1000 per server
- **Scale-in Trigger:** Connection count < 500 per server
- **Min Instances:** 2
- **Max Instances:** 10
- **Desired Capacity:** 3

---

