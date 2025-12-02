# iGamio Fantasy Sports Platform - Low Level Design (LLD)

> **Project Type:** Full-Stack Web Application (MERN Stack)  
> **Tech Stack:** 
> - **Frontend:** React.js, TypeScript, React Router, Redux Toolkit, Axios, Material-UI
> - **Backend:** Node.js, Express.js, MongoDB, Redis, Socket.io, JWT
> - **Services:** Cashfree Payment Gateway, AWS S3

---

## 3. Component Architecture

**Think of this as the building blocks - how components are organized and connected**

### Component Hierarchy (React.js)

```
App (Root Component - Entry Point)
├── Layout (Main Layout with Navigation)
│   ├── Header
│   │   ├── Logo
│   │   ├── NavigationMenu
│   │   └── UserMenu
│   ├── Sidebar (Desktop Only)
│   │   ├── NavLink (Matches)
│   │   ├── NavLink (Contests)
│   │   ├── NavLink (Wallet)
│   │   └── NavLink (Profile)
│   └── Main Content Area
│       ├── LoginPage
│       │   └── LoginForm
│       │       ├── EmailInput
│       │       ├── PasswordInput
│       │       └── SubmitButton
│       ├── MatchesPage
│       │   ├── FilterTabs (Scheduled/Live/Completed)
│       │   ├── MatchesList
│       │   │   └── MatchCard
│       │   │       ├── MatchInfo
│       │   │       ├── TeamNames
│       │   │       ├── MatchStatus
│       │   │       └── ViewContestsButton
│       │   └── Pagination
│       ├── MatchDetailPage
│       │   ├── MatchHeader
│       │   ├── ScoreCard
│       │   ├── AvailableContests
│       │   │   └── ContestCard
│       │   │       ├── ContestInfo
│       │   │       ├── PrizePool
│       │   │       ├── Participants
│       │   │       └── JoinButton
│       │   └── CreateTeamButton
│       ├── ContestsPage
│       │   ├── FilterTabs (All/Upcoming/Live/Completed)
│       │   ├── MyContestsList
│       │   │   └── ContestCard
│       │   │       ├── ContestInfo
│       │   │       ├── PrizePool
│       │   │       ├── UserRank
│       │   │       └── ViewDetailsButton
│       │   └── EmptyState
│       ├── ContestDetailPage
│       │   ├── ContestHeader
│       │   ├── Leaderboard
│       │   │   └── LeaderboardRow
│       │   │       ├── Rank
│       │   │       ├── UserInfo
│       │   │       ├── Points
│       │   │       └── Prize
│       │   └── MyTeamInfo
│       ├── CreateTeamPage
│       │   ├── PlayerList (with filters)
│       │   │   └── PlayerCard
│       │   │       ├── PlayerImage
│       │   │       ├── PlayerInfo
│       │   │       ├── PlayerPrice
│       │   │       └── SelectButton
│       │   ├── SelectedTeam
│       │   │   ├── SelectedPlayerCard
│       │   │   │   ├── CaptainBadge
│       │   │   │   └── ViceCaptainBadge
│       │   │   └── RemoveButton
│       │   └── TeamStats
│       │       ├── BudgetIndicator
│       │       ├── PlayerCount
│       │       └── ValidationErrors
│       ├── WalletPage
│       │   ├── BalanceCard
│       │   │   ├── AvailableBalance
│       │   │   └── QuickActions
│       │   │       ├── DepositButton
│       │   │       └── WithdrawButton
│       │   └── TransactionHistory
│       │       └── TransactionItem
│       │           ├── TransactionType
│       │           ├── Amount
│       │           ├── Status
│       │           └── Timestamp
│       ├── ProfilePage
│       │   ├── UserInfo
│       │   │   ├── Avatar
│       │   │   ├── Name
│       │   │   └── Email
│       │   └── MenuList
│       │       ├── MenuItem (KYC)
│       │       └── MenuItem (Settings)
│       └── B2BDashboardPage (Conditional - B2B Users Only)
│           ├── B2BDashboard
│           └── CreateContestPage
├── ReduxProvider (Global State Management)
│   └── Store
│       ├── authSlice (User authentication state)
│       ├── matchesSlice (Matches data)
│       ├── contestsSlice (Contests data)
│       ├── teamsSlice (User teams)
│       ├── walletSlice (Wallet balance & transactions)
│       └── userSlice (User profile data)
└── ThemeProvider (Material-UI Theme)
    └── CustomTheme (Light/Dark mode, colors, typography)
```

**How components work together:**
- **App** is the root - wraps everything, provides context
- **Layout** provides structure - header, sidebar, main content area
- **Pages** are top-level components - each page has its own components
- **Components** are reusable pieces - MatchCard, ContestCard, PlayerCard
- **ReduxProvider** manages global state - any component can access shared data
- **ThemeProvider** manages styling - colors, fonts, dark/light mode

### Data Sharing Strategy

