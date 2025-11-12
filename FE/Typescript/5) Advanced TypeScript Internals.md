# 🧠 5. Advanced TypeScript Internals (Q40–53)

---

## 🧩 Q40. How does module resolution work?

### 🧠 Concept

Module resolution determines how TypeScript finds and loads modules, with classic strategy for legacy code and node strategy for modern Node.js. Node strategy is the modern standard.

---

### 💡 Example

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

### 🔍 Deep Insights

* **Rule:** Classic strategy (legacy resolution, looks for .ts files first), Node strategy (modern resolution, follows Node.js module resolution).
* **Use Case:** Use baseUrl and paths for custom module resolution.
* **Common Mistake:** Node strategy handles .js, .ts, .d.ts files.
* **Pro Tip:** Node strategy supports index files and directory imports.

---

### ⭐ Senior Takeaway

Node strategy is the modern standard.

---

## 🧩 Q41. How does the internal classic module resolution strategy work?

### 🧠 Concept

Classic module resolution looks for TypeScript files first, then checks for declaration files, following a simple file extension priority order. Simple logic uses straightforward file extension matching.

---

### 💡 Example

```typescript
import { utils } from './utils'; // Looks for:
// 1. ./utils.ts
// 2. ./utils.d.ts
// 3. ./utils/index.ts
// 4. ./utils/index.d.ts
```

---

### 🔍 Deep Insights

* **Rule:** .ts files take precedence over .d.ts files.
* **Use Case:** Checks .ts, then .d.ts, then index files.
* **Common Mistake:** Doesn't look in node_modules directory.
* **Pro Tip:** Designed for older TypeScript projects.

---

### ⭐ Senior Takeaway

Simple logic uses straightforward file extension matching.

---

## 🧩 Q42. How does the internal node module resolution strategy work?

### 🧠 Concept

Node module resolution follows Node.js algorithm, checking node_modules, package.json, and supporting directory imports with index files. Follows Node.js module resolution algorithm (modern standard).

---

### 💡 Example

```typescript
import { lodash } from 'lodash'; // Looks for:
// 1. ./node_modules/lodash/package.json (main field)
// 2. ./node_modules/lodash/index.js
// 3. ./node_modules/lodash/index.d.ts
// 4. ./node_modules/@types/lodash/index.d.ts
```

---

### 🔍 Deep Insights

* **Rule:** Searches node_modules directory hierarchy.
* **Use Case:** Uses main field in package.json to find entry point.
* **Common Mistake:** Checks @types packages for type definitions.
* **Pro Tip:** Supports importing directories with index files.

---

### ⭐ Senior Takeaway

Follows Node.js module resolution algorithm (modern standard).

---

## 🧩 Q43. What are declaration files and how do you create them?

### 🧠 Concept

Declaration files provide type information for JavaScript libraries, generated automatically or written manually for type safety. Enable type checking for JavaScript code (type safety).

---

### 💡 Example

```typescript
declare module "my-library" {
  export interface Config {
    apiKey: string;
    timeout?: number;
  }
}
```

---

### 🔍 Deep Insights

* **Rule:** Provide type definitions for JavaScript libraries.
* **Use Case:** TypeScript can generate .d.ts files from .ts files (auto-generation).
* **Common Mistake:** Write .d.ts files for external libraries (manual creation).
* **Pro Tip:** Use declare module for external modules.

---

### ⭐ Senior Takeaway

Enable type checking for JavaScript code (type safety).

---

## 🧩 Q44. What are ambient modules and how do you use them?

### 🧠 Concept

Ambient modules declare types for existing JavaScript code, while normal modules are TypeScript modules with implementation. Ambient modules don't affect runtime behavior (no runtime).

---

### 💡 Example

```typescript
declare module "lodash" {
  export function chunk<T>(array: T[], size: number): T[][];
  export function debounce<T extends (...args: any[]) => any>(
    func: T, wait: number): T;
}
```

---

### 🔍 Deep Insights

* **Rule:** Ambient modules are type declarations without implementation.
* **Use Case:** Normal modules are TypeScript modules with actual implementation.
* **Common Mistake:** Use ambient modules for JavaScript libraries (external libraries).
* **Pro Tip:** Ambient modules provide type safety for external code.

---

### ⭐ Senior Takeaway

Ambient modules don't affect runtime behavior (no runtime).

---

## 🧩 Q45. What is the `declare` keyword and how do you use it?

### 🧠 Concept

`declare` tells TypeScript that a variable, function, or module exists elsewhere, providing type information without implementation. Declare statements don't generate JavaScript code (no runtime impact).

---

### 💡 Example

```typescript
declare const process: {
  env: {
    NODE_ENV: string;
    API_URL: string;
  };
};
```

---

### 🔍 Deep Insights

* **Rule:** Provide types without implementation (type information).
* **Use Case:** Declare global variables and their types.
* **Common Mistake:** Declare types for external modules.
* **Pro Tip:** Declare global namespaces.

---

### ⭐ Senior Takeaway

Declare statements don't generate JavaScript code (no runtime impact).

---

## 🧩 Q46. What is the difference between namespaces and ES modules?

### 🧠 Concept

Namespaces provide logical grouping of code and can be split across files, while ES modules are the modern standard for module systems. Use cases: namespaces for legacy code, ES modules for new projects.

---

### 💡 Example

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

### 🔍 Deep Insights

