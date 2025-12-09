# Real-Time Poker Game

> **Project Type:** Full-Stack Web Application (MERN Stack)
> **Frontend:** React.js Web Application
> **Backend:** Node.js, Express.js, MongoDB, Socket.io Server, REST APIs
> **Tech Stack:**
> - **Frontend:** React.js, TypeScript, React Router, Socket.io Client, Framer Motion, Material-UI
> - **Backend:** Node.js, Express.js, MongoDB, Redis, Socket.io Server, JWT
> **Key Features:** Real-time multiplayer, advanced animations, performance optimization

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

## a) Requirements

### i) Functional Requirements

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

### ii) Non-Functional Requirements

#### Performance

- **Web Application:** Optimized for desktop and mobile browsers (Chrome, Firefox, Safari, Edge)

- **Responsive Design:** Mobile-first adaptive layouts for all screen sizes

- **Fast Load Times:**
  - First Contentful Paint (FCP) < 1.0s
  - Largest Contentful Paint (LCP) < 2.0s
  - Time to Interactive (TTI) < 2.5s
  - Cumulative Layout Shift (CLS) < 0.1

- **Asset Optimization:**
  - Code splitting with React.lazy() and dynamic imports
  - Route-based code splitting
  - Image lazy loading for cards and avatars (WebP format)
  - CSS/JS minification and compression with Vite/Webpack
  - Bundle size optimization with tree shaking
  - Service Worker for asset caching

- **Animation Performance:**
  - 60fps animations with Framer Motion
  - GPU-accelerated CSS transforms
  - Reduced re-renders with React.memo and useMemo
  - Will-change CSS property for animation optimization

#### Real-time Communication

- **Low Latency:** < 100ms message delivery

- **Connection Stability:** Automatic reconnection

- **Scalability:** Support multiple concurrent game rooms

- **Message Reliability:** Ensure all game actions are received

#### Platform Support

- **Cross-browser:** Chrome, Firefox, Safari, Edge (latest 2 versions)

- **Device Compatibility:** Desktop, Tablet, Mobile (responsive design)

- **Internet Connectivity:** Handle connection drops gracefully with Socket.io reconnection

- **WebSocket Support:** Required for real-time features (Socket.io with fallback)

- **PWA Support:** Progressive Web App capabilities for app-like experience

#### Security

- **Authentication/Authorization:** Secure login and session management

- **Game Security:** Server-side validation of all game actions

- **Anti-cheating:** Prevent client-side manipulation

- **Data Encryption:** HTTPS/WSS for all communications

- **API Security:** Rate limiting, authentication tokens

#### Scalability

- **High Availability:** 99.9% uptime

- **Concurrent Users:** Support thousands of simultaneous players

- **Load Handling:** Handle peak traffic during tournaments

- **Database Optimization:** Efficient queries and indexing

- **Caching Strategy:** Redis for game state and session data

- **Load Balancing:** Distribute WebSocket connections

#### User Experience

- **Smooth Animations:** 60fps card and chip animations with Framer Motion

- **Responsive UI:** Instant feedback for user actions with optimistic updates

- **Error Handling:** Graceful error messages and recovery with React Error Boundaries

- **Offline Handling:** Show connection status indicator, handle reconnection

- **Push Notifications:** Browser push notifications for game invitations, turn reminders

- **Accessibility:**
  - Keyboard navigation (Tab, Enter, Arrow keys)
  - Screen reader support (ARIA labels)
  - WCAG 2.1 AA compliance
  - Focus management for modals and dialogs

#### Reliability

- **Error Handling:** Comprehensive error handling and recovery

- **Logging & Monitoring:** Real-time monitoring and error tracking

- **Game State Recovery:** Recover from connection issues

- **Testing:** Unit tests, integration tests, E2E tests

- **CI/CD Pipeline:** Automated testing and deployment

#### SEO & Marketing

- **SEO Optimization:** Meta tags, structured data

- **Analytics:** User behavior tracking and game analytics

- **A/B Testing:** Feature flagging for gradual rollouts

- **Versioning:** API versioning for backward compatibility

---

## b) Scope and Priority

### Phase 1: MVP (Must Have) - Priority 1

#### Functional

- **Core Gameplay:**
  - User registration and login
  - Create/join game rooms (2-6 players)
  - Texas Hold'em poker rules
  - Basic betting actions (Fold, Check, Call, Raise)
  - Hand ranking and winner determination
  - Real-time game updates via Socket.io

#### Non-Functional

- **Platform:** React.js Web application

- **Responsive:** Mobile-first responsive design

- **Performance:**
  - Core Web Vitals optimization
  - Code splitting with React.lazy() and route-based splitting
  - Advanced animations (card dealing, chip betting) with Framer Motion
  - Virtual scrolling for long lists
  - Memoization for expensive calculations

- **Rendering:** Client-side rendering (CSR) with React.js

- **Caching:**
  - Browser caching
  - Service Worker for offline support
  - React Query for API response caching

- **Security:**
  - Authentication with JWT tokens
  - HTTPS/WSS for all communications
  - Server-side validation of all game actions
  - XSS protection
  - CSRF protection

### Phase 2: Enhanced Features - Priority 2

#### Functional

- **Advanced Gameplay:**
  - All-in functionality
  - Side pot calculation
  - Time limits for actions
  - Hand history
  - Spectator mode

- **Social Features:**
  - Chat functionality
  - Friend system
  - Private messaging

- **UI Enhancements:**
  - Advanced animations
  - Improved card animations
  - Better visual feedback

