# ⚛️ React Native Interview Notes (2025 Edition)

## 🧩 Section 2 — Android & iOS Platform Essentials — Q31-Q60

---

## **Q31. What is the Android Activity lifecycle in React Native?**

**🧠 Concept**

The Android Activity lifecycle manages the different states of an Android app and React Native integrates with these lifecycle events.

**💻 Example**
```java
public class MainActivity extends ReactActivity {
    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
    }

    @Override
    protected void onResume() {
        super.onResume();
    }
}
```

**💬 Explanation + Insight**

- **onCreate** - Activity is being created, set up initial state
- **onResume** - Activity is visible and interactive (foreground)
- **onPause** - Activity is not visible but still running
- **React Native Integration** - Integrates with these lifecycle events
- **Performance** - Handle lifecycle events for better performance

---

## **Q32. What is the iOS App lifecycle in React Native?**

**🧠 Concept**

The iOS App lifecycle manages different states of an iOS app and React Native provides hooks to handle these transitions.

**💻 Example**
```javascript
import { AppState } from 'react-native';

const App = () => {
  const [appState, setAppState] = useState(AppState.currentState);

  useEffect(() => {
    const handleAppStateChange = (nextAppState) => {
      if (nextAppState === 'active') {
        console.log('App has come to the foreground!');
      } else {
        console.log('App has gone to the background!');
      }
      setAppState(nextAppState);
    };

    const subscription = AppState.addEventListener('change', handleAppStateChange);
    return () => subscription?.remove();
  }, []);
};
```

**💬 Explanation + Insight**

- Active: App is in foreground and receiving events
- Background: App is in background but still running
- Suspended: App is in background and not running
- React Native: Provides AppState API to handle these states
- Performance: Handle state changes for better performance

---

## **Q33. What is MainActivity.java in React Native?**

**🧠 Concept**

MainActivity.java is the main entry point for Android React Native apps, extending ReactActivity and handling the initial setup of the React Native environment.

**💻 Example**
```java
public class MainActivity extends ReactActivity {
    @Override
    protected String getMainComponentName() {
        return "MyApp";
    }

    @Override
    protected ReactActivityDelegate createReactActivityDelegate() {
        return new DefaultReactActivityDelegate(
            this,
            getMainComponentName(),
            DefaultNewArchitectureEntryPoint.getFabricEnabled()
        );
    }
}
```

**💬 Explanation + Insight**

- Entry point: Main entry point for Android React Native apps
- ReactActivity: Extends ReactActivity for React Native integration
- getMainComponentName: Returns the name of the main React component
- New Architecture: Supports new React Native architecture
- Performance: Handles initial setup for better performance

---

## **Q34. What is MainApplication.java in React Native?**

**🧠 Concept**

MainApplication.java is the Android application class that initializes React Native, registers native modules, and configures the React Native environment.

**💻 Example**
```java
public class MainApplication extends Application implements ReactApplication {
    private final ReactNativeHost mReactNativeHost = new DefaultReactNativeHost(this) {
        @Override
        public boolean getUseDeveloperSupport() {
            return BuildConfig.DEBUG;
        }

        @Override
        protected List<ReactPackage> getPackages() {
            return new PackageList(this).getPackages();
        }
    };

    @Override
    public ReactNativeHost getReactNativeHost() {
        return mReactNativeHost;
    }
}
```

**💬 Explanation + Insight**

- Application class: Main Android application class
- ReactNativeHost: Manages React Native environment
- getPackages: Returns list of React packages
- Developer support: Enables developer support in debug mode
- New Architecture: Supports new React Native architecture

---

## **Q35. What is AndroidManifest.xml in React Native?**

**🧠 Concept**

AndroidManifest.xml is the configuration file that declares app permissions, activities, services, and other app components for Android React Native apps.

**💻 Example**
```xml
<manifest xmlns:android="http://schemas.android.com/apk/res/android">
    <uses-permission android:name="android.permission.INTERNET" />
    <uses-permission android:name="android.permission.CAMERA" />

    <application android:name=".MainApplication">
        <activity
            android:name=".MainActivity"
            android:exported="true">
            <intent-filter>
                <action android:name="android.intent.action.MAIN" />
                <category android:name="android.intent.category.LAUNCHER" />
            </intent-filter>
        </activity>
    </application>
</manifest>
```

