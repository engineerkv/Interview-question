# ⚛️ React.js Interview Notes (2025 Edition)

## 🔄 Section 3 — State Management (Local  Global  Server) — Q51-Q76

---

### 51. 🔄 What is state management in React?

**🧠 Concept**

State management is how you store, update, and share data across your React application components.

**💻 Example**
```jsx
// Local state
const [count, setCount] = useState(0);

// Global state (Context)
const { user } = useContext(AuthContext);
```

**💬 Explanation + Insight**

- **Local State** - Data that belongs to one component
- **Shared State** - Data that multiple components need
- **Global State** - Data that the whole app needs
- **Server State** - Data that comes from APIs
- **Right Tool** - Choose the right tool for the right job

---

### 52. 🔄 What is prop drilling, and how can you avoid it?

**🧠 Concept**

Prop drilling happens when you pass data through many components that don't need it, just to get it to a deeply nested component.

**💻 Example**
```jsx
// ❌ Prop drilling
<App user={user}>
  <Header user={user}>
    <Nav user={user}>
      <UserMenu user={user} />
    </Nav>
  </Header>
</App>

// ✅ Context solution
<UserContext.Provider value={user}>
  <App>
    <Header>
      <Nav>
        <UserMenu /> {/* Gets user from context */}
      </Nav>
    </Header>
  </App>
</UserContext.Provider>
```

**💬 Explanation + Insight**

- Like passing a message through many people to reach the right person
- Makes components tightly connected and hard to change
- Use Context API, Redux, or other state management tools
- Components get data directly instead of through props
- Makes code cleaner and easier to maintain

---

### 53. 🔄 What is Context API, and how does it work internally?

**🧠 Concept**

Context API is React's built-in way to share data between components without passing props through every level.

**💻 Example**
```jsx
const ThemeContext = createContext('light');

function App() {
  return (
    <ThemeContext.Provider value="dark">
      <Header />
    </ThemeContext.Provider>
  );
}

function Header() {
  const theme = useContext(ThemeContext);
  return <div className={theme}>Header</div>;
}
```

**💬 Explanation + Insight**

- Like a data tunnel that skips intermediate components
- Provider gives data, Consumer (or useContext) gets data
- Perfect for theme, language, user data that many components need
- When context changes, all components using it re-render
- Don't use for data that changes frequently (causes performance issues)

---

### 54. 🔄 What are the limitations of Context API?

**🧠 Concept**

Context API has some limitations that make it not great for complex state management.

**💻 Example**
```jsx
// ❌ Problem: All consumers re-render when any value changes
const AppContext = createContext({
  user: null,
  theme: 'light',
  notifications: []
});

// ✅ Solution: Split contexts
const UserContext = createContext();
const ThemeContext = createContext();
const NotificationContext = createContext();
```

📝 **Deeper Insight**

Limitations include:
- **No built-in selectors** (all consumers re-render)
- **No middleware** for side effects
- **No time-travel debugging**
- **No devtools integration**
- **Performance issues** with frequent updates
- **No built-in persistence**

---

### 55. 🔄 What is Redux, and how does it manage global state?

🧠 **Concept**

Redux is a **predictable state container** that manages global application state using a unidirectional data flow pattern.

💻 **Example**

```jsx
// Store
const store = createStore(reducer);

// Action
const increment = () => ({ type: 'INCREMENT' });

// Reducer
function reducer(state = { count: 0 }, action) {
  switch (action.type) {
    case 'INCREMENT':
      return { count: state.count + 1 };
    default:
      return state;
  }
}
```

📝 **Deeper Insight**

Redux follows three principles:
1. **Single source of truth** (one store)
2. **State is read-only** (actions only)
3. **Changes via pure functions** (reducers)

---

### 56. 🔄 What are actions, reducers, and stores in Redux?

🧠 **Concept**

- **Actions**  plain objects describing what happened
- **Reducers**  pure functions that specify how state changes
- **Store**  holds the complete state tree

💻 **Example**

```jsx
// Action
const addTodo = (text) => ({
  type: 'ADD_TODO',
  payload: { text, id: Date.now() }
});

// Reducer
function todosReducer(state = [], action) {
  switch (action.type) {
    case 'ADD_TODO':
      return [...state, action.payload];
    default:
      return state;
  }
}

// Store
const store = createStore(todosReducer);
```

