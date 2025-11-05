# 🚀 6. ES6+ Features (Q72–81)

---

## 72) What are template literals?

Template literals use backticks (`) instead of quotes and let you put variables and expressions directly inside strings.

```js
const name = 'Alice';
const msg = `Hello ${name}!
Today is ${new Date().toDateString()}`;
```

- **Core Rule**: Use `${}` to put variables and expressions inside strings
- **Real-World Use**: Building dynamic HTML, SQL queries, and API responses
- **Common Mistake**: Forgetting backticks and using regular quotes
- **Advanced Feature**: Tagged templates let you process strings with custom functions
- **Interview Tip**: Explain that show the difference between template literals and string concatenation

---

## 73) What is destructuring assignment (object/array)?

Destructuring lets you pull values out of objects and arrays and put them into variables in one line.

```js
const { name, age } = { name: 'Alice', age: 30 };
const [first, ...rest] = [1, 2, 3, 4];
const { data: user } = { data: { id: 1 } };
```

- **Core Rule**: Use `{}` for objects and `[]` for arrays to extract values
- **Real-World Use**: Function parameters, API responses, and configuration objects
- **Common Mistake**: Forgetting to match the exact property names
- **Advanced Feature**: Use `...rest` to collect remaining items and `=` for default values
- **Interview Tip**: Explain that show how to rename variables with `{ oldName: newName }`

---

## 74) What are spread and rest operators?

Spread (`...`) expands arrays and objects, while rest (`...`) collects remaining items into an array.

```js
const arr = [1, 2, 3];
const copy = [...arr];
const sum = (a, b, ...rest) => a + b + rest.reduce((s, n) => s + n, 0);
```

- **Core Rule**: Spread expands things, rest collects remaining items
- **Real-World Use**: Copying arrays, merging objects, and function parameters
- **Common Mistake**: Using rest in the middle of function parameters
- **Advanced Feature**: Object spread creates new objects, useful for immutable updates
- **Interview Tip**: Explain that show how spread can pass array elements as separate arguments

---

## 75) What are default parameters?

Default parameters give functions fallback values when you don't pass arguments or pass `undefined`.

```js
const greet = (name = 'World', greeting = 'Hello') => 
  `${greeting}, ${name}!`;
greet(); // "Hello, World!"
```

- **Core Rule**: Default values only work when arguments are `undefined`, not `null` or `false`
- **Real-World Use**: Making functions more flexible and easier to use
- **Common Mistake**: Expecting defaults to work with `null` or `0`
- **Advanced Feature**: You can use previous parameters in default values
- **Interview Tip**: Explain that show how defaults make functions more user-friendly

---

## 76) What are ES modules (`import`/`export`)?

ES modules let you split your code into separate files and import/export functions, classes, and variables between them.

```js
// math.js
export const add = (a, b) => a + b;
export default class Calculator {}

// main.js
import Calculator, { add } from './math.js';
```

- **Core Rule**: Use `export` to share things and `import` to use them from other files
- **Real-World Use**: Organizing large codebases and sharing code between projects
- **Common Mistake**: Forgetting the `.js` extension in import paths
- **Advanced Feature**: Default exports are values, named exports are references
- **Interview Tip**: Explain that show the difference between default and named imports

---

## 77) What are generators and how do they work?

Generators are special functions that can pause and resume, giving you one value at a time when you ask for it.

```js
function* counter() {
  let i = 0;
  while (true) yield i++;
}
const gen = counter();
console.log(gen.next().value); // 0
console.log(gen.next().value); // 1
```

- **Core Rule**: Use `function*` and `yield` to create generators that pause and resume
- **Real-World Use**: Processing large datasets without loading everything into memory
- **Common Mistake**: Forgetting to call `.next()` to get the next value
- **Advanced Feature**: Generators can receive values through `yield` expressions
- **Interview Tip**: Explain that show how generators create infinite sequences efficiently

---

## 78) What are async generators?

Async generators combine generators with async/await, letting you yield promises and process them one at a time.

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

- **Core Rule**: Use `async function*` to create generators that work with promises
- **Real-World Use**: Streaming data from APIs and processing large datasets asynchronously
- **Common Mistake**: Forgetting to use `for await` to consume async generators
- **Advanced Feature**: Great for handling backpressure and memory management
- **Interview Tip**: Explain that show how to process API data page by page

---

## 79) What are symbols and what are they used for?

Symbols are unique values that you can use as object property keys to create truly private properties.

```js
const id = Symbol('id');
const obj = { [id]: 123, name: 'Alice' };
Object.keys(obj); // ['name'] - symbols hidden
```

- **Core Rule**: Every symbol is unique, even if they have the same description
- **Real-World Use**: Creating private object properties and special object behaviors
- **Common Mistake**: Thinking symbols with the same description are equal
- **Advanced Feature**: `Symbol.iterator` lets you make objects work with `for...of` loops
- **Interview Tip**: Explain that show how symbols create truly private properties

---

## 80) What are Maps, Sets, WeakMaps, and WeakSets?

Maps store key-value pairs with any keys, Sets store unique values, and Weak versions help with memory management.

```js
const map = new Map([['a', 1]]);
map.set('b', 2);
console.log(map.get('a')); // 1

const set = new Set([1, 2, 2, 3]);
console.log(set.size); // 3 (duplicates removed)
```

- **Core Rule**: Maps use any keys, Sets keep unique values, Weak versions help with memory
- **Real-World Use**: Maps for object keys, Sets for removing duplicates, Weak for cleanup
- **Common Mistake**: Using objects as Maps when you need better key handling
- **Advanced Feature**: WeakMap keys must be objects and don't prevent garbage collection
- **Interview Tip**: Explain that show when to use each collection type

---

## 81) What are optional chaining (`?.`) and nullish coalescing (`??`)?

Optional chaining (`?.`) safely accesses nested properties without errors, and nullish coalescing (`??`) provides fallbacks for null or undefined values.

```js
const user = { profile: { name: 'Alice' } };
const name = user?.profile?.name ?? 'Unknown';
const count = data?.items?.length ?? 0;
```

- **Core Rule**: `?.` stops at null/undefined, `??` only checks null/undefined (not false or 0)
- **Real-World Use**: Safely accessing API responses and optional object properties
- **Common Mistake**: Using `??` when you want to check for falsy values
- **Advanced Feature**: Works with function calls like `obj?.method?.()`
- **Interview Tip**: Explain that show how these operators reduce verbose null checking

---
