# Time-Limited Content System

> **Project Type:** Full-Stack Web Application (MERN Stack)
> **Scale:** Handle 1B+ users, 500M+ content items per day, configurable expiration duration
> **Tech Stack:** React.js, Node.js, Express.js, MongoDB, Redis, CDN

# 1) Problem Statement

Design and implement a time-limited content system that addresses the following challenges:

- **Core Functionality**: Enable users to create time-limited content (images, videos, stories) that automatically expires after a configurable duration (e.g., 24 hours), with view tracking and engagement features
- **Scale Requirements**: Handle 1B+ users, 500M+ content items per day, millions of concurrent viewers, and viral content scenarios
- **Performance**: Content upload < 5 seconds, content viewing latency < 2 seconds, fast content discovery and feed loading
- **Automatic Expiration**: Reliable content expiration at the configured time, automatic cleanup of expired content from storage, prevent access to expired content
- **Content Management**: Support multiple content types (images, videos, stories), configurable expiration duration, content metadata management
- **User Engagement**: Real-time view tracking, content reactions (likes, replies), view analytics, engagement metrics
- **Storage Optimization**: Efficient cleanup of expired media files, optimize storage costs, handle storage lifecycle management
- **Data Consistency**: Ensure content is accessible only during its active period, handle expiration reliably across distributed systems, maintain view tracking accuracy

---

# 2) High Level Design (HLD)

## a) Requirements

### i) Functional Requirements

- Users can create time-limited content (photos/videos)

- Content expires after configurable duration (e.g., 24 hours)

- Users can view content from followed users

- Content views tracking

- Content reactions (likes, replies)

### ii) Non-Functional Requirements

- Content upload < 5 seconds

- Content viewing latency < 2 seconds

- Automatic expiration after configured duration

- Handle viral content

---

## b) Scope and Priority

### Phase 1: MVP (Must Have) - Priority 1

- Core functionality

- Basic features

### Phase 2: Enhanced Features - Priority 2

- Additional capabilities

- Performance improvements

### Phase 2: Enhanced Features - Priority 2

- Content reactions (likes, replies)

- View analytics and engagement metrics

- Content discovery and recommendations

- Advanced expiration policies (custom durations, scheduled expiration)

---

## c) Technology Choices

### Backend Framework

- **Node.js with Express.js** - Fast, scalable backend for handling content creation and expiration

### Database

- **MongoDB** - Document database with TTL indexes for automatic content expiration

- **Redis** - In-memory cache for active content and view tracking

### Storage

- **Object Storage (AWS S3)** - Store media files (images, videos)

- **CDN** - Fast global delivery of content media

### Background Jobs

- **Cron Jobs / Queue Workers** - Scheduled cleanup of expired content

---

## d) Capacity Estimation

### Throughput Requirements

- **Total Users**: 1 billion users
- **Daily Active Users (DAU)**: 500 million users per day
- **Peak Traffic**: 3x average during peak hours (1.5 billion users per day)
- **Content Items per Day**: 500 million content items
- **Average Content Size**: 5 MB (images/videos)
- **Read:Write Ratio**: 20:1 (viewing content vs creating content)

**Calculations:**
- **Average Writes Per Second (WPS)**: 500M content items / 86,400 seconds ≈ 5,787 WPS
- **Peak WPS**: 5,787 × 3 = 17,361 WPS
- **Average Reads Per Second (RPS)**: 5,787 × 20 = 115,740 RPS
- **Peak RPS**: 115,740 × 3 = 347,220 RPS
- **Concurrent Viewers**: 50 million concurrent content viewers

### Storage Estimation

**Storage per Content Item:**
- Media file: 5 MB average (image/video)
- Metadata: 1 KB (id, userId, expiration, timestamps)
- **Total per Content Item**: 5.001 MB

**Storage Requirements:**
- **Content Items per Year**: 500M content items/day × 365 = 182.5 billion content items
- **Active Content Storage**: 500M active items × 5.001 MB ≈ 2.5 PB (at any given time, assuming 24-hour expiration)
- **User Data**: 1B users × 5 KB ≈ 5 TB
- **View Tracking**: 500M items/day × 100 views/item × 100 bytes ≈ 5 TB/day
- **Total Storage**: ~2.5 PB (active content) + 5 TB (users) + 5 TB/day (view tracking) ≈ 2.5 PB + 1.8 TB/year

