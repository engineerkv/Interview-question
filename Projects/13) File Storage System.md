# File Storage System

> **Project Type:** Full-Stack Web Application (MERN Stack)
> **Scale:** Handle 1B+ users, 100PB+ storage, file synchronization
> **Tech Stack:** React.js, Node.js, Express.js, MongoDB, AWS S3, CDN

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

## a) Requirements

### i) Functional Requirements

- File upload and download

- File versioning

- File synchronization across devices

- File sharing and permissions

- File search

- Folder organization

### ii) Non-Functional Requirements

- File upload < 10 seconds for 100MB files

- 99.9% availability

- Support files up to 10GB

- Efficient storage (deduplication)

---

## b) Scope and Priority

### Phase 1: MVP (Must Have) - Priority 1

- Core functionality

- Basic features

### Phase 2: Enhanced Features - Priority 2

- Additional capabilities

- Performance improvements

### Phase 2: Enhanced Features - Priority 2

- Advanced file sharing (public links, password protection)

- File collaboration (real-time editing)

- Advanced search (full-text search, filters)

- File preview and thumbnails

- Bandwidth optimization and compression

---

## c) Technology Choices

### Backend Framework

- **Node.js with Express.js** - Handle file uploads and metadata

### Storage

- **Object Storage (AWS S3)** - Store file chunks

- **Database** - Store file metadata and chunk references

### Additional Services

- **CDN** - Fast global file delivery

- **Deduplication Service** - Identify duplicate chunks

---

## d) Capacity Estimation

### Throughput Requirements

- **Total Users**: 1 billion users
- **Daily Active Users (DAU)**: 500 million users per day
- **Peak Traffic**: 3x average during peak hours (1.5 billion users per day)
- **Files Uploaded per Day**: 1 billion files
- **File Operations per Day**: 10 billion operations (upload, download, sync, share)
- **Read:Write Ratio**: 5:1 (downloading/viewing files vs uploading files)

**Calculations:**
- **Average Writes Per Second (WPS)**: 1B file uploads / 86,400 seconds ≈ 11,574 WPS
- **Peak WPS**: 11,574 × 3 = 34,722 WPS
- **Average Reads Per Second (RPS)**: 11,574 × 5 = 57,870 RPS
- **Peak RPS**: 57,870 × 3 = 173,610 RPS
- **Concurrent Active Uploads**: 10 million concurrent file uploads

### Storage Estimation

**Storage per File:**
- File chunks: Variable (average 10 MB per file)
- File metadata: 1 KB (id, userId, name, size, type, timestamps, version)
- Chunk references: 500 bytes (chunk IDs, order)
- **Total per File**: ~10.0015 MB average

**Storage Requirements:**
- **Files per Year**: 1B files/day × 365 = 365 billion files
- **File Storage**: 365B × 10 MB ≈ 3.65 EB per year (before deduplication)
- **With Deduplication (30% savings)**: 3.65 EB × 0.7 ≈ 2.555 EB per year
- **User Data**: 1B users × 5 KB ≈ 5 TB
- **Metadata Storage**: 365B files × 1.5 KB ≈ 547.5 TB/year
- **Total Storage**: ~2.555 EB (files) + 5 TB (users) + 547.5 TB (metadata) ≈ 2.555 EB/year

### Bandwidth Estimation

- **Average File Size**: 10 MB per file
- **Daily Bandwidth**: 1B uploads × 10 MB + 5B downloads × 10 MB = 60 PB/day
- **Peak Bandwidth**: 60 PB × 3 = 180 PB/day during peak hours
- **Average Bandwidth**: 60 PB / 86,400 seconds ≈ 694 TB/s
- **Peak Bandwidth**: 694 TB/s × 3 ≈ 2.08 PB/s

### Caching Estimation

Following the **80-20 rule** where 20% of files generate 80% of traffic:
- **Cache 20% of popular files**: 1B × 0.2 = 200M files
- **Cache memory required**: 200M × 10 MB = 2 PB (CDN edge cache)
- **Cache hit ratio**: 90% (only 10% of file requests hit origin)
- **Requests hitting Origin**: 57,870 × 0.10 ≈ 5,787 RPS (manageable with CDN)

### Infrastructure Sizing

- **API Servers**: 1,000-2,000 instances behind load balancer, each handling 50-100 RPS
- **File Upload Workers**: 500-1,000 instances for processing file uploads
- **Deduplication Service**: 100-200 instances for chunk deduplication
- **Message Queue**: RabbitMQ/Kafka cluster with 50-100 nodes for file processing
- **Database**: MongoDB cluster with 100-200 nodes for metadata storage and high read/write throughput
- **Cache Layer**: Redis cluster with 50-100 nodes for high availability and performance
- **Object Storage**: AWS S3 or similar with multiple regions for file chunks
- **CDN**: CloudFront/Cloudflare with edge locations globally for file delivery

