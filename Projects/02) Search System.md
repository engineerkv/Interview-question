# 1) Problem Statement

Design and implement a full-text search system that addresses the following challenges:

- **Core Functionality**: Enable fast and relevant search across billions of documents, support full-text search, autocomplete, search suggestions, and faceted search with filters
- **Scale Requirements**: Handle 1B+ documents, 10M+ queries per day, millions of concurrent search requests, and growing document volumes
- **Performance**: Search latency < 100ms, fast indexing of new documents, efficient query processing, real-time search suggestions
- **Search Features**: Full-text search, autocomplete and suggestions, relevance ranking, faceted search with filters, search analytics
- **Indexing**: Efficient document indexing, handle document updates and deletions, maintain index consistency, support real-time indexing
- **Query Processing**: Support complex search queries, handle query parsing and optimization, provide fast query response times
- **Relevance Ranking**: Rank search results by relevance, support custom ranking algorithms, handle personalized search results
- **Data Consistency**: Maintain search index consistency, handle concurrent document updates, ensure accurate search results

---

# 2) High Level Design (HLD)

## a) Functional Requirements

- Full-text search interface with real-time results
- Autocomplete/suggestions as user types
- Search ranking (relevance) display
- Faceted search (filters) UI
- Search analytics dashboard
- Search history tracking
- Result highlighting and snippets

## b) Non-Functional Requirements

- Search latency < 100ms for results display
- Support 1B+ documents in search interface
- Handle 10M+ queries per day in UI
- Real-time autocomplete suggestions (< 10ms)
- High availability (99.9% uptime)
- Responsive design for mobile and desktop
- Accessible search interface (keyboard navigation, screen readers)

---

## c) MVP (Minimum Viable Product)

### Phase 1: Core Features (Must Have)

- Basic full-text search interface

- Search input with debouncing

- Search results display

- Basic filtering UI

### Phase 2: Enhanced Features

- Autocomplete/suggestions

- Advanced faceted search (multiple filters, range queries)

- Search result highlighting

- Pagination

### Phase 3: Advanced Features

- Personalized search results

- Search analytics and reporting

- Advanced ranking algorithms

- Multi-language search support

---

## d) Technology Choices

### Frontend Framework

- **React 19** - Latest React version with useOptimistic, useActionState, useTransition, useDeferredValue, and use() hook
- **TypeScript** - Type safety and better developer experience

### State Management

- **React Query (TanStack Query)** - Server state management for search results, autocomplete suggestions

- **Redux Toolkit** - Client state management for UI state (selected filters, search query, preferences)

- **Context API** - App-wide configuration (theme, user preferences)

### UI/UX Libraries

- **React Router** - Client-side routing and navigation

- **Debounce libraries** - For search input debouncing (useDeferredValue, useTransition from React 19)

### Build Tools

- **Vite** - Fast build tool and development server

### Testing

- **React Testing Library** - Component testing

- **Vitest** - Unit testing framework

- **Playwright** - E2E testing for search flows

### Deployment

- **Vercel/Netlify** - Static site hosting with CDN

- **AWS S3 + CloudFront** - Alternative deployment with custom CDN configuration

### Additional Libraries

- **Virtual Scrolling** - @tanstack/react-virtual for large result lists
- **Chart Libraries** - Recharts for search analytics visualization

**Trade-offs:**

- **React Query vs SWR**: React Query provides better caching and mutation handling for search, but SWR is lighter - choose React Query for complex search operations with filters
- **Redux Toolkit vs Zustand**: Redux Toolkit offers better DevTools for debugging search state, but Zustand is simpler - choose Redux Toolkit for complex filter management
- **Virtual Scrolling**: Essential for large result lists (1000+ items), but adds complexity - use when result lists exceed 100 items

---

## e) Architecture Overview

The frontend follows a layered architecture optimized for search operations with real-time autocomplete and filtering.

**Component Structure:**