📝 **Deeper Insight**

- **Actions** must have a `type` property
- **Reducers** must be pure (no side effects)
- **Store** provides `getState()`, `dispatch()`, and `subscribe()`

---

### 57. 🔄 What is Redux Toolkit (RTK), and how is it different from classic Redux?

🧠 **Concept**

Redux Toolkit is the **official, opinionated way** to write Redux logic with less boilerplate and better developer experience.

💻 **Example**

```jsx
// Classic Redux
const ADD_TODO = 'ADD_TODO';
const addTodo = (text) => ({ type: ADD_TODO, payload: text });
function todosReducer(state = [], action) {
  switch (action.type) {
    case ADD_TODO:
      return [...state, action.payload];
    default:
      return state;
  }
}

// Redux Toolkit
const todosSlice = createSlice({
  name: 'todos',
  initialState: [],
  reducers: {
    addTodo: (state, action) => {
      state.push(action.payload);
    }
  }
});
```

📝 **Deeper Insight**

RTK provides:
- **createSlice** for reducers and actions
- **configureStore** with good defaults
- **createAsyncThunk** for async logic
- **Immer integration** for immutable updates
- **DevTools** and **middleware** pre-configured

---

### 58. 🔄 What are selectors in Redux?

🧠 **Concept**

Selectors are **functions that extract specific pieces** of state from the Redux store, often with memoization for performance.

💻 **Example**

```jsx
// Basic selector
const selectTodos = (state) => state.todos;

// Memoized selector with reselect
const selectVisibleTodos = createSelector(
  [selectTodos, (state, filter) => filter],
  (todos, filter) => {
    switch (filter) {
      case 'SHOW_COMPLETED':
        return todos.filter(todo => todo.completed);
      case 'SHOW_ACTIVE':
        return todos.filter(todo => !todo.completed);
      default:
        return todos;
    }
  }
);
```

📝 **Deeper Insight**
Selectors help with:
- **Performance** (memoization prevents unnecessary recalculations)
- **Encapsulation** (hiding state structure)
- **Reusability** (same logic across components)
- **Testing** (pure functions are easy to test)

---

### 59. 🔄 What is the difference between Redux Thunk and Redux Saga?

🧠 **Concept**

Both handle async operations in Redux, but with different approaches:
- **Redux Thunk**  simple functions that can dispatch actions
- **Redux Saga**  uses generators for complex async flows

💻 **Example**

```jsx
// Redux Thunk
const fetchUser = (id) => async (dispatch) => {
  dispatch({ type: 'FETCH_USER_START' });
  try {
    const user = await api.getUser(id);
    dispatch({ type: 'FETCH_USER_SUCCESS', payload: user });
  } catch (error) {
    dispatch({ type: 'FETCH_USER_ERROR', payload: error });
  }
};

// Redux Saga
function* fetchUserSaga(action) {
  try {
    yield put({ type: 'FETCH_USER_START' });
    const user = yield call(api.getUser, action.payload);
    yield put({ type: 'FETCH_USER_SUCCESS', payload: user });
  } catch (error) {
    yield put({ type: 'FETCH_USER_ERROR', payload: error });
  }
}
```

📝 **Deeper Insight**
- **Thunk** is simpler but limited for complex flows
- **Saga** is powerful for complex async patterns (cancellation, race conditions, etc.)
- **RTK Query** is now preferred for data fetching

---

### 60. 🔄 What are Recoil and Zustand, and how do they differ from Redux?

🧠 **Concept**

Modern alternatives to Redux with different philosophies:
- **Recoil**  Facebook's atomic state management
- **Zustand**  minimal, unopinionated state management

💻 **Example**

```jsx
// Recoil
const countState = atom({
  key: 'countState',
  default: 0
});

function Counter() {
  const [count, setCount] = useRecoilState(countState);
  return <button onClick={() => setCount(count + 1)}>{count}</button>;
}

// Zustand
const useStore = create((set) => ({
  count: 0,
  increment: () => set((state) => ({ count: state.count + 1 }))
}));

function Counter() {
  const { count, increment } = useStore();
  return <button onClick={increment}>{count}</button>;
}
```

