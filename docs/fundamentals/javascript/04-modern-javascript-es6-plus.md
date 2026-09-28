---
sidebar_label: "Modern JavaScript (ES6+)"
---
# ⚡ 4. Modern JavaScript (ES6+) (Q44–53)

> **Reviewed:** 2026-09 · Modernized; legacy topics are labeled.

> **Modern baseline (2026):** Beyond ES6, interviewers expect you to know the everyday post-ES2015 additions, all of which are in the finished ECMAScript standard: optional chaining `?.` and nullish coalescing `??` (ES2020), logical assignment `??=`/`||=`/`&&=` (ES2021), `Array.prototype.at()` and top-level `await` in modules (ES2022), `findLast`/`findLastIndex` and the non-mutating `toSorted`/`toReversed`/`toSpliced`/`with` (ES2023), `Object.groupBy`/`Map.groupBy` and `Promise.withResolvers` (ES2024), and Set methods like `union`/`intersection` plus iterator helpers (ES2025). `structuredClone()` is a web/Node platform API (not ECMAScript) available in all modern browsers and Node 17+. **Temporal**, the long-awaited replacement for `Date`, is still a TC39 proposal (not yet in a finished edition of the spec) that has begun shipping in some engines - mention it as emerging and check current support or use the polyfill before relying on it.

---

## Q44. 💡 Destructuring assignment

Destructuring allows you to pull values out of objects and arrays and put them into variables in one line - use `{}` for objects and `[]` for arrays. You can use `...rest` to collect remaining items and `=` for default values, and rename variables with `{ oldName: newName }` syntax.

- **Trade-offs**: The catch is forgetting to match the exact property names breaks destructuring - use default values to handle missing properties. It's perfect for function parameters, API responses, and configuration objects, but watch out for nested destructuring which can get complex.

Example:

```js
// Object destructuring: extract properties into variables
const { name, age } = { name: 'Alice', age: 30 }; // name = 'Alice', age = 30

// Array destructuring: extract elements, rest collects remaining
const [first, ...rest] = [1, 2, 3, 4]; // first = 1, rest = [2, 3, 4]

// Renaming during destructuring: extract 'data' as 'user'
const { data: user } = { data: { id: 1 } }; // user = { id: 1 }

```

---

## Q45. ❓ Spread operator and how to use it

Spread (`...`) expands arrays and objects, letting you copy arrays, merge objects, and pass array elements as separate arguments to functions. Object spread creates new objects, which is useful for immutable updates.

- **Trade-offs**: The catch is spread does shallow copies, so nested objects are still shared - use `structuredClone()` if you need complete independence (it handles `Date`, `Map`, `Set`, and cycles, but not functions or DOM nodes). It's great for copying arrays and merging objects, but watch out for performance with large arrays since it creates new arrays.

Example:

```js
const arr = [1, 2, 3];
const copy = [...arr]; // Spread: create shallow copy of array
const merged = { ...obj1, ...obj2 }; // Spread: merge objects (obj2 properties override obj1)
Math.max(...numbers); // Spread: expand array as function arguments

```

---

## Q46. 🌐 Rest parameter and how to use it

Rest (`...`) collects remaining function arguments into an array, letting you handle variable numbers of arguments cleanly. It must be the last parameter in a function signature.

- **Trade-offs**: The catch is using rest in the middle of function parameters - it must be last, or you'll get a syntax error. It's perfect for functions that need to handle variable arguments, but watch out for performance with many arguments since it creates an array.

Example:

```js
// Rest parameter: collects remaining arguments into array
const sum = (a, b, ...rest) => a + b + rest.reduce((s, n) => s + n, 0); // rest = [3rd, 4th, ...args]

// Rest in destructuring: collects remaining array elements
const [first, ...rest] = [1, 2, 3, 4]; // first = 1, rest = [2, 3, 4]

```

---

## Q47. ❓ Template literals and how to use them

