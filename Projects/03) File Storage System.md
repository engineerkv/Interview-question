# 1) Problem Statement

Design and implement a cloud file storage system that addresses the following challenges:

- **Core Functionality**: Enable users to upload, store, organize, and share files with features like folders, search, and synchronization across devices
- **Scale Requirements**: Handle 1B+ users, 100PB+ storage, billions of files, and millions of concurrent file operations
- **Performance**: File upload < 10 seconds for 100MB files, fast file download, efficient file search, real-time synchronization
- **File Management**: Support file versioning, deduplication, folder organization, file sharing with access control, file search
- **Storage Optimization**: Optimize storage costs through deduplication, efficient chunk storage, compression, and lifecycle management
- **Data Durability**: Ensure data durability and availability, handle file replication, provide backup and recovery mechanisms
- **Synchronization**: Support real-time synchronization across devices, handle conflict resolution, maintain file consistency
- **Data Consistency**: Maintain file metadata consistency, handle concurrent file operations reliably, ensure accurate file versioning

---

# 2) High Level Design (HLD)

## a) Functional Requirements

- **File Upload and Download** - Upload files of any size, download files with progress tracking
- **File Versioning** - Track file versions, restore previous versions, view version history
- **File Synchronization** - Sync files across multiple devices in real-time
- **File Sharing and Permissions** - Share files with other users, set permission levels (read, write, admin)
- **File Search** - Search files by name, content, tags, and metadata
- **Folder Organization** - Create folders, organize files in hierarchical structure, move files between folders
- **File Preview** - Preview images, documents, and videos without downloading
- **File Management** - Rename, delete, move, and copy files and folders

---

## b) Non-Functional Requirements

- **Performance**: File upload < 10 seconds for 100MB files, fast file download, efficient file search
- **Scalability**: Support 1B+ users, 100PB+ storage, billions of files, millions of concurrent operations
- **Availability**: 99.9% uptime with fault tolerance and redundancy
- **File Size**: Support files up to 10GB with chunked upload
- **Responsive Design**: Mobile and desktop support with adaptive UI
- **Accessibility**: Keyboard navigation, screen reader support, ARIA labels
- **Security**: Secure file storage, access control, encrypted file transfers

---

## c) MVP (Minimum Viable Product)

**Phase 1: Core Features (Must Have)**

- File upload and download with progress tracking
- Basic folder organization (create, navigate, delete folders)
- File sharing with basic permissions (read, write)
- File search by name
- Responsive web interface

**Phase 2: Enhanced Features**

- File versioning and history
- Advanced file sharing (public links, password protection, expiration)
- Real-time file synchronization across devices
- Advanced search (full-text search, filters, tags)
- File preview and thumbnails
- Drag-and-drop file upload

**Phase 3: Advanced Features**

- File collaboration (real-time editing, comments)
- Bandwidth optimization and compression
- Offline file access with sync
- Advanced analytics and usage reports
- Multi-language support

---

## d) Technology Choices

### Frontend Framework

- **React 19** - Latest React version with useOptimistic, useActionState, useTransition, useDeferredValue, and use() hook
- **TypeScript** - Type safety and better developer experience

### State Management

- **React Query (TanStack Query)** - Server state management for file data, folder structure, search results, and synchronization
- **Redux Toolkit** - Client state management for UI state (selected files, upload queue, view preferences, filters)
- **Context API** - App-wide configuration (user authentication, theme, app settings)

### UI/UX Libraries

- **React Router** - Client-side routing for navigation between folders and pages
- **React Hot Toast** - Toast notifications for upload progress, errors, and success messages
- **@tanstack/react-virtual** - Virtual scrolling for large file lists
- **React Dropzone** - Drag-and-drop file upload interface

### Build Tools

- **Vite** - Fast build tool and development server with HMR
- **Webpack** (alternative) - Module bundler with code splitting

### Testing

- **React Testing Library** - Component testing for file components
- **Vitest / Jest** - Unit testing framework
- **Playwright / Cypress** - E2E testing for file operations

### Deployment

- **Vercel / Netlify** - Static site hosting with CDN and automatic deployments
- **AWS S3 + CloudFront** - Alternative deployment with custom CDN configuration

**Trade-offs:**

- **React Query vs SWR**: React Query provides better caching and mutation handling, but SWR is lighter - choose React Query for complex file operations
- **Redux Toolkit vs Zustand**: Redux Toolkit offers better DevTools and middleware, but Zustand is simpler - choose Redux Toolkit for complex state management needs
- **Vite vs Webpack**: Vite is faster for development, but Webpack has more plugins - choose Vite for modern React projects

---

## e) Architecture Overview

The frontend follows a layered architecture with clear separation of concerns, optimized for file management operations.

**Component Structure:**

