---
sidebar_label: "Testing"
---
# 🧪 Testing

---

## 1. 🧪 Unit Testing

Unit testing focuses on testing the smallest pieces of your code in complete isolation. When you write a unit test, you're checking that a single function, hook, or component behaves correctly when you give it specific inputs, without any dependencies on external systems.

### 🔹 Key Characteristics

* Tests the **smallest pieces of logic** in isolation (functions, hooks, components)

* No external systems (network, database, real browser) – everything is **mocked or stubbed**, so you're testing just that one piece

* Fast execution – runs in milliseconds, so you get quick feedback as you code

* Deterministic – same input always produces same output, which makes tests reliable

* Easy to debug – when a unit test fails, you know exactly what broke because it's testing one thing

### 🔹 What to Test in Unit Tests

**Pure Functions:**

* Utility functions that transform data

* Formatters, validators, calculators

* Business logic that has no side effects

**React Hooks:**

* Custom hooks that manage state or side effects

* Hook behavior with different inputs

* Edge cases and error handling

**Individual Components:**

* Component rendering with different props

* User interactions (clicks, inputs)

* State changes within the component

### 🔹 Example: Testing a React Component

```javascript
// Counter.tsx
export function Counter() {
  const [count, setCount] = useState(0);
  return (
    <button onClick={() => setCount(c => c + 1)}>
      Count: {count}
    </button>
  );
}

```

```javascript
// Counter.test.tsx
import { render, screen, fireEvent } from '@testing-library/react';
import { Counter } from './Counter';

test('increments count on click', () => {
  render(<Counter />);
  const button = screen.getByRole('button', { name: /count: 0/i });
  fireEvent.click(button);
  expect(button).toHaveTextContent('Count: 1');
});

```

### 🔹 Example: Testing a Utility Function

```javascript
// utils/formatPrice.ts
export function formatPrice(amount: number, currency: string = 'USD'): string {
  return new Intl.NumberFormat('en-US', {
    style: 'currency',
    currency,
  }).format(amount);
}

```

```javascript
// utils/formatPrice.test.ts
import { formatPrice } from './formatPrice';

test('formats USD price correctly', () => {
  expect(formatPrice(19.99)).toBe('$19.99');
  expect(formatPrice(1000)).toBe('$1,000.00');
});

test('formats EUR price correctly', () => {
  expect(formatPrice(19.99, 'EUR')).toMatch(/19,99\s*€/);
});

```

### 🔹 Example: Testing a Custom Hook

```javascript
// hooks/useLocalStorage.ts
export function useLocalStorage(key: string, initialValue: string) {
  const [value, setValue] = useState(() => {
    const item = window.localStorage.getItem(key);
    return item ? JSON.parse(item) : initialValue;
  });

  const setStoredValue = (value: string) => {
    setValue(value);
    window.localStorage.setItem(key, JSON.stringify(value));
  };

  return [value, setStoredValue];
}

```

```javascript
// hooks/useLocalStorage.test.ts
import { renderHook, act } from '@testing-library/react';
import { useLocalStorage } from './useLocalStorage';

test('reads initial value from localStorage', () => {
  localStorage.setItem('test-key', JSON.stringify('stored-value'));
  const { result } = renderHook(() => useLocalStorage('test-key', 'default'));
  expect(result.current[0]).toBe('stored-value');
});

test('updates localStorage when value changes', () => {
  const { result } = renderHook(() => useLocalStorage('test-key', 'default'));
  act(() => {
    result.current[1]('new-value');
  });
  expect(localStorage.getItem('test-key')).toBe(JSON.stringify('new-value'));
});

```

📌 **In simple terms**: A unit test checks "does this tiny piece of code behave correctly by itself?" - it's fast, isolated, and tells you exactly what broke when it fails.

---

### 🔹 🧪 Integration Testing

Integration testing verifies that multiple pieces of your application work together correctly. Unlike unit tests that test things in isolation, integration tests check how components, modules, and services actually interact with each other in practice.

### 🔹 Key Characteristics

* Tests how **multiple pieces work together**:
  * Components + state management (Redux, Context)
  * Components + routing (React Router)
  * Component + API layer (mocked network calls)
  * Forms with validation and submission

* Still runs in a **simulated environment** (JSDOM, test runner), but closer to real user flows - you're testing how things actually connect

* Slower than unit tests but faster than E2E tests - good middle ground

* Catches issues that unit tests miss (integration bugs) - like when components don't talk to each other correctly

