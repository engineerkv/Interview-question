# Chat Messaging System

## Overview

Design a real-time chat messaging system where users can send instant messages, support one-on-one and group chats, with message delivery status, typing indicators, and media sharing.

---

## 1) Requirements

### Functional Requirements

**Core Features:**
- Real-time messaging (one-on-one and group chats)
- Message delivery status (sent, delivered, read)
- Typing indicators (show when users are typing)
- Online/offline status
- Media sharing (images, videos, files, voice messages)
- Message search
- Message reactions (emojis)
- Message editing and deletion
- Push notifications for offline users

**Advanced Features:**
- End-to-end encryption
- Message forwarding
- Chat archiving
- Voice and video calls
- Group chat management (add/remove members, roles)

### Non-Functional Requirements

**Performance:**
- Sub-100ms message delivery latency
- Real-time typing indicators
- Fast message history loading
- Efficient media handling

**Scalability:**
- Handle 2B+ users
- 100B+ messages per day
- Millions of concurrent connections
- High availability (99.9% uptime)

**Reliability:**
- 99.9% message delivery guarantee
- Message persistence and retrieval
- Offline message delivery
- Message ordering guarantee

---

## 2) Component Hierarchy

The frontend is a React application with real-time messaging. Here's the structure:

```
App
├── Layout
│   ├── Header
│   │   ├── Logo
│   │   └── UserMenu
│   └── MainContent
├── Pages
│   ├── ChatPage
│   │   ├── ChatSidebar
│   │   │   ├── ChatList
│   │   │   │   └── ChatItem
│   │   │   │       ├── Avatar
│   │   │   │       ├── ChatName
│   │   │   │       ├── LastMessage
│   │   │   │       ├── Timestamp
│   │   │   │       └── UnreadBadge
│   │   │   └── SearchBar (search chats)
│   │   └── ChatWindow
│   │       ├── ChatHeader
│   │       │   ├── ChatName
│   │       │   ├── OnlineStatus
│   │       │   └── ChatActions (Info, Mute)
│   │       ├── MessageList
│   │       │   └── MessageBubble
│   │       │       ├── MessageContent (text, media)
│   │       │       ├── MessageTime
│   │       │       ├── DeliveryStatus (sent, delivered, read)
│   │       │       ├── MessageReactions
│   │       │       └── MessageActions (Edit, Delete, Forward)
│   │       ├── TypingIndicator (shows who's typing)
│   │       └── MessageInput
│   │           ├── TextInput
│   │           ├── AttachmentButton
│   │           ├── EmojiPicker
│   │           └── SendButton
│   └── ChatInfoPage
│       ├── ChatDetails
│       ├── MediaGallery
│       └── GroupMembers (for group chats)
└── SharedComponents
    ├── Avatar
    ├── MessageBubble
    ├── TypingIndicator
    └── MediaViewer
```

### Key Components Explained

**1. ChatWindow Component**
- Main chat interface
- Manages WebSocket connection
- Handles message sending/receiving
- Real-time updates via WebSocket

**2. MessageList Component**
- Displays messages with virtual scrolling
- Infinite scroll for message history
- Groups messages by date
- Shows delivery status

**3. MessageBubble Component**
- Individual message display
- Shows sender, content, time, status
- Handles media (images, videos, files)
- Message reactions and actions

**4. MessageInput Component**
- Text input for messages
- Attachment support
- Emoji picker
- Typing indicator triggers
- Send button with validation

**5. ChatList Component**
- List of conversations
- Shows last message preview
- Unread count badges
- Search and filter functionality

---

## 3) Data Models

Here are the key data structures:

```typescript
// Conversation (chat)
interface Conversation {
  id: string;
  type: "direct" | "group";
  participants: Participant[];
  lastMessage?: Message;
  unreadCount: number;
  updatedAt: string;
  createdAt: string;
  name?: string;  // For group chats
  avatar?: string;  // For group chats
}

// Participant
interface Participant {
  id: string;
  name: string;
  avatar?: string;
  isOnline: boolean;
  lastSeen?: string;
  role?: "admin" | "member";  // For group chats
}

// Message
interface Message {
  id: string;
  conversationId: string;
  senderId: string;
  sender: Participant;
  content: string;
  type: "text" | "image" | "file" | "audio" | "video";
  timestamp: string;
  status: "sending" | "sent" | "delivered" | "read";
  readBy: string[];  // User IDs who read the message
  reactions: Reaction[];
  replyTo?: {
    id: string;
    content: string;
    senderId: string;
  };
  attachments?: Attachment[];
  editedAt?: string;
  deletedAt?: string;
}

// Reaction
interface Reaction {
  emoji: string;
  users: string[];  // User IDs who reacted
}

// Attachment
interface Attachment {
  id: string;
  type: "image" | "file" | "audio" | "video";
  url: string;
  name?: string;
  size?: number;
  mimeType?: string;
  thumbnailUrl?: string;  // For videos
}
```

### Data Flow Explanation

**When a user sends a message:**
1. User types message in MessageInput
2. Optimistic update: message appears immediately with "sending" status
3. WebSocket sends message to server
4. Server broadcasts to other participants
5. Status updates to "sent", then "delivered", then "read"
6. Other users receive message via WebSocket

**Message delivery status:**
1. "sending" - Message being sent (optimistic)
2. "sent" - Message sent to server
3. "delivered" - Message delivered to recipient's device
4. "read" - Recipient has read the message (read receipts)