```

Frontend Application
├── Presentation Layer
│   ├── UI Components (SearchBar, SearchResultItem, FilterButton, Pagination, LoadingSpinner)
│   ├── Feature Components (SearchBar, SearchResultsList, FilterSidebar, AutocompleteDropdown, SearchHistory)
│   └── Layout Components (Header, Footer, Navigation, MainLayout, SearchPageLayout)
├── Business/Controller Layer
│   ├── Business Logic (Search query validation, query normalization, result formatting, highlight generation)
│   ├── Custom Hooks (useSearch, useAutocomplete, useSearchFilters, useSearchHistory)
│   └── Service Functions (Query building, result highlighting, filter parsing)
├── State Management
│   ├── Client State
│   │   ├── Local State (useState) - Component-specific UI state
│   │   ├── Global State (Redux Toolkit) - Search history, filter preferences, recent searches
│   │   └── Context API - User authentication, theme preferences, app-wide search settings
│   └── Server State
│       ├── React Query (useQuery/useMutation) - Search results caching, autocomplete suggestions, refetching
│       └── Service Worker - Offline caching for search results
├── API Integration
│   ├── API Client (Axios with interceptors for auth, error handling, retry logic)
│   ├── API Services (searchService, autocompleteService, analyticsService)
│   └── Request/Response Transformation (Query building, result normalization, error handling)
└── Routing
    ├── Public Routes (Search, Results)
    ├── Protected Routes (Search History, Analytics)
    └── Route Guards (Authentication and authorization checks)

```

**Frontend Deployment:**

- **Build**: Production bundle with code splitting and lazy loading using Webpack/Vite
- **CDN**: Static assets served from CloudFront/Cloudflare edge locations for fast global delivery
- **Caching**: Aggressive caching for static assets, cache-busting for updates
- **Environment**: Environment variables for API endpoints and feature flags

**Key Frontend Components:**

- **React 19 Application**:
  - Single-page application with client-side routing
  - Component-based architecture for reusability
  - React Query with React 19 hooks (useOptimistic, useTransition, useDeferredValue)
  - Real-time autocomplete with useDeferredValue for performance
  - Responsive design for mobile and desktop
  - Modern React 19 features for better performance and UX

- **CDN/Edge**:
  - Global distribution of static assets
  - Edge caching for improved performance
  - DDoS protection and rate limiting at edge

**Trade-offs:**

- **Layered Architecture**: Provides clear separation of concerns and maintainability, but can add complexity for simple searches - works great for complex search systems with filters and analytics
- **Business/Controller Layer**: Centralizes search logic and makes it testable, but requires careful design to avoid over-engineering - essential for complex query building and result processing
- **State Management Separation**: Client and server state separation improves performance and caching, but requires understanding when to use each - React Query for search results, Redux for filter state

---

## f) App Flow

### Complete System Flow (Frontend Perspective)

**Primary User Flow - Search:**

1. **User lands on search page** → React Router renders SearchPage component
2. **User types query** → SearchInput component captures input, validates in real-time
3. **Debounced input** → useDeferredValue (React 19) defers search API call by 300ms
4. **Autocomplete triggers** → React Query useQuery fetches suggestions if query length >= 2
5. **User selects result or submits** → SearchResults component renders with React Query data
6. **Loading state** → Skeleton screens displayed while fetching results
7. **Results display** → SearchResultItem components render with highlighted text
8. **User applies filters** → FilterSidebar updates URL params, triggers refetch

**Component Interaction Flow:**

```

User Types → SearchInput (local state with useDeferredValue)
            ↓
Debounced → useSearch hook (React Query useQuery)
            ↓
API Call → searchService (business logic)
            ↓
Response → React Query cache update
            ↓
Re-render → SearchResultsList (receives cached data)

```

**State Update Flow:**

1. **Local State** → SearchInput uses useState for input value
2. **Deferred State** → useDeferredValue (React 19) defers expensive search operations
3. **Server State** → React Query manages search results, caching, refetching
4. **Global State** → Redux Toolkit manages filter state, search history
5. **Component Re-render** → React updates UI based on state changes

**Error Handling Flow:**

1. **API Error** → React Query query returns error
2. **Error Boundary** → Catches component errors, shows fallback UI
3. **User Feedback** → Toast notification displays error message
4. **Retry Logic** → User can retry failed searches

**Autocomplete Flow:**

1. **User types** → SearchInput component captures keystrokes
2. **Debounce** → useDeferredValue defers API call by 300ms
3. **API request** → React Query useQuery fetches suggestions
4. **Display suggestions** → AutocompleteDropdown renders matching queries
5. **Keyboard navigation** → Arrow keys navigate, Enter selects
6. **User selects** → Navigate to search results or update input

