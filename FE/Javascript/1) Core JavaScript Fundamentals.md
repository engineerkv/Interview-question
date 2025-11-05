# 🧠 1. Core JavaScript Fundamentals (Q1–15)

---

## 1) What are the different data types in JavaScript?

JavaScript has primitive and non-primitive types. Primitives are immutable values; objects are reference types.

```js
const primitives = [undefined, null, true, 42, 'hi', 10n, Symbol('id')];
const obj = { a: 1 };
const arr = [1, 2, 3];
const func = () => {};
```

- **Core Types**: Primitives (undefined, null, boolean, number, string, bigint, symbol), Objects (arrays, functions, dates, regex, etc.)
- **Real-World Impact**: `typeof null === 'object'` is a historical bug, numbers are IEEE-754 doubles
- **Common Mistake**: Use `Number.isNaN` instead of global `isNaN` for accurate checking
- **Advanced Types**: Symbols are unique identifiers, BigInt for arbitrary precision
- **Interview Tip**: Explain that primitives are immutable, objects are reference types

---

## 2) What is the difference between `var`, `let`, and `const`?

`var` is function-scoped with hoisting quirks. `let`/`const` are block-scoped. `const` prevents rebinding, not mutation.

```js
var a = 1; if (true) var a = 2; // same binding
let b = 1; if (true) { let b = 2; } // block scoped
const obj = { x: 1 }; obj.x = 2; // ok; obj = {} is not
```

- **Core Difference**: `var` hoists as `undefined`, `let`/`const` have TDZ until declaration
- **Real-World Use**: Prefer `const` by default, use `let` for reassignment
- **Common Mistake**: `var` attaches to global object in non-module scripts
- **Optimization**: Block scope reduces accidental leaks and shadowing bugs
- **Interview Tip**: Explain that TDZ catches use-before-declare at runtime

---

## 3) What is the difference between `==` and `===`?

`===` compares without coercion. `==` allows type coercion with complex rules.

```js
0 == false // true
0 === false // false
null == undefined // true
'\t42' == 42 // true via coercion
```

- **Core Rule**: Prefer `===` to avoid implicit conversions
- **Real-World Use**: Only sensible `==` use: checking nullish `x == null` (matches null or undefined)
- **Common Mistake**: Objects compare by reference for both operators
- **Advanced Feature**: NaN is not equal to itself, use `Number.isNaN`
- **Interview Tip**: Explain that coercion rules follow ToPrimitive/ToNumber algorithms

---

## 4) Explain hoisting in JavaScript.

Declarations are moved to the top of their scope during compilation. Initialization is not hoisted.

```js
console.log(a); // undefined (var hoisted)
var a = 1;
// console.log(b); // TDZ error
let b = 2;
```

- **Core Concept**: `var` declarations hoist, `let`/`const` create bindings but stay in TDZ
- **Real-World Impact**: Function declarations hoist with their definitions, function expressions hoist only the variable
- **Common Mistake**: Hoisting happens per scope (function/module/block)
- **Optimization**: TDZ improves correctness by catching early access
- **Interview Tip**: Explain that initialization is not hoisted, only declarations

---

## 5) What is scope (global, local, block)?

Scope is where bindings are visible. Global spans the program, function scope is inside a function, block scope is within `{}`.

```js
let x = 1; // global (module/global)
function f() { let y = 2; if (true) { let z = 3; } }
// x visible everywhere; y in f; z only inside block
```

- **Core Types**: `let`/`const` are block-scoped, `var` is function-scoped
- **Real-World Use**: Modules have their own top-level scope (no globals)
- **Common Mistake**: Shadowing creates new inner bindings with same name
- **Advanced Feature**: Closures capture variables by reference, not by value
- **Interview Tip**: Explain that strict mode changes some global behaviors

---

## 6) What is the difference between null and undefined?

`undefined` means "not assigned". `null` is an explicit "empty" value chosen by the developer.

```js
let x; // undefined
let y = null; // intentional empty
typeof undefined; // 'undefined'
typeof null; // 'object'
```

- **Core Difference**: Uninitialized variables, missing params, absent object keys → `undefined`
- **Real-World Use**: Use `x == null` to match either `null` or `undefined`
- **Common Mistake**: JSON serializes `null` but drops `undefined` values
- **Optimization**: Optional chaining helps navigate possibly undefined paths
- **Interview Tip**: Explain that prefer `null` to signal intentional emptiness

---

## 7) What are function declarations vs function expressions?

Declarations are hoisted and named. Expressions produce a function value at runtime (can be anonymous or named).

```js
function add(a, b) { return a + b; } // declaration
const mul = function (a, b) { return a * b; }; // expression
const sub = (a, b) => a - b; // arrow expression
```

- **Core Difference**: Declarations hoist fully, expressions do not
- **Real-World Use**: Named function expressions aid stack traces and recursion
- **Common Mistake**: Arrow functions are expressions with lexical `this`
- **Optimization**: Use declarations for top-level APIs, expressions for inline behavior
- **Interview Tip**: Explain that declarations can be redeclared in sloppy mode (avoid)

---

## 8) What are arrow functions and how do they differ from regular functions?

Arrow functions (=>) are a shorter way to write functions, introduced in ES6. They have lexical `this` binding.

```js
const o = {
  regular() { return this; },
  arrow: () => this,
};
```

- **Core Difference**: Lexical `this`, `arguments`, `super`, `new.target` (no binding)
- **Real-World Use**: No `prototype`, cannot use `new` with arrows
- **Common Mistake**: Implicit return for single-expression bodies
- **Optimization**: Great for callbacks, avoid when method needs `this`
- **Interview Tip**: Explain that parentheses needed to return object literals concisely

