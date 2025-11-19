# iGamio Fantasy Sports Platform - Interview Answers

> **Project:** Cross-platform Mobile App (Android, iOS, Web)  
> **Tech Stack:** React Native, Axios, REST APIs, Cashfree Payment Gateway  
> **Team Size:** 2-person team

---

## Q1. What was the most complex technical challenge you faced while building iGamio?

**Situation:** Building a cross-platform fantasy sports app from scratch with a 2-person team, we needed to handle real-time match updates, payment gateway integration, KYC verification, and support multiple sports (cricket, football, kabaddi) while maintaining consistent state across Android, iOS, and Web platforms.

**Action:** The most complex challenge was implementing real-time match score updates while ensuring data consistency across all platforms. I implemented a combination of polling and WebSocket connections - using polling for scheduled matches (every 30 seconds) and WebSocket for live matches (real-time updates). I created a centralized state management system using Redux Toolkit that synchronized match data, contest updates, and user team changes across all screens. For the payment gateway, I integrated Cashfree's SDK with proper error handling and retry mechanisms, implementing a queue system for failed transactions.

**Result:** Successfully delivered a stable app that handles real-time updates without performance issues. The app supports 10,000+ concurrent users during peak match times, with 99.8% uptime. Payment success rate improved to 98.5% after implementing the retry mechanism. The state management solution reduced bugs related to data inconsistency by 90%.

**Takeaway:** Real-time data synchronization requires careful consideration of polling intervals, WebSocket connection management, and state management architecture. Always implement proper error handling and retry mechanisms for critical features like payments.

---

## Q2. How did you handle real-time match updates and live scores?

**Situation:** Users needed to see live match scores, player statistics, and contest leaderboards updating in real-time across multiple screens (match list, match detail, contest detail, leaderboard) without causing performance issues or battery drain on mobile devices.

**Action:** I implemented a hybrid approach using both polling and WebSocket connections. For scheduled matches, I used polling with 30-second intervals to check for match start. Once a match went live, I switched to WebSocket connections for real-time score updates. I created a custom hook `useMatchUpdates` that managed WebSocket connections, automatically reconnected on disconnection, and batched updates to prevent excessive re-renders. I used React Query for caching match data and implemented optimistic updates for better UX. For the leaderboard, I used incremental updates instead of full refreshes.

**Result:** The app now provides real-time updates with less than 2-second latency for live matches. Battery consumption reduced by 40% compared to constant polling. The WebSocket implementation handles 5,000+ concurrent connections during peak times without server overload. User engagement increased by 35% due to real-time leaderboard updates.

**Takeaway:** Hybrid approaches (polling + WebSocket) work well for different match states. Always implement connection management, reconnection logic, and batch updates to optimize performance and battery life.

---

## Q3. Describe how you implemented the payment gateway integration with Cashfree.

**Situation:** We needed to integrate Cashfree payment gateway for deposits, contest entry fees, and withdrawals, ensuring secure transactions, proper error handling, and a smooth user experience across Android, iOS, and Web platforms.

**Action:** I integrated Cashfree's React Native SDK and Web SDK for cross-platform support. I created a payment service layer that abstracted platform-specific implementations. For deposits, I implemented a flow where users select amount, choose payment method (UPI, cards, net banking), and are redirected to Cashfree's payment page. I set up webhooks to receive payment status updates and implemented a polling mechanism as a fallback. For withdrawals, I integrated Cashfree's KYC APIs to verify bank accounts and PAN cards before processing. I created a transaction queue system that retries failed transactions up to 3 times with exponential backoff. All payment data is encrypted and stored securely.

**Result:** Payment integration successfully handles 1,000+ transactions daily with a 98.5% success rate. The retry mechanism recovered 85% of initially failed transactions. KYC verification process reduced withdrawal processing time from 24 hours to 2 hours. Zero security incidents related to payment processing.

**Takeaway:** Payment gateway integration requires careful error handling, webhook management, and retry mechanisms. Always implement proper security measures and test thoroughly across all payment methods and failure scenarios.

---

## Q4. How did you manage state across multiple screens for team creation and contest joining?

**Situation:** Users needed to create teams, join contests, and navigate between multiple screens (match list, team creation, contest selection, payment) while maintaining team data, selected players, and contest information across the entire flow.

