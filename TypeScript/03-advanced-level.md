# 🧩 TypeScript Interview Notes (2025 Edition)

## 🔵 Section 3 — Advanced Level (Type System Deep Dive) — Q41-Q60

---

### 41. 🔵 What is the `never` type, and when is it used?

**🧠 Concept**

The `never` type represents values that never occur, used for functions that never return or impossible code paths.

**💻 Example**

```typescript
// Function that never returns
function throwError(message: string): never {
  throw new Error(message);
}

// Exhaustive switch
function handleStatus(status: "loading" | "success" | "error"): string {
  switch (status) {
    case "loading":
      return "Please wait...";
    case "success":
      return "Done!";
    case "error":
      return "Something went wrong";
    default:
      const _exhaustive: never = status; // Ensures all cases handled
      return _exhaustive;
  }
}
```

**💬 Explanation + Insight**

- **Impossible Values** - Represents values that can never exist
- **Exhaustive Checking** - Ensures all cases are handled in switches
- **Type Safety** - Prevents impossible code paths
- **Use Cases** - Error throwing, exhaustive switches, type guards
- **Compile-time** - Helps catch logic errors at compile time

---

### 42. 🔵 What is the difference between `unknown` and `any`?

**🧠 Concept**

`unknown` is type-safe and requires type checking before use, while `any` disables type checking entirely.

**💻 Example**

```typescript
// any - disables type checking
let data: any = "hello";
data.foo.bar.baz; // No error, but runtime error possible

// unknown - requires type checking
let data: unknown = "hello";
// data.toUpperCase(); // Error - must check type first

if (typeof data === "string") {
  data.toUpperCase(); // OK - type is narrowed to string
}

// Type guard for unknown
function isString(value: unknown): value is string {
  return typeof value === "string";
}
```

**💬 Explanation + Insight**

- **Type Safety** - `unknown` maintains type safety, `any` disables it
- **Type Checking** - `unknown` requires explicit type checking
- **Runtime Safety** - `unknown` prevents runtime errors
- **Best Practice** - Use `unknown` instead of `any` when possible
- **Use Cases** - External APIs, user input, dynamic data

---

### 43. 🔵 What are conditional types (`T extends U ? X : Y`)?

**🧠 Concept**

Conditional types allow types to be selected based on conditions, enabling powerful type transformations and utility types.

**💻 Example**

```typescript
// Basic conditional type
type IsString<T> = T extends string ? true : false;

type Test1 = IsString<string>; // true
type Test2 = IsString<number>; // false

// More complex example
type NonNullable<T> = T extends null | undefined ? never : T;

type ApiResponse<T> = T extends string 
  ? { message: T }
  : { data: T };

type StringResponse = ApiResponse<string>; // { message: string }
type DataResponse = ApiResponse<User>; // { data: User }
```

**💬 Explanation + Insight**

- **Type Conditions** - Select types based on conditions
- **Powerful Transformations** - Enable complex type manipulations
- **Utility Types** - Foundation for many built-in utility types
- **Type Safety** - Maintain type safety during transformations
- **Use Cases** - API responses, configuration objects, type guards

---

### 44. 🔵 What are infer types (`infer U`) in conditional types?

**🧠 Concept**

`infer` allows extracting types from other types within conditional types, enabling powerful type introspection.

**💻 Example**

```typescript
// Extract return type
type ReturnType<T> = T extends (...args: any[]) => infer R ? R : never;

// Extract array element type
type ArrayElement<T> = T extends (infer U)[] ? U : never;

// Extract promise type
type Awaited<T> = T extends Promise<infer U> ? U : T;

// Usage
type Func = () => string;
type Return = ReturnType<Func>; // string

type Numbers = number[];
type Element = ArrayElement<Numbers>; // number
```

**💬 Explanation + Insight**

- **Type Extraction** - Extract types from other types
- **Introspection** - Inspect the structure of types
- **Powerful Patterns** - Enable advanced type manipulations
- **Utility Types** - Foundation for many utility type implementations
- **Use Cases** - Function types, array types, promise types

---

### 45. 🔵 What are template literal types, and when are they useful?

**🧠 Concept**

Template literal types allow string literal types to be manipulated and combined, enabling type-safe string operations.

**💻 Example**

