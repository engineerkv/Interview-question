# ⚛️ React Native Interview Master List (2025 Edition)

A complete collection of React Native interview questions — from fundamentals to native module creation, architecture, performance, and real-world scenarios.

---

## 🟢 1. React Native Fundamentals (Basics  Advanced)

1. What is React Native, and how is it different from React.js?  
2. What are the advantages of using React Native over native development?  
3. What are core components in React Native? (View, Text, Image, ScrollView, etc.)  
4. What is JSX, and how does React Native use it?  
5. What is Flexbox, and how does it control layouts in React Native?  
6. What are props and state, and how are they used?  
7. What is `StyleSheet.create()` and why is it used?  
8. How does React Native render UI internally (JS  Fabric  Native)?  
9. What is the React Native Bridge, and how does it work?  
10. What is JSI (JavaScript Interface), and how is it different from the Bridge?  
11. What is Hermes, and why is it the recommended JavaScript engine?  
12. What are the improvements in Hermes 2.0?  
13. What are TurboModules, and how do they improve performance?  
14. What is the Fabric architecture, and how does it differ from the legacy bridge?  
15. What is the Yoga layout engine, and how does it calculate flex layouts?  
16. What is the React Compiler, and how does it optimize components?  
17. What is the Metro bundler, and how does it bundle JS code?  
18. What are inline requires, and how do they reduce startup time?  
19. What’s the difference between Hot Reload, Fast Refresh, and Live Reload?  
20. What are Managed (Expo) vs Bare workflows?  
21. What’s new in React Native 0.80+ (Fabric default, Hermes 2.0, Compiler support)?  
22. How does React Native handle cross-platform module resolution?  
23. What’s the difference between View, ScrollView, and FlatList?  
24. When should you use SectionList instead of FlatList?  
25. What’s the difference between TouchableOpacity, Pressable, and GestureHandler?  
26. What is SafeAreaView, and why is it used?  
27. How do you handle StatusBar styling across devices?  
28. How do you manage JS, UI, and Shadow threads?  
29. How does one-way data flow work in React Native?  
30. How does React Native handle styling consistency across platforms?

---

## 🧩 2. Android & iOS Platform Essentials

31. What is the Android Activity lifecycle, and how does React Native tie into it?  
32. How does the iOS App lifecycle (AppDelegate, SceneDelegate) connect to RN?  
33. What is `MainActivity.java`, and what’s its role in an RN app?  
34. What is `MainApplication.java`, and what does it initialize?  
35. What is `AndroidManifest.xml`, and what does it control?  
36. How do you define permissions in Android (`camera`, `location`, `internet`)?  
37. What is an `<intent-filter>`, and how is it used for deep linking?  
38. How do you define your app’s launch activity in the manifest?  
39. How do you manage environment variables or flavors in Gradle?  
40. What is the difference between `build.gradle` (project) and (app)?  
41. What are `buildTypes` and `productFlavors` in Gradle?  
42. How do you configure ProGuard and R8 for minification?  
43. What is Gradle dependency resolution, and how does it affect builds?  
44. What are `.aar` files, and when are they used?  
45. What is `Info.plist`, and what configurations are defined there?  
46. How do you define permissions (camera, location, Face ID) in Info.plist?  
47. What is `AppDelegate.m` or `AppDelegate.swift`, and how does RN use it?  
48. What is the role of `SceneDelegate` in iOS apps?  
49. What are provisioning profiles and signing certificates?  
50. How do you manage Debug, Release, and Staging builds in Xcode?  
51. What is a `.xcworkspace` file, and why does CocoaPods create it?  
52. What are CocoaPods, and why are they essential for React Native?  
53. What’s the difference between a `Podfile` and a `.podspec`?  
54. How do you install or update pods using the CLI?  
55. What is autolinking, and how does it work with native dependencies?  
56. What are build phases and build settings in Xcode?  
57. How do you view and analyze logs in Android Studio (Logcat) and Xcode Console?  
58. What are `.ipa` and `.aab` files, and how are they generated?  
59. What is App Thinning in iOS, and how does it reduce size?  
60. How do you handle app signing for production builds in both platforms?

---

## 🧱 3. Native Modules & SDK Integration (Extended)

61. What are Native Modules, and why are they needed?  
62. What’s the difference between Native Modules and TurboModules?  
63. How does the React Native Bridge communicate with native code?  
64. What role does JSI play in native module communication?  
65. What is Codegen, and how does it generate bindings automatically?  
66. How do you create a Native Module on Android (Java/Kotlin)?  
67. How do you register a Native Module in `MainApplication.java`?  
68. How do you expose constants from a Native Module to JS?  
69. How do you return Promises or callbacks from Android native code?  
70. How do you send events from Android native  JS using `RCTDeviceEventEmitter`?  
71. How do you handle async operations in Native Modules?  
72. What is JNI (Java Native Interface), and how is it used in RN?  
73. How do you use TurboModules to replace the legacy bridge?  
74. How do you integrate SDKs like Firebase or Stripe into a Native Module?  
75. How do you create a Native Module in iOS (Objective-C/Swift)?  
76. How do you expose methods using `RCT_EXPORT_METHOD` or `@objc` in Swift?  
77. How do you emit events using `RCTEventEmitter` in iOS?  
78. How do you return Promises from iOS native code?  
79. How do you share data between JS and native threads safely?  
80. What is autolinking, and how does it simplify native linking?  
81. How do TurboModules improve JS ↔ Native communication speed?  
82. How do you create a cross-platform JSI module with C++?  
83. What are the advantages of JSI over the legacy bridge?  
84. What is `react-native-codegen`, and how do you configure it?  
85. How do you debug JSI-based native modules?  
86. How do you mock native modules in Jest tests?  
87. How do you test native logic with JUnit (Android) or XCTest (iOS)?  
88. What are common causes of native crashes and how do you fix them?  
89. How do you publish a native module to npm or GitHub?  
90. How do you ensure backward compatibility with older RN versions?

