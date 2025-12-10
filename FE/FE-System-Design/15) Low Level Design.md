# 🔧 Low Level Design

---

## 📍 Navigation

<div align="center">

[← Previous: High Level Design](14%29%20High%20Level%20Design.md) • [Home: Questions Index](question.md) • [Next: Security →](16%29%20Security.md)

[📋 Cheatsheet](FE-System-Design%20Interview%20Cheatsheet.md)

</div>

---

---

## Q45. 💡 View Layer Implementation

The view layer is everything the user sees and interacts with - buttons, forms, pages, animations. It's your UI code, and how you structure it makes a huge difference in how easy it is to build, maintain, and update. Understanding view layer patterns and best practices is crucial for building scalable, maintainable frontend applications.

---

## 1. 🧩 Component Architecture

Think of components like LEGO blocks - small, reusable pieces that you combine to build bigger things. Good component architecture makes your code easier to understand, test, and reuse.

### 🔹 Atomic Design Pattern

This is a way to organize components by size and complexity:

* **Atoms**: The smallest pieces - a button, an input field, a label. These can't be broken down further.

* **Molecules**: Combinations of atoms - a search bar (input + button), a form field (label + input + error message).

* **Organisms**: Complex UI sections - a header (logo + nav + user menu), a product card (image + title + price + button).

* **Templates**: Page layouts - where organisms go, the overall structure.

* **Pages**: Specific instances of templates with real data.

### 🔹 Component Patterns

**Presentational Components (Dumb Components)**

* These are all about appearance - you pass data in and these components display it

* These components don't know where data comes from or what happens when you click

* These are like actors following a script - these components just do what you tell them

* Examples: `<Button>`, `<Card>`, `<Input>`, `<Avatar>`

* Super reusable because these components don't have any business logic

* Easy to test - just check if these components render correctly with given props

* Example:

```javascript
// Presentational component - just displays data
function Button({ label, onClick, variant = 'primary' }) {
  return (
    <button
      className={`btn btn-${variant}`}
      onClick={onClick}
    >
      {label}
    </button>
  );
}

// Usage - parent handles the logic
function LoginForm() {
  const handleLogin = () => {
    // Business logic here
  };

  return <Button label="Login" onClick={handleLogin} />;
}

```

**Container Components (Smart Components)**

* These handle the logic - you use them to fetch data, manage state, handle events

* These are like directors - these components tell presentational components what to show

* These connect your UI to your data and business logic

* Examples: `<UserProfileContainer>`, `<ProductListContainer>`, `<CheckoutContainer>`

* Less reusable, but these components orchestrate everything

* Example:

```javascript
// Container component - handles logic
function UserProfileContainer({ userId }) {
  const [user, setUser] = useState(null);
  const [loading, setLoading] = useState(true);

  useEffect(() => {
    fetchUser(userId).then(user => {
      setUser(user);
      setLoading(false);
    });
  }, [userId]);

  if (loading) return <Spinner />;
  if (!user) return <Error />;

  // Pass data to presentational component
  return <UserProfile user={user} />;
}

// Presentational component - just displays
function UserProfile({ user }) {
  return (
    <div>
      <Avatar src={user.avatar} />
      <h1>{user.name}</h1>
      <p>{user.email}</p>
    </div>
  );
}

```

**Benefits of This Pattern:**

* Separation of concerns - UI separate from logic

* Easier testing - test logic and UI separately

* Better reusability - presentational components can be reused anywhere

* Easier to maintain - change logic without touching UI and vice versa

The idea is: separate what things look like (presentational) from how these components work (container). This makes both easier to change independently.

📌 **In simple terms**: Build small, reusable components (atoms, molecules) and combine them into bigger pieces (organisms, pages). Keep components that just display things separate from components that handle logic.

---

## 2. 🎨 Rendering Patterns

Where and when you render your HTML matters a lot for performance and SEO. Different patterns work better for different use cases.

### 🔹 Client-Side Rendering (CSR)

* **How it works**: Browser downloads a mostly empty HTML file, then JavaScript runs and builds the page

* **Good for**: Apps where users stay and interact a lot (dashboards, admin panels, SPAs)

* **Pros**: Fast navigation between pages (no full reloads), great for interactive apps

* **Cons**: Slower initial load (waiting for JS), bad for SEO (search engines see empty page), requires JavaScript

* **Example**: Traditional React SPA, Vue SPA

### 🔹 Server-Side Rendering (SSR)

* **How it works**: Server builds the HTML for each request and sends it to the browser

* **Good for**: Content that changes frequently, needs good SEO, or is personalized

* **Pros**: Fast initial load (HTML ready immediately), great SEO, works without JavaScript

* **Cons**: More server load (rendering on every request), slower time-to-first-byte

* **Example**: Next.js with `getServerSideProps`, Nuxt.js SSR

### 🔹 Static Site Generation (SSG)

* **How it works**: Build HTML files at build time, serve them as static files

* **Good for**: Content that doesn't change often (blogs, documentation, marketing sites)

* **Pros**: Fastest possible load (just serve static files), great SEO, cheap hosting (CDN)

* **Cons**: Content must be known at build time, need to rebuild to update content

* **Example**: Next.js with `getStaticProps`, Gatsby, Jekyll

### 🔹 Incremental Static Regeneration (ISR)

* **How it works**: Pre-render pages at build time, but regenerate them in the background when pages are requested and stale

* **Good for**: Sites with lots of pages where some change frequently (e-commerce, blogs with many posts)

* **Pros**: Fast like SSG, but content can update without full rebuild, great for large sites

* **Cons**: First request after content changes might see stale data (until regeneration completes)

* **Example**: Next.js ISR with `revalidate` option

📌 **In simple terms**: CSR renders in the browser (good for apps), SSR renders on the server (good for dynamic content), SSG pre-renders at build time (good for static content), and ISR combines SSG with background updates (good for large sites).

---

## 3. 🔍 Styling Approaches

How you write CSS affects how easy it is to maintain, how fast you can build, and how big your bundle is. Different approaches work better for different teams and projects.

### 🔹 CSS Modules

* **How it works**: Write regular CSS files, but these are scoped to components (class names get hashed)

* **Good for**: Teams comfortable with CSS, want scoped styles without learning new syntax

* **Pros**: No style conflicts (automatic scoping), familiar CSS syntax, works with any framework

* **Cons**: Still need to write CSS, can't share styles easily between components

* **Example**: `Button.module.css` imported into `Button.jsx`

### 🔹 CSS-in-JS (Styled Components)

* **How it works**: Write CSS as JavaScript, styles are component-scoped and can use props/state

* **Good for**: Dynamic styling, component libraries, teams comfortable with JavaScript

* **Pros**: Styles co-located with components, dynamic styling based on props, automatic vendor prefixes

* **Cons**: Runtime cost (styles generated in JavaScript), larger bundle size, learning curve

* **Example**: styled-components, emotion, styled-jsx

### 🔹 Utility-First CSS (Tailwind)

* **How it works**: Use pre-built utility classes instead of writing custom CSS

* **Good for**: Rapid prototyping, consistent design systems, teams that prefer HTML/JSX

* **Pros**: Super fast to build (just add classes), consistent spacing/colors, small bundle (unused styles removed)

* **Cons**: HTML/JSX can get verbose, learning curve for the utility classes, less semantic