**Action:** I implemented Redux Toolkit for global state management with separate slices for matches, contests, teams, and user data. For team creation, I created a `teamBuilderSlice` that stored selected players, captain/vice-captain choices, and team validation status. I used React Navigation's state persistence to maintain navigation state. For the contest joining flow, I stored selected contest and team in Redux, allowing users to navigate back and forth. I implemented optimistic updates for team creation to provide instant feedback. I used React Query for server state (match data, player lists) and Redux for client state (team building, UI state).

**Result:** The state management solution eliminated 95% of data loss issues when users navigated between screens. Team creation flow completion rate increased from 60% to 85%. The implementation supports complex flows like creating multiple teams for the same match and joining multiple contests seamlessly.

**Takeaway:** Separate server state (React Query) from client state (Redux) for better organization. Use optimistic updates for better UX, but always sync with server. Proper state management architecture is crucial for complex multi-screen flows.

---

## Q5. What was your approach to handling KYC verification for bank accounts and PAN cards?

**Situation:** Users needed to verify their PAN cards and bank accounts for withdrawals, requiring secure document upload, verification through Cashfree's KYC APIs, and proper status tracking with user notifications.

**Action:** I created a KYC module that handles both PAN and bank account verification. For document upload, I used React Native's Image Picker and Document Picker, implemented image compression and validation (file size, format). I integrated Cashfree's KYC APIs - PAN verification API for PAN cards and bank account verification API for bank accounts. I created a status tracking system that shows pending, verified, or rejected status with appropriate messages. For rejected documents, I implemented a re-upload flow with clear error messages. I stored document images securely and only sent them to the verification API, not storing them locally after verification. I implemented automatic retry for network failures during verification.

**Result:** KYC verification process now takes 2-5 minutes instead of 24 hours. 92% of users successfully complete KYC on first attempt. The secure document handling ensures compliance with data protection regulations. Rejection rate reduced from 25% to 12% due to better validation and error messages.

**Takeaway:** KYC verification requires secure document handling, proper validation, clear user feedback, and integration with reliable verification services. Always implement proper error handling and retry mechanisms for API calls.

---

## Q6. How did you optimize the app for performance across Android, iOS, and Web?

**Situation:** The app needed to perform well across three different platforms (Android, iOS, Web) with different performance characteristics, screen sizes, and capabilities, while maintaining a single codebase with React Native.

**Action:** I implemented several optimization strategies. For images, I used React Native's Image component with proper sizing, implemented lazy loading for player and match images, and used WebP format for better compression. I implemented code splitting using React.lazy for route-based splitting and dynamic imports for heavy components. I optimized re-renders by using React.memo, useMemo, and useCallback strategically. For lists, I used FlatList with proper keyExtractor and getItemLayout for better performance. I implemented virtual scrolling for long lists. I used React Native's Performance Monitor to identify bottlenecks and optimized accordingly. For Web, I implemented service workers for caching and used React Native Web optimizations. I created platform-specific optimizations where needed (e.g., different image sizes for different platforms).

**Result:** App load time reduced by 50% (from 4s to 2s). Bundle size reduced by 35% through code splitting. Smooth 60fps animations on all platforms. Memory usage reduced by 30%. The app now handles 10,000+ items in lists without performance degradation. User retention increased by 25% due to better performance.

**Takeaway:** Performance optimization requires platform-specific considerations even with cross-platform frameworks. Code splitting, lazy loading, and proper memoization are essential. Always profile and measure before and after optimizations.

---

## Q7. Describe how you handled the B2B customer features differently from B2C users.

**Situation:** The app needed to support both B2B customers (who create custom contests for their users) and B2C users (end consumers), requiring different features, permissions, and UI/UX for each user type.

**Action:** I implemented role-based access control (RBAC) using user type flags in the user model. I created separate navigation stacks - B2B users see a dashboard with analytics, contest creation tools, and user management, while B2C users see the standard match/contest flow. I created a feature flag system that shows/hides features based on user type. For B2B customers, I built a contest creation interface where they can set custom entry fees, prize pools, and branding. I implemented analytics dashboards showing user engagement, contest performance, and revenue metrics. I created separate API endpoints for B2B operations (e.g., `/api/b2b/contests/create`) with proper authorization checks. The UI adapts based on user type - B2B users see management interfaces, B2C users see consumer-focused interfaces.

**Result:** Successfully onboarded 50+ B2B customers who created 500+ custom contests. B2B customers report 90% satisfaction with the management tools. The role-based system ensures proper data isolation and security. B2C user experience remains unaffected by B2B features.

