# ⚙️ 4. Navigation & Lifecycle (Q31–40)

---

## 31) What are the popular navigation solutions for React Native?

Popular navigation libraries include React Navigation, React Native Navigation, and Wix Navigator.

```jsx
import { NavigationContainer } from '@react-navigation/native';
import { createStackNavigator } from '@react-navigation/stack';

const Stack = createStackNavigator();
```

- **Core Libraries**: React Navigation (most popular, JavaScript-based), React Native Navigation (native navigation, better performance)
- **Real-World Options**: Wix Navigator is alternative navigation solution
- **Common Comparison**: Different features and performance characteristics (feature comparison)
- **Advanced Consideration**: Different levels of community support
- **Interview Tip**: Explain that choose based on performance needs and complexity

---

## 32) What is the difference between **Stack**, **Tab**, and **Drawer** navigation patterns?

Stack navigation uses a stack-based approach, Tab navigation uses bottom/top tabs, and Drawer navigation uses a side drawer.

```jsx
const Stack = createStackNavigator();
<Stack.Navigator>
  <Stack.Screen name="Home" component={HomeScreen} />
  <Stack.Screen name="Details" component={DetailsScreen} />
</Stack.Navigator>
```

- **Core Patterns**: Stack navigation (push/pop navigation, good for hierarchical content), Tab navigation (bottom/top tabs, good for main app sections), Drawer navigation (side drawer, good for app menu and settings)
- **Real-World Use**: Can combine different navigation patterns (combination)
- **Common Advantage**: Different navigation patterns for different use cases (user experience)
- **Advanced Feature**: Mix and match patterns for complex apps
- **Interview Tip**: Explain that choose pattern based on app structure

---

## 33) How do you handle **deep linking** and **universal links**?

Configure URL schemes and universal links in platform-specific files and handle navigation in the app.

```jsx
import { Linking } from 'react-native';

function App() {
  useEffect(() => {
    const handleDeepLink = (url) => {
      // Navigate based on URL
    };
    Linking.addEventListener('url', handleDeepLink);
    return () => Linking.removeEventListener('url', handleDeepLink);
  }, []);
}
```

- **Core Mechanisms**: URL schemes (custom URL schemes for deep linking), Universal links (iOS-specific deep linking), App links (Android-specific deep linking)
- **Real-World Use**: Route deep links to appropriate screens (navigation handling)
- **Common Configuration**: Different configuration for iOS and Android (platform configuration)
- **Advanced Feature**: Handle complex deep link scenarios
- **Interview Tip**: Explain that deep linking improves user experience

---

## 34) How do you detect app lifecycle changes (foreground, background, inactive)?

Use the AppState API to listen for app state changes and handle appropriate actions.

```jsx
import { AppState } from 'react-native';

function App() {
  const [appState, setAppState] = useState(AppState.currentState);
  
  useEffect(() => {
    const subscription = AppState.addEventListener('change', nextAppState => {
      setAppState(nextAppState);
    });
    return () => subscription.remove();
  }, []);
}
```

- **Core API**: AppState API provides app state information
- **Real-World States**: active, background, inactive states (state changes)
- **Common Use**: Handle app lifecycle events (lifecycle management)
- **Advanced Feature**: Manage resources based on app state (resource management)
- **Interview Tip**: Explain that provide appropriate behavior for each state (user experience)

---

## 35) What is the role of the **AppState API**?

AppState API provides information about the current app state and allows listening for state changes.

```jsx
import { AppState } from 'react-native';

function useAppState() {
  const [appState, setAppState] = useState(AppState.currentState);
  
  useEffect(() => {
    const subscription = AppState.addEventListener('change', setAppState);
    return () => subscription.remove();
  }, []);
  
  return appState;
}
```

- **Core Purpose**: Provides current app state (state information)
- **Real-World Use**: Listen for state changes (event listening)
- **Common Use**: Manage app lifecycle (lifecycle management)
- **Advanced Feature**: Handle resources based on state (resource management)
- **Interview Tip**: Explain that works on both iOS and Android (cross-platform)

---

## 36) How do you handle **screen focus** with `useFocusEffect`?

useFocusEffect runs effects when a screen comes into focus, useful for data fetching and cleanup.

```jsx
import { useFocusEffect } from '@react-navigation/native';

function ProfileScreen() {
  const [user, setUser] = useState(null);
  
  useFocusEffect(
    useCallback(() => {
      fetchUser().then(setUser);
      return () => {
        // Cleanup when screen loses focus
      };
    }, [])
  );
}
```

