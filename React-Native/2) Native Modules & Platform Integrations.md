# 🔌 2. Native Modules & Platform Integrations (Q11–20)

---

## 11) What are **Native Modules**, and why do we need them in React Native?

Concept:
Native Modules are JavaScript interfaces to native platform APIs, needed to access device features not available through React Native's built-in components.

Example:
```jsx
// Using a native module
import { NativeModules } from 'react-native';

const { MyNativeModule } = NativeModules;

// Call native function
MyNativeModule.doSomething().then(result => console.log(result));
```

Deep Insight:
- **Platform APIs**: Access to device-specific functionality
- **Performance**: Native code runs faster than JavaScript
- **Device Features**: Camera, sensors, file system, etc.
- **Bridge Communication**: Uses bridge to communicate with native code
- **Platform Specific**: Different implementations for iOS and Android

---

## 12) How do you create a custom native module for **Android** using Java/Kotlin?

Concept:
Create a native module by extending ReactContextBaseJavaModule and registering it in the ReactPackage.

Example:
```java
// MyNativeModule.java
package com.myapp;

import com.facebook.react.bridge.ReactApplicationContext;
import com.facebook.react.bridge.ReactContextBaseJavaModule;
import com.facebook.react.bridge.ReactMethod;

public class MyNativeModule extends ReactContextBaseJavaModule {
  @ReactMethod
  public void doSomething(Promise promise) {
    promise.resolve("Result from native");
  }
}
```

Deep Insight:
- **ReactContextBaseJavaModule**: Base class for native modules
- **getName()**: Returns module name used in JavaScript
- **@ReactMethod**: Exposes methods to JavaScript
- **Promise**: Handles asynchronous results and errors
- **Registration**: Must be registered in ReactPackage

---

## 13) How do you create a custom native module for **iOS** using Objective-C/Swift?

Concept:
Create a native module by implementing RCTBridgeModule protocol and using RCT_EXPORT_MODULE macro.

Example:
```objc
// MyNativeModule.m
#import "MyNativeModule.h"
#import <React/RCTLog.h>

@implementation MyNativeModule

```

Deep Insight:
- **RCTBridgeModule**: Protocol for native modules
- **RCT_EXPORT_MODULE**: Exports module to JavaScript
- **RCT_EXPORT_METHOD**: Exports methods to JavaScript
- **Promise Blocks**: Handle resolve and reject callbacks
- **Objective-C**: Primary language for iOS native modules

---

## 14) How does **JSI** replace the old bridge for native communication?

Concept:
JSI allows direct function calls between JavaScript and native code, eliminating serialization overhead and enabling synchronous communication.

Example:
```jsx
// Old Bridge approach (asynchronous)
const result = await NativeModules.MyModule.doSomething(data);

// JSI approach (synchronous)
const result = MyModule.doSomething(data);
```

Deep Insight:
- **Direct Calls**: JavaScript can directly call native functions
- **Synchronous**: Enables synchronous communication when needed
- **No Serialization**: Eliminates data serialization overhead
- **Better Performance**: Faster communication between JS and native
- **Type Safety**: Better type checking and error handling

---

## 15) What are **TurboModules**, and how are they connected through JSI?

Concept:
TurboModules are the new native module system that uses JSI for direct communication, providing better performance and type safety.

Example:
```jsx
// TurboModule usage
import { NativeModules } from 'react-native';

const { MyTurboModule } = NativeModules;

// Direct function call through JSI
```

Deep Insight:
- **JSI Integration**: Uses JSI for direct communication
- **Type Safety**: Better type checking and validation
- **Performance**: Faster than bridge-based modules
- **Synchronous**: Can make synchronous calls when needed
- **Future Architecture**: Part of React Native's new architecture

---

## 16) How do you use native APIs like Camera, Location, or Sensors in React Native?

Concept:
Use third-party libraries or create custom native modules to access device APIs, with proper permissions and platform-specific implementations.

Example:
```jsx
// Using react-native-camera
import { RNCamera } from 'react-native-camera';

function CameraScreen() {
  const takePicture = async () => {
    if (cameraRef.current) {
```

Deep Insight:
- **Third-party Libraries**: Use existing libraries for common APIs
- **Permissions**: Request appropriate permissions at runtime
- **Platform Differences**: Handle iOS and Android differences
- **Error Handling**: Proper error handling for device APIs
- **Performance**: Consider performance implications of native APIs

---

## 17) What is a **headless JS task**, and when should it be used?

Concept:
Headless JS tasks run JavaScript code in the background on Android, useful for background processing and notifications.

Example:
```jsx
// HeadlessTask.js
import { AppRegistry } from 'react-native';
import BackgroundJob from 'react-native-background-job';

const HeadlessTask = async (taskData) => {
  console.log('Running headless task:', taskData);
```

Deep Insight:
- **Android Only**: Available only on Android platform
- **Background Processing**: Runs when app is not active
- **Limited Time**: Has time limits for execution
- **Use Cases**: Data sync, notifications, background tasks
- **Restrictions**: Limited access to UI and some APIs

---

## 18) How does **autolinking** work for native dependencies (since RN 0.60+)?

Concept:
Autolinking automatically links native dependencies by scanning package.json and configuring native projects, eliminating manual linking steps.

Example:
```json
// package.json
{
  "dependencies": {
    "react-native-camera": "^4.0.0",
    "react-native-vector-icons": "^9.0.0"
  }
```

Deep Insight:
- **Automatic Linking**: No manual linking required
- **Package Scanning**: Scans package.json for native dependencies
- **Configuration**: Automatically configures native projects
- **Platform Support**: Works for both iOS and Android
- **Migration**: Replaces manual linking process

---

## 19) What's the difference between **bridged** and **JSI-based** native modules?

Concept:
Bridged modules use the old bridge system with serialization, while JSI-based modules use direct function calls for better performance.

Example:
```jsx
// Bridged module (old)
const result = await NativeModules.BridgedModule.doSomething(data);

// JSI-based module (new)
const result = JSIModule.doSomething(data);
```

Deep Insight:
- **Bridge System**: Uses serialization and message passing
- **JSI System**: Direct function calls without serialization
- **Performance**: JSI is faster than bridge
- **Synchronous**: JSI enables synchronous calls
- **Migration**: Gradual migration from bridge to JSI

---

## 20) How do you handle **permissions** for native APIs on both platforms?

Concept:
Use platform-specific permission systems and libraries like react-native-permissions to request and check permissions at runtime.

Example:
```jsx
import { PermissionsAndroid, Platform } from 'react-native';
import { request, PERMISSIONS, RESULTS } from 'react-native-permissions';

const requestCameraPermission = async () => {
  if (Platform.OS === 'android') {
    const granted = await PermissionsAndroid.request(
```

Deep Insight:
- **Platform Differences**: Different permission systems for iOS and Android
- **Runtime Requests**: Request permissions when needed
- **User Experience**: Handle permission denials gracefully
- **Permission Libraries**: Use libraries for consistent permission handling
- **App Store Guidelines**: Follow platform-specific permission guidelines

---