* **Example**: Tailwind CSS, UnoCSS

### 🔹 Regular CSS / SCSS

* **How it works**: Write traditional CSS or SCSS files, import them globally or per component

* **Good for**: Simple projects, teams with strong CSS skills, when you need full control

* **Pros**: Full CSS power, familiar to everyone, works everywhere

* **Cons**: Global scope (can have conflicts), harder to maintain at scale, no automatic scoping

📌 **In simple terms**: CSS Modules scope your styles automatically, CSS-in-JS allows you to write styles in JavaScript with dynamic values, utility-first gives you pre-built classes for rapid development, and regular CSS gives you full control but requires careful management.

---

## ⭐ Summary — 10-second Interview Version

> "View layer implements UI components using patterns like atomic design. Rendering can be CSR, SSR, SSG, or ISR. Styling options include CSS modules, styled-components, or utility-first CSS like Tailwind."

---

## ⭐ Extra Points (If Interviewer Asks More)

### How do you decide between CSR and SSR?

Use CSR for dashboards and authenticated apps. Use SSR for public pages needing SEO. Use SSG for content sites. Use ISR for content that updates occasionally.

### What is component composition?

Building complex components by combining simpler ones, like building a Form from Input, Button, and Label components.

---

## Q46. 💡 Service Layer Implementation

The service layer is your app's way of talking to the outside world - APIs, backends, third-party services. It's like having a dedicated phone operator who knows how to call everyone and translate what those services say into something your app understands.

---

## 1. 💡 Service Layer Responsibilities

The service layer has a few key jobs - think of it as your app's communication department.

### 🔹 API Communication

* **What it does**: Makes HTTP requests to your backend or third-party APIs

* **Its job**: Know all the API endpoints, handle authentication, manage request/response cycles

* **Why it matters**: Keeps all API logic in one place instead of scattered across components

* **Example**: `userService.getUser(id)` knows how to call `/api/users/123` with the right headers

### 🔹 Data Transformation

* **What it does**: Converts API responses into formats your app can use

* **Its job**: The API might return `{ user_name: "John" }` but your app wants `{ name: "John" }` - service layer fixes that

* **Why it matters**: APIs don't always return data in the shape your components expect

* **Example**: Transform snake_case API responses to camelCase, or combine multiple API calls into one object

### 🔹 Error Handling

* **What it does**: Catches API errors and turns them into something useful

* **Its job**: Network failures, 404s, 500s - handle them all and give components clear error messages

* **Why it matters**: Components shouldn't have to know about HTTP status codes

* **Example**: API returns 404 → service layer throws `UserNotFoundError` with a friendly message

### 🔹 Caching

* **What it does**: Remembers API responses so you don't call the same endpoint repeatedly

* **Its job**: Store responses, check if data is still fresh, invalidate cache when needed

* **Why it matters**: Reduces API calls, makes your app faster, saves bandwidth

* **Example**: Cache user profile for 5 minutes, so multiple components can use it without extra API calls

📌 **In simple terms**: The service layer is your app's translator and messenger - it talks to APIs, transforms data into useful formats, handles errors gracefully, and caches responses to make everything faster.

---

## 2. 💡 Service Implementation Patterns

There are different ways to structure your services - pick what works for your team and project.

### 🔹 Service Classes

Use classes when you want to encapsulate related methods and maybe share some state:

```javascript
class UserService {
  constructor(apiClient) {
    this.api = apiClient;
  }

  async getUser(id) {
    const response = await this.api.get(`/users/${id}`);
    return this.transformUser(response.data);
  }

  async createUser(userData) {
    const response = await this.api.post('/users', userData);
    return this.transformUser(response.data);
  }

  transformUser(data) {
    return {
      id: data.id,
      name: data.user_name, // Transform API format
      email: data.email_address
    };
  }
}

```

**Good for**: When you need to share configuration or helper methods, object-oriented style

### 🔹 Service Functions

Use plain functions/objects when you want something simpler:

```javascript
export const userService = {
  getUser: async (id) => {
    const response = await api.get(`/users/${id}`);
    return transformUserResponse(response.data);
  },

  createUser: async (userData) => {
    const response = await api.post('/users', userData);
    return transformUserResponse(response.data);
  }
};

// Or even simpler - just export functions
export async function getUser(id) {
  const response = await api.get(`/users/${id}`);
  return transformUserResponse(response.data);
}

```

**Good for**: Functional style, simpler code, easier to test

### 🔹 API Client Abstraction

Create a shared API client that handles common stuff (auth, errors, base URL):

```javascript
// apiClient.js - Set up once, use everywhere
const apiClient = axios.create({
  baseURL: process.env.API_URL,
  timeout: 10000,
  headers: {
    'Content-Type': 'application/json'
  }
});

// Add auth token to every request
apiClient.interceptors.request.use((config) => {
  const token = getAuthToken();
  if (token) {
    config.headers.Authorization = `Bearer ${token}`;
  }
  return config;
});

// Handle errors consistently
apiClient.interceptors.response.use(
  (response) => response,
  (error) => {
    if (error.response?.status === 401) {
      // Redirect to login
      redirectToLogin();
    }
    return Promise.reject(error);
  }
);

export default apiClient;

```

**Why this matters**: Write auth/error handling once, use it everywhere. Services just use `apiClient.get()` and don't worry about tokens or error codes.

---

## 3. 💡 Service Layer Best Practices

### 🔹 Separation of Concerns

* Keep services focused on API communication

* Move business logic to controller/state layer

* Services should be stateless

### 🔹 Error Handling

* Consistent error format

* Transform API errors to app errors

* Handle network failures gracefully

### 🔹 Type Safety

* Use TypeScript for type safety

* Define interfaces for requests/responses

* Catch type errors at compile time

---

## ⭐ Summary — 10-second Interview Version

> "Service layer handles API communication, data transformation, and error handling. Implement as classes or functions, use API client abstraction, and keep services focused on external communication."

---

## ⭐ Extra Points (If Interviewer Asks More)

### How do you handle API versioning in services?

Use versioned endpoints (`/api/v1/users`), or include version in headers. Create service methods that abstract version details from components.

### What's the difference between service layer and API client?

API client is the low-level HTTP library (axios, fetch wrapper). Service layer uses the API client and adds business logic, transformation, and error handling.

---

## Q47. 💡 Controller/Business Logic Implementation

The controller layer is like the conductor of an orchestra - it coordinates everything. It manages state, handles user actions, and makes sure data flows correctly between your UI and your services.

---

## 1. 💡 Controller Responsibilities

The controller is the brain of your app - it makes decisions and coordinates everything.

### 🔹 State Management

* **What it does**: Keeps track of what's happening in your app - user data, UI state, what's loading

* **Its job**: Store state, update it when things change, share it between components that need it

* **Why it matters**: Components need to know what to show - state tells them

* **Example**: User logs in → controller updates `isAuthenticated` state → all components know user is logged in

### 🔹 Event Handling

* **What it does**: Responds to user actions - clicks, form submissions, navigation

* **Its job**: When user clicks "Submit", figure out what should happen and make it happen

* **Why it matters**: User actions need to trigger the right responses

* **Example**: User clicks "Add to Cart" → controller calls service → updates cart state → UI shows updated cart

### 🔹 Data Flow Orchestration

* **What it does**: Coordinates the dance between services (getting data) and views (showing data)

