
### 🧠 2. Functions, Scope & Closures — Q26-Q45

### 1️⃣ What are first-class functions in JavaScript?

**🧠 Concept**

In JavaScript, functions are treated like any other value — you can store them in variables, pass them as arguments, or return them from other functions.

**💻 Example**
```js
const greet = () => console.log("Hello!");
function execute(fn) { fn(); }

execute(greet); // Hello!
```

**💬 Explanation + Insight**

- **First-class Citizens** - Functions can be stored in variables
- **Function Arguments** - Functions can be passed as arguments
- **Return Functions** - Functions can be returned from other functions
- **Functional Programming** - This enables functional programming patterns
- **JavaScript Power** - Makes JavaScript very flexible and powerful

This property makes higher-order functions, callbacks, and closures possible — the foundation of functional JS.

---

### 2️⃣ What are higher-order functions?

**🧠 Concept**

A higher-order function (HOF) is one that takes a function as an argument or returns a function.

**💻 Example**
```js
function repeat(fn, times) {
  for (let i = 0; i < times; i++) fn();
}

repeat(() => console.log("Hi!"), 3);
```

**💬 Explanation + Insight**

- **Function Arguments** - Functions that take other functions as arguments
- **Return Functions** - Functions that return functions as their result
- **Functional Patterns** - Enable powerful functional programming patterns
- **Built-in Examples** - Examples: `map`, `filter`, `reduce` are higher-order functions
- **Code Reusability** - Make code more reusable and flexible

Built-ins like `map`, `filter`, and `reduce` are HOFs.
They make code **declarative** and **modular**.

---

### 3️⃣ What is a closure in JavaScript?

**🧠 Concept**


A closure is formed when an **inner function** remembers variables from its **outer function**, even after the outer function has finished executing.

**💻 Example**

```js
function outer() {
  let counter = 0;
  return function inner() {
    counter++;
    console.log(counter);
  };
}

const count = outer();
count(); // 1
count(); // 2
```

🧠 **Memory Visualization:**

```
outer()
 ├─ counter = 0
 └─ returns  inner() with access to counter (via closure)

inner()  still "remembers" counter even after outer() is gone!
```

**💬 Explanation + Insight**


Closures give **persistent state** without global variables — vital in React hooks, event handlers, and factory functions.

---

### 4️⃣ How do closures help with data privacy?

**🧠 Concept**


Closures create **private variables** that cannot be accessed from outside the function’s scope.

**💻 Example**

```js
function createBankAccount() {
  let balance = 0;
  return {
    deposit(amount) { balance += amount; },
    getBalance() { return balance; }
  };
}

const account = createBankAccount();
account.deposit(100);
console.log(account.getBalance()); // 100
// console.log(account.balance); ❌ undefined
```

🧠 **Diagram:**

```
🔒 balance variable
⤷ Only accessible to functions inside createBankAccount()
```

**💬 Explanation + Insight**


Used to **encapsulate state**, like in module patterns or custom hooks.
This is how JS mimics **private fields** before ES2022.

---

### 5️⃣ What is the lexical environment?

**🧠 Concept**


The lexical environment is the **scope chain** created by where a function is defined — not where it’s called.

**💻 Example**

```js
function outer() {
  let x = 10;
  function inner() {
    console.log(x);
  }
  inner();
}
outer(); // 10
```

🧠 **Diagram:**

```
inner()  looks for x
  ⤷ not found in local scope
  ⤷ found in outer()'s scope (lexical environment)
```

**💬 Explanation + Insight**


Lexical scope = scope defined **at write-time**, not **run-time**.
That’s why arrow functions preserve `this` context — they respect lexical scope.

---

### 6️⃣ What is the difference between function declaration and expression?

**🧠 Concept**



* **Declaration:** Named and hoisted (can be called before definition).
* **Expression:** Assigned to a variable; not hoisted.

**💻 Example**

```js
sayHi(); // ✅ works
function sayHi() { console.log("Hi!"); }

greet(); // ❌ Error
const greet = function() { console.log("Hello!"); };
```

