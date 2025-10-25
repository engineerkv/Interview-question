# 🧩 TypeScript Interview Notes (2025 Edition)

## 🟠 Section 2 — Intermediate Level (Objects, Classes, and Generics) — Q21-Q40

---

### 21. 🟠 What are interfaces, and how are they used?

**🧠 Concept**

Interfaces define the shape of objects, providing contracts that classes and objects must follow for type safety and code documentation.

**💻 Example**

```typescript
interface User {
  id: number;
  name: string;
  email: string;
  isActive?: boolean;
}

function createUser(userData: User): User {
  return {
    id: Date.now(),
    ...userData,
    isActive: userData.isActive ?? true
  };
}
```

**💬 Explanation + Insight**

- **Object Shape** - Define the structure of objects
- **Type Safety** - Ensure objects have required properties
- **Optional Properties** - Use `?` for optional properties
- **Documentation** - Serve as inline documentation
- **Extensibility** - Can be extended and merged

---

### 22. 🟠 What is the difference between extending an interface and implementing it?

**🧠 Concept**

Extending creates inheritance relationships between interfaces, while implementing enforces that classes follow interface contracts.

**💻 Example**

```typescript
// Interface extending
interface Person {
  name: string;
  age: number;
}

interface Employee extends Person {
  id: number;
  department: string;
}

// Class implementing
class User implements Person {
  name: string;
  age: number;
  
  constructor(name: string, age: number) {
    this.name = name;
    this.age = age;
  }
}
```

**💬 Explanation + Insight**

- **Extending** - Interface inheritance, creates new interface
- **Implementing** - Class must follow interface contract
- **Multiple Interfaces** - Classes can implement multiple interfaces
- **Type Safety** - Both provide compile-time type checking
- **Use Cases** - Extend for interface composition, implement for class contracts

---

### 23. 🟠 What are classes in TypeScript, and how do they differ from ES6 classes?

**🧠 Concept**

TypeScript classes add type annotations, access modifiers, and additional features like abstract classes and parameter properties.

**💻 Example**

```typescript
class Person {
  private name: string;
  protected age: number;
  public email: string;
  
  constructor(name: string, age: number, email: string) {
    this.name = name;
    this.age = age;
    this.email = email;
  }
  
  public getName(): string {
    return this.name;
  }
}
```

**💬 Explanation + Insight**

- **Type Annotations** - Add types to properties and methods
- **Access Modifiers** - Control property and method visibility
- **Parameter Properties** - Shortcut for constructor properties
- **Abstract Classes** - Support for abstract classes and methods
- **Enhanced Features** - More features than ES6 classes

---

### 24. 🟠 What are access modifiers (`public`, `private`, `protected`)?

**🧠 Concept**

Access modifiers control the visibility and accessibility of class members, providing encapsulation and data hiding.

**💻 Example**

```typescript
class BankAccount {
  public accountNumber: string;
  private balance: number;
  protected accountType: string;
  
  constructor(accountNumber: string, balance: number) {
    this.accountNumber = accountNumber;
    this.balance = balance;
    this.accountType = "checking";
  }
  
  public getBalance(): number {
    return this.balance; // Can access private within class
  }
}
```

**💬 Explanation + Insight**

- **public** - Accessible from anywhere (default)
- **private** - Only accessible within the same class
- **protected** - Accessible within class and subclasses
- **Encapsulation** - Hide internal implementation details
- **Data Hiding** - Prevent external access to sensitive data

---

### 25. 🟠 What is `readonly` in classes?

**🧠 Concept**

`readonly` properties can only be assigned during initialization and cannot be modified afterward, providing immutability.

**💻 Example**

```typescript
class User {
  readonly id: number;
  readonly createdAt: Date;
  name: string;
  
  constructor(id: number, name: string) {
    this.id = id; // Can assign during initialization
    this.createdAt = new Date();
    this.name = name;
  }
  
  updateName(newName: string): void {
    this.name = newName; // OK - name is not readonly
    // this.id = 123; // Error - id is readonly
  }
}
```

**💬 Explanation + Insight**

- **Initialization Only** - Can only be assigned during initialization
- **Immutability** - Prevents modification after creation
- **Type Safety** - Compile-time immutability guarantee
- **Use Cases** - IDs, timestamps, configuration values
- **Performance** - No runtime overhead, compile-time feature

---

### 26. 🟠 How does inheritance work in TypeScript?

**🧠 Concept**