* **Its job**: Call services, wait for data, transform it if needed, pass it to components, handle loading/errors

* **Why it matters**: Services and views shouldn't talk directly - controller is the middleman

* **Example**: Component needs user data → controller calls `userService.getUser()` → waits → transforms data → updates state → component re-renders with data

### 🔹 Business Logic

* **What it does**: Implements the rules of your app - what's allowed, what's not, how things work

* **Its job**: Validate data, enforce business rules, coordinate workflows

* **Why it matters**: Your app has rules - "users can't checkout with empty cart", "admins can delete posts" - controller enforces them

* **Example**: User tries to checkout → controller checks if cart has items → if empty, show error → if not, proceed to payment

📌 **In simple terms**: The controller manages state (what's happening), handles events (user actions), orchestrates data flow (services ↔ views), and enforces business rules (what's allowed).

---

## 2. 📦 State Management Patterns

### 🔹 Local State (React)

```javascript
const [user, setUser] = useState(null);
const [loading, setLoading] = useState(false);

const fetchUser = async (id) => {
  setLoading(true);
  try {
    const data = await userService.getUser(id);
    setUser(data);
  } catch (error) {
    handleError(error);
  } finally {
    setLoading(false);
  }
};

```

### 🔹 Global State (Redux)

```javascript
// Actions
const fetchUser = (id) => async (dispatch) => {
  dispatch({ type: 'FETCH_USER_START' });
  try {
    const user = await userService.getUser(id);
    dispatch({ type: 'FETCH_USER_SUCCESS', payload: user });
  } catch (error) {
    dispatch({ type: 'FETCH_USER_ERROR', payload: error });
  }
};

// Reducer
const userReducer = (state = initialState, action) => {
  switch (action.type) {
    case 'FETCH_USER_SUCCESS':
      return { ...state, user: action.payload, loading: false };
    // ...
  }
};

```

### 🔹 Context API (React)

```javascript
const UserContext = createContext();

const UserProvider = ({ children }) => {
  const [user, setUser] = useState(null);
  const value = { user, setUser };
  return <UserContext.Provider value={value}>{children}</UserContext.Provider>;
};

```

---

## 3. 💡 Controller Patterns

### 🔹 Custom Hooks (React)

```javascript
const useUser = (userId) => {
  const [user, setUser] = useState(null);
  const [loading, setLoading] = useState(true);

  useEffect(() => {
    userService.getUser(userId)
      .then(setUser)
      .finally(() => setLoading(false));
  }, [userId]);

  return { user, loading };
};

```

### 🔹 View Models (MVVM)

```javascript
class UserViewModel {
  constructor(userService) {
    this.userService = userService;
    this.user = null;
    this.loading = false;
  }

  async loadUser(id) {
    this.loading = true;
    this.user = await this.userService.getUser(id);
    this.loading = false;
  }
}

```

---

## ⭐ Summary — 10-second Interview Version

> "Controller layer manages state (local, global, or context), handles events, and orchestrates data flow. Use custom hooks, Redux, or view models to implement controllers that coordinate between services and views."

---

## ⭐ Extra Points (If Interviewer Asks More)

### When to use local vs global state?

Use local state for component-specific data (form inputs, UI state). Use global state for shared data (user info, theme, cart) accessed by multiple components.

### What is the difference between controller and service?

Controller manages application flow and state. Service handles external communication (APIs). Controller uses services to fetch data, then updates state.

---

## Q48. 💡 Data Model Implementation

Data models are like blueprints for your data - these define what shape your data should be, what fields it has, what types those fields are, and what rules those fields need to follow. Good data models make your code more predictable and catch errors early.

---

## 1. 🏷️ Data Model Types

There are different ways to define your data models - pick what works for your project.

### 🔹 TypeScript Interfaces

TypeScript interfaces give you compile-time type checking - catch errors before code runs:

```typescript
interface User {
  id: string;
  name: string;
  email: string;
  createdAt: Date;
  profile?: UserProfile; // Optional field
}

interface UserProfile {
  avatar: string;
  bio: string;
  location: string;
}

// Now TypeScript knows what a User looks like
function displayUser(user: User) {
  console.log(user.name); // ✅ TypeScript knows this exists
  console.log(user.phone); // ❌ TypeScript error - phone doesn't exist
}

```

**Good for**: Type safety, catching errors early, better IDE autocomplete

### 🔹 Classes

Classes let you add methods and behavior to your data:

```javascript
class User {
  constructor(data) {
    this.id = data.id;
    this.name = data.name;
    this.email = data.email;
    this.createdAt = new Date(data.createdAt);
  }

  // Methods that work with the data
  getDisplayName() {
    return this.name || this.email;
  }

  isValid() {
    return this.email && this.email.includes('@');
  }

  getAge() {
    return new Date().getFullYear() - this.createdAt.getFullYear();
  }
}

// Use it
const user = new User({ id: '1', name: 'John', email: 'john@example.com', createdAt: '2020-01-01' });
console.log(user.getDisplayName()); // "John"

```

**Good for**: When you need methods, object-oriented style, data transformation

### 🔹 JSON Schema

JSON Schema is a standard way to describe and validate data:

```json
{
  "type": "object",
  "properties": {
    "id": { "type": "string" },
    "name": { "type": "string", "minLength": 1 },
    "email": { "type": "string", "format": "email" },
    "age": { "type": "number", "minimum": 0, "maximum": 120 }
  },
  "required": ["id", "name", "email"]
}

```

**Good for**: API documentation, runtime validation, language-agnostic schemas

📌 **In simple terms**: Use TypeScript interfaces for type safety, classes when you need methods, and JSON Schema for validation and documentation. Pick what fits your needs.

---

## 2. 💡 Data Normalization

Normalization means organizing your data so you don't store the same thing in multiple places. It's like having one master list instead of copies everywhere.

### 🔹 The Problem with Nested Data

When data is nested, you end up duplicating it:

```javascript
// Nested structure - data is duplicated
{
  users: [
    {
      id: '1',
      name: 'John',
      posts: [
        { id: '1', title: 'Post 1', author: 'John' }, // John's name duplicated
        { id: '2', title: 'Post 2', author: 'John' }  // John's name duplicated again
      ]
    }
  ]
}

// Problem: If John changes his name, you have to update it in multiple places!

```

### 🔹 Normalized Structure

Store each type of data separately and reference them:

```javascript
// Normalized structure - single source of truth
{
  users: {
    '1': { id: '1', name: 'John' } // John's data in one place
  },
  posts: {
    '1': { id: '1', title: 'Post 1', userId: '1' }, // Reference to user
    '2': { id: '2', title: 'Post 2', userId: '1' }  // Reference to user
  }
}

// To get user's posts: Look up user, get their postIds, look up posts
// To update John's name: Update users['1'].name - done!

```

### 🔹 Why Normalize?

* **No duplication**: Store data once, reference it everywhere

* **Easier updates**: Change John's name in one place, it updates everywhere

* **Better performance**: No deep object traversal, faster lookups

* **Easier queries**: "Find all posts by John" - just filter posts by userId

* **Consistent data**: Can't have John's name be different in different places

📌 **In simple terms**: Normalization means storing each piece of data once and referencing it, instead of duplicating it. Makes updates easier and data more consistent.

---

## 3. ✅ Data Validation

