# 🚀 TypeScript Cheatsheet (2025 Edition)

## 📋 Quick Reference Guide

### 🔧 Basic Types
```typescript
// Primitive types
let name: string = "John";
let age: number = 25;
let isActive: boolean = true;
let data: any = { anything: "goes" };
let unknownData: unknown = "could be anything";
let nothing: never; // Never returns
let empty: void = undefined;

// Arrays
let numbers: number[] = [1, 2, 3];
let strings: Array<string> = ["a", "b", "c"];

// Tuples
let person: [string, number, boolean] = ["John", 25, true];
```

### 🏗️ Interfaces & Types
```typescript
// Interface
interface User {
  id: number;
  name: string;
  email: string;
  isActive?: boolean; // Optional
  readonly createdAt: Date; // Readonly
}

// Type alias
type Status = "pending" | "approved" | "rejected";
type UserWithStatus = User & { status: Status };

// Index signature
interface StringDictionary {
  [key: string]: string;
}
```

### 🎯 Generics
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

// Generic constraints
function logLength<T extends { length: number }>(arg: T): T {
  console.log(arg.length);
  return arg;
}
```

### 🏛️ Classes
```typescript
class Person {
  private name: string;
  protected age: number;
  public email: string;
  readonly id: number;
  
  constructor(name: string, age: number, email: string) {
    this.name = name;
    this.age = age;
    this.email = email;
    this.id = Date.now();
  }
  
  public getName(): string {
    return this.name;
  }
  
  private validateEmail(email: string): boolean {
    return email.includes("@");
  }
}

// Abstract class
abstract class Shape {
  abstract getArea(): number;
  
  public getColor(): string {
    return "blue";
  }
}
```

### 🔧 Utility Types
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

// Record - creates object type
type ColorMap = Record<"red" | "green" | "blue", string>;
// { red: string; green: string; blue: string; }
```

### 🎭 Advanced Types
```typescript
// Conditional types
type IsString<T> = T extends string ? true : false;
type Test = IsString<string>; // true

// Mapped types
type Partial<T> = {
  [P in keyof T]?: T[P];
};

// Template literal types
type EventName<T extends string> = `on${Capitalize<T>}`;
type ClickEvent = EventName<"click">; // "onClick"

// Discriminated unions
type LoadingState = 
  | { status: "idle" }
  | { status: "loading" }
  | { status: "success"; data: any }
  | { status: "error"; error: string };
```

### 🔍 Type Guards
```typescript
// Type guard function
function isString(value: unknown): value is string {
  return typeof value === "string";
}

function isUser(value: unknown): value is User {
  return (
    typeof value === "object" &&
    value !== null &&
    "id" in value &&
    "name" in value
  );
}

// Usage
function processValue(value: unknown) {
  if (isString(value)) {
    // TypeScript knows value is string
    console.log(value.toUpperCase());
  }
}
```

### 🚀 Async & Promises
```typescript
// Promise typing
function fetchUser(id: number): Promise<User> {
  return fetch(`/api/users/${id}`)
    .then(response => response.json());
}

// Async/await typing
async function getUser(id: number): Promise<User> {
  const response = await fetch(`/api/users/${id}`);
  return response.json();
}

// Awaited utility type
type UserPromise = Promise<User>;
type User = Awaited<UserPromise>; // User
```

### ⚛️ React Integration
```typescript
// Component props
interface ButtonProps {
  label: string;
  onClick: () => void;
  disabled?: boolean;
  variant?: "primary" | "secondary";
}

function Button({ label, onClick, disabled = false, variant = "primary" }: ButtonProps) {
  return (
    <button 
      onClick={onClick} 
      disabled={disabled}
      className={`btn btn-${variant}`}
    >
      {label}
    </button>
  );
}

// Generic component
interface ListProps<T> {
  items: T[];
  renderItem: (item: T) => React.ReactNode;
}

function List<T>({ items, renderItem }: ListProps<T>) {
  return (
    <ul>
      {items.map((item, index) => (
        <li key={index}>{renderItem(item)}</li>
      ))}
    </ul>
  );
}
```

### 🔧 Configuration
```typescript
// tsconfig.json
{
  "compilerOptions": {
    "target": "ES2020",
    "module": "commonjs",
    "strict": true,
    "esModuleInterop": true,
    "skipLibCheck": true,
    "forceConsistentCasingInFileNames": true,
    "baseUrl": "./src",
    "paths": {
      "@/*": ["*"],
      "@/components/*": ["components/*"]
    }
  },
  "include": ["src/**/*"],
  "exclude": ["node_modules", "dist"]
}
```

### 📦 Module Declarations
```typescript
// Custom declaration file
declare module "my-library" {
  export interface Config {
    apiKey: string;
    baseUrl: string;
  }
  
  export function initialize(config: Config): void;
  export function getData(): Promise<any>;
}

// Global declarations
declare global {
  interface Window {
    myCustomProperty: string;
  }
}

// JSON imports
declare module "*.json" {
  const value: any;
  export default value;
}
```

### 🧪 Testing
```typescript
// Jest configuration
// jest.config.js
module.exports = {
  preset: 'ts-jest',
  testEnvironment: 'node',
  roots: ['<rootDir>/src'],
  testMatch: ['**/__tests__/**/*.ts', '**/?(*.)+(spec|test).ts']
};

// Test example
import { User } from '../src/types/user';

describe('User', () => {
  it('should create user with valid data', () => {
    const user: User = {
      id: 1,
      name: 'John Doe',
      email: 'john@example.com'
    };
    
    expect(user.name).toBe('John Doe');
  });
});
```

### 🚀 Performance Tips
- Use `skipLibCheck: true` for faster builds
- Enable `incremental: true` for incremental compilation
- Use project references for large codebases
- Avoid `any` type, use `unknown` instead
- Use type-only imports when possible
- Enable strict mode for better type safety

### 🛡️ Best Practices
- Use interfaces for object shapes
- Use type aliases for unions and primitives
- Enable strict mode for new projects
- Use generic constraints for type safety
- Implement proper error handling
- Use discriminated unions for state management
- Avoid circular dependencies
- Use type guards for runtime safety

---

*This cheatsheet provides quick reference for TypeScript development, covering types, generics, classes, utility types, and best practices for building type-safe applications.*
