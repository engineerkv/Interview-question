# URL Shortener

> **Project Type:** Full-Stack Web Application (MERN Stack)
> **Scale:** Handle 100M+ URLs per day, 10:1 read/write ratio
> **Tech Stack:** React.js, Node.js, Express.js, MongoDB, Redis, CDN

# 1) Problem Statement

Design and implement a scalable URL shortening service that addresses the following challenges:

- **Core Functionality**: Convert long URLs into short, shareable links (e.g., `https://example.com/very/long/path` → `https://short.ly/abc123`)
- **Scale Requirements**: Handle 100M+ URL shortening requests per day with a 10:1 read/write ratio (10,000 reads/sec, 1,000 writes/sec)
- **Performance**: Provide fast redirection with minimal latency (< 100ms) for billions of stored URLs
- **Customization**: Support custom aliases allowing users to create memorable short links (e.g., `short.ly/my-brand`)
- **Analytics**: Track and provide analytics data including click counts, geographic distribution, referrer information, and device types
- **High Availability**: Maintain 99.9% uptime with fault tolerance and redundancy across all system components
- **Scalability**: Design for horizontal scaling to handle billions of URLs while maintaining consistent performance
- **Data Persistence**: Store URL mappings reliably with support for URL expiration and cleanup of expired links

---

# 2) High Level Design (HLD)

## a) Requirements

### i) Functional Requirements

- **Generate unique short URL** for a given long URL
- **Redirect users** to the original URL when short URL is accessed
- **Custom alias support** - Allow users to customize their short URLs (optional)
- **Link expiration** - URLs become inactive after a specified period (optional)
- **Analytics tracking** - Track click counts, referrer information, geographic location, and device types (optional)

### ii) Non-Functional Requirements

- **High availability** - Service should be up 99.9% of the time with fault tolerance and redundancy
- **Low latency** - URL shortening and redirects should happen in milliseconds (< 100ms for redirect)
- **Scalability** - System should handle millions of requests per day and scale to billions of URLs
- **Durability** - Shortened URLs should work for years with reliable data persistence
- **Security** - Prevent malicious use such as phishing, implement rate limiting, input validation, and HTTPS
- **URL length** - Short URLs should be as short as possible (typically 6-8 characters)

---

## b) Scope and Priority

### Phase 1: MVP (Must Have) - Priority 1

- URL shortening and redirection
- Basic analytics (click count)
- Custom alias support

### Phase 2: Enhanced Features - Priority 2

- URL expiration
- Advanced analytics (referrer, location, device)
- User accounts and URL management
- API for developers
- Bulk URL shortening
- White-label solution

---

## c) Technology Choices

### Database

- **MongoDB (NoSQL)** - Better choice for this use case due to:
  - Efficient handling of billions of simple key-value lookups
  - High scalability and availability with horizontal sharding
  - Flexible schema for URL metadata and analytics
  - Better performance for read-heavy workloads

### Caching

- **Redis** - Fast in-memory cache for hot URLs (20% of traffic), session data, and rate limiting

### CDN

- **CloudFront/Cloudflare** - Global CDN for redirects to reduce latency and distribute load geographically

### Message Queue

- **RabbitMQ/Kafka** - For async analytics processing to decouple analytics from core redirection service

---

## e) Architecture Overview

The system follows a layered architecture with clear separation of concerns across frontend and backend. Here's how the complete system works:

### Frontend Architecture

**Frontend Layers:**

1. **Presentation Layer (React Components)**
   - **UI Components**: Reusable components (buttons, inputs, cards)
   - **Feature Components**: URLShortenerForm, AnalyticsDashboard, URLList
   - **Layout Components**: Header, Footer, Navigation, MainLayout
   - **Page Components**: HomePage, DashboardPage, AnalyticsPage

2. **State Management Layer**
   - **Local State (useState)**: Component-specific UI state (form inputs, loading, errors)
   - **Server State (React Query)**: API data caching, refetching, optimistic updates
   - **Global State (Context)**: User authentication, theme preferences, app-wide settings

3. **API Integration Layer**
   - **API Client**: Axios instance with interceptors for auth, error handling
   - **React Query Hooks**: Custom hooks for API operations (useShortenURL, useAnalytics)
   - **Request/Response Transformation**: Data normalization and error handling

4. **Routing Layer (React Router)**
   - **Route Configuration**: Define routes and protected routes
   - **Navigation**: Programmatic and declarative navigation
   - **Route Guards**: Authentication and authorization checks

5. **Build & Deployment Layer**
   - **Build Process**: Webpack/Vite bundling with code splitting
   - **Static Assets**: Served from CDN (CloudFront/Cloudflare)
   - **Environment Configuration**: Environment-specific API endpoints and configs

**Frontend Request Flow:**

1. **User Interaction** → User enters URL in form component
2. **Form Validation** → Client-side validation before submission
3. **API Call** → React Query mutation triggers API request
4. **Loading State** → UI shows loading indicator
5. **Response Handling** → Success/error state updates UI
6. **State Update** → React Query caches response, components re-render
7. **User Feedback** → Display short URL or error message

### Complete Request Flow

**URL Shortening Flow:**

1. **Frontend**: User submits URL through React form
2. **Load Balancer**: Routes request to available API server
3. **API Server**: Validates request, extracts URL and optional custom alias
4. **URL Service**: Generates short code (Base62 or custom alias)
5. **Database**: Stores URL mapping in MongoDB (with transaction)
6. **Cache**: Optionally caches new URL if it's expected to be popular
7. **Response**: Returns short URL to frontend
8. **Frontend**: Displays short URL with copy functionality

**URL Redirection Flow:**

1. **User**: Clicks short URL (e.g., short.ly/abc123)
2. **CDN/Edge**: Checks if redirect can be served from edge location
3. **Load Balancer**: Routes to API server if not cached at edge
4. **Cache Check**: Redis checked first for hot URLs
5. **Database Lookup**: If cache miss, query MongoDB shard
6. **Expiration Check**: Verify URL hasn't expired
7. **Analytics**: Async tracking via message queue (non-blocking)
8. **Redirect**: Return 301/302 redirect to original URL
9. **Cache Update**: Update Redis cache for future requests

**Analytics Flow:**

1. **Frontend**: User views analytics dashboard
2. **API Request**: React Query fetches analytics data
3. **Cache Check**: Check Redis for cached analytics
4. **Database Query**: If cache miss, query aggregated analytics from MongoDB
5. **Response**: Return pre-aggregated data (fast queries)
6. **Frontend**: Display charts and statistics
7. **Real-Time Updates**: Polling every 30 seconds for active URLs

**Complete Architecture Diagram:**

```
┌─────────────────────────────────────────────────────────────────────┐
│                        FRONTEND LAYER                                │
│  ┌──────────────────────────────────────────────────────────────┐  │
│  │              Client Browser (User Interface)                  │  │
│  │  ┌──────────────┐  ┌──────────────┐  ┌──────────────┐      │  │
│  │  │   React App  │  │  React Query │  │  React Router│      │  │
│  │  │  Components  │  │  (API State) │  │  (Routing)   │      │  │
│  │  └──────────────┘  └──────────────┘  └──────────────┘      │  │
│  │                                                               │  │
│  │  ┌──────────────────────────────────────────────────────┐   │  │
│  │  │  Components: URLShortenerForm, AnalyticsDashboard    │   │  │
│  │  │  State: Local (useState) + Server (React Query)      │   │  │
│  │  └──────────────────────────────────────────────────────┘   │  │
│  └───────────────────────┬──────────────────────────────────────┘  │
└──────────────────────────┼──────────────────────────────────────────┘
                           │ HTTPS
                           ▼
┌─────────────────────────────────────────────────────────────────────┐
│                    CDN / EDGE LAYER                                  │
│  ┌──────────────────────────────────────────────────────────────┐  │
│  │         CloudFront / Cloudflare (Global CDN)                 │  │
│  │  - Static assets (JS, CSS, images)                           │  │
│  │  - Edge caching for redirects                                │  │
│  │  - DDoS protection                                           │  │
│  └───────────────────────┬──────────────────────────────────────┘  │
└──────────────────────────┼──────────────────────────────────────────┘
                           │
                           ▼
┌─────────────────────────────────────────────────────────────────────┐
│                  LOAD BALANCER LAYER                                 │
│  ┌──────────────────────────────────────────────────────────────┐  │
│  │              Nginx / AWS ALB                                  │  │
│  │  - SSL/TLS termination                                        │  │
│  │  - Request routing to API servers                             │  │
│  │  - Health checks and failover                                 │  │
│  └───────────────────────┬──────────────────────────────────────┘  │
└──────────────────────────┼──────────────────────────────────────────┘
                           │
              ┌────────────┴────────────┐
              │                         │
              ▼                         ▼
┌─────────────────────┐    ┌─────────────────────┐
│    API Server 1     │    │    API Server 2     │
│  Node.js/Express.js │    │  Node.js/Express.js │
│                     │    │                     │
│  - URL Shortening   │    │  - URL Shortening   │
│  - Redirect         │    │  - Redirect         │
│  - Analytics API    │    │  - Analytics API    │
│  (Stateless)        │    │  (Stateless)        │
└──────────┬──────────┘    └──────────┬──────────┘
           │                          │
           └────────────┬─────────────┘
                        │
                        ▼
┌─────────────────────────────────────────────────────────────────────┐
│              APPLICATION SERVICE LAYER                               │
│  ┌──────────────┐  ┌──────────────┐  ┌──────────────┐             │
│  │URL Generation│  │  Validation  │  │  Analytics   │             │
│  │   Service    │  │   Service    │  │   Service    │             │
│  │              │  │              │  │              │             │
│  │- Base62      │  │- URL Format  │  │- Event Track │             │
│  │- Custom Alias│  │- Expiration  │  │- Aggregation │             │
│  └──────────────┘  └──────────────┘  └──────┬───────┘             │
└──────────────────────────────────────────────┼──────────────────────┘
                                               │
                        ┌──────────────────────┴──────────────────────┐
                        │                                             │
                        ▼                                             ▼
        ┌───────────────────────────┐    ┌───────────────────────────┐
        │      CACHE LAYER          │    │    MESSAGE QUEUE          │
        │   Redis Cluster           │    │   RabbitMQ / Kafka        │
        │                           │    │                           │
        │  - Hot URLs (20%)         │    │  - Analytics Events       │
        │  - Session Data           │    │  - Async Processing       │
        │  - Rate Limiting          │    │  - Worker Queue           │
        └───────────┬───────────────┘    └───────────┬───────────────┘
                    │                                 │
                    │                                 │
                    ▼                                 ▼
┌─────────────────────────────────────────────────────────────────────┐
│                    DATABASE LAYER                                    │
│  ┌──────────────┐  ┌──────────────┐  ┌──────────────┐             │
│  │   Shard 1    │  │   Shard 2    │  │   Shard 3    │             │
│  │  (MongoDB)   │  │  (MongoDB)   │  │  (MongoDB)   │             │
│  │              │  │              │  │              │             │
│  │ - URLs       │  │ - URLs       │  │ - URLs       │             │
│  │ - Analytics  │  │ - Analytics  │  │ - Analytics  │             │
│  └──────┬───────┘  └──────┬───────┘  └──────┬───────┘             │
│         │                 │                  │                     │
│         └─────────────────┴──────────────────┘                     │
│                            │                                       │
│                            ▼                                       │
│         ┌──────────────────────────────┐                          │
│         │    Read Replicas             │                          │
│         │  (Analytics Queries)         │                          │
│         └──────────────────────────────┘                          │
└─────────────────────────────────────────────────────────────────────┘

```

