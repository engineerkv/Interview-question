# Social Media Feed

> **Project Type:** Full-Stack Web Application (MERN Stack)
> **Scale:** Handle millions of users, billions of posts, real-time updates for thousands of concurrent users
> **Tech Stack:** React.js, Node.js, Express.js, MongoDB, Redis, Socket.io, Elasticsearch, AWS S3

# 1) Problem Statement

Design and implement a social media feed system that addresses the following challenges:

- **Core Functionality**: Enable users to create posts, follow other users, and view personalized content feeds in real-time with seamless interactions
- **Scale Requirements**: Handle millions of users, billions of posts, and thousands of concurrent real-time connections
- **Performance**: Fast feed loading (< 1 second), smooth infinite scroll, optimized media handling
- **Feed Generation**: Generate personalized feeds efficiently based on user interests, following relationships, and engagement patterns
- **Real-time Updates**: Support real-time updates for likes, comments, shares, and new posts with low latency
- **Content Discovery**: Provide fast content discovery through trending feeds, explore features, and hashtag search
- **Media Handling**: Efficient storage and delivery of images and videos with optimization and CDN integration
- **Data Consistency**: Maintain data consistency for engagement metrics (likes, comments) across distributed systems

---

# 2) High Level Design (HLD)

## a) Requirements

### i) Functional Requirements

#### User Management

- **User registration and authentication** - Users can sign up with email, phone, or social login - makes it easy to get started

- **User profiles** - Users can customize profiles, upload profile picture, add bio

- **Follow system** - Users can follow other users, see their posts in feed

- **Friend requests** - Users can send and accept friend requests (for Facebook-like features)

#### Posts/Content

- **Create posts** - Users can create text posts, image posts, video posts

- **Edit/Delete posts** - Users can edit or delete their own posts

- **Post types** - Text, images, videos, links, polls

- **Post visibility** - Public, friends only, private

- **Hashtags** - Users can add hashtags to posts for discoverability

#### Feed

- **Home feed** - Personalized feed showing posts from followed users

- **Trending feed** - Show trending posts based on engagement

- **Explore feed** - Discover new content based on interests

- **Feed algorithms** - Rank posts by relevance, recency, engagement

- **Infinite scroll** - Load more posts as user scrolls

#### Interactions

- **Like/React** - Users can like posts, react with emojis (like, love, haha, wow, sad, angry)

- **Comments** - Users can comment on posts, reply to comments

- **Shares** - Users can share posts to their feed or send as message

- **Bookmarks** - Users can save posts to read later

- **Report** - Users can report inappropriate content

#### Real-time Features

- **Real-time notifications** - Get notified when someone likes, comments, or shares your post

- **Live updates** - See new posts in feed without refreshing

- **Typing indicators** - See when someone is typing a comment

- **Online status** - See when friends are online

#### Messaging (Optional)

- **Direct messages** - Users can send private messages to each other

- **Group messages** - Users can create group chats

- **Message notifications** - Get notified of new messages

### ii) Non-Functional Requirements

#### Performance

- **Fast feed loading** - Feed should load quickly - users expect instant content

- **Smooth scrolling** - Infinite scroll should be smooth, no lag

- **Image optimization** - Compress images, lazy load, use WebP format

- **Video optimization** - Optimize video uploads and playback

#### Scalability

- **Handle millions of users** - System should handle millions of users and posts

- **High concurrent users** - Support millions of concurrent users

- **Feed generation** - Generate personalized feeds efficiently

- **Database optimization** - Fast queries for feed generation

#### User Experience

- **Responsive design** - Works great on mobile, tablet, desktop

- **Smooth interactions** - Like, comment, share should feel instant

- **Fast search** - Search users, posts, hashtags quickly

- **Intuitive UI** - Easy to navigate, post, interact

#### Security

- **Content moderation** - Moderate posts and comments for inappropriate content

- **Spam detection** - Detect and prevent spam posts

- **Privacy controls** - Users can control who sees their posts

- **Secure uploads** - Validate and secure media uploads

---

## b) Scope and Priority

### Phase 1: MVP (Must Have) - Priority 1

**Core social media features - what users need to post and interact**

#### Functional

- **User authentication** - Sign up, login, user profiles

- **Create posts** - Text, image posts

- **Home feed** - Show posts from followed users

- **Basic interactions** - Like, comment on posts

- **Follow system** - Follow/unfollow users

- **Real-time notifications** - Get notified of interactions

#### Non-Functional

- **Performance** - Fast feed loading, smooth scrolling

- **Responsive** - Mobile-first design

- **Security** - Secure uploads, content moderation

### Phase 2: Enhanced Features - Priority 2

**Features that improve user experience and engagement**

#### Functional

- **Video posts** - Upload and watch video posts

- **Hashtags** - Add hashtags, explore by hashtags

- **Trending feed** - Show trending posts

- **Explore feed** - Discover new content

- **Bookmarks** - Save posts to read later

- **Advanced interactions** - React with emojis, share posts

#### Non-Functional

- **Feed algorithm** - Better feed ranking

- **Analytics** - Track user engagement

### Phase 3: Advanced Features - Priority 3

**Advanced features for power users**

#### Functional

- **Direct messaging** - Private messaging between users

- **Stories** - Temporary posts that disappear after 24 hours

- **Live streaming** - Live video streaming

- **Groups** - Create and join groups

- **Events** - Create and join events

---

## c) Technology Choices

### Frontend Framework

- **React.js:** Perfect for building interactive social media feed
  - **Component-based** - Post cards, comment sections are reusable
  - **Fast updates** - Virtual DOM makes feed updates smooth
  - **Code splitting** - Load pages only when needed
  - **TypeScript** - Type safety for posts, users, comments

### State Management

- **Redux Toolkit:** Manages complex state (posts, user, feed, notifications)
  - **Post state** - Current posts, feed, search results
  - **User state** - Authentication, profile, following list
  - **Feed state** - Home feed, trending feed, explore feed
  - **Notification state** - Real-time notifications

### Routing

