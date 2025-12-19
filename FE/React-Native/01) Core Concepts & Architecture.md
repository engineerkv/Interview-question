# 1. Core Concepts & Architecture (Q1–10)

---

## 📍 Navigation

<div align="center">

[Home: README](../README.md) • [State Management & Data Persistence →](02%29%20State%20Management%20%26%20Data%20Persistence.md)

[📋 Cheatsheet](React%20Native%20Interview%20Cheatsheet.md)

</div>

---

---

## Q1. 📱 React Native and how it differs from React.js

React Native is a framework for building mobile applications using React, but instead of rendering to the web DOM, it renders to native mobile components - handles platform-specific UI patterns and behaviors. Designed specifically for iOS and Android development (mobile focus).

- **Trade-offs**: The catch is write once, run on both iOS and Android (cross-platform) - near-native performance through native rendering. Handles platform-specific UI patterns and behaviors, but watch out - renders to native UI components, not HTML elements (native components).

Example:

```jsx
import React from 'react';
import { View, Text, StyleSheet } from 'react-native'; // Native components, not HTML

function App() {
  return (
    <View style={styles.container}> {/* View = div equivalent, renders to native View */}
      <Text style={styles.title}>Hello React Native!</Text> {/* Text = p/span equivalent */}
    </View>
  );
}

// StyleSheet: optimized styling for React Native (not CSS)
const styles = StyleSheet.create({
  container: { flex: 1, justifyContent: 'center', alignItems: 'center' },
  title: { fontSize: 24, fontWeight: 'bold' }
});

```

---

## Q2. 📱 How React Native renders UI on mobile devices and JSI

React Native uses JSI (New Architecture) to communicate between JavaScript and native code, translating JavaScript calls into native platform APIs - New Architecture uses JSI and Fabric for better performance (stable in 0.73+). Direct calls between JS and native threads (JSI).

- **Trade-offs**: The catch is JavaScript runs on separate thread from native UI (thread separation) - JSI enables direct communication without serialization. New Architecture uses JSI and Fabric for better performance (stable in 0.73+), but watch out - JSI enables direct calls without serialization overhead (no serialization).

Example:

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

## Q3. 📋 JavaScript Interface (JSI) and how it works

JSI is the New Architecture that allows direct communication between JavaScript and native code, eliminating the need for the bridge and improving performance - part of React Native's New Architecture (stable in 0.73+). JavaScript can directly call native functions (direct communication).

- **Trade-offs**: The catch is eliminates serialization overhead (better performance, 20-500x faster) - better type checking and error handling through codegen (type safety). Part of React Native's New Architecture (stable in 0.73+), but watch out - enables synchronous communication when needed (synchronous calls).

Example:

```jsx
// JSI approach (New Architecture, direct function call, ~0.01-0.1ms)
import { TurboModuleRegistry } from 'react-native';
const MyModule = TurboModuleRegistry.get('MyModule');
const result = await MyModule.doSomething(data); // Can be synchronous
```

---

## Q4. 📱 Fabric and TurboModules in React Native

Fabric is the new rendering system, while TurboModules are the new native module system, both part of React Native's New Architecture (stable in 0.73+) - designed to improve performance and enable synchronous communication. Fabric (new rendering system with better performance, priority-based updates, concurrent rendering), TurboModules (new native module system using JSI with lazy loading and codegen).

- **Trade-offs**: The catch is improved debugging capabilities and performance (20-500x faster) - works with existing code while providing new features (backward compatibility). New Architecture is stable in 0.73+, but watch out - enables synchronous UI updates and direct native calls (synchronous rendering and communication).

Example:

```jsx
// Fabric - New rendering system (automatic in New Architecture)
import { View, Text } from 'react-native';

function MyComponent() {
  return (
    <View>
      <Text>Fabric renders this efficiently with priority-based updates</Text>
    </View>
  );
}

// TurboModules - New native module system
import { TurboModuleRegistry } from 'react-native';

// Lazy loaded - module loads on first use
const MyTurboModule = TurboModuleRegistry.get('MyTurboModule');
const result = await MyTurboModule.doSomething(); // Direct JSI call
```

