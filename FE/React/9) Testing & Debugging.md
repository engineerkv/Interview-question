# 🧪 9. Testing & Debugging (Q81–90)

---

## 81) What are the main testing types in React (unit, integration, end-to-end)?

Concept:
Unit tests test individual components, integration tests test component interactions, and E2E tests test complete user workflows.

Example:
```jsx
// Unit Test - testing individual component
import { render, screen } from '@testing-library/react';
import Button from './Button';

test('renders button with text', () => {
  render(<Button>Click me</Button>);
  expect(screen.getByText('Click me')).toBeInTheDocument();
});
```

Deep Insight:
- **Unit Tests**: Test individual components in isolation
- **Integration Tests**: Test how components work together
- **E2E Tests**: Test complete user workflows from start to finish
- **Testing Pyramid**: More unit tests, fewer integration tests, even fewer E2E tests
- **Tools**: Jest for unit/integration, Cypress/Playwright for E2E

---

## 92) What is Jest and how is it used for React testing?

Concept:
Jest is a JavaScript testing framework that provides test runners, assertions, mocking, and code coverage for React applications.

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

Deep Insight:
- **Test Runner**: Runs tests and provides feedback
- **Assertions**: Built-in assertion library for testing
- **Mocking**: Mock functions, modules, and timers
- **Code Coverage**: Measure how much code is tested
- **Configuration**: Highly configurable for different projects

---

## 92) What is React Testing Library and what problem does it solve compared to Enzyme?

Concept:
React Testing Library focuses on testing user behavior rather than implementation details, providing better testing practices and maintainability.

Example:
```jsx
// React Testing Library - testing user behavior
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

Deep Insight:
- **User-centric**: Tests what users see and do
- **Accessibility**: Encourages accessible component design
- **Maintainable**: Less brittle tests that don't break with refactoring
- **Best Practices**: Follows testing best practices and principles
- **Modern**: Built for modern React with hooks and functional components

---

## 92) How do you test React Hooks using Jest and React Testing Library?

Concept:
Use renderHook from React Testing Library to test custom hooks, or test hooks indirectly through component testing.

Example:
```jsx
import { renderHook, act } from '@testing-library/react';
import { useCounter } from './useCounter';

// Testing custom hook directly
test('useCounter hook', () => {
  const { result } = renderHook(() => useCounter(0));
  
  expect(result.current.count).toBe(0);
  
  act(() => {
    result.current.increment();
  });
  
  expect(result.current.count).toBe(1);
});
```

Deep Insight:
- **renderHook**: Test custom hooks in isolation
- **act**: Wrap state updates in act() for proper testing
- **Component Testing**: Test hooks through components they're used in
- **Mocking**: Mock dependencies and external functions
- **Async Hooks**: Handle async operations in hooks properly

---

## 92) How do you mock API calls in tests?

Concept:
Mock API calls using Jest mocks, MSW (Mock Service Worker), or mock implementations to isolate components from external dependencies.

Example:
```jsx
// Jest fetch mock
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

Deep Insight:
- **Jest Mocks**: Simple mocking for fetch and functions
- **MSW**: More realistic API mocking with actual HTTP requests
- **Mock Implementations**: Replace entire modules with mock versions
- **Isolation**: Isolate components from external dependencies
- **Realistic Testing**: Use realistic mock data and responses

---

## 92) How do you test form input changes and button clicks?

Concept:
Use fireEvent or userEvent from React Testing Library to simulate user interactions and test form behavior.

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

Deep Insight:
- **userEvent**: More realistic user interactions than fireEvent
- **Form Testing**: Test input changes, validation, and submission
- **Accessibility**: Use accessible queries like getByLabelText
- **Async Operations**: Handle async form submissions properly
- **Validation**: Test both valid and invalid form inputs

---

## 92) How do you test asynchronous behavior (Promises, React Query) in components?

Concept:
Use waitFor, findBy queries, or act() to handle asynchronous operations and test loading states and data fetching.

Example:
```jsx
import { render, screen, waitFor } from '@testing-library/react';
import { QueryClient, QueryClientProvider } from 'react-query';

// Test async data fetching
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

Deep Insight:
- **waitFor**: Wait for async operations to complete
- **findBy Queries**: Wait for elements to appear
- **act**: Wrap state updates in act() for proper testing
- **Mocking**: Mock async functions and API calls
- **Error Handling**: Test both success and error states

---

## 92) What are snapshot tests in Jest and how are they used?

Concept:
Snapshot tests capture component output and compare it to stored snapshots, useful for detecting unintended changes.

Example:
```jsx
import { render } from '@testing-library/react';
import Button from './Button';

test('button renders correctly', () => {
  const { container } = render(<Button>Click me</Button>);
  expect(container.firstChild).toMatchSnapshot();
});
```

Deep Insight:
- **Change Detection**: Automatically detect unintended changes
- **Regression Testing**: Prevent regressions in component output
- **Maintenance**: Easy to update snapshots when changes are intentional
- **Use Cases**: Good for UI components with stable output
- **Limitations**: Can be brittle and hard to maintain

---

## 92) How do you debug React applications in VS Code and browser dev tools?

Concept:
Use React DevTools, VS Code debugger, console logging, and breakpoints to debug React applications effectively.

Example:
```jsx
// Console logging for debugging
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

Deep Insight:
- **React DevTools**: Browser extension for debugging React components
- **VS Code Debugger**: Debug React apps directly in VS Code
- **Console Logging**: Use console.log, console.error for debugging
- **Breakpoints**: Set breakpoints in VS Code or browser dev tools
- **State Inspection**: Inspect component state and props

---

## 92) How do you use the React DevTools Profiler for debugging performance issues?

Concept:
Use the Profiler tab to record component renders, analyze performance, and identify optimization opportunities.

Example:
```jsx
// Profiler component
import { Profiler } from 'react';

function onRenderCallback(id, phase, actualDuration, baseDuration, startTime, commitTime) {
  console.log('Profiler:', {
    id,
    phase,
    actualDuration,
    baseDuration
  });
}

function App() {
  return (
    <Profiler id="App" onRender={onRenderCallback}>
      <MyComponent />
    </Profiler>
  );
}
```

Deep Insight:
- **Profiler Tab**: Record and analyze component performance
- **Render Times**: See how long components take to render
- **Re-render Analysis**: Identify unnecessary re-renders
- **Optimization**: Find components that need optimization
- **Production**: Can be used in production for monitoring

---