- **React Router v6:** Client-side routing for smooth navigation
  - **Home feed** - `/` for home feed
  - **Profile pages** - `/profile/:userId` for user profiles
  - **Post pages** - `/post/:postId` for single post view
  - **Explore** - `/explore` for explore feed

### Real-time Communication

- **Socket.io Client:** Real-time updates for notifications and feed
  - **Why Socket.io?** Automatic reconnection, room-based messaging
  - **Notifications** - Real-time notification delivery
  - **Live updates** - See new posts without refreshing
  - **Typing indicators** - Show when someone is typing

### UI Components

- **Material-UI:** Pre-built components for faster development
  - **Post cards** - Consistent post display
  - **Forms** - Post creation forms, comment forms
  - **Modals** - Image viewer, video player
  - **Responsive grid** - Feed grid that adapts to screen size

### Backend Framework

- **Node.js + Express.js:** Backend server that handles all business logic
  - **Why Node.js?** JavaScript everywhere - same language for frontend and backend
  - **Express.js** - Fast, minimal web framework
  - **REST APIs** - Standard REST endpoints for frontend to call

### Database

- **MongoDB:** NoSQL database for storing posts, users, comments, interactions
  - **Why MongoDB?** Flexible schema - easy to change post structure
  - **Document-based** - Stores data as JSON-like documents
  - **Scalable** - Handles large amounts of posts and users

### Real-time Server

- **Socket.io Server:** WebSocket server for real-time communication
  - **Why Socket.io?** Handles real-time notifications and updates
  - **Room-based** - Users join notification rooms
  - **Automatic reconnection** - Handles connection drops gracefully

### Caching

- **Redis:** In-memory cache for frequently accessed data
  - **Feed cache** - Cache user feeds
  - **Post cache** - Cache popular posts
  - **Session storage** - User sessions

### Search

- **MongoDB Text Search / Elasticsearch:** Full-text search for posts and users
  - **MongoDB Text Search** - Good for basic search needs
  - **Elasticsearch** - Better for advanced search with ranking

### Media Storage

- **AWS S3:** Cloud storage for images and videos
  - **Why S3?** Scalable, reliable file storage
  - **CDN integration** - Serve media through CDN for faster access

---

## d) Capacity Estimation

### Throughput Requirements

- **Daily Active Users**: 10 million users per day
- **Peak Traffic**: 5x average during peak hours (50 million users per day)
- **Read:Write Ratio**: 100:1 (viewing feeds vs creating posts)
- **Average Posts Per User**: 2 posts per day

**Calculations:**
- **Average Writes Per Second (WPS)**: (10M users × 2 posts) / 86,400 seconds ≈ 231 WPS
- **Peak WPS**: 231 × 5 = 1,155 WPS
- **Average Reads Per Second (RPS)**: 231 × 100 = 23,100 RPS
- **Peak RPS**: 23,100 × 5 = 115,500 RPS
- **Real-time Connections**: 1 million concurrent WebSocket connections

### Storage Estimation

**Storage per Post:**
- Post metadata: 1 KB (text, author, timestamp, etc.)
- Post images: 500 KB average (1-3 images × 200 KB each)
- Post videos: 5 MB average (optional)
- **Total per Post**: ~1.5 KB (text) + 500 KB (images) = ~501.5 KB average

**Storage Requirements:**
- **Total Posts per Year**: 10M users × 2 posts/day × 365 = 7.3 billion posts
- **Post Storage**: 7.3B × 501.5 KB ≈ 3.66 PB per year
- **User Data**: 100M users × 10 KB ≈ 1 TB
- **Engagement Data**: 7.3B posts × 100 interactions × 100 bytes ≈ 73 TB/year
- **Total Storage**: ~3.66 PB (posts) + 1 TB (users) + 73 TB (engagement) ≈ 3.73 PB/year

### Bandwidth Estimation

- **Average Feed Page Size**: 2 MB (including images, posts, metadata)
- **Daily Bandwidth**: 10M users × 20 feed views × 2 MB = 400 TB/day
- **Peak Bandwidth**: 400 TB × 5 = 2 PB/day during peak hours
- **Average Bandwidth**: 400 TB / 86,400 seconds ≈ 4.6 GB/s
- **Peak Bandwidth**: 4.6 GB/s × 5 ≈ 23 GB/s

### Caching Estimation

Following the **80-20 rule** where 20% of posts generate 80% of traffic:
- **Cache 20% of hot posts**: 7.3B × 0.2 = 1.46B posts
- **Cache memory required**: 1.46B × 1.5 KB = 2.19 TB
- **Cache hit ratio**: 80% (only 20% of feed requests hit database)
- **Requests hitting DB**: 23,100 × 0.20 ≈ 4,620 RPS (manageable with proper indexing)

### Infrastructure Sizing

- **API Servers**: 50-100 instances behind load balancer, each handling 500-1,000 RPS
- **WebSocket Servers**: 20-30 instances for real-time connections, each handling 30,000-50,000 connections
- **Database**: MongoDB cluster with 20-30 nodes for storage and high read/write throughput
- **Cache Layer**: Redis cluster with 10-15 nodes for high availability and performance
- **Search**: Elasticsearch cluster with 10-15 nodes for content search
- **CDN**: CloudFront/Cloudflare for global media and static asset delivery

---

## e) Architecture Overview