---

## e) Architecture Overview

The system follows a cloud file storage architecture with chunking, deduplication, versioning, and distributed storage. Here's how the complete system works:

### Frontend Architecture

**Frontend Layers:**

1. **Presentation Layer (React Components)**
   - **UI Components**: Reusable components (FileCard, FolderCard, UploadProgress, ShareDialog)
   - **Feature Components**: FileBrowser, FileUploader, FileViewer, ShareManager, SearchBar
   - **Layout Components**: Header, Sidebar, Navigation, MainLayout
   - **Page Components**: HomePage, FilePage, SharePage, SettingsPage

2. **State Management Layer**
   - **Local State (useState)**: Component-specific UI state (selected files, upload progress, loading, errors)
   - **Server State (Redux Toolkit)**: Global state for files, folders, user, sharing
   - **API State (React Query)**: File data caching, refetching, optimistic updates

3. **File Upload Layer**
   - **Chunking**: Split large files into chunks for efficient upload
   - **Upload Progress**: Track upload progress per chunk
   - **Resume Upload**: Resume failed uploads from last successful chunk

4. **API Integration Layer**
   - **API Client**: Axios instance with interceptors for auth, error handling
   - **Redux Thunks**: Async actions for API operations (uploadFile, downloadFile, shareFile)
   - **Request/Response Transformation**: Data normalization and error handling

5. **Routing Layer (React Router)**
   - **Route Configuration**: Define routes and protected routes
   - **Navigation**: Programmatic and declarative navigation
   - **Route Guards**: Authentication and authorization checks

6. **Build & Deployment Layer**
   - **Build Process**: Webpack/Vite bundling with code splitting
   - **Static Assets**: Served from CDN (CloudFront/Cloudflare)
   - **Environment Configuration**: Environment-specific API endpoints and configs

**Frontend Request Flow:**

1. **User Interaction** → User uploads file, downloads file, or shares file
2. **State Update** → Redux action dispatched or React Query mutation triggered
3. **API Call** → Axios makes HTTP request to backend API
4. **File Upload** → Upload file chunks to object storage
5. **Response Handling** → Success/error state updates Redux store or React Query cache
6. **UI Update** → Components re-render with new data

### Backend Architecture

**Backend Layers:**

1. **API Gateway/Load Balancer** - Entry point for all HTTP requests
2. **API Server Layer** - Stateless servers handling HTTP requests
3. **File Processing Layer** - Workers for file chunking, deduplication, compression
4. **Deduplication Layer** - Service for identifying and storing duplicate chunks
5. **Application Service Layer** - Business logic and orchestration
6. **Cache Layer** - In-memory caching for performance
7. **Database Layer** - Persistent data storage for metadata
8. **Object Storage Layer** - Distributed object storage for file chunks
9. **CDN Layer** - Global content delivery network

### Complete Request Flow

**File Upload Flow:**
1. **Frontend**: User selects file to upload
2. **Chunking**: Split file into chunks (e.g., 5MB chunks)
3. **API Call**: POST request to upload API with file metadata
4. **Backend**: Create file record in database, generate chunk IDs
5. **Upload Chunks**: Upload chunks to object storage (S3) in parallel
6. **Deduplication**: Check if chunks already exist (hash-based)
7. **Metadata**: Store chunk references in database
8. **Response**: Return file ID and upload status
9. **Frontend**: Show upload completion and file in browser

**File Download Flow:**
1. **Frontend**: User clicks to download file
2. **API Call**: GET request to file API
3. **Backend**: Fetch file metadata and chunk references from database
4. **CDN Check**: Check if file is cached in CDN
5. **Chunk Retrieval**: Retrieve chunks from object storage
6. **Response**: Return file chunks or CDN URL
7. **Frontend**: Download file chunks and reassemble, or download from CDN

**File Synchronization Flow:**
1. **Frontend**: Client app checks for file changes
2. **API Call**: GET request to sync API with last sync timestamp
3. **Backend**: Query database for files changed since last sync
4. **Response**: Return list of changed files with metadata
5. **Frontend**: Download new/changed files, update local cache
6. **Conflict Resolution**: Handle conflicts if same file modified on multiple devices

**File Sharing Flow:**
1. **Frontend**: User shares file with another user
2. **API Call**: POST request to share API with file ID and permissions
3. **Backend**: Create share record in database
4. **Access Control**: Update access control list
5. **Notification**: Notify recipient of shared file
6. **Response**: Return share link or confirmation
7. **Frontend**: Show share confirmation