You can't trust data from APIs or users - always validate it. Validation checks if data matches what you expect.

### 🔹 Runtime Validation with Zod

Zod is a popular library for validating data at runtime:

```javascript
import { z } from 'zod';

// Define what valid data looks like
const UserSchema = z.object({
  id: z.string(),
  name: z.string().min(1, 'Name cannot be empty'),
  email: z.string().email('Invalid email format'),
  age: z.number().min(0).max(120).optional()
});

// Validate API response
try {
  const user = UserSchema.parse(apiResponse); // Throws if invalid
  // user is now guaranteed to match the schema
} catch (error) {
  console.error('Invalid user data:', error.errors);
}

```

**Why this matters**: APIs can return unexpected data. Validation catches it before it breaks your app.

### 🔹 Type Guards (TypeScript)

Type guards help TypeScript understand what type something is:

```typescript
function isUser(data: unknown): data is User {
  return (
    typeof data === 'object' &&
    data !== null &&
    'id' in data &&
    typeof data.id === 'string' &&
    'name' in data &&
    typeof data.name === 'string' &&
    'email' in data &&
    typeof data.email === 'string'
  );
}

// Use it
const data = await fetchUser();
if (isUser(data)) {
  // TypeScript now knows data is a User
  console.log(data.name); // ✅ TypeScript knows this is safe
} else {
  // Handle invalid data
  throw new Error('Invalid user data');
}

```

**Why this matters**: TypeScript can't check runtime data - type guards bridge that gap.

📌 **In simple terms**: Always validate data from APIs/users. Use Zod for runtime validation or type guards for TypeScript. Don't trust external data - validate it!

---

## ⭐ Summary — 10-second Interview Version

> "Data models define data structure using TypeScript interfaces, classes, or JSON schemas. Normalize nested data for better performance. Validate data at runtime using libraries like Zod or type guards."

---

## ⭐ Extra Points (If Interviewer Asks More)

### Why normalize data?

Normalization eliminates duplication, makes updates easier (single source of truth), improves performance (no deep object traversal), and simplifies queries.

### How do you handle API response transformation?

Create mapper functions that transform API responses to your app's data models, handling differences in structure, naming, and types.

---

## Q49. 🕸️ API/GraphQL Implementation

API implementation is how your frontend talks to your backend. You need to set up clients, handle requests/responses, manage errors, and structure your API calls. Whether you use REST or GraphQL, good API implementation makes your code cleaner and more maintainable.

---

## 1. 🔀 REST API Implementation

REST APIs use standard HTTP methods (GET, POST, PUT, DELETE) to interact with resources. Setting up a good API client makes all your API calls consistent and easy.

### 🔹 API Client Setup

Create a shared API client that handles common stuff (auth, errors, base URL):

```javascript
// apiClient.js - Set up once, use everywhere
import axios from 'axios';

const apiClient = axios.create({
  baseURL: process.env.REACT_APP_API_URL, // Base URL for all requests
  timeout: 10000, // Request times out after 10 seconds
  headers: {
    'Content-Type': 'application/json'
  }
});

// Request interceptor - runs before every request
apiClient.interceptors.request.use((config) => {
  const token = getAuthToken();
  if (token) {
    config.headers.Authorization = `Bearer ${token}`; // Add auth token
  }
  return config;
});

// Response interceptor - runs after every response
apiClient.interceptors.response.use(
  (response) => response.data, // Just return the data, not the whole response
  (error) => {
    if (error.response?.status === 401) {
      // User not authenticated - redirect to login
      redirectToLogin();
    }
    // Transform error to something useful
    return Promise.reject(transformError(error));
  }
);

```

**Why this matters**: Write auth/error handling once, use it everywhere. All your API calls automatically get auth tokens and proper error handling.

### 🔹 API Methods

Organize API calls by resource:

```javascript
// usersApi.js - All user-related API calls
export const usersApi = {
  getAll: () => apiClient.get('/users'),
  getById: (id) => apiClient.get(`/users/${id}`),
  create: (data) => apiClient.post('/users', data),
  update: (id, data) => apiClient.put(`/users/${id}`, data),
  delete: (id) => apiClient.delete(`/users/${id}`)
};

// Use it in components
const users = await usersApi.getAll();
const user = await usersApi.getById('123');

```

**Why this matters**: All API calls in one place, easy to find and update, consistent naming.

---

## 2. 🕸️ GraphQL Implementation

GraphQL allows you to request exactly the data you need in a single query. Instead of multiple REST endpoints, you have one endpoint and specify what fields you want.

### 🔹 GraphQL Client Setup

Apollo Client is the most popular GraphQL client for React:

```javascript
// apolloClient.js
import { ApolloClient, InMemoryCache, createHttpLink } from '@apollo/client';

const httpLink = createHttpLink({
  uri: process.env.REACT_APP_GRAPHQL_URL // Your GraphQL endpoint
});

const client = new ApolloClient({
  link: httpLink,
  cache: new InMemoryCache(), // Caches query results automatically
  defaultOptions: {
    watchQuery: {
      fetchPolicy: 'cache-and-network' // Use cache but also fetch fresh data
    }
  }
});

```

**Why Apollo**: Handles caching, loading states, error handling, and subscriptions automatically.

### 🔹 Queries (Reading Data)

Queries fetch data - you specify exactly what fields you want:

```javascript
// queries.js
import { gql } from '@apollo/client';

export const GET_USER = gql`
  query GetUser($id: ID!) {
    user(id: $id) {
      id
      name
      email
      posts {
        id
        title
      }
    }
  }
`;

// Usage in component
import { useQuery } from '@apollo/client';

function UserProfile({ userId }) {
  const { data, loading, error } = useQuery(GET_USER, {
    variables: { id: userId }
  });

  if (loading) return <div>Loading...</div>;
  if (error) return <div>Error: {error.message}</div>;

  return <div>{data.user.name}</div>;
}

```

**Why GraphQL queries are great**: Get exactly what you need in one request - no over-fetching or under-fetching.

### 🔹 Mutations (Writing Data)

Mutations change data - create, update, or delete:

```javascript
export const CREATE_USER = gql`
  mutation CreateUser($input: UserInput!) {
    createUser(input: $input) {
      id
      name
      email
    }
  }
`;

// Usage in component
import { useMutation } from '@apollo/client';

function CreateUserForm() {
  const [createUser, { loading, error }] = useMutation(CREATE_USER);

  const handleSubmit = async (formData) => {
    try {
      const { data } = await createUser({
        variables: { input: formData }
      });
      console.log('User created:', data.createUser);
    } catch (err) {
      console.error('Error:', err);
    }
  };

  return <form onSubmit={handleSubmit}>...</form>;
}

```

**Why GraphQL mutations**: Same flexibility as queries - get back exactly what you need after creating/updating.

📌 **In simple terms**: GraphQL allows you to request exactly the data you need in one query. Apollo Client handles caching, loading states, and errors. Queries fetch data, mutations change data.

---

## 3. 🔌 API Best Practices

### 🔹 Error Handling

* **Consistent format**: All errors should have the same structure - makes handling easier

* **Network errors**: Handle offline, timeout, connection refused - show user-friendly messages

* **Transform errors**: API returns `{ error: "INVALID_EMAIL" }` → show "Please enter a valid email address"

