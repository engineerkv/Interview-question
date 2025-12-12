# Real-Time Collaboration System

> **Project Type:** Full-Stack Web Application (MERN Stack)
> **Scale:** Handle 1B+ users, real-time collaborative editing, conflict resolution
> **Tech Stack:** React.js, Node.js, Express.js, MongoDB, Redis, Socket.io, OT/CRDT

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

## a) Requirements

### i) Functional Requirements

- Multiple users can edit document simultaneously

- Real-time synchronization of changes

- Conflict resolution (operational transformation/CRDT)

- Version history

- Comments and suggestions

### ii) Non-Functional Requirements

- Change propagation < 100ms

- Handle 50+ concurrent editors

- No data loss during conflicts

---

## b) Scope and Priority

### Phase 1: MVP (Must Have) - Priority 1

- Core functionality

- Basic features

### Phase 2: Enhanced Features - Priority 2

- Additional capabilities

- Performance improvements

### Phase 2: Enhanced Features - Priority 2

- Comments and suggestions

- Document versioning and history

- Advanced conflict resolution strategies

- Document sharing and permissions

---

## c) Technology Choices

### Backend Framework

- **Node.js with Express.js** - Fast, scalable backend for real-time collaboration

### Real-time Communication

- **WebSocket (Socket.io)** - Real-time bidirectional communication for live editing

- **Operational Transformation (OT) or CRDT** - Conflict resolution for concurrent edits

### Database

- **MongoDB** - Document storage for documents and operations

- **Redis** - In-memory storage for active sessions and operation queue

### Additional Services

- **Message Queue** - For processing operations asynchronously

---

## d) Capacity Estimation

### Throughput Requirements

- **Total Users**: 1 billion users
- **Daily Active Users (DAU)**: 500 million users per day
- **Peak Traffic**: 3x average during peak hours (1.5 billion users per day)
- **Documents per Day**: 10 million documents created/edited
- **Operations per Document**: 1,000 operations per document per day (edits, cursor movements)
- **Read:Write Ratio**: 100:1 (viewing documents vs editing documents)

**Calculations:**

- **Average Writes Per Second (WPS)**: 10M documents × 1,000 ops / 86,400 seconds ≈ 115,740 WPS
- **Peak WPS**: 115,740 × 3 = 347,220 WPS
- **Average Reads Per Second (RPS)**: 115,740 × 100 = 11,574,000 RPS
- **Peak RPS**: 11,574,000 × 3 = 34,722,000 RPS
- **Concurrent Editors**: 50 million concurrent editors across all documents

### Storage Estimation

**Storage per Document:**

- Document content: 50 KB average (text, formatting)
- Operations log: 1 MB (1,000 operations × 1 KB per operation)
- Metadata: 1 KB (id, userId, timestamps, version)
- **Total per Document**: ~1.05 MB

**Storage Requirements:**

- **Documents per Year**: 10M documents/day × 365 = 3.65 billion documents
- **Document Storage**: 3.65B × 1.05 MB ≈ 3.83 PB per year
- **User Data**: 1B users × 5 KB ≈ 5 TB
- **Operations Log**: 3.65B documents × 1 MB ≈ 3.65 PB/year
- **Total Storage**: ~3.83 PB (documents) + 5 TB (users) + 3.65 PB (operations) ≈ 7.48 PB/year

### Bandwidth Estimation

- **Average Operation Size**: 1 KB per operation
- **Daily Bandwidth**: 10M documents × 1,000 ops × 1 KB = 10 TB/day
- **Peak Bandwidth**: 10 TB × 3 = 30 TB/day during peak hours
- **Average Bandwidth**: 10 TB / 86,400 seconds ≈ 115 MB/s
- **Peak Bandwidth**: 115 MB/s × 3 ≈ 345 MB/s

### Caching Estimation

Following the **80-20 rule** where 20% of documents generate 80% of traffic:

- **Cache 20% of active documents**: 10M × 0.2 = 2M documents
- **Cache memory required**: 2M × 1.05 MB = 2.1 TB (distributed across Redis cluster)
- **Cache hit ratio**: 90% (only 10% of document requests hit database)
- **Requests hitting Database**: 11,574,000 × 0.10 ≈ 1,157,400 RPS (manageable with sharding)

### Infrastructure Sizing

- **WebSocket Servers**: 5,000-10,000 instances behind load balancer, each handling 5,000-10,000 concurrent connections
- **API Servers**: 2,000-5,000 instances for REST API, each handling 2,000-5,000 RPS
- **Message Queue**: RabbitMQ/Kafka cluster with 50-100 nodes for operation distribution
- **Database**: MongoDB cluster with 200-300 nodes for storage and high read/write throughput
- **Cache Layer**: Redis cluster with 100-200 nodes for high availability and performance
- **OT/CRDT Service**: 100-200 instances for conflict resolution processing

---

## e) Architecture Overview

The system follows a real-time collaborative editing architecture with Operational Transformation (OT) or CRDT for conflict resolution, WebSocket for real-time communication, and distributed document storage. Here's how the complete system works:

### Frontend Architecture

**Frontend Layers:**

1. **Presentation Layer (React Components)**
   - **UI Components**: Reusable components (Editor, CursorIndicator, PresenceList, CommentPanel)
   - **Feature Components**: DocumentEditor, CollaborationPanel, VersionHistory, CommentThread
   - **Layout Components**: Header, Sidebar, Toolbar, MainLayout
   - **Page Components**: DocumentPage, DashboardPage, SettingsPage

