# Notification System

> **Project Type:** Full-Stack System Component (MERN Stack)
> **Purpose:** Design and implement a notification system to send real-time notifications to users across multiple channels
> **Tech Stack:**
> - **Frontend:** React.js, Socket.io Client
> - **Backend:** Node.js, Express.js, MongoDB, Redis, Socket.io Server, Message Queue (RabbitMQ/Kafka)
> - **Services:** SendGrid (Email), FCM (Push), Twilio (SMS)
> **Key Features:** Multi-channel notifications, real-time delivery, notification preferences, delivery tracking

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

## a) Requirements

### i) Functional Requirements

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

### ii) Non-Functional Requirements

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

## b) Scope and Priority

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

## c) Technology Choices

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

- **PostgreSQL / MongoDB:** For notification history and preferences
  - **Why database?** Persistent storage, query notification history

---

## d) Capacity Estimation

### Throughput Requirements

- **Total Users**: 100 million users
- **Daily Active Users (DAU)**: 50 million users per day
- **Peak Traffic**: 3x average during peak hours (150 million users per day)
- **Notifications per Day**: 500 million notifications
- **Average Notification Size**: 1 KB (metadata + content)
- **Read:Write Ratio**: 5:1 (reading notifications vs creating notifications)

**Calculations:**
- **Average Writes Per Second (WPS)**: 500M notifications / 86,400 seconds ≈ 5,787 WPS
- **Peak WPS**: 5,787 × 3 = 17,361 WPS
- **Average Reads Per Second (RPS)**: 5,787 × 5 = 28,935 RPS
- **Peak RPS**: 28,935 × 3 = 86,805 RPS
- **Concurrent Connections**: 10 million concurrent WebSocket connections for in-app notifications

### Storage Estimation

**Storage per Notification:**
- Notification metadata: 500 bytes (id, userId, type, channel, status, timestamps)
- Notification content: 500 bytes (title, message, action URL)
- **Total per Notification**: 1 KB

**Storage Requirements:**
- **Notifications per Year**: 500M notifications/day × 365 = 182.5 billion notifications
- **Notification Storage**: 182.5B × 1 KB ≈ 182.5 TB per year
- **User Preferences**: 100M users × 2 KB ≈ 200 GB
- **Delivery Logs**: 182.5B notifications × 200 bytes ≈ 36.5 TB/year
- **Total Storage**: ~182.5 TB (notifications) + 200 GB (preferences) + 36.5 TB (logs) ≈ 219.2 TB/year

### Bandwidth Estimation

- **Average Notification Bandwidth**: 1 KB per notification
- **Daily Bandwidth**: 500M notifications × 1 KB = 500 TB/day
- **Peak Bandwidth**: 500 TB × 3 = 1,500 TB/day during peak hours
- **Average Bandwidth**: 500 TB / 86,400 seconds ≈ 5.8 TB/s
- **Peak Bandwidth**: 5.8 TB/s × 3 ≈ 17.4 TB/s

### Caching Estimation

Following the **80-20 rule** where 20% of users generate 80% of traffic:
- **Cache 20% of active users' notifications**: 50M × 0.2 = 10M users
- **Cache memory required**: 10M users × 10 KB (recent notifications) = 100 GB (distributed across Redis cluster)
- **Cache hit ratio**: 90% (only 10% of notification requests hit database)
- **Requests hitting Database**: 28,935 × 0.10 ≈ 2,894 RPS (manageable with sharding)

### Infrastructure Sizing

- **WebSocket Servers**: 1,000-2,000 instances behind load balancer, each handling 5,000-10,000 concurrent connections
- **API Servers**: 500-1,000 instances for REST API, each handling 20-50 RPS
- **Message Queue**: RabbitMQ/Kafka cluster with 20-50 nodes for notification distribution
- **Database**: MongoDB/PostgreSQL cluster with 50-100 nodes for storage and high read/write throughput
- **Cache Layer**: Redis cluster with 20-50 nodes for high availability and performance
- **Worker Nodes**: 100-200 instances for processing notifications (in-app, email, push, SMS)
- **External Services**: SendGrid (email), FCM (push), Twilio (SMS) with appropriate rate limits

---

## e) Architecture Overview

The system follows a multi-channel notification architecture with message queues, worker nodes, and real-time delivery. Here's how the complete system works:

### Frontend Architecture

**Frontend Layers:**

1. **Presentation Layer (React Components)**
   - **UI Components**: Reusable components (NotificationBell, NotificationItem, NotificationDropdown, NotificationSettings)
   - **Feature Components**: NotificationCenter, NotificationPreferences, NotificationHistory
   - **Layout Components**: Header, Sidebar, NotificationBadge
   - **Page Components**: NotificationsPage, SettingsPage

2. **State Management Layer**
   - **Local State (useState)**: Component-specific UI state (dropdown open/closed, loading, errors)
   - **Server State (Redux Toolkit)**: Global state for notifications, unread count, preferences
   - **WebSocket State**: Real-time notification updates, unread count updates

3. **WebSocket Layer**
   - **Socket.io Client**: WebSocket connection for real-time notifications
   - **Event Handlers**: New notification received, notification read, notification dismissed
   - **Connection Management**: Auto-reconnect, heartbeat, connection state

4. **API Integration Layer**
   - **API Client**: Axios instance with interceptors for auth, error handling
   - **Redux Thunks**: Async actions for API operations (fetchNotifications, markAsRead, updatePreferences)
   - **Request/Response Transformation**: Data normalization and error handling

5. **Routing Layer (React Router)**
   - **Route Configuration**: Define routes and protected routes
   - **Navigation**: Programmatic and declarative navigation
   - **Route Guards**: Authentication and authorization checks

6. **Build & Deployment Layer**
   - **Build Process**: Webpack/Vite bundling with code splitting
   - **Static Assets**: Served from CDN (CloudFront/Cloudflare)
   - **Environment Configuration**: Environment-specific API endpoints and WebSocket URLs

**Frontend Request Flow:**

1. **User Interaction** → User receives notification or opens notification center
2. **WebSocket Event** → Socket.io receives new notification event
3. **State Update** → Redux action dispatched or local state updated
4. **UI Update** → Components re-render with new notification
5. **User Action** → User clicks notification or marks as read
6. **API Call** → HTTP request to update notification status

### Backend Architecture

**Backend Layers:**

