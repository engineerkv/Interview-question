---
sidebar_label: "Output-Based Questions"
---
# 📊 8. Output-Based Questions (Q148–207)

> **Reviewed:** 2026-09 · Modernized; legacy topics are labeled.

> **How to read these outputs:** Unless a snippet says otherwise, outputs assume a *classic script in sloppy mode* - for example, pasted into a browser console. That matters for `this`: in sloppy mode a plain function call gets `this === globalThis`, so `this.a` is usually `undefined`. In **ES modules, class bodies, and `'use strict'` code**, a plain call gets `this === undefined`, so reading `this.a` throws a `TypeError` instead, and silent failures (writing to frozen objects, implicit globals) become thrown errors. Array output uses Node's `console.log` format. For the underlying rules, [MDN's JavaScript reference](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference) is the most reliable source.

---

## Q148. ⚡ Event loop ordering with timers, promises, and microtasks

**Why:** The event loop always finishes the current synchronous script first. Then it drains the *entire* microtask queue (promise reactions and `queueMicrotask` callbacks, in the order they were queued) before it takes the next macrotask, such as a `setTimeout` callback - so a 0 ms timer still runs last.

- **Trade-offs**: The catch is assuming timers beat promises—microtasks always drain before the macrotask queue, so timers run last even with zero delay.

Example:

```js
console.log('Start'); // Synchronous: executes immediately
setTimeout(() => console.log('Timeout'), 0); // Macrotask: scheduled for next event loop tick
Promise.resolve().then(() => console.log('Promise')); // Microtask: executes before macrotasks
queueMicrotask(() => console.log('Microtask')); // Microtask: executes before macrotasks
console.log('End'); // Synchronous: executes immediately
// Execution order: sync code → microtasks → macrotasks

```

Output:

```

Start
End
Promise
Microtask
Timeout

```

---

## Q149. ⚡ Async/await vs synchronous code and timers

**Why:** Code in an `async` function runs synchronously until the first `await`, so `async1 start` and `async2` print immediately. The `await` suspends `async1` and queues its continuation as a microtask; the `new Promise` executor also runs synchronously (`promise1`). After `script end`, microtasks drain in queue order (`async1 end`, then `promise2`), and only then does the timer fire.

- **Trade-offs**: The catch is expecting `async/await` to block like synchronous code—other synchronous logs finish before awaited work resumes.

Example:

```js
async function async1() {
  console.log('async1 start'); // Synchronous: executes immediately
  await async2(); // Pauses here, rest of function becomes microtask
  console.log('async1 end'); // Microtask: executes after await resolves
}

async function async2() {
  console.log('async2'); // Synchronous: executes immediately
}

console.log('script start'); // Synchronous: executes first
setTimeout(() => console.log('setTimeout'), 0); // Macrotask: scheduled
async1(); // Calls async function
new Promise(resolve => {
  console.log('promise1'); // Synchronous: executor runs immediately
  resolve();
}).then(() => console.log('promise2')); // Microtask: scheduled
console.log('script end'); // Synchronous: executes before microtasks
// Order: sync → microtasks (async1 end, promise2) → macrotasks (setTimeout)

```

Output:

```

script start
async1 start
async2
promise1
script end
async1 end
promise2
setTimeout

```

---

## Q150. 💡 Property descriptors, getters/setters, and non-configurable fields

**Why:** The setter stores `value * 2`, so reading gives `20`. Because the property was defined with `configurable: false`, `delete obj.prop` fails - it returns `false` in sloppy mode (and would throw a `TypeError` in strict mode) - so the accessor survives and the second read is still `20`.

- **Trade-offs**: The catch is thinking `delete` removes any property—non-configurable descriptors stay put; setters still run on assignment, doubling the stored value.

Example:

```js
const obj = {};
Object.defineProperty(obj, 'prop', {
  get() { return this._value; },
  set(value) { this._value = value * 2; },
  enumerable: true,
  configurable: false
});

obj.prop = 10;
console.log(obj.prop);
delete obj.prop;
console.log(obj.prop);

```

Output:

```

20
20

```

---

## Q151. 🔗 Prototype methods, deletion, and fallback behavior

**Why:** `greet` lives on `Person.prototype`, not on `person`. `delete person.greet` only removes *own* properties, so it's a no-op and lookup still finds the prototype method. Once you delete it from the prototype, the lookup reaches `Object.prototype`, finds nothing, and calling `undefined` throws `TypeError: person.greet is not a function`.

- **Trade-offs**: The catch is assuming `delete person.greet` kills the method—only `delete Person.prototype.greet` removes the shared implementation.

Example:

```js
function Person(name) {
  this.name = name;
}

Person.prototype.greet = function() {
  console.log(`Hello, ${this.name}`);
};

const person = new Person('John');
person.greet();

delete person.greet;
person.greet();

delete Person.prototype.greet;
person.greet();

```

Output:

```

Hello, John
Hello, John
person.greet is not a function

```

---

## Q152. 🔗 Prototype inheritance, hasOwnProperty, and deletion side effects

**Why:** `a` is inherited through `Object.create(parent)`, so `hasOwnProperty('a')` is `false`. `delete child.a` only affects own properties, so the inherited `1` is still visible. `b` is an own property, so deleting it really removes it and the read becomes `undefined`.

- **Trade-offs**: The catch is treating inherited properties as removable from the child—only own properties vanish with `delete`.

Example:

```js
const parent = { a: 1 };
const child = Object.create(parent);
child.b = 2;

console.log(child.a);
console.log(child.b);
console.log(child.hasOwnProperty('a'));
console.log(child.hasOwnProperty('b'));

delete child.a;
console.log(child.a);

delete child.b;
console.log(child.b);

```

Output:

```

1
2
false
true
1
undefined

```

---

## Q153. 📦 Object.freeze on objects and arrays

