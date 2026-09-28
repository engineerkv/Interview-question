---
sidebar_position: 1
sidebar_label: "Manual Review Guide"
description: "A Frontend Lead's guide to effective human code review for JavaScript, TypeScript and React, with checklists and good vs needs-review examples."
---

# Code Review Guide for Frontend Lead

> **Reviewed:** 2026-09 · **Level:** Senior / Tech Lead · **Type:** Foundational

A comprehensive guide on how to conduct effective code reviews as a Frontend Lead using JavaScript, React.js, and TypeScript.

This page is about the **human** part of review: judgment, context and teaching. Everything mechanical (formatting, lint, types, tests, security scanning) should be automated so reviewers can focus here. See also:

- [Question index](./question-index.md) for interview questions with model answers
- [Automated review process](./automated-review-process.md) for the end-to-end pipeline
- [CI quality gates](./03-ci-quality-gates.md) for gate configs and legacy rollout
- [AI-assisted review](./04-ai-assisted-review.md) for where AI reviewers fit
- [Metrics and team adoption](./05-metrics-and-team-adoption.md) for review health and team norms

---

## What is Code Review?

Code review is the process of examining code changes before they're merged into the main codebase. It ensures code quality, catches bugs early, shares knowledge, and maintains consistent coding standards across the team.

**Purpose**: Improve code quality, prevent bugs, share knowledge, and maintain team standards.

---

## Code Review Mindset

### As a Reviewer

- **Be constructive, not critical**: Focus on improving code, not criticizing the author
- **Ask questions, don't demand**: Use phrases like "Could we consider..." instead of "You must..."
- **Explain the "why"**: Help developers understand the reasoning behind suggestions
- **Praise good work**: Acknowledge well-written code and creative solutions
- **Be timely**: Give a first response within one working day at most (sooner is better); if you can't, hand the review to someone else

### Review Priorities

1. **Functionality**: Does the code work correctly?
2. **Security**: Are there any security vulnerabilities?
3. **Performance**: Will this impact performance negatively?
4. **Maintainability**: Is the code easy to understand and modify?
5. **Best Practices**: Does it follow team conventions and industry standards?

---

## Code Review Checklist

### 1. Functionality & Logic

- [ ] Does the code solve the problem correctly?
- [ ] Are edge cases handled?
- [ ] Are error cases properly managed?
- [ ] Do functions have clear, single responsibilities?
- [ ] Is the logic easy to follow?

**Example - Good:**
```typescript
function calculateTotal(items: CartItem[]): number {
  if (!items || items.length === 0) return 0;
  return items.reduce((sum, item) => sum + (item.price * item.quantity), 0);
}
```

**Example - Needs Review:**
```typescript
function calculateTotal(items: any): any {
  let total = 0;
  for (let i = 0; i < items.length; i++) {
    total = total + items[i].price * items[i].quantity;
  }
  return total;
}
```

**Issues**: No type safety, no null check, uses `any`, less readable.

---

### 2. TypeScript & Type Safety

- [ ] Are types properly defined (avoid `any`)?
- [ ] Are interfaces/types used appropriately?
- [ ] Are generic types used where beneficial?
- [ ] Are type guards used for runtime checks?
- [ ] Are optional chaining and nullish coalescing used correctly?

**Example - Good:**
```typescript
interface User {
  id: string;
  name: string;
  email?: string;
}

function getUserEmail(user: User | null): string {
  return user?.email ?? 'No email provided';
}
```

**Example - Needs Review:**
```typescript
function getUserEmail(user: any): string {
  if (user && user.email) {
    return user.email;
  }
  return 'No email provided';
}
```

**Issues**: Uses `any`, verbose null checking, less type-safe.

---

### 3. React Best Practices

#### Component Structure

- [ ] Are components properly structured (hooks, logic, JSX)?
- [ ] Are components small and focused (single responsibility)?
- [ ] Is prop drilling avoided (use Context or state management)?
- [ ] Are custom hooks used for reusable logic?

