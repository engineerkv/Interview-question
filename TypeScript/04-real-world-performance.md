# 🧩 TypeScript Interview Notes (2025 Edition)

## 🧩 Section 4 — Real-World & Performance Considerations — Q61-Q80

---

### 61. 🧩 How do you integrate TypeScript into an existing JavaScript project?

**🧠 Concept**

TypeScript integration involves gradual migration, starting with configuration, then adding types incrementally to existing JavaScript code.

**💻 Example**

```typescript
// tsconfig.json
{
  "compilerOptions": {
    "allowJs": true,
    "checkJs": false,
    "target": "ES2020",
    "module": "commonjs"
  },
  "include": ["src/**/*"],
  "exclude": ["node_modules"]
}

// Start with .js files, gradually rename to .ts
// app.js -> app.ts
function greet(name) {
  return "Hello, " + name;
}

// Add types incrementally
function greet(name: string): string {
  return "Hello, " + name;
}
```

**💬 Explanation + Insight**

- **Gradual Migration** - Start with configuration, add types incrementally
- **allowJs** - Allow JavaScript files in TypeScript project
- **Incremental Typing** - Add types to existing code gradually
- **Type Safety** - Improve type safety over time
- **Use Cases** - Legacy projects, gradual adoption, team migration

---

### 62. 🧩 What is `esModuleInterop`, and why is it important?

**🧠 Concept**

`esModuleInterop` enables interoperability between CommonJS and ES modules, allowing seamless imports from CommonJS libraries.

**💻 Example**

```typescript
// tsconfig.json
{
  "compilerOptions": {
    "esModuleInterop": true,
    "allowSyntheticDefaultImports": true
  }
}

// Before esModuleInterop
import * as React from "react";
import * as express from "express";

// After esModuleInterop
import React from "react";
import express from "express";
```

**💬 Explanation + Insight**

- **Module Interop** - Enables CommonJS/ES module interoperability
- **Default Imports** - Allows default imports from CommonJS modules
- **Synthetic Defaults** - Creates synthetic default exports
- **Compatibility** - Improves compatibility with existing libraries
- **Use Cases** - React, Express, other CommonJS libraries

---

### 63. 🧩 How do you configure strict mode, and what options does it include?

**🧠 Concept**

Strict mode enables additional type checking options that catch more potential errors, improving code quality and type safety.

**💻 Example**

```typescript
// tsconfig.json
{
  "compilerOptions": {
    "strict": true,
    // Individual strict options
    "noImplicitAny": true,
    "strictNullChecks": true,
    "strictFunctionTypes": true,
    "strictBindCallApply": true,
    "strictPropertyInitialization": true,
    "noImplicitReturns": true,
    "noFallthroughCasesInSwitch": true
  }
}
```

**💬 Explanation + Insight**

- **Strict Mode** - Enables all strict type checking options
- **Individual Options** - Can enable specific strict options
- **Type Safety** - Catches more potential errors at compile time
- **Code Quality** - Improves overall code quality
- **Use Cases** - New projects, high-quality codebases, team standards

---

### 64. 🧩 What are the pros and cons of using `noImplicitAny`?

**🧠 Concept**

`noImplicitAny` prevents implicit `any` types, forcing explicit type annotations and improving type safety.

**💻 Example**

```typescript
// With noImplicitAny: false
function processData(data) { // Implicit any
  return data.toString();
}

// With noImplicitAny: true
function processData(data: unknown): string {
  if (typeof data === "string") {
    return data;
  }
  return String(data);
}
```

**💬 Explanation + Insight**

- **Pros** - Forces explicit typing, catches type errors, improves code quality
- **Cons** - More verbose code, requires more type annotations
- **Type Safety** - Prevents accidental any types
- **Migration** - Can be challenging for existing codebases
- **Best Practice** - Enable for new projects, gradual adoption for existing

---

### 65. 🧩 How do you use `paths` and `baseUrl` in `tsconfig.json`?

**🧠 Concept**

`paths` and `baseUrl` enable module resolution with custom path mappings, improving import organization and avoiding relative paths.

**💻 Example**