### 🔹 What to Test in Integration Tests

**Component Interactions:**

* Parent-child component communication

* Multiple components working together

* State flowing through component trees

**API Integration:**

* Components making API calls

* Handling loading, success, and error states

* Data transformation and display

**Form Flows:**

* Form validation across multiple fields

* Form submission with API calls

* Error handling and user feedback

**Routing:**

* Navigation between pages

* Route parameters and query strings

* Protected routes and authentication

### 🔹 Example: Testing a Form with API Integration

```javascript
// LoginForm.tsx
export function LoginForm() {
  const [email, setEmail] = useState('');
  const [password, setPassword] = useState('');
  const [error, setError] = useState('');
  const [loading, setLoading] = useState(false);

  const handleSubmit = async (e: React.FormEvent) => {
    e.preventDefault();
    setLoading(true);
    setError('');

    try {
      const response = await fetch('/api/login', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ email, password }),
      });

      if (!response.ok) {
        throw new Error('Login failed');
      }

      const data = await response.json();
      // Handle success (e.g., redirect, store token)
    } catch (err) {
      setError('Invalid credentials');
    } finally {
      setLoading(false);
    }
  };

  return (
    <form onSubmit={handleSubmit}>
      <input
        type="email"
        value={email}
        onChange={(e) => setEmail(e.target.value)}
        data-testid="email-input"
      />
      <input
        type="password"
        value={password}
        onChange={(e) => setPassword(e.target.value)}
        data-testid="password-input"
      />
      {error && <div data-testid="error-message">{error}</div>}
      <button type="submit" disabled={loading}>
        {loading ? 'Logging in...' : 'Login'}
      </button>
    </form>
  );
}

```

```javascript
// LoginForm.test.tsx
import { render, screen, fireEvent, waitFor } from '@testing-library/react';
import { LoginForm } from './LoginForm';

// Mock fetch globally
global.fetch = jest.fn();

test('submits form with email and password', async () => {
  (global.fetch as jest.Mock).mockResolvedValueOnce({
    ok: true,
    json: async () => ({ token: 'fake-token' }),
  });

  render(<LoginForm />);

  fireEvent.change(screen.getByTestId('email-input'), {
    target: { value: 'user@example.com' },
  });
  fireEvent.change(screen.getByTestId('password-input'), {
    target: { value: 'password123' },
  });
  fireEvent.click(screen.getByRole('button', { name: /login/i }));

  await waitFor(() => {
    expect(global.fetch).toHaveBeenCalledWith('/api/login', {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify({
        email: 'user@example.com',
        password: 'password123',
      }),
    });
  });
});

test('displays error message on failed login', async () => {
  (global.fetch as jest.Mock).mockResolvedValueOnce({
    ok: false,
  });

  render(<LoginForm />);

  fireEvent.change(screen.getByTestId('email-input'), {
    target: { value: 'user@example.com' },
  });
  fireEvent.change(screen.getByTestId('password-input'), {
    target: { value: 'wrong-password' },
  });
  fireEvent.click(screen.getByRole('button', { name: /login/i }));

  await waitFor(() => {
    expect(screen.getByTestId('error-message')).toHaveTextContent(
      'Invalid credentials'
    );
  });
});

```

### 🔹 Example: Testing Component with State Management

```javascript
// ProductList.tsx (using Redux)
import { useSelector, useDispatch } from 'react-redux';
import { fetchProducts } from './store/productsSlice';

export function ProductList() {
  const dispatch = useDispatch();
  const { products, loading, error } = useSelector((state) => state.products);

  useEffect(() => {
    dispatch(fetchProducts());
  }, [dispatch]);

  if (loading) return <div>Loading...</div>;
  if (error) return <div>Error: {error}</div>;

  return (
    <ul>
      {products.map((product) => (
        <li key={product.id}>{product.name}</li>
      ))}
    </ul>
  );
}

```

```javascript
// ProductList.test.tsx
import { render, screen } from '@testing-library/react';
import { Provider } from 'react-redux';
import { configureStore } from '@reduxjs/toolkit';
import { ProductList } from './ProductList';
import productsReducer from './store/productsSlice';

test('displays products from Redux store', () => {
  const store = configureStore({
    reducer: {
      products: productsReducer,
    },
    preloadedState: {
      products: {
        items: [
          { id: 1, name: 'Product 1' },
          { id: 2, name: 'Product 2' },
        ],
        loading: false,
        error: null,
      },
    },
  });

  render(
    <Provider store={store}>
      <ProductList />
    </Provider>
  );

  expect(screen.getByText('Product 1')).toBeInTheDocument();
  expect(screen.getByText('Product 2')).toBeInTheDocument();
});

```

