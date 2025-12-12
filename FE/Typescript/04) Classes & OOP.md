# 🏛️ 4. Classes & OOP (Q37–44)

---

## 📍 Navigation

<div align="center">

[← Previous: Advanced Types & Generics](03%29%20Advanced%20Types%20%26%20Generics.md) • [Home: README](../README.md)

[📋 Cheatsheet](TypeScript%20Interview%20Cheatsheet.md)

</div>

---

---

## Q37. 💡 Access modifiers

Access modifiers control visibility of class members, with public being default, private only accessible within class, and protected accessible in subclasses - access modifiers enable proper object-oriented design. Public (default access, accessible from anywhere), Private (only accessible within the same class), Protected (accessible within class and subclasses).

- **Trade-offs**: The catch is type safety prevents external access to sensitive data - encapsulation improves code maintainability. Access modifiers enable proper object-oriented design, but watch out - control access to internal implementation (encapsulation).

Example:

```typescript
class BankAccount {
  public accountNumber: string; // Public: accessible from anywhere
  private balance: number; // Private: only accessible within this class
  protected bankName: string; // Protected: accessible in this class and subclasses

  constructor(accountNumber: string, initialBalance: number) {
    this.accountNumber = accountNumber; // Can access public property
    this.balance = initialBalance; // Can access private property (within class)
    this.bankName = "MyBank"; // Can access protected property (within class)
  }
  
  // Public method can access private property
  getBalance(): number {
    return this.balance; // Accessing private property is allowed within class
  }
}

```

---

## Q38. 📋 Difference between abstract classes and interfaces

Abstract classes can have implementation and cannot be instantiated, while interfaces only define contracts and can be implemented by classes - abstract classes provide base implementation, interfaces provide contracts. Abstract classes can have implementation, interfaces only define contracts.

- **Trade-offs**: The catch is abstract classes can have concrete methods - use cases: abstract classes for shared behavior, interfaces for contracts. Abstract classes provide base implementation, interfaces provide contracts, but watch out - classes can implement multiple interfaces.

Example:

```typescript
// Abstract class: cannot be instantiated, can have implementation
abstract class Animal {
  protected name: string; // Protected: accessible in subclasses
  constructor(name: string) { this.name = name; } // Constructor with implementation
  abstract makeSound(): string; // Abstract method: must be implemented by subclasses
}

// Interface: only defines contract, no implementation
interface Flyable {
  fly(): void; // Method signature only, no implementation
}

// Class can extend abstract class and implement interface
class Bird extends Animal implements Flyable {
  makeSound(): string { return "Chirp"; } // Must implement abstract method
  fly(): void { console.log("Flying"); } // Must implement interface method
}

```

---

## Q39. 🧬 Inheritance

Inheritance uses `extends` keyword, while polymorphism allows objects of different types to be treated uniformly through common interfaces - inheritance maintains type safety across hierarchy. Use `extends` to create class hierarchies.

- **Trade-offs**: The catch is override parent methods in child classes - super keyword calls parent constructor and methods. Inheritance maintains type safety across hierarchy, but watch out - polymorphism means same interface, different implementations.

Example:

```typescript
// Parent class: base implementation
class Vehicle {
  protected brand: string; // Protected: accessible in subclasses
  constructor(brand: string) { this.brand = brand; }
  start(): string { return `${this.brand} started!`; } // Base implementation
}

// Child class: inherits from Vehicle, overrides start method
class Car extends Vehicle {
  start(): string { 
    return `Car ${super.start()}`; // super.start() calls parent's start method
  }
}

```

---

## Q40. 💡 Polymorphism

Polymorphism allows objects of different types to be treated uniformly through common interfaces - same interface, different implementations. Same interface, different implementations.

- **Trade-offs**: The catch is enables runtime polymorphism - maintains type safety while allowing flexibility. Same interface, different implementations, but watch out - objects can be treated uniformly through common interfaces.

