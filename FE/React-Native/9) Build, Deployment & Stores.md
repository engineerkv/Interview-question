# 🏗 9. Build, Deployment & Stores (Q79–90)

---

## 79) How do you create an Android release build using Gradle and keystore?

Configure signing in build.gradle, create a keystore, and build the release APK.

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

- **Core Steps**: Use keytool to create release keystore (keystore creation)
- **Real-World Configuration**: Configure signing in build.gradle (signing configuration)
- **Common Practice**: Enable code obfuscation for release builds (Proguard)
- **Security**: Keep keystore and passwords secure
- **Interview Tip**: Explain that use gradlew assembleRelease to build (build process)

---

## 80) How do you create an iOS release build using Xcode and provisioning profiles?

Configure code signing in Xcode, create provisioning profiles, and archive the app.

```bash
# iOS build process
# 1. Open project in Xcode
# 2. Configure signing & capabilities
# 3. Select provisioning profile
# 4. Archive the app
# 5. Distribute to App Store
```

- **Core Steps**: Configure code signing in Xcode (code signing)
- **Real-World Setup**: Create and manage provisioning profiles (provisioning profiles)
- **Common Process**: Archive app for distribution (archive process)
- **Advanced Feature**: Upload to App Store Connect (App Store Connect)
- **Interview Tip**: Explain that manage development and distribution certificates (certificates)

---

## 81) How do you manage build numbers and versioning across both platforms?

Use consistent versioning strategies and automate version management across platforms.

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

- **Core Strategy**: Use semantic versioning (major.minor.patch) (semantic versioning)
- **Real-World Use**: Android version code (integer) (version code)
- **Common Practice**: iOS bundle version (string) (bundle version)
- **Advanced Feature**: Automate version management (automation)
- **Interview Tip**: Explain that keep versions consistent across platforms (consistency)

---

## 82) What are the guidelines for Play Store submission (Android)?

Follow Google Play Store guidelines for app quality, content, and technical requirements.

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

- **Core Requirements**: Meet quality guidelines and standards (app quality)
- **Real-World Compliance**: Follow content and policy guidelines (content policy)
- **Common Requirements**: Meet technical requirements (technical requirements)
- **Advanced Feature**: Include privacy policy (privacy policy)
- **Interview Tip**: Explain that target recent Android API levels (target API)

---

## 83) What are the guidelines for App Store submission (iOS)?

Follow Apple App Store guidelines for app quality, content, and technical requirements.

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

- **Core Requirements**: Follow App Store review guidelines (app review)
- **Real-World Compliance**: Follow iOS design guidelines (human interface guidelines)
- **Common Requirements**: Meet technical requirements (technical requirements)
- **Advanced Feature**: Include privacy policy (privacy policy)
- **Interview Tip**: Explain that use App Store Connect for submission (App Store Connect)

---

## 84) How do you handle **phased rollouts** or staged updates?

Use store-specific rollout features to gradually release updates to users.

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

- **Core Strategy**: Release updates to subset of users first (gradual release)
- **Real-World Benefit**: Reduce risk of widespread issues (risk mitigation)
- **Common Practice**: Monitor metrics and user feedback (monitoring)
- **Advanced Feature**: Automatically promote successful rollouts (auto-promotion)
- **Interview Tip**: Explain that ability to pause or rollback if issues arise (rollback)

---

## 85) How do you automate builds using **Fastlane**, **EAS**, or **Bitrise**?

Use CI/CD tools to automate the build, test, and deployment process.

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

- **Core Tools**: Fastlane (Ruby-based automation tool), EAS (Expo's build and deployment service), Bitrise (cloud-based CI/CD platform)
- **Real-World Use**: Automate repetitive build tasks (automation)
- **Common Integration**: Integrate with CI/CD pipelines (CI/CD integration)
- **Advanced Feature**: Full automation of build and deployment
- **Interview Tip**: Explain that automation improves development workflow

---

## 86) What are common causes of store rejections and how to fix them?

Common causes include policy violations, technical issues, and quality problems that need to be addressed.

```jsx
// Common rejection causes and fixes

// 1. Privacy Policy missing
// Fix: Add privacy policy link in app

// 2. App crashes on launch
// Fix: Test thoroughly and fix crashes

// 3. Misleading metadata
// Fix: Ensure accurate app descriptions
```

- **Common Causes**: Follow store policies and guidelines (policy violations), Fix crashes and performance issues (technical issues)
- **Real-World Problems**: Ensure appropriate content (content issues), Accurate app descriptions (metadata issues)
- **Common Fix**: Meet quality standards (quality issues)
- **Advanced Practice**: Address all rejection reasons systematically
- **Interview Tip**: Explain that prevention is better than fixing rejections

---

## 87) How do you reduce app size (Hermes, Proguard, asset optimization)?

Use Hermes, code obfuscation, asset optimization, and other techniques to reduce app size.

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

- **Core Techniques**: Use Hermes JavaScript engine, Enable code obfuscation and shrinking (Proguard)
- **Real-World Practice**: Optimize images and assets (asset optimization)
- **Common Analysis**: Analyze bundle size (bundle analysis)
- **Advanced Feature**: Remove unused code (tree shaking)
- **Interview Tip**: Explain that smaller apps improve download rates

---

## 88) How do you handle app analytics and tracking (Firebase, Segment)?

Integrate analytics tools to track user behavior and app performance.

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

- **Core Tools**: Firebase Analytics (Google's analytics platform), Segment (customer data platform)
- **Real-World Use**: Track user interactions (event tracking)
- **Common Practice**: Understand user behavior (user behavior)
- **Advanced Feature**: Monitor app performance (performance monitoring)
- **Interview Tip**: Explain that analytics help improve app experience

---

## 89) What are best practices for signing, certificates, and release management?

Use proper certificate management, secure signing practices, and automated release processes.

```bash
# Android keystore management
keytool -genkey -v -keystore my-release-key.keystore \
        -alias my-key-alias -keyalg RSA -keysize 2048 \
        -validity 10000

# iOS certificate management - Use Xcode
```

- **Core Practices**: Keep Android keystore secure (keystore security), Manage iOS certificates properly (certificate management)
- **Real-World Use**: Use automated signing when possible (automated signing)
- **Common Practice**: Backup signing keys and certificates (backup)
- **Advanced Feature**: Rotate certificates regularly (rotation)
- **Interview Tip**: Explain that secure signing is critical for production

---

## 90) How do you set up CI/CD pipelines for React Native apps?

Configure automated pipelines for building, testing, and deploying React Native apps.

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

- **Core Tools**: Use GitHub Actions for CI/CD (GitHub Actions)
- **Real-World Use**: Run tests automatically (automated testing)
- **Common Practice**: Build apps automatically (automated building)
- **Advanced Feature**: Deploy to stores automatically (automated deployment)
- **Interview Tip**: Explain that implement quality gates in pipeline (quality gates)

---
