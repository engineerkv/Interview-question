# Real-Time Poker Game

## Overview

Design a real-time multiplayer poker game where multiple players can join tables, play Texas Hold'em poker with synchronized game state, and handle player actions in real-time with minimal latency.

---

## 1) Requirements

### Functional Requirements

**Core Features:**
- User registration and authentication
- Create and join game rooms (2-9 players)
- Texas Hold'em poker gameplay
- Player actions (fold, check, call, raise, all-in)
- Real-time card dealing
- Betting rounds (Pre-flop, Flop, Turn, River)
- Hand rankings and winner determination
- Real-time pot updates
- Player status tracking (active, folded, all-in)
- Chat functionality during games
- Game history and replay

**Advanced Features:**
- Multiple game variants (No-Limit, Pot-Limit, Fixed-Limit)
- Tournament support
- Spectator mode
- Player statistics and leaderboards
- Reconnection to active games

### Non-Functional Requirements

**Performance:**
- Minimal latency for game state synchronization
- Smooth animations (60fps)
- Fast player action processing
- Real-time updates: < 100ms

**Scalability:**
- Support thousands of concurrent game tables
- Millions of players
- Real-time synchronization across all players

**Reliability:**
- 99.9% uptime
- Fair gameplay (no cheating)
- Game state consistency
- Handle player disconnections gracefully

---

## 2) Component Hierarchy

The frontend is a React application for real-time poker. Here's the structure:

```
App
├── Layout
│   ├── Header
│   │   ├── Logo
│   │   ├── Balance (chips)
│   │   └── UserMenu
│   └── MainContent
├── Pages
│   ├── LobbyPage
│   │   ├── RoomList
│   │   │   └── RoomCard
│   │   │       ├── RoomName
│   │   │       ├── PlayersCount
│   │   │       ├── Blinds
│   │   │       └── JoinButton
│   │   └── CreateRoomButton
│   ├── GameRoomPage
│   │   ├── GameTable
│   │   │   ├── PlayerSeats (circular arrangement)
│   │   │   │   └── PlayerSeat
│   │   │   │       ├── PlayerInfo (name, avatar, chips)
│   │   │   │       ├── PlayerCards (face down or face up)
│   │   │   │       ├── PlayerBet (chips in pot)
│   │   │   │       └── PlayerStatus (active, folded, all-in)
│   │   │   ├── CommunityCards (center of table)
│   │   │   │   ├── FlopCards (3 cards)
│   │   │   │   ├── TurnCard (1 card)
│   │   │   │   └── RiverCard (1 card)
│   │   │   ├── PotDisplay (total pot amount)
│   │   │   ├── DealerButton
│   │   │   └── ActionTimer (countdown for current player)
│   │   ├── PlayerActions
│   │   │   ├── FoldButton
│   │   │   ├── CheckButton
│   │   │   ├── CallButton
│   │   │   ├── RaiseButton
│   │   │   │   └── RaiseAmountInput
│   │   │   └── AllInButton
│   │   ├── HandInfo (current hand strength)
│   │   └── ChatPanel
│   │       ├── ChatMessages
│   │       └── ChatInput
│   └── GameHistoryPage
│       └── HandHistoryList
└── SharedComponents
    ├── Card (playing card component)
    ├── ChipStack
    └── Timer
```

### Key Components Explained

**1. GameTable Component**
- Main game interface
- Circular player seats arrangement
- Community cards in center
- Pot display
- Dealer button indicator
- Action timer for current player

**2. PlayerSeat Component**
- Individual player seat
- Player info (name, avatar, chip count)
- Player cards (face down for others, face up for user)
- Bet amount display
- Status indicator (active, folded, all-in)

**3. PlayerActions Component**
- Action buttons for current player
- Fold, Check, Call, Raise, All-in
- Raise amount input
- Disabled when not player's turn
- Timer countdown

**4. CommunityCards Component**
- Flop (3 cards), Turn (1 card), River (1 card)
- Card dealing animations
- Face up display

---

## 3) Data Models

Here are the key data structures:

```typescript
// Game room
interface GameRoom {
  id: string;
  name: string;
  type: "cash" | "tournament";
  maxPlayers: number;
  currentPlayers: number;
  blinds: {
    smallBlind: number;
    bigBlind: number;
  };
  buyIn: number;
  status: "waiting" | "active" | "finished";
  players: Player[];
  currentHand?: Hand;
}

// Player (in game)
interface Player {
  id: string;
  userId: string;
  name: string;
  avatar?: string;
  seatNumber: number;
  chips: number;
  status: "active" | "folded" | "all_in" | "sitting_out";
  cards?: Card[];  // Only visible to player or when hand ends
  currentBet: number;
  isDealer: boolean;
  isSmallBlind: boolean;
  isBigBlind: boolean;
  isTurn: boolean;  // Is it this player's turn to act
}

// Card
interface Card {
  suit: "hearts" | "diamonds" | "clubs" | "spades";
  rank: "2" | "3" | "4" | "5" | "6" | "7" | "8" | "9" | "10" | "J" | "Q" | "K" | "A";
}

// Hand (current game hand)
interface Hand {
  id: string;
  roomId: string;
  stage: "pre_flop" | "flop" | "turn" | "river" | "showdown" | "finished";
  pot: number;
  communityCards: Card[];
  currentPlayerId: string;  // Player whose turn it is
  actionTimer: number;  // Seconds remaining
  lastRaiseAmount: number;
  minimumRaise: number;
  winners?: Winner[];  // After showdown
}

// Winner
interface Winner {
  playerId: string;
  handRank: string;  // "Royal Flush", "Straight Flush", etc.
  prize: number;
}

// Player action
interface PlayerAction {
  type: "fold" | "check" | "call" | "raise" | "all_in";
  amount?: number;  // For raise
  playerId: string;
  handId: string;
  timestamp: string;
}
```

