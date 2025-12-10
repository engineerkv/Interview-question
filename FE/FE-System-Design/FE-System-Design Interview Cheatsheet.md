# 🎨 Front-End System Design Interview Cheatsheet

> **⏱️ Review Time: 30-40 minutes** | **Priority: ⭐⭐⭐ Critical** | Quick reference for front-end system design interviews

**Quick Review Checklist:**

- [ ] Introduction (React vs Vue/Angular, Webpack vs Parcel/Vite/Rollup, Node.js vs Python/Java, SQL vs NoSQL, React Native vs Flutter/Cordova)

- [ ] Network (DNS, TCP, HTTP, Protocols, REST, GraphQL, gRPC, Rendering Path, Payment Gateway)

- [ ] High Level Design (Requirements, Scope/MVP, Architecture, Database, Load Balancer, CDN, Middleware, Caching, Queue, Cron, CI/CD)

- [ ] Communication (Polling, WebSockets, SSE, Webhooks, Socket.io)

- [ ] Performance + Caching (Monitoring, Tools, Optimization, Storage, HTTP Cache, SW Cache, API Cache, State)

- [ ] Security (XSS, CSRF, CORS, Security Headers, HTTPS, Dependencies, Access/Refresh Tokens)

- [ ] Testing (Unit, Integration, E2E, A/B, Performance, Security)

- [ ] Logging & Monitoring (Telemetry, Alerting, Fixing)

- [ ] Accessibility (Keyboard, Screen Reader, Focus, Color Contrast, Tools)

- [ ] Offline Support (Service Workers, PWAs)

- [ ] Patterns & Anti-Patterns (Rendering Patterns, React Anti-Patterns, JavaScript Anti-Patterns, Node.js Anti-Patterns)

- [ ] Low Level Design (View Layer, Service Layer, Controller, Data Model, API, State, Error Handling, Performance, Security, Testing)

- [ ] HTML Internals (Parsing, DOM Construction, Tokenization, Tree Building, HTML5 Features, Accessibility)

- [ ] CSS Internals (Parsing, CSSOM, Cascade, Specificity, Layout Systems, Rendering Pipeline, Performance)

- [ ] JavaScript Internals (Engine, Execution Context, Memory, Event Loop, Hoisting, Scope, Closures, Prototypes, This, Promises)

- [ ] TypeScript Internals (Compiler Architecture, Type System, Type Inference, Generics, Module System, Compilation)

- [ ] React Internals (Architecture, Virtual DOM, Lifecycle, Fiber, State, Events, Rendering, Performance)

- [ ] Next.js Internals (App Router, Server Components, Build System, Routing, Rendering Strategies, Caching)

- [ ] Node.js Internals (Architecture, Event Loop, V8, libuv, Modules, Streams, Buffer, Cluster)

- [ ] React Native Internals (Bridge, Native Modules, Threading, Performance)

- [ ] Browser APIs (DOM, Fetch, Storage, Geolocation, Canvas, Workers, Intersection Observer, Notifications, Media, File, History, WebSocket)

- [ ] Microfrontend (Architecture, Patterns, Implementation, Communication, Deployment)

---

## 🧭 Recommended Preparation Path

### 0. Introduction (Q0–4)

- **Focus**: Framework comparisons (React vs Vue/Angular/Svelte), bundling tools (Webpack vs Vite/Rollup), backend comparisons (Node.js vs Python/Go/Java), database choices (SQL vs NoSQL), and mobile frameworks (React Native vs Flutter vs Cordova).

### 1. Foundation (Q1–20)

- **Focus**: How the web works, networking, rendering path, communication patterns, HTML/CSS/JavaScript/TypeScript internals, and how React, Next.js, Node.js, and React Native work internally.

### 2. APIs & Design (Q21–54)

- **Focus**: Browser APIs, high-level design (requirements, architecture, infrastructure), and low-level design (implementation details).

