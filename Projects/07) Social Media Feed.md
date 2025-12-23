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

---

## a) Functional Requirements

#### User Management

- **User registration and authentication** - Email, phone, or social login
- **User profiles** - Profile pages with bio, avatar, followers/following counts
- **Follow/Unfollow** - Follow other users, see their posts in feed

#### Post Management

- **Create posts** - Text posts, image posts, video posts
- **Edit/Delete posts** - Users can edit or delete their own posts
- **Post engagement** - Like, comment, share, save posts
- **Post media** - Upload images and videos with optimization

#### Feed Generation

- **Personalized feed** - Show posts from followed users
- **Trending feed** - Show trending posts based on engagement
- **Explore feed** - Discover new content and users
- **Hashtag feeds** - View posts by hashtag

#### Real-time Features

- **Real-time likes** - See likes update in real-time via WebSocket
- **Real-time comments** - See new comments appear instantly
- **Real-time notifications** - Get notified of new interactions
- **Typing indicators** - See when users are typing comments

#### Content Discovery

- **Search** - Search users, posts, hashtags
- **Hashtags** - Tag posts with hashtags for discovery
- **Trending topics** - See what's trending
- **Recommendations** - Personalized user and content recommendations

---

## b) Non-Functional Requirements

#### Performance

- **Fast feed loading** - Feed loads in < 1 second
- **Smooth infinite scroll** - Seamless scrolling with pagination
- **Optimized media** - Images and videos load efficiently with CDN
- **Low latency** - Real-time updates delivered in < 500ms

#### Scalability

- **Handle millions of users** - Support large user base
- **Billions of posts** - Efficiently store and retrieve posts
- **High concurrency** - Handle thousands of concurrent real-time connections
- **Traffic spikes** - Handle viral posts and trending content

#### Reliability

- **99.9% uptime** - High availability
- **Fault tolerance** - System continues working if components fail
- **Data consistency** - Maintain engagement metrics accurately

#### User Experience

- **Responsive design** - Works on mobile and desktop
- **Accessibility** - ARIA labels, keyboard navigation
- **Intuitive UI** - Easy to use, familiar patterns
- **Fast interactions** - Instant feedback on likes, comments

---

## c) MVP (Minimum Viable Product)

### Phase 1: MVP (Must Have) - Priority 1

**Core Features:**

- User registration and authentication
- Create text and image posts
- View personalized feed (posts from followed users)
- Like and comment on posts
- Follow/unfollow users
- Basic user profiles
- Real-time updates for likes and comments (WebSocket)

### Phase 2: Enhanced Features - Priority 2

**Advanced Features:**

- Video posts
- Share and save posts
- Hashtag support
- Search functionality
- Trending feed
- Explore feed
- Post editing and deletion
- Advanced user profiles

---

## d) Technology Choices

### Frontend Framework

- **React 19** - Latest React version with useOptimistic, useActionState, useTransition, useDeferredValue, and use() hook
- **TypeScript** - Type safety and better developer experience - Component-based UI framework with type safety

### State Management

- **React Query (TanStack Query)** - Server state management
- **Redux Toolkit** - Client state management
- **Context API** - App-wide configuration

### UI/UX Libraries

- **React Router** - Client-side routing
- **React Hot Toast** - Toast notifications

### Build Tools

- **Vite** - Fast build tool

### Testing

- **React Testing Library** - Component testing
- **Vitest** - Unit testing
- **Playwright** - E2E testing

### Deployment

- **Vercel/Netlify** - Static site hosting
- **AWS S3 + CloudFront** - Alternative deployment

**Trade-offs:**

- **React Query vs SWR**: React Query provides better caching
- **Redux Toolkit vs Zustand**: Redux Toolkit offers better DevTools

---

## e) Architecture Overview

The frontend follows a layered architecture optimized for social media feed operations with real-time updates.

**Component Structure:**

```

Frontend Application
├── Presentation Layer
│   ├── UI Components (PostCard, CommentCard, LikeButton, ShareButton)
│   ├── Feature Components (FeedList, PostComposer, CommentThread, UserProfile)
│   └── Layout Components (Header, Sidebar, Navigation, MainLayout)
├── Business/Controller Layer
│   ├── Business Logic (Post validation, content formatting, data transformation)
│   ├── Custom Hooks (useFeed, usePost, useComments, useLikes)
│   └── Service Functions (Pure functions for data processing and validation)
├── State Management
│   ├── Client State
│   │   ├── Local State (useState) - Component-specific UI state
│   │   ├── Global State (Redux Toolkit/Zustand) - Feed state, user preferences
│   │   └── Context API - User authentication, app configuration
│   └── Server State
│       ├── React Query (useQuery/useMutation) - API data caching, refetching, optimistic updates
│       └── Service Worker - Offline caching, background sync
├── API Integration
│   ├── API Client (Axios with interceptors for auth, error handling)
│   ├── API Services (feedService, postService, commentService)
│   └── Request/Response Transformation (Data normalization and error handling)
└── Routing
    ├── Public Routes (Home, Feed)
    ├── Protected Routes (Profile, Settings)
    └── Route Guards (Authentication and authorization checks)

```