**💬 Explanation + Insight**

- Permissions: Declares app permissions (camera, location, internet)
- Activities: Declares app activities and their configurations
- Intent filters: Handles deep linking and app launching
- Configuration: Configures app behavior and appearance
- Security: Manages app security and permissions

---

## **Q36. What are Android permissions in React Native?**

**🧠 Concept**

Android permissions are declarations that allow React Native apps to access device features like camera, location, storage, and network.

**💻 Example**
```javascript
import { PermissionsAndroid, Platform } from 'react-native';

const requestCameraPermission = async () => {
  if (Platform.OS === 'android') {
    try {
      const granted = await PermissionsAndroid.request(
        PermissionsAndroid.PERMISSIONS.CAMERA,
        {
          title: 'Camera Permission',
          message: 'App needs access to camera to take photos',
        }
      );
      if (granted === PermissionsAndroid.RESULTS.GRANTED) {
        console.log('Camera permission granted');
      }
    } catch (err) {
      console.warn(err);
    }
  }
};
```

**💬 Explanation + Insight**

- Runtime permissions: Request permissions at runtime for sensitive features
- Manifest permissions: Declare permissions in AndroidManifest.xml
- User experience: Provide clear permission requests
- Security: Handle permissions securely
- Fallback: Handle permission denials gracefully

---

## **Q37. What are intent-filters in React Native?**

**🧠 Concept**

Intent-filters are Android mechanisms that allow React Native apps to respond to system intents like deep linking, sharing, and app launching.

**💻 Example**
```xml
<activity android:name=".MainActivity" android:exported="true">
    <intent-filter>
        <action android:name="android.intent.action.MAIN" />
        <category android:name="android.intent.category.LAUNCHER" />
    </intent-filter>
    
    <intent-filter>
        <action android:name="android.intent.action.VIEW" />
        <category android:name="android.intent.category.DEFAULT" />
        <data android:scheme="myapp" />
    </intent-filter>
</activity>
```

**💬 Explanation + Insight**

- Deep linking: Handle custom URL schemes and universal links
- Sharing: Handle content sharing from other apps
- App launching: Handle app launching from system
- Integration: Integrate with Android ecosystem
- User experience: Provide seamless app integration

---

## **Q38. What is Gradle configuration in React Native?**

**🧠 Concept**

Gradle is the build system for Android React Native apps, managing dependencies, build configurations, and compilation settings.

**💻 Example**
```gradle
android {
    compileSdkVersion rootProject.ext.compileSdkVersion

    defaultConfig {
        applicationId "com.myapp"
        minSdkVersion rootProject.ext.minSdkVersion
        targetSdkVersion rootProject.ext.targetSdkVersion
    }

    buildTypes {
        debug {
            applicationIdSuffix ".debug"
        }
        release {
            minifyEnabled true
        }
    }
}
```

**💬 Explanation + Insight**

- Build system: Manages Android app building process
- Dependencies: Manages app dependencies and libraries
- Build types: Different configurations for debug/release
- Versioning: Manages app versioning and SDK versions
- Optimization: Optimizes app for different build types

---

## **Q39. What is Info.plist in React Native iOS?**

**🧠 Concept**

Info.plist is the configuration file for iOS React Native apps that declares app permissions, URL schemes, bundle information, and other iOS-specific settings.

**💻 Example**
```xml
<plist version="1.0">
<dict>
    <key>CFBundleDisplayName</key>
    <string>My App</string>
    <key>CFBundleIdentifier</key>
    <string>com.myapp</string>
    
    <key>NSCameraUsageDescription</key>
    <string>App needs access to camera to take photos</string>
    
    <key>CFBundleURLTypes</key>
    <array>
        <dict>
            <key>CFBundleURLName</key>
            <string>myapp</string>
            <key>CFBundleURLSchemes</key>
            <array>
                <string>myapp</string>
            </array>
        </dict>
    </array>
</dict>
</plist>
```

**💬 Explanation + Insight**

