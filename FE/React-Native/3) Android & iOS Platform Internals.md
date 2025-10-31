# 📱 3. Android & iOS Platform Internals (Q21–30)

---

## 21) What is the purpose of the `AndroidManifest.xml` file in Android projects?

Concept:
AndroidManifest.xml defines app metadata, permissions, activities, and services for Android applications.

Example:
```xml
<!-- android/app/src/main/AndroidManifest.xml -->
<manifest xmlns:android="http://schemas.android.com/apk/res/android">
    <uses-permission android:name="android.permission.INTERNET" />
    <uses-permission android:name="android.permission.CAMERA" />
    
    <application
```

Deep Insight:
- **App Metadata**: Defines app name, version, and package
- **Permissions**: Declares required permissions
- **Activities**: Defines app screens and entry points
- **Services**: Declares background services
- **Intent Filters**: Handles deep links and app launching

---

## 22) What is the role of `Info.plist` in iOS projects?

Concept:
Info.plist contains app configuration, permissions, and metadata for iOS applications.

Example:
```xml
<!-- ios/MyApp/Info.plist -->
<dict>
    <key>CFBundleDisplayName</key>
    <string>My App</string>
    <key>CFBundleIdentifier</key>
    <string>com.myapp</string>
```

Deep Insight:
- **App Configuration**: Defines app settings and behavior
- **Permission Descriptions**: Explains why permissions are needed
- **Bundle Information**: App name, version, and identifier
- **URL Schemes**: Handles deep links and universal links
- **Required by Apple**: Must be properly configured for App Store

---

## 23) What's the difference between `MainActivity.java` and `MainApplication.java`?

Concept:
MainActivity.java is the main entry point for the app, while MainApplication.java initializes the React Native host.

Example:
```java
// MainActivity.java
public class MainActivity extends ReactActivity {
    @Override
    protected String getMainComponentName() {
        return "MyApp";
    }
```

Deep Insight:
- **MainActivity**: Entry point, handles app lifecycle
- **MainApplication**: Initializes React Native, registers packages
- **Component Registration**: MainActivity registers the main component
- **Package Management**: MainApplication manages native modules
- **Lifecycle Management**: Different responsibilities for app lifecycle

---

## 24) How does the **Android lifecycle** differ from React Native's component lifecycle?

Concept:
Android lifecycle manages app states (created, started, resumed, paused, stopped, destroyed), while React Native lifecycle manages component states.

Example:
```jsx
// React Native component lifecycle
import { useEffect } from 'react';
import { AppState } from 'react-native';

function MyComponent() {
  useEffect(() => {
```

Deep Insight:
- **Android Lifecycle**: onCreate, onStart, onResume, onPause, onStop, onDestroy
- **React Native Lifecycle**: componentDidMount, componentDidUpdate, componentWillUnmount
- **App State**: React Native provides AppState API for app-level lifecycle
- **Different Purposes**: Android manages app, React Native manages components
- **Integration**: React Native integrates with Android lifecycle

---

## 25) What are **App Delegates** in iOS, and how does React Native use them?

Concept:
App Delegates handle app lifecycle events in iOS, with React Native using them to initialize the bridge and manage app states.

Example:
```objc
// AppDelegate.m
#import "AppDelegate.h"
#import <React/RCTBundleURLProvider.h>

@implementation AppDelegate

```

Deep Insight:
- **App Lifecycle**: Handles app launch, background, foreground events
- **React Native Integration**: Initializes React Native bridge
- **Root View**: Sets up the root view for React Native
- **iOS Specific**: iOS-specific app lifecycle management
- **Bridge Initialization**: Manages React Native bridge lifecycle

---

## 26) How do you manage app permissions for iOS and Android (location, camera, etc.)?

Concept:
Configure permissions in platform-specific files and request them at runtime using appropriate libraries and APIs.

Example:
```jsx
// Permission management
import { Platform, Alert } from 'react-native';
import { request, PERMISSIONS, RESULTS } from 'react-native-permissions';

const requestLocationPermission = async () => {
  const permission = Platform.OS === 'ios' 
```

Deep Insight:
- **Platform Differences**: Different permission systems for iOS and Android
- **Runtime Requests**: Request permissions when needed
- **User Experience**: Handle permission denials gracefully
- **Permission Libraries**: Use libraries for consistent permission handling
- **App Store Guidelines**: Follow platform-specific permission guidelines

---

## 27) How do you configure app icons, splash screens, and launch screens?

Concept:
Use platform-specific tools and configurations to set app icons and splash screens for both iOS and Android.

Example:
```jsx
// react-native-splash-screen
import SplashScreen from 'react-native-splash-screen';

function App() {
  useEffect(() => {
    // Hide splash screen when app is ready
```

Deep Insight:
- **App Icons**: Different sizes for different devices and contexts
- **Splash Screens**: Show while app is loading
- **Platform Tools**: Use Xcode for iOS, Android Studio for Android
- **Asset Management**: Proper asset organization and optimization
- **User Experience**: Smooth transition from splash to app

---

## 28) What is the difference between **Gradle** and **Xcode** build systems?

Concept:
Gradle is Android's build system using Groovy/Kotlin, while Xcode is iOS's IDE and build system using Objective-C/Swift.

Example:
```gradle
// android/app/build.gradle
android {
    compileSdkVersion 30
    defaultConfig {
        applicationId "com.myapp"
        minSdkVersion 21
```

Deep Insight:
- **Gradle**: Android build system, uses Groovy/Kotlin
- **Xcode**: iOS IDE and build system, uses Objective-C/Swift
- **Dependency Management**: Different dependency management systems
- **Build Configuration**: Different build configuration approaches
- **Platform Specific**: Each platform has its own build system

---

## 29) What are the differences between **debug** and **release** builds?

Concept:
Debug builds include debugging symbols and are unoptimized, while release builds are optimized and minified for production.

Example:
```jsx
// Debug vs Release behavior
import { __DEV__ } from 'react-native';

function MyComponent() {
  if (__DEV__) {
    console.log('Debug mode - extra logging enabled');
```

Deep Insight:
- **Debug Builds**: Include debugging symbols, unoptimized
- **Release Builds**: Optimized, minified, production-ready
- **Performance**: Release builds are faster and smaller
- **Debugging**: Debug builds have better debugging capabilities
- **Distribution**: Release builds are used for app stores

---

## 30) How do you manage signing and provisioning (keystore, certificates, profiles)?

Concept:
Use platform-specific tools to manage code signing, certificates, and provisioning profiles for app distribution.

Example:
```bash
# Android signing
keytool -genkey -v -keystore my-release-key.keystore -alias my-key-alias -keyalg RSA -keysize 2048 -validity 10000

# iOS provisioning
# Use Xcode to manage certificates and provisioning profiles
```

Deep Insight:
- **Android Keystore**: Used for signing Android apps
- **iOS Certificates**: Used for signing iOS apps
- **Provisioning Profiles**: iOS-specific app distribution configuration
- **Security**: Proper key management and security practices
- **Distribution**: Required for app store submission

---
