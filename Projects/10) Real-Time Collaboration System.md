# 1) Problem Statement

Design and implement a real-time collaborative editing system that addresses the following challenges:

- **Core Functionality**: Enable multiple users to edit documents simultaneously without conflicts, with real-time synchronization, conflict resolution, and document versioning
- **Scale Requirements**: Handle 1B+ users, support 50+ concurrent editors per document, millions of documents, and real-time change propagation
- **Performance**: Change propagation < 100ms, low latency for smooth editing experience, fast document loading and saving
- **Conflict Resolution**: Automatic conflict resolution using Operational Transformation (OT) or CRDT algorithms, ensure zero data loss, maintain document consistency across all clients
- **Real-time Features**: Real-time presence indicators, cursor positions, change highlighting, live collaboration awareness
- **Document Management**: Document versioning and history, comments and suggestions, document sharing and permissions
- **Data Consistency**: Maintain document consistency across distributed systems, handle concurrent edits reliably, ensure all clients see the same document state
- **User Experience**: Smooth editing experience with minimal lag, visual feedback for changes, intuitive collaboration features

---

# 2) High Level Design (HLD)

## a) Functional Requirements

- Multiple users can edit document simultaneously
- Real-time synchronization of changes
- Conflict resolution (operational transformation/CRDT)
- Version history
- Comments and suggestions
- Document sharing and permissions

---

## b) Non-Functional Requirements

- Change propagation < 100ms
- Handle 50+ concurrent editors
- No data loss during conflicts
- High availability (99.9% uptime)
- Responsive design for mobile and desktop
  - Modern React 19 features for better performance and UX
- Accessible editing interface (keyboard navigation, screen readers)

---

## c) MVP (Minimum Viable Product)

**Phase 1: Core Features (Must Have)**

- Real-time collaborative editing
- Basic conflict resolution
- Presence indicators
- Document saving

**Phase 2: Enhanced Features**

- Comments and suggestions
- Document versioning
- Advanced conflict resolution
- Document sharing

---

## d) Technology Choices

### Frontend Framework

- **React 19** - Latest React version with useOptimistic, useActionState, useTransition, useDeferredValue, and use() hook
- **TypeScript** - Type safety and better developer experience - Component-based UI framework with type safety

### State Management

- **React Query (TanStack Query)** - Server state management for documents, operations
- **Redux Toolkit** - Client state management for UI state, presence, operations
- **Context API** - App-wide configuration

### Real-time Communication

- **Socket.io Client** - Real-time bidirectional communication for live editing
- **WebSocket** - Real-time operation updates

### UI/UX Libraries

- **React Router** - Client-side routing
- **React Hot Toast** - Toast notifications

### Build Tools

- **Vite** - Fast build tool

### Testing

- **React Testing Library** - Component testing
- **Vitest** - Unit testing
- **Playwright** - E2E testing

### Deployment

- **Vercel/Netlify** - Static site hosting
- **AWS S3 + CloudFront** - Alternative deployment

**Trade-offs:**

- **React Query vs SWR**: React Query provides better caching for document operations
- **Redux Toolkit vs Zustand**: Redux Toolkit offers better DevTools for complex state

---

## e) Architecture Overview

The frontend follows a real-time collaborative editing architecture with Operational Transformation (OT) or CRDT for conflict resolution, WebSocket for real-time communication, and distributed document storage.

**Component Structure:**

