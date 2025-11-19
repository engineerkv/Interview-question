# Real-Time Poker Game - Low Level Design (LLD)

> **Project Type:** Multiplayer Real-time Card Game (Web Application)  
> **Tech Stack:** React.js, TypeScript, Socket.io, REST APIs

---

## 3. Component Architecture

### Routing Structure

```
App Router
├── Public Routes
│   ├── Login Page
│   ├── Register Page
│   └── Landing Page
├── Protected Routes
│   ├── Lobby Page
│   │   ├── Room List
│   │   ├── Create Room Modal
│   │   └── Room Search
│   ├── Game Room Page
│   │   ├── Game Table
│   │   ├── Player Seats
│   │   ├── Community Cards
│   │   ├── Action Buttons
│   │   ├── Pot Display
│   │   ├── Chat Panel
│   │   └── Hand History
│   ├── Profile Page
│   │   ├── User Stats
│   │   ├── Game History
│   │   └── Settings
│   └── Leaderboard Page
└── Spectator Routes
    └── Spectate Game Page
```

### Component Hierarchy

```
App
├── Router
│   ├── PublicRoute
│   │   └── LoginPage
│   │       ├── LoginForm
│   │       └── SocialLogin
│   └── ProtectedRoute
│       ├── LobbyPage
│       │   ├── RoomList
│       │   │   ├── RoomCard
│       │   │   │   ├── RoomInfo
│       │   │   │   ├── PlayerCount
│       │   │   │   └── JoinButton
│       │   │   └── FilterBar
│       │   ├── CreateRoomModal
│       │   │   ├── RoomSettings
│       │   │   └── CreateButton
│       │   └── SearchBar
│       ├── GameRoomPage
│       │   ├── GameTable
│       │   │   ├── TableCanvas
│       │   │   ├── PlayerSeats
│       │   │   │   └── PlayerSeat
│       │   │   │       ├── PlayerAvatar
│       │   │   │       ├── PlayerCards
│       │   │   │       ├── PlayerChips
│       │   │   │       ├── PlayerStatus
│       │   │   │       └── PlayerAction
│       │   │   ├── CommunityCards
│       │   │   │   └── Card
│       │   │   ├── PotDisplay
│       │   │   │   ├── MainPot
│       │   │   │   └── SidePots
│       │   │   └── DealerButton
│       │   ├── ActionPanel
│       │   │   ├── ActionButtons
│       │   │   │   ├── FoldButton
│       │   │   │   ├── CheckButton
│       │   │   │   ├── CallButton
│       │   │   │   ├── RaiseButton
│       │   │   │   └── AllInButton
│       │   │   ├── BetSlider
│       │   │   └── TimerDisplay
│       │   ├── ChatPanel
│       │   │   ├── ChatMessages
│       │   │   │   └── ChatMessage
│       │   │   └── ChatInput
│       │   └── HandHistory
│       │       └── HandHistoryItem
│       └── ProfilePage
│           ├── UserStats
│           │   ├── WinRate
│           │   ├── GamesPlayed
│           │   └── TotalWinnings
│           └── GameHistory
│               └── GameHistoryItem
└── GameProvider (Context)
    ├── GameState
    ├── SocketConnection
    └── GameActions
```

### Data Sharing Strategy

#### Global State (Context API + useReducer)
- **Game State:** Current game room, players, cards, pot, betting round
- **User State:** Current user, authentication status
- **Socket State:** Connection status, room subscriptions
- **UI State:** Modals, notifications, loading states

#### Local State (Component State)
- **Form Inputs:** Login form, room creation form, chat input
- **UI State:** Modal visibility, dropdowns, tooltips
- **Animation State:** Card flip states, chip animation states

#### Socket.io Events
- **Real-time Updates:** Game actions, player updates, card dealing
- **Room Events:** Player join/leave, room updates
- **Chat Events:** New messages, typing indicators

#### Props Drilling
- **Simple Data:** Pass props for parent-child communication
- **Avoid Deep Nesting:** Use Context for deeply nested game components

---

## 4. Data Models

### User Model
```typescript
interface User {
  id: string;
  username: string;
  email: string;
  avatar?: string;
  chips: number;
  stats: UserStats;
  createdAt: string;
}

interface UserStats {
  gamesPlayed: number;
  gamesWon: number;
  gamesLost: number;
  totalWinnings: number;
  winRate: number;
}
```

