# Youtube - Low Level Design (LLD)

> **Project Type:** Full-Stack Web Application (MERN Stack)  
> **Tech Stack:** 
> - **Frontend:** React.js, TypeScript, React Router, Redux Toolkit, Axios, Material-UI, Video.js
> - **Backend:** Node.js, Express.js, MongoDB, Redis, Elasticsearch, JWT
> - **Services:** AWS S3, CloudFront CDN, FFmpeg (video processing)

---

## 3. Component Architecture

**Think of this as the building blocks - how components are organized and connected**

### Component Hierarchy (React.js)

```
App (Root Component - Entry Point)
├── Layout (Main Layout with Navigation)
│   ├── Header
│   │   ├── Logo
│   │   ├── SearchBar (with autocomplete)
│   │   ├── NavigationMenu
│   │   └── UserMenu (Upload, Profile, Sign out)
│   └── Main Content Area
│       ├── HomePage
│       │   ├── VideoGrid
│       │   │   └── VideoCard
│       │   │       ├── Thumbnail
│       │   │       ├── VideoTitle
│       │   │       ├── ChannelName
│       │   │       ├── ViewCount
│       │   │       └── UploadDate
│       │   └── Sidebar (Trending, Subscriptions)
│       ├── WatchPage
│       │   ├── VideoPlayer
│       │   │   ├── Video.js Player
│       │   │   ├── QualitySelector
│       │   │   ├── PlaybackControls
│       │   │   └── FullscreenButton
│       │   ├── VideoInfo
│       │   │   ├── VideoTitle
│       │   │   ├── ViewCount
│       │   │   ├── LikeDislikeButtons
│       │   │   ├── SubscribeButton
│       │   │   └── ShareButton
│       │   ├── VideoDescription
│       │   ├── CommentsSection
│       │   │   ├── CommentInput
│       │   │   └── CommentList
│       │   │       └── CommentItem
│       │   │           ├── UserAvatar
│       │   │           ├── CommentText
│       │   │           ├── LikeButton
│       │   │           └── ReplyButton
│       │   └── RelatedVideos
│       │       └── VideoCard
│       ├── SearchPage
│       │   ├── FilterBar (Upload date, Type, Duration, Features)
│       │   ├── SearchResults
│       │   │   └── VideoCard (with search highlights)
│       │   └── Pagination
│       ├── ChannelPage
│       │   ├── ChannelHeader
│       │   │   ├── ChannelBanner
│       │   │   ├── ChannelAvatar
│       │   │   ├── ChannelName
│       │   │   ├── SubscriberCount
│       │   │   └── SubscribeButton
│       │   ├── ChannelTabs (Videos, Playlists, About)
│       │   └── VideoGrid
│       ├── UploadPage
│       │   ├── UploadForm
│       │   │   ├── VideoUpload (drag & drop)
│       │   │   ├── TitleInput
│       │   │   ├── DescriptionTextarea
│       │   │   ├── TagsInput
│       │   │   ├── ThumbnailUpload
│       │   │   ├── PrivacySelector
│       │   │   └── PublishButton
│       │   └── UploadProgress
│       ├── PlaylistPage
│       │   ├── PlaylistHeader
│       │   ├── PlaylistVideos
│       │   │   └── PlaylistVideoItem
│       │   └── PlaylistActions
│       └── LibraryPage
│           ├── WatchHistory
│           ├── WatchLater
│           └── Playlists
└── ReduxProvider (Global State Management)
    └── Store
        ├── authSlice (User authentication state)
        ├── videoSlice (Videos data)
        ├── playlistSlice (Playlists data)
        ├── watchHistorySlice (Watch history)
        └── userSlice (User profile data)
```

---

## 4. Data Models

### Video Model
```typescript
interface Video {
  id: string;
  title: string;
  description: string;
  channelId: string;
  channelName: string;
  thumbnailUrl: string;
  videoUrl: string;        // CDN URL
  duration: number;        // in seconds
  views: number;
  likes: number;
  dislikes: number;
  tags: string[];
  category: string;
  privacy: 'public' | 'private' | 'unlisted';
  status: 'processing' | 'ready' | 'failed';
  uploadedAt: Date;
  publishedAt?: Date;
}
```

### Comment Model
```typescript
interface Comment {
  id: string;
  videoId: string;
  userId: string;
  userName: string;
  userAvatar: string;
  text: string;
  likes: number;
  replies: Comment[];      // Nested comments
  createdAt: Date;
}
```

### Playlist Model
```typescript
interface Playlist {
  id: string;
  userId: string;
  title: string;
  description: string;
  videos: string[];        // Array of video IDs
  privacy: 'public' | 'private';
  thumbnailUrl?: string;
  createdAt: Date;
}
```

---

## 5. Data APIs

**Note:** All API endpoints are implemented on the **backend (Node.js/Express)**, and the **frontend (React.js)** calls these APIs using Axios.

### Video APIs

**Backend Implementation:** Express.js routes handle video logic  
**Frontend Implementation:** React components call these APIs and display videos

#### GET /api/videos
- **URL:** `/api/videos?page=1&limit=20&category=gaming`
- **Method:** GET
- **Response:**
  ```json
  {
    "success": true,
    "data": {
      "videos": [/* Video objects */],
      "pagination": {/* pagination info */}
    }
  }
  ```

#### GET /api/videos/:id
- **URL:** `/api/videos/123`
- **Method:** GET
- **Response:**
  ```json
  {
    "success": true,
    "data": {
      "video": {/* Video object with full details */}
    }
  }
  ```