**Faceted Search Flow:**

1. **User applies filter** → FilterSidebar updates filter state
2. **URL update** → Query params updated via React Router
3. **Refetch results** → React Query refetches with new filters
4. **Update UI** → SearchResultsList re-renders with filtered data
5. **Clear filters** → Reset URL params, refetch all results

**Search History Flow:**

1. **User performs search** → Search query saved to Redux store
2. **History display** → SearchHistory component shows recent searches
3. **User clicks history item** → Pre-fills search input, triggers search
4. **Clear history** → Removes all history from Redux store

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
│   ├── SearchPage
│   │   ├── SearchBar
│   │   │   ├── SearchInput
│   │   │   ├── AutocompleteDropdown
│   │   │   └── SearchButton
│   │   ├── FilterSidebar
│   │   │   ├── CategoryFilter
│   │   │   ├── PriceFilter
│   │   │   ├── RatingFilter
│   │   │   └── ClearFiltersButton
│   │   └── SearchResultsList
│   │       ├── SearchResultItem
│   │       │   ├── ResultTitle
│   │       │   ├── ResultSnippet
│   │       │   └── ResultMetadata
│   │       └── Pagination
│   ├── SearchHistoryPage
│   │   └── SearchHistoryList
│   └── AnalyticsPage
│       ├── SearchAnalyticsDashboard
│       └── SearchTrendsChart
└── SharedComponents
    ├── Button
    ├── Input
    ├── Card
    ├── Toast
    ├── LoadingSpinner
    └── HighlightedText

```

**Key React Components:**

**1. SearchBar Component:**

- Handles search input with debouncing
- Manages autocomplete state with useState
- Uses React Query useQuery for suggestions
- Implements keyboard navigation (arrow keys, enter, escape)
- Uses useDeferredValue (React 19) for performance

**2. SearchResultsList Component:**

- Displays search results with virtual scrolling
- Fetches results with React Query useSuspenseQuery (React 19)
- Handles pagination and infinite scroll
- Implements result highlighting
- Uses useTransition (React 19) for non-urgent updates

**3. FilterSidebar Component:**

- Displays available filters (category, price, rating)
- Manages filter state with Redux Toolkit
- Updates URL query parameters
- Handles multi-select and range filters

**4. AutocompleteDropdown Component:**

- Shows search suggestions
- Handles keyboard navigation
- Highlights matching text
- Manages selection state

**5. SearchResultItem Component:**

- Displays individual search result
- Highlights search terms in title and snippet
- Shows result metadata (date, category, rating)
- Handles click to navigate to detail page

**6. SearchHistoryList Component:**

- Displays recent searches from Redux store
- Allows quick re-search
- Provides clear history functionality

**Component Communication:**

- **Props** → Parent to child data flow
- **Callbacks** → Child to parent communication
- **Context API** → Shared state across components (theme, user)
- **React Query** → Server state management (search results, suggestions)
- **Redux Toolkit** → Global client state (filters, search history)

# 4) Data Models

### TypeScript Interfaces

```typescript
interface SearchQuery {
  query: string;
  filters: Filter[];
  sortBy: "relevance" | "date" | "price" | "rating";
  page: number;
  limit: number;
}

interface Filter {
  type: "category" | "price" | "rating" | "date";
  value: string | number | [number, number];
  label: string;
}

interface SearchResult {
  id: string;
  title: string;
  snippet: string;
  url: string;
  category: string;
  rating?: number;
  price?: number;
  date?: string;
  highlights?: string[];
}

interface SearchResponse {
  success: boolean;
  data: {
    results: SearchResult[];
    total: number;
    page: number;
    limit: number;
    facets: Facet[];
  };
}

interface Facet {
  name: string;
  values: Array<{ value: string; count: number }>;
}

interface SearchSuggestion {
  text: string;
  type: "query" | "product" | "category";
  count?: number;
}

interface SearchHistoryItem {
  query: string;
  timestamp: string;
  resultCount: number;
}

interface SearchAnalytics {
  totalSearches: number;
  popularQueries: Array<{ query: string; count: number }>;
  searchTrends: Array<{ date: string; count: number }>;
  averageResultsPerQuery: number;
}

interface FormState {
  query: string;
  filters: Filter[];
  sortBy: string;
  errors: {
    query?: string;
  };
}

