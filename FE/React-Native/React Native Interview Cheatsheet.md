# ⚛️ React Native Interview Cheatsheet

> **⏱️ Review Time: 15-20 minutes** | **Priority: ⭐⭐ Medium** | Quick reference for React Native interviews
>
> **Coverage: Q1-Q95** (95 questions across 10 topics)

**Quick Review Checklist:**

- [ ] React Native Basics (Components, JSX, New Architecture)

- [ ] Native Modules (TurboModules, JSI)

- [ ] Platform Configuration (AndroidManifest, Info.plist)

- [ ] Navigation (React Native Navigation, Deep Linking)

- [ ] Performance (FlatList Optimization, Memoization, Fabric)

- [ ] State Management (Redux, AsyncStorage)

- [ ] Testing (Jest, Detox E2E)

- [ ] Build & Deployment (Release Builds, CodePush)

---

## 📋 **Question Coverage**

- **Q1-Q10**: React Native Fundamentals

- **Q11-Q20**: Native Modules & Platform Integrations

- **Q22-Q31**: Navigation & App Lifecycle

- **Q41-Q50**: Performance Optimization & Measurement

- **Q51-Q60**: State Management & Data Handling

- **Q61-Q68**: CodePush & OTA Updates

- **Q69-Q78**: Debugging & Testing

- **Q79-Q90**: Build, Deployment & Stores

- **Q91-Q95**: Push Notifications & Messaging

---

## 📋 **React Native Basics**

| Concept | Description | Example |
|---------|-------------|---------|
| **Component** | Reusable UI piece | `function Button() { return <TouchableOpacity><Text>Click</Text></TouchableOpacity>; }` |
| **JSX** | Mobile UI syntax | `<View><Text>Hello</Text></View>` |
| **Props** | Data passed to components | `<Button title="Click me" onPress={handlePress} />` |
| **State** | Component's internal data | `const [count, setCount] = useState(0)` |
| **Bridge (Legacy)** | JS ↔ Native communication (old) | `NativeModules.MyModule.doSomething()` |
| **JSI/TurboModules** | Direct JS ↔ Native calls (New Architecture) | `TurboModuleRegistry.get('MyModule').doSomething()` |

---

## 🔌 **Native Modules**

### **TurboModules (New Architecture - Recommended)**

**Definition:** TurboModules use JSI for direct communication between JavaScript and native code, providing better performance (20-500x faster), lazy loading, and type safety through codegen.

```jsx
// TurboModule with TypeScript spec (codegen)
// NativeMyModule.ts
import { TurboModule, TurboModuleRegistry } from 'react-native';

export interface Spec extends TurboModule {
  readonly doSomething: (input: string) => Promise<string>;
  readonly getConstants: () => { readonly apiKey: string };
}

export default TurboModuleRegistry.get<Spec>('MyModule');

// Usage - lazy loaded on first use
import MyModule from './NativeMyModule';
const result = await MyModule.doSomething('Hello');
```

### **Android Native Module (TurboModule)**

```java
// TurboModule approach (New Architecture)
@ReactModule(name = MyModuleSpec.NAME)
public class MyModule extends MyModuleSpec {
  public MyModule(ReactApplicationContext reactContext) {
    super(reactContext);
  }

  @Override
  public String doSomething(String input) {
    return "Android: " + input;
  }
}
```

### **iOS Native Module (TurboModule)**

```objc
// TurboModule approach (New Architecture)
// MyModule.mm
@interface RCT_EXTERN_MODULE(MyModule, NSObject)
RCT_EXTERN_METHOD(doSomething:(NSString *)input
                  resolver:(RCTPromiseResolveBlock)resolve
                  rejecter:(RCTPromiseRejectBlock)reject)
@end
```

---

## 📱 **Platform Configuration**

### **Android Manifest**

```xml
<!-- android/app/src/main/AndroidManifest.xml -->
<manifest xmlns:android="http://schemas.android.com/apk/res/android">
    <uses-permission android:name="android.permission.INTERNET" />
    <uses-permission android:name="android.permission.CAMERA" />

    <application
        android:name=".MainApplication"
        android:label="@string/app_name">

        <activity
            android:name=".MainActivity"
            android:exported="true"
            android:launchMode="singleTop">
            <intent-filter>
                <action android:name="android.intent.action.MAIN" />
                <category android:name="android.intent.category.LAUNCHER" />
            </intent-filter>
        </activity>
    </application>
</manifest>

```

### **iOS Info.plist**

```xml
<!-- ios/MyApp/Info.plist -->
<dict>
    <key>CFBundleDisplayName</key>
    <string>My App</string>
    <key>CFBundleIdentifier</key>
    <string>com.myapp</string>
    <key>NSCameraUsageDescription</key>
    <string>This app needs camera access</string>
</dict>

```

