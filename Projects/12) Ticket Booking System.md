# 1) Problem Statement

Design and implement a ticket booking system that addresses the following challenges:

- **Core Functionality**: Enable users to browse available seats, select seats, and complete bookings for events, movies, or shows while preventing double booking
- **Scale Requirements**: Handle 10M+ users, 1M+ bookings per day, millions of concurrent seat selections during popular events
- **Performance**: Booking latency < 2 seconds, fast seat availability updates, smooth booking experience
- **Seat Management**: Handle concurrent seat selection from multiple users, lock seats during booking process, prevent double booking, provide real-time seat availability
- **Booking Process**: Secure booking flow, seat locking mechanism, payment processing, booking confirmation
- **Concurrency Control**: Handle high concurrency during popular events, prevent race conditions, ensure seat availability accuracy
- **Payment Processing**: Process payments securely, handle payment failures, manage booking lifecycle
- **Data Consistency**: Ensure zero double bookings, maintain seat availability consistency, handle concurrent booking requests reliably

---

# 2) High Level Design (HLD)

---

## a) Functional Requirements

- Core functionality for [project]
- User interactions and features
- Content management
- Real-time features (if applicable)

---

## b) Non-Functional Requirements

- **Performance:** Fast page loads (< 2 seconds), smooth interactions
- **Scalability:** Handle millions of users, high traffic
- **Security:** Secure authentication, data encryption
- **Reliability:** 99.9% uptime, handle peak traffic
- **User Experience:** Responsive design, accessible, intuitive

---

## c) MVP (Minimum Viable Product)

**Phase 1: Core Features (Must Have)**

- Core functionality
- Basic features
- Essential user interactions

**Phase 2: Enhanced Features**

- Advanced features
- Performance improvements
- Additional capabilities

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

The frontend follows a layered architecture optimized for ticket booking with seat selection and real-time availability.

**Component Structure:**

```

Frontend Application
├── Presentation Layer
│   ├── UI Components (SeatMap, TicketCard, BookingForm, PaymentButton)
│   ├── Feature Components (EventList, SeatSelector, BookingSummary, TicketViewer)
│   └── Layout Components (Header, Sidebar, Navigation, MainLayout)
├── Business/Controller Layer
│   ├── Business Logic (Seat validation, booking calculations, availability checks)
│   ├── Custom Hooks (useBooking, useSeats, useEvents, usePayment)
│   └── Service Functions (Pure functions for booking calculations and validation)
├── State Management
│   ├── Client State
│   │   ├── Local State (useState) - Component-specific UI state
│   │   ├── Global State (Redux Toolkit/Zustand) - Booking state, selected seats, user preferences
│   │   └── Context API - User authentication, app configuration
│   └── Server State
│       ├── React Query (useQuery/useMutation) - API data caching, refetching, optimistic updates
│       └── Service Worker - Offline caching, background sync
├── API Integration
│   ├── API Client (Axios with interceptors for auth, error handling)
│   ├── API Services (bookingService, eventService, seatService, paymentService)
│   └── Request/Response Transformation (Data normalization and error handling)
└── Routing
    ├── Public Routes (Home, Events)
    ├── Protected Routes (Booking, Tickets, Settings)
    └── Route Guards (Authentication and authorization checks)

```

**Frontend Deployment:**

- **Build**: Production bundle with code splitting using Vite
- **CDN**: Static assets served from CloudFront/Cloudflare edge locations
- **Caching**: Aggressive caching for static assets, cache-busting for updates
- **Environment**: Environment variables for API endpoints and feature flags

**Key Frontend Components:**

- **React 19 Application**:
  - Single-page application with client-side routing
  - Component-based architecture for reusability
  - React Query with React 19 hooks (useOptimistic, useTransition, useDeferredValue)
  - Real-time seat availability updates
  - Responsive design for mobile and desktop
  - Modern React 19 features for better performance and UX

- **CDN/Edge**:
  - Global distribution of static assets
  - Edge caching for improved performance
  - DDoS protection and rate limiting at edge

---

## f) App Flow

### Complete System Flow (Frontend Perspective)

**Primary User Flow - Ticket Booking System:**

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

### POST /api/v1/bookings

- **URL:** `/api/v1/bookings`
- **Method:** POST
- **Description:** Create a new booking
- **Request Body:**

 ```json
 {
 "eventId": "event_abc123",
 "showtimeId": "showtime_xyz789",
 "seatIds": ["seat_1", "seat_2", "seat_3"],
 "paymentMethod": "card",
 "customerInfo": {
 "name": "John Doe",
 "email": "john@example.com",
 "phone": "+1234567890"
 }
 }

 ```

- **Response:**

 ```json
 {
 "success": true,
 "data": {
 "bookingId": "booking_abc123",
 "eventId": "event_abc123",
 "seatIds": ["seat_1", "seat_2", "seat_3"],
 "status": "confirmed",
 "totalAmount": 150.00,
 "qrCode": "https://example.com/qr/booking_abc123",
 "createdAt": "2024-01-15T10:30:00Z"
 }
 }

 ```

- **Status Codes:** 201 (Created), 400 (Validation Error), 409 (Seats Already Booked), 402 (Payment Failed)

### GET /api/v1/showtimes/:showtimeId/seats

- **URL:** `/api/v1/showtimes/:showtimeId/seats`
- **Method:** GET
- **Description:** Get seat map with availability for a showtime
- **Response:**

 ```json
 {
 "success": true,
 "data": {
 "showtimeId": "showtime_xyz789",
 "seats": [
 {
 "seatId": "seat_1",
 "row": "A",
 "number": "1",
 "status": "available",
 "price": 50.00,
 "category": "premium"
 },
 {
 "seatId": "seat_2",
 "row": "A",
 "number": "2",
 "status": "booked",
 "price": 50.00,
 "category": "premium"
 }
 ]
 }
 }

 ```

- **Status Codes:** 200 (Success), 404 (Showtime Not Found)

### POST /api/v1/seats/lock

- **URL:** `/api/v1/seats/lock`
- **Method:** POST
- **Description:** Lock seats temporarily during booking process
- **Request Body:**

 ```json
 {
 "showtimeId": "showtime_xyz789",
 "seatIds": ["seat_1", "seat_2"]
 }

 ```

- **Response:**

 ```json
 {
 "success": true,
 "data": {
 "lockedSeats": ["seat_1", "seat_2"],
 "lockExpiresAt": "2024-01-15T10:35:00Z"
 }
 }

 ```

- **Status Codes:** 200 (Success), 409 (Seats Already Locked/Booked)

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
- Example: Test Ticket Booking System flow from start to finish

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

**Situation:** In a Ticket Booking System system, we need to manage both client-side UI state and server-side data efficiently.

**Action:**

- Use React Query for server state (URL data, analytics) - handles caching, refetching, and synchronization
- Use useState for local component state (form inputs, modal visibility)
- Use Context API for global client state (user authentication, theme preferences)
- Implement optimistic updates for better UX

**Result:** Reduced API calls through caching, improved performance, better user experience with instant feedback.

**Takeaway:** Separating client and server state management leads to cleaner code and better performance.
