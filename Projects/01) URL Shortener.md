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

## a) Functional Requirements

- **Generate unique short URL** for a given long URL
- **Redirect users** to the original URL when short URL is accessed
- **Custom alias support** - Allow users to customize their short URLs (optional)
- **Link expiration** - URLs become inactive after a specified period (optional)
- **Analytics tracking** - Track click counts, referrer information, geographic location, and device types (optional)

---

## b) Non-Functional Requirements

- **High availability** - Service should be up 99.9% of the time with fault tolerance and redundancy
- **Low latency** - URL shortening and redirects should happen in milliseconds (< 100ms for redirect)
- **Scalability** - System should handle millions of requests per day and scale to billions of URLs
- **Durability** - Shortened URLs should work for years with reliable data persistence
- **Security** - Prevent malicious use such as phishing, implement rate limiting, input validation, and HTTPS
- **URL length** - Short URLs should be as short as possible (typically 6-8 characters)

---

## c) MVP (Minimum Viable Product)

**Phase 1: Core Features - Must Have**

- URL shortening and redirection
- Basic analytics (click count)
- Custom alias support
- Responsive web interface
- Copy to clipboard functionality

**Phase 2: Enhanced Features**

- URL expiration with frontend warnings
- Advanced analytics dashboard (referrer, location, device)
- User accounts and URL management dashboard
- Real-time analytics updates
- QR code generation

---

## d) Technology Choices

### Frontend Framework

- **React 19** - Latest React version with useOptimistic, useActionState, useTransition, useDeferredValue, and use() hook
- **TypeScript** - Type safety and better developer experience
- **React Router** - Client-side routing for single-page application

### State Management

- **React Query (TanStack Query)** - Server state management, caching, and synchronization
- **Context API** - Global state for user authentication and theme
- **useState/useReducer** - Local component state

### UI/UX Libraries

- **React Hot Toast** - Toast notifications for user feedback
- **Chart.js / Recharts** - Analytics visualization

### Build Tools

- **Vite** - Fast build tool and dev server
- **Webpack** (alternative) - Module bundler

### Testing

- **React Testing Library** - Component testing
- **Vitest / Jest** - Unit testing framework
- **Playwright / Cypress** - E2E testing

### Deployment

- **Vercel / Netlify** - Static site hosting with CDN
- **AWS S3 + CloudFront** - Alternative deployment option

---

## e) Architecture Overview

The frontend follows a layered architecture with clear separation of concerns, optimized for URL shortening operations with real-time analytics.

**Component Structure:**

```

Frontend Application
├── Presentation Layer
│   ├── UI Components (Buttons, Inputs, Cards)
│   ├── Feature Components (URLShortenerForm, AnalyticsDashboard, URLList)
│   └── Layout Components (Header, Footer, Navigation, MainLayout)
├── Business/Controller Layer
│   ├── Business Logic (URL validation, alias format checking, data transformation)
│   ├── Custom Hooks (useShortenURL, useAnalytics, useAliasCheck)
│   └── Service Functions (Pure functions for data processing and validation)
├── State Management
│   ├── Client State
│   │   ├── Local State (useState) - Component-specific UI state
│   │   ├── Global State (Redux Toolkit/Zustand) - URL list, user preferences
│   │   └── Context API - User authentication, theme preferences
│   └── Server State
│       ├── React Query (useQuery) - API data caching, refetching, optimistic updates
│       └── Service Worker - Offline caching, background sync
├── API Integration
│   ├── API Client (Axios with interceptors for auth, error handling)
│   ├── API Services (urlService, analyticsService)
│   └── Request/Response Transformation (Data normalization and error handling)
└── Routing
    ├── Public Routes (Home, About)
    ├── Protected Routes (Dashboard, Analytics)
    └── Route Guards (Authentication and authorization checks)

```

**Frontend Deployment:**

- **Build**: Production bundle with code splitting and tree shaking using Webpack/Vite
- **CDN**: Static assets served from CloudFront/Cloudflare edge locations