```typescript
// tsconfig.json
{
  "compilerOptions": {
    "baseUrl": "./src",
    "paths": {
      "@/*": ["*"],
      "@/components/*": ["components/*"],
      "@/utils/*": ["utils/*"],
      "@/types/*": ["types/*"]
    }
  }
}

// Usage
import { Button } from "@/components/Button";
import { formatDate } from "@/utils/date";
import { User } from "@/types/user";
```

**💬 Explanation + Insight**

- **Path Mapping** - Create custom import paths
- **Base URL** - Set base directory for module resolution
- **Clean Imports** - Avoid relative path hell
- **IDE Support** - Better autocomplete and navigation
- **Use Cases** - Large projects, component libraries, utility functions

---

### 66. 🧩 How do you optimize TypeScript build performance?

**🧠 Concept**

TypeScript build performance can be optimized through configuration options, incremental compilation, and project references.

**💻 Example**

```typescript
// tsconfig.json
{
  "compilerOptions": {
    "incremental": true,
    "tsBuildInfoFile": ".tsbuildinfo",
    "skipLibCheck": true,
    "isolatedModules": true
  },
  "references": [
    { "path": "./packages/shared" },
    { "path": "./packages/ui" }
  ]
}

// Project references
// packages/shared/tsconfig.json
{
  "compilerOptions": {
    "composite": true,
    "declaration": true
  }
}
```

**💬 Explanation + Insight**

- **Incremental Compilation** - Only recompile changed files
- **Skip Lib Check** - Skip type checking of declaration files
- **Project References** - Split large projects into smaller ones
- **Build Info** - Cache build information for faster rebuilds
- **Use Cases** - Large codebases, monorepos, CI/CD pipelines

---

### 67. 🧩 What is `skipLibCheck`, and when should you use it?

**🧠 Concept**

`skipLibCheck` skips type checking of declaration files, significantly improving build performance but reducing type safety.

**💻 Example**

```typescript
// tsconfig.json
{
  "compilerOptions": {
    "skipLibCheck": true
  }
}

// With skipLibCheck: false
// TypeScript checks all .d.ts files
// Slower builds, more type safety

// With skipLibCheck: true
// TypeScript skips .d.ts files
// Faster builds, less type safety
```

**💬 Explanation + Insight**

- **Performance** - Significantly improves build performance
- **Type Safety** - Reduces type safety for external libraries
- **Use Cases** - Large projects, CI/CD, development builds
- **Trade-offs** - Balance between performance and type safety
- **Best Practice** - Use for development, disable for production builds

---

### 68. 🧩 How do you type asynchronous code (Promises, async/await)?

**🧠 Concept**

TypeScript provides strong typing for asynchronous code through Promise types, async/await, and utility types like `Awaited`.

**💻 Example**

```typescript
// Promise typing
function fetchUser(id: number): Promise<User> {
  return fetch(`/api/users/${id}`)
    .then(response => response.json());
}

// Async/await typing
async function getUser(id: number): Promise<User> {
  const response = await fetch(`/api/users/${id}`);
  return response.json();
}

// Awaited utility type
type UserPromise = Promise<User>;
type User = Awaited<UserPromise>; // User
```

**💬 Explanation + Insight**

- **Promise Types** - Type Promise return values
- **Async Functions** - Type async function return types
- **Awaited Type** - Extract resolved type from Promise
- **Error Handling** - Type error cases in async code
- **Use Cases** - API calls, database operations, file I/O

---

### 69. 🧩 How do you define types for API responses or dynamic objects?

**🧠 Concept**

API response typing involves creating interfaces for expected data structures and handling dynamic or unknown data safely.

**💻 Example**

```typescript
// API response types
interface ApiResponse<T> {
  data: T;
  status: number;
  message: string;
}

interface User {
  id: number;
  name: string;
  email: string;
}

// Usage
async function fetchUser(id: number): Promise<ApiResponse<User>> {
  const response = await fetch(`/api/users/${id}`);
  return response.json();
}

// Dynamic object typing
interface DynamicObject {
  [key: string]: unknown;
}

function processDynamicData(data: DynamicObject): void {
  if (typeof data.name === "string") {
    console.log(data.name.toUpperCase());
  }
}
```

