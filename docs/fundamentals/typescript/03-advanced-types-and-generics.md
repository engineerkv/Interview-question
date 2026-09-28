---
sidebar_label: "Advanced Types & Generics"
---
# ⚡ 3. Advanced Types & Generics (Q25–36)

> **Reviewed:** 2026-09 · Modernized; legacy topics are labeled.

---

## Q25. 🔧 Function overloading and overriding

Function overloading allows you to define multiple signatures for the same function with different parameter types - TypeScript picks the right one based on what you pass, and you write one implementation that handles all cases. Overriding happens when a child class replaces a parent class method with its own implementation - the child's version runs at runtime instead of the parent's.

- **Trade-offs**: The catch is overloading is compile-time only - TypeScript uses it for type checking, but at runtime there's just one function that needs to handle all cases. Overriding enables runtime polymorphism where the actual method called depends on the object type, but you need to make sure the child method matches the parent's signature or TypeScript will complain.

Example:

```typescript
// Overloading: multiple type signatures, one implementation
function process(value: string): string; // Signature 1: string input → string output
function process(value: number): number; // Signature 2: number input → number output
function process(value: string | number): string | number { // Implementation handles both
  return typeof value === "string" ? value.toUpperCase() : value * 2;
}

// Overriding: child class replaces parent method implementation
class Animal {
  makeSound(): void {
    console.log("Some sound"); // Parent implementation
  }
}

class Dog extends Animal {
  override makeSound(): void { // `override` (TS 4.3) - errors if the parent method is renamed or removed
    console.log("Woof!"); // Child's implementation runs at runtime
  }
}
// Enable "noImplicitOverride": true so the `override` keyword is required

```

---

## Q26. 📝 Difference between optional and default parameters in TypeScript

Optional parameters use `?` and can be undefined, while default parameters provide a fallback value when omitted - optional parameters allow undefined, default parameters provide a value. Optional parameters are typed as `T | undefined`, default parameters maintain the original type.

- **Trade-offs**: The catch is optional parameters require type guards to handle undefined - default parameters eliminate the need for undefined checks. Optional parameters provide flexibility, but watch out - default parameters provide better type safety and cleaner code.

Example:

```typescript
// Optional parameter
function greet(name?: string): string {
  return name ? `Hello, ${name}` : "Hello";
}

// Default parameter
function greetDefault(name: string = "Guest"): string {
  return `Hello, ${name}`;
}

// Optional requires undefined check
function process(value?: number): void {
  if (value !== undefined) {
    console.log(value * 2);
  }
}

// Default provides value automatically
function processDefault(value: number = 0): void {
  console.log(value * 2); // Always works
}

```

---

## Q27. 🌐 Default and rest parameters

Default parameters provide fallback values, while rest parameters collect remaining arguments into an array - default and rest parameters improve function flexibility. Default parameters provide fallback values when arguments are omitted.

- **Trade-offs**: The catch is rest parameters are typed as arrays, functions can handle variable number of arguments - rest parameters must come last in parameter list. Default and rest parameters improve function flexibility, but watch out - rest parameters collect variable number of arguments into array.

Example:

```typescript
function greet(name: string, greeting: string = "Hello"): string {
  return `${greeting}, ${name}!`;
}

function sum(...numbers: number[]): number {
  return numbers.reduce((total, num) => total + num, 0);
}

```

---

## Q28. 🔧 Generics and how to use them

Generics allow you to write code once and use it with different types, keeping everything type-safe - generics provide better IDE support with IntelliSense. Maintain type information throughout function execution.

- **Trade-offs**: The catch is work with any type while preserving type constraints - reduce code duplication and improve maintainability. Generics provide better IDE support with IntelliSense, but watch out - write once, use with multiple types (reusability).

Example:

```typescript
// Generic function: T is type parameter, can be any type
function identity<T>(arg: T): T {
  return arg; // Returns same type as input
}

// Generic interface: T can be specified when using the interface
interface Container<T> {
  value: T; // Value of type T
  getValue(): T; // Method returns type T
}

// Usage: specify type when using
const stringContainer: Container<string> = { value: "hello", getValue: () => "hello" };
const numberContainer: Container<number> = { value: 42, getValue: () => 42 };

// Usually you let inference pick T instead of writing it
const inferred = identity(['a', 'b']); // T = string[]
// Want literal types inferred instead? See `const` type parameters (Q46, TS 5.0).

```