- **Core Feature**: Runs when screen comes into focus (focus events)
- **Real-World Use**: Useful for refreshing data (data fetching)
- **Common Practice**: Handle cleanup when screen loses focus (cleanup)
- **Performance**: Avoid unnecessary re-renders
- **Interview Tip**: Explain that works with React Navigation (navigation integration)

---

## 37) How do you handle hardware back button behavior on Android?

Use BackHandler API to customize back button behavior and prevent default actions when needed.

```jsx
import { BackHandler } from 'react-native';

function MyScreen() {
  useEffect(() => {
    const backAction = () => {
      // Show confirmation dialog
      return true; // Prevent default behavior
    };
    BackHandler.addEventListener('hardwareBackPress', backAction);
    return () => BackHandler.removeEventListener('hardwareBackPress', backAction);
  }, []);
}
```

- **Core API**: BackHandler API handles hardware back button
- **Real-World Use**: Override default back button behavior (custom behavior)
- **Common Practice**: Provide appropriate back button behavior (user experience)
- **Platform Limitation**: Only works on Android (Android specific)
- **Interview Tip**: Explain that works with navigation libraries (navigation integration)

---

## 38) How can you persist navigation state between sessions?

Use navigation state persistence features or custom storage solutions to save and restore navigation state.

```jsx
import AsyncStorage from '@react-native-async-storage/async-storage';

const PERSISTENCE_KEY = 'NAVIGATION_STATE';

function App() {
  const [isReady, setIsReady] = useState(false);
  const [initialState, setInitialState] = useState();
  
  useEffect(() => {
    AsyncStorage.getItem(PERSISTENCE_KEY).then(savedState => {
      setInitialState(savedState ? JSON.parse(savedState) : undefined);
      setIsReady(true);
    });
  }, []);
  
  if (!isReady) return null;
  
  return (
    <NavigationContainer
      initialState={initialState}
      onStateChange={state => AsyncStorage.setItem(PERSISTENCE_KEY, JSON.stringify(state))}
    >
      {/* Navigation */}
    </NavigationContainer>
  );
}
```

- **Core Feature**: Save navigation state between sessions (state persistence)
- **Real-World Benefit**: Maintain navigation state across app restarts (user experience)
- **Common Solutions**: Use AsyncStorage or other storage solutions (storage solutions)
- **Performance**: Consider performance implications of state persistence
- **Interview Tip**: Explain that different libraries have different persistence features

---

## 39) What are **navigation guards**, and how can they be implemented?

Navigation guards prevent navigation based on conditions, implemented using navigation listeners and conditional rendering.

```jsx
import { useFocusEffect } from '@react-navigation/native';

function ProtectedScreen() {
  const [isAuthenticated, setIsAuthenticated] = useState(false);
  
  useFocusEffect(
    useCallback(() => {
      if (!isAuthenticated) {
        // Redirect to login
      }
    }, [isAuthenticated])
  );
}
```

- **Core Purpose**: Control access to screens based on conditions (access control)
- **Real-World Use**: Check authentication status before navigation (authentication)
- **Common Practice**: Provide appropriate navigation behavior (user experience)
- **Advanced Feature**: Implement security measures in navigation (security)
- **Interview Tip**: Explain that use conditional rendering for navigation guards

---

## 40) How do you integrate custom gestures or animations in navigation transitions?

Use platform-specific animation libraries and gesture handlers to create custom navigation transitions.

```jsx
import { PanGestureHandler } from 'react-native-gesture-handler';
import Animated, { useAnimatedGestureHandler } from 'react-native-reanimated';

function CustomGestureScreen() {
  const translateX = useSharedValue(0);
  
  const gestureHandler = useAnimatedGestureHandler({
    onActive: (event) => {
      translateX.value = event.translationX;
    }
  });
  
  return (
    <PanGestureHandler onGestureEvent={gestureHandler}>
      <Animated.View style={{ transform: [{ translateX }] }}>
        {/* Content */}
      </Animated.View>
    </PanGestureHandler>
  );
}
```

- **Core Libraries**: Use gesture handling libraries (gesture handlers), use animation libraries for smooth transitions (animation libraries)
- **Real-World Use**: Integrate with platform-specific navigation (platform integration)
- **Common Benefit**: Provide intuitive gesture-based navigation (user experience)
- **Performance**: Consider performance implications of custom animations
- **Interview Tip**: Explain that custom animations improve UX

---
