# Video Streaming Platform

> **Project Type:** Full-Stack Web Application (MERN Stack)
> **Scale:** Handle 200M+ users, 1B+ hours watched per day, global CDN, adaptive bitrate streaming
> **Tech Stack:** React.js, Node.js, Express.js, MongoDB, Redis, Elasticsearch, AWS S3, CloudFront, FFmpeg

# 1) Problem Statement

Design and implement a video streaming platform that addresses the following challenges:

- **Core Functionality**: Enable users to upload, process, and stream videos globally with adaptive bitrate streaming, playlists, subscriptions, and recommendations
- **Scale Requirements**: Handle 200M+ users, 1B+ hours watched per day, millions of concurrent viewers, and billions of hours of video content
- **Performance**: Fast video loading with minimal buffering, adaptive quality based on network speed, CDN delivery for global reach
- **Video Processing**: Transcode videos into multiple quality formats (360p, 720p, 1080p, 4K) for different devices and network conditions
- **Content Delivery**: Deliver content through global CDN to minimize latency and optimize bandwidth usage
- **Video Management**: Support video upload, metadata management, search, and discovery features
- **User Engagement**: Provide likes, comments, views tracking, watch history, and personalized recommendations
- **Data Consistency**: Maintain data consistency for view counts, engagement metrics, and video metadata across distributed systems

---

# 2) High Level Design (HLD)

## a) Requirements

### i) Functional Requirements

#### User Management

- **User registration and authentication** - Users can sign up with email or Google account - makes it easy to get started

- **User profiles** - Users can customize their channel, upload profile picture, add channel description

- **Channel management** - Users can create and manage their own channels - like having your own TV channel

- **Subscription system** - Users can subscribe to channels, get notified of new videos

#### Video Management

- **Video upload** - Users can upload videos with title, description, tags, thumbnail

- **Video processing** - Videos are processed (transcoding, thumbnail generation) after upload

- **Video playback** - Users can watch videos with quality options (360p, 720p, 1080p, 4K)

- **Video metadata** - Videos have title, description, tags, category, duration, view count

- **Video search** - Users can search videos by title, description, tags, channel name

#### Video Interaction

- **Likes and dislikes** - Users can like or dislike videos

- **Comments** - Users can comment on videos, reply to comments, like comments

- **Views** - Video view count tracks how many times video was watched

- **Watch history** - Users can see their watch history

- **Watch later** - Users can save videos to watch later

#### Playlists

- **Create playlists** - Users can create custom playlists

- **Add to playlist** - Users can add videos to playlists

- **Playlist management** - Users can edit, delete, reorder playlists

- **Public/Private playlists** - Playlists can be public or private

#### Recommendations

- **Home feed** - Personalized video recommendations on home page

- **Related videos** - Show related videos based on current video

- **Trending videos** - Show trending videos based on views, likes, recent activity

- **Subscriptions feed** - Show videos from subscribed channels

### ii) Non-Functional Requirements

#### Performance

- **Fast video loading** - Videos should start playing quickly - users expect instant playback

- **Adaptive streaming** - Video quality adjusts based on network speed automatically

- **CDN delivery** - Videos served from CDN for fast global delivery

- **Efficient encoding** - Videos encoded in multiple formats for different devices

#### Scalability

- **Handle millions of videos** - System should handle millions of videos and users

- **High concurrent viewers** - Support millions of concurrent video viewers

- **Video storage** - Store petabytes of video data efficiently

- **Database optimization** - Fast search and retrieval of video metadata

#### User Experience

- **Responsive design** - Works great on mobile, tablet, desktop

- **Smooth playback** - No buffering, smooth video playback

- **Fast search** - Search results appear instantly

- **Intuitive UI** - Easy to navigate, find videos, manage playlists

#### Security

- **Content moderation** - Moderate videos and comments for inappropriate content

- **Copyright protection** - Detect and handle copyright violations

- **User privacy** - Protect user data and viewing history

- **Secure uploads** - Validate and secure video uploads

---

## b) Scope and Priority

### Phase 1: MVP (Must Have) - Priority 1

**Core video platform - what users need to watch and upload videos**

#### Functional

- **User authentication** - Sign up, login, user profiles

- **Video upload** - Upload videos with basic metadata

- **Video playback** - Watch videos with quality options

- **Video search** - Search videos by title, description

- **Basic interactions** - Likes, comments, views

- **Subscriptions** - Subscribe to channels, see subscription feed

#### Non-Functional

- **Performance** - Fast video loading, smooth playback

- **Responsive** - Mobile-first design

- **Security** - Secure uploads, content moderation

### Phase 2: Enhanced Features - Priority 2

**Features that improve user experience and engagement**

#### Functional

- **Playlists** - Create and manage playlists

- **Watch history** - Track and display watch history

- **Watch later** - Save videos to watch later

- **Recommendations** - Personalized video recommendations

- **Trending** - Trending videos based on popularity

- **Video analytics** - Channel owners can see video statistics

#### Non-Functional

- **Advanced search** - Better search with filters

- **Analytics** - Track user behavior, video performance

### Phase 3: Advanced Features - Priority 3

**Advanced features for power users and business growth**

#### Functional

- **Live streaming** - Live video streaming capability

- **Monetization** - Ads, channel memberships, super chats

- **Community features** - Community posts, polls

- **Advanced analytics** - Detailed analytics for creators

---

## c) Technology Choices

### Frontend Framework

- **React.js:** Perfect for building interactive video platform
  - **Component-based** - Video player, comments, playlists are reusable components
  - **Fast updates** - Virtual DOM makes UI updates smooth
  - **Code splitting** - Load video pages only when needed
  - **TypeScript** - Type safety for video data, user data

