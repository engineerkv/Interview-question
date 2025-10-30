# ⚛️ 1. React Native Fundamentals (Q1–10)

---

## 1) What is React Native, and how is it different from React.js?

Concept:
React Native is a framework for building mobile applications using React, but instead of rendering to the web DOM, it renders to native mobile components.

Example:
```jsx
// React Native component
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

Deep Insight:
- **Mobile Focus**: Designed specifically for iOS and Android development
- **Native Components**: Renders to native UI components, not HTML elements
- **Cross-Platform**: Write once, run on both iOS and Android
- **Performance**: Near-native performance through native rendering
- **Platform Differences**: Handles platform-specific UI patterns and behaviors

---

## 2) How does React Native render UI on mobile devices? Explain the bridge concept.

Concept:
React Native uses a bridge to communicate between JavaScript and native code, translating JavaScript calls into native platform APIs.

Example:
```jsx
// JavaScript side
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

Deep Insight:
- **Bridge Communication**: Asynchronous communication between JS and native threads
- **Serialization**: Data is serialized when crossing the bridge
- **Thread Separation**: JavaScript runs on separate thread from native UI
- **Performance Impact**: Bridge communication can cause performance bottlenecks
- **New Architecture**: JSI replaces bridge for better performance

---

## 3) What is the **JavaScript Interface (JSI)**, and how does it improve performance?

Concept:
JSI is a new architecture that allows direct communication between JavaScript and native code, eliminating the need for the bridge and improving performance.

Example:
```jsx
// Old Bridge approach (serialized)
const result = await NativeModules.MyModule.doSomething(data);

// JSI approach (direct function call)
const result = MyModule.doSomething(data);
```

Deep Insight:
- **Direct Communication**: JavaScript can directly call native functions
- **Synchronous Calls**: Enables synchronous communication when needed
- **Better Performance**: Eliminates serialization overhead
- **Type Safety**: Better type checking and error handling
- **Future-Proof**: Foundation for new React Native architecture

---

## 4) What are **Fabric** and **TurboModules**, and how do they improve React Native's new architecture?

Concept:
Fabric is the new rendering system, while TurboModules are the new native module system, both designed to improve performance and enable synchronous communication.

Example:
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

Deep Insight:
- **Fabric**: New rendering system with better performance and debugging
- **TurboModules**: New native module system using JSI
- **Synchronous Rendering**: Enables synchronous UI updates
- **Better Debugging**: Improved debugging capabilities
- **Backward Compatibility**: Works with existing code while providing new features

---

## 5) How does React Native communicate between JavaScript and native code internally?

Concept:
React Native uses the bridge (or JSI in new architecture) to serialize data and pass it between JavaScript and native threads.

Example:
```jsx
// JavaScript calling native module
import { NativeModules } from 'react-native';

const { MyNativeModule } = NativeModules;

// This call goes through the bridge
MyNativeModule.doSomething('Hello from JS', (result) => {
  console.log('Native response:', result);
});

// Data is serialized when crossing the bridge
const data = { name: 'John', age: 30 };
MyNativeModule.processData(data);
```

Deep Insight:
- **Bridge Protocol**: Defines how data is serialized and passed
- **Message Queue**: Uses message queue for asynchronous communication
- **Data Types**: Supports specific data types (strings, numbers, objects, arrays)
- **Error Handling**: Handles errors and exceptions across the bridge
- **Performance**: Bridge communication can be a bottleneck for high-frequency calls

---

## 6) What are the key differences between React Native rendering on iOS vs Android?

Concept:
iOS uses UIKit components while Android uses Android Views, with different styling systems and platform-specific optimizations.

Example:
```jsx
// Same React Native code
<View style={styles.container}>
  <Text style={styles.text}>Hello</Text>
</View>

// Renders as:
// iOS: UIView with UILabel
// Android: ViewGroup with TextView

// Platform-specific styling
const styles = StyleSheet.create({
  container: {
    flex: 1,
    // iOS: Uses Auto Layout
    // Android: Uses ConstraintLayout
  }
});
```

Deep Insight:
- **iOS UIKit**: Uses UIKit components and Auto Layout
- **Android Views**: Uses Android View system and ConstraintLayout
- **Styling Differences**: Different default values and behaviors
- **Performance**: Platform-specific optimizations
- **Platform APIs**: Different native APIs and capabilities

---

## 7) What is the role of the **Metro bundler** in React Native?

Concept:
Metro is the JavaScript bundler that transforms, bundles, and serves React Native code, similar to Webpack for web applications.

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

Deep Insight:
- **JavaScript Bundling**: Bundles JavaScript code for mobile
- **Asset Handling**: Processes images, fonts, and other assets
- **Hot Reloading**: Enables hot reloading and fast refresh
- **Tree Shaking**: Removes unused code to reduce bundle size
- **Platform Support**: Handles platform-specific code splitting

---

## 8) What is the difference between **Live Reload**, **Hot Reload**, and **Fast Refresh**?

Concept:
Live Reload reloads the entire app, Hot Reload updates components without losing state, and Fast Refresh is the improved version that combines both features.

Example:
```jsx
// Fast Refresh example
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

Deep Insight:
- **Live Reload**: Reloads entire app, loses all state
- **Hot Reload**: Updates components while preserving state
- **Fast Refresh**: Combines both with better error recovery
- **Development Experience**: Improves developer productivity
- **State Preservation**: Maintains component state during updates

---

## 9) What are the common built-in React Native components (View, Text, Image, FlatList, ScrollView)?

Concept:
React Native provides core components like View (container), Text (text display), Image (images), FlatList (efficient lists), and ScrollView (scrollable content).

Example:
```jsx
import React from 'react';
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

Deep Insight:
- **View**: Basic container component, equivalent to div
- **Text**: Text display component, equivalent to span/p
- **Image**: Image display component with optimization
- **FlatList**: Efficient list component with virtualization
- **ScrollView**: Scrollable container for content

---

## 10) How does **Flexbox layout** in React Native differ from CSS on the web?

Concept:
React Native uses a subset of Flexbox with some differences in default values and behavior, optimized for mobile layouts.

Example:
```jsx
// React Native Flexbox
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

Deep Insight:
- **Default Direction**: Column by default (row in CSS)
- **Flex Property**: Different behavior and default values
- **No Float**: No float property in React Native
- **Position**: Simplified positioning system
- **Mobile Optimized**: Designed for touch interfaces and mobile layouts

---