**Why:** `Object.freeze` makes existing properties read-only and the object non-extensible. Plain assignments like `obj.a = 2` or `arr[0] = 10` are *silently ignored* in sloppy mode. But `arr.push(4)` is different: built-in methods like `push` always throw when they can't write, even in sloppy mode, so the script stops with a `TypeError` before `console.log(arr)` runs.

- **Trade-offs**: The catch is assuming sloppy mode always fails silently - plain property writes do, but array methods like `push`, `pop`, and `splice` throw on frozen arrays regardless of mode. Freeze is also shallow: nested objects stay mutable.

Example:

```js
const obj = { a: 1 };
Object.freeze(obj);
obj.a = 2;
obj.b = 3;

console.log(obj.a);
console.log(obj.b);

const arr = [1, 2, 3];
Object.freeze(arr);
arr[0] = 10;
arr.push(4);

console.log(arr);

```

Output:

```

1
undefined
TypeError: Cannot add property 3, object is not extensible

```

---

## Q154. 🔒 Nested closures and shared lexical state

**Why:** `inner` and `innermost` both close over the *same* `count` variable created by the single `outer()` call - closures capture variables, not copies of values. Every call increments that shared binding: `fn()` → 1, `innerFn()` → 2, `fn()` again → 3.

- **Trade-offs**: The catch is assuming each returned function gets a fresh copy—incrementing inside one closure affects every consumer sharing the scope.

Example:

```js
function outer() {
  let count = 0;
  return function inner() {
    count++;
    console.log(count);
    return function innermost() {
      count++;
      console.log(count);
    };
  };
}

const fn = outer();
const innerFn = fn();
innerFn();
fn();

```

Output:

```

1
2
3

```

---

## Q155. 📝 `var` vs `let` in loops with asynchronous callbacks

**Why:** `var` is function-scoped, so all three callbacks share one `i`, which is already `3` when the timers fire. `let` in a `for` header creates a fresh binding for each iteration, so each callback captures its own `j` (0, 1, 2).

- **Trade-offs**: The catch is expecting `var` to retain per-iteration values—use `let` (or IIFEs) when closures inside loops need unique indexes.

Example:

```js
for (var i = 0; i < 3; i++) {
  setTimeout(() => console.log(i), 0);
}

for (let j = 0; j < 3; j++) {
  setTimeout(() => console.log(j), 0);
}

```

Output:

```

3
3
3
0
1
2

```

---

## Q156. 🔧 `this` binding differences between regular and arrow methods

**Why:** A regular function's `this` is decided by the call site: `obj.getValue()` sets `this` to `obj`. An arrow function has no `this` of its own - it uses the `this` of the surrounding scope (the top level here), so `this.value` is `undefined`. Pulling the method off the object (`extracted()`) loses the receiver, so `this` falls back to `globalThis` in sloppy mode.

- **Trade-offs**: The catch is expecting arrow methods to reference the object—they capture the surrounding scope (often `window`/`global`), so `this.value` becomes `undefined`.

Example:

```js
const obj = {
  value: 10,
  getValue: function() { return this.value; },
  getValueArrow: () => { return this.value; }
};

console.log(obj.getValue());
console.log(obj.getValueArrow());

const extracted = obj.getValue;
console.log(extracted());

```

Output:

```

10
undefined
undefined

```

---

## Q157. 🧬 Class inheritance, `super()`, and method extraction

**Why:** `Child`'s constructor overwrites `this.name` after `super()`, so `child.getName()` returns `'Child'`. But class bodies are **always strict mode**, so when you call the extracted method without a receiver, `this` is `undefined` - and `this.name` throws a `TypeError` instead of returning `undefined`.

- **Trade-offs**: The catch is thinking class methods auto-bind; use `.bind()` or arrow properties to maintain context when passing methods around.

Example:

```js
class Parent {
  constructor() { this.name = 'Parent'; }
  getName() { return this.name; }
}

class Child extends Parent {
  constructor() {
    super();
    this.name = 'Child';
  }
}

const child = new Child();
console.log(child.getName());

const extracted = child.getName;
console.log(extracted());

```

Output:

```

Child
TypeError: Cannot read properties of undefined (reading 'name')

```

---

## Q158. 💡 Regular methods, arrow methods, and nested arrows referencing `this`

**Why:** `obj.b()` is a method call, so `this` is `obj`. `c` is an arrow defined at the top level, so it uses the top-level `this` (not `obj`). Inside `d`, the nested arrow borrows `d`'s `this`, which is `obj` because `d` was called as `obj.d()`. `extracted()` is a plain call, so `this` is `globalThis` (sloppy) and `a` is `undefined`.

- **Trade-offs**: The catch is expecting arrow functions to use the object—they capture lexical `this`, so only regular methods (or nested arrows inside them) resolve properties.

Example:

```js
const obj = {
  a: 1,
  b: function() { console.log(this.a); },
  c: () => { console.log(this.a); },
  d() {
    const nested = () => { console.log(this.a); };
    nested();
  }
};

obj.b();
obj.c();
obj.d();

const extracted = obj.b;
extracted();

```

Output:

```

1
undefined
1
undefined

```

---

## Q159. ⚡ Async function returning a promise and chaining `.then()`

**Why:** `test()` logs `1` synchronously, then `await` suspends it and control returns to the caller, which logs `4`. The continuation logs `2`; returning a promise from an `async` function adopts that promise's value, so `.then(console.log)` eventually receives `'3'` (after a few extra microtask ticks).

- **Trade-offs**: The catch is expecting `await` to block other synchronous logs—`console.log('4')` runs before the async microtask resumes.

Example:

```js
async function test() {
  console.log('1');
  await Promise.resolve();
  console.log('2');
  return Promise.resolve('3');
}

test().then(console.log);
console.log('4');

```

Output:

```

1
4
2
3

```

---

## Q160. ⚡ Promise unwrapping and concurrent microtask ordering

