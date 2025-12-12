# 3. Navigation & App Lifecycle (Q22–31)

---

## 📍 Navigation

<div align="center">

[State Management & Data Persistence](02%29%20State%20Management%20%26%20Data%20Persistence.md) • [Home: README](../README.md) • [Native Modules & Platform APIs →](04%29%20Native Modules%20%26%20Platform Integrations.md)

[📋 Cheatsheet](React%20Native%20Interview%20Cheatsheet.md)

</div>

---

---

## Q22. 🧭 Different navigation solutions available for React Native

Popular navigation libraries include React Navigation, React Native Navigation, and Wix Navigator - choose based on performance needs and complexity. React Navigation (most popular, JavaScript-based), React Native Navigation (native navigation, better performance).

- **Trade-offs**: The catch is different features and performance characteristics (feature comparison) - different levels of community support. Choose based on performance needs and complexity, but watch out - Wix Navigator is alternative navigation solution.

Example:

```jsx
import { NavigationContainer } from '@react-navigation/native';
import { createStackNavigator } from '@react-navigation/stack';

const Stack = createStackNavigator();

```

---

## Q23. 🧭 Implementing stack navigation

Stack navigation uses a stack-based approach for hierarchical navigation, good for hierarchical content - choose pattern based on app structure. Stack navigation (push/pop navigation, good for hierarchical content).

- **Trade-offs**: The catch is different navigation patterns for different use cases (user experience) - mix and match patterns for complex apps. Choose pattern based on app structure, but watch out - can combine different navigation patterns (combination).

Example:

```jsx
const Stack = createStackNavigator();
<Stack.Navigator>
  <Stack.Screen name="Home" component={HomeScreen} />
  <Stack.Screen name="Details" component={DetailsScreen} />
</Stack.Navigator>

```

---

## Q24. 🧭 Implementing tab navigation

Tab navigation uses bottom/top tabs, good for main app sections - good for main app sections. Tab navigation (bottom/top tabs, good for main app sections).

- **Trade-offs**: The catch is can customize tab appearance and behavior - works well with stack navigation for nested navigation. Good for main app sections, but watch out - provides easy access to main app sections.

Example:

```jsx
import { createBottomTabNavigator } from '@react-navigation/bottom-tabs';

const Tab = createBottomTabNavigator();

<Tab.Navigator>
  <Tab.Screen name="Home" component={HomeScreen} />
  <Tab.Screen name="Profile" component={ProfileScreen} />
</Tab.Navigator>

```

---

## Q25. 🧭 Implementing drawer navigation

Drawer navigation uses a side drawer, good for app menu and settings - good for app menu and settings. Drawer navigation (side drawer, good for app menu and settings).

- **Trade-offs**: The catch is can customize drawer appearance and behavior - works well with other navigation patterns. Good for app menu and settings, but watch out - provides access to app menu and settings.

Example:

```jsx
import { createDrawerNavigator } from '@react-navigation/drawer';

const Drawer = createDrawerNavigator();

<Drawer.Navigator>
  <Drawer.Screen name="Home" component={HomeScreen} />
  <Drawer.Screen name="Settings" component={SettingsScreen} />
</Drawer.Navigator>

```

---

## Q26. 📱 Handling deep linking in React Native

Configure URL schemes and universal links in platform-specific files and handle navigation in the app - deep linking improves user experience. URL schemes (custom URL schemes for deep linking), Universal links (iOS-specific deep linking), App links (Android-specific deep linking).

- **Trade-offs**: The catch is different configuration for iOS and Android (platform configuration) - handle complex deep link scenarios. Deep linking improves user experience, but watch out - route deep links to appropriate screens (navigation handling).

Example:

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

---

## Q27. 🔧 Implementing universal links for iOS

Universal links are iOS-specific deep linking that work seamlessly with web URLs - configure in Info.plist and handle in app. Configure in Info.plist with associated domains.

- **Trade-offs**: The catch is requires proper server configuration - better user experience than custom URL schemes. Works seamlessly with web URLs, but watch out - works seamlessly with web URLs.

Example:

```jsx
import { Linking } from 'react-native';

useEffect(() => {
  const handleUniversalLink = (event) => {
    const { url } = event;
    // Handle universal link
  };
  Linking.addEventListener('url', handleUniversalLink);
  return () => Linking.removeEventListener('url', handleUniversalLink);
}, []);

```

---

## Q28. 📊 Handling app lifecycle changes with AppState API

Use the AppState API to listen for app state changes and handle appropriate actions - works on both iOS and Android (cross-platform). AppState API provides app state information.

- **Trade-offs**: The catch is handle app lifecycle events (lifecycle management) - manage resources based on app state (resource management). Works on both iOS and Android (cross-platform), but watch out - active, background, inactive states (state changes).

Example:

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

---

## Q29. 💡 ⏰ Using `useFocusEffect` for screen focus handling

useFocusEffect runs effects when a screen comes into focus, useful for data fetching and cleanup - works with React Navigation (navigation integration). Runs when screen comes into focus (focus events).

- **Trade-offs**: The catch is handle cleanup when screen loses focus (cleanup) - avoid unnecessary re-renders. Works with React Navigation (navigation integration), but watch out - useful for refreshing data (data fetching).

Example:

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

---

## Q30. 💡 Handling the hardware back button on Android

Use BackHandler API to customize back button behavior and prevent default actions when needed - works with navigation libraries (navigation integration). BackHandler API handles hardware back button.

- **Trade-offs**: The catch is provide appropriate back button behavior (user experience) - only works on Android (Android specific). Works with navigation libraries (navigation integration), but watch out - override default back button behavior (custom behavior).

Example:

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

---

## Q31. 📊 Persisting navigation state

Use navigation state persistence features or custom storage solutions to save and restore navigation state - different libraries have different persistence features. Save navigation state between sessions (state persistence).

- **Trade-offs**: The catch is use AsyncStorage or other storage solutions (storage solutions) - consider performance implications of state persistence. Different libraries have different persistence features, but watch out - maintain navigation state across app restarts (user experience).

Example:

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

---

---

## 📍 Navigation

<div align="center">

[State Management & Data Persistence](02%29%20State%20Management%20%26%20Data%20Persistence.md) • [Home: README](../README.md) • [Native Modules & Platform APIs →](04%29%20Native Modules%20%26%20Platform Integrations.md)

[📋 Cheatsheet](React%20Native%20Interview%20Cheatsheet.md)

</div>

---
