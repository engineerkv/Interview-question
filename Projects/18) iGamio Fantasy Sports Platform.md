# Fantasy Sports Platform

---

## 📍 Navigation

<div align="center">

[Home: README](README.md) • [← Previous: Real-Time Poker Game](17%29%20Real-Time%20Poker%20Game.md)

[📋 Cheatsheet](Projects%20Interview%20Cheatsheet.md)

</div>

---

## Overview

Design a fantasy sports platform where users create teams, join contests, and compete based on real-world sports match performance. The system handles team selection, real-time match data, player points calculation, and dynamic leaderboards.

---

## 1) Requirements

### Functional Requirements

**Core Features:**
- User registration and authentication
- Create teams for matches (select players within budget)
- Join contests (free or paid)
- Real-time match score updates
- Real-time player points calculation
- Dynamic leaderboard updates
- Wallet management (deposit, withdraw)
- Contest creation (B2B - businesses can create private contests)
- Multiple sports support (Cricket, Football, Basketball)

**Advanced Features:**
- Multiple teams per match
- Team editing before match deadline
- Contest analytics
- Player statistics and recent performance
- Tournament support

### Non-Functional Requirements

**Performance:**
- Real-time match updates: < 1 second
- Fast player points calculation
- Low-latency leaderboard updates
- Fast page loads: < 2 seconds

**Scalability:**
- Handle millions of users
- Thousands of concurrent contests
- Millions of team selections during major events
- Real-time connections for live matches

**Reliability:**
- 99.9% uptime (critical during matches)
- Accurate points calculation
- Fair contest management

---

## 2) Component Hierarchy

The frontend is a React application for fantasy sports. Here's the structure:

```
App
├── Layout
│   ├── Header
│   │   ├── Logo
│   │   ├── WalletBalance
│   │   └── UserMenu
│   └── MainContent
├── Pages
│   ├── MatchesPage
│   │   └── MatchList
│   │       └── MatchCard
│   ├── TeamBuilderPage
│   │   ├── MatchInfo
│   │   ├── PlayerList
│   │   │   ├── PlayerCard
│   │   │   │   ├── PlayerInfo (name, team, position)
│   │   │   │   ├── PlayerPrice
│   │   │   │   ├── PlayerStats
│   │   │   │   └── AddToTeamButton
│   │   │   └── Filters (position, team, price)
│   │   ├── SelectedTeam
│   │   │   ├── TeamSummary (selected players, budget used)
│   │   │   ├── TeamValidation (rules check)
│   │   │   └── SaveTeamButton
│   │   └── BudgetIndicator
│   ├── ContestsPage
│   │   ├── ContestList
│   │   │   └── ContestCard
│   │   │       ├── ContestInfo (size, entry fee, prize pool)
│   │   │       ├── JoinedCount
│   │   │       └── JoinButton
│   │   └── ContestFilters (free, paid, private)
│   ├── LiveMatchPage
│   │   ├── MatchScore (real-time updates)
│   │   ├── PlayerPoints (real-time calculation)
│   │   ├── Leaderboard (dynamic updates)
│   │   └── MatchEvents (goals, wickets, etc.)
│   └── WalletPage
│       ├── WalletBalance
│       ├── DepositButton
│       ├── WithdrawButton
│       └── TransactionHistory
└── SharedComponents
    ├── PlayerCard
    ├── Leaderboard
    └── MatchScore
```

### Key Components Explained

**1. TeamBuilderPage Component**
- Main team building interface
- Player list with filters
- Selected team display
- Budget tracking
- Team validation (rules check)

**2. PlayerCard Component**
- Individual player display
- Player info, price, stats
- Add to team button
- Disabled if budget exceeded or position limit reached

**3. LiveMatchPage Component**
- Real-time match updates
- Player points calculation
- Dynamic leaderboard
- Match events (goals, wickets, etc.)

**4. Leaderboard Component**
- Shows contest rankings
- Real-time position updates
- User's position highlighted
- Prize distribution display

---

## 3) Data Models

Here are the key data structures:

```typescript
// Match
interface Match {
  id: string;
  sport: "cricket" | "football" | "basketball";
  team1: Team;
  team2: Team;
  date: string;
  status: "upcoming" | "live" | "completed";
  score?: MatchScore;
}

// Team (sports team)
interface Team {
  id: string;
  name: string;
  logo?: string;
}

// Player
interface Player {
  id: string;
  name: string;
  teamId: string;
  team: Team;
  position: string;  // "Batsman", "Bowler", "Forward", etc.
  price: number;
  points: number;  // Current match points
  stats: PlayerStats;
}

// Player stats
interface PlayerStats {
  recentPerformance: number[];  // Last 5 matches points
  averagePoints: number;
  totalMatches: number;
}

// Fantasy team
interface FantasyTeam {
  id: string;
  userId: string;
  matchId: string;
  players: FantasyPlayer[];
  totalPoints: number;
  budgetUsed: number;
  budgetLimit: number;
  createdAt: string;
}

// Fantasy player (player in user's team)
interface FantasyPlayer {
  playerId: string;
  player: Player;
  position: string;
  isCaptain: boolean;  // Captain gets 2x points
  isViceCaptain: boolean;  // Vice-captain gets 1.5x points
}

// Contest
interface Contest {
  id: string;
  matchId: string;
  name: string;
  type: "free" | "paid" | "private";
  size: number;  // Max participants
  entryFee: number;
  prizePool: number;
  joinedCount: number;
  createdBy?: string;  // For private contests (B2B)
  prizeDistribution: PrizeDistribution[];
}

// Prize distribution
interface PrizeDistribution {
  rank: string;  // "1", "2-3", "4-10"
  prize: number;
  percentage?: number;
}

// Leaderboard entry
interface LeaderboardEntry {
  rank: number;
  teamId: string;
  team: FantasyTeam;
  totalPoints: number;
  prize?: number;
}
```