```

Frontend Application
├── Presentation Layer
│   ├── UI Components (FileCard, FolderCard, UploadProgress, ShareDialog, FileIcon)
│   ├── Feature Components (FileBrowser, FileUploader, FileViewer, ShareManager, SearchBar, FolderTree)
│   └── Layout Components (Header, Sidebar, Navigation, MainLayout, BreadcrumbNavigation)
├── Business/Controller Layer
│   ├── Business Logic (File validation, file format checking, path normalization)
│   ├── Custom Hooks (useFileUpload, useFileDownload, useFileShare, useFileSync)
│   └── Service Functions (Chunking, hashing, format detection)
├── State Management
│   ├── Client State
│   │   ├── Local State (useState) - Component-specific UI state
│   │   ├── Global State (Redux Toolkit) - File list, folder structure, upload queue, user preferences
│   │   └── Context API - User authentication, theme preferences, app-wide settings
│   └── Server State
│       ├── React Query (useQuery/useMutation) - File data caching, refetching, optimistic updates, synchronization
│       └── Service Worker - Offline caching, background file sync
├── API Integration
│   ├── API Client (Axios with interceptors for auth, error handling, retry logic)
│   ├── API Services (fileService, folderService, shareService, syncService)
│   └── Request/Response Transformation (Data normalization, error handling, progress tracking)
└── Routing
    ├── Public Routes (Home)
    ├── Protected Routes (File Browser, Share Pages)
    └── Route Guards (Authentication and authorization checks for file access)

```

**Frontend Deployment:**

- **Build**: Production bundle with code splitting and lazy loading using Webpack/Vite
- **CDN**: Static assets served from CloudFront/Cloudflare edge locations for fast global delivery
- **Caching**: Aggressive caching for static assets, cache-busting for updates
- **Environment**: Environment variables for API endpoints and feature flags

**Key Frontend Components:**

- **React 19 Application**:
  - Single-page application with client-side routing
  - Component-based architecture for reusability
  - React Query with React 19 hooks (useOptimistic, useTransition, useDeferredValue)
  - File upload with progress tracking and chunking
  - Responsive design for mobile and desktop
  - Modern React 19 features for better performance and UX

- **CDN/Edge**:
  - Global distribution of static assets
  - Edge caching for improved performance
  - DDoS protection and rate limiting at edge

**Trade-offs:**

- **Layered Architecture**: Provides clear separation of concerns and maintainability, but can add complexity for simple operations - works great for large file management applications
- **Business/Controller Layer**: Centralizes business logic and makes it testable, but requires careful design to avoid over-engineering - essential for complex file operations
- **State Management Separation**: Client and server state separation improves performance and caching, but requires understanding when to use each - React Query for server data, Redux for complex UI state

---

## f) App Flow

### Complete System Flow (Frontend Perspective)

**Primary User Flow - File Upload:**

1. **User lands on file browser** → React Router renders FileBrowserPage component
2. **User selects files** → FileUploader component captures files via drag-and-drop or file picker
3. **File validation** → Client-side validation checks file size, type, and name
4. **Chunk preparation** → Large files split into chunks using useTransition (React 19) for non-urgent processing
5. **Upload starts** → useFileUpload hook triggers React Query mutation with progress tracking
6. **Progress tracking** → UploadProgress component shows real-time upload progress for each file
7. **Chunk upload** → Each chunk uploaded sequentially with retry logic
8. **Success response** → React Query caches response, FileCard component renders in file list
9. **State update** → Components re-render with new file data, toast notification shows success

**Component Interaction Flow:**

```

User Selects Files → FileUploader (local state)
            ↓
File Validation → useFileUpload hook (business logic)
            ↓
Chunk Preparation → FileChunker service (useTransition for non-urgent)
            ↓
Upload Start → React Query mutation (useOptimistic for instant UI)
            ↓
Progress Updates → UploadProgress (receives progress events)
            ↓
Response → React Query cache update
            ↓
Re-render → FileBrowser (receives cached file list)

```

**State Update Flow:**

1. **Local State** → FileUploader uses useState for selected files, upload progress
2. **Optimistic State** → useOptimistic (React 19) shows files immediately before upload completes
3. **Server State** → React Query manages file list, folder structure, caching, refetching
4. **Global State** → Redux Toolkit manages upload queue, selected files, view preferences
5. **Component Re-render** → React updates UI based on state changes

**Error Handling Flow:**

1. **API Error** → React Query mutation returns error
2. **Error Boundary** → Catches component errors, shows fallback UI
3. **User Feedback** → Toast notification displays error message with retry option
4. **Retry Logic** → Failed chunks automatically retry with exponential backoff
5. **Partial Upload** → Resume upload from last successful chunk

**File Download Flow:**

1. **User clicks download** → FileCard triggers download action
2. **Download URL fetch** → React Query useQuery fetches signed download URL
3. **Download starts** → Browser downloads file with progress tracking
4. **Progress display** → DownloadProgress component shows download percentage
5. **Completion** → Toast notification confirms successful download

**File Sharing Flow:**

1. **User clicks share** → ShareDialog component opens
2. **User selects permissions** → PermissionSelector updates share settings
3. **Share creation** → useFileShare hook triggers React Query mutation
4. **Share link generated** → ShareLink component displays shareable link
5. **Copy to clipboard** → CopyButton uses Clipboard API, shows toast notification

**File Synchronization Flow:**

1. **File change detected** → FileSync service detects local file changes
2. **Sync trigger** → useFileSync hook triggers React Query mutation
3. **Conflict detection** → System checks for conflicts with server version
4. **Conflict resolution** → ConflictResolver component prompts user for resolution
5. **Sync completion** → File list updates, toast notification confirms sync

