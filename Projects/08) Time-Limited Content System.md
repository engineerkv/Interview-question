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

## e) Architecture Overview

```

┌─────────────┐
│ Client │
└──────┬──────┘
 │
 ▼
┌─────────────────┐
│ Load Balancer │
└──────┬──────────┘
 │
 ┌───┴───┐
 ▼ ▼
┌──────┐ ┌──────┐
│Server│ │Server│
└──┬───┘ └──┬───┘
 │ │
 └───┬────┘
 ▼
┌─────────────────┐
│ Database │
└─────────────────┘

```

---

## Key Design Decisions

1. **TTL Storage:** Use TTL in database for automatic expiration

2. **CDN:** Use CDN for content media delivery

3. **Caching:** Cache active content in Redis

4. **Background Jobs:** Cleanup expired content on schedule

---

# 3) Low Level Design (LLD)

---

## Component Architecture

### Content Service

```javascript
class ContentService {
 async createContent(userId, mediaUrl, duration){
 // Create content with expiration time
 // Store in database with TTL
 // Return content ID
 }

 async getContent(contentId){
 // Check if content exists and not expired
 // Track view
 // Return content
 }

 async deleteExpiredContent(){
 // Background job to cleanup expired content
 }
}

```

### View Tracking Service

```javascript
class ViewTrackingService {
 async trackView(contentId, userId){
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
│ ├── Logo
│ ├── Navigation
│ └── UserMenu (Profile, Settings, Sign out)
├── MainContent
│ ├── ContentFeedPage
│ │ ├── ContentFeed
│ │ │ └── ContentCard
│ │ │ ├── UserInfo
│ │ │ ├── MediaDisplay
│ │ │ │ ├── Image/Video
│ │ │ │ └── ExpirationCountdown
│ │ │ ├── ViewCount
│ │ │ ├── ReactionButtons
│ │ │ │ ├── LikeButton
│ │ │ │ └── ReplyButton
│ │ │ └── ReactionCount
│ │ └── InfiniteScrollTrigger
│ ├── ContentCreationPage
│ │ ├── MediaUpload
│ │ │ ├── FileDropzone
│ │ │ ├── MediaPreview
│ │ │ └── UploadProgress
│ │ ├── DurationSelector
│ │ │ ├── DurationOptions (1h, 6h, 12h, 24h)
│ │ │ └── CustomDuration
│ │ └── PublishButton
│ └── ContentDetailPage
│ ├── MediaDisplay
│ ├── ExpirationCountdown
│ ├── ViewCount
│ ├── ReactionsList
│ └── ReplySection
└── Footer

```

### Key React Components

**Frontend Implementation:**

```javascript
// Content Card Component
const ContentCard<{ content: Content }> = ({ content }) => {
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
const ContentCreationPage= () => {
 const [file, setFile] = useState(null);
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

**State Management Strategy (React 19):**

- **Local State (useState)**: File selection, duration, UI state (loading, errors, modals)
- **Optimistic Updates (useOptimistic)**: React 19 hook for optimistic content creation and reactions
- **Form Actions (useActionState)**: React 19 hook for content upload forms with server actions
- **Transitions (useTransition)**: React 19 hook for expiration timer updates and non-urgent UI updates
- **API State**: React Query for server state (content feed, content details) - caching, refetching
- **Global State (Redux Toolkit)**: User authentication, followed users, content feed

**Frontend Implementation:**

```javascript
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

### iii) Advanced Patterns with React 19

**Expiration Countdown Timer:**

```javascript
import { useState, useEffect, useTransition } from 'react';

const ExpirationTimer<{ expiresAt}> = ({ expiresAt }) => {
 const [timeRemaining, setTimeRemaining] = useState(calculateTimeRemaining(expiresAt));
 const [isPending, startTransition] = useTransition();

 useEffect(() => {
 const interval = setInterval(() => {
 const remaining = calculateTimeRemaining(expiresAt);

 startTransition(() => {
 setTimeRemaining(remaining);
 });

 if (remaining.total <= 0) {
 clearInterval(interval);
 }
 }, 1000);

 return () => clearInterval(interval);
 }, [expiresAt]);

 const formatTime = (seconds) => {
 const hours = Math.floor(seconds / 3600);
 const minutes = Math.floor((seconds % 3600) / 60);
 const secs = seconds % 60;
 return `${hours}h ${minutes}m ${secs}s`;
 };

 if (timeRemaining.total <= 0) {
 return <div className="expired">Content has expired</div>;
 }

 return (
 <div className="expiration-timer">
 <span className="time-remaining">
 {formatTime(timeRemaining.total)}
 </span>
 <span className="label">remaining</span>
 </div>
 );
};

function calculateTimeRemaining(expiresAt) {
 const now = Date.now();
 const expires = expiresAt.getTime();
 const total = Math.max(0, Math.floor((expires - now) / 1000));

 return {
 total,
 hours: Math.floor(total / 3600),
 minutes: Math.floor((total % 3600) / 60),
 seconds: total % 60
 };
}
```

