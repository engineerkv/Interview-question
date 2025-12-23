# 1) Problem Statement

Design and implement a fantasy sports platform that addresses the following challenges:

- **Core Functionality**: Enable users to create teams, join contests, and compete based on real-world sports match performance, with support for both B2B (businesses creating contests) and B2C (users playing) models
- **Scale Requirements**: Handle millions of users, thousands of concurrent contests, millions of team selections during major sporting events, and real-time updates
- **Performance**: Real-time match data updates, fast player points calculation, dynamic leaderboard updates, low-latency contest operations
- **Team Management**: Handle concurrent team selections, validate team rules, support multiple teams per match, manage team updates
- **Contest Management**: Manage contest creation and joining, handle different contest types (free, paid, private, public), support multiple sports
- **Payment Processing**: Process payments for contest entry fees, handle deposits and withdrawals, manage wallet transactions, ensure secure payment processing
- **Real-time Updates**: Provide real-time score updates, calculate player points in real-time, update leaderboards dynamically, handle live match data
- **Data Consistency**: Ensure fair contest management, handle concurrent operations reliably, maintain accurate leaderboards and points

---

# 2) High Level Design (HLD)

---

## a) Functional Requirements

#### User Management

- **User registration and authentication** - Email, phone, or social login
- **User profiles** - Profile pages with stats, achievements, wallet balance
- **Wallet management** - Deposit, withdraw, view transaction history

#### Team Management

- **Create teams** - Select players within budget and team rules
- **Edit teams** - Update team before match deadline
- **Multiple teams** - Create multiple teams for same match
- **Team validation** - Validate team rules (budget, player limits, positions)

#### Contest Management

- **Join contests** - Join free or paid contests
- **Create contests (B2B)** - Businesses can create private contests
- **Contest types** - Free, paid, private, public contests
- **Contest details** - View contest size, entry fee, prize pool

#### Real-time Features

- **Live scores** - Real-time match score updates via WebSocket
- **Player points** - Real-time player points calculation
- **Leaderboard** - Dynamic leaderboard updates during matches
- **Match updates** - Live match events (goals, wickets, points)

#### Sports & Matches

- **Multiple sports** - Cricket, Football, Basketball, etc.
- **Match listing** - View upcoming and live matches
- **Match details** - View match info, players, teams
- **Player stats** - View player statistics and recent performance

---

## b) Non-Functional Requirements

#### Performance

- **Real-time updates** - Match data updates in < 1 second
- **Fast calculations** - Player points calculated in real-time
- **Low latency** - Leaderboard updates with minimal delay
- **Fast page loads** - Pages load in < 2 seconds

#### Scalability

- **Handle millions of users** - Support large user base
- **Thousands of contests** - Support concurrent contests
- **Peak traffic** - Handle traffic spikes during major matches
- **Real-time connections** - Support thousands of WebSocket connections

#### Reliability

- **99.9% uptime** - High availability during matches
- **Fault tolerance** - System continues working if components fail
- **Data consistency** - Maintain accurate leaderboards and points

#### User Experience

- **Responsive design** - Works on mobile and desktop
- **Accessibility** - ARIA labels, keyboard navigation
- **Intuitive UI** - Easy team building, clear contest information
- **Real-time feedback** - Instant updates on team changes

---

## c) MVP (Minimum Viable Product)

### Phase 1: MVP (Must Have) - Priority 1

**Core Features:**

- User registration and authentication
- Create teams for matches (single sport)
- Join free and paid contests
- Real-time match score updates (WebSocket)
- Real-time player points calculation
- Dynamic leaderboard updates
- Basic wallet functionality (deposit, view balance)

### Phase 2: Enhanced Features - Priority 2

**Advanced Features:**

- Multiple teams per match
- Multiple sports support
- B2B contest creation
- Advanced player stats
- Team sharing
- Contest history
- Withdrawal functionality

---

## d) Technology Choices

### Frontend Framework

- **React 19** - Latest React version with useOptimistic, useActionState, useTransition, useDeferredValue, and use() hook
- **TypeScript** - Type safety and better developer experience - Component-based UI framework with type safety

### State Management

