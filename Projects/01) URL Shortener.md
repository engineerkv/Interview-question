# URL Shortener System

---

## 📍 Navigation

<div align="center">

[Home: README](README.md) • [Next: Search System →](02%29%20Search%20System.md)

[📋 Cheatsheet](Projects%20Interview%20Cheatsheet.md)

</div>

---

## Overview

Design a URL shortening service like bit.ly or TinyURL that converts long URLs into short, shareable links. Users can shorten URLs, customize aliases, and track analytics.

---

## 1) Requirements

### Functional Requirements

**Core Features:**
- Generate unique short URLs for long URLs (e.g., `https://example.com/very/long/path` → `https://short.ly/abc123`)
- Redirect users to original URL when short URL is accessed
- Custom alias support (users can create memorable links like `short.ly/my-brand`)
- URL expiration (URLs can expire after a set time)
- Analytics tracking (click counts, geographic data, referrer, device types)
- User accounts with URL management dashboard
- QR code generation for short URLs

**User Features:**
- Responsive web interface
- Copy to clipboard functionality
- Real-time analytics updates
- URL list with search and filtering
- Bulk URL management

### Non-Functional Requirements

**Performance:**
- URL shortening: < 100ms
- URL redirection: < 100ms
- Handle 100M+ requests per day
- 10:1 read/write ratio (10,000 reads/sec, 1,000 writes/sec)

**Scalability:**
- Support billions of URLs
- Horizontal scaling capability
- High availability (99.9% uptime)

**Security:**
- Rate limiting to prevent abuse
- URL validation and sanitization
- Phishing detection
- HTTPS enforcement

---

## 2) Component Hierarchy

The frontend is a React application with a clean component structure. Here's how I'd organize it:

```
App
├── Layout
│   ├── Header
│   │   ├── Logo
│   │   ├── Navigation (Home, Dashboard, Analytics)
│   │   └── UserMenu (Login/Logout, Profile)
│   └── MainContent
├── Pages
│   ├── HomePage
│   │   ├── URLShortenerForm
│   │   │   ├── URLInput (validates URL in real-time)
│   │   │   ├── AliasInput (optional custom alias)
│   │   │   ├── ExpirationDatePicker (optional)
│   │   │   └── SubmitButton
│   │   └── ShortUrlDisplay
│   │       ├── ShortUrlCard (displays generated short URL)
│   │       ├── CopyButton (copies to clipboard)
│   │       ├── QRCodeButton (generates QR code)
│   │       └── ShareButtons (social media sharing)
│   ├── DashboardPage
│   │   ├── URLList
│   │   │   ├── URLItem (individual shortened URL)
│   │   │   │   ├── OriginalUrl
│   │   │   │   ├── ShortUrl
│   │   │   │   ├── ClickCount
│   │   │   │   ├── ExpirationBadge
│   │   │   │   └── ActionButtons (Edit, Delete, View Analytics)
│   │   │   └── SearchBar (filter URLs)
│   │   └── Pagination
│   └── AnalyticsPage
│       ├── AnalyticsDashboard
│       │   ├── SummaryCards (Total Clicks, Unique Clicks, Top Countries)
│       │   ├── ClickCountChart (line chart over time)
│       │   ├── CountryChart (bar chart by country)
│       │   ├── ReferrerChart (pie chart of referrers)
│       │   ├── DeviceChart (mobile vs desktop)
│       │   └── DateRangeFilter
│       └── URLSelector (select which URL to analyze)
└── SharedComponents
    ├── Button
    ├── Input
    ├── Card
    ├── Toast (notifications)
    ├── LoadingSpinner
    └── Modal (for QR code, delete confirmation)
```

### Key Components Explained

**1. URLShortenerForm Component**
- Main form for shortening URLs
- Real-time URL validation (checks if URL is valid format)
- Custom alias availability check (debounced API call)
- Handles form submission with React Query mutation
- Shows loading state during API call

**2. ShortUrlDisplay Component**
- Displays generated short URL
- Copy to clipboard functionality using Clipboard API
- QR code generation and display in modal
- Share buttons for social media

**3. URLList Component**
- Displays user's shortened URLs
- Virtual scrolling for performance with many URLs
- Search and filter functionality
- Pagination for large lists

