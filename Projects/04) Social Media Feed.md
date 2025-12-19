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

### Database

- **MongoDB:** NoSQL database for storing posts, users, comments, interactions
 - **Why MongoDB?** Flexible schema - easy to change post structure
 - **Document-based** - Stores data-like documents
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

## e) Architecture Overview

The system follows a layered architecture with real-time capabilities for instant updates. Here's how the complete system works:

```

┌─────────────────────────────────────────────────────────┐
│ Frontend (React.js) - Client Side │
│ (This is what users see in their browser) │
├─────────────────────────────────────────────────────────┤
│ ┌──────────────────────────────────────────────────┐ │
│ │ Browser (Chrome, Firefox, Safari) │ │
│ │ ┌────────────────────────────────────────────┐ │ │
│ │ │ React.js Application (SPA) │ │ │
│ │ │ ┌──────────────────────────────────────┐ │ │ │
│ │ │ │ React Router (Client-side Routing) │ │ │ │
│ │ │ └──────────────────────────────────────┘ │ │ │
│ │ │ ┌──────────────────────────────────────┐ │ │ │
│ │ │ │ Redux Toolkit (State Management) │ │ │ │
│ │ │ │ - Posts, User, Feed, Notifications │ │ │ │
│ │ │ └──────────────────────────────────────┘ │ │ │
│ │ │ ┌──────────────────────────────────────┐ │ │ │
│ │ │ │ Socket.io Client (Real-time) │ │ │ │
│ │ │ │ - Receives notifications instantly │ │ │ │
│ │ │ └──────────────────────────────────────┘ │ │ │
│ │ │ ┌──────────────────────────────────────┐ │ │ │
│ │ │ │ Material-UI Components │ │ │ │
│ │ │ └──────────────────────────────────────┘ │ │ │
│ │ └────────────────────────────────────────────┘ │ │
│ └──────────────────────────────────────────────────┘ │
└─────────────────────────────────────────────────────────┘
 │ │
 │ HTTP/REST API │ WebSocket
 │ (Posts, actions) │ (Notifications)
 ▼ ▼
┌─────────────────────────────────────────────────────────┐
│ Backend (Node.js + Express.js) │
│ (Server that handles business logic and data) │
├─────────────────────────────────────────────────────────┤
│ ┌──────────────────────────────────────────────────┐ │
│ │ Load Balancer / API Gateway │ │
│ └──────────────────────────────────────────────────┘ │
│ │ │
│ ┌───────────────┼───────────────┐ │
│ ▼ ▼ ▼ │
│ ┌──────────┐ ┌──────────┐ ┌──────────┐ │
│ │ Express │ │ Express │ │ Express │ │
│ │ Server 1 │ │ Server 2 │ │ Server 3 │ │
│ └──────────┘ └──────────┘ └──────────┘ │
│ │ │ │ │
│ └───────────────┼───────────────┘ │
│ ▼ │
│ ┌──────────────────────────────────────────────────┐ │
│ │ Socket.io Server (Real-time) │ │
│ │ - Handles WebSocket connections │ │
│ │ - Manages notification rooms │ │
│ │ - Broadcasts notifications │ │
│ └──────────────────────────────────────────────────┘ │
│ ▼ │
│ ┌──────────────────────────────────────────────────┐ │
│ │ Business Logic Layer │ │
│ │ - Post Service (create, update, delete posts) │ │
│ │ - Feed Service (generate personalized feeds) │ │
│ │ - User Service (authentication, profiles) │ │
│ │ - Interaction Service (likes, comments) │ │
│ │ - Notification Service (send notifications) │ │
│ └──────────────────────────────────────────────────┘ │
│ ▼ │
│ ┌──────────────────────────────────────────────────┐ │
│ │ Data Access Layer │ │
│ │ - MongoDB (Posts, users, comments) │ │
│ │ - Redis (Feed cache, sessions) │ │
│ │ - Elasticsearch (Post search) │ │
│ └──────────────────────────────────────────────────┘ │
└─────────────────────────────────────────────────────────┘
 │ │ │
 ▼ ▼ ▼
┌──────────────┐ ┌──────────────┐ ┌──────────────┐
│ MongoDB │ │ Redis │ │ Elasticsearch│
│ (Database) │ │ (Cache) │ │ (Search) │
│ │ │ │ │ │
│ - Posts │ │ - Feed │ │ - Post │
│ - Users │ │ Cache │ │ Index │
│ - Comments │ │ - Post │ │ - Search │
│ - Follows │ │ Cache │ │ Results │
└──────────────┘ └──────────────┘ └──────────────┘
 │ │ │
 └────────────────────┼────────────────────┘
 │
 ▼
 ┌──────────────┐
 │ External │
 │ Services │
 │ │
 │ - AWS S3 │
 │ - CDN │
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
│ ├── Header
│ │ ├── Logo
│ │ ├── SearchBar
│ │ ├── NavigationMenu (Home, Explore, Notifications, Messages)
│ │ └── UserMenu (Profile, Settings, Logout)
│ └── Main Content Area
│ ├── HomePage
│ │ ├── CreatePostCard
│ │ │ ├── PostInput (text, image, video)
│ │ │ ├── MediaUpload
│ │ │ └── PostButton
│ │ ├── Feed
│ │ │ └── PostCard
│ │ │ ├── PostHeader (User info, timestamp)
│ │ │ ├── PostContent (Text, images, video)
│ │ │ ├── PostActions
│ │ │ │ ├── LikeButton
│ │ │ │ ├── CommentButton
│ │ │ │ ├── ShareButton
│ │ │ │ └── BookmarkButton
│ │ │ ├── LikeCount
│ │ │ ├── CommentsSection
│ │ │ │ ├── CommentInput
│ │ │ │ └── CommentList
│ │ │ │ └── CommentItem
│ │ │ └── ShareCount
│ │ └── InfiniteScrollTrigger
│ ├── ProfilePage
│ │ ├── ProfileHeader
│ │ │ ├── CoverPhoto
│ │ │ ├── ProfilePicture
│ │ │ ├── UserName
│ │ │ ├── Bio
│ │ │ └── FollowButton
│ │ ├── ProfileTabs (Posts, About, Photos, Videos)
│ │ └── PostGrid
│ ├── PostDetailPage
│ │ ├── PostCard (full post)
│ │ └── CommentsSection (expanded)
│ ├── ExplorePage
│ │ ├── TrendingHashtags
│ │ ├── TrendingPosts
│ │ └── SuggestedUsers
│ └── NotificationsPage
│ ├── NotificationList
│ │ └── NotificationItem
│ └── MarkAllAsReadButton
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
│ ├── Header
│ │ ├── Logo
│ │ ├── SearchBar
│ │ ├── NavigationMenu (Home, Explore, Notifications, Messages)
│ │ └── UserMenu (Profile, Settings, Logout)
│ └── Main Content Area
│ ├── HomePage
│ │ ├── CreatePostCard
│ │ │ ├── PostInput (text, image, video)
│ │ │ ├── MediaUpload
│ │ │ └── PostButton
│ │ ├── Feed
│ │ │ └── PostCard
│ │ │ ├── PostHeader (User info, timestamp)
│ │ │ ├── PostContent (Text, images, video)
│ │ │ ├── PostActions
│ │ │ │ ├── LikeButton
│ │ │ │ ├── CommentButton
│ │ │ │ ├── ShareButton
│ │ │ │ └── BookmarkButton
│ │ │ ├── LikeCount
│ │ │ ├── CommentsSection
│ │ │ │ ├── CommentInput
│ │ │ │ └── CommentList
│ │ │ │ └── CommentItem
│ │ │ └── ShareCount
│ │ └── InfiniteScrollTrigger
│ ├── ProfilePage
│ │ ├── ProfileHeader
│ │ │ ├── CoverPhoto
│ │ │ ├── ProfilePicture
│ │ │ ├── UserName
│ │ │ ├── Bio
│ │ │ └── FollowButton
│ │ ├── ProfileTabs (Posts, About, Photos, Videos)
│ │ └── PostGrid
│ └── ExplorePage
│ ├── TrendingHashtags
│ ├── TrendingPosts
│ └── SuggestedUsers
└── ReduxProvider (Global State Management)
 └── Store
 ├── authSlice (User authentication state)
 ├── postSlice (Posts data)
 ├── feedSlice (Feed data)
 └── notificationSlice (Notifications)

```

