<div align="center">

**[← Previous: Type System & Interfaces](2%29%20Type%20System%20%26%20Interfaces.md)** | **[Next: Classes & Object-Oriented Features →](4%29%20Classes%20%26%20Object-Oriented%20Features.md)**

</div>

# 3. Functions & Advanced Type Features (Q22–31)

---

## Q22. Function overloading and overriding

Function overloading allows you to define multiple signatures for the same function with different parameter types - TypeScript picks the right one based on what you pass, and you write one implementation that handles all cases. Overriding happens when a child class replaces a parent class method with its own implementation - the child's version runs at runtime instead of the parent's.

- **Trade-offs**: The catch is overloading is compile-time only - TypeScript uses it for type checking, but at runtime there's just one function that needs to handle all cases. Overriding enables runtime polymorphism where the actual method called depends on the object type, but you need to make sure the child method matches the parent's signature or TypeScript will complain.

Example:

```typescript
// Overloading - multiple signatures, one implementation
function process(value: string): string;
function process(value: number): number;
function process(value: string | number): string | number {
  return typeof value === "string" ? value.toUpperCase() : value * 2;
}

// Overriding - child class replaces parent method
class Animal {
  makeSound(): void {
    console.log("Some sound");
  }
}

class Dog extends Animal {
  makeSound(): void {
    console.log("Woof!");
  }
}
```

---

## Q23. Default and rest parameters

Default parameters provide fallback values, while rest parameters collect remaining arguments into an array - default and rest parameters improve function flexibility. Default parameters provide fallback values when arguments are omitted.

- **Trade-offs**: The catch is rest parameters are typed as arrays, functions can handle variable number of arguments - rest parameters must come last in parameter list. Default and rest parameters improve function flexibility, but watch out - rest parameters collect variable number of arguments into array.

Example:

```typescript
function greet(name: string, greeting: string = "Hello"): string {
  return `${greeting}, ${name}!`;
}

function sum(...numbers: number[]): number {
  return numbers.reduce((total, num) => total + num, 0);
}
```

---

## Q24. Generics and how to use them

Generics allow you to write code once and use it with different types, keeping everything type-safe - generics provide better IDE support with IntelliSense. Maintain type information throughout function execution.

- **Trade-offs**: The catch is work with any type while preserving type constraints - reduce code duplication and improve maintainability. Generics provide better IDE support with IntelliSense, but watch out - write once, use with multiple types (reusability).

Example:

```typescript
function identity<T>(arg: T): T {
  return arg;
}

interface Container<T> {
  value: T;
  getValue(): T;
}
```

---

## Q25. Generic constraints and how to use them

The `extends` keyword constrains generic types to specific shapes or types, ensuring they have required properties - use with `keyof` operator to constrain to object keys. Limit generic types to specific shapes.

- **Trade-offs**: The catch is prevent errors from missing properties - still allow different types that meet constraints. Use with `keyof` operator to constrain to object keys, but watch out - ensure required properties exist on generic type.

Example:

```typescript
function getLength<T extends { length: number }>(item: T): number {
  return item.length;
}

function getKeys<T extends object>(obj: T): (keyof T)[] {
  return Object.keys(obj) as (keyof T)[];
}
```

---

## Q26. Utility types and how to use them

Utility types are built-in type transformations that modify existing types for common use cases - utility types reduce boilerplate code. Partial (makes all properties optional), Pick (selects specific properties), Omit (excludes specific properties).

- **Trade-offs**: The catch is partial makes all properties optional for updates - these utility types are built on mapped types. Utility types reduce boilerplate code, but watch out - Required (makes all properties required), Readonly (makes all properties immutable).

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

---

## Q27. Mapped types and how to use them

Mapped types transform existing types by applying transformations to each property, creating new types based on existing ones - mapped types enable complex type transformations. Iterate over all properties of a type.

- **Trade-offs**: The catch is modify property names using template literals - use conditional types within mapped types. Mapped types enable complex type transformations, but watch out - apply transformations to each property.

Example:

```typescript
type Optional<T> = {
  [K in keyof T]?: T[K];
};

type Readonly<T> = {
  readonly [K in keyof T]: T[K];
};
```

---

## Q28. Conditional types and how to use them

Conditional types select one of two types based on a condition, enabling type-level programming and complex type transformations - conditional types enable complex type manipulations. Perform logic at the type level.

- **Trade-offs**: The catch is can be recursive for complex transformations - use never to exclude types. Conditional types enable complex type manipulations, but watch out - choose between types based on conditions.

Example:

```typescript
type IsString<T> = T extends string ? true : false;

type ApiResponse<T> = T extends string 
  ? { message: T } 
  : { data: T };
```

---

## Q29. `infer` keyword and how to use it

`infer` extracts and infers types from other types within conditional types, enabling powerful type inference patterns - use cases include utility types, type extraction, pattern matching. Extract types from other types.

- **Trade-offs**: The catch is let TypeScript infer types automatically - enable complex type transformations. Use cases include utility types, type extraction, pattern matching, but watch out - match patterns and extract parts.

Example:

```typescript
type ReturnType<T> = T extends (...args: any[]) => infer R ? R : never;

type Parameters<T> = T extends (...args: infer P) => any ? P : never;
```

---

## Q30. `keyof` and `typeof` operators

`keyof` extracts keys from object types, while `typeof` gets the type of a value, both enabling type-level operations - these operators enable type-level programming. `keyof` extracts all keys from object types, `typeof` gets type of a value or expression.

- **Trade-offs**: The catch is use keys to access property types (indexed access) - use together for advanced type operations. These operators enable type-level programming, but watch out - enable type-safe property access.

Example:

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

---

## Q31. Indexed access types and lookup types

Indexed access types access property types using bracket notation, enabling type lookups and property type extraction - can create unions of property types. Access property types using bracket notation.

- **Trade-offs**: The catch is use with generics for dynamic property access - enable type lookups and transformations. Can create unions of property types, but watch out - can access nested property types.

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

---

