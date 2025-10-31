# 🧠 1. Core JavaScript Fundamentals (Q1–15)

---

## 1) What are the different data types in JavaScript?

Concept:
JavaScript has primitive and non-primitive types. Primitives are immutable values; objects are reference types.

Example:
```js
const primitives = [undefined, null, true, 42, 'hi', 10n, Symbol('id')];
const obj = { a: 1 };
const arr = [1, 2, 3];
const func = () => {};
```

Deep Insight:
- Primitives: undefined, null, boolean, number, string, bigint, symbol
- Objects cover arrays, functions, dates, regex, etc.
- `typeof null === 'object'` is a historical bug
- Numbers are IEEE-754 doubles; `Number.isNaN` vs global `isNaN`
- Symbols are unique identifiers; BigInt for arbitrary precision

---

## 2) What is the difference between `var`, `let`, and `const`?

Concept:
`var` is function-scoped with hoisting quirks; `let`/`const` are block-scoped. `const` prevents rebinding, not mutation.

Example:
```js
var a = 1; if (true) var a = 2; // same binding
let b = 1; if (true) { let b = 2; } // block scoped
const obj = { x: 1 }; obj.x = 2; // ok; obj = {} is not
```

Deep Insight:
- `var` hoists as `undefined`; `let`/`const` have TDZ until declaration
- Prefer `const` by default; use `let` for reassignment
- `var` attaches to global object in non-module scripts
- Block scope reduces accidental leaks and shadowing bugs
- TDZ catches use-before-declare at runtime

---

## 3) What is the difference between `==` and `===`?

Concept:
`===` compares without coercion; `==` allows type coercion with complex rules.

Example:
```js
0 == false // true
0 === false // false
null == undefined // true
'\t42' == 42 // true via coercion
```

Deep Insight:
- Prefer `===` to avoid implicit conversions
- Only sensible `==` use: checking nullish `x == null` (matches null or undefined)
- Objects compare by reference for both operators
- NaN is not equal to itself; use `Number.isNaN`
- Coercion rules follow ToPrimitive/ToNumber algorithms

---

## 4) Explain hoisting in JavaScript.

Concept:
Declarations are moved to the top of their scope during compilation. Initialization is not hoisted.

Example:
```js
console.log(a); // undefined (var hoisted)
var a = 1;
// console.log(b); // TDZ error
let b = 2;
```

Deep Insight:
- `var` declarations hoist; `let`/`const` create bindings but stay in TDZ
- Function declarations hoist with their definitions
- Function expressions hoist only the variable, not the value
- Hoisting happens per scope (function/module/block)
- TDZ improves correctness by catching early access

---

## 5) What is scope (global, local, block)?

Concept:
Scope is where bindings are visible. Global spans the program, function scope is inside a function, block scope is within `{}`.

Example:
```js
let x = 1; // global (module/global)
function f() { let y = 2; if (true) { let z = 3; } }
// x visible everywhere; y in f; z only inside block
```

Deep Insight:
- `let`/`const` are block-scoped; `var` is function-scoped
- Modules have their own top-level scope (no globals)
- Shadowing creates new inner bindings with same name
- Closures capture variables by reference, not by value
- Strict mode changes some global behaviors

---

## 6) What is the difference between null and undefined?

Concept:
`undefined` means “not assigned”; `null` is an explicit “empty” value chosen by the developer.

Example:
```js
let x; // undefined
let y = null; // intentional empty
typeof undefined; // 'undefined'
typeof null; // 'object'
```

Deep Insight:
- Uninitialized variables, missing params, absent object keys → `undefined`
- Use `x == null` to match either `null` or `undefined`
- JSON serializes `null` but drops `undefined` values
- Optional chaining helps navigate possibly undefined paths
- Prefer `null` to signal intentional emptiness

---

## 7) What are function declarations vs function expressions?

Concept:
Declarations are hoisted and named; expressions produce a function value at runtime (can be anonymous or named).

Example:
```js
function add(a, b) { return a + b; } // declaration
const mul = function (a, b) { return a * b; }; // expression
const sub = (a, b) => a - b; // arrow expression
```

Deep Insight:
- Declarations hoist fully; expressions do not
- Named function expressions aid stack traces and recursion
- Arrow functions are expressions with lexical `this`
- Style: use declarations for top-level APIs, expressions for inline behavior
- Declarations can be redeclared in sloppy mode; avoid

---

## 8) What are arrow functions and how do they differ from regular functions?

Concept:
Arrow functions (=>) in JavaScript are a shorter and more concise way to write functions, introduced in ES6 (ECMAScript 2015).

Example:
```js
const o = {
  regular() { return this; },
  arrow: () => this,
};
```

Deep Insight:
- Lexical `this`, `arguments`, `super`, `new.target`
- No `prototype`; cannot use `new` with arrows
- Implicit return for single-expression bodies
- Great for callbacks; avoid when method needs `this`
- Parentheses needed to return object literals concisely

---

## 9) What are first-class functions in JavaScript?

Concept:
Functions are values: assignable, passable, returnable—enabling higher-order programming.

Example:
```js
const twice = f => x => f(f(x));
const inc = x => x + 1;
const result = twice(inc)(3); // 5
```