- **Caching**: Aggressive caching for static assets, cache-busting for updates
- **Environment**: Environment variables for API endpoints and feature flags

**Key Frontend Components:**

- **React 19 Application**: - Single-page application with client-side routing
  - Component-based architecture for reusability
  - React Query with React 19 hooks (useOptimistic, useTransition, useDeferredValue)
  - Responsive design for mobile and desktop
  - Modern React 19 features for better performance and UX

- **CDN/Edge**: - Global distribution of static assets
  - Edge caching for improved performance
  - DDoS protection and rate limiting at edge

---

## f) App Flow

### Complete System Flow (Frontend Perspective)

**Primary User Flow - URL Shortening:**

1. **User lands on homepage** → React Router renders HomePage component
2. **User enters URL** → URLInput component captures input, validates in real-time
3. **User clicks submit** → URLShortenerForm triggers React Query mutation
4. **Loading state** → SubmitButton shows loading spinner, form disabled
5. **API call** → useMutation sends POST request to /api/v1/shorten
6. **Success response** → React Query caches response, ShortUrlDisplay component renders
7. **User copies URL** → CopyButton uses Clipboard API, shows toast notification
8. **State update** → Components re-render with new short URL data

**Component Interaction Flow:**

```

User Input → URLInput (local state)
            ↓
Form Submit → URLShortenerForm (React Query mutation)
            ↓
API Call → useShortenURL hook (business logic)
            ↓
Response → React Query cache update
            ↓
Re-render → ShortUrlDisplay (receives cached data)

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

**Custom Alias Flow:**

1. **User enters custom alias** → AliasInput component validates format (alphanumeric, hyphens, underscores)
2. **Real-time validation** → useAliasCheck hook checks availability via debounced API call
3. **Availability feedback** → UI shows green checkmark if available, red X if taken
4. **Form submission** → Custom alias included in POST request to /api/v1/shorten
5. **Success/Error** → Toast notification confirms creation or shows error if alias exists

**URL Expiration Flow:**

1. **User sets expiration** → DatePicker component allows selecting expiration date
2. **Frontend validation** → Ensures expiration is in the future
3. **Warning display** → Shows warning badge for URLs expiring soon (< 7 days)
4. **Expiration check** → Frontend checks expiration before displaying URL
5. **Expired URL handling** → Shows "Expired" badge and disables copy functionality

**QR Code Generation Flow:**

1. **User clicks QR button** → QRCodeButton triggers QR code generation
2. **QR code library** → Uses qrcode.react or similar library to generate QR code
3. **Display modal** → Shows QR code in modal with download option
4. **Download functionality** → Allows user to download QR code as PNG image

---

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
│   │   ├── URLShortenerForm
│   │   │   ├── URLInput
│   │   │   ├── AliasInput (optional)
│   │   │   └── SubmitButton
│   │   └── ShortUrlDisplay
│   │       ├── ShortUrlCard
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

**1. URLShortenerForm Component:**

- Handles form submission logic
- Manages form state with useState
- Uses React Query mutation for API call
- Validates input before submission

**2. ShortUrlDisplay Component:**

- Displays generated short URL
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

**5. URLItem Component:**

- Displays individual shortened URL with metadata
- Shows original URL, short URL, click count, expiration status
- Handles actions: copy, view analytics, delete, edit
- Implements optimistic updates for delete/edit operations

**6. DateRangeFilter Component:**

- Allows filtering analytics by date range
- Uses date picker library (react-datepicker)
- Updates query params and triggers React Query refetch
- Persists filter state in URL for shareability

**7. QRCodeModal Component:**

- Displays QR code in modal overlay
- Generates QR code using qrcode.react library
- Provides download functionality for QR code image
- Handles modal open/close state

# 4) Data Models

### TypeScript Interfaces

```typescript
interface ShortUrl {
  shortCode: string;
  originalUrl: string;
  shortUrl: string;
  expiresAt?: string;
  createdAt: string;
}

