### 🟢 1. JavaScript Fundamentals (Basics  Intermediate) — Q1-Q25

---

### 1️⃣ What is JavaScript and how is it different from Java?

**🧠 Concept**

JavaScript is a lightweight scripting language mainly used for web interactivity, while Java is a full-fledged, compiled, general-purpose programming language.

**💻 Example**
```js
// JavaScript Example
console.log("Hello from JavaScript!");
```

**💬 Explanation + Insight**

- **Interpreted Language** - JS is interpreted (JIT compiled), dynamically typed, runs in browser or Node.js
- **Compiled Language** - Java is compiled to bytecode, statically typed, runs on JVM
- **OOP Differences** - JS uses prototype-based OOP; Java uses class-based OOP
- **Event-driven** - JavaScript is single-threaded and event-driven
- **Performance** - JIT compilation makes JS nearly as fast as compiled languages

---

### 2️⃣ What are primitive and non-primitive data types in JavaScript?

**🧠 Concept**

Primitive types are immutable and stored by value. Non-primitives are objects stored by reference.

**💻 Example**
```js
// Primitives
let name = "Kamal";
let age = 31;
let isDev = true;

// Non-primitives
let user = { name: "Kamal" };
let arr = [1, 2, 3];
```

**💬 Explanation + Insight**

- **Primitive Types** - `string`, `number`, `boolean`, `undefined`, `null`, `symbol`, `bigint`
- **Non-Primitive Types** - `object`, `array`, `function`
- **Primitive Copying** - Copying primitives creates a new value
- **Object References** - Copying objects shares the same reference
- **Bug Prevention** - Understanding this helps avoid bugs when working with objects

---

### 3️⃣ What is the difference between `var`, `let`, and `const`?

**🧠 Concept**

`var` is function-scoped and can be re-declared. `let` is block-scoped and can be updated. `const` is block-scoped and cannot be updated.

**💻 Example**
```js
var x = 10;
let y = 20;
const z = 30;

x = 15; // ✅
y = 25; // ✅
z = 35; // ❌ Error
```

**💬 Explanation + Insight**

- **var Hoisting** - `var` is hoisted and initialized with `undefined`
- **let/const Hoisting** - `let` and `const` are hoisted but uninitialized (Temporal Dead Zone)
- **Best Practice** - Use `const` by default, `let` when you need to reassign
- **Avoid var** - Avoid `var` in modern JavaScript
- **Scope Understanding** - Understanding scope helps prevent bugs

---

### 4️⃣ What is hoisting in JavaScript?

**🧠 Concept**

Hoisting moves variable and function declarations to the top of their scope during compilation.

**💻 Example**
```js
console.log(a); // undefined (hoisted)
var a = 10;

sayHi(); // Works (function hoisted)
function sayHi() {
  console.log("Hi!");
}
```

**💬 Explanation + Insight**

- **Declaration Hoisting** - Only declarations are hoisted, not initializations
- **Function Hoisting** - Function declarations are fully hoisted; function expressions are not
- **TDZ (Temporal Dead Zone)** - `let`/`const` are hoisted but remain inaccessible until declared
- **Bug Prevention** - Understanding hoisting helps avoid bugs and write better code
- **Best Practice** - Declare variables at the top of their scope

---

### 5️⃣ What are truthy and falsy values?

**🧠 Concept**


Truthy values evaluate to `true` in Boolean context; falsy values evaluate to `false`.

**💻 Example**

```js
if ("Kamal") console.log("Truthy!"); // ✅
if (0) console.log("Falsy!"); // ❌
```

**💬 Explanation + Insight**


**Falsy values:**
`false`, `0`, `""`, `null`, `undefined`, `NaN`
Everything else is **truthy** (including `[]`, `{}`, `"0"`).

---

### 6️⃣ What is the difference between `==` and `===`?

**🧠 Concept**



* `==`  checks for **value equality** (performs type coercion).
* `===`  checks for **strict equality** (no type conversion).

**💻 Example**

```js
5 == "5";  // true
5 === "5"; // false
```

**💬 Explanation + Insight**


