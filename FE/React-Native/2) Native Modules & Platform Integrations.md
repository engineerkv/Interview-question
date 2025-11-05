# 🔌 2. Native Modules & Platform Integrations (Q11–20)

---

## 11) What are **Native Modules**, and why do we need them in React Native?

Native Modules are JavaScript interfaces to native platform APIs, needed to access device features not available through React Native's built-in components.

```jsx
import { NativeModules } from 'react-native';

const { MyNativeModule } = NativeModules;

MyNativeModule.doSomething().then(result => console.log(result));
```

- **Core Purpose**: Access to device-specific functionality (platform APIs)
- **Real-World Use**: Native code runs faster than JavaScript (performance)
- **Common Use Cases**: Camera, sensors, file system, etc. (device features)
- **Architecture**: Uses bridge to communicate with native code
- **Interview Tip**: Explain that different implementations for iOS and Android (platform specific)

---

## 12) How do you create a custom native module for **Android** using Java/Kotlin?

Create a native module by extending ReactContextBaseJavaModule and registering it in the ReactPackage.

```java
package com.myapp;

import com.facebook.react.bridge.ReactContextBaseJavaModule;
import com.facebook.react.bridge.ReactMethod;

public class MyNativeModule extends ReactContextBaseJavaModule {
  @ReactMethod
  public void doSomething(Promise promise) {
    promise.resolve("Result from native");
  }
}
```

- **Core Class**: Base class for native modules (ReactContextBaseJavaModule)
- **Real-World Use**: `getName()` returns module name used in JavaScript
- **Common Pattern**: `@ReactMethod` exposes methods to JavaScript
- **Advanced Feature**: Promise handles asynchronous results and errors
- **Interview Tip**: Explain that must be registered in ReactPackage

---

## 13) How do you create a custom native module for **iOS** using Objective-C/Swift?

Create a native module by implementing RCTBridgeModule protocol and using RCT_EXPORT_MODULE macro.

```objc
// MyNativeModule.m
#import "MyNativeModule.h"
#import <React/RCTLog.h>

@implementation MyNativeModule

RCT_EXPORT_MODULE();

RCT_EXPORT_METHOD(doSomething:(RCTPromiseResolveBlock)resolve
                  rejecter:(RCTPromiseRejectBlock)reject)
{
  resolve(@"Result from native");
}

@end
```

- **Core Protocol**: Protocol for native modules (RCTBridgeModule)
- **Real-World Use**: `RCT_EXPORT_MODULE` exports module to JavaScript
- **Common Pattern**: `RCT_EXPORT_METHOD` exports methods to JavaScript
- **Advanced Feature**: Promise blocks handle resolve and reject callbacks
- **Interview Tip**: Explain that Objective-C is primary language for iOS native modules

---

## 14) How does **JSI** replace the old bridge for native communication?

JSI allows direct function calls between JavaScript and native code, eliminating serialization overhead and enabling synchronous communication.

```jsx
// Old Bridge approach (asynchronous)
const result = await NativeModules.MyModule.doSomething(data);

// JSI approach (synchronous)
const result = MyModule.doSomething(data);
```

- **Core Advantage**: JavaScript can directly call native functions (direct calls)
- **Real-World Benefit**: Enables synchronous communication when needed (synchronous)
- **Performance**: Eliminates data serialization overhead (no serialization)
- **Advanced Feature**: Faster communication between JS and native (better performance)
- **Interview Tip**: Explain that better type checking and error handling (type safety)

---

## 15) What are **TurboModules**, and how are they connected through JSI?

TurboModules are the new native module system that uses JSI for direct communication, providing better performance and type safety.

```jsx
import { NativeModules } from 'react-native';

const { MyTurboModule } = NativeModules;
// Direct function call through JSI
```

- **Core Architecture**: Uses JSI for direct communication (JSI integration)
- **Real-World Benefit**: Better type checking and validation (type safety)
- **Performance**: Faster than bridge-based modules
- **Advanced Feature**: Can make synchronous calls when needed (synchronous)
- **Interview Tip**: Explain that part of React Native's new architecture (future architecture)

---

## 16) How do you use native APIs like Camera, Location, or Sensors in React Native?

Use third-party libraries or create custom native modules to access device APIs, with proper permissions and platform-specific implementations.

```jsx
import { RNCamera } from 'react-native-camera';

function CameraScreen() {
  const takePicture = async () => {
    if (cameraRef.current) {
      const options = { quality: 0.5, base64: true };
      const data = await cameraRef.current.takePictureAsync(options);
    }
  };
  return <RNCamera ref={cameraRef} />;
}
```

- **Core Approach**: Use existing libraries for common APIs (third-party libraries)
- **Real-World Requirement**: Request appropriate permissions at runtime (permissions)
- **Common Challenge**: Handle iOS and Android differences (platform differences)
- **Advanced Practice**: Proper error handling for device APIs
- **Interview Tip**: Explain that consider performance implications of native APIs

---

## 17) What is a **headless JS task**, and when should it be used?

Headless JS tasks run JavaScript code in the background on Android, useful for background processing and notifications.

```jsx
import { AppRegistry } from 'react-native';

const HeadlessTask = async (taskData) => {
  console.log('Running headless task:', taskData);
  // Background processing
};

AppRegistry.registerHeadlessTask('BackgroundTask', () => HeadlessTask);
```

- **Core Limitation**: Available only on Android platform (Android only)
- **Real-World Use**: Runs when app is not active (background processing)
- **Common Constraint**: Has time limits for execution (limited time)
- **Use Cases**: Data sync, notifications, background tasks
- **Interview Tip**: Explain that limited access to UI and some APIs (restrictions)

---

## 18) How does **autolinking** work for native dependencies (since RN 0.60+)?

Autolinking automatically links native dependencies by scanning package.json and configuring native projects, eliminating manual linking steps.

```json
{
  "dependencies": {
    "react-native-camera": "^4.0.0",
    "react-native-vector-icons": "^9.0.0"
  }
}
```

- **Core Feature**: No manual linking required (automatic linking)
- **Real-World Process**: Scans package.json for native dependencies (package scanning)
- **Common Benefit**: Automatically configures native projects (configuration)
- **Advanced Feature**: Works for both iOS and Android (platform support)
- **Interview Tip**: Explain that replaces manual linking process (migration)

---

## 19) What's the difference between **bridged** and **JSI-based** native modules?

Bridged modules use the old bridge system with serialization, while JSI-based modules use direct function calls for better performance.

```jsx
// Bridged module (old)
const result = await NativeModules.BridgedModule.doSomething(data);

// JSI-based module (new)
const result = JSIModule.doSomething(data);
```

- **Core Difference**: Bridge system uses serialization and message passing; JSI system uses direct function calls without serialization
- **Real-World Impact**: JSI is faster than bridge (performance)
- **Advanced Feature**: JSI enables synchronous calls (synchronous)
- **Migration Path**: Gradual migration from bridge to JSI
- **Interview Tip**: Explain that JSI is the future of React Native modules

---

## 20) How do you handle **permissions** for native APIs on both platforms?

Use platform-specific permission systems and libraries like react-native-permissions to request and check permissions at runtime.

```jsx
import { Platform } from 'react-native';
import { request, PERMISSIONS, RESULTS } from 'react-native-permissions';

const requestCameraPermission = async () => {
  const permission = Platform.OS === 'ios' 
    ? PERMISSIONS.IOS.CAMERA 
    : PERMISSIONS.ANDROID.CAMERA;
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
