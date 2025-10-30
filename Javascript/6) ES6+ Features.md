# 🚀 6. ES6+ Features (Q66–75)

---

## 66) What are template literals?

Concept:
Template literals use backticks (`) instead of quotes and let you put variables and expressions directly inside strings.

Example:
```js
const name = 'Alice';
const msg = `Hello ${name}!
Today is ${new Date().toDateString()}`;
```

Deep Insight:
- **Core rule:** Use `${}` to put variables and expressions inside strings
- **Real-world use:** Building dynamic HTML, SQL queries, and API responses
- **Common mistake:** Forgetting backticks and using regular quotes
- **Advanced point:** Tagged templates let you process strings with custom functions
- **Interview tip:** Show the difference between template literals and string concatenation

---

## 67) What is destructuring assignment (object/array)?

Concept:
Destructuring lets you pull values out of objects and arrays and put them into variables in one line.

Example:
```js
const { name, age } = { name: 'Alice', age: 30 };
const [first, ...rest] = [1, 2, 3, 4];
const { data: user } = { data: { id: 1 } };
```

Deep Insight:
- **Core rule:** Use `{}` for objects and `[]` for arrays to extract values
- **Real-world use:** Function parameters, API responses, and configuration objects
- **Common mistake:** Forgetting to match the exact property names
- **Advanced point:** Use `...rest` to collect remaining items and `=` for default values
- **Interview tip:** Show how to rename variables with `{ oldName: newName }`

---

## 68) What are spread and rest operators?

Concept:
Spread (`...`) expands arrays and objects, while rest (`...`) collects remaining items into an array.

Example:
```js
const arr = [1, 2, 3];
const copy = [...arr];
const sum = (a, b, ...rest) => a + b + rest.reduce((s, n) => s + n, 0);
```

Deep Insight:
- **Core rule:** Spread expands things, rest collects remaining items
- **Real-world use:** Copying arrays, merging objects, and function parameters
- **Common mistake:** Using rest in the middle of function parameters
- **Advanced point:** Object spread creates new objects, useful for immutable updates
- **Interview tip:** Show how spread can pass array elements as separate arguments

---

## 69) What are default parameters?

Concept:
Default parameters give functions fallback values when you don't pass arguments or pass `undefined`.

Example:
```js
const greet = (name = 'World', greeting = 'Hello') => 
  `${greeting}, ${name}!`;
greet(); // "Hello, World!"
```

Deep Insight:
- **Core rule:** Default values only work when arguments are `undefined`, not `null` or `false`
- **Real-world use:** Making functions more flexible and easier to use
- **Common mistake:** Expecting defaults to work with `null` or `0`
- **Advanced point:** You can use previous parameters in default values
- **Interview tip:** Show how defaults make functions more user-friendly

---

## 70) What are ES modules (`import`/`export`)?

Concept:
ES modules let you split your code into separate files and import/export functions, classes, and variables between them.

Example:
```js
// math.js
export const add = (a, b) => a + b;
export default class Calculator {}

// main.js
import Calculator, { add } from './math.js';
```

Deep Insight:
- **Core rule:** Use `export` to share things and `import` to use them from other files
- **Real-world use:** Organizing large codebases and sharing code between projects
- **Common mistake:** Forgetting the `.js` extension in import paths
- **Advanced point:** Default exports are values, named exports are references
- **Interview tip:** Show the difference between default and named imports

---

## 71) What are generators and how do they work?

Concept:
Generators are special functions that can pause and resume, giving you one value at a time when you ask for it.

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

Deep Insight:
- **Core rule:** Use `function*` and `yield` to create generators that pause and resume
- **Real-world use:** Processing large datasets without loading everything into memory
- **Common mistake:** Forgetting to call `.next()` to get the next value
- **Advanced point:** Generators can receive values through `yield` expressions
- **Interview tip:** Show how generators create infinite sequences efficiently

---

## 72) What are async generators?

Concept:
Async generators combine generators with async/await, letting you yield promises and process them one at a time.

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

Deep Insight:
- **Core rule:** Use `async function*` to create generators that work with promises
- **Real-world use:** Streaming data from APIs and processing large datasets asynchronously
- **Common mistake:** Forgetting to use `for await` to consume async generators
- **Advanced point:** Great for handling backpressure and memory management
- **Interview tip:** Show how to process API data page by page

---

## 73) What are symbols and what are they used for?

Concept:
Symbols are unique values that you can use as object property keys to create truly private properties.

Example:
```js
const id = Symbol('id');
const obj = { [id]: 123, name: 'Alice' };
Object.keys(obj); // ['name'] - symbols hidden
```

Deep Insight:
- **Core rule:** Every symbol is unique, even if they have the same description
- **Real-world use:** Creating private object properties and special object behaviors
- **Common mistake:** Thinking symbols with the same description are equal
- **Advanced point:** `Symbol.iterator` lets you make objects work with `for...of` loops
- **Interview tip:** Show how symbols create truly private properties

---

## 74) What are Maps, Sets, WeakMaps, and WeakSets?

Concept:
Maps store key-value pairs with any keys, Sets store unique values, and Weak versions help with memory management.

Example:
```js
const map = new Map([['a', 1]]);
map.set('b', 2);
console.log(map.get('a')); // 1

const set = new Set([1, 2, 2, 3]);
console.log(set.size); // 3 (duplicates removed)
```

Deep Insight:
- **Core rule:** Maps use any keys, Sets keep unique values, Weak versions help with memory
- **Real-world use:** Maps for object keys, Sets for removing duplicates, Weak for cleanup
- **Common mistake:** Using objects as Maps when you need better key handling
- **Advanced point:** WeakMap keys must be objects and don't prevent garbage collection
- **Interview tip:** Show when to use each collection type

---

## 75) What are optional chaining (`?.`) and nullish coalescing (`??`)?

Concept:
Optional chaining (`?.`) safely accesses nested properties without errors, and nullish coalescing (`??`) provides fallbacks for null or undefined values.

Example:
```js
const user = { profile: { name: 'Alice' } };
const name = user?.profile?.name ?? 'Unknown';
const count = data?.items?.length ?? 0;
```

Deep Insight:
- **Core rule:** `?.` stops at null/undefined, `??` only checks null/undefined (not false or 0)
- **Real-world use:** Safely accessing API responses and optional object properties
- **Common mistake:** Using `??` when you want to check for falsy values
- **Advanced point:** Works with function calls like `obj?.method?.()`
- **Interview tip:** Show how these operators reduce verbose null checking
