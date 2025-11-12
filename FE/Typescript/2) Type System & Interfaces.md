# ⚙️ 2. Type System & Interfaces (Q10–21)

---

## 🧩 Q10. What is a type?

### 🧠 Concept

A type is a way to define the shape, structure, and behavior of data, providing compile-time type checking and better developer experience. Types provide compile-time guarantees.

---

### 💡 Example

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

### 🔍 Deep Insights

* **Rule:** Type safety prevents runtime errors by catching type mismatches at compile time.
* **Use Case:** Types serve as self-documenting code, provides better IDE support with autocomplete.
* **Common Mistake:** Can represent any data structure, function signature, or primitive.
* **Pro Tip:** Types can be combined, extended, and reused throughout the codebase.

---

### ⭐ Senior Takeaway

Types provide compile-time guarantees.

---

## 🧩 Q11. What is an interface?

### 🧠 Concept

An interface defines the contract or shape that an object must follow, specifying what properties and methods it should have. Interfaces ensure objects conform to the expected structure.

---

### 💡 Example

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

### 🔍 Deep Insights

* **Rule:** Specifies what an object should look like.
* **Use Case:** Can be extended using inheritance or intersection.
* **Common Mistake:** Declaration merging allows multiple interface declarations with the same name to be merged.
* **Pro Tip:** Classes can implement interfaces to ensure they follow the contract.

---

### ⭐ Senior Takeaway

Interfaces ensure objects conform to the expected structure.

---

## 🧩 Q12. What is the difference between `type` and `interface`?

### 🧠 Concept

`type` aliases can represent any type, while `interface` specifically defines object shapes and can be extended. Use types for unions/primitives, interfaces for object shapes.

---

### 💡 Example

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

### 🔍 Deep Insights

* **Rule:** Type aliases can represent unions, primitives, and complex types.
* **Use Case:** Interfaces only for object shapes, can be extended and merged.
* **Common Mistake:** Declaration merging works with interfaces, not types.
* **Pro Tip:** Interfaces support inheritance, types use intersection.

---

### ⭐ Senior Takeaway

Use types for unions/primitives, interfaces for object shapes.

---

## 🧩 Q13. What are optional and readonly properties?

### 🧠 Concept

Optional properties can be undefined, while readonly properties cannot be modified after initialization. Readonly properties enable immutability.

---

### 💡 Example

```typescript
interface User {
  id: number;
  name: string;
  email?: string; // Optional property
  readonly createdAt: Date; // Readonly property
}
```

---

### 🔍 Deep Insights

* **Rule:** Use `?` to make properties optional, use `readonly` to prevent modification.
* **Use Case:** Type safety prevents accidental modification of immutable data.
* **Common Mistake:** Optional properties for flexible object creation.
* **Pro Tip:** Readonly properties ensure data integrity.

---

### ⭐ Senior Takeaway

Readonly properties enable immutability.

---

## 🧩 Q14. What are index signatures and how do you use them?

### 🧠 Concept

Index signatures allow objects to have additional properties with dynamic keys, useful for dictionaries and dynamic objects. Use cases include configuration objects, API responses, dynamic data.

---

### 💡 Example

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

### 🔍 Deep Insights

* **Rule:** Allow objects with unknown property names.
* **Use Case:** Common for key-value mappings (dictionary pattern).
* **Common Mistake:** Still provides type checking for known properties.
* **Pro Tip:** Balance between type safety and flexibility.

---

### ⭐ Senior Takeaway

Use cases include configuration objects, API responses, dynamic data.

---

## 🧩 Q15. What is structural typing?

### 🧠 Concept

Structural typing means types are compatible if they have the same structure, regardless of their names. Structural typing maintains type checking while being flexible.

---

### 💡 Example

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

### 🔍 Deep Insights

* **Rule:** Types are compatible based on shape, not name.
* **Use Case:** "If it walks like a duck and quacks like a duck, it's a duck".
* **Common Mistake:** Allows loose coupling between components.
* **Pro Tip:** Objects don't need to explicitly implement interfaces.

---

### ⭐ Senior Takeaway

Structural typing maintains type checking while being flexible.

---

## 🧩 Q16. What is excess property checking?

### 🧠 Concept