**Why:** Both `.then` callbacks registered on already-resolved promises are queued as microtasks: first the one logging `1`, then the one logging `4`. Returning a promise from a `.then` handler doesn't resolve the chain immediately - adopting a thenable takes two extra microtask ticks - so `4` sneaks in before `2`, and `3` comes last.

- **Trade-offs**: The catch is expecting `.then()` chains to be isolated—microtasks share a global queue, so separate chains can interleave.

Example:

```js
Promise.resolve()
  .then(() => {
    console.log('1');
    return Promise.resolve('2');
  })
  .then(res => {
    console.log(res);
    return Promise.resolve('3');
  })
  .then(console.log);

Promise.resolve().then(() => console.log('4'));

```

Output:

```

1
4
2
3

```

---

## Q161. ⚡ Async `try/catch` with awaited rejections

**Why:** `return await` waits for the promise *inside* the `try` block, so the rejection is thrown right there and caught. The `catch` returns `'Caught'`, which fulfills the async function's promise, so `.then(console.log)` runs.

- **Trade-offs**: The catch is expecting the returned promise to reject—because the catch returns `'Caught'`, the caller’s `.then()` runs.

Example:

```js
async function test() {
  try {
    return await Promise.reject('Error');
  } catch (e) {
    return 'Caught';
  }
}

test().then(console.log).catch(console.error);

```

Output:

```

Caught

```

---

## Q162. ⚡ Returning a rejected promise without awaiting inside `try/catch`

**Why:** Without `await`, `return Promise.reject('Error')` just hands the rejected promise back - nothing throws inside the `try`, so the `catch` never runs. The async function's promise adopts the rejection and the caller's `.catch(console.error)` prints `Error`. That's why linters recommend `return await` inside `try` blocks.

- **Trade-offs**: The catch is expecting `try/catch` to intercept all promise rejections—you must `await` or use `.catch()` to trap errors.

Example:

```js
async function test() {
  try {
    return Promise.reject('Error');
  } catch (e) {
    return 'Caught';
  }
}

test().then(console.log).catch(console.error);

```

Output:

```

Error

```

---

## Q163. 💡 WeakMap keys and garbage collection

**Why:** The first `get` uses the real key object, so it returns `'value'`. After `obj = null`, the second call is literally `map.get(null)` - `null` was never a key (WeakMap keys must be objects), so it returns `undefined`. This has nothing to do with GC timing: the entry becomes *eligible* for garbage collection, but you can never observe when it's collected because WeakMaps aren't iterable.

- **Trade-offs**: The catch is thinking the second `undefined` proves the entry was garbage-collected - it only proves `null` isn't a key. WeakMaps are for attaching data to objects without keeping them alive (caches, private metadata); you can't enumerate them or check their size.

Example:

```js
const map = new WeakMap();
let obj = {};

map.set(obj, 'value');
console.log(map.get(obj));

obj = null;
console.log(map.get(obj));

```

Output:

```

value
undefined

```

---

## Q164. 💡 Symbol uniqueness and non-enumerability

**Why:** Every `Symbol()` call creates a brand-new unique value; the description is only a debugging label, so `sym1 === sym2` is `false` and both keys coexist. `Object.keys` only returns string keys, so the count is `0`.

- **Trade-offs**: The catch is expecting identical descriptions to be equal—Symbols compare by identity, so equality fails.

Example:

```js
const sym1 = Symbol('id');
const sym2 = Symbol('id');
const obj = {
  [sym1]: 'value1',
  [sym2]: 'value2'
};

console.log(obj[sym1]);
console.log(obj[sym2]);
console.log(sym1 === sym2);
console.log(Object.keys(obj).length);

```

Output:

```

value1
value2
false
0

```

---

## Q165. 📝 Proxies intercepting get/set for transformed values

**Why:** Every interaction goes through the handler. `proxy.b = 5` hits `set`, which stores `10` on the target. Reads hit `get`, which doubles again: `proxy.a` → `2`, `proxy.b` → `20`, and missing `c` → `0`. Reading `target` directly bypasses the proxy, showing the stored values `1` and `10`.

- **Trade-offs**: The catch is assuming the proxy leaves the target untouched—handlers can mutate or synthesize properties before hitting the target.

Example:

```js
const target = { a: 1 };
const handler = {
  get(target, prop) {
    return prop in target ? target[prop] * 2 : 0;
  },
  set(target, prop, value) {
    target[prop] = value * 2;
    return true;
  }
};

const proxy = new Proxy(target, handler);
proxy.b = 5;
console.log(proxy.a);
console.log(proxy.b);
console.log(proxy.c);
console.log(target.a);
console.log(target.b);

```

Output:

```

2
20
0
1
10

```

---

## Q166. 💡 Generator `next()` sequencing and completion records

**Why:** Each `next()` runs the generator to the next `yield` and reports `done: false`. The `return 4` produces the final `{ value: 4, done: true }`. After completion, the generator is closed, so every later `next()` returns `{ value: undefined, done: true }`.

- **Trade-offs**: The catch is expecting yields after `return`—once done, further `next()` calls stay done.

Example:

```js
function* generator() {
  yield 1;
  yield 2;
  yield 3;
  return 4;
}

const gen = generator();
console.log(gen.next());
console.log(gen.next());
console.log(gen.next());
console.log(gen.next());
console.log(gen.next());

```

Output:

```

{ value: 1, done: false }
{ value: 2, done: false }
{ value: 3, done: false }
{ value: 4, done: true }
{ value: undefined, done: true }

```

---

## Q167. ⚡ Async generators consumed via `for await...of`

**Why:** Inside an async generator, `yield` awaits a promise operand before handing it out, and `for await...of` awaits each `next()` call, so the loop receives plain values `1`, `2`, `3` in order. `Done` prints only after the loop sees `done: true`.

- **Trade-offs**: The catch is thinking you must manually `await` inside the loop—`for await...of` does it for you.

