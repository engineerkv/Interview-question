# Search System

---

## 📍 Navigation

<div align="center">

[Home: README](README.md) • [← Previous: URL Shortener](01%29%20URL%20Shortener.md) • [Next: File Storage System →](03%29%20File%20Storage%20System.md)

[📋 Cheatsheet](Projects%20Interview%20Cheatsheet.md)

</div>

---

## Overview

Design a full-text search system that enables fast and relevant search across billions of documents. Users can search, filter, and get real-time autocomplete suggestions.

---

## 1) Requirements

### Functional Requirements

**Core Features:**
- Full-text search across documents
- Real-time autocomplete and search suggestions
- Faceted search with filters (category, price, rating, date)
- Search result ranking by relevance
- Search result highlighting (highlight matching terms)
- Search history tracking
- Search analytics dashboard

**User Features:**
- Responsive search interface
- Keyboard navigation (arrow keys, Enter)
- Search suggestions dropdown
- Filter sidebar with multiple filter types
- Pagination or infinite scroll
- Sort options (relevance, date, price, rating)

### Non-Functional Requirements

**Performance:**
- Search latency: < 100ms
- Autocomplete suggestions: < 10ms
- Support 1B+ documents
- Handle 10M+ queries per day

**Scalability:**
- Horizontal scaling for search load
- Efficient indexing and query processing
- High availability (99.9% uptime)

**User Experience:**
- Responsive design (mobile and desktop)
- Accessible interface (keyboard navigation, screen readers)
- Fast, responsive UI with debouncing

---

## 2) Component Hierarchy

The frontend is a React application optimized for search operations. Here's the structure:

```
App
├── Layout
│   ├── Header
│   │   ├── Logo
│   │   ├── SearchBar (global search)
│   │   └── UserMenu
│   └── MainContent
├── Pages
│   ├── SearchPage
│   │   ├── SearchBar
│   │   │   ├── SearchInput (with debouncing)
│   │   │   ├── AutocompleteDropdown
│   │   │   │   ├── SuggestionItem (query suggestions)
│   │   │   │   └── CategoryItem (category suggestions)
│   │   │   └── SearchButton
│   │   ├── FilterSidebar
│   │   │   ├── CategoryFilter (multi-select)
│   │   │   ├── PriceFilter (range slider)
│   │   │   ├── RatingFilter (star rating)
│   │   │   ├── DateFilter (date range picker)
│   │   │   └── ClearFiltersButton
│   │   └── SearchResultsList
│   │       ├── ResultsHeader (total count, sort options)
│   │       ├── SearchResultItem
│   │       │   ├── ResultTitle (with highlights)
│   │       │   ├── ResultSnippet (with highlights)
│   │       │   ├── ResultMetadata (category, date, rating)
│   │       │   └── ResultActions (view, save)
│   │       └── Pagination (or InfiniteScroll)
│   ├── SearchHistoryPage
│   │   └── SearchHistoryList
│   │       └── HistoryItem (clickable to re-search)
│   └── AnalyticsPage
│       ├── SearchAnalyticsDashboard
│       │   ├── SummaryCards (total searches, popular queries)
│       │   ├── SearchTrendsChart (line chart over time)
│       │   └── PopularQueriesChart (bar chart)
│       └── DateRangeFilter
└── SharedComponents
    ├── Button
    ├── Input
    ├── Card
    ├── Toast
    └── LoadingSpinner
```

### Key Components Explained

**1. SearchBar Component**
- Main search input with debouncing (300ms delay)
- Real-time autocomplete as user types
- Keyboard navigation (arrow keys to navigate, Enter to select)
- Shows search suggestions dropdown
- Uses useDeferredValue (React 19) for performance

**2. AutocompleteDropdown Component**
- Displays search suggestions
- Shows query suggestions and category suggestions
- Highlights matching text in suggestions
- Handles keyboard navigation
- Closes on outside click or Escape key

**3. SearchResultsList Component**
- Displays search results with virtual scrolling
- Highlights search terms in results
- Handles pagination or infinite scroll
- Shows loading skeleton while fetching
- Updates when filters change

**4. FilterSidebar Component**
- Multiple filter types (category, price, rating, date)
- Multi-select for categories
- Range sliders for price and date
- Updates URL query parameters
- Triggers search refetch when filters change

**5. SearchResultItem Component**
- Individual search result card
- Highlights matching terms in title and snippet
- Shows metadata (category, date, rating, price)
- Clickable to view full result

---

## 3) Data Models

Here are the key data structures:

```typescript
// Search query
interface SearchQuery {
  query: string;
  filters: Filter[];
  sortBy: "relevance" | "date" | "price" | "rating";
  page: number;
  limit: number;
}

// Filter
interface Filter {
  type: "category" | "price" | "rating" | "date";
  value: string | number | [number, number];  // Single value or range
  label: string;
}

// Search result
interface SearchResult {
  id: string;
  title: string;
  snippet: string;  // Excerpt with highlighted terms
  url: string;
  category: string;
  rating?: number;
  price?: number;
  date?: string;
  highlights?: string[];  // Terms that matched
}

// Search response
interface SearchResponse {
  success: boolean;
  data: {
    results: SearchResult[];
    total: number;
    page: number;
    limit: number;
    facets: Facet[];  // Available filter options with counts
  };
}

// Facet (for filters)
interface Facet {
  name: string;  // "category", "price", etc.
  values: Array<{
    value: string;
    count: number;  // How many results have this value
  }>;
}

// Search suggestion (for autocomplete)
interface SearchSuggestion {
  text: string;
  type: "query" | "product" | "category";
  count?: number;  // How many results for this query
}

// Search history
interface SearchHistoryItem {
  query: string;
  timestamp: string;
  resultCount: number;
}

// Search analytics
interface SearchAnalytics {
  totalSearches: number;
  popularQueries: Array<{
    query: string;
    count: number;
  }>;
  searchTrends: Array<{
    date: string;
    count: number;
  }>;
  averageResultsPerQuery: number;
}
```

