# 🔄 3. Functions & Advanced Type Features (Q22–31)

---

## 22) What is the difference between function overloading and overriding?

Overloading provides multiple function signatures for the same function, while overriding replaces a parent class method in a child class.

```typescript
function process(value: string): string;
function process(value: number): number;
function process(value: string | number): string | number {
  return typeof value === "string" ? value.toUpperCase() : value * 2;
}

class Animal {
  makeSound(): string { return "Some sound"; }
}

class Dog extends Animal {
  makeSound(): string { return "Woof!"; }
}
```

- **Core Difference**: Overloading: same function name, different parameter types; Overriding: child class replaces parent class method
- **Real-World Use**: Overloading needs one implementation, overriding needs new implementation
- **Common Advantage**: Overloading provides type safety for different parameter types
- **Advanced Feature**: Overriding enables runtime polymorphism
- **Interview Tip**: Explain that overloading is compile-time, overriding is runtime

---

## 23) What are default and rest parameters in functions?

Default parameters provide fallback values, while rest parameters collect remaining arguments into an array.

```typescript
function greet(name: string, greeting: string = "Hello"): string {
  return `${greeting}, ${name}!`;
}

function sum(...numbers: number[]): number {
  return numbers.reduce((total, num) => total + num, 0);
}
```

- **Core Features**: Default parameters provide fallback values when arguments are omitted
- **Real-World Use**: Rest parameters collect variable number of arguments into array
- **Common Advantage**: Rest parameters are typed as arrays, functions can handle variable number of arguments
- **Important Rule**: Rest parameters must come last in parameter list
- **Interview Tip**: Explain that default and rest parameters improve function flexibility

---

## 24) What are generics and why are they important?

Generics allow you to write code once and use it with different types, keeping everything type-safe.

```typescript
function identity<T>(arg: T): T {
  return arg;
}

interface Container<T> {
  value: T;
  getValue(): T;
}
```

- **Core Purpose**: Maintain type information throughout function execution
- **Real-World Benefit**: Write once, use with multiple types (reusability)
- **Common Advantage**: Work with any type while preserving type constraints
- **Advanced Feature**: Reduce code duplication and improve maintainability
- **Interview Tip**: Explain that generics provide better IDE support with IntelliSense

---

## 25) How do you constrain generics using the `extends` keyword?

The `extends` keyword constrains generic types to specific shapes or types, ensuring they have required properties.

```typescript
function getLength<T extends { length: number }>(item: T): number {
  return item.length;
}

function getKeys<T extends object>(obj: T): (keyof T)[] {
  return Object.keys(obj) as (keyof T)[];
}
```

- **Core Purpose**: Limit generic types to specific shapes
- **Real-World Use**: Ensure required properties exist on generic type
- **Common Advantage**: Prevent errors from missing properties
- **Advanced Feature**: Still allow different types that meet constraints
- **Interview Tip**: Explain that use with `keyof` operator to constrain to object keys

---

## 26) What are utility types (`Partial`, `Pick`, `Omit`, `Required`, `Readonly`)?

Utility types are built-in type transformations that modify existing types for common use cases.

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

- **Core Utilities**: Partial (makes all properties optional), Pick (selects specific properties), Omit (excludes specific properties)
- **Real-World Use**: Required (makes all properties required), Readonly (makes all properties immutable)
- **Common Use Case**: Partial makes all properties optional for updates
- **Advanced Feature**: These utility types are built on mapped types
- **Interview Tip**: Explain that utility types reduce boilerplate code

---

## 27) What are mapped types and how do they work internally?

Mapped types transform existing types by applying transformations to each property, creating new types based on existing ones.

```typescript
type Optional<T> = {
  [K in keyof T]?: T[K];
};

type Readonly<T> = {
  readonly [K in keyof T]: T[K];
};
```

- **Core Concept**: Iterate over all properties of a type
- **Real-World Use**: Apply transformations to each property
- **Advanced Feature**: Modify property names using template literals
- **Advanced Feature**: Use conditional types within mapped types
- **Interview Tip**: Explain that mapped types enable complex type transformations

---

## 28) What are conditional types?

Conditional types select one of two types based on a condition, enabling type-level programming and complex type transformations.

```typescript
type IsString<T> = T extends string ? true : false;

type ApiResponse<T> = T extends string 
  ? { message: T } 
  : { data: T };
```

- **Core Concept**: Perform logic at the type level
- **Real-World Use**: Choose between types based on conditions
- **Advanced Feature**: Can be recursive for complex transformations
- **Advanced Feature**: Use never to exclude types
- **Interview Tip**: Explain that conditional types enable complex type manipulations

---

## 29) What does the `infer` keyword do in conditional types?

`infer` extracts and infers types from other types within conditional types, enabling powerful type inference patterns.

```typescript
type ReturnType<T> = T extends (...args: any[]) => infer R ? R : never;

type Parameters<T> = T extends (...args: infer P) => any ? P : never;
```

- **Core Purpose**: Extract types from other types
- **Real-World Use**: Match patterns and extract parts
- **Advanced Feature**: Let TypeScript infer types automatically
- **Advanced Feature**: Enable complex type transformations
- **Interview Tip**: Explain that use cases include utility types, type extraction, pattern matching

---

## 30) What are keyof and typeof operators and how are they used?

`keyof` extracts keys from object types, while `typeof` gets the type of a value, both enabling type-level operations.

```typescript
interface User {
  id: number;
  name: string;
  email: string;
}

type UserKeys = keyof User; // "id" | "name" | "email"
type UserName = User["name"]; // string

const user = { id: 1, name: "John", age: 30 };
type UserType = typeof user; // { id: number; name: string; age: number; }
```

- **Core Operators**: `keyof` extracts all keys from object types, `typeof` gets type of a value or expression
- **Real-World Use**: Enable type-safe property access
- **Common Use**: Use keys to access property types (indexed access)
- **Advanced Feature**: Use together for advanced type operations
- **Interview Tip**: Explain that these operators enable type-level programming

---

## 31) What are indexed access types and lookup types?

Indexed access types access property types using bracket notation, enabling type lookups and property type extraction.

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

- **Core Concept**: Access property types using bracket notation
- **Real-World Use**: Can access nested property types
- **Advanced Feature**: Use with generics for dynamic property access
- **Advanced Feature**: Enable type lookups and transformations
- **Interview Tip**: Explain that can create unions of property types

---