📌 **In simple terms**: Integration tests check that components and modules talk to each other correctly - these tests verify the connections between pieces, not just the pieces themselves.

---

### 🔹 💡 Unit vs Integration Testing: When to Use Which

Understanding when to write unit tests versus integration tests helps you build a balanced test suite that gives you confidence without slowing down your development workflow - you want fast feedback where it matters most.

### 🔹 Use Unit Tests For

**Core Utilities and Pure Functions:**

* Formatters, validators, calculators

* Data transformation functions

* Business logic with no side effects

* Edge cases and boundary conditions

**Example:** Testing a price calculator that applies discounts, handles taxes, and formats currency - you want fast, isolated tests for all the edge cases so you can catch calculation bugs quickly.

**Individual React Hooks:**

* Custom hooks that manage state

* Hooks with complex logic

* Hook edge cases and error scenarios

**Example:** Testing a `useDebounce` hook that delays value updates - you want to verify it works correctly with different delays and input patterns, making sure it actually debounces as expected.

**Simple Components:**

* Presentational components with minimal logic

* Components that are easy to test in isolation

* Reusable UI components (buttons, inputs, cards)

**Example:** Testing a `Button` component with different variants, sizes, and disabled states - you want to make sure it renders correctly and handles clicks properly in all scenarios.

### 🔹 Use Integration Tests For

**Critical User Flows:**

* Login and authentication flows

* Checkout and payment processes

* Form submissions with validation

* Search and filtering functionality

**Example:** Testing the complete login flow - form validation, API call, success/error handling, and navigation - you want to make sure the whole flow works end-to-end, not just individual pieces.

**Cross-Component Behavior:**

* Forms with multiple fields and validation

* Complex screens with multiple components

* Parent-child component interactions

* Components that share state

**Example:** Testing a product search page - search input, filters, product list, pagination, and sorting all working together - you want to verify that when you change a filter, the list updates correctly and pagination resets.

**API Integration:**

* Components that fetch and display data

* Error handling and loading states

* Data transformation and formatting

* Caching and state management

**Example:** Testing a user profile page that fetches user data, displays it, handles errors, and allows editing - you want to make sure the loading states work, errors are shown properly, and edits actually save.

### 🔹 Real-World Testing Strategy

**E-commerce Product Page:**

* **Unit tests:** Price formatter, discount calculator, image URL builder

* **Integration tests:** Product display with API data, add to cart flow, variant selection

* **E2E tests:** Complete purchase flow from product page to checkout

**Social Media Feed:**

* **Unit tests:** Post formatter, date utilities, text truncation

* **Integration tests:** Feed loading, infinite scroll, like/comment interactions

* **E2E tests:** Post creation, feed interaction, notifications

**Dashboard with Charts:**

* **Unit tests:** Data aggregation functions, chart data formatters

* **Integration tests:** Chart rendering with real data, filter interactions, date range selection

* **E2E tests:** Complete dashboard workflow with multiple filters

---

### 🔹 🧪 End-to-End (E2E) Testing

End-to-end (E2E) tests simulate real user behavior in a real browser against a running application. These tests verify that the entire stack (frontend, backend, infrastructure) works as expected from the user's perspective - like having a robot user actually click through your app.

### 🔹 Characteristics

* Launches a **real browser** (or headless)

* Interacts with UI: click buttons, type in inputs, navigate pages

* Talks to real or staging backend

* Verifies complete user flows from start to finish

### 🔹 Example Tools

* **Cypress** - Modern E2E testing framework with great developer experience
* **Playwright** - Cross-browser testing with multiple browser support
* **WebdriverIO** - WebDriver protocol-based testing
* **Selenium** - Original browser automation tool

### 🔹 What to Test with E2E

**Critical User Flows:**

* User registration and login
* Complete purchase/checkout flow
* Form submissions with validation
* Navigation between pages
* Search and filtering workflows

**Example: E2E Test for Login Flow**

