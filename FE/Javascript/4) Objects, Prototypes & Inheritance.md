# 🧱 4. Objects, Prototypes & Inheritance (Q52–71)

---

## 52) What is an object in JavaScript?

An object is a container that holds data and behavior together. It stores information as key-value pairs and can include functions.

```js
const person = {
  name: 'John',
  age: 30,
  greet() { return `Hi, I'm ${this.name}`; }
};
console.log(person.greet()); // "Hi, I'm John"
```

- **Core Concept**: Objects are reference types, not copied when assigned
- **Real-World Use**: Storing user data, configuration, API responses
- **Common Mistake**: Modifying objects when you meant to copy them
- **Advanced Feature**: All objects inherit from `Object.prototype` by default
- **Interview Tip**: Explain that objects can be modified after creation

---

## 53) What is the difference between object literal and object constructor?

Object literals create objects with `{}` syntax, while constructors use `new` keyword with functions.

```js
const obj1 = { x: 1 }; // Literal
const obj2 = new Object({ x: 1 }); // Constructor
const obj3 = new Date(); // Constructor
```

- **Core Difference**: Literals are simpler, constructors allow custom setup
- **Real-World Use**: Literals for data, constructors for reusable objects
- **Common Mistake**: Using constructors when literals would work
- **Advanced Feature**: Both create objects with `Object.prototype` as prototype
- **Interview Tip**: Explain that show when to use each approach

---

## 54) What is a prototype in JavaScript?

A prototype is an object that provides fallback properties and methods when they're not found on the current object.

```js
const obj = { a: 1 };
const proto = { b: 2 };
Object.setPrototypeOf(obj, proto);
console.log(obj.b); // 2 (from prototype)
```

- **Core Concept**: Every object has a `[[Prototype]]` internal slot, property lookup follows the prototype chain
- **Real-World Use**: `__proto__` is deprecated; use `Object.getPrototypeOf`
- **Common Mistake**: Functions have a `prototype` property for `new` instances
- **Advanced Feature**: `Object.prototype` is the root of all chains
- **Interview Tip**: Explain that prototypes enable inheritance in JavaScript

---

## 55) What is __proto__ in JavaScript?

`__proto__` is a hidden link inside every object that points to another object — its prototype. That's how one object can inherit properties and methods from another.

```js
const proto = { greet() { return 'hi'; } };
const obj = Object.create(proto);
console.log(obj.__proto__ === proto); // true
console.log(Object.getPrototypeOf(obj) === proto); // true (preferred)
```

- **Core Concept**: `__proto__` is deprecated; use `Object.getPrototypeOf`/`Object.setPrototypeOf`
- **Real-World Impact**: It exposes the internal [[Prototype]] slot, can be used to read or set prototype links
- **Common Mistake**: Modern code should avoid `__proto__` for better compatibility
- **Optimization**: `Object.create` is the preferred way to set prototypes
- **Interview Tip**: Explain that use modern methods instead of `__proto__`

---

## 56) What is the prototype chain?

The prototype chain is how JavaScript looks up properties by checking each object in a linked list until it finds what it needs.

```js
const arr = [];
// arr → Array.prototype → Object.prototype → null
console.log(arr.toString); // from Object.prototype
```

- **Core Rule**: Property lookup follows the chain until found or reaches `Object.prototype`
- **Real-World Use**: Method inheritance, extending built-in objects
- **Common Mistake**: Not understanding that own properties override inherited ones
- **Advanced Feature**: The chain ends at `Object.prototype` (whose prototype is `null`)
- **Interview Tip**: Explain that show how to trace the prototype chain

---

## 57) What is the difference between `__proto__` and `prototype`?

`__proto__` is an object's link to its parent, while `prototype` is a function's blueprint for creating new objects.

```js
function Person() {}
Person.prototype.greet = () => 'hi';
const p = new Person();
console.log(p.__proto__ === Person.prototype); // true
```

- **Core Difference**: `__proto__` is the actual link, `prototype` is only on functions
- **Real-World Use**: Understanding how inheritance works in JavaScript
- **Common Mistake**: Confusing `__proto__` and `prototype` properties
- **Advanced Feature**: Arrow functions don't have `prototype` property
- **Interview Tip**: Explain that show the difference with constructor functions

---

## 58) How does prototypal inheritance work?

Prototypal inheritance means objects can use properties and methods from their parent objects through the prototype chain.

```js
const animal = { speak: () => 'sound' };
const dog = Object.create(animal);
dog.speak = () => 'woof';
console.log(dog.speak()); // 'woof' (own property wins)
```

- **Core Rule**: Objects inherit from their prototype and can override inherited properties
- **Real-World Use**: Sharing methods between objects, extending functionality
- **Common Mistake**: Modifying prototypes affects all instances
- **Advanced Feature**: Own properties always override inherited ones
- **Interview Tip**: Explain that show how to check own vs inherited properties

---

## 59) What is the difference between `Object.create()` and class inheritance?

`Object.create()` sets up prototype links directly, while classes use `extends` with constructor chaining and `super`.

```js
const base = { x: 1 };
const child = Object.create(base);
child.y = 2;

