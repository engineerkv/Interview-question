# Chat Messaging System

> **Project Type:** Full-Stack Web Application (MERN Stack)
> **Scale:** Handle 2B+ users, 100B+ messages per day, real-time delivery
> **Tech Stack:** React.js, Node.js, Express.js, MongoDB, Redis, Socket.io, WebSocket

# 1) Problem Statement

Design and implement a real-time chat messaging system that addresses the following challenges:

- **Core Functionality**: Enable instant message delivery between users with minimal latency, supporting one-on-one and group messaging, message delivery status, and media sharing
- **Scale Requirements**: Handle 2B+ users, 100B+ messages per day, millions of concurrent connections, and real-time message delivery
- **Performance**: Sub-100ms message delivery latency, 99.9% message delivery guarantee, real-time typing indicators and read receipts
- **Message Persistence**: Reliable message storage and retrieval, message search functionality, offline message delivery
- **Real-time Communication**: WebSocket-based real-time messaging, typing indicators, online/offline status, push notifications for offline users
- **Data Consistency**: Maintain message ordering, ensure message delivery even when recipients are offline, handle message delivery status accurately
- **Security**: End-to-end encryption for message privacy, secure authentication and authorization

---

# 2) High Level Design (HLD)

## a) Requirements

### i) Functional Requirements

- One-on-one messaging between users

- Group messaging (up to 256 members)

- Message delivery status (sent, delivered, read)

- Media sharing (images, videos, files)

- Message search

- Push notifications for offline users

### ii) Non-Functional Requirements

- Message delivery latency < 100ms

- 99.9% message delivery guarantee

- Support 2B+ users, 100B+ messages/day

- End-to-end encryption

---

## b) Scope and Priority

### Phase 1: MVP (Must Have) - Priority 1

- One-on-one messaging

- Message delivery

- Basic group messaging

### Phase 2: Enhanced Features - Priority 2

- Media sharing

- Message search

- Push notifications

### Phase 2: Enhanced Features - Priority 2

- Media sharing (images, videos, files)

- Message search functionality

- Push notifications for offline users

- Read receipts and typing indicators

---

## c) Technology Choices

### Backend Framework

- **Node.js with Express.js** - Fast, scalable backend framework

### Database

- **Database** - Primary data storage

### Caching

- **Redis** - In-memory caching for performance

### Additional Services

- **Message Queue** - For async processing

- **CDN** - For content delivery

---

## d) Capacity Estimation

### Throughput Requirements

- **Total Users**: 2 billion users
- **Daily Active Users (DAU)**: 1 billion users per day
- **Peak Traffic**: 3x average during peak hours (3 billion users per day)
- **Messages per Day**: 100 billion messages
- **Average Message Size**: 100 bytes (text messages), 1 MB (media messages)
- **Read:Write Ratio**: 10:1 (reading messages vs sending messages)

**Calculations:**
- **Average Writes Per Second (WPS)**: 100B messages / 86,400 seconds ≈ 1.16M WPS
- **Peak WPS**: 1.16M × 3 = 3.48M WPS
- **Average Reads Per Second (RPS)**: 1.16M × 10 = 11.6M RPS
- **Peak RPS**: 11.6M × 3 = 34.8M RPS
- **Concurrent Connections**: 500 million concurrent WebSocket connections

### Storage Estimation

**Storage per Message:**
- Text message: 100 bytes (message content) + 200 bytes (metadata) = 300 bytes
- Media message: 1 MB (media file) + 200 bytes (metadata) = 1.0002 MB
- **Average per Message**: 80% text (300 bytes) + 20% media (1.0002 MB) ≈ 200 KB

**Storage Requirements:**
- **Messages per Year**: 100B messages/day × 365 = 36.5 trillion messages
- **Message Storage**: 36.5T × 200 KB ≈ 7.3 PB per year
- **User Data**: 2B users × 5 KB ≈ 10 TB
- **Chat Metadata**: 500M chats × 1 KB ≈ 500 TB/year
- **Total Storage**: ~7.3 PB (messages) + 10 TB (users) + 500 TB (chats) ≈ 7.81 PB/year

### Bandwidth Estimation

- **Average Message Bandwidth**: 200 KB per message
- **Daily Bandwidth**: 100B messages × 200 KB = 20,000 TB/day
- **Peak Bandwidth**: 20,000 TB × 3 = 60,000 TB/day during peak hours
- **Average Bandwidth**: 20,000 TB / 86,400 seconds ≈ 231 TB/s
- **Peak Bandwidth**: 231 TB/s × 3 ≈ 693 TB/s

### Caching Estimation

Following the **80-20 rule** where 20% of chats generate 80% of traffic:
- **Cache 20% of active chats**: 500M × 0.2 = 100M chats
- **Cache memory required**: 100M chats × 1 MB (recent messages) = 100 TB (distributed across Redis cluster)
- **Cache hit ratio**: 90% (only 10% of message requests hit database)
- **Requests hitting Database**: 11.6M × 0.10 ≈ 1.16M RPS (manageable with sharding)

### Infrastructure Sizing

- **WebSocket Servers**: 10,000-20,000 instances behind load balancer, each handling 25,000-50,000 concurrent connections
- **API Servers**: 5,000-10,000 instances for REST API, each handling 1,000-2,000 RPS
- **Message Queue**: RabbitMQ/Kafka cluster with 50-100 nodes for message distribution
- **Database**: MongoDB cluster with 200-300 nodes for storage and high read/write throughput
- **Cache Layer**: Redis cluster with 100-200 nodes for high availability and performance
- **Search**: Elasticsearch cluster with 50-100 nodes for message search
- **Media Storage**: AWS S3 or similar object storage for media files
- **CDN**: CloudFront/Cloudflare for media delivery

---

## e) Architecture Overview

### Messages Table

- `messageId` (bigint, primary key)

- `chatId` (string, indexed)

- `senderId` (bigint, indexed)

- `content` (text)

- `type` (enum: text, image, video, file)

- `createdAt` (timestamp, indexed)

- `deliveredAt` (timestamp, nullable)

- `readAt` (timestamp, nullable)

### Chats Table

- `chatId` (string, primary key)

- `type` (enum: one-on-one, group)

- `participants` (json array)

- `lastMessageId` (bigint)

- `updatedAt` (timestamp)

---

## e) Architecture Overview

The system follows a real-time messaging architecture with WebSocket connections, message queues, and distributed storage. Here's how the complete system works:

### Frontend Architecture

**Frontend Layers:**

1. **Presentation Layer (React Components)**
   - **UI Components**: Reusable components (MessageBubble, ChatList, UserAvatar, TypingIndicator)
   - **Feature Components**: ChatWindow, MessageInput, MediaUploader, SearchBar
   - **Layout Components**: Sidebar, ChatHeader, MessageList, InputArea
   - **Page Components**: ChatPage, ContactsPage, SettingsPage

2. **State Management Layer**
   - **Local State (useState)**: Component-specific UI state (input text, loading, errors, typing state)
   - **Server State (Redux Toolkit)**: Global state for chats, messages, users, online status
   - **WebSocket State**: Real-time message updates, typing indicators, online/offline status