Inheritance allows classes to inherit properties and methods from parent classes, enabling code reuse and polymorphism.

**💻 Example**

```typescript
class Animal {
  protected name: string;
  
  constructor(name: string) {
    this.name = name;
  }
  
  public makeSound(): string {
    return "Some sound";
  }
}

class Dog extends Animal {
  public makeSound(): string {
    return "Woof!";
  }
  
  public getName(): string {
    return this.name; // Can access protected property
  }
}
```

**💬 Explanation + Insight**

- **extends Keyword** - Use extends for inheritance
- **Method Overriding** - Override parent methods in child classes
- **Access Modifiers** - Control inheritance visibility
- **Polymorphism** - Child classes can be used as parent types
- **Code Reuse** - Share common functionality across classes

---

### 27. 🟠 What are abstract classes and abstract methods?

**🧠 Concept**

Abstract classes cannot be instantiated and may contain abstract methods that must be implemented by subclasses.

**💻 Example**

```typescript
abstract class Shape {
  protected color: string;
  
  constructor(color: string) {
    this.color = color;
  }
  
  abstract getArea(): number; // Must be implemented by subclasses
  
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

**💬 Explanation + Insight**

- **Cannot Instantiate** - Abstract classes cannot be created directly
- **Abstract Methods** - Must be implemented by subclasses
- **Template Pattern** - Define common structure for subclasses
- **Type Safety** - Ensure subclasses implement required methods
- **Use Cases** - Base classes with common functionality

---

### 28. 🟠 How do you use generics (`<T>`) in TypeScript?

**🧠 Concept**

Generics provide type parameters that allow functions and classes to work with different types while maintaining type safety.

**💻 Example**

```typescript
// Generic function
function identity<T>(arg: T): T {
  return arg;
}

// Generic class
class Container<T> {
  private items: T[] = [];
  
  add(item: T): void {
    this.items.push(item);
  }
  
  get(index: number): T {
    return this.items[index];
  }
}

// Usage
let stringContainer = new Container<string>();
stringContainer.add("Hello");
```

**💬 Explanation + Insight**

- **Type Parameters** - Use `<T>` for generic type parameters
- **Type Safety** - Maintain type safety with different types
- **Reusability** - Write code that works with multiple types
- **Inference** - TypeScript can often infer generic types
- **Use Cases** - Collections, utility functions, API responses

---

### 29. 🟠 What are generic constraints (`T extends ...`)?

**🧠 Concept**

Generic constraints limit the types that can be used with generics, ensuring they have certain properties or capabilities.

**💻 Example**

```typescript
interface Lengthwise {
  length: number;
}

function logLength<T extends Lengthwise>(arg: T): T {
  console.log(arg.length); // OK - T has length property
  return arg;
}

// Usage
logLength("Hello"); // OK - string has length
logLength([1, 2, 3]); // OK - array has length
// logLength(123); // Error - number doesn't have length
```

**💬 Explanation + Insight**

- **Type Constraints** - Limit generic types to specific interfaces
- **Property Access** - Access properties guaranteed by constraints
- **Type Safety** - Ensure types have required properties
- **Flexibility** - Still work with multiple types that meet constraints
- **Use Cases** - Utility functions, type-safe operations

---

### 30. 🟠 What are default generic types?

**🧠 Concept**

Default generic types provide fallback types when no type argument is specified, making generics more convenient to use.

**💻 Example**

```typescript
// Default generic type
interface ApiResponse<T = any> {
  data: T;
  status: number;
  message: string;
}

// Usage without type argument
let response: ApiResponse = { data: "Hello", status: 200, message: "OK" };

// Usage with specific type
let userResponse: ApiResponse<User> = { 
  data: { id: 1, name: "John" }, 
  status: 200, 
  message: "OK" 
};
```

**💬 Explanation + Insight**

- **Fallback Types** - Provide default types when none specified
- **Convenience** - Make generics easier to use
- **Backward Compatibility** - Maintain compatibility with existing code
- **Type Safety** - Still provide type safety with defaults
- **Use Cases** - API responses, configuration objects, utility types

---

### 31. 🟠 What are utility types in TypeScript (`Partial`, `Pick`, `Omit`, `Readonly`, etc.)?

**🧠 Concept**

Utility types are built-in generic types that provide common type transformations, making it easier to work with existing types.

**💻 Example**

```typescript
interface User {
  id: number;
  name: string;
  email: string;
  age: number;
}

