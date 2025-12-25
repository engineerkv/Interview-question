# Collaborative Word Processor System

## Overview

Design a collaborative word processor where multiple users can edit documents in real-time, similar to Google Docs or Microsoft Word Online. The system needs to handle rich text editing, formatting, comments, and real-time synchronization.

---

## 1) Requirements

### Functional Requirements

**Core Features:**
- Create, edit, and delete documents
- Real-time collaborative editing with multiple users (50+ concurrent editors)
- Rich text formatting (bold, italic, headings, lists, tables, links, images)
- Comments and suggestions system
- Version history and document restoration
- Document sharing and permissions (viewer, editor, commenter, owner)
- Export/import (PDF, DOCX, Markdown, HTML)
- Document templates
- Search and find/replace
- Undo/redo functionality
- Document organization (folders, tags)

**Collaboration Features:**
- Real-time text changes visible to all users
- Presence indicators (who's viewing/editing)
- Cursor positions for active users
- Operational transformation for conflict resolution
- Comments with replies and resolution

### Non-Functional Requirements

**Performance:**
- Character updates: < 100ms latency
- Document rendering: < 200ms
- Support documents with 100K+ words
- Fast scrolling and rendering for long documents

**Scalability:**
- Handle millions of documents
- Support 50+ concurrent editors per document
- Billions of characters in storage

**Reliability:**
- High availability (99.9% uptime)
- Auto-save functionality
- Version history with restoration

**User Experience:**
- Responsive design (mobile and desktop)
- Keyboard shortcuts
- Accessible interface (keyboard navigation, screen readers)

---

## 2) Component Hierarchy

The frontend is built as a React application with a rich text editor. Here's how I'd structure it:

```
App
├── Layout
│   ├── Header
│   │   ├── DocumentTitle (editable)
│   │   ├── CollaborationIndicator (shows active users)
│   │   ├── ShareButton
│   │   └── UserMenu
│   ├── Toolbar
│   │   ├── FormatButtons (Bold, Italic, Underline)
│   │   ├── HeadingButtons (H1, H2, H3)
│   │   ├── ListButtons (Bulleted, Numbered)
│   │   ├── InsertButtons (Image, Link, Table)
│   │   └── ActionButtons (Undo, Redo, Comment)
│   ├── MainContent
│   │   ├── RichTextEditor
│   │   │   ├── EditorContent (the actual editable area)
│   │   │   ├── SelectionOverlay (highlights selected text)
│   │   │   └── CursorIndicators (other users' cursors with colors)
│   │   └── Sidebar
│   │       ├── CommentPanel
│   │       │   ├── CommentThread (comment with replies)
│   │       │   └── CommentHighlight (highlighted text in document)
│   │       ├── VersionHistory
│   │       │   ├── VersionList (timeline of versions)
│   │       │   └── VersionPreview (preview before restore)
│   │       └── DocumentOutline (table of contents)
│   └── Footer
│       ├── WordCount
│       └── LastSaved (auto-save indicator)
└── Modals
    ├── ShareDialog (document sharing and permissions)
    ├── ExportDialog (export format selection)
    └── SuggestionPanel (review mode for suggestions)
```

### Key Components Explained

**1. RichTextEditor Component**
- Uses a rich text editor library (Slate.js or Draft.js)
- Handles text editing with formatting
- Manages text selection and cursor tracking
- Renders document content as blocks (paragraphs, headings, lists, etc.)

**2. FormatToolbar Component**
- Displays formatting options based on selection
- Shows active formatting state (bold is active if selected text is bold)
- Applies formatting to selected text
- Updates in real-time as selection changes

**3. CommentPanel Component**
- Displays comments and suggestions
- Shows comment threads with replies
- Highlights commented text in the document
- Handles comment creation, replies, and resolution

**4. VersionHistory Component**
- Displays document version timeline
- Shows version metadata (author, date, change summary)
- Allows version preview before restoration
- Handles version restoration

**5. CollaborationManager**
- WebSocket connection for real-time updates
- Operational transformation for conflict resolution
- Presence tracking (who's viewing, cursor positions)
- Broadcasts document changes to all connected clients

**6. Operational Transformation Engine**
- Transforms concurrent operations to maintain consistency
- Handles insert-insert, insert-delete, delete-delete conflicts
- Ensures all clients see the same document state

---

## 3) Data Models

Here are the key data structures I'd use:

```typescript
// Main document structure
interface Document {
  id: string;
  title: string;
  content: DocumentContent;
  createdAt: string;
  updatedAt: string;
  ownerId: string;
  collaborators: Collaborator[];
  permissions: DocumentPermissions;
  version: number;  // For conflict resolution
}

// Document content structure (block-based)
interface DocumentContent {
  type: 'doc';
  content: Block[];  // Array of blocks (paragraphs, headings, etc.)
}

// A block is a structural element (paragraph, heading, list, table, etc.)
interface Block {
  type: 'paragraph' | 'heading' | 'list' | 'table' | 'image' | 'quote';
  id: string;  // Unique block ID
  content: InlineContent[];  // Text and inline elements
  attributes?: BlockAttributes;  // Block-level formatting
}

// Inline content (text, links, mentions)
interface InlineContent {
  type: 'text' | 'link' | 'mention';
  text?: string;
  marks?: Mark[];  // Formatting marks (bold, italic, etc.)
  attributes?: InlineAttributes;  // Link href, mention userId, etc.
}

// Formatting marks
interface Mark {
  type: 'bold' | 'italic' | 'underline' | 'strikethrough' | 'code';
}

// Block attributes
interface BlockAttributes {
  level?: number;  // For headings (1-6)
  listType?: 'ordered' | 'unordered';
  alignment?: 'left' | 'center' | 'right' | 'justify';
}

// Comment structure
interface Comment {
  id: string;
  documentId: string;
  blockId: string;  // Which block the comment is on
  text: string;
  authorId: string;
  authorName: string;
  createdAt: string;
  resolved: boolean;
  replies: CommentReply[];
  selection?: TextSelection;  // Which text is commented on
}

interface CommentReply {
  id: string;
  text: string;
  authorId: string;
  authorName: string;
  createdAt: string;
}

// Suggestion (for review mode)
interface Suggestion {
  id: string;
  documentId: string;
  blockId: string;
  originalText: string;  // Original text
  suggestedText: string;  // Suggested replacement
  authorId: string;
  authorName: string;
  createdAt: string;
  status: 'pending' | 'accepted' | 'rejected';
  selection: TextSelection;
}

// Text selection for comments/suggestions
interface TextSelection {
  start: number;  // Character offset in block
  end: number;
  blockId: string;
}

// Document version
interface DocumentVersion {
  id: string;
  documentId: string;
  version: number;
  content: DocumentContent;
  authorId: string;
  authorName: string;
  createdAt: string;
  changeSummary: string;  // Brief description of changes
}

// Collaboration
interface Collaborator {
  userId: string;
  email: string;
  role: 'owner' | 'editor' | 'viewer' | 'commenter';
  cursorPosition: CursorPosition | null;
}

interface CursorPosition {
  blockId: string;
  offset: number;  // Character offset in block
  color: string;  // User's cursor color
}

// Document permissions
interface DocumentPermissions {
  canView: string[];  // User IDs
  canEdit: string[];
  canComment: string[];
  isPublic: boolean;
  shareLink?: string;
}

// Update operation for real-time sync
interface DocumentUpdate {
  type: 'insert' | 'delete' | 'format' | 'comment_add' | 'comment_resolve';
  blockId: string;
  position: number;  // Character position in block
  content?: string;  // For insert operations
  length?: number;  // For delete operations
  marks?: Mark[];  // For format operations
  timestamp: string;
  userId: string;
  version: number;  // For conflict resolution
}
```

### Data Flow Explanation

**Document Structure:**
- Documents are block-based (not just plain text)
- Each block is a structural element: paragraph, heading, list item, table, etc.
- Blocks contain inline content: text with formatting, links, mentions
- This structure makes it easier to handle formatting, comments, and collaboration

**When a user types:**
1. Text is inserted into the current block at cursor position
2. Update operation is created (type: 'insert')
3. Operation is applied locally immediately (optimistic update)
4. Operation is broadcasted via WebSocket to other users
5. Other users apply the operation using operational transformation

**When a user adds a comment:**
1. User selects text (creates TextSelection)
2. Comment is created with selection information
3. Comment is saved to server
4. Comment is broadcasted to all users
5. Comment highlight appears in document for all users

**Version History:**
- Each significant change creates a new version
- Versions store the full document content at that point
- Users can preview and restore any version
- Restoration creates a new version (doesn't delete history)

---

## 4) API Design

### REST Endpoints

**GET /api/v1/documents/:id**
- Fetch document data
- Returns document with content, metadata, collaborators
- Response includes current version number

**PATCH /api/v1/documents/:id/content**
- Update document content
- Request contains array of operations (insert, delete, format)
- Uses version number for conflict detection
- Returns new version number and any conflicts

**POST /api/v1/documents/:id/comments**
- Add a comment to the document
- Request includes block ID, text, and selection
- Returns created comment with ID

**GET /api/v1/documents/:id/comments**
- Get all comments for a document
- Returns array of comments with replies

**PATCH /api/v1/documents/:id/comments/:commentId/resolve**
- Resolve a comment (mark as resolved)
- Returns updated comment

**POST /api/v1/documents/:id/export**
- Export document to PDF/DOCX/Markdown
- Request specifies format and options
- Returns file download

**GET /api/v1/documents/:id/versions**
- Get version history
- Returns array of versions with metadata

**POST /api/v1/documents/:id/restore**
- Restore document to a specific version
- Creates new version from restored content
- Returns new version number

### API Request/Response Examples

**Update Document Content:**
```json
// PATCH /api/v1/documents/:id/content
{
  "version": 5,
  "operations": [
    {
      "type": "insert",
      "blockId": "block_1",
      "position": 5,
      "content": " Beautiful"
    },
    {
      "type": "format",
      "blockId": "block_1",
      "position": 0,
      "length": 5,
      "marks": [{"type": "bold"}]
    }
  ]
}

// Response
{
  "success": true,
  "data": {
    "version": 6,
    "appliedOperations": 2,
    "conflicts": []  // Empty if no conflicts
  }
}
```

**Add Comment:**
```json
// POST /api/v1/documents/:id/comments
{
  "blockId": "block_1",
  "text": "This needs revision",
  "selection": {
    "start": 0,
    "end": 5,
    "blockId": "block_1"
  }
}

// Response
{
  "success": true,
  "data": {
    "id": "comment_123",
    "text": "This needs revision",
    "authorId": "user_123",
    "authorName": "John Doe",
    "createdAt": "2024-01-15T12:00:00Z",
    "resolved": false,
    "replies": []
  }
}
```

**Get Document:**
```json
// GET /api/v1/documents/:id
// Response
{
  "success": true,
  "data": {
    "id": "doc_123",
    "title": "My Document",
    "content": {
      "type": "doc",
      "content": [
        {
          "type": "paragraph",
          "id": "block_1",
          "content": [
            {
              "type": "text",
              "text": "Hello World",
              "marks": [{"type": "bold"}]
            }
          ]
        }
      ]
    },
    "version": 5,
    "createdAt": "2024-01-15T10:00:00Z",
    "updatedAt": "2024-01-15T12:00:00Z"
  }
}
```

### WebSocket Protocol

**Connection:** `wss://api.example.com/documents/:id`

**Events:**
- `content_update` - Document content changed (insert, delete, format)
- `comment_add` - Comment added
- `comment_resolve` - Comment resolved
- `presence_update` - User joined/left or cursor moved
- `conflict` - Conflict detected, requires resolution

**Message Format:**
```json
{
  "type": "content_update",
  "data": {
    "operation": {
      "type": "insert",
      "blockId": "block_1",
      "position": 5,
      "content": " Beautiful"
    },
    "version": 5,
    "userId": "user_123",
    "timestamp": "2024-01-15T12:00:00Z"
  }
}
```

### Conflict Resolution Strategy

**Operational Transformation (OT):**
- When two users edit simultaneously, operations are transformed
- Example: User A inserts "Hello" at position 5, User B inserts "World" at position 3
  - Operations are transformed so both insertions are preserved
  - Result: "WoHello" or "HelloWo" depending on transformation rules

**Version-based Conflict Detection:**
- Each operation includes current document version
- If version mismatch, server returns 409 Conflict
- Client must fetch latest version and retry operation

**Transformation Rules:**
- Insert-Insert: If positions are different, adjust positions
- Insert-Delete: Adjust insert position based on delete
- Delete-Delete: Handle overlapping deletes
- Format operations: Usually commutative, can be applied independently

---

## Key Design Decisions

**1. Block-Based Document Structure**
- Documents are structured as blocks (paragraphs, headings, lists)
- Makes formatting, comments, and collaboration easier
- Similar to how Google Docs and Notion work

**2. Operational Transformation for Collaboration**
- Transforms concurrent operations to maintain consistency
- Ensures all users see the same document state
- Handles conflicts automatically

**3. Optimistic Updates**
- Apply changes locally immediately (optimistic)
- Send to server in background
- If server rejects, rollback and show error

**4. WebSocket for Real-time**
- WebSocket connection per document
- Broadcast changes to all connected clients
- Low latency for real-time feel

**5. Version History**
- Store full document content at each version
- Allows restoration to any point in time
- Useful for undo/redo and document recovery

**6. Comment System**
- Comments are anchored to specific text selections
- Comments persist even if text is edited (selection updates)
- Supports threaded replies

---

## Interview Talking Points

**When explaining this system, I'd focus on:**

1. **Requirements First**: Start with what the system needs to do - real-time collaboration, rich text editing, comments, version history

2. **Component Structure**: Explain the React component hierarchy - rich text editor, toolbar, comment panel, version history

3. **Data Models**: Walk through the key data structures - Document, Block, InlineContent, Comment - and the block-based structure

4. **API Design**: Show the REST endpoints and WebSocket protocol for real-time updates

5. **Key Challenges**: 
   - Operational transformation for conflict resolution
   - Real-time synchronization with low latency
   - Comment anchoring to text that might be edited
   - Version history storage and restoration

**Example explanation flow:**
> "So for a collaborative word processor, I'd start with the requirements: we need real-time editing, rich text formatting, comments, and version history. The frontend would be a React app with a rich text editor component (like Slate.js) that handles the editing. Documents are structured as blocks - paragraphs, headings, lists - rather than plain text, which makes formatting and comments easier. Each block contains inline content with formatting marks. For real-time collaboration, we use WebSockets to broadcast changes, and operational transformation to resolve conflicts when multiple users edit simultaneously. Comments are anchored to text selections, and we maintain version history so users can restore previous versions."