2. **State Management Layer**
   - **Local State (useState)**: Component-specific UI state (editor content, cursor position, loading, errors)
   - **Server State (Redux Toolkit)**: Global state for documents, users, presence, operations
   - **WebSocket State**: Real-time operation updates, presence updates, cursor positions

3. **Editor Layer**
   - **Rich Text Editor**: Quill/Slate/Draft.js for document editing
   - **Operation Tracking**: Track local operations and apply remote operations
   - **Conflict Resolution**: Apply OT/CRDT transformations for conflict resolution

4. **API Integration Layer**
   - **API Client**: Axios instance with interceptors for auth, error handling
   - **Redux Thunks**: Async actions for API operations (createDocument, fetchDocument, saveDocument)
   - **Request/Response Transformation**: Data normalization and error handling

5. **WebSocket Layer**
   - **Socket.io Client**: WebSocket connection for real-time collaboration
   - **Event Handlers**: Operation received, presence update, cursor movement
   - **Connection Management**: Auto-reconnect, heartbeat, connection state

6. **Routing Layer (React Router)**
   - **Route Configuration**: Define routes and protected routes
   - **Navigation**: Programmatic and declarative navigation
   - **Route Guards**: Authentication and authorization checks

7. **Build & Deployment Layer**
   - **Build Process**: Webpack/Vite bundling with code splitting
   - **Static Assets**: Served from CDN (CloudFront/Cloudflare)
   - **Environment Configuration**: Environment-specific API endpoints and WebSocket URLs

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
- **Database (MongoDB)**: Sharded across multiple nodes for horizontal scaling, stores documents, operations, versions

---

# 3) Low Level Design (LLD)

## a) Frontend

### i) Component Architecture

---

## Component Architecture

### Document Service

```typescript
class DocumentService {
  async createDocument(userId: string, title: string): Promise<Document> {
    // Create new document
    // Initialize version
    // Return document ID
  }

  async applyOperation(documentId: string, operation: Operation): Promise<void> {
    // Transform operation against current state
    // Apply to document
    // Broadcast to other users
  }
}

```

### Operation Transformation Service

```typescript
class OTService {
  transform(op1: Operation, op2: Operation): Operation {
    // Transform operation op1 against op2
    // Return transformed operation
  }
}

```

---

## Service Components

```typescript
class Service {
  async processRequest(data: any) {
    // Implementation details
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
│   ├── DocumentTitle
│   ├── PresenceIndicator (Active users)
│   └── DocumentActions (Share, Export, History)
├── MainContent
│   ├── DocumentEditor
│   │   ├── Toolbar
│   │   │   ├── FormatButtons (Bold, Italic, etc.)
│   │   │   ├── HeadingSelector
│   │   │   └── InsertOptions
│   │   ├── EditorArea
│   │   │   ├── RichTextEditor (Draft.js/Slate)
│   │   │   ├── UserCursors (Other users' cursors)
│   │   │   └── UserSelections (Other users' selections)
│   │   └── StatusBar
│   │       ├── ConnectionStatus
│   │       └── VersionNumber
│   ├── Sidebar
│   │   ├── UserList
│   │   │   └── UserItem
│   │   │       ├── Avatar
│   │   │       ├── UserName
│   │   │       └── CursorIndicator
│   │   ├── CommentsPanel
│   │   │   ├── CommentList
│   │   │   └── AddCommentButton
│   │   └── VersionHistory
│   │       ├── VersionList
│   │       └── RestoreButton
│   └── ShareDialog
│       ├── ShareLinkInput
│       ├── PermissionSelector
│       └── InviteButton
└── SocketProvider (WebSocket connection)

```

### Key React Components

**Frontend Implementation:**

```typescript
// Collaborative Editor Component
const CollaborativeEditor: React.FC<{ documentId: string }> = ({ documentId }) => {
  const { content, applyLocalOperation, activeUsers } = useCollaborativeEditor(documentId);
  const editorRef = useRef<any>(null);

  const handleChange = (editorState: EditorState) => {
    // Detect changes and create operations
    const operations = detectOperations(editorState, content);

    operations.forEach(op => {
      // Apply optimistically
      applyLocalOperation(op);
    });
  };

  return (
    <div className="collaborative-editor">
      <Toolbar />
      <div className="editor-container">
        <RichTextEditor
          ref={editorRef}
          value={content}
          onChange={handleChange}
        />
        {/* Render other users' cursors */}
        {activeUsers.map(user => (
          <UserCursor
            key={user.id}
            userId={user.id}
            position={user.cursorPosition}
            color={user.color}
          />
        ))}
      </div>
      <StatusBar />
    </div>
  );
};

// Presence Indicator Component
const PresenceIndicator: React.FC<{ documentId: string }> = ({ documentId }) => {
  const { activeUsers } = usePresence(documentId);

  return (
    <div className="presence-indicator">
      {activeUsers.map(user => (
        <Avatar
          key={user.id}
          userId={user.id}
          name={user.name}
          color={user.color}
        />
      ))}
      <span className="user-count">{activeUsers.length} active</span>
    </div>
  );
};

```

### ii) State Management

**State Management Strategy:**