The system follows a layered architecture with real-time capabilities for instant updates. Here's how the complete system works:

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
│  │  │  │  - Posts, User, Feed, Notifications │  │  │   │
│  │  │  └──────────────────────────────────────┘  │  │   │
│  │  │  ┌──────────────────────────────────────┐  │  │   │
│  │  │  │  Socket.io Client (Real-time)        │  │  │   │
│  │  │  │  - Receives notifications instantly  │  │  │   │
│  │  │  └──────────────────────────────────────┘  │  │   │
│  │  │  ┌──────────────────────────────────────┐  │  │   │
│  │  │  │  Material-UI Components              │  │  │   │
│  │  │  └──────────────────────────────────────┘  │  │   │
│  │  └────────────────────────────────────────────┘  │   │
│  └──────────────────────────────────────────────────┘   │
└─────────────────────────────────────────────────────────┘
        │                                    │
        │ HTTP/REST API                     │ WebSocket
        │ (Posts, actions)                  │ (Notifications)
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
│  │         Socket.io Server (Real-time)             │   │
│  │  - Handles WebSocket connections                 │   │
│  │  - Manages notification rooms                    │   │
│  │  - Broadcasts notifications                      │   │
│  └──────────────────────────────────────────────────┘   │
│                        ▼                                 │
│  ┌──────────────────────────────────────────────────┐   │
│  │         Business Logic Layer                     │   │
│  │  - Post Service (create, update, delete posts)   │   │
│  │  - Feed Service (generate personalized feeds)    │   │
│  │  - User Service (authentication, profiles)       │   │
│  │  - Interaction Service (likes, comments)         │   │
│  │  - Notification Service (send notifications)     │   │
│  └──────────────────────────────────────────────────┘   │
│                        ▼                                 │
│  ┌──────────────────────────────────────────────────┐   │
│  │         Data Access Layer                        │   │
│  │  - MongoDB (Posts, users, comments)              │   │
│  │  - Redis (Feed cache, sessions)                  │   │
│  │  - Elasticsearch (Post search)                   │   │
│  └──────────────────────────────────────────────────┘   │
└─────────────────────────────────────────────────────────┘
        │                    │                    │
        ▼                    ▼                    ▼
┌──────────────┐  ┌──────────────┐  ┌──────────────┐
│   MongoDB    │  │    Redis     │  │ Elasticsearch│
│  (Database)  │  │   (Cache)    │  │   (Search)   │
│              │  │              │  │              │
│  - Posts     │  │  - Feed      │  │  - Post      │
│  - Users     │  │    Cache     │  │    Index     │
│  - Comments  │  │  - Post      │  │  - Search    │
│  - Follows   │  │    Cache     │  │    Results   │
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
                    │  - CDN       │
                    └──────────────┘