Example:

```js
async function* asyncGenerator() {
  yield Promise.resolve(1);
  yield Promise.resolve(2);
  yield Promise.resolve(3);
}

(async () => {
  for await (const value of asyncGenerator()) {
    console.log(value);
  }
  console.log('Done');
})();

```

Output:

```

1
2
3
Done

```

---

## Q168. 💡 Sparse array behavior and skipped slots in `map`

**Why:** Assigning `arr[10]` grows `length` to `11` and leaves indexes 3-9 as *holes* (no property at all). Reading a hole gives `undefined`, but `map` skips holes rather than calling the callback, so the result keeps the same holes. Node prints them as `<7 empty items>`.

- **Trade-offs**: The catch is expecting undefined entries to become `NaN`—`map` ignores holes entirely, leaving them empty.

Example:

```js
const arr = [1, 2, 3];
arr[10] = 10;

console.log(arr.length);
console.log(arr[5]);
console.log(arr);

const mapped = arr.map(x => x * 2);
console.log(mapped);

```

Output:

```

11
undefined
[ 1, 2, 3, <7 empty items>, 10 ]
[ 2, 4, 6, <7 empty items>, 20 ]

```

---

## Q169. 💡 Manipulating `array.length` to expand or truncate data

**Why:** `length` is writable. Setting it larger creates holes without adding elements; setting it smaller permanently deletes every element at or beyond the new length.

- **Trade-offs**: The catch is expecting lost elements to persist somewhere; shrinking length permanently discards them.

Example:

```js
const arr = [1, 2, 3];
arr.length = 10;
console.log(arr);
console.log(arr.length);

arr.length = 2;
console.log(arr);
console.log(arr.length);

```

Output:

```

[ 1, 2, 3, <7 empty items> ]
10
[ 1, 2 ]
2

```

---

## Q170. 💡 Set de-duplication and Map key overwrites

**Why:** A `Set` keeps only the first occurrence of each value (using SameValueZero comparison) and preserves insertion order. A `Map` built from entries overwrites the value when a key repeats, but the key keeps its *original* insertion position, so `'a'` stays first with value `3`.

- **Trade-offs**: The catch is expecting old values to stick around—Maps overwrite when keys repeat.

Example:

```js
const set = new Set([1, 2, 3, 3, 2, 1]);
console.log(set.size);
console.log([...set]);

const map = new Map([
  ['a', 1],
  ['b', 2],
  ['a', 3]
]);
console.log(map.size);
console.log([...map]);

```

Output:

```

3
[ 1, 2, 3 ]
2
[ [ 'a', 3 ], [ 'b', 2 ] ]

```

---

## Q171. 🤔 String vs symbol key enumeration

**Why:** String and symbol keys are stored separately. `Object.keys` (own enumerable strings) and `Object.getOwnPropertyNames` (own strings, including non-enumerable) skip symbols, `Object.getOwnPropertySymbols` returns only symbols, and `Reflect.ownKeys` returns everything - strings first, then symbols.

- **Trade-offs**: The catch is expecting `Object.keys` to include everything—only `Reflect.ownKeys` sees every key.

Example:

```js
const obj = {
  a: 1,
  b: 2,
  [Symbol('c')]: 3
};

console.log(Object.keys(obj));
console.log(Object.getOwnPropertyNames(obj));
console.log(Object.getOwnPropertySymbols(obj));
console.log(Reflect.ownKeys(obj));

```

Output:

```

[ 'a', 'b' ]
[ 'a', 'b' ]
[ Symbol(c) ]
[ 'a', 'b', Symbol(c) ]

```

---

## Q172. 📊 Getter/setter computed values affecting backing state

**Why:** `b` is an accessor with no storage of its own. Reading it computes `a * 2` (`2`). Assigning `10` runs the setter, which stores `10 / 2` into `a` (`5`), so the next read computes `10`.

- **Trade-offs**: The catch is expecting `b` to reflect the setter argument; instead, it mutates `a`, influencing future getter calls.

Example:

```js
const obj = {
  a: 1,
  get b() { return this.a * 2; },
  set b(value) { this.a = value / 2; }
};

console.log(obj.b);
obj.b = 10;
console.log(obj.a);
console.log(obj.b);

```

Output:

```

2
5
10

```

---

## Q173. 🔗 Prototype properties vs own properties with `hasOwnProperty`

**Why:** `a` is assigned in the constructor, so it's an own property. `b` lives on `Foo.prototype` and is found by lookup. Because instances *reference* the prototype rather than copying it, changing `Foo.prototype.b` later is immediately visible through `foo.b`.

- **Trade-offs**: The catch is expecting prototype changes to leave instances untouched—instances reference the shared prototype unless they define their own property.

Example:

```js
function Foo() {
  this.a = 1;
}

Foo.prototype.b = 2;

const foo = new Foo();
console.log(foo.a);
console.log(foo.b);
console.log(foo.hasOwnProperty('a'));
console.log(foo.hasOwnProperty('b'));

Foo.prototype.b = 3;
console.log(foo.b);

```

Output:

```

1
2
true
false
3

```

---

## Q174. 📦 Objects created with `Object.create(null)`

**Why:** `Object.create(null)` creates an object whose prototype is `null`, so there is no `Object.prototype` in its chain - no `toString`, no `hasOwnProperty`. That's what makes it a safe dictionary; use `Object.hasOwn(obj, key)` to check keys.

- **Trade-offs**: The catch is expecting built-in methods; these objects are dictionary-like and require manual handling.

Example:

```js
const obj = Object.create(null);
obj.a = 1;

console.log(obj.a);
console.log(obj.toString);
console.log(obj.hasOwnProperty);

```

Output:

```

1
undefined
undefined

```

---

## Q175. 📝 `Object.seal` allowing updates but blocking additions & deletions