### Key Components

- **Frontend (React.js)**: Single-page application with file upload/download, component-based architecture, Redux for state management, chunk-based upload handling
- **CDN/Edge**: Global distribution of popular files, reduces latency and bandwidth costs
- **Load Balancer**: Distributes HTTP traffic across API servers, SSL/TLS termination
- **API Servers**: Stateless design for horizontal scaling, handle file operations, metadata management
- **File Processing Workers**: Workers for file chunking, deduplication, compression, thumbnail generation
- **Deduplication Service**: Hash-based deduplication, identify duplicate chunks, optimize storage
- **Application Services**: File Service, Share Service, Sync Service, Search Service
- **Cache Layer (Redis)**: In-memory cache for file metadata (20% of traffic), chunk hashes, access control
- **Database (MongoDB)**: Sharded across multiple nodes for horizontal scaling, stores file metadata, chunk references, sharing
- **Object Storage (AWS S3)**: Distributed object storage for file chunks, organized by chunk hash
- **CDN (CloudFront)**: Global CDN for file delivery, cache popular files at edge locations

---

# 3) Low Level Design (LLD)

---

## Component Architecture

### Service Components

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
│   ├── SearchBar (file search)
│   └── UserMenu (Profile, Settings, Sign out)
├── MainContent
│   ├── Sidebar
│   │   ├── FolderTree
│   │   │   └── FolderNode
│   │   ├── QuickAccess
│   │   └── StorageInfo
│   ├── FileBrowser
│   │   ├── BreadcrumbNavigation
│   │   ├── Toolbar
│   │   │   ├── UploadButton
│   │   │   ├── NewFolderButton
│   │   │   ├── ViewToggle (Grid/List)
│   │   │   └── SortOptions
│   │   ├── FileGrid/FileList
│   │   │   └── FileItem
│   │   │       ├── FileIcon
│   │   │       ├── FileName
│   │   │       ├── FileSize
│   │   │       ├── ModifiedDate
│   │   │       └── ContextMenu
│   │   │           ├── Download
│   │   │           ├── Share
│   │   │           ├── Rename
│   │   │           ├── Move
│   │   │           └── Delete
│   │   └── EmptyState
│   ├── UploadDialog
│   │   ├── FileDropzone
│   │   ├── UploadProgressList
│   │   │   └── UploadProgressItem
│   │   └── CloseButton
│   └── ShareDialog
│       ├── ShareLinkInput
│       ├── PermissionSelector
│       └── ShareButton
└── Footer
    └── StorageUsage
```

### Key React Components

**Frontend Implementation:**

```typescript
// File Browser Component
const FileBrowser: React.FC<{ folderId?: string }> = ({ folderId }) => {
  const [viewMode, setViewMode] = useState<'grid' | 'list'>('grid');
  const [sortBy, setSortBy] = useState<'name' | 'date' | 'size'>('name');
  const { data: files, isLoading } = useFiles(folderId, sortBy);

  const handleFileClick = (file: File) => {
    if (file.type === 'folder') {
      navigate(`/files/${file.id}`);
    } else {
      handleFileDownload(file);
    }
  };

  return (
    <div className="file-browser">
      <Toolbar 
        viewMode={viewMode}
        onViewModeChange={setViewMode}
        sortBy={sortBy}
        onSortChange={setSortBy}
      />
      {isLoading ? (
        <LoadingSpinner />
      ) : (
        <FileGrid 
          files={files}
          viewMode={viewMode}
          onFileClick={handleFileClick}
        />
      )}
    </div>
  );
};

// File Upload Component
const FileUploadDialog: React.FC = () => {
  const [files, setFiles] = useState<File[]>([]);
  const [uploadProgress, setUploadProgress] = useState<Record<string, number>>({});
  const uploadMutation = useUploadFiles();

  const handleDrop = (droppedFiles: File[]) => {
    setFiles(prev => [...prev, ...droppedFiles]);
};

  const handleUpload = async () => {
    files.forEach(file => {
      uploadMutation.mutate(
        { file, folderId: currentFolderId },
        {
          onUploadProgress: (progressEvent) => {
            const progress = Math.round(
              (progressEvent.loaded * 100) / progressEvent.total
            );
            setUploadProgress(prev => ({
              ...prev,
              [file.name]: progress
            }));
      }
        }
      );
    });
  };

  return (
    <div className="upload-dialog">
      <FileDropzone onDrop={handleDrop} />
      <div className="upload-list">
        {files.map(file => (
          <UploadProgressItem
            key={file.name}
            fileName={file.name}
            progress={uploadProgress[file.name] || 0}
          />
        ))}
      </div>
      <button onClick={handleUpload}>Upload Files</button>
    </div>
  );
};
```

### State Management

**State Management Strategy:**

- **Local State (useState)**: UI state (view mode, sort options, selected files, modals)
- **Component State**: Each component manages its own UI state
- **API State**: React Query or SWR for server state (file list, folder structure, file metadata) - caching, refetching, optimistic updates
- **Global State (Redux Toolkit)**: Current folder path, selected files, upload queue, user preferences

**Frontend Implementation:**

```typescript
// Using React Query for API state management
import { useQuery, useMutation, useQueryClient } from '@tanstack/react-query';

