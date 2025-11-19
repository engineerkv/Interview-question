# iGamio Fantasy Sports Platform - High Level Design (HLD)

> **Project Type:** Cross-platform Application (Web + Mobile)  
> **Frontend:** Web (React.js) + Mobile (React Native for Android & iOS)  
> **Backend:** Node.js, Express.js, REST APIs  
> **Tech Stack:** React.js, React Native, Axios, REST APIs, Cashfree Payment Gateway  
> **Team Size:** 2-person team  
> **Built:** From scratch

---

## 1. Requirements

### a) Functional Requirements

#### User Management
- User registration and authentication (Email, Phone, Social Login)
- User profile management
- B2B customer accounts with separate features
- B2C user accounts
- Role-based access control (Admin, B2B, B2C)

#### Sports & Contests
- Support multiple sports: Cricket, Football, Kabaddi
- View scheduled matches (upcoming)
- View live matches (in-progress)
- View completed matches (past results)
- Join real-money contests
- Contest types: Free, Paid, Private, Public
- Contest categories: Head-to-Head, Small League, Mega League

#### Team Management
- Create fantasy teams for matches
- Update teams before match deadline
- View team composition
- Team validation (player selection rules, budget constraints)
- Multiple team creation for same match

#### Payment & Transactions
- Deposit money to wallet
- Withdraw money from wallet
- Join paid contests
- Win amount distribution
- Transaction history
- Payment gateway integration (Cashfree)
- Secure payment processing

#### KYC Verification
- Bank account verification
- PAN card verification
- Document upload
- Verification status tracking
- KYC required for withdrawals

#### Match & Score Updates
- Real-time match scores
- Live match updates
- Player statistics
- Match leaderboard
- Contest leaderboard
- Points calculation

#### B2B Features
- B2B customer dashboard
- Custom contest creation
- Branding customization
- Analytics and reporting
- User management for B2B customers

### b) Non-Functional Requirements

#### Performance
- **Mobile First:** Optimized for mobile devices (Android, iOS)
- **Responsive Design:** Adaptive layouts for different screen sizes
- **Fast Load Times:** 
  - First Contentful Paint (FCP) < 1.5s
  - Largest Contentful Paint (LCP) < 2.5s
  - Time to Interactive (TTI) < 3.5s
  - Cumulative Layout Shift (CLS) < 0.1
- **Asset Optimization:** 
  - Image compression and lazy loading
  - Code splitting and bundle optimization
  - CSS/JS minification

#### Platform Support
- **Cross-platform:** Android, iOS, Web
- **Device Compatibility:** Support for various screen sizes and resolutions
- **Internet Connectivity:** Handle offline scenarios gracefully
- **Location Services:** Optional for location-based features

#### Security
- **Authentication/Authorization:** Secure login and session management
- **Data Encryption:** HTTPS for all API calls
- **Payment Security:** PCI-DSS compliant payment processing
- **KYC Security:** Secure document storage and verification
- **API Security:** Rate limiting, authentication tokens

#### Scalability
- **High Availability:** 99.9% uptime
- **Load Handling:** Support concurrent users during match time
- **Database Optimization:** Efficient queries and indexing
- **Caching Strategy:** Redis for frequently accessed data
- **CDN:** Content delivery for static assets

#### User Experience
- **Accessibility:** WCAG 2.1 AA compliance
- **Smooth Animations:** 60fps animations
- **Offline Support:** Basic offline functionality
- **Push Notifications:** Match reminders, contest updates
- **Internationalization (i18n):** Multi-language support (future)
- **Localization (l10n):** Regional preferences

#### Reliability
- **Error Handling:** Graceful error messages
- **Logging & Monitoring:** Comprehensive logging and error tracking
- **A/B Testing:** Feature flagging for gradual rollouts
- **Testing:** Unit tests, integration tests, E2E tests
- **CI/CD Pipeline:** Automated testing and deployment

#### SEO & Marketing
- **SEO Optimization:** Meta tags, structured data (Web version)
- **Analytics:** User behavior tracking
- **Versioning:** API versioning for backward compatibility
- **PWA:** Progressive Web App features (Web version)

---

## 2. Scope & Priority

### Phase 1: MVP (Must Have) - Priority 1

#### Functional
- **B2C User Features:**
  - User registration and login
  - View matches (scheduled, live, completed)
  - Create fantasy teams
  - Join contests (free and paid)
  - Payment integration (deposit, join contest)
  - Basic KYC (PAN card verification)
  - View leaderboards

#### Non-Functional
- **Platform:** Mobile-first (Android, iOS)
- **Responsive:** Basic responsive design
- **Performance:** 
  - Core Web Vitals optimization
  - Asset optimization (images, CSS, JS)
- **CSR/SSR:** Client-side rendering (React Native)
- **Caching:** Basic API response caching
- **Security:** Authentication, HTTPS, secure payments

### Phase 2: Enhanced Features - Priority 2

#### Functional
- **B2B Customer Features:**
  - B2B dashboard
  - Custom contest creation
  - User management
- **Enhanced Team Features:**
  - Multiple teams per match
  - Team sharing
- **Enhanced Payment:**
  - Withdrawal functionality
  - Bank account verification
  - Transaction history

#### Non-Functional
- **Performance:** Advanced caching strategies
- **Offline Support:** Basic offline functionality
- **Push Notifications:** Match and contest updates
- **Analytics:** User behavior tracking

### Phase 3: Advanced Features - Priority 3