### Key React Components

**Frontend Implementation:**

```javascript
// Post Card Component
const PostCard<{ post: Post }> = ({ post }) => {
 const dispatch = useAppDispatch();
 const [showComments, setShowComments] = useState(false);
 const { data: comments } = useComments(post.id);

 const handleLike = async () => {
 dispatch(likePost(post.id));
 // Optimistic update
 };

 const handleComment = async (commentText) => {
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
const CreatePostCard= () => {
 const [text, setText] = useState('');
 const [media, setMedia] = useState([]);
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

**State Management Strategy (React 19):**

- **Local State (useState)**: Form inputs, UI state (loading, errors, modals, show/hide comments)
- **Optimistic Updates (useOptimistic)**: React 19 hook for optimistic post creation, likes, comments
- **Form Actions (useActionState)**: React 19 hook for post creation forms with server actions
- **Deferred Values (useDeferredValue)**: React 19 hook for feed updates and search
- **Transitions (useTransition)**: React 19 hook for non-urgent feed updates
- **API State**: React Query for server state (posts, feed, comments) - caching, refetching
- **Global State (Redux Toolkit)**: User authentication, feed data, notifications, selected post

**Frontend Implementation:**

```javascript
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

### iii) Advanced Feed Rendering Patterns

**Infinite Scroll Feed with Intersection Observer:**

```javascript
const Feed= () => {
 const {
 data,
 fetchNextPage,
 hasNextPage,
 isFetchingNextPage,
 isLoading,
 refetch
 } = useInfiniteQuery({
 queryKey: ['feed'],
 queryFn: ({ pageParam = null }) => fetchFeed({ cursor: pageParam }),
 getNextPageParam: (lastPage) => lastPage.nextCursor,
 staleTime: 30000
 });

 const observerTarget = useRef(null);

 useEffect(() => {
 const observer = new IntersectionObserver(
 (entries) => {
 if (entries[0].isIntersecting && hasNextPage && !isFetchingNextPage) {
 fetchNextPage();
 }
 },
 { threshold: 0.1 }
 );

 if (observerTarget.current) {
 observer.observe(observerTarget.current);
 }

 return () => observer.disconnect();
 }, [hasNextPage, isFetchingNextPage, fetchNextPage]);

 const posts = data?.pages.flatMap(page => page.posts) || [];

 return (
 <div className="feed">
 {posts.map(post => (
 <PostCard key={post.id} post={post} />
 ))}
 <div ref={observerTarget} className="load-more-trigger">
 {isFetchingNextPage && <LoadingSpinner />}
 </div>
 </div>
 );
};
```

**Optimistic Post Creation with React 19:**