**💬 Explanation + Insight**


Declarations are **hoisted** with their function body.
Expressions (and arrow functions) are **not callable before initialization**.

---

### 7️⃣ What are pure and impure functions?

**🧠 Concept**



* **Pure:** No side effects; same inputs always give same output.
* **Impure:** Modifies external state or depends on it.

**💻 Example**

```js
// Pure
function add(a, b) {
  return a + b;
}

// Impure
let total = 0;
function addToTotal(n) {
  total += n;
}
```

**💬 Explanation + Insight**


Pure functions are predictable, testable, and **core to functional programming**.

---

### 8️⃣ What is function currying?

**🧠 Concept**


Currying transforms a function with multiple arguments into **a sequence of functions**, each taking one argument.

**💻 Example**

```js
function add(a) {
  return function(b) {
    return function(c) {
      return a + b + c;
    };
  };
}

console.log(add(1)(2)(3)); // 6
```

🧠 **Diagram:**

```
add(1)  returns fn waiting for b
  add(1)(2)  returns fn waiting for c
  add(1)(2)(3)  returns 6
```

**💬 Explanation + Insight**


Used in functional programming and frameworks (like Redux’s `compose`) to **partially apply arguments** and build flexible utilities.

---

### 9️⃣ What is partial application?

**🧠 Concept**


Partial application **fixes some arguments** of a function and returns a new function.

**💻 Example**

```js
function multiply(a, b, c) {
  return a * b * c;
}

const double = multiply.bind(null, 2);
console.log(double(3, 4)); // 24
```

**💬 Explanation + Insight**


Currying  1 argument per function
Partial  fixes *some* arguments
Useful in **configuration-based functions** (e.g., logging utilities, event handlers).

---

### 🔟 How do you memoize a function?

**🧠 Concept**


Memoization stores results of expensive function calls so that the next call with the same input returns instantly.

**💻 Example**

```js
function memoize(fn) {
  const cache = {};
  return function(x) {
    if (cache[x]) return cache[x];
    const result = fn(x);
    cache[x] = result;
    return result;
  };
}

const square = memoize(x => x * x);
console.log(square(4)); // calculates
console.log(square(4)); // cached ✅
```

🧠 **Diagram:**

```
cache = { 4: 16 }
next call with 4  returns from cache
```

**💬 Explanation + Insight**



* Boosts performance for heavy computations (e.g., Fibonacci).
* Used widely in React (e.g., `useMemo`, `memo`) and optimization patterns.

---

## ⚠️ Interview Gotchas & Quick Tips (Closures & Functions)

1. 🧩 **Closure trap:**

   ```js
   for (var i = 0; i < 3; i++) {
     setTimeout(() => console.log(i), 1000);
   }
   // 3, 3, 3 (not 0,1,2)
   ```

   ✅ Fix: use `let` (block scope) or IIFE:

   ```js
   for (var i = 0; i < 3; i++) {
     ((x) => setTimeout(() => console.log(x), 1000))(i);
   }
   ```

2. 🔄 **Lexical scope vs dynamic scope:**
   JS is **lexically scoped**, not dynamically — meaning functions use the scope **where they were defined**, not **where called**.

3. 💥 **Memoization vs caching:**
   Memoization = input-specific cache
   Caching = more general (e.g., API responses).

4. 🧠 **Arrow functions & this:**
   They **don’t bind `this`**, making them perfect for callbacks, but *not* for methods or constructors.

5. 🧰 **Pure functions = Predictability:**
   If function output depends on no external variables and has no side effects  ✅ pure.

6. 🧵 **Closures keep memory alive** — beware in loops, or you can cause memory leaks if large data stays referenced.

### 11️⃣ What is recursion in JavaScript?

**🧠 Concept**


Recursion is when a function **calls itself** until it reaches a stopping condition (base case).

**💻 Example**

```js
function factorial(n) {
  if (n === 1) return 1;
  return n * factorial(n - 1);
}
console.log(factorial(5)); // 120
```

🧠 **Diagram:**

