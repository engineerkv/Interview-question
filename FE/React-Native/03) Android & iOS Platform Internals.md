# 3. Android & iOS Platform Internals (Q21–30)

---

## 📍 Navigation

<div align="center">

[Native Modules & Platform Integrations](02%29%20Native%20Modules%20%26%20Platform%20Integrations.md) • [Home: README](../README.md) • [Navigation & Lifecycle →](04%29%20Navigation%20%26%20Lifecycle.md)

[📋 Cheatsheet](React%20Native%20Interview%20Cheatsheet.md)

</div>

---

---

## Q21. 🔧 AndroidManifest.xml and how to configure it

AndroidManifest.xml defines app metadata, permissions, activities, and services for Android applications - handles deep links and app launching (intent filters). Defines app name, version, and package (app metadata).

- **Trade-offs**: The catch is defines app screens and entry points (activities) - declares background services (services). Handles deep links and app launching (intent filters), but watch out - declares required permissions (permissions).

Example:

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

## Q22. 🔧 Info.plist and how to configure it

Info.plist contains app configuration, permissions, and metadata for iOS applications - must be properly configured for App Store (required by Apple). Defines app settings and behavior (app configuration).

- **Trade-offs**: The catch is app name, version, and identifier (bundle information) - handles deep links and universal links (URL schemes). Must be properly configured for App Store (required by Apple), but watch out - explains why permissions are needed (permission descriptions).

Example:

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

## Q23. 🤔 Difference between MainActivity.java and MainApplication.java

MainActivity.java is the main entry point for the app, while MainApplication.java initializes the React Native host - both are required for React Native apps. MainActivity is entry point, handles app lifecycle; MainApplication initializes React Native, registers packages.

- **Trade-offs**: The catch is MainApplication manages native modules (package management) - different responsibilities for app lifecycle (lifecycle management). Both are required for React Native apps, but watch out - MainActivity registers the main component (component registration).

Example:

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

## Q24. 📱 How the Android lifecycle works in React Native

Android lifecycle manages app states (created, started, resumed, paused, stopped, destroyed), while React Native lifecycle manages component states - both lifecycles work together. Android lifecycle: onCreate, onStart, onResume, onPause, onStop, onDestroy; React Native lifecycle: componentDidMount, componentDidUpdate, componentWillUnmount.

- **Trade-offs**: The catch is Android manages app, React Native manages components (different purposes) - React Native integrates with Android lifecycle. Both lifecycles work together, but watch out - React Native provides AppState API for app-level lifecycle.

Example:

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

## Q25. 🔧 App Delegates in iOS and how they work

App Delegates handle app lifecycle events in iOS, with React Native using them to initialize the bridge and manage app states - manages React Native bridge lifecycle (bridge initialization). Handles app launch, background, foreground events (app lifecycle).

- **Trade-offs**: The catch is sets up the root view for React Native (root view) - iOS-specific app lifecycle management (iOS specific). Manages React Native bridge lifecycle (bridge initialization), but watch out - initializes React Native bridge (React Native integration).

Example:

```objc
#import "AppDelegate.h"
#import <React/RCTBundleURLProvider.h>

@implementation AppDelegate

- (BOOL)application:(UIApplication *)application didFinishLaunchingWithOptions:(NSDictionary *)launchOptions {
  RCTBridge *bridge = [RCTBridge alloc] initWithDelegate:self launchOptions:launchOptions];
  RCTRootView *rootView = [RCTRootView alloc] initWithBridge:bridge moduleName:@"MyApp" initialProperties:nil];
  return YES;
}

@end

```

---

## Q26. 📝 Configuring app permissions for both platforms

Configure permissions in platform-specific files and request them at runtime using appropriate libraries and APIs - follow platform-specific permission guidelines (app store guidelines). Different permission systems for iOS and Android (platform differences).

- **Trade-offs**: The catch is handle permission denials gracefully (user experience) - use libraries for consistent permission handling (permission libraries). Follow platform-specific permission guidelines (app store guidelines), but watch out - request permissions when needed (runtime requests).

Example:

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

## Q27. 💡 Setting up app icons and splash screens

Use platform-specific tools and configurations to set app icons and splash screens for both iOS and Android - smooth transition from splash to app (user experience). Different sizes for different devices and contexts (app icons).

- **Trade-offs**: The catch is use Xcode for iOS, Android Studio for Android (platform tools) - proper asset organization and optimization (asset management). Smooth transition from splash to app (user experience), but watch out - show while app is loading (splash screens).

Example:

```jsx
import SplashScreen from 'react-native-splash-screen';

function App() {
  useEffect(() => {
    SplashScreen.hide();
  }, []);
}

```

---

## Q28. 🏗️ Difference between Gradle and Xcode build systems

Gradle is Android's build system using Groovy/Kotlin, while Xcode is iOS's IDE and build system using Objective-C/Swift - both are required for React Native development. Gradle (Android build system, uses Groovy/Kotlin), Xcode (iOS IDE and build system, uses Objective-C/Swift).

- **Trade-offs**: The catch is different build configuration approaches (build configuration) - each platform has its own build system (platform specific). Both are required for React Native development, but watch out - different dependency management systems.

Example:

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

## Q29. 🐛 Creating debug vs release builds

Debug builds include debugging symbols and are unoptimized, while release builds are optimized and minified for production - always test release builds before distribution. Debug builds include debugging symbols, unoptimized; Release builds are optimized, minified, production-ready.

- **Trade-offs**: The catch is debug builds have better debugging capabilities (debugging) - release builds are used for app stores (distribution). Always test release builds before distribution, but watch out - release builds are faster and smaller (performance).

Example:

```jsx
import { __DEV__ } from 'react-native';

function MyComponent() {
  if (__DEV__) {
    console.log('Debug mode - extra logging enabled');
  }
}

```

---

## Q30. 💡 Handling app signing and provisioning

Use platform-specific tools to manage code signing, certificates, and provisioning profiles for app distribution - secure key storage is critical for production. Android keystore used for signing Android apps; iOS certificates used for signing iOS apps.

- **Trade-offs**: The catch is proper key management and security practices (security) - required for app store submission (distribution). Secure key storage is critical for production, but watch out - iOS-specific app distribution configuration (provisioning profiles).

Example:

```bash

# Android signing

keytool -genkey -v -keystore my-release-key.keystore -alias my-key-alias -keyalg RSA -keysize 2048 -validity 10000

# iOS provisioning - Use Xcode to manage certificates and provisioning profiles

```

---

---

## 📍 Navigation

<div align="center">

[Native Modules & Platform Integrations](02%29%20Native%20Modules%20%26%20Platform%20Integrations.md) • [Home: README](../README.md) • [Navigation & Lifecycle →](04%29%20Navigation%20%26%20Lifecycle.md)

[📋 Cheatsheet](React%20Native%20Interview%20Cheatsheet.md)

</div>

---
