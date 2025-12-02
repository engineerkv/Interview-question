# News Media Feed (Facebook, Twitter) - Low Level Design (LLD)

> **Project Type:** Full-Stack Web Application (MERN Stack)  
> **Tech Stack:** 
> - **Frontend:** React.js, TypeScript, React Router, Redux Toolkit, Axios, Material-UI, Socket.io Client
> - **Backend:** Node.js, Express.js, MongoDB, Redis, Socket.io Server, JWT
> - **Services:** AWS S3, CDN

---

## 3. Component Architecture

**Think of this as the building blocks - how components are organized and connected**

### Component Hierarchy (React.js)

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

## 4. Data Models

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

## 5. Data APIs

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

## 6. Backend Implementation Details

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

---

## 7. Implementation Details

**Note:** Implementation details are split between frontend (React.js) and backend (Node.js/Express.js).

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

## 8. Performance Optimizations

**Frontend Optimizations:** React.js code splitting, lazy loading, infinite scroll  
**Backend Optimizations:** Database indexing, Redis caching, feed pre-computation

### Feed Optimization

- **Feed Caching:** Cache user feeds in Redis for fast retrieval
- **Feed Pre-computation:** Pre-compute feeds for active users
- **Lazy Loading:** Load images as user scrolls
- **Virtual Scrolling:** For very long feeds

