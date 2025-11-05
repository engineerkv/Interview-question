# ⚡ 7. CodePush & OTA Updates (Q61–68)

---

## 61) What is **Microsoft CodePush**, and how does it work?

CodePush is a service that allows updating React Native apps over-the-air without going through app stores.

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

- **Core Feature**: Update apps without app store approval (over-the-air updates)
- **Real-World Limitation**: Can only update JavaScript and assets (JavaScript only)
- **Common Benefit**: Automatic rollback on failed updates (rollback support)
- **Advanced Feature**: Different environments for testing and production (staging/production)
- **Interview Tip**: Explain that built-in analytics and crash reporting

---

## 62) How do you integrate CodePush into a React Native project?

Install the CodePush SDK, configure it in the app, and set up deployment keys for different environments.

```jsx
import codePush from 'react-native-code-push';

const codePushOptions = {
  checkFrequency: codePush.CheckFrequency.ON_APP_START,
  installMode: codePush.InstallMode.ON_NEXT_RESTART
};

export default codePush(codePushOptions)(App);
```

- **Core Steps**: Install CodePush SDK and native dependencies (SDK installation)
- **Real-World Configuration**: Configure update behavior and frequency (configuration)
- **Common Setup**: Set up different keys for staging and production (deployment keys)
- **Advanced Feature**: Wrap app with CodePush HOC (app wrapping)
- **Interview Tip**: Explain that choose appropriate update strategy

---

## 63) What are the **limitations** of CodePush under App Store policies?

CodePush cannot update native code, change app permissions, or modify core app functionality.

```jsx
// ❌ Cannot do with CodePush
// - Update native modules
// - Change app permissions
// - Modify Info.plist or AndroidManifest.xml
// - Change app icon or splash screen
// - Update native dependencies
```

- **Core Limitation**: Cannot update native code or modules (native code)
- **Real-World Restriction**: Cannot change app permissions (permissions)
- **Common Restriction**: Cannot modify core app functionality (core functionality)
- **Important Rule**: Must comply with app store policies (app store compliance)
- **Interview Tip**: Explain that limited to JavaScript and asset updates (JavaScript only)

---

## 64) How do you handle rollbacks and version mismatches with CodePush?

Use CodePush's rollback features and version checking to handle failed updates and version conflicts.

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

- **Core Feature**: CodePush automatically rolls back failed updates (automatic rollback)
- **Real-World Use**: Check for version compatibility (version checking)
- **Common Practice**: Implement retry logic for failed updates (retry logic)
- **Advanced Feature**: Handle rollbacks gracefully (user experience)
- **Interview Tip**: Explain that monitor update success and failure rates (monitoring)

---

## 65) How do you secure OTA updates and ensure stability in production?

Use proper authentication, code signing, and testing strategies to ensure secure and stable updates.

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

- **Core Security**: Use proper authentication for updates (authentication)
- **Real-World Practice**: Sign updates to ensure integrity (code signing)
- **Common Practice**: Thoroughly test updates before deployment (testing)
- **Advanced Strategy**: Use staged rollouts for safer deployments (staged rollouts)
- **Interview Tip**: Explain that monitor update success and stability (monitoring)

---

## 66) What's the difference between CodePush and Expo's EAS OTA?

CodePush is for bare React Native apps, while EAS OTA is for Expo-managed apps with different deployment strategies.

```jsx
// CodePush (bare React Native)
import codePush from 'react-native-code-push';

// EAS OTA (Expo managed)
import { Updates } from 'expo';
```

- **Core Difference**: CodePush for bare React Native apps, EAS OTA for Expo-managed apps
- **Real-World Impact**: Different deployment strategies (deployment)
- **Common Variation**: Different configuration approaches (configuration)
- **Advanced Feature**: Different feature sets and capabilities (features)
- **Interview Tip**: Explain that choose based on your React Native setup

---

## 67) How do you monitor crash/error rates post-OTA using Sentry or Firebase?

Integrate crash reporting tools to monitor app stability and error rates after OTA updates.

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

- **Core Tools**: Use Sentry or Firebase for crash reporting (crash reporting)
- **Real-World Use**: Monitor error rates after updates (error monitoring)
- **Common Practice**: Track performance metrics (performance tracking)
- **Advanced Feature**: Collect user feedback on updates (user feedback)
- **Interview Tip**: Explain that use crash rates to trigger rollbacks (rollback triggers)

---

## 68) What are best practices for OTA updates in React Native?

Test thoroughly, use staged rollouts, monitor metrics, and have rollback strategies in place.

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

- **Core Practice**: Thoroughly test updates before deployment (testing)
- **Real-World Strategy**: Use staged rollouts for safer deployments (staged rollouts)
- **Common Practice**: Monitor update success and failure rates (monitoring)
- **Advanced Feature**: Have rollback strategies in place (rollback strategy)
- **Interview Tip**: Explain that communicate updates to users (user communication)

---
