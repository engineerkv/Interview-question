# Search System

> **Project Type:** Full-Stack Web Application (MERN Stack)
> **Scale:** Handle 1B+ documents, 10M+ queries per day, < 100ms search latency
> **Tech Stack:** React.js, Node.js, Express.js, MongoDB, Elasticsearch, Redis

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

## a) Requirements

### i) Functional Requirements

- Full-text search

- Autocomplete/suggestions

- Search ranking (relevance)

- Faceted search (filters)

- Search analytics

### ii) Non-Functional Requirements

- Search latency < 100ms

- Support 1B+ documents

- Handle 10M+ queries per day

---

## b) Scope and Priority

### Phase 1: MVP (Must Have) - Priority 1

- Core functionality

- Basic features

### Phase 2: Enhanced Features - Priority 2

- Additional capabilities

- Performance improvements

### Phase 2: Enhanced Features - Priority 2

- Advanced faceted search (multiple filters, range queries)

- Personalized search results

- Search analytics and reporting

- Advanced ranking algorithms

- Multi-language search support

---

## c) Technology Choices

### Search Engine

- **Elasticsearch** - Full-text search with inverted index

### Database

- **Database** - Store document metadata

### Caching

- **Redis** - Cache popular search queries

### Additional Services

- **Autocomplete Service** - Trie-based suggestions

- **Ranking Service** - Relevance scoring

---

## d) Capacity Estimation

### Throughput Requirements

- **Total Documents**: 1 billion documents
- **Daily Active Users (DAU)**: 100 million users per day
- **Peak Traffic**: 3x average during peak hours (300 million users per day)
- **Search Queries per Day**: 10 million queries
- **Document Updates per Day**: 100 million document updates (new, modified, deleted)
- **Read:Write Ratio**: 100:1 (search queries vs document indexing)

**Calculations:**
- **Average Writes Per Second (WPS)**: 100M document updates / 86,400 seconds ≈ 1,157 WPS
- **Peak WPS**: 1,157 × 3 = 3,471 WPS
- **Average Reads Per Second (RPS)**: 10M queries / 86,400 seconds ≈ 116 RPS
- **Peak RPS**: 116 × 3 = 348 RPS
- **Concurrent Search Queries**: 1 million concurrent search queries

### Storage Estimation

**Storage per Document:**
- Document content: 10 KB average (text content)
- Indexed fields: 5 KB (title, description, tags, metadata)
- **Total per Document**: ~15 KB

**Storage Requirements:**
- **Documents**: 1B documents × 15 KB ≈ 15 TB
- **Elasticsearch Index**: 1B documents × 20 KB (with inverted index) ≈ 20 TB
- **User Data**: 100M users × 5 KB ≈ 500 GB
- **Search Analytics**: 10M queries/day × 1 KB ≈ 10 GB/day ≈ 3.65 TB/year
- **Total Storage**: ~20 TB (Elasticsearch) + 500 GB (users) + 3.65 TB (analytics) ≈ 24.15 TB

### Bandwidth Estimation

- **Average Query Size**: 500 bytes per query
- **Average Response Size**: 50 KB per search result (10 results × 5 KB)
- **Daily Bandwidth**: 10M queries × (500 bytes + 50 KB) = 505 GB/day
- **Peak Bandwidth**: 505 GB × 3 = 1.515 TB/day during peak hours
- **Average Bandwidth**: 505 GB / 86,400 seconds ≈ 5.85 MB/s
- **Peak Bandwidth**: 5.85 MB/s × 3 ≈ 17.55 MB/s

### Caching Estimation

Following the **80-20 rule** where 20% of queries generate 80% of traffic:
- **Cache 20% of popular queries**: 10M × 0.2 = 2M queries
- **Cache memory required**: 2M queries × 50 KB = 100 GB (distributed across Redis cluster)
- **Cache hit ratio**: 80% (only 20% of search queries hit Elasticsearch)
- **Requests hitting Elasticsearch**: 116 × 0.20 ≈ 23 RPS (manageable with Elasticsearch cluster)

### Infrastructure Sizing

- **API Servers**: 500-1,000 instances behind load balancer, each handling 1-2 RPS
- **Elasticsearch Cluster**: 50-100 nodes for indexing and search, with proper sharding
- **Indexing Workers**: 100-200 instances for document indexing
- **Message Queue**: RabbitMQ/Kafka cluster with 20-50 nodes for indexing tasks
- **Database**: MongoDB cluster with 20-50 nodes for document metadata storage
- **Cache Layer**: Redis cluster with 20-50 nodes for high availability and performance
- **Autocomplete Service**: 10-20 instances for search suggestions

