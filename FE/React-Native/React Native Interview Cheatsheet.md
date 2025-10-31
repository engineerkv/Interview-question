# ⚛️ **React Native Interview Cheatsheet**

*Quick reference guide for React Native interview preparation*

---

## 📋 **React Native Basics**

| Concept | Description | Example |
|---------|-------------|---------|
| **Component** | Reusable UI piece | `function Button() { return <TouchableOpacity><Text>Click</Text></TouchableOpacity>; }` |
| **JSX** | Mobile UI syntax | `<View><Text>Hello</Text></View>` |
| **Props** | Data passed to components | `<Button title="Click me" onPress={handlePress} />` |
| **State** | Component's internal data | `const [count, setCount] = useState(0)` |
| **Bridge** | JS ↔ Native communication | `NativeModules.MyModule.doSomething()` |

---

## 🔌 **Native Modules**

### **Creating Native Modules**
```jsx
// JavaScript side
import { NativeModules } from 'react-native';
const { MyNativeModule } = NativeModules;

MyNativeModule.doSomething('Hello')
  .then(result => console.log(result))
  .catch(error => console.error(error));
```

### **Android Native Module**
```java
// MyNativeModule.java
public class MyNativeModule extends ReactContextBaseJavaModule {
    @ReactMethod
    public void doSomething(String message, Promise promise) {
        try {
            String result = "Android: " + message;
            promise.resolve(result);
        } catch (Exception e) {
            promise.reject("ERROR", e.getMessage());
        }
    }
}
```

### **iOS Native Module**
```objc
// MyNativeModule.m
RCT_EXPORT_METHOD(doSomething:(NSString *)message
                  resolver:(RCTPromiseResolveBlock)resolve
                  rejecter:(RCTPromiseRejectBlock)reject)
{
    NSString *result = [NSString stringWithFormat:@"iOS: %@", message];
    resolve(result);
}
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

### **React Navigation**
```jsx
import { NavigationContainer } from '@react-navigation/native';
import { createStackNavigator } from '@react-navigation/stack';

const Stack = createStackNavigator();

function App() {
  return (
    <NavigationContainer>
      <Stack.Navigator>
        <Stack.Screen name="Home" component={HomeScreen} />
        <Stack.Screen name="Details" component={DetailsScreen} />
      </Stack.Navigator>
    </NavigationContainer>
  );
}
```

### **Deep Linking**
```jsx
import { Linking } from 'react-native';

useEffect(() => {
  const handleDeepLink = (url) => {
    if (url.includes('product/')) {
      const productId = url.split('product/')[1];
      navigation.navigate('Product', { productId });
    }
  };
  
  Linking.addEventListener('url', handleDeepLink);
  return () => Linking.removeEventListener('url', handleDeepLink);
}, []);
```

---

## 🚀 **Performance Optimization**

### **FlatList Optimization**
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
5. **Navigation** - How to handle navigation in mobile apps

### **Key Concepts**
- **Bridge Communication**: How JS communicates with native code
- **Platform APIs**: Accessing device features through native modules
- **Performance**: Optimization techniques for mobile apps
- **State Management**: Managing state in mobile applications
- **Testing**: Testing strategies for mobile apps

### **Best Practices**
- Use FlatList for large lists
- Optimize images and assets
- Handle platform differences
- Test on real devices
- Monitor app performance

---

*Remember: Practice with real devices, understand platform differences, and focus on performance optimization!*