```javascript
// cypress/integration/login.spec.js
describe('Login Flow', () => {
  it('allows user to log in successfully', () => {
    cy.visit('/login');
    cy.get('[data-testid="email-input"]').type('user@example.com');
    cy.get('[data-testid="password-input"]').type('password123');
    cy.get('[data-testid="login-button"]').click();
    cy.url().should('include', '/dashboard');
    cy.get('[data-testid="user-menu"]').should('be.visible');
  });

  it('shows error for invalid credentials', () => {
    cy.visit('/login');
    cy.get('[data-testid="email-input"]').type('user@example.com');
    cy.get('[data-testid="password-input"]').type('wrong-password');
    cy.get('[data-testid="login-button"]').click();
    cy.get('[data-testid="error-message"]').should('contain', 'Invalid credentials');
  });
});
```

### 🔹 Automation Testing Beyond E2E

**Smoke Tests:**

* Quick checks after each deploy to ensure app is up and basic paths work
* Verify critical pages load without errors
* Test essential functionality still works
* Fast execution (minutes, not hours)

**Regression Suites:**

* Ensure old bugs don't come back
* Test previously fixed issues
* Verify features still work after changes
* Comprehensive coverage of core functionality

**Visual Regression Tests:**

* Detect unexpected UI changes
* Compare screenshots before/after changes
* Catch layout shifts and styling issues
* Tools: Percy, Chromatic, BackstopJS

### 🔹 Trade-offs

**Pros:**

* Highest confidence – covers full stack
* Works great for critical flows (signup, purchase, payments)
* Catches integration issues between frontend and backend
* Tests real user scenarios

**Cons:**

* Slower and more brittle
* Can be harder to maintain and debug
* Requires stable test environment
* Flaky tests can slow down development

### 🔹 Best Practices

1. **Keep E2E tests focused** - Test critical paths only
2. **Use data-testid attributes** - More stable than CSS selectors
3. **Isolate tests** - Each test should be independent
4. **Use page object pattern** - Reusable page interactions
5. **Run in CI/CD** - Catch issues before deployment

📌 **In simple terms**: E2E tests act like a robot user clicking through your app in a real browser. They're slower but give the highest confidence that the whole system works from the user's point of view.

---

### 🔹 🧪 A/B Testing

A/B testing is a technique where you show two or more variants of a feature to different user groups and use data to decide which performs better. It's essential for making data-driven product and UX decisions instead of guessing what works.

1. Define a **goal metric** (conversion, click-through, retention) - what you're trying to improve

2. Implement **Variant A** (control) and **Variant B** (experiment) - the current version and the new version

3. Randomly assign users to variants - split traffic between the two

4. Collect events and measure impact - track how each variant performs

5. Use statistical analysis to choose a winner - see which one actually performs better with real data

📌 **In simple terms**: A/B testing is “try two versions in production and see which one performs better with real users.”

---

### 🔹 💡 Frontend responsibilities

* Integrate with **experimentation platform** (e.g., LaunchDarkly, Optimizely, homegrown) - this handles the variant assignment

* Ensure:
  * Random assignment is **consistent per user** - same user always sees the same variant
  * No **flicker** (showing both variants briefly) - avoid showing one variant then switching to another
  * Events are sent correctly for each variant - track which variant the user saw so you can measure impact

### 🔹 Implementation Example

```javascript
// A/B Testing with LaunchDarkly
import { useFlags } from 'launchdarkly-react-client-sdk';

function CheckoutButton() {
  const { newCheckoutDesign } = useFlags();

  // Consistent variant per user (handled by SDK)
  if (newCheckoutDesign) {
    return <NewCheckoutButton />; // Variant B
  }
  return <OldCheckoutButton />; // Variant A
}

// Track events for analysis
function trackCheckoutClick(variant) {
  analytics.track('checkout_clicked', {
    variant: variant,
    timestamp: Date.now()
  });
}
```

### 🔹 Avoiding Flicker

**Problem:** User sees variant A, then it switches to variant B (bad UX)

**Solutions:**

* Load experiment decision server-side (SSR)
* Use CSS to hide content until variant is determined
* Bootstrap experiment config early in app lifecycle
* Use feature flags that load synchronously

📌 **In simple terms**: A/B testing shows different variants to different users and measures which one improves a target metric. On the frontend, handle variant rendering, event tracking, and avoid visual flicker by loading decisions early.

---

### 🔹 ⚡ Performance Testing

Performance testing checks how fast your application loads, responds, and behaves under different conditions. It helps you find bottlenecks before users actually feel them. This section covers testing methodology; for performance optimization and monitoring strategies, see [Performance](./18-performance.md).

### 🔹 Types of Performance Testing

**Frontend Performance Testing:**

**Page Load Metrics:**

