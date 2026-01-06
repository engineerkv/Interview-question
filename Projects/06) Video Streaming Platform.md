# Video Streaming Platform

---

## 📍 Navigation

<div align="center">

[Home: README](README.md) • [← Previous: Notification System](05%29%20Notification%20System.md) • [Next: Social Media Feed →](07%29%20Social%20Media%20Feed.md)

[📋 Cheatsheet](Projects%20Interview%20Cheatsheet.md)

</div>

---

## Overview

Design a video streaming platform like YouTube where users can upload, watch, and interact with videos. The system handles video processing, adaptive streaming, recommendations, and real-time engagement.

---

## 1) Requirements

### Functional Requirements

**Core Features:**
- Video upload with metadata (title, description, tags, thumbnail)
- Video playback with quality options (360p, 720p, 1080p, 4K)
- User channels and subscriptions
- Video search and discovery
- Likes, comments, and views tracking
- Playlists (create, add videos, share)
- Watch history and watch later
- Personalized recommendations
- Trending videos feed

**Advanced Features:**
- Live streaming
- Video editing tools
- Community features (channels, memberships)
- Video analytics for creators
- Monetization features
- Video chapters and timestamps

### Non-Functional Requirements

**Performance:**
- Fast video loading with minimal buffering
- Adaptive bitrate streaming (quality adjusts to network)
- CDN delivery for global reach
- Video processing after upload

**Scalability:**
- Handle 200M+ users
- 1B+ hours watched per day
- Millions of concurrent viewers
- Billions of hours of video content

**User Experience:**
- Responsive design (mobile-first)
- Smooth playback (no buffering)
- Fast search results
- Intuitive navigation

---

## 2) Component Hierarchy

The frontend is a React application for video streaming. Here's the structure:

```
App
├── Layout
│   ├── Header
│   │   ├── Logo
│   │   ├── SearchBar
│   │   ├── UploadButton
│   │   └── UserMenu
│   └── MainContent
├── Pages
│   ├── HomePage
│   │   ├── VideoGrid (recommended videos)
│   │   └── CategoryTabs
│   ├── VideoPlayerPage
│   │   ├── VideoPlayer
│   │   │   ├── VideoElement (HTML5 video with controls)
│   │   │   ├── QualitySelector
│   │   │   ├── PlaybackSpeedSelector
│   │   │   └── FullscreenToggle
│   │   ├── VideoInfo
│   │   │   ├── VideoTitle
│   │   │   ├── VideoMetadata (views, date, channel)
│   │   │   ├── EngagementBar
│   │   │   │   ├── LikeButton (with count)
│   │   │   │   ├── DislikeButton
│   │   │   │   ├── ShareButton
│   │   │   │   └── SaveButton
│   │   │   └── SubscribeButton
│   │   ├── VideoDescription
│   │   ├── CommentSection
│   │   │   ├── CommentList
│   │   │   │   └── CommentItem (with replies)
│   │   │   └── CommentInput
│   │   └── RelatedVideos (sidebar)
│   ├── ChannelPage
│   │   ├── ChannelHeader (banner, avatar, subscribe button)
│   │   ├── ChannelTabs (Videos, Playlists, About)
│   │   └── VideoGrid (channel's videos)
│   ├── SearchPage
│   │   ├── SearchResults
│   │   │   ├── VideoResults
│   │   │   ├── ChannelResults
│   │   │   └── PlaylistResults
│   │   └── Filters (Upload date, Type, Duration)
│   └── UploadPage
│       ├── VideoUploader (drag-and-drop)
│       ├── UploadProgress
│       └── VideoMetadataForm (title, description, tags, thumbnail)
└── SharedComponents
    ├── VideoCard (thumbnail, title, channel, views)
    ├── VideoPlayer
    └── LoadingSpinner
```

### Key Components Explained

**1. VideoPlayer Component**
- HTML5 video player with custom controls
- Adaptive bitrate streaming (HLS or DASH)
- Quality selector (360p, 720p, 1080p, 4K)
- Playback speed control
- Fullscreen support