**Frontend Deployment:**

- **Build**: Production bundle with code splitting using Vite
- **CDN**: Static assets served from CloudFront/Cloudflare edge locations
- **Caching**: Aggressive caching for static assets, cache-busting for updates
- **Environment**: Environment variables for API endpoints and feature flags

**Key Frontend Components:**

- **React 19 Application**:
  - Single-page application with client-side routing
  - Component-based architecture for reusability
  - React Query with React 19 hooks (useOptimistic, useTransition, useDeferredValue)
  - Infinite scroll for feed loading
  - Responsive design for mobile and desktop
  - Modern React 19 features for better performance and UX

- **CDN/Edge**:
  - Global distribution of static assets
  - Edge caching for improved performance
  - DDoS protection and rate limiting at edge

---

## f) App Flow

### Complete System Flow (Frontend Perspective)

**Primary User Flow - Viewing Feed:**

1. **User opens app** → React Router renders FeedPage component
2. **Feed loading** → FeedList component fetches posts with React Query useSuspenseQuery (React 19)
3. **Posts display** → PostCard components render posts with images, text, engagement counts
4. **User scrolls** → Infinite scroll triggers pagination, loads more posts
5. **User likes post** → LikeButton triggers useOptimistic (React 19) for instant like update
6. **Real-time update** → WebSocket receives like update, syncs with server
7. **User comments** → CommentInput opens, user types comment
8. **Comment submission** → useActionState (React 19) handles form, shows comment immediately

**Component Interaction Flow:**

```
User Opens App → FeedPage (React Router)
            ↓
Feed Loading → FeedList (React Query useSuspenseQuery)
            ↓
Post Display → PostCard (renders post data)
            ↓
User Likes → LikeButton (useOptimistic for instant UI)
            ↓
WebSocket Update → Real-time sync with server
            ↓
State Update → Redux Toolkit (engagement counts)
```

**State Update Flow:**

1. **Local State** → Post composer, comment input use useState
2. **Optimistic State** → useOptimistic (React 19) shows likes/comments immediately
3. **Server State** → React Query manages posts, comments, caching, refetching
4. **Global State** → Redux Toolkit manages feed state, user preferences
5. **Real-time State** → WebSocket updates engagement metrics in real-time
6. **Component Re-render** → React updates UI based on state changes

**Error Handling Flow:**

1. **API Error** → React Query mutation returns error
2. **Error Boundary** → Catches component errors, shows fallback UI
3. **User Feedback** → Toast notification displays error message
4. **Retry Logic** → User can retry failed requests
5. **WebSocket Error** → Connection retries automatically, shows connection status

**Post Creation Flow:**

1. **User clicks compose** → PostComposer modal opens
2. **User types content** → TextInput captures post text
3. **User adds media** → ImageUploader handles image upload with preview
4. **User submits** → PostComposer uses useActionState (React 19) for form handling
5. **Optimistic update** → useOptimistic (React 19) shows post in feed immediately
6. **API call** → useMutation sends POST request to /api/v1/posts
7. **Success response** → React Query cache updates, post persists
8. **Feed update** → FeedList re-renders with new post

**Real-time Engagement Flow:**

1. **User likes post** → LikeButton triggers optimistic update
2. **Instant UI** → useOptimistic (React 19) shows like immediately
3. **WebSocket event** → Server broadcasts like to all connected clients
4. **State sync** → Redux Toolkit updates engagement count
5. **UI update** → PostCard shows updated like count
6. **Comment added** → Similar flow for comments with real-time updates

# 3) Component Architecture

Think of the frontend as a tree of React components - each component handles a specific part of the UI, and they work together to create the complete user experience.

**Component Hierarchy:**

