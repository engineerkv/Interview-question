# ⚡ 7. CodePush & OTA Updates (Q61–68)

---

## 🧩 Q61. What is Microsoft CodePush and how does it work?

### 🧠 Concept

CodePush is a service that allows updating React Native apps over-the-air without going through app stores. Built-in analytics and crash reporting.

---

### 💡 Example

```jsx
import codePush from 'react-native-code-push';

function App() {
  useEffect(() => {
    codePush.sync({
      installMode: codePush.InstallMode.IMMEDIATE,
      updateDialog: {
        title: 'Update available',
        mandatoryUpdateMessage: 'Update is mandatory'
      }
    });
  }, []);
}
```

---

### 🔍 Deep Insights

* **Rule:** Update apps without app store approval (over-the-air updates).
* **Use Case:** Can only update JavaScript and assets (JavaScript only).
* **Common Mistake:** Automatic rollback on failed updates (rollback support).
* **Pro Tip:** Different environments for testing and production (staging/production).

---

### ⭐ Senior Takeaway

Built-in analytics and crash reporting.

---

## 🧩 Q62. How do you integrate CodePush into a React Native project?

### 🧠 Concept

Install the CodePush SDK, configure it in the app, and set up deployment keys for different environments. Choose appropriate update strategy.

---

### 💡 Example

```jsx
import codePush from 'react-native-code-push';

const codePushOptions = {
  checkFrequency: codePush.CheckFrequency.ON_APP_START,
  installMode: codePush.InstallMode.ON_NEXT_RESTART
};

export default codePush(codePushOptions)(App);
```

---

### 🔍 Deep Insights

* **Rule:** Install CodePush SDK and native dependencies (SDK installation).
* **Use Case:** Configure update behavior and frequency (configuration).
* **Common Mistake:** Set up different keys for staging and production (deployment keys).
* **Pro Tip:** Wrap app with CodePush HOC (app wrapping).

---

### ⭐ Senior Takeaway

Choose appropriate update strategy.

---

## 🧩 Q63. What are the limitations of CodePush under App Store policies?

### 🧠 Concept

CodePush cannot update native code, change app permissions, or modify core app functionality. Limited to JavaScript and asset updates (JavaScript only).

---

### 💡 Example

```jsx
// ❌ Cannot do with CodePush
// - Update native modules
// - Change app permissions
// - Modify Info.plist or AndroidManifest.xml
// - Change app icon or splash screen
// - Update native dependencies
```

---

### 🔍 Deep Insights

* **Rule:** Cannot update native code or modules (native code).
* **Use Case:** Cannot change app permissions (permissions).
* **Common Mistake:** Cannot modify core app functionality (core functionality).
* **Pro Tip:** Must comply with app store policies (app store compliance).

---

### ⭐ Senior Takeaway

Limited to JavaScript and asset updates (JavaScript only).

---

## 🧩 Q64. How do you handle rollbacks and version mismatches with CodePush?

### 🧠 Concept

Use CodePush's rollback features and version checking to handle failed updates and version conflicts. Monitor update success and failure rates (monitoring).

---

### 💡 Example

```jsx
import codePush from 'react-native-code-push';

function App() {
  useEffect(() => {
    codePush.sync({
      updateDialog: {
        optionalUpdateMessage: 'Update available',
        mandatoryUpdateMessage: 'Update is mandatory'
      },
      rollbackRetryOptions: {
        delayInHours: 1,
        maxRetries: 3
      }
    });
  }, []);
}
```

---

### 🔍 Deep Insights

* **Rule:** CodePush automatically rolls back failed updates (automatic rollback).
* **Use Case:** Check for version compatibility (version checking).
* **Common Mistake:** Implement retry logic for failed updates (retry logic).
* **Pro Tip:** Handle rollbacks gracefully (user experience).

---

### ⭐ Senior Takeaway

Monitor update success and failure rates (monitoring).

---

## 🧩 Q65. How do you secure OTA updates and ensure stability?

### 🧠 Concept

Use proper authentication, code signing, and testing strategies to ensure secure and stable updates. Monitor update success and stability (monitoring).

---

### 💡 Example

```jsx
const secureCodePushOptions = {
  checkFrequency: codePush.CheckFrequency.ON_APP_START,
  installMode: codePush.InstallMode.ON_NEXT_RESTART,
  minimumBackgroundDuration: 60,
  updateDialog: {
    mandatoryUpdateMessage: 'Security update required'
  }
};
```

---

### 🔍 Deep Insights

* **Rule:** Use proper authentication for updates (authentication).
* **Use Case:** Sign updates to ensure integrity (code signing).
* **Common Mistake:** Thoroughly test updates before deployment (testing).
* **Pro Tip:** Use staged rollouts for safer deployments (staged rollouts).

---

### ⭐ Senior Takeaway

Monitor update success and stability (monitoring).

---

## 🧩 Q66. What's the difference between CodePush and Expo's EAS OTA?

### 🧠 Concept

CodePush is for bare React Native apps, while EAS OTA is for Expo-managed apps with different deployment strategies. Choose based on your React Native setup.

---

### 💡 Example

```jsx
// CodePush (bare React Native)
import codePush from 'react-native-code-push';

// EAS OTA (Expo managed)
import { Updates } from 'expo';
```

---

### 🔍 Deep Insights

* **Rule:** CodePush for bare React Native apps, EAS OTA for Expo-managed apps.
* **Use Case:** Different deployment strategies (deployment).
* **Common Mistake:** Different configuration approaches (configuration).
* **Pro Tip:** Different feature sets and capabilities (features).

---

### ⭐ Senior Takeaway

Choose based on your React Native setup.

---

## 🧩 Q67. How do you monitor crash/error rates post-OTA?

### 🧠 Concept

Integrate crash reporting tools to monitor app stability and error rates after OTA updates. Use crash rates to trigger rollbacks (rollback triggers).

---

### 💡 Example

```jsx
import Sentry from '@sentry/react-native';
import codePush from 'react-native-code-push';

Sentry.init({
  dsn: 'your-sentry-dsn',
  integrations: [
    new Sentry.ReactNativeTracing()
  ]
});

codePush.sync({
  updateDialog: {
    title: 'Update available'
  }
});
```

---

### 🔍 Deep Insights

* **Rule:** Use Sentry or Firebase for crash reporting (crash reporting).
* **Use Case:** Monitor error rates after updates (error monitoring).
* **Common Mistake:** Track performance metrics (performance tracking).
* **Pro Tip:** Collect user feedback on updates (user feedback).

---

### ⭐ Senior Takeaway

Use crash rates to trigger rollbacks (rollback triggers).

---

## 🧩 Q68. What are best practices for OTA updates in React Native?

### 🧠 Concept

Test thoroughly, use staged rollouts, monitor metrics, and have rollback strategies in place. Communicate updates to users (user communication).

---

### 💡 Example

```jsx
const codePushOptions = {
  checkFrequency: codePush.CheckFrequency.ON_APP_START,
  installMode: codePush.InstallMode.ON_NEXT_RESTART,
  minimumBackgroundDuration: 60,
  updateDialog: {
    title: 'Update available',
    optionalUpdateMessage: 'A new update is available',
    mandatoryUpdateMessage: 'Update is required'
  }
};
```

---

### 🔍 Deep Insights

* **Rule:** Thoroughly test updates before deployment (testing).
* **Use Case:** Use staged rollouts for safer deployments (staged rollouts).
* **Common Mistake:** Monitor update success and failure rates (monitoring).
* **Pro Tip:** Have rollback strategies in place (rollback strategy).

---

### ⭐ Senior Takeaway

Communicate updates to users (user communication).

---
