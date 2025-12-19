# 8. Hardware & System APIs (Q74–84)

---

## 📍 Navigation

<div align="center">

[Animations & Graphics](07%29%20Animations%20%26%20Graphics.md) • [Home: README](../README.md) • [Testing & Debugging →](09%29%20Testing%20%26%20Debugging.md)

[📋 Cheatsheet](React%20Native%20Interview%20Cheatsheet.md)

</div>

---

---

## Q74. 📡 Implementing Bluetooth functionality in React Native

Use react-native-bluetooth-serial or react-native-ble-plx for Bluetooth communication - essential for IoT and device connectivity. Bluetooth Classic (serial communication), BLE (Bluetooth Low Energy), Platform differences (iOS vs Android).

- **Trade-offs**: The catch is requires native permissions (permissions) - different APIs for iOS and Android (platform differences). Essential for IoT and device connectivity, but watch out - handle connection states and errors (error handling).

Example:

```jsx
import { BleManager } from 'react-native-ble-plx';

const manager = new BleManager();

// Scan for devices
manager.startDeviceScan(null, null, (error, device) => {
  if (error) {
    console.error('Scan error:', error);
    return;
  }
  console.log('Found device:', device.name);
});

// Connect to device
const connectToDevice = async (deviceId) => {
  const device = await manager.connectToDevice(deviceId);
  await device.discoverAllServicesAndCharacteristics();
  return device;
};
```

---

## Q75. 📡 Using Bluetooth Low Energy (BLE) in React Native

BLE is energy-efficient Bluetooth protocol for IoT devices - use react-native-ble-plx for BLE communication. Low energy consumption (battery efficiency), IoT device support (device connectivity), GATT services (service discovery).

- **Trade-offs**: The catch is requires understanding BLE concepts (BLE knowledge) - different from Bluetooth Classic (protocol differences). Use react-native-ble-plx for BLE communication, but watch out - handle BLE-specific errors and states (error handling).

Example:

```jsx
import { BleManager } from 'react-native-ble-plx';

const manager = new BleManager();

// Read characteristic
const readCharacteristic = async (deviceId, serviceUUID, characteristicUUID) => {
  const device = await manager.connectToDevice(deviceId);
  const characteristic = await device.readCharacteristicForService(
    serviceUUID,
    characteristicUUID
  );
  return characteristic.value;
};

// Write characteristic
const writeCharacteristic = async (deviceId, serviceUUID, characteristicUUID, value) => {
  const device = await manager.connectToDevice(deviceId);
  await device.writeCharacteristicWithResponseForService(
    serviceUUID,
    characteristicUUID,
    value
  );
};
```

---

## Q76. 🔄 Background services and tasks in React Native

Background services run tasks when app is in background - essential for data sync and notifications. Background tasks (task execution), Platform differences (iOS vs Android), Battery optimization (battery efficiency).

- **Trade-offs**: The catch is platform-specific limitations (platform limitations) - battery impact (battery optimization). Essential for data sync and notifications, but watch out - use appropriate background task type (task selection).

Example:

```jsx
// Android: Background service
import BackgroundFetch from 'react-native-background-fetch';

BackgroundFetch.configure({
  minimumFetchInterval: 15, // minutes
}, async (taskId) => {
  // Background task
  await syncData();
  BackgroundFetch.finish(taskId);
});

// iOS: Background tasks
import BackgroundTasks from 'react-native-background-tasks';

BackgroundTasks.defineTask('syncTask', async () => {
  await syncData();
});
```

---

## Q77. 🔄 Implementing background sync on Android

Android background sync uses WorkManager or BackgroundFetch for scheduled tasks - handle Android-specific limitations. WorkManager (recommended), BackgroundFetch (alternative), Battery optimization (battery efficiency).

- **Trade-offs**: The catch is Android battery optimization restrictions (battery restrictions) - requires proper configuration (configuration). Handle Android-specific limitations, but watch out - use WorkManager for reliable background tasks (reliability).

Example:

```jsx
import BackgroundFetch from 'react-native-background-fetch';

// Configure background fetch
BackgroundFetch.configure({
  minimumFetchInterval: 15,
  stopOnTerminate: false,
  startOnBoot: true,
}, async (taskId) => {
  // Sync data
  await syncData();
  BackgroundFetch.finish(taskId);
}, (error) => {
  console.error('Background fetch failed:', error);
});

// Start background fetch
BackgroundFetch.start();
```

