# 3. Navigation & App Lifecycle (Q22–30)

---

## 📍 Navigation

<div align="center">

[State Management & Data Persistence](02%29%20State%20Management%20%26%20Data%20Persistence.md) • [Home: README](../README.md) • [Native Modules & Platform APIs →](04%29%20Native%20Modules%20%26%20Platform%20APIs.md)

[📋 Cheatsheet](React%20Native%20Interview%20Cheatsheet.md)

</div>

---

---

## Q22. 🧭 Implementing stack navigation

Stack navigation uses a stack-based approach for hierarchical navigation, good for hierarchical content - choose pattern based on app structure. Stack navigation (push/pop navigation, good for hierarchical content).

- **Trade-offs**: The catch is different navigation patterns for different use cases (user experience) - mix and match patterns for complex apps. Choose pattern based on app structure, but watch out - can combine different navigation patterns (combination).

Example:

```jsx
import { Navigation } from 'react-native-navigation';
import { View, Text, Button } from 'react-native';

// Register screens
Navigation.registerComponent('HomeScreen', () => HomeScreen);
Navigation.registerComponent('DetailsScreen', () => DetailsScreen);

// Home Screen Component
function HomeScreen({ componentId }) {
  const navigateToDetails = () => {
    Navigation.push(componentId, {
      component: {
        name: 'DetailsScreen',
        passProps: { itemId: 123 },
        options: {
          topBar: {
            title: { text: 'Details' }
          }
        }
      }
    });
  };

  return (
    <View>
      <Text>Home Screen</Text>
      <Button title="Go to Details" onPress={navigateToDetails} />
    </View>
  );
}

// Details Screen Component
function DetailsScreen({ componentId, itemId }) {
  return (
    <View>
      <Text>Details Screen - Item ID: {itemId}</Text>
      <Button
        title="Go Back"
        onPress={() => Navigation.pop(componentId)}
      />
    </View>
  );
}

// Initialize navigation
function startApp() {
  Navigation.setRoot({
    root: {
      stack: {
        children: [{
          component: {
            name: 'HomeScreen',
            options: {
              topBar: {
                title: { text: 'Home' }
              }
            }
          }
        }]
      }
    }
  });
}

startApp();
```

---

## Q23. 🧭 Implementing tab navigation

Tab navigation uses bottom/top tabs, good for main app sections - good for main app sections. Tab navigation (bottom/top tabs, good for main app sections).

- **Trade-offs**: The catch is can customize tab appearance and behavior - works well with stack navigation for nested navigation. Good for main app sections, but watch out - provides easy access to main app sections.

Example:

```jsx
import { Navigation } from 'react-native-navigation';
import { View, Text } from 'react-native';

// Register screens
Navigation.registerComponent('HomeScreen', () => HomeScreen);
Navigation.registerComponent('ProfileScreen', () => ProfileScreen);

// Home Screen Component
function HomeScreen() {
  return (
    <View>
      <Text>Home Screen</Text>
    </View>
  );
}

// Profile Screen Component
function ProfileScreen() {
  return (
    <View>
      <Text>Profile Screen</Text>
    </View>
  );
}

// Initialize navigation
function startApp() {
  Navigation.setRoot({
    root: {
      bottomTabs: {
        children: [
          {
            stack: {
              children: [{
                component: {
                  name: 'HomeScreen',
                  options: {
                    bottomTab: {
                      text: 'Home',
                      icon: require('./assets/home.png')
                    },
                    topBar: {
                      title: { text: 'Home' }
                    }
                  }
                }
              }]
            }
          },
          {
            stack: {
              children: [{
                component: {
                  name: 'ProfileScreen',
                  options: {
                    bottomTab: {
                      text: 'Profile',
                      icon: require('./assets/profile.png')
                    },
                    topBar: {
                      title: { text: 'Profile' }
                    }
                  }
                }
              }]
            }
          }
        ]
      }
    }
  });
}

startApp();
```

---

## Q24. 🧭 Implementing drawer navigation

Drawer navigation uses a side drawer, good for app menu and settings - good for app menu and settings. Drawer navigation (side drawer, good for app menu and settings).

- **Trade-offs**: The catch is can customize drawer appearance and behavior - works well with other navigation patterns. Good for app menu and settings, but watch out - provides access to app menu and settings.

Example:

```jsx
import { Navigation } from 'react-native-navigation';
import { View, Text, Button } from 'react-native';

// Register screens
Navigation.registerComponent('HomeScreen', () => HomeScreen);
Navigation.registerComponent('DrawerScreen', () => DrawerScreen);

// Home Screen Component
function HomeScreen({ componentId }) {
  const openDrawer = () => {
    Navigation.mergeOptions(componentId, {
      sideMenu: {
        left: { visible: true }
      }
    });
  };

  return (
    <View>
      <Text>Home Screen</Text>
      <Button title="Open Drawer" onPress={openDrawer} />
    </View>
  );
}

// Drawer Screen Component
function DrawerScreen({ componentId }) {
  const navigateToScreen = (screenName) => {
    Navigation.mergeOptions(componentId, {
      sideMenu: {
        left: { visible: false }
      }
    });
    Navigation.push(componentId, {
      component: { name: screenName }
    });
  };

  return (
    <View>
      <Text>Drawer Menu</Text>
      <Button title="Settings" onPress={() => navigateToScreen('SettingsScreen')} />
    </View>
  );
}

// Initialize navigation
function startApp() {
  Navigation.setRoot({
    root: {
      sideMenu: {
        left: {
          component: {
            name: 'DrawerScreen',
            options: {
              drawer: {
                width: 280
              }
            }
          }
        },
        center: {
          stack: {
            children: [{
              component: {
                name: 'HomeScreen',
                options: {
                  topBar: {
                    title: { text: 'Home' },
                    leftButtons: [{
                      id: 'menuButton',
                      icon: require('./assets/menu.png'),
                      color: 'black'
                    }]
                  }
                }
              }
            }]
          }
        }
      }
    }
  });
}

startApp();
```

---

## Q25. 📱 Handling deep linking in React Native

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

## Q26. 🔧 Implementing universal links for iOS

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

## Q27. 📊 Handling app lifecycle changes with AppState API

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

## Q28. 💡 ⏰ Using screen lifecycle events for focus handling

Screen lifecycle events run when screens appear or disappear, useful for data fetching and cleanup - works with React Native Navigation (navigation integration). Runs when screen appears or disappears (lifecycle events).

- **Trade-offs**: The catch is handle cleanup when screen disappears (cleanup) - avoid unnecessary re-renders. Works with React Native Navigation (navigation integration), but watch out - useful for refreshing data (data fetching).

Example:

```jsx
import { Navigation } from 'react-native-navigation';

class ProfileScreen extends React.Component {
  componentDidAppear() {
    // Screen came into focus
    this.fetchUser();
  }

  componentDidDisappear() {
    // Screen lost focus
    // Cleanup if needed
  }

  fetchUser = () => {
    // Fetch user data
  }
}

```

---

## Q29. 💡 Handling the hardware back button on Android

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

## Q30. 📊 Persisting navigation state

Use navigation state persistence features or custom storage solutions to save and restore navigation state - different libraries have different persistence features. Save navigation state between sessions (state persistence).

- **Trade-offs**: The catch is use AsyncStorage or other storage solutions (storage solutions) - consider performance implications of state persistence. Different libraries have different persistence features, but watch out - maintain navigation state across app restarts (user experience).

Example:

```jsx
import AsyncStorage from '@react-native-async-storage/async-storage';
import { Navigation } from 'react-native-navigation';

const PERSISTENCE_KEY = 'NAVIGATION_STATE';

// Save navigation state
const saveNavigationState = async (state) => {
  try {
    await AsyncStorage.setItem(PERSISTENCE_KEY, JSON.stringify(state));
  } catch (error) {
    console.error('Error saving navigation state:', error);
  }
};

// Restore navigation state
const restoreNavigationState = async () => {
  try {
    const savedState = await AsyncStorage.getItem(PERSISTENCE_KEY);
    if (savedState) {
      const state = JSON.parse(savedState);
      Navigation.setRoot(state);
    }
  } catch (error) {
    console.error('Error restoring navigation state:', error);
  }
};

```

---

---

## 📍 Navigation

<div align="center">

[State Management & Data Persistence](02%29%20State%20Management%20%26%20Data%20Persistence.md) • [Home: README](../README.md) • [Native Modules & Platform APIs →](04%29%20Native%20Modules%20%26%20Platform%20APIs.md)

[📋 Cheatsheet](React%20Native%20Interview%20Cheatsheet.md)

</div>

---