**4. AnalyticsDashboard Component**
- Fetches analytics data with React Query
- Renders various charts (line, bar, pie)
- Date range filtering
- Real-time updates via polling

**5. URLItem Component**
- Individual URL card in the list
- Shows original URL, short URL, click count
- Expiration status badge
- Actions: edit, delete, view analytics

---

## 3) Data Models

Here are the key data structures:

```typescript
// Shortened URL
interface ShortUrl {
  id: string;
  shortCode: string;  // "abc123" part of short.ly/abc123
  originalUrl: string;
  shortUrl: string;  // Full short URL: "https://short.ly/abc123"
  userId?: string;  // Optional, for authenticated users
  createdAt: string;
  expiresAt?: string;  // Optional expiration date
  clickCount: number;
  isActive: boolean;
}

// Analytics data
interface Analytics {
  shortCode: string;
  clickCount: number;
  uniqueClicks: number;
  topCountries: Array<{
    country: string;
    clicks: number;
  }>;
  clicksByDate: Array<{
    date: string;  // "2024-01-15"
    clicks: number;
  }>;
  referrers: Array<{
    referrer: string;  // "google.com", "direct", etc.
    clicks: number;
  }>;
  devices: Array<{
    device: string;  // "mobile", "desktop", "tablet"
    clicks: number;
  }>;
}

// User (for authenticated users)
interface User {
  id: string;
  email: string;
  name: string;
  createdAt: string;
}

// Request/Response types
interface CreateShortUrlRequest {
  url: string;
  customAlias?: string;  // Optional custom short code
  expiresAt?: string;  // Optional expiration date
}

interface CreateShortUrlResponse {
  success: boolean;
  data: ShortUrl;
  error?: {
    code: string;  // "ALIAS_EXISTS", "INVALID_URL", etc.
    message: string;
  };
}

// Click tracking (for analytics)
interface ClickEvent {
  id: string;
  shortCode: string;
  timestamp: string;
  ipAddress: string;
  userAgent: string;
  referrer?: string;
  country?: string;
  device?: string;
}
```

### Data Flow Explanation

**When a user shortens a URL:**
1. User enters long URL in form
2. Optional: User enters custom alias
3. Frontend validates URL format
4. If custom alias, check availability via API
5. Submit to API: `POST /api/v1/shorten`
6. Server generates short code (or uses custom alias)
7. Response includes full short URL
8. Display short URL to user

**When a user clicks a short URL:**
1. User visits `short.ly/abc123`
2. Frontend makes request to redirect endpoint
3. Server looks up original URL by short code
4. Server records click event (for analytics)
5. Server returns 301 redirect to original URL
6. Browser follows redirect

**Analytics tracking:**
- Each click is recorded with metadata (IP, user agent, referrer)
- Analytics are aggregated and stored
- Frontend fetches analytics when viewing dashboard
- Real-time updates via polling or WebSocket

---

## 4) API Design

### REST Endpoints

**POST /api/v1/shorten**
- Create a new short URL
- Request body: `{ url: string, customAlias?: string, expiresAt?: string }`
- Returns: ShortUrl object with generated short code
- Status codes: 201 (Created), 400 (Invalid URL), 409 (Alias Exists)

**GET /api/v1/:shortCode**
- Redirect to original URL
- Returns: 301 redirect to original URL
- Status codes: 301 (Redirect), 404 (Not Found), 410 (Gone - Expired)

**GET /api/v1/urls**
- Get user's shortened URLs (requires authentication)
- Query params: `page`, `limit`, `search`
- Returns: Paginated list of ShortUrl objects

**GET /api/v1/urls/:shortCode/analytics**
- Get analytics for a specific short URL
- Query params: `startDate`, `endDate`
- Returns: Analytics object with charts data

**DELETE /api/v1/urls/:shortCode**
- Delete a short URL (requires authentication)
- Returns: Success confirmation

**GET /api/v1/alias/check**
- Check if custom alias is available
- Query params: `alias`
- Returns: `{ available: boolean }`

### API Request/Response Examples

