# ⚛️ React Native Interview Notes (2025 Edition)

## 🛠️ Section 7 — Real-World Scenarios & Architecture — Q141-Q160

---

## **Q141. How do you integrate push notifications (FCM, APNs)?**

**🧠 Concept**

Push notifications are integrated using Firebase Cloud Messaging (FCM) for Android and Apple Push Notification Service (APNs) for iOS to send real-time notifications to users.

**💻 Example**
```javascript
import messaging from '@react-native-firebase/messaging';

const MyComponent = () => {
  useEffect(() => {
    const requestPermission = async () => {
      const authStatus = await messaging().requestPermission();
      const enabled = authStatus === messaging.AuthorizationStatus.AUTHORIZED;
      
      if (enabled) {
        const token = await messaging().getToken();
        console.log('FCM Token:', token);
      }
    };

    requestPermission();
  }, []);

  return <View>{/* Component content */}</View>;
};
```

**💬 Explanation + Insight**

- FCM: Firebase Cloud Messaging for Android
- APNs: Apple Push Notification Service for iOS
- Permissions: Request notification permissions
- Tokens: Get device tokens for targeting
- Real-time: Send real-time notifications

---

## **Q142. How do you implement biometric authentication (Face ID, Touch ID)?**

**🧠 Concept**

Biometric authentication is implemented using biometric libraries to authenticate users using fingerprint, face, or other biometric data.

**💻 Example**
```javascript
import TouchID from 'react-native-touch-id';

const MyComponent = () => {
  const [biometricAvailable, setBiometricAvailable] = useState(false);

  useEffect(() => {
    const checkBiometric = async () => {
      try {
        const available = await TouchID.isSupported();
        setBiometricAvailable(available);
      } catch (error) {
        console.error('Biometric not available:', error);
      }
    };

    checkBiometric();
  }, []);

  const authenticateWithBiometric = async () => {
    try {
      const result = await TouchID.authenticate('Authenticate to continue');
      return result;
    } catch (error) {
      console.error('Biometric authentication failed:', error);
    }
  };

  return <View>{/* Component content */}</View>;
};
```

**💬 Explanation + Insight**

- Biometric support: Checks for biometric support
- Authentication: Authenticates users with biometrics
- Security: Provides secure authentication
- User experience: Enhances user experience
- Fallback: Provides fallback authentication methods

---

## **Q143. How do you build an offline-first app using Realm or MMKV?**

**🧠 Concept**

Offline-first apps are built by using local storage solutions like Realm or MMKV to store data locally and sync when online.

**💻 Example**
```javascript
import Realm from 'realm';

const MyComponent = () => {
  const [realm, setRealm] = useState(null);

  useEffect(() => {
    const openRealm = async () => {
      const realmInstance = await Realm.open({
        schema: [UserSchema, PostSchema],
        schemaVersion: 1,
      });
      setRealm(realmInstance);
    };

    openRealm();
  }, []);

  const saveData = (data) => {
    if (realm) {
      realm.write(() => {
        realm.create('User', data);
      });
    }
  };

  return <View>{/* Component content */}</View>;
};
```

**💬 Explanation + Insight**

- Local storage: Store data locally
- Offline support: Works without internet
- Sync: Sync data when online
- Performance: Fast local access
- User experience: Seamless offline experience

---

## **Q144. How do you implement feature flags (LaunchDarkly or custom)?**

**🧠 Concept**

Feature flags are implemented to enable/disable features dynamically without deploying new code, allowing for controlled rollouts and A/B testing.

**💻 Example**
```javascript
import { LaunchDarkly } from 'react-native-launchdarkly';

const MyComponent = () => {
  const [featureEnabled, setFeatureEnabled] = useState(false);

  useEffect(() => {
    const checkFeature = async () => {
      const enabled = await LaunchDarkly.boolVariation('new-feature', false);
      setFeatureEnabled(enabled);
    };

    checkFeature();
  }, []);

  return (
    <View>
      {featureEnabled ? (
        <NewFeatureComponent />
      ) : (
        <OldFeatureComponent />
      )}
    </View>
  );
};
```