**💬 Explanation + Insight**

- **Response Types** - Type API response structures
- **Generic Types** - Use generics for reusable response types
- **Dynamic Objects** - Handle objects with unknown structure
- **Type Guards** - Use type guards for safe property access
- **Use Cases** - REST APIs, GraphQL, external services

---

### 70. 🧩 How do you share types between frontend and backend projects?

**🧠 Concept**

Type sharing between frontend and backend involves creating shared type definitions, using monorepos, or publishing type packages.

**💻 Example**

```typescript
// shared/types.ts
export interface User {
  id: number;
  name: string;
  email: string;
  createdAt: Date;
}

export interface CreateUserRequest {
  name: string;
  email: string;
}

export interface UpdateUserRequest {
  name?: string;
  email?: string;
}

// Frontend usage
import { User, CreateUserRequest } from "@shared/types";

// Backend usage
import { User, CreateUserRequest } from "@shared/types";
```

**💬 Explanation + Insight**

- **Shared Types** - Create common type definitions
- **Monorepos** - Use monorepos for shared code
- **Type Packages** - Publish types as npm packages
- **Consistency** - Ensure type consistency across projects
- **Use Cases** - Full-stack applications, microservices, API contracts

---

### 71. 🧩 How do you integrate TypeScript with bundlers (Webpack, Vite, ESBuild)?

**🧠 Concept**

TypeScript integration with bundlers involves configuration, type checking, and ensuring proper module resolution.

**💻 Example**

```typescript
// webpack.config.js
const path = require('path');

module.exports = {
  entry: './src/index.ts',
  module: {
    rules: [
      {
        test: /\.ts$/,
        use: 'ts-loader',
        exclude: /node_modules/
      }
    ]
  },
  resolve: {
    extensions: ['.ts', '.js']
  }
};

// vite.config.ts
import { defineConfig } from 'vite';

export default defineConfig({
  plugins: [vue()],
  resolve: {
    alias: {
      '@': path.resolve(__dirname, './src')
    }
  }
});
```

**💬 Explanation + Insight**

- **Bundler Integration** - Configure bundlers for TypeScript
- **Type Checking** - Ensure type checking during build
- **Module Resolution** - Configure proper module resolution
- **Performance** - Optimize build performance
- **Use Cases** - Web applications, libraries, build pipelines

---

### 72. 🧩 How do you use TypeScript with Jest or Cypress for testing?

**🧠 Concept**

TypeScript testing involves configuring test runners, typing test utilities, and ensuring type safety in test code.

**💻 Example**

```typescript
// jest.config.js
module.exports = {
  preset: 'ts-jest',
  testEnvironment: 'node',
  roots: ['<rootDir>/src'],
  testMatch: ['**/__tests__/**/*.ts', '**/?(*.)+(spec|test).ts']
};

// test/user.test.ts
import { User } from '../src/types/user';

describe('User', () => {
  it('should create user with valid data', () => {
    const user: User = {
      id: 1,
      name: 'John Doe',
      email: 'john@example.com'
    };
    
    expect(user.name).toBe('John Doe');
  });
});
```

**💬 Explanation + Insight**

- **Test Configuration** - Configure test runners for TypeScript
- **Type Safety** - Ensure type safety in test code
- **Test Utilities** - Type test utilities and helpers
- **Mocking** - Type mocks and test doubles
- **Use Cases** - Unit testing, integration testing, E2E testing

---

### 73. 🧩 How do you use generics with React components and hooks?

**🧠 Concept**

Generic React components and hooks provide type safety and reusability across different data types.

**💻 Example**

```typescript
// Generic component
interface ListProps<T> {
  items: T[];
  renderItem: (item: T) => React.ReactNode;
}

function List<T>({ items, renderItem }: ListProps<T>) {
  return (
    <ul>
      {items.map((item, index) => (
        <li key={index}>{renderItem(item)}</li>
      ))}
    </ul>
  );
}

// Generic hook
function useApi<T>(url: string): {
  data: T | null;
  loading: boolean;
  error: string | null;
} {
  const [data, setData] = useState<T | null>(null);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState<string | null>(null);
  
  // Implementation...
  
  return { data, loading, error };
}
```