#### Non-Functional

- **Performance:** Advanced code splitting, reduced re-renders

- **Real-time:** Improved WebSocket handling, reconnection logic

- **Mobile:** Enhanced mobile experience

- **Analytics:** Game analytics and user tracking

### Phase 3: Advanced Features - Priority 3

#### Functional

- **Tournament Mode:**
  - Multi-table tournaments
  - Tournament brackets
  - Prize distribution

- **Advanced Features:**
  - Multiple game variants
  - Custom room settings
  - Advanced statistics
  - Replay system

#### Non-Functional

- **Scalability:** Advanced load balancing, horizontal scaling

- **Monitoring:** Real-time monitoring dashboards

- **A/B Testing:** Feature flagging system

- **PWA:** Progressive Web App support

---

## c) Technology Choices

### Frontend Framework

- **React.js:** Perfect for building interactive game interfaces
  - **Component-based:** Like building with LEGO blocks - each piece (component) does one thing well
  - **Virtual DOM:** React is smart - it only updates what actually changed, making animations smooth
  - **Hooks:** Modern way to manage state - useState for simple stuff, useReducer for complex game state
  - **Code splitting:** Load only what you need - game room code only loads when you join a game
  - **TypeScript:** Catches bugs before they happen - especially important for game logic

### TypeScript

- **TypeScript:** JavaScript with types - like having labels on boxes so you know what's inside
  - **Why use it?** Catches bugs before they happen - especially important for game logic
  - **Better IDE:** Autocomplete knows what properties exist - like having a smart assistant
  - **Self-documenting:** Types tell you what data looks like - easier to understand code

### Real-time Communication

- **Socket.io:** Like a walkie-talkie between browser and server - instant two-way communication
  - **Why Socket.io?** WebSocket with fallbacks - works even if WebSocket is blocked
  - **Room-based:** Players join a "room" - only people in that room get updates
  - **Auto-reconnect:** If connection drops, automatically reconnects - like your phone reconnecting to WiFi
  - **Event-based:** Server sends events like "card dealt" or "player folded" - app reacts instantly

### State Management

- **Context API + useReducer:** Built-in React solution - like a shared whiteboard for game state
  - **Why Context?** No external library needed - keeps bundle size small
  - **useReducer:** Perfect for game state - handles complex state updates (like betting rounds)
  - **Real-time friendly:** When Socket.io updates come in, just update the context - all components see it

- **Local State (useState):** For component-specific stuff - like "is modal open?" or "selected card"

- **React Query:** For REST API data - handles caching and refetching automatically

### API Communication

- **Axios:** HTTP client for REST APIs
  - Interceptors for auth tokens
  - Request/response transformation
  - Error handling
  - Request cancellation

### Animation Libraries

- **Framer Motion:** Makes animations smooth and easy - like having a professional animator
  - **Card dealing:** Cards flip and slide smoothly - feels like real cards
  - **Chip animations:** Chips move to pot with physics - looks natural
  - **Declarative:** Describe what you want ("card flips"), it handles the details
  - **60fps:** Smooth animations that don't lag - important for game feel

### UI Components & Styling

- **Material-UI (MUI) / Chakra UI:** Component library for React.js
  - Pre-built accessible components
  - Theming support with custom theme
  - Responsive grid system
  - Accessibility features (ARIA labels, keyboard navigation)

- **Styled Components / CSS Modules:** Component-scoped styling
  - Dynamic styling with props
  - Theme support
  - Better component isolation
  - CSS-in-JS for better component encapsulation

- **Tailwind CSS (Optional):** Utility-first CSS framework

### Build Tools

- **Webpack / Vite:** Module bundler
  - Code splitting
  - Hot module replacement
  - Asset optimization
  - Tree shaking

### Code Splitting & Lazy Loading

- **React.lazy():** Lazy load components
  - Reduce initial bundle size
  - Load components on demand
  - Better performance
  - Used with Suspense for loading states

- **Dynamic imports:** Code splitting at route level
  - Split by routes (React Router)
  - Split by features (game room, lobby, profile)
  - Split heavy components (game table, animations)

- **Route-based splitting:** Each route loaded on demand

### Testing

- **Jest:** Unit testing framework

- **React Testing Library:** Component testing

- **Cypress / Playwright:** E2E testing

### Development Tools

- **ESLint:** Code linting

- **Prettier:** Code formatting

- **TypeScript:** Type checking

- **React DevTools:** Debugging

### Backend Integration

- **REST APIs:** Backend communication
  - Standard REST endpoints
  - JSON data format
  - Authentication via JWT tokens

- **Socket.io Client:** Real-time communication
  - WebSocket connection
  - Room-based events
  - Automatic reconnection

---

## e) Architecture Overview

The system follows a real-time multiplayer poker game architecture with WebSocket synchronization, game state management, and distributed game processing. Here's how the complete system works:

### Frontend Architecture

**Frontend Layers:**

1. **Presentation Layer (React Components)**
   - **UI Components**: Reusable components (Card, Chip, PlayerSeat, PotDisplay, ActionButtons)
   - **Feature Components**: GameTable, Lobby, PlayerList, ChatPanel, HandHistory
   - **Layout Components**: Header, Sidebar, Navigation, MainLayout
   - **Page Components**: HomePage, LobbyPage, GamePage, ProfilePage

2. **State Management Layer**
   - **Local State (useState)**: Component-specific UI state (selected action, bet amount, loading, errors)
   - **Context API + useReducer**: Global state for game state, player state, room state
   - **WebSocket State**: Real-time game updates, player actions, game state synchronization

