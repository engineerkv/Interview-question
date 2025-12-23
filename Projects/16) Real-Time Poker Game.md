# 1) Problem Statement

Design and implement a real-time multiplayer poker game that addresses the following challenges:

- **Core Functionality**: Enable multiple players to join tables, play poker with synchronized game state, and handle player actions in real-time
- **Scale Requirements**: Support thousands of concurrent game tables, millions of players, real-time synchronization across all players
- **Performance**: Minimal latency for game state synchronization, smooth animations (60fps), fast player action processing
- **Game State Synchronization**: Synchronize game state across all players with minimal latency, handle player actions (bet, call, raise, fold) in real-time
- **Game Logic**: Manage game logic and rules validation, prevent cheating through server-side validation, handle hand rankings and winner determination
- **Player Management**: Handle player disconnections gracefully, support reconnection to active games, manage player turn order
- **Real-time Features**: Real-time card dealing, live betting updates, real-time pot updates, player status updates, chat functionality
- **Data Consistency**: Ensure fair gameplay, maintain game state consistency, handle network latency, prevent race conditions

---

# 2) High Level Design (HLD)

## a) Functional Requirements

#### User Management

- User registration and authentication (Email, Social Login)

- User profile management

- Avatar and username customization

- User statistics (games played, wins, losses)

- Leaderboard rankings

#### Game Rooms & Lobby

- Create private game rooms

- Join public game rooms

- Room capacity management (2-9 players)

- Room settings (blinds, buy-in, game type)

- Lobby with available rooms

- Room search and filtering

#### Gameplay

- Texas Hold'em poker rules

- Multiple game variants (No-Limit, Pot-Limit, Fixed-Limit)

- Betting rounds (Pre-flop, Flop, Turn, River)

- Player actions (Fold, Check, Call, Raise, All-in)

- Hand rankings and winner determination

- Side pot calculation for all-in scenarios

- Time limits for player actions

- Turn indicators and action prompts

#### Real-time Features

- Real-time card dealing

- Live betting updates

- Real-time pot updates

- Player status updates (active, folded, all-in)

- Chat functionality during games

- Spectator mode for completed hands

#### Game State Management

- Game session persistence

- Reconnection to active games

- Hand history and replay

- Game statistics tracking

- Tournament support (future)

#### Animations & UI/UX

- Card dealing animations

- Chip betting animations

- Card flip animations

- Pot animation updates

- Smooth transitions between game states

- Loading states and progress indicators

- Responsive design for different screen sizes

#### Social Features

- Friend system

- Private messaging

- Game invitations

- Spectator viewing

- Emoji reactions

---

## b) Non-Functional Requirements

- **Performance:** Fast page loads (< 2 seconds), 60fps animations, smooth gameplay
- **Real-time Communication:** < 100ms message delivery, automatic reconnection
- **Scalability:** Support thousands of concurrent game rooms
- **Security:** Secure authentication, server-side validation, anti-cheating
- **User Experience:** Responsive design, accessible, intuitive interface

---

## c) MVP (Minimum Viable Product)

**Phase 1: Core Features (Must Have)**

