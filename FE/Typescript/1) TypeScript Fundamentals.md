# 🧠 1. TypeScript Fundamentals (Q1–9)

---

## 1) What is TypeScript, and how is it different from JavaScript?

TypeScript is a statically typed superset of JavaScript that compiles to plain JavaScript, providing type safety and better tooling support.

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

- **Core Difference**: Static typing checks types at compile time, JavaScript at runtime
- **Real-World Use**: Superset means all valid JavaScript is valid TypeScript
- **Common Mistake**: TypeScript compiles to JavaScript, not interpreted directly
- **Advanced Feature**: Better IDE support with autocomplete, refactoring, and error detection
- **Interview Tip**: Explain that you can gradually adopt TypeScript in existing JavaScript projects

---

## 2) What are the key benefits of using TypeScript in large-scale applications?

TypeScript provides type safety, better IDE support, early error detection, improved refactoring, and better documentation through types.

```typescript
interface User {
  id: number;
  name: string;
  email: string;
}

function createUser(userData: User): User {
  return {
    id: Date.now(),
    name: userData.name,
    email: userData.email
  };
}
```

- **Core Benefits**: Early error detection catches errors during development, not production
- **Real-World Impact**: Better refactoring enables safe renaming and restructuring with confidence
- **Common Advantage**: Self-documenting types serve as documentation for function signatures
- **Advanced Feature**: Enhanced IDE support with autocomplete, go-to-definition, and find references
- **Interview Tip**: Explain that clear contracts between different parts improve team collaboration

---

## 3) What are TypeScript's primitive data types?

TypeScript includes string, number, boolean, null, undefined, symbol, bigint, and void as primitive types.

```typescript
let name: string = "John";
let age: number = 30;
let isActive: boolean = true;
let data: null = null;
let value: undefined = undefined;
```

- **Core Types**: String (text data), Number (both integers and floating-point), Boolean (true or false)
- **Real-World Use**: Null/Undefined represent absence of value differently
- **Advanced Types**: Symbol (unique identifiers, often used as object keys), BigInt (arbitrary precision integers)
- **Special Type**: Void (absence of any type, commonly used for functions)
- **Interview Tip**: Explain that TypeScript extends JavaScript's type system

---

## 4) What is type inference?

Type inference is TypeScript's ability to automatically determine the type of a variable based on its initial value.

```typescript
let message = "Hello World"; // Inferred as 'string'
let count = 42; // Inferred as 'number'
let isReady = true; // Inferred as 'boolean'
let numbers = [1, 2, 3]; // Inferred as 'number[]'
let mixed = [1, "hello", true]; // Inferred as '(string | number | boolean)[]'
```

- **Core Concept**: TypeScript analyzes code to determine types automatically
- **Real-World Benefit**: Reduces boilerplate, less need for explicit type annotations
- **Advanced Feature**: Context-aware inference considers surrounding code context
- **Optimization**: For arrays, finds the most specific common type
- **Interview Tip**: Explain that function return types can be inferred from function body

---

## 5) What is the difference between `any`, `unknown`, and `never` types?

`any` disables type checking, `unknown` is type-safe but requires type checking, and `never` represents values that never occur.

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
```

- **Core Difference**: Any bypasses type system, use sparingly for migration or external libraries
- **Real-World Use**: Unknown is type-safe alternative to any, requires type narrowing before use
- **Common Mistake**: Never represents impossible states, useful for exhaustive checking
- **Type Safety**: Unknown is safer than any, never is for impossible cases
- **Interview Tip**: Explain that use cases: any for quick fixes, unknown for user input, never for error handling

---

## 6) What is the `void` type and when is it used?

`void` represents the absence of a value, commonly used for functions that don't return a value.

```typescript
function logMessage(message: string): void {
  console.log(message);
  // No return statement
}
```

- **Core Purpose**: Represents functions that don't return anything
- **Real-World Use**: Implicit return means functions with void can have no return statement
- **Common Mistake**: Different from undefined - void means no return, undefined means returned undefined
- **Advanced Feature**: Common use for event handlers, side effects, logging functions
- **Interview Tip**: Explain that type safety prevents accidental use of return value

---

## 7) What are tuples, and how are they different from arrays?

Tuples are arrays with fixed length and known types at each position, while arrays have variable length and same type elements.

```typescript
let person: [string, number] = ["John", 30];
let coordinates: [number, number] = [10, 20];
let names: string[] = ["John", "Jane", "Bob"];
```

- **Core Difference**: Tuples have fixed length, arrays have variable length
- **Real-World Use**: Type safety means each position has a specific type
- **Common Use Cases**: Coordinates, key-value pairs, function returns
- **Advanced Feature**: Can destructure tuples like arrays, tuples can have optional elements with ?
- **Interview Tip**: Explain that tuples provide stronger type safety than arrays

---

## 8) What are enums, and what is the difference between numeric and string enums?

Enums define a set of named constants, with numeric enums having auto-incrementing values and string enums having explicit string values.

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
```

- **Core Difference**: Numeric enums have auto-incrementing numbers starting from 0, string enums have explicit string values
- **Real-World Use**: Type safety prevents invalid enum values
- **Advanced Feature**: Numeric enums create reverse lookup, string enums have no reverse mapping
- **Common Use Cases**: Status codes, configuration options, constants
- **Interview Tip**: Explain that enums provide type-safe constants

---

## 9) What is the purpose of `tsconfig.json` and what are some key compiler options?

`tsconfig.json` configures TypeScript compiler options, including target, module, strict mode, and file inclusion settings.

```json
{
  "compilerOptions": {
    "target": "ES2020",
    "module": "commonjs",
    "lib": ["ES2020", "DOM"],
    "outDir": "./dist",
    "strict": true,
    "esModuleInterop": true
  },
  "include": ["src/**/*"],
  "exclude": ["node_modules", "dist"]
}
```

- **Core Purpose**: Controls how TypeScript compiles code
- **Real-World Settings**: Target (JavaScript version to compile to), Module system (CommonJS, ES modules)
- **Common Configuration**: Strict mode enables additional type checking options
- **Advanced Feature**: File management controls which files to include/exclude
- **Interview Tip**: Explain that different configs for development vs production

---