3. **Game Logic Layer**
   - **Client-side Validation**: Validate player actions before sending to server
   - **Optimistic Updates**: Update UI immediately, revert if server rejects
   - **Animation Triggers**: Trigger animations based on game state changes

4. **WebSocket Layer**
   - **Socket.io Client**: WebSocket connection for real-time game updates
   - **Event Handlers**: Game state update, player action, card dealing, pot update
   - **Connection Management**: Auto-reconnect, heartbeat, connection state

5. **Animation Layer**
   - **Framer Motion**: Smooth card dealing, chip betting, card flip animations
   - **Performance Optimization**: GPU-accelerated animations, 60fps target
   - **Animation Sequencing**: Coordinate multiple animations (cards, chips, pot)

6. **API Integration Layer**
   - **API Client**: Axios instance with interceptors for auth, error handling
   - **Redux Thunks**: Async actions for API operations (joinRoom, leaveRoom, getHistory)
   - **Request/Response Transformation**: Data normalization and error handling

7. **Routing Layer (React Router)**
   - **Route Configuration**: Define routes and protected routes
   - **Navigation**: Programmatic and declarative navigation
   - **Route Guards**: Authentication and authorization checks

8. **Build & Deployment Layer**
   - **Build Process**: Webpack/Vite bundling with code splitting
   - **Static Assets**: Served from CDN (CloudFront/Cloudflare)
   - **Environment Configuration**: Environment-specific API endpoints and WebSocket URLs

**Frontend Request Flow:**

1. **User Interaction** → User performs game action (bet, call, raise, fold)
2. **Client Validation** → Validate action locally
3. **Optimistic Update** → Update UI immediately
4. **WebSocket Send** → Send action to server via Socket.io
5. **Server Response** → Receive game state update from server
6. **State Update** → Update game state with server response
7. **Animation** → Trigger animations for game state changes
8. **UI Update** → Components re-render with new game state

### Backend Architecture

**Backend Layers:**

1. **WebSocket Server Layer** - Handles real-time WebSocket connections
2. **Load Balancer** - Distributes WebSocket and HTTP traffic with sticky sessions
3. **Game Engine Layer** - Server-side game logic and validation
4. **Room Management Layer** - Game room creation, joining, leaving
5. **Application Service Layer** - Business logic and orchestration
6. **Cache Layer** - In-memory caching for game state
7. **Database Layer** - Persistent data storage for game history
8. **Message Queue Layer** - Async processing for game events

### Complete Request Flow

**Player Action Flow:**
1. **Frontend**: Player performs action (bet, call, raise, fold)
2. **WebSocket**: Send action to server via Socket.io
3. **Game Engine**: Validate action (server-side validation)
4. **Game Logic**: Process action, update game state
5. **Broadcast**: Broadcast game state update to all players in room
6. **Frontend**: All players receive update, UI updates with animations

**Game State Synchronization Flow:**
1. **Game Engine**: Game state changes (card dealing, betting round)
2. **State Update**: Update game state in memory and cache
3. **Broadcast**: Broadcast state update to all players via WebSocket
4. **Frontend**: All players receive update simultaneously
5. **UI Update**: All players see synchronized game state

**Player Reconnection Flow:**
1. **Player Disconnects**: WebSocket connection lost
2. **Game State Persisted**: Save game state to database
3. **Player Reconnects**: New WebSocket connection established
4. **State Recovery**: Fetch current game state from database
5. **State Sync**: Send current game state to reconnected player
6. **UI Update**: Player sees current game state

### Key Components

- **Frontend (React.js)**: Single-page application with WebSocket integration, component-based architecture, Context API for state management, Framer Motion for animations, Socket.io client for real-time updates
- **WebSocket Servers**: Stateless servers handling WebSocket connections, game state synchronization, player action processing
- **Load Balancer**: Distributes WebSocket and HTTP traffic, sticky sessions for WebSocket connections
- **Game Engine**: Server-side game logic, poker rules validation, hand evaluation, winner determination
- **Room Management**: Game room creation, joining, leaving, capacity management
- **Application Services**: Game Service, Room Service, Player Service, Chat Service
- **Cache Layer (Redis)**: In-memory cache for active game states (20% of traffic), player sessions
- **Database (MongoDB)**: Sharded across multiple nodes for horizontal scaling, stores game history, player data, room data
- **Message Queue (RabbitMQ/Kafka)**: Async processing for game events, analytics, notifications

