# 4. Native Modules & Platform APIs (Q32–41)

---

## 📍 Navigation

<div align="center">

[Navigation & App Lifecycle](03%29%20Navigation%20%26%20App%20Lifecycle.md) • [Home: README](../README.md) • [Platform-Specific Development →](05%29%20Platform-Specific%20Development.md)

[📋 Cheatsheet](React%20Native%20Interview%20Cheatsheet.md)

</div>

---

---

## Q32. 📱 Native modules in React Native

Native Modules are JavaScript interfaces to native platform APIs, needed to access device features not available through React Native's built-in components - different implementations for iOS and Android (platform specific). Access to device-specific functionality (platform APIs).

- **Trade-offs**: The catch is camera, sensors, file system, etc. (device features) - uses bridge to communicate with native code. Different implementations for iOS and Android (platform specific), but watch out - native code runs faster than JavaScript (performance).

Example:

```jsx
import { NativeModules } from 'react-native';

const { MyNativeModule } = NativeModules;

MyNativeModule.doSomething().then(result => console.log(result));

```

---

## Q33. 📱 Creating custom native modules for Android

Create a native module by extending ReactContextBaseJavaModule and registering it in the ReactPackage - must be registered in ReactPackage. Base class for native modules (ReactContextBaseJavaModule).

- **Trade-offs**: The catch is `@ReactMethod` exposes methods to JavaScript - promise handles asynchronous results and errors. Must be registered in ReactPackage, but watch out - `getName()` returns module name used in JavaScript.

Example:

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

---

## Q34. 📱 Creating custom native modules for iOS

Create a native module by implementing RCTBridgeModule protocol and using RCT_EXPORT_MODULE macro - Objective-C is primary language for iOS native modules. Protocol for native modules (RCTBridgeModule).

- **Trade-offs**: The catch is `RCT_EXPORT_METHOD` exports methods to JavaScript - promise blocks handle resolve and reject callbacks. Objective-C is primary language for iOS native modules, but watch out - `RCT_EXPORT_MODULE` exports module to JavaScript.

Example:

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

---

## Q35. 🤔 Difference between JSI and the old bridge

JSI allows direct function calls between JavaScript and native code, eliminating serialization overhead and enabling synchronous communication - better type checking and error handling (type safety). JavaScript can directly call native functions (direct calls).

- **Trade-offs**: The catch is eliminates data serialization overhead (no serialization) - faster communication between JS and native (better performance). Better type checking and error handling (type safety), but watch out - enables synchronous communication when needed (synchronous).

Example:

```jsx
// Old Bridge approach (asynchronous)
const result = await NativeModules.MyModule.doSomething(data);

// JSI approach (synchronous)
const result = MyModule.doSomething(data);

```

---

## Q36. 🧩 TurboModules and how they work

TurboModules are the new native module system that uses JSI for direct communication, providing better performance and type safety - part of React Native's new architecture (future architecture). Uses JSI for direct communication (JSI integration).

- **Trade-offs**: The catch is faster than bridge-based modules - can make synchronous calls when needed (synchronous). Part of React Native's new architecture (future architecture), but watch out - better type checking and validation (type safety).

Example:

```jsx
import { NativeModules } from 'react-native';

const { MyTurboModule } = NativeModules;
// Direct function call through JSI

```

---

## Q37. 📱 Accessing native APIs like Camera, Location, and Sensors

Use third-party libraries or create custom native modules to access device APIs, with proper permissions and platform-specific implementations - consider performance implications of native APIs. Use existing libraries for common APIs (third-party libraries).

- **Trade-offs**: The catch is handle iOS and Android differences (platform differences) - proper error handling for device APIs. Consider performance implications of native APIs, but watch out - request appropriate permissions at runtime (permissions).

Example:

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

---

## Q38. 💡 ⏰ Headless JS and when to use it

Headless JS tasks run JavaScript code in the background on Android, useful for background processing and notifications - limited access to UI and some APIs (restrictions). Available only on Android platform (Android only).

- **Trade-offs**: The catch is has time limits for execution (limited time) - data sync, notifications, background tasks. Limited access to UI and some APIs (restrictions), but watch out - runs when app is not active (background processing).

Example:

```jsx
import { AppRegistry } from 'react-native';

const HeadlessTask = async (taskData) => {
  console.log('Running headless task:', taskData);
  // Background processing
};

AppRegistry.registerHeadlessTask('BackgroundTask', () => HeadlessTask);

```

---

## Q39. 📱 How autolinking works in React Native

Autolinking automatically links native dependencies by scanning package.json and configuring native projects, eliminating manual linking steps - replaces manual linking process (migration). No manual linking required (automatic linking).

- **Trade-offs**: The catch is automatically configures native projects (configuration) - works for both iOS and Android (platform support). Replaces manual linking process (migration), but watch out - scans package.json for native dependencies (package scanning).

Example:

```json
{
  "dependencies": {
    "react-native-camera": "^4.0.0",
    "react-native-vector-icons": "^9.0.0"
  }
}

```

---

## Q40. 🧩 Difference between bridged and JSI-based modules

Bridged modules use the old bridge system with serialization, while JSI-based modules use direct function calls for better performance - JSI is the future of React Native modules. Bridge system uses serialization and message passing; JSI system uses direct function calls without serialization.

- **Trade-offs**: The catch is JSI enables synchronous calls (synchronous) - gradual migration from bridge to JSI. JSI is the future of React Native modules, but watch out - JSI is faster than bridge (performance).

Example:

```jsx
// Bridged module (old)
const result = await NativeModules.BridgedModule.doSomething(data);

// JSI-based module (new)
const result = JSIModule.doSomething(data);

```

---

## Q41. 📱 Handling permissions in React Native

Use platform-specific permission systems and libraries like react-native-permissions to request and check permissions at runtime - follow platform-specific permission guidelines (app store guidelines). Different permission systems for iOS and Android (platform differences).

- **Trade-offs**: The catch is handle permission denials gracefully (user experience) - use libraries for consistent permission handling (permission libraries). Follow platform-specific permission guidelines (app store guidelines), but watch out - request permissions when needed (runtime requests).

Example:

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

---

## 📍 Navigation

<div align="center">

[Navigation & App Lifecycle](03%29%20Navigation%20%26%20App%20Lifecycle.md) • [Home: README](../README.md) • [Platform-Specific Development →](05%29%20Platform-Specific%20Development.md)

[📋 Cheatsheet](React%20Native%20Interview%20Cheatsheet.md)

</div>

---
