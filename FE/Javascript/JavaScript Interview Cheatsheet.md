# 🚀 JavaScript Interview Cheatsheet

> **Quick Reference Guide** - Essential JavaScript concepts, syntax, and patterns for interviews

---

## 📋 **Table of Contents**

- [Core Concepts](#-core-concepts)
- [Data Types & Variables](#-data-types--variables)
- [Functions & Scope](#-functions--scope)
- [Objects & Prototypes](#-objects--prototypes)
- [Promises & Async](#-promises--async)
- [ES6+ Features](#-es6-features)
- [Common Patterns](#-common-patterns)
- [Performance Tips](#-performance-tips)
- [Interview Keywords](#-interview-keywords)

---

## 🧠 **Core Concepts**

### **Hoisting**
```js
// var: hoisted as undefined
console.log(x); // undefined
var x = 1;

// let/const: hoisted but in TDZ
console.log(y); // ReferenceError
let y = 2;
```

### **Closure**
```js
function outer(x) {
  return function inner(y) {
    return x + y; // x is "closed over"
  };
}
const add5 = outer(5);
add5(3); // 8
```

### **`this` Binding**
```js
// Method call: this = object
obj.method(); // this = obj

// Arrow function: lexical this
const arrow = () => this; // this from outer scope

// bind/call/apply: explicit this
fn.call(context, args);
```

---

## 📊 **Data Types & Variables**

### **Primitives vs Objects**
```js
// Primitives (immutable)
let a = 1;
let b = a; // copy
a = 2; // b still 1

// Objects (mutable)
let obj1 = { x: 1 };
let obj2 = obj1; // reference
obj1.x = 2; // obj2.x is also 2
```

### **Type Checking**
```js
typeof null; // "object" (bug)
typeof undefined; // "undefined"
Array.isArray([]); // true
Object.prototype.toString.call([]); // "[object Array]"
```

### **Variable Declarations**
```js
var x = 1; // function-scoped, hoisted
let y = 2; // block-scoped, TDZ
const z = 3; // block-scoped, immutable binding
```

---

## 🔧 **Functions & Scope**

### **Function Types**
```js
// Declaration (hoisted)
function fn() { return 1; }

// Expression
const fn = function() { return 1; };

// Arrow (lexical this)
const fn = () => 1;

// IIFE
(function() { return 1; })();
```

### **Scope Chain**
```js
let global = 1;
function outer() {
  let outer = 2;
  function inner() {
    let inner = 3;
    return global + outer + inner; // 6
  }
  return inner();
}
```

### **Currying**
```js
const curry = fn => (...args) =>
  args.length >= fn.length ? fn(...args) : (...more) => curry(fn)(...args, ...more);

const add = (a, b, c) => a + b + c;
curry(add)(1)(2)(3); // 6
```

---

## 🏗️ **Objects & Prototypes**

### **Prototype Chain**
```js
const obj = {};
obj.__proto__ === Object.prototype; // true
Object.getPrototypeOf(obj) === Object.prototype; // true
```

### **Inheritance**
```js
// ES6 Classes
class Parent { constructor(x) { this.x = x; } }
class Child extends Parent {
  constructor(x, y) {
    super(x);
    this.y = y;
  }
}

// Object.create
const child = Object.create(parent);
```

### **Property Access**
```js
// Own vs inherited
obj.hasOwnProperty('prop'); // own only
'prop' in obj; // own + inherited
Object.hasOwn(obj, 'prop'); // safer own check
```

---

## ⚡ **Promises & Async**

### **Promise Basics**
```js
const promise = new Promise((resolve, reject) => {
  if (success) resolve(value);
  else reject(error);
});

promise
  .then(value => console.log(value))
  .catch(error => console.error(error))
  .finally(() => console.log('done'));
```

### **Async/Await**
```js
async function fetchData() {
  try {
    const response = await fetch('/api/data');
    const data = await response.json();
    return data;
  } catch (error) {
    console.error(error);
  }
}
```

### **Promise Combinators**
```js
// All must succeed
Promise.all([p1, p2, p3]);

// Wait for all (success or failure)
Promise.allSettled([p1, p2, p3]);

// First to complete
Promise.race([p1, p2, p3]);

// First to succeed
Promise.any([p1, p2, p3]);
```

---

## 🚀 **ES6+ Features**

### **Destructuring**
```js
// Object
const { name, age } = person;
const { name: fullName } = person;

// Array
const [first, second, ...rest] = array;
```

### **Spread & Rest**
```js
// Spread
const newArray = [...oldArray];
const newObj = { ...oldObj, newProp: value };

// Rest
function fn(a, b, ...rest) { }
```

### **Template Literals**
```js
const name = 'World';
const greeting = `Hello ${name}!`;
const multiline = `
  Line 1
  Line 2
`;
```

### **Modules**
```js
// Export
export const name = 'value';
export default function() { }

// Import
import { name } from './module.js';
import defaultExport from './module.js';
```

---

## 🎯 **Common Patterns**

### **Debounce**
```js
const debounce = (fn, delay) => {
  let timeoutId;
  return (...args) => {
    clearTimeout(timeoutId);
    timeoutId = setTimeout(() => fn(...args), delay);
  };
};
```

### **Throttle**
```js
const throttle = (fn, delay) => {
  let lastCall = 0;
  return (...args) => {
    const now = Date.now();
    if (now - lastCall >= delay) {
      lastCall = now;
      fn(...args);
    }
  };
};
```

### **Memoization**
```js
const memoize = fn => {
  const cache = new Map();
  return (...args) => {
    const key = JSON.stringify(args);
    if (cache.has(key)) return cache.get(key);
    const result = fn(...args);
    cache.set(key, result);
    return result;
  };
};
```

### **Event Emitter**
```js
class EventEmitter {
  constructor() { this.events = {}; }
  on(event, fn) { (this.events[event] ||= []).push(fn); }
  emit(event, data) { (this.events[event] || []).forEach(fn => fn(data)); }
  off(event, fn) { this.events[event] = (this.events[event] || []).filter(f => f !== fn); }
}
```

---

## ⚡ **Performance Tips**

### **Memory Management**
```js
// Avoid memory leaks
element.removeEventListener('click', handler);
clearInterval(intervalId);
weakMap.set(obj, value); // WeakMap for cleanup
```

### **Optimization**
```js
// Use const/let over var
const arr = []; // not var arr = [];

// Cache DOM queries
const element = document.getElementById('id');

// Use document fragments for DOM manipulation
const fragment = document.createDocumentFragment();
```

### **Async Patterns**
```js
// Parallel execution
const [a, b] = await Promise.all([fetchA(), fetchB()]);

// Sequential when needed
for (const item of items) {
  await processItem(item);
}
```

---

## 🧩 **V8 Internals (Quick View)**

### **Execution Pipeline**
```text
Source → Parser (AST) → Ignition (Bytecode) → TurboFan (Optimized Machine Code) → GC (Orinoco)
```

### **Simple Code Flow**
```js
function add(a, b) { return a + b; }
add(2, 3); // Parse → Bytecode → Execute → (maybe optimize)
```

### **Fetch Flow (who does what?)**
```text
V8: runs JS, creates/manages Promises, microtasks
Blink: handles fetch network request, returns result back to V8
```

Key Notes:
- Ignition = fast startup; TurboFan = hot-path performance
- Type feedback + hidden classes + inline caches boost speed
- GC is incremental/parallel to minimize pauses

---

## ⚙️ **V8 Engine Internals: Deep Dive**

Excellent 👏 — this is one of the most powerful topics for a senior front-end or system design interview: "How does V8 work internally?"

Let's go deep — beyond the surface — into V8's internal architecture, from parsing → bytecode → execution → optimization → garbage collection.

### 🧠 1️⃣ Parsing Stage (Code → AST)
- V8 starts with raw JS source code (plain text).
- Parser breaks it into tokens (keywords, identifiers, symbols, etc.).
- Parser runs syntactic analysis to form a tree structure (AST) that describes the program's hierarchy and relationships.

```text
JS: let x = 2 + 3;
Tokens: LET, IDENTIFIER(x), ASSIGN, NUMBER(2), PLUS, NUMBER(3)
AST: root → VariableDeclaration → Identifier(x) → BinaryExpression(2 + 3)
```

### 🧩 2️⃣ Bytecode Generation (Ignition Interpreter)
- V8's Ignition Interpreter reads the AST and generates bytecode instructions.
- Bytecode is like assembly — it tells V8 what operations to perform step-by-step.

```text
JS: let x = 2 + 3;
Bytecode:
  LdaSmi [2]
  AddSmi [3]
  StaGlobal [x]
```

### ⚙️ 3️⃣ Execution (Ignition Interpreter Runs Bytecode)
- Ignition maintains a call stack and executes bytecode instructions sequentially.
- Uses registers and a stack-based virtual machine model to manage data.
- During execution, Ignition collects profiling data (how often functions are called, what data types are used, which branches are taken).

### 🚀 4️⃣ Optimization (TurboFan JIT Compiler)
- When Ignition sees that a function runs repeatedly ("hot"), it sends that function and its profiling data to TurboFan.
- TurboFan (JIT compiler) translates bytecode → optimized native machine code (x86, ARM, etc.).
- Uses type feedback and hidden classes to make optimizations:
  - Inline caching: assumes object properties will stay consistent
  - Type specialization: assumes a variable keeps the same type
  - Inlining: merges small functions into callers for speed

### ⚡ 5️⃣ Execution of Optimized Code
- Once compiled, TurboFan's code is stored in V8's code cache.
- Future calls to that function execute machine code directly — skipping the interpreter.
- This gives near-native performance.

### 🧹 6️⃣ Garbage Collection (Orinoco GC System)
- V8's memory heap is split into regions:
  - New Space (Young Generation) – small, short-lived objects
  - Old Space (Old Generation) – long-lived or promoted objects
- Garbage Collector Algorithms:
  - Scavenger (Minor GC): Quickly clears short-lived objects in new space
  - Mark-and-Sweep (Major GC): Identifies live vs. dead objects in old space
  - Mark-Compact: Defragments memory to prevent fragmentation
  - Incremental & Parallel GC: Runs partially in background threads to reduce blocking

### 🧬 7️⃣ Hidden Classes & Inline Caches
- V8 creates hidden "blueprints" internally for JS objects (similar to classes in C++).

```js
const user = { name: "Kamal", age: 31 };
// V8 internally creates a hidden class structure with offsets for name and age
// Accessing properties becomes as fast as accessing fields in a C++ struct
```

- When V8 sees repeated property access (user.name), it caches the location of that property.
- Future accesses skip dynamic lookup → direct memory access → faster performance.

### 🔄 8️⃣ De-Optimization
- Undo over-optimizations when assumptions fail.

```js
function add(a, b) { return a + b; }
add(2, 3);   // optimized for numbers
add("2", 3); // breaks type assumption → de-optimizes → returns to bytecode
```

### 💾 9️⃣ Caching and Reuse
- V8 caches parsed scripts and compiled bytecode so repeated loads (like React bundles) are faster.
- Reuses optimized machine code across reloads when possible.

### 🧠 Final Flow Summary

```text
JavaScript Source
       ↓
   Parser → AST
       ↓
 Ignition → Bytecode
       ↓
 Executes (profiling)
       ↓
 TurboFan JIT → Optimized Machine Code
       ↓
 Executes natively on CPU
       ↓
 Garbage Collector (memory cleanup)
```

### 🔍 Deep Insights
- Ignition + TurboFan form V8's dual-engine architecture — fast startup + high performance
- Type feedback drives TurboFan's optimization choices dynamically
- Hidden classes and inline caches make property access nearly as fast as C++
- Adaptive compilation ensures V8 balances speed and flexibility
- Incremental GC avoids blocking the main thread — critical for smooth web apps

### 💡 Interview Summary
"V8 first parses JS into an AST, then Ignition interprets it as bytecode. Hot code is optimized by TurboFan into native machine code using profiling data. V8 continuously monitors runtime types to optimize and deoptimize as needed. Its garbage collector and caching systems keep memory efficient and execution fast."

### 🌐 V8 + Fetch API Internal Flow

```js
async function getData() {
  const res = await fetch("https://api.example.com");
  const data = await res.json();
  console.log(data);
}
getData();
```

**Complete Internal Flow:**
1️⃣ V8 parses async function → 2️⃣ Ignition creates bytecode → 3️⃣ V8 executes until fetch → 4️⃣ Blink handles network → 5️⃣ V8 creates Promise → 6️⃣ Microtask queue → 7️⃣ V8 resumes execution

**Key Points:**
- V8 handles JS execution and Promises, Blink handles network I/O and Web APIs
- Event loop coordinates between V8's microtask queue and Blink's network responses
- This separation allows V8 to stay responsive while network requests happen in background

---

## 🌐 **Workers (Quick View)**

### **Web Worker**
```js
// main.js
const worker = new Worker('worker.js');
worker.postMessage([1,2,3]);
worker.onmessage = e => console.log(e.data);

// worker.js
self.onmessage = e => self.postMessage(e.data.reduce((a,b)=>a+b,0));
```

### **Service Worker (Install + Fetch)**
```js
// sw.js
self.addEventListener('install', e => {
  e.waitUntil(caches.open('v1').then(c => c.addAll(['/','/app.js'])));
});
self.addEventListener('fetch', e => {
  e.respondWith(caches.match(e.request).then(r => r || fetch(e.request)));
});
```

---

## 🔑 **Interview Keywords**

### **Must Know Concepts**
- **Hoisting** - Variable/function declarations moved to top
- **Closure** - Function retains access to outer scope
- **Prototype** - Object inheritance mechanism
- **Event Loop** - JavaScript execution model
- **Scope** - Variable accessibility rules
- **`this`** - Function context binding
- **Promises** - Async operation handling
- **Closure** - Function + lexical environment

### **Common Gotchas**
```js
// typeof null === "object"
// 0.1 + 0.2 !== 0.3 (floating point precision)
// var vs let/const hoisting
// this binding in different contexts
// Promise vs callback timing
```

### **Key Differences**
| Feature | Comparison |
|---------|------------|
| `==` vs `===` | Loose vs strict equality |
| `var` vs `let` | Function vs block scope |
| `function` vs `=>` | Dynamic vs lexical `this` |
| `null` vs `undefined` | Intentional vs uninitialized |
| `Promise.all` vs `Promise.race` | All succeed vs first complete |

---

## 🎯 **Quick Reference**

### **Array Methods**
```js
arr.map(fn)     // Transform each element
arr.filter(fn)  // Keep elements that pass test
arr.reduce(fn)  // Reduce to single value
arr.find(fn)    // Find first matching element
arr.some(fn)    // Test if any element passes
arr.every(fn)   // Test if all elements pass
```

### **Object Methods**
```js
Object.keys(obj)           // Get own property names
Object.values(obj)         // Get own property values
Object.entries(obj)        // Get [key, value] pairs
Object.assign(target, src) // Copy properties
Object.freeze(obj)         // Make immutable
```

### **String Methods**
```js
str.includes(substr)  // Check if contains
str.startsWith(prefix) // Check if starts with
str.endsWith(suffix)   // Check if ends with
str.repeat(count)      // Repeat string
str.padStart(len, pad) // Pad start
str.padEnd(len, pad)   // Pad end
```

---

## 🚀 **Final Tips**

1. **Practice Coding** - Don't just memorize, implement
2. **Explain Aloud** - Practice verbal explanations
3. **Know the Why** - Understand underlying mechanisms
4. **Stay Current** - Keep up with ES2020+ features
5. **Think Edge Cases** - Consider error scenarios
6. **Performance Matters** - Know optimization techniques

**Good luck with your interview! 🎉**