```

┌─────────────────────────────────────────────────────────┐
│              Frontend (React.js) - Client Side           │
│  (This is what users see in their browser)              │
├─────────────────────────────────────────────────────────┤
│  ┌──────────────────────────────────────────────────┐   │
│  │         Browser (Chrome, Firefox, Safari)        │   │
│  │  ┌────────────────────────────────────────────┐  │   │
│  │  │     React.js Application (SPA)             │  │   │
│  │  │  ┌──────────────────────────────────────┐  │  │   │
│  │  │  │  React Router (Client-side Routing)  │  │  │   │
│  │  │  └──────────────────────────────────────┘  │  │   │
│  │  │  ┌──────────────────────────────────────┐  │  │   │
│  │  │  │  Context API + useReducer (State)    │  │  │   │
│  │  │  │  - Game state, user state, UI state  │  │  │   │
│  │  │  └──────────────────────────────────────┘  │  │   │
│  │  │  ┌──────────────────────────────────────┐  │  │   │
│  │  │  │  Socket.io Client (Real-time)        │  │  │   │
│  │  │  │  - Receives game updates instantly   │  │  │   │
│  │  │  └──────────────────────────────────────┘  │  │   │
│  │  │  ┌──────────────────────────────────────┐  │  │   │
│  │  │  │  Framer Motion (Animations)          │  │  │   │
│  │  │  │  - Card animations, chip animations  │  │  │   │
│  │  │  └──────────────────────────────────────┘  │  │   │
│  │  │  ┌──────────────────────────────────────┐  │  │   │
│  │  │  │  Material-UI Components              │  │  │   │
│  │  │  └──────────────────────────────────────┘  │  │   │
│  │  └────────────────────────────────────────────┘  │   │
│  └──────────────────────────────────────────────────┘   │
└─────────────────────────────────────────────────────────┘
        │                                    │
        │ HTTP/REST API                     │ WebSocket
        │ (User data, room list)            │ (Game updates)
        ▼                                    ▼
┌─────────────────────────────────────────────────────────┐
│              Backend (Node.js + Express.js)              │
│  (Server that handles game logic and real-time updates) │
├─────────────────────────────────────────────────────────┤
│  ┌──────────────────────────────────────────────────┐   │
│  │         Load Balancer                            │   │
│  └──────────────────────────────────────────────────┘   │
│                        │                                 │
│        ┌───────────────┼───────────────┐                │
│        ▼               ▼               ▼                │
│  ┌──────────┐  ┌──────────┐  ┌──────────┐             │
│  │ Express  │  │ Express  │  │ Express  │             │
│  │ Server 1 │  │ Server 2 │  │ Server 3 │             │
│  └──────────┘  └──────────┘  └──────────┘             │
│        │               │               │                │
│        └───────────────┼───────────────┘                │
│                        ▼                                 │
│  ┌──────────────────────────────────────────────────┐   │
│  │         Socket.io Server (Real-time)             │   │
│  │  - Handles WebSocket connections                 │   │
│  │  - Manages game rooms                            │   │
│  │  - Broadcasts game updates                       │   │
│  └──────────────────────────────────────────────────┘   │
│                        ▼                                 │
│  ┌──────────────────────────────────────────────────┐   │
│  │         Game Engine (Backend)                    │   │
│  │  - Validates game actions                        │   │
│  │  - Calculates game state                         │   │
│  │  - Determines winners                            │   │
│  │  - Prevents cheating                             │   │
│  └──────────────────────────────────────────────────┘   │
│                        ▼                                 │
│  ┌──────────────────────────────────────────────────┐   │
│  │         Business Logic Layer                     │   │
│  │  - User Service (authentication, profiles)       │   │
│  │  - Room Service (create, join, leave rooms)      │   │
│  │  - Game Service (game state management)          │   │
│  │  - Stats Service (user statistics)               │   │
│  └──────────────────────────────────────────────────┘   │
│                        ▼                                 │
│  ┌──────────────────────────────────────────────────┐   │
│  │         Data Access Layer                        │   │
│  │  - MongoDB (User data, game history, stats)      │   │
│  │  - Redis (Active game state, sessions)           │   │
│  └──────────────────────────────────────────────────┘   │
└─────────────────────────────────────────────────────────┘
        │                    │
        ▼                    ▼
┌──────────────┐  ┌──────────────┐
│   MongoDB    │  │    Redis     │
│  (Database)  │  │   (Cache)    │
│              │  │              │
│  - Users     │  │  - Game      │
│  - Rooms     │  │    State     │
│  - Game      │  │  - Sessions  │
│    History   │  │              │
│  - Stats     │  │              │
└──────────────┘  └──────────────┘

```

**How it works:**

1. **Frontend (React.js):** User sees game UI, clicks buttons (fold, call, raise)

2. **Socket.io Client:** Sends game action to server via WebSocket - instant communication

3. **Backend Socket.io Server:** Receives action, validates it, processes game logic

4. **Game Engine (Backend):** Validates action, updates game state, determines if valid

5. **Broadcast Update:** Server broadcasts updated game state to all players in room

6. **Frontend Updates:** All players receive update, React updates UI, animations play

7. **Database:** Game history saved to MongoDB, active game state cached in Redis

---

## Key Design Decisions

1. **React.js for Web:** Perfect for interactive games - component-based, fast updates, great ecosystem
   - **Virtual DOM:** Only updates what changed - keeps animations smooth
   - **Hooks:** Clean way to manage game state and side effects

2. **Socket.io for Real-time:** Like a walkie-talkie - instant two-way communication
   - **Why not just WebSocket?** Socket.io has fallbacks and auto-reconnect - more reliable
   - **Room-based:** Players join a "room" - only that room gets updates

3. **Context API + useReducer for State:** Built-in React solution - no external library needed
   - **useReducer:** Perfect for game state - handles complex updates (betting rounds, card dealing)
   - **Real-time friendly:** Socket updates go to context, all components see changes instantly

4. **Framer Motion for Animations:** Makes animations smooth and easy
   - **Card dealing:** Cards flip and slide - feels like real cards
   - **60fps:** Smooth animations that don't lag - important for game feel

5. **Server-side Validation:** All game actions validated on server - prevents cheating
   - Client can't fake a win - server is the authority
   - Like a referee in a real game

6. **Room-based Architecture:** Each game is a "room" - scalable approach
   - Can have thousands of games running simultaneously
   - Like having multiple poker tables in a casino

7. **Code Splitting:** Only loads code for the current page - faster initial load
   - Game room code only loads when you join a game
   - Like loading one chapter of a book instead of the whole library

