# 🧩 4. Classes & Object-Oriented Features (Q32–39)

---

## 32) What are access modifiers (`public`, `private`, `protected`)?

Concept:
Access modifiers control visibility of class members, with public being default, private only accessible within class, and protected accessible in subclasses.

Example:
```typescript
class BankAccount {
  public accountNumber: string; // Accessible everywhere
  private balance: number; // Only accessible within this class
  protected bankName: string; // Accessible in this class and subclasses

  constructor(accountNumber: string, initialBalance: number) {
    this.accountNumber = accountNumber;
    this.balance = initialBalance;
    this.bankName = "MyBank";
  }
}
```

Deep Insight:
- **Public**: Default access, accessible from anywhere
- **Private**: Only accessible within the same class
- **Protected**: Accessible within class and subclasses
- **Encapsulation**: Control access to internal implementation
- **Type Safety**: Prevents external access to sensitive data

---

## 33) What is the difference between abstract classes and interfaces?

Concept:
Abstract classes can have implementation and cannot be instantiated, while interfaces only define contracts and can be implemented by classes.

Example:
```typescript
// Abstract class - can have implementation
abstract class Animal {
  protected name: string;
  constructor(name: string) { this.name = name; }
  abstract makeSound(): string;
}

// Interface - only contract
interface Flyable {
  fly(): void;
}
```

Deep Insight:
- **Abstract Classes**: Can have implementation, cannot be instantiated
- **Interfaces**: Only define contracts, can be implemented by classes
- **Multiple Inheritance**: Classes can implement multiple interfaces
- **Implementation**: Abstract classes can have concrete methods
- **Use Cases**: Abstract classes for shared behavior, interfaces for contracts

---

## 34) How do you implement inheritance and polymorphism in classes?

Concept:
Inheritance uses `extends` keyword, while polymorphism allows objects of different types to be treated uniformly through common interfaces.

Example:
```typescript
// Base class
class Vehicle {
  protected brand: string;
  constructor(brand: string) { this.brand = brand; }
  start(): string { return `${this.brand} started!`; }
}

// Child class
class Car extends Vehicle {
  start(): string { return `Car ${super.start()}`; }
}
```

Deep Insight:
- **Inheritance**: Use `extends` to create class hierarchies
- **Polymorphism**: Same interface, different implementations
- **Method Overriding**: Override parent methods in child classes
- **Super Keyword**: Call parent constructor and methods
- **Type Safety**: Maintain type safety across inheritance hierarchy

---

## 35) What are static properties and methods in classes?

Concept:
Static members belong to the class itself rather than instances, accessed through the class name without instantiation.

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

Deep Insight:
- **Class-Level**: Static members belong to the class, not instances
- **No Instantiation**: Can access static members without creating instances
- **Shared State**: Static properties are shared across all instances
- **Utility Functions**: Common use case for static methods
- **Memory Efficiency**: Static methods don't require instance creation

---

## 36) What is the purpose of `readonly` properties in classes?

Concept:
`readonly` properties can only be assigned during initialization, preventing modification after object creation.

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

Deep Insight:
- **Immutability**: Prevent modification after initialization
- **Constructor Assignment**: Can assign values in constructor
- **Type Safety**: Compile-time protection against modification
- **Data Integrity**: Ensure critical data remains unchanged
- **Use Cases**: IDs, timestamps, configuration values

---

## 37) What are decorators? How do class, method, and property decorators work?

Concept:
Decorators are functions that modify classes, methods, or properties, providing metadata and enabling aspect-oriented programming.

Example:
```typescript
// Class decorator
function LogClass(target: any) {
  console.log(`Class ${target.name} created`);
}

// Method decorator
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

Deep Insight:
- **Aspect-Oriented**: Add cross-cutting concerns to classes
- **Metadata**: Provide additional information about classes/methods
- **Composition**: Combine multiple decorators on same target
- **Runtime**: Decorators execute at runtime
- **Use Cases**: Logging, validation, dependency injection

---

## 38) What is metadata reflection and how is it used with decorators?

Concept:
Metadata reflection allows runtime access to type information and decorator metadata, enabling advanced programming patterns.

Example:
```typescript
import "reflect-metadata";

// Custom decorator that stores metadata
function Column(columnName: string) {
  return function(target: any, propertyKey: string) {
    Reflect.defineMetadata("column", columnName, target, propertyKey);
  };
}

// Usage
class User {
  @Column("user_name")
  name: string;
}
```

Deep Insight:
- **Runtime Metadata**: Access type information at runtime
- **Decorator Metadata**: Store and retrieve decorator information
- **Reflection API**: Use Reflect API for metadata operations
- **Advanced Patterns**: Enable dependency injection, ORM mapping
- **Type Information**: Access type information that's normally lost

---

## 39) What are mixins and how do you implement them?

Concept:
Mixins are a way to combine multiple classes into one, enabling multiple inheritance-like behavior in TypeScript.

Example:
```typescript
// Mixin function
function Timestamped<T extends new (...args: any[]) => {}>(Base: T) {
  return class extends Base {
    timestamp: Date = new Date();
    getTimestamp() { return this.timestamp; }
  };
}

// Apply mixin
class User { name: string = "John"; }
const TimestampedUser = Timestamped(User);
const user = new TimestampedUser();
```

Deep Insight:
- **Multiple Inheritance**: Combine multiple classes into one
- **Mixin Pattern**: Use functions to apply multiple classes
- **Interface Merging**: Use interfaces to declare mixin types
- **Runtime Application**: Mixins are applied at runtime
- **Flexibility**: Add functionality to existing classes

---