### 3. Security & Quality (Q55–74)

- **Focus**: Security best practices (XSS, CSRF, CORS, etc.) and testing strategies (unit, integration, E2E, A/B, performance, security).

### 4. Performance & Data (Q75–91)

- **Focus**: Performance optimization, monitoring, database & caching strategies, and logging & monitoring.

### 5. UX & Reliability (Q92–99)

- **Focus**: Accessibility (keyboard nav, screen readers, contrast, focus, tools) and offline UX (Service Workers, PWAs).

### 6. Patterns & Best Practices (Q100–103)

- **Focus**: Rendering patterns, React anti-patterns, JavaScript anti-patterns, and Node.js anti-patterns.

### 7. Advanced Architecture (Q104)

- **Focus**: Microfrontend architecture, patterns, implementation approaches, communication strategies, and deployment.

---

## 📋 Question Coverage

- **Q0-Q4**: Introduction (React vs Vue/Angular, Webpack vs Parcel/Vite/Rollup, Node.js vs Python/Java, SQL vs NoSQL, React Native vs Flutter/Cordova)

- **Q1**: Web Works

- **Q2-Q7, Q9-Q10**: Networking (TCP/UDP, HTTP/HTTPS, REST, GraphQL, gRPC, SMTP/FTP, Payment Gateway)

- **Q8**: Rendering Path

- **Q11-Q16**: Communication (Short/Long Polling, WebSockets, SSE, Webhooks, Socket.io)

- **Q8.5**: HTML Internals (Parsing, DOM, Tokenization, HTML5 Features)

- **Q8.6**: CSS Internals (Parsing, CSSOM, Cascade, Specificity, Layout Systems)

- **Q17**: JavaScript Internals (Engine, Execution Context, Event Loop, Memory)

- **Q17.5**: TypeScript Internals (Compiler, Type System, Generics, Module System)

- **Q18**: React Internals (Virtual DOM, Fiber, State, Events, Rendering)

- **Q18.5**: Next.js Internals (App Router, Server Components, Build System, Routing)

- **Q19**: Node.js Internals (Event Loop, V8, libuv, Modules, Streams)

- **Q20**: React Native Internals (Bridge, Native Modules, Threading)

- **Q21-Q32**: Browser APIs (DOM, Fetch, Storage, Geolocation, Canvas, Workers, Intersection Observer, Notifications, Media, File, History, WebSocket)

- **Q33-Q44**: High Level Design (HLD)

- **Q45-Q54**: Low Level Design (LLD)

- **Q55-Q69**: Security (includes Access Token and Refresh Token Management)

- **Q70-Q74**: Testing

- **Q75-Q79**: Performance

- **Q80-Q88**: Database & Caching

- **Q89-Q91**: Logging & Monitoring

- **Q92-Q97**: Accessibility

- **Q98-Q99**: Offline Support

- **Q100-Q103**: Patterns & Anti-Patterns

- **Q104**: Microfrontend Architecture

---

## 🌐 Network

### How the Web Works

**Definition:** Web request flow: DNS lookup resolves domain to IP, TCP handshake establishes connection, TLS encrypts HTTPS, HTTP transfers data, browser renders response.

- DNS lookup (cache → ISP → Root → TLD → Authoritative)

- TCP 3-way handshake (SYN → SYN-ACK → ACK)

- TLS handshake for HTTPS

- HTTP request/response

- Browser rendering (DOM → CSSOM → Render Tree → Paint)

### Protocols

- **HTTP/HTTPS**: Web communication

- **HTTP/3 (QUIC)**: UDP-based, faster

- **WebSocket**: Real-time bidirectional

- **Socket.io**: WebSocket with fallbacks, automatic reconnection, room-based messaging

- **TCP**: Reliable, connection-oriented

- **UDP**: Fast, connectionless

- **SMTP**: Email

- **FTP**: File transfer

### Payment Gateway