8. **Optimistic Updates:** Shows changes immediately, fixes if server says no
   - When you fold, UI updates instantly - feels responsive
   - If server says "invalid", it reverts - user sees error

---

# 3) Low Level Design (LLD)

---

## Component Architecture

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

## Frontend Design

### Component Architecture

Think of the frontend as a tree of React components - each component handles a specific part of the UI, and they work together to create the complete user experience.

**Component Hierarchy:**

```
App
├── Header
│   ├── Logo
│   ├── Navigation
│   └── UserMenu (Profile, Wallet, Settings, Sign out)
├── MainContent
│   ├── LobbyPage
│   │   ├── TableList
│   │   │   └── TableCard
│   │   │       ├── TableName
│   │   │       ├── Blinds
│   │   │       ├── PlayersCount
│   │   │       └── JoinButton
│   │   └── CreateTableButton
│   ├── GameTablePage
│   │   ├── GameTable
│   │   │   ├── PlayerSeats (6-9 seats)
│   │   │   │   └── PlayerSeat
│   │   │   │       ├── PlayerAvatar
│   │   │   │       ├── PlayerName
│   │   │   │       ├── PlayerChips
│   │   │   │       ├── PlayerCards (face down/up)
│   │   │   │       ├── PlayerBet
│   │   │   │       └── PlayerStatus (active, folded, all-in)
│   │   │   ├── CommunityCards
│   │   │   │   └── Card (face down/up)
│   │   │   ├── PotDisplay
│   │   │   ├── DealerButton
│   │   │   └── ActionTimer
│   │   ├── PlayerControls
│   │   │   ├── BettingControls
│   │   │   │   ├── CheckButton
│   │   │   │   ├── CallButton
│   │   │   │   ├── RaiseButton
│   │   │   │   ├── FoldButton
│   │   │   │   └── AllInButton
│   │   │   ├── BetAmountSlider
│   │   │   └── BetAmountInput
│   │   ├── GameInfo
│   │   │   ├── CurrentBet
│   │   │   ├── PotSize
│   │   │   ├── Blinds
│   │   │   └── HandHistory
│   │   └── ChatPanel
│   │       ├── ChatMessages
│   │       └── ChatInput
│   └── LeaderboardPage
│       ├── LeaderboardList
│       └── UserStats
└── SocketProvider (Real-time game updates)
```

### Key React Components

**Frontend Implementation:**

```typescript
// Game Table Component
const GameTable: React.FC<{ tableId: string }> = ({ tableId }) => {
  const { data: gameState } = useGameState(tableId);
  const { socket } = useSocket();

  useEffect(() => {
    socket.on('game-state-update', (update: GameStateUpdate) => {
      // Update game state in real-time
    });

    socket.on('player-action', (action: PlayerAction) => {
      // Animate player action
    });

    return () => {
      socket.off('game-state-update');
      socket.off('player-action');
    };
  }, [socket]);

  return (
    <div className="game-table">
      <div className="player-seats">
        {gameState?.players.map((player, index) => (
          <PlayerSeat
            key={player.id}
            player={player}
            position={index}
            isCurrentPlayer={player.id === currentUserId}
            isActive={gameState.currentPlayerId === player.id}
          />
        ))}
      </div>
      <CommunityCards cards={gameState?.communityCards} />
      <PotDisplay pot={gameState?.pot} />
      <DealerButton position={gameState?.dealerPosition} />
      {gameState?.currentPlayerId === currentUserId && (
        <PlayerControls
          gameState={gameState}
          onAction={handlePlayerAction}
        />
      )}
    </div>
  );
};

// Player Controls Component
const PlayerControls: React.FC<{ gameState: GameState; onAction: (action: PlayerAction) => void }> = ({ 
  gameState, 
  onAction 
}) => {
  const [betAmount, setBetAmount] = useState(gameState.currentBet);

  const handleCheck = () => {
    onAction({ type: 'check' });
  };

  const handleCall = () => {
    onAction({ type: 'call', amount: gameState.currentBet });
  };

  const handleRaise = () => {
    onAction({ type: 'raise', amount: betAmount });
  };

  const handleFold = () => {
    onAction({ type: 'fold' });
  };

  return (
    <div className="player-controls">
      <div className="betting-amount">
        <BetAmountSlider
          min={gameState.currentBet}
          max={gameState.playerChips}
          value={betAmount}
          onChange={setBetAmount}
        />
        <input
          type="number"
          value={betAmount}
          onChange={(e) => setBetAmount(Number(e.target.value))}
        />
      </div>
      <div className="action-buttons">
        {gameState.canCheck && (
          <button onClick={handleCheck}>Check</button>
        )}
        {gameState.canCall && (
          <button onClick={handleCall}>Call ${gameState.currentBet}</button>
        )}
        <button onClick={handleRaise}>Raise ${betAmount}</button>
        <button onClick={handleFold}>Fold</button>
        <button onClick={() => onAction({ type: 'all-in' })}>All In</button>
      </div>
    </div>
  );
};
```

### State Management

**State Management Strategy:**

- **Local State (useState)**: UI state (loading, errors, bet amount, selected action)
- **Component State**: Each component manages its own UI state
- **API State**: React Query or SWR for server state (game state, leaderboard) - caching, refetching
- **Global State (Redux Toolkit)**: User authentication, wallet balance, active game, player statistics

**Frontend Implementation:**

