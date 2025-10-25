# ⚛️ React Native Interview Notes (2025 Edition)

## 🧱 Section 3 — Native Modules & SDK Integration — Q61-Q90

---

## **Q61. What are Native Modules in React Native?**

**🧠 Concept**

Native Modules are JavaScript interfaces that allow React Native apps to access native platform features and APIs that aren't available in JavaScript.

**💻 Example**
```javascript
import { NativeModules } from 'react-native';

const { MyNativeModule } = NativeModules;

const result = await MyNativeModule.performNativeOperation();
console.log(result);
```

**💬 Explanation + Insight**

- **Bridge Communication** - JavaScript calls native code through the bridge
- **Platform Access** - Access device features like camera, GPS, sensors
- **Performance** - Native code runs faster than JavaScript
- **Custom Functionality** - Create platform-specific features
- **Event Emitters** - Native code can send events back to JavaScript

---

## **Q62. What are TurboModules in React Native?**

**🧠 Concept**

TurboModules are the new module system that provides lazy loading of native modules and better performance through JSI.

**💻 Example**
```javascript
import { TurboModuleRegistry } from 'react-native';

const MyTurboModule = TurboModuleRegistry.get('MyTurboModule');
const result = await MyTurboModule.performAsyncOperation();
```

**💬 Explanation + Insight**

- Lazy loading: Modules are loaded only when first accessed
- Better performance: Uses JSI for direct communication
- Type safety: Better TypeScript support with codegen
- Backward compatible: Old modules still work during transition
- Future: This is the future of React Native modules

---

## **Q63. What is the React Native Bridge?**

**🧠 Concept**

The React Native Bridge is a communication layer that allows JavaScript code to interact with native iOS and Android code.

**💻 Example**
```javascript
import { NativeModules } from 'react-native';

const { MyNativeModule } = NativeModules;
MyNativeModule.showAlert('Hello from JavaScript!');
```

**💬 Explanation + Insight**

- Communication layer: Connects JavaScript thread with native UI thread
- Asynchronous: All bridge communication is asynchronous for performance
- Performance impact: Bridge calls have overhead, so minimize them
- JSI: Newer architecture uses JavaScript Interface for better performance
- Native modules: Custom native code can be exposed through the bridge

---

## **Q64. What is JSI (JavaScript Interface) in React Native?**

**🧠 Concept**

JSI is a new architecture that allows direct synchronous communication between JavaScript and native code for better performance.

**💻 Example**
```javascript
import { NativeModules } from 'react-native';

const result = NativeModules.Calculator.add(5, 3);
console.log(result); // 8 - immediate result
```

**💬 Explanation + Insight**

- Direct communication: JavaScript can call native methods directly
- Synchronous: No need for callbacks or promises for simple operations
- Better performance: Eliminates bridge serialization overhead
- TurboModules: New module system built on top of JSI
- Future: JSI is the future of React Native architecture

---

## **Q65. What is Codegen in React Native?**

**🧠 Concept**

Codegen is a tool that automatically generates TypeScript definitions for native modules, providing type safety and better developer experience.

**💻 Example**
```javascript
// Generated TypeScript definitions
interface MyTurboModuleSpec extends TurboModule {
  performAsyncOperation(): Promise<string>;
  performSyncOperation(): string;
}

const MyTurboModule = TurboModuleRegistry.get<MyTurboModuleSpec>('MyTurboModule');
```

**💬 Explanation + Insight**

- Type safety: Generates TypeScript definitions for native modules
- Developer experience: Better autocomplete and error checking
- Automatic generation: No need to manually write type definitions
- TurboModules: Works with the new TurboModule system
- Performance: Helps catch errors at compile time

---

## **Q66. How do you create Android native modules?**

**🧠 Concept**

Android native modules are created by extending ReactContextBaseJavaModule and registering them in the ReactPackage.

**💻 Example**
```java
public class MyNativeModule extends ReactContextBaseJavaModule {
    @Override
    public String getName() {
        return "MyNativeModule";
    }

    @ReactMethod
    public void showAlert(String message) {
        // Native Android code here
    }
}
```

**💬 Explanation + Insight**

- ReactContextBaseJavaModule: Base class for native modules
- @ReactMethod: Exposes methods to JavaScript
- getName: Returns the module name used in JavaScript
- Registration: Must be registered in ReactPackage
- Performance: Native code runs faster than JavaScript

