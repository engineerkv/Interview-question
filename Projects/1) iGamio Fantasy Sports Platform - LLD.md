# iGamio Fantasy Sports Platform - Low Level Design (LLD)

> **Project Type:** Cross-platform Mobile App (Android, iOS, Web)  
> **Tech Stack:** React Native, Axios, REST APIs, Cashfree Payment Gateway

---

## 3. Component Architecture

### Routing Structure

```
App Navigator (Stack)
├── Auth Stack
│   ├── Login Screen
│   ├── Register Screen
│   └── Forgot Password Screen
├── Main Tab Navigator
│   ├── Home Tab
│   │   ├── Matches Screen (Scheduled/Live/Completed)
│   │   └── Match Detail Screen
│   ├── Contests Tab
│   │   ├── My Contests Screen
│   │   ├── Contest Detail Screen
│   │   └── Leaderboard Screen
│   ├── Create Team Tab
│   │   ├── Team Selection Screen
│   │   └── Team Preview Screen
│   ├── Wallet Tab
│   │   ├── Wallet Balance Screen
│   │   ├── Deposit Screen
│   │   ├── Withdraw Screen
│   │   └── Transaction History Screen
│   └── Profile Tab
│       ├── Profile Screen
│       ├── KYC Verification Screen
│       └── Settings Screen
└── B2B Stack (Conditional)
    ├── B2B Dashboard Screen
    ├── Create Contest Screen
    └── Analytics Screen
```

### Component Hierarchy

```
App
├── NavigationContainer
│   ├── AuthNavigator (if not authenticated)
│   │   └── AuthStack
│   └── MainNavigator (if authenticated)
│       ├── TabNavigator
│       │   ├── HomeStack
│       │   │   ├── MatchesList
│       │   │   │   ├── MatchCard
│       │   │   │   │   ├── MatchInfo
│       │   │   │   │   ├── TeamNames
│       │   │   │   │   └── MatchStatus
│       │   │   │   └── FilterTabs
│       │   │   └── MatchDetail
│       │   │       ├── MatchHeader
│       │   │       ├── ScoreCard
│       │   │       ├── AvailableContests
│       │   │       └── ContestCard
│       │   ├── ContestsStack
│       │   │   ├── MyContestsList
│       │   │   │   ├── ContestCard
│       │   │   │   │   ├── ContestInfo
│       │   │   │   │   ├── PrizePool
│       │   │   │   │   └── UserRank
│       │   │   │   └── FilterTabs
│       │   │   └── ContestDetail
│       │   │       ├── ContestHeader
│       │   │       ├── Leaderboard
│       │   │       │   └── LeaderboardRow
│       │   │       └── MyTeamInfo
│       │   ├── CreateTeamStack
│       │   │   ├── TeamSelection
│       │   │   │   ├── PlayerList
│       │   │   │   │   └── PlayerCard
│       │   │   │   ├── SelectedTeam
│       │   │   │   │   └── SelectedPlayerCard
│       │   │   │   └── TeamStats
│       │   │   │       ├── BudgetIndicator
│       │   │   │       └── PlayerCount
│       │   │   └── TeamPreview
│       │   │       ├── TeamFormation
│       │   │       └── SaveTeamButton
│       │   ├── WalletStack
│       │   │   ├── WalletBalance
│       │   │   │   ├── BalanceCard
│       │   │   │   └── QuickActions
│       │   │   ├── DepositScreen
│       │   │   │   ├── AmountInput
│       │   │   │   └── PaymentGateway
│       │   │   └── TransactionHistory
│       │   │       └── TransactionItem
│       │   └── ProfileStack
│       │       ├── ProfileScreen
│       │       │   ├── UserInfo
│       │       │   └── MenuList
│       │       └── KYCScreen
│       │           ├── DocumentUpload
│       │           └── VerificationStatus
│       └── B2BNavigator (if B2B user)
│           └── B2BStack
│               ├── B2BDashboard
│               └── CreateContest
└── ReduxProvider
    └── Store
        ├── authSlice
        ├── matchesSlice
        ├── contestsSlice
        ├── teamsSlice
        ├── walletSlice
        └── userSlice
```

### Data Sharing Strategy

#### Global State (Redux)
- **User Authentication:** Login status, user profile, tokens
- **Matches Data:** List of matches, match details, live scores
- **Contests Data:** User's contests, contest details, leaderboards
- **Teams Data:** Created teams, team details
- **Wallet Data:** Balance, transactions
- **App Settings:** Theme, notifications preferences

#### Local State (Component State)
- **Form Inputs:** Temporary form data before submission
- **UI State:** Loading states, modal visibility, selected filters
- **Temporary Data:** Search queries, filter selections

