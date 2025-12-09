# 🎯 3. Objects, Prototypes & Inheritance (Q26–44)

---

## 📍 Navigation

<div align="center">

[Functions, Closures & Execution Context](2%29%20Functions%2C%20Closures%20%26%20Execution%20Context.md) • [Home: README](../README.md) • [ES6+ Features →](4%29%20ES6%2B%20Features.md)

[📋 Cheatsheet](JavaScript%20Interview%20Cheatsheet.md]

</div>

---

---

## Q26. 📦 Objects in JavaScript

An object is a container that holds data and behavior together - it stores information as key-value pairs and can include functions as methods. Objects are reference types, not copied when assigned, so modifying them affects all references. All objects inherit from `Object.prototype` by default, which provides common methods like `toString()` and `hasOwnProperty()`.

- **Trade-offs**: Objects can be modified after creation, making them flexible but requiring careful handling - modifying objects when you meant to copy them is a common mistake. They're perfect for storing user data, configuration, and API responses, but watch out for accidental mutations when passing objects around.

Example:

```js
const person = {
  name: 'John',
  age: 30,
  greet() { return `Hi, I'm ${this.name}`; }
};
console.log(person.greet()); // "Hi, I'm John"

```

---

## Q27. 🔗 Prototype in JavaScript

A prototype is an object that provides fallback properties and methods when these are not found on the current object - property lookup follows the prototype chain. Every object has a `[Prototype]` internal slot, and `Object.prototype` is the root of all chains.

- **Trade-offs**: Prototypes enable inheritance in JavaScript through the prototype chain, but the tricky part is `__proto__` is deprecated - use `Object.getPrototypeOf` instead. Functions have a `prototype` property for `new` instances, which can be confusing if you're not careful.

Example:

```js
const obj = { a: 1 };
const proto = { b: 2 };
Object.setPrototypeOf(obj, proto);
console.log(obj.b); // 2 (from prototype)

```

---

## Q28. 💡 `__proto__` in JavaScript

`__proto__` is a hidden link inside every object that points to another object—its prototype, but modern code should avoid it and use `Object.getPrototypeOf` instead. It exposes the internal [Prototype] slot and can be used to read or set prototype links.

- **Trade-offs**: The catch is `__proto__` is deprecated for better compatibility - use `Object.getPrototypeOf`/`Object.setPrototypeOf` or `Object.create` instead. `Object.create` is the preferred way to set prototypes, and it's cleaner than using `__proto__`.

Example:

```js
const proto = { greet() { return 'hi'; } };
const obj = Object.create(proto);
console.log(obj.__proto__ === proto); // true
console.log(Object.getPrototypeOf(obj) === proto); // true (preferred)

```

---

## Q29. 🔗 Prototype chain

The prototype chain is how JavaScript looks up properties by checking each object in a linked list until it finds what it needs or reaches `Object.prototype` - the chain ends at `Object.prototype` (whose prototype is `null`). Property lookup follows the chain until found, and own properties always override inherited ones.

- **Trade-offs**: The prototype chain enables method inheritance and extending built-in objects, but the tricky part is not understanding that own properties override inherited ones. Tracing the prototype chain helps understand inheritance, but modifying prototypes affects all instances, which can cause surprise bugs.

Example:

```js
const arr = [];
// arr → Array.prototype → Object.prototype → null
console.log(arr.toString); // from Object.prototype

```

---

## Q30. 📝 `__proto__` vs `prototype`

`__proto__` is an object's link to its parent, while `prototype` is a function's blueprint for creating new objects - only functions have `prototype`. When you use `new` with a function, the instance's `__proto__` points to the function's `prototype`.

- **Trade-offs**: The catch is confusing `__proto__` and `prototype` properties - `__proto__` is the actual link, `prototype` is only on functions. Arrow functions don't have `prototype` property, which is why these can't be used as constructors. Understanding this difference is key to understanding how inheritance works in JavaScript.

Example:

```js
function Person() {}
Person.prototype.greet = () => 'hi';
const p = new Person();
console.log(p.__proto__ === Person.prototype); // true

```

---

## Q31. 🤔 `hasOwn` vs `in` operator

`Object.hasOwn` checks if a property exists on the object itself (not inherited), while `in` operator checks the entire prototype chain including inherited properties. `Object.hasOwn` is the modern safer way to check own properties - it works everywhere, even on objects created with `Object.create(null)`.

- **Trade-offs**: The catch is `in` checks the entire prototype chain, so it returns `true` for inherited properties, while `Object.hasOwn` only checks the object itself. Use `in` when you need to check inherited properties, but use `Object.hasOwn` for own property checks since it's safer and more reliable than `hasOwnProperty`.

Example:

```js
const obj = { a: 1 };
Object.setPrototypeOf(obj, { b: 2 });