```

### Frontend Architecture

**Frontend Layers:**

1. **Presentation Layer (React Components)**
   - **UI Components**: Reusable components (PostCard, CommentCard, LikeButton, ShareButton)
   - **Feature Components**: FeedList, PostCreator, CommentSection, NotificationPanel
   - **Layout Components**: Header, Sidebar, Navigation, MainLayout
   - **Page Components**: HomePage, ProfilePage, ExplorePage, NotificationPage

2. **State Management Layer**
   - **Local State (useState)**: Component-specific UI state (form inputs, loading, errors, modals)
   - **Server State (Redux Toolkit)**: Global state for posts, user, feed, notifications
   - **Real-time State (Socket.io)**: Live updates for notifications, new posts, engagement

3. **API Integration Layer**
   - **API Client**: Axios instance with interceptors for auth, error handling
   - **Redux Thunks**: Async actions for API operations (fetchFeed, createPost, likePost)
   - **Request/Response Transformation**: Data normalization and error handling

4. **Real-time Layer (Socket.io Client)**
   - **WebSocket Connection**: Persistent connection for real-time updates
   - **Event Handlers**: Listen for notifications, new posts, engagement updates
   - **Room Management**: Join user-specific rooms for targeted notifications

5. **Routing Layer (React Router)**
   - **Route Configuration**: Define routes and protected routes
   - **Navigation**: Programmatic and declarative navigation
   - **Route Guards**: Authentication and authorization checks

6. **Build & Deployment Layer**
   - **Build Process**: Webpack/Vite bundling with code splitting
   - **Static Assets**: Served from CDN (CloudFront/Cloudflare)
   - **Environment Configuration**: Environment-specific API endpoints and configs

**Frontend Request Flow:**

1. **User Interaction** → User scrolls feed or creates post
2. **State Update** → Redux action dispatched or Socket.io event received
3. **API Call** → Axios makes HTTP request to backend API (or WebSocket message)
4. **Loading State** → UI shows loading indicator
5. **Response Handling** → Success/error state updates Redux store
6. **Real-time Update** → Socket.io receives notification, updates UI instantly
7. **UI Update** → Components re-render with new data

### Backend Architecture

**Backend Layers:**

1. **API Gateway/Load Balancer** - Entry point for all HTTP requests
2. **WebSocket Gateway** - Entry point for all WebSocket connections
3. **API Server Layer** - Stateless servers handling HTTP requests
4. **WebSocket Server Layer** - Socket.io servers handling real-time connections
5. **Application Service Layer** - Business logic and orchestration
6. **Cache Layer** - In-memory caching for performance
7. **Database Layer** - Persistent data storage
8. **Search Layer** - Elasticsearch for content search
9. **External Services** - S3, CDN

### Complete Request Flow

**Feed Loading Flow:**
1. **Frontend**: User opens home feed
2. **Load Balancer**: Routes request to available API server
3. **API Server**: Validates request, extracts user ID
4. **Cache Check**: Check Redis for cached feed
5. **Feed Generation**: If cache miss, generate personalized feed from followed users
6. **Response**: Return feed posts to frontend
7. **Frontend**: Display posts with infinite scroll

**Post Creation Flow:**
1. **Frontend**: User creates post with text/image
2. **API Call**: POST request to create post API
3. **Backend**: Validate post, upload media to S3
4. **Database**: Store post in MongoDB
5. **Search Index**: Index post in Elasticsearch
6. **Real-time Broadcast**: Emit new post event via Socket.io to followers
7. **Response**: Return created post to frontend
8. **Frontend**: Add post to feed immediately (optimistic update)

**Like/Comment Flow:**
1. **Frontend**: User likes or comments on post
2. **API Call**: POST request to like/comment API
3. **Backend**: Update engagement in MongoDB
4. **Real-time Notification**: Emit notification via Socket.io to post author
5. **Response**: Return updated engagement count
6. **Frontend**: Update UI immediately (optimistic update)
7. **Real-time Update**: Other users see updated like count instantly

### Key Components

- **Frontend (React.js)**: Single-page application with client-side routing, component-based architecture, Redux for state management, Socket.io for real-time updates
- **CDN/Edge**: Global distribution of static assets and media, reduces latency
- **Load Balancer**: Distributes HTTP traffic across API servers, SSL/TLS termination
- **WebSocket Gateway**: Routes WebSocket connections to Socket.io servers
- **API Servers**: Stateless design for horizontal scaling, handle posts, feed, interactions
- **WebSocket Servers**: Socket.io servers for real-time connections, handle notifications and live updates
- **Application Services**: Post Service, Feed Service, User Service, Interaction Service, Notification Service
- **Cache Layer (Redis)**: In-memory cache for hot posts (20% of traffic), feed cache, sessions
- **Database (MongoDB)**: Sharded across multiple nodes for horizontal scaling, stores posts, users, comments, follows
- **Search (Elasticsearch)**: Fast full-text search for posts, handles hashtag search and content discovery
- **Media Storage (AWS S3)**: Stores post images and videos, served via CDN

6. **Database:** Backend reads/writes data from MongoDB, caches in Redis

7. **Media:** Images/videos uploaded to S3, served via CDN

8. **Response:** Backend sends response back to frontend, React updates UI

---

## Key Design Decisions

1. **React.js for Frontend:** Perfect for interactive social media - feed updates, likes, comments all need fast UI updates
   - **Component-based** - Post cards, comment sections are reusable
   - **Fast updates** - Virtual DOM makes feed updates smooth
   - **Code splitting** - Load pages only when needed

2. **Socket.io for Real-time:** Real-time notifications and live updates - essential for social media
   - **Why Socket.io?** Automatic reconnection, room-based messaging
   - **Notifications** - Users get instant notifications
   - **Live updates** - See new posts without refreshing

3. **Feed Generation Algorithm:** Personalized feeds based on user interests and engagement
   - **Why important?** Users see relevant content, increases engagement
   - **Ranking** - Posts ranked by relevance, recency, engagement
   - **Caching** - Cache feeds in Redis for fast retrieval

4. **Infinite Scroll:** Load more posts as user scrolls - better UX than pagination
   - **Why infinite scroll?** Users can continuously browse, no need to click next page
   - **Performance** - Load posts in batches, lazy load images
   - **Smooth scrolling** - No lag, smooth experience

5. **MongoDB for Posts:** Flexible schema for different post types - text, images, videos
   - **Why MongoDB?** Easy to add new post types and fields
   - **Scalable** - Handles millions of posts
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
│   │   ├── SearchBar
│   │   ├── NavigationMenu (Home, Explore, Notifications, Messages)
│   │   └── UserMenu (Profile, Settings, Logout)
│   └── Main Content Area
│       ├── HomePage
│       │   ├── CreatePostCard
│       │   │   ├── PostInput (text, image, video)
│       │   │   ├── MediaUpload
│       │   │   └── PostButton
│       │   ├── Feed
│       │   │   └── PostCard
│       │   │       ├── PostHeader (User info, timestamp)
│       │   │       ├── PostContent (Text, images, video)
│       │   │       ├── PostActions
│       │   │       │   ├── LikeButton
│       │   │       │   ├── CommentButton
│       │   │       │   ├── ShareButton
│       │   │       │   └── BookmarkButton
│       │   │       ├── LikeCount
│       │   │       ├── CommentsSection
│       │   │       │   ├── CommentInput
│       │   │       │   └── CommentList
│       │   │       │       └── CommentItem
│       │   │       └── ShareCount
│       │   └── InfiniteScrollTrigger
│       ├── ProfilePage
│       │   ├── ProfileHeader
│       │   │   ├── CoverPhoto
│       │   │   ├── ProfilePicture
│       │   │   ├── UserName
│       │   │   ├── Bio
│       │   │   └── FollowButton
│       │   ├── ProfileTabs (Posts, About, Photos, Videos)
│       │   └── PostGrid
│       ├── PostDetailPage
│       │   ├── PostCard (full post)
│       │   └── CommentsSection (expanded)
│       ├── ExplorePage
│       │   ├── TrendingHashtags
│       │   ├── TrendingPosts
│       │   └── SuggestedUsers
│       └── NotificationsPage
│           ├── NotificationList
│           │   └── NotificationItem
│           └── MarkAllAsReadButton
└── ReduxProvider (Global State Management)
    └── Store
        ├── authSlice (User authentication state)
        ├── postSlice (Posts data)
        ├── feedSlice (Feed data)
        ├── notificationSlice (Notifications)
        └── userSlice (User profile data)

```

---

```
App (Root Component - Entry Point)
├── Layout (Main Layout with Navigation)
│   ├── Header
│   │   ├── Logo
│   │   ├── SearchBar
│   │   ├── NavigationMenu (Home, Explore, Notifications, Messages)
│   │   └── UserMenu (Profile, Settings, Logout)
│   └── Main Content Area
│       ├── HomePage
│       │   ├── CreatePostCard
│       │   │   ├── PostInput (text, image, video)
│       │   │   ├── MediaUpload
│       │   │   └── PostButton
│       │   ├── Feed
│       │   │   └── PostCard
│       │   │       ├── PostHeader (User info, timestamp)
│       │   │       ├── PostContent (Text, images, video)
│       │   │       ├── PostActions
│       │   │       │   ├── LikeButton
│       │   │       │   ├── CommentButton
│       │   │       │   ├── ShareButton
│       │   │       │   └── BookmarkButton
│       │   │       ├── LikeCount
│       │   │       ├── CommentsSection
│       │   │       │   ├── CommentInput
│       │   │       │   └── CommentList
│       │   │       │       └── CommentItem
│       │   │       └── ShareCount
│       │   └── InfiniteScrollTrigger
│       ├── ProfilePage
│       │   ├── ProfileHeader
│       │   │   ├── CoverPhoto
│       │   │   ├── ProfilePicture
│       │   │   ├── UserName
│       │   │   ├── Bio
│       │   │   └── FollowButton
│       │   ├── ProfileTabs (Posts, About, Photos, Videos)
│       │   └── PostGrid
│       └── ExplorePage
│           ├── TrendingHashtags
│           ├── TrendingPosts
│           └── SuggestedUsers
└── ReduxProvider (Global State Management)
    └── Store
        ├── authSlice (User authentication state)
        ├── postSlice (Posts data)
        ├── feedSlice (Feed data)
        └── notificationSlice (Notifications)
```