**Content Upload with React 19:**

```javascript
import { useActionState, useFormStatus, useTransition } from 'react';

// React 19: Server Action for content upload
async function uploadContentAction(
 prevState: { progress?; error?},
 formData: FormData
) {
 const file = formData.get('media');
 const durationHours = parseInt(formData.get('durationHours') as string);

 if (!file) {
 return { error: 'Please select a file' };
 }

 if (durationHours < 1 || durationHours > 168) {
 return { error: 'Duration must be between 1 and 168 hours' };
 }

 try {
 const uploadPromise = uploadContentWithProgress(formData, (progress) => {
 return { progress };
 });

 const result = await uploadPromise;
 return { success: true, contentId: result.contentId };
 } catch (error) {
 return { error: 'Upload failed' };
 }
}

const UploadButton= () => {
 const { pending } = useFormStatus(); // React 19 hook

 return (
 <button type="submit" disabled={pending}>
 {pending ? 'Uploading...' : 'Publish Content'}
 </button>
 );
};

const ContentUploadForm= () => {
 const [file, setFile] = useState(null);
 const [preview, setPreview] = useState(null);

 // React 19: useActionState for upload form
 const [state, formAction, isPending] = useActionState(uploadContentAction, {});

 const handleFileSelect = (selectedFile: File) => {
 setFile(selectedFile);

 // Generate preview
 if (selectedFile.type.startsWith('image/')) {
 const reader = new FileReader();
 reader.onloadend = () => setPreview(reader.result as string);
 reader.readAsDataURL(selectedFile);
 }
 };

 const handleSubmit = (formData: FormData) => {
 if (file) {
 formData.append('media', file);
 formAction(formData);
 }
 };

 return (
 <form action={handleSubmit}>
 <FileDropzone onFileSelect={handleFileSelect} />
 {preview && <img src={preview} alt="Preview" />}

 <select name="durationHours" required>
 <option value="24">24 hours</option>
 <option value="48">48 hours</option>
 <option value="72">72 hours</option>
 <option value="168">7 days</option>
 </select>

 {state.progress !== undefined && (
 <ProgressBar progress={state.progress} />
 )}
 {state.error && <span className="error">{state.error}</span>}
 {state.success && <span className="success">Content published!</span>}
 <UploadButton />
 </form>
 );
};
```

**Optimistic Reactions with React 19:**

```javascript
import { useOptimistic, useTransition } from 'react';

const ReactionButton<{ contentId; initialReactions: Reaction[] }> = ({
 contentId,
 initialReactions
}) => {
 const [reactions, setReactions] = useState(initialReactions);
 const [isPending, startTransition] = useTransition();

 // React 19: useOptimistic for reactions
 const [optimisticReactions, addOptimisticReaction] = useOptimistic(
 reactions,
 (state, newReaction: Reaction) => [...state, newReaction]
 );

 const handleLike = async () => {
 const newReaction: Reaction = {
 userId: currentUserId,
 type: 'like',
 createdAt: new Date()
 };

 // Optimistically add reaction
 startTransition(() => {
 addOptimisticReaction(newReaction);
 });

 try {
 await addReactionAPI(contentId, 'like');
 } catch (error) {
 // Rollback on error
 setReactions(reactions);
 }
 };

 return (
 <button onClick={handleLike} disabled={isPending}>
 ❤️ {optimisticReactions.filter(r => r.type === 'like').length}
 </button>
 );
};
```

### iv) Implementation Details

**Data Flow:**

