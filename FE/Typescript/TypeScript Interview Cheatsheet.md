# 🧠 TypeScript Interview Cheatsheet

> **⏱️ Review Time: 15-20 minutes** | **Priority: ⭐⭐ Medium** | Quick reference for TypeScript interviews
>
> **Coverage: Q1-Q44** (44 questions across 4 topics)

**Quick Review Checklist:**

- [ ] TypeScript Basics (Type Annotation, Inference, Union/Intersection)

- [ ] Interfaces & Types (Interface vs Type, Extension)

- [ ] Functions (Function Types, Overloading, Generics)

- [ ] Advanced Types (Conditional, Mapped, Utility Types)

- [ ] Classes & Inheritance (Access Modifiers, Abstract Classes)

- [ ] TypeScript Configuration (tsconfig.json, Compiler Flags)

---

## 📋 **Question Coverage**

- **Q1-Q10**: TypeScript Fundamentals

- **Q11-Q24**: Type System & Interfaces

- **Q25-Q36**: Functions & Advanced Type Features

- **Q37-Q44**: Classes & Object-Oriented Features

---

## 📋 **TypeScript Basics**

| Concept | Description | Example |
|---------|-------------|---------|
| **Type Annotation** | Explicit type declaration | `let name: string = "John"` |
| **Type Inference** | Automatic type detection | `let age = 30` // inferred as number |
| **Union Types** | Multiple possible types | `let id: string \| number` |
| **Intersection Types** | Combine multiple types | `type User = Person & Employee` |
| **Generic Types** | Reusable type parameters | `function identity<T>(arg: T): T` |

---

## 🔧 **Primitive Types**

### **Basic Types**

**Definition:** TypeScript provides type annotations for primitives (string, number, boolean, null, undefined, symbol, bigint) and type inference to automatically detect types.

```typescript
// Primitive types
let name: string = "John";
let age: number = 30;
let isActive: boolean = true;
let data: null = null;
let value: undefined = undefined;
let id: symbol = Symbol("id");
let bigNumber: bigint = 123n;
let nothing: void = undefined;

// Type inference
let inferredString = "Hello"; // TypeScript infers 'string'
let inferredNumber = 42; // TypeScript infers 'number'

```

### **Special Types**

```typescript
// any - disables type checking
let anything: any = 42;
anything = "hello";
anything.foo.bar.baz; // No error, but will crash at runtime

// unknown - type-safe but requires checking
let userInput: unknown = getUserInput();
if (typeof userInput === "string") {
  console.log(userInput.toUpperCase()); // Safe after type check
}

// never - represents unreachable code
function throwError(message: string): never {
  throw new Error(message);
}

```

---

## 🏗️ **Interfaces & Types**

### **Interfaces**

**Definition:** Interfaces define object shapes with required/optional properties, readonly modifiers, and can be extended; support index signatures for dynamic properties.

```typescript
// Basic interface
interface User {
  id: number;
  name: string;
  email?: string; // Optional property
  readonly createdAt: Date; // Readonly property
}

// Interface extension
interface AdminUser extends User {
  permissions: string[];
}

// Index signature
interface StringDictionary {
  [key: string]: string;
}

```

### **Type Aliases**

**Definition:** Type aliases create reusable type definitions for unions, intersections, and object types; can represent complex type combinations.

```typescript
// Type alias
type StringOrNumber = string | number;
type User = {
  id: number;
  name: string;
};

// Union types
type Status = "pending" | "approved" | "rejected";

// Intersection types
type UserEmployee = User & Employee;

```

---

## 🔄 **Functions**

### **Function Types**

**Definition:** TypeScript functions specify parameter types and return types; support optional parameters, rest parameters, and function type annotations.

```typescript
// Function declaration
function add(a: number, b: number): number {
  return a + b;
}

// Function expression
const multiply = (a: number, b: number): number => a * b;

// Function type
type MathOperation = (a: number, b: number) => number;

// Optional parameters
function greet(name: string, greeting?: string): string {
  return `${greeting || "Hello"}, ${name}!`;
}

// Rest parameters
function sum(...numbers: number[]): number {
  return numbers.reduce((total, num) => total + num, 0);
}

```

### **Function Overloading**