### Game Room Model
```typescript
interface GameRoom {
  id: string;
  name: string;
  type: 'public' | 'private';
  maxPlayers: number;
  currentPlayers: number;
  smallBlind: number;
  bigBlind: number;
  buyIn: number;
  status: 'waiting' | 'playing' | 'finished';
  players: Player[];
  createdAt: string;
}
```

### Player Model
```typescript
interface Player {
  id: string;
  userId: string;
  username: string;
  avatar?: string;
  seatNumber: number;
  chips: number;
  cards: Card[];
  status: 'active' | 'folded' | 'all-in' | 'sitting-out';
  currentBet: number;
  isDealer: boolean;
  isSmallBlind: boolean;
  isBigBlind: boolean;
  isTurn: boolean;
  lastAction?: PlayerAction;
}
```

### Card Model
```typescript
interface Card {
  suit: 'hearts' | 'diamonds' | 'clubs' | 'spades';
  rank: '2' | '3' | '4' | '5' | '6' | '7' | '8' | '9' | '10' | 'J' | 'Q' | 'K' | 'A';
  value: number; // For comparison
  isVisible: boolean; // For hole cards
}

interface Hand {
  cards: Card[];
  rank: HandRank;
  description: string;
}
```

### Game State Model
```typescript
interface GameState {
  roomId: string;
  phase: 'pre-flop' | 'flop' | 'turn' | 'river' | 'showdown' | 'finished';
  communityCards: Card[];
  pot: number;
  sidePots: SidePot[];
  currentBet: number;
  minimumRaise: number;
  activePlayers: Player[];
  currentPlayerIndex: number;
  dealerIndex: number;
  winners: Winner[];
  handHistory: HandHistoryItem[];
}
```

### Player Action Model
```typescript
interface PlayerAction {
  playerId: string;
  action: 'fold' | 'check' | 'call' | 'raise' | 'all-in';
  amount?: number;
  timestamp: string;
}
```

### Message Model
```typescript
interface ChatMessage {
  id: string;
  userId: string;
  username: string;
  message: string;
  timestamp: string;
  type: 'text' | 'emoji' | 'system';
}
```

---

## 5. Data APIs

### Authentication APIs

#### POST /api/auth/register
- **URL:** `/api/auth/register`
- **Method:** POST
- **Request Body:**
  ```json
  {
    "username": "player123",
    "email": "player@example.com",
    "password": "securePassword123"
  }
  ```
- **Response:**
  ```json
  {
    "success": true,
    "data": {
      "user": { /* User object */ },
      "token": "jwt_token_here"
    }
  }
  ```
- **Status Codes:** 200 (Success), 400 (Validation Error), 409 (User Exists)

#### POST /api/auth/login
- **URL:** `/api/auth/login`
- **Method:** POST
- **Request Body:**
  ```json
  {
    "email": "player@example.com",
    "password": "securePassword123"
  }
  ```
- **Response:**
  ```json
  {
    "success": true,
    "data": {
      "user": { /* User object */ },
      "token": "jwt_token_here"
    }
  }
  ```
- **Status Codes:** 200 (Success), 401 (Invalid Credentials)

### Game Room APIs

#### GET /api/rooms
- **URL:** `/api/rooms?status=waiting&type=public&page=1&limit=20`
- **Method:** GET
- **Query Parameters:**
  - `status`: waiting | playing | finished
  - `type`: public | private
  - `page`: number
  - `limit`: number
- **Response:**
  ```json
  {
    "success": true,
    "data": {
      "rooms": [ /* Array of GameRoom objects */ ],
      "pagination": {
        "page": 1,
        "limit": 20,
        "total": 100,
        "totalPages": 5
      }
    }
  }
  ```
- **Status Codes:** 200 (Success)

#### POST /api/rooms
- **URL:** `/api/rooms`
- **Method:** POST
- **Request Body:**
  ```json
  {
    "name": "High Stakes Room",
    "type": "private",
    "maxPlayers": 6,
    "smallBlind": 10,
    "bigBlind": 20,
    "buyIn": 1000
  }
  ```