1. **Notification API Layer** - REST API for creating and managing notifications
2. **WebSocket Server Layer** - Handles real-time WebSocket connections for in-app notifications
3. **Message Queue Layer** - RabbitMQ/Kafka for reliable notification distribution
4. **Worker Layer** - Worker nodes for processing notifications across channels
5. **Application Service Layer** - Business logic and orchestration
6. **Cache Layer** - In-memory caching for performance
7. **Database Layer** - Persistent data storage
8. **External Service Layer** - Integration with SendGrid, FCM, Twilio

### Complete Request Flow

**Notification Creation Flow:**
1. **Source**: User action, system event, or scheduled job triggers notification
2. **API Call**: POST request to notification API with notification data
3. **Validation**: Validate notification request, check user preferences
4. **Database**: Create notification record in database
5. **Message Queue**: Send notification to appropriate channel queue (in-app, email, push, SMS)
6. **Worker**: Worker node processes notification from queue
7. **Delivery**: Notification delivered via appropriate channel (WebSocket, email, push, SMS)
8. **Tracking**: Update delivery status in database

**In-App Notification Flow:**
1. **Worker**: In-app worker processes notification from queue
2. **WebSocket**: Check if user is online via WebSocket connection
3. **Delivery**: If online, send notification via WebSocket to client
4. **Offline**: If offline, store notification for later delivery
5. **Frontend**: Client receives notification and displays in UI

**Email Notification Flow:**
1. **Worker**: Email worker processes notification from queue
2. **Template**: Render email template with notification content
3. **SendGrid**: Send email via SendGrid API
4. **Tracking**: Update delivery status based on SendGrid webhook

**Push Notification Flow:**
1. **Worker**: Push worker processes notification from queue
2. **FCM/APNS**: Send push notification via FCM (Android) or APNS (iOS)
3. **Tracking**: Update delivery status based on FCM/APNS response

### Key Components

- **Frontend (React.js)**: Single-page application with WebSocket integration, component-based architecture, Redux for state management, Socket.io client for real-time notifications
- **Notification API**: REST API for creating notifications, managing preferences, retrieving notification history
- **WebSocket Servers**: Stateless servers handling WebSocket connections, real-time notification delivery, online/offline status
- **Load Balancer**: Distributes WebSocket and HTTP traffic across servers, sticky sessions for WebSocket connections
- **Message Queue (RabbitMQ/Kafka)**: Reliable notification distribution, ensures notification delivery, handles retry logic
- **Worker Nodes**: Process notifications from queues, handle channel-specific delivery (in-app, email, push, SMS)
- **Application Services**: Notification Service, Preference Service, Delivery Service, Analytics Service
- **Cache Layer (Redis)**: In-memory cache for recent notifications (20% of traffic), user preferences, unread counts
- **Database (MongoDB/PostgreSQL)**: Sharded across multiple nodes for horizontal scaling, stores notifications, preferences, delivery logs
- **External Services**: SendGrid (email), FCM (push notifications), Twilio (SMS), webhook endpoints

**How it works:**

1. **Event occurs** - User action or system event triggers notification

2. **Notification Service** - Validates, checks preferences, creates notification

3. **Message Queue** - Notification sent to appropriate queue (in-app, email, push)

4. **Workers** - Workers process notifications from queues

5. **Delivery** - Notification delivered via appropriate channel (WebSocket, email, push)

6. **Tracking** - Delivery status tracked and stored

---

## Key Design Decisions

1. **Message Queue Architecture:** Decouples notification generation from delivery - handles spikes, ensures reliability
   - **Why queue?** Can handle millions of notifications, workers process at their own pace
   - **Separate queues** - Different queues for different channels (in-app, email, push)
   - **Reliability** - Queue ensures notifications aren't lost if worker crashes

2. **Socket.io for Real-time:** Provides instant in-app notifications with automatic reconnection
   - **Room-based** - Each user has their own room, receives notifications instantly
   - **Automatic reconnection** - Handles connection drops, user doesn't miss notifications
   - **Fallback support** - Works even if WebSocket is blocked

3. **External Services for Delivery:** Use specialized services for email, push, SMS
   - **Why external?** Better deliverability, handles bounces, spam filtering
   - **Reliability** - These services are experts at delivery
   - **Cost-effective** - Pay per use, no infrastructure to maintain

4. **User Preferences:** Let users control what notifications they receive
   - **Better UX** - Users only get notifications they want
   - **Reduces spam** - Prevents notification fatigue
   - **Compliance** - Required for GDPR, user privacy

5. **Delivery Tracking:** Track if notifications were delivered and read
   - **Analytics** - Understand notification effectiveness
   - **Retry logic** - Retry failed deliveries
   - **User experience** - Show read/unread status

---

# 3) Low Level Design (LLD)

## a) Frontend

### i) Component Architecture

**Component Hierarchy:**

```

NotificationService
├── NotificationAPI
│   ├── CreateNotification (endpoint)
│   ├── GetNotifications (endpoint)
│   ├── MarkAsRead (endpoint)
│   └── UpdatePreferences (endpoint)
├── NotificationProcessor
│   ├── ValidateNotification
│   ├── CheckUserPreferences
│   ├── CreateNotificationRecord
│   └── SendToQueue
├── NotificationWorkers
│   ├── InAppWorker (WebSocket delivery)
│   ├── EmailWorker (Email delivery)
│   ├── PushWorker (Push notification delivery)
│   └── SMSWorker (SMS delivery)
├── PreferenceManager
│   ├── GetUserPreferences
│   ├── UpdatePreferences
│   └── CheckIfNotificationAllowed
└── DeliveryTracker
    ├── TrackDelivery
    ├── TrackRead
    └── UpdateStatus

```

**Component Hierarchy:**