---

## e) Architecture Overview

The system follows a full-text search architecture with Elasticsearch, inverted indexing, caching, and distributed search processing. Here's how the complete system works:

### Frontend Architecture

**Frontend Layers:**

1. **Presentation Layer (React Components)**
   - **UI Components**: Reusable components (SearchBar, SearchResult, FilterPanel, AutocompleteDropdown)
   - **Feature Components**: SearchPage, SearchResults, FacetedSearch, SearchAnalytics
   - **Layout Components**: Header, Sidebar, Navigation, MainLayout
   - **Page Components**: SearchPage, ResultsPage, AnalyticsPage

2. **State Management Layer**
   - **Local State (useState)**: Component-specific UI state (search query, selected filters, loading, errors)
   - **Server State (Redux Toolkit)**: Global state for search results, filters, user preferences
   - **API State (React Query)**: Search results caching, refetching, optimistic updates

3. **Search Integration Layer**
   - **Search Bar**: Real-time search input with autocomplete
   - **Query Builder**: Build complex search queries with filters
   - **Result Display**: Display search results with highlighting and pagination

4. **API Integration Layer**
   - **API Client**: Axios instance with interceptors for auth, error handling
   - **Redux Thunks**: Async actions for API operations (search, autocomplete, getSuggestions)
   - **Request/Response Transformation**: Data normalization and error handling

5. **Routing Layer (React Router)**
   - **Route Configuration**: Define routes and protected routes
   - **Navigation**: Programmatic and declarative navigation
   - **Route Guards**: Authentication and authorization checks

6. **Build & Deployment Layer**
   - **Build Process**: Webpack/Vite bundling with code splitting
   - **Static Assets**: Served from CDN (CloudFront/Cloudflare)
   - **Environment Configuration**: Environment-specific API endpoints and configs

**Frontend Request Flow:**

1. **User Interaction** → User types search query or applies filters
2. **State Update** → Redux action dispatched or React Query mutation triggered
3. **API Call** → Axios makes HTTP request to search API
4. **Loading State** → UI shows loading indicator
5. **Response Handling** → Success/error state updates Redux store or React Query cache
6. **UI Update** → Components re-render with search results

### Backend Architecture

**Backend Layers:**

1. **API Gateway/Load Balancer** - Entry point for all HTTP requests
2. **API Server Layer** - Stateless servers handling HTTP requests
3. **Search Service Layer** - Elasticsearch query processing and result ranking
4. **Indexing Layer** - Document indexing workers for Elasticsearch
5. **Autocomplete Service Layer** - Trie-based autocomplete and suggestions
6. **Application Service Layer** - Business logic and orchestration
7. **Cache Layer** - In-memory caching for performance
8. **Database Layer** - Persistent data storage for document metadata
9. **Search Engine Layer** - Elasticsearch cluster for full-text search

### Complete Request Flow

**Search Query Flow:**
1. **Frontend**: User types search query in search bar
2. **API Call**: GET request to search API with query and filters
3. **Cache Check**: Check Redis for cached search results
4. **Elasticsearch Query**: If not cached, query Elasticsearch with search query
5. **Ranking**: Rank results by relevance using BM25/TF-IDF
6. **Response**: Return search results with relevance scores
7. **Cache**: Cache search results in Redis
8. **Frontend**: Display search results with highlighting

**Document Indexing Flow:**
1. **Document Update**: New document created or updated
2. **Message Queue**: Add indexing task to message queue
3. **Indexing Worker**: Worker processes indexing task
4. **Elasticsearch**: Index document in Elasticsearch
5. **Update**: Update document metadata in database
6. **Response**: Confirm indexing completion

**Autocomplete Flow:**
1. **Frontend**: User types in search bar
2. **API Call**: GET request to autocomplete API with partial query
3. **Trie Lookup**: Query Trie data structure for suggestions
4. **Response**: Return top suggestions
5. **Frontend**: Display autocomplete dropdown with suggestions

### Key Components

