---
sidebar_label: "Fundamentals & Setup"
---
# 🧠 1. Fundamentals & Setup (Q1–10)

> **Reviewed:** 2026-09 · Modernized; legacy topics are labeled.

---

## Q1. 📝 TypeScript and how it differs from JavaScript

TypeScript is a statically typed superset of JavaScript that compiles to plain JavaScript, providing type safety and better tooling support - you can gradually adopt TypeScript in existing JavaScript projects. Static typing checks types at compile time, JavaScript at runtime.

- **Trade-offs**: The catch is TypeScript compiles to JavaScript, not interpreted directly - better IDE support with autocomplete, refactoring, and error detection. You can gradually adopt TypeScript in existing JavaScript projects, but watch out - superset means all valid JavaScript is valid TypeScript.

Example:

```typescript
// JavaScript
function greet(name) {
  return "Hello, " + name;
}

// TypeScript
function greet(name: string): string {
  return "Hello, " + name;
}

```

---

## Q2. 📝 Key features of TypeScript

TypeScript's key features include static typing, type inference, interfaces, generics, enums, access modifiers, and compilation to JavaScript - these features enable better code quality and developer experience. Static typing provides compile-time type checking, catching errors before runtime.

- **Trade-offs**: The catch is type inference reduces boilerplate while maintaining type safety - interfaces define contracts for objects and classes. Generics enable reusable code with type parameters, but watch out - enums provide type-safe constants, access modifiers control visibility in classes.

Example:

```typescript
// Static typing
let name: string = "John";

// Type inference
let age = 30; // Inferred as number

// Interfaces
interface User {
  id: number;
  name: string;
}

// Generics
function identity<T>(arg: T): T {
  return arg;
}

// Enums
enum Status {
  Active,
  Inactive
}

```

---

## Q3. 📝 How TypeScript improves code quality and development in large-scale applications

TypeScript improves code quality and development experience through early error detection, better IDE support, self-documenting code, improved refactoring capabilities, and enhanced team collaboration - catches errors during development, not production. Type safety prevents common runtime errors like null reference exceptions and type mismatches, which is especially critical in large-scale applications where bugs can be costly and hard to track down.

- **Trade-offs**: The catch is better IDE support provides autocomplete, go-to-definition, and find references - self-documenting types serve as inline documentation that reduces the need for external documentation. Improved refactoring enables safe renaming and restructuring across large codebases with confidence, but watch out - enhanced team collaboration through clear contracts between components becomes essential when multiple developers work on the same codebase. In large-scale applications, TypeScript's type system acts as a communication tool, making it easier for teams to understand code structure and dependencies without reading implementation details.

Example:

```typescript
interface ApiResponse<T> {
  data: T;
  status: number;
  message?: string;
}

interface User {
  id: number;
  name: string;
  email: string;
}

function handleResponse<T>(response: ApiResponse<T>): void {
  // TypeScript ensures response has correct structure
  if (response.status === 200) {
    console.log(response.data);
  }
}

function createUser(userData: User): User {
  // Type safety ensures all required fields are present
  return {
    id: Date.now(),
    name: userData.name,
    email: userData.email
  };
}

```

---

## Q4. 📝 Installing and setting up TypeScript

Install TypeScript globally or locally, then create a `tsconfig.json` file to configure the compiler - different configs for development vs production. Install TypeScript as a dev dependency for projects.

- **Trade-offs**: The catch is configure compiler options based on project needs - use different configs for development vs production. Different configs for development vs production, but watch out - use `tsc --init` to create a default `tsconfig.json`.

Example:

```bash
npm install --save-dev typescript   # pin the compiler per project
npx tsc --init                      # generate tsconfig.json
npx tsc --noEmit                    # type-check only (common when a bundler emits JS)
```

In 2026, the compiler is often used purely as a **type checker**, while a faster tool strips types and emits JS: Vite/esbuild/SWC for front-ends, `tsx` for scripts, and Node itself - recent Node releases (23.6+, backported to 22.18) run `.ts` files directly by stripping *erasable* type syntax. That's why the `erasableSyntaxOnly` option (TS 5.8) exists: it flags TS-only runtime constructs like `enum`, `namespace`, and constructor parameter properties that can't simply be erased.

