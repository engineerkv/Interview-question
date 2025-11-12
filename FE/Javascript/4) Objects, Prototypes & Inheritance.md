# 🧱 4. Objects, Prototypes & Inheritance (Q52–71)

---

## 🧩 Q52. What is an object in JavaScript?

### 🧠 Concept

An object is a container that holds data and behavior together. It stores information as key-value pairs and can include functions as methods.

---

### 💡 Example

```js
const person = {
  name: 'John',
  age: 30,
  greet() { return `Hi, I'm ${this.name}`; }
};
console.log(person.greet()); // "Hi, I'm John"
```

---

### 🔍 Deep Insights

* **Rule:** Objects are reference types, not copied when assigned.
* **Use Case:** Storing user data, configuration, API responses.
* **Common Mistake:** Modifying objects when you meant to copy them.
* **Pro Tip:** All objects inherit from `Object.prototype` by default.

---

### ⭐ Senior Takeaway

Objects can be modified after creation, making them flexible but requiring careful handling.

---

## 🧩 Q53. What is the difference between object literal and object constructor?

### 🧠 Concept

Object literals create objects with `{}` syntax, while constructors use `new` keyword with functions. Literals are simpler, constructors allow custom setup.

---

### 💡 Example

```js
const obj1 = { x: 1 }; // Literal
const obj2 = new Object({ x: 1 }); // Constructor
const obj3 = new Date(); // Constructor
```

---

### 🔍 Deep Insights

* **Rule:** Literals are simpler, constructors allow custom setup.
* **Use Case:** Literals for data, constructors for reusable objects.
* **Common Mistake:** Using constructors when literals would work.
* **Pro Tip:** Both create objects with `Object.prototype` as prototype.

---

### ⭐ Senior Takeaway

Show when to use each approach based on your needs.

---

## 🧩 Q54. What is a prototype in JavaScript?

### 🧠 Concept

A prototype is an object that provides fallback properties and methods when they're not found on the current object. Property lookup follows the prototype chain.

---

### 💡 Example

```js
const obj = { a: 1 };
const proto = { b: 2 };
Object.setPrototypeOf(obj, proto);
console.log(obj.b); // 2 (from prototype)
```

---

### 🔍 Deep Insights

* **Rule:** Every object has a `[[Prototype]]` internal slot, property lookup follows the prototype chain.
* **Use Case:** `__proto__` is deprecated; use `Object.getPrototypeOf`.
* **Common Mistake:** Functions have a `prototype` property for `new` instances.
* **Pro Tip:** `Object.prototype` is the root of all chains.

---

### ⭐ Senior Takeaway

Prototypes enable inheritance in JavaScript through the prototype chain.

---

## 🧩 Q55. What is __proto__ in JavaScript?

### 🧠 Concept

`__proto__` is a hidden link inside every object that points to another object—its prototype. Modern code should avoid it and use `Object.getPrototypeOf` instead.

---

### 💡 Example

```js
const proto = { greet() { return 'hi'; } };
const obj = Object.create(proto);
console.log(obj.__proto__ === proto); // true
console.log(Object.getPrototypeOf(obj) === proto); // true (preferred)
```

---

### 🔍 Deep Insights

* **Rule:** `__proto__` is deprecated; use `Object.getPrototypeOf`/`Object.setPrototypeOf`.
* **Use Case:** It exposes the internal [[Prototype]] slot, can be used to read or set prototype links.
* **Common Mistake:** Modern code should avoid `__proto__` for better compatibility.
* **Pro Tip:** `Object.create` is the preferred way to set prototypes.

---

### ⭐ Senior Takeaway

Use modern methods instead of `__proto__` for better compatibility.

---

## 🧩 Q56. What is the prototype chain?

### 🧠 Concept

The prototype chain is how JavaScript looks up properties by checking each object in a linked list until it finds what it needs or reaches `Object.prototype`.

---

### 💡 Example

```js
const arr = [];
// arr → Array.prototype → Object.prototype → null
console.log(arr.toString); // from Object.prototype
```

---

### 🔍 Deep Insights

* **Rule:** Property lookup follows the chain until found or reaches `Object.prototype`.
* **Use Case:** Method inheritance, extending built-in objects.
* **Common Mistake:** Not understanding that own properties override inherited ones.
* **Pro Tip:** The chain ends at `Object.prototype` (whose prototype is `null`).

---

### ⭐ Senior Takeaway

Show how to trace the prototype chain to understand inheritance.

---

## 🧩 Q57. What is the difference between `__proto__` and `prototype`?

### 🧠 Concept

`__proto__` is an object's link to its parent, while `prototype` is a function's blueprint for creating new objects. Only functions have `prototype`.

---

### 💡 Example

```js
function Person() {}
Person.prototype.greet = () => 'hi';
const p = new Person();
console.log(p.__proto__ === Person.prototype); // true
```

---

### 🔍 Deep Insights

* **Rule:** `__proto__` is the actual link, `prototype` is only on functions.
* **Use Case:** Understanding how inheritance works in JavaScript.
* **Common Mistake:** Confusing `__proto__` and `prototype` properties.
* **Pro Tip:** Arrow functions don't have `prototype` property.

---

### ⭐ Senior Takeaway

Show the difference with constructor functions to clarify the concept.

---

## 🧩 Q58. How does prototypal inheritance work?

### 🧠 Concept

Prototypal inheritance means objects can use properties and methods from their parent objects through the prototype chain. Objects inherit from their prototype and can override inherited properties.

---

### 💡 Example

```js
const animal = { speak: () => 'sound' };
const dog = Object.create(animal);
dog.speak = () => 'woof';
console.log(dog.speak()); // 'woof' (own property wins)
```

---

### 🔍 Deep Insights

* **Rule:** Objects inherit from their prototype and can override inherited properties.
* **Use Case:** Sharing methods between objects, extending functionality.
* **Common Mistake:** Modifying prototypes affects all instances.
* **Pro Tip:** Own properties always override inherited ones.

---

### ⭐ Senior Takeaway

Show how to check own vs inherited properties to understand inheritance.

---

## 🧩 Q59. What is the difference between `Object.create()` and class inheritance?

### 🧠 Concept

`Object.create()` sets up prototype links directly, while classes use `extends` with constructor chaining and `super`. `Object.create` is explicit, classes are syntactic sugar.

---

### 💡 Example

```js
const base = { x: 1 };
const child = Object.create(base);
child.y = 2;

