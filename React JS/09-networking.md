# ⚛️ React.js Interview Notes (2025 Edition)

## 🌐 Section 9 — Networking, Protocols & Integration — Q167-Q186

---

### 167. 🌐 What are REST APIs?

**🧠 Concept**

REST is a way to design web services that use HTTP methods to perform operations on data (like getting, creating, updating, or deleting).

**💻 Example**
```jsx
// REST API client
const apiClient = {
  // GET - Retrieve data
  async getUsers() {
    const response = await fetch('/api/users');
    return response.json();
  },
  
  // POST - Create new resource
  async createUser(userData) {
    const response = await fetch('/api/users', {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify(userData)
    });
    return response.json();
  },
  
  // PUT - Update entire resource
  async updateUser(id, userData) {
    const response = await fetch(`/api/users/${id}`, {
      method: 'PUT',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify(userData)
    });
    return response.json();
  },
  
  // DELETE - Remove resource
  async deleteUser(id) {
    const response = await fetch(`/api/users/${id}`, {
      method: 'DELETE'
    });
    return response.ok;
  }
};

// React hook for REST API
const useUsers = () => {
  const [users, setUsers] = useState([]);
  const [loading, setLoading] = useState(false);
  
  const fetchUsers = async () => {
    setLoading(true);
    try {
      const data = await apiClient.getUsers();
      setUsers(data);
    } catch (error) {
      console.error('Failed to fetch users:', error);
    } finally {
      setLoading(false);
    }
  };
  
  return { users, loading, fetchUsers };
};
```

📝 **Deeper Insight**

REST principles:
- **Stateless** - Each request contains all necessary information
- **Resource-based** - URLs represent resources
- **HTTP methods** - GET, POST, PUT, DELETE, PATCH
- **Status codes** - 200, 201, 400, 404, 500
- **JSON format** - Standard data exchange
- **Cacheable** - GET requests can be cached

---

### 168. 🌐 What is GraphQL, and how does it differ from REST?

🧠 **Concept**

GraphQL is a query language and runtime for APIs that allows clients to request exactly the data they need, reducing over-fetching and under-fetching problems.

💻 **Example**

```jsx
// GraphQL query
const GET_USER = gql`
  query GetUser($id: ID!) {
    user(id: $id) {
      id
      name
      email
      posts {
        id
        title
        content
      }
    }
  }
`;

// GraphQL mutation
const CREATE_USER = gql`
  mutation CreateUser($input: UserInput!) {
    createUser(input: $input) {
      id
      name
      email
    }
  }
`;

// React component with GraphQL
function UserProfile({ userId }) {
  const { data, loading, error } = useQuery(GET_USER, {
    variables: { id: userId }
  });
  
  const [createUser] = useMutation(CREATE_USER);
  
  if (loading) return <div>Loading...</div>;
  if (error) return <div>Error: {error.message}</div>;
  
  return (
    <div>
      <h1>{data.user.name}</h1>
      <p>{data.user.email}</p>
      {data.user.posts.map(post => (
        <div key={post.id}>
          <h3>{post.title}</h3>
          <p>{post.content}</p>
        </div>
      ))}
    </div>
  );
}
```

📝 **Deeper Insight**

GraphQL vs REST:
- **Single endpoint** - One GraphQL endpoint vs multiple REST endpoints
- **Client-driven** - Client specifies required fields
- **Type system** - Strong typing with schema
- **Real-time** - Subscriptions for live updates
- **Introspection** - Self-documenting API
- **Over-fetching** - GraphQL reduces unnecessary data

---

### 169. 🌐 What are the advantages of GraphQL?

🧠 **Concept**

GraphQL provides several advantages including efficient data fetching, strong typing, real-time subscriptions, and a single endpoint for all operations.

💻 **Example**

```jsx
// Efficient data fetching
const GET_USER_SUMMARY = gql`
  query GetUserSummary($id: ID!) {
    user(id: $id) {
      name
      email
      # Only fetch what we need
    }
  }