```

Frontend Application
├── Presentation Layer
│   ├── UI Components (Editor, CursorIndicator, PresenceList, CommentPanel)
│   ├── Feature Components (DocumentEditor, CollaborationPanel, VersionHistory, CommentThread)
│   └── Layout Components (Header, Sidebar, Toolbar, MainLayout)
├── Business/Controller Layer
│   ├── Business Logic (Validation, formatting, data transformation)
│   ├── Custom Hooks (useDocument, useCollaboration, useOperations)
│   └── Service Functions (Pure functions for data processing)
├── Editor Layer
│   ├── Rich Text Editor (Quill/Slate/Draft.js for document editing)
│   ├── Operation Tracking (Track local operations and apply remote operations)
│   └── Conflict Resolution (Apply OT/CRDT transformations for conflict resolution)
├── State Management
│   ├── Client State
│   │   ├── Local State (useState) - Component-specific UI state
│   │   └── Global State (Redux Toolkit) - Documents, users, presence, operations
│   ├── Server State
│   │   └── React Query - API data caching, refetching
│   └── WebSocket State (Real-time operation updates, presence updates, cursor positions)
├── WebSocket Layer
│   ├── Socket.io Client (WebSocket connection for real-time collaboration)
│   ├── Event Handlers (Operation received, presence update, cursor movement)
│   └── Connection Management (Auto-reconnect, heartbeat, connection state)
├── API Integration
│   ├── API Client (Axios with interceptors for auth, error handling)
│   ├── API Services (documentService, collaborationService)
│   └── Request/Response Transformation (Data normalization and error handling)
└── Routing
    ├── Public Routes (Home)
    ├── Protected Routes (Document, Dashboard, Settings)
    └── Route Guards (Authentication and authorization checks)

```

**Frontend Deployment:**

- **Build**: Production bundle with code splitting using Webpack/Vite
- **CDN**: Static assets served from CloudFront/Cloudflare edge locations
- **Caching**: Aggressive caching for static assets, cache-busting for updates
- **Environment**: Environment variables for API endpoints and WebSocket URLs

**Key Frontend Components:**

- **React 19 Application**:
  - Single-page application with client-side routing
  - Component-based architecture for reusability
  - React Query with React 19 hooks (useOptimistic, useTransition, useDeferredValue)
  - Real-time collaboration via WebSocket with OT/CRDT
  - Responsive design for mobile and desktop
  - Modern React 19 features for better performance and UX

- **CDN/Edge**:
  - Global distribution of static assets
  - Edge caching for improved performance
  - DDoS protection and rate limiting at edge

**Frontend Request Flow:**

1. **User Interaction** → User types or edits document
2. **Local Operation** → Create operation object (insert, delete, format)
3. **WebSocket Emit** → Send operation to server via Socket.io
4. **Optimistic Update** → Apply operation locally immediately
5. **Server Response** → Receive transformed operation from server
6. **Apply Remote Operations** → Apply remote operations from other users
7. **UI Update** → Editor re-renders with updated content

### Backend Architecture

**Backend Layers:**

1. **WebSocket Server Layer** - Handles real-time WebSocket connections
2. **API Gateway/Load Balancer** - Entry point for all HTTP and WebSocket requests
3. **Collaboration Server Layer** - Stateless servers handling WebSocket connections and HTTP requests
4. **Operation Processing Layer** - OT/CRDT service for conflict resolution
5. **Message Queue Layer** - RabbitMQ/Kafka for reliable operation distribution
6. **Application Service Layer** - Business logic and orchestration
7. **Cache Layer** - In-memory caching for performance
8. **Database Layer** - Persistent data storage

### Complete Request Flow

**Document Editing Flow:**

1. **Frontend**: User types in editor, creates operation (insert/delete/format)
2. **WebSocket**: Socket.io client emits operation to server
3. **Backend**: Receive operation, transform against current document state using OT/CRDT
4. **Database**: Apply transformed operation to document, store operation in log
5. **Broadcast**: Broadcast transformed operation to all connected clients
6. **Frontend**: Clients receive operation, apply to local document state
7. **UI Update**: Editor re-renders with updated content

**Document Loading Flow:**

1. **Frontend**: User opens document
2. **API Call**: GET request to document API
3. **Backend**: Fetch document from database (or cache)
4. **Operations**: Fetch recent operations from operations log
5. **Response**: Return document content and operations
6. **Frontend**: Initialize editor with document content
7. **WebSocket**: Join document room for real-time updates

**Presence Tracking Flow:**

1. **Frontend**: User opens document, sends presence update
2. **WebSocket**: Socket.io client emits presence event
3. **Backend**: Update user presence in Redis, broadcast to other users
4. **Frontend**: Other users receive presence update, show cursor/avatar