3. **WebSocket Layer**
   - **Socket.io Client**: WebSocket connection for real-time messaging
   - **Event Handlers**: Message received, typing started/stopped, user online/offline
   - **Connection Management**: Auto-reconnect, heartbeat, connection state

4. **API Integration Layer**
   - **API Client**: Axios instance with interceptors for auth, error handling
   - **Redux Thunks**: Async actions for API operations (fetchChats, sendMessage, searchMessages)
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

1. **User Interaction** → User sends message or opens chat
2. **WebSocket Event** → Socket.io emits message event to server
3. **State Update** → Redux action dispatched or local state updated
4. **Message Delivery** → Server broadcasts message to recipients via WebSocket
5. **UI Update** → Components re-render with new message
6. **Offline Handling** → Messages queued and delivered when user comes online

### Backend Architecture

**Backend Layers:**

1. **WebSocket Server Layer** - Handles real-time WebSocket connections
2. **API Gateway/Load Balancer** - Entry point for all HTTP and WebSocket requests
3. **Chat Server Layer** - Stateless servers handling WebSocket connections and HTTP requests
4. **Message Queue Layer** - Kafka/RabbitMQ for reliable message distribution
5. **Application Service Layer** - Business logic and orchestration
6. **Cache Layer** - In-memory caching for performance
7. **Database Layer** - Persistent data storage
8. **Search Layer** - Elasticsearch for message search
9. **Media Storage Layer** - Object storage for media files
10. **Push Notification Layer** - FCM/APNS for offline notifications

### Complete Request Flow

**Message Sending Flow:**
1. **Frontend**: User types message and sends
2. **WebSocket**: Socket.io client emits 'send_message' event
3. **Backend**: WebSocket server receives message, validates, stores in message queue
4. **Message Queue**: Message distributed to relevant chat servers
5. **Database**: Message persisted in database
6. **Cache**: Recent messages cached in Redis
7. **Broadcast**: Message broadcasted to all online participants via WebSocket
8. **Push Notification**: Offline users receive push notification
9. **Frontend**: Recipients receive message in real-time

**Message Retrieval Flow:**
1. **Frontend**: User opens chat or scrolls up for history
2. **API Call**: GET request to messages API with chatId and pagination
3. **Backend**: Check Redis cache for recent messages
4. **Database**: Query database for older messages if not in cache
5. **Response**: Return messages with pagination
6. **Frontend**: Display messages in chat window

**Typing Indicator Flow:**
1. **Frontend**: User starts typing
2. **WebSocket**: Socket.io client emits 'typing_start' event
3. **Backend**: WebSocket server broadcasts typing indicator to other participants
4. **Frontend**: Recipients see typing indicator in real-time

### Key Components

- **Frontend (React.js)**: Single-page application with WebSocket integration, component-based architecture, Redux for state management, Socket.io client for real-time communication
- **WebSocket Servers**: Stateless servers handling WebSocket connections, message routing, typing indicators, online/offline status
- **Load Balancer**: Distributes WebSocket and HTTP traffic across chat servers, sticky sessions for WebSocket connections
- **Chat Servers**: Stateless design for horizontal scaling, handle WebSocket connections, HTTP API requests, message routing
- **Message Queue (Kafka/RabbitMQ)**: Reliable message distribution, ensures message delivery, handles offline message queuing
- **Application Services**: Message Service, Chat Service, User Service, Notification Service
- **Cache Layer (Redis)**: In-memory cache for recent messages (20% of traffic), online users, chat metadata
- **Database (MongoDB/Cassandra)**: Sharded across multiple nodes for horizontal scaling, stores messages, chats, users
- **Search (Elasticsearch)**: Fast full-text search for messages, handles message content search
- **Media Storage (AWS S3)**: Object storage for media files (images, videos, files)
- **Push Notification Service**: FCM/APNS for offline message delivery

---

# 3) Low Level Design (LLD)

## a) Frontend

### i) Component Architecture

### Message Service

```typescript
class MessageService {
  async sendMessage(chatId: string, senderId: string, content: string): Promise<Message> {
    // Validate message
    // Store in message queue
    // Return message ID
  }

  async getMessages(chatId: string, limit: number, before?: string): Promise<Message[]> {
    // Query database
    // Return messages
  }
}

```

### Chat Service

```typescript
class ChatService {
  async createChat(participants: string[], type: 'one-on-one' | 'group'): Promise<Chat> {
    // Create chat
    // Return chat ID
  }

  async getChat(chatId: string): Promise<Chat> {
    // Query database
    // Return chat
  }
}

```

---

## Frontend Design

### Component Architecture

Think of the frontend as a tree of React components - each component handles a specific part of the UI, and they work together to create the complete user experience.

**Component Hierarchy:**

```
App
├── Header
│   ├── Logo
│   └── UserMenu (Profile, Settings, Sign out)
├── MainContent
│   ├── ChatListSidebar
│   │   ├── SearchBar
│   │   ├── ChatList
│   │   │   └── ChatListItem
│   │   │       ├── Avatar
│   │   │       ├── ChatName
│   │   │       ├── LastMessage
│   │   │       ├── Timestamp
│   │   │       └── UnreadCount
│   │   └── NewChatButton
│   └── ChatWindow
│       ├── ChatHeader
│       │   ├── ChatName
│       │   ├── OnlineStatus
│       │   └── ChatActions (Info, More)
│       ├── MessageList
│       │   └── MessageItem
│       │       ├── Avatar
│       │       ├── MessageBubble
│       │       │   ├── MessageText
│       │       │   ├── MessageMedia (image, video, file)
│       │       │   ├── Timestamp
│       │       │   └── StatusIndicator (sent, delivered, read)
│       │       └── MessageActions (Reply, Forward, Delete)
│       ├── TypingIndicator
│       └── MessageInput
│           ├── TextInput
│           ├── AttachmentButton
│           ├── EmojiButton
│           └── SendButton
└── SocketProvider (WebSocket connection)

```

**Key React Components:**

