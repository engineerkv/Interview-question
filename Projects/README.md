# 📁 Projects Directory

This directory contains detailed **frontend system design** documentation following High Level Design (HLD) and Low Level Design (LLD) approaches, along with interview questions about complex frontend problems solved.

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
- **Debouncing/Throttling**: Search input, scroll events, resize handlers (useDeferredValue, useTransition)
- **Virtual Scrolling**: Large lists (@tanstack/react-virtual)
- **Memoization**: React.memo, useMemo, useCallback for expensive operations
- **Bundle Optimization**: Tree shaking, chunk splitting, bundle analysis

### User Experience

- **Infinite Scroll**: Pagination alternative for feeds/lists
- **Skeleton Loading**: Better perceived performance
- **Error Boundaries**: Graceful error handling
- **Progressive Web App (PWA)**: Offline support, push notifications
- **Dark Mode**: Theme switching
- **Accessibility**: ARIA labels, keyboard navigation, screen reader support

### Real-Time Features

- **WebSocket Reconnection**: Auto-reconnect with exponential backoff
- **Optimistic Updates**: Instant UI feedback (useOptimistic)
- **Conflict Resolution**: For collaborative features
- **Presence Indicators**: Show who's online/active

### Caching Strategies

- **Browser Caching**: Cache-Control headers
- **CDN Caching**: Static asset delivery
- **React Query Caching**: Server state caching
- **Service Worker**: Offline-first approach

### Security Enhancements

- **Input Sanitization**: XSS prevention (React escaping)
- **CSRF Protection**: Token-based protection (SameSite cookies)
- **Content Security Policy**: XSS mitigation
- **Secure Storage**: httpOnly cookies for tokens

### Monitoring & Analytics

- **Error Tracking**: Sentry for frontend errors
- **Performance Monitoring**: Web Vitals, Lighthouse
- **User Analytics**: Event tracking, user behavior
- **A/B Testing**: Feature flags, experimentation

## 🎯 Projects

Projects are organized in logical order for interview preparation: **Foundation Systems** → **Infrastructure Systems** → **Full-Stack Web Applications** → **Real-Time Systems** → **Specialized Systems** → **Geo-Spatial Systems** → **Real-World Examples**

### Foundation Systems

### 1. URL Shortener

- **Type:** Frontend System Design

- **Tech Stack:** React 19, TypeScript, React Query, Redux Toolkit, React Router, Vite

- **Key Focus:** URL validation, form handling, analytics dashboard, state management

- **Optional Features:** Code splitting, debouncing (analytics input), CDN caching, error boundaries

- **File:** [01) URL Shortener.md](01%20URL%20Shortener.md)

### 2. Search System

- **Type:** Frontend System Design

- **Tech Stack:** React 19, TypeScript, React Query, Redux Toolkit, React Router, Vite

- **Key Focus:** Search interface, autocomplete, result rendering, filtering UI, state management

- **Optional Features:** Debouncing (search input), throttling (autocomplete), virtual scrolling (results), skeleton loading, infinite scroll, code splitting

- **File:** [02) Search System.md](02%20Search%20System.md)

> **Note:** Search System focuses on search interface design, while E-commerce App includes product search as one feature.

### 3. File Storage System

- **Type:** Frontend System Design

- **Tech Stack:** React 19, TypeScript, React Query, Redux Toolkit, React Router, Vite

- **Key Focus:** File upload UI, file browser interface, progress tracking, file preview, state management

- **Optional Features:** Code splitting, virtual scrolling (file list), image optimization (thumbnails), PWA support, CDN caching, progress indicators, error boundaries

- **File:** [03) File Storage System.md](03%20File%20Storage%20System.md)

### Infrastructure Systems

### 4. Payment System

- **Type:** Frontend System Design

- **Tech Stack:** React 19, TypeScript, React Query, Redux Toolkit, React Router, Vite

- **Key Focus:** Payment form handling, payment gateway integration, transaction status UI, state management

- **Optional Features:** Code splitting, error boundaries, security enhancements (CSRF protection, input validation)

- **File:** [04) Payment System.md](04%20Payment%20System.md)

> **Note:** Payment System focuses on payment form handling and gateway integration UI, while E-commerce App includes payment as one feature within a larger shopping platform.

### 5. Notification System

- **Type:** Frontend System Design

