---
sidebar_label: "State Management"
---
# 🗂️ 3. State Management (Q39–49)

---

## Q39. 🔌 Context API and how to use it

Context API shares data across the component tree without prop drilling - use it for global data like themes, user info, or language settings that many components need. Context shares data globally without prop drilling through multiple levels.

- **Trade-offs**: The catch is creating new context values every render causes unnecessary re-renders - memoize context value with useMemo to prevent performance issues. Context solves prop drilling but isn't a replacement for Redux, so use wisely, but watch out - context updates cause all consumers to re-render, which can be expensive.

Example:

```jsx
// Create context for sharing theme data
const ThemeContext = createContext();

// Provider component: wraps app to share context value
function ThemeProvider({ children }) {
  const [theme, setTheme] = useState('light'); // State managed in provider
  return (
    <ThemeContext.Provider value={{ theme, setTheme }}>
      {children} {/* All children can access context */}
    </ThemeContext.Provider>
  );
}

// Consumer component: accesses context without prop drilling
function ThemedButton() {
  const { theme, setTheme } = useContext(ThemeContext); // Get context value
  return (
    <button onClick={() => setTheme(theme === 'light' ? 'dark' : 'light')}>
      Toggle
    </button>
  );
}

```

---

## Q40. 🔧 Redux and how it works

Redux manages app state in one store using actions and reducers - it follows unidirectional data flow for predictable updates, making state changes traceable and debuggable. Actions describe changes, reducers update state, store holds everything.

- **Trade-offs**: The catch is using Redux for simple apps - it adds complexity without benefit, same state and action always produce same result, enabling predictable debugging. Unidirectional flow (action → reducer → store → component) keeps state predictable, but watch out - Redux adds boilerplate, so only use it when you need the benefits.

Example:

```jsx
// Reducer: pure function that updates state based on action
const counterReducer = (state = { count: 0 }, action) => {
  switch (action.type) {
    case 'INCREMENT':
      return { count: state.count + 1 }; // Return new state, don't mutate
    case 'DECREMENT':
      return { count: state.count - 1 };
    default:
      return state; // Return current state for unknown actions
  }
};

// Store: holds state and provides dispatch method
const store = createStore(counterReducer);
store.dispatch({ type: 'INCREMENT' }); // Dispatch action to update state

```

---

## Q41. 💡 Redux: actions, reducers, and store

Actions describe what happened, reducers specify how state changes, and the store holds state and provides access methods - together they create predictable state updates. Actions are plain objects with type and optional payload describing what happened, reducers are pure functions that take current state and action, return new state.

- **Trade-offs**: The catch is store is single source of truth with getState(), dispatch(), and subscribe() methods - data flow: dispatch(action) → reducer updates state → store notifies subscribers. The three parts work together to create predictable state updates, but watch out - you need to understand all three parts to use Redux effectively.

Example:

```jsx
const actions = {
  increment: { type: 'INCREMENT' },
  decrement: { type: 'DECREMENT' }
};
const reducer = (state = { count: 0 }, action) => {
  switch (action.type) {
    case 'INCREMENT':
      return { count: state.count + 1 };
    case 'DECREMENT':
      return { count: state.count - 1 };
    default:
      return state;
  }
};

```

---

## Q42. 🔧 Redux middleware and how to use it

Middleware intercepts actions before they reach reducers, allowing you to modify, log, or delay actions - it's a function that receives the store, returns a function that receives the next middleware, which returns a function that receives the action. Use middleware for async operations, logging, error handling, or any side effects that need to happen between dispatch and reducer.

- **Trade-offs**: Middleware extends Redux with custom functionality between dispatch and reducer, which is powerful, but the catch is the function signature (store => next => action) can be confusing at first. Multiple middleware can be composed together in a chain, but watch out - order matters since each middleware calls the next one in sequence.

Example:

```jsx
// Middleware: intercepts actions before they reach reducer
// Function signature: store => next => action
const loggerMiddleware = (store) => (next) => (action) => {
  console.log('Dispatching:', action); // Log before action
  const result = next(action); // Pass action to next middleware/reducer
  console.log('New state:', store.getState()); // Log after state update
  return result; // Return result to previous middleware
};

```

---

## Q43. 🔧 Redux Thunk and how to use it

Redux Thunk is middleware that allows action creators to return functions instead of plain objects - these functions receive dispatch and getState as arguments, enabling async operations like API calls, conditional dispatches, and accessing current state. Apply it to your store with `applyMiddleware(thunk)` and use it for async actions like fetching data or handling side effects.

- **Trade-offs**: Thunk is simple and easy to learn, perfect for most async Redux needs, but the catch is it's less powerful than Saga for complex async orchestration - use Thunk for straightforward async operations, but watch out - for very complex flows with cancellation, debouncing, or complex sequencing, Saga might be better.

Example:

