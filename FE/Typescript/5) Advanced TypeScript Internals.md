# 5. Advanced TypeScript Internals (Q40–53)

---

## Q40. How does module resolution work?

Module resolution determines how TypeScript finds and loads modules, with classic strategy for legacy code and node strategy for modern Node.js - node strategy is the modern standard. Classic strategy (legacy resolution, looks for .ts files first), Node strategy (modern resolution, follows Node.js module resolution).

- **Trade-offs**: The catch is node strategy handles .js, .ts, .d.ts files - node strategy supports index files and directory imports. Node strategy is the modern standard, but watch out - use baseUrl and paths for custom module resolution.

Example:

```typescript
{
  "compilerOptions": {
    "moduleResolution": "node",
    "baseUrl": "./src",
    "paths": { "@/*": ["src/*"] }
  }
}
```

---

## Q41. How does the internal classic module resolution strategy work?

Classic module resolution looks for TypeScript files first, then checks for declaration files, following a simple file extension priority order - simple logic uses straightforward file extension matching. .ts files take precedence over .d.ts files.

- **Trade-offs**: The catch is doesn't look in node_modules directory - designed for older TypeScript projects. Simple logic uses straightforward file extension matching, but watch out - checks .ts, then .d.ts, then index files.

Example:

```typescript
import { utils } from './utils'; // Looks for:
// 1. ./utils.ts
// 2. ./utils.d.ts
// 3. ./utils/index.ts
// 4. ./utils/index.d.ts
```

---

## Q42. How does the internal node module resolution strategy work?

Node module resolution follows Node.js algorithm, checking node_modules, package.json, and supporting directory imports with index files - follows Node.js module resolution algorithm (modern standard). Searches node_modules directory hierarchy.

- **Trade-offs**: The catch is checks @types packages for type definitions - supports importing directories with index files. Follows Node.js module resolution algorithm (modern standard), but watch out - uses main field in package.json to find entry point.

Example:

```typescript
import { lodash } from 'lodash'; // Looks for:
// 1. ./node_modules/lodash/package.json (main field)
// 2. ./node_modules/lodash/index.js
// 3. ./node_modules/lodash/index.d.ts
// 4. ./node_modules/@types/lodash/index.d.ts
```

---

## Q43. What are declaration files and how do you create them?

Declaration files provide type information for JavaScript libraries, generated automatically or written manually for type safety - enable type checking for JavaScript code (type safety). Provide type definitions for JavaScript libraries.

- **Trade-offs**: The catch is write .d.ts files for external libraries (manual creation) - use declare module for external modules. Enable type checking for JavaScript code (type safety), but watch out - TypeScript can generate .d.ts files from .ts files (auto-generation).

Example:

```typescript
declare module "my-library" {
  export interface Config {
    apiKey: string;
    timeout?: number;
  }
}
```

---

## Q44. What are ambient modules and how do you use them?

Ambient modules declare types for existing JavaScript code, while normal modules are TypeScript modules with implementation - ambient modules don't affect runtime behavior (no runtime). Ambient modules are type declarations without implementation.

- **Trade-offs**: The catch is use ambient modules for JavaScript libraries (external libraries) - ambient modules provide type safety for external code. Ambient modules don't affect runtime behavior (no runtime), but watch out - normal modules are TypeScript modules with actual implementation.

Example:

```typescript
declare module "lodash" {
  export function chunk<T>(array: T[], size: number): T[][];
  export function debounce<T extends (...args: any[]) => any>(
    func: T, wait: number): T;
}
```

---

## Q45. What is the `declare` keyword and how do you use it?

`declare` tells TypeScript that a variable, function, or module exists elsewhere, providing type information without implementation - declare statements don't generate JavaScript code (no runtime impact). Provide types without implementation (type information).

- **Trade-offs**: The catch is declare types for external modules - declare global namespaces. Declare statements don't generate JavaScript code (no runtime impact), but watch out - declare global variables and their types.

Example:

```typescript
declare const process: {
  env: {
    NODE_ENV: string;
    API_URL: string;
  };
};
```

---

## Q46. What is the difference between namespaces and ES modules?

Namespaces provide logical grouping of code and can be split across files, while ES modules are the modern standard for module systems - use cases: namespaces for legacy code, ES modules for new projects. Namespaces group related code together (logical grouping).

- **Trade-offs**: The catch is ES modules are modern standard for module system - ES modules support tree shaking. Use cases: namespaces for legacy code, ES modules for new projects, but watch out - namespaces can be split across multiple files.

