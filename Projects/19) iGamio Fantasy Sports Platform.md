# iGamio Fantasy Sports Platform

> **Project Type:** Full-Stack Web Application (MERN Stack)
> **Frontend:** React.js Web Application
> **Backend:** Node.js, Express.js, MongoDB, REST APIs
> **Tech Stack:**
> - **Frontend:** React.js, TypeScript, React Router, Redux Toolkit, Axios, Material-UI
> - **Backend:** Node.js, Express.js, MongoDB, Redis, Socket.io, JWT
> - **Services:** Cashfree Payment Gateway, AWS S3 (for file storage)

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

## a) Requirements

### i) Functional Requirements

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

### ii) Non-Functional Requirements

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

## b) Scope and Priority

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

## c) Technology Choices

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

## d) Capacity Estimation

### Throughput Requirements

- **Total Users**: 10 million users
- **Daily Active Users (DAU)**: 5 million users per day
- **Peak Traffic**: 10x average during major sporting events (50 million users per day)
- **Team Selections per Day**: 10 million team selections
- **Contest Joins per Day**: 5 million contest joins
- **Read:Write Ratio**: 20:1 (viewing matches/contests vs creating teams/joining contests)

**Calculations:**
- **Average Writes Per Second (WPS)**: 5M contest joins / 86,400 seconds ≈ 58 WPS
- **Peak WPS**: 58 × 10 = 580 WPS
- **Average Reads Per Second (RPS)**: 58 × 20 = 1,160 RPS
- **Peak RPS**: 1,160 × 10 = 11,600 RPS
- **Concurrent Team Selections**: 1 million concurrent team selections during major events

### Storage Estimation

**Storage per Team Selection:**
- Team metadata: 1 KB (id, userId, matchId, players, points, timestamps)
- Contest join: 500 bytes (contestId, entryFee, status)
- Payment data: 500 bytes (amount, payment method, transaction ID)
- **Total per Team Selection**: ~2 KB

**Storage Requirements:**
- **Team Selections per Year**: 10M selections/day × 365 = 3.65 billion selections
- **Team Storage**: 3.65B × 2 KB ≈ 7.3 TB per year
- **User Data**: 10M users × 5 KB ≈ 50 GB
- **Match Data**: 10K matches/year × 100 KB ≈ 1 GB
- **Contest Data**: 1M contests/year × 1 KB ≈ 1 GB
- **Total Storage**: ~7.3 TB (teams) + 50 GB (users) + 1 GB (matches) + 1 GB (contests) ≈ 7.35 TB/year

### Bandwidth Estimation

- **Average Request Size**: 2 KB per request
- **Average Response Size**: 10 KB per response (match data, contest data, leaderboards)
- **Daily Bandwidth**: 5M requests × (2 KB + 10 KB) = 60 GB/day
- **Peak Bandwidth**: 60 GB × 10 = 600 GB/day during major events
- **Average Bandwidth**: 60 GB / 86,400 seconds ≈ 694 KB/s
- **Peak Bandwidth**: 694 KB/s × 10 ≈ 6.94 MB/s

### Caching Estimation

Following the **80-20 rule** where 20% of matches generate 80% of traffic:
- **Cache 20% of popular matches**: 10K × 0.2 = 2K matches
- **Cache memory required**: 2K matches × 100 KB = 200 MB (distributed across Redis cluster)
- **Cache hit ratio**: 90% (only 10% of match/contest requests hit database)
- **Requests hitting Database**: 1,160 × 0.10 ≈ 116 RPS (manageable with sharding)

### Infrastructure Sizing

- **API Servers**: 500-1,000 instances behind load balancer, each handling 20-50 RPS
- **WebSocket Servers**: 200-500 instances for real-time updates, each handling 2,000-5,000 connections
- **Points Calculation Workers**: 100-200 instances for real-time points calculation
- **Message Queue**: RabbitMQ/Kafka cluster with 20-50 nodes for async processing
- **Database**: MongoDB cluster with 50-100 nodes for storage and high read/write throughput
- **Cache Layer**: Redis cluster with 50-100 nodes for high availability and performance
- **Payment Gateway**: Cashfree with appropriate rate limits