```
factorial(5)
 └─> factorial(4)
     └─> factorial(3)
         └─> factorial(2)
             └─> factorial(1)
                 ⤴ unwinds and multiplies  120
```

**💬 Explanation + Insight**



* Always define a **base case** to stop recursion.
* Each recursive call adds a new **stack frame**  too deep = **stack overflow**.

---

### 12️⃣ What is the Call Stack?

**🧠 Concept**


The call stack tracks which function is currently being executed — and which one to return to after it finishes.

**💻 Example**

```js
function a() { b(); }
function b() { c(); }
function c() { console.log("End"); }

a();
```

🧠 **Execution Flow Diagram:**

```
[Start]
Call a()
 └─ Call b()
     └─ Call c()
         └─ console.log("End")
     ← Return b()
 ← Return a()
[Stack Empty]
```

**💬 Explanation + Insight**



* JS is **single-threaded**, executing one call at a time.
* When async code runs, it’s delegated to the **event loop** (outside the call stack).

---

### 13️⃣ What is tail call optimization?

**🧠 Concept**


If the **last action** in a function is a call to another function, the current function’s stack frame can be reused — preventing stack overflow.

**💻 Example**

```js
"use strict";
function factorial(n, acc = 1) {
  if (n === 1) return acc;
  return factorial(n - 1, n * acc);
}
```

🧠 **Diagram:**

```
Tail Call Optimization (TCO)
No new stack frame is created  reuses the same one.
```

**💬 Explanation + Insight**



* Supported in strict mode by spec, but not widely implemented (e.g., V8 skipped it).
* Used in functional languages for deep recursion.

---

### 14️⃣ What are callback functions?

**🧠 Concept**


A callback is a function **passed as an argument** to another function, to be executed later.

**💻 Example**

```js
function fetchData(callback) {
  setTimeout(() => {
    console.log("Data fetched");
    callback();
  }, 1000);
}

fetchData(() => console.log("Processing data"));
```

🧠 **Diagram:**

```
fetchData()  registers callback  event loop
  ↓
After 1s  executes callback()
```

**💬 Explanation + Insight**



* Core to async patterns (before Promises).
* Lead to **callback hell** when nested too deeply.

---

### 15️⃣ What is callback hell and how do you avoid it?

**🧠 Concept**


Callback hell occurs when multiple async operations are nested, making code hard to read and maintain.

💻 **Example (callback hell):**

```js
getUser(id, user => {
  getPosts(user, posts => {
    getComments(posts, comments => {
      console.log(comments);
    });
  });
});
```

🧠 **Diagram:**

```
getUser()
 └ getPosts()
    └ getComments()
       └ chaos...
```

✅ **Avoid it:** Use **Promises** or **async/await**.

**💬 Explanation + Insight**


Modern JS avoids callback hell using:

* **Promise chaining**
* **Async/Await syntax**
* **Modularization** of async logic

---

### 16️⃣ What is the difference between `.call()`, `.apply()`, and `.bind()`?

**🧠 Concept**


They manually set the value of `this` for a function.

**💻 Example**

```js
const user = { name: "Kamal" };
function greet(greeting) {
  console.log(`${greeting}, ${this.name}`);
}

greet.call(user, "Hello");  // Hello, Kamal
greet.apply(user, ["Hi"]);  // Hi, Kamal
const bound = greet.bind(user);
bound("Hey"); // Hey, Kamal
```

🧠 **Diagram:**

```
.call()  fn.call(thisArg, arg1, arg2)
.apply()  fn.apply(thisArg, [args])
.bind()  returns new bound function
```

**💬 Explanation + Insight**



* `.call()` and `.apply()` **invoke immediately**.
* `.bind()` **returns a new function** with a bound context.
* Crucial for event handlers, object methods, and constructors.

---

### 17️⃣ What is the difference between event delegation and event bubbling?

**🧠 Concept**



* **Event bubbling:** Events propagate upward (child  parent).
* **Event delegation:** A single parent handles events for its children.

**💻 Example**

