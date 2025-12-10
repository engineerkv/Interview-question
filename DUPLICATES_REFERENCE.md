# 📋 Duplicates & Overlaps Reference Guide

**Purpose:** Reference guide for overlapping content across folders and logical preparation order

---

## 📝 Important Note

**Question numbers are unique WITHIN each tech stack, not globally:**

- ✅ **FE/** has Q1-Q247 (JavaScript, React, HTML, CSS, etc.)
- ✅ **BE/** has Q1-Q224 (Node.js, SQL, MongoDB, System Design)
- ✅ **DSA/** has Q1-Q229 (Arrays, Trees, Graphs, etc.)
- ✅ **Projects/** has Q1-Q5 per project (20 projects)

**This is expected and correct!** Each tech stack maintains its own sequential numbering.

---

## 🔗 Overlapping Content Topics

The following sections have overlapping content. Use cross-references to navigate between related topics:

### Frontend System Design ↔ Backend System Design

#### Networking & Protocols

- **FE System Design**: `FE/FE-System-Design/03) Networking.md` - Q2-Q10
  - TCP/UDP, HTTP/HTTPS, REST, GraphQL, gRPC, WebSockets
- **BE System Design**: `BE/BE-System-Design/02) Communication Protocols.md` - Q26-Q40
  - HTTP/1.1 vs HTTP/2 vs HTTP/3, gRPC vs REST, WebSockets, TCP/UDP, TLS

**📌 Cross-reference:**

- For frontend perspective: See `FE/FE-System-Design/03) Networking.md`
- For backend perspective: See `BE/BE-System-Design/02) Communication Protocols.md`

#### API Design

- **FE System Design**: `FE/FE-System-Design/14) High Level Design.md` - Q33-Q44
  - API design, REST principles, GraphQL
- **BE System Design**: `BE/BE-System-Design/03) REST vs GraphQL.md` - Q41-Q50
  - REST vs GraphQL comparison, API versioning, authentication

**📌 Cross-reference:**

- Frontend API usage: See `FE/FE-System-Design/14) High Level Design.md`
- Backend API implementation: See `BE/BE-System-Design/03) REST vs GraphQL.md`

#### Performance & Scaling

- **FE System Design**: `FE/FE-System-Design/18) Performance.md` - Q75-Q79
  - Frontend performance optimization, Core Web Vitals
- **BE System Design**: `BE/BE-System-Design/04) API Scaling.md` - Q51-Q65
  - Backend API scaling, load balancing, caching

**📌 Cross-reference:**

- Frontend performance: See `FE/FE-System-Design/18) Performance.md`
- Backend scaling: See `BE/BE-System-Design/04) API Scaling.md`

#### Database & Caching

- **FE System Design**: `FE/FE-System-Design/19) Database & Caching.md` - Q80-Q88
  - Frontend caching strategies, IndexedDB, localStorage
- **BE System Design**: `BE/BE-System-Design/08) Database Design.md` - Q135-Q169
  - SQL vs NoSQL, database design, Redis, MongoDB

**📌 Cross-reference:**

- Frontend caching: See `FE/FE-System-Design/19) Database & Caching.md`
- Backend databases: See `BE/BE-System-Design/08) Database Design.md`

#### Security

- **FE System Design**: `FE/FE-System-Design/16) Security.md` - Q55-Q69
  - XSS, CSRF, CORS, client-side security
- **BE System Design**: `BE/BE-System-Design/01) System Design Fundamentals.md` - Q1-Q25
  - Security patterns, authentication, authorization

**📌 Cross-reference:**

- Frontend security: See `FE/FE-System-Design/16) Security.md`
- Backend security: See `BE/BE-System-Design/01) System Design Fundamentals.md`

### JavaScript ↔ Node.js

#### Event Loop & Async

- **JavaScript**: `FE/Javascript/05) Promises, Async-Await & Event Loop.md` - Q55-Q80
  - Event loop, promises, async/await, microtasks
- **Node.js**: `BE/Node-Express/01) Node.js Fundamentals.md` - Q1-Q18
  - Node.js event loop, async I/O, callbacks

**📌 Cross-reference:**

- Browser event loop: See `FE/Javascript/05) Promises, Async-Await & Event Loop.md`
- Node.js event loop: See `BE/Node-Express/01) Node.js Fundamentals.md`

#### Modules

- **JavaScript**: `FE/Javascript/04) ES6+ Features.md` - Q50
  - ES modules, import/export
- **Node.js**: `BE/Node-Express/01) Node.js Fundamentals.md` - Q10-Q15
  - CommonJS, ES modules in Node.js

**📌 Cross-reference:**

- ES modules: See `FE/Javascript/04) ES6+ Features.md`
- Node.js modules: See `BE/Node-Express/01) Node.js Fundamentals.md`

---

## 📚 Logical Preparation Order

### For Frontend Developer Interviews

**Phase 1: Fundamentals (Weeks 1-2)**

1. `FE/HTML/` - HTML Fundamentals (Q1-Q111)
2. `FE/CSS/` - CSS Fundamentals (Q1-Q70)
3. `FE/Javascript/` - JavaScript Core (Q1-Q80)

**Phase 2: Core Frameworks (Weeks 3-4)**
4. `FE/React/` - React Fundamentals (Q1-Q100)
5. `FE/Next/` - Next.js (Q1-Q60)
6. `FE/Typescript/` - TypeScript (Q1-Q53)

**Phase 3: Advanced Topics (Weeks 5-6)**
7. `FE/FE-System-Design/` - Frontend System Design (Q0-Q104)
8. `FE/React-Native/` - React Native (Q1-Q95) - Optional

**Phase 4: Practice (Week 7)**
9. `DSA/` - Data Structures & Algorithms (Q1-Q229)
10. `Projects/` - Project Discussions (20 projects)

---

### For Backend Developer Interviews

**Phase 1: Fundamentals (Weeks 1-2)**

1. `FE/Javascript/` - JavaScript Core (Q1-Q80) - Foundation
2. `BE/Node-Express/` - Node.js & Express (Q1-Q100)
3. `BE/Sql/` - SQL Fundamentals (Q1-Q50)

**Phase 2: Databases (Week 3)**
4. `BE/No-Sql/` - MongoDB (Q1-Q57)
5. `BE/BE-System-Design/08) Database Design.md` - Database Design (Q135-Q169)

**Phase 3: System Design (Weeks 4-5)**
6. `BE/BE-System-Design/` - Backend System Design (Q1-Q224)

- Start with: System Design Fundamentals (Q1-Q25)
- Then: Communication Protocols (Q26-Q40)
- Then: API Scaling (Q51-Q65)
- Then: Messaging Systems (Q66-Q94)
- Then: AWS Cloud Architecture (Q95-Q119)
- Finally: Observability, Database Design, Node.js System Design

**Phase 4: Practice (Week 6)**
7. `DSA/` - Data Structures & Algorithms (Q1-Q229)
8. `Projects/` - Project Discussions (20 projects)

---

### For Full Stack Developer Interviews

**Phase 1: Foundation (Weeks 1-3)**

1. `FE/HTML/` - HTML (Q1-Q111)
2. `FE/CSS/` - CSS (Q1-Q70)
3. `FE/Javascript/` - JavaScript (Q1-Q247)
4. `BE/Node-Express/` - Node.js & Express (Q1-Q100)
5. `BE/Sql/` - SQL (Q1-Q50)
6. `BE/No-Sql/` - MongoDB (Q1-Q57)

**Phase 2: Frameworks (Weeks 4-5)**
7. `FE/React/` - React (Q1-Q100)
8. `FE/Next/` - Next.js (Q1-Q60)
9. `FE/Typescript/` - TypeScript (Q1-Q53)

**Phase 3: System Design (Weeks 6-7)**
10. `FE/FE-System-Design/` - Frontend System Design (Q0-Q104)
11. `BE/BE-System-Design/` - Backend System Design (Q1-Q224)

**Phase 4: Practice (Week 8)**
12. `DSA/` - Data Structures & Algorithms (Q1-Q229)
13. `Projects/` - Project Discussions (20 projects)

---

## 🎯 DSA Preparation Order

**Recommended order for DSA preparation:**

1. **Arrays** (Q1-Q33) - Foundation
2. **Strings** (Q34-Q55) - Text manipulation
3. **Linked List** (Q56-Q74) - Linear structures
4. **Stacks & Queues** (Q75-Q86) - Linear structures
5. **Binary Trees** (Q87-Q113) - Tree structures
6. **Binary Search Tree** (Q114-Q123) - Tree structures
7. **Heaps & Priority Queue** (Q124-Q135) - Tree structures
8. **Graphs** (Q136-Q159) - Advanced structures
9. **Dynamic Programming** (Q160-Q192) - Advanced algorithms
10. **Recursion & Backtracking** (Q193-Q202) - Advanced algorithms
11. **Matrix** (Q203-Q207) - Specialized
12. **Trie** (Q208-Q210) - Specialized
13. **Binary Search** (Q211-Q217) - Search algorithms
14. **Bit Manipulation** (Q218-Q223) - Specialized
15. **Math** (Q224-Q229) - Specialized

**See:** `DSA/question.md` for complete problem list

---

## 📖 How to Use Cross-References

When you encounter overlapping content:

1. **Read the primary source first** (based on your role - FE or BE)
2. **Check the cross-reference** for complementary perspective
3. **Add notes** linking related concepts
4. **Practice explaining** both perspectives in interviews

**Example:**

- Learning about HTTP? Read both:
  - `FE/FE-System-Design/03) Networking.md` (browser perspective)
  - `BE/BE-System-Design/02) Communication Protocols.md` (server perspective)

---

## ✅ Summary

- ✅ **No duplicate question numbers within tech stacks** (each tech stack has unique numbering)
- ✅ **Overlaps are intentional** - Different perspectives (FE vs BE) on same topics
- ✅ **Use cross-references** to get complete understanding
- ✅ **Follow logical order** for systematic interview preparation

**Last Updated:** Generated by check_duplicates_and_order.py