---

## e) Architecture Overview

The system follows a fantasy sports architecture with real-time updates, contest management, and distributed team processing. Here's how the complete system works:

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

---

# 2) Low Level Design (LLD)

## Component Architecture

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

## Frontend Design

### Component Architecture

Think of the frontend as a tree of React components - each component handles a specific part of the UI, and they work together to create the complete user experience.

**Component Hierarchy:**

```
App
├── Header
│   ├── Logo
│   ├── Navigation (Matches, Contests, My Teams, Leaderboard)
│   └── UserMenu (Profile, Wallet, Settings, Sign out)
├── MainContent
│   ├── MatchesPage
│   │   ├── MatchList
│   │   │   └── MatchCard
│   │   │       ├── TeamsInfo
│   │   │       ├── MatchDate
│   │   │       ├── ContestCount
│   │   │       └── CreateTeamButton
│   │   └── FilterBar (Sport, Date, Status)
│   ├── TeamSelectionPage
│   │   ├── MatchInfo
│   │   ├── PlayerPool
│   │   │   ├── PlayerFilters
│   │   │   └── PlayerList
│   │   │       └── PlayerCard
│   │   │           ├── PlayerImage
│   │   │           ├── PlayerName
│   │   │           ├── PlayerStats
│   │   │           ├── PlayerPoints
│   │   │           └── AddToTeamButton
│   │   ├── SelectedTeam
│   │   │   ├── TeamFormation
│   │   │   │   ├── WicketKeeper
│   │   │   │   ├── Batsmen
│   │   │   │   ├── AllRounders
│   │   │   │   └── Bowlers
│   │   │   ├── TeamSummary
│   │   │   │   ├── TotalPlayers
│   │   │   │   ├── RemainingBudget
│   │   │   │   └── TeamValue
│   │   │   └── SaveTeamButton
│   │   └── CaptainViceCaptainSelector
│   ├── ContestsPage
│   │   ├── ContestList
│   │   │   └── ContestCard
│   │   │       ├── ContestName
│   │   │       ├── EntryFee
│   │   │       ├── PrizePool
│   │   │       ├── SpotsFilled
│   │   │       └── JoinButton
│   │   └── CreateContestButton (B2B only)
│   ├── LeaderboardPage
│   │   ├── ContestSelector
│   │   ├── LeaderboardList
│   │   │   └── LeaderboardRow
│   │   │       ├── Rank
│   │   │       ├── UserInfo
│   │   │       ├── TeamName
│   │   │       └── Points
│   │   └── MyRank
│   └── WalletPage
│       ├── Balance
│       ├── TransactionHistory
│       └── AddMoneyButton
└── SocketProvider (Real-time match updates)
```

### Key React Components

**Frontend Implementation:**

```typescript
// Team Selection Component
const TeamSelectionPage: React.FC<{ matchId: string }> = ({ matchId }) => {
  const [selectedPlayers, setSelectedPlayers] = useState<Player[]>([]);
  const [captain, setCaptain] = useState<Player | null>(null);
  const [viceCaptain, setViceCaptain] = useState<Player | null>(null);
  const { data: players } = usePlayers(matchId);

  const handlePlayerSelect = (player: Player) => {
    if (selectedPlayers.length >= 11) return;
    if (selectedPlayers.find(p => p.id === player.id)) return;
    
    setSelectedPlayers(prev => [...prev, player]);
  };

  const handleSaveTeam = () => {
    // Save team with captain and vice-captain
    saveTeamMutation.mutate({
      matchId,
      players: selectedPlayers,
      captain: captain!.id,
      viceCaptain: viceCaptain!.id
    });
  };

  return (
    <div className="team-selection">
      <PlayerPool players={players} onSelect={handlePlayerSelect} />
      <SelectedTeam
        players={selectedPlayers}
        captain={captain}
        viceCaptain={viceCaptain}
        onCaptainSelect={setCaptain}
        onViceCaptainSelect={setViceCaptain}
        onSave={handleSaveTeam}
      />
    </div>
  );
};

// Contest Card Component
const ContestCard: React.FC<{ contest: Contest }> = ({ contest }) => {
  const joinContestMutation = useJoinContest();

  const handleJoin = () => {
    joinContestMutation.mutate(contest.id);
  };

  return (
    <div className="contest-card">
      <h3>{contest.name}</h3>
      <div className="contest-info">
        <div>Entry Fee: ₹{contest.entryFee}</div>
        <div>Prize Pool: ₹{contest.prizePool}</div>
        <div>Spots: {contest.spotsFilled}/{contest.totalSpots}</div>
      </div>
      <button onClick={handleJoin} disabled={contest.spotsFilled >= contest.totalSpots}>
        Join Contest
      </button>
    </div>
  );
};
```