#### Context API (Optional)
- **Theme Context:** App-wide theme (light/dark)
- **Language Context:** i18n translations
- **Auth Context:** Quick access to auth state (alternative to Redux)

#### Props Drilling
- **Simple Data:** Pass props for parent-child communication
- **Avoid Deep Nesting:** Use Redux or Context for deeply nested components

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

### Authentication APIs

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

## 7. Implementation Details

### Pagination
- **Strategy:** Offset-based pagination
- **Default Page Size:** 20 items per page
- **Implementation:**
  ```javascript
  // API call with pagination
  const fetchMatches = async (page = 1, limit = 20) => {
    const response = await axios.get('/api/matches', {
      params: { page, limit }
    });
    return response.data;
  };
  
  // Infinite scroll implementation
  const loadMore = () => {
    if (hasMore && !loading) {
      setPage(prev => prev + 1);
    }
  };
  ```

### Debouncing/Throttling
- **Search Debouncing:** 300ms delay for search inputs
  ```javascript
  const debouncedSearch = useMemo(
    () => debounce((query) => {
      searchPlayers(query);
    }, 300),
    []
  );
  ```
- **API Call Throttling:** Prevent multiple rapid API calls
- **Scroll Throttling:** Throttle scroll events for performance

### Error Handling
- **API Error Handling:**
  ```javascript
  // Axios interceptor for error handling
  axios.interceptors.response.use(
    (response) => response,
    (error) => {
      if (error.response?.status === 401) {
        // Handle unauthorized - redirect to login
        store.dispatch(logout());
      }
      return Promise.reject(error);
    }
  );
  ```
- **Network Error Handling:** Show offline message
- **Validation Error Handling:** Display field-specific errors

### Caching Strategy
- **API Response Caching:** Cache match list, contest list (5 minutes)
- **Image Caching:** React Native Image caching
- **Local Storage:** Cache user preferences, recent searches

### State Management Implementation
```javascript
// Redux slice example
const matchesSlice = createSlice({
  name: 'matches',
  initialState: {
    matches: [],
    loading: false,
    error: null,
  },
  reducers: {
    setMatches: (state, action) => {
      state.matches = action.payload;
    },
    setLoading: (state, action) => {
      state.loading = action.payload;
    },
  },
  extraReducers: (builder) => {
    builder
      .addCase(fetchMatches.pending, (state) => {
        state.loading = true;
      })
      .addCase(fetchMatches.fulfilled, (state, action) => {
        state.loading = false;
        state.matches = action.payload;
      });
  },
});
```

### Payment Gateway Integration
```javascript
// Cashfree payment integration
const initiatePayment = async (amount) => {
  const response = await axios.post('/api/wallet/deposit', {
    amount,
    paymentMethod: 'upi'
  });
  
  // Open Cashfree payment page
  const paymentUrl = response.data.paymentUrl;
  // Use WebView or deep link to open payment
  Linking.openURL(paymentUrl);
};

// Handle payment callback
const handlePaymentCallback = (paymentId, status) => {
  if (status === 'success') {
    // Verify payment with backend
    verifyPayment(paymentId);
  }
};
```

### Real-time Score Updates
```javascript
// Polling for live scores
useEffect(() => {
  if (match.status === 'live') {
    const interval = setInterval(() => {
      fetchMatchScore(matchId);
    }, 5000); // Poll every 5 seconds
    
    return () => clearInterval(interval);
  }
}, [match.status, matchId]);
```

### Image Upload for KYC
```javascript
// Document upload
const uploadKYCDocument = async (type, documentNumber, imageUri) => {
  const formData = new FormData();
  formData.append('type', type);
  formData.append('documentNumber', documentNumber);
  formData.append('documentImage', {
    uri: imageUri,
    type: 'image/jpeg',
    name: 'document.jpg',
  });
  
  const response = await axios.post('/api/kyc/upload', formData, {
    headers: {
      'Content-Type': 'multipart/form-data',
    },
  });
  
  return response.data;
};
```

### Performance Optimizations
- **Code Splitting:** Lazy load screens and components
- **Image Optimization:** Compress images, use WebP format
- **List Virtualization:** Use FlatList with proper optimization
- **Memoization:** Use React.memo, useMemo, useCallback
- **Bundle Size:** Remove unused dependencies, tree shaking

### Security Implementation
- **Token Storage:** Secure storage with encryption
- **HTTPS:** All API calls over HTTPS
- **Input Validation:** Validate all user inputs
- **XSS Prevention:** Sanitize user inputs
- **API Rate Limiting:** Handle rate limit errors gracefully