### Bandwidth Estimation

- **Average Content Bandwidth**: 5 MB per content view
- **Daily Bandwidth**: 500M items × 100 views/item × 5 MB = 250,000 TB/day
- **Peak Bandwidth**: 250,000 TB × 3 = 750,000 TB/day during peak hours
- **Average Bandwidth**: 250,000 TB / 86,400 seconds ≈ 2.9 PB/s
- **Peak Bandwidth**: 2.9 PB/s × 3 ≈ 8.7 PB/s

### Caching Estimation

Following the **80-20 rule** where 20% of content generates 80% of traffic:
- **Cache 20% of active content**: 500M × 0.2 = 100M content items
- **Cache memory required**: 100M × 5 MB = 500 TB (CDN edge cache)
- **Cache hit ratio**: 90% (only 10% of content requests hit origin)
- **Requests hitting Origin**: 115,740 × 0.10 ≈ 11,574 RPS (manageable with CDN)

### Infrastructure Sizing

- **API Servers**: 500-1,000 instances behind load balancer, each handling 200-500 RPS
- **Content Processing Workers**: 50-100 instances for media processing, each handling 2-5 items concurrently
- **Expiration Workers**: 20-50 instances for content expiration and cleanup
- **Database**: MongoDB cluster with 100-200 nodes for storage and high read/write throughput
- **Cache Layer**: Redis cluster with 50-100 nodes for high availability and performance
- **Storage**: AWS S3 or similar object storage for media files with lifecycle policies
- **CDN**: CloudFront/Cloudflare with edge locations globally for content delivery

---

## e) Architecture Overview

```

┌─────────────┐
│   Client    │
└──────┬──────┘
       │
       ▼
┌─────────────────┐
│  Load Balancer  │
└──────┬──────────┘
       │
   ┌───┴───┐
   ▼       ▼
┌──────┐ ┌──────┐
│Server│ │Server│
└──┬───┘ └──┬───┘
   │        │
   └───┬────┘
       ▼
┌─────────────────┐
│  Database       │
└─────────────────┘

```

---

## Key Design Decisions

1. **TTL Storage:** Use TTL in database for automatic expiration

2. **CDN:** Use CDN for content media delivery

3. **Caching:** Cache active content in Redis

4. **Background Jobs:** Cleanup expired content on schedule

---

# 2) Low Level Design (LLD)

---

## Component Architecture

### Content Service

```typescript
class ContentService {
  async createContent(userId: string, mediaUrl: string, duration: number): Promise<Content> {
    // Create content with expiration time
    // Store in database with TTL
    // Return content ID
  }

  async getContent(contentId: string): Promise<Content | null> {
    // Check if content exists and not expired
    // Track view
    // Return content
  }

  async deleteExpiredContent(): Promise<void> {
    // Background job to cleanup expired content
  }
}

```

### View Tracking Service

```typescript
class ViewTrackingService {
  async trackView(contentId: string, userId: string): Promise<void> {
    // Track who viewed the content
    // Store in Redis for fast access
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
│   ├── Navigation
│   └── UserMenu (Profile, Settings, Sign out)
├── MainContent
│   ├── ContentFeedPage
│   │   ├── ContentFeed
│   │   │   └── ContentCard
│   │   │       ├── UserInfo
│   │   │       ├── MediaDisplay
│   │   │       │   ├── Image/Video
│   │   │       │   └── ExpirationCountdown
│   │   │       ├── ViewCount
│   │   │       ├── ReactionButtons
│   │   │       │   ├── LikeButton
│   │   │       │   └── ReplyButton
│   │   │       └── ReactionCount
│   │   └── InfiniteScrollTrigger
│   ├── ContentCreationPage
│   │   ├── MediaUpload
│   │   │   ├── FileDropzone
│   │   │   ├── MediaPreview
│   │   │   └── UploadProgress
│   │   ├── DurationSelector
│   │   │   ├── DurationOptions (1h, 6h, 12h, 24h)
│   │   │   └── CustomDuration
│   │   └── PublishButton
│   └── ContentDetailPage
│       ├── MediaDisplay
│       ├── ExpirationCountdown
│       ├── ViewCount
│       ├── ReactionsList
│       └── ReplySection
└── Footer
```