- **Tech Stack:** React 19, TypeScript, React Query, Redux Toolkit, Socket.io Client, React Router, Vite

- **Key Focus:** Notification center UI, real-time notification handling, preference management, state management

- **Optional Features:** Virtual scrolling (notification list), optimistic updates, WebSocket reconnection, PWA push notifications

- **File:** [05) Notification System.md](05%20Notification%20System.md)

### Full-Stack Web Applications

### 6. E-commerce App

- **Type:** Frontend System Design

- **Tech Stack:** React 19, TypeScript, React Query, Redux Toolkit, React Router, Vite

- **Key Focus:** Product search interface, shopping cart management, checkout flow, state management

- **Optional Features:** Image optimization, code splitting, debouncing (search), virtual scrolling, infinite scroll, skeleton loading, PWA support

- **File:** [06) E-commerce App.md](06%20E-commerce%20App.md)

### 7. Social Media Feed

- **Type:** Frontend System Design

- **Tech Stack:** React 19, TypeScript, React Query, Redux Toolkit, Socket.io Client, React Router, Vite

- **Key Focus:** Feed rendering, infinite scroll, real-time updates, post interactions, state management

- **Optional Features:** Image optimization, infinite scroll, virtual scrolling, optimistic updates, skeleton loading, presence indicators, dark mode

- **File:** [07) Social Media Feed.md](07%20Social%20Media%20Feed.md)

### 8. Video Streaming Platform

- **Type:** Frontend System Design

- **Tech Stack:** React 19, TypeScript, React Query, Redux Toolkit, Video.js, React Router, Vite

- **Key Focus:** Video player integration, adaptive streaming, playlist management, watch history, state management

- **Optional Features:** Code splitting, infinite scroll, skeleton loading, PWA support, CDN caching, error boundaries

- **File:** [08) Video Streaming Platform.md](08%20Video%20Streaming%20Platform.md)

### Real-Time Systems

### 9. Chat Messaging System

- **Type:** Frontend System Design

- **Tech Stack:** React 19, TypeScript, React Query, Redux Toolkit, Socket.io Client, React Router, Vite

- **Key Focus:** Real-time messaging interface, message rendering, typing indicators, offline handling, state management

- **Optional Features:** Virtual scrolling (message list), optimistic updates, WebSocket reconnection, presence indicators, image optimization (media sharing), PWA support, debouncing (typing indicators)

- **File:** [09) Chat Messaging System.md](09%20Chat%20Messaging%20System.md)

### 10. Real-Time Collaboration System

- **Type:** Frontend System Design

- **Tech Stack:** React 19, TypeScript, React Query, Redux Toolkit, Socket.io Client, React Router, Vite

- **Key Focus:** Real-time editing interface, conflict resolution UI, presence indicators, state management

- **Optional Features:** Optimistic updates, WebSocket reconnection, presence indicators, debouncing (auto-save), code splitting, error boundaries, PWA support

- **File:** [10) Real-Time Collaboration System.md](10%20Real-Time%20Collaboration%20System.md)

### Specialized Systems

### 11. Time-Limited Content System

- **Type:** Frontend System Design

- **Tech Stack:** React 19, TypeScript, React Query, Redux Toolkit, React Router, Vite

- **Key Focus:** Content display with expiration, view tracking, countdown timers, state management

- **Optional Features:** Image optimization, infinite scroll, skeleton loading, CDN caching, code splitting

- **File:** [11) Time-Limited Content System.md](11%20Time-Limited%20Content%20System.md)

### 12. Ticket Booking System

- **Type:** Frontend System Design

- **Tech Stack:** React 19, TypeScript, React Query, Redux Toolkit, Socket.io Client, React Router, Vite

- **Key Focus:** Seat selection UI, booking flow, real-time seat availability, state management

- **Optional Features:** Code splitting, optimistic updates, skeleton loading, error boundaries, WebSocket (real-time seat updates)

- **File:** [12) Ticket Booking System.md](12%20Ticket%20Booking%20System.md)

### Geo-Spatial Systems

### 13. Ride-Sharing System

- **Type:** Frontend System Design

- **Tech Stack:** React 19, TypeScript, React Query, Redux Toolkit, Socket.io Client, React Router, Vite

- **Key Focus:** Ride request interface, real-time location tracking UI, ETA display, map integration, state management

- **Optional Features:** Code splitting, WebSocket reconnection, throttling (location updates), PWA support, error boundaries, skeleton loading