```typescript
// Basic template literal
type Greeting = `Hello, ${string}`;
let greeting: Greeting = "Hello, World"; // OK
// let invalid: Greeting = "Hi there"; // Error

// More complex example
type EventName<T extends string> = `on${Capitalize<T>}`;
type ClickEvent = EventName<"click">; // "onClick"
type HoverEvent = EventName<"hover">; // "onHover"

// CSS property names
type CSSProperty = `--${string}`;
let cssVar: CSSProperty = "--primary-color"; // OK
```

**💬 Explanation + Insight**

- **String Manipulation** - Manipulate string literal types
- **Type Safety** - Ensure string patterns are correct
- **IntelliSense** - Provide autocomplete for string patterns
- **Use Cases** - Event names, CSS properties, API endpoints
- **Advanced Patterns** - Combine with other type features

---

### 46. 🔵 What are recursive types, and how can they be used?

**🧠 Concept**

Recursive types reference themselves in their definition, enabling complex data structures like trees and nested objects.

**💻 Example**

```typescript
// Recursive type for tree structure
type TreeNode<T> = {
  value: T;
  children: TreeNode<T>[];
};

// Recursive type for nested objects
type NestedObject = {
  [key: string]: NestedObject | string | number;
};

// Recursive utility type
type DeepPartial<T> = {
  [P in keyof T]?: T[P] extends object ? DeepPartial<T[P]> : T[P];
};

// Usage
let tree: TreeNode<string> = {
  value: "root",
  children: [
    { value: "child1", children: [] },
    { value: "child2", children: [] }
  ]
};
```

**💬 Explanation + Insight**

- **Self-reference** - Types that reference themselves
- **Complex Structures** - Enable tree-like and nested structures
- **Type Safety** - Maintain type safety in recursive structures
- **Use Cases** - Tree structures, nested configurations, deep transformations
- **Performance** - Be mindful of deeply nested recursive types

---

### 47. 🔵 How do you define and use user-defined type guards (`arg is Type`)?

**🧠 Concept**

User-defined type guards are functions that return type predicates, allowing custom type narrowing logic.

**💻 Example**

```typescript
// Type guard function
function isString(value: unknown): value is string {
  return typeof value === "string";
}

function isUser(value: unknown): value is User {
  return (
    typeof value === "object" &&
    value !== null &&
    "id" in value &&
    "name" in value
  );
}

// Usage
function processValue(value: unknown) {
  if (isString(value)) {
    // TypeScript knows value is string
    console.log(value.toUpperCase());
  }
  
  if (isUser(value)) {
    // TypeScript knows value is User
    console.log(value.name);
  }
}
```

**💬 Explanation + Insight**

- **Type Predicates** - Return type predicates for type narrowing
- **Custom Logic** - Define custom type checking logic
- **Type Safety** - Provide type safety for complex type checks
- **Reusability** - Create reusable type guard functions
- **Use Cases** - API responses, form validation, data parsing

---

### 48. 🔵 What is covariance and contravariance in TypeScript?

**🧠 Concept**

Covariance and contravariance describe how type relationships are preserved or reversed in function parameters and return types.

**💻 Example**

```typescript
// Covariance - return types
interface Animal {
  name: string;
}

interface Dog extends Animal {
  breed: string;
}

// Covariant return type
function getAnimal(): Animal {
  return { name: "Generic Animal" };
}

function getDog(): Dog {
  return { name: "Buddy", breed: "Golden Retriever" };
}

// Contravariance - parameter types
function processAnimal(animal: Animal): void {
  console.log(animal.name);
}

function processDog(dog: Dog): void {
  console.log(dog.name, dog.breed);
}

// Covariant assignment
let animalFunc: () => Animal = getDog; // OK

// Contravariant assignment
let dogProcessor: (dog: Dog) => void = processAnimal; // OK
```

**💬 Explanation + Insight**

- **Covariance** - Type relationships preserved in same direction
- **Contravariance** - Type relationships reversed
- **Function Types** - Parameters are contravariant, returns are covariant
- **Type Safety** - Ensures type safety in function assignments
- **Use Cases** - Function type compatibility, generic constraints

---

### 49. 🔵 What is the difference between structural and nominal typing?

**🧠 Concept**

Structural typing checks if types have compatible structure, while nominal typing checks if types have the same name.

