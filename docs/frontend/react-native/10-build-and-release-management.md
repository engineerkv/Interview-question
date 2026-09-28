---
sidebar_label: "Build & Release Management"
---
# 10. Build & Release Management (Q99–112)

---

## Q99. 🏗️ Creating Android release builds

Configure signing in build.gradle, create a keystore, and build the release APK - use gradlew assembleRelease to build (build process). Use keytool to create release keystore (keystore creation).

- **Trade-offs**: The catch is enable code obfuscation for release builds (Proguard) - keep keystore and passwords secure. Use gradlew assembleRelease to build (build process), but watch out - configure signing in build.gradle (signing configuration).

Example:

```gradle
// android/app/build.gradle
android {
    signingConfigs {
        release {
            if (project.hasProperty('MYAPP_RELEASE_STORE_FILE')) {
                storeFile file(MYAPP_RELEASE_STORE_FILE)
                storePassword MYAPP_RELEASE_STORE_PASSWORD
                keyAlias MYAPP_RELEASE_KEY_ALIAS
                keyPassword MYAPP_RELEASE_KEY_PASSWORD
            }
        }
    }
    buildTypes {
        release {
            signingConfig signingConfigs.release
            minifyEnabled true
            proguardFiles getDefaultProguardFile('proguard-android.txt'), 'proguard-rules.pro'
        }
    }
}

```

---

## Q100. 🏗️ Creating iOS release builds

Configure code signing in Xcode, create provisioning profiles, and archive the app - manage development and distribution certificates (certificates). Configure code signing in Xcode (code signing).

- **Trade-offs**: The catch is archive app for distribution (archive process) - upload to App Store Connect (App Store Connect). Manage development and distribution certificates (certificates), but watch out - create and manage provisioning profiles (provisioning profiles).

Example:

```bash

# iOS build process

# 10. Open project in Xcode

# 10. Configure signing & capabilities

# 10. Select provisioning profile

# 10. Archive the app

# 10. Distribute to App Store

```

---

## Q101. 🏗️ Handling build numbers and versioning

Use consistent versioning strategies and automate version management across platforms - keep versions consistent across platforms (consistency). Use semantic versioning (major.minor.patch) (semantic versioning).

- **Trade-offs**: The catch is iOS bundle version (string) (bundle version) - automate version management (automation). Keep versions consistent across platforms (consistency), but watch out - Android version code (integer) (version code).

Example:

```jsx
// package.json
{
  "version": "1.2.3"
}

// android/app/build.gradle
android {
    defaultConfig {
        versionCode 123
        versionName "1.2.3"
    }
}

```

---

## Q102. 💡 Submitting apps to Google Play Store

Follow Google Play Store guidelines for app quality, content, and technical requirements - target recent Android API levels (target API). Meet quality guidelines and standards (app quality).

- **Trade-offs**: The catch is meet technical requirements (technical requirements) - include privacy policy (privacy policy). Target recent Android API levels (target API), but watch out - follow content and policy guidelines (content policy).

Example:

```xml
<!-- AndroidManifest.xml requirements -->
<manifest xmlns:android="http://schemas.android.com/apk/res/android">
    <uses-permission android:name="android.permission.INTERNET" />
    <application
        android:name=".MainApplication"
        android:label="@string/app_name"
        android:icon="@mipmap/ic_launcher">
    </application>
</manifest>

```

---

## Q103. 💡 Submitting apps to Apple App Store

Follow Apple App Store guidelines for app quality, content, and technical requirements - use App Store Connect for submission (App Store Connect). Follow App Store review guidelines (app review).

- **Trade-offs**: The catch is meet technical requirements (technical requirements) - include privacy policy (privacy policy). Use App Store Connect for submission (App Store Connect), but watch out - follow iOS design guidelines (human interface guidelines).

Example:

```xml
<!-- Info.plist requirements -->
<dict>
    <key>CFBundleDisplayName</key>
    <string>My App</string>
    <key>CFBundleIdentifier</key>
    <string>com.myapp</string>
    <key>NSPrivacyPolicyURL</key>
    <string>https://example.com/privacy</string>
</dict>

```

---

## Q104. 🔧 Implementing phased rollouts

Use store-specific rollout features to gradually release updates to users - ability to pause or rollback if issues arise (rollback). Release updates to subset of users first (gradual release).

- **Trade-offs**: The catch is monitor metrics and user feedback (monitoring) - automatically promote successful rollouts (auto-promotion). Ability to pause or rollback if issues arise (rollback), but watch out - reduce risk of widespread issues (risk mitigation).

Example:

```jsx
const rolloutConfig = {
  android: {
    rolloutPercentage: 20, // Start with 20% of users
    monitoringPeriod: 7, // Monitor for 7 days
    autoPromote: true
  },
  ios: {
    phasedReleasePeriod: 7 // 7 days for phased release
  }
};

```

---

## Q105. 🏗️ Setting up Fastlane for iOS automation

Use Fastlane to automate iOS build, test, and deployment processes - automate repetitive iOS build tasks (iOS automation). Configure Fastlane for iOS builds (iOS configuration).

