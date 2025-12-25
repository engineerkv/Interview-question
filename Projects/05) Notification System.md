# Notification System

## Overview

Design a scalable notification system that delivers millions of notifications per day across multiple channels (in-app, email, push, SMS) with high reliability and real-time delivery.

---

## 1) Requirements

### Functional Requirements

**Core Features:**
- In-app notifications (real-time via WebSocket)
- Push notifications (browser and mobile)
- Email notifications
- SMS notifications (for critical alerts)
- Notification preferences (channel, category, frequency)
- Notification history
- Read/unread status tracking
- Notification grouping and batching

**Notification Types:**
- System notifications (app updates, maintenance)
- User activity (likes, comments, mentions, follows)
- Transaction notifications (payments, orders)
- Marketing notifications (promotions, offers)
- Security notifications (login alerts, password changes)

**User Preferences:**
- Channel preferences (which channels to receive)
- Category preferences (enable/disable categories)
- Frequency preferences (real-time, batched, digest)
- Quiet hours (don't send during specific times)

### Non-Functional Requirements

**Performance:**
- Real-time delivery: < 1 second
- High throughput: millions of notifications per day
- Low latency for critical alerts

**Reliability:**
- Guaranteed delivery for important notifications
- At-least-once delivery guarantee
- Retry mechanisms for failed deliveries
- Fault tolerance

**User Experience:**
- Non-intrusive (don't overwhelm users)
- Relevant (only send what users care about)
- Actionable (clear actions in notifications)

---

## 2) Component Hierarchy

The frontend is a React application with real-time notification handling. Here's the structure:

```
App
├── Layout
│   ├── Header
│   │   ├── Logo
│   │   ├── NotificationBell (shows unread count)
│   │   │   └── NotificationBadge (unread count)
│   │   └── UserMenu
│   └── MainContent
├── Components
│   ├── NotificationCenter
│   │   ├── NotificationDropdown
│   │   │   ├── NotificationHeader (Mark all read, Settings)
│   │   │   ├── NotificationList
│   │   │   │   └── NotificationItem
│   │   │   │       ├── NotificationIcon (type icon)
│   │   │   │       ├── NotificationContent (title, message)
│   │   │   │       ├── NotificationTime (relative time)
│   │   │   │       ├── UnreadIndicator
│   │   │   │       └── ActionButtons (Mark read, Dismiss)
│   │   │   └── ViewAllButton
│   │   └── NotificationToast (popup notifications)
│   ├── NotificationHistoryPage
│   │   ├── NotificationFilters (category, date, read status)
│   │   ├── NotificationList
│   │   │   └── NotificationItem (same as above)
│   │   └── Pagination
│   └── NotificationSettingsPage
│       ├── ChannelPreferences
│       │   ├── InAppToggle
│       │   ├── EmailToggle
│       │   ├── PushToggle
│       │   └── SMSToggle
│       ├── CategoryPreferences
│       │   ├── SystemNotificationsToggle
│       │   ├── UserActivityToggle
│       │   ├── TransactionToggle
│       │   └── MarketingToggle
│       ├── FrequencyPreferences
│       │   ├── RealTimeRadio
│       │   ├── BatchedRadio
│       │   └── DigestRadio
│       └── QuietHours
│           ├── StartTimePicker
│           └── EndTimePicker
└── SharedComponents
    ├── Toast (for notification toasts)
    └── LoadingSpinner
```

### Key Components Explained

**1. NotificationBell Component**
- Shows unread notification count
- Opens NotificationDropdown on click
- Badge shows unread count
- Updates in real-time via WebSocket

**2. NotificationDropdown Component**
- Dropdown menu with recent notifications
- Shows unread notifications first
- Mark all as read functionality
- Link to full notification history

**3. NotificationItem Component**
- Individual notification card
- Shows icon, title, message, time
- Unread indicator
- Actions: mark read, dismiss
- Clickable to navigate to related content

**4. NotificationToast Component**
- Popup toast notifications
- Appears for important notifications
- Auto-dismisses after few seconds
- Clickable to view full notification

**5. NotificationSettings Component**
- User preference management
- Channel preferences (which channels)
- Category preferences (which categories)
- Frequency preferences (real-time/batched/digest)
- Quiet hours configuration

---

## 3) Data Models

Here are the key data structures:

```typescript
// Notification
interface Notification {
  id: string;
  userId: string;
  type: "system" | "user_activity" | "transaction" | "marketing" | "security";
  category: string;  // "like", "comment", "payment", etc.
  title: string;
  message: string;
  icon?: string;
  imageUrl?: string;
  actionUrl?: string;  // URL to navigate when clicked
  channels: NotificationChannel[];  // Which channels to send to
  priority: "low" | "medium" | "high" | "critical";
  isRead: boolean;
  readAt?: string;
  createdAt: string;
  expiresAt?: string;  // Optional expiration
  metadata?: Record<string, any>;  // Additional data
}

// Notification channel
type NotificationChannel = "in_app" | "email" | "push" | "sms";

// Notification delivery status
interface NotificationDelivery {
  notificationId: string;
  channel: NotificationChannel;
  status: "pending" | "sent" | "delivered" | "failed";
  deliveredAt?: string;
  error?: string;
  retryCount: number;
}

// User notification preferences
interface NotificationPreferences {
  userId: string;
  channels: {
    in_app: boolean;
    email: boolean;
    push: boolean;
    sms: boolean;
  };
  categories: {
    [category: string]: boolean;  // Enable/disable per category
  };
  frequency: "realtime" | "batched" | "digest";
  quietHours: {
    enabled: boolean;
    startTime: string;  // "22:00"
    endTime: string;  // "08:00"
  };
}

// Notification batch (for batched/digest mode)
interface NotificationBatch {
  id: string;
  userId: string;
  notifications: string[];  // Notification IDs
  scheduledAt: string;
  sentAt?: string;
}

// Push notification subscription
interface PushSubscription {
  userId: string;
  endpoint: string;  // Push service endpoint
  keys: {
    p256dh: string;
    auth: string;
  };
  createdAt: string;
}
```

### Data Flow Explanation

**When a notification is created:**
1. System creates notification for user
2. Check user preferences (channels, categories, quiet hours)
3. Filter notifications based on preferences
4. Send to enabled channels (in-app, email, push, SMS)
5. Track delivery status for each channel
6. Retry failed deliveries

**In-app notification flow:**
1. Notification created on server
2. WebSocket sends notification to connected clients
3. Frontend receives notification via WebSocket
4. Show notification in NotificationDropdown
5. Show toast if high priority
6. Update unread count
7. Mark as read when user views/clicks

**Push notification flow:**
1. User subscribes to push notifications
2. Browser generates push subscription
3. Subscription saved to server
4. When notification created, server sends push
5. Browser shows native notification
6. User clicks notification → navigate to app

**Batching flow:**
1. User has frequency preference set to "batched"
2. Notifications are queued instead of sent immediately
3. Batch is sent at scheduled time (e.g., every hour)
4. Multiple notifications grouped in one email/push
5. User receives batched notifications

---

## 4) API Design

### REST Endpoints

**GET /api/v1/notifications**
- Get user notifications
- Query params: `page`, `limit`, `category`, `isRead`, `startDate`, `endDate`
- Returns: Paginated list of Notification objects

**GET /api/v1/notifications/unread-count**
- Get unread notification count
- Returns: `{ count: number }`

**PATCH /api/v1/notifications/:id/read**
- Mark notification as read
- Returns: Updated Notification object

**POST /api/v1/notifications/mark-all-read**
- Mark all notifications as read
- Returns: Success confirmation

**DELETE /api/v1/notifications/:id**
- Dismiss/delete a notification
- Returns: Success confirmation

**GET /api/v1/notifications/preferences**
- Get user notification preferences
- Returns: NotificationPreferences object

**PATCH /api/v1/notifications/preferences**
- Update user notification preferences
- Request body: Partial NotificationPreferences
- Returns: Updated NotificationPreferences

**POST /api/v1/notifications/push/subscribe**
- Subscribe to push notifications
- Request body: PushSubscription object
- Returns: Success confirmation

**POST /api/v1/notifications/push/unsubscribe**
- Unsubscribe from push notifications
- Returns: Success confirmation

### WebSocket Events

**Connection:** `wss://api.example.com/notifications`

**Events:**
- `notification` - New notification received
- `notification_read` - Notification marked as read
- `notification_dismissed` - Notification dismissed

**Message Format:**
```json
{
  "type": "notification",
  "data": {
    "id": "notif_123",
    "type": "user_activity",
    "title": "New like",
    "message": "John liked your post",
    "actionUrl": "/posts/123",
    "createdAt": "2024-01-15T10:00:00Z"
  }
}
```

### API Request/Response Examples

**Get Notifications:**
```json
// GET /api/v1/notifications?page=1&limit=20&isRead=false
// Response
{
  "success": true,
  "data": {
    "notifications": [
      {
        "id": "notif_123",
        "type": "user_activity",
        "category": "like",
        "title": "New like",
        "message": "John liked your post",
        "actionUrl": "/posts/123",
        "isRead": false,
        "createdAt": "2024-01-15T10:00:00Z"
      }
    ],
    "total": 45,
    "page": 1,
    "limit": 20
  }
}
```

**Get Unread Count:**
```json
// GET /api/v1/notifications/unread-count
// Response
{
  "success": true,
  "data": {
    "count": 5
  }
}
```

**Update Preferences:**
```json
// PATCH /api/v1/notifications/preferences
{
  "channels": {
    "in_app": true,
    "email": false,
    "push": true,
    "sms": false
  },
  "categories": {
    "like": true,
    "comment": true,
    "marketing": false
  },
  "frequency": "batched",
  "quietHours": {
    "enabled": true,
    "startTime": "22:00",
    "endTime": "08:00"
  }
}

// Response
{
  "success": true,
  "data": {
    "userId": "user_123",
    "channels": { ... },
    "categories": { ... },
    "frequency": "batched",
    "quietHours": { ... }
  }
}
```

---

## Key Design Decisions

**1. WebSocket for Real-time In-app Notifications**
- Instant delivery for in-app notifications
- Low latency (< 1 second)
- Better user experience
- Auto-reconnect on connection loss

**2. Multi-channel Support**
- Different channels for different notification types
- User preferences control which channels
- Fallback to other channels if one fails
- Critical notifications use multiple channels

**3. Notification Preferences**
- Users control what they receive
- Reduces notification fatigue
- Improves user experience
- Respects quiet hours

**4. Batching and Digest Mode**
- Group multiple notifications together
- Reduces notification spam
- Better for less urgent notifications
- Scheduled delivery

**5. Delivery Status Tracking**
- Track delivery status per channel
- Retry failed deliveries
- Analytics on delivery rates
- Identify delivery issues

**6. Optimistic Updates**
- Show notifications immediately via WebSocket
- Use useOptimistic (React 19) for instant UI
- Better perceived performance
- Sync with server state

---

## Interview Talking Points

**When explaining this system, I'd focus on:**

1. **Requirements First**: Start with core functionality - multi-channel notifications, preferences, real-time delivery

2. **Component Structure**: Explain the React component hierarchy - notification bell, dropdown, settings, history

3. **Data Models**: Walk through Notification, NotificationPreferences, NotificationDelivery - and how preferences filter notifications

4. **API Design**: Show the REST endpoints and WebSocket protocol - get notifications, update preferences, real-time delivery

5. **Key Challenges**: 
   - Real-time delivery with low latency
   - Multi-channel delivery and status tracking
   - User preferences and filtering
   - Batching and digest mode
   - Handling millions of notifications per day

**Example explanation flow:**
> "So for a notification system, the core requirement is delivering notifications across multiple channels (in-app, email, push, SMS) with high reliability. The frontend is a React app with a notification bell component that shows unread count and opens a dropdown with recent notifications. For real-time in-app notifications, we use WebSocket to deliver notifications instantly (< 1 second). The data model includes Notification objects with type, category, channels, and delivery status. Users have NotificationPreferences that control which channels and categories they receive, plus frequency preferences (real-time, batched, or digest). The main API endpoints handle getting notifications, marking as read, and managing preferences. For push notifications, users subscribe and we send push notifications through the browser's push service. Key challenges include ensuring real-time delivery, respecting user preferences, handling batching for less urgent notifications, and tracking delivery status across multiple channels."