### Frontend Architecture Details

**Component Structure:**

```
Frontend Application
├── Presentation Layer
│   ├── UI Components (Buttons, Inputs, Cards)
│   ├── Feature Components (URLShortenerForm, AnalyticsDashboard)
│   └── Layout Components (Header, Footer, Navigation)
├── State Management
│   ├── Local State (Component-level with useState)
│   ├── Server State (React Query for API data)
│   └── Global State (Context for auth, theme)
├── API Integration
│   ├── API Client (Axios with interceptors)
│   ├── Custom Hooks (useShortenURL, useAnalytics)
│   └── Error Handling & Retry Logic
└── Routing
    ├── Public Routes (Home, About)
    ├── Protected Routes (Dashboard, Analytics)
    └── Route Guards (Authentication checks)

```

**Frontend Deployment:**

- **Build**: Production bundle with code splitting and tree shaking
- **CDN**: Static assets served from CloudFront/Cloudflare edge locations
- **Caching**: Aggressive caching for static assets, cache-busting for updates
- **Environment**: Environment variables for API endpoints and feature flags

**Key Components:**

- **Frontend (React.js)**:
  - Single-page application with client-side routing
  - Component-based architecture for reusability
  - React Query for efficient API state management
  - Responsive design for mobile and desktop

- **CDN/Edge**:
  - Global distribution of static assets
  - Edge caching for redirects to reduce latency
  - DDoS protection and rate limiting at edge

- **Load Balancer**:
  - Distributes traffic across API servers
  - SSL/TLS termination
  - Health checks and automatic failover

- **API Servers**:
  - Stateless design for horizontal scaling
  - Handle URL shortening, redirection, and analytics APIs
  - Can add/remove instances based on load

- **Application Services**:
  - URL Generation Service (Base62 encoding, custom aliases)
  - Validation Service (URL format, expiration checks)
  - Analytics Service (event tracking, aggregation)

- **Cache Layer (Redis)**:
  - In-memory cache for 20% hot URLs (80-20 rule)
  - Session data and rate limiting counters
  - 90% cache hit rate target

- **Database (MongoDB)**:
  - Sharded across multiple nodes for horizontal scaling
  - Consistent hashing for even distribution
  - Read replicas for analytics queries

- **Message Queue**:
  - RabbitMQ/Kafka for async analytics processing
  - Decouples analytics from core redirect functionality
  - Enables independent scaling of workers

---

# 3) Low Level Design (LLD)

## a) Frontend

### i) Component Architecture

Think of the frontend as a tree of React components - each component handles a specific part of the UI, and they work together to create the complete user experience.

**Component Hierarchy:**

```
App
├── Header
│   ├── Logo
│   └── Navigation
├── MainContent
│   ├── URLShortenerForm
│   │   ├── URLInput
│   │   ├── CustomAliasInput (optional)
│   │   └── SubmitButton
│   ├── ShortURLDisplay
│   │   ├── ShortURL
│   │   └── CopyButton
│   └── AnalyticsDashboard
│       ├── ClickCount
│       ├── ReferrerChart
│       └── TimeSeriesChart
└── Footer

```

**Key React Components:**

```typescript
// Main URL Shortener Component
const URLShortenerForm: React.FC = () => {
  const [originalUrl, setOriginalUrl] = useState('');
  const [customAlias, setCustomAlias] = useState('');
  const [shortUrl, setShortUrl] = useState('');
  const [loading, setLoading] = useState(false);
  const [error, setError] = useState('');

  const handleSubmit = async (e: React.FormEvent) => {
    e.preventDefault();
    setLoading(true);
    setError('');

    try {
      const response = await axios.post('/api/v1/shorten', {
        url: originalUrl,
        customAlias: customAlias || undefined
      });

      setShortUrl(response.data.shortUrl);
    } catch (err) {
      setError(err.response?.data?.error || 'Failed to shorten URL');
    } finally {
      setLoading(false);
    }
  };

  return (
    <form onSubmit={handleSubmit}>
      <URLInput
        value={originalUrl}
        onChange={setOriginalUrl}
        placeholder="Enter long URL"
      />
      <CustomAliasInput
        value={customAlias}
        onChange={setCustomAlias}
        placeholder="Custom alias (optional)"
      />
      <SubmitButton loading={loading}>
        Shorten URL
      </SubmitButton>
      {error && <ErrorMessage message={error} />}
    </form>
  );
};

// Short URL Display Component
const ShortURLDisplay: React.FC<{ shortUrl: string }> = ({ shortUrl }) => {
  const [copied, setCopied] = useState(false);

  const handleCopy = async () => {
    await navigator.clipboard.writeText(shortUrl);
    setCopied(true);
    setTimeout(() => setCopied(false), 2000);
  };

  return (
    <div className="short-url-display">
      <input type="text" value={shortUrl} readOnly />
      <button onClick={handleCopy}>
        {copied ? 'Copied!' : 'Copy'}
      </button>
    </div>
  );
};

// Analytics Dashboard Component
const AnalyticsDashboard: React.FC<{ shortCode: string }> = ({ shortCode }) => {
  const [analytics, setAnalytics] = useState(null);
  const [loading, setLoading] = useState(true);

  useEffect(() => {
    const fetchAnalytics = async () => {
      try {
        const response = await axios.get(`/api/v1/urls/${shortCode}/analytics`);
        setAnalytics(response.data);
      } catch (err) {
        console.error('Failed to fetch analytics:', err);
      } finally {
        setLoading(false);
      }
    };

    fetchAnalytics();
  }, [shortCode]);

  if (loading) return <LoadingSpinner />;
  if (!analytics) return null;

  return (
    <div className="analytics-dashboard">
      <ClickCount count={analytics.clickCount} />
      <ReferrerChart data={analytics.topReferrers} />
      <TimeSeriesChart data={analytics.clicksByDate} />
    </div>
  );
};

```

### ii) State Management

**State Management Strategy (React 19):**

- **Local State (useState)**: Form inputs, UI state (loading, errors, copied status)
- **Optimistic Updates (useOptimistic)**: React 19 hook for optimistic UI updates
- **Form Actions (useActionState)**: React 19 hook for form state management with server actions
- **Deferred Values (useDeferredValue)**: React 19 hook for debouncing and deferred updates
- **Transitions (useTransition)**: React 19 hook for non-urgent updates
- **API State**: React Query for server state (caching, refetching) - works with React 19
- **Global State (Context/Redux)**: User authentication, theme preferences (if needed)

**Frontend Implementation:**

```typescript
// Using React Query for API state management
import { useQuery, useMutation, useQueryClient } from '@tanstack/react-query';

const useShortenURL = () => {
  const queryClient = useQueryClient();

  return useMutation({
    mutationFn: async ({ url, customAlias }: { url: string; customAlias?: string }) => {
      const response = await axios.post('/api/v1/shorten', { url, customAlias });
      return response.data;
    },
    onSuccess: () => {
      // Invalidate and refetch URLs list
      queryClient.invalidateQueries({ queryKey: ['urls'] });
    }
  });
};

const useAnalytics = (shortCode: string) => {
  return useQuery({
    queryKey: ['analytics', shortCode],
    queryFn: async () => {
      const response = await axios.get(`/api/v1/urls/${shortCode}/analytics`);
      return response.data;
    },
    refetchInterval: 30000 // Refetch every 30 seconds
  });
};

```

