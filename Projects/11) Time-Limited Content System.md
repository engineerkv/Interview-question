# Time-Limited Content System

---

## 📍 Navigation

<div align="center">

[Home: README](README.md) • [← Previous: Real-Time Collaboration System](10%29%20Real-Time%20Collaboration%20System.md) • [Next: Ticket Booking System →](12%29%20Ticket%20Booking%20System.md)

[📋 Cheatsheet](Projects%20Interview%20Cheatsheet.md)

</div>

---

## Overview

Design a time-limited content system like Instagram Stories where users can create content (images, videos) that automatically expires after a configurable duration (e.g., 24 hours), with view tracking and engagement features.

---

## 1) Requirements

### Functional Requirements

**Core Features:**
- Create time-limited content (images, videos, stories)
- Configurable expiration duration (default 24 hours)
- Automatic expiration and cleanup
- View content before expiration
- View tracking (who viewed and when)
- Content reactions (likes, replies)
- Content feed (browse stories)
- Expiration countdown display
- Content sharing links

**Advanced Features:**
- Multiple content types (images, videos, text)
- Content analytics (views, engagement)
- Personalized content feed
- Content moderation
- Custom expiration durations

### Non-Functional Requirements

**Performance:**
- Content upload: < 5 seconds
- Viewing latency: < 2 seconds
- Fast feed loading

**Scalability:**
- Handle 1B+ users
- 500M+ content items per day
- Millions of concurrent viewers

**Reliability:**
- 99.9% uptime
- Reliable expiration handling
- Accurate expiration timing

---

## 2) Component Hierarchy

The frontend is a React application for time-limited content. Here's the structure:

```
App
├── Layout
│   ├── Header
│   │   ├── Logo
│   │   └── UserMenu
│   └── MainContent
├── Pages
│   ├── StoriesFeedPage
│   │   ├── StoriesList (horizontal scroll)
│   │   │   └── StoryCircle
│   │   │       ├── UserAvatar
│   │   │       └── UnreadIndicator
│   │   └── StoryViewer
│   │       ├── StoryContent (image/video)
│   │       ├── CountdownTimer
│   │       ├── ViewList (who viewed)
│   │       └── ReactionButtons
│   ├── CreateStoryPage
│   │   ├── MediaUploader
│   │   ├── ExpirationSelector
│   │   └── PublishButton
│   └── StoryAnalyticsPage
│       └── AnalyticsDashboard
└── SharedComponents
    ├── StoryViewer
    ├── CountdownTimer
    └── MediaViewer
```

### Key Components Explained

**1. StoryViewer Component**
- Displays story content (image/video)
- Shows countdown timer
- Auto-advances to next story
- Swipe navigation
- View tracking

**2. StoriesList Component**
- Horizontal scrollable list
- Story circles with avatars
- Unread indicators
- Click to view story

**3. CountdownTimer Component**
- Shows time until expiration
- Updates in real-time
- Visual countdown display

---

## 3) Data Models

Here are the key data structures:

```typescript
// Story (time-limited content)
interface Story {
  id: string;
  userId: string;
  user: User;
  type: "image" | "video" | "text";
  mediaUrl: string;
  expiresAt: string;
  createdAt: string;
  viewsCount: number;
  reactionsCount: number;
  isViewed: boolean;  // By current user
}

// Story view
interface StoryView {
  id: string;
  storyId: string;
  userId: string;
  viewedAt: string;
}

// Story reaction
interface StoryReaction {
  id: string;
  storyId: string;
  userId: string;
  type: "like" | "reply";
  content?: string;  // For replies
  createdAt: string;
}
```

### Data Flow Explanation

**When a user creates a story:**
1. User uploads image/video
2. User selects expiration duration
3. Story is created with expiresAt timestamp
4. Story appears in feed
5. Automatic cleanup when expired

**When a user views a story:**
1. User clicks story circle
2. StoryViewer displays content
3. View is tracked (who, when)
4. Countdown timer shows remaining time
5. Story marked as viewed

---

## 4) API Design

### REST Endpoints

**GET /api/v1/stories**
- Get stories feed
- Returns: Array of Story objects

**POST /api/v1/stories**
- Create a story
- Request: Multipart form data with media and expiration
- Returns: Story object

**GET /api/v1/stories/:id**
- Get story details
- Returns: Story object

**POST /api/v1/stories/:id/view**
- Track story view
- Returns: StoryView object

**POST /api/v1/stories/:id/reactions**
- Add reaction (like/reply)
- Request body: `{ type: string, content?: string }`
- Returns: StoryReaction object

---

## Key Design Decisions

**1. Automatic Expiration**
- Stories expire at configured time
- Server-side cleanup of expired content
- Frontend hides expired stories
- Accurate expiration timing

**2. View Tracking**
- Track who viewed and when
- Privacy controls for view tracking
- Analytics for creators

**3. Countdown Timer**
- Real-time countdown display
- Updates every second
- Visual indicator of remaining time

---

## Interview Talking Points

**When explaining this system, I'd focus on:**

1. **Requirements First**: Start with core functionality - create time-limited content, automatic expiration, view tracking

2. **Component Structure**: Explain the React component hierarchy - stories feed, story viewer, countdown timer

3. **Data Models**: Walk through Story, StoryView, StoryReaction - and expiration handling

4. **API Design**: Show the REST endpoints - create story, view story, track views, reactions

5. **Key Challenges**: 
   - Automatic expiration and cleanup
   - Accurate expiration timing
   - View tracking and privacy
   - Handling millions of concurrent viewers

**Example explanation flow:**
> "So for a time-limited content system like Stories, the core requirement is allowing users to create content that automatically expires after a set duration. The frontend is a React app with a stories feed showing story circles for each user, and a story viewer that displays content with a countdown timer. When a user creates a story, they upload media and set an expiration duration (default 24 hours). The story has an expiresAt timestamp, and the frontend shows a countdown timer. When expired, stories are hidden and cleaned up. View tracking records who viewed each story and when. The data model centers around Story objects with expiration timestamps, StoryView objects for tracking, and StoryReaction objects for engagement. The main API endpoints handle creating stories, viewing stories, tracking views, and reactions. Key challenges include ensuring accurate expiration timing, automatic cleanup of expired content, and handling millions of concurrent viewers during popular stories."

---

---

## 📍 Navigation

<div align="center">

[Home: README](README.md) • [← Previous: Real-Time Collaboration System](10%29%20Real-Time%20Collaboration%20System.md) • [Next: Ticket Booking System →](12%29%20Ticket%20Booking%20System.md)

[📋 Cheatsheet](Projects%20Interview%20Cheatsheet.md)

</div>

---