- **Response:**
  ```json
  {
    "success": true,
    "data": {
      "room": { /* GameRoom object */ }
    }
  }
  ```
- **Status Codes:** 200 (Success), 400 (Validation Error)

#### GET /api/rooms/:roomId
- **URL:** `/api/rooms/123`
- **Method:** GET
- **Response:**
  ```json
  {
    "success": true,
    "data": {
      "room": { /* GameRoom object with full details */ }
    }
  }
  ```
- **Status Codes:** 200 (Success), 404 (Room Not Found)

#### POST /api/rooms/:roomId/join
- **URL:** `/api/rooms/123/join`
- **Method:** POST
- **Request Body:**
  ```json
  {
    "seatNumber": 1
  }
  ```
- **Response:**
  ```json
  {
    "success": true,
    "data": {
      "room": { /* Updated GameRoom object */ },
      "player": { /* Player object */ }
    }
  }
  ```
- **Status Codes:** 200 (Success), 400 (Room Full), 403 (Invalid Seat)

### Game APIs

#### GET /api/games/:gameId/state
- **URL:** `/api/games/456/state`
- **Method:** GET
- **Response:**
  ```json
  {
    "success": true,
    "data": {
      "gameState": { /* GameState object */ }
    }
  }
  ```
- **Status Codes:** 200 (Success), 404 (Game Not Found)

#### GET /api/games/:gameId/history
- **URL:** `/api/games/456/history?page=1&limit=10`
- **Method:** GET
- **Response:**
  ```json
  {
    "success": true,
    "data": {
      "history": [ /* Array of HandHistoryItem objects */ ],
      "pagination": { /* Pagination object */ }
    }
  }
  ```
- **Status Codes:** 200 (Success)

### User APIs

#### GET /api/users/:userId/stats
- **URL:** `/api/users/789/stats`
- **Method:** GET
- **Response:**
  ```json
  {
    "success": true,
    "data": {
      "stats": { /* UserStats object */ }
    }
  }
  ```
- **Status Codes:** 200 (Success)

#### GET /api/users/:userId/history
- **URL:** `/api/users/789/history?page=1&limit=20`
- **Method:** GET
- **Response:**
  ```json
  {
    "success": true,
    "data": {
      "history": [ /* Array of game history items */ ],
      "pagination": { /* Pagination object */ }
    }
  }
  ```
- **Status Codes:** 200 (Success)

---

## 6. Protocols

### REST API Protocol
- **Protocol:** REST (Representational State Transfer)
- **Data Format:** JSON (JavaScript Object Notation)
- **HTTP Methods:**
  - GET: Retrieve data
  - POST: Create new resources
  - PUT: Update existing resources
  - DELETE: Delete resources
- **Status Codes:**
  - 200: Success
  - 201: Created
  - 400: Bad Request
  - 401: Unauthorized
  - 403: Forbidden
  - 404: Not Found
  - 500: Internal Server Error

### WebSocket Protocol (Socket.io)
- **Protocol:** WebSocket with Socket.io
- **Connection:** WSS (WebSocket Secure)
- **Events:**
  - **Client to Server:**
    - `join-room`: Join a game room
    - `leave-room`: Leave a game room
    - `player-action`: Player game action (fold, call, raise, etc.)
    - `send-message`: Send chat message
    - `request-game-state`: Request current game state
  - **Server to Client:**
    - `room-updated`: Room state updated
    - `game-state-updated`: Game state changed
    - `player-joined`: New player joined
    - `player-left`: Player left room
    - `cards-dealt`: Cards dealt to players
    - `action-required`: Player's turn to act
    - `hand-completed`: Hand finished
    - `new-message`: New chat message
    - `error`: Error occurred

### Authentication Protocol
- **Method:** JWT (JSON Web Tokens)
- **Token Storage:** localStorage or httpOnly cookies
- **Token Refresh:** Refresh token mechanism
- **Header Format:** `Authorization: Bearer <token>`
- **Socket Authentication:** Token sent during connection handshake

### Real-time Communication Protocol
- **Method:** Socket.io with WebSocket
- **Room-based:** Players join specific game rooms
- **Event-driven:** Event-based communication
- **Automatic Reconnection:** Socket.io handles reconnection
- **Heartbeat:** Keep-alive mechanism