**Why:** `Object.seal` makes the object non-extensible and every existing property non-configurable, but leaves them writable. So updating `a` works, while adding `b` and deleting `a` are silently ignored in sloppy mode (both would throw in strict mode).

- **Trade-offs**: The catch is expecting `seal` to behave like `freeze`; values still change.

Example:

```js
const obj = { a: 1 };
Object.seal(obj);
obj.a = 2;
obj.b = 3;
delete obj.a;

console.log(obj.a);
console.log(obj.b);
console.log(Object.isSealed(obj));

```

Output:

```

2
undefined
true

```

---

## Q176. 📊 `Object.preventExtensions` blocking new props only

**Why:** `Object.preventExtensions` only blocks *adding* properties. Existing properties can still be changed (and even deleted), so `a` becomes `2`, the `b` assignment is ignored (it throws in strict mode), and `isExtensible` reports `false`.

- **Trade-offs**: The catch is expecting new properties to appear—they’re silently ignored.

Example:

```js
const obj = { a: 1 };
Object.preventExtensions(obj);
obj.a = 2;
obj.b = 3;

console.log(obj.a);
console.log(obj.b);
console.log(Object.isExtensible(obj));

```

Output:

```

2
undefined
false

```

---

## Q177. 💡 Tagged template literal parameter breakdown

**Why:** A tag function receives the literal string pieces as its first argument (always one more piece than there are interpolations - here the last piece is `'!'`), followed by the evaluated interpolation values. The tag decides what to return; this one stitches the first two values back in, and since it ignores `strings[2]`, the trailing `!` is actually dropped.

- **Trade-offs**: The catch is expecting plain concatenation—tag functions receive structured arguments and can return anything.

Example:

```js
function tag(strings, ...values) {
  console.log(strings);
  console.log(values);
  return strings[0] + values[0] + strings[1] + values[1];
}

const name = 'John';
const age = 30;
const result = tag`Hello ${name}, you are ${age}!`;
console.log(result);

```

Output:

```

[ 'Hello ', ', you are ', '!' ]
[ 'John', 30 ]
Hello John, you are 30

```

---

## Q178. 🤔 Nullish coalescing vs optional chaining default handling

**Why:** `??` only falls back when the left side is `null` or `undefined`, so `0`, `false`, and `''` are kept (the last one prints as an empty line). Optional chaining short-circuits to `undefined` as soon as it hits `null`/`undefined`, instead of throwing a `TypeError`.

- **Trade-offs**: The catch is expecting falsy values like `0` or `''` to trigger defaults—they do not with `??`.

Example:

```js
const obj = {
  a: null,
  b: undefined,
  c: 0,
  d: false,
  e: ''
};

console.log(obj.a ?? 'default');
console.log(obj.b ?? 'default');
console.log(obj.c ?? 'default');
console.log(obj.d ?? 'default');
console.log(obj.e ?? 'default');

console.log(obj.a?.prop?.nested);
console.log(obj.b?.prop);
console.log(obj.f?.prop);

```

Output:

```

default
default
0
false
(empty line - the empty string '' is kept)
undefined
undefined
undefined

```

---

## Q179. 💡 Custom primitive conversion via `Symbol.toPrimitive`

**Why:** JavaScript passes a *hint* to `Symbol.toPrimitive`: unary `+` and `*` ask for `'number'` (42, and 42 * 2 = 84), `String()` asks for `'string'`. Binary `+` and loose `==` send `'default'`, because `+` could mean addition or concatenation - so `obj + ''` is `'default'`, and `obj == 'default'` is `true`.

- **Trade-offs**: The catch is expecting uniform conversion—operators send different hints, so results vary.

Example:

```js
const obj = {
  value: 10,
  [Symbol.toPrimitive](hint) {
    if (hint === 'number') return 42;
    if (hint === 'string') return 'hello';
    return 'default';
  }
};

console.log(+obj);
console.log(String(obj));
console.log(obj + '');
console.log(obj == 'default');
console.log(obj * 2);

```

Output:

```

42
hello
default
true
84

```

---

## Q180. 💡 BigInt arithmetic and equality comparisons

**Why:** BigInt arithmetic stays BigInt (`30n`, `typeof` is `'bigint'`). Strict equality compares types, so `10n === 10` is `false`, but `==` and relational operators compare mathematical values across BigInt and Number. You can't mix them in arithmetic (`10n + 5` throws), so convert explicitly with `Number()` or `BigInt()`.

- **Trade-offs**: The catch is expecting `===` to pass when comparing BigInt to Number—they differ; convert explicitly when needed.

Example:

```js
const a = 10n;
const b = 20n;

console.log(a + b);
console.log(typeof (a + b));
console.log(a === 10);
console.log(a == 10);
console.log(a > 5);
console.log(Number(a) + 5);

```

Output:

```

30n
bigint
false
true
true
15

```

---

## Q181. 🔧 Bound functions ignore subsequent `call`/`apply`

**Why:** `bind` returns a new function with its `this` permanently fixed. `call`/`apply` on a bound function can pass arguments, but they cannot override the bound `this` - the only thing that can is `new`.

- **Trade-offs**: The catch is expecting `call(obj2)` to override binding—it doesn’t for bound functions.

Example:

```js
function greet() {
  return this.name;
}

const obj1 = { name: 'John' };
const obj2 = { name: 'Jane' };

const boundGreet1 = greet.bind(obj1);
const boundGreet2 = greet.bind(obj2);

console.log(boundGreet1());
console.log(boundGreet2());
console.log(boundGreet1.call(obj2));
console.log(boundGreet2.apply(obj1));

```

Output:

```

John
Jane
John
Jane

```

---

## Q182. 💡 Destructuring defaults triggered only by `undefined`

**Why:** Destructuring defaults apply only when the value is strictly `undefined` (missing properties count as `undefined`). `null`, `0`, and `false` are real values, so they're kept.

- **Trade-offs**: The catch is expecting `null` to trigger defaults; only `undefined` does.

