# 💻 JavaScript Interview Notes (2025 Edition)

## 🔴 Section 6 — Advanced JavaScript Internals — Q111-Q130

---

### 111. 🔴 What is the V8 JavaScript engine and how does it work?

**🧠 Concept**

V8 is Google's JavaScript engine that compiles JavaScript to machine code using JIT compilation for high performance.

**💻 Example**

```javascript
// V8 optimizations
function optimizedFunction(x) {
  return x * 2; // V8 optimizes this to bit shift
}

// V8 creates hidden classes for objects
const obj1 = { a: 1, b: 2 };
const obj2 = { a: 1, b: 2 }; // Same hidden class
```

**💬 Explanation + Insight**

- **JIT Compilation** - Just-In-Time compilation for faster execution
- **Hidden Classes** - V8 creates classes for object property access optimization
- **Inline Caching** - Caches property access patterns for speed
- **Garbage Collection** - Automatic memory management with generational GC
- **Optimization** - Hot code gets optimized, cold code stays interpreted

---

## 2️⃣ How does JavaScript memory management work?

**🧠 Concept**

JavaScript uses automatic garbage collection with mark-and-sweep algorithm to manage memory allocation and deallocation.

**💻 Example**

```javascript
// Memory allocation
let largeArray = new Array(1000000).fill(0);

// Memory deallocation (automatic)
largeArray = null; // Garbage collector will clean this up

// Memory leak example
function createClosure() {
  const data = new Array(1000000);
  return function() {
    return data.length; // Keeps data in memory
  };
}
```

**💬 Explanation + Insight**

- **Automatic Management** - No manual memory allocation/deallocation needed
- **Reference Counting** - Counts references to objects
- **Mark and Sweep** - Marks reachable objects, sweeps unreachable ones
- **Generational GC** - Different collection strategies for young/old objects
- **Memory Leaks** - Can occur with closures, event listeners, or circular references

---

## 3️⃣ What is the difference between heap and stack memory?

**🧠 Concept**

Stack stores primitive values and function calls, while heap stores objects and complex data structures.

**💻 Example**

```javascript
// Stack memory (primitive values)
let num = 42;        // Stored in stack
let str = "hello";   // Stored in stack

// Heap memory (objects)
let obj = { name: "John" };  // Object stored in heap
let arr = [1, 2, 3];        // Array stored in heap

// Stack stores reference to heap
let reference = obj; // Stack stores pointer to heap object
```

**💬 Explanation + Insight**

- **Stack** - Fast access, limited size, stores primitives and function calls
- **Heap** - Larger size, stores objects, slower access
- **References** - Stack stores pointers to heap objects
- **Function Calls** - Each function call creates a stack frame
- **Memory Layout** - Stack grows downward, heap grows upward

---

## 4️⃣ How does JavaScript's prototype chain work internally?

**🧠 Concept**

JavaScript uses prototype-based inheritance where objects inherit properties and methods from their prototype chain.

**💻 Example**

```javascript
// Prototype chain example
function Person(name) {
  this.name = name;
}

Person.prototype.sayHello = function() {
  return `Hello, I'm ${this.name}`;
};

const person = new Person("John");
console.log(person.sayHello()); // Inherited from prototype
console.log(person.__proto__ === Person.prototype); // true
```

**💬 Explanation + Insight**

- **Prototype Chain** - Objects inherit from their prototype's prototype
- **__proto__ Property** - Points to the object's prototype
- **Property Lookup** - Searches up the prototype chain
- **Method Inheritance** - Methods are shared through prototype
- **Performance** - Deep prototype chains can slow property access

---

## 5️⃣ What is the difference between == and === in terms of performance?

**🧠 Concept**

=== (strict equality) is generally faster than == (loose equality) because it doesn't perform type coercion.

**💻 Example**

```javascript
// Strict equality (faster)
if (a === b) { /* no type coercion */ }

// Loose equality (slower)
if (a == b) { /* type coercion happens */ }

