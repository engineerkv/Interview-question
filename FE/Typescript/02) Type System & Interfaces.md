# 🎯 2. Type System & Interfaces (Q10–21)

---

## 📍 Navigation

<div align="center">

[← Previous: TypeScript Fundamentals](01%29%20TypeScript%20Fundamentals.md) • [Home: README](../README.md) • [Next: Functions & Advanced Type Features →](03%29%20Functions%20%26%20Advanced%20Type%20Features.md)

[📋 Cheatsheet](TypeScript%20Interview%20Cheatsheet.md)

</div>

---

---

## Q10. 📝 Type in TypeScript

A type is a way to define the shape, structure, and behavior of data, providing compile-time type checking and better developer experience - types provide compile-time guarantees. Type safety prevents runtime errors by catching type mismatches at compile time.

- **Trade-offs**: The catch is can represent any data structure, function signature, or primitive - types can be combined, extended, and reused throughout the codebase. Types provide compile-time guarantees, but watch out - types serve as self-documenting code, provides better IDE support with autocomplete.

Example:

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

---

## Q11. 📝 Interface in TypeScript

An interface defines the contract or shape that an object must follow, specifying what properties and methods it should have - interfaces ensure objects conform to the expected structure. Specifies what an object should look like.

- **Trade-offs**: The catch is declaration merging allows multiple interface declarations with the same name to be merged - classes can implement interfaces to ensure they follow the contract. Interfaces ensure objects conform to the expected structure, but watch out - can be extended using inheritance or intersection.

Example:

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

---

## Q12. 📝 Difference between `type` and `interface`

`type` aliases can represent any type, while `interface` specifically defines object shapes and can be extended - use types for unions/primitives, interfaces for object shapes. Type aliases can represent unions, primitives, and complex types.

- **Trade-offs**: The catch is declaration merging works with interfaces, not types - interfaces support inheritance, types use intersection. Use types for unions/primitives, interfaces for object shapes, but watch out - interfaces only for object shapes, can be extended and merged.

Example:

```typescript
type StringOrNumber = string | number;
type User = {
  id: number;
  name: string;
};

interface ApiResponse {
  data: any;
  status: number;
}

```

---

## Q13. 💡 Optional and readonly properties

Optional properties can be undefined, while readonly properties cannot be modified after initialization - readonly properties enable immutability. Use `?` to make properties optional, use `readonly` to prevent modification.

- **Trade-offs**: The catch is optional properties for flexible object creation - readonly properties ensure data integrity. Readonly properties enable immutability, but watch out - type safety prevents accidental modification of immutable data.

Example:

```typescript
interface User {
  id: number;
  name: string;
  email?: string; // Optional property
  readonly createdAt: Date; // Readonly property
}

```

---

## Q14. 📇 Index signatures and how to use them

Index signatures allow objects to have additional properties with dynamic keys, useful for dictionaries and dynamic objects - use cases include configuration objects, API responses, dynamic data. Allow objects with unknown property names.

- **Trade-offs**: The catch is still provides type checking for known properties - balance between type safety and flexibility. Use cases include configuration objects, API responses, dynamic data, but watch out - common for key-value mappings (dictionary pattern).

Example:

```typescript
interface StringDictionary {
  [key: string]: string;
}

interface FlexibleUser {
  id: number;
  name: string;
  [key: string]: any;
}

```

---

## Q15. 💡 Structural typing

Structural typing means types are compatible if they have the same structure, regardless of their names - structural typing maintains type checking while being flexible. Types are compatible based on shape, not name.

- **Trade-offs**: The catch is allows loose coupling between components - objects don't need to explicitly implement interfaces. Structural typing maintains type checking while being flexible, but watch out - "If it walks like a duck and quacks like a duck, it's a duck".

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

function movePoint(point: Point) {
  console.log(`Moving to (${point.x}, ${point.y})`);
}

