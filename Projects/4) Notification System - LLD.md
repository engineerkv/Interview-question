# Notification System - Low Level Design (LLD)

> **Project Type:** Full-Stack System Component (MERN Stack)  
> **Tech Stack:** 
> - **Frontend:** React.js, Socket.io Client
> - **Backend:** Node.js, Express.js, MongoDB, Redis, Socket.io Server, RabbitMQ

---

## 3. Component Architecture

**Think of this as the building blocks - how notification components are organized**

### Notification System Components

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

**How components work together:**
- **NotificationAPI** - REST endpoints for creating and managing notifications
- **NotificationProcessor** - Processes notification requests, checks preferences, sends to queue
- **NotificationWorkers** - Workers that consume from queues and deliver notifications
- **PreferenceManager** - Manages user notification preferences
- **DeliveryTracker** - Tracks delivery and read status

---

## 4. Data Models

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

## 5. API Endpoints

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

## 6. Real-time In-App Notifications (WebSocket)

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

## 7. Email Notification Worker

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

## 8. Push Notification Worker

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

## 9. User Preferences Management

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

## 10. Delivery Tracking

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

## 11. Retry Mechanism

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

## 12. Notification Preferences UI

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