### Key React Components

**Frontend Implementation:**

```typescript
// Content Card Component
const ContentCard: React.FC<{ content: Content }> = ({ content }) => {
  const [timeRemaining, setTimeRemaining] = useState(calculateTimeRemaining(content.expiresAt));
  const { mutate: likeContent } = useLikeContent();

  useEffect(() => {
    const interval = setInterval(() => {
      setTimeRemaining(calculateTimeRemaining(content.expiresAt));
    }, 1000);
    return () => clearInterval(interval);
  }, [content.expiresAt]);

  const handleLike = () => {
    likeContent(content.contentId);
  };

  return (
    <div className="content-card">
      <UserInfo user={content.user} />
      <MediaDisplay 
        mediaUrl={content.mediaUrl} 
        mediaType={content.mediaType}
      />
      <ExpirationCountdown timeRemaining={timeRemaining} />
      <div className="content-stats">
        <ViewCount count={content.viewCount} />
        <ReactionCount count={content.reactions.length} />
      </div>
      <ReactionButtons
        onLike={handleLike}
        onReply={() => navigate(`/content/${content.contentId}`)}
      />
    </div>
  );
};

// Content Creation Component
const ContentCreationPage: React.FC = () => {
  const [file, setFile] = useState<File | null>(null);
  const [duration, setDuration] = useState(24); // hours
  const [uploadProgress, setUploadProgress] = useState(0);
  const createContentMutation = useCreateContent();

  const handleFileSelect = (selectedFile: File) => {
    setFile(selectedFile);
  };

  const handlePublish = async () => {
    if (!file) return;

    const formData = new FormData();
    formData.append('media', file);
    formData.append('duration', duration.toString());

    createContentMutation.mutate(formData, {
      onUploadProgress: (progressEvent) => {
        const progress = Math.round(
          (progressEvent.loaded * 100) / progressEvent.total
        );
        setUploadProgress(progress);
      }
    });
  };

  return (
    <div className="content-creation">
      <MediaUpload 
        file={file}
        onFileSelect={handleFileSelect}
        progress={uploadProgress}
      />
      <DurationSelector
        duration={duration}
        onDurationChange={setDuration}
      />
      <button 
        onClick={handlePublish} 
        disabled={!file || createContentMutation.isLoading}
      >
        {createContentMutation.isLoading ? 'Publishing...' : 'Publish'}
      </button>
    </div>
  );
};
```

### ii) State Management

**State Management Strategy:**

- **Local State (useState)**: File selection, duration, UI state (loading, errors, modals)
- **Component State**: Each component manages its own UI state
- **API State**: React Query or SWR for server state (content feed, content details) - caching, refetching, optimistic updates
- **Global State (Redux Toolkit)**: User authentication, followed users, content feed

**Frontend Implementation:**

```typescript
// Using React Query for API state management
import { useQuery, useMutation, useQueryClient } from '@tanstack/react-query';

const useContentFeed = () => {
  return useInfiniteQuery({
    queryKey: ['content-feed'],
    queryFn: async ({ pageParam = 0 }) => {
      const response = await axios.get('/api/v1/content/feed', {
        params: { offset: pageParam, limit: 20 }
      });
      return response.data;
    },
    getNextPageParam: (lastPage, pages) => {
      return lastPage.hasMore ? pages.length * 20 : undefined;
    }
  });
};

const useCreateContent = () => {
  const queryClient = useQueryClient();
  
  return useMutation({
    mutationFn: async (formData: FormData) => {
      const response = await axios.post('/api/v1/content', formData, {
        headers: { 'Content-Type': 'multipart/form-data' },
        onUploadProgress: (progressEvent) => {
          // Handle upload progress
        }
      });
      return response.data;
    },
    onSuccess: () => {
      // Invalidate feed to show new content
      queryClient.invalidateQueries({ queryKey: ['content-feed'] });
    }
  });
};
```

### Component Interactions

