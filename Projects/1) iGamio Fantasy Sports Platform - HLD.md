# iGamio Fantasy Sports Platform - High Level Design (HLD)

> **Project Type:** Full-Stack Web Application (MERN Stack)  
> **Frontend:** React.js Web Application  
> **Backend:** Node.js, Express.js, MongoDB, REST APIs  
> **Tech Stack:** 
> - **Frontend:** React.js, TypeScript, React Router, Redux Toolkit, Axios, Material-UI
> - **Backend:** Node.js, Express.js, MongoDB, Redis, Socket.io, JWT
> - **Services:** Cashfree Payment Gateway, AWS S3 (for file storage)
> **Team Size:** 2-person team  
> **Built:** From scratch

---

## 1. Requirements

### a) Functional Requirements

#### User Management
- **User registration and authentication** - Users can sign up with email, phone, or social login (Google, Facebook) - makes it easy to get started
- **User profile management** - Users can update their profile, change password, manage settings
- **B2B customer accounts** - Separate accounts for businesses who want to create their own contests - like white-label solution
- **B2C user accounts** - Regular users who play fantasy sports
- **Role-based access control** - Different permissions for Admin (full access), B2B (create contests), and B2C (play contests) - like having different keys for different doors

#### Contests
- **Multiple sports support** - Cricket, Football, Kabaddi - users can play different sports
- **Match views** - Scheduled (upcoming), Live (in-progress), Completed (past results) - like a sports calendar
- **Real-money contests** - Users can join paid contests and win real money
- **Contest types** - Free (no entry fee), Paid (entry fee required), Private (invite-only), Public (anyone can join)
- **Contest categories** - Head-to-Head (1v1), Small League (few players), Mega League (thousands of players) - different competition levels

#### Team Management
- **Create fantasy teams** - Users pick players from both teams, like building a dream team
- **Update teams** - Can change team before match starts - like editing your lineup
- **View team composition** - See which players you selected, their roles, and points
- **Team validation** - System checks rules: correct number of players, budget limit, player roles - like a referee checking if team is valid
- **Multiple teams** - Can create multiple teams for same match - increases winning chances

#### Payment & Transactions
- **Deposit money** - Users add money to their wallet using UPI, cards, or net banking - like adding money to a prepaid card
- **Withdraw money** - Users can withdraw winnings to their bank account (after KYC verification)
- **Join paid contests** - Use wallet balance to enter paid contests
- **Win amount distribution** - Winners get money automatically added to wallet - like instant prize money
- **Transaction history** - Users can see all deposits, withdrawals, contest entries, and winnings - like a bank statement
- **Payment gateway (Cashfree)** - Handles all payments securely - like a cashier that processes payments
- **Secure processing** - PCI-DSS compliant, all payments encrypted - like a bank vault

#### KYC Verification
- **Bank account verification** - Users verify their bank account for withdrawals - like linking your bank
- **PAN card verification** - Required for tax purposes - like showing ID at a bank
- **Document upload** - Users upload documents (PAN, bank statement) - drag and drop or click to upload
- **Verification status** - Users can see if documents are pending, verified, or rejected - like tracking a package
- **KYC required for withdrawals** - Can't withdraw money until KYC is verified - security measure, like bank verification

#### Match & Score Updates
- **Real-time match scores** - Scores update automatically during live matches - like watching live TV
- **Live match updates** - Ball-by-ball updates, player performances - keeps users engaged
- **Player statistics** - Points earned by each player based on their performance - like a scorecard
- **Match leaderboard** - See how your team ranks in the match - like a race leaderboard
- **Contest leaderboard** - See rankings within a contest - who's winning the prize
- **Points calculation** - System calculates points based on player performance - automatic scoring

#### B2B Features
- B2B customer dashboard
- Custom contest creation
- Branding customization
- Analytics and reporting
- User management for B2B customers

### b) Non-Functional Requirements

#### Performance
- **Responsive Design:** Works great on all devices - mobile, tablet, desktop - like a website that adapts to your screen
- **Fast Load Times:** 
  - **First Contentful Paint (FCP) < 1.0s** - Something appears on screen in under 1 second - feels instant
  - **Largest Contentful Paint (LCP) < 2.0s** - Main content loads in under 2 seconds - page feels ready
  - **Time to Interactive (TTI) < 2.5s** - Page is fully interactive in under 2.5 seconds - can click buttons
  - **Cumulative Layout Shift (CLS) < 0.1** - Page doesn't jump around while loading - smooth experience
