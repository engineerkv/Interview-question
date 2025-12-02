# Real-Time Poker Game - Low Level Design (LLD)

> **Project Type:** Full-Stack Web Application (MERN Stack)  
> **Tech Stack:** 
> - **Frontend:** React.js, TypeScript, React Router, Socket.io Client, Framer Motion, Material-UI
> - **Backend:** Node.js, Express.js, MongoDB, Redis, Socket.io Server, JWT

---

## 3. Component Architecture

**Think of this as the building blocks - how components are organized and connected**

### Component Hierarchy (React.js)

```
App (Root Component - Entry Point)
├── Layout (Main Layout with Navigation)
│   ├── Header
│   │   ├── Logo
│   │   ├── UserMenu
│   │   └── CreateRoomButton
│   └── Main Content Area
│       ├── LandingPage
│       ├── LoginPage
│       │   └── LoginForm
│       │       ├── EmailInput
│       │       ├── PasswordInput
│       │       └── SubmitButton
│       ├── LobbyPage
│       │   ├── SearchBar
│       │   ├── FilterBar
│       │   │   ├── StatusFilter
│       │   │   └── TypeFilter
│       │   ├── RoomList
│       │   │   └── RoomCard
│       │   │       ├── RoomInfo
│       │   │       │   ├── RoomName
│       │   │       │   ├── Blinds
│       │   │       │   └── BuyIn
│       │   │       ├── PlayerCount
│       │   │       └── JoinButton
│       │   └── CreateRoomModal
│       │       ├── RoomSettingsForm
│       │       └── CreateButton
│       ├── GameRoomPage (Main Game Interface)
│       │   ├── GameTable
│       │   │   ├── TableCanvas (SVG/Canvas for table graphics)
│       │   │   ├── PlayerSeats (6-9 seats around table)
│       │   │   │   └── PlayerSeat
│       │   │   │       ├── PlayerAvatar
│       │   │   │       ├── PlayerCards (animated card flip)
│       │   │   │       ├── PlayerChips
│       │   │   │       ├── PlayerStatus
│       │   │   │       │   ├── ActiveBadge
│       │   │   │       │   ├── FoldedBadge
│       │   │   │       │   └── AllInBadge
│       │   │   │       └── PlayerAction
│       │   │   ├── CommunityCards (Center of table)
│       │   │   │   └── Card (animated)
│       │   │   │       ├── CardFront
│       │   │   │       └── CardBack
│       │   │   ├── PotDisplay
│       │   │   │   ├── MainPot
│       │   │   │   └── SidePots
│       │   │   └── DealerButton (animated, moves around table)
│       │   ├── ActionPanel (Player's action buttons)
│       │   │   ├── ActionButtons
│       │   │   │   ├── FoldButton
│       │   │   │   ├── CheckButton
│       │   │   │   ├── CallButton
│       │   │   │   ├── RaiseButton
│       │   │   │   └── AllInButton
│       │   │   ├── BetSlider (Adjust bet amount)
│       │   │   │   ├── MinBet
│       │   │   │   ├── MaxBet
│       │   │   │   └── CurrentBet
│       │   │   └── TimerDisplay (Time left to act)
│       │   │       └── ProgressBar
│       │   ├── ChatPanel (collapsible side panel)
│       │   │   ├── ChatHeader
│       │   │   ├── ChatMessages
│       │   │   │   └── ChatMessage
│       │   │   │       ├── UserAvatar
│       │   │   │       ├── MessageText
│       │   │   │       └── Timestamp
│       │   │   └── ChatInput
│       │   └── HandHistory (modal overlay)
│       │       └── HandHistoryItem
│       ├── ProfilePage
│       │   ├── UserStats
│       │   │   ├── WinRate
│       │   │   ├── GamesPlayed
│       │   │   └── TotalWinnings
│       │   └── GameHistory
│       │       └── GameHistoryItem
│       ├── LeaderboardPage
│       │   ├── GlobalLeaderboard
│       │   └── TimePeriodFilter
│       └── SpectateGamePage (Read-only game view)
│           └── GameTable (Same as GameRoomPage but no actions)
├── GameProvider (Context API - Game State Management)
│   ├── GameState (Current game state - cards, pot, players)
│   ├── SocketConnection (WebSocket connection status)
│   └── GameActions (Functions to perform game actions)
└── ThemeProvider (Material-UI Theme)
    └── CustomTheme (Light/Dark mode, colors, typography)
```

