# 🧩 2. Functions, Closures & Execution Context (Q11–20)

---

## 11) What is a closure?

Concept:
A closure lets an inner function access variables from its outer function, even after the outer function finishes.

Example:
```js
function counter(start = 0) {
  let n = start;
  return () => ++n;
}
const inc = counter(1); inc(); // 2
```

Deep Insight:
- Formed when an inner function captures outer variables
- Variables are captured by reference, not copied
- Common in factories, memoization, and data privacy
- Beware of stale closures in loops; use `let`
- Memory persists while references live

---

## 12) What are higher-order functions?

Concept:
A higher-order function either takes functions as input or returns a function.

Example:
```js
const times = n => f => x => { while (n--) x = f(x); return x; };
const double = x => x * 2;
const eightTimes = times(3)(double);
eightTimes(1); // 8
```

Deep Insight:
- Enables composition, callbacks, and reusable control flow
- Abstracts iteration and effects (e.g., map/filter)
- Encourages declarative code over imperative loops
- Watch allocations in hot paths; inline when needed
- Pair with closures for configuration

---

## 13) What is function currying and how do you implement it?

Concept:
Function currying means breaking a function that takes multiple arguments into a chain of functions, where each function takes one argument at a time.

Example:
```js
const curry = fn => (...a) =>
  a.length >= fn.length ? fn(...a) : (...b) => curry(fn)(...a, ...b);
const sum3 = (a, b, c) => a + b + c;
curry(sum3)(1)(2)(3); // 6
```

Deep Insight:
- Useful for partial application and composition
- Arity (`fn.length`) guides when to execute
- Works best with pure, side-effect-free functions
- Beware readability; not every API benefits
- Combine with placeholders for flexibility (advanced)

---

## 14) What are IIFEs (Immediately Invoked Function Expressions)?

Concept:
An IIFE is a function that runs right away and creates its own private scope.

Example:
```js
const api = (() => {
  const secret = 42;
  return { get: () => secret };
})();
api.get(); // 42
```

Deep Insight:
- Great for privacy before modules existed
- Avoids leaking variables to outer scope
- Today, prefer ES modules and block scope
- Still handy for one-off isolated execution
- Expression form is required to invoke immediately

---

## 15) How does the `this` keyword behave in different contexts?

Concept:
The `this` keyword in JavaScript can be confusing because its value depends on how a function is called, not where it's defined. `this` changes based on how you call a function, but arrow functions keep `this` from where they were written.

Example:
```js
function f() { return this.v; }
const obj = { v: 10, g: f };
const bound = f.bind({ v: 20 });
obj.g(); // 10, bound(); // 20
```

Deep Insight:
- Call-site rules: method call, `call`/`apply`/`bind`, constructor
- In modules/strict mode, bare function call `this` is `undefined`
- Arrow functions ignore `call`/`bind` for `this`
- Prefer explicit binding or arrows to avoid surprises
- Avoid relying on global `this`

---

## 16) What is the call stack?

Concept:
The **call stack** is how JavaScript keeps track of **which function is running** and **where to return** after each one finishes.
It works in a **Last In, First Out (LIFO)** order — the last function called runs first.

Example:
```js
function one() { two(); console.log("One"); }
function two() { three(); console.log("Two"); }
function three() { console.log("Three"); }

one();
```

**Output:**
```
Three
Two
One
```

Deep Insight:
- **Core rule:** The call stack pushes functions when called and pops them when done
- **Real-world use:** Helps debug stack traces when an error shows "where" it happened
- **Common mistake:** Deep recursion → "Maximum call stack size exceeded"
- **Advanced point:** JS handles only *sync* code in the stack; async tasks wait in the event queue
- **Interview tip:** Be ready to trace order of function execution step-by-step

---

## 17) What happens in the creation and execution phases of JavaScript?

Concept:
JavaScript runs code in **two main phases** inside the **Execution Context**:
1️⃣ **Creation phase** – memory is set up.
2️⃣ **Execution phase** – code actually runs line by line.

Example:
```js
var x = 10;
function greet() { console.log("Hi"); }
greet();
```

Deep Insight:
- **Creation phase:** JS allocates memory — variables = `undefined`, functions = full definitions
- **Execution phase:** Code runs top to bottom, replacing `undefined` with actual values
- **Real-world use:** Explains why you can call functions *before* declaring them (hoisting)
- **Common mistake:** Using a variable before initialization gives `undefined` or ReferenceError
- **Interview tip:** Always mention "memory creation first, then code execution" when asked about hoisting

---

## 18) What is the difference between synchronous and asynchronous execution?

Concept:
**Synchronous** code runs **one line at a time**, blocking the next until the current finishes.
**Asynchronous** code lets other tasks run **while waiting** — it doesn't block execution.

Example:
```js
console.log("Start");
setTimeout(() => console.log("Async Task"), 1000);
console.log("End");
```

**Output:**
```
Start  
End  
Async Task
```

Deep Insight:
- **Core rule:** Synchronous = sequential; Asynchronous = non-blocking via event loop
- **Real-world use:** Used in API calls, file reads, timers, and UI rendering
- **Common mistake:** Expecting async code to finish before the next line runs
- **Advanced point:** Async tasks move to the callback/microtask queue until the call stack is empty
- **Interview tip:** Mention the **event loop** as the heart of async execution in JS

---

## 19) How does lexical environment relate to closures?

Concept:
A lexical environment remembers variables in each scope; closures keep access to these variables.

Example:
```js
function makeAdder(a) {
  return b => a + b;
}
const add5 = makeAdder(5); add5(2); // 7
```

Deep Insight:
- Each scope has an environment record and outer link
- Closures preserve the chain for later access
- Variables are looked up through the outer links
- GC frees environments when no references remain
- Helps reason about variable lifetime and capture

---

## 20) What is the difference between function declaration and arrow function `this` binding?

Concept:
Regular functions have `this` that changes based on how you call them; arrow functions keep `this` from where they were written.

Example:
```js
const obj = {
  id: 1,
  regular() { return function () { return this.id; }; },
  arrow() { return () => this.id; }
};
obj.regular()(); // undefined, obj.arrow()(); // 1
```

Deep Insight:
- Declarations/methods use call-site `this`
- Arrows close over `this` from defining scope
- `bind` affects regular functions, not arrows
- Arrows lack `prototype` and cannot be constructors
- Choose based on whether method needs dynamic or lexical `this`