interface Analytics {
  shortCode: string;
  clickCount: number;
  uniqueClicks: number;
  topCountries: Array<{ country: string; clicks: number }>;
  clicksByDate: Array<{ date: string; clicks: number }>;
  referrers: Array<{ referrer: string; clicks: number }>;
  devices: Array<{ device: string; clicks: number }>;
}

interface User {
  id: string;
  email: string;
  name: string;
  createdAt: string;
}

interface CreateShortUrlRequest {
  url: string;
  customAlias?: string;
  expiresAt?: string;
}

interface CreateShortUrlResponse {
  success: boolean;
  data: ShortUrl;
  error?: {
    code: string;
    message: string;
  };
}

interface ApiError {
  success: false;
  error: {
    code: string;
    message: string;
    details?: string;
  };
}

interface FormState {
  url: string;
  customAlias: string;
  expiresAt: string | null;
  errors: {
    url?: string;
    alias?: string;
    expiresAt?: string;
  };
}

```

# 5) API Design

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

- **Status Codes:** 200 (Success), 404 (Not Found)

---

# 6) Protocols

### REST API Protocol

**Request Format:**

- HTTP methods: GET, POST, PUT, DELETE
- Headers: Content-Type: application/json
- Authentication: Bearer token in Authorization header

**Response Format:**

- Success: `{ success: true, data: {...} }`
- Error: `{ success: false, error: {...} }`
- Status codes: 200 (Success), 201 (Created), 400 (Bad Request), 401 (Unauthorized), 404 (Not Found), 500 (Server Error)

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

**Authentication:**

- Bearer token authentication for protected routes
- Token stored in httpOnly cookie
- Automatic token refresh on 401 responses
- Redirect to login on authentication failure

**Request Headers:**

```

Content-Type: application/json
Authorization: Bearer <token>
Accept: application/json

```

**Response Headers:**

```

Content-Type: application/json
X-RateLimit-Limit: 1000
X-RateLimit-Remaining: 999
X-RateLimit-Reset: 1640995200

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

**State Management for URL Shortener:**

**Client State Examples (React 19):**

```typescript
import { useState, useTransition, useDeferredValue, useActionState } from 'react';

// Form state with useActionState (React 19)
const [formState, formAction, isPending] = useActionState(
  async (prevState: FormState, formData: FormData) => {
    const url = formData.get('url') as string;
    const customAlias = formData.get('customAlias') as string;

    // Validation
    const urlValidation = validateUrl(url);
    if (!urlValidation.isValid) {
      return { ...prevState, errors: { url: urlValidation.error } };
    }

    // Submit logic
    return prevState;
  },
  { url: '', customAlias: '', expiresAt: null, errors: {} }
);

// Modal visibility
const [isQRModalOpen, setIsQRModalOpen] = useState(false);

// UI state with deferred value for performance
const [selectedDateRange, setSelectedDateRange] = useState({ start: null, end: null });
const deferredDateRange = useDeferredValue(selectedDateRange);

```

**Server State with React Query (React 19):**

```typescript
import { use, useTransition } from 'react';
import { useQuery, useMutation, useSuspenseQuery } from '@tanstack/react-query';

// Fetch URLs list with Suspense (React 19)
const { data: urls } = useSuspenseQuery({
  queryKey: ['urls'],
  queryFn: fetchUserUrls,
  staleTime: 30000 // 30 seconds
});

// Using use() hook for promise handling (React 19)
function AnalyticsData({ analyticsPromise }: { analyticsPromise: Promise<Analytics> }) {
  const analytics = use(analyticsPromise);
  return <AnalyticsChart data={analytics} />;
}

// Shorten URL mutation with optimistic updates
const { mutate: shortenUrl, isPending } = useMutation({
  mutationFn: createShortUrl,
  onSuccess: () => {
    queryClient.invalidateQueries({ queryKey: ['urls'] });
    toast.success('URL shortened successfully!');
  }
});

// Analytics query with polling
const { data: analytics } = useQuery({
  queryKey: ['analytics', shortCode],
  queryFn: () => fetchAnalytics(shortCode),
  refetchInterval: 30000 // Poll every 30 seconds
});

```