📝 **Deeper Insight**
- **Recoil**  atomic, fine-grained reactivity
- **Zustand**  minimal boilerplate, TypeScript-friendly
- **Redux**  predictable, time-travel debugging, ecosystem

---

### 61. 🔄 What is Jotai, and when should it be used?

🧠 **Concept**

Jotai is an **atomic state management library** that provides fine-grained reactivity with minimal re-renders.

💻 **Example**

```jsx
import { atom, useAtom } from 'jotai';

const countAtom = atom(0);
const doubledAtom = atom((get) => get(countAtom) * 2);

function Counter() {
  const [count, setCount] = useAtom(countAtom);
  const doubled = useAtomValue(doubledAtom);
  
  return (
    <div>
      <button onClick={() => setCount(count + 1)}>{count}</button>
      <p>Doubled: {doubled}</p>
    </div>
  );
}
```

📝 **Deeper Insight**
Jotai is ideal for:
- **Fine-grained updates** (only affected components re-render)
- **Derived state** (computed values)
- **TypeScript** projects
- **Performance-critical** applications

---

### 62. 🔄 What is MobX, and how does it differ from Redux?

🧠 **Concept**

MobX is a **reactive state management** library that automatically tracks and updates components when observable data changes.

💻 **Example**

```jsx
import { makeAutoObservable } from 'mobx';
import { observer } from 'mobx-react-lite';

class TodoStore {
  todos = [];
  
  constructor() {
    makeAutoObservable(this);
  }
  
  addTodo(text) {
    this.todos.push({ text, completed: false });
  }
}

const store = new TodoStore();

const TodoList = observer(() => (
  <div>
    {store.todos.map(todo => <div key={todo.text}>{todo.text}</div>)}
    <button onClick={() => store.addTodo('New todo')}>Add</button>
  </div>
));
```

📝 **Deeper Insight**
MobX vs Redux:
- **MobX**  mutable state, automatic updates, less boilerplate
- **Redux**  immutable state, explicit updates, more predictable

---

### 63. 🔄 What are derived and computed states?

🧠 **Concept**

Derived state is **automatically calculated** from other state values, eliminating the need to manually sync related data.

💻 **Example**

```jsx
// Manual derived state (error-prone)
const [todos, setTodos] = useState([]);
const [completedCount, setCompletedCount] = useState(0);

// Automatic derived state
const completedCount = useMemo(() => 
  todos.filter(todo => todo.completed).length, 
  [todos]
);
```

📝 **Deeper Insight**
Benefits of derived state:
- **Single source of truth** for base data
- **Automatic updates** when dependencies change
- **No sync bugs** between related values
- **Performance optimization** with memoization

---

### 64. 🔄 What are global vs local vs server states?

🧠 **Concept**

Different types of state serve different purposes in React applications.

💻 **Example**

```jsx
// Local state (component-specific)
const [isOpen, setIsOpen] = useState(false);

// Global state (app-wide)
const { user } = useContext(AuthContext);

// Server state (external data)
const { data: posts, isLoading } = useQuery('posts', fetchPosts);
```

📝 **Deeper Insight**
- **Local state**  component-specific, short-lived
- **Global state**  shared across components, persistent
- **Server state**  external data, caching, synchronization

---

### 65. 🔄 What is React Query (TanStack Query), and how does it handle async state?

🧠 **Concept**

React Query is a **data fetching and caching library** that manages server state with built-in caching, synchronization, and background updates.

💻 **Example**

```jsx
import { useQuery, useMutation, useQueryClient } from '@tanstack/react-query';

function Posts() {
  const { data: posts, isLoading, error } = useQuery({
    queryKey: ['posts'],
    queryFn: fetchPosts,
    staleTime: 5 * 60 * 1000, // 5 minutes
  });

  const queryClient = useQueryClient();
  
  const addPost = useMutation({
    mutationFn: createPost,
    onSuccess: () => {
      queryClient.invalidateQueries(['posts']);
    }
  });

  if (isLoading) return 'Loading...';
  if (error) return 'Error!';
  
  return (
    <div>
      {posts.map(post => <div key={post.id}>{post.title}</div>)}
    </div>
  );
}
```

