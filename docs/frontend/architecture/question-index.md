---
sidebar_label: "Question Index"
sidebar_position: 0
---
## 📋 Quick Navigation

| Section | Topic | Coverage | Difficulty |
|---------|-------|----------|------------|
| [📚](#introduction) | Introduction | Framework & Tool Comparisons | ⭐⭐⭐ |
| [🌐](#network) | Network | Web Works, Protocols, APIs | ⭐⭐⭐ |
| [📡](#communication) | Communication | Polling, WebSockets, SSE, Webhooks | ⭐⭐⭐ |
| [📄](#html-internals) | HTML Internals | Parsing, DOM, HTML5 Features | ⭐⭐⭐⭐ |
| [🎨](#css-internals) | CSS Internals | Parsing, CSSOM, Layout Systems | ⭐⭐⭐⭐ |
| [⚙️](#javascript-internals) | JavaScript Internals | Engine, Event Loop, Memory | ⭐⭐⭐⭐ |
| [🔷](#typescript-internals) | TypeScript Internals | Compiler, Type System, Generics | ⭐⭐⭐⭐ |
| [⚛️](#react-internals) | React Internals | Virtual DOM, Fiber, Hooks | ⭐⭐⭐⭐ |
| [⚡](#nextjs-internals) | Next.js Internals | App Router, Server Components | ⭐⭐⭐⭐ |
| [🟢](#nodejs-internals) | Node.js Internals | Event Loop, V8, libuv | ⭐⭐⭐⭐ |
| [📱](#react-native-internals) | React Native Internals | Bridge, Native Modules, Threading | ⭐⭐⭐⭐ |
| [🌐](#browser-apis) | Browser APIs | DOM, Fetch, Storage, Media, etc. | ⭐⭐⭐ |
| [🏗️](#high-level-design) | High Level Design | Requirements, Architecture, Infrastructure | ⭐⭐⭐⭐ |
| [🔧](#low-level-design) | Low Level Design | Implementation Details | ⭐⭐⭐⭐ |
| [🔐](#security) | Security | XSS, CSRF, CORS, Headers, Tokens | ⭐⭐⭐⭐ |
| [🧪](#testing) | Testing | Unit, Integration, E2E, A/B, Performance | ⭐⭐⭐ |
| [⚡](#performance) | Performance | Monitoring, Tools, Optimization, Patterns | ⭐⭐⭐⭐ |
| [💾](#database--caching) | Database & Caching | Storage, Caching, State Management | ⭐⭐⭐⭐ |
| [📊](#logging--monitoring) | Logging & Monitoring | Telemetry, Alerting, Debugging | ⭐⭐⭐ |
| [♿](#accessibility) | Accessibility | Keyboard, Screen Reader, Focus, Contrast | ⭐⭐⭐⭐ |
| [📱](#offline-support) | Offline Support | Service Workers, PWAs | ⭐⭐⭐ |
| [🎯](#patterns) | Patterns | Rendering Patterns, Anti-Patterns | ⭐⭐⭐⭐ |
| [🏗️](#microfrontend) | Microfrontend | Architecture, Patterns, Deployment | ⭐⭐⭐⭐ |

---

# 🎨 Frontend System Design Interview Questions

---

## 🧭 Recommended Preparation Order

### 0. Introduction

- **What to cover**: Framework comparisons (React vs Vue/Angular/Svelte), bundling tools (Webpack vs Vite/Rollup), backend comparisons (Node.js vs Python/Go/Java), database choices (SQL vs NoSQL), and mobile frameworks (React Native vs Flutter vs Cordova).

### 1. Foundation

- **What to cover**: How the web works, networking, communication patterns, HTML/CSS/JavaScript/TypeScript internals, and how React, Next.js, Node.js, and React Native work internally.

### 2. APIs & Design

- **What to cover**: Browser APIs, high-level design (requirements, architecture, infrastructure), and low-level design (implementation details).

### 3. Security & Quality

- **What to cover**: Security best practices (XSS, CSRF, CORS, etc.) and testing strategies (unit, integration, E2E, A/B, performance, security).

### 4. Performance & Data

- **What to cover**: Performance optimization, monitoring, database & caching strategies, and logging & monitoring.

### 5. UX & Reliability

- **What to cover**: Accessibility basics (keyboard, screen reader, contrast, focus) and offline-ready UX (Service Workers + PWAs).

### 6. Patterns

- **What to cover**: Rendering patterns (CSR, SSR, SSG, ISR), React anti-patterns, JavaScript anti-patterns, and Node.js anti-patterns.

### 7. Advanced Architecture

- **What to cover**: Microfrontend architecture, patterns, implementation approaches, communication strategies, and deployment.

---

## 📚 Introduction

⚛️ React vs Other Frameworks (React, Vue, Angular comparison)

📦 Webpack vs Other Bundling Tools (Webpack, Parcel, Vite, Rollup)

🟢 Node.js vs Other Frameworks (Node.js, Python, Java comparison)

💾 SQL vs NoSQL (Database selection and trade-offs)

📱 React Native vs Flutter vs Cordova (Mobile framework comparison)

---

## 🌐 Network

🌍 How the Web Works (DNS, TCP, HTTP, Rendering)

🔌 TCP/UDP (Transport layer protocols)

🤝 TCP Handshake + TLS Handshake (Connection establishment)

🔒 HTTP vs HTTPS (Protocol comparison and security)

🔗 REST APIs (RESTful API design and principles)

📊 GraphQL (Query language and API design)

⚡ gRPC (High-performance RPC framework)

🎨 Critical Rendering Path (Browser rendering process)

📧 SMTP/FTP (Email and file transfer protocols)

💳 Payment Gateway Internal Working (Payment processing flow)

---

## 📡 Communication

⏱️ Short Polling

⏳ Long Polling

🔌 WebSockets

📡 Server-Sent Events (SSE)

🪝 Webhooks

🔌 Socket.io Internal Working

---

## 📄 HTML Internals

📄 How HTML Works Internally (Parsing, DOM, Tokenization, HTML5 Features)

---

## 🎨 CSS Internals

🎨 How CSS Works Internally (Parsing, CSSOM, Cascade, Specificity, Layout Systems)

---

## ⚙️ JavaScript Internals

⚙️ How JavaScript Works Internally (Engine, Execution Context, Event Loop, Memory Management)

---

## 🔷 TypeScript Internals

🔷 How TypeScript Works Internally (Compiler, Type System, Type Inference, Generics)

---

## ⚛️ React Internals

⚛️ How React.js Works Internally (Virtual DOM, Fiber, Reconciliation, Hooks, State Management)

---

## ⚡ Next.js Internals

⚡ How Next.js Works Internally (App Router, Server Components, Build System, Rendering Strategies)

---

## 🟢 Node.js Internals

🟢 How Node.js Works Internally (Event Loop, V8, libuv, Modules, Streams, Cluster)

---

## 📱 React Native Internals

📱 How React Native Works Internally (Bridge, JSI, Fabric, Native Modules, Threading)

---

## 🌐 Browser APIs

🌳 DOM API

📡 Fetch API

💾 Web Storage APIs

📍 Geolocation API

🎨 Canvas API

👷 Web Workers API

👁️ Intersection Observer API

🔔 Notification API

🎬 Media APIs

📁 File API

📜 History API

🔌 WebSocket API

---

## 🏗️ High Level Design

📋 Requirements (Functional & Non-Functional)

🎯 Scope, Priority & MVP

💻 Client Architecture

🖥️ Server Architecture

💾 Database Design (SQL/No-SQL)

⚖️ Load Balancer

🌐 CDN (Content Delivery Network)

🔧 Middleware

⚡ Caching & Redis

📬 Queue System

⏰ Cron Jobs

🚀 CI/CD Pipeline

---

## 🔧 Low Level Design

👁️ View Layer Implementation

🔌 Service Layer Implementation

🎮 Controller/Business Logic Implementation

📊 Data Model Implementation

🔗 API/GraphQL Implementation

🗃️ State Management Implementation

⚠️ Error Handling & Validation

⚡ Performance Optimization Implementation

🔐 Security Implementation

🧪 Testing Implementation

---

## 🔐 Security

⚠️ Cross-Site Scripting (XSS)

🛡️ iframe Protection (Clickjacking)

🔒 Security Headers

🔐 Client-Side Security

🔒 Secure Communication (HTTPS)

📦 Dependency Security

📜 Compliance and Regulations

✅ Input Validation and Sanitization

🚨 Server-Side Request Forgery (SSRF)

💉 Server-Side JavaScript Injection (SSJI)

🎛️ Feature Policy / Permissions Policy

🔐 Subresource Integrity (SRI)

🌐 Cross-Origin Resource Sharing (CORS)

🚫 Cross-Site Request Forgery (CSRF)

🎫 Access Token and Refresh Token Management

---

## 🧪 Testing

🧩 Unit and Integration Testing

🤖 E2E and Automation Testing

📊 A/B Testing

⚡ Performance Testing

🔐 Security Testing

---

## ⚡ Performance

📊 Performance Monitoring

🛠️ Performance Tools

🌐 Network Optimization

🎨 Rendering Patterns

📦 Build Optimization

---

## 💾 Database & Caching

💾 Local Storage

🗂️ Session Storage

🍪 Cookie Storage

🗄️ IndexedDB

📊 Normalization

🌐 HTTP Caching

👷 Service Worker Caching

🔗 API Caching

🗃️ State Management

---

## 📊 Logging & Monitoring

📡 Telemetry

🚨 Alerting

🔧 Fixing Performance and Error Issues

🐛 Error Tracking and Source Maps

🔭 OpenTelemetry in the Browser

🎯 Sampling and Cost Control

🔒 Privacy and PII Scrubbing

---

## ♿ Accessibility

📏 The Target: WCAG 2.2 AA

⌨️ Keyboard Accessibility

🔊 Screen Reader

🎯 Focus Management

🎨 Color Contrast

🛠️ Accessibility Tools

🔧 How to Fix Accessibility Issues

🧱 Accessibility in a Design System

---

## 📱 Offline Support

👷 Service Workers

🧰 Workbox (Production Service Workers)

💾 Storing Data Offline (IndexedDB)

🔄 Background Sync and Offline Writes

⚖️ Conflict Resolution

📱 Progressive Web Applications (PWAs)

---

## 🎯 Patterns

🎨 Rendering Patterns

⚛️ Anti-React Patterns

⚙️ Anti-JavaScript Patterns

🟢 Anti-Node.js Patterns

---

## 🏗️ Microfrontend

🏗️ Microfrontend Architecture

---

## 📖 Complete Answer Guide

- [01) Introduction](./01-introduction.md) - Framework & Tool Comparisons (React vs Vue/Angular, Webpack vs Parcel/Vite/Rollup, Node.js vs Python/Java, SQL vs NoSQL, React Native vs Flutter/Cordova)

- [02) Web Works](./02-web-works.md) - How the Web Works (DNS, TCP, HTTP, Rendering)

- [03) Networking](./03-networking.md) - Protocols, APIs, Payment Gateway (TCP/UDP, HTTP/HTTPS, REST, GraphQL, gRPC, SMTP/FTP)

- [04) Rendering Path](./04-rendering-path.md) - Critical Rendering Path (Browser rendering process)

- [Communication](./question-index.md#communication) - Real-time Communication (Short/Long Polling, WebSockets, SSE, Webhooks, Socket.io)

- [05) HTML Internals](./05-html-internals.md) - HTML Parsing, DOM Construction, Tokenization, HTML5 Features

- [06) CSS Internals](./06-css-internals.md) - CSS Parsing, CSSOM, Cascade, Specificity, Layout Systems

- [07) JavaScript Internals](./07-javascript-internals.md) - Engine, Execution Context, Event Loop, Memory Management, Hoisting, Scope, Closures

- [08) TypeScript Internals](./08-typescript-internals.md) - Compiler, Type System, Type Inference, Generics, Module System

- [09) React Internals](./09-react-internals.md) - Virtual DOM, Fiber, Reconciliation, Hooks, State Management, Event System

- [10) Next.js Internals](./10-next-js-internals.md) - App Router, Server Components, Build System, Routing, Rendering Strategies

- [11) Node.js Internals](./11-node-js-internals.md) - Event Loop, V8, libuv, Modules, Streams, Buffer, Cluster

- [12) React Native Internals](./12-react-native-internals.md) - Bridge, JSI, Fabric, Native Modules, Threading, Performance

- [13) Browser APIs](./13-browser-apis.md) - DOM, Fetch, Storage, Geolocation, Canvas, Workers, Intersection Observer, Notifications, Media, File, History, WebSocket

- [14) High Level Design](./14-high-level-design.md) - Requirements, Scope/MVP, Architecture, Database, Load Balancer, CDN, Middleware, Caching, Queue, Cron, CI/CD

- [15) Low Level Design](./15-low-level-design.md) - View Layer, Service Layer, Controller, Data Model, API, State Management, Error Handling, Performance, Security, Testing

- [16) Security](./16-security.md) - XSS, CSRF, CORS, Security Headers, HTTPS, Dependency Security, Compliance, Input Validation, SSRF, SSJI, Permissions Policy, SRI, Access/Refresh Tokens

- [17) Testing](./17-testing.md) - Unit Testing, Integration Testing, E2E Testing, A/B Testing, Performance Testing, Security Testing

- [18) Performance](./18-performance.md) - Performance Monitoring, Core Web Vitals, Performance Tools, Network Optimization, Rendering Patterns, Build Optimization

- [19) Database & Caching](./19-database-and-caching.md) - Local Storage, Session Storage, Cookies, IndexedDB, Normalization, HTTP Caching, Service Worker Caching, API Caching, State Management

- [20) Logging & Monitoring](./20-logging-and-monitoring.md) - Telemetry, Alerting, Fixing Performance and Error Issues

- [21) Accessibility](./21-accessibility.md) - Keyboard Accessibility, Screen Reader Support, Focus Management, Color Contrast, Accessibility Tools, Fixing Issues

- [22) Offline Support](./22-offline-support.md) - Service Workers, Progressive Web Applications (PWAs)

- [23) Patterns](./23-patterns.md) - Rendering Patterns (CSR, SSR, SSG, ISR, Streaming, Partial Hydration), Anti-React Patterns, Anti-JavaScript Patterns, Anti-Node.js Patterns

- [24) Microfrontend](./24-microfrontend.md) - Microfrontend Architecture, Patterns, Implementation Approaches, Communication, Routing, Styling, Testing, Deployment