**Global State (Context API):**

```typescript
// User context
const UserContext = createContext<{
  user: User | null;
  setUser: (user: User | null) => void;
}>({ user: null, setUser: () => {} });

// Theme context
const ThemeContext = createContext<{
  theme: 'light' | 'dark';
  toggleTheme: () => void;
}>({ theme: 'light', toggleTheme: () => {} });

```

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

### Performance Optimizations (React 19)

- **Code splitting** with React.lazy() and Suspense (React 19 improves Suspense)
- **Memoization** with useMemo() and useCallback()
- **useDeferredValue()** for deferring non-urgent updates (React 19)
- **useTransition()** for marking non-urgent state updates (React 19)
- **Virtual scrolling** for long lists (react-window, react-virtuoso)
- **Image optimization** and lazy loading with native loading="lazy"
- **Debouncing and throttling** for user inputs
- **React.memo** for preventing unnecessary re-renders
- **useOptimistic()** for instant UI feedback (React 19)

### UI/UX Enhancements

- **Toast notifications** for user feedback (react-hot-toast)
- **Loading states** and skeleton screens
- **Error boundaries** for error handling
- **Responsive design** for mobile and desktop
- **Accessibility features** (ARIA labels, keyboard navigation, focus management)
- **Animations** with Framer Motion or CSS transitions

### Code Examples

**Custom Hook Example (React 19):**

```typescript
import { useOptimistic, useTransition } from 'react';

function useShortenURL() {
  const [isPending, startTransition] = useTransition();
  const queryClient = useQueryClient();

  return useMutation({
    mutationFn: (url: string) => shortenUrl(url),
    onSuccess: () => {
      startTransition(() => {
        queryClient.invalidateQueries({ queryKey: ["urls"] });
      });
    }
  });
}

```

**Component with React Query (React 19):**

```typescript
function URLShortenerForm() {
  const { mutate, isPending } = useShortenURL();
  const [url, setUrl] = useState("");
  const [isPendingTransition, startTransition] = useTransition();

  const handleSubmit = async (e: FormEvent) => {
    e.preventDefault();
    startTransition(() => {
      mutate(url);
    });
  };

  return <form onSubmit={handleSubmit}>...</form>;
}

```

**URL Shortener Specific Implementations:**

**Custom Hook: useShortenURL (React 19 with useOptimistic)**

```typescript
import { useOptimistic } from 'react';

function useShortenURL() {
  const queryClient = useQueryClient();
  const { data: urls = [] } = useQuery({
    queryKey: ['urls'],
    queryFn: fetchUserUrls
  });

  const [optimisticUrls, addOptimisticUrl] = useOptimistic(
    urls,
    (state, newUrl: ShortUrl) => [...state, newUrl]
  );

  return useMutation({
    mutationFn: async (data: CreateShortUrlRequest) => {
      const response = await fetch('/api/v1/shorten', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify(data)
      });
      if (!response.ok) throw new Error('Failed to shorten URL');
      return response.json();
    },
    onMutate: async (newData) => {
      await queryClient.cancelQueries({ queryKey: ['urls'] });
      const optimisticUrl: ShortUrl = {
        shortCode: newData.customAlias || 'temp',
        originalUrl: newData.url,
        shortUrl: `https://short.ly/${newData.customAlias || 'temp'}`,
        createdAt: new Date().toISOString()
      };
      addOptimisticUrl(optimisticUrl);
    },
    onSuccess: (data) => {
      queryClient.invalidateQueries(['urls']);
      queryClient.setQueryData(['url', data.data.shortCode], data.data);
    },
    onError: (error) => {
      queryClient.invalidateQueries(['urls']);
      toast.error('Failed to shorten URL. Please try again.');
    }
  });
}