**Data Flow:**

1. **Content Feed** → ContentFeedPage fetches content via React Query infinite query, displays ContentCard components
2. **Content Creation** → User uploads media, selects duration, publishes content
3. **Expiration Countdown** → Timer updates every second, shows time remaining
4. **Reactions** → User likes/replies, optimistically updates UI
5. **View Tracking** → Content views tracked when content is displayed

**Event Handling:**

- Media upload tracks progress and updates UI
- Expiration countdown updates every second
- Like/reply actions update optimistically
- Infinite scroll loads more content automatically
- Real-time updates via WebSocket for new content from followed users

### UI/UX Considerations

- **Loading States**: Show skeleton loaders for content feed, progress bars for uploads
- **Error Handling**: Display user-friendly error messages with retry options
- **Validation**: Client-side validation for file size, type, duration
- **Responsive Design**: Mobile-first layout, optimized for vertical scrolling
- **Accessibility**: ARIA labels, keyboard navigation, screen reader support
- **Performance**: Virtual scrolling for long feeds, lazy loading for media, image compression before upload

---

## Data Models

### Content Model

```typescript
interface Content {
  contentId: string;
  userId: string;
  mediaUrl: string;
  mediaType: 'image' | 'video';
  createdAt: Date;
  expiresAt: Date;  // TTL index for automatic deletion
  viewCount: number;
  reactions: Reaction[];
}

```

### Reaction Model

```typescript
interface Reaction {
  userId: string;
  type: 'like' | 'reply';
  createdAt: Date;
}

```

## Data APIs

### POST /api/v1/content

- **URL:** `/api/v1/content`

- **Method:** POST

- **Request Body (multipart/form-data):**
  ```json
  {
    "media": "file",
    "durationHours": 24,
    "caption": "Optional caption"
  }
  ```

- **Response:**
  ```json
  {
    "success": true,
    "data": {
      "contentId": "content_abc123",
      "mediaUrl": "https://cdn.example.com/content_abc123.jpg",
      "expiresAt": "2024-01-16T10:30:00Z",
      "durationHours": 24
    }
  }
  ```

- **Status Codes:** 201 (Created), 400 (Validation Error), 401 (Unauthorized)

### GET /api/v1/content/:contentId

- **URL:** `/api/v1/content/:contentId`

- **Method:** GET

- **Response:**
  ```json
  {
    "success": true,
    "data": {
      "contentId": "content_abc123",
      "userId": "user123",
      "mediaUrl": "https://cdn.example.com/content_abc123.jpg",
      "mediaType": "image",
      "createdAt": "2024-01-15T10:30:00Z",
      "expiresAt": "2024-01-16T10:30:00Z",
      "viewCount": 150,
      "reactions": [
        { "userId": "user456", "type": "like", "createdAt": "2024-01-15T11:00:00Z" }
      ]
    }
  }
  ```

- **Status Codes:** 200 (Success), 404 (Not Found), 410 (Gone - Expired)

### GET /api/v1/content/user/:userId

- **URL:** `/api/v1/content/user/:userId`

- **Method:** GET

- **Query Parameters:**
  - `limit`: number (default: 20, max: 50)
  - `before`: contentId (for pagination)

- **Response:**
  ```json
  {
    "success": true,
    "data": {
      "content": [
        {
          "contentId": "content_abc123",
          "mediaUrl": "https://cdn.example.com/content_abc123.jpg",
          "expiresAt": "2024-01-16T10:30:00Z",
          "viewCount": 150
        }
      ],
      "hasMore": true,
      "nextCursor": "content_xyz789"
    }
  }
  ```

- **Status Codes:** 200 (Success)

### POST /api/v1/content/:contentId/reactions

- **URL:** `/api/v1/content/:contentId/reactions`

- **Method:** POST

- **Request Body:**
  ```json
  {
    "type": "like"
  }
  ```

- **Response:**
  ```json
  {
    "success": true,
    "data": {
      "reactionId": "reaction_abc123",
      "contentId": "content_abc123",
      "userId": "user123",
      "type": "like",
      "createdAt": "2024-01-15T11:00:00Z"
    }
  }
  ```

