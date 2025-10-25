# 🏗️ Objects, Classes & Prototypes — Q46-Q65

---

## 1️⃣ What are objects in JavaScript?

**🧠 Concept**

Objects are collections of key-value pairs that represent data and behavior.

**💻 Example**

```js
const user = {
  name: "Kamal",
  age: 31,
  greet() {
    console.log(`Hi, I'm ${this.name}`);
  }
};
user.greet(); // Hi, I'm Kamal
```

🧠 **Diagram:**

```
user
 ├─ name: "Kamal"
 ├─ age: 31
 └─ greet(): function
```

**💬 Explanation + Insight**


- **String Keys** - Keys are always strings or symbols
- **Object Creation** - Objects can be created via literals `{}`, `new Object()`, or factories/classes
- **Everything is Object** - Everything (except primitives) in JS is an object

---

## 2️⃣ What is prototypal inheritance?

**🧠 Concept**


In JS, objects can **inherit properties and methods** from other objects via the prototype chain.

**💻 Example**

```js
const animal = { eats: true };
const dog = Object.create(animal);
dog.barks = true;

console.log(dog.eats); // true (inherited)
```

🧠 **Diagram:**

```
dog ---> animal ---> Object.prototype ---> null
```

**💬 Explanation + Insight**



* JavaScript uses **prototype-based inheritance**, not classical (like Java).
* `Object.create()` allows direct prototype assignment.
* Property lookup travels **up the chain** if not found on the object itself.

---

## 3️⃣ How does the prototype chain work?

**🧠 Concept**


When you access a property on an object, JS looks for it on the object first — if not found, it moves up the prototype chain until it reaches `null`.

**💻 Example**

```js
let obj = { a: 1 };
let child = Object.create(obj);
child.b = 2;
console.log(child.a); // found in parent prototype
```

🧠 **Diagram:**

```
child.b (own)
  ↓
obj.a (prototype)
  ↓
Object.prototype
  ↓
null
```

**💬 Explanation + Insight**



* The prototype chain enables inheritance without classes.
* The lookup process is **runtime dynamic** — no copying, just referencing.

---

## 4️⃣ What is the difference between `__proto__` and `prototype`?

**🧠 Concept**



* `__proto__`: the *actual* internal link to the object's prototype.
* `prototype`: a property that exists only on **constructor functions** and **classes**, used to define methods for all instances.

**💻 Example**

```js
function Person(name) { this.name = name; }
Person.prototype.greet = function() { console.log(`Hi ${this.name}`); };

const kamal = new Person("Kamal");
console.log(kamal.__proto__ === Person.prototype); // true
```

🧠 **Diagram:**

```
kamal.__proto__  Person.prototype
Person.prototype.__proto__  Object.prototype
```

**💬 Explanation + Insight**



* `__proto__` is *instance  prototype link*
* `prototype` is *constructor  shared methods*
* Always avoid setting `__proto__` directly — use `Object.create()` instead.

---

## 5️⃣ What is object destructuring?

**🧠 Concept**


Destructuring extracts specific properties from an object into separate variables.

**💻 Example**

```js
const user = { name: "Kamal", age: 31 };
const { name, age } = user;
console.log(name, age);
```

🧠 **Diagram:**

```
user = { name: "Kamal", age: 31 }
↓
{name, age}  extracted  variables
```

**💬 Explanation + Insight**



* Default values and nested destructuring are supported:

```js
const { city = "Unknown" } = user;
```

* Useful in function arguments and React hooks.

---

## 6️⃣ What are getters and setters?

**🧠 Concept**


They allow you to define **computed properties** that act like normal fields but run logic when accessed or modified.

**💻 Example**

```js
const person = {
  firstName: "Kamal",
  lastName: "Sharma",
  get fullName() {
    return `${this.firstName} ${this.lastName}`;
  },
  set fullName(name) {
    [this.firstName, this.lastName] = name.split(" ");
  }
};

person.fullName = "John Doe";
console.log(person.firstName); // John
```

🧠 **Diagram:**

```
person.fullName
 ├─ get  combine fields
 ├─ set  split into first/last
