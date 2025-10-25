# ⚛️ React.js Interview Notes (2025 Edition)

## 🧪 Section 7 — Testing in React — Q137-Q156

---

### 137. 🧪 What are the types of tests used in React apps?

**🧠 Concept**

React apps use different types of tests: unit tests for individual components, integration tests for component interactions, and end-to-end tests for complete user workflows.

**💻 Example**
```jsx
// Unit Test - Testing individual component
import { render, screen } from '@testing-library/react';
import Button from './Button';

test('renders button with text', () => {
  render(<Button>Click me</Button>);
  expect(screen.getByText('Click me')).toBeInTheDocument();
});

// Integration Test - Testing component interactions
test('form submission works', () => {
  render(<LoginForm />);
  fireEvent.change(screen.getByLabelText(/email/i), {
    target: { value: 'test@example.com' }
  });
  fireEvent.click(screen.getByRole('button', { name: /submit/i }));
  expect(mockSubmit).toHaveBeenCalledWith({
    email: 'test@example.com'
  });
});
```

📝 **Deeper Insight**

Testing pyramid in React:
- **Unit Tests** (70%) - Individual components, hooks, utilities
- **Integration Tests** (20%) - Component interactions, API calls
- **E2E Tests** (10%) - Complete user journeys
- **Visual Regression Tests** - UI consistency
- **Performance Tests** - Bundle size, render time

---

### 138. 🧪 What is Jest, and why is it commonly used?

🧠 **Concept**

Jest is a JavaScript testing framework that provides a complete testing solution with built-in assertions, mocking, and test runners for React applications.

💻 **Example**

```jsx
// Jest configuration
module.exports = {
  testEnvironment: 'jsdom',
  setupFilesAfterEnv: ['<rootDir>/src/setupTests.js'],
  moduleNameMapping: {
    '\\.(css|less|scss)$': 'identity-obj-proxy'
  }
};

// Jest test example
describe('UserProfile', () => {
  beforeEach(() => {
    jest.clearAllMocks();
  });

  test('displays user information', () => {
    const mockUser = { name: 'John', email: 'john@example.com' };
    render(<UserProfile user={mockUser} />);
    
    expect(screen.getByText('John')).toBeInTheDocument();
    expect(screen.getByText('john@example.com')).toBeInTheDocument();
  });
});
```

📝 **Deeper Insight**

Jest advantages:
- **Zero configuration** - Works out of the box
- **Built-in mocking** - Functions, modules, timers
- **Snapshot testing** - UI regression detection
- **Code coverage** - Built-in coverage reports
- **Parallel execution** - Fast test runs
- **Watch mode** - Automatic re-running

---

### 139. 🧪 What is React Testing Library (RTL), and how does it differ from Enzyme?

🧠 **Concept**

React Testing Library is a testing utility that encourages testing components the way users interact with them, focusing on behavior rather than implementation details.

💻 **Example**

```jsx
// React Testing Library approach
import { render, screen, fireEvent } from '@testing-library/react';
import userEvent from '@testing-library/user-event';

test('user can submit form', async () => {
  const user = userEvent.setup();
  render(<ContactForm />);
  
  await user.type(screen.getByLabelText(/name/i), 'John Doe');
  await user.type(screen.getByLabelText(/email/i), 'john@example.com');
  await user.click(screen.getByRole('button', { name: /submit/i }));
  
  expect(screen.getByText(/thank you/i)).toBeInTheDocument();
});

// Enzyme approach (older)
import { shallow } from 'enzyme';

test('component renders correctly', () => {
  const wrapper = shallow(<MyComponent />);
  expect(wrapper.find('.button').length).toBe(1);
});
```

📝 **Deeper Insight**

RTL vs Enzyme:
- **RTL Philosophy** - Test behavior, not implementation
- **Enzyme Philosophy** - Test component internals
- **RTL Benefits** - More maintainable, user-focused
- **Enzyme Benefits** - More control over component state
- **RTL Queries** - getByRole, getByLabelText, getByText
- **Enzyme Queries** - find(), hasClass(), state()