```javascript
import { useOptimistic, useTransition, useActionState } from 'react';

// React 19: Server Action for creating post
async function createPostAction(
 prevState: { error?},
 formData: FormData
) {
 const content = formData.get('content') as string;
 const mediaFiles = formData.getAll('media');

 if (!content.trim() && mediaFiles.length === 0) {
 return { error: 'Post cannot be empty' };
 }

 try {
 const post = await createPostAPI({ content, media: mediaFiles });
 return { success: true, post };
 } catch (error) {
 return { error: 'Failed to create post' };
 }
}

const Feed= () => {
 const [posts, setPosts] = useState([]);
 const [isPending, startTransition] = useTransition();

 // React 19: useOptimistic for feed updates
 const [optimisticPosts, addOptimisticPost] = useOptimistic(
 posts,
 (state, newPost: Post) => [
 { ...newPost, id: 'temp', syncing: true },
 ...state
 ]
 );

 // React 19: useActionState for form actions
 const [state, formAction] = useActionState(createPostAction, {});

 const handleCreatePost = (formData: FormData) => {
 const tempPost: Post = {
 id: 'temp',
 userId: currentUserId,
 content: formData.get('content') as string,
 createdAt: new Date(),
 syncing: true
 };

 // Optimistically add to feed
 startTransition(() => {
 addOptimisticPost(tempPost);
 });

 formAction(formData);
 };

 // Update posts when action succeeds
 useEffect(() => {
 if (state.success && state.post) {
 setPosts(prev => prev.map(p => p.id === 'temp' ? state.post : p));
 } else if (state.error) {
 // Remove temp post on error
 setPosts(prev => prev.filter(p => p.id !== 'temp'));
 }
 }, [state]);

 return (
 <div className="feed">
 <CreatePostForm onSubmit={handleCreatePost} />
 {optimisticPosts.map(post => (
 <PostCard key={post.id} post={post} />
 ))}
 </div>
 );
};
```

**Real-time Feed Updates with Socket.io:**

```javascript
const useFeedSocket = () => {
 const queryClient = useQueryClient();
 const socketRef = useRef<Socket | null>(null);

 useEffect(() => {
 socketRef.current = io('ws://api.example.com', {
 auth: { token: getAuthToken() }
 });

 // New post received
 socketRef.current.on('new_post', (post: Post) => {
 queryClient.setQueryData(['feed'], (old: any) => {
 if (!old) return old;

 return {
 pages: [
 {
 posts: [post, ...old.pages[0].posts],
 nextCursor: old.pages[0].nextCursor
 },
 ...old.pages.slice(1)
 ]
 };
 });

 toast.info(`${post.userName} posted something new`);
 });

 // Post updated (likes, comments)
 socketRef.current.on('post_updated', (updatedPost: Post) => {
 queryClient.setQueryData(['feed'], (old: any) => {
 if (!old) return old;

 return {
 pages: old.pages.map((page: any) => ({
 ...page,
 posts: page.posts.map((p: Post) =>
 p.id === updatedPost.id ? updatedPost : p
 )
 }))
 };
 });
 });

 return () => {
 socketRef.current?.disconnect();
 };
 }, [queryClient]);
};
```

### iv) Media Handling & Upload

**Image Upload with Preview:**

```javascript
const MediaUpload<{
 files: File[];
 onFilesChange: (files: File[]) => void;
 maxFiles?;
 maxSize?;
}> = ({ files, onFilesChange, maxFiles = 10, maxSize = 10 * 1024 * 1024 }) => {
 const [previews, setPreviews] = useState([]);
 const [uploadProgress, setUploadProgress] = useState>({});

 const handleFileSelect = (e: React.ChangeEvent) => {
 const selectedFiles = Array.from(e.target.files || []);

 // Validate files
 const validFiles = selectedFiles.filter(file => {
 if (file.size > maxSize) {
 toast.error(`${file.name} is too large. Max size: ${maxSize / 1024 / 1024}MB`);
 return false;
 }
 return true;
 });

 if (files.length + validFiles.length > maxFiles) {
 toast.error(`Maximum ${maxFiles} files allowed`);
 return;
 }

 const newFiles = [...files, ...validFiles];
 onFilesChange(newFiles);

 // Generate previews
 validFiles.forEach(file => {
 const reader = new FileReader();
 reader.onloadend = () => {
 setPreviews(prev => [...prev, reader.result as string]);
 };
 reader.readAsDataURL(file);
 });
 };

 const removeFile = (index) => {
 const newFiles = files.filter((_, i) => i !== index);
 const newPreviews = previews.filter((_, i) => i !== index);
 onFilesChange(newFiles);
 setPreviews(newPreviews);
 };

 return (
 <div className="media-upload">
 <input
 type="file"
 multiple
 accept="image/*,video/*"
 onChange={handleFileSelect}
 style={{ display: 'none' }}
 id="media-input"
 />
 <label htmlFor="media-input" className="upload-button">
 Add Photos/Videos
 </label>

 <div className="media-preview-grid">
 {previews.map((preview, index) => (
 <div key={index} className="media-preview">
 <img src={preview} alt={`Preview ${index + 1}`} />
 <button onClick={() => removeFile(index)}>×</button>
 {uploadProgress[files[index]?.name] && (
 <div className="upload-progress">
 <div
 className="progress-bar"
 style={{ width: `${uploadProgress[files[index]?.name]}%` }}
 />
 </div>
 )}
 </div>
 ))}
 </div>
 </div>
 );
};
```

**Image Gallery with Lightbox:**

