# 🎯 11. JavaScript Output Questions (Q131–180)

Senior to expert-level JavaScript output questions testing deep understanding of closures, prototypes, event loop, async behavior, and advanced language features.

---

## Q131. What will be the output of the following code?

```js
console.log('Start');
setTimeout(() => console.log('Timeout'), 0);
Promise.resolve().then(() => console.log('Promise'));
queueMicrotask(() => console.log('Microtask'));
console.log('End');
```

**Output:**
```
Start
End
Promise
Microtask
Timeout
```

**Explanation:** Synchronous code runs first (`Start`, `End`). Microtasks (Promises and `queueMicrotask`) run before macrotasks (setTimeout). Microtasks execute in order they were queued (`Promise` before `Microtask`). `setTimeout` runs last.

---

## Q132. What will be the output of the following code?

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

**Output:**
```
script start
async1 start
async2
promise1
script end
promise2
async1 end
setTimeout
```

**Explanation:** Synchronous code runs first. `await` pauses execution and returns control. The promise after `await` is queued as a microtask. All microtasks run before macrotasks.

---

## Q133. What will be the output of the following code?

```js
const obj = {};
Object.defineProperty(obj, 'prop', {
  get() {
    return this._value;
  },
  set(value) {
    this._value = value * 2;
  },
  enumerable: true,
  configurable: false
});

obj.prop = 10;
console.log(obj.prop);
delete obj.prop;
console.log(obj.prop);
```

**Output:**
```
20
20
```

**Explanation:** The setter multiplies by 2. `delete` fails silently because `configurable: false`. The property remains, so `obj.prop` still returns `20`.

---

## Q134. What will be the output of the following code?

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

**Output:**
```
Hello, John
Hello, John
TypeError: person.greet is not a function
```

**Explanation:** Deleting `person.greet` doesn't remove it from the prototype. The method still exists on the prototype chain. Deleting `Person.prototype.greet` removes it from the prototype, so the third call throws an error.

---

## Q135. What will be the output of the following code?

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

**Output:**
```
1
2
false
true
1
undefined
```

**Explanation:** `child.a` comes from the prototype. `hasOwnProperty('a')` returns `false` because it's not on `child`. Deleting `child.a` fails silently (it's on the prototype). Deleting `child.b` succeeds because it's an own property.

---

## Q136. What will be the output of the following code?

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

**Output:**
```
1
undefined
[1, 2, 3]
```

**Explanation:** `Object.freeze()` prevents adding, modifying, or deleting properties. Assignments fail silently. `arr.push()` throws in strict mode (TypeError), but in non-strict mode it fails silently.

---

## Q137. What will be the output of the following code?

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

**Output:**
```
1
2
3
```

**Explanation:** All three functions share the same `count` variable from the closure. Each call increments the shared `count`. The closure persists across all returned functions.

---

## Q138. What will be the output of the following code?

```js
for (var i = 0; i < 3; i++) {
  setTimeout(() => console.log(i), 0);
}

for (let j = 0; j < 3; j++) {
  setTimeout(() => console.log(j), 0);
}
```

**Output:**
```
3
3
3
0
1
2
```

**Explanation:** `var` is function-scoped, so there's one `i` shared across iterations. By the time callbacks run, `i` is `3`. `let` is block-scoped, so each iteration creates a new `j` captured by the closure.

---

## Q139. What will be the output of the following code?

```js
const obj = {
  value: 10,
  getValue: function() {
    return this.value;
  },
  getValueArrow: () => {
    return this.value;
  }
};

console.log(obj.getValue());
console.log(obj.getValueArrow());

const extracted = obj.getValue;
console.log(extracted());
```

**Output:**
```
10
undefined
undefined
```

**Explanation:** Regular functions have dynamic `this` (bound to `obj` when called as a method). Arrow functions have lexical `this` (from outer scope, likely `undefined` in strict mode). Extracting a method loses its `this` binding.

---

## Q140. What will be the output of the following code?