```

# 5) API Design

### GET /api/v1/search

- **URL:** `/api/v1/search?q=query&category=electronics&page=1&limit=20&sortBy=relevance`
- **Method:** GET
- **Query Parameters:**
  - `q` (required) - Search query string
  - `category` (optional) - Filter by category
  - `minPrice`, `maxPrice` (optional) - Price range filter
  - `rating` (optional) - Minimum rating filter
  - `page` (default: 1) - Page number
  - `limit` (default: 20) - Results per page
  - `sortBy` (optional) - Sort by relevance, date, price, rating
- **Response:**

  ```json
  {
    "success": true,
    "data": {
      "results": [
        {
          "id": "result_123",
          "title": "Product Title",
          "snippet": "Product description with highlighted text...",
          "url": "https://example.com/product/123",
          "category": "electronics",
          "rating": 4.5,
          "price": 99.99,
          "highlights": ["Product", "description"]
        }
      ],
      "total": 1250,
      "page": 1,
      "limit": 20,
      "facets": [
        {
          "name": "category",
          "values": [
            { "value": "electronics", "count": 450 },
            { "value": "books", "count": 320 }
          ]
        }
      ]
    }
  }
  ```

- **Status Codes:** 200 (Success), 400 (Invalid Query), 500 (Server Error)

### GET /api/v1/autocomplete

- **URL:** `/api/v1/autocomplete?q=query&limit=10`
- **Method:** GET
- **Query Parameters:**
  - `q` (required) - Search query string (min 2 characters)
  - `limit` (default: 10) - Maximum suggestions
- **Response:**

  ```json
  {
    "success": true,
    "data": {
      "suggestions": [
        { "text": "laptop", "type": "query", "count": 1250 },
        { "text": "laptop bag", "type": "query", "count": 320 },
        { "text": "Laptop Computers", "type": "category", "count": 450 }
      ]
    }
  }
  ```

- **Status Codes:** 200 (Success), 400 (Invalid Query)

### GET /api/v1/search/analytics

- **URL:** `/api/v1/search/analytics?startDate=2024-01-01&endDate=2024-01-31`
- **Method:** GET
- **Query Parameters:**
  - `startDate` (optional) - Start date for analytics
  - `endDate` (optional) - End date for analytics
- **Response:**

  ```json
  {
    "success": true,
    "data": {
      "totalSearches": 125000,
      "popularQueries": [
        { "query": "laptop", "count": 12500 },
        { "query": "phone", "count": 9800 }
      ],
      "searchTrends": [
        { "date": "2024-01-15", "count": 4500 },
        { "date": "2024-01-16", "count": 5200 }
      ],
      "averageResultsPerQuery": 125.5
    }
  }
  ```

- **Status Codes:** 200 (Success)

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
    "code": "INVALID_QUERY",
    "message": "Search query must be at least 2 characters",
    "details": "Query 'a' is too short"
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

---

# 7) Low Level Design (LLD)

## ii) State Management

### Client State

**Local State (useState):**

- Component-specific UI state (form inputs, modal visibility, loading states)
- Example: `const [isOpen, setIsOpen] = useState(false);`

**Global State:**

- Redux Toolkit for complex global state (filters, search history)
- Context API for user authentication, theme preferences
- Example: Filter preferences, search history, app configuration

### Server State

**React Query (TanStack Query):**

- `useQuery` for data fetching and caching
- `useMutation` for data mutations (create, update, delete)
- `useSuspenseQuery` (React 19) for better loading states
- Automatic refetching, background updates, optimistic updates
- Example: Search results caching, autocomplete suggestions synchronization

**State Management for Search System:**

**Client State Examples (React 19):**

```typescript
import { useState, useDeferredValue, useTransition } from 'react';

// Search input with deferred value (React 19)
const [query, setQuery] = useState("");
const deferredQuery = useDeferredValue(query); // Defers expensive operations

// Filter state
const [filters, setFilters] = useState<Filter[]>([]);

// UI state with transition (React 19)
const [isPending, startTransition] = useTransition();

```

**Server State with React Query (React 19):**

```typescript
import { use, useTransition } from 'react';
import { useQuery, useSuspenseQuery } from '@tanstack/react-query';