---

### 140. 🧪 How do you test components with props and state?

🧠 **Concept**

Testing components with props involves rendering with different prop values, while state testing requires simulating user interactions that trigger state changes.

💻 **Example**

```jsx
// Testing props
test('renders with different props', () => {
  const { rerender } = render(<Counter initialCount={0} />);
  expect(screen.getByText('0')).toBeInTheDocument();
  
  rerender(<Counter initialCount={5} />);
  expect(screen.getByText('5')).toBeInTheDocument();
});

// Testing state changes
test('increments counter on button click', () => {
  render(<Counter />);
  
  const button = screen.getByRole('button', { name: /increment/i });
  expect(screen.getByText('0')).toBeInTheDocument();
  
  fireEvent.click(button);
  expect(screen.getByText('1')).toBeInTheDocument();
  
  fireEvent.click(button);
  expect(screen.getByText('2')).toBeInTheDocument();
});

// Testing conditional rendering based on state
test('shows loading state', () => {
  render(<DataComponent isLoading={true} />);
  expect(screen.getByText(/loading/i)).toBeInTheDocument();
  expect(screen.queryByText(/data/i)).not.toBeInTheDocument();
});
```

📝 **Deeper Insight**

Testing strategies:
- **Props Testing** - Different prop combinations
- **State Testing** - User interactions, async updates
- **Conditional Rendering** - Different states
- **Error Boundaries** - Error state handling
- **Controlled vs Uncontrolled** - Form input testing
- **Custom Hooks** - State logic isolation

---

### 141. 🧪 How do you test custom hooks?

🧠 **Concept**

Custom hooks are tested using `@testing-library/react-hooks` or `renderHook` to isolate hook logic and test different scenarios without component dependencies.

💻 **Example**

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
  
  act(() => {
    result.current.decrement();
  });
  
  expect(result.current.count).toBe(0);
});

// Testing async hooks
test('useFetch hook', async () => {
  const mockFetch = jest.fn().mockResolvedValue({
    json: () => Promise.resolve({ data: 'test' })
  });
  global.fetch = mockFetch;
  
  const { result } = renderHook(() => useFetch('/api/data'));
  
  expect(result.current.loading).toBe(true);
  
  await act(async () => {
    await result.current.refetch();
  });
  
  expect(result.current.data).toEqual({ data: 'test' });
  expect(result.current.loading).toBe(false);
});
```

📝 **Deeper Insight**

Hook testing patterns:
- **renderHook** - Isolate hook logic
- **act()** - Wrap state updates
- **Async testing** - Wait for promises
- **Mock dependencies** - External APIs, context
- **Error scenarios** - Exception handling
- **Cleanup** - useEffect cleanup functions

---

### 142. 🧪 How do you mock API requests in Jest?

🧠 **Concept**

API mocking in Jest involves intercepting fetch calls or axios requests to return predictable responses for testing different scenarios.

💻 **Example**

```jsx
// Mocking fetch
global.fetch = jest.fn();

test('fetches user data', async () => {
  const mockUser = { id: 1, name: 'John' };
  fetch.mockResolvedValueOnce({
    ok: true,
    json: async () => mockUser
  });
  
  render(<UserProfile userId={1} />);
  
  await waitFor(() => {
    expect(screen.getByText('John')).toBeInTheDocument();
  });
  
  expect(fetch).toHaveBeenCalledWith('/api/users/1');
});

// Mocking axios
import axios from 'axios';
jest.mock('axios');

test('handles API error', async () => {
  axios.get.mockRejectedValueOnce(new Error('API Error'));
  
  render(<DataComponent />);
  
  await waitFor(() => {
    expect(screen.getByText(/error/i)).toBeInTheDocument();
  });
});

// Mocking with MSW (Mock Service Worker)
import { rest } from 'msw';
import { setupServer } from 'msw/node';