- **React Query (TanStack Query)** - Server state management
- **Redux Toolkit** - Client state management
- **Context API** - App-wide configuration

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

- **React Query vs SWR**: React Query provides better caching
- **Redux Toolkit vs Zustand**: Redux Toolkit offers better DevTools

---

## e) Architecture Overview

The frontend follows a layered architecture optimized for fantasy sports with real-time scoring and team management.

**Component Structure:**

```

Frontend Application
├── Presentation Layer
│   ├── UI Components (PlayerCard, TeamCard, MatchCard, ScoreBoard)
│   ├── Feature Components (TeamBuilder, MatchViewer, Leaderboard, PlayerStats)
│   └── Layout Components (Header, Sidebar, Navigation, MainLayout)
├── Business/Controller Layer
│   ├── Business Logic (Team validation, scoring calculations, player selection)
│   ├── Custom Hooks (useTeam, useMatch, usePlayer, useScoring)
│   └── Service Functions (Pure functions for scoring calculations and validation)
├── State Management
│   ├── Client State
│   │   ├── Local State (useState) - Component-specific UI state
│   │   ├── Global State (Redux Toolkit/Zustand) - Team state, match data, user preferences
│   │   └── Context API - User authentication, app configuration
│   └── Server State
│       ├── React Query (useQuery/useMutation) - API data caching, refetching, optimistic updates
│       └── Service Worker - Offline caching, background sync
├── API Integration
│   ├── API Client (Axios with interceptors for auth, error handling)
│   ├── API Services (teamService, matchService, playerService, scoringService)
│   └── Request/Response Transformation (Data normalization and error handling)
└── Routing
    ├── Public Routes (Home, Matches)
    ├── Protected Routes (Team, Leaderboard, Settings)
    └── Route Guards (Authentication and authorization checks)

```

**Frontend Deployment:**

- **Build**: Production bundle with code splitting using Vite
- **CDN**: Static assets served from CloudFront/Cloudflare edge locations
- **Caching**: Aggressive caching for static assets, cache-busting for updates
- **Environment**: Environment variables for API endpoints and feature flags

**Key Frontend Components:**

- **React 19 Application**:
  - Single-page application with client-side routing
  - Component-based architecture for reusability
  - React Query with React 19 hooks (useOptimistic, useTransition, useDeferredValue)
  - Real-time scoring updates
  - Responsive design for mobile and desktop
  - Modern React 19 features for better performance and UX

- **CDN/Edge**:
  - Global distribution of static assets
  - Edge caching for improved performance
  - DDoS protection and rate limiting at edge

---

## f) App Flow

### Complete System Flow (Frontend Perspective)

**Primary User Flow - Creating Team and Joining Contest:**

1. **User browses matches** → MatchList component displays upcoming matches with React Query useSuspenseQuery (React 19)
2. **User selects match** → MatchCard navigates to TeamBuilderPage
3. **User builds team** → TeamBuilder component allows selecting players within budget
4. **Team validation** → useDeferredValue (React 19) defers expensive validation calculations
5. **User saves team** → SaveTeamButton triggers useOptimistic (React 19) for instant team save
6. **User joins contest** → ContestList shows available contests, user selects contest
7. **Payment processing** → PaymentForm uses useActionState (React 19) for entry fee payment
8. **Contest joined** → User redirected to ContestDetailPage with live leaderboard

**Component Interaction Flow:**

```
User Browses → MatchList (React Query useSuspenseQuery)
            ↓
Match Selected → TeamBuilder (player selection)
            ↓
Team Built → TeamBuilder (useOptimistic for instant save)
            ↓
Contest Selected → ContestList (shows contests)
            ↓
Payment → PaymentForm (useActionState for form)
            ↓
Contest Joined → ContestDetail (live leaderboard)
```

**State Update Flow:**

1. **Local State** → Team builder, form inputs use useState
2. **Deferred State** → useDeferredValue (React 19) defers team validation calculations
3. **Optimistic State** → useOptimistic (React 19) shows team saved immediately
4. **Server State** → React Query manages matches, teams, contests, caching, refetching
5. **Global State** → Redux Toolkit manages wallet balance, user preferences
6. **Real-time State** → WebSocket updates match scores, player points, leaderboard
7. **Component Re-render** → React updates UI based on state changes