---

## Q29. 🔧 Generic constraints and how to use them

The `extends` keyword constrains generic types to specific shapes or types, ensuring they have required properties - use with `keyof` operator to constrain to object keys. Limit generic types to specific shapes.

- **Trade-offs**: The catch is prevent errors from missing properties - still allow different types that meet constraints. Use with `keyof` operator to constrain to object keys, but watch out - ensure required properties exist on generic type.

Example:

```typescript
// Generic constraint: T must have 'length' property
function getLength<T extends { length: number }>(item: T): number {
  return item.length; // TypeScript knows T has length property
}

// Constraint to object type, return array of keys
function getKeys<T extends object>(obj: T): (keyof T)[] {
  return Object.keys(obj) as (keyof T)[]; // Cast to typed array of keys
}

```

---

## Q30. 📝 Utility types and how to use them

Utility types are built-in type transformations that modify existing types for common use cases - utility types reduce boilerplate code. Partial (makes all properties optional), Pick (selects specific properties), Omit (excludes specific properties).

- **Trade-offs**: The catch is partial makes all properties optional for updates - these utility types are built on mapped types. Utility types reduce boilerplate code, but watch out - Required (makes all properties required), Readonly (makes all properties immutable).

Example:

```typescript
interface User {
  id: number;
  name: string;
  email: string;
  age: number;
}

type PartialUser = Partial<User>; // All optional
type UserName = Pick<User, 'name'>; // Only name
type UserWithoutId = Omit<User, 'id'>; // Exclude id
type RequiredUser = Required<PartialUser>; // All required
type ReadonlyUser = Readonly<User>; // All readonly
type Roles = Record<'admin' | 'user', string[]>; // Object type from key union
type NonNull = NonNullable<string | null>; // string
type Resolved = Awaited<Promise<Promise<number>>>; // number (TS 4.5)
type Params = Parameters<(a: string, b: number) => void>; // [a: string, b: number]

// NoInfer<T> (TS 5.4) stops a parameter from influencing inference
function createFSM<S extends string>(states: S[], initial: NoInfer<S>) {}
createFSM(['idle', 'running'], 'stopped'); // ❌ error - 'stopped' isn't one of the states

```

---

## Q31. 📝 Mapped types and how to use them

Mapped types transform existing types by applying transformations to each property, creating new types based on existing ones - mapped types enable complex type transformations. Iterate over all properties of a type.

- **Trade-offs**: The catch is modify property names using template literals - use conditional types within mapped types. Mapped types enable complex type transformations, but watch out - apply transformations to each property.

Example:

```typescript
type Optional<T> = {
  [K in keyof T]?: T[K];
};

type MyReadonly<T> = { // named MyReadonly so it doesn't clash with the built-in Readonly
  readonly [K in keyof T]: T[K];
};

type Mutable<T> = {
  -readonly [K in keyof T]: T[K]; // `-` removes a modifier (also works with `-?`)
};

```

---

## Q32. 📝 Conditional types and how to use them

Conditional types select one of two types based on a condition, enabling type-level programming and complex type transformations - conditional types enable complex type manipulations. Perform logic at the type level.

- **Trade-offs**: The catch is can be recursive for complex transformations - use never to exclude types. Conditional types enable complex type manipulations, but watch out - choose between types based on conditions.

Example:

```typescript
type IsString<T> = T extends string ? true : false;

type ApiResponse<T> = T extends string
  ? { message: T }
  : { data: T };

// Conditional types *distribute* over unions when T is a naked type parameter
type ToArray<T> = T extends unknown ? T[] : never;
type A = ToArray<string | number>; // string[] | number[]
type NoDistribute<T> = [T] extends [unknown] ? T[] : never;
type B = NoDistribute<string | number>; // (string | number)[]

```

---

## Q33. 🔧 `infer` keyword and how to use it

`infer` extracts and infers types from other types within conditional types, enabling powerful type inference patterns - use cases include utility types, type extraction, pattern matching. Extract types from other types.

- **Trade-offs**: The catch is let TypeScript infer types automatically - enable complex type transformations. Use cases include utility types, type extraction, pattern matching, but watch out - match patterns and extract parts.