Example:

```typescript
// Interface: defines contract that multiple classes can implement
interface Shape {
  area(): number; // All shapes must implement area method
}

// Circle implements Shape interface
class Circle implements Shape {
  constructor(private radius: number) {}
  area(): number { return Math.PI * this.radius ** 2; } // Circle's implementation
}

// Rectangle implements same Shape interface
class Rectangle implements Shape {
  constructor(private width: number, private height: number) {}
  area(): number { return this.width * this.height; } // Rectangle's implementation
}

// Polymorphism: treat different shapes uniformly
function printArea(shape: Shape) {
  console.log(shape.area()); // Works with any Shape implementation
}

```

---

## Q41. 💡 Static properties and methods

Static members belong to the class itself rather than instances, accessed through the class name without instantiation - static methods don't require instance creation (memory efficient). Static members belong to the class, not instances.

- **Trade-offs**: The catch is static properties are shared across all instances - utility functions are common use case for static methods. Static methods don't require instance creation (memory efficient), but watch out - can access static members without creating instances.

Example:

```typescript
class MathUtils {
  static PI: number = 3.14159;
  static E: number = 2.71828;

  static add(a: number, b: number): number {
    return a + b;
  }
}

```

---

## Q42. 💡 Readonly properties

`readonly` properties can only be assigned during initialization, preventing modification after object creation - use cases include IDs, timestamps, configuration values. Prevent modification after initialization (immutability).

- **Trade-offs**: The catch is compile-time protection against modification - ensure critical data remains unchanged (data integrity). Use cases include IDs, timestamps, configuration values, but watch out - can assign values in constructor.

Example:

```typescript
class User {
  readonly id: number;
  readonly createdAt: Date;
  public name: string;
  public email: string;

  constructor(id: number, name: string, email: string) {
    this.id = id;
    this.createdAt = new Date();
    this.name = name;
    this.email = email;
  }
}

```

---

## Q43. 🔧 Decorators and how to use them

Decorators are functions that modify classes, methods, or properties, providing metadata and enabling aspect-oriented programming - use cases include logging, validation, dependency injection. Add cross-cutting concerns to classes (aspect-oriented).

- **Trade-offs**: The catch is combine multiple decorators on same target - decorators execute at runtime. Use cases include logging, validation, dependency injection, but watch out - provide additional information about classes/methods (metadata).

Example:

```typescript
function LogClass(target: any) {
  console.log(`Class ${target.name} created`);
}

function LogMethod(target: any, methodName: string, descriptor: PropertyDescriptor) {
  const original = descriptor.value;
  descriptor.value = function(...args: any[]) {
    console.log(`Calling ${methodName} with args:`, args);
    return original.apply(this, args);
  };
}

@LogClass
class User {
  @LogMethod
  getName() { return "John"; }
}

```

---

## Q44. 🔧 Mixins and how to use them

Mixins are a way to combine multiple classes into one, enabling multiple inheritance-like behavior in TypeScript - mixins add functionality to existing classes (flexibility). Combine multiple classes into one (multiple inheritance).

- **Trade-offs**: The catch is use interfaces to declare mixin types - mixins are applied at runtime. Mixins add functionality to existing classes (flexibility), but watch out - use functions to apply multiple classes (mixin pattern).

Example:

```typescript
function Timestamped<T extends new (...args: any[]) => {}>(Base: T) {
  return class extends Base {
    timestamp: Date = new Date();
    getTimestamp() { return this.timestamp; }
  };
}

class User { name: string = "John"; }
const TimestampedUser = Timestamped(User);
const user = new TimestampedUser();

```

---

## 📍 Navigation

<div align="center">

[← Previous: Advanced Types & Generics](03%29%20Advanced%20Types%20%26%20Generics.md) • [Home: README](../README.md)

[📋 Cheatsheet](TypeScript%20Interview%20Cheatsheet.md)

</div>

---
