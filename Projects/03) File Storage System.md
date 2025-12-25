# File Storage System

## Overview

Design a cloud file storage system like Dropbox or Google Drive where users can upload, organize, share, and sync files across devices. The system handles large files, versioning, and real-time synchronization.

---

## 1) Requirements

### Functional Requirements

**Core Features:**
- File upload and download with progress tracking
- Folder organization (create, navigate, delete folders)
- File sharing with permissions (read, write, admin)
- File versioning and history (restore previous versions)
- File search by name, content, tags, metadata
- File preview (images, documents, videos)
- Real-time file synchronization across devices
- Drag-and-drop file upload

**Advanced Features:**
- Public links with password protection and expiration
- File collaboration (comments, real-time editing)
- Offline file access with sync
- Advanced search with filters and tags
- File thumbnails and previews

### Non-Functional Requirements

**Performance:**
- File upload: < 10 seconds for 100MB files
- Support files up to 10GB with chunked upload
- Fast file download
- Efficient file search

**Scalability:**
- Support 1B+ users
- Handle 100PB+ storage
- Billions of files
- Millions of concurrent operations

**Reliability:**
- 99.9% uptime
- Data durability and backup
- Fault tolerance

**User Experience:**
- Responsive design (mobile and desktop)
- Accessible interface (keyboard navigation, screen readers)
- Real-time sync indicators

---

## 2) Component Hierarchy

The frontend is a React application for file management. Here's the structure:

```
App
├── Layout
│   ├── Header
│   │   ├── Logo
│   │   ├── SearchBar (global file search)
│   │   ├── UploadButton
│   │   └── UserMenu
│   ├── Sidebar
│   │   ├── FolderTree (hierarchical folder navigation)
│   │   ├── QuickAccess (Recent, Starred, Shared)
│   │   └── StorageUsage (shows used/total storage)
│   └── MainContent
├── Pages
│   ├── FileBrowserPage
│   │   ├── BreadcrumbNavigation (folder path)
│   │   ├── Toolbar
│   │   │   ├── ViewToggle (Grid/List view)
│   │   │   ├── SortOptions (Name, Date, Size)
│   │   │   └── ActionButtons (New Folder, Upload, Share)
│   │   ├── FileGrid (or FileList)
│   │   │   ├── FileCard
│   │   │   │   ├── FileIcon (based on file type)
│   │   │   │   ├── FileName (editable)
│   │   │   │   ├── FileMetadata (size, modified date)
│   │   │   │   ├── FileActions (Share, Download, Delete)
│   │   │   │   └── SelectionCheckbox
│   │   │   └── FolderCard
│   │   │       ├── FolderIcon
│   │   │       ├── FolderName
│   │   │       └── ItemCount
│   │   └── UploadProgress (shows active uploads)
│   ├── FilePreviewPage
│   │   ├── FileViewer (image viewer, PDF viewer, video player)
│   │   ├── FileInfo (metadata, version history)
│   │   ├── CommentsPanel (file comments)
│   │   └── SharePanel (sharing options)
│   └── SharePage
│       ├── ShareDialog
│       │   ├── PermissionSelector (Read, Write, Admin)
│       │   ├── UserSearch (add users)
│       │   ├── PublicLinkToggle
│       │   └── LinkSettings (password, expiration)
│       └── SharedWithList (users who have access)
└── SharedComponents
    ├── FileUploader (drag-and-drop zone)
    ├── UploadProgress (progress bar per file)
    ├── FileIcon (icon based on file type)
    ├── Toast
    └── LoadingSpinner
```

### Key Components Explained

**1. FileBrowser Component**
- Main file browsing interface
- Grid or list view toggle
- Handles file selection (single or multiple)
- Virtual scrolling for large file lists
- Drag-and-drop file upload support

**2. FileUploader Component**
- Handles file selection (file picker or drag-and-drop)
- Chunks large files for upload
- Shows upload progress for each file
- Retry logic for failed uploads
- Uses useOptimistic (React 19) for instant UI feedback

**3. FileCard Component**
- Displays individual file or folder
- Shows file icon, name, metadata
- Handles file actions (share, download, delete)
- Supports inline renaming
- Selection checkbox for bulk operations

**4. FilePreview Component**
- Displays file content (images, PDFs, videos)
- Handles different file types
- Shows file metadata and version history
- Comments and sharing panels

