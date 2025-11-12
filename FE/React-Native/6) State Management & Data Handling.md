# 🧩 6. State Management & Data Handling (Q51–60)

---

## 🧩 Q51. What are popular state management tools in React Native?

### 🧠 Concept

Popular tools include Redux, Redux Toolkit, Recoil, Zustand, and Context API for state management. Choose based on app complexity and team preference.

---

### 💡 Example

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

### 🔍 Deep Insights

* **Rule:** Redux (most popular, complex but powerful), Redux Toolkit (simplified Redux with less boilerplate).
* **Use Case:** Recoil (Facebook's state management library), Zustand (lightweight and simple).
* **Common Mistake:** Built-in React solution for simple state (Context API).
* **Pro Tip:** Each tool has different use cases.

---

### ⭐ Senior Takeaway

Choose based on app complexity and team preference.

---

## 🧩 Q52. How do you decide between Redux Toolkit and Context API?

### 🧠 Concept

Use Redux Toolkit for complex state logic and multiple components, Context API for simple state and fewer components. Start with Context API, migrate to Redux if needed.

---

### 💡 Example

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

### 🔍 Deep Insights

* **Rule:** Context API (good for simple state and fewer components), Redux Toolkit (better for complex state and many components).
* **Use Case:** Redux has better performance for large apps (performance).
* **Common Mistake:** Redux Toolkit provides better debugging (developer experience).
* **Pro Tip:** Context API is easier to learn (learning curve).

---

### ⭐ Senior Takeaway

Start with Context API, migrate to Redux if needed.

---

## 🧩 Q53. How do you persist data locally?

### 🧠 Concept

Use AsyncStorage for simple key-value storage, MMKV for better performance, or SQLite for complex relational data. Choose storage based on data structure.

---

### 💡 Example

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

### 🔍 Deep Insights

* **Rule:** AsyncStorage (simple key-value storage, good for small data), MMKV (better performance, good for frequent access), SQLite (relational database, good for complex data).
* **Use Case:** MMKV is faster than AsyncStorage (performance).
* **Common Mistake:** Choose based on data complexity and performance needs.
* **Pro Tip:** SQLite provides full database capabilities.

---

### ⭐ Senior Takeaway

Choose storage based on data structure.

---

## 🧩 Q54. What's the difference between AsyncStorage and SecureStorage?

### 🧠 Concept

AsyncStorage stores data in plain text, while SecureStorage encrypts data for sensitive information like tokens. Always use SecureStorage for sensitive data.

---

### 💡 Example

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

### 🔍 Deep Insights

* **Rule:** AsyncStorage is plain text storage, not secure; SecureStorage is encrypted storage, secure for sensitive data.
* **Use Case:** Use SecureStorage for tokens, passwords, etc. (use cases).
* **Common Mistake:** SecureStorage is slightly slower due to encryption (performance).
* **Pro Tip:** SecureStorage provides better security.

---

### ⭐ Senior Takeaway

Always use SecureStorage for sensitive data.

---

## 🧩 Q55. How do you build an offline-first React Native app?

### 🧠 Concept

Use local storage, sync mechanisms, and network state detection to build apps that work offline. Provide seamless offline experience (user experience).

---

### 💡 Example

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

### 🔍 Deep Insights

* **Rule:** Store data locally for offline access (local storage).
* **Use Case:** Sync data when back online (sync mechanisms).
* **Common Mistake:** Monitor network state (network detection).
* **Pro Tip:** Queue actions when offline (queue actions).

---

### ⭐ Senior Takeaway

Provide seamless offline experience (user experience).

---

## 🧩 Q56. How do you handle background data sync and refresh?

### 🧠 Concept

Use background tasks, push notifications, and sync strategies to update data when the app is in the background. Handle platform-specific limitations.

---

### 💡 Example

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

### 🔍 Deep Insights

* **Rule:** Use background task libraries (background tasks).
* **Use Case:** Implement efficient sync strategies (sync strategies).
* **Common Mistake:** Keep data fresh with background updates (data freshness).
* **Pro Tip:** Consider battery impact (battery optimization).

---

### ⭐ Senior Takeaway

Handle platform-specific limitations.

---

## 🧩 Q57. What is batching in React Native?

### 🧠 Concept

Batching groups multiple state updates into a single render cycle, reducing the number of re-renders and improving performance. React 18 has improved batching.

---

### 💡 Example

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

### 🔍 Deep Insights

* **Rule:** React Native automatically batches updates (automatic batching).
* **Use Case:** Reduces number of re-renders (performance).
* **Common Mistake:** Groups synchronous updates together (synchronous updates).
* **Pro Tip:** May not batch async updates (async updates).

---

### ⭐ Senior Takeaway

React 18 has improved batching.

---

## 🧩 Q58. How do you manage environment variables in mobile builds?

### 🧠 Concept

Use platform-specific configuration files and build-time environment variables for different environments. Use build scripts to set environment variables.

---

### 💡 Example

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

### 🔍 Deep Insights

* **Rule:** Set variables at build time (build-time variables).
* **Use Case:** Different configs for iOS and Android (platform configuration).
* **Common Mistake:** Use .env files for configuration (environment files).
* **Pro Tip:** Don't expose sensitive data in environment variables.

---

### ⭐ Senior Takeaway

Use build scripts to set environment variables.

---

## 🧩 Q59. How do you handle secrets securely?

### 🧠 Concept

Use secure storage solutions, environment variables, and proper key management practices. Control access to sensitive data (access control).

---

### 💡 Example

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

### 🔍 Deep Insights

* **Rule:** Use keychain or keystore for sensitive data (secure storage).
* **Use Case:** Use build-time environment variables.
* **Common Mistake:** Implement proper key management practices (key management).
* **Pro Tip:** Encrypt sensitive data at rest (encryption).

---

### ⭐ Senior Takeaway

Control access to sensitive data (access control).

---

## 🧩 Q60. What are common state management anti-patterns to avoid?

### 🧠 Concept

Avoid prop drilling, mutating state directly, overusing global state, and not properly handling async state. Recognize and fix these patterns early.

---

### 💡 Example

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

### 🔍 Deep Insights

* **Rule:** Avoid passing props through multiple levels (prop drilling), never mutate state directly (state mutation).
* **Use Case:** Don't put everything in global state (overusing global state), handle async state properly (async state).
* **Common Mistake:** Follow React and React Native best practices.
* **Pro Tip:** Use proper state management patterns.

---

### ⭐ Senior Takeaway

Recognize and fix these patterns early.

---