```js
class Parent {
  constructor() {
    this.name = 'Parent';
  }
  
  getName() {
    return this.name;
  }
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

**Output:**
```
Child
TypeError: Cannot read property 'name' of undefined
```

**Explanation:** `super()` calls the parent constructor. `child.getName()` works because `this` is `child`. Extracting the method loses `this` binding, causing `this` to be `undefined` in strict mode.

---

## Q141. What will be the output of the following code?

```js
const obj = {
  a: 1,
  b: function() {
    console.log(this.a);
  },
  c: () => {
    console.log(this.a);
  },
  d() {
    const nested = () => {
      console.log(this.a);
    };
    nested();
  }
};

obj.b();
obj.c();
obj.d();

const extracted = obj.b;
extracted();
```

**Output:**
```
1
undefined
1
undefined
```

**Explanation:** Regular methods have `this` bound to the object. Arrow functions have lexical `this`. Nested arrow functions inherit `this` from the enclosing method. Extracted methods lose `this` binding.

---

## Q142. What will be the output of the following code?

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

**Output:**
```
1
4
2
3
```

**Explanation:** `await` pauses execution and queues the rest as a microtask. Synchronous code continues (`4`). After the promise resolves, execution continues (`2`). The returned promise resolves with `'3'`.

---

## Q143. What will be the output of the following code?

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

**Output:**
```
1
4
2
3
```

**Explanation:** Returning a promise from a `.then()` unwraps it, adding another microtask. Both promise chains run, but microtasks interleave. The unwrapping adds a delay, so `4` appears before `2`.

---

## Q144. What will be the output of the following code?

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

**Output:**
```
Caught
```

**Explanation:** `await` on a rejected promise throws an error. The `catch` block catches it and returns `'Caught'`. The function returns a resolved promise with `'Caught'`, so `.then()` executes.

---

## Q145. What will be the output of the following code?

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

**Output:**
```
Error
```

**Explanation:** Without `await`, the rejected promise is returned directly. The `catch` block doesn't catch it because the error isn't thrown. The returned promise is rejected, so `.catch()` executes.

---

## Q146. What will be the output of the following code?

```js
const map = new WeakMap();
const obj = {};

map.set(obj, 'value');
console.log(map.get(obj));

delete obj;
console.log(map.get(obj));
```

**Output:**
```
value
value
```

**Explanation:** `delete obj` only removes the reference, not the object itself. WeakMap holds weak references. The object becomes eligible for garbage collection when no other references exist, but the WeakMap entry remains until then.

---

## Q147. What will be the output of the following code?

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

**Output:**
```
value1
value2
false
0
```

**Explanation:** Each `Symbol()` call creates a unique symbol, even with the same description. Symbols are not enumerable, so `Object.keys()` doesn't include them. Use `Object.getOwnPropertySymbols()` to get symbols.

---

## Q148. What will be the output of the following code?

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

**Output:**
```
2
10
0
1
10
```

**Explanation:** The proxy intercepts `get` and `set` operations. Getting `a` returns `1 * 2 = 2`. Setting `b = 5` stores `5 * 2 = 10` in the target. Getting `c` (not in target) returns `0`. The target object is modified by the proxy.

---

## Q149. What will be the output of the following code?

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

**Output:**
```
{ value: 1, done: false }
{ value: 2, done: false }
{ value: 3, done: false }
{ value: 4, done: true }
{ value: undefined, done: true }
```

**Explanation:** Each `next()` call resumes the generator. `yield` pauses and returns a value. `return` ends the generator. After `done: true`, subsequent calls return `{ value: undefined, done: true }`.

---

## Q150. What will be the output of the following code?

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

**Output:**
```
1
2
3
```

**Explanation:** `for await...of` automatically awaits each yielded promise. The async generator yields promises, which are unwrapped by `for await...of`.

---

## Q151. What will be the output of the following code?

```js
const arr = [1, 2, 3];
arr[10] = 10;

console.log(arr.length);
console.log(arr[5]);
console.log(arr);

const mapped = arr.map(x => x * 2);
console.log(mapped);
```

**Output:**
```
11
undefined
[1, 2, 3, <7 empty items>, 10]
[2, 4, 6, <7 empty items>, 20]
```

**Explanation:** Setting an index beyond length creates a sparse array. Empty slots are `undefined`. `map()` skips empty slots but preserves the array structure with empty slots.

---

## Q152. What will be the output of the following code?

```js
const arr = [1, 2, 3];
arr.length = 10;
console.log(arr);
console.log(arr.length);