```typescript
function process(value: string): string;
function process(value: number): number;
function process(value: string | number): string | number {
  if (typeof value === "string") {
    return value.toUpperCase();
  } else {
    return value * 2;
  }
}

```

---

## 🧩 **Generics**

### **Generic Functions**

```typescript
// Basic generic function
function identity<T>(arg: T): T {
  return arg;
}

// Generic with constraints
function getProperty<T, K extends keyof T>(obj: T, key: K): T[K] {
  return obj[key];
}

// Generic with default type
function createResponse<T = string>(data: T): ApiResponse<T> {
  return { data, status: 200, message: "Success" };
}

```

### **Generic Interfaces**

```typescript
interface Container<T> {
  value: T;
  getValue(): T;
  setValue(value: T): void;
}

interface ApiResponse<T> {
  data: T;
  status: number;
  message: string;
}

```

### **Generic Classes**

```typescript
class Stack<T> {
  private items: T[] = [];

  push(item: T): void {
    this.items.push(item);
  }

  pop(): T | undefined {
    return this.items.pop();
  }
}

```

---

## 🏛️ **Classes**

### **Basic Class**

```typescript
class User {
  private id: number;
  public name: string;
  protected email: string;

  constructor(id: number, name: string, email: string) {
    this.id = id;
    this.name = name;
    this.email = email;
  }

  public getName(): string {
    return this.name;
  }

  private validateEmail(): boolean {
    return this.email.includes("@");
  }
}

```

### **Inheritance**

```typescript
class Animal {
  protected name: string;

  constructor(name: string) {
    this.name = name;
  }

  public makeSound(): void {
    console.log("Some sound");
  }
}

class Dog extends Animal {
  public makeSound(): void {
    console.log("Woof!");
  }
}

```

### **Abstract Classes**

```typescript
abstract class Shape {
  protected color: string;

  constructor(color: string) {
    this.color = color;
  }

  // Abstract method - must be implemented by subclasses
  abstract getArea(): number;

  // Concrete method
  public getColor(): string {
    return this.color;
  }
}

class Circle extends Shape {
  private radius: number;

  constructor(color: string, radius: number) {
    super(color);
    this.radius = radius;
  }

  getArea(): number {
    return Math.PI * this.radius * this.radius;
  }
}

```

---

## 🎭 **Decorators & Mixins**

### **Decorators**

```typescript
// Class decorator
function LogClass(target: any) {
  console.log(`Class ${target.name} created`);
}

// Method decorator
function LogMethod(target: any, methodName: string, descriptor: PropertyDescriptor) {
  const original = descriptor.value;
  descriptor.value = function(...args: any[]) {
    console.log(`Calling ${methodName} with args:`, args);
    return original.apply(this, args);
  };
}

// Property decorator
function LogProperty(target: any, propertyName: string) {
  let value: any;
  const getter = () => {
    console.log(`Getting ${propertyName}: ${value}`);
    return value;
  };
  const setter = (newValue: any) => {
    console.log(`Setting ${propertyName} to: ${newValue}`);
    value = newValue;
  };
  Object.defineProperty(target, propertyName, {
    get: getter,
    set: setter,
    enumerable: true,
    configurable: true
  });
}

// Usage
@LogClass
class User {
  @LogProperty
  name: string = "John";

  @LogMethod
  getName() { return this.name; }
}

```

### **Mixins**

```typescript
// Mixin function
function Timestamped<T extends new (...args: any[]) => {}>(Base: T) {
  return class extends Base {
    timestamp: Date = new Date();
    getTimestamp() { return this.timestamp; }
  };
}

function Loggable<T extends new (...args: any[]) => {}>(Base: T) {
  return class extends Base {
    log(message: string) { console.log(message); }
  };
}

// Apply mixins
class User { name: string = "John"; }
const TimestampedUser = Timestamped(User);
const LoggableUser = Loggable(User);
const FullUser = Loggable(Timestamped(User));

const user = new FullUser();
user.getTimestamp(); // Available from Timestamped mixin
user.log("Hello"); // Available from Loggable mixin

```

---

## 🛠️ **Utility Types**

### **Built-in Utility Types**

```typescript
interface User {
  id: number;
  name: string;
  email: string;
  age: number;
}

// Partial - makes all properties optional
type PartialUser = Partial<User>;

// Pick - selects specific properties
type UserName = Pick<User, "name">;

// Omit - excludes specific properties
type UserWithoutId = Omit<User, "id">;

// Required - makes all properties required
type RequiredUser = Required<PartialUser>;

// Readonly - makes all properties readonly
type ReadonlyUser = Readonly<User>;

```

