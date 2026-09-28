---
sidebar_label: "React Native Internals"
---
# 📱 React Native Internals

---

## 1. ⚛️ How React Native Works Internally

React Native allows you to build mobile apps using React, but instead of rendering to the web DOM, it renders to native mobile components. Understanding how React Native works internally helps you write better mobile apps, debug performance issues, and understand the bridge between JavaScript and native code. This knowledge is crucial for senior developers - it helps you understand why certain patterns work better, how to optimize React Native applications, and how to debug complex issues.

---

### 🔹 ⚛️ React Native Architecture

### 🔹 Core Concept

React Native uses the same React principles you know from web development, but with a key difference: instead of rendering to HTML elements, it renders to native mobile components.

**Three-Layer Architecture:**

* **JavaScript Layer (JS Thread)**: Your React code runs here - components, state, props, hooks all work the same way as React web. This is where your business logic, state management, and React component tree live. It runs in a JavaScript engine (JavaScriptCore on iOS, V8/Hermes on Android).

* **Native Layer (UI Thread)**: The actual native UI components live here - iOS uses UIKit, Android uses Android Views. This is where platform-specific UI rendering happens. Each platform has its own main/UI thread that handles all UI operations.

* **Bridge/JSI Layer**: This is the communication layer between JavaScript and native code - think of it as a translator that converts JavaScript calls into native API calls. In the old architecture, this is the asynchronous bridge. In the new architecture, this is JSI (JavaScript Interface) for direct communication.

### 🔹 How It Works

When you write React Native code:

1. **You write JSX** just like React web - `<View>`, `<Text>`, `<Button>` etc.

2. **React Native transforms** your JSX into a description of what the UI should look like

3. **The Bridge serializes** this description and sends it to the native thread (old architecture) or **JSI directly updates** native components (new architecture)

4. **Native code creates** actual iOS/Android UI components based on that description

5. **User interactions** (taps, swipes) go back through the bridge/JSI to your JavaScript code

### 🔹 App Startup Process

Here's how a React Native app starts up - understanding this helps you see how everything fits together:

**1. Native App Launch:**

* iOS/Android app starts (native process)

* Native code initializes the JavaScript engine

* JavaScriptCore (iOS) or Hermes/V8 (Android) is loaded

* Native modules are registered

**2. JavaScript Bundle Loading:**

* Metro bundler creates a JavaScript bundle

* Bundle is loaded into the JavaScript engine

* Your React Native code starts executing

* React Native runtime initializes

**3. Root Component Mount:**

* `AppRegistry.registerComponent()` registers your root component

* React Native creates the root React element

* Initial render happens on JavaScript thread

* Shadow tree is created

**4. Native UI Creation:**

* Shadow tree is sent to native thread (via bridge or JSI)

* Native views are created and mounted

* UI appears on screen

* App is ready for user interaction

**5. Event Loop Starts:**

* JavaScript event loop begins processing events

* Native events (touches, timers) are queued

* React Native processes events and updates UI

* App enters interactive state

### 🔹 Thread Architecture Details

**JavaScript Thread:**

* Single-threaded event loop (just like web JavaScript)

* Runs all your React code, business logic, and JavaScript execution

* Processes events from the native thread

* Can be blocked by heavy computations - watch out, this affects UI responsiveness

* Uses a message queue to receive events from native

**UI Thread (Main Thread):**

* Platform-specific main thread (iOS main thread, Android main thread)

* Handles all UI rendering and user interactions

* Must not be blocked - the catch is if you block it, the UI freezes

* Receives updates from the JavaScript thread

* Processes touch events, animations, and rendering

**Background Threads:**

* Native modules can create background threads

* Used for heavy work like image processing or network requests

* Can't directly update UI - must go through the UI thread

* Helps keep JavaScript and UI threads responsive

**Thread Communication:**

* **Old Architecture**: Asynchronous message passing via bridge

* **New Architecture**: Direct calls via JSI (can be synchronous)

* Events flow: UI Thread → Bridge/JSI → JavaScript Thread

* Updates flow: JavaScript Thread → Bridge/JSI → UI Thread

### 🔹 Component Mapping

**React Native Components → Native Components:**

**iOS Mapping:**

* `<View>` → `UIView` (base container)

* `<Text>` → `UILabel` (text display)

* `<TextInput>` → `UITextField` or `UITextView` (text input)

* `<Image>` → `UIImageView` (image display)

* `<ScrollView>` → `UIScrollView` (scrollable container)

* `<FlatList>` → `UICollectionView` (optimized list)

* `<Button>` → `UIButton` (button control)

**Android Mapping:**

* `<View>` → `ViewGroup` (usually `ReactViewGroup`)

* `<Text>` → `TextView` (text display)

* `<TextInput>` → `EditText` (text input)

* `<Image>` → `ImageView` (image display)

* `<ScrollView>` → `ScrollView` (scrollable container)

* `<FlatList>` → `RecyclerView` (optimized list)

* `<Button>` → `Button` or `AppCompatButton` (button control)

### 🔹 Platform Differences

**iOS Specifics:**

* Uses UIKit framework (or SwiftUI in newer versions)

* Auto Layout for positioning (or frame-based layout)

* Core Animation for animations

* Metal/OpenGL for hardware-accelerated rendering

* Objective-C or Swift for native modules

**Android Specifics:**

* Uses Android View system

* ConstraintLayout or LinearLayout for positioning

* Android Animation framework

* Hardware acceleration via OpenGL ES

* Java or Kotlin for native modules

**Cross-Platform Considerations:**

* Same JavaScript code works on both platforms

* Platform-specific code can be added using `Platform.OS` checks

* Platform-specific files: `Component.ios.js` and `Component.android.js`

* Some components behave differently (e.g., `TextInput` keyboard behavior)

* Styling may render slightly differently due to platform conventions

### 🔹 Architecture Evolution

**Old Architecture (Bridge-based):**

* Asynchronous bridge for all communication

* Serialization overhead for every call

* Modules loaded at startup

* Slower performance, especially for animations

* Still used in React Native < 0.68 (or when new architecture not enabled)

**New Architecture (JSI-based):**

* JSI for direct communication

* Fabric for rendering

* TurboModules for native modules

* Better performance, synchronous calls when needed

* Available from React Native 0.68+ (opt-in)

* Will become default in future versions

📌 **In simple terms**: React Native runs your React code in JavaScript, uses a bridge (old) or JSI (new) to communicate with native code, and renders to real native mobile components instead of HTML. The architecture separates JavaScript execution from native UI rendering, keeping the UI responsive. You write once, it works on both iOS and Android, though platform-specific optimizations are possible.

---

### 🔹 💡 The Bridge (Old Architecture)

### 🔹 What is the Bridge?

The bridge is like a message passing system between JavaScript and native code. It's asynchronous, which means JavaScript and native code don't block each other.

* **Asynchronous Communication**: JavaScript sends messages to native, native sends messages back - neither side waits for the other

* **Serialization**: Data gets converted to JSON-like format when crossing the bridge - this is necessary because JavaScript and native code use different data types

* **Message Queue**: Messages are queued and processed in batches - this is efficient but can add latency

### 🔹 How Bridge Communication Works

The bridge works by sending messages asynchronously between JavaScript and native code, and it has to convert data along the way. Here's how it works step by step:

**Step-by-Step Process:**

**1. You call native from JavaScript:**

* You call a native module method from your JavaScript code

* Example: `NativeModules.Camera.takePicture(options)`

* This doesn't run right away - it gets queued up

**2. Data gets converted:**

* The bridge converts your JavaScript data (objects, arrays, strings, numbers) into JSON-like format

* This happens because JavaScript and native code use different data types

* Example: Your JavaScript object `{width: 100, height: 200}` becomes a JSON string

* The catch is this conversion takes time - can be slow for large objects

**3. Message gets sent:**

* The converted message is added to a message queue

* Messages are batched together for efficiency

* The queue processes messages asynchronously

**4. Native code runs:**

* Native code receives the message from the queue

* Converts the JSON back into native data types

* Runs the native method (like taking a picture with the camera)

* This happens on the native thread - doesn't block your JavaScript

**5. Response comes back:**

* Native code converts the result (like image data or an error) back to JSON

* Sends it back through the bridge (same conversion process)

* Gets added to the response queue

**6. JavaScript gets the response:**

* Your JavaScript code receives the response

* Usually through a callback or promise

* The conversion back to JavaScript happens automatically

* Example:

```javascript
NativeModules.Camera.takePicture(options, (error, image) => {
  // This callback runs when native code responds
  // image is deserialized from native format
});

```

**Performance Implications:**

* Converting data back and forth adds delay (usually 1-5ms per call)

* Large objects take longer to convert (gets slower as size grows)

* Lots of calls create queue buildup - watch out, this can cause delays

* This is why animations can feel janky with the old bridge (60fps means 60 calls per second, which adds up to significant overhead)

**Message Batching:**

* Bridge batches multiple messages together for efficiency

* Messages are collected during a JavaScript execution cycle

* Batched messages sent together to native thread

* Reduces overhead but can add slight delay

* Example: Multiple `setState` calls in one render cycle are batched

**Error Handling:**

* Errors in native code are serialized and sent back to JavaScript

* JavaScript errors can be sent to native for logging

* Bridge handles error serialization automatically

* Errors in bridge communication itself can cause app crashes

* Example: If native module throws exception, it's caught and sent as error object to JavaScript

### 🔹 Bridge Limitations

Here's why the new architecture was needed - these are the main issues with the bridge:

**1. Converting Data Takes Time:**

* Converting data to/from JSON takes time

* Can be slow for large objects like images or big arrays

* Every call has this conversion cost

* Example: Sending a large image through the bridge is slow

**2. Everything is Async:**

* Everything is async, even when you need synchronous access

* This can make some things tricky - like reading layout measurements

* You always need callbacks or promises

* Example: You can't synchronously read view dimensions - must use a callback

**3. Performance Bottleneck:**

* Lots of calls (like animations) can be slow

* Bridge overhead adds up with many calls

* Can cause janky animations (dropped frames)

* Example: 60fps animation means 60 calls per second, which creates lots of bridge overhead

**4. Message Queue Delays:**

* Messages are queued and batched

* Can add delay even for simple operations

* Not great for real-time operations

* Example: Touch events might feel a bit delayed

**5. Memory Usage:**

* Serialized data takes memory (JSON strings in memory)

* Large objects in queue consume memory (can accumulate)

* Can cause memory pressure (especially with images or large arrays)

* Example: Queueing many large images can cause memory issues

* Bridge maintains message queues on both sides (JavaScript and native)

**Bridge Protocol:**

* Defines how data is serialized/deserialized

* Supports specific data types: strings, numbers, booleans, objects, arrays, null

* Functions are converted to callback IDs (not passed directly)

* Dates are converted to numbers (timestamps)

* Special handling for native modules and view managers

**Bridge Message Format:**