- **Frontend (React.js)**: Single-page application with search interface, component-based architecture, Redux for state management, real-time autocomplete
- **Load Balancer**: Distributes HTTP traffic across API servers, SSL/TLS termination
- **API Servers**: Stateless design for horizontal scaling, handle search queries, autocomplete requests
- **Search Service**: Elasticsearch query processing, result ranking, relevance scoring
- **Indexing Workers**: Workers for document indexing, handle document updates and deletions
- **Autocomplete Service**: Trie-based autocomplete, provides search suggestions
- **Application Services**: Search Service, Indexing Service, Autocomplete Service, Analytics Service
- **Cache Layer (Redis)**: In-memory cache for popular search queries (20% of traffic), autocomplete suggestions
- **Database (MongoDB)**: Sharded across multiple nodes for horizontal scaling, stores document metadata
- **Search Engine (Elasticsearch)**: Distributed Elasticsearch cluster with inverted indexes, handles full-text search, relevance ranking

---

# 3) Low Level Design (LLD)

---

## Component Architecture

### Service Components

```typescript
class Service {
  async processRequest(data: any) {
    // Implementation details
  }
}

```

---

## Frontend Design

### Component Architecture

Think of the frontend as a tree of React components - each component handles a specific part of the UI, and they work together to create the complete user experience.

**Component Hierarchy:**

```
App
├── Header
│   ├── Logo
│   ├── SearchBar
│   │   ├── SearchInput
│   │   ├── AutocompleteDropdown
│   │   │   └── SuggestionItem
│   │   └── SearchButton
│   └── Navigation
├── MainContent
│   ├── SearchResultsPage
│   │   ├── FilterSidebar
│   │   │   ├── CategoryFilter
│   │   │   ├── DateRangeFilter
│   │   │   ├── TypeFilter
│   │   │   └── ClearFiltersButton
│   │   ├── ResultsHeader
│   │   │   ├── ResultsCount
│   │   │   ├── SortOptions
│   │   │   └── ViewToggle (List/Grid)
│   │   ├── SearchResultsList
│   │   │   └── SearchResultItem
│   │   │       ├── Title (with highlights)
│   │   │       ├── Snippet (with highlights)
│   │   │       ├── Metadata (date, author, category)
│   │   │       └── RelevanceScore
│   │   ├── Pagination
│   │   └── NoResultsState
│   └── SearchHistoryPage
│       ├── RecentSearches
│       └── PopularSearches
└── Footer
```

### Key React Components

**Frontend Implementation:**

```typescript
// Search Bar with Autocomplete Component
const SearchBar: React.FC = () => {
  const [query, setQuery] = useState('');
  const [showSuggestions, setShowSuggestions] = useState(false);
  const { data: suggestions } = useAutocomplete(query);

  const handleSearch = (searchQuery: string) => {
    navigate(`/search?q=${encodeURIComponent(searchQuery)}`);
    setShowSuggestions(false);
  };

  const handleInputChange = (value: string) => {
    setQuery(value);
    setShowSuggestions(value.length > 0);
  };

  return (
    <div className="search-bar">
      <input
        type="text"
        value={query}
        onChange={(e) => handleInputChange(e.target.value)}
        onKeyDown={(e) => {
          if (e.key === 'Enter') {
            handleSearch(query);
          }
        }}
        placeholder="Search..."
      />
      {showSuggestions && suggestions && (
        <AutocompleteDropdown
          suggestions={suggestions}
          onSelect={handleSearch}
        />
      )}
      <button onClick={() => handleSearch(query)}>Search</button>
    </div>
  );
};

// Search Result Item Component
const SearchResultItem: React.FC<{ result: SearchResult }> = ({ result }) => {
  return (
    <div className="search-result-item" onClick={() => navigate(result.url)}>
      <h3 dangerouslySetInnerHTML={{ __html: result.highlightedTitle }} />
      <p dangerouslySetInnerHTML={{ __html: result.highlightedSnippet }} />
      <div className="result-meta">
        <span>{result.url}</span>
        <span>{formatDate(result.date)}</span>
        {result.category && <span>{result.category}</span>}
      </div>
    </div>
  );
};

// Filter Sidebar Component
const FilterSidebar: React.FC<{ filters: SearchFilters; onFilterChange: (filters: SearchFilters) => void }> = ({ 
  filters, 
  onFilterChange 
}) => {
  const handleCategoryChange = (category: string) => {
    onFilterChange({
      ...filters,
      category: filters.category === category ? undefined : category
    });
  };

  return (
    <div className="filter-sidebar">
      <h3>Filters</h3>
      <CategoryFilter
        selected={filters.category}
        onChange={handleCategoryChange}
      />
      <DateRangeFilter
        value={filters.dateRange}
        onChange={(dateRange) => onFilterChange({ ...filters, dateRange })}
      />
      <TypeFilter
        selected={filters.type}
        onChange={(type) => onFilterChange({ ...filters, type })}
      />
    </div>
  );
};
```