```js
document.querySelector("#list").addEventListener("click", e => {
  if (e.target.tagName === "LI") {
    console.log("Clicked:", e.target.textContent);
  }
});
```

🧠 **Diagram:**

```
<li>  click
 ⤴ bubbles to <ul>  handled there (delegation)
```

**💬 Explanation + Insight**



* Efficient for dynamically generated elements.
* Use `event.target` to detect which child was clicked.

---

### 18️⃣ How does `this` keyword behave in different contexts?

**🧠 Concept**


`this` refers to the **object that owns the function at runtime** — but behaves differently depending on context.

**💻 Example**

```js
console.log(this); // Window (global)

function show() { console.log(this); }
show(); // undefined (strict mode)

const obj = { show };
obj.show(); // obj

const arrow = () => console.log(this);
arrow(); // lexical this (from surrounding scope)
```

🧠 **Diagram Summary:**

```
Context                 this
---------------------------------
Global (non-strict)     window
Function (strict)       undefined
Method call             calling object
Constructor call        new instance
Arrow function          outer scope (lexical)
.bind/.call/.apply()    explicitly set
```

**💬 Explanation + Insight**


In interviews, they often test nested and arrow function combos — remember:
**Arrow functions never have their own `this`!**

---

### 19️⃣ What is implicit vs explicit binding?

**🧠 Concept**



* **Implicit:** Determined by how the function is called.
* **Explicit:** Determined by using `.call()`, `.apply()`, or `.bind()`.

**💻 Example**

```js
const person = {
  name: "Kamal",
  greet() {
    console.log(`Hello, ${this.name}`);
  }
};
person.greet(); // implicit binding  person

const greetFn = person.greet;
greetFn.call(person); // explicit binding
```

🧠 **Diagram:**

```
person.greet()  implicit  person
greetFn.call(person)  explicit  person
```

**💬 Explanation + Insight**


If a function loses its context (e.g., passed as a callback), `this` becomes undefined — fix it using **explicit binding**.

---

### 20️⃣ What are arrow function limitations with `this` and `arguments`?

**🧠 Concept**


Arrow functions don’t have their own `this`, `arguments`, or `prototype`.

**💻 Example**

```js
const obj = {
  name: "Kamal",
  say: () => console.log(this.name)
};
obj.say(); // undefined (not "Kamal")
```

🧠 **Diagram:**

```
Arrow fn  no local this
 ⤷ inherits from parent scope (lexical)
```

**💬 Explanation + Insight**



* Perfect for callbacks and array methods.
* Avoid in constructors and class methods.
* Also can’t use `arguments` — use rest `(...args)` instead.

---

## ⚠️ Interview Gotchas & Quick Tips (Execution, `this`, and Events)

1. 🧠 **Callback Hell Fix:**
   Always replace nested callbacks with Promises or async/await.

2. 🪄 **`this` trap in nested objects:**

   ```js
   const obj = {
     name: "Kamal",
     inner: {
       name: "Dev",
       say() { console.log(this.name); }
     }
   };
   obj.inner.say(); // "Dev"
   ```

   ✅ `this` always refers to **the immediate caller**.

3. 🧩 **`call`, `apply`, and `bind`:**

   * `.call(obj, a, b)`
   * `.apply(obj, [a, b])`
   * `.bind(obj)`  returns new function

4. ⚡ **Arrow in setTimeout:**

   ```js
   const obj = { id: 1, show() { setTimeout(() => console.log(this.id)); } };
   obj.show(); // 1 ✅ (lexical this)
   ```

5. 🔄 **Event bubbling:**
   The event travels from inner  outer.
   To stop it  `e.stopPropagation()`.

6. ⚔️ **Binding loss:**

   ```js
   const greet = person.greet;
   greet(); // ❌ undefined
   ```

   ✅ Fix  `greet.call(person)`.

7. 🧱 **Recursion limits:**
   JS stack depth ~10k–20k calls  prefer loops for large operations.

8. 💬 **Arrow function in objects:**
   Arrow inside object literal doesn’t auto-bind to object  use regular methods.