* Messages have a structure: `[moduleID, methodID, params, callbackID]`

* Module ID identifies which native module to call

* Method ID identifies which method on that module

* Params are serialized arguments

* Callback ID is used for async responses

**Example Bridge Call:**

```javascript
// JavaScript side
NativeModules.Camera.takePicture({ quality: 0.8 }, (error, image) => {
  console.log(image);
});

// Bridge serializes to something like:
// [CameraModuleID, takePictureMethodID, {quality: 0.8}, callbackID123]

// Native side receives and deserializes
// Executes: CameraModule.takePicture({quality: 0.8}, callbackID123)
// When done, sends response back: [callbackID123, null, imageData]
```

**Bridge Limitations in Practice:**

* **Animation Performance**: 60fps animations require 60 updates/sec, bridge overhead causes frame drops

* **Touch Responsiveness**: Touch events must cross bridge, can feel laggy

* **Layout Measurements**: Reading view dimensions requires async callback, complicates code

* **Synchronous Operations**: Impossible to do truly synchronous operations (e.g., reading from storage)

* **Large Data Transfer**: Images, videos, large arrays are slow to transfer

📌 **In simple terms**: The bridge is an asynchronous message passing system between JavaScript and native code. It serializes data when crossing between the two worlds, which works but can be slow for frequent or large data transfers. Messages are batched for efficiency, but this adds latency. The bridge protocol defines how data types are converted, and errors are handled through serialization.

---

### 🔹 📋 JavaScript Interface (JSI) - New Architecture

### 🔹 What is JSI?

JSI (JavaScript Interface) is the new architecture that allows direct communication between JavaScript and native code, eliminating the need for serialization and enabling synchronous calls when needed.

* **Direct Function Calls**: JavaScript can directly call native functions without going through a message queue

* **No Serialization**: Data is passed directly without conversion - much faster

* **Synchronous When Needed**: You can make synchronous calls when necessary, not just async

* **Better Performance**: Eliminates the bridge overhead, especially important for animations and high-frequency updates

### 🔹 How JSI Works

JSI lets JavaScript talk directly to native code without going through a message queue. Here's how it works:

**Step-by-Step Process:**

**1. Native modules register:**

* Native code registers its functions with JSI

* Functions become available to JavaScript

* Registration happens at startup or when needed

* Example: Camera module registers `takePicture` function

**2. JavaScript gets direct access:**

* JavaScript gets a direct reference to the native function

* No data conversion needed - it's a direct memory reference

* This is much faster than bridge messages

* Example: `const takePicture = NativeModules.Camera.takePicture;`

**3. Direct call:**

* When you call the function, it runs immediately in native code

* No message queue, no batching delay

* Function runs synchronously (if designed that way)

* Example: `const result = takePicture(options);` - runs immediately

**4. No data conversion:**

* Data is passed directly, no conversion needed

* JavaScript objects map directly to native objects

* Much faster than JSON conversion

* Example: Passing an object is instant, no conversion

**5. Synchronous or async:**

* You can choose based on what you need

* Synchronous for simple operations (like reading layout)

* Async for long-running operations (like network requests)

* Example:

```javascript
// Synchronous - immediate result
const dimensions = view.measureSync();

// Async - for long operations
const image = await camera.takePictureAsync();

```

**Performance Benefits:**

* No data conversion overhead (much faster - 10-100x improvement for frequent calls)

* No message queue delays (runs immediately)

* Synchronous access when you need it (better for animations)

* Direct memory access (more efficient - no data copying)

**How JSI Works Under the Hood:**

**1. Host Objects:**

* JSI uses "host objects" - these are JavaScript objects that are backed by native C++ objects

* When you access a property, it calls native code directly

* No data conversion - native code reads/writes directly to JavaScript memory

* Example: `view.measure()` directly calls the native `measure()` function

**2. Function Binding:**

* Native functions are connected to JavaScript at runtime

* Functions become regular JavaScript functions you can call

* You can call them like any other JavaScript function

* Type information is preserved (better than the bridge)

**3. Memory Management:**

* JSI uses shared memory between JavaScript and native

* No copying of data structures (just passing references)

* JavaScript garbage collector manages memory

* Native code needs to be careful not to hold references too long

**4. Thread Safety:**

* JSI calls can happen on any thread

* You need to make sure thread safety in native code

* JavaScript engine is single-threaded, but native can be multi-threaded

* You have synchronization tools available for thread-safe operations

**Example JSI Usage:**

```javascript
// Old bridge way (async)
UIManager.measure(nodeHandle, (x, y, width, height) => {
  console.log(width, height);
});

// New JSI way (can be sync)
const { width, height } = UIManager.measureSync(nodeHandle);
console.log(width, height); // Immediate result, no callback needed
```

**JSI vs Bridge Comparison:**

| Aspect | Bridge (Old) | JSI (New) |
|--------|--------------|-----------|
| Communication | Async message queue | Direct function calls |
| Serialization | Required (JSON) | Not required |
| Speed | Slower (1-5ms overhead) | Faster (microseconds) |
| Synchronous | Not possible | Possible |
| Memory | Copies data | Shares memory |
| Type Safety | Limited | Better |

### 🔹 JSI Benefits

* **Faster**: No serialization overhead means much faster communication (10-100x for frequent operations)

* **Type safety**: Better type checking and error handling (compile-time validation)

* **Synchronous access**: Can access native APIs synchronously when needed (like reading layout measurements, immediate property access)

* **Lower latency**: Direct calls eliminate queue delays (critical for animations and touch handling)

* **Memory efficient**: Shared memory instead of copying (important for large data structures)

* **Future-proof**: This is the foundation for React Native's new architecture (Fabric, TurboModules)

**JSI Limitations:**

* **Complexity**: More complex to implement native modules - you need to handle memory management
* **Thread Safety**: You need to make sure thread safety in native code
* **Debugging**: Can be trickier to debug - direct calls mean no message queue to inspect
* **Migration**: Requires rewriting native modules - not backward compatible with bridge modules

📌 **In simple terms**: JSI allows JavaScript to directly call native functions without serialization or message queues. It uses host objects and shared memory for efficient communication. It's faster, supports synchronous calls, and is the foundation of React Native's new architecture. However, it requires more careful memory management and thread safety considerations.

---

### 🔹 🎨 Fabric - New Rendering System

### 🔹 What is Fabric?

Fabric is React Native's new rendering system that uses JSI for better performance and enables synchronous UI updates.

* **New Renderer**: Replaces the old rendering system with one built on JSI

* **Synchronous Updates**: Can update the UI synchronously when needed - important for smooth animations

* **Better Performance**: More efficient rendering, especially for complex UIs

* **Improved Debugging**: Better tools for debugging rendering issues

### 🔹 How Fabric Works

1. **React renders**: Your React components render as usual

2. **Shadow Tree**: Fabric creates a "shadow tree" - think of it as a JavaScript representation of the native UI tree

3. **Direct updates**: Changes are applied directly to native components using JSI

4. **Synchronous when needed**: Layout calculations and updates can happen synchronously when you need them

5. **Better batching**: More efficient batching of updates

### 🔹 Fabric Rendering Phases

**1. Render Phase (JavaScript Thread):**

* React components execute and create element tree

* Reconciliation happens (comparing old vs new tree)

* Fabric creates/updates shadow tree nodes

* This phase can be interrupted (concurrent rendering)

**2. Commit Phase (JavaScript Thread):**

* Changes are committed to shadow tree

* Layout calculations happen (Yoga)

* Operations are batched and prepared

* Shadow tree is marked as ready for native

**3. Mount/Update Phase (Native Thread):**

* Native code reads shadow tree via JSI

* Native views are created, updated, or deleted

* View hierarchy is updated

* Layout is applied to native views

* This phase is synchronous and cannot be interrupted

**4. Paint Phase (Native Thread):**

* Native views are painted to screen

* Platform-specific rendering happens

* Animations are applied

* User sees the updated UI

### 🔹 Priority System

Fabric supports priority-based updates, allowing React Native to prioritize urgent updates:

**Update Priorities:**

* **Synchronous**: Highest priority, blocks until complete (critical updates)

* **User-blocking**: High priority, should complete quickly (user interactions)

* **Normal**: Default priority (regular state updates)

* **Low**: Low priority, can be deferred (background updates)

**Priority Example:**

```javascript
// High priority - user interaction
onPress={() => {
  // This update gets high priority
  setState(newState);
}}

// Low priority - background data
useEffect(() => {
  // This update can be deferred
  fetchData().then(setData);
}, []);
```

### 🔹 Concurrent Rendering Support

Fabric enables React 18 concurrent features:

* **Concurrent Mode**: Can interrupt rendering for higher priority work

* **Suspense**: Better handling of async operations

* **Transitions**: Mark updates as non-urgent (can be interrupted)

* **Automatic Batching**: Multiple state updates batched automatically

**Example:**

```javascript
import { startTransition } from 'react';

// Urgent update
setUrgentState(newValue);

// Non-urgent update (can be interrupted)
startTransition(() => {
  setNonUrgentState(newValue);
});
```

### 🔹 Fabric Benefits

* **Smoother animations**: Synchronous updates mean animations can be smoother (60fps achievable)

* **Better performance**: More efficient rendering pipeline (less overhead, better batching)

* **Improved debugging**: Better tools to see what's happening in the render process (React DevTools integration)

* **Future features**: Enables new React features like concurrent rendering, Suspense, transitions

* **Priority-based updates**: Can prioritize urgent updates over less important ones (better UX)

* **Synchronous when needed**: Critical updates can be synchronous (no frame drops)

* **Better memory management**: More efficient memory usage (shared memory via JSI)

**Fabric vs Old Renderer:**

| Aspect | Old Renderer | Fabric |
|--------|--------------|--------|
| Communication | Bridge (async) | JSI (sync possible) |
| Serialization | Required | Not required |
| Update Priority | No priority | Priority-based |
| Concurrent Features | Limited | Full support |
| Performance | Slower | Faster |
| Animations | Can be janky | Smooth |

📌 **In simple terms**: Fabric is the new rendering system that uses JSI for direct, synchronous UI updates. It supports priority-based updates, concurrent rendering, and makes animations smoother. The rendering process has distinct phases (render, commit, mount, paint), and Fabric can prioritize urgent updates over less important ones for better user experience.

---

### 🔹 📦 TurboModules - New Native Module System

### 🔹 What are TurboModules?

TurboModules are the new native module system that uses JSI instead of the bridge, providing better performance and type safety.

* **JSI-based**: Uses JSI for direct communication instead of the bridge

* **Lazy loading**: Modules are loaded only when needed, not all at startup

* **Type safety**: Better type checking and validation

* **Synchronous calls**: Can make synchronous calls when needed

### 🔹 How TurboModules Work

1. **Module registration**: Native modules register with TurboModule system

2. **Lazy loading**: Modules aren't loaded until JavaScript actually uses them

3. **Direct access**: JavaScript gets direct access via JSI