```typescript
// Chat Window Component
const ChatWindow: React.FC<{ chatId: string }> = ({ chatId }) => {
  const [messages, setMessages] = useState<Message[]>([]);
  const [inputText, setInputText] = useState('');
  const { socket } = useSocket();
  const { data: chat } = useChat(chatId);

  useEffect(() => {
    // Join chat room
    socket.emit('join-chat', chatId);
    
    // Listen for new messages
    socket.on('new-message', (message: Message) => {
      setMessages(prev => [...prev, message]);
    });

    return () => {
      socket.emit('leave-chat', chatId);
      socket.off('new-message');
    };
  }, [chatId, socket]);

  const handleSendMessage = () => {
    if (!inputText.trim()) return;

    const message: Message = {
      chatId,
      content: inputText,
      type: 'text',
      senderId: currentUserId,
      createdAt: new Date()
};

    // Optimistic update
    setMessages(prev => [...prev, message]);
    setInputText('');

    // Send via Socket.io
    socket.emit('send-message', message);
  };

  return (
    <div className="chat-window">
      <ChatHeader chat={chat} />
      <MessageList messages={messages} />
      <MessageInput
        value={inputText}
        onChange={setInputText}
        onSend={handleSendMessage}
      />
    </div>
  );
};

// Message Item Component
const MessageItem: React.FC<{ message: Message }> = ({ message }) => {
  const isOwn = message.senderId === currentUserId;

  return (
    <div className={`message-item ${isOwn ? 'own' : 'other'}`}>
      {!isOwn && <Avatar userId={message.senderId} />}
      <div className="message-bubble">
        <div className="message-text">{message.content}</div>
        <div className="message-meta">
          <span className="timestamp">{formatTime(message.createdAt)}</span>
          {isOwn && <StatusIndicator status={message.status} />}
        </div>
      </div>
    </div>
  );
};

```

### ii) State Management

**State Management Strategy:**

- **Local State (useState)**: Message input, UI state (loading, errors, selected chat)
- **Component State**: Each component manages its own UI state
- **API State**: React Query or SWR for server state (chat list, message history) - caching, refetching
- **Global State (Redux Toolkit)**: User authentication, active chats, unread counts, socket connection

**Frontend Implementation:**

```typescript
// Using React Query for API state management
import { useQuery, useMutation, useQueryClient } from '@tanstack/react-query';

const useChats = () => {
  return useQuery({
    queryKey: ['chats'],
    queryFn: async () => {
      const response = await axios.get('/api/v1/chats');
      return response.data;
    },
    staleTime: 30 * 1000 // Cache for 30 seconds
  });
};

const useMessages = (chatId: string) => {
  return useInfiniteQuery({
    queryKey: ['messages', chatId],
    queryFn: async ({ pageParam = null }) => {
      const response = await axios.get(`/api/v1/chats/${chatId}/messages`, {
        params: { before: pageParam, limit: 50 }
      });
      return response.data;
    },
    getNextPageParam: (lastPage) => lastPage.nextCursor
  });
};

```

### Component Interactions

**Data Flow:**

1. **Chat Loading** → ChatListSidebar fetches chats via React Query, displays ChatListItem components
2. **Chat Selection** → User clicks chat, ChatWindow loads and joins Socket.io room
3. **Message Sending** → MessageInput sends message via Socket.io, optimistically updates UI
4. **Real-time Updates** → Socket.io receives new messages, updates MessageList
5. **Message History** → Infinite scroll loads older messages from database

**Event Handling:**

- Message input triggers send on Enter key
- Socket.io events update message list in real-time
- Typing indicators show when users are typing
- Read receipts update message status
- File attachments trigger upload before sending

### UI/UX Considerations

- **Loading States**: Show skeleton loaders for chat list, spinners for message sending
- **Error Handling**: Display user-friendly error messages, retry failed messages
- **Validation**: Client-side validation for message content
- **Responsive Design**: Mobile-first layout, optimized for touch interactions
- **Accessibility**: ARIA labels, keyboard navigation, screen reader support
- **Performance**: Virtual scrolling for long message lists, lazy loading for media, message pagination

---

## Data Models

### Message Model

```typescript
interface Message {
  messageId: string;
  chatId: string;
  senderId: string;
  content: string;
  type: 'text' | 'image' | 'video' | 'file';
  createdAt: Date;
  deliveredAt?: Date;
  readAt?: Date;
}

```

### Chat Model

```typescript
interface Chat {
  chatId: string;
  type: 'one-on-one' | 'group';
  participants: string[];
  lastMessageId?: string;
  updatedAt: Date;
}

```

---

## Data APIs

### POST /api/v1/messages

- **URL:** `/api/v1/messages`

- **Method:** POST

- **Request Body:**

  ```json
  {
    "chatId": "chat123",
    "content": "Hello, how are you?",
    "type": "text"
  }

  ```

- **Response:**

  ```json
  {
    "success": true,
    "data": {
      "messageId": "msg_abc123",
      "chatId": "chat123",
      "senderId": "user123",
      "content": "Hello, how are you?",
      "type": "text",
      "timestamp": "2024-01-15T10:30:00Z",
      "status": "sent"
    }
  }

  ```

- **Status Codes:** 201 (Created), 400 (Validation Error), 401 (Unauthorized)

### GET /api/v1/messages/:chatId

- **URL:** `/api/v1/messages/:chatId?limit=50&before=messageId`

- **Method:** GET

- **Query Parameters:**
  - `limit`: number (default: 50, max: 100)
  - `before`: messageId (for pagination)

- **Response:**

  ```json
  {
    "success": true,
    "data": {
      "messages": [
        {
          "messageId": "msg_abc123",
          "senderId": "user123",
          "content": "Hello",
          "type": "text",
          "timestamp": "2024-01-15T10:30:00Z",
          "status": "delivered"
        }
      ],
      "hasMore": true,
      "nextCursor": "msg_xyz789"
    }
  }

  ```

- **Status Codes:** 200 (Success), 404 (Chat Not Found)

### GET /api/v1/chats

- **URL:** `/api/v1/chats`

- **Method:** GET

- **Response:**

  ```json
  {
    "success": true,
    "data": {
      "chats": [
        {
          "chatId": "chat123",
          "type": "one-on-one",
          "participants": ["user123", "user456"],
          "lastMessage": {
            "content": "Hello",
            "timestamp": "2024-01-15T10:30:00Z"
          },
          "unreadCount": 2
        }
      ]
    }
  }

  ```

- **Status Codes:** 200 (Success)

### POST /api/v1/chats

- **URL:** `/api/v1/chats`

- **Method:** POST

- **Request Body:**

  ```json
  {
    "participants": ["user123", "user456"],
    "type": "one-on-one"
  }

  ```

- **Response:**

  ```json
  {
    "success": true,
    "data": {
      "chatId": "chat123",
      "participants": ["user123", "user456"],
      "type": "one-on-one",
      "createdAt": "2024-01-15T10:30:00Z"
    }
  }

  ```

- **Status Codes:** 201 (Created), 400 (Validation Error)

### WebSocket Events

- **Connection:** `socket.on('connect')` - Client connects

- **Message Sent:** `socket.emit('message:sent', { messageId, chatId, content })`

- **Message Delivered:** `socket.on('message:delivered', { messageId })`

- **Message Read:** `socket.on('message:read', { messageId, readAt })`

- **Typing Indicator:** `socket.emit('typing', { chatId, userId })`

### iii) Implementation Details

**WebSocket Integration:**
- Socket.io client for real-time messaging
- Auto-reconnect on connection loss
- Heartbeat mechanism for connection health
- Event handlers for message received, typing indicators, online/offline status

**Message Sending Implementation:**
- Optimistic UI updates for instant feedback
- WebSocket emit for real-time delivery
- Error handling and retry logic
- Message status tracking (sent, delivered, read)