* **Retry logic**: For transient failures (network blips), retry automatically with exponential backoff

* **Error boundaries**: Catch errors at component level, show fallback UI

### 🔹 Caching

* **Cache GET requests**: Don't refetch data you already have

* **Invalidate on mutations**: When you create/update/delete, clear related cache

* **Cache headers**: Use HTTP cache headers (`Cache-Control`) for browser caching

* **Request deduplication**: If multiple components request same data simultaneously, only make one request

* **Stale-while-revalidate**: Show cached data immediately, fetch fresh data in background

### 🔹 Type Safety

* **Generate types**: Use tools to generate TypeScript types from your API schema

* **GraphQL Code Generator**: Automatically generates types from GraphQL schema

* **Runtime validation**: Even with TypeScript, validate API responses at runtime (APIs can change)

* **Type-safe API calls**: Your IDE should autocomplete API methods and catch type errors

📌 **In simple terms**: Handle errors consistently and user-friendly. Cache responses to avoid unnecessary requests. Use TypeScript and generate types from your API schema for type safety.

---

## ⭐ Summary — 10-second Interview Version

> "REST APIs use HTTP methods with axios/fetch. GraphQL uses queries and mutations with Apollo Client. Implement interceptors for auth, error handling, and caching. Use TypeScript for type safety."

---

## ⭐ Extra Points (If Interviewer Asks More)

### How do you handle API versioning?

Include version in URL (`/api/v1/users`) or headers. Create versioned API clients. Gradually migrate to new versions.

### What are the trade-offs between REST and GraphQL?

REST is simpler, cacheable, and works well with HTTP. GraphQL reduces over-fetching, allows flexible queries, but requires more complex caching and can have N+1 query problems.

---

## Q50. 📦 State Management Implementation

State management is how you store and share data across your app. When multiple components need the same data (like user info, theme, shopping cart), you need a way to manage it centrally so everything stays in sync.

---

## 1. ✅ State Management Solutions

Different tools work better for different situations. Here are the most common options:

### 🔹 React Context API

Context is built into React - no extra libraries needed. Good for sharing data across a component tree:

```javascript
// UserContext.js
const UserContext = createContext();

export const UserProvider = ({ children }) => {
  const [user, setUser] = useState(null);
  const [loading, setLoading] = useState(false);

  const login = async (credentials) => {
    setLoading(true);
    const userData = await authService.login(credentials);
    setUser(userData);
    setLoading(false);
  };

  return (
    <UserContext.Provider value={{ user, login, loading }}>
      {children}
    </UserContext.Provider>
  );
};

// Use it in components
const { user, login } = useContext(UserContext);

```

**Good for**: Simple shared state, theme, user info, when you don't need complex state logic
**Watch out for**: Can cause re-renders if not optimized, not great for frequently updating state

### 🔹 Redux Toolkit

Redux is the most popular state management library - powerful but has a learning curve:

```javascript
// userSlice.js
import { createSlice, createAsyncThunk } from '@reduxjs/toolkit';

export const fetchUser = createAsyncThunk(
  'user/fetchUser',
  async (userId) => {
    return await userService.getUser(userId);
  }
);

const userSlice = createSlice({
  name: 'user',
  initialState: { user: null, loading: false },
  reducers: {
    logout: (state) => {
      state.user = null;
    }
  },
  extraReducers: (builder) => {
    builder
      .addCase(fetchUser.pending, (state) => {
        state.loading = true;
      })
      .addCase(fetchUser.fulfilled, (state, action) => {
        state.user = action.payload;
        state.loading = false;
      });
  }
});

// Use it
const dispatch = useDispatch();
const user = useSelector(state => state.user.user);
dispatch(fetchUser(userId));

```

**Good for**: Complex state, large apps, when you need time-travel debugging, predictable state updates
**Watch out for**: More boilerplate, steeper learning curve

### 🔹 Zustand

Zustand is a lightweight alternative to Redux - simpler API, less boilerplate:

```javascript
// userStore.js
import create from 'zustand';

const useUserStore = create((set) => ({
  user: null,
  loading: false,
  setUser: (user) => set({ user }),
  fetchUser: async (id) => {
    set({ loading: true });
    const user = await userService.getUser(id);
    set({ user, loading: false });
  },
  logout: () => set({ user: null })
}));

// Use it - super simple!
const { user, fetchUser, loading } = useUserStore();

```

**Good for**: Simpler than Redux, good for medium complexity apps, less boilerplate
**Watch out for**: Less tooling/ecosystem than Redux

📌 **In simple terms**: Use Context for simple shared state, Redux for complex apps, Zustand for a middle ground. Pick based on your app's complexity.

---

## 2. 📦 Server State Management

Server state (data from APIs) is different from client state - it needs caching, refetching, and synchronization. Special tools handle this better than regular state management.

### 🔹 React Query (TanStack Query)

React Query is the most popular tool for managing server state - it handles caching, refetching, and synchronization automatically:

```javascript
import { useQuery, useMutation, useQueryClient } from '@tanstack/react-query';

// Query - automatically caches, refetches, handles loading/errors
const { data, isLoading, error } = useQuery({
  queryKey: ['user', userId], // Cache key
  queryFn: () => userService.getUser(userId), // Function to fetch data
  staleTime: 5 * 60 * 1000, // Data is fresh for 5 minutes
  cacheTime: 10 * 60 * 1000 // Keep in cache for 10 minutes
});

// Mutation - automatically invalidates related queries
const queryClient = useQueryClient();
const mutation = useMutation({
  mutationFn: userService.createUser,
  onSuccess: () => {
    // Invalidate users list - will refetch automatically
    queryClient.invalidateQueries(['users']);
  }
});

```

**Why React Query is great**: Handles caching, background refetching, deduplication, error retries - all the annoying stuff you'd have to write yourself.

### 🔹 SWR (Stale-While-Revalidate)

SWR is similar to React Query but simpler and lighter:

```javascript
import useSWR from 'swr';

const fetcher = (url) => fetch(url).then(res => res.json());

const { data, error, isLoading } = useSWR(
  `/api/users/${userId}`, // Cache key (the URL)
  fetcher, // Function to fetch
  {
    revalidateOnFocus: false, // Don't refetch when window gains focus
    dedupingInterval: 2000, // Dedupe requests within 2 seconds
    refreshInterval: 0 // Don't auto-refresh
  }
);

```

**Why SWR is great**: Simpler API than React Query, good for straightforward use cases, smaller bundle size.

📌 **In simple terms**: React Query and SWR handle server state (API data) - these libraries cache responses, refetch when needed, handle loading/errors, and keep data fresh. Much better than managing API state manually.

---

## 3. 📦 State Management Best Practices

### 🔹 Choose the Right Tool for the Job

* **Local state (`useState`)**: Component-specific data - form inputs, modal open/closed, UI state

* **Context API**: Shared data in a component tree - theme, user info, simple global state

* **Redux/Zustand**: Complex global state - large apps, complex state logic, need for time-travel debugging

* **React Query/SWR**: Server state (API data) - automatic caching, refetching, synchronization

**Rule of thumb**: Start simple (useState, Context), add complexity only when needed. Don't use Redux for everything - most apps don't need it.

### 🔹 Keep State Close to Where It's Used

* **Component state**: If only one component needs it, use `useState` in that component

* **Lift state up**: If multiple siblings need it, lift to common parent