4. **Type checking**: Better validation of parameters and return values

5. **Performance**: Much faster than bridge-based modules

### 🔹 TurboModule Registration

**1. Code Generation:**

* TurboModules use code generation for type safety

* You define the module interface in TypeScript/Flow

* Codegen creates native bindings automatically

* This ensures type safety between JavaScript and native

**2. Lazy Loading:**

* Modules aren't loaded when the app starts

* They're loaded only when you first use them from JavaScript

* This reduces initial app startup time

* Memory efficient - only loads what you actually use

**3. JSI Binding:**

* Native module registers with the TurboModule registry

* JSI creates host objects for module methods

* JavaScript gets direct access to native functions

* No bridge data conversion needed

**Example TurboModule Definition:**

```typescript
// Native module interface (TypeScript)
export interface Spec extends TurboModule {
  readonly getConstants: () => {
    readonly apiKey: string;
  };
  readonly processData: (data: string) => Promise<string>;
  readonly measureSync: (nodeId: number) => { width: number; height: number };
}

// Codegen generates native bindings
// JavaScript can use it like:
const MyModule = TurboModuleRegistry.get<Spec>('MyModule');
const result = await MyModule.processData('input');
const { width, height } = MyModule.measureSync(123);
```

### 🔹 TurboModule vs Old Module Comparison

**Old Native Modules:**

* **Loading**: Loaded when app starts (all modules loaded right away)

* **Communication**: Use bridge (async message passing)

* **Data Conversion**: Required for all data

* **Performance**: Slower (bridge overhead)

* **Type Safety**: Limited (runtime checks)

* **Synchronous**: Not possible

* **Memory**: Higher (all modules in memory)

**TurboModules:**

* **Loading**: Lazy loading (loaded when you need them)

* **Communication**: Use JSI (direct function calls)

* **Data Conversion**: Not required

* **Performance**: Faster (no bridge overhead)

* **Type Safety**: Better (codegen ensures types)

* **Synchronous**: Possible when you need it

* **Memory**: Lower (only loaded modules in memory)

**Performance Comparison:**

| Operation | Old Module | TurboModule | Improvement |
|-----------|------------|-------------|-------------|
| Simple call | ~2-5ms | ~0.01-0.1ms | 20-500x faster |
| Large data | ~10-50ms | ~0.1-1ms | 10-500x faster |
| Frequent calls | Queue buildup | Direct calls | Much smoother |

### 🔹 Migration to TurboModules

**Migrating Existing Modules:**

* Rewrite module to use TurboModule spec

* Define TypeScript interface

* Update native implementation (iOS/Android)

* Run codegen to create bindings

* Update JavaScript code to use the new module

**Backward Compatibility:**

* Old bridge modules still work

* You can use both old and new modules in the same app

* Gradual migration is possible

* Some modules may not need migration (if performance is fine)

**When to Migrate:**

* Module is performance-critical

* Module makes lots of calls

* Module needs synchronous access

* Module handles large data

* Module is used in animations

### 🔹 TurboModule Best Practices

**1. Use Codegen:**

* Always use codegen for type safety

* Define clear interfaces

* Let codegen handle bindings

**2. Lazy Loading:**

* Design modules to be lazy-loadable

* Don't do heavy work in module initialization

* Initialize on first use

**3. Thread Safety:**

* Ensure thread-safe implementations

* Use proper synchronization

* Document thread requirements

**4. Error Handling:**

* Use proper error types

* Return meaningful errors

* Handle errors in JavaScript

**Example Best Practice:**

```typescript
// Good: Lazy-loaded, type-safe TurboModule
export interface CameraSpec extends TurboModule {
  readonly takePicture: (options: CameraOptions) => Promise<ImageData>;
  readonly getConstants: () => { readonly maxZoom: number };
}

// Usage
const Camera = TurboModuleRegistry.get<CameraSpec>('Camera');
// Module loaded here (lazy)
const image = await Camera.takePicture({ quality: 0.8 });
```

📌 **In simple terms**: TurboModules are the new way to create native modules using JSI. They use code generation for type safety, are loaded on demand (lazy loading), and support synchronous calls when needed. They're much faster than old bridge-based modules, especially for frequent operations or large data transfers. Migration from old modules is possible but requires rewriting to use the TurboModule spec.

---

### 🔹 💡 Threading Model

### 🔹 Thread Separation

React Native runs different parts of your app on different threads to keep the UI responsive and enable parallelism:

* **JavaScript Thread**: Your React code, state, business logic - single thread, event-driven. Runs JavaScript engine (JavaScriptCore/Hermes/V8). Handles all React rendering, state updates, and business logic.

* **UI Thread (Main Thread)**: Native UI rendering, user interactions - iOS and Android each have their own main thread. Platform-specific main thread that handles all UI operations. Must stay responsive (blocking causes UI freezing).

* **Background Threads**: Native modules can use background threads for heavy work. Used for CPU-intensive tasks, network requests, file I/O. Cannot directly update UI (must dispatch to UI thread).

### 🔹 Thread Responsibilities

**JavaScript Thread:**

* React component rendering

* State management and updates

* Business logic execution

* Event handling (from native)

* Layout calculations (Yoga - old architecture)

* JavaScript execution (all your code)

**UI Thread (Main Thread):**

* Native view creation and updates

* Touch event handling

* Animation rendering

* Screen painting

* Platform-specific UI operations

* Must not be blocked (causes jank/freezing)

**Background Threads:**

* Heavy computations (image processing, data parsing)

* Network requests (can be done here)

* File I/O operations

* Database operations

* Any CPU-intensive work

### 🔹 Why Thread Separation?

* **Non-blocking**: JavaScript work doesn't block the UI thread - your app stays responsive even during heavy JavaScript execution

* **Performance**: Native UI rendering happens on the native thread, which is optimized for that platform (better performance than JavaScript rendering)

* **Parallelism**: JavaScript and native code can work at the same time (true parallelism, not just async)

* **Responsiveness**: UI thread stays responsive even when JavaScript is busy (user can still interact)

* **Platform Optimization**: Each platform's UI thread is optimized for that platform's rendering pipeline

### 🔹 Communication Between Threads

**Old Architecture (Bridge):**

* Asynchronous message passing between threads

* Messages queued and processed in batches

* Serialization required for all data

* Cannot block either thread

* Example: JavaScript → Bridge Queue → Native Thread

**New Architecture (JSI):**

* Direct function calls, can be synchronous when needed

* No message queue (direct execution)

* No serialization (shared memory)

* Can block if synchronous (use carefully)

* Example: JavaScript → Direct JSI Call → Native Thread

### 🔹 Thread Safety Considerations

**JavaScript Thread Safety:**

* JavaScript is single-threaded (no race conditions in JS code)

* Event loop processes events sequentially

* State updates are atomic within a render cycle

* But: Heavy work can block the thread (affects responsiveness)

**Native Thread Safety:**

* Native code can be multi-threaded

* Must ensure thread safety when accessing shared data

* UI updates must happen on UI thread

* Background threads cannot directly update UI

**Cross-Thread Communication:**

* Bridge/JSI handles thread synchronization

* Messages are thread-safe (serialized/deserialized safely)

* Callbacks are dispatched to correct thread

* Must be careful with shared state between threads

**Common Thread Safety Issues:**

**1. UI Updates from Wrong Thread:**

```javascript
// ❌ Wrong: Updating UI from background thread
someBackgroundTask(() => {
  setState(newValue); // This is actually OK (React handles it)
  // But native UI updates must be on UI thread
});

// ✅ Correct: React state updates are thread-safe
// Native modules should dispatch UI updates to UI thread
```

**2. Race Conditions in Native Code:**

```objective-c
// ❌ Wrong: Race condition
- (void)updateValue {
    self.value = self.value + 1; // Not thread-safe
}

// ✅ Correct: Use synchronization
- (void)updateValue {
    @synchronized(self) {
        self.value = self.value + 1;
    }
}
```

**3. Blocking UI Thread:**

```javascript
// ❌ Wrong: Blocking JavaScript thread
for (let i = 0; i < 10000000; i++) {
  heavyComputation(); // Blocks thread, UI freezes
}

// ✅ Correct: Use background thread or break up work
// Use InteractionManager or requestIdleCallback
```

### 🔹 Threading Best Practices

**1. Keep JavaScript Thread Responsive:**

* Break up heavy computations

* Use `InteractionManager` for non-urgent work

* Use `requestIdleCallback` for low-priority work

* Avoid blocking operations in render

**2. Use Background Threads for Heavy Work:**

* Image processing

* Large data parsing

* Complex calculations

* File operations

**3. Minimize Cross-Thread Communication:**

* Batch updates when possible

* Reduce frequency of bridge/JSI calls

* Cache data to avoid repeated calls

**4. Be Careful with Synchronous Calls:**

* Synchronous JSI calls can block JavaScript thread

* Use only for small, fast operations

* Prefer async for longer operations

**Example: Proper Thread Usage:**

```javascript
// Heavy computation on background thread
import { InteractionManager } from 'react-native';

const processLargeData = (data) => {
  // Wait for interactions to finish
  InteractionManager.runAfterInteractions(() => {
    // This runs after UI interactions complete
    const result = heavyComputation(data);
    setState(result);
  });
};

// Or use native module with background thread
NativeModules.DataProcessor.processAsync(data, (result) => {
  setState(result); // Callback on JavaScript thread
});
```

### 🔹 Thread Lifecycle

**App Startup:**

1. Native app starts (UI thread active)
2. JavaScript engine initializes (JavaScript thread created)
3. Bridge/JSI established (communication ready)
4. React Native runtime starts
5. Root component renders (JavaScript thread)
6. Native views created (UI thread)
7. App interactive (both threads running)

**During Runtime:**

* JavaScript thread: Processing events, rendering, state updates

* UI thread: Rendering, handling touches, animations

* Background threads: Created as needed by native modules

**App Shutdown:**

* JavaScript thread stops processing

* Native views unmount (UI thread)

* Background threads finish work

* Resources cleaned up

📌 **In simple terms**: React Native separates JavaScript execution from native UI rendering into different threads. The JavaScript thread handles React code and business logic, while the UI thread handles native rendering. Background threads can be used for heavy work. This separation keeps the UI responsive, but requires careful thread safety considerations. The bridge (old) or JSI (new) handles communication between threads safely.

---

### 🔹 🧩 Component Rendering Process

### 🔹 How Components Render

The rendering process in React Native involves multiple stages from JSX to native UI. Understanding each step helps you optimize performance and debug rendering issues.

**Step-by-Step Rendering Flow:**

**1. JSX Written & Transpiled:**

* You write JSX like `<View><Text>Hello</Text></View>`

* Babel/Metro bundler transforms JSX into `React.createElement()` calls

* Example: `<View style={styles.container}>` becomes `React.createElement(View, { style: styles.container }, children)`

* This happens at build time, not runtime

