# 🎯 Project Discussion Questions

Interview questions about complex problems solved in real projects, following STAR method format.

## 📋 Projects

| # | Project | Type | Questions | Files |
|---|---------|------|-----------|-------|
| 1 | [URL Shortener](#url-shortener) | Full-Stack MERN | Q1-Q5 | HLD + LLD + Answers |
| 2 | [Rate Limiter](#rate-limiter) | Full-Stack System Component | Q1-Q5 | HLD + LLD + Answers |
| 3 | [E-commerce App](#e-commerce-app) | Full-Stack MERN | Q1-Q5 | HLD + LLD + Answers |
| 4 | [Social Media Feed](#social-media-feed) | Full-Stack MERN | Q1-Q5 | HLD + LLD + Answers |
| 5 | [Video Streaming Platform](#video-streaming-platform) | Full-Stack MERN | Q1-Q5 | HLD + LLD + Answers |
| 6 | [Chat Messaging System](#chat-messaging-system) | Full-Stack MERN | Q1-Q5 | HLD + LLD + Answers |
| 7 | [Notification System](#notification-system) | Full-Stack System Component | Q1-Q5 | HLD + LLD + Answers |
| 8 | [Time-Limited Content System](#time-limited-content-system) | Full-Stack MERN | Q1-Q5 | HLD + LLD + Answers |
| 9 | [Real-Time Collaboration System](#real-time-collaboration-system) | Full-Stack MERN | Q1-Q5 | HLD + LLD + Answers |
| 10 | [Ride-Sharing System](#ride-sharing-system) | Full-Stack MERN | Q1-Q5 | HLD + LLD + Answers |
| 11 | [Food Delivery System](#food-delivery-system) | Full-Stack MERN | Q1-Q5 | HLD + LLD + Answers |
| 12 | [Payment System](#payment-system) | Full-Stack MERN | Q1-Q5 | HLD + LLD + Answers |
| 13 | [File Storage System](#file-storage-system) | Full-Stack MERN | Q1-Q5 | HLD + LLD + Answers |
| 14 | [Search System](#search-system) | Full-Stack MERN | Q1-Q5 | HLD + LLD + Answers |
| 15 | [API Gateway](#api-gateway) | System Design | Q1-Q5 | HLD + LLD + Answers |
| 16 | [Scaling REST API](#scaling-rest-api) | System Design | Q1-Q5 | HLD + LLD + Answers |
| 17 | [Ticket Booking System](#ticket-booking-system) | Full-Stack MERN | Q1-Q5 | HLD + LLD + Answers |
| 18 | [Monitoring Logging System](#monitoring-logging-system) | Full-Stack MERN | Q1-Q5 | HLD + LLD + Answers |
| 19 | [iGamio Fantasy Sports Platform](#igamio-fantasy-sports-platform) | Full-Stack MERN | Q1-Q15 | HLD + LLD + Answers |
| 20 | [Real-Time Poker Game](#real-time-poker-game) | Full-Stack MERN | Q1-Q10 | HLD + LLD + Answers |

---

## 🎴 Real-Time Poker Game

**Project Overview:**
High-quality multiplayer poker card game built with React.js and TypeScript, featuring real-time communication via Socket.io and integrated REST APIs. The game includes advanced animations, immersive gameplay, smooth user experiences, and high retention rates. Performance optimizations include code-splitting, React.lazy, and reduced re-renders to deliver a seamless gaming experience.

**Tech Stack:** React.js, TypeScript, Socket.io, REST APIs
**Key Features:** Real-time multiplayer, advanced animations, performance optimization

### Interview Questions

1. **Most complex technical challenge in building the Real-Time Poker Game**

2. **Handling real-time multiplayer synchronization using Socket.io**

3. **Approach to managing game state across multiple players in real-time**

4. **Handling network latency and ensuring fair gameplay for all players**

5. **Strategy for handling player disconnections and reconnections during active games**

6. **Implementing poker game logic and rules validation on both client and server**

7. **Approach to anti-cheating measures and game security**

8. **Optimizing the game for different network conditions and ensuring smooth gameplay**

9. **Strategy for handling concurrent game sessions and room management**

10. **Biggest performance challenge solved with code-splitting and React.lazy**

---

## 🚦 Rate Limiter

**Project Overview:**
Design and implement a rate limiting system to prevent API abuse and ensure fair resource usage. The system supports multiple rate limiting algorithms (fixed window, sliding window, token bucket), distributed rate limiting using Redis, and configurable limits per endpoint and user.

**Tech Stack:** Node.js, Express.js, Redis, TypeScript
**Key Features:** Multiple algorithms, distributed rate limiting, configurable limits, monitoring

### Interview Questions

1. **Most complex technical challenge in building the rate limiter**

2. **Handling distributed rate limiting across multiple servers**

3. **Different rate limiting algorithms and when to use each**

4. **Ensuring the rate limiter doesn't slow down API requests significantly**

5. **Approach to handling rate limiter failures (fail-open vs fail-closed)**

---

## 🛒 E-commerce App

**Project Overview:**
Full-stack e-commerce platform with product catalog, shopping cart, checkout, payment gateway integration, order management, and product search capabilities.

**Tech Stack:** React.js, Node.js, Express.js, MongoDB, Redis, Elasticsearch, Payment Gateway
**Key Features:** Product search, shopping cart, payment processing, order management

### Interview Questions

1. 🎯 **Most complex technical challenge in building the e-commerce platform**

2. 🔍 **Implementing product search with Elasticsearch**

3. 🛒 **Designing the shopping cart to persist across sessions**

4. 💳 **Handling payment gateway integration**

5. 📦 **Implementing inventory management and preventing overselling**

---

## 📱 Social Media Feed

**Project Overview:**
Design a social media feed system that generates personalized, ranked feeds with real-time updates, handling billions of users and posts.

**Tech Stack:** React.js, Node.js, Express.js, MongoDB, Redis, Socket.io, Message Queue
**Key Features:** Feed generation, ranking algorithm, real-time updates, fan-out pattern

### Interview Questions

1. 🏗️ **Designing a social media feed**

2. ⭐ **Handling users with millions of followers (celebrities)**

3. 📊 **Ranking posts in the feed**

4. 🔄 **Handling real-time feed updates**

5. 📈 **Scaling the feed generation system**

---

## 📺 Video Streaming Platform

**Project Overview:**
Design a video streaming platform that handles video upload, processing, adaptive bitrate streaming, content recommendation, and global delivery via CDN.

**Tech Stack:** React.js, Node.js, Express.js, MongoDB, Redis, AWS S3, CDN, FFmpeg
**Key Features:** Video upload, transcoding, adaptive streaming, recommendations

### Interview Questions

1. 🏗️ **Designing a video streaming platform**

2. 📤 **Handling video upload and processing**

3. 🎯 **Implementing content recommendation**

4. ⚡ **Handling adaptive bitrate streaming**

5. 🌐 **Scaling video delivery globally**

---

## 💬 Chat Messaging System

**Project Overview:**
Design a real-time messaging system that handles billions of messages per day with low latency and reliable delivery.

**Tech Stack:** React.js, Node.js, Express.js, MongoDB, Redis, Socket.io, WebSocket, Message Queue
**Key Features:** Real-time messaging, offline handling, group messaging, message delivery

### Interview Questions

1. 🏗️ **Designing a chat/messaging system**

2. 📬 **Ensuring message delivery when recipient is offline**

3. 👥 **Handling group messaging with 256 members**

4. ✅ **Implementing message read receipts**

5. 📈 **Scaling the messaging system for millions of users**

---

## 🔔 Notification System

**Project Overview:**
Design and implement a notification system to send real-time notifications to users across multiple channels (in-app, email, push, SMS). The system includes user preferences, delivery tracking, batching, and retry mechanisms for reliable notification delivery.

**Tech Stack:** Node.js, Express.js, Socket.io, Redis, RabbitMQ, React.js
**Key Features:** Multi-channel notifications, real-time delivery, user preferences, delivery tracking

### Interview Questions

1. 🎯 **Most complex technical challenge in building the notification system**

2. 🔌 **Handling real-time in-app notifications using WebSocket**

3. ⚙️ **Approach to managing user notification preferences**

4. ✅ **Ensuring notifications are delivered reliably even if a service fails**

5. 📦 **Strategy for batching notifications for users who prefer batched mode**

---

## ⏱️ Time-Limited Content System

**Project Overview:**
Design a system for content that expires after a configurable duration, handling billions of users and automatic expiration.

**Tech Stack:** React.js, Node.js, Express.js, MongoDB, Redis, CDN
**Key Features:** Content expiration, TTL storage, automatic cleanup

### Interview Questions

1. 🏗️ **Designing a time-limited content system**

2. ⏰ **Handling content expiration**

3. 🔄 **Implementing real-time content updates**

4. ❤️ **Handling content reactions and engagement**

5. 📈 **Scaling the system for billions of users**

---

## 📝 Real-Time Collaboration System

**Project Overview:**
Design a real-time collaborative editing system where multiple users can edit simultaneously with conflict resolution.

**Tech Stack:** React.js, Node.js, Express.js, MongoDB, Redis, Socket.io, Operational Transformation/CRDT
**Key Features:** Real-time editing, conflict resolution, version control

### Interview Questions

1. 🏗️ **Designing a real-time collaboration system**

2. ⚔️ **Handling conflicts when two users edit the same position**

3. 🔄 **Implementing operational transformation**

4. 👤 **Handling user presence and cursors**

5. 📈 **Scaling the system for thousands of concurrent editors**

---

## 🚗 Ride-Sharing System

**Project Overview:**
Design a ride-sharing system that matches riders with nearest available drivers in real-time with location tracking.

**Tech Stack:** React.js, Node.js, Express.js, MongoDB, Redis, Socket.io, Geo-spatial DB
**Key Features:** Ride matching, location tracking, ETA calculation, real-time updates

### Interview Questions

1. 🏗️ **Designing a ride-sharing system**

2. 🔍 **Finding the nearest available driver**

3. 📍 **Handling real-time location tracking**

4. ⏱️ **Calculating ETA accurately**

5. ❌ **Handling ride cancellation and refunds**

---

## 💳 Payment System

**Project Overview:**
Design a payment processing system that handles billions of transactions per day with high reliability and fraud detection.

**Tech Stack:** React.js, Node.js, Express.js, MongoDB/PostgreSQL, Redis, Payment Gateway SDKs
**Key Features:** Payment processing, idempotency, webhooks, fraud detection

### Interview Questions

1. 🏗️ **Designing a payment system**

2. 🔄 **Ensuring idempotency in payment processing**

3. 🪝 **Handling payment webhooks**

4. 🔄 **Implementing payment retry logic**

5. 💰 **Handling payment refunds**

---

## 📁 File Storage System

**Project Overview:**
Design a file storage system with upload, download, synchronization, versioning, and sharing capabilities.

**Tech Stack:** React.js, Node.js, Express.js, MongoDB, AWS S3, CDN
**Key Features:** File upload, chunking, deduplication, versioning, sync

### Interview Questions

1. 🏗️ **Designing a file storage system**

2. 🔍 **Implementing file deduplication**

3. 🔄 **Handling file synchronization across devices**

4. 📤 **Handling large file uploads**

5. 🔗 **Implementing file sharing and permissions**

---

## 🚪 API Gateway

**Project Overview:**
Design an API Gateway that routes requests to microservices with authentication, rate limiting, and monitoring.

**Tech Stack:** Node.js, Load Balancer, Service Discovery, Redis
**Key Features:** Request routing, authentication, rate limiting, circuit breaker

### Interview Questions

1. 🏗️ **Designing an API Gateway**

2. 🔍 **Implementing service discovery**

3. 🔌 **Handling circuit breaker pattern**

---

## 🔍 Search System

**Project Overview:**
Design a search system that handles billions of documents with fast search latency and relevance ranking.

**Tech Stack:** React.js, Node.js, Express.js, MongoDB, Elasticsearch, Redis
**Key Features:** Full-text search, autocomplete, ranking, faceted search

### Interview Questions

1. 🏗️ **Designing a search system**

2. 🔤 **Implementing autocomplete/suggestions**

3. 📊 **Ranking search results by relevance**

4. 📇 **Handling search indexing**

5. 📈 **Scaling search for billions of documents**

---

## ⚡ Scaling REST API

**Project Overview:**
Design strategies to scale a REST API to handle billions of requests per day while maintaining low latency.

**Tech Stack:** Load Balancer, Caching, Database Scaling, CDN
**Key Features:** Horizontal scaling, caching, database optimization, load balancing

### Interview Questions

1. 📈 **Scaling a REST API to handle 1B+ requests per day**

2. 💾 **Handling database scaling**

3. 📊 **Handling traffic spikes**

4. 💾 **Implementing caching strategies**

5. 📊 **Monitoring and optimizing API performance**

---

## 🎫 Ticket Booking System

**Project Overview:**
Design a ticket booking system that prevents double booking, handles concurrent seat selection, and processes high volumes of bookings.

**Tech Stack:** React.js, Node.js, Express.js, MongoDB, Redis, Message Queue
**Key Features:** Seat locking, booking flow, payment processing, conflict prevention

### Interview Questions

1. 🏗️ **Designing a ticket booking system**

2. 🔒 **Preventing double booking of the same seat**

3. ⚡ **Handling concurrent seat selection**

4. 💳 **Handling payment processing in bookings**

5. 📈 **Scaling the system for high-traffic events**

---

## 🍔 Food Delivery System

**Project Overview:**
Design a food delivery system with order management, delivery partner assignment, and real-time tracking.

**Tech Stack:** React.js, Node.js, Express.js, MongoDB, Redis, Socket.io, Geo-spatial DB
**Key Features:** Order management, delivery assignment, real-time tracking, ETA calculation

### Interview Questions

1. 🏗️ **Designing a food delivery system**

2. 👤 **Assigning delivery partners to orders**

3. 📍 **Tracking orders in real-time**

4. ❌ **Handling order cancellation and refunds**

5. 🗺️ **Optimizing delivery routes**

---

## 📊 Monitoring Logging System

**Project Overview:**
Design a monitoring and logging system that collects logs and metrics from multiple services with real-time alerting.

**Tech Stack:** React.js, Node.js, Express.js, MongoDB, Prometheus, Grafana, ELK Stack
**Key Features:** Log collection, metrics collection, dashboards, alerting

### Interview Questions

1. 🏗️ **Designing a monitoring and logging system**

2. 📥 **Handling high-volume log ingestion**

3. 🚨 **Implementing real-time alerting**

4. 📊 **Building dashboards for metrics visualization**

5. 📈 **Scaling the system for billions of log entries**

---

## 🏏 iGamio Fantasy Sports Platform

**Project Overview:**
High-performance cross-platform mobile app (Android, iOS, Web) using React Native, enabling users and B2B customers to join real-money cricket, football, and kabaddi contests, view scheduled, live, and completed matches, create and update teams, and securely participate using the integrated Cashfree payment gateway for deposits, transactions, and KYC verification for bank accounts and PAN cards.

**Tech Stack:** React.js, TypeScript, React Router, Redux Toolkit, Axios, Material-UI, REST APIs, Cashfree Payment Gateway

### Interview Questions

1. 🎯 **Most complex technical challenge in building iGamio**

2. 🏗️ **Designing the frontend architecture using React.js for scalability and maintainability**

3. 🏗️ **Designing the backend architecture using Node.js and Express.js to handle high traffic**

4. 🔌 **Implementing real-time match updates using Socket.io on both frontend and backend**

5. 🗃️ **Handling state management complexity using Redux Toolkit in React.js**

6. 💾 **Optimizing MongoDB queries and database performance in Node.js**

7. 💳 **Implementing payment gateway integration with proper error handling and security**

8. 📈 **Handling scalability challenges during peak traffic (10,000+ concurrent users)**

9. 🔒 **Ensuring data consistency and handling race conditions in a multi-user environment**

10. 🔐 **Implementing authentication and authorization using JWT in the MERN stack**

11. 📤 **Handling file uploads (KYC documents) securely in the MERN stack**

12. ⚡ **Implementing caching strategies using Redis in Node.js for performance**

13. ⚠️ **Handling error handling and logging across the MERN stack**

14. 🚀 **Ensuring the system is production-ready with monitoring, logging, and deployment**

15. 📈 **Biggest scalability challenge and how it was solved**

---

## 🔗 URL Shortener

**Project Overview:**
Design a URL shortener that can shorten billions of URLs, handle high traffic with minimal latency, and provide analytics.

**Tech Stack:** React.js, Node.js, Express.js, MongoDB, Redis, CDN
**Key Features:** URL encoding, redirect handling, analytics, caching

### Interview Questions

1. 🏗️ **Designing a scalable URL shortener system**

2. 🔍 **Handling URL collisions and ensuring uniqueness**

3. 📈 **Scaling the database for billions of URLs**

4. ⏰ **Handling expired URLs and cleanup**

5. 📊 **Implementing URL analytics and tracking**

---

## 🚦 Rate Limiter

**Project Overview:**
Design and implement a rate limiting system to prevent API abuse and ensure fair resource usage. The system supports multiple rate limiting algorithms (fixed window, sliding window, token bucket), distributed rate limiting using Redis, and configurable limits per endpoint and user.

**Tech Stack:** Node.js, Express.js, Redis, TypeScript
**Key Features:** Multiple algorithms, distributed rate limiting, configurable limits, monitoring

### Interview Questions

1. 🎯 **Most complex technical challenge in building the rate limiter**

2. 🌐 **Handling distributed rate limiting across multiple servers**

3. 📊 **Different rate limiting algorithms and when to use each**

4. ⚡ **Ensuring the rate limiter doesn't slow down API requests significantly**

5. ⚠️ **Approach to handling rate limiter failures (fail-open vs fail-closed)**

---

## 🎴 Real-Time Poker Game

**Project Overview:**
High-quality multiplayer poker card game built with React.js and TypeScript, featuring real-time communication via Socket.io and integrated REST APIs. The game includes advanced animations, immersive gameplay, smooth user experiences, and high retention rates. Performance optimizations include code-splitting, React.lazy, and reduced re-renders to deliver a seamless gaming experience.

**Tech Stack:** React.js, TypeScript, Socket.io, REST APIs
**Key Features:** Real-time multiplayer, advanced animations, performance optimization

### Interview Questions

1. 🎯 **Most complex technical challenge in building the Real-Time Poker Game**

2. 🔌 **Handling real-time multiplayer synchronization using Socket.io**

3. 🎮 **Approach to managing game state across multiple players in real-time**

4. ⚡ **Handling network latency and ensuring fair gameplay for all players**

5. 🔄 **Strategy for handling player disconnections and reconnections during active games**

6. 🎲 **Implementing poker game logic and rules validation on both client and server**

7. 🛡️ **Approach to anti-cheating measures and game security**

8. ⚡ **Optimizing the game for different network conditions and ensuring smooth gameplay**

9. 🏠 **Strategy for handling concurrent game sessions and room management**

10. ⚡ **Biggest performance challenge solved with code-splitting and React.lazy**

---

## 📝 Answer Format

All project questions follow the **STAR method**:

- **Situation**: What happened, explained simply

- **Action**: What you did, in plain language

- **Result**: Impact - numbers, feedback, outcomes

- **Takeaway**: What you learned, easy to remember

See `rule.md` - Section 3 for complete format rules.

---

## 📖 Design Documents

All projects include:

- **[High Level Design (HLD)](README.md#high-level-design-hld)** - Requirements, Scope, Tech Choices, Architecture

- **[Low Level Design (LLD)](README.md#low-level-design-lld)** - Component Architecture, Data Models, APIs, Implementation

- **[Interview Answers](README.md#interview-answers)** - Complete STAR method answers to all interview questions

See [README.md](README.md) for detailed structure and file references.