class Base { constructor() { this.x = 1; } }
class Child extends Base {
  constructor() { super(); this.y = 2; }
}
```

- **Core Difference**: `Object.create` is explicit, classes are syntactic sugar over prototypes
- **Real-World Use**: `Object.create` for simple inheritance, classes for complex hierarchies
- **Common Mistake**: Using classes when `Object.create` would be simpler
- **Advanced Feature**: Classes provide constructor chaining and `super` calls
- **Interview Tip**: Explain that show when to use each approach

---

## 60) How do you check if an object has a property (own vs inherited)?

Use `hasOwnProperty` for own properties, `in` operator for inherited properties, and `Object.hasOwn` for safer own checks.

```js
const obj = { a: 1 };
Object.setPrototypeOf(obj, { b: 2 });
console.log(obj.hasOwnProperty('a')); // true
console.log('b' in obj); // true
console.log(Object.hasOwn(obj, 'b')); // false
```

- **Core Methods**: `hasOwnProperty` checks own properties, `in` checks the entire chain
- **Real-World Use**: Validating object structure, checking for inherited methods
- **Common Mistake**: Using `hasOwnProperty` when you need inherited properties
- **Advanced Feature**: `Object.hasOwn` is safer than `hasOwnProperty`
- **Interview Tip**: Explain that show the difference between own and inherited properties

---

## 61) What are getters and setters?

Getters and setters are special methods that control property access, allowing custom logic on read/write.

```js
const obj = {
  _value: 0,
  get count() { return this._value; },
  set count(v) { this._value = Math.max(0, v); }
};
obj.count = -5; // becomes 0
```

- **Core Purpose**: Getters run when reading, setters run when writing properties
- **Real-World Use**: Validation, computed properties, data transformation
- **Common Mistake**: Forgetting to handle edge cases in setters
- **Advanced Feature**: Getters without setters create read-only properties
- **Interview Tip**: Explain that show how to add getters/setters with `Object.defineProperty`

---

## 62) What is a class in JavaScript and how is it implemented internally?

A class in JavaScript is syntactic sugar over prototype-based inheritance. It provides a cleaner way to create objects and handle inheritance.

```js
class Person {
  constructor(name) { this.name = name; }
  greet() { return `Hi, I'm ${this.name}`; }
}
const p = new Person('Alice');
```

- **Core Concept**: Classes are just constructor functions with special syntax
- **Real-World Use**: Creating reusable objects with shared methods
- **Common Mistake**: Thinking classes are completely different from functions
- **Advanced Feature**: Methods go on `prototype`, not on instances
- **Interview Tip**: Explain that `typeof Person` is `'function'`

---

## 63) What is the difference between class declaration and class expression?

Class declarations create classes with names, while class expressions create classes as values.

```js
class MyClass {} // declaration
const MyClass = class {}; // expression
const Named = class Inner {}; // named expression
```

- **Core Difference**: Both declarations and expressions create constructor functions
- **Real-World Use**: Use expressions when you need classes as values
- **Common Mistake**: Not understanding that classes are functions
- **Advanced Feature**: Named expressions help with debugging
- **Interview Tip**: Explain that show when to use each approach

---

## 64) How does inheritance work with the `extends` keyword?

`extends` lets one class inherit from another class, giving it access to all the parent's properties and methods.

```js
class Animal {
  speak() { return 'sound'; }
}
class Dog extends Animal {
  speak() { return 'woof'; }
}
```

- **Core Mechanism**: `extends` creates a prototype chain between classes
- **Real-World Use**: Building class hierarchies, reusing parent functionality
- **Common Mistake**: Forgetting to call `super()` in constructor
- **Advanced Feature**: `super` is lexically bound, not dynamic
- **Interview Tip**: Explain that show how to override methods with `super`

---

## 65) What does `super()` do in a subclass constructor?

`super()` calls the parent class constructor and must be called before using `this` in a child constructor.

```js
class Parent { constructor(x) { this.x = x; } }
class Child extends Parent {
  constructor(x, y) {
    super(x); // must call first
    this.y = y;
  }
}
```

- **Core Rule**: `super()` must be called before accessing `this`
- **Real-World Use**: Initializing parent properties in child constructors
- **Common Mistake**: Trying to use `this` before calling `super()`
- **Advanced Feature**: `super()` returns the current instance, not the parent
- **Interview Tip**: Explain that show what happens if you forget `super()`

---

## 66) What are static methods and properties?

Static methods and properties belong to the class itself, not to individual instances, and are called directly on the class.

```js
class Math {
  static add(a, b) { return a + b; }
  static PI = 3.14;
}
Math.add(1, 2); // 3
```

- **Core Concept**: Static members are called on the class, not instances
- **Real-World Use**: Utility functions, constants, factory methods
- **Common Mistake**: Trying to access `this` in static methods
- **Advanced Feature**: Static members are inherited by subclasses
- **Interview Tip**: Explain that show when to use static vs instance methods

---

## 67) How are private class fields (`#field`) implemented?

