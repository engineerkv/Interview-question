# 🧩 2. Functions, Closures & Execution Context (Q16–25)

---

## 🧩 Q16. What is a closure?

### 🧠 Concept

A closure lets an inner function access variables from its outer function, even after the outer function finishes. This happens because the inner function "closes over" the outer scope's variables.

---

### 💡 Example

```js
function counter(start = 0) {
  let n = start;
  return () => ++n;
}
const inc = counter(1);
inc(); // 2
```

---

### 🔍 Deep Insights

* **Rule:** Variables are captured by reference, not copied—all closures share the same variable.
* **Use Case:** Common in factories, memoization, and data privacy patterns.
* **Common Mistake:** Beware of stale closures in loops—use `let` instead of `var`.
* **Pro Tip:** Memory persists while references live, garbage collected when no references remain.

---

### ⭐ Senior Takeaway

Closures enable data privacy and function factories, making JavaScript's functional programming powerful.

---

## 🧩 Q17. What are higher-order functions?

### 🧠 Concept

A higher-order function either takes functions as input or returns a function. This enables composition, callbacks, and reusable control flow patterns.

---

### 💡 Example

```js
const times = n => f => x => { 
  while (n--) x = f(x); 
  return x; 
};
const double = x => x * 2;
const eightTimes = times(3)(double);
eightTimes(1); // 8
```

---

### 🔍 Deep Insights

* **Rule:** Enables composition, callbacks, and reusable control flow.
* **Use Case:** Abstracts iteration and effects—think map, filter, reduce.
* **Common Mistake:** Watch allocations in hot paths—inline when needed for performance.
* **Pro Tip:** Pair with closures for configuration and flexibility.

---

### ⭐ Senior Takeaway

Higher-order functions encourage declarative code over imperative loops.

---

## 🧩 Q18. What is function currying and how do you implement it?

### 🧠 Concept

Function currying breaks a function that takes multiple arguments into a chain of functions, where each function takes one argument at a time. This enables partial application and composition.

---

### 💡 Example

```js
const curry = fn => (...a) =>
  a.length >= fn.length ? fn(...a) : (...b) => curry(fn)(...a, ...b);
const sum3 = (a, b, c) => a + b + c;
curry(sum3)(1)(2)(3); // 6
```

---

### 🔍 Deep Insights

* **Rule:** Arity (`fn.length`) guides when to execute—works best with pure functions.
* **Use Case:** Useful for partial application and composition.
* **Common Mistake:** Beware readability—not every API benefits from currying.
* **Pro Tip:** Combine with placeholders for flexibility (advanced technique).

---

### ⭐ Senior Takeaway

Currying enables functional programming patterns but balance elegance with clarity.

---

## 🧩 Q19. What are IIFEs (Immediately Invoked Function Expressions)?

### 🧠 Concept

An IIFE is a function that runs right away and creates its own private scope. It's useful for avoiding variable leaks to the outer scope.

---

### 💡 Example

```js
const api = (() => {
  const secret = 42;
  return { get: () => secret };
})();
api.get(); // 42
```

---

### 🔍 Deep Insights

* **Rule:** Expression form is required to invoke immediately—wrapping in parentheses makes it an expression.
* **Use Case:** Great for privacy before modules existed—today, prefer ES modules and block scope.
* **Common Mistake:** Still handy for one-off isolated execution.
* **Pro Tip:** IIFEs are less needed with modern ES modules.

---

### ⭐ Senior Takeaway

IIFEs provide privacy but modern modules and block scope are cleaner alternatives.

---

## 🧩 Q20. How does the `this` keyword behave in different contexts?

### 🧠 Concept

The `this` keyword depends on how a function is called, not where it's defined. Arrow functions keep `this` from where they were written (lexical binding).

---

### 💡 Example

```js
function f() { return this.v; }
const obj = { v: 10, g: f };
const bound = f.bind({ v: 20 });
obj.g(); // 10
bound(); // 20
```

---

### 🔍 Deep Insights

* **Rule:** Call-site rules: method call, `call`/`apply`/`bind`, constructor.
* **Use Case:** In modules/strict mode, bare function call `this` is `undefined`.
* **Common Mistake:** Arrow functions ignore `call`/`bind` for `this`.
* **Pro Tip:** Prefer explicit binding or arrows to avoid surprises.

---

### ⭐ Senior Takeaway