**💬 Explanation + Insight**

- Dynamic features: Enable/disable features dynamically
- A/B testing: Test different feature versions
- Rollouts: Controlled feature rollouts
- Configuration: Remote configuration
- User experience: Personalized experiences

---

## **Q145. How do you implement dark mode with persistent state?**

**🧠 Concept**

Dark mode is implemented by creating theme contexts, storing user preferences, and applying different styles based on the current theme.

**💻 Example**
```javascript
import AsyncStorage from '@react-native-async-storage/async-storage';

const ThemeContext = createContext();

const ThemeProvider = ({ children }) => {
  const [isDarkMode, setIsDarkMode] = useState(false);

  useEffect(() => {
    const loadTheme = async () => {
      const savedTheme = await AsyncStorage.getItem('theme');
      if (savedTheme) {
        setIsDarkMode(savedTheme === 'dark');
      }
    };
    loadTheme();
  }, []);

  const toggleTheme = async () => {
    const newTheme = !isDarkMode;
    setIsDarkMode(newTheme);
    await AsyncStorage.setItem('theme', newTheme ? 'dark' : 'light');
  };

  return (
    <ThemeContext.Provider value={{ isDarkMode, toggleTheme }}>
      {children}
    </ThemeContext.Provider>
  );
};
```

**💬 Explanation + Insight**

- Theme context: Manage theme state
- Persistence: Store theme preferences
- Dynamic styling: Apply styles based on theme
- User experience: Better user experience
- Accessibility: Support for user preferences

---

## **Q146. How do you integrate Maps, Camera, or Payment SDKs?**

**🧠 Concept**

Third-party SDKs are integrated by adding native dependencies and creating bridge modules to expose SDK functionality to JavaScript.

**💻 Example**
```javascript
import { NativeModules } from 'react-native';

const MyComponent = () => {
  const { MapsSDK, CameraSDK, PaymentSDK } = NativeModules;

  const openMap = async () => {
    try {
      await MapsSDK.openMap(latitude, longitude);
    } catch (error) {
      console.error('Map error:', error);
    }
  };

  const takePhoto = async () => {
    try {
      const photo = await CameraSDK.takePhoto();
      return photo;
    } catch (error) {
      console.error('Camera error:', error);
    }
  };

  const processPayment = async (amount) => {
    try {
      const result = await PaymentSDK.processPayment(amount);
      return result;
    } catch (error) {
      console.error('Payment error:', error);
    }
  };

  return <View>{/* Component content */}</View>;
};
```

**💬 Explanation + Insight**

- SDK integration: Integrate third-party SDKs
- Native modules: Create bridge modules
- Error handling: Handle SDK errors
- User experience: Provide seamless integration
- Performance: Optimize SDK usage

---

## **Q147. How do you design skeleton loaders for perceived performance?**

**🧠 Concept**

Skeleton loaders are designed to show placeholder content while data is loading, improving perceived performance and user experience.

**💻 Example**
```javascript
const SkeletonLoader = () => (
  <View style={styles.skeletonContainer}>
    <View style={styles.skeletonHeader} />
    <View style={styles.skeletonContent}>
      <View style={styles.skeletonLine} />
      <View style={styles.skeletonLine} />
      <View style={styles.skeletonLine} />
    </View>
  </View>
);

const MyComponent = () => {
  const [loading, setLoading] = useState(true);
  const [data, setData] = useState(null);

  useEffect(() => {
    const fetchData = async () => {
      setLoading(true);
      const result = await api.getData();
      setData(result);
      setLoading(false);
    };

    fetchData();
  }, []);

  if (loading) {
    return <SkeletonLoader />;
  }

  return <DataComponent data={data} />;
};
```

**💬 Explanation + Insight**