arr.length = 2;
console.log(arr);
console.log(arr.length);
```

**Output:**
```
[1, 2, 3, <7 empty items>]
10
[1, 2]
2
```

**Explanation:** Setting `length` to a larger value extends the array with empty slots. Setting `length` to a smaller value truncates the array, removing elements beyond the new length.

---

## Q153. What will be the output of the following code?

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

**Output:**
```
3
[1, 2, 3]
2
[['a', 3], ['b', 2]]
```

**Explanation:** Sets store unique values; duplicates are ignored. Maps store unique keys; duplicate keys overwrite previous values. The last value for a key is kept.

---

## Q154. What will be the output of the following code?

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

**Output:**
```
['a', 'b']
['a', 'b']
[Symbol(c)]
['a', 'b', Symbol(c)]
```

**Explanation:** `Object.keys()` returns enumerable string keys. `Object.getOwnPropertyNames()` returns all string keys (enumerable or not). `Object.getOwnPropertySymbols()` returns symbol keys. `Reflect.ownKeys()` returns all keys (strings and symbols).

---

## Q155. What will be the output of the following code?

```js
const obj = {
  a: 1,
  get b() {
    return this.a * 2;
  },
  set b(value) {
    this.a = value / 2;
  }
};

console.log(obj.b);
obj.b = 10;
console.log(obj.a);
console.log(obj.b);
```

**Output:**
```
2
5
10
```

**Explanation:** The getter returns `this.a * 2` (1 * 2 = 2). The setter sets `this.a = value / 2` (10 / 2 = 5). The getter then returns `5 * 2 = 10`.

---

## Q156. What will be the output of the following code?

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

**Output:**
```
1
2
true
false
3
```

**Explanation:** `foo.a` is an own property. `foo.b` comes from the prototype. Changing `Foo.prototype.b` affects all instances because they share the prototype.

---

## Q157. What will be the output of the following code?

```js
const obj = Object.create(null);
obj.a = 1;

console.log(obj.a);
console.log(obj.toString);
console.log(obj.hasOwnProperty('a'));
```

**Output:**
```
1
undefined
TypeError: obj.hasOwnProperty is not a function
```

**Explanation:** `Object.create(null)` creates an object without a prototype. It has no inherited methods like `toString()` or `hasOwnProperty()`. Use `Object.prototype.hasOwnProperty.call(obj, 'a')` instead.

---

## Q158. What will be the output of the following code?

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

**Output:**
```
2
undefined
true
```

**Explanation:** `Object.seal()` prevents adding or deleting properties but allows modifying existing ones. `obj.a = 2` succeeds. `obj.b = 3` fails (silently). `delete obj.a` fails (silently).

---

## Q159. What will be the output of the following code?

```js
const obj = { a: 1 };
Object.preventExtensions(obj);
obj.a = 2;
obj.b = 3;

console.log(obj.a);
console.log(obj.b);
console.log(Object.isExtensible(obj));
```

**Output:**
```
2
undefined
false
```

**Explanation:** `Object.preventExtensions()` prevents adding new properties but allows modifying or deleting existing ones. `obj.a = 2` succeeds. `obj.b = 3` fails (silently).

---

## Q160. What will be the output of the following code?

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

**Output:**
```
['Hello ', ', you are ', '!']
['John', 30]
Hello John, you are 30!
```

**Explanation:** Tagged template literals call the function with an array of strings and an array of interpolated values. The strings array contains the text between interpolations. The function can process and return a custom result.

---

## Q161. What will be the output of the following code?

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

**Output:**
```
default
default
0
false