### State Management

**State Management Strategy:**

- **Local State (useState)**: Form inputs, UI state (loading, errors, selected players, filters)
- **Component State**: Each component manages its own UI state
- **API State**: React Query or SWR for server state (matches, players, contests, leaderboard) - caching, refetching
- **Global State (Redux Toolkit)**: User authentication, wallet balance, active teams, selected match

**Frontend Implementation:**

```typescript
// Using React Query for API state management
import { useQuery, useMutation, useQueryClient } from '@tanstack/react-query';

const useMatches = (filters?: MatchFilters) => {
  return useQuery({
    queryKey: ['matches', filters],
    queryFn: async () => {
      const response = await axios.get('/api/v1/matches', { params: filters });
      return response.data;
    },
    staleTime: 5 * 60 * 1000 // Cache for 5 minutes
  });
};

const useJoinContest = () => {
  const queryClient = useQueryClient();
  
  return useMutation({
    mutationFn: async (contestId: string) => {
      const response = await axios.post(`/api/v1/contests/${contestId}/join`);
      return response.data;
    },
    onSuccess: () => {
      // Invalidate contests list
      queryClient.invalidateQueries({ queryKey: ['contests'] });
    }
  });
};
```

### Component Interactions

**Data Flow:**

1. **Match Selection** → User selects match, navigates to TeamSelectionPage
2. **Team Creation** → User selects players, sets captain/vice-captain, saves team
3. **Contest Joining** → User joins contest with saved team, payment processed
4. **Real-time Updates** → Socket.io updates match scores and leaderboard
5. **Leaderboard** → User views contest leaderboard with live rankings

**Event Handling:**

- Player selection updates team formation
- Contest joining triggers payment processing
- Real-time match updates refresh scores
- Leaderboard updates automatically during match
- Wallet transactions update balance

### UI/UX Considerations

- **Loading States**: Show skeleton loaders for matches and contests, spinners for actions
- **Error Handling**: Display user-friendly error messages with retry options
- **Validation**: Client-side validation for team formation rules and budget
- **Responsive Design**: Mobile-first layout, optimized for touch interactions
- **Accessibility**: ARIA labels, keyboard navigation, screen reader support
- **Performance**: Virtual scrolling for long player lists, efficient leaderboard updates, real-time updates via WebSocket

---

## Data Models

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

## Data APIs

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

## Backend Implementation Details

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

## Implementation Details

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

---

## Testing Strategy

### Frontend Testing (React.js)

**Unit Testing:**

- **Jest + React Testing Library** - Test individual components in isolation

- **Test Coverage:** Components, hooks, utilities, reducers

- **Mocking:** Mock API calls, external dependencies, browser APIs

**Integration Testing:**

- **React Testing Library** - Test component interactions

- **Redux Testing** - Test Redux slices and middleware

- **API Integration Tests** - Test API calls with mock server

**E2E Testing:**

- **Cypress / Playwright** - Test complete user flows

- **Test Scenarios:** User registration, team creation, contest joining, payment flow

### Backend Testing (Node.js/Express.js)

**Unit Testing:**

- **Jest + Supertest** - Test API endpoints, services, utilities