- **Trade-offs**: The catch is automate iOS app signing and provisioning (signing automation) - automate App Store submission (App Store automation). Automate repetitive iOS build tasks (iOS automation), but watch out - integrate with CI/CD pipelines (CI/CD integration).

Example:

```ruby
# Fastfile
platform :ios do
  desc "Build and upload to App Store"
  lane :deploy do
    match(type: "appstore")
    build_app(scheme: "MyApp")
    upload_to_app_store
  end
end
```

---

## Q106. 🏗️ Setting up Fastlane for Android automation

Use Fastlane to automate Android build, test, and deployment processes - automate repetitive Android build tasks (Android automation). Configure Fastlane for Android builds (Android configuration).

- **Trade-offs**: The catch is automate Android app signing (signing automation) - automate Play Store submission (Play Store automation). Automate repetitive Android build tasks (Android automation), but watch out - integrate with CI/CD pipelines (CI/CD integration).

Example:

```ruby
# Fastfile
platform :android do
  desc "Build and upload to Play Store"
  lane :deploy do
    gradle(
      task: "bundle",
      build_type: "Release"
    )
    upload_to_play_store
  end
end
```

---

## Q107. 🔧 Configuring Fastlane lanes and actions

Configure Fastlane lanes to organize build and deployment workflows - use actions to perform specific tasks (actions). Create custom lanes for different workflows (custom lanes).

- **Trade-offs**: The catch is organize lanes by platform and purpose (lane organization) - reuse actions across lanes (action reuse). Use actions to perform specific tasks (actions), but watch out - configure lanes for different environments (environment configuration).

Example:

```ruby
# Fastfile
platform :ios do
  lane :beta do
    build_app(scheme: "MyApp")
    upload_to_testflight
  end

  lane :release do
    match(type: "appstore")
    build_app(scheme: "MyApp")
    upload_to_app_store
  end
end
```

---

## Q108. 💡 Handling store rejections and resubmissions

Common causes include policy violations, technical issues, and quality problems that need to be addressed - prevention is better than fixing rejections. Follow store policies and guidelines (policy violations), Fix crashes and performance issues (technical issues).

- **Trade-offs**: The catch is ensure appropriate content (content issues), Accurate app descriptions (metadata issues) - meet quality standards (quality issues). Prevention is better than fixing rejections, but watch out - address all rejection reasons systematically.

Example:

```jsx
// Common rejection causes and fixes

// 1. Privacy Policy missing
// Fix: Add privacy policy link in app

// 2. App crashes on launch
// Fix: Test thoroughly and fix crashes

// 3. Misleading metadata
// Fix: Ensure accurate app descriptions

```

---

## Q109. 💡 Reducing app size for store submission

Use Hermes, code obfuscation, asset optimization, and other techniques to reduce app size - smaller apps improve download rates. Use Hermes JavaScript engine, Enable code obfuscation and shrinking (Proguard).

- **Trade-offs**: The catch is analyze bundle size (bundle analysis) - remove unused code (tree shaking). Smaller apps improve download rates, but watch out - optimize images and assets (asset optimization).

Example:

```gradle
// android/app/build.gradle
android {
    buildTypes {
        release {
            minifyEnabled true
            shrinkResources true
            proguardFiles getDefaultProguardFile('proguard-android-optimize.txt'), 'proguard-rules.pro'
        }
    }
}

```

---

## Q110. 📱 Implementing analytics in React Native apps

Integrate analytics tools to track user behavior and app performance - analytics help improve app experience. Firebase Analytics (Google's analytics platform), Segment (customer data platform).

- **Trade-offs**: The catch is understand user behavior (user behavior) - monitor app performance (performance monitoring). Analytics help improve app experience, but watch out - track user interactions (event tracking).

Example:

```jsx
import analytics from '@react-native-firebase/analytics';

function App() {
  useEffect(() => {
    analytics().logAppOpen();
  }, []);

  const trackEvent = (eventName, params) => {
    analytics().logEvent(eventName, params);
  };
}

```

---

## Q111. 💡 Handling app signing and certificates

Use proper certificate management, secure signing practices, and automated release processes - secure signing is critical for production. Keep Android keystore secure (keystore security), Manage iOS certificates properly (certificate management).

- **Trade-offs**: The catch is backup signing keys and certificates (backup) - rotate certificates regularly (rotation). Secure signing is critical for production, but watch out - use automated signing when possible (automated signing).

Example:

```bash

# Android keystore management

keytool -genkey -v -keystore my-release-key.keystore \
        -alias my-key-alias -keyalg RSA -keysize 2048 \
        -validity 10000

# iOS certificate management - Use Xcode

```

---

## Q112. 📱 Setting up CI/CD pipelines for React Native

Configure automated pipelines for building, testing, and deploying React Native apps - implement quality gates in pipeline (quality gates). Use GitHub Actions for CI/CD (GitHub Actions).

- **Trade-offs**: The catch is build apps automatically (automated building) - deploy to stores automatically (automated deployment). Implement quality gates in pipeline (quality gates), but watch out - run tests automatically (automated testing).

Example:

```yaml

# .github/workflows/deploy.yml

name: Deploy
on:
  push:
    branches: [main]

jobs:
  build:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v2
      - run: npm install
      - run: npm test
      - run: npm run build:android
      - run: npm run build:ios

```

---

