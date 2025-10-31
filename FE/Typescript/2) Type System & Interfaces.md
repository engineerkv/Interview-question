# ⚙️ 2. Type System & Interfaces (Q10–21)

---

## 10) What is a type?

Concept:
A type is a way to define the shape, structure, and behavior of data, providing compile-time type checking and better developer experience.

Example:
```typescript
// Basic type definition
type User = {
  id: number;
  name: string;
  email: string;
  isActive: boolean;
};

// Union types
type Status = 'pending' | 'approved' | 'rejected';

// Function types
type EventHandler = (event: Event) => void;

// Primitive types
type ID = string | number;
```

Deep Insight:
- **Type Safety**: Prevents runtime errors by catching type mismatches at compile time
- **Documentation**: Types serve as self-documenting code
- **IntelliSense**: Provides better IDE support with autocomplete and error detection
- **Flexibility**: Can represent any data structure, function signature, or primitive
- **Composability**: Types can be combined, extended, and reused throughout the codebase

---

## 11) What is an interface?

Concept:
An interface defines the contract or shape that an object must follow, specifying what properties and methods it should have.

Example:
```typescript
// Basic interface
interface Person {
  name: string;
  age: number;
  greet(): string;
}

// Optional properties
interface User {
  id: number;
  name: string;
  email?: string; // Optional
}

// Readonly properties
interface Config {
  readonly apiUrl: string;
  readonly timeout: number;
}

// Method signatures
interface Calculator {
  add(a: number, b: number): number;
  subtract(a: number, b: number): number;
}
```

Deep Insight:
- **Contract Definition**: Specifies what an object should look like
- **Extensibility**: Can be extended using inheritance or intersection
- **Declaration Merging**: Multiple interface declarations with the same name are merged
- **Implementation**: Classes can implement interfaces to ensure they follow the contract
- **Type Checking**: Ensures objects conform to the expected structure

---

## 12) What is the difference between `type` aliases and `interface`?

Concept:
`type` aliases can represent any type, while `interface` specifically defines object shapes and can be extended.

Example:
```typescript
// Type alias - can represent any type
type StringOrNumber = string | number;
type User = {
  id: number;
  name: string;
};
```

Deep Insight:
- **Type Aliases**: Can represent unions, primitives, and complex types
- **Interfaces**: Only for object shapes, can be extended and merged
- **Declaration Merging**: Interfaces can be merged, types cannot
- **Extensibility**: Interfaces support inheritance, types use intersection
- **Use Cases**: Use types for unions/primitives, interfaces for object shapes

---

## 13) When should you use `interface` vs `type`?

Concept:
Use `interface` for object shapes that might be extended, and `type` for unions, primitives, and complex type expressions.

Example:
```typescript
// Use interface for object shapes
interface ApiResponse {
  data: any;
  status: number;
}

```

Deep Insight:
- **Object Shapes**: Use interface for objects that might be extended
- **Unions/Primitives**: Use type for non-object types
- **Complex Types**: Use type for mapped types and conditional types
- **Declaration Merging**: Interface allows merging, type doesn't
- **Performance**: Interface is slightly faster for object types

---

## 14) What are optional properties and readonly properties in interfaces?

Concept:
Optional properties can be undefined, while readonly properties cannot be modified after initialization.

Example:
```typescript
interface User {
  id: number;
  name: string;
  email?: string; // Optional property
  readonly createdAt: Date; // Readonly property
}
```

Deep Insight:
- **Optional Properties**: Use ? to make properties optional
- **Readonly Properties**: Use readonly to prevent modification
- **Type Safety**: Prevents accidental modification of immutable data
- **API Design**: Optional properties for flexible object creation
- **Immutability**: Readonly properties ensure data integrity

---

## 15) What are index signatures and when would you use them?

Concept:
Index signatures allow objects to have additional properties with dynamic keys, useful for dictionaries and dynamic objects.

Example:
```typescript
// Index signature for string keys
interface StringDictionary {
  [key: string]: string;
}

// Index signature for number keys
```

Deep Insight:
- **Dynamic Keys**: Allow objects with unknown property names
- **Dictionary Pattern**: Common for key-value mappings
- **Type Safety**: Still provides type checking for known properties
- **Flexibility**: Balance between type safety and flexibility
- **Use Cases**: Configuration objects, API responses, dynamic data

---

## 16) What is structural typing (duck typing)?

Concept:
Structural typing means types are compatible if they have the same structure, regardless of their names.

Example:
```typescript
interface Point {
  x: number;
  y: number;
}

interface Vector {
  x: number;
  y: number;
}

// These are compatible due to structural typing
function movePoint(point: Point) {
  console.log(`Moving to (${point.x}, ${point.y})`);
}

const vector: Vector = { x: 10, y: 20 };
movePoint(vector); // Works! Vector has same structure as Point
```