- **Asset Optimization:** 
  - **Image compression** - Smaller image files (WebP format) load faster - like compressing photos
  - **Lazy loading** - Images load as you scroll - like Instagram, only loads what you see
  - **Code splitting** - Only loads code for the page you're on - like opening one chapter of a book
  - **Bundle optimization** - Removes unused code, minifies files - like cleaning and compressing
  - **Service Worker caching** - Stores files locally, works offline - like downloading a movie

#### Platform Support
- **Cross-browser:** Works on all major browsers - Chrome, Firefox, Safari, Edge - like a website that works everywhere
- **Device Compatibility:** Works on desktop, tablet, mobile - responsive design adapts to screen size
- **Internet Connectivity:** Handles offline gracefully - shows cached data, works without internet - like offline mode
- **PWA Support:** Can be installed on phone like an app - works offline, push notifications - like a native app

#### Security
- **Authentication/Authorization:** Secure login with JWT tokens - like having a secure key to access your account
- **Data Encryption:** All data sent over HTTPS - encrypted connection, like a secure tunnel
- **Payment Security:** PCI-DSS compliant - payment data is super secure, like a bank vault
- **KYC Security:** Documents stored securely, verified properly - like a secure document locker
- **API Security:** Rate limiting prevents abuse, tokens verify identity - like a bouncer checking IDs

#### Scalability
- **High Availability:** 99.9% uptime - app is almost always available, like a reliable service
- **Load Handling:** Handles thousands of users during match time - when everyone checks scores at once
- **Database Optimization:** Fast queries with proper indexing - like having a well-organized library
- **Caching Strategy:** Redis stores frequently accessed data - like keeping hot food ready
- **CDN:** Static assets served from edge locations - faster loading, like having copies everywhere

#### User Experience
- **Accessibility:** Works with screen readers, keyboard navigation - everyone can use it, like an accessible building
- **Smooth Animations:** 60fps animations - smooth transitions, no lag - like butter
- **Offline Support:** Works offline with cached data - like downloading a movie to watch later
- **Push Notifications:** Browser notifications for match reminders - like getting alerts on your phone
- **Internationalization (i18n):** Multi-language support (future) - can switch languages
- **Localization (l10n):** Regional preferences - date formats, currency - like adapting to local customs

#### Reliability
- **Error Handling:** Shows friendly error messages instead of crashing - like a helpful assistant
- **Logging & Monitoring:** Tracks errors and performance - like having a dashboard to see what's happening
- **A/B Testing:** Test new features with small groups first - like trying a new recipe on a few people
- **Testing:** Unit tests (test small pieces), integration tests (test connections), E2E tests (test full flow) - like quality checks
- **CI/CD Pipeline:** Automatically tests and deploys code - like an assembly line

#### SEO & Marketing
- **SEO Optimization:** Meta tags help Google understand the page - like labels on products
- **Analytics:** Track user behavior - see what users do, where they click - like having a camera in a store
- **Versioning:** API versioning - old apps still work when we update - like backward compatibility
- **PWA:** Can be installed like an app - works offline, push notifications - like a native app

---

## 2. Scope & Priority

### Phase 1: MVP (Must Have) - Priority 1

**Think of this as the core features - what users absolutely need to play fantasy sports**

#### Functional
- **B2C User Features:**
  - **User registration and login** - Users can sign up and log in - basic requirement
  - **View matches** - See scheduled, live, and completed matches - like a sports calendar
  - **Create fantasy teams** - Pick players and create teams - core feature
  - **Join contests** - Join free and paid contests - main gameplay
  - **Payment integration** - Deposit money and join paid contests - enables real-money gaming
  - **Basic KYC** - PAN card verification - required for withdrawals
  - **View leaderboards** - See rankings - competitive element

#### Non-Functional
- **Platform:** Web application built with React.js - modern, fast, interactive
- **Responsive:** Mobile-first design - works great on phones, which is where most users are
- **Performance:** 
  - **Core Web Vitals optimization** - Fast loading, smooth experience - Google's performance standards
  - **Code splitting** - Only loads what you need - faster initial load
  - **Asset optimization** - Compressed images, minified code - smaller files, faster loading
  - **Bundle size optimization** - Removes unused code - like cleaning out your closet
- **Rendering:** Client-side rendering (CSR) - app runs in browser, fast navigation
- **Caching:** Browser caching, Service Worker, API caching - stores data locally, faster access
- **Security:** Authentication, HTTPS, secure payments, XSS protection - keeps user data safe