```
App
├── Header
│   ├── Logo
│   ├── Navigation
│   └── NotificationBell
│       ├── BellIcon
│       ├── UnreadBadge
│       └── NotificationDropdown
│           ├── NotificationList
│           │   └── NotificationItem
│           │       ├── Icon
│           │       ├── Message
│           │       ├── Timestamp
│           │       └── ReadIndicator
│           ├── MarkAllAsReadButton
│           └── ViewAllLink
├── MainContent
│   ├── NotificationsPage
│   │   ├── FilterTabs (All, Unread, Mentions)
│   │   ├── NotificationList
│   │   │   └── NotificationItem
│   │   │       ├── Icon
│   │   │       ├── Message
│   │   │       ├── Timestamp
│   │   │       ├── ActionButton
│   │   │       └── DeleteButton
│   │   └── EmptyState
│   └── NotificationPreferencesPage
│       ├── ChannelPreferences
│       │   ├── InAppToggle
│       │   ├── EmailToggle
│       │   ├── PushToggle
│       │   └── SMSToggle
│       ├── CategoryPreferences
│       │   ├── SystemNotifications
│       │   ├── ActivityNotifications
│       │   ├── TransactionNotifications
│       │   └── MarketingNotifications
│       └── QuietHoursSettings
│           ├── EnableToggle
│           ├── StartTime
│           └── EndTime
└── SocketProvider (Real-time notifications)

```

### Key React Components

**Frontend Implementation:**

```typescript
// Notification Bell Component
const NotificationBell: React.FC = () => {
  const [isOpen, setIsOpen] = useState(false);
  const { data: notifications } = useNotifications({ unreadOnly: true });
  const { socket } = useSocket();

  useEffect(() => {
    // Listen for real-time notifications
    socket.on('new-notification', (notification: Notification) => {
      // Update notifications list
      queryClient.setQueryData(['notifications'], (old: any) => {
        return [notification, ...(old || [])];
      });
    });

    return () => {
      socket.off('new-notification');
    };
  }, [socket]);

  const unreadCount = notifications?.filter(n => !n.read).length || 0;

  return (
    <div className="notification-bell">
      <button onClick={() => setIsOpen(!isOpen)}>
        <BellIcon />
        {unreadCount > 0 && <UnreadBadge count={unreadCount} />}
      </button>
      {isOpen && (
        <NotificationDropdown
          notifications={notifications}
          onClose={() => setIsOpen(false)}
        />
      )}
    </div>
  );
};

// Notification Item Component
const NotificationItem: React.FC<{ notification: Notification }> = ({ notification }) => {
  const markAsReadMutation = useMarkAsRead();

  const handleClick = () => {
    if (!notification.read) {
      markAsReadMutation.mutate(notification.id);
    }
    // Navigate to related content
    navigate(notification.link);
  };

  return (
    <div 
      className={`notification-item ${notification.read ? 'read' : 'unread'}`}
      onClick={handleClick}
    >
      <Icon type={notification.type} />
      <div className="notification-content">
        <div className="message">{notification.message}</div>
        <div className="timestamp">{formatTime(notification.createdAt)}</div>
      </div>
      {!notification.read && <div className="unread-indicator" />}
    </div>
  );
};

```

### ii) State Management

**State Management Strategy:**

- **Local State (useState)**: UI state (dropdown open/closed, selected filters, modals)
- **Component State**: Each component manages its own UI state
- **API State**: React Query or SWR for server state (notifications, preferences) - caching, refetching, optimistic updates
- **Global State (Redux Toolkit)**: User authentication, unread count, notification preferences

**Frontend Implementation:**

```typescript
// Using React Query for API state management
import { useQuery, useMutation, useQueryClient } from '@tanstack/react-query';

const useNotifications = (filters?: { unreadOnly?: boolean }) => {
  return useQuery({
    queryKey: ['notifications', filters],
    queryFn: async () => {
      const response = await axios.get('/api/v1/notifications', { params: filters });
      return response.data;
    },
    staleTime: 30 * 1000 // Cache for 30 seconds
  });
};

const useMarkAsRead = () => {
  const queryClient = useQueryClient();
  
  return useMutation({
    mutationFn: async (notificationId: string) => {
      const response = await axios.put(`/api/v1/notifications/${notificationId}/read`);
      return response.data;
    },
    onSuccess: () => {
      // Invalidate notifications list
      queryClient.invalidateQueries({ queryKey: ['notifications'] });
    }
  });
};

```

### Component Interactions

**Data Flow:**

1. **Real-time Notifications** → Socket.io receives notifications, updates NotificationBell
2. **Notification Click** → User clicks notification, marks as read, navigates to content
3. **Preferences Update** → User updates preferences, syncs with backend
4. **Notification List** → NotificationsPage fetches and displays all notifications
5. **Mark All Read** → Bulk action marks all notifications as read

**Event Handling:**

- Socket.io events update notification list in real-time
- Notification clicks mark as read and navigate
- Preference changes sync with backend immediately
- Browser notifications show for desktop alerts
- Unread count updates automatically

### UI/UX Considerations

- **Loading States**: Show skeleton loaders for notification list, spinners for actions
- **Error Handling**: Display user-friendly error messages with retry options
- **Validation**: Client-side validation for preference settings
- **Responsive Design**: Mobile-friendly layout, notification dropdown adapts to screen size
- **Accessibility**: ARIA labels, keyboard navigation, screen reader support, focus management
- **Performance**: Virtual scrolling for long notification lists, lazy loading, real-time updates via WebSocket

---

## Data Models

### Notification Model

```typescript
interface Notification {
  id: string;
  userId: string;
  type: 'in-app' | 'email' | 'push' | 'sms' | 'webhook';
  category: 'system' | 'activity' | 'transaction' | 'marketing' | 'security';
  title: string;
  message: string;
  data?: Record<string, any>;      // Additional data (URLs, actions, etc.)
  priority: 'low' | 'medium' | 'high' | 'urgent';
  status: 'pending' | 'sent' | 'delivered' | 'read' | 'failed';
  channels: string[];               // Which channels to send to
  createdAt: Date;
  sentAt?: Date;
  deliveredAt?: Date;
  readAt?: Date;
  retryCount: number;
  metadata?: Record<string, any>;
}

```

### User Preferences Model

```typescript
interface NotificationPreferences {
  userId: string;
  channels: {
    inApp: boolean;
    email: boolean;
    push: boolean;
    sms: boolean;
  };
  categories: {
    system: ChannelPreferences;
    activity: ChannelPreferences;
    transaction: ChannelPreferences;
    marketing: ChannelPreferences;
    security: ChannelPreferences;
  };
  quietHours: {
    enabled: boolean;
    start: string;        // "22:00"
    end: string;          // "08:00"
    timezone: string;
  };
  frequency: 'realtime' | 'batched' | 'digest';
  digestSchedule?: 'daily' | 'weekly';  // For digest mode
}

```

### Notification Queue Message

