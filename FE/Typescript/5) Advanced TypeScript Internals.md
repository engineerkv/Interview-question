# 🧠 5. Advanced TypeScript Internals (Q40–53)

---

## 40) What is module resolution (classic vs node strategy)?

Concept:
Module resolution determines how TypeScript finds and loads modules, with classic strategy for legacy code and node strategy for modern Node.js.

Example:
```typescript
// tsconfig.json
{
  "compilerOptions": {
    "moduleResolution": "node",
    "baseUrl": "./src",
    "paths": { "@/*": ["src/*"] }
  }
}
```

Deep Insight:
- **Classic Strategy**: Legacy resolution, looks for .ts files first
- **Node Strategy**: Modern resolution, follows Node.js module resolution
- **Path Mapping**: Use baseUrl and paths for custom module resolution
- **File Extensions**: Node strategy handles .js, .ts, .d.ts files
- **Directory Resolution**: Node strategy supports index files and directory imports

---

## 41) How does the internal classic module resolution strategy work?

Concept:
Classic module resolution looks for TypeScript files first, then checks for declaration files, following a simple file extension priority order.

Example:
```typescript
// Import resolution order in classic strategy
import { utils } from './utils'; // Looks for:
// 1. ./utils.ts
// 2. ./utils.d.ts
// 3. ./utils/index.ts
// 4. ./utils/index.d.ts
```

Deep Insight:
- **File Priority**: .ts files take precedence over .d.ts files
- **Extension Order**: Checks .ts, then .d.ts, then index files
- **No Node Modules**: Doesn't look in node_modules directory
- **Legacy Support**: Designed for older TypeScript projects
- **Simple Logic**: Straightforward file extension matching

---

## 42) How does the internal node module resolution strategy work?

Concept:
Node module resolution follows Node.js algorithm, checking node_modules, package.json, and supporting directory imports with index files.

Example:
```typescript
// Import resolution order in node strategy
import { lodash } from 'lodash'; // Looks for:
// 1. ./node_modules/lodash/package.json (main field)
// 2. ./node_modules/lodash/index.js
// 3. ./node_modules/lodash/index.d.ts
// 4. ./node_modules/@types/lodash/index.d.ts
```

Deep Insight:
- **Node Modules**: Searches node_modules directory hierarchy
- **Package.json**: Uses main field to find entry point
- **Type Definitions**: Checks @types packages for type definitions
- **Directory Imports**: Supports importing directories with index files
- **Modern Standard**: Follows Node.js module resolution algorithm

---

## 43) What is the purpose of declaration files (`.d.ts`) and how are they generated?

Concept:
Declaration files provide type information for JavaScript libraries, generated automatically or written manually for type safety.

Example:
```typescript
// my-library.d.ts (manually written)
declare module "my-library" {
  export interface Config {
    apiKey: string;
    timeout?: number;
  }
```

Deep Insight:
- **Type Information**: Provide type definitions for JavaScript libraries
- **Auto-Generation**: TypeScript can generate .d.ts files from .ts files
- **Manual Creation**: Write .d.ts files for external libraries
- **Module Declaration**: Use declare module for external modules
- **Type Safety**: Enable type checking for JavaScript code

---

## 44) What is the difference between ambient modules and normal modules?

Concept:
Ambient modules declare types for existing JavaScript code, while normal modules are TypeScript modules with implementation.

Example:
```typescript
// Ambient module declaration (no implementation)
declare module "lodash" {
  export function chunk<T>(array: T[], size: number): T[][];
  export function debounce<T extends (...args: any[]) => any>(
    func: T, wait: number): T;
}
```

Deep Insight:
- **Ambient Modules**: Type declarations without implementation
- **Normal Modules**: TypeScript modules with actual implementation
- **External Libraries**: Use ambient modules for JavaScript libraries
- **Type Safety**: Ambient modules provide type safety for external code
- **No Runtime**: Ambient modules don't affect runtime behavior

---

## 45) What is the purpose of `declare` keyword?

Concept:
`declare` tells TypeScript that a variable, function, or module exists elsewhere, providing type information without implementation.

Example:
```typescript
// Declare global variables
declare const process: {
  env: {
    NODE_ENV: string;
    API_URL: string;
  };
```

Deep Insight:
- **Type Information**: Provide types without implementation
- **Global Variables**: Declare global variables and their types
- **Module Types**: Declare types for external modules
- **Namespace Declaration**: Declare global namespaces
- **No Runtime Impact**: Declare statements don't generate JavaScript code

---

## 46) What are namespaces, and how do they differ from ES modules?

Concept:
Namespaces provide logical grouping of code and can be split across files, while ES modules are the modern standard for module systems.

Example:
```typescript
// Namespace declaration
namespace MathUtils {
  export function add(a: number, b: number): number {
    return a + b;
  }
}

// ES module
export function multiply(a: number, b: number): number {
  return a * b;
}
```