Use `===` almost always to avoid unexpected coercion:

```js
0 == false // true
0 === false // false
```

---

### 7️⃣ What are template literals?

**🧠 Concept**


Template literals allow embedding variables or expressions inside strings using backticks (`` ` ``).

**💻 Example**

```js
const name = "Kamal";
console.log(`Hello, ${name}!`);
```

**💬 Explanation + Insight**



* Introduced in ES6.
* Supports **multi-line strings** and **string interpolation**.
* Can also be used for **tagged templates** (advanced string processing).

---

### 8️⃣ What are default parameters in ES6?

**🧠 Concept**


Default parameters allow functions to have fallback values when no arguments are provided.

**💻 Example**

```js
function greet(name = "Guest") {
  console.log(`Hello, ${name}!`);
}
greet(); // Hello, Guest!
```

**💬 Explanation + Insight**



* Evaluated at call time (not definition).
* Can use expressions as defaults:

```js
function calc(x, y = x * 2) { return y; }
```

---

### 9️⃣ What is the `typeof` operator used for?

**🧠 Concept**


`typeof` checks the **data type** of a value.

**💻 Example**

```js
typeof "Kamal";  // "string"
typeof 42;       // "number"
typeof null;     // "object" 😅 (legacy bug)
```

**💬 Explanation + Insight**



* For arrays or `null`, use `Array.isArray()` or strict equality (`=== null`).
* Functions return `"function"`.
* Helps in runtime type checking.

---

### 🔟 What is NaN and how do you check for it?

**🧠 Concept**


`NaN` stands for “Not-a-Number” — it represents an invalid numeric result.

**💻 Example**

```js
let result = "abc" / 3; // NaN
console.log(isNaN(result)); // true
console.log(Number.isNaN(result)); // true
```

**💬 Explanation + Insight**



* `NaN` is the only value **not equal to itself** (`NaN !== NaN`).
* `isNaN()` coerces input before checking, `Number.isNaN()` is safer.
* Useful for validating numeric operations.

### 11️⃣ What is the difference between `undefined` and `null`?

**🧠 Concept**



* `undefined`  means a variable **has been declared but not assigned** a value.
* `null`  means a variable **intentionally has no value**.

**💻 Example**

```js
let a;
console.log(a); // undefined

let b = null;
console.log(b); // null
```

**💬 Explanation + Insight**



* `typeof undefined`  `"undefined"`
* `typeof null`  `"object"` (legacy JS bug)
* Use `undefined` for system-defined absence, `null` for developer-defined absence.

---

### 12️⃣ What are pass-by-value and pass-by-reference?

**🧠 Concept**



* **Primitive types** are passed **by value** (copied).
* **Objects and arrays** are passed **by reference** (points to the same memory).

**💻 Example**

```js
let x = 10;
let y = x;
y = 20;
console.log(x); // 10 ✅

let obj1 = { name: "Kamal" };
let obj2 = obj1;
obj2.name = "John";
console.log(obj1.name); // John 😅 (same reference)
```

**💬 Explanation + Insight**



* “Pass-by-reference” in JS technically means **object references are copied by value**.
* To prevent mutations  use shallow or deep copy.

---

### 13️⃣ What is scope in JavaScript?

**🧠 Concept**


Scope defines where variables are accessible.

**💻 Example**

```js
let a = 10; // global scope
function test() {
  let b = 20; // local scope
  console.log(a, b);
}
test();
```

**💬 Explanation + Insight**



* Types: **Global**, **Function**, **Block**
* Introduced in ES6: `let` and `const`  block scope
* Determines variable **visibility and lifetime**.

---

### 14️⃣ What is the difference between global and block scope?

**🧠 Concept**



* **Global scope**: Accessible everywhere.
* **Block scope**: Accessible only within `{}` braces.

**💻 Example**

```js
let x = 1; // global
{
  let y = 2; // block scope
}
console.log(x); // 1
console.log(y); // ❌ ReferenceError
```

**💬 Explanation + Insight**



* `var` is **function-scoped**, not block-scoped.
* Always use `let` or `const` to avoid scope pollution.

---

### 15️⃣ What are Immediately Invoked Function Expressions (IIFEs)?

**🧠 Concept**


An IIFE runs immediately after it’s defined — often used to create private scope.

**💻 Example**

```js
(function() {
  console.log("IIFE executed!");
})();
```

**💬 Explanation + Insight**



* Used to **avoid polluting the global scope**.
* Common in older JS patterns before ES6 modules.
* Can also be async:

```js
(async () => {
  await fetchData();
})();
```

---

### 16️⃣ What are arrow functions and how do they differ from regular functions?

**🧠 Concept**


Arrow functions are a shorter syntax for writing functions and **don’t bind their own `this`**.

**💻 Example**

```js
const greet = name => `Hello, ${name}!`;
console.log(greet("Kamal"));
```

**💬 Explanation + Insight**



* Don’t have their own `this`, `arguments`, or `prototype`.
* Always **lexically bind** `this` (inherits from outer scope).
* Perfect for callbacks, not for methods or constructors.

---

### 17️⃣ What is destructuring assignment and when should you use it?

**🧠 Concept**


Destructuring allows unpacking values from arrays or objects into variables easily.

**💻 Example**

```js
const user = { name: "Kamal", age: 31 };
const { name, age } = user;
console.log(name, age);

const [a, b] = [1, 2];
```

**💬 Explanation + Insight**



* Makes code **concise** and **readable**.
* Can set **default values**:

```js
const { city = "Unknown" } = user;
```

* Useful in React hooks and function arguments.

---

### 18️⃣ What are spread and rest operators?

**🧠 Concept**



* **Spread (`...`)**  expands an array/object.
* **Rest (`...`)**  collects multiple arguments into an array.

**💻 Example**

```js
// Spread
const nums = [1, 2, 3];
console.log([...nums, 4, 5]);

// Rest
function sum(...args) {
  return args.reduce((a, b) => a + b, 0);
}
console.log(sum(1, 2, 3)); // 6
```

**💬 Explanation + Insight**



* Spread works with **iterables**.
* Rest works with **function parameters** or **destructuring**.
* Makes merging, copying, and variadic functions easier.

---

### 19️⃣ What is the difference between shallow and deep copies in JS?

**🧠 Concept**



* **Shallow copy**  copies only one level of an object.
* **Deep copy**  copies nested objects completely.

**💻 Example**

```js
const obj = { user: { name: "Kamal" } };
const shallow = { ...obj };
const deep = structuredClone(obj);

shallow.user.name = "John";
console.log(obj.user.name); // "John" 😅
console.log(deep.user.name); // "Kamal" ✅
```

**💬 Explanation + Insight**



* Shallow copy: `Object.assign()`, spread (`...`)
* Deep copy: `structuredClone()`, `JSON.parse(JSON.stringify())`, or libraries like Lodash.
* Deep copy ensures **data immutability**.

---

### 20️⃣ How does JavaScript handle type coercion?

**🧠 Concept**


Type coercion means JS **automatically converts types** to perform operations.

**💻 Example**

```js
console.log("5" - 2); // 3 (string  number)
console.log("5" + 2); // "52" (number  string)
```

**💬 Explanation + Insight**



* Happens in **comparison** and **arithmetic**.
* `==` triggers coercion; `===` avoids it.
* Always be aware of **implicit conversions** — they can lead to bugs.

### 21️⃣ What are Symbols in ES6?

**🧠 Concept**


A `Symbol` is a unique and immutable primitive value introduced in ES6, used mainly as object property keys to avoid naming conflicts.

**💻 Example**

```js
const id = Symbol("id");
const user = {
  name: "Kamal",
  [id]: 101
};
console.log(user[id]); // 101
```

**💬 Explanation + Insight**



* Every `Symbol()` is unique — even if they have the same description.
* Not enumerable in `for...in` or `Object.keys()`.
* Useful for creating **private-like** object keys or internal identifiers (used in JS internals like `Symbol.iterator`, `Symbol.toStringTag`).

---

### 22️⃣ What is the difference between mutable and immutable data types?

**🧠 Concept**



* **Mutable**  can be changed after creation (e.g., objects, arrays).
* **Immutable**  cannot be changed; new value replaces old (e.g., strings, numbers).

**💻 Example**

```js
let name = "Kamal";
name[0] = "B";
console.log(name); // still "Kamal" ❌ not "Bamal"

let arr = [1, 2];
arr.push(3);
console.log(arr); // [1, 2, 3] ✅ mutable
```

**💬 Explanation + Insight**



* Strings and numbers are **immutable**.
* Objects and arrays are **mutable** by default.
* Immutability helps with **predictability** and **state management** (React, Redux, etc.).

---

### 23️⃣ What are Tagged Template Literals?

**🧠 Concept**


Tagged templates let you **process template literals with a custom function** before returning a value.

**💻 Example**

```js
function highlight(strings, ...values) {
  return strings.map((s, i) => `${s}<b>${values[i] || ""}</b>`).join("");
}

const name = "Kamal";
const age = 31;
console.log(highlight`My name is ${name} and I am ${age}.`);
```

**💬 Explanation + Insight**



* The tag function receives the raw strings and values separately.
* Used for **custom formatting**, **i18n (internationalization)**, or **XSS-safe HTML rendering**.
* It doesn’t just concatenate strings — it gives **control over interpolation**.

---

### 24️⃣ What is a module in ES6?

**🧠 Concept**


A module is a **separate file that exports or imports values**, promoting reusability and maintainability.

**💻 Example**
`math.js`

```js
export const add = (a, b) => a + b;
```

`main.js`

```js
import { add } from "./math.js";
console.log(add(2, 3)); // 5
```

**💬 Explanation + Insight**



* Each module has its own **scope** (no pollution of globals).
* `import` and `export` are **static**, enabling tree shaking.
* Modules are **deferred by default** when used with `<script type="module">`.

---

### 25️⃣ What are named vs default exports?

**🧠 Concept**



* **Named export**  allows exporting multiple values by name.
* **Default export**  allows exporting a single main value per module.

**💻 Example**
`utils.js`

```js
export const greet = () => "Hello!";
export default function sayBye() { return "Goodbye!"; }
```

`main.js`

```js
import sayBye, { greet } from "./utils.js";
console.log(greet()); // Hello!
console.log(sayBye()); // Goodbye!
```

**💬 Explanation + Insight**



* You can have **only one default export** per file.
* Named exports must be imported using `{}` and exact names.
* Default exports can be imported with any name.

---

## ⚠️ Interview Gotchas & Quick Tips (Fundamentals)

1. 🧩 **Gotcha:**

   ```js
   typeof null; // "object"
   ```

    Legacy bug in JS since 1995 — still kept for backward compatibility.

2. ⚔️ **Tricky Comparison:**

   ```js
   [] == ![]; // true 🤯
   ```

   * `![]`  `false`
   * `[] == false`  `true` (due to coercion)

3. 🔄 **NaN trap:**
   `NaN === NaN`  `false`
   Always check with `Number.isNaN()`.

4. 🧠 **Default Parameter Behavior:**
   Default values are **evaluated at call time**, not definition time.

5. 🧰 **const ≠ immutable:**
   You can still mutate a const object:

   ```js
   const obj = { a: 1 };
   obj.a = 2; // ✅ works
   ```

6. 🕳️ **TDZ (Temporal Dead Zone):**
   Accessing `let`/`const` before declaration  `ReferenceError`.

7. 🧵 **Hoisting confusion:**
   Function declarations are hoisted *completely*,
   but arrow/function expressions are not:

   ```js
   sayHi(); // Works
   greet(); // ❌ Error

   function sayHi() {}
   const greet = () => {};
   ```

8. 🪄 **Implicit type coercion traps:**

   ```js
   [] + [] // ""
   [] + {} // "[object Object]"
   {} + [] // 0
   ```

9. 🧩 **`this` in Arrow vs Regular:**
   Arrow  lexically bound
   Regular  dynamically bound at call time

10. 🧱 **Object immutability:**
    Use `Object.freeze(obj)` for shallow immutability,
    or `structuredClone()` for deep cloning.