`;

// Real-time subscriptions
const USER_UPDATED = gql`
  subscription OnUserUpdated($userId: ID!) {
    userUpdated(userId: $userId) {
      id
      name
      email
    }
  }
`;

// Strong typing with TypeScript
interface User {
  id: string;
  name: string;
  email: string;
  posts: Post[];
}

interface Post {
  id: string;
  title: string;
  content: string;
}

// Fragment for reusable queries
const USER_FRAGMENT = gql`
  fragment UserInfo on User {
    id
    name
    email
  }
`;

const GET_USERS = gql`
  query GetUsers {
    users {
      ...UserInfo
    }
  }
  ${USER_FRAGMENT}
`;
```

📝 **Deeper Insight**

GraphQL advantages:
- **Efficient fetching** - Request only needed data
- **Single endpoint** - One URL for all operations
- **Strong typing** - Schema-based type safety
- **Real-time** - Subscriptions for live updates
- **Introspection** - Self-documenting API
- **Versioning** - Add fields without breaking changes
- **Developer experience** - Better tooling and debugging

---

### 170. 🌐 What are the disadvantages of GraphQL compared to REST?

🧠 **Concept**

GraphQL has several disadvantages including complexity, caching challenges, potential N+1 query problems, and learning curve compared to REST.

💻 **Example**

```jsx
// N+1 Query Problem
const GET_USERS_WITH_POSTS = gql`
  query GetUsersWithPosts {
    users {
      id
      name
      posts {  # This could cause N+1 queries
        id
        title
      }
    }
  }
`;

// Caching complexity
const client = new ApolloClient({
  uri: '/graphql',
  cache: new InMemoryCache({
    typePolicies: {
      User: {
        fields: {
          posts: {
            merge(existing = [], incoming) {
              return [...existing, ...incoming];
            }
          }
        }
      }
    }
  })
});

// Error handling complexity
const { data, loading, error } = useQuery(GET_USERS, {
  errorPolicy: 'all', // Handle partial errors
  onError: (error) => {
    console.error('GraphQL error:', error);
  }
});
```

📝 **Deeper Insight**

GraphQL disadvantages:
- **Complexity** - Steeper learning curve
- **Caching** - More complex than HTTP caching
- **N+1 queries** - Potential performance issues
- **File uploads** - Requires additional setup
- **Schema complexity** - Can become unwieldy
- **Over-engineering** - May be overkill for simple APIs
- **Debugging** - More complex error handling

---

### 171. 🌐 What is gRPC, and when is it preferred?

🧠 **Concept**

gRPC is a high-performance RPC framework that uses Protocol Buffers for serialization and HTTP/2 for transport, ideal for microservices communication.

💻 **Example**

```jsx
// gRPC client setup
import { grpc } from '@grpc/grpc-js';
import { loadSync } from '@grpc/proto-loader';

const packageDefinition = loadSync('user.proto');
const userProto = grpc.loadPackageDefinition(packageDefinition).user;

// gRPC service client
const client = new userProto.UserService('localhost:50051', grpc.credentials.createInsecure());

// React hook for gRPC
const useGrpcService = () => {
  const [data, setData] = useState(null);
  const [loading, setLoading] = useState(false);
  
  const getUser = (userId) => {
    setLoading(true);
    client.GetUser({ id: userId }, (error, response) => {
      if (error) {
        console.error('gRPC error:', error);
      } else {
        setData(response);
      }
      setLoading(false);
    });
  };
  
  return { data, loading, getUser };
};

// Usage in component
function UserComponent() {
  const { data, loading, getUser } = useGrpcService();
  
  useEffect(() => {
    getUser('123');
  }, []);
  
  if (loading) return <div>Loading...</div>;
  return <div>{data?.name}</div>;
}
```

📝 **Deeper Insight**