```typescript
// Using React Query for API state management
import { useQuery, useMutation, useQueryClient } from '@tanstack/react-query';

const useGameState = (tableId: string) => {
  return useQuery({
    queryKey: ['game-state', tableId],
    queryFn: async () => {
      const response = await axios.get(`/api/v1/tables/${tableId}/state`);
      return response.data;
    },
    refetchInterval: 1000 // Refetch every second for real-time updates
  });
};

const usePlayerAction = () => {
  const queryClient = useQueryClient();
  
  return useMutation({
    mutationFn: async ({ tableId, action }: { tableId: string; action: PlayerAction }) => {
      const response = await axios.post(`/api/v1/tables/${tableId}/action`, action);
      return response.data;
    },
    onSuccess: (data, variables) => {
      // Invalidate game state
      queryClient.invalidateQueries({ queryKey: ['game-state', variables.tableId] });
    }
  });
};
```

### Component Interactions

**Data Flow:**

1. **Table Joining** → User joins table, receives initial game state
2. **Player Actions** → User makes action (check, call, raise, fold), sent via Socket.io
3. **Game State Updates** → Socket.io broadcasts game state updates to all players
4. **Card Animations** → Cards revealed with animations using Framer Motion
5. **Hand Completion** → Winner determined, chips distributed, next hand starts

**Event Handling:**

- Player actions sent via Socket.io for real-time updates
- Game state updates trigger UI animations
- Timer counts down for player actions
- Card reveals animated with Framer Motion
- Chat messages broadcast to all players

### UI/UX Considerations

- **Loading States**: Show skeleton loaders for game table, spinners for actions
- **Error Handling**: Display user-friendly error messages, handle connection failures gracefully
- **Validation**: Client-side validation for bet amounts and actions
- **Responsive Design**: Mobile-first layout, optimized for touch interactions
- **Accessibility**: ARIA labels, keyboard navigation, screen reader support
- **Performance**: Efficient card animations, optimized game state updates, real-time synchronization via WebSocket

---

## Data Models

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

## Data APIs

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

## Backend Implementation Details

### Express.js Server Structure

```

server/
├── routes/
│   ├── auth.js
│   ├── games.js
│   └── rooms.js
├── controllers/
│   ├── GameController.js
│   └── RoomController.js
├── services/
│   ├── GameEngine.js
│   └── CardService.js
├── socket/
│   └── gameSocket.js
└── models/
    ├── Game.js
    ├── Room.js
    └── User.js

```

### Game Engine Implementation

```typescript
class GameEngine {
  async processPlayerAction(roomId: string, action: PlayerAction) {
    // Validate action
    // Update game state
    // Broadcast to all players
    // Persist to database
  }

  async dealCards(roomId: string) {
    // Generate random cards
    // Distribute to players
    // Update game state
  }
}

```

---

## Protocols

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

## Implementation Details

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

---

## Testing Strategy

### Frontend Testing (React.js)

**Unit Testing:**

- **Jest + React Testing Library** - Test components, hooks, game logic

- **Redux Testing** - Test game state management

- **Animation Testing** - Test Framer Motion animations

**Integration Testing:**

- **Socket.io Mocking** - Mock WebSocket connections

- **Game Flow Testing** - Test complete game flows

**E2E Testing:**

- **Cypress / Playwright** - Test multiplayer game scenarios

- **Test Scenarios:** Room creation, game joining, gameplay, disconnection handling

### Backend Testing (Node.js/Express.js)

**Unit Testing:**

- **Jest + Supertest** - Test API endpoints, game engine

- **Game Logic Testing** - Test poker hand evaluation, betting logic

- **Mocking:** Mock Socket.io, Redis, MongoDB

**Integration Testing:**

- **MongoDB Memory Server** - Test database operations

- **Redis Mock** - Test caching and distributed locks

- **Socket.io Testing** - Test real-time communication

**Load Testing:**

- **Artillery / k6** - Test concurrent game rooms

- **WebSocket Load Testing** - Test Socket.io under load

---

## Deployment & DevOps

### Frontend Deployment

**Build & Deploy:**

- **Production Build:** Optimized bundle with code splitting

- **CDN:** Deploy to CDN for fast global delivery

- **CI/CD:** Automated deployment pipeline

### Backend Deployment

**Server Setup:**

- **PM2:** Process manager with clustering

- **Nginx:** Load balancer and WebSocket proxy

- **Docker:** Containerized deployment

**Socket.io Scaling:**

- **Redis Adapter:** Enable horizontal scaling

- **Sticky Sessions:** Required for Socket.io

- **Load Balancer:** Configure for WebSocket support

**CI/CD Pipeline:**

- **Automated Testing:** Run tests before deployment

- **Zero-Downtime:** Rolling deployment strategy

- **Health Checks:** Verify Socket.io connections

---

## Environment Configuration

### Environment Variables

**Frontend:**

```env
REACT_APP_API_URL=https://api.example.com
REACT_APP_SOCKET_URL=wss://socket.example.com
REACT_APP_ENVIRONMENT=production

```

**Backend:**

```env
NODE_ENV=production
PORT=3000
MONGODB_URI=mongodb://...
REDIS_URL=redis://...
JWT_SECRET=xxx
SOCKET_IO_REDIS_URL=redis://...

```

---

## Database Migrations & Seeding

### MongoDB Migrations

**Migration Scripts:**

- **Schema Changes:** Add indexes for game queries

- **Data Migrations:** Update game state formats

- **Index Optimization:** Add compound indexes for performance

### Data Seeding

**Seed Data:**

- **Game Rooms:** Seed test game rooms

- **User Accounts:** Seed test players

- **Game History:** Seed sample game history

---

