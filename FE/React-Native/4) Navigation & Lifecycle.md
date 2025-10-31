# ⚙️ 4. Navigation & Lifecycle (Q31–40)

---

## 31) What are the popular navigation solutions for React Native?

Concept:
Popular navigation libraries include React Navigation, React Native Navigation, and Wix Navigator.

Example:
```jsx
// React Navigation setup
import { NavigationContainer } from '@react-navigation/native';
import { createStackNavigator } from '@react-navigation/stack';

const Stack = createStackNavigator();

```

Deep Insight:
- **React Navigation**: Most popular, JavaScript-based
- **React Native Navigation**: Native navigation, better performance
- **Wix Navigator**: Alternative navigation solution
- **Feature Comparison**: Different features and performance characteristics
- **Community Support**: Different levels of community support

---

## 32) What is the difference between **Stack**, **Tab**, and **Drawer** navigation patterns?

Concept:
Stack navigation uses a stack-based approach, Tab navigation uses bottom/top tabs, and Drawer navigation uses a side drawer.

Example:
```jsx
// Stack Navigation
const Stack = createStackNavigator();
<Stack.Navigator>
  <Stack.Screen name="Home" component={HomeScreen} />
  <Stack.Screen name="Details" component={DetailsScreen} />
</Stack.Navigator>
```

Deep Insight:
- **Stack Navigation**: Push/pop navigation, good for hierarchical content
- **Tab Navigation**: Bottom/top tabs, good for main app sections
- **Drawer Navigation**: Side drawer, good for app menu and settings
- **Combination**: Can combine different navigation patterns
- **User Experience**: Different navigation patterns for different use cases

---

## 33) How do you handle **deep linking** and **universal links**?

Concept:
Configure URL schemes and universal links in platform-specific files and handle navigation in the app.

Example:
```jsx
// Deep linking handling
import { Linking } from 'react-native';

function App() {
  useEffect(() => {
    const handleDeepLink = (url) => {
```

Deep Insight:
- **URL Schemes**: Custom URL schemes for deep linking
- **Universal Links**: iOS-specific deep linking
- **App Links**: Android-specific deep linking
- **Navigation Handling**: Route deep links to appropriate screens
- **Platform Configuration**: Different configuration for iOS and Android

---

## 34) How do you detect app lifecycle changes (foreground, background, inactive)?

Concept:
Use the AppState API to listen for app state changes and handle appropriate actions.

Example:
```jsx
import { AppState } from 'react-native';

function App() {
  const [appState, setAppState] = useState(AppState.currentState);
  
  useEffect(() => {
```

Deep Insight:
- **AppState API**: Provides app state information
- **State Changes**: active, background, inactive states
- **Lifecycle Management**: Handle app lifecycle events
- **Resource Management**: Manage resources based on app state
- **User Experience**: Provide appropriate behavior for each state

---

## 35) What is the role of the **AppState API**?

Concept:
AppState API provides information about the current app state and allows listening for state changes.

Example:
```jsx
import { AppState } from 'react-native';

function useAppState() {
  const [appState, setAppState] = useState(AppState.currentState);
  
  useEffect(() => {
```

Deep Insight:
- **State Information**: Provides current app state
- **Event Listening**: Listen for state changes
- **Lifecycle Management**: Manage app lifecycle
- **Resource Management**: Handle resources based on state
- **Cross-Platform**: Works on both iOS and Android

---

## 36) How do you handle **screen focus** with `useFocusEffect`?

Concept:
useFocusEffect runs effects when a screen comes into focus, useful for data fetching and cleanup.

Example:
```jsx
import { useFocusEffect } from '@react-navigation/native';

function ProfileScreen() {
  const [user, setUser] = useState(null);
  
  useFocusEffect(
```

Deep Insight:
- **Focus Events**: Runs when screen comes into focus
- **Data Fetching**: Useful for refreshing data
- **Cleanup**: Handle cleanup when screen loses focus
- **Performance**: Avoid unnecessary re-renders
- **Navigation Integration**: Works with React Navigation

---

## 37) How do you handle hardware back button behavior on Android?

Concept:
Use BackHandler API to customize back button behavior and prevent default actions when needed.

Example:
```jsx
import { BackHandler } from 'react-native';

function MyScreen() {
  useEffect(() => {
    const backAction = () => {
      // Show confirmation dialog
```

Deep Insight:
- **BackHandler API**: Handles hardware back button
- **Custom Behavior**: Override default back button behavior
- **User Experience**: Provide appropriate back button behavior
- **Android Specific**: Only works on Android
- **Navigation Integration**: Works with navigation libraries

---

## 38) How can you persist navigation state between sessions?

Concept:
Use navigation state persistence features or custom storage solutions to save and restore navigation state.

Example:
```jsx
import AsyncStorage from '@react-native-async-storage/async-storage';

const PERSISTENCE_KEY = 'NAVIGATION_STATE';

function App() {
  const [isReady, setIsReady] = useState(false);
```

Deep Insight:
- **State Persistence**: Save navigation state between sessions
- **User Experience**: Maintain navigation state across app restarts
- **Storage Solutions**: Use AsyncStorage or other storage solutions
- **Performance**: Consider performance implications of state persistence
- **Navigation Libraries**: Different libraries have different persistence features

---

## 39) What are **navigation guards**, and how can they be implemented?

Concept:
Navigation guards prevent navigation based on conditions, implemented using navigation listeners and conditional rendering.

Example:
```jsx
import { useFocusEffect } from '@react-navigation/native';

function ProtectedScreen() {
  const [isAuthenticated, setIsAuthenticated] = useState(false);
  
  useFocusEffect(
```

Deep Insight:
- **Access Control**: Control access to screens based on conditions
- **Authentication**: Check authentication status before navigation
- **User Experience**: Provide appropriate navigation behavior
- **Security**: Implement security measures in navigation
- **Conditional Rendering**: Use conditional rendering for navigation guards

---

## 40) How do you integrate custom gestures or animations in navigation transitions?

Concept:
Use platform-specific animation libraries and gesture handlers to create custom navigation transitions.

Example:
```jsx
import { PanGestureHandler } from 'react-native-gesture-handler';
import Animated, { useAnimatedGestureHandler } from 'react-native-reanimated';

function CustomGestureScreen() {
  const translateX = useSharedValue(0);
  
```

Deep Insight:
- **Gesture Handlers**: Use gesture handling libraries
- **Animation Libraries**: Use animation libraries for smooth transitions
- **Platform Integration**: Integrate with platform-specific navigation
- **User Experience**: Provide intuitive gesture-based navigation
- **Performance**: Consider performance implications of custom animations

---
