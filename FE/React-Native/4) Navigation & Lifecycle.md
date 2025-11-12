# ⚙️ 4. Navigation & Lifecycle (Q31–40)

---

## 🧩 Q31. What are the different navigation solutions available for React Native?

### 🧠 Concept

Popular navigation libraries include React Navigation, React Native Navigation, and Wix Navigator. Choose based on performance needs and complexity.

---

### 💡 Example

```jsx
import { NavigationContainer } from '@react-navigation/native';
import { createStackNavigator } from '@react-navigation/stack';

const Stack = createStackNavigator();
```

---

### 🔍 Deep Insights

* **Rule:** React Navigation (most popular, JavaScript-based), React Native Navigation (native navigation, better performance).
* **Use Case:** Wix Navigator is alternative navigation solution.
* **Common Mistake:** Different features and performance characteristics (feature comparison).
* **Pro Tip:** Different levels of community support.

---

### ⭐ Senior Takeaway

Choose based on performance needs and complexity.

---

## 🧩 Q32. How do you implement stack navigation?

### 🧠 Concept

Stack navigation uses a stack-based approach for hierarchical navigation, good for hierarchical content. Choose pattern based on app structure.

---

### 💡 Example

```jsx
const Stack = createStackNavigator();
<Stack.Navigator>
  <Stack.Screen name="Home" component={HomeScreen} />
  <Stack.Screen name="Details" component={DetailsScreen} />
</Stack.Navigator>
```

---

### 🔍 Deep Insights

* **Rule:** Stack navigation (push/pop navigation, good for hierarchical content).
* **Use Case:** Can combine different navigation patterns (combination).
* **Common Mistake:** Different navigation patterns for different use cases (user experience).
* **Pro Tip:** Mix and match patterns for complex apps.

---

### ⭐ Senior Takeaway

Choose pattern based on app structure.

---

## 🧩 Q33. How do you implement tab navigation?

### 🧠 Concept

Tab navigation uses bottom/top tabs, good for main app sections. Good for main app sections.

---

### 💡 Example

```jsx
import { createBottomTabNavigator } from '@react-navigation/bottom-tabs';

const Tab = createBottomTabNavigator();

<Tab.Navigator>
  <Tab.Screen name="Home" component={HomeScreen} />
  <Tab.Screen name="Profile" component={ProfileScreen} />
</Tab.Navigator>
```

---

### 🔍 Deep Insights

* **Rule:** Tab navigation (bottom/top tabs, good for main app sections).
* **Use Case:** Provides easy access to main app sections.
* **Common Mistake:** Can customize tab appearance and behavior.
* **Pro Tip:** Works well with stack navigation for nested navigation.

---

### ⭐ Senior Takeaway

Good for main app sections.

---

## 🧩 Q34. How do you implement drawer navigation?

### 🧠 Concept

Drawer navigation uses a side drawer, good for app menu and settings. Good for app menu and settings.

---

### 💡 Example

```jsx
import { createDrawerNavigator } from '@react-navigation/drawer';

const Drawer = createDrawerNavigator();

<Drawer.Navigator>
  <Drawer.Screen name="Home" component={HomeScreen} />
  <Drawer.Screen name="Settings" component={SettingsScreen} />
</Drawer.Navigator>
```

---

### 🔍 Deep Insights

* **Rule:** Drawer navigation (side drawer, good for app menu and settings).
* **Use Case:** Provides access to app menu and settings.
* **Common Mistake:** Can customize drawer appearance and behavior.
* **Pro Tip:** Works well with other navigation patterns.

---

### ⭐ Senior Takeaway

Good for app menu and settings.

---

## 🧩 Q35. How do you handle deep linking in React Native?

### 🧠 Concept

Configure URL schemes and universal links in platform-specific files and handle navigation in the app. Deep linking improves user experience.

---

### 💡 Example

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

### 🔍 Deep Insights

* **Rule:** URL schemes (custom URL schemes for deep linking), Universal links (iOS-specific deep linking), App links (Android-specific deep linking).
* **Use Case:** Route deep links to appropriate screens (navigation handling).
* **Common Mistake:** Different configuration for iOS and Android (platform configuration).
* **Pro Tip:** Handle complex deep link scenarios.

---

### ⭐ Senior Takeaway

Deep linking improves user experience.

---

## 🧩 Q36. How do you implement universal links for iOS?

### 🧠 Concept

Universal links are iOS-specific deep linking that work seamlessly with web URLs. Configure in Info.plist and handle in app.

---

### 💡 Example

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

### 🔍 Deep Insights

* **Rule:** Configure in Info.plist with associated domains.
* **Use Case:** Works seamlessly with web URLs.
* **Common Mistake:** Requires proper server configuration.
* **Pro Tip:** Better user experience than custom URL schemes.

---

### ⭐ Senior Takeaway

Works seamlessly with web URLs.

---

## 🧩 Q37. How do you handle app lifecycle changes with AppState API?

### 🧠 Concept

Use the AppState API to listen for app state changes and handle appropriate actions. Works on both iOS and Android (cross-platform).

---

### 💡 Example

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

### 🔍 Deep Insights

* **Rule:** AppState API provides app state information.
* **Use Case:** active, background, inactive states (state changes).
* **Common Mistake:** Handle app lifecycle events (lifecycle management).
* **Pro Tip:** Manage resources based on app state (resource management).

---

### ⭐ Senior Takeaway

Works on both iOS and Android (cross-platform).

---

## 🧩 Q38. How do you use `useFocusEffect` for screen focus handling?

### 🧠 Concept

useFocusEffect runs effects when a screen comes into focus, useful for data fetching and cleanup. Works with React Navigation (navigation integration).

---

### 💡 Example

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

### 🔍 Deep Insights

* **Rule:** Runs when screen comes into focus (focus events).
* **Use Case:** Useful for refreshing data (data fetching).
* **Common Mistake:** Handle cleanup when screen loses focus (cleanup).
* **Pro Tip:** Avoid unnecessary re-renders.

---

### ⭐ Senior Takeaway

Works with React Navigation (navigation integration).

---

## 🧩 Q39. How do you handle the hardware back button on Android?

### 🧠 Concept

Use BackHandler API to customize back button behavior and prevent default actions when needed. Works with navigation libraries (navigation integration).

---

### 💡 Example

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

### 🔍 Deep Insights

* **Rule:** BackHandler API handles hardware back button.
* **Use Case:** Override default back button behavior (custom behavior).
* **Common Mistake:** Provide appropriate back button behavior (user experience).
* **Pro Tip:** Only works on Android (Android specific).

---

### ⭐ Senior Takeaway

Works with navigation libraries (navigation integration).

---

## 🧩 Q40. How do you persist navigation state?

### 🧠 Concept

Use navigation state persistence features or custom storage solutions to save and restore navigation state. Different libraries have different persistence features.

---

### 💡 Example

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

### 🔍 Deep Insights

* **Rule:** Save navigation state between sessions (state persistence).
* **Use Case:** Maintain navigation state across app restarts (user experience).
* **Common Mistake:** Use AsyncStorage or other storage solutions (storage solutions).
* **Pro Tip:** Consider performance implications of state persistence.

---

### ⭐ Senior Takeaway

Different libraries have different persistence features.

---
