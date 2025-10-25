# 🚀 JavaScript Comprehensive Cheatsheet 2025

> **Quick Reference Guide for JavaScript Interview Preparation**

---

## 📚 **Quick Navigation**

- [**Fundamentals**](#fundamentals) - Core concepts and syntax
- [**Functions & Closures**](#functions--closures) - Function concepts and scope
- [**Objects & Classes**](#objects--classes) - OOP and prototypes
- [**Async JavaScript**](#async-javascript) - Promises, async/await, event loop
- [**ES6+ Features**](#es6-features) - Modern JavaScript syntax
- [**Performance**](#performance) - Optimization techniques
- [**Common Patterns**](#common-patterns) - Design patterns and best practices

---

## 🟢 **Fundamentals**

### **Data Types**
```javascript
// Primitives
typeof undefined    // "undefined"
typeof null        // "object" (bug)
typeof true        // "boolean"
typeof 42          // "number"
typeof "hello"     // "string"
typeof Symbol()    // "symbol"
typeof 123n        // "bigint"

// Non-primitives
typeof {}          // "object"
typeof []          // "object"
typeof function(){} // "function"
```

### **Variable Declarations**
```javascript
// var - function scoped, hoisted
var x = 1;

// let - block scoped, temporal dead zone
let y = 2;

// const - block scoped, immutable reference
const z = 3;
```

### **Equality**
```javascript
// Strict equality (preferred)
=== !==  // No type coercion

// Loose equality (avoid)
== !=    // Type coercion

// Examples
"5" == 5   // true (coercion)
"5" === 5  // false (no coercion)
```

### **Truthy/Falsy Values**
```javascript
// Falsy values
false, 0, -0, 0n, "", null, undefined, NaN

// Everything else is truthy
"0", "false", [], {}, function(){}
```

---

## 🧠 **Functions & Closures**

### **Function Types**
```javascript
// Function declaration (hoisted)
function myFunc() {}

// Function expression
const myFunc = function() {};

// Arrow function (no 'this' binding)
const myFunc = () => {};

// IIFE (Immediately Invoked Function Expression)
(function() {
  // Private scope
})();
```

### **Closures**
```javascript
function outer(x) {
  return function inner(y) {
    return x + y; // x is "closed over"
  };
}

const add5 = outer(5);
add5(3); // 8
```

### **Higher-Order Functions**
```javascript
// Functions that take/return functions
const numbers = [1, 2, 3, 4, 5];

// Map
const doubled = numbers.map(x => x * 2);

// Filter
const evens = numbers.filter(x => x % 2 === 0);

// Reduce
const sum = numbers.reduce((acc, x) => acc + x, 0);
```

### **Currying**
```javascript
const add = (a) => (b) => a + b;
const add5 = add(5);
add5(3); // 8

// Manual currying
function curry(fn) {
  return function curried(...args) {
    if (args.length >= fn.length) {
      return fn.apply(this, args);
    }
    return function(...nextArgs) {
      return curried(...args, ...nextArgs);
    };
  };
}
```

---

## 🏗️ **Objects & Classes**

### **Object Creation**
```javascript
// Object literal
const obj = { name: "John", age: 30 };

// Object.create()
const proto = { greet() { return "Hello"; } };
const obj = Object.create(proto);

// Constructor function
function Person(name) {
  this.name = name;
}
const person = new Person("John");

// ES6 Class
class Person {
  constructor(name) {
    this.name = name;
  }
  
  greet() {
    return `Hello, I'm ${this.name}`;
  }
}
```

### **Prototype Chain**
```javascript
// Every object has a prototype
obj.__proto__ === Object.prototype
Object.getPrototypeOf(obj) === Object.prototype

// Prototype methods
obj.hasOwnProperty('name')  // true
obj.toString()              // "[object Object]"
```

### **ES6 Classes**
```javascript
class Animal {
  constructor(name) {
    this.name = name;
  }
  
  speak() {
    return `${this.name} makes a sound`;
  }
}

class Dog extends Animal {
  constructor(name, breed) {
    super(name);
    this.breed = breed;
  }
  
  speak() {
    return `${this.name} barks`;
  }
}
```

---

## ⚡ **Async JavaScript**

### **Promises**
```javascript
// Promise creation
const promise = new Promise((resolve, reject) => {
  if (success) {
    resolve(value);
  } else {
    reject(error);
  }
});

// Promise consumption
promise
  .then(value => console.log(value))
  .catch(error => console.error(error))
  .finally(() => console.log("Done"));
```

### **Async/Await**
```javascript
async function fetchData() {
  try {
    const response = await fetch('/api/data');
    const data = await response.json();
    return data;
  } catch (error) {
    console.error('Error:', error);
  }
}
```

### **Promise Methods**
```javascript
// Promise.all - all must succeed
Promise.all([promise1, promise2, promise3])
  .then(values => console.log(values));

// Promise.race - first to complete
Promise.race([promise1, promise2])
  .then(value => console.log(value));

// Promise.allSettled - all complete (success or failure)
Promise.allSettled([promise1, promise2])
  .then(results => console.log(results));
```

### **Event Loop**
```javascript
// Execution order
console.log('1');           // 1

setTimeout(() => {          // 4
  console.log('2');
}, 0);

Promise.resolve().then(() => { // 3
  console.log('3');
});

console.log('4');           // 2

// Output: 1, 4, 3, 2
```

---

## 🧩 **ES6+ Features**

### **Destructuring**
```javascript
// Object destructuring
const { name, age } = person;
const { name: fullName, age = 25 } = person;

// Array destructuring
const [first, second, ...rest] = array;
const [a, , c] = array; // Skip second element
```

### **Spread/Rest Operators**
```javascript
// Spread
const newArray = [...oldArray, newItem];
const newObj = { ...oldObj, newProp: value };

// Rest
function sum(...numbers) {
  return numbers.reduce((a, b) => a + b);
}
```

### **Template Literals**
```javascript
const name = "John";
const age = 30;

// String interpolation
const message = `Hello, ${name}! You are ${age} years old.`;

// Multiline strings
const html = `
  <div>
    <h1>${name}</h1>
    <p>Age: ${age}</p>
  </div>
`;
```

### **Modules**
```javascript
// Export
export const name = "John";
export function greet() { return "Hello"; }
export default class Person {}

// Import
import Person, { name, greet } from './module.js';
import * as utils from './utils.js';
```

---

## ⚡ **Performance**

### **Memory Management**
```javascript
// Avoid memory leaks
// 1. Remove event listeners
element.removeEventListener('click', handler);

// 2. Clear intervals/timeouts
clearInterval(intervalId);
clearTimeout(timeoutId);

// 3. Avoid circular references
let obj = {};
obj.self = obj; // Memory leak!
```

### **Optimization Techniques**
```javascript
// Debouncing
function debounce(func, delay) {
  let timeoutId;
  return function(...args) {
    clearTimeout(timeoutId);
    timeoutId = setTimeout(() => func.apply(this, args), delay);
  };
}

// Throttling
function throttle(func, limit) {
  let inThrottle;
  return function(...args) {
    if (!inThrottle) {
      func.apply(this, args);
      inThrottle = true;
      setTimeout(() => inThrottle = false, limit);
    }
  };
}

// Memoization
function memoize(fn) {
  const cache = new Map();
  return function(...args) {
    const key = JSON.stringify(args);
    if (cache.has(key)) {
      return cache.get(key);
    }
    const result = fn.apply(this, args);
    cache.set(key, result);
    return result;
  };
}
```

---

## 🎯 **Common Patterns**

### **Module Pattern**
```javascript
const MyModule = (function() {
  let privateVar = 0;
  
  return {
    publicMethod() {
      return privateVar++;
    }
  };
})();
```

### **Observer Pattern**
```javascript
class EventEmitter {
  constructor() {
    this.events = {};
  }
  
  on(event, listener) {
    if (!this.events[event]) {
      this.events[event] = [];
    }
    this.events[event].push(listener);
  }
  
  emit(event, ...args) {
    if (this.events[event]) {
      this.events[event].forEach(listener => listener(...args));
    }
  }
}
```

### **Factory Pattern**
```javascript
function createUser(type) {
  const users = {
    admin: () => new AdminUser(),
    user: () => new RegularUser(),
    guest: () => new GuestUser()
  };
  
  return users[type] ? users[type]() : new RegularUser();
}
```

---

## 🔧 **Useful Utilities**

### **Array Methods**
```javascript
// Find
const user = users.find(u => u.id === 1);

// Some/Every
const hasAdults = users.some(u => u.age >= 18);
const allAdults = users.every(u => u.age >= 18);

// Flat
const flattened = nestedArray.flat(2);

// Includes
const hasItem = array.includes(item);
```

### **Object Methods**
```javascript
// Object.keys/values/entries
Object.keys(obj)    // ['key1', 'key2']
Object.values(obj)  // ['value1', 'value2']
Object.entries(obj) // [['key1', 'value1'], ['key2', 'value2']]

// Object.assign
const merged = Object.assign({}, obj1, obj2);

// Object.freeze/seal
Object.freeze(obj)  // Immutable
Object.seal(obj)    // Can't add/remove properties
```

---

## 🚨 **Common Gotchas**

### **Hoisting**
```javascript
console.log(x); // undefined (not error)
var x = 5;

// vs
console.log(y); // ReferenceError
let y = 5;
```

### **This Binding**
```javascript
const obj = {
  name: 'John',
  greet: function() {
    return `Hello, ${this.name}`;
  },
  greetArrow: () => {
    return `Hello, ${this.name}`; // undefined
  }
};
```

### **Closure in Loops**
```javascript
// Wrong
for (var i = 0; i < 3; i++) {
  setTimeout(() => console.log(i), 100); // 3, 3, 3
}

// Right
for (let i = 0; i < 3; i++) {
  setTimeout(() => console.log(i), 100); // 0, 1, 2
}
```

---

## 📝 **Quick Reference**

### **String Methods**
```javascript
str.includes(substr)    // true/false
str.startsWith(prefix)   // true/false
str.endsWith(suffix)    // true/false
str.repeat(count)       // repeated string
str.padStart(length)    // padded string
```

### **Number Methods**
```javascript
Number.isInteger(num)   // true/false
Number.isNaN(num)       // true/false
Math.floor(num)         // round down
Math.ceil(num)          // round up
Math.round(num)         // round nearest
```

### **Date Methods**
```javascript
const now = new Date();
now.getFullYear()       // 2025
now.getMonth()          // 0-11
now.getDate()           // 1-31
now.toISOString()       // "2025-01-01T00:00:00.000Z"
```

---

*This cheatsheet covers the most important JavaScript concepts for interviews. For detailed explanations, refer to the individual section files.*