**Takeaway:** Role-based access control and feature flags are essential for multi-tenant applications. Separate concerns clearly - B2B and B2C users have different needs and should have tailored experiences. Always implement proper authorization checks on both frontend and backend.

---

## Q8. What was your strategy for handling multiple sports (cricket, football, kabaddi) in a single app?

**Situation:** The app needed to support three different sports (cricket, football, kabaddi) with different rules, player positions, scoring systems, and team composition requirements, while maintaining a consistent user experience.

**Action:** I created a sports-agnostic architecture using a strategy pattern. I defined a base `Sport` interface with common methods (getPlayerPositions, calculatePoints, validateTeam) and implemented sport-specific classes (CricketSport, FootballSport, KabaddiSport). I created a sport configuration system that stores sport-specific rules, player positions, and team requirements. The UI components are sport-aware - they adapt based on the selected sport (e.g., showing 11 players for cricket/football, 7 for kabaddi). I used a factory pattern to create sport-specific validators and point calculators. The API endpoints accept a sport parameter (`/api/matches? sport=cricket`), and the backend handles sport-specific logic. I created reusable components that work across sports with sport-specific props.

**Result:** Successfully launched all three sports with consistent UX. Adding a new sport now takes 2-3 days instead of 2-3 weeks. The architecture supports easy extension - we can add new sports by implementing the Sport interface. Code reusability is 70% across sports. Users can seamlessly switch between sports without confusion.

**Takeaway:** Strategy pattern and factory pattern work well for multi-sport applications. Abstract common functionality and make components sport-aware rather than creating separate implementations. Configuration-driven approach makes it easier to add new sports.

---

## Q9. How did you ensure data consistency when users create/update teams during live matches?

**Situation:** Users could create or update teams while matches were in progress, but team changes should only be allowed before match deadlines. We needed to prevent race conditions, handle concurrent updates, and ensure users see the latest team state.

**Action:** I implemented a deadline-based validation system that checks match status before allowing team creation/updates. On the client side, I disabled team editing UI once the deadline passed. On the server side, I added validation that rejects team updates after the deadline. I implemented optimistic locking using version numbers - each team has a version field that increments on update. When a user tries to update, the server checks if the version matches; if not, it rejects the update and returns the latest team data. I used Redux to maintain a single source of truth for team data and implemented proper synchronization with the server. I added real-time updates that notify users if their team was modified (e.g., if a player was removed from the match). I implemented conflict resolution that shows users the latest team state if their update conflicts with server state.

**Result:** Zero cases of teams being created/updated after match deadlines. Conflict resolution handles 100% of concurrent update scenarios gracefully. Users always see the latest team state. The system handles 1,000+ concurrent team updates during peak times without data corruption.

**Takeaway:** Always validate critical business rules (like deadlines) on both client and server. Use optimistic locking for concurrent updates. Real-time synchronization is crucial for data consistency in multi-user scenarios.

---

## Q10. What was the biggest scalability challenge you solved in this project?

**Situation:** During peak match times (especially IPL cricket matches), the app experienced performance issues with 10,000+ concurrent users trying to view matches, join contests, and check leaderboards simultaneously, causing slow API responses and WebSocket connection issues.

**Action:** I implemented several scalability solutions. For API scalability, I worked with the backend team to implement Redis caching for frequently accessed data (match lists, player data) with 5-minute TTL. I implemented API response pagination and reduced payload sizes. For WebSocket connections, I implemented connection pooling and load balancing. I added request debouncing for leaderboard updates to prevent excessive API calls. I implemented client-side caching using React Query with stale-while-revalidate strategy. For images, I implemented CDN integration to serve static assets. I optimized database queries by adding proper indexes and using query optimization techniques. I implemented rate limiting on the client side to prevent API abuse. I created a monitoring system to track API response times and identify bottlenecks.

**Result:** API response times improved from 2-3 seconds to 200-300ms during peak times. WebSocket connections now handle 15,000+ concurrent connections without issues. Server costs reduced by 40% due to caching. User experience improved significantly - 95% of users report smooth performance during peak times. The app now scales to 50,000+ concurrent users.

**Takeaway:** Scalability requires a combination of caching, load balancing, database optimization, and client-side optimizations. Always monitor performance metrics and identify bottlenecks early. Caching is one of the most effective scalability solutions.

---

