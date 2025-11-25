# 4. ES6+ Features (Q46–55)

<div align="center">

**[← Previous: Objects, Prototypes & Inheritance](4%29%20Objects%2C%20Prototypes%20%26%20Inheritance.md)** | **[Next: Promises, Async-Await & Event Loop →](3%29%20Promises%2C%20Async-Await%20%26%20Event%20Loop.md)**

</div>

---

## Q46. Destructuring assignment

Destructuring allows you to pull values out of objects and arrays and put them into variables in one line - use `{}` for objects and `[]` for arrays. You can use `...rest` to collect remaining items and `=` for default values, and rename variables with `{ oldName: newName }` syntax.

- **Trade-offs**: The catch is forgetting to match the exact property names breaks destructuring - use default values to handle missing properties. It's perfect for function parameters, API responses, and configuration objects, but watch out for nested destructuring which can get complex.

Example:

```js
const { name, age } = { name: 'Alice', age: 30 };
const [first, ...rest] = [1, 2, 3, 4];
const { data: user } = { data: { id: 1 } };
```

---

## Q47. Spread operator: what it is and how to use it

Spread (`...`) expands arrays and objects, letting you copy arrays, merge objects, and pass array elements as separate arguments to functions. Object spread creates new objects, which is useful for immutable updates.

- **Trade-offs**: The catch is spread does shallow copies, so nested objects are still shared - use deep cloning if you need complete independence. It's great for copying arrays and merging objects, but watch out for performance with large arrays since it creates new arrays.

Example:

```js
const arr = [1, 2, 3];
const copy = [...arr];
const merged = { ...obj1, ...obj2 };
Math.max(...numbers);
```

---

## Q48. Rest parameter: what it is and how to use it

Rest (`...`) collects remaining function arguments into an array, letting you handle variable numbers of arguments cleanly. It must be the last parameter in a function signature.

- **Trade-offs**: The catch is using rest in the middle of function parameters - it must be last, or you'll get a syntax error. It's perfect for functions that need to handle variable arguments, but watch out for performance with many arguments since it creates an array.

Example:

```js
const sum = (a, b, ...rest) => a + b + rest.reduce((s, n) => s + n, 0);
const [first, ...rest] = [1, 2, 3, 4];
```

---

## Q49. Template literals: what they are and how to use them

Template literals use backticks (`) instead of quotes and let you put variables and expressions directly inside strings using `${}` syntax. They support multi-line strings and tagged templates let you process strings with custom functions.

- **Trade-offs**: The catch is forgetting backticks and using regular quotes breaks template literal syntax - always use backticks for template literals. They're perfect for building dynamic HTML, SQL queries, and API responses, but watch out for injection attacks when building queries or HTML.

Example:

```js
const name = 'Alice';
const msg = `Hello ${name}!
Today is ${new Date().toDateString()}`;
```

---

## Q50. `let` vs `const`

`let` allows reassignment, while `const` prevents reassignment but still allows you to mutate objects - so `const obj = { x: 1 }; obj.x = 2;` works, but `obj = {}` doesn't. Both are block-scoped and stay in a Temporal Dead Zone until declared.

- **Trade-offs**: The catch is `const` doesn't make objects immutable - it only prevents reassigning the variable itself. Use `const` by default and `let` only when you need to reassign - this makes code more predictable and easier to reason about.

Example:

```js
let a = 1; a = 2; // ok
const b = 1; b = 2; // error
const obj = { x: 1 }; obj.x = 2; // ok
```

---

## Q51. ES modules: what they are and how to use them

ES modules let you split your code into separate files and import/export functions, classes, and variables between them - use `export` to share things and `import` to use them. Default exports are values, named exports are references.

- **Trade-offs**: The catch is forgetting the `.js` extension in import paths can cause issues in some environments - always include the extension. They're perfect for organizing large codebases and sharing code between projects, but watch out for circular dependencies which can cause problems.

Example:

```js
// math.js
export const add = (a, b) => a + b;
export default class Calculator {}

// main.js
import Calculator, { add } from './math.js';
```

---

## Q52. Generators: what they are and how to use them

Generators are special functions that can pause and resume, giving you one value at a time when you ask for it - use `function*` and `yield` to create them. They're great for processing large datasets without loading everything into memory and creating infinite sequences efficiently.

- **Trade-offs**: The catch is forgetting to call `.next()` to get the next value - generators return iterator objects, not values directly. They're perfect for lazy evaluation and memory-efficient processing, but watch out for complexity - generators can be harder to understand than regular functions.

Example:

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

## Q53. Async generators

Async generators combine generators with async/await, letting you yield promises and process them one at a time - use `async function*` to create them. They're great for streaming data from APIs and processing large datasets asynchronously.

- **Trade-offs**: The catch is forgetting to use `for await` to consume async generators - regular `for...of` won't work. They're perfect for handling backpressure and memory management with async data, but watch out for error handling - errors in async generators need special handling.

Example:

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

## Q54. Symbols: what they are and how to use them

Symbols are unique values that you can use as object property keys to create truly private properties - every symbol is unique, even if they have the same description. They don't appear in `Object.keys()` or `for...in` loops, making them useful for hidden properties.

- **Trade-offs**: The catch is thinking symbols with the same description are equal - they're always unique, even with the same description. They're perfect for creating private object properties and special object behaviors like `Symbol.iterator` for making objects work with `for...of` loops, but watch out for debugging - symbols can be harder to inspect.

Example:

```js
const id = Symbol('id');
const obj = { [id]: 123, name: 'Alice' };
Object.keys(obj); // ['name'] - symbols hidden
```

---

## Q55. Maps, Sets, WeakMaps, and WeakSets

Maps store key-value pairs with any keys (including objects), Sets store unique values, and Weak versions help with memory management by allowing garbage collection of keys. Maps are better than objects when you need object keys or better key handling, Sets are great for removing duplicates.

- **Trade-offs**: The catch is using objects as Maps when you need better key handling - Maps support any key type and have better size tracking. WeakMap keys must be objects and don't prevent garbage collection, which is great for cleanup, but watch out - you can't iterate over WeakMaps or WeakSets, and they don't have a size property.

Example:

```js
const map = new Map([['a', 1]]);
map.set('b', 2);
console.log(map.get('a')); // 1

const set = new Set([1, 2, 2, 3]);
console.log(set.size); // 3 (duplicates removed)
```

---
<div align="center">

**[← Previous: Objects, Prototypes & Inheritance](4%29%20Objects%2C%20Prototypes%20%26%20Inheritance.md)** | **[Next: Promises, Async-Await & Event Loop →](3%29%20Promises%2C%20Async-Await%20%26%20Event%20Loop.md)**

</div>

**[← Previous Section](4%29%20Objects%2C%20Prototypes%20%26%20Inheritance.md)** | **[Next Section →](3%29%20Promises%2C%20Async-Await%20%26%20Event%20Loop.md)**