### State Management

- **Redux Toolkit:** Manages complex state (videos, user, playlists, watch history)
  - **Video state** - Current video, video list, search results
  - **User state** - Authentication, profile, subscriptions
  - **Playlist state** - User playlists, current playlist
  - **Watch history** - User's watch history

### Routing

- **React Router v6:** Client-side routing for smooth navigation
  - **Video pages** - `/watch/:videoId` for video playback
  - **Channel pages** - `/channel/:channelId` for channel view
  - **Search page** - `/search?q=query` for search results
  - **Playlist page** - `/playlist/:playlistId` for playlists

### Video Player

- **Video.js / React Player:** Video player library for playback
  - **Multiple formats** - Supports different video formats
  - **Quality selection** - Users can choose video quality
  - **Controls** - Play, pause, volume, fullscreen controls
  - **Adaptive streaming** - Adjusts quality based on network

### UI Components

- **Material-UI:** Pre-built components for faster development
  - **Video cards** - Consistent video display
  - **Forms** - Upload forms, comment forms
  - **Modals** - Video player modal, playlist modal
  - **Responsive grid** - Video grid that adapts to screen size

### Backend Framework

- **Node.js + Express.js:** Backend server that handles all business logic
  - **Why Node.js?** JavaScript everywhere - same language for frontend and backend
  - **Express.js** - Fast, minimal web framework
  - **REST APIs** - Standard REST endpoints for frontend to call

### Database

- **MongoDB:** NoSQL database for storing videos, users, comments, playlists
  - **Why MongoDB?** Flexible schema - easy to change video metadata structure
  - **Document-based** - Stores data as JSON-like documents
  - **Scalable** - Handles large amounts of video metadata

### Video Storage

- **AWS S3:** Cloud storage for video files
  - **Why S3?** Scalable, reliable file storage for large video files
  - **Lifecycle policies** - Move old videos to cheaper storage
  - **CDN integration** - Serve videos through CloudFront for faster access

### Video Processing

- **FFmpeg:** Video processing library for transcoding
  - **Transcoding** - Convert videos to different formats and qualities
  - **Thumbnail generation** - Generate video thumbnails
  - **Metadata extraction** - Extract video duration, resolution, etc.

### Search

- **MongoDB Text Search / Elasticsearch:** Full-text search for videos
  - **MongoDB Text Search** - Good for basic search needs
  - **Elasticsearch** - Better for advanced search with filters and ranking

### Caching

- **Redis:** In-memory cache for frequently accessed data
  - **Video metadata cache** - Cache popular video metadata
  - **Search cache** - Cache search results
  - **Session storage** - User sessions

---

## d) Capacity Estimation

### Throughput Requirements

- **Daily Active Users**: 200 million users per day
- **Peak Traffic**: 3x average during peak hours (600 million users per day)
- **Read:Write Ratio**: 1000:1 (watching videos vs uploading videos)
- **Average Videos Watched Per User**: 5 videos per day
- **Average Video Duration**: 10 minutes

**Calculations:**
- **Average Writes Per Second (WPS)**: (200M users × 0.1 uploads/day) / 86,400 seconds ≈ 231 WPS
- **Peak WPS**: 231 × 3 = 693 WPS
- **Average Reads Per Second (RPS)**: 200M users × 5 videos/day / 86,400 seconds ≈ 11,574 RPS
- **Peak RPS**: 11,574 × 3 = 34,722 RPS
- **Concurrent Viewers**: 10 million concurrent video streams

### Storage Estimation

**Storage per Video:**
- Original video: 500 MB average (10-minute video at 1080p)
- Transcoded versions: 360p (50 MB), 720p (150 MB), 1080p (300 MB), 4K (1 GB)
- Thumbnails: 5 MB (multiple thumbnails)
- **Total per Video**: ~2 GB (including all quality versions)

**Storage Requirements:**
- **Total Videos per Year**: 200M users × 0.1 uploads/day × 365 = 7.3 billion videos
- **Video Storage**: 7.3B × 2 GB ≈ 14.6 PB per year
- **User Data**: 200M users × 10 KB ≈ 2 TB
- **Metadata**: 7.3B videos × 5 KB ≈ 36.5 TB/year
- **Total Storage**: ~14.6 PB (videos) + 2 TB (users) + 36.5 TB (metadata) ≈ 14.64 PB/year

### Bandwidth Estimation

- **Average Video Bitrate**: 5 Mbps (adaptive streaming average)
- **Daily Bandwidth**: 200M users × 5 videos × 10 min × 5 Mbps = 500,000 TB/day
- **Peak Bandwidth**: 500,000 TB × 3 = 1,500,000 TB/day during peak hours
- **Average Bandwidth**: 500,000 TB / 86,400 seconds ≈ 5.8 PB/s
- **Peak Bandwidth**: 5.8 PB/s × 3 ≈ 17.4 PB/s

### Caching Estimation

Following the **80-20 rule** where 20% of videos generate 80% of traffic:
- **Cache 20% of hot videos**: 7.3B × 0.2 = 1.46B videos
- **Cache memory required**: 1.46B × 2 GB = 2.92 PB (CDN edge cache)
- **Cache hit ratio**: 90% (only 10% of video requests hit origin)
- **Requests hitting Origin**: 34,722 × 0.10 ≈ 3,472 RPS (manageable with CDN)

### Infrastructure Sizing

