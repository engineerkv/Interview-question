# 🧠 5. Advanced TypeScript Internals (Q40–53)

---

## 40) What is module resolution (classic vs node strategy)?

Module resolution determines how TypeScript finds and loads modules, with classic strategy for legacy code and node strategy for modern Node.js.

```typescript
{
  "compilerOptions": {
    "moduleResolution": "node",
    "baseUrl": "./src",
    "paths": { "@/*": ["src/*"] }
  }
}
```

- **Core Strategies**: Classic strategy (legacy resolution, looks for .ts files first), Node strategy (modern resolution, follows Node.js module resolution)
- **Real-World Use**: Use baseUrl and paths for custom module resolution
- **Common Settings**: Node strategy handles .js, .ts, .d.ts files
- **Advanced Feature**: Node strategy supports index files and directory imports
- **Interview Tip**: Explain that node strategy is the modern standard

---

## 41) How does the internal classic module resolution strategy work?

Classic module resolution looks for TypeScript files first, then checks for declaration files, following a simple file extension priority order.

```typescript
import { utils } from './utils'; // Looks for:
// 1. ./utils.ts
// 2. ./utils.d.ts
// 3. ./utils/index.ts
// 4. ./utils/index.d.ts
```

- **Core Process**: .ts files take precedence over .d.ts files
- **Real-World Order**: Checks .ts, then .d.ts, then index files
- **Common Limitation**: Doesn't look in node_modules directory
- **Legacy Support**: Designed for older TypeScript projects
- **Interview Tip**: Explain that simple logic uses straightforward file extension matching

---

## 42) How does the internal node module resolution strategy work?

Node module resolution follows Node.js algorithm, checking node_modules, package.json, and supporting directory imports with index files.

```typescript
import { lodash } from 'lodash'; // Looks for:
// 1. ./node_modules/lodash/package.json (main field)
// 2. ./node_modules/lodash/index.js
// 3. ./node_modules/lodash/index.d.ts
// 4. ./node_modules/@types/lodash/index.d.ts
```

- **Core Process**: Searches node_modules directory hierarchy
- **Real-World Use**: Uses main field in package.json to find entry point
- **Common Feature**: Checks @types packages for type definitions
- **Advanced Feature**: Supports importing directories with index files
- **Interview Tip**: Explain that follows Node.js module resolution algorithm (modern standard)

---

## 43) What is the purpose of declaration files (`.d.ts`) and how are they generated?

Declaration files provide type information for JavaScript libraries, generated automatically or written manually for type safety.

```typescript
declare module "my-library" {
  export interface Config {
    apiKey: string;
    timeout?: number;
  }
}
```

- **Core Purpose**: Provide type definitions for JavaScript libraries
- **Real-World Use**: TypeScript can generate .d.ts files from .ts files (auto-generation)
- **Common Practice**: Write .d.ts files for external libraries (manual creation)
- **Advanced Feature**: Use declare module for external modules
- **Interview Tip**: Explain that enable type checking for JavaScript code (type safety)

---

## 44) What is the difference between ambient modules and normal modules?

Ambient modules declare types for existing JavaScript code, while normal modules are TypeScript modules with implementation.

```typescript
declare module "lodash" {
  export function chunk<T>(array: T[], size: number): T[][];
  export function debounce<T extends (...args: any[]) => any>(
    func: T, wait: number): T;
}
```

- **Core Difference**: Ambient modules are type declarations without implementation
- **Real-World Use**: Normal modules are TypeScript modules with actual implementation
- **Common Use Case**: Use ambient modules for JavaScript libraries (external libraries)
- **Advanced Feature**: Ambient modules provide type safety for external code
- **Interview Tip**: Explain that ambient modules don't affect runtime behavior (no runtime)

---

## 45) What is the purpose of `declare` keyword?

`declare` tells TypeScript that a variable, function, or module exists elsewhere, providing type information without implementation.

```typescript
declare const process: {
  env: {
    NODE_ENV: string;
    API_URL: string;
  };
};
```

- **Core Purpose**: Provide types without implementation (type information)
- **Real-World Use**: Declare global variables and their types
- **Common Use Case**: Declare types for external modules
- **Advanced Feature**: Declare global namespaces
- **Interview Tip**: Explain that declare statements don't generate JavaScript code (no runtime impact)

---

## 46) What are namespaces, and how do they differ from ES modules?

Namespaces provide logical grouping of code and can be split across files, while ES modules are the modern standard for module systems.

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

- **Core Difference**: Namespaces group related code together (logical grouping)
- **Real-World Use**: Namespaces can be split across multiple files
- **Common Advantage**: ES modules are modern standard for module system
- **Advanced Feature**: ES modules support tree shaking
- **Interview Tip**: Explain that use cases: namespaces for legacy code, ES modules for new projects