console.log(Object.hasOwn(obj, 'a')); // true - own property
console.log(Object.hasOwn(obj, 'b')); // false - inherited property
console.log('a' in obj); // true - found in object
console.log('b' in obj); // true - found in prototype chain

// Object.hasOwn works even on objects without hasOwnProperty
const nullObj = Object.create(null);
nullObj.x = 1;
console.log(Object.hasOwn(nullObj, 'x')); // true - works perfectly

```

---

## Q32. 🔧 `Object.create()` vs `new` operator

`Object.create()` sets up prototype links directly, while `new` operator calls a constructor function and sets up the prototype automatically - `Object.create` is explicit, `new` is more convenient. `Object.create` is great for simple inheritance, while `new` is better for constructor-based object creation.

- **Trade-offs**: The catch is using `new` when `Object.create` would be simpler - `Object.create` is explicit and gives you more control, while `new` is syntactic sugar that does constructor chaining automatically. `Object.create(null)` creates objects without a prototype, which is useful for pure data structures.

Example:

```js
const base = { x: 1 };
const child = Object.create(base);
child.y = 2;

function Parent(x) { this.x = x; }
const child2 = new Parent(1);

```

---

## Q33. 🤔 `Object.assign()` vs spread operator

`Object.assign()` copies properties from source objects to a target object, while spread operator creates a new object with copied properties - both do shallow copies. `Object.assign` mutates the target, while spread creates a new object.

- **Trade-offs**: The catch is both do shallow copies, so nested objects are still shared - use deep cloning if you need complete independence. Spread is more modern and readable, but `Object.assign` is useful when you need to mutate an existing object or copy to multiple targets.

Example:

```js
const obj1 = { a: 1, nested: { b: 2 } };
const obj2 = Object.assign({}, obj1);
const obj3 = { ...obj1 };
// Both create shallow copies - nested objects are shared

```

---

## Q34. 🤔 `Object.freeze()` vs `Object.seal()`

`Object.freeze()` makes an object completely immutable - you can't add, delete, or modify properties. `Object.seal()` prevents adding or deleting properties but allows modifying existing ones. Both prevent adding new properties, but `freeze` is stricter.

- **Trade-offs**: The catch is both are shallow - nested objects aren't frozen or sealed, so you need to recursively freeze/seal if you want complete immutability. `freeze` is useful for constants, while `seal` is useful when you want to prevent property additions but allow modifications.

Example:

```js
const obj1 = { x: 1 };
Object.freeze(obj1);
obj1.x = 2; // silently fails in strict mode

const obj2 = { x: 1 };
Object.seal(obj2);
obj2.x = 2; // works
obj2.y = 3; // fails

```

---

## Q35. 🤔 `Object.keys()` vs `Object.getOwnPropertyNames()`

`Object.keys()` returns only enumerable own property names, while `Object.getOwnPropertyNames()` returns all own property names including non-enumerable ones. Both ignore inherited properties, but `getOwnPropertyNames` includes properties like `length` on arrays.

- **Trade-offs**: The catch is `Object.keys` skips non-enumerable properties, which can be surprising if you've defined properties with `Object.defineProperty` with `enumerable: false`. Use `getOwnPropertyNames` when you need all properties, or `Object.keys` when you only need enumerable ones.

Example:

```js
const obj = {};
Object.defineProperty(obj, 'hidden', { value: 1, enumerable: false });
console.log(Object.keys(obj)); // []
console.log(Object.getOwnPropertyNames(obj)); // ['hidden']

```

---

## Q36. 🤔 `Object.entries()` vs `Object.values()` vs `Object.keys()`

`Object.keys()` returns an array of property names (keys), `Object.values()` returns an array of property values, and `Object.entries()` returns an array of `[key, value]` pairs - all three only include enumerable own properties. `keys` is useful when you need just the property names, `values` when you only need values, and `entries` when you need both keys and values together.

- **Trade-offs**: All three ignore inherited and non-enumerable properties, so they only work with own enumerable properties. `keys` is great for iterating over property names, `values` for processing just the values, and `entries` is perfect for converting objects to maps or iterating with destructuring.

Example:

```js
const obj = { a: 1, b: 2 };
console.log(Object.keys(obj)); // ['a', 'b']
console.log(Object.values(obj)); // [1, 2]
console.log(Object.entries(obj)); // ['a', 1], ['b', 2]

```

---

## Q37. 💡 Getters and setters in JavaScript

Getters and setters are special methods that control property access, allowing custom logic on read/write - getters run when reading, setters run when writing. They're useful for validation, computed properties, and data transformation.

- **Trade-offs**: The catch is forgetting to handle edge cases in setters can cause bugs - always validate input in setters. Getters without setters create read-only properties, which is useful for computed values. You can add getters/setters with `Object.defineProperty` for more control.

Example:

```js
const obj = {
  _value: 0,
  get count() { return this._value; },
  set count(v) { this._value = Math.max(0, v); }
};
obj.count = -5; // becomes 0

