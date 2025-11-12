# 🧩 4. State Management (Q31–41)

---

## 🧩 Q31. What is the Context API and how do you use it?

### 🧠 Concept

Context API shares data across the component tree without prop drilling. Use it for global data like themes, user info, or language settings that many components need.

---

### 💡 Example

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

---

### 🔍 Deep Insights

* **Rule:** Context shares data globally without prop drilling through multiple levels.
* **Use Case:** Themes, user authentication, language settings, or any global app config.
* **Common Mistake:** Creating new context values every render causes unnecessary re-renders.
* **Pro Tip:** Memoize context value with useMemo to prevent performance issues.

---

### ⭐ Senior Takeaway

Context solves prop drilling but isn't a replacement for Redux—use wisely.

---

## 🧩 Q32. What is Redux and how does it work?

### 🧠 Concept

Redux manages app state in one store using actions and reducers. Follows unidirectional data flow for predictable updates, making state changes traceable and debuggable.

---

### 💡 Example

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

### 🔍 Deep Insights

* **Rule:** Actions describe changes, reducers update state, store holds everything.
* **Use Case:** Complex apps with lots of shared state or when you need time-travel debugging.
* **Common Mistake:** Using Redux for simple apps—it adds complexity without benefit.
* **Pro Tip:** Same state and action always produce same result, enabling predictable debugging.

---

### ⭐ Senior Takeaway

Unidirectional flow: action → reducer → store → component keeps state predictable.

---

## 🧩 Q33. What are Redux actions, reducers, and store?

### 🧠 Concept

Actions describe what happened, reducers specify how state changes, and the store holds state and provides access methods. Together they create predictable state updates.

---

### 💡 Example

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

### 🔍 Deep Insights

* **Rule:** Actions are plain objects with type and optional payload describing what happened.
* **Use Case:** Reducers are pure functions that take current state and action, return new state.
* **Common Mistake:** Store is single source of truth with getState(), dispatch(), and subscribe() methods.
* **Pro Tip:** Data flow: dispatch(action) → reducer updates state → store notifies subscribers.

---

### ⭐ Senior Takeaway

The three parts work together to create predictable state updates.

---

## 🧩 Q34. What is Redux middleware and how do you use it?

### 🧠 Concept

Middleware intercepts actions before they reach reducers. Used for async operations, logging, or side effects. It's a function that returns a function that returns a function.

---

### 💡 Example

```jsx
const loggerMiddleware = (store) => (next) => (action) => {
  console.log('Dispatching:', action);
  const result = next(action);
  console.log('New state:', store.getState());
  return result;
};
```

---

### 🔍 Deep Insights

* **Rule:** Middleware extends Redux with custom functionality between dispatch and reducer.
* **Use Case:** Async operations (Thunk/Saga), logging, analytics, or error handling.
* **Common Mistake:** Middleware is a function that returns a function that returns a function.
* **Pro Tip:** Multiple middleware can be composed together in a chain.

---

### ⭐ Senior Takeaway

Middleware is the "middle layer" between dispatch and reducer.

---

## 🧩 Q35. What is Redux Thunk and how do you use it?

### 🧠 Concept

Redux Thunk lets action creators return functions instead of plain objects. These functions receive dispatch and getState, enabling async operations and conditional dispatches.

---

### 💡 Example

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

### 🔍 Deep Insights

* **Rule:** Thunk lets action creators return functions for async operations.
* **Use Case:** Simple async flows, API calls, or conditional dispatches.
* **Common Mistake:** Thunk is simpler than Saga but less powerful for complex flows.
* **Pro Tip:** Use Thunk for most cases, Saga for complex async orchestration.

---

### ⭐ Senior Takeaway

Thunk is simple and easy to learn—perfect for most async Redux needs.

---

## 🧩 Q36. What is Redux Saga and how does it differ from Thunk?

### 🧠 Concept

Redux Saga uses generator functions for complex async flows. It handles cancellation, debouncing, race conditions, and complex orchestration better than Thunk.

---

### 💡 Example

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

### 🔍 Deep Insights