const useFiles = (folderId?: string, sortBy?: string) => {
  return useQuery({
    queryKey: ['files', folderId, sortBy],
    queryFn: async () => {
      const response = await axios.get('/api/v1/files', {
        params: { folderId, sortBy }
      });
      return response.data;
    },
    staleTime: 30 * 1000 // Cache for 30 seconds
  });
};

const useUploadFiles = () => {
  const queryClient = useQueryClient();
  
  return useMutation({
    mutationFn: async ({ file, folderId }: { file: File; folderId?: string }) => {
      const formData = new FormData();
      formData.append('file', file);
      if (folderId) formData.append('folderId', folderId);

      const response = await axios.post('/api/v1/files/upload', formData, {
        headers: { 'Content-Type': 'multipart/form-data' },
        onUploadProgress: (progressEvent) => {
          // Handle upload progress
        }
      });
      return response.data;
    },
    onSuccess: () => {
      // Invalidate files list
      queryClient.invalidateQueries({ queryKey: ['files'] });
    }
  });
};
```

### Component Interactions

**Data Flow:**

1. **File Browsing** → FileBrowser fetches files via React Query, displays FileItem components
2. **Folder Navigation** → User clicks folder, navigates to folder contents
3. **File Upload** → UploadDialog handles file selection and upload with progress tracking
4. **File Operations** → Context menu actions (download, share, delete) trigger API calls
5. **File Sync** → Changes sync across devices via WebSocket or polling

**Event Handling:**

- File drag-and-drop triggers upload dialog
- Folder clicks navigate to folder contents
- File clicks trigger download or preview
- Context menu actions update file state
- Real-time sync updates file list when changes occur

### UI/UX Considerations

- **Loading States**: Show skeleton loaders for file lists, progress bars for uploads
- **Error Handling**: Display user-friendly error messages with retry options
- **Validation**: Client-side validation for uploads (file size, type, name)
- **Responsive Design**: Mobile-friendly layout, touch-friendly file operations
- **Accessibility**: ARIA labels, keyboard navigation, screen reader support, keyboard shortcuts
- **Performance**: Virtual scrolling for large file lists, lazy loading for thumbnails, chunked uploads for large files

---

## Data Models

### Model Interface

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

### POST /api/v1/files/upload

- **URL:** `/api/v1/files/upload`

- **Method:** POST

- **Content-Type:** `multipart/form-data`

- **Request Body:**
  ```

  file: File
  folderId: string (optional)
  ```

- **Response:**
  ```json
  {
    "success": true,
    "data": {
      "fileId": "file_abc123",
      "fileName": "document.pdf",
      "fileSize": 1024000,
      "fileType": "application/pdf",
      "uploadUrl": "https://s3.amazonaws.com/bucket/file_abc123",
      "folderId": "folder_xyz789",
      "createdAt": "2024-01-15T10:30:00Z"
    }
  }
  ```

- **Status Codes:** 201 (Created), 400 (Validation Error), 413 (File Too Large)

### GET /api/v1/files/:fileId

- **URL:** `/api/v1/files/:fileId`

- **Method:** GET

- **Response:**
  ```json
  {
    "success": true,
    "data": {
      "fileId": "file_abc123",
      "fileName": "document.pdf",
      "fileSize": 1024000,
      "fileType": "application/pdf",
      "downloadUrl": "https://s3.amazonaws.com/bucket/file_abc123?signature=...",
      "previewUrl": "https://cdn.example.com/preview/file_abc123",
      "folderId": "folder_xyz789",
      "createdAt": "2024-01-15T10:30:00Z",
      "updatedAt": "2024-01-15T10:30:00Z"
    }
  }
  ```

- **Status Codes:** 200 (Success), 404 (Not Found)

### GET /api/v1/files/:fileId/download

- **URL:** `/api/v1/files/:fileId/download`

- **Method:** GET

- **Response:** Redirect to signed S3 URL or file stream

- **Status Codes:** 302 (Redirect), 404 (Not Found)

### DELETE /api/v1/files/:fileId

- **URL:** `/api/v1/files/:fileId`

- **Method:** DELETE

- **Response:**
  ```json
  {
    "success": true,
    "message": "File deleted successfully"
  }
  ```

- **Status Codes:** 200 (Success), 404 (Not Found)

### POST /api/v1/files/:fileId/move

- **URL:** `/api/v1/files/:fileId/move`

- **Method:** POST

- **Request Body:**
  ```json
  {
    "targetFolderId": "folder_new123"
  }
  ```

- **Response:**
  ```json
  {
    "success": true,
    "data": {
      "fileId": "file_abc123",
      "folderId": "folder_new123",
      "updatedAt": "2024-01-15T11:00:00Z"
    }
  }
  ```

- **Status Codes:** 200 (Success), 404 (Not Found)

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

### File Storage Service

```typescript
class FileStorageService {
  async uploadFile(file: Express.Multer.File, folderId?: string): Promise<File> {
    // Validate file
    // Upload to S3
    // Create file metadata
    // Return file record
  }