- Bundle info: Declares app bundle information
- Permissions: Declares iOS permissions with usage descriptions
- URL schemes: Handles deep linking and URL schemes
- Configuration: Configures iOS-specific settings
- Security: Manages app security and permissions

---

## **Q40. What is AppDelegate in React Native iOS?**

**🧠 Concept**

AppDelegate is the main iOS application delegate that handles app lifecycle events, initializes React Native, and manages app-wide functionality.

**💻 Example**
```objc
@implementation AppDelegate

- (BOOL)application:(UIApplication *)application didFinishLaunchingWithOptions:(NSDictionary *)launchOptions
{
    RCTBridge *bridge = [[RCTBridge alloc] initWithDelegate:self launchOptions:launchOptions];
    RCTRootView *rootView = [[RCTRootView alloc] initWithBridge:bridge
                                                     moduleName:@"MyApp"
                                              initialProperties:nil];

    self.window = [[UIWindow alloc] initWithFrame:[UIScreen mainScreen].bounds];
    UIViewController *rootViewController = [UIViewController new];
    rootViewController.view = rootView;
    self.window.rootViewController = rootViewController;
    [self.window makeKeyAndVisible];
    return YES;
}

@end
```

**💬 Explanation + Insight**

- App delegate: Main iOS application delegate
- Lifecycle: Handles app lifecycle events
- React Native: Initializes React Native environment
- Bridge: Manages React Native bridge
- Configuration: Configures app behavior

---

## **Q41. What is SceneDelegate in React Native iOS?**

**🧠 Concept**

SceneDelegate is the iOS 13+ scene delegate that handles scene lifecycle events, window management, and multi-window support.

**💻 Example**
```objc
@implementation SceneDelegate

- (void)scene:(UIScene *)scene willConnectToSession:(UISceneSession *)session options:(UISceneConnectionOptions *)connectionOptions
{
    if ([scene isKindOfClass:[UIWindowScene class]]) {
        UIWindowScene *windowScene = (UIWindowScene *)scene;
        self.window = [[UIWindow alloc] initWithWindowScene:windowScene];
        
        RCTBridge *bridge = [[RCTBridge alloc] initWithDelegate:nil launchOptions:nil];
        RCTRootView *rootView = [[RCTRootView alloc] initWithBridge:bridge
                                                         moduleName:@"MyApp"
                                                  initialProperties:nil];
        
        UIViewController *rootViewController = [UIViewController new];
        rootViewController.view = rootView;
        self.window.rootViewController = rootViewController;
        [self.window makeKeyAndVisible];
    }
}

@end
```

**💬 Explanation + Insight**

- Scene delegate: Handles scene lifecycle events
- Multi-window: Supports multi-window functionality
- iOS 13+: Required for iOS 13 and later
- Window management: Manages app windows
- Performance: Handles scene performance

---

## **Q42. What are provisioning profiles in React Native iOS?**

**🧠 Concept**

Provisioning profiles are iOS certificates that allow React Native apps to run on physical devices and be distributed through the App Store.

**💻 Example**
```bash
# Xcode project settings
# Build Settings -> Code Signing Identity
# Development Team: Your Team ID
# Provisioning Profile: Automatic or specific profile
```

**💬 Explanation + Insight**

- App Store: Required for App Store distribution
- Development: Required for development on physical devices
- Certificates: Contains app signing certificates
- Device management: Manages device registration
- Security: Ensures app security and authenticity

---

## **Q43. What is CocoaPods in React Native?**

**🧠 Concept**

CocoaPods is the dependency manager for iOS React Native apps, managing native iOS dependencies and integrating with the iOS build system.

**💻 Example**
```ruby
# Podfile
platform :ios, '11.0'

target 'MyApp' do
  config = use_native_modules!

  use_react_native!(
    :path => config[:reactNativePath],
    :hermes_enabled => true,
    :fabric_enabled => true
  )
end
```

**💬 Explanation + Insight**

- Dependency manager: Manages iOS dependencies
- Integration: Integrates with React Native
- Podfile: Configuration file for dependencies
- Native modules: Manages native iOS modules
- Build system: Integrates with iOS build system

---

## **Q44. What is autolinking in React Native?**