- **Test Coverage:** Controllers, services, middleware, utilities

- **Mocking:** Mock database, external APIs, Redis

**Integration Testing:**

- **MongoDB Memory Server** - Test database operations

- **Redis Mock** - Test caching logic

- **API Integration Tests** - Test complete API flows

**Load Testing:**

- **Artillery / k6** - Test API performance under load

- **Test Scenarios:** High concurrent users, peak traffic simulation

---

## Deployment & DevOps

### Frontend Deployment

**Build Process:**

- **Production Build:** `npm run build` - Creates optimized production bundle

- **Code Splitting:** Automatic code splitting for optimal loading

- **Asset Optimization:** Minification, compression, tree-shaking

- **Environment Variables:** `.env.production` for production config

**Deployment Platforms:**

- **Vercel / Netlify** - Automatic deployments from Git

- **AWS S3 + CloudFront** - Static site hosting with CDN

- **Docker Container** - Containerized deployment option

**CI/CD Pipeline:**

- **GitHub Actions / GitLab CI** - Automated testing and deployment

- **Steps:** Lint → Test → Build → Deploy

- **Environment Promotion:** Dev → Staging → Production

### Backend Deployment

**Server Setup:**

- **Node.js Runtime:** Node.js 18+ LTS version

- **Process Manager:** PM2 for process management and auto-restart

- **Reverse Proxy:** Nginx for load balancing and SSL termination

**Deployment Platforms:**

- **AWS EC2 / DigitalOcean** - Virtual server deployment

- **Docker + Kubernetes** - Containerized deployment with orchestration

- **Serverless (AWS Lambda)** - Serverless deployment option

**CI/CD Pipeline:**

- **Automated Testing:** Run tests before deployment

- **Database Migrations:** Run migrations automatically

- **Zero-Downtime Deployment:** Blue-green or rolling deployment

- **Health Checks:** Verify deployment success

### Database Deployment

**MongoDB Setup:**

- **MongoDB Atlas** - Managed MongoDB service (recommended)

- **Self-Hosted:** MongoDB replica set for production

- **Backup Strategy:** Daily automated backups, point-in-time recovery

- **Monitoring:** MongoDB Atlas monitoring or custom monitoring

**Redis Setup:**

- **Redis Cloud / AWS ElastiCache** - Managed Redis service

- **Self-Hosted:** Redis cluster for high availability

- **Persistence:** RDB snapshots + AOF for data durability

---

## Environment Configuration

### Environment Variables

**Frontend (.env):**

```env
REACT_APP_API_URL=https://api.example.com
REACT_APP_SOCKET_URL=wss://socket.example.com
REACT_APP_PAYMENT_GATEWAY_KEY=pk_live_xxx
REACT_APP_ENVIRONMENT=production

```

**Backend (.env):**

```env
NODE_ENV=production
PORT=3000
MONGODB_URI=mongodb://...
REDIS_URL=redis://...
JWT_SECRET=xxx
JWT_REFRESH_SECRET=xxx
PAYMENT_GATEWAY_SECRET=xxx
AWS_ACCESS_KEY_ID=xxx
AWS_SECRET_ACCESS_KEY=xxx
AWS_S3_BUCKET=xxx

```

**Security:**

- **Secrets Management:** Use AWS Secrets Manager / HashiCorp Vault

- **Never Commit Secrets:** Use `.env.example` for reference

- **Environment-Specific Configs:** Separate configs for dev/staging/prod

---

## Database Migrations & Seeding

### MongoDB Migrations

**Migration Strategy:**

- **Manual Scripts:** Node.js scripts for schema changes

- **Migration Tools:** Consider `migrate-mongo` for version control

- **Backward Compatibility:** Ensure migrations are reversible

**Example Migration:**

```typescript
// migrations/add-indexes.js
async function up() {
  await db.collection('matches').createIndex({ matchId: 1, status: 1 });
  await db.collection('contests').createIndex({ contestId: 1, points: -1 });
}

async function down() {
  await db.collection('matches').dropIndex({ matchId: 1, status: 1 });
  await db.collection('contests').dropIndex({ contestId: 1, points: -1 });
}

```