```typescript
interface NotificationQueueMessage {
  notificationId: string;
  userId: string;
  type: string;
  channel: string;
  payload: {
    title: string;
    message: string;
    data?: Record<string, any>;
  };
  retryCount: number;
  scheduledAt?: Date;     // For scheduled notifications
}

```

---

## Data APIs

### Create Notification

```typescript
// POST /api/notifications
app.post('/api/notifications', async (req, res) => {
  const { userId, type, category, title, message, data, priority } = req.body;

  // Validate request
  if (!userId || !type || !title || !message) {
    return res.status(400).json({ error: 'Missing required fields' });
  }

  // Check user preferences
  const preferences = await getUserPreferences(userId);
  if (!isNotificationAllowed(preferences, type, category)) {
    return res.status(200).json({
      message: 'Notification not sent - user preferences',
      notificationId: null
    });
  }

  // Create notification record
  const notification = await createNotification({
    userId,
    type,
    category,
    title,
    message,
    data,
    priority,
    status: 'pending'
  });

  // Send to appropriate queue
  await sendToQueue(notification);

  res.json({
    notificationId: notification.id,
    status: 'queued'
  });
});

```

### Get Notifications

```typescript
// GET /api/notifications?userId=123&limit=20&offset=0
app.get('/api/notifications', async (req, res) => {
  const { userId, limit = 20, offset = 0, unreadOnly = false } = req.query;

  const notifications = await getNotifications({
    userId,
    limit: parseInt(limit),
    offset: parseInt(offset),
    unreadOnly: unreadOnly === 'true'
  });

  res.json({
    notifications,
    total: await getNotificationCount(userId, unreadOnly === 'true')
  });
});

```

### Mark as Read

```typescript
// PUT /api/notifications/:id/read
app.put('/api/notifications/:id/read', async (req, res) => {
  const { id } = req.params;
  const { userId } = req.body;

  await markNotificationAsRead(id, userId);

  res.json({ success: true });
});

```

### Update Preferences

```typescript
// PUT /api/notifications/preferences
app.put('/api/notifications/preferences', async (req, res) => {
  const { userId, preferences } = req.body;

  await updateUserPreferences(userId, preferences);

  res.json({ success: true });
});

```

---

## Backend Implementation Details

### Express.js Server Structure

```

server/
├── routes/
│   ├── notifications.js
│   └── preferences.js
├── controllers/
│   ├── NotificationController.js
│   └── PreferenceController.js
├── services/
│   ├── NotificationService.js
│   ├── EmailService.js
│   ├── PushService.js
│   └── SMSService.js
├── workers/
│   ├── emailWorker.js
│   ├── pushWorker.js
│   └── smsWorker.js
└── models/
    ├── Notification.js
    └── Preference.js

```

### Notification Service Implementation

```typescript
class NotificationService {
  async createNotification(data: CreateNotificationDto) {
    // Check user preferences
    // Queue notification to appropriate channel queue
    // Return notification ID
  }

  async sendInAppNotification(userId: string, notification: Notification) {
    // Send via Socket.io to user's room
  }
}

```

---

## Protocols

### REST API Protocol

- **Protocol:** REST (Representational State Transfer)

- **Data Format:** JSON

- **Authentication:** JWT Bearer token

### WebSocket Protocol

- **Protocol:** Socket.io over WebSocket

- **Events:** `notification:new`, `notification:read`, `notification:delivered`

- **Authentication:** JWT token in handshake

### Message Queue Protocol

- **Queue System:** RabbitMQ/Kafka

- **Message Format:** JSON

- **Queues:** `notifications.email`, `notifications.push`, `notifications.sms`

---

## Implementation Details

### Real-time In-App Notifications (WebSocket)

### Socket.io Setup

```typescript
import { Server } from 'socket.io';
import { createServer } from 'http';

const httpServer = createServer();
const io = new Server(httpServer, {
  cors: {
    origin: process.env.FRONTEND_URL,
    methods: ['GET', 'POST']
  }
});

// Authentication middleware
io.use(async (socket, next) => {
  const token = socket.handshake.auth.token;
  try {
    const user = await verifyToken(token);
    socket.data.userId = user.id;
    next();
  } catch (error) {
    next(new Error('Authentication failed'));
  }
});

// User connects
io.on('connection', (socket) => {
  const userId = socket.data.userId;

  // Join user's notification room
  socket.join(`user:${userId}`);

  console.log(`User ${userId} connected`);

  // Send pending notifications
  sendPendingNotifications(socket, userId);

  // Handle disconnect
  socket.on('disconnect', () => {
    console.log(`User ${userId} disconnected`);
  });
});

// Function to send notification to user
export function sendInAppNotification(userId: string, notification: Notification) {
  io.to(`user:${userId}`).emit('notification', {
    id: notification.id,
    type: notification.type,
    category: notification.category,
    title: notification.title,
    message: notification.message,
    data: notification.data,
    createdAt: notification.createdAt
  });
}

```

### In-App Notification Worker

```typescript
// Worker that consumes from in-app notification queue
async function processInAppNotifications() {
  const channel = await rabbitmq.createChannel();
  await channel.assertQueue('notifications:in-app');

  channel.consume('notifications:in-app', async (msg) => {
    if (!msg) return;

    try {
      const notification: NotificationQueueMessage = JSON.parse(msg.content.toString());

      // Send via WebSocket
      sendInAppNotification(notification.userId, notification.payload);

      // Update notification status
      await updateNotificationStatus(notification.notificationId, 'delivered', {
        deliveredAt: new Date()
      });

      channel.ack(msg);
    } catch (error) {
      console.error('Error processing in-app notification:', error);
      // Retry or send to dead letter queue
      channel.nack(msg, false, true); // Requeue
    }
  });
}

```

---

## Email Notification Worker

```typescript
import sgMail from '@sendgrid/mail';

sgMail.setApiKey(process.env.SENDGRID_API_KEY);

async function processEmailNotifications() {
  const channel = await rabbitmq.createChannel();
  await channel.assertQueue('notifications:email');

  channel.consume('notifications:email', async (msg) => {
    if (!msg) return;

    try {
      const notification: NotificationQueueMessage = JSON.parse(msg.content.toString());

      // Get user email
      const user = await getUser(notification.userId);

      // Send email
      await sgMail.send({
        to: user.email,
        from: 'noreply@example.com',
        subject: notification.payload.title,
        text: notification.payload.message,
        html: generateEmailHTML(notification.payload)
      });

      // Update notification status
      await updateNotificationStatus(notification.notificationId, 'delivered', {
        deliveredAt: new Date()
      });

      channel.ack(msg);
    } catch (error) {
      console.error('Error sending email:', error);

      // Retry logic
      if (notification.retryCount < 3) {
        notification.retryCount++;
        channel.nack(msg, false, true); // Requeue
      } else {
        // Send to dead letter queue
        await updateNotificationStatus(notification.notificationId, 'failed');
        channel.ack(msg);
      }
    }
  });
}

```