**Real-time Match Updates Flow:**

1. **Match starts** → WebSocket connection established
2. **Score update** → WebSocket receives match event
3. **Player points calculation** → Frontend calculates player points based on events
4. **Leaderboard update** → useOptimistic (React 19) updates leaderboard immediately
5. **UI refresh** → ContestDetail component shows updated scores and rankings
6. **User notification** → Toast shows significant score changes

**Error Handling Flow:**

1. **API Error** → React Query mutation returns error
2. **Error Boundary** → Catches component errors, shows fallback UI
3. **User Feedback** → Toast notification displays error message
4. **Retry Logic** → User can retry failed requests

**Analytics Dashboard Flow:**

1. **User navigates** → React Router navigates to /dashboard
2. **Data Fetching** → React Query useQuery fetches analytics data
3. **Loading State** → Skeleton screens displayed while loading
4. **Data Display** → Charts render with analytics data
5. **Real-time Updates** → Polling every 30 seconds for active URLs
6. **User Interactions** → Filters update query params, trigger refetch

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
│   │       └── WalletBalance
│   ├── MainContent
│   └── Footer
├── Pages
│   ├── HomePage
│   │   └── MatchList
│   │       └── MatchCard
│   ├── TeamBuilderPage
│   │   ├── TeamBuilder
│   │   │   ├── PlayerList
│   │   │   │   └── PlayerCard
│   │   │   ├── SelectedTeam
│   │   │   └── BudgetIndicator
│   │   └── SaveTeamButton
│   ├── ContestListPage
│   │   ├── ContestFilters
│   │   └── ContestList
│   │       └── ContestCard
│   ├── ContestDetailPage
│   │   ├── ContestInfo
│   │   ├── Leaderboard
│   │   │   └── LeaderboardRow
│   │   └── MyTeamScore
│   └── MatchDetailPage
│       ├── MatchScore
│       ├── PlayerPoints
│       └── MatchEvents
└── SharedComponents
    ├── Button
    ├── Input
    ├── Card
    ├── Toast
    └── LoadingSpinner
```

**Key React Components:**

**1. TeamBuilder Component:**

- Allows selecting players within budget and team rules
- Shows available budget and team composition
- Uses useDeferredValue (React 19) for deferred validation
- Validates team rules (budget, player limits, positions)
- Uses useOptimistic (React 19) for instant team save

**2. MatchList Component:**

- Displays upcoming and live matches
- Fetches matches with React Query useSuspenseQuery (React 19)
- Filters matches by sport, date, status
- Links to match detail or team builder

**3. ContestDetail Component:**

- Displays contest information and live leaderboard
- Shows real-time leaderboard updates via WebSocket
- Uses useOptimistic (React 19) for instant leaderboard updates
- Displays user's team rank and score
- Shows prize distribution

**4. Leaderboard Component:**

- Displays contest leaderboard with rankings
- Updates in real-time as player points change
- Handles pagination for large contests
- Highlights user's position
- Uses useTransition (React 19) for non-urgent updates

**5. PlayerCard Component:**

- Displays player information and stats
- Shows player price and points
- Handles player selection/deselection
- Shows player role and team
- Updates player points in real-time

**Component Communication:**

- **Props** → Parent to child data flow
- **Callbacks** → Child to parent communication
- **Context API** → Shared state across components (theme, user)
- **React Query** → Server state management (matches, teams, contests)
- **Redux Toolkit** → Global client state (wallet balance, user preferences)
- **WebSocket** → Real-time match scores, player points, leaderboard updates

# 4) Data Models

### TypeScript Interfaces

```typescript
interface Match {
  id: string;
  sport: "cricket" | "football" | "basketball";
  teamA: Team;
  teamB: Team;
  startTime: string;
  status: "upcoming" | "live" | "completed";
  score?: MatchScore;
}

interface Team {
  id: string;
  name: string;
  logo: string;
  players: Player[];
}

interface Player {
  id: string;
  name: string;
  role: string;
  price: number;
  points: number;
  team: Team;
  stats?: PlayerStats;
}