**2. React Reconciliation (Render Phase):**

* React processes your component tree and creates a virtual representation

* Similar to Virtual DOM in web React, but called "React Element Tree" in React Native

* React performs reconciliation - compares previous tree with new tree

* Determines what changed: new components, updated props, removed components

* Creates a list of mutations needed (not actual UI changes yet)

* This all happens on the JavaScript thread

**3. Shadow Tree Creation (Layout Phase):**

* React Native creates a "Shadow Tree" - a platform-agnostic representation

* Shadow nodes mirror your component hierarchy but contain layout information

* Each shadow node has properties: width, height, position, flex properties

* Yoga layout engine calculates positions and sizes based on flexbox rules

* Layout calculations happen on JavaScript thread (can be moved to background thread in new architecture)

**4. Serialization & Bridge (Old Architecture):**

* Shadow tree gets serialized into JSON-like format

* Serialized data includes: component type, props, layout information, hierarchy

* Data is batched and sent through the bridge asynchronously

* Bridge queues messages and sends them to native thread

* Example: `{ type: 'View', props: { style: {...} }, children: [...] }`

**5. Direct Update via JSI (New Architecture - Fabric):**

* In new architecture, no serialization needed

* JSI provides direct memory access between JavaScript and native code

* Shadow tree is directly accessible to native code via JSI

* Native code can read shadow tree properties synchronously

* Much faster than bridge serialization

**6. Native Component Creation (Commit Phase):**

* Native thread receives updates (via bridge or JSI)

* Native code creates or updates actual platform components

* **iOS**: Creates `UIView`, `UILabel`, `UIButton` etc. from UIKit

* **Android**: Creates `ViewGroup`, `TextView`, `Button` etc. from Android Views

* Components are positioned and styled according to shadow tree layout

* Native views are added to the view hierarchy

**7. Platform-Specific Rendering:**

* Each platform renders using its native rendering engine

* **iOS**: Uses Core Animation and UIKit rendering pipeline

* **Android**: Uses Android's View system and hardware acceleration

* Styling is converted: React Native styles → platform-specific styling

* Native rendering happens on UI thread (main thread) of each platform

### 🔹 Detailed Rendering Phases

**Render Phase (JavaScript Thread):**

* Component functions execute

* Hooks run (useState, useEffect, etc.)

* React creates element tree

* Reconciliation determines changes

* Shadow tree nodes created/updated

**Layout Phase (JavaScript Thread - can be background in new arch):**

* Yoga layout engine calculates positions

* Flexbox rules applied

* Dimensions computed based on constraints

* Layout results stored in shadow nodes

**Commit Phase (Native Thread):**

* Changes committed to native views

* Native components created/updated/destroyed

* View hierarchy updated

* Actual pixels rendered on screen

### 🔹 Shadow Tree & Yoga Layout

**Shadow Tree:**

* Platform-agnostic representation of your UI

* Each React Native component has a corresponding shadow node

* Shadow nodes store layout properties (width, height, margins, padding)

* Shadow tree is what gets diffed, not the native views directly

* Allows React Native to batch and optimize updates

**Yoga Layout Engine:**

* Facebook's cross-platform layout engine (also used in other frameworks)

* Implements Flexbox layout algorithm

* Calculates positions and sizes based on flex properties

* Handles constraints: parent dimensions, flex-basis, flex-grow, flex-shrink

* Computes layout synchronously on JavaScript thread (old) or background thread (new)

**Layout Calculation Example:**

```jsx
<View style={{ flex: 1, flexDirection: 'row' }}>
  <View style={{ width: 100 }} />
  <View style={{ flex: 1 }} />
</View>
```

* Yoga calculates: first View = 100px, second View = remaining space
* Results stored in shadow nodes
* Native views positioned accordingly

### 🔹 Fabric Renderer (New Architecture)

**What is Fabric:**

* New rendering system replacing the old bridge-based renderer

* Part of React Native's new architecture

* Enables synchronous rendering when needed

* Direct access to shadow tree via JSI

**Fabric Benefits:**

* **Synchronous Updates**: Can update UI synchronously for critical updates

* **No Serialization**: Direct memory access eliminates serialization overhead

* **Better Performance**: Faster rendering, especially for animations

* **Priority-based Updates**: Can prioritize urgent updates over less important ones

* **Concurrent Features**: Supports React 18 concurrent features

**Fabric Rendering Flow:**

1. React creates element tree (same as before)
2. Fabric creates shadow tree (same concept, better implementation)
3. Layout calculated (can happen on background thread)
4. JSI directly exposes shadow tree to native code
5. Native code reads shadow tree and updates views
6. No serialization, no message queue delays

### 🔹 Platform-Specific Rendering Details

**iOS Rendering:**

* JSX `<View>` → `UIView` (container view)

* JSX `<Text>` → `UILabel` (text label)

* JSX `<Button>` → `UIButton` (native button)

* JSX `<Image>` → `UIImageView` (image view)

* Styles converted to Auto Layout constraints or frame-based layout

* Uses Core Animation for animations

* Renders using Metal or OpenGL for hardware acceleration

**Android Rendering:**

* JSX `<View>` → `ViewGroup` (container, often `ReactViewGroup`)

* JSX `<Text>` → `TextView` (text view)

* JSX `<Button>` → `Button` or `AppCompatButton` (native button)

* JSX `<Image>` → `ImageView` (image view)

* Styles converted to Android View attributes and ConstraintLayout

* Uses Android's animation framework

* Renders using hardware acceleration when available

**Styling Conversion:**

* React Native uses a subset of CSS properties

* Styles are converted to platform-specific equivalents

* Example: `flexDirection: 'row'` → iOS Auto Layout horizontal, Android horizontal LinearLayout

* Example: `backgroundColor: 'red'` → iOS `backgroundColor` property, Android `setBackgroundColor()`

* Some styles are platform-specific and only work on one platform

### 🔹 Update Flow & Diffing

**When State Changes:**

1. **State Update**: `setState()` or state hook called
2. **Re-render Triggered**: React schedules a re-render
3. **Component Re-executes**: Component function runs again with new state
4. **New Element Tree**: React creates new element tree
5. **Reconciliation**: React compares old and new trees
6. **Diff Calculated**: Only changed parts identified
7. **Shadow Tree Updated**: Only changed shadow nodes updated
8. **Layout Recalculated**: Yoga recalculates layout for affected nodes
9. **Native Update**: Only changed native views updated (not entire tree)

**Efficient Updates:**

* React Native only updates what changed

* If a `<Text>` component's text changes, only that `UILabel`/`TextView` updates

* Parent views don't re-render unless their props changed

* Sibling components unaffected by other components' updates

* This is why keys are important in lists - helps React identify what changed

### 🔹 Performance Considerations

**1. Render Performance:**

* Keep component trees shallow when possible

* Use `React.memo()` to prevent unnecessary re-renders

* Avoid inline functions and objects in render (creates new references)

* Use `useMemo()` and `useCallback()` for expensive computations

* Flat lists are more performant than nested ScrollViews

**2. Layout Performance:**

* Complex flexbox layouts can be expensive to calculate

* Avoid deeply nested flex containers

* Use `flex: 1` carefully - triggers layout calculations

* Fixed dimensions (`width: 100`) are faster than flex calculations

* `onLayout` callbacks can cause performance issues if overused

**3. Bridge/JSI Performance:**

* Old architecture: Minimize bridge calls, batch updates

* New architecture: JSI eliminates most bridge overhead

* Still avoid unnecessary re-renders (wastes CPU even with JSI)

* Use native driver for animations (bypasses JavaScript thread)

📌 **In simple terms**: Your JSX gets transformed into a shadow tree representation, layout is calculated by Yoga, and then native platform components are created/updated. The new Fabric renderer uses JSI for direct access, eliminating serialization overhead. React Native efficiently updates only what changed, keeping performance optimal.

---

### 🔹 📦 State Management & Updates

### 🔹 State Updates Work the Same

React Native uses the same state management as React web, with the same APIs and behavior:

* **useState**: Works exactly the same - manages component state, triggers re-renders

* **useEffect**: Same lifecycle management - runs after render, cleanup on unmount, dependency tracking

* **Context**: Same context API for sharing state across components, avoids prop drilling

* **Redux/MobX**: Same state management libraries work in React Native (Redux, MobX, Zustand, etc.)

* **Custom Hooks**: Same pattern - reusable stateful logic

### 🔹 Update Flow

**Detailed State Update Process:**

1. **State changes**: You call `setState` or update state (useState, useReducer, etc.)

2. **Batching**: React batches multiple state updates in the same event handler or synchronous code

3. **Scheduling**: React schedules a re-render (may be deferred in concurrent mode)

4. **Re-render**: React determines which components need to re-render

5. **Reconciliation**: React compares old and new element trees (diffing algorithm)

6. **Diff Calculated**: Only changed parts identified (components, props, children)

7. **Shadow Tree Updated**: Only changed shadow nodes updated (React Native specific)

8. **Layout Recalculated**: Yoga recalculates layout for affected nodes

9. **Updates Sent**: Only the changes are sent to native (through bridge or JSI)

10. **Native Updates**: Native components update efficiently (only changed views)

### 🔹 Automatic Batching

React automatically batches state updates for performance:

**Batched Updates:**

```javascript
// All these updates are batched into one re-render
function handleClick() {
  setCount(c => c + 1);
  setFlag(f => !f);
  setName('New Name');
  // Only one re-render happens
}
```

**Not Batched (Old React):**

```javascript
// In React < 18, these would cause multiple re-renders
setTimeout(() => {
  setCount(c => c + 1); // Re-render 1
  setFlag(f => !f);     // Re-render 2
}, 1000);
```

**Batched in React 18+ (Including React Native 0.69+):**

```javascript
// React 18+ batches these too
setTimeout(() => {
  setCount(c => c + 1); // Batched
  setFlag(f => !f);     // Batched
  // Only one re-render
}, 1000);
```

### 🔹 Update Scheduling & Priorities

**Update Priorities (React 18 Concurrent Features):**

* **Urgent Updates**: User interactions (clicks, input) - highest priority

* **Transition Updates**: Non-urgent updates (data fetching, list updates) - can be interrupted

**Example:**

```javascript
import { startTransition, useTransition } from 'react';

function Component() {
  const [isPending, startTransition] = useTransition();
  const [input, setInput] = useState('');
  const [results, setResults] = useState([]);

  // Urgent: User input (high priority)
  const handleInput = (value) => {
    setInput(value);

    // Non-urgent: Search results (low priority, can be interrupted)
    startTransition(() => {
      const results = search(value);
      setResults(results);
    });
  };
}
```

### 🔹 State Update Optimization

**Preventing Unnecessary Re-renders:**

**1. React.memo:**

```javascript
const ExpensiveComponent = React.memo(({ data }) => {
  // Only re-renders if props change
  return <View>{data}</View>;
});
```

**2. useMemo:**