- **Internal Working**: Customer → Website → Gateway → Processor → Bank → Response

- **Integration Methods**: Redirect (gateway page) or API (your site)

- **Security**: PCI-DSS compliance, encryption, tokenization

- **Webhooks**: Reliable payment status updates

- **Flow**: Authorization → Capture → Settlement

### REST APIs

- Resource-based URLs (nouns)

- HTTP methods (GET, POST, PUT, DELETE)

- Stateless, cacheable

- JSON responses

### GraphQL

- Single endpoint

- Client specifies fields

- Reduces over/under-fetching

- Strong typing

### gRPC

- High-performance RPC

- Protocol Buffers (binary)

- HTTP/2 transport

- Streaming support

---

## 📡 Communication

### Short Polling

**Definition:** Client repeatedly requests server at fixed intervals; simple but inefficient, wastes bandwidth with empty responses when no updates available.

- Client requests at fixed intervals

- Simple, works everywhere

- Wastes bandwidth

### Long Polling

- Server holds request until update

- Reduces empty responses

- Many open connections

### WebSockets

**Definition:** Full-duplex persistent connection enabling real-time bidirectional communication with low latency, ideal for chat, gaming, and live updates.

- Full-duplex, persistent connection

- Low latency, real-time

- Bidirectional communication

### Server-Sent Events (SSE)

- Server → client only

- Automatic reconnection

- Simpler than WebSockets

### Webhooks

- Server-to-server HTTP callbacks

- Event-driven

- Requires signature verification

---

## 🔐 Security

### XSS (Cross-Site Scripting)

- Inject malicious scripts

- Prevent: Input validation, output encoding, CSP

- React/Vue auto-escape (watch dangerouslySetInnerHTML)

### CSRF (Cross-Site Request Forgery)

- Trick authenticated users

- Prevent: CSRF tokens, SameSite cookies

- Double-submit cookie pattern

### CORS (Cross-Origin Resource Sharing)

- Browser security feature

- Server sets Access-Control-Allow-Origin

- Preflight requests for complex requests

### Security Headers

- CSP (Content Security Policy)

- HSTS (Strict-Transport-Security)

- X-Frame-Options (clickjacking protection)

- X-Content-Type-Options (MIME sniffing)

### HTTPS

- TLS encryption

- Certificate verification

- Required for modern features

---

## 🧪 Testing

### Unit Testing

- Test individual functions/components

- Fast, isolated

- Jest, Vitest

### Integration Testing

- Test component interactions

- Test API integrations

- React Testing Library

### E2E Testing

- Test full user flows

- Cypress, Playwright

- Slower, more realistic

### A/B Testing

- Compare variants

- Statistical significance

- Feature flags

### Performance Testing

- Load testing, stress testing

- Lighthouse, WebPageTest

- Core Web Vitals

### Security Testing

- Vulnerability scanning

- Penetration testing

- OWASP Top 10

---

## ⚡ Performance

### Performance Monitoring

- Core Web Vitals (LCP, FID, CLS)

- Real User Monitoring (RUM)

- Synthetic monitoring

### Performance Tools

- Lighthouse (audits)

- Chrome DevTools (profiling)

- WebPageTest (detailed analysis)

- Bundle analyzers

### Network Optimization

- Compression (gzip, Brotli)

- HTTP/2, HTTP/3

- CDN usage

- Resource hints (preconnect, dns-prefetch)

### Rendering Patterns

- CSR (Client-Side Rendering)

- SSR (Server-Side Rendering)

- SSG (Static Site Generation)

- ISR (Incremental Static Regeneration)

- Streaming SSR

- Partial Hydration

### Build Optimization

- Code splitting

- Tree shaking

- Minification

- Dead code elimination

---

## 💾 Database & Caching

### Client Storage

- **LocalStorage**: ~5-10MB, persistent, sync

- **SessionStorage**: ~5-10MB, per-tab, sync

