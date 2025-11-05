# ⚛️ 1. React Native Fundamentals (Q1–10)

---

## 1) What is React Native, and how is it different from React.js?

React Native is a framework for building mobile applications using React, but instead of rendering to the web DOM, it renders to native mobile components.

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

- **Core Difference**: Designed specifically for iOS and Android development (mobile focus)
- **Real-World Use**: Renders to native UI components, not HTML elements (native components)
- **Common Advantage**: Write once, run on both iOS and Android (cross-platform)
- **Performance**: Near-native performance through native rendering
- **Interview Tip**: Explain that handles platform-specific UI patterns and behaviors

---

## 2) How does React Native render UI on mobile devices? Explain the bridge concept.

React Native uses a bridge to communicate between JavaScript and native code, translating JavaScript calls into native platform APIs.

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

- **Core Concept**: Asynchronous communication between JS and native threads (bridge communication)
- **Real-World Process**: Data is serialized when crossing the bridge
- **Architecture**: JavaScript runs on separate thread from native UI (thread separation)
- **Performance Impact**: Bridge communication can cause performance bottlenecks
- **Interview Tip**: Explain that JSI replaces bridge for better performance (new architecture)

---

## 3) What is the **JavaScript Interface (JSI)**, and how does it improve performance?

JSI is a new architecture that allows direct communication between JavaScript and native code, eliminating the need for the bridge and improving performance.

```jsx
// Old Bridge approach (serialized)
const result = await NativeModules.MyModule.doSomething(data);

// JSI approach (direct function call)
const result = MyModule.doSomething(data);
```

- **Core Advantage**: JavaScript can directly call native functions (direct communication)
- **Real-World Benefit**: Enables synchronous communication when needed (synchronous calls)
- **Performance**: Eliminates serialization overhead (better performance)
- **Advanced Feature**: Better type checking and error handling (type safety)
- **Interview Tip**: Explain that foundation for new React Native architecture (future-proof)

---

## 4) What are **Fabric** and **TurboModules**, and how do they improve React Native's new architecture?

Fabric is the new rendering system, while TurboModules are the new native module system, both designed to improve performance and enable synchronous communication.

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

- **Core Components**: Fabric (new rendering system with better performance and debugging), TurboModules (new native module system using JSI)
- **Real-World Benefit**: Enables synchronous UI updates (synchronous rendering)
- **Common Advantage**: Improved debugging capabilities (better debugging)
- **Advanced Feature**: Works with existing code while providing new features (backward compatibility)
- **Interview Tip**: Explain that new architecture significantly improves performance

---

## 5) How does React Native communicate between JavaScript and native code internally?

React Native uses the bridge (or JSI in new architecture) to serialize data and pass it between JavaScript and native threads.

```jsx
import { NativeModules } from 'react-native';

const { MyNativeModule } = NativeModules;

MyNativeModule.doSomething('Hello from JS', (result) => {
  console.log('Native response:', result);
});

const data = { name: 'John', age: 30 };
MyNativeModule.processData(data);
```

- **Core Mechanism**: Bridge protocol defines how data is serialized and passed
- **Real-World Process**: Uses message queue for asynchronous communication
- **Common Support**: Supports specific data types (strings, numbers, objects, arrays)
- **Error Handling**: Handles errors and exceptions across the bridge
- **Interview Tip**: Explain that bridge communication can be a bottleneck for high-frequency calls (performance)

---

## 6) What are the key differences between React Native rendering on iOS vs Android?

iOS uses UIKit components while Android uses Android Views, with different styling systems and platform-specific optimizations.

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

- **Core Platforms**: iOS UIKit uses UIKit components and Auto Layout, Android Views uses Android View system and ConstraintLayout
- **Real-World Impact**: Different default values and behaviors (styling differences)
- **Common Optimization**: Platform-specific optimizations (performance)
- **Advanced Feature**: Different native APIs and capabilities (platform APIs)
- **Interview Tip**: Explain that same code renders differently on each platform

---

## 7) What is the role of the **Metro bundler** in React Native?

Metro is the JavaScript bundler that transforms, bundles, and serves React Native code, similar to Webpack for web applications.

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

- **Core Purpose**: Bundles JavaScript code for mobile (JavaScript bundling)
- **Real-World Use**: Processes images, fonts, and other assets (asset handling)
- **Common Benefit**: Enables hot reloading and fast refresh
- **Advanced Feature**: Removes unused code to reduce bundle size (tree shaking)
- **Interview Tip**: Explain that handles platform-specific code splitting

---

## 8) What is the difference between **Live Reload**, **Hot Reload**, and **Fast Refresh**?

Live Reload reloads the entire app, Hot Reload updates components without losing state, and Fast Refresh is the improved version that combines both features.

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

- **Core Differences**: Live Reload reloads entire app, loses all state; Hot Reload updates components while preserving state; Fast Refresh combines both with better error recovery
- **Real-World Benefit**: Improves developer productivity (development experience)
- **Common Advantage**: Maintains component state during updates (state preservation)
- **Advanced Feature**: Better error recovery than Hot Reload
- **Interview Tip**: Explain that Fast Refresh is the recommended approach

---

## 9) What are the common built-in React Native components (View, Text, Image, FlatList, ScrollView)?

React Native provides core components like View (container), Text (text display), Image (images), FlatList (efficient lists), and ScrollView (scrollable content).

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

- **Core Components**: View (basic container component, equivalent to div), Text (text display component, equivalent to span/p), Image (image display component with optimization)
- **Real-World Use**: FlatList (efficient list component with virtualization), ScrollView (scrollable container for content)
- **Common Advantage**: All components are optimized for mobile
- **Advanced Feature**: FlatList provides virtualization for large lists
- **Interview Tip**: Explain that these are the building blocks of React Native apps

---

## 10) How does **Flexbox layout** in React Native differ from CSS on the web?

React Native uses a subset of Flexbox with some differences in default values and behavior, optimized for mobile layouts.

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

- **Core Difference**: Column by default (row in CSS) (default direction)
- **Real-World Impact**: Different behavior and default values (flex property)
- **Common Limitation**: No float property in React Native (no float)
- **Advanced Feature**: Simplified positioning system (position)
- **Interview Tip**: Explain that designed for touch interfaces and mobile layouts (mobile optimized)

---