**Message Retrieval Implementation:**
- Pagination for message history
- Infinite scroll for loading older messages
- Caching recent messages in Redux
- Real-time message updates via WebSocket

---

## b) Backend

### i) Services

**Message Service:**

```typescript
export class MessageService {
  async sendMessage(chatId: string, senderId: string, content: string): Promise<Message> {
    // Validate message
    const message = {
      chatId,
      senderId,
      content,
      createdAt: new Date(),
      status: 'sent'
    };
    
    // Store in message queue (Kafka/RabbitMQ)
    await this.messageQueue.publish('messages', message);
    
    // Send acknowledgment to sender via WebSocket
    this.webSocketService.sendToUser(senderId, 'message-sent', message);
    
    return message;
  }

  async getMessages(chatId: string, limit: number, before?: string): Promise<Message[]> {
    // Check cache first
    const cached = await this.redis.get(`messages:${chatId}:${before || 'latest'}`);
    if (cached) return JSON.parse(cached);
    
    // Query database
    const messages = await Message.find({ chatId })
      .sort({ createdAt: -1 })
      .limit(limit);
    
    // Cache results
    await this.redis.setex(`messages:${chatId}:${before || 'latest'}`, 300, JSON.stringify(messages));
    
    return messages;
  }
}

```

**WebSocket Service:**

```typescript
export class WebSocketService {
  private activeConnections: Map<string, Socket> = new Map(); // userId -> WebSocket

  async handleConnection(socket: Socket, userId: string): Promise<void> {
    this.activeConnections.set(userId, socket);
    
    // Join user's chat rooms
    const chats = await this.chatService.getUserChats(userId);
    chats.forEach(chat => socket.join(`chat:${chat.id}`));
    
    socket.on('disconnect', () => {
      this.activeConnections.delete(userId);
    });
  }

  async sendMessage(userId: string, message: Message): Promise<void> {
    const socket = this.activeConnections.get(userId);
    if (socket) {
      socket.emit('new-message', message);
    } else {
      // User offline, store for later delivery
      await this.notificationService.sendPushNotification(userId, message);
    }
  }

  async broadcastToChat(chatId: string, message: Message, excludeUserId?: string): Promise<void> {
    const chat = await this.chatService.getChat(chatId);
    chat.participants.forEach(userId => {
      if (userId !== excludeUserId) {
        this.sendMessage(userId, message);
      }
    });
  }
}

```

### ii) Server Structure

**Express.js + Socket.io Server Structure:**

```

server/
├── routes/
│   ├── messages.js
│   └── chats.js
├── controllers/
│   ├── MessageController.js
│   └── ChatController.js
├── services/
│   ├── MessageService.js
│   └── ChatService.js
├── socket/
│   └── chatSocket.js
└── models/
    ├── Message.js
    └── Chat.js

```

### Message Service Implementation

```typescript
class MessageService {
  async sendMessage(chatId: string, senderId: string, content: string) {
    // Validate message
    // Store in message queue (Kafka/RabbitMQ)
    // Send acknowledgment to sender via WebSocket
    // Consumer processes and stores in database
    // If recipient online, push via WebSocket
  }
}

```

---

## Message Flow

### Sending Message

1. Client sends message via WebSocket

2. Server validates and stores in message queue

3. Server sends acknowledgment to sender

4. Message consumer processes and stores in database

5. If recipient online, push via WebSocket

6. If recipient offline, store for later delivery

### Receiving Message

1. Server receives message from queue

2. Check if recipient is online

3. If online, push via WebSocket

4. If offline, store in pending messages

5. Send push notification

---

## WebSocket Connection Management

```typescript
class ChatServer {
  private activeConnections: Map<string, Socket> = new Map(); // userId -> WebSocket

  async handleConnection(socket: Socket, userId: string): Promise<void> {
    this.activeConnections.set(userId, socket);

    socket.on('disconnect', () => {
      this.activeConnections.delete(userId);
    });
  }

  async sendMessage(userId: string, message: any): Promise<void> {
    const socket = this.activeConnections.get(userId);
    if (socket) {
      socket.emit('message', message);
    } else {
      // User offline, store for later
      await this.storePendingMessage(userId, message);
    }
  }
}

```

---

## Message Storage

### Cassandra Schema

```cql
CREATE TABLE messages (
    chat_id TEXT,
    message_id BIGINT,
    sender_id BIGINT,
    content TEXT,
    type TEXT,
    created_at TIMESTAMP,
    PRIMARY KEY (chat_id, created_at, message_id)
) WITH CLUSTERING ORDER BY (created_at DESC);

```

## Protocols

### REST API Protocol

- **Protocol:** REST (Representational State Transfer)

- **Data Format:** JSON

- **Authentication:** JWT Bearer token

### Additional Protocols

- **WebSocket** - For real-time features (if applicable)

- **Message Queue** - For async processing (if applicable)

---

---

## Implementation Details

### Core Implementation

**Note:** Implementation details are split between frontend (React.js) and backend (Node.js/Express.js). Each section indicates where the code runs.

### Real-Time Message Delivery

**Frontend Implementation:** React component handles WebSocket connection and displays messages in real-time
**Backend Implementation:** Socket.io server with Redis adapter handles message broadcasting

- **Strategy:** Room-based messaging using Socket.io - like joining a chat room, all users in the room receive messages

- **Update Frequency:** Messages delivered instantly via WebSocket, no polling needed

**Backend (Express.js):**

```typescript
// Backend: socket/chatSocket.ts
import { Server } from 'socket.io';
import redis from '../config/redis';

export const setupChatSocket = (io: Server) => {
  // Use Redis adapter for horizontal scaling
  io.adapter(createAdapter(redis));

  io.on('connection', (socket) => {
    // Join chat room
    socket.on('chat:join', async (chatId: string) => {
      socket.join(`chat:${chatId}`);

      // Send recent messages
      const messages = await Message.find({ chatId })
        .sort({ createdAt: -1 })
        .limit(50);
      socket.emit('messages:history', messages.reverse());
    });

    // Handle new message
    socket.on('message:send', async (data: { chatId: string; content: string; type: string }) => {
      // Store message in database
      const message = await Message.create({
        chatId: data.chatId,
        senderId: socket.data.userId,
        content: data.content,
        type: data.type,
        status: 'sent'
      });

      // Broadcast to all users in chat room
      io.to(`chat:${data.chatId}`).emit('message:new', message);

      // Send to message queue for offline users
      await messageQueue.publish('message:new', message);
    });

    // Handle message delivery confirmation
    socket.on('message:delivered', async (messageId: string) => {
      await Message.updateOne(
        { _id: messageId },
        { $set: { status: 'delivered', deliveredAt: new Date() } }
      );

      // Notify sender
      io.emit('message:delivered', { messageId });
    });

    socket.on('disconnect', () => {
      // Clean up on disconnect
    });
  });
};

```

**Frontend Implementation:**

