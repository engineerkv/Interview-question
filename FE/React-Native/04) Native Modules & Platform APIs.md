# 4. Native Modules & Platform APIs (Q32–39)

---

## 📍 Navigation

<div align="center">

[Navigation & App Lifecycle](03%29%20Navigation%20%26%20App%20Lifecycle.md) • [Home: README](../README.md) • [Platform-Specific Development →](05%29%20Platform-Specific%20Development.md)

[📋 Cheatsheet](React%20Native%20Interview%20Cheatsheet.md)

</div>

---

---

## Q32. 📱 Native modules in React Native

Native Modules are JavaScript interfaces to native platform APIs, needed to access device features not available through React Native's built-in components - uses TurboModule architecture with JSI. Access to device-specific functionality (platform APIs).

- **Trade-offs**: The catch is camera, sensors, file system, etc. (device features) - TurboModules use JSI for direct communication (better performance). Uses TurboModule architecture with JSI, but watch out - TurboModules provide lazy loading and type safety through codegen (New Architecture).

Example:

```jsx
// TurboModule approach (New Architecture)
import { TurboModuleRegistry } from 'react-native';
const MyTurboModule = TurboModuleRegistry.get('MyTurboModule');
const result = await MyTurboModule.doSomething();
```

---

## Q33. 📱 Creating custom native modules for Android

Create a native module using TurboModule - TurboModules use codegen for type safety and lazy loading. Base class for TurboModules (TurboModuleSpec).

- **Trade-offs**: The catch is TurboModules provide better performance and type safety - uses JSI for direct communication (20-500x faster). TurboModules use codegen for type safety and lazy loading, but watch out - TurboModules require TypeScript spec definition and codegen setup (New Architecture).

Example:

```java
// TurboModule approach (New Architecture)
package com.myapp;

import com.facebook.react.bridge.Promise;
import com.facebook.react.module.annotations.ReactModule;
import com.facebook.react.turbomodule.core.interfaces.TurboModule;

@ReactModule(name = MyModuleSpec.NAME)
public class MyModule extends MyModuleSpec {
  public MyModule(ReactApplicationContext reactContext) {
    super(reactContext);
  }

  @Override
  public String doSomething(String input) {
    return "Result: " + input;
  }
}
```

---

## Q34. 📱 Creating custom native modules for iOS

Create a native module using TurboModule - TurboModules use codegen for type safety and support Swift/Objective-C. Protocol for TurboModules (RCTTurboModule).

- **Trade-offs**: The catch is TurboModules provide better performance and type safety - uses JSI for direct communication (20-500x faster). TurboModules use codegen for type safety and support Swift/Objective-C, but watch out - TurboModules require TypeScript spec definition and codegen setup (New Architecture).

Example:

```objc
// TurboModule approach (New Architecture)
// MyModule.mm
#import <React/RCTBridgeModule.h>
#import <React/RCTTurboModule.h>

@interface RCT_EXTERN_MODULE(MyModule, NSObject)

RCT_EXTERN_METHOD(doSomething:(NSString *)input
                  resolver:(RCTPromiseResolveBlock)resolve
                  rejecter:(RCTPromiseRejectBlock)reject)

@end

// MyModule.swift (Swift implementation)
@objc(MyModule)
class MyModule: NSObject, MyModuleSpec {
  @objc
  static func requiresMainQueueSetup() -> Bool {
    return false
  }

  @objc
  func doSomething(_ input: String, resolver resolve: @escaping RCTPromiseResolveBlock, rejecter reject: @escaping RCTPromiseRejectBlock) {
    resolve("Result: \(input)")
  }
}
```

---

## Q35. 🧩 TurboModules and how they work

TurboModules are the native module system that uses JSI for direct communication, providing better performance and type safety - part of React Native's New Architecture (now stable in 0.73+). Uses JSI for direct communication with lazy loading and codegen.

- **Trade-offs**: The catch is faster than bridge-based modules (20-500x faster) - can make synchronous calls when needed (synchronous). Part of React Native's New Architecture (now stable in 0.73+), but watch out - uses codegen for type safety and lazy loading (modules load on demand).

Example:

```jsx
// TurboModule with TypeScript spec (codegen)
// NativeMyModule.ts (spec file)
import { TurboModule, TurboModuleRegistry } from 'react-native';

export interface Spec extends TurboModule {
  readonly getConstants: () => {
    readonly apiKey: string;
  };
  readonly doSomething: (input: string) => Promise<string>;
  readonly measureSync: (nodeId: number) => { width: number; height: number };
}

export default TurboModuleRegistry.get<Spec>('MyModule');

// Usage
import MyModule from './NativeMyModule';

// Lazy loaded - module loads here on first use
const result = await MyModule.doSomething('input');
const { width, height } = MyModule.measureSync(123); // Synchronous call
const apiKey = MyModule.getConstants().apiKey;
```

---

## Q36. 📱 Accessing native APIs like Camera, Location, and Sensors

Use third-party libraries or create custom native modules to access device APIs, with proper permissions and platform-specific implementations - modern libraries use TurboModules for better performance. Use existing libraries for common APIs (third-party libraries).

- **Trade-offs**: The catch is handle iOS and Android differences (platform differences) - proper error handling for device APIs. Modern libraries use TurboModules for better performance, but watch out - request appropriate permissions at runtime (permissions).

Example:

```jsx
// Camera - react-native-vision-camera (recommended, uses TurboModules)
import { Camera, useCameraDevice } from 'react-native-vision-camera';

function CameraScreen() {
  const device = useCameraDevice('back');
  const camera = useRef<Camera>(null);

  const takePicture = async () => {
    if (camera.current) {
      const photo = await camera.current.takePhoto({
        qualityPrioritization: 'speed',
        flash: 'off'
      });
      console.log('Photo taken:', photo.path);
    }
  };

  if (!device) return null;

  return (
    <Camera
      ref={camera}
      device={device}
      isActive={true}
      photo={true}
    />
  );
}

// Location - react-native-geolocation-service
import Geolocation from 'react-native-geolocation-service';

const getLocation = async () => {
  const position = await Geolocation.getCurrentPosition(
    (position) => {
      console.log(position.coords.latitude, position.coords.longitude);
    },
    (error) => console.error(error),
    { enableHighAccuracy: true, timeout: 15000 }
  );
};
```

---

## Q37. 💡 ⏰ Headless JS and when to use it

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

## Q38. 📱 How autolinking works in React Native

Autolinking automatically links native dependencies by scanning package.json and configuring native projects, eliminating manual linking steps - standard feature in React Native 0.60+ (no configuration needed). No manual linking required (automatic linking).

- **Trade-offs**: The catch is automatically configures native projects (configuration) - works for both iOS and Android (platform support). Standard feature in React Native 0.60+ (no configuration needed), but watch out - scans package.json for native dependencies and configures native projects automatically (package scanning).

Example:

```json
{
  "dependencies": {
    "react-native-vision-camera": "^4.0.0",
    "react-native-vector-icons": "^10.0.0"
  }
}

// After npm install, autolinking automatically:
// - Adds native dependencies to iOS Podfile
// - Configures Android gradle files
// - No manual linking required

// To disable autolinking for a specific package:
// react-native.config.js
module.exports = {
  dependencies: {
    'some-package': {
      platforms: {
        android: null, // disable Android autolinking
        ios: null, // disable iOS autolinking
      },
    },
  },
};
```

---

## Q39. 📱 Handling permissions in React Native

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
