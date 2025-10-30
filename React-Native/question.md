# ⚛️ React Native Interview Questions

95 carefully curated questions covering React Native fundamentals to advanced platform internals.

## 📋 Quick Navigation

| Section | Topic | Questions | Difficulty |
|---------|-------|-----------|------------|
| [1️⃣](#1-react-native-fundamentals) | React Native Fundamentals | Q1–10 | ⭐⭐ |
| [2️⃣](#2-native-modules--platform-integrations) | Native Modules & Platform Integrations | Q11–20 | ⭐⭐⭐ |
| [3️⃣](#3-android--ios-platform-internals) | Android & iOS Platform Internals | Q21–30 | ⭐⭐⭐ |
| [4️⃣](#4-navigation--lifecycle) | Navigation & Lifecycle | Q31–40 | ⭐⭐⭐ |
| [5️⃣](#5-performance-optimization--measurement) | Performance Optimization & Measurement | Q41–50 | ⭐⭐⭐⭐ |
| [6️⃣](#6-state-management--data-handling) | State Management & Data Handling | Q51–60 | ⭐⭐⭐ |
| [7️⃣](#7-codepush--ota-updates) | CodePush & OTA Updates | Q61–68 | ⭐⭐⭐⭐ |
| [8️⃣](#8-debugging--testing) | Debugging & Testing | Q69–78 | ⭐⭐⭐⭐ |
| [9️⃣](#9-build-deployment--stores) | Build, Deployment & Stores | Q79–90 | ⭐⭐⭐⭐⭐ |
| [🔟](#10-push-notifications--messaging) | Push Notifications & Messaging | Q91–95 | ⭐⭐⭐ |

## ⚛️ 1. React Native Fundamentals

1. What is React Native, and how is it different from React.js?
2. How does React Native render UI on mobile devices? Explain the bridge concept.
3. What is the JavaScript Interface (JSI) and how does it work?
4. What are Fabric and TurboModules in React Native?
5. How does JavaScript communicate with native code?
6. What are the differences between iOS and Android rendering in React Native?
7. What is Metro bundler and how does it work?
8. What is the difference between Live Reload, Hot Reload, and Fast Refresh?
9. What are the built-in components in React Native?
10. How does Flexbox work in React Native compared to CSS?

## 🔧 2. Native Modules & Platform Integrations

11. What are native modules in React Native?
12. How do you create custom native modules for Android?
13. How do you create custom native modules for iOS?
14. What is the difference between JSI and the old bridge?
15. What are TurboModules and how do they work?
16. How do you access native APIs like Camera, Location, and Sensors?
17. What is Headless JS and when do you use it?
18. How does autolinking work in React Native?
19. What is the difference between bridged and JSI-based modules?
20. How do you handle permissions in React Native?

## 📱 3. Android & iOS Platform Internals

21. What is AndroidManifest.xml and how do you configure it?
22. What is Info.plist and how do you configure it?
23. What is the difference between MainActivity.java and MainApplication.java?
24. How does the Android lifecycle work in React Native?
25. What are App Delegates in iOS and how do they work?
26. How do you configure app permissions for both platforms?
27. How do you set up app icons and splash screens?
28. What is the difference between Gradle and Xcode build systems?
29. How do you create debug vs release builds?
30. How do you handle app signing and provisioning?

## 🧭 4. Navigation & Lifecycle

31. What are the different navigation solutions available for React Native?
32. How do you implement stack navigation?
33. How do you implement tab navigation?
34. How do you implement drawer navigation?
35. How do you handle deep linking in React Native?
36. How do you implement universal links for iOS?
37. How do you handle app lifecycle changes with AppState API?
38. How do you use `useFocusEffect` for screen focus handling?
39. How do you handle the hardware back button on Android?
40. How do you persist navigation state?

## ⚡ 5. Performance Optimization & Measurement

41. What are the common performance issues in React Native?
42. What is Hermes engine and how does it improve performance?
43. How do you measure performance in React Native apps?
44. How do you use Flipper for debugging React Native apps?
45. How do you optimize FlatList for large datasets?
46. What is the difference between FlatList and ScrollView?
47. How do you implement virtualization in React Native?
48. How do you optimize `renderItem` functions?
49. How do you implement pagination with `onEndReached`?
50. How do you use `removeClippedSubviews` for performance?

## 🗃️ 6. State Management & Data Handling

51. What state management tools are available for React Native?
52. How do you implement Redux in React Native?
53. How do you use Recoil for state management?
54. How do you implement Zustand for state management?
55. How do you use Context API for state management?
56. How do you persist data locally with AsyncStorage?
57. What is MMKV and how does it compare to AsyncStorage?
58. How do you implement offline-first apps?
59. How do you handle background data synchronization?
60. How do you implement data batching for performance?

## 🔄 7. CodePush & OTA Updates

61. What is Microsoft CodePush and how does it work?
62. How do you integrate CodePush in React Native?
63. What are the limitations of CodePush?
64. How do you implement rollbacks with CodePush?
65. How do you handle version mismatches with CodePush?
66. How do you secure CodePush deployments?
67. What is the difference between CodePush and Expo EAS OTA?
68. How do you monitor crashes and errors with CodePush?

## 🐛 8. Debugging & Testing

69. How do you debug React Native apps?
70. How do you use Flipper for React Native debugging?
71. How do you debug with Chrome DevTools?
72. How do you create custom Flipper plugins?
73. How do you write unit tests with Jest?
74. How do you implement end-to-end testing with Detox?
75. How do you mock native modules in tests?
76. How do you test asynchronous behavior in React Native?
77. How do you simulate gestures in tests?
78. How do you monitor app performance and crashes?

## 🚀 9. Build, Deployment & Stores

79. How do you create Android release builds?
80. How do you create iOS release builds?
81. How do you handle build numbers and versioning?
82. How do you submit apps to Google Play Store?
83. How do you submit apps to Apple App Store?
84. How do you implement phased rollouts?
85. How do you automate builds with Fastlane?
86. How do you handle store rejections and resubmissions?
87. How do you reduce app size for store submission?
88. How do you implement analytics in React Native apps?
89. How do you handle app signing and certificates?
90. How do you set up CI/CD pipelines for React Native?

## 📱 10. Push Notifications & Messaging

91. What is the difference between local and push notifications?
92. How do you implement Firebase Cloud Messaging (FCM) for Android?
93. How do you implement Apple Push Notification service (APNs) for iOS?
94. How do you handle background and foreground notifications?
95. How do you manage notification permissions and channels?

---

## 📖 Complete Answer Guide

- [1) React Native Fundamentals](1%20React%20Native%20Fundamentals.md) - Q1-10
- [2) Native Modules & Platform Integrations](2%20Native%20Modules%20%26%20Platform%20Integrations.md) - Q11-20
- [3) Android & iOS Platform Internals](3%20Android%20%26%20iOS%20Platform%20Internals.md) - Q21-30
- [4) Navigation & Lifecycle](4%20Navigation%20%26%20Lifecycle.md) - Q31-40
- [5) Performance Optimization & Measurement](5%20Performance%20Optimization%20%26%20Measurement.md) - Q41-50
- [6) State Management & Data Handling](6%20State%20Management%20%26%20Data%20Handling.md) - Q51-60
- [7) CodePush & OTA Updates](7%20CodePush%20%26%20OTA%20Updates.md) - Q61-68
- [8) Debugging & Testing](8%20Debugging%20%26%20Testing.md) - Q69-78
- [9) Build, Deployment & Stores](9%20Build%20Deployment%20%26%20Stores.md) - Q79-90
- [10) Push Notifications & Messaging](10%20Push%20Notifications%20%26%20Messaging.md) - Q91-95

## 📝 Cheatsheet

[React Native Interview Cheatsheet](React%20Native%20Interview%20Cheatsheet.md) - Quick reference guide