```

**Custom Hook: useAliasCheck**

```typescript
function useAliasCheck(alias: string) {
  return useQuery({
    queryKey: ['alias-check', alias],
    queryFn: () => checkAliasAvailability(alias),
    enabled: alias.length >= 3 && /^[a-zA-Z0-9_-]+$/.test(alias),
    staleTime: Infinity,
    retry: false
  });
}

```

**Service Function: URL Validation**

```typescript
function validateUrl(url: string): { isValid: boolean; error?: string } {
  try {
    const urlObj = new URL(url);
    if (!['http:', 'https:'].includes(urlObj.protocol)) {
      return { isValid: false, error: 'URL must start with http:// or https://' };
    }
    return { isValid: true };
  } catch {
    return { isValid: false, error: 'Invalid URL format' };
  }
}

```

**Service Function: Alias Validation**

```typescript
function validateAlias(alias: string): { isValid: boolean; error?: string } {
  if (alias.length < 3) {
    return { isValid: false, error: 'Alias must be at least 3 characters' };
  }
  if (alias.length > 20) {
    return { isValid: false, error: 'Alias must be less than 20 characters' };
  }
  if (!/^[a-zA-Z0-9_-]+$/.test(alias)) {
    return { isValid: false, error: 'Alias can only contain letters, numbers, hyphens, and underscores' };
  }
  return { isValid: true };
}

```

**Copy to Clipboard Implementation (React 19 with useTransition)**

```typescript
import { useTransition } from 'react';

function useCopyToClipboard() {
  const [copied, setCopied] = useState(false);
  const [isPending, startTransition] = useTransition();

  const copy = async (text: string) => {
    startTransition(async () => {
      try {
        await navigator.clipboard.writeText(text);
        setCopied(true);
        toast.success('Copied to clipboard!');
        setTimeout(() => setCopied(false), 2000);
      } catch (err) {
        toast.error('Failed to copy');
      }
    });
  };

  return { copy, copied, isPending };
}

```

**QR Code Generation (React 19)**

```typescript
import { useTransition, useDeferredValue } from 'react';
import QRCode from 'qrcode.react';

function QRCodeModal({ url, isOpen, onClose }: { url: string; isOpen: boolean; onClose: () => void }) {
  const [isPending, startTransition] = useTransition();
  const deferredUrl = useDeferredValue(url); // Defer QR code generation for performance

  const downloadQR = () => {
    startTransition(() => {
      const canvas = document.getElementById('qrcode') as HTMLCanvasElement;
      const dataUrl = canvas.toDataURL();
      const link = document.createElement('a');
      link.download = 'qrcode.png';
      link.href = dataUrl;
      link.click();
    });
  };

  return (
    <Modal isOpen={isOpen} onClose={onClose}>
      {isPending && <LoadingSpinner />}
      <QRCode id="qrcode" value={deferredUrl} size={256} />
      <Button onClick={downloadQR} disabled={isPending}>
        {isPending ? 'Downloading...' : 'Download QR Code'}
      </Button>
    </Modal>
  );
}

```

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
- Example: Test URL shortening flow from start to finish

**URL Shortener Specific Tests:**

**Component Test: URLShortenerForm**

```typescript
test('validates URL before submission', async () => {
  render(<URLShortenerForm />);
  const input = screen.getByPlaceholderText('Enter URL');
  fireEvent.change(input, { target: { value: 'invalid-url' } });
  fireEvent.submit(screen.getByRole('form'));
  expect(await screen.findByText('Invalid URL format')).toBeInTheDocument();
});

test('submits valid URL', async () => {
  const mockMutate = jest.fn();
  render(<URLShortenerForm />);
  fireEvent.change(screen.getByPlaceholderText('Enter URL'), {
    target: { value: 'https://example.com' }
  });
  fireEvent.submit(screen.getByRole('form'));
  expect(mockMutate).toHaveBeenCalledWith({ url: 'https://example.com' });
});