- **Status Codes:** 201 (Created), 404 (Not Found), 410 (Gone - Expired)

### iii) Implementation Details

**Content Upload Implementation:**
- Multipart upload to S3 with progress tracking
- Set expiration duration and calculate expiration timestamp
- Create content record in MongoDB with TTL index
- Process media (resize, optimize) if needed
- Return content ID and CDN URL

**Content Viewing Implementation:**
- Check if content exists and not expired (TTL check)
- Track view in Redis and database
- Serve content from CDN with expiration countdown
- Handle expired content gracefully

**Expiration Timer Implementation:**
- Real-time countdown timer showing time remaining
- Update timer every second
- Hide/disable content when expired
- Show expiration message

---

## b) Backend

### i) Services

**Content Service:**

```typescript
export class ContentService {
  async createContent(userId: string, mediaFile: File, durationHours: number): Promise<Content> {
    // Upload media to S3
    const mediaKey = `content/${userId}/${Date.now()}-${mediaFile.name}`;
    await this.s3Client.upload(mediaFile, mediaKey);
    
    // Calculate expiration time
    const expiresAt = new Date(Date.now() + durationHours * 60 * 60 * 1000);
    
    // Create content record with TTL
    const content = await Content.create({
      userId,
      mediaUrl: this.getCDNUrl(mediaKey),
      expiresAt,
      viewCount: 0,
      reactions: []
    });

    // Set TTL in Redis for fast expiration check
    await redis.setex(`content:${content.contentId}`, durationHours * 3600, 'active');

    return content;
  }

  async getContent(contentId: string) {
    // Check Redis first
    const exists = await redis.exists(`content:${contentId}`);
    if (!exists) {
      throw new Error('Content expired or not found');
    }

    // Query database
    const content = await ContentModel.findOne({ contentId, expiresAt: { $gt: new Date() } });
    return content;
  }
}

```

---

- **Response:** `{ "content": [...], "hasMore": true }`

---

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

### Content Expiration

**TTL Implementation:**

- MongoDB TTL index on `expiresAt` field for automatic deletion

- Redis TTL for fast expiration checks

- Background job runs every hour to cleanup any remaining expired content

### View Tracking

**Implementation:**

- Track views in Redis for fast access

- Batch write to database every 5 minutes

- Prevent duplicate views from same user

### Error Handling

**Error Scenarios:**

- Content expired: Return 404 with "Content expired" message

- Content not found: Return 404

- Invalid duration: Return 400 validation error

- Media upload failure: Return 500 with retry mechanism

---

## Testing Strategy

### Frontend Testing (React.js)

**Unit Testing:**

- **Jest + React Testing Library** - Test components, content viewer, expiration timer

- **Content Component Testing** - Test content display, countdown timer, expiration handling

- **Mocking:** Mock API calls, time-based functions

**Integration Testing:**

- **Content Upload Flow** - Test complete content upload process

- **Expiration Handling** - Test content expiration and removal

- **API Integration Tests** - Test API calls with mock server

**E2E Testing:**

- **Cypress / Playwright** - Test content viewing and expiration flows

- **Test Scenarios:** Upload content, view content, verify expiration, handle expired content

### Backend Testing (Node.js/Express.js)

**Unit Testing:**

- **Jest + Supertest** - Test API endpoints, expiration logic

- **TTL Testing** - Test MongoDB TTL index functionality

- **Mocking:** Mock database, Redis, CDN

**Integration Testing:**

- **MongoDB Memory Server** - Test database operations with TTL

- **Redis Mock** - Test caching logic

- **Expiration Service Tests** - Test content expiration service

**Load Testing:**

- **Artillery / k6** - Test content serving under high load

- **Expiration Performance** - Test expiration handling performance

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

- **Health Checks:** Verify content endpoints

### Database Deployment

**MongoDB Setup:**

- **MongoDB Atlas** - Managed MongoDB service

- **TTL Index Configuration** - Configure TTL indexes for automatic expiration

- **Backup Strategy:** Daily automated backups

**Redis Setup:**

- **Redis Cloud / AWS ElastiCache** - Managed Redis service

- **Caching:** Cache content metadata

---

## Environment Configuration

### Environment Variables