- **Cookies**: ~4KB, sent with requests

- **IndexedDB**: Large, structured, async

### Normalization

- Flatten nested data

- Entity maps keyed by IDs

- Prevents duplication

- Redux Toolkit Entity Adapter

### Caching Layers

- CDN/Edge Cache

- HTTP Cache (browser)

- Service Worker Cache

- API Client Cache (React Query)

- App State (Redux)

- Persistence (LocalStorage/IndexedDB)

### State Management

- Local state (component-level)

- Global state (shared data)

- Server cache (React Query/RTK Query)

- Normalized state

---

## 📊 Logging & Monitoring

### Telemetry

- Collect metrics, errors, events

- Batch events

- Sample high-volume data

- Respect privacy

### Alerting

- Set thresholds

- Different severity levels

- Avoid alert fatigue

- Actionable alerts only

### Fixing Issues

- Identify root causes

- Prioritize by impact

- Reproduce, isolate, fix, verify

- Monitor after fixes

---

## ♿ Accessibility

### Keyboard Accessibility

- Tab order

- Keyboard shortcuts

- Skip links

- Focus indicators

### Screen Reader

- Semantic HTML

- ARIA attributes

- Alt text for images

- ARIA live regions

### Focus Management

- Focus trapping (modals)

- Focus restoration

- Visible focus indicators

- Logical tab order

### Color Contrast

- WCAG AA: 4.5:1 (normal text)

- WCAG AA: 3:1 (large text)

- Don't rely on color alone

- Test with color blindness simulators

### Accessibility Tools

- axe DevTools

- WAVE

- Lighthouse

- Screen readers (NVDA, JAWS, VoiceOver)

---

## 📱 Offline Support

### Service Workers

- Background scripts

- Intercept network requests

- Cache resources

- Enable offline functionality

### Progressive Web Apps (PWAs)

- Service Worker

- Web App Manifest

- Installable

- Push notifications

- Offline support

---

## 🎯 Patterns & Anti-Patterns

### Rendering Patterns

- **CSR**: Client-side rendering (fast nav, slow initial)

- **SSR**: Server-side rendering (fast initial, SEO friendly)

- **SSG**: Static site generation (fastest, pre-rendered)

- **ISR**: Incremental static regeneration (SSG + updates)

- **Streaming SSR**: Progressive HTML delivery

- **Partial Hydration**: Only hydrate interactive parts

### React Anti-Patterns

- Direct DOM manipulation (use state)

- Mutating state (create new objects)

- Index as key (use stable IDs)

- Functions/objects in render (use useCallback/useMemo)

- Prop drilling (use Context)

- Missing useEffect dependencies

- Not cleaning up effects

### JavaScript Anti-Patterns

- Using var (use let/const)

- Not handling async errors (use try/catch)

- Using == (use ===)

- Modifying prototypes (create utilities)

- Verbose null checks (use ?. and ??)

- Functions in loops (use let or forEach)

- Not using destructuring

### Node.js Anti-Patterns

- Blocking event loop (use async/worker threads)

- Not handling async errors (use try/catch)

- Callback hell (use async/await)

- Not using streams (use for large files)

- Hardcoded config (use env vars)

- No graceful shutdown (handle signals)

- No connection pooling (reuse connections)

---

## 🏗️ High Level Design (HLD)

### Requirements

- **Functional**: What system does (features, behaviors)

- **Non-Functional**: How well it performs (performance, security, scalability, availability)

### Scope & MVP

- **Scope**: What's included/excluded

