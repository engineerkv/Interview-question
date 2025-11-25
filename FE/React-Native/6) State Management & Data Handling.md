# 6. State Management & Data Handling (Q51–60)

---

## Q51. State management tools available for React Native

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

<div align="center">

**[← Previous: Performance Optimization & Measurement](5%29%20Performance%20Optimization%20%26%20Measurement.md)** | **[Next: CodePush & OTA Updates →](7%29%20CodePush%20%26%20OTA%20Updates.md)**

</div>

---

## Q52. Implementing Redux in React Native

Use Redux Toolkit for complex state logic and multiple components, Context API for simple state and fewer components - start with Context API, migrate to Redux if needed. Context API (good for simple state and fewer components), Redux Toolkit (better for complex state and many components).

- **Trade-offs**: The catch is Redux Toolkit provides better debugging (developer experience) - Context API is easier to learn (learning curve). Start with Context API, migrate to Redux if needed, but watch out - Redux has better performance for large apps (performance).

Example:

```jsx
// Context API - for simple state
const ThemeContext = createContext();

function ThemeProvider({ children }) {
  const [theme, setTheme] = useState('light');
  return (
    <ThemeContext.Provider value={{ theme, setTheme }}>
      {children}
    </ThemeContext.Provider>
  );
}
```

---

## Q53. Using Recoil for state management

Use AsyncStorage for simple key-value storage, MMKV for better performance, or SQLite for complex relational data - choose storage based on data structure. AsyncStorage (simple key-value storage, good for small data), MMKV (better performance, good for frequent access), SQLite (relational database, good for complex data).

- **Trade-offs**: The catch is choose based on data complexity and performance needs - SQLite provides full database capabilities. Choose storage based on data structure, but watch out - MMKV is faster than AsyncStorage (performance).

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
```

---

## Q54. Implementing Zustand for state management

AsyncStorage stores data in plain text, while SecureStorage encrypts data for sensitive information like tokens - always use SecureStorage for sensitive data. AsyncStorage is plain text storage, not secure; SecureStorage is encrypted storage, secure for sensitive data.

- **Trade-offs**: The catch is SecureStorage is slightly slower due to encryption (performance) - SecureStorage provides better security. Always use SecureStorage for sensitive data, but watch out - use SecureStorage for tokens, passwords, etc. (use cases).

Example:

```jsx
// AsyncStorage - plain text
import AsyncStorage from '@react-native-async-storage/async-storage';

const storeToken = async (token) => {
  await AsyncStorage.setItem('authToken', token);
};

// SecureStorage - encrypted
import * as Keychain from 'react-native-keychain';

const storeSecureToken = async (token) => {
  await Keychain.setGenericPassword('authToken', token);
};
```

---

## Q55. Using Context API for state management

Use local storage, sync mechanisms, and network state detection to build apps that work offline - provide seamless offline experience (user experience). Store data locally for offline access (local storage).

- **Trade-offs**: The catch is monitor network state (network detection) - queue actions when offline (queue actions). Provide seamless offline experience (user experience), but watch out - sync data when back online (sync mechanisms).

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
}
```

---

## Q56. Persisting data locally with AsyncStorage

Use background tasks, push notifications, and sync strategies to update data when the app is in the background - handle platform-specific limitations. Use background task libraries (background tasks).

- **Trade-offs**: The catch is keep data fresh with background updates (data freshness) - consider battery impact (battery optimization). Handle platform-specific limitations, but watch out - implement efficient sync strategies (sync strategies).

Example:

```jsx
import BackgroundJob from 'react-native-background-job';

function BackgroundSync() {
  useEffect(() => {
    BackgroundJob.register({
      jobKey: 'syncJob',
      period: 60000, // 1 minute
    });
  }, []);
}
```

---

## Q57. MMKV and how it compares to AsyncStorage

Batching groups multiple state updates into a single render cycle, reducing the number of re-renders and improving performance - React 18 has improved batching. React Native automatically batches updates (automatic batching).

- **Trade-offs**: The catch is groups synchronous updates together (synchronous updates) - may not batch async updates (async updates). React 18 has improved batching, but watch out - reduces number of re-renders (performance).

Example:

```jsx
function BatchingExample() {
  const [count, setCount] = useState(0);
  const [name, setName] = useState('');
  
  const handleUpdate = () => {
    // These updates are batched together
    setCount(1);
    setName('John');
    // Only one re-render occurs
  };
}
```

---

## Q58. Implementing offline-first apps

Use platform-specific configuration files and build-time environment variables for different environments - use build scripts to set environment variables. Set variables at build time (build-time variables).

- **Trade-offs**: The catch is use .env files for configuration (environment files) - don't expose sensitive data in environment variables. Use build scripts to set environment variables, but watch out - different configs for iOS and Android (platform configuration).

Example:

```jsx
const config = {
  development: {
    apiUrl: 'https://dev-api.example.com',
    debug: true
  },
  production: {
    apiUrl: 'https://api.example.com',
    debug: false
  }
};

const env = __DEV__ ? 'development' : 'production';
export const API_URL = config[env].apiUrl;
```

---

## Q59. Handling background data synchronization

Use secure storage solutions, environment variables, and proper key management practices - control access to sensitive data (access control). Use keychain or keystore for sensitive data (secure storage).

- **Trade-offs**: The catch is implement proper key management practices (key management) - encrypt sensitive data at rest (encryption). Control access to sensitive data (access control), but watch out - use build-time environment variables.

Example:

```jsx
import { getItem, setItem } from 'react-native-keychain';

const storeApiKey = async (apiKey) => {
  try {
    await setItem('apiKey', apiKey);
  } catch (error) {
    console.error('Error storing key:', error);
  }
};
```

---

## Q60. Implementing data batching for performance

Avoid prop drilling, mutating state directly, overusing global state, and not properly handling async state - recognize and fix these patterns early. Avoid passing props through multiple levels (prop drilling), never mutate state directly (state mutation).

- **Trade-offs**: The catch is don't put everything in global state (overusing global state), handle async state properly (async state) - use proper state management patterns. Recognize and fix these patterns early, but watch out - follow React and React Native best practices.

Example:

```jsx
// ❌ Anti-pattern: Prop drilling
function App() {
  const [user, setUser] = useState(null);
  return <Parent user={user} setUser={setUser} />;
}

function Parent({ user, setUser }) {
  return <Child user={user} setUser={setUser} />;
}

// ✅ Better: Use Context or Redux
```

---

<div align="center">

**[← Previous: Performance Optimization & Measurement](5%29%20Performance%20Optimization%20%26%20Measurement.md)** | **[Next: CodePush & OTA Updates →](7%29%20CodePush%20%26%20OTA%20Updates.md)**

</div>