### Data Seeding

**Seed Scripts:**

- **Initial Data:** Seed sports, default contests, admin users

- **Test Data:** Seed test users, matches, contests for development

- **Production Data:** Seed reference data (sports, player positions)

---

## API Documentation

### API Documentation Tools

**Swagger/OpenAPI:**

- **Swagger UI** - Interactive API documentation

- **OpenAPI Spec** - Machine-readable API specification

- **Auto-Generated Docs** - Generate docs from code annotations

**Postman Collection:**

- **API Collection** - Complete API collection with examples

- **Environment Variables** - Pre-configured environments

- **Test Scripts** - Automated API tests

---

## API Versioning

**Versioning Strategy:**

- **URL Versioning:** `/api/v1/matches`, `/api/v2/matches`

- **Header Versioning:** `Accept: application/vnd.api+json;version=1`

- **Backward Compatibility:** Maintain old versions for existing clients

---

## Monitoring & Logging

### Application Monitoring

**Frontend Monitoring:**

- **Error Tracking:** Sentry for frontend error tracking

- **Performance Monitoring:** Web Vitals tracking (LCP, FID, CLS)

- **User Analytics:** Google Analytics / Mixpanel for user behavior

**Backend Monitoring:**

- **APM Tools:** New Relic / Datadog for application performance

- **Error Tracking:** Sentry for backend error tracking

- **Log Aggregation:** ELK Stack (Elasticsearch, Logstash, Kibana) or CloudWatch

### Logging Strategy

**Structured Logging:**

- **Winston / Pino** - Structured logging library

- **Log Levels:** Error, Warn, Info, Debug

- **Log Format:** JSON format for easy parsing

- **Context:** Include request ID, user ID, timestamp

**Log Storage:**

- **CloudWatch Logs** - AWS log storage

- **ELK Stack** - Self-hosted log aggregation

- **Log Rotation:** Automatic log rotation to prevent disk full

### Health Checks

**Health Check Endpoints:**

- **`/health`** - Basic health check

- **`/health/detailed`** - Check database, Redis, external services

- **Monitoring:** Uptime monitoring with Pingdom / UptimeRobot

---

## Database Transactions & Consistency

### MongoDB Transactions

**Transaction Usage:**

- **Multi-Document Transactions** - For operations requiring ACID guarantees

- **Example:** Wallet deposit + transaction record creation

- **Session Management:** Use MongoDB sessions for transaction control

**Example:**

