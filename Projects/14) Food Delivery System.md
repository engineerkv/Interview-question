# 1) Problem Statement

Design and implement a food delivery platform that addresses the following challenges:

- **Core Functionality**: Enable users to browse restaurants and menus, place orders, track deliveries in real-time, and process payments
- **Scale Requirements**: Handle 50M+ users, 10M+ orders per day, thousands of restaurants, millions of concurrent users during peak hours
- **Performance**: Order placement < 3 seconds, real-time location tracking, fast restaurant and menu browsing, accurate ETA calculation
- **Order Management**: Process orders with real-time inventory updates, prevent overselling, handle complex menus and customization options, manage order lifecycle
- **Delivery Matching**: Match orders with delivery partners based on proximity, optimize delivery routes, handle concurrent order assignments
- **Real-time Tracking**: Provide live tracking of order status and delivery location, real-time updates to users, restaurants, and delivery partners
- **Payment Processing**: Secure payment processing, handle multiple payment methods, process order payments and restaurant payouts
- **Data Consistency**: Ensure accurate order processing, maintain inventory consistency, handle concurrent order requests reliably

---

# 2) High Level Design (HLD)

## a) Functional Requirements

- Browse restaurants and menus
- Place orders
- Assign delivery partners
- Real-time order tracking
- Payment processing
- Order history
- Restaurant ratings and reviews

---

## b) Non-Functional Requirements

- Order placement < 3 seconds
- Real-time location tracking
- Handle peak hours (lunch/dinner)
- ETA calculation
- High availability (99.9% uptime)
- Responsive design for mobile and desktop
  - Modern React 19 features for better performance and UX
- Accessible interface (keyboard navigation, screen readers)

---

## c) MVP (Minimum Viable Product)

**Phase 1: Core Features (Must Have)**

- Restaurant browsing interface
- Menu viewing and selection
- Order placement
- Real-time order tracking
- Basic payment processing

**Phase 2: Enhanced Features**

- Order scheduling (book orders in advance)
- Multiple payment methods
- Restaurant ratings and reviews
- Order recommendations and personalization
- Loyalty programs and discounts

---

## d) Technology Choices

### Frontend Framework

- **React 19** - Latest React version with useOptimistic, useActionState, useTransition, useDeferredValue, and use() hook
- **TypeScript** - Type safety and better developer experience - Component-based UI framework with type safety

### State Management

- **React Query (TanStack Query)** - Server state management
- **Redux Toolkit** - Client state management
- **Context API** - App-wide configuration

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

- **React Query vs SWR**: React Query provides better caching
- **Redux Toolkit vs Zustand**: Redux Toolkit offers better DevTools

---

## e) Architecture Overview

The frontend follows a food delivery architecture with real-time order tracking, geospatial matching, and distributed order management.

**Component Structure:**