### State Management

**State Management Strategy:**

- **Local State (useState)**: Search query, UI state (loading, errors, selected filters, show/hide suggestions)
- **Component State**: Each component manages its own UI state
- **API State**: React Query or SWR for server state (search results, autocomplete suggestions) - caching, refetching
- **Global State (Redux Toolkit)**: Search history, recent searches, user preferences

**Frontend Implementation:**

```typescript
// Using React Query for API state management
import { useQuery, useMutation, useQueryClient } from '@tanstack/react-query';

const useSearch = (query: string, filters?: SearchFilters) => {
  return useQuery({
    queryKey: ['search', query, filters],
    queryFn: async () => {
      const response = await axios.get('/api/v1/search', {
        params: { q: query, ...filters }
      });
      return response.data;
    },
    enabled: query.length > 0,
    staleTime: 5 * 60 * 1000 // Cache for 5 minutes
  });
};

const useAutocomplete = (query: string) => {
  return useQuery({
    queryKey: ['autocomplete', query],
    queryFn: async () => {
      const response = await axios.get('/api/v1/search/autocomplete', {
        params: { q: query }
      });
      return response.data;
    },
    enabled: query.length > 2,
    staleTime: 1 * 60 * 1000 // Cache for 1 minute
  });
};
```

### Component Interactions

**Data Flow:**

1. **Search Input** → User types query, triggers autocomplete suggestions
2. **Search Execution** → User submits search, fetches results via API
3. **Filter Application** → User applies filters, refetches results with filters
4. **Result Selection** → User clicks result, navigates to content
5. **Search History** → Search queries saved for recent searches

**Event Handling:**

- Search input triggers debounced autocomplete API call
- Search submission fetches full search results
- Filter changes refetch results with new filters
- Pagination loads next page of results
- Keyboard navigation for autocomplete suggestions

### UI/UX Considerations

- **Loading States**: Show skeleton loaders for search results, spinners for autocomplete
- **Error Handling**: Display user-friendly error messages with retry options
- **Validation**: Client-side validation for search query length
- **Responsive Design**: Mobile-first layout, collapsible filters on mobile
- **Accessibility**: ARIA labels, keyboard navigation, screen reader support, focus management
- **Performance**: Debounced autocomplete, virtual scrolling for long result lists, result caching

---

## Data Models

### Model Interface

```typescript
interface Model {
  id: string;
  // Model fields
  createdAt: Date;
  updatedAt: Date;
}

```

---

## Data APIs

### GET /api/v1/search

- **URL:** `/api/v1/search?q=query&page=1&limit=20&filters=category:electronics`

- **Method:** GET

- **Query Parameters:**
  - `q`: string (required) - Search query
  - `page`: number (default: 1)
  - `limit`: number (default: 20, max: 100)
  - `filters`: string (optional) - Filter criteria (e.g., "category:electronics,price:0-100")
  - `sort`: string (optional) - Sort order (e.g., "price:asc", "relevance:desc")

- **Response:**
  ```json
  {
    "success": true,
    "data": {
      "results": [
        {
          "id": "product_abc123",
          "title": "Product Name",
          "description": "Product description...",
          "category": "electronics",
          "price": 99.99,
          "score": 0.95
        }
      ],
      "total": 1250,
      "page": 1,
      "limit": 20,
      "totalPages": 63
    }
  }
  ```

- **Status Codes:** 200 (Success), 400 (Invalid Query)

### GET /api/v1/search/autocomplete

- **URL:** `/api/v1/search/autocomplete?q=quer`

- **Method:** GET

- **Query Parameters:**
  - `q`: string (required) - Partial search query
  - `limit`: number (default: 10, max: 20)

- **Response:**
  ```json
  {
    "success": true,
    "data": {
      "suggestions": [
        { "text": "query suggestion 1", "count": 150 },
        { "text": "query suggestion 2", "count": 120 }
      ]
    }
  }
  ```

- **Status Codes:** 200 (Success), 400 (Invalid Query)

### POST /api/v1/search/index