// Fetch search results with Suspense (React 19)
const { data: results } = useSuspenseQuery({
  queryKey: ['search', deferredQuery, filters],
  queryFn: () => searchService(deferredQuery, filters),
  staleTime: 30000 // 30 seconds
});

// Autocomplete query
const { data: suggestions } = useQuery({
  queryKey: ['autocomplete', deferredQuery],
  queryFn: () => fetchAutocomplete(deferredQuery),
  enabled: deferredQuery.length >= 2,
  staleTime: 60000 // 1 minute
});

// Using use() hook for promise handling (React 19)
function SearchResults({ resultsPromise }: { resultsPromise: Promise<SearchResponse> }) {
  const results = use(resultsPromise);
  return <SearchResultsList results={results.data.results} />;
}

```

**Global State (Redux Toolkit):**

```typescript
// Search history slice
const searchHistorySlice = createSlice({
  name: 'searchHistory',
  initialState: [] as SearchHistoryItem[],
  reducers: {
    addSearch: (state, action) => {
      state.unshift(action.payload);
      if (state.length > 50) state.pop();
    },
    clearHistory: (state) => {
      return [];
    }
  }
});

// Filter slice
const filterSlice = createSlice({
  name: 'filters',
  initialState: [] as Filter[],
  reducers: {
    addFilter: (state, action) => {
      state.push(action.payload);
    },
    removeFilter: (state, action) => {
      return state.filter(f => f.type !== action.payload.type);
    },
    clearFilters: () => []
  }
});

```

## iii) Implementation Details

### Business/Controller Layer

**Custom Hooks:**

- Encapsulate business logic and API calls
- Example: `useSearch`, `useAutocomplete`, `useSearchFilters`, `useSearchHistory`
- Handle data transformation and validation

**Service Functions:**

- Pure functions for data processing and validation
- Query normalization, result highlighting, filter parsing
- Reusable across components

### Advanced Component Patterns

**Compound Components:**

- Group related components together (e.g., Filter.Category, Filter.Price)
- Share implicit state between components

**Render Props Pattern:**

- Pass render functions as props for flexible component composition

**Custom Hooks Pattern:**

- Extract reusable logic into custom hooks
- Example: `useSearch`, `useAutocomplete`, `useDebounce`, `useHighlight`

**Higher-Order Components (HOCs):**

- Wrap components with additional functionality
- Example: `withSearch`, `withLoading`

### Performance Optimizations (React 19)

- **Code splitting** with React.lazy() and Suspense (React 19 improves Suspense)
- **Memoization** with useMemo() and useCallback()
- **useDeferredValue()** for deferring non-urgent search operations (React 19)
- **useTransition()** for marking non-urgent state updates (React 19)
- **Virtual scrolling** for long result lists (react-window, react-virtuoso)
- **Image optimization** and lazy loading with native loading="lazy"
- **Debouncing and throttling** for search inputs
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

**Custom Hook: useSearch (React 19)**

```typescript
import { useDeferredValue, useTransition } from 'react';
import { useQuery } from '@tanstack/react-query';

function useSearch(query: string, filters: Filter[]) {
  const deferredQuery = useDeferredValue(query);
  const [isPending, startTransition] = useTransition();

  return useQuery({
    queryKey: ['search', deferredQuery, filters],
    queryFn: () => searchService(deferredQuery, filters),
    enabled: deferredQuery.length >= 2,
    staleTime: 30000
  });
}

```

**Component with React Query (React 19):**

```typescript
function SearchBar() {
  const [query, setQuery] = useState("");
  const deferredQuery = useDeferredValue(query);
  const [isPending, startTransition] = useTransition();
  const { data: suggestions } = useQuery({
    queryKey: ['autocomplete', deferredQuery],
    queryFn: () => fetchAutocomplete(deferredQuery),
    enabled: deferredQuery.length >= 2
  });

  const handleChange = (e: ChangeEvent<HTMLInputElement>) => {
    setQuery(e.target.value);
    startTransition(() => {
      // Non-urgent updates
    });
  };

  return <input value={query} onChange={handleChange} />;
}

```

**Search System Specific Implementations:**

**Custom Hook: useAutocomplete**

```typescript
import { useDeferredValue } from 'react';

function useAutocomplete(query: string) {
  const deferredQuery = useDeferredValue(query);

  return useQuery({
    queryKey: ['autocomplete', deferredQuery],
    queryFn: () => fetchAutocomplete(deferredQuery),
    enabled: deferredQuery.length >= 2,
    staleTime: 60000,
    retry: false
  });
}