---

## Push Notification Worker

```typescript
import admin from 'firebase-admin';

admin.initializeApp({
  credential: admin.credential.cert(serviceAccount)
});

async function processPushNotifications() {
  const channel = await rabbitmq.createChannel();
  await channel.assertQueue('notifications:push');

  channel.consume('notifications:push', async (msg) => {
    if (!msg) return;

    try {
      const notification: NotificationQueueMessage = JSON.parse(msg.content.toString());

      // Get user's FCM tokens
      const tokens = await getUserFCMTokens(notification.userId);

      if (tokens.length === 0) {
        // No tokens, skip
        channel.ack(msg);
        return;
      }

      // Send push notification
      const message = {
        notification: {
          title: notification.payload.title,
          body: notification.payload.message
        },
        data: notification.payload.data || {},
        tokens: tokens
      };

      const response = await admin.messaging().sendMulticast(message);

      // Handle failed tokens
      if (response.failureCount > 0) {
        const failedTokens = [];
        response.responses.forEach((resp, idx) => {
          if (!resp.success) {
            failedTokens.push(tokens[idx]);
          }
        });
        // Remove invalid tokens
        await removeFCMTokens(notification.userId, failedTokens);
      }

      // Update notification status
      await updateNotificationStatus(notification.notificationId, 'delivered', {
        deliveredAt: new Date()
      });

      channel.ack(msg);
    } catch (error) {
      console.error('Error sending push notification:', error);
      channel.nack(msg, false, true); // Requeue
    }
  });
}

```

---

## User Preferences Management

### Check if Notification Allowed

```typescript
async function isNotificationAllowed(
  preferences: NotificationPreferences,
  type: string,
  category: string
): Promise<boolean> {
  // Check if channel is enabled
  if (!preferences.channels[type as keyof typeof preferences.channels]) {
    return false;
  }

  // Check if category is enabled for this channel
  const categoryPrefs = preferences.categories[category as keyof typeof preferences.categories];
  if (!categoryPrefs[type as keyof typeof categoryPrefs]) {
    return false;
  }

  // Check quiet hours
  if (preferences.quietHours.enabled) {
    const now = new Date();
    const currentTime = now.toLocaleTimeString('en-US', {
      hour12: false,
      timeZone: preferences.quietHours.timezone
    });

    const start = preferences.quietHours.start;
    const end = preferences.quietHours.end;

    if (isInQuietHours(currentTime, start, end)) {
      return false;
    }
  }

  return true;
}

```

### Batching Notifications

```typescript
// Batch notifications for users who prefer batched mode
async function batchNotifications(userId: string) {
  const preferences = await getUserPreferences(userId);

  if (preferences.frequency !== 'batched') {
    return; // User wants real-time, don't batch
  }

  // Get pending notifications
  const pending = await getPendingNotifications(userId);

  if (pending.length === 0) {
    return;
  }

  // Group by category
  const grouped = groupBy(pending, 'category');

  // Send batched notification
  for (const [category, notifications] of Object.entries(grouped)) {
    await sendBatchedNotification(userId, category, notifications);
  }
}

// Run batching every 5 minutes
setInterval(() => {
  const users = getUsersWithBatchedPreferences();
  users.forEach(userId => batchNotifications(userId));
}, 5 * 60 * 1000);

```

---

## Delivery Tracking

### Track Delivery Status

```typescript
async function trackDelivery(
  notificationId: string,
  status: 'sent' | 'delivered' | 'read' | 'failed',
  metadata?: Record<string, any>
) {
  const update: Partial<Notification> = {
    status,
    ...(status === 'sent' && { sentAt: new Date() }),
    ...(status === 'delivered' && { deliveredAt: new Date() }),
    ...(status === 'read' && { readAt: new Date() }),
    metadata: { ...metadata }
  };

  await updateNotification(notificationId, update);
}

// Track read status via WebSocket
io.on('connection', (socket) => {
  socket.on('notification:read', async (data) => {
    const { notificationId } = data;
    await trackDelivery(notificationId, 'read');
  });
});

```

### React Client Implementation

```typescript
// React component for receiving notifications
import { useEffect, useState } from 'react';
import { io, Socket } from 'socket.io-client';

const useNotifications = (userId: string) => {
  const [socket, setSocket] = useState<Socket | null>(null);
  const [notifications, setNotifications] = useState<Notification[]>([]);

  useEffect(() => {
    const token = localStorage.getItem('auth_token');
    const newSocket = io(process.env.REACT_APP_SOCKET_URL, {
      auth: { token }
    });

    newSocket.on('connect', () => {
      console.log('Connected to notification server');
    });

    newSocket.on('notification', (notification: Notification) => {
      setNotifications(prev => [notification, ...prev]);

      // Show browser notification if permission granted
      if ('Notification' in window && Notification.permission === 'granted') {
        new Notification(notification.title, {
          body: notification.message,
          icon: '/icon.png'
        });
      }
    });

    setSocket(newSocket);

    return () => {
      newSocket.close();
    };
  }, [userId]);

  const markAsRead = (notificationId: string) => {
    socket?.emit('notification:read', { notificationId });
    setNotifications(prev =>
      prev.map(n => n.id === notificationId ? { ...n, status: 'read' } : n)
    );
  };

  return { notifications, markAsRead };
};

```

---

## Retry Mechanism

### Exponential Backoff Retry

```typescript
async function retryNotification(
  notification: NotificationQueueMessage,
  maxRetries: number = 3
) {
  let retryCount = notification.retryCount || 0;

  while (retryCount < maxRetries) {
    try {
      // Wait before retry (exponential backoff)
      const delay = Math.pow(2, retryCount) * 1000; // 1s, 2s, 4s
      await sleep(delay);

      // Retry sending
      await sendNotification(notification);

      return; // Success
    } catch (error) {
      retryCount++;

      if (retryCount >= maxRetries) {
        // Max retries reached, send to dead letter queue
        await sendToDeadLetterQueue(notification);
        await updateNotificationStatus(notification.notificationId, 'failed');
      }
    }
  }
}

```