Deep Insight:
- **Structure Matters**: Types are compatible based on shape, not name
- **Duck Typing**: "If it walks like a duck and quacks like a duck, it's a duck"
- **Flexibility**: Allows loose coupling between components
- **No Inheritance Required**: Objects don't need to explicitly implement interfaces
- **Type Safety**: Still maintains type checking while being flexible

---

## 17) What is excess property checking and how can you avoid it?

Concept:
Excess property checking prevents assigning objects with extra properties to variables, avoidable with type assertions or index signatures.

Example:
```typescript
interface User {
  id: number;
  name: string;
}

// This will cause an error due to excess property checking
const user: User = {
  id: 1,
  name: "John",
  email: "john@example.com" // Error: Object literal may only specify known properties
};

// Solutions to avoid excess property checking:

// 1. Type assertion
const user1: User = {
  id: 1,
  name: "John",
  email: "john@example.com"
} as User;

// 2. Index signature
interface FlexibleUser {
  id: number;
  name: string;
  [key: string]: any;
}

// 3. Variable assignment
const userData = {
  id: 1,
  name: "John",
  email: "john@example.com"
};
const user2: User = userData; // Works!
```

Deep Insight:
- **Prevents Errors**: Catches typos and unexpected properties
- **Type Safety**: Ensures objects match expected interface exactly
- **Workarounds**: Type assertions, index signatures, variable assignment
- **Strict Mode**: More aggressive checking in strict mode
- **API Contracts**: Helps maintain clear interfaces between components

---

## 18) What is type assertion and how is it different from type casting?

Concept:
Type assertion tells TypeScript the type of a value, while type casting is a runtime operation that TypeScript doesn't perform.

Example:
```typescript
// Type assertion - tells TypeScript the type
let value: unknown = "Hello World";
let strLength: number = (value as string).length;

// Alternative syntax
let strLength2: number = (<string>value).length;
```

Deep Insight:
- **Compile Time**: Type assertion only affects TypeScript compilation
- **No Runtime Cost**: No performance impact, just type information
- **Type Safety**: Override TypeScript's type checking
- **Use Cases**: Working with external libraries, DOM elements
- **Risky**: Can lead to runtime errors if assertion is wrong

---

## 19) What are literal types and template literal types?

Concept:
Literal types are exact values, while template literal types create string types from template expressions.

Example:
```typescript
// Literal types
let direction: "up" | "down" | "left" | "right" = "up";
let status: 200 | 404 | 500 = 200;

// Template literal types
type EventName<T extends string> = `on${Capitalize<T>}`;
```

Deep Insight:
- **Exact Values**: Literal types represent specific values
- **String Templates**: Template literals create string types from expressions
- **Type Manipulation**: Capitalize, Uppercase, Lowercase utility types
- **Conditional Logic**: Can combine with conditional types
- **Use Cases**: Event names, CSS properties, API endpoints

---

## 20) What is discriminated union (tagged union) and how is it used for type safety?

Concept:
Discriminated unions use a common property to distinguish between different union members, enabling type-safe pattern matching.

Example:
```typescript
// Discriminated union
type LoadingState = {
  status: "loading";
};

type SuccessState = {
  status: "success";
  data: string;
};

type ErrorState = {
  status: "error";
  error: string;
};

type AppState = LoadingState | SuccessState | ErrorState;

// Type-safe pattern matching
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

Deep Insight:
- **Discriminator**: Common property that identifies the union member
- **Type Narrowing**: TypeScript narrows types based on discriminator
- **Pattern Matching**: Switch statements work perfectly with discriminated unions
- **Type Safety**: Prevents accessing properties that don't exist
- **Use Cases**: State management, API responses, event handling

---

## 21) What are intersection and union types, and how do they differ?

Concept:
Union types represent values that can be one of several types, while intersection types combine multiple types into one.

Example:
```typescript
// Union types - one of several types
type StringOrNumber = string | number;
type Status = "pending" | "approved" | "rejected";

function processValue(value: StringOrNumber) {
  if (typeof value === "string") {
    return value.toUpperCase(); // TypeScript knows this is string
  }
  return value.toString(); // TypeScript knows this is number
}

// Intersection types - combine multiple types
interface Person {
  name: string;
  age: number;
}

interface Employee {
  id: number;
  department: string;
}

type PersonEmployee = Person & Employee; // Must have all properties

const worker: PersonEmployee = {
  name: "John",
  age: 30,
  id: 123,
  department: "Engineering"
};
```

Deep Insight:
- **Union Types**: Values can be one of several types
- **Intersection Types**: Values must satisfy all types simultaneously
- **Type Narrowing**: Union types require type guards
- **Property Merging**: Intersection types merge properties
- **Use Cases**: Unions for alternatives, intersections for combining interfaces

---