- **Local State (useState)**: Editor content, UI state (loading, errors, modals, cursor position)
- **Component State**: Each component manages its own UI state
- **API State**: React Query or SWR for server state (document content, version history) - caching, refetching
- **Global State (Context API/Redux)**: Document state, active users, operation queue, connection status

**Frontend Implementation:**

```typescript
// Using React Query for API state management
import { useQuery, useMutation, useQueryClient } from '@tanstack/react-query';

const useDocument = (documentId: string) => {
  return useQuery({
    queryKey: ['document', documentId],
    queryFn: async () => {
      const response = await axios.get(`/api/v1/documents/${documentId}`);
      return response.data;
    },
    staleTime: 5 * 60 * 1000 // Cache for 5 minutes
  });
};

const useCollaborativeEditor = (documentId: string) => {
  const [content, setContent] = useState('');
  const [pendingOps, setPendingOps] = useState<Operation[]>([]);
  const { socket } = useSocket();

  useEffect(() => {
    socket.emit('document:join', documentId);

    socket.on('operation:transformed', (operation: Operation) => {
      setContent(prev => applyOperation(prev, operation));
      setPendingOps(prev => prev.filter(op => op.id !== operation.id));
    });

    return () => {
      socket.emit('document:leave', documentId);
    };
  }, [documentId, socket]);

  const applyLocalOperation = (operation: Operation) => {
    setContent(prev => applyOperation(prev, operation));
    setPendingOps(prev => [...prev, operation]);
    socket.emit('operation', { documentId, operation });
  };

  return { content, applyLocalOperation, pendingOps };
};

```

### Component Interactions

**Data Flow:**

1. **Document Loading** → Editor fetches document via React Query, initializes editor state
2. **User Edits** → Editor detects changes, creates operations, applies optimistically
3. **Operation Broadcasting** → Operations sent via Socket.io, server transforms and broadcasts
4. **Operation Reception** → Editor receives transformed operations, applies to content
5. **Presence Updates** → Socket.io updates active users and cursor positions in real-time

**Event Handling:**

- Text changes trigger operation creation and sending
- Socket.io events update editor content and presence
- Cursor movements broadcast to other users
- Version history loads on demand
- Conflict resolution handles version mismatches

### UI/UX Considerations

- **Loading States**: Show skeleton loaders for document loading, spinners for operations
- **Error Handling**: Display user-friendly error messages, handle connection failures gracefully
- **Validation**: Client-side validation for document operations
- **Responsive Design**: Mobile-friendly layout, touch-optimized editor controls
- **Accessibility**: ARIA labels, keyboard navigation, screen reader support, keyboard shortcuts
- **Performance**: Debounce operation sending, batch operations, virtual rendering for large documents

---

## Data Models

### Document Model

```typescript
interface Document {
  documentId: string;
  title: string;
  content: string;
  version: number;
  ownerId: string;
  collaborators: string[];
  createdAt: Date;
  updatedAt: Date;
}

```

### Operation Model

```typescript
interface Operation {
  operationId: string;
  documentId: string;
  userId: string;
  type: 'insert' | 'delete' | 'retain';
  position: number;
  content?: string;
  version: number;
  timestamp: Date;
}

```

---

## Model Interface

```typescript
interface Model {
  id: string;
  // Model fields
  createdAt: Date;
  updatedAt: Date;
}

```

---

## Data APIs

### POST /api/v1/documents

- **URL:** `/api/v1/documents`

- **Method:** POST

- **Request Body:**

  ```json
  {
    "title": "My Document",
    "content": ""
  }

  ```

- **Response:**

  ```json
  {
    "success": true,
    "data": {
      "documentId": "doc_abc123",
      "title": "My Document",
      "version": 0,
      "createdAt": "2024-01-15T10:30:00Z"
    }
  }

  ```

- **Status Codes:** 201 (Created), 400 (Validation Error), 401 (Unauthorized)

### GET /api/v1/documents/:documentId

- **URL:** `/api/v1/documents/:documentId`

- **Method:** GET

- **Response:**

  ```json
  {
    "success": true,
    "data": {
      "documentId": "doc_abc123",
      "title": "My Document",
      "content": "Document content...",
      "version": 5,
      "updatedAt": "2024-01-15T11:00:00Z"
    }
  }

  ```

- **Status Codes:** 200 (Success), 404 (Not Found)

### PUT /api/v1/documents/:documentId

- **URL:** `/api/v1/documents/:documentId`

- **Method:** PUT

- **Request Body:**

  ```json
  {
    "title": "Updated Title"
  }

  ```

- **Response:**

  ```json
  {
    "success": true,
    "data": {
      "documentId": "doc_abc123",
      "title": "Updated Title",
      "version": 6
    }
  }

  ```

- **Status Codes:** 200 (Success), 404 (Not Found), 409 (Version Conflict)

### WebSocket Events

- **Connection:** `socket.on('connect')` - Client connects to document room

- **Operation Sent:** `socket.emit('operation', { documentId, operation, version })`

- **Operation Received:** `socket.on('operation', { operation, version })` - Receive transformed operation

- **Operation Acknowledged:** `socket.on('operation:ack', { operationId })` - Server acknowledges operation

- **User Joined:** `socket.on('user:joined', { userId, cursor })` - Another user joined

- **User Left:** `socket.on('user:left', { userId })` - User left the document

---

## Backend Implementation Details

### Express.js Server Structure

```

server/
├── routes/
├── controllers/
├── services/
└── models/

```

### Service Implementation