**Folder Navigation Flow:**

1. **User clicks folder** → FolderCard triggers navigation
2. **Route update** → React Router updates URL to /folder/:folderId
3. **Data fetching** → React Query useSuspenseQuery fetches folder contents
4. **Loading state** → Skeleton screens displayed while loading
5. **File list display** → FileBrowser renders files and folders
6. **Breadcrumb update** → BreadcrumbNavigation updates navigation path

# 3) Component Architecture

Think of the frontend as a tree of React components - each component handles a specific part of the UI, and they work together to create the complete user experience.

**Component Hierarchy:**

```

App
├── Layout
│   ├── Header
│   │   ├── Logo
│   │   ├── Navigation
│   │   └── UserMenu
│   ├── Sidebar
│   │   ├── FolderTree
│   │   └── QuickAccess
│   ├── MainContent
│   └── Footer
├── Pages
│   ├── FileBrowserPage
│   │   ├── BreadcrumbNavigation
│   │   ├── FileBrowser
│   │   │   ├── FileCard
│   │   │   ├── FolderCard
│   │   │   └── FileGrid
│   │   ├── FileUploader
│   │   │   ├── Dropzone
│   │   │   ├── FilePicker
│   │   │   └── UploadProgress
│   │   └── FileViewer
│   │       ├── ImageViewer
│   │       ├── DocumentViewer
│   │       └── VideoViewer
│   ├── SharePage
│   │   ├── ShareDialog
│   │   │   ├── PermissionSelector
│   │   │   ├── ShareLink
│   │   │   └── ShareSettings
│   │   └── SharedFilesList
│   └── SearchPage
│       ├── SearchBar
│       └── SearchResults
└── SharedComponents
    ├── Button
    ├── Input
    ├── Card
    ├── Toast
    ├── LoadingSpinner
    ├── ProgressBar
    └── Modal

```

**Key React Components:**

**1. FileBrowser Component:**

- Displays files and folders in grid or list view
- Handles file selection with multi-select support
- Uses virtual scrolling for large file lists
- Fetches file list with React Query useSuspenseQuery (React 19)
- Uses useTransition (React 19) for non-urgent view changes

**2. FileUploader Component:**

- Handles drag-and-drop and file picker uploads
- Manages upload queue with Redux Toolkit
- Uses useOptimistic (React 19) for instant UI feedback
- Shows upload progress for each file
- Handles chunked uploads for large files

**3. FileCard Component:**

- Displays file metadata (name, size, date, icon)
- Handles file actions (download, share, delete, rename)
- Shows file preview thumbnail
- Uses React.memo for performance optimization

**4. FolderTree Component:**

- Displays hierarchical folder structure
- Handles folder expansion/collapse
- Supports drag-and-drop for moving files
- Uses React Query for folder data caching

**5. ShareDialog Component:**

- Manages file sharing with permissions
- Generates shareable links
- Handles permission updates
- Uses React Query mutation for share operations

**6. FileViewer Component:**

- Displays file previews (images, documents, videos)
- Handles file navigation (next/previous)
- Supports fullscreen mode
- Uses lazy loading for large files

**Component Communication:**

- **Props** → Parent to child data flow
- **Callbacks** → Child to parent communication
- **Context API** → Shared state across components (theme, user)
- **React Query** → Server state management (files, folders, shares)
- **Redux Toolkit** → Global client state (upload queue, selected files, view preferences)

# 4) Data Models

### TypeScript Interfaces

```typescript
interface File {
  id: string;
  name: string;
  size: number;
  type: string;
  mimeType: string;
  folderId: string | null;
  path: string;
  createdAt: string;
  updatedAt: string;
  uploadedBy: string;
  version: number;
  thumbnailUrl?: string;
  previewUrl?: string;
}

interface Folder {
  id: string;
  name: string;
  parentId: string | null;
  path: string;
  createdAt: string;
  updatedAt: string;
  createdBy: string;
}

interface FileUpload {
  fileId: string;
  fileName: string;
  fileSize: number;
  uploadId: string;
  chunks: Array<{ index: number; chunkId: string }>;
  progress: number;
  status: "pending" | "uploading" | "completed" | "failed";
}

interface Share {
  id: string;
  fileId: string;
  userId?: string;
  permission: "read" | "write" | "admin";
  shareLink?: string;
  expiresAt?: string;
  createdAt: string;
}

interface FileVersion {
  id: string;
  fileId: string;
  version: number;
  size: number;
  createdAt: string;
  createdBy: string;
}

interface SearchResult {
  id: string;
  name: string;
  type: "file" | "folder";
  path: string;
  matches: string[];
}

interface FormState {
  fileName: string;
  folderId: string | null;
  errors: {
    fileName?: string;
    folderId?: string;
  };
}

```

# 5) API Design

### POST /api/v1/files/upload

- **URL:** `/api/v1/files/upload`
- **Method:** POST
- **Description:** Upload a file (supports chunked upload)
- **Content-Type:** `multipart/form-data`
- **Request Body:**

 ```

 file: [File]
 folderId(optional)
 fileName(optional, defaults to original filename)

 ```