```

Frontend Application
├── Presentation Layer
│   ├── UI Components (RestaurantCard, MenuItem, OrderCard, TrackingMap)
│   ├── Feature Components (RestaurantList, MenuView, OrderPlacer, OrderTracker, PaymentForm)
│   └── Layout Components (Header, Sidebar, Navigation, MainLayout)
├── Business/Controller Layer
│   ├── Business Logic (Validation, formatting, data transformation)
│   ├── Custom Hooks (useOrder, useRestaurant, useCart, usePayment)
│   └── Service Functions (Pure functions for data processing)
├── Map Integration Layer
│   ├── Map Component (Google Maps/Mapbox integration for restaurant and delivery tracking)
│   ├── Location Services (Get current location, geocoding, route calculation)
│   └── Marker Management (Display restaurants, delivery partner locations, route visualization)
├── State Management
│   ├── Client State
│   │   ├── Local State (useState) - Component-specific UI state
│   │   └── Global State (Redux Toolkit) - Restaurants, orders, cart, user
│   ├── Server State
│   │   └── React Query - API data caching, refetching
│   └── WebSocket State (Real-time order status updates, delivery location updates)
├── WebSocket Layer
│   ├── Socket.io Client (WebSocket connection for real-time updates)
│   ├── Event Handlers (Order status change, delivery location update, ETA update)
│   └── Connection Management (Auto-reconnect, heartbeat, connection state)
├── API Integration
│   ├── API Client (Axios with interceptors for auth, error handling)
│   ├── API Services (orderService, restaurantService, paymentService)
│   └── Request/Response Transformation (Data normalization and error handling)
└── Routing
    ├── Public Routes (Home, Restaurants)
    ├── Protected Routes (Order, Tracking, Payment)
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
  - Real-time order tracking via WebSocket
  - Map integration for delivery tracking
  - Responsive design for mobile and desktop
  - Modern React 19 features for better performance and UX

- **CDN/Edge**:
  - Global distribution of static assets
  - Edge caching for improved performance
  - DDoS protection and rate limiting at edge

**Frontend Request Flow:**

1. **User Interaction** → User browses restaurants, places order, or tracks delivery
2. **State Update** → Redux action dispatched or local state updated
3. **API Call** → Axios makes HTTP request to backend API
4. **WebSocket** → Real-time updates via Socket.io
5. **Map Update** → Map component updates with new locations
6. **UI Update** → Components re-render with new data

### Backend Architecture

**Backend Layers:**

1. **WebSocket Server Layer** - Handles real-time WebSocket connections
2. **API Gateway/Load Balancer** - Entry point for all HTTP and WebSocket requests
3. **Order Service Layer** - Stateless servers handling order requests and management
4. **Matching Service Layer** - Geospatial matching algorithm for delivery partner assignment
5. **Location Service Layer** - Real-time location tracking and updates
6. **Message Queue Layer** - RabbitMQ/Kafka for reliable order processing and assignment
7. **Application Service Layer** - Business logic and orchestration
8. **Cache Layer** - In-memory caching for performance
9. **Database Layer** - Persistent data storage with geospatial indexes
10. **External Services Layer** - Maps API, Payment Gateway integration

### Complete Request Flow

**Order Placement Flow:**

1. **Frontend**: User selects restaurant, adds items to cart, places order
2. **API Call**: POST request to order API with order details
3. **Backend**: Validate order, check inventory, process payment
4. **Database**: Create order record with status "placed"
5. **Matching**: Find nearest available delivery partner using geospatial query
6. **Assignment**: Assign order to delivery partner
7. **WebSocket**: Notify restaurant, delivery partner, and user of order status
8. **Response**: Return order confirmation with estimated delivery time
9. **Frontend**: Show order confirmation and tracking screen

**Order Tracking Flow:**

1. **Frontend**: User opens order tracking page
2. **API Call**: GET request to order API
3. **Backend**: Fetch order details and current status
4. **WebSocket**: Join order room for real-time updates
5. **Location Updates**: Delivery partner sends location updates every 5 seconds
6. **Broadcast**: Server broadcasts location to user
7. **Frontend**: Map component updates with delivery partner location and ETA

**Delivery Partner Assignment Flow:**

1. **Order Created**: New order created, needs delivery partner
2. **Geospatial Query**: Find available delivery partners within 5km radius
3. **Filtering**: Filter by availability, rating, current load
4. **Assignment**: Assign order to best matching delivery partner
5. **Notification**: Notify delivery partner via push notification and WebSocket
6. **Acceptance**: Delivery partner accepts order
7. **Update**: Update order status and notify all parties

### Key Components

- **Frontend (React.js)**: Single-page application with WebSocket integration, map integration, component-based architecture, Redux for state management, Socket.io client for real-time updates
- **WebSocket Servers**: Stateless servers handling WebSocket connections, order status updates, location updates
- **Load Balancer**: Distributes WebSocket and HTTP traffic across servers, sticky sessions for WebSocket connections
- **Order Service Servers**: Stateless design for horizontal scaling, handle order placement, order management, payment processing
- **Matching Service**: Geospatial matching algorithm using Redis GeoHash or MongoDB geospatial indexes
- **Location Service**: Real-time location tracking and updates, geospatial queries
- **Message Queue (RabbitMQ/Kafka)**: Reliable order processing, ensures order assignment, handles order state transitions
- **Application Services**: Order Service, Restaurant Service, Delivery Service, Payment Service, Notification Service
- **Cache Layer (Redis)**: In-memory cache for active orders (20% of traffic), restaurant locations (GeoHash), menu data
- **Maps API**: Google Maps/Mapbox for route calculation, ETA, geocoding
- **Payment Gateway**: Stripe/PayPal for secure payment processing

---

## f) App Flow

### Complete System Flow (Frontend Perspective)

**Primary User Flow - Food Delivery System:**

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
- Example: Test Food Delivery System flow from start to finish

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

**Situation:** In a Food Delivery System system, we need to manage both client-side UI state and server-side data efficiently.

**Action:**

- Use React Query for server state (URL data, analytics) - handles caching, refetching, and synchronization
- Use useState for local component state (form inputs, modal visibility)
- Use Context API for global client state (user authentication, theme preferences)
- Implement optimistic updates for better UX

**Result:** Reduced API calls through caching, improved performance, better user experience with instant feedback.

**Takeaway:** Separating client and server state management leads to cleaner code and better performance.