**🧠 Concept**

Autolinking is React Native's automatic dependency linking system that automatically links native dependencies without manual configuration.

**💻 Example**
```javascript
// react-native.config.js
module.exports = {
  dependencies: {
    'react-native-vector-icons': {
      platforms: {
        ios: {
          project: './ios/VectorIcons.xcodeproj',
        },
        android: {
          sourceDir: './android/',
        },
      },
    },
  },
};
```

**💬 Explanation + Insight**

- Automatic linking: Automatically links native dependencies
- Configuration: Minimal configuration required
- Platform support: Works on both iOS and Android
- Native modules: Handles native module linking
- Performance: Optimizes linking process

---

## **Q45. What are build processes in React Native?**

**🧠 Concept**

Build processes in React Native involve compiling JavaScript, bundling assets, building native code, and creating distributable packages for iOS and Android platforms.

**💻 Example**
```bash
# Development build
npx react-native run-ios
npx react-native run-android

# Production build
cd ios && xcodebuild -workspace MyApp.xcworkspace -scheme MyApp -configuration Release
cd android && ./gradlew assembleRelease
```

**💬 Explanation + Insight**

- JavaScript bundling: Bundles JavaScript code
- Asset bundling: Bundles images, fonts, and other assets
- Native compilation: Compiles native iOS and Android code
- Optimization: Optimizes code for production
- Signing: Signs apps for distribution

---

## **Q46. How does React Native handle iOS-specific features?**

**🧠 Concept**

React Native handles iOS-specific features through platform-specific code, native modules, and iOS-specific APIs.

**💻 Example**
```javascript
import { Platform } from 'react-native';
import { request, PERMISSIONS, RESULTS } from 'react-native-permissions';

const handleIOSFeature = async () => {
  if (Platform.OS === 'ios') {
    const result = await request(PERMISSIONS.IOS.CAMERA);
    if (result === RESULTS.GRANTED) {
      // Use camera
    }
  }
};
```

**💬 Explanation + Insight**

- Platform detection: Use Platform.OS to detect iOS
- Native modules: Access iOS-specific native modules
- Permissions: Handle iOS-specific permissions
- Features: Access iOS-specific features
- Performance: Optimize for iOS performance

---

## **Q47. How does React Native handle Android-specific features?**

**🧠 Concept**

React Native handles Android-specific features through platform-specific code, native modules, and Android-specific APIs.

**💻 Example**
```javascript
import { Platform, BackHandler } from 'react-native';
import { request, PERMISSIONS, RESULTS } from 'react-native-permissions';

const handleAndroidFeature = async () => {
  if (Platform.OS === 'android') {
    const result = await request(PERMISSIONS.ANDROID.CAMERA);
    if (result === RESULTS.GRANTED) {
      // Use camera
    }
  }
};
```

**💬 Explanation + Insight**

- Platform detection: Use Platform.OS to detect Android
- Native modules: Access Android-specific native modules
- Permissions: Handle Android-specific permissions
- Features: Access Android-specific features
- Performance: Optimize for Android performance

---

## **Q48. What is the difference between iOS and Android builds in React Native?**

**🧠 Concept**

iOS and Android builds in React Native differ in build tools, signing processes, distribution methods, and platform-specific requirements.

**💻 Example**
```bash
# iOS build process
# 1. Xcode project
# 2. CocoaPods dependencies
# 3. Code signing
# 4. App Store distribution

# Android build process
# 1. Gradle build system
# 2. Android dependencies
# 3. APK signing
# 4. Play Store distribution
```

**💬 Explanation + Insight**

- Build tools: Different build tools (Xcode vs Gradle)
- Signing: Different signing processes
- Distribution: Different distribution methods
- Requirements: Different platform requirements
- Performance: Different performance characteristics

---

## **Q49. How does React Native handle platform-specific styling?**

**🧠 Concept**

React Native handles platform-specific styling through Platform.OS checks, platform-specific style files, and conditional styling.