---

## Notification Preferences UI

### React Component for Preferences

```typescript
const NotificationPreferences: React.FC = () => {
  const [preferences, setPreferences] = useState<NotificationPreferences | null>(null);

  const updatePreference = async (path: string, value: boolean) => {
    const updated = setNestedValue(preferences, path, value);
    setPreferences(updated);

    await axios.put('/api/notifications/preferences', {
      userId: currentUser.id,
      preferences: updated
    });
  };

  return (
    <div>
      <h2>Notification Preferences</h2>

      <div>
        <h3>Channels</h3>
        <label>
          <input
            type="checkbox"
            checked={preferences?.channels.inApp}
            onChange={(e) => updatePreference('channels.inApp', e.target.checked)}
          />
          In-App Notifications
        </label>
        {/* Similar for email, push, sms */}
      </div>

      <div>
        <h3>Categories</h3>
        {Object.entries(preferences?.categories || {}).map(([category, prefs]) => (
          <div key={category}>
            <h4>{category}</h4>
            {Object.entries(prefs).map(([channel, enabled]) => (
              <label key={channel}>
                <input
                  type="checkbox"
                  checked={enabled}
                  onChange={(e) =>
                    updatePreference(`categories.${category}.${channel}`, e.target.checked)
                  }
                />
                {channel}
              </label>
            ))}
          </div>
        ))}
      </div>
    </div>
  );
};

```

---

# 4) Algorithms

## Notification Batching Algorithm

**Purpose:** Batch multiple notifications for users who prefer batched delivery instead of real-time.

**Algorithm:**
1. Collect notifications for user over time window (e.g., 5 minutes)
2. Group notifications by category
3. Create batched notification with summary
4. Send batched notification at end of time window
5. Reset timer for next batch

**Implementation:**

```typescript
class NotificationBatcher {
  private batches: Map<string, Notification[]> = new Map();
  private timers: Map<string, NodeJS.Timeout> = new Map();
  private batchWindow = 5 * 60 * 1000; // 5 minutes
  
  addNotification(userId: string, notification: Notification): void {
    if (!this.batches.has(userId)) {
      this.batches.set(userId, []);
      this.startBatchTimer(userId);
    }
    
    this.batches.get(userId)!.push(notification);
  }
  
  private startBatchTimer(userId: string): void {
    const timer = setTimeout(() => {
      this.sendBatch(userId);
      this.batches.delete(userId);
      this.timers.delete(userId);
    }, this.batchWindow);
    
    this.timers.set(userId, timer);
  }
  
  private async sendBatch(userId: string): Promise<void> {
    const notifications = this.batches.get(userId) || [];
    if (notifications.length === 0) return;
    
    // Group by category
    const grouped = this.groupByCategory(notifications);
    
    // Send batched notification
    for (const [category, categoryNotifications] of Object.entries(grouped)) {
      await this.sendBatchedNotification(userId, category, categoryNotifications);
    }
  }
}

```

**Complexity:**
- Time: O(n) where n is number of notifications
- Space: O(n) for batching
- **Batching Efficiency:** Reduces notification spam for users

---

## Notification Priority Queue Algorithm

**Purpose:** Prioritize urgent notifications over regular notifications for faster delivery.

**Algorithm:**
1. Assign priority levels to notifications (urgent, high, normal, low)
2. Use priority queue to order notifications
3. Process high-priority notifications first
4. Respect user preferences even for urgent notifications

**Implementation:**

```typescript
class PriorityNotificationQueue {
  private queues: Map<string, Notification[]> = new Map();
  
  enqueue(notification: Notification): void {
    const priority = notification.priority || 'normal';
    
    if (!this.queues.has(priority)) {
      this.queues.set(priority, []);
    }
    
    this.queues.get(priority)!.push(notification);
  }
  
  dequeue(): Notification | null {
    // Process in priority order: urgent > high > normal > low
    const priorities = ['urgent', 'high', 'normal', 'low'];
    
    for (const priority of priorities) {
      const queue = this.queues.get(priority);
      if (queue && queue.length > 0) {
        return queue.shift()!;
      }
    }
    
    return null;
  }
}

```

**Complexity:**
- Time: O(1) for enqueue/dequeue
- Space: O(n) for queues
- **Priority Delivery:** Urgent notifications delivered faster

---

# 5) Data Models

## Notifications Collection (MongoDB)

```javascript
{
  _id: ObjectId,
  notificationId: String,   // Unique notification ID, indexed
  userId: ObjectId,         // User reference, indexed
  type: String,            // in-app, email, push, sms, webhook
  category: String,        // system, activity, transaction, marketing, security
  title: String,           // Notification title
  message: String,         // Notification message
  data: Object,            // Additional data
  priority: String,        // urgent, high, normal, low
  status: String,          // pending, sent, delivered, read, failed
  sentAt: Date,           // Sent timestamp
  deliveredAt: Date,      // Delivered timestamp
  readAt: Date,           // Read timestamp
  createdAt: Date,        // Created timestamp, indexed
  updatedAt: Date         // Updated timestamp
}

// Indexes:
// - { notificationId: 1 } (unique)
// - { userId: 1, createdAt: -1 } (compound)
// - { status: 1, createdAt: -1 } (compound)
// - { type: 1, status: 1 } (compound)

```

## Notification Preferences Collection (MongoDB)

```javascript
{
  _id: ObjectId,
  userId: ObjectId,         // User reference, indexed (unique)
  channels: Object,         // { inApp: boolean, email: boolean, push: boolean, sms: boolean }
  categories: Object,       // Category preferences per channel
  frequency: String,        // realtime, batched, digest
  quietHours: Object,       // { enabled: boolean, start: string, end: string, timezone: string }
  createdAt: Date,
  updatedAt: Date
}

// Indexes:
// - { userId: 1 } (unique)

```

---

# 6) Database Transactions and Consistency

### MongoDB Transactions

**Transaction Usage:**
- **Multi-Document Transactions** - For operations requiring ACID guarantees
- **Example:** Notification creation + preference check + status update in single transaction
- **Session Management:** Use MongoDB sessions for transaction control

**Example:**

