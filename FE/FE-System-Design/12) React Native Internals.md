# 📱 React Native Internals

---

## 📍 Navigation

<div align="center">

[← Previous: Node.js Internals](11%29%20Node.js%20Internals.md) • [Home: Questions Index](question.md) • [Next: Browser APIs →](13%29%20Browser%20APIs.md)

[📋 Cheatsheet](FE-System-Design%20Interview%20Cheatsheet.md)

</div>

---

---

## Q20. How React Native Works Internally

React Native allows you to build mobile apps using React, but instead of rendering to the web DOM, it renders to native mobile components. Understanding how React Native works internally helps you write better mobile apps, debug performance issues, and understand the bridge between JavaScript and native code. This knowledge is crucial for senior developers - it helps you understand why certain patterns work better, how to optimize React Native applications, and how to debug complex issues.

---

## 1. React Native Architecture

### 🔹 Core Concept

React Native uses the same React principles you know from web development, but with a key difference: instead of rendering to HTML elements, it renders to native mobile components.

* **JavaScript Thread**: Your React code runs here - components, state, props, hooks all work the same way as React web

* **Native Thread**: The actual native UI components live here - iOS uses UIKit, Android uses Android Views

* **Bridge**: This is the communication layer between JavaScript and native code - it's like a translator that converts JavaScript calls into native API calls

### 🔹 How It Works

When you write React Native code:

1. **You write JSX** just like React web - `<View>`, `<Text>`, `<Button>` etc.

2. **React Native transforms** your JSX into a description of what the UI should look like

3. **The Bridge serializes** this description and sends it to the native thread

4. **Native code creates** actual iOS/Android UI components based on that description

5. **User interactions** (taps, swipes) go back through the bridge to your JavaScript code

### 🔹 Platform Differences

* **iOS**: Uses UIKit components - `<View>` becomes `UIView`, `<Text>` becomes `UILabel`

* **Android**: Uses Android Views - `<View>` becomes `ViewGroup`, `<Text>` becomes `TextView`

* **Same Code**: You write once, React Native handles the platform differences for you

📌 **In simple terms**: React Native runs your React code in JavaScript, uses a bridge to communicate with native code, and renders to real native mobile components instead of HTML. You write once, it works on both iOS and Android.

---

## 2. The Bridge (Old Architecture)

### 🔹 What is the Bridge?

The bridge is like a message passing system between JavaScript and native code. It's asynchronous, which means JavaScript and native code don't block each other.

* **Asynchronous Communication**: JavaScript sends messages to native, native sends messages back - neither side waits for the other

* **Serialization**: Data gets converted to JSON-like format when crossing the bridge - this is necessary because JavaScript and native code use different data types

* **Message Queue**: Messages are queued and processed in batches - this is efficient but can add latency

### 🔹 How Bridge Communication Works

The bridge communication is asynchronous and involves serialization. Understanding this flow helps you understand performance implications.

**Step-by-Step Process:**

**1. JavaScript calls native:**

* You call a native module method from JavaScript

* Example: `NativeModules.Camera.takePicture(options)`

* This doesn't execute immediately - it's queued

**2. Serialization:**

* The bridge converts your JavaScript data (objects, arrays, strings, numbers) into JSON-like format

* This is necessary because JavaScript and native code use different data types

* Example: JavaScript object `{width: 100, height: 200}` becomes JSON string

* Serialization has overhead - can be slow for large objects

**3. Message sent:**

* The serialized message is added to a message queue

* Messages are batched for efficiency

* The queue is processed asynchronously

**4. Native processes:**

* Native code receives the message from the queue

* Deserializes the JSON back into native data types

* Executes the native method (e.g., takes a picture with camera)