---

## 7. Implementation Details

### Code Splitting with React.lazy
```typescript
// Lazy load game room page
const GameRoomPage = React.lazy(() => import('./pages/GameRoomPage'));
const LobbyPage = React.lazy(() => import('./pages/LobbyPage'));

// Route with Suspense
<Suspense fallback={<LoadingSpinner />}>
  <Routes>
    <Route path="/game/:roomId" element={<GameRoomPage />} />
    <Route path="/lobby" element={<LobbyPage />} />
  </Routes>
</Suspense>
```

### Socket.io Connection Management
```typescript
// Socket connection setup
import { io, Socket } from 'socket.io-client';

const socket: Socket = io(process.env.REACT_APP_SOCKET_URL, {
  auth: {
    token: getAuthToken()
  },
  transports: ['websocket'],
  reconnection: true,
  reconnectionDelay: 1000,
  reconnectionAttempts: 5
});

// Event listeners
socket.on('connect', () => {
  console.log('Connected to server');
});

socket.on('disconnect', () => {
  console.log('Disconnected from server');
});

socket.on('game-state-updated', (gameState: GameState) => {
  dispatch(updateGameState(gameState));
});
```

### Game State Management with Context API
```typescript
// Game Context
interface GameContextType {
  gameState: GameState | null;
  socket: Socket | null;
  joinRoom: (roomId: string) => void;
  leaveRoom: () => void;
  performAction: (action: PlayerAction) => void;
}

const GameContext = createContext<GameContextType | null>(null);

// Game Provider
const GameProvider: React.FC<{ children: React.ReactNode }> = ({ children }) => {
  const [gameState, dispatch] = useReducer(gameReducer, null);
  const [socket, setSocket] = useState<Socket | null>(null);

  useEffect(() => {
    const newSocket = io(process.env.REACT_APP_SOCKET_URL, {
      auth: { token: getAuthToken() }
    });
    setSocket(newSocket);

    newSocket.on('game-state-updated', (state: GameState) => {
      dispatch({ type: 'UPDATE_GAME_STATE', payload: state });
    });

    return () => {
      newSocket.close();
    };
  }, []);

  const performAction = (action: PlayerAction) => {
    socket?.emit('player-action', action);
  };

  return (
    <GameContext.Provider value={{ gameState, socket, performAction }}>
      {children}
    </GameContext.Provider>
  );
};
```

### Card Animation with Framer Motion
```typescript
import { motion } from 'framer-motion';

// Card component with animation
const Card: React.FC<{ card: Card; delay?: number }> = ({ card, delay = 0 }) => {
  return (
    <motion.div
      initial={{ opacity: 0, scale: 0, rotateY: 180 }}
      animate={{ opacity: 1, scale: 1, rotateY: 0 }}
      transition={{ duration: 0.5, delay }}
      className="card"
    >
      {card.isVisible ? (
        <img src={`/cards/${card.suit}-${card.rank}.png`} alt={`${card.rank} of ${card.suit}`} />
      ) : (
        <img src="/cards/back.png" alt="Card back" />
      )}
    </motion.div>
  );
};

// Chip animation
const Chip: React.FC<{ amount: number; position: { x: number; y: number } }> = ({ amount, position }) => {
  return (
    <motion.div
      initial={{ x: 0, y: 0, scale: 0 }}
      animate={{ x: position.x, y: position.y, scale: 1 }}
      transition={{ duration: 0.6, ease: "easeOut" }}
      className="chip"
    >
      {amount}
    </motion.div>
  );
};
```

### Reduced Re-renders with useMemo and useCallback
```typescript
// Memoize expensive calculations
const handRank = useMemo(() => {
  return calculateHandRank(player.cards, communityCards);
}, [player.cards, communityCards]);

// Memoize callbacks
const handleFold = useCallback(() => {
  performAction({ action: 'fold', playerId: currentPlayer.id });
}, [currentPlayer.id, performAction]);

// Memoize components
const PlayerSeat = React.memo(({ player }: { player: Player }) => {
  return (
    <div className="player-seat">
      <PlayerAvatar player={player} />
      <PlayerCards cards={player.cards} />
      <PlayerChips chips={player.chips} />
    </div>
  );
});
```

