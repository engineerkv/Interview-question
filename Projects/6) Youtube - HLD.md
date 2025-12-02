# Youtube - High Level Design (HLD)

> **Project Type:** Full-Stack Web Application (MERN Stack)  
> **Frontend:** React.js Web Application  
> **Backend:** Node.js, Express.js, MongoDB, REST APIs  
> **Tech Stack:** 
> - **Frontend:** React.js, TypeScript, React Router, Redux Toolkit, Axios, Material-UI
> - **Backend:** Node.js, Express.js, MongoDB, Redis, JWT
> - **Services:** AWS S3 (for video storage), CloudFront CDN (for video delivery), FFmpeg (for video processing)
> **Team Size:** 5-10 person team  
> **Built:** From scratch

---

## 1. Requirements

### a) Functional Requirements

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

### b) Non-Functional Requirements

#### Performance
- **Fast video loading** - Videos should start playing quickly - users expect instant playback
- **Adaptive streaming** - Video quality adjusts based on network speed - like Netflix
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

## 2. Scope & Priority

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

## 3. Tech Choices

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

## Architecture Overview

**Think of this as the big picture - how frontend and backend work together for video platform**

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

**How it works:**
1. **Frontend (React.js):** User watches videos, uploads videos, searches, manages playlists
2. **API Calls:** React app makes HTTP requests to backend API (using Axios)
3. **Backend (Node.js):** Express server receives request, processes business logic
4. **Video Upload:** Videos uploaded to S3, processing job queued
5. **Video Processing:** FFmpeg worker processes videos (transcoding, thumbnails)
6. **Video Playback:** Videos served from CloudFront CDN for fast global delivery
7. **Search:** Video search queries go to Elasticsearch for fast search
8. **Database:** Backend reads/writes data from MongoDB, caches in Redis
9. **Response:** Backend sends response back to frontend, React updates UI

---

## Key Design Decisions

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