* **Core Web Vitals**: LCP (Largest Contentful Paint) - how fast the main content loads, FID/INP (First Input Delay / Interaction to Next Paint) - how responsive the page feels, CLS (Cumulative Layout Shift) - how stable the layout is

* **Time to Interactive (TTI)**: When the page becomes fully interactive - when users can actually click things

* **First Contentful Paint (FCP)**: When first content appears - when users see something on screen

* **Total Blocking Time (TBT)**: Time the main thread is blocked - how much JavaScript is blocking the UI

**Tools for Testing:**

* **Lighthouse**: Automated audits with performance scores - gives you a quick overview of performance issues

* **WebPageTest**: Real-world testing from different locations and devices - see how your app performs from different places

* **Chrome DevTools Performance Panel**: Detailed CPU and rendering analysis - deep dive into what's slow

* **RUM (Real User Monitoring)**: Production performance data from actual users - see how real users experience your app

### 🔹 Load and Stress Testing

**Backend/API Testing:**

* Simulated traffic to backend and APIs - send lots of requests to see how it handles load

* Tests how the system handles concurrent users - what happens when many people use it at once

* Identifies bottlenecks and breaking points - find where things slow down or break

* Tools: k6, JMeter, Gatling, Artillery - these tools simulate the load

**Frontend Considerations:**

* Test how frontend handles slow API responses - make sure the UI doesn't freeze when APIs are slow

* Verify error handling under load - ensure errors are shown properly even when things are slow

* Test rate limiting and retry logic - make sure your retry logic works correctly

* Ensure UI remains responsive during high load - users should still be able to interact even when things are slow

**Load and Stress Testing:**

**Backend/API Testing:**

* Simulated traffic to backend and APIs - send lots of requests to see how it handles load
* Tests how the system handles concurrent users - what happens when many people use it at once
* Identifies bottlenecks and breaking points - find where things slow down or break
* Tools: k6, JMeter, Gatling, Artillery - these tools simulate the load

**Frontend Considerations:**

* Test how frontend handles slow API responses - make sure the UI doesn't freeze when APIs are slow
* Verify error handling under load - ensure errors are shown properly even when things are slow
* Test rate limiting and retry logic - make sure your retry logic works correctly
* Ensure UI remains responsive during high load - users should still be able to interact even when things are slow

📌 **In simple terms**: Performance testing asks "how fast is it, and does it stay fast when many users hit it?" - it measures both individual page performance and system behavior under load.

---

### 🔹 Frontend Performance Testing Workflow

**Establish Baselines:**

* Measure current performance metrics before making changes - know where you're starting from

* Document key pages and critical user flows - focus on what matters most to users

* Set performance budgets (e.g., LCP < 2.5s, bundle size < 200KB) - define what "good enough" means

**Identify Bottlenecks:**

**Common Issues to Test For:**

* **Large bundles**: JavaScript bundles that are too big - these take forever to download

* **Too many requests**: Excessive network requests - each request adds latency

* **Slow rendering**: Expensive components or layout thrashing - components that take too long to render

* **Blocking resources**: Resources that delay page rendering - things that block the initial paint

* **Unoptimized images**: Large images without compression or lazy loading - images that are way bigger than needed

**Test and Measure:**

1. **Lab Testing**: Use Lighthouse and DevTools in controlled environments - test in ideal conditions first

2. **Synthetic Testing**: Automated tests from different locations (WebPageTest) - see how it performs from different places

3. **Real User Monitoring**: Collect performance data from actual users in production - see what real users actually experience

4. **Regression Testing**: Compare before/after metrics when making changes - make sure you didn't make things worse

**Continuous Monitoring:**

