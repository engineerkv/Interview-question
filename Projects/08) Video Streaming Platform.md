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

## a) Functional Requirements

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

---

## b) Non-Functional Requirements

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

---

## c) MVP (Minimum Viable Product)

### Phase 1: Core Features - Must Have

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

---

## d) Technology Choices

### Frontend Framework

- **React.js** - Component-based UI library for interactive video platform
- **TypeScript** - Type safety for video data, user data, playlists
- **React Router** - Client-side routing for single-page application

### State Management

- **React Query (TanStack Query)** - Server state management, video data caching, refetching
- **Redux Toolkit** (or **Zustand**) - Global state for current video, playlists, watch history
- **Context API** - User authentication, app configuration
- **useState/useReducer** - Local component state

### Video Player

- **Video.js / React Player** - Video player library with adaptive streaming support
- **HLS.js** - HLS (HTTP Live Streaming) support for adaptive bitrate

### UI/UX Libraries

- **Material-UI / Chakra UI** - Component library for faster development
- **React Hot Toast** - Toast notifications for user feedback

### Build Tools

- **Vite** - Fast build tool and dev server
- **Webpack** (alternative) - Module bundler

### Testing

- **React Testing Library** - Component testing
- **Vitest / Jest** - Unit testing framework
- **Playwright / Cypress** - E2E testing

---

## e) Architecture Overview

The frontend follows a layered architecture with video player integration and real-time updates.

**Component Structure:**

```

Frontend Application
├── Presentation Layer
│   ├── UI Components (VideoCard, CommentCard, PlaylistCard, LikeButton)
│   ├── Feature Components (VideoPlayer, VideoUploader, PlaylistManager, SearchBar)
│   └── Layout Components (Header, Sidebar, Navigation, MainLayout)
├── Business/Controller Layer
│   ├── Business Logic (Video validation, metadata formatting, playlist calculations, search filtering)
│   ├── Custom Hooks (useVideo, usePlaylist, useSearch)
│   └── Service Functions (Pure functions for data processing and validation)
├── Video Player Layer
│   ├── Video.js Player (HTML5 video player with adaptive bitrate streaming HLS/DASH)
│   ├── Quality Selection (Automatic quality adjustment based on network speed)
│   └── Playback Controls (Play, pause, seek, volume, fullscreen, playback speed)
├── State Management
│   ├── Client State
│   │   ├── Local State (useState) - Component-specific UI state
│   │   ├── Global State (Redux Toolkit/Zustand) - Current video, playlists, watch history
│   │   └── Context API - User authentication, app configuration
│   └── Server State
│       ├── React Query (useQuery) - API data caching, refetching, optimistic updates
│       └── Service Worker - Offline caching, background sync
├── API Integration
│   ├── API Client (Axios with interceptors for auth, error handling)
│   ├── API Services (videoService, playlistService, userService)
│   └── Request/Response Transformation (Data normalization and error handling)
└── Routing
    ├── Public Routes (Home, Videos)
    ├── Protected Routes (Channel, Upload, Settings)
    └── Route Guards (Authentication and authorization checks)

```

**Frontend Deployment:**

- **Build**: Production bundle with code splitting using Webpack/Vite
- **CDN**: Static assets served from CloudFront/Cloudflare edge locations
- **Caching**: Aggressive caching for static assets, cache-busting for updates
- **Environment**: Environment variables for API endpoints and configs

**Key Frontend Components:**

- **React 19 Application**:
  - Single-page application with client-side routing
  - Component-based architecture for reusability
  - React Query with React 19 hooks (useOptimistic, useTransition, useDeferredValue)
  - Video player with adaptive streaming
  - Responsive design for mobile and desktop
  - Modern React 19 features for better performance and UX

- **CDN/Edge**:
  - Global distribution of static assets
  - Edge caching for improved performance
  - DDoS protection and rate limiting at edge

---

## f) App Flow

### Complete System Flow (Frontend Perspective)

**Primary User Flow - Video Streaming Platform:**

