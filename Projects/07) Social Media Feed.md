# Social Media Feed

---

## 📍 Navigation

<div align="center">

[Home: README](README.md) • [← Previous: Video Streaming Platform](06%29%20Video%20Streaming%20Platform.md) • [Next: E-commerce App →](08%29%20E-commerce%20App.md)

[📋 Cheatsheet](Projects%20Interview%20Cheatsheet.md)

</div>

---

## Overview

Design a social media feed system where users can create posts, follow other users, and view personalized content feeds in real-time. The system handles likes, comments, shares, and real-time engagement updates.

---

## 1) Requirements

### Functional Requirements

**Core Features:**
- User registration and authentication
- Create posts (text, images, videos)
- Follow/unfollow users
- Personalized feed (posts from followed users)
- Like, comment, and share posts
- User profiles with followers/following
- Real-time updates (likes, comments appear instantly)
- Hashtag support and trending topics
- Search (users, posts, hashtags)
- Explore feed (discover new content)

**Advanced Features:**
- Video posts
- Story feature (24-hour posts)
- Save posts
- Post editing and deletion
- Comment replies and threads
- Message reactions
- Notifications for interactions

### Non-Functional Requirements

**Performance:**
- Feed loading: < 1 second
- Smooth infinite scroll
- Optimized media (images, videos)
- Real-time updates: < 500ms latency

**Scalability:**
- Handle millions of users
- Billions of posts
- Thousands of concurrent real-time connections
- Traffic spikes (viral posts)

**User Experience:**
- Responsive design (mobile-first)
- Fast interactions (instant likes)
- Intuitive UI
- Accessible interface

---

## 2) Component Hierarchy

The frontend is a React application for social media. Here's the structure:

```
App
├── Layout
│   ├── Header
│   │   ├── Logo
│   │   ├── SearchBar
│   │   ├── NotificationBell
│   │   └── UserMenu
│   └── MainContent
├── Pages
│   ├── FeedPage
│   │   ├── PostComposer
│   │   │   ├── TextInput
│   │   │   ├── ImageUpload
│   │   │   └── PostButton
│   │   └── FeedList
│   │       └── PostCard
│   │           ├── UserHeader (avatar, name, time)
│   │           ├── PostContent (text, images, video)
│   │           ├── EngagementBar
│   │           │   ├── LikeButton (with count)
│   │           │   ├── CommentButton (with count)
│   │           │   ├── ShareButton
│   │           │   └── SaveButton
│   │           └── CommentSection
│   │               ├── CommentList
│   │               │   └── CommentItem (with replies)
│   │               └── CommentInput
│   ├── ExplorePage
│   │   ├── TrendingHashtags
│   │   └── ExploreFeed (trending posts)
│   ├── ProfilePage
│   │   ├── ProfileHeader (avatar, bio, followers/following)
│   │   ├── FollowButton
│   │   └── PostGrid (user's posts)
│   └── PostDetailPage
│       └── PostCard (full post with all comments)
└── SharedComponents
    ├── UserAvatar
    ├── LikeButton
    ├── CommentInput
    └── ImageViewer
```

### Key Components Explained

**1. FeedList Component**
- Displays personalized feed
- Infinite scroll for pagination
- Real-time updates via WebSocket
- Optimistic updates for likes/comments

**2. PostCard Component**
- Individual post display
- Shows user info, content, engagement
- Like button with real-time count updates
- Comment section with replies
- Share and save functionality

**3. PostComposer Component**
- Create new posts
- Text input with character count
- Image/video upload
- Preview before posting
- Post button with validation

**4. CommentSection Component**
- Display comments with replies
- Comment input for new comments
- Real-time comment updates
- Like comments functionality

**5. EngagementBar Component**
- Like, comment, share, save buttons
- Real-time count updates
- Optimistic updates for instant feedback

---

## 3) Data Models

Here are the key data structures:

```typescript
// User
interface User {
  id: string;
  username: string;
  name: string;
  avatar?: string;
  bio?: string;
  followersCount: number;
  followingCount: number;
  postsCount: number;
  isFollowing: boolean;
}

// Post
interface Post {
  id: string;
  userId: string;
  user: User;
  content: string;
  media?: Media[];
  hashtags: string[];
  likesCount: number;
  commentsCount: number;
  sharesCount: number;
  isLiked: boolean;
  isSaved: boolean;
  createdAt: string;
  location?: string;
}

// Media (image or video)
interface Media {
  id: string;
  type: "image" | "video";
  url: string;
  thumbnailUrl?: string;  // For videos
}

// Comment
interface Comment {
  id: string;
  postId: string;
  userId: string;
  user: User;
  content: string;
  likesCount: number;
  repliesCount: number;
  replies?: Comment[];  // Nested replies
  replyToId?: string;  // If this is a reply
  createdAt: string;
}

// Feed response
interface FeedResponse {
  posts: Post[];
  hasMore: boolean;
  nextCursor?: string;
}

// Like/Unlike request
interface LikeRequest {
  postId: string;
  isLiked: boolean;
}
```

### Data Flow Explanation

**When a user creates a post:**
1. User enters content in PostComposer
2. Optional: Upload images/videos
3. Extract hashtags from content
4. Submit post: POST /api/v1/posts
5. Optimistic update: post appears in feed immediately
6. On success, post is saved; on failure, rollback

**When a user likes a post:**
1. User clicks like button
2. Optimistic update: like count increments, button shows liked
3. API call: POST /api/v1/posts/:id/like
4. WebSocket broadcasts like to all connected clients
5. Other users see updated like count in real-time

**Feed generation:**
1. Fetch posts from followed users
2. Sort by engagement and recency
3. Paginate with cursor-based pagination
4. Infinite scroll loads more posts
5. Real-time updates via WebSocket for new posts