- **Response:**

 ```json
 {
 "success": true,
 "data": {
 "fileId": "file_abc123",
 "fileName": "document.pdf",
 "fileSize": 5242880,
 "uploadId": "upload_xyz789",
 "chunks": [
 { "index": 0, "chunkId": "chunk_1" },
 { "index": 1, "chunkId": "chunk_2" }
 ],
 "createdAt": "2024-01-15T10:30:00Z"
 }
 }

 ```

- **Status Codes:** 201 (Created), 400 (Validation Error), 413 (File Too Large), 507 (Storage Quota Exceeded)

### GET /api/v1/files/:fileId/download

- **URL:** `/api/v1/files/:fileId/download`
- **Method:** GET
- **Description:** Get download URL for file
- **Response:**

 ```json
 {
 "success": true,
 "data": {
 "downloadUrl": "https://s3.amazonaws.com/bucket/file_abc123?signature=...",
 "expiresAt": "2024-01-15T11:30:00Z"
 }
 }

 ```

- **Status Codes:** 200 (Success), 404 (File Not Found), 403 (Access Denied)

### POST /api/v1/files/:fileId/share

- **URL:** `/api/v1/files/:fileId/share`
- **Method:** POST
- **Description:** Share file with other users
- **Request Body:**

 ```json
 {
 "userId": "user_xyz789",
 "permission": "read" // read, write, admin
 }

 ```

- **Response:**

 ```json
 {
 "success": true,
 "data": {
 "shareId": "share_abc123",
 "fileId": "file_abc123",
 "userId": "user_xyz789",
 "permission": "read",
 "createdAt": "2024-01-15T10:30:00Z"
 }
 }

 ```

- **Status Codes:** 201 (Created), 400 (Validation Error), 404 (File Not Found)

### GET /api/v1/files

- **URL:** `/api/v1/files?folderId=folder_123&page=1&limit=50`
- **Method:** GET
- **Description:** Get list of files in a folder
- **Query Parameters:**
  - `folderId` (optional) - Filter by folder ID
  - `page` (default: 1) - Page number
  - `limit` (default: 50) - Results per page
  - `sortBy` (optional) - Sort by name, date, size
- **Response:**

  ```json
  {
    "success": true,
    "data": {
      "files": [
        {
          "id": "file_abc123",
          "name": "document.pdf",
          "size": 5242880,
          "type": "file",
          "mimeType": "application/pdf",
          "folderId": "folder_123",
          "createdAt": "2024-01-15T10:30:00Z",
          "updatedAt": "2024-01-15T10:30:00Z"
        }
      ],
      "folders": [
        {
          "id": "folder_456",
          "name": "Documents",
          "parentId": "folder_123",
          "createdAt": "2024-01-15T10:30:00Z"
        }
      ],
      "total": 125,
      "page": 1,
      "limit": 50
    }
  }
  ```

- **Status Codes:** 200 (Success), 404 (Folder Not Found)

### GET /api/v1/files/:fileId

- **URL:** `/api/v1/files/:fileId`
- **Method:** GET
- **Description:** Get file metadata
- **Response:**

  ```json
  {
    "success": true,
    "data": {
      "id": "file_abc123",
      "name": "document.pdf",
      "size": 5242880,
      "type": "file",
      "mimeType": "application/pdf",
      "folderId": "folder_123",
      "path": "/Documents/document.pdf",
      "createdAt": "2024-01-15T10:30:00Z",
      "updatedAt": "2024-01-15T10:30:00Z",
      "uploadedBy": "user_xyz789",
      "version": 3,
      "thumbnailUrl": "https://cdn.example.com/thumbnails/file_abc123.jpg",
      "previewUrl": "https://cdn.example.com/previews/file_abc123.pdf"
    }
  }
  ```

- **Status Codes:** 200 (Success), 404 (File Not Found)

### GET /api/v1/files/search

- **URL:** `/api/v1/files/search?q=document&type=file&page=1`
- **Method:** GET
- **Description:** Search files by name or content
- **Query Parameters:**
  - `q` (required) - Search query
  - `type` (optional) - Filter by file or folder
  - `page` (default: 1) - Page number
- **Response:**

  ```json
  {
    "success": true,
    "data": {
      "results": [
        {
          "id": "file_abc123",
          "name": "document.pdf",
          "type": "file",
          "path": "/Documents/document.pdf",
          "matches": ["document"]
        }
      ],
      "total": 25,
      "page": 1
    }
  }
  ```

- **Status Codes:** 200 (Success), 400 (Invalid Query)

---

# 6) Protocols

### REST API Protocol

**Request Format:**

- HTTP methods: GET, POST, PUT, DELETE
- Headers: Content-Type: application/json or multipart/form-data
- Authentication: Bearer token in Authorization header

**Response Format:**

- Success: `{ success: true, data: {...} }`
- Error: `{ success: false, error: {...} }`
- Status codes: 200 (Success), 201 (Created), 400 (Bad Request), 401 (Unauthorized), 403 (Forbidden), 404 (Not Found), 413 (Payload Too Large), 507 (Insufficient Storage), 500 (Server Error)