### Key Components

- **Frontend (React.js)**: Single-page application with WebSocket integration, rich text editor, component-based architecture, Redux for state management, Socket.io client for real-time collaboration
- **WebSocket Servers**: Stateless servers handling WebSocket connections, operation routing, presence tracking
- **Load Balancer**: Distributes WebSocket and HTTP traffic across servers, sticky sessions for WebSocket connections
- **Collaboration Servers**: Stateless design for horizontal scaling, handle WebSocket connections, HTTP API requests, operation processing
- **OT/CRDT Service**: Service for conflict resolution using Operational Transformation or CRDT algorithms
- **Message Queue (RabbitMQ/Kafka)**: Reliable operation distribution, ensures operation delivery, handles operation ordering
- **Application Services**: Document Service, Operation Service, Presence Service, Version Service
- **Cache Layer (Redis)**: In-memory cache for active documents (20% of traffic), presence data, operation queue

---

## f) App Flow

### Complete System Flow (Frontend Perspective)

**Primary User Flow - Real-Time Collaboration System:**

1. **User lands on homepage** → React Router renders HomePage component
2. **User enters URL** → URLInput component captures input, validates in real-time
3. **User clicks submit** → Form triggers React Query mutation
4. **Loading state** → SubmitButton shows loading spinner, form disabled
5. **API call** → useMutation sends POST request to /api/v1/shorten
6. **Success response** → React Query caches response, itemDisplay component renders
7. **User copies URL** → CopyButton uses Clipboard API, shows toast notification
8. **State update** → Components re-render with new item data

**Component Interaction Flow:**

```

User Input → URLInput (local state)
            ↓
Form Submit → Form (React Query mutation)
            ↓
API Call → useShortenURL hook (business logic)
            ↓
Response → React Query cache update
            ↓
Re-render → itemDisplay (receives cached data)

```

**State Update Flow:**

1. **Local State** → URLInput uses useState for input value
2. **Server State** → React Query manages API response, caching, refetching
3. **Global State** → Context API manages user authentication, theme
4. **Component Re-render** → React updates UI based on state changes

**Error Handling Flow:**

1. **API Error** → React Query mutation returns error
2. **Error Boundary** → Catches component errors, shows fallback UI
3. **User Feedback** → Toast notification displays error message
4. **Retry Logic** → User can retry failed requests

**Analytics Dashboard Flow:**

1. **User navigates** → React Router navigates to /dashboard
2. **Data Fetching** → React Query useQuery fetches analytics data
3. **Loading State** → Skeleton screens displayed while loading
4. **Data Display** → Charts render with analytics data
5. **Real-time Updates** → Polling every 30 seconds for active URLs
6. **User Interactions** → Filters update query params, trigger refetch

# 3) Component Architecture

Think of the frontend as a tree of React components - each component handles a specific part of the UI, and they work together to create the complete user experience.

**Component Hierarchy:**

```

App
├── Layout
│   ├── Header
│   │   ├── Logo
│   │   ├── Navigation
│   │   └── UserMenu
│   ├── MainContent
│   └── Footer
├── Pages
│   ├── HomePage
│   │   ├── Form
│   │   │   ├── URLInput
│   │   │   ├── AliasInput (optional)
│   │   │   └── SubmitButton
│   │   └── itemDisplay
│   │       ├── itemCard
│   │       ├── CopyButton
│   │       └── QRCodeButton
│   ├── DashboardPage
│   │   ├── URLList
│   │   │   └── URLItem
│   │   └── AnalyticsDashboard
│   │       ├── ClickCountChart
│   │       ├── CountryChart
│   │       └── DateRangeFilter
│   └── AnalyticsPage
└── SharedComponents
    ├── Button
    ├── Input
    ├── Card
    ├── Toast
    └── LoadingSpinner

```

**Key React Components:**

**1. Form Component:**

- Handles form submission logic
- Manages form state with useState
- Uses React Query mutation for API call
- Validates input before submission

