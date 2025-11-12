# 🏗 9. Build, Deployment & Stores (Q79–90)

---

## 🧩 Q79. How do you create an Android release build using Gradle and keystore?

### 🧠 Concept

Configure signing in build.gradle, create a keystore, and build the release APK. Use gradlew assembleRelease to build (build process).

---

### 💡 Example

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

### 🔍 Deep Insights

* **Rule:** Use keytool to create release keystore (keystore creation).
* **Use Case:** Configure signing in build.gradle (signing configuration).
* **Common Mistake:** Enable code obfuscation for release builds (Proguard).
* **Pro Tip:** Keep keystore and passwords secure.

---

### ⭐ Senior Takeaway

Use gradlew assembleRelease to build (build process).

---

## 🧩 Q80. How do you create an iOS release build using Xcode and provisioning profiles?

### 🧠 Concept

Configure code signing in Xcode, create provisioning profiles, and archive the app. Manage development and distribution certificates (certificates).

---

### 💡 Example

```bash
# iOS build process
# 1. Open project in Xcode
# 2. Configure signing & capabilities
# 3. Select provisioning profile
# 4. Archive the app
# 5. Distribute to App Store
```

---

### 🔍 Deep Insights

* **Rule:** Configure code signing in Xcode (code signing).
* **Use Case:** Create and manage provisioning profiles (provisioning profiles).
* **Common Mistake:** Archive app for distribution (archive process).
* **Pro Tip:** Upload to App Store Connect (App Store Connect).

---

### ⭐ Senior Takeaway

Manage development and distribution certificates (certificates).

---

## 🧩 Q81. How do you manage build numbers and versioning across both platforms?

### 🧠 Concept

Use consistent versioning strategies and automate version management across platforms. Keep versions consistent across platforms (consistency).

---

### 💡 Example

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

### 🔍 Deep Insights

* **Rule:** Use semantic versioning (major.minor.patch) (semantic versioning).
* **Use Case:** Android version code (integer) (version code).
* **Common Mistake:** iOS bundle version (string) (bundle version).
* **Pro Tip:** Automate version management (automation).

---

### ⭐ Senior Takeaway

Keep versions consistent across platforms (consistency).

---

## 🧩 Q82. What are the guidelines for Play Store submission?

### 🧠 Concept

Follow Google Play Store guidelines for app quality, content, and technical requirements. Target recent Android API levels (target API).

---

### 💡 Example

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

### 🔍 Deep Insights

* **Rule:** Meet quality guidelines and standards (app quality).
* **Use Case:** Follow content and policy guidelines (content policy).
* **Common Mistake:** Meet technical requirements (technical requirements).
* **Pro Tip:** Include privacy policy (privacy policy).

---

### ⭐ Senior Takeaway

Target recent Android API levels (target API).

---

## 🧩 Q83. What are the guidelines for App Store submission?

### 🧠 Concept

Follow Apple App Store guidelines for app quality, content, and technical requirements. Use App Store Connect for submission (App Store Connect).

---

### 💡 Example

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

### 🔍 Deep Insights

* **Rule:** Follow App Store review guidelines (app review).
* **Use Case:** Follow iOS design guidelines (human interface guidelines).
* **Common Mistake:** Meet technical requirements (technical requirements).
* **Pro Tip:** Include privacy policy (privacy policy).

---

### ⭐ Senior Takeaway

Use App Store Connect for submission (App Store Connect).

---

## 🧩 Q84. How do you handle phased rollouts or staged updates?

### 🧠 Concept

Use store-specific rollout features to gradually release updates to users. Ability to pause or rollback if issues arise (rollback).

---

### 💡 Example

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

### 🔍 Deep Insights

* **Rule:** Release updates to subset of users first (gradual release).
* **Use Case:** Reduce risk of widespread issues (risk mitigation).
* **Common Mistake:** Monitor metrics and user feedback (monitoring).
* **Pro Tip:** Automatically promote successful rollouts (auto-promotion).

---

### ⭐ Senior Takeaway

Ability to pause or rollback if issues arise (rollback).

---