**Example - Good:**
```typescript
// Custom hook
function useUserData(userId: string) {
  const [user, setUser] = useState<User | null>(null);
  const [loading, setLoading] = useState(true);
  
  useEffect(() => {
    fetchUser(userId).then(setUser).finally(() => setLoading(false));
  }, [userId]);
  
  return { user, loading };
}

// Component
function UserProfile({ userId }: { userId: string }) {
  const { user, loading } = useUserData(userId);
  if (loading) return <Spinner />;
  return <div>{user?.name}</div>;
}
```

**Example - Needs Review:**
```typescript
function UserProfile({ userId }: { userId: string }) {
  const [user, setUser] = useState(null);
  const [loading, setLoading] = useState(true);
  
  useEffect(() => {
    fetch(`/api/users/${userId}`)
      .then(res => res.json())
      .then(data => {
        setUser(data);
        setLoading(false);
      });
  }, []);
  
  if (loading) return <div>Loading...</div>;
  return <div>{user.name}</div>;
}
```

**Issues**: Missing dependency in useEffect, no error handling, logic not reusable, potential null access.

**Modern note:** For server data, prefer a data-fetching library (TanStack Query, SWR) or your framework's data layer (Next.js Server Components, route loaders) over hand-written `useEffect` fetching. They handle caching, deduplication, race conditions and cancellation. Hand-rolled effects are still worth reviewing carefully because they are where most race-condition bugs live.

#### Hooks Usage

- [ ] Are hooks called at the top level (not in conditionals/loops)?
- [ ] Are dependencies correctly specified in `useEffect`, `useMemo`, `useCallback`?
- [ ] Are cleanup functions used in `useEffect` when needed?
- [ ] Is `useMemo`/`useCallback` used appropriately (not overused)?

**Example - Good:**
```typescript
function ProductList({ category }: { category: string }) {
  const [products, setProducts] = useState<Product[]>([]);
  
  useEffect(() => {
    const controller = new AbortController();
    fetchProducts(category, { signal: controller.signal })
      .then(setProducts)
      .catch(console.error);
    
    return () => controller.abort();
  }, [category]);
  
  // toSorted returns a new array; .sort() would mutate state in place
  const sortedProducts = useMemo(
    () => products.toSorted((a, b) => a.price - b.price),
    [products]
  );
  
  return <div>{sortedProducts.map(p => <ProductCard key={p.id} product={p} />)}</div>;
}
```

**Example - Needs Review:**
```typescript
function ProductList({ category }: { category: string }) {
  const [products, setProducts] = useState([]);
  
  useEffect(() => {
    fetchProducts(category).then(setProducts);
  }); // Missing dependency array!
  
  const sortedProducts = products.sort((a, b) => a.price - b.price);
  
  return <div>{products.map(p => <ProductCard product={p} />)}</div>; // Missing key
}
```

**Issues**: Missing dependency array, no cleanup, `.sort()` mutates state in place, sorted result is never used, missing key prop.

#### State Management

- [ ] Is state lifted appropriately?
- [ ] Is local state used when global state isn't needed?
- [ ] Are state updates done immutably?
- [ ] Is Context used appropriately (not overused)?

---

### 4. Performance

- [ ] Are expensive computations memoized (`useMemo`, `useCallback`)?
- [ ] Are unnecessary re-renders prevented?
- [ ] Are images optimized (lazy loading, proper sizing)?
- [ ] Are large lists virtualized if needed?
- [ ] Are bundle sizes considered (code splitting, tree shaking)?

**Example - Good:**
```typescript
const ExpensiveComponent = memo(({ data, onAction }: Props) => {
  const processedData = useMemo(
    () => data.map(transform),
    [data]
  );
  
  const handleClick = useCallback(() => {
    onAction(processedData);
  }, [processedData, onAction]);
  
  return <div onClick={handleClick}>{/* render */}</div>;
});
```

**Example - Needs Review:**
```typescript
function ExpensiveComponent({ data, onAction }: Props) {
  const processedData = data.map(transform); // Recomputes on every render
  
  return <div onClick={() => onAction(processedData)}>{/* render */}</div>;
}
```

**Issues**: No memoization, creates new function on every render, unnecessary re-computations.