**Frontend:**

```env
REACT_APP_API_URL=https://api.example.com
REACT_APP_CDN_URL=https://cdn.example.com
REACT_APP_ENVIRONMENT=production

```

**Backend:**

```env
NODE_ENV=production
PORT=3000
MONGODB_URI=mongodb://...
REDIS_URL=redis://...
CDN_URL=https://cdn.example.com

```

---

## Database Migrations & Seeding

### MongoDB Migrations

**Migration Scripts:**

- **Schema Changes:** Add TTL indexes for content expiration

- **Data Migrations:** Update content formats

- **Index Optimization:** Add compound indexes for content queries

### Data Seeding

**Seed Data:**

- **Test Content:** Seed test content with various expiration times

- **User Accounts:** Seed test users

---

## API Documentation

### Swagger/OpenAPI

**API Documentation:**

- **Swagger UI:** Document REST APIs

- **Content API:** Document content upload and retrieval endpoints

- **Expiration API:** Document expiration handling

---

## API Versioning

**Versioning Strategy:**

- **URL Versioning:** `/api/v1/content`, `/api/v2/content`

- **Header Versioning:** `Accept: application/vnd.api+json;version=1`

- **Backward Compatibility:** Maintain old API versions for existing clients

---

## Monitoring & Logging

### Application Monitoring

**Frontend:**

- **Error Tracking:** Sentry for content errors

- **Performance:** Track content loading times

- **User Analytics:** Track content viewing patterns

**Backend:**

- **APM:** Monitor content serving performance

- **Expiration Monitoring:** Track content expiration events

- **Content Metrics:** Track upload, view, expiration counts

### Logging

**Structured Logging:**

- **Winston / Pino:** Log content operations

- **Content Events:** Log upload, view, expiration events

- **Error Logging:** Detailed error logs with context

---

## Database Transactions & Consistency

### MongoDB Transactions

**Transaction Usage:**

- **Multi-Document Transactions** - For operations requiring ACID guarantees

- **Example:** Content creation + metadata update + CDN upload

- **Session Management:** Use MongoDB sessions for transaction control

**Example:**