```javascript
const PostMedia<{ media[]; type: 'image' | 'video' }> = ({
 media,
 type
}) => {
 const [selectedIndex, setSelectedIndex] = useState(null);

 if (media.length === 0) return null;

 if (media.length === 1) {
 return (
 <div className="post-media single">
 {type === 'image' ? (
 <img
 src={media[0]}
 alt="Post media"
 onClick={() => setSelectedIndex(0)}
 loading="lazy"
 />
 ) : (
 <video src={media[0]} controls />
 )}
 </div>
 );
 }

 if (media.length === 2) {
 return (
 <div className="post-media grid-2">
 {media.map((url, index) => (
 <img
 key={index}
 src={url}
 alt={`Media ${index + 1}`}
 onClick={() => setSelectedIndex(index)}
 loading="lazy"
 />
 ))}
 </div>
 );
 }

 return (
 <>
 <div className="post-media grid">
 {media.slice(0, 4).map((url, index) => (
 <div
 key={index}
 className={`media-item ${index === 3 && media.length > 4 ? 'more-overlay' : ''}`}
 onClick={() => setSelectedIndex(index)}
 >
 <img src={url} alt={`Media ${index + 1}`} loading="lazy" />
 {index === 3 && media.length > 4 && (
 <div className="more-count">+{media.length - 4}</div>
 )}
 </div>
 ))}
 </div>

 {selectedIndex !== null && (
 <Lightbox
 images={media}
 currentIndex={selectedIndex}
 onClose={() => setSelectedIndex(null)}
 onNext={() => setSelectedIndex((selectedIndex + 1) % media.length)}
 onPrev={() => setSelectedIndex((selectedIndex - 1 + media.length) % media.length)}
 />
 )}
 </>
 );
};
```

**Video Player with Controls:**

```javascript
const VideoPlayer<{ src; autoplay?}> = ({
 src,
 autoplay = false
}) => {
 const videoRef = useRef(null);
 const [playing, setPlaying] = useState(autoplay);
 const [muted, setMuted] = useState(true);
 const [progress, setProgress] = useState(0);

 useEffect(() => {
 const video = videoRef.current;
 if (!video) return;

 const handleTimeUpdate = () => {
 setProgress((video.currentTime / video.duration) * 100);
 };

 video.addEventListener('timeupdate', handleTimeUpdate);

 return () => {
 video.removeEventListener('timeupdate', handleTimeUpdate);
 };
 }, []);

 const togglePlay = () => {
 const video = videoRef.current;
 if (!video) return;

 if (playing) {
 video.pause();
 } else {
 video.play();
 }
 setPlaying(!playing);
 };

 return (
 <div className="video-player">
 <video
 ref={videoRef}
 src={src}
 muted={muted}
 loop
 playsInline
 onClick={togglePlay}
 />
 <div className="video-controls">
 <button onClick={togglePlay} aria-label={playing ? 'Pause' : 'Play'}>
 {playing ? '⏸' : '▶'}
 </button>
 <button onClick={() => setMuted(!muted)} aria-label={muted ? 'Unmute' : 'Mute'}>
 {muted ? '🔇' : '🔊'}
 </button>
 <div className="progress-bar">
 <div
 className="progress-fill"
 style={{ width: `${progress}%` }}
 />
 </div>
 </div>
 </div>
 );
};
```

### v) Post Interactions

**Optimistic Like with React 19:**

```javascript
import { useOptimistic, useTransition } from 'react';

const LikeButton<{ postId; initialLikes; isLiked}> = ({
 postId,
 initialLikes,
 isLiked: initialIsLiked
}) => {
 const [isLiked, setIsLiked] = useState(initialIsLiked);
 const [likeCount, setLikeCount] = useState(initialLikes);
 const [isPending, startTransition] = useTransition();

 // React 19: useOptimistic for like count
 const [optimisticLikeCount, updateLikeCount] = useOptimistic(
 likeCount,
 (state, delta) => state + delta
 );

 const [showAnimation, setShowAnimation] = useState(false);
 const lastTapRef = useRef<number>(0);

 const handleLike = async () => {
 const newIsLiked = !isLiked;
 const delta = newIsLiked ? 1 : -1;

 // Optimistically update UI
 startTransition(() => {
 setIsLiked(newIsLiked);
 updateLikeCount(delta);
 });

 try {
 await toggleLikeAPI(postId);
 } catch (error) {
 // Rollback on error
 setIsLiked(isLiked);
 setLikeCount(likeCount);
 toast.error('Failed to update like');
 }
 };

 const handleDoubleTap = () => {
 const now = Date.now();
 const DOUBLE_TAP_DELAY = 300;

 if (now - lastTapRef.current < DOUBLE_TAP_DELAY) {
 if (!isLiked) {
 handleLike();
 setShowAnimation(true);
 setTimeout(() => setShowAnimation(false), 1000);
 }
 }

 lastTapRef.current = now;
 };

 return (
 <div className="like-button-container" onDoubleClick={handleDoubleTap}>
 <button
 className={`like-button ${isLiked ? 'liked' : ''}`}
 onClick={handleLike}
 disabled={isPending}
 aria-label={isLiked ? 'Unlike' : 'Like'}
 >
 {isLiked ? '❤️' : '🤍'}
 </button>
 <span className="like-count">{optimisticLikeCount}</span>
 {showAnimation && <div className="like-animation">❤️</div>}
 </div>
 );
};
```

**Comment Section with Real-time Updates:**