## API Documentation

### Swagger/OpenAPI

**API Documentation:**

- **Swagger UI:** Document REST APIs

- **WebSocket Documentation:** Document Socket.io events

- **Game Protocol:** Document game message formats

---

## API Versioning

**Versioning Strategy:**

- **URL Versioning:** `/api/v1/games`, `/api/v2/games`

- **Header Versioning:** `Accept: application/vnd.api+json;version=1`

- **Backward Compatibility:** Maintain old API versions for existing clients

- **WebSocket Versioning:** Version Socket.io events and message formats

---

## Monitoring & Logging

### Application Monitoring

**Frontend:**

- **Error Tracking:** Sentry for game errors

- **Performance:** Track animation performance

- **User Analytics:** Track game engagement

**Backend:**

- **APM:** Monitor game server performance

- **Socket.io Monitoring:** Track connection counts, latency

- **Game Metrics:** Track active rooms, concurrent players

### Logging

**Structured Logging:**

- **Winston / Pino:** Log game events

- **Game Actions:** Log all player actions for audit

- **Error Logging:** Detailed error logs with context

---

## Database Transactions & Consistency

### MongoDB Transactions

**Transaction Usage:**

- **Multi-Document Transactions** - For operations requiring ACID guarantees

- **Example:** Chip transfer + pot distribution + action logging

- **Session Management:** Use MongoDB sessions for transaction control

**Game State Updates:**

- **Atomic Operations:** Use transactions for critical game state changes

- **Example:** Chip transfer, pot distribution

- **Session Management:** Use MongoDB sessions

**Example:**

```typescript
const session = await mongoose.startSession();
session.startTransaction();
try {
  await Player.updateOne({ userId }, { $inc: { chips: -betAmount } }, { session });
  await Game.updateOne({ roomId }, { $inc: { pot: betAmount } }, { session });
  await Action.create([{ roomId, userId, action: 'bet', amount: betAmount }], { session });
  await session.commitTransaction();
} catch (error) {
  await session.abortTransaction();
  throw error;
} finally {
  session.endSession();
}

```

### Optimistic Locking

**Version Field:**

- **Version Field:** Add `version` field to game state documents

- **Conflict Detection:** Check version before update

- **Retry Logic:** Retry on version conflict for concurrent game actions

### Consistency Strategies

**Data Consistency:**

- **Game State Consistency:** Use transactions for all game state changes

- **Chip Consistency:** Ensure chip transfers are atomic

- **Action Consistency:** Log all actions atomically with state changes

---

## Third-Party Service Integration

### Socket.io Integration

**Real-time Communication:**

- **Redis Adapter:** Enable horizontal scaling

- **Room Management:** Efficient room-based messaging

- **Connection Management:** Handle reconnections, heartbeats

### Redis Integration

**Caching & Locks:**

- **Game State Caching:** Cache active game states

- **Distributed Locks:** Prevent race conditions

- **Pub/Sub:** Cross-server communication

---

## Security Implementation

### Frontend Security

**XSS Protection:**

- **React Escaping:** Automatic XSS protection

- **Input Sanitization:** Sanitize user inputs

- **CSP Headers:** Content Security Policy

### Backend Security

**Input Validation:**

- **Joi / Yup:** Validate game actions

- **Action Validation:** Validate betting rules, game rules

- **Rate Limiting:** Prevent action spam

**Game Security:**

- **Server-Authoritative:** All game logic on server

- **Cheat Prevention:** Validate all actions server-side

- **Secure Random:** Cryptographically secure random for cards

---

# 3) Interview Answers

## Q1. Most complex technical challenge in building the real-time poker game

**Situation:** Building a real-time multiplayer poker game required handling simultaneous player actions, ensuring game state consistency across all players, preventing cheating, managing network latency, and maintaining smooth 60fps animations while supporting 1,000+ concurrent game rooms.

**Action:** The most complex challenge was implementing a server-authoritative game architecture that ensures fair gameplay while providing responsive client-side interactions. **Backend (Node.js/Express.js):** I built a game engine that validates all player actions (fold, call, raise, all-in) on the server before applying them. I used **Socket.io with Redis adapter** for real-time communication across multiple servers. I implemented **room-based architecture** - each game room is isolated, and players join specific rooms. The game engine maintains authoritative game state in Redis for fast access, with MongoDB for persistence. **Frontend (React.js):** I implemented **client-side prediction** - UI updates immediately when player acts, but server reconciliation ensures correctness. I used **Context API with useReducer** for game state management. I implemented **latency compensation** - showing actions immediately and adjusting if server rejects. I used **Framer Motion** for smooth card animations and chip movements.

**Result:** Successfully delivered a fair, responsive multiplayer game. The system handles 1,000+ concurrent game rooms with 5,000+ active players. Game state is 100% consistent across all players. Zero cheating incidents due to server-authoritative architecture. Animations run at smooth 60fps. Player satisfaction is 95% with fair gameplay.

**Takeaway:** Server-authoritative architecture is essential for multiplayer games to prevent cheating. Client-side prediction improves UX but must reconcile with server. Room-based architecture enables horizontal scaling. Proper state management and animations are crucial for game feel.

---

## Q2. Implementing real-time multiplayer synchronization using Socket.io in the MERN stack

**Situation:** Multiple players needed to see game actions (folds, bets, card deals) in real-time with minimal latency, while ensuring all players see the same game state simultaneously across different network conditions.

