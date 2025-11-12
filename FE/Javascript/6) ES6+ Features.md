# 🚀 6. ES6+ Features (Q72–81)

---

## 🧩 Q72. What are template literals?

### 🧠 Concept

Template literals use backticks (`) instead of quotes and let you put variables and expressions directly inside strings using `${}` syntax.

---

### 💡 Example

```js
const name = 'Alice';
const msg = `Hello ${name}!
Today is ${new Date().toDateString()}`;
```

---

### 🔍 Deep Insights

* **Rule:** Use `${}` to put variables and expressions inside strings.
* **Use Case:** Building dynamic HTML, SQL queries, and API responses.
* **Common Mistake:** Forgetting backticks and using regular quotes.
* **Pro Tip:** Tagged templates let you process strings with custom functions.

---

### ⭐ Senior Takeaway

Show the difference between template literals and string concatenation.

---

## 🧩 Q73. What is destructuring assignment (object/array)?

### 🧠 Concept

Destructuring lets you pull values out of objects and arrays and put them into variables in one line. Use `{}` for objects and `[]` for arrays.

---

### 💡 Example

```js
const { name, age } = { name: 'Alice', age: 30 };
const [first, ...rest] = [1, 2, 3, 4];
const { data: user } = { data: { id: 1 } };
```

---

### 🔍 Deep Insights

* **Rule:** Use `{}` for objects and `[]` for arrays to extract values.
* **Use Case:** Function parameters, API responses, and configuration objects.
* **Common Mistake:** Forgetting to match the exact property names.
* **Pro Tip:** Use `...rest` to collect remaining items and `=` for default values.

---

### ⭐ Senior Takeaway

Show how to rename variables with `{ oldName: newName }` syntax.

---

## 🧩 Q74. What are spread and rest operators?

### 🧠 Concept

Spread (`...`) expands arrays and objects, while rest (`...`) collects remaining items into an array. Spread expands things, rest collects remaining items.

---

### 💡 Example

```js
const arr = [1, 2, 3];
const copy = [...arr];
const sum = (a, b, ...rest) => a + b + rest.reduce((s, n) => s + n, 0);
```

---

### 🔍 Deep Insights

* **Rule:** Spread expands things, rest collects remaining items.
* **Use Case:** Copying arrays, merging objects, and function parameters.
* **Common Mistake:** Using rest in the middle of function parameters.
* **Pro Tip:** Object spread creates new objects, useful for immutable updates.

---

### ⭐ Senior Takeaway

Show how spread can pass array elements as separate arguments.

---

## 🧩 Q75. What are default parameters?

### 🧠 Concept

Default parameters give functions fallback values when you don't pass arguments or pass `undefined`. They make functions more flexible and easier to use.

---

### 💡 Example

```js
const greet = (name = 'World', greeting = 'Hello') => 
  `${greeting}, ${name}!`;
greet(); // "Hello, World!"
```

---

### 🔍 Deep Insights

* **Rule:** Default values only work when arguments are `undefined`, not `null` or `false`.
* **Use Case:** Making functions more flexible and easier to use.
* **Common Mistake:** Expecting defaults to work with `null` or `0`.
* **Pro Tip:** You can use previous parameters in default values.

---

### ⭐ Senior Takeaway

Show how defaults make functions more user-friendly with examples.

---

## 🧩 Q76. What are ES modules (`import`/`export`)?

### 🧠 Concept

ES modules let you split your code into separate files and import/export functions, classes, and variables between them. Use `export` to share things and `import` to use them.

---

### 💡 Example

```js
// math.js
export const add = (a, b) => a + b;
export default class Calculator {}

// main.js
import Calculator, { add } from './math.js';
```

---

### 🔍 Deep Insights

* **Rule:** Use `export` to share things and `import` to use them from other files.
* **Use Case:** Organizing large codebases and sharing code between projects.
* **Common Mistake:** Forgetting the `.js` extension in import paths.
* **Pro Tip:** Default exports are values, named exports are references.

---

### ⭐ Senior Takeaway

Show the difference between default and named imports to clarify usage.

---

## 🧩 Q77. What are generators and how do they work?

### 🧠 Concept

Generators are special functions that can pause and resume, giving you one value at a time when you ask for it. Use `function*` and `yield` to create them.

---

### 💡 Example

```js
function* counter() {
  let i = 0;
  while (true) yield i++;
}
const gen = counter();
console.log(gen.next().value); // 0
console.log(gen.next().value); // 1
```

---

### 🔍 Deep Insights

* **Rule:** Use `function*` and `yield` to create generators that pause and resume.
* **Use Case:** Processing large datasets without loading everything into memory.
* **Common Mistake:** Forgetting to call `.next()` to get the next value.
* **Pro Tip:** Generators can receive values through `yield` expressions.

---

### ⭐ Senior Takeaway

Show how generators create infinite sequences efficiently.

---

## 🧩 Q78. What are async generators?

### 🧠 Concept

Async generators combine generators with async/await, letting you yield promises and process them one at a time. Use `async function*` to create them.

---

### 💡 Example

```js
async function* fetchPages() {
  for (let i = 1; i <= 3; i++) {
    const data = await fetch(`/page/${i}`);
    yield data.json();
  }
}
for await (const page of fetchPages()) {
  console.log(page);
}
```

---

### 🔍 Deep Insights

* **Rule:** Use `async function*` to create generators that work with promises.
* **Use Case:** Streaming data from APIs and processing large datasets asynchronously.
* **Common Mistake:** Forgetting to use `for await` to consume async generators.
* **Pro Tip:** Great for handling backpressure and memory management.

---

### ⭐ Senior Takeaway

Show how to process API data page by page with async generators.

---

## 🧩 Q79. What are symbols and what are they used for?

### 🧠 Concept

Symbols are unique values that you can use as object property keys to create truly private properties. Every symbol is unique, even if they have the same description.

---

### 💡 Example

```js
const id = Symbol('id');
const obj = { [id]: 123, name: 'Alice' };
Object.keys(obj); // ['name'] - symbols hidden
```

---

### 🔍 Deep Insights

* **Rule:** Every symbol is unique, even if they have the same description.
* **Use Case:** Creating private object properties and special object behaviors.
* **Common Mistake:** Thinking symbols with the same description are equal.
* **Pro Tip:** `Symbol.iterator` lets you make objects work with `for...of` loops.

---

### ⭐ Senior Takeaway

Show how symbols create truly private properties that don't appear in iteration.

---

## 🧩 Q80. What are Maps, Sets, WeakMaps, and WeakSets?

### 🧠 Concept

Maps store key-value pairs with any keys, Sets store unique values, and Weak versions help with memory management. Each serves different purposes.

---

### 💡 Example

```js
const map = new Map([['a', 1]]);
map.set('b', 2);
console.log(map.get('a')); // 1

const set = new Set([1, 2, 2, 3]);
console.log(set.size); // 3 (duplicates removed)
```

---

### 🔍 Deep Insights

* **Rule:** Maps use any keys, Sets keep unique values, Weak versions help with memory.
* **Use Case:** Maps for object keys, Sets for removing duplicates, Weak for cleanup.
* **Common Mistake:** Using objects as Maps when you need better key handling.
* **Pro Tip:** WeakMap keys must be objects and don't prevent garbage collection.

---

### ⭐ Senior Takeaway

Show when to use each collection type based on your needs.

---

## 🧩 Q81. What are optional chaining (`?.`) and nullish coalescing (`??`)?

### 🧠 Concept

Optional chaining (`?.`) safely accesses nested properties without errors, and nullish coalescing (`??`) provides fallbacks for null or undefined values. They reduce verbose null checking.

---

### 💡 Example

```js
const user = { profile: { name: 'Alice' } };
const name = user?.profile?.name ?? 'Unknown';
const count = data?.items?.length ?? 0;
```

---

### 🔍 Deep Insights

* **Rule:** `?.` stops at null/undefined, `??` only checks null/undefined (not false or 0).
* **Use Case:** Safely accessing API responses and optional object properties.
* **Common Mistake:** Using `??` when you want to check for falsy values.
* **Pro Tip:** Works with function calls like `obj?.method?.()`.

---

### ⭐ Senior Takeaway

Show how these operators reduce verbose null checking in real code.

---