**2. VideoCard Component**
- Displays video in grid/list
- Shows thumbnail, title, channel, views, date
- Clickable to navigate to video page
- Lazy load thumbnails

**3. CommentSection Component**
- Display comments with replies
- Comment input for new comments
- Like comments functionality
- Sort options (newest, top comments)

**4. VideoUploader Component**
- Drag-and-drop file upload
- Upload progress tracking
- Video metadata form
- Thumbnail selection/upload

**5. EngagementBar Component**
- Like/dislike buttons with counts
- Share button (copy link, social media)
- Save to playlist button
- Subscribe button

---

## 3) Data Models

Here are the key data structures:

```typescript
// Video
interface Video {
  id: string;
  title: string;
  description: string;
  channelId: string;
  channel: Channel;
  thumbnailUrl: string;
  videoUrl: string;  // Master playlist URL for adaptive streaming
  duration: number;  // Seconds
  views: number;
  likes: number;
  dislikes: number;
  commentsCount: number;
  tags: string[];
  category: string;
  isLive: boolean;
  publishedAt: string;
  createdAt: string;
}

// Channel
interface Channel {
  id: string;
  name: string;
  description: string;
  avatarUrl: string;
  bannerUrl: string;
  subscribersCount: number;
  videosCount: number;
  isSubscribed: boolean;
}

// Comment
interface Comment {
  id: string;
  videoId: string;
  userId: string;
  user: User;
  content: string;
  likesCount: number;
  repliesCount: number;
  replies?: Comment[];
  replyToId?: string;
  createdAt: string;
}

// Playlist
interface Playlist {
  id: string;
  name: string;
  description?: string;
  channelId: string;
  videos: PlaylistVideo[];
  isPublic: boolean;
  createdAt: string;
}

// Playlist video
interface PlaylistVideo {
  videoId: string;
  video: Video;
  position: number;  // Order in playlist
  addedAt: string;
}

// Watch history
interface WatchHistory {
  videoId: string;
  video: Video;
  watchedAt: string;
  watchTime: number;  // Seconds watched
  completed: boolean;
}
```

### Data Flow Explanation

**When a user watches a video:**
1. User clicks video card
2. Navigate to VideoPlayerPage
3. Fetch video metadata and streaming URLs
4. Video player loads adaptive streaming playlist
5. Player automatically selects quality based on network
6. Track watch time and update history
7. Increment view count (debounced)

**Video upload flow:**
1. User selects video file
2. Upload video file (chunked for large files)
3. Show upload progress
4. User enters metadata (title, description, tags)
5. Server processes video (transcoding, thumbnail generation)
6. Video appears in channel when processing complete

**Adaptive streaming:**
1. Video is transcoded into multiple qualities
2. Master playlist contains all quality URLs
3. Player selects quality based on network speed
4. Quality switches automatically during playback
5. Better user experience with minimal buffering

---

## 4) API Design

### REST Endpoints

**GET /api/v1/videos**
- Get videos (home feed, recommendations)
- Query params: `page`, `limit`, `category`, `sortBy`
- Returns: Paginated list of Video objects

**GET /api/v1/videos/:id**
- Get video details
- Returns: Video object with full details

**GET /api/v1/videos/:id/stream**
- Get video streaming URLs (adaptive streaming)
- Returns: Streaming URLs for different qualities

**POST /api/v1/videos**
- Upload a video
- Request: Multipart form data with video file and metadata
- Returns: Video object (processing status)

**POST /api/v1/videos/:id/like**
- Like or unlike a video
- Returns: Updated Video with like status

**GET /api/v1/videos/:id/comments**
- Get video comments
- Query params: `page`, `limit`, `sortBy`
- Returns: Paginated list of Comment objects

**POST /api/v1/videos/:id/comments**
- Add a comment
- Request body: `{ content: string, replyToId?: string }`
- Returns: Comment object

**GET /api/v1/channels/:id**
- Get channel details
- Returns: Channel object

**POST /api/v1/channels/:id/subscribe**
- Subscribe or unsubscribe to channel
- Returns: Updated Channel with subscription status