Example:

```js
const obj = { a: undefined, b: null, c: 0, d: false };

const { a = 'defaultA', b = 'defaultB', c = 'defaultC', d = 'defaultD', e = 'defaultE' } = obj;

console.log(a, b, c, d, e);

```

Output:

```

defaultA null 0 false defaultE

```

---

## Q183. 🔍 Variable shadowing across nested scopes

**Why:** Each `let x` creates a new binding in its own scope that *shadows* the outer one without touching it. Lookup walks outward from the current scope, so each `console.log` finds the nearest `x`, while `y` is only declared at the top and is found by every level.

- **Trade-offs**: The catch is expecting inner assignments to leak outward—each block scope gets its own binding.

Example:

```js
let x = 1;
let y = 2;

function outer() {
  let x = 10;

  function inner() {
    let x = 100;
    console.log(x, y);
  }

  inner();
  console.log(x, y);
}

outer();
console.log(x, y);

```

Output:

```

100 2
10 2
1 2

```

---

## Q184. 🤔 Strict-mode `this` vs method invocation contexts

**Why:** In strict mode, a plain function call gets `this === undefined` (no fallback to `globalThis`). `obj.test()` is a method call, so `this` is `obj`. `inner()` is again a plain call, so it gets `undefined` - nested regular functions don't inherit the outer `this`.

- **Trade-offs**: The catch is expecting nested inner functions to share the object’s `this`—they don’t unless you capture it or use arrow functions.

Example:

```js
'use strict';

function test() {
  console.log(this);
}

const obj = {
  test: function() {
    console.log(this);
    function inner() {
      console.log(this);
    }
    inner();
  }
};

test();
obj.test();

```

Output:

```

undefined
{ test: [Function: test] }
undefined

```

---

## Q185. 💡 Proxy traps customizing property access and enumeration

**Why:** The `get` trap doubles whatever the target holds: `a` → `2`, missing `c` → `undefined * 2` = `NaN`. The `has` trap forwards to `in`, and `Object.keys` uses the `ownKeys` trap plus each key's descriptor from the target, giving `['a', 'b']`.

- **Trade-offs**: The catch is expecting proxies to fall back on defaults—these can rewrite behavior entirely.

Example:

```js
const handler = {
  get(target, prop) {
    if (prop === 'constructor') return target.constructor;
    return target[prop] * 2;
  },
  has(target, prop) {
    return prop in target;
  },
  ownKeys(target) {
    return Object.keys(target);
  }
};

const target = { a: 1, b: 2 };
const proxy = new Proxy(target, handler);

console.log(proxy.a);
console.log('a' in proxy);
console.log(Object.keys(proxy));
console.log(proxy.c);

```

Output:

```

2
true
[ 'a', 'b' ]
NaN

```

---

## Q186. ⚠️ Generator `try/catch` catching internal errors

**Why:** The first two `next()` calls stop at `yield 1` and `yield 2`. The third resumes, hits `throw`, and control jumps to the generator's own `catch`, which yields `4` (`yield 3` is skipped). Execution then continues after the `try/catch` to `yield 5`, and the next call finishes the generator.

- **Trade-offs**: The catch is expecting `throw` to terminate the generator immediately—after handling, it may yield again.

Example:

```js
function* generator() {
  try {
    yield 1;
    yield 2;
    throw new Error('Error');
    yield 3;
  } catch (e) {
    yield 4;
  }
  yield 5;
}

const gen = generator();
console.log(gen.next());
console.log(gen.next());
console.log(gen.next());
console.log(gen.next());
console.log(gen.next());

```

Output:

```

{ value: 1, done: false }
{ value: 2, done: false }
{ value: 4, done: false }
{ value: 5, done: false }
{ value: undefined, done: true }

```

---

## Q187. 🔧 Mixed regular and arrow functions inside objects