- **API Servers**: 100-200 instances behind load balancer, each handling 200-500 RPS
- **Video Processing Workers**: 50-100 instances for transcoding, each handling 2-5 videos concurrently
- **Database**: MongoDB cluster with 30-50 nodes for storage and high read/write throughput
- **Cache Layer**: Redis cluster with 15-20 nodes for high availability and performance
- **Search**: Elasticsearch cluster with 15-20 nodes for video search
- **CDN**: CloudFront/Cloudflare with edge locations globally for video delivery
- **Storage**: AWS S3 or similar object storage for video files

---

## e) Architecture Overview

The system follows a layered architecture with video processing pipeline and global CDN delivery. Here's how the complete system works:

```

┌─────────────────────────────────────────────────────────┐
│              Frontend (React.js) - Client Side           │
│  (This is what users see in their browser)              │
├─────────────────────────────────────────────────────────┤
│  ┌──────────────────────────────────────────────────┐   │
│  │         Browser (Chrome, Firefox, Safari)        │   │
│  │  ┌────────────────────────────────────────────┐  │   │
│  │  │     React.js Application (SPA)             │  │   │
│  │  │  ┌──────────────────────────────────────┐  │  │   │
│  │  │  │  React Router (Client-side Routing)  │  │  │   │
│  │  │  └──────────────────────────────────────┘  │  │   │
│  │  │  ┌──────────────────────────────────────┐  │  │   │
│  │  │  │  Redux Toolkit (State Management)    │  │  │   │
│  │  │  │  - Videos, User, Playlists, History │  │  │   │
│  │  │  └──────────────────────────────────────┘  │  │   │
│  │  │  ┌──────────────────────────────────────┐  │  │   │
│  │  │  │  Video.js Player (Video Playback)    │  │  │   │
│  │  │  └──────────────────────────────────────┘  │  │   │
│  │  │  ┌──────────────────────────────────────┐  │  │   │
│  │  │  │  Material-UI Components              │  │  │   │
│  │  │  └──────────────────────────────────────┘  │  │   │
│  │  └────────────────────────────────────────────┘  │   │
│  └──────────────────────────────────────────────────┘   │
└─────────────────────────────────────────────────────────┘
        │                                    │
        │ HTTP/REST API                     │ Video Streaming
        │ (Metadata, actions)               │ (CDN)
        ▼                                    ▼
┌─────────────────────────────────────────────────────────┐
│              Backend (Node.js + Express.js)              │
│  (Server that handles business logic and data)          │
├─────────────────────────────────────────────────────────┤
│  ┌──────────────────────────────────────────────────┐   │
│  │         Load Balancer / API Gateway              │   │
│  └──────────────────────────────────────────────────┘   │
│                        │                                 │
│        ┌───────────────┼───────────────┐                │
│        ▼               ▼               ▼                │
│  ┌──────────┐  ┌──────────┐  ┌──────────┐             │
│  │ Express  │  │ Express  │  │ Express  │             │
│  │ Server 1 │  │ Server 2 │  │ Server 3 │             │
│  └──────────┘  └──────────┘  └──────────┘             │
│        │               │               │                │
│        └───────────────┼───────────────┘                │
│                        ▼                                 │
│  ┌──────────────────────────────────────────────────┐   │
│  │         Business Logic Layer                     │   │
│  │  - Video Service (upload, metadata)              │   │
│  │  - User Service (authentication, profiles)       │   │
│  │  - Comment Service (comments, replies)           │   │
│  │  - Playlist Service (playlist management)        │   │
│  │  - Recommendation Service (video recommendations)│   │
│  └──────────────────────────────────────────────────┘   │
│                        ▼                                 │
│  ┌──────────────────────────────────────────────────┐   │
│  │         Data Access Layer                        │   │
│  │  - MongoDB (Videos, users, comments)             │   │
│  │  - Redis (Caching, sessions)                     │   │
│  │  - Elasticsearch (Video search)                  │   │
│  └──────────────────────────────────────────────────┘   │
└─────────────────────────────────────────────────────────┘
        │                    │                    │
        ▼                    ▼                    ▼
┌──────────────┐  ┌──────────────┐  ┌──────────────┐
│   MongoDB    │  │    Redis     │  │ Elasticsearch│
│  (Database)  │  │   (Cache)    │  │   (Search)   │
│              │  │              │  │              │
│  - Videos    │  │  - Video     │  │  - Video     │
│  - Users     │  │    Metadata  │  │    Index     │
│  - Comments  │  │  - Search    │  │  - Search    │
│  - Playlists │  │    Results   │  │    Results   │
└──────────────┘  └──────────────┘  └──────────────┘
        │                    │                    │
        └────────────────────┼────────────────────┘
                             │
                             ▼
                    ┌──────────────┐
                    │   External   │
                    │   Services   │
                    │              │
                    │  - AWS S3    │
                    │  - CloudFront│
                    │  - FFmpeg    │
                    │    (Worker)  │
                    └──────────────┘

```

### Frontend Architecture

**Frontend Layers:**

1. **Presentation Layer (React Components)**
   - **UI Components**: Reusable components (VideoCard, CommentCard, PlaylistCard, LikeButton)
   - **Feature Components**: VideoPlayer, VideoUploader, PlaylistManager, SearchBar
   - **Layout Components**: Header, Sidebar, Navigation, MainLayout
   - **Page Components**: HomePage, VideoPage, ChannelPage, SearchPage

2. **State Management Layer**
   - **Local State (useState)**: Component-specific UI state (form inputs, loading, errors, player state)
   - **Server State (Redux Toolkit)**: Global state for videos, user, playlists, watch history
   - **API State (React Query)**: Video data caching, refetching, optimistic updates

3. **Video Player Layer**
   - **Video.js Player**: HTML5 video player with adaptive bitrate streaming (HLS/DASH)
   - **Quality Selection**: Automatic quality adjustment based on network speed
   - **Playback Controls**: Play, pause, seek, volume, fullscreen, playback speed

