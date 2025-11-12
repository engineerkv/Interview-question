# 🧠 1. Core JavaScript Fundamentals (Q1–15)

---

## 🧩 Q1. What are the different data types in JavaScript?

### 🧠 Concept

JavaScript has primitives (immutable values like numbers, strings) and objects (reference types like arrays, functions). Primitives are copied by value, objects by reference.

---

### 💡 Example

```js
const primitives = [undefined, null, true, 42, 'hi', 10n, Symbol('id')];
const obj = { a: 1 };
const arr = [1, 2, 3];
const func = () => {};
```

---

### 🔍 Deep Insights

* **Rule:** Primitives are immutable—modifying them creates a new value.
* **Use Case:** Use `Number.isNaN()` instead of global `isNaN()` for accurate checking.
* **Common Mistake:** `typeof null === 'object'` is a historical bug—null is actually a primitive.
* **Pro Tip:** Symbols create unique identifiers perfect for object keys that won't conflict.

---

### ⭐ Senior Takeaway

Understanding primitives vs objects helps you reason about mutations, comparisons, and memory usage.

---

## 🧩 Q2. What is the difference between `var`, `let`, and `const`?

### 🧠 Concept

`var` is function-scoped and hoists as `undefined`. `let` and `const` are block-scoped and stay in a Temporal Dead Zone until declared. `const` prevents reassignment but allows object mutation.

---

### 💡 Example

```js
var a = 1; if (true) var a = 2; // same binding
let b = 1; if (true) { let b = 2; } // block scoped
const obj = { x: 1 }; obj.x = 2; // ok; obj = {} is not
```

---

### 🔍 Deep Insights

* **Rule:** `var` hoists as `undefined`, while `let`/`const` create bindings that stay in TDZ until declaration.
* **Use Case:** Prefer `const` by default, use `let` only when you need reassignment.
* **Common Mistake:** `var` attaches to the global object in non-module scripts, causing namespace pollution.
* **Pro Tip:** TDZ catches use-before-declare errors at runtime, making bugs easier to spot.

---

### ⭐ Senior Takeaway

Block scope with `let`/`const` prevents accidental leaks and makes code more predictable.

---

## 🧩 Q3. What is the difference between `==` and `===`?

### 🧠 Concept

`===` compares without type coercion—both value and type must match. `==` allows type coercion with complex rules that can lead to surprising results.

---

### 💡 Example

```js
0 == false // true (coercion)
0 === false // false
null == undefined // true
'\t42' == 42 // true via coercion
```

---

### 🔍 Deep Insights

* **Rule:** Always prefer `===` to avoid implicit type conversions that cause bugs.
* **Use Case:** The only sensible `==` use is `x == null` to check for both null and undefined.
* **Common Mistake:** Objects compare by reference for both operators—two objects with same content are never equal.
* **Pro Tip:** NaN is the only value that doesn't equal itself—use `Number.isNaN()` to check.

---

### ⭐ Senior Takeaway

Strict equality (`===`) eliminates coercion surprises and makes your code's behavior predictable.

---

## 🧩 Q4. Explain hoisting in JavaScript.

### 🧠 Concept

Hoisting moves declarations to the top of their scope during compilation. Only the declaration hoists—initialization stays in place. `var` hoists as `undefined`, while `let`/`const` stay in a Temporal Dead Zone.

---

### 💡 Example

```js
console.log(a); // undefined (var hoisted)
var a = 1;
// console.log(b); // TDZ error
let b = 2;
```

---

### 🔍 Deep Insights

* **Rule:** Function declarations hoist with their full definition, while function expressions only hoist the variable.
* **Use Case:** Function declarations can be called before they appear in code, useful for organizing code.
* **Common Mistake:** Hoisting happens per scope—function scope for `var`, block scope for `let`/`const`.
* **Pro Tip:** TDZ prevents accessing `let`/`const` before declaration, catching bugs early.

---

### ⭐ Senior Takeaway

Understanding hoisting helps you write code that works, but prefer `let`/`const` to avoid surprises.

---

## 🧩 Q5. What is scope (global, local, block)?

### 🧠 Concept

Scope determines where variables are visible. Global scope spans the entire program, function scope is inside a function, and block scope is within curly braces. `let`/`const` are block-scoped, while `var` is function-scoped.

---

### 💡 Example

```js
let x = 1; // global (module/global)
function f() { 
  let y = 2; 
  if (true) { let z = 3; } 
}
// x visible everywhere; y in f; z only inside block
```

---

### 🔍 Deep Insights

* **Rule:** Modules have their own top-level scope—variables don't leak to global unless explicitly exported.
* **Use Case:** Block scope with `let`/`const` prevents accidental variable leaks and shadowing bugs.
* **Common Mistake:** Shadowing creates new inner bindings with the same name, which can be confusing.
* **Pro Tip:** Closures capture variables by reference, not by value—watch out in loops.

---

### ⭐ Senior Takeaway

Block scope creates predictable boundaries and prevents the variable pollution that `var` causes.

---

