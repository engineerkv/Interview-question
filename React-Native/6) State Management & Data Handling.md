# 🧩 6. State Management & Data Handling (Q51–60)

---

## 51) What are popular state management tools in React Native (Redux, Recoil, Zustand)?

Concept:
Popular tools include Redux, Redux Toolkit, Recoil, Zustand, and Context API for state management.

Example:
```jsx
// Redux Toolkit
import { createSlice, configureStore } from '@reduxjs/toolkit';

const counterSlice = createSlice({
  name: 'counter',
  initialState: { count: 0 },
```

Deep Insight:
- **Redux**: Most popular, complex but powerful
- **Redux Toolkit**: Simplified Redux with less boilerplate
- **Recoil**: Facebook's state management library
- **Zustand**: Lightweight and simple
- **Context API**: Built-in React solution for simple state

---

## 52) How do you decide between Redux Toolkit and Context API for app-wide state?

Concept:
Use Redux Toolkit for complex state logic and multiple components, Context API for simple state and fewer components.

Example:
```jsx
// Context API - for simple state
const ThemeContext = createContext();

function ThemeProvider({ children }) {
  const [theme, setTheme] = useState('light');
  
```

Deep Insight:
- **Context API**: Good for simple state and fewer components
- **Redux Toolkit**: Better for complex state and many components
- **Performance**: Redux has better performance for large apps
- **Developer Experience**: Redux Toolkit provides better debugging
- **Learning Curve**: Context API is easier to learn

---

## 53) How do you persist data locally (AsyncStorage, MMKV, SQLite)?

Concept:
Use AsyncStorage for simple key-value storage, MMKV for better performance, or SQLite for complex relational data.

Example:
```jsx
// AsyncStorage
import AsyncStorage from '@react-native-async-storage/async-storage';

const storeData = async (key, value) => {
  try {
    await AsyncStorage.setItem(key, JSON.stringify(value));
```

Deep Insight:
- **AsyncStorage**: Simple key-value storage, good for small data
- **MMKV**: Better performance, good for frequent access
- **SQLite**: Relational database, good for complex data
- **Performance**: MMKV is faster than AsyncStorage
- **Use Cases**: Choose based on data complexity and performance needs

---

## 54) What's the difference between AsyncStorage and SecureStorage?

Concept:
AsyncStorage stores data in plain text, while SecureStorage encrypts data for sensitive information like tokens.

Example:
```jsx
// AsyncStorage - plain text
import AsyncStorage from '@react-native-async-storage/async-storage';

const storeToken = async (token) => {
  await AsyncStorage.setItem('authToken', token);
};
```

Deep Insight:
- **AsyncStorage**: Plain text storage, not secure
- **SecureStorage**: Encrypted storage, secure for sensitive data
- **Use Cases**: Use SecureStorage for tokens, passwords, etc.
- **Performance**: SecureStorage is slightly slower due to encryption
- **Security**: SecureStorage provides better security

---

## 55) How do you build an **offline-first** React Native app?

Concept:
Use local storage, sync mechanisms, and network state detection to build apps that work offline.

Example:
```jsx
import NetInfo from '@react-native-community/netinfo';
import AsyncStorage from '@react-native-async-storage/async-storage';

function OfflineFirstApp() {
  const [isOnline, setIsOnline] = useState(true);
  const [pendingActions, setPendingActions] = useState([]);
```

Deep Insight:
- **Local Storage**: Store data locally for offline access
- **Sync Mechanisms**: Sync data when back online
- **Network Detection**: Monitor network state
- **Queue Actions**: Queue actions when offline
- **User Experience**: Provide seamless offline experience

---

## 56) How do you handle background data sync and refresh?

Concept:
Use background tasks, push notifications, and sync strategies to update data when the app is in the background.

Example:
```jsx
import BackgroundJob from 'react-native-background-job';

function BackgroundSync() {
  useEffect(() => {
    // Schedule background sync
    BackgroundJob.register({
```

Deep Insight:
- **Background Tasks**: Use background task libraries
- **Sync Strategies**: Implement efficient sync strategies
- **Data Freshness**: Keep data fresh with background updates
- **Battery Optimization**: Consider battery impact
- **Platform Limitations**: Handle platform-specific limitations

---

## 57) What is batching in React Native, and how does it improve performance?

Concept:
Batching groups multiple state updates into a single render cycle, reducing the number of re-renders and improving performance.

Example:
```jsx
function BatchingExample() {
  const [count, setCount] = useState(0);
  const [name, setName] = useState('');
  
  const handleUpdate = () => {
    // These updates are batched together
```

Deep Insight:
- **Automatic Batching**: React Native automatically batches updates
- **Performance**: Reduces number of re-renders
- **Synchronous Updates**: Groups synchronous updates together
- **Async Updates**: May not batch async updates
- **React 18**: Improved batching in React 18

---

## 58) How do you manage environment variables in mobile builds?

Concept:
Use platform-specific configuration files and build-time environment variables for different environments.

Example:
```jsx
// Environment configuration
const config = {
  development: {
    apiUrl: 'https://dev-api.example.com',
    debug: true
  },
```

Deep Insight:
- **Build-time Variables**: Set variables at build time
- **Platform Configuration**: Different configs for iOS and Android
- **Environment Files**: Use .env files for configuration
- **Security**: Don't expose sensitive data in environment variables
- **Build Scripts**: Use build scripts to set environment variables

---

## 59) How do you handle secrets securely (e.g., API keys, tokens)?

Concept:
Use secure storage solutions, environment variables, and proper key management practices.

Example:
```jsx
import { getItem, setItem } from 'react-native-keychain';

// Store API key securely
const storeApiKey = async (apiKey) => {
  try {
    await setItem('apiKey', apiKey);
```

Deep Insight:
- **Secure Storage**: Use keychain or keystore for sensitive data
- **Environment Variables**: Use build-time environment variables
- **Key Management**: Implement proper key management practices
- **Encryption**: Encrypt sensitive data at rest
- **Access Control**: Control access to sensitive data

---

## 60) What are common state management anti-patterns to avoid?

Concept:
Avoid prop drilling, mutating state directly, overusing global state, and not properly handling async state.

Example:
```jsx
// ❌ Anti-pattern: Prop drilling
function App() {
  const [user, setUser] = useState(null);
  
  return (
    <div>
```

Deep Insight:
- **Prop Drilling**: Avoid passing props through multiple levels
- **State Mutation**: Never mutate state directly
- **Overusing Global State**: Don't put everything in global state
- **Async State**: Handle async state properly
- **Best Practices**: Follow React and React Native best practices

---
