<div align="center">

**[← Previous: README](../README.md)** | **[Next: Functions, Closures & Execution Context →](2%29%20Functions%2C%20Closures%20%26%20Execution%20Context.md)**

</div>

# 🚀 1. Core JavaScript Fundamentals (Q1–15)

---

## Q1. 📝 Data types in JavaScript

JavaScript has primitives (immutable values like numbers, strings, booleans, null, undefined, bigint, symbols) and objects (reference types like arrays, functions, dates). When you assign primitives, they're copied by value - so `let a = 5; let b = a; b = 10;` leaves `a` as 5 because it's a copy. Objects are copied by reference, so both variables point to the same object in memory.

- **Trade-offs**: Primitives are immutable - modifying them creates a new value, which is safe but can use more memory. Objects are mutable and shared by reference, which is efficient but can cause surprise bugs when you modify something you didn't mean to.

Example:

```js
const primitives = [undefined, null, true, 42, 'hi', 10n, Symbol('id')];
const obj = { a: 1 };
const arr = [1, 2, 3];
const func = () => {};

```

---

## Q2. 📝 `var`, `let`, and `const`: differences

`var` is function-scoped and hoists as `undefined`, which can cause weird bugs. `let` and `const` are block-scoped and stay in a Temporal Dead Zone until declared - if you try to use them before the declaration, you get an error. `const` prevents reassignment but still allows you to mutate objects - so `const obj = { x: 1 }; obj.x = 2;` works, but `obj = {}` doesn't.

- **Trade-offs**: The catch is `var` can leak outside blocks and hoists in confusing ways, which is why most linters warn you to avoid it. `let` and `const` are safer because they're block-scoped, but the TDZ can be tricky if you're not careful about declaration order.

Example:

```js
var a = 1; if (true) var a = 2; // same binding
let b = 1; if (true) { let b = 2; } // block scoped
const obj = { x: 1 }; obj.x = 2; // ok; obj = {} is not

```

---

## Q3. 🔍 `==` vs `===` in JavaScript

`===` compares without type coercion - both value and type must match exactly. `==` does type coercion first, which leads to weird results like `0 == false` being true or `'\t42' == 42` being true.

- **Trade-offs**: The catch is `==` can cause surprise bugs that are hard to track down - most linters will warn you to always use `===`. The only sensible use of `==` is `x == null` to check for both null and undefined in one condition.

Example:

```js
0 == false // true (coercion)
0 === false // false
null == undefined // true
'\t42' == 42 // true via coercion

```

---

## Q4. 💡 Hoisting in JavaScript

Hoisting moves declarations to the top of their scope during compilation, but only the declaration hoists - initialization stays in place. `var` hoists as `undefined`, so you can access it before the line where it's declared, but it'll be undefined. `let` and `const` hoist too, but they stay in a Temporal Dead Zone until the declaration line - if you try to use them before that, you get a reference error.

- **Trade-offs**: Function declarations hoist with their full definition, which is convenient but can make code harder to follow. The TDZ for `let`/`const` prevents accessing variables before declaration, which catches bugs early, but it can be confusing if you're not expecting it.

Example:

```js
console.log(a); // undefined (var hoisted)
var a = 1;
// console.log(b); // TDZ error
let b = 2;

```

---

## Q5. 🔍 Scope: global, local, and block

Scope determines where variables are visible. Global scope spans the entire program, function scope is inside a function, and block scope is within curly braces. `let` and `const` are block-scoped, so they only exist inside the block where they're declared, while `var` is function-scoped and can leak outside blocks.

- **Trade-offs**: Block scope with `let`/`const` prevents accidental variable leaks and makes code more predictable, but shadowing (using the same name in nested scopes) can be confusing. Modules have their own top-level scope, so variables don't leak to global unless you explicitly export them.

Example:

```js
let x = 1; // global (module/global)
function f() { 
  let y = 2; 
  if (true) { let z = 3; } 
}
// x visible everywhere; y in f; z only inside block

```

---

## Q6. ❓ `null` vs `undefined`

`undefined` means "not assigned" - it's what you get from uninitialized variables, missing function parameters, or absent object keys. `null` is an explicit "empty" value that developers intentionally set to signal absence. Both represent "no value" but `null` is intentional, while `undefined` usually means something wasn't set.

- **Trade-offs**: The tricky part is JSON serializes `null` but drops `undefined` values, which can cause issues with API payloads. Use `x == null` to check for both in one condition, or use optional chaining (`?.`) for possibly undefined paths.

Example:

```js
let x; // undefined
let y = null; // intentional empty
typeof undefined; // 'undefined'
typeof null; // 'object' (historical bug)

```

---

## Q7. 🔧 Function declarations vs function expressions

Function declarations are hoisted and can be called before they appear in code - the entire function definition moves to the top. Function expressions produce a function value at runtime and can be anonymous or named - arrow functions are always expressions. Only the variable binding hoists for expressions, not the function itself.

- **Trade-offs**: Declarations offer hoisting convenience, which is nice for organizing code, but expressions give you more control over when functions are created. Named function expressions help with stack traces and recursion, even when assigned to variables.

Example:

```js
function add(a, b) { return a + b; } // declaration
const mul = function (a, b) { return a * b; }; // expression
const sub = (a, b) => a - b; // arrow expression

```

---

## Q8. 🔧 Arrow functions vs regular functions

Arrow functions are a shorter syntax for writing functions with lexical `this` binding - they inherit `this` from their enclosing scope instead of having their own. They don't have their own `this`, `arguments`, or `super`, and can't be used as constructors or with `new`.

