# ⚙️ 2. Type System & Interfaces (Q10–21)

---

## 10) What is a type?

A type is a way to define the shape, structure, and behavior of data, providing compile-time type checking and better developer experience.

```typescript
type User = {
  id: number;
  name: string;
  email: string;
  isActive: boolean;
};

type Status = 'pending' | 'approved' | 'rejected';
type EventHandler = (event: Event) => void;
type ID = string | number;
```

- **Core Purpose**: Type safety prevents runtime errors by catching type mismatches at compile time
- **Real-World Benefit**: Types serve as self-documenting code, provides better IDE support with autocomplete
- **Common Advantage**: Can represent any data structure, function signature, or primitive
- **Advanced Feature**: Types can be combined, extended, and reused throughout the codebase
- **Interview Tip**: Explain that types provide compile-time guarantees

---

## 11) What is an interface?

An interface defines the contract or shape that an object must follow, specifying what properties and methods it should have.

```typescript
interface Person {
  name: string;
  age: number;
  greet(): string;
}

interface User {
  id: number;
  name: string;
  email?: string; // Optional
}

interface Config {
  readonly apiUrl: string;
  readonly timeout: number;
}
```

- **Core Concept**: Specifies what an object should look like
- **Real-World Use**: Can be extended using inheritance or intersection
- **Advanced Feature**: Declaration merging allows multiple interface declarations with the same name to be merged
- **Common Use**: Classes can implement interfaces to ensure they follow the contract
- **Interview Tip**: Explain that interfaces ensure objects conform to the expected structure

---

## 12) What is the difference between `type` aliases and `interface`?

`type` aliases can represent any type, while `interface` specifically defines object shapes and can be extended.

```typescript
type StringOrNumber = string | number;
type User = {
  id: number;
  name: string;
};
```

- **Core Difference**: Type aliases can represent unions, primitives, and complex types
- **Real-World Use**: Interfaces only for object shapes, can be extended and merged
- **Common Mistake**: Declaration merging works with interfaces, not types
- **Advanced Feature**: Interfaces support inheritance, types use intersection
- **Interview Tip**: Explain that use types for unions/primitives, interfaces for object shapes

---

## 13) When should you use `interface` vs `type`?

Use `interface` for object shapes that might be extended, and `type` for unions, primitives, and complex type expressions.

```typescript
interface ApiResponse {
  data: any;
  status: number;
}
```

- **Core Rule**: Use interface for objects that might be extended
- **Real-World Use**: Use type for non-object types (unions/primitives)
- **Common Mistake**: Use type for mapped types and conditional types
- **Advanced Feature**: Interface allows merging, type doesn't
- **Interview Tip**: Explain that interface is slightly faster for object types

---

## 14) What are optional properties and readonly properties in interfaces?

Optional properties can be undefined, while readonly properties cannot be modified after initialization.

```typescript
interface User {
  id: number;
  name: string;
  email?: string; // Optional property
  readonly createdAt: Date; // Readonly property
}
```

- **Core Features**: Use `?` to make properties optional, use `readonly` to prevent modification
- **Real-World Use**: Type safety prevents accidental modification of immutable data
- **Common Use Case**: Optional properties for flexible object creation
- **Advanced Feature**: Readonly properties ensure data integrity
- **Interview Tip**: Explain that readonly properties enable immutability

---

## 15) What are index signatures and when would you use them?

Index signatures allow objects to have additional properties with dynamic keys, useful for dictionaries and dynamic objects.

```typescript
interface StringDictionary {
  [key: string]: string;
}
```

- **Core Purpose**: Allow objects with unknown property names
- **Real-World Use**: Common for key-value mappings (dictionary pattern)
- **Common Advantage**: Still provides type checking for known properties
- **Advanced Feature**: Balance between type safety and flexibility
- **Interview Tip**: Explain that use cases include configuration objects, API responses, dynamic data

---

## 16) What is structural typing (duck typing)?

Structural typing means types are compatible if they have the same structure, regardless of their names.