**GET /api/v1/search**
- Search videos, channels, playlists
- Query params: `q` (query), `type`, `page`, `limit`
- Returns: Search results

### API Request/Response Examples

**Get Videos:**
```json
// GET /api/v1/videos?page=1&limit=20&category=gaming
// Response
{
  "success": true,
  "data": {
    "videos": [
      {
        "id": "video_123",
        "title": "Amazing Gameplay",
        "channel": {
          "id": "channel_456",
          "name": "Gaming Channel",
          "avatarUrl": "https://cdn.example.com/avatar.jpg"
        },
        "thumbnailUrl": "https://cdn.example.com/thumb.jpg",
        "duration": 600,
        "views": 1250000,
        "likes": 45000,
        "publishedAt": "2024-01-15T10:00:00Z"
      }
    ],
    "total": 500,
    "page": 1,
    "limit": 20
  }
}
```

**Get Video Streaming URLs:**
```json
// GET /api/v1/videos/video_123/stream
// Response
{
  "success": true,
  "data": {
    "masterPlaylist": "https://cdn.example.com/video_123/master.m3u8",
    "qualities": [
      { "quality": "360p", "url": "https://cdn.example.com/video_123/360p.m3u8" },
      { "quality": "720p", "url": "https://cdn.example.com/video_123/720p.m3u8" },
      { "quality": "1080p", "url": "https://cdn.example.com/video_123/1080p.m3u8" }
    ]
  }
}
```

---

## Key Design Decisions

**1. Adaptive Bitrate Streaming**
- Transcode videos into multiple qualities
- Player selects quality based on network
- Automatic quality switching during playback
- Better experience with minimal buffering

**2. CDN for Video Delivery**
- Serve videos from CDN edge locations
- Faster global delivery
- Reduced server load
- Better scalability

**3. Lazy Loading for Thumbnails**
- Load thumbnails as user scrolls
- Improves initial page load
- Better performance with many videos

**4. Optimistic Updates for Engagement**
- Show likes/comments immediately
- Better perceived performance
- Sync with server state

**5. Infinite Scroll for Feed**
- Load more videos as user scrolls
- Cursor-based pagination
- Smooth scrolling experience

**6. Real-time View Count Updates**
- Debounce view count increments
- Batch updates for efficiency
- Real-time updates via polling or WebSocket

---

## Interview Talking Points

**When explaining this system, I'd focus on:**

1. **Requirements First**: Start with core functionality - upload videos, watch videos, subscriptions, engagement

2. **Component Structure**: Explain the React component hierarchy - video player, video cards, comments, channels

3. **Data Models**: Walk through Video, Channel, Comment, Playlist - and how they support the platform

4. **API Design**: Show the REST endpoints - videos, streaming, comments, channels, search

5. **Key Challenges**: 
   - Adaptive bitrate streaming for different network conditions
   - Video processing and transcoding
   - CDN delivery for global reach
   - Handling millions of concurrent viewers
   - Real-time engagement updates

**Example explanation flow:**
> "So for a video streaming platform, the core requirement is allowing users to upload and watch videos. The frontend is a React app with a video player component that uses adaptive bitrate streaming - videos are transcoded into multiple qualities (360p, 720p, 1080p), and the player automatically selects the best quality based on the user's network speed. The data model centers around Video objects with metadata, Channel objects for creators, and Comment objects for engagement. Videos are delivered through a CDN for fast global access. The main API endpoints handle video upload (with processing), video playback (with streaming URLs), comments, subscriptions, and search. Key challenges include adaptive streaming for different network conditions, video processing and transcoding after upload, CDN delivery for scalability, and handling millions of concurrent viewers during popular videos."

---

## 📍 Navigation

<div align="center">

[Home: README](README.md) • [← Previous: Notification System](05%29%20Notification%20System.md) • [Next: Social Media Feed →](07%29%20Social%20Media%20Feed.md)

[📋 Cheatsheet](Projects%20Interview%20Cheatsheet.md)

</div>

---