**Error Response Format:**

```json
{
  "success": false,
  "error": {
    "code": "FILE_TOO_LARGE",
    "message": "File size exceeds maximum allowed size",
    "details": "Maximum file size is 10GB"
  }
}

```

**Authentication:**

- Bearer token authentication for protected routes
- Token stored in httpOnly cookie
- Automatic token refresh on 401 responses
- Redirect to login on authentication failure

**Request Headers:**

```

Content-Type: multipart/form-data
Authorization: Bearer <token>
Accept: application/json

```

**Response Headers:**

```

Content-Type: application/json
X-RateLimit-Limit: 1000
X-RateLimit-Remaining: 999
X-RateLimit-Reset: 1640995200

```

**File Upload Protocol:**

- Chunked upload for files > 100MB
- Chunk size: 5MB per chunk
- Resume upload from last successful chunk
- Progress tracking via WebSocket or polling

---

# 7) Low Level Design (LLD)

## ii) State Management

### Client State

**Local State (useState):**

- Component-specific UI state (file selection, modal visibility, upload progress)
- Example: `const [selectedFiles, setSelectedFiles] = useState<string[]>([]);`

**Global State:**

- Redux Toolkit for complex global state (upload queue, selected files, view preferences)
- Context API for user authentication, theme preferences
- Example: Upload queue, file selection, folder navigation state

### Server State

**React Query (TanStack Query):**

- `useQuery` for data fetching and caching
- `useMutation` for data mutations (upload, delete, share)
- `useSuspenseQuery` (React 19) for better loading states
- Automatic refetching, background updates, optimistic updates
- Example: File list caching, folder structure synchronization

**State Management for File Storage System:**

**Client State Examples (React 19):**

```typescript
import { useState, useTransition, useOptimistic } from 'react';

// File selection with transition (React 19)
const [selectedFiles, setSelectedFiles] = useState<string[]>([]);
const [isPending, startTransition] = useTransition();

// Upload queue with optimistic updates (React 19)
const [uploadQueue, addOptimisticUpload] = useOptimistic(
  [] as FileUpload[],
  (currentQueue, newUpload) => [...currentQueue, newUpload]
);

```

**Server State with React Query (React 19):**

```typescript
import { use, useTransition } from 'react';
import { useQuery, useMutation, useSuspenseQuery } from '@tanstack/react-query';

// Fetch file list with Suspense (React 19)
const { data: files } = useSuspenseQuery({
  queryKey: ['files', folderId],
  queryFn: () => fetchFiles(folderId),
  staleTime: 30000 // 30 seconds
});

// File upload mutation with optimistic updates
const uploadMutation = useMutation({
  mutationFn: uploadFile,
  onMutate: async (newFile) => {
    await queryClient.cancelQueries({ queryKey: ['files'] });
    const previousFiles = queryClient.getQueryData(['files']);
    queryClient.setQueryData(['files'], (old: File[]) => [...old, newFile]);
    return { previousFiles };
  },
  onError: (err, newFile, context) => {
    queryClient.setQueryData(['files'], context?.previousFiles);
  }
});

// Using use() hook for promise handling (React 19)
function FileViewer({ filePromise }: { filePromise: Promise<File> }) {
  const file = use(filePromise);
  return <FilePreview file={file} />;
}

```

**Global State (Redux Toolkit):**

```typescript
// Upload queue slice
const uploadQueueSlice = createSlice({
  name: 'uploadQueue',
  initialState: [] as FileUpload[],
  reducers: {
    addUpload: (state, action) => {
      state.push(action.payload);
    },
    updateUploadProgress: (state, action) => {
      const upload = state.find(u => u.uploadId === action.payload.uploadId);
      if (upload) upload.progress = action.payload.progress;
    },
    removeUpload: (state, action) => {
      return state.filter(u => u.uploadId !== action.payload);
    }
  }
});

// File selection slice
const fileSelectionSlice = createSlice({
  name: 'fileSelection',
  initialState: [] as string[],
  reducers: {
    selectFile: (state, action) => {
      if (!state.includes(action.payload)) {
        state.push(action.payload);
      }
    },
    deselectFile: (state, action) => {
      return state.filter(id => id !== action.payload);
    },
    clearSelection: () => []
  }
});

```

## iii) Implementation Details

### Business/Controller Layer

**Custom Hooks:**

- Encapsulate business logic and API calls
- Example: `useFileUpload`, `useFileDownload`, `useFileShare`, `useFileSync`
- Handle data transformation and validation

**Service Functions:**

- Pure functions for data processing and validation
- File chunking, hashing, format detection, path normalization
- Reusable across components

### Advanced Component Patterns

**Compound Components:**

- Group related components together (e.g., FileBrowser.FileCard, FileBrowser.FolderCard)
- Share implicit state between components

**Render Props Pattern:**

- Pass render functions as props for flexible component composition

**Custom Hooks Pattern:**

- Extract reusable logic into custom hooks
- Example: `useFileUpload`, `useFileDownload`, `useDragAndDrop`, `useFilePreview`

**Higher-Order Components (HOCs):**