// Partial - makes all properties optional
type PartialUser = Partial<User>;
// { id?: number; name?: string; email?: string; age?: number; }

// Pick - selects specific properties
type UserName = Pick<User, 'name'>;
// { name: string; }

// Omit - excludes specific properties
type UserWithoutId = Omit<User, 'id'>;
// { name: string; email: string; age: number; }

// Readonly - makes all properties readonly
type ReadonlyUser = Readonly<User>;
```

**💬 Explanation + Insight**

- **Type Transformations** - Transform existing types into new types
- **Common Patterns** - Provide solutions for common type operations
- **Composition** - Can be composed together for complex transformations
- **Type Safety** - Maintain type safety during transformations
- **Use Cases** - API updates, form data, configuration objects

---

### 32. 🟠 What is a mapped type, and how does it work?

**🧠 Concept**

Mapped types create new types by transforming properties of existing types, providing powerful type manipulation capabilities.

**💻 Example**

```typescript
interface User {
  id: number;
  name: string;
  email: string;
}

// Mapped type - make all properties optional
type Partial<T> = {
  [P in keyof T]?: T[P];
};

// Mapped type - make all properties readonly
type Readonly<T> = {
  readonly [P in keyof T]: T[P];
};

// Custom mapped type
type Stringify<T> = {
  [K in keyof T]: string;
};
```

**💬 Explanation + Insight**

- **Property Transformation** - Transform each property of a type
- **keyof Operator** - Iterate over all keys of a type
- **Conditional Logic** - Apply different transformations based on conditions
- **Type Composition** - Combine with other type operations
- **Use Cases** - Utility types, API transformations, configuration mapping

---

### 33. 🟠 What is the difference between `keyof` and `typeof`?

**🧠 Concept**

`keyof` gets the keys of a type, while `typeof` gets the type of a value, both providing different ways to work with types.

**💻 Example**

```typescript
interface User {
  id: number;
  name: string;
  email: string;
}

// keyof - gets keys of a type
type UserKeys = keyof User; // "id" | "name" | "email"

// typeof - gets type of a value
const user = { id: 1, name: "John", email: "john@example.com" };
type UserType = typeof user; // { id: number; name: string; email: string; }

// Combined usage
function getProperty<T, K extends keyof T>(obj: T, key: K): T[K] {
  return obj[key];
}
```

**💬 Explanation + Insight**

- **keyof** - Extract property names from types
- **typeof** - Extract types from values
- **Type Safety** - Both provide compile-time type safety
- **Generic Constraints** - Often used together in generic functions
- **Use Cases** - Property access, type guards, utility functions

---

### 34. 🟠 What is the `in` operator in mapped types?

**🧠 Concept**

The `in` operator in mapped types iterates over union types, creating new properties for each member of the union.

**💻 Example**

```typescript
// Union type
type Color = "red" | "green" | "blue";

// Mapped type using 'in'
type ColorMap = {
  [K in Color]: string;
};
// { red: string; green: string; blue: string; }

// More complex example
type EventHandlers = {
  [K in keyof HTMLElementEventMap as `on${K}`]: (event: HTMLElementEventMap[K]) => void;
};
```

**💬 Explanation + Insight**

- **Union Iteration** - Iterate over each member of a union type
- **Property Creation** - Create new properties for each union member
- **Type Transformation** - Transform union types into object types
- **Advanced Patterns** - Enable complex type manipulations
- **Use Cases** - Event handlers, configuration objects, API mappings

---

### 35. 🟠 What are index signatures (`[key: string]: type`)?

**🧠 Concept**

Index signatures allow objects to have properties with dynamic keys, providing flexibility for objects with unknown property names.

**💻 Example**

```typescript
// Index signature
interface StringDictionary {
  [key: string]: string;
}

// Usage
let dict: StringDictionary = {
  "hello": "world",
  "foo": "bar"
};

// Mixed with known properties
interface ApiResponse {
  status: number;
  message: string;
  [key: string]: any; // Allow additional properties
}
```

**💬 Explanation + Insight**

- **Dynamic Keys** - Allow properties with unknown names
- **Type Safety** - Ensure all values have the same type
- **Flexibility** - Handle objects with varying property names
- **Use Cases** - Configuration objects, API responses, dictionaries
- **Best Practice** - Use sparingly, prefer specific property definitions

---

### 36. 🟠 What is the difference between namespaces and modules?

**🧠 Concept**

Namespaces provide logical grouping within a single file, while modules are separate files that can be imported and exported.

**💻 Example**

```typescript
// Namespace
namespace MyNamespace {
  export interface User {
    id: number;
    name: string;
  }
  
