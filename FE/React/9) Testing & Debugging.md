# 🧪 9. Testing & Debugging (Q81–90)

---

## 81) What are the main testing types in React (unit, integration, end-to-end)?

Unit tests test individual components. Integration tests test component interactions. E2E tests test complete user workflows.

```jsx
import { render, screen } from '@testing-library/react';
import Button from './Button';

test('renders button with text', () => {
  render(<Button>Click me</Button>);
  expect(screen.getByText('Click me')).toBeInTheDocument();
});
```

- **Unit Tests**: Test individual components in isolation, most common and fastest
- **Integration Tests**: Test how components work together, fewer but more valuable
- **E2E Tests**: Test complete user workflows, fewest but most realistic
- **Testing Pyramid**: More unit tests, fewer integration tests, even fewer E2E tests
- **Interview Tip**: Explain that the testing pyramid balances speed, coverage, and confidence

---

## 82) What is Jest and how is it used for React testing?

Jest is a JavaScript testing framework. It provides test runners, assertions, mocking, and code coverage for React.

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

- **Core Purpose**: Test runner with built-in assertions, mocking, and coverage
- **Real-World Use**: Standard testing framework for React apps, works with React Testing Library
- **Features**: Mock functions, modules, timers, and measure code coverage
- **Configuration**: Highly configurable for different projects and environments
- **Interview Tip**: Explain that Jest is the foundation, React Testing Library is the testing approach

---

## 83) What is React Testing Library and what problem does it solve compared to Enzyme?

React Testing Library tests user behavior, not implementation details. It's more maintainable than Enzyme.

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

- **Core Philosophy**: Test what users see and do, not how components work internally
- **Real-World Benefit**: Tests don't break when refactoring, focus on user experience
- **Accessibility**: Encourages accessible component design through accessible queries
- **Modern React**: Built for hooks and functional components, Enzyme struggles with hooks
- **Interview Tip**: Explain that Testing Library tests behavior, Enzyme tests implementation

---

## 84) How do you test React Hooks using Jest and React Testing Library?

Use renderHook to test custom hooks in isolation, or test hooks through components.

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

- **renderHook**: Test custom hooks in isolation without components
- **act**: Wrap state updates in act() for proper testing of state changes
- **Component Testing**: Test hooks through components they're used in
- **Mocking**: Mock dependencies and external functions for isolated testing
- **Interview Tip**: Explain that renderHook is for unit testing hooks, component testing is for integration

---

## 85) How do you mock API calls in tests?

Mock API calls using Jest mocks, MSW (Mock Service Worker), or mock implementations to isolate components.

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

- **Jest Mocks**: Simple mocking for fetch and functions, good for basic cases
- **MSW**: More realistic API mocking with actual HTTP requests, better for complex scenarios
- **Real-World Use**: Isolate components from external dependencies for reliable tests
- **Mock Data**: Use realistic mock data and responses to test edge cases
- **Interview Tip**: Explain that MSW is better for integration tests, Jest mocks for unit tests

---

## 86) How do you test form input changes and button clicks?

Use userEvent from React Testing Library to simulate realistic user interactions.

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

- **userEvent**: More realistic than fireEvent, simulates actual user interactions
- **Real-World Use**: Test form validation, submission, and user flows
- **Accessibility**: Use accessible queries like getByLabelText to encourage good practices
- **Async Operations**: Handle async form submissions properly with waitFor
- **Interview Tip**: Explain that userEvent is preferred over fireEvent for realistic testing

---

## 87) How do you test asynchronous behavior (Promises, React Query) in components?

Use waitFor, findBy queries, or act() to handle async operations and test loading states.

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

- **waitFor**: Wait for async operations to complete with timeout
- **findBy Queries**: Wait for elements to appear, automatically wait and retry
- **act**: Wrap state updates in act() for proper async state testing
- **Mocking**: Mock async functions and API calls to control timing
- **Interview Tip**: Explain that async testing requires waiting for state updates and DOM changes

---

## 88) What are snapshot tests in Jest and how are they used?

Snapshot tests capture component output and compare it to stored snapshots. Use them to detect unintended changes.

```jsx
import { render } from '@testing-library/react';
import Button from './Button';

test('button renders correctly', () => {
  const { container } = render(<Button>Click me</Button>);
  expect(container.firstChild).toMatchSnapshot();
});
```

- **Core Purpose**: Detect unintended changes in component output automatically
- **Real-World Use**: Good for UI components with stable output, regression testing
- **Maintenance**: Easy to update snapshots when changes are intentional
- **Limitations**: Can be brittle and hard to maintain, not ideal for frequently changing UI
- **Interview Tip**: Explain that snapshots are useful but shouldn't replace assertion-based tests

---

## 89) How do you debug React applications in VS Code and browser dev tools?

Use React DevTools, VS Code debugger, console logging, and breakpoints to debug React apps.

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

- **React DevTools**: Browser extension for inspecting components, state, and props
- **VS Code Debugger**: Debug React apps directly in VS Code with breakpoints
- **Console Logging**: Use console.log, console.error for quick debugging
- **Breakpoints**: Set breakpoints in VS Code or browser dev tools for step-through debugging
- **Interview Tip**: Explain that React DevTools is essential for debugging React component trees

---

## 90) How do you use the React DevTools Profiler for debugging performance issues?

Use the Profiler tab in React DevTools to record renders and analyze performance bottlenecks.

```jsx
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

- **Profiler Tab**: Record and analyze component performance visually
- **Real-World Use**: Identify slow components and unnecessary re-renders
- **Render Times**: See how long components take to render and compare
- **Optimization**: Find components that need memoization or optimization
- **Interview Tip**: Explain that Profiler helps identify performance bottlenecks before optimizing

---