### Data Flow Explanation

**When a player joins a game:**
1. User selects or creates game room
2. User joins room and takes a seat
3. User buys in (adds chips)
4. Game starts when enough players join
5. Dealer button assigned
6. Blinds posted
7. Cards dealt

**Gameplay flow:**
1. Pre-flop: Each player receives 2 cards
2. Betting round: Players act (fold, call, raise)
3. Flop: 3 community cards dealt
4. Betting round: Players act
5. Turn: 1 community card dealt
6. Betting round: Players act
7. River: 1 community card dealt
8. Betting round: Players act
9. Showdown: Players reveal cards, winner determined
10. Pot distributed to winner(s)

**Real-time synchronization:**
1. Player action sent via WebSocket
2. Server validates action
3. Server updates game state
4. Server broadcasts to all players
5. All clients update UI simultaneously
6. Next player's turn begins

---

## 4) API Design

### REST Endpoints

**GET /api/v1/rooms**
- Get available game rooms
- Query params: `type`, `status`, `page`, `limit`
- Returns: Paginated list of GameRoom objects

**POST /api/v1/rooms**
- Create a game room
- Request body: `{ name: string, type: string, maxPlayers: number, blinds: Blinds, buyIn: number }`
- Returns: GameRoom object

**POST /api/v1/rooms/:id/join**
- Join a game room
- Request body: `{ buyIn: number }`
- Returns: Updated GameRoom object

**GET /api/v1/rooms/:id**
- Get game room details
- Returns: GameRoom object with current hand

**GET /api/v1/rooms/:id/history**
- Get hand history
- Returns: Array of Hand objects

### WebSocket Events

**Connection:** `wss://api.example.com/rooms/:id`

**Events:**
- `player_joined` - Player joined room
- `player_left` - Player left room
- `hand_started` - New hand started
- `cards_dealt` - Cards dealt to players
- `community_cards` - Community cards dealt
- `player_action` - Player made action
- `hand_finished` - Hand completed, winners announced
- `game_state` - Full game state update

**Message Format:**
```json
{
  "type": "player_action",
  "data": {
    "action": {
      "type": "raise",
      "amount": 100,
      "playerId": "player_123"
    },
    "hand": {
      "stage": "flop",
      "pot": 500,
      "currentPlayerId": "player_456"
    }
  }
}
```

---

## Key Design Decisions

**1. Real-time Game State Synchronization**
- WebSocket for instant updates
- All players see same game state
- Minimal latency (< 100ms)
- Fair gameplay

**2. Action Validation**
- Server validates all actions
- Prevents cheating
- Enforces game rules
- Time limits for actions

**3. Card Dealing Animation**
- Smooth card dealing animations
- Face down for other players
- Face up for user
- Reveal animations at showdown

**4. Turn Management**
- Clear turn indicators
- Action timer countdown
- Disable actions when not player's turn
- Auto-fold on timeout

**5. Hand History**
- Store all hands for replay
- Show hand history
- Winner determination
- Fair dispute resolution

---

## Interview Talking Points

**When explaining this system, I'd focus on:**

1. **Requirements First**: Start with core functionality - multiplayer poker, real-time synchronization, player actions, game state management

2. **Component Structure**: Explain the React component hierarchy - game table, player seats, community cards, action buttons

3. **Data Models**: Walk through GameRoom, Player, Hand, Card - and game state management

4. **API Design**: Show the REST endpoints and WebSocket protocol - rooms, player actions, real-time game events

5. **Key Challenges**: 
   - Real-time game state synchronization with minimal latency
   - Fair gameplay and action validation
   - Handling player disconnections and reconnections
   - Smooth animations and user experience

**Example explanation flow:**
> "So for a real-time poker game, the core requirement is allowing multiple players to join tables and play poker with synchronized game state. The frontend is a React app with a game table component showing player seats in a circular arrangement, community cards in the center, and action buttons for the current player. When a player makes an action (fold, call, raise), it's sent via WebSocket to the server, which validates the action, updates the game state, and broadcasts to all players. The data model includes GameRoom objects for game tables, Player objects with chips and status, Hand objects tracking the current hand with betting rounds, and Card objects for the deck. Real-time synchronization ensures all players see the same game state simultaneously with minimal latency (< 100ms). The main API endpoints handle room management and hand history, while WebSocket handles all real-time game events (actions, card dealing, pot updates). Key challenges include ensuring fair gameplay through server-side validation, maintaining game state consistency across all clients, handling player disconnections gracefully, and providing smooth animations for card dealing and betting."