### iii) Advanced Component Patterns

**Form Handling with React 19 Actions:**

```typescript
import { useActionState, useFormStatus } from 'react';

// Simple validation function
function validateUrl(url: string): string | null {
  try {
    new URL(url);
    return null; // Valid
  } catch {
    return 'Please enter a valid URL';
  }
}

function validateAlias(alias: string | null): string | null {
  if (!alias) return null; // Optional
  if (alias.length < 3) return 'Alias must be at least 3 characters';
  if (alias.length > 20) return 'Alias must be less than 20 characters';
  if (!/^[a-zA-Z0-9-_]+$/.test(alias)) {
    return 'Alias can only contain letters, numbers, hyphens, and underscores';
  }
  return null; // Valid
}

// React 19: Server Action
async function shortenUrlAction(
  prevState: { error?: string; success?: boolean },
  formData: FormData
) {
  const url = formData.get('url') as string;
  const customAlias = formData.get('customAlias') as string | null;

  // Validate
  const urlError = validateUrl(url);
  if (urlError) return { error: urlError };

  const aliasError = validateAlias(customAlias);
  if (aliasError) return { error: aliasError };

  try {
    const response = await shortenUrlAPI({ url, customAlias });
    return { success: true, shortUrl: response.shortUrl };
  } catch (error) {
    return { error: 'Failed to shorten URL' };
  }
}

// React 19: Submit Button Component with useFormStatus
const SubmitButton: React.FC<{ children: React.ReactNode }> = ({ children }) => {
  const { pending } = useFormStatus(); // React 19 hook

  return (
    <button type="submit" disabled={pending}>
      {pending ? 'Shortening...' : children}
    </button>
  );
};

const URLShortenerForm: React.FC = () => {
  // React 19: useActionState for form actions
  const [state, formAction, isPending] = useActionState(shortenUrlAction, {});

  const [customAlias, setCustomAlias] = useState('');

  // Debounced alias availability check
  const { data: aliasAvailable } = useQuery({
    queryKey: ['alias-check', customAlias],
    queryFn: () => checkAliasAvailability(customAlias),
    enabled: !!customAlias && customAlias.length >= 3,
    staleTime: 5000
  });

  return (
    <form action={formAction}>
      <div className="form-group">
        <input
          name="url"
          type="url"
          placeholder="Enter long URL"
          required
          className={state.error ? 'error' : ''}
        />
        {state.error && <span className="error-message">{state.error}</span>}
      </div>

      <div className="form-group">
        <input
          name="customAlias"
          value={customAlias}
          onChange={(e) => setCustomAlias(e.target.value)}
          placeholder="Custom alias (optional)"
        />
        {aliasAvailable !== undefined && (
          <span className={aliasAvailable ? 'success' : 'error'}>
            {aliasAvailable ? '✓ Available' : '✗ Taken'}
          </span>
        )}
      </div>

      <SubmitButton>Shorten URL</SubmitButton>

      {state.success && (
        <div className="success-message">
          Short URL: {state.shortUrl}
        </div>
      )}
    </form>
  );
};
```

**Optimistic Updates with React 19:**

```typescript
import { useOptimistic, useTransition } from 'react';

const URLShortenerForm: React.FC = () => {
  const [isPending, startTransition] = useTransition();
  const [urls, setUrls] = useState<URL[]>([]);

  // React 19: useOptimistic for optimistic updates
  const [optimisticUrls, addOptimisticUrl] = useOptimistic(
    urls,
    (state, newUrl: URL) => [
      { ...newUrl, id: 'temp', syncing: true },
      ...state
    ]
  );

  const handleSubmit = async (data: FormData) => {
    const newUrl = {
      id: 'temp',
      url: data.get('url') as string,
      shortCode: 'generating...',
      syncing: true
    };

    // Optimistically add to UI
    startTransition(() => {
      addOptimisticUrl(newUrl);
    });

    try {
      const result = await shortenUrlAPI(data);
      setUrls(prev => [result, ...prev.filter(u => u.id !== 'temp')]);
    } catch (error) {
      // Rollback on error
      setUrls(prev => prev.filter(u => u.id !== 'temp'));
      toast.error('Failed to shorten URL');
    }
  };

  return (
    <form action={handleSubmit}>
      {/* Form fields */}
    </form>
  );
};
```

**Error Boundaries with React 19:**

```typescript
import { Component, ErrorInfo, ReactNode } from 'react';

// React 19: Improved error boundaries with better TypeScript support
class ErrorBoundary extends Component<
  { children: ReactNode; fallback?: (error: Error, reset: () => void) => ReactNode },
  { hasError: boolean; error: Error | null }
> {
  constructor(props: { children: ReactNode; fallback?: (error: Error, reset: () => void) => ReactNode }) {
    super(props);
    this.state = { hasError: false, error: null };
  }

  static getDerivedStateFromError(error: Error) {
    return { hasError: true, error };
  }

  componentDidCatch(error: Error, errorInfo: ErrorInfo) {
    console.error('Error caught:', error, errorInfo);
    // Log to error tracking service (Sentry, etc.)
  }

  reset = () => {
    this.setState({ hasError: false, error: null });
  };

  render() {
    if (this.state.hasError && this.state.error) {
      if (this.props.fallback) {
        return this.props.fallback(this.state.error, this.reset);
      }

      return (
        <div className="error-boundary">
          <h2>Something went wrong</h2>
          <p>{this.state.error.message}</p>
          <button onClick={this.reset}>Try again</button>
        </div>
      );
    }

    return this.props.children;
  }
}

// React 19: Using error boundaries with fallback prop
<ErrorBoundary
  fallback={(error, reset) => (
    <div>
      <h2>Error: {error.message}</h2>
      <button onClick={reset}>Retry</button>
    </div>
  )}
>
  <App />
</ErrorBoundary>
```

**Loading States & Skeletons:**

```typescript
const AnalyticsSkeleton: React.FC = () => (
  <div className="analytics-skeleton">
    <div className="skeleton-header" />
    <div className="skeleton-chart" />
    <div className="skeleton-stats">
      {[1, 2, 3].map(i => <div key={i} className="skeleton-stat" />)}
    </div>
  </div>
);

const AnalyticsDashboard: React.FC<{ shortCode: string }> = ({ shortCode }) => {
  const { data, isLoading, error } = useAnalytics(shortCode);

  if (isLoading) return <AnalyticsSkeleton />;
  if (error) return <ErrorMessage error={error} />;

  return (
    <div className="analytics-dashboard">
      {/* Analytics content */}
    </div>
  );
};
```

### iv) Performance Optimizations

**Code Splitting & Lazy Loading:**

```typescript
import { lazy, Suspense } from 'react';

const AnalyticsDashboard = lazy(() => import('./AnalyticsDashboard'));
const URLHistory = lazy(() => import('./URLHistory'));

const App: React.FC = () => {
  return (
    <Router>
      <Suspense fallback={<LoadingSpinner />}>
        <Routes>
          <Route path="/analytics/:code" element={<AnalyticsDashboard />} />
          <Route path="/history" element={<URLHistory />} />
        </Routes>
      </Suspense>
    </Router>
  );
};
```

**Memoization for Expensive Components:**

```typescript
const ReferrerChart = React.memo<{ data: ReferrerData[] }>(({ data }) => {
  const chartData = useMemo(() => {
    return data.map(item => ({
      name: item.referrer || 'Direct',
      value: item.clicks
    }));
  }, [data]);

  return <Chart data={chartData} />;
}, (prevProps, nextProps) => {
  return prevProps.data.length === nextProps.data.length;
});
```

**Virtual Scrolling for Long Lists:**

```typescript
import { useVirtualizer } from '@tanstack/react-virtual';

const URLList: React.FC<{ urls: URL[] }> = ({ urls }) => {
  const parentRef = useRef<HTMLDivElement>(null);

  const virtualizer = useVirtualizer({
    count: urls.length,
    getScrollElement: () => parentRef.current,
    estimateSize: () => 80,
    overscan: 5
  });

  return (
    <div ref={parentRef} style={{ height: '600px', overflow: 'auto' }}>
      <div style={{ height: `${virtualizer.getTotalSize()}px`, position: 'relative' }}>
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
            <URLItem url={urls[virtualItem.index]} />
          </div>
        ))}
      </div>
    </div>
  );
};
```

**Image Optimization:**

```typescript
const OptimizedImage: React.FC<{ src: string; alt: string }> = ({ src, alt }) => {
  return (
    <picture>
      <source srcSet={`${src}.webp`} type="image/webp" />
      <source srcSet={`${src}.avif`} type="image/avif" />
      <img
        src={src}
        alt={alt}
        loading="lazy"
        decoding="async"
        onError={(e) => {
          e.currentTarget.src = '/placeholder.png';
        }}
      />
    </picture>
  );
};
```

**Debouncing with React 19:**