---

## ⚙️ **Navigation**

### **React Native Navigation**

**Definition:** React Native Navigation provides native navigation for React Native apps, handling navigation state, deep linking, and screen transitions with native performance.

```jsx
import { Navigation } from 'react-native-navigation';

// Set root navigation
Navigation.setRoot({
  root: {
    stack: {
      children: [{
        component: {
          name: 'HomeScreen'
        }
      }]
    }
  }
});

// Push to new screen
Navigation.push(componentId, {
  component: {
    name: 'DetailsScreen',
    passProps: { itemId: 123 }
  }
});

// Pop current screen
Navigation.pop(componentId);
```

### **Deep Linking**

```jsx
import { Linking } from 'react-native';

useEffect(() => {
  const handleDeepLink = (url) => {
    if (url.includes('product/')) {
      const productId = url.split('product/')[1];
      // Handle navigation based on deep link
      console.log('Navigate to product:', productId);
    }
  };

  Linking.addEventListener('url', handleDeepLink);
  return () => Linking.removeEventListener('url', handleDeepLink);
}, []);

```

---

## 🚀 **Performance Optimization**

### **FlatList Optimization**

**Definition:** Optimize FlatList performance with getItemLayout, keyExtractor, removeClippedSubviews, maxToRenderPerBatch, and windowSize props to handle large lists efficiently.

```jsx
function OptimizedList({ data }) {
  const renderItem = useCallback(({ item }) => (
    <ListItem item={item} />
  ), []);

  return (
    <FlatList
      data={data}
      renderItem={renderItem}
      keyExtractor={item => item.id}
      getItemLayout={(data, index) => ({
        length: ITEM_HEIGHT,
        offset: ITEM_HEIGHT * index,
        index,
      })}
      initialNumToRender={10}
      maxToRenderPerBatch={5}
      windowSize={10}
      removeClippedSubviews={true}
    />
  );
}

```

### **Memoization**

```jsx
// React.memo for components
const ExpensiveComponent = React.memo(({ data }) => {
  return <View>{data.map(item => <Text key={item.id}>{item.name}</Text>)}</View>;
});

// useMemo for calculations
const expensiveValue = useMemo(() => {
  return heavyCalculation(data);
}, [data]);

// useCallback for functions
const handlePress = useCallback(() => {
  doSomething();
}, [dependency]);

```

---

## 🧩 **State Management**

### **Redux Toolkit**

```jsx
import { createSlice, configureStore } from '@reduxjs/toolkit';

const counterSlice = createSlice({
  name: 'counter',
  initialState: { count: 0 },
  reducers: {
    increment: (state) => { state.count += 1; },
    decrement: (state) => { state.count -= 1; }
  }
});

const store = configureStore({
  reducer: { counter: counterSlice.reducer }
});

function Counter() {
  const count = useSelector(state => state.counter.count);
  const dispatch = useDispatch();
  return <Button title={count} onPress={() => dispatch(increment())} />;
}

```

### **AsyncStorage**

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
    return value ? JSON.parse(value) : null;
  } catch (error) {
    console.error('Error retrieving data:', error);
  }
};

```

---

## ⚡ **CodePush & OTA Updates**

### **CodePush Setup**

```jsx
import codePush from 'react-native-code-push';

function App() {
  useEffect(() => {
    codePush.sync({
      updateDialog: true,
      installMode: codePush.InstallMode.IMMEDIATE
    });
  }, []);

  return <MainApp />;
}

export default codePush(App);

```

### **OTA Update Handling**

```jsx
const codePushOptions = {
  checkFrequency: codePush.CheckFrequency.ON_APP_START,
  installMode: codePush.InstallMode.ON_NEXT_RESTART,
  rollbackRetryOptions: {
    delayInHours: 1,
    maxRetryAttempts: 3
  }
};

```

---

## 🧪 **Testing**

### **Jest Testing**

```jsx
import { render, fireEvent, waitFor } from '@testing-library/react-native';

test('renders correctly', () => {
  const { getByText } = render(<MyComponent />);
  expect(getByText('Hello World')).toBeTruthy();
});

test('handles button press', async () => {
  const { getByText } = render(<MyComponent />);
  fireEvent.press(getByText('Press Me'));

  await waitFor(() => {
    expect(getByText('Button Pressed')).toBeTruthy();
  });
});

```

### **Detox E2E Testing**

```jsx
describe('Login Flow', () => {
  it('should login successfully', async () => {
    await element(by.id('email-input')).typeText('user@example.com');
    await element(by.id('password-input')).typeText('password123');
    await element(by.id('login-button')).tap();

    await expect(element(by.id('welcome-message'))).toBeVisible();
  });
});