- **Priority**: MoSCoW (Must, Should, Could, Won't)

- **MVP**: Minimal version that delivers core value

### Architecture Layers

- **Client**: View, Service, Controller, Data Model

- **Server**: Web Server, Application Server, Database, Cache

- **Infrastructure**: Load Balancer, CDN, Middleware, Queue, Cron

### Database

- **SQL**: Structured, ACID, relationships

- **NoSQL**: Document (MongoDB), Key-Value (Redis), Column (Cassandra), Graph (Neo4j)

### Caching & Performance

- **CDN**: Edge caching for static assets

- **Redis**: In-memory cache, sessions, real-time features

- **Cache strategies**: Cache-aside, write-through, write-back

### CI/CD

- **CI**: Automated builds, tests on every commit

- **CD**: Automated deployment (delivery or deployment)

- **Tools**: GitHub Actions, GitLab CI, Jenkins

---

## 🔧 Low Level Design (LLD)

### View Layer

- **Components**: Atomic design, presentational vs container

- **Rendering**: CSR, SSR, SSG, ISR

- **Styling**: CSS Modules, styled-components, Tailwind

### Service Layer

- **API Communication**: HTTP requests, data transformation

- **Error Handling**: Consistent error format

- **Caching**: Request caching, cache invalidation

### State Management

- **Local**: Component-level (useState)

- **Global**: Context API, Redux, Zustand

- **Server**: React Query, SWR

### Data Models

- **TypeScript**: Interfaces, types

- **Normalization**: Flat structure, avoid nesting

- **Validation**: Zod, runtime validation

---

## 🌐 Important Browser APIs

### DOM API

- Select, create, modify elements

- Event handling, delegation

- DOM traversal

### Fetch API

- Modern HTTP requests

- Promise-based

- AbortController for cancellation

### Storage APIs

- **localStorage**: Persistent, ~5-10MB

- **sessionStorage**: Session-only, ~5-10MB

- **IndexedDB**: Large structured data, async

### Other APIs

- **Geolocation**: User location (requires permission)

- **Canvas**: Graphics and animations

- **Web Workers**: Background threads

- **Intersection Observer**: Viewport visibility

- **Notifications**: System notifications

- **Media APIs**: Camera, microphone, recording

- **File API**: Read files, drag & drop

- **History API**: SPA routing

- **WebSocket**: Real-time bidirectional communication

---

## ⚙️ JavaScript Internals

### Engine

- **V8**: Chrome, Node.js

- **JIT Compilation**: Interpreter + Compiler

- **Garbage Collection**: Mark-and-sweep

### Execution

- **Execution Context**: Global, function, eval

- **Call Stack**: Tracks function calls

- **Hoisting**: Declarations moved to top

### Memory

- **Garbage Collection**: Automatic memory management

- **Memory Leaks**: Global variables, event listeners, timers

### Event Loop

- **Phases**: Timers, pending, poll, check, close

- **Priority**: nextTick > microtasks > event loop

- **Single-threaded**: Uses event loop for concurrency

### Advanced

- **Scope**: Global, function, block

- **Closures**: Access outer variables

- **Prototypes**: Inheritance chain

- **This Binding**: Depends on call site

- **Promises**: Async operations, async/await

---

## ⚛️ React Internals

### Architecture

- **Component-based**: Reusable components

- **Declarative**: Describe UI, React updates DOM

- **Virtual DOM**: JavaScript representation of DOM

### Reconciliation

- **Diffing**: Compare old and new Virtual DOM

- **Keys**: Identify list items

- **Fiber**: New reconciliation engine

### Hooks

- **useState**: Component state

- **useEffect**: Side effects, lifecycle

- **useMemo/useCallback**: Memoization

### Performance

- **Code Splitting**: Lazy loading

- **Memoization**: React.memo, useMemo, useCallback

- **Virtualization**: Long lists

---

## 🟢 Node.js Internals

### Architecture

- **V8**: JavaScript engine

- **libuv**: Async I/O, event loop

- **Core Modules**: fs, http, etc.

### Event Loop

- **Phases**: Timers, pending, poll, check, close

- **Thread Pool**: Default 4 threads for blocking I/O

- **Non-blocking**: I/O doesn't block event loop

### Modules

- **CommonJS**: module.exports, require()

- **Module Cache**: Cached after first load

- **Resolution**: Core → local → node_modules

### Other

- **Streams**: Readable, Writable, Duplex, Transform

- **Buffer**: Binary data handling

- **Cluster**: Multiple processes, load balancing

- **Child Processes**: spawn, exec, fork

---

## 📱 React Native Internals

### Architecture

- **Bridge**: Communication between JS and native threads

- **Native Modules**: Access to device features

- **Threading**: JS thread, UI thread, native modules thread

### Key Concepts

- **JavaScript Core**: Runs JavaScript code

- **Native Layer**: Platform-specific code (iOS/Android)

- **Serialization**: Data passed via JSON over bridge

- **Async Operations**: Native operations don't block JS thread

### Performance

- **Hermes**: Optimized JS engine for React Native

- **Fabric**: New rendering system (replaces Bridge)

- **TurboModules**: Faster native module system

- **Code Splitting**: Reduce bundle size

---

## 🏗️ Microfrontend

### Core Concept

- **Independent deployment**: Each microfrontend deploys separately

- **Technology diversity**: Different frameworks per microfrontend

- **Team autonomy**: Teams own their microfrontend end-to-end

- **Isolation**: Microfrontends isolated from each other

- **Composition**: Work together to form full application

### Architecture Patterns

- **Build-time integration**: Compile together (monorepo)

- **Server-side integration**: Compose on server (SSI, Edge Side Includes)

- **Runtime integration**: Compose in browser (Module Federation, Single-SPA)

- **iframe integration**: Isolated via iframes

### Implementation Approaches

- **Module Federation**: Webpack 5 feature for runtime sharing

- **Single-SPA**: Framework-agnostic router

- **qiankun**: Alibaba's microfrontend solution

- **Custom solutions**: Custom orchestration layer

### Communication

- **Custom Events**: Browser event system

- **Shared State**: Global state management

- **Props/Context**: Parent-child communication

- **Message Bus**: Centralized event bus

### Deployment

- **Independent CI/CD**: Each team has own pipeline

- **Version management**: Handle version conflicts

- **Rollback strategies**: Independent rollbacks

- **Feature flags**: Gradual rollout

---

## 📚 Introduction

### Framework Comparisons

- **React vs Vue/Angular**: Library vs framework, JSX vs templates, flexibility vs structure, ecosystem size

- **Webpack vs Parcel/Vite/Rollup**: Configuration complexity, development speed, production builds, use cases

- **Node.js vs Python/Java**: I/O performance, development speed, ecosystem, use cases (real-time vs data science vs enterprise)

- **SQL vs NoSQL**: Structured vs flexible schemas, ACID vs eventual consistency, relationships vs scale

- **React Native vs Flutter vs Cordova**: Native components vs compiled code vs WebView, performance, development experience

### Key Considerations

- **Performance**: Runtime performance, bundle size, startup time

- **Developer Experience**: Learning curve, tooling, ecosystem

- **Scalability**: Team size, codebase size, deployment

- **Use Cases**: When to use each technology

---

## ⚡ Quick Tips

- **Introduction**: Choose frameworks based on team expertise, project requirements, and scalability needs

- **DNS caching** speeds up requests

- **TCP ensures reliability**, UDP prioritizes speed

- **HTTPS required** for modern features

- **REST is simple**, GraphQL is flexible, gRPC is fast

- **WebSockets** for real-time, SSE for server→client

- **XSS prevention**: Validate input, encode output

- **CSRF prevention**: Tokens + SameSite cookies

- **Performance**: Monitor Core Web Vitals

- **Caching**: Multiple layers (CDN → HTTP → SW → API → State)

- **Accessibility**: Semantic HTML + ARIA + keyboard navigation

- **Service Workers**: Enable offline-first apps

- **Microfrontend**: Use for large teams, independent deployments, technology diversity
