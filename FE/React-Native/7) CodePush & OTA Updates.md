<div align="center">

**[← Previous: State Management & Data Handling](6%29%20State%20Management%20%26%20Data%20Handling.md)** | **[Next: Debugging & Testing →](8%29%20Debugging%20%26%20Testing.md)**

</div>

# 7. CodePush & OTA Updates (Q61–68)

---

## Q61. 📲 Microsoft CodePush and how it works

CodePush is a service that allows updating React Native apps over-the-air without going through app stores - built-in analytics and crash reporting. Update apps without app store approval (over-the-air updates).

- **Trade-offs**: The catch is automatic rollback on failed updates (rollback support) - different environments for testing and production (staging/production). Built-in analytics and crash reporting, but watch out - can only update JavaScript and assets (JavaScript only).

Example:

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

## Q62. 📱 Integrating CodePush in React Native

Install the CodePush SDK, configure it in the app, and set up deployment keys for different environments - choose appropriate update strategy. Install CodePush SDK and native dependencies (SDK installation).

- **Trade-offs**: The catch is set up different keys for staging and production (deployment keys) - wrap app with CodePush HOC (app wrapping). Choose appropriate update strategy, but watch out - configure update behavior and frequency (configuration).

Example:

```jsx
import codePush from 'react-native-code-push';

const codePushOptions = {
  checkFrequency: codePush.CheckFrequency.ON_APP_START,
  installMode: codePush.InstallMode.ON_NEXT_RESTART
};

export default codePush(codePushOptions)(App);

```

---

## Q63. 📲 Limitations of CodePush

CodePush cannot update native code, change app permissions, or modify core app functionality - limited to JavaScript and asset updates (JavaScript only). Cannot update native code or modules (native code).

- **Trade-offs**: The catch is cannot modify core app functionality (core functionality) - must comply with app store policies (app store compliance). Limited to JavaScript and asset updates (JavaScript only), but watch out - cannot change app permissions (permissions).

Example:

```jsx
// ❌ Cannot do with CodePush
// - Update native modules
// - Change app permissions
// - Modify Info.plist or AndroidManifest.xml
// - Change app icon or splash screen
// - Update native dependencies

```

---

## Q64. 📲 Implementing rollbacks with CodePush

Use CodePush's rollback features and version checking to handle failed updates and version conflicts - monitor update success and failure rates (monitoring). CodePush automatically rolls back failed updates (automatic rollback).

- **Trade-offs**: The catch is implement retry logic for failed updates (retry logic) - handle rollbacks gracefully (user experience). Monitor update success and failure rates (monitoring), but watch out - check for version compatibility (version checking).

Example:

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

## Q65. 📲 Handling version mismatches with CodePush

Use proper authentication, code signing, and testing strategies to ensure secure and stable updates - monitor update success and stability (monitoring). Use proper authentication for updates (authentication).

- **Trade-offs**: The catch is thoroughly test updates before deployment (testing) - use staged rollouts for safer deployments (staged rollouts). Monitor update success and stability (monitoring), but watch out - sign updates to ensure integrity (code signing).

Example:

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

## Q66. 🚀 Securing CodePush deployments

CodePush is for bare React Native apps, while EAS OTA is for Expo-managed apps with different deployment strategies - choose based on your React Native setup. CodePush for bare React Native apps, EAS OTA for Expo-managed apps.

- **Trade-offs**: The catch is different configuration approaches (configuration) - different feature sets and capabilities (features). Choose based on your React Native setup, but watch out - different deployment strategies (deployment).

Example:

```jsx
// CodePush (bare React Native)
import codePush from 'react-native-code-push';

// EAS OTA (Expo managed)
import { Updates } from 'expo';

```

---

## Q67. 📲 Difference between CodePush and Expo EAS OTA

Integrate crash reporting tools to monitor app stability and error rates after OTA updates - use crash rates to trigger rollbacks (rollback triggers). Use Sentry or Firebase for crash reporting (crash reporting).

- **Trade-offs**: The catch is track performance metrics (performance tracking) - collect user feedback on updates (user feedback). Use crash rates to trigger rollbacks (rollback triggers), but watch out - monitor error rates after updates (error monitoring).

Example:

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

## Q68. 📲 Monitoring crashes and errors with CodePush

Test thoroughly, use staged rollouts, monitor metrics, and have rollback strategies in place - communicate updates to users (user communication). Thoroughly test updates before deployment (testing).

- **Trade-offs**: The catch is monitor update success and failure rates (monitoring) - have rollback strategies in place (rollback strategy). Communicate updates to users (user communication), but watch out - use staged rollouts for safer deployments (staged rollouts).

Example:

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

