# 🎯 Project Discussion Questions

Interview questions about complex problems solved in real projects, following STAR method format.

## 📋 Projects

| Project | Type | Questions | Files |
|---------|------|-----------|-------|
| [iGamio Fantasy Sports Platform](#igamio-fantasy-sports-platform) | Cross-platform Mobile App | Q1-Q10 | HLD + LLD |
| [Real-Time Poker Game](#real-time-poker-game) | Real-time Multiplayer Game | Q11-Q20 | HLD + LLD |

---

## 🏏 iGamio Fantasy Sports Platform

**Project Overview:**
High-performance cross-platform mobile app (Android, iOS, Web) using React Native, enabling users and B2B customers to join real-money cricket, football, and kabaddi contests, view scheduled, live, and completed matches, create and update teams, and securely participate using the integrated Cashfree payment gateway for deposits, transactions, and KYC verification for bank accounts and PAN cards.

**Team Size:** 2-person team  
**Built:** From scratch  
**Tech Stack:** React Native, Axios, REST APIs, Cashfree Payment Gateway

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

## 📖 Design Documents

### iGamio Fantasy Sports Platform

- **[High Level Design (HLD)](1%20iGamio%20Fantasy%20Sports%20Platform%20-%20HLD.md)** - Requirements, Scope, Tech Choices
- **[Low Level Design (LLD)](1%20iGamio%20Fantasy%20Sports%20Platform%20-%20LLD.md)** - Component Architecture, Data Models, APIs, Protocols, Implementation
- **[Backend System Design](1%20iGamio%20Fantasy%20Sports%20Platform%20-%20Backend%20System%20Design.md)** - Backend Architecture, APIs, Database, Scalability
- **[Interview Answers](1%20iGamio%20Fantasy%20Sports%20Platform%20-%20Answers.md)** - Complete answers to all interview questions

### Real-Time Poker Game

- **[High Level Design (HLD)](2%20Real-Time%20Poker%20Game%20-%20HLD.md)** - Requirements, Scope, Tech Choices
- **[Low Level Design (LLD)](2%20Real-Time%20Poker%20Game%20-%20LLD.md)** - Component Architecture, Data Models, APIs, Protocols, Implementation
- **[Backend System Design](2%20Real-Time%20Poker%20Game%20-%20Backend%20System%20Design.md)** - Backend Architecture, Game Engine, Socket.io, Scalability
- **[Interview Answers](2%20Real-Time%20Poker%20Game%20-%20Answers.md)** - Complete answers to all interview questions

## 📝 Answer Format

All project questions follow the **STAR method**:

- **Situation**: What happened, explained simply
- **Action**: What you did, in plain language
- **Result**: Impact - numbers, feedback, outcomes
- **Takeaway**: What you learned, easy to remember

See `rule.md` - Section 3 for complete format rules.