undefined
undefined
undefined
```

**Explanation:** Nullish coalescing (`??`) only uses the default for `null` or `undefined`, not for other falsy values like `0`, `false`, or `''`. Optional chaining (`?.`) safely accesses nested properties, returning `undefined` if any part is `null` or `undefined`.

---

## Q162. What will be the output of the following code?

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

**Output:**
```
42
hello
hello
true
84
```

**Explanation:** `Symbol.toPrimitive` controls how an object is converted to a primitive. The `hint` parameter indicates the preferred type: `'number'` for numeric operations, `'string'` for string operations, `'default'` for equality comparisons. `+obj` uses `'number'`, `String(obj)` uses `'string'`, `obj + ''` uses `'string'`, `==` uses `'default'`.

---

## Q163. What will be the output of the following code?

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

**Output:**
```
30n
bigint
false
true
true
15
```

**Explanation:** BigInt is a primitive for arbitrary-precision integers. Operations with BigInt return BigInt. `typeof` returns `'bigint'`. Strict equality (`===`) compares type and value, so `a === 10` is `false`. Loose equality (`==`) allows type coercion, so `a == 10` is `true`. BigInt can be compared with numbers and converted with `Number()`.

---

## Q164. What will be the output of the following code?

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

**Output:**
```
John
Jane
John
Jane
```

**Explanation:** `bind()` creates a new function with permanently bound `this`. Once bound, the `this` value cannot be changed with `call()` or `apply()`. The bound function always uses the original bound context.

---

## Q165. What will be the output of the following code?

```js
const obj = { a: undefined, b: null, c: 0, d: false };

const { a = 'defaultA', b = 'defaultB', c = 'defaultC', d = 'defaultD', e = 'defaultE' } = obj;

console.log(a, b, c, d, e);
```

**Output:**
```
defaultA null 0 false defaultE
```

**Explanation:** In destructuring, default values only apply when the property is `undefined`. `null`, `0`, and `false` are not `undefined`, so they are used as-is. Missing properties use default values.

---

## Q166. What will be the output of the following code?

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

**Output:**
```
100 2
10 2
1 2
```

**Explanation:** Variable shadowing occurs when inner scopes declare variables with the same name as outer scopes. Each scope has its own `x`. `y` is not shadowed, so all functions access the global `y = 2`.

---

## Q167. What will be the output of the following code?

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

**Output:**
```
undefined
{ test: [Function: test] }
undefined
```

**Explanation:** In strict mode, `this` is `undefined` for regular functions called without context. When called as a method, `this` refers to the object. Inner functions don't inherit `this` from outer functions; they have their own `this` (undefined in strict mode).

---

## Q168. What will be the output of the following code?

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

**Output:**
```
2
true
['a', 'b']
NaN
```

**Explanation:** The Proxy intercepts `get`, returning `target[prop] * 2`. Accessing `proxy.a` returns `1 * 2 = 2`. The `has` trap returns `true` for existing properties. `ownKeys` returns the target's keys. Accessing a non-existent property returns `undefined * 2 = NaN`.

---

## Q169. What will be the output of the following code?

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

**Output:**
```
{ value: 1, done: false }
{ value: 2, done: false }
{ value: 4, done: false }
{ value: 5, done: false }
{ value: undefined, done: true }
```

**Explanation:** The generator yields `1` and `2`. The error is thrown and caught by the `catch` block, which yields `4`. Execution continues and yields `5`. The generator completes after `5`.

---

## Q170. What will be the output of the following code?

```js
const obj = {
  a: 1,
  b() {
    return this.a;
  },
  c: () => {
    return this.a;
  },
  d: function() {
    const self = this;
    return {
      e: () => this.a,
      f: function() {
        return self.a;
      }
    };
  }
};

