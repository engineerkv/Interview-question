# 📱 3. Android & iOS Platform Internals (Q21–30)

---

## 21) What is the purpose of the `AndroidManifest.xml` file in Android projects?

AndroidManifest.xml defines app metadata, permissions, activities, and services for Android applications.

```xml
<manifest xmlns:android="http://schemas.android.com/apk/res/android">
    <uses-permission android:name="android.permission.INTERNET" />
    <uses-permission android:name="android.permission.CAMERA" />
    <application android:name=".MainApplication">
        <activity android:name=".MainActivity" />
    </application>
</manifest>
```

- **Core Purpose**: Defines app name, version, and package (app metadata)
- **Real-World Use**: Declares required permissions (permissions)
- **Common Configuration**: Defines app screens and entry points (activities)
- **Advanced Feature**: Declares background services (services)
- **Interview Tip**: Explain that handles deep links and app launching (intent filters)

---

## 22) What is the role of `Info.plist` in iOS projects?

Info.plist contains app configuration, permissions, and metadata for iOS applications.

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

- **Core Purpose**: Defines app settings and behavior (app configuration)
- **Real-World Requirement**: Explains why permissions are needed (permission descriptions)
- **Common Configuration**: App name, version, and identifier (bundle information)
- **Advanced Feature**: Handles deep links and universal links (URL schemes)
- **Interview Tip**: Explain that must be properly configured for App Store (required by Apple)

---

## 23) What's the difference between `MainActivity.java` and `MainApplication.java`?

MainActivity.java is the main entry point for the app, while MainApplication.java initializes the React Native host.

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

- **Core Difference**: MainActivity is entry point, handles app lifecycle; MainApplication initializes React Native, registers packages
- **Real-World Use**: MainActivity registers the main component (component registration)
- **Common Practice**: MainApplication manages native modules (package management)
- **Advanced Feature**: Different responsibilities for app lifecycle (lifecycle management)
- **Interview Tip**: Explain that both are required for React Native apps

---

## 24) How does the **Android lifecycle** differ from React Native's component lifecycle?

Android lifecycle manages app states (created, started, resumed, paused, stopped, destroyed), while React Native lifecycle manages component states.

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

- **Core Difference**: Android lifecycle: onCreate, onStart, onResume, onPause, onStop, onDestroy; React Native lifecycle: componentDidMount, componentDidUpdate, componentWillUnmount
- **Real-World Use**: React Native provides AppState API for app-level lifecycle
- **Common Purpose**: Android manages app, React Native manages components (different purposes)
- **Advanced Feature**: React Native integrates with Android lifecycle
- **Interview Tip**: Explain that both lifecycles work together

---

## 25) What are **App Delegates** in iOS, and how does React Native use them?

App Delegates handle app lifecycle events in iOS, with React Native using them to initialize the bridge and manage app states.

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

- **Core Purpose**: Handles app launch, background, foreground events (app lifecycle)
- **Real-World Use**: Initializes React Native bridge (React Native integration)
- **Common Setup**: Sets up the root view for React Native (root view)
- **Advanced Feature**: iOS-specific app lifecycle management (iOS specific)
- **Interview Tip**: Explain that manages React Native bridge lifecycle (bridge initialization)

---

## 26) How do you manage app permissions for iOS and Android (location, camera, etc.)?

Configure permissions in platform-specific files and request them at runtime using appropriate libraries and APIs.

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

- **Core Challenge**: Different permission systems for iOS and Android (platform differences)
- **Real-World Practice**: Request permissions when needed (runtime requests)
- **Common Approach**: Handle permission denials gracefully (user experience)
- **Advanced Feature**: Use libraries for consistent permission handling (permission libraries)
- **Interview Tip**: Explain that follow platform-specific permission guidelines (app store guidelines)

---

## 27) How do you configure app icons, splash screens, and launch screens?

Use platform-specific tools and configurations to set app icons and splash screens for both iOS and Android.

```jsx
import SplashScreen from 'react-native-splash-screen';

function App() {
  useEffect(() => {
    SplashScreen.hide();
  }, []);
}
```

- **Core Assets**: Different sizes for different devices and contexts (app icons)
- **Real-World Use**: Show while app is loading (splash screens)
- **Common Tools**: Use Xcode for iOS, Android Studio for Android (platform tools)
- **Advanced Practice**: Proper asset organization and optimization (asset management)
- **Interview Tip**: Explain that smooth transition from splash to app (user experience)

---

## 28) What is the difference between **Gradle** and **Xcode** build systems?

Gradle is Android's build system using Groovy/Kotlin, while Xcode is iOS's IDE and build system using Objective-C/Swift.

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

- **Core Systems**: Gradle (Android build system, uses Groovy/Kotlin), Xcode (iOS IDE and build system, uses Objective-C/Swift)
- **Real-World Impact**: Different dependency management systems
- **Common Difference**: Different build configuration approaches (build configuration)
- **Advanced Feature**: Each platform has its own build system (platform specific)
- **Interview Tip**: Explain that both are required for React Native development

---

## 29) What are the differences between **debug** and **release** builds?

Debug builds include debugging symbols and are unoptimized, while release builds are optimized and minified for production.

```jsx
import { __DEV__ } from 'react-native';

function MyComponent() {
  if (__DEV__) {
    console.log('Debug mode - extra logging enabled');
  }
}
```

- **Core Difference**: Debug builds include debugging symbols, unoptimized; Release builds are optimized, minified, production-ready
- **Real-World Impact**: Release builds are faster and smaller (performance)
- **Common Use**: Debug builds have better debugging capabilities (debugging)
- **Advanced Feature**: Release builds are used for app stores (distribution)
- **Interview Tip**: Explain that always test release builds before distribution

---

## 30) How do you manage signing and provisioning (keystore, certificates, profiles)?

Use platform-specific tools to manage code signing, certificates, and provisioning profiles for app distribution.

```bash
# Android signing
keytool -genkey -v -keystore my-release-key.keystore -alias my-key-alias -keyalg RSA -keysize 2048 -validity 10000

# iOS provisioning - Use Xcode to manage certificates and provisioning profiles
```

- **Core Tools**: Android keystore used for signing Android apps; iOS certificates used for signing iOS apps
- **Real-World Requirement**: iOS-specific app distribution configuration (provisioning profiles)
- **Common Practice**: Proper key management and security practices (security)
- **Advanced Feature**: Required for app store submission (distribution)
- **Interview Tip**: Explain that secure key storage is critical for production

---
