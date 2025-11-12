# 🧰 8. Debugging & Testing (Q69–78)

---

## 🧩 Q69. How do you debug a React Native app using Flipper or Chrome DevTools?

### 🧠 Concept

Use Flipper for native debugging and Chrome DevTools for JavaScript debugging. Use Flipper for native debugging, Chrome for JS.

---

### 💡 Example

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

### 🔍 Deep Insights

* **Rule:** Flipper (comprehensive debugging platform for React Native), Chrome DevTools (JavaScript debugging and profiling).
* **Use Case:** Debug network requests and responses (network debugging).
* **Common Mistake:** Profile app performance and memory usage (performance).
* **Pro Tip:** Works on both iOS and Android (platform support).

---

### ⭐ Senior Takeaway

Use Flipper for native debugging, Chrome for JS.

---

## 🧩 Q70. What is remote debugging and when should you avoid it?

### 🧠 Concept

Remote debugging runs JavaScript on Chrome, useful for debugging but can cause performance issues and should be avoided in production. Never use in production.

---

### 💡 Example

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

### 🔍 Deep Insights

* **Rule:** Use only in development (development only).
* **Use Case:** Can cause performance issues (performance impact).
* **Common Mistake:** May behave differently than production (different behavior).
* **Pro Tip:** Can cause memory leaks (memory issues).

---

### ⭐ Senior Takeaway

Never use in production.

---

## 🧩 Q71. What is Flipper and what plugins does it provide?

### 🧠 Concept

Flipper is a debugging platform that provides plugins for network inspection, layout debugging, and performance monitoring. Flipper is essential for React Native debugging.

---

### 💡 Example

```jsx
import { Flipper } from 'react-native-flipper';

Flipper.addPlugin({
  getId: () => 'Network',
  onConnect: () => {}
});
```

---

### 🔍 Deep Insights

* **Rule:** Network plugin (debug network requests and responses), Layout plugin (debug UI layout and styling), Performance plugin (monitor app performance).
* **Use Case:** Crash plugin (debug crashes and errors).
* **Common Mistake:** Create custom debugging plugins (custom plugins).
* **Pro Tip:** Comprehensive debugging capabilities.

---

### ⭐ Senior Takeaway

Flipper is essential for React Native debugging.

---

## 🧩 Q72. How do you test React Native components using Jest?

### 🧠 Concept

Use Jest with React Native Testing Library to test components, hooks, and user interactions. Handle asynchronous operations in tests (async testing).

---

### 💡 Example

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

### 🔍 Deep Insights

* **Rule:** Jest (JavaScript testing framework).
* **Use Case:** React Native Testing Library (testing utilities for React Native).
* **Common Mistake:** Test component rendering and behavior (component testing).
* **Pro Tip:** Test user interactions and events (user interactions).

---

### ⭐ Senior Takeaway

Handle asynchronous operations in tests (async testing).

---

## 🧩 Q73. How do you perform end-to-end (E2E) tests using Detox?

### 🧠 Concept

Use Detox to write and run E2E tests that interact with the app like a real user. Integrate with CI/CD pipelines.

---

### 💡 Example

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

### 🔍 Deep Insights

* **Rule:** Test complete user workflows (E2E testing).
* **Use Case:** Test on real devices (real device testing).
* **Common Mistake:** Simulate real user interactions (user interactions).
* **Pro Tip:** Test on both iOS and Android (cross-platform).

---

### ⭐ Senior Takeaway

Integrate with CI/CD pipelines.

---

## 🧩 Q74. How do you mock native modules in Jest?

### 🧠 Concept

Use Jest's mocking capabilities to mock native modules and their methods. Isolate tests from external dependencies (test isolation).

---

### 💡 Example

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

### 🔍 Deep Insights

* **Rule:** Mock native modules for testing (module mocking).
* **Use Case:** Mock specific methods and return values (method mocking).
* **Common Mistake:** Handle asynchronous operations in mocks (async mocking).
* **Pro Tip:** Mock platform-specific functionality (platform mocking).

---

### ⭐ Senior Takeaway

Isolate tests from external dependencies (test isolation).

---

## 🧩 Q75. How do you test asynchronous native functions or network requests?

### 🧠 Concept

Use async/await, promises, and Jest's async testing utilities to test asynchronous code. Test error cases in async code (error handling).

---

### 💡 Example

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

### 🔍 Deep Insights

* **Rule:** Use async/await for asynchronous tests (async testing).
* **Use Case:** Handle promises in tests (promise testing).
* **Common Mistake:** Mock async functions and network requests (mocking).
* **Pro Tip:** Use waitFor for async operations (wait for).

---

### ⭐ Senior Takeaway

Test error cases in async code (error handling).

---

## 🧩 Q76. How do you simulate gestures in E2E tests?

### 🧠 Concept

Use gesture simulation methods provided by testing frameworks to test touch interactions. Test multi-touch interactions (multi-touch).

---

### 💡 Example

```jsx
describe('Gesture Tests', () => {
  it('should handle swipe gesture', async () => {
    await element(by.id('swipeable-item')).swipe('left');
    await expect(element(by.id('delete-button'))).toBeVisible();
  });
});
```

---

### 🔍 Deep Insights

* **Rule:** Simulate touch gestures in tests (gesture simulation).
* **Use Case:** Test swipe interactions (swipe gestures).
* **Common Mistake:** Test long press interactions (long press).
* **Pro Tip:** Test pinch and zoom interactions (pinch gestures).

---

### ⭐ Senior Takeaway

Test multi-touch interactions (multi-touch).

---

## 🧩 Q77. What are common test performance pitfalls to watch for?

### 🧠 Concept

Avoid slow tests, memory leaks, and inefficient test setup that can impact test performance. Keep tests isolated and independent (test isolation).

---

### 💡 Example

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

### 🔍 Deep Insights

* **Rule:** Avoid unnecessary waits and timeouts (slow tests).
* **Use Case:** Clean up resources in tests (memory leaks).
* **Common Mistake:** Mock heavy dependencies (heavy dependencies).
* **Pro Tip:** Mock network requests (network requests).

---

### ⭐ Senior Takeaway

Keep tests isolated and independent (test isolation).

---

## 🧩 Q78. How do you monitor app crashes using Crashlytics or Sentry?

### 🧠 Concept

Integrate crash reporting tools to monitor and analyze app crashes in production. Track crashes by app version (release tracking).

---

### 💡 Example

```jsx
import Sentry from '@sentry/react-native';

Sentry.init({
  dsn: 'your-sentry-dsn',
  environment: 'production',
  tracesSampleRate: 1.0
});
```

---

### 🔍 Deep Insights

* **Rule:** Monitor app crashes and errors (crash reporting).
* **Use Case:** Track errors and exceptions (error tracking).
* **Common Mistake:** Monitor app performance (performance monitoring).
* **Pro Tip:** Add user context to crash reports (user context).

---

### ⭐ Senior Takeaway

Track crashes by app version (release tracking).

---