Excess property checking prevents assigning objects with extra properties to variables, avoidable with type assertions or index signatures. Helps maintain clear interfaces between components.

---

### 💡 Example

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

### 🔍 Deep Insights

* **Rule:** Prevents errors, catches typos and unexpected properties.
* **Use Case:** Ensures objects match expected interface exactly.
* **Common Mistake:** Type assertions, index signatures, variable assignment.
* **Pro Tip:** More aggressive checking in strict mode.

---

### ⭐ Senior Takeaway

Helps maintain clear interfaces between components.

---

## 🧩 Q17. What is type assertion and how do you use it?

### 🧠 Concept

Type assertion tells TypeScript the type of a value, while type casting is a runtime operation that TypeScript doesn't perform. Type assertion is compile-time only, not runtime.

---

### 💡 Example

```typescript
let value: unknown = "Hello World";
let strLength: number = (value as string).length;
let strLength2: number = (<string>value).length;
```

---

### 🔍 Deep Insights

* **Rule:** Type assertion only affects TypeScript compilation, no runtime cost.
* **Use Case:** Override TypeScript's type checking.
* **Common Mistake:** Working with external libraries, DOM elements.
* **Pro Tip:** Can lead to runtime errors if assertion is wrong.

---

### ⭐ Senior Takeaway

Type assertion is compile-time only, not runtime.

---

## 🧩 Q18. What are literal types and how do you use them?

### 🧠 Concept

Literal types are exact values, while template literal types create string types from template expressions. Use cases include event names, CSS properties, API endpoints.

---

### 💡 Example

```typescript
let direction: "up" | "down" | "left" | "right" = "up";
let status: 200 | 404 | 500 = 200;

type EventName<T extends string> = `on${Capitalize<T>}`;
```

---

### 🔍 Deep Insights

* **Rule:** Literal types represent specific values.
* **Use Case:** Template literals create string types from expressions.
* **Common Mistake:** Type manipulation with Capitalize, Uppercase, Lowercase utility types.
* **Pro Tip:** Can combine with conditional types.

---

### ⭐ Senior Takeaway

Use cases include event names, CSS properties, API endpoints.

---

## 🧩 Q19. What are template literal types and how do you use them?

### 🧠 Concept

Template literal types create string types from template expressions, enabling type-safe string manipulation. Use cases include event names, CSS properties, API endpoints.

---

### 💡 Example

```typescript
type EventName<T extends string> = `on${Capitalize<T>}`;
type CSSProperty = `margin-${'top' | 'bottom' | 'left' | 'right'}`;
```

---

### 🔍 Deep Insights

* **Rule:** Create string types from template expressions.
* **Use Case:** Type manipulation with Capitalize, Uppercase, Lowercase utility types.
* **Common Mistake:** Can combine with conditional types.
* **Pro Tip:** Enable type-safe string manipulation.

---

### ⭐ Senior Takeaway

Enable type-safe string manipulation.

---

## 🧩 Q20. What are discriminated unions and how do you use them?

### 🧠 Concept

Discriminated unions use a common property to distinguish between different union members, enabling type-safe pattern matching. Use cases include state management, API responses, event handling.

---

### 💡 Example

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

### 🔍 Deep Insights

* **Rule:** Common property (discriminator) identifies the union member.
* **Use Case:** TypeScript narrows types based on discriminator.
* **Common Mistake:** Switch statements work perfectly with discriminated unions.
* **Pro Tip:** Type safety prevents accessing properties that don't exist.

---

### ⭐ Senior Takeaway

Use cases include state management, API responses, event handling.

---

## 🧩 Q21. What are intersection and union types?

### 🧠 Concept

Union types represent values that can be one of several types, while intersection types combine multiple types into one. Choose based on need: alternatives vs combination.

---

### 💡 Example

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

### 🔍 Deep Insights

* **Rule:** Union types: values can be one of several types; Intersection types: values must satisfy all types simultaneously.
* **Use Case:** Union types require type guards, intersection types merge properties.
* **Common Mistake:** Unions for alternatives, intersections for combining interfaces.
* **Pro Tip:** Type narrowing works with union types.

---

### ⭐ Senior Takeaway

Choose based on need: alternatives vs combination.

---