### Phase 2: Enhanced Features - Priority 2

**After MVP works, add features that make the product better and add new revenue streams**

#### Functional
- **B2B Customer Features:**
  - **B2B dashboard** - Businesses can see their contests, users, analytics - like a control panel
  - **Custom contest creation** - Businesses create their own contests with branding - white-label solution
  - **User management** - Businesses can manage their users - like having admin access
- **Enhanced Team Features:**
  - **Multiple teams per match** - Create multiple teams for same match - increases winning chances
  - **Team sharing** - Share teams with friends - social feature
- **Enhanced Payment:**
  - **Withdrawal functionality** - Users can withdraw winnings - completes the payment cycle
  - **Bank account verification** - Verify bank for withdrawals - security measure
  - **Transaction history** - See all transactions - like a bank statement

#### Non-Functional
- **Performance:** Advanced caching - smarter caching, faster responses
- **Offline Support:** Basic offline functionality - works without internet, shows cached data
- **Push Notifications:** Match reminders, contest updates - keeps users engaged
- **Analytics:** User behavior tracking - understand how users use the app, improve features

### Phase 3: Advanced Features - Priority 3

**Nice-to-have features that add polish and advanced capabilities**

#### Functional
- **Advanced Features:**
  - **Social features** - Team sharing, referrals - users invite friends, get rewards
  - **Advanced analytics for B2B** - Detailed reports, insights - helps businesses make decisions
  - **Multi-language support** - App in multiple languages - reach more users
  - **Advanced KYC features** - More verification options, faster processing

#### Non-Functional
- **Micro-frontend:** If B2B needs heavy customization - separate frontend for B2B
- **Advanced Monitoring:** Real-time dashboards - see what's happening live, like a control room
- **A/B Testing:** Feature flagging - test new features safely, roll out gradually
- **PWA:** Full Progressive Web App - install like an app, works offline, push notifications

---

## 3. Tech Choices

### Frontend Framework
- **React.js:** Modern web application development
  - Component-based architecture with hooks
  - Virtual DOM for efficient rendering
  - Large ecosystem and community support
  - Code splitting with React.lazy() and Suspense
  - Server-side rendering (SSR) capability with Next.js (future)
  - TypeScript support for type safety

### State Management
- **Redux Toolkit (RTK):** Think of it as a global storage box that any component can access
  - **Why Redux?** When you have lots of data (matches, contests, teams) that many components need, Redux keeps it organized
  - **DevTools:** Amazing debugging tool - you can see every state change like watching a movie frame by frame
  - **RTK Query:** Handles API calls automatically - fetches data, caches it, and updates when needed
  - **Thunks:** For async stuff like API calls - Redux's way of handling "wait, let me fetch this first"
- **Context API:** For simple shared stuff like theme (dark/light mode) - lighter than Redux
- **Local State (useState):** For component-specific data - like form inputs that only that component cares about

### API Communication
- **Axios:** Like a smart messenger between your app and the server
  - **Interceptors:** Automatically adds your login token to every request - like signing every letter you send
  - **Error Handling:** Catches problems and shows friendly messages instead of crashing
  - **Request Cancellation:** If user navigates away, stops the request - saves bandwidth

### Navigation
- **React Router v6:** Like GPS for your app - tells it which page to show
  - **Declarative:** You describe what you want, React Router figures out how - like saying "I want to go to matches page"
  - **Route Guards:** Protects pages - like a bouncer checking if you're logged in before letting you in
  - **Deep Linking:** Share a link to a specific match - works like sharing a YouTube video at a specific timestamp
  - **Code Splitting:** Only loads the code for the page you're on - like opening one chapter of a book instead of the whole library

### UI Components & Styling
- **Material-UI (MUI):** Pre-built UI components - like having LEGO blocks that already look good
  - **Why use it?** Saves time - buttons, forms, cards are ready to use
  - **Theming:** Change colors everywhere with one setting - like changing your phone's theme
  - **Accessibility:** Works with screen readers and keyboard - everyone can use it
- **Styled Components:** Write CSS inside your JavaScript - styles travel with the component
  - **Dynamic Styling:** Button changes color based on props - like a chameleon
- **Tailwind CSS (Optional):** Utility classes - like having a toolbox of small CSS pieces you combine