**How components work together:**
- **App** is the root - wraps everything, provides context
- **Layout** provides structure - header, main content area
- **Pages** are top-level components - LobbyPage, GameRoomPage, ProfilePage
- **GameRoomPage** is the main game interface - has GameTable, ActionPanel, ChatPanel
- **GameTable** shows the poker table - PlayerSeats, CommunityCards, PotDisplay
- **ActionPanel** lets players act - buttons for Fold, Call, Raise, etc.
- **GameProvider** manages game state - connects to Socket.io, updates UI in real-time
- **ThemeProvider** manages styling - colors, fonts, dark/light mode

### Data Sharing Strategy

#### Global State (Context API + useReducer)
- **Game State:** Current game room, players, cards, pot, betting round, phase
- **User State:** Current user, authentication status, user stats
- **Socket State:** Connection status, room subscriptions, reconnection state
- **UI State:** Modals, notifications, loading states, theme

#### Local State (React useState/useReducer)
- **Form Inputs:** Login form, room creation form, chat input (React Hook Form)
- **UI State:** Modal visibility, dropdowns, tooltips, selected filters
- **Animation State:** Card flip states, chip animation states, transition states
- **Component-specific State:** Loading states, error states

#### Socket.io Events
- **Real-time Updates:** Game actions, player updates, card dealing
- **Room Events:** Player join/leave, room updates, room status changes
- **Chat Events:** New messages, typing indicators, user presence

#### Props Drilling
- **Simple Data:** Pass props for parent-child communication
- **Avoid Deep Nesting:** Use Context for deeply nested game components
- **Component Composition:** Use children props and render props pattern

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

**Note:** All API endpoints are implemented on the **backend (Node.js/Express)**, and the **frontend (React.js)** calls these APIs using Axios. Socket.io events are handled by **backend Socket.io server** and received by **frontend Socket.io client**.

### Authentication APIs

**Backend Implementation:** Express.js routes handle authentication logic  
**Frontend Implementation:** React components call these APIs and handle responses

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

## 8. Implementation Details

**Note:** Implementation details are split between frontend (React.js) and backend (Node.js/Express.js/Socket.io). Each section indicates where the code runs.

### Code Splitting with React.lazy

**Frontend Implementation:** React.js code splitting for faster initial load
```typescript
import { lazy, Suspense } from 'react';
import { Routes, Route } from 'react-router-dom';
import { CircularProgress, Box } from '@mui/material';

// Lazy load pages - only loads code when you visit that page, like opening one chapter of a book
const GameRoomPage = lazy(() => import('./pages/GameRoomPage'));
const LobbyPage = lazy(() => import('./pages/LobbyPage'));
const ProfilePage = lazy(() => import('./pages/ProfilePage'));
const LeaderboardPage = lazy(() => import('./pages/LeaderboardPage'));

// Loading fallback component
const LoadingFallback = () => (
  <Box display="flex" justifyContent="center" alignItems="center" minHeight="100vh">
    <CircularProgress />
  </Box>
);

// Route with Suspense
<Suspense fallback={<LoadingFallback />}>
  <Routes>
    <Route path="/game/:roomId" element={<GameRoomPage />} />
    <Route path="/lobby" element={<LobbyPage />} />
    <Route path="/profile" element={<ProfilePage />} />
    <Route path="/leaderboard" element={<LeaderboardPage />} />
  </Routes>
</Suspense>
```

### Socket.io Connection Management

