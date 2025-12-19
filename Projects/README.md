# 📁 Projects Directory

This directory contains detailed project documentation following High Level Design (HLD) and Low Level Design (LLD) approaches, along with interview questions about complex problems solved.

## 🎤 Interview Guide

### How to Explain Projects in Interviews

**1. Project Overview (30 seconds)**

- Start with: "I built [project name], a [type] that [main purpose]"
- Mention scale: "It handles [X] users/requests per day"
- Key tech: "Built with [tech stack]"

**2. Technical Challenges (2-3 minutes)**

- Pick 2-3 most interesting challenges
- Use STAR method: Situation → Action → Result → Takeaway
- Include numbers: "Reduced latency by 50%", "Handles 10,000+ concurrent users"

**3. Architecture Decisions (1-2 minutes)**

- Explain key choices: "I chose [X] because [reason]"
- Discuss trade-offs: "The trade-off was [Y], but it was worth it because [Z]"
- Be ready to draw diagrams

**4. What You Learned (30 seconds)**

- Key insights: "I learned that [insight]"
- What you'd do differently: "If I rebuilt it, I would [improvement]"

### STAR Method Template

**Situation:** Context and problem

- "We needed to [goal] but faced [challenge]"

**Action:** Technical approach

- "I implemented [solution] using [technology/approach]"

**Result:** Quantifiable outcomes

- "This resulted in [metric improvement]"

**Takeaway:** Key learning

- "I learned that [insight]"

## 📋 Structure

Each project includes:

- **High Level Design (HLD)** - Requirements, Scope, Tech Choices, Architecture

- **Low Level Design (LLD)** - Component Architecture, Data Models, APIs, Protocols, Implementation

- **Interview Answers** - Complete STAR method answers to all interview questions

All sections are combined in a single markdown file per project.

## ⚡ Optional Features (Add When Applicable)

These features can be added to projects where they make sense. Not all features apply to all projects.

**How to Use:**

- Review the "Optional Features" listed for each project
- Add features that make sense for your use case
- Don't add features just to have them - each should solve a real problem
- In interviews, mention these as "enhancements I would add" or "optimizations I implemented"

### Frontend Performance

- **Image Optimization**: Lazy loading, WebP format, responsive images, compression
- **Code Splitting**: Route-based (React.lazy), component-based, dynamic imports
- **Debouncing/Throttling**: Search input, scroll events, resize handlers
- **Virtual Scrolling**: Large lists (react-window, react-virtualized)
- **Memoization**: React.memo, useMemo, useCallback for expensive operations
- **Bundle Optimization**: Tree shaking, chunk splitting, bundle analysis

### User Experience

- **Infinite Scroll**: Pagination alternative for feeds/lists
- **Skeleton Loading**: Better perceived performance
- **Error Boundaries**: Graceful error handling
- **Progressive Web App (PWA)**: Offline support, push notifications
- **Dark Mode**: Theme switching
- **Accessibility**: ARIA labels, keyboard navigation, screen reader support

### Backend Performance

- **Request Batching**: Combine multiple requests
- **Connection Pooling**: Database connection management
- **Query Optimization**: Indexing, query analysis, N+1 prevention
- **Background Jobs**: Async processing with queues
- **Rate Limiting**: API protection (per user/endpoint)

### Real-Time Features

- **WebSocket Reconnection**: Auto-reconnect with exponential backoff
- **Optimistic Updates**: Instant UI feedback
- **Conflict Resolution**: For collaborative features
- **Presence Indicators**: Show who's online/active

### Caching Strategies

- **Browser Caching**: Cache-Control headers
- **CDN Caching**: Static asset delivery
- **Application Caching**: Redis for hot data
- **Service Worker**: Offline-first approach

### Security Enhancements

- **Input Sanitization**: XSS prevention
- **CSRF Protection**: Token-based protection
- **Content Security Policy**: XSS mitigation
- **Rate Limiting**: DDoS protection
- **Encryption**: Data at rest and in transit

### Monitoring & Analytics

- **Error Tracking**: Sentry, LogRocket
- **Performance Monitoring**: Web Vitals, Lighthouse
- **User Analytics**: Event tracking, user behavior
- **A/B Testing**: Feature flags, experimentation

## 🎯 Projects

Projects are organized in logical order: Foundation → Full-Stack Apps → Real-Time Systems → Specialized Systems → Infrastructure → System Design → Specific Examples

### Foundation Systems

### 1. URL Shortener