- **URL:** `/api/v1/search/index`

- **Method:** POST

- **Description:** Index a document for search (Admin/Internal)

- **Request Body:**
  ```json
  {
    "id": "product_abc123",
    "title": "Product Name",
    "description": "Product description...",
    "category": "electronics",
    "price": 99.99,
    "tags": ["tag1", "tag2"]
  }
  ```

- **Response:**
  ```json
  {
    "success": true,
    "data": {
      "id": "product_abc123",
      "indexed": true,
      "indexedAt": "2024-01-15T10:30:00Z"
    }
  }
  ```

- **Status Codes:** 201 (Created), 400 (Validation Error)

---

## Backend Implementation Details

### Express.js Server Structure

```

server/
├── routes/
├── controllers/
├── services/
└── models/

```

### Search Service

```typescript
class SearchService {
  async search(query: string, filters: any, page: number, limit: number): Promise<SearchResults> {
    // Build Elasticsearch query
    // Apply filters
    // Execute search
    // Return results
  }

  async autocomplete(partialQuery: string): Promise<string[]> {
    // Get suggestions from Elasticsearch
    // Return autocomplete suggestions
  }

  async indexDocument(document: any): Promise<void> {
    // Index document in Elasticsearch
    // Update index
  }
}

```

---

## Search Index

### Inverted Index

- Word → [Document IDs containing word]

- Example: "python" → [doc1, doc3, doc5]

## Protocols

### REST API Protocol

- **Protocol:** REST (Representational State Transfer)

- **Data Format:** JSON

- **Authentication:** JWT Bearer token

### Additional Protocols

- **WebSocket** - For real-time features (if applicable)

- **Message Queue** - For async processing (if applicable)

---

---

## Implementation Details

### Core Implementation

**Note:** Implementation details are split between frontend (React.js) and backend (Node.js/Express.js). Each section indicates where the code runs.

### Search Query Processing

**Frontend Implementation:** React component handles search input with debouncing and autocomplete
**Backend Implementation:** Express.js service processes search queries using Elasticsearch

- **Strategy:** Elasticsearch-based search with autocomplete - like Google search, provides instant results and suggestions

- **Query Processing:** Full-text search with relevance scoring, filters, and sorting

**Backend (Express.js):**

```typescript
// Backend: services/SearchService.ts
import { Client } from '@elastic/elasticsearch';

const esClient = new Client({ node: process.env.ELASTICSEARCH_URL });

class SearchService {
  async search(query: string, filters: any, page: number = 1, limit: number = 20) {
    const from = (page - 1) * limit;

    // Build Elasticsearch query
    const esQuery = {
      index: 'products',
      body: {
        query: {
          bool: {
            must: [
              {
                multi_match: {
                  query: query,
                  fields: ['title^3', 'description', 'tags'],
                  fuzziness: 'AUTO'
                }
              }
            ],
            filter: this.buildFilters(filters)
          }
        },
        sort: this.buildSort(filters.sort),
        from,
        size: limit
      }
    };

    try {
      const response = await esClient.search(esQuery);

      return {
        results: response.body.hits.hits.map((hit: any) => ({
          id: hit._id,
          ...hit._source,
          score: hit._score
        })),
        total: response.body.hits.total.value,
        page,
        limit,
        totalPages: Math.ceil(response.body.hits.total.value / limit)
      };
    } catch (error) {
      console.error('Elasticsearch error:', error);
      throw new Error('Search failed');
    }
  }

  async autocomplete(partialQuery: string, limit: number = 10) {
    const response = await esClient.search({
      index: 'products',
      body: {
        suggest: {
          autocomplete: {
            prefix: partialQuery,
            completion: {
              field: 'suggest',
              size: limit
            }
          }
        }
      }
    });

    return response.body.suggest.autocomplete[0].options.map((option: any) => ({
      text: option.text,
      count: option._source.count
    }));
  }

  private buildFilters(filters: any) {
    const filterClauses = [];

    if (filters.category) {
      filterClauses.push({ term: { category: filters.category } });
    }

    if (filters.priceRange) {
      filterClauses.push({
        range: {
          price: {
            gte: filters.priceRange.min,
            lte: filters.priceRange.max
          }
        }
      });
    }

    return filterClauses;
  }

  private buildSort(sortParam?: string) {
    if (!sortParam) {
      return [{ _score: 'desc' }]; // Default: relevance
    }

    const [field, order] = sortParam.split(':');
    return [{ [field]: order || 'asc' }];
  }
}

```