4. **API Integration Layer**
   - **API Client**: Axios instance with interceptors for auth, error handling
   - **Redux Thunks**: Async actions for API operations (fetchVideos, uploadVideo, likeVideo)
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

1. **User Interaction** → User watches video or uploads video
2. **State Update** → Redux action dispatched or React Query mutation triggered
3. **API Call** → Axios makes HTTP request to backend API
4. **Loading State** → UI shows loading indicator
5. **Response Handling** → Success/error state updates Redux store or React Query cache
6. **Video Playback** → Video.js player requests video segments from CDN
7. **UI Update** → Components re-render with new data

### Backend Architecture

**Backend Layers:**

1. **API Gateway/Load Balancer** - Entry point for all HTTP requests
2. **API Server Layer** - Stateless servers handling HTTP requests
3. **Video Processing Layer** - Worker nodes for video transcoding
4. **Application Service Layer** - Business logic and orchestration
5. **Cache Layer** - In-memory caching for performance
6. **Database Layer** - Persistent data storage
7. **Search Layer** - Elasticsearch for video search
8. **CDN Layer** - Global content delivery network
9. **Storage Layer** - Object storage for video files

### Complete Request Flow

**Video Upload Flow:**
1. **Frontend**: User selects video file and uploads
2. **API Call**: POST request to upload API with video file
3. **Backend**: Validate file, upload to S3, create video record in MongoDB
4. **Processing Queue**: Add video to processing queue
5. **Worker**: FFmpeg worker transcodes video into multiple qualities
6. **Thumbnails**: Generate thumbnails at key timestamps
7. **Indexing**: Index video in Elasticsearch for search
8. **Response**: Return video ID and processing status
9. **Frontend**: Show upload progress and processing status

**Video Playback Flow:**
1. **Frontend**: User clicks on video to watch
2. **API Call**: GET request to video metadata API
3. **Backend**: Fetch video metadata from MongoDB (or cache)
4. **Response**: Return video metadata including CDN URLs for different qualities
5. **Frontend**: Video.js player requests video segments from CDN
6. **CDN**: Serves video segments from nearest edge location
7. **Adaptive Streaming**: Player automatically adjusts quality based on network speed
8. **Analytics**: Track view count and watch time

**Feed Loading Flow:**
1. **Frontend**: User opens home feed
2. **API Call**: GET request to feed API
3. **Backend**: Generate personalized feed based on user preferences
4. **Cache Check**: Check Redis for cached feed
5. **Response**: Return video recommendations
6. **Frontend**: Display video cards with thumbnails
7. **Lazy Loading**: Load video metadata as user scrolls

### Key Components

- **Frontend (React.js)**: Single-page application with client-side routing, component-based architecture, Redux for state management, Video.js for playback
- **CDN/Edge**: Global distribution of video segments and static assets, reduces latency and bandwidth costs
- **Load Balancer**: Distributes HTTP traffic across API servers, SSL/TLS termination
- **API Servers**: Stateless design for horizontal scaling, handle video metadata, uploads, interactions
- **Video Processing Workers**: FFmpeg-based workers for video transcoding, thumbnail generation, metadata extraction
- **Application Services**: Video Service, User Service, Comment Service, Playlist Service, Recommendation Service
- **Cache Layer (Redis)**: In-memory cache for hot videos (20% of traffic), video metadata, search results
- **Database (MongoDB)**: Sharded across multiple nodes for horizontal scaling, stores videos, users, comments, playlists
- **Search (Elasticsearch)**: Fast full-text search for videos, handles title, description, tags, channel search
- **Video Storage (AWS S3)**: Object storage for video files, organized by video ID and quality
- **CDN (CloudFront)**: Global CDN for video delivery, adaptive bitrate streaming support

1. **React.js for Frontend:** Perfect for interactive video platform - video player, comments, playlists all need fast UI updates
   - **Component-based** - Video cards, comment sections are reusable
   - **Fast navigation** - No page reloads, smooth transitions
   - **Code splitting** - Video pages load only when needed

2. **CDN for Video Delivery:** Videos are large files - CDN makes them load faster globally
   - **Why CDN?** Videos served from edge locations - closer to users
   - **Faster playback** - Especially important for video streaming
   - **Reduces server load** - Videos don't hit main server

3. **Adaptive Streaming:** Video quality adjusts based on network speed - better user experience
   - **Why important?** Users have different internet speeds
   - **Better UX** - No buffering, smooth playback
   - **Saves bandwidth** - Lower quality for slower connections

4. **Video Processing Queue:** Videos need processing after upload - use queue for reliability
   - **Why queue?** Processing takes time, can't block user
   - **Reliability** - Retry if processing fails
   - **Scalability** - Multiple workers can process videos

5. **MongoDB for Metadata:** Video metadata is flexible - MongoDB handles schema changes easily
   - **Why MongoDB?** Easy to add new fields (tags, categories, etc.)
   - **Scalable** - Handles millions of videos
   - **Fast queries** - Indexed fields for fast retrieval

---

# 3) Low Level Design (LLD)

## a) Frontend

### i) Component Architecture

**Component Hierarchy:**

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

Think of the frontend as a tree of React components - each component handles a specific part of the UI, and they work together to create the complete user experience.

**Component Hierarchy:**

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
│       └── ChannelPage
│           ├── ChannelHeader
│           ├── ChannelTabs (Videos, Playlists, About)
│           └── VideoGrid
└── ReduxProvider (Global State Management)
    └── Store
        ├── authSlice (User authentication state)
        ├── videoSlice (Videos data)
        ├── playlistSlice (Playlists data)
        └── watchHistorySlice (Watch history)
