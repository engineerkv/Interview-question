# 🧰 8. Debugging & Testing (Q69–78)

---

## 69) How do you debug a React Native app using **Flipper** or **Chrome DevTools**?

Concept:
Use Flipper for native debugging and Chrome DevTools for JavaScript debugging.

Example:
```jsx
// Flipper debugging
import { Flipper } from 'react-native-flipper';

function App() {
  useEffect(() => {
    // Flipper network debugging
```

Deep Insight:
- **Flipper**: Comprehensive debugging platform for React Native
- **Chrome DevTools**: JavaScript debugging and profiling
- **Network Debugging**: Debug network requests and responses
- **Performance**: Profile app performance and memory usage
- **Platform Support**: Works on both iOS and Android

---

## 70) What is **remote debugging**, and when should you avoid it?

Concept:
Remote debugging runs JavaScript on Chrome, useful for debugging but can cause performance issues and should be avoided in production.

Example:
```jsx
// Remote debugging setup
// Enable in development only
if (__DEV__) {
  // Enable remote debugging
  // This runs JavaScript on Chrome
  // Good for debugging but affects performance
```

Deep Insight:
- **Development Only**: Use only in development
- **Performance Impact**: Can cause performance issues
- **Different Behavior**: May behave differently than production
- **Memory Issues**: Can cause memory leaks
- **Production**: Never use in production

---

## 71) What is **Flipper**, and what plugins does it provide for React Native debugging?

Concept:
Flipper is a debugging platform that provides plugins for network inspection, layout debugging, and performance monitoring.

Example:
```jsx
// Flipper plugins
import { Flipper } from 'react-native-flipper';

// Network plugin
Flipper.addPlugin({
  getId() {
```

Deep Insight:
- **Network Plugin**: Debug network requests and responses
- **Layout Plugin**: Debug UI layout and styling
- **Performance Plugin**: Monitor app performance
- **Crash Plugin**: Debug crashes and errors
- **Custom Plugins**: Create custom debugging plugins

---

## 72) How do you test React Native components using **Jest**?

Concept:
Use Jest with React Native Testing Library to test components, hooks, and user interactions.

Example:
```jsx
import React from 'react';
import { render, fireEvent, waitFor } from '@testing-library/react-native';
import MyComponent from '../MyComponent';

describe('MyComponent', () => {
  test('renders correctly', () => {
```

Deep Insight:
- **Jest**: JavaScript testing framework
- **React Native Testing Library**: Testing utilities for React Native
- **Component Testing**: Test component rendering and behavior
- **User Interactions**: Test user interactions and events
- **Async Testing**: Handle asynchronous operations in tests

---

## 73) How do you perform **end-to-end (E2E)** tests using **Detox**?

Concept:
Use Detox to write and run E2E tests that interact with the app like a real user.

Example:
```jsx
// Detox E2E test
describe('Login Flow', () => {
  beforeAll(async () => {
    await device.launchApp();
  });
  
```

Deep Insight:
- **E2E Testing**: Test complete user workflows
- **Real Device Testing**: Test on real devices
- **User Interactions**: Simulate real user interactions
- **Cross-Platform**: Test on both iOS and Android
- **CI/CD Integration**: Integrate with CI/CD pipelines

---

## 74) How do you mock native modules in Jest?

Concept:
Use Jest's mocking capabilities to mock native modules and their methods.

Example:
```jsx
// Mock native module
jest.mock('react-native-camera', () => ({
  RNCamera: {
    Constants: {
      Type: {
        back: 'back',
```

Deep Insight:
- **Module Mocking**: Mock native modules for testing
- **Method Mocking**: Mock specific methods and return values
- **Async Mocking**: Handle asynchronous operations in mocks
- **Platform Mocking**: Mock platform-specific functionality
- **Test Isolation**: Isolate tests from external dependencies

---

## 75) How do you test asynchronous native functions or network requests?

Concept:
Use async/await, promises, and Jest's async testing utilities to test asynchronous code.

Example:
```jsx
// Test async function
test('fetches user data', async () => {
  const mockUser = { id: 1, name: 'John Doe' };
  
  // Mock fetch
  global.fetch = jest.fn().mockResolvedValue({
```

Deep Insight:
- **Async Testing**: Use async/await for asynchronous tests
- **Promise Testing**: Handle promises in tests
- **Mocking**: Mock async functions and network requests
- **Wait For**: Use waitFor for async operations
- **Error Handling**: Test error cases in async code

---

## 76) How do you simulate gestures in E2E tests (Detox, Appium)?

Concept:
Use gesture simulation methods provided by testing frameworks to test touch interactions.

Example:
```jsx
// Detox gesture simulation
describe('Gesture Tests', () => {
  it('should handle swipe gesture', async () => {
    await element(by.id('swipeable-item')).swipe('left');
    await expect(element(by.id('delete-button'))).toBeVisible();
  });
```

Deep Insight:
- **Gesture Simulation**: Simulate touch gestures in tests
- **Swipe Gestures**: Test swipe interactions
- **Long Press**: Test long press interactions
- **Pinch Gestures**: Test pinch and zoom interactions
- **Multi-touch**: Test multi-touch interactions

---

## 77) What are common test performance pitfalls to watch for?

Concept:
Avoid slow tests, memory leaks, and inefficient test setup that can impact test performance.

Example:
```jsx
// ❌ Performance pitfalls
describe('Slow Tests', () => {
  test('slow test with unnecessary waits', async () => {
    // Don't use unnecessary timeouts
    await new Promise(resolve => setTimeout(resolve, 1000));
    
```

Deep Insight:
- **Slow Tests**: Avoid unnecessary waits and timeouts
- **Memory Leaks**: Clean up resources in tests
- **Heavy Dependencies**: Mock heavy dependencies
- **Network Requests**: Mock network requests
- **Test Isolation**: Keep tests isolated and independent

---

## 78) How do you monitor app crashes using **Crashlytics** or **Sentry**?

Concept:
Integrate crash reporting tools to monitor and analyze app crashes in production.

Example:
```jsx
// Sentry integration
import Sentry from '@sentry/react-native';

// Initialize Sentry
Sentry.init({
  dsn: 'your-sentry-dsn',
```

Deep Insight:
- **Crash Reporting**: Monitor app crashes and errors
- **Error Tracking**: Track errors and exceptions
- **Performance Monitoring**: Monitor app performance
- **User Context**: Add user context to crash reports
- **Release Tracking**: Track crashes by app version

---