- Placeholder content: Show loading placeholders
- Perceived performance: Improve perceived performance
- User experience: Better user experience
- Loading states: Handle loading states
- Animation: Add loading animations

---

## **Q148. How do you use React Query to cache API calls?**

**🧠 Concept**

React Query is used to cache API calls, manage server state, and provide background updates for better performance and user experience.

**💻 Example**
```javascript
import { useQuery, useMutation, useQueryClient } from 'react-query';

const MyComponent = () => {
  const queryClient = useQueryClient();

  const { data, isLoading, error } = useQuery('users', fetchUsers, {
    staleTime: 5 * 60 * 1000, // 5 minutes
    cacheTime: 10 * 60 * 1000, // 10 minutes
  });

  const mutation = useMutation(updateUser, {
    onSuccess: () => {
      queryClient.invalidateQueries('users');
    },
  });

  if (isLoading) return <Loading />;
  if (error) return <Error />;

  return <UserList data={data} />;
};
```

**💬 Explanation + Insight**

- Caching: Automatic caching of API responses
- Background updates: Updates data in background
- Optimistic updates: Updates UI before server response
- Performance: Reduces unnecessary API calls
- User experience: Better user experience

---

## **Q149. How do you modularize a large React Native project?**

**🧠 Concept**

Large React Native projects are modularized by organizing code into feature-based modules, using monorepos, and implementing proper architecture patterns.

**💻 Example**
```javascript
// Project structure
src/
  features/
    auth/
      components/
      hooks/
      services/
    profile/
      components/
      hooks/
      services/
  shared/
    components/
    hooks/
    utils/
  navigation/
    AppNavigator.js
    AuthNavigator.js
```

**💬 Explanation + Insight**

- Feature modules: Organize by features
- Shared components: Reusable components
- Architecture: Proper architecture patterns
- Scalability: Scale with team size
- Maintenance: Easier maintenance

---

## **Q150. How do you migrate to the new RN architecture (Fabric + TurboModules)?**

**🧠 Concept**

Migration to the new React Native architecture involves enabling Fabric and TurboModules, updating dependencies, and testing for compatibility.

**💻 Example**
```javascript
// metro.config.js
module.exports = {
  resolver: {
    unstable_enablePackageExports: true,
  },
  transformer: {
    unstable_allowRequireContext: true,
  },
};

// react-native.config.js
module.exports = {
  dependencies: {
    'react-native': {
      platforms: {
        android: {
          sourceDir: '../node_modules/react-native/android',
          packageImportPath: 'import io.invertase.firebase.RNFirebasePackage;',
        },
      },
    },
  },
};
```

**💬 Explanation + Insight**

- Fabric: Enable new rendering system
- TurboModules: Enable new module system
- Migration: Gradual migration approach
- Testing: Test for compatibility
- Performance: Better performance

---

## **Q151. How do you handle background sync using Headless JS?**

**🧠 Concept**

Background sync is handled using Headless JS to run JavaScript code in the background when the app is not active.

**💻 Example**
```javascript
import { AppRegistry } from 'react-native';

const BackgroundSync = () => {
  const syncData = async () => {
    try {
      const data = await fetchData();
      await saveToLocalStorage(data);
    } catch (error) {
      console.error('Background sync error:', error);
    }
  };

  syncData();
  return null;
};

AppRegistry.registerComponent('BackgroundSync', () => BackgroundSync);
```

**💬 Explanation + Insight**

- Background tasks: Run tasks in background
- Headless JS: JavaScript in background
- Sync: Sync data when offline
- Performance: Optimize background tasks
- User experience: Seamless experience

---

## **Q152. How do you monitor app performance using Sentry and Flipper?**

**🧠 Concept**

App performance is monitored using Sentry for error tracking and Flipper for debugging to identify and fix performance issues.