1. **Content Feed** → ContentFeedPage fetches content via React Query infinite query, displays ContentCard components with expiration timers
2. **Content Creation** → User uploads media with React 19 useActionState, selects duration, publishes content
3. **Expiration Countdown** → Timer updates every second using React 19 transitions, shows time remaining
4. **Reactions** → User likes/replies with optimistic updates using useOptimistic
5. **View Tracking** → Content views tracked automatically when content is displayed

**Event Handling:**

- Media upload tracks progress with React 19 form actions
- Expiration countdown updates every second with useTransition for smooth updates
- Like/reply actions update optimistically with useOptimistic hook
- Infinite scroll loads more content automatically with Intersection Observer
- Real-time updates via WebSocket for new content with use() hook for promises

**UI/UX Considerations:**

- **Loading States**: Skeleton loaders for content feed, progress bars for uploads, loading indicators
- **Error Handling**: User-friendly error messages with retry options, error boundaries
- **Validation**: Client-side validation for file size, type, duration with React 19 form validation
- **Responsive Design**: Mobile-first layout, optimized for vertical scrolling, touch-friendly interactions
- **Accessibility**: ARIA labels, keyboard navigation, screen reader support, focus management
- **Performance**: Virtual scrolling for long feeds, lazy loading for media, image compression before upload, React 19 transitions for smooth animations

---

## Data Models

### Content Model

```javascript
// Content structure:
//
 contentId;
 userId;
 mediaUrl;
 mediaType: 'image' | 'video';
 createdAt;
 expiresAt; // TTL index for automatic deletion
 viewCount;
 reactions: Reaction[];

```

### Reaction Model

```javascript
// Reaction structure:
//
 userId;
 type: 'like' | 'reply';
 createdAt;

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
 - `limit`(default: 20, max: 50)
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

## b) Backend

*Note: Backend implementation details are kept minimal. Focus is on frontend integration.*

**API Endpoints Reference:**

- `POST /api/v1/content` - Create time-limited content
- `GET /api/v1/content/:contentId` - Get content details
- `GET /api/v1/content/user/:userId` - Get user's content
- `GET /api/v1/content/feed` - Get content feed
- `POST /api/v1/content/:contentId/reactions` - Add reaction

**WebSocket Events:**

- `content:new` - New content from followed users
- `content:expired` - Content expiration notification

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

```javascript
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

# 4) Algorithms

## Content Expiration Check Algorithm

**Purpose:** Efficiently check if content has expired before serving it to users.

**Algorithm:**

1. Check Redis cache for expiration status (fast path)
2. If not in cache, check database expiresAt field
3. Compare current time with expiresAt
4. Cache expiration status in Redis with TTL
5. Return expiration status

**Implementation:**

```javascript
async function isContentExpired(contentId){
 // Check Redis cache first
 const cached = await redis.get(`content:expired:${contentId}`);
 if (cached !== null) {
 return cached === 'true';
 }

 // Check database
 const content = await Content.findById(contentId);
 if (!content) {
 return true; // Content doesn't exist
 }

 const isExpired = content.expiresAt < new Date();

 // Cache result
 const ttl = Math.max(0, Math.floor((content.expiresAt.getTime() - Date.now()) / 1000));
 await redis.setex(`content:expired:${contentId}`, ttl, isExpired ? 'true' : 'false');

 return isExpired;
}

```

**Complexity:**

- Time: O(1) for cache hit, O(1) for database lookup
- Space: O(1) per content item
- **Performance:** Cache reduces database queries significantly

---

## View Deduplication Algorithm

**Purpose:** Prevent duplicate view counts from the same user viewing content multiple times.

**Algorithm:**

1. Check if user has already viewed content (Redis set)
2. If not viewed, add user to viewed set
3. Increment view count
4. Store view record in database

**Implementation:**

```javascript
async function trackView(contentId, userId){
 const viewKey = `content:views:${contentId}`;

 // Check if user already viewed
 const hasViewed = await redis.sismember(viewKey, userId);
 if (hasViewed) {
 return; // Already viewed
 }

 // Add user to viewed set
 await redis.sadd(viewKey, userId);

 // Get expiration TTL
 const content = await Content.findById(contentId);
 const ttl = Math.max(0, Math.floor((content.expiresAt.getTime() - Date.now()) / 1000));
 await redis.expire(viewKey, ttl);

 // Increment view count
 await redis.incr(`content:viewcount:${contentId}`);

 // Store view record asynchronously
 await View.create({ contentId, userId, viewedAt: new Date() });
}

```