---

## **Q67. How do you create iOS native modules?**

**🧠 Concept**

iOS native modules are created by implementing RCTBridgeModule protocol and using RCT_EXPORT_METHOD to expose methods to JavaScript.

**💻 Example**
```objc
#import <React/RCTBridgeModule.h>

@interface MyNativeModule : NSObject <RCTBridgeModule>
@end

@implementation MyNativeModule

RCT_EXPORT_MODULE();

RCT_EXPORT_METHOD(showAlert:(NSString *)message) {
    // Native iOS code here
}

@end
```

**💬 Explanation + Insight**

- RCTBridgeModule: Protocol for native modules
- RCT_EXPORT_MODULE: Exposes the module to JavaScript
- RCT_EXPORT_METHOD: Exposes methods to JavaScript
- Registration: Automatically registered with autolinking
- Performance: Native code runs faster than JavaScript

---

## **Q68. What are Event Emitters in React Native?**

**🧠 Concept**

Event Emitters allow native modules to send events back to JavaScript, enabling real-time communication from native to JavaScript.

**💻 Example**
```javascript
import { NativeEventEmitter, NativeModules } from 'react-native';

const { MyNativeModule } = NativeModules;
const eventEmitter = new NativeEventEmitter(MyNativeModule);

useEffect(() => {
    const subscription = eventEmitter.addListener('MyEvent', (event) => {
        console.log('Received event:', event);
    });

    return () => subscription.remove();
}, []);
```

**💬 Explanation + Insight**

- Real-time communication: Native code can send events to JavaScript
- Event listeners: JavaScript can listen for native events
- Cleanup: Always remove event listeners to prevent memory leaks
- Use cases: Progress updates, sensor data, notifications
- Performance: Efficient way to communicate from native to JavaScript

---

## **Q69. How do you handle Promises in React Native native modules?**

**🧠 Concept**

Native modules can return Promises to JavaScript, allowing for async operations and better error handling.

**💻 Example**
```javascript
// JavaScript side
const result = await MyNativeModule.performAsyncOperation();
console.log(result);

// Native side (Android)
@ReactMethod
public void performAsyncOperation(Promise promise) {
    try {
        String result = doAsyncWork();
        promise.resolve(result);
    } catch (Exception e) {
        promise.reject("ERROR", e.getMessage());
    }
}
```

**💬 Explanation + Insight**

- Async operations: Handle long-running native operations
- Error handling: Use promise.reject for errors
- Success: Use promise.resolve for successful results
- JavaScript: Use await/async for cleaner code
- Performance: Non-blocking operations

---

## **Q70. What is JNI in React Native Android?**

**🧠 Concept**

JNI (Java Native Interface) allows Java code to call native C/C++ code, enabling high-performance operations in React Native.

**💻 Example**
```java
public class MyNativeModule extends ReactContextBaseJavaModule {
    static {
        System.loadLibrary("mynative");
    }

    @ReactMethod
    public void performNativeOperation(Promise promise) {
        try {
            String result = nativePerformOperation();
            promise.resolve(result);
        } catch (Exception e) {
            promise.reject("ERROR", e.getMessage());
        }
    }

    private native String nativePerformOperation();
}
```

**💬 Explanation + Insight**

- High performance: C/C++ code runs faster than Java
- Native libraries: Access to native C/C++ libraries
- System.loadLibrary: Loads native libraries
- native keyword: Declares native methods
- Use cases: Image processing, cryptography, mathematical operations

---

## **Q71. How do you integrate third-party SDKs in React Native?**

**🧠 Concept**

Third-party SDKs are integrated by adding native dependencies and creating bridge modules to expose SDK functionality to JavaScript.

**💻 Example**
```javascript
// JavaScript usage
import { NativeModules } from 'react-native';

const { AnalyticsSDK } = NativeModules;
AnalyticsSDK.trackEvent('user_action', { userId: '123' });
```

**💬 Explanation + Insight**

- Native dependencies: Add SDKs to native projects
- Bridge modules: Create JavaScript interfaces for SDKs
- Autolinking: Modern React Native handles linking automatically
- Configuration: Configure SDKs in native code
- Documentation: Follow SDK integration guides

---

