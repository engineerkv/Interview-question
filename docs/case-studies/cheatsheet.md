---
sidebar_label: "Cheatsheet"
sidebar_position: 100
---
# 📁 Projects Interview Cheatsheet

> **Review Time: 15-20 minutes** | **Priority: High** | Quick reference for project discussion interviews

**Quick Review Checklist:**

- [ ] Project overview and tech stack
- [ ] Requirements (functional and non-functional)
- [ ] Component hierarchy and structure
- [ ] Data models and relationships
- [ ] API design and endpoints
- [ ] Key design decisions
- [ ] Interview talking points

---

## 🎯 How to Explain Projects in Interviews

### Structure (2-3 minutes)

1. **Overview (30 seconds)**
   - "I designed [project name], a [type] that [main purpose]"
   - Mention scale if relevant: "It handles [X] users/requests per day"

2. **Requirements (30 seconds)**
   - Core functionality: "The system needs to [key features]"
   - Performance goals: "With requirements like [latency/throughput]"

3. **Component Hierarchy (30 seconds)**
   - "The frontend is a React app with [main components]"
   - "Key components include [component names] for [purpose]"

4. **Data Models (30 seconds)**
   - "The data model centers around [main entities]"
   - "These support [key features]"

5. **API Design (30 seconds)**
   - "The main API endpoints handle [operations]"
   - "For real-time features, we use WebSocket for [events]"

6. **Key Challenges (30 seconds)**
   - "Key challenges include [challenge 1], [challenge 2], [challenge 3]"

---

## 📋 All Projects Quick Reference

### Foundation Systems

#### 1. URL Shortener
- **Focus:** Short URL generation, redirect handling, analytics
- **Key Components:** URLInput, ShortUrlDisplay, AnalyticsDashboard
- **Data Models:** ShortUrl, Analytics
- **Key Challenge:** URL encoding, redirect performance, analytics tracking

#### 2. Search System
- **Focus:** Full-text search, autocomplete, ranking, faceted search
- **Key Components:** SearchBar, SearchResults, Filters
- **Data Models:** SearchResult, SearchQuery
- **Key Challenge:** Fast search, autocomplete, ranking algorithm

#### 3. File Storage System
- **Focus:** File upload, organization, sharing, versioning
- **Key Components:** FileBrowser, FileUploader, FilePreview
- **Data Models:** FileItem, FilePermissions, FileVersion
- **Key Challenge:** Chunked upload, real-time sync, versioning

### Infrastructure Systems

#### 4. Payment System
- **Focus:** Secure payment processing, idempotency, fraud detection
- **Key Components:** PaymentForm, PaymentMethodSelector, PaymentHistory
- **Data Models:** Payment, PaymentMethod, PaymentRequest
- **Key Challenge:** PCI-DSS compliance, idempotency, payment gateway integration

#### 5. Notification System
- **Focus:** Multi-channel delivery, real-time updates, preferences
- **Key Components:** NotificationBell, NotificationDropdown, NotificationSettings
- **Data Models:** Notification, NotificationPreferences, NotificationDelivery
- **Key Challenge:** Real-time delivery, multi-channel support, user preferences

### Content & Media Systems

#### 6. Video Streaming Platform
- **Focus:** Video upload, adaptive streaming, recommendations
- **Key Components:** VideoPlayer, VideoCard, CommentSection
- **Data Models:** Video, Channel, Comment, Playlist
- **Key Challenge:** Adaptive streaming, video processing, CDN delivery

#### 7. Social Media Feed
- **Focus:** Feed generation, real-time engagement, content discovery
- **Key Components:** FeedList, PostCard, PostComposer, CommentSection
- **Data Models:** Post, User, Comment, FeedResponse
- **Key Challenge:** Feed generation, real-time updates, viral posts

#### 11. Time-Limited Content System
- **Focus:** Content expiration, view tracking, countdown timers
- **Key Components:** StoryViewer, StoriesList, CountdownTimer
- **Data Models:** Story, StoryView, StoryReaction
- **Key Challenge:** Automatic expiration, view tracking, cleanup

### E-commerce & Booking Systems

#### 8. E-commerce App
- **Focus:** Product browsing, shopping cart, checkout, orders
- **Key Components:** ProductList, ShoppingCart, CheckoutForm
- **Data Models:** Product, CartItem, Order, Address
- **Key Challenge:** Inventory management, optimistic updates, traffic spikes

