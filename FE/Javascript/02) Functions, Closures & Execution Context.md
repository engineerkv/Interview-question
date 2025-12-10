# 🔧 2. Functions, Closures & Execution Context (Q16–24)

---

## 📍 Navigation

<div align="center">

[Core JavaScript Fundamentals](01%29%20Core%20JavaScript%20Fundamentals.md) • [Home: README](../README.md) • [Objects, Prototypes & Inheritance →](03%29%20Objects%2C%20Prototypes%20%26%20Inheritance.md)

[📋 Cheatsheet](JavaScript%20Interview%20Cheatsheet.md)

</div>

---

---

## Q16. 🔒 Closures in JavaScript

A closure allows an inner function to access variables from its outer function, even after the outer function finishes. This happens because the inner function "closes over" the outer scope's variables, keeping them alive in memory.

- **Trade-offs**: Variables are captured by reference, not copied - all closures share the same variable, which is efficient but can cause surprise bugs in loops. Watch out for stale closures in loops - use `let` instead of `var` to avoid this. Memory persists while references live, and gets garbage collected when no references remain.

Example:

```js
function counter(start = 0) {
  let n = start;
  return () => ++n;
}
const inc = counter(1);
inc(); // 2

```

---

## Q17. 🔧 Higher-order functions

A higher-order function either takes functions as input or returns a function - this enables composition, callbacks, and reusable control flow patterns. They abstract iteration and effects, like map, filter, and reduce.

- **Trade-offs**: Higher-order functions encourage declarative code over imperative loops, but watch allocations in hot paths - inline when needed for performance. Pair with closures for configuration and flexibility.

Example:

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

## Q18. 🔧 Function currying and how to implement it

Function currying breaks a function that takes multiple arguments into a chain of functions, where each function takes one argument at a time. This enables partial application and composition - you can call it like `curry(sum3)(1)(2)(3)` instead of `sum3(1, 2, 3)`.

- **Trade-offs**: Currying enables functional programming patterns, but beware readability - not every API benefits from currying. It works best with pure functions, and you can combine with placeholders for flexibility.

Example:

```js
const curry = fn => (...a) =>
  a.length >= fn.length ? fn(...a) : (...b) => curry(fn)(...a, ...b);
const sum3 = (a, b, c) => a + b + c;
curry(sum3)(1)(2)(3); // 6

```

---

## Q19. 🔧 IIFEs (Immediately Invoked Function Expressions)

An IIFE is a function that runs right away and creates its own private scope - it's useful for avoiding variable leaks to the outer scope. You wrap a function in parentheses and call it immediately, like `(() => { ... })()`.

- **Trade-offs**: IIFEs provide privacy and were great before modules existed, but today prefer ES modules and block scope - these are cleaner alternatives. Still handy for one-off isolated execution though.

Example:

```js
const api = (() => {
  const secret = 42;
  return { get: () => secret };
})();
api.get(); // 42

```

---

## Q20. 🔧 How `this` keyword behaves in different contexts

The `this` keyword depends on how a function is called, not where it's defined - it's dynamic binding. Arrow functions keep `this` from where they were written (lexical binding), so they ignore `call`/`bind` for `this`.

- **Trade-offs**: Call-site rules determine `this` - method call, `call`/`apply`/`bind`, or constructor. In modules/strict mode, bare function call `this` is `undefined`. Prefer explicit binding or arrows to avoid surprises - avoid relying on global `this` in modern JavaScript.

Example:

```js
function f() { return this.v; }
const obj = { v: 10, g: f };
const bound = f.bind({ v: 20 });
obj.g(); // 10
bound(); // 20

```

---

## Q21. 💡 Call stack in JavaScript

The call stack is how JavaScript keeps track of which function is running and where to return after each one finishes - it works in Last In, First Out (LIFO) order. It pushes functions when called and pops them when done.

- **Trade-offs**: The call stack helps debug stack traces when an error shows "where" it happened, but deep recursion causes "Maximum call stack size exceeded" errors. JavaScript handles only sync code in the stack - async tasks wait in the event queue.

Example:

```js
function one() { two(); console.log("One"); }
function two() { three(); console.log("Two"); }
function three() { console.log("Three"); }
one(); // Output: Three, Two, One

```

---

## Q22. 💡 Creation and execution phases in JavaScript

JavaScript runs code in two main phases: Creation phase (memory is set up) and Execution phase (code actually runs line by line). In creation, variables are set to `undefined` and functions get their full definitions - this explains hoisting behavior.

- **Trade-offs**: Creation phase allocates memory first, then execution phase runs code top to bottom, replacing `undefined` with actual values. This is why you can call functions before declaring them, but using a variable before initialization gives `undefined` or ReferenceError.

Example:

```js
var x = 10;
function greet() { console.log("Hi"); }
greet();

```

---

## Q23. ⚡ Synchronous vs asynchronous execution

Synchronous code runs one line at a time, blocking the next until the current finishes. Asynchronous code allows other tasks to run while waiting - it doesn't block execution, and the event loop handles async tasks via callback/microtask queues.

- **Trade-offs**: Synchronous is sequential and predictable, but can block the UI. Asynchronous is non-blocking and great for API calls, file reads, timers, and UI rendering, but the tricky part is async code doesn't finish before the next line runs - async tasks move to queues until the call stack is empty.

Example:

```js
console.log("Start");
setTimeout(() => console.log("Async Task"), 1000);
console.log("End");
// Output: Start, End, Async Task

```

---

## Q24. 🔒 How lexical environment relates to closures

A lexical environment tracks variables in each scope. Each scope includes an environment record and an outer link, and lookups follow the outer links. Closures maintain access to these variables through the environment chain after the outer function completes.

- **Trade-offs**: Closures preserve the chain for later use, enabling useful patterns, but garbage collection frees environments when no references remain. This clarifies variable lifetime and capture.

Example:

```js
function makeAdder(a) {
  return b => a + b;
}
const add5 = makeAdder(5);
add5(2); // 7

```

---

---

## 📍 Navigation

<div align="center">

[Core JavaScript Fundamentals](01%29%20Core%20JavaScript%20Fundamentals.md) • [Home: README](../README.md) • [Objects, Prototypes & Inheritance →](03%29%20Objects%2C%20Prototypes%20%26%20Inheritance.md)

[📋 Cheatsheet](JavaScript%20Interview%20Cheatsheet.md)

</div>

---