### Payment Gateway
- **Cashfree:** The payment processor - like a cashier that handles all payment methods
  - **Multiple Methods:** UPI, cards, net banking - customers can pay however they want
  - **KYC APIs:** Verifies documents automatically - like a digital ID checker
  - **Secure:** PCI-DSS compliant - your payment data is safe
  - **Webhooks:** Server gets notified when payment succeeds - like getting a receipt automatically

### Build Tools
- **Vite:** Super fast build tool - like having a race car instead of a bicycle
  - **HMR (Hot Module Replacement):** See changes instantly without refreshing - like live preview
  - **Tree Shaking:** Removes unused code - like cleaning out your closet, only keeps what you wear
  - **Minification:** Shrinks code for production - like compressing a file to send faster

### Additional Packages
- **Framer Motion:** Makes animations smooth and easy - like having a professional animator
  - **Declarative:** Describe the animation, it handles the details
- **React Query:** Smart data fetching - remembers what you fetched, updates when needed
  - **Caching:** Like browser cache but smarter - knows when to refresh
  - **Optimistic Updates:** Shows changes immediately, fixes if server says no - feels instant
- **localStorage:** Browser's storage - like a small safe in your browser
- **Service Worker:** Makes app work offline - like downloading a movie to watch without internet
- **React Hook Form:** Makes forms easy - handles validation, errors, submission
- **Zod / Yup:** Validates data - like a bouncer checking IDs before letting data in

### File Storage
- **AWS S3:** Cloud storage for KYC documents, user avatars
  - **Why S3?** Scalable, reliable file storage - don't store files on server
  - **KYC documents** - Store uploaded PAN cards, bank statements securely
  - **CDN integration** - Can serve files through CloudFront for faster access

### Design System
- **Custom Design System:** Based on brand guidelines
  - Color palette
  - Typography
  - Spacing system
  - Component library
  - Icon set

### Backend Framework
- **Node.js + Express.js:** Backend server that handles all business logic
  - **Why Node.js?** JavaScript everywhere - same language for frontend and backend, easier for team
  - **Express.js** - Fast, minimal web framework - like having a lightweight server framework
  - **REST APIs** - Standard REST endpoints for frontend to call
  - **Middleware** - Authentication, validation, error handling - like having helpers that process requests

### Database
- **MongoDB:** NoSQL database for storing user data, matches, contests, teams
  - **Why MongoDB?** Flexible schema - easy to change data structure as requirements change
  - **Document-based** - Stores data as JSON-like documents - matches JavaScript objects
  - **Scalable** - Handles large amounts of data, easy to scale horizontally
  - **Good for** - User profiles, matches, contests, teams - flexible data structures

### Caching & Sessions
- **Redis:** In-memory data store for caching and sessions
  - **Why Redis?** Super fast (in-memory) - perfect for caching frequently accessed data
  - **Caching** - Cache match data, contest data - reduces database load
  - **Sessions** - Store user sessions - faster than database
  - **Rate limiting** - Store rate limit counters - needed for API protection

### Real-time Communication
- **Socket.io (Backend):** WebSocket server for real-time updates
  - **Why Socket.io?** Handles real-time score updates - instant updates to all users
  - **Room-based** - Users join match rooms, get live score updates
  - **Automatic reconnection** - Handles connection drops gracefully

### Authentication & Security
- **JWT (JSON Web Tokens):** For user authentication
  - **Why JWT?** Stateless authentication - server doesn't need to store sessions
  - **Access token** - Short-lived token for API requests
  - **Refresh token** - Long-lived token to get new access tokens
  - **Secure** - Tokens are signed, can't be tampered with

### Testing
- **Jest:** Unit testing framework
- **React Testing Library:** Component testing for React.js
- **Cypress / Playwright:** E2E testing for web applications
- **MSW (Mock Service Worker):** API mocking for tests

### Development Tools
- **ESLint:** Code linting with React plugins
- **Prettier:** Code formatting
- **TypeScript:** Type safety for better developer experience
- **React DevTools:** Browser extension for debugging React components
- **Redux DevTools:** Browser extension for debugging Redux state
- **Chrome DevTools:** Performance profiling and debugging

---

## Architecture Overview

