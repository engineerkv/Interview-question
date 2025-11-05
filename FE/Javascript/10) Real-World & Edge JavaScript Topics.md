# 🧩 Real-World & Edge JavaScript Topics (Q121–130)

---

## 121) What is event delegation?

Event delegation attaches a single event listener to a parent element to handle events from child elements.

```js
document.addEventListener('click', e => {
  if (e.target.matches('.button')) {
    console.log('Button clicked:', e.target.textContent);
  }
});
```

- **Core Concept**: Reduces memory usage and improves performance, works with dynamically added elements
- **Real-World Use**: Use `e.target` to identify the actual clicked element, great for lists and tables with many interactive elements
- **Common Mistake**: Consider event bubbling vs capturing
- **Optimization**: Single listener handles multiple child elements
- **Interview Tip**: Explain that event delegation is more efficient than multiple listeners

---

## 122) What are event bubbling and capturing?

Event bubbling propagates from child to parent; capturing propagates from parent to child.

```js
// Capturing phase (parent to child)
element.addEventListener('click', handler, true);

// Bubbling phase (child to parent) - default
element.addEventListener('click', handler, false);
```

- **Core Concept**: Three phases: capture → target → bubble
- **Real-World Use**: Use `e.stopPropagation()` to stop propagation, use `e.stopImmediatePropagation()` to stop all handlers
- **Common Mistake**: Capturing is less commonly used
- **Advanced Feature**: Event delegation relies on bubbling
- **Interview Tip**: Explain that understanding propagation helps with event handling

---

## 123) What is a shadow DOM?

Shadow DOM encapsulates DOM and CSS, creating isolated components that don't interfere with the main document.

```js
const host = document.getElementById('host');
const shadow = host.attachShadow({ mode: 'open' });
shadow.innerHTML = `
  <style>p { color: red; }</style>
  <p>This is isolated from main document</p>
`;
```

- **Core Concept**: Creates encapsulated DOM subtree, styles don't leak out or in
- **Real-World Use**: Used by Web Components, `mode: 'open'` allows external access
- **Common Mistake**: Great for reusable component libraries
- **Advanced Feature**: Enables true component encapsulation
- **Interview Tip**: Explain that shadow DOM prevents style conflicts

---

## 124) What is the difference between `innerHTML`, `textContent`, and `innerText`?

`innerHTML` includes HTML tags; `textContent` gets all text; `innerText` gets visible text respecting CSS.

```js
const div = document.createElement('div');
div.innerHTML = '<p>Hello <span style="display:none">hidden</span> World</p>';
div.innerHTML; // '<p>Hello <span style="display:none">hidden</span> World</p>'
div.textContent; // 'Hello hidden World'
div.innerText; // 'Hello World'
```

- **Core Difference**: `innerHTML`: includes HTML markup, can execute scripts; `textContent`: all text content, safer, faster; `innerText`: visible text only, respects CSS, slower
- **Real-World Use**: Use `textContent` for security and performance
- **Common Mistake**: `innerHTML` can cause XSS if not sanitized
- **Security**: Prefer `textContent` to avoid XSS attacks
- **Interview Tip**: Explain that choose based on need: HTML vs text vs visible text

---

## 125) What is the difference between `for...in` and `for...of`?

`for...in` iterates over enumerable property names; `for...of` iterates over iterable values.

```js
const arr = [1, 2, 3];
arr.custom = 'property';

for (let key in arr) console.log(key); // '0', '1', '2', 'custom'
for (let value of arr) console.log(value); // 1, 2, 3
```

- **Core Difference**: `for...in`: property names, includes inherited properties; `for...of`: values, works with iterables (arrays, strings, maps)
- **Real-World Use**: Use `for...of` for arrays and iterables, use `for...in` with `hasOwnProperty` for object properties
- **Common Mistake**: `for...of` is generally preferred for arrays
- **Optimization**: `for...of` is more efficient for arrays
- **Interview Tip**: Explain that choose based on whether you need keys or values

---

## 126) What is a polyfill and when would you use one?

A polyfill is code that implements a feature in older browsers that don't natively support it.

```js
// Polyfill for Array.includes
if (!Array.prototype.includes) {
  Array.prototype.includes = function(searchElement, fromIndex) {
    return this.indexOf(searchElement, fromIndex) !== -1;
  };
}
```

- **Core Purpose**: Provides missing functionality in older browsers
- **Real-World Use**: Use feature detection before adding polyfills, consider bundle size impact
- **Common Mistake**: Use tools like Babel and core-js for automatic polyfilling
- **Advanced Feature**: Test thoroughly in target browsers
- **Interview Tip**: Explain that polyfills enable backward compatibility

---

## 127) What are data attributes and how do you access them in JavaScript?

Data attributes store custom data on HTML elements using `data-*` attributes.

```js
// HTML: <div data-user-id="123" data-role="admin"></div>
const element = document.querySelector('div');
const userId = element.dataset.userId; // '123'
const role = element.dataset.role; // 'admin'
element.dataset.status = 'active'; // Sets data-status="active"
```

- **Core Method**: Use `dataset` property to access data attributes, kebab-case becomes camelCase (`data-user-id` → `userId`)
- **Real-World Use**: Values are always strings, great for storing component state and configuration
- **Common Mistake**: Avoid storing complex data, use JSON if needed
- **Advanced Feature**: Data attributes are part of HTML5 spec
- **Interview Tip**: Explain that data attributes enable custom metadata on elements

---

## 128) What are pure functions and side effects?

Pure functions always return the same output for the same input and have no side effects.

```js
// Pure function
const add = (a, b) => a + b;

// Impure function (has side effects)
let counter = 0;
const increment = () => ++counter;
```

- **Core Concept**: Pure functions are predictable and testable
- **Real-World Impact**: Side effects include: DOM manipulation, API calls, console.log
- **Common Mistake**: Prefer pure functions when possible
- **Advanced Feature**: Use pure functions for reducers and transformations, side effects are necessary but should be isolated
- **Interview Tip**: Explain that pure functions are easier to test and reason about

---

## 129) What is a memory leak and how can you detect it?

Memory leaks occur when objects remain in memory but are no longer needed, preventing garbage collection.

```js
// Memory leak example
const leaks = [];
setInterval(() => {
  leaks.push(new Array(1000000)); // Growing array
}, 1000);
```

- **Core Issue**: Use browser dev tools Memory tab to detect leaks, look for growing heap size over time
- **Real-World Impact**: Common causes: event listeners, closures, timers
- **Common Mistake**: Use `performance.memory` API for monitoring
- **Advanced Feature**: Test with long-running applications
- **Interview Tip**: Explain that memory leaks cause performance degradation over time

---

## 130) How does JavaScript handle tail call optimization (TCO)?

TCO optimizes recursive function calls by reusing the current stack frame instead of creating new ones.

```js
// Tail recursive function
const factorial = (n, acc = 1) => 
  n <= 1 ? acc : factorial(n - 1, n * acc);

// Non-tail recursive (not optimized)
const factorialBad = n => 
  n <= 1 ? 1 : n * factorialBad(n - 1);
```

- **Core Concept**: Only works with tail calls (last operation is the recursive call)
- **Real-World Impact**: Prevents stack overflow for deep recursion
- **Common Mistake**: Not widely implemented in JavaScript engines
- **Advanced Feature**: Use iteration or trampolines as alternatives
- **Interview Tip**: Explain that consider the recursive pattern carefully for optimization

---