  async getFile(fileId: string): Promise<File> {
    // Get file metadata
    // Generate signed URL
    // Return file info
  }

  async deleteFile(fileId: string): Promise<void> {
    // Delete from S3
    // Delete metadata
  }
}

```

---

## File Upload Flow

1. Client splits file into chunks (5MB each)

2. Upload chunks in parallel

3. Server stores chunks in object storage (S3)

4. Create file metadata record

5. Link chunks to file

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

### File Upload with Chunking

**Frontend Implementation:** React component handles file chunking and parallel upload
**Backend Implementation:** Express.js service handles chunk uploads and file assembly

- **Strategy:** Chunk-based upload for large files - like uploading a video in parts, uploads chunks in parallel for faster uploads

- **Chunk Size:** 5MB per chunk - good balance between upload speed and memory usage

**Backend (Express.js):**

```typescript
// Backend: services/FileStorageService.ts
import AWS from 'aws-sdk';
import multer from 'multer';
import { v4 as uuidv4 } from 'uuid';

const s3 = new AWS.S3({
  accessKeyId: process.env.AWS_ACCESS_KEY_ID,
  secretAccessKey: process.env.AWS_SECRET_ACCESS_KEY,
  region: process.env.AWS_REGION
});

class FileStorageService {
  async uploadChunk(fileId: string, chunkNumber: number, chunk: Buffer): Promise<void> {
    const key = `chunks/${fileId}/${chunkNumber}`;

    await s3.putObject({
      Bucket: process.env.S3_BUCKET_NAME!,
      Key: key,
      Body: chunk,
      ContentType: 'application/octet-stream'
    }).promise();
  }

  async assembleFile(fileId: string, totalChunks: number, fileName: string): Promise<string> {
    const chunks: Buffer[] = [];

    // Download all chunks
    for (let i = 0; i < totalChunks; i++) {
      const key = `chunks/${fileId}/${i}`;
      const chunk = await s3.getObject({
        Bucket: process.env.S3_BUCKET_NAME!,
        Key: key
      }).promise();

      chunks.push(chunk.Body as Buffer);
    }

    // Assemble file
    const fileBuffer = Buffer.concat(chunks);

    // Upload complete file
    const fileKey = `files/${fileId}/${fileName}`;
    await s3.putObject({
      Bucket: process.env.S3_BUCKET_NAME!,
      Key: fileKey,
      Body: fileBuffer,
      ContentType: this.getContentType(fileName)
    }).promise();

    // Delete chunks
    for (let i = 0; i < totalChunks; i++) {
      await s3.deleteObject({
        Bucket: process.env.S3_BUCKET_NAME!,
        Key: `chunks/${fileId}/${i}`
      }).promise();
    }

    return fileKey;
  }

  async generateSignedUrl(fileKey: string, expiresIn: number = 3600): Promise<string> {
    return s3.getSignedUrl('getObject', {
      Bucket: process.env.S3_BUCKET_NAME!,
      Key: fileKey,
      Expires: expiresIn
    });
  }

  private getContentType(fileName: string): string {
    const ext = fileName.split('.').pop()?.toLowerCase();
    const contentTypes: Record<string, string> = {
      'pdf': 'application/pdf',
      'jpg': 'image/jpeg',
      'png': 'image/png',
      'mp4': 'video/mp4'
    };
    return contentTypes[ext || ''] || 'application/octet-stream';
  }
}

```

**Frontend Implementation:**

```typescript
// React component for chunked file upload
import { useState } from 'react';
import axios from 'axios';

const CHUNK_SIZE = 5 * 1024 * 1024; // 5MB