#### POST /api/videos/upload
- **URL:** `/api/videos/upload`
- **Method:** POST
- **Content-Type:** multipart/form-data
- **Request Body:**
  - `video` - Video file
  - `title` - Video title
  - `description` - Video description
  - `tags` - Comma-separated tags
  - `thumbnail` - Thumbnail image (optional)

#### GET /api/videos/search
- **URL:** `/api/videos/search?q=laptop&page=1`
- **Method:** GET
- **Description:** Search videos using Elasticsearch

---

## 6. Backend Implementation Details

### Video Upload and Processing

**Backend (Express.js):**
```typescript
// Backend: routes/videos.ts
import multer from 'multer';
import { S3Client, PutObjectCommand } from '@aws-sdk/client-s3';

const upload = multer({ storage: multer.memoryStorage() });

router.post('/upload', authenticate, upload.single('video'), async (req, res) => {
  const file = req.file;
  const { title, description, tags } = req.body;
  
  // Upload video to S3
  const s3Client = new S3Client({ region: 'us-east-1' });
  const videoKey = `videos/${req.user.id}/${Date.now()}-${file.originalname}`;
  
  await s3Client.send(new PutObjectCommand({
    Bucket: process.env.S3_BUCKET,
    Key: videoKey,
    Body: file.buffer,
    ContentType: file.mimetype
  }));
  
  const videoUrl = `https://${process.env.CLOUDFRONT_DOMAIN}/${videoKey}`;
  
  // Create video record in database
  const video = await Video.create({
    title,
    description,
    channelId: req.user.id,
    channelName: req.user.name,
    videoUrl,
    status: 'processing',
    uploadedAt: new Date()
  });
  
  // Queue video processing job
  await videoProcessingQueue.add({
    videoId: video.id,
    videoUrl,
    userId: req.user.id
  });
  
  res.json({ success: true, data: { video } });
});
```

### Video Processing Worker

**Backend (FFmpeg Worker):**
```typescript
// Backend: workers/videoProcessor.ts
import ffmpeg from 'fluent-ffmpeg';
import { S3Client, PutObjectCommand } from '@aws-sdk/client-s3';

async function processVideo(job: VideoProcessingJob) {
  const { videoId, videoUrl, userId } = job.data;
  
  // Download video from S3
  const videoBuffer = await downloadFromS3(videoUrl);
  
  // Generate multiple quality versions
  const qualities = ['360p', '720p', '1080p'];
  
  for (const quality of qualities) {
    const outputBuffer = await transcodeVideo(videoBuffer, quality);
    
    // Upload to S3
    const key = `videos/${userId}/${videoId}/${quality}.mp4`;
    await uploadToS3(key, outputBuffer);
  }
  
  // Generate thumbnail
  const thumbnailBuffer = await generateThumbnail(videoBuffer);
  const thumbnailKey = `thumbnails/${userId}/${videoId}.jpg`;
  await uploadToS3(thumbnailKey, thumbnailBuffer);
  
  // Update video status
  await Video.updateOne(
    { id: videoId },
    {
      status: 'ready',
      thumbnailUrl: `https://${process.env.CLOUDFRONT_DOMAIN}/${thumbnailKey}`,
      publishedAt: new Date()
    }
  );
}
```

---

## 7. Implementation Details

**Note:** Implementation details are split between frontend (React.js) and backend (Node.js/Express.js).

### Video Player Implementation

**Frontend (React.js):**
```typescript
// Frontend: components/VideoPlayer.tsx
import VideoPlayer from 'video.js';

const VideoPlayerComponent: React.FC<{ videoUrl: string }> = ({ videoUrl }) => {
  const playerRef = useRef<HTMLVideoElement>(null);
  
  useEffect(() => {
    if (playerRef.current) {
      const player = VideoPlayer(playerRef.current, {
        sources: [
          { src: `${videoUrl}?quality=1080p`, type: 'video/mp4', label: '1080p' },
          { src: `${videoUrl}?quality=720p`, type: 'video/mp4', label: '720p' },
          { src: `${videoUrl}?quality=360p`, type: 'video/mp4', label: '360p' }
        ],
        controls: true,
        responsive: true,
        fluid: true
      });
      
      return () => {
        player.dispose();
      };
    }
  }, [videoUrl]);
  
  return (
    <div data-vjs-player>
      <video ref={playerRef} className="video-js" />
    </div>
  );
};
```

### Video Search with Autocomplete

**Backend (Elasticsearch):**
```typescript
// Backend: services/searchService.ts
export class SearchService {
  async searchVideos(query: string, filters: SearchFilters) {
    const result = await elasticsearchClient.search({
      index: 'videos',
      body: {
        query: {
          bool: {
            must: [
              {
                multi_match: {
                  query,
                  fields: ['title^3', 'description^2', 'tags', 'channelName']
                }
              }
            ],
            filter: [
              { term: { privacy: 'public' } },
              { term: { status: 'ready' } }
            ]
          }
        },
        highlight: {
          fields: {
            title: {},
            description: {}
          }
        }
      }
    });
    
    return result.hits.hits.map(hit => ({
      ...hit._source,
      highlights: hit.highlight
    }));
  }
}
```

---

## 8. Performance Optimizations

**Frontend Optimizations:** React.js code splitting, lazy loading, video preloading  
**Backend Optimizations:** Database indexing, Redis caching, CDN for videos

### Video Streaming Optimization

- **Adaptive Bitrate Streaming:** Serve different quality versions based on network
- **CDN Delivery:** Serve videos from CloudFront CDN for global delivery
- **Video Preloading:** Preload next video in playlist
- **Thumbnail Optimization:** Lazy load thumbnails, use WebP format