class Base { constructor() { this.x = 1; } }
class Child extends Base {
  constructor() { super(); this.y = 2; }
}
```

---

### 🔍 Deep Insights

* **Rule:** `Object.create` is explicit, classes are syntactic sugar over prototypes.
* **Use Case:** `Object.create` for simple inheritance, classes for complex hierarchies.
* **Common Mistake:** Using classes when `Object.create` would be simpler.
* **Pro Tip:** Classes provide constructor chaining and `super` calls.

---

### ⭐ Senior Takeaway

Show when to use each approach based on complexity and needs.

---

## 🧩 Q60. How do you check if an object has a property (own vs inherited)?

### 🧠 Concept

Use `hasOwnProperty` for own properties, `in` operator for inherited properties, and `Object.hasOwn` for safer own checks. Each method checks different scopes.

---

### 💡 Example

```js
const obj = { a: 1 };
Object.setPrototypeOf(obj, { b: 2 });
console.log(obj.hasOwnProperty('a')); // true
console.log('b' in obj); // true
console.log(Object.hasOwn(obj, 'b')); // false
```

---

### 🔍 Deep Insights

* **Rule:** `hasOwnProperty` checks own properties, `in` checks the entire chain.
* **Use Case:** Validating object structure, checking for inherited methods.
* **Common Mistake:** Using `hasOwnProperty` when you need inherited properties.
* **Pro Tip:** `Object.hasOwn` is safer than `hasOwnProperty`.

---

### ⭐ Senior Takeaway

Show the difference between own and inherited properties with examples.

---

## 🧩 Q61. What are getters and setters?

### 🧠 Concept

Getters and setters are special methods that control property access, allowing custom logic on read/write. Getters run when reading, setters run when writing.

---

### 💡 Example

```js
const obj = {
  _value: 0,
  get count() { return this._value; },
  set count(v) { this._value = Math.max(0, v); }
};
obj.count = -5; // becomes 0
```

---

### 🔍 Deep Insights

* **Rule:** Getters run when reading, setters run when writing properties.
* **Use Case:** Validation, computed properties, data transformation.
* **Common Mistake:** Forgetting to handle edge cases in setters.
* **Pro Tip:** Getters without setters create read-only properties.

---

### ⭐ Senior Takeaway

Show how to add getters/setters with `Object.defineProperty`.

---

## 🧩 Q62. What is a class in JavaScript and how is it implemented internally?

### 🧠 Concept

A class in JavaScript is syntactic sugar over prototype-based inheritance. It provides a cleaner way to create objects and handle inheritance, but works like constructor functions underneath.

---

### 💡 Example

```js
class Person {
  constructor(name) { this.name = name; }
  greet() { return `Hi, I'm ${this.name}`; }
}
const p = new Person('Alice');
```

---

### 🔍 Deep Insights

* **Rule:** Classes are just constructor functions with special syntax.
* **Use Case:** Creating reusable objects with shared methods.
* **Common Mistake:** Thinking classes are completely different from functions.
* **Pro Tip:** Methods go on `prototype`, not on instances.

---

### ⭐ Senior Takeaway

Explain that `typeof Person` is `'function'` to show classes are functions.

---

## 🧩 Q63. What is the difference between class declaration and class expression?

### 🧠 Concept

Class declarations create classes with names, while class expressions create classes as values. Both create constructor functions, but expressions are useful when you need classes as values.

---

### 💡 Example

```js
class MyClass {} // declaration
const MyClass = class {}; // expression
const Named = class Inner {}; // named expression
```

---

### 🔍 Deep Insights

* **Rule:** Both declarations and expressions create constructor functions.
* **Use Case:** Use expressions when you need classes as values.
* **Common Mistake:** Not understanding that classes are functions.
* **Pro Tip:** Named expressions help with debugging.

---

### ⭐ Senior Takeaway

Show when to use each approach based on your needs.

---

## 🧩 Q64. How does inheritance work with the `extends` keyword?

### 🧠 Concept

`extends` lets one class inherit from another class, giving it access to all the parent's properties and methods. It creates a prototype chain between classes.

---

### 💡 Example

```js
class Animal {
  speak() { return 'sound'; }
}
class Dog extends Animal {
  speak() { return 'woof'; }
}
```

---

### 🔍 Deep Insights

* **Rule:** `extends` creates a prototype chain between classes.
* **Use Case:** Building class hierarchies, reusing parent functionality.
* **Common Mistake:** Forgetting to call `super()` in constructor.
* **Pro Tip:** `super` is lexically bound, not dynamic.

---

### ⭐ Senior Takeaway

Show how to override methods with `super` to demonstrate inheritance.

---

## 🧩 Q65. What does `super()` do in a subclass constructor?

### 🧠 Concept

`super()` calls the parent class constructor and must be called before using `this` in a child constructor. It initializes parent properties in child constructors.

---

### 💡 Example

```js
class Parent { constructor(x) { this.x = x; } }
class Child extends Parent {
  constructor(x, y) {
    super(x); // must call first
    this.y = y;
  }
}
```

---

### 🔍 Deep Insights

* **Rule:** `super()` must be called before accessing `this`.
* **Use Case:** Initializing parent properties in child constructors.
* **Common Mistake:** Trying to use `this` before calling `super()`.
* **Pro Tip:** `super()` returns the current instance, not the parent.

---

### ⭐ Senior Takeaway

Show what happens if you forget `super()` to highlight the requirement.

---

## 🧩 Q66. What are static methods and properties?

### 🧠 Concept

Static methods and properties belong to the class itself, not to individual instances, and are called directly on the class. They're useful for utility functions and constants.

---

### 💡 Example

```js
class Math {
  static add(a, b) { return a + b; }
  static PI = 3.14;
}
Math.add(1, 2); // 3
```

---

### 🔍 Deep Insights

* **Rule:** Static members are called on the class, not instances.
* **Use Case:** Utility functions, constants, factory methods.
* **Common Mistake:** Trying to access `this` in static methods.
* **Pro Tip:** Static members are inherited by subclasses.

---

### ⭐ Senior Takeaway

Show when to use static vs instance methods based on context.

---

## 🧩 Q67. How are private class fields (`#field`) implemented?