📝 **Deeper Insight**
React Query provides:
- **Automatic caching** and background updates
- **Optimistic updates** and rollback
- **Request deduplication**
- **Offline support**
- **DevTools** integration

---

### 66. 🔄 What is SWR, and how does it differ from React Query?

🧠 **Concept**

SWR is a **lightweight data fetching library** focused on caching and revalidation, while React Query is more feature-complete.

💻 **Example**

```jsx
// SWR
import useSWR from 'swr';

function Profile() {
  const { data, error, isLoading } = useSWR('/api/user', fetcher);
  
  if (error) return <div>Failed to load</div>;
  if (isLoading) return <div>Loading...</div>;
  return <div>Hello {data.name}!</div>;
}

// React Query
const { data, error, isLoading } = useQuery({
  queryKey: ['user'],
  queryFn: () => fetch('/api/user').then(res => res.json())
});
```

📝 **Deeper Insight**
- **SWR**  simpler, smaller bundle, Vercel-backed
- **React Query**  more features, better TypeScript, larger ecosystem

---

### 67. 🔄 What are optimistic updates, and when should you use them?

🧠 **Concept**

Optimistic updates **immediately update the UI** before the server confirms the change, providing instant feedback to users.

💻 **Example**

```jsx
const updateTodo = useMutation({
  mutationFn: updateTodoAPI,
  onMutate: async (newTodo) => {
    // Cancel outgoing refetches
    await queryClient.cancelQueries(['todos']);
    
    // Snapshot previous value
    const previousTodos = queryClient.getQueryData(['todos']);
    
    // Optimistically update
    queryClient.setQueryData(['todos'], old => 
      old.map(todo => todo.id === newTodo.id ? newTodo : todo)
    );
    
    return { previousTodos };
  },
  onError: (err, newTodo, context) => {
    // Rollback on error
    queryClient.setQueryData(['todos'], context.previousTodos);
  }
});
```

📝 **Deeper Insight**
Use optimistic updates for:
- **Better UX** (instant feedback)
- **Network latency** compensation
- **High-frequency interactions** (likes, toggles)

---

### 68. 🔄 How do you persist state across sessions?

🧠 **Concept**

State persistence saves application state to **localStorage, sessionStorage, or external storage** to survive page refreshes and browser sessions.

💻 **Example**

```jsx
// Custom hook for persistence
function usePersistedState(key, defaultValue) {
  const [state, setState] = useState(() => {
    const saved = localStorage.getItem(key);
    return saved ? JSON.parse(saved) : defaultValue;
  });

  useEffect(() => {
    localStorage.setItem(key, JSON.stringify(state));
  }, [key, state]);

  return [state, setState];
}

// Usage
const [theme, setTheme] = usePersistedState('theme', 'light');
```

📝 **Deeper Insight**
Persistence strategies:
- **localStorage**  survives browser restarts
- **sessionStorage**  survives page refreshes
- **IndexedDB**  large data, complex queries
- **Server persistence**  cross-device sync

---

### 69. 🔄 How do you share state between unrelated components?

🧠 **Concept**

Unrelated components can share state through **global state management** solutions that don't require prop drilling.

💻 **Example**

```jsx
// Context API
const AppStateContext = createContext();

function App() {
  const [user, setUser] = useState(null);
  return (
    <AppStateContext.Provider value={{ user, setUser }}>
      <Header />
      <Sidebar />
    </AppStateContext.Provider>
  );
}

// Zustand
const useStore = create((set) => ({
  user: null,
  setUser: (user) => set({ user })
}));

function Header() {
  const { user } = useStore();
  return <div>Welcome {user?.name}</div>;
}
```

📝 **Deeper Insight**
Solutions for unrelated components:
- **Context API** (React built-in)
- **State management libraries** (Redux, Zustand, Jotai)
- **Event emitters** (custom solutions)
- **URL state** (for shareable state)

---

### 70. 🔄 What are common state management anti-patterns?

🧠 **Concept**

Anti-patterns are **common mistakes** that lead to bugs, performance issues, and maintainability problems in state management.

💻 **Example**