---

## 47) What is strict mode, and what does `strictNullChecks` enforce?

Strict mode enables additional type checking options, with `strictNullChecks` preventing null and undefined from being assigned to non-nullable types.

```typescript
{
  "compilerOptions": {
    "strict": true,
    "strictNullChecks": true,
    "strictFunctionTypes": true
  }
}
```

- **Core Purpose**: Enables additional type checking options
- **Real-World Impact**: strictNullChecks prevents null/undefined errors (null safety)
- **Common Advantage**: More rigorous type checking (type safety)
- **Advanced Feature**: Helps catch errors during development
- **Interview Tip**: Explain that reduces runtime errors in production

---

## 48) What is the difference between compile-time and runtime type checking?

Compile-time checking happens during TypeScript compilation, while runtime checking happens during JavaScript execution.

```typescript
function processData(data: string): number {
  return data.length; // TypeScript checks types at compile time
}

function isString(value: any): value is string {
  return typeof value === "string";
}
```

- **Core Difference**: TypeScript checks types during compilation (compile time)
- **Real-World Impact**: JavaScript has no built-in type checking (runtime)
- **Common Practice**: Use runtime checks to narrow types (type guards)
- **Advanced Feature**: Compile-time checking has no runtime cost (performance)
- **Interview Tip**: Explain that combine both for maximum type safety

---

## 49) How does TypeScript handle JSX in React applications?

TypeScript supports JSX through special file extensions and compiler options, providing type checking for React components.

```typescript
{
  "compilerOptions": {
    "jsx": "react-jsx", // or "react" for older versions
    "jsxImportSource": "react"
  }
}
```

- **Core Support**: TypeScript understands JSX syntax
- **Real-World Benefit**: Provides type checking for React components
- **Common Features**: TypeScript provides types for React events
- **Advanced Feature**: Interface-based prop typing for component props
- **Interview Tip**: Explain that TypeScript supports React hooks with proper typing

---

## 50) What are some commonly used compiler flags for type safety (`noImplicitAny`, `strict`, `noUnusedLocals`, etc.)?

Common flags include `noImplicitAny` for explicit any types, `strict` for strict type checking, and `noUnusedLocals` for unused variable detection.

```typescript
{
  "compilerOptions": {
    "strict": true,
    "noImplicitAny": true,
    "noImplicitReturns": true
  }
}
```

- **Core Flags**: Strict mode enables comprehensive type checking
- **Real-World Use**: Prevents accidental any types (implicit any)
- **Common Feature**: Detects unused variables and parameters (unused code)
- **Advanced Feature**: Makes optional properties more precise (exact types)
- **Interview Tip**: Explain that helps maintain clean, type-safe code (code quality)

---

## 51) How does TypeScript handle generics with default types?

TypeScript allows generic parameters to have default types, providing fallback types when no type argument is specified.

```typescript
interface ApiResponse<T = any> {
  data: T;
  status: number;
  message: string;
}
```

- **Core Feature**: Provide fallback types for generics (default types)
- **Real-World Use**: Allow generic usage without explicit type arguments (flexibility)
- **Common Advantage**: TypeScript can infer types when defaults are used (type inference)
- **Advanced Feature**: Defaults help with API evolution (backward compatibility)
- **Interview Tip**: Explain that common for libraries and frameworks (use cases)

---

## 52) What is covariance and contravariance in the type system?

Covariance preserves the subtype relationship in the same direction, while contravariance reverses it, affecting function parameter and return types.

```typescript
class Animal { name: string; }
class Dog extends Animal { breed: string; }

function getAnimal(): Animal { return new Dog(); }
```

- **Core Concepts**: Covariance preserves subtype relationship in same direction, contravariance reverses it
- **Real-World Impact**: Function parameters are contravariant, returns are covariant
- **Common Advantage**: Variance rules ensure type safety
- **Advanced Feature**: Understanding variance helps with complex generic types
- **Interview Tip**: Explain that variance affects function parameter and return types

---

## 53) What are performance considerations of using TypeScript in large-scale projects?

Performance considerations include compilation time, bundle size, type checking overhead, and the balance between type safety and development speed.

```typescript
{
  "compilerOptions": {
    "incremental": true,
    "tsBuildInfoFile": ".tsbuildinfo",
    "skipLibCheck": true
  }
}
```

- **Core Considerations**: Use incremental compilation and build caching (compilation time)
- **Real-World Impact**: TypeScript types are stripped at compile time (bundle size)
- **Common Practice**: Can be disabled for faster development builds (type checking)
- **Advanced Feature**: Only recompile changed files (incremental builds)
- **Interview Tip**: Explain that avoid overly complex types in performance-critical code

---