#### Global State (Redux Toolkit)
- **User Authentication:** Login status, user profile, JWT tokens
- **Matches Data:** List of matches, match details, live scores (cached)
- **Contests Data:** User's contests, contest details, leaderboards
- **Teams Data:** Created teams, team details
- **Wallet Data:** Balance, transactions
- **App Settings:** Theme (light/dark), notifications preferences
- **UI State:** Global loading states, error messages, notifications

#### Local State (React useState/useReducer)
- **Form Inputs:** Temporary form data before submission (React Hook Form)
- **UI State:** Modal visibility, dropdowns, tooltips, selected filters
- **Temporary Data:** Search queries, filter selections, pagination state
- **Component-specific State:** Loading states for individual components

#### Context API
- **Theme Context:** App-wide theme (light/dark mode) - Material-UI ThemeProvider
- **Auth Context:** Quick access to auth state (optional, can use Redux)
- **Language Context:** i18n translations (react-i18next)

#### Props Drilling
- **Simple Data:** Pass props for parent-child communication
- **Avoid Deep Nesting:** Use Redux or Context for deeply nested components
- **Component Composition:** Use children props and render props pattern

---

## 4. Data Models

### User Model
```typescript
interface User {
  id: string;
  email: string;
  phone: string;
  name: string;
  avatar?: string;
  userType: 'B2C' | 'B2B';
  kycStatus: 'pending' | 'verified' | 'rejected';
  walletBalance: number;
  createdAt: string;
  updatedAt: string;
}
```

### Match Model
```typescript
interface Match {
  id: string;
  sport: 'cricket' | 'football' | 'kabaddi';
  teamA: Team;
  teamB: Team;
  status: 'scheduled' | 'live' | 'completed';
  scheduledAt: string;
  startedAt?: string;
  completedAt?: string;
  venue: string;
  score?: MatchScore;
  availableContests: number;
}
```

### Contest Model
```typescript
interface Contest {
  id: string;
  matchId: string;
  name: string;
  type: 'free' | 'paid' | 'private' | 'public';
  entryFee: number;
  prizePool: number;
  maxParticipants: number;
  currentParticipants: number;
  prizeDistribution: PrizeDistribution[];
  startTime: string;
  endTime: string;
  isJoined: boolean;
  userRank?: number;
  userPoints?: number;
}
```

### Team Model
```typescript
interface FantasyTeam {
  id: string;
  matchId: string;
  userId: string;
  players: SelectedPlayer[];
  captain: string; // playerId
  viceCaptain: string; // playerId
  totalPoints: number;
  rank?: number;
  createdAt: string;
}
```

### Player Model
```typescript
interface Player {
  id: string;
  name: string;
  role: 'batsman' | 'bowler' | 'allrounder' | 'wicketkeeper' | 'forward' | 'midfielder' | 'defender' | 'goalkeeper' | 'raider' | 'defender';
  team: string;
  price: number;
  points: number;
  image?: string;
}
```

### Transaction Model
```typescript
interface Transaction {
  id: string;
  userId: string;
  type: 'deposit' | 'withdraw' | 'contest_join' | 'contest_win';
  amount: number;
  status: 'pending' | 'success' | 'failed';
  paymentId?: string;
  contestId?: string;
  createdAt: string;
}
```

### KYC Document Model
```typescript
interface KYCDocument {
  id: string;
  userId: string;
  type: 'pan' | 'bank_account';
  documentNumber: string;
  documentImage: string;
  status: 'pending' | 'verified' | 'rejected';
  verifiedAt?: string;
  rejectionReason?: string;
}
```

---

## 5. Data APIs

**Note:** All API endpoints are implemented on the **backend (Node.js/Express)**, and the **frontend (React.js)** calls these APIs using Axios.

### Authentication APIs

**Backend Implementation:** Express.js routes handle authentication logic  
**Frontend Implementation:** React components call these APIs and handle responses

