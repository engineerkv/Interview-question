# 🧩 ES6+ Features & Modern JavaScript — Q86-Q105

---

## 🕓 JavaScript Evolution Timeline (ES6  ES13)

| ECMAScript Version            | Year | Major Features Introduced                                                                                                                                |
| ----------------------------- | ---- | -------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **ES6 (ES2015)**              | 2015 | `let`, `const`, arrow functions, classes, template literals, destructuring, default params, spread/rest, Promises, modules, generators, symbols, Map/Set |
| **ES7 (ES2016)**              | 2016 | Exponentiation operator `**`, `Array.prototype.includes()`                                                                                               |
| **ES8 (ES2017)**              | 2017 | `async/await`, `Object.values()`, `Object.entries()`, `String.padStart/End`, shared memory & atomics                                                     |
| **ES9 (ES2018)**              | 2018 | Rest/spread for objects, async iteration, Promise.finally(), RegExp improvements                                                                         |
| **ES10 (ES2019)**             | 2019 | `Array.flat()`, `flatMap()`, `Object.fromEntries()`, optional catch binding, trimStart/trimEnd                                                           |
| **ES11 (ES2020)**             | 2020 | `BigInt`, `globalThis`, `nullish coalescing (??)`, `optional chaining (?.)`, `Promise.allSettled()`, dynamic `import()`, private fields in classes       |
| **ES12 (ES2021)**             | 2021 | `String.replaceAll()`, `Promise.any()`, `WeakRefs`, `Logical assignment (??=, ||=, &&=)`, numeric separators |
| **ES13 (ES2022)**             | 2022 | Top-level `await`, class static blocks, ergonomic brand checks (`#private in obj`), `Array.prototype.at()`, temporal proposal (stage 3)                  |
| **ES14 (Upcoming / Stage 3)** | 2025 | Pattern matching, pipeline operator (`|>`), decorators, new Date/Time API (`Temporal`) |

---

## 1️⃣ What is the spread syntax and how does it differ from `Object.assign()`?

**🧠 Concept**

Spread (`...`) **expands** elements from arrays or objects. `Object.assign()` **copies** properties from source objects into a target object.

**💻 Example**

```js
// Spread syntax
const arr1 = [1, 2, 3];
const arr2 = [...arr1, 4, 5]; // [1, 2, 3, 4, 5]

const obj1 = { a: 1, b: 2 };
const obj2 = { ...obj1, c: 3 }; // { a: 1, b: 2, c: 3 }

// Object.assign()
const obj3 = Object.assign({}, obj1, { c: 3 });
```

**💬 Explanation + Insight**

- **Spread is more readable** - Cleaner syntax for copying/merging
- **Object.assign() is older** - ES5 method, still widely used
- **Performance difference** - Spread is generally faster
- **Shallow copying** - Both create shallow copies
- **Array vs Object** - Spread works with both, Object.assign() only objects

---

## 2️⃣ What are arrow functions and when should you use them?

**🧠 Concept**

Arrow functions are a concise way to write functions with lexical `this` binding and no `arguments` object.

**💻 Example**

```js
// Traditional function
function add(a, b) {
  return a + b;
}

// Arrow function
const add = (a, b) => a + b;

// Arrow function with block
const add = (a, b) => {
  return a + b;
};
```

**💬 Explanation + Insight**

- **Lexical `this`** - `this` is bound to the enclosing scope
- **No `arguments`** - Use rest parameters instead
- **Cannot be constructors** - No `new` keyword
- **Implicit return** - Single expression returns automatically
- **Use cases** - Callbacks, array methods, short functions

---

## 3️⃣ What is destructuring and how do you use it?

**🧠 Concept**

Destructuring allows you to extract values from arrays or properties from objects into distinct variables.

**💻 Example**

```js
// Array destructuring
const [first, second, ...rest] = [1, 2, 3, 4, 5];

// Object destructuring
const { name, age, city = 'Unknown' } = { name: 'John', age: 30 };

// Nested destructuring
const { user: { name, email } } = { user: { name: 'John', email: 'john@example.com' } };
```

**💬 Explanation + Insight**

- **Array destructuring** - Extract values by position
- **Object destructuring** - Extract values by property name
- **Default values** - Provide fallback values
- **Rest operator** - Capture remaining elements
- **Nested destructuring** - Extract from nested structures

---

## 4️⃣ What are template literals and tagged templates?

**🧠 Concept**

Template literals are string literals that allow embedded expressions and tagged templates are functions that process template literals.

**💻 Example**

```js
// Template literals
const name = 'John';
const age = 30;
const message = `Hello, ${name}! You are ${age} years old.`;

// Tagged templates
function highlight(strings, ...values) {
  return strings.reduce((result, string, i) => {
    return result + string + (values[i] ? `<mark>${values[i]}</mark>` : '');
  }, '');
}

const result = highlight`Hello ${name}!`;
```

**💬 Explanation + Insight**

- **Embedded expressions** - Use `${}` for variables and expressions
- **Multiline strings** - No need for `\n` or concatenation
- **Tagged templates** - Custom processing of template literals
- **Raw strings** - Access to raw string content
- **Use cases** - SQL queries, HTML templates, internationalization