```

### Key React Components

**Frontend Implementation:**

```typescript
// Video Player Component
const VideoPlayer: React.FC<{ videoId: string }> = ({ videoId }) => {
  const [player, setPlayer] = useState<any>(null);
  const [quality, setQuality] = useState('auto');
  const { data: video } = useVideo(videoId);

  useEffect(() => {
    if (video) {
      const videoJsPlayer = videojs('video-player', {
        sources: video.sources,
        controls: true,
        responsive: true,
        fluid: true
      });
      setPlayer(videoJsPlayer);
      return () => videoJsPlayer.dispose();
    }
  }, [video]);

  return (
    <div className="video-player-container">
      <video id="video-player" className="video-js" />
      <QualitySelector 
        qualities={video?.qualities || []} 
        current={quality}
        onChange={setQuality}
      />
    </div>
  );
};

// Video Upload Component
const VideoUploadForm: React.FC = () => {
  const [file, setFile] = useState<File | null>(null);
  const [title, setTitle] = useState('');
  const [description, setDescription] = useState('');
  const [uploadProgress, setUploadProgress] = useState(0);
  const uploadMutation = useUploadVideo();

  const handleFileSelect = (selectedFile: File) => {
    setFile(selectedFile);
  };

  const handleUpload = async () => {
    if (!file) return;
    
    const formData = new FormData();
    formData.append('video', file);
    formData.append('title', title);
    formData.append('description', description);

    uploadMutation.mutate(formData, {
      onUploadProgress: (progressEvent) => {
        const progress = Math.round(
          (progressEvent.loaded * 100) / progressEvent.total
        );
        setUploadProgress(progress);
      }
    });
  };

  return (
    <div className="upload-form">
      <FileDropzone onFileSelect={handleFileSelect} />
      <input 
        type="text" 
        placeholder="Video Title"
        value={title}
        onChange={(e) => setTitle(e.target.value)}
      />
      <textarea 
        placeholder="Description"
        value={description}
        onChange={(e) => setDescription(e.target.value)}
      />
      {uploadProgress > 0 && (
        <ProgressBar progress={uploadProgress} />
      )}
      <button onClick={handleUpload} disabled={!file || uploadMutation.isLoading}>
        {uploadMutation.isLoading ? 'Uploading...' : 'Upload Video'}
      </button>
    </div>
  );
};
```

### ii) State Management

**State Management Strategy:**

- **Local State (useState)**: Form inputs, UI state (loading, errors, modals, player state)
- **Component State**: Each component manages its own UI state
- **API State**: React Query or SWR for server state (video data, search results, comments) - caching, refetching, optimistic updates
- **Global State (Redux Toolkit)**: User authentication, watch history, playlists, subscriptions

**Frontend Implementation:**

```typescript
// Using React Query for API state management
import { useQuery, useMutation, useQueryClient } from '@tanstack/react-query';

const useVideo = (videoId: string) => {
  return useQuery({
    queryKey: ['video', videoId],
    queryFn: async () => {
      const response = await axios.get(`/api/v1/videos/${videoId}`);
      return response.data;
    },
    staleTime: 5 * 60 * 1000 // Cache for 5 minutes
  });
};

const useUploadVideo = () => {
  const queryClient = useQueryClient();
  
  return useMutation({
    mutationFn: async (formData: FormData) => {
      const response = await axios.post('/api/v1/videos/upload', formData, {
        headers: { 'Content-Type': 'multipart/form-data' },
        onUploadProgress: (progressEvent) => {
          // Handle upload progress
        }
      });
      return response.data;
    },
    onSuccess: () => {
      // Invalidate videos list
      queryClient.invalidateQueries({ queryKey: ['videos'] });
    }
  });
};
```

### iii) Implementation Details

**Data Flow:**

1. **Video Browsing** → HomePage fetches videos via React Query, displays VideoCard components
2. **Video Selection** → User clicks VideoCard, navigates to WatchPage with VideoPlayer
3. **Video Upload** → UploadPage handles file upload with progress tracking
4. **Comments** → CommentsSection displays and allows adding comments
5. **Watch History** → Video views tracked and stored in Redux/backend

**Event Handling:**

- Video search triggers debounced API call with autocomplete
- Video upload tracks progress and updates UI
- Video player controls handle play/pause/seek
- Comments update optimistically with server sync
- Real-time view count updates via WebSocket or polling

### UI/UX Considerations

- **Loading States**: Show skeleton loaders for video grids, spinners for uploads
- **Error Handling**: Display user-friendly error messages with retry options
- **Validation**: Client-side validation for uploads (file size, format)
- **Responsive Design**: Mobile-first layout, adaptive video player sizing
- **Accessibility**: ARIA labels, keyboard shortcuts for player, screen reader support
- **Performance**: Lazy loading for video thumbnails, code splitting per route, video preloading

---

## Data Models

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

## Data APIs

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

## b) Backend

### i) Services

**Video Service:**

```typescript
export class VideoService {
  async uploadVideo(userId: string, file: File, metadata: VideoMetadata): Promise<Video> {
    // Upload video to S3
    const videoKey = `videos/${userId}/${Date.now()}-${file.name}`;
    await this.s3Client.upload(file, videoKey);
    
    // Create video record
    const video = await Video.create({
      ...metadata,
      channelId: userId,
      videoUrl: this.getCDNUrl(videoKey),
      status: 'processing'
    });
    
    // Queue processing job
    await this.processingQueue.add({ videoId: video.id, videoUrl: video.videoUrl });
    
    return video;
  }