const server = setupServer(
  rest.get('/api/users', (req, res, ctx) => {
    return res(ctx.json({ users: [] }));
  })
);
```

📝 **Deeper Insight**

API mocking strategies:
- **Jest mocks** - Simple fetch/axios mocking
- **MSW (Mock Service Worker)** - Network-level mocking
- **Mock data** - Consistent test data
- **Error scenarios** - Network failures, timeouts
- **Loading states** - Async behavior testing
- **Cache testing** - Response caching

---

### 143. 🧪 What is snapshot testing?

🧠 **Concept**

Snapshot testing captures the rendered output of a component and compares it against a stored snapshot to detect unexpected changes in UI.

💻 **Example**

```jsx
import { render } from '@testing-library/react';
import Button from './Button';

test('Button component snapshot', () => {
  const { container } = render(<Button>Click me</Button>);
  expect(container.firstChild).toMatchSnapshot();
});

// Testing with different props
test('Button variants snapshot', () => {
  const { container: primary } = render(<Button variant="primary">Primary</Button>);
  const { container: secondary } = render(<Button variant="secondary">Secondary</Button>);
  
  expect(primary.firstChild).toMatchSnapshot('primary-button');
  expect(secondary.firstChild).toMatchSnapshot('secondary-button');
});

// Updating snapshots
// npm test -- --updateSnapshot
```

📝 **Deeper Insight**

Snapshot testing considerations:
- **When to use** - UI regression detection
- **When to avoid** - Frequently changing components
- **Maintenance** - Regular snapshot updates
- **False positives** - Timestamps, random IDs
- **Best practices** - Small, focused snapshots
- **CI/CD** - Automated snapshot updates

---

### 144. 🧪 What is the difference between integration and unit tests?

🧠 **Concept**

Unit tests isolate individual components or functions, while integration tests verify how multiple components work together in realistic scenarios.

💻 **Example**

```jsx
// Unit Test - Testing individual component
test('Button component unit test', () => {
  render(<Button onClick={mockClick}>Click</Button>);
  fireEvent.click(screen.getByRole('button'));
  expect(mockClick).toHaveBeenCalledTimes(1);
});

// Integration Test - Testing component interactions
test('Login form integration', () => {
  render(
    <AuthProvider>
      <LoginForm />
    </AuthProvider>
  );
  
  fireEvent.change(screen.getByLabelText(/email/i), {
    target: { value: 'test@example.com' }
  });
  fireEvent.change(screen.getByLabelText(/password/i), {
    target: { value: 'password123' }
  });
  fireEvent.click(screen.getByRole('button', { name: /login/i }));
  
  expect(screen.getByText(/welcome/i)).toBeInTheDocument();
});
```

📝 **Deeper Insight**

Testing pyramid:
- **Unit Tests** (70%) - Fast, isolated, many
- **Integration Tests** (20%) - Slower, realistic, fewer
- **E2E Tests** (10%) - Slowest, complete, fewest
- **Unit Benefits** - Fast feedback, easy debugging
- **Integration Benefits** - Real user scenarios
- **Balance** - Right mix for your app

---

### 145. 🧪 How do you test Context or Redux-connected components?

🧠 **Concept**

Testing components with Context or Redux requires providing the necessary providers and mocking the state management layer to test different scenarios.

💻 **Example**

```jsx
// Testing Context components
import { ThemeProvider } from './ThemeContext';

test('component uses theme context', () => {
  render(
    <ThemeProvider value="dark">
      <ThemedComponent />
    </ThemeProvider>
  );
  
  expect(screen.getByTestId('themed-element')).toHaveClass('dark-theme');
});

// Testing Redux components
import { Provider } from 'react-redux';
import { configureStore } from '@reduxjs/toolkit';

test('Redux component', () => {
  const store = configureStore({
    reducer: {
      todos: (state = [], action) => state
    },
    preloadedState: {
      todos: [{ id: 1, text: 'Test todo' }]
    }
  });
  
  render(
    <Provider store={store}>
      <TodoList />
    </Provider>
  );
  
  expect(screen.getByText('Test todo')).toBeInTheDocument();
});