interface FantasyTeam {
  id: string;
  userId: string;
  matchId: string;
  players: Player[];
  captainId: string;
  viceCaptainId: string;
  totalPoints: number;
  budget: number;
  createdAt: string;
}

interface Contest {
  id: string;
  matchId: string;
  name: string;
  type: "free" | "paid" | "private" | "public";
  entryFee: number;
  prizePool: number;
  maxParticipants: number;
  currentParticipants: number;
  prizeDistribution: PrizeDistribution[];
  status: "upcoming" | "live" | "completed";
}

interface LeaderboardEntry {
  rank: number;
  userId: string;
  username: string;
  teamId: string;
  totalPoints: number;
  prize?: number;
}

interface Wallet {
  userId: string;
  balance: number;
  transactions: Transaction[];
}

interface Transaction {
  id: string;
  type: "deposit" | "withdrawal" | "contest_entry" | "winnings";
  amount: number;
  status: "pending" | "completed" | "failed";
  createdAt: string;
}

interface FormState {
  players: string[];
  captainId: string;
  viceCaptainId: string;
  budget: number;
  errors: {
    budget?: string;
    players?: string;
  };
}
```

# 5) API Design

### POST /api/v1/contests/:contestId/join

- **URL:** `/api/v1/contests/:contestId/join`
- **Method:** POST
- **Description:** Join a contest with a team
- **Request Body:**

 ```json
 {
 "teamId": "team_abc123",
 "paymentMethod": "wallet"
 }

 ```

- **Response:**

 ```json
 {
 "success": true,
 "data": {
 "contest": {...},
 "transaction": {...}
 }
 }

 ```

- **Status Codes:** 200 (Success), 400 (Invalid Request), 402 (Insufficient Balance)

### GET /api/v1/contests/:contestId/leaderboard

- **URL:** `/api/v1/contests/:contestId/leaderboard?page=1&limit=50`
- **Method:** GET
- **Description:** Get contest leaderboard
- **Response:**

 ```json
 {
 "success": true,
 "data": {
 "leaderboard": [...],
 "pagination": {...}
 }
 }

 ```

- **Status Codes:** 200 (Success), 404 (Contest Not Found)

---

# 6) Protocols

### REST API Protocol

**Request Format:**

## iii) Implementation Details

### Business/Controller Layer

**Custom Hooks:**

- Encapsulate business logic and API calls
- Example: `useTeam`, `useContest`, `useMatch`, `useLeaderboard`, `useWallet`
- Handle data transformation and validation

**Service Functions:**

- Pure functions for data processing and validation
- Team validation, player points calculation, budget calculations
- Reusable across components

### Advanced Component Patterns

**Compound Components:**

- Group related components together (e.g., Form.Input, Form.Button)
- Share implicit state between components

**Render Props Pattern:**

- Pass render functions as props for flexible component composition

**Custom Hooks Pattern:**

- Extract reusable logic into custom hooks
- Example: `useShortenURL`, `useAnalytics`, `useCopyToClipboard`

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
function useShortenURL() {
  return useMutation({
    mutationFn: (url: string) => shortenUrl(url),
    onSuccess: () => queryClient.invalidateQueries(["urls"])
  });
}

```

**Component with React Query:**