```typescript
const session = await mongoose.startSession();
session.startTransaction();
try {
  await Content.create([contentData], { session });
  await User.updateOne({ userId }, { $inc: { contentCount: 1 } }, { session });
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

- **Content Consistency:** Use transactions for content operations

- **Expiration Consistency:** Ensure TTL indexes work correctly

- **Cache Consistency:** Invalidate cache on content expiration

---

## Third-Party Service Integration

### CDN Integration

**Content Delivery:**

- **Content Serving:** Serve content from CDN

- **Cache Configuration:** Configure cache headers for expiration

- **Geographic Distribution:** Global CDN for low latency

### Redis Integration

**Caching:**

- **Content Metadata Caching:** Cache content metadata

- **Expiration Tracking:** Track content expiration in Redis

- **Rate Limiting:** Use Redis for rate limiting

---

# 3) Interview Answers

---

## Q1. Designing a time-limited content system

**Situation:** Need to design a time-limited content system for 1B+ users where content expires after a set duration (e.g., 24 hours), handling 500M+ content items per day.

**Action:** **Backend (Node.js/Express.js):** I designed a time-limited content system using MongoDB TTL index on the expiresAt field for automatic content expiration. I integrated CDN (CloudFront) for fast content media delivery globally. I implemented Redis caching for active content with configurable TTL. I created scheduled cleanup jobs using node-cron to remove expired content from storage. I built a content feed service that generates feeds from followed users and filters expired content. I implemented view tracking in a separate collection that updates in real-time. I added media processing to optimize content (compression, thumbnails). **Frontend (React.js):** I built a content creation interface with media upload, duration selection, and preview. I created a content feed showing active content with expiration countdown timers. I implemented view tracking and reaction features with real-time updates.

**Result:** System handles 1B+ users with content upload < 5 seconds. Automatic expiration works reliably. 99.9% of expired content cleaned up within 1 hour. User engagement increased by 40% with expiration countdown timers.

**Takeaway:** TTL storage simplifies expiration logic. CDN is essential for fast media delivery. Expiration countdowns create urgency and increase engagement.

---

## Q2. Handling content expiration

**Situation:** Content must expire exactly after the configured duration (e.g., 24 hours) after creation.

**Action:** **Backend (Node.js/Express.js):** I implemented content expiration using MongoDB TTL index on the `expiresAt` field for automatic deletion. I created scheduled background jobs using node-cron to remove expired content from storage. I implemented feed filtering that excludes expired content when generating content feeds. I invalidate expired content from Redis cache when detected. I built a media cleanup service that deletes content media files from CDN/storage after expiration. **Frontend (React.js):** I display expiration countdown timers on all content items. I show expiration warnings when content is about to expire. I hide expired content from feeds automatically. I provide clear messaging when users try to access expired content.

**Result:** 99.9% of content expires correctly. Cleanup jobs run efficiently without impacting performance. CDN storage is cleaned up efficiently, reducing storage costs by 60%. User notifications increased engagement by 25%.

**Takeaway:** Database TTL provides automatic expiration. Background jobs ensure complete cleanup. User notifications improve engagement.

---

## Q3. Implementing media upload and CDN integration

**Situation:** Users need to upload images/videos that are stored in CDN for fast global delivery, with proper validation and processing.

**Action:** **Backend (Node.js/Express.js):** I implemented media upload using Multer for file handling with size and type validation. I processed images (resize, compress) and videos (transcode) before uploading to CDN. I uploaded processed media to AWS S3 and configured CloudFront CDN for global distribution. I generated signed URLs for secure media access with expiration. I stored media metadata in MongoDB with CDN URLs. **Frontend (React.js):** I built a drag-and-drop upload interface with progress indicators. I implemented client-side validation for file size and type. I showed upload progress and preview before submission. I displayed uploaded content with CDN URLs for fast loading.

**Result:** Media uploads complete in < 5 seconds for images, < 30 seconds for videos. CDN provides < 200ms load times globally. File validation prevents invalid uploads. User experience smooth with progress indicators.

**Takeaway:** CDN is essential for global media delivery. Client-side validation improves UX. Progress indicators are crucial for large file uploads. Signed URLs provide secure access.

---

## Q4. Handling view tracking and analytics

**Situation:** Need to track how many times content is viewed, by whom, and when, before content expires.

**Action:** **Backend (Node.js/Express.js):** I implemented view tracking by storing view records in MongoDB with contentId, userId, and timestamp. I used Redis to track unique views per content to prevent duplicate counting. I aggregated view counts for fast retrieval. I created analytics endpoints that provide view statistics. I implemented view tracking asynchronously to avoid blocking content retrieval. **Frontend (React.js):** I displayed view counts on content items. I created an analytics dashboard showing view statistics and trends. I used React Query to fetch and cache analytics data. I implemented real-time view count updates using polling.

**Result:** View tracking adds < 10ms overhead to content retrieval. Analytics dashboard loads in < 1 second. System handles millions of view events per day. Users can see engagement metrics in real-time.

**Takeaway:** Async tracking prevents blocking content retrieval. Redis helps prevent duplicate counting. Aggregated data enables fast analytics queries. Real-time updates improve user engagement.

---

## Q5. Implementing reactions and engagement features

**Situation:** Users need to react to content (like, reply) before it expires, with real-time updates.

**Action:** **Backend (Node.js/Express.js):** I implemented reactions by storing reaction records in MongoDB with contentId, userId, type, and timestamp. I used Redis to cache reaction counts for fast retrieval. I created WebSocket connections using Socket.io to broadcast reaction updates in real-time. I validated that content hasn't expired before allowing reactions. I aggregated reaction counts for efficient queries. **Frontend (React.js):** I built reaction buttons (like, reply) with instant feedback. I displayed reaction counts with real-time updates via WebSocket. I showed who reacted to content. I implemented optimistic updates for better UX.

**Result:** Reactions are processed in < 50ms. Real-time updates provide instant feedback. System handles 10M+ reactions per day. User engagement increased by 35% with real-time reactions.

**Takeaway:** WebSocket enables real-time engagement. Optimistic updates improve perceived performance. Caching reaction counts reduces database load. Real-time features increase user engagement.