**Complexity:**

- Time: O(1) for Redis operations
- Space: O(n) where n is number of unique viewers
- **Deduplication:** Redis sets ensure unique view tracking

---

# 5) Data Models

## Content Collection (MongoDB)

```javascript
{
 _id: ObjectId,
 contentId: String, // Unique content ID, indexed
 userId: ObjectId, // Creator reference, indexed
 type: String, // image, video, story
 mediaUrl: String, // CDN URL for media
 thumbnailUrl: String, // Thumbnail URL
 caption: String, // Content caption
 duration: Number, // Expiration duration in hours
 expiresAt, // Expiration timestamp, indexed (TTL)
 views: Number, // View count
 likes: Number, // Like count
 replies: Number, // Reply count
 createdAt, // Created timestamp, indexed
 updatedAt// Updated timestamp
}

// Indexes:
// - { contentId: 1 } (unique)
// - { expiresAt: 1 } (TTL index for automatic deletion)
// - { userId: 1, createdAt: -1 } (compound)
// - { expiresAt: 1, createdAt: -1 } (compound)

```

## Views Collection (MongoDB)

```javascript
{
 _id: ObjectId,
 contentId: ObjectId, // Content reference, indexed
 userId: ObjectId, // Viewer reference, indexed
 viewedAt, // View timestamp, indexed
 createdAt// Created timestamp
}

// Indexes:
// - { contentId: 1, userId: 1 } (compound, unique)
// - { contentId: 1, viewedAt: -1 } (compound)

```

---

# 6) Database Transactions and Consistency

### MongoDB Transactions

**Transaction Usage:**

- **Multi-Document Transactions** - For operations requiring ACID guarantees
- **Example:** Content creation + metadata update + CDN upload in single transaction
- **Session Management:** Use MongoDB sessions for transaction control

**Example:**