  async getVideo(videoId: string): Promise<Video> {
    // Check cache first
    const cached = await this.redis.get(`video:${videoId}`);
    if (cached) return JSON.parse(cached);
    
    // Query database
    const video = await Video.findById(videoId);
    await this.redis.setex(`video:${videoId}`, 300, JSON.stringify(video));
    
    return video;
  }

  async getFeed(userId: string, offset: number, limit: number): Promise<Video[]> {
    // Generate personalized feed based on user preferences
    // Check cache, query database, return videos
  }
}
```

**Video Processing Service:**

```typescript
export class VideoProcessingService {
  async processVideo(videoId: string, videoUrl: string): Promise<void> {
    // Download video from S3
    const videoBuffer = await this.downloadFromS3(videoUrl);
    
    // Transcode into multiple qualities
    const qualities = ['360p', '720p', '1080p', '4K'];
    for (const quality of qualities) {
      const transcoded = await this.transcode(videoBuffer, quality);
      await this.uploadToS3(`videos/${videoId}/${quality}.mp4`, transcoded);
    }
    
    // Generate thumbnails
    const thumbnails = await this.generateThumbnails(videoBuffer);
    for (const thumbnail of thumbnails) {
      await this.uploadToS3(`thumbnails/${videoId}/${thumbnail.timestamp}.jpg`, thumbnail.buffer);
    }
    
    // Update video status
    await Video.updateOne({ id: videoId }, { status: 'ready' });
    
    // Index in Elasticsearch
    await this.searchService.indexVideo(videoId);
  }
}
```

**Comment Service:**

```typescript
export class CommentService {
  async addComment(videoId: string, userId: string, text: string, parentId?: string): Promise<Comment> {
    const comment = await Comment.create({
      videoId,
      userId,
      text,
      parentId,
      createdAt: new Date()
    });
    
    // Update comment count
    await Video.updateOne({ id: videoId }, { $inc: { commentCount: 1 } });
    
    return comment;
  }

  async getComments(videoId: string, offset: number, limit: number): Promise<Comment[]> {
    return await Comment.find({ videoId, parentId: null })
      .sort({ createdAt: -1 })
      .skip(offset)
      .limit(limit)
      .populate('userId', 'name avatar');
  }
}
```

### ii) Server Structure

**Express.js Server Structure:**

```
server/
├── routes/
│   ├── videos.js          # Video routes
│   ├── comments.js        # Comment routes
│   ├── playlists.js       # Playlist routes
│   └── users.js           # User routes
├── controllers/
│   ├── VideoController.js
│   ├── CommentController.js
│   └── PlaylistController.js
├── services/
│   ├── VideoService.js
│   ├── VideoProcessingService.js
│   ├── CommentService.js
│   └── RecommendationService.js
├── workers/
│   └── videoProcessor.js  # FFmpeg video processing worker
├── models/
│   ├── Video.js
│   ├── Comment.js
│   └── Playlist.js
├── middleware/
│   ├── auth.js
│   ├── upload.js
│   └── validation.js
└── utils/
    ├── s3.js              # S3 client utilities
    ├── ffmpeg.js          # FFmpeg utilities
    └── cache.js           # Redis utilities
```

### iii) Implementation Details

**Video Upload Implementation:**
- Multipart upload to S3 with progress tracking
- Queue video processing job after upload
- Update video status throughout processing pipeline

**Video Processing Implementation:**
- FFmpeg transcoding into multiple quality formats
- Thumbnail generation at key timestamps
- HLS/DASH manifest generation for adaptive streaming
- Error handling and retry logic for failed processing

**Video Playback Implementation:**
- Video.js player with HLS/DASH support
- Adaptive bitrate streaming based on network conditions
- Quality selector for manual quality selection
- Playback analytics tracking (watch time, completion rate)

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

## Protocols

### REST API Protocol

- **Protocol:** REST (Representational State Transfer)

- **Data Format:** JSON

- **Authentication:** JWT Bearer token

### Video Streaming Protocol

- **Protocol:** HLS (HTTP Live Streaming) / DASH (Dynamic Adaptive Streaming)

- **Format:** M3U8 playlists with video segments

- **Adaptive Bitrate:** Multiple quality versions (360p, 720p, 1080p, 4K)

### CDN Protocol

- **Provider:** AWS CloudFront / Cloudflare

- **Content:** Video segments, thumbnails, static assets

- **Caching:** Long TTL for video segments

---

## Performance Optimizations

**Frontend Optimizations:** React.js code splitting, lazy loading, video preloading
**Backend Optimizations:** Database indexing, Redis caching, CDN for videos

### Video Streaming Optimization

- **Adaptive Bitrate Streaming:** Serve different quality versions based on network

- **CDN Delivery:** Serve videos from CloudFront CDN for global delivery

- **Video Preloading:** Preload next video in playlist

- **Thumbnail Optimization:** Lazy load thumbnails, use WebP format

---

## Testing Strategy

### Frontend Testing (React.js)

**Unit Testing:**

- **Jest + React Testing Library** - Test components, video player, playlist functionality

- **Video Player Testing** - Test video playback, controls, quality switching

- **Mocking:** Mock video APIs, CDN, browser video APIs

**Integration Testing:**

- **Video Upload Flow** - Test complete upload process

- **Playlist Management** - Test playlist creation and management

- **Search Integration** - Test search functionality

**E2E Testing:**

- **Cypress / Playwright** - Test video streaming flows

- **Test Scenarios:** Video upload, playback, playlist creation, search

### Backend Testing (Node.js/Express.js)

**Unit Testing:**

- **Jest + Supertest** - Test API endpoints, video processing

- **FFmpeg Testing** - Test video transcoding logic

- **Mocking:** Mock AWS S3, CDN, FFmpeg

**Integration Testing:**

- **MongoDB Memory Server** - Test database operations

- **Redis Mock** - Test caching logic

- **Video Processing Tests** - Test transcoding pipeline

**Load Testing:**

- **Artillery / k6** - Test video streaming under load

- **CDN Load Testing** - Test CDN performance

---

## Deployment & DevOps

### Frontend Deployment

**Build Process:**

- **Production Build:** Optimized bundle with code splitting

- **Video Player Optimization:** Lazy load video player components

- **CDN Deployment:** Deploy static assets to CloudFront

**Deployment Platforms:**

- **Vercel / Netlify** - Automatic deployments

- **AWS S3 + CloudFront** - Static site hosting with CDN

### Backend Deployment

**Server Setup:**

- **PM2:** Process manager with clustering

- **Nginx:** Load balancer and reverse proxy

- **Docker:** Containerized deployment

**Video Processing:**

- **FFmpeg Workers:** Separate workers for video transcoding

- **Queue System:** Process video uploads asynchronously

- **CDN Integration:** Upload transcoded videos to CDN

**CI/CD Pipeline:**

- **Automated Testing:** Run tests before deployment

- **Zero-Downtime:** Rolling deployment strategy

- **Health Checks:** Verify video streaming endpoints

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
AWS_ACCESS_KEY_ID=xxx
AWS_SECRET_ACCESS_KEY=xxx
AWS_S3_BUCKET=xxx
CLOUDFRONT_DOMAIN=xxx
ELASTICSEARCH_URL=xxx

```

