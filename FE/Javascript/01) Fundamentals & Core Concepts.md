# 🚀 1. Fundamentals & Core Concepts (Q1–Q8)

---

## 📍 Navigation

<div align="center">

[Home: README](../README.md) • [Next: Functions & Execution Context →](02%29%20Functions%20%26%20Execution%20Context.md)

[📋 Cheatsheet](JavaScript%20Interview%20Cheatsheet.md)

</div>

---

---

## Q1. 📝 Data types in JavaScript

JavaScript has primitives (immutable values like numbers, strings, booleans, null, undefined, bigint, symbols) and objects (reference types like arrays, functions, dates). When you assign primitives, you're copying the value - so `let a = 5; let b = a; b = 10;` leaves `a` as 5 because it's a copy. Objects are copied by reference, so both variables point to the same object in memory.

- **Trade-offs**: Primitives are immutable - modifying them creates a new value, which is safe but can use more memory. Objects are mutable and shared by reference, which is efficient but can cause surprise bugs when you modify something you didn't mean to.

Example:

```js
const primitives = [undefined, null, true, 42, 'hi', 10n, Symbol('id')];
const obj = { a: 1 };
const arr = [1, 2, 3];
const func = () => {};

```

---

## Q2. 🔍 `==` vs `===` in JavaScript

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

## Q3. ❓ `null` vs `undefined`

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

## Q4. 🔧 First-class functions in JavaScript

Functions are first-class citizens - you can assign these to variables, pass these as arguments, and return these from other functions just like any other value. This enables higher-order programming patterns like map, filter, and function composition, where you pass behavior as data.

- **Trade-offs**: First-class functions enable powerful abstractions and make code more expressive, but over-abstraction can make simple code harder to read - balance elegance with clarity. Closures retain access to outer variables, making functions stateful and reusable.

Example:

```js
// Function that takes a function and returns a function (higher-order function)
const twice = f => x => f(f(x));
const inc = x => x + 1; // Simple increment function
// Pass function as argument, get function as return value
const result = twice(inc)(3); // inc(inc(3)) = inc(4) = 5

```

---

## Q5. 📝 `typeof NaN` return value and why

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

## Q6. 🔍 `[2] == [2]` return value and why

`[2] == [2]` returns `false` because arrays are objects, and objects are compared by reference, not by value. Even though both arrays contain the same value, these are two different objects in memory, so the references don't match.

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

## Q7. 🔍 `0.1 + 0.2 === 0.3` evaluation and why

`0.1 + 0.2 === 0.3` returns `false` because floating-point numbers use binary representation, and some decimals can't be exactly represented - this causes tiny precision errors. So `0.1 + 0.2` actually equals `0.30000000000000004`, not exactly `0.3`.

- **Trade-offs**: Floating-point precision is a hardware limitation, so always use tolerance checks, never direct equality. Use `Number.EPSILON` for tolerance-based comparisons when precision matters. For financial calculations, consider decimal libraries that avoid binary precision issues.

Example:

```js
console.log(0.1 + 0.2 === 0.3); // false
console.log(0.1 + 0.2); // 0.30000000000000004
console.log(Math.abs(0.1 + 0.2 - 0.3) < Number.EPSILON); // true

```

---

## Q8. 💡 `'5' + 3` and `'5' - 3` return values

`'5' + 3` returns `"53"` because `+` performs string concatenation when one operand is a string. `'5' - 3` returns `2` because `-` forces numeric conversion on both operands - all other arithmetic operators convert to numbers too, only `+` works with strings.

- **Trade-offs**: The `+` operator's dual nature (addition vs concatenation) requires careful type awareness to avoid bugs. This behavior makes string concatenation convenient but can cause bugs with mixed types - use template literals or explicit `Number()` conversion to avoid coercion surprises.

Example:

```js
console.log('5' + 3); // "53" (string concatenation)
console.log('5' - 3); // 2 (numeric subtraction)
console.log('5' * 3); // 15 (numeric multiplication)

```

---

---

## 📍 Navigation

<div align="center">

[Home: README](../README.md) • [Next: Functions & Execution Context →](02%29%20Functions%20%26%20Execution%20Context.md)

[📋 Cheatsheet](JavaScript%20Interview%20Cheatsheet.md)

</div>

---
