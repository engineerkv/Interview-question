# 9. Build, Deployment & Stores (Q79–90)

---

## Q79. How do you create an Android release build using Gradle and keystore?

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

## Q80. How do you create an iOS release build using Xcode and provisioning profiles?

Configure code signing in Xcode, create provisioning profiles, and archive the app - manage development and distribution certificates (certificates). Configure code signing in Xcode (code signing).

- **Trade-offs**: The catch is archive app for distribution (archive process) - upload to App Store Connect (App Store Connect). Manage development and distribution certificates (certificates), but watch out - create and manage provisioning profiles (provisioning profiles).

Example:

```bash
# iOS build process
# 1. Open project in Xcode
# 2. Configure signing & capabilities
# 3. Select provisioning profile
# 4. Archive the app
# 5. Distribute to App Store
```

---

## Q81. How do you manage build numbers and versioning across both platforms?

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

## Q82. What are the guidelines for Play Store submission?

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

## Q83. What are the guidelines for App Store submission?

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

## Q84. How do you handle phased rollouts or staged updates?

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

## Q85. How do you automate builds using Fastlane, EAS, or Bitrise?

Use CI/CD tools to automate the build, test, and deployment process - automation improves development workflow. Fastlane (Ruby-based automation tool), EAS (Expo's build and deployment service), Bitrise (cloud-based CI/CD platform).

- **Trade-offs**: The catch is integrate with CI/CD pipelines (CI/CD integration) - full automation of build and deployment. Automation improves development workflow, but watch out - automate repetitive build tasks (automation).

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

## Q86. What are common causes of store rejections and how to fix them?

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

## Q87. How do you reduce app size?

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

## Q88. How do you handle app analytics and tracking?

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

## Q89. What are best practices for signing, certificates, and release management?

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

## Q90. How do you set up CI/CD pipelines for React Native apps?

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
