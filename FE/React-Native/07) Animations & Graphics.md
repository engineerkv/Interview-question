# 7. Animations & Graphics (Q67–73)

---

## 📍 Navigation

<div align="center">

[Performance & Profiling](06%29%20Performance%20%26%20Profiling.md) • [Home: README](../README.md) • [Hardware & System APIs →](08%29%20Hardware%20%26%20System%20APIs.md)

[📋 Cheatsheet](React%20Native%20Interview%20Cheatsheet.md)

</div>

---

---

## Q67. 🎨 React Native Reanimated 2/3 and how it works

Reanimated 2/3 is a high-performance animation library that runs animations on the UI thread - provides smooth 60fps animations. UI thread animations (performance), Worklets (JavaScript functions that run on UI thread), Declarative API (ease of use).

- **Trade-offs**: The catch is requires native module setup (native dependency) - learning curve for worklets (learning curve). Provides smooth 60fps animations, but watch out - better performance than Animated API (performance).

Example:

```jsx
import Animated, {
  useSharedValue,
  useAnimatedStyle,
  withSpring,
} from 'react-native-reanimated';

function AnimatedComponent() {
  const translateX = useSharedValue(0);

  const animatedStyle = useAnimatedStyle(() => {
    return {
      transform: [{ translateX: translateX.value }],
    };
  });

  const handlePress = () => {
    translateX.value = withSpring(100);
  };

  return (
    <Animated.View style={animatedStyle}>
      <Button title="Animate" onPress={handlePress} />
    </Animated.View>
  );
}
```

---

## Q68. ⚡ Worklets and UI thread animations in Reanimated

Worklets are JavaScript functions that run on the UI thread, enabling synchronous animations - critical for smooth animations. UI thread execution (performance), Synchronous animations (smoothness), Uses JSI for direct communication (no bridge serialization).

- **Trade-offs**: The catch is worklets have limitations (worklet limitations) - cannot use all JavaScript features (feature restrictions). Critical for smooth animations, but watch out - worklets run on UI thread, not JS thread (execution context).

Example:

```jsx
import { useAnimatedStyle } from 'react-native-reanimated';

function WorkletExample() {
  const progress = useSharedValue(0);

  // This is a worklet - runs on UI thread
  const animatedStyle = useAnimatedStyle(() => {
    'worklet'; // Explicit worklet declaration
    return {
      opacity: progress.value,
      transform: [{ scale: 1 + progress.value * 0.5 }],
    };
  });

  return <Animated.View style={animatedStyle} />;
}
```

---

## Q69. 👆 Gesture handling with Reanimated

Reanimated Gesture Handler provides gesture recognition and animation integration - essential for interactive animations. Gesture recognition (touch handling), Animation integration (smooth transitions), Platform support (cross-platform).

- **Trade-offs**: The catch is requires react-native-gesture-handler (dependency) - learning curve for gesture API (learning curve). Essential for interactive animations, but watch out - provides better performance than PanResponder (performance).

Example:

```jsx
import { GestureDetector, Gesture } from 'react-native-gesture-handler';
import Animated, {
  useSharedValue,
  useAnimatedStyle,
  withSpring,
} from 'react-native-reanimated';

function GestureExample() {
  const translateX = useSharedValue(0);
  const translateY = useSharedValue(0);

  const pan = Gesture.Pan()
    .onUpdate((e) => {
      translateX.value = e.translationX;
      translateY.value = e.translationY;
    })
    .onEnd(() => {
      translateX.value = withSpring(0);
      translateY.value = withSpring(0);
    });

  const animatedStyle = useAnimatedStyle(() => {
    return {
      transform: [
        { translateX: translateX.value },
        { translateY: translateY.value },
      ],
    };
  });

  return (
    <GestureDetector gesture={pan}>
      <Animated.View style={animatedStyle} />
    </GestureDetector>
  );
}
```

---

## Q70. 🎨 React Native Skia and when to use it