```

**💬 Explanation + Insight**



* Getters/setters make APIs more **natural** and **controlled**.
* Often used in frameworks (like Vue.js reactivity system).

---

## 7️⃣ What is `Object.create()` used for?

**🧠 Concept**


`Object.create(proto)` creates a new object with the specified prototype.

**💻 Example**

```js
const animal = { eats: true };
const rabbit = Object.create(animal);
rabbit.jumps = true;
console.log(rabbit.eats); // true
```

🧠 **Diagram:**

```
rabbit  __proto__  animal  __proto__  Object.prototype
```

**💬 Explanation + Insight**



* It's the cleanest way to implement **prototype inheritance**.
* Second optional arg lets you define **property descriptors**.

---

## 8️⃣ What are static methods in classes?

**🧠 Concept**


Static methods belong to the **class itself**, not to instances.

**💻 Example**

```js
class MathUtils {
  static add(a, b) { return a + b; }
}
console.log(MathUtils.add(3, 4)); // 7
```

🧠 **Diagram:**

```
MathUtils
 ├─ static add()
Instances (new MathUtils()) ❌ don't have it
```

**💬 Explanation + Insight**


Used for **utility functions**, e.g., `Array.isArray()`.
They can't be called on instances, only on the class itself.

---

## 9️⃣ What are private fields in ES2022 classes?

**🧠 Concept**


Private fields start with `#` and can only be accessed inside the class definition.

**💻 Example**

```js
class User {
  #password = "secret";
  checkPassword(pwd) {
    return this.#password === pwd;
  }
}
const u = new User();
console.log(u.checkPassword("secret")); // true
console.log(u.#password); // ❌ SyntaxError
```

🧠 **Diagram:**

```
User
 ├─ #password (private)
 └─ checkPassword()
```

**💬 Explanation + Insight**



* Enforced privacy at language level (not symbolic).
* Cannot be inherited or accessed via `this["#field"]`.
* Great for encapsulation in modern class APIs.

---

## 🔟 What are class fields and why were they introduced?

**🧠 Concept**


Class fields let you define properties **directly inside class definitions**, not just in constructors.

**💻 Example**

```js
class Counter {
  count = 0;
  increment = () => this.count++;
}
const c = new Counter();
c.increment();
console.log(c.count); // 1
```

🧠 **Diagram:**

```
Class fields:
count = 0 (instance property)
increment() = arrow fn bound to instance
```

**💬 Explanation + Insight**



* Helps avoid constructor boilerplate.
* Arrow functions ensure `this` stays bound correctly.
* Makes class syntax cleaner and more predictable.

---

## ⚠️ Interview Gotchas & Quick Tips (Objects & Prototypes)

1. 🧠 **`__proto__` vs `prototype`:**

   * `obj.__proto__`  points *to* prototype
   * `Func.prototype`  object *used for new instances*

2. 🧱 **Prototype chain lookup order:**
   Own property  prototype  Object.prototype  null

3. ⚔️ **Shadowing:**

   ```js
   const obj = { a: 1 };
   const child = Object.create(obj);
   child.a = 2;
   console.log(child.a); // 2 (shadows parent)
   ```

4. 🪄 **Static methods ≠ instance methods:**

   ```js
   class A { static hi() {} }
   new A().hi(); // ❌ TypeError
   ```

5. 🔐 **Private fields are not enumerable:**
   They don't appear in `Object.keys()` or JSON.stringify.

6. 🔄 **`Object.assign()` makes a shallow copy** — nested objects remain referenced.

7. 🧩 **Inheritance chain with classes:**

   ```js
   class A {}
   class B extends A {}
   console.log(B.prototype.__proto__ === A.prototype); // true
   ```

8. 🧰 **Use Object.create(null)** when you want an object **with no prototype** — useful for pure key-value maps.

9. ⚡ **Classes are just syntactic sugar** over prototypes — under the hood they still use the same prototype chain.

10. 🧩 **Functions are objects too:**

