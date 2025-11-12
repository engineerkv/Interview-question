# 🧪 9. Testing & Debugging (Q81–90)

---

## 🧩 Q81. What are the different types of testing in React?

### 🧠 Concept

Unit tests test individual components. Integration tests test component interactions. E2E tests test complete user workflows. The testing pyramid balances speed, coverage, and confidence.

---

### 💡 Example

```jsx
import { render, screen } from '@testing-library/react';
import Button from './Button';

test('renders button with text', () => {
  render(<Button>Click me</Button>);
  expect(screen.getByText('Click me')).toBeInTheDocument();
});
```

---

### 🔍 Deep Insights

* **Rule:** Unit tests test individual components in isolation, most common and fastest.
* **Use Case:** Integration tests test how components work together, fewer but more valuable.
* **Common Mistake:** E2E tests test complete user workflows, fewest but most realistic.
* **Pro Tip:** More unit tests, fewer integration tests, even fewer E2E tests.

---

### ⭐ Senior Takeaway

The testing pyramid balances speed, coverage, and confidence.

---

## 🧩 Q82. How do you test React components with Jest?

### 🧠 Concept

Jest is a JavaScript testing framework providing test runners, assertions, mocking, and code coverage for React. It's the foundation, React Testing Library is the testing approach.

---

### 💡 Example

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

### 🔍 Deep Insights

* **Rule:** Test runner with built-in assertions, mocking, and coverage.
* **Use Case:** Standard testing framework for React apps, works with React Testing Library.
* **Common Mistake:** Features: mock functions, modules, timers, and measure code coverage.
* **Pro Tip:** Highly configurable for different projects and environments.

---

### ⭐ Senior Takeaway

Jest is the foundation, React Testing Library is the testing approach.

---

## 🧩 Q83. What is React Testing Library and how do you use it?

### 🧠 Concept

React Testing Library tests user behavior, not implementation details. It's more maintainable than Enzyme and encourages accessible component design.

---

### 💡 Example

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

### 🔍 Deep Insights

* **Rule:** Test what users see and do, not how components work internally.
* **Use Case:** Tests don't break when refactoring, focus on user experience.
* **Common Mistake:** Encourages accessible component design through accessible queries.
* **Pro Tip:** Built for hooks and functional components, Enzyme struggles with hooks.

---

### ⭐ Senior Takeaway

Testing Library tests behavior, Enzyme tests implementation.

---

## 🧩 Q84. How do you test custom hooks?

### 🧠 Concept

Use renderHook to test custom hooks in isolation, or test hooks through components. renderHook is for unit testing hooks, component testing is for integration.

---

### 💡 Example

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

### 🔍 Deep Insights

* **Rule:** renderHook tests custom hooks in isolation without components.
* **Use Case:** Wrap state updates in act() for proper testing of state changes.
* **Common Mistake:** Test hooks through components they're used in.
* **Pro Tip:** Mock dependencies and external functions for isolated testing.

---

### ⭐ Senior Takeaway

renderHook is for unit testing hooks, component testing is for integration.

---

## 🧩 Q85. How do you mock API calls in tests?

### 🧠 Concept

Mock API calls using Jest mocks, MSW (Mock Service Worker), or mock implementations to isolate components. MSW is better for integration tests, Jest mocks for unit tests.

---

### 💡 Example

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

### 🔍 Deep Insights

* **Rule:** Jest mocks are simple mocking for fetch and functions, good for basic cases.
* **Use Case:** MSW is more realistic API mocking with actual HTTP requests, better for complex scenarios.
* **Common Mistake:** Isolate components from external dependencies for reliable tests.
* **Pro Tip:** Use realistic mock data and responses to test edge cases.

---

### ⭐ Senior Takeaway

MSW is better for integration tests, Jest mocks for unit tests.

---

## 🧩 Q86. How do you test form inputs and user interactions?

### 🧠 Concept