---

## Database Migrations & Seeding

### MongoDB Migrations

**Migration Scripts:**

- **Schema Changes:** Add indexes for video queries

- **Data Migrations:** Update video metadata formats

- **Index Optimization:** Add compound indexes for search

### Data Seeding

**Seed Data:**

- **Video Categories:** Seed video categories

- **Test Videos:** Seed test video metadata

- **User Accounts:** Seed test accounts

---

## API Documentation

### Swagger/OpenAPI

**API Documentation:**

- **Swagger UI:** Document REST APIs

- **Video API:** Document video upload, streaming endpoints

- **Search API:** Document search endpoints

---

## API Versioning

**Versioning Strategy:**

- **URL Versioning:** `/api/v1/videos`, `/api/v2/videos`

- **Header Versioning:** `Accept: application/vnd.api+json;version=1`

- **Backward Compatibility:** Maintain old API versions for existing clients

---

## Monitoring & Logging

### Application Monitoring

**Frontend:**

- **Error Tracking:** Sentry for video player errors

- **Performance:** Track video loading times

- **User Analytics:** Track video engagement

**Backend:**

- **APM:** Monitor video processing performance

- **CDN Monitoring:** Track CDN performance

- **Video Metrics:** Track upload, transcoding, streaming metrics

### Logging

**Structured Logging:**

- **Winston / Pino:** Log video operations

- **Video Events:** Log upload, transcoding, streaming events

- **Error Logging:** Detailed error logs with context

---

## Database Transactions & Consistency

### MongoDB Transactions

**Transaction Usage:**

- **Multi-Document Transactions** - For operations requiring ACID guarantees

- **Example:** Video upload + metadata creation + user update

- **Session Management:** Use MongoDB sessions for transaction control

**Example:**

```typescript
const session = await mongoose.startSession();
session.startTransaction();
try {
  await Video.create([videoData], { session });
  await User.updateOne({ userId }, { $inc: { videoCount: 1 } }, { session });
  await Category.updateOne({ categoryId }, { $inc: { videoCount: 1 } }, { session });
  await session.commitTransaction();
} catch (error) {
  await session.abortTransaction();
  throw error;
} finally {
  session.endSession();
}

```

### Optimistic Locking

**Version Field:**

- **Version Field:** Add `version` field to video documents

- **Conflict Detection:** Check version before update

- **Retry Logic:** Retry on version conflict

### Consistency Strategies

**Data Consistency:**

- **Video Metadata Consistency:** Use transactions for video operations

- **View Count Consistency:** Use transactions for view count updates

- **Playlist Consistency:** Ensure playlist updates are atomic

---

## Third-Party Service Integration

### AWS S3 Integration

**File Storage:**

- **Video Upload:** Upload original videos to S3

- **Transcoded Videos:** Store transcoded versions in S3

- **Thumbnails:** Store video thumbnails in S3

- **Access Control:** Signed URLs for video access

### CloudFront CDN Integration

**Content Delivery:**

- **Video Streaming:** Serve videos from CloudFront

- **Cache Configuration:** Configure cache headers

- **Geographic Distribution:** Global CDN for low latency

### FFmpeg Integration

**Video Processing:**

- **Transcoding:** Convert videos to multiple formats

- **Thumbnail Generation:** Generate video thumbnails

- **Metadata Extraction:** Extract video metadata

### Elasticsearch Integration

**Search:**

- **Video Indexing:** Index video metadata

- **Search Queries:** Full-text search for videos

- **Autocomplete:** Video title autocomplete

---

# 3) Interview Answers

---

## Q1. Most complex technical challenge in building the video streaming platform

**Situation:** Building a video platform that handles video uploads (GB-sized files), video processing (transcoding to multiple qualities), video streaming to millions of users, search across millions of videos, and real-time features like comments and recommendations.

