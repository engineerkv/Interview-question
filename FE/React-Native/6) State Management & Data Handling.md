# 🧩 6. State Management & Data Handling (Q51–60)

---

## 51) What are popular state management tools in React Native (Redux, Recoil, Zustand)?

Popular tools include Redux, Redux Toolkit, Recoil, Zustand, and Context API for state management.

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

- **Core Tools**: Redux (most popular, complex but powerful), Redux Toolkit (simplified Redux with less boilerplate)
- **Real-World Options**: Recoil (Facebook's state management library), Zustand (lightweight and simple)
- **Common Alternative**: Built-in React solution for simple state (Context API)
- **Advanced Feature**: Each tool has different use cases
- **Interview Tip**: Explain that choose based on app complexity and team preference

---

## 52) How do you decide between Redux Toolkit and Context API for app-wide state?

Use Redux Toolkit for complex state logic and multiple components, Context API for simple state and fewer components.

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

- **Core Decision**: Context API (good for simple state and fewer components), Redux Toolkit (better for complex state and many components)
- **Real-World Impact**: Redux has better performance for large apps (performance)
- **Common Advantage**: Redux Toolkit provides better debugging (developer experience)
- **Learning**: Context API is easier to learn (learning curve)
- **Interview Tip**: Explain that start with Context API, migrate to Redux if needed

---

## 53) How do you persist data locally (AsyncStorage, MMKV, SQLite)?

Use AsyncStorage for simple key-value storage, MMKV for better performance, or SQLite for complex relational data.

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

- **Core Options**: AsyncStorage (simple key-value storage, good for small data), MMKV (better performance, good for frequent access), SQLite (relational database, good for complex data)
- **Real-World Comparison**: MMKV is faster than AsyncStorage (performance)
- **Common Use Cases**: Choose based on data complexity and performance needs
- **Advanced Feature**: SQLite provides full database capabilities
- **Interview Tip**: Explain that choose storage based on data structure

---

## 54) What's the difference between AsyncStorage and SecureStorage?

AsyncStorage stores data in plain text, while SecureStorage encrypts data for sensitive information like tokens.

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

- **Core Difference**: AsyncStorage is plain text storage, not secure; SecureStorage is encrypted storage, secure for sensitive data
- **Real-World Use**: Use SecureStorage for tokens, passwords, etc. (use cases)
- **Performance Trade-off**: SecureStorage is slightly slower due to encryption (performance)
- **Security**: SecureStorage provides better security
- **Interview Tip**: Explain that always use SecureStorage for sensitive data

---

## 55) How do you build an **offline-first** React Native app?

Use local storage, sync mechanisms, and network state detection to build apps that work offline.

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

- **Core Strategy**: Store data locally for offline access (local storage)
- **Real-World Use**: Sync data when back online (sync mechanisms)
- **Common Practice**: Monitor network state (network detection)
- **Advanced Feature**: Queue actions when offline (queue actions)
- **Interview Tip**: Explain that provide seamless offline experience (user experience)

---

## 56) How do you handle background data sync and refresh?

Use background tasks, push notifications, and sync strategies to update data when the app is in the background.

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

- **Core Approach**: Use background task libraries (background tasks)
- **Real-World Use**: Implement efficient sync strategies (sync strategies)
- **Common Benefit**: Keep data fresh with background updates (data freshness)
- **Important Consideration**: Consider battery impact (battery optimization)
- **Interview Tip**: Explain that handle platform-specific limitations

---

## 57) What is batching in React Native, and how does it improve performance?

Batching groups multiple state updates into a single render cycle, reducing the number of re-renders and improving performance.

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

- **Core Feature**: React Native automatically batches updates (automatic batching)
- **Real-World Benefit**: Reduces number of re-renders (performance)
- **Common Pattern**: Groups synchronous updates together (synchronous updates)
- **Limitation**: May not batch async updates (async updates)
- **Interview Tip**: Explain that React 18 has improved batching

---

## 58) How do you manage environment variables in mobile builds?

Use platform-specific configuration files and build-time environment variables for different environments.

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

- **Core Approach**: Set variables at build time (build-time variables)
- **Real-World Use**: Different configs for iOS and Android (platform configuration)
- **Common Practice**: Use .env files for configuration (environment files)
- **Security**: Don't expose sensitive data in environment variables
- **Interview Tip**: Explain that use build scripts to set environment variables

---

## 59) How do you handle secrets securely (e.g., API keys, tokens)?

Use secure storage solutions, environment variables, and proper key management practices.

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

- **Core Methods**: Use keychain or keystore for sensitive data (secure storage)
- **Real-World Practice**: Use build-time environment variables
- **Common Approach**: Implement proper key management practices (key management)
- **Advanced Feature**: Encrypt sensitive data at rest (encryption)
- **Interview Tip**: Explain that control access to sensitive data (access control)

---

## 60) What are common state management anti-patterns to avoid?

Avoid prop drilling, mutating state directly, overusing global state, and not properly handling async state.

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

- **Common Anti-patterns**: Avoid passing props through multiple levels (prop drilling), never mutate state directly (state mutation)
- **Real-World Mistakes**: Don't put everything in global state (overusing global state), handle async state properly (async state)
- **Best Practices**: Follow React and React Native best practices
- **Advanced Pattern**: Use proper state management patterns
- **Interview Tip**: Explain that recognize and fix these patterns early

---