**Why:** `b` is a method call, so `this` is `obj`. `c` is a top-level arrow, so it uses the top-level `this`, not `obj`. When `d` is called as `obj.d()`, its `this` is `obj`, so the arrow `e` (which borrows `d`'s `this`) and the regular function `f` (which reads the captured `self`) both see `obj.a`.

- **Trade-offs**: The catch is expecting extracted functions to retain context—only arrow functions inside bound methods preserve it.

Example:

```js
const obj = {
  a: 1,
  b() { return this.a; },
  c: () => { return this.a; },
  d: function() {
    const self = this;
    return {
      e: () => this.a,
      f: function() { return self.a; }
    };
  }
};

console.log(obj.b());
console.log(obj.c());
console.log(obj.d().e());
console.log(obj.d().f());

```

Output:

```

1
undefined
1
1

```

---

## Q188. 💡 Global symbol registry via `Symbol.for`

**Why:** `Symbol('a')` creates a new symbol every time, so `obj[Symbol('a')]` looks up a key that was never set. `Symbol.for('shared')` looks up the global symbol registry and returns the *same* symbol for the same key, so `sym1` and `sym2` are one key and the second assignment overwrites the first.

- **Trade-offs**: The catch is expecting descriptions to guarantee equality—they don’t for bare `Symbol`, only for `Symbol.for`.

Example:

```js
const obj = {
  [Symbol('a')]: 1,
  [Symbol('b')]: 2,
  c: 3
};

const sym1 = Symbol.for('shared');
const sym2 = Symbol.for('shared');

obj[sym1] = 'shared1';
obj[sym2] = 'shared2';

console.log(obj[Symbol('a')]);
console.log(obj[sym1]);
console.log(obj[sym2]);
console.log(Symbol('a') === Symbol('a'));
console.log(Symbol.for('shared') === Symbol.for('shared'));

```

Output:

```

undefined
shared2
shared2
false
true

```

---

## Q189. 💡 Method chaining depends on returning `this`

**Why:** Each method returns `this`, so the next call in the chain is made on the same object: `1` → `increment` → `2` → `add(5)` → `7`. If any method returned `undefined`, the next call would throw a `TypeError`.

- **Trade-offs**: The catch is forgetting to return `this`, breaking the chain.

Example:

```js
const obj = {
  value: 1,
  increment() {
    this.value++;
    return this;
  },
  add(n) {
    this.value += n;
    return this;
  },
  getValue() {
    return this.value;
  }
};

console.log(obj.increment().add(5).getValue());

```

Output:

```

7

```

---

## Q190. 💡 Infinite Fibonacci generator producing successive values

**Why:** The generator yields `curr`, then advances the pair with a destructuring swap. It only computes the next value when `next()` is called (lazy evaluation), so the infinite `while (true)` loop is safe.

- **Trade-offs**: The catch is expecting finite sequences—generators can be infinite, so callers must decide when to stop.

Example:

```js
function* fibonacci() {
  let [prev, curr] = [0, 1];
  while (true) {
    yield curr;
    [prev, curr] = [curr, prev + curr];
  }
}

const gen = fibonacci();
console.log(gen.next().value);
console.log(gen.next().value);
console.log(gen.next().value);
console.log(gen.next().value);

```

Output:

```

1
1
2
3

```

---

## Q191. 🔒 Capturing `this` via closure vs relying on dynamic binding

**Why:** The returned function is called as a plain function (`fn()`), so its own `this` is not `obj` - it's `globalThis` in sloppy mode (or `undefined` in strict mode, where `this.a` would throw). But `self` is a normal variable captured by closure, so `self.a` is still `1`.

- **Trade-offs**: The catch is expecting inner regular functions to inherit `this`—they don’t; capture or bind explicitly.

Example:

```js
const obj = {
  a: 1,
  b: function() {
    const self = this;
    return function() {
      console.log(self.a);
      console.log(this.a);
    };
  }
};

const fn = obj.b();
fn();

```

Output:

```

1
undefined

```

---

## Q192. 🔧 Arrow functions capturing `this` from creation context

**Why:** An arrow function takes `this` from the scope where it was *created*. `obj.b()` runs `b` with `this = obj`, so that arrow always sees `obj.a`. `extracted()` runs `b` with no receiver, so the arrow created in that call captures `globalThis` (sloppy) and logs `undefined`.

- **Trade-offs**: The catch is expecting arrow functions to rebind when called—they never rebind.

Example:

```js
const obj = {
  a: 1,
  b: function() {
    return () => { console.log(this.a); };
  }
};

const fn = obj.b();
fn();

const extracted = obj.b;
const fn2 = extracted();
fn2();

```

Output:

```

1
undefined

```

---

## Q193. ⚡ Promise chain errors recovered by `.catch`

**Why:** Each `.then` passes its return value to the next. The `throw` rejects the chain, so the next `.then` success handler is skipped and control jumps to `.catch`. Returning `10` from `.catch` fulfills the chain again, so the final `.then` receives `10`.

- **Trade-offs**: The catch is assuming the chain stops—`.catch` can hand control back down the chain.

Example:

```js
Promise.resolve(1)
  .then(val => {
    console.log(val);
    return val + 1;
  })
  .then(val => {
    console.log(val);
    throw new Error('Error');
  })
  .then(val => {
    console.log('Not reached');
  })
  .catch(err => {
    console.log(err.message);
    return 10;
  })
  .then(val => {
    console.log(val);
  });

```

Output:

```

1
2
Error
10

```

---

## Q194. 💡 Map keys compared by reference

**Why:** Map keys are compared by identity (SameValueZero), not by structure. `obj1` and `obj2` look alike but are different objects, so they're separate keys. Setting `obj1` again updates its existing entry, so `size` stays `2`.

- **Trade-offs**: The catch is expecting structural equality—Maps use reference identity.

Example:

```js
const map = new Map();
const obj1 = { a: 1 };
const obj2 = { a: 1 };

map.set(obj1, 'value1');
map.set(obj2, 'value2');

console.log(map.get(obj1));
console.log(map.get(obj2));
console.log(map.size);

map.set(obj1, 'value3');
console.log(map.get(obj1));
console.log(map.size);

```

Output:

```

value1
value2
2
value3
2

```

---

## Q195. 💡 Set uniqueness and delete behavior

**Why:** Adding `3` again is a no-op because it's already present; `4` is new; `delete(2)` removes `2`. That leaves `1, 3, 4` in insertion order.

- **Trade-offs**: The catch is expecting duplicates—Sets enforce uniqueness automatically.

Example:

```js
const set = new Set([1, 2, 3]);
set.add(3);
set.add(4);
set.delete(2);

console.log(set.size);
console.log([...set]);
console.log(set.has(2));
console.log(set.has(4));

```

Output:

```

3
[ 1, 3, 4 ]
false
true

```

---

## Q196. 📦 Custom iterable object consumed via spread/Array.from

**Why:** Spread, `Array.from`, and `for...of` all call `obj[Symbol.iterator]()` and pull values until `done: true`. A generator method is the simplest way to implement that iterator protocol.

- **Trade-offs**: The catch is expecting iteration without defining `[Symbol.iterator]`—it’s required for custom iterables.

Example:

```js
const obj = {
  *[Symbol.iterator]() {
    yield 1;
    yield 2;
    yield 3;
  }
};

console.log([...obj]);
console.log(Array.from(obj));

for (const val of obj) {
  console.log(val);
}

```

Output:

```

[ 1, 2, 3 ]
[ 1, 2, 3 ]
1
2
3

```

---

## Q197. ⚡ Async generator with delay per iteration

**Why:** The generator awaits a 100 ms timer before each `yield`, and `for await...of` waits for each value before asking for the next, so values arrive one at a time about 100 ms apart and `Done` prints only after the generator finishes.

- **Trade-offs**: The catch is expecting synchronous output—the loop awaits each value.

Example:

```js
async function* asyncGen() {
  for (let i = 0; i < 3; i++) {
    await new Promise(resolve => setTimeout(resolve, 100));
    yield i;
  }
}

(async () => {
  for await (const val of asyncGen()) {
    console.log(val);
  }
  console.log('Done');
})();

```

Output:

```

0
1
2
Done

```

---

## Q198. 🔧 Hoisting order between functions and variables

**Why:** During the creation phase, the function declaration `foo` is hoisted with its body, while `var foo` is hoisted but its assignment is not. So the first call runs the declaration. When execution reaches the `var foo = function...` line, it reassigns `foo`, and the second call uses the new function.

- **Trade-offs**: The catch is expecting the `var` assignment to override the declaration before the initial call—it doesn’t run until runtime.

Example:

```js
console.log(foo());

function foo() {
  return 'function';
}

var foo = function() {
  return 'var';
};

console.log(foo());

```

Output:

```

function
var

```

---

## Q199. 💡 Temporal Dead Zone (TDZ) with `let`

**Why:** `let`, `const`, and `class` bindings are hoisted but left uninitialized until their declaration line runs. The period in between is the Temporal Dead Zone, and any access throws a `ReferenceError`.

- **Trade-offs**: The catch is expecting `undefined` like `var`; TDZ gives a ReferenceError instead.

Example:

```js
console.log(value);
let value = 10;

```

Output:

```

ReferenceError: Cannot access 'value' before initialization

```

---

## Q200. 💡 Default parameters referencing later parameters

**Why:** Parameters are initialized left to right, and each has its own TDZ. When `x`'s default `y` is evaluated, `y` hasn't been initialized yet, so it throws a `ReferenceError`. Swapping the order (`y = 2, x = y`) works.

- **Trade-offs**: The catch is assuming all parameters are in scope for defaults—only those to the left are available.

Example:

```js
function test(x = y, y = 2) {
  return x + y;
}

console.log(test());

```

Output:

```

ReferenceError: Cannot access 'y' before initialization

```

---

## Q201. 🌐 Spread arguments vs rest parameters

**Why:** At the call site, `...arr` spreads the array into separate arguments, so the call is `mix(1, 2, 3, 4)`. In the function signature, `...rest` collects every argument after `a` into a real array.

- **Trade-offs**: The catch is expecting rest to represent only explicit arrays—it captures every leftover argument.

Example:

```js
function mix(a, ...rest) {
  console.log(a, rest);
}

const arr = [1, 2, 3];
mix(...arr, 4);

```

Output:

```

1 [ 2, 3, 4 ]

```

---

## Q202. 📝 `typeof null` and `instanceof`

**Why:** `typeof null === 'object'` is a bug from the very first JavaScript implementation that can't be fixed without breaking the web. `instanceof` walks the prototype chain, and `null` has no chain at all, so it's `false`. Check for null with `x === null`.

- **Trade-offs**: The catch is relying on `typeof` for null checks—prefer direct equality.

Example:

```js
console.log(typeof null);
console.log(null instanceof Object);

```

Output:

```

object
false

```

---

## Q203. 🔍 `NaN` equality quirks and `Object.is`

**Why:** IEEE 754 defines `NaN` as unequal to everything, including itself, so `===` returns `false`. `Object.is` uses SameValue comparison, which treats `NaN` as equal to `NaN` (and also distinguishes `+0` from `-0`).

- **Trade-offs**: The catch is expecting regular equality to work; use `Number.isNaN` or `Object.is`.

Example:

```js
const value = NaN;
console.log(value === NaN);
console.log(Object.is(value, NaN));

```

Output:

```

false
true

```

---

## Q204. 💡 Implicit globals created via sloppy-mode assignment

**Why:** In sloppy mode, assigning to an undeclared name creates a property on the global object, so `implicit` leaks out of the function. In strict mode (and in every ES module and class body) the same line throws `ReferenceError: implicit is not defined`.

- **Trade-offs**: The catch is expecting a ReferenceError—without `'use strict'`, the assignment succeeds.

Example:

```js
function test() {
  implicit = 10;
}

test();
console.log(implicit);

```

Output:

```

10

```

---

## Q205. 📝 `delete` behavior on variables vs properties

**Why:** `delete` removes object properties only. A `var` declaration creates a non-configurable binding, so `delete count` returns `false` and does nothing (in strict mode, `delete` on a plain identifier is a `SyntaxError`). `obj.count` is a normal configurable property, so it's removed.

- **Trade-offs**: The catch is expecting `delete count` to succeed—only object members (or implicit globals) are deletable.

Example:

```js
var count = 5;
const obj = { count: 10 };

delete count;
delete obj.count;

console.log(count);
console.log(obj.count);

```

Output:

```

5
undefined

```

---

## Q206. ⚡ `Promise.all` short-circuits on rejection

**Why:** `Promise.all` rejects as soon as any input rejects, with that rejection's reason. The already-fulfilled values are discarded, so only `.catch` runs and prints `boom`.

- **Trade-offs**: The catch is expecting partial success—use `Promise.allSettled` when you need every result.

Example:

```js
Promise.all([
  Promise.resolve(1),
  Promise.reject('boom'),
  Promise.resolve(3)
]).then(console.log)
  .catch(console.log);

```

Output:

```

boom

```

---

## Q207. ⚡ `forEach` ignores async/await

**Why:** `forEach` calls each async callback and ignores the promise it returns - it never waits. So the synchronous `Done scheduling` prints first, and each id prints when its own timer (100, 200, 300 ms) finishes.

- **Trade-offs**: The catch is expecting sequential awaits—use `for...of` or `Promise.all` to control async iteration.

Example:

```js
const ids = [1, 2, 3];

ids.forEach(async id => {
  await new Promise(r => setTimeout(r, 100 * id));
  console.log(id);
});

console.log('Done scheduling');

```

Output:

```

Done scheduling
1
2
3

```

---

