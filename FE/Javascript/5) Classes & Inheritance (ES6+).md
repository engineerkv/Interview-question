# 🏗️ 5. Classes & Inheritance (ES6+) (Q56–65)

---

## 56) What is a class in JavaScript and how is it implemented internally?

Concept:
A class in JavaScript is just a syntactic sugar over its prototype-based inheritance system. It provides a cleaner, more readable way to create objects and handle inheritance — but under the hood, it still uses functions and prototypes.

Example:
```js
class Person {
  constructor(name) { this.name = name; }
  greet() { return `Hi, I'm ${this.name}`; }
}
const p = new Person('Alice');
```

Deep Insight:
- **Core rule:** Classes are just constructor functions with special syntax
- **Real-world use:** Creating reusable objects with shared methods
- **Common mistake:** Thinking classes are completely different from functions
- **Advanced point:** Methods go on `prototype`, not on instances
- **Interview tip:** Show that `typeof Person` is `'function'`

---

## 57) What is the difference between class declaration and class expression?

Concept:
Class declarations create classes with names, while class expressions create classes as values.

Example:
```js
class MyClass {} // declaration
const MyClass = class {}; // expression
const Named = class Inner {}; // named expression
```

Deep Insight:
- **Core rule:** Both declarations and expressions create constructor functions
- **Real-world use:** Use expressions when you need classes as values
- **Common mistake:** Not understanding that classes are functions
- **Advanced point:** Named expressions help with debugging
- **Interview tip:** Show when to use each approach

---

## 58) How does inheritance work with the `extends` keyword?

Concept:
`extends` lets one class inherit from another class, giving it access to all the parent's properties and methods.

Example:
```js
class Animal {
  speak() { return 'sound'; }
}
class Dog extends Animal {
  speak() { return 'woof'; }
}
```

Deep Insight:
- **Core rule:** `extends` creates a prototype chain between classes
- **Real-world use:** Building class hierarchies, reusing parent functionality
- **Common mistake:** Forgetting to call `super()` in constructor
- **Advanced point:** `super` is lexically bound, not dynamic
- **Interview tip:** Show how to override methods with `super`

---

## 59) What does `super()` do in a subclass constructor?

Concept:
`super()` calls the parent class constructor and must be called before using `this` in a child constructor.

Example:
```js
class Parent { constructor(x) { this.x = x; } }
class Child extends Parent {
  constructor(x, y) {
    super(x); // must call first
    this.y = y;
  }
```

Deep Insight:
- **Core rule:** `super()` must be called before accessing `this`
- **Real-world use:** Initializing parent properties in child constructors
- **Common mistake:** Trying to use `this` before calling `super()`
- **Advanced point:** `super()` returns the current instance, not the parent
- **Interview tip:** Show what happens if you forget `super()`

---

## 60) What are static methods and properties?

Concept:
Static methods and properties belong to the class itself, not to individual instances, and are called directly on the class.

Example:
```js
class Math {
  static add(a, b) { return a + b; }
  static PI = 3.14;
}
Math.add(1, 2); // 3
```

Deep Insight:
- **Core rule:** Static members are called on the class, not instances
- **Real-world use:** Utility functions, constants, factory methods
- **Common mistake:** Trying to access `this` in static methods
- **Advanced point:** Static members are inherited by subclasses
- **Interview tip:** Show when to use static vs instance methods

---

## 61) How are private class fields (`#field`) implemented?

Concept:
Private fields use the `#` prefix and can only be accessed from within the same class, making them truly private.

Example:
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

Deep Insight:
- **Core rule:** Private fields with `#` are truly private, not just conventionally private
- **Real-world use:** Hiding internal implementation details
- **Common mistake:** Forgetting the `#` prefix when accessing private fields
- **Advanced point:** Private fields are not accessible from subclasses
- **Interview tip:** Show the difference between `_private` and `#private`

---

## 62) Can you use `super` in object literals?

Concept:
No, `super` only works inside class methods and constructors, not in regular object literals.

Example:
```js
const obj = {
  method() {
    // super.method(); // SyntaxError
    return this.__proto__.method.call(this);
  }
};
```

Deep Insight:
- **Core rule:** `super` only works in class context, not object literals
- **Real-world use:** Understanding when you can and can't use `super`
- **Common mistake:** Trying to use `super` in object literals
- **Advanced point:** Use `this.__proto__` for similar functionality in objects
- **Interview tip:** Show the difference between class and object contexts

---

## 63) What's the difference between ES6 classes and prototype-based inheritance?

Concept:
Classes provide cleaner syntax but work exactly like constructor functions and prototypes underneath.

Example:
```js
// ES6 class
class Person { constructor(name) { this.name = name; } }
const p1 = new Person('Alice');

// Equivalent prototype
function Person(name) { this.name = name; }
const p2 = new Person('Bob');
```

Deep Insight:
- **Core rule:** Classes are just syntactic sugar over constructor functions
- **Real-world use:** Both approaches work the same, choose based on preference
- **Common mistake:** Thinking classes are completely different from functions
- **Advanced point:** Classes enforce `new` usage and have better tooling
- **Interview tip:** Show that both approaches create the same result

---

## 64) What are mixins and how do they simulate multiple inheritance?

Concept:
Mixins are objects with methods that get copied into classes to simulate multiple inheritance.

Example:
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

Deep Insight:
- **Core rule:** Mixins copy methods from objects into class prototypes
- **Real-world use:** Adding functionality to classes without inheritance
- **Common mistake:** Creating naming conflicts between mixins
- **Advanced point:** `Object.assign` is the common pattern for mixins
- **Interview tip:** Show how to compose multiple mixins

---

## 65) How can you polyfill class inheritance in older JavaScript engines?

Concept:
Use `Object.create` to set up prototype chains and manual constructor chaining for older browsers that don't support classes.

Example:
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

Deep Insight:
- **Core rule:** `Object.create` sets up prototype chains, `Parent.call` chains constructors
- **Real-world use:** Supporting older browsers that don't have classes
- **Common mistake:** Forgetting to set the `constructor` property
- **Advanced point:** Use transpilers like Babel for production code
- **Interview tip:** Show the manual steps that classes do automatically