console.log(obj.b());
console.log(obj.c());
console.log(obj.d().e());
console.log(obj.d().f());
```

**Output:**
```
1
undefined
1
1
```

**Explanation:** Regular methods have `this` bound to the object. Arrow functions have lexical `this` from the outer scope. The arrow function in `d()` captures `this` from `obj.d()`, so it works. The regular function in `d()` uses `self` to capture `this`.

---

## Q171. What will be the output of the following code?

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

**Output:**
```
undefined
shared2
shared2
false
true
```

**Explanation:** `Symbol()` creates unique symbols; `Symbol('a') !== Symbol('a')`. `Symbol.for()` creates/retrieves symbols from a global registry; `Symbol.for('shared') === Symbol.for('shared')`. Accessing with a different `Symbol('a')` returns `undefined` because it's a different symbol. `sym1` and `sym2` reference the same symbol, so `obj[sym1]` and `obj[sym2]` both return `'shared2'` (the last assigned value).

---

## Q172. What will be the output of the following code?

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

**Output:**
```
7
```

**Explanation:** Method chaining works because each method returns `this`. `increment()` makes `value = 2`. `add(5)` makes `value = 7`. `getValue()` returns `7`.

---

## Q173. What will be the output of the following code?

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

**Output:**
```
1
1
2
3
```

**Explanation:** The generator yields Fibonacci numbers. Each `next()` call resumes execution, computes the next number, and yields it. The generator can run indefinitely.

---

## Q174. What will be the output of the following code?

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

**Output:**
```
1
undefined
```

**Explanation:** `self` captures `this` from the outer function (`obj`). The inner function has its own `this` (global/undefined). `self.a` is `1`. `this.a` is `undefined` because `this` is not `obj`.

---

## Q175. What will be the output of the following code?

```js
const obj = {
  a: 1,
  b: function() {
    return () => {
      console.log(this.a);
    };
  }
};

const fn = obj.b();
fn();

const extracted = obj.b;
const fn2 = extracted();
fn2();
```

**Output:**
```
1
undefined
```

**Explanation:** Arrow functions capture `this` from the enclosing scope. When `obj.b()` is called, `this` is `obj`, so the arrow function captures `obj`. When `extracted()` is called, `this` is `undefined` (strict mode), so the arrow function captures `undefined`.

---

## Q176. What will be the output of the following code?

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

**Output:**
```
1
2
Error
10
```

**Explanation:** The first `.then()` logs `1` and returns `2`. The second `.then()` logs `2` and throws. The error is caught by `.catch()`, which logs the message and returns `10`. The final `.then()` receives `10`.

---

## Q177. What will be the output of the following code?

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

**Output:**
```
value1
value2
2
value3
2
```

**Explanation:** Maps use reference equality for keys. `obj1` and `obj2` are different objects, so they create separate entries. Setting the same key again overwrites the value but doesn't change the size.

---

## Q178. What will be the output of the following code?

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

**Output:**
```
3
[1, 3, 4]
false
true
```

**Explanation:** Sets store unique values. Adding `3` again doesn't change the set. `delete(2)` removes `2`. `has(2)` returns `false`, `has(4)` returns `true`.

---

## Q179. What will be the output of the following code?

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

**Output:**
```
[1, 2, 3]
[1, 2, 3]
1
2
3
```

**Explanation:** The `Symbol.iterator` method makes the object iterable. The spread operator and `Array.from()` consume the iterator. `for...of` also iterates over the values.

---

## Q180. What will be the output of the following code?

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

**Output:**
```
0
1
2
Done
```

**Explanation:** The async generator yields values after delays. `for await...of` automatically awaits each yielded promise. The sequence completes, then `'Done'` is logged.

---

**Deep Insights:**
- **Event Loop**: Microtasks (Promises, queueMicrotask) run before macrotasks (setTimeout, setInterval)
- **Closures**: Functions capture variables from outer scope; all closures share the same variable reference
- **Prototype Chain**: Objects inherit from prototypes; `hasOwnProperty()` distinguishes own vs inherited properties
- **this Binding**: Regular functions have dynamic `this`; arrow functions have lexical `this`; extracted methods lose `this` binding
- **Object Methods**: `Object.freeze()`, `Object.seal()`, `Object.preventExtensions()` have different restrictions
- **Symbols & Iterators**: Symbols are unique and non-enumerable; iterators enable custom iteration behavior
- **Async/Await**: `await` pauses execution and queues microtasks; errors in async functions must be caught
- **Generators**: Functions that can pause and resume; useful for lazy evaluation and async iteration
- **WeakMap/WeakSet**: Store weak references; keys must be objects; entries are garbage collected when keys are unreachable
- **Proxy**: Intercept and customize operations on objects; enables metaprogramming and reactivity
- **Interview Tip**: Understand execution order, prototype inheritance, closure behavior, and async patterns deeply