React Native Skia is a 2D graphics library based on Skia graphics engine - provides custom drawing and advanced animations. Custom drawing (canvas-like API), Advanced animations (complex animations), High performance (native rendering).

- **Trade-offs**: The catch is requires native module (native dependency) - steeper learning curve (learning curve). Provides custom drawing and advanced animations, but watch out - use for complex graphics and animations (use cases).

Example:

```jsx
import { Canvas, Circle, LinearGradient, vec } from '@shopify/react-native-skia';

function SkiaExample() {
  return (
    <Canvas style={{ flex: 1 }}>
      <Circle cx={128} cy={128} r={64}>
        <LinearGradient
          start={vec(64, 64)}
          end={vec(192, 192)}
          colors={['#FF0000', '#0000FF']}
        />
      </Circle>
    </Canvas>
  );
}
```

---

## Q71. 🖌️ Custom drawing and animations with Skia

Skia provides canvas-like API for custom drawing and complex animations - essential for advanced graphics. Custom drawing (drawing API), Path operations (path API), Animations (animation API).

- **Trade-offs**: The catch is requires understanding graphics concepts (graphics knowledge) - more complex than standard components (complexity). Essential for advanced graphics, but watch out - use for custom charts, graphs, and animations (use cases).

Example:

```jsx
import { Canvas, Path, Skia } from '@shopify/react-native-skia';
import { useSharedValue, useAnimatedStyle } from 'react-native-reanimated';

function CustomDrawing() {
  const path = Skia.Path.Make();
  path.moveTo(0, 0);
  path.lineTo(100, 100);
  path.quadTo(150, 50, 200, 100);

  return (
    <Canvas style={{ flex: 1 }}>
      <Path path={path} color="blue" style="stroke" strokeWidth={2} />
    </Canvas>
  );
}
```

---

## Q72. ⚡ Performance considerations for animations

Optimize animations by using UI thread animations, avoiding unnecessary re-renders, and using appropriate animation libraries - performance is critical for smooth UX. UI thread animations (Reanimated), Avoid re-renders (optimization), Choose right library (library selection).

- **Trade-offs**: The catch is balance between performance and complexity (trade-offs) - test on real devices (device testing). Performance is critical for smooth UX, but watch out - measure animation performance (performance measurement).

Example:

```jsx
// ❌ Bad: Animated API (runs on JS thread)
import { Animated } from 'react-native';

// ✅ Good: Reanimated (runs on UI thread)
import Animated from 'react-native-reanimated';

// Performance tips:
// 1. Use Reanimated for complex animations
// 2. Avoid animating layout properties
// 3. Use native driver when possible
// 4. Test on low-end devices
```

---

## Q73. 🤔 Choosing between Reanimated and Skia

Reanimated is for animations and gestures, while Skia is for custom drawing and advanced graphics - choose based on use case. Reanimated (animations and gestures), Skia (custom drawing and graphics), Different use cases (use case selection).

- **Trade-offs**: The catch is Reanimated is easier to learn (learning curve) - Skia provides more flexibility (flexibility). Choose based on use case, but watch out - can use both together (combination).

Example:

```jsx
// Use Reanimated for:
// - UI animations
// - Gesture-based interactions
// - Transitions
// - Layout animations

// Use Skia for:
// - Custom charts and graphs
// - Complex graphics
// - Custom drawing
// - Advanced visual effects

// Can combine both:
import Animated from 'react-native-reanimated';
import { Canvas } from '@shopify/react-native-skia';

function CombinedExample() {
  const progress = useSharedValue(0);
  // Use Reanimated for animation value
  // Use Skia for custom drawing
}
```

---

---

## 📍 Navigation

<div align="center">

[Performance & Profiling](06%29%20Performance%20%26%20Profiling.md) • [Home: README](../README.md) • [Hardware & System APIs →](08%29%20Hardware%20%26%20System%20APIs.md)

[📋 Cheatsheet](React%20Native%20Interview%20Cheatsheet.md)

</div>

---
