# 1) Problem Statement

Design and implement a scalable notification system that addresses the following challenges:

- **Core Functionality**: Deliver millions of notifications per day across multiple channels (in-app, email, push, SMS, webhook) with high reliability and real-time delivery
- **Scale Requirements**: Handle millions of notifications per day, support millions of users, scale horizontally to handle traffic spikes
- **Performance**: Real-time notifications delivered in < 1 second, high throughput for bulk notifications, low latency for critical alerts
- **Multi-Channel Support**: Support in-app notifications, push notifications (browser/mobile), email, SMS, and webhook notifications
- **User Preferences**: Support channel preferences, category preferences, frequency preferences (real-time/batched/digest), and quiet hours
- **Reliability**: Guaranteed delivery for important notifications, at-least-once delivery guarantee, retry mechanisms for failed deliveries, fault tolerance
- **Delivery Tracking**: Track notification delivery status, read receipts, notification history, and analytics for notification performance
- **Data Consistency**: Ensure no notifications are lost, respect user preferences, maintain delivery status accurately across distributed systems

---

# 2) High Level Design (HLD)

## a) Functional Requirements

#### Notification Types

- **Push notifications** - Browser push notifications, mobile push notifications

- **In-app notifications** - Real-time notifications within the app

- **Email notifications** - Email alerts for important events

- **SMS notifications** - Text messages for critical alerts

- **Webhook notifications** - Send notifications to external systems

#### Notification Categories

- **System notifications** - App updates, maintenance alerts

- **User activity** - Likes, comments, mentions, follows

- **Transaction notifications** - Payment confirmations, order updates

- **Marketing notifications** - Promotions, offers, newsletters

- **Security notifications** - Login alerts, password changes

#### User Preferences

- **Channel preferences** - User chooses which channels to receive notifications

- **Category preferences** - User can enable/disable notification categories

- **Frequency preferences** - Real-time, batched, or digest mode

- **Quiet hours** - Don't send notifications during specific times

#### Delivery Features

- **Real-time delivery** - Instant notifications for important events

- **Batching** - Group multiple notifications together

- **Retry mechanism** - Retry failed notifications

- **Delivery tracking** - Track if notification was delivered/read

- **Notification history** - Store notification history for users

---

## b) Non-Functional Requirements

#### Performance

- **Low latency** - Real-time notifications delivered in < 1 second

- **High throughput** - Handle millions of notifications per day

- **Scalability** - Scale horizontally to handle load

#### Reliability

- **Guaranteed delivery** - Important notifications must be delivered

- **At-least-once delivery** - Notifications delivered at least once (may have duplicates)

- **Fault tolerance** - System continues working if one component fails

#### User Experience

- **Non-intrusive** - Don't overwhelm users with notifications

- **Relevant** - Only send notifications user cares about

- **Actionable** - Notifications should have clear actions

---

---

## c) MVP (Minimum Viable Product)

### Phase 1: MVP (Must Have) - Priority 1

#### Functional

- **In-app notifications** - Real-time notifications using WebSocket

- **Email notifications** - Basic email sending

- **Notification preferences** - Basic enable/disable per category

- **Notification history** - Store and display notification history

#### Non-Functional

- **Real-time delivery** - WebSocket for instant notifications

- **Basic retry** - Retry failed notifications 3 times

### Phase 2: Enhanced Features - Priority 2

#### Functional

- **Push notifications** - Browser and mobile push notifications

- **SMS notifications** - Text message alerts

- **Advanced preferences** - Channel preferences, quiet hours

- **Batching** - Group notifications together

- **Delivery tracking** - Track delivery and read status

#### Non-Functional

- **Message queue** - Use queue for reliable delivery

- **Advanced retry** - Exponential backoff, dead letter queue

### Phase 3: Advanced Features - Priority 3

#### Functional

- **Webhook notifications** - Send to external systems

- **Notification analytics** - Track open rates, click rates

- **A/B testing** - Test different notification formats

- **Smart batching** - AI-based notification grouping

---

---

## d) Technology Choices

### Real-time Communication

- **Socket.io:** Real-time bidirectional communication for in-app notifications
 - **Why Socket.io?** Automatic reconnection, room-based messaging, fallback support
 - **Room-based** - Users join their notification room, receive notifications instantly
 - **Automatic reconnection** - Handles connection drops gracefully

### Message Queue