* **Global state**: Only use global state if many components across the app need it

### 🔹 Normalize State

* Store data in normalized form (by ID, not nested arrays)

* Makes updates easier, prevents inconsistencies

* Use libraries like `normalizr` if needed

### 🔹 Separate Server and Client State

* **Server state**: Use React Query/SWR - handles caching, refetching automatically

* **Client state**: Use useState/Context/Redux - UI state, user preferences, form data

📌 **In simple terms**: Use the simplest tool that works. Keep state close to where it's used. Separate server state (use React Query) from client state (use useState/Context/Redux). Don't over-engineer.

### 🔹 Normalize State

* Keep state flat and normalized

* Avoid nested objects when possible

* Use IDs to reference related data

### 🔹 Immutability

* Never mutate state directly

* Always return new objects/arrays

* Use libraries like Immer for complex updates

---

## ⭐ Summary — 10-second Interview Version

> "State management handles app data using Context API, Redux, or Zustand for global state, and React Query/SWR for server state. Normalize state, maintain immutability, and choose the right tool for each use case."

---

## ⭐ Extra Points (If Interviewer Asks More)

### When to use Redux vs Context API?

Use Context for simple shared state in a component tree. Use Redux for complex state with time-travel debugging, middleware needs, or large applications.

### What is the difference between client state and server state?

Client state is UI state and app state managed in memory. Server state is data from APIs that needs caching, synchronization, and background updates.

---

## Q51. ✅ Error Handling & Validation

Error handling is about gracefully dealing with things that go wrong - network failures, invalid data, bugs. Validation is about checking data before you use it - making sure user input is correct and API responses are what you expect. Both are essential for building robust apps.

---

## 1. 💡 Error Handling Patterns

Errors happen - network failures, bugs, invalid data. Good error handling means your app doesn't crash and users get helpful messages.

### 🔹 Try-Catch Blocks

Wrap risky operations in try-catch to handle errors gracefully:

```javascript
try {
  const user = await userService.getUser(userId);
  setUser(user);
} catch (error) {
  // Handle different types of errors
  if (error.response?.status === 404) {
    showError('User not found');
  } else if (error.response?.status === 500) {
    showError('Server error. Please try again.');
  } else if (error.code === 'NETWORK_ERROR') {
    showError('Network error. Check your connection.');
  } else {
    showError('Something went wrong');
    // Log unexpected errors for debugging
    logError(error);
  }
}

```

**Why this matters**: Users see helpful messages instead of crashes, and you can log errors for debugging.

### 🔹 Error Boundaries (React)

Error boundaries catch React component errors and show a fallback UI instead of crashing the whole app:

```javascript
class ErrorBoundary extends React.Component {
  constructor(props) {
    super(props);
    this.state = { hasError: false, error: null };
  }

  static getDerivedStateFromError(error) {
    return { hasError: true, error };
  }

  componentDidCatch(error, errorInfo) {
    // Log error to monitoring service
    logErrorToService(error, errorInfo);
  }

  render() {
    if (this.state.hasError) {
      return <ErrorFallback error={this.state.error} />;
    }
    return this.props.children;
  }
}

// Wrap your app or parts of it
<ErrorBoundary>
  <App />
</ErrorBoundary>

```

**Why this matters**: One component crashing doesn't kill your entire app - users see an error message for that part, rest of app works.

### 🔹 Global Error Handler

Catch errors that slip through - unhandled errors and promise rejections:

```javascript
// Catch JavaScript errors
window.addEventListener('error', (event) => {
  logError({
    message: event.message,
    source: event.filename,
    line: event.lineno,
    column: event.colno,
    stack: event.error?.stack
  });
  // Optionally show user-friendly message
  showErrorNotification('An error occurred. We\'ve been notified.');
});

// Catch unhandled promise rejections
window.addEventListener('unhandledrejection', (event) => {
  logError({
    message: 'Unhandled promise rejection',
    error: event.reason,
    stack: event.reason?.stack
  });
});

```

**Why this matters**: Catches errors you might have missed, helps you debug production issues.

📌 **In simple terms**: Use try-catch for async operations, error boundaries for React components, and global handlers to catch everything else. Always show user-friendly messages and log errors for debugging.

---

## 2. ✅ Validation

Never trust user input or API responses - always validate. Validation catches problems early and gives users helpful feedback.

### 🔹 Form Validation with Zod

Zod makes validation easy and type-safe:

```javascript
import { z } from 'zod';

// Define what valid data looks like
const userSchema = z.object({
  name: z.string().min(1, 'Name is required'),
  email: z.string().email('Invalid email format'),
  age: z.number().min(18, 'Must be 18 or older').max(120, 'Invalid age'),
  password: z.string().min(8, 'Password must be at least 8 characters')
});

// Validate form data
const validateUser = (data) => {
  try {
    userSchema.parse(data); // Throws if invalid
    return { valid: true, errors: null };
  } catch (error) {
    return {
      valid: false,
      errors: error.errors // Array of validation errors
    };
  }
};

// Use in form
const handleSubmit = (formData) => {
  const result = validateUser(formData);
  if (!result.valid) {
    // Show errors to user
    setErrors(result.errors);
    return;
  }
  // Data is valid, proceed
  submitUser(formData);
};

```

**Why Zod is great**: Type-safe, clear error messages, works with TypeScript, handles complex validation rules.

### 🔹 Input Validation

Validate individual fields as user types (real-time validation):

```javascript
const validateEmail = (email) => {
  if (!email) {
    return 'Email is required';
  }
  const emailRegex = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
  if (!emailRegex.test(email)) {
    return 'Please enter a valid email address';
  }
  return null; // null means valid
};

const validatePassword = (password) => {
  if (!password) {
    return 'Password is required';
  }
  if (password.length < 8) {
    return 'Password must be at least 8 characters';
  }
  if (!/[A-Z]/.test(password)) {
    return 'Password must contain an uppercase letter';
  }
  if (!/[0-9]/.test(password)) {
    return 'Password must contain a number';
  }
  return null; // Valid
};

// Use in form component
const [email, setEmail] = useState('');
const [emailError, setEmailError] = useState(null);

const handleEmailChange = (value) => {
  setEmail(value);
  setEmailError(validateEmail(value)); // Validate on change
};

```

**Why this matters**: Users get immediate feedback, catch errors before submission, better UX.

📌 **In simple terms**: Always validate user input and API responses. Use Zod for complex validation, simple functions for individual fields. Validate on submit and optionally as user types.

---

## 3. 💡 Error Handling Best Practices

### 🔹 User-Friendly Messages

* Don't show technical error messages to users

* Provide actionable error messages

* Guide users on how to fix issues

### 🔹 Error Logging

* Log errors to monitoring service

* Include context (user, action, timestamp)

* Categorize errors by severity

### 🔹 Graceful Degradation

* App should continue working despite errors

* Show fallback UI when features fail

* Retry failed operations when appropriate

---

## ⭐ Summary — 10-second Interview Version

> "Error handling uses try-catch, error boundaries, and global handlers. Validation uses schemas (Zod) or custom functions. Provide user-friendly messages, log errors, and implement graceful degradation."

---

## ⭐ Extra Points (If Interviewer Asks More)

### How do you handle network errors?

Implement retry logic with exponential backoff, show offline indicators, cache data for offline use, and provide clear error messages to users.

