# 🔄 3. Functions & Advanced Type Features (Q22–31)

---

## 🧩 Q22. What is function overloading?

### 🧠 Concept

Function overloading provides multiple function signatures for the same function, enabling type safety for different parameter types. Overloading is compile-time, overriding is runtime.

---

### 💡 Example

```typescript
function process(value: string): string;
function process(value: number): number;
function process(value: string | number): string | number {
  return typeof value === "string" ? value.toUpperCase() : value * 2;
}
```

---

### 🔍 Deep Insights

* **Rule:** Overloading: same function name, different parameter types; Overriding: child class replaces parent class method.
* **Use Case:** Overloading needs one implementation, overriding needs new implementation.
* **Common Mistake:** Overloading provides type safety for different parameter types.
* **Pro Tip:** Overriding enables runtime polymorphism.

---

### ⭐ Senior Takeaway

Overloading is compile-time, overriding is runtime.

---

## 🧩 Q23. What are default and rest parameters?

### 🧠 Concept

Default parameters provide fallback values, while rest parameters collect remaining arguments into an array. Default and rest parameters improve function flexibility.

---

### 💡 Example

```typescript
function greet(name: string, greeting: string = "Hello"): string {
  return `${greeting}, ${name}!`;
}

function sum(...numbers: number[]): number {
  return numbers.reduce((total, num) => total + num, 0);
}
```

---

### 🔍 Deep Insights

* **Rule:** Default parameters provide fallback values when arguments are omitted.
* **Use Case:** Rest parameters collect variable number of arguments into array.
* **Common Mistake:** Rest parameters are typed as arrays, functions can handle variable number of arguments.
* **Pro Tip:** Rest parameters must come last in parameter list.

---

### ⭐ Senior Takeaway

Default and rest parameters improve function flexibility.

---

## 🧩 Q24. What are generics and how do you use them?

### 🧠 Concept

Generics allow you to write code once and use it with different types, keeping everything type-safe. Generics provide better IDE support with IntelliSense.

---

### 💡 Example

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

### 🔍 Deep Insights

* **Rule:** Maintain type information throughout function execution.
* **Use Case:** Write once, use with multiple types (reusability).
* **Common Mistake:** Work with any type while preserving type constraints.
* **Pro Tip:** Reduce code duplication and improve maintainability.

---

### ⭐ Senior Takeaway

Generics provide better IDE support with IntelliSense.

---

## 🧩 Q25. What are generic constraints and how do you use them?

### 🧠 Concept

The `extends` keyword constrains generic types to specific shapes or types, ensuring they have required properties. Use with `keyof` operator to constrain to object keys.

---

### 💡 Example

```typescript
function getLength<T extends { length: number }>(item: T): number {
  return item.length;
}

function getKeys<T extends object>(obj: T): (keyof T)[] {
  return Object.keys(obj) as (keyof T)[];
}
```

---

### 🔍 Deep Insights

* **Rule:** Limit generic types to specific shapes.
* **Use Case:** Ensure required properties exist on generic type.
* **Common Mistake:** Prevent errors from missing properties.
* **Pro Tip:** Still allow different types that meet constraints.

---

### ⭐ Senior Takeaway

Use with `keyof` operator to constrain to object keys.

---

## 🧩 Q26. What are utility types and how do you use them?

### 🧠 Concept

Utility types are built-in type transformations that modify existing types for common use cases. Utility types reduce boilerplate code.

---

### 💡 Example

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

### 🔍 Deep Insights

* **Rule:** Partial (makes all properties optional), Pick (selects specific properties), Omit (excludes specific properties).
* **Use Case:** Required (makes all properties required), Readonly (makes all properties immutable).
* **Common Mistake:** Partial makes all properties optional for updates.
* **Pro Tip:** These utility types are built on mapped types.

---

### ⭐ Senior Takeaway

Utility types reduce boilerplate code.

---

## 🧩 Q27. What are mapped types and how do they work?

### 🧠 Concept

Mapped types transform existing types by applying transformations to each property, creating new types based on existing ones. Mapped types enable complex type transformations.

---

### 💡 Example

```typescript
type Optional<T> = {
  [K in keyof T]?: T[K];
};

type Readonly<T> = {
  readonly [K in keyof T]: T[K];
};
```

---

### 🔍 Deep Insights

* **Rule:** Iterate over all properties of a type.
* **Use Case:** Apply transformations to each property.
* **Common Mistake:** Modify property names using template literals.
* **Pro Tip:** Use conditional types within mapped types.

---

### ⭐ Senior Takeaway

Mapped types enable complex type transformations.

---

## 🧩 Q28. What are conditional types and how do you use them?

### 🧠 Concept

Conditional types select one of two types based on a condition, enabling type-level programming and complex type transformations. Conditional types enable complex type manipulations.

---

### 💡 Example

```typescript
type IsString<T> = T extends string ? true : false;

type ApiResponse<T> = T extends string 
  ? { message: T } 
  : { data: T };
```

---

### 🔍 Deep Insights

* **Rule:** Perform logic at the type level.
* **Use Case:** Choose between types based on conditions.
* **Common Mistake:** Can be recursive for complex transformations.
* **Pro Tip:** Use never to exclude types.

---

### ⭐ Senior Takeaway

Conditional types enable complex type manipulations.

---

## 🧩 Q29. What is the `infer` keyword and how do you use it?

### 🧠 Concept

`infer` extracts and infers types from other types within conditional types, enabling powerful type inference patterns. Use cases include utility types, type extraction, pattern matching.

---

### 💡 Example

```typescript
type ReturnType<T> = T extends (...args: any[]) => infer R ? R : never;

type Parameters<T> = T extends (...args: infer P) => any ? P : never;
```

---

### 🔍 Deep Insights

* **Rule:** Extract types from other types.
* **Use Case:** Match patterns and extract parts.
* **Common Mistake:** Let TypeScript infer types automatically.
* **Pro Tip:** Enable complex type transformations.

---

### ⭐ Senior Takeaway

Use cases include utility types, type extraction, pattern matching.

---

## 🧩 Q30. What are `keyof` and `typeof` operators?

### 🧠 Concept

`keyof` extracts keys from object types, while `typeof` gets the type of a value, both enabling type-level operations. These operators enable type-level programming.

---

### 💡 Example

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

### 🔍 Deep Insights

* **Rule:** `keyof` extracts all keys from object types, `typeof` gets type of a value or expression.
* **Use Case:** Enable type-safe property access.
* **Common Mistake:** Use keys to access property types (indexed access).
* **Pro Tip:** Use together for advanced type operations.

---

### ⭐ Senior Takeaway

These operators enable type-level programming.

---

## 🧩 Q31. What are indexed access types and lookup types?

### 🧠 Concept

Indexed access types access property types using bracket notation, enabling type lookups and property type extraction. Can create unions of property types.

---

### 💡 Example

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

### 🔍 Deep Insights

* **Rule:** Access property types using bracket notation.
* **Use Case:** Can access nested property types.
* **Common Mistake:** Use with generics for dynamic property access.
* **Pro Tip:** Enable type lookups and transformations.

---

### ⭐ Senior Takeaway

Can create unions of property types.

---
