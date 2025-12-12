# 9. Testing & Debugging (Q85–98)

---

## 📍 Navigation

<div align="center">

[Hardware & System APIs](08%29%20Hardware%20%26%20System%20APIs.md) • [Home: README](../README.md) • [Build & Release Management →](10%29%20Build%20%26%20Release%20Management.md)

[📋 Cheatsheet](React%20Native%20Interview%20Cheatsheet.md)

</div>

---

---

## Q85. 🐛 Debugging React Native apps

Use Flipper for native debugging and Chrome DevTools for JavaScript debugging - use Flipper for native debugging, Chrome for JS. Flipper (comprehensive debugging platform for React Native), Chrome DevTools (JavaScript debugging and profiling).

- **Trade-offs**: The catch is profile app performance and memory usage (performance) - works on both iOS and Android (platform support). Use Flipper for native debugging, Chrome for JS, but watch out - debug network requests and responses (network debugging).

Example:

```jsx
import { Flipper } from 'react-native-flipper';

function App() {
  useEffect(() => {
    // Flipper network debugging
    Flipper.addPlugin({
      getId: () => 'Network',
      onConnect: () => {}
    });
  }, []);
}

```

---

## Q86. 🐛 Using Flipper for React Native debugging

Remote debugging runs JavaScript on Chrome, useful for debugging but can cause performance issues and should be avoided in production - never use in production. Use only in development (development only).

- **Trade-offs**: The catch is may behave differently than production (different behavior) - can cause memory leaks (memory issues). Never use in production, but watch out - can cause performance issues (performance impact).

Example:

```jsx
// Remote debugging setup
// Enable in development only
if (__DEV__) {
  // Enable remote debugging
  // This runs JavaScript on Chrome
  // Good for debugging but affects performance
}

```

---

## Q87. 🐛 Debugging with Chrome DevTools

Flipper is a debugging platform that provides plugins for network inspection, layout debugging, and performance monitoring - Flipper is essential for React Native debugging. Network plugin (debug network requests and responses), Layout plugin (debug UI layout and styling), Performance plugin (monitor app performance).

- **Trade-offs**: The catch is create custom debugging plugins (custom plugins) - comprehensive debugging capabilities. Flipper is essential for React Native debugging, but watch out - crash plugin (debug crashes and errors).

Example:

```jsx
import { Flipper } from 'react-native-flipper';

Flipper.addPlugin({
  getId: () => 'Network',
  onConnect: () => {}
});

```

---

## Q88. 💡 Creating custom Flipper plugins

Use Jest with React Native Testing Library to test components, hooks, and user interactions - handle asynchronous operations in tests (async testing). Jest (JavaScript testing framework).

- **Trade-offs**: The catch is test component rendering and behavior (component testing) - test user interactions and events (user interactions). Handle asynchronous operations in tests (async testing), but watch out - React Native Testing Library (testing utilities for React Native).

Example:

```jsx
import { render, fireEvent, waitFor } from '@testing-library/react-native';
import MyComponent from '../MyComponent';

describe('MyComponent', () => {
  test('renders correctly', () => {
    const { getByText } = render(<MyComponent />);
    expect(getByText('Hello')).toBeTruthy();
  });
});

```

---


Use Detox to write and run E2E tests that interact with the app like a real user - integrate with CI/CD pipelines. Test complete user workflows (E2E testing).

- **Trade-offs**: The catch is simulate real user interactions (user interactions) - test on both iOS and Android (cross-platform). Integrate with CI/CD pipelines, but watch out - test on real devices (real device testing).

Example:

```jsx
describe('Login Flow', () => {
  beforeAll(async () => {
    await device.launchApp();
  });

  it('should login successfully', async () => {
    await element(by.id('email-input')).typeText('user@example.com');
    await element(by.id('password-input')).typeText('password');
    await element(by.id('login-button')).tap();
    await expect(element(by.id('home-screen'))).toBeVisible();
  });
});

```

---

## Q86. 🧪 Implementing end-to-end testing with Detox

Use Jest's mocking capabilities to mock native modules and their methods - isolate tests from external dependencies (test isolation). Mock native modules for testing (module mocking).

- **Trade-offs**: The catch is handle asynchronous operations in mocks (async mocking) - mock platform-specific functionality (platform mocking). Isolate tests from external dependencies (test isolation), but watch out - mock specific methods and return values (method mocking).

Example:

```jsx
jest.mock('react-native-camera', () => ({
  RNCamera: {
    Constants: {
      Type: {
        back: 'back',
        front: 'front'
      }
    }
  }
}));

```

---

## Q91. 🧪 Mocking native modules in tests

Use async/await, promises, and Jest's async testing utilities to test asynchronous code - test error cases in async code (error handling). Use async/await for asynchronous tests (async testing).

- **Trade-offs**: The catch is mock async functions and network requests (mocking) - use waitFor for async operations (wait for). Test error cases in async code (error handling), but watch out - handle promises in tests (promise testing).

Example:

```jsx
test('fetches user data', async () => {
  const mockUser = { id: 1, name: 'John Doe' };

  global.fetch = jest.fn().mockResolvedValue({
    ok: true,
    json: async () => mockUser
  });

  const user = await fetchUser(1);
  expect(user).toEqual(mockUser);
});

```

---

## Q92. ⚡ Testing asynchronous behavior in React Native

Use gesture simulation methods provided by testing frameworks to test touch interactions - test multi-touch interactions (multi-touch). Simulate touch gestures in tests (gesture simulation).

- **Trade-offs**: The catch is test long press interactions (long press) - test pinch and zoom interactions (pinch gestures). Test multi-touch interactions (multi-touch), but watch out - test swipe interactions (swipe gestures).

Example:

```jsx
describe('Gesture Tests', () => {
  it('should handle swipe gesture', async () => {
    await element(by.id('swipeable-item')).swipe('left');
    await expect(element(by.id('delete-button'))).toBeVisible();
  });
});

```

---

## Q93. 🧪 Simulating gestures in tests

Avoid slow tests, memory leaks, and inefficient test setup that can impact test performance - keep tests isolated and independent (test isolation). Avoid unnecessary waits and timeouts (slow tests).

- **Trade-offs**: The catch is mock heavy dependencies (heavy dependencies) - mock network requests (network requests). Keep tests isolated and independent (test isolation), but watch out - clean up resources in tests (memory leaks).

Example:

```jsx
// ❌ Performance pitfalls
describe('Slow Tests', () => {
  test('slow test with unnecessary waits', async () => {
    // Don't use unnecessary timeouts
    await new Promise(resolve => setTimeout(resolve, 1000));
  });
});

// ✅ Better: Use proper async testing
describe('Fast Tests', () => {
  test('fast test with proper mocking', async () => {
    // Mock async operations
  });
});

```

---

## Q87. 🐛 Debugging native crashes on Android

Debug Android native crashes using logcat, Android Studio debugger, and native crash reports - critical for identifying native module issues. Use logcat for crash logs (logcat), Use Android Studio debugger (native debugging), Analyze native stack traces (stack traces).

- **Trade-offs**: The catch is requires understanding native Android code (native knowledge) - different from JavaScript debugging (debugging approach). Critical for identifying native module issues, but watch out - use symbolication for readable stack traces (symbolication).

Example:

```bash
# View crash logs
adb logcat | grep -i "fatal\|crash\|exception"

# Common Android native crash causes:
# - NullPointerException
# - OutOfMemoryError
# - Native module errors
# - JNI errors

# Debugging steps:
# 9. Check logcat for crash logs
# 9. Use Android Studio to attach debugger
# 9. Analyze native stack traces
# 9. Check native module code
```

---

## Q88. 🐛 Debugging native crashes on iOS

Debug iOS native crashes using Xcode crash reports, symbolication, and native debugging tools - critical for identifying native module issues. Use Xcode crash reports (crash reports), Symbolicate crash logs (symbolication), Use Xcode debugger (native debugging).

- **Trade-offs**: The catch is requires understanding native iOS code (native knowledge) - requires macOS and Xcode (platform requirement). Critical for identifying native module issues, but watch out - use dSYM files for symbolication (symbolication).

Example:

```bash
# View crash reports in Xcode:
# 9. Window > Devices and Simulators
# 9. Select device > View Device Logs
# 9. Find crash report

# Common iOS native crash causes:
# - EXC_BAD_ACCESS (memory access violation)
# - EXC_CRASH (uncaught exception)
# - Native module errors
# - Threading issues

# Symbolication:
# 9. Ensure dSYM files are available
# 9. Use symbolicatecrash tool
# 9. Match addresses to source code
```

---

## Q89. 🔍 Using Xcode Instruments for debugging

Xcode Instruments provides debugging tools like Time Profiler, Allocations, and Leaks for iOS apps - essential for debugging performance and memory issues. Time Profiler (CPU debugging), Allocations (memory debugging), Leaks (memory leak detection).

- **Trade-offs**: The catch is requires macOS and Xcode (platform requirement) - provides detailed debugging insights (detailed analysis). Essential for debugging performance and memory issues, but watch out - use appropriate instrument for specific issues (tool selection).

Example:

```bash
# Using Xcode Instruments:
# 9. Product > Profile (Cmd+I)
# 9. Select appropriate instrument:
#    - Time Profiler: CPU bottlenecks
#    - Allocations: Memory usage
#    - Leaks: Memory leaks
#    - Network: Network activity
# 9. Record and analyze data

# Debugging workflow:
# 9. Identify issue (crash, performance, memory)
# 9. Select appropriate instrument
# 9. Record app behavior
# 9. Analyze collected data
# 9. Fix identified issues
```

---

## Q90. 🔍 Using Android Studio Profiler for debugging

Android Studio Profiler provides CPU, Memory, and Network profiling tools for debugging Android apps - essential for debugging performance and memory issues. CPU Profiler (CPU debugging), Memory Profiler (memory debugging), Network Profiler (network debugging).