- **RabbitMQ / Kafka:** Message queue for reliable notification delivery
 - **Why queue?** Decouples notification generation from delivery, handles spikes
 - **RabbitMQ** - Good for simple use cases, easy to set up
 - **Kafka** - Better for high throughput, event streaming

### Email Service

- **SendGrid / AWS SES:** Email delivery service
 - **Why external service?** Reliable delivery, handles bounces, spam filtering
 - **SendGrid** - Easy to use, good deliverability
 - **AWS SES** - Cost-effective, integrates with AWS

### Push Notification Service

- **Firebase Cloud Messaging (FCM):** For mobile and web push notifications
 - **Why FCM?** Free, reliable, supports both mobile and web
 - **Web Push API** - Browser push notifications
 - **Mobile push** - iOS and Android push notifications

### SMS Service

- **Twilio / AWS SNS:** SMS delivery service
 - **Why external service?** Reliable delivery, handles carrier issues
 - **Twilio** - Easy to use, good documentation
 - **AWS SNS** - Cost-effective, integrates with AWS

### Storage

- **Redis:** For real-time notification delivery and caching
 - **Why Redis?** Fast, pub/sub support, good for real-time

---

## e) Architecture Overview

The frontend follows a layered architecture with real-time notification handling.

**Component Structure:**

```

Frontend Application
├── Presentation Layer
│   ├── UI Components (NotificationBell, NotificationItem, NotificationDropdown, NotificationSettings)
│   ├── Feature Components (NotificationCenter, NotificationPreferences, NotificationHistory)
│   └── Layout Components (Header, Sidebar, NotificationBadge)
├── Business/Controller Layer
│   ├── Business Logic (Notification filtering, grouping, formatting, preference validation)
│   ├── Custom Hooks (useNotifications, useNotificationPreferences)
│   └── Service Functions (Pure functions for data processing and validation)
├── State Management
│   ├── Client State
│   │   ├── Local State (useState) - Component-specific UI state
│   │   ├── Global State (Redux Toolkit/Zustand) - Notifications, unread count, preferences
│   │   └── Context API - User authentication, app configuration
│   ├── Server State
│   │   ├── React Query (useQuery) - API data caching, refetching, optimistic updates
│   │   └── Service Worker - Offline caching, background sync
│   └── Real-time State (Socket.io client for live notification updates)
├── WebSocket Layer
│   ├── Socket.io Client (WebSocket connection for real-time notifications)
│   ├── Event Handlers (New notification received, notification read, notification dismissed)
│   └── Connection Management (Auto-reconnect, heartbeat, connection state)
├── API Integration
│   ├── API Client (Axios with interceptors for auth, error handling)
│   ├── API Services (notificationService, preferenceService)
│   └── Request/Response Transformation (Data normalization and error handling)
└── Routing
    ├── Public Routes (Home)
    ├── Protected Routes (Notifications, Settings)
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
  - Real-time notifications via WebSocket
  - Responsive design for mobile and desktop
  - Modern React 19 features for better performance and UX

- **CDN/Edge**:
  - Global distribution of static assets
  - Edge caching for improved performance
  - DDoS protection and rate limiting at edge

---

## f) App Flow

### Complete System Flow (Frontend Perspective)

**Primary User Flow - Notification Reception:**

1. **User receives notification** → WebSocket connection receives real-time notification event
2. **Notification processing** → useNotifications hook processes notification with useOptimistic (React 19)
3. **UI update** → NotificationBell shows unread count, NotificationDropdown displays new notification
4. **User clicks notification** → NotificationItem navigates to relevant page, marks as read
5. **Read status update** → useMutation updates read status, React Query cache updates
6. **Notification history** → NotificationHistory component displays all notifications

**Component Interaction Flow:**

```
WebSocket Event → useNotifications hook (real-time state)
            ↓
Notification Processing → useOptimistic (React 19) for instant UI
            ↓
State Update → Redux Toolkit (unread count, notification list)
            ↓