```typescript
import { useDeferredValue, useTransition } from 'react';

const SearchInput: React.FC = () => {
  const [query, setQuery] = useState('');
  const [isPending, startTransition] = useTransition();

  // React 19: useDeferredValue for debouncing
  const deferredQuery = useDeferredValue(query);

  // React 19: use() hook for async search results
  const searchPromise = useMemo(() => {
    if (!deferredQuery) return Promise.resolve([]);
    return searchAPI(deferredQuery);
  }, [deferredQuery]);

  const searchResults = use(searchPromise);

  const handleChange = (e: React.ChangeEvent<HTMLInputElement>) => {
    const value = e.target.value;
    setQuery(value);
    startTransition(() => {
      // Transition updates are lower priority
    });
  };

  return (
    <div>
      <input
        value={query}
        onChange={handleChange}
        placeholder="Search..."
      />
      {isPending && <span>Searching...</span>}
      <SearchResults results={searchResults} />
    </div>
  );
};
```

### v) State Management Architecture

**Context API for Global State:**

```typescript
interface AppState {
  user: User | null;
  theme: 'light' | 'dark';
  notifications: Notification[];
}

const AppContext = createContext<{
  state: AppState;
  dispatch: React.Dispatch<AppAction>;
} | null>(null);

const appReducer = (state: AppState, action: AppAction): AppState => {
  switch (action.type) {
    case 'SET_USER':
      return { ...state, user: action.payload };
    case 'TOGGLE_THEME':
      return { ...state, theme: state.theme === 'light' ? 'dark' : 'light' };
    case 'ADD_NOTIFICATION':
      return { ...state, notifications: [...state.notifications, action.payload] };
    default:
      return state;
  }
};

export const AppProvider: React.FC<{ children: React.ReactNode }> = ({ children }) => {
  const [state, dispatch] = useReducer(appReducer, initialState);

  return (
    <AppContext.Provider value={{ state, dispatch }}>
      {children}
    </AppContext.Provider>
  );
};
```

**React Query Configuration:**

```typescript
const queryClient = new QueryClient({
  defaultOptions: {
    queries: {
      staleTime: 5 * 60 * 1000, // 5 minutes
      cacheTime: 10 * 60 * 1000, // 10 minutes
      retry: 3,
      retryDelay: (attemptIndex) => Math.min(1000 * 2 ** attemptIndex, 30000),
      refetchOnWindowFocus: false,
      refetchOnReconnect: true
    },
    mutations: {
      retry: 1,
      onError: (error) => {
        // Global error handling
        toast.error('An error occurred');
      }
    }
  }
});
```

### vi) UI/UX Enhancements

**Toast Notifications:**

```typescript
import { toast } from 'react-hot-toast';

const useShortenURL = () => {
  return useMutation({
    mutationFn: shortenUrlAPI,
    onSuccess: (data) => {
      toast.success('URL shortened successfully!');
      navigator.clipboard.writeText(data.shortUrl);
      toast.success('Copied to clipboard');
    },
    onError: (error) => {
      toast.error(error.message || 'Failed to shorten URL');
    }
  });
};
```

**Copy to Clipboard with React 19:**

```typescript
import { use, useTransition } from 'react';

const CopyButton: React.FC<{ text: string }> = ({ text }) => {
  const [copied, setCopied] = useState(false);
  const [isPending, startTransition] = useTransition();

  const handleCopy = async () => {
    startTransition(async () => {
      try {
        await navigator.clipboard.writeText(text);
        setCopied(true);
        setTimeout(() => setCopied(false), 2000);
      } catch (err) {
        // Fallback for older browsers
        const textArea = document.createElement('textarea');
        textArea.value = text;
        document.body.appendChild(textArea);
        textArea.select();
        document.execCommand('copy');
        document.body.removeChild(textArea);
        setCopied(true);
      }
    });
  };

  return (
    <button onClick={handleCopy} disabled={isPending} className={copied ? 'copied' : ''}>
      {copied ? '✓ Copied!' : 'Copy'}
    </button>
  );
};

// React 19: Using use() hook for promises
const AsyncCopyButton: React.FC<{ textPromise: Promise<string> }> = ({ textPromise }) => {
  const text = use(textPromise); // React 19: use() hook reads promises
  return <CopyButton text={text} />;
};
```

**QR Code Generation:**

```typescript
import QRCode from 'qrcode.react';

const QRCodeDisplay: React.FC<{ url: string }> = ({ url }) => {
  const [downloadUrl, setDownloadUrl] = useState('');

  const handleDownload = async () => {
    const canvas = document.getElementById('qrcode') as HTMLCanvasElement;
    const url = await canvas.toDataURL('image/png');
    setDownloadUrl(url);

    const link = document.createElement('a');
    link.download = 'qrcode.png';
    link.href = url;
    link.click();
  };

  return (
    <div className="qrcode-container">
      <QRCode id="qrcode" value={url} size={200} />
      <button onClick={handleDownload}>Download QR Code</button>
    </div>
  );
};
```

**Responsive Design Patterns:**

```typescript
// Custom hook for responsive breakpoints
const useBreakpoint = () => {
  const [breakpoint, setBreakpoint] = useState<'mobile' | 'tablet' | 'desktop'>('desktop');

  useEffect(() => {
    const checkBreakpoint = () => {
      const width = window.innerWidth;
      if (width < 768) setBreakpoint('mobile');
      else if (width < 1024) setBreakpoint('tablet');
      else setBreakpoint('desktop');
    };

    checkBreakpoint();
    window.addEventListener('resize', checkBreakpoint);
    return () => window.removeEventListener('resize', checkBreakpoint);
  }, []);

  return breakpoint;
};

// Usage
const Dashboard: React.FC = () => {
  const breakpoint = useBreakpoint();

  return (
    <div className={`dashboard ${breakpoint}`}>
      {breakpoint === 'mobile' ? <MobileLayout /> : <DesktopLayout />}
    </div>
  );
};
```

### vii) Accessibility Features

**ARIA Labels & Roles:**

```typescript
const URLInput: React.FC<Props> = ({ value, onChange }) => {
  return (
    <div className="input-group">
      <label htmlFor="url-input" className="sr-only">
        Enter URL to shorten
      </label>
      <input
        id="url-input"
        type="url"
        value={value}
        onChange={onChange}
        aria-label="URL input"
        aria-describedby="url-help"
        aria-invalid={errors.url ? 'true' : 'false'}
        aria-required="true"
      />
      <span id="url-help" className="help-text">
        Enter a valid URL starting with http:// or https://
      </span>
    </div>
  );
};
```

**Keyboard Navigation:**

```typescript
const ShortURLDisplay: React.FC<{ shortUrl: string }> = ({ shortUrl }) => {
  const inputRef = useRef<HTMLInputElement>(null);

  const handleKeyDown = (e: React.KeyboardEvent) => {
    if (e.key === 'Enter' || (e.key === 'c' && e.ctrlKey)) {
      handleCopy();
    }
  };

  return (
    <div className="short-url-display" role="region" aria-label="Short URL">
      <input
        ref={inputRef}
        type="text"
        value={shortUrl}
        readOnly
        aria-label="Shortened URL"
        onKeyDown={handleKeyDown}
      />
      <button
        onClick={handleCopy}
        aria-label="Copy short URL to clipboard"
      >
        Copy
      </button>
    </div>
  );
};
```

**Focus Management:**

```typescript
const Modal: React.FC<{ isOpen: boolean; onClose: () => void; children: React.ReactNode }> = ({
  isOpen,
  onClose,
  children
}) => {
  const modalRef = useRef<HTMLDivElement>(null);
  const previousFocusRef = useRef<HTMLElement | null>(null);

  useEffect(() => {
    if (isOpen) {
      previousFocusRef.current = document.activeElement as HTMLElement;
      modalRef.current?.focus();
    } else {
      previousFocusRef.current?.focus();
    }
  }, [isOpen]);

  const handleKeyDown = (e: React.KeyboardEvent) => {
    if (e.key === 'Escape') onClose();
  };

  if (!isOpen) return null;

  return (
    <div
      className="modal-overlay"
      onClick={onClose}
      role="dialog"
      aria-modal="true"
      aria-labelledby="modal-title"
    >
      <div
        ref={modalRef}
        className="modal-content"
        onClick={(e) => e.stopPropagation()}
        onKeyDown={handleKeyDown}
        tabIndex={-1}
      >
        {children}
      </div>
    </div>
  );
};
```

### viii) Frontend Testing

**Component Testing:**

```typescript
import { render, screen, fireEvent, waitFor } from '@testing-library/react';
import { QueryClient, QueryClientProvider } from '@tanstack/react-query';
import URLShortenerForm from './URLShortenerForm';

const createTestQueryClient = () => new QueryClient({
  defaultOptions: { queries: { retry: false } }
});

test('shortens URL successfully', async () => {
  const queryClient = createTestQueryClient();

  render(
    <QueryClientProvider client={queryClient}>
      <URLShortenerForm />
    </QueryClientProvider>
  );

  const input = screen.getByPlaceholderText('Enter long URL');
  fireEvent.change(input, { target: { value: 'https://example.com' } });

  const button = screen.getByText('Shorten URL');
  fireEvent.click(button);

  await waitFor(() => {
    expect(screen.getByText(/shortened/i)).toBeInTheDocument();
  });
});
```

**Integration Testing:**