**💻 Example**

```typescript
// Structural typing (TypeScript's approach)
interface Point {
  x: number;
  y: number;
}

interface NamedPoint {
  x: number;
  y: number;
  name: string;
}

let point: Point = { x: 1, y: 2 };
let namedPoint: NamedPoint = { x: 1, y: 2, name: "origin" };

point = namedPoint; // OK - structural typing

// Nominal typing simulation
class UserId {
  constructor(public value: string) {}
}

class ProductId {
  constructor(public value: string) {}
}

let userId = new UserId("123");
let productId = new ProductId("123");
// userId = productId; // Error - different types
```

**💬 Explanation + Insight**

- **Structural** - TypeScript uses structural typing by default
- **Nominal** - Can simulate nominal typing with classes
- **Flexibility** - Structural typing provides more flexibility
- **Type Safety** - Both approaches provide type safety
- **Use Cases** - Structural for flexibility, nominal for strict identity

---

### 50. 🔵 What are intersection vs union types in practical terms?

**🧠 Concept**

Intersection types combine all properties from multiple types, while union types allow a value to be one of several types.

**💻 Example**

```typescript
// Intersection type
interface Person {
  name: string;
  age: number;
}

interface Employee {
  id: number;
  department: string;
}

type PersonEmployee = Person & Employee;
// Must have all properties from both types

// Union type
type Status = "pending" | "approved" | "rejected";
// Can be any one of the three values

// Practical usage
function processUser(user: PersonEmployee): void {
  // Has access to all properties from both interfaces
  console.log(user.name, user.id);
}

function handleStatus(status: Status): void {
  switch (status) {
    case "pending":
      console.log("Please wait...");
      break;
    case "approved":
      console.log("Approved!");
      break;
    case "rejected":
      console.log("Rejected!");
      break;
  }
}
```

**💬 Explanation + Insight**

- **Intersection** - Combines all properties from multiple types
- **Union** - Allows value to be one of several types
- **Use Cases** - Intersection for combining types, union for alternatives
- **Type Safety** - Both provide type safety in different ways
- **Pattern Matching** - Union types enable pattern matching

---

### 51. 🔵 How do you make a deep partial or deep readonly type using recursion?

**🧠 Concept**

Deep utility types use recursion to transform nested object properties, providing powerful type transformations.

**💻 Example**

```typescript
// Deep partial type
type DeepPartial<T> = {
  [P in keyof T]?: T[P] extends object ? DeepPartial<T[P]> : T[P];
};

// Deep readonly type
type DeepReadonly<T> = {
  readonly [P in keyof T]: T[P] extends object ? DeepReadonly<T[P]> : T[P];
};

// Usage
interface User {
  id: number;
  name: string;
  address: {
    street: string;
    city: string;
    country: {
      code: string;
      name: string;
    };
  };
}

type PartialUser = DeepPartial<User>;
// All properties are optional, including nested ones

type ReadonlyUser = DeepReadonly<User>;
// All properties are readonly, including nested ones
```

**💬 Explanation + Insight**

- **Recursion** - Use recursion to transform nested properties
- **Type Safety** - Maintain type safety during deep transformations
- **Flexibility** - Provide powerful type manipulation capabilities
- **Use Cases** - Form data, configuration objects, API updates
- **Performance** - Be mindful of deeply nested recursive types

---

### 52. 🔵 What are `Exclude`, `Extract`, `NonNullable`, and `Record` utility types?

**🧠 Concept**

These utility types provide common type transformations for filtering, extracting, and creating object types.

**💻 Example**

```typescript
// Exclude - remove types from union
type AllColors = "red" | "green" | "blue" | "yellow";
type PrimaryColors = Exclude<AllColors, "yellow">; // "red" | "green" | "blue"

// Extract - extract types from union
type Colors = "red" | "green" | "blue" | "yellow";
type WarmColors = Extract<Colors, "red" | "yellow">; // "red" | "yellow"

// NonNullable - remove null and undefined
type MaybeString = string | null | undefined;
type String = NonNullable<MaybeString>; // string

// Record - create object type with specific keys and values
type ColorMap = Record<"red" | "green" | "blue", string>;
// { red: string; green: string; blue: string; }
```

**💬 Explanation + Insight**