---

## Q78. 🔄 Implementing background tasks on iOS

iOS background tasks use BackgroundTasks framework for scheduled tasks - handle iOS-specific limitations. BackgroundTasks (iOS framework), Background modes (Info.plist), Task scheduling (scheduling).

- **Trade-offs**: The catch is iOS background execution limits (execution limits) - requires background modes configuration (configuration). Handle iOS-specific limitations, but watch out - background tasks have time limits (time limits).

Example:

```jsx
import BackgroundTasks from 'react-native-background-tasks';

// Define background task
BackgroundTasks.defineTask('syncTask', async () => {
  await syncData();
});

// Schedule background task
const scheduleBackgroundTask = () => {
  BackgroundTasks.scheduleTask({
    taskName: 'syncTask',
    delay: 15 * 60 * 1000, // 15 minutes
  });
};

// iOS Info.plist configuration required:
// <key>UIBackgroundModes</key>
// <array>
//   <string>background-processing</string>
// </array>
```

---

## Q79. 📁 File system operations in React Native

Use react-native-fs or expo-file-system for file operations - essential for data persistence and file management. File reading (read operations), File writing (write operations), Directory operations (directory management).

- **Trade-offs**: The catch is platform-specific file paths (platform differences) - handle permissions (permissions). Essential for data persistence and file management, but watch out - use appropriate storage location (storage selection).

Example:

```jsx
import RNFS from 'react-native-fs';

// Read file
const readFile = async (path) => {
  try {
    const content = await RNFS.readFile(path, 'utf8');
    return content;
  } catch (error) {
    console.error('Read error:', error);
  }
};

// Write file
const writeFile = async (path, content) => {
  try {
    await RNFS.writeFile(path, content, 'utf8');
  } catch (error) {
    console.error('Write error:', error);
  }
};

// Check if file exists
const fileExists = async (path) => {
  return await RNFS.exists(path);
};
```

---

## Q80. 📁 Reading and writing files on Android

Android file operations use Android file system APIs - handle Android-specific paths and permissions. Storage locations (internal/external), Permissions (runtime permissions), File paths (path handling).

- **Trade-offs**: The catch is Android storage scoped access (storage restrictions) - handle different Android versions (version compatibility). Handle Android-specific paths and permissions, but watch out - use appropriate storage location (storage selection).

Example:

```jsx
import RNFS from 'react-native-fs';
import { PermissionsAndroid, Platform } from 'react-native';

// Request storage permission
const requestStoragePermission = async () => {
  if (Platform.OS === 'android') {
    const granted = await PermissionsAndroid.request(
      PermissionsAndroid.PERMISSIONS.WRITE_EXTERNAL_STORAGE
    );
    return granted === PermissionsAndroid.RESULTS.GRANTED;
  }
  return true;
};

// Android file paths
const androidPaths = {
  internal: RNFS.DocumentDirectoryPath,
  external: RNFS.ExternalDirectoryPath,
  cache: RNFS.CachesDirectoryPath,
};

// Write to Android storage
const writeToAndroid = async (filename, content) => {
  const hasPermission = await requestStoragePermission();
  if (!hasPermission) return;

  const path = `${RNFS.DocumentDirectoryPath}/${filename}`;
  await RNFS.writeFile(path, content, 'utf8');
};
```

---

## Q81. 📁 Reading and writing files on iOS

iOS file operations use iOS file system APIs - handle iOS-specific paths and sandbox restrictions. Sandbox restrictions (iOS sandbox), File paths (path handling), iCloud integration (optional).

- **Trade-offs**: The catch is iOS sandbox limitations (sandbox restrictions) - app-specific directories only (directory restrictions). Handle iOS-specific paths and sandbox restrictions, but watch out - use appropriate iOS directory (directory selection).

Example:

```jsx
import RNFS from 'react-native-fs';

// iOS file paths
const iosPaths = {
  documents: RNFS.DocumentDirectoryPath,
  library: RNFS.LibraryDirectoryPath,
  cache: RNFS.CachesDirectoryPath,
  temp: RNFS.TemporaryDirectoryPath,
};

// Write to iOS storage
const writeToiOS = async (filename, content) => {
  const path = `${RNFS.DocumentDirectoryPath}/${filename}`;
  await RNFS.writeFile(path, content, 'utf8');
};

// Read from iOS storage
const readFromiOS = async (filename) => {
  const path = `${RNFS.DocumentDirectoryPath}/${filename}`;
  return await RNFS.readFile(path, 'utf8');
};
```