- User registration and authentication
- Create and join game rooms
- Basic poker gameplay (Texas Hold'em)
- Real-time game synchronization
- Basic UI with card animations

**Phase 2: Enhanced Features**

- Advanced game variants
- Tournament support
- Social features (friends, chat)
- Spectator mode
- Hand history and replay

---

## d) Technology Choices

### Frontend Framework

- **React 19** - Latest React version with useOptimistic, useActionState, useTransition, useDeferredValue, and use() hook
- **TypeScript** - Type safety and better developer experience - Component-based UI framework

### State Management

- **React Query (TanStack Query)** - Server state for game rooms, player data
- **Context API with useReducer** - Complex game state management
- **Redux Toolkit** (optional) - Global UI state

### Real-time Communication

- **Socket.io Client** - Real-time game synchronization

### Animation

- **Framer Motion** - Smooth card and chip animations

### UI/UX Libraries

- **React Router** - Client-side routing
- **React Hot Toast** - Toast notifications

### Build Tools

- **Vite** - Fast build tool

### Testing

- **React Testing Library** - Component testing
- **Vitest** - Unit testing
- **Playwright** - E2E testing

### Deployment

- **Vercel/Netlify** - Static site hosting
- **AWS S3 + CloudFront** - Alternative deployment

**Trade-offs:**

- **Context API vs Redux**: Context API works well for game state, Redux for complex global state
- **Framer Motion**: Essential for smooth animations but adds bundle size

---

## e) Architecture Overview

The frontend follows a layered architecture optimized for real-time game synchronization.

**Component Structure:**

```

Frontend Application
├── Presentation Layer
│   ├── UI Components (Card, ChipStack, PlayerAvatar, ActionButton)
│   ├── Feature Components (GameTable, PlayerPanel, ActionPanel, ChatPanel)
│   └── Layout Components (Header, Sidebar, Navigation, MainLayout)
├── Business/Controller Layer
│   ├── Business Logic (Game rules validation, hand evaluation, betting validation)
│   ├── Custom Hooks (useGameState, usePlayerAction, useGameRoom)
│   └── Service Functions (Hand evaluation, betting calculations)
├── State Management
│   ├── Client State
│   │   ├── Context API with useReducer - Complex game state (game phase, player actions, cards, pot)
│   │   ├── Local State (useState) - UI state (modals, selected actions, animations)
│   │   └── Global State (Redux Toolkit) - User preferences, lobby state
│   └── Server State
│       ├── React Query - Game room data, player profiles, hand history
│       └── Socket.io - Real-time game state updates, player actions
├── WebSocket Layer
│   ├── Socket.io Client (WebSocket connection for real-time game updates)
│   ├── Event Handlers (Game state update, player action, turn change)
│   └── Connection Management (Auto-reconnect, heartbeat, connection state)
├── Socket.io Integration
│   ├── Socket.io Client (Primary communication for real-time game operations)
│   ├── Event Handlers (Handle incoming game events)
│   ├── Event Emitters (Send player actions and chat messages)
│   └── Connection Management (Auto-reconnect, heartbeat, error handling)
├── REST API Integration (Limited use)
│   ├── API Client (Axios) - Only for non-real-time operations
│   ├── API Services (playerService for profiles, handHistoryService)
│   └── Use Cases: Fetch player profiles, hand history, room list (initial load)
└── Routing
    ├── Public Routes (Home, Lobby)
    ├── Protected Routes (Game, Profile)
    └── Route Guards (Authentication checks)

```

**Frontend Deployment:**

- **Build**: Production bundle with code splitting using Vite
- **CDN**: Static assets served from CDN edge locations
- **Caching**: Aggressive caching for static assets, cache-busting for updates
- **Environment**: Environment variables for API endpoints and WebSocket URLs

**Key Frontend Components:**

- **React 19 Application**:
  - Single-page application with client-side routing
  - Component-based architecture for reusability
  - React Query with React 19 hooks (useOptimistic, useTransition, useDeferredValue)
  - Real-time game synchronization via Socket.io
  - Game animations with Framer Motion
  - Responsive design for mobile and desktop
  - Modern React 19 features for better performance and UX

- **CDN/Edge**:
  - Global distribution of static assets
  - Edge caching for improved performance
  - DDoS protection and rate limiting at edge

**Trade-offs:**

- **Context API for Game State**: Works well for complex game state but can cause re-renders - use memoization
- **Socket.io for Real-time**: Essential for multiplayer games, requires reconnection handling
- **Framer Motion**: Adds bundle size but essential for game feel

---

## f) App Flow

### Complete System Flow (Frontend Perspective)

**Primary User Flow - Joining Game and Playing:**

1. **User opens lobby** → LobbyPage displays available game rooms with React Query useSuspenseQuery (React 19)
2. **User joins room** → JoinRoomButton triggers useOptimistic (React 19) for instant room join
3. **Game room loads** → GameTable component renders with player positions
4. **Game starts** → WebSocket connection established, cards dealt
5. **User's turn** → ActionPanel shows available actions (fold, check, call, raise, all-in)
6. **User makes action** → ActionButton triggers useActionState (React 19) for action submission
7. **Optimistic update** → useOptimistic (React 19) shows action immediately
8. **Real-time sync** → WebSocket broadcasts action to all players
9. **Game state update** → GameTable updates with new pot, player chips, next turn

**Component Interaction Flow:**

```
User Joins → LobbyPage (React Query useSuspenseQuery)
            ↓
Room Selected → GameTable (WebSocket connection)
            ↓
Game Starts → Cards Dealt (WebSocket event)
            ↓
User Action → ActionPanel (useActionState for form)
            ↓
Action Sent → useOptimistic (instant UI)
            ↓
WebSocket Update → All Players (real-time sync)
            ↓
Game State → GameTable (updates pot, chips, turn)
```

**State Update Flow:**

1. **Local State** → Action selection, modal visibility use useState
2. **Optimistic State** → useOptimistic (React 19) shows actions immediately
3. **Game State** → Context API with useReducer manages game state (cards, pot, turn)
4. **Server State** → React Query manages game rooms, player profiles, hand history
5. **Real-time State** → WebSocket updates game state, player actions, turn changes
6. **Global State** → Redux Toolkit manages user preferences, lobby state
7. **Component Re-render** → React updates UI based on state changes

**Real-time Game Synchronization Flow:**

1. **WebSocket connection** → Socket.io client establishes connection on game join
2. **Game state received** → WebSocket event handler updates game state
3. **Optimistic action** → useOptimistic (React 19) shows user action immediately
4. **Server confirmation** → WebSocket receives server-confirmed game state
5. **State sync** → Game state synchronized across all players
6. **UI update** → GameTable, PlayerPanel, ActionPanel update with new state
7. **Animation** → Framer Motion animates card dealing, chip movements

**Error Handling Flow:**

1. **Socket.io Error** → Socket.io `error` event received
2. **Error Boundary** → Catches component errors, shows fallback UI
3. **User Feedback** → Toast notification displays error message
4. **Reconnection Logic** → Socket.io automatically retries connection with exponential backoff
5. **Game State Sync** → On reconnection, request current game state from server

**Hand History Flow:**

1. **User navigates** → React Router navigates to /history
2. **Data Fetching** → React Query useQuery fetches hand history (non-real-time)
3. **Loading State** → Skeleton screens displayed while loading
4. **Data Display** → HandHistoryList renders past hands
5. **User Interactions** → Filters update query params, trigger refetch

# 3) Component Architecture

Think of the frontend as a tree of React components - each component handles a specific part of the UI, and they work together to create the complete user experience.

**Component Hierarchy:**

```

App
├── Layout
│   ├── Header
│   │   ├── Logo
│   │   ├── Navigation
│   │   └── UserMenu
│   ├── MainContent
│   └── Footer
├── Pages
│   ├── LobbyPage
│   │   ├── RoomList
│   │   │   └── RoomCard
│   │   └── CreateRoomButton
│   ├── GamePage
│   │   ├── GameTable
│   │   │   ├── PlayerSeat
│   │   │   │   ├── PlayerAvatar
│   │   │   │   ├── ChipStack
│   │   │   │   └── PlayerCards
│   │   │   ├── CommunityCards
│   │   │   └── PotDisplay
│   │   ├── ActionPanel
│   │   │   ├── FoldButton
│   │   │   ├── CheckButton
│   │   │   ├── CallButton
│   │   │   ├── RaiseButton
│   │   │   └── AllInButton
│   │   └── ChatPanel
│   └── HandHistoryPage
│       └── HandHistoryList
└── SharedComponents
    ├── Button
    ├── Input
    ├── Card
    ├── Toast
    └── LoadingSpinner
```

**Key React Components:**

**1. GameTable Component:**

- Displays game table with player positions
- Shows community cards, pot, and betting information
- Handles card animations with Framer Motion
- Updates in real-time via WebSocket
- Uses useTransition (React 19) for non-urgent updates

**2. ActionPanel Component:**

- Displays available actions based on game state
- Handles user action selection (fold, check, call, raise, all-in)
- Uses useActionState (React 19) for action submission
- Shows betting amount input for raise action
- Disables actions when not user's turn

**3. PlayerSeat Component:**

- Displays player information (avatar, chips, status)
- Shows player cards (face up for user, face down for others)
- Indicates active player and dealer button
- Updates player status (active, folded, all-in)
- Animates chip movements with Framer Motion

**4. LobbyPage Component:**

- Displays available game rooms
- Fetches rooms with React Query useSuspenseQuery (React 19)
- Allows creating and joining rooms
- Uses useOptimistic (React 19) for instant room join
- Filters rooms by game type, blinds, players

**5. ChatPanel Component:**

- Displays game chat messages
- Handles sending chat messages
- Uses useOptimistic (React 19) for instant message display
- Updates in real-time via WebSocket
- Shows typing indicators

**Component Communication:**

- **Props** → Parent to child data flow
- **Callbacks** → Child to parent communication
- **Context API** → Shared game state (cards, pot, turn, players)
- **React Query** → Server state management (rooms, player profiles, hand history)
- **Redux Toolkit** → Global client state (user preferences, lobby state)
- **WebSocket** → Real-time game state updates, player actions

# 4) Data Models

### TypeScript Interfaces

```typescript
interface GameRoom {
  id: string;
  name: string;
  gameType: "no-limit" | "pot-limit" | "fixed-limit";
  smallBlind: number;
  bigBlind: number;
  buyIn: number;
  maxPlayers: number;
  currentPlayers: number;
  status: "waiting" | "active" | "finished";
}

interface GameState {
  roomId: string;
  phase: "pre-flop" | "flop" | "turn" | "river" | "showdown" | "finished";
  players: Player[];
  communityCards: Card[];
  pot: number;
  currentBet: number;
  dealerPosition: number;
  currentPlayerPosition: number;
  activePlayers: number;
}

interface Player {
  id: string;
  username: string;
  avatar: string;
  position: number;
  chips: number;
  hand: Card[];
  status: "active" | "folded" | "all-in" | "sitting-out";
  currentBet: number;
  isDealer: boolean;
  isSmallBlind: boolean;
  isBigBlind: boolean;
  isCurrentPlayer: boolean;
}

interface Card {
  suit: "hearts" | "diamonds" | "clubs" | "spades";
  rank: "2" | "3" | "4" | "5" | "6" | "7" | "8" | "9" | "10" | "J" | "Q" | "K" | "A";
}

interface PlayerAction {
  playerId: string;
  action: "fold" | "check" | "call" | "raise" | "all-in";
  amount?: number;
  timestamp: string;
}

interface HandHistory {
  id: string;
  roomId: string;
  players: Player[];
  communityCards: Card[];
  winner: Player;
  pot: number;
  actions: PlayerAction[];
  finishedAt: string;
}

interface FormState {
  action: "fold" | "check" | "call" | "raise" | "all-in";
  raiseAmount: number;
  errors: {
    action?: string;
    raiseAmount?: string;
  };
}
```

# 5) API Design

### Socket.io Events (Real-time Communication)

**Client → Server Events:**

#### `join-room`

- **Event:** `join-room`
- **Description:** Join a game room
- **Payload:**

```json
{
  "roomId": "room_abc123",
  "userId": "user_xyz789"
}
```

- **Server Response:** `room-joined` event with game state

#### `player-action`

- **Event:** `player-action`
- **Description:** Send player action (fold, check, call, raise, all-in)
- **Payload:**

```json
{
  "roomId": "room_abc123",
  "playerId": "user_xyz789",
  "action": "raise",
  "amount": 100
}
```

- **Server Response:** `game-state-update` event with updated game state

#### `send-chat`

- **Event:** `send-chat`
- **Description:** Send chat message
- **Payload:**

```json
{
  "roomId": "room_abc123",
  "playerId": "user_xyz789",
  "message": "Good hand!"
}
```

- **Server Response:** `chat-message` event broadcast to all players

#### `create-room`

- **Event:** `create-room`
- **Description:** Create a new game room
- **Payload:**

```json
{
  "name": "High Stakes Table",
  "gameType": "no-limit",
  "smallBlind": 10,
  "bigBlind": 20,
  "buyIn": 1000,
  "maxPlayers": 6
}
```

- **Server Response:** `room-created` event with room details

**Server → Client Events:**

#### `game-state-update`

- **Event:** `game-state-update`
- **Description:** Broadcast game state updates to all players
- **Payload:**

```json
{
  "gameState": {
    "phase": "flop",
    "players": [...],
    "communityCards": [...],
    "pot": 150,
    "currentBet": 20,
    "currentPlayerPosition": 2
  }
}
```

#### `player-action-received`

- **Event:** `player-action-received`
- **Description:** Confirm player action was received
- **Payload:**

```json
{
  "playerId": "user_xyz789",
  "action": "raise",
  "amount": 100,
  "timestamp": "2024-01-15T10:30:00Z"
}
```

#### `room-joined`

- **Event:** `room-joined`
- **Description:** Confirm player joined room
- **Payload:**

```json
{
  "roomId": "room_abc123",
  "gameState": {...},
  "players": [...]
}
```

#### `chat-message`

- **Event:** `chat-message`
- **Description:** Broadcast chat message to all players
- **Payload:**

```json
{
  "playerId": "user_xyz789",
  "username": "Player1",
  "message": "Good hand!",
  "timestamp": "2024-01-15T10:30:00Z"
}
```

#### `error`

- **Event:** `error`
- **Description:** Error notification
- **Payload:**

```json
{
  "code": "INVALID_ACTION",
  "message": "Invalid action for current game state"
}
```

---

# 6) Protocols

### WebSocket/Socket.io Protocol

**Connection:**

- **Protocol:** WebSocket (upgraded from HTTP)
- **Library:** Socket.io Client
- **Connection URL:** `ws://api.example.com` or `wss://api.example.com` (secure)
- **Authentication:** Token passed in connection query or auth event

**Event-Based Communication:**

- **Bidirectional:** Client and server can emit events
- **Real-time:** Low latency (< 100ms)
- **Automatic Reconnection:** Socket.io handles reconnection automatically
- **Room Support:** Join/leave rooms for targeted messaging

**Event Format:**

- **Client Emit:** `socket.emit('event-name', payload)`
- **Server Emit:** `socket.on('event-name', callback)`
- **Broadcast:** `socket.broadcast.to('room').emit('event-name', payload)`

**Connection Management:**

- **Heartbeat:** Automatic ping/pong to keep connection alive
- **Reconnection:** Exponential backoff on disconnection
- **Connection State:** Track connection status (connecting, connected, disconnected)

## iii) Implementation Details

### Business/Controller Layer

**Custom Hooks:**

- Encapsulate business logic and API calls
- Example: `useGameState`, `usePlayerAction`, `useGameRoom`, `useChat`
- Handle data transformation and validation

**Service Functions:**

- Pure functions for data processing and validation
- Hand evaluation, betting calculations, game rules validation
- Reusable across components

### Advanced Component Patterns

**Compound Components:**

- Group related components together (e.g., Form.Input, Form.Button)
- Share implicit state between components

**Render Props Pattern:**

- Pass render functions as props for flexible component composition

**Custom Hooks Pattern:**

- Extract reusable logic into custom hooks
- Example: `useSocket`, `useGameState`, `usePlayerAction`

**Higher-Order Components (HOCs):**

- Wrap components with additional functionality
- Example: `withAuth`, `withLoading`

### Performance Optimizations

- **Code splitting** with React.lazy() and Suspense
- **Memoization** with useMemo() and useCallback()
- **Virtual scrolling** for long lists (react-window, react-virtuoso)
- **Image optimization** and lazy loading
- **Debouncing and throttling** for user inputs
- **React.memo** for preventing unnecessary re-renders

### UI/UX Enhancements

- **Toast notifications** for user feedback (react-hot-toast)
- **Loading states** and skeleton screens
- **Error boundaries** for error handling
- **Responsive design** for mobile and desktop
- **Accessibility features** (ARIA labels, keyboard navigation, focus management)
- **Animations** with Framer Motion or CSS transitions

### Code Examples

**Custom Hook Example:**

```typescript
**Custom Hook: usePlayerAction (React 19)**
```typescript

import { useOptimistic, useTransition, useActionState } from 'react';
import { useMutation } from '@tanstack/react-query';
import { useSocket } from './useSocket';

function usePlayerAction(gameId: string) {
  const socket = useSocket();
  const [optimisticActions, addOptimisticAction] = useOptimistic(
    [] as PlayerAction[],
    (currentActions, newAction: PlayerAction) => [...currentActions, newAction]
  );
  const [isPending, startTransition] = useTransition();

  const [formState, formAction, isFormPending] = useActionState(
    async (prevState: FormState, formData: FormData) => {
      const action = formData.get('action') as string;
      const amount = formData.get('amount') ? Number(formData.get('amount')) : undefined;

      const playerAction: PlayerAction = {
        playerId: currentUser.id,
        action: action as any,
        amount,
        timestamp: new Date().toISOString()
      };

      addOptimisticAction(playerAction);
      socket.emit('player-action', { gameId, action: playerAction });

      return { ...prevState, errors: {} };
    },
    { action: 'fold', raiseAmount: 0, errors: {} }
  );

  return { formState, formAction, isFormPending, optimisticActions };
}

```

**Component with React Query (React 19):**
```typescript

function ActionPanel({ gameState }: { gameState: GameState }) {
  const { formState, formAction, isFormPending } = usePlayerAction(gameState.roomId);
  const [isPending, startTransition] = useTransition();

  const isMyTurn = gameState.currentPlayerPosition === myPlayerPosition;

  return (
    <form action={formAction}>
      {isMyTurn && (
        <>
          <button type="submit" name="action" value="fold" disabled={isFormPending}>
            Fold
          </button>
          <button type="submit" name="action" value="check" disabled={isFormPending}>
            Check
          </button>
          <button type="submit" name="action" value="call" disabled={isFormPending}>
            Call {gameState.currentBet}
          </button>
          <button type="submit" name="action" value="raise" disabled={isFormPending}>
            Raise
          </button>
          <input type="number" name="amount" placeholder="Raise amount" />
        </>
      )}
    </form>
  );
}

```

# 7) Low Level Design (LLD)

## ii) State Management

### Client State

**Local State (useState):**
- Component-specific UI state (form inputs, modal visibility, loading states)
- Example: `const [isOpen, setIsOpen] = useState(false);`

**Global State:**
- Redux Toolkit OR Zustand for complex global state
- Context API for user authentication, theme preferences
- Example: User preferences, app configuration

### Server State

**React Query (TanStack Query):**
- `useQuery` for non-real-time data (initial room list, player profiles, hand history)
- Limited use - most operations use Socket.io for real-time updates
- Automatic refetching, background updates
- Example: Fetch room list on lobby load, fetch hand history, player profiles

## iii) Implementation Details

### Business/Controller Layer

**Custom Hooks:**
- Encapsulate business logic and API calls
- Example: `useGameState`, `usePlayerAction`, `useGameRoom`, `useChat`
- Handle data transformation and validation

**Service Functions:**
- Pure functions for data processing and validation
- Hand evaluation, betting calculations, game rules validation

### Performance Optimizations

- Code splitting with React.lazy()
- Memoization with useMemo() and useCallback()
- Virtual scrolling for long lists
- Image optimization and lazy loading
- Debouncing and throttling for user inputs

### UI/UX Enhancements

- Toast notifications for user feedback
- Loading states and skeleton screens
- Error boundaries for error handling
- Responsive design for mobile and desktop
  - Modern React 19 features for better performance and UX
- Accessibility features (ARIA labels, keyboard navigation)

## iv) Testing

### Component Testing

- React Testing Library for component tests
- Test user interactions and component behavior
- Example: Test form submission, button clicks, input validation

### Integration Testing

- Test component interactions
- Test API integration with mock data
- Test state management flows

### E2E Testing

- Playwright or Cypress for end-to-end tests
- Test complete user flows
- Example: Test Real-Time Poker Game flow from start to finish

# 8) Algorithms

### Frontend Algorithms

**URL Validation Algorithm:**

```javascript

function isValidUrl(url) {
  try {
    new URL(url);
    return url.startsWith("http://") || url.startsWith("https://");
  } catch {
    return false;
  }
}

```

**Debouncing Algorithm:**

```javascript

function debounce(func, delay) {
  let timeoutId;
  return (...args) => {
    clearTimeout(timeoutId);
    timeoutId = setTimeout(() => func(...args), delay);
  };
}

```

# 9) Security

### Frontend Security

**Input Validation:**

- Client-side validation before action submission
- Sanitize user input to prevent XSS attacks
- Validate betting amounts, action types, game rules

**XSS Prevention:**

- React automatically escapes content
- Use `dangerouslySetInnerHTML` only when necessary with sanitization
- Content Security Policy (CSP) headers

**CSRF Protection:**

- SameSite cookies for authentication
- CSRF tokens for state-changing operations
- Verify origin header on API requests

**Secure Storage:**

- Never store sensitive data in localStorage
- Use httpOnly cookies for authentication tokens
- Clear sensitive data on logout

**Secure WebSocket:**

- Use WSS (WebSocket Secure) in production
- Enforce secure WebSocket connections
- Validate WebSocket origin to prevent unauthorized connections

**Rate Limiting (Client-Side):**

- Throttle Socket.io events to prevent abuse
- Show user-friendly messages when rate limited
- Implement exponential backoff for reconnection
- Validate actions client-side before sending

# 10) Deployment and DevOps

### Frontend Deployment

**Build Optimization:**

- Production build with code splitting and tree shaking
- Minification and compression
- Asset optimization (images, fonts)
- Environment variables for API endpoints

**CI/CD Pipeline:**

- Automated testing on pull requests
- Build and deploy on merge to main
- Preview deployments for feature branches
- Rollback capabilities

**Deployment Platforms:**

- Vercel / Netlify for static site hosting with CDN
- AWS S3 + CloudFront for alternative deployment
- GitHub Pages for simple static sites

**Monitoring:**

- Error tracking (Sentry, LogRocket)
- Performance monitoring (Web Vitals)
- Analytics (user behavior, page views)

# 11) Interview Answers (Frontend Focus)

### Q: How would you handle state management for this system?

**Answer (STAR Method):**

**Situation:** In a real-time poker game, we need to manage game state (cards, pot, turn, player actions), real-time synchronization, and UI state efficiently.

**Action:**
- Use Context API with useReducer for complex game state (cards, pot, turn, players) - single source of truth
- Use Socket.io for all real-time game operations (player actions, game state updates, chat) - primary communication method
- Use React Query only for non-real-time data (initial room list, player profiles, hand history) - handles caching, refetching
- Use `useOptimistic()` (React 19) for instant player action display before server confirmation via Socket.io
- Use `useActionState()` (React 19) for action form handling
- Use Redux Toolkit for global client state (user preferences, lobby state)
- Use useState for local component state (modal visibility, animations)

**Result:** Real-time game synchronization via Socket.io, reduced server load, improved performance, better user experience with instant action feedback.

**Takeaway:** Context API with useReducer is perfect for complex game state, combined with React 19's optimistic updates and WebSocket for real-time sync provides seamless poker game experience.

### Q: How would you implement real-time game synchronization?

**Answer (STAR Method):**

**Situation:** Multiple players need to see game state updates (cards, bets, pot) in real-time with minimal latency.

**Action:**
- Use WebSocket (Socket.io) for real-time bidirectional communication
- Use `useOptimistic()` (React 19) to show player actions immediately before server confirmation
- Use `useTransition()` (React 19) for non-urgent UI updates (animations, card flips)
- Implement connection retry logic with exponential backoff
- Show connection status indicator
- Handle reconnection to active games gracefully
- Sync game state on reconnection

**Result:** Game state synchronized in < 100ms, instant UI feedback, smooth gameplay, reliable real-time delivery.

**Takeaway:** WebSocket combined with React 19's optimistic updates provides the best real-time game synchronization for multiplayer poker.
