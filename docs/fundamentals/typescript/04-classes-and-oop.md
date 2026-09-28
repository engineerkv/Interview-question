---
sidebar_label: "Classes, OOP & Modern TS"
---
# 🏛️ 4. Classes & OOP + Modern TypeScript (Q37–49)

> **Reviewed:** 2026-09 · Modernized; legacy topics are labeled.

---

## Q37. 💡 Access modifiers

Access modifiers control visibility of class members, with public being default, private only accessible within class, and protected accessible in subclasses - access modifiers enable proper object-oriented design. Public (default access, accessible from anywhere), Private (only accessible within the same class), Protected (accessible within class and subclasses).

- **Trade-offs**: The catch is type safety prevents external access to sensitive data - encapsulation improves code maintainability. Access modifiers enable proper object-oriented design, but watch out - control access to internal implementation (encapsulation).

Example:

```typescript
class BankAccount {
  public accountNumber: string; // Public: accessible from anywhere
  private balance: number; // Private: only accessible within this class
  protected bankName: string; // Protected: accessible in this class and subclasses

  constructor(accountNumber: string, initialBalance: number) {
    this.accountNumber = accountNumber; // Can access public property
    this.balance = initialBalance; // Can access private property (within class)
    this.bankName = "MyBank"; // Can access protected property (within class)
  }

  // Public method can access private property
  getBalance(): number {
    return this.balance; // Accessing private property is allowed within class
  }
}

// TypeScript `private` vs JavaScript `#private`
class Wallet {
  private pin = 1234; // compile-time only: erased in JS, reachable via (w as any).pin or JSON.stringify
  #secret = 'abc';    // runtime-enforced by the JS engine: truly inaccessible outside the class
}

```

Interview nuance: TypeScript's `private`/`protected` are **compile-time checks only** - the emitted JavaScript has ordinary public properties. Native ES `#private` fields (ES2022) are enforced at runtime. Use `#` when privacy must hold at runtime (libraries, security-sensitive state); TS `private` is still common and gives you `protected`, which `#` has no equivalent for.

---

## Q38. 📋 Difference between abstract classes and interfaces

Abstract classes can have implementation and cannot be instantiated, while interfaces only define contracts and can be implemented by classes - abstract classes provide base implementation, interfaces provide contracts. Abstract classes can have implementation, interfaces only define contracts.

- **Trade-offs**: The catch is abstract classes can have concrete methods - use cases: abstract classes for shared behavior, interfaces for contracts. Abstract classes provide base implementation, interfaces provide contracts, but watch out - classes can implement multiple interfaces.

Example:

```typescript
// Abstract class: cannot be instantiated, can have implementation
abstract class Animal {
  protected name: string; // Protected: accessible in subclasses
  constructor(name: string) { this.name = name; } // Constructor with implementation
  abstract makeSound(): string; // Abstract method: must be implemented by subclasses
}

// Interface: only defines contract, no implementation
interface Flyable {
  fly(): void; // Method signature only, no implementation
}

// Class can extend abstract class and implement interface
class Bird extends Animal implements Flyable {
  makeSound(): string { return "Chirp"; } // Must implement abstract method
  fly(): void { console.log("Flying"); } // Must implement interface method
}

```

---

## Q39. 🧬 Inheritance

Inheritance uses `extends` keyword, while polymorphism allows objects of different types to be treated uniformly through common interfaces - inheritance maintains type safety across hierarchy. Use `extends` to create class hierarchies.

- **Trade-offs**: The catch is override parent methods in child classes - super keyword calls parent constructor and methods. Inheritance maintains type safety across hierarchy, but watch out - polymorphism means same interface, different implementations.

Example:

```typescript
// Parent class: base implementation
class Vehicle {
  protected brand: string; // Protected: accessible in subclasses
  constructor(brand: string) { this.brand = brand; }
  start(): string { return `${this.brand} started!`; } // Base implementation
}

// Child class: inherits from Vehicle, overrides start method
class Car extends Vehicle {
  start(): string {
    return `Car ${super.start()}`; // super.start() calls parent's start method
  }
}

```

---

## Q40. 💡 Polymorphism

Polymorphism allows objects of different types to be treated uniformly through common interfaces - same interface, different implementations. Same interface, different implementations.

- **Trade-offs**: The catch is enables runtime polymorphism - maintains type safety while allowing flexibility. Same interface, different implementations, but watch out - objects can be treated uniformly through common interfaces.

Example:

```typescript
// Interface: defines contract that multiple classes can implement
interface Shape {
  area(): number; // All shapes must implement area method
}

// Circle implements Shape interface
class Circle implements Shape {
  constructor(private radius: number) {}
  area(): number { return Math.PI * this.radius ** 2; } // Circle's implementation
}

// Rectangle implements same Shape interface
class Rectangle implements Shape {
  constructor(private width: number, private height: number) {}
  area(): number { return this.width * this.height; } // Rectangle's implementation
}

// Polymorphism: treat different shapes uniformly
function printArea(shape: Shape) {
  console.log(shape.area()); // Works with any Shape implementation
}

```

---

## Q41. 💡 Static properties and methods

Static members belong to the class itself rather than instances, accessed through the class name without instantiation - static methods don't require instance creation (memory efficient). Static members belong to the class, not instances.

- **Trade-offs**: The catch is static properties are shared across all instances - utility functions are common use case for static methods. Static methods don't require instance creation (memory efficient), but watch out - can access static members without creating instances.

Example:

```typescript
class MathUtils {
  static PI: number = 3.14159;
  static E: number = 2.71828;

  static add(a: number, b: number): number {
    return a + b;
  }
}

```

---

## Q42. 💡 Readonly properties

`readonly` properties can only be assigned during initialization, preventing modification after object creation - use cases include IDs, timestamps, configuration values. Prevent modification after initialization (immutability).

- **Trade-offs**: The catch is compile-time protection against modification - ensure critical data remains unchanged (data integrity). Use cases include IDs, timestamps, configuration values, but watch out - can assign values in constructor.

Example:

```typescript
class User {
  readonly id: number;
  readonly createdAt: Date;
  public name: string;
  public email: string;

  constructor(id: number, name: string, email: string) {
    this.id = id;
    this.createdAt = new Date();
    this.name = name;
    this.email = email;
  }
}

```

---

## Q43. 🔧 Decorators and how to use them

Decorators are functions that modify classes, methods, or properties, providing metadata and enabling aspect-oriented programming - use cases include logging, validation, dependency injection. Add cross-cutting concerns to classes (aspect-oriented).

- **Trade-offs**: The catch is combine multiple decorators on same target - decorators execute at runtime. Use cases include logging, validation, dependency injection, but watch out - provide additional information about classes/methods (metadata).

Example:

Since **TypeScript 5.0**, decorators follow the TC39 standard proposal (Stage 3) and work *without* any compiler flag. A method decorator receives the original method and a `context` object, and returns a replacement:

```typescript
// Standard decorators (TS 5.0+, no experimentalDecorators flag)
function log<This, Args extends unknown[], Return>(
  target: (this: This, ...args: Args) => Return,
  context: ClassMethodDecoratorContext<This, (this: This, ...args: Args) => Return>
) {
  return function (this: This, ...args: Args): Return {
    console.log(`Calling ${String(context.name)} with`, args);
    return target.call(this, ...args);
  };
}

class User {
  @log
  getName() { return "John"; }
}
```

> **Legacy note (2026):** The older `(target, propertyKey, descriptor)` signature belongs to TypeScript's *experimental* decorators, enabled with `"experimentalDecorators": true` (often with `emitDecoratorMetadata`). Angular, NestJS, TypeORM, and many DI libraries were built on them, so you'll still see this style in those codebases. The two systems are not interchangeable: experimental decorators support parameter decorators and reflect-metadata; standard decorators do not (yet).
>
> ```typescript
> // experimentalDecorators style
> function LogMethod(target: any, methodName: string, descriptor: PropertyDescriptor) {
>   const original = descriptor.value;
>   descriptor.value = function (...args: any[]) {
>     console.log(`Calling ${methodName} with args:`, args);
>     return original.apply(this, args);
>   };
> }
> ```

---

## Q44. 🔧 Mixins and how to use them

Mixins are a way to combine multiple classes into one, enabling multiple inheritance-like behavior in TypeScript - mixins add functionality to existing classes (flexibility). Combine multiple classes into one (multiple inheritance).

- **Trade-offs**: The catch is use interfaces to declare mixin types - mixins are applied at runtime. Mixins add functionality to existing classes (flexibility), but watch out - use functions to apply multiple classes (mixin pattern).

Example:

```typescript
function Timestamped<T extends new (...args: any[]) => {}>(Base: T) {
  return class extends Base {
    timestamp: Date = new Date();
    getTimestamp() { return this.timestamp; }
  };
}

class User { name: string = "John"; }
const TimestampedUser = Timestamped(User);
const user = new TimestampedUser();

```