### Key React Components

**Frontend Implementation:**

```typescript
// Post Card Component
const PostCard: React.FC<{ post: Post }> = ({ post }) => {
  const dispatch = useAppDispatch();
  const [showComments, setShowComments] = useState(false);
  const { data: comments } = useComments(post.id);

  const handleLike = async () => {
    dispatch(likePost(post.id));
    // Optimistic update
  };

  const handleComment = async (commentText: string) => {
    dispatch(addComment({ postId: post.id, text: commentText }));
  };

  return (
    <div className="post-card">
      <PostHeader user={post.user} timestamp={post.createdAt} />
      <PostContent content={post.content} media={post.media} />
      <PostActions
        likes={post.likes}
        comments={post.comments}
        shares={post.shares}
        onLike={handleLike}
        onComment={() => setShowComments(!showComments)}
        onShare={handleShare}
      />
      {showComments && (
        <CommentsSection
          comments={comments}
          onAddComment={handleComment}
        />
      )}
    </div>
  );
};

// Create Post Component
const CreatePostCard: React.FC = () => {
  const [text, setText] = useState('');
  const [media, setMedia] = useState<File[]>([]);
  const createPostMutation = useCreatePost();

  const handleSubmit = async () => {
    const formData = new FormData();
    formData.append('text', text);
    media.forEach(file => formData.append('media', file));

    createPostMutation.mutate(formData);
    setText('');
    setMedia([]);
  };

  return (
    <div className="create-post-card">
      <textarea
        value={text}
        onChange={(e) => setText(e.target.value)}
        placeholder="What's on your mind?"
      />
      <MediaUpload files={media} onFilesChange={setMedia} />
      <button onClick={handleSubmit} disabled={!text.trim() && media.length === 0}>
        Post
      </button>
    </div>
  );
};
```

### ii) State Management

**State Management Strategy:**

- **Local State (useState)**: Form inputs, UI state (loading, errors, modals, show/hide comments)
- **Component State**: Each component manages its own UI state
- **API State**: React Query or SWR for server state (posts, feed, comments) - caching, refetching, optimistic updates
- **Global State (Redux Toolkit)**: User authentication, feed data, notifications, selected post

**Frontend Implementation:**

```typescript
// Using React Query for API state management
import { useQuery, useMutation, useQueryClient } from '@tanstack/react-query';

const useFeed = () => {
  return useInfiniteQuery({
    queryKey: ['feed'],
    queryFn: async ({ pageParam = 0 }) => {
      const response = await axios.get('/api/v1/feed', {
        params: { offset: pageParam, limit: 20 }
      });
      return response.data;
    },
    getNextPageParam: (lastPage, pages) => {
      return lastPage.hasMore ? pages.length * 20 : undefined;
    }
  });
};

const useCreatePost = () => {
  const queryClient = useQueryClient();
  
  return useMutation({
    mutationFn: async (formData: FormData) => {
      const response = await axios.post('/api/v1/posts', formData, {
        headers: { 'Content-Type': 'multipart/form-data' }
      });
      return response.data;
    },
    onSuccess: () => {
      // Invalidate feed to show new post
      queryClient.invalidateQueries({ queryKey: ['feed'] });
    }
  });
};
```

### iii) Implementation Details

**Data Flow:**

1. **Feed Loading** → HomePage fetches feed via React Query infinite query, displays PostCard components
2. **Post Creation** → CreatePostCard submits post, optimistically updates feed
3. **Post Interactions** → Like/Comment actions update Redux state and sync with backend
4. **Real-time Updates** → Socket.io receives new posts/comments, updates feed in real-time
5. **Infinite Scroll** → User scrolls to bottom, triggers next page fetch

**Event Handling:**

- Post creation triggers optimistic update
- Like/Comment actions update immediately with server sync
- Real-time notifications via Socket.io
- Infinite scroll loads more posts automatically
- Media upload shows progress

### UI/UX Considerations

- **Loading States**: Show skeleton loaders for feed, spinners for actions
- **Error Handling**: Display user-friendly error messages with retry options
- **Validation**: Client-side validation for post content and media
- **Responsive Design**: Mobile-first layout, optimized for touch interactions
- **Accessibility**: ARIA labels, keyboard navigation, screen reader support
- **Performance**: Virtual scrolling for long feeds, image lazy loading, code splitting per route

---

## Data Models

### Post Model

```typescript
interface Post {
  id: string;
  userId: string;
  userName: string;
  userAvatar: string;
  content: string;
  type: 'text' | 'image' | 'video' | 'link' | 'poll';
  media?: string[];        // Array of media URLs
  hashtags: string[];
  mentions: string[];      // Array of mentioned user IDs
  likes: number;
  comments: number;
  shares: number;
  visibility: 'public' | 'friends' | 'private';
  createdAt: Date;
  updatedAt: Date;
}

```

### Comment Model

```typescript
interface Comment {
  id: string;
  postId: string;
  userId: string;
  userName: string;
  userAvatar: string;
  text: string;
  likes: number;
  replies: Comment[];      // Nested comments
  createdAt: Date;
}

```

### Feed Model

```typescript
interface Feed {
  userId: string;
  posts: string[];         // Array of post IDs
  lastUpdated: Date;
}

```

---

## Data APIs

**Note:** All API endpoints are implemented on the **backend (Node.js/Express)**, and the **frontend (React.js)** calls these APIs using Axios. Real-time updates use **Socket.io**.

### Post APIs

**Backend Implementation:** Express.js routes handle post logic
**Frontend Implementation:** React components call these APIs and display posts

#### GET /api/feed

- **URL:** `/api/feed?page=1&limit=20`

- **Method:** GET

- **Authentication:** Required