const FileUpload: React.FC = () => {
  const [uploadProgress, setUploadProgress] = useState(0);
  const [isUploading, setIsUploading] = useState(false);

  const uploadFile = async (file: File) => {
    setIsUploading(true);
    const fileId = uuidv4();
    const totalChunks = Math.ceil(file.size / CHUNK_SIZE);

    try {
      // Upload chunks in parallel
      const uploadPromises = [];

      for (let i = 0; i < totalChunks; i++) {
        const start = i * CHUNK_SIZE;
        const end = Math.min(start + CHUNK_SIZE, file.size);
        const chunk = file.slice(start, end);

        const formData = new FormData();
        formData.append('chunk', chunk);
        formData.append('fileId', fileId);
        formData.append('chunkNumber', i.toString());
        formData.append('totalChunks', totalChunks.toString());
        formData.append('fileName', file.name);

        uploadPromises.push(
          axios.post('/api/v1/files/upload-chunk', formData, {
            onUploadProgress: (progressEvent) => {
              const chunkProgress = (progressEvent.loaded / progressEvent.total) * 100;
              const overallProgress = ((i + chunkProgress / 100) / totalChunks) * 100;
              setUploadProgress(overallProgress);
            }
          })
        );
      }

      await Promise.all(uploadPromises);

      // Assemble file
      await axios.post('/api/v1/files/assemble', {
        fileId,
        fileName: file.name,
        totalChunks
      });

      setUploadProgress(100);
    } catch (error) {
      console.error('Upload failed:', error);
    } finally {
      setIsUploading(false);
    }
  };

  return (
    <div>
      <input
        type="file"
        onChange={(e) => {
          const file = e.target.files?.[0];
          if (file) uploadFile(file);
        }}
        disabled={isUploading}
      />
      {isUploading && (
        <div>
          <progress value={uploadProgress} max={100} />
          <span>{uploadProgress.toFixed(0)}%</span>
        </div>
      )}
    </div>
  );
};

```

### File Management and Metadata

**Frontend Implementation:** React component handles file browser and file operations
**Backend Implementation:** Express.js service manages file metadata and operations

- **Strategy:** Metadata stored in MongoDB, files in S3 - like Google Drive, metadata for fast queries, S3 for storage

- **File Operations:** Move, rename, delete operations update metadata and S3

**Backend (Express.js):**

```typescript
// Backend: controllers/FileController.ts
class FileController {
  async getFiles(req: Request, res: Response) {
    const { folderId, page = 1, limit = 50 } = req.query;

    const files = await File.find({ folderId: folderId || null })
      .skip((page - 1) * limit)
      .limit(parseInt(limit as string))
      .sort({ createdAt: -1 });

    res.json({
      success: true,
      data: { files }
    });
  }

  async moveFile(req: Request, res: Response) {
    const { fileId } = req.params;
    const { targetFolderId } = req.body;

    const file = await File.findByIdAndUpdate(
      fileId,
      { $set: { folderId: targetFolderId } },
      { new: true }
    );

    if (!file) {
      return res.status(404).json({ error: 'File not found' });
    }

    res.json({
      success: true,
      data: { file }
    });
  }

  async deleteFile(req: Request, res: Response) {
    const { fileId } = req.params;

    const file = await File.findById(fileId);
    if (!file) {
      return res.status(404).json({ error: 'File not found' });
    }

    // Delete from S3
    await s3.deleteObject({
      Bucket: process.env.S3_BUCKET_NAME!,
      Key: file.s3Key
    }).promise();

    // Delete metadata
    await File.findByIdAndDelete(fileId);

    res.json({
      success: true,
      message: 'File deleted successfully'
    });
  }
}

```

**Frontend Implementation:**

```typescript
// React component for file browser
import { useQuery, useMutation } from '@tanstack/react-query';

const FileBrowser: React.FC<{ folderId?: string }> = ({ folderId }) => {
  const { data: files, refetch } = useQuery({
    queryKey: ['files', folderId],
    queryFn: () => axios.get('/api/v1/files', { params: { folderId } })
      .then(res => res.data.data.files)
  });

  const moveFileMutation = useMutation({
    mutationFn: ({ fileId, targetFolderId }: { fileId: string; targetFolderId: string }) =>
      axios.post(`/api/v1/files/${fileId}/move`, { targetFolderId }),
    onSuccess: () => refetch()
  });

  const deleteFileMutation = useMutation({
    mutationFn: (fileId: string) =>
      axios.delete(`/api/v1/files/${fileId}`),
    onSuccess: () => refetch()
  });

  return (
    <div className="file-browser">
      {files?.map((file: File) => (
        <div key={file.fileId} className="file-item">
          <span>{file.fileName}</span>
          <button onClick={() => deleteFileMutation.mutate(file.fileId)}>Delete</button>
        </div>
      ))}
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
    return res.status(400).json({ error: 'Invalid file data', details: err.message });
  }

  if (err.message === 'File too large') {
    return res.status(413).json({ error: 'File size exceeds maximum limit' });
  }

  if (err.message === 'File not found') {
    return res.status(404).json({ error: 'File not found' });
  }

  if (err.name === 'S3Error') {
    return res.status(503).json({ error: 'Storage service unavailable. Please try again later.' });
  }

  res.status(500).json({ error: 'Internal server error' });
};