```

---

## 🏗 **Build & Deployment**

### **Android Release Build**

```gradle
// android/app/build.gradle
android {
    signingConfigs {
        release {
            storeFile file(MYAPP_RELEASE_STORE_FILE)
            storePassword MYAPP_RELEASE_STORE_PASSWORD
            keyAlias MYAPP_RELEASE_KEY_ALIAS
            keyPassword MYAPP_RELEASE_KEY_PASSWORD
        }
    }
    buildTypes {
        release {
            signingConfig signingConfigs.release
            minifyEnabled true
            proguardFiles getDefaultProguardFile("proguard-android.txt")
        }
    }
}

```

### **iOS Release Build**

```bash

# Archive iOS app

xcodebuild -workspace MyApp.xcworkspace \
           -scheme MyApp \
           -configuration Release \
           -archivePath MyApp.xcarchive \
           archive

```

---

## 📳 **Push Notifications**

### **FCM Setup**

```jsx
import messaging from '@react-native-firebase/messaging';

// Request permission
const requestPermission = async () => {
  const authStatus = await messaging().requestPermission();
  return authStatus === messaging.AuthorizationStatus.AUTHORIZED;
};

// Get FCM token
const getFCMToken = async () => {
  const token = await messaging().getToken();
  console.log('FCM Token:', token);
  return token;
};

// Handle notifications
messaging().onMessage(async remoteMessage => {
  console.log('Foreground notification:', remoteMessage);
});

```

---

## 🔧 **Common Patterns**

### **Permission Handling**

```jsx
import { PermissionsAndroid, Platform } from 'react-native';

const requestCameraPermission = async () => {
  if (Platform.OS === 'android') {
    const granted = await PermissionsAndroid.request(
      PermissionsAndroid.PERMISSIONS.CAMERA
    );
    return granted === PermissionsAndroid.RESULTS.GRANTED;
  }
  return true; // iOS handled by Info.plist
};

```

### **App State Handling**

```jsx
import { AppState } from 'react-native';

function App() {
  const [appState, setAppState] = useState(AppState.currentState);

  useEffect(() => {
    const handleAppStateChange = (nextAppState) => {
      if (appState.match(/inactive|background/) && nextAppState === 'active') {
        console.log('App has come to the foreground!');
      }
      setAppState(nextAppState);
    };

    AppState.addEventListener('change', handleAppStateChange);
    return () => AppState.removeEventListener('change', handleAppStateChange);
  }, [appState]);
}

```

---

## 🎯 **Interview Tips**

### **Common Questions**

1. **React Native vs React** - Mobile vs web differences

2. **Native Modules** - How to create and use native modules

3. **Performance** - How to optimize React Native apps

4. **Platform Differences** - iOS vs Android specific implementations

5. **Navigation** - How to handle navigation in mobile apps with React Native Navigation

### **Key Concepts**

- **New Architecture**: JSI, Fabric, and TurboModules (stable in 0.73+)

- **JSI/TurboModules**: Direct JSI calls (20-500x faster than legacy bridge)

- **Platform APIs**: Accessing device features through TurboModules

- **Performance**: Optimization techniques including Fabric rendering

- **State Management**: Managing state in mobile applications

- **Testing**: Testing strategies for mobile apps

### **Best Practices**

- Use FlatList for large lists

- Optimize images and assets

- Handle platform differences

- Test on real devices

- Monitor app performance

---

## ⚡ **Last-Minute Review (5 minutes)**

### **Must-Know Concepts**

- **New Architecture**: JSI, Fabric, TurboModules (stable in 0.73+)

- **TurboModules**: Direct JS ↔ Native calls (20-500x faster than bridge)

- **Native Modules**: Access platform APIs (camera, GPS, etc.) via TurboModules

- **Platform Differences**: Use `Platform.OS` for iOS/Android specific code

- **FlatList**: Use for large lists (not ScrollView)

- **Navigation**: React Native Navigation for native navigation

### **Quick Code Snippets**

```jsx
// Platform Check
if (Platform.OS === 'ios') { /* iOS code */ }

// FlatList
<FlatList
  data={items}
  renderItem={({ item }) => <Item data={item} />}
  keyExtractor={item => item.id}
/>

// TurboModule (New Architecture)
import { TurboModuleRegistry } from 'react-native';
const MyModule = TurboModuleRegistry.get('MyModule');
MyModule.doSomething();

```

### **Common Gotchas**

- Use `View` instead of `div`, `Text` instead of `span`

- FlatList for performance, ScrollView for small lists

- Handle platform differences (iOS vs Android)

- Test on real devices, not just simulators

*Remember: Practice with real devices, understand platform differences, and focus on performance optimization!*