```typescript
import { render, screen } from '@testing-library/react';
import userEvent from '@testing-library/user-event';
import App from './App';

test('complete URL shortening flow', async () => {
  const user = userEvent.setup();

  render(<App />);

  // Enter URL
  const urlInput = screen.getByLabelText('URL input');
  await user.type(urlInput, 'https://example.com');

  // Submit form
  const submitButton = screen.getByRole('button', { name: /shorten/i });
  await user.click(submitButton);

  // Verify short URL displayed
  await waitFor(() => {
    expect(screen.getByText(/short\.ly/)).toBeInTheDocument();
  });

  // Copy to clipboard
  const copyButton = screen.getByRole('button', { name: /copy/i });
  await user.click(copyButton);

  expect(screen.getByText(/copied/i)).toBeInTheDocument();
});
```

### ix) Frontend Deployment

**Build Optimization:**

```typescript
// vite.config.ts
export default defineConfig({
  build: {
    rollupOptions: {
      output: {
        manualChunks: {
          'react-vendor': ['react', 'react-dom', 'react-router-dom'],
          'query-vendor': ['@tanstack/react-query'],
          'ui-vendor': ['react-hot-toast', 'react-hook-form']
        }
      }
    },
    chunkSizeWarningLimit: 1000,
    minify: 'terser',
    terserOptions: {
      compress: {
        drop_console: true,
        drop_debugger: true
      }
    }
  }
});
```

**Environment Configuration:**

```typescript
// config.ts
export const config = {
  apiUrl: import.meta.env.VITE_API_URL || 'https://api.short.ly',
  environment: import.meta.env.MODE,
  enableAnalytics: import.meta.env.VITE_ENABLE_ANALYTICS === 'true',
  sentryDsn: import.meta.env.VITE_SENTRY_DSN
};
```

**Service Worker for Offline Support:**

```typescript
// service-worker.ts
self.addEventListener('fetch', (event: FetchEvent) => {
  if (event.request.url.includes('/api/')) {
    // Cache API responses
    event.respondWith(
      caches.open('api-cache').then(cache => {
        return fetch(event.request)
          .then(response => {
            cache.put(event.request, response.clone());
            return response;
          })
          .catch(() => cache.match(event.request))
      })
    );
  }
});
```

### x) Implementation Details

**Data Flow:**

1. **User Input** → URLShortenerForm component captures URL input with real-time validation
2. **Form Submission** → Triggers API call via React Query mutation with optimistic updates
3. **API Response** → Updates local state and cache with short URL
4. **Display** → ShortURLDisplay component shows the result with copy functionality
5. **Analytics** → AnalyticsDashboard fetches and displays analytics data with polling

**Event Handling:**

- Form submission triggers API call with debounced validation
- Copy button uses Clipboard API with fallback for older browsers
- Real-time analytics updates via polling every 30 seconds
- Keyboard shortcuts for common actions (Ctrl+C to copy)

**UI/UX Considerations:**

- **Loading States**: Skeleton screens during API calls for better perceived performance
- **Error Handling**: User-friendly error messages with retry options
- **Validation**: Real-time client-side URL validation with helpful error messages
- **Responsive Design**: Mobile-first layout using CSS Grid/Flexbox with breakpoints
- **Accessibility**: ARIA labels, keyboard navigation, screen reader support, focus management
- **Progressive Enhancement**: Works without JavaScript for basic functionality
- **Offline Support**: Service worker caches API responses for offline access

---

## b) Backend

*Note: Backend implementation details are kept minimal. Focus is on frontend integration.*

**API Endpoints Reference:**

- `POST /api/v1/shorten` - Create short URL
- `GET /api/v1/:shortCode` - Redirect to original URL
- `GET /api/v1/urls/:shortCode/analytics` - Get analytics data
- `GET /api/v1/alias/:alias/check` - Check alias availability

---

# 4) Algorithms

## Base62 Encoding Algorithm

**Purpose:** Convert auto-increment database IDs into short, URL-friendly strings.

**Algorithm:**

1. Take the numeric ID from database
2. Convert to Base62 using characters: `a-z, A-Z, 0-9` (62 characters total)
3. Repeatedly divide by 62 and use remainder as index
4. Reverse the result to get the short code

**Implementation:**

```typescript
const BASE62_CHARS = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789";

function encodeToBase62(id: number): string {
  if (id === 0) return BASE62_CHARS[0];

  let result = '';
  let num = id;

  while (num > 0) {
    result = BASE62_CHARS[num % 62] + result;
    num = Math.floor(num / 62);
  }

  return result.padStart(7, '0'); // Ensure minimum 7 characters
}

function decodeFromBase62(shortCode: string): number {
  let id = 0;

  for (let i = 0; i < shortCode.length; i++) {
    const char = shortCode[i];
    const charIndex = BASE62_CHARS.indexOf(char);
    id = id * 62 + charIndex;
  }

  return id;
}

```

**Complexity:**

- Time: O(log₆₂(n)) where n is the ID
- Space: O(1)
- **Capacity:** 7 characters = 62^7 ≈ 3.5 billion unique URLs

---

## Hash-based Encoding Algorithm

**Purpose:** Generate short URLs from long URLs using cryptographic hashing.

**Algorithm:**

1. Hash the original URL using MD5 or SHA256
2. Extract first 6-8 bytes from hash
3. Convert bytes to decimal number
4. Encode decimal to Base62

**Implementation:**

```typescript
import crypto from 'crypto';

function hashBasedEncoding(originalUrl: string, length: number = 7): string {
  // Step 1: Generate hash
  const hash = crypto.createHash('md5').update(originalUrl).digest('hex');

  // Step 2: Take first 6 bytes (12 hex characters)
  const hexSubstring = hash.substring(0, 12);

  // Step 3: Convert hex to decimal
  const decimal = parseInt(hexSubstring, 16);

  // Step 4: Encode to Base62
  return encodeToBase62(decimal).substring(0, length);
}

```

**Collision Handling:**

```typescript
async function generateUniqueShortCode(originalUrl: string): Promise<string> {
  let shortCode = hashBasedEncoding(originalUrl);
  let attempts = 0;
  const maxAttempts = 10;

  while (attempts < maxAttempts) {
    const exists = await checkIfShortCodeExists(shortCode);

    if (!exists) {
      return shortCode;
    }

    // Append attempt number to create variation
    shortCode = hashBasedEncoding(originalUrl + attempts.toString());
    attempts++;
  }

  throw new Error('Unable to generate unique short code');
}

```

**Complexity:**

- Time: O(1) for hash generation, O(log n) for Base62 encoding
- Space: O(1)
- **Collision Probability:** Low but requires collision detection

---

## Consistent Hashing Algorithm

**Purpose:** Distribute URLs across database shards evenly and minimize data movement when adding/removing shards.

**Algorithm:**

1. Create a hash ring (circular space) from 0 to 2^64 - 1
2. Hash each shard server to multiple points on the ring
3. Hash the shortCode to a point on the ring
4. Find the first shard clockwise from the shortCode's position

**Implementation:**

```typescript
import crypto from 'crypto';

class ConsistentHash {
  private ring: Map<number, string> = new Map();
  private sortedKeys: number[] = [];
  private virtualNodes: number = 150; // Virtual nodes per shard

  addShard(shardId: string): void {
    for (let i = 0; i < this.virtualNodes; i++) {
      const hash = this.hash(`${shardId}-${i}`);
      this.ring.set(hash, shardId);
      this.sortedKeys.push(hash);
    }
    this.sortedKeys.sort((a, b) => a - b);
  }

  removeShard(shardId: string): void {
    for (let i = 0; i < this.virtualNodes; i++) {
      const hash = this.hash(`${shardId}-${i}`);
      this.ring.delete(hash);
      const index = this.sortedKeys.indexOf(hash);
      if (index > -1) {
        this.sortedKeys.splice(index, 1);
      }
    }
  }

  getShard(shortCode: string): string {
    if (this.ring.size === 0) {
      throw new Error('No shards available');
    }

    const hash = this.hash(shortCode);

    // Find first shard clockwise
    for (const key of this.sortedKeys) {
      if (key >= hash) {
        return this.ring.get(key)!;
      }
    }

    // Wrap around to first shard
    return this.ring.get(this.sortedKeys[0])!;
  }

  private hash(key: string): number {
    const hash = crypto.createHash('md5').update(key).digest();
    return hash.readUInt32BE(0);
  }
}

```

**Complexity:**

- Time: O(log n) for shard lookup where n is number of virtual nodes
- Space: O(v * s) where v is virtual nodes, s is number of shards
- **Data Movement:** Only ~1/n of data moves when adding/removing shards

---

## URL Generation Algorithm

**Purpose:** Generate unique short codes for URLs with collision detection and retry logic.

**Algorithm:**

1. Check if custom alias provided
2. If custom: validate and check uniqueness
3. If auto-generate: use Base62 encoding with ID
4. Handle collisions with retry mechanism
5. Store in database with transaction

**Implementation:**