```

**Integration Test: URL Shortening Flow**

```typescript
test('complete URL shortening flow', async () => {
  render(<App />);
  // Enter URL
  fireEvent.change(screen.getByPlaceholderText('Enter URL'), {
    target: { value: 'https://example.com' }
  });
  // Submit
  fireEvent.click(screen.getByText('Shorten'));
  // Wait for response
  await waitFor(() => {
    expect(screen.getByText(/short\.ly/)).toBeInTheDocument();
  });
  // Copy button appears
  expect(screen.getByText('Copy')).toBeInTheDocument();
});

```

**E2E Test: Complete User Journey**

```typescript
test('user can shorten URL and view analytics', async ({ page }) => {
  await page.goto('/');
  await page.fill('input[placeholder="Enter URL"]', 'https://example.com');
  await page.click('button:has-text("Shorten")');
  await page.waitForSelector('text=/short\.ly/');
  await page.click('button:has-text("View Analytics")');
  await expect(page.locator('text=Click Count')).toBeVisible();
});

```

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

**Alias Format Validation Algorithm:**

```javascript
function isValidAlias(alias) {
  // Must be 3-20 characters
  if (alias.length < 3 || alias.length > 20) return false;
  // Only alphanumeric, hyphens, underscores
  return /^[a-zA-Z0-9_-]+$/.test(alias);
}

```

**URL Expiration Check Algorithm:**

```javascript
function isUrlExpired(expiresAt) {
  if (!expiresAt) return false;
  return new Date(expiresAt) < new Date();
}

function getExpirationStatus(expiresAt) {
  if (!expiresAt) return 'never';
  const daysUntilExpiry = Math.ceil(
    (new Date(expiresAt) - new Date()) / (1000 * 60 * 60 * 24)
  );
  if (daysUntilExpiry < 0) return 'expired';
  if (daysUntilExpiry < 7) return 'soon';
  return 'active';
}