**5. FolderTree Component**
- Hierarchical folder navigation
- Expandable/collapsible folders
- Breadcrumb navigation
- Quick access to recent/favorite folders

---

## 3) Data Models

Here are the key data structures:

```typescript
// File or folder
interface FileItem {
  id: string;
  name: string;
  type: "file" | "folder";
  mimeType?: string;  // For files: "image/jpeg", "application/pdf", etc.
  size?: number;  // File size in bytes
  parentId: string | null;  // Parent folder ID, null for root
  path: string;  // Full path: "/Documents/Projects/file.pdf"
  createdAt: string;
  updatedAt: string;
  modifiedBy: string;
  ownerId: string;
  version: number;  // For versioning
  isShared: boolean;
  permissions: FilePermissions;
  thumbnailUrl?: string;  // For images/videos
}

// File permissions
interface FilePermissions {
  canRead: string[];  // User IDs
  canWrite: string[];  // User IDs
  canAdmin: string[];  // User IDs
  publicLink?: {
    link: string;
    password?: string;
    expiresAt?: string;
  };
}

// File version
interface FileVersion {
  id: string;
  fileId: string;
  version: number;
  size: number;
  createdAt: string;
  createdBy: string;
  downloadUrl: string;
}

// Upload progress
interface UploadProgress {
  fileId: string;
  fileName: string;
  progress: number;  // 0-100
  status: "uploading" | "completed" | "failed";
  error?: string;
}

// Share link
interface ShareLink {
  id: string;
  fileId: string;
  link: string;
  password?: string;
  expiresAt?: string;
  accessCount: number;
  createdAt: string;
}

// File search result
interface FileSearchResult {
  id: string;
  name: string;
  type: "file" | "folder";
  path: string;
  snippet?: string;  // Matching text snippet
  highlights?: string[];  // Highlighted terms
}
```

### Data Flow Explanation

**When a user uploads a file:**
1. User selects files (drag-and-drop or file picker)
2. Files are validated (size, type)
3. Large files are chunked (e.g., 5MB chunks)
4. Each chunk is uploaded sequentially
5. Progress is tracked for each file
6. On completion, file metadata is saved
7. File appears in file browser immediately (optimistic update)

**When a user navigates folders:**
1. User clicks folder in FolderTree or FileCard
2. Fetch files in that folder: `GET /api/v1/files?folderId=xxx`
3. Display files in grid or list view
4. Update breadcrumb navigation
5. Update URL with folder path (for shareability)

**File sharing flow:**
1. User clicks share on a file
2. ShareDialog opens with permission options
3. User selects users or creates public link
4. Permissions are saved
5. Shared users receive notification
6. File appears in their "Shared with me" section

**File versioning:**
1. When file is updated, new version is created
2. Previous versions are preserved
3. Users can view version history
4. Users can restore previous versions
5. Version metadata (who, when) is tracked

---

## 4) API Design

### REST Endpoints

**GET /api/v1/files**
- Get files in a folder
- Query params: `folderId` (null for root), `page`, `limit`, `sortBy`
- Returns: Array of FileItem objects

**POST /api/v1/files/upload**
- Upload a file
- Request: Multipart form data with file and folderId
- Returns: FileItem object
- Supports chunked upload for large files

**GET /api/v1/files/:id**
- Get file metadata
- Returns: FileItem object with full details

**GET /api/v1/files/:id/download**
- Get download URL (signed URL)
- Returns: Download URL with expiration

**PATCH /api/v1/files/:id**
- Update file (rename, move, etc.)
- Request body: `{ name?: string, parentId?: string }`
- Returns: Updated FileItem

**DELETE /api/v1/files/:id**
- Delete a file or folder
- Returns: Success confirmation

**POST /api/v1/files/:id/share**
- Share a file
- Request body: `{ userIds: string[], permissions: FilePermissions }`
- Returns: Updated FileItem with permissions

**GET /api/v1/files/:id/versions**
- Get file version history
- Returns: Array of FileVersion objects

**POST /api/v1/files/:id/restore**
- Restore a previous version
- Request body: `{ version: number }`
- Returns: Updated FileItem

**GET /api/v1/files/search**
- Search files
- Query params: `q` (query), `type`, `folderId`
- Returns: Array of FileSearchResult objects

