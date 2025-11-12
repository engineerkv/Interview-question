# 📱 3. Android & iOS Platform Internals (Q21–30)

---

## 🧩 Q21. What is AndroidManifest.xml and how do you configure it?

### 🧠 Concept

AndroidManifest.xml defines app metadata, permissions, activities, and services for Android applications. Handles deep links and app launching (intent filters).

---

### 💡 Example

```xml
<manifest xmlns:android="http://schemas.android.com/apk/res/android">
    <uses-permission android:name="android.permission.INTERNET" />
    <uses-permission android:name="android.permission.CAMERA" />
    <application android:name=".MainApplication">
        <activity android:name=".MainActivity" />
    </application>
</manifest>
```

---

### 🔍 Deep Insights

* **Rule:** Defines app name, version, and package (app metadata).
* **Use Case:** Declares required permissions (permissions).
* **Common Mistake:** Defines app screens and entry points (activities).
* **Pro Tip:** Declares background services (services).

---

### ⭐ Senior Takeaway

Handles deep links and app launching (intent filters).

---

## 🧩 Q22. What is Info.plist and how do you configure it?

### 🧠 Concept

Info.plist contains app configuration, permissions, and metadata for iOS applications. Must be properly configured for App Store (required by Apple).

---

### 💡 Example

```xml
<dict>
    <key>CFBundleDisplayName</key>
    <string>My App</string>
    <key>CFBundleIdentifier</key>
    <string>com.myapp</string>
    <key>NSCameraUsageDescription</key>
    <string>We need camera access to take photos</string>
</dict>
```

---

### 🔍 Deep Insights

* **Rule:** Defines app settings and behavior (app configuration).
* **Use Case:** Explains why permissions are needed (permission descriptions).
* **Common Mistake:** App name, version, and identifier (bundle information).
* **Pro Tip:** Handles deep links and universal links (URL schemes).

---

### ⭐ Senior Takeaway

Must be properly configured for App Store (required by Apple).

---

## 🧩 Q23. What is the difference between MainActivity.java and MainApplication.java?

### 🧠 Concept

MainActivity.java is the main entry point for the app, while MainApplication.java initializes the React Native host. Both are required for React Native apps.

---

### 💡 Example

```java
public class MainActivity extends ReactActivity {
    @Override
    protected String getMainComponentName() {
        return "MyApp";
    }
}

public class MainApplication extends Application implements ReactApplication {
    @Override
    public ReactNativeHost getReactNativeHost() {
        return mReactNativeHost;
    }
}
```

---

### 🔍 Deep Insights

* **Rule:** MainActivity is entry point, handles app lifecycle; MainApplication initializes React Native, registers packages.
* **Use Case:** MainActivity registers the main component (component registration).
* **Common Mistake:** MainApplication manages native modules (package management).
* **Pro Tip:** Different responsibilities for app lifecycle (lifecycle management).

---

### ⭐ Senior Takeaway

Both are required for React Native apps.

---

## 🧩 Q24. How does the Android lifecycle work in React Native?

### 🧠 Concept

Android lifecycle manages app states (created, started, resumed, paused, stopped, destroyed), while React Native lifecycle manages component states. Both lifecycles work together.

---

### 💡 Example

```jsx
import { useEffect } from 'react';
import { AppState } from 'react-native';

function MyComponent() {
  useEffect(() => {
    const subscription = AppState.addEventListener('change', nextAppState => {
      console.log('App state:', nextAppState);
    });
    return () => subscription.remove();
  }, []);
}
```

---

### 🔍 Deep Insights

* **Rule:** Android lifecycle: onCreate, onStart, onResume, onPause, onStop, onDestroy; React Native lifecycle: componentDidMount, componentDidUpdate, componentWillUnmount.
* **Use Case:** React Native provides AppState API for app-level lifecycle.
* **Common Mistake:** Android manages app, React Native manages components (different purposes).
* **Pro Tip:** React Native integrates with Android lifecycle.

---

### ⭐ Senior Takeaway

Both lifecycles work together.

---

## 🧩 Q25. What are App Delegates in iOS and how do they work?

### 🧠 Concept

App Delegates handle app lifecycle events in iOS, with React Native using them to initialize the bridge and manage app states. Manages React Native bridge lifecycle (bridge initialization).

---

### 💡 Example

```objc
#import "AppDelegate.h"
#import <React/RCTBundleURLProvider.h>

@implementation AppDelegate

- (BOOL)application:(UIApplication *)application didFinishLaunchingWithOptions:(NSDictionary *)launchOptions {
  RCTBridge *bridge = [[RCTBridge alloc] initWithDelegate:self launchOptions:launchOptions];
  RCTRootView *rootView = [[RCTRootView alloc] initWithBridge:bridge moduleName:@"MyApp" initialProperties:nil];
  return YES;
}

@end
```

---

### 🔍 Deep Insights