```

App
├── Layout
│   ├── Header
│   │   ├── Logo
│   │   ├── Navigation
│   │   └── UserMenu
│   ├── MainContent
│   └── Footer
├── Pages
│   ├── FeedPage
│   │   ├── FeedList
│   │   │   └── PostCard
│   │   │       ├── PostHeader
│   │   │       ├── PostContent
│   │   │       ├── PostMedia
│   │   │       ├── PostActions
│   │   │       │   ├── LikeButton
│   │   │       │   ├── CommentButton
│   │   │       │   └── ShareButton
│   │   │       └── CommentThread
│   │   └── PostComposer
│   ├── ProfilePage
│   │   ├── ProfileHeader
│   │   ├── ProfileStats
│   │   └── UserPostsGrid
│   ├── ExplorePage
│   │   ├── TrendingHashtags
│   │   └── TrendingPosts
│   └── SearchPage
│       ├── SearchBar
│       ├── SearchResults
│       └── SearchFilters
└── SharedComponents
    ├── Button
    ├── Input
    ├── Card
    ├── Toast
    └── LoadingSpinner
```

**Key React Components:**

**1. FeedList Component:**

- Displays feed of posts with infinite scroll
- Fetches posts with React Query useSuspenseQuery (React 19)
- Handles pagination and loading states
- Uses useTransition (React 19) for non-urgent updates
- Implements virtual scrolling for performance

**2. PostCard Component:**

- Displays individual post with author, content, media
- Handles like, comment, share interactions
- Uses useOptimistic (React 19) for instant engagement updates
- Shows engagement counts (likes, comments, shares)
- Links to post detail or author profile

**3. PostComposer Component:**

- Allows creating new posts with text and media
- Handles image upload with preview
- Uses useActionState (React 19) for form submission
- Validates post content before submission
- Shows character count and media preview

**4. LikeButton Component:**

- Handles like/unlike functionality
- Uses useOptimistic (React 19) for instant UI feedback
- Updates like count immediately
- Syncs with server via WebSocket
- Shows liked state with visual feedback

**5. CommentThread Component:**

- Displays comments for a post
- Handles adding new comments
- Uses useOptimistic (React 19) for instant comment display
- Shows comment author, text, timestamp
- Handles nested replies

**Component Communication:**

- **Props** → Parent to child data flow
- **Callbacks** → Child to parent communication
- **Context API** → Shared state across components (theme, user)
- **React Query** → Server state management (posts, comments, users)
- **Redux Toolkit** → Global client state (feed state, engagement counts)
- **WebSocket** → Real-time engagement updates

# 4) Data Models

### TypeScript Interfaces

```typescript
interface Post {
  id: string;
  userId: string;
  author: User;
  content: string;
  media?: Media[];
  hashtags?: string[];
  likes: number;
  comments: number;
  shares: number;
  isLiked: boolean;
  isSaved: boolean;
  createdAt: string;
  updatedAt: string;
}

interface User {
  id: string;
  username: string;
  displayName: string;
  avatar: string;
  bio?: string;
  followersCount: number;
  followingCount: number;
  postsCount: number;
  isFollowing: boolean;
  isVerified: boolean;
}

interface Comment {
  id: string;
  postId: string;
  userId: string;
  author: User;
  content: string;
  likes: number;
  replies?: Comment[];
  createdAt: string;
}

interface Media {
  id: string;
  type: "image" | "video";
  url: string;
  thumbnail?: string;
  width?: number;
  height?: number;
}

interface Feed {
  posts: Post[];
  hasMore: boolean;
  nextCursor?: string;
}

interface FormState {
  content: string;
  media: Media[];
  hashtags: string[];
  errors: {
    content?: string;
    media?: string;
  };
}
```

# 5) API Design

*Note: Frontend algorithms focus on client-side processing.*

## Feed Pagination Algorithm

**Purpose:** Efficiently paginate feed content for infinite scroll.

**Implementation:**

```typescript
function paginateFeed(posts: Post[], page: number, limit: number): PaginatedResult {
  const start = (page - 1) * limit;
  const end = start + limit;
  return {
    posts: posts.slice(start, end),
    hasMore: end < posts.length,
    nextPage: page + 1
  };
}

```

---

# 6) Protocols

### REST API Protocol

**Request Format:**

## iii) Implementation Details

### Business/Controller Layer

**Custom Hooks:**

- Encapsulate business logic and API calls
- Example: `useShortenURL`, `useAnalytics`, `useAliasCheck`
- Handle data transformation and validation

**Service Functions:**

- Pure functions for data processing and validation
- URL validation, data transformation, format checking
- Reusable across components

### Advanced Component Patterns

**Compound Components:**

- Group related components together (e.g., Form.Input, Form.Button)
- Share implicit state between components

**Render Props Pattern:**

