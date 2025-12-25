# Real-Time Collaboration System

## Overview

Design a real-time collaborative editing system where multiple users can edit documents simultaneously without conflicts. The system uses operational transformation for conflict resolution and provides presence indicators and version history.

---

## 1) Requirements

### Functional Requirements

**Core Features:**
- Multiple users editing documents simultaneously
- Real-time synchronization of changes
- Conflict resolution (operational transformation/CRDT)
- Presence indicators (who's viewing/editing)
- Cursor positions for active users
- Document versioning and history
- Comments and suggestions
- Document sharing and permissions

**Advanced Features:**
- Document templates
- Export/import (PDF, DOCX, Markdown)
- Offline editing with sync
- Advanced collaboration features (mentions, notifications)

### Non-Functional Requirements

**Performance:**
- Change propagation: < 100ms
- Handle 50+ concurrent editors per document
- Fast document loading and saving
- Smooth editing experience

**Reliability:**
- No data loss during conflicts
- High availability (99.9% uptime)
- Document consistency across all clients

**User Experience:**
- Responsive design (mobile and desktop)
- Accessible editing interface
- Visual feedback for changes
- Intuitive collaboration features

---

## 2) Component Hierarchy

The frontend is a React application with real-time collaborative editing. Here's the structure:

```
App
├── Layout
│   ├── Header
│   │   ├── DocumentTitle (editable)
│   │   ├── CollaborationIndicator (active users)
│   │   ├── ShareButton
│   │   └── UserMenu
│   └── MainContent
├── Pages
│   ├── DocumentEditorPage
│   │   ├── DocumentEditor
│   │   │   ├── RichTextEditor (Slate.js/Draft.js)
│   │   │   ├── SelectionOverlay
│   │   │   └── CursorIndicators (other users' cursors)
│   │   ├── PresencePanel
│   │   │   ├── ActiveUsersList
│   │   │   └── CursorPositions
│   │   ├── CommentsPanel
│   │   │   └── CommentThread
│   │   └── VersionHistory
│   │       ├── VersionList
│   │       └── VersionPreview
│   └── DocumentsPage
│       └── DocumentList
└── SharedComponents
    ├── Button
    ├── Input
    └── Toast
```

### Key Components Explained

**1. DocumentEditor Component**
- Rich text editor (Slate.js or Draft.js)
- Handles text editing with formatting
- Tracks operations (insert, delete, format)
- Applies remote operations via operational transformation

**2. PresencePanel Component**
- Shows active users in document
- Displays user avatars and names
- Tracks cursor positions for each user
- Updates in real-time via WebSocket

**3. CommentsPanel Component**
- Displays comments and suggestions
- Comment threads with replies
- Highlights commented text
- Real-time comment updates

**4. VersionHistory Component**
- Document version timeline
- Version preview before restoration
- Version metadata (author, date, changes)
- Restore functionality

---

## 3) Data Models

Here are the key data structures:

```typescript
// Document
interface Document {
  id: string;
  title: string;
  content: DocumentContent;
  version: number;
  createdAt: string;
  updatedAt: string;
  ownerId: string;
  collaborators: Collaborator[];
}

// Document content (block-based)
interface DocumentContent {
  type: "doc";
  content: Block[];
}

// Block (paragraph, heading, list, etc.)
interface Block {
  type: "paragraph" | "heading" | "list" | "table";
  id: string;
  content: InlineContent[];
  attributes?: BlockAttributes;
}

// Inline content
interface InlineContent {
  type: "text" | "link";
  text?: string;
  marks?: Mark[];  // Bold, italic, etc.
}

// Operation (for operational transformation)
interface Operation {
  type: "insert" | "delete" | "format";
  blockId: string;
  position: number;
  content?: string;
  length?: number;
  marks?: Mark[];
  version: number;
  userId: string;
  timestamp: string;
}

// Collaborator
interface Collaborator {
  userId: string;
  name: string;
  avatar?: string;
  cursorPosition?: CursorPosition;
  isActive: boolean;
}

// Cursor position
interface CursorPosition {
  blockId: string;
  offset: number;
  color: string;
}
```

### Data Flow Explanation

**When a user edits:**
1. User types in editor
2. Operation is created (insert/delete/format)
3. Operation applied locally immediately
4. Operation sent to server via WebSocket
5. Server broadcasts to other users
6. Other users apply operation using operational transformation
7. All clients see consistent document state

**Operational transformation:**
1. Two users edit simultaneously
2. Operations are transformed to maintain consistency
3. Example: User A inserts at position 5, User B inserts at position 3
4. Operations are transformed so both insertions are preserved
5. Result: Both changes appear correctly

---

## 4) API Design

### REST Endpoints

**GET /api/v1/documents/:id**
- Get document
- Returns: Document object

**PATCH /api/v1/documents/:id/content**
- Update document content
- Request body: `{ version: number, operations: Operation[] }`
- Returns: Updated document with new version

**GET /api/v1/documents/:id/versions**
- Get version history
- Returns: Array of DocumentVersion objects

**POST /api/v1/documents/:id/restore**
- Restore document to version
- Request body: `{ version: number }`
- Returns: Updated document

### WebSocket Events

**Connection:** `wss://api.example.com/documents/:id`

**Events:**
- `operation` - Document operation received
- `presence` - User joined/left or cursor moved
- `comment` - Comment added
- `conflict` - Conflict detected

**Message Format:**
```json
{
  "type": "operation",
  "data": {
    "operation": {
      "type": "insert",
      "blockId": "block_1",
      "position": 5,
      "content": "Hello"
    },
    "version": 5,
    "userId": "user_123"
  }
}
```

---

## Key Design Decisions

**1. Operational Transformation for Conflict Resolution**
- Transforms concurrent operations
- Maintains document consistency
- No data loss during conflicts
- All clients see same state

**2. Block-Based Document Structure**
- Documents structured as blocks
- Easier to handle formatting and collaboration
- Better for operational transformation

**3. Optimistic Updates**
- Apply changes locally immediately
- Better perceived performance
- Sync with server state

**4. WebSocket for Real-time**
- Instant operation propagation
- Low latency (< 100ms)
- Presence and cursor tracking

---

## Interview Talking Points

**When explaining this system, I'd focus on:**

1. **Requirements First**: Start with core functionality - real-time collaborative editing, conflict resolution, presence indicators

2. **Component Structure**: Explain the React component hierarchy - document editor, presence panel, comments, version history

3. **Data Models**: Walk through Document, Block, Operation - and block-based structure

4. **API Design**: Show the REST endpoints and WebSocket protocol - document operations, real-time events

5. **Key Challenges**: 
   - Operational transformation for conflict resolution
   - Real-time synchronization with low latency
   - Handling 50+ concurrent editors
   - Maintaining document consistency

**Example explanation flow:**
> "So for a real-time collaboration system, the core requirement is allowing multiple users to edit documents simultaneously without conflicts. The frontend is a React app with a rich text editor component that tracks operations (insert, delete, format) as users type. Documents are structured as blocks (paragraphs, headings) rather than plain text, which makes collaboration easier. For conflict resolution, we use operational transformation - when two users edit simultaneously, operations are transformed so both changes are preserved correctly. Real-time updates are delivered via WebSocket for instant propagation (< 100ms). The data model includes Document objects with block-based content, Operation objects for changes, and Collaborator objects for presence tracking. The main API endpoints handle document operations and version history, while WebSocket handles real-time operation broadcasting. Key challenges include implementing operational transformation correctly, ensuring low-latency real-time updates, and maintaining document consistency across all clients."
