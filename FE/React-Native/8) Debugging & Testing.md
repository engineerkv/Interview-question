# 🧰 8. Debugging & Testing (Q69–78)

---

## 69) How do you debug a React Native app using **Flipper** or **Chrome DevTools**?

Use Flipper for native debugging and Chrome DevTools for JavaScript debugging.

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

- **Core Tools**: Flipper (comprehensive debugging platform for React Native), Chrome DevTools (JavaScript debugging and profiling)
- **Real-World Use**: Debug network requests and responses (network debugging)
- **Common Practice**: Profile app performance and memory usage (performance)
- **Advanced Feature**: Works on both iOS and Android (platform support)
- **Interview Tip**: Explain that use Flipper for native debugging, Chrome for JS

---

## 70) What is **remote debugging**, and when should you avoid it?

Remote debugging runs JavaScript on Chrome, useful for debugging but can cause performance issues and should be avoided in production.

```jsx
// Remote debugging setup
// Enable in development only
if (__DEV__) {
  // Enable remote debugging
  // This runs JavaScript on Chrome
  // Good for debugging but affects performance
}
```

- **Core Limitation**: Use only in development (development only)
- **Real-World Impact**: Can cause performance issues (performance impact)
- **Common Problem**: May behave differently than production (different behavior)
- **Advanced Issue**: Can cause memory leaks (memory issues)
- **Interview Tip**: Explain that never use in production

---

## 71) What is **Flipper**, and what plugins does it provide for React Native debugging?

Flipper is a debugging platform that provides plugins for network inspection, layout debugging, and performance monitoring.

```jsx
import { Flipper } from 'react-native-flipper';

Flipper.addPlugin({
  getId: () => 'Network',
  onConnect: () => {}
});
```

- **Core Plugins**: Network plugin (debug network requests and responses), Layout plugin (debug UI layout and styling), Performance plugin (monitor app performance)
- **Real-World Use**: Crash plugin (debug crashes and errors)
- **Advanced Feature**: Create custom debugging plugins (custom plugins)
- **Common Benefit**: Comprehensive debugging capabilities
- **Interview Tip**: Explain that Flipper is essential for React Native debugging

---

## 72) How do you test React Native components using **Jest**?

Use Jest with React Native Testing Library to test components, hooks, and user interactions.

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

- **Core Framework**: Jest (JavaScript testing framework)
- **Real-World Use**: React Native Testing Library (testing utilities for React Native)
- **Common Practice**: Test component rendering and behavior (component testing)
- **Advanced Feature**: Test user interactions and events (user interactions)
- **Interview Tip**: Explain that handle asynchronous operations in tests (async testing)

---

## 73) How do you perform **end-to-end (E2E)** tests using **Detox**?

Use Detox to write and run E2E tests that interact with the app like a real user.

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

- **Core Purpose**: Test complete user workflows (E2E testing)
- **Real-World Use**: Test on real devices (real device testing)
- **Common Practice**: Simulate real user interactions (user interactions)
- **Advanced Feature**: Test on both iOS and Android (cross-platform)
- **Interview Tip**: Explain that integrate with CI/CD pipelines

---

## 74) How do you mock native modules in Jest?

Use Jest's mocking capabilities to mock native modules and their methods.

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

- **Core Technique**: Mock native modules for testing (module mocking)
- **Real-World Use**: Mock specific methods and return values (method mocking)
- **Common Practice**: Handle asynchronous operations in mocks (async mocking)
- **Advanced Feature**: Mock platform-specific functionality (platform mocking)
- **Interview Tip**: Explain that isolate tests from external dependencies (test isolation)

---

## 75) How do you test asynchronous native functions or network requests?

Use async/await, promises, and Jest's async testing utilities to test asynchronous code.

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

- **Core Approach**: Use async/await for asynchronous tests (async testing)
- **Real-World Use**: Handle promises in tests (promise testing)
- **Common Practice**: Mock async functions and network requests (mocking)
- **Advanced Feature**: Use waitFor for async operations (wait for)
- **Interview Tip**: Explain that test error cases in async code (error handling)

---

## 76) How do you simulate gestures in E2E tests (Detox, Appium)?

Use gesture simulation methods provided by testing frameworks to test touch interactions.

```jsx
describe('Gesture Tests', () => {
  it('should handle swipe gesture', async () => {
    await element(by.id('swipeable-item')).swipe('left');
    await expect(element(by.id('delete-button'))).toBeVisible();
  });
});
```

- **Core Feature**: Simulate touch gestures in tests (gesture simulation)
- **Real-World Use**: Test swipe interactions (swipe gestures)
- **Common Practice**: Test long press interactions (long press)
- **Advanced Feature**: Test pinch and zoom interactions (pinch gestures)
- **Interview Tip**: Explain that test multi-touch interactions (multi-touch)

---

## 77) What are common test performance pitfalls to watch for?

Avoid slow tests, memory leaks, and inefficient test setup that can impact test performance.

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

- **Common Pitfalls**: Avoid unnecessary waits and timeouts (slow tests)
- **Real-World Issue**: Clean up resources in tests (memory leaks)
- **Common Mistake**: Mock heavy dependencies (heavy dependencies)
- **Advanced Practice**: Mock network requests (network requests)
- **Interview Tip**: Explain that keep tests isolated and independent (test isolation)

---

## 78) How do you monitor app crashes using **Crashlytics** or **Sentry**?

Integrate crash reporting tools to monitor and analyze app crashes in production.

```jsx
import Sentry from '@sentry/react-native';

Sentry.init({
  dsn: 'your-sentry-dsn',
  environment: 'production',
  tracesSampleRate: 1.0
});
```

- **Core Purpose**: Monitor app crashes and errors (crash reporting)
- **Real-World Use**: Track errors and exceptions (error tracking)
- **Common Practice**: Monitor app performance (performance monitoring)
- **Advanced Feature**: Add user context to crash reports (user context)
- **Interview Tip**: Explain that track crashes by app version (release tracking)

---