- **Response:**
  ```json
  {
    "success": true,
    "data": {
      "posts": [/* Post objects */],
      "hasMore": true,
      "nextPage": 2
    }
  }
  ```

#### POST /api/posts

- **URL:** `/api/posts`

- **Method:** POST

- **Request Body:**
  ```json
  {
    "content": "Hello world!",
    "type": "text",
    "hashtags": ["hello", "world"],
    "visibility": "public"
  }
  ```

#### POST /api/posts/:id/like

- **URL:** `/api/posts/123/like`

- **Method:** POST

- **Description:** Like or unlike a post

#### POST /api/posts/:id/comment

- **URL:** `/api/posts/123/comment`

- **Method:** POST

- **Request Body:**
  ```json
  {
    "text": "Great post!"
  }
  ```

---

## b) Backend

### i) Services

### Feed Generation Algorithm

**Backend (Express.js):**

```typescript
// Backend: services/feedService.ts
export class FeedService {
  async generateFeed(userId: string, page: number, limit: number): Promise<Post[]> {
    // Get user's following list
    const following = await this.getFollowing(userId);
    const followingIds = following.map(f => f.userId);

    // Get cached feed if available
    const cachedFeed = await redis.get(`feed:${userId}`);
    if (cachedFeed) {
      const postIds = JSON.parse(cachedFeed);
      const posts = await Post.find({ id: { $in: postIds } })
        .sort({ createdAt: -1 })
        .skip((page - 1) * limit)
        .limit(limit);
      return posts;
    }

    // Generate feed based on algorithm
    const posts = await Post.find({
      userId: { $in: followingIds },
      visibility: { $in: ['public', 'friends'] }
    })
    .sort({
      // Rank by engagement score
      score: -1,
      createdAt: -1
    })
    .limit(limit * 3); // Get more posts for ranking

    // Calculate engagement score
    const rankedPosts = posts.map(post => ({
      ...post,
      score: this.calculateEngagementScore(post)
    })).sort((a, b) => b.score - a.score)
    .slice(0, limit);

    // Cache feed
    await redis.setex(
      `feed:${userId}`,
      300, // 5 minutes
      JSON.stringify(rankedPosts.map(p => p.id))
    );

    return rankedPosts;
  }

  private calculateEngagementScore(post: Post): number {
    const timeDecay = Math.exp(-(Date.now() - post.createdAt.getTime()) / (1000 * 60 * 60 * 24));
    const engagement = (post.likes * 1) + (post.comments * 2) + (post.shares * 3);
    return engagement * timeDecay;
  }
}

```

### Real-time Notifications

**Backend (Socket.io Server):**

```typescript
// Backend: socket.io server
io.on('connection', (socket) => {
  const userId = socket.handshake.auth.userId;

  // Join user's notification room
  socket.join(`user:${userId}`);

  // Handle like event
  socket.on('post:like', async (data) => {
    const { postId } = data;
    const post = await Post.findById(postId);

    // Send notification to post owner
    io.to(`user:${post.userId}`).emit('notification', {
      type: 'like',
      message: `${userId} liked your post`,
      postId
    });
  });
});

```

### ii) Server Structure

**Express.js Server Structure:**

```
server/
├── routes/
│   ├── posts.js          # Post routes
│   ├── feed.js           # Feed routes
│   ├── users.js          # User routes
│   └── interactions.js   # Like, comment routes
├── controllers/
│   ├── PostController.js
│   ├── FeedController.js
│   └── InteractionController.js
├── services/
│   ├── PostService.js
│   ├── FeedService.js
│   ├── NotificationService.js
│   └── SearchService.js
├── models/
│   ├── Post.js
│   ├── User.js
│   └── Comment.js
├── middleware/
│   ├── auth.js
│   ├── upload.js
│   └── validation.js
└── utils/
    ├── socket.js         # Socket.io setup
    └── cache.js          # Redis utilities
```

### iii) Implementation Details

### Infinite Scroll Feed

**Frontend (React.js):**

```typescript
// Frontend: components/Feed.tsx
import { useInfiniteQuery } from '@tanstack/react-query';

const Feed: React.FC = () => {
  const {
    data,
    fetchNextPage,
    hasNextPage,
    isFetchingNextPage
  } = useInfiniteQuery({
    queryKey: ['feed'],
    queryFn: ({ pageParam = 1 }) => fetchFeed(pageParam),
    getNextPageParam: (lastPage) => lastPage.hasMore ? lastPage.nextPage : undefined
  });

  const posts = data?.pages.flatMap(page => page.posts) || [];

  return (
    <div>
      {posts.map(post => (
        <PostCard key={post.id} post={post} />
      ))}
      {hasNextPage && (
        <button onClick={() => fetchNextPage()}>
          {isFetchingNextPage ? 'Loading...' : 'Load More'}
        </button>
      )}
    </div>
  );
};

```

### Real-time Notifications

**Frontend (Socket.io Client):**

```typescript
// Frontend: hooks/useNotifications.ts
import { useEffect } from 'react';
import { io } from 'socket.io-client';
import { useDispatch } from 'react-redux';
import { addNotification } from '../store/notificationSlice';

export const useNotifications = (userId: string) => {
  const dispatch = useDispatch();

  useEffect(() => {
    const socket = io(process.env.REACT_APP_SOCKET_URL, {
      auth: { userId }
    });

    socket.on('notification', (notification) => {
      dispatch(addNotification(notification));
      // Show browser notification
      if ('Notification' in window && Notification.permission === 'granted') {
        new Notification(notification.message);
      }
    });

    return () => {
      socket.disconnect();
    };
  }, [userId, dispatch]);
};

```

---

## Protocols

### REST API Protocol

- **Protocol:** REST (Representational State Transfer)

- **Data Format:** JSON

- **Authentication:** JWT Bearer token

### WebSocket Protocol

- **Protocol:** Socket.io over WebSocket

- **Events:** `post:new`, `like:new`, `comment:new`, `feed:update`

- **Authentication:** JWT token in handshake

### Message Queue Protocol

- **Queue System:** RabbitMQ/Kafka

- **Purpose:** Fan-out posts to followers' feeds