### **Custom Utility Types**

```typescript
// Custom utility type
type Optional<T, K extends keyof T> = Omit<T, K> & Partial<Pick<T, K>>;

// Usage
type UserWithOptionalEmail = Optional<User, "email">;

// Conditional utility type
type NonNullable<T> = T extends null | undefined ? never : T;

// Mapped utility type
type Getters<T> = {
  [K in keyof T as `get${Capitalize<string & K>}`]: () => T[K];
};

```

---

## 🔍 **Advanced Types**

### **Conditional Types**

```typescript
// Basic conditional type
type IsString<T> = T extends string ? true : false;

// Conditional type with infer
type ReturnType<T> = T extends (...args: any[]) => infer R ? R : never;

// Recursive conditional type
type DeepReadonly<T> = {
  readonly [P in keyof T]: T[P] extends object ? DeepReadonly<T[P]> : T[P];
};

```

### **Mapped Types**

```typescript
// Basic mapped type
type Optional<T> = {
  [K in keyof T]?: T[K];
};

// Mapped type with key manipulation
type Getters<T> = {
  [K in keyof T as `get${Capitalize<string & K>}`]: () => T[K];
};

// Conditional mapped type
type StringProperties<T> = {
  [K in keyof T]: T[K] extends string ? K : never;
}[keyof T];

```

### **Template Literal Types**

```typescript
// Basic template literal type
type EventName<T extends string> = `on${Capitalize<T>}`;
type ClickEvent = EventName<"click">; // "onClick"

// Complex template literal type
type CSSProperty = `--${string}`;
type CSSValue = `${number}px` | `${number}%` | `${number}em`;

```

---

## 🎯 **Type Guards**

### **Type Guard Functions**

```typescript
// Type guard function
function isString(value: unknown): value is string {
  return typeof value === "string";
}

// Usage
function processValue(value: unknown): string {
  if (isString(value)) {
    return value.toUpperCase(); // TypeScript knows it's a string
  }
  throw new Error("Value must be a string");
}

// In operator type guard
function hasName(obj: any): obj is { name: string } {
  return "name" in obj && typeof obj.name === "string";
}

```

### **Discriminated Unions**

```typescript
type LoadingState = {
  status: "loading";
};

type SuccessState = {
  status: "success";
  data: any;
};

type ErrorState = {
  status: "error";
  error: string;
};

type AppState = LoadingState | SuccessState | ErrorState;

function handleState(state: AppState) {
  switch (state.status) {
    case "loading":
      console.log("Loading...");
      break;
    case "success":
      console.log("Data:", state.data); // TypeScript knows this is SuccessState
      break;
    case "error":
      console.log("Error:", state.error); // TypeScript knows this is ErrorState
      break;
  }
}

```

---

## 🔍 **Module Resolution**

### **Classic Module Resolution**

```typescript
// Classic strategy - looks for TypeScript files first
import { utils } from './utils'; // Resolution order:
// 1. ./utils.ts
// 2. ./utils.d.ts
// 3. ./utils/index.ts
// 4. ./utils/index.d.ts

// tsconfig.json
{
  "compilerOptions": {
    "moduleResolution": "classic"
  }
}

```

### **Node Module Resolution**

```typescript
// Node strategy - follows Node.js algorithm
import { lodash } from 'lodash'; // Resolution order:
// 1. ./node_modules/lodash/package.json (main field)
// 2. ./node_modules/lodash/index.js
// 3. ./node_modules/lodash/index.d.ts
// 4. ./node_modules/@types/lodash/index.d.ts

// tsconfig.json
{
  "compilerOptions": {
    "moduleResolution": "node",
    "baseUrl": "./src",
    "paths": { "@/*": ["src/*"] }
  }
}

```

### **Declaration Files**

```typescript
// my-library.d.ts
declare module "my-library" {
  export interface Config {
    apiKey: string;
    timeout?: number;
  }
  export function process(data: Config): void;
}

// Ambient module
declare module "lodash" {
  export function chunk<T>(array: T[], size: number): T[][];
  export function debounce<T extends (...args: any[]) => any>(
    func: T, wait: number): T;
}

```