```typescript
function Form() {
  const { mutate, isPending } = useShortenURL();
  const [url, setUrl] = useState("");

  const handleSubmit = (e: FormEvent) => {
    e.preventDefault();
    mutate(url);
  };

  return <form onSubmit={handleSubmit}>...</form>;
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

- `useQuery` for data fetching and caching
- `useMutation` for data mutations (create, update, delete)
- Automatic refetching, background updates, optimistic updates
- Example: API data caching, synchronization

## iii) Implementation Details

### Business/Controller Layer

**Custom Hooks:**

- Encapsulate business logic and API calls
- Example: `useTeam`, `useContest`, `useMatch`, `useLeaderboard`, `useWallet`
- Handle data transformation and validation

**Service Functions:**

- Pure functions for data processing and validation
- Team validation, player points calculation, budget calculations

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
- Example: Test iGamio Fantasy Sports Platform flow from start to finish

# 8) Algorithms

### Frontend Algorithms

**Team Budget Validation Algorithm:**

```javascript
function validateTeamBudget(selectedPlayers, maxBudget) {
  const totalCost = selectedPlayers.reduce((sum, player) => sum + player.price, 0);
  return {
    isValid: totalCost <= maxBudget,
    totalCost,
    remaining: maxBudget - totalCost,
    exceedsBy: totalCost > maxBudget ? totalCost - maxBudget : 0
  };
}
```

**Player Points Calculation:**

```javascript
function calculatePlayerPoints(player, matchEvents) {
  let points = 0;
  const playerEvents = matchEvents.filter(e => e.playerId === player.id);

  playerEvents.forEach(event => {
    switch(event.type) {
      case 'run': points += event.value; break;
      case 'wicket': points += 25; break;
      case 'catch': points += 8; break;
      case 'boundary': points += event.value === 4 ? 1 : 2; break;
      // ... more event types
    }
  });

  return points;
}
```

**Team Points Calculation:**

```javascript
function calculateTeamPoints(team, matchEvents) {
  const captainMultiplier = 2;
  const viceCaptainMultiplier = 1.5;

  let totalPoints = team.players.reduce((sum, player) => {
    let playerPoints = calculatePlayerPoints(player, matchEvents);

    if (player.id === team.captainId) {
      playerPoints *= captainMultiplier;
    } else if (player.id === team.viceCaptainId) {
      playerPoints *= viceCaptainMultiplier;
    }

    return sum + playerPoints;
  }, 0);

  return totalPoints;
}
```

**Leaderboard Sorting:**

```javascript
function sortLeaderboard(entries) {
  return entries.sort((a, b) => {
    if (b.totalPoints !== a.totalPoints) {
      return b.totalPoints - a.totalPoints;
    }
    return new Date(a.createdAt) - new Date(b.createdAt); // Earlier team wins tie
  }).map((entry, index) => ({
    ...entry,
    rank: index + 1
  }));
}
```

**Debouncing Algorithm (for search):**

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

- Client-side validation before team submission
- Sanitize user input to prevent XSS attacks
- Validate team rules (budget, player limits, positions)
- Validate payment amounts and wallet balance

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

**HTTPS:**

- All API calls over HTTPS
- Enforce HTTPS in production
- HSTS headers for security

**Rate Limiting (Client-Side):**

- Debounce API calls to prevent abuse
- Show user-friendly messages when rate limited
- Implement exponential backoff for retries

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

**Situation:** In a fantasy sports platform, we need to manage teams, contests, real-time match scores, player points, leaderboards, and wallet transactions efficiently.

**Action:**

- Use React Query for server state (matches, teams, contests) - handles caching, refetching, and synchronization
- Use `useOptimistic()` (React 19) for instant team saves and leaderboard updates before server confirmation
- Use `useDeferredValue()` (React 19) for deferred team validation calculations to improve performance
- Use WebSocket for real-time match scores, player points, and leaderboard updates
- Use Redux Toolkit for global client state (wallet balance, user preferences)
- Use useState for local component state (team builder, form inputs)
- Use Context API for user authentication, theme preferences

**Result:** Real-time updates, reduced API calls through caching, improved performance with deferred values, better user experience with instant feedback.

**Takeaway:** Combining React Query for server state, React 19's optimistic updates for teams, deferred values for validation, and WebSocket for real-time scores provides seamless fantasy sports experience.

### Q: How would you implement real-time leaderboard updates?

**Answer (STAR Method):**

**Situation:** Users need to see leaderboard rankings update in real-time as player points change during matches.

**Action:**

- Use WebSocket (Socket.io) for real-time connection
- Use `useOptimistic()` (React 19) to show leaderboard updates immediately before server confirmation
- Calculate player points on frontend based on match events
- Use `useTransition()` (React 19) for non-urgent leaderboard re-renders
- Implement connection retry logic with exponential backoff
- Show connection status indicator
- Handle offline scenarios gracefully

**Result:** Leaderboard updates delivered in < 1 second, instant UI feedback, improved user engagement, reliable real-time delivery.

**Takeaway:** WebSocket combined with React 19's optimistic updates and frontend point calculations provides the best real-time leaderboard experience for fantasy sports.