**Real-time updates:**
1. WebSocket connection per user
2. Server broadcasts new posts, likes, comments
3. Frontend receives updates and updates UI
4. Optimistic updates for instant feedback
5. Sync with server state

---

## 4) API Design

### REST Endpoints

**GET /api/v1/feed**
- Get personalized feed
- Query params: `cursor`, `limit`
- Returns: FeedResponse with posts

**POST /api/v1/posts**
- Create a post
- Request body: `{ content: string, media?: Media[], hashtags?: string[] }`
- Returns: Post object

**GET /api/v1/posts/:id**
- Get post details
- Returns: Post object with full details

**POST /api/v1/posts/:id/like**
- Like or unlike a post
- Returns: Updated Post with like status

**GET /api/v1/posts/:id/comments**
- Get post comments
- Query params: `page`, `limit`
- Returns: Paginated list of Comment objects

**POST /api/v1/posts/:id/comments**
- Add a comment
- Request body: `{ content: string, replyToId?: string }`
- Returns: Comment object

**GET /api/v1/users/:id**
- Get user profile
- Returns: User object

**POST /api/v1/users/:id/follow**
- Follow or unfollow a user
- Returns: Updated User with follow status

**GET /api/v1/explore**
- Get explore feed (trending posts)
- Query params: `cursor`, `limit`
- Returns: FeedResponse

**GET /api/v1/hashtags/:tag/posts**
- Get posts by hashtag
- Query params: `cursor`, `limit`
- Returns: FeedResponse

### WebSocket Events

**Connection:** `wss://api.example.com/feed`

**Events:**
- `new_post` - New post from followed user
- `post_liked` - Post was liked
- `comment_added` - New comment on post
- `user_followed` - User followed someone

**Message Format:**
```json
{
  "type": "post_liked",
  "data": {
    "postId": "post_123",
    "likesCount": 1250,
    "userId": "user_456"
  }
}
```

### API Request/Response Examples

**Get Feed:**
```json
// GET /api/v1/feed?cursor=abc123&limit=20
// Response
{
  "success": true,
  "data": {
    "posts": [
      {
        "id": "post_123",
        "userId": "user_456",
        "user": {
          "id": "user_456",
          "username": "johndoe",
          "name": "John Doe",
          "avatar": "https://cdn.example.com/avatar.jpg"
        },
        "content": "Check out this amazing sunset! #sunset #photography",
        "media": [
          {
            "type": "image",
            "url": "https://cdn.example.com/sunset.jpg"
          }
        ],
        "hashtags": ["sunset", "photography"],
        "likesCount": 1250,
        "commentsCount": 45,
        "isLiked": false,
        "createdAt": "2024-01-15T10:00:00Z"
      }
    ],
    "hasMore": true,
    "nextCursor": "xyz789"
  }
}
```

**Like Post:**
```json
// POST /api/v1/posts/post_123/like
// Response
{
  "success": true,
  "data": {
    "id": "post_123",
    "likesCount": 1251,
    "isLiked": true
  }
}
```

---

## Key Design Decisions

**1. Optimistic Updates**
- Show likes/comments immediately (useOptimistic)
- Better perceived performance
- Rollback if API fails
- Instant user feedback

**2. Infinite Scroll**
- Cursor-based pagination
- Load more posts as user scrolls
- Smooth scrolling experience
- Efficient for large feeds

**3. Real-time Updates via WebSocket**
- Instant updates for likes, comments, new posts
- Low latency (< 500ms)
- Better user experience
- Auto-reconnect on connection loss

**4. Feed Generation Strategy**
- Personalized feed from followed users
- Sort by engagement and recency
- Cache feed for performance
- Real-time updates for new posts

**5. Media Optimization**
- Lazy load images and videos
- Use CDN for fast delivery
- Thumbnails for videos
- Responsive images

**6. Hashtag Extraction**
- Extract hashtags from post content
- Link hashtags to hashtag feeds
- Trending hashtags algorithm
- Search by hashtag

---

## Interview Talking Points

**When explaining this system, I'd focus on:**

1. **Requirements First**: Start with core functionality - create posts, follow users, personalized feed, real-time engagement

2. **Component Structure**: Explain the React component hierarchy - feed list, post card, post composer, comment section

3. **Data Models**: Walk through Post, User, Comment - and how they support the feed and engagement features

4. **API Design**: Show the REST endpoints and WebSocket protocol - feed, posts, likes, comments, real-time updates

5. **Key Challenges**: 
   - Real-time updates with low latency
   - Feed generation and personalization
   - Handling viral posts and traffic spikes
   - Optimistic updates for instant feedback
   - Infinite scroll with efficient pagination

**Example explanation flow:**
> "So for a social media feed, the core requirement is allowing users to create posts, follow others, and see a personalized feed. The frontend is a React app with a feed list component that displays posts from followed users. Users can like, comment, and share posts, with real-time updates via WebSocket so changes appear instantly. The data model centers around Post objects with content, media, engagement counts, and User objects with profile information. When a user likes a post, we use optimistic updates to show the like immediately, then sync with the server. The feed uses infinite scroll with cursor-based pagination for efficient loading. Real-time updates are delivered via WebSocket for likes, comments, and new posts. Key challenges include generating personalized feeds efficiently, handling real-time updates at scale, and managing traffic spikes when posts go viral."

---

## 📍 Navigation

<div align="center">

[Home: README](README.md) • [← Previous: Video Streaming Platform](06%29%20Video%20Streaming%20Platform.md) • [Next: E-commerce App →](08%29%20E-commerce%20App.md)

[📋 Cheatsheet](Projects%20Interview%20Cheatsheet.md)

</div>

---