> **Legacy note (2026):** `npm install -g typescript` still works but a global compiler drifts from each project's version - prefer a local dev dependency run via `npx`. Likewise `ts-node` has largely been replaced by `tsx` or Node's built-in type stripping.

---

## Q5. 📝 Type inference

Type inference is TypeScript's ability to automatically determine the type of a variable based on its initial value - function return types can be inferred from function body. TypeScript analyzes code to determine types automatically.

- **Trade-offs**: The catch is context-aware inference considers surrounding code context - for arrays, finds the most specific common type. Function return types can be inferred from function body, but watch out - reduces boilerplate, less need for explicit type annotations.

Example:

```typescript
let message = "Hello World"; // Inferred as 'string'
let count = 42; // Inferred as 'number'
let isReady = true; // Inferred as 'boolean'
let numbers = [1, 2, 3]; // Inferred as 'number[]'
let mixed = [1, "hello", true]; // Inferred as '(string | number | boolean)[]'

```

---

## Q6. 📝 Primitive types

TypeScript includes string, number, boolean, null, undefined, symbol, bigint, and void as primitive types - TypeScript extends JavaScript's type system. String (text data), Number (both integers and floating-point), Boolean (true or false).

- **Trade-offs**: The catch is Symbol (unique identifiers, often used as object keys), BigInt (arbitrary precision integers) - Void (absence of any type, commonly used for functions). TypeScript extends JavaScript's type system, but watch out - Null/Undefined represent absence of value differently.

Example:

```typescript
let name: string = "John";
let age: number = 30;
let isActive: boolean = true;
let data: null = null;
let value: undefined = undefined;

```

---

## Q7. 🤔 Differences between `any`, `unknown`, and `never`

`any` disables type checking, `unknown` is type-safe but requires type checking, and `never` represents values that never occur. The modern rule of thumb: **reach for `unknown`, not `any`**, whenever you don't know a type yet - API responses, `JSON.parse` output, `catch` variables (under `strict`, `useUnknownInCatchVariables` already types them as `unknown`). `unknown` forces you to narrow (with `typeof`, `instanceof`, `in`, or a schema validator like Zod/Valibot) before use; `any` silently spreads through your code. Keep `any` for migrations and truly untyped edges, and enforce this with `@typescript-eslint/no-explicit-any`.

- **Trade-offs**: The catch is never represents impossible states, useful for exhaustive checking - unknown is safer than any, never is for impossible cases. Use cases: any for quick fixes, unknown for user input, never for error handling, but watch out - unknown is type-safe alternative to any, requires type narrowing before use.

Example:

```typescript
let anything: any = 42;
anything = "hello"; // No error, but will crash at runtime

let userInput: unknown = getUserInput();
if (typeof userInput === "string") {
  console.log(userInput.toUpperCase()); // Safe to use
}

function throwError(message: string): never {
  throw new Error(message);
}

try {
  riskyCall();
} catch (err) { // err: unknown under strict
  const message = err instanceof Error ? err.message : String(err);
}

```

---

## Q8. 🔧 Tuples and how to use them

Tuples are arrays with fixed length and known types at each position, while arrays have variable length and same type elements - tuples provide stronger type safety than arrays. Tuples have fixed length, arrays have variable length.

- **Trade-offs**: The catch is coordinates, key-value pairs, function returns - can destructure tuples like arrays, tuples can have optional elements with ?. Tuples provide stronger type safety than arrays, but watch out - type safety means each position has a specific type.

Example:

```typescript
let person: [string, number] = ["John", 30];
let coordinates: [number, number] = [10, 20];
let names: string[] = ["John", "Jane", "Bob"];

```

---

## Q9. 🔧 Enums and how to use them

Enums define a set of named constants, with numeric enums having auto-incrementing values and string enums having explicit string values - enums provide type-safe constants. Numeric enums have auto-incrementing numbers starting from 0, string enums have explicit string values.

