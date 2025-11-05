# 🧩 4. State Management (Q30–40)

---

## 30) What is state management and why is it important in React?

State management is sharing and managing data across components. It prevents prop drilling and keeps data consistent.

```jsx
function App() {
  const [user, setUser] = useState(null);
  return <div><Header user={user} /><Main user={user} /><Footer user={user} /></div>;
}
```

- **Core Purpose**: Share data across components without passing props through every level
- **Real-World Need**: Essential for complex apps where many components need the same data
- **Common Mistake**: Lifting state too high or using global state for local UI needs
- **Scalability**: Centralized state makes large apps more maintainable and predictable
- **Interview Tip**: Explain when to use local state vs global state vs Context API

---

## 31) What is the Context API and when should you use it?

Context API shares data across the component tree without prop drilling. Use it for global data like themes or user info.

```jsx
const ThemeContext = createContext();
function ThemeProvider({ children }) {
  const [theme, setTheme] = useState('light');
  return <ThemeContext.Provider value={{ theme, setTheme }}>{children}</ThemeContext.Provider>;
}
function ThemedButton() {
  const { theme, setTheme } = useContext(ThemeContext);
  return <button onClick={() => setTheme(theme === 'light' ? 'dark' : 'light')}>Toggle</button>;
}
```

- **Core Purpose**: Share data globally without prop drilling through multiple levels
- **Real-World Use**: Themes, user authentication, language settings, or any global app config
- **Common Mistake**: Creating new context values every render causes unnecessary re-renders
- **Optimization**: Memoize context value with useMemo to prevent performance issues
- **Interview Tip**: Explain that Context solves prop drilling but isn't a replacement for Redux

---

## 32) What is Redux and how does it work?

Redux manages app state in one store using actions and reducers. Follows unidirectional data flow for predictable updates.

```jsx
const counterReducer = (state = { count: 0 }, action) => {
  switch (action.type) {
    case 'INCREMENT': return { count: state.count + 1 };
    case 'DECREMENT': return { count: state.count - 1 };
    default: return state;
  }
};
const store = createStore(counterReducer);
store.dispatch({ type: 'INCREMENT' });
```

- **Core Pattern**: Actions describe changes, reducers update state, store holds everything
- **Real-World Use**: Complex apps with lots of shared state or when you need time-travel debugging
- **Common Mistake**: Using Redux for simple apps - it adds complexity without benefit
- **Predictability**: Same state and action always produce same result, enabling debugging
- **Interview Tip**: Explain unidirectional flow: action → reducer → store → component

---

## 33) What are the main principles of Redux?

Redux has three principles: single source of truth, read-only state, and pure reducer functions.

```jsx
const store = createStore(reducer);
// ❌ state.count = state.count + 1;
// ✅ store.dispatch({ type: 'INCREMENT' });
```

- **Single Source of Truth**: One store contains all app state, making it predictable
- **Immutable Updates**: Never mutate state directly, always return new state objects
- **Pure Functions**: Reducers must be pure - no side effects, same input = same output
- **Real-World Benefit**: These principles enable time-travel debugging and predictable testing
- **Interview Tip**: Explain how these principles make Redux state predictable and debuggable

---

## 34) What are actions, reducers, and the store in Redux?

Actions describe what happened, reducers specify how state changes, and the store holds state and provides access methods.

```jsx
const actions = { increment: { type: 'INCREMENT' }, decrement: { type: 'DECREMENT' } };
const reducer = (state = { count: 0 }, action) => {
  switch (action.type) {
    case 'INCREMENT': return { count: state.count + 1 };
    case 'DECREMENT': return { count: state.count - 1 };
    default: return state;
  }
};
```

- **Actions**: Plain objects with type and optional payload describing what happened
- **Reducers**: Pure functions that take current state and action, return new state
- **Store**: Single source of truth with getState(), dispatch(), and subscribe() methods
- **Data Flow**: dispatch(action) → reducer updates state → store notifies subscribers
- **Interview Tip**: Explain the three parts work together to create predictable state updates

---

## 35) What is Redux Toolkit (RTK) and how does it simplify Redux?