- **Exclude** - Remove specific types from union
- **Extract** - Extract specific types from union
- **NonNullable** - Remove null and undefined from type
- **Record** - Create object type with specific keys and values
- **Use Cases** - API filtering, configuration objects, type transformations

---

### 53. 🔵 How do you create strongly typed React props or Redux stores with TypeScript?

**🧠 Concept**

TypeScript provides powerful type safety for React components and Redux stores through proper type definitions.

**💻 Example**

```typescript
// React component props
interface ButtonProps {
  label: string;
  onClick: () => void;
  disabled?: boolean;
  variant?: "primary" | "secondary";
}

function Button({ label, onClick, disabled = false, variant = "primary" }: ButtonProps) {
  return (
    <button 
      onClick={onClick} 
      disabled={disabled}
      className={`btn btn-${variant}`}
    >
      {label}
    </button>
  );
}

// Redux store
interface RootState {
  user: {
    id: number;
    name: string;
    email: string;
  };
  posts: Post[];
}

// Redux action
interface SetUserAction {
  type: "SET_USER";
  payload: User;
}
```

**💬 Explanation + Insight**

- **Props Typing** - Type React component props for better IntelliSense
- **State Typing** - Type Redux store state for type safety
- **Action Typing** - Type Redux actions for consistency
- **Type Safety** - Catch errors at compile time
- **Use Cases** - Component libraries, state management, API integration

---

### 54. 🔵 What is a declaration file (`.d.ts`), and how is it used?

**🧠 Concept**

Declaration files provide type information for JavaScript libraries, enabling TypeScript to understand external code.

**💻 Example**

```typescript
// my-library.d.ts
declare module "my-library" {
  export interface Config {
    apiKey: string;
    baseUrl: string;
  }
  
  export function initialize(config: Config): void;
  export function getData(): Promise<any>;
}

// Usage
import { initialize, getData } from "my-library";
initialize({ apiKey: "123", baseUrl: "https://api.example.com" });
```

**💬 Explanation + Insight**

- **Type Information** - Provide types for JavaScript libraries
- **No Implementation** - Only type information, no runtime code
- **Integration** - Enable TypeScript support for external libraries
- **Type Safety** - Provide type safety for external code
- **Use Cases** - Third-party libraries, legacy code, external APIs

---

### 55. 🔵 How do you write a custom declaration file for a JS library without types?

**🧠 Concept**

Custom declaration files define types for JavaScript libraries that don't have built-in TypeScript support.

**💻 Example**

```typescript
// jquery.d.ts
declare namespace $ {
  function ajax(settings: {
    url: string;
    method?: string;
    data?: any;
    success?: (data: any) => void;
    error?: (error: any) => void;
  }): void;
  
  function ready(callback: () => void): void;
}

// Usage
$.ready(() => {
  $.ajax({
    url: "/api/data",
    success: (data) => console.log(data)
  });
});
```

**💬 Explanation + Insight**

- **Custom Types** - Define types for libraries without TypeScript support
- **Namespace Declarations** - Use namespaces for global objects
- **Function Declarations** - Define function signatures
- **Type Safety** - Provide type safety for external libraries
- **Use Cases** - Legacy libraries, global objects, external APIs

---

### 56. 🔵 What is the `declare global` syntax, and when is it used?

**🧠 Concept**

`declare global` extends the global scope with new types, enabling TypeScript to understand global variables and functions.

**💻 Example**

```typescript
// Extend global scope
declare global {
  interface Window {
    myCustomProperty: string;
    myCustomFunction: () => void;
  }
  
  var globalVariable: string;
}

// Usage
window.myCustomProperty = "Hello";
window.myCustomFunction();
console.log(globalVariable);
```

**💬 Explanation + Insight**

- **Global Extension** - Extend global scope with new types
- **Window Object** - Add properties to window object
- **Global Variables** - Define global variables and functions
- **Type Safety** - Provide type safety for global code
- **Use Cases** - Browser APIs, global utilities, third-party scripts

---

### 57. 🔵 What is type compatibility, and how does TypeScript check it?

**🧠 Concept**

Type compatibility determines when one type can be assigned to another, based on structural typing and type relationships.

**💻 Example**