**Action:** I implemented a robust real-time synchronization system. **Backend (Node.js/Express.js):** I set up a **Socket.io server** integrated with Express.js. I used **Redis adapter** for Socket.io to enable horizontal scaling - multiple servers share WebSocket connections through Redis pub/sub. I implemented **room-based messaging** - players join game-specific rooms (`room:${roomId}`), and when a player acts, the server validates the action, updates game state, and broadcasts to all players in that room. I stored **active game state in Redis** for fast access and low latency. I implemented **event ordering** - actions are processed in order using sequence numbers to prevent race conditions. **Frontend (React.js):** I created a Socket.io client that connects to the server. I implemented **automatic reconnection** with exponential backoff if connection drops. I used **event handlers** to update game state when receiving server broadcasts. I implemented **client-side prediction** - UI updates immediately, but server state is authoritative. I added **connection status indicators** to show when players are connected/disconnected.

**Result:** Real-time synchronization works seamlessly with less than 100ms latency for game actions. The system handles 5,000+ concurrent WebSocket connections. All players see game actions simultaneously. Automatic reconnection ensures 99% connection success rate. The Redis adapter allows scaling to multiple servers without connection issues.

**Takeaway:** Socket.io with Redis adapter is essential for scalable real-time multiplayer games. Room-based messaging reduces unnecessary broadcasts. Client-side prediction improves UX but server is authoritative. Always implement reconnection logic and connection status indicators.

---

## Q3. Designing the game engine architecture in Node.js to prevent cheating

**Situation:** The game needed to prevent players from manipulating game state, sending invalid actions, or exploiting client-side logic, ensuring fair gameplay for all players.

**Action:** I implemented a server-authoritative game engine architecture. **Backend (Node.js/Express.js):** I created a **GameEngine class** that maintains authoritative game state. All game logic runs on the server - card dealing, hand evaluation, winner determination, betting validation. I implemented **strict validation** - every player action (fold, call, raise, all-in) is validated against current game state, player's turn, betting rules, and chip count. I used **cryptographically secure random number generation** for card dealing to prevent prediction. I stored **game state in Redis** for fast access and **MongoDB for persistence**. I implemented **action logging** - all actions are logged with timestamps for audit trail. I added **rate limiting** to prevent action spam. I implemented **turn-based validation** - only the current player can act, and actions are processed in order. I used **database transactions** for critical operations (chip transfers, pot distribution) to ensure atomicity.

**Result:** Zero cheating incidents due to server-authoritative architecture. All game actions are validated and logged. Game state is 100% consistent across all players. Fair gameplay is ensured - no player can manipulate outcomes. The system handles 1,000+ concurrent games without security issues.

**Takeaway:** Server-authoritative architecture is the only way to prevent cheating in multiplayer games. All game logic must run on the server. Validate every action against game rules. Log all actions for audit trail. Use secure random number generation for card dealing.

---

## Q4. Handling network latency and ensuring fair gameplay for all players

**Situation:** Players from different locations experience varying network latencies (50ms to 500ms), which could give unfair advantages to players with lower latency if not handled properly.

**Action:** I implemented several latency compensation strategies. **Backend (Node.js/Express.js):** I implemented **turn timers** with buffer time - each player gets 30 seconds to act, with 5-second buffer for network latency. I used **action queuing** - actions are queued and processed in order, regardless of when they arrive (within the turn window). I implemented **server-side timing** - turn timers run on the server, not client, to prevent manipulation. I added **latency measurement** - server measures round-trip time for each player and adjusts timers accordingly. **Frontend (React.js):** I implemented **client-side prediction** - UI updates immediately when player acts, providing instant feedback. I used **interpolation** for smooth animations - if server state differs slightly, UI smoothly transitions. I added **latency indicators** showing each player's connection quality. I implemented **graceful degradation** - if latency is high, UI shows "Waiting for server..." instead of freezing.

**Result:** Fair gameplay is ensured regardless of network latency. Players with high latency (300-500ms) can still play effectively. Turn timers account for network delays. Client-side prediction provides responsive UI. Player satisfaction is 95% with fair gameplay experience.

**Takeaway:** Server-side timing is essential for fair gameplay. Turn timers should account for network latency. Client-side prediction improves UX but server is authoritative. Always show connection quality to players.

---

## Q5. Managing game state complexity using React.js and Context API

**Situation:** The game had complex state requirements - current game phase, player actions, card states, chip counts, pot size, turn order, and UI state needed to be managed and synchronized with server state.

**Action:** I implemented a sophisticated state management solution using **Context API with useReducer**. I created a **GameContext** that provides game state to all components. I used **useReducer** with a complex reducer function that handles all game state transitions (player acts, cards dealt, phase changes). I implemented **state normalization** - game state is stored in a normalized structure (players by ID, cards by position). I used **useMemo** and **useCallback** to prevent unnecessary re-renders. I implemented **optimistic updates** - UI updates immediately when player acts, but server state is authoritative. I created **custom hooks** (`useGameState`, `usePlayerAction`) to encapsulate game logic. I used **React.memo** for expensive components (card components, chip stacks). I implemented **state synchronization** - when server broadcasts game state, Context updates accordingly. I added **error boundaries** to handle state errors gracefully.

**Result:** Game state management is clean and maintainable. State updates are predictable and consistent. Performance is optimal - 60fps animations maintained. Adding new game features is easier with Context API. State synchronization with server works seamlessly.

**Takeaway:** Context API with useReducer works well for complex game state. Normalize state structure for better performance. Use memoization to prevent unnecessary re-renders. Optimistic updates improve UX but server is authoritative. Custom hooks encapsulate game logic.

---