### Pagination for Room List
```typescript
// Infinite scroll for room list
const useInfiniteRooms = () => {
  const [rooms, setRooms] = useState<GameRoom[]>([]);
  const [page, setPage] = useState(1);
  const [hasMore, setHasMore] = useState(true);
  const [loading, setLoading] = useState(false);

  const loadMore = useCallback(async () => {
    if (loading || !hasMore) return;

    setLoading(true);
    const response = await axios.get('/api/rooms', {
      params: { page, limit: 20 }
    });

    setRooms(prev => [...prev, ...response.data.rooms]);
    setHasMore(response.data.pagination.hasMore);
    setPage(prev => prev + 1);
    setLoading(false);
  }, [page, hasMore, loading]);

  return { rooms, loadMore, hasMore, loading };
};
```

### Debouncing for Search
```typescript
// Debounced search for rooms
const useDebouncedSearch = (delay: number = 300) => {
  const [searchTerm, setSearchTerm] = useState('');
  const [debouncedTerm, setDebouncedTerm] = useState('');

  useEffect(() => {
    const timer = setTimeout(() => {
      setDebouncedTerm(searchTerm);
    }, delay);

    return () => clearTimeout(timer);
  }, [searchTerm, delay]);

  return { searchTerm, debouncedTerm, setSearchTerm };
};
```

### Error Handling
```typescript
// Error boundary for game components
class GameErrorBoundary extends React.Component {
  state = { hasError: false, error: null };

  static getDerivedStateFromError(error: Error) {
    return { hasError: true, error };
  }

  componentDidCatch(error: Error, errorInfo: React.ErrorInfo) {
    console.error('Game error:', error, errorInfo);
    // Log to error tracking service
  }

  render() {
    if (this.state.hasError) {
      return <ErrorFallback error={this.state.error} />;
    }
    return this.props.children;
  }
}

// Socket error handling
socket.on('error', (error: { message: string; code: string }) => {
  if (error.code === 'AUTH_ERROR') {
    // Redirect to login
    logout();
  } else {
    // Show error message
    showNotification(error.message, 'error');
  }
});
```

### Performance Optimizations
```typescript
// Virtual scrolling for large lists
import { FixedSizeList } from 'react-window';

const RoomList: React.FC<{ rooms: GameRoom[] }> = ({ rooms }) => {
  const Row = ({ index, style }: { index: number; style: React.CSSProperties }) => (
    <div style={style}>
      <RoomCard room={rooms[index]} />
    </div>
  );

  return (
    <FixedSizeList
      height={600}
      itemCount={rooms.length}
      itemSize={100}
      width="100%"
    >
      {Row}
    </FixedSizeList>
  );
};

// Image lazy loading
const LazyCardImage: React.FC<{ src: string; alt: string }> = ({ src, alt }) => {
  const [isLoaded, setIsLoaded] = useState(false);
  const imgRef = useRef<HTMLImageElement>(null);

  useEffect(() => {
    const observer = new IntersectionObserver(([entry]) => {
      if (entry.isIntersecting) {
        setIsLoaded(true);
        observer.disconnect();
      }
    });

    if (imgRef.current) {
      observer.observe(imgRef.current);
    }

    return () => observer.disconnect();
  }, []);

  return (
    <img
      ref={imgRef}
      src={isLoaded ? src : '/placeholder.png'}
      alt={alt}
      loading="lazy"
    />
  );
};
```

### Security Implementation
```typescript
// Validate actions on client (server validates too)
const validateAction = (action: PlayerAction, gameState: GameState): boolean => {
  const player = gameState.activePlayers.find(p => p.id === action.playerId);
  if (!player || !player.isTurn) return false;

  switch (action.action) {
    case 'raise':
      if (!action.amount || action.amount < gameState.minimumRaise) return false;
      if (action.amount > player.chips) return false;
      break;
    case 'call':
      if (player.chips < gameState.currentBet) return false;
      break;
    // ... other validations
  }

  return true;
};

// Secure token storage
const setAuthToken = (token: string) => {
  localStorage.setItem('auth_token', token);
  // Set token in axios default headers
  axios.defaults.headers.common['Authorization'] = `Bearer ${token}`;
};
```