// Mocking Redux actions
jest.mock('./todoSlice', () => ({
  addTodo: jest.fn(),
  removeTodo: jest.fn()
}));
```

📝 **Deeper Insight**

State management testing:
- **Context Testing** - Provider wrapping
- **Redux Testing** - Store configuration
- **Mocking Actions** - Action creators
- **State Scenarios** - Different state combinations
- **Provider Isolation** - Testing without providers
- **Integration** - Full state management flow

---

### 146. 🧪 How do you simulate user interactions in RTL?

🧠 **Concept**

React Testing Library provides user-event utilities to simulate realistic user interactions like typing, clicking, and keyboard navigation.

💻 **Example**

```jsx
import userEvent from '@testing-library/user-event';

test('user interactions', async () => {
  const user = userEvent.setup();
  render(<ContactForm />);
  
  // Typing
  await user.type(screen.getByLabelText(/name/i), 'John Doe');
  await user.type(screen.getByLabelText(/email/i), 'john@example.com');
  
  // Clicking
  await user.click(screen.getByRole('button', { name: /submit/i }));
  
  // Keyboard navigation
  await user.keyboard('{Tab}');
  await user.keyboard('{Enter}');
  
  // File upload
  const file = new File(['hello'], 'hello.txt', { type: 'text/plain' });
  await user.upload(screen.getByLabelText(/upload/i), file);
  
  // Hover
  await user.hover(screen.getByText('Hover me'));
  
  expect(screen.getByText(/success/i)).toBeInTheDocument();
});
```

📝 **Deeper Insight**

User interaction testing:
- **userEvent** - More realistic than fireEvent
- **Async interactions** - Proper async/await usage
- **Accessibility** - Screen reader compatibility
- **Keyboard navigation** - Tab, Enter, Arrow keys
- **File operations** - Upload, drag & drop
- **Form interactions** - Validation, submission

---

### 147. 🧪 What is Cypress, and how is it used for E2E testing?

🧠 **Concept**

Cypress is an end-to-end testing framework that runs tests in a real browser, allowing you to test complete user workflows and interactions.

💻 **Example**

```jsx
// Cypress test
describe('User Login Flow', () => {
  it('should login successfully', () => {
    cy.visit('/login');
    
    cy.get('[data-testid="email-input"]')
      .type('user@example.com');
    
    cy.get('[data-testid="password-input"]')
      .type('password123');
    
    cy.get('[data-testid="login-button"]')
      .click();
    
    cy.url().should('include', '/dashboard');
    cy.get('[data-testid="welcome-message"]')
      .should('contain', 'Welcome back');
  });
  
  it('should handle login errors', () => {
    cy.visit('/login');
    
    cy.get('[data-testid="email-input"]')
      .type('invalid@example.com');
    
    cy.get('[data-testid="password-input"]')
      .type('wrongpassword');
    
    cy.get('[data-testid="login-button"]')
      .click();
    
    cy.get('[data-testid="error-message"]')
      .should('contain', 'Invalid credentials');
  });
});
```

📝 **Deeper Insight**

Cypress advantages:
- **Real browser** - Actual user environment
- **Time travel** - Debug test execution
- **Automatic waiting** - No manual waits needed
- **Network stubbing** - Mock API calls
- **Screenshots/Videos** - Visual debugging
- **Parallel execution** - Faster test runs

---

### 148. 🧪 How do you mock fetch or Axios in tests?

🧠 **Concept**

Mocking HTTP requests involves intercepting network calls to return predictable responses, allowing testing of different API scenarios without real network calls.

💻 **Example**

```jsx
// Mocking fetch
global.fetch = jest.fn();

beforeEach(() => {
  fetch.mockClear();
});

test('successful API call', async () => {
  const mockData = { id: 1, name: 'John' };
  fetch.mockResolvedValueOnce({
    ok: true,
    json: async () => mockData
  });
  
  render(<UserProfile userId={1} />);
  
  await waitFor(() => {
    expect(screen.getByText('John')).toBeInTheDocument();
  });
});