**💻 Example**
```javascript
import * as Sentry from '@sentry/react-native';

const MyComponent = () => {
  const trackPerformance = (operation, duration) => {
    Sentry.addBreadcrumb({
      message: `Operation: ${operation}`,
      level: 'info',
      data: { duration },
    });
  };

  const measurePerformance = (operation) => {
    const startTime = performance.now();
    operation();
    const endTime = performance.now();
    trackPerformance(operation.name, endTime - startTime);
  };

  return <View>{/* Component content */}</View>;
};
```

**💬 Explanation + Insight**

- Error tracking: Track errors and crashes
- Performance monitoring: Monitor app performance
- Debugging: Use Flipper for debugging
- Analytics: Get performance analytics
- Optimization: Use data for optimization

---

## **Q153. How do you manage multiple environments using `.env` files?**

**🧠 Concept**

Multiple environments are managed using `.env` files to store environment-specific configuration and variables.

**💻 Example**
```javascript
// .env.development
API_URL=https://api-dev.example.com
DEBUG=true
LOG_LEVEL=debug

// .env.production
API_URL=https://api.example.com
DEBUG=false
LOG_LEVEL=error

// config.js
import Config from 'react-native-config';

const config = {
  apiUrl: Config.API_URL,
  debug: Config.DEBUG === 'true',
  logLevel: Config.LOG_LEVEL,
};

export default config;
```

**💬 Explanation + Insight**

- Environment files: Use .env files
- Configuration: Environment-specific config
- Security: Secure configuration data
- Deployment: Deploy with correct config
- Management: Easy environment management

---

## **Q154. How do you set up CI/CD pipelines for automated testing & deployment?**

**🧠 Concept**

CI/CD pipelines are set up using GitHub Actions, CircleCI, or Bitrise to automate testing, building, and deploying React Native apps.

**💻 Example**
```yaml
# .github/workflows/ci.yml
name: CI/CD Pipeline

on:
  push:
    branches: [main, develop]
  pull_request:
    branches: [main]

jobs:
  test:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v3
      - uses: actions/setup-node@v3
        with:
          node-version: '18'
      - run: npm install
      - run: npm test
      - run: npm run test:coverage

  build:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v3
      - uses: actions/setup-node@v3
        with:
          node-version: '18'
      - run: npm install
      - run: npm run build:android
      - run: npm run build:ios
```

**💬 Explanation + Insight**

- Automation: Automate testing and deployment
- Pipelines: Set up CI/CD pipelines
- Testing: Automated testing
- Building: Automated building
- Deployment: Automated deployment

---

## **Q155. How do you structure scalable folder architecture?**

**🧠 Concept**

Scalable folder architecture is structured by organizing code into logical modules, using proper naming conventions, and implementing clean architecture principles.

**💻 Example**
```javascript
// Folder structure
src/
  components/
    common/
      Button/
        Button.js
        Button.test.js
        Button.styles.js
    features/
      auth/
        LoginForm/
          LoginForm.js
          LoginForm.test.js
          LoginForm.styles.js
  hooks/
    useAuth.js
    useApi.js
  services/
    api.js
    auth.js
  utils/
    helpers.js
    constants.js
  navigation/
    AppNavigator.js
    AuthNavigator.js
```

**💬 Explanation + Insight**

- Organization: Organize code logically
- Scalability: Scale with team size
- Maintenance: Easier maintenance
- Architecture: Clean architecture
- Best practices: Follow best practices

---

## **Q156. How do you optimize cold start and app launch time?**

**🧠 Concept**

Cold start and app launch time are optimized by reducing bundle size, using Hermes, implementing lazy loading, and optimizing native code.

**💻 Example**
```javascript
// Lazy loading
const LazyScreen = React.lazy(() => import('./LazyScreen'));

const App = () => {
  return (
    <Suspense fallback={<Loading />}>
      <LazyScreen />
    </Suspense>
  );
};

// Hermes configuration
module.exports = {
  transformer: {
    hermesParser: true,
  },
};
```

**💬 Explanation + Insight**

- Bundle size: Reduce bundle size
- Hermes: Use Hermes for better performance
- Lazy loading: Load code only when needed
- Optimization: Optimize native code
- Performance: Better overall performance