**Frontend Implementation:** React.js Socket.io client connects to backend server  
**Backend Implementation:** Socket.io server handles connections and broadcasts

**Backend (Socket.io Server):**
```typescript
// Backend: Socket.io server - handles all WebSocket connections
```

**Frontend Implementation:**
```typescript
// Frontend: Socket connection setup - like a walkie-talkie connection, automatically reconnects if it drops
import { io, Socket } from 'socket.io-client';
import { createContext, useContext, useEffect, useState, useCallback } from 'react';

interface SocketContextType {
  socket: Socket | null;
  isConnected: boolean;
  joinRoom: (roomId: string) => void;
  leaveRoom: (roomId: string) => void;
}

const SocketContext = createContext<SocketContextType | null>(null);

export const SocketProvider: React.FC<{ children: React.ReactNode }> = ({ children }) => {
  const [socket, setSocket] = useState<Socket | null>(null);
  const [isConnected, setIsConnected] = useState(false);

  useEffect(() => {
    const token = localStorage.getItem('auth_token');
    const newSocket = io(process.env.REACT_APP_SOCKET_URL!, {
      auth: {
        token
      },
      transports: ['websocket'],
      reconnection: true,
      reconnectionDelay: 1000,
      reconnectionAttempts: 5,
      timeout: 20000,
    });

    newSocket.on('connect', () => {
      console.log('Connected to server');
      setIsConnected(true);
    });

    newSocket.on('disconnect', (reason) => {
      console.log('Disconnected from server:', reason);
      setIsConnected(false);
    });

    newSocket.on('connect_error', (error) => {
      console.error('Connection error:', error);
      setIsConnected(false);
    });

    setSocket(newSocket);

    return () => {
      newSocket.close();
    };
  }, []);

  const joinRoom = useCallback((roomId: string) => {
    if (socket && isConnected) {
      socket.emit('join-room', roomId);
    }
  }, [socket, isConnected]);

  const leaveRoom = useCallback((roomId: string) => {
    if (socket && isConnected) {
      socket.emit('leave-room', roomId);
    }
  }, [socket, isConnected]);

  return (
    <SocketContext.Provider value={{ socket, isConnected, joinRoom, leaveRoom }}>
      {children}
    </SocketContext.Provider>
  );
};

export const useSocket = () => {
  const context = useContext(SocketContext);
  if (!context) {
    throw new Error('useSocket must be used within SocketProvider');
  }
  return context;
};
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

**Frontend Implementation:** React.js components use Framer Motion for animations
```typescript
import { motion, AnimatePresence } from 'framer-motion';
import { Box } from '@mui/material';

// Card component with flip animation - cards flip and slide smoothly, feels like real cards
const Card: React.FC<{ card: Card; delay?: number; isFlipping?: boolean }> = ({ 
  card, 
  delay = 0,
  isFlipping = false 
}) => {
  return (
    <motion.div
      initial={{ opacity: 0, scale: 0, rotateY: 180 }}
      animate={{ 
        opacity: 1, 
        scale: 1, 
        rotateY: isFlipping ? 0 : 180 
      }}
      transition={{ 
        duration: 0.5, 
        delay,
        ease: "easeInOut"
      }}
      style={{
        perspective: '1000px',
        transformStyle: 'preserve-3d',
      }}
      className="card"
    >
      <AnimatePresence mode="wait">
        {card.isVisible ? (
          <motion.img
            key="front"
            initial={{ rotateY: 180 }}
            animate={{ rotateY: 0 }}
            exit={{ rotateY: 180 }}
            src={`/cards/${card.suit}-${card.rank}.png`}
            alt={`${card.rank} of ${card.suit}`}
            style={{ width: '100%', height: '100%' }}
          />
        ) : (
          <motion.img
            key="back"
            initial={{ rotateY: 0 }}
            animate={{ rotateY: 180 }}
            exit={{ rotateY: 0 }}
            src="/cards/back.png"
            alt="Card back"
            style={{ width: '100%', height: '100%' }}
          />
        )}
      </AnimatePresence>
    </motion.div>
  );
};