**Modern note:** If the project uses the React Compiler, most manual `memo`, `useMemo` and `useCallback` calls become unnecessary because the compiler memoizes automatically. In that case, review for code that breaks the Rules of React (mutating props or state, side effects during render), since that is what prevents the compiler from optimizing. Without the compiler, only memoize where profiling or a memoized child actually needs a stable reference.

---

### 5. Security

- [ ] Are user inputs sanitized?
- [ ] Are API keys/secrets not exposed?
- [ ] Is XSS prevention in place (avoid `dangerouslySetInnerHTML`)?
- [ ] Are authentication/authorization checks present?
- [ ] Are sensitive data handled securely?

**Example - Good:**
```typescript
// Plain text: React escapes it automatically, no sanitizing needed
function Comment({ text }: { text: string }) {
  return <div>{text}</div>;
}

// Rich HTML that must be rendered: sanitize first
function RichComment({ html }: { html: string }) {
  const sanitized = DOMPurify.sanitize(html);
  return <div dangerouslySetInnerHTML={{ __html: sanitized }} />;
}
```

**Example - Needs Review:**
```typescript
function Comment({ text }: { text: string }) {
  return <div dangerouslySetInnerHTML={{ __html: text }} />;
}
```

**Issues**: Direct HTML injection risk, XSS vulnerability.

---

### 6. Code Quality & Maintainability

#### Naming

- [ ] Are variables/functions named clearly and descriptively?
- [ ] Are boolean variables prefixed with `is`, `has`, `should`?
- [ ] Are constants in UPPER_CASE?
- [ ] Are component names in PascalCase?

**Example - Good:**
```typescript
const MAX_RETRY_ATTEMPTS = 3;
const isUserAuthenticated = checkAuth();
const hasPermission = user.role === 'admin';

function UserProfileCard() { /* ... */ }
```

**Example - Needs Review:**
```typescript
const max = 3;
const auth = checkAuth();
const perm = user.role === 'admin';

function card() { /* ... */ }
```

**Issues**: Unclear names, not descriptive, wrong casing.

#### Code Organization

- [ ] Is code organized logically (imports, constants, functions, exports)?
- [ ] Are files not too large (consider splitting)?
- [ ] Is DRY principle followed (no code duplication)?
- [ ] Are magic numbers replaced with named constants?

**Example - Good:**
```typescript
// Constants
const API_TIMEOUT = 5000;
const MAX_ITEMS = 100;

// Types
interface ApiResponse<T> {
  data: T;
  status: number;
}

// Functions
async function fetchData<T>(url: string): Promise<ApiResponse<T>> {
  // implementation
}
```

#### Comments & Documentation

- [ ] Are complex logic sections commented?
- [ ] Are function JSDoc comments present for public APIs?
- [ ] Are TODO comments actionable with context?
- [ ] Are comments explaining "why", not "what"?

**Example - Good:**
```typescript
/**
 * Calculates the discount price based on user tier and coupon code.
 * @param basePrice - Original price before discount
 * @param userTier - User's membership tier (bronze, silver, gold)
 * @param couponCode - Optional coupon code
 * @returns Final price after applying all discounts
 */
function calculateDiscountPrice(
  basePrice: number,
  userTier: UserTier,
  couponCode?: string
): number {
  // Apply tier discount first (stacking discounts)
  let discounted = basePrice * TIER_DISCOUNTS[userTier];
  
  // Then apply coupon if valid
  if (couponCode && isValidCoupon(couponCode)) {
    discounted *= 0.9; // 10% additional discount
  }
  
  return Math.max(discounted, MIN_PRICE); // Ensure minimum price
}
```

---

### 7. Testing

- [ ] Are unit tests present for complex logic?
- [ ] Are edge cases covered in tests?
- [ ] Are tests readable and maintainable?
- [ ] Are test descriptions clear?

**Example - Good:**
```typescript
describe('calculateDiscountPrice', () => {
  it('should apply tier discount for gold members', () => {
    expect(calculateDiscountPrice(100, 'gold')).toBe(80);
  });
  
  it('should apply both tier and coupon discounts', () => {
    expect(calculateDiscountPrice(100, 'gold', 'SAVE10')).toBe(72);
  });
  
  it('should not go below minimum price', () => {
    expect(calculateDiscountPrice(5, 'gold', 'SAVE10')).toBe(MIN_PRICE);
  });
});
```