#### 12. Ticket Booking System
- **Focus:** Seat selection, booking flow, double booking prevention
- **Key Components:** SeatMap, SeatSelectionPage, BookingForm
- **Data Models:** Event, Seat, Booking, Venue
- **Key Challenge:** Seat locking, real-time availability, concurrency

### Real-Time Communication & Collaboration

#### 9. Chat Messaging System
- **Focus:** Real-time messaging, delivery status, typing indicators
- **Key Components:** ChatWindow, MessageList, MessageInput
- **Data Models:** Conversation, Message, Participant
- **Key Challenge:** Real-time delivery, message ordering, offline handling

#### 10. Real-Time Collaboration System
- **Focus:** Collaborative editing, conflict resolution, presence
- **Key Components:** DocumentEditor, PresencePanel, CommentsPanel
- **Data Models:** Document, Block, Operation, Collaborator
- **Key Challenge:** Operational transformation, real-time sync, conflict resolution

#### 15. Collaborative Spreadsheet
- **Focus:** Real-time spreadsheet editing, formulas, cell synchronization
- **Key Components:** SpreadsheetGrid, CellEditor, FormulaBar
- **Data Models:** Spreadsheet, Sheet, Cell, Formula
- **Key Challenge:** Real-time cell updates, formula evaluation, conflict resolution

#### 16. Collaborative Word Processor
- **Focus:** Real-time document editing, formatting, collaboration
- **Key Components:** DocumentEditor, FormattingToolbar, CollaborationPanel
- **Data Models:** Document, Block, InlineContent, Collaborator
- **Key Challenge:** Real-time editing, formatting sync, conflict resolution

### Geo-Spatial Systems

#### 13. Ride-Sharing System
- **Focus:** Ride matching, real-time tracking, dynamic pricing
- **Key Components:** MapView, RideRequestPanel, ActiveRidePanel
- **Data Models:** Ride, Location, Driver, PriceEstimate
- **Key Challenge:** Geospatial matching, real-time tracking, dynamic pricing

#### 14. Food Delivery System
- **Focus:** Order management, delivery tracking, real-time updates
- **Key Components:** RestaurantList, MenuList, OrderTrackingPage
- **Data Models:** Restaurant, MenuItem, Order, DeliveryPartner
- **Key Challenge:** Real-time tracking, order status, peak hours

### Gaming Systems

#### 17. Real-Time Poker Game
- **Focus:** Multiplayer poker, game state sync, player actions
- **Key Components:** GameTable, PlayerSeat, PlayerActions
- **Data Models:** GameRoom, Player, Hand, Card, PlayerAction
- **Key Challenge:** Real-time sync, action validation, fair gameplay

#### 18. Fantasy Sports Platform
- **Focus:** Team creation, contests, real-time points, leaderboards
- **Key Components:** TeamBuilderPage, LiveMatchPage, Leaderboard
- **Data Models:** Match, Player, FantasyTeam, Contest, LeaderboardEntry
- **Key Challenge:** Real-time points calculation, team validation, leaderboard updates

---

## 🔑 Key Technical Concepts

### Real-time Features
- **WebSocket:** For instant updates (chat, collaboration, notifications)
- **Polling:** For scheduled updates (fantasy sports scheduled matches)
- **Hybrid Approach:** Polling + WebSocket for different states

### State Management
- **React Query:** Server state (API data, caching, refetching)
- **Redux Toolkit:** Global client state (cart, user preferences)
- **Context API:** App-wide settings (theme, auth)
- **useOptimistic:** Instant UI feedback (React 19)

### Performance
- **Code Splitting:** React.lazy for route-based splitting
- **Virtual Scrolling:** For large lists (react-window, react-virtuoso)
- **Lazy Loading:** Images and components
- **Memoization:** React.memo, useMemo, useCallback

### Scalability
- **CDN:** For static assets and media
- **Caching:** Redis for API responses, React Query for client
- **Load Balancing:** Horizontal scaling
- **Database Optimization:** Indexing, sharding, read replicas

### Security
- **PCI-DSS:** Payment data handling
- **Idempotency:** Prevent duplicate operations
- **Server-side Validation:** All critical operations
- **JWT:** Authentication tokens

---

## 💡 Common Interview Questions