```typescript
class Service {
  async processRequest(data: any) {
    // Implementation details
  }
}

```

---

## Operational Transformation

### Basic Concept

- When two users edit simultaneously, transform operations to maintain consistency

- Example: User A inserts at position 5, User B inserts at position 3

- Transform User A's operation: position becomes 6

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

### Operational Transformation (OT)

**Frontend Implementation:** React component handles local operation queuing and applies transformed operations
**Backend Implementation:** Express.js service transforms operations to resolve conflicts

- **Strategy:** Operational Transformation algorithm - like Google Docs, transforms concurrent edits to maintain consistency

- **Transformation:** Operations are transformed against concurrent operations before applying

**Backend (Express.js):**

```typescript
// Backend: services/OTService.ts
import { transform } from 'ot-text';

interface Operation {
  type: 'insert' | 'delete' | 'retain';
  position: number;
  content?: string;
  length?: number;
}

class OTService {
  // Transform operation op1 against op2
  transform(op1: Operation, op2: Operation): Operation {
    // Use OT library (ot-text) for text operations
    return transform(op1, op2);
  }

  // Apply operation to document content
  apply(content: string, operation: Operation): string {
    let result = content;
    let pos = 0;

    if (operation.type === 'insert') {
      result = result.slice(0, operation.position) +
               operation.content +
               result.slice(operation.position);
    } else if (operation.type === 'delete') {
      result = result.slice(0, operation.position) +
               result.slice(operation.position + (operation.length || 0));
    }

    return result;
  }

  // Transform operation against multiple concurrent operations
  transformAgainstOps(operation: Operation, concurrentOps: Operation[]): Operation {
    let transformedOp = operation;

    for (const concurrentOp of concurrentOps) {
      transformedOp = this.transform(transformedOp, concurrentOp);
    }

    return transformedOp;
  }
}

```

**Frontend Implementation:**

```typescript
// React hook for operational transformation
import { useState, useCallback } from 'react';
import { io, Socket } from 'socket.io-client';

const useCollaborativeEditor = (documentId: string) => {
  const [content, setContent] = useState('');
  const [pendingOps, setPendingOps] = useState<Operation[]>([]);
  const [socket, setSocket] = useState<Socket | null>(null);

  useEffect(() => {
    const newSocket = io(process.env.REACT_APP_SOCKET_URL || '');

    newSocket.on('connect', () => {
      newSocket.emit('document:join', documentId);
    });

    // Receive transformed operation from server
    newSocket.on('operation:transformed', (operation: Operation) => {
      // Apply transformed operation to local content
      setContent(prev => applyOperation(prev, operation));

      // Remove from pending ops if it was pending
      setPendingOps(prev => prev.filter(op => op.id !== operation.id));
    });

    setSocket(newSocket);

    return () => {
      newSocket.disconnect();
    };
  }, [documentId]);

  const applyLocalOperation = useCallback((operation: Operation) => {
    // Apply optimistically to local content
    setContent(prev => applyOperation(prev, operation));

    // Add to pending operations
    setPendingOps(prev => [...prev, operation]);

    // Send to server
    socket?.emit('operation', {
      documentId,
      operation,
      version: getCurrentVersion()
    });
  }, [socket, documentId]);

  return { content, applyLocalOperation };
};

```

### Real-Time Operation Broadcasting

**Frontend Implementation:** React component sends operations via WebSocket
**Backend Implementation:** Socket.io server transforms and broadcasts operations

- **Strategy:** Room-based operation broadcasting - all users in document room receive transformed operations

- **Ordering:** Operations are versioned and transformed to maintain consistency

**Backend (Express.js):**

```typescript
// Backend: socket/collaborationSocket.ts
import { Server } from 'socket.io';
import { OTService } from '../services/OTService';

export const setupCollaborationSocket = (io: Server) => {
  const otService = new OTService();
  const operationQueues = new Map<string, Operation[]>(); // documentId -> operations

  io.on('connection', (socket) => {
    // Join document room
    socket.on('document:join', async (documentId: string) => {
      socket.join(`document:${documentId}`);

      // Send current document state
      const document = await Document.findById(documentId);
      socket.emit('document:state', {
        content: document.content,
        version: document.version
      });
    });

    // Handle incoming operation
    socket.on('operation', async (data: { documentId: string; operation: Operation; version: number }) => {
      const { documentId, operation, version } = data;

      // Get pending operations for this document
      const pendingOps = operationQueues.get(documentId) || [];

      // Transform operation against pending operations
      const transformedOp = otService.transformAgainstOps(operation, pendingOps);

      // Apply to document
      const document = await Document.findById(documentId);
      document.content = otService.apply(document.content, transformedOp);
      document.version += 1;
      await document.save();

      // Add to pending queue
      pendingOps.push(transformedOp);
      operationQueues.set(documentId, pendingOps);

      // Broadcast transformed operation to all clients in room
      io.to(`document:${documentId}`).emit('operation:transformed', {
        ...transformedOp,
        version: document.version
      });

      // Clean up old operations from queue
      if (pendingOps.length > 100) {
        pendingOps.shift();
      }
    });
  });
};

```

**Frontend Implementation:**