- **Type:** Full-Stack Web Application (MERN Stack)

- **Tech Stack:** React.js, Node.js, Express.js, MongoDB, Redis, CDN

- **Key Focus:** URL encoding, redirect handling, analytics, caching strategies

- **Optional Features:** Code splitting, debouncing (analytics input), CDN caching, error boundaries

- **File:** [01) URL Shortener.md](01%20URL%20Shortener.md)

### Full-Stack Web Applications

### 2. E-commerce App

- **Type:** Full-Stack Web Application (MERN Stack)

- **Tech Stack:** React.js, Node.js, Express.js, MongoDB, Redis, Elasticsearch, Payment Gateway

- **Key Focus:** Product search, shopping cart, payment processing, inventory management

- **Optional Features:** Image optimization, code splitting, debouncing (search), virtual scrolling, infinite scroll, skeleton loading, PWA support

- **File:** [03) E-commerce App.md](03%20E-commerce%20App.md)

### 3. Social Media Feed

- **Type:** Full-Stack Web Application (MERN Stack)

- **Tech Stack:** React.js, Node.js, Express.js, MongoDB, Redis, Socket.io, Elasticsearch, AWS S3

- **Key Focus:** Feed generation, ranking algorithm, fan-out pattern, real-time updates

- **Optional Features:** Image optimization, infinite scroll, virtual scrolling, optimistic updates, skeleton loading, presence indicators, dark mode

- **File:** [04) Social Media Feed.md](04%20Social%20Media%20Feed.md)

### 4. Video Streaming Platform

- **Type:** Full-Stack Web Application (MERN Stack)

- **Tech Stack:** React.js, Node.js, Express.js, MongoDB, Redis, Elasticsearch, AWS S3, CloudFront, FFmpeg

- **Key Focus:** Video upload, transcoding, adaptive streaming, content recommendation

- **Optional Features:** Code splitting, infinite scroll, skeleton loading, PWA support, background jobs (transcoding), CDN caching, error boundaries

- **File:** [05) Video Streaming Platform.md](05%20Video%20Streaming%20Platform.md)

### Real-Time Systems

### 5. Chat Messaging System

- **Type:** Full-Stack Web Application (MERN Stack)

- **Tech Stack:** React.js, Node.js, Express.js, MongoDB, Redis, Socket.io, WebSocket

- **Key Focus:** Real-time messaging, offline handling, group messaging, message ordering

- **Optional Features:** Virtual scrolling (message list), optimistic updates, WebSocket reconnection, presence indicators, image optimization (media sharing), PWA support, debouncing (typing indicators)

- **File:** [06) Chat Messaging System.md](06%20Chat%20Messaging%20System.md)

### 6. Notification System

- **Type:** Full-Stack System Component (MERN Stack)

- **Tech Stack:** React.js, Node.js, Express.js, MongoDB, Redis, Socket.io Server, Message Queue (RabbitMQ/Kafka)

- **Key Focus:** Multi-channel delivery, real-time notifications, user preferences, reliable delivery

- **Optional Features:** Virtual scrolling (notification list), optimistic updates, WebSocket reconnection, background jobs (delivery), rate limiting, PWA push notifications

- **File:** [07) Notification System.md](07%20Notification%20System.md)

### Specialized Systems

### 7. Time-Limited Content System

- **Type:** Full-Stack Web Application (MERN Stack)

- **Tech Stack:** React.js, Node.js, Express.js, MongoDB, Redis, CDN

- **Key Focus:** Content expiration, TTL storage, automatic cleanup, view tracking

- **Optional Features:** Image optimization, infinite scroll, skeleton loading, background jobs (cleanup), CDN caching, code splitting

- **File:** [08) Time-Limited Content System.md](08%20Time-Limited%20Content%20System.md)

### 8. Real-Time Collaboration System

- **Type:** Full-Stack Web Application (MERN Stack)

- **Tech Stack:** React.js, Node.js, Express.js, MongoDB, Redis, Socket.io, OT/CRDT

- **Key Focus:** Real-time editing, conflict resolution, operational transformation, version control

- **Optional Features:** Optimistic updates, WebSocket reconnection, presence indicators, debouncing (auto-save), code splitting, error boundaries, PWA support

- **File:** [09) Real-Time Collaboration System.md](09%20Real-Time%20Collaboration%20System.md)

### 9. Ride-Sharing System

- **Type:** Full-Stack Web Application (MERN Stack)