```jsx
// ❌ Anti-pattern: Mutating state directly
const [todos, setTodos] = useState([]);
const addTodo = (text) => {
  todos.push({ text }); // Mutating!
  setTodos(todos);
};

// ✅ Correct: Immutable updates
const addTodo = (text) => {
  setTodos(prev => [...prev, { text }]);
};

// ❌ Anti-pattern: Storing derived state
const [todos, setTodos] = useState([]);
const [completedCount, setCompletedCount] = useState(0);

// ✅ Correct: Derive state
const completedCount = todos.filter(todo => todo.completed).length;
```

📝 **Deeper Insight**
Common anti-patterns:
- **Mutating state** directly
- **Storing derived state** instead of computing it
- **Over-normalizing** state structure
- **Prop drilling** instead of proper state management
- **Mixing concerns** in state (UI + data)
- **Not handling loading/error states**

---

### 71. 🔄 What are Redux middleware, and how do they work?

🧠 **Concept**


Redux middleware is a **function that sits between dispatching an action and the moment it reaches the reducer**, allowing you to intercept, modify, or enhance actions.

💻 **Example**

```javascript
// Custom middleware
const loggerMiddleware = (store) => (next) => (action) => {
  console.log('Dispatching:', action);
  const result = next(action);
  console.log('New state:', store.getState());
  return result;
};

// Apply middleware
const store = createStore(
  rootReducer,
  applyMiddleware(loggerMiddleware, thunk)
);
```

📝 **Deeper Insight**

Middleware provides a **third-party extension point** between dispatching an action and the moment it reaches the reducer:
- **Order matters** - middleware executes in the order it's applied
- **Can modify actions** before they reach reducers
- **Can dispatch additional actions**
- **Can access store state** and dispatch function
- **Common middleware**: Redux Thunk, Redux Saga, Redux Logger

---

### 72. 🔄 What is Redux Toolkit (RTK), and how does it simplify Redux?

🧠 **Concept**


Redux Toolkit is the **official, opinionated, batteries-included toolset** for efficient Redux development, providing utilities to simplify common Redux patterns.

💻 **Example**

```javascript
// ❌ Traditional Redux (verbose)
const ADD_TODO = 'ADD_TODO';
const addTodo = (text) => ({ type: ADD_TODO, payload: text });
const todosReducer = (state = [], action) => {
  switch (action.type) {
    case ADD_TODO:
      return [...state, { text: action.payload, completed: false }];
    default:
      return state;
  }
};

// ✅ Redux Toolkit (concise)
import { createSlice } from '@reduxjs/toolkit';

const todosSlice = createSlice({
  name: 'todos',
  initialState: [],
  reducers: {
    addTodo: (state, action) => {
      state.push({ text: action.payload, completed: false });
    }
  }
});
```

📝 **Deeper Insight**

RTK provides:
- **createSlice** - generates actions and reducers
- **configureStore** - simplified store setup
- **createAsyncThunk** - handles async operations
- **Immer integration** - allows "mutating" state safely
- **DevTools integration** - automatic setup
- **TypeScript support** - better type safety

---

### 73. 🔄 What are Redux slices, and how do they organize state?

🧠 **Concept**


A Redux slice is a **collection of Redux reducer logic and actions** for a specific feature, automatically generating action creators and action types.

💻 **Example**

```javascript
import { createSlice } from '@reduxjs/toolkit';

const counterSlice = createSlice({
  name: 'counter',
  initialState: { value: 0 },
  reducers: {
    increment: (state) => {
      state.value += 1;
    },
    decrement: (state) => {
      state.value -= 1;
    },
    incrementByAmount: (state, action) => {
      state.value += action.payload;
    }
  }
});

// Auto-generated actions
export const { increment, decrement, incrementByAmount } = counterSlice.actions;
export default counterSlice.reducer;
```

📝 **Deeper Insight**

Slices provide:
- **Automatic action type generation** (counter/increment)
- **Immer integration** - safe state mutations
- **Action creators** - functions to dispatch actions
- **Feature organization** - group related logic
- **TypeScript support** - better type inference
- **Redux DevTools** - automatic integration

---

### 74. 🔄 How do you handle async operations with Redux Toolkit?

🧠 **Concept**