---

## **Q157. How do you handle large teams and feature-based modularization?**

**🧠 Concept**

Large teams and feature-based modularization are handled by organizing code into feature modules, using monorepos, and implementing proper team workflows.

**💻 Example**
```javascript
// Feature module structure
features/
  auth/
    components/
    hooks/
    services/
    types/
    index.js
  profile/
    components/
    hooks/
    services/
    types/
    index.js

// Team workflow
// 1. Feature branches
// 2. Code reviews
// 3. Automated testing
// 4. Continuous integration
```

**💬 Explanation + Insight**

- Feature modules: Organize by features
- Team workflow: Proper team workflows
- Code reviews: Implement code reviews
- Testing: Automated testing
- Integration: Continuous integration

---

## **Q158. How do you plan an RN migration strategy across versions?**

**🧠 Concept**

RN migration strategy involves planning upgrades, testing compatibility, and implementing gradual migration approaches to minimize risks.

**💻 Example**
```javascript
// Migration plan
// 1. Analyze current version
// 2. Check breaking changes
// 3. Update dependencies
// 4. Test thoroughly
// 5. Deploy gradually

// Migration checklist
const migrationChecklist = [
  'Update React Native version',
  'Update dependencies',
  'Check breaking changes',
  'Update native code',
  'Test on both platforms',
  'Update CI/CD',
  'Deploy to staging',
  'Deploy to production',
];
```

**💬 Explanation + Insight**

- Planning: Plan migration strategy
- Testing: Test thoroughly
- Gradual: Gradual migration approach
- Risk mitigation: Minimize risks
- Documentation: Document migration process

---

## **Q159. How do you measure mobile performance metrics (TTI, TTFB, FPS)?**

**🧠 Concept**

Mobile performance metrics are measured using performance monitoring tools to track TTI (Time to Interactive), TTFB (Time to First Byte), and FPS (Frames Per Second).

**💻 Example**
```javascript
import { Performance } from 'react-native';

const MyComponent = () => {
  const measurePerformance = (operation, name) => {
    const startTime = Performance.now();
    
    operation();
    
    const endTime = Performance.now();
    const duration = endTime - startTime;
    
    // Track metrics
    analytics.track('performance', {
      operation: name,
      duration,
      timestamp: Date.now(),
    });
  };

  return <View>{/* Component content */}</View>;
};
```

**💬 Explanation + Insight**

- Performance metrics: Track performance metrics
- TTI: Time to Interactive
- TTFB: Time to First Byte
- FPS: Frames Per Second
- Optimization: Use data for optimization

---

## **Q160. How do you distribute builds to testers using Firebase App Distribution or TestFlight?**

**🧠 Concept**

Builds are distributed to testers using Firebase App Distribution for Android and TestFlight for iOS to provide easy access to test builds.

**💻 Example**
```javascript
// Firebase App Distribution
import { getApp } from 'firebase/app';
import { getFunctions, httpsCallable } from 'firebase/functions';

const MyComponent = () => {
  const distributeBuild = async () => {
    try {
      const functions = getFunctions();
      const distribute = httpsCallable(functions, 'distributeBuild');
      await distribute({ buildId: 'latest' });
    } catch (error) {
      console.error('Distribution error:', error);
    }
  };

  return <View>{/* Component content */}</View>;
};
```

**💬 Explanation + Insight**

- Distribution: Distribute builds to testers
- Firebase: Use Firebase App Distribution
- TestFlight: Use TestFlight for iOS
- Testing: Easy access to test builds
- Feedback: Collect tester feedback

---

*This section covers push notifications (FCM, APNs), biometric authentication, offline-first apps, feature flags, dark mode, Maps/Camera/Payment SDKs, skeleton loaders, React Query caching, project modularization, Fabric migration, background sync, performance monitoring, environment management, CI/CD pipelines, folder architecture, and mobile performance metrics.*