```javascript
const CommentsSection<{ postId}> = ({ postId }) => {
 const [showComments, setShowComments] = useState(false);
 const [newComment, setNewComment] = useState('');
 const commentsEndRef = useRef(null);

 const { data: comments, refetch } = useQuery({
 queryKey: ['comments', postId],
 queryFn: () => fetchComments(postId),
 enabled: showComments
 });

 const addCommentMutation = useMutation({
 mutationFn: (text) => addCommentAPI(postId, text),
 onSuccess: () => {
 setNewComment('');
 refetch();
 // Scroll to bottom
 setTimeout(() => {
 commentsEndRef.current?.scrollIntoView({ behavior: 'smooth' });
 }, 100);
 }
 });

 // Real-time comment updates
 useEffect(() => {
 if (!showComments) return;

 const socket = io('ws://api.example.com');
 socket.on(`post:${postId}:comment`, (comment: Comment) => {
 refetch();
 });

 return () => socket.disconnect();
 }, [postId, showComments, refetch]);

 return (
 <div className="comments-section">
 <button onClick={() => setShowComments(!showComments)}>
 {showComments ? 'Hide' : 'Show'} Comments ({comments?.length || 0})
 </button>

 {showComments && (
 <>
 <div className="comments-list">
 {comments?.map(comment => (
 <CommentItem key={comment.id} comment={comment} />
 ))}
 <div ref={commentsEndRef} />
 </div>

 <div className="comment-input">
 <input
 type="text"
 value={newComment}
 onChange={(e) => setNewComment(e.target.value)}
 onKeyPress={(e) => {
 if (e.key === 'Enter' && newComment.trim()) {
 addCommentMutation.mutate(newComment);
 }
 }}
 placeholder="Write a comment..."
 />
 <button
 onClick={() => addCommentMutation.mutate(newComment)}
 disabled={!newComment.trim() || addCommentMutation.isPending}
 >
 Post
 </button>
 </div>
 </>
 )}
 </div>
 );
};
```

**Typing Indicator:**

```javascript
const useTypingIndicator = (postId) => {
 const [typingUsers, setTypingUsers] = useState([]);
 const socketRef = useRef<Socket | null>(null);
 const typingTimeoutRef = useRef<NodeJS.Timeout>();

 useEffect(() => {
 socketRef.current = io('ws://api.example.com');

 socketRef.current.on(`post:${postId}:typing`, (data: { userId; userName}) => {
 setTypingUsers(prev => {
 if (!prev.includes(data.userName)) {
 return [...prev, data.userName];
 }
 return prev;
 });

 // Clear after 3 seconds
 clearTimeout(typingTimeoutRef.current);
 typingTimeoutRef.current = setTimeout(() => {
 setTypingUsers(prev => prev.filter(u => u !== data.userName));
 }, 3000);
 });

 return () => {
 socketRef.current?.disconnect();
 clearTimeout(typingTimeoutRef.current);
 };
 }, [postId]);

 const emitTyping = useCallback(() => {
 socketRef.current?.emit('typing', { postId });
 }, [postId]);

 return { typingUsers, emitTyping };
};
```

### vi) Performance Optimizations

**Virtual Scrolling for Long Feeds:**

```javascript
const VirtualizedFeed<{ posts: Post[] }> = ({ posts }) => {
 const parentRef = useRef(null);

 const virtualizer = useVirtualizer({
 count: posts.length,
 getScrollElement: () => parentRef.current,
 estimateSize: () => 600, // Estimated post height
 overscan: 3
 });

 return (
 <div ref={parentRef} style={{ height: '100vh', overflow: 'auto' }}>
 <div
 style={{
 height: `${virtualizer.getTotalSize()}px`,
 width: '100%',
 position: 'relative'
 }}
 >
 {virtualizer.getVirtualItems().map(virtualItem => (
 <div
 key={virtualItem.key}
 style={{
 position: 'absolute',
 top: 0,
 left: 0,
 width: '100%',
 height: `${virtualItem.size}px`,
 transform: `translateY(${virtualItem.start}px)`
 }}
 >
 <PostCard post={posts[virtualItem.index]} />
 </div>
 ))}
 </div>
 </div>
 );
};
```

**Image Lazy Loading:**

```javascript
const LazyImage<{ src; alt}> = ({ src, alt }) => {
 const [loaded, setLoaded] = useState(false);
 const [inView, setInView] = useState(false);
 const imgRef = useRef(null);

 useEffect(() => {
 const observer = new IntersectionObserver(
 (entries) => {
 if (entries[0].isIntersecting) {
 setInView(true);
 observer.disconnect();
 }
 },
 { threshold: 0.1 }
 );

 if (imgRef.current) {
 observer.observe(imgRef.current);
 }

 return () => observer.disconnect();
 }, []);

 return (
 <div className="lazy-image-wrapper" ref={imgRef}>
 {!loaded && <div className="image-skeleton" />}
 {inView && (
 <img
 src={src}
 alt={alt}
 onLoad={() => setLoaded(true)}
 className={loaded ? 'loaded' : 'loading'}
 loading="lazy"
 />
 )}
 </div>
 );
};
```

### vii) Implementation Details

**Data Flow:**

1. **Feed Loading** → HomePage fetches feed via React Query infinite query with cursor-based pagination, displays PostCard components with virtual scrolling
2. **Post Creation** → CreatePostCard submits post with media upload progress, optimistically updates feed, syncs with backend
3. **Post Interactions** → Like/Comment actions update immediately with optimistic updates, sync with backend, show real-time updates via Socket.io
4. **Real-time Updates** → Socket.io receives new posts/comments/likes, updates feed in real-time without refetching
5. **Infinite Scroll** → Intersection Observer detects scroll to bottom, triggers next page fetch automatically

**Event Handling:**

- Post creation triggers optimistic update with rollback on error
- Like/Comment actions update immediately with server sync and error handling
- Real-time notifications via Socket.io for new posts, comments, likes
- Infinite scroll loads more posts automatically with loading indicators
- Media upload shows progress with preview and error handling
- Double-tap to like with animation feedback
- Typing indicators for real-time comment typing