* **Rule:** Handles app launch, background, foreground events (app lifecycle).
* **Use Case:** Initializes React Native bridge (React Native integration).
* **Common Mistake:** Sets up the root view for React Native (root view).
* **Pro Tip:** iOS-specific app lifecycle management (iOS specific).

---

### ⭐ Senior Takeaway

Manages React Native bridge lifecycle (bridge initialization).

---

## 🧩 Q26. How do you configure app permissions for both platforms?

### 🧠 Concept

Configure permissions in platform-specific files and request them at runtime using appropriate libraries and APIs. Follow platform-specific permission guidelines (app store guidelines).

---

### 💡 Example

```jsx
import { Platform } from 'react-native';
import { request, PERMISSIONS, RESULTS } from 'react-native-permissions';

const requestLocationPermission = async () => {
  const permission = Platform.OS === 'ios' 
    ? PERMISSIONS.IOS.LOCATION_WHEN_IN_USE
    : PERMISSIONS.ANDROID.ACCESS_FINE_LOCATION;
  const result = await request(permission);
  return result === RESULTS.GRANTED;
};
```

---

### 🔍 Deep Insights

* **Rule:** Different permission systems for iOS and Android (platform differences).
* **Use Case:** Request permissions when needed (runtime requests).
* **Common Mistake:** Handle permission denials gracefully (user experience).
* **Pro Tip:** Use libraries for consistent permission handling (permission libraries).

---

### ⭐ Senior Takeaway

Follow platform-specific permission guidelines (app store guidelines).

---

## 🧩 Q27. How do you set up app icons and splash screens?

### 🧠 Concept

Use platform-specific tools and configurations to set app icons and splash screens for both iOS and Android. Smooth transition from splash to app (user experience).

---

### 💡 Example

```jsx
import SplashScreen from 'react-native-splash-screen';

function App() {
  useEffect(() => {
    SplashScreen.hide();
  }, []);
}
```

---

### 🔍 Deep Insights

* **Rule:** Different sizes for different devices and contexts (app icons).
* **Use Case:** Show while app is loading (splash screens).
* **Common Mistake:** Use Xcode for iOS, Android Studio for Android (platform tools).
* **Pro Tip:** Proper asset organization and optimization (asset management).

---

### ⭐ Senior Takeaway

Smooth transition from splash to app (user experience).

---

## 🧩 Q28. What is the difference between Gradle and Xcode build systems?

### 🧠 Concept

Gradle is Android's build system using Groovy/Kotlin, while Xcode is iOS's IDE and build system using Objective-C/Swift. Both are required for React Native development.

---

### 💡 Example

```gradle
// android/app/build.gradle
android {
    compileSdkVersion 30
    defaultConfig {
        applicationId "com.myapp"
        minSdkVersion 21
    }
}
```

---

### 🔍 Deep Insights

* **Rule:** Gradle (Android build system, uses Groovy/Kotlin), Xcode (iOS IDE and build system, uses Objective-C/Swift).
* **Use Case:** Different dependency management systems.
* **Common Mistake:** Different build configuration approaches (build configuration).
* **Pro Tip:** Each platform has its own build system (platform specific).

---

### ⭐ Senior Takeaway

Both are required for React Native development.

---

## 🧩 Q29. How do you create debug vs release builds?

### 🧠 Concept

Debug builds include debugging symbols and are unoptimized, while release builds are optimized and minified for production. Always test release builds before distribution.

---

### 💡 Example

```jsx
import { __DEV__ } from 'react-native';

function MyComponent() {
  if (__DEV__) {
    console.log('Debug mode - extra logging enabled');
  }
}
```

---

### 🔍 Deep Insights

* **Rule:** Debug builds include debugging symbols, unoptimized; Release builds are optimized, minified, production-ready.
* **Use Case:** Release builds are faster and smaller (performance).
* **Common Mistake:** Debug builds have better debugging capabilities (debugging).
* **Pro Tip:** Release builds are used for app stores (distribution).

---

### ⭐ Senior Takeaway

Always test release builds before distribution.

---

## 🧩 Q30. How do you handle app signing and provisioning?

### 🧠 Concept

Use platform-specific tools to manage code signing, certificates, and provisioning profiles for app distribution. Secure key storage is critical for production.

---

### 💡 Example

```bash
# Android signing
keytool -genkey -v -keystore my-release-key.keystore -alias my-key-alias -keyalg RSA -keysize 2048 -validity 10000

# iOS provisioning - Use Xcode to manage certificates and provisioning profiles
```

---

### 🔍 Deep Insights

* **Rule:** Android keystore used for signing Android apps; iOS certificates used for signing iOS apps.
* **Use Case:** iOS-specific app distribution configuration (provisioning profiles).
* **Common Mistake:** Proper key management and security practices (security).
* **Pro Tip:** Required for app store submission (distribution).

---

### ⭐ Senior Takeaway

Secure key storage is critical for production.

---