Re-render → NotificationBell, NotificationDropdown (receives state)
```

**State Update Flow:**

1. **Real-time State** → WebSocket receives notification events
2. **Optimistic State** → useOptimistic (React 19) shows notifications immediately
3. **Server State** → React Query manages notification history, caching, refetching
4. **Global State** → Redux Toolkit manages unread count, notification preferences
5. **Component Re-render** → React updates UI based on state changes

**Error Handling Flow:**

1. **WebSocket Error** → Connection retries automatically, shows connection status
2. **API Error** → React Query mutation returns error
3. **Error Boundary** → Catches component errors, shows fallback UI
4. **User Feedback** → Toast notification displays error message

**Notification Preferences Flow:**

1. **User navigates** → React Router navigates to /notifications/settings
2. **Preferences display** → NotificationPreferences component shows current settings
3. **User updates preferences** → useNotificationPreferences hook updates preferences
4. **State update** → Redux Toolkit updates preferences, React Query invalidates cache
5. **Confirmation** → Toast notification confirms preference update

**Real-time Notification Flow:**

1. **WebSocket connection** → Socket.io client establishes connection on app load
2. **Notification received** → WebSocket event handler processes notification
3. **Optimistic update** → useOptimistic (React 19) adds notification to list immediately
4. **Badge update** → NotificationBell updates unread count badge
5. **Browser notification** → Shows browser push notification if enabled
6. **User interaction** → User clicks notification, navigates to relevant content

# 3) Component Architecture

Think of the frontend as a tree of React components - each component handles a specific part of the UI, and they work together to create the complete user experience.

**Component Hierarchy:**

```

App
├── Layout
│   ├── Header
│   │   ├── Logo
│   │   ├── Navigation
│   │   └── NotificationBell
│   │       └── NotificationBadge
│   ├── MainContent
│   └── Footer
├── Pages
│   ├── NotificationCenterPage
│   │   ├── NotificationList
│   │   │   └── NotificationItem
│   │   └── NotificationFilters
│   ├── NotificationSettingsPage
│   │   ├── NotificationPreferences
│   │   │   ├── ChannelPreferences
│   │   │   ├── CategoryPreferences
│   │   │   └── QuietHoursSettings
│   │   └── NotificationHistory
│   └── NotificationDropdown
│       ├── NotificationItem
│       └── MarkAllReadButton
└── SharedComponents
    ├── Button
    ├── Input
    ├── Card
    ├── Toast
    └── LoadingSpinner
```

**Key React Components:**

**1. NotificationBell Component:**

- Displays notification icon with unread count badge
- Opens NotificationDropdown on click
- Uses Redux Toolkit for unread count state
- Shows real-time updates via WebSocket
- Uses useOptimistic (React 19) for instant badge updates

**2. NotificationList Component:**

- Displays list of notifications with virtual scrolling
- Fetches notifications with React Query useSuspenseQuery (React 19)
- Handles pagination and infinite scroll
- Uses useTransition (React 19) for non-urgent updates
- Groups notifications by date/category

**3. NotificationItem Component:**

- Displays individual notification with icon, title, message
- Handles click to navigate to relevant page
- Marks notification as read on interaction
- Shows notification timestamp and category
- Uses useOptimistic (React 19) for instant read status updates

**4. NotificationPreferences Component:**

- Manages user notification preferences
- Handles channel, category, and frequency preferences
- Updates preferences with React Query mutation
- Uses useActionState (React 19) for form handling
- Validates preferences before saving

**5. NotificationDropdown Component:**

- Shows recent notifications in dropdown
- Handles mark all as read functionality
- Closes on outside click or escape key
- Uses useOptimistic (React 19) for instant UI updates
- Displays unread count in header

**Component Communication:**

- **Props** → Parent to child data flow
- **Callbacks** → Child to parent communication
- **Context API** → Shared state across components (theme, user)
- **React Query** → Server state management (notifications, preferences)
- **Redux Toolkit** → Global client state (unread count, notification list)
- **WebSocket** → Real-time notification updates

# 4) Data Models

### TypeScript Interfaces

```typescript
interface Notification {
  id: string;
  userId: string;
  type: "in-app" | "push" | "email" | "sms" | "webhook";
  category: "system" | "activity" | "transaction" | "marketing" | "security";
  title: string;
  message: string;
  priority: "low" | "normal" | "high" | "urgent";
  status: "pending" | "sent" | "delivered" | "read" | "failed";
  readAt?: string;
  deliveredAt?: string;
  createdAt: string;
  actionUrl?: string;
  metadata?: Record<string, any>;
}

interface NotificationPreferences {
  userId: string;
  channels: {
    inApp: boolean;
    push: boolean;
    email: boolean;
    sms: boolean;
  };
  categories: {
    system: boolean;
    activity: boolean;
    transaction: boolean;
    marketing: boolean;
    security: boolean;
  };
  frequency: "realtime" | "batched" | "digest";
  quietHours: {
    enabled: boolean;
    startTime: string;
    endTime: string;
  };
}