**💻 Example**
```javascript
import { Platform, StyleSheet } from 'react-native';

const styles = StyleSheet.create({
  container: {
    flex: 1,
    backgroundColor: '#fff',
    ...Platform.select({
      ios: {
        shadowColor: '#000',
        shadowOffset: { width: 0, height: 2 },
        shadowOpacity: 0.25,
      },
      android: {
        elevation: 5,
      },
    }),
  },
  button: {
    padding: 10,
    borderRadius: Platform.OS === 'ios' ? 8 : 4,
  },
});
```

**💬 Explanation + Insight**

- Platform.OS: Check current platform for styling
- Platform.select: Choose styles based on platform
- Shadow: iOS uses shadow, Android uses elevation
- Border radius: Different border radius values
- Colors: Platform-specific color schemes

---

## **Q50. What is the React Native CLI and how does it work?**

**🧠 Concept**

The React Native CLI is the command-line interface for React Native development, providing commands for project creation, building, running, and managing React Native apps.

**💻 Example**
```bash
# Create new project
npx react-native init MyApp

# Run on iOS
npx react-native run-ios

# Run on Android
npx react-native run-android

# Build for production
npx react-native bundle --platform android --dev false --entry-file index.js
```

**💬 Explanation + Insight**

- Project creation: Creates new React Native projects
- Running apps: Runs apps on simulators and devices
- Building: Builds apps for production
- Linking: Links native dependencies
- Debugging: Provides debugging tools

---

## **Q51. What is Metro bundler in React Native?**

**🧠 Concept**

Metro is React Native's JavaScript bundler that transforms, bundles, and serves JavaScript code, similar to Webpack but optimized for mobile development.

**💻 Example**
```javascript
// metro.config.js
module.exports = {
  transformer: {
    getTransformOptions: async () => ({
      transform: {
        experimentalImportSupport: false,
        inlineRequires: true,
      },
    }),
  },
  resolver: {
    alias: {
      '@': './src',
    },
  },
};
```

**💬 Explanation + Insight**

- JavaScript bundler: Bundles all JavaScript code
- Fast refresh: Enables hot reloading during development
- Tree shaking: Removes unused code to reduce bundle size
- Asset handling: Processes images, fonts, and other assets
- Platform specific: Can create different bundles for iOS and Android
- Performance: Optimized for mobile development
- Configurable: Can be customized for specific needs
- Development: Provides development server with hot reloading

---

## **Q52. What is Flipper in React Native?**

**🧠 Concept**

Flipper is Facebook's debugging platform for React Native apps that provides network inspection, layout debugging, performance profiling, and other debugging tools.

**💻 Example**
```javascript
// Flipper integration
import { Flipper } from 'react-native-flipper';

const App = () => {
  useEffect(() => {
    // Flipper debugging
    Flipper.addPlugin({
      getId() {
        return 'MyPlugin';
      },
      onConnect(connection) {
        connection.send('greeting', { message: 'Hello from React Native!' });
      },
      onDisconnect() {
        // Cleanup
      },
    });
  }, []);

  return <Text>My App</Text>;
};
```

**💬 Explanation + Insight**

- Debugging platform: Comprehensive debugging platform
- Network inspection: Inspect network requests and responses
- Layout debugging: Debug layout and styling issues
- Performance profiling: Profile app performance
- Plugin system: Extensible plugin system
- Development: Enhances development experience
- Performance: Helps identify performance issues
- User experience: Improves debugging workflow

---

## **Q53. What is React Native Debugger?**

**🧠 Concept**

React Native Debugger is a standalone debugging tool that combines Chrome DevTools, Redux DevTools, and React Native specific debugging features in one application.

**💻 Example**
```javascript
// Enable debugging
import { DevSettings } from 'react-native';

// Open debugger
DevSettings.openDebugger();

// Debugging with Redux
import { createStore } from 'redux';
import { Provider } from 'react-redux';

const store = createStore(reducer);

const App = () => (
  <Provider store={store}>
    <MyComponent />
  </Provider>
);
```

**💬 Explanation + Insight**

- Standalone tool: Independent debugging application
- Chrome DevTools: Integrates Chrome DevTools
- Redux DevTools: Integrates Redux DevTools
- React Native specific: React Native specific debugging features
- Performance: Helps debug performance issues
- Development: Enhances development experience
- User experience: Improves debugging workflow
- Maintenance: Maintains debugging tools