**Action:** The most complex challenge was implementing the video upload and processing pipeline that handles large files, transcodes to multiple qualities, and ensures reliable processing. **Backend (Node.js/Express.js):**, I implemented **multipart file upload** using Multer to handle large video files. I uploaded videos directly to **AWS S3** using multipart upload for large files. I created **video processing queue** using RabbitMQ - when video is uploaded, a processing job is queued. I implemented **FFmpeg workers** that consume from queue, download video from S3, transcode to multiple qualities (360p, 720p, 1080p, 4K), generate thumbnails, extract metadata, and upload processed videos back to S3. I used **CloudFront CDN** to serve videos globally. **Frontend (React.js):**, I implemented **upload progress tracking** with resumable uploads for large files. I created **video player** using Video.js with adaptive bitrate streaming.

**Result:** Successfully delivered a scalable video platform. Video uploads work for GB-sized files. Processing pipeline handles thousands of videos. CDN ensures fast global delivery. Video playback is smooth with adaptive streaming.

**Takeaway:** Video platforms require complex processing pipelines. Use queues for async processing. FFmpeg for transcoding. CDN for global delivery. Resumable uploads for large files. Adaptive streaming for best UX.

---

## Q2. Implementing video upload with progress tracking in React.js

**Situation:** Users needed to upload large video files (GBs) with progress tracking, resumable uploads, and proper error handling.

**Action:** I implemented comprehensive video upload system. **Frontend (React.js):**, I used **React Dropzone** for drag-and-drop file selection. I implemented **file validation** - check file size (max 10GB), format (MP4, MOV, AVI), and duration. I created **upload progress tracking** using XMLHttpRequest with progress events - show percentage, upload speed, time remaining. I implemented **resumable uploads** using AWS S3 multipart upload - if upload fails, resume from last chunk. I added **upload queue** - users can queue multiple videos. I implemented **error handling** with retry mechanism. **Backend (Node.js/Express.js):**, I created **upload endpoint** that generates presigned S3 URLs for direct upload. I implemented **upload completion webhook** - when upload completes, trigger processing job.

**Result:** Video upload works for large files. Progress tracking provides good UX. Resumable uploads handle network failures. Upload queue allows multiple uploads. User experience is excellent.

**Takeaway:** Large file uploads require special handling. Use multipart upload for resumability. Show progress for better UX. Validate files before upload. Queue system for multiple uploads.

---

## Q3. Implementing video processing pipeline using FFmpeg in Node.js

**Situation:** Uploaded videos needed to be transcoded to multiple qualities, thumbnails generated, and metadata extracted for playback and search.

**Action:** I implemented video processing pipeline using FFmpeg. I created **FFmpeg worker processes** that consume from RabbitMQ queue. When video is uploaded, processing job is queued with video URL. Worker **downloads video from S3** to temporary storage. I implemented **transcoding** using FFmpeg to generate multiple quality versions:

- 360p (mobile)

- 720p (standard)

- 1080p (HD)

- 4K (if source supports)

I generated **thumbnails** - extract frame at 10% of video duration, generate multiple sizes. I extracted **metadata** - duration, resolution, bitrate, codec using FFmpeg. I **uploaded processed videos** to S3 in organized structure (`videos/${userId}/${videoId}/${quality}.mp4`). I updated **video status in MongoDB** - processing → ready. I implemented **error handling** - if processing fails, retry up to 3 times, then mark as failed.

**Result:** Video processing pipeline works reliably. Multiple quality versions generated. Thumbnails created automatically. Processing time: 5-10 minutes for 10-minute video. System handles thousands of videos.

**Takeaway:** Video processing requires async workers. FFmpeg is powerful for transcoding. Generate multiple qualities for adaptive streaming. Thumbnails improve UX. Error handling is crucial.

---

## Q4. Implementing adaptive bitrate video streaming

**Situation:** Users have different network speeds and devices, requiring video quality to adapt automatically for smooth playback.

**Action:** I implemented adaptive bitrate streaming. I generated **multiple quality versions** of each video (360p, 720p, 1080p) during processing. I created **video manifest** (HLS or DASH) that lists all available qualities. I integrated **Video.js player** on frontend that supports adaptive streaming. I implemented **quality selection logic** - player monitors network speed and buffer, automatically switches quality. I used **CloudFront CDN** to serve video segments from edge locations. I implemented **segment-based delivery** - videos split into small segments (10 seconds), player requests segments as needed.

**Result:** Adaptive streaming provides smooth playback. Video quality adapts to network conditions. No buffering for users. CDN ensures fast delivery globally. User experience is excellent.

**Takeaway:** Adaptive streaming is essential for video platforms. Generate multiple qualities. Use CDN for global delivery. Monitor network and buffer. Segment-based delivery improves efficiency.

---

## Q5. Implementing video search using Elasticsearch

**Situation:** Users needed to search millions of videos by title, description, tags, and channel name with fast results.

**Action:** I implemented Elasticsearch for video search. I created **video index** in Elasticsearch with mappings:

- Title (boosted 3x for relevance)

- Description (boosted 2x)

- Tags

- Channel name

- Category

I implemented **indexing pipeline** - when video is published, index it in Elasticsearch. I created **search service** that builds Elasticsearch queries:

- Multi-match query across title, description, tags, channel

- Filters for category, duration, upload date

- Sort by relevance, views, upload date

- Highlight matching terms

I added **search autocomplete** using Elasticsearch completion suggester. I implemented **Redis caching** for popular search queries. I added **search analytics** to track popular searches.

**Result:** Video search is fast and accurate. Search latency < 200ms. System handles millions of videos. Autocomplete provides instant suggestions. Search results are relevant.

**Takeaway:** Elasticsearch is essential for video search. Proper field boosting improves relevance. Caching popular queries. Autocomplete enhances UX. Search analytics help optimization.

---