- Wrap components with additional functionality
- Example: `withFileAccess`, `withUploadProgress`

### Performance Optimizations (React 19)

- **Code splitting** with React.lazy() and Suspense (React 19 improves Suspense)
- **Memoization** with useMemo() and useCallback()
- **useDeferredValue()** for deferring non-urgent file operations (React 19)
- **useTransition()** for marking non-urgent state updates (React 19)
- **Virtual scrolling** for long file lists (react-window, react-virtuoso)
- **Image optimization** and lazy loading with native loading="lazy"
- **Chunked file uploads** for large files
- **React.memo** for preventing unnecessary re-renders
- **useOptimistic()** for instant UI feedback on file operations (React 19)

### UI/UX Enhancements

- **Toast notifications** for user feedback (react-hot-toast)
- **Loading states** and skeleton screens
- **Error boundaries** for error handling
- **Responsive design** for mobile and desktop
- **Accessibility features** (ARIA labels, keyboard navigation, focus management)
- **Animations** with Framer Motion or CSS transitions
- **Drag-and-drop** file upload interface
- **Progress bars** for upload/download operations

### Code Examples

**Custom Hook: useFileUpload (React 19)**

```typescript
import { useOptimistic, useTransition } from 'react';
import { useMutation } from '@tanstack/react-query';

function useFileUpload() {
  const [optimisticFiles, addOptimisticFile] = useOptimistic(
    [] as File[],
    (currentFiles, newFile: File) => [...currentFiles, newFile]
  );
  const [isPending, startTransition] = useTransition();

  return useMutation({
    mutationFn: async (file: File) => {
      addOptimisticFile({ id: 'temp', name: file.name, size: file.size } as File);
      return await uploadFile(file);
    },
    onSuccess: () => {
      queryClient.invalidateQueries({ queryKey: ['files'] });
    }
  });
}

```

**Component with React Query (React 19):**

```typescript
function FileBrowser({ folderId }: { folderId: string }) {
  const [isPending, startTransition] = useTransition();
  const { data: files } = useSuspenseQuery({
    queryKey: ['files', folderId],
    queryFn: () => fetchFiles(folderId)
  });

  const handleFolderClick = (id: string) => {
    startTransition(() => {
      navigate(`/folder/${id}`);
    });
  };

  return (
    <div>
      {files.map(file => (
        <FileCard key={file.id} file={file} onClick={handleFolderClick} />
      ))}
    </div>
  );
}

```

**File Upload Component (React 19):**

```typescript
function FileUploader() {
  const [files, setFiles] = useState<File[]>([]);
  const [isPending, startTransition] = useTransition();
  const uploadMutation = useFileUpload();

  const handleDrop = (acceptedFiles: File[]) => {
    startTransition(() => {
      setFiles(prev => [...prev, ...acceptedFiles]);
      acceptedFiles.forEach(file => {
        uploadMutation.mutate(file);
      });
    });
  };

  return (
    <Dropzone onDrop={handleDrop}>
      {({ getRootProps, getInputProps }) => (
        <div {...getRootProps()}>
          <input {...getInputProps()} />
          {isPending ? <LoadingSpinner /> : <UploadArea />}
        </div>
      )}
    </Dropzone>
  );
}

```

**Chunked Upload Implementation:**

```typescript
async function uploadFileInChunks(file: File, onProgress: (progress: number) => void) {
  const chunkSize = 5 * 1024 * 1024; // 5MB
  const totalChunks = Math.ceil(file.size / chunkSize);
  let uploadedBytes = 0;

  for (let i = 0; i < totalChunks; i++) {
    const start = i * chunkSize;
    const end = Math.min(start + chunkSize, file.size);
    const chunk = file.slice(start, end);

    await uploadChunk(chunk, i, totalChunks);
    uploadedBytes += chunk.size;
    onProgress((uploadedBytes / file.size) * 100);
  }
}

```

## iv) Testing

### Component Testing

- React Testing Library for component tests
- Test user interactions and component behavior
- Example: Test file upload, folder navigation, file selection

### Integration Testing

- Test component interactions
- Test API integration with mock data
- Test state management flows

### E2E Testing

- Playwright or Cypress for end-to-end tests
- Test complete user flows
- Example: Test file upload flow from start to finish

**File Storage System Specific Tests:**

**Component Test: FileUploader**

```typescript
test('handles file drop', async () => {
  const file = new File(['content'], 'test.pdf', { type: 'application/pdf' });
  render(<FileUploader />);
  const dropzone = screen.getByTestId('dropzone');
  fireEvent.drop(dropzone, { dataTransfer: { files: [file] } });
  await waitFor(() => {
    expect(screen.getByText('test.pdf')).toBeInTheDocument();
  });
});

test('shows upload progress', async () => {
  render(<FileUploader />);
  // Simulate file upload with progress
  await waitFor(() => {
    expect(screen.getByText(/50%/)).toBeInTheDocument();
  });
});

```

**Integration Test: File Upload Flow**