---

## 🔧 **TypeScript Configuration**

### **tsconfig.json**

```json
{
  "compilerOptions": {
    "target": "ES2020",
    "module": "commonjs",
    "lib": ["ES2020", "DOM"],
    "outDir": "./dist",
    "rootDir": "./src",
    "strict": true,
    "noImplicitAny": true,
    "strictNullChecks": true,
    "noImplicitReturns": true,
    "noUnusedLocals": true,
    "noUnusedParameters": true,
    "exactOptionalPropertyTypes": true,
    "incremental": true,
    "skipLibCheck": true
  },
  "include": ["src/**/*"],
  "exclude": ["node_modules", "dist"]
}

```

### **Common Compiler Flags**

```typescript
// Strict mode options
"strict": true, // Enables all strict mode options
"noImplicitAny": true, // Error on expressions with implied 'any' type
"noImplicitReturns": true, // Error when not all code paths return a value
"noImplicitThis": true, // Error when 'this' has type 'any'
"strictNullChecks": true, // Error on null/undefined assignments
"strictFunctionTypes": true, // Strict checking of function types
"strictBindCallApply": true, // Strict checking of bind/call/apply
"strictPropertyInitialization": true, // Strict checking of property initialization
"noImplicitOverride": true, // Require explicit override keyword
"noUncheckedIndexedAccess": true, // Add undefined to index signature
"exactOptionalPropertyTypes": true, // Make optional properties exact
"noFallthroughCasesInSwitch": true, // Error on fallthrough cases
"noUnusedLocals": true, // Error on unused locals
"noUnusedParameters": true // Error on unused parameters

```

---

## 🎯 **Interview Tips**

### **Common Questions**

1. **TypeScript vs JavaScript** - Static typing, compilation, tooling

2. **Type System** - Interfaces, types, unions, intersections

3. **Generics** - Reusable components, type constraints

4. **Advanced Types** - Conditional types, mapped types, utility types

5. **Classes** - Inheritance, access modifiers, abstract classes

6. **Module Resolution** - Classic vs Node strategies, declaration files

7. **Decorators & Mixins** - Aspect-oriented programming, multiple inheritance

8. **Compiler Internals** - Type checking, performance, configuration

### **Key Concepts**

- **Type Safety**: Compile-time error detection

- **Type Inference**: Automatic type detection

- **Generics**: Reusable type parameters

- **Utility Types**: Built-in type transformations

- **Advanced Types**: Conditional and mapped types

- **Module Resolution**: How TypeScript finds and loads modules

- **Decorators**: Aspect-oriented programming with metadata

- **Mixins**: Multiple inheritance patterns

- **Compiler Internals**: Type checking, performance, configuration

### **Best Practices**

- Use strict mode for better type safety

- Prefer interfaces for object shapes

- Use type aliases for unions and complex types

- Leverage type inference when possible

- Use utility types for common transformations

- Use Node module resolution for modern projects

- Create declaration files for JavaScript libraries

- Use decorators sparingly and with clear purpose

- Prefer composition over mixins when possible

- Enable incremental compilation for large projects

---

## ⚡ **Last-Minute Review (5 minutes)**

### **Must-Know Concepts**

- **Type vs Interface**: Type for unions/intersections, Interface for object shapes

- **Generics**: Reusable type parameters `<T>`

- **Utility Types**: `Partial<T>`, `Pick<T, K>`, `Omit<T, K>`, `Required<T>`

- **Type Guards**: Narrow types with `typeof`, `instanceof`, custom functions

- **Strict Mode**: Enables all strict checks for better type safety

### **Quick Code Snippets**

```typescript
// Generic
function identity<T>(arg: T): T { return arg; }

// Utility Types
type PartialUser = Partial<User>;
type UserName = Pick<User, "name">;
type UserWithoutId = Omit<User, "id">;

// Type Guard
function isString(value: unknown): value is string {
  return typeof value === "string";
}

```

### **Common Gotchas**

- `any` disables type checking (use `unknown` instead)

- Interfaces can be extended, types use intersections

- Generics enable reusable, type-safe code

- Type guards narrow types for safe access

*Remember: TypeScript is about type safety, not runtime behavior. Focus on compile-time benefits and type system features!*