---

## 9) What are first-class functions in JavaScript?

Functions are values: assignable, passable, returnable—enabling higher-order programming.

```js
const twice = f => x => f(f(x));
const inc = x => x + 1;
const result = twice(inc)(3); // 5
```

- **Core Concept**: Enables map/filter/reduce, callbacks, composition
- **Real-World Impact**: Closures retain access to outer variables
- **Advanced Feature**: Passing behavior enables inversion of control
- **Optimization**: Encourages declarative and reusable patterns
- **Interview Tip**: Explain that careful with over-abstraction in simple code

---

## 10) What is lexical scope?

Lexical scope is determined by where code is written. Inner code can access outer bindings.

```js
function outer() {
  const a = 1;
  function inner() { return a + 1; }
  return inner();
}
outer(); // 2
```

- **Core Concept**: Scope is fixed at parse time, not call time
- **Real-World Impact**: Closures form when inner functions capture outer vars
- **Common Mistake**: `with` and `eval` can disrupt lexical clarity (avoid)
- **Optimization**: Modules and blocks create predictable lexical boundaries
- **Interview Tip**: Explain that lexical scope helps reason about visibility and lifetime of variables

---

## 11) What will "typeof NaN" return and why?

`typeof NaN` returns `"number"` because NaN is technically a numeric type representing "Not a Number" values.

```js
console.log(typeof NaN); // "number"
console.log(NaN === NaN); // false
console.log(Number.isNaN(NaN)); // true
console.log(isNaN("hello")); // true
console.log(Number.isNaN("hello")); // false
```

- **Core Concept**: NaN is a special numeric value, not a separate data type
- **Real-World Use**: Use `Number.isNaN()` instead of `isNaN()` for accurate checking
- **Common Mistake**: `isNaN()` converts to number first, `Number.isNaN()` doesn't
- **Advanced Feature**: NaN is the only value that doesn't equal itself
- **Interview Tip**: Explain that NaN results from invalid mathematical operations (0/0, Math.sqrt(-1))

---

## 12) What will [2] == [2] return and why?

`[2] == [2]` returns `false` because arrays are compared by reference, not by value, and these are two different array objects.

```js
console.log([2] == [2]); // false
console.log([2] === [2]); // false
console.log([2] == "2"); // true (type coercion)
const arr1 = [2];
const arr2 = arr1;
console.log(arr1 == arr2); // true (same reference)
```

- **Core Rule**: Arrays are objects, compared by reference
- **Real-World Impact**: `==` performs type coercion, `===` doesn't
- **Common Mistake**: `[2] == "2"` is true due to array-to-string conversion
- **Optimization**: Use `JSON.stringify()` for deep comparison of simple arrays
- **Interview Tip**: Explain that consider using libraries like Lodash for complex comparisons

---

## 13) What does 0.1 + 0.2 === 0.3 evaluate to and why?

`0.1 + 0.2 === 0.3` returns `false` due to floating-point precision issues in binary representation.

```js
console.log(0.1 + 0.2 === 0.3); // false
console.log(0.1 + 0.2); // 0.30000000000000004
console.log(Math.abs(0.1 + 0.2 - 0.3) < Number.EPSILON); // true
```

- **Core Issue**: Floating-point numbers use binary representation
- **Real-World Impact**: Some decimal numbers can't be exactly represented in binary
- **Common Mistake**: Use `Number.EPSILON` for tolerance-based comparisons
- **Optimization**: Use `toFixed()` or `Math.round()` for display purposes
- **Interview Tip**: Explain that consider using decimal libraries for financial calculations

---

## 14) What will '5' + 3 and '5' - 3 return?

String concatenation occurs with `+`, while `-` forces numeric conversion, demonstrating JavaScript's type coercion rules.

```js
console.log('5' + 3); // "53" (string concatenation)
console.log('5' - 3); // 2 (numeric subtraction)
console.log('5' * 3); // 15 (numeric multiplication)
```

- **Core Rule**: `+` operator has special behavior for strings (concatenation)
- **Real-World Impact**: Other arithmetic operators (`-`, `*`, `/`, `%`) convert to numbers
- **Common Mistake**: `+` is the only operator that can work with strings
- **Optimization**: Use `Number()` or `parseInt()` for explicit conversion
- **Interview Tip**: Explain that be careful with mixed types in calculations

---

## 15) What are different ways to create an object in JavaScript?

Multiple ways exist to create objects in JavaScript, each with different use cases and characteristics.

```js
const obj1 = { name: 'John', age: 30 }; // Object literal
const obj2 = new Object(); obj2.name = 'John'; // Object constructor
const obj3 = Object.create(null); obj3.name = 'John'; // Object.create()
function Person(name, age) { this.name = name; this.age = age; }
const obj4 = new Person('John', 30); // Constructor function
class PersonClass { constructor(name, age) { this.name = name; this.age = age; } }
const obj5 = new PersonClass('John', 30); // Class (ES6)
const createPerson = (name, age) => ({ name, age }); const obj6 = createPerson('John', 30); // Factory function
```

- **Core Methods**: Object literal (most common), Object constructor (rarely used), Object.create() (sets prototype)
- **Real-World Use**: Constructor function (traditional OOP), Class (modern OOP with syntactic sugar)
- **Advanced Pattern**: Factory function (functional approach, returns new objects)
- **Optimization**: Object.create() can create objects without Object.prototype
- **Interview Tip**: Explain that each method has different prototype behavior

---