```typescript
const session = await mongoose.startSession();
session.startTransaction();
try {
  await Wallet.updateOne({ userId }, { $inc: { balance: amount } }, { session });
  await Transaction.create([{ userId, amount, type: 'deposit' }], { session });
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

- **Version Field:** Add `version` field to documents

- **Conflict Detection:** Check version before update

- **Retry Logic:** Retry on version conflict

---

## Third-Party Service Integration

### Payment Gateway Integration

**Cashfree Integration:**

- **SDK:** Official Cashfree Node.js SDK

- **Webhooks:** Secure webhook endpoint with signature verification

- **Idempotency:** Unique transaction IDs to prevent duplicates

- **Error Handling:** Comprehensive error handling and retry logic

### AWS S3 Integration

**File Storage:**

- **SDK:** AWS SDK for JavaScript

- **Upload:** Multipart upload for large files

- **Access Control:** Private buckets with signed URLs

- **Lifecycle Policies:** Automatic cleanup of old files

### Socket.io Integration

**Real-time Communication:**

- **Redis Adapter:** Socket.io Redis adapter for scaling

- **Room Management:** Efficient room-based messaging

- **Connection Management:** Handle reconnections, heartbeats

---

# 3) Interview Answers

## Q1. Most complex technical challenge in building the fantasy sports platform

**Situation:** Building a full-stack fantasy sports platform from scratch with a 2-person team, we needed to handle real-time match updates, payment gateway integration, KYC verification, support multiple sports, and ensure the system scales to handle 10,000+ concurrent users during peak match times.

**Action:** The most complex challenge was implementing a scalable real-time system architecture that handles both scheduled and live matches efficiently. **Frontend (React.js):** I implemented a hybrid approach using polling for scheduled matches (every 30 seconds) and WebSocket (Socket.io) for live matches. I created a custom React hook `useMatchUpdates` that manages WebSocket connections, automatically reconnects on disconnection, and batches updates to prevent excessive re-renders. **Backend (Node.js/Express.js):** I implemented a Socket.io server with Redis adapter for horizontal scaling across multiple servers. I used Redis pub/sub to broadcast match updates to all connected clients. For state management, I used Redux Toolkit to synchronize match data, contest updates, and user team changes across the React application. I implemented proper error boundaries and fallback mechanisms.

**Result:** Successfully delivered a stable system that handles real-time updates without performance issues. The app supports 10,000+ concurrent users during peak match times with 99.8% uptime. WebSocket connections handle 5,000+ concurrent connections without server overload. The hybrid approach reduced server load by 60% compared to constant polling. User engagement increased by 35% due to real-time leaderboard updates.

**Takeaway:** Real-time systems require careful architecture decisions - hybrid approaches (polling + WebSocket) work well for different states. Always implement proper connection management, reconnection logic, and horizontal scaling using Redis adapter. Frontend and backend must work together seamlessly for optimal performance.

---

## Q2. Designing the frontend architecture using React.js for scalability and maintainability

**Situation:** The React.js frontend needed to handle complex state management (matches, contests, teams, wallet), support multiple sports, provide smooth navigation, and maintain performance as the application grew in features and users.

**Action:** I designed a scalable React.js architecture with clear separation of concerns. **Frontend (React.js):** I used **Redux Toolkit** for global state management with separate slices for matches, contests, teams, wallet, and user data. I implemented **React Router v6** for client-side routing with code splitting using `React.lazy()` and `Suspense` - each route loads only when needed, reducing initial bundle size by 35%. I created reusable components following the component composition pattern - small, focused components that can be combined (e.g., `MatchCard`, `ContestCard`, `PlayerCard`). I used **Material-UI** for consistent UI components and theming. For performance, I implemented memoization with `React.memo`, `useMemo`, and `useCallback` to prevent unnecessary re-renders. I used **React Query** for server state management (API data caching, automatic refetching) and Redux for client state (UI state, form data). I created custom hooks (`useMatchUpdates`, `useContest`, `useWallet`) to encapsulate business logic and make components cleaner.

**Result:** The frontend architecture supports easy feature additions - adding a new sport takes 2-3 days instead of weeks. Code reusability is 70% across different features. Bundle size reduced from 2.5MB to 1.6MB through code splitting. Initial load time improved from 4s to 2s. The architecture makes it easy for new developers to onboard and contribute.

**Takeaway:** Proper React.js architecture with code splitting, state management separation, and reusable components is crucial for scalability. Use React Query for server state and Redux for client state. Custom hooks encapsulate business logic and improve code reusability.

---

## Q3. Designing the backend architecture using Node.js and Express.js to handle high traffic

**Situation:** The backend needed to handle 10,000+ concurrent users, process real-time match updates, manage payment transactions, handle KYC verifications, and scale horizontally as traffic grows.

**Action:** I designed a scalable Node.js/Express.js backend architecture with multiple layers. **Backend (Node.js/Express.js):** I structured the backend with **separation of concerns** - Routes layer (API endpoints), Controllers layer (business logic), Services layer (data access and external API calls), and Models layer (MongoDB schemas). I implemented **middleware** for authentication (JWT verification), authorization (role-based access control), request validation (using Joi), error handling, and rate limiting. I used **MongoDB** for primary data storage with proper indexing on frequently queried fields (userId, matchId, contestId). I implemented **Redis caching** for frequently accessed data (match lists, player data, leaderboards) with 5-minute TTL to reduce database load. I used **Socket.io with Redis adapter** for horizontal scaling - multiple Express servers can share WebSocket connections through Redis pub/sub. I implemented **connection pooling** for MongoDB and Redis. I added **request logging** and **monitoring** to track API performance and identify bottlenecks.

**Result:** API response times improved from 2-3 seconds to 200-300ms during peak times. The backend handles 15,000+ concurrent connections without issues. Server costs reduced by 40% due to caching. The architecture supports horizontal scaling - we can add more Express servers behind a load balancer. Zero downtime deployments with proper health checks.

**Takeaway:** Layered architecture with proper separation of concerns makes the backend maintainable and scalable. Caching with Redis is essential for high-traffic applications. Socket.io with Redis adapter enables horizontal scaling for real-time features. Always implement proper monitoring and logging.

---

## Q4. Implementing real-time match updates using Socket.io on both frontend and backend

**Situation:** Users needed to see live match scores, player statistics, and contest leaderboards updating in real-time without page refreshes, while ensuring the system scales to handle thousands of concurrent connections.

**Action:** **Backend (Node.js/Express.js):** I set up a Socket.io server integrated with Express.js. I implemented authentication middleware for Socket.io connections - clients send JWT token during handshake, server validates it before allowing connection. I used **Redis adapter** for Socket.io to enable horizontal scaling - multiple Express servers share WebSocket connections through Redis pub/sub. I created room-based messaging - users join match-specific rooms (`match:${matchId}`), and when match data updates, server broadcasts to all users in that room. I implemented heartbeat mechanism to detect and clean up dead connections. **Frontend (React.js):** I created a Socket.io client connection using the `socket.io-client` library. I created a custom React hook `useMatchUpdates` that manages the Socket.io connection, handles reconnection automatically, and updates Redux state when receiving match updates. I implemented connection status indicators and fallback to polling if WebSocket fails. I used `useEffect` cleanup to disconnect Socket.io when component unmounts.

**Result:** Real-time updates work seamlessly with less than 1-second latency for live matches. The system handles 5,000+ concurrent WebSocket connections during peak times. Automatic reconnection ensures 99% connection success rate. Users see live score updates instantly without refreshing. The Redis adapter allows scaling to multiple servers without connection issues.

**Takeaway:** Socket.io with Redis adapter is essential for scalable real-time systems. Room-based messaging reduces unnecessary broadcasts. Always implement reconnection logic and fallback mechanisms on the frontend. Proper cleanup prevents memory leaks.

---

## Q5. Handling state management complexity using Redux Toolkit in React.js

**Situation:** The application had complex state requirements - matches data, contests, user teams, wallet balance, authentication state, and UI state needed to be shared across multiple components and screens.

**Action:** I implemented **Redux Toolkit** for global state management with a well-organized store structure. I created separate slices for different domains - `authSlice` (user authentication, JWT tokens), `matchesSlice` (match data, live scores), `contestsSlice` (contest data, leaderboards), `teamsSlice` (user teams, team creation state), `walletSlice` (balance, transactions), and `uiSlice` (loading states, errors, notifications). I used **RTK Query** for API calls - it automatically handles caching, refetching, and state updates. I implemented **normalized state** structure to avoid data duplication (e.g., storing players by ID in a map). I used **selectors** with `createSelector` for computed values (e.g., total wallet balance, contest statistics). I implemented **middleware** for logging actions in development and handling async actions. I used **Redux DevTools** for debugging state changes. For local component state, I used `useState` for simple UI state (modals, dropdowns) and Redux for shared state.

**Result:** State management is now predictable and maintainable. Adding new features is easier - just add a new slice. Debugging is easier with Redux DevTools. State updates are consistent across the application. The normalized state structure prevents data inconsistencies. RTK Query reduced API call code by 60%.

**Takeaway:** Redux Toolkit simplifies Redux boilerplate and makes state management more maintainable. Use RTK Query for server state, Redux for client state. Normalized state structure prevents data duplication. Proper slice organization makes the codebase scalable.

---