---

## ⚙️ 4. Performance Optimization & Memory Management

91. What are the most common RN performance bottlenecks?  
92. How do you profile JS and UI threads?  
93. How does Hermes improve startup time and memory usage?  
94. How do you optimize FlatList and SectionList performance?  
95. How does `getItemLayout()` improve virtualization?  
96. How do you prevent unnecessary re-renders in RN?  
97. How do you use Flipper for performance debugging?  
98. How do you detect and fix JS or native memory leaks?  
99. How do you reduce bundle size (inline requires, code splitting)?  
100. How do you use Android Profiler and Xcode Instruments?  
101. How do you optimize image loading and caching?  
102. How do you preload Hermes bytecode?  
103. How do TurboModules minimize JS-native overhead?  
104. How do you handle background tasks efficiently?  
105. How do you keep 60 FPS on low-end Android devices?  
106. How do you offload heavy JS work to native threads?  
107. How do you optimize animations (Reanimated 3, Skia)?  
108. How do you use React Query or SWR for API caching?  
109. How do you reduce cold start time in production builds?  
110. How do you detect and fix dropped frames or jank?

---

## 🔒 5. Security, Stability & Error Monitoring

111. How do you handle JS and native crashes gracefully?  
112. How do you use Error Boundaries for crash recovery?  
113. How do you integrate Sentry or Crashlytics?  
114. What are ANRs (Application Not Responding), and how do you prevent them?  
115. How do you secure data using Keychain (iOS) or Keystore (Android)?  
116. What is SSL pinning, and how do you implement it?  
117. How do you protect environment variables and API keys?  
118. How do you detect jailbroken or rooted devices?  
119. How do you encrypt data at rest and in transit?  
120. How do you secure OTA (CodePush) updates?  
121. How do you prevent code tampering or reverse engineering?  
122. How do you handle GDPR and CCPA compliance?  
123. How do you handle permission revocations gracefully?  
124. How do you implement secure logout and token invalidation?  
125. How do you rotate and refresh encryption keys?

---

## 🧪 6. Testing, Automation & CI/CD

126. What are the main testing types in React Native (unit, integration, E2E)?  
127. How do you test components with Jest and RN Testing Library?  
128. How do you mock native modules in Jest?  
129. How do you perform E2E testing with Detox?  
130. What is snapshot testing, and when should it be used?  
131. How do you measure test coverage in React Native?  
132. How do you automate builds using GitHub Actions, CircleCI, or Bitrise?  
133. What is EAS Build, and how does it simplify Expo workflows?  
134. How do you manage multiple build variants (debug, release, staging)?  
135. How do you automate signing and key handling?  
136. How do you handle environment configs securely in CI?  
137. What are phased rollouts and blue-green deployments?  
138. How do you manage OTA updates via CodePush or AppCenter?  
139. How do you automate performance benchmarks?  
140. How do you integrate static analysis tools (ESLint, TypeScript) in pipelines?

---

## 🛠️ 7. Real-World Scenarios & Architecture

141. How do you integrate push notifications (FCM, APNs)?  
142. How do you implement biometric authentication (Face ID, Touch ID)?  
143. How do you build an offline-first app using Realm or MMKV?  
144. How do you implement feature flags (LaunchDarkly or custom)?  
145. How do you implement dark mode with persistent state?  
146. How do you integrate Maps, Camera, or Payment SDKs?  
147. How do you design skeleton loaders for perceived performance?  
148. How do you use React Query to cache API calls?  
149. How do you modularize a large React Native project?  
150. How do you migrate to the new RN architecture (Fabric + TurboModules)?  
151. How do you handle background sync using Headless JS?  
152. How do you monitor app performance using Sentry and Flipper?  
153. How do you manage multiple environments using `.env` files?  
154. How do you set up CI/CD pipelines for automated testing & deployment?  
155. How do you structure scalable folder architecture?  
156. How do you optimize cold start and app launch time?  
157. How do you handle large teams and feature-based modularization?  
158. How do you plan an RN migration strategy across versions?  
159. How do you measure mobile performance metrics (TTI, TTFB, FPS)?  
160. How do you distribute builds to testers using Firebase App Distribution or TestFlight?

---

## ✅ Final Summary

| Category | Focus | Questions |
|-----------|--------|-----------|
| Fundamentals | React Native core, Fabric, Hermes | 1–30 |
| Android & iOS | Lifecycle, Manifest, Info.plist, Pods | 31–60 |
| Native Modules | TurboModules, JSI, Codegen, SDKs | 61–90 |
| Performance | Optimization, Profiling, Threads | 91–110 |
| Security | Encryption, Error Handling | 111–125 |
| Testing & CI/CD | Jest, Detox, Pipelines | 126–140 |
| Real-World | Architecture, Scaling, Fabric Migration | 141–160 |

---

🧠 **Pro Tip for Interview Prep**

- Master **Fabric, TurboModules, and JSI** — they’re the future of React Native.  
- Be ready to explain **Android lifecycle + iOS Info.plist** in context of RN initialization.  
- Focus on **Flipper, Hermes, and Codegen** for advanced debugging and performance.  
- Know at least one **native module implementation (Android + iOS)** end-to-end.

---