### Architecture & Design
- "Walk me through the system architecture"
- "How did you handle scalability?"
- "What were your key design decisions?"
- "How did you ensure data consistency?"

### Technical Challenges
- "What was the most complex problem you solved?"
- "How did you handle [specific challenge]?"
- "What trade-offs did you make?"

### Performance & Optimization
- "How did you optimize performance?"
- "What was your caching strategy?"
- "How did you reduce bundle size?"

### Real-time & State Management
- "How did you handle real-time updates?"
- "How did you manage state across the application?"
- "How did you handle synchronization?"

---

## 🎯 Project-Specific Highlights

### Real-time Systems (Chat, Collaboration, Poker)
- **Key:** WebSocket for instant updates
- **Challenge:** Message ordering, conflict resolution, state sync
- **Solution:** Server-authoritative, operational transformation

### E-commerce & Payment
- **Key:** Inventory management, payment processing
- **Challenge:** Preventing overselling, idempotency
- **Solution:** Atomic operations, optimistic locking

### Geo-spatial Systems (Ride-sharing, Food Delivery)
- **Key:** Location tracking, matching algorithms
- **Challenge:** Real-time location updates, ETA calculation
- **Solution:** Geospatial indexing, WebSocket for tracking

### Content Systems (Video, Social Media, Stories)
- **Key:** Content delivery, feed generation
- **Challenge:** CDN delivery, feed ranking, expiration
- **Solution:** Adaptive streaming, fan-out pattern, TTL storage

---

## 📊 Quick Metrics Reference

### Performance Targets
- **Real-time Updates:** < 100ms latency
- **Page Load:** < 2 seconds
- **API Response:** < 200ms
- **Search Latency:** < 100ms

### Scalability Targets
- **Concurrent Users:** Thousands to millions
- **Throughput:** Millions of requests per day
- **Storage:** Petabytes for content systems
- **Availability:** 99.9% uptime

---

## 🎨 Architecture Patterns

### Component Structure
- **Presentation Layer:** UI Components (buttons, cards, inputs)
- **Feature Components:** Business logic components (forms, lists)
- **Layout Components:** Page structure (header, sidebar, main)

### State Management Pattern
- **Local State:** useState for component-specific UI
- **Global State:** Redux Toolkit for shared state
- **Server State:** React Query for API data
- **Real-time State:** WebSocket for live updates

### API Design Pattern
- **REST:** Standard CRUD operations
- **WebSocket:** Real-time events
- **Pagination:** Cursor-based for large datasets
- **Error Handling:** Consistent error responses

---

## 🔒 Security Checklist

- [ ] Server-side validation for all actions
- [ ] JWT authentication with refresh tokens
- [ ] Rate limiting on APIs
- [ ] Input validation and sanitization
- [ ] HTTPS/WSS for all communications
- [ ] PCI-DSS compliance (for payments)
- [ ] Idempotency keys (for critical operations)

---

## ⚡ Performance Checklist

- [ ] Code splitting implemented
- [ ] Lazy loading for images
- [ ] API response caching
- [ ] Reduced re-renders (memoization)
- [ ] Virtual scrolling for large lists
- [ ] Bundle size optimization
- [ ] CDN for static assets

---

## 📝 Interview Answer Template

### Project Overview Template
```
"I designed [project name], a [type] that [main purpose]. 
The system handles [scale] and uses [key tech]. 
The frontend is a React app with [main components] for [purpose]. 
The data model centers around [entities] that support [features]. 
The main API endpoints handle [operations], and for real-time features, 
we use WebSocket for [events]. Key challenges include [challenges]."
```

### Challenge Explanation Template
```
Situation: [Context and problem]
Action: [Technical approach and implementation]
Result: [Quantifiable outcomes]
Takeaway: [Key learning]
```

---

## 🚀 Quick Tips

1. **Start with Overview:** 30-second project summary
2. **Use Structure:** Requirements → Components → Data Models → APIs
3. **Be Specific:** Use numbers and metrics
4. **Show Trade-offs:** Discuss alternatives considered
5. **Explain Decisions:** Always explain WHY
6. **Admit Challenges:** It's okay to discuss difficulties
7. **Show Learning:** Demonstrate what you learned

---

**Last Updated:** 2024
**Review Before:** System Design Interviews, Project Discussion Rounds