```typescript
test('complete file upload flow', async () => {
  render(<App />);
  const file = new File(['content'], 'test.pdf', { type: 'application/pdf' });
  fireEvent.drop(screen.getByTestId('dropzone'), {
    dataTransfer: { files: [file] }
  });
  await waitFor(() => {
    expect(screen.getByText('test.pdf')).toBeInTheDocument();
  });
  await waitFor(() => {
    expect(screen.getByText(/upload complete/i)).toBeInTheDocument();
  });
});

```

**E2E Test: Complete File Management Journey**

```typescript
test('user can upload, view, and download file', async ({ page }) => {
  await page.goto('/files');
  await page.setInputFiles('input[type="file"]', 'test.pdf');
  await page.waitForSelector('text=test.pdf');
  await page.click('text=test.pdf');
  await expect(page.locator('text=Download')).toBeVisible();
  await page.click('text=Download');
  await expect(page.locator('text=Download started')).toBeVisible();
});

```

# 8) Algorithms

### Frontend Algorithms

**File Chunking Algorithm:**

```javascript
function chunkFile(file, chunkSize = 5 * 1024 * 1024) {
  const chunks = [];
  let start = 0;

  while (start < file.size) {
    const end = Math.min(start + chunkSize, file.size);
    chunks.push({
      index: chunks.length,
      blob: file.slice(start, end),
      start,
      end
    });
    start = end;
  }

  return chunks;
}

```

**File Hash Calculation (MD5):**

```javascript
async function calculateFileHash(file) {
  const buffer = await file.arrayBuffer();
  const hashBuffer = await crypto.subtle.digest('SHA-256', buffer);
  const hashArray = Array.from(new Uint8Array(hashBuffer));
  return hashArray.map(b => b.toString(16).padStart(2, '0')).join('');
}

```

**Path Normalization Algorithm:**

```javascript
function normalizePath(path) {
  return path
    .split('/')
    .filter(segment => segment && segment !== '.')
    .reduce((acc, segment) => {
      if (segment === '..') {
        acc.pop();
      } else {
        acc.push(segment);
      }
      return acc;
    }, [])
    .join('/');
}

```

**File Type Detection:**

```javascript
function detectFileType(file) {
  const extension = file.name.split('.').pop()?.toLowerCase();
  const mimeType = file.type;

  const typeMap = {
    'pdf': 'document',
    'doc': 'document',
    'docx': 'document',
    'jpg': 'image',
    'jpeg': 'image',
    'png': 'image',
    'mp4': 'video',
    'mov': 'video'
  };

  return typeMap[extension] || 'file';
}

```

**Upload Progress Calculation:**

```javascript
function calculateUploadProgress(uploadedChunks, totalChunks) {
  return Math.round((uploadedChunks / totalChunks) * 100);
}

```

**File Size Formatting:**

```javascript
function formatFileSize(bytes) {
  const units = ['B', 'KB', 'MB', 'GB', 'TB'];
  let size = bytes;
  let unitIndex = 0;

  while (size >= 1024 && unitIndex < units.length - 1) {
    size /= 1024;
    unitIndex++;
  }

  return `${size.toFixed(2)} ${units[unitIndex]}`;
}

```

# 9) Security

### Frontend Security

**Input Validation:**

- Client-side validation before file upload
- Validate file size, type, and name
- Sanitize file names to prevent path traversal
- Check file extensions against allowed list

**XSS Prevention:**

- React automatically escapes content
- Use `dangerouslySetInnerHTML` only when necessary with sanitization
- Content Security Policy (CSP) headers
- Sanitize file previews and metadata

**CSRF Protection:**

- SameSite cookies for authentication
- CSRF tokens for state-changing operations
- Verify origin header on API requests

**Secure Storage:**

- Never store sensitive data in localStorage
- Use httpOnly cookies for authentication tokens
- Clear sensitive data on logout
- Encrypt file metadata in transit

**HTTPS:**

- All API calls over HTTPS
- Enforce HTTPS in production
- HSTS headers for security

**Rate Limiting (Client-Side):**

- Debounce API calls to prevent abuse
- Show user-friendly messages when rate limited
- Implement exponential backoff for retries
- Limit concurrent uploads

**File Storage System Specific Security:**

**File Name Sanitization:**

```typescript
function sanitizeFileName(fileName: string): string {
  // Remove path traversal attempts
  const sanitized = fileName
    .replace(/\.\./g, '')
    .replace(/[\/\\]/g, '_')
    .replace(/[<>:"|?*]/g, '');

  // Limit length
  const maxLength = 255;
  if (sanitized.length > maxLength) {
    const ext = sanitized.split('.').pop();
    const name = sanitized.substring(0, maxLength - ext.length - 1);
    return `${name}.${ext}`;
  }

  return sanitized;
}

```

**File Type Validation:**

```typescript
const ALLOWED_TYPES = ['image/jpeg', 'image/png', 'application/pdf', 'text/plain'];
const ALLOWED_EXTENSIONS = ['.jpg', '.jpeg', '.png', '.pdf', '.txt'];

function validateFileType(file: File): boolean {
  return ALLOWED_TYPES.includes(file.type) ||
         ALLOWED_EXTENSIONS.some(ext => file.name.toLowerCase().endsWith(ext));
}

function validateFileSize(file: File, maxSize: number = 10 * 1024 * 1024 * 1024): boolean {
  return file.size <= maxSize;
}

```