### What's the difference between validation and sanitization?

Validation checks if data is correct (format, type, constraints). Sanitization cleans data to make it safe (remove scripts, escape HTML). Do both!

---

## Q52. ⚡ Performance Optimization Implementation

Performance optimization is about making your app faster - faster to load, faster to interact with, smoother animations. Users expect apps to be fast, and slow apps lose users. There are many techniques to improve performance, from code splitting to memoization to image optimization.

---

## 1. 💡 Code Splitting

Code splitting means only loading the code you need, when you need it. Instead of loading your entire app upfront (slow initial load), split it into chunks and load them on demand.

### 🔹 Route-Based Splitting

Split your app by routes - only load the code for the page the user is visiting:

```javascript
// ❌ Bad: Loads all pages upfront
import Home from './pages/Home';
import About from './pages/About';
import Contact from './pages/Contact';

// ✅ Good: Only loads when needed
const Home = lazy(() => import('./pages/Home'));
const About = lazy(() => import('./pages/About'));
const Contact = lazy(() => import('./pages/Contact'));

// Wrap in Suspense for loading state
<Suspense fallback={<Loading />}>
  <Routes>
    <Route path="/" element={<Home />} />
    <Route path="/about" element={<About />} />
    <Route path="/contact" element={<Contact />} />
  </Routes>
</Suspense>

```

**Why this matters**: Initial bundle is smaller, page loads faster. Users only download code for pages users visit.

### 🔹 Component-Based Splitting

Split heavy components that aren't always needed:

```javascript
// Heavy component (large library, complex logic)
const ChartComponent = lazy(() => import('./ChartComponent'));

function Dashboard() {
  const [showChart, setShowChart] = useState(false);

  return (
    <>
      <button onClick={() => setShowChart(true)}>Show Chart</button>
      {showChart && (
        <Suspense fallback={<ChartSkeleton />}>
          <ChartComponent /> {/* Only loads when user clicks */}
        </Suspense>
      )}
    </>
  );
}

```

**Why this matters**: Don't load heavy components until user needs them. Faster initial render.

📌 **In simple terms**: Code splitting loads code on demand instead of all at once. Split by routes (pages) or by components (heavy features). Use `lazy()` and `Suspense` in React.

---

## 2. 💡 Memoization

Memoization means remembering computed values so you don't have to recompute them. React has several memoization tools to prevent unnecessary work.

### 🔹 React.memo

Prevents component from re-rendering if props haven't changed:

```javascript
// Without memo - re-renders every time parent re-renders
const ExpensiveComponent = ({ data }) => {
  // Expensive rendering logic
  return <div>{/* complex render */}</div>;
};

// With memo - only re-renders if props actually change
const ExpensiveComponent = React.memo(({ data }) => {
  return <div>{/* complex render */}</div>;
});

// Now parent can re-render without causing this to re-render

```

**When to use**: Components that are expensive to render and receive props that don't change often.

### 🔹 useMemo

Memoizes computed values - only recomputes when dependencies change:

```javascript
// Without useMemo - recomputes on every render
function ProductList({ products, filter }) {
  const filteredProducts = products.filter(p => p.category === filter);
  // This runs every render, even if products and filter didn't change
  return <div>{/* render */}</div>;
}

// With useMemo - only recomputes when dependencies change
function ProductList({ products, filter }) {
  const filteredProducts = useMemo(() => {
    return products.filter(p => p.category === filter);
  }, [products, filter]); // Only recompute if products or filter changes

  return <div>{/* render */}</div>;
}

```

**When to use**: Expensive computations (filtering, sorting, calculations) that depend on props/state.

### 🔹 useCallback

Memoizes functions - prevents recreating function on every render:

```javascript
// Without useCallback - new function every render
function Parent() {
  const [count, setCount] = useState(0);

  const handleClick = () => {
    console.log('clicked');
  };
  // New function every render - causes Child to re-render

  return <Child onClick={handleClick} />;
}

// With useCallback - same function unless dependencies change
function Parent() {
  const [count, setCount] = useState(0);

  const handleClick = useCallback(() => {
    console.log('clicked');
  }, []); // Same function every render

  return <Child onClick={handleClick} />; // Child won't re-render unnecessarily
}

```

**When to use**: Functions passed as props to memoized components, or functions in dependency arrays.

📌 **In simple terms**: Memoization prevents unnecessary work. `React.memo` for components, `useMemo` for values, `useCallback` for functions. Use when re-rendering/recomputing is expensive.

---

## 3. 💡 Virtualization

### 🔹 React Window

```javascript
import { FixedSizeList } from 'react-window';

function VirtualizedList({ items }) {
  return (
    <FixedSizeList
      height={600}
      itemCount={items.length}
      itemSize={50}
      width="100%"
    >
      {({ index, style }) => (
        <div style={style}>
          {items[index].name}
        </div>
      )}
    </FixedSizeList>
  );
}

```

---

## 4. 💡 Image Optimization

### 🔹 Lazy Loading

```javascript
<img
  src={imageSrc}
  loading="lazy"
  alt="Description"
/>

```

### 🔹 Responsive Images

```javascript
<img
  srcSet="image-320w.jpg 320w,
          image-640w.jpg 640w,
          image-1024w.jpg 1024w"
  sizes="(max-width: 640px) 320px,
         (max-width: 1024px) 640px,
         1024px"
  src="image-1024w.jpg"
  alt="Description"
/>

```

---

## ⭐ Summary — 10-second Interview Version

> "Performance optimization includes code splitting (lazy loading), memoization (React.memo, useMemo, useCallback), virtualization for long lists, and image optimization (lazy loading, responsive images)."

---

## ⭐ Extra Points (If Interviewer Asks More)

### How do you identify performance bottlenecks?

Use React DevTools Profiler, Chrome DevTools Performance tab, Lighthouse audits, and monitor Core Web Vitals in production.

### What is the difference between useMemo and useCallback?

useMemo memoizes computed values. useCallback memoizes functions. Both prevent unnecessary recalculations/recreations.

---

## Q53. 🛡️ Security Implementation

Security is about protecting your app and users from attacks. Frontend security focuses on preventing common vulnerabilities like XSS, CSRF, and ensuring sensitive data is handled safely. Security isn't optional - it's essential.

---

## 1. 🎯 XSS Prevention

### 🔹 Sanitize User Input

```javascript
import DOMPurify from 'dompurify';

const userContent = userInput;
const sanitized = DOMPurify.sanitize(userContent);
dangerouslySetInnerHTML={{ __html: sanitized }}

```

### 🔹 Use Safe APIs

```javascript
// ❌ Dangerous
element.innerHTML = userInput;

// ✅ Safe
element.textContent = userInput;

```

---

## 2. 💡 CSRF Protection

### 🔹 CSRF Tokens

```javascript
// Get token from server
const csrfToken = await fetch('/api/csrf-token').then(r => r.json());

// Include in requests
fetch('/api/users', {
  method: 'POST',
  headers: {
    'X-CSRF-Token': csrfToken
  },
  body: JSON.stringify(data)
});

```

---

## 3. 💡 Secure Storage

### 🔹 Don't Store Sensitive Data

```javascript
// ❌ Never store tokens in localStorage
localStorage.setItem('token', token);

// ✅ Use httpOnly cookies (backend sets)
// Or use secure, short-lived storage
sessionStorage.setItem('tempToken', token);

```