## 🧩 Q85. How do you automate builds using Fastlane, EAS, or Bitrise?

### 🧠 Concept

Use CI/CD tools to automate the build, test, and deployment process. Automation improves development workflow.

---

### 💡 Example

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

### 🔍 Deep Insights

* **Rule:** Fastlane (Ruby-based automation tool), EAS (Expo's build and deployment service), Bitrise (cloud-based CI/CD platform).
* **Use Case:** Automate repetitive build tasks (automation).
* **Common Mistake:** Integrate with CI/CD pipelines (CI/CD integration).
* **Pro Tip:** Full automation of build and deployment.

---

### ⭐ Senior Takeaway

Automation improves development workflow.

---

## 🧩 Q86. What are common causes of store rejections and how to fix them?

### 🧠 Concept

Common causes include policy violations, technical issues, and quality problems that need to be addressed. Prevention is better than fixing rejections.

---

### 💡 Example

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

### 🔍 Deep Insights

* **Rule:** Follow store policies and guidelines (policy violations), Fix crashes and performance issues (technical issues).
* **Use Case:** Ensure appropriate content (content issues), Accurate app descriptions (metadata issues).
* **Common Mistake:** Meet quality standards (quality issues).
* **Pro Tip:** Address all rejection reasons systematically.

---

### ⭐ Senior Takeaway

Prevention is better than fixing rejections.

---

## 🧩 Q87. How do you reduce app size?

### 🧠 Concept

Use Hermes, code obfuscation, asset optimization, and other techniques to reduce app size. Smaller apps improve download rates.

---

### 💡 Example

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

### 🔍 Deep Insights

* **Rule:** Use Hermes JavaScript engine, Enable code obfuscation and shrinking (Proguard).
* **Use Case:** Optimize images and assets (asset optimization).
* **Common Mistake:** Analyze bundle size (bundle analysis).
* **Pro Tip:** Remove unused code (tree shaking).

---

### ⭐ Senior Takeaway

Smaller apps improve download rates.

---

## 🧩 Q88. How do you handle app analytics and tracking?

### 🧠 Concept

Integrate analytics tools to track user behavior and app performance. Analytics help improve app experience.

---

### 💡 Example

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

### 🔍 Deep Insights

* **Rule:** Firebase Analytics (Google's analytics platform), Segment (customer data platform).
* **Use Case:** Track user interactions (event tracking).
* **Common Mistake:** Understand user behavior (user behavior).
* **Pro Tip:** Monitor app performance (performance monitoring).

---

### ⭐ Senior Takeaway

Analytics help improve app experience.

---

## 🧩 Q89. What are best practices for signing, certificates, and release management?

### 🧠 Concept

Use proper certificate management, secure signing practices, and automated release processes. Secure signing is critical for production.

---

### 💡 Example

```bash
# Android keystore management
keytool -genkey -v -keystore my-release-key.keystore \
        -alias my-key-alias -keyalg RSA -keysize 2048 \
        -validity 10000

# iOS certificate management - Use Xcode
```

---

### 🔍 Deep Insights

* **Rule:** Keep Android keystore secure (keystore security), Manage iOS certificates properly (certificate management).
* **Use Case:** Use automated signing when possible (automated signing).
* **Common Mistake:** Backup signing keys and certificates (backup).
* **Pro Tip:** Rotate certificates regularly (rotation).

---

### ⭐ Senior Takeaway

Secure signing is critical for production.

---

## 🧩 Q90. How do you set up CI/CD pipelines for React Native apps?

### 🧠 Concept

Configure automated pipelines for building, testing, and deploying React Native apps. Implement quality gates in pipeline (quality gates).

---

### 💡 Example

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

### 🔍 Deep Insights

* **Rule:** Use GitHub Actions for CI/CD (GitHub Actions).
* **Use Case:** Run tests automatically (automated testing).
* **Common Mistake:** Build apps automatically (automated building).
* **Pro Tip:** Deploy to stores automatically (automated deployment).

---

### ⭐ Senior Takeaway

Implement quality gates in pipeline (quality gates).

---