---

### 8. Accessibility (a11y)

- [ ] Are semantic HTML elements used?
- [ ] Are ARIA labels present when needed?
- [ ] Is keyboard navigation supported?
- [ ] Are color contrasts sufficient?
- [ ] Are focus states visible?

**Example - Good:**
```typescript
<button
  onClick={handleSubmit}
  aria-label="Submit form"
  className="submit-btn"
>
  Submit
</button>
```

**Example - Needs Review:**
```typescript
<div onClick={handleSubmit} className="submit-btn">
  Submit
</div>
```

**Issues**: Not keyboard accessible, not semantic, no ARIA label.

---

### 9. Error Handling

- [ ] Are errors caught and handled appropriately?
- [ ] Are user-friendly error messages displayed?
- [ ] Are errors logged for debugging?
- [ ] Are loading and error states handled in UI?

**Example - Good:**
```typescript
function UserData({ userId }: { userId: string }) {
  const [user, setUser] = useState<User | null>(null);
  const [error, setError] = useState<string | null>(null);
  const [loading, setLoading] = useState(true);
  
  useEffect(() => {
    fetchUser(userId)
      .then(setUser)
      .catch(err => {
        setError('Failed to load user data');
        logger.error('User fetch failed', { userId, error: err });
      })
      .finally(() => setLoading(false));
  }, [userId]);
  
  if (loading) return <Spinner />;
  if (error) return <ErrorMessage message={error} />;
  if (!user) return <EmptyState />;
  
  return <UserProfile user={user} />;
}
```

---

### 10. Git & Code History

- [ ] Are commit messages clear and descriptive?
- [ ] Are changes logically grouped in commits?
- [ ] Are merge conflicts resolved properly?
- [ ] Is the branch up to date with main?

---

## Common Issues to Catch

### JavaScript/TypeScript

1. **Missing null/undefined checks**
   ```typescript
   // Bad
   const name = user.profile.name;
   
   // Good
   const name = user?.profile?.name ?? 'Unknown';
   ```

2. **Incorrect array/object operations**
   ```typescript
   // Bad - mutates original
   items.push(newItem);
   
   // Good - immutable
   const updatedItems = [...items, newItem];
   ```

3. **Memory leaks (event listeners, subscriptions)**
   ```typescript
   // Bad
   useEffect(() => {
     window.addEventListener('resize', handleResize);
   });
   
   // Good
   useEffect(() => {
     window.addEventListener('resize', handleResize);
     return () => window.removeEventListener('resize', handleResize);
   }, [handleResize]);
   ```

### React

1. **Missing keys in lists**
   ```typescript
   // Bad
   {items.map(item => <Item data={item} />)}
   
   // Good
   {items.map(item => <Item key={item.id} data={item} />)}
   ```

2. **Incorrect dependency arrays**
   ```typescript
   // Bad
   useEffect(() => {
     fetchData(userId);
   }, []); // Missing userId
   
   // Good
   useEffect(() => {
     fetchData(userId);
   }, [userId]);
   ```

3. **Unnecessary re-renders**
   ```typescript
   // Bad
   function Parent() {
     const [count, setCount] = useState(0);
     return <Child onClick={() => console.log('click')} />;
   }
   
   // Good
   function Parent() {
     const [count, setCount] = useState(0);
     const handleClick = useCallback(() => console.log('click'), []);
     return <Child onClick={handleClick} />;
   }
   ```

---

## Review Process

### Step 1: Initial Scan (5-10 minutes)

- Read the PR description and understand the context
- Check the files changed and their scope
- Look for obvious issues (syntax errors, missing imports)

### Step 2: Functional Review (15-20 minutes)

- Understand what the code does
- Check if it solves the problem correctly
- Verify edge cases are handled
- Test the changes locally if possible

### Step 3: Code Quality Review (15-20 minutes)

- Check code structure and organization
- Review naming conventions
- Verify TypeScript types
- Check for code duplication

### Step 4: Best Practices Review (10-15 minutes)

- Verify React patterns are followed
- Check performance considerations
- Review security aspects
- Verify accessibility

### Step 5: Provide Feedback

