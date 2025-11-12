# 🔌 2. Native Modules & Platform Integrations (Q11–20)

---

## 🧩 Q11. What are native modules in React Native?

### 🧠 Concept

Native Modules are JavaScript interfaces to native platform APIs, needed to access device features not available through React Native's built-in components. Different implementations for iOS and Android (platform specific).

---

### 💡 Example

```jsx
import { NativeModules } from 'react-native';

const { MyNativeModule } = NativeModules;

MyNativeModule.doSomething().then(result => console.log(result));
```

---

### 🔍 Deep Insights

* **Rule:** Access to device-specific functionality (platform APIs).
* **Use Case:** Native code runs faster than JavaScript (performance).
* **Common Mistake:** Camera, sensors, file system, etc. (device features).
* **Pro Tip:** Uses bridge to communicate with native code.

---

### ⭐ Senior Takeaway

Different implementations for iOS and Android (platform specific).

---

## 🧩 Q12. How do you create custom native modules for Android?

### 🧠 Concept

Create a native module by extending ReactContextBaseJavaModule and registering it in the ReactPackage. Must be registered in ReactPackage.

---

### 💡 Example

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

### 🔍 Deep Insights

* **Rule:** Base class for native modules (ReactContextBaseJavaModule).
* **Use Case:** `getName()` returns module name used in JavaScript.
* **Common Mistake:** `@ReactMethod` exposes methods to JavaScript.
* **Pro Tip:** Promise handles asynchronous results and errors.

---

### ⭐ Senior Takeaway

Must be registered in ReactPackage.

---

## 🧩 Q13. How do you create custom native modules for iOS?

### 🧠 Concept

Create a native module by implementing RCTBridgeModule protocol and using RCT_EXPORT_MODULE macro. Objective-C is primary language for iOS native modules.

---

### 💡 Example

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

### 🔍 Deep Insights

* **Rule:** Protocol for native modules (RCTBridgeModule).
* **Use Case:** `RCT_EXPORT_MODULE` exports module to JavaScript.
* **Common Mistake:** `RCT_EXPORT_METHOD` exports methods to JavaScript.
* **Pro Tip:** Promise blocks handle resolve and reject callbacks.

---

### ⭐ Senior Takeaway

Objective-C is primary language for iOS native modules.

---

## 🧩 Q14. What is the difference between JSI and the old bridge?

### 🧠 Concept

JSI allows direct function calls between JavaScript and native code, eliminating serialization overhead and enabling synchronous communication. Better type checking and error handling (type safety).

---

### 💡 Example

```jsx
// Old Bridge approach (asynchronous)
const result = await NativeModules.MyModule.doSomething(data);

// JSI approach (synchronous)
const result = MyModule.doSomething(data);
```

---

### 🔍 Deep Insights

* **Rule:** JavaScript can directly call native functions (direct calls).
* **Use Case:** Enables synchronous communication when needed (synchronous).
* **Common Mistake:** Eliminates data serialization overhead (no serialization).
* **Pro Tip:** Faster communication between JS and native (better performance).

---

### ⭐ Senior Takeaway

Better type checking and error handling (type safety).

---

## 🧩 Q15. What are TurboModules and how do they work?

### 🧠 Concept

TurboModules are the new native module system that uses JSI for direct communication, providing better performance and type safety. Part of React Native's new architecture (future architecture).

---

### 💡 Example

```jsx
import { NativeModules } from 'react-native';

const { MyTurboModule } = NativeModules;
// Direct function call through JSI
```

---

### 🔍 Deep Insights

* **Rule:** Uses JSI for direct communication (JSI integration).
* **Use Case:** Better type checking and validation (type safety).
* **Common Mistake:** Faster than bridge-based modules.
* **Pro Tip:** Can make synchronous calls when needed (synchronous).

---

### ⭐ Senior Takeaway

Part of React Native's new architecture (future architecture).

---

## 🧩 Q16. How do you access native APIs like Camera, Location, and Sensors?

### 🧠 Concept

Use third-party libraries or create custom native modules to access device APIs, with proper permissions and platform-specific implementations. Consider performance implications of native APIs.

---

### 💡 Example

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

### 🔍 Deep Insights

* **Rule:** Use existing libraries for common APIs (third-party libraries).
* **Use Case:** Request appropriate permissions at runtime (permissions).
* **Common Mistake:** Handle iOS and Android differences (platform differences).
* **Pro Tip:** Proper error handling for device APIs.

---

### ⭐ Senior Takeaway

Consider performance implications of native APIs.

---

## 🧩 Q17. What is Headless JS and when do you use it?

### 🧠 Concept

Headless JS tasks run JavaScript code in the background on Android, useful for background processing and notifications. Limited access to UI and some APIs (restrictions).

---

### 💡 Example

```jsx
import { AppRegistry } from 'react-native';

const HeadlessTask = async (taskData) => {
  console.log('Running headless task:', taskData);
  // Background processing
};

AppRegistry.registerHeadlessTask('BackgroundTask', () => HeadlessTask);
```

---

### 🔍 Deep Insights

* **Rule:** Available only on Android platform (Android only).
* **Use Case:** Runs when app is not active (background processing).
* **Common Mistake:** Has time limits for execution (limited time).
* **Pro Tip:** Data sync, notifications, background tasks.

---

### ⭐ Senior Takeaway

Limited access to UI and some APIs (restrictions).

---

## 🧩 Q18. How does autolinking work in React Native?

### 🧠 Concept

Autolinking automatically links native dependencies by scanning package.json and configuring native projects, eliminating manual linking steps. Replaces manual linking process (migration).

---

### 💡 Example

```json
{
  "dependencies": {
    "react-native-camera": "^4.0.0",
    "react-native-vector-icons": "^9.0.0"
  }
}
```

---

### 🔍 Deep Insights

* **Rule:** No manual linking required (automatic linking).
* **Use Case:** Scans package.json for native dependencies (package scanning).
* **Common Mistake:** Automatically configures native projects (configuration).
* **Pro Tip:** Works for both iOS and Android (platform support).

---

### ⭐ Senior Takeaway

Replaces manual linking process (migration).

---

## 🧩 Q19. What is the difference between bridged and JSI-based modules?

### 🧠 Concept

Bridged modules use the old bridge system with serialization, while JSI-based modules use direct function calls for better performance. JSI is the future of React Native modules.

---

### 💡 Example

```jsx
// Bridged module (old)
const result = await NativeModules.BridgedModule.doSomething(data);

// JSI-based module (new)
const result = JSIModule.doSomething(data);
```

---

### 🔍 Deep Insights

* **Rule:** Bridge system uses serialization and message passing; JSI system uses direct function calls without serialization.
* **Use Case:** JSI is faster than bridge (performance).
* **Common Mistake:** JSI enables synchronous calls (synchronous).
* **Pro Tip:** Gradual migration from bridge to JSI.

---

### ⭐ Senior Takeaway

JSI is the future of React Native modules.

---

## 🧩 Q20. How do you handle permissions in React Native?

### 🧠 Concept

Use platform-specific permission systems and libraries like react-native-permissions to request and check permissions at runtime. Follow platform-specific permission guidelines (app store guidelines).

---

### 💡 Example

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

### 🔍 Deep Insights

* **Rule:** Different permission systems for iOS and Android (platform differences).
* **Use Case:** Request permissions when needed (runtime requests).
* **Common Mistake:** Handle permission denials gracefully (user experience).
* **Pro Tip:** Use libraries for consistent permission handling (permission libraries).

---

### ⭐ Senior Takeaway

Follow platform-specific permission guidelines (app store guidelines).

---