Deep Insight:
- **Logical Grouping**: Namespaces group related code together
- **Split Files**: Namespaces can be split across multiple files
- **ES Modules**: Modern standard for module system
- **Tree Shaking**: ES modules support tree shaking
- **Use Cases**: Namespaces for legacy code, ES modules for new projects

---

## 47) What is strict mode, and what does `strictNullChecks` enforce?

Concept:
Strict mode enables additional type checking options, with `strictNullChecks` preventing null and undefined from being assigned to non-nullable types.

Example:
```typescript
// tsconfig.json
{
  "compilerOptions": {
    "strict": true,
    "strictNullChecks": true,
    "strictFunctionTypes": true
  }
}
```

Deep Insight:
- **Strict Mode**: Enables additional type checking options
- **Null Safety**: strictNullChecks prevents null/undefined errors
- **Type Safety**: More rigorous type checking
- **Development**: Helps catch errors during development
- **Production**: Reduces runtime errors in production

---

## 48) What is the difference between compile-time and runtime type checking?

Concept:
Compile-time checking happens during TypeScript compilation, while runtime checking happens during JavaScript execution.

Example:
```typescript
// Compile-time type checking
function processData(data: string): number {
  return data.length; // TypeScript checks types at compile time
}

// Runtime type checking (manual)
function isString(value: any): value is string {
  return typeof value === "string";
}
```

Deep Insight:
- **Compile Time**: TypeScript checks types during compilation
- **Runtime**: JavaScript has no built-in type checking
- **Type Guards**: Use runtime checks to narrow types
- **Performance**: Compile-time checking has no runtime cost
- **Safety**: Combine both for maximum type safety

---

## 49) How does TypeScript handle JSX in React applications?

Concept:
TypeScript supports JSX through special file extensions and compiler options, providing type checking for React components.

Example:
```typescript
// tsconfig.json
{
  "compilerOptions": {
    "jsx": "react-jsx", // or "react" for older versions
    "jsxImportSource": "react"
  }
```

Deep Insight:
- **JSX Support**: TypeScript understands JSX syntax
- **Type Checking**: Provides type checking for React components
- **Event Types**: TypeScript provides types for React events
- **Component Props**: Interface-based prop typing
- **Hooks**: TypeScript supports React hooks with proper typing

---

## 50) What are some commonly used compiler flags for type safety (`noImplicitAny`, `strict`, `noUnusedLocals`, etc.)?

Concept:
Common flags include `noImplicitAny` for explicit any types, `strict` for strict type checking, and `noUnusedLocals` for unused variable detection.

Example:
```typescript
// tsconfig.json
{
  "compilerOptions": {
    "strict": true,
    "noImplicitAny": true,
    "noImplicitReturns": true
  }
}
```

Deep Insight:
- **Strict Mode**: Enables comprehensive type checking
- **Implicit Any**: Prevents accidental any types
- **Unused Code**: Detects unused variables and parameters
- **Exact Types**: Makes optional properties more precise
- **Code Quality**: Helps maintain clean, type-safe code

---

## 51) How does TypeScript handle generics with default types?

Concept:
TypeScript allows generic parameters to have default types, providing fallback types when no type argument is specified.

Example:
```typescript
// Generic with default type
interface ApiResponse<T = any> {
  data: T;
  status: number;
  message: string;
}
```

Deep Insight:
- **Default Types**: Provide fallback types for generics
- **Flexibility**: Allow generic usage without explicit type arguments
- **Type Inference**: TypeScript can infer types when defaults are used
- **Backward Compatibility**: Defaults help with API evolution
- **Use Cases**: Common for libraries and frameworks

---

## 52) What is covariance and contravariance in the type system?

Concept:
Covariance preserves the subtype relationship in the same direction, while contravariance reverses it, affecting function parameter and return types.

Example:
```typescript
// Covariance - return types
class Animal { name: string; }
class Dog extends Animal { breed: string; }

// Covariant return type
function getAnimal(): Animal { return new Dog(); }
```

Deep Insight:
- **Covariance**: Subtype relationship preserved in same direction
- **Contravariance**: Subtype relationship reversed
- **Function Types**: Parameters are contravariant, returns are covariant
- **Type Safety**: Variance rules ensure type safety
- **Complex Types**: Understanding variance helps with complex generic types

---

## 53) What are performance considerations of using TypeScript in large-scale projects?

Concept:
Performance considerations include compilation time, bundle size, type checking overhead, and the balance between type safety and development speed.

Example:
```typescript
// tsconfig.json - Performance optimizations
{
  "compilerOptions": {
    "incremental": true,
    "tsBuildInfoFile": ".tsbuildinfo",
    "skipLibCheck": true
  }
}
```

Deep Insight:
- **Compilation Time**: Use incremental compilation and build caching
- **Bundle Size**: TypeScript types are stripped at compile time
- **Type Checking**: Can be disabled for faster development builds
- **Incremental Builds**: Only recompile changed files
- **Complex Types**: Avoid overly complex types in performance-critical code

---