**💬 Explanation + Insight**

- **Generic Components** - Create reusable components with type safety
- **Generic Hooks** - Create reusable hooks with type safety
- **Type Inference** - TypeScript infers types from usage
- **Flexibility** - Work with different data types
- **Use Cases** - Data tables, forms, API hooks, utility components

---

### 74. 🧩 How do you create reusable form types with generics?

**🧠 Concept**

Generic form types provide type safety for form data, validation, and submission across different form structures.

**💻 Example**

```typescript
// Generic form types
interface FormField<T> {
  value: T;
  error?: string;
  touched: boolean;
}

interface FormState<T> {
  [K in keyof T]: FormField<T[K]>;
}

// Usage
interface LoginForm {
  email: string;
  password: string;
}

type LoginFormState = FormState<LoginForm>;
// {
//   email: FormField<string>;
//   password: FormField<string>;
// }

// Generic form hook
function useForm<T>(initialValues: T) {
  const [values, setValues] = useState<T>(initialValues);
  const [errors, setErrors] = useState<Partial<Record<keyof T, string>>>({});
  
  const setValue = <K extends keyof T>(field: K, value: T[K]) => {
    setValues(prev => ({ ...prev, [field]: value }));
  };
  
  return { values, errors, setValue };
}
```

**💬 Explanation + Insight**

- **Form Types** - Type form data and validation
- **Generic Forms** - Create reusable form types
- **Type Safety** - Ensure type safety in form handling
- **Validation** - Type validation errors and rules
- **Use Cases** - Dynamic forms, form libraries, validation frameworks

---

### 75. 🧩 How does TypeScript handle JSON imports and dynamic data?

**🧠 Concept**

TypeScript handles JSON imports through module declarations and dynamic data through type guards and unknown types.

**💻 Example**

```typescript
// JSON import typing
declare module "*.json" {
  const value: any;
  export default value;
}

// Usage
import config from "./config.json";
// config is typed as any

// Dynamic data handling
function processDynamicData(data: unknown): string {
  if (typeof data === "string") {
    return data.toUpperCase();
  }
  
  if (typeof data === "object" && data !== null) {
    return JSON.stringify(data);
  }
  
  return String(data);
}
```

**💬 Explanation + Insight**

- **JSON Imports** - Type JSON imports with module declarations
- **Dynamic Data** - Handle unknown data with type guards
- **Type Safety** - Ensure type safety with dynamic data
- **Runtime Safety** - Use type guards for runtime type checking
- **Use Cases** - Configuration files, API responses, user input

---

### 76. 🧩 How do you migrate a large JS codebase to TypeScript?

**🧠 Concept**

Large codebase migration involves gradual adoption, starting with configuration, then adding types incrementally.

**💻 Example**

```typescript
// Phase 1: Configuration
// tsconfig.json
{
  "compilerOptions": {
    "allowJs": true,
    "checkJs": false,
    "strict": false
  }
}

// Phase 2: Add types incrementally
// utils.js -> utils.ts
function formatDate(date) {
  return date.toISOString();
}

// Add types
function formatDate(date: Date): string {
  return date.toISOString();
}

// Phase 3: Enable strict mode
// tsconfig.json
{
  "compilerOptions": {
    "strict": true
  }
}
```

**💬 Explanation + Insight**

- **Gradual Migration** - Start with configuration, add types incrementally
- **allowJs** - Allow JavaScript files during migration
- **Incremental Typing** - Add types to existing code gradually
- **Strict Mode** - Enable strict mode after migration
- **Use Cases** - Legacy projects, team adoption, gradual improvement

---

### 77. 🧩 How do you avoid circular dependency issues in TypeScript modules?

**🧠 Concept**

Circular dependencies are avoided through proper module organization, dependency injection, and interface segregation.

**💻 Example**

