# 🧪 7. Testing & Debugging (Q77–102)

---

## 📍 Navigation

<div align="center">

[← Previous: Performance Optimization](6%29%20Performance%20Optimization.md) • [Home: README](../README.md) • [Next: Architecture & Best Practices →](8%29%20Architecture%20%26%20Best%20Practices.md)

[📋 Cheatsheet](React%20Interview%20Cheatsheet.md)

</div>

---

---

## Q77. 🧪 Types of testing in React

Unit tests test individual components, integration tests test component interactions, and E2E tests test complete user workflows - the testing pyramid balances speed, coverage, and confidence. Unit tests test individual components in isolation, most common and fastest.

- **Trade-offs**: The catch is E2E tests test complete user workflows, fewest but most realistic - more unit tests, fewer integration tests, even fewer E2E tests. The testing pyramid balances speed, coverage, and confidence, but watch out - integration tests test how components work together, fewer but more valuable.

Example:

```jsx
import { render, screen } from '@testing-library/react';
import Button from './Button';

test('renders button with text', () => {
  render(<Button>Click me</Button>);
  expect(screen.getByText('Click me')).toBeInTheDocument();
});

```

## Q78. 🧩 Testing React components with Jest

Jest is a JavaScript testing framework providing test runners, assertions, mocking, and code coverage for React - it's the foundation, React Testing Library is the testing approach. Test runner with built-in assertions, mocking, and coverage.

- **Trade-offs**: The catch is features: mock functions, modules, timers, and measure code coverage - highly configurable for different projects and environments. Jest is the foundation, React Testing Library is the testing approach, but watch out - standard testing framework for React apps, works with React Testing Library.

Example:

```jsx
// Jest configuration
module.exports = {
  testEnvironment: 'jsdom',
  setupFilesAfterEnv: ['<rootDir>/src/setupTests.js'],
  moduleNameMapping: {
    '\\.(css|less|scss)$': 'identity-obj-proxy'
  }
};

```

---

## Q79. 🧪 React Testing Library and how to use it

React Testing Library tests user behavior, not implementation details - it's more maintainable than Enzyme and encourages accessible component design. Test what users see and do, not how components work internally.

- **Trade-offs**: The catch is encourages accessible component design through accessible queries - built for hooks and functional components, Enzyme struggles with hooks. Testing Library tests behavior, Enzyme tests implementation, but watch out - tests don't break when refactoring, focus on user experience.

Example:

```jsx
import { render, screen, fireEvent } from '@testing-library/react';
import userEvent from '@testing-library/user-event';

test('user can submit form', async () => {
  const user = userEvent.setup();
  render(<ContactForm />);

  await user.type(screen.getByLabelText(/name/i), 'John');
  await user.click(screen.getByRole('button', { name: /submit/i }));

  expect(screen.getByText('Form submitted!')).toBeInTheDocument();
});

```

---

## Q80. 🪝 Testing custom hooks

Use renderHook to test custom hooks in isolation, or test hooks through components - renderHook is for unit testing hooks, component testing is for integration. renderHook tests custom hooks in isolation without components.

- **Trade-offs**: The catch is test hooks through components they're used in - mock dependencies and external functions for isolated testing. renderHook is for unit testing hooks, component testing is for integration, but watch out - wrap state updates in act() for proper testing of state changes.

Example:

```jsx
import { renderHook, act } from '@testing-library/react';
import { useCounter } from './useCounter';

test('useCounter hook', () => {
  const { result } = renderHook(() => useCounter(0));

  expect(result.current.count).toBe(0);

  act(() => {
    result.current.increment();
  });

  expect(result.current.count).toBe(1);
});

```

---

## Q81. 🧪 Mocking API calls in tests

Mock API calls using Jest mocks, MSW (Mock Service Worker), or mock implementations to isolate components - MSW is better for integration tests, Jest mocks for unit tests. Jest mocks are simple mocking for fetch and functions, good for basic cases.

- **Trade-offs**: The catch is isolate components from external dependencies for reliable tests - use realistic mock data and responses to test edge cases. MSW is better for integration tests, Jest mocks for unit tests, but watch out - MSW is more realistic API mocking with actual HTTP requests, better for complex scenarios.

Example:

```jsx
global.fetch = jest.fn();

test('fetches user data on mount', async () => {
  const mockUser = { id: 1, name: 'John Doe' };
  fetch.mockResolvedValueOnce({
    ok: true,
    json: async () => mockUser
  });

  render(<UserProfile userId={1} />);

  await waitFor(() => {
    expect(screen.getByText('John Doe')).toBeInTheDocument();
  });
});

```

---

## Q82. 🧪 Testing form inputs and user interactions

Use userEvent from React Testing Library to simulate realistic user interactions - userEvent is preferred over fireEvent for realistic testing. userEvent is more realistic than fireEvent, simulates actual user interactions.