---

## **Q54. What is React Native's approach to hot reloading?**

**🧠 Concept**

React Native provides hot reloading through Fast Refresh, which allows developers to see changes instantly without losing app state, improving development efficiency.

**💻 Example**
```javascript
// Fast Refresh automatically works with functional components
const MyComponent = () => {
  const [count, setCount] = useState(0);
  
  return (
    <View>
      <Text>Count: {count}</Text>
      <Button onPress={() => setCount(count + 1)} title="Increment" />
    </View>
  );
};

// Fast Refresh preserves state
const App = () => {
  const [user, setUser] = useState({ name: 'John' });
  
  return (
    <View>
      <Text>Hello {user.name}</Text>
    </View>
  );
};
```

**💬 Explanation + Insight**

- Fast Refresh: New hot reloading system
- State preservation: Preserves component state during reload
- Functional components: Works best with functional components
- Development: Improves development efficiency
- Performance: Optimizes development workflow
- User experience: Enhances development experience
- Maintenance: Reduces development time
- Compatibility: Works with modern React patterns

---

## **Q55. What is React Native's approach to code splitting?**

**🧠 Concept**

React Native handles code splitting through dynamic imports, lazy loading, and bundle optimization to reduce initial bundle size and improve app performance.

**💻 Example**
```javascript
import { lazy, Suspense } from 'react';
import { View, Text } from 'react-native';

// Lazy load components
const LazyComponent = lazy(() => import('./LazyComponent'));

const App = () => {
  return (
    <View>
      <Suspense fallback={<Text>Loading...</Text>}>
        <LazyComponent />
      </Suspense>
    </View>
  );
};

// Dynamic imports
const loadFeature = async () => {
  const { default: Feature } = await import('./Feature');
  return Feature;
};
```

**💬 Explanation + Insight**

- Dynamic imports: Load code dynamically
- Lazy loading: Load components when needed
- Bundle optimization: Reduce initial bundle size
- Performance: Improve app performance
- User experience: Faster app startup
- Maintenance: Maintain code splitting
- Compatibility: Works with modern JavaScript
- Development: Enhance development workflow

---

## **Q56. What is React Native's approach to asset management?**

**🧠 Concept**

React Native handles assets through the assets folder, require() statements, and platform-specific asset handling to manage images, fonts, and other static resources.

**💻 Example**
```javascript
import { Image } from 'react-native';

// Local assets
const localImage = require('./assets/logo.png');

// Platform-specific assets
const platformImage = require('./assets/logo.png');

// Asset with different resolutions
const multiResolutionImage = require('./assets/icon.png');

const App = () => (
  <View>
    <Image source={localImage} style={{ width: 100, height: 100 }} />
    <Image source={platformImage} style={{ width: 100, height: 100 }} />
    <Image source={multiResolutionImage} style={{ width: 100, height: 100 }} />
  </View>
);
```

**💬 Explanation + Insight**

- Asset folder: Organize assets in assets folder
- require(): Use require() for local assets
- Platform specific: Handle platform-specific assets
- Multi-resolution: Support different screen densities
- Performance: Optimize asset loading
- User experience: Provide appropriate assets
- Maintenance: Maintain asset organization
- Compatibility: Ensure compatibility across platforms

---

## **Q57. What is React Native's approach to environment variables?**

**🧠 Concept**

React Native handles environment variables through configuration files, build-time variables, and runtime configuration to manage different environments and settings.

**💻 Example**
```javascript
// .env
API_URL=https://api.example.com
DEBUG=true

// config.js
const config = {
  development: {
    API_URL: 'https://dev-api.example.com',
    DEBUG: true,
  },
  production: {
    API_URL: 'https://api.example.com',
    DEBUG: false,
  },
};

export default config[process.env.NODE_ENV || 'development'];

// Usage
import config from './config';

const fetchData = async () => {
  const response = await fetch(`${config.API_URL}/data`);
  return response.json();
};
```

**💬 Explanation + Insight**