* This happens on the native thread (doesn't block JavaScript)

**5. Response sent back:**

* Native code serializes the result (e.g., image data, error)

* Sends it back through the bridge (same serialization process)

* Added to the response queue

**6. JavaScript receives:**

* Your JavaScript code gets the response

* Usually through a callback or promise

* Deserialization happens automatically

* Example:

```javascript
NativeModules.Camera.takePicture(options, (error, image) => {
  // This callback runs when native code responds
  // image is deserialized from native format
});

```

**Performance Implications:**

* Serialization/deserialization adds latency

* Large objects take longer to serialize

* Frequent calls create queue buildup

* This is why animations can be janky with the old bridge

### 🔹 Bridge Limitations

Understanding bridge limitations helps you understand why the new architecture was needed.

**Serialization Overhead:**

* Converting data to/from JSON takes time

* Can be slow for large objects (images, large arrays)

* Every call has serialization cost

* Example: Sending a large image through the bridge is slow

**Asynchronous Only:**

* Everything is async, even if you need synchronous access

* Can complicate some use cases (e.g., reading layout measurements)

* You always need callbacks or promises

* Example: Can't synchronously read view dimensions (must use callback)

**Performance Bottleneck:**

* High-frequency calls (like animations) can be slow

* Bridge overhead accumulates with many calls

* Can cause janky animations (dropped frames)

* Example: 60fps animation = 60 calls per second = lots of bridge overhead

**Message Queue Delays:**

* Messages are queued and batched

* Can add latency even for simple operations

* Not suitable for real-time operations

* Example: Touch events might feel delayed

**Memory Overhead:**

* Serialized data takes memory

* Large objects in queue consume memory

* Can cause memory pressure

* Example: Queueing many large images can cause memory issues

📌 **In simple terms**: The bridge is an asynchronous message passing system between JavaScript and native code. It serializes data when crossing between the two worlds, which works but can be slow for frequent or large data transfers.

---

## 3. JavaScript Interface (JSI) - New Architecture

### 🔹 What is JSI?

JSI (JavaScript Interface) is the new architecture that allows direct communication between JavaScript and native code, eliminating the need for serialization and enabling synchronous calls when needed.

* **Direct Function Calls**: JavaScript can directly call native functions without going through a message queue

* **No Serialization**: Data is passed directly without conversion - much faster

* **Synchronous When Needed**: You can make synchronous calls when necessary, not just async

* **Better Performance**: Eliminates the bridge overhead, especially important for animations and high-frequency updates

### 🔹 How JSI Works

JSI enables direct communication between JavaScript and native code. Understanding how it works helps you understand the performance improvements.

**Step-by-Step Process:**

**1. Native modules register:**

* Native code registers its functions with JSI

* Functions are exposed to JavaScript

* Registration happens at startup or lazily

* Example: Camera module registers `takePicture` function

**2. JavaScript gets direct reference:**

* JavaScript gets a direct reference (pointer) to the native function

* No serialization needed - it's a direct memory reference

* This is much faster than bridge messages

* Example: `const takePicture = NativeModules.Camera.takePicture;`

**3. Direct call:**

* When you call the function, it executes immediately in native code

* No message queue, no batching delay

* Function executes synchronously (if designed that way)

* Example: `const result = takePicture(options);` - executes immediately

**4. No serialization:**

* Data is passed directly, no conversion needed

* JavaScript objects map directly to native objects

* Much faster than JSON serialization

* Example: Passing an object is instant, no conversion

**5. Synchronous or async:**

* You can choose based on your needs

* Synchronous for simple operations (read layout)

* Async for long-running operations (network requests)

* Example:

```javascript
// Synchronous - immediate result
const dimensions = view.measureSync();

// Async - for long operations
const image = await camera.takePictureAsync();

```

**Performance Benefits:**

* No serialization overhead (much faster)

* No message queue delays (immediate execution)

* Synchronous access when needed (better for animations)

* Direct memory access (more efficient)

### 🔹 JSI Benefits

* **Faster**: No serialization overhead means much faster communication

* **Type safety**: Better type checking and error handling

* **Synchronous access**: Can access native APIs synchronously when needed (like reading layout measurements)

* **Future-proof**: This is the foundation for React Native's new architecture

📌 **In simple terms**: JSI allows JavaScript to directly call native functions without serialization or message queues. It's faster, supports synchronous calls, and is the foundation of React Native's new architecture.

---

## 4. Fabric - New Rendering System

### 🔹 What is Fabric?

Fabric is React Native's new rendering system that uses JSI for better performance and enables synchronous UI updates.

* **New Renderer**: Replaces the old rendering system with one built on JSI

* **Synchronous Updates**: Can update the UI synchronously when needed - important for smooth animations

* **Better Performance**: More efficient rendering, especially for complex UIs

* **Improved Debugging**: Better tools for debugging rendering issues

### 🔹 How Fabric Works

1. **React renders**: Your React components render as usual

2. **Shadow Tree**: Fabric creates a "shadow tree" - a JavaScript representation of the native UI tree

3. **Direct updates**: Changes are applied directly to native components using JSI

4. **Synchronous when needed**: Layout calculations and updates can happen synchronously

5. **Better batching**: More efficient batching of updates

### 🔹 Fabric Benefits

* **Smoother animations**: Synchronous updates mean animations can be smoother

* **Better performance**: More efficient rendering pipeline

* **Improved debugging**: Better tools to see what's happening in the render process

* **Future features**: Enables new React features like concurrent rendering

📌 **In simple terms**: Fabric is the new rendering system that uses JSI for direct, synchronous UI updates. It makes animations smoother and rendering more efficient.

---

## 5. TurboModules - New Native Module System

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

### 🔹 TurboModules vs Old Modules

* **Old modules**: Loaded at startup, use bridge, always async, slower

* **TurboModules**: Loaded on demand, use JSI, can be sync, faster

📌 **In simple terms**: TurboModules are the new way to create native modules using JSI. These modules are faster, loaded on demand, and support synchronous calls when needed.

---

## 6. Threading Model

### 🔹 Thread Separation

React Native runs different parts of your app on different threads:

* **JavaScript Thread**: Your React code, state, business logic - single thread, event-driven

* **UI Thread (Main Thread)**: Native UI rendering, user interactions - iOS and Android each have their own main thread

* **Background Threads**: Native modules can use background threads for heavy work

### 🔹 Why Thread Separation?

* **Non-blocking**: JavaScript work doesn't block the UI thread - your app stays responsive

* **Performance**: Native UI rendering happens on the native thread, which is optimized for that platform

* **Parallelism**: JavaScript and native code can work at the same time

### 🔹 Communication Between Threads

* **Bridge (old)**: Asynchronous message passing between threads

* **JSI (new)**: Direct function calls, can be synchronous when needed

📌 **In simple terms**: React Native separates JavaScript execution from native UI rendering into different threads. This keeps the UI responsive while JavaScript code runs, and the bridge (or JSI) handles communication between them.

---

## 7. Component Rendering Process

### 🔹 How Components Render

1. **JSX written**: You write JSX like `<View><Text>Hello</Text></View>`

2. **React processes**: React creates a virtual representation (similar to Virtual DOM)

3. **Serialization (old)**: In old architecture, this gets serialized and sent through bridge

4. **Direct update (new)**: In new architecture, JSI directly updates native components

5. **Native renders**: Native code creates actual UI components (UIView on iOS, ViewGroup on Android)

### 🔹 Platform-Specific Rendering

* **iOS**: JSX `<View>` → `UIView`, `<Text>` → `UILabel`, `<Button>` → `UIButton`

* **Android**: JSX `<View>` → `ViewGroup`, `<Text>` → `TextView`, `<Button>` → `Button`

* **Styling**: React Native styles are converted to platform-specific styling (Auto Layout on iOS, ConstraintLayout on Android)

📌 **In simple terms**: Your JSX gets transformed into native UI components. React Native handles the conversion, so the same code works on both iOS and Android, even though the underlying native components are different.

---

## 8. State Management & Updates

### 🔹 State Updates Work the Same

React Native uses the same state management as React web:

* **useState**: Works exactly the same - manages component state

* **useEffect**: Same lifecycle management - runs after render, cleanup on unmount

* **Context**: Same context API for sharing state across components

* **Redux/MobX**: Same state management libraries work in React Native

### 🔹 Update Flow

1. **State changes**: You call `setState` or update state

2. **React re-renders**: React determines what changed

3. **Diffing**: React compares old and new virtual representation

4. **Updates sent**: Only the changes are sent to native (through bridge or JSI)

5. **Native updates**: Native components update efficiently

📌 **In simple terms**: State management works exactly like React web. When state changes, React figures out what changed and efficiently updates only those native components.

---

## ⭐ Summary — 10-second Interview Version

> "React Native runs React code in JavaScript and uses a bridge (or JSI in new architecture) to communicate with native code. It renders to native mobile components instead of HTML. The new architecture with JSI, Fabric, and TurboModules eliminates serialization overhead and enables synchronous calls for better performance."

---

---

## 📍 Navigation

<div align="center">

[07) Node.js Internals.md](07%29%20Node.js%20Internals.md) • [Questions Index](question.md) • [09) Browser APIs.md →](09%29%20Browser%20APIs.md)

[FE-System-Design Cheatsheet](FE-System-Design%20Interview%20Cheatsheet.md]

</div>

---
