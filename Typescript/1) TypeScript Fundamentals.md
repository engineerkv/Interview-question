# 🧠 1. TypeScript Fundamentals (Q1–9)

---

## 1) What is TypeScript, and how is it different from JavaScript?

Concept:
TypeScript is a statically typed superset of JavaScript that compiles to plain JavaScript, providing type safety and better tooling support.

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

Deep Insight:
- **Static Typing**: TypeScript checks types at compile time, JavaScript at runtime
- **Superset**: All valid JavaScript is valid TypeScript
- **Compilation**: TypeScript compiles to JavaScript, not interpreted directly
- **Tooling**: Better IDE support with autocomplete, refactoring, and error detection
- **Optional**: You can gradually adopt TypeScript in existing JavaScript projects

---

## 2) What are the key benefits of using TypeScript in large-scale applications?

Concept:
TypeScript provides type safety, better IDE support, early error detection, improved refactoring, and better documentation through types.

Example:
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

Deep Insight:
- **Early Error Detection**: Catch errors during development, not production
- **Better Refactoring**: Safe renaming and restructuring with confidence
- **Self-Documenting**: Types serve as documentation for function signatures
- **IDE Support**: Enhanced autocomplete, go-to-definition, and find references
- **Team Collaboration**: Clear contracts between different parts of the application

---

## 3) What are TypeScript's primitive data types?

Concept:
TypeScript includes string, number, boolean, null, undefined, symbol, bigint, and void as primitive types.

Example:
```typescript
// Primitive types
let name: string = "John";
let age: number = 30;
let isActive: boolean = true;
let data: null = null;
let value: undefined = undefined;
```

Deep Insight:
- **String**: Text data with single or double quotes
- **Number**: Both integers and floating-point numbers
- **Boolean**: True or false values
- **Null/Undefined**: Represent absence of value differently
- **Symbol**: Unique identifiers, often used as object keys
- **BigInt**: Arbitrary precision integers for large numbers
- **Void**: Absence of any type, commonly used for functions

---

## 4) What is type inference?

Concept:
Type inference is TypeScript's ability to automatically determine the type of a variable based on its initial value.

Example:
```typescript
// TypeScript infers types automatically
let message = "Hello World"; // Inferred as 'string'
let count = 42; // Inferred as 'number'
let isReady = true; // Inferred as 'boolean'

// Arrays are inferred based on content
let numbers = [1, 2, 3]; // Inferred as 'number[]'
let mixed = [1, "hello", true]; // Inferred as '(string | number | boolean)[]'
```

Deep Insight:
- **Automatic Detection**: TypeScript analyzes code to determine types
- **Reduces Boilerplate**: Less need for explicit type annotations
- **Context-Aware**: Inference considers surrounding code context
- **Best Common Type**: For arrays, finds the most specific common type
- **Function Returns**: Can infer return types from function body

---

## 5) What is the difference between `any`, `unknown`, and `never` types?

Concept:
`any` disables type checking, `unknown` is type-safe but requires type checking, and `never` represents values that never occur.

Example:
```typescript
// any - disables type checking
let anything: any = 42;
anything = "hello";
anything = true;
anything.foo.bar.baz; // No error, but will crash at runtime

// unknown - type-safe but requires checking
let userInput: unknown = getUserInput();
if (typeof userInput === "string") {
  console.log(userInput.toUpperCase()); // Safe to use
}

// never - represents impossible states
function throwError(message: string): never {
  throw new Error(message);
}
```

Deep Insight:
- **Any**: Bypasses type system, use sparingly for migration or external libraries
- **Unknown**: Type-safe alternative to any, requires type narrowing before use
- **Never**: Represents impossible states, useful for exhaustive checking
- **Type Safety**: Unknown is safer than any, never is for impossible cases
- **Use Cases**: Any for quick fixes, unknown for user input, never for error handling

---

## 6) What is the `void` type and when is it used?

Concept:
`void` represents the absence of a value, commonly used for functions that don't return a value.

Example:
```typescript
// Functions that don't return a value
function logMessage(message: string): void {
  console.log(message);
  // No return statement
}

```

Deep Insight:
- **Absence of Value**: Represents functions that don't return anything
- **Implicit Return**: Functions with void can have no return statement
- **Different from Undefined**: Void means no return, undefined means returned undefined
- **Common Use**: Event handlers, side effects, logging functions
- **Type Safety**: Prevents accidental use of return value

---

## 7) What are tuples, and how are they different from arrays?

Concept:
Tuples are arrays with fixed length and known types at each position, while arrays have variable length and same type elements.

Example:
```typescript
// Tuple - fixed length, specific types
let person: [string, number] = ["John", 30];
let coordinates: [number, number] = [10, 20];

// Array - variable length, same type
let names: string[] = ["John", "Jane", "Bob"];
```

Deep Insight:
- **Fixed Length**: Tuples have a specific number of elements
- **Type Safety**: Each position has a specific type
- **Use Cases**: Coordinates, key-value pairs, function returns
- **Destructuring**: Can destructure tuples like arrays
- **Optional Elements**: Tuples can have optional elements with ?

---

## 8) What are enums, and what is the difference between numeric and string enums?

Concept:
Enums define a set of named constants, with numeric enums having auto-incrementing values and string enums having explicit string values.

Example:
```typescript
// Numeric enum (default)
enum Status {
  Pending,    // 0
  Approved,   // 1
  Rejected    // 2
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

Deep Insight:
- **Numeric Enums**: Auto-incrementing numbers starting from 0
- **String Enums**: Explicit string values, no reverse mapping
- **Type Safety**: Prevents invalid enum values
- **Reverse Mapping**: Numeric enums create reverse lookup
- **Use Cases**: Status codes, configuration options, constants

---

## 9) What is the purpose of `tsconfig.json` and what are some key compiler options?

Concept:
`tsconfig.json` configures TypeScript compiler options, including target, module, strict mode, and file inclusion settings.

Example:
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

Deep Insight:
- **Compiler Configuration**: Controls how TypeScript compiles code
- **Target**: JavaScript version to compile to
- **Module System**: How modules are handled (CommonJS, ES modules)
- **Strict Mode**: Enables additional type checking options
- **File Management**: Controls which files to include/exclude
- **Development**: Different configs for development vs production

---
