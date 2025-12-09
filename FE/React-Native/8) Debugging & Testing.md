# 8. Debugging & Testing (Q69–78)

---

## 📍 Navigation

<div align="center">

[CodePush & OTA Updates](7%29%20CodePush%20%26%20OTA%20Updates.md) • [Home: README](../README.md) • [Build, Deployment & Stores →](9%29%20Build%2C%20Deployment%20%26%20Stores.md)

[📋 Cheatsheet](React%20Native%20Interview%20Cheatsheet.md]

</div>

---

---

## Q69. 🐛 Debugging React Native apps

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

## Q70. 🐛 Using Flipper for React Native debugging

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

## Q71. 🐛 Debugging with Chrome DevTools

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

## Q72. 💡 Creating custom Flipper plugins

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

## Q73. 🧪 Writing unit tests with Jest

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

## Q74. 🧪 Implementing end-to-end testing with Detox

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

## Q75. 🧪 Mocking native modules in tests

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

## Q76. ⚡ Testing asynchronous behavior in React Native

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

## Q77. 🧪 Simulating gestures in tests

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

## Q78. ⚡ Monitoring app performance and crashes

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

[CodePush & OTA Updates](7%29%20CodePush%20%26%20OTA%20Updates.md) • [Home: README](../README.md) • [Build, Deployment & Stores →](9%29%20Build%2C%20Deployment%20%26%20Stores.md)

[📋 Cheatsheet](React%20Native%20Interview%20Cheatsheet.md]

</div>

---