```typescript
// React component for collaborative editor
import { useEffect, useRef } from 'react';
import { useCollaborativeEditor } from '../hooks/useCollaborativeEditor';

const CollaborativeEditor: React.FC<{ documentId: string }> = ({ documentId }) => {
  const { content, applyLocalOperation } = useCollaborativeEditor(documentId);
  const editorRef = useRef<HTMLTextAreaElement>(null);

  const handleChange = (e: React.ChangeEvent<HTMLTextAreaElement>) => {
    const newContent = e.target.value;
    const oldContent = content;

    // Calculate operation (simplified - in real implementation, use diff algorithm)
    const operation = calculateOperation(oldContent, newContent);

    // Apply operation
    applyLocalOperation(operation);
  };

  return (
    <textarea
      ref={editorRef}
      value={content}
      onChange={handleChange}
      placeholder="Start typing..."
    />
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
    return res.status(400).json({ error: 'Invalid operation', details: err.message });
  }

  if (err.message === 'Version conflict') {
    return res.status(409).json({
      error: 'Document version conflict. Please refresh and try again.',
      currentVersion: err.currentVersion
    });
  }

  if (err.message === 'Document not found') {
    return res.status(404).json({ error: 'Document not found' });
  }

  res.status(500).json({ error: 'Internal server error' });
};

```

**Frontend Implementation:**