- **Tech Stack:** React.js, Node.js, Express.js, MongoDB, Redis, Socket.io, Geo-spatial DB

- **Key Focus:** Ride matching, real-time location tracking, ETA calculation, dynamic pricing

- **Optional Features:** Code splitting, WebSocket reconnection, throttling (location updates), PWA support, background jobs (matching), error boundaries, skeleton loading

- **File:** [10) Ride-Sharing System.md](10%20Ride-Sharing%20System.md)

### 10. Food Delivery System

- **Type:** Full-Stack Web Application (MERN Stack)

- **Tech Stack:** React.js, Node.js, Express.js, MongoDB, Redis, Socket.io, Geo-spatial DB

- **Key Focus:** Order management, delivery partner assignment, real-time tracking, inventory management

- **Optional Features:** Image optimization (restaurant/menu images), code splitting, infinite scroll, WebSocket reconnection, throttling (location updates), skeleton loading, PWA support, background jobs (order processing)

- **File:** [11) Food Delivery System.md](11%20Food%20Delivery%20System.md)

> **Note:** Ride-Sharing and Food Delivery share similar geospatial matching patterns but differ in core business logic (ride matching vs order fulfillment, dynamic pricing vs fixed pricing, driver management vs restaurant management).

### Infrastructure Systems

### 11. Payment System

- **Type:** Full-Stack Web Application (MERN Stack)

- **Tech Stack:** React.js, Node.js, Express.js, MongoDB/PostgreSQL, Redis, Payment Gateway SDKs

- **Key Focus:** Payment processing, idempotency, webhooks, fraud detection, transaction reliability

- **Optional Features:** Code splitting, error boundaries, rate limiting, background jobs (webhook processing), request batching, connection pooling, security enhancements (CSRF, encryption)

- **File:** [12) Payment System.md](12%20Payment%20System.md)

> **Note:** Payment System focuses on payment infrastructure (idempotency, webhooks, fraud detection), while E-commerce App includes payment as one feature within a larger shopping platform.

### 12. File Storage System

- **Type:** Full-Stack Web Application (MERN Stack)

- **Tech Stack:** React.js, Node.js, Express.js, MongoDB, AWS S3, CDN

- **Key Focus:** File upload, chunking, deduplication, versioning, synchronization

- **Optional Features:** Code splitting, virtual scrolling (file list), image optimization (thumbnails), PWA support, background jobs (sync), CDN caching, progress indicators, error boundaries

- **File:** [13) File Storage System.md](13%20File%20Storage%20System.md)

### 13. Search System

- **Type:** Full-Stack Web Application (MERN Stack)

- **Tech Stack:** React.js, Node.js, Express.js, MongoDB, Elasticsearch, Redis

- **Key Focus:** Full-text search, autocomplete, ranking, faceted search, indexing

- **Optional Features:** Debouncing (search input), throttling (autocomplete), virtual scrolling (results), skeleton loading, infinite scroll, code splitting, caching strategies

- **File:** [14) Search System.md](14%20Search%20System.md)

> **Note:** Search System focuses on search infrastructure, while E-commerce App includes product search as one feature.

### 14. Ticket Booking System

- **Type:** Full-Stack Web Application (MERN Stack)

- **Tech Stack:** React.js, Node.js, Express.js, MongoDB, Redis, Message Queue

- **Key Focus:** Seat locking, booking flow, double booking prevention, concurrent seat selection

- **Optional Features:** Code splitting, optimistic updates, skeleton loading, error boundaries, rate limiting, background jobs (cleanup), WebSocket (real-time seat updates)

- **File:** [17) Ticket Booking System.md](17%20Ticket%20Booking%20System.md)

### Real-World Examples

### 15. iGamio Fantasy Sports Platform

- **Type:** Full-Stack Web Application (MERN Stack)

- **Tech Stack:** React.js, Node.js, Express.js, MongoDB, Redis, Socket.io, Cashfree, AWS S3

- **Key Focus:** Real-time match updates, payment integration, KYC verification, B2B/B2C support, multi-sport architecture

- **Optional Features:** Image optimization, code splitting, virtual scrolling, memoization, bundle optimization, WebSocket reconnection, optimistic updates, skeleton loading

- **File:** [19) iGamio Fantasy Sports Platform.md](19%20iGamio%20Fantasy%20Sports%20Platform.md)

### 16. Real-Time Poker Game

- **Type:** Full-Stack Web Application (MERN Stack)