```

**Copy to Clipboard Algorithm:**

```javascript
async function copyToClipboard(text) {
  if (navigator.clipboard && window.isSecureContext) {
    await navigator.clipboard.writeText(text);
  } else {
    // Fallback for older browsers
    const textArea = document.createElement('textarea');
    textArea.value = text;
    textArea.style.position = 'fixed';
    document.body.appendChild(textArea);
    textArea.select();
    document.execCommand('copy');
    document.body.removeChild(textArea);
  }
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

**URL Shortener Specific Security:**

**Phishing Prevention:**

- Display original URL prominently before redirect
- Show warning for suspicious domains
- Validate URL against known phishing databases
- Allow users to report malicious URLs

**Custom Alias Security:**

- Prevent reserved aliases (admin, api, www, etc.)
- Rate limit alias creation attempts
- Validate alias format server-side (client-side is not enough)
- Prevent SQL injection and XSS in alias display

**Input Sanitization:**

```typescript
function sanitizeUrl(url: string): string {
  // Remove any script tags or event handlers
  const div = document.createElement('div');
  div.textContent = url;
  return div.textContent || '';
}

function sanitizeAlias(alias: string): string {
  // Only allow safe characters
  return alias.replace(/[^a-zA-Z0-9_-]/g, '');
}

```

**Rate Limiting Implementation:**

```typescript
let requestCount = 0;
let resetTime = Date.now() + 60000; // 1 minute

function checkRateLimit(): boolean {
  if (Date.now() > resetTime) {
    requestCount = 0;
    resetTime = Date.now() + 60000;
  }
  if (requestCount >= 10) {
    toast.error('Rate limit exceeded. Please wait a moment.');
    return false;
  }
  requestCount++;
  return true;
}

```

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

**URL Shortener Deployment Configuration:**

**Environment Variables:**

```

bash
VITE_API_BASE_URL=https://api.short.ly
VITE_APP_URL=https://short.ly
VITE_ENABLE_ANALYTICS=true
VITE_MAX_URL_LENGTH=2048

```

**Build Configuration (vite.config.ts):**

```typescript
export default defineConfig({
  build: {
    rollupOptions: {
      output: {
        manualChunks: {
          'react-vendor': ['react', 'react-dom', 'react-router-dom'],
          'query-vendor': ['@tanstack/react-query'],
          'chart-vendor': ['recharts']
        }
      }
    }
  }
});

```

**CDN Configuration:**

- Static assets cached for 1 year
- HTML files cached for 5 minutes
- Cache busting via query parameters for updates
- Gzip/Brotli compression enabled

**Monitoring Setup:**

- Track URL shortening success rate
- Monitor API response times
- Alert on error rate spikes (> 5%)
- Track user engagement metrics (clicks, shares)

# 11) Interview Answers (Frontend Focus)

### Q: How would you handle state management for this system?

**Answer (STAR Method):**

**Situation:** In a URL shortening system, we need to manage both client-side UI state and server-side data efficiently.

**Action:**

- Use React Query for server state (URL data, analytics) - handles caching, refetching, and synchronization
- Use `useOptimistic()` (React 19) for instant UI feedback on mutations
- Use `useActionState()` (React 19) for form handling with built-in pending states
- Use `useTransition()` (React 19) for non-urgent updates
- Use `useDeferredValue()` (React 19) for deferring expensive computations
- Use Context API for global client state (user authentication, theme preferences)

**Result:** Reduced API calls through caching, improved performance, better user experience with instant feedback.

**Takeaway:** Separating client and server state management leads to cleaner code and better performance.

### Q: How would you handle real-time analytics updates?

**Answer (STAR Method):**

**Situation:** Users need to see analytics data update in real-time without manual refresh, especially for active URLs with high click rates.

**Action:**

- Use React Query's `refetchInterval` for polling analytics every 30 seconds
- Use `useOptimistic()` (React 19) for instant UI updates before server confirmation
- Use `useTransition()` (React 19) to mark analytics updates as non-urgent
- Use `useSuspenseQuery()` (React 19) for better loading states
- Implement WebSocket connection for truly real-time updates (optional enhancement)
- Implement smart polling: only poll active URLs, pause polling when tab is inactive
- Cache analytics data with appropriate stale time to reduce API calls

**Result:** Users see analytics updates automatically, improving engagement. Reduced server load through intelligent polling strategy.

**Takeaway:** Balance between real-time updates and performance - polling is simpler than WebSockets for most use cases.

### Q: How would you optimize performance for displaying thousands of URLs?

**Answer (STAR Method):**

**Situation:** Users with many shortened URLs need to browse their list efficiently without performance degradation.

**Action:**

- Implement virtual scrolling using react-window or react-virtuoso
- Use pagination with React Query's infinite query
- Use `useDeferredValue()` (React 19) for search input to defer filtering
- Use `useTransition()` (React 19) for non-urgent list updates
- Implement code splitting for URLList component with Suspense (React 19)
- Use React.memo for URLItem components to prevent unnecessary re-renders
- Implement debounced search and filtering
- Lazy load images and QR codes only when visible

**Result:** Smooth scrolling even with 10,000+ URLs, reduced initial load time by 60%, improved user experience.

**Takeaway:** Virtual scrolling is essential for large lists - rendering only visible items dramatically improves performance.

### Q: How would you handle URL expiration on the frontend?

**Answer (STAR Method):**

**Situation:** URLs can expire at different times, and users need clear visual feedback about expiration status.

**Action:**

- Store expiration timestamp in URL data model
- Create utility function to check expiration status (expired, expiring soon, active)
- Display visual indicators: red badge for expired, yellow for expiring soon (< 7 days)
- Disable copy functionality for expired URLs
- Show countdown timer for URLs expiring soon
- Implement background check using setInterval for active pages

**Result:** Users always know URL status, prevented confusion from expired links, improved user trust.

**Takeaway:** Proactive expiration handling improves UX - users appreciate transparency about link status.