**2. itemDisplay Component:**

- Displays generated item
- Handles copy to clipboard functionality
- Shows QR code generation
- Manages display state (expanded/collapsed)

**3. AnalyticsDashboard Component:**

- Fetches analytics data with React Query
- Renders charts and statistics
- Handles date range filtering
- Updates data in real-time via polling

**4. URLList Component:**

- Displays list of shortened URLs
- Implements virtual scrolling for performance
- Handles pagination
- Supports search and filtering

**Component Communication:**

- **Props** → Parent to child data flow
- **Callbacks** → Child to parent communication
- **Context API** → Shared state across components
- **React Query** → Server state management

# 4) Data Models

### TypeScript Interfaces

```typescript
interface item {
  shortCode: string;
  originalUrl: string;
  item: string;
  expiresAt?: string;
  createdAt: string;
}

interface Analytics {
  shortCode: string;
  clickCount: number;
  uniqueClicks: number;
  topCountries: Array<{ country: string; clicks: number }>;
  clicksByDate: Array<{ date: string; clicks: number }>;
}

```

# 5) API Design

### POST /api/v1/[endpoint]

- **URL:** `/api/v1/[endpoint]`
- **Method:** POST
- **Request Body:**

 ```json
 {
  "field": "value"
}
 ```

- **Response:**

 ```json
 {
 "success": true,
  "data": {}
 }
 ```

---

# 6) Protocols

### REST API Protocol

**Request Format:**

## iii) Implementation Details

### Business/Controller Layer

**Custom Hooks:**

- Encapsulate business logic and API calls
- Example: `useShortenURL`, `useAnalytics`, `useAliasCheck`
- Handle data transformation and validation

**Service Functions:**

- Pure functions for data processing and validation
- URL validation, data transformation, format checking
- Reusable across components

### Advanced Component Patterns

**Compound Components:**

- Group related components together (e.g., Form.Input, Form.Button)
- Share implicit state between components

**Render Props Pattern:**

- Pass render functions as props for flexible component composition

**Custom Hooks Pattern:**

- Extract reusable logic into custom hooks
- Example: `useShortenURL`, `useAnalytics`, `useCopyToClipboard`

**Higher-Order Components (HOCs):**

- Wrap components with additional functionality
- Example: `withAuth`, `withLoading`

### Performance Optimizations

- **Code splitting** with React.lazy() and Suspense
- **Memoization** with useMemo() and useCallback()
- **Virtual scrolling** for long lists (react-window, react-virtuoso)
- **Image optimization** and lazy loading
- **Debouncing and throttling** for user inputs
- **React.memo** for preventing unnecessary re-renders

### UI/UX Enhancements

- **Toast notifications** for user feedback (react-hot-toast)
- **Loading states** and skeleton screens
- **Error boundaries** for error handling
- **Responsive design** for mobile and desktop
- **Accessibility features** (ARIA labels, keyboard navigation, focus management)
- **Animations** with Framer Motion or CSS transitions

### Code Examples

**Custom Hook Example:**

```typescript
function useShortenURL() {
  return useMutation({
    mutationFn: (url: string) => shortenUrl(url),
    onSuccess: () => queryClient.invalidateQueries(["urls"])
  });
}

```

**Component with React Query:**

```typescript
function Form() {
  const { mutate, isPending } = useShortenURL();
  const [url, setUrl] = useState("");

  const handleSubmit = (e: FormEvent) => {
    e.preventDefault();
    mutate(url);
  };

  return <form onSubmit={handleSubmit}>...</form>;
}

```

# 7) Low Level Design (LLD)

## ii) State Management

### Client State

**Local State (useState):**

- Component-specific UI state (form inputs, modal visibility, loading states)
- Example: `const [isOpen, setIsOpen] = useState(false);`

**Global State:**

- Redux Toolkit OR Zustand for complex global state
- Context API for user authentication, theme preferences
- Example: User preferences, app configuration

### Server State

**React Query (TanStack Query):**