```typescript
async function generateShortUrl(
  originalUrl: string,
  customAlias?: string
): Promise<string> {
  // Validate original URL
  if (!isValidUrl(originalUrl)) {
    throw new Error('Invalid URL format');
  }

  let shortCode: string;

  if (customAlias) {
    // Custom alias path
    if (!isValidAlias(customAlias)) {
      throw new Error('Invalid alias format');
    }

    const exists = await checkAliasExists(customAlias);
    if (exists) {
      throw new Error('Alias already exists');
    }

    shortCode = customAlias;
  } else {
    // Auto-generate path
    shortCode = await generateUniqueShortCode(originalUrl);
  }

  // Store in database with transaction
  const session = await mongoose.startSession();
  session.startTransaction();

  try {
    await Url.create([{
      shortCode,
      originalUrl,
      createdAt: new Date()
    }], { session });

    await session.commitTransaction();
    return shortCode;
  } catch (error) {
    await session.abortTransaction();

    // Retry if collision occurred
    if (error.code === 11000) { // Duplicate key error
      if (!customAlias) {
        return generateShortUrl(originalUrl); // Retry with new ID
      }
      throw new Error('Alias collision detected');
    }

    throw error;
  } finally {
    session.endSession();
  }
}

```

**Complexity:**

- Time: O(1) average case, O(k) worst case where k is retry attempts
- Space: O(1)

---

## Cache Eviction Algorithm (LRU)

**Purpose:** Manage Redis cache efficiently by evicting least recently used URLs when cache is full.

**Algorithm:**

1. Maintain a doubly-linked list of cached URLs ordered by access time
2. Use a hash map for O(1) lookup
3. On access: move item to front (most recently used)
4. On eviction: remove item from back (least recently used)

**Implementation:**

```typescript
class LRUCache {
  private capacity: number;
  private cache: Map<string, { value: string; node: Node }> = new Map();
  private head: Node;
  private tail: Node;

  constructor(capacity: number) {
    this.capacity = capacity;
    this.head = new Node('', '');
    this.tail = new Node('', '');
    this.head.next = this.tail;
    this.tail.prev = this.head;
  }

  get(key: string): string | null {
    const item = this.cache.get(key);

    if (!item) {
      return null;
    }

    // Move to front (most recently used)
    this.moveToFront(item.node);
    return item.value;
  }

  put(key: string, value: string): void {
    const existing = this.cache.get(key);

    if (existing) {
      existing.value = value;
      this.moveToFront(existing.node);
      return;
    }

    // Check capacity
    if (this.cache.size >= this.capacity) {
      this.evictLRU();
    }

    // Add new node
    const node = new Node(key, value);
    this.addToFront(node);
    this.cache.set(key, { value, node });
  }

  private moveToFront(node: Node): void {
    this.removeNode(node);
    this.addToFront(node);
  }

  private addToFront(node: Node): void {
    node.prev = this.head;
    node.next = this.head.next;
    this.head.next!.prev = node;
    this.head.next = node;
  }

  private removeNode(node: Node): void {
    node.prev!.next = node.next;
    node.next!.prev = node.prev;
  }

  private evictLRU(): void {
    const lru = this.tail.prev!;
    this.removeNode(lru);
    this.cache.delete(lru.key);
  }
}

class Node {
  key: string;
  value: string;
  prev: Node | null = null;
  next: Node | null = null;

  constructor(key: string, value: string) {
    this.key = key;
    this.value = value;
  }
}

```

**Complexity:**

- Time: O(1) for get and put operations
- Space: O(capacity)

---

## Sharding Key Selection Algorithm

**Purpose:** Determine which database shard should store a given URL based on shortCode.

**Algorithm:**

1. Hash the shortCode using consistent hashing
2. Map hash value to shard using hash ring
3. Return shard identifier for database routing

**Implementation:**

```typescript
function getShardForShortCode(shortCode: string, numShards: number): number {
  // Hash the shortCode
  const hash = crypto.createHash('md5').update(shortCode).digest();
  const hashValue = hash.readUInt32BE(0);

  // Map to shard using modulo
  return hashValue % numShards;
}

// Alternative: Using consistent hashing
function getShardConsistentHash(shortCode: string, consistentHash: ConsistentHash): string {
  return consistentHash.getShard(shortCode);
}

```

**Complexity:**

- Time: O(1) for modulo, O(log n) for consistent hashing
- Space: O(1)

---

# 5) Data Models

## URLs Collection (MongoDB)

```javascript
{
  _id: ObjectId,
  shortCode: String,        // Unique index, 7 characters
  originalUrl: String,      // Indexed for lookups
  userId: ObjectId,         // Optional, indexed
  createdAt: Date,          // Indexed
  expiresAt: Date,          // Optional, indexed
  clickCount: Number,       // Default: 0
  isActive: Boolean         // Default: true
}

// Indexes:
// - { shortCode: 1 } (unique)
// - { userId: 1 }
// - { expiresAt: 1 }
// - { createdAt: -1 }

```

## Analytics Collection (MongoDB)

```javascript
{
  _id: ObjectId,
  shortCode: String,        // Indexed
  clickedAt: Date,          // Indexed
  ipAddress: String,
  referrer: String,         // Optional
  userAgent: String,        // Optional
  country: String,          // Optional, from IP geolocation
  device: String            // Optional, mobile/desktop/tablet
}

// Indexes:
// - { shortCode: 1, clickedAt: -1 } (compound)
// - { clickedAt: -1 }

```

## Alternative: SQL Schema (if using PostgreSQL/MySQL)

**URLs Table:**

```sql
CREATE TABLE urls (
    id BIGINT PRIMARY KEY AUTO_INCREMENT,
    short_code VARCHAR(10) UNIQUE NOT NULL,
    original_url TEXT NOT NULL,
    user_id BIGINT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    expires_at TIMESTAMP NULL,
    click_count INT DEFAULT 0,
    is_active BOOLEAN DEFAULT TRUE,
    INDEX idx_short_code (short_code),
    INDEX idx_user_id (user_id),
    INDEX idx_expires_at (expires_at)
);

```

**Analytics Table:**

```sql
CREATE TABLE analytics (
    id BIGINT PRIMARY KEY AUTO_INCREMENT,
    short_code VARCHAR(10) NOT NULL,
    clicked_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    ip_address VARCHAR(45),
    referrer TEXT,
    user_agent TEXT,
    country VARCHAR(2),
    device VARCHAR(20),
    INDEX idx_short_code_time (short_code, clicked_at),
    INDEX idx_clicked_at (clicked_at)
);

```

---

# 6) Database Transactions and Consistency

### MongoDB Transactions

**Transaction Usage:**

- **Multi-Document Transactions** - For operations requiring ACID guarantees
- **Example:** URL creation + analytics initialization in single transaction
- **Session Management:** Use MongoDB sessions for transaction control

**Example:**

```typescript
const session = await mongoose.startSession();
session.startTransaction();
try {
  await Url.create([urlData], { session });
  await Analytics.create([analyticsData], { session });
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

- **URL Consistency:** Ensure short code uniqueness using unique index and application-level checks
- **Analytics Consistency:** Use transactions for analytics updates to maintain data integrity
- **Cache Consistency:** Invalidate cache on URL updates to prevent serving stale data
- **Optimistic Locking:** Use version fields for conflict detection and retry logic

---

# 7) Protocols

### REST API Protocol

- **Protocol:** REST (Representational State Transfer)
- **Data Format:** JSON
- **HTTP Methods:** GET, POST
- **Status Codes:** 200 (Success), 301/302 (Redirect), 404 (Not Found), 429 (Rate Limited)

### Redirect Protocol

- **301 Permanent Redirect** - For SEO, tells search engines the redirect is permanent
- **302 Temporary Redirect** - For analytics, allows tracking each redirect

---

# 8) API Design

### POST /api/v1/shorten

- **URL:** `/api/v1/shorten`
- **Method:** POST
- **Request Body:**

  ```json
  {
    "url": "https://www.example.com/very/long/url/path",
    "customAlias": "my-link",
    "expiresAt": "2024-12-31T23:59:59Z"
  }

  ```

- **Response:**

  ```json
  {
    "success": true,
    "data": {
      "shortUrl": "https://short.ly/my-link",
      "shortCode": "my-link",
      "originalUrl": "https://www.example.com/very/long/url/path",
      "expiresAt": "2024-12-31T23:59:59Z"
    }
  }

  ```

- **Status Codes:** 201 (Created), 400 (Invalid URL), 409 (Alias Exists)

### GET /api/v1/:shortCode

- **URL:** `/api/v1/:shortCode`
- **Method:** GET
- **Response:** 301 Redirect to original URL
- **Status Codes:** 301 (Redirect), 404 (Not Found), 410 (Gone - Expired)

### GET /api/v1/urls/:shortCode/analytics

- **URL:** `/api/v1/urls/:shortCode/analytics`
- **Method:** GET
- **Response:**

  ```json
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
      ]
    }
  }

  ```

- **Status Codes:** 200 (Success), 404 (Not Found)

---

# 9) Caching Strategy

### Redis Cache

**Cache Strategy:**

- **Key Format:** `url:{shortCode}`
- **Value:** Original URL string
- **TTL:** 1 hour (configurable, can be extended for hot URLs)
- **Eviction Policy:** LRU (Least Recently Used)

**Cache Pattern:**

- **Cache-Aside Pattern**: Check cache first, if miss query database and update cache
- **Cache 20% hot URLs**: Following 80-20 rule, cache the most popular URLs
- **Cache Hit Ratio Target**: 90% (only 10% of requests hit database)

### Cache Warming

- **Pre-load Strategy**: Pre-load top 1M URLs into cache on server startup
- **Update on Read**: Update cache on every database read to keep hot URLs cached
- **TTL Extension:** Extend TTL for frequently accessed URLs

---

# 10) Error Handling

### Error Scenarios and Responses

**Edge Cases Handling:**

- **Invalid URL Format:** Return 400 Bad Request with descriptive error message
- **Custom Alias Already Exists:** Return 409 Conflict with suggestion to use different alias
- **URL Not Found:** Return 404 Not Found when short code doesn't exist in database
- **URL Expired:** Return 410 Gone when URL has passed expiration date
- **Rate Limiting:** Return 429 Too Many Requests when user exceeds rate limit
- **Database Connection Failure:** Return 503 Service Unavailable with retry suggestion
- **Cache Miss:** Gracefully fallback to database (not an error, but handled scenario)

**URL Conflicts:**

- **Collision Detection:** Implement collision detection during URL creation
- **Retry Logic:** If collision occurs (rare with base62), retry with next ID
- **Database Constraints:** Use unique index on shortCode column as primary defense
- **Distributed Locks:** Use Redis distributed locks for custom alias creation to prevent race conditions

### Error Response Format

```json
{
  "error": {
    "code": "INVALID_URL",
    "message": "The provided URL is not valid",
    "details": "URL must start with http:// or https://"
  }
}