1. **User lands on homepage** → React Router renders HomePage component
2. **User enters URL** → URLInput component captures input, validates in real-time
3. **User clicks submit** → Form triggers React Query mutation
4. **Loading state** → SubmitButton shows loading spinner, form disabled
5. **API call** → useMutation sends POST request to /api/v1/shorten
6. **Success response** → React Query caches response, itemDisplay component renders
7. **User copies URL** → CopyButton uses Clipboard API, shows toast notification
8. **State update** → Components re-render with new item data

**Component Interaction Flow:**

```

User Input → URLInput (local state)
            ↓
Form Submit → Form (React Query mutation)
            ↓
API Call → useShortenURL hook (business logic)
            ↓
Response → React Query cache update
            ↓
Re-render → itemDisplay (receives cached data)

```

**State Update Flow:**

1. **Local State** → URLInput uses useState for input value
2. **Server State** → React Query manages API response, caching, refetching
3. **Global State** → Context API manages user authentication, theme
4. **Component Re-render** → React updates UI based on state changes

**Error Handling Flow:**

1. **API Error** → React Query mutation returns error
2. **Error Boundary** → Catches component errors, shows fallback UI
3. **User Feedback** → Toast notification displays error message
4. **Retry Logic** → User can retry failed requests

**Analytics Dashboard Flow:**

1. **User navigates** → React Router navigates to /dashboard
2. **Data Fetching** → React Query useQuery fetches analytics data
3. **Loading State** → Skeleton screens displayed while loading
4. **Data Display** → Charts render with analytics data
5. **Real-time Updates** → Polling every 30 seconds for active URLs
6. **User Interactions** → Filters update query params, trigger refetch

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
│   ├── HomePage
│   │   ├── Form
│   │   │   ├── URLInput
│   │   │   ├── AliasInput (optional)
│   │   │   └── SubmitButton
│   │   └── itemDisplay
│   │       ├── itemCard
│   │       ├── CopyButton
│   │       └── QRCodeButton
│   ├── DashboardPage
│   │   ├── URLList
│   │   │   └── URLItem
│   │   └── AnalyticsDashboard
│   │       ├── ClickCountChart
│   │       ├── CountryChart
│   │       └── DateRangeFilter
│   └── AnalyticsPage
└── SharedComponents
    ├── Button
    ├── Input
    ├── Card
    ├── Toast
    └── LoadingSpinner

```

**Key React Components:**

**1. Form Component:**

- Handles form submission logic
- Manages form state with useState
- Uses React Query mutation for API call
- Validates input before submission

**2. itemDisplay Component:**

- Displays generated item
- Handles copy to clipboard functionality
- Shows QR code generation
- Manages display state (expanded/collapsed)

**3. AnalyticsDashboard Component:**

- Fetches analytics data with React Query
- Renders charts and statistics
- Handles date range filtering
- Updates data in real-time via polling

**4. URLList Component:**

- Displays list of shortened URLs
- Implements virtual scrolling for performance
- Handles pagination
- Supports search and filtering

**Component Communication:**

- **Props** → Parent to child data flow
- **Callbacks** → Child to parent communication
- **Context API** → Shared state across components
- **React Query** → Server state management

# 4) Data Models

### TypeScript Interfaces

```typescript
interface item {
  shortCode: string;
  originalUrl: string;
  item: string;
  expiresAt?: string;
  createdAt: string;
}

interface Analytics {
  shortCode: string;
  clickCount: number;
  uniqueClicks: number;
  topCountries: Array<{ country: string; clicks: number }>;
  clicksByDate: Array<{ date: string; clicks: number }>;
}

```

# 5) API Design

## Adaptive Bitrate Selection Algorithm

**Purpose:** Automatically select optimal video quality based on network conditions and buffer state.

**Algorithm:**

1. Monitor network bandwidth and buffer level
2. Calculate available bandwidth (bytes downloaded / time)
3. Select quality level that matches available bandwidth
4. Switch to higher quality if buffer is sufficient
5. Switch to lower quality if buffer is depleting

**Implementation:**

```javascript
class AdaptiveBitrateSelector {
 private qualities = ['360p', '720p', '1080p', '4K'];
 private currentQuality = 0;
 private bufferThreshold = 10; // seconds

