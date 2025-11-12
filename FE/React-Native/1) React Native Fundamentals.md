# ⚛️ 1. React Native Fundamentals (Q1–10)

---

## 🧩 Q1. What is React Native, and how is it different from React.js?

### 🧠 Concept

React Native is a framework for building mobile applications using React, but instead of rendering to the web DOM, it renders to native mobile components. Handles platform-specific UI patterns and behaviors.

---

### 💡 Example

```jsx
import React from 'react';
import { View, Text, StyleSheet } from 'react-native';

function App() {
  return (
    <View style={styles.container}>
      <Text style={styles.title}>Hello React Native!</Text>
    </View>
  );
}

const styles = StyleSheet.create({
  container: { flex: 1, justifyContent: 'center', alignItems: 'center' },
  title: { fontSize: 24, fontWeight: 'bold' }
});
```

---

### 🔍 Deep Insights

* **Rule:** Designed specifically for iOS and Android development (mobile focus).
* **Use Case:** Renders to native UI components, not HTML elements (native components).
* **Common Mistake:** Write once, run on both iOS and Android (cross-platform).
* **Pro Tip:** Near-native performance through native rendering.

---

### ⭐ Senior Takeaway

Handles platform-specific UI patterns and behaviors.

---

## 🧩 Q2. How does React Native render UI on mobile devices? Explain the bridge concept.

### 🧠 Concept

React Native uses a bridge to communicate between JavaScript and native code, translating JavaScript calls into native platform APIs. JSI replaces bridge for better performance (new architecture).

---

### 💡 Example

```jsx
import { View, Text } from 'react-native';

function MyComponent() {
  return (
    <View>
      <Text>Hello from JavaScript!</Text>
    </View>
  );
}

// Bridge translates JSX to native calls
// <View> -> UIView (iOS) / ViewGroup (Android)
// <Text> -> UILabel (iOS) / TextView (Android)
```

---

### 🔍 Deep Insights

* **Rule:** Asynchronous communication between JS and native threads (bridge communication).
* **Use Case:** Data is serialized when crossing the bridge.
* **Common Mistake:** JavaScript runs on separate thread from native UI (thread separation).
* **Pro Tip:** Bridge communication can cause performance bottlenecks.

---

### ⭐ Senior Takeaway

JSI replaces bridge for better performance (new architecture).

---

## 🧩 Q3. What is the JavaScript Interface (JSI) and how does it work?

### 🧠 Concept

JSI is a new architecture that allows direct communication between JavaScript and native code, eliminating the need for the bridge and improving performance. Foundation for new React Native architecture (future-proof).

---

### 💡 Example

```jsx
// Old Bridge approach (serialized)
const result = await NativeModules.MyModule.doSomething(data);

// JSI approach (direct function call)
const result = MyModule.doSomething(data);
```

---

### 🔍 Deep Insights

* **Rule:** JavaScript can directly call native functions (direct communication).
* **Use Case:** Enables synchronous communication when needed (synchronous calls).
* **Common Mistake:** Eliminates serialization overhead (better performance).
* **Pro Tip:** Better type checking and error handling (type safety).

---

### ⭐ Senior Takeaway

Foundation for new React Native architecture (future-proof).

---

## 🧩 Q4. What are Fabric and TurboModules in React Native?

### 🧠 Concept

Fabric is the new rendering system, while TurboModules are the new native module system, both designed to improve performance and enable synchronous communication. New architecture significantly improves performance.

---

### 💡 Example

```jsx
// Fabric - New rendering system
import { View, Text } from 'react-native';

function MyComponent() {
  return (
    <View>
      <Text>Fabric renders this efficiently</Text>
    </View>
  );
}

// TurboModules - New native module system
import { TurboModuleRegistry } from 'react-native';
const MyTurboModule = TurboModuleRegistry.get('MyTurboModule');
```

---

### 🔍 Deep Insights

* **Rule:** Fabric (new rendering system with better performance and debugging), TurboModules (new native module system using JSI).
* **Use Case:** Enables synchronous UI updates (synchronous rendering).
* **Common Mistake:** Improved debugging capabilities (better debugging).
* **Pro Tip:** Works with existing code while providing new features (backward compatibility).

---

### ⭐ Senior Takeaway

New architecture significantly improves performance.

---

## 🧩 Q5. How does JavaScript communicate with native code?

### 🧠 Concept

React Native uses the bridge (or JSI in new architecture) to serialize data and pass it between JavaScript and native threads. Bridge communication can be a bottleneck for high-frequency calls (performance).

---

### 💡 Example

```jsx
import { NativeModules } from 'react-native';

const { MyNativeModule } = NativeModules;

MyNativeModule.doSomething('Hello from JS', (result) => {
  console.log('Native response:', result);
});

const data = { name: 'John', age: 30 };
MyNativeModule.processData(data);
```

---

### 🔍 Deep Insights

* **Rule:** Bridge protocol defines how data is serialized and passed.
* **Use Case:** Uses message queue for asynchronous communication.
* **Common Mistake:** Supports specific data types (strings, numbers, objects, arrays).
* **Pro Tip:** Handles errors and exceptions across the bridge.

---

### ⭐ Senior Takeaway

Bridge communication can be a bottleneck for high-frequency calls (performance).

---

## 🧩 Q6. What are the differences between iOS and Android rendering in React Native?