```javascript
const expensiveValue = useMemo(() => {
  return computeExpensiveValue(a, b);
}, [a, b]); // Only recomputes if a or b change
```

**3. useCallback:**

```javascript
const handleClick = useCallback(() => {
  doSomething(id);
}, [id]); // Only recreates if id changes
```

**4. Context Optimization:**

```javascript
// ❌ Bad: All consumers re-render when any value changes
const Context = createContext({ user: null, theme: null });

// ✅ Good: Split contexts
const UserContext = createContext(null);
const ThemeContext = createContext(null);
```

### 🔹 State Update Performance

**Performance Considerations:**

**1. Update Frequency:**

* Too many updates can cause performance issues

* Batch related updates together

* Use debouncing/throttling for frequent updates (scroll, input)

**2. Update Scope:**

* Update only what's necessary

* Avoid updating parent when only child needs update

* Use local state when possible (don't lift state unnecessarily)

**3. Large State Objects:**

* Updating large objects causes expensive re-renders

* Use immutable updates (create new objects)

* Consider state normalization (like Redux)

**Example: Efficient State Updates:**

```javascript
// ❌ Bad: Creates new object every render
const [state, setState] = useState({ count: 0, name: '' });
setState({ ...state, count: state.count + 1 });

// ✅ Good: Functional update
setState(prev => ({ ...prev, count: prev.count + 1 }));

// ✅ Better: Split state
const [count, setCount] = useState(0);
const [name, setName] = useState('');
setCount(c => c + 1); // Only count updates
```

### 🔹 State Management Patterns

**Local State (useState):**

* Component-specific state

* Simple, no external dependencies

* Good for UI state (toggles, form inputs)

**Lifted State:**

* Shared between sibling components

* Lift to common parent

* Can cause unnecessary re-renders

**Context API:**

* Global or deeply nested state

* Avoids prop drilling

* Can cause performance issues if not optimized

**External State Management:**

* Redux: Predictable state container, good for complex apps

* MobX: Observable state, simpler API

* Zustand: Lightweight, hooks-based

* Recoil: Facebook's state management (experimental)

### 🔹 State Update Flow in React Native

**Complete Flow:**

1. **State Update Triggered**: `setState()` called
2. **React Schedules Update**: Added to update queue
3. **Batching**: Multiple updates batched together
4. **Render Phase**: Component function executes
5. **Element Tree Created**: New React elements created
6. **Reconciliation**: Compare with previous tree
7. **Diff Calculated**: Identify changes
8. **Shadow Tree Update**: Update shadow nodes (React Native)
9. **Layout Calculation**: Yoga calculates new layout
10. **Commit Phase**: Changes committed to shadow tree
11. **Native Update**: Changes sent to native (bridge/JSI)
12. **UI Update**: Native views updated
13. **Screen Refresh**: User sees updated UI

**Performance Optimizations:**

* Only changed components re-render

* Only changed shadow nodes update

* Only changed native views update

* Layout recalculated only for affected nodes

* Updates batched to reduce bridge/JSI calls

📌 **In simple terms**: State management works exactly like React web. React automatically batches updates, schedules them based on priority, and efficiently updates only what changed. React Native adds shadow tree updates and native view updates to the flow. Use React.memo, useMemo, and useCallback to prevent unnecessary re-renders, and be mindful of update frequency and scope for optimal performance.

---

### 🔹 📋 FlatList Optimization - Deep Dive

### 🔹 What is FlatList?

FlatList is React Native's optimized list component that implements virtualization - it only renders items that are visible on screen, dramatically improving performance for large datasets.

* **Virtualization**: Only visible items are rendered in memory
* **Native Performance**: Uses native list components (UICollectionView on iOS, RecyclerView on Android)
* **Automatic Optimization**: Built-in optimizations for scrolling, memory, and rendering
* **Flexible**: Supports horizontal/vertical scrolling, headers, footers, separators, pull-to-refresh

### 🔹 How FlatList Virtualization Works

**Core Concept:**

FlatList doesn't render all items at once. Instead, it maintains a "window" of visible items plus a buffer, and recycles views as you scroll.

**Virtualization Process:**

1. **Initial Render**: FlatList calculates which items should be visible based on viewport size
2. **Render Window**: Only items in the "render window" are actually rendered
3. **View Recycling**: As you scroll, views are recycled - old views are reused for new items
4. **Dynamic Loading**: Items are added/removed from the render window as you scroll
5. **Memory Efficient**: Only a small subset of items exist in memory at any time

**Visual Representation:**

```
Total Items: 10,000
Viewport: Shows ~10 items
Render Window: ~30 items (visible + buffer)

Memory: Only 30 items rendered
Performance: Same as rendering 30 items, not 10,000
```

### 🔹 FlatList Internal Architecture

**iOS Implementation (UICollectionView):**

* Uses `UICollectionView` with custom layout
* Cell reuse queue for efficient memory usage
* Automatic cell recycling as you scroll
* Native scrolling performance (60fps)

**Android Implementation (RecyclerView):**

* Uses `RecyclerView` with adapter pattern
* ViewHolder pattern for view recycling
* Layout manager handles positioning
* Native scrolling performance (60fps)

**JavaScript Layer:**

* Manages data and item rendering logic
* Calculates which items should be visible
* Handles item updates and state
* Communicates with native layer via bridge/JSI

### 🔹 Key Performance Props Explained

**1. `getItemLayout` - Critical for Performance**

**What it does:**

* Tells FlatList the exact size and position of each item
* Eliminates layout measurement overhead
* Enables instant scrolling to any position

**When to use:**

* Items have fixed height/width
* You know exact dimensions
* Performance is critical

**Performance Impact:**

* Without: FlatList must measure each item (~5-10ms per item)
* With: No measurement needed (instant)
* Improvement: 10-100x faster scrolling, especially for large lists

**Example:**

```jsx
const ITEM_HEIGHT = 80; // Fixed height

const getItemLayout = useCallback((data, index) => ({
  length: ITEM_HEIGHT,
  offset: ITEM_HEIGHT * index,
  index,
}), []);

<FlatList
  data={items}
  getItemLayout={getItemLayout}
  renderItem={renderItem}
/>
```

**2. `initialNumToRender` - First Render Performance**

**What it does:**

* Controls how many items render on initial mount
* Lower = faster initial render, but more blank space
* Higher = slower initial render, but less blank space

**Default:** 10 items

**Performance Impact:**

* Lower values: Faster Time to Interactive (TTI)
* Higher values: Smoother initial scroll experience
* Sweet spot: Usually 5-15 items depending on item complexity

**Example:**

```jsx
<FlatList
  data={items}
  initialNumToRender={10} // Render 10 items initially
  renderItem={renderItem}
/>
```

**3. `windowSize` - Render Window Control**

**What it does:**

* Controls how many viewport lengths to render outside visible area
* windowSize = 5 means render 5 viewport lengths (2.5 above, 2.5 below)
* Lower = less memory, but more blank space when scrolling fast
* Higher = more memory, but smoother scrolling

**Default:** 21 (renders ~10.5 viewport lengths on each side)

**Performance Impact:**

* windowSize = 5: ~5x viewport items in memory (good for memory)
* windowSize = 21: ~21x viewport items in memory (good for smooth scrolling)
* Memory usage: windowSize × itemsPerViewport × itemMemory

**Example:**

```jsx
<FlatList
  data={items}
  windowSize={10} // Render 10 viewport lengths (5 above, 5 below)
  renderItem={renderItem}
/>
```

**4. `maxToRenderPerBatch` - Batch Rendering Control**

**What it does:**

* Controls how many items render per batch during scrolling
* Lower = smoother scrolling, but more batches
* Higher = fewer batches, but potential jank

**Default:** 10 items per batch

**Performance Impact:**

* Lower values: Smoother scrolling (less work per frame)
* Higher values: Faster initial load, but can cause frame drops
* Optimal: 5-10 for most cases

**Example:**

```jsx
<FlatList
  data={items}
  maxToRenderPerBatch={5} // Render 5 items per batch
  renderItem={renderItem}
/>
```

**5. `updateCellsBatchingPeriod` - Batch Update Timing**

**What it does:**

* Controls delay between batch updates (in milliseconds)
* Lower = more responsive, but more frequent updates
* Higher = less frequent updates, but potential lag

**Default:** 50ms

**Performance Impact:**

* Lower values: More responsive to scroll
* Higher values: Better batching, less overhead
* Optimal: 50-100ms for most cases

**Example:**

```jsx
<FlatList
  data={items}
  updateCellsBatchingPeriod={50} // Batch updates every 50ms
  renderItem={renderItem}
/>
```

**6. `removeClippedSubviews` - Memory Optimization**

**What it does:**

* Removes off-screen views from native view hierarchy
* Reduces memory usage for complex items
* May cause slight delay when scrolling back

**Default:** true on Android, false on iOS

**Performance Impact:**

* Memory: Can reduce memory by 30-50% for complex items
* Scrolling: Slight delay when scrolling back to removed views
* Best for: Lists with complex, memory-heavy items

**Example:**

```jsx
<FlatList
  data={items}
  removeClippedSubviews={true} // Remove off-screen views
  renderItem={renderItem}
/>
```

**7. `keyExtractor` - Efficient Item Identification**

**What it does:**

* Extracts unique key for each item
* Critical for React's reconciliation algorithm
* Must be stable and unique

**Performance Impact:**

* Without: React uses array index (causes issues with reordering)
* With stable keys: Efficient diffing, proper view recycling
* Improvement: Prevents unnecessary re-renders

**Example:**

```jsx
<FlatList
  data={items}
  keyExtractor={(item) => item.id} // Stable, unique key
  renderItem={renderItem}
/>
```

### 🔹 Optimizing renderItem Function

**The Problem:**

`renderItem` is called frequently during scrolling. If it's not optimized, it can cause performance issues.

**Optimization Techniques:**

**1. Memoize the Component:**

```jsx
const ListItem = React.memo(({ item, onPress }) => {
  return (
    <TouchableOpacity onPress={() => onPress(item.id)}>
      <Text>{item.title}</Text>
    </TouchableOpacity>
  );
});

// Use in FlatList
<FlatList
  data={items}
  renderItem={({ item }) => <ListItem item={item} onPress={handlePress} />}
/>
```

**2. Memoize Callbacks:**

```jsx
const handlePress = useCallback((id) => {
  // Handle press
}, []);

const renderItem = useCallback(({ item }) => (
  <ListItem item={item} onPress={handlePress} />
), [handlePress]);
```

**3. Avoid Inline Functions:**

```jsx
// ❌ Bad: Creates new function every render
<FlatList
  renderItem={({ item }) => (
    <Item onPress={() => handlePress(item.id)} />
  )}
/>

// ✅ Good: Memoized callback
const renderItem = useCallback(({ item }) => (
  <Item item={item} onPress={handlePress} />
), [handlePress]);
```

**4. Avoid Inline Objects/Styles:**

```jsx
// ❌ Bad: Creates new object every render
<FlatList
  renderItem={({ item }) => (
    <View style={{ padding: 10 }}>
      <Text>{item.title}</Text>
    </View>
  )}
/>

// ✅ Good: Stable style reference
const itemStyle = { padding: 10 };
const renderItem = useCallback(({ item }) => (
  <View style={itemStyle}>
    <Text>{item.title}</Text>
  </View>
), []);
```

### 🔹 Advanced Optimization Strategies

**1. Pagination with `onEndReached`:**

```jsx
function PaginatedList() {
  const [data, setData] = useState([]);
  const [loading, setLoading] = useState(false);
  const [page, setPage] = useState(1);

  const loadMore = useCallback(async () => {
    if (loading) return;
    setLoading(true);
    const newData = await fetchPage(page);
    setData(prev => [...prev, ...newData]);
    setPage(prev => prev + 1);
    setLoading(false);
  }, [page, loading]);

  return (
    <FlatList
      data={data}
      renderItem={renderItem}
      onEndReached={loadMore}
      onEndReachedThreshold={0.5} // Trigger when 50% from bottom
      ListFooterComponent={loading ? <LoadingSpinner /> : null}
    />
  );
}
```

**2. Optimized Item Component:**

```jsx
const OptimizedListItem = React.memo(({ item, onPress }) => {
  // Memoize expensive calculations
  const formattedDate = useMemo(() => {
    return new Date(item.timestamp).toLocaleDateString();
  }, [item.timestamp]);

  // Memoize callbacks
  const handlePress = useCallback(() => {
    onPress(item.id);
  }, [item.id, onPress]);

  return (
    <TouchableOpacity onPress={handlePress} style={styles.item}>
      <Text style={styles.title}>{item.title}</Text>
      <Text style={styles.date}>{formattedDate}</Text>
    </TouchableOpacity>
  );
}, (prevProps, nextProps) => {
  // Custom comparison for better control
  return prevProps.item.id === nextProps.item.id &&
         prevProps.item.title === nextProps.item.title;
});
```

**3. Fixed Height Optimization:**

```jsx
// If all items have the same height
const ITEM_HEIGHT = 80;

const getItemLayout = useCallback((data, index) => ({
  length: ITEM_HEIGHT,
  offset: ITEM_HEIGHT * index,
  index,
}), []);

<FlatList
  data={items}
  getItemLayout={getItemLayout}
  renderItem={renderItem}
  // These props work together for best performance
  initialNumToRender={10}
  maxToRenderPerBatch={10}
  windowSize={10}
  removeClippedSubviews={true}
/>
```

**4. Variable Height with Estimation:**

```jsx
// If items have variable heights, provide estimate
<FlatList
  data={items}
  estimatedItemSize={80} // Average item height
  renderItem={renderItem}
  // Still benefits from estimation
  initialNumToRender={10}
  windowSize={10}
/>
```

### 🔹 Performance Metrics & Monitoring

**Key Metrics to Monitor:**

1. **Frame Rate**: Should maintain 60fps during scrolling
2. **Memory Usage**: Should remain stable, not grow with scroll
3. **Initial Render Time**: Time to first item visible
4. **Scroll Jank**: Frame drops during scrolling

**Measuring Performance:**

```jsx
import { PerformanceObserver } from 'react-native-performance';

// Monitor render performance
const observer = new PerformanceObserver((list) => {
  for (const entry of list.getEntries()) {
    if (entry.duration > 16) { // > 16ms = dropped frame
      console.warn('Slow render:', entry.name, entry.duration);
    }
  }
});

observer.observe({ entryTypes: ['measure'] });

// Measure FlatList render
performance.mark('flatlist-render-start');
// ... render FlatList
performance.mark('flatlist-render-end');
performance.measure('flatlist-render', 'flatlist-render-start', 'flatlist-render-end');
```

### 🔹 Common Performance Pitfalls

**1. Not Using `keyExtractor`:**

```jsx
// ❌ Bad: Uses array index
<FlatList data={items} renderItem={renderItem} />

// ✅ Good: Stable keys
<FlatList
  data={items}
  keyExtractor={(item) => item.id}
  renderItem={renderItem}
/>
```

**2. Complex Items Without Memoization:**

```jsx
// ❌ Bad: Re-renders on every scroll
<FlatList
  renderItem={({ item }) => (
    <ComplexItem item={item} />
  )}
/>

// ✅ Good: Memoized component
const MemoizedItem = React.memo(ComplexItem);
<FlatList renderItem={({ item }) => <MemoizedItem item={item} />} />
```

**3. Inline Functions in renderItem:**

```jsx
// ❌ Bad: New function every render
<FlatList
  renderItem={({ item }) => (
    <Item onPress={() => handlePress(item.id)} />
  )}
/>

// ✅ Good: Memoized callback
const renderItem = useCallback(({ item }) => (
  <Item item={item} onPress={handlePress} />
), [handlePress]);
```

**4. Not Using `getItemLayout` for Fixed Heights:**

```jsx
// ❌ Bad: Measures every item
<FlatList data={fixedHeightItems} renderItem={renderItem} />

// ✅ Good: Provides layout info
<FlatList
  data={fixedHeightItems}
  getItemLayout={getItemLayout}
  renderItem={renderItem}
/>
```

**5. Too Large `windowSize`:**

```jsx
// ❌ Bad: Renders too many items
<FlatList windowSize={50} /> // 50 viewport lengths = huge memory

// ✅ Good: Reasonable window
<FlatList windowSize={10} /> // 10 viewport lengths = good balance
```

### 🔹 FlatList vs ScrollView

**When to Use FlatList:**

* Large datasets (100+ items)
* Dynamic data that changes
* Need virtualization
* Performance is critical
* Memory is a concern

**When to Use ScrollView:**

* Small, static lists (< 50 items)
* All items need to be rendered
* Simple layout
* Performance not critical

**Performance Comparison:**

| Aspect | ScrollView | FlatList |
|--------|-----------|----------|
| Memory | All items in memory | Only visible items |
| Initial Render | Slower (renders all) | Faster (renders window) |
| Scroll Performance | Can be janky (large lists) | Smooth (virtualized) |
| Use Case | Small lists | Large lists |

### 🔹 Complete Optimization Example

```jsx
import React, { useCallback, useMemo } from 'react';
import { FlatList, View, Text, StyleSheet } from 'react-native';

const ITEM_HEIGHT = 80;

function OptimizedList({ data }) {
  // Memoize item component
  const ListItem = useMemo(() => React.memo(({ item }) => (
    <View style={styles.item}>
      <Text style={styles.title}>{item.title}</Text>
      <Text style={styles.subtitle}>{item.subtitle}</Text>
    </View>
  )), []);

  // Memoize getItemLayout
  const getItemLayout = useCallback((data, index) => ({
    length: ITEM_HEIGHT,
    offset: ITEM_HEIGHT * index,
    index,
  }), []);

  // Memoize renderItem
  const renderItem = useCallback(({ item }) => (
    <ListItem item={item} />
  ), []);

  // Memoize keyExtractor
  const keyExtractor = useCallback((item) => item.id, []);

  return (
    <FlatList
      data={data}
      renderItem={renderItem}
      keyExtractor={keyExtractor}
      getItemLayout={getItemLayout}
      // Performance props
      initialNumToRender={10}
      maxToRenderPerBatch={10}
      windowSize={10}
      updateCellsBatchingPeriod={50}
      removeClippedSubviews={true}
      // Additional optimizations
      maintainVisibleContentPosition={{
        minIndexForVisible: 0,
        autoscrollToTopThreshold: 10
      }}
    />
  );
}

const styles = StyleSheet.create({
  item: {
    height: ITEM_HEIGHT,
    padding: 10,
    justifyContent: 'center',
  },
  title: {
    fontSize: 16,
    fontWeight: 'bold',
  },
  subtitle: {
    fontSize: 14,
    color: '#666',
  },
});
```

### 🔹 FlatList Internal Flow

**1. Data Processing:**

* FlatList receives data array
* Calculates total number of items
* Determines initial render window

**2. Initial Render:**

* Renders `initialNumToRender` items
* Calculates layout for visible items
* Creates native views for visible items

**3. Scroll Detection:**

* Native scroll events trigger JavaScript callbacks
* FlatList calculates new visible range
* Determines which items need to be rendered/removed

**4. View Recycling:**

* Old views are removed from render tree
* Views are reused for new items (recycling)
* Only item data changes, views are reused

**5. Batch Updates:**

* Multiple scroll events batched together
* Updates applied in batches (controlled by `updateCellsBatchingPeriod`)
* Reduces JavaScript thread work

**6. Memory Management:**

* Off-screen views removed (if `removeClippedSubviews={true}`)
* View recycling reduces memory allocation
* Only render window items in memory

### 🔹 Performance Best Practices Summary

**Essential Optimizations:**

1. ✅ Always provide `keyExtractor` with stable keys
2. ✅ Use `getItemLayout` for fixed-height items
3. ✅ Memoize `renderItem` with `useCallback`
4. ✅ Memoize item components with `React.memo`
5. ✅ Avoid inline functions and objects in `renderItem`

**Advanced Optimizations:**

1. ✅ Tune `windowSize` based on item complexity
2. ✅ Adjust `initialNumToRender` for faster TTI
3. ✅ Use `removeClippedSubviews` for complex items
4. ✅ Implement pagination for large datasets
5. ✅ Monitor frame rate and memory usage

**Performance Targets:**

* Frame Rate: Maintain 60fps during scrolling
* Memory: Stable memory usage (no growth with scroll)
* Initial Render: < 100ms for first items
* Scroll Jank: < 1% frame drops

📌 **In simple terms**: FlatList uses virtualization to only render visible items, dramatically improving performance for large lists. Key optimizations include providing `getItemLayout` for fixed heights, memoizing `renderItem` and item components, tuning `windowSize` and `initialNumToRender`, and avoiding inline functions. The component uses native list views (UICollectionView/RecyclerView) for optimal scrolling performance.

---

### 🔹 ⚡ Performance & Optimization - Comprehensive Guide

### 🔹 Performance Fundamentals

**What Affects Performance:**

* **JavaScript Thread**: Heavy computations block rendering
* **UI Thread**: Native rendering and animations
* **Bridge/JSI Communication**: Data serialization and message passing
* **Memory Usage**: Large objects, memory leaks, image caching
* **Network Requests**: Slow APIs, large payloads, inefficient caching
* **Bundle Size**: Large JavaScript bundles slow startup
* **Rendering**: Unnecessary re-renders, complex layouts, large component trees

**Performance Metrics:**

* **Frame Rate**: Target 60fps (16.67ms per frame)
* **Time to Interactive (TTI)**: < 3 seconds
* **Memory Usage**: Stable, no leaks
* **Bundle Size**: < 2MB for initial load
* **Network**: Efficient requests, proper caching

### 🔹 Common Performance Issues

**1. JavaScript Thread Blocking:**

**Problem:**

* Heavy computations block the JavaScript thread
* UI becomes unresponsive
* Animations stutter or freeze

**Symptoms:**

* UI freezes during operations
* Scroll jank
* Touch delays
* Frame drops

**Solutions:**

```jsx
// ❌ Bad: Blocks JavaScript thread
function processData(data) {
  const result = [];
  for (let i = 0; i < 1000000; i++) {
    result.push(heavyComputation(data[i]));
  }
  return result;
}

// ✅ Good: Use InteractionManager
import { InteractionManager } from 'react-native';

function processData(data) {
  InteractionManager.runAfterInteractions(() => {
    const result = [];
    for (let i = 0; i < 1000000; i++) {
      result.push(heavyComputation(data[i]));
    }
    setState(result);
  });
}

// ✅ Better: Use background thread (native module)
NativeModules.DataProcessor.processAsync(data, (result) => {
  setState(result);
});

// ✅ Best: Break into chunks
function processDataChunked(data) {
  const chunkSize = 1000;
  let index = 0;

  const processChunk = () => {
    const chunk = data.slice(index, index + chunkSize);
    const result = chunk.map(heavyComputation);
    setState(prev => [...prev, ...result]);

    index += chunkSize;
    if (index < data.length) {
      requestAnimationFrame(processChunk);
    }
  };

  processChunk();
}
```

**2. Unnecessary Re-renders:**

**Problem:**

* Components re-render when props/state haven't changed
* Causes wasted CPU cycles
* Can trigger expensive operations

**Solutions:**

```jsx
// ❌ Bad: Re-renders on every parent update
function Item({ data }) {
  return <Text>{data.name}</Text>;
}

// ✅ Good: Memoize component
const Item = React.memo(({ data }) => {
  return <Text>{data.name}</Text>;
});

// ✅ Better: Custom comparison
const Item = React.memo(({ data }) => {
  return <Text>{data.name}</Text>;
}, (prevProps, nextProps) => {
  return prevProps.data.id === nextProps.data.id &&
         prevProps.data.name === nextProps.data.name;
});

// ❌ Bad: Inline functions cause re-renders
function Parent() {
  return <Child onPress={() => handlePress()} />;
}

// ✅ Good: Memoized callback
function Parent() {
  const handlePress = useCallback(() => {
    // Handle press
  }, []);
  return <Child onPress={handlePress} />;
}

// ❌ Bad: Inline objects cause re-renders
function Parent() {
  return <Child style={{ padding: 10 }} />;
}

// ✅ Good: Stable style reference
const styles = StyleSheet.create({
  child: { padding: 10 }
});
function Parent() {
  return <Child style={styles.child} />;
}
```

**3. Memory Leaks:**

**Problem:**

* Event listeners not cleaned up
* Timers not cleared
* Subscriptions not unsubscribed
* Large objects held in memory

**Solutions:**

```jsx
// ❌ Bad: Memory leak
function Component() {
  useEffect(() => {
    const subscription = EventEmitter.addListener('event', handleEvent);
    // Missing cleanup
  }, []);
}

// ✅ Good: Cleanup
function Component() {
  useEffect(() => {
    const subscription = EventEmitter.addListener('event', handleEvent);
    return () => subscription.remove(); // Cleanup
  }, []);
}

// ❌ Bad: Timer leak
function Component() {
  useEffect(() => {
    const timer = setInterval(() => {
      // Do something
    }, 1000);
    // Missing cleanup
  }, []);
}

// ✅ Good: Clear timer
function Component() {
  useEffect(() => {
    const timer = setInterval(() => {
      // Do something
    }, 1000);
    return () => clearInterval(timer); // Cleanup
  }, []);
}

// ❌ Bad: Large object in memory
function Component() {
  const [data, setData] = useState([]);

  useEffect(() => {
    fetchLargeData().then(setData);
    // data stays in memory even when component unmounts
  }, []);
}

// ✅ Good: Clear on unmount
function Component() {
  const [data, setData] = useState([]);

  useEffect(() => {
    fetchLargeData().then(setData);
    return () => setData([]); // Clear on unmount
  }, []);
}
```

**4. Large Bundle Size:**

**Problem:**

* Large JavaScript bundle slows app startup
* Increases memory usage
* Slower download on first launch

**Solutions:**

```jsx
// ❌ Bad: Import entire library
import _ from 'lodash';
const result = _.map(data, item => item.name);

// ✅ Good: Import only what you need
import map from 'lodash/map';
const result = map(data, item => item.name);

// ✅ Better: Use native alternatives
const result = data.map(item => item.name);

// ❌ Bad: No code splitting
import HeavyComponent from './HeavyComponent';

function App() {
  return <HeavyComponent />;
}

// ✅ Good: Lazy loading
const HeavyComponent = React.lazy(() => import('./HeavyComponent'));

function App() {
  return (
    <Suspense fallback={<Loading />}>
      <HeavyComponent />
    </Suspense>
  );
}

// Metro config optimization
// metro.config.js
module.exports = {
  transformer: {
    getTransformOptions: async () => ({
      transform: {
        experimentalImportSupport: false,
        inlineRequires: true, // Reduces bundle size
      },
    }),
  },
};
```

### 🔹 Rendering Optimization

**1. Component Memoization:**

```jsx
// React.memo for functional components
const ExpensiveComponent = React.memo(({ data, onPress }) => {
  return (
    <View>
      <Text>{data.title}</Text>
      <Button onPress={onPress} />
    </View>
  );
});

// useMemo for expensive calculations
function Component({ items }) {
  const sortedItems = useMemo(() => {
    return items.sort((a, b) => a.date - b.date);
  }, [items]);

  return <List items={sortedItems} />;
}

// useCallback for stable function references
function Component() {
  const handlePress = useCallback((id) => {
    // Handle press
  }, []);

  return <Child onPress={handlePress} />;
}
```

**2. List Optimization:**

```jsx
// FlatList optimization
function OptimizedList({ data }) {
  const renderItem = useCallback(({ item }) => (
    <ListItem item={item} />
  ), []);

  const keyExtractor = useCallback((item) => item.id, []);

  const getItemLayout = useCallback((data, index) => ({
    length: ITEM_HEIGHT,
    offset: ITEM_HEIGHT * index,
    index,
  }), []);

  return (
    <FlatList
      data={data}
      renderItem={renderItem}
      keyExtractor={keyExtractor}
      getItemLayout={getItemLayout}
      initialNumToRender={10}
      maxToRenderPerBatch={10}
      windowSize={10}
      removeClippedSubviews={true}
    />
  );
}
```

**3. Layout Optimization:**

```jsx
// ❌ Bad: Complex nested flex layouts
<View style={{ flex: 1 }}>
  <View style={{ flex: 1 }}>
    <View style={{ flex: 1 }}>
      <View style={{ flex: 1 }}>
        <Text>Deep nesting</Text>
      </View>
    </View>
  </View>
</View>

// ✅ Good: Flatter structure
<View style={styles.container}>
  <Text>Flatter structure</Text>
</View>

// ❌ Bad: Dynamic layout calculations
<View style={{ width: calculateWidth() }} />

// ✅ Good: Fixed or memoized dimensions
const width = useMemo(() => calculateWidth(), [dependencies]);
<View style={{ width }} />
```

### 🔹 Memory Management

**1. Image Optimization:**

```jsx
// ❌ Bad: Large images without optimization
<Image source={{ uri: 'https://example.com/large-image.jpg' }} />

// ✅ Good: Resize images
<Image
  source={{ uri: 'https://example.com/image.jpg' }}
  resizeMode="cover"
  style={{ width: 200, height: 200 }}
/>

// ✅ Better: Use optimized image formats
// Use WebP on Android, HEIC on iOS when possible

// ✅ Best: Cache images
import FastImage from 'react-native-fast-image';

<FastImage
  source={{
    uri: 'https://example.com/image.jpg',
    priority: FastImage.priority.normal,
    cache: FastImage.cacheControl.immutable,
  }}
  resizeMode={FastImage.resizeMode.cover}
/>
```

**2. Data Structure Optimization:**

```jsx
// ❌ Bad: Large arrays in state
const [items, setItems] = useState([]);
// Adding 10,000 items causes performance issues

// ✅ Good: Pagination
const [items, setItems] = useState([]);
const [page, setPage] = useState(1);

const loadMore = async () => {
  const newItems = await fetchPage(page);
  setItems(prev => [...prev, ...newItems]);
  setPage(prev => prev + 1);
};

// ❌ Bad: Deep object nesting
const data = {
  user: {
    profile: {
      settings: {
        theme: 'dark'
      }
    }
  }
};

// ✅ Good: Flatten structure
const data = {
  userTheme: 'dark'
};

// ❌ Bad: Inefficient lookups
const findItem = (id) => {
  return items.find(item => item.id === id); // O(n)
};

// ✅ Good: Use Map for O(1) lookups
const itemsMap = useMemo(() => {
  return new Map(items.map(item => [item.id, item]));
}, [items]);

const findItem = (id) => {
  return itemsMap.get(id); // O(1)
};
```

**3. Memory Leak Prevention:**

```jsx
// Cleanup patterns
function Component() {
  useEffect(() => {
    // Setup
    const subscription = subscribe();
    const timer = setInterval(() => {}, 1000);
    const listener = addEventListener();

    // Cleanup (runs on unmount)
    return () => {
      subscription.unsubscribe();
      clearInterval(timer);
      removeEventListener(listener);
    };
  }, []);

  // Cleanup on dependency change
  useEffect(() => {
    const controller = new AbortController();

    fetch(url, { signal: controller.signal })
      .then(response => response.json())
      .then(setData);

    return () => {
      controller.abort(); // Cancel fetch on unmount
    };
  }, [url]);
}
```

### 🔹 Network Optimization

**1. Request Optimization:**

```jsx
// ❌ Bad: Multiple sequential requests
const loadData = async () => {
  const users = await fetchUsers();
  const posts = await fetchPosts();
  const comments = await fetchComments();
  // Sequential = slow
};

// ✅ Good: Parallel requests
const loadData = async () => {
  const [users, posts, comments] = await Promise.all([
    fetchUsers(),
    fetchPosts(),
    fetchComments(),
  ]);
  // Parallel = faster
};

// ❌ Bad: No caching
const fetchData = async () => {
  const response = await fetch(url);
  return response.json();
};

// ✅ Good: Implement caching
const cache = new Map();

const fetchData = async (url) => {
  if (cache.has(url)) {
    return cache.get(url);
  }

  const response = await fetch(url);
  const data = await response.json();
  cache.set(url, data);
  return data;
};

// ✅ Better: Use React Query or SWR
import { useQuery } from 'react-query';

const { data } = useQuery('users', fetchUsers, {
  staleTime: 5 * 60 * 1000, // 5 minutes
  cacheTime: 10 * 60 * 1000, // 10 minutes
});
```

**2. Request Debouncing/Throttling:**

```jsx
// Debounce search input
function SearchInput() {
  const [query, setQuery] = useState('');
  const [results, setResults] = useState([]);

  useEffect(() => {
    const timer = setTimeout(() => {
      if (query) {
        search(query).then(setResults);
      }
    }, 300); // Wait 300ms after user stops typing

    return () => clearTimeout(timer);
  }, [query]);

  return (
    <TextInput
      value={query}
      onChangeText={setQuery}
      placeholder="Search..."
    />
  );
}

// Throttle scroll events
function ScrollableList() {
  const [scrollY, setScrollY] = useState(0);
  const lastUpdate = useRef(0);

  const handleScroll = (event) => {
    const now = Date.now();
    if (now - lastUpdate.current > 100) { // Update max once per 100ms
      setScrollY(event.nativeEvent.contentOffset.y);
      lastUpdate.current = now;
    }
  };

  return (
    <ScrollView onScroll={handleScroll} scrollEventThrottle={16}>
      {/* Content */}
    </ScrollView>
  );
}
```

### 🔹 Image Optimization

**1. Image Loading Strategies:**

```jsx
// Lazy load images
function LazyImage({ uri }) {
  const [loaded, setLoaded] = useState(false);

  return (
    <View>
      {!loaded && <Placeholder />}
      <Image
        source={{ uri }}
        onLoad={() => setLoaded(true)}
        style={{ opacity: loaded ? 1 : 0 }}
      />
    </View>
  );
}

// Progressive image loading
function ProgressiveImage({ uri, thumbnail }) {
  const [loaded, setLoaded] = useState(false);

  return (
    <View>
      <Image source={{ uri: thumbnail }} style={styles.thumbnail} />
      <Image
        source={{ uri }}
        onLoad={() => setLoaded(true)}
        style={[styles.full, { opacity: loaded ? 1 : 0 }]}
      />
    </View>
  );
}

// Image caching with FastImage
import FastImage from 'react-native-fast-image';

<FastImage
  source={{
    uri: 'https://example.com/image.jpg',
    priority: FastImage.priority.high,
    cache: FastImage.cacheControl.immutable,
  }}
  resizeMode={FastImage.resizeMode.cover}
  style={styles.image}
/>
```

**2. Image Size Optimization:**

```jsx
// Resize images before display
function OptimizedImage({ uri, width, height }) {
  // Use image CDN with resize parameters
  const optimizedUri = `${uri}?w=${width}&h=${height}&q=80`;

  return (
    <Image
      source={{ uri: optimizedUri }}
      style={{ width, height }}
      resizeMode="cover"
    />
  );
}

// Use appropriate image formats
// WebP for Android (smaller file size)
// HEIC for iOS (better compression)
```

### 🔹 Bundle Size Optimization

**1. Code Splitting:**

```jsx
// Lazy load routes
const HomeScreen = React.lazy(() => import('./screens/HomeScreen'));
const ProfileScreen = React.lazy(() => import('./screens/ProfileScreen'));

function App() {
  return (
    <NavigationContainer>
      <Suspense fallback={<Loading />}>
        <Stack.Navigator>
          <Stack.Screen name="Home" component={HomeScreen} />
          <Stack.Screen name="Profile" component={ProfileScreen} />
        </Stack.Navigator>
      </Suspense>
    </NavigationContainer>
  );
}

// Conditional imports
const loadFeature = async () => {
  if (needsFeature) {
    const { Feature } = await import('./Feature');
    return Feature;
  }
  return null;
};
```

**2. Tree Shaking:**

```jsx
// ❌ Bad: Import entire library
import _ from 'lodash';
const result = _.map(data, x => x * 2);

// ✅ Good: Import specific functions
import map from 'lodash/map';
const result = map(data, x => x * 2);

// ✅ Better: Use native methods
const result = data.map(x => x * 2);

// Remove unused code
// Use tools like ESLint to detect unused imports
```

**3. Metro Configuration:**

```js
// metro.config.js
module.exports = {
  transformer: {
    getTransformOptions: async () => ({
      transform: {
        experimentalImportSupport: false,
        inlineRequires: true, // Reduces bundle size
      },
    }),
  },
  resolver: {
    // Exclude unnecessary files
    blockList: [/node_modules\/.*\/android\/.*/],
  },
};
```

### 🔹 Profiling & Monitoring

**1. Performance Monitoring:**

```jsx
import { PerformanceObserver } from 'react-native-performance';

// Monitor render performance
const observer = new PerformanceObserver((list) => {
  for (const entry of list.getEntries()) {
    if (entry.duration > 16) { // > 16ms = dropped frame
      console.warn('Slow render:', entry.name, entry.duration);
    }
  }
});

observer.observe({ entryTypes: ['measure'] });

// Measure component render
function Component() {
  useEffect(() => {
    performance.mark('component-render-start');
    // Component logic
    performance.mark('component-render-end');
    performance.measure('component-render', 'component-render-start', 'component-render-end');
  }, []);
}
```

**2. Memory Profiling:**

```jsx
// Monitor memory usage
import { NativeModules } from 'react-native';

const checkMemory = () => {
  if (NativeModules.DeviceInfo) {
    NativeModules.DeviceInfo.getUsedMemory((usedMemory) => {
      console.log('Used memory:', usedMemory);
      if (usedMemory > 100 * 1024 * 1024) { // > 100MB
        console.warn('High memory usage!');
      }
    });
  }
};

// Use React DevTools Profiler
// Enable "Record why each component rendered"
```

**3. Network Monitoring:**

```jsx
// Monitor network requests
import { NetworkInfo } from 'react-native-network-info';

const monitorNetwork = async () => {
  const type = await NetworkInfo.getConnectionType();
  const isConnected = await NetworkInfo.isConnectionExpensive();

  console.log('Network type:', type);
  console.log('Is expensive:', isConnected);

  // Adjust behavior based on network
  if (isConnected) {
    // Reduce image quality, disable auto-play videos
  }
};
```

### 🔹 Animation Performance

**1. Use Native Driver:**

```jsx
import { Animated } from 'react-native';

// ❌ Bad: Runs on JavaScript thread
Animated.timing(animatedValue, {
  toValue: 1,
  duration: 1000,
  // useNativeDriver: false (default)
}).start();

// ✅ Good: Runs on UI thread
Animated.timing(animatedValue, {
  toValue: 1,
  duration: 1000,
  useNativeDriver: true, // Runs on UI thread
}).start();

// ✅ Better: Use Reanimated for complex animations
import Animated, { useSharedValue, withSpring } from 'react-native-reanimated';

function Component() {
  const translateX = useSharedValue(0);

  const handlePress = () => {
    translateX.value = withSpring(100); // Runs on UI thread
  };

  const animatedStyle = useAnimatedStyle(() => ({
    transform: [{ translateX: translateX.value }],
  }));

  return <Animated.View style={animatedStyle} />;
}
```

**2. Optimize Animation Properties:**

```jsx
// ✅ Good: Animate transform and opacity (GPU accelerated)
Animated.timing(animatedValue, {
  toValue: 1,
  useNativeDriver: true, // Works with transform/opacity
}).start();

// ❌ Bad: Animate width/height (not GPU accelerated)
Animated.timing(animatedValue, {
  toValue: 100,
  useNativeDriver: false, // Required for layout properties
}).start();

// ✅ Good: Use transform instead of width/height
const animatedStyle = {
  transform: [{ scaleX: animatedValue }], // GPU accelerated
};
```

### 🔹 Best Practices Summary

**Essential Optimizations:**

1. ✅ **Memoize Components**: Use `React.memo` for expensive components
2. ✅ **Memoize Callbacks**: Use `useCallback` for stable function references
3. ✅ **Memoize Values**: Use `useMemo` for expensive calculations
4. ✅ **Optimize Lists**: Use FlatList with proper props
5. ✅ **Avoid Inline Functions**: Don't create functions in render
6. ✅ **Avoid Inline Objects**: Don't create objects in render
7. ✅ **Clean Up Effects**: Always cleanup subscriptions, timers, listeners
8. ✅ **Use Native Driver**: Enable for animations when possible
9. ✅ **Optimize Images**: Resize, cache, use appropriate formats
10. ✅ **Code Split**: Lazy load routes and features

**Performance Checklist:**

- [ ] Components memoized where appropriate
- [ ] Callbacks memoized with `useCallback`
- [ ] Expensive calculations memoized with `useMemo`
- [ ] FlatList optimized with `getItemLayout`, `keyExtractor`
- [ ] No inline functions in render
- [ ] No inline objects in render
- [ ] All effects have cleanup
- [ ] Images optimized and cached
- [ ] Network requests debounced/throttled
- [ ] Bundle size optimized
- [ ] Animations use native driver
- [ ] Memory leaks prevented
- [ ] Performance monitored

**Performance Targets:**

* **Frame Rate**: Maintain 60fps (16.67ms per frame)
* **Time to Interactive**: < 3 seconds
* **Memory Usage**: Stable, no growth over time
* **Bundle Size**: < 2MB initial load
* **Network**: Efficient requests, proper caching
* **Scroll Performance**: Smooth 60fps scrolling

📌 **In simple terms**: React Native performance optimization involves preventing JavaScript thread blocking, minimizing re-renders through memoization, optimizing lists with FlatList, managing memory properly, optimizing network requests and images, reducing bundle size, and using native drivers for animations. Key techniques include React.memo, useCallback, useMemo, proper cleanup, code splitting, and performance monitoring.

---

## ⭐ Summary — 10-second Interview Version

> "React Native runs React code in JavaScript and uses a bridge (or JSI in new architecture) to communicate with native code. It renders to native mobile components instead of HTML. The new architecture with JSI, Fabric, and TurboModules eliminates serialization overhead and enables synchronous calls for better performance."

---

## ⭐ Extra Points (If Interviewer Asks More)

### What's the difference between the old bridge and new JSI architecture?

The old bridge used asynchronous message passing with JSON serialization - JavaScript and native code communicated by sending serialized messages, which added overhead. The new JSI (JavaScript Interface) architecture allows direct synchronous calls between JavaScript and native code without serialization. This eliminates the bridge overhead and enables better performance, especially for frequent operations like animations.

### How does React Native render to native components?

React Native uses a renderer (Fabric in the new architecture) that converts React components to native mobile components. When you write `<View>`, React Native creates a native UIView (iOS) or ViewGroup (Android). The renderer maintains a shadow tree (layout calculations) and updates native components when React state changes. This is different from web React, which renders to DOM elements.

### Can you use native modules in React Native?

Yes, you can create native modules to access platform-specific APIs or write performance-critical code in native languages (Java/Kotlin for Android, Objective-C/Swift for iOS). Native modules expose functions that can be called from JavaScript. The new TurboModules architecture makes this easier and more performant by allowing direct synchronous calls instead of going through the bridge.

---

