# 🧩 Real-World & Edge JavaScript Topics (Q130–139)

---

## 130) What is event delegation?

Concept:
Event delegation attaches a single event listener to a parent element to handle events from child elements.

Example:
```js
document.addEventListener('click', e => {
  if (e.target.matches('.button')) {
    console.log('Button clicked:', e.target.textContent);
  }
});
```

Deep Insight:
- Reduces memory usage and improves performance
- Works with dynamically added elements
- Use `e.target` to identify the actual clicked element
- Great for lists and tables with many interactive elements
- Consider event bubbling vs capturing

---

## 131) What are event bubbling and capturing?

Concept:
Event bubbling propagates from child to parent; capturing propagates from parent to child.

Example:
```js
// Capturing phase (parent to child)
element.addEventListener('click', handler, true);

// Bubbling phase (child to parent) - default
element.addEventListener('click', handler, false);
```

Deep Insight:
- Three phases: capture → target → bubble
- Use `e.stopPropagation()` to stop propagation
- Use `e.stopImmediatePropagation()` to stop all handlers
- Capturing is less commonly used
- Event delegation relies on bubbling

---

## 132) What is a shadow DOM?

Concept:
Shadow DOM encapsulates DOM and CSS, creating isolated components that don't interfere with the main document.

Example:
```js
const host = document.getElementById('host');
const shadow = host.attachShadow({ mode: 'open' });
shadow.innerHTML = `
  <style>p { color: red; }</style>
  <p>This is isolated from main document</p>
`;
```

Deep Insight:
- Creates encapsulated DOM subtree
- Styles don't leak out or in
- Used by Web Components
- `mode: 'open'` allows external access
- Great for reusable component libraries

---

## 133) What is the difference between `innerHTML`, `textContent`, and `innerText`?

Concept:
`innerHTML` includes HTML tags; `textContent` gets all text; `innerText` gets visible text respecting CSS.

Example:
```js
const div = document.createElement('div');
div.innerHTML = '<p>Hello <span style="display:none">hidden</span> World</p>';
div.innerHTML; // '<p>Hello <span style="display:none">hidden</span> World</p>'
div.textContent; // 'Hello hidden World'
div.innerText; // 'Hello World'
```

Deep Insight:
- `innerHTML`: includes HTML markup, can execute scripts
- `textContent`: all text content, safer, faster
- `innerText`: visible text only, respects CSS, slower
- Use `textContent` for security and performance
- `innerHTML` can cause XSS if not sanitized

---

## 134) What is the difference between `for...in` and `for...of`?

Concept:
`for...in` iterates over enumerable property names; `for...of` iterates over iterable values.

Example:
```js
const arr = [1, 2, 3];
arr.custom = 'property';

for (let key in arr) console.log(key); // '0', '1', '2', 'custom'
for (let value of arr) console.log(value); // 1, 2, 3
```

Deep Insight:
- `for...in`: property names, includes inherited properties
- `for...of`: values, works with iterables (arrays, strings, maps)
- Use `for...of` for arrays and iterables
- Use `for...in` with `hasOwnProperty` for object properties
- `for...of` is generally preferred for arrays

---

## 135) What is a polyfill and when would you use one?

Concept:
A polyfill is code that implements a feature in older browsers that don't natively support it.

Example:
```js
// Polyfill for Array.includes
if (!Array.prototype.includes) {
  Array.prototype.includes = function(searchElement, fromIndex) {
    return this.indexOf(searchElement, fromIndex) !== -1;
  };
}
```

Deep Insight:
- Provides missing functionality in older browsers
- Use feature detection before adding polyfills
- Consider bundle size impact
- Use tools like Babel and core-js for automatic polyfilling
- Test thoroughly in target browsers

---

## 136) What are data attributes and how do you access them in JavaScript?

Concept:
Data attributes store custom data on HTML elements using `data-*` attributes.

Example:
```js
// HTML: <div data-user-id="123" data-role="admin"></div>
const element = document.querySelector('div');
const userId = element.dataset.userId; // '123'
const role = element.dataset.role; // 'admin'
element.dataset.status = 'active'; // Sets data-status="active"
```

Deep Insight:
- Use `dataset` property to access data attributes
- Kebab-case becomes camelCase (`data-user-id` → `userId`)
- Values are always strings
- Great for storing component state and configuration
- Avoid storing complex data, use JSON if needed

---

## 137) What are pure functions and side effects?

Concept:
Pure functions always return the same output for the same input and have no side effects.

Example:
```js
// Pure function
const add = (a, b) => a + b;

// Impure function (has side effects)
let counter = 0;
const increment = () => ++counter;
```

Deep Insight:
- Pure functions are predictable and testable
- Side effects include: DOM manipulation, API calls, console.log
- Prefer pure functions when possible
- Use pure functions for reducers and transformations
- Side effects are necessary but should be isolated

---

## 138) What is a memory leak and how can you detect it?

Concept:
Memory leaks occur when objects remain in memory but are no longer needed, preventing garbage collection.

Example:
```js
// Memory leak example
const leaks = [];
setInterval(() => {
  leaks.push(new Array(1000000)); // Growing array
}, 1000);

```

Deep Insight:
- Use browser dev tools Memory tab to detect leaks
- Look for growing heap size over time
- Common causes: event listeners, closures, timers
- Use `performance.memory` API for monitoring
- Test with long-running applications

---

## 139) How does JavaScript handle tail call optimization (TCO)?

Concept:
TCO optimizes recursive function calls by reusing the current stack frame instead of creating new ones.

Example:
```js
// Tail recursive function
const factorial = (n, acc = 1) => 
  n <= 1 ? acc : factorial(n - 1, n * acc);

// Non-tail recursive (not optimized)
const factorialBad = n => 
```

Deep Insight:
- Only works with tail calls (last operation is the recursive call)
- Prevents stack overflow for deep recursion
- Not widely implemented in JavaScript engines
- Use iteration or trampolines as alternatives
- Consider the recursive pattern carefully
