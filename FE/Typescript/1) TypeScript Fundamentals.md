# 🧠 1. TypeScript Fundamentals (Q1–9)

---

## 🧩 Q1. What is TypeScript, and how is it different from JavaScript?

### 🧠 Concept

TypeScript is a statically typed superset of JavaScript that compiles to plain JavaScript, providing type safety and better tooling support. You can gradually adopt TypeScript in existing JavaScript projects.

---

### 💡 Example

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

### 🔍 Deep Insights

* **Rule:** Static typing checks types at compile time, JavaScript at runtime.
* **Use Case:** Superset means all valid JavaScript is valid TypeScript.
* **Common Mistake:** TypeScript compiles to JavaScript, not interpreted directly.
* **Pro Tip:** Better IDE support with autocomplete, refactoring, and error detection.

---

### ⭐ Senior Takeaway

You can gradually adopt TypeScript in existing JavaScript projects.

---

## 🧩 Q2. What are the key benefits of using TypeScript in large-scale applications?

### 🧠 Concept

TypeScript provides type safety, better IDE support, early error detection, improved refactoring, and better documentation through types. Clear contracts between different parts improve team collaboration.

---

### 💡 Example

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

---

### 🔍 Deep Insights

* **Rule:** Early error detection catches errors during development, not production.
* **Use Case:** Better refactoring enables safe renaming and restructuring with confidence.
* **Common Mistake:** Self-documenting types serve as documentation for function signatures.
* **Pro Tip:** Enhanced IDE support with autocomplete, go-to-definition, and find references.

---

### ⭐ Senior Takeaway

Clear contracts between different parts improve team collaboration.

---

## 🧩 Q3. How do you install and set up TypeScript?

### 🧠 Concept

Install TypeScript globally or locally, then create a `tsconfig.json` file to configure the compiler. Different configs for development vs production.

---

### 💡 Example

```bash
npm install -g typescript
npm install --save-dev typescript
npx tsc --init
```

---

### 🔍 Deep Insights

* **Rule:** Install TypeScript as a dev dependency for projects.
* **Use Case:** Use `tsc --init` to create a default `tsconfig.json`.
* **Common Mistake:** Configure compiler options based on project needs.
* **Pro Tip:** Use different configs for development vs production.

---

### ⭐ Senior Takeaway

Different configs for development vs production.

---

## 🧩 Q4. What is type inference?

### 🧠 Concept

Type inference is TypeScript's ability to automatically determine the type of a variable based on its initial value. Function return types can be inferred from function body.

---

### 💡 Example

```typescript
let message = "Hello World"; // Inferred as 'string'
let count = 42; // Inferred as 'number'
let isReady = true; // Inferred as 'boolean'
let numbers = [1, 2, 3]; // Inferred as 'number[]'
let mixed = [1, "hello", true]; // Inferred as '(string | number | boolean)[]'
```

---

### 🔍 Deep Insights

* **Rule:** TypeScript analyzes code to determine types automatically.
* **Use Case:** Reduces boilerplate, less need for explicit type annotations.
* **Common Mistake:** Context-aware inference considers surrounding code context.
* **Pro Tip:** For arrays, finds the most specific common type.

---

### ⭐ Senior Takeaway

Function return types can be inferred from function body.

---

## 🧩 Q5. What are the primitive types?

### 🧠 Concept

TypeScript includes string, number, boolean, null, undefined, symbol, bigint, and void as primitive types. TypeScript extends JavaScript's type system.

---

### 💡 Example

```typescript
let name: string = "John";
let age: number = 30;
let isActive: boolean = true;
let data: null = null;
let value: undefined = undefined;
```

---

### 🔍 Deep Insights

* **Rule:** String (text data), Number (both integers and floating-point), Boolean (true or false).
* **Use Case:** Null/Undefined represent absence of value differently.
* **Common Mistake:** Symbol (unique identifiers, often used as object keys), BigInt (arbitrary precision integers).
* **Pro Tip:** Void (absence of any type, commonly used for functions).

---

### ⭐ Senior Takeaway

TypeScript extends JavaScript's type system.

---

## 🧩 Q6. What is the difference between `any`, `unknown`, and `never`?

### 🧠 Concept

`any` disables type checking, `unknown` is type-safe but requires type checking, and `never` represents values that never occur. Use cases: any for quick fixes, unknown for user input, never for error handling.

---

### 💡 Example

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

---

### 🔍 Deep Insights

* **Rule:** Any bypasses type system, use sparingly for migration or external libraries.
* **Use Case:** Unknown is type-safe alternative to any, requires type narrowing before use.
* **Common Mistake:** Never represents impossible states, useful for exhaustive checking.
* **Pro Tip:** Unknown is safer than any, never is for impossible cases.

---

### ⭐ Senior Takeaway

Use cases: any for quick fixes, unknown for user input, never for error handling.

---

## 🧩 Q7. What are tuples and how do you use them?

### 🧠 Concept

Tuples are arrays with fixed length and known types at each position, while arrays have variable length and same type elements. Tuples provide stronger type safety than arrays.

---

### 💡 Example

```typescript
let person: [string, number] = ["John", 30];
let coordinates: [number, number] = [10, 20];
let names: string[] = ["John", "Jane", "Bob"];
```

---

### 🔍 Deep Insights

* **Rule:** Tuples have fixed length, arrays have variable length.
* **Use Case:** Type safety means each position has a specific type.
* **Common Mistake:** Coordinates, key-value pairs, function returns.
* **Pro Tip:** Can destructure tuples like arrays, tuples can have optional elements with ?.

---

### ⭐ Senior Takeaway

Tuples provide stronger type safety than arrays.

---

## 🧩 Q8. What are enums and how do you use them?

### 🧠 Concept

Enums define a set of named constants, with numeric enums having auto-incrementing values and string enums having explicit string values. Enums provide type-safe constants.

---

### 💡 Example

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

---

### 🔍 Deep Insights

* **Rule:** Numeric enums have auto-incrementing numbers starting from 0, string enums have explicit string values.
* **Use Case:** Type safety prevents invalid enum values.
* **Common Mistake:** Numeric enums create reverse lookup, string enums have no reverse mapping.
* **Pro Tip:** Status codes, configuration options, constants.

---

### ⭐ Senior Takeaway

Enums provide type-safe constants.

---

## 🧩 Q9. What is the purpose of `tsconfig.json` and what are some key compiler options?

### 🧠 Concept

`tsconfig.json` configures TypeScript compiler options, including target, module, strict mode, and file inclusion settings. Different configs for development vs production.

---

### 💡 Example

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

---

### 🔍 Deep Insights

* **Rule:** Controls how TypeScript compiles code.
* **Use Case:** Target (JavaScript version to compile to), Module system (CommonJS, ES modules).
* **Common Mistake:** Strict mode enables additional type checking options.
* **Pro Tip:** File management controls which files to include/exclude.

---

### ⭐ Senior Takeaway

Different configs for development vs production.

---