- **Trade-offs**: The catch is requires Android Studio (platform requirement) - provides real-time debugging data (real-time analysis). Essential for debugging performance and memory issues, but watch out - use appropriate profiler for specific issues (tool selection).

Example:

```bash
# Using Android Studio Profiler:
# 9. View > Tool Windows > Profiler
# 9. Select appropriate profiler:
#    - CPU: CPU usage and threads
#    - Memory: Heap and allocations
#    - Network: Network requests
# 9. Record and analyze data

# Debugging workflow:
# 9. Identify issue (crash, performance, memory)
# 9. Select appropriate profiler
# 9. Record app behavior
# 9. Analyze collected data
# 9. Fix identified issues
```

---


Use Jest with React Native Testing Library to test components, hooks, and user interactions - handle asynchronous operations in tests (async testing). Jest (JavaScript testing framework).

- **Trade-offs**: The catch is test component rendering and behavior (component testing) - test user interactions and events (user interactions). Handle asynchronous operations in tests (async testing), but watch out - React Native Testing Library (testing utilities for React Native).

Example:

```jsx
import { render, fireEvent, waitFor } from '@testing-library/react-native';
import MyComponent from '../MyComponent';

describe('MyComponent', () => {
  test('renders correctly', () => {
    const { getByText } = render(<MyComponent />);
    expect(getByText('Hello')).toBeTruthy();
  });
});
```

---

## Q86. 🧪 Implementing end-to-end testing with Detox

Use Detox to write and run E2E tests that interact with the app like a real user - integrate with CI/CD pipelines. Test complete user workflows (E2E testing).

- **Trade-offs**: The catch is simulate real user interactions (user interactions) - test on both iOS and Android (cross-platform). Integrate with CI/CD pipelines, but watch out - test on real devices (real device testing).

Example:

```jsx
describe('Login Flow', () => {
  beforeAll(async () => {
    await device.launchApp();
  });

  it('should login successfully', async () => {
    await element(by.id('email-input')).typeText('user@example.com');
    await element(by.id('password-input')).typeText('password');
    await element(by.id('login-button')).tap();
    await expect(element(by.id('home-screen'))).toBeVisible();
  });
});
```

---

## Q91. 🧪 Mocking native modules in tests

Use Jest's mocking capabilities to mock native modules and their methods - isolate tests from external dependencies (test isolation). Mock native modules for testing (module mocking).

- **Trade-offs**: The catch is handle asynchronous operations in mocks (async mocking) - mock platform-specific functionality (platform mocking). Isolate tests from external dependencies (test isolation), but watch out - mock specific methods and return values (method mocking).

Example:

```jsx
jest.mock('react-native-camera', () => ({
  RNCamera: {
    Constants: {
      Type: {
        back: 'back',
        front: 'front'
      }
    }
  }
}));
```

---

## Q92. ⚡ Testing asynchronous behavior in React Native

Use async/await, promises, and Jest's async testing utilities to test asynchronous code - test error cases in async code (error handling). Use async/await for asynchronous tests (async testing).

- **Trade-offs**: The catch is mock async functions and network requests (mocking) - use waitFor for async operations (wait for). Test error cases in async code (error handling), but watch out - handle promises in tests (promise testing).

Example:

```jsx
test('fetches user data', async () => {
  const mockUser = { id: 1, name: 'John Doe' };

  global.fetch = jest.fn().mockResolvedValue({
    ok: true,
    json: async () => mockUser
  });

  const user = await fetchUser(1);
  expect(user).toEqual(mockUser);
});
```

---

## Q93. 🧪 Simulating gestures in tests

Use gesture simulation methods provided by testing frameworks to test touch interactions - test multi-touch interactions (multi-touch). Simulate touch gestures in tests (gesture simulation).

- **Trade-offs**: The catch is test long press interactions (long press) - test pinch and zoom interactions (pinch gestures). Test multi-touch interactions (multi-touch), but watch out - test swipe interactions (swipe gestures).

Example:

```jsx
describe('Gesture Tests', () => {
  it('should handle swipe gesture', async () => {
    await element(by.id('swipeable-item')).swipe('left');
    await expect(element(by.id('delete-button'))).toBeVisible();
  });
});
```

---

## Q94. ⚡ Monitoring app performance and crashes

Integrate crash reporting tools to monitor and analyze app crashes in production - track crashes by app version (release tracking). Monitor app crashes and errors (crash reporting).

- **Trade-offs**: The catch is monitor app performance (performance monitoring) - add user context to crash reports (user context). Track crashes by app version (release tracking), but watch out - track errors and exceptions (error tracking).

Example:

```jsx
import Sentry from '@sentry/react-native';

Sentry.init({
  dsn: 'your-sentry-dsn',
  environment: 'production',
  tracesSampleRate: 1.0
});

```

---

---

## 📍 Navigation

<div align="center">

[Hardware & System APIs](08%29%20Hardware%20%26%20System%20APIs.md) • [Home: README](../README.md) • [Build & Release Management →](10%29%20Build%20%26%20Release%20Management.md)

[📋 Cheatsheet](React%20Native%20Interview%20Cheatsheet.md)

</div>

---