---

## Q5. 📱 How JavaScript communicates with native code

React Native uses JSI (New Architecture) to communicate between JavaScript and native threads - uses direct calls without serialization (better performance). JSI enables direct function calls with lazy loading and type safety.

- **Trade-offs**: The catch is JSI supports all data types (strings, numbers, objects, arrays) without serialization overhead - eliminates serialization (20-500x faster). Uses direct calls with lazy loading and type safety through codegen, but watch out - enables synchronous communication when needed (synchronous calls).

Example:

```jsx
// New Architecture - JSI/TurboModules (direct calls, no serialization)
import { TurboModuleRegistry } from 'react-native';
const MyTurboModule = TurboModuleRegistry.get('MyTurboModule');
const result = await MyTurboModule.doSomething('Hello from JS'); // Direct call
const syncResult = MyTurboModule.processDataSync({ name: 'John', age: 30 }); // Synchronous
```

---

## Q6. 📱 Differences between iOS and Android rendering in React Native

iOS uses UIKit components while Android uses Android Views, with different styling systems and platform-specific optimizations - same code renders differently on each platform. iOS UIKit uses UIKit components and Auto Layout, Android Views uses Android View system and ConstraintLayout.

- **Trade-offs**: The catch is different default values and behaviors (styling differences) - different native APIs and capabilities (platform APIs). Same code renders differently on each platform, but watch out - platform-specific optimizations (performance).

Example:

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

## Q7. 🔧 Metro bundler and how it works

Metro is the JavaScript bundler that transforms, bundles, and serves React Native code, similar to Webpack for web applications - handles platform-specific code splitting. Bundles JavaScript code for mobile (JavaScript bundling).

- **Trade-offs**: The catch is enables hot reloading and fast refresh - removes unused code to reduce bundle size (tree shaking). Handles platform-specific code splitting, but watch out - processes images, fonts, and other assets (asset handling).

Example:

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

## Q8. 🤔 Difference between Live Reload, Hot Reload, and Fast Refresh

Live Reload reloads the entire app, Hot Reload updates components without losing state, and Fast Refresh is the improved version that combines both features - Fast Refresh is the recommended approach. Live Reload reloads entire app, loses all state; Hot Reload updates components while preserving state; Fast Refresh combines both with better error recovery.

- **Trade-offs**: The catch is maintains component state during updates (state preservation) - better error recovery than Hot Reload. Fast Refresh is the recommended approach, but watch out - improves developer productivity (development experience).

Example:

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

## Q9. 🧩 Built-in components in React Native

React Native provides core components like View (container), Text (text display), Image (images), FlatList (efficient lists), and ScrollView (scrollable content) - these are the building blocks of React Native apps. View (basic container component, equivalent to div), Text (text display component, equivalent to span/p), Image (image display component with optimization).

- **Trade-offs**: The catch is all components are optimized for mobile - FlatList provides virtualization for large lists. These are the building blocks of React Native apps, but watch out - FlatList (efficient list component with virtualization), ScrollView (scrollable container for content).

Example:

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

## Q10. 🎨 How Flexbox works in React Native compared to CSS

React Native uses a subset of Flexbox with some differences in default values and behavior, optimized for mobile layouts - designed for touch interfaces and mobile layouts (mobile optimized). Column by default (row in CSS) (default direction).

- **Trade-offs**: The catch is no float property in React Native (no float) - simplified positioning system (position). Designed for touch interfaces and mobile layouts (mobile optimized), but watch out - different behavior and default values (flex property).

Example:

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

---

## 📍 Navigation

<div align="center">

[Home: README](../README.md) • [State Management & Data Persistence →](02%29%20State%20Management%20%26%20Data%20Persistence.md)

[📋 Cheatsheet](React%20Native%20Interview%20Cheatsheet.md)

</div>

---