```typescript
// React hook for real-time messaging
import { useEffect, useState } from 'react';
import { io, Socket } from 'socket.io-client';

const useChatSocket = (chatId: string) => {
  const [socket, setSocket] = useState<Socket | null>(null);
  const [messages, setMessages] = useState<Message[]>([]);
  const [isConnected, setIsConnected] = useState(false);

  useEffect(() => {
    const newSocket = io(process.env.REACT_APP_SOCKET_URL || '', {
      auth: { token: localStorage.getItem('token') }
    });

    newSocket.on('connect', () => {
      setIsConnected(true);
      newSocket.emit('chat:join', chatId);
    });

    newSocket.on('disconnect', () => {
      setIsConnected(false);
    });

    newSocket.on('messages:history', (history: Message[]) => {
      setMessages(history);
    });

    newSocket.on('message:new', (message: Message) => {
      setMessages(prev => [...prev, message]);
    });

    newSocket.on('message:delivered', ({ messageId }: { messageId: string }) => {
      setMessages(prev => prev.map(msg =>
        msg.id === messageId ? { ...msg, status: 'delivered' } : msg
      ));
    });

    setSocket(newSocket);

    return () => {
      newSocket.disconnect();
    };
  }, [chatId]);

  const sendMessage = (content: string, type: string = 'text') => {
    if (socket && isConnected) {
      socket.emit('message:send', { chatId, content, type });
    }
  };

  return { messages, sendMessage, isConnected };
};

```

### Message Persistence and Pagination

**Frontend Implementation:** React component handles infinite scroll for message history
**Backend Implementation:** Express.js API handles cursor-based pagination

- **Strategy:** Cursor-based pagination - like scrolling through chat history, loads older messages as you scroll up

- **Page Size:** 50 messages per page - good balance between load time and user experience

**Backend (Express.js):**

```typescript
// Backend: routes/messages.ts
router.get('/messages/:chatId', async (req, res) => {
  const { chatId } = req.params;
  const { before, limit = 50 } = req.query;

  let query: any = { chatId };

  // Cursor-based pagination
  if (before) {
    query.createdAt = { $lt: new Date(before) };
  }

  const messages = await Message.find(query)
    .sort({ createdAt: -1 })
    .limit(parseInt(limit as string))
    .lean();

  const hasMore = messages.length === parseInt(limit as string);
  const nextCursor = messages.length > 0 ? messages[messages.length - 1].createdAt : null;

  res.json({
    success: true,
    data: {
      messages: messages.reverse(),
      hasMore,
      nextCursor
    }
  });
});

```

**Frontend Implementation:**

```typescript
// React component with infinite scroll
import { useInfiniteQuery } from '@tanstack/react-query';
import { useRef, useCallback } from 'react';

const MessageList: React.FC<{ chatId: string }> = ({ chatId }) => {
  const observerRef = useRef<IntersectionObserver | null>(null);

  const {
    data,
    fetchNextPage,
    hasNextPage,
    isFetchingNextPage,
  } = useInfiniteQuery({
    queryKey: ['messages', chatId],
    queryFn: ({ pageParam }) =>
      axios.get(`/api/v1/messages/${chatId}`, {
        params: { before: pageParam, limit: 50 }
      }).then(res => res.data),
    getNextPageParam: (lastPage) =>
      lastPage.data.hasMore ? lastPage.data.nextCursor : undefined,
  });

  const lastMessageRef = useCallback((node: HTMLDivElement | null) => {
    if (isFetchingNextPage) return;
    if (observerRef.current) observerRef.current.disconnect();
    observerRef.current = new IntersectionObserver(entries => {
      if (entries[0].isIntersecting && hasNextPage) {
        fetchNextPage();
      }
    });
    if (node) observerRef.current.observe(node);
  }, [isFetchingNextPage, hasNextPage, fetchNextPage]);

  return (
    <div className="message-list">
      {data?.pages.map((page) =>
        page.data.messages.map((message: Message, index: number) => (
          <div
            key={message.id}
            ref={index === 0 ? lastMessageRef : null}
          >
            <MessageBubble message={message} />
          </div>
        ))
      )}
      {isFetchingNextPage && <LoadingSpinner />}
    </div>
  );
};

```

### Error Handling

**Frontend Implementation:** React components handle errors and show user-friendly messages
**Backend Implementation:** Express.js middleware handles errors and returns proper status codes

**Backend (Express.js):**

```typescript
// Backend: middleware/errorHandler.ts
export const errorHandler = (err: Error, req: Request, res: Response, next: NextFunction) => {
  console.error('Error:', err);

  if (err.name === 'ValidationError') {
    return res.status(400).json({ error: 'Invalid message data', details: err.message });
  }

  if (err.message === 'Chat not found') {
    return res.status(404).json({ error: 'Chat not found' });
  }

  if (err.name === 'RateLimitError') {
    return res.status(429).json({
      error: 'Too many messages. Please wait before sending another message.',
      retryAfter: err.retryAfter
    });
  }

  res.status(500).json({ error: 'Internal server error' });
};

```

**Frontend Implementation:**

```typescript
// React error handling with toast notifications
import { toast } from 'react-toastify';
import { ErrorBoundary } from 'react-error-boundary';

// Axios interceptor for API errors
axios.interceptors.response.use(
  (response) => response,
  (error) => {
    if (error.response?.status === 429) {
      toast.error('Too many messages. Please wait a moment.');
    } else if (error.response?.status === 404) {
      toast.error('Chat not found.');
    } else {
      toast.error('Failed to send message. Please try again.');
    }
    return Promise.reject(error);
  }
);

// WebSocket reconnection logic
const useReconnectingSocket = (url: string) => {
  const [socket, setSocket] = useState<Socket | null>(null);
  const [reconnectAttempts, setReconnectAttempts] = useState(0);

  useEffect(() => {
    const connect = () => {
      const newSocket = io(url, {
        reconnection: true,
        reconnectionDelay: 1000 * Math.min(reconnectAttempts, 5), // Exponential backoff
        reconnectionAttempts: 10
      });

      newSocket.on('connect', () => {
        setReconnectAttempts(0);
        toast.success('Connected');
      });

      newSocket.on('disconnect', () => {
        toast.warning('Disconnected. Reconnecting...');
        setReconnectAttempts(prev => prev + 1);
      });

      newSocket.on('connect_error', () => {
        toast.error('Connection failed. Retrying...');
      });

      setSocket(newSocket);
    };

    connect();

    return () => {
      socket?.disconnect();
    };
  }, [url, reconnectAttempts]);

  return socket;
};

```

**Error Scenarios:**

- **Connection Errors:** Handle WebSocket connection failures, implement reconnection logic with exponential backoff - auto-reconnect with increasing delays, show connection status to users

- **Message Delivery Failures:** Retry failed message deliveries, store in dead letter queue after max retries - queue messages for offline users, deliver when they reconnect

- **Rate Limiting:** Prevent message spam, implement per-user rate limits - show rate limit warnings, prevent excessive API calls

- **Invalid Messages:** Validate message format, reject malformed messages with clear error responses - client-side and server-side validation, show user-friendly error messages

---

## Testing Strategy

### Frontend Testing (React.js)

