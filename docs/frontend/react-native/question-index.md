---
sidebar_label: "Question Index"
sidebar_position: 0
---
# ⚛️ React Native Interview Questions

122 carefully curated questions covering React Native fundamentals to advanced platform internals.

## 📋 Quick Navigation

| Section | Topic | Questions | Difficulty |
|---------|-------|-----------|------------|
| [1️⃣](#1-core-concepts--architecture) | Core Concepts & Architecture | Q1–10 | ⭐⭐ |
| [2️⃣](#2-state-management--data-persistence) | State Management & Data Persistence | Q11–21 | ⭐⭐⭐ |
| [3️⃣](#3-navigation--app-lifecycle) | Navigation & App Lifecycle | Q22–30 | ⭐⭐⭐ |
| [4️⃣](#4-native-modules--platform-apis) | Native Modules & Platform APIs | Q32–39 | ⭐⭐⭐ |
| [5️⃣](#5-platform-specific-development) | Platform-Specific Development | Q42–51 | ⭐⭐⭐ |
| [6️⃣](#6-performance--profiling) | Performance & Profiling | Q52–66 | ⭐⭐⭐⭐ |
| [7️⃣](#7-animations--graphics) | Animations & Graphics | Q67–73 | ⭐⭐⭐⭐ |
| [8️⃣](#8-hardware--system-apis) | Hardware & System APIs | Q74–84 | ⭐⭐⭐⭐⭐ |
| [9️⃣](#9-testing--debugging) | Testing & Debugging | Q85–98 | ⭐⭐⭐⭐ |
| [🔟](#10-build--release-management) | Build & Release Management | Q99–112 | ⭐⭐⭐⭐⭐ |
| [1️⃣1️⃣](#11-over-the-air-updates) | Over-The-Air Updates | Q113–120 | ⭐⭐⭐⭐ |
| [1️⃣2️⃣](#12-notifications--messaging) | Notifications & Messaging | Q121–125 | ⭐⭐⭐ |

## ⚛️ 1. Core Concepts & Architecture

1. React Native and how it differs from React.js

2. How React Native renders UI on mobile devices and the bridge concept

3. JavaScript Interface (JSI) and how it works

4. Fabric and TurboModules in React Native

5. How JavaScript communicates with native code

6. Differences between iOS and Android rendering in React Native

7. Metro bundler and how it works

8. Difference between Live Reload, Hot Reload, and Fast Refresh

9. Built-in components in React Native

10. How Flexbox works in React Native compared to CSS

## 🗃️ 2. State Management & Data Persistence

11. State management tools available for React Native

12. Implementing Redux Toolkit in React Native

13. Using Recoil for state management

14. Implementing Zustand for state management

15. Using MobX for state management

16. Using Context API for state management

17. Persisting data locally with AsyncStorage

18. MMKV and how it compares to AsyncStorage

19. Implementing offline-first apps

20. Handling background data synchronization

21. Implementing data batching for performance

## 🧭 3. Navigation & App Lifecycle

22. implement stack navigation

23. implement tab navigation

24. implement drawer navigation

25. handle deep linking in React Native

26. implement universal links for iOS

27. handle app lifecycle changes with AppState API

28. use screen lifecycle events for focus handling

29. handle the hardware back button on Android

30. persist navigation state

## 🔧 4. Native Modules & Platform APIs

32. Native modules in React Native

33. Creating custom native modules for Android

34. Creating custom native modules for iOS

35. TurboModules and how they work

36. Accessing native APIs like Camera, Location, and Sensors

37. Headless JS and when to use it

38. How autolinking works in React Native

39. Handling permissions in React Native

## 📱 5. Platform-Specific Development

42. AndroidManifest.xml and how to configure it

43. Info.plist and how to configure it

44. Difference between MainActivity.java and MainApplication.java

45. How the Android lifecycle works in React Native

46. App Delegates in iOS and how they work

47. Configuring app permissions for both platforms

48. Setting up app icons and splash screens

49. Difference between Gradle and Xcode build systems

50. Creating debug vs release builds

51. Handling app signing and provisioning

## ⚡ 6. Performance & Profiling

52. Common performance issues in React Native

53. Hermes engine and how it improves performance

54. Measuring performance in React Native apps

55. Using Flipper for debugging React Native apps

56. Optimizing FlatList for large datasets

57. Difference between FlatList and ScrollView

58. Implementing virtualization in React Native

59. Optimizing `renderItem` functions

60. Implementing pagination with `onEndReached`

61. Using `removeClippedSubviews` for performance

62. Using Xcode Instruments for iOS performance profiling

63. Using Android Studio Profiler for Android performance profiling

64. Profiling memory leaks in React Native apps

65. Analyzing native crash logs and stack traces

66. Optimizing JavaScript bundle size and startup time

## 🎨 7. Animations & Graphics

67. React Native Reanimated 2/3 and how it works

68. Worklets and UI thread animations in Reanimated

69. Gesture handling with Reanimated

70. React Native Skia and when to use it

71. Custom drawing and animations with Skia

72. Performance considerations for animations

73. Choosing between Reanimated and Skia

## 🔌 8. Hardware & System APIs

74. Implementing Bluetooth functionality in React Native

75. Using Bluetooth Low Energy (BLE) in React Native

76. Background services and tasks in React Native

77. Implementing background sync on Android

78. Implementing background tasks on iOS

79. File system operations in React Native

80. Reading and writing files on Android

81. Reading and writing files on iOS

82. Handling file permissions and security

83. Accessing device sensors and hardware APIs

84. Platform-specific API integrations

## 🐛 9. Testing & Debugging

85. Debugging React Native apps

86. Using Flipper for React Native debugging

87. Debugging with Chrome DevTools

88. Creating custom Flipper plugins

89. Debugging native crashes on Android

90. Debugging native crashes on iOS

91. Using Xcode Instruments for debugging

92. Using Android Studio Profiler for debugging

93. Writing unit tests with Jest

94. Implementing end-to-end testing with Detox

95. Mocking native modules in tests

96. Testing asynchronous behavior in React Native

97. Simulating gestures in tests

98. Monitoring app performance and crashes

## 🚀 10. Build & Release Management

99. Creating Android release builds

100. Creating iOS release builds

101. Handling build numbers and versioning

102. Submitting apps to Google Play Store

103. Submitting apps to Apple App Store

104. Implementing phased rollouts

105. Setting up Fastlane for iOS automation

106. Setting up Fastlane for Android automation

107. Configuring Fastlane lanes and actions

108. Handling store rejections and resubmissions

109. Reducing app size for store submission

110. Implementing analytics in React Native apps

111. Handling app signing and certificates

112. Setting up CI/CD pipelines for React Native

## 🔄 11. Over-The-Air Updates

113. Microsoft CodePush and how it works

114. Integrating CodePush in React Native

115. Limitations of CodePush

116. Implementing rollbacks with CodePush

117. Handling version mismatches with CodePush

118. Securing CodePush deployments

119. Difference between CodePush and Expo EAS OTA

120. Monitoring crashes and errors with CodePush

## 📱 12. Notifications & Messaging

121. Difference between local and push notifications

122. Implementing Firebase Cloud Messaging (FCM) for Android

123. Implementing Apple Push Notification service (APNs) for iOS

124. Handling background and foreground notifications

125. Managing notification permissions and channels

---

## 📖 Complete Answer Guide

- [1) Core Concepts & Architecture](./01-core-concepts-and-architecture.md) - Q1-10

- [2) State Management & Data Persistence](./02-state-management-and-data-persistence.md) - Q11-21

- [3) Navigation & App Lifecycle](./03-navigation-and-app-lifecycle.md) - Q22-30

- [4) Native Modules & Platform APIs](./04-native-modules-and-platform-apis.md) - Q32-39

- [5) Platform-Specific Development](./05-platform-specific-development.md) - Q42-51

- [6) Performance & Profiling](./06-performance-and-profiling.md) - Q52-66

- [7) Animations & Graphics](./07-animations-and-graphics.md) - Q67-73

- [8) Hardware & System APIs](./08-hardware-and-system-apis.md) - Q74-84

- [9) Testing & Debugging](./09-testing-and-debugging.md) - Q85-98

- [10) Build & Release Management](./10-build-and-release-management.md) - Q99-112

- [11) Over-The-Air Updates](./11-over-the-air-updates.md) - Q113-120

- [12) Notifications & Messaging](./12-notifications-and-messaging.md) - Q121-125

## 📝 Cheatsheet

[React Native Interview Cheatsheet](./cheatsheet.md) - Quick reference guide