  export function createUser(name: string): User {
    return { id: Date.now(), name };
  }
}

// Module (separate file)
// user.ts
export interface User {
  id: number;
  name: string;
}

export function createUser(name: string): User {
  return { id: Date.now(), name };
}
```

**💬 Explanation + Insight**

- **Namespaces** - Logical grouping within single file
- **Modules** - Separate files with imports/exports
- **Modern Approach** - Modules are preferred over namespaces
- **Tree Shaking** - Modules enable better tree shaking
- **Use Cases** - Namespaces for legacy code, modules for new projects

---

### 37. 🟠 How do you import and export types and interfaces between files?

**🧠 Concept**

TypeScript supports importing and exporting types using the same syntax as JavaScript, with additional type-only imports for optimization.

**💻 Example**

```typescript
// types.ts
export interface User {
  id: number;
  name: string;
}

export type Status = "active" | "inactive";

// main.ts
import { User, Status } from './types';
import type { User as UserType } from './types'; // Type-only import

// Re-export
export { User, Status } from './types';
export type { User as UserType } from './types';
```

**💬 Explanation + Insight**

- **Same Syntax** - Use same import/export syntax as JavaScript
- **Type-only Imports** - Use `import type` for type-only imports
- **Re-exporting** - Re-export types from other modules
- **Tree Shaking** - Type-only imports are removed from runtime
- **Best Practice** - Use type-only imports when possible

---

### 38. 🟠 What are discriminated (tagged) unions?

**🧠 Concept**

Discriminated unions use a common property to distinguish between different types, enabling type-safe pattern matching.

**💻 Example**

```typescript
// Discriminated union
type Shape = 
  | { kind: "circle"; radius: number }
  | { kind: "rectangle"; width: number; height: number }
  | { kind: "triangle"; base: number; height: number };

function getArea(shape: Shape): number {
  switch (shape.kind) {
    case "circle":
      return Math.PI * shape.radius * shape.radius;
    case "rectangle":
      return shape.width * shape.height;
    case "triangle":
      return (shape.base * shape.height) / 2;
  }
}
```

**💬 Explanation + Insight**

- **Common Property** - Use a common property to distinguish types
- **Type Safety** - TypeScript can narrow types based on the discriminator
- **Exhaustive Checking** - Ensures all cases are handled
- **Pattern Matching** - Enable type-safe pattern matching
- **Use Cases** - State machines, API responses, configuration objects

---

### 39. 🟠 What is type narrowing, and how does TypeScript perform it?

**🧠 Concept**

Type narrowing reduces the type of a variable within a specific scope, allowing TypeScript to provide more accurate type checking.

**💻 Example**

```typescript
function processValue(value: string | number) {
  if (typeof value === "string") {
    // TypeScript knows value is string here
    console.log(value.toUpperCase());
  } else {
    // TypeScript knows value is number here
    console.log(value.toFixed(2));
  }
}

// Type guards
function isString(value: unknown): value is string {
  return typeof value === "string";
}
```

**💬 Explanation + Insight**

- **Scope-based** - Type narrowing works within specific scopes
- **Type Guards** - Use type guards for custom narrowing
- **Control Flow** - TypeScript analyzes control flow for narrowing
- **Type Safety** - Provides more accurate type checking
- **Use Cases** - Union types, unknown types, API responses

---

### 40. 🟠 How do you define and use function overloads in TypeScript?

**🧠 Concept**

Function overloads allow a single function to have multiple signatures, providing different parameter and return types.

**💻 Example**

```typescript
// Function overloads
function createElement(tag: "div"): HTMLDivElement;
function createElement(tag: "span"): HTMLSpanElement;
function createElement(tag: string): HTMLElement {
  return document.createElement(tag);
}

// Usage
let div = createElement("div"); // Type: HTMLDivElement
let span = createElement("span"); // Type: HTMLSpanElement
```

**💬 Explanation + Insight**

- **Multiple Signatures** - Define multiple function signatures
- **Type Safety** - Provide specific types for different use cases
- **Implementation** - Single implementation handles all cases
- **IntelliSense** - Better IDE support with specific types
- **Use Cases** - DOM manipulation, API wrappers, utility functions

---

*This comprehensive TypeScript intermediate section covers all essential concepts including classes, generics, utility types, and advanced type system features for building robust applications.*