**Unit Testing:**

- **Jest + React Testing Library** - Test components, chat interface, message rendering

- **Chat Component Testing** - Test message list, input, real-time updates

- **Mocking:** Mock API calls, Socket.io, WebSocket connections

**Integration Testing:**

- **Message Sending Flow** - Test complete message sending process

- **Real-time Updates** - Test Socket.io message delivery

- **API Integration Tests** - Test API calls with mock server

**E2E Testing:**

- **Cypress / Playwright** - Test chat messaging flows

- **Test Scenarios:** Send message, receive message, group chat, message delivery status

### Backend Testing (Node.js/Express.js)

**Unit Testing:**

- **Jest + Supertest** - Test API endpoints, message processing

- **WebSocket Testing** - Test Socket.io message handling

- **Mocking:** Mock MongoDB, Redis, Socket.io

**Integration Testing:**

- **MongoDB Memory Server** - Test database operations

- **Redis Mock** - Test message caching

- **Socket.io Testing** - Test real-time message delivery

**Load Testing:**

- **Artillery / k6** - Test message handling under high load

- **Concurrent Connections:** Test WebSocket performance with high concurrency

---

## Deployment & DevOps

### Frontend Deployment

**Build Process:**

- **Production Build:** Optimized bundle with code splitting

- **CDN Deployment:** Deploy static assets to CDN

- **Environment Variables:** `.env.production` for production config

**Deployment Platforms:**

- **Vercel / Netlify** - Automatic deployments

- **AWS S3 + CloudFront** - Static site hosting with CDN

### Backend Deployment

**Server Setup:**

- **PM2:** Process manager with clustering

- **Nginx:** Load balancer and WebSocket proxy

- **Docker:** Containerized deployment

**Real-time Communication:**

- **Socket.io Scaling:** Redis adapter for horizontal scaling

- **Sticky Sessions:** Required for Socket.io

- **Load Balancer:** Configure for WebSocket support

**CI/CD Pipeline:**

- **Automated Testing:** Run tests before deployment

- **Zero-Downtime:** Rolling deployment strategy

- **Health Checks:** Verify messaging endpoints

---

## Environment Configuration

### Environment Variables

**Frontend:**

```env
REACT_APP_API_URL=https://api.example.com
REACT_APP_SOCKET_URL=wss://socket.example.com
REACT_APP_ENVIRONMENT=production

```

**Backend:**

```env
NODE_ENV=production
PORT=3000
MONGODB_URI=mongodb://...
REDIS_URL=redis://...
JWT_SECRET=xxx
SOCKET_IO_REDIS_URL=redis://...

```

---

## Database Migrations & Seeding

### MongoDB Migrations

**Migration Scripts:**

- **Schema Changes:** Add indexes for message queries

- **Data Migrations:** Update message formats

- **Index Optimization:** Add compound indexes for chat queries

### Data Seeding

**Seed Data:**

- **Chat Rooms:** Seed test chat rooms

- **Messages:** Seed test messages

- **User Accounts:** Seed test users

---

## API Documentation

### Swagger/OpenAPI

**API Documentation:**

- **Swagger UI:** Document REST APIs

- **Message API:** Document message endpoints

- **WebSocket Documentation:** Document Socket.io events

---

## API Versioning

**Versioning Strategy:**

- **URL Versioning:** `/api/v1/messages`, `/api/v2/messages`

- **Header Versioning:** `Accept: application/vnd.api+json;version=1`

- **Backward Compatibility:** Maintain old API versions for existing clients

- **WebSocket Versioning:** Version Socket.io events

---

## Monitoring & Logging

### Application Monitoring

**Frontend:**

- **Error Tracking:** Sentry for chat errors

- **Performance:** Track message delivery times

- **User Analytics:** Track messaging usage

**Backend:**

- **APM:** Monitor message processing performance

- **Socket.io Monitoring:** Track connection counts, message throughput

- **Message Metrics:** Track message delivery, latency

### Logging

**Structured Logging:**

- **Winston / Pino:** Log message operations

- **Message Events:** Log message sending, delivery, read receipts

- **Error Logging:** Detailed error logs with context

---

## Database Transactions & Consistency

### MongoDB Transactions

**Transaction Usage:**

- **Multi-Document Transactions** - For operations requiring ACID guarantees

- **Example:** Message creation + chat update + notification creation

- **Session Management:** Use MongoDB sessions for transaction control

**Example:**

```typescript
const session = await mongoose.startSession();
session.startTransaction();
try {
  await Message.create([messageData], { session });
  await Chat.updateOne({ chatId }, { $set: { lastMessageId: messageId } }, { session });
  await Notification.create([notificationData], { session });
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

- **Message Consistency:** Use transactions for message operations

- **Chat Consistency:** Ensure chat updates are atomic

- **Delivery Status Consistency:** Track message delivery status consistently

---

## Third-Party Service Integration

### Socket.io Integration

**Real-time Communication:**

- **Redis Adapter:** Enable horizontal scaling

- **Room Management:** Efficient room-based messaging for group chats

- **Connection Management:** Handle reconnections, heartbeats

### Redis Integration

**Caching & Message Queue:**

- **Message Caching:** Cache recent messages

- **Distributed Locks:** Prevent race conditions

- **Pub/Sub:** Cross-server message broadcasting

---

# 4) Algorithms

## Message Ordering Algorithm

**Purpose:** Ensure messages are delivered and displayed in correct chronological order.

**Algorithm:**
1. Assign sequence number to each message in chat
2. Store messages with sequence number and timestamp
3. Sort messages by sequence number when retrieving
4. Handle out-of-order delivery using sequence numbers

**Implementation:**

```typescript
class MessageOrdering {
  async sendMessage(chatId: string, message: Message): Promise<void> {
    // Get next sequence number for chat
    const sequence = await this.getNextSequence(chatId);
    
    // Store message with sequence
    await Message.create({
      ...message,
      chatId,
      sequence,
      timestamp: Date.now()
    });
    
    // Broadcast to chat room
    io.to(`chat:${chatId}`).emit('message', {
      ...message,
      sequence,
      timestamp: Date.now()
    });
  }
  
  async getMessages(chatId: string, limit: number = 50): Promise<Message[]> {
    return await Message.find({ chatId })
      .sort({ sequence: -1 })
      .limit(limit)
      .sort({ sequence: 1 }); // Return in ascending order
  }
}

```

**Complexity:**
- Time: O(n log n) for sorting where n is number of messages
- Space: O(n)
- **Message Ordering:** Sequence numbers ensure correct message order

---

## Offline Message Delivery Algorithm

**Purpose:** Deliver messages to users when they come online after being offline.

**Algorithm:**
1. Check if recipient is online when message is sent
2. If offline, store message in offline queue
3. When user comes online, check for pending messages
4. Deliver all pending messages in order
5. Mark messages as delivered

**Implementation:**

```typescript
class OfflineMessageDelivery {
  async sendMessage(message: Message): Promise<void> {
    const recipient = await this.getUserStatus(message.recipientId);
    
    if (recipient.isOnline) {
      // Deliver immediately via WebSocket
      await this.deliverMessage(message);
    } else {
      // Store in offline queue
      await OfflineQueue.create({
        messageId: message.id,
        recipientId: message.recipientId,
        message: message,
        createdAt: Date.now()
      });
      
      // Send push notification
      await this.sendPushNotification(message.recipientId, message);
    }
  }
  