- Use clear, actionable comments
- Prioritize feedback (must-fix vs. nice-to-have)
- Suggest improvements with examples
- Approve or request changes

---

## Review Comments Best Practices

### Good Comment Examples

**Constructive:**
```
"Consider extracting this logic into a custom hook to make it reusable across components."
```

**Explanatory:**
```
"This might cause unnecessary re-renders. We could use `useMemo` here since the calculation only depends on `items`."
```

**Question-based:**
```
"Should we handle the case where `userId` is undefined? This could throw an error."
```

### Bad Comment Examples

**Too vague:**
```
"This looks wrong."
```

**Too demanding:**
```
"You must change this immediately."
```

**Without explanation:**
```
"Use useMemo here."
```

---

## Review Approval Criteria

### Must Approve When:

- ✅ Code solves the problem correctly
- ✅ No security vulnerabilities
- ✅ Follows team conventions
- ✅ Tests are present and passing
- ✅ No critical performance issues
- ✅ Code is maintainable

### Request Changes When:

- ❌ Functionality is broken or incomplete
- ❌ Security issues present
- ❌ Significant performance problems
- ❌ Code doesn't follow team standards
- ❌ Missing error handling
- ❌ Tests are missing or inadequate

---

## Tools & Automation

### Recommended Tools

1. **ESLint** (flat config) or **Biome**: Catch JavaScript/TypeScript issues
2. **Prettier** or **Biome**: Ensure consistent code formatting
3. **TypeScript** (`tsc --noEmit`): Type checking as its own CI step
4. **React Testing Library**: Component testing
5. **Vitest** or **Jest**: Unit testing
6. **Playwright**: End-to-end smoke tests
7. **size-limit** / bundle analyzer: Check bundle sizes

For the full pipeline and configs, see [Automated review process](./automated-review-process.md) and [CI quality gates](./03-ci-quality-gates.md).

### Pre-commit Hooks

Set up pre-commit hooks to catch issues before review (husky v9 style). Hooks are a convenience only; CI must re-run the same checks because hooks can be skipped.

```bash
# .husky/pre-commit
npx lint-staged
```

```json
{
  "scripts": {
    "prepare": "husky"
  },
  "lint-staged": {
    "*.{ts,tsx}": ["eslint --fix", "prettier --write"]
  }
}
```

---

## Code Review Metrics

Track these metrics to improve the review process (use them to find system bottlenecks, never to rank individuals; see [Metrics and team adoption](./05-metrics-and-team-adoption.md)):

- **Review Time**: Average time to complete a review
- **Review Coverage**: Percentage of code reviewed
- **Defect Rate**: Bugs found in production vs. caught in review
- **Review Comments**: Average comments per PR
- **Approval Rate**: Percentage of PRs approved on first review

---

## Continuous Improvement

### Regular Retrospectives

- Discuss what's working well
- Identify pain points
- Update review checklist based on common issues
- Share learnings with the team

### Knowledge Sharing

- Document common patterns and anti-patterns
- Create code review examples
- Conduct review training sessions
- Maintain a team style guide

---

## Key Takeaways

- **Code review is a collaborative process**, not a gatekeeping exercise
- **Focus on teaching**, not just finding issues
- **Be timely and responsive** to maintain team velocity
- **Prioritize critical issues** (security, bugs) over style preferences
- **Celebrate good code** to encourage best practices
- **Use automation** to catch low-level issues, focus reviews on logic and architecture
- **Keep learning** and adapt review process based on team feedback

---

**Remember**: The goal of code review is to improve code quality and help developers grow, not to find every possible issue or enforce personal preferences.

---

## References

- [Google Engineering Practices: Code Review](https://google.github.io/eng-practices/review/)
- [React: Rules of Hooks](https://react.dev/reference/rules/rules-of-hooks)
- [React Compiler](https://react.dev/learn/react-compiler)
- [TypeScript Handbook](https://www.typescriptlang.org/docs/handbook/intro.html)
- [OWASP Cross Site Scripting Prevention Cheat Sheet](https://cheatsheetseries.owasp.org/cheatsheets/Cross_Site_Scripting_Prevention_Cheat_Sheet.html)

