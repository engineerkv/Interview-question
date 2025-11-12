# 🧩 4. Classes & Object-Oriented Features (Q32–39)

---

## 🧩 Q32. What are access modifiers?

### 🧠 Concept

Access modifiers control visibility of class members, with public being default, private only accessible within class, and protected accessible in subclasses. Access modifiers enable proper object-oriented design.

---

### 💡 Example

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

---

### 🔍 Deep Insights

* **Rule:** Public (default access, accessible from anywhere), Private (only accessible within the same class), Protected (accessible within class and subclasses).
* **Use Case:** Control access to internal implementation (encapsulation).
* **Common Mistake:** Type safety prevents external access to sensitive data.
* **Pro Tip:** Encapsulation improves code maintainability.

---

### ⭐ Senior Takeaway

Access modifiers enable proper object-oriented design.

---

## 🧩 Q33. What is the difference between abstract classes and interfaces?

### 🧠 Concept

Abstract classes can have implementation and cannot be instantiated, while interfaces only define contracts and can be implemented by classes. Abstract classes provide base implementation, interfaces provide contracts.

---

### 💡 Example

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

---

### 🔍 Deep Insights

* **Rule:** Abstract classes can have implementation, interfaces only define contracts.
* **Use Case:** Classes can implement multiple interfaces.
* **Common Mistake:** Abstract classes can have concrete methods.
* **Pro Tip:** Use cases: abstract classes for shared behavior, interfaces for contracts.

---

### ⭐ Senior Takeaway

Abstract classes provide base implementation, interfaces provide contracts.

---

## 🧩 Q34. What is inheritance?

### 🧠 Concept

Inheritance uses `extends` keyword, while polymorphism allows objects of different types to be treated uniformly through common interfaces. Inheritance maintains type safety across hierarchy.

---

### 💡 Example

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

---

### 🔍 Deep Insights

* **Rule:** Use `extends` to create class hierarchies.
* **Use Case:** Polymorphism means same interface, different implementations.
* **Common Mistake:** Override parent methods in child classes.
* **Pro Tip:** Super keyword calls parent constructor and methods.

---

### ⭐ Senior Takeaway

Inheritance maintains type safety across hierarchy.

---

## 🧩 Q35. What is polymorphism?

### 🧠 Concept

Polymorphism allows objects of different types to be treated uniformly through common interfaces. Same interface, different implementations.

---

### 💡 Example

```typescript
interface Shape {
  area(): number;
}

class Circle implements Shape {
  constructor(private radius: number) {}
  area(): number { return Math.PI * this.radius ** 2; }
}

class Rectangle implements Shape {
  constructor(private width: number, private height: number) {}
  area(): number { return this.width * this.height; }
}
```

---

### 🔍 Deep Insights

* **Rule:** Same interface, different implementations.
* **Use Case:** Objects can be treated uniformly through common interfaces.
* **Common Mistake:** Enables runtime polymorphism.
* **Pro Tip:** Maintains type safety while allowing flexibility.

---

### ⭐ Senior Takeaway

Same interface, different implementations.

---

## 🧩 Q36. What are static properties and methods?

### 🧠 Concept

Static members belong to the class itself rather than instances, accessed through the class name without instantiation. Static methods don't require instance creation (memory efficient).

---

### 💡 Example

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

### 🔍 Deep Insights

* **Rule:** Static members belong to the class, not instances.
* **Use Case:** Can access static members without creating instances.
* **Common Mistake:** Static properties are shared across all instances.
* **Pro Tip:** Utility functions are common use case for static methods.

---

### ⭐ Senior Takeaway

Static methods don't require instance creation (memory efficient).

---

## 🧩 Q37. What are readonly properties?

### 🧠 Concept

`readonly` properties can only be assigned during initialization, preventing modification after object creation. Use cases include IDs, timestamps, configuration values.

---

### 💡 Example

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

### 🔍 Deep Insights

* **Rule:** Prevent modification after initialization (immutability).
* **Use Case:** Can assign values in constructor.
* **Common Mistake:** Compile-time protection against modification.
* **Pro Tip:** Ensure critical data remains unchanged (data integrity).

---

### ⭐ Senior Takeaway

Use cases include IDs, timestamps, configuration values.

---

## 🧩 Q38. What are decorators and how do you use them?

### 🧠 Concept

Decorators are functions that modify classes, methods, or properties, providing metadata and enabling aspect-oriented programming. Use cases include logging, validation, dependency injection.

---

### 💡 Example

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

### 🔍 Deep Insights

* **Rule:** Add cross-cutting concerns to classes (aspect-oriented).
* **Use Case:** Provide additional information about classes/methods (metadata).
* **Common Mistake:** Combine multiple decorators on same target.
* **Pro Tip:** Decorators execute at runtime.

---

### ⭐ Senior Takeaway

Use cases include logging, validation, dependency injection.

---

## 🧩 Q39. What are mixins and how do you implement them?

### 🧠 Concept

Mixins are a way to combine multiple classes into one, enabling multiple inheritance-like behavior in TypeScript. Mixins add functionality to existing classes (flexibility).

---

### 💡 Example

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

### 🔍 Deep Insights

* **Rule:** Combine multiple classes into one (multiple inheritance).
* **Use Case:** Use functions to apply multiple classes (mixin pattern).
* **Common Mistake:** Use interfaces to declare mixin types.
* **Pro Tip:** Mixins are applied at runtime.

---

### ⭐ Senior Takeaway

Mixins add functionality to existing classes (flexibility).

---