- Pass render functions as props for flexible component composition

**Custom Hooks Pattern:**

- Extract reusable logic into custom hooks
- Example: `useShortenURL`, `useAnalytics`, `useCopyToClipboard`

**Higher-Order Components (HOCs):**

- Wrap components with additional functionality
- Example: `withAuth`, `withLoading`

### Performance Optimizations

- **Code splitting** with React.lazy() and Suspense
- **Memoization** with useMemo() and useCallback()
- **Virtual scrolling** for long lists (react-window, react-virtuoso)
- **Image optimization** and lazy loading
- **Debouncing and throttling** for user inputs
- **React.memo** for preventing unnecessary re-renders

### UI/UX Enhancements

- **Toast notifications** for user feedback (react-hot-toast)
- **Loading states** and skeleton screens
- **Error boundaries** for error handling
- **Responsive design** for mobile and desktop
- **Accessibility features** (ARIA labels, keyboard navigation, focus management)
- **Animations** with Framer Motion or CSS transitions

### Code Examples

**Custom Hook: useLikePost (React 19)**

```typescript
import { useOptimistic, useTransition } from 'react';
import { useMutation, useQueryClient } from '@tanstack/react-query';

function useLikePost(postId: string) {
  const queryClient = useQueryClient();
  const [optimisticLikes, addOptimisticLike] = useOptimistic(
    0,
    (currentLikes, action: 'like' | 'unlike') =>
      action === 'like' ? currentLikes + 1 : currentLikes - 1
  );
  const [isPending, startTransition] = useTransition();

  return useMutation({
    mutationFn: async (action: 'like' | 'unlike') => {
      addOptimisticLike(action);
      return await toggleLike(postId, action);
    },
    onSuccess: () => {
      queryClient.invalidateQueries({ queryKey: ['post', postId] });
    }
  });
}
```

**Component with React Query (React 19):**

```typescript
function LikeButton({ post }: { post: Post }) {
  const [isPending, startTransition] = useTransition();
  const likeMutation = useLikePost(post.id);

  const handleLike = () => {
    startTransition(() => {
      likeMutation.mutate(post.isLiked ? 'unlike' : 'like');
    });
  };

  return (
    <button onClick={handleLike} disabled={isPending}>
      {post.isLiked ? '❤️' : '🤍'} {post.likes}
    </button>
  );
}
```

# 7) Low Level Design (LLD)

## ii) State Management

### Client State

**Local State (useState):**

- Component-specific UI state (form inputs, modal visibility, loading states)
- Example: `const [isOpen, setIsOpen] = useState(false);`

**Global State:**

- Redux Toolkit OR Zustand for complex global state
- Context API for user authentication, theme preferences
- Example: User preferences, app configuration

### Server State

**React Query (TanStack Query):**

- `useQuery` for data fetching and caching
- `useMutation` for data mutations (create, update, delete)
- Automatic refetching, background updates, optimistic updates
- Example: API data caching, synchronization

## iii) Implementation Details

### Business/Controller Layer

**Custom Hooks:**

- Encapsulate business logic and API calls
- Example: `useFeed`, `usePost`, `useComments`, `useLikes`, `useFollow`
- Handle data transformation and validation

**Service Functions:**

- Pure functions for data processing and validation
- Post content validation, hashtag extraction, engagement count formatting

### Performance Optimizations

- Code splitting with React.lazy()
- Memoization with useMemo() and useCallback()
- Virtual scrolling for long lists
- Image optimization and lazy loading
- Debouncing and throttling for user inputs

### UI/UX Enhancements

- Toast notifications for user feedback
- Loading states and skeleton screens
- Error boundaries for error handling
- Responsive design for mobile and desktop
  - Modern React 19 features for better performance and UX
- Accessibility features (ARIA labels, keyboard navigation)

## iv) Testing

### Component Testing

- React Testing Library for component tests
- Test user interactions and component behavior
- Example: Test form submission, button clicks, input validation

### Integration Testing

- Test component interactions
- Test API integration with mock data
- Test state management flows

### E2E Testing

- Playwright or Cypress for end-to-end tests
- Test complete user flows
- Example: Test Social Media Feed flow from start to finish

# 8) Algorithms

### Frontend Algorithms

**Hashtag Extraction Algorithm:**

```javascript
function extractHashtags(text) {
  const hashtagRegex = /#[\w]+/g;
  const matches = text.match(hashtagRegex);
  return matches ? matches.map(tag => tag.substring(1)) : [];
}
```

**Post Content Validation:**