### 🧠 Concept

Private fields use the `#` prefix and can only be accessed from within the same class, making them truly private. They're not just conventionally private like `_private`.

---

### 💡 Example

```js
class Counter {
  #count = 0;
  increment() { this.#count++; }
  getCount() { return this.#count; }
}
const counter = new Counter();
counter.increment();
console.log(counter.getCount()); // 1
```

---

### 🔍 Deep Insights

* **Rule:** Private fields with `#` are truly private, not just conventionally private.
* **Use Case:** Hiding internal implementation details.
* **Common Mistake:** Forgetting the `#` prefix when accessing private fields.
* **Pro Tip:** Private fields are not accessible from subclasses.

---

### ⭐ Senior Takeaway

Show the difference between `_private` and `#private` to clarify true privacy.

---

## 🧩 Q68. Can you use `super` in object literals?

### 🧠 Concept

No, `super` only works inside class methods and constructors, not in regular object literals. Use `this.__proto__` for similar functionality in objects.

---

### 💡 Example

```js
const obj = {
  method() {
    // super.method(); // SyntaxError
    return this.__proto__.method.call(this);
  }
};
```

---

### 🔍 Deep Insights

* **Rule:** `super` only works in class context, not object literals.
* **Use Case:** Understanding when you can and can't use `super`.
* **Common Mistake:** Trying to use `super` in object literals.
* **Pro Tip:** Use `this.__proto__` for similar functionality in objects.