#### POST /api/auth/register
- **URL:** `/api/auth/register`
- **Method:** POST
- **Request Body:**
  ```json
  {
    "email": "user@example.com",
    "phone": "+919876543210",
    "password": "securePassword123",
    "name": "John Doe",
    "userType": "B2C"
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
    "email": "user@example.com",
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

### Match APIs

#### GET /api/matches
- **URL:** `/api/matches?status=scheduled&sport=cricket&page=1&limit=20`
- **Method:** GET
- **Query Parameters:**
  - `status`: scheduled | live | completed
  - `sport`: cricket | football | kabaddi
  - `page`: number (pagination)
  - `limit`: number (items per page)
- **Response:**
  ```json
  {
    "success": true,
    "data": {
      "matches": [ /* Array of Match objects */ ],
      "pagination": {
        "page": 1,
        "limit": 20,
        "total": 100,
        "totalPages": 5
      }
    }
  }
  ```
- **Status Codes:** 200 (Success), 400 (Invalid Parameters)

#### GET /api/matches/:matchId
- **URL:** `/api/matches/123`
- **Method:** GET
- **Response:**
  ```json
  {
    "success": true,
    "data": {
      "match": { /* Match object with details */ },
      "availableContests": [ /* Array of Contest objects */ ]
    }
  }
  ```
- **Status Codes:** 200 (Success), 404 (Match Not Found)

### Contest APIs

#### GET /api/contests
- **URL:** `/api/contests?matchId=123&type=paid&page=1`
- **Method:** GET
- **Query Parameters:**
  - `matchId`: string
  - `type`: free | paid | private | public
  - `page`: number
  - `limit`: number
- **Response:**
  ```json
  {
    "success": true,
    "data": {
      "contests": [ /* Array of Contest objects */ ],
      "pagination": { /* Pagination object */ }
    }
  }
  ```
- **Status Codes:** 200 (Success)

#### POST /api/contests/:contestId/join
- **URL:** `/api/contests/456/join`
- **Method:** POST
- **Request Body:**
  ```json
  {
    "teamId": "789",
    "paymentMethod": "wallet" | "gateway"
  }
  ```
- **Response:**
  ```json
  {
    "success": true,
    "data": {
      "contest": { /* Updated Contest object */ },
      "transaction": { /* Transaction object */ }
    }
  }
  ```
- **Status Codes:** 200 (Success), 400 (Invalid Request), 402 (Insufficient Balance)

#### GET /api/contests/:contestId/leaderboard
- **URL:** `/api/contests/456/leaderboard?page=1&limit=50`
- **Method:** GET
- **Response:**
  ```json
  {
    "success": true,
    "data": {
      "leaderboard": [
        {
          "rank": 1,
          "userId": "user123",
          "userName": "John Doe",
          "teamId": "team789",
          "points": 150,
          "prize": 1000
        }
      ],
      "pagination": { /* Pagination object */ }
    }
  }
  ```
- **Status Codes:** 200 (Success)

### Team APIs

#### GET /api/matches/:matchId/players
- **URL:** `/api/matches/123/players`
- **Method:** GET
- **Response:**
  ```json
  {
    "success": true,
    "data": {
      "players": [ /* Array of Player objects */ ],
      "teamA": [ /* Players from team A */ ],
      "teamB": [ /* Players from team B */ ]
    }
  }
  ```
- **Status Codes:** 200 (Success)

#### POST /api/teams
- **URL:** `/api/teams`
- **Method:** POST
- **Request Body:**
  ```json
  {
    "matchId": "123",
    "players": [
      { "playerId": "p1", "isCaptain": true, "isViceCaptain": false },
      { "playerId": "p2", "isCaptain": false, "isViceCaptain": true }
    ]
  }
  ```
- **Response:**
  ```json
  {
    "success": true,
    "data": {
      "team": { /* FantasyTeam object */ }
    }
  }
  ```
- **Status Codes:** 200 (Success), 400 (Validation Error - Invalid team composition)

#### PUT /api/teams/:teamId
- **URL:** `/api/teams/789`
- **Method:** PUT
- **Request Body:** Same as POST
- **Response:** Same as POST
- **Status Codes:** 200 (Success), 400 (Validation Error), 403 (Cannot update after deadline)

### Wallet APIs

#### GET /api/wallet/balance
- **URL:** `/api/wallet/balance`
- **Method:** GET
- **Response:**
  ```json
  {
    "success": true,
    "data": {
      "balance": 5000,
      "lockedAmount": 200
    }
  }
  ```
- **Status Codes:** 200 (Success)

#### POST /api/wallet/deposit
- **URL:** `/api/wallet/deposit`
- **Method:** POST
- **Request Body:**
  ```json
  {
    "amount": 1000,
    "paymentMethod": "upi" | "card" | "netbanking"
  }
  ```
- **Response:**
  ```json
  {
    "success": true,
    "data": {
      "paymentUrl": "https://cashfree.com/payment/...",
      "orderId": "order_123"
    }
  }
  ```
- **Status Codes:** 200 (Success), 400 (Invalid Amount)

#### GET /api/wallet/transactions
- **URL:** `/api/wallet/transactions?page=1&limit=20&type=deposit`
- **Method:** GET
- **Query Parameters:**
  - `page`: number
  - `limit`: number
  - `type`: deposit | withdraw | contest_join | contest_win
- **Response:**
  ```json
  {
    "success": true,
    "data": {
      "transactions": [ /* Array of Transaction objects */ ],
      "pagination": { /* Pagination object */ }
    }
  }
  ```
- **Status Codes:** 200 (Success)

### KYC APIs

#### POST /api/kyc/upload
- **URL:** `/api/kyc/upload`
- **Method:** POST
- **Request Body:** FormData
  - `type`: pan | bank_account
  - `documentNumber`: string
  - `documentImage`: File
- **Response:**
  ```json
  {
    "success": true,
    "data": {
      "document": { /* KYCDocument object */ }
    }
  }
  ```
- **Status Codes:** 200 (Success), 400 (Invalid Document)

#### GET /api/kyc/status
- **URL:** `/api/kyc/status`
- **Method:** GET
- **Response:**
  ```json
  {
    "success": true,
    "data": {
      "panStatus": "verified",
      "bankStatus": "pending",
      "documents": [ /* Array of KYCDocument objects */ ]
    }
  }
  ```
- **Status Codes:** 200 (Success)

---

## 6. Backend Implementation Details

### Express.js Server Structure

**Backend Architecture:**
```
Backend Server (Node.js + Express.js)
├── Routes (API Endpoints)
│   ├── /api/auth/* - Authentication routes
│   ├── /api/matches/* - Match routes
│   ├── /api/contests/* - Contest routes
│   ├── /api/teams/* - Team routes
│   ├── /api/wallet/* - Wallet routes
│   └── /api/kyc/* - KYC routes
├── Middleware
│   ├── Authentication (JWT verification)
│   ├── Authorization (Role-based access)
│   ├── Validation (Request validation)
│   ├── Rate Limiting
│   └── Error Handling
├── Controllers (Business Logic)
│   ├── AuthController
│   ├── MatchController
│   ├── ContestController
│   ├── TeamController
│   ├── WalletController
│   └── KYCController
├── Services (Data Access)
│   ├── UserService
│   ├── MatchService
│   ├── ContestService
│   ├── TeamService
│   ├── WalletService
│   └── KYCService
└── Models (Database Schemas)
    ├── User Model
    ├── Match Model
    ├── Contest Model
    ├── Team Model
    └── Transaction Model
```

### Backend API Implementation Example

**Backend (Express.js):**
```typescript
// Backend: routes/auth.ts
import express from 'express';
import { register, login } from '../controllers/authController';

const router = express.Router();

// POST /api/auth/register
router.post('/register', async (req, res) => {
  try {
    const { email, phone, password, name, userType } = req.body;
    
    // Validate input
    if (!email || !password || !name) {
      return res.status(400).json({ error: 'Missing required fields' });
    }
    
    // Check if user exists
    const existingUser = await User.findOne({ email });
    if (existingUser) {
      return res.status(409).json({ error: 'User already exists' });
    }
    
    // Hash password
    const hashedPassword = await bcrypt.hash(password, 10);
    
    // Create user
    const user = await User.create({
      email,
      phone,
      password: hashedPassword,
      name,
      userType
    });
    
    // Generate JWT tokens
    const accessToken = jwt.sign(
      { userId: user.id, email: user.email },
      process.env.JWT_SECRET,
      { expiresIn: '15m' }
    );
    
    const refreshToken = jwt.sign(
      { userId: user.id },
      process.env.REFRESH_TOKEN_SECRET,
      { expiresIn: '7d' }
    );
    
    res.json({
      success: true,
      data: {
        user: { id: user.id, email: user.email, name: user.name },
        accessToken,
        refreshToken
      }
    });
  } catch (error) {
    res.status(500).json({ error: 'Registration failed' });
  }
});
```

**Frontend (React.js):**
```typescript
// Frontend: services/authService.ts
import axios from 'axios';

export const register = async (userData: RegisterData) => {
  const response = await axios.post('/api/auth/register', userData);
  return response.data;
};

// Frontend: components/RegisterForm.tsx
const RegisterForm: React.FC = () => {
  const [formData, setFormData] = useState({ email: '', password: '', name: '' });
  
  const handleSubmit = async (e: React.FormEvent) => {
    e.preventDefault();
    try {
      const result = await register(formData);
      // Store tokens
      localStorage.setItem('accessToken', result.data.accessToken);
      // Redirect to home
      navigate('/');
    } catch (error) {
      // Show error message
      setError('Registration failed');
    }
  };
  
  return <form onSubmit={handleSubmit}>...</form>;
};
```

### MongoDB Schema Examples

**Backend (MongoDB Models):**
```typescript
// Backend: models/User.ts
import mongoose from 'mongoose';

const userSchema = new mongoose.Schema({
  email: { type: String, required: true, unique: true },
  phone: { type: String, required: true },
  password: { type: String, required: true },
  name: { type: String, required: true },
  userType: { type: String, enum: ['B2C', 'B2B', 'Admin'], default: 'B2C' },
  kycStatus: { type: String, enum: ['pending', 'verified', 'rejected'], default: 'pending' },
  walletBalance: { type: Number, default: 0 },
  createdAt: { type: Date, default: Date.now },
  updatedAt: { type: Date, default: Date.now }
});

export const User = mongoose.model('User', userSchema);
```

### Redis Caching Implementation

**Backend (Redis):**
```typescript
// Backend: services/cacheService.ts
import Redis from 'ioredis';

const redis = new Redis(process.env.REDIS_URL);

// Cache match data
export async function cacheMatches(matches: Match[]) {
  await redis.setex('matches:scheduled', 300, JSON.stringify(matches)); // 5 min cache
}

// Get cached matches
export async function getCachedMatches(): Promise<Match[] | null> {
  const cached = await redis.get('matches:scheduled');
  return cached ? JSON.parse(cached) : null;
}
```

---

## 7. Protocols

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

### Authentication Protocol
- **Method:** JWT (JSON Web Tokens)
- **Token Storage:** Secure storage (AsyncStorage with encryption)
- **Token Refresh:** Refresh token mechanism
- **Header Format:** `Authorization: Bearer <token>`

### Payment Gateway Protocol
- **Provider:** Cashfree Payment Gateway
- **Integration:** REST API + Webhooks
- **Payment Methods:** UPI, Cards, Net Banking, Wallets
- **Webhook Events:** Payment success, failure, refund

### Real-time Updates Protocol
- **Method:** Polling (for MVP) / WebSockets (future)
- **Polling Interval:** 5-10 seconds for live matches
- **WebSocket (Future):** For real-time score updates

---

## 8. Implementation Details

**Note:** Implementation details are split between frontend (React.js) and backend (Node.js/Express.js). Each section indicates where the code runs.

### Pagination

**Frontend Implementation:** React component handles infinite scroll UI  
**Backend Implementation:** Express.js API handles pagination logic

- **Strategy:** Offset-based pagination with infinite scroll - like scrolling through Instagram, loads more as you reach the bottom
- **Default Page Size:** 20 items per page - good balance between load time and user experience

**Backend (Express.js):**
```typescript
// Backend: routes/matches.ts
router.get('/matches', async (req, res) => {
  const { page = 1, limit = 20, status } = req.query;
  const skip = (page - 1) * limit;
  
  // Query database with pagination
  const matches = await Match.find({ status })
    .skip(skip)
    .limit(parseInt(limit))
    .sort({ scheduledAt: 1 });
  
  const total = await Match.countDocuments({ status });
  
  res.json({
    success: true,
    data: {
      matches,
      pagination: {
        page: parseInt(page),
        limit: parseInt(limit),
        total,
        totalPages: Math.ceil(total / limit),
        hasNextPage: page * limit < total
      }
    }
  });
});
```

**Frontend Implementation:**
  ```typescript
  // React component with pagination
  import { useState, useEffect, useCallback } from 'react';
  import { useInfiniteQuery } from '@tanstack/react-query';
  
  const MatchesList: React.FC = () => {
    const {
      data,
      fetchNextPage,
      hasNextPage,
      isFetchingNextPage,
    } = useInfiniteQuery({
      queryKey: ['matches'],
      queryFn: ({ pageParam = 1 }) => 
        axios.get('/api/matches', {
          params: { page: pageParam, limit: 20 }
        }).then(res => res.data),
      getNextPageParam: (lastPage) => 
        lastPage.pagination.hasNextPage ? lastPage.pagination.page + 1 : undefined,
    });
  
    // Infinite scroll with Intersection Observer
    const observerRef = useCallback((node: HTMLDivElement | null) => {
      if (isFetchingNextPage) return;
      if (observer.current) observer.current.disconnect();
      observer.current = new IntersectionObserver(entries => {
        if (entries[0].isIntersecting && hasNextPage) {
          fetchNextPage();
        }
      });
      if (node) observer.current.observe(node);
    }, [isFetchingNextPage, hasNextPage, fetchNextPage]);
  
    return (
      <div>
        {data?.pages.map((page) => 
          page.matches.map((match) => <MatchCard key={match.id} match={match} />)
        )}
        <div ref={observerRef} />
        {isFetchingNextPage && <LoadingSpinner />}
      </div>
    );
  };
  ```

### Debouncing/Throttling
- **Search Debouncing:** 300ms delay for search inputs - waits until user stops typing before searching, like Google search
  ```typescript
  import { useMemo, useState, useEffect } from 'react';
  import { debounce } from 'lodash';
  
  const PlayerSearch: React.FC = () => {
    const [searchTerm, setSearchTerm] = useState('');
    const [debouncedTerm, setDebouncedTerm] = useState('');
  
    useEffect(() => {
      const timer = setTimeout(() => {
        setDebouncedTerm(searchTerm);
      }, 300);
      return () => clearTimeout(timer);
    }, [searchTerm]);
  
    // Use debouncedTerm for API calls
    useEffect(() => {
      if (debouncedTerm) {
        searchPlayers(debouncedTerm);
      }
    }, [debouncedTerm]);
  
    return (
      <TextField
        value={searchTerm}
        onChange={(e) => setSearchTerm(e.target.value)}
        placeholder="Search players..."
      />
    );
  };
  ```
- **API Call Throttling:** Prevent multiple rapid API calls using React Query's built-in deduplication
- **Scroll Throttling:** Use Intersection Observer API for infinite scroll instead of scroll events

### Error Handling

**Frontend Implementation:** React components handle API errors and show user-friendly messages  
**Backend Implementation:** Express.js middleware handles errors and returns proper status codes

**Backend (Express.js):**
```typescript
// Backend: middleware/errorHandler.ts
export const errorHandler = (err: Error, req: Request, res: Response, next: NextFunction) => {
  console.error('Error:', err);
  
  if (err.name === 'ValidationError') {
    return res.status(400).json({ error: 'Validation failed', details: err.message });
  }
  
  if (err.name === 'UnauthorizedError') {
    return res.status(401).json({ error: 'Unauthorized' });
  }
  
  res.status(500).json({ error: 'Internal server error' });
};
```

**Frontend Implementation:**
- **API Error Handling:** Catches problems and shows friendly messages - like having a safety net that catches errors before they crash the app
  ```typescript
  // Axios interceptor for error handling
  import axios from 'axios';
  import { store } from './store';
  import { logout } from './store/slices/authSlice';
  import { useNavigate } from 'react-router-dom';
  
  axios.interceptors.response.use(
    (response) => response,
    (error) => {
      if (error.response?.status === 401) {
        // Handle unauthorized - redirect to login
        store.dispatch(logout());
        window.location.href = '/login';
      } else if (error.response?.status === 403) {
        // Handle forbidden
        showNotification('Access denied', 'error');
      } else if (error.response?.status >= 500) {
        // Handle server errors
        showNotification('Server error. Please try again later.', 'error');
      }
      return Promise.reject(error);
    }
  );
  
  // React Error Boundary
  class ErrorBoundary extends React.Component {
    state = { hasError: false, error: null };
  
    static getDerivedStateFromError(error: Error) {
      return { hasError: true, error };
    }
  
    componentDidCatch(error: Error, errorInfo: React.ErrorInfo) {
      console.error('Error caught:', error, errorInfo);
      // Log to error tracking service (Sentry, etc.)
    }
  
    render() {
      if (this.state.hasError) {
        return <ErrorFallback error={this.state.error} />;
      }
      return this.props.children;
    }
  }
  ```
- **Network Error Handling:** Show offline message with Service Worker status
- **Validation Error Handling:** Display field-specific errors using React Hook Form

### Caching Strategy
- **API Response Caching:** 
  - React Query/RTK Query remembers what you fetched - like having a smart assistant that knows when to refresh data (5 minutes default)
  - Browser HTTP cache headers - browser's built-in memory
  - Service Worker for offline caching - works even without internet
- **Image Caching:** 
  - Browser native image caching - browser remembers images it's seen
  - Lazy loading with Intersection Observer - only loads images when they're about to be visible, like loading photos as you scroll
  - WebP format for better compression - smaller file sizes, faster loading
- **Browser Storage:** 
  - localStorage: Like a small safe in your browser - stores user preferences, theme, recent searches
  - sessionStorage: Temporary storage that clears when tab closes - like a sticky note
  - IndexedDB: Large data sets (future) - like a database in the browser

### State Management Implementation

**Frontend Implementation:** Redux Toolkit manages client-side state

```typescript
// Frontend: Redux Toolkit slice - like a section of the global storage box
import { createSlice, createAsyncThunk } from '@reduxjs/toolkit';
import axios from 'axios';

// Async thunk for API calls
export const fetchMatches = createAsyncThunk(
  'matches/fetchMatches',
  async (params: { status?: string; page?: number }) => {
    const response = await axios.get('/api/matches', { params });
    return response.data;
  }
);

const matchesSlice = createSlice({
  name: 'matches',
  initialState: {
    matches: [] as Match[],
    loading: false,
    error: null as string | null,
    pagination: {
      page: 1,
      total: 0,
      hasMore: false,
    },
  },
  reducers: {
    clearMatches: (state) => {
      state.matches = [];
    },
  },
  extraReducers: (builder) => {
    builder
      .addCase(fetchMatches.pending, (state) => {
        state.loading = true;
        state.error = null;
      })
      .addCase(fetchMatches.fulfilled, (state, action) => {
        state.loading = false;
        state.matches = action.payload.matches;
        state.pagination = action.payload.pagination;
      })
      .addCase(fetchMatches.rejected, (state, action) => {
        state.loading = false;
        state.error = action.error.message || 'Failed to fetch matches';
      });
  },
});

export const { clearMatches } = matchesSlice.actions;
export default matchesSlice.reducer;
```

### Payment Gateway Integration

**Backend Implementation:** Express.js handles payment gateway integration  
**Frontend Implementation:** React components initiate payment and handle callbacks

**Backend (Express.js):**
```typescript
// Backend: routes/wallet.ts
router.post('/deposit', authenticate, async (req, res) => {
  const { amount, paymentMethod } = req.body;
  const userId = req.user.id;
  
  // Create order with Cashfree
  const order = await cashfree.createOrder({
    orderAmount: amount,
    orderCurrency: 'INR',
    customerDetails: {
      customerId: userId,
      customerEmail: req.user.email
    }
  });
  
  // Save order to database
  await Order.create({
    userId,
    amount,
    orderId: order.orderId,
    status: 'pending'
  });
  
  res.json({
    success: true,
    data: {
      paymentUrl: order.paymentSessionId,
      orderId: order.orderId
    }
  });
});
```

**Frontend Implementation:**
```typescript
// Frontend: Cashfree payment integration - like a cashier that handles all payment methods
import { loadScript } from '@cashfreepayments/cashfree-js';

const DepositPage: React.FC = () => {
  const [amount, setAmount] = useState(0);
  
  const initiatePayment = async () => {
    try {
      // Get payment session from backend
  const response = await axios.post('/api/wallet/deposit', {
    amount,
    paymentMethod: 'upi'
  });
  
      const { paymentSessionId } = response.data;
      
      // Initialize Cashfree Checkout
      const cashfree = await loadScript();
      const checkoutOptions = {
        paymentSessionId,
        returnUrl: `${window.location.origin}/wallet?payment=success`,
      };
      
      cashfree.checkout(checkoutOptions);
    } catch (error) {
      showNotification('Payment initiation failed', 'error');
    }
  };
  
  // Handle payment callback on return
  useEffect(() => {
    const urlParams = new URLSearchParams(window.location.search);
    const paymentStatus = urlParams.get('payment');
    if (paymentStatus === 'success') {
    // Verify payment with backend
      const orderId = urlParams.get('orderId');
      verifyPayment(orderId);
    }
  }, []);
  
  return (
    <Box>
      <TextField
        type="number"
        value={amount}
        onChange={(e) => setAmount(Number(e.target.value))}
        label="Amount"
      />
      <Button onClick={initiatePayment}>Deposit</Button>
    </Box>
  );
};
```

### Real-time Score Updates

**Backend Implementation:** Express.js API provides match scores, Socket.io for real-time updates  
**Frontend Implementation:** React components poll API or use WebSocket for live updates

**Backend (Socket.io):**
```typescript
// Backend: socket.io server
io.on('connection', (socket) => {
  socket.on('join-match', (matchId) => {
    socket.join(`match:${matchId}`);
  });
});

// When score updates
function broadcastScoreUpdate(matchId: string, score: MatchScore) {
  io.to(`match:${matchId}`).emit('score-update', score);
}
```

**Frontend Implementation:**
```typescript
// Frontend: Polling for live scores - checks server every 5 seconds if match is live, like refreshing a sports score page
import { useQuery, useQueryClient } from '@tanstack/react-query';

const MatchDetailPage: React.FC<{ matchId: string }> = ({ matchId }) => {
  const queryClient = useQueryClient();
  
  const { data: match } = useQuery({
    queryKey: ['match', matchId],
    queryFn: () => axios.get(`/api/matches/${matchId}`).then(res => res.data),
    refetchInterval: (data) => {
      // Poll every 5 seconds if match is live
      return data?.match?.status === 'live' ? 5000 : false;
    },
    refetchIntervalInBackground: true,
  });
  
  // Alternative: WebSocket for real-time updates (future)
  // useEffect(() => {
  //   const socket = io(process.env.REACT_APP_SOCKET_URL);
  //   socket.on(`match:${matchId}:update`, (data) => {
  //     queryClient.setQueryData(['match', matchId], data);
  //   });
  //   return () => socket.disconnect();
  // }, [matchId]);
  
  return <MatchScoreCard match={match} />;
};
```

### Image Upload for KYC

**Frontend Implementation:** React component handles file selection and upload UI  
**Backend Implementation:** Express.js handles file upload, stores in AWS S3

**Backend (Express.js + AWS S3):**
```typescript
// Backend: routes/kyc.ts
import multer from 'multer';
import { S3Client, PutObjectCommand } from '@aws-sdk/client-s3';

const upload = multer({ storage: multer.memoryStorage() });

router.post('/upload', authenticate, upload.single('documentImage'), async (req, res) => {
  const file = req.file;
  const { type, documentNumber } = req.body;
  
  // Upload to S3
  const s3Client = new S3Client({ region: 'us-east-1' });
  const key = `kyc/${req.user.id}/${type}-${Date.now()}.jpg`;
  
  await s3Client.send(new PutObjectCommand({
    Bucket: process.env.S3_BUCKET,
    Key: key,
    Body: file.buffer,
    ContentType: file.mimetype
  }));
  
  const documentUrl = `https://${process.env.S3_BUCKET}.s3.amazonaws.com/${key}`;
  
  // Save to database
  const document = await KYCDocument.create({
    userId: req.user.id,
    type,
    documentNumber,
    documentImage: documentUrl,
    status: 'pending'
  });
  
  res.json({ success: true, data: { document } });
});
```

**Frontend Implementation:**
```typescript
// Frontend: Document upload - drag and drop or click to select, like uploading a profile picture
import { useDropzone } from 'react-dropzone';
import { useMutation } from '@tanstack/react-query';

const KYCDocumentUpload: React.FC = () => {
  const [file, setFile] = useState<File | null>(null);
  const [preview, setPreview] = useState<string | null>(null);
  
  const uploadMutation = useMutation({
    mutationFn: async (formData: FormData) => {
  const response = await axios.post('/api/kyc/upload', formData, {
    headers: {
      'Content-Type': 'multipart/form-data',
    },
  });
  return response.data;
    },
    onSuccess: () => {
      showNotification('Document uploaded successfully', 'success');
    },
  });
  
  const onDrop = useCallback((acceptedFiles: File[]) => {
    const file = acceptedFiles[0];
    setFile(file);
    // Create preview
    const reader = new FileReader();
    reader.onload = () => setPreview(reader.result as string);
    reader.readAsDataURL(file);
  }, []);
  
  const { getRootProps, getInputProps, isDragActive } = useDropzone({
    onDrop,
    accept: {
      'image/*': ['.jpeg', '.jpg', '.png'],
    },
    maxFiles: 1,
  });
  
  const handleUpload = () => {
    if (!file) return;
    
    const formData = new FormData();
    formData.append('type', 'pan');
    formData.append('documentNumber', 'ABCDE1234F');
    formData.append('documentImage', file);
    
    uploadMutation.mutate(formData);
  };
  
  return (
    <Box>
      <div {...getRootProps()}>
        <input {...getInputProps()} />
        {isDragActive ? (
          <p>Drop the file here...</p>
        ) : (
          <p>Drag & drop a file here, or click to select</p>
        )}
      </div>
      {preview && <img src={preview} alt="Preview" />}
      <Button onClick={handleUpload} disabled={!file || uploadMutation.isLoading}>
        Upload
      </Button>
    </Box>
  );
};
```

### Performance Optimizations

**Frontend Optimizations:** React.js code splitting, lazy loading, memoization  
**Backend Optimizations:** Database indexing, Redis caching, query optimization
- **Code Splitting:** 
  - Route-based: React.lazy() with Suspense for pages - only loads the page you're visiting, like opening one chapter of a book
  - Component-based: Dynamic imports for heavy components - loads heavy stuff only when needed
  ```typescript
  const MatchDetailPage = React.lazy(() => import('./pages/MatchDetailPage'));
  ```
- **Image Optimization:** 
  - Compress images, use WebP format - smaller files, faster loading
  - Lazy loading with Intersection Observer - loads images as you scroll, like Instagram
  - Responsive images with srcset - shows smaller images on mobile, bigger on desktop
- **List Virtualization:** 
  - Use react-window for long lists - only renders what's visible, like a window showing part of a long list
  - Virtual scrolling for leaderboards - handles thousands of items smoothly
- **Memoization:** 
  - React.memo for component memoization - remembers component output, skips re-render if props didn't change
  - useMemo for expensive calculations - remembers calculation result, recalculates only when inputs change
  - useCallback for stable function references - keeps function reference stable, prevents unnecessary re-renders
- **Bundle Size:** 
  - Tree shaking removes unused code - like cleaning out your closet, only keeps what you use
  - Remove unused dependencies - smaller bundle, faster load
  - Analyze bundle with webpack-bundle-analyzer - see what's taking up space
- **React Query Caching:** 
  - Automatic caching and deduplication - smart assistant that remembers and avoids duplicate requests
  - Background refetching - updates data in background, keeps UI fresh
  - Optimistic updates - shows changes immediately, feels instant

### Security Implementation

**Frontend Security:** XSS protection, input validation, secure token storage  
**Backend Security:** Authentication, authorization, data validation, encryption
- **Token Storage:** 
  - JWT tokens in httpOnly cookies (preferred) - like a secure vault, JavaScript can't access it
  - Refresh token rotation - changes tokens regularly, like changing passwords
  - Automatic token refresh before expiry - renews before it expires, seamless for user
- **HTTPS:** All API calls over HTTPS - encrypted connection, like a secure tunnel
- **Input Validation:** 
  - Client-side: React Hook Form with Zod/Yup validation - catches errors before sending to server, like a bouncer checking IDs
  - Server-side: Always validate on backend - never trust the client, server is the authority
- **XSS Prevention:** 
  - Sanitize user inputs with DOMPurify - cleans user input, removes dangerous code
  - Use React's built-in XSS protection - React escapes by default, like having a built-in security guard
  - Avoid dangerouslySetInnerHTML - only use when absolutely necessary, like opening a door carefully
- **CSRF Protection:** 
  - CSRF tokens for state-changing operations - like a secret handshake, proves request is legitimate
  - SameSite cookie attribute - cookies only sent with same-site requests, prevents cross-site attacks
- **API Rate Limiting:** 
  - Handle rate limit errors gracefully - shows friendly message, doesn't crash
  - Show user-friendly error messages - "Too many requests, please wait" instead of error code
  - Implement retry logic with exponential backoff - waits longer between retries, like backing off when someone says "not now"
- **Content Security Policy (CSP):** 
  - Set appropriate CSP headers - tells browser what's allowed, like security rules
  - Restrict inline scripts and styles - prevents injection attacks, like locking doors