```javascript
function validatePostContent(content, maxLength = 280) {
  if (!content || content.trim().length === 0) {
    return { valid: false, error: 'Post cannot be empty' };
  }
  if (content.length > maxLength) {
    return { valid: false, error: `Post exceeds ${maxLength} characters` };
  }
  return { valid: true };
}
```

**Engagement Count Formatting:**

```javascript
function formatEngagementCount(count) {
  if (count >= 1000000) {
    return `${(count / 1000000).toFixed(1)}M`;
  }
  if (count >= 1000) {
    return `${(count / 1000).toFixed(1)}K`;
  }
  return count.toString();
}
```

**Debouncing Algorithm (for search):**

```javascript
function debounce(func, delay) {
  let timeoutId;
  return (...args) => {
    clearTimeout(timeoutId);
    timeoutId = setTimeout(() => func(...args), delay);
  };
}
```

**Infinite Scroll Pagination:**

```javascript
function useInfiniteScroll(callback, hasMore) {
  const observerRef = useRef();
  const lastElementRef = useCallback((node) => {
    if (observerRef.current) observerRef.current.disconnect();
    observerRef.current = new IntersectionObserver(entries => {
      if (entries[0].isIntersecting && hasMore) {
        callback();
      }
    });
    if (node) observerRef.current.observe(node);
  }, [callback, hasMore]);
  return lastElementRef;
}
```

# 9) Security

### Frontend Security

**Input Validation:**

- Client-side validation before post submission
- Sanitize post content to prevent XSS attacks
- Validate post length, media file types, hashtag formats

**XSS Prevention:**

- React automatically escapes content
- Use `dangerouslySetInnerHTML` only when necessary with sanitization
- Content Security Policy (CSP) headers

**CSRF Protection:**

- SameSite cookies for authentication
- CSRF tokens for state-changing operations
- Verify origin header on API requests

**Secure Storage:**

- Never store sensitive data in localStorage
- Use httpOnly cookies for authentication tokens
- Clear sensitive data on logout

**HTTPS:**

- All API calls over HTTPS
- Enforce HTTPS in production
- HSTS headers for security

**Rate Limiting (Client-Side):**

- Debounce API calls to prevent abuse
- Show user-friendly messages when rate limited
- Implement exponential backoff for retries

# 10) Deployment and DevOps

### Frontend Deployment

**Build Optimization:**

- Production build with code splitting and tree shaking
- Minification and compression
- Asset optimization (images, fonts)
- Environment variables for API endpoints

**CI/CD Pipeline:**

- Automated testing on pull requests
- Build and deploy on merge to main
- Preview deployments for feature branches
- Rollback capabilities

**Deployment Platforms:**

- Vercel / Netlify for static site hosting with CDN
- AWS S3 + CloudFront for alternative deployment
- GitHub Pages for simple static sites

**Monitoring:**

- Error tracking (Sentry, LogRocket)
- Performance monitoring (Web Vitals)
- Analytics (user behavior, page views)

# 11) Interview Answers (Frontend Focus)

### Q: How would you handle state management for this system?

**Answer (STAR Method):**

**Situation:** In a social media feed system, we need to manage posts, engagement metrics (likes, comments), real-time updates, and user interactions efficiently.

**Action:**

- Use React Query for server state (posts, comments, users) - handles caching, refetching, and synchronization
- Use `useOptimistic()` (React 19) for instant engagement updates (likes, comments) before server confirmation
- Use WebSocket for real-time engagement updates
- Use Redux Toolkit for global client state (feed state, engagement counts)
- Use useState for local component state (post composer, comment input)
- Use Context API for user authentication, theme preferences

**Result:** Real-time engagement updates, reduced API calls through caching, improved performance, better user experience with instant feedback.

**Takeaway:** Combining React Query for server state, React 19's optimistic updates for engagement, and WebSocket for real-time sync provides seamless social media experience.

### Q: How would you implement real-time engagement updates?

**Answer (STAR Method):**

**Situation:** Users need to see likes and comments update in real-time as other users interact with posts.

**Action:**

- Use WebSocket (Socket.io) for real-time connection
- Use `useOptimistic()` (React 19) to show likes/comments immediately before server confirmation
- Use `useTransition()` (React 19) for non-urgent feed updates
- Implement connection retry logic with exponential backoff
- Show connection status indicator
- Sync optimistic updates with WebSocket events

**Result:** Engagement updates delivered in < 500ms, instant UI feedback, improved user engagement, reliable real-time delivery.

**Takeaway:** WebSocket combined with React 19's optimistic updates provides the best real-time engagement experience for social media feeds.