### Data Flow Explanation

**When a user searches:**
1. User types in search input
2. Input is debounced (300ms delay)
3. If query length >= 2, fetch autocomplete suggestions
4. User submits search or selects suggestion
5. Fetch search results with query and filters
6. Display results with highlighted terms
7. Update URL with search params (for shareability)

**When filters are applied:**
1. User selects filter (category, price, etc.)
2. Filter is added to filter state
3. URL query params are updated
4. Search is refetched with new filters
5. Results update with filtered data
6. Facets update to show available filter options

**Autocomplete flow:**
1. User types in search input
2. After 300ms debounce, fetch suggestions
3. Display suggestions dropdown
4. User can navigate with arrow keys
5. User selects suggestion or continues typing
6. If selected, trigger search with that query

---

## 4) API Design

### REST Endpoints

**GET /api/v1/search**
- Perform search query
- Query params: `q` (query), `category`, `minPrice`, `maxPrice`, `rating`, `page`, `limit`, `sortBy`
- Returns: SearchResponse with results, total count, and facets
- Status codes: 200 (Success), 400 (Invalid Query)

**GET /api/v1/autocomplete**
- Get search suggestions
- Query params: `q` (query, min 2 chars), `limit`
- Returns: Array of SearchSuggestion objects
- Status codes: 200 (Success), 400 (Invalid Query)

**GET /api/v1/search/analytics**
- Get search analytics
- Query params: `startDate`, `endDate`
- Returns: SearchAnalytics object
- Status codes: 200 (Success)

### API Request/Response Examples

**Search:**
  ```json
// GET /api/v1/search?q=laptop&category=electronics&page=1&limit=20&sortBy=relevance
// Response
  {
    "success": true,
    "data": {
      "results": [
        {
          "id": "result_123",
        "title": "Gaming Laptop",
        "snippet": "High-performance gaming laptop with RTX graphics...",
          "url": "https://example.com/product/123",
          "category": "electronics",
          "rating": 4.5,
        "price": 1299.99,
        "highlights": ["laptop", "gaming"]
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
          { "value": "computers", "count": 320 }
        ]
      },
      {
        "name": "price",
        "values": [
          { "value": "0-500", "count": 200 },
          { "value": "500-1000", "count": 350 }
          ]
        }
      ]
    }
  }
  ```

**Autocomplete:**
  ```json
// GET /api/v1/autocomplete?q=lapt&limit=10
// Response
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

**Analytics:**
  ```json
// GET /api/v1/search/analytics?startDate=2024-01-01&endDate=2024-01-31
// Response
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

### Error Handling

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

---

## Key Design Decisions

**1. Debouncing for Performance**
- Debounce search input (300ms) to reduce API calls
- Use useDeferredValue (React 19) for better performance
- Only fetch autocomplete after user stops typing

**2. URL State Management**
- Store search query and filters in URL params
- Enables shareable search URLs
- Browser back/forward works correctly
- Deep linking to specific searches

**3. Virtual Scrolling**
- Use virtual scrolling for large result sets
- Only render visible results
- Improves performance with thousands of results

**4. Faceted Search**
- Return facets (available filter options) with search results
- Shows counts for each filter value
- Helps users refine their search

**5. Result Highlighting**
- Highlight matching terms in results
- Makes it easy to see why result matched
- Improves user experience

**6. Caching Strategy**
- Cache search results with React Query
- Cache autocomplete suggestions
- Reduces API calls for repeated queries

---

## Interview Talking Points

**When explaining this system, I'd focus on:**

1. **Requirements First**: Start with core functionality - full-text search, autocomplete, filters, ranking

2. **Component Structure**: Explain the React component hierarchy - search bar, autocomplete dropdown, results list, filter sidebar

3. **Data Models**: Walk through SearchQuery, SearchResult, Filter, Facet - and how they work together

4. **API Design**: Show the REST endpoints - search, autocomplete, analytics - and query parameters

5. **Key Challenges**: 
   - Debouncing for performance (reduce API calls)
   - Real-time autocomplete with low latency
   - Faceted search with dynamic filter counts
   - Result highlighting and relevance ranking
   - Handling large result sets efficiently

**Example explanation flow:**
> "So for a search system, the core requirement is fast, relevant search across billions of documents. The frontend is a React app with a search bar component that debounces input to reduce API calls. As users type, we fetch autocomplete suggestions in real-time. The search results are displayed in a list with highlighted matching terms. We have a filter sidebar for faceted search - users can filter by category, price, rating, etc. The data model includes SearchQuery with the query string and filters, SearchResult with the result data, and Facets which show available filter options with counts. The main API endpoint is GET /search with query parameters for the search query and filters. Key challenges include debouncing for performance, real-time autocomplete, and efficiently handling large result sets with virtual scrolling."

---

## 📍 Navigation

<div align="center">

[Home: README](README.md) • [← Previous: URL Shortener](01%29%20URL%20Shortener.md) • [Next: File Storage System →](03%29%20File%20Storage%20System.md)

[📋 Cheatsheet](Projects%20Interview%20Cheatsheet.md)

</div>

---