```typescript
const session = await mongoose.startSession();
session.startTransaction();
try {
  await Notification.create([notificationData], { session });
  await User.updateOne({ userId }, { $inc: { notificationCount: 1 } }, { session });
  await session.commitTransaction();
} catch (error) {
  await session.abortTransaction();
  throw error;
} finally {
  session.endSession();
}

```

### Consistency Strategies

**Data Consistency:**
- **Notification Consistency:** Use transactions for notification operations to ensure atomicity
- **Preference Consistency:** Ensure preference updates are atomic
- **Status Consistency:** Track notification status consistently
- **Eventual Consistency:** Accept eventual consistency for delivery status updates (may update with slight delay)

---

# 7) Protocols

### REST API Protocol

- **Protocol:** REST (Representational State Transfer)
- **Data Format:** JSON
- **HTTP Methods:** GET, POST, PUT, DELETE
- **Status Codes:** 200 (Success), 201 (Created), 400 (Bad Request), 401 (Unauthorized), 404 (Not Found), 500 (Server Error)
- **Authentication:** JWT Bearer token in Authorization header

### WebSocket Protocol

- **Protocol:** Socket.io over WebSocket
- **Events:** `notification:new`, `notification:read`, `notification:delivered`
- **Authentication:** JWT token in handshake
- **Use Case:** Real-time in-app notifications

### Message Queue Protocol

- **Queue System:** RabbitMQ/Kafka
- **Message Format:** JSON
- **Queues:** `notifications:in-app`, `notifications:email`, `notifications:push`, `notifications:sms`
- **Use Case:** Reliable notification delivery

---

# 8) API Design

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
  - `status`: string (optional) - Filter by status (unread, read, all)
  - `limit`: number (default: 20, max: 100)
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

# 9) Caching Strategy

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
- **Cache-Aside Pattern:** Check cache first, if miss query database and update cache
- **Write-Through Pattern:** Update cache when notifications are created/updated
- **Cache Invalidation:** Invalidate notification cache on new notifications

---

# 10) Error Handling

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

# 11) Deployment and DevOps

### Scalability

**API Layer:**
- Deploy API layer across multiple instances behind load balancer
- Use auto-scaling based on CPU/memory metrics
- Stateless design allows horizontal scaling

**Worker Scaling:**
- **Worker Scaling:** Scale workers independently per channel based on queue length
- **Queue System:** Use message queue for reliable notification delivery
- **Horizontal Scaling:** Add more workers as notification volume grows

**Database Scaling:**
- **Read Replicas:** Deploy read replicas for notification queries
- **Sharding:** Shard notifications by userId for write scaling
- **Connection Pooling:** Use connection pooling to manage database connections

**Caching:**
- Distributed Redis cluster for high availability
- Cache notifications and preferences
- Reduces database load significantly

### Availability

**Replication:**
- Database replication ensures data availability
- Multi-region replication for disaster recovery

**Failover:**
- Automated failover mechanisms for API and data store layers
- Health checks and monitoring for proactive failover
- Circuit breaker pattern to prevent cascading failures

**Geo-Distributed Deployment:**
- Deploy service across multiple geographical regions
- Reduces latency for users worldwide
- Improves availability by eliminating single point of failure

### Frontend Deployment

**Build Process:**
- **Production Build:** Optimized bundle with code splitting
- **CDN Deployment:** Deploy static assets to CDN for fast global delivery
- **Environment Variables:** `.env.production` for production config

**Deployment Platforms:**
- **Vercel / Netlify** - Automatic deployments from Git
- **AWS S3 + CloudFront** - Static site hosting with CDN

### Backend Deployment

**Server Setup:**
- **PM2:** Process manager with clustering for Node.js apps
- **Nginx:** Load balancer and reverse proxy with SSL termination
- **Docker:** Containerized deployment for consistency
- **Kubernetes:** Container orchestration for auto-scaling

**CI/CD Pipeline:**
- **Automated Testing:** Run tests before deployment
- **Zero-Downtime:** Rolling deployment strategy
- **Health Checks:** Verify notification endpoints are healthy
- **Blue-Green Deployment:** Maintain two identical production environments

### Database Deployment

**MongoDB Setup:**
- **MongoDB Atlas** - Managed MongoDB service with automatic backups
- **Backup Strategy:** Daily automated backups with point-in-time recovery
- **Indexing:** Proper indexes on notificationId, userId, status, createdAt
- **Replication:** Replica sets for high availability

**Redis Setup:**
- **Redis Cloud / AWS ElastiCache** - Managed Redis service
- **Cluster Mode:** Redis cluster for high availability and performance
- **Persistence:** RDB snapshots and AOF for data durability

---

# 12) Security Considerations

### Rate Limiting

- Implement rate limiting at API layer to prevent abuse
- Limit number of notifications per user per minute/hour
- Use Redis for distributed rate limiting across multiple servers

### Input Validation

- Validate all API inputs (notification data, preferences)
- Sanitize user input to prevent XSS attacks
- Validate notification content for malicious content

### HTTPS/TLS

- All communication between clients and API encrypted using HTTPS
- Prevents eavesdropping and man-in-the-middle attacks
- SSL/TLS certificates for secure connections

### Authentication and Authorization

- **JWT Tokens:** Use JWT for stateless authentication
- **Token Expiration:** Set appropriate token expiration times
- **Role-Based Access Control:** Implement RBAC for notification operations
- **User Verification:** Verify user owns notification before allowing access

### Privacy

- **Data Privacy:** Don't expose sensitive data in notifications
- **Preference Privacy:** Respect user privacy preferences
- **Notification Content:** Sanitize notification content to prevent information leakage

### Monitoring and Alerts

- Set up monitoring for unusual notification patterns
- Trigger alerts for potential security issues
- Track metrics: notification rates, delivery rates, error rates
- Log all operations for security auditing

---

# 3) Interview Answers

---

## Q1. 💡 Most complex technical challenge in building the notification system

**Situation:** Building a notification system that delivers millions of notifications per day across multiple channels (in-app, email, push, SMS) with real-time delivery, user preferences, reliable delivery guarantees, and horizontal scalability.