  async onUserOnline(userId: string): Promise<void> {
    // Get all pending messages
    const pendingMessages = await OfflineQueue.find({ recipientId: userId })
      .sort({ createdAt: 1 });
    
    // Deliver all messages
    for (const queueItem of pendingMessages) {
      await this.deliverMessage(queueItem.message);
      await OfflineQueue.deleteOne({ _id: queueItem._id });
    }
  }
}

```

**Complexity:**
- Time: O(n) where n is number of pending messages
- Space: O(n) for offline queue
- **Delivery Guarantee:** Offline queue ensures message delivery

---

# 5) Data Models

## Messages Collection (MongoDB)

```javascript
{
  _id: ObjectId,
  messageId: String,        // Unique message ID, indexed
  chatId: ObjectId,         // Chat reference, indexed
  senderId: ObjectId,       // Sender reference, indexed
  recipientId: ObjectId,    // Recipient reference (for 1-on-1), indexed
  content: String,          // Message content
  type: String,            // text, image, video, file
  mediaUrl: String,        // Media URL (if applicable)
  sequence: Number,        // Sequence number for ordering, indexed
  status: String,          // sent, delivered, read
  readAt: Date,           // Read timestamp
  createdAt: Date,         // Created timestamp, indexed
  updatedAt: Date          // Updated timestamp
}

// Indexes:
// - { messageId: 1 } (unique)
// - { chatId: 1, sequence: 1 } (compound)
// - { senderId: 1, createdAt: -1 } (compound)
// - { recipientId: 1, status: 1 } (compound)

```

## Chats Collection (MongoDB)

```javascript
{
  _id: ObjectId,
  chatId: String,          // Unique chat ID, indexed
  type: String,           // one-on-one, group
  participants: [ObjectId], // Array of user IDs, indexed
  lastMessageId: ObjectId, // Last message reference
  lastMessageAt: Date,    // Last message timestamp, indexed
  createdAt: Date,        // Created timestamp
  updatedAt: Date         // Updated timestamp
}

// Indexes:
// - { chatId: 1 } (unique)
// - { participants: 1 } (for finding user chats)
// - { lastMessageAt: -1 } (for chat list sorting)

