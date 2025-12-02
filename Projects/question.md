# 🎯 Project Discussion Questions

Interview questions about complex problems solved in real projects, following STAR method format.

## 📋 Projects

| Project | Type | Questions | Files |
|---------|------|-----------|-------|
| [iGamio Fantasy Sports Platform](#igamio-fantasy-sports-platform) | React.js Web App | Q1-Q10 | HLD + LLD |
| [Real-Time Poker Game](#real-time-poker-game) | Real-time Multiplayer Game | Q11-Q20 | HLD + LLD |
| [Rate Limiter](#rate-limiter) | Backend System Component | Q21-Q25 | HLD + LLD |
| [Notification System](#notification-system) | Backend System Component | Q26-Q30 | HLD + LLD |
| [E-commerce App](#e-commerce-app) | Full-Stack (MERN) | Q31-Q40 | HLD + LLD |
| [Youtube](#youtube) | Full-Stack (MERN) | Q41-Q50 | HLD + LLD |
| [News Media Feed](#news-media-feed) | Full-Stack (MERN) | Q51-Q60 | HLD + LLD |

---

## 🏏 iGamio Fantasy Sports Platform

**Project Overview:**
High-performance cross-platform mobile app (Android, iOS, Web) using React Native, enabling users and B2B customers to join real-money cricket, football, and kabaddi contests, view scheduled, live, and completed matches, create and update teams, and securely participate using the integrated Cashfree payment gateway for deposits, transactions, and KYC verification for bank accounts and PAN cards.

**Team Size:** 2-person team  
**Built:** From scratch  
**Tech Stack:** React.js, TypeScript, React Router, Redux Toolkit, Axios, Material-UI, REST APIs, Cashfree Payment Gateway

### Interview Questions

1. **What was the most complex technical challenge you faced while building iGamio?**
2. **How did you handle real-time match updates and live scores?**
3. **Describe how you implemented the payment gateway integration with Cashfree.**
4. **How did you manage state across multiple screens for team creation and contest joining?**
5. **What was your approach to handling KYC verification for bank accounts and PAN cards?**
6. **How did you optimize the app for performance across Android, iOS, and Web?**
7. **Describe how you handled the B2B customer features differently from B2C users.**
8. **What was your strategy for handling multiple sports (cricket, football, kabaddi) in a single app?**
9. **How did you ensure data consistency when users create/update teams during live matches?**
10. **What was the biggest scalability challenge you solved in this project?**

---

## 🎴 Real-Time Poker Game

**Project Overview:**
High-quality multiplayer poker card game built with React.js and TypeScript, featuring real-time communication via Socket.io and integrated REST APIs. The game includes advanced animations, immersive gameplay, smooth user experiences, and high retention rates. Performance optimizations include code-splitting, React.lazy, and reduced re-renders to deliver a seamless gaming experience.

**Tech Stack:** React.js, TypeScript, Socket.io, REST APIs  
**Key Features:** Real-time multiplayer, advanced animations, performance optimization

### Interview Questions

1. **What was the most complex technical challenge you faced while building the Real-Time Poker Game?**
2. **How did you handle real-time multiplayer synchronization using Socket.io?**
3. **Describe your approach to managing game state across multiple players in real-time.**
4. **How did you handle network latency and ensure fair gameplay for all players?**
5. **What was your strategy for handling player disconnections and reconnections during active games?**
6. **How did you implement the poker game logic and rules validation on both client and server?**
7. **Describe your approach to anti-cheating measures and game security.**
8. **How did you optimize the game for different network conditions and ensure smooth gameplay?**
9. **What was your strategy for handling concurrent game sessions and room management?**
10. **What was the biggest performance challenge you solved, and how did code-splitting and React.lazy help?**

---

## 🚦 Rate Limiter

**Project Overview:**
Design and implement a rate limiting system to prevent API abuse and ensure fair resource usage. The system supports multiple rate limiting algorithms (fixed window, sliding window, token bucket), distributed rate limiting using Redis, and configurable limits per endpoint and user.

**Tech Stack:** Node.js, Express.js, Redis, TypeScript  
**Key Features:** Multiple algorithms, distributed rate limiting, configurable limits, monitoring

### Interview Questions

1. **What was the most complex technical challenge you faced while building the rate limiter?**
2. **How did you handle distributed rate limiting across multiple servers?**
3. **Describe the different rate limiting algorithms you implemented and when to use each.**
4. **How did you ensure the rate limiter doesn't slow down API requests significantly?**
5. **What was your approach to handling rate limiter failures (fail-open vs fail-closed)?**
6. **How did you implement per-endpoint and per-user rate limiting?**
7. **Describe how you handled rate limit violations and what information you return to clients.**
8. **What was your strategy for monitoring and alerting on rate limit hits?**
9. **How did you implement whitelist and blacklist functionality?**
10. **What was the biggest scalability challenge you solved in this system?**

---

## 🔔 Notification System

**Project Overview:**
Design and implement a notification system to send real-time notifications to users across multiple channels (in-app, email, push, SMS). The system includes user preferences, delivery tracking, batching, and retry mechanisms for reliable notification delivery.

**Tech Stack:** Node.js, Express.js, Socket.io, Redis, RabbitMQ, React.js  
**Key Features:** Multi-channel notifications, real-time delivery, user preferences, delivery tracking

### Interview Questions

1. **What was the most complex technical challenge you faced while building the notification system?**
2. **How did you handle real-time in-app notifications using WebSocket?**
3. **Describe your approach to managing user notification preferences.**
4. **How did you ensure notifications are delivered reliably even if a service fails?**
5. **What was your strategy for batching notifications for users who prefer batched mode?**
6. **How did you implement delivery tracking and read receipts?**
7. **Describe how you handled retry logic for failed notifications.**
8. **What was your approach to preventing notification spam and respecting user preferences?**
9. **How did you scale the notification system to handle millions of notifications per day?**
10. **What was the biggest reliability challenge you solved in this system?**

---

## 📖 Design Documents

### Rate Limiter

- **[High Level Design (HLD)](3%20Rate%20Limiter%20-%20HLD.md)** - Requirements, Scope, Tech Choices, Architecture
- **[Low Level Design (LLD)](3%20Rate%20Limiter%20-%20LLD.md)** - Algorithms, Implementation, Redis Integration

### Notification System

- **[High Level Design (HLD)](4%20Notification%20System%20-%20HLD.md)** - Requirements, Scope, Tech Choices, Architecture (Full-Stack MERN)
- **[Low Level Design (LLD)](4%20Notification%20System%20-%20LLD.md)** - Components, Workers, WebSocket, Delivery Tracking (Full-Stack MERN)

### E-commerce App

- **[High Level Design (HLD)](5%20E-commerce%20App%20-%20HLD.md)** - Requirements, Scope, Tech Choices, Architecture (Full-Stack MERN)
- **[Low Level Design (LLD)](5%20E-commerce%20App%20-%20LLD.md)** - Component Architecture, Data Models, APIs, Backend Implementation (Full-Stack MERN)

### Youtube

- **[High Level Design (HLD)](6%20Youtube%20-%20HLD.md)** - Requirements, Scope, Tech Choices, Architecture (Full-Stack MERN)
- **[Low Level Design (LLD)](6%20Youtube%20-%20LLD.md)** - Component Architecture, Data Models, APIs, Backend Implementation (Full-Stack MERN)

### News Media Feed

- **[High Level Design (HLD)](7%20News%20Media%20Feed%20-%20HLD.md)** - Requirements, Scope, Tech Choices, Architecture (Full-Stack MERN)
- **[Low Level Design (LLD)](7%20News%20Media%20Feed%20-%20LLD.md)** - Component Architecture, Data Models, APIs, Backend Implementation (Full-Stack MERN)

---

### iGamio Fantasy Sports Platform

- **[High Level Design (HLD)](1%20iGamio%20Fantasy%20Sports%20Platform%20-%20HLD.md)** - Requirements, Scope, Tech Choices, Architecture (Full-Stack MERN)
- **[Low Level Design (LLD)](1%20iGamio%20Fantasy%20Sports%20Platform%20-%20LLD.md)** - Component Architecture, Data Models, APIs, Backend Implementation (Full-Stack MERN)
- **[Interview Answers](1%20iGamio%20Fantasy%20Sports%20Platform%20-%20Answers.md)** - Complete answers to all interview questions

### Real-Time Poker Game

- **[High Level Design (HLD)](2%20Real-Time%20Poker%20Game%20-%20HLD.md)** - Requirements, Scope, Tech Choices, Architecture (Full-Stack MERN)
- **[Low Level Design (LLD)](2%20Real-Time%20Poker%20Game%20-%20LLD.md)** - Component Architecture, Data Models, APIs, Backend Implementation (Full-Stack MERN)
- **[Interview Answers](2%20Real-Time%20Poker%20Game%20-%20Answers.md)** - Complete answers to all interview questions

## 📝 Answer Format

All project questions follow the **STAR method**:

- **Situation**: What happened, explained simply
- **Action**: What you did, in plain language
- **Result**: Impact - numbers, feedback, outcomes
- **Takeaway**: What you learned, easy to remember

See `rule.md` - Section 3 for complete format rules.