**UI/UX Considerations:**

- **Loading States**: Skeleton loaders for feed, spinners for actions, progress bars for media uploads
- **Error Handling**: User-friendly error messages with retry options, toast notifications for actions
- **Validation**: Client-side validation for post content (character limits), media (size, format)
- **Responsive Design**: Mobile-first layout, optimized for touch interactions, swipe gestures for navigation
- **Accessibility**: ARIA labels, keyboard navigation, screen reader support, focus management, alt text for images
- **Performance**: Virtual scrolling for long feeds, image lazy loading with Intersection Observer, code splitting per route, service worker for offline support
- **Real-time Experience**: Instant feedback for interactions, real-time updates via WebSocket, typing indicators, live notifications

---

## Data Models

### Post Model

```javascript
// Post structure:
//
 id;
 userId;
 userName;
 userAvatar;
 content;
 type: 'text' | 'image' | 'video' | 'link' | 'poll';
 media?[]; // Array of media URLs
 hashtags[];
 mentions[]; // Array of mentioned user IDs
 likes;
 comments;
 shares;
 visibility: 'public' | 'friends' | 'private';
 createdAt;
 updatedAt;

```

### Comment Model

```javascript
// Comment structure:
//
 id;
 postId;
 userId;
 userName;
 userAvatar;
 text;
 likes;
 replies: Comment[]; // Nested comments
 createdAt;

```

### Feed Model

```javascript
// Feed structure:
//
 userId;
 posts[]; // Array of post IDs
 lastUpdated;

```

---

## Data APIs

**Note:** All API endpoints are implemented on the **backend (Node.js/Express)**, and the **frontend (React.js)** calls these APIs using Axios. Real-time updates use **Socket.io**.

### Post APIs

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

*Note: Backend implementation details are kept minimal. Focus is on frontend integration.*

**API Endpoints Reference:**

- `GET /api/feed` - Get feed posts (cursor-based pagination)
- `POST /api/posts` - Create new post
- `POST /api/posts/:id/like` - Like/unlike post
- `POST /api/posts/:id/comments` - Add comment
- `GET /api/posts/:id/comments` - Get comments
- `POST /api/posts/:id/share` - Share post
- `GET /api/notifications` - Get notifications
- `PUT /api/notifications/:id/read` - Mark notification as read

**WebSocket Events:**

- `post:new` - New post received
- `post:updated` - Post updated (likes, comments)
- `notification` - New notification received
- `typing` - User typing indicator

---

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

---

## Environment Configuration

### Environment Variables

**Frontend:**

```env
REACT_APP_API_URL=https://api.example.com
REACT_APP_SOCKET_URL=wss://socket.example.com
REACT_APP_ENVIRONMENT=production

```

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

```javascript

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

# 4) Algorithms

## Feed Ranking Algorithm

**Purpose:** Rank posts in user's feed by engagement score and time decay.

**Algorithm:**

1. Fetch posts from users you follow
2. Calculate engagement score: (likes × 1) + (comments × 2) + (shares × 3)
3. Apply time decay: exponential decay based on post age
4. Calculate final score: engagement × time decay
5. Sort posts by score (highest first)

**Implementation:**

```javascript

function calculateEngagementScore(post: Post){
 const engagement = (post.likes * 1) + (post.comments * 2) + (post.shares * 3);
 const hoursSincePost = (Date.now() - post.createdAt.getTime()) / (1000 * 60 * 60);
 const timeDecay = Math.exp(-hoursSincePost / 24); // Decay over 24 hours
 return engagement * timeDecay;
}

function rankFeed(posts: Post[]): Post[] {
 return posts
 .map(post => ({ ...post, score: calculateEngagementScore(post) }))
 .sort((a, b) => b.score - a.score);
}

```

**Complexity:**

- Time: O(n log n) for sorting where n is number of posts
- Space: O(n) for scoring
- **Ranking Quality:** Engagement-based ranking improves feed relevance

---

## Fan-out Algorithm

**Purpose:** Distribute new posts to all followers' feeds efficiently.

**Algorithm:**

1. When user creates post, get list of followers
2. For each follower, add post to their feed cache
3. Use message queue for async fan-out
4. Batch updates for efficiency

**Implementation:**

```javascript

async function fanOutPost(post: Post, followers[]){
 // Batch updates
 const batchSize = 100;
 for (let i = 0; i < followers.length; i += batchSize) {
 const batch = followers.slice(i, i + batchSize);

 await Promise.all(
 batch.map(followerId =>
 redis.lpush(`feed:${followerId}`, post.id)
 )
 );
 }
}

```

**Complexity:**

- Time: O(n) where n is number of followers
- Space: O(1) per follower
- **Efficiency:** Batch processing improves performance

---

# 5) Data Models

## Posts Collection (MongoDB)

```javascript

{
 _id: ObjectId,
 postId: String, // Unique post ID, indexed
 userId: ObjectId, // User reference, indexed
 content: String, // Post content
 type: String, // text, image, video, link, poll
 media: [String], // Array of media URLs
 hashtags: [String], // Array of hashtags, indexed
 mentions: [ObjectId], // Array of mentioned user IDs
 likes: Number, // Like count
 comments: Number, // Comment count
 shares: Number, // Share count
 visibility: String, // public, friends, private
 createdAt, // Created timestamp, indexed
 updatedAt// Updated timestamp
}

// Indexes:
// - { postId: 1 } (unique)
// - { userId: 1, createdAt: -1 } (compound)
// - { hashtags: 1 } (for hashtag search)
// - { visibility: 1, createdAt: -1 } (compound)