```js
function fn() {}
console.log(typeof fn); // "function"
console.log(fn.__proto__ === Function.prototype); // true
```

---

## 11️⃣ How does inheritance work with ES6 classes?

**🧠 Concept**


`extends` lets one class inherit another's properties & methods.

**💻 Example**

```js
class Animal {
  eat() { console.log("Eating"); }
}
class Dog extends Animal {
  bark() { console.log("Woof!"); }
}
const d = new Dog();
d.eat();  // Eating ✅ (from parent)
```

🧠 **Prototype Chain Diagram:**

```
d ─▶ Dog.prototype ─▶ Animal.prototype ─▶ Object.prototype ─▶ null
```

**💬 Explanation + Insight**


Each subclass prototype points to its parent's prototype.
This chain enables **method lookup across generations**.

---

## 12️⃣ What is the difference between composition and inheritance?

**🧠 Concept**



* **Inheritance:** "is-a" relationship — Dog *is an* Animal.
* **Composition:** "has-a" relationship — Car *has an* Engine.

**💻 Example**

```js
// Composition
const canBark = obj => ({ ...obj, bark: () => "Woof" });
const canEat  = obj => ({ ...obj, eat: () => "Nom" });

const dog = canEat(canBark({ name: "Buddy" }));
console.log(dog.bark(), dog.eat());
```

🧠 **Diagram:**

```
Dog = Bark + Eat + (other traits)
```

**💬 Explanation + Insight**


Prefer **composition** for flexible architectures — avoids deep, rigid inheritance chains.

---

## 13️⃣ How does `super()` work in ES6 classes?

**🧠 Concept**


`super()` calls the **constructor of the parent class** or accesses parent methods.

**💻 Example**

```js
class Animal {
  constructor(name) { this.name = name; }
  speak() { console.log(`${this.name} makes a noise`); }
}
class Dog extends Animal {
  constructor(name) {
    super(name); // must call before using this
  }
  speak() {
    super.speak();
    console.log(`${this.name} barks`);
  }
}
new Dog("Kamal").speak();
```

🧠 **Diagram:**

```
Dog  super()  Animal
Dog.speak()  super.speak()
```

**💬 Explanation + Insight**



* Must call `super()` before accessing `this`.
* Also used for **method overriding** with parent access.

---

## 14️⃣ What is the difference between mixins and multiple inheritance?

**🧠 Concept**


JS doesn't support multiple inheritance, so **mixins** are used to add features from multiple sources.

**💻 Example**

```js
const canFly  = Base => class extends Base { fly() { console.log("Flying"); } };
const canSwim = Base => class extends Base { swim() { console.log("Swimming"); } };

class Animal {}
class Duck extends canSwim(canFly(Animal)) {}
new Duck().fly(); // Flying
```

🧠 **Diagram:**

```
Duck
 ├─ from canFly
 └─ from canSwim
```

**💬 Explanation + Insight**


Mixins promote **horizontal code sharing** — more flexible than deep class trees.

---

## 15️⃣ What are factory functions?

**🧠 Concept**


A factory function **returns a new object** instead of using `new`.

**💻 Example**

```js
function createUser(name) {
  return {
    name,
    greet() { console.log(`Hi ${this.name}`); }
  };
}
const u = createUser("Kamal");
u.greet();
```

🧠 **Diagram:**

```
createUser()  returns  plain object
```

**💬 Explanation + Insight**



* No prototype linkage unless you add one.
* Easier to mix features or create closures for private data.

---

## 16️⃣ How do you create a deep clone of an object?

**🧠 Concept**


A deep clone copies **nested objects** too, not just top-level references.

**💻 Example**

```js
const obj = { a: 1, b: { c: 2 } };
const deep = structuredClone(obj);
deep.b.c = 99;
console.log(obj.b.c); // 2 ✅
```

🧠 **Diagram:**

```
Original  separate memory  Clone
```

**💬 Explanation + Insight**



* `structuredClone()` (modern & safe)
* Fallback: `JSON.parse(JSON.stringify(obj))`
* Or libraries: Lodash `cloneDeep()`

