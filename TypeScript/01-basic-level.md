# 🧩 TypeScript Interview Notes (2025 Edition)

## 🟢 Section 1 — Basic Level (Core Fundamentals) — Q1-Q20

---

### 1. 🟢 What is TypeScript, and how is it different from JavaScript?

**🧠 Concept**

TypeScript is a statically typed superset of JavaScript that compiles to plain JavaScript, adding type safety and better tooling.

**💻 Example**

```javascript
// JavaScript
function greet(name) {
  return "Hello, " + name;
}

// TypeScript
function greet(name: string): string {
  return "Hello, " + name;
}
```

**💬 Explanation + Insight**

- **Static Typing** - TypeScript adds compile-time type checking
- **Superset** - All valid JavaScript is valid TypeScript
- **Compilation** - TypeScript compiles to JavaScript
- **Tooling** - Better IDE support with autocomplete and error detection
- **Catch Errors** - Catch errors at compile time instead of runtime

---

### 2. 🟢 What are the main benefits of using TypeScript?

**🧠 Concept**

TypeScript provides type safety, better IDE support, refactoring capabilities, and helps catch errors early in development.

**💻 Example**

```typescript
interface User {
  id: number;
  name: string;
  email: string;
}

function createUser(userData: User): User {
  // TypeScript ensures userData has required properties
  return {
    id: Date.now(),
    ...userData
  };
}
```

**💬 Explanation + Insight**

- **Type Safety** - Prevents runtime type errors
- **IDE Support** - Better autocomplete and IntelliSense
- **Refactoring** - Safe refactoring with type checking
- **Documentation** - Types serve as inline documentation
- **Team Collaboration** - Better code understanding across teams

---

### 3. 🟢 What are the primitive types available in TypeScript?

**🧠 Concept**

TypeScript includes all JavaScript primitive types plus additional types like `any`, `unknown`, `never`, and `void`.

**💻 Example**

```typescript
let name: string = "John";
let age: number = 25;
let isActive: boolean = true;
let data: any = { anything: "goes" };
let unknownData: unknown = "could be anything";
let nothing: never; // Never returns
let empty: void = undefined;
```

**💬 Explanation + Insight**