```

---

## Q38. 🏛️ Classes in JavaScript

Classes in JavaScript are syntactic sugar over prototype-based inheritance - they provide a cleaner way to create objects and handle inheritance, but work like constructor functions underneath. `typeof Person` is `'function'` because classes are just constructor functions with special syntax.

- **Trade-offs**: The catch is thinking classes are completely different from functions - they're just constructor functions with better syntax. Methods go on `prototype`, not on instances, which is the same as constructor functions. Classes enforce `new` usage and have better tooling, but they work the same way under the hood.

Example:

```js
class Person {
  constructor(name) { this.name = name; }
  greet() { return `Hi, I'm ${this.name}`; }
}
const p = new Person('Alice');

```

---

## Q39. 🏛️ Class declaration vs class expression

Class declarations create classes with names, while class expressions create classes as values - both create constructor functions, but expressions are useful when you need classes as values. Named expressions help with debugging, and expressions are useful for conditional class creation.

- **Trade-offs**: Both declarations and expressions create constructor functions, so they work the same way. The catch is not understanding that classes are functions - use expressions when you need classes as values, or declarations when you want hoisting (though class declarations aren't fully hoisted like function declarations).

Example:

```js
class MyClass {} // declaration
const MyClass = class {}; // expression
const Named = class Inner {}; // named expression

```

---

## Q40. ❓ `extends` keyword and how it works

`extends` allows one class to inherit from another class, giving it access to all the parent's properties and methods - it creates a prototype chain between classes. `super` is lexically bound, not dynamic, which means it always refers to the parent class in the same lexical scope.

- **Trade-offs**: The catch is forgetting to call `super()` in constructor - you must call it before using `this` in a child constructor. `extends` is great for building class hierarchies and reusing parent functionality, but watch out for deep inheritance chains which can make code harder to understand.

Example:

```js
class Animal {
  speak() { return 'sound'; }
}
class Dog extends Animal {
  speak() { return 'woof'; }
}

```

---

## Q41. ❓ `super()` and when to use it

`super()` calls the parent class constructor and must be called before using `this` in a child constructor - it initializes parent properties in child constructors. `super()` returns the current instance, not the parent, which can be confusing.

- **Trade-offs**: The catch is trying to use `this` before calling `super()` - you'll get a reference error. `super()` must be called first in the constructor, and it's required when the parent has a constructor. You can also use `super.method()` to call parent methods, which is useful for method overriding.

Example:

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

## Q42. 🏛️ Static members in classes

Static methods and properties belong to the class itself, not to individual instances, and are called directly on the class - they're useful for utility functions and constants. Static members are inherited by subclasses, so child classes can access parent static methods.

- **Trade-offs**: The catch is trying to access `this` in static methods - `this` refers to the class, not an instance. Static members are great for utility functions, constants, and factory methods, but watch out - these can't access instance properties or methods.

Example:

```js
class Math {
  static add(a, b) { return a + b; }
  static PI = 3.14;
}
Math.add(1, 2); // 3

```

---

## Q43. 🏛️ Private class fields

Private fields use the `#` prefix and can only be accessed from within the same class, making them truly private - they're not just conventionally private like `_private`. Private fields are not accessible from subclasses, which is different from protected fields in other languages.

- **Trade-offs**: The catch is forgetting the `#` prefix when accessing private fields - you'll get a syntax error. Private fields are great for hiding internal implementation details, but they're not accessible from subclasses, which can be limiting. Use `_private` for conventional privacy that subclasses can access, or `#private` for true privacy.

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

---

## Q44. 🔗 ES6 classes vs prototype-based inheritance

Classes provide cleaner syntax but work exactly like constructor functions and prototypes underneath - they're just syntactic sugar over prototype-based inheritance. Both approaches create the same result, so choose based on preference and tooling support.

- **Trade-offs**: The catch is thinking classes are completely different from functions - they compile to the same prototype-based code. Classes enforce `new` usage and have better tooling, but they work the same way under the hood. Use classes for cleaner syntax, or constructor functions if you need more control or are targeting older environments.

Example:

```js
class Person { constructor(name) { this.name = name; } }
const p1 = new Person('Alice');

function Person(name) { this.name = name; }
const p2 = new Person('Bob');

```

---

---

## 📍 Navigation

<div align="center">

[Functions, Closures & Execution Context](2%29%20Functions%2C%20Closures%20%26%20Execution%20Context.md) • [Home: README](../README.md) • [ES6+ Features →](4%29%20ES6%2B%20Features.md)

[📋 Cheatsheet](JavaScript%20Interview%20Cheatsheet.md]

</div>

---