### Data Flow Explanation

**When a user creates a team:**
1. User selects match
2. User selects players within budget
3. Team validation (budget, position limits, team rules)
4. User sets captain and vice-captain
5. Team is saved
6. User can join contests with this team

**Real-time points calculation:**
1. Match events occur (goal, wicket, point)
2. Player points calculated based on event
3. Fantasy team points updated (sum of player points)
4. Leaderboard updated in real-time
5. WebSocket broadcasts updates to all users

**Contest flow:**
1. User creates team for match
2. User browses available contests
3. User joins contest (free or paid)
4. Contest fills up to size limit
5. Match starts, points calculated in real-time
6. Leaderboard updates dynamically
7. Contest ends, prizes distributed

---

## 4) API Design

### REST Endpoints

**GET /api/v1/matches**
- Get matches
- Query params: `sport`, `status`, `date`
- Returns: Array of Match objects

**GET /api/v1/matches/:id/players**
- Get players for match
- Returns: Array of Player objects

**POST /api/v1/teams**
- Create a fantasy team
- Request body: `{ matchId: string, players: FantasyPlayer[] }`
- Returns: FantasyTeam object

**GET /api/v1/contests**
- Get contests
- Query params: `matchId`, `type`, `page`, `limit`
- Returns: Paginated list of Contest objects

**POST /api/v1/contests/:id/join**
- Join a contest
- Request body: `{ teamId: string }`
- Returns: Updated Contest object

**GET /api/v1/contests/:id/leaderboard**
- Get contest leaderboard
- Returns: Array of LeaderboardEntry objects

**GET /api/v1/matches/:id/live**
- Get live match data
- Returns: Match with real-time score and player points

### WebSocket Events

**Connection:** `wss://api.example.com/matches/:id`

**Events:**
- `match_event` - Match event occurred (goal, wicket, etc.)
- `player_points` - Player points updated
- `leaderboard_update` - Leaderboard updated

**Message Format:**
```json
{
  "type": "player_points",
  "data": {
    "playerId": "player_123",
    "points": 25,
    "event": "goal"
  }
}
```

---

## Key Design Decisions

**1. Real-time Points Calculation**
- Calculate points immediately on match events
- Update leaderboard in real-time
- WebSocket for instant updates
- Fair and transparent scoring

**2. Team Validation**
- Validate team rules (budget, positions, limits)
- Client-side validation for immediate feedback
- Server-side validation for security
- Clear error messages

**3. Dynamic Leaderboard**
- Update leaderboard in real-time
- Show user's position
- Prize distribution display
- Efficient ranking calculation

**4. Budget Management**
- Track budget used as players selected
- Disable players if budget exceeded
- Clear budget indicator
- Prevent invalid team creation

---

## Interview Talking Points

**When explaining this system, I'd focus on:**

1. **Requirements First**: Start with core functionality - create teams, join contests, real-time match updates, leaderboards

2. **Component Structure**: Explain the React component hierarchy - team builder, player list, live match, leaderboard

3. **Data Models**: Walk through Match, Player, FantasyTeam, Contest - and team validation rules

4. **API Design**: Show the REST endpoints and WebSocket protocol - teams, contests, live match data, leaderboard

5. **Key Challenges**: 
   - Real-time points calculation and leaderboard updates
   - Team validation and budget management
   - Handling millions of team selections during major events
   - Fair contest management and prize distribution

**Example explanation flow:**
> "So for a fantasy sports platform, the core requirement is allowing users to create teams by selecting players within a budget, join contests, and compete based on real-world match performance. The frontend is a React app with a team builder component where users select players, a budget tracker that shows remaining budget, and team validation that checks rules (budget limits, position requirements). When matches are live, real-time match events (goals, wickets) trigger player points calculation, which updates fantasy team points and leaderboards instantly via WebSocket. The data model includes Match objects, Player objects with prices and stats, FantasyTeam objects with selected players and budget tracking, and Contest objects with prize pools. The main API endpoints handle team creation, contest joining, and leaderboard retrieval, while WebSocket handles real-time match events and points updates. Key challenges include real-time points calculation during live matches, ensuring fair team validation, handling traffic spikes during major sporting events, and maintaining accurate leaderboards with thousands of participants."

---

---

## 📍 Navigation

<div align="center">

[Home: README](README.md) • [← Previous: Real-Time Poker Game](17%29%20Real-Time%20Poker%20Game.md)

[📋 Cheatsheet](Projects%20Interview%20Cheatsheet.md)

</div>

---