gRPC advantages:
- **Performance** - Binary serialization, HTTP/2
- **Type safety** - Protocol Buffer schemas
- **Streaming** - Bidirectional streaming support
- **Code generation** - Auto-generated client/server code
- **Microservices** - Ideal for service-to-service communication
- **Load balancing** - Built-in load balancing support

---

### 172. 🌐 What are WebSockets and how are they used in React?

🧠 **Concept**

WebSockets provide full-duplex communication between client and server, enabling real-time features like chat, live updates, and collaborative editing in React apps.

💻 **Example**

```jsx
// WebSocket hook
const useWebSocket = (url) => {
  const [socket, setSocket] = useState(null);
  const [message, setMessage] = useState(null);
  const [connectionStatus, setConnectionStatus] = useState('Connecting');
  
  useEffect(() => {
    const ws = new WebSocket(url);
    
    ws.onopen = () => {
      setConnectionStatus('Connected');
      setSocket(ws);
    };
    
    ws.onmessage = (event) => {
      setMessage(JSON.parse(event.data));
    };
    
    ws.onclose = () => {
      setConnectionStatus('Disconnected');
    };
    
    ws.onerror = (error) => {
      console.error('WebSocket error:', error);
      setConnectionStatus('Error');
    };
    
    return () => {
      ws.close();
    };
  }, [url]);
  
  const sendMessage = (data) => {
    if (socket && socket.readyState === WebSocket.OPEN) {
      socket.send(JSON.stringify(data));
    }
  };
  
  return { message, sendMessage, connectionStatus };
};

// Chat component
function ChatRoom() {
  const { message, sendMessage, connectionStatus } = useWebSocket('ws://localhost:8080');
  const [messages, setMessages] = useState([]);
  
  useEffect(() => {
    if (message) {
      setMessages(prev => [...prev, message]);
    }
  }, [message]);
  
  const handleSendMessage = (text) => {
    sendMessage({ type: 'message', text, timestamp: Date.now() });
  };
  
  return (
    <div>
      <div>Status: {connectionStatus}</div>
      <div>
        {messages.map((msg, index) => (
          <div key={index}>{msg.text}</div>
        ))}
      </div>
      <button onClick={() => handleSendMessage('Hello!')}>
        Send Message
      </button>
    </div>
  );
}
```

📝 **Deeper Insight**

WebSocket use cases:
- **Real-time chat** - Instant messaging
- **Live updates** - Stock prices, sports scores
- **Collaborative editing** - Google Docs-like features
- **Gaming** - Multiplayer games
- **Notifications** - Push notifications
- **IoT** - Device communication

---

### 173. 🌐 What is Server-Sent Events (SSE), and when to use it?

🧠 **Concept**

Server-Sent Events (SSE) provide one-way communication from server to client, ideal for live updates, notifications, and real-time data streaming.

💻 **Example**

```jsx
// SSE hook
const useServerSentEvents = (url) => {
  const [data, setData] = useState(null);
  const [connectionStatus, setConnectionStatus] = useState('Connecting');
  
  useEffect(() => {
    const eventSource = new EventSource(url);
    
    eventSource.onopen = () => {
      setConnectionStatus('Connected');
    };
    
    eventSource.onmessage = (event) => {
      setData(JSON.parse(event.data));
    };
    
    eventSource.onerror = (error) => {
      console.error('SSE error:', error);
      setConnectionStatus('Error');
    };
    
    return () => {
      eventSource.close();
    };
  }, [url]);
  
  return { data, connectionStatus };
};

// Live updates component
function LiveUpdates() {
  const { data, connectionStatus } = useServerSentEvents('/api/events');
  const [updates, setUpdates] = useState([]);
  
  useEffect(() => {
    if (data) {
      setUpdates(prev => [...prev, data]);
    }
  }, [data]);
  
  return (
    <div>
      <div>Connection: {connectionStatus}</div>
      <div>
        {updates.map((update, index) => (
          <div key={index}>
            {update.type}: {update.message}
          </div>
        ))}
      </div>
    </div>
  );
}
```