Avoid relying on global `this` in modern JavaScript—use explicit binding or arrow functions.

---

## 🧩 Q21. What is the call stack?

### 🧠 Concept

The call stack is how JavaScript keeps track of which function is running and where to return after each one finishes. It works in Last In, First Out (LIFO) order.

---

### 💡 Example

```js
function one() { two(); console.log("One"); }
function two() { three(); console.log("Two"); }
function three() { console.log("Three"); }
one(); // Output: Three, Two, One
```

---

### 🔍 Deep Insights

* **Rule:** The call stack pushes functions when called and pops them when done.
* **Use Case:** Helps debug stack traces when an error shows "where" it happened.
* **Common Mistake:** Deep recursion → "Maximum call stack size exceeded".
* **Pro Tip:** JS handles only sync code in the stack—async tasks wait in the event queue.

---

### ⭐ Senior Takeaway

Understanding the call stack helps you trace function execution and debug errors.

---

## 🧩 Q22. What happens in the creation and execution phases of JavaScript?

### 🧠 Concept

JavaScript runs code in two main phases: Creation phase (memory is set up) and Execution phase (code actually runs line by line). This explains hoisting behavior.

---

### 💡 Example

```js
var x = 10;
function greet() { console.log("Hi"); }
greet();
```

---

### 🔍 Deep Insights

* **Rule:** Creation phase allocates memory—variables = `undefined`, functions = full definitions.
* **Use Case:** Execution phase runs code top to bottom, replacing `undefined` with actual values.
* **Common Mistake:** Explains why you can call functions before declaring them (hoisting).
* **Pro Tip:** Using a variable before initialization gives `undefined` or ReferenceError.

---

### ⭐ Senior Takeaway

Always mention "memory creation first, then code execution" when explaining hoisting.

---

## 🧩 Q23. What is the difference between synchronous and asynchronous execution?

### 🧠 Concept

Synchronous code runs one line at a time, blocking the next until the current finishes. Asynchronous code lets other tasks run while waiting—it doesn't block execution.

---

### 💡 Example

```js
console.log("Start");
setTimeout(() => console.log("Async Task"), 1000);
console.log("End");
// Output: Start, End, Async Task
```

---

### 🔍 Deep Insights

* **Rule:** Synchronous = sequential; Asynchronous = non-blocking via event loop.
* **Use Case:** Used in API calls, file reads, timers, and UI rendering.
* **Common Mistake:** Expecting async code to finish before the next line runs.
* **Pro Tip:** Async tasks move to the callback/microtask queue until the call stack is empty.

---

### ⭐ Senior Takeaway

Mention the event loop as the heart of async execution in JavaScript.

---

## 🧩 Q24. How does lexical environment relate to closures?

### 🧠 Concept

A lexical environment remembers variables in each scope. Closures keep access to these variables through the environment chain, even after the outer function finishes.

---

### 💡 Example

```js
function makeAdder(a) {
  return b => a + b;
}
const add5 = makeAdder(5);
add5(2); // 7
```

---

### 🔍 Deep Insights

* **Rule:** Each scope has an environment record and outer link—variables are looked up through the outer links.
* **Use Case:** Closures preserve the chain for later access.
* **Common Mistake:** GC frees environments when no references remain.
* **Pro Tip:** Helps reason about variable lifetime and capture.

---

### ⭐ Senior Takeaway

Lexical environment enables closures to work—it's the mechanism behind the magic.

---

## 🧩 Q25. What is the difference between function declaration and arrow function `this` binding?

### 🧠 Concept

Regular functions have `this` that changes based on how you call them (dynamic binding). Arrow functions keep `this` from where they were written (lexical binding).

---

### 💡 Example

```js
const obj = {
  id: 1,
  regular() { return function () { return this.id; }; },
  arrow() { return () => this.id; }
};
obj.regular()(); // undefined
obj.arrow()(); // 1
```

---

### 🔍 Deep Insights

* **Rule:** Declarations/methods use call-site `this`, arrows close over `this` from defining scope.
* **Use Case:** `bind` affects regular functions, not arrows.
* **Common Mistake:** Arrows lack `prototype` and cannot be constructors.
* **Pro Tip:** Choose based on whether method needs dynamic or lexical `this`.

---

### ⭐ Senior Takeaway

Arrow functions preserve `this` from lexical scope, making callbacks simpler.

---