Use userEvent from React Testing Library to simulate realistic user interactions. userEvent is preferred over fireEvent for realistic testing.

---

### 💡 Example

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

### 🔍 Deep Insights

* **Rule:** userEvent is more realistic than fireEvent, simulates actual user interactions.
* **Use Case:** Test form validation, submission, and user flows.
* **Common Mistake:** Use accessible queries like getByLabelText to encourage good practices.
* **Pro Tip:** Handle async form submissions properly with waitFor.

---

### ⭐ Senior Takeaway

userEvent is preferred over fireEvent for realistic testing.

---

## 🧩 Q87. How do you test asynchronous behavior in React?

### 🧠 Concept

Use waitFor, findBy queries, or act() to handle async operations and test loading states. Async testing requires waiting for state updates and DOM changes.

---

### 💡 Example

```jsx
import { render, screen, waitFor } from '@testing-library/react';
import { QueryClient, QueryClientProvider } from 'react-query';

test('displays user data after loading', async () => {
  const mockUser = { id: 1, name: 'John Doe' };
  const queryClient = new QueryClient();
  
  render(
    <QueryClientProvider client={queryClient}>
      <UserProfile userId={1} />
    </QueryClientProvider>
  );
  
  await waitFor(() => {
    expect(screen.getByText('John Doe')).toBeInTheDocument();
  });
});
```

---

### 🔍 Deep Insights

* **Rule:** waitFor waits for async operations to complete with timeout.
* **Use Case:** findBy queries wait for elements to appear, automatically wait and retry.
* **Common Mistake:** Wrap state updates in act() for proper async state testing.
* **Pro Tip:** Mock async functions and API calls to control timing.

---

### ⭐ Senior Takeaway

Async testing requires waiting for state updates and DOM changes.

---

## 🧩 Q88. How do you write snapshot tests?

### 🧠 Concept

Snapshot tests capture component output and compare it to stored snapshots. Use them to detect unintended changes, but they shouldn't replace assertion-based tests.

---

### 💡 Example

```jsx
import { render } from '@testing-library/react';
import Button from './Button';

test('button renders correctly', () => {
  const { container } = render(<Button>Click me</Button>);
  expect(container.firstChild).toMatchSnapshot();
});
```

---

### 🔍 Deep Insights

* **Rule:** Detect unintended changes in component output automatically.
* **Use Case:** Good for UI components with stable output, regression testing.
* **Common Mistake:** Easy to update snapshots when changes are intentional.
* **Pro Tip:** Can be brittle and hard to maintain, not ideal for frequently changing UI.

---

### ⭐ Senior Takeaway

Snapshots are useful but shouldn't replace assertion-based tests.

---

## 🧩 Q89. How do you debug React applications?

### 🧠 Concept

Use React DevTools, VS Code debugger, console logging, and breakpoints to debug React apps. React DevTools is essential for debugging React component trees.

---

### 💡 Example

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

### 🔍 Deep Insights

* **Rule:** React DevTools browser extension inspects components, state, and props.
* **Use Case:** VS Code debugger debugs React apps directly in VS Code with breakpoints.
* **Common Mistake:** Use console.log, console.error for quick debugging.
* **Pro Tip:** Set breakpoints in VS Code or browser dev tools for step-through debugging.

---

### ⭐ Senior Takeaway

React DevTools is essential for debugging React component trees.

---

## 🧩 Q90. What are the best practices for React testing?

### 🧠 Concept

Best practices include testing user behavior not implementation, using accessible queries, mocking external dependencies, handling async properly, and maintaining test readability.

---

### 💡 Example

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

### 🔍 Deep Insights

* **Rule:** Test what users see and do, not how components work internally.
* **Use Case:** Use accessible queries to encourage good accessibility practices.
* **Common Mistake:** Mock external dependencies to isolate components.
* **Pro Tip:** Handle async operations properly with waitFor and findBy queries.

---

### ⭐ Senior Takeaway

Test behavior, not implementation—focus on user experience.

---