📝 **Deeper Insight**

SSE advantages:
- **Simple** - Easier than WebSockets
- **Automatic reconnection** - Built-in reconnection
- **HTTP/2 compatible** - Works with HTTP/2
- **One-way** - Server to client only
- **Event types** - Multiple event types
- **Use cases** - Notifications, live feeds, progress updates

---

### 174. 🌐 What are HTTP/2 and HTTP/3, and how do they improve network performance?

🧠 **Concept**

HTTP/2 and HTTP/3 are newer HTTP versions that improve performance through multiplexing, header compression, and better connection management.

💻 **Example**

```jsx
// HTTP/2 multiplexing benefits
const fetchMultipleResources = async () => {
  // HTTP/2 allows multiple requests over single connection
  const [users, posts, comments] = await Promise.all([
    fetch('/api/users'),
    fetch('/api/posts'),
    fetch('/api/comments')
  ]);
  
  return {
    users: await users.json(),
    posts: await posts.json(),
    comments: await comments.json()
  };
};

// HTTP/2 server push (conceptual)
const useServerPush = () => {
  useEffect(() => {
    // Server can push resources before client requests them
    const link = document.createElement('link');
    link.rel = 'preload';
    link.href = '/api/critical-data';
    link.as = 'fetch';
    document.head.appendChild(link);
  }, []);
};

// HTTP/3 with QUIC protocol
const useHttp3 = () => {
  const [data, setData] = useState(null);
  
  useEffect(() => {
    // HTTP/3 provides better performance over unreliable networks
    fetch('/api/data', {
      // HTTP/3 is handled by the browser automatically
      headers: {
        'Accept': 'application/json'
      }
    })
    .then(response => response.json())
    .then(setData);
  }, []);
  
  return data;
};
```

📝 **Deeper Insight**

HTTP version improvements:
- **HTTP/2** - Multiplexing, header compression, server push
- **HTTP/3** - QUIC protocol, better mobile performance
- **Multiplexing** - Multiple requests over single connection
- **Header compression** - Reduced overhead
- **Server push** - Proactive resource delivery
- **QUIC** - Better performance over unreliable networks

---

### 175. 🌐 What is the difference between Fetch and Axios?

🧠 **Concept**

Fetch is a native browser API for HTTP requests, while Axios is a third-party library that provides additional features like request/response interceptors and automatic JSON parsing.

💻 **Example**

```jsx
// Fetch API
const fetchData = async () => {
  try {
    const response = await fetch('/api/data', {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json',
        'Authorization': 'Bearer token'
      },
      body: JSON.stringify({ data: 'value' })
    });
    
    if (!response.ok) {
      throw new Error(`HTTP error! status: ${response.status}`);
    }
    
    const data = await response.json();
    return data;
  } catch (error) {
    console.error('Fetch error:', error);
  }
};

// Axios
import axios from 'axios';

const axiosInstance = axios.create({
  baseURL: '/api',
  timeout: 5000,
  headers: {
    'Content-Type': 'application/json'
  }
});

// Request interceptor
axiosInstance.interceptors.request.use(
  (config) => {
    config.headers.Authorization = `Bearer ${getToken()}`;
    return config;
  },
  (error) => Promise.reject(error)
);

// Response interceptor
axiosInstance.interceptors.response.use(
  (response) => response,
  (error) => {
    if (error.response?.status === 401) {
      // Handle unauthorized
      redirectToLogin();
    }
    return Promise.reject(error);
  }
);

const fetchDataWithAxios = async () => {
  try {
    const response = await axiosInstance.post('/data', { data: 'value' });
    return response.data;
  } catch (error) {
    console.error('Axios error:', error);
  }
};
```

📝 **Deeper Insight**