```

---

# 6) Database Transactions and Consistency

### MongoDB Transactions

**Transaction Usage:**
- **Multi-Document Transactions** - For operations requiring ACID guarantees
- **Example:** Message creation + chat update + notification creation in single transaction
- **Session Management:** Use MongoDB sessions for transaction control

**Example:**

```typescript
const session = await mongoose.startSession();
session.startTransaction();
try {
  await Message.create([messageData], { session });
  await Chat.updateOne({ chatId }, { $set: { lastMessageId: messageId } }, { session });
  await Notification.create([notificationData], { session });
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
- **Message Consistency:** Use transactions for message operations to ensure atomicity
- **Chat Consistency:** Ensure chat updates are atomic
- **Delivery Status Consistency:** Track message delivery status consistently
- **Eventual Consistency:** Accept eventual consistency for read receipts (may update with slight delay)

---

# 7) Protocols

### REST API Protocol

- **Protocol:** REST (Representational State Transfer)
- **Data Format:** JSON
- **HTTP Methods:** GET, POST, PUT, DELETE
- **Status Codes:** 200 (Success), 201 (Created), 400 (Bad Request), 401 (Unauthorized), 404 (Not Found), 429 (Rate Limited), 500 (Server Error)
- **Authentication:** JWT Bearer token in Authorization header

### WebSocket Protocol

- **Protocol:** Socket.io over WebSocket
- **Events:** `message`, `typing`, `read`, `online`, `offline`
- **Authentication:** JWT token in handshake
- **Use Case:** Real-time message delivery

---

# 8) API Design

### POST /api/v1/messages

- **URL:** `/api/v1/messages`
- **Method:** POST
- **Description:** Send a message
- **Request Body:**

  ```json
  {
    "chatId": "chat_abc123",
    "content": "Hello!",
    "type": "text"
  }

  ```
- **Response:**

  ```json
  {
    "success": true,
    "data": {
      "messageId": "msg_abc123",
      "chatId": "chat_abc123",
      "content": "Hello!",
      "status": "sent",
      "createdAt": "2024-01-15T10:30:00Z"
    }
  }

  ```
- **Status Codes:** 201 (Created), 400 (Validation Error), 429 (Rate Limited)

### GET /api/v1/chats/:chatId/messages

- **URL:** `/api/v1/chats/:chatId/messages?limit=50&cursor=msg_xyz789`
- **Method:** GET
- **Description:** Get messages for a chat
- **Query Parameters:**
  - `limit`: number (default: 50, max: 100)
  - `cursor`: string (optional) - Cursor for pagination
- **Response:**

  ```json
  {
    "success": true,
    "data": {
      "messages": [...],
      "hasMore": true,
      "nextCursor": "msg_abc123"
    }
  }

  ```
- **Status Codes:** 200 (Success), 404 (Chat Not Found)

---

# 9) Caching Strategy

### Redis Cache

**Cache Strategy:**
- **Key Format:** `chat:{chatId}:messages`, `user:{userId}:online`, `chat:{chatId}:typing`
- **Value:** Serialized JSON (recent messages, online status, typing indicators)
- **TTL:** 
  - Recent messages: 3600 seconds (1 hour)
  - Online status: 60 seconds (frequently updated)
  - Typing indicators: 10 seconds (short-lived)
- **Eviction Policy:** LRU (Least Recently Used)

**Cache Patterns:**
- **Cache-Aside Pattern:** Check cache first, if miss query database and update cache
- **Write-Through Pattern:** Update cache when messages are sent
- **Cache Invalidation:** Invalidate message cache on new messages

---

# 10) Error Handling

### Error Scenarios and Responses

**Edge Cases Handling:**
- **Chat Not Found:** Return 404 Not Found when chat doesn't exist
- **Rate Limit Exceeded:** Return 429 Too Many Requests with Retry-After header
- **Connection Failure:** Handle WebSocket connection failures with automatic reconnection
- **Message Delivery Failure:** Retry failed message deliveries with exponential backoff
- **Invalid Message Format:** Return 400 Bad Request with validation errors

**Error Response Format:**

```json
{
  "error": {
    "code": "RATE_LIMIT_EXCEEDED",
    "message": "Too many messages",
    "details": "Please wait before sending another message",
    "retryAfter": 60
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

**WebSocket Scaling:**
- **Socket.io Redis Adapter:** Enable horizontal scaling of WebSocket connections
- **Sticky Sessions:** Required for Socket.io (use session affinity in load balancer)
- **Connection Management:** Monitor and manage WebSocket connections

**Database Scaling:**
- **Read Replicas:** Deploy read replicas for message queries
- **Sharding:** Shard messages by chatId for write scaling
- **Connection Pooling:** Use connection pooling to manage database connections

**Caching:**
- Distributed Redis cluster for high availability
- Cache recent messages and online status
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
- **Health Checks:** Verify messaging endpoints are healthy
- **Blue-Green Deployment:** Maintain two identical production environments

### Database Deployment

**MongoDB Setup:**
- **MongoDB Atlas** - Managed MongoDB service with automatic backups
- **Backup Strategy:** Daily automated backups with point-in-time recovery
- **Indexing:** Proper indexes on messageId, chatId, senderId, sequence
- **Replication:** Replica sets for high availability

**Redis Setup:**
- **Redis Cloud / AWS ElastiCache** - Managed Redis service
- **Cluster Mode:** Redis cluster for high availability and performance
- **Persistence:** RDB snapshots and AOF for data durability

---

# 12) Security Considerations

### Rate Limiting

- Implement rate limiting at API layer to prevent abuse
- Limit number of messages per user per minute/hour
- Use Redis for distributed rate limiting across multiple servers

### Input Validation

- Validate all API inputs (message content, chat IDs)
- Sanitize user input to prevent XSS attacks
- Validate file uploads (images, videos) for type and size

### HTTPS/TLS

- All communication between clients and API encrypted using HTTPS
- Prevents eavesdropping and man-in-the-middle attacks
- SSL/TLS certificates for secure connections

### End-to-End Encryption

- **Message Encryption:** Optional end-to-end encryption for message privacy
- **Key Management:** Secure key exchange and management
- **Encryption at Rest:** Encrypt messages stored in database

### Authentication and Authorization

- **JWT Tokens:** Use JWT for stateless authentication
- **Token Expiration:** Set appropriate token expiration times
- **Role-Based Access Control:** Implement RBAC for chat operations
- **Chat Access Control:** Verify user is participant before allowing message access

### Monitoring and Alerts

- Set up monitoring for unusual activity patterns
- Trigger alerts for potential security issues
- Track metrics: message rates, connection counts, error rates
- Log all operations for security auditing

---

# 3) Interview Answers

---

## Q1. 💡 Designing a chat/messaging system

**Situation:** Need to design a messaging system for 2B+ users that delivers messages in real-time with < 100ms latency and 99.9% delivery guarantee.

**Action:** **Backend (Node.js/Express.js):** I designed a real-time messaging system using Socket.io with Redis adapter for horizontal scaling. I implemented message queues (RabbitMQ) for reliable message delivery and decoupling. I used MongoDB for time-series message storage optimized for writes. I maintained active WebSocket connections in memory with connection management and automatic reconnection handling. I created an offline message queue that stores messages when recipients are offline and delivers them on reconnect. I integrated push notifications for offline users. I ensured message ordering using timestamps and sequence numbers. **Frontend (React.js):** I built a real-time chat interface with Socket.io client that automatically reconnects. I implemented message rendering with proper ordering, typing indicators, and read receipts. I created a chat list with unread counts and last message previews.

**Result:** System handles 2B+ users with message delivery latency < 100ms. 99.9% message delivery rate. Handles 100B+ messages per day.

**Takeaway:** WebSocket is essential for real-time messaging. Message queues provide reliability and decoupling. Cassandra is ideal for time-series message data.

---

## Q2. 💡 Ensuring message delivery when recipient is offline

**Situation:** Messages must be delivered even when recipient is not connected to the system.

**Action:** **Backend (Node.js/Express.js):** I implemented offline message handling by storing messages in MongoDB when the recipient is offline. I tracked user online/offline status in Redis for fast lookups. When a user reconnects, I check for pending messages and deliver them immediately via WebSocket. I integrated push notifications to alert offline users about new messages. I tracked message delivery status (sent, delivered, read) in the database. I implemented retry logic with exponential backoff for failed deliveries. **Frontend (React.js):** I displayed offline/online status indicators for users. I showed pending message counts and delivered messages when the connection is restored. I implemented a notification system to alert users of new messages when the app is in the background.

**Result:** 99.9% message delivery rate even for offline users. Users receive all messages when they reconnect.

**Takeaway:** Always store messages before attempting delivery. Push notifications help alert offline users.

---

## Q3. 💡 Handling group messaging with 256 members

**Situation:** Group messages need to be delivered to all members efficiently.

**Action:** **Backend (Node.js/Express.js):** I implemented group messaging using a fan-out pattern. When a message is sent to a group, I fan-out to all members asynchronously using a message queue. I processed group messages in batches to avoid overwhelming the system. I maintained WebSocket connections for all online members in room-based groups. For large groups, I optimized using multicast or broadcast strategies. **Frontend (React.js):** I built a group chat interface showing all participants, message threads, and group settings. I implemented group message rendering with sender names and avatars. I added group management features like adding/removing members and group info display.

**Result:** Group messages delivered to all 256 members in < 500ms. System handles thousands of concurrent group chats.

**Takeaway:** Fan-out pattern works well for group messaging. Async processing prevents blocking.

---

## Q4. 🔌 Implementing real-time message delivery using WebSocket

**Situation:** Users need to receive messages instantly without polling, requiring real-time bidirectional communication between client and server.

**Action:** **Backend (Node.js/Express.js):** I implemented Socket.io server with Redis adapter for horizontal scaling. I created room-based messaging where users join chat-specific rooms. When a message is sent, the server broadcasts it to all users in that room. I implemented connection management with heartbeat to detect dead connections and automatic cleanup. **Frontend (React.js):** I created a Socket.io client connection that automatically reconnects on disconnection. I used React hooks to manage WebSocket state and update UI when messages arrive. I implemented message queuing on the client to handle messages received while offline.

**Result:** Messages delivered in < 100ms latency. 99.9% connection success rate with automatic reconnection. System handles 10,000+ concurrent WebSocket connections.

**Takeaway:** Socket.io with Redis adapter enables horizontal scaling. Room-based messaging is efficient for group chats. Always implement reconnection logic and message queuing.

---

## Q5. 💡 Handling message persistence and retrieval

**Situation:** Messages need to be stored permanently and retrieved efficiently, even for chats with thousands of messages.

**Action:** **Backend (Node.js/Express.js):** I used MongoDB for message storage with proper indexing on chatId and timestamp. I implemented pagination using cursor-based approach for efficient retrieval. I stored messages in time-series format optimized for chronological queries. I implemented message archiving for old messages to keep database size manageable. **Frontend (React.js):** I implemented infinite scroll to load messages progressively. I cached recent messages in Redux state for fast access. I used React Query for automatic message fetching and caching.

**Result:** Message retrieval takes < 200ms even for chats with 10,000+ messages. Database queries optimized with proper indexing. User experience smooth with infinite scroll.

**Takeaway:** Cursor-based pagination is efficient for large message lists. Proper indexing is crucial for performance. Client-side caching improves perceived performance.