---

## Q82. 🔒 Handling file permissions and security

File permissions control access to files and directories - essential for data security. Permission requests (runtime permissions), File encryption (data encryption), Secure storage (secure locations).

- **Trade-offs**: The catch is platform-specific permission models (platform differences) - balance security and usability (security balance). Essential for data security, but watch out - use secure storage for sensitive data (security).

Example:

```jsx
import RNFS from 'react-native-fs';
import * as Keychain from 'react-native-keychain';

// Store sensitive data securely
const storeSecureData = async (key, data) => {
  // Use Keychain for sensitive data
  await Keychain.setGenericPassword(key, data);
};

// Store non-sensitive data in files
const storeFileData = async (filename, data) => {
  const path = `${RNFS.DocumentDirectoryPath}/${filename}`;
  await RNFS.writeFile(path, data, 'utf8');
};

// Request file permissions
const requestFilePermissions = async () => {
  if (Platform.OS === 'android') {
    const granted = await PermissionsAndroid.requestMultiple([
      PermissionsAndroid.PERMISSIONS.READ_EXTERNAL_STORAGE,
      PermissionsAndroid.PERMISSIONS.WRITE_EXTERNAL_STORAGE,
    ]);
    return Object.values(granted).every(
      status => status === PermissionsAndroid.RESULTS.GRANTED
    );
  }
  return true; // iOS handles permissions automatically
};
```

---

## Q83. 📱 Accessing device sensors and hardware APIs

Access device sensors like accelerometer, gyroscope, and magnetometer using react-native-sensors - essential for sensor-based apps. Sensor access (sensor APIs), Hardware APIs (hardware access), Platform support (cross-platform).

- **Trade-offs**: The catch is battery impact (battery consumption) - requires native modules (native dependencies). Essential for sensor-based apps, but watch out - handle sensor data efficiently (data efficiency).

Example:

```jsx
import { accelerometer, gyroscope, magnetometer } from 'react-native-sensors';

// Subscribe to accelerometer
const subscription = accelerometer.subscribe(({ x, y, z }) => {
  console.log('Accelerometer:', { x, y, z });
});

// Subscribe to gyroscope
const gyroSubscription = gyroscope.subscribe(({ x, y, z }) => {
  console.log('Gyroscope:', { x, y, z });
});

// Cleanup
subscription.unsubscribe();
gyroSubscription.unsubscribe();
```

---

## Q84. 🔌 Platform-specific API integrations

Integrate platform-specific APIs like Camera, Location, Contacts using native modules - essential for platform features. Native modules (module creation), Platform APIs (API access), Bridge communication (bridge usage).

- **Trade-offs**: The catch is requires native code knowledge (native knowledge) - platform-specific implementations (platform differences). Essential for platform features, but watch out - use existing libraries when possible (library usage).

Example:

```jsx
// Camera integration - react-native-vision-camera (recommended)
import { Camera, useCameraDevice } from 'react-native-vision-camera';
import { useRef } from 'react';

function CameraComponent() {
  const device = useCameraDevice('back');
  const camera = useRef<Camera>(null);

  const takePicture = async () => {
    if (camera.current) {
      const photo = await camera.current.takePhoto({
        qualityPrioritization: 'speed',
        flash: 'off'
      });
      return photo.path;
    }
  };

  if (!device) return null;

  return (
    <Camera
      ref={camera}
      device={device}
      isActive={true}
      photo={true}
      style={{ flex: 1 }}
    />
  );
}

// Location integration
import Geolocation from '@react-native-community/geolocation';

const getCurrentLocation = () => {
  return new Promise((resolve, reject) => {
    Geolocation.getCurrentPosition(
      (position) => resolve(position),
      (error) => reject(error)
    );
  });
};
```

---

---

## 📍 Navigation

<div align="center">

[Animations & Graphics](07%29%20Animations%20%26%20Graphics.md) • [Home: README](../README.md) • [Testing & Debugging →](09%29%20Testing%20%26%20Debugging.md)

[📋 Cheatsheet](React%20Native%20Interview%20Cheatsheet.md)

</div>

---