- **Trade-offs**: The catch is numeric enums create reverse lookup, string enums have no reverse mapping - status codes, configuration options, constants. Enums provide type-safe constants, but watch out - type safety prevents invalid enum values.

Example:

```typescript
enum Status {
  Pending,    // 0
  Approved,   // 1
  Rejected    // 2
}

enum Color {
  Red = "red",
  Green = "green",
  Blue = "blue"
}

let currentStatus: Status = Status.Pending;
let favoriteColor: Color = Color.Blue;

// Common 2026 alternative: a union of string literals (zero runtime cost)
type StatusName = 'pending' | 'approved' | 'rejected';

// ...or an "as const" object when you also want runtime values to iterate over
const STATUS = { Pending: 'pending', Approved: 'approved', Rejected: 'rejected' } as const;
type StatusValue = (typeof STATUS)[keyof typeof STATUS]; // 'pending' | 'approved' | 'rejected'

```

**Enums vs union types - the trade-off interviewers want:** Enums are one of the few TypeScript features that emit runtime JavaScript. Numeric enums accept any number (`const s: Status = 42` compiles), generate a reverse mapping object, and don't work with "type-stripping" runtimes such as Node's built-in TS support or `erasableSyntaxOnly`. `const enum` inlines values but breaks under `isolatedModules` across files. String literal unions (optionally backed by an `as const` object) give the same autocomplete and exhaustiveness checking with plain JS output, so many teams now default to them. Enums are still fine in existing codebases - just prefer string enums over numeric ones if you use them.

---

## Q10. 💡 Purpose of `tsconfig.json` and key compiler options

`tsconfig.json` configures TypeScript compiler options, including target, module, strict mode, and file inclusion settings - different configs for development vs production. Controls how TypeScript compiles code.

- **Trade-offs**: The catch is strict mode enables additional type checking options - file management controls which files to include/exclude. Different configs for development vs production, but watch out - Target (JavaScript version to compile to), Module system (CommonJS, ES modules).

Example:

A solid 2026 baseline for an app built with a bundler (Vite, Next.js, etc.):

```json
{
  "compilerOptions": {
    "target": "ES2022",
    "lib": ["ES2023", "DOM", "DOM.Iterable"],
    "module": "ESNext",
    "moduleResolution": "bundler",
    "strict": true,
    "noUncheckedIndexedAccess": true,
    "exactOptionalPropertyTypes": true,
    "noImplicitOverride": true,
    "verbatimModuleSyntax": true,
    "isolatedModules": true,
    "skipLibCheck": true,
    "noEmit": true
  },
  "include": ["src"]
}
```

For a Node.js library or server that `tsc` compiles itself, swap to `"module": "NodeNext"` (which implies `"moduleResolution": "NodeNext"`), drop `noEmit`, and set `outDir`/`declaration`.

What the key options buy you:

- **`strict`** - turns on the whole strict family (`strictNullChecks`, `noImplicitAny`, `strictFunctionTypes`, `useUnknownInCatchVariables`, ...). Non-negotiable for new code.
- **`noUncheckedIndexedAccess`** - `arr[i]` and `record[key]` become `T | undefined`, catching out-of-bounds bugs `strict` alone misses.
- **`verbatimModuleSyntax`** (TS 5.0) - imports are emitted exactly as written; type-only imports must use `import type`. Replaces the older `importsNotUsedAsValues`/`preserveValueImports` flags and keeps you compatible with single-file transpilers.
- **`moduleResolution: "bundler"`** (TS 5.0) - matches how Vite/esbuild resolve imports (extensionless paths, `package.json` `exports`). **`"NodeNext"`** matches real Node ESM/CJS rules, including required `.js` extensions in relative imports.

> **Legacy note (2026):** `"module": "commonjs"` with `"moduleResolution": "node"` (now called `node10`) and `esModuleInterop` was the standard setup for years and is still common in older Node projects. New projects should target ESM with `bundler` or `NodeNext` resolution.

---