interface NotificationStats {
  total: number;
  unread: number;
  byCategory: Array<{ category: string; count: number }>;
  byType: Array<{ type: string; count: number }>;
}

interface FormState {
  channel: string;
  category: string;
  frequency: string;
  errors: {
    channel?: string;
    category?: string;
  };
}
```

# 5) API Design

### POST /api/v1/notifications

- **URL:** `/api/v1/notifications`
- **Method:** POST
- **Description:** Create and send a notification
- **Request Body:**

 ```json

 {
 "userId": "user_abc123",
 "type": "in-app",
 "category": "activity",
 "title": "New like",
 "message": "John liked your post",
 "priority": "normal"
 }

 ```

- **Response:**

 ```json

 {
 "success": true,
 "data": {
 "notificationId": "notif_abc123",
 "status": "pending",
 "createdAt": "2024-01-15T10:30:00Z"
 }
 }

 ```

- **Status Codes:** 201 (Created), 400 (Validation Error)

### GET /api/v1/notifications

- **URL:** `/api/v1/notifications?status=unread&limit=20`
- **Method:** GET
- **Description:** Get user notifications
- **Query Parameters:**
 - `status`(optional) - Filter by status (unread, read, all)
 - `limit`(default: 20, max: 100)
- **Response:**

 ```json

 {
 "success": true,
 "data": {
 "notifications": [...],
 "total": 125,
 "unread": 15
 }
 }

 ```

- **Status Codes:** 200 (Success), 401 (Unauthorized)

---

### Redis Cache

**Cache Strategy:**

- **Key Format:** `notifications:{userId}:unread`, `preferences:{userId}`, `user:{userId}:online`
- **Value:** Serialized JSON (notification list, preferences, online status)
- **TTL:**
 - Unread notifications: 300 seconds (5 minutes)
 - User preferences: 3600 seconds (1 hour)
 - Online status: 60 seconds (frequently updated)
- **Eviction Policy:** LRU (Least Recently Used)

**Cache Patterns:**

- **Write-Through Pattern:** Update cache when notifications are created/updated
- **Cache Invalidation:** Invalidate notification cache on new notifications

---

### Error Scenarios and Responses

**Edge Cases Handling:**

- **Invalid User:** Return 404 Not Found when user doesn't exist
- **Preference Check Failed:** Skip notification if user preferences don't allow it
- **Delivery Failure:** Retry failed deliveries with exponential backoff
- **Queue Full:** Return 503 Service Unavailable when queue is full
- **Invalid Notification Format:** Return 400 Bad Request with validation errors

**Error Response Format:**

```json

{
 "error": {
 "code": "DELIVERY_FAILED",
 "message": "Notification delivery failed",
 "details": "Email service unavailable",
 "retryable": true
 }
}

```

---

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

**Custom Hook: useNotifications (React 19)**

```typescript
import { useOptimistic, useTransition } from 'react';
import { useQuery, useMutation } from '@tanstack/react-query';
import { useSocket } from './useSocket';