Fetch vs Axios:
- **Fetch** - Native, lightweight, promise-based
- **Axios** - Feature-rich, interceptors, automatic JSON
- **Error handling** - Axios throws for HTTP errors
- **Request/Response transformation** - Axios interceptors
- **Timeout** - Axios built-in, Fetch needs AbortController
- **Browser support** - Fetch newer, Axios more compatible

---

### 176. 🌐 How do you handle API retries, caching, and timeouts?

🧠 **Concept**

API reliability requires implementing retry logic, caching strategies, and timeout handling to ensure robust network communication in React applications.

💻 **Example**

```jsx
// Retry utility
const retryRequest = async (requestFn, maxRetries = 3, delay = 1000) => {
  for (let i = 0; i < maxRetries; i++) {
    try {
      return await requestFn();
    } catch (error) {
      if (i === maxRetries - 1) throw error;
      await new Promise(resolve => setTimeout(resolve, delay * Math.pow(2, i)));
    }
  }
};

// Caching with React Query
import { useQuery } from 'react-query';

const useCachedData = (key, fetchFn, options = {}) => {
  return useQuery(key, fetchFn, {
    staleTime: 5 * 60 * 1000, // 5 minutes
    cacheTime: 10 * 60 * 1000, // 10 minutes
    retry: 3,
    retryDelay: attemptIndex => Math.min(1000 * 2 ** attemptIndex, 30000),
    ...options
  });
};

// Timeout handling
const fetchWithTimeout = async (url, options = {}, timeout = 5000) => {
  const controller = new AbortController();
  const timeoutId = setTimeout(() => controller.abort(), timeout);
  
  try {
    const response = await fetch(url, {
      ...options,
      signal: controller.signal
    });
    clearTimeout(timeoutId);
    return response;
  } catch (error) {
    clearTimeout(timeoutId);
    if (error.name === 'AbortError') {
      throw new Error('Request timeout');
    }
    throw error;
  }
};

// Complete API client
class ApiClient {
  constructor(baseURL) {
    this.baseURL = baseURL;
    this.cache = new Map();
  }
  
  async request(endpoint, options = {}) {
    const url = `${this.baseURL}${endpoint}`;
    const cacheKey = `${url}-${JSON.stringify(options)}`;
    
    // Check cache
    if (this.cache.has(cacheKey)) {
      return this.cache.get(cacheKey);
    }
    
    try {
      const response = await retryRequest(
        () => fetchWithTimeout(url, options),
        3,
        1000
      );
      
      const data = await response.json();
      this.cache.set(cacheKey, data);
      return data;
    } catch (error) {
      console.error('API request failed:', error);
      throw error;
    }
  }
}
```

📝 **Deeper Insight**

API reliability strategies:
- **Retry logic** - Exponential backoff, circuit breakers
- **Caching** - Memory cache, HTTP cache, service workers
- **Timeouts** - Request timeouts, connection timeouts
- **Error handling** - Graceful degradation, fallbacks
- **Rate limiting** - Request throttling, backoff strategies
- **Monitoring** - Error tracking, performance metrics

---

### 177. 🌐 How do you cancel network requests in React?

🧠 **Concept**

Network request cancellation prevents memory leaks and unnecessary processing by aborting ongoing requests when components unmount or new requests are initiated.

💻 **Example**

