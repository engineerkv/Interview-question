# 🧱 4. Objects, Prototypes & Inheritance (Q46–57)

---

## 46) What is an object in JavaScript?

Concept:
An object is a container that holds data and behavior together. It stores information as key-value pairs and can include functions.

Example:
```js
const person = {
  name: 'John',
  age: 30,
  greet() { return `Hi, I'm ${this.name}`; }
};
console.log(person.greet()); // "Hi, I'm John"
```

Deep Insight:
- **Core rule:** Objects are reference types, not copied when assigned
- **Real-world use:** Storing user data, configuration, API responses
- **Common mistake:** Modifying objects when you meant to copy them
- **Advanced point:** All objects inherit from `Object.prototype` by default
- **Interview tip:** Show how objects can be modified after creation

---

## 47) What is the difference between object literal and object constructor?

Concept:
Object literals create objects with `{}` syntax, while constructors use `new` keyword with functions.

Example:
```js
// Literal
const obj1 = { x: 1 };

// Constructor
const obj2 = new Object({ x: 1 });
const obj3 = new Date();
```

Deep Insight:
- **Core rule:** Literals are simpler, constructors allow custom setup
- **Real-world use:** Literals for data, constructors for reusable objects
- **Common mistake:** Using constructors when literals would work
- **Advanced point:** Both create objects with `Object.prototype` as prototype
- **Interview tip:** Show when to use each approach

---

## 48) What is a prototype in JavaScript?

Concept:
A prototype is an object that provides fallback properties and methods when they're not found on the current object.

Example:
```js
const obj = { a: 1 };
const proto = { b: 2 };
Object.setPrototypeOf(obj, proto);
console.log(obj.b); // 2 (from prototype)
```

Deep Insight:
- Every object has a `[[Prototype]]` internal slot
- Property lookup follows the prototype chain
- `__proto__` is deprecated; use `Object.getPrototypeOf`
- Functions have a `prototype` property for `new` instances
- `Object.prototype` is the root of all chains

---

## 49) What is __proto__ in JavaScript?

Concept:
`__proto__` is a hidden link inside every object that points to another object — its prototype. That's how one object can inherit properties and methods from another.

Example:
```js
const proto = { greet() { return 'hi'; } };
const obj = Object.create(proto);
console.log(obj.__proto__ === proto); // true
console.log(Object.getPrototypeOf(obj) === proto); // true (preferred)
```

Deep Insight:
- `__proto__` is deprecated; use `Object.getPrototypeOf`/`Object.setPrototypeOf`
- It exposes the internal [[Prototype]] slot
- Can be used to read or set prototype links
- Modern code should avoid `__proto__` for better compatibility
- `Object.create` is the preferred way to set prototypes

---

## 50) What is the prototype chain?

Concept:
The prototype chain is how JavaScript looks up properties by checking each object in a linked list until it finds what it needs.

Example:
```js
const arr = [];
// arr → Array.prototype → Object.prototype → null
console.log(arr.toString); // from Object.prototype
```

Deep Insight:
- **Core rule:** Property lookup follows the chain until found or reaches `Object.prototype`
- **Real-world use:** Method inheritance, extending built-in objects
- **Common mistake:** Not understanding that own properties override inherited ones
- **Advanced point:** The chain ends at `Object.prototype` (whose prototype is `null`)
- **Interview tip:** Show how to trace the prototype chain

---

## 51) What is the difference between `__proto__` and `prototype`?

Concept:
`__proto__` is an object's link to its parent, while `prototype` is a function's blueprint for creating new objects.

Example:
```js
function Person() {}
Person.prototype.greet = () => 'hi';
const p = new Person();
console.log(p.__proto__ === Person.prototype); // true
```

Deep Insight:
- **Core rule:** `__proto__` is the actual link, `prototype` is only on functions
- **Real-world use:** Understanding how inheritance works in JavaScript
- **Common mistake:** Confusing `__proto__` and `prototype` properties
- **Advanced point:** Arrow functions don't have `prototype` property
- **Interview tip:** Show the difference with constructor functions

---

## 52) How does prototypal inheritance work?

Concept:
Prototypal inheritance means objects can use properties and methods from their parent objects through the prototype chain.

Example:
```js
const animal = { speak: () => 'sound' };
const dog = Object.create(animal);
dog.speak = () => 'woof';
console.log(dog.speak()); // 'woof' (own property wins)
```

Deep Insight:
- **Core rule:** Objects inherit from their prototype and can override inherited properties
- **Real-world use:** Sharing methods between objects, extending functionality
- **Common mistake:** Modifying prototypes affects all instances
- **Advanced point:** Own properties always override inherited ones
- **Interview tip:** Show how to check own vs inherited properties

---

## 53) What is the difference between `Object.create()` and class inheritance?

Concept:
`Object.create()` sets up prototype links directly, while classes use `extends` with constructor chaining and `super`.

Example:
```js
const base = { x: 1 };
const child = Object.create(base);
child.y = 2;