Deep Insight:
- Enables map/filter/reduce, callbacks, composition
- Closures retain access to outer variables
- Passing behavior enables inversion of control
- Encourages declarative and reusable patterns
- Careful with over-abstraction in simple code

---

## 10) What is lexical scope?

Concept:
Lexical scope is determined by where code is written; inner code can access outer bindings.

Example:
```js
function outer() {
  const a = 1;
  function inner() { return a + 1; }
  return inner();
}
outer(); // 2
```

Deep Insight:
- Scope is fixed at parse time, not call time
- Closures form when inner functions capture outer vars
- `with` and `eval` can disrupt lexical clarity (avoid)
- Modules and blocks create predictable lexical boundaries
- Helps reason about visibility and lifetime of variables

---

## 11) What will "typeof NaN" return and why?

Concept:
`typeof NaN` returns `"number"` because NaN is technically a numeric type representing "Not a Number" values.

Example:
```js
console.log(typeof NaN); // "number"
console.log(NaN === NaN); // false
console.log(Number.isNaN(NaN)); // true
console.log(isNaN("hello")); // true
console.log(Number.isNaN("hello")); // false
```

Deep Insight:
- NaN is a special numeric value, not a separate data type
- Use `Number.isNaN()` instead of `isNaN()` for accurate checking
- `isNaN()` converts to number first, `Number.isNaN()` doesn't
- NaN is the only value that doesn't equal itself
- Results from invalid mathematical operations (0/0, Math.sqrt(-1))

---

## 12) What will [2] == [2] return and why?

Concept:
`[2] == [2]` returns `false` because arrays are compared by reference, not by value, and these are two different array objects.

Example:
```js
console.log([2] == [2]); // false
console.log([2] === [2]); // false
console.log([2] == "2"); // true (type coercion)
console.log([2].toString() == "2"); // true

const arr1 = [2];
const arr2 = arr1;
console.log(arr1 == arr2); // true (same reference)
```

Deep Insight:
- Arrays are objects, compared by reference
- `==` performs type coercion, `===` doesn't
- `[2] == "2"` is true due to array-to-string conversion
- Use `JSON.stringify()` for deep comparison of simple arrays
- Consider using libraries like Lodash for complex comparisons

---

## 13) What does 0.1 + 0.2 === 0.3 evaluate to and why?

Concept:
`0.1 + 0.2 === 0.3` returns `false` due to floating-point precision issues in binary representation.

Example:
```js
console.log(0.1 + 0.2 === 0.3); // false
console.log(0.1 + 0.2); // 0.30000000000000004
console.log(0.1 + 0.2 === 0.30000000000000004); // true

// Solutions
console.log(Math.abs(0.1 + 0.2 - 0.3) < Number.EPSILON); // true
console.log(Number.parseFloat((0.1 + 0.2).toFixed(10)) === 0.3); // true
```

Deep Insight:
- Floating-point numbers use binary representation
- Some decimal numbers can't be exactly represented in binary
- Use `Number.EPSILON` for tolerance-based comparisons
- Use `toFixed()` or `Math.round()` for display purposes
- Consider using decimal libraries for financial calculations

---

## 14) What will '5' + 3 and '5' - 3 return?

Concept:
String concatenation occurs with `+`, while `-` forces numeric conversion, demonstrating JavaScript's type coercion rules.

Example:
```js
console.log('5' + 3); // "53" (string concatenation)
console.log('5' - 3); // 2 (numeric subtraction)
console.log('5' * 3); // 15 (numeric multiplication)
console.log('5' / 3); // 1.6666666666666667 (numeric division)
console.log('5' % 3); // 2 (numeric modulo)
```

Deep Insight:
- `+` operator has special behavior for strings (concatenation)
- Other arithmetic operators (`-`, `*`, `/`, `%`) convert to numbers
- `+` is the only operator that can work with strings
- Use `Number()` or `parseInt()` for explicit conversion
- Be careful with mixed types in calculations

---

## 15) What are different ways to create an object in JavaScript?

Concept:
Multiple ways exist to create objects in JavaScript, each with different use cases and characteristics.

Example:
```js
// 1. Object literal
const obj1 = { name: 'John', age: 30 };

// 2. Object constructor
const obj2 = new Object();
obj2.name = 'John';

// 3. Object.create()
const obj3 = Object.create(null);
obj3.name = 'John';

// 4. Constructor function
function Person(name, age) {
  this.name = name;
  this.age = age;
}
const obj4 = new Person('John', 30);

// 5. Class (ES6)
class PersonClass {
  constructor(name, age) {
    this.name = name;
    this.age = age;
  }
}
const obj5 = new PersonClass('John', 30);

// 6. Factory function
const createPerson = (name, age) => ({ name, age });
const obj6 = createPerson('John', 30);
```

Deep Insight:
- **Object literal**: Most common, simple syntax
- **Object constructor**: Rarely used, same as literal
- **Object.create()**: Sets prototype, can create objects without Object.prototype
- **Constructor function**: Traditional OOP approach
- **Class**: Modern OOP with syntactic sugar
- **Factory function**: Functional approach, returns new objects