```jsx
// AbortController for request cancellation
const useApiRequest = (url) => {
  const [data, setData] = useState(null);
  const [loading, setLoading] = useState(false);
  const [error, setError] = useState(null);
  
  useEffect(() => {
    const controller = new AbortController();
    
    const fetchData = async () => {
      setLoading(true);
      try {
        const response = await fetch(url, {
          signal: controller.signal
        });
        const result = await response.json();
        setData(result);
      } catch (err) {
        if (err.name !== 'AbortError') {
          setError(err);
        }
      } finally {
        setLoading(false);
      }
    };
    
    fetchData();
    
    return () => {
      controller.abort();
    };
  }, [url]);
  
  return { data, loading, error };
};

// Axios cancellation
import axios from 'axios';

const useAxiosRequest = (url) => {
  const [data, setData] = useState(null);
  
  useEffect(() => {
    const source = axios.CancelToken.source();
    
    const fetchData = async () => {
      try {
        const response = await axios.get(url, {
          cancelToken: source.token
        });
        setData(response.data);
      } catch (err) {
        if (!axios.isCancel(err)) {
          console.error('Request failed:', err);
        }
      }
    };
    
    fetchData();
    
    return () => {
      source.cancel('Component unmounted');
    };
  }, [url]);
  
  return data;
};

// React Query with cancellation
const useQueryWithCancellation = (queryKey, queryFn) => {
  return useQuery(queryKey, queryFn, {
    onError: (error) => {
      if (error.name === 'AbortError') {
        console.log('Query was cancelled');
      }
    }
  });
};
```

📝 **Deeper Insight**

Request cancellation benefits:
- **Memory leak prevention** - Avoid updating unmounted components
- **Performance** - Cancel unnecessary requests
- **User experience** - Prevent stale data display
- **Resource management** - Free up network resources
- **Race condition prevention** - Handle overlapping requests
- **Cleanup** - Proper component unmounting

---

### 178. 🌐 What are optimistic UI updates?

🧠 **Concept**

Optimistic UI updates immediately reflect user actions in the interface before server confirmation, providing instant feedback and better user experience.

💻 **Example**

```jsx
// Optimistic update hook
const useOptimisticUpdate = () => {
  const [optimisticData, setOptimisticData] = useState(null);
  
  const updateOptimistically = async (updateFn, rollbackFn) => {
    // Apply optimistic update
    setOptimisticData(updateFn);
    
    try {
      // Send to server
      const result = await apiCall();
      setOptimisticData(null); // Clear optimistic data
      return result;
    } catch (error) {
      // Rollback on error
      setOptimisticData(rollbackFn);
      throw error;
    }
  };
  
  return { optimisticData, updateOptimistically };
};

// Like button with optimistic updates
function LikeButton({ postId, initialLikes, isLiked }) {
  const [likes, setLikes] = useState(initialLikes);
  const [liked, setLiked] = useState(isLiked);
  const [isUpdating, setIsUpdating] = useState(false);
  
  const handleLike = async () => {
    if (isUpdating) return;
    
    setIsUpdating(true);
    const previousLikes = likes;
    const previousLiked = liked;
    
    // Optimistic update
    setLikes(prev => liked ? prev - 1 : prev + 1);
    setLiked(prev => !prev);
    
    try {
      await api.likePost(postId);
    } catch (error) {
      // Rollback on error
      setLikes(previousLikes);
      setLiked(previousLiked);
      console.error('Like failed:', error);
    } finally {
      setIsUpdating(false);
    }
  };
  
  return (
    <button onClick={handleLike} disabled={isUpdating}>
      {liked ? 'Unlike' : 'Like'} ({likes})
    </button>
  );
}
```

📝 **Deeper Insight**

Optimistic updates considerations:
- **User experience** - Instant feedback, perceived performance
- **Error handling** - Rollback mechanisms, error states
- **Conflict resolution** - Handle concurrent updates
- **Data consistency** - Sync with server state
- **Network conditions** - Handle offline scenarios
- **Complexity** - Additional state management

---

### 179. 🌐 What is stale-while-revalidate, and how does SWR use it?

🧠 **Concept**

Stale-while-revalidate (SWR) is a caching strategy that serves stale data immediately while fetching fresh data in the background, providing fast responses with eventual consistency.

💻 **Example**