```

**Service Function: Query Normalization**

```typescript
function normalizeQuery(query: string): string {
  return query
    .trim()
    .toLowerCase()
    .replace(/\s+/g, ' ')
    .replace(/[^\w\s-]/g, '');
}

```

**Service Function: Text Highlighting**

```typescript
function highlightText(text: string, query: string): string {
  const words = query.toLowerCase().split(/\s+/).filter(w => w.length > 0);
  let highlighted = text;

  words.forEach(word => {
    const regex = new RegExp(`(${word})`, 'gi');
    highlighted = highlighted.replace(regex, '<mark>$1</mark>');
  });

  return highlighted;
}

```

**Debounce Hook (React 19 with useDeferredValue):**

```typescript
import { useDeferredValue } from 'react';

function useDebouncedSearch(query: string, delay: number = 300) {
  const deferredQuery = useDeferredValue(query);
  // useDeferredValue automatically debounces
  return deferredQuery;
}

```

## iv) Testing

### Component Testing

- React Testing Library for component tests
- Test user interactions and component behavior
- Example: Test search input, autocomplete dropdown, filter selection

### Integration Testing

- Test component interactions
- Test API integration with mock data
- Test state management flows

### E2E Testing

- Playwright or Cypress for end-to-end tests
- Test complete user flows
- Example: Test search flow from input to results display

**Search System Specific Tests:**

**Component Test: SearchBar**

```typescript
test('debounces search input', async () => {
  render(<SearchBar />);
  const input = screen.getByPlaceholderText('Search...');
  fireEvent.change(input, { target: { value: 'laptop' } });
  await waitFor(() => {
    expect(screen.getByText(/laptop/i)).toBeInTheDocument();
  }, { timeout: 500 });
});

test('handles keyboard navigation', async () => {
  render(<SearchBar />);
  const input = screen.getByPlaceholderText('Search...');
  fireEvent.change(input, { target: { value: 'laptop' } });
  fireEvent.keyDown(input, { key: 'ArrowDown' });
  expect(screen.getByRole('option', { selected: true })).toBeInTheDocument();
});

```

**Integration Test: Search Flow**

```typescript
test('complete search flow', async () => {
  render(<App />);
  fireEvent.change(screen.getByPlaceholderText('Search...'), {
    target: { value: 'laptop' }
  });
  await waitFor(() => {
    expect(screen.getByText(/results/i)).toBeInTheDocument();
  });
  fireEvent.click(screen.getByText('Electronics'));
  await waitFor(() => {
    expect(screen.getAllByRole('article')).toHaveLength(20);
  });
});

```

**E2E Test: Complete Search Journey**

```typescript
test('user can search and filter results', async ({ page }) => {
  await page.goto('/search');
  await page.fill('input[placeholder="Search..."]', 'laptop');
  await page.waitForSelector('text=/results/i');
  await page.click('text=Electronics');
  await expect(page.locator('article')).toHaveCount(20);
});

```

# 8) Algorithms

### Frontend Algorithms

**Search Query Debouncing Algorithm:**

```javascript
function debounce(func, delay) {
  let timeoutId;
  return (...args) => {
    clearTimeout(timeoutId);
    timeoutId = setTimeout(() => func(...args), delay);
  };
}

```

**Text Highlighting Algorithm:**

```javascript
function highlightText(text, query) {
  const words = query.toLowerCase().split(/\s+/).filter(w => w.length > 0);
  let highlighted = text;

  words.forEach(word => {
    const regex = new RegExp(`(${word})`, 'gi');
    highlighted = highlighted.replace(regex, '<mark>$1</mark>');
  });

  return highlighted;
}

```

**Query Normalization Algorithm:**

```javascript
function normalizeQuery(query) {
  return query
    .trim()
    .toLowerCase()
    .replace(/\s+/g, ' ')
    .replace(/[^\w\s-]/g, '');
}