**Upload Rate Limiting:**

```typescript
let uploadRequestCount = 0;
let resetTime = Date.now() + 60000; // 1 minute

function checkUploadRateLimit(): boolean {
  if (Date.now() > resetTime) {
    uploadRequestCount = 0;
    resetTime = Date.now() + 60000;
  }
  if (uploadRequestCount >= 10) {
    toast.error('Too many uploads. Please wait a moment.');
    return false;
  }
  uploadRequestCount++;
  return true;
}

```

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

**File Storage System Deployment Configuration:**

**Environment Variables:**

```bash
VITE_API_URL=https://api.storage.example.com
VITE_MAX_FILE_SIZE=10737418240
VITE_CHUNK_SIZE=5242880
VITE_ENABLE_PREVIEW=true
VITE_CDN_URL=https://cdn.example.com

```

**Build Configuration (vite.config.ts):**

```typescript
export default defineConfig({
  build: {
    rollupOptions: {
      output: {
        manualChunks: {
          'react-vendor': ['react', 'react-dom', 'react-router-dom'],
          'query-vendor': ['@tanstack/react-query'],
          'redux-vendor': ['@reduxjs/toolkit'],
          'upload-vendor': ['react-dropzone']
        }
      }
    }
  }
});

```

**CDN Configuration:**

- Static assets cached for 1 year
- HTML files cached for 5 minutes
- Cache busting via query parameters for updates
- Gzip/Brotli compression enabled

**Monitoring Setup:**

- Track upload success rate
- Monitor API response times
- Alert on error rate spikes (> 5%)
- Track file operations (uploads, downloads, shares)

# 11) Interview Answers (Frontend Focus)

### Q: How would you handle state management for this system?

**Answer (STAR Method):**

**Situation:** In a file storage system, we need to manage file lists, upload queues, folder structures, and synchronization efficiently.

**Action:**

- Use React Query for server state (file lists, folder structure, shares) - handles caching, refetching, and synchronization
- Use `useOptimistic()` (React 19) for instant UI feedback on file operations
- Use `useTransition()` (React 19) for non-urgent folder navigation and view changes
- Use `useDeferredValue()` (React 19) for deferring expensive file operations
- Use Redux Toolkit for global client state (upload queue, selected files, view preferences)
- Use useState for local component state (modal visibility, form inputs)
- Use Context API for user authentication, theme preferences

**Result:** Reduced API calls through caching, improved performance with deferred values, better user experience with instant feedback, efficient upload queue management.

**Takeaway:** Separating client and server state management leads to cleaner code and better performance. React 19's optimistic updates are perfect for file operations.

### Q: How would you implement file upload with progress tracking?

**Answer (STAR Method):**

**Situation:** Users need to upload large files with real-time progress feedback and the ability to resume failed uploads.

**Action:**

- Implement chunked upload for files > 100MB
- Use `useOptimistic()` (React 19) to show files immediately in the UI
- Use `useTransition()` (React 19) for non-urgent chunk processing
- Track upload progress via XMLHttpRequest or Fetch API with progress events
- Store upload state in Redux Toolkit for persistence
- Implement retry logic with exponential backoff for failed chunks
- Allow resume from last successful chunk

**Result:** Users see instant feedback, can track upload progress, and resume failed uploads. Reduced server load through chunking.

**Takeaway:** Chunked uploads with React 19's optimistic updates provide excellent UX for large file uploads.

### Q: How would you optimize performance for displaying thousands of files?

**Answer (STAR Method):**

**Situation:** Users need to browse file lists efficiently without performance degradation, even with 10,000+ files.

**Action:**

- Implement virtual scrolling using react-window or react-virtuoso
- Use `useDeferredValue()` (React 19) for search and filtering to defer expensive operations
- Use `useTransition()` (React 19) for non-urgent file list updates
- Use pagination with React Query's infinite query
- Implement code splitting for FileBrowser component with Suspense (React 19)
- Use React.memo for FileCard components to prevent unnecessary re-renders
- Lazy load file thumbnails only when visible
- Implement debounced search

**Result:** Smooth scrolling even with 10,000+ files, reduced initial load time by 70%, improved user experience, no performance degradation.

**Takeaway:** Virtual scrolling is essential for large file lists - rendering only visible items dramatically improves performance. React 19's deferred values help defer expensive operations.

### Q: How would you handle file synchronization across devices?

**Answer (STAR Method):**

**Situation:** Users need real-time file synchronization across multiple devices with conflict resolution.

**Action:**

- Use WebSocket or Server-Sent Events for real-time updates
- Use React Query's `refetchInterval` for polling as fallback
- Implement conflict detection by comparing file versions
- Use `useOptimistic()` (React 19) for instant UI updates before server confirmation
- Show conflict resolution UI when conflicts detected
- Store sync state in Redux Toolkit for persistence
- Implement exponential backoff for failed sync operations

**Result:** Users see file changes in real-time, conflicts are resolved smoothly, improved user experience across devices.

**Takeaway:** Real-time synchronization with React 19's optimistic updates provides seamless multi-device experience.