## 🧩 Q6. What is the difference between null and undefined?

### 🧠 Concept

`undefined` means "not assigned"—it's what you get from uninitialized variables or missing object keys. `null` is an explicit "empty" value that developers intentionally set to signal absence.

---

### 💡 Example

```js
let x; // undefined
let y = null; // intentional empty
typeof undefined; // 'undefined'
typeof null; // 'object' (historical bug)
```

---

### 🔍 Deep Insights

* **Rule:** Uninitialized variables, missing params, and absent object keys all return `undefined`.
* **Use Case:** Use `x == null` to check for both null and undefined in one condition.
* **Common Mistake:** JSON serializes `null` but drops `undefined` values—be careful with API payloads.
* **Pro Tip:** Prefer `null` to signal intentional emptiness, use optional chaining for possibly undefined paths.

---

### ⭐ Senior Takeaway

Use `null` for intentional emptiness and `undefined` for "not set"—this clarifies your code's intent.

---

## 🧩 Q7. What are function declarations vs function expressions?

### 🧠 Concept

Function declarations are hoisted and can be called before they appear in code. Function expressions produce a function value at runtime and can be anonymous or named. Arrow functions are always expressions.

---

### 💡 Example

```js
function add(a, b) { return a + b; } // declaration
const mul = function (a, b) { return a * b; }; // expression
const sub = (a, b) => a - b; // arrow expression
```

---

### 🔍 Deep Insights

* **Rule:** Declarations hoist fully with their definition, expressions only hoist the variable binding.
* **Use Case:** Named function expressions help with stack traces and recursion, even when assigned to variables.
* **Common Mistake:** Arrow functions are always expressions and have lexical `this` binding.
* **Pro Tip:** Use declarations for top-level APIs, expressions for inline behavior or callbacks.

---

### ⭐ Senior Takeaway

Declarations offer hoisting convenience, but expressions give you more control over when functions are created.

---

## 🧩 Q8. What are arrow functions and how do they differ from regular functions?

### 🧠 Concept

Arrow functions are a shorter syntax for writing functions with lexical `this` binding. They don't have their own `this`, `arguments`, or `super`, and can't be used as constructors.

---

### 💡 Example

```js
const obj = {
  regular() { return this; },
  arrow: () => this,
};
obj.regular(); // obj
obj.arrow(); // global/window (lexical this)
```

---

### 🔍 Deep Insights

* **Rule:** Arrow functions inherit `this` from their enclosing scope, making them perfect for callbacks.
* **Use Case:** Great for array methods like `map` and `filter`, but avoid when methods need their own `this`.
* **Common Mistake:** Arrow functions can't be used with `new` and don't have a `prototype` property.
* **Pro Tip:** Use parentheses to return object literals concisely: `() => ({ name: 'John' })`.

---

### ⭐ Senior Takeaway

Arrow functions simplify callbacks but aren't a drop-in replacement—use regular functions when you need `this` binding.

---

## 🧩 Q9. What are first-class functions in JavaScript?

### 🧠 Concept

Functions are first-class citizens—they can be assigned to variables, passed as arguments, and returned from other functions. This enables higher-order programming patterns like map, filter, and function composition.

---

### 💡 Example

```js
const twice = f => x => f(f(x));
const inc = x => x + 1;
const result = twice(inc)(3); // 5
```

---

### 🔍 Deep Insights

* **Rule:** First-class functions enable passing behavior as data, enabling powerful abstractions.
* **Use Case:** Closures retain access to outer variables, making functions stateful and reusable.
* **Common Mistake:** Over-abstraction can make simple code harder to read—balance elegance with clarity.
* **Pro Tip:** Function composition and higher-order functions encourage declarative, reusable patterns.

---

### ⭐ Senior Takeaway

First-class functions unlock functional programming patterns that make code more expressive and reusable.

---

## 🧩 Q10. What is lexical scope?

### 🧠 Concept

Lexical scope is determined by where code is written in the source file. Inner functions can access variables from their outer scope, but not vice versa. This scope is fixed at parse time, not runtime.

---

### 💡 Example

```js
function outer() {
  const a = 1;
  function inner() { return a + 1; }
  return inner();
}
outer(); // 2
```

---

### 🔍 Deep Insights

* **Rule:** Scope is fixed at parse time based on code structure, not where functions are called.
* **Use Case:** Closures form when inner functions capture outer variables, enabling powerful patterns.
* **Common Mistake:** `with` and `eval` can disrupt lexical scope—avoid them in modern code.
* **Pro Tip:** Modules and blocks create predictable lexical boundaries that make code easier to reason about.

---

### ⭐ Senior Takeaway

Lexical scope makes variable visibility predictable and enables closures, one of JavaScript's most powerful features.

---

## 🧩 Q11. What will "typeof NaN" return and why?

### 🧠 Concept

`typeof NaN` returns `"number"` because NaN is technically a numeric type representing invalid mathematical operations. It's a special value in the number type, not a separate data type.

---

### 💡 Example