- **Tech Stack:** React.js, TypeScript, Socket.io, Node.js, Express.js, MongoDB, Redis

- **Key Focus:** Real-time multiplayer synchronization, server-authoritative game logic, anti-cheating, network latency handling

- **Optional Features:** Code splitting, image optimization, virtual scrolling, memoization, WebSocket reconnection, optimistic updates, error boundaries, bundle optimization

- **File:** [20) Real-Time Poker Game.md](20%20Real-Time%20Poker%20Game.md)

## 📖 Design Document Structure

### High Level Design (HLD)

1. **Requirements**
   - Functional Requirements
   - Non-Functional Requirements

2. **Scope & Priority**
   - Phase 1: MVP (Must Have)
   - Phase 2: Enhanced Features
   - Phase 3: Advanced Features

3. **Tech Choices**
   - Frontend Framework
   - State Management
   - API Communication
   - Additional Tools & Libraries

4. **Architecture Overview**
   - System architecture diagrams
   - Component interactions
   - Data flow

5. **Key Design Decisions**
   - Rationale for technology choices
   - Trade-offs considered

### Low Level Design (LLD)

1. **Component Architecture**
   - Component hierarchy
   - Data sharing strategy
   - State management approach

2. **Data Models**
   - TypeScript/JavaScript interfaces
   - Database schemas
   - Data structure definitions

3. **Data APIs**
   - REST API endpoints
   - Request/Response formats
   - Status codes
   - WebSocket events (if applicable)

4. **Backend Implementation Details**
   - Server structure
   - Database operations
   - Caching strategies
   - Error handling

5. **Implementation Details**
   - Pagination
   - Debouncing/Throttling
   - Error Handling
   - Caching Strategy
   - Code examples

6. **Protocols**
   - API protocols (REST, GraphQL, etc.)
   - Authentication protocols
   - Real-time communication protocols

### Interview Answers

All answers follow the **STAR method**:

- **Situation**: Context and problem

- **Action**: Technical approach and implementation

- **Result**: Quantifiable outcomes and impact

- **Takeaway**: Key learnings and insights

## 🎤 Interview Questions

Each project includes interview questions covering:

- Complex technical challenges

- Architecture decisions

- Performance optimizations

- Scalability solutions

- Problem-solving approaches

See [question.md](question.md) for the complete list of questions for all projects.

## 📝 Usage

1. **For Interviews:**
   - Review the HLD to understand project scope
   - Study the LLD for technical details
   - Practice answering the interview questions using STAR method
   - **How to Explain Projects:**
     - Start with a 30-second overview: "I built [project name], a [type] that [main purpose]. It handles [scale] and uses [key tech]."
     - Focus on challenges, not just features: "The biggest challenge was [X], which I solved by [Y]."
     - Use numbers: "Reduced load time by 50%", "Handles 10,000+ concurrent users"
     - Explain trade-offs: "I chose [X] over [Y] because [reason], though it meant [trade-off]."
     - Be ready to draw architecture diagrams

2. **For System Design:**
   - Use HLD as a template for new projects
   - Follow LLD structure for detailed design
   - Reference implementation details for coding

3. **For Learning:**
   - Understand real-world project structure
   - Learn design patterns and best practices
   - See practical implementation examples

## 🔄 Handling Overlapping Projects

Some projects share similar patterns but have distinct focuses:

### Ride-Sharing vs Food Delivery

- **Similar:** Geospatial matching, real-time tracking, ETA calculation
- **Different:**
  - Ride-Sharing: Dynamic pricing, driver-rider matching, ride lifecycle
  - Food Delivery: Order management, restaurant inventory, multi-party coordination (user-restaurant-delivery partner)

### Payment System vs E-commerce App

- **Similar:** Payment processing, gateway integration
- **Different:**
  - Payment System: Focus on payment infrastructure (idempotency, webhooks, fraud detection, transaction reliability)
  - E-commerce App: Payment is one feature within shopping cart, inventory, search, and order management

### Search System vs E-commerce App

- **Similar:** Product search functionality
- **Different:**
  - Search System: Focus on search infrastructure (indexing, ranking algorithms, autocomplete, faceted search)
  - E-commerce App: Search is one feature within product catalog, cart, and checkout flow

## 🔍 Quick Reference

- **Question List:** [question.md](question.md)

- **Cheatsheet:** [Projects Interview Cheatsheet.md](Projects%20Interview%20Cheatsheet.md)

- **Answer Format:** STAR method (Situation, Action, Result, Takeaway)