const vector: Vector = { x: 10, y: 20 };
movePoint(vector); // Works! Vector has same structure as Point

```

---

## Q16. 💡 Excess property checking

Excess property checking prevents assigning objects with extra properties to variables, avoidable with type assertions or index signatures - helps maintain clear interfaces between components. Prevents errors, catches typos and unexpected properties.

- **Trade-offs**: The catch is type assertions, index signatures, variable assignment - more aggressive checking in strict mode. Helps maintain clear interfaces between components, but watch out - ensures objects match expected interface exactly.

Example:

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

---

## Q17. 📝 Type assertion and how to use it

Type assertion tells TypeScript the type of a value, while type casting is a runtime operation that TypeScript doesn't perform - type assertion is compile-time only, not runtime. Type assertion only affects TypeScript compilation, no runtime cost.

- **Trade-offs**: The catch is working with external libraries, DOM elements - can lead to runtime errors if assertion is wrong. Type assertion is compile-time only, not runtime, but watch out - override TypeScript's type checking.

Example:

```typescript
let value: unknown = "Hello World";
let strLength: number = (value as string).length;
let strLength2: number = (<string>value).length;

```

---

## Q18. 📝 Literal types and how to use them

Literal types allow you specify exact values instead of broad types - when you use `"up"` instead of `string`, TypeScript only allows that specific value. You can use them for string literals like `"success" | "error"`, number literals like `200 | 404 | 500`, or boolean literals like `true` - perfect for event names, status codes, CSS properties, and API endpoints where you need to restrict values to specific options.

- **Trade-offs**: The catch is these can get verbose when you have many possible values - instead of `direction: "up" | "down" | "left" | "right"`, you might want an enum or const object for better maintainability, but literal types work great when you have a small, fixed set of values.

Example:

```typescript
let direction: "up" | "down" | "left" | "right" = "up";
let status: 200 | 404 | 500 = 200;

type Theme = "light" | "dark";
let currentTheme: Theme = "light";

```

---

## Q19. 📝 Template literal types and how to use them

Template literal types create string types from template expressions, enabling type-safe string manipulation - use cases include event names, CSS properties, API endpoints. Create string types from template expressions.

- **Trade-offs**: The catch is can combine with conditional types - enable type-safe string manipulation. Enable type-safe string manipulation, but watch out - type manipulation with Capitalize, Uppercase, Lowercase utility types.

Example:

```typescript
type EventName<T extends string> = `on${Capitalize<T>}`;
type CSSProperty = `margin-${'top' | 'bottom' | 'left' | 'right'}`;

```

---

## Q20. 🔧 Discriminated unions and how to use them

Discriminated unions use a common property to distinguish between different union members, enabling type-safe pattern matching - use cases include state management, API responses, event handling. Common property (discriminator) identifies the union member.

- **Trade-offs**: The catch is switch statements work perfectly with discriminated unions - type safety prevents accessing properties that don't exist. Use cases include state management, API responses, event handling, but watch out - TypeScript narrows types based on discriminator.

Example:

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

---

## Q21. 📝 Intersection and union types

Union types represent values that can be one of several types, while intersection types combine multiple types into one - choose based on need: alternatives vs combination. Union types: values can be one of several types; Intersection types: values must satisfy all types simultaneously.

- **Trade-offs**: The catch is unions for alternatives, intersections for combining interfaces - type narrowing works with union types. Choose based on need: alternatives vs combination, but watch out - union types require type guards, intersection types merge properties.

Example:

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

---

## 📍 Navigation

<div align="center">

[← Previous: TypeScript Fundamentals](01%29%20TypeScript%20Fundamentals.md) • [Home: README](../README.md) • [Next: Functions & Advanced Type Features →](03%29%20Functions%20%26%20Advanced%20Type%20Features.md)

[📋 Cheatsheet](TypeScript%20Interview%20Cheatsheet.md)

</div>

---