```js
console.log(typeof NaN); // "number"
console.log(NaN === NaN); // false
console.log(Number.isNaN(NaN)); // true
console.log(isNaN("hello")); // true (coerces first)
```

---

### 🔍 Deep Insights

* **Rule:** NaN is the only value that doesn't equal itself—use `Number.isNaN()` to check for it.
* **Use Case:** Always use `Number.isNaN()` instead of global `isNaN()`—the global version coerces values first.
* **Common Mistake:** `isNaN("hello")` returns `true` because it converts to number first, while `Number.isNaN("hello")` returns `false`.

---

### ⭐ Senior Takeaway

NaN is a number type quirk—always use `Number.isNaN()` for accurate checking, never the global version.

---

## 🧩 Q12. What will [2] == [2] return and why?

### 🧠 Concept

`[2] == [2]` returns `false` because arrays are objects, and objects are compared by reference, not by value. Even though both arrays contain the same value, they're two different objects in memory.

---

### 💡 Example

```js
console.log([2] == [2]); // false (different references)
console.log([2] === [2]); // false
console.log([2] == "2"); // true (coercion)
const arr1 = [2];
const arr2 = arr1;
console.log(arr1 == arr2); // true (same reference)
```

---

### 🔍 Deep Insights

* **Rule:** Arrays are objects, so both `==` and `===` compare by reference, not content.
* **Use Case:** `==` performs type coercion, so `[2] == "2"` is true due to array-to-string conversion.
* **Common Mistake:** Expecting array equality to compare contents—use libraries like Lodash for deep comparison.
* **Pro Tip:** For simple arrays, `JSON.stringify()` works for comparison, but beware of order and type issues.

---

### ⭐ Senior Takeaway

Array comparison is by reference, not content—use specialized libraries for meaningful value comparisons.

---

## 🧩 Q13. What does 0.1 + 0.2 === 0.3 evaluate to and why?

### 🧠 Concept

`0.1 + 0.2 === 0.3` returns `false` because floating-point numbers use binary representation, and some decimals can't be exactly represented. This causes tiny precision errors.

---

### 💡 Example

```js
console.log(0.1 + 0.2 === 0.3); // false
console.log(0.1 + 0.2); // 0.30000000000000004
console.log(Math.abs(0.1 + 0.2 - 0.3) < Number.EPSILON); // true
```

---

### 🔍 Deep Insights

* **Rule:** Floating-point uses binary representation, so some decimal numbers can't be exactly stored.
* **Use Case:** Use `Number.EPSILON` for tolerance-based comparisons when precision matters.
* **Common Mistake:** Direct equality checks fail for floating-point—always use tolerance ranges.
* **Pro Tip:** For financial calculations, consider decimal libraries that avoid binary precision issues.

---

### ⭐ Senior Takeaway

Floating-point precision is a hardware limitation—always use tolerance checks, never direct equality.

---

## 🧩 Q14. What will '5' + 3 and '5' - 3 return?

### 🧠 Concept

`'5' + 3` returns `"53"` because `+` performs string concatenation when one operand is a string. `'5' - 3` returns `2` because `-` forces numeric conversion on both operands.

---

### 💡 Example

```js
console.log('5' + 3); // "53" (string concatenation)
console.log('5' - 3); // 2 (numeric subtraction)
console.log('5' * 3); // 15 (numeric multiplication)
```

---

### 🔍 Deep Insights

* **Rule:** `+` is the only operator that works with strings—all other arithmetic operators convert to numbers.
* **Use Case:** This behavior makes string concatenation convenient but can cause bugs with mixed types.
* **Common Mistake:** Accidentally concatenating numbers when you meant to add—use `Number()` for explicit conversion.
* **Pro Tip:** Use template literals or explicit `Number()` conversion to avoid coercion surprises.

---

### ⭐ Senior Takeaway

The `+` operator's dual nature (addition vs concatenation) requires careful type awareness to avoid bugs.

---

## 🧩 Q15. What are different ways to create an object in JavaScript?

### 🧠 Concept

You can create objects using object literals (most common), constructor functions, classes, `Object.create()`, or factory functions. Each method has different prototype behavior and use cases.

---

### 💡 Example

```js
const obj1 = { name: 'John' }; // literal
const obj2 = new Object(); // constructor
const obj3 = Object.create(null); // no prototype
function Person(name) { this.name = name; }
const obj4 = new Person('John'); // constructor function
class PersonClass { constructor(name) { this.name = name; } }
const obj5 = new PersonClass('John'); // class
```

---

### 🔍 Deep Insights

* **Rule:** Object literals are the simplest and most common—they inherit from `Object.prototype`.
* **Use Case:** `Object.create(null)` creates objects without prototype, useful for pure data structures.
* **Common Mistake:** Each method has different prototype behavior—classes are syntactic sugar over constructors.
* **Pro Tip:** Factory functions return new objects without `new`, offering a functional alternative to constructors.

---

### ⭐ Senior Takeaway

Choose object creation method based on your needs—literals for simple data, classes for OOP, factories for flexibility.

---