**Frontend Implementation:**

```typescript
// React component for search with autocomplete
import { useState, useEffect, useCallback } from 'react';
import { useQuery } from '@tanstack/react-query';
import { debounce } from 'lodash';
import axios from 'axios';

const SearchComponent: React.FC = () => {
  const [query, setQuery] = useState('');
  const [debouncedQuery, setDebouncedQuery] = useState('');

  // Debounce search query
  useEffect(() => {
    const timer = setTimeout(() => {
      setDebouncedQuery(query);
    }, 300);
    return () => clearTimeout(timer);
  }, [query]);

  // Search query
  const { data: searchResults, isLoading } = useQuery({
    queryKey: ['search', debouncedQuery],
    queryFn: () => axios.get('/api/v1/search', { params: { q: debouncedQuery } })
      .then(res => res.data.data),
    enabled: debouncedQuery.length > 0
  });

  // Autocomplete query
  const { data: suggestions } = useQuery({
    queryKey: ['autocomplete', query],
    queryFn: () => axios.get('/api/v1/search/autocomplete', { params: { q: query } })
      .then(res => res.data.data.suggestions),
    enabled: query.length > 2
  });

  return (
    <div className="search-container">
      <input
        type="text"
        value={query}
        onChange={(e) => setQuery(e.target.value)}
        placeholder="Search..."
      />
      {suggestions && suggestions.length > 0 && (
        <div className="autocomplete-dropdown">
          {suggestions.map((suggestion: any) => (
            <div key={suggestion.text} onClick={() => setQuery(suggestion.text)}>
              {suggestion.text}
            </div>
          ))}
        </div>
      )}
      {isLoading && <div>Searching...</div>}
      {searchResults && (
        <div className="search-results">
          {searchResults.results.map((result: any) => (
            <div key={result.id}>{result.title}</div>
          ))}
        </div>
      )}
    </div>
  );
};

```

### Document Indexing

**Frontend Implementation:** React component for admin to index documents
**Backend Implementation:** Express.js service indexes documents in Elasticsearch

- **Strategy:** Async indexing with message queue - like background processing, indexes documents without blocking requests

- **Indexing:** Full-text indexing with analyzers, tokenizers, and mappings

**Backend (Express.js):**

```typescript
// Backend: services/IndexingService.ts
import { Client } from '@elastic/elasticsearch';
import rabbitmq from '../config/rabbitmq';

class IndexingService {
  async indexDocument(document: any) {
    try {
      await esClient.index({
        index: 'products',
        id: document.id,
        body: {
          ...document,
          indexedAt: new Date()
        }
      });

      // Refresh index for immediate searchability
      await esClient.indices.refresh({ index: 'products' });
    } catch (error) {
      console.error('Indexing error:', error);
      throw error;
    }
  }

  async bulkIndex(documents: any[]) {
    const body = documents.flatMap((doc) => [
      { index: { _index: 'products', _id: doc.id } },
      doc
    ]);

    await esClient.bulk({ body });
    await esClient.indices.refresh({ index: 'products' });
  }
}

// Message queue consumer for async indexing
rabbitmq.consume('index-document', async (message) => {
  const document = JSON.parse(message.content.toString());
  await indexingService.indexDocument(document);
});

```

### Error Handling

**Frontend Implementation:** React components handle errors and show user-friendly messages
**Backend Implementation:** Express.js middleware handles errors and returns proper status codes

**Backend (Express.js):**

```typescript
// Backend: middleware/errorHandler.ts
export const errorHandler = (err: Error, req: Request, res: Response, next: NextFunction) => {
  console.error('Search Error:', err);

  if (err.message === 'Invalid query') {
    return res.status(400).json({ error: 'Invalid search query' });
  }

  if (err.message === 'Elasticsearch unavailable') {
    return res.status(503).json({ error: 'Search service temporarily unavailable' });
  }

  if (err.name === 'TimeoutError') {
    return res.status(504).json({ error: 'Search timeout. Please try again.' });
  }

  res.status(500).json({ error: 'Internal server error' });
};

```

**Frontend Implementation:**

```typescript
// React error handling
axios.interceptors.response.use(
  (response) => response,
  (error) => {
    if (error.response?.status === 503) {
      toast.error('Search service unavailable. Please try again later.');
    } else if (error.response?.status === 400) {
      toast.error('Invalid search query. Please check your input.');
    } else {
      toast.error('Search failed. Please try again.');
    }
    return Promise.reject(error);
  }
);

```