### API Request/Response Examples

**Upload File:**
```json
// POST /api/v1/files/upload
// FormData: file, folderId
// Response
{
  "success": true,
  "data": {
    "id": "file_123",
    "name": "document.pdf",
    "type": "file",
    "mimeType": "application/pdf",
    "size": 1024000,
    "parentId": "folder_456",
    "path": "/Documents/document.pdf",
    "createdAt": "2024-01-15T10:00:00Z",
    "version": 1
  }
}
```

**Get Files in Folder:**
```json
// GET /api/v1/files?folderId=folder_456&page=1&limit=20
// Response
{
  "success": true,
  "data": {
    "files": [
      {
        "id": "file_123",
        "name": "document.pdf",
        "type": "file",
        "size": 1024000,
        "updatedAt": "2024-01-15T10:00:00Z"
      },
      {
        "id": "folder_789",
        "name": "Projects",
        "type": "folder",
        "updatedAt": "2024-01-14T15:00:00Z"
      }
    ],
    "total": 45,
    "page": 1,
    "limit": 20
  }
}
```

**Share File:**
```json
// POST /api/v1/files/file_123/share
{
  "userIds": ["user_1", "user_2"],
  "permissions": {
    "canRead": ["user_1", "user_2"],
    "canWrite": ["user_1"],
    "canAdmin": []
  }
}

// Response
{
  "success": true,
  "data": {
    "id": "file_123",
    "isShared": true,
    "permissions": {
      "canRead": ["user_1", "user_2"],
      "canWrite": ["user_1"]
    }
  }
}
```

**Search Files:**
```json
// GET /api/v1/files/search?q=project&type=file
// Response
{
  "success": true,
  "data": {
    "results": [
      {
        "id": "file_123",
        "name": "project-plan.pdf",
        "type": "file",
        "path": "/Documents/project-plan.pdf",
        "snippet": "This is the project plan document...",
        "highlights": ["project"]
      }
    ],
    "total": 15
  }
}
```

---

## Key Design Decisions

**1. Chunked Upload for Large Files**
- Split large files into chunks (e.g., 5MB each)
- Upload chunks sequentially or in parallel
- Resume upload from last successful chunk if failed
- Better progress tracking and error handling

**2. Virtual Scrolling for File Lists**
- Only render visible files in viewport
- Improves performance with thousands of files
- Smooth scrolling experience

**3. Optimistic Updates**
- Show files immediately after upload starts
- Use useOptimistic (React 19) for instant UI feedback
- Rollback if upload fails

**4. Real-time Synchronization**
- WebSocket connection for real-time file updates
- Notify users when files are shared/updated
- Sync file changes across devices

**5. File Versioning**
- Store all file versions
- Allow users to restore previous versions
- Track version metadata (who, when, what changed)

**6. Hierarchical Folder Structure**
- Tree structure for folders
- Efficient navigation with breadcrumbs
- Support nested folders (unlimited depth)

---

## Interview Talking Points

**When explaining this system, I'd focus on:**

1. **Requirements First**: Start with core functionality - upload, organize, share, sync files

2. **Component Structure**: Explain the React component hierarchy - file browser, uploader, preview, sharing

3. **Data Models**: Walk through FileItem, FilePermissions, FileVersion - and how they support the features

4. **API Design**: Show the REST endpoints - upload, download, share, search, versioning

5. **Key Challenges**: 
   - Chunked upload for large files (10GB+)
   - Real-time synchronization across devices
   - File versioning and storage optimization
   - Efficient file search across billions of files
   - Handling concurrent file operations

**Example explanation flow:**
> "So for a file storage system, the core requirement is allowing users to upload, organize, and share files. The frontend is a React app with a file browser component that displays files in a grid or list view. Users can upload files via drag-and-drop, and for large files, we chunk them into smaller pieces for reliable upload with progress tracking. The data model centers around FileItem objects that represent files or folders, with a hierarchical structure using parentId. Files can be shared with permissions (read, write, admin), and we support file versioning so users can restore previous versions. For real-time sync, we use WebSockets to notify users when files are shared or updated. The main API endpoints handle upload (with chunking), download (with signed URLs), sharing, and search. Key challenges include handling large file uploads efficiently, real-time synchronization, and providing fast search across billions of files."