* Integrate performance checks into CI/CD pipelines - catch regressions before they go live
* Set up alerts for performance regressions - get notified when things get slow
* Track performance trends over time - see if performance is getting better or worse over time
* See [Performance Monitoring](./18-performance.md#q75-performance-monitoring) for monitoring strategies

---

### 🔹 🛡️ Security Testing

Security testing looks for vulnerabilities in your application before attackers do. For frontend-heavy apps, it focuses on issues like XSS, CSRF, misconfigured CORS, and insecure dependencies. This section covers the testing perspective of security - how you actually test for these issues; for detailed security concepts and prevention strategies, see [Security](./16-security.md).

### 🔹 Types of Security Testing

**Static Analysis (SAST):**

* Scans source code for insecure patterns without running the application - looks at your code for known bad patterns

* Finds issues like unsafe DOM manipulation, hardcoded secrets, insecure API calls - catches common mistakes

* Tools: ESLint security plugins, SonarQube, CodeQL - these tools scan your code automatically

* Runs in CI/CD pipelines to catch issues early - find problems before code goes to production

**Dependency Scanning:**

* Checks npm packages for known vulnerabilities (CVEs) - looks for packages with known security issues

* Scans `package-lock.json` or `yarn.lock` against vulnerability databases - checks what you're actually using

* Tools: `npm audit`, GitHub Dependabot, Snyk, WhiteSource - these tools check your dependencies

* Should run on every build and block deployments with critical vulnerabilities - don't deploy if there are critical issues

**Dynamic Analysis (DAST):**

* Tests running application like an external attacker would - actually tries to break in

* Attempts to exploit vulnerabilities in the live app - tries common attack patterns

* Tools: OWASP ZAP, Burp Suite, Acunetix - these tools simulate attacks

* Finds runtime issues that static analysis might miss - catches things that only show up when the app is running

**Manual Security Testing:**

* Targeted tests based on threat models - test for specific attack scenarios

* Manual penetration testing by security experts - have experts try to break your app

* Code reviews focused on security patterns - have someone else look at your code for security issues

* Bug bounty programs for external security researchers - pay people to find security bugs

📌 **In simple terms**: Security testing is "attack your app yourself before others do, using both automated tools and manual checks."

---

### 🔹 Frontend Engineer's Role in Security Testing

**During Development:**

* Run dependency audits regularly (`npm audit`, Dependabot) - check for vulnerable packages often

* Use security-focused linting rules (ESLint security plugins) - catch insecure code patterns automatically

* Review code for insecure patterns before merging - look for things like `innerHTML` or `eval` usage

* Test input validation and sanitization - make sure user input is actually being cleaned

**Common Security Issues to Test:**

**XSS (Cross-Site Scripting):**

* Test all user inputs with script payloads - try injecting `<script>alert(1)</script>` into every input field
* Verify that user-generated content is properly escaped - make sure it's displayed as text, not executed as code
* Check for unsafe use of `dangerouslySetInnerHTML` or `innerHTML` - these are red flags that need extra scrutiny
* See [Cross-Site Scripting (XSS)](./16-security.md) for prevention details

**CSRF (Cross-Site Request Forgery):**

* Verify CSRF tokens are present in forms - make sure forms include the token
* Test that state-changing requests require authentication - ensure you can't make changes without being logged in
* See [Cross-Site Request Forgery (CSRF)](./16-security.md) for prevention details

**CORS Misconfiguration:**

* Test cross-origin requests to ensure proper CORS headers - make sure CORS is configured correctly
* Verify sensitive endpoints don't allow wildcard origins - don't allow `*` for authenticated endpoints
* See [Cross-Origin Resource Sharing (CORS)](./16-security.md) for details

**Insecure Dependencies:**

* Regularly audit dependencies for known vulnerabilities - check your packages often
* Keep dependencies updated to patched versions - update when security fixes are released
* See [Dependency Security](./16-security.md) for management strategies

**Testing Workflow:**

1. **Pre-commit**: Run linting with security rules - catch issues before you even commit

2. **CI/CD**: Run dependency scans and SAST tools - automated checks on every build

3. **Pre-deployment**: Run DAST scans on staging environment - test the running app before production

4. **Post-deployment**: Monitor for security incidents and respond to findings - watch for attacks and fix issues quickly

---

📌 **In simple terms**: Security testing combines automated scanners (SAST, dependency scanning, DAST) and manual checks to find vulnerabilities. On the frontend, run audits regularly, test for XSS/CSRF/CORS issues, and coordinate with security teams for comprehensive coverage. For detailed security concepts, see the Security section.

---

## ⭐ Summary — 10-second Interview Version

> "Testing includes unit tests (isolated, fast), integration tests (components working together), E2E tests (real browser, full stack), A/B testing (data-driven decisions), performance testing (speed and load), and security testing (vulnerability scanning). Use the right test type for each scenario - fast unit tests for logic, integration tests for flows, E2E for critical paths."

---

## ⭐ Extra Points (If Interviewer Asks More)

### What's your testing strategy?

I use a testing pyramid: many fast unit tests for core logic, fewer integration tests for component interactions, and a small set of E2E tests for critical user flows. This gives fast feedback while maintaining confidence.

### How do you handle flaky tests?

Identify root causes (timing issues, test isolation problems), use proper wait strategies, ensure test data is clean, and retry flaky tests with exponential backoff. Fix the underlying issue rather than just retrying.

---