- **Trade-offs**: Arrow functions are perfect for callbacks and array methods like `map` and `filter`, but watch out - they can't be used when methods need their own `this` binding. They also can't be used with `new` and don't have a `prototype` property.

Example:

```js
const obj = {
  regular() { return this; },
  arrow: () => this,
};
obj.regular(); // obj
obj.arrow(); // global/window (lexical this)

```

---

## Q9. 🔧 First-class functions in JavaScript

Functions are first-class citizens - they can be assigned to variables, passed as arguments, and returned from other functions just like any other value. This enables higher-order programming patterns like map, filter, and function composition, where you pass behavior as data.

- **Trade-offs**: First-class functions enable powerful abstractions and make code more expressive, but over-abstraction can make simple code harder to read - balance elegance with clarity. Closures retain access to outer variables, making functions stateful and reusable.

Example:

```js
const twice = f => x => f(f(x));
const inc = x => x + 1;
const result = twice(inc)(3); // 5

```

---

## Q10. 🔍 Lexical scope in JavaScript

Lexical scope is determined by where code is written in the source file - inner functions can access variables from their outer scope, but not vice versa. This scope is fixed at parse time based on code structure, not where functions are called at runtime.

- **Trade-offs**: Lexical scope makes variable visibility predictable and enables closures, but `with` and `eval` can disrupt it - avoid them in modern code. Modules and blocks create predictable lexical boundaries that make code easier to reason about.

Example:

```js
function outer() {
  const a = 1;
  function inner() { return a + 1; }
  return inner();
}
outer(); // 2

```

---

## Q11. 📝 `typeof NaN` return value and why

`typeof NaN` returns `"number"` because NaN is technically a numeric type representing invalid mathematical operations - it's a special value in the number type, not a separate data type. NaN is the only value that doesn't equal itself, so `NaN === NaN` is false.

- **Trade-offs**: Always use `Number.isNaN()` instead of global `isNaN()` - the global version coerces values first, so `isNaN("hello")` returns `true` because it converts to number first, while `Number.isNaN("hello")` returns `false`.

Example:

```js
console.log(typeof NaN); // "number"
console.log(NaN === NaN); // false
console.log(Number.isNaN(NaN)); // true
console.log(isNaN("hello")); // true (coerces first)

```

---

## Q12. 🔍 `[2] == [2]` return value and why

`[2] == [2]` returns `false` because arrays are objects, and objects are compared by reference, not by value. Even though both arrays contain the same value, they're two different objects in memory, so the references don't match.

- **Trade-offs**: Arrays are objects, so both `==` and `===` compare by reference, not content. The weird part is `==` performs type coercion, so `[2] == "2"` is true due to array-to-string conversion. For simple arrays, `JSON.stringify()` works for comparison, but beware of order and type issues - use libraries like Lodash for deep comparison.

Example:

```js
console.log([2] == [2]); // false (different references)
console.log([2] === [2]); // false
console.log([2] == "2"); // true (coercion)
const arr1 = [2];
const arr2 = arr1;
console.log(arr1 == arr2); // true (same reference)

```

---

## Q13. 🔍 `0.1 + 0.2 === 0.3` evaluation and why

`0.1 + 0.2 === 0.3` returns `false` because floating-point numbers use binary representation, and some decimals can't be exactly represented - this causes tiny precision errors. So `0.1 + 0.2` actually equals `0.30000000000000004`, not exactly `0.3`.

- **Trade-offs**: Floating-point precision is a hardware limitation, so always use tolerance checks, never direct equality. Use `Number.EPSILON` for tolerance-based comparisons when precision matters. For financial calculations, consider decimal libraries that avoid binary precision issues.

Example:

```js
console.log(0.1 + 0.2 === 0.3); // false
console.log(0.1 + 0.2); // 0.30000000000000004
console.log(Math.abs(0.1 + 0.2 - 0.3) < Number.EPSILON); // true

```

---

## Q14. 💡 `'5' + 3` and `'5' - 3` return values

`'5' + 3` returns `"53"` because `+` performs string concatenation when one operand is a string. `'5' - 3` returns `2` because `-` forces numeric conversion on both operands - all other arithmetic operators convert to numbers too, only `+` works with strings.

- **Trade-offs**: The `+` operator's dual nature (addition vs concatenation) requires careful type awareness to avoid bugs. This behavior makes string concatenation convenient but can cause bugs with mixed types - use template literals or explicit `Number()` conversion to avoid coercion surprises.

Example:

```js
console.log('5' + 3); // "53" (string concatenation)
console.log('5' - 3); // 2 (numeric subtraction)
console.log('5' * 3); // 15 (numeric multiplication)

```

---

## Q15. 📦 Different ways to create objects in JavaScript

You can create objects using object literals (most common), constructor functions, classes, `Object.create()`, or factory functions. Object literals are the simplest and inherit from `Object.prototype`, while `Object.create(null)` creates objects without prototype, useful for pure data structures.

- **Trade-offs**: Each method has different prototype behavior - classes are syntactic sugar over constructors, and factory functions return new objects without `new`, offering a functional alternative. Choose based on your needs - literals for simple data, classes for OOP, factories for flexibility.

Example:

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

<div align="center">

**[← Previous: README](../README.md)** | **[Next: Functions, Closures & Execution Context →](2%29%20Functions%2C%20Closures%20%26%20Execution%20Context.md)**

</div>