```typescript
// Bad: Circular dependency
// user.ts
import { Order } from './order';
export class User {
  orders: Order[] = [];
}

// order.ts
import { User } from './user';
export class Order {
  user: User;
}

// Good: Use interfaces
// user.interface.ts
export interface IUser {
  id: number;
  name: string;
}

// order.interface.ts
export interface IOrder {
  id: number;
  userId: number;
}

// user.ts
import { IOrder } from './order.interface';
export class User implements IUser {
  id: number;
  name: string;
  orders: IOrder[] = [];
}
```

**💬 Explanation + Insight**

- **Interface Segregation** - Use interfaces to break circular dependencies
- **Dependency Injection** - Inject dependencies instead of importing
- **Module Organization** - Organize modules to avoid circular imports
- **Type Safety** - Maintain type safety without circular dependencies
- **Use Cases** - Large applications, complex domain models, shared types

---

### 78. 🧩 How does TypeScript help prevent runtime errors at scale?

**🧠 Concept**

TypeScript prevents runtime errors through compile-time type checking, catching type mismatches and undefined access.

**💻 Example**

```typescript
// TypeScript catches these errors at compile time
interface User {
  id: number;
  name: string;
  email: string;
}

function processUser(user: User): string {
  // TypeScript error: Property 'age' does not exist
  // return user.age.toString();
  
  // TypeScript error: Cannot assign string to number
  // user.id = "123";
  
  // TypeScript error: Cannot assign undefined to string
  // user.name = undefined;
  
  return user.name.toUpperCase();
}
```

**💬 Explanation + Insight**

- **Compile-time Checking** - Catch errors before runtime
- **Type Safety** - Prevent type mismatches and undefined access
- **Refactoring** - Safe refactoring with type checking
- **Documentation** - Types serve as inline documentation
- **Use Cases** - Large codebases, team development, production applications

---

### 79. 🧩 How do you use discriminated unions for exhaustive switch checks?

**🧠 Concept**

Discriminated unions enable exhaustive switch checking, ensuring all cases are handled and preventing runtime errors.

**💻 Example**

```typescript
// Discriminated union
type LoadingState = 
  | { status: "idle" }
  | { status: "loading" }
  | { status: "success"; data: any }
  | { status: "error"; error: string };

function handleState(state: LoadingState): string {
  switch (state.status) {
    case "idle":
      return "Ready to load";
    case "loading":
      return "Loading...";
    case "success":
      return `Data: ${state.data}`;
    case "error":
      return `Error: ${state.error}`;
    default:
      // TypeScript ensures this is never reached
      const _exhaustive: never = state;
      return _exhaustive;
  }
}
```

**💬 Explanation + Insight**

- **Exhaustive Checking** - Ensure all cases are handled
- **Type Safety** - Prevent runtime errors from unhandled cases
- **Never Type** - Use never type for exhaustive checking
- **Pattern Matching** - Enable type-safe pattern matching
- **Use Cases** - State management, API responses, configuration objects

---

### 80. 🧩 How do you type complex third-party libraries with missing definitions?

**🧠 Concept**

Complex third-party libraries are typed through declaration files, module augmentation, and type assertion techniques.

**💻 Example**

```typescript
// Custom declaration file
// my-library.d.ts
declare module "complex-library" {
  interface LibraryConfig {
    apiKey: string;
    baseUrl: string;
    timeout?: number;
  }
  
  class Library {
    constructor(config: LibraryConfig);
    method1(param: string): Promise<any>;
    method2(param: number): void;
  }
  
  export = Library;
}

// Module augmentation
declare module "existing-library" {
  interface ExistingInterface {
    newProperty: string;
  }
}

// Type assertion for complex objects
const complexData = (window as any).complexLibrary.getData() as {
  items: Array<{ id: number; name: string }>;
  total: number;
};
```

**💬 Explanation + Insight**

- **Declaration Files** - Create custom type definitions
- **Module Augmentation** - Extend existing library types
- **Type Assertions** - Assert types for complex objects
- **Type Safety** - Provide type safety for external libraries
- **Use Cases** - Legacy libraries, complex APIs, external services

---

*This comprehensive TypeScript real-world section covers all essential concepts including project configuration, performance optimization, testing, and practical application patterns for building production-ready applications.*