- **String** - Text data with string methods
- **Number** - Numeric data (integers and floats)
- **Boolean** - True/false values
- **Any** - Disables type checking (avoid when possible)
- **Unknown** - Type-safe alternative to any
- **Never** - Represents values that never occur
- **Void** - Absence of a value (functions that don't return)

---

### 4. 🟢 How do you declare a variable in TypeScript?

**🧠 Concept**

Variables in TypeScript can be declared with explicit type annotations or rely on type inference for automatic type detection.

**💻 Example**

```typescript
// Explicit type annotation
let message: string = "Hello World";
let count: number = 42;
let isReady: boolean = false;

// Type inference
let name = "John"; // TypeScript infers string
let age = 25; // TypeScript infers number
let active = true; // TypeScript infers boolean
```

**💬 Explanation + Insight**

- **Explicit Types** - Use colon syntax for type annotations
- **Type Inference** - TypeScript automatically detects types
- **Immutability** - Use `const` for immutable values
- **Scope** - `let` and `const` have block scope
- **Best Practice** - Let TypeScript infer types when possible

---

### 5. 🟢 What is the difference between `let`, `const`, and `var` in TypeScript?

**🧠 Concept**

`let` and `const` have block scope and are preferred over `var`, which has function scope and can cause hoisting issues.

**💻 Example**

```typescript
// var - function scoped, can be redeclared
var oldWay = "function scoped";

// let - block scoped, can be reassigned
let modernWay = "block scoped";
modernWay = "can be reassigned";

// const - block scoped, cannot be reassigned
const immutable = "cannot be reassigned";
// immutable = "error"; // TypeScript error
```

**💬 Explanation + Insight**

- **var** - Function scoped, hoisted, can be redeclared
- **let** - Block scoped, not hoisted, can be reassigned
- **const** - Block scoped, not hoisted, cannot be reassigned
- **Hoisting** - var declarations are hoisted, let/const are not
- **Best Practice** - Use const by default, let when reassignment needed

---

### 6. 🟢 What is a tuple in TypeScript?

**🧠 Concept**

Tuples are arrays with a fixed number of elements where each element has a specific type, providing type safety for ordered data.

**💻 Example**

```typescript
// Tuple with fixed types
let person: [string, number, boolean] = ["John", 25, true];

// Accessing tuple elements
let name: string = person[0]; // "John"
let age: number = person[1]; // 25
let isActive: boolean = person[2]; // true

// Optional tuple elements
let coordinates: [number, number, number?] = [10, 20];
```

**💬 Explanation + Insight**

- **Fixed Length** - Tuples have a predetermined number of elements
- **Type Safety** - Each position has a specific type
- **Order Matters** - Element order is significant
- **Optional Elements** - Use `?` for optional tuple elements
- **Use Cases** - Coordinates, key-value pairs, function returns

---

### 7. 🟢 What is an enum, and when should you use it?

**🧠 Concept**

Enums define a set of named constants, making code more readable and maintainable by using meaningful names instead of magic numbers.

**💻 Example**

```typescript
// Numeric enum
enum Status {
  Pending,
  Approved,
  Rejected
}

// String enum
enum Color {
  Red = "red",
  Green = "green",
  Blue = "blue"
}

// Usage
let currentStatus: Status = Status.Pending;
let favoriteColor: Color = Color.Blue;
```

**💬 Explanation + Insight**

- **Named Constants** - Replace magic numbers with meaningful names
- **Type Safety** - Prevents invalid values
- **Autocomplete** - IDE provides autocomplete for enum values
- **Refactoring** - Easy to rename and refactor
- **Use Cases** - Status codes, configuration options, API responses

---

### 8. 🟢 What is the difference between `interface` and `type`?

**🧠 Concept**

Interfaces define object shapes and can be extended, while type aliases can represent any type and support union/intersection types.

**💻 Example**

```typescript
// Interface
interface User {
  name: string;
  age: number;
}

interface Employee extends User {
  id: number;
  department: string;
}

// Type alias
type Status = "pending" | "approved" | "rejected";
type UserWithStatus = User & { status: Status };
```

**💬 Explanation + Insight**

- **Interfaces** - Define object shapes, can be extended
- **Type Aliases** - Can represent any type, more flexible
- **Extensibility** - Interfaces can be extended and merged
- **Union Types** - Type aliases support union and intersection
- **Use Cases** - Interfaces for objects, types for unions/primitives

---

### 9. 🟢 What is the `any` type, and when should it be avoided?

**🧠 Concept**

The `any` type disables TypeScript's type checking, providing flexibility but losing type safety benefits.

**💻 Example**

```typescript
// any disables type checking
let data: any = "Hello";
data = 42; // No error
data = true; // No error
data.foo.bar.baz; // No error, but runtime error possible

// Better alternatives
let data: unknown = "Hello";
if (typeof data === "string") {
  console.log(data.toUpperCase()); // Type-safe
}
```

**💬 Explanation + Insight**

- **Type Safety** - `any` disables all type checking
- **Runtime Errors** - Can lead to runtime errors
- **Alternatives** - Use `unknown` for truly unknown data
- **Gradual Typing** - Useful for migrating JavaScript to TypeScript
- **Best Practice** - Avoid `any`, use specific types or `unknown`

---

### 10. 🟢 What is the difference between `any`, `unknown`, and `never`?

**🧠 Concept**

`any` disables type checking, `unknown` requires type checking before use, and `never` represents values that never occur.

**💻 Example**

```typescript
// any - disables type checking
let anything: any = "hello";
anything.foo.bar; // No error

// unknown - requires type checking
let something: unknown = "hello";
// something.toUpperCase(); // Error
if (typeof something === "string") {
  something.toUpperCase(); // OK
}

// never - represents impossible values
function throwError(): never {
  throw new Error("Something went wrong");
}
```

**💬 Explanation + Insight**

- **any** - Disables type checking, use sparingly
- **unknown** - Type-safe alternative to any
- **never** - Represents values that never occur
- **Type Guards** - Use type guards with unknown
- **Use Cases** - any for migration, unknown for external data, never for impossible cases

---

### 11. 🟢 What is type inference, and how does it work?

**🧠 Concept**

Type inference automatically determines types based on values, reducing the need for explicit type annotations.

**💻 Example**

```typescript
// TypeScript infers types automatically
let name = "John"; // Inferred as string
let age = 25; // Inferred as number
let isActive = true; // Inferred as boolean

// Function return type inference
function add(a: number, b: number) {
  return a + b; // Inferred return type: number
}

// Array inference
let numbers = [1, 2, 3]; // Inferred as number[]
```

**💬 Explanation + Insight**

- **Automatic Detection** - TypeScript infers types from values
- **Reduces Annotations** - Less need for explicit type annotations
- **Context Awareness** - Considers context for better inference
- **Best Practice** - Let TypeScript infer when possible
- **Explicit When Needed** - Add annotations when inference is unclear

---

### 12. 🟢 What is a union type, and how do you use it?

**🧠 Concept**

Union types allow a variable to be one of several types, providing flexibility while maintaining type safety.

**💻 Example**

```typescript
// Union type
let id: string | number = "user123";
id = 123; // Also valid

// Function with union parameter
function formatId(id: string | number): string {
  return id.toString();
}

// Union with literals
type Status = "pending" | "approved" | "rejected";
let currentStatus: Status = "pending";
```

**💬 Explanation + Insight**

- **Multiple Types** - Variable can be one of several types
- **Type Safety** - TypeScript ensures valid types
- **Type Guards** - Use type guards to narrow union types
- **Flexibility** - Provides flexibility while maintaining safety
- **Use Cases** - API responses, configuration options, state management

---

### 13. 🟢 What is an intersection type?

**🧠 Concept**

Intersection types combine multiple types into one, requiring the resulting type to have all properties from each type.

**💻 Example**

```typescript
interface Person {
  name: string;
  age: number;
}

interface Employee {
  id: number;
  department: string;
}

// Intersection type
type PersonEmployee = Person & Employee;

let person: PersonEmployee = {
  name: "John",
  age: 30,
  id: 123,
  department: "Engineering"
};
```

**💬 Explanation + Insight**

- **Combines Types** - Merges multiple types into one
- **All Properties** - Resulting type has all properties
- **Type Safety** - Ensures all required properties are present
- **Composition** - Useful for composing complex types
- **Use Cases** - Mixins, extending interfaces, combining types

---

### 14. 🟢 What is the difference between optional (`?`) and default parameters?

**🧠 Concept**

Optional parameters may or may not be provided, while default parameters have fallback values when not provided.

**💻 Example**

```typescript
// Optional parameter
function greet(name: string, age?: number): string {
  if (age) {
    return `Hello ${name}, you are ${age} years old`;
  }
  return `Hello ${name}`;
}

// Default parameter
function createUser(name: string, isActive: boolean = true): object {
  return { name, isActive };
}

// Usage
greet("John"); // OK
greet("John", 25); // OK
createUser("John"); // isActive defaults to true
```

**💬 Explanation + Insight**

- **Optional Parameters** - May or may not be provided
- **Default Parameters** - Have fallback values
- **Type Safety** - Both maintain type safety
- **Flexibility** - Provide flexibility in function calls
- **Use Cases** - Optional for truly optional data, defaults for common values

---

### 15. 🟢 What is type casting in TypeScript, and how do you perform it?

**🧠 Concept**

Type casting tells TypeScript to treat a value as a specific type, useful when you know more about a type than TypeScript can infer.

**💻 Example**

```typescript
// Type assertion (casting)
let value: unknown = "Hello World";
let strLength: number = (value as string).length;

// Alternative syntax
let strLength2: number = (<string>value).length;

// More complex example
interface ApiResponse {
  data: unknown;
}

let response: ApiResponse = { data: { name: "John", age: 25 } };
let userData = response.data as { name: string; age: number };
```

**💬 Explanation + Insight**

- **Type Assertions** - Tell TypeScript the type of a value
- **Two Syntaxes** - `as` keyword or angle bracket syntax
- **Use Carefully** - Can lead to runtime errors if incorrect
- **Type Guards** - Prefer type guards over type assertions
- **Use Cases** - Working with external APIs, DOM elements, unknown data

---

### 16. 🟢 What is `tsconfig.json`, and why is it important?

**🧠 Concept**

`tsconfig.json` configures TypeScript compiler options, project structure, and build settings for consistent compilation.

**💻 Example**

```json
{
  "compilerOptions": {
    "target": "ES2020",
    "module": "commonjs",
    "strict": true,
    "outDir": "./dist",
    "rootDir": "./src"
  },
  "include": ["src/**/*"],
  "exclude": ["node_modules", "dist"]
}
```

**💬 Explanation + Insight**

- **Compiler Configuration** - Sets TypeScript compiler options
- **Project Structure** - Defines project files and directories
- **Build Settings** - Configures output and compilation settings
- **Team Consistency** - Ensures consistent compilation across team
- **IDE Support** - Provides configuration for IDE features

---

### 17. 🟢 What are type assertions (`as` keyword), and when do you use them?

**🧠 Concept**

Type assertions tell TypeScript to treat a value as a specific type, useful when you know more about the type than TypeScript can infer.

**💻 Example**

```typescript
// Type assertion with 'as'
let element = document.getElementById("myButton") as HTMLButtonElement;
element.click(); // Now TypeScript knows it's a button

// With unknown data
let apiResponse: unknown = { name: "John", age: 25 };
let user = apiResponse as { name: string; age: number };

// Function return type assertion
function getData(): unknown {
  return { id: 1, name: "John" };
}
let data = getData() as { id: number; name: string };
```

**💬 Explanation + Insight**

- **Type Override** - Override TypeScript's type inference
- **Use When Confident** - Use when you know the actual type
- **Runtime Safety** - No runtime checking, can cause errors
- **DOM Elements** - Common use case for DOM element types
- **API Responses** - Useful for typing external API responses

---

### 18. 🟢 What is `readonly`, and how is it different from `const`?

**🧠 Concept**

`readonly` makes object properties immutable after initialization, while `const` prevents reassignment of variables.

**💻 Example**

```typescript
// const - prevents reassignment
const name = "John";
// name = "Jane"; // Error

// readonly - prevents property modification
interface User {
  readonly id: number;
  name: string;
}

let user: User = { id: 1, name: "John" };
// user.id = 2; // Error
user.name = "Jane"; // OK

// readonly arrays
let numbers: readonly number[] = [1, 2, 3];
// numbers.push(4); // Error
```

**💬 Explanation + Insight**

- **const** - Prevents variable reassignment
- **readonly** - Prevents object property modification
- **Immutability** - Both provide immutability at different levels
- **Use Cases** - const for variables, readonly for object properties
- **Type Safety** - Both provide compile-time immutability guarantees

---

### 19. 🟢 What is structural typing in TypeScript?

**🧠 Concept**

Structural typing means TypeScript checks if types have compatible structure rather than exact type names, enabling flexible type relationships.

**💻 Example**

```typescript
interface Point {
  x: number;
  y: number;
}

interface NamedPoint {
  x: number;
  y: number;
  name: string;
}

// Structural typing allows this
let point: Point = { x: 1, y: 2 };
let namedPoint: NamedPoint = { x: 1, y: 2, name: "origin" };

// NamedPoint is assignable to Point
point = namedPoint; // OK - has x and y properties
```

**💬 Explanation + Insight**

- **Structure Matters** - TypeScript checks property structure
- **Flexible Assignment** - Objects with compatible structure are assignable
- **Duck Typing** - "If it walks like a duck, it's a duck"
- **Interoperability** - Enables easy integration between libraries
- **Type Safety** - Maintains type safety while providing flexibility

---

### 20. 🟢 What are ambient declarations (`declare var`, `declare module`)?

**🧠 Concept**

Ambient declarations tell TypeScript about types that exist at runtime but aren't defined in TypeScript code, like global variables or external libraries.

**💻 Example**

```typescript
// Declare global variable
declare var process: {
  env: { [key: string]: string };
};

// Declare module
declare module "my-library" {
  export function doSomething(): void;
  export const version: string;
}

// Usage
console.log(process.env.NODE_ENV);
import { doSomething } from "my-library";
```

**💬 Explanation + Insight**

- **Global Types** - Declare types for global variables
- **External Libraries** - Add types for JavaScript libraries
- **No Implementation** - Only type information, no runtime code
- **Integration** - Essential for integrating with JavaScript libraries
- **Type Safety** - Provides type safety for external code

---

*This comprehensive TypeScript basics section covers all essential concepts including types, interfaces, enums, and type system fundamentals for building type-safe applications.*