- Environment files: Use .env files for configuration
- Build-time variables: Set variables at build time
- Runtime configuration: Configure at runtime
- Platform specific: Handle platform-specific configuration
- Security: Handle sensitive configuration securely
- Performance: Optimize configuration loading
- Maintenance: Maintain configuration
- User experience: Provide appropriate configuration

---

## **Q58. What is React Native's approach to error boundaries?**

**🧠 Concept**

React Native uses Error Boundaries to catch JavaScript errors in component trees, providing fallback UI and error reporting to handle errors gracefully.

**💻 Example**
```javascript
class ErrorBoundary extends React.Component {
  constructor(props) {
    super(props);
    this.state = { hasError: false, error: null };
  }

  static getDerivedStateFromError(error) {
    return { hasError: true, error };
  }

  componentDidCatch(error, errorInfo) {
    console.error('Error caught by boundary:', error, errorInfo);
    // Send error to crash reporting service
  }

  render() {
    if (this.state.hasError) {
      return (
        <View style={{ flex: 1, justifyContent: 'center', alignItems: 'center' }}>
          <Text>Something went wrong.</Text>
          <Button onPress={() => this.setState({ hasError: false })} title="Try Again" />
        </View>
      );
    }
    return this.props.children;
  }
}
```

**💬 Explanation + Insight**

- Error boundaries: Catch JavaScript errors in component trees
- Fallback UI: Provide fallback UI when errors occur
- Error reporting: Report errors to crash reporting services
- Graceful degradation: Handle errors gracefully
- Development: Show detailed error messages in development
- Production: Show user-friendly error messages
- Recovery: Allow users to recover from errors
- Maintenance: Maintain error handling

---

## **Q59. What is React Native's approach to performance monitoring?**

**🧠 Concept**

React Native provides performance monitoring through profiling tools, performance metrics, and monitoring libraries to track app performance and identify bottlenecks.

**💻 Example**
```javascript
import { Performance } from 'react-native-performance';

// Track performance metrics
const trackPerformance = () => {
  const startTime = performance.now();
  
  // Perform expensive operation
  expensiveOperation();
  
  const endTime = performance.now();
  const duration = endTime - startTime;
  
  console.log(`Operation took ${duration} milliseconds`);
};

// Monitor memory usage
const monitorMemory = () => {
  const memoryInfo = performance.memory;
  console.log('Memory usage:', memoryInfo);
};
```

**💬 Explanation + Insight**

- Performance metrics: Track performance metrics
- Memory monitoring: Monitor memory usage
- Profiling: Profile app performance
- Bottleneck identification: Identify performance bottlenecks
- Optimization: Optimize app performance
- User experience: Improve user experience
- Maintenance: Maintain performance monitoring
- Development: Enhance development workflow

---

## **Q60. What is React Native's approach to testing on different platforms?**

**🧠 Concept**

React Native handles testing on different platforms through platform-specific testing tools, simulators, and real device testing to ensure compatibility and functionality.

**💻 Example**
```javascript
// Platform-specific testing
import { Platform } from 'react-native';

const testPlatformFeature = () => {
  if (Platform.OS === 'ios') {
    // Test iOS-specific features
    testIOSFeature();
  } else if (Platform.OS === 'android') {
    // Test Android-specific features
    testAndroidFeature();
  }
};

// Test on different screen sizes
import { Dimensions } from 'react-native';

const testResponsiveDesign = () => {
  const { width, height } = Dimensions.get('window');
  if (width > 768) {
    // Test tablet layout
    testTabletLayout();
  } else {
    // Test phone layout
    testPhoneLayout();
  }
};
```

**💬 Explanation + Insight**

- Platform testing: Test on different platforms
- Screen size testing: Test on different screen sizes
- Device testing: Test on real devices
- Simulator testing: Test on simulators
- Performance testing: Test performance on different platforms
- User experience: Ensure consistent user experience
- Compatibility: Ensure compatibility across platforms
- Maintenance: Maintain testing processes

---

*This section covers Android Activity lifecycle, iOS App lifecycle, MainActivity.java, MainApplication.java, AndroidManifest.xml, permissions, intent-filters, Gradle configuration, Info.plist, AppDelegate, SceneDelegate, provisioning profiles, CocoaPods, autolinking, and build processes.*