**Think of this as the big picture - how frontend and backend work together**

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
│  │  │  │  Redux Toolkit (State Management)    │  │  │   │
│  │  │  │  - Cart, User, Products, Orders      │  │  │   │
│  │  │  └──────────────────────────────────────┘  │  │   │
│  │  │  ┌──────────────────────────────────────┐  │  │   │
│  │  │  │  Material-UI Components              │  │  │   │
│  │  │  └──────────────────────────────────────┘  │  │   │
│  │  │  ┌──────────────────────────────────────┐  │  │   │
│  │  │  │  Service Worker (PWA/Offline)        │  │  │   │
│  │  │  └──────────────────────────────────────┘  │  │   │
│  │  └────────────────────────────────────────────┘  │   │
│  └──────────────────────────────────────────────────┘   │
└─────────────────────────────────────────────────────────┘
                        │
                        │ HTTP/REST API Calls
                        │ WebSocket (for real-time)
                        ▼
┌─────────────────────────────────────────────────────────┐
│              Backend (Node.js + Express.js)              │
│  (Server that handles business logic and data)          │
├─────────────────────────────────────────────────────────┤
│  ┌──────────────────────────────────────────────────┐   │
│  │         Load Balancer / API Gateway              │   │
│  │  - Routes requests, handles SSL                  │   │
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
│  │         Application Layer                        │   │
│  │  - Authentication (JWT)                          │   │
│  │  - Authorization (Role-based)                    │   │
│  │  - Request Validation                            │   │
│  │  - Rate Limiting                                 │   │
│  └──────────────────────────────────────────────────┘   │
│                        ▼                                 │
│  ┌──────────────────────────────────────────────────┐   │
│  │         Business Logic Layer                     │   │
│  │  - User Service (registration, login)            │   │
│  │  - Match Service (matches, scores)               │   │
│  │  - Contest Service (contests, leaderboards)      │   │
│  │  - Team Service (team creation, validation)      │   │
│  │  - Wallet Service (transactions, payments)       │   │
│  │  - KYC Service (document verification)           │   │
│  └──────────────────────────────────────────────────┘   │
│                        ▼                                 │
│  ┌──────────────────────────────────────────────────┐   │
│  │         Data Access Layer                        │   │
│  │  - MongoDB (User data, matches, contests)        │   │
│  │  - Redis (Caching, sessions)                     │   │
│  └──────────────────────────────────────────────────┘   │
└─────────────────────────────────────────────────────────┘
        │                    │                    │
        ▼                    ▼                    ▼
┌──────────────┐  ┌──────────────┐  ┌──────────────┐
│   MongoDB    │  │    Redis     │  │   External   │
│  (Database)  │  │   (Cache)    │  │   Services   │
│              │  │              │  │  - Cashfree  │
│  - Users     │  │  - Sessions  │  │  - AWS S3    │
│  - Matches   │  │  - Cache     │  │  - Score API │
│  - Contests  │  │  - Rate Lim  │  │              │
│  - Teams     │  │              │  │              │
└──────────────┘  └──────────────┘  └──────────────┘
```

**How it works:**
1. **Frontend (React.js):** User interacts with React app in browser - sees UI, clicks buttons
2. **API Calls:** React app makes HTTP requests to backend API (using Axios)
3. **Backend (Node.js):** Express server receives request, validates, processes business logic
4. **Database:** Backend reads/writes data from MongoDB, caches in Redis
5. **External Services:** Backend calls payment gateway, file storage, score APIs
6. **Response:** Backend sends response back to frontend, React updates UI
7. **Real-time Updates:** For live scores, WebSocket connection for instant updates

---

## Key Design Decisions

1. **React.js for Web:** Modern, component-based framework with excellent ecosystem and performance optimizations
2. **Client-side Rendering (CSR):** React.js SPA approach for fast, interactive user experience without page reloads
3. **Redux Toolkit for State:** Complex state management needs (matches, contests, teams, user) require predictable state management with excellent DevTools support
4. **React Router for Navigation:** Declarative routing with code splitting support for optimal bundle sizes
5. **Material-UI for Components:** Pre-built accessible components with theming support, reducing development time
6. **REST APIs:** Standard, well-understood protocol, easy to integrate with React.js using Axios
7. **Cashfree Payment Gateway:** Supports Indian payment methods and KYC verification with web SDK integration
8. **Mobile-first Responsive Design:** Optimized for mobile devices while providing excellent desktop experience
9. **Code Splitting with React.lazy():** Route-based and component-based code splitting for optimal initial load times
10. **Service Worker for PWA:** Offline functionality and app-like experience with push notifications
11. **TypeScript:** Type safety for better code quality, maintainability, and developer experience
12. **Caching Strategy:** Browser caching, Service Worker caching, and RTK Query for API response caching