- **Trade-offs**: The catch is use accessible queries like getByLabelText to encourage good practices - handle async form submissions properly with waitFor. userEvent is preferred over fireEvent for realistic testing, but watch out - test form validation, submission, and user flows.

Example:

```jsx
import { render, screen } from '@testing-library/react';
import userEvent from '@testing-library/user-event';

test('form input changes update state', async () => {
  const user = userEvent.setup();
  render(<ContactForm />);

  const input = screen.getByLabelText(/email/i);
  await user.type(input, 'test@example.com');

  expect(input).toHaveValue('test@example.com');
});

```

---

## Q83. ⚡ Testing asynchronous behavior in React

Use waitFor, findBy queries, or act() to handle async operations and test loading states - async testing requires waiting for state updates and DOM changes. waitFor waits for async operations to complete with timeout.

- **Trade-offs**: The catch is wrap state updates in act() for proper async state testing - mock async functions and API calls to control timing. Async testing requires waiting for state updates and DOM changes, but watch out - findBy queries wait for elements to appear, automatically wait and retry.

Example:

```jsx
import { render, screen, waitFor } from '@testing-library/react';
import { useState, useEffect } from 'react';

// Simple component with async data fetching
function UserProfile({ userId }) {
  const [user, setUser] = useState(null);

  useEffect(() => {
    fetch(`/api/users/${userId}`)
      .then(r => r.json())
      .then(setUser);
  }, [userId]);

  return <div>{user ? user.name : 'Loading...'}</div>;
}

// Simple test with waitFor
test('displays user after loading', async () => {
  global.fetch = jest.fn(() =>
    Promise.resolve({
      json: () => Promise.resolve({ name: 'John Doe' })
    })
  );

  render(<UserProfile userId={1} />);

  await waitFor(() => {
    expect(screen.getByText('John Doe')).toBeInTheDocument();
  });
});

// Simple test with findBy (automatically waits)
test('finds user with findBy', async () => {
  global.fetch = jest.fn(() =>
    Promise.resolve({
      json: () => Promise.resolve({ name: 'Jane Smith' })
    })
  );

  render(<UserProfile userId={1} />);

  const userName = await screen.findByText('Jane Smith');
  expect(userName).toBeInTheDocument();
});

```

---

## Q84. 🧪 Writing snapshot tests

Snapshot tests capture component output and compare it to stored snapshots - use them to detect unintended changes, but they shouldn't replace assertion-based tests. Detect unintended changes in component output automatically.

- **Trade-offs**: The catch is easy to update snapshots when changes are intentional - can be brittle and hard to maintain, not ideal for frequently changing UI. Snapshots are useful but shouldn't replace assertion-based tests, but watch out - good for UI components with stable output, regression testing.

Example:

```jsx
import { render } from '@testing-library/react';
import Button from './Button';

test('button renders correctly', () => {
  const { container } = render(<Button>Click me</Button>);
  expect(container.firstChild).toMatchSnapshot();
});

```

---

## Q85. 🐛 Debugging React applications

Use React DevTools, VS Code debugger, console logging, and breakpoints to debug React apps - React DevTools is essential for debugging React component trees. React DevTools browser extension inspects components, state, and props.

- **Trade-offs**: The catch is use console.log, console.error for quick debugging - set breakpoints in VS Code or browser dev tools for step-through debugging. React DevTools is essential for debugging React component trees, but watch out - VS Code debugger debugs React apps directly in VS Code with breakpoints.

Example:

```jsx
function UserProfile({ userId }) {
  const [user, setUser] = useState(null);

  useEffect(() => {
    console.log('Fetching user:', userId);
    fetch(`/api/users/${userId}`)
      .then(r => r.json())
      .then(setUser)
      .catch(err => console.error('Error:', err));
  }, [userId]);

  return <div>{user ? user.name : 'Loading...'}</div>;
}

```

---

## Q86. 🧪 Best practices for React testing

Best practices include testing user behavior not implementation, using accessible queries, mocking external dependencies, handling async properly, and maintaining test readability. Test what users see and do, not how components work internally.

- **Trade-offs**: The catch is mock external dependencies to isolate components - handle async operations properly with waitFor and findBy queries. Test behavior, not implementation, focus on user experience, but watch out - use accessible queries to encourage good accessibility practices.

Example:

```jsx
test('user can complete form flow', async () => {
  const user = userEvent.setup();
  render(<ContactForm />);

  await user.type(screen.getByLabelText(/name/i), 'John');
  await user.click(screen.getByRole('button', { name: /submit/i }));

  expect(await screen.findByText('Success!')).toBeInTheDocument();
});

```

---

---

## 📍 Navigation

<div align="center">

[6) Performance Optimization.md](6%29%20Performance%20Optimization.md) • [Home: README](../README.md) • [8) Architecture & Best Practices.md →](8%29%20Architecture%20&%20Best%20Practices.md)

[📋 Cheatsheet](React%20Interview%20Cheatsheet.md]

</div>

---