```

**Filter Parsing Algorithm:**

```javascript
function parseFilters(searchParams) {
  const filters = [];

  // Parse category filters
  const categories = searchParams.getAll('category');
  categories.forEach(cat => {
    filters.push({ type: 'category', value: cat, label: cat });
  });

  // Parse price range
  const minPrice = searchParams.get('minPrice');
  const maxPrice = searchParams.get('maxPrice');
  if (minPrice || maxPrice) {
    filters.push({
      type: 'price',
      value: [parseInt(minPrice) || 0, parseInt(maxPrice) || Infinity],
      label: `$${minPrice || 0} - $${maxPrice || '∞'}`
    });
  }

  return filters;
}

```

**Result Ranking Algorithm (Frontend):**

```javascript
function rankResults(results, query) {
  const queryWords = normalizeQuery(query).split(' ');

  return results.sort((a, b) => {
    // Score based on title match
    const aTitleScore = queryWords.reduce((score, word) => {
      return score + (a.title.toLowerCase().includes(word) ? 10 : 0);
    }, 0);

    const bTitleScore = queryWords.reduce((score, word) => {
      return score + (b.title.toLowerCase().includes(word) ? 10 : 0);
    }, 0);

    // Score based on rating
    const aRatingScore = a.rating || 0;
    const bRatingScore = b.rating || 0;

    return (bTitleScore + bRatingScore) - (aTitleScore + aRatingScore);
  });
}

```

# 9) Security

### Frontend Security

**Input Validation:**

- Client-side validation before search submission
- Sanitize search queries to prevent XSS attacks
- Validate filter parameters
- Limit query length (max 200 characters)

**XSS Prevention:**

- React automatically escapes content
- Use `dangerouslySetInnerHTML` only when necessary with sanitization for highlighted text
- Content Security Policy (CSP) headers
- Sanitize search results before displaying

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

- Debounce search API calls to prevent abuse
- Show user-friendly messages when rate limited
- Implement exponential backoff for retries

**Search System Specific Security:**

**Query Sanitization:**

```typescript
function sanitizeQuery(query: string): string {
  // Remove any script tags or event handlers
  const div = document.createElement('div');
  div.textContent = query;
  return div.textContent || '';
}

function sanitizeHighlightedText(html: string): string {
  // Only allow <mark> tags
  return html.replace(/<(?!\/?mark\b)[^>]*>/gi, '');
}

```

**Filter Validation:**

```typescript
function validateFilter(filter: Filter): boolean {
  if (filter.type === 'price' && Array.isArray(filter.value)) {
    const [min, max] = filter.value;
    return min >= 0 && max >= min && max <= 1000000;
  }
  if (filter.type === 'rating') {
    return typeof filter.value === 'number' && filter.value >= 0 && filter.value <= 5;
  }
  return true;
}

```

**Rate Limiting Implementation:**

```typescript
let searchRequestCount = 0;
let resetTime = Date.now() + 60000; // 1 minute