// Mocking Axios
import axios from 'axios';
jest.mock('axios');

test('API error handling', async () => {
  axios.get.mockRejectedValueOnce(new Error('Network Error'));
  
  render(<DataComponent />);
  
  await waitFor(() => {
    expect(screen.getByText(/error/i)).toBeInTheDocument();
  });
});

// Using MSW for more realistic mocking
import { rest } from 'msw';
import { setupServer } from 'msw/node';

const server = setupServer(
  rest.get('/api/users', (req, res, ctx) => {
    return res(ctx.json({ users: [] }));
  })
);

beforeAll(() => server.listen());
afterEach(() => server.resetHandlers());
afterAll(() => server.close());
```

📝 **Deeper Insight**

HTTP mocking strategies:
- **Jest mocks** - Simple fetch/axios mocking
- **MSW** - Network-level interception
- **Mock data** - Consistent test responses
- **Error scenarios** - Network failures, timeouts
- **Loading states** - Async behavior testing
- **Realistic mocking** - Close to production behavior

---

### 149. 🧪 What are async testing utilities in RTL?

🧠 **Concept**

React Testing Library provides utilities like `waitFor`, `findBy` queries, and `act` to handle asynchronous operations and state updates in tests.

💻 **Example**

```jsx
import { render, screen, waitFor, act } from '@testing-library/react';

test('async data loading', async () => {
  render(<DataComponent />);
  
  // Using findBy (automatically waits)
  const data = await screen.findByText(/loading/i);
  expect(data).toBeInTheDocument();
  
  // Using waitFor for custom conditions
  await waitFor(() => {
    expect(screen.getByText(/data loaded/i)).toBeInTheDocument();
  });
  
  // Using act for state updates
  act(() => {
    // Trigger state update
    fireEvent.click(screen.getByRole('button'));
  });
  
  await waitFor(() => {
    expect(screen.getByText(/updated/i)).toBeInTheDocument();
  });
});

// Testing async hooks
test('async hook', async () => {
  const { result } = renderHook(() => useAsyncData());
  
  expect(result.current.loading).toBe(true);
  
  await waitFor(() => {
    expect(result.current.loading).toBe(false);
    expect(result.current.data).toBeDefined();
  });
});
```

📝 **Deeper Insight**

Async testing patterns:
- **waitFor** - Custom async conditions
- **findBy queries** - Automatic waiting
- **act** - State update wrapping
- **Timeout handling** - Configurable waits
- **Error boundaries** - Async error testing
- **Race conditions** - Multiple async operations

---

### 150. 🧪 How do you measure test coverage?

🧠 **Concept**

Test coverage measures how much of your code is executed during tests, helping identify untested areas and ensuring comprehensive testing.

💻 **Example**

```jsx
// Jest coverage configuration
module.exports = {
  collectCoverage: true,
  coverageDirectory: 'coverage',
  coverageReporters: ['text', 'lcov', 'html'],
  collectCoverageFrom: [
    'src/**/*.{js,jsx}',
    '!src/index.js',
    '!src/**/*.test.{js,jsx}'
  ],
  coverageThreshold: {
    global: {
      branches: 80,
      functions: 80,
      lines: 80,
      statements: 80
    }
  }
};

// Running coverage
// npm test -- --coverage

// Coverage reports
// - Terminal output
// - HTML report in coverage/lcov-report/index.html
// - LCOV format for CI/CD integration
```

📝 **Deeper Insight**

Coverage metrics:
- **Line coverage** - Lines of code executed
- **Branch coverage** - Conditional paths taken
- **Function coverage** - Functions called
- **Statement coverage** - Statements executed
- **Coverage thresholds** - Minimum coverage requirements
- **Coverage reports** - Visual coverage analysis

---

*This comprehensive testing section covers all essential React testing concepts, tools, and best practices for building robust, well-tested React applications.*