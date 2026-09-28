---
sidebar_label: "State Management & Data Persistence"
---
# 2. State Management & Data Persistence (Q11–21)

---

## Q11. 📊 State management tools available for React Native

Popular tools include Redux, Redux Toolkit, Recoil, Zustand, and Context API for state management - choose based on app complexity and team preference. Redux (most popular, complex but powerful), Redux Toolkit (simplified Redux with less boilerplate).

- **Trade-offs**: The catch is built-in React solution for simple state (Context API) - each tool has different use cases. Choose based on app complexity and team preference, but watch out - Recoil (Facebook's state management library), Zustand (lightweight and simple).

Example:

```jsx
import { createSlice, configureStore } from '@reduxjs/toolkit';

const counterSlice = createSlice({
  name: 'counter',
  initialState: { count: 0 },
  reducers: {
    increment: (state) => { state.count += 1; }
  }
});

const store = configureStore({
  reducer: { counter: counterSlice.reducer }
});

```

---

## Q12. 📱 Implementing Redux Toolkit in React Native

Use Redux Toolkit for complex state logic and multiple components - provides better debugging and performance for large apps. Redux Toolkit (simplified Redux with less boilerplate), Better debugging (developer experience), Better performance for large apps (performance).

- **Trade-offs**: The catch is requires more setup than Context API (setup complexity) - provides better debugging tools (developer experience). Better performance for large apps (performance), but watch out - use for complex state management needs (use cases).

Example:

```jsx
import { createSlice, configureStore } from '@reduxjs/toolkit';
import { Provider, useSelector, useDispatch } from 'react-redux';

// Create slice
const counterSlice = createSlice({
  name: 'counter',
  initialState: { count: 0 },
  reducers: {
    increment: (state) => { state.count += 1; },
    decrement: (state) => { state.count -= 1; }
  }
});

// Configure store
const store = configureStore({
  reducer: { counter: counterSlice.reducer }
});

// Use in component
function Counter() {
  const count = useSelector(state => state.counter.count);
  const dispatch = useDispatch();

  return (
    <View>
      <Text>Count: {count}</Text>
      <Button title="Increment" onPress={() => dispatch(counterSlice.actions.increment())} />
    </View>
  );
}

// Wrap app with Provider
function App() {
  return (
    <Provider store={store}>
      <Counter />
    </Provider>
  );
}

```

---

## Q13. 📊 Using Recoil for state management

Recoil is Facebook's state management library that provides atoms and selectors for managing application state - good for complex state with derived values. Atoms (units of state), Selectors (derived state), Better performance with large state trees (performance).

- **Trade-offs**: The catch is requires understanding Recoil concepts (learning curve) - provides fine-grained reactivity (reactivity). Good for complex state with derived values, but watch out - less popular than Redux (ecosystem).

Example:

```jsx
import { atom, useRecoilState, selector, useRecoilValue } from 'recoil';

// Define atom
const counterState = atom({
  key: 'counterState',
  default: 0,
});

// Define selector
const doubledCounter = selector({
  key: 'doubledCounter',
  get: ({ get }) => get(counterState) * 2,
});

// Use in component
function Counter() {
  const [count, setCount] = useRecoilState(counterState);
  const doubled = useRecoilValue(doubledCounter);

  return (
    <View>
      <Text>Count: {count}</Text>
      <Text>Doubled: {doubled}</Text>
      <Button title="Increment" onPress={() => setCount(count + 1)} />
    </View>
  );
}

```

---

## Q14. 📊 Implementing Zustand for state management

Zustand is a lightweight state management library with minimal boilerplate - good for small to medium apps with simple state needs. Minimal boilerplate (simplicity), Small bundle size (performance), Easy to learn (learning curve).

- **Trade-offs**: The catch is less powerful than Redux for complex apps (scalability) - provides hooks-based API (developer experience). Good for small to medium apps with simple state needs, but watch out - can be extended with middleware (extensibility).

Example:

```jsx
import create from 'zustand';

const useStore = create((set) => ({
  count: 0,
  increment: () => set((state) => ({ count: state.count + 1 })),
  decrement: () => set((state) => ({ count: state.count - 1 })),
}));

function Counter() {
  const { count, increment, decrement } = useStore();

  return (
    <View>
      <Text>Count: {count}</Text>
      <Button title="Increment" onPress={increment} />
      <Button title="Decrement" onPress={decrement} />
    </View>
  );
}

```

---

## Q15. 📊 Using MobX for state management

MobX is a reactive state management library that uses observables and actions - good for apps with complex reactive state requirements. Observables (reactive state), Actions (state mutations), Computed values (derived state), Automatic reactivity (reactivity).

- **Trade-offs**: The catch is requires decorators or makeObservable (setup complexity) - provides automatic reactivity (developer experience). Good for apps with complex reactive state requirements, but watch out - less popular than Redux (ecosystem).

Example:

```jsx
import { makeAutoObservable } from 'mobx';
import { observer } from 'mobx-react-lite';

class CounterStore {
  count = 0;

  constructor() {
    makeAutoObservable(this);
  }

  increment() {
    this.count++;
  }

  decrement() {
    this.count--;
  }

  get doubled() {
    return this.count * 2;
  }
}

const store = new CounterStore();

const Counter = observer(() => {
  return (
    <View>
      <Text>Count: {store.count}</Text>
      <Text>Doubled: {store.doubled}</Text>
      <Button title="Increment" onPress={() => store.increment()} />
      <Button title="Decrement" onPress={() => store.decrement()} />
    </View>
  );
});

```

---

## Q16. 📊 Using Context API for state management

Context API is React's built-in solution for sharing state across components - good for simple state that doesn't require complex logic. Built-in React solution (no dependencies), Simple API (ease of use), Good for simple state (use cases).

- **Trade-offs**: The catch is can cause performance issues with frequent updates (performance) - no built-in devtools (developer experience). Good for simple state that doesn't require complex logic, but watch out - combine with useReducer for complex state (scalability).

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

function ThemedComponent() {
  const { theme, setTheme } = useContext(ThemeContext);

  return (
    <View style={{ backgroundColor: theme === 'light' ? '#fff' : '#000' }}>
      <Button title="Toggle Theme" onPress={() => setTheme(theme === 'light' ? 'dark' : 'light')} />
    </View>
  );
}

```

---

## Q17. ⚡ Persisting data locally with AsyncStorage

AsyncStorage provides simple key-value storage for React Native apps - good for storing small amounts of non-sensitive data. Simple API (ease of use), Works on both iOS and Android (cross-platform), Asynchronous operations (performance).

- **Trade-offs**: The catch is limited storage size (storage limits) - not encrypted (security). Good for storing small amounts of non-sensitive data, but watch out - use SecureStorage for sensitive data (security).

Example:

```jsx
import AsyncStorage from '@react-native-async-storage/async-storage';

const storeData = async (key, value) => {
  try {
    await AsyncStorage.setItem(key, JSON.stringify(value));
  } catch (error) {
    console.error('Error storing data:', error);
  }
};

const getData = async (key) => {
  try {
    const value = await AsyncStorage.getItem(key);
    return value != null ? JSON.parse(value) : null;
  } catch (error) {
    console.error('Error reading data:', error);
  }
};

```

---

## Q18. ⚡ MMKV and how it compares to AsyncStorage

MMKV is a high-performance key-value storage library that's faster than AsyncStorage - good for frequently accessed data. Faster than AsyncStorage (performance), Synchronous API available (synchronous access), Better for large data (scalability).

- **Trade-offs**: The catch is requires native module (native dependency) - smaller API surface (simplicity). Good for frequently accessed data, but watch out - AsyncStorage is simpler for basic use cases (ease of use).

Example:

```jsx
import { MMKV } from 'react-native-mmkv';

const storage = new MMKV();

// Store data
storage.set('user.name', 'John Doe');
storage.set('user.age', 30);

// Read data
const name = storage.getString('user.name');
const age = storage.getNumber('user.age');

// Delete data
storage.delete('user.name');

// Compare with AsyncStorage
// AsyncStorage: Async, slower, simpler
// MMKV: Sync/Async, faster, more features
```

---

## Q19. 🔧 Implementing offline-first apps

Offline-first apps work without internet connection by storing data locally and syncing when online - provides better user experience. Local storage (data persistence), Network detection (connectivity), Sync mechanisms (data synchronization).

- **Trade-offs**: The catch is handle sync conflicts (conflict resolution) - manage storage limits (storage management). Provides better user experience, but watch out - implement efficient sync strategies (sync strategies).

Example:

```jsx
import NetInfo from '@react-native-community/netinfo';
import AsyncStorage from '@react-native-async-storage/async-storage';

function OfflineFirstApp() {
  const [isOnline, setIsOnline] = useState(true);
  const [pendingActions, setPendingActions] = useState([]);

  useEffect(() => {
    const unsubscribe = NetInfo.addEventListener(state => {
      setIsOnline(state.isConnected);
      if (state.isConnected) {
        syncPendingActions();
      }
    });
    return () => unsubscribe();
  }, []);

  const syncPendingActions = async () => {
    const pending = await AsyncStorage.getItem('pendingActions');
    if (pending) {
      // Sync with server
      await syncToServer(JSON.parse(pending));
      await AsyncStorage.removeItem('pendingActions');
    }
  };
}

```

---

## Q20. 💡 Handling background data synchronization

Background sync updates data when app is in background using background tasks and push notifications - keeps data fresh without user interaction. Background tasks (task scheduling), Push notifications (data updates), Sync strategies (sync patterns).

- **Trade-offs**: The catch is platform-specific limitations (platform differences) - battery impact (battery optimization). Keeps data fresh without user interaction, but watch out - implement efficient sync intervals (sync efficiency).

Example:

```jsx
import BackgroundFetch from 'react-native-background-fetch';

BackgroundFetch.configure({
  minimumFetchInterval: 15, // minutes
}, async (taskId) => {
  // Sync data
  await syncData();
  BackgroundFetch.finish(taskId);
}, (error) => {
  console.error('Background fetch failed:', error);
  BackgroundFetch.finish(taskId);
});

```

---

## Q21. ⚡ Implementing data batching for performance

Data batching groups multiple state updates into a single render cycle, reducing re-renders and improving performance - React 18 has improved automatic batching. Automatic batching (React 18), Manual batching (React Native), Reduces re-renders (performance).

- **Trade-offs**: The catch is groups synchronous updates together (synchronous updates) - may not batch async updates (async updates). React 18 has improved automatic batching, but watch out - use startTransition for non-urgent updates (performance optimization).

Example:

```jsx
import { startTransition } from 'react';

function BatchingExample() {
  const [count, setCount] = useState(0);
  const [name, setName] = useState('');

  const handleUpdate = () => {
    // These updates are batched together
    setCount(1);
    setName('John');
    // Only one re-render occurs
  };

  const handleNonUrgentUpdate = () => {
    startTransition(() => {
      // Non-urgent updates
      setCount(count + 1);
    });
  };
}

```

---