Example:

```typescript
namespace MathUtils {
  export function add(a: number, b: number): number {
    return a + b;
  }
}

export function multiply(a: number, b: number): number {
  return a * b;
}
```

---

## Q47. What is strict mode and why is it important?

Strict mode enables additional type checking options, with `strictNullChecks` preventing null and undefined from being assigned to non-nullable types - reduces runtime errors in production. Enables additional type checking options.

- **Trade-offs**: The catch is more rigorous type checking (type safety) - helps catch errors during development. Reduces runtime errors in production, but watch out - strictNullChecks prevents null/undefined errors (null safety).

Example:

```typescript
{
  "compilerOptions": {
    "strict": true,
    "strictNullChecks": true,
    "strictFunctionTypes": true
  }
}
```

---

## Q48. What is the difference between compile-time and runtime type checking?

Compile-time checking happens during TypeScript compilation, while runtime checking happens during JavaScript execution - combine both for maximum type safety. TypeScript checks types during compilation (compile time).

- **Trade-offs**: The catch is use runtime checks to narrow types (type guards) - compile-time checking has no runtime cost (performance). Combine both for maximum type safety, but watch out - JavaScript has no built-in type checking (runtime).

Example:

```typescript
function processData(data: string): number {
  return data.length; // TypeScript checks types at compile time
}

function isString(value: any): value is string {
  return typeof value === "string";
}
```

---

## Q49. How does TypeScript handle JSX?

TypeScript supports JSX through special file extensions and compiler options, providing type checking for React components - TypeScript supports React hooks with proper typing. TypeScript understands JSX syntax.

- **Trade-offs**: The catch is TypeScript provides types for React events - interface-based prop typing for component props. TypeScript supports React hooks with proper typing, but watch out - provides type checking for React components.

Example:

```typescript
{
  "compilerOptions": {
    "jsx": "react-jsx", // or "react" for older versions
    "jsxImportSource": "react"
  }
}
```

---

## Q50. What are compiler flags and how do you use them?

Common flags include `noImplicitAny` for explicit any types, `strict` for strict type checking, and `noUnusedLocals` for unused variable detection - helps maintain clean, type-safe code (code quality). Strict mode enables comprehensive type checking.

- **Trade-offs**: The catch is detects unused variables and parameters (unused code) - makes optional properties more precise (exact types). Helps maintain clean, type-safe code (code quality), but watch out - prevents accidental any types (implicit any).

Example:

```typescript
{
  "compilerOptions": {
    "strict": true,
    "noImplicitAny": true,
    "noImplicitReturns": true
  }
}
```

---

## Q51. What are generics with default types?

TypeScript allows generic parameters to have default types, providing fallback types when no type argument is specified - common for libraries and frameworks (use cases). Provide fallback types for generics (default types).

- **Trade-offs**: The catch is TypeScript can infer types when defaults are used (type inference) - defaults help with API evolution (backward compatibility). Common for libraries and frameworks (use cases), but watch out - allow generic usage without explicit type arguments (flexibility).

Example:

```typescript
interface ApiResponse<T = any> {
  data: T;
  status: number;
  message: string;
}
```

---

## Q52. What is covariance and contravariance?

Covariance preserves the subtype relationship in the same direction, while contravariance reverses it, affecting function parameter and return types - variance affects function parameter and return types. Covariance preserves subtype relationship in same direction, contravariance reverses it.

- **Trade-offs**: The catch is variance rules ensure type safety - understanding variance helps with complex generic types. Variance affects function parameter and return types, but watch out - function parameters are contravariant, returns are covariant.

Example:

```typescript
class Animal { name: string; }
class Dog extends Animal { breed: string; }

function getAnimal(): Animal { return new Dog(); }
```

---

## Q53. What are the performance considerations when using TypeScript?

Performance considerations include compilation time, bundle size, type checking overhead, and the balance between type safety and development speed - avoid overly complex types in performance-critical code. Use incremental compilation and build caching (compilation time).

- **Trade-offs**: The catch is can be disabled for faster development builds (type checking) - only recompile changed files (incremental builds). Avoid overly complex types in performance-critical code, but watch out - TypeScript types are stripped at compile time (bundle size).

Example:

```typescript
{
  "compilerOptions": {
    "incremental": true,
    "tsBuildInfoFile": ".tsbuildinfo",
    "skipLibCheck": true
  }
}
```

---