Redux Toolkit provides **createAsyncThunk** to handle async operations like API calls, automatically managing loading, success, and error states.

💻 **Example**

```javascript
import { createSlice, createAsyncThunk } from '@reduxjs/toolkit';

// Async thunk
export const fetchUser = createAsyncThunk(
  'user/fetchUser',
  async (userId, { rejectWithValue }) => {
    try {
      const response = await api.getUser(userId);
      return response.data;
    } catch (error) {
      return rejectWithValue(error.message);
    }
  }
);

const userSlice = createSlice({
  name: 'user',
  initialState: {
    data: null,
    loading: false,
    error: null
  },
  reducers: {
    clearError: (state) => {
      state.error = null;
    }
  },
  extraReducers: (builder) => {
    builder
      .addCase(fetchUser.pending, (state) => {
        state.loading = true;
        state.error = null;
      })
      .addCase(fetchUser.fulfilled, (state, action) => {
        state.loading = false;
        state.data = action.payload;
      })
      .addCase(fetchUser.rejected, (state, action) => {
        state.loading = false;
        state.error = action.payload;
      });
  }
});
```

📝 **Deeper Insight**

createAsyncThunk provides:
- **Automatic action types** - pending, fulfilled, rejected
- **Loading state management** - built-in loading flags
- **Error handling** - automatic error state
- **Payload handling** - success and error payloads
- **Cancellation support** - abort requests
- **TypeScript support** - type-safe async operations

---

### 75. 🔄 What is the difference between Redux Thunk and Redux Saga?

🧠 **Concept**


Redux Thunk and Redux Saga are both **middleware for handling side effects** in Redux, but they use different approaches for managing async operations.

💻 **Example**

```javascript
// Redux Thunk (function-based)
const fetchUser = (userId) => async (dispatch, getState) => {
  dispatch({ type: 'FETCH_USER_START' });
  try {
    const user = await api.getUser(userId);
    dispatch({ type: 'FETCH_USER_SUCCESS', payload: user });
  } catch (error) {
    dispatch({ type: 'FETCH_USER_ERROR', payload: error.message });
  }
};

// Redux Saga (generator-based)
function* fetchUserSaga(action) {
  try {
    yield put({ type: 'FETCH_USER_START' });
    const user = yield call(api.getUser, action.payload);
    yield put({ type: 'FETCH_USER_SUCCESS', payload: user });
  } catch (error) {
    yield put({ type: 'FETCH_USER_ERROR', payload: error.message });
  }
}
```

📝 **Deeper Insight**

**Redux Thunk:**
- **Function-based** - simple async functions
- **Easy to learn** - minimal concepts
- **Good for simple cases** - basic async operations
- **Less boilerplate** - straightforward implementation

**Redux Saga:**
- **Generator-based** - uses ES6 generators
- **More powerful** - complex async flows
- **Better testing** - easier to test generators
- **More features** - cancellation, debouncing, etc.

---

### 76. 🔄 How do you create custom Redux middleware?

🧠 **Concept**


Custom Redux middleware is a **function that follows the middleware pattern** (store) => (next) => (action) => result, allowing you to intercept and modify actions.

💻 **Example**

```javascript
// Custom middleware for API calls
const apiMiddleware = (store) => (next) => (action) => {
  if (action.type.endsWith('_REQUEST')) {
    // Add loading state
    store.dispatch({ type: 'SET_LOADING', payload: true });
  }
  
  if (action.type.endsWith('_SUCCESS') || action.type.endsWith('_ERROR')) {
    // Remove loading state
    store.dispatch({ type: 'SET_LOADING', payload: false });
  }
  
  return next(action);
};

// Middleware for logging
const loggerMiddleware = (store) => (next) => (action) => {
  console.group(`Action: ${action.type}`);
  console.log('Previous state:', store.getState());
  console.log('Action:', action);
  const result = next(action);
  console.log('Next state:', store.getState());
  console.groupEnd();
  return result;
};
```

📝 **Deeper Insight**

Middleware pattern:
- **store** - Redux store instance
- **next** - next middleware in chain
- **action** - dispatched action
- **return** - result of next middleware
- **Can modify actions** before they reach reducers
- **Can dispatch additional actions**
- **Can access store state** and dispatch function

---