- **Message Format:** JSON

---

## Performance Optimizations

**Frontend Optimizations:** React.js code splitting, lazy loading, infinite scroll
**Backend Optimizations:** Database indexing, Redis caching, feed pre-computation

### Feed Optimization

- **Feed Caching:** Cache user feeds in Redis for fast retrieval

- **Feed Pre-computation:** Pre-compute feeds for active users

- **Lazy Loading:** Load images as user scrolls

- **Virtual Scrolling:** For very long feeds

---

## Testing Strategy

### Frontend Testing (React.js)

**Unit Testing:**

- **Jest + React Testing Library** - Test components, feed, post creation

- **Feed Component Testing** - Test infinite scroll, post rendering

- **Mocking:** Mock API calls, Socket.io, image uploads

**Integration Testing:**

- **Feed Integration** - Test feed loading and pagination

- **Post Creation Flow** - Test complete post creation

- **Real-time Updates** - Test Socket.io integration

**E2E Testing:**

- **Cypress / Playwright** - Test social media flows

- **Test Scenarios:** Post creation, feed loading, likes, comments, real-time updates

### Backend Testing (Node.js/Express.js)

**Unit Testing:**

- **Jest + Supertest** - Test API endpoints, feed generation

- **Feed Algorithm Testing** - Test feed ranking logic

- **Mocking:** Mock MongoDB, Redis, Socket.io

**Integration Testing:**

- **MongoDB Memory Server** - Test database operations

- **Redis Mock** - Test caching and feed generation

- **Socket.io Testing** - Test real-time notifications

**Load Testing:**

- **Artillery / k6** - Test feed generation under load

- **Concurrent Users:** Test feed performance with high concurrency

---

## Deployment & DevOps

### Frontend Deployment

**Build Process:**

- **Production Build:** Optimized bundle with code splitting

- **Image Optimization:** Optimize images for web

- **CDN Deployment:** Deploy static assets to CDN

**Deployment Platforms:**

- **Vercel / Netlify** - Automatic deployments

- **AWS S3 + CloudFront** - Static site hosting with CDN

### Backend Deployment

**Server Setup:**

- **PM2:** Process manager with clustering

- **Nginx:** Load balancer and reverse proxy

- **Docker:** Containerized deployment

**Real-time Communication:**

- **Socket.io Scaling:** Redis adapter for horizontal scaling

- **Sticky Sessions:** Required for Socket.io

- **Load Balancer:** Configure for WebSocket support

**CI/CD Pipeline:**

- **Automated Testing:** Run tests before deployment

- **Zero-Downtime:** Rolling deployment strategy

- **Health Checks:** Verify feed endpoints

---

## Environment Configuration

### Environment Variables

**Frontend:**

```env
REACT_APP_API_URL=https://api.example.com
REACT_APP_SOCKET_URL=wss://socket.example.com
REACT_APP_ENVIRONMENT=production

```

**Backend:**

```env
NODE_ENV=production
PORT=3000
MONGODB_URI=mongodb://...
REDIS_URL=redis://...
JWT_SECRET=xxx
SOCKET_IO_REDIS_URL=redis://...
AWS_ACCESS_KEY_ID=xxx
AWS_SECRET_ACCESS_KEY=xxx
AWS_S3_BUCKET=xxx
ELASTICSEARCH_URL=xxx

```

---

## Database Migrations & Seeding

### MongoDB Migrations

**Migration Scripts:**

- **Schema Changes:** Add indexes for feed queries

- **Data Migrations:** Update post formats

- **Index Optimization:** Add compound indexes for feed generation

### Data Seeding

**Seed Data:**

- **User Accounts:** Seed test users

- **Posts:** Seed test posts

- **Relationships:** Seed follow relationships

---

## API Documentation

### Swagger/OpenAPI

**API Documentation:**

- **Swagger UI:** Document REST APIs

- **Feed API:** Document feed endpoints

- **Post API:** Document post creation endpoints

- **WebSocket Documentation:** Document Socket.io events

---

## API Versioning

**Versioning Strategy:**

- **URL Versioning:** `/api/v1/posts`, `/api/v2/posts`

- **Header Versioning:** `Accept: application/vnd.api+json;version=1`

- **Backward Compatibility:** Maintain old API versions for existing clients

- **WebSocket Versioning:** Version Socket.io events

---

## Monitoring & Logging

### Application Monitoring

**Frontend:**

- **Error Tracking:** Sentry for feed errors

- **Performance:** Track feed loading times

- **User Analytics:** Track engagement metrics

**Backend:**

- **APM:** Monitor feed generation performance

- **Socket.io Monitoring:** Track connection counts

- **Feed Metrics:** Track feed generation time, cache hit rates

### Logging

**Structured Logging:**

- **Winston / Pino:** Log feed operations

- **Feed Events:** Log feed generation, post creation

- **Error Logging:** Detailed error logs with context

---

## Database Transactions & Consistency

### MongoDB Transactions

**Transaction Usage:**

- **Multi-Document Transactions** - For operations requiring ACID guarantees

- **Example:** Post creation + user update + notification creation

- **Session Management:** Use MongoDB sessions for transaction control

**Example:**