#### Functional
- **Advanced Features:**
  - Social features (team sharing, referrals)
  - Advanced analytics for B2B
  - Multi-language support
  - Advanced KYC features

#### Non-Functional
- **Micro-frontend:** If needed for B2B customization
- **Advanced Monitoring:** Real-time monitoring dashboards
- **A/B Testing:** Feature flagging system
- **PWA:** Full Progressive Web App support

---

## 3. Tech Choices

### Frontend Framework
- **React.js (Web):** Web application development
  - Component-based architecture
  - Virtual DOM for performance
  - Large ecosystem and community
  - SEO-friendly with SSR capabilities
- **React Native (Mobile):** Cross-platform mobile development (Android, iOS)
  - Single codebase for Android and iOS
  - Native performance
  - Code sharing with React.js (business logic)
  - Platform-specific optimizations

### State Management
- **Redux Toolkit (RTK):** Global state management
  - Predictable state updates
  - DevTools support
  - Middleware for async operations
  - Good for complex state (matches, contests, teams, user)

### API Communication
- **Axios:** HTTP client for REST APIs
  - Interceptors for auth tokens
  - Request/response transformation
  - Error handling
  - Request cancellation

### Navigation
- **React Navigation:** Navigation library for React Native
  - Stack, Tab, Drawer navigation
  - Deep linking support
  - Screen transitions

### UI Components & Styling
- **React Native Paper / NativeBase:** Component library
  - Pre-built components
  - Theming support
  - Accessibility features
- **Styled Components / StyleSheet:** Styling approach
  - Component-scoped styles
  - Dynamic styling

### Payment Gateway
- **Cashfree:** Payment gateway integration
  - Supports multiple payment methods
  - KYC verification APIs
  - Secure payment processing
  - Webhook support for payment status

### Build Tools
- **Metro Bundler:** React Native bundler
  - Fast refresh
  - Code splitting
  - Asset optimization

### Additional Packages
- **React Native Reanimated:** Smooth animations
- **React Native Gesture Handler:** Touch gestures
- **React Query / RTK Query:** Server state management and caching
- **AsyncStorage:** Local data persistence
- **React Native Push Notifications:** Push notification handling
- **React Native Image Picker:** Image upload for KYC
- **React Native Document Picker:** Document upload

### Design System
- **Custom Design System:** Based on brand guidelines
  - Color palette
  - Typography
  - Spacing system
  - Component library
  - Icon set

### Backend Integration
- **REST APIs:** Backend communication
  - Standard REST endpoints
  - JSON data format
  - Authentication via JWT tokens

### Testing
- **Jest:** Unit testing
- **React Native Testing Library:** Component testing
- **Detox:** E2E testing

### Development Tools
- **ESLint:** Code linting
- **Prettier:** Code formatting
- **TypeScript (Optional):** Type safety
- **Flipper:** Debugging tool

---

## Architecture Overview

```
┌─────────────────────────────────────────────────────────┐
│                    Frontend Applications                 │
├─────────────────────────────────────────────────────────┤
│  ┌──────────────────────┐  ┌──────────────────────┐    │
│  │   Web (React.js)     │  │  Mobile (React Native)│    │
│  │  ┌────────────────┐  │  │  ┌────────────────┐  │    │
│  │  │   Browser      │  │  │  │  Android + iOS │  │    │
│  │  └────────────────┘  │  │  └────────────────┘  │    │
│  └──────────────────────┘  └──────────────────────┘    │
├─────────────────────────────────────────────────────────┤
│  Shared Business Logic & State Management               │
│  State Management (Redux Toolkit)                       │
│  API Layer (Axios + Interceptors)                       │
│  Navigation (React Router / React Navigation)           │
│  UI Components (Material-UI / React Native Paper)       │
├─────────────────────────────────────────────────────────┤
│  ┌──────────────┐  ┌──────────────┐  ┌──────────────┐  │
│  │   Payment    │  │     KYC      │  │   Real-time  │  │
│  │   Gateway    │  │  Verification│  │   Updates    │  │
│  │  (Cashfree)  │  │              │  │              │  │
│  └──────────────┘  └──────────────┘  └──────────────┘  │
└─────────────────────────────────────────────────────────┘
                        │
                        ▼
┌─────────────────────────────────────────────────────────┐
│              Backend APIs (REST)                         │
│  ┌──────────┐  ┌──────────┐  ┌──────────┐  ┌──────────┐│
│  │   Load   │  │   API    │  │   API    │  │   API    ││
│  │ Balancer │  │ Gateway  │  │  Server  │  │  Server  ││
│  └──────────┘  └──────────┘  └──────────┘  └──────────┘│
└─────────────────────────────────────────────────────────┘
```

---

## Key Design Decisions

1. **React.js for Web + React Native for Mobile:** Separate codebases allow platform-specific optimizations while sharing business logic and API layer
2. **Code Sharing:** Shared utilities, API clients, and business logic between web and mobile for consistency
3. **Redux Toolkit for State:** Complex state management needs (matches, contests, teams, user) require predictable state management across platforms
4. **REST APIs:** Standard, well-understood protocol, easy to integrate with both web and mobile
5. **Cashfree Payment Gateway:** Supports Indian payment methods and KYC verification on both platforms
6. **Mobile-first Approach:** Primary users are on mobile devices, web serves as secondary platform
7. **Client-side Rendering (Web):** React.js uses CSR for web, suitable for interactive applications
8. **Caching Strategy:** API response caching to reduce server load and improve performance on both platforms