 selectQuality(networkSpeed, bufferLevel){
 // Calculate target quality based on network speed
 let targetQuality = 0;
 if (networkSpeed > 10000000) targetQuality = 3; // 4K
 else if (networkSpeed > 5000000) targetQuality = 2; // 1080p
 else if (networkSpeed > 2000000) targetQuality = 1; // 720p
 else targetQuality = 0; // 360p

 // Adjust based on buffer level
 if (bufferLevel < this.bufferThreshold && this.currentQuality > 0) {
 targetQuality = Math.max(0, this.currentQuality - 1);
 } else if (bufferLevel > this.bufferThreshold * 2 && targetQuality > this.currentQuality) {
 targetQuality = Math.min(3, this.currentQuality + 1);
 }

 this.currentQuality = targetQuality;
 return this.qualities[targetQuality];
 }
}

```

**Complexity:**

- Time: O(1) for quality selection
- Space: O(1)
- **Adaptive Quality:** Improves playback experience based on network conditions

---

## Video Recommendation Algorithm

**Purpose:** Recommend videos to users based on watch history, preferences, and trending content.

**Algorithm:**

1. Collect user watch history and preferences
2. Calculate similarity scores with other users (collaborative filtering)
3. Calculate content-based similarity (tags, category, channel)
4. Combine scores with weighted formula
5. Rank videos by recommendation score

**Implementation:**

```javascript
function recommendVideos(userId, watchHistory: Video[]): Video[] {
 // Collaborative filtering
 const similarUsers = findSimilarUsers(userId);
 const collaborativeScore = calculateCollaborativeScore(similarUsers);

 // Content-based filtering
 const userPreferences = extractPreferences(watchHistory);
 const contentScore = calculateContentScore(userPreferences);

 // Trending boost
 const trendingScore = calculateTrendingScore();

 // Combined score
 const finalScore = collaborativeScore * 0.4 + contentScore * 0.4 + trendingScore * 0.2;

 return videos.sort((a, b) => b.finalScore - a.finalScore);
}

```

**Complexity:**

- Time: O(n * m) where n is users, m is videos
- Space: O(n + m)
- **Recommendation Quality:** Hybrid approach improves recommendation accuracy

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

**Custom Hook Example:**

```typescript
function useShortenURL() {
  return useMutation({
    mutationFn: (url: string) => shortenUrl(url),
    onSuccess: () => queryClient.invalidateQueries(["urls"])
  });
}

```

**Component with React Query:**

```typescript
function Form() {
  const { mutate, isPending } = useShortenURL();
  const [url, setUrl] = useState("");

  const handleSubmit = (e: FormEvent) => {
    e.preventDefault();
    mutate(url);
  };

  return <form onSubmit={handleSubmit}>...</form>;
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
- Example: `useShortenURL`, `useAnalytics`, `useAliasCheck`

**Service Functions:**

- Pure functions for data processing and validation
- URL validation, data transformation, format checking

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
- Example: Test Video Streaming Platform flow from start to finish

# 8) Algorithms

### Frontend Algorithms

**URL Validation Algorithm:**

```javascript
function isValidUrl(url) {
  try {
    new URL(url);
    return url.startsWith("http://") || url.startsWith("https://");
  } catch {
    return false;
  }
}

```

**Debouncing Algorithm:**

```javascript
function debounce(func, delay) {
  let timeoutId;
  return (...args) => {
    clearTimeout(timeoutId);
    timeoutId = setTimeout(() => func(...args), delay);
  };
}

```

# 9) Security

### Frontend Security

**Input Validation:**

- Client-side validation before form submission
- Sanitize user input to prevent XSS attacks
- Validate data formats (URLs, emails, custom aliases)

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

**Situation:** In a Video Streaming Platform system, we need to manage both client-side UI state and server-side data efficiently.

**Action:**

- Use React Query for server state (URL data, analytics) - handles caching, refetching, and synchronization
- Use useState for local component state (form inputs, modal visibility)
- Use Context API for global client state (user authentication, theme preferences)
- Implement optimistic updates for better UX

**Result:** Reduced API calls through caching, improved performance, better user experience with instant feedback.

**Takeaway:** Separating client and server state management leads to cleaner code and better performance.