- **File:** [13) Ride-Sharing System.md](13%20Ride-Sharing%20System.md)

### 14. Food Delivery System

- **Type:** Frontend System Design

- **Tech Stack:** React 19, TypeScript, React Query, Redux Toolkit, Socket.io Client, React Router, Vite

- **Key Focus:** Restaurant browsing, order placement UI, real-time tracking interface, cart management, state management

- **Optional Features:** Image optimization (restaurant/menu images), code splitting, infinite scroll, WebSocket reconnection, throttling (location updates), skeleton loading, PWA support

- **File:** [14) Food Delivery System.md](14%20Food%20Delivery%20System.md)

> **Note:** Ride-Sharing and Food Delivery share similar frontend patterns (real-time tracking, map integration) but differ in UI/UX (ride request vs order placement, driver tracking vs delivery tracking).

### Real-World Examples

### 15. iGamio Fantasy Sports Platform

- **Type:** Frontend System Design

- **Tech Stack:** React 19, TypeScript, React Query, Redux Toolkit, Socket.io Client, React Router, Vite

- **Key Focus:** Team creation UI, contest management, real-time score updates, payment integration UI, state management

- **Optional Features:** Image optimization, code splitting, virtual scrolling, memoization, bundle optimization, WebSocket reconnection, optimistic updates, skeleton loading

- **File:** [15) iGamio Fantasy Sports Platform.md](15%20iGamio%20Fantasy%20Sports%20Platform.md)

### 16. Real-Time Poker Game

- **Type:** Frontend System Design

- **Tech Stack:** React 19, TypeScript, React Query, Redux Toolkit, Socket.io Client, Framer Motion, React Router, Vite

- **Key Focus:** Game UI, real-time synchronization, player actions, animations, state management

- **Optional Features:** Code splitting, image optimization, virtual scrolling, memoization, WebSocket reconnection, optimistic updates, error boundaries, bundle optimization

- **File:** [16) Real-Time Poker Game.md](16%20Real-Time%20Poker%20Game.md)

## 📖 Design Document Structure

### High Level Design (HLD)

1. **a) Functional Requirements**
   - User-facing features and capabilities

2. **b) Non-Functional Requirements**
   - Performance, scalability, security, UX goals

3. **c) MVP (Minimum Viable Product)**
   - Phase 1: Core Features (Must Have)
   - Phase 2: Enhanced Features
   - Phase 3: Advanced Features

4. **d) Technology Choices**
   - Frontend Framework (React 19, TypeScript)
   - State Management (React Query, Redux Toolkit/Zustand, Context API)
   - UI/UX Libraries
   - Build Tools (Vite/Webpack)
   - Testing (React Testing Library, Vitest/Jest, Playwright/Cypress)
   - Deployment (Vercel/Netlify, AWS S3 + CloudFront)

5. **e) Architecture Overview**
   - Frontend Architecture Layers:
     - Presentation Layer (React Components)
     - Business/Controller Layer
     - State Management Layer (Client State, Server State)
     - API Integration Layer
     - Routing Layer
     - Build & Deployment Layer

6. **f) App Flow**
   - Frontend user journeys
   - Component interaction flows
   - State update flows

### Low Level Design (LLD)

1. **i) Component Architecture**
   - Component hierarchy
   - Component structure
   - Key React components

2. **ii) State Management**
   - Client State (useState, Redux Toolkit/Zustand, Context API)
   - Server State (React Query, SWR, Service Worker)

3. **iii) Implementation Details**
   - Business/Controller Layer
   - Advanced component patterns
   - Performance optimizations
   - UI/UX enhancements
   - Accessibility features

4. **iv) Testing**
   - Component Testing
   - Integration Testing
   - E2E Testing

5. **Algorithms (if needed)**
   - Frontend-relevant algorithms only (URL validation, debouncing)

6. **Data Models**
   - TypeScript interfaces (NO database schemas)

7. **Protocols**
   - REST API Protocol
   - WebSocket Protocol (if applicable)

8. **API Design**
   - Request/Response formats
   - Status codes
   - Complete API endpoints for all features

9. **Security**
   - Frontend security (input validation, XSS prevention, CSRF protection)

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

- **Cheatsheet:** [Projects Interview Cheatsheet.md](Projects%20Interview%20Cheatsheet.md)