```typescript
// Structural compatibility
interface Point {
  x: number;
  y: number;
}

interface NamedPoint {
  x: number;
  y: number;
  name: string;
}

let point: Point = { x: 1, y: 2 };
let namedPoint: NamedPoint = { x: 1, y: 2, name: "origin" };

point = namedPoint; // OK - structural compatibility
// namedPoint = point; // Error - missing 'name' property

// Function compatibility
type Handler = (event: Event) => void;
type SpecificHandler = (event: MouseEvent) => void;

let handler: Handler = (event: Event) => console.log(event);
let specificHandler: SpecificHandler = (event: MouseEvent) => console.log(event);

handler = specificHandler; // OK - contravariant parameters
// specificHandler = handler; // Error - incompatible parameter types
```

**💬 Explanation + Insight**

- **Structural Typing** - Types are compatible if they have compatible structure
- **Property Compatibility** - All required properties must be present
- **Function Compatibility** - Parameters are contravariant, returns are covariant
- **Type Safety** - Ensures type safety during assignments
- **Use Cases** - API integration, function assignments, object assignments

---

### 58. 🔵 How do you handle ambient modules and external libraries?

**🧠 Concept**

Ambient modules provide type information for external libraries, enabling TypeScript to understand and type-check external code.

**💻 Example**

```typescript
// Ambient module declaration
declare module "lodash" {
  export function chunk<T>(array: T[], size: number): T[][];
  export function debounce<T extends (...args: any[]) => any>(
    func: T,
    wait: number
  ): T;
}

// Usage
import { chunk, debounce } from "lodash";
const chunks = chunk([1, 2, 3, 4], 2);
const debouncedFn = debounce(() => console.log("Hello"), 1000);
```

**💬 Explanation + Insight**

- **External Libraries** - Provide types for external JavaScript libraries
- **Module Declarations** - Use `declare module` for external modules
- **Type Safety** - Provide type safety for external code
- **Integration** - Enable TypeScript support for external libraries
- **Use Cases** - Third-party libraries, npm packages, external APIs

---

### 59. 🔵 What are decorators in TypeScript, and what must be enabled to use them?

**🧠 Concept**

Decorators are experimental features that allow metadata to be added to classes, methods, and properties.

**💻 Example**

```typescript
// Enable decorators in tsconfig.json
// {
//   "compilerOptions": {
//     "experimentalDecorators": true,
//     "emitDecoratorMetadata": true
//   }
// }

function log(target: any, propertyName: string, descriptor: PropertyDescriptor) {
  const method = descriptor.value;
  descriptor.value = function (...args: any[]) {
    console.log(`Calling ${propertyName} with args:`, args);
    return method.apply(this, args);
  };
}

class Calculator {
  @log
  add(a: number, b: number): number {
    return a + b;
  }
}
```

**💬 Explanation + Insight**

- **Experimental Feature** - Requires enabling in tsconfig.json
- **Metadata** - Add metadata to classes, methods, and properties
- **Decorator Functions** - Functions that modify target behavior
- **Use Cases** - Logging, validation, dependency injection
- **Configuration** - Must enable experimentalDecorators and emitDecoratorMetadata

---

### 60. 🔵 How does the experimental `emitDecoratorMetadata` option work?

**🧠 Concept**

`emitDecoratorMetadata` enables runtime metadata for decorators, allowing decorators to access type information at runtime.

**💻 Example**

```typescript
// tsconfig.json
// {
//   "compilerOptions": {
//     "experimentalDecorators": true,
//     "emitDecoratorMetadata": true
//   }
// }

import "reflect-metadata";

function inject(target: any, propertyKey: string | symbol | undefined, parameterIndex: number) {
  const existingTokens = Reflect.getMetadata("design:paramtypes", target) || [];
  existingTokens[parameterIndex] = "Service";
  Reflect.defineMetadata("design:paramtypes", existingTokens, target);
}

class MyClass {
  constructor(@inject private service: any) {}
}
```

**💬 Explanation + Insight**

- **Runtime Metadata** - Enables runtime access to type information
- **Reflection** - Use Reflect API to access metadata
- **Dependency Injection** - Enable dependency injection patterns
- **Type Information** - Access type information at runtime
- **Use Cases** - Dependency injection, validation, serialization

---

*This comprehensive TypeScript advanced section covers all essential concepts including conditional types, inference, template literals, and advanced type system features for building complex applications.*