Redux Toolkit reduces Redux boilerplate with createSlice, configureStore, and Immer integration.

```jsx
const counterSlice = createSlice({
  name: 'counter',
  initialState: { count: 0 },
  reducers: {
    increment: state => { state.count += 1; },
    addBy: (state, action) => { state.count += action.payload; }
  }
});
const store = configureStore({ reducer: { counter: counterSlice.reducer } });
```

- **Core Benefit**: Less boilerplate - combines actions and reducers in createSlice
- **Real-World Use**: Modern Redux apps should use RTK, it's the official recommended way
- **Immer Integration**: Can write "mutating" code in reducers, Immer handles immutability
- **Built-in Best Practices**: configureStore includes good defaults and DevTools setup
- **Interview Tip**: Explain that RTK is now the standard way to use Redux, not plain Redux

---

## 36) What are Redux middleware and how do they work?

Middleware intercepts actions before they reach reducers. Used for async operations, logging, or side effects.

```jsx
const loggerMiddleware = (store) => (next) => (action) => {
  console.log('Dispatching:', action);
  const result = next(action);
  console.log('New state:', store.getState());
  return result;
};
```

- **Core Purpose**: Extend Redux with custom functionality between dispatch and reducer
- **Real-World Use**: Async operations (Thunk/Saga), logging, analytics, or error handling
- **Common Pattern**: Middleware is a function that returns a function that returns a function
- **Chaining**: Multiple middleware can be composed together in a chain
- **Interview Tip**: Explain middleware as the "middle layer" between dispatch and reducer

---

## 37) What are Redux Thunk and Redux Saga, and how do they differ?

Thunk lets action creators return functions. Saga uses generators for complex async flows. Thunk is simpler, Saga is more powerful.

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

- **Thunk**: Simple functions returned from action creators, easy to learn and use
- **Saga**: Generator functions for complex flows like cancellation, debouncing, or race conditions
- **Real-World Choice**: Use Thunk for most cases, Saga for complex async orchestration
- **Testing**: Saga is easier to test because generators are testable, Thunk needs more mocking
- **Interview Tip**: Explain that Thunk is simpler but Saga handles complex async scenarios better

---

## 38) What is the difference between local component state and global state?

Local state lives in one component. Global state is shared across multiple components and managed centrally.

```jsx
function Counter() {
  const [count, setCount] = useState(0);
  return <div><div>{count}</div><button onClick={() => setCount(c => c + 1)}>+</button></div>;
}
```

- **Local State**: Component-specific, doesn't affect other components, simpler to manage
- **Global State**: Shared across components, managed with Context, Redux, or other solutions
- **Real-World Rule**: Use local state for UI state, global state for business logic
- **Performance**: Local state changes only affect one component, global affects all subscribers
- **Interview Tip**: Explain when to lift state up vs when to use global state management

---

## 39) What is Zustand and how does it differ from Redux?

Zustand is a lightweight state library with less boilerplate than Redux. No actions or reducers needed.

```jsx
const useStore = create((set) => ({
  count: 0,
  increment: () => set((state) => ({ count: state.count + 1 }))
}));
```

- **Core Benefit**: Minimal boilerplate, simple API, no actions or reducers required
- **Real-World Use**: Great for smaller apps or when Redux feels like overkill
- **Performance**: Good performance with selective subscriptions, only re-renders what changed
- **TypeScript**: Excellent TypeScript support out of the box
- **Interview Tip**: Explain that Zustand is Redux-like but simpler, good for many use cases

---

## 40) What is Recoil and how does it manage global state differently?

Recoil uses atoms and selectors for fine-grained state. More React-like than Redux with automatic derived state.

```jsx
const countState = atom({ key: 'countState', default: 0 });
const [count, setCount] = useRecoilState(countState);
```

- **Core Concept**: Atoms are individual state pieces, selectors compute derived state automatically
- **Real-World Benefit**: Only components using specific atoms re-render, better performance
- **React-like**: Feels more natural to React developers than Redux patterns
- **Derived State**: Selectors automatically update when dependencies change, no manual management
- **Interview Tip**: Explain that Recoil is React-specific and optimized for React's rendering

---