```

---

# 11) Deployment and DevOps

### Scalability

**API Layer:**

- Deploy API layer across multiple instances behind load balancer
- Use round-robin or consistent hashing for request distribution
- Stateless design allows horizontal scaling

**Database Sharding:**

- **Hash-Based Sharding:** Apply hash function to shortCode to determine shard
  - Formula: `hash(shortCode) % N` where N is number of shards
  - Ensures even distribution across shards
- **Consistent Hashing:** Use consistent hashing to minimize data movement when adding/removing shards
- **Shard Management:** Metadata service tracks shard locations and health for dynamic shard management

**Caching:**

- Distributed Redis cluster for high availability
- Cache frequently accessed short URL-to-long URL mappings
- Reduces database load significantly (90% cache hit ratio target)

**Read Replicas:**

- Use read replicas for analytics queries to separate read/write workloads
- Multiple replicas for high availability and load distribution

### Availability

**Replication:**

- Database replication ensures data availability even if some nodes fail
- Multi-region replication for disaster recovery

**Failover:**

- Automated failover mechanisms for API and data store layers
- Switch to backup servers automatically in case of failure
- Health checks and monitoring for proactive failover

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

### Database Deployment

**MongoDB Setup:**

- **MongoDB Atlas** - Managed MongoDB service with automatic backups
- **Backup Strategy:** Daily automated backups with point-in-time recovery
- **Indexing:** Proper indexes on shortCode, userId, expiresAt, and createdAt
- **Sharding:** Horizontal sharding across multiple nodes for scalability

**Redis Setup:**

- **Redis Cloud / AWS ElastiCache** - Managed Redis service
- **Cluster Mode:** Redis cluster for high availability and performance
- **Persistence:** RDB snapshots and AOF for data durability

---

# 12) Security Considerations

### MongoDB Transactions

**Transaction Usage:**

- **Multi-Document Transactions** - For operations requiring ACID guarantees
- **Example:** URL creation + analytics initialization in single transaction
- **Session Management:** Use MongoDB sessions for transaction control

**Example:**

```typescript
const session = await mongoose.startSession();
session.startTransaction();
try {
  await Url.create([urlData], { session });
  await Analytics.create([analyticsData], { session });
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

- **URL Consistency:** Ensure short code uniqueness using unique index and application-level checks
- **Analytics Consistency:** Use transactions for analytics updates to maintain data integrity
- **Cache Consistency:** Invalidate cache on URL updates to prevent serving stale data
- **Optimistic Locking:** Use version fields for conflict detection and retry logic

### Security Considerations

**Rate Limiting:**

- Implement rate limiting at API layer to prevent abuse
- Limit number of URLs each user can create per minute/hour
- Use Redis for distributed rate limiting across multiple servers

**Input Validation:**

- Validate URLs to ensure they don't contain malicious content
- Sanitize user input to prevent injection attacks
- Check URL format and protocol (http/https only)

**HTTPS:**

- All communication between clients and service encrypted using HTTPS
- Prevents eavesdropping and man-in-the-middle attacks
- SSL/TLS certificates for secure connections

**Monitoring and Alerts:**

- Set up monitoring for unusual activity patterns
- Trigger alerts for potential DDoS attacks or misuse
- Track metrics: request rates, error rates, response times
- Log all operations for security auditing

---

# 13) Interview Answers

---

## Q1. 💡 Designing a scalable URL shortener system

**The Challenge:** We need to handle 100M+ requests per day with a 10:1 read/write ratio, support billions of URLs, and keep redirect latency under 100ms.

**My Approach:**

**First, URL Generation - Base62 vs Hash-based:**
I'd use Base62 encoding because it's predictable and collision-free. We convert auto-increment database IDs to 7-character codes using a-z, A-Z, 0-9. That gives us 62^7, roughly 3.5 billion unique URLs. The trade-off is it reveals how many URLs we've created, but for most use cases that's acceptable. Hash-based is an alternative if we need idempotency - same long URL always gets the same short URL - but it requires collision handling.

**Architecture - Think Layers:**
At the front, a load balancer distributes traffic to stateless API servers. This is key - stateless means we can scale horizontally without sticky sessions. Behind that, MongoDB with hash-based sharding on the shortCode. I chose MongoDB over SQL because we're doing simple key-value lookups at scale, and NoSQL handles horizontal scaling better.

**The Caching Strategy:**
Here's where it gets interesting - we follow the 80-20 rule. 20% of URLs generate 80% of traffic. So we cache the top 20% in Redis, targeting a 90% cache hit rate. This means most redirects never hit the database. We also use a CDN for redirects to serve from edge locations globally.

**Scaling the Database:**
For billions of URLs, we shard by hashing the shortCode. I'd use consistent hashing so when we add or remove shards, we only move about 1/n of the data. Read replicas handle analytics queries separately, so heavy analytics don't slow down writes.

**Decoupling Analytics:**
Analytics go through a message queue - RabbitMQ or Kafka - so tracking clicks doesn't block redirects. This is critical because redirects need to be fast, but analytics can be processed asynchronously.

**Results:**

- Handles 1,160 writes/sec average, 11,600 at peak
- Redirect latency under 100ms (90% from cache)
- Scales to billions of URLs across 20-30 shards
- 99.9% uptime with redundancy

**Key Insight:** The 80-20 rule is crucial here. Most traffic goes to popular URLs, so caching those gives us massive performance gains. Also, keeping the API layer stateless and using async processing for non-critical features allows us to scale independently.

---

## Q2. 💡 Handling URL collisions and ensuring uniqueness

**The Problem:** With concurrent requests, we need to guarantee no two URLs get the same short code, especially for custom aliases where users might try the same name.

**My Solution - Defense in Depth:**

**Layer 1: Database Constraints (The Foundation)**
The database has a unique index on shortCode. This is our ultimate authority - even if application logic fails, the database won't allow duplicates. We use transactions to make URL creation atomic. This is the most important layer because it's enforced at the lowest level.

**Layer 2: Application Checks (Fast Feedback)**
Before inserting, we check if the shortCode exists. For base62 encoding, collisions are extremely rare, but we still handle them. If we catch a duplicate key error - MongoDB error code 11000 - we retry with the next ID. This gives us fast feedback and reduces unnecessary database writes.

**Layer 3: Custom Alias Handling (The Tricky Part)**
Custom aliases are where race conditions happen. Two users might try "mybrand" at the same time. Here's what I do:

- First, validate the format - only alphanumeric and hyphens
- Check against reserved words like "admin" or "api"
- Use a distributed lock in Redis before checking existence
- If it exists, return 409 Conflict with a helpful message

The distributed lock is crucial. Without it, two requests could both check, see it's available, and both try to create it. The lock ensures only one request can check and create at a time.

**Layer 4: Frontend Validation (User Experience)**
As the user types, we debounce API calls to check availability. Show a green checkmark if available, red X if taken. This prevents users from submitting unavailable aliases and reduces server load.

**The Code Flow:**

```typescript
// For custom aliases, use distributed lock
if (customAlias) {
  const lock = await acquireLock(`alias:${customAlias}`, 5000);
  try {
    if (await exists(customAlias)) throw new ConflictError();
  } finally {
    releaseLock(lock);
  }
}

// Create with transaction - database enforces uniqueness
const session = await mongoose.startSession();
session.startTransaction();
try {
  await Url.create([{ shortCode, originalUrl }], { session });
  await session.commitTransaction();
} catch (error) {
  if (error.code === 11000) {
    // Retry with new ID
    return createShortUrl(originalUrl);
  }
  throw error;
}

```

**Why This Works:**

- Database constraints are the source of truth - these can't be bypassed
- Application checks give fast feedback and reduce database load
- Distributed locks prevent race conditions in high-concurrency scenarios
- Retry logic handles edge cases transparently

**Key Insight:** You need multiple layers because each serves a different purpose. Database constraints ensure correctness, application checks improve UX, and locks handle concurrency. No single layer is sufficient on its own.

---

## Q3. 🗄️ Scaling the database to handle billions of URLs

**The Challenge:** A single database can't handle billions of URLs. We need horizontal scaling that maintains performance and allows us to add capacity without downtime.

**My Strategy - Sharding with Consistent Hashing:**

**Why Sharding?**
Vertical scaling - bigger machines - hits limits. Horizontal scaling - more machines - is the answer. We shard by hashing the shortCode, which distributes URLs evenly across shards. No hot spots, no single point of failure.

**The Sharding Key Decision:**
I use the hash of shortCode as the sharding key. This is important because:

- It's evenly distributed - hash functions spread data uniformly
- Lookups are fast - we know exactly which shard to query
- It's stable - same shortCode always maps to same shard

**Consistent Hashing - The Game Changer:**
Simple modulo sharding (`hash % numShards`) breaks when you add or remove shards - you'd have to rehash everything. Consistent hashing solves this. We create a hash ring, place each shard at multiple points (virtual nodes), and map shortCodes to the nearest shard clockwise.

When we add a shard, only about 1/n of data moves. When we remove one, same thing. This is huge for production - we can scale without massive data migration.

**Read Replicas for Isolation:**
Analytics queries are heavy - aggregations, time-series data, complex filters. If these run on the primary shards, they'll slow down writes. So I use read replicas. Writes go to primaries, analytics reads go to replicas. This isolates workloads and improves performance.

**Shard Management:**
A metadata service tracks which shard has which data, monitors health, and routes requests. If a shard goes down, we automatically route to a replica. The application layer abstracts this - developers just query by shortCode, the router figures out which shard.

**Indexing Strategy:**
Each shard needs proper indexes. Unique index on shortCode for fast lookups. Compound indexes on userId, createdAt, expiresAt for common queries. Critical point: design queries to hit a single shard. Cross-shard queries are slow and complex.

**The Implementation:**

```typescript
// Router abstracts sharding complexity
class ShardRouter {
  getShard(shortCode: string): string {
    return this.consistentHash.getShard(shortCode);
  }

  routeRequest(shortCode: string, operation: 'read' | 'write') {
    const shard = this.getShard(shortCode);
    // Use read replica for analytics, primary for writes
    return operation === 'read' ? shard.readReplica : shard.primary;
  }
}

```

**Results:**

- Handles billions of URLs across 20-30 shards
- Query latency stays under 10ms even at scale
- 99.9% uptime with automatic failover
- Can add shards without downtime

**Key Insight:** Consistent hashing is what makes this production-ready. Without it, scaling becomes a nightmare of data migration. Also, separating read and write workloads is crucial - analytics can be slow, but redirects must be fast. The abstraction layer is important too - developers shouldn't need to think about sharding.

---

## Q4. 💡 Handling expired URLs and cleanup

**The Problem:** URLs can expire, and we need to prevent redirects to expired URLs while cleaning up old data to keep the database manageable.

**My Approach - Two-Phase Strategy:**

**Phase 1: Real-Time Validation (User-Facing)**
Every redirect request checks expiration before serving. If expired, we return 410 Gone - this is clearer than 404 because it tells the user the URL existed but expired. We immediately invalidate it from cache so we don't serve stale data. This is critical - we can't rely on cache TTL alone because expiration might happen mid-TTL.

**Phase 2: Background Cleanup (Maintenance)**
A daily cron job runs during off-peak hours - say 2 AM - to clean up expired URLs. Here's the strategy:

- First, soft delete - mark as inactive. This gives us a safety net in case we need to recover
- After a grace period (7 days), hard delete
- Process in batches of 1000 to avoid overwhelming the database
- We keep expired URLs for 30 days before cleanup - this handles edge cases and provides an audit trail

**Why Soft Delete First?**
Mistakes happen. Maybe a user reports an issue, or we need to investigate. Soft delete allows us to recover. After the grace period, we're confident it's safe to hard delete.

**Cache Synchronization:**
This is important - cache and database must stay in sync. When we detect expiration, we invalidate cache immediately. We also set Redis TTL to match expiration time, but that's a backup. The real-time check is primary.

**User Experience:**
On the frontend, we show expiration warnings for URLs expiring within 7 days. Users can see expiration dates in their dashboard and extend them if needed. This reduces support requests and improves UX.

**The Code:**

```typescript
// Real-time check - happens on every redirect
async function redirect(shortCode: string) {
  const url = await getUrl(shortCode);

  if (url?.expiresAt && new Date() > url.expiresAt) {
    await invalidateCache(shortCode);
    throw new GoneError('URL expired');
  }

  return url.originalUrl;
}

// Background job - runs daily
async function cleanupExpired() {
  const cutoff = new Date(Date.now() - 30 * 24 * 60 * 60 * 1000);

  // Soft delete in batches
  const batch = await Url.find({ expiresAt: { $lt: cutoff } }).limit(1000);
  for (const url of batch) {
    await invalidateCache(url.shortCode);
    await url.updateOne({ isActive: false, deletedAt: new Date() });
  }

  // Hard delete after grace period
  await Url.deleteMany({
    isActive: false,
    deletedAt: { $lt: new Date(Date.now() - 7 * 24 * 60 * 60 * 1000) }
  });
}

```

**Why This Works:**

- Real-time validation ensures users never get redirected to expired URLs
- Background cleanup prevents database bloat without impacting users
- Soft delete provides safety net and audit trail
- Cache invalidation keeps data consistent

**Key Insight:** Always validate at request time, not just creation time. Expiration is a time-based condition that changes. Also, background jobs are essential for maintenance - they run when users aren't affected. The soft-delete pattern is a best practice - it gives you recovery options and better observability.

---

## Q5. 💡 Implementing analytics tracking for URL clicks

**The Challenge:** Track detailed analytics - clicks, location, device, referrer - without slowing down redirects. We're talking millions of events per day.

**My Solution - Decoupled Async Pipeline:**

**The Core Principle:**
Analytics can't block redirects. Redirects need to be fast - under 100ms. Analytics can be processed later. So we decouple them completely using a message queue.

**Event Collection - Fire and Forget:**
During a redirect, we extract analytics data - IP, user agent, referrer, timestamp. We send this to a message queue (RabbitMQ or Kafka) asynchronously. We don't wait for acknowledgment. This adds less than 5ms overhead. The redirect returns immediately.

**Why Message Queue?**
Message queues give us several benefits:

- Decoupling - redirect service doesn't care about analytics processing
- Buffering - if analytics is slow, events queue up
- Independent scaling - we can scale workers separately
- Reliability - if a worker crashes, events aren't lost

**Event Processing - Worker Pool:**
Separate worker processes consume events from the queue. They process in batches - 100 to 1000 events at a time. This is much more efficient than one-by-one. Workers enrich the data - add geolocation from IP, detect device type, filter bots. Then store raw events in MongoDB.

**The Aggregation Strategy:**
Here's the key insight - we can't query raw events for dashboards. With millions of events, that's too slow. So we pre-aggregate. As events come in, we update aggregates - daily counts, top countries, device breakdown. We store these in separate collections. When a user queries analytics, we read pre-calculated data, not raw events.

**Time Windows:**
We aggregate by different time windows - hour, day, week, month. This allows users to see trends at different granularities. We update aggregates incrementally - when a new click comes in, we increment the count for that day. Much faster than recalculating from scratch.

**Query Optimization:**
Even with aggregates, we cache in Redis. Analytics queries are cached for 5-15 minutes. We use compound indexes on shortCode and clickedAt for time-range queries. For large result sets, cursor-based pagination.

**The Implementation:**

```typescript
// During redirect - non-blocking
async function trackClick(shortCode: string, req: Request) {
  const event = {
    shortCode,
    clickedAt: new Date(),
    ip: req.ip,
    userAgent: req.headers['user-agent'],
    referrer: req.headers['referer']
  };

  // Fire and forget - don't wait
  messageQueue.publish('analytics', event);
}

// Worker - processes in batches
async function processEvents() {
  const batch = await queue.consume('analytics', { batchSize: 100 });

  // Enrich and store
  const enriched = batch.map(enrichEvent); // Add geo, device, etc.
  await Analytics.insertMany(enriched);

  // Update aggregates incrementally
  for (const event of enriched) {
    await incrementAggregate(event.shortCode, event);
  }
}

// Dashboard query - fast because pre-aggregated
async function getAnalytics(shortCode: string, range: string) {
  const cached = await redis.get(`analytics:${shortCode}:${range}`);
  if (cached) return JSON.parse(cached);

  const data = await AnalyticsAggregate.findOne({ shortCode, range });
  await redis.setex(`analytics:${shortCode}:${range}`, 300, JSON.stringify(data));
  return data;
}

```

**Why This Works:**

- Async processing means zero impact on redirect performance
- Message queue provides buffering and reliability
- Pre-aggregation makes dashboard queries fast
- Batch processing is 10-100x more efficient than individual processing
- Caching reduces database load for frequently accessed analytics

**Results:**

- Less than 5ms overhead on redirects
- Processes millions of events per day
- Dashboard loads in under 1 second
- Workers scale independently based on queue depth

**Key Insight:** The decoupling is crucial. Analytics is a nice-to-have feature, but redirects are the core business. They must never be blocked. Pre-aggregation is also essential - you can't query raw events at scale. The incremental update pattern is much more efficient than recalculating aggregates from scratch.