```

## Comments Collection (MongoDB)

```javascript

{
 _id: ObjectId,
 commentId: String, // Unique comment ID, indexed
 postId: ObjectId, // Post reference, indexed
 userId: ObjectId, // User reference, indexed
 text: String, // Comment text
 likes: Number, // Like count
 parentCommentId: ObjectId, // Parent comment (for nested comments)
 createdAt, // Created timestamp, indexed
 updatedAt// Updated timestamp
}

// Indexes:
// - { commentId: 1 } (unique)
// - { postId: 1, createdAt: -1 } (compound)
// - { userId: 1 } (indexed)

```

---

# 6) Database Transactions and Consistency

### MongoDB Transactions

**Transaction Usage:**

- **Multi-Document Transactions** - For operations requiring ACID guarantees
- **Example:** Post creation + user update + notification creation in single transaction
- **Session Management:** Use MongoDB sessions for transaction control

**Example:**

```javascript

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

### Consistency Strategies

**Data Consistency:**

- **Feed Consistency:** Use transactions for feed updates to ensure atomicity
- **Like Count Consistency:** Use transactions for like operations
- **Comment Consistency:** Ensure comment updates are atomic
- **Eventual Consistency:** Accept eventual consistency for feed fan-out (feeds may update with slight delay)

---

# 7) Protocols

### REST API Protocol

- **Protocol:** REST (Representational State Transfer)
- **Data Format:** JSON
- **HTTP Methods:** GET, POST, PUT, DELETE
- **Status Codes:** 200 (Success), 201 (Created), 400 (Bad Request), 401 (Unauthorized), 404 (Not Found), 500 (Server Error)
- **Authentication:** JWT Bearer token in Authorization header

### WebSocket Protocol

- **Protocol:** Socket.io over WebSocket
- **Events:** `post:new`, `like:new`, `comment:new`, `feed:update`
- **Authentication:** JWT token in handshake
- **Use Case:** Real-time feed updates and notifications

---

# 8) API Design

### GET /api/v1/feed

- **URL:** `/api/v1/feed?page=1&limit=20`
- **Method:** GET
- **Description:** Get personalized feed
- **Response:**

 ```json

 {
 "success": true,
 "data": {
 "posts": [...],
 "hasMore": true,
 "nextPage": 2
 }
 }

 ```

- **Status Codes:** 200 (Success), 401 (Unauthorized)

### POST /api/v1/posts

- **URL:** `/api/v1/posts`
- **Method:** POST
- **Description:** Create a new post
- **Request Body:**

 ```json

 {
 "content": "Hello world!",
 "type": "text",
 "hashtags": ["hello", "world"],
 "visibility": "public"
 }

 ```

- **Response:**

 ```json

 {
 "success": true,
 "data": {
 "postId": "post_abc123",
 "content": "Hello world!",
 "createdAt": "2024-01-15T10:30:00Z"
 }
 }

 ```

- **Status Codes:** 201 (Created), 400 (Validation Error)

---

# 9) Caching Strategy

### Redis Cache

**Cache Strategy:**

- **Key Format:** `feed:{userId}`, `post:{postId}`, `user:{userId}`
- **Value:** Serialized JSON (feed post IDs, post data, user data)
- **TTL:**
 - Feed cache: 300 seconds (5 minutes)
 - Post data: 3600 seconds (1 hour)
 - User data: 1800 seconds (30 minutes)
- **Eviction Policy:** LRU (Least Recently Used)

**Cache Patterns:**

- **Cache-Aside Pattern:** Check cache first, if miss query database and update cache
- **Write-Through Pattern:** Update cache when posts are created/updated
- **Cache Invalidation:** Invalidate feed cache on new posts from followed users

---

# 10) Error Handling

### Error Scenarios and Responses

**Edge Cases Handling:**

- **Post Not Found:** Return 404 Not Found when post doesn't exist
- **Unauthorized Access:** Return 403 Forbidden when user doesn't have permission
- **Invalid Post Data:** Return 400 Bad Request with validation errors
- **Feed Generation Failure:** Return 500 Server Error, fallback to cached feed

**Error Response Format:**