function useNotifications() {
  const [optimisticNotifications, addOptimisticNotification] = useOptimistic(
    [] as Notification[],
    (currentNotifications, newNotification: Notification) => [...currentNotifications, newNotification]
  );
  const [isPending, startTransition] = useTransition();
  const socket = useSocket();

  // Fetch notifications
  const { data: notifications } = useQuery({
    queryKey: ['notifications'],
    queryFn: fetchNotifications,
    staleTime: 30000
  });

  // Mark as read mutation
  const markAsReadMutation = useMutation({
    mutationFn: markNotificationAsRead,
    onMutate: async (notificationId) => {
      await queryClient.cancelQueries({ queryKey: ['notifications'] });
      const previousNotifications = queryClient.getQueryData(['notifications']);
      queryClient.setQueryData(['notifications'], (old: Notification[]) =>
        old.map(n => n.id === notificationId ? { ...n, status: 'read' } : n)
      );
      return { previousNotifications };
    }
  });

  // Listen for real-time notifications
  useEffect(() => {
    socket.on('notification', (notification: Notification) => {
      addOptimisticNotification(notification);
    });
    return () => socket.off('notification');
  }, [socket]);

  return { notifications: optimisticNotifications, markAsRead: markAsReadMutation.mutate };
}
```

**Component with React Query (React 19):**

```typescript
function NotificationBell() {
  const { notifications, markAsRead } = useNotifications();
  const [isOpen, setIsOpen] = useState(false);
  const [isPending, startTransition] = useTransition();

  const handleNotificationClick = (notification: Notification) => {
    startTransition(() => {
      markAsRead(notification.id);
      navigate(notification.actionUrl);
    });
  };

  return (
    <div>
      <BellIcon onClick={() => setIsOpen(!isOpen)} />
      {isOpen && (
        <NotificationDropdown
          notifications={notifications}
          onNotificationClick={handleNotificationClick}
        />
      )}
    </div>
  );
}
```

# 6) Protocols

### REST API Protocol

**Request Format:**

- HTTP methods: GET, POST, PUT, DELETE
- Headers: Content-Type: application/json
- Authentication: Bearer token in Authorization header

**Response Format:**

- Success: `{ success: true, data: {...} }`
- Error: `{ success: false, error: {...} }`
- Status codes: 200 (Success), 201 (Created), 400 (Bad Request), 401 (Unauthorized), 404 (Not Found), 500 (Server Error)

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
- Example: `useNotifications`, `useNotificationPreferences`, `useSocket`
- Handle data transformation and validation

**Service Functions:**

- Pure functions for data processing and validation
- Notification filtering, grouping, formatting, preference validation

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
- Example: Test Notification System flow from start to finish

# 8) Algorithms

### Frontend Algorithms

**Notification Grouping Algorithm:**

```javascript
function groupNotifications(notifications) {
  const groups = {
    today: [],
    yesterday: [],
    thisWeek: [],
    older: []
  };

  const now = new Date();
  const today = new Date(now.getFullYear(), now.getMonth(), now.getDate());
  const yesterday = new Date(today);
  yesterday.setDate(yesterday.getDate() - 1);
  const weekAgo = new Date(today);
  weekAgo.setDate(weekAgo.getDate() - 7);

  notifications.forEach(notification => {
    const notifDate = new Date(notification.createdAt);
    if (notifDate >= today) {
      groups.today.push(notification);
    } else if (notifDate >= yesterday) {
      groups.yesterday.push(notification);
    } else if (notifDate >= weekAgo) {
      groups.thisWeek.push(notification);
    } else {
      groups.older.push(notification);
    }
  });

  return groups;
}
```

**Notification Filtering Algorithm:**

```javascript
function filterNotifications(notifications, filters) {
  return notifications.filter(notification => {
    if (filters.status && notification.status !== filters.status) return false;
    if (filters.category && notification.category !== filters.category) return false;
    if (filters.type && notification.type !== filters.type) return false;
    if (filters.search) {
      const searchLower = filters.search.toLowerCase();
      return notification.title.toLowerCase().includes(searchLower) ||
             notification.message.toLowerCase().includes(searchLower);
    }
    return true;
  });
}
```

**Unread Count Calculation:**

```javascript
function calculateUnreadCount(notifications) {
  return notifications.filter(n => n.status === 'unread' || !n.readAt).length;
}
```

# 9) Security

### Frontend Security

**Input Validation:**

- Client-side validation before preference submission
- Sanitize notification content to prevent XSS attacks
- Validate preference settings (channel selection, quiet hours)

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

**Situation:** In a notification system, we need to manage real-time notifications, notification preferences, unread counts, and WebSocket connections efficiently.

**Action:**

- Use React Query for server state (notification history, preferences) - handles caching, refetching, and synchronization
- Use `useOptimistic()` (React 19) for instant UI feedback on notification updates
- Use WebSocket for real-time notification delivery
- Use Redux Toolkit for global client state (unread count, notification list)
- Use useState for local component state (dropdown visibility, filters)
- Use Context API for user authentication, theme preferences

**Result:** Real-time notifications delivered instantly, reduced API calls through caching, improved performance, better user experience with instant feedback.

**Takeaway:** Combining React Query for server state, WebSocket for real-time updates, and React 19's optimistic updates provides seamless notification experience.

### Q: How would you implement real-time notifications?

**Answer (STAR Method):**

**Situation:** Users need to receive notifications in real-time as events happen, with instant UI updates.

**Action:**

- Use WebSocket (Socket.io) for real-time connection
- Use `useOptimistic()` (React 19) to show notifications immediately before server confirmation
- Use `useTransition()` (React 19) for non-urgent notification list updates
- Implement connection retry logic with exponential backoff
- Show connection status indicator
- Handle offline scenarios with service worker caching

**Result:** Notifications delivered in < 1 second, instant UI updates, improved user engagement, reliable real-time delivery.

**Takeaway:** WebSocket combined with React 19's optimistic updates provides the best real-time notification experience.