---

## 4. 🛡️ Content Security Policy

```javascript
// meta tag or HTTP header
<meta
  httpEquiv="Content-Security-Policy"
  content="default-src 'self'; script-src 'self' 'unsafe-inline';"
/>

```

---

## ⭐ Summary — 10-second Interview Version

> "Security implementation includes XSS prevention (sanitize input, use safe APIs), CSRF tokens, secure storage (avoid localStorage for tokens), and Content Security Policy headers."

---

## ⭐ Extra Points (If Interviewer Asks More)

### How do you handle authentication tokens securely?

Use httpOnly cookies set by backend, or store short-lived tokens in memory. Never store long-lived tokens in localStorage. Implement token refresh.

### What is the difference between XSS and CSRF?

XSS injects malicious scripts into your page. CSRF tricks users into making unwanted requests. Both need different defenses.

---

## Q54. 🧪 Testing Implementation

Testing is about making sure your code works correctly and doesn't break when you make changes. Good tests catch bugs early, give you confidence to refactor, and serve as documentation. There are different types of tests for different purposes - unit tests, integration tests, and end-to-end tests.

---

## 1. 🧪 Unit Testing

Unit tests test individual pieces of code in isolation - one component, one function, one module. These tests are fast, easy to write, and catch bugs early.

### 🔹 Component Testing

Test React components - what these components render and how these components behave:

```javascript
import { render, screen, fireEvent } from '@testing-library/react';
import Button from './Button';

test('renders button with text', () => {
  render(<Button>Click me</Button>);
  expect(screen.getByText('Click me')).toBeInTheDocument();
});

test('calls onClick when clicked', () => {
  const handleClick = jest.fn(); // Mock function
  render(<Button onClick={handleClick}>Click</Button>);
  fireEvent.click(screen.getByText('Click'));
  expect(handleClick).toHaveBeenCalledTimes(1); // Verify it was called
});

```

**Why React Testing Library**: Tests components like users interact with them (find by text, click buttons), not implementation details.

### 🔹 Function Testing

Test utility functions, helpers, business logic:

```javascript
import { validateEmail, formatCurrency } from './utils';

test('validates email correctly', () => {
  expect(validateEmail('test@example.com')).toBe(true);
  expect(validateEmail('invalid')).toBe(false);
  expect(validateEmail('')).toBe(false);
});

test('formats currency correctly', () => {
  expect(formatCurrency(1000)).toBe('$1,000.00');
  expect(formatCurrency(0)).toBe('$0.00');
});

```

**Why this matters**: Test pure functions easily - same input always gives same output, easy to test edge cases.

📌 **In simple terms**: Unit tests test one thing at a time in isolation. Test components (what these components render, how these components behave) and functions (do these functions return correct values). Fast and easy to write.

---

## 2. 🧪 Integration Testing

Integration tests test how multiple pieces work together - components talking to each other, components using services, API calls.

```javascript
import { render, screen, waitFor } from '@testing-library/react';
import UserProfile from './UserProfile';

// Mock the API service
jest.mock('./userService', () => ({
  getUser: jest.fn(() => Promise.resolve({ name: 'John Doe', email: 'john@example.com' }))
}));

test('loads and displays user data', async () => {
  render(<UserProfile userId="123" />);

  // Test loading state
  expect(screen.getByText('Loading...')).toBeInTheDocument();

  // Wait for data to load and verify it displays
  await waitFor(() => {
    expect(screen.getByText('John Doe')).toBeInTheDocument();
    expect(screen.getByText('john@example.com')).toBeInTheDocument();
  });
});

```

**Why integration tests**: Catch bugs in how components work together - data flow, state updates, API integration.

---

## 3. 🧪 E2E Testing

End-to-end tests test the entire user flow - like a real user using your app. These tests verify the whole stack (frontend + backend).

```javascript
// Cypress - tests real browser interactions
describe('User Login Flow', () => {
  it('should login successfully', () => {
    cy.visit('/login');
    cy.get('[data-testid="email"]').type('user@example.com');
    cy.get('[data-testid="password"]').type('password');
    cy.get('[data-testid="submit"]').click();
    cy.url().should('include', '/dashboard');
    cy.get('[data-testid="welcome-message"]').should('contain', 'Welcome');
  });

  it('should show error for invalid credentials', () => {
    cy.visit('/login');
    cy.get('[data-testid="email"]').type('wrong@example.com');
    cy.get('[data-testid="password"]').type('wrong');
    cy.get('[data-testid="submit"]').click();
    cy.get('[data-testid="error"]').should('contain', 'Invalid credentials');
  });
});

```

**Why E2E tests**: Test real user flows, catch issues that unit/integration tests miss, confidence that the whole app works.

📌 **In simple terms**: Integration tests verify components work together. E2E tests verify complete user flows work end-to-end. Use all three types - these tests catch different problems.

---

## 4. 🧪 Testing Best Practices

### 🔹 Test Structure (AAA Pattern)

Follow the Arrange-Act-Assert pattern for clear, readable tests:

```javascript
test('should calculate total correctly', () => {
  // Arrange: Set up test data
  const items = [
    { price: 10, quantity: 2 },
    { price: 5, quantity: 3 }
  ];

  // Act: Execute the code being tested
  const total = calculateTotal(items);

  // Assert: Verify the results
  expect(total).toBe(35);
});

```

**Why this matters**: Makes tests easy to read and understand - clear what's being tested and what's expected.

### 🔹 Test Coverage

* **Aim for high coverage**: But don't obsess over 100% - focus on critical paths

* **Test edge cases**: Empty arrays, null values, boundary conditions

* **Test error conditions**: What happens when things go wrong?

* **Don't test implementation details**: Test behavior, not how it's implemented

### 🔹 Mocking

Mock external dependencies to isolate what you're testing:

```javascript
// Mock API calls
jest.mock('./api', () => ({
  fetchUser: jest.fn(() => Promise.resolve({ name: 'John' }))
}));

// Mock timers
jest.useFakeTimers();

// Mock modules
jest.mock('react-router-dom', () => ({
  useNavigate: () => jest.fn()
}));

```

**Why mocking**: Isolate the code you're testing, make tests fast and reliable, control external dependencies.

📌 **In simple terms**: Follow AAA pattern (Arrange, Act, Assert). Focus on critical paths and edge cases. Mock external dependencies to isolate what you're testing. Test behavior, not implementation.

---

## ⭐ Summary — 10-second Interview Version

> "Testing includes unit tests (components, functions), integration tests (component interactions), and E2E tests (full user flows). Use testing libraries like Jest, React Testing Library, and Cypress. Follow AAA pattern (Arrange, Act, Assert)."

---

## ⭐ Extra Points (If Interviewer Asks More)

### How do you test async code?

Use async/await with waitFor, mock async functions, and test loading and error states separately from success states.

### What's the difference between unit and integration tests?

Unit tests test individual components/functions in isolation. Integration tests test how multiple components work together.

---

---

## 📍 Navigation

<div align="center">

[← Previous: High Level Design](14%29%20High%20Level%20Design.md) • [Home: Questions Index](question.md) • [Next: Security →](16%29%20Security.md)

[📋 Cheatsheet](FE-System-Design%20Interview%20Cheatsheet.md)

</div>

---