Template literals use backticks (`) instead of quotes and let you put variables and expressions directly inside strings using`${}` syntax. They support multi-line strings and tagged templates let you process strings with custom functions.

- **Trade-offs**: The catch is forgetting backticks and using regular quotes breaks template literal syntax - always use backticks for template literals. They're perfect for building dynamic HTML, SQL queries, and API responses, but watch out for injection attacks when building queries or HTML.

Example:

```js
const name = 'Alice';
// Template literal: backticks allow interpolation and multi-line strings
const msg = `Hello ${name}!
Today is ${new Date().toDateString()}`; // ${} evaluates expressions

```

---

## Q48. 📝 `let` vs `const`

`let` allows reassignment, while `const` prevents reassignment but still allows you to mutate objects - so `const obj = { x: 1 }; obj.x = 2;` works, but `obj = {}` doesn't. Both are block-scoped and stay in a Temporal Dead Zone until declared.

- **Trade-offs**: The catch is `const` doesn't make objects immutable - it only prevents reassigning the variable itself. Use `const` by default and `let` only when you need to reassign - this makes code more predictable and easier to reason about.

Example:

```js
let a = 1; a = 2; // ok - let allows reassignment
const b = 1; b = 2; // error - const prevents reassignment
const obj = { x: 1 }; obj.x = 2; // ok - const prevents reassignment, not mutation

```

---

## Q49. 🧩 ES modules and how to use them

ES modules (ESM) are the standard module system and the default choice in 2026 for browsers, Node.js, Deno, Bun, and every bundler. You use `export` to share things and `import` to use them. Imports are *live bindings* - if the exporting module later reassigns a named export, importers see the new value (the exception is `export default <expression>`, which exports the value computed at that moment). ESM is statically analyzable, which is what makes tree-shaking possible, and modules run in strict mode automatically.

Beyond static imports, modern ESM gives you **dynamic `import()`** (returns a promise - great for code-splitting and lazy loading) and **top-level `await`** (ES2022, only inside modules).

- **Trade-offs**: In browsers and native Node ESM you must write full specifiers including the `.js` extension; bundlers and TypeScript's `moduleResolution: "bundler"` let you omit it. Watch out for circular dependencies (you can hit a TDZ error reading a binding that hasn't been initialized yet), and remember top-level `await` blocks the evaluation of every module that imports that module.

Example:

```js
// math.js
export const add = (a, b) => a + b; // Named export
export default class Calculator {} // Default export

// main.js
import Calculator, { add } from './math.js'; // Import default and named exports

// Dynamic import: loaded on demand, returns a promise
const { format } = await import('./format.js'); // top-level await works in modules

// Metadata about the current module
console.log(import.meta.url);
```

> **Legacy note (2026):** CommonJS (`require()` / `module.exports`) is Node's original module system and still appears in older codebases and packages. Key differences: CommonJS loads synchronously and exports a copied value object, while ESM is async-capable and uses live bindings. For interop, ESM can `import` a CommonJS module (you get `module.exports` as the default export), and recent Node versions (22.12+/20.19+) can `require()` a synchronous ESM module. New code should use ESM (`"type": "module"` in `package.json` or `.mjs` files).

---

## Q50. ❓ Generators and how to use them

Generators are special functions that can pause and resume, giving you one value at a time when you ask for it - use `function*` and `yield` to create them. They're great for processing large datasets without loading everything into memory and creating infinite sequences efficiently.

- **Trade-offs**: The catch is forgetting to call `.next()` to get the next value - generators return iterator objects, not values directly. They're perfect for lazy evaluation and memory-efficient processing, but watch out for complexity - generators can be harder to understand than regular functions.

Example:

```js
// Generator function: can pause and resume execution
function* counter() {
  let i = 0;
  while (true) yield i++; // yield pauses, returns value, resumes on next()
}
const gen = counter(); // Returns iterator object
console.log(gen.next().value); // 0 - call next() to get next value
console.log(gen.next().value); // 1 - generator resumes from yield

```

---

## Q51. ⚡ Async generators

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

## Q52. ❓ Symbols and how to use them

Symbols are unique values that you can use as object property keys to avoid name collisions - every symbol is unique, even if they have the same description. They don't appear in `Object.keys()`, `JSON.stringify()`, or `for...in` loops, making them useful for "hidden" metadata properties.

- **Trade-offs**: The catch is thinking symbols with the same description are equal - they are always unique (unless you use the global registry `Symbol.for('key')`). Symbol keys are *not* truly private: `Object.getOwnPropertySymbols()` and `Reflect.ownKeys()` expose them. For real privacy use class `#private` fields. Symbols are perfect for collision-free keys and special object behaviors like `Symbol.iterator` for making objects work with `for...of` loops, but watch out for debugging - symbols can be harder to inspect.

Example:

```js
const id = Symbol('id');
const obj = { [id]: 123, name: 'Alice' };
Object.keys(obj); // ['name'] - symbols hidden

```

---

## Q53. 💡 Maps, Sets, WeakMaps, and WeakSets

Maps store key-value pairs with any keys (including objects), Sets store unique values, and Weak versions help with memory management by allowing garbage collection of keys. Maps are better than objects when you need object keys or better key handling, Sets are great for removing duplicates.

- **Trade-offs**: The catch is using objects as Maps when you need better key handling - Maps support any key type and have better size tracking. WeakMap keys must be objects and don't prevent garbage collection, which is great for cleanup, but watch out - you can't iterate over WeakMaps or WeakSets, and these don't have a size property.

Example:

```js
const map = new Map([['a', 1]]); // Map takes an iterable of [key, value] pairs
map.set('b', 2);
console.log(map.get('a')); // 1

const set = new Set([1, 2, 2, 3]);
console.log(set.size); // 3 (duplicates removed)

// ES2025 Set methods
new Set([1, 2]).union(new Set([2, 3])); // Set {1, 2, 3}
new Set([1, 2]).intersection(new Set([2, 3])); // Set {2}

```

---