---

### ⭐ Senior Takeaway

Show the difference between class and object contexts to clarify usage.

---

## 🧩 Q69. What's the difference between ES6 classes and prototype-based inheritance?

### 🧠 Concept

Classes provide cleaner syntax but work exactly like constructor functions and prototypes underneath. They're just syntactic sugar over prototype-based inheritance.

---

### 💡 Example

```js
class Person { constructor(name) { this.name = name; } }
const p1 = new Person('Alice');

function Person(name) { this.name = name; }
const p2 = new Person('Bob');
```

---

### 🔍 Deep Insights

* **Rule:** Classes are just syntactic sugar over constructor functions.
* **Use Case:** Both approaches work the same, choose based on preference.
* **Common Mistake:** Thinking classes are completely different from functions.
* **Pro Tip:** Classes enforce `new` usage and have better tooling.

---

### ⭐ Senior Takeaway

Show that both approaches create the same result to demonstrate equivalence.

---

## 🧩 Q70. What are mixins and how do they simulate multiple inheritance?

### 🧠 Concept

Mixins are objects with methods that get copied into classes to simulate multiple inheritance. They add functionality to classes without using inheritance.

---

### 💡 Example

```js
const Flyable = {
  fly() { return 'flying'; }
};
class Bird {
  constructor(name) { this.name = name; }
}
Object.assign(Bird.prototype, Flyable);
const bird = new Bird('Eagle');
console.log(bird.fly()); // 'flying'
```

---

### 🔍 Deep Insights

* **Rule:** Mixins copy methods from objects into class prototypes.
* **Use Case:** Adding functionality to classes without inheritance.
* **Common Mistake:** Creating naming conflicts between mixins.
* **Pro Tip:** `Object.assign` is the common pattern for mixins.

---

### ⭐ Senior Takeaway

Show how to compose multiple mixins to demonstrate flexibility.

---

## 🧩 Q71. How can you polyfill class inheritance in older JavaScript engines?

### 🧠 Concept

Use `Object.create` to set up prototype chains and manual constructor chaining for older browsers that don't support classes. This shows the manual steps that classes do automatically.

---

### 💡 Example

```js
function Parent(x) { this.x = x; }
function Child(x, y) {
  Parent.call(this, x);
  this.y = y;
}
Child.prototype = Object.create(Parent.prototype);
Child.prototype.constructor = Child;
const child = new Child(1, 2);
```

---

### 🔍 Deep Insights

* **Rule:** `Object.create` sets up prototype chains, `Parent.call` chains constructors.
* **Use Case:** Supporting older browsers that don't have classes.
* **Common Mistake:** Forgetting to set the `constructor` property.
* **Pro Tip:** Use transpilers like Babel for production code.

---

### ⭐ Senior Takeaway

Show the manual steps that classes do automatically to understand inheritance.

---