---

## 5️⃣ What are default parameters and how do they work?

**🧠 Concept**

Default parameters allow you to specify default values for function parameters when they are undefined.

**💻 Example**

```js
// Default parameters
function greet(name = 'World', greeting = 'Hello') {
  return `${greeting}, ${name}!`;
}

// Default parameters with expressions
function createUser(name, age = 18, isActive = true) {
  return { name, age, isActive };
}

// Default parameters with function calls
function log(message, timestamp = new Date().toISOString()) {
  console.log(`[${timestamp}] ${message}`);
}
```

**💬 Explanation + Insight**

- **Undefined check** - Defaults apply when parameter is `undefined`
- **Expression evaluation** - Defaults are evaluated each time
- **Left-to-right** - Later parameters can reference earlier ones
- **Function calls** - Defaults can be function calls
- **Use cases** - Optional parameters, configuration objects

---

## 6️⃣ What is the rest operator and how does it work?

**🧠 Concept**

The rest operator (`...`) collects remaining elements into an array, used in function parameters and destructuring.

**💻 Example**

```js
// Rest in function parameters
function sum(...numbers) {
  return numbers.reduce((total, num) => total + num, 0);
}

// Rest in destructuring
const [first, ...rest] = [1, 2, 3, 4, 5];

// Rest in object destructuring
const { name, ...otherProps } = { name: 'John', age: 30, city: 'NYC' };
```

**💬 Explanation + Insight**

- **Collects remaining elements** - Gathers all remaining items
- **Always an array** - Rest parameter is always an array
- **Must be last** - Rest parameter must be the last parameter
- **Use cases** - Variable number of arguments, array methods
- **Performance** - More efficient than `arguments` object

---

## 7️⃣ What are Promises and how do they work?

**🧠 Concept**

Promises represent the eventual completion or failure of an asynchronous operation, providing a cleaner alternative to callbacks.

**💻 Example**

```js
// Creating a Promise
const fetchData = () => {
  return new Promise((resolve, reject) => {
    setTimeout(() => {
      resolve('Data fetched successfully');
    }, 1000);
  });
};

// Using Promises
fetchData()
  .then(result => console.log(result))
  .catch(error => console.error(error));
```

**💬 Explanation + Insight**

- **Three states** - Pending, fulfilled, rejected
- **Chainable** - `.then()` returns a new Promise
- **Error handling** - Use `.catch()` for error handling
- **Always asynchronous** - Even if resolved immediately
- **Use cases** - API calls, file operations, timers

---

## 8️⃣ What is async/await and how does it work?

**🧠 Concept**

Async/await provides a cleaner way to work with Promises, making asynchronous code look and behave like synchronous code.

**💻 Example**

```js
// Async function
async function fetchUserData(userId) {
  try {
    const response = await fetch(`/api/users/${userId}`);
    const user = await response.json();
    return user;
  } catch (error) {
    console.error('Error fetching user:', error);
    throw error;
  }
}

// Using async/await
const user = await fetchUserData(123);
```

**💬 Explanation + Insight**

- **Syntactic sugar** - Makes Promises easier to work with
- **Error handling** - Use try/catch for error handling
- **Sequential execution** - Code executes in order
- **Always returns Promise** - Async functions always return Promises
- **Use cases** - API calls, database operations, file handling

---

## 9️⃣ What are classes and how do they work in JavaScript?

**🧠 Concept**

Classes are syntactic sugar over JavaScript's prototype-based inheritance, providing a cleaner way to create objects and handle inheritance.

**💻 Example**

```js
// Class definition
class Person {
  constructor(name, age) {
    this.name = name;
    this.age = age;
  }
  
  greet() {
    return `Hello, I'm ${this.name}`;
  }
}

// Inheritance
class Student extends Person {
  constructor(name, age, grade) {
    super(name, age);
    this.grade = grade;
  }
}
```

**💬 Explanation + Insight**

- **Syntactic sugar** - Classes are functions under the hood
- **Constructor** - Special method for object initialization
- **Inheritance** - Use `extends` for inheritance
- **Super keyword** - Call parent class methods
- **Use cases** - Object-oriented programming, component libraries

---

## 🔟 What are modules and how do you use them?

**🧠 Concept**

Modules allow you to split code into separate files and import/export functionality between them.

**💻 Example**

```js
// math.js - Export
export const add = (a, b) => a + b;
export const subtract = (a, b) => a - b;

// main.js - Import
import { add, subtract } from './math.js';
import * as math from './math.js';

// Default export
export default class Calculator {
  add(a, b) { return a + b; }
}
```

**💬 Explanation + Insight**

- **Named exports** - Export specific functions/variables
- **Default exports** - Export one main thing per module
- **Import/Export** - Use `import` and `export` keywords
- **Tree shaking** - Unused exports can be removed
- **Use cases** - Code organization, reusability, maintainability

---

*This comprehensive ES6+ features section covers essential modern JavaScript concepts including spread syntax, arrow functions, destructuring, template literals, Promises, async/await, classes, and modules for modern JavaScript development.*