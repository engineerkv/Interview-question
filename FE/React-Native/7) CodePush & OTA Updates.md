# ⚡ 7. CodePush & OTA Updates (Q61–68)

---

## 61) What is **Microsoft CodePush**, and how does it work?

Concept:
CodePush is a service that allows updating React Native apps over-the-air without going through app stores.

Example:
```jsx
import codePush from 'react-native-code-push';

function App() {
  useEffect(() => {
    // Check for updates on app start
    codePush.sync({
```

Deep Insight:
- **Over-the-Air Updates**: Update apps without app store approval
- **JavaScript Only**: Can only update JavaScript and assets
- **Rollback Support**: Automatic rollback on failed updates
- **Staging/Production**: Different environments for testing and production
- **Analytics**: Built-in analytics and crash reporting

---

## 62) How do you integrate CodePush into a React Native project?

Concept:
Install the CodePush SDK, configure it in the app, and set up deployment keys for different environments.

Example:
```jsx
// Installation
// npm install react-native-code-push

// Configuration
import codePush from 'react-native-code-push';

```

Deep Insight:
- **SDK Installation**: Install CodePush SDK and native dependencies
- **Configuration**: Configure update behavior and frequency
- **Deployment Keys**: Set up different keys for staging and production
- **App Wrapping**: Wrap app with CodePush HOC
- **Update Strategy**: Choose appropriate update strategy

---

## 63) What are the **limitations** of CodePush under App Store policies?

Concept:
CodePush cannot update native code, change app permissions, or modify core app functionality.

Example:
```jsx
// ❌ Cannot do with CodePush
// - Update native modules
// - Change app permissions
// - Modify Info.plist or AndroidManifest.xml
// - Change app icon or splash screen
// - Update native dependencies
```

Deep Insight:
- **Native Code**: Cannot update native code or modules
- **Permissions**: Cannot change app permissions
- **Core Functionality**: Cannot modify core app functionality
- **App Store Compliance**: Must comply with app store policies
- **JavaScript Only**: Limited to JavaScript and asset updates

---

## 64) How do you handle rollbacks and version mismatches with CodePush?

Concept:
Use CodePush's rollback features and version checking to handle failed updates and version conflicts.

Example:
```jsx
import codePush from 'react-native-code-push';

function App() {
  useEffect(() => {
    codePush.sync({
      updateDialog: {
```

Deep Insight:
- **Automatic Rollback**: CodePush automatically rolls back failed updates
- **Version Checking**: Check for version compatibility
- **Retry Logic**: Implement retry logic for failed updates
- **User Experience**: Handle rollbacks gracefully
- **Monitoring**: Monitor update success and failure rates

---

## 65) How do you secure OTA updates and ensure stability in production?

Concept:
Use proper authentication, code signing, and testing strategies to ensure secure and stable updates.

Example:
```jsx
// Secure CodePush configuration
const secureCodePushOptions = {
  checkFrequency: codePush.CheckFrequency.ON_APP_START,
  installMode: codePush.InstallMode.ON_NEXT_RESTART,
  minimumBackgroundDuration: 60,
  updateDialog: {
```

Deep Insight:
- **Authentication**: Use proper authentication for updates
- **Code Signing**: Sign updates to ensure integrity
- **Testing**: Thoroughly test updates before deployment
- **Staged Rollouts**: Use staged rollouts for safer deployments
- **Monitoring**: Monitor update success and stability

---

## 66) What's the difference between CodePush and Expo's EAS OTA?

Concept:
CodePush is for bare React Native apps, while EAS OTA is for Expo-managed apps with different deployment strategies.

Example:
```jsx
// CodePush (bare React Native)
import codePush from 'react-native-code-push';

// EAS OTA (Expo managed)
import { Updates } from 'expo';

```

Deep Insight:
- **CodePush**: For bare React Native apps
- **EAS OTA**: For Expo-managed apps
- **Deployment**: Different deployment strategies
- **Configuration**: Different configuration approaches
- **Features**: Different feature sets and capabilities

---

## 67) How do you monitor crash/error rates post-OTA using Sentry or Firebase?

Concept:
Integrate crash reporting tools to monitor app stability and error rates after OTA updates.

Example:
```jsx
import Sentry from '@sentry/react-native';
import codePush from 'react-native-code-push';

// Initialize Sentry
Sentry.init({
  dsn: 'your-sentry-dsn',
```

Deep Insight:
- **Crash Reporting**: Use Sentry or Firebase for crash reporting
- **Error Monitoring**: Monitor error rates after updates
- **Performance Tracking**: Track performance metrics
- **User Feedback**: Collect user feedback on updates
- **Rollback Triggers**: Use crash rates to trigger rollbacks

---

## 68) What are best practices for OTA updates in React Native?

Concept:
Test thoroughly, use staged rollouts, monitor metrics, and have rollback strategies in place.

Example:
```jsx
// Best practices implementation
const codePushOptions = {
  checkFrequency: codePush.CheckFrequency.ON_APP_START,
  installMode: codePush.InstallMode.ON_NEXT_RESTART,
  minimumBackgroundDuration: 60,
  updateDialog: {
```

Deep Insight:
- **Testing**: Thoroughly test updates before deployment
- **Staged Rollouts**: Use staged rollouts for safer deployments
- **Monitoring**: Monitor update success and failure rates
- **Rollback Strategy**: Have rollback strategies in place
- **User Communication**: Communicate updates to users

---