---

## Q45. 🎯 The `satisfies` operator

`satisfies` (TypeScript 4.9) checks that an expression matches a type **without changing the type TypeScript infers for it**. Compare the three options:

- A **type annotation** (`const x: T = ...`) checks the value but *widens* it to `T`, so you lose the specific literal types and keys.
- A **type assertion** (`... as T`) doesn't really check - it tells the compiler to trust you.
- **`satisfies T`** checks the value against `T` (including excess-property checks) and keeps the narrow inferred type.

- **Trade-offs**: It's ideal for config objects, route tables, theme tokens, and lookup maps where you want both validation and precise autocomplete. It's not a replacement for annotations on function parameters or public APIs - there you *want* the declared type. Combine with `as const` (`{...} as const satisfies T`) for deeply readonly literal types.

Example:

```typescript
type Route = { path: string; auth?: boolean };

// Annotation: checked, but keys are widened to string
const routesA: Record<string, Route> = { home: { path: '/' }, admin: { path: '/admin', auth: true } };
routesA.hoem; // no error - any string key is allowed

// satisfies: checked AND the exact keys are preserved
const routes = {
  home: { path: '/' },
  admin: { path: '/admin', auth: true },
  // bogus: { pth: '/x' }, // ❌ error - 'pth' does not exist in type 'Route'
} satisfies Record<string, Route>;

routes.hoem;  // ❌ error - Property 'hoem' does not exist
routes.admin; // ✅ autocomplete knows exactly 'home' | 'admin'

type Palette = Record<'primary' | 'secondary', string | [number, number, number]>;
const colors = { primary: '#0af', secondary: [0, 128, 255] } satisfies Palette;
colors.primary.toUpperCase(); // ✅ still known to be a string, not string | tuple
```

---

## Q46. 🧷 `const` type parameters

By default, TypeScript widens literals when inferring generics: passing `['a', 'b']` infers `string[]`. Adding the `const` modifier to a type parameter (TypeScript 5.0) makes inference behave as if the caller wrote `as const` - you get readonly tuples and literal types, without forcing every caller to remember `as const`.

- **Trade-offs**: Great for builder APIs, route definitions, event names, and anything where literal values drive types. The inferred types are `readonly`, so constrain with `readonly unknown[]` - with a mutable `unknown[]` constraint the readonly tuple doesn't fit and inference can fall back to the wide type. It only affects literals written directly at the call site - a variable declared earlier keeps its already-widened type.

Example:

```typescript
function pick<T extends readonly string[]>(keys: T): T { return keys; }
const a = pick(['id', 'name']); // string[]

function pickConst<const T extends readonly string[]>(keys: T): T { return keys; }
const b = pickConst(['id', 'name']); // readonly ['id', 'name']

// Practical use: type-safe event registry
function defineEvents<const E extends readonly string[]>(events: E) {
  return {
    on(event: E[number], handler: () => void) { /* ... */ },
  };
}
const bus = defineEvents(['login', 'logout']);
bus.on('login', () => {});   // ✅
bus.on('signup', () => {});  // ❌ Argument of type '"signup"' is not assignable
```

---

## Q47. 🧹 `using` declarations (explicit resource management)

`using` (TypeScript 5.2) implements the TC39 Explicit Resource Management proposal. A variable declared with `using` is automatically disposed when it goes out of scope - its `[Symbol.dispose]()` method runs at the end of the block, even if an exception is thrown. `await using` does the same with `[Symbol.asyncDispose]()` for async cleanup. Think of it as JavaScript's version of C#'s `using` or Python's `with`.

- **Trade-offs**: It removes error-prone `try/finally` boilerplate for file handles, DB connections, locks, and temporary subscriptions, and disposes multiple resources in reverse order automatically. Runtime support is still rolling out: some engines (recent V8-based Chrome and Node releases) ship `Symbol.dispose` natively, but for older targets you need `"lib": ["esnext.disposable"]` (or `"esnext"`), down-level compilation, and a polyfill for `Symbol.dispose`/`Symbol.asyncDispose`. Check your target runtimes before using it in production.

Example:

```typescript
class TempFile implements Disposable {
  constructor(public path: string) { console.log('open', path); }
  [Symbol.dispose]() { console.log('delete', this.path); }
}

function process() {
  using file = new TempFile('/tmp/data.csv');
  using lock = acquireLock();          // disposed first (reverse order)
  if (Math.random() > 0.5) throw new Error('boom');
  return 'done';
} // lock and file are disposed here - on return AND on throw

async function query() {
  await using conn = await pool.connect(); // conn[Symbol.asyncDispose]() is awaited on exit
  return conn.query('SELECT 1');
}

// DisposableStack collects ad-hoc cleanups
function setup() {
  using stack = new DisposableStack();
  const timer = setInterval(tick, 1000);
  stack.defer(() => clearInterval(timer));
}
```

---

## Q48. 📦 Namespaces vs ES modules

Namespaces (originally called "internal modules") group code under a named object, e.g. `namespace Validation { export function isEmail() {} }`, and compile to an IIFE that builds a global object. ES modules instead scope everything to the file and share code with `import`/`export`.

> **Legacy note (2026):** Namespaces pre-date ES modules and are considered legacy for application code. They're one of the few TS features that emit runtime code, so they are rejected by `erasableSyntaxOnly`, don't work with Node's built-in type stripping, and don't tree-shake well. The TypeScript handbook itself recommends ES modules for new code. Where you'll still meet them: old codebases using `/// <reference path="..." />` and `outFile`, and **type-only** uses in declaration files - `declare namespace` to describe a global library (like `declare namespace NodeJS { ... }`) or to augment types - which is still perfectly normal.

- **Trade-offs**: Modules give you explicit dependencies, tree-shaking, lazy loading via `import()`, and compatibility with every bundler and runtime. If you want a namespaced API from a module, re-export it: `export * as Validation from './validation.js'` gives callers `Validation.isEmail()` with none of the downsides.

Example:

```typescript
// ❌ Legacy: namespace (emits an IIFE + global object)
namespace Validation {
  export function isEmail(s: string) { return s.includes('@'); }
}
Validation.isEmail('a@b.c');

// ✅ Modern: ES module
// validation.ts
export function isEmail(s: string) { return s.includes('@'); }
// index.ts
export * as Validation from './validation.js';
// app.ts
import { Validation } from './index.js';
Validation.isEmail('a@b.c');

// ✅ Still fine: type-only namespace in a .d.ts for a global script library
declare namespace Analytics {
  function track(event: string, props?: Record<string, unknown>): void;
}
```

---

## Q49. 🛡️ Narrowing `unknown` safely: type predicates, assertion functions, and schemas

TypeScript types disappear at runtime, so data from outside your program (HTTP responses, `JSON.parse`, `localStorage`, form input) should enter as `unknown` and be **proven** to have a shape before use. Three tools do that:

1. **Type predicates** - a function returning `value is T` narrows the type in the caller's `if`. Since TypeScript 5.5, simple filter-style functions like `x => x !== null` get an inferred predicate automatically.
2. **Assertion functions** - `asserts value is T` throws if the check fails and narrows everything after the call.
3. **Schema validators** (Zod, Valibot, ArkType, etc.) - define the schema once, get both runtime validation and the static type via inference. This is the most common choice for API boundaries today.

- **Trade-offs**: Hand-written predicates are trusted, not verified - if the body is wrong, the compiler believes it anyway, so keep them small and tested. Schema libraries add bundle size but eliminate drift between the runtime check and the type. Avoid `as SomeType` on parsed JSON - it's the most common source of "TypeScript said it was fine" production bugs.

Example:

```typescript
type User = { id: number; name: string };

// 1. Type predicate
function isUser(value: unknown): value is User {
  return typeof value === 'object' && value !== null
    && 'id' in value && typeof value.id === 'number'
    && 'name' in value && typeof value.name === 'string';
}

// 2. Assertion function
function assertUser(value: unknown): asserts value is User {
  if (!isUser(value)) throw new TypeError('Invalid user payload');
}

const data: unknown = await fetch('/api/me').then(r => r.json());
assertUser(data);
data.name; // ✅ narrowed to User from here on

// Inferred type predicate (TS 5.5): no annotation needed
const ids = [1, null, 3].filter(x => x !== null); // number[] (was (number | null)[] before 5.5)

// 3. Schema validation (Zod shown; the pattern is the same in other libraries)
import { z } from 'zod';
const UserSchema = z.object({ id: z.number(), name: z.string() });
type UserFromSchema = z.infer<typeof UserSchema>; // { id: number; name: string }
const parsed = UserSchema.safeParse(data);
if (parsed.success) parsed.data.name;
```

---