Example:

```typescript
// Re-implementations of built-ins (renamed to avoid clashing with the global ReturnType/Parameters)
type MyReturnType<T> = T extends (...args: any[]) => infer R ? R : never;

type MyParameters<T> = T extends (...args: infer P) => any ? P : never;

// infer with an extends constraint (TS 4.7)
type FirstString<T> = T extends [infer S extends string, ...unknown[]] ? S : never;
type F = FirstString<['a', 1]>; // 'a'

```

---

## Q34. 📝 `keyof` and `typeof` operators

`keyof` extracts keys from object types, while `typeof` gets the type of a value, both enabling type-level operations - these operators enable type-level programming. `keyof` extracts all keys from object types, `typeof` gets type of a value or expression.

- **Trade-offs**: The catch is use keys to access property types (indexed access) - use together for advanced type operations. These operators enable type-level programming, but watch out - enable type-safe property access.

Example:

```typescript
interface User {
  id: number;
  name: string;
  email: string;
}

type UserKeys = keyof User; // "id" | "name" | "email"
type UserName = User["name"]; // string

const user = { id: 1, name: "John", age: 30 };
type UserType = typeof user; // { id: number; name: string; age: number; }

```

---

## Q35. 💡 Covariance and contravariance

Covariance preserves the subtype relationship in the same direction, while contravariance reverses it, affecting function parameter and return types - variance affects function parameter and return types. Covariance preserves subtype relationship in same direction, contravariance reverses it.

- **Trade-offs**: The catch is variance rules ensure type safety - understanding variance helps with complex generic types. Variance affects function parameter and return types, but watch out - function parameters are contravariant, returns are covariant.

Example:

```typescript
class Animal { name = ''; }
class Dog extends Animal { breed = ''; }

// Covariance: return types preserve subtype relationship
function getAnimal(): Animal { return new Dog(); } // ✅ Valid: Dog is subtype of Animal

// Contravariance: parameter types reverse subtype relationship
function processAnimal(animal: Animal): void { }
function processDog(dog: Dog): void { console.log(dog.breed); }

// A function that accepts any Animal can safely stand in where only Dogs will be passed
let dogHandler: (dog: Dog) => void = processAnimal; // ✅ Valid: contravariant
// But a Dog-only function can't handle every Animal (it would read .breed on a Cat)
let animalHandler: (animal: Animal) => void = processDog; // ❌ Error under strictFunctionTypes

// Explicit variance annotations on type parameters (TS 4.7) - mostly for library authors
interface Producer<out T> { get(): T }
interface Consumer<in T> { accept(value: T): void }

```

---

## Q36. ⚡ Performance considerations when using TypeScript

Performance considerations include compilation time, bundle size, type checking overhead, and the balance between type safety and development speed - avoid overly complex types in performance-critical code. Use incremental compilation and build caching (compilation time).

- **Trade-offs**: The catch is can be disabled for faster development builds (type checking) - only recompile changed files (incremental builds). Avoid overly complex types in performance-critical code, but watch out - TypeScript types are stripped at compile time (bundle size).

Example:

```json
{
  "compilerOptions": {
    "incremental": true, // Enable incremental compilation
    "tsBuildInfoFile": ".tsbuildinfo", // Cache build info for faster rebuilds
    "skipLibCheck": true // Skip type checking of declaration files (faster compilation)
  }
}

```

Other levers used on large codebases in 2026:

- **Separate type checking from emitting** - let esbuild/SWC/Vite transpile (fast, per-file) and run `tsc --noEmit` in CI and the editor. This requires `isolatedModules` (or `verbatimModuleSyntax`).
- **Project references** (`"composite": true` + `tsc --build`) split a monorepo into independently cached projects.
- **`isolatedDeclarations`** (TS 5.5) requires explicit types on exports so `.d.ts` files can be generated per file, in parallel, by other tools.
- **Diagnose before optimizing** - `tsc --extendedDiagnostics` and `--generateTrace` show which files and types are slow. Common culprits are huge unions, deeply recursive conditional types, and large `&` intersections (prefer `interface extends`).
- Microsoft's native Go port of the compiler (announced in 2025 and planned as TypeScript 7) targets large speedups on the same code - check its current release status before relying on it.

---