```javascript
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

- **Content Consistency:** Use transactions for content operations to ensure atomicity
- **Expiration Consistency:** Ensure TTL indexes work correctly
- **View Count Consistency:** Use Redis for view count updates, sync to database periodically
- **Cache Consistency:** Invalidate cache on content expiration

---

# 7) Protocols

### REST API Protocol

- **Protocol:** REST (Representational State Transfer)
- **Data Format:** JSON
- **HTTP Methods:** GET, POST, PUT, DELETE
- **Status Codes:** 200 (Success), 201 (Created), 400 (Bad Request), 401 (Unauthorized), 404 (Not Found - Content Expired), 500 (Server Error)
- **Authentication:** JWT Bearer token in Authorization header

---

# 8) API Design

### POST /api/v1/content

- **URL:** `/api/v1/content`
- **Method:** POST
- **Description:** Create time-limited content
- **Request Body:**

 ```json
 {
 "type": "image",
 "mediaUrl": "https://cdn.example.com/media/...",
 "caption": "My story",
 "duration": 24
 }

 ```

- **Response:**

 ```json
 {
 "success": true,
 "data": {
 "contentId": "content_abc123",
 "expiresAt": "2024-01-16T10:30:00Z",
 "createdAt": "2024-01-15T10:30:00Z"
 }
 }

 ```

- **Status Codes:** 201 (Created), 400 (Validation Error)

### GET /api/v1/content/:contentId

- **URL:** `/api/v1/content/:contentId`
- **Method:** GET
- **Description:** Get content (if not expired)
- **Response:**

 ```json
 {
 "success": true,
 "data": {
 "contentId": "content_abc123",
 "type": "image",
 "mediaUrl": "https://cdn.example.com/media/...",
 "expiresAt": "2024-01-16T10:30:00Z",
 "views": 1250,
 "likes": 45
 }
 }

 ```

- **Status Codes:** 200 (Success), 404 (Content Expired or Not Found)

---

# 9) Caching Strategy

### Redis Cache

**Cache Strategy:**

- **Key Format:** `content:{contentId}`, `content:expired:{contentId}`, `content:views:{contentId}`
- **Value:** Serialized JSON (content metadata, expiration status, view set)
- **TTL:**
 - Content metadata: Until expiration
 - Expiration status: Until expiration
 - View set: Until expiration
- **Eviction Policy:** TTL-based eviction

**Cache Patterns:**

- **Cache-Aside Pattern:** Check cache first, if miss query database and update cache
- **Write-Through Pattern:** Update cache when content is created
- **Cache Invalidation:** Invalidate cache on content expiration

---

# 10) Error Handling

### Error Scenarios and Responses

**Edge Cases Handling:**

- **Content Expired:** Return 404 Not Found with "Content has expired" message
- **Content Not Found:** Return 404 Not Found
- **Invalid Duration:** Return 400 Bad Request with validation errors
- **Media Upload Failure:** Return 500 Server Error, allow retry
- **Expiration Check Failure:** Return 500 Server Error, log for investigation

**Error Response Format:**

```json
{
 "error": {
 "code": "CONTENT_EXPIRED",
 "message": "Content has expired",
 "details": "This content expired on 2024-01-16T10:30:00Z"
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

**Database Scaling:**

- **Read Replicas:** Deploy read replicas for content queries
- **Sharding:** Shard content by userId for write scaling
- **Connection Pooling:** Use connection pooling to manage database connections

**Caching:**

- Distributed Redis cluster for high availability
- Cache content metadata and expiration status
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
- **Health Checks:** Verify content endpoints are healthy
- **Blue-Green Deployment:** Maintain two identical production environments

### Database Deployment

**MongoDB Setup:**

- **MongoDB Atlas** - Managed MongoDB service with automatic backups
- **TTL Index Configuration** - Configure TTL indexes for automatic expiration
- **Backup Strategy:** Daily automated backups with point-in-time recovery
- **Indexing:** Proper indexes on contentId, userId, expiresAt
- **Replication:** Replica sets for high availability

**Redis Setup:**

- **Redis Cloud / AWS ElastiCache** - Managed Redis service
- **Cluster Mode:** Redis cluster for high availability and performance
- **Persistence:** RDB snapshots and AOF for data durability

---

# 12) Security Considerations

### Rate Limiting

- Implement rate limiting at API layer to prevent abuse
- Limit number of content uploads per user per day/hour
- Use Redis for distributed rate limiting across multiple servers

### Input Validation

- Validate all API inputs (content data, duration, media files)
- Sanitize user input to prevent XSS attacks
- Validate media files for type, size, and content

### HTTPS/TLS

- All communication between clients and API encrypted using HTTPS
- Prevents eavesdropping and man-in-the-middle attacks
- SSL/TLS certificates for secure connections

### Content Access Control

- **Signed URLs:** Use time-limited signed URLs for media access
- **Expiration Enforcement:** Enforce content expiration on API level
- **User Verification:** Verify user owns content before allowing modifications

### Authentication and Authorization

- **JWT Tokens:** Use JWT for stateless authentication
- **Token Expiration:** Set appropriate token expiration times
- **Role-Based Access Control:** Implement RBAC for content operations

### Content Moderation

- **Content Filtering:** Filter inappropriate content using ML models
- **Report System:** Allow users to report inappropriate content
- **Automated Moderation:** Use automated tools for content moderation

### Monitoring and Alerts

- Set up monitoring for unusual activity patterns
- Trigger alerts for potential security issues
- Track metrics: upload rates, view rates, expiration rates
- Log all operations for security auditing

---

# 3) Interview Answers

---

## Q1. ⏰ ⏰ ⏰ Designing a time-limited content system

**Situation:** Need to design a time-limited content system for 1B+ users where content expires after a set duration (e.g., 24 hours), handling 500M+ content items per day.

**Action:** **Backend (Node.js/Express.js):** I designed a time-limited content system using MongoDB TTL index on the expiresAt field for automatic content expiration. I integrated CDN (CloudFront) for fast content media delivery globally. I implemented Redis caching for active content with configurable TTL. I created scheduled cleanup jobs using node-cron to remove expired content from storage. I built a content feed service that generates feeds from followed users and filters expired content. I implemented view tracking in a separate collection that updates in real-time. I added media processing to optimize content (compression, thumbnails). **Frontend (React.js):** I built a content creation interface with media upload, duration selection, and preview. I created a content feed showing active content with expiration countdown timers. I implemented view tracking and reaction features with real-time updates.

**Result:** System handles 1B+ users with content upload < 5 seconds. Automatic expiration works reliably. 99.9% of expired content cleaned up within 1 hour. User engagement increased by 40% with expiration countdown timers.

**Takeaway:** TTL storage simplifies expiration logic. CDN is essential for fast media delivery. Expiration countdowns create urgency and increase engagement.

---

## Q2. 💡 Handling content expiration

**Situation:** Content must expire exactly after the configured duration (e.g., 24 hours) after creation.

**Action:** **Backend (Node.js/Express.js):** I implemented content expiration using MongoDB TTL index on the `expiresAt` field for automatic deletion. I created scheduled background jobs using node-cron to remove expired content from storage. I implemented feed filtering that excludes expired content when generating content feeds. I invalidate expired content from Redis cache when detected. I built a media cleanup service that deletes content media files from CDN/storage after expiration. **Frontend (React.js):** I display expiration countdown timers on all content items. I show expiration warnings when content is about to expire. I hide expired content from feeds automatically. I provide clear messaging when users try to access expired content.

**Result:** 99.9% of content expires correctly. Cleanup jobs run efficiently without impacting performance. CDN storage is cleaned up efficiently, reducing storage costs by 60%. User notifications increased engagement by 25%.

**Takeaway:** Database TTL provides automatic expiration. Background jobs ensure complete cleanup. User notifications improve engagement.

---

## Q3. 💡 Implementing media upload and CDN integration

**Situation:** Users need to upload images/videos that are stored in CDN for fast global delivery, with proper validation and processing.

**Action:** **Backend (Node.js/Express.js):** I implemented media upload using Multer for file handling with size and type validation. I processed images (resize, compress) and videos (transcode) before uploading to CDN. I uploaded processed media to AWS S3 and configured CloudFront CDN for global distribution. I generated signed URLs for secure media access with expiration. I stored media metadata in MongoDB with CDN URLs. **Frontend (React.js):** I built a drag-and-drop upload interface with progress indicators. I implemented client-side validation for file size and type. I showed upload progress and preview before submission. I displayed uploaded content with CDN URLs for fast loading.

**Result:** Media uploads complete in < 5 seconds for images, < 30 seconds for videos. CDN provides < 200ms load times globally. File validation prevents invalid uploads. User experience smooth with progress indicators.

**Takeaway:** CDN is essential for global media delivery. Client-side validation improves UX. Progress indicators are crucial for large file uploads. Signed URLs provide secure access.

---

## Q4. 💡 Handling view tracking and analytics

**Situation:** Need to track how many times content is viewed, by whom, and when, before content expires.

**Action:** **Backend (Node.js/Express.js):** I implemented view tracking by storing view records in MongoDB with contentId, userId, and timestamp. I used Redis to track unique views per content to prevent duplicate counting. I aggregated view counts for fast retrieval. I created analytics endpoints that provide view statistics. I implemented view tracking asynchronously to avoid blocking content retrieval. **Frontend (React.js):** I displayed view counts on content items. I created an analytics dashboard showing view statistics and trends. I used React Query to fetch and cache analytics data. I implemented real-time view count updates using polling.

**Result:** View tracking adds < 10ms overhead to content retrieval. Analytics dashboard loads in < 1 second. System handles millions of view events per day. Users can see engagement metrics in real-time.

**Takeaway:** Async tracking prevents blocking content retrieval. Redis helps prevent duplicate counting. Aggregated data enables fast analytics queries. Real-time updates improve user engagement.

---

## Q5. ⚛️ Implementing reactions and engagement features

**Situation:** Users need to react to content (like, reply) before it expires, with real-time updates.

**Action:** **Backend (Node.js/Express.js):** I implemented reactions by storing reaction records in MongoDB with contentId, userId, type, and timestamp. I used Redis to cache reaction counts for fast retrieval. I created WebSocket connections using Socket.io to broadcast reaction updates in real-time. I validated that content hasn't expired before allowing reactions. I aggregated reaction counts for efficient queries. **Frontend (React.js):** I built reaction buttons (like, reply) with instant feedback. I displayed reaction counts with real-time updates via WebSocket. I showed who reacted to content. I implemented optimistic updates for better UX.

**Result:** Reactions are processed in < 50ms. Real-time updates provide instant feedback. System handles 10M+ reactions per day. User engagement increased by 35% with real-time reactions.

**Takeaway:** WebSocket enables real-time engagement. Optimistic updates improve perceived performance. Caching reaction counts reduces database load. Real-time features increase user engagement.