class Base { constructor() { this.x = 1; } }
class Child extends Base {
  constructor() { super(); this.y = 2; }
}
```

Deep Insight:
- **Core rule:** `Object.create` is explicit, classes are syntactic sugar over prototypes
- **Real-world use:** `Object.create` for simple inheritance, classes for complex hierarchies
- **Common mistake:** Using classes when `Object.create` would be simpler
- **Advanced point:** Classes provide constructor chaining and `super` calls
- **Interview tip:** Show when to use each approach

---

## 54) How do you check if an object has a property (own vs inherited)?

Concept:
Use `hasOwnProperty` for own properties, `in` operator for inherited properties, and `Object.hasOwn` for safer own checks.

Example:
```js
const obj = { a: 1 };
Object.setPrototypeOf(obj, { b: 2 });
console.log(obj.hasOwnProperty('a')); // true
console.log('b' in obj); // true
console.log(Object.hasOwn(obj, 'b')); // false
```

Deep Insight:
- **Core rule:** `hasOwnProperty` checks own properties, `in` checks the entire chain
- **Real-world use:** Validating object structure, checking for inherited methods
- **Common mistake:** Using `hasOwnProperty` when you need inherited properties
- **Advanced point:** `Object.hasOwn` is safer than `hasOwnProperty`
- **Interview tip:** Show the difference between own and inherited properties

---

## 55) What are getters and setters?

Concept:
Getters and setters are special methods that control property access, allowing custom logic on read/write.

Example:
```js
const obj = {
  _value: 0,
  get count() { return this._value; },
  set count(v) { this._value = Math.max(0, v); }
};
obj.count = -5; // becomes 0
```

Deep Insight:
- **Core rule:** Getters run when reading, setters run when writing properties
- **Real-world use:** Validation, computed properties, data transformation
- **Common mistake:** Forgetting to handle edge cases in setters
- **Advanced point:** Getters without setters create read-only properties
- **Interview tip:** Show how to add getters/setters with `Object.defineProperty`

---

## 56) What is the difference between shallow copy and deep copy?

Concept:
Shallow copy duplicates only the top level, while deep copy recursively copies all nested objects and arrays.

Example:
```js
const original = { a: 1, nested: { b: 2 } };
const shallow = { ...original };
const deep = JSON.parse(JSON.stringify(original));
shallow.nested.b = 3; // affects original
```

Deep Insight:
- **Core rule:** Shallow copies share nested references, deep copies create new objects
- **Real-world use:** Cloning data structures, avoiding mutation bugs
- **Common mistake:** Using shallow copy when you need deep copy
- **Advanced point:** `structuredClone` is the modern way to deep copy
- **Interview tip:** Show the difference with nested objects

---

## 57) How do you deep clone an object without JSON methods?

Concept:
Use recursive functions to traverse and copy all properties, handling different data types appropriately.

Example:
```js
function deepClone(obj) {
  if (obj === null || typeof obj !== "object") return obj;

  const clone = Array.isArray(obj) ? [] : {};
  for (let key in obj) {
    if (obj.hasOwnProperty(key)) {
      clone[key] = deepClone(obj[key]); // recursion
    }
  }
  return clone;
}
```

Deep Insight:
- **Core rule:** Recursively copy all nested objects and arrays
- **Real-world use:** Cloning complex data structures, avoiding mutation
- **Common mistake:** Not handling circular references or special objects
- **Advanced point:** Use `WeakMap` to track circular references
- **Interview tip:** Show how to handle different data types

---

## 58) How does `new` keyword work internally?

Concept:
`new` creates an object, sets its prototype to the constructor's `prototype`, calls the constructor with `this`, and returns the object.

Example:
```js
function Person(name) { this.name = name; }
Person.prototype.greet = () => 'hi';
const p = new Person('Alice');
// p.__proto__ === Person.prototype
```

Deep Insight:
- **Core rule:** `new` creates an object and calls the constructor function
- **Real-world use:** Creating instances from constructor functions
- **Common mistake:** Forgetting `new` when calling constructors
- **Advanced point:** Arrow functions can't be constructors (no `prototype`)
- **Interview tip:** Show the 4 steps of what `new` does internally

