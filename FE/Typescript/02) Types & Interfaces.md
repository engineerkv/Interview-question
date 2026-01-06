# 🎯 2. Types & Interfaces (Q11–24)

---

## 📍 Navigation

<div align="center">

[← Previous: Fundamentals & Setup](01%29%20Fundamentals%20%26%20Setup.md) • [Home: README](../README.md) • [Next: Advanced Types & Generics →](03%29%20Advanced%20Types%20%26%20Generics.md)

[📋 Cheatsheet](TypeScript%20Interview%20Cheatsheet.md)

</div>

---

---

## Q11. 📝 Type in TypeScript

A type defines the shape and structure of your data, giving you compile-time type checking that catches errors before your code runs. When you use types, TypeScript checks for type mismatches at compile time, which prevents runtime errors and gives you guarantees about your code.

- **Trade-offs**: The catch is you can use types for any data structure, function signature, or primitive - you can combine them, extend them, and reuse them throughout your codebase. Types give you compile-time safety, but watch out - they also work as self-documenting code and give you better IDE autocomplete.

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

## Q12. 📝 Interface in TypeScript

An interface defines the contract that an object must follow - it specifies what properties and methods the object should have. When you use interfaces, they make sure objects match the expected structure, which helps you catch errors early.

- **Trade-offs**: The catch is declaration merging allows you to declare the same interface multiple times and TypeScript merges them together - classes can implement interfaces to follow the contract. Interfaces ensure objects match the expected structure, but watch out - you can extend them using inheritance or intersection types.

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

## Q13. 📝 Difference between `type` and `interface`

`type` aliases can represent any type including unions, primitives, and complex types, while `interface` specifically defines object shapes and can be extended - use types for unions and primitives, interfaces for object shapes. When you need to combine types, interfaces use inheritance while types use intersection.

- **Trade-offs**: The catch is declaration merging works with interfaces, not types - you can declare the same interface multiple times and TypeScript merges them together. Interfaces support inheritance with `extends`, while types use intersection with `&`. Use types for unions and primitives, interfaces for object shapes, but watch out - interfaces only work for object shapes, while types can represent anything.

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

## Q14. 💡 Optional and readonly properties

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

## Q15. 📇 Index signatures and how to use them

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

## Q16. 💡 Structural typing

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

## Q17. 💡 How TypeScript handles type compatibility and structural typing

TypeScript uses structural typing for type compatibility, meaning types are compatible if they have the same structure - type compatibility is based on shape, not name. TypeScript checks if the source type has all required properties of the target type, allowing more flexible type relationships.

- **Trade-offs**: The catch is function parameter types are checked contravariantly - return types are checked covariantly. Type compatibility enables loose coupling between components, but watch out - structural typing allows objects with compatible shapes to be used interchangeably.

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

function movePoint(point: Point): void {
  console.log(`Moving to (${point.x}, ${point.y})`);
}

const vector: Vector = { x: 10, y: 20 };
movePoint(vector); // Compatible! Same structure

// Function compatibility
type Handler = (value: string) => void;
const handler: Handler = (value: string | number) => {
  console.log(value);
}; // Contravariant: can accept more general parameter

```

---

## Q18. 💡 Excess property checking

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

## Q19. 📝 Type assertion and how to use it

Type assertion tells TypeScript the type of a value, while type casting is a runtime operation that TypeScript doesn't perform - type assertion is compile-time only, not runtime. Type assertion only affects TypeScript compilation, no runtime cost.

- **Trade-offs**: The catch is working with external libraries, DOM elements - can lead to runtime errors if assertion is wrong. Type assertion is compile-time only, not runtime, but watch out - override TypeScript's type checking.

Example:

```typescript
let value: unknown = "Hello World";
let strLength: number = (value as string).length;
let strLength2: number = (<string>value).length;

```

---

## Q20. 📝 How to create and use custom types in TypeScript

Create custom types using `type` aliases or `interface` declarations, combining primitives, unions, intersections, and other types - custom types provide reusable type definitions throughout your codebase. Use `type` for unions, primitives, and complex types, use `interface` for object shapes.

- **Trade-offs**: The catch is type aliases can represent any type including unions and intersections - interfaces support declaration merging and extension. Custom types improve code maintainability and readability, but watch out - combine types using unions, intersections, and generics for powerful type definitions.

Example:

```typescript
// Type alias for union
type Status = "pending" | "approved" | "rejected";

// Type alias for object
type User = {
  id: number;
  name: string;
  email: string;
};

// Type alias with intersection
type AdminUser = User & {
  permissions: string[];
};

// Type alias for function
type EventHandler = (event: Event) => void;

// Interface for object shape
interface ApiResponse<T> {
  data: T;
  status: number;
  message: string;
}

// Using custom types
function processUser(user: User): AdminUser {
  return {
    ...user,
    permissions: ["read", "write"]
  };
}

```

---

## Q21. 📝 Literal types and how to use them

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

## Q22. 📝 Template literal types and how to use them

Template literal types create string types from template expressions, enabling type-safe string manipulation - use cases include event names, CSS properties, API endpoints. Create string types from template expressions.

- **Trade-offs**: The catch is can combine with conditional types - enable type-safe string manipulation. Enable type-safe string manipulation, but watch out - type manipulation with Capitalize, Uppercase, Lowercase utility types.

Example:

```typescript
type EventName<T extends string> = `on${Capitalize<T>}`;
type CSSProperty = `margin-${'top' | 'bottom' | 'left' | 'right'}`;

```

---

## Q23. 🔧 Discriminated unions and how to use them

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

## Q24. 📝 Intersection and union types

Union types (`|`) represent "either/or" - a value can be one of several types. Intersection types (`&`) represent "and" - combine multiple types requiring all properties.

```typescript
// Union: value can be string OR number
type StringOrNumber = string | number;
let id: StringOrNumber = "abc123";

// Intersection: must have ALL properties
interface Person { name: string; age: number; }
interface Employee { id: number; }
type Worker = Person & Employee; // Must have name, age, AND id
```

- **Union types require type guards** - TypeScript narrows types after runtime checks, but you must check before accessing type-specific properties
- **Intersection types merge all properties** - Useful for mixins and extending interfaces, but watch for property conflicts between combined types
- **Union types enable discriminated unions** - Add a common literal property (like `type: "dog"`) to enable exhaustive type checking in switch statements
- **Intersection with primitives creates `never`** - `string & number` is impossible, resulting in `never` type, useful for type-level programming
- **Use unions for flexibility, intersections for composition** - Unions handle alternatives (API responses, state machines), intersections combine capabilities (mixins, extending contracts)

---

## 📍 Navigation

<div align="center">

[← Previous: Fundamentals & Setup](01%29%20Fundamentals%20%26%20Setup.md) • [Home: README](../README.md) • [Next: Advanced Types & Generics →](03%29%20Advanced%20Types%20%26%20Generics.md)

[📋 Cheatsheet](TypeScript%20Interview%20Cheatsheet.md)

</div>

---