```typescript
const session = await mongoose.startSession();
session.startTransaction();
try {
  await Post.create([postData], { session });
  await User.updateOne({ userId }, { $inc: { postCount: 1 } }, { session });
  await Notification.create([notificationData], { session });
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

- **Version Field:** Add `version` field to post documents

- **Conflict Detection:** Check version before update

- **Retry Logic:** Retry on version conflict

### Consistency Strategies

**Data Consistency:**

- **Feed Consistency:** Use transactions for feed updates

- **Like Count Consistency:** Use transactions for like operations

- **Comment Consistency:** Ensure comment updates are atomic

---

## Third-Party Service Integration

### Socket.io Integration

**Real-time Communication:**

- **Redis Adapter:** Enable horizontal scaling

- **Room Management:** Efficient room-based messaging

- **Connection Management:** Handle reconnections, heartbeats

### Redis Integration

**Caching & Feed Generation:**

- **Feed Caching:** Cache user feeds

- **Distributed Locks:** Prevent race conditions

- **Pub/Sub:** Cross-server communication

### AWS S3 Integration

**File Storage:**

- **Image Upload:** Upload post images to S3

- **Profile Pictures:** Store user profile pictures

- **Access Control:** Signed URLs for image access

### Elasticsearch Integration

**Search:**

- **Post Indexing:** Index post content

- **User Search:** Search for users

- **Hashtag Search:** Search posts by hashtags

---

# 3) Interview Answers

---

## Q1. Most complex technical challenge in building the social media platform

**Situation:** Building a social media platform that generates personalized feeds for millions of users, handles real-time updates, manages millions of posts, and scales to handle viral content while maintaining performance.

**Action:** The most complex challenge was implementing the personalized feed generation algorithm that ranks posts based on relevance, recency, and engagement while handling millions of users and posts efficiently. **Backend (Node.js/Express.js):**, I implemented a **feed generation service** that:

- Fetches posts from users you follow

- Calculates engagement score (likes, comments, shares, time decay)

- Ranks posts by score

- Caches feeds in Redis for fast retrieval

I used **MongoDB aggregation pipelines** for efficient post fetching. I implemented **feed pre-computation** - pre-generate feeds for active users. I used **Redis caching** with 5-minute TTL for feed data. **Frontend (React.js):**, I implemented **infinite scroll** with React Query for pagination. I used **Socket.io** for real-time feed updates. I implemented **optimistic updates** for likes and comments.

**Result:** Successfully delivered a scalable feed system. Feed generation takes < 500ms. System handles millions of users. Personalized feeds improve engagement by 45%. Real-time updates work seamlessly.

**Takeaway:** Feed generation is the core of social media. Engagement scoring is crucial. Caching is essential for performance. Real-time updates improve engagement. Pre-computation helps scalability.

---

## Q2. Implementing the personalized feed algorithm in Node.js

**Situation:** Users needed personalized feeds showing relevant posts from people they follow, ranked by engagement and recency.

**Action:** I implemented engagement-based feed algorithm. I fetched **posts from followed users** using MongoDB query with userId in following list. I calculated **engagement score** for each post:

- Base engagement: (likes × 1) + (comments × 2) + (shares × 3)

- Time decay: exponential decay based on post age

- Final score: engagement × time decay

I implemented **ranking** - sort posts by score (highest first). I added **diversity factor** - avoid showing too many posts from same user. I implemented **boost factors** - boost posts from close friends, recent interactions. I cached **computed feeds in Redis** with 5-minute TTL. I implemented **feed refresh** - regenerate feed every 5 minutes or on new post from followed user.

**Result:** Feed algorithm provides relevant content. Engagement-based ranking works well. Caching improves performance. Users see fresh content. Engagement increased by 45%.

**Takeaway:** Engagement scoring is crucial for feed relevance. Time decay prevents stale content. Caching improves performance. Diversity prevents monotony. Boost important connections.

---

## Q3. Implementing real-time feed updates using Socket.io

**Situation:** Users needed to see new posts in their feed without refreshing, requiring real-time updates.

**Action:** I implemented real-time feed updates using Socket.io. **Backend (Node.js/Express.js):**, I set up **Socket.io server** with Redis adapter for horizontal scaling. When a user posts, I **broadcast to followers** - get user's followers, emit post to their Socket.io rooms. I implemented **room-based messaging** - users join their feed room (`feed:${userId}`). I used **Redis pub/sub** to broadcast across multiple servers. **Frontend (React.js):**, I created **Socket.io client** that connects to server. I implemented **feed update handler** - when new post received, prepend to feed. I added **notification** for new posts. I implemented **connection management** - reconnect on disconnect, show connection status.

**Result:** Real-time feed updates work seamlessly. Users see new posts instantly. System handles 10,000+ concurrent connections. Automatic reconnection ensures reliability.

**Takeaway:** Socket.io enables real-time feed updates. Room-based messaging targets specific users. Redis adapter enables scaling. Show connection status. Handle reconnection.

---

## Q4. Implementing infinite scroll feed in React.js

**Situation:** Feeds could have thousands of posts, requiring efficient pagination and smooth scrolling.

**Action:** I implemented infinite scroll using React Query. I used **useInfiniteQuery** hook that handles pagination automatically. I implemented **fetch function** that accepts page parameter and returns posts with `hasMore` flag. I added **Intersection Observer** to detect when user scrolls near bottom. I triggered **fetchNextPage** when bottom is reached. I implemented **loading states** - show loading indicator while fetching. I added **error handling** with retry. I used **virtual scrolling** for very long feeds to improve performance. I implemented **scroll restoration** - remember scroll position on navigation.

**Result:** Infinite scroll works smoothly. Feeds load efficiently. Performance is good even with thousands of posts. User experience is excellent.

**Takeaway:** Infinite scroll improves UX. React Query simplifies pagination. Intersection Observer detects scroll. Virtual scrolling for performance. Handle loading and errors.

---

## Q5. Handling post interactions (likes, comments, shares) with real-time updates

**Situation:** Users needed to like, comment, and share posts with instant UI updates and real-time notifications.

**Action:** I implemented real-time post interactions. **Backend (Node.js/Express.js):**, I created **interaction APIs** - POST like, POST comment, POST share. I updated **post document** atomically using MongoDB $inc for likes, $push for comments. I implemented **Socket.io broadcasting** - when user likes/comments, broadcast to post owner and other viewers. I stored **interactions in MongoDB** for analytics. **Frontend (React.js):**, I implemented **optimistic updates** - update UI immediately, revert if server rejects. I used **Socket.io** to receive real-time updates. I updated **like count, comment count** in real-time. I added **notification** when someone interacts with your post.

**Result:** Post interactions work seamlessly. Real-time updates provide instant feedback. Optimistic updates improve UX. Notifications keep users engaged.

**Takeaway:** Optimistic updates improve UX. Real-time updates keep feed fresh. Atomic operations prevent race conditions. Notifications increase engagement.