```json

{
 "error": {
 "code": "POST_NOT_FOUND",
 "message": "Post not found",
 "details": "Post post_abc123 does not exist"
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

- **Read Replicas:** Deploy read replicas for feed queries
- **Sharding:** Shard posts by userId for write scaling
- **Connection Pooling:** Use connection pooling to manage database connections

**Caching:**

- Distributed Redis cluster for high availability
- Cache feeds and post data
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

**Server Setup:**

- **PM2:** Process manager with clustering for Node.js apps
- **Nginx:** Load balancer and reverse proxy with SSL termination
- **Docker:** Containerized deployment for consistency
- **Kubernetes:** Container orchestration for auto-scaling

**CI/CD Pipeline:**

- **Automated Testing:** Run tests before deployment
- **Zero-Downtime:** Rolling deployment strategy
- **Health Checks:** Verify feed endpoints are healthy
- **Blue-Green Deployment:** Maintain two identical production environments

### Database Deployment

**MongoDB Setup:**

- **MongoDB Atlas** - Managed MongoDB service with automatic backups
- **Backup Strategy:** Daily automated backups with point-in-time recovery
- **Indexing:** Proper indexes on postId, userId, hashtags, createdAt
- **Replication:** Replica sets for high availability

**Redis Setup:**

- **Redis Cloud / AWS ElastiCache** - Managed Redis service
- **Cluster Mode:** Redis cluster for high availability and performance
- **Persistence:** RDB snapshots and AOF for data durability

---

# 12) Security Considerations

### Rate Limiting

- Implement rate limiting at API layer to prevent abuse
- Limit number of posts per user per day/hour
- Use Redis for distributed rate limiting across multiple servers

### Input Validation

- Validate all API inputs (post content, media files)
- Sanitize user input to prevent XSS attacks
- Validate file uploads (images, videos) for type and size

### HTTPS/TLS

- All communication between clients and API encrypted using HTTPS
- Prevents eavesdropping and man-in-the-middle attacks
- SSL/TLS certificates for secure connections

### Authentication and Authorization

- **JWT Tokens:** Use JWT for stateless authentication
- **Token Expiration:** Set appropriate token expiration times
- **Role-Based Access Control:** Implement RBAC for admin vs user access
- **Post Privacy:** Enforce post visibility settings (public, friends, private)

### Content Moderation

- **Content Filtering:** Filter inappropriate content using ML models
- **Report System:** Allow users to report inappropriate posts
- **Automated Moderation:** Use automated tools for content moderation

### Monitoring and Alerts

- Set up monitoring for unusual activity patterns
- Trigger alerts for potential security issues
- Track metrics: post creation rates, engagement rates, user activity
- Log all operations for security auditing

---

# 3) Interview Answers

---

## Q1. 💡 Most complex technical challenge in building the social media platform

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

## Q2. ⚙️ Implementing the personalized feed algorithm in Node.js

**Situation:** Users needed personalized feeds showing relevant posts from people they follow, ranked by engagement and recency.

**Action:** I implemented engagement-based feed algorithm. I fetched **posts from followed users** using MongoDB query with userId in following list. I calculated **engagement score** for each post:

- Base engagement: (likes × 1) + (comments × 2) + (shares × 3)

- Time decay: exponential decay based on post age

- Final score: engagement × time decay

I implemented **ranking** - sort posts by score (highest first). I added **diversity factor** - avoid showing too many posts from same user. I implemented **boost factors** - boost posts from close friends, recent interactions. I cached **computed feeds in Redis** with 5-minute TTL. I implemented **feed refresh** - regenerate feed every 5 minutes or on new post from followed user.

**Result:** Feed algorithm provides relevant content. Engagement-based ranking works well. Caching improves performance. Users see fresh content. Engagement increased by 45%.

**Takeaway:** Engagement scoring is crucial for feed relevance. Time decay prevents stale content. Caching improves performance. Diversity prevents monotony. Boost important connections.

---

## Q3. ⏰ ⏰ ⏰ Implementing real-time feed updates using Socket.io

**Situation:** Users needed to see new posts in their feed without refreshing, requiring real-time updates.

**Action:** I implemented real-time feed updates using Socket.io. **Backend (Node.js/Express.js):**, I set up **Socket.io server** with Redis adapter for horizontal scaling. When a user posts, I **broadcast to followers** - get user's followers, emit post to their Socket.io rooms. I implemented **room-based messaging** - users join their feed room (`feed:${userId}`). I used **Redis pub/sub** to broadcast across multiple servers. **Frontend (React.js):**, I created **Socket.io client** that connects to server. I implemented **feed update handler** - when new post received, prepend to feed. I added **notification** for new posts. I implemented **connection management** - reconnect on disconnect, show connection status.

**Result:** Real-time feed updates work seamlessly. Users see new posts instantly. System handles 10,000+ concurrent connections. Automatic reconnection ensures reliability.

**Takeaway:** Socket.io enables real-time feed updates. Room-based messaging targets specific users. Redis adapter enables scaling. Show connection status. Handle reconnection.

---

## Q4. ⚛️ Implementing infinite scroll feed in React.js

**Situation:** Feeds could have thousands of posts, requiring efficient pagination and smooth scrolling.

**Action:** I implemented infinite scroll using React Query. I used **useInfiniteQuery** hook that handles pagination automatically. I implemented **fetch function** that accepts page parameter and returns posts with `hasMore` flag. I added **Intersection Observer** to detect when user scrolls near bottom. I triggered **fetchNextPage** when bottom is reached. I implemented **loading states** - show loading indicator while fetching. I added **error handling** with retry. I used **virtual scrolling** for very long feeds to improve performance. I implemented **scroll restoration** - remember scroll position on navigation.

**Result:** Infinite scroll works smoothly. Feeds load efficiently. Performance is good even with thousands of posts. User experience is excellent.

**Takeaway:** Infinite scroll improves UX. React Query simplifies pagination. Intersection Observer detects scroll. Virtual scrolling for performance. Handle loading and errors.

---

## Q5. ⏰ ⏰ ⏰ Handling post interactions (likes, comments, shares) with real-time updates

**Situation:** Users needed to like, comment, and share posts with instant UI updates and real-time notifications.

**Action:** I implemented real-time post interactions. **Backend (Node.js/Express.js):**, I created **interaction APIs** - POST like, POST comment, POST share. I updated **post document** atomically using MongoDB $inc for likes, $push for comments. I implemented **Socket.io broadcasting** - when user likes/comments, broadcast to post owner and other viewers. I stored **interactions in MongoDB** for analytics. **Frontend (React.js):**, I implemented **optimistic updates** - update UI immediately, revert if server rejects. I used **Socket.io** to receive real-time updates. I updated **like count, comment count** in real-time. I added **notification** when someone interacts with your post.

**Result:** Post interactions work seamlessly. Real-time updates provide instant feedback. Optimistic updates improve UX. Notifications keep users engaged.

**Takeaway:** Optimistic updates improve UX. Real-time updates keep feed fresh. Atomic operations prevent race conditions. Notifications increase engagement.
