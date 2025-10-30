# 🔄 3. Functions & Advanced Type Features (Q22–31)

---

## 22) What is the difference between function overloading and overriding?

Concept:
Overloading provides multiple function signatures for the same function, while overriding replaces a parent class method in a child class.

Example:
```typescript
// Function overloading - multiple signatures
function process(value: string): string;
function process(value: number): number;
function process(value: string | number): string | number {
  return typeof value === "string" ? value.toUpperCase() : value * 2;
}

// Method overriding - child replaces parent method
class Animal {
  makeSound(): string {
    return "Some sound";
  }
}

class Dog extends Animal {
  makeSound(): string {
    return "Woof!";
  }
}
```

Deep Insight:
- **Overloading**: Same function name, different parameter types
- **Overriding**: Child class replaces parent class method
- **Implementation**: Overloading needs one implementation, overriding needs new implementation
- **Type Safety**: Overloading provides type safety for different parameter types
- **Polymorphism**: Overriding enables runtime polymorphism

---

## 23) What are default and rest parameters in functions?

Concept:
Default parameters provide fallback values, while rest parameters collect remaining arguments into an array.

Example:
```typescript
// Default parameters
function greet(name: string, greeting: string = "Hello"): string {
  return `${greeting}, ${name}!`;
}

// Rest parameters
function sum(...numbers: number[]): number {
  return numbers.reduce((total, num) => total + num, 0);
}
```

Deep Insight:
- **Default Parameters**: Provide fallback values when arguments are omitted
- **Rest Parameters**: Collect variable number of arguments into array
- **Type Safety**: Rest parameters are typed as arrays
- **Flexibility**: Functions can handle variable number of arguments
- **Order**: Rest parameters must come last in parameter list

---

## 24) What are generics and why are they important?

Concept:
Generics allow you to write code once and use it with different types, keeping everything type-safe.

Example:
```typescript
// Generic function
function identity<T>(arg: T): T {
  return arg;
}

// Generic interface
interface Container<T> {
  value: T;
  getValue(): T;
}
```

Deep Insight:
- **Type Safety**: Maintain type information throughout function execution
- **Reusability**: Write once, use with multiple types
- **Flexibility**: Work with any type while preserving type constraints
- **Code Quality**: Reduce code duplication and improve maintainability
- **IntelliSense**: Better IDE support with generic types

---

## 25) How do you constrain generics using the `extends` keyword?

Concept:
The `extends` keyword constrains generic types to specific shapes or types, ensuring they have required properties.

Example:
```typescript
// Constrain generic to have length property
function getLength<T extends { length: number }>(item: T): number {
  return item.length;
}

// Constrain generic to specific type
function getKeys<T extends object>(obj: T): (keyof T)[] {
  return Object.keys(obj) as (keyof T)[];
}
```

Deep Insight:
- **Type Constraints**: Limit generic types to specific shapes
- **Property Access**: Ensure required properties exist on generic type
- **Type Safety**: Prevent errors from missing properties
- **Flexibility**: Still allow different types that meet constraints
- **Keyof Operator**: Use with extends to constrain to object keys

---

## 26) What are utility types (`Partial`, `Pick`, `Omit`, `Required`, `Readonly`)?

Concept:
Utility types are built-in type transformations that modify existing types for common use cases.

Example:
```typescript
interface User {
  id: number;
  name: string;
  email: string;
  age: number;
}

type PartialUser = Partial<User>; // All optional
type UserName = Pick<User, 'name'>; // Only name
type UserWithoutId = Omit<User, 'id'>; // Exclude id
type RequiredUser = Required<PartialUser>; // All required
type ReadonlyUser = Readonly<User>; // All readonly
```

Deep Insight:
- **Partial**: Makes all properties optional for updates
- **Pick**: Selects specific properties from a type
- **Omit**: Excludes specific properties from a type
- **Required**: Makes all properties required
- **Readonly**: Makes all properties immutable

---

## 27) What are mapped types and how do they work internally?

Concept:
Mapped types transform existing types by applying transformations to each property, creating new types based on existing ones.

Example:
```typescript
// Basic mapped type
type Optional<T> = {
  [K in keyof T]?: T[K];
};

// More complex mapped type
type Readonly<T> = {
  readonly [K in keyof T]: T[K];
};
```

Deep Insight:
- **Property Iteration**: Iterate over all properties of a type
- **Type Transformation**: Apply transformations to each property
- **Key Manipulation**: Modify property names using template literals
- **Conditional Logic**: Use conditional types within mapped types
- **Powerful**: Enable complex type transformations

---

## 28) What are conditional types?

Concept:
Conditional types select one of two types based on a condition, enabling type-level programming and complex type transformations.

Example:
```typescript
// Basic conditional type
type IsString<T> = T extends string ? true : false;

// More complex conditional type
type ApiResponse<T> = T extends string 
  ? { message: T } 
  : { data: T };
```

Deep Insight:
- **Type-Level Logic**: Perform logic at the type level
- **Conditional Selection**: Choose between types based on conditions
- **Recursive Types**: Can be recursive for complex transformations
- **Never Type**: Use never to exclude types
- **Powerful**: Enable complex type manipulations

---

## 29) What does the `infer` keyword do in conditional types?

Concept:
`infer` extracts and infers types from other types within conditional types, enabling powerful type inference patterns.

Example:
```typescript
// Extract return type from function
type ReturnType<T> = T extends (...args: any[]) => infer R ? R : never;

// Extract parameter types from function
type Parameters<T> = T extends (...args: infer P) => any ? P : never;
```

Deep Insight:
- **Type Extraction**: Extract types from other types
- **Pattern Matching**: Match patterns and extract parts
- **Inference**: Let TypeScript infer types automatically
- **Powerful**: Enable complex type transformations
- **Use Cases**: Utility types, type extraction, pattern matching

---

## 30) What are keyof and typeof operators and how are they used?

Concept:
`keyof` extracts keys from object types, while `typeof` gets the type of a value, both enabling type-level operations.

Example:
```typescript
// keyof operator
interface User {
  id: number;
  name: string;
  email: string;
}

type UserKeys = keyof User; // "id" | "name" | "email"
type UserName = User["name"]; // string

// typeof operator
const user = { id: 1, name: "John", age: 30 };
type UserType = typeof user; // { id: number; name: string; age: number; }
```

Deep Insight:
- **keyof**: Extract all keys from object types
- **typeof**: Get type of a value or expression
- **Type Safety**: Enable type-safe property access
- **Indexed Access**: Use keys to access property types
- **Combined Power**: Use together for advanced type operations

---

## 31) What are indexed access types and lookup types?

Concept:
Indexed access types access property types using bracket notation, enabling type lookups and property type extraction.

Example:
```typescript
interface User {
  id: number;
  name: string;
  email: string;
  address: {
    street: string;
    city: string;
  };
}

type UserId = User["id"]; // number
type UserAddress = User["address"]; // { street: string; city: string; }
```

Deep Insight:
- **Property Access**: Access property types using bracket notation
- **Nested Access**: Can access nested property types
- **Dynamic Access**: Use with generics for dynamic property access
- **Type Lookups**: Enable type lookups and transformations
- **Union Types**: Can create unions of property types

---