```

**Frontend Implementation:**

```typescript
// React error handling
axios.interceptors.response.use(
  (response) => response,
  (error) => {
    if (error.response?.status === 413) {
      toast.error('File is too large. Maximum size is 100MB.');
    } else if (error.response?.status === 404) {
      toast.error('File not found.');
    } else if (error.response?.status === 503) {
      toast.error('Storage service unavailable. Please try again later.');
    } else {
      toast.error('Upload failed. Please try again.');
    }
    return Promise.reject(error);
  }
);

```

**Error Scenarios:**

- **Upload Errors:** Handle network failures, S3 errors, chunk upload failures - retry failed chunks, resume upload from last successful chunk

- **File Size Errors:** Handle files exceeding size limits - validate before upload, show clear error messages

- **Storage Errors:** Handle S3 service unavailability - queue uploads, retry with exponential backoff

- **Metadata Errors:** Handle database failures during file operations - ensure consistency between S3 and database

---

## Testing Strategy

### Frontend Testing (React.js)

**Unit Testing:**

- **Jest + React Testing Library** - Test components, file upload, file browser

- **File Component Testing** - Test file upload, download, preview, folder navigation

- **Mocking:** Mock API calls, file operations, AWS S3

**Integration Testing:**

- **File Upload Flow** - Test complete file upload process

- **File Management** - Test file operations (rename, delete, move)

- **API Integration Tests** - Test API calls with mock server

**E2E Testing:**

- **Cypress / Playwright** - Test file storage flows

- **Test Scenarios:** Upload file, download file, organize files, share files

### Backend Testing (Node.js/Express.js)

**Unit Testing:**

- **Jest + Supertest** - Test API endpoints, file processing

- **S3 Integration Testing** - Test AWS S3 operations

- **Mocking:** Mock database, AWS S3, Redis

**Integration Testing:**

- **MongoDB Memory Server** - Test database operations

- **Redis Mock** - Test file metadata caching

- **S3 Mock** - Test S3 operations

**Load Testing:**

- **Artillery / k6** - Test file operations under high load

- **Concurrent Uploads:** Test performance with multiple simultaneous uploads

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

- **Nginx:** Load balancer and reverse proxy

- **Docker:** Containerized deployment

**CI/CD Pipeline:**

- **Automated Testing:** Run tests before deployment

- **Zero-Downtime:** Rolling deployment strategy

- **Health Checks:** Verify file storage endpoints

### Database Deployment

**MongoDB Setup:**

- **MongoDB Atlas** - Managed MongoDB service

- **Backup Strategy:** Daily automated backups

- **Indexing:** Proper indexes for file queries

**Redis Setup:**

- **Redis Cloud / AWS ElastiCache** - Managed Redis service

- **File Metadata Caching:** Cache file metadata

---

## Environment Configuration

### Environment Variables

**Frontend:**

```env
REACT_APP_API_URL=https://api.example.com
REACT_APP_S3_BUCKET_URL=https://bucket.s3.amazonaws.com
REACT_APP_ENVIRONMENT=production

```

**Backend:**

```env
NODE_ENV=production
PORT=3000
MONGODB_URI=mongodb://...
REDIS_URL=redis://...
AWS_ACCESS_KEY_ID=xxx
AWS_SECRET_ACCESS_KEY=xxx
AWS_S3_BUCKET=xxx
AWS_REGION=us-east-1