## **Q72. What is autolinking in React Native?**

**🧠 Concept**

Autolinking is React Native's automatic dependency linking system that automatically links native dependencies without manual configuration.

**💻 Example**
```javascript
// react-native.config.js
module.exports = {
  dependencies: {
    'react-native-vector-icons': {
      platforms: {
        ios: {
          project: './ios/VectorIcons.xcodeproj',
        },
        android: {
          sourceDir: './android/',
        },
      },
    },
  },
};
```

**💬 Explanation + Insight**

- Automatic linking: Automatically links native dependencies
- Configuration: Minimal configuration required
- Platform support: Works on both iOS and Android
- Native modules: Handles native module linking
- Performance: Optimizes linking process

---

## **Q73. How do you debug native modules in React Native?**

**🧠 Concept**

Native modules can be debugged using native debugging tools, console logging, and React Native debugging tools.

**💻 Example**
```javascript
// JavaScript debugging
console.log('Calling native module');
const result = await MyNativeModule.performOperation();
console.log('Native module result:', result);
```

**💬 Explanation + Insight**

- Console logging: Use console.log for debugging
- Native debugging: Use Xcode/Android Studio debuggers
- Flipper: Use Flipper for advanced debugging
- Error handling: Implement proper error handling
- Testing: Test native modules thoroughly

---

## **Q74. What are the performance considerations for native modules?**

**🧠 Concept**

Native modules have performance implications including bridge overhead, memory usage, and thread management.

**💻 Example**
```javascript
// Minimize bridge calls
const results = await MyNativeModule.performBatchOperations(data);
// Instead of multiple individual calls
```

**💬 Explanation + Insight**

- Bridge overhead: Minimize bridge calls for better performance
- Memory usage: Be mindful of memory usage in native code
- Thread management: Native code runs on different threads
- Batch operations: Group operations to reduce bridge calls
- Profiling: Use profiling tools to identify bottlenecks

---

## **Q75. How do you handle errors in native modules?**

**🧠 Concept**

Native modules should implement proper error handling using try-catch blocks, promise rejection, and error boundaries.

**💻 Example**
```javascript
try {
    const result = await MyNativeModule.performOperation();
    return result;
} catch (error) {
    console.error('Native module error:', error);
    throw error;
}
```

**💬 Explanation + Insight**

- Error handling: Implement proper error handling
- Promise rejection: Use promise.reject for errors
- Error boundaries: Use React error boundaries
- Logging: Log errors for debugging
- User experience: Provide meaningful error messages

---

## **Q76. What are the differences between Native Modules and TurboModules?**

**🧠 Concept**

TurboModules are the new module system that provides better performance, lazy loading, and type safety compared to traditional Native Modules.

**💻 Example**
```javascript
// Traditional Native Module
import { NativeModules } from 'react-native';
const { MyModule } = NativeModules;

// TurboModule
import { TurboModuleRegistry } from 'react-native';
const MyTurboModule = TurboModuleRegistry.get('MyTurboModule');
```

**💬 Explanation + Insight**

- Performance: TurboModules use JSI for better performance
- Lazy loading: TurboModules are loaded only when needed
- Type safety: Better TypeScript support with codegen
- Backward compatible: Old modules still work
- Future: TurboModules are the future of React Native

---

## **Q77. How do you create custom native modules for specific use cases?**

**🧠 Concept**

Custom native modules are created by implementing platform-specific code and exposing it through the React Native bridge.

**💻 Example**
```javascript
// Custom module for file operations
const FileModule = {
    async readFile(path) {
        return await NativeModules.FileModule.readFile(path);
    },
    
    async writeFile(path, content) {
        return await NativeModules.FileModule.writeFile(path, content);
    }
};
```

**💬 Explanation + Insight**

- Custom functionality: Create modules for specific use cases
- Platform-specific: Implement different code for iOS and Android
- Bridge exposure: Expose functionality through the bridge
- Testing: Test custom modules thoroughly
- Documentation: Document custom module APIs

---

## **Q78. What are the best practices for native module development?**

**🧠 Concept**

Best practices for native module development include proper error handling, performance optimization, and following React Native conventions.

