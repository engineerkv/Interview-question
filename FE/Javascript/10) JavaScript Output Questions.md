<!-- markdownlint-disable MD040 -->

# 10. JavaScript Output Questions (Q191–250)

---

## Q191. Event loop ordering with timers, promises, and microtasks

Synchronous logs run first, then microtasks (`Promise` callbacks, `queueMicrotask`), then macrotasks (`setTimeout`), matching the event-loop order described in the GFG output list.[\[1\]](https://www.geeksforgeeks.org/javascript/javascript-output-based-interview-questions/)

- **Trade-offs**: The catch is assuming timers beat promises—microtasks always drain before the macrotask queue, so timers run last even with zero delay.

Example:

```js
console.log('Start');
setTimeout(() => console.log('Timeout'), 0);
Promise.resolve().then(() => console.log('Promise'));
queueMicrotask(() => console.log('Microtask'));
console.log('End');
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

## Q192. Async/await vs synchronous code and timers

`await` pauses inside `async1`, so the remainder of `async1` runs as a microtask after the current stack, aligning with common interview traps noted by GFG.[\[1\]](https://www.geeksforgeeks.org/javascript/javascript-output-based-interview-questions/)

- **Trade-offs**: The catch is expecting `async/await` to block like synchronous code—other synchronous logs finish before awaited work resumes.

Example:

```js
async function async1() {
  console.log('async1 start');
  await async2();
  console.log('async1 end');
}

async function async2() {
  console.log('async2');
}

console.log('script start');
setTimeout(() => console.log('setTimeout'), 0);
async1();
new Promise(resolve => {
  console.log('promise1');
  resolve();
}).then(() => console.log('promise2'));
console.log('script end');
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

## Q193. Property descriptors, getters/setters, and non-configurable fields

`configurable: false` blocks `delete`, so the accessor remains even after calling `delete obj.prop`, reflecting the behavior highlighted in multiple tricky question lists.[\[1\]](https://www.geeksforgeeks.org/javascript/javascript-output-based-interview-questions/)

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

## Q194. Prototype methods, deletion, and fallback behavior

Deleting an instance method only removes own properties; prototype methods keep working until removed from the prototype, a frequent “gotcha” noted by interview write-ups.[\[1\]](https://www.geeksforgeeks.org/javascript/javascript-output-based-interview-questions/)

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

## Q195. Prototype inheritance, hasOwnProperty, and deletion side effects

`child.a` is inherited from `parent`; deleting it on `child` does nothing until you delete the parent property, matching sample puzzles from GFG’s list.[\[1\]](https://www.geeksforgeeks.org/javascript/javascript-output-based-interview-questions/)

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

## Q196. Object.freeze on objects and arrays

Frozen objects reject reassignment/additions (silently in non-strict mode); arrays also reject `push`, reproducing a common trap covered on GFG.[\[1\]](https://www.geeksforgeeks.org/javascript/javascript-output-based-interview-questions/)

- **Trade-offs**: The catch is expecting freeze to throw—without strict mode it fails silently, so values appear unchanged even after attempted writes.

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
[1, 2, 3]
```

---

## Q197. Nested closures and shared lexical state

Closures capture variables by reference, so each invocation manipulates the same `count`, demonstrating classic closure behavior documented in Medium’s question set.[\[2\]](https://medium.com/@sohammehta56/javascript-interesting-output-based-interview-questions-38682c0b64fe)

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
4
```

---

## Q198. `var` vs `let` in loops with asynchronous callbacks

`var` is function-scoped, so each timeout logs `3`, whereas `let` creates a new binding per iteration, yielding `0,1,2`; widely cited as a classic interview trap.[\[1\]](https://www.geeksforgeeks.org/javascript/javascript-output-based-interview-questions/)

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
0
1
2
```

---

## Q199. `this` binding differences between regular and arrow methods

Regular methods bind `this` dynamically while arrow functions inherit lexical `this`; extracting a method loses context, aligning with Medium’s tricky scenarios.[\[2\]](https://medium.com/@sohammehta56/javascript-interesting-output-based-interview-questions-38682c0b64fe)

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

## Q200. Class inheritance, `super()`, and method extraction

`Child` overrides `name`, but extracting `getName` loses the `this` binding, returning `undefined`, echoing patterns from Medium question banks.[\[3\]](https://medium.com/@iamyashkhandelwal/5-output-based-interview-questions-in-javascript-b64a707f34d2)

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
undefined
```

---

## Q201. Regular methods, arrow methods, and nested arrows referencing `this`

Only standard methods bound via the object can access `this.a`; arrow functions inside the object or nested ones inherit `this` from the file scope (often `undefined`).[\[1\]](https://www.geeksforgeeks.org/javascript/javascript-output-based-interview-questions/)

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

## Q202. Async function returning a promise and chaining `.then()`

Returning `Promise.resolve('3')` after `await` means `test().then(console.log)` logs `'3'` after current microtasks, similar to examples cataloged on GFG.[\[1\]](https://www.geeksforgeeks.org/javascript/javascript-output-based-interview-questions/)

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

## Q203. Promise unwrapping and concurrent microtask ordering

Returning a promise from `.then()` queues another microtask; separate `Promise.resolve().then` calls interleave, mirroring tricky sequences referenced in GFG articles.[\[1\]](https://www.geeksforgeeks.org/javascript/javascript-output-based-interview-questions/)

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
2
Error
10
```

---

## Q204. Async `try/catch` with awaited rejections

Awaiting a rejected promise throws inside `try/catch`, so returning `'Caught'` yields a resolved promise—exactly the pattern highlighted in Medium write-ups.[\[3\]](https://medium.com/@iamyashkhandelwal/5-output-based-interview-questions-in-javascript-b64a707f34d2)

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

## Q205. Returning a rejected promise without awaiting inside `try/catch`

Without `await`, the rejection bypasses `try/catch`, so the caller’s `.catch()` handles it—mirroring Medium’s emphasis on the difference between awaited and unawaited promises.[\[3\]](https://medium.com/@iamyashkhandelwal/5-output-based-interview-questions-in-javascript-b64a707f34d2)

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

## Q206. WeakMap keys and garbage collection

WeakMaps use weak references; `delete obj` only removes the local variable, and the WeakMap entry becomes unreachable only after garbage collection, per standard JS behaviors discussed online.[\[1\]](https://www.geeksforgeeks.org/javascript/javascript-output-based-interview-questions/)

- **Trade-offs**: The catch is expecting immediate `undefined`—without GC, `map.get(obj)` (with the original reference) still works; after `delete obj`, you can’t reference it anymore.

Example:

```js
const map = new WeakMap();
const obj = {};

map.set(obj, 'value');
console.log(map.get(obj));

delete obj;
console.log(map.get(obj));
```

Output:

```
value
undefined
```

---

## Q207. Symbol uniqueness and non-enumerability

Even identical descriptions produce distinct symbols, and symbol keys aren’t part of `Object.keys`, reflecting standard questions from GFG’s resource.[\[1\]](https://www.geeksforgeeks.org/javascript/javascript-output-based-interview-questions/)

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

## Q208. Proxies intercepting get/set for transformed values

Proxies can double reads/writes, exactly like similar interview puzzles; all interactions go through handlers, not the original object.[\[1\]](https://www.geeksforgeeks.org/javascript/javascript-output-based-interview-questions/)

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
10
0
1
2
1
10
```

---

## Q209. Generator `next()` sequencing and completion records

Generators yield values until `return`; subsequent `next()` calls show `{value: undefined, done: true}`, a staple of output questions.[\[1\]](https://www.geeksforgeeks.org/javascript/javascript-output-based-interview-questions/)

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

## Q210. Async generators consumed via `for await...of`

Each `yield Promise.resolve(x)` is awaited automatically, producing sequential logs, echoing examples from Medium.[\[2\]](https://medium.com/@sohammehta56/javascript-interesting-output-based-interview-questions-38682c0b64fe)

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

## Q211. Sparse array behavior and skipped slots in `map`

Setting `arr[10]` creates empty slots; `map` skips them, so the mapped array retains holes, a common subtlety on GFG.[\[1\]](https://www.geeksforgeeks.org/javascript/javascript-output-based-interview-questions/)

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

## Q212. Manipulating `array.length` to expand or truncate data

Increasing length adds holes; shrinking truncates data—reflecting interview questions that highlight how mutable `length` is.[\[1\]](https://www.geeksforgeeks.org/javascript/javascript-output-based-interview-questions/)

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
[ 1, 2 ]
[ 1, 2, 3, 4, 5, <5 empty items> ]
[ 1, 2 ]
[ 1, 2, 3 ]
```

---

## Q213. Set de-duplication and Map key overwrites

Sets ignore duplicates and maintain insertion order; Maps keep only the latest value for a duplicate key, per GFG’s question guide.[\[1\]](https://www.geeksforgeeks.org/javascript/javascript-output-based-interview-questions/)

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

## Q214. String vs symbol key enumeration

`Object.keys` ignores symbols, `Object.getOwnPropertySymbols` returns only symbols, while `Reflect.ownKeys` returns both—as frequently tested.[\[1\]](https://www.geeksforgeeks.org/javascript/javascript-output-based-interview-questions/)

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

## Q215. Getter/setter computed values affecting backing state

The getter doubles `a`, while the setter halves assignments—matching JS trick questions cataloged online.[\[2\]](https://medium.com/@sohammehta56/javascript-interesting-output-based-interview-questions-38682c0b64fe)

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

## Q216. Prototype properties vs own properties with `hasOwnProperty`

`foo.b` comes from the prototype until overwritten, so `hasOwnProperty` distinguishes them, as shown in standard interview snippets.[\[1\]](https://www.geeksforgeeks.org/javascript/javascript-output-based-interview-questions/)

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

## Q217. Objects created with `Object.create(null)`

Prototype-less objects lack default methods, so accessing `.toString` or `.hasOwnProperty` yields `undefined`, per widely cited examples.[\[1\]](https://www.geeksforgeeks.org/javascript/javascript-output-based-interview-questions/)

- **Trade-offs**: The catch is expecting built-in methods; these objects are dictionary-like and require manual handling.

Example:

```js
const obj = Object.create(null);
obj.a = 1;

console.log(obj.a);
console.log(obj.toString);
console.log(obj.hasOwnProperty('a'));
```

Output:

```
1
undefined
undefined
```

---

## Q218. `Object.seal` allowing updates but blocking additions & deletions

`seal` keeps existing keys mutable but prevents additions/deletions—mirroring typical output puzzles.[\[1\]](https://www.geeksforgeeks.org/javascript/javascript-output-based-interview-questions/)

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

## Q219. `Object.preventExtensions` blocking new props only

Extensions are blocked but existing values change—less restrictive than `seal` or `freeze`, as shown in many quizzes.[\[1\]](https://www.geeksforgeeks.org/javascript/javascript-output-based-interview-questions/)

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

## Q220. Tagged template literal parameter breakdown

Tagged templates pass literal segments array plus interpolated values, enabling custom string construction as demonstrated in GFG’s question bank.[\[1\]](https://www.geeksforgeeks.org/javascript/javascript-output-based-interview-questions/)

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
Hello John, you are 30!
```

---

## Q221. Nullish coalescing vs optional chaining default handling

`??` only falls back on `null`/`undefined`; optional chaining returns `undefined` for missing nested props without throwing, consistent with modern JS quizzes.[\[1\]](https://www.geeksforgeeks.org/javascript/javascript-output-based-interview-questions/)

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
""
undefined
undefined
undefined
```

---

## Q222. Custom primitive conversion via `Symbol.toPrimitive`

The method inspects hints (`number`, `string`, `default`) to return different values, as showcased in tricky problem sets.[\[1\]](https://www.geeksforgeeks.org/javascript/javascript-output-based-interview-questions/)

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
hello
true
84
```

---

## Q223. BigInt arithmetic and equality comparisons

BigInt operations stay BigInt; `===` respects type, `==` coerces, matching modern JS interview content.[\[1\]](https://www.geeksforgeeks.org/javascript/javascript-output-based-interview-questions/)

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

## Q224. Bound functions ignore subsequent `call`/`apply`

Once bound, `greet` always uses the bound object, regardless of later `.call`/`.apply`, a frequent trick question.[\[1\]](https://www.geeksforgeeks.org/javascript/javascript-output-based-interview-questions/)

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

## Q225. Destructuring defaults triggered only by `undefined`

Default values skip when properties are `null`, `0`, `false`, etc., aligning with examples in frequently cited articles.[\[2\]](https://medium.com/@sohammehta56/javascript-interesting-output-based-interview-questions-38682c0b64fe)

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

## Q226. Variable shadowing across nested scopes

Inner `let x` declarations shadow outer ones but don’t modify them; output shows per-scope values, per classic puzzles.[\[1\]](https://www.geeksforgeeks.org/javascript/javascript-output-based-interview-questions/)

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

## Q227. Strict-mode `this` vs method invocation contexts

Standalone calls produce `undefined`; object method calls bind `this` to the object, supporting canonical interview examples.[\[1\]](https://www.geeksforgeeks.org/javascript/javascript-output-based-interview-questions/)

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
{ a: 1, b: 2, e: undefined }
undefined
undefined
```

---

## Q228. Proxy traps customizing property access and enumeration

Handlers intercept `get`, `has`, `ownKeys`; here `get` doubles values and unknown props yield `NaN`, matching tricky patterns from GFG.[\[1\]](https://www.geeksforgeeks.org/javascript/javascript-output-based-interview-questions/)

- **Trade-offs**: The catch is expecting proxies to fall back on defaults—they can rewrite behavior entirely.

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

## Q229. Generator `try/catch` catching internal errors

Throwing inside a generator can be caught and the generator can continue yielding, as seen in interview question archives.[\[1\]](https://www.geeksforgeeks.org/javascript/javascript-output-based-interview-questions/)

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
{ value: 'Error', done: false }
{ value: 5, done: false }
{ value: undefined, done: true }
```

---

## Q230. Mixed regular and arrow functions inside objects

Regular methods use dynamic `this`, arrows capture lexical `this`, and nested arrows inside methods inherit object context—mirroring common output puzzles.[\[2\]](https://medium.com/@sohammehta56/javascript-interesting-output-based-interview-questions-38682c0b64fe)

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
undefined
```

---

## Q231. Global symbol registry via `Symbol.for`

Symbols from `Symbol()` are unique per call; `Symbol.for` reuses registry entries, so assignments with the same key hit the same symbol, as covered in quizzes.[\[1\]](https://www.geeksforgeeks.org/javascript/javascript-output-based-interview-questions/)

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

## Q232. Method chaining depends on returning `this`

Each method must return the instance to allow chaining; otherwise, later calls fail, per classic chain examples.[\[2\]](https://medium.com/@sohammehta56/javascript-interesting-output-based-interview-questions-38682c0b64fe)

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

## Q233. Infinite Fibonacci generator producing successive values

The generator yields successive Fibonacci numbers lazily, per well-known interview exercises.[\[1\]](https://www.geeksforgeeks.org/javascript/javascript-output-based-interview-questions/)

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

## Q234. Capturing `this` via closure vs relying on dynamic binding

`self` (or arrow function) captures the object, while standalone functions fall back to `undefined`, echoing typical closure vs `this` puzzles.[\[1\]](https://www.geeksforgeeks.org/javascript/javascript-output-based-interview-questions/)

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

## Q235. Arrow functions capturing `this` from creation context

`obj.b()` returns an arrow that remembers `obj`; calling the function returned by an unbound `extracted()` has `this` as `undefined`, reflecting Medium’s outputs.[\[3\]](https://medium.com/@iamyashkhandelwal/5-output-based-interview-questions-in-javascript-b64a707f34d2)

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

## Q236. Promise chain errors recovered by `.catch`

Throwing inside `.then` hits `.catch`, which can return a value to continue the chain, as stressed in popular interview examples.[\[2\]](https://medium.com/@sohammehta56/javascript-interesting-output-based-interview-questions-38682c0b64fe)

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

## Q237. Map keys compared by reference

Different objects with identical contents are distinct keys; overwriting the same key replaces its value without growing the size.[\[1\]](https://www.geeksforgeeks.org/javascript/javascript-output-based-interview-questions/)

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

## Q238. Set uniqueness and delete behavior

Sets ignore duplicate adds; `delete` removes values if present.[\[1\]](https://www.geeksforgeeks.org/javascript/javascript-output-based-interview-questions/)

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

## Q239. Custom iterable object consumed via spread/Array.from

Defining `[Symbol.iterator]` lets objects work with `...` and `Array.from`, per frequent interview fodder.[\[1\]](https://www.geeksforgeeks.org/javascript/javascript-output-based-interview-questions/)

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

## Q240. Async generator with delay per iteration

Each iteration waits before yielding; completion logs `'Done'`, aligning with asynchronous iteration patterns shown in references.[\[1\]](https://www.geeksforgeeks.org/javascript/javascript-output-based-interview-questions/)

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

---

## Q241. Hoisting order between functions and variables

Function declarations hoist before `var`, so the first call hits the declared function before the `var` assignment executes.[\[1\]](https://www.geeksforgeeks.org/javascript/javascript-output-based-interview-questions/)

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

## Q242. Temporal Dead Zone (TDZ) with `let`

`let` bindings exist in TDZ until their declaration executes; accessing them early throws.[\[2\]](https://medium.com/@sohammehta56/javascript-interesting-output-based-interview-questions-38682c0b64fe)

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

## Q243. Default parameters referencing later parameters

Default parameters evaluate left-to-right, so using a later parameter inside an earlier default crashes.[\[2\]](https://medium.com/@sohammehta56/javascript-interesting-output-based-interview-questions-38682c0b64fe)

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

## Q244. Spread arguments vs rest parameters

Spread expands arrays into arguments, while rest collects remaining arguments into an array.[\[1\]](https://www.geeksforgeeks.org/javascript/javascript-output-based-interview-questions/)

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

## Q245. `typeof null` and `instanceof`

Legacy behavior makes `typeof null === 'object'`, yet `null instanceof Object` is false.[\[1\]](https://www.geeksforgeeks.org/javascript/javascript-output-based-interview-questions/)

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

## Q246. `NaN` equality quirks and `Object.is`

`NaN` isn’t equal to itself via `===`, but `Object.is` recognizes it, a common interview trick.[\[1\]](https://www.geeksforgeeks.org/javascript/javascript-output-based-interview-questions/)

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

## Q247. Implicit globals created via sloppy-mode assignment

Assigning to an undeclared identifier creates a global (in non-strict mode), which can surprise developers.[\[1\]](https://www.geeksforgeeks.org/javascript/javascript-output-based-interview-questions/)

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

## Q248. `delete` behavior on variables vs properties

`delete` removes object properties but not declared variables; `var` bindings remain.[\[1\]](https://www.geeksforgeeks.org/javascript/javascript-output-based-interview-questions/)

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

## Q249. `Promise.all` short-circuits on rejection

`Promise.all` rejects as soon as any promise rejects, ignoring remaining resolutions.[\[1\]](https://www.geeksforgeeks.org/javascript/javascript-output-based-interview-questions/)

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

## Q250. `forEach` ignores async/await

`Array.prototype.forEach` doesn’t await async callbacks, so logs happen after the synchronous message.[\[2\]](https://medium.com/@sohammehta56/javascript-interesting-output-based-interview-questions-38682c0b64fe)

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