- `useQuery` for data fetching and caching
- `useMutation` for data mutations (create, update, delete)
- Automatic refetching, background updates, optimistic updates
- Example: API data caching, synchronization

## iii) Implementation Details

### Business/Controller Layer

**Custom Hooks:**

- Encapsulate business logic and API calls
- Example: `useShortenURL`, `useAnalytics`, `useAliasCheck`

**Service Functions:**

- Pure functions for data processing and validation
- URL validation, data transformation, format checking

### Performance Optimizations

- Code splitting with React.lazy()
- Memoization with useMemo() and useCallback()
- Virtual scrolling for long lists
- Image optimization and lazy loading
- Debouncing and throttling for user inputs

### UI/UX Enhancements

- Toast notifications for user feedback
- Loading states and skeleton screens
- Error boundaries for error handling
- Responsive design for mobile and desktop
  - Modern React 19 features for better performance and UX
- Accessibility features (ARIA labels, keyboard navigation)

## iv) Testing

### Component Testing

- React Testing Library for component tests
- Test user interactions and component behavior
- Example: Test form submission, button clicks, input validation

### Integration Testing

- Test component interactions
- Test API integration with mock data
- Test state management flows

### E2E Testing

- Playwright or Cypress for end-to-end tests
- Test complete user flows
- Example: Test Real-Time Collaboration System flow from start to finish

# 8) Algorithms

### Frontend Algorithms

**URL Validation Algorithm:**

```javascript
function isValidUrl(url) {
  try {
    new URL(url);
    return url.startsWith("http://") || url.startsWith("https://");
  } catch {
    return false;
  }
}

```

**Debouncing Algorithm:**

```javascript
function debounce(func, delay) {
  let timeoutId;
  return (...args) => {
    clearTimeout(timeoutId);
    timeoutId = setTimeout(() => func(...args), delay);
  };
}

```

# 9) Security

### Frontend Security

**Input Validation:**

- Client-side validation before form submission
- Sanitize user input to prevent XSS attacks
- Validate data formats (URLs, emails, custom aliases)

**XSS Prevention:**

- React automatically escapes content
- Use `dangerouslySetInnerHTML` only when necessary with sanitization
- Content Security Policy (CSP) headers

**CSRF Protection:**

- SameSite cookies for authentication
- CSRF tokens for state-changing operations
- Verify origin header on API requests

**Secure Storage:**

- Never store sensitive data in localStorage
- Use httpOnly cookies for authentication tokens
- Clear sensitive data on logout

**HTTPS:**

- All API calls over HTTPS
- Enforce HTTPS in production
- HSTS headers for security

**Rate Limiting (Client-Side):**

- Debounce API calls to prevent abuse
- Show user-friendly messages when rate limited
- Implement exponential backoff for retries

# 10) Deployment and DevOps

### Frontend Deployment

**Build Optimization:**

- Production build with code splitting and tree shaking
- Minification and compression
- Asset optimization (images, fonts)
- Environment variables for API endpoints

**CI/CD Pipeline:**

- Automated testing on pull requests
- Build and deploy on merge to main
- Preview deployments for feature branches
- Rollback capabilities

**Deployment Platforms:**

- Vercel / Netlify for static site hosting with CDN
- AWS S3 + CloudFront for alternative deployment
- GitHub Pages for simple static sites

**Monitoring:**

- Error tracking (Sentry, LogRocket)
- Performance monitoring (Web Vitals)
- Analytics (user behavior, page views)

# 11) Interview Answers (Frontend Focus)

### Q: How would you handle state management for this system?

**Answer (STAR Method):**

**Situation:** In a Real-Time Collaboration System system, we need to manage both client-side UI state and server-side data efficiently.

**Action:**

- Use React Query for server state (URL data, analytics) - handles caching, refetching, and synchronization
- Use useState for local component state (form inputs, modal visibility)
- Use Context API for global client state (user authentication, theme preferences)
- Implement optimistic updates for better UX

**Result:** Reduced API calls through caching, improved performance, better user experience with instant feedback.

**Takeaway:** Separating client and server state management leads to cleaner code and better performance.