* **Rule:** Namespaces group related code together (logical grouping).
* **Use Case:** Namespaces can be split across multiple files.
* **Common Mistake:** ES modules are modern standard for module system.
* **Pro Tip:** ES modules support tree shaking.

---

### ⭐ Senior Takeaway

Use cases: namespaces for legacy code, ES modules for new projects.

---

## 🧩 Q47. What is strict mode and why is it important?

### 🧠 Concept

Strict mode enables additional type checking options, with `strictNullChecks` preventing null and undefined from being assigned to non-nullable types. Reduces runtime errors in production.

---

### 💡 Example

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

### 🔍 Deep Insights

* **Rule:** Enables additional type checking options.
* **Use Case:** strictNullChecks prevents null/undefined errors (null safety).
* **Common Mistake:** More rigorous type checking (type safety).
* **Pro Tip:** Helps catch errors during development.

---

### ⭐ Senior Takeaway

Reduces runtime errors in production.

---

## 🧩 Q48. What is the difference between compile-time and runtime type checking?

### 🧠 Concept

Compile-time checking happens during TypeScript compilation, while runtime checking happens during JavaScript execution. Combine both for maximum type safety.

---

### 💡 Example

```typescript
function processData(data: string): number {
  return data.length; // TypeScript checks types at compile time
}

function isString(value: any): value is string {
  return typeof value === "string";
}
```

---

### 🔍 Deep Insights

* **Rule:** TypeScript checks types during compilation (compile time).
* **Use Case:** JavaScript has no built-in type checking (runtime).
* **Common Mistake:** Use runtime checks to narrow types (type guards).
* **Pro Tip:** Compile-time checking has no runtime cost (performance).

---

### ⭐ Senior Takeaway

Combine both for maximum type safety.

---

## 🧩 Q49. How does TypeScript handle JSX?

### 🧠 Concept

TypeScript supports JSX through special file extensions and compiler options, providing type checking for React components. TypeScript supports React hooks with proper typing.

---

### 💡 Example

```typescript
{
  "compilerOptions": {
    "jsx": "react-jsx", // or "react" for older versions
    "jsxImportSource": "react"
  }
}
```

---

### 🔍 Deep Insights

* **Rule:** TypeScript understands JSX syntax.
* **Use Case:** Provides type checking for React components.
* **Common Mistake:** TypeScript provides types for React events.
* **Pro Tip:** Interface-based prop typing for component props.

---

### ⭐ Senior Takeaway

TypeScript supports React hooks with proper typing.

---

## 🧩 Q50. What are compiler flags and how do you use them?

### 🧠 Concept

Common flags include `noImplicitAny` for explicit any types, `strict` for strict type checking, and `noUnusedLocals` for unused variable detection. Helps maintain clean, type-safe code (code quality).

---

### 💡 Example

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

### 🔍 Deep Insights

* **Rule:** Strict mode enables comprehensive type checking.
* **Use Case:** Prevents accidental any types (implicit any).
* **Common Mistake:** Detects unused variables and parameters (unused code).
* **Pro Tip:** Makes optional properties more precise (exact types).

---

### ⭐ Senior Takeaway

Helps maintain clean, type-safe code (code quality).

---

## 🧩 Q51. What are generics with default types?

### 🧠 Concept

TypeScript allows generic parameters to have default types, providing fallback types when no type argument is specified. Common for libraries and frameworks (use cases).

---

### 💡 Example

```typescript
interface ApiResponse<T = any> {
  data: T;
  status: number;
  message: string;
}
```

---

### 🔍 Deep Insights

* **Rule:** Provide fallback types for generics (default types).
* **Use Case:** Allow generic usage without explicit type arguments (flexibility).
* **Common Mistake:** TypeScript can infer types when defaults are used (type inference).
* **Pro Tip:** Defaults help with API evolution (backward compatibility).

---

### ⭐ Senior Takeaway

Common for libraries and frameworks (use cases).

---

## 🧩 Q52. What is covariance and contravariance?

### 🧠 Concept

Covariance preserves the subtype relationship in the same direction, while contravariance reverses it, affecting function parameter and return types. Variance affects function parameter and return types.

---

### 💡 Example

```typescript
class Animal { name: string; }
class Dog extends Animal { breed: string; }

function getAnimal(): Animal { return new Dog(); }
```

---

### 🔍 Deep Insights

* **Rule:** Covariance preserves subtype relationship in same direction, contravariance reverses it.
* **Use Case:** Function parameters are contravariant, returns are covariant.
* **Common Mistake:** Variance rules ensure type safety.
* **Pro Tip:** Understanding variance helps with complex generic types.

---

### ⭐ Senior Takeaway

Variance affects function parameter and return types.

---

## 🧩 Q53. What are the performance considerations when using TypeScript?

### 🧠 Concept

Performance considerations include compilation time, bundle size, type checking overhead, and the balance between type safety and development speed. Avoid overly complex types in performance-critical code.

---

### 💡 Example

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

### 🔍 Deep Insights

* **Rule:** Use incremental compilation and build caching (compilation time).
* **Use Case:** TypeScript types are stripped at compile time (bundle size).
* **Common Mistake:** Can be disabled for faster development builds (type checking).
* **Pro Tip:** Only recompile changed files (incremental builds).

---

### ⭐ Senior Takeaway

Avoid overly complex types in performance-critical code.

---