// Performance difference
const start = performance.now();
for (let i = 0; i < 1000000; i++) {
  "5" === 5; // Fast
}
const end = performance.now();
```

**💬 Explanation + Insight**

- **Type Coercion** - == performs automatic type conversion
- **Performance** - === skips coercion, making it faster
- **Predictability** - === behavior is more predictable
- **Best Practice** - Always use === unless you need coercion
- **Optimization** - V8 can optimize === better than ==

---

## 6️⃣ How does JavaScript's event loop work internally?

**🧠 Concept**

The event loop continuously checks the call stack and task queues, executing callbacks when the stack is empty.

**💻 Example**

```javascript
// Event loop demonstration
console.log("1"); // Synchronous

setTimeout(() => console.log("2"), 0); // Macro task
Promise.resolve().then(() => console.log("3")); // Micro task

console.log("4"); // Synchronous

// Output: 1, 4, 3, 2
```

**💬 Explanation + Insight**

- **Call Stack** - Executes synchronous code first
- **Microtasks** - Promises, queueMicrotask() - higher priority
- **Macrotasks** - setTimeout, setInterval - lower priority
- **Continuous Loop** - Event loop runs until all queues are empty
- **Non-blocking** - Allows asynchronous operations without blocking

---

## 7️⃣ What is the difference between let, const, and var in terms of memory?

**🧠 Concept**

let and const are block-scoped and stored in different memory locations than var, affecting garbage collection and performance.

**💻 Example**

```javascript
// var - function scoped, hoisted
function example() {
  var x = 1; // Stored in function scope
  if (true) {
    var y = 2; // Same scope as x
  }
}

// let/const - block scoped
function example2() {
  let x = 1; // Block scope
  if (true) {
    let y = 2; // Different scope
  }
}
```

**💬 Explanation + Insight**

- **Scope Chain** - var uses function scope, let/const use block scope
- **Memory Allocation** - Different scoping affects memory layout
- **Hoisting** - var is hoisted, let/const have temporal dead zone
- **Garbage Collection** - Block scope allows earlier cleanup
- **Performance** - Block scope can be more memory efficient

---

## 8️⃣ How does JavaScript handle large numbers and BigInt?

**🧠 Concept**

JavaScript uses IEEE 754 double precision for numbers, with BigInt for arbitrary precision integers beyond Number.MAX_SAFE_INTEGER.

**💻 Example**

```javascript
// Number limitations
console.log(Number.MAX_SAFE_INTEGER); // 9007199254740991
console.log(9007199254740991 + 1); // 9007199254740992 (precision loss)

// BigInt solution
const bigNum = 9007199254740991n;
const result = bigNum + 1n; // 9007199254740992n (exact)
```

**💬 Explanation + Insight**

- **IEEE 754** - 64-bit floating point representation
- **Precision Loss** - Numbers beyond 2^53 lose precision
- **BigInt** - Arbitrary precision integers
- **Memory Usage** - BigInt uses more memory than regular numbers
- **Operations** - BigInt requires separate arithmetic operations

---

## 9️⃣ What is the difference between shallow and deep copying in JavaScript?

**🧠 Concept**

Shallow copy creates a new object but shares nested references, while deep copy creates completely independent objects.

**💻 Example**

```javascript
// Shallow copy
const original = { a: 1, b: { c: 2 } };
const shallow = { ...original };
shallow.b.c = 3; // Affects original.b.c

// Deep copy
const deep = JSON.parse(JSON.stringify(original));
deep.b.c = 4; // Doesn't affect original
```

**💬 Explanation + Insight**

- **Shallow Copy** - Copies first level, shares nested references
- **Deep Copy** - Copies all levels, creates independent objects
- **Memory Usage** - Deep copy uses more memory
- **Performance** - Shallow copy is faster
- **Use Cases** - Shallow for simple objects, deep for complex nested structures

---

## 🔟 How does JavaScript's module system work internally?

**🧠 Concept**

JavaScript modules use lexical scoping and create separate execution contexts with their own scope chains and variable environments.

**💻 Example**

```javascript
// Module scope
const moduleVar = "module scope";

export function moduleFunction() {
  return moduleVar; // Access to module scope
}

// Import creates new scope
import { moduleFunction } from './module.js';
```

**💬 Explanation + Insight**

- **Module Scope** - Each module has its own scope
- **Lexical Scoping** - Functions remember their creation context
- **Import/Export** - Creates connections between module scopes
- **Hoisting** - Module code is hoisted differently than script code
- **Circular Dependencies** - Modules can reference each other with proper handling