```jsx
import useSWR from 'swr';

// SWR hook with stale-while-revalidate
const useUserData = (userId) => {
  const { data, error, mutate } = useSWR(
    `/api/users/${userId}`,
    fetcher,
    {
      revalidateOnFocus: true,
      revalidateOnReconnect: true,
      refreshInterval: 0,
      dedupingInterval: 2000,
      errorRetryCount: 3,
      errorRetryInterval: 5000
    }
  );
  
  return {
    user: data,
    isLoading: !error && !data,
    isError: error,
    mutate
  };
};

// Custom SWR configuration
const swrConfig = {
  fetcher: (url) => fetch(url).then(res => res.json()),
  revalidateOnFocus: false,
  revalidateOnReconnect: true,
  refreshInterval: 30000, // 30 seconds
  dedupingInterval: 2000,
  errorRetryCount: 3,
  errorRetryInterval: 5000,
  onError: (error) => {
    console.error('SWR error:', error);
  }
};

// Global SWR configuration
import { SWRConfig } from 'swr';

function App() {
  return (
    <SWRConfig value={swrConfig}>
      <UserProfile />
    </SWRConfig>
  );
}
```

📝 **Deeper Insight**

SWR benefits:
- **Fast responses** - Serve stale data immediately
- **Background updates** - Fresh data without blocking UI
- **Automatic revalidation** - Focus, reconnect, interval
- **Deduplication** - Prevent duplicate requests
- **Error handling** - Retry logic, error boundaries
- **Cache management** - Automatic cache invalidation

---

### 180. 🌐 How do you handle authentication in API requests?

🧠 **Concept**

API authentication involves securely managing user credentials, tokens, and session data to authorize requests and protect sensitive resources.

💻 **Example**

```jsx
// Authentication context
const AuthContext = createContext();

const AuthProvider = ({ children }) => {
  const [user, setUser] = useState(null);
  const [token, setToken] = useState(localStorage.getItem('token'));
  
  const login = async (credentials) => {
    try {
      const response = await fetch('/api/auth/login', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify(credentials)
      });
      
      const { user, token } = await response.json();
      setUser(user);
      setToken(token);
      localStorage.setItem('token', token);
    } catch (error) {
      throw new Error('Login failed');
    }
  };
  
  const logout = () => {
    setUser(null);
    setToken(null);
    localStorage.removeItem('token');
  };
  
  return (
    <AuthContext.Provider value={{ user, token, login, logout }}>
      {children}
    </AuthContext.Provider>
  );
};

// Authenticated API client
const useAuthenticatedApi = () => {
  const { token } = useContext(AuthContext);
  
  const apiCall = async (url, options = {}) => {
    const headers = {
      'Content-Type': 'application/json',
      ...options.headers
    };
    
    if (token) {
      headers.Authorization = `Bearer ${token}`;
    }
    
    const response = await fetch(url, {
      ...options,
      headers
    });
    
    if (response.status === 401) {
      // Handle unauthorized
      localStorage.removeItem('token');
      window.location.href = '/login';
    }
    
    return response;
  };
  
  return { apiCall };
};

// JWT token refresh
const useTokenRefresh = () => {
  const { token, setToken } = useContext(AuthContext);
  
  useEffect(() => {
    if (!token) return;
    
    const refreshToken = async () => {
      try {
        const response = await fetch('/api/auth/refresh', {
          method: 'POST',
          headers: {
            'Authorization': `Bearer ${token}`
          }
        });
        
        if (response.ok) {
          const { token: newToken } = await response.json();
          setToken(newToken);
          localStorage.setItem('token', newToken);
        }
      } catch (error) {
        console.error('Token refresh failed:', error);
      }
    };
    
    const interval = setInterval(refreshToken, 15 * 60 * 1000); // 15 minutes
    return () => clearInterval(interval);
  }, [token, setToken]);
};
```

📝 **Deeper Insight**

Authentication strategies:
- **JWT tokens** - Stateless authentication
- **Session cookies** - Server-side session management
- **OAuth 2.0** - Third-party authentication
- **API keys** - Simple authentication
- **Token refresh** - Automatic token renewal
- **Security** - HTTPS, secure storage, CSRF protection

---

*This comprehensive networking section covers all essential React networking, API integration, and protocol concepts for building robust web applications.*