```

---

## Database Migrations & Seeding

### MongoDB Migrations

**Migration Scripts:**

- **Schema Changes:** Add indexes for file queries

- **Data Migrations:** Update file formats

- **Index Optimization:** Add compound indexes for file operations

### Data Seeding

**Seed Data:**

- **Test Files:** Seed test file metadata

- **Folders:** Seed test folder structure

- **User Accounts:** Seed test users

---

## API Documentation

### Swagger/OpenAPI

**API Documentation:**

- **Swagger UI:** Document REST APIs

- **File API:** Document file upload, download, management endpoints

- **S3 Integration:** Document S3 signed URL generation

---

## API Versioning

**Versioning Strategy:**

- **URL Versioning:** `/api/v1/files`, `/api/v2/files`

- **Header Versioning:** `Accept: application/vnd.api+json;version=1`

- **Backward Compatibility:** Maintain old API versions for existing clients

---

## Monitoring & Logging

### Application Monitoring

**Frontend:**

- **Error Tracking:** Sentry for file operation errors

- **Performance:** Track file upload/download times

- **User Analytics:** Track file storage usage

**Backend:**

- **APM:** Monitor file processing performance

- **S3 Monitoring:** Track S3 operation performance

- **File Metrics:** Track upload, download, storage usage

### Logging

**Structured Logging:**

- **Winston / Pino:** Log file operations

- **File Events:** Log upload, download, delete, share events

- **Error Logging:** Detailed error logs with context

---

## Database Transactions & Consistency

### MongoDB Transactions

**Transaction Usage:**

- **Multi-Document Transactions** - For operations requiring ACID guarantees

- **Example:** File creation + folder update + user quota update

- **Session Management:** Use MongoDB sessions for transaction control

**Example:**

```typescript
const session = await mongoose.startSession();
session.startTransaction();
try {
  await File.create([fileData], { session });
  await Folder.updateOne({ folderId }, { $inc: { fileCount: 1 } }, { session });
  await User.updateOne({ userId }, { $inc: { storageUsed: fileSize } }, { session });
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

- **File Consistency:** Use transactions for file operations

- **Storage Quota Consistency:** Ensure quota updates are atomic

- **Metadata Consistency:** Keep file metadata in sync with S3

---

## Third-Party Service Integration

### AWS S3 Integration

**File Storage:**

- **File Upload:** Upload files to S3 with proper access control

- **File Download:** Generate signed URLs for secure file access

- **File Management:** Delete, copy, move files in S3

- **Lifecycle Policies:** Configure S3 lifecycle policies for cost optimization

### CDN Integration

**Content Delivery:**

- **CloudFront:** Serve files through CloudFront CDN

- **Cache Configuration:** Configure cache headers

- **Geographic Distribution:** Global CDN for fast file access

### Redis Integration

**Caching:**

- **File Metadata Caching:** Cache file metadata

- **Signed URL Caching:** Cache signed URLs for frequently accessed files

- **Rate Limiting:** Use Redis for rate limiting

---

# 3) Interview Answers

---

## Q1. Designing a file storage system

**Situation:** Need to design a file storage system for 1B+ users with 100PB+ storage, supporting file upload, download, synchronization, and sharing.

**Action:** I designed a file storage system:

- **Chunking:** Split large files into 5MB chunks for efficient upload and storage

- **Object Storage:** Use S3/object storage for chunk storage (scalable, durable)

- **Deduplication:** Store file chunks once, reference multiple times (saves storage)

- **Versioning:** Store file versions as delta changes (only store differences)

- **Metadata Database:** Store file metadata (name, size, chunks, versions) in database

- **CDN:** Use CDN for fast file download globally

- **Sync Service:** Track file changes, sync across devices using change logs

- **Sharing:** Implement access control lists (ACL) for file sharing

**Result:** System handles 1B+ users with 100PB+ storage. Deduplication saves 40% storage. File upload completes in < 10 seconds for 100MB files.

**Takeaway:** Chunking enables efficient upload and deduplication. Object storage provides scalability. Versioning with deltas saves storage.

---

## Q2. Implementing file deduplication

**Situation:** Multiple users upload same file, need to store only once to save storage.

**Action:** I implemented deduplication:

- **Chunk Hashing:** Calculate SHA-256 hash for each file chunk

- **Hash Index:** Store hash → chunk mapping in database

- **Duplicate Detection:** Check if chunk hash exists before storing

- **Reference Counting:** Track how many files reference each chunk

- **Chunk Reuse:** If chunk exists, reuse instead of storing again

- **Cleanup:** Delete chunks with zero references

**Result:** Deduplication saves 40% storage space. File upload faster for duplicate files (no upload needed).

**Takeaway:** Content-based hashing enables deduplication. Reference counting prevents premature deletion.

---

## Q3. Handling file synchronization across devices

**Situation:** User edits file on device A, changes should sync to device B automatically.

**Action:** I implemented file synchronization:

- **Change Tracking:** Track file changes (create, update, delete) with timestamps

- **Change Log:** Maintain change log per user/device

- **Sync Protocol:** Client requests changes since last sync timestamp

- **Conflict Resolution:** Handle conflicts when same file edited on multiple devices

- **Delta Sync:** Only sync changed chunks, not entire file

- **Background Sync:** Sync changes in background without user intervention

**Result:** File changes sync across devices in < 5 seconds. Delta sync reduces bandwidth by 80%. Conflict resolution works smoothly.

**Takeaway:** Change logs enable efficient synchronization. Delta sync reduces bandwidth usage.