**💻 Example**
```javascript
// Good practice: Proper error handling
const MyModule = {
    async performOperation(data) {
        try {
            validateInput(data);
            const result = await NativeModules.MyModule.performOperation(data);
            return result;
        } catch (error) {
            console.error('Operation failed:', error);
            throw new Error('Operation failed');
        }
    }
};
```

**💬 Explanation + Insight**

- Error handling: Implement proper error handling
- Input validation: Validate inputs before processing
- Performance: Optimize for performance
- Documentation: Document module APIs
- Testing: Write comprehensive tests

---

## **Q79. How do you handle memory management in native modules?**

**🧠 Concept**

Memory management in native modules involves proper resource cleanup, avoiding memory leaks, and managing object lifecycles.

**💻 Example**
```javascript
// Proper cleanup
useEffect(() => {
    const subscription = eventEmitter.addListener('event', handler);
    
    return () => {
        subscription.remove();
    };
}, []);
```

**💬 Explanation + Insight**

- Resource cleanup: Always clean up resources
- Memory leaks: Avoid memory leaks
- Object lifecycle: Manage object lifecycles properly
- Event listeners: Remove event listeners
- Native resources: Clean up native resources

---

## **Q80. What are the security considerations for native modules?**

**🧠 Concept**

Native modules should implement proper security measures including input validation, secure storage, and secure communication.

**💻 Example**
```javascript
// Secure input validation
const MySecureModule = {
    async processData(data) {
        if (!isValidInput(data)) {
            throw new Error('Invalid input');
        }
        
        return await NativeModules.MySecureModule.processData(data);
    }
};
```

**💬 Explanation + Insight**

- Input validation: Validate all inputs
- Secure storage: Use secure storage for sensitive data
- Secure communication: Use secure communication protocols
- Authentication: Implement proper authentication
- Data protection: Protect sensitive data

---

## **Q81. How do you test native modules in React Native?**

**🧠 Concept**

Native modules can be tested using unit tests, integration tests, and native testing frameworks.

**💻 Example**
```javascript
// Unit test
describe('MyNativeModule', () => {
    test('should perform operation correctly', async () => {
        const result = await MyNativeModule.performOperation('test');
        expect(result).toBe('expected result');
    });
});
```

**💬 Explanation + Insight**

- Unit testing: Test individual module functions
- Integration testing: Test module integration
- Mocking: Mock native modules for testing
- Error testing: Test error scenarios
- Performance testing: Test module performance

---

## **Q82. What are the common pitfalls in native module development?**

**🧠 Concept**

Common pitfalls include memory leaks, improper error handling, thread safety issues, and performance problems.

**💻 Example**
```javascript
// Bad practice: Memory leak
useEffect(() => {
    const subscription = eventEmitter.addListener('event', handler);
    // Missing cleanup - causes memory leak
}, []);

// Good practice: Proper cleanup
useEffect(() => {
    const subscription = eventEmitter.addListener('event', handler);
    
    return () => {
        subscription.remove();
    };
}, []);
```

**💬 Explanation + Insight**

- Memory leaks: Always clean up resources
- Error handling: Implement proper error handling
- Thread safety: Be aware of thread safety issues
- Performance: Optimize for performance
- Testing: Test thoroughly

---

## **Q83. How do you optimize native module performance?**

**🧠 Concept**

Native module performance can be optimized by minimizing bridge calls, using efficient algorithms, and proper resource management.

**💻 Example**
```javascript
// Optimize: Batch operations
const results = await MyNativeModule.performBatchOperations(data);

// Instead of multiple individual calls
for (const item of data) {
    await MyNativeModule.performOperation(item);
}
```

**💬 Explanation + Insight**

- Batch operations: Group operations to reduce bridge calls
- Efficient algorithms: Use efficient algorithms
- Resource management: Manage resources properly
- Profiling: Use profiling tools
- Optimization: Optimize critical paths

---

## **Q84. What are the differences between iOS and Android native modules?**

**🧠 Concept**

iOS and Android native modules differ in implementation, APIs, and platform-specific features.

**💻 Example**
```javascript
// Platform-specific implementation
import { Platform } from 'react-native';

const MyModule = Platform.OS === 'ios' 
    ? NativeModules.MyIOSModule 
    : NativeModules.MyAndroidModule;
```

**💬 Explanation + Insight**

- Implementation: Different implementation approaches
- APIs: Different platform APIs
- Features: Platform-specific features
- Testing: Test on both platforms
- Maintenance: Maintain platform-specific code