```typescript
interface Point {
  x: number;
  y: number;
}

interface Vector {
  x: number;
  y: number;
}

function movePoint(point: Point) {
  console.log(`Moving to (${point.x}, ${point.y})`);
}

const vector: Vector = { x: 10, y: 20 };
movePoint(vector); // Works! Vector has same structure as Point
```

- **Core Concept**: Types are compatible based on shape, not name
- **Real-World Impact**: "If it walks like a duck and quacks like a duck, it's a duck"
- **Common Advantage**: Allows loose coupling between components
- **Advanced Feature**: Objects don't need to explicitly implement interfaces
- **Interview Tip**: Explain that structural typing maintains type checking while being flexible

---

## 17) What is excess property checking and how can you avoid it?

Excess property checking prevents assigning objects with extra properties to variables, avoidable with type assertions or index signatures.

```typescript
interface User {
  id: number;
  name: string;
}

const user: User = {
  id: 1,
  name: "John",
  email: "john@example.com"
} as User; // Type assertion

interface FlexibleUser {
  id: number;
  name: string;
  [key: string]: any;
}
```

- **Core Purpose**: Prevents errors, catches typos and unexpected properties
- **Real-World Impact**: Ensures objects match expected interface exactly
- **Common Solutions**: Type assertions, index signatures, variable assignment
- **Advanced Feature**: More aggressive checking in strict mode
- **Interview Tip**: Explain that helps maintain clear interfaces between components

---

## 18) What is type assertion and how is it different from type casting?

Type assertion tells TypeScript the type of a value, while type casting is a runtime operation that TypeScript doesn't perform.

```typescript
let value: unknown = "Hello World";
let strLength: number = (value as string).length;
let strLength2: number = (<string>value).length;
```

- **Core Concept**: Type assertion only affects TypeScript compilation, no runtime cost
- **Real-World Use**: Override TypeScript's type checking
- **Common Use Cases**: Working with external libraries, DOM elements
- **Common Risk**: Can lead to runtime errors if assertion is wrong
- **Interview Tip**: Explain that type assertion is compile-time only, not runtime

---

## 19) What are literal types and template literal types?

Literal types are exact values, while template literal types create string types from template expressions.

```typescript
let direction: "up" | "down" | "left" | "right" = "up";
let status: 200 | 404 | 500 = 200;

type EventName<T extends string> = `on${Capitalize<T>}`;
```

- **Core Concept**: Literal types represent specific values
- **Real-World Use**: Template literals create string types from expressions
- **Advanced Feature**: Type manipulation with Capitalize, Uppercase, Lowercase utility types
- **Advanced Feature**: Can combine with conditional types
- **Interview Tip**: Explain that use cases include event names, CSS properties, API endpoints

---

## 20) What is discriminated union (tagged union) and how is it used for type safety?

Discriminated unions use a common property to distinguish between different union members, enabling type-safe pattern matching.

```typescript
type LoadingState = { status: "loading"; };
type SuccessState = { status: "success"; data: string; };
type ErrorState = { status: "error"; error: string; };
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

- **Core Concept**: Common property (discriminator) identifies the union member
- **Real-World Impact**: TypeScript narrows types based on discriminator
- **Common Use**: Switch statements work perfectly with discriminated unions
- **Advanced Feature**: Type safety prevents accessing properties that don't exist
- **Interview Tip**: Explain that use cases include state management, API responses, event handling

---

## 21) What are intersection and union types, and how do they differ?

Union types represent values that can be one of several types, while intersection types combine multiple types into one.

```typescript
type StringOrNumber = string | number;
type Status = "pending" | "approved" | "rejected";

interface Person {
  name: string;
  age: number;
}

interface Employee {
  id: number;
  department: string;
}

type PersonEmployee = Person & Employee; // Must have all properties
```

- **Core Difference**: Union types: values can be one of several types; Intersection types: values must satisfy all types simultaneously
- **Real-World Use**: Union types require type guards, intersection types merge properties
- **Common Use Cases**: Unions for alternatives, intersections for combining interfaces
- **Advanced Feature**: Type narrowing works with union types
- **Interview Tip**: Explain that choose based on need: alternatives vs combination

---