**Action:** The most complex challenge was implementing reliable multi-channel notification delivery with user preferences and real-time in-app notifications. **Backend (Node.js/Express.js):**, I implemented a **message queue architecture** using RabbitMQ - notifications are queued in separate queues per channel (in-app, email, push, SMS). I created **worker processes** that consume from queues and deliver notifications. I implemented **Socket.io server** for real-time in-app notifications - users join notification rooms, and workers send notifications via Socket.io. I integrated **external services** (email service for email, push notification service for push, SMS service for SMS) with proper error handling and retry mechanisms. I implemented **user preference system** in MongoDB that checks if notification should be sent based on channel and category preferences. **Frontend (React.js):**, I created Socket.io client that receives real-time notifications and updates UI. I implemented **notification preferences UI** where users can configure channels and categories.

**Result:** Successfully delivered a reliable notification system. System handles millions of notifications per day. 99.9% delivery success rate. Real-time in-app notifications work with < 1 second latency. User preferences are respected. System scales horizontally.

**Takeaway:** Message queue architecture is essential for reliable notification delivery. Separate queues per channel enable independent scaling. Socket.io provides real-time in-app notifications. User preferences must be checked before sending. Retry mechanisms ensure delivery.

---

## Q2. ⏰ ⏰ ⏰ Implementing real-time in-app notifications using Socket.io in the MERN stack

**Situation:** Users needed to receive instant in-app notifications when events occur (likes, comments, mentions) without page refresh, requiring real-time WebSocket communication.

**Action:** I implemented real-time notifications using Socket.io. **Backend (Node.js/Express.js):**, I set up a **Socket.io server** integrated with Express.js. I implemented **authentication middleware** for Socket.io - clients send JWT token during handshake, server validates it. I used **room-based messaging** - users join their notification room (`user:${userId}`), and when a notification is created, server sends it to that room. I used **Redis adapter** for Socket.io to enable horizontal scaling across multiple servers. I implemented **notification workers** that consume from RabbitMQ queue and send notifications via Socket.io. **Frontend (React.js):**, I created Socket.io client using `socket.io-client` library. I implemented a **custom hook `useNotifications`** that manages Socket.io connection, handles reconnection, and updates Redux state when receiving notifications. I added **notification UI components** that display notifications in real-time. I implemented **browser notifications** using Web Notifications API for desktop alerts.

**Result:** Real-time in-app notifications work seamlessly with < 1 second latency. Users receive notifications instantly without page refresh. System handles 10,000+ concurrent Socket.io connections. Automatic reconnection ensures 99% connection success rate. User engagement increased by 30% with real-time notifications.

**Takeaway:** Socket.io with Redis adapter enables scalable real-time notifications. Room-based messaging targets specific users. Custom React hooks encapsulate Socket.io logic. Browser notifications enhance user experience. Always implement reconnection logic.

---

## Q3. 🔢 Designing the message queue architecture using RabbitMQ for reliable delivery

**Situation:** The system needed to reliably deliver millions of notifications per day across multiple channels, handling failures, retries, and ensuring no notifications are lost.

**Action:** I implemented a message queue architecture using RabbitMQ. I created **separate queues per channel** - `notifications:in-app`, `notifications:email`, `notifications:push`, `notifications:sms` to enable independent processing and scaling. I implemented **worker processes** that consume from queues - each worker type handles one channel (in-app worker, email worker, push worker, SMS worker). I configured **message persistence** - messages are persisted to disk to survive broker restarts. I implemented **acknowledgment mechanism** - workers acknowledge messages only after successful delivery, unacknowledged messages are requeued. I added **dead letter queues** for messages that fail after max retries. I implemented **retry mechanism** with exponential backoff - failed deliveries are retried up to 3 times with increasing delays. I added **message TTL** to prevent old notifications from being delivered. I implemented **priority queues** for urgent notifications.

**Result:** Message queue architecture ensures reliable delivery. 99.9% delivery success rate. Failed notifications are retried automatically. Dead letter queue captures permanently failed notifications. System handles millions of notifications per day. Workers can scale independently per channel.

**Takeaway:** Message queues are essential for reliable notification delivery. Separate queues per channel enable independent scaling. Acknowledgment ensures messages aren't lost. Retry mechanisms handle transient failures. Dead letter queues capture permanent failures.

---

## Q4. 💡 Implementing user notification preferences and quiet hours

**Situation:** Users needed to control which notifications they receive (channels, categories) and when (quiet hours), requiring flexible preference system.

**Action:** I implemented a comprehensive preference system. I created **preference schema in MongoDB** with structure: channels (in-app, email, push, SMS), categories (system, activity, transaction, marketing, security), quiet hours (enabled, start time, end time, timezone), and frequency (realtime, batched, digest). I implemented **preference checking** before sending notifications - notification service checks if user has enabled the channel and category. I added **quiet hours logic** - if current time is within quiet hours, notifications are queued for later delivery (except urgent notifications). I created **preference update API** that allows users to update preferences. **Frontend (React.js):**, I built **preference UI** where users can configure channels, categories, and quiet hours. I implemented **real-time preference updates** - when preferences change, they're immediately applied.

**Result:** User preferences are respected. 95% of users configure preferences. Quiet hours prevent notification spam. System reduces unwanted notifications by 40%. User satisfaction improved significantly.

**Takeaway:** User preferences are essential for notification systems. Check preferences before sending. Quiet hours prevent notification fatigue. Make preferences easy to configure. Apply preferences in real-time.

---

## Q5. 💡 Handling delivery tracking and read receipts for notifications

**Situation:** System needed to track if notifications were delivered and read by users for analytics and user experience.

**Action:** I implemented comprehensive delivery tracking. I created **notification status fields** in MongoDB - `status: pending | sent | delivered | read | failed`. I implemented **delivery tracking** - when notification is sent via channel, status is updated to "sent", when delivery is confirmed (webhook, Socket.io acknowledgment), status is updated to "delivered". For **in-app notifications**, I tracked delivery when Socket.io emits notification and receives acknowledgment. For **email**, I used email service webhooks to track delivery and opens. For **push notifications**, I used push notification service delivery receipts. For **read receipts**, I implemented API endpoint that updates status to "read" when user views notification. **Frontend (React.js):**, I sent read receipt when notification is displayed in UI. I created **analytics dashboard** showing delivery rates, read rates, and channel performance.

**Result:** Delivery tracking works accurately. System tracks 99.9% of deliveries. Read receipts provide engagement metrics. Analytics help optimize notification strategy. User experience improved with read/unread indicators.

**Takeaway:** Delivery tracking is essential for notification systems. Use webhooks and acknowledgments for tracking. Track read receipts for engagement metrics. Analytics help optimize strategy. Provide read/unread indicators in UI.

---