Private fields use the `#` prefix and can only be accessed from within the same class, making them truly private.

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

- **Core Rule**: Private fields with `#` are truly private, not just conventionally private
- **Real-World Use**: Hiding internal implementation details
- **Common Mistake**: Forgetting the `#` prefix when accessing private fields
- **Advanced Feature**: Private fields are not accessible from subclasses
- **Interview Tip**: Explain that show the difference between `_private` and `#private`

---

## 68) Can you use `super` in object literals?

No, `super` only works inside class methods and constructors, not in regular object literals.

```js
const obj = {
  method() {
    // super.method(); // SyntaxError
    return this.__proto__.method.call(this);
  }
};
```

- **Core Rule**: `super` only works in class context, not object literals
- **Real-World Impact**: Understanding when you can and can't use `super`
- **Common Mistake**: Trying to use `super` in object literals
- **Advanced Feature**: Use `this.__proto__` for similar functionality in objects
- **Interview Tip**: Explain that show the difference between class and object contexts

---

## 69) What's the difference between ES6 classes and prototype-based inheritance?

Classes provide cleaner syntax but work exactly like constructor functions and prototypes underneath.

```js
class Person { constructor(name) { this.name = name; } }
const p1 = new Person('Alice');

function Person(name) { this.name = name; }
const p2 = new Person('Bob');
```

- **Core Rule**: Classes are just syntactic sugar over constructor functions
- **Real-World Use**: Both approaches work the same, choose based on preference
- **Common Mistake**: Thinking classes are completely different from functions
- **Advanced Feature**: Classes enforce `new` usage and have better tooling
- **Interview Tip**: Explain that show that both approaches create the same result

---

## 70) What are mixins and how do they simulate multiple inheritance?

Mixins are objects with methods that get copied into classes to simulate multiple inheritance.

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

- **Core Concept**: Mixins copy methods from objects into class prototypes
- **Real-World Use**: Adding functionality to classes without inheritance
- **Common Mistake**: Creating naming conflicts between mixins
- **Advanced Feature**: `Object.assign` is the common pattern for mixins
- **Interview Tip**: Explain that show how to compose multiple mixins

---

## 71) How can you polyfill class inheritance in older JavaScript engines?

Use `Object.create` to set up prototype chains and manual constructor chaining for older browsers that don't support classes.

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

- **Core Process**: `Object.create` sets up prototype chains, `Parent.call` chains constructors
- **Real-World Use**: Supporting older browsers that don't have classes
- **Common Mistake**: Forgetting to set the `constructor` property
- **Advanced Feature**: Use transpilers like Babel for production code
- **Interview Tip**: Explain that show the manual steps that classes do automatically

---