* **Rule:** Saga uses generator functions for complex flows like cancellation or debouncing.
* **Use Case:** Complex async orchestration, race conditions, or when you need cancellation.
* **Common Mistake:** Saga is easier to test because generators are testable, Thunk needs more mocking.
* **Pro Tip:** Use Thunk for most cases, Saga for complex async scenarios.

---

### ⭐ Senior Takeaway

Saga handles complex async scenarios better than Thunk, but adds complexity.

---

## 🧩 Q37. What is Redux Toolkit (RTK) and why should you use it?

### 🧠 Concept

Redux Toolkit reduces Redux boilerplate with createSlice, configureStore, and Immer integration. It's the official recommended way to use Redux in modern apps.

---

### 💡 Example

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

### 🔍 Deep Insights

* **Rule:** RTK combines actions and reducers in createSlice, reducing boilerplate.
* **Use Case:** Modern Redux apps should use RTK—it's the official recommended way.
* **Common Mistake:** Can write "mutating" code in reducers, Immer handles immutability.
* **Pro Tip:** configureStore includes good defaults and DevTools setup.

---

### ⭐ Senior Takeaway

RTK is now the standard way to use Redux, not plain Redux.

---

## 🧩 Q38. What is Zustand and how does it compare to Redux?

### 🧠 Concept

Zustand is a lightweight state library with less boilerplate than Redux. No actions or reducers needed—just create a store and use it directly in components.

---

### 💡 Example

```jsx
const useStore = create((set) => ({
  count: 0,
  increment: () => set((state) => ({ count: state.count + 1 }))
}));
```

---

### 🔍 Deep Insights

* **Rule:** Minimal boilerplate, simple API, no actions or reducers required.
* **Use Case:** Great for smaller apps or when Redux feels like overkill.
* **Common Mistake:** Good performance with selective subscriptions, only re-renders what changed.
* **Pro Tip:** Excellent TypeScript support out of the box.

---

### ⭐ Senior Takeaway

Zustand is Redux-like but simpler—good for many use cases.

---

## 🧩 Q39. What is Recoil and how does it work?

### 🧠 Concept

Recoil uses atoms and selectors for fine-grained state. More React-like than Redux with automatic derived state, optimized for React's rendering model.

---

### 💡 Example

```jsx
const countState = atom({ key: 'countState', default: 0 });
const [count, setCount] = useRecoilState(countState);
```

---

### 🔍 Deep Insights

* **Rule:** Atoms are individual state pieces, selectors compute derived state automatically.
* **Use Case:** Only components using specific atoms re-render, better performance.
* **Common Mistake:** Feels more natural to React developers than Redux patterns.
* **Pro Tip:** Selectors automatically update when dependencies change, no manual management.

---

### ⭐ Senior Takeaway

Recoil is React-specific and optimized for React's rendering model.

---

## 🧩 Q40. What is the difference between local and global state?

### 🧠 Concept

Local state lives in one component and doesn't affect others. Global state is shared across multiple components and managed centrally with Context, Redux, or other solutions.

---

### 💡 Example

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

### 🔍 Deep Insights

* **Rule:** Local state is component-specific, simpler to manage.
* **Use Case:** Use local state for UI state, global state for business logic.
* **Common Mistake:** Local state changes only affect one component, global affects all subscribers.
* **Pro Tip:** Lift state up when needed, use global state when many components need it.

---

### ⭐ Senior Takeaway

Use local state for UI, global state for shared business logic.

---

## 🧩 Q41. When should you use each state management solution?

### 🧠 Concept

Use local state for component-specific UI. Use Context for simple global data. Use Redux/Zustand for complex shared state. Choose based on app complexity and team needs.

---

### 💡 Example

```jsx
// Local state
const [isOpen, setIsOpen] = useState(false);

// Context
const { theme } = useContext(ThemeContext);

// Redux
const count = useSelector(state => state.counter.count);
```

---

### 🔍 Deep Insights

* **Rule:** Start with local state, lift up when needed, use global state for shared data.
* **Use Case:** Context for themes/config, Redux for complex apps, Zustand for simpler alternatives.
* **Common Mistake:** Over-engineering with Redux when Context or local state would work.
* **Pro Tip:** Consider team familiarity, app size, and debugging needs when choosing.

---

### ⭐ Senior Takeaway

Choose the simplest solution that fits your needs—don't over-engineer.

---
