# 🏗 9. Build, Deployment & Stores (Q79–90)

---

## 79) How do you create an Android release build using Gradle and keystore?

Concept:
Configure signing in build.gradle, create a keystore, and build the release APK.

Example:
```gradle
// android/app/build.gradle
android {
    signingConfigs {
        release {
            if (project.hasProperty('MYAPP_RELEASE_STORE_FILE')) {
                storeFile file(MYAPP_RELEASE_STORE_FILE)
```

Deep Insight:
- **Keystore Creation**: Use keytool to create release keystore
- **Signing Configuration**: Configure signing in build.gradle
- **Proguard**: Enable code obfuscation for release builds
- **Security**: Keep keystore and passwords secure
- **Build Process**: Use gradlew assembleRelease to build

---

## 80) How do you create an iOS release build using Xcode and provisioning profiles?

Concept:
Configure code signing in Xcode, create provisioning profiles, and archive the app.

Example:
```bash
# iOS build process
# 1. Open project in Xcode
# 2. Configure signing & capabilities
# 3. Select provisioning profile
# 4. Archive the app
# 5. Distribute to App Store
```

Deep Insight:
- **Code Signing**: Configure code signing in Xcode
- **Provisioning Profiles**: Create and manage provisioning profiles
- **Archive Process**: Archive app for distribution
- **App Store Connect**: Upload to App Store Connect
- **Certificates**: Manage development and distribution certificates

---

## 81) How do you manage build numbers and versioning across both platforms?

Concept:
Use consistent versioning strategies and automate version management across platforms.

Example:
```jsx
// package.json
{
  "version": "1.2.3"
}

// android/app/build.gradle
```

Deep Insight:
- **Semantic Versioning**: Use semantic versioning (major.minor.patch)
- **Version Code**: Android version code (integer)
- **Bundle Version**: iOS bundle version (string)
- **Automation**: Automate version management
- **Consistency**: Keep versions consistent across platforms

---

## 82) What are the guidelines for Play Store submission (Android)?

Concept:
Follow Google Play Store guidelines for app quality, content, and technical requirements.

Example:
```xml
<!-- AndroidManifest.xml requirements -->
<manifest xmlns:android="http://schemas.android.com/apk/res/android">
    <uses-permission android:name="android.permission.INTERNET" />
    
    <application
        android:name=".MainApplication"
```

Deep Insight:
- **App Quality**: Meet quality guidelines and standards
- **Content Policy**: Follow content and policy guidelines
- **Technical Requirements**: Meet technical requirements
- **Privacy Policy**: Include privacy policy
- **Target API**: Target recent Android API levels

---

## 83) What are the guidelines for App Store submission (iOS)?

Concept:
Follow Apple App Store guidelines for app quality, content, and technical requirements.

Example:
```xml
<!-- Info.plist requirements -->
<dict>
    <key>CFBundleDisplayName</key>
    <string>My App</string>
    <key>CFBundleIdentifier</key>
    <string>com.myapp</string>
```

Deep Insight:
- **App Review**: Follow App Store review guidelines
- **Human Interface Guidelines**: Follow iOS design guidelines
- **Technical Requirements**: Meet technical requirements
- **Privacy Policy**: Include privacy policy
- **App Store Connect**: Use App Store Connect for submission

---

## 84) How do you handle **phased rollouts** or staged updates?

Concept:
Use store-specific rollout features to gradually release updates to users.

Example:
```jsx
// Phased rollout configuration
const rolloutConfig = {
  android: {
    // Google Play Console phased rollout
    rolloutPercentage: 20, // Start with 20% of users
    monitoringPeriod: 7, // Monitor for 7 days
```

Deep Insight:
- **Gradual Release**: Release updates to subset of users first
- **Risk Mitigation**: Reduce risk of widespread issues
- **Monitoring**: Monitor metrics and user feedback
- **Auto-Promotion**: Automatically promote successful rollouts
- **Rollback**: Ability to pause or rollback if issues arise

---

## 85) How do you automate builds using **Fastlane**, **EAS**, or **Bitrise**?

Concept:
Use CI/CD tools to automate the build, test, and deployment process.

Example:
```ruby
# Fastfile
platform :android do
  desc "Build and upload to Play Store"
  lane :deploy do
    gradle(
      task: "bundle",
```

Deep Insight:
- **Fastlane**: Ruby-based automation tool
- **EAS**: Expo's build and deployment service
- **Bitrise**: Cloud-based CI/CD platform
- **Automation**: Automate repetitive build tasks
- **CI/CD Integration**: Integrate with CI/CD pipelines

---

## 86) What are common causes of store rejections and how to fix them?

Concept:
Common causes include policy violations, technical issues, and quality problems that need to be addressed.

Example:
```jsx
// Common rejection causes and fixes

// 1. Privacy Policy missing
// Fix: Add privacy policy link in app

// 2. App crashes on launch
```

Deep Insight:
- **Policy Violations**: Follow store policies and guidelines
- **Technical Issues**: Fix crashes and performance issues
- **Content Issues**: Ensure appropriate content
- **Metadata Issues**: Accurate app descriptions
- **Quality Issues**: Meet quality standards

---

## 87) How do you reduce app size (Hermes, Proguard, asset optimization)?

Concept:
Use Hermes, code obfuscation, asset optimization, and other techniques to reduce app size.

Example:
```gradle
// android/app/build.gradle
android {
    buildTypes {
        release {
            minifyEnabled true
            shrinkResources true
```

Deep Insight:
- **Hermes**: Use Hermes JavaScript engine
- **Proguard**: Enable code obfuscation and shrinking
- **Asset Optimization**: Optimize images and assets
- **Bundle Analysis**: Analyze bundle size
- **Tree Shaking**: Remove unused code

---

## 88) How do you handle app analytics and tracking (Firebase, Segment)?

Concept:
Integrate analytics tools to track user behavior and app performance.

Example:
```jsx
// Firebase Analytics
import analytics from '@react-native-firebase/analytics';

function App() {
  useEffect(() => {
    // Track app open
```

Deep Insight:
- **Firebase Analytics**: Google's analytics platform
- **Segment**: Customer data platform
- **Event Tracking**: Track user interactions
- **User Behavior**: Understand user behavior
- **Performance Monitoring**: Monitor app performance

---

## 89) What are best practices for signing, certificates, and release management?

Concept:
Use proper certificate management, secure signing practices, and automated release processes.

Example:
```bash
# Android keystore management
keytool -genkey -v -keystore my-release-key.keystore \
        -alias my-key-alias -keyalg RSA -keysize 2048 \
        -validity 10000

# iOS certificate management
```

Deep Insight:
- **Keystore Security**: Keep Android keystore secure
- **Certificate Management**: Manage iOS certificates properly
- **Automated Signing**: Use automated signing when possible
- **Backup**: Backup signing keys and certificates
- **Rotation**: Rotate certificates regularly

---

## 90) How do you set up CI/CD pipelines for React Native apps?

Concept:
Configure automated pipelines for building, testing, and deploying React Native apps.

Example:
```yaml
# .github/workflows/deploy.yml
name: Deploy
on:
  push:
    branches: [main]

```

Deep Insight:
- **GitHub Actions**: Use GitHub Actions for CI/CD
- **Automated Testing**: Run tests automatically
- **Automated Building**: Build apps automatically
- **Automated Deployment**: Deploy to stores automatically
- **Quality Gates**: Implement quality gates in pipeline

---