**Error Scenarios:**

- **Search Errors:** Handle Elasticsearch failures, query timeouts, index errors - retry with exponential backoff, fallback to database search

- **Indexing Errors:** Handle document indexing failures, mapping errors - queue failed documents, retry indexing

- **Query Errors:** Handle invalid search queries, syntax errors - validate queries, show user-friendly error messages

- **Performance Errors:** Handle slow queries, high load - implement query timeout, rate limiting, query optimization

---

## Testing Strategy

### Frontend Testing (React.js)

**Unit Testing:**

- **Jest + React Testing Library** - Test components, search interface, autocomplete

- **Search Component Testing** - Test search input, results display, filters, pagination

- **Mocking:** Mock API calls, Elasticsearch, search results

**Integration Testing:**

- **Search Flow** - Test complete search process

- **Autocomplete Integration** - Test autocomplete functionality

- **API Integration Tests** - Test API calls with mock server

**E2E Testing:**

- **Cypress / Playwright** - Test search flows

- **Test Scenarios:** Perform search, filter results, view details, autocomplete

### Backend Testing (Node.js/Express.js)

**Unit Testing:**

- **Jest + Supertest** - Test API endpoints, search query processing

- **Elasticsearch Testing** - Test Elasticsearch query construction

- **Mocking:** Mock database, Elasticsearch, Redis

**Integration Testing:**

- **MongoDB Memory Server** - Test database operations

- **Redis Mock** - Test search result caching

- **Elasticsearch Mock** - Test Elasticsearch operations

**Load Testing:**

- **Artillery / k6** - Test search performance under high load

- **Concurrent Searches:** Test performance with multiple simultaneous searches

---

## Deployment & DevOps

### Frontend Deployment

**Build Process:**

- **Production Build:** Optimized bundle with code splitting

- **CDN Deployment:** Deploy static assets to CDN

- **Environment Variables:** `.env.production` for production config

**Deployment Platforms:**

- **Vercel / Netlify** - Automatic deployments

- **AWS S3 + CloudFront** - Static site hosting with CDN

### Backend Deployment

**Server Setup:**

- **PM2:** Process manager with clustering

- **Nginx:** Load balancer and reverse proxy

- **Docker:** Containerized deployment

**Elasticsearch Setup:**

- **Elasticsearch Cluster** - Managed Elasticsearch service or self-hosted

- **Index Management** - Configure indexes and mappings

- **Backup Strategy:** Backup Elasticsearch indexes

**CI/CD Pipeline:**

- **Automated Testing:** Run tests before deployment

- **Zero-Downtime:** Rolling deployment strategy

- **Health Checks:** Verify search endpoints

---

## Environment Configuration

### Environment Variables

**Frontend:**

```env
REACT_APP_API_URL=https://api.example.com
REACT_APP_ENVIRONMENT=production

```

**Backend:**

```env
NODE_ENV=production
PORT=3000
MONGODB_URI=mongodb://...
REDIS_URL=redis://...
ELASTICSEARCH_URL=https://elasticsearch.example.com
ELASTICSEARCH_INDEX=search_index

```

---

## Database Migrations & Seeding

### MongoDB Migrations

**Migration Scripts:**

- **Schema Changes:** Add indexes for search queries

- **Data Migrations:** Update document formats

- **Index Optimization:** Add compound indexes for search

### Elasticsearch Indexing

**Index Management:**

- **Index Creation:** Create Elasticsearch indexes with proper mappings

- **Data Indexing:** Index documents from MongoDB to Elasticsearch

- **Index Updates:** Update indexes when schema changes

### Data Seeding

**Seed Data:**

- **Test Documents:** Seed test documents

- **Search Index:** Seed Elasticsearch index with test data

---

## API Documentation

### Swagger/OpenAPI

**API Documentation:**

- **Swagger UI:** Document REST APIs

- **Search API:** Document search endpoints

- **Autocomplete API:** Document autocomplete endpoints

---

## API Versioning

**Versioning Strategy:**

- **URL Versioning:** `/api/v1/search`, `/api/v2/search`

- **Header Versioning:** `Accept: application/vnd.api+json;version=1`

- **Backward Compatibility:** Maintain old API versions for existing clients