**Typing indicator:**
1. User starts typing in MessageInput
2. WebSocket emits "typing" event
3. Other users see typing indicator
4. Indicator hides after 3 seconds of inactivity

**Real-time updates:**
1. WebSocket connection per user
2. Server broadcasts new messages, typing, presence
3. Frontend receives and updates UI
4. Optimistic updates for instant feedback
5. Sync with server state

---

## 4) API Design

### REST Endpoints

**GET /api/v1/conversations**
- Get user's conversations
- Query params: `page`, `limit`
- Returns: Paginated list of Conversation objects

**POST /api/v1/conversations**
- Create a conversation
- Request body: `{ type: "direct" | "group", participantIds: string[] }`
- Returns: Conversation object

**GET /api/v1/conversations/:id/messages**
- Get messages in conversation
- Query params: `cursor`, `limit`
- Returns: Paginated list of Message objects

**POST /api/v1/conversations/:id/messages**
- Send a message
- Request body: `{ content: string, type: string, attachments?: Attachment[] }`
- Returns: Message object

**PATCH /api/v1/messages/:id**
- Edit a message
- Request body: `{ content: string }`
- Returns: Updated Message object

**DELETE /api/v1/messages/:id**
- Delete a message
- Returns: Success confirmation

**POST /api/v1/messages/:id/reactions**
- Add or remove reaction
- Request body: `{ emoji: string }`
- Returns: Updated Message with reactions

**POST /api/v1/messages/:id/read**
- Mark message as read
- Returns: Success confirmation

### WebSocket Events

**Connection:** `wss://api.example.com/chat`

**Events:**
- `message` - New message received
- `message_sent` - Message sent confirmation
- `message_delivered` - Message delivered confirmation
- `message_read` - Message read confirmation
- `typing` - User is typing
- `typing_stop` - User stopped typing
- `presence` - User online/offline status
- `user_joined` - User joined conversation
- `user_left` - User left conversation

**Message Format:**
```json
{
  "type": "message",
  "data": {
    "id": "msg_123",
    "conversationId": "conv_456",
    "senderId": "user_789",
    "content": "Hello!",
    "timestamp": "2024-01-15T10:00:00Z",
    "status": "sent"
  }
}
```

### API Request/Response Examples

**Get Messages:**
```json
// GET /api/v1/conversations/conv_456/messages?cursor=abc123&limit=50
// Response
{
  "success": true,
  "data": {
    "messages": [
      {
        "id": "msg_123",
        "senderId": "user_789",
        "sender": {
          "id": "user_789",
          "name": "John Doe",
          "avatar": "https://cdn.example.com/avatar.jpg"
        },
        "content": "Hello!",
        "type": "text",
        "timestamp": "2024-01-15T10:00:00Z",
        "status": "read",
        "reactions": []
      }
    ],
    "hasMore": true,
    "nextCursor": "xyz789"
  }
}
```

**Send Message:**
```json
// POST /api/v1/conversations/conv_456/messages
{
  "content": "Hello!",
  "type": "text"
}

// Response
{
  "success": true,
  "data": {
    "id": "msg_123",
    "content": "Hello!",
    "status": "sent",
    "timestamp": "2024-01-15T10:00:00Z"
  }
}
```

---

## Key Design Decisions

**1. WebSocket for Real-time Messaging**
- Instant message delivery (< 100ms)
- Real-time typing indicators
- Presence updates
- Better user experience

**2. Optimistic Updates**
- Show messages immediately (useOptimistic)
- Better perceived performance
- Rollback if send fails
- Instant user feedback

**3. Message Delivery Status**
- Track sent, delivered, read status
- Read receipts for confirmation
- Better user experience
- Privacy controls for read receipts

**4. Infinite Scroll for Message History**
- Load older messages as user scrolls up
- Cursor-based pagination
- Efficient for long conversations
- Smooth scrolling

**5. Message Persistence**
- Store all messages in database
- Enable message search
- Offline message delivery
- Message history retrieval

**6. Typing Indicators**
- Show when users are typing
- Debounce typing events (3 seconds)
- Better real-time feel
- WebSocket for instant updates

---

## Interview Talking Points

**When explaining this system, I'd focus on:**

1. **Requirements First**: Start with core functionality - real-time messaging, one-on-one and group chats, delivery status, typing indicators

2. **Component Structure**: Explain the React component hierarchy - chat window, message list, message input, chat list

3. **Data Models**: Walk through Conversation, Message, Participant - and how they support messaging features

4. **API Design**: Show the REST endpoints and WebSocket protocol - conversations, messages, real-time events

5. **Key Challenges**: 
   - Real-time message delivery with low latency
   - Message ordering and delivery guarantees
   - Handling millions of concurrent connections
   - Message persistence and search
   - Typing indicators and presence tracking

**Example explanation flow:**
> "So for a chat messaging system, the core requirement is enabling real-time messaging between users. The frontend is a React app with a chat window component that displays messages and handles sending/receiving. For real-time delivery, we use WebSocket to send messages instantly (< 100ms latency). The data model centers around Conversation objects (chats) containing Message objects, with Participant objects for users. Messages have delivery status tracking (sent, delivered, read) and support reactions, replies, and media attachments. When a user sends a message, we use optimistic updates to show it immediately, then sync with the server via WebSocket. Typing indicators are shown when users are typing, and presence status shows who's online. The main API endpoints handle conversations, messages, and reactions, while WebSocket handles real-time events. Key challenges include ensuring low-latency message delivery, maintaining message ordering, handling millions of concurrent WebSocket connections, and providing reliable message persistence and search."
