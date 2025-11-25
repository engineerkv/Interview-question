# 3. State Management (Q37–47)

---

## Q37. Context API and how to use it

Context API shares data across the component tree without prop drilling - use it for global data like themes, user info, or language settings that many components need. Context shares data globally without prop drilling through multiple levels.

- **Trade-offs**: The catch is creating new context values every render causes unnecessary re-renders - memoize context value with useMemo to prevent performance issues. Context solves prop drilling but isn't a replacement for Redux, so use wisely, but watch out - context updates cause all consumers to re-render, which can be expensive.

Example:

```jsx
const ThemeContext = createContext();
function ThemeProvider({ children }) {
  const [theme, setTheme] = useState('light');
  return (
    <ThemeContext.Provider value={{ theme, setTheme }}>
      {children}
    </ThemeContext.Provider>
  );
}
function ThemedButton() {
  const { theme, setTheme } = useContext(ThemeContext);
  return (
    <button onClick={() => setTheme(theme === 'light' ? 'dark' : 'light')}>
      Toggle
    </button>
  );
}
```

<div align="center">

**[← Previous: React Hooks](2%29%20React%20Hooks.md)** | **[Next: Server State & Data Fetching →](4%29%20Server%20State%20%26%20Data%20Fetching.md)**

</div>

---

## Q38. Redux and how it works

Redux manages app state in one store using actions and reducers - it follows unidirectional data flow for predictable updates, making state changes traceable and debuggable. Actions describe changes, reducers update state, store holds everything.

- **Trade-offs**: The catch is using Redux for simple apps - it adds complexity without benefit, same state and action always produce same result, enabling predictable debugging. Unidirectional flow (action → reducer → store → component) keeps state predictable, but watch out - Redux adds boilerplate, so only use it when you need the benefits.

Example:

```jsx
const counterReducer = (state = { count: 0 }, action) => {
  switch (action.type) {
    case 'INCREMENT': 
      return { count: state.count + 1 };
    case 'DECREMENT': 
      return { count: state.count - 1 };
    default: 
      return state;
  }
};
const store = createStore(counterReducer);
store.dispatch({ type: 'INCREMENT' });
```

---

## Q39. Redux: actions, reducers, and store

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

## Q40. Redux middleware and how to use it

Middleware intercepts actions before they reach reducers, allowing you to modify, log, or delay actions - it's a function that receives the store, returns a function that receives the next middleware, which returns a function that receives the action. Use middleware for async operations, logging, error handling, or any side effects that need to happen between dispatch and reducer.

- **Trade-offs**: Middleware extends Redux with custom functionality between dispatch and reducer, which is powerful, but the catch is the function signature (store => next => action) can be confusing at first. Multiple middleware can be composed together in a chain, but watch out - order matters since each middleware calls the next one in sequence.

Example:

```jsx
const loggerMiddleware = (store) => (next) => (action) => {
  console.log('Dispatching:', action);
  const result = next(action);
  console.log('New state:', store.getState());
  return result;
};
```

---

## Q41. Redux Thunk and how to use it

Redux Thunk is middleware that allows action creators to return functions instead of plain objects - these functions receive dispatch and getState as arguments, enabling async operations like API calls, conditional dispatches, and accessing current state. Apply it to your store with `applyMiddleware(thunk)` and use it for async actions like fetching data or handling side effects.

- **Trade-offs**: Thunk is simple and easy to learn, perfect for most async Redux needs, but the catch is it's less powerful than Saga for complex async orchestration - use Thunk for straightforward async operations, but watch out - for very complex flows with cancellation, debouncing, or complex sequencing, Saga might be better.

Example:

```jsx
const fetchUserThunk = (userId) => async (dispatch, getState) => {
  dispatch({ type: 'FETCH_USER_START' });
  try {
    const user = await api.getUser(userId);
    dispatch({ type: 'FETCH_USER_SUCCESS', payload: user });
  } catch (e) {
    dispatch({ type: 'FETCH_USER_ERROR', error: String(e) });
  }
};
```

---

## Q42. Redux Saga vs Redux Thunk

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

## Q43. Redux Toolkit (RTK) and why to use it

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

## Q44. Zustand vs Redux

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

## Q45. Recoil and how it works

Recoil uses atoms and selectors for fine-grained state - more React-like than Redux with automatic derived state, optimized for React's rendering model. Atoms are individual state pieces, selectors compute derived state automatically.

- **Trade-offs**: The catch is feels more natural to React developers than Redux patterns - selectors automatically update when dependencies change, no manual management. Recoil is React-specific and optimized for React's rendering model, but watch out - it's still experimental, so use with caution in production.

Example:

```jsx
const countState = atom({ key: 'countState', default: 0 });
const [count, setCount] = useRecoilState(countState);
```

---

## Q46. Local state vs global state

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

## Q47. When to use each state management solution

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

<div align="center">

**[← Previous: React Hooks](2%29%20React%20Hooks.md)** | **[Next: Server State & Data Fetching →](4%29%20Server%20State%20%26%20Data%20Fetching.md)**

</div>