```typescript
// React error handling with reconnection
const useReconnectingSocket = (url: string) => {
  const [socket, setSocket] = useState<Socket | null>(null);
  const [reconnectAttempts, setReconnectAttempts] = useState(0);

  useEffect(() => {
    const connect = () => {
      const newSocket = io(url, {
        reconnection: true,
        reconnectionDelay: 1000 * Math.min(reconnectAttempts, 5),
        reconnectionAttempts: 10
      });

      newSocket.on('connect', () => {
        setReconnectAttempts(0);
      });

      newSocket.on('disconnect', () => {
        setReconnectAttempts(prev => prev + 1);
      });

      newSocket.on('error', (error) => {
        console.error('Socket error:', error);
        // Handle version conflicts
        if (error.type === 'version_conflict') {
          // Refresh document state
          refreshDocument();
        }
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

- **Connection Errors:** Handle WebSocket connection failures, implement reconnection logic with exponential backoff - auto-reconnect with increasing delays, sync document state on reconnect

- **Operation Conflicts:** Handle concurrent operation conflicts using Operational Transformation - transform operations before applying, maintain operation queues

- **Version Mismatches:** Detect and resolve version conflicts when clients are out of sync - refresh document state, retry operations with correct version

- **Invalid Operations:** Validate operations before applying, reject malformed operations with clear error responses - client-side and server-side validation, show user-friendly error messages

---

## Testing Strategy

### Frontend Testing (React.js)

**Unit Testing:**

- **Jest + React Testing Library** - Test components, editor, collaboration features

- **Editor Component Testing** - Test text editing, cursor position, conflict resolution

- **Mocking:** Mock API calls, Socket.io, OT/CRDT operations

**Integration Testing:**

- **Collaboration Flow** - Test real-time collaborative editing

- **Conflict Resolution** - Test OT/CRDT conflict resolution

- **Real-time Updates** - Test Socket.io integration

**E2E Testing:**

- **Cypress / Playwright** - Test collaborative editing flows

- **Test Scenarios:** Create document, multiple users edit, conflict resolution, version history

### Backend Testing (Node.js/Express.js)

**Unit Testing:**

- **Jest + Supertest** - Test API endpoints, OT/CRDT operations

- **Operation Transformation Testing** - Test OT algorithm correctness

- **Mocking:** Mock MongoDB, Redis, Socket.io

**Integration Testing:**

- **MongoDB Memory Server** - Test database operations

- **Redis Mock** - Test operation caching

- **Socket.io Testing** - Test real-time operation broadcasting

**Load Testing:**

- **Artillery / k6** - Test collaborative editing under high load

- **Concurrent Editors:** Test performance with multiple simultaneous editors

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

- **Health Checks:** Verify collaboration endpoints

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

- **Schema Changes:** Add indexes for document queries

- **Data Migrations:** Update document formats

- **Index Optimization:** Add compound indexes for document operations

### Data Seeding

**Seed Data:**

- **Test Documents:** Seed test documents

- **User Accounts:** Seed test users

- **Operations:** Seed sample operations

---

## API Documentation

### Swagger/OpenAPI

**API Documentation:**

- **Swagger UI:** Document REST APIs

- **Document API:** Document document endpoints

- **WebSocket Documentation:** Document Socket.io events for operations

---

## API Versioning

**Versioning Strategy:**

- **URL Versioning:** `/api/v1/documents`, `/api/v2/documents`

- **Header Versioning:** `Accept: application/vnd.api+json;version=1`

- **Backward Compatibility:** Maintain old API versions for existing clients

- **WebSocket Versioning:** Version Socket.io operation events

---

## Monitoring & Logging

### Application Monitoring

**Frontend:**

- **Error Tracking:** Sentry for collaboration errors

- **Performance:** Track operation latency

- **User Analytics:** Track collaboration patterns

**Backend:**

- **APM:** Monitor operation processing performance

- **Socket.io Monitoring:** Track connection counts, operation throughput

- **Collaboration Metrics:** Track concurrent editors, operation latency

### Logging

**Structured Logging:**

- **Winston / Pino:** Log collaboration operations

- **Operation Events:** Log operation creation, transformation, application

- **Error Logging:** Detailed error logs with context

---

## Database Transactions & Consistency

### MongoDB Transactions

**Transaction Usage:**

- **Multi-Document Transactions** - For operations requiring ACID guarantees

- **Example:** Document creation + operation log + version update

- **Session Management:** Use MongoDB sessions for transaction control

**Example:**

```typescript
const session = await mongoose.startSession();
session.startTransaction();
try {
  await Document.create([documentData], { session });
  await Operation.create([operationData], { session });
  await Version.create([versionData], { session });
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

- **Document Consistency:** Use transactions for document operations

- **Operation Consistency:** Ensure operations are applied in order

- **Version Consistency:** Maintain document version consistency

---

## Third-Party Service Integration

### Socket.io Integration

**Real-time Communication:**

- **Redis Adapter:** Enable horizontal scaling

- **Room Management:** Efficient room-based messaging for document collaboration

- **Connection Management:** Handle reconnections, operation synchronization

### Redis Integration

**Caching & Operation Queue:**

- **Operation Caching:** Cache recent operations

- **Distributed Locks:** Prevent race conditions in operation application

- **Pub/Sub:** Cross-server operation broadcasting

---

# 4) Algorithms

## Operational Transformation Algorithm

**Purpose:** Transform concurrent operations to resolve conflicts and maintain document consistency.

**Algorithm:**

1. Receive operation from client with version number
2. Get all pending operations for document
3. Transform operation against all pending operations
4. Apply transformed operation to document
5. Broadcast transformed operation to all clients
6. Increment document version

**Implementation:**

```typescript
class OTService {
  transform(op1: Operation, op2: Operation): Operation {
    // Transform op1 against op2
    if (op1.type === 'insert' && op2.type === 'insert') {
      if (op1.position <= op2.position) {
        return op1; // op1 comes before op2, no transformation needed
      } else {
        return { ...op1, position: op1.position + op2.content!.length };
      }
    }
    // ... more transformation rules
    return op1;
  }

  transformAgainstOps(operation: Operation, concurrentOps: Operation[]): Operation {
    let transformedOp = operation;
    for (const concurrentOp of concurrentOps) {
      transformedOp = this.transform(transformedOp, concurrentOp);
    }
    return transformedOp;
  }
}

```

**Complexity:**

- Time: O(n) where n is number of concurrent operations
- Space: O(1) per operation
- **Conflict Resolution:** OT ensures zero data loss during concurrent edits

---

## CRDT (Conflict-Free Replicated Data Type) Algorithm

**Purpose:** Alternative to OT, provides automatic conflict resolution without transformation.

**Algorithm:**

1. Each operation has unique ID and timestamp
2. Operations are commutative and idempotent
3. Apply operations in any order
4. Merge operations using CRDT merge function
5. All replicas converge to same state

**Implementation:**

```typescript
class CRDTService {
  applyOperation(document: CRDTDocument, operation: Operation): CRDTDocument {
    // CRDT operations are commutative
    const newDocument = { ...document };

    if (operation.type === 'insert') {
      // Insert with unique ID
      newDocument.operations.push({
        id: generateUniqueId(),
        type: 'insert',
        position: operation.position,
        content: operation.content,
        timestamp: Date.now()
      });
    }

    // Sort operations by timestamp for consistent ordering
    newDocument.operations.sort((a, b) => a.timestamp - b.timestamp);

    return newDocument;
  }
}

```

**Complexity:**

- Time: O(n log n) for sorting where n is number of operations
- Space: O(n) for operation history
- **Conflict Resolution:** CRDT provides automatic conflict resolution

---

# 5) Data Models

## Documents Collection (MongoDB)

```javascript
{
  _id: ObjectId,
  documentId: String,       // Unique document ID, indexed
  userId: ObjectId,         // Owner reference, indexed
  title: String,           // Document title
  content: String,         // Document content
  version: Number,         // Current version number, indexed
  collaborators: [ObjectId], // Array of collaborator user IDs
  permissions: Object,      // { read: [userId], write: [userId] }
  createdAt: Date,         // Created timestamp, indexed
  updatedAt: Date          // Updated timestamp
}

// Indexes:
// - { documentId: 1 } (unique)
// - { userId: 1, createdAt: -1 } (compound)
// - { collaborators: 1 } (for finding user documents)

```

## Operations Collection (MongoDB)

```javascript
{
  _id: ObjectId,
  operationId: String,      // Unique operation ID, indexed
  documentId: ObjectId,     // Document reference, indexed
  userId: ObjectId,         // User who created operation
  type: String,            // insert, delete, format
  position: Number,        // Character position
  content: String,         // Content (for insert)
  length: Number,          // Length (for delete)
  version: Number,         // Document version when operation created
  createdAt: Date,         // Created timestamp, indexed
}

// Indexes:
// - { operationId: 1 } (unique)
// - { documentId: 1, version: 1 } (compound)

```

---

# 6) Database Transactions and Consistency

### MongoDB Transactions

**Transaction Usage:**

- **Multi-Document Transactions** - For operations requiring ACID guarantees
- **Example:** Document creation + operation log + version update in single transaction
- **Session Management:** Use MongoDB sessions for transaction control

**Example:**

```typescript
const session = await mongoose.startSession();
session.startTransaction();
try {
  await Document.create([documentData], { session });
  await Operation.create([operationData], { session });
  await Version.create([versionData], { session });
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

- **Document Consistency:** Use transactions for document operations to ensure atomicity
- **Operation Consistency:** Ensure operations are applied in order using version numbers
- **Version Consistency:** Maintain document version consistency across all clients
- **Eventual Consistency:** Accept eventual consistency for operation broadcasting (operations may arrive slightly out of order)

---

# 7) Protocols

### REST API Protocol

- **Protocol:** REST (Representational State Transfer)
- **Data Format:** JSON
- **HTTP Methods:** GET, POST, PUT, DELETE
- **Status Codes:** 200 (Success), 201 (Created), 400 (Bad Request), 401 (Unauthorized), 404 (Not Found), 409 (Version Conflict), 500 (Server Error)
- **Authentication:** JWT Bearer token in Authorization header

### WebSocket Protocol

- **Protocol:** Socket.io over WebSocket
- **Events:** `operation`, `operation:transformed`, `cursor:update`, `presence:update`
- **Authentication:** JWT token in handshake
- **Use Case:** Real-time operation broadcasting and presence tracking

---

# 8) API Design

### GET /api/v1/documents/:documentId

- **URL:** `/api/v1/documents/:documentId`
- **Method:** GET
- **Description:** Get document with current version
- **Response:**

  ```json
  {
    "success": true,
    "data": {
      "documentId": "doc_abc123",
      "title": "My Document",
      "content": "Document content...",
      "version": 42,
      "collaborators": ["user_1", "user_2"]
    }
  }

  ```

- **Status Codes:** 200 (Success), 404 (Document Not Found)

### POST /api/v1/documents/:documentId/operations

- **URL:** `/api/v1/documents/:documentId/operations`
- **Method:** POST
- **Description:** Apply operation to document
- **Request Body:**

  ```json
  {
    "operation": {
      "type": "insert",
      "position": 10,
      "content": "Hello"
    },
    "version": 42
  }

  ```

- **Response:**

  ```json
  {
    "success": true,
    "data": {
      "operationId": "op_abc123",
      "transformedOperation": {...},
      "newVersion": 43
    }
  }

  ```

- **Status Codes:** 200 (Success), 409 (Version Conflict), 400 (Invalid Operation)

---

# 9) Caching Strategy

### Redis Cache

**Cache Strategy:**

- **Key Format:** `document:{documentId}`, `document:{documentId}:version`, `presence:{documentId}`
- **Value:** Serialized JSON (document content, version, active users)
- **TTL:**
  - Document content: 300 seconds (5 minutes)
  - Version: 60 seconds (frequently updated)
  - Presence: 30 seconds (short-lived)
- **Eviction Policy:** LRU (Least Recently Used)

**Cache Patterns:**

- **Cache-Aside Pattern:** Check cache first, if miss query database and update cache
- **Write-Through Pattern:** Update cache when document is updated
- **Cache Invalidation:** Invalidate document cache on operations

---

# 10) Error Handling

### Error Scenarios and Responses

**Edge Cases Handling:**

- **Version Conflict:** Return 409 Conflict when client version is outdated
- **Document Not Found:** Return 404 Not Found when document doesn't exist
- **Invalid Operation:** Return 400 Bad Request with validation errors
- **Connection Failure:** Handle WebSocket disconnections with automatic reconnection
- **Operation Transformation Failure:** Return 500 Server Error, log for investigation

**Error Response Format:**

```json
{
  "error": {
    "code": "VERSION_CONFLICT",
    "message": "Document version conflict",
    "details": "Your version (40) is outdated. Current version is 42.",
    "currentVersion": 42
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

- **Read Replicas:** Deploy read replicas for document queries
- **Sharding:** Shard documents by userId for write scaling
- **Connection Pooling:** Use connection pooling to manage database connections

**Caching:**

- Distributed Redis cluster for high availability
- Cache document content and versions
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
- **Health Checks:** Verify collaboration endpoints are healthy
- **Blue-Green Deployment:** Maintain two identical production environments

### Database Deployment

**MongoDB Setup:**

- **MongoDB Atlas** - Managed MongoDB service with automatic backups
- **Backup Strategy:** Daily automated backups with point-in-time recovery
- **Indexing:** Proper indexes on documentId, userId, version
- **Replication:** Replica sets for high availability

**Redis Setup:**

- **Redis Cloud / AWS ElastiCache** - Managed Redis service
- **Cluster Mode:** Redis cluster for high availability and performance
- **Persistence:** RDB snapshots and AOF for data durability

---

# 12) Security Considerations

### Rate Limiting

- Implement rate limiting at API layer to prevent abuse
- Limit number of operations per user per second
- Use Redis for distributed rate limiting across multiple servers

### Input Validation

- Validate all API inputs (operations, document data)
- Sanitize user input to prevent XSS attacks
- Validate operation format and content

### HTTPS/TLS

- All communication between clients and API encrypted using HTTPS
- Prevents eavesdropping and man-in-the-middle attacks
- SSL/TLS certificates for secure connections

### Authentication and Authorization

- **JWT Tokens:** Use JWT for stateless authentication
- **Token Expiration:** Set appropriate token expiration times
- **Role-Based Access Control:** Implement RBAC for document operations
- **Document Permissions:** Verify user has permission before allowing document access

### Access Control

- **Document Sharing:** Implement fine-grained document sharing permissions
- **Operation Authorization:** Verify user can edit document before accepting operations
- **Version Control:** Track who made what changes for audit trail

### Monitoring and Alerts

- Set up monitoring for unusual activity patterns
- Trigger alerts for potential security issues
- Track metrics: operation rates, concurrent editors, version conflicts
- Log all operations for security auditing

---

# 3) Interview Answers

---

## Q1. ⏰ ⏰ ⏰ Designing a real-time collaboration system

**Situation:** Need to design a collaborative document editor where multiple users can edit simultaneously with real-time synchronization and conflict resolution.

**Action:** **Backend (Node.js/Express.js):** I designed a real-time collaboration system using Operational Transformation (OT) to transform operations and resolve conflicts when users edit simultaneously. I implemented Socket.io with Redis adapter for real-time bidirectional communication and horizontal scaling. I created an operation queue that queues operations from clients and applies transformations server-side. I built version control to store document versions for history and rollback. I implemented OT algorithm to transform operations and maintain consistency. I broadcast transformed operations to all connected clients via WebSocket. I maintained authoritative document state on the server. **Frontend (React.js):** I built a collaborative editor using a rich text editor library (Draft.js/Slate) that tracks local changes. I implemented operation queuing on the client to send changes to the server. I created real-time synchronization that applies server-transformed operations to the local document state. I displayed active users with cursors and selections. I implemented conflict resolution UI that shows when conflicts occur.

**Result:** System handles 50+ concurrent editors with change propagation < 100ms. Zero data loss during conflicts. Smooth collaborative editing experience.

**Takeaway:** Operational Transformation is complex but essential for real-time collaboration. Server maintains authoritative state.

---

## Q2. 💡 Handling conflicts when two users edit the same position

**Situation:** Two users insert text at the same position simultaneously, causing conflict.

**Action:** **Backend (Node.js/Express.js):** I implemented conflict resolution using Operational Transformation. I transform operations based on other concurrent operations using OT algorithms. I adjust character positions when operations are transformed to maintain document consistency. The server applies transformations and maintains consistent state as the source of truth. I broadcast transformed operations to all clients. **Frontend (React.js):** Clients receive transformed operations and apply them to local state. I implemented operation queuing to handle operations that arrive out of order. I created visual indicators for conflicts and resolved them automatically. I ensured the UI reflects the server's authoritative state after transformation.

**Result:** Conflicts resolved automatically. Users see consistent document state. No manual conflict resolution needed. System handles 50+ concurrent editors with zero data loss.

**Takeaway:** Operational Transformation provides automatic conflict resolution. Server maintains authoritative state. Client-side operation queuing ensures smooth user experience.

---

## Q3. ✅ Implementing Operational Transformation for conflict resolution

**Situation:** Multiple users editing simultaneously need their operations transformed to maintain document consistency without conflicts.

**Action:** **Backend (Node.js/Express.js):** I implemented Operational Transformation using a library (ShareJS/ot.js) that transforms operations based on concurrent edits. When an operation arrives, I transform it against all pending operations in the queue. I maintain operation history and version numbers for each document. I apply transformations server-side and broadcast transformed operations to all clients. I handle insert, delete, and format operations with proper position adjustments. **Frontend (React.js):** I implemented operation queuing on the client to handle operations that arrive out of order. I apply transformed operations to the local document state. I maintain a local operation queue and sync with server state. I handle operation acknowledgments to ensure all operations are applied.

**Result:** System handles 50+ concurrent editors with zero conflicts. Operations are transformed correctly 100% of the time. Document state remains consistent across all clients.

**Takeaway:** Operational Transformation is complex but essential for real-time collaboration. Server-side transformation ensures consistency. Client-side queuing handles network delays.

---

## Q4. 💡 Implementing document versioning and history

**Situation:** Users need to view document history, revert changes, and handle version conflicts.

**Action:** **Backend (Node.js/Express.js):** I implemented document versioning by storing each operation with a version number. I created a version history table that stores document snapshots at regular intervals. I built a diff algorithm to show changes between versions. I implemented version conflict detection when clients try to update outdated versions. I created endpoints to retrieve document history and revert to previous versions. **Frontend (React.js):** I built a version history sidebar showing document versions with timestamps and authors. I implemented a diff viewer to show changes between versions. I created a revert functionality that restores previous versions. I displayed version conflict warnings when the document is outdated.

**Result:** Users can view complete document history. Version conflicts are detected and resolved. Revert functionality works reliably. History storage optimized with snapshots.

**Takeaway:** Versioning is crucial for collaboration. Regular snapshots reduce storage overhead. Diff algorithms enable efficient history viewing.

---

## Q5. ⏰ ⏰ ⏰ Implementing real-time presence and cursors

**Situation:** Users need to see who else is editing the document and where their cursors are positioned.

**Action:** **Backend (Node.js/Express.js):** I implemented presence tracking by storing active users in Redis with documentId as the key. I broadcast cursor positions via WebSocket to all users in the document room. I track user selections and highlight them in real-time. I implemented heartbeat to detect when users disconnect. I clean up presence data when users leave. **Frontend (React.js):** I displayed active users with avatars and names. I rendered cursors with user colors and names. I highlighted text selections from other users. I implemented smooth cursor animations. I showed typing indicators when users are actively editing.

**Result:** Users can see all active collaborators in real-time. Cursor positions update with < 50ms latency. Presence indicators improve collaboration awareness. System handles 50+ concurrent users smoothly.

**Takeaway:** Real-time presence enhances collaboration. Cursor tracking requires efficient WebSocket broadcasting. User colors help distinguish collaborators.