---

## Monitoring & Logging

### Application Monitoring

**Frontend:**

- **Error Tracking:** Sentry for search errors

- **Performance:** Track search query times

- **User Analytics:** Track search patterns

**Backend:**

- **APM:** Monitor search performance

- **Elasticsearch Monitoring:** Track Elasticsearch query performance

- **Search Metrics:** Track search volume, query latency, result relevance

### Logging

**Structured Logging:**

- **Winston / Pino:** Log search operations

- **Search Events:** Log search queries, results, user interactions

- **Error Logging:** Detailed error logs with context

---

## Database Transactions & Consistency

### MongoDB Transactions

**Transaction Usage:**

- **Multi-Document Transactions** - For operations requiring ACID guarantees

- **Example:** Document creation + Elasticsearch indexing

- **Session Management:** Use MongoDB sessions for transaction control

**Example:**

```typescript
const session = await mongoose.startSession();
session.startTransaction();
try {
  await Document.create([documentData], { session });
  await ElasticsearchService.indexDocument(documentData);
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

- **Search Index Consistency:** Keep Elasticsearch in sync with MongoDB

- **Cache Consistency:** Invalidate search cache on document updates

- **Eventual Consistency:** Handle eventual consistency between MongoDB and Elasticsearch

---

## Third-Party Service Integration

### Elasticsearch Integration

**Search Engine:**

- **Indexing:** Index documents from MongoDB to Elasticsearch

- **Query Processing:** Process search queries and return results

- **Autocomplete:** Implement autocomplete using Elasticsearch suggesters

- **Analytics:** Use Elasticsearch aggregations for search analytics

### Redis Integration

**Caching:**

- **Search Result Caching:** Cache frequently searched queries

- **Autocomplete Caching:** Cache autocomplete suggestions

- **Rate Limiting:** Use Redis for rate limiting

---

# 3) Interview Answers

---

## Q1. Designing a search system

**Situation:** Need to design a search system for 1B+ documents with < 100ms search latency, handling 10M+ queries per day.

**Action:** I designed a search system:

- **Inverted Index:** Build inverted index mapping words to document IDs for fast lookup

- **Elasticsearch:** Use Elasticsearch for distributed search engine with built-in ranking

- **Indexing Pipeline:** Index documents asynchronously, update index in real-time

- **Ranking Algorithm:** Use BM25/TF-IDF for relevance ranking, consider factors like term frequency, document length

- **Caching:** Cache popular search queries in Redis to reduce search load

- **Autocomplete:** Build trie data structure for fast autocomplete suggestions

- **Faceted Search:** Support filters (category, date, etc.) using Elasticsearch aggregations

- **Sharding:** Shard index across multiple nodes for scalability

**Result:** System handles 1B+ documents with search latency < 100ms. Cache hit rate of 60% reduces search load. Autocomplete responds in < 10ms.

**Takeaway:** Inverted index enables fast text search. Elasticsearch provides distributed search capabilities. Caching improves performance.

---

## Q2. Implementing autocomplete/suggestions

**Situation:** Users type search query, need to show suggestions in real-time.

**Action:** I implemented autocomplete:

- **Trie Data Structure:** Build trie (prefix tree) for fast prefix matching

- **Popular Queries:** Store top 10K popular queries in trie

- **Real-time Updates:** Update trie as search queries change

- **Caching:** Cache trie in Redis for fast access

- **Fuzzy Matching:** Support typos using edit distance algorithm

- **Ranking:** Rank suggestions by popularity and relevance

**Result:** Autocomplete responds in < 10ms. Suggestions are relevant and popular. Handles typos gracefully.

**Takeaway:** Trie provides fast prefix matching. Caching improves response time.

---

## Q3. Ranking search results by relevance

**Situation:** Multiple documents match search query, need to rank by relevance.

**Action:** I implemented search ranking:

- **BM25 Algorithm:** Use BM25 (Best Matching 25) for relevance scoring

- **Factors:** Consider term frequency, inverse document frequency, document length

- **Boosting:** Boost results based on document metadata (date, popularity)

- **Learning to Rank:** Use ML model to learn optimal ranking from user clicks

- **Personalization:** Personalize results based on user history (optional)

**Result:** Search relevance improved by 40%. Users find relevant results faster. Click-through rate increased by 25%.

**Takeaway:** BM25 provides good baseline ranking. ML models can improve ranking with user feedback.