// Chip animation with physics
const Chip: React.FC<{ 
  amount: number; 
  from: { x: number; y: number };
  to: { x: number; y: number };
  onComplete?: () => void;
}> = ({ amount, from, to, onComplete }) => {
  return (
    <motion.div
      initial={{ 
        x: from.x, 
        y: from.y, 
        scale: 0,
        opacity: 0
      }}
      animate={{ 
        x: to.x, 
        y: to.y, 
        scale: 1,
        opacity: 1
      }}
      exit={{
        scale: 0,
        opacity: 0
      }}
      transition={{ 
        duration: 0.6, 
        ease: "easeOut",
        type: "spring",
        stiffness: 200,
        damping: 20
      }}
      onAnimationComplete={onComplete}
      style={{
        position: 'absolute',
        zIndex: 1000,
      }}
      className="chip"
    >
      <Box
        sx={{
          width: 60,
          height: 60,
          borderRadius: '50%',
          backgroundColor: 'gold',
          display: 'flex',
          alignItems: 'center',
          justifyContent: 'center',
          fontWeight: 'bold',
          boxShadow: '0 4px 8px rgba(0,0,0,0.3)',
        }}
      >
        {amount}
      </Box>
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

**Frontend Optimizations:** React.js code splitting, lazy loading, memoization  
**Backend Optimizations:** Redis caching for game state, efficient database queries
```typescript
// Virtual scrolling - only renders what's visible, like a window showing part of a long list
import { FixedSizeList } from 'react-window';
import { memo } from 'react';

const RoomList: React.FC<{ rooms: GameRoom[] }> = ({ rooms }) => {
  const Row = memo(({ index, style }: { index: number; style: React.CSSProperties }) => (
    <div style={style}>
      <RoomCard room={rooms[index]} />
    </div>
  ));

  return (
    <FixedSizeList
      height={600}
      itemCount={rooms.length}
      itemSize={100}
      width="100%"
      overscanCount={5}
    >
      {Row}
    </FixedSizeList>
  );
};

// Image lazy loading - loads images as you scroll, like Instagram with Intersection Observer
const LazyCardImage: React.FC<{ src: string; alt: string }> = ({ src, alt }) => {
  const [isLoaded, setIsLoaded] = useState(false);
  const [isInView, setIsInView] = useState(false);
  const imgRef = useRef<HTMLImageElement>(null);

  useEffect(() => {
    const observer = new IntersectionObserver(
      ([entry]) => {
        if (entry.isIntersecting) {
          setIsInView(true);
          observer.disconnect();
        }
      },
      { rootMargin: '50px' }
    );

    if (imgRef.current) {
      observer.observe(imgRef.current);
    }

    return () => observer.disconnect();
  }, []);

  return (
    <img
      ref={imgRef}
      src={isInView ? src : '/placeholder.png'}
      alt={alt}
      loading="lazy"
      onLoad={() => setIsLoaded(true)}
      style={{
        opacity: isLoaded ? 1 : 0,
        transition: 'opacity 0.3s',
      }}
    />
  );
};

// Memoized expensive calculations - remembers result, recalculates only when inputs change
const HandRankDisplay: React.FC<{ cards: Card[] }> = ({ cards }) => {
  const handRank = useMemo(() => {
    return calculateHandRank(cards);
  }, [cards]);

  return <div>{handRank.description}</div>;
};

// Memoized components - remembers component output, skips re-render if props didn't change
const PlayerSeat = memo(({ player }: { player: Player }) => {
  return (
    <div className="player-seat">
      <PlayerAvatar player={player} />
      <PlayerCards cards={player.cards} />
      <PlayerChips chips={player.chips} />
    </div>
  );
}, (prevProps, nextProps) => {
  // Custom comparison function
  return prevProps.player.id === nextProps.player.id &&
         prevProps.player.chips === nextProps.player.chips &&
         prevProps.player.status === nextProps.player.status;
});
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

