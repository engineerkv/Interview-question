# 🧩 2. Functions, Closures & Execution Context (Q16–25)

---

## 16) What is a closure?

A closure lets an inner function access variables from its outer function, even after the outer function finishes.

```js
function counter(start = 0) {
  let n = start;
  return () => ++n;
}
const inc = counter(1); inc(); // 2
```

- **Core Concept**: Formed when an inner function captures outer variables, variables are captured by reference, not copied
- **Real-World Use**: Common in factories, memoization, and data privacy patterns
- **Common Mistake**: Beware of stale closures in loops; use `let` instead of `var`
- **Optimization**: Memory persists while references live, garbage collected when no references remain
- **Interview Tip**: Explain that closures enable data privacy and function factories

---

## 17) What are higher-order functions?

A higher-order function either takes functions as input or returns a function.

```js
const times = n => f => x => { while (n--) x = f(x); return x; };
const double = x => x * 2;
const eightTimes = times(3)(double);
eightTimes(1); // 8
```

- **Core Purpose**: Enables composition, callbacks, and reusable control flow
- **Real-World Use**: Abstracts iteration and effects (e.g., map/filter/reduce)
- **Common Mistake**: Watch allocations in hot paths; inline when needed for performance
- **Optimization**: Encourages declarative code over imperative loops
- **Interview Tip**: Explain that pair with closures for configuration and flexibility

---

## 18) What is function currying and how do you implement it?

Function currying means breaking a function that takes multiple arguments into a chain of functions, where each function takes one argument at a time.

```js
const curry = fn => (...a) =>
  a.length >= fn.length ? fn(...a) : (...b) => curry(fn)(...a, ...b);
const sum3 = (a, b, c) => a + b + c;
curry(sum3)(1)(2)(3); // 6
```

- **Core Purpose**: Useful for partial application and composition
- **Real-World Use**: Arity (`fn.length`) guides when to execute, works best with pure functions
- **Common Mistake**: Beware readability; not every API benefits from currying
- **Optimization**: Combine with placeholders for flexibility (advanced technique)
- **Interview Tip**: Explain that currying enables functional programming patterns

---

## 19) What are IIFEs (Immediately Invoked Function Expressions)?

An IIFE is a function that runs right away and creates its own private scope.

```js
const api = (() => {
  const secret = 42;
  return { get: () => secret };
})();
api.get(); // 42
```

- **Core Purpose**: Great for privacy before modules existed, avoids leaking variables to outer scope
- **Real-World Use**: Today, prefer ES modules and block scope
- **Common Mistake**: Still handy for one-off isolated execution
- **Optimization**: Expression form is required to invoke immediately
- **Interview Tip**: Explain that IIFEs are less needed with modern ES modules

---

## 20) How does the `this` keyword behave in different contexts?

The `this` keyword in JavaScript depends on how a function is called, not where it's defined. Arrow functions keep `this` from where they were written.

```js
function f() { return this.v; }
const obj = { v: 10, g: f };
const bound = f.bind({ v: 20 });
obj.g(); // 10, bound(); // 20
```

- **Core Rule**: Call-site rules: method call, `call`/`apply`/`bind`, constructor
- **Real-World Impact**: In modules/strict mode, bare function call `this` is `undefined`
- **Common Mistake**: Arrow functions ignore `call`/`bind` for `this`
- **Optimization**: Prefer explicit binding or arrows to avoid surprises
- **Interview Tip**: Explain that avoid relying on global `this` in modern JavaScript

---

## 21) What is the call stack?

The call stack is how JavaScript keeps track of which function is running and where to return after each one finishes. It works in Last In, First Out (LIFO) order.

```js
function one() { two(); console.log("One"); }
function two() { three(); console.log("Two"); }
function three() { console.log("Three"); }
one(); // Output: Three, Two, One
```

- **Core Rule**: The call stack pushes functions when called and pops them when done
- **Real-World Use**: Helps debug stack traces when an error shows "where" it happened
- **Common Mistake**: Deep recursion → "Maximum call stack size exceeded"
- **Advanced Feature**: JS handles only sync code in the stack; async tasks wait in the event queue
- **Interview Tip**: Explain that be ready to trace order of function execution step-by-step

---

## 22) What happens in the creation and execution phases of JavaScript?

JavaScript runs code in two main phases inside the Execution Context: Creation phase (memory is set up) and Execution phase (code actually runs line by line).

```js
var x = 10;
function greet() { console.log("Hi"); }
greet();
```

- **Core Process**: Creation phase allocates memory — variables = `undefined`, functions = full definitions
- **Real-World Impact**: Execution phase runs code top to bottom, replacing `undefined` with actual values
- **Common Mistake**: Explains why you can call functions before declaring them (hoisting)
- **Optimization**: Using a variable before initialization gives `undefined` or ReferenceError
- **Interview Tip**: Explain that always mention "memory creation first, then code execution" when asked about hoisting

---

## 23) What is the difference between synchronous and asynchronous execution?

Synchronous code runs one line at a time, blocking the next until the current finishes. Asynchronous code lets other tasks run while waiting — it doesn't block execution.

```js
console.log("Start");
setTimeout(() => console.log("Async Task"), 1000);
console.log("End");
// Output: Start, End, Async Task
```

- **Core Difference**: Synchronous = sequential; Asynchronous = non-blocking via event loop
- **Real-World Use**: Used in API calls, file reads, timers, and UI rendering
- **Common Mistake**: Expecting async code to finish before the next line runs
- **Advanced Feature**: Async tasks move to the callback/microtask queue until the call stack is empty
- **Interview Tip**: Explain that mention the event loop as the heart of async execution in JS

---

## 24) How does lexical environment relate to closures?

A lexical environment remembers variables in each scope. Closures keep access to these variables.

```js
function makeAdder(a) {
  return b => a + b;
}
const add5 = makeAdder(5); add5(2); // 7
```

- **Core Concept**: Each scope has an environment record and outer link
- **Real-World Impact**: Closures preserve the chain for later access, variables are looked up through the outer links
- **Common Mistake**: GC frees environments when no references remain
- **Optimization**: Helps reason about variable lifetime and capture
- **Interview Tip**: Explain that lexical environment enables closures to work

---

## 25) What is the difference between function declaration and arrow function `this` binding?

Regular functions have `this` that changes based on how you call them. Arrow functions keep `this` from where they were written.

```js
const obj = {
  id: 1,
  regular() { return function () { return this.id; }; },
  arrow() { return () => this.id; }
};
obj.regular()(); // undefined, obj.arrow()(); // 1
```

- **Core Difference**: Declarations/methods use call-site `this`, arrows close over `this` from defining scope
- **Real-World Impact**: `bind` affects regular functions, not arrows
- **Common Mistake**: Arrows lack `prototype` and cannot be constructors
- **Optimization**: Choose based on whether method needs dynamic or lexical `this`
- **Interview Tip**: Explain that arrow functions preserve `this` from lexical scope

---