```jsx
// Thunk: action creator that returns function instead of object
const fetchUserThunk = (userId) => async (dispatch, getState) => {
  dispatch({ type: 'FETCH_USER_START' }); // Dispatch loading state
  try {
    const user = await api.getUser(userId); // Async operation
    dispatch({ type: 'FETCH_USER_SUCCESS', payload: user }); // Dispatch success
  } catch (e) {
    dispatch({ type: 'FETCH_USER_ERROR', error: String(e) }); // Dispatch error
  }
};

```

---

## Q44. 🤔 Redux Saga vs Redux Thunk

Redux Saga uses generator functions for complex async flows - it handles cancellation, debouncing, race conditions, and complex orchestration better than Thunk.

- **Trade-offs**: The catch is Saga is easier to test because generators are testable, Thunk needs more mocking - use Thunk for most cases, Saga for complex async scenarios. Saga handles complex async scenarios better than Thunk, but adds complexity, so watch out - only use Saga when you need its advanced features.

Example:

```jsx
function* fetchUserSaga(action) {
  try {
    yield put({ type: 'FETCH_USER_START' });
    const user = yield call(api.getUser, action.payload);
    yield put({ type: 'FETCH_USER_SUCCESS', payload: user });
  } catch (e) {
    yield put({ type: 'FETCH_USER_ERROR', error: String(e) });
  }
}

```

---

## Q45. 🤔 Redux Toolkit (RTK) and why to use it

Redux Toolkit reduces Redux boilerplate with createSlice, configureStore, and Immer integration - it's the official recommended way to use Redux in modern apps. RTK combines actions and reducers in createSlice, reducing boilerplate.

- **Trade-offs**: The catch is can write "mutating" code in reducers, Immer handles immutability - configureStore includes good defaults and DevTools setup. RTK is now the standard way to use Redux, not plain Redux, but watch out - if you're learning Redux, start with RTK, not plain Redux.

Example:

```jsx
const counterSlice = createSlice({
  name: 'counter',
  initialState: { count: 0 },
  reducers: {
    increment: state => { state.count += 1; },
    addBy: (state, action) => { state.count += action.payload; }
  }
});
const store = configureStore({
  reducer: { counter: counterSlice.reducer }
});

```

---

## Q46. 🤔 Zustand vs Redux

Zustand is a lightweight state library with less boilerplate than Redux - no actions or reducers needed, just create a store and use it directly in components. Minimal boilerplate, simple API, no actions or reducers required.

- **Trade-offs**: The catch is good performance with selective subscriptions, only re-renders what changed - excellent TypeScript support out of the box. Zustand is Redux-like but simpler, good for many use cases, but watch out - it doesn't have Redux's ecosystem and tooling, so consider your needs.

Example:

```jsx
const useStore = create((set) => ({
  count: 0,
  increment: () => set((state) => ({ count: state.count + 1 }))
}));

```

---

## Q47. 🔧 Recoil and how it works

Recoil uses atoms and selectors for fine-grained state - more React-like than Redux with automatic derived state, optimized for React's rendering model. Atoms are individual state pieces, selectors compute derived state automatically.

- **Trade-offs**: The catch is feels more natural to React developers than Redux patterns - selectors automatically update when dependencies change, no manual management. Recoil is React-specific and optimized for React's rendering model, but watch out - it's still experimental, so use with caution in production.

Example:

```jsx
const countState = atom({ key: 'countState', default: 0 });
const [count, setCount] = useRecoilState(countState);

```

---

## Q48. 📊 Local state vs global state

Local state lives in one component and doesn't affect others, while global state is shared across multiple components and managed centrally with Context, Redux, or other solutions. Local state is component-specific, simpler to manage.

- **Trade-offs**: The catch is local state changes only affect one component, global affects all subscribers - lift state up when needed, use global state when many components need it. Use local state for UI, global state for shared business logic, but watch out - don't overuse global state, it can make your app harder to reason about.

Example:

```jsx
function Counter() {
  const [count, setCount] = useState(0);
  return (
    <div>
      <div>{count}</div>
      <button onClick={() => setCount(c => c + 1)}>+</button>
    </div>
  );
}

```

---

## Q49. 📊 When to use each state management solution

Use local state for component-specific UI, Context for simple global data, Redux/Zustand for complex shared state - choose based on app complexity and team needs. Start with local state, lift up when needed, use global state for shared data.

- **Trade-offs**: The catch is over-engineering with Redux when Context or local state would work - consider team familiarity, app size, and debugging needs when choosing. Choose the simplest solution that fits your needs, don't over-engineer, but watch out - sometimes you need to refactor as your app grows, so plan ahead.

Example:

```jsx
// Local state
const [isOpen, setIsOpen] = useState(false);

// Context
const { theme } = useContext(ThemeContext);

// Redux
const count = useSelector(state => state.counter.count);

```

---