---

## 17️⃣ What are `Object.freeze()` and `Object.seal()`?

**🧠 Concept**



* `freeze()`  can't add/remove/change properties.
* `seal()`  can't add/remove, but can modify existing values.

**💻 Example**

```js
const obj = { a: 1 };
Object.freeze(obj);
obj.a = 2; // ignored
```

🧠 **Diagram:**

```
freeze  lock all
seal    lock structure only
```

**💬 Explanation + Insight**



* Both are **shallow** — nested objects remain mutable.
* Use deep-freeze recursively for true immutability.

---

## 18️⃣ What are WeakMaps and WeakSets?

**🧠 Concept**


They store **object keys** without preventing garbage collection.

**💻 Example**

```js
let obj = {};
const wm = new WeakMap();
wm.set(obj, "secret");
obj = null; // entry auto-removed
```

🧠 **Diagram:**

```
WeakMap
 └─ [obj]  "secret"
(obj deleted ⇒ key removed)
```

**💬 Explanation + Insight**



* Keys must be objects.
* Ideal for **private data** or **DOM element caching**.

---

## 19️⃣ What are Maps and Sets in ES6 and their advantages?

**🧠 Concept**



* **Map:** key–value pairs (keys can be any type).
* **Set:** unique values (no duplicates).

**💻 Example**

```js
const map = new Map([["a", 1]]);
map.set("b", 2);

const set = new Set([1, 2, 2]);
console.log(set.size); // 2
```

🧠 **Diagram:**

```
Map  { "a"1, "b"2 }
Set  [1,2]
```

**💬 Explanation + Insight**



* Maintain insertion order.
* More performant than plain objects for frequent add/remove.
* Iterables  support `for...of`.

---

## 20️⃣ How do you check if an object has a property (3 methods)?

**🧠 Concept**


1️⃣ `'key' in obj` 2️⃣ `obj.hasOwnProperty('key')` 3️⃣ `Object.hasOwn(obj,'key')`

**💻 Example**

```js
const car = { brand: "Tesla" };
console.log("brand" in car);              // true
console.log(car.hasOwnProperty("brand")); // true
console.log(Object.hasOwn(car, "brand")); // true
```

🧠 **Diagram:**

```
"key" in obj  checks prototype chain
hasOwn...     checks only own keys
```

**💬 Explanation + Insight**


Use `Object.hasOwn()` (ES2022) — it's safe even if `hasOwnProperty` is shadowed.

---

## ⚠️ Interview Gotchas & Quick Tips (Objects & Classes Part 2)

1. 🧩 **Prototype chain clarity:**

   ```js
   instance.__proto__ === Class.prototype // ✅
   Class.__proto__ === Function.prototype // ✅
   Class.prototype.__proto__ === Parent.prototype // ✅ when extends
   ```

2. ⚔️ **Arrow in class fields:**
   Arrow functions auto-bind `this`:

   ```js
   class C { click = () => this; }
   ```

3. 🔒 **Freeze ≠ deep freeze:**
   Nested objects still mutable  use recursive freeze.

4. 🧠 **WeakMap advantage:**
   Automatically clears memory — no manual delete.

5. 🪄 **Map vs Object:**

   * Map preserves insertion order
   * Keys of any type
   * Easier iteration (`for…of`)

6. 🔄 **Mixins + composition = flexible re-use**
   No diamond problem like C++ multiple inheritance.

7. 🧰 **Factory functions** are simpler for data encapsulation than classes — great for closures.

8. ⚡ **Don't confuse `Object.create()` with `new`:**

   * `new` links to Function.prototype
   * `Object.create()` links directly to the passed object

9. 🧩 **`super()` must be called** before accessing `this` in subclass constructors — otherwise `ReferenceError`.

10. 🧱 **Class fields** defined outside constructors are initialized **per instance**, not shared like prototype methods.

---

*This section covers all aspects of JavaScript objects, classes, and prototypes - from basic concepts to advanced patterns and gotchas.*