### 🧠 Concept

iOS uses UIKit components while Android uses Android Views, with different styling systems and platform-specific optimizations. Same code renders differently on each platform.

---

### 💡 Example

```jsx
<View style={styles.container}>
  <Text style={styles.text}>Hello</Text>
</View>

// Renders as:
// iOS: UIView with UILabel
// Android: ViewGroup with TextView

const styles = StyleSheet.create({
  container: {
    flex: 1,
    // iOS: Uses Auto Layout
    // Android: Uses ConstraintLayout
  }
});
```

---

### 🔍 Deep Insights

* **Rule:** iOS UIKit uses UIKit components and Auto Layout, Android Views uses Android View system and ConstraintLayout.
* **Use Case:** Different default values and behaviors (styling differences).
* **Common Mistake:** Platform-specific optimizations (performance).
* **Pro Tip:** Different native APIs and capabilities (platform APIs).

---

### ⭐ Senior Takeaway

Same code renders differently on each platform.

---

## 🧩 Q7. What is Metro bundler and how does it work?

### 🧠 Concept

Metro is the JavaScript bundler that transforms, bundles, and serves React Native code, similar to Webpack for web applications. Handles platform-specific code splitting.

---

### 💡 Example

```jsx
// metro.config.js
module.exports = {
  transformer: {
    getTransformOptions: async () => ({
      transform: {
        experimentalImportSupport: false,
        inlineRequires: true,
      },
    }),
  },
  resolver: {
    assetExts: ['bin', 'txt', 'jpg', 'png', 'json'],
  },
};
```

---

### 🔍 Deep Insights

* **Rule:** Bundles JavaScript code for mobile (JavaScript bundling).
* **Use Case:** Processes images, fonts, and other assets (asset handling).
* **Common Mistake:** Enables hot reloading and fast refresh.
* **Pro Tip:** Removes unused code to reduce bundle size (tree shaking).

---

### ⭐ Senior Takeaway

Handles platform-specific code splitting.

---

## 🧩 Q8. What is the difference between Live Reload, Hot Reload, and Fast Refresh?

### 🧠 Concept

Live Reload reloads the entire app, Hot Reload updates components without losing state, and Fast Refresh is the improved version that combines both features. Fast Refresh is the recommended approach.

---

### 💡 Example

```jsx
function Counter() {
  const [count, setCount] = useState(0);
  
  return (
    <View>
      <Text>Count: {count}</Text>
      <Button title="Increment" onPress={() => setCount(count + 1)} />
    </View>
  );
}

// Fast Refresh preserves state when you edit this component
// Live Reload would reset count to 0
// Hot Reload would keep count value
```

---

### 🔍 Deep Insights

* **Rule:** Live Reload reloads entire app, loses all state; Hot Reload updates components while preserving state; Fast Refresh combines both with better error recovery.
* **Use Case:** Improves developer productivity (development experience).
* **Common Mistake:** Maintains component state during updates (state preservation).
* **Pro Tip:** Better error recovery than Hot Reload.

---

### ⭐ Senior Takeaway

Fast Refresh is the recommended approach.

---

## 🧩 Q9. What are the built-in components in React Native?

### 🧠 Concept

React Native provides core components like View (container), Text (text display), Image (images), FlatList (efficient lists), and ScrollView (scrollable content). These are the building blocks of React Native apps.

---

### 💡 Example

```jsx
import { View, Text, Image, FlatList, ScrollView } from 'react-native';

function MyScreen() {
  const data = [
    { id: '1', title: 'Item 1' },
    { id: '2', title: 'Item 2' }
  ];

  return (
    <ScrollView>
      <View>
        <Text>Hello World</Text>
        <Image source={{ uri: 'https://example.com/image.jpg' }} />
        <FlatList data={data} renderItem={({ item }) => <Text>{item.title}</Text>} />
      </View>
    </ScrollView>
  );
}
```

---

### 🔍 Deep Insights

* **Rule:** View (basic container component, equivalent to div), Text (text display component, equivalent to span/p), Image (image display component with optimization).
* **Use Case:** FlatList (efficient list component with virtualization), ScrollView (scrollable container for content).
* **Common Mistake:** All components are optimized for mobile.
* **Pro Tip:** FlatList provides virtualization for large lists.

---

### ⭐ Senior Takeaway

These are the building blocks of React Native apps.

---

## 🧩 Q10. How does Flexbox work in React Native compared to CSS?

### 🧠 Concept

React Native uses a subset of Flexbox with some differences in default values and behavior, optimized for mobile layouts. Designed for touch interfaces and mobile layouts (mobile optimized).

---

### 💡 Example

```jsx
const styles = StyleSheet.create({
  container: {
    flex: 1,
    flexDirection: 'column', // Default in RN (row in CSS)
    justifyContent: 'center',
    alignItems: 'center',
    backgroundColor: '#f0f0f0'
  },
  item: {
    flex: 1,
    margin: 10
  }
});
```

---

### 🔍 Deep Insights

* **Rule:** Column by default (row in CSS) (default direction).
* **Use Case:** Different behavior and default values (flex property).
* **Common Mistake:** No float property in React Native (no float).
* **Pro Tip:** Simplified positioning system (position).

---

### ⭐ Senior Takeaway

Designed for touch interfaces and mobile layouts (mobile optimized).

---