---

## **Q85. How do you handle async operations in native modules?**

**🧠 Concept**

Async operations in native modules are handled using Promises, callbacks, and proper thread management.

**💻 Example**
```javascript
// Promise-based async operation
const result = await MyNativeModule.performAsyncOperation();

// Callback-based async operation
MyNativeModule.performAsyncOperation((error, result) => {
    if (error) {
        console.error('Error:', error);
    } else {
        console.log('Result:', result);
    }
});
```

**💬 Explanation + Insight**

- Promises: Use Promises for async operations
- Callbacks: Use callbacks for async operations
- Thread management: Manage threads properly
- Error handling: Handle errors in async operations
- Performance: Consider performance implications

---

## **Q86. What are the debugging tools for native modules?**

**🧠 Concept**

Native modules can be debugged using various tools including console logging, native debuggers, and React Native debugging tools.

**💻 Example**
```javascript
// Console logging
console.log('Debug: Calling native module');
const result = await MyNativeModule.performOperation();
console.log('Debug: Native module result:', result);
```

**💬 Explanation + Insight**

- Console logging: Use console.log for debugging
- Native debuggers: Use Xcode/Android Studio debuggers
- Flipper: Use Flipper for advanced debugging
- Error tracking: Use error tracking tools
- Performance profiling: Use performance profiling tools

---

## **Q87. How do you handle platform-specific native modules?**

**🧠 Concept**

Platform-specific native modules are handled by creating separate implementations for iOS and Android.

**💻 Example**
```javascript
// Platform-specific module
import { Platform } from 'react-native';

const MyPlatformModule = Platform.OS === 'ios' 
    ? NativeModules.MyIOSModule 
    : NativeModules.MyAndroidModule;

const result = await MyPlatformModule.performOperation();
```

**💬 Explanation + Insight**

- Platform detection: Use Platform.OS to detect platform
- Separate implementations: Create separate implementations
- Testing: Test on both platforms
- Maintenance: Maintain platform-specific code
- Documentation: Document platform differences

---

## **Q88. What are the migration strategies for native modules?**

**🧠 Concept**

Migration strategies for native modules include gradual migration, backward compatibility, and testing strategies.

**💻 Example**
```javascript
// Gradual migration
const MyModule = TurboModuleRegistry.get('MyTurboModule') 
    || NativeModules.MyNativeModule;

const result = await MyModule.performOperation();
```

**💬 Explanation + Insight**

- Gradual migration: Migrate gradually to new systems
- Backward compatibility: Maintain backward compatibility
- Testing: Test migration thoroughly
- Documentation: Document migration process
- Support: Provide support during migration

---

## **Q89. How do you handle versioning in native modules?**

**🧠 Concept**

Versioning in native modules involves managing API changes, backward compatibility, and proper versioning strategies.

**💻 Example**
```javascript
// Version checking
const MyModule = NativeModules.MyModule;

if (MyModule.getVersion() >= 2.0) {
    // Use new API
    const result = await MyModule.performOperationV2(data);
} else {
    // Use old API
    const result = await MyModule.performOperation(data);
}
```

**💬 Explanation + Insight**

- API versioning: Manage API changes
- Backward compatibility: Maintain backward compatibility
- Version checking: Check module versions
- Migration: Plan for API changes
- Documentation: Document version changes

---

## **Q90. What are the future trends in native module development?**

**🧠 Concept**

Future trends include TurboModules, JSI, improved type safety, and better performance optimizations.

**💻 Example**
```javascript
// Future: Better type safety
interface MyTurboModuleSpec extends TurboModule {
    performOperation(data: string): Promise<string>;
}

const MyTurboModule = TurboModuleRegistry.get<MyTurboModuleSpec>('MyTurboModule');
```

**💬 Explanation + Insight**

- TurboModules: New module system
- JSI: JavaScript Interface for better performance
- Type safety: Improved TypeScript support
- Performance: Better performance optimizations
- Developer experience: Improved developer experience

---

*This section covers Native Modules, TurboModules, React Native Bridge, JSI, Codegen, Android native modules (Java/Kotlin), iOS native modules (Objective-C/Swift), event emitters, promises, async operations, JNI, SDK integration, autolinking, and debugging.*
