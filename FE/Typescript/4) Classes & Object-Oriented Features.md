# 🧩 4. Classes & Object-Oriented Features (Q32–39)

---

## 32) What are access modifiers (`public`, `private`, `protected`)?

Access modifiers control visibility of class members, with public being default, private only accessible within class, and protected accessible in subclasses.

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

- **Core Modifiers**: Public (default access, accessible from anywhere), Private (only accessible within the same class), Protected (accessible within class and subclasses)
- **Real-World Use**: Control access to internal implementation (encapsulation)
- **Common Advantage**: Type safety prevents external access to sensitive data
- **Advanced Feature**: Encapsulation improves code maintainability
- **Interview Tip**: Explain that access modifiers enable proper object-oriented design

---

## 33) What is the difference between abstract classes and interfaces?

Abstract classes can have implementation and cannot be instantiated, while interfaces only define contracts and can be implemented by classes.

```typescript
abstract class Animal {
  protected name: string;
  constructor(name: string) { this.name = name; }
  abstract makeSound(): string;
}

interface Flyable {
  fly(): void;
}
```

- **Core Difference**: Abstract classes can have implementation, interfaces only define contracts
- **Real-World Use**: Classes can implement multiple interfaces
- **Common Advantage**: Abstract classes can have concrete methods
- **Advanced Feature**: Use cases: abstract classes for shared behavior, interfaces for contracts
- **Interview Tip**: Explain that abstract classes provide base implementation, interfaces provide contracts

---

## 34) How do you implement inheritance and polymorphism in classes?

Inheritance uses `extends` keyword, while polymorphism allows objects of different types to be treated uniformly through common interfaces.

```typescript
class Vehicle {
  protected brand: string;
  constructor(brand: string) { this.brand = brand; }
  start(): string { return `${this.brand} started!`; }
}

class Car extends Vehicle {
  start(): string { return `Car ${super.start()}`; }
}
```

- **Core Concept**: Use `extends` to create class hierarchies
- **Real-World Impact**: Polymorphism means same interface, different implementations
- **Common Pattern**: Override parent methods in child classes
- **Advanced Feature**: Super keyword calls parent constructor and methods
- **Interview Tip**: Explain that inheritance maintains type safety across hierarchy

---

## 35) What are static properties and methods in classes?

Static members belong to the class itself rather than instances, accessed through the class name without instantiation.

```typescript
class MathUtils {
  static PI: number = 3.14159;
  static E: number = 2.71828;

  static add(a: number, b: number): number {
    return a + b;
  }
}
```

- **Core Concept**: Static members belong to the class, not instances
- **Real-World Use**: Can access static members without creating instances
- **Common Use Case**: Static properties are shared across all instances
- **Advanced Feature**: Utility functions are common use case for static methods
- **Interview Tip**: Explain that static methods don't require instance creation (memory efficient)

---

## 36) What is the purpose of `readonly` properties in classes?

`readonly` properties can only be assigned during initialization, preventing modification after object creation.

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

- **Core Purpose**: Prevent modification after initialization (immutability)
- **Real-World Use**: Can assign values in constructor
- **Common Advantage**: Compile-time protection against modification
- **Advanced Feature**: Ensure critical data remains unchanged (data integrity)
- **Interview Tip**: Explain that use cases include IDs, timestamps, configuration values

---

## 37) What are decorators? How do class, method, and property decorators work?

Decorators are functions that modify classes, methods, or properties, providing metadata and enabling aspect-oriented programming.

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

- **Core Purpose**: Add cross-cutting concerns to classes (aspect-oriented)
- **Real-World Use**: Provide additional information about classes/methods (metadata)
- **Common Pattern**: Combine multiple decorators on same target
- **Advanced Feature**: Decorators execute at runtime
- **Interview Tip**: Explain that use cases include logging, validation, dependency injection

---

## 38) What is metadata reflection and how is it used with decorators?

Metadata reflection allows runtime access to type information and decorator metadata, enabling advanced programming patterns.

```typescript
import "reflect-metadata";

function Column(columnName: string) {
  return function(target: any, propertyKey: string) {
    Reflect.defineMetadata("column", columnName, target, propertyKey);
  };
}

class User {
  @Column("user_name")
  name: string;
}
```

- **Core Concept**: Access type information at runtime
- **Real-World Use**: Store and retrieve decorator information
- **Advanced Feature**: Use Reflect API for metadata operations
- **Advanced Patterns**: Enable dependency injection, ORM mapping
- **Interview Tip**: Explain that reflection accesses type information that's normally lost

---

## 39) What are mixins and how do you implement them?

Mixins are a way to combine multiple classes into one, enabling multiple inheritance-like behavior in TypeScript.

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

- **Core Concept**: Combine multiple classes into one (multiple inheritance)
- **Real-World Use**: Use functions to apply multiple classes (mixin pattern)
- **Advanced Feature**: Use interfaces to declare mixin types
- **Advanced Feature**: Mixins are applied at runtime
- **Interview Tip**: Explain that mixins add functionality to existing classes (flexibility)

---