function checkSearchRateLimit(): boolean {
  if (Date.now() > resetTime) {
    searchRequestCount = 0;
    resetTime = Date.now() + 60000;
  }
  if (searchRequestCount >= 20) {
    toast.error('Too many searches. Please wait a moment.');
    return false;
  }
  searchRequestCount++;
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

**Search System Deployment Configuration:**

**Environment Variables:**

```bash
VITE_SEARCH_API_URL=https://api.search.example.com
VITE_AUTOCOMPLETE_DELAY=300
VITE_MAX_SUGGESTIONS=10
VITE_MAX_QUERY_LENGTH=200
VITE_ENABLE_ANALYTICS=true

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
          'redux-vendor': ['@reduxjs/toolkit'],
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

- Track search success rate
- Monitor API response times
- Alert on error rate spikes (> 5%)
- Track search analytics (popular queries, trends)

# 11) Interview Answers (Frontend Focus)

### Q: How would you handle state management for this system?

**Answer (STAR Method):**

**Situation:** In a search system, we need to manage search queries, results, filters, autocomplete suggestions, and search history efficiently.

**Action:**

- Use React Query for server state (search results, autocomplete suggestions) - handles caching, refetching, and synchronization
- Use `useOptimistic()` (React 19) for instant UI feedback on filter changes
- Use `useDeferredValue()` (React 19) for search input to defer expensive operations
- Use `useTransition()` (React 19) for non-urgent filter updates
- Use Redux Toolkit for global client state (filters, search history)
- Use useState for local component state (input value, modal visibility)
- Use Context API for user authentication, theme preferences

**Result:** Reduced API calls through caching, improved performance with deferred values, better user experience with instant feedback, efficient filter management.

**Takeaway:** Separating client and server state management leads to cleaner code and better performance. React 19's deferred values are perfect for search inputs.

### Q: How would you implement autocomplete search?

**Answer (STAR Method):**

**Situation:** Users need fast, responsive search suggestions as they type, with minimal API calls and smooth UX.

**Action:**

- Use `useDeferredValue()` (React 19) to defer autocomplete API calls
- Implement debounced input (300ms delay) to reduce API calls
- Use React Query for caching suggestions with appropriate stale time
- Add keyboard navigation (arrow keys, enter, escape)
- Show loading states during fetch
- Highlight matching text in suggestions
- Implement proper error handling

**Result:** Reduced API calls by 70%, improved performance, better UX with instant feedback, smooth keyboard navigation.

**Takeaway:** Debouncing with React 19's useDeferredValue is essential for autocomplete performance - it defers expensive operations while keeping UI responsive.

### Q: How would you optimize performance for displaying thousands of search results?

**Answer (STAR Method):**

**Situation:** Users need to browse search results efficiently without performance degradation, even with 10,000+ results.

**Action:**

- Implement virtual scrolling using react-window or react-virtuoso
- Use `useDeferredValue()` (React 19) for search input to defer filtering
- Use `useTransition()` (React 19) for non-urgent result list updates
- Use pagination with React Query's infinite query
- Implement code splitting for SearchResultsList component with Suspense (React 19)
- Use React.memo for SearchResultItem components to prevent unnecessary re-renders
- Implement debounced search and filtering
- Lazy load images only when visible

**Result:** Smooth scrolling even with 10,000+ results, reduced initial load time by 60%, improved user experience, no performance degradation.

**Takeaway:** Virtual scrolling is essential for large result lists - rendering only visible items dramatically improves performance. React 19's deferred values help defer expensive operations.

### Q: How would you handle real-time search suggestions?

**Answer (STAR Method):**

**Situation:** Users need to see search suggestions update in real-time as they type, with minimal latency and API calls.

**Action:**

- Use `useDeferredValue()` (React 19) for search input to defer API calls
- Use React Query's `refetchInterval` for active search sessions (optional)
- Implement smart caching: cache suggestions with appropriate stale time
- Use `useTransition()` (React 19) to mark suggestion updates as non-urgent
- Implement request cancellation for outdated queries
- Show loading states with skeleton screens

**Result:** Users see suggestions update smoothly, reduced server load through intelligent caching, improved engagement.

**Takeaway:** Balance between real-time updates and performance - React 19's deferred values help defer expensive operations while keeping UI responsive.

**Purpose:** Debounce search input to reduce API calls while user is typing.

**Implementation:**

```typescript
function debounce<T extends (...args: any[]) => any>(
  func: T,
  wait: number
): (...args: Parameters<T>) => void {
  let timeout: NodeJS.Timeout | null = null;

  return function executedFunction(...args: Parameters<T>) {
    const later = () => {
      timeout = null;
      func(...args);
    };

    if (timeout) clearTimeout(timeout);
    timeout = setTimeout(later, wait);
  };
}

// Usage with React 19 useDeferredValue
const SearchBar: React.FC = () => {
  const [query, setQuery] = useState('');
  const deferredQuery = useDeferredValue(query);

  useEffect(() => {
    if (deferredQuery.length >= 2) {
      fetchAutocomplete(deferredQuery);
    }
  }, [deferredQuery]);
};

```

## Text Highlighting Algorithm (Frontend)

**Purpose:** Highlight search terms in search results for better visibility.

**Implementation:**

```typescript
function highlightText(text: string, query: string): string {
  const words = query.toLowerCase().split(/\s+/);
  let highlighted = text;

  words.forEach(word => {
    const regex = new RegExp(`(${word})`, 'gi');
    highlighted = highlighted.replace(regex, '<mark>$1</mark>');
  });

  return highlighted;
}

```

## Query Normalization (Frontend)

**Purpose:** Normalize search queries for consistent searching.

**Implementation:**

```typescript
function normalizeQuery(query: string): string {
  return query
    .trim()
    .toLowerCase()
    .replace(/\s+/g, ' ')
    .replace(/[^\w\s-]/g, '');
}

```

---