**Shorten URL:**
  ```json
// POST /api/v1/shorten
  {
    "url": "https://www.example.com/very/long/url/path",
    "customAlias": "my-link",
    "expiresAt": "2024-12-31T23:59:59Z"
  }

// Response
  {
    "success": true,
    "data": {
      "shortCode": "my-link",
      "originalUrl": "https://www.example.com/very/long/url/path",
      "shortUrl": "https://short.ly/my-link",
      "createdAt": "2024-01-15T10:00:00Z",
      "expiresAt": "2024-12-31T23:59:59Z",
      "clickCount": 0
    }
  }
  ```

**Get Analytics:**
  ```json
// GET /api/v1/urls/abc123/analytics?startDate=2024-01-01&endDate=2024-01-31
// Response
  {
    "success": true,
    "data": {
      "shortCode": "abc123",
      "clickCount": 1250,
      "uniqueClicks": 980,
      "topCountries": [
        { "country": "US", "clicks": 450 },
        { "country": "IN", "clicks": 320 }
      ],
      "clicksByDate": [
        { "date": "2024-01-15", "clicks": 45 },
        { "date": "2024-01-16", "clicks": 52 }
      ],
      "referrers": [
        { "referrer": "google.com", "clicks": 320 },
        { "referrer": "direct", "clicks": 280 }
      ],
      "devices": [
        { "device": "mobile", "clicks": 650 },
        { "device": "desktop", "clicks": 600 }
      ]
    }
  }
  ```

**Check Alias Availability:**
```json
// GET /api/v1/alias/check?alias=my-link
// Response
{
  "available": false,
  "message": "Alias already exists"
}
```

### Error Handling

**Error Response Format:**
```json
{
  "success": false,
  "error": {
    "code": "ALIAS_EXISTS",
    "message": "Custom alias already exists",
    "details": "The alias 'my-link' is already taken"
  }
}
```

**Common Error Codes:**
- `INVALID_URL` - URL format is invalid
- `ALIAS_EXISTS` - Custom alias is already taken
- `ALIAS_INVALID` - Alias format is invalid (must be alphanumeric, hyphens, underscores)
- `URL_EXPIRED` - Short URL has expired
- `NOT_FOUND` - Short code doesn't exist

---

## Key Design Decisions

**1. Short Code Generation**
- Base62 encoding (a-z, A-Z, 0-9) for 6-8 character codes
- Can generate billions of unique codes
- Custom aliases allow user-friendly URLs

**2. Caching Strategy**
- Cache short code → original URL mapping in Redis
- Most reads are redirects, so caching is critical
- Cache expiration matches URL expiration

**3. Analytics Storage**
- Store click events in time-series database
- Aggregate data for dashboard display
- Real-time analytics via streaming

**4. URL Validation**
- Client-side validation for immediate feedback
- Server-side validation for security
- Check for malicious URLs (phishing detection)

**5. Rate Limiting**
- Limit URL creation per user/IP
- Prevent abuse and spam
- Different limits for authenticated vs anonymous users

---

## Interview Talking Points

**When explaining this system, I'd focus on:**

1. **Requirements First**: Start with core functionality - shorten URLs, redirect, analytics, custom aliases

2. **Component Structure**: Explain the React component hierarchy - form, display, dashboard, analytics

3. **Data Models**: Walk through ShortUrl, Analytics, and how click tracking works

4. **API Design**: Show the REST endpoints - shorten, redirect, analytics, alias check

5. **Key Challenges**: 
   - Generating unique short codes at scale
   - Fast redirects (caching strategy)
   - Analytics aggregation and real-time updates
   - Handling high read/write ratio

**Example explanation flow:**
> "So for a URL shortener, the core requirement is converting long URLs to short ones. The frontend is a React app with a form component where users enter URLs, optionally with custom aliases. When submitted, it calls the shorten API which generates a unique short code. The data model is simple - a ShortUrl object with the original URL, short code, and metadata. For redirects, when someone visits the short URL, we look up the original URL and return a 301 redirect. Analytics are tracked on each click and aggregated for the dashboard. The main challenge is handling the high read/write ratio - most traffic is redirects, so we heavily cache the short code mappings."

---

## 📍 Navigation

<div align="center">

[Home: README](README.md) • [Next: Search System →](02%29%20Search%20System.md)

[📋 Cheatsheet](Projects%20Interview%20Cheatsheet.md)

</div>

---
