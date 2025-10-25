# ⚛️ React Native Interview Notes (2025 Edition)

## 🔒 Section 5 — Security, Stability & Error Monitoring — Q111-Q125

---

## **Q111. How do you handle crashes in React Native?**

**🧠 Concept**

Crashes in React Native are handled using Error Boundaries, crash reporting tools, and proper error handling to prevent app crashes and provide better user experience.

**💻 Example**
```javascript
import crashlytics from '@react-native-firebase/crashlytics';

const MyComponent = () => {
  const handleError = (error) => {
    crashlytics().recordError(error);
    console.error('Error occurred:', error);
  };

  const performOperation = async () => {
    try {
      await riskyOperation();
    } catch (error) {
      handleError(error);
    }
  };

  return <View>{/* Component content */}</View>;
};
```

**💬 Explanation + Insight**

- Error Boundaries: Catch JavaScript errors in components
- Crash reporting: Use tools like Crashlytics or Sentry
- Error handling: Implement proper try-catch blocks
- User experience: Provide fallback UI for errors
- Monitoring: Monitor crashes in production

---

## **Q112. What are Error Boundaries in React Native?**

**🧠 Concept**

Error Boundaries are React components that catch JavaScript errors anywhere in the component tree and display a fallback UI instead of crashing the app.

**💻 Example**
```javascript
class ErrorBoundary extends React.Component {
  constructor(props) {
    super(props);
    this.state = { hasError: false };
  }

  static getDerivedStateFromError(error) {
    return { hasError: true };
  }

  componentDidCatch(error, errorInfo) {
    console.error('Error caught by boundary:', error, errorInfo);
  }

  render() {
    if (this.state.hasError) {
      return <Text>Something went wrong.</Text>;
    }

    return this.props.children;
  }
}
```

**💬 Explanation + Insight**

- Error catching: Catches JavaScript errors in components
- Fallback UI: Shows fallback UI instead of crashing
- Error logging: Logs errors for debugging
- User experience: Prevents app crashes
- Recovery: Allows app to continue functioning

---

## **Q113. How do you integrate Sentry for error monitoring?**

**🧠 Concept**

Sentry is integrated for error monitoring by installing the SDK, configuring it, and using it to track errors, crashes, and performance issues.

**💻 Example**
```javascript
import * as Sentry from '@sentry/react-native';

Sentry.init({
  dsn: 'YOUR_DSN_HERE',
  environment: __DEV__ ? 'development' : 'production',
});

const MyComponent = () => {
  const handleError = (error) => {
    Sentry.captureException(error);
  };

  return <View>{/* Component content */}</View>;
};
```

**💬 Explanation + Insight**

- Error tracking: Tracks errors and crashes
- Performance monitoring: Monitors app performance
- User context: Provides user context for errors
- Release tracking: Tracks app releases
- Real-time: Real-time error monitoring

---

## **Q114. How do you integrate Crashlytics for crash reporting?**

**🧠 Concept**

Crashlytics is integrated for crash reporting by installing Firebase Crashlytics, configuring it, and using it to track crashes and errors.

**💻 Example**
```javascript
import crashlytics from '@react-native-firebase/crashlytics';

const MyComponent = () => {
  const handleError = (error) => {
    crashlytics().recordError(error);
  };

  const setUser = (userId) => {
    crashlytics().setUserId(userId);
  };

  return <View>{/* Component content */}</View>;
};
```

**💬 Explanation + Insight**

- Crash reporting: Reports crashes and errors
- User identification: Identifies users in crash reports
- Custom logs: Adds custom logs to crash reports
- Real-time: Real-time crash reporting
- Analytics: Provides crash analytics

---

## **Q115. How do you prevent ANRs (Application Not Responding) in React Native?**

**🧠 Concept**

ANRs are prevented by avoiding long-running operations on the main thread, using background threads, and optimizing performance.

**💻 Example**
```javascript
import { InteractionManager } from 'react-native';

const MyComponent = () => {
  const [data, setData] = useState([]);

  useEffect(() => {
    InteractionManager.runAfterInteractions(() => {
      // Heavy operation after interactions complete
      processLargeData();
    });
  }, []);

  return <View>{/* Component content */}</View>;
};
```

**💬 Explanation + Insight**

- Main thread: Avoid blocking the main thread
- Background threads: Use background threads for heavy operations
- InteractionManager: Use InteractionManager for timing
- Performance: Optimize performance to prevent ANRs
- User experience: Maintain responsive UI

---

## **Q116. How do you implement Keychain security in React Native?**

**🧠 Concept**

Keychain security is implemented using react-native-keychain to securely store sensitive data like passwords, tokens, and keys.

**💻 Example**
```javascript
import Keychain from 'react-native-keychain';

const MyComponent = () => {
  const storeCredentials = async (username, password) => {
    try {
      await Keychain.setInternetCredentials('myapp', username, password);
    } catch (error) {
      console.error('Error storing credentials:', error);
    }
  };

  const getCredentials = async () => {
    try {
      const credentials = await Keychain.getInternetCredentials('myapp');
      return credentials;
    } catch (error) {
      console.error('Error getting credentials:', error);
    }
  };

  return <View>{/* Component content */}</View>;
};
```

**💬 Explanation + Insight**

- Secure storage: Securely stores sensitive data
- Encryption: Encrypts data at rest
- Biometric: Supports biometric authentication
- Cross-platform: Works on both iOS and Android
- Security: Provides enterprise-grade security

---

## **Q117. How do you implement SSL pinning in React Native?**

**🧠 Concept**

SSL pinning is implemented to prevent man-in-the-middle attacks by validating server certificates and ensuring secure communication.

**💻 Example**
```javascript
import { SSL } from 'react-native-ssl-pinning';

const MyComponent = () => {
  const makeSecureRequest = async () => {
    try {
      const response = await SSL.fetch('https://api.example.com/data', {
        method: 'GET',
        timeout: 30,
        sslPinning: {
          certs: ['certificate1', 'certificate2'],
        },
      });
      return response;
    } catch (error) {
      console.error('SSL pinning error:', error);
    }
  };

  return <View>{/* Component content */}</View>;
};
```

**💬 Explanation + Insight**

- Certificate validation: Validates server certificates
- Security: Prevents man-in-the-middle attacks
- Trust: Ensures communication with trusted servers
- Configuration: Configure certificate pinning
- Monitoring: Monitor SSL pinning failures

---

## **Q118. How do you protect environment variables in React Native?**

**🧠 Concept**

Environment variables are protected by using secure storage, obfuscation, and proper configuration management to prevent sensitive data exposure.

**💻 Example**
```javascript
import Config from 'react-native-config';

const MyComponent = () => {
  const [config, setConfig] = useState({});

  useEffect(() => {
    // Load configuration securely
    setConfig({
      apiUrl: Config.API_URL,
      apiKey: Config.API_KEY,
    });
  }, []);

  return <View>{/* Component content */}</View>;
};
```

**💬 Explanation + Insight**

- Secure storage: Store sensitive data securely
- Obfuscation: Obfuscate sensitive data
- Configuration: Use proper configuration management
- Environment: Separate development and production configs
- Security: Protect sensitive information

---

## **Q119. How do you implement jailbreak detection in React Native?**

**🧠 Concept**

Jailbreak detection is implemented to detect if a device is jailbroken and take appropriate security measures.

**💻 Example**
```javascript
import JailMonkey from 'jail-monkey';

const MyComponent = () => {
  const [isJailbroken, setIsJailbroken] = useState(false);

  useEffect(() => {
    const checkJailbreak = () => {
      if (JailMonkey.isJailBroken()) {
        setIsJailbroken(true);
        // Take security measures
        handleJailbrokenDevice();
      }
    };

    checkJailbreak();
  }, []);

  const handleJailbrokenDevice = () => {
    // Implement security measures
    console.log('Device is jailbroken');
  };

  return <View>{/* Component content */}</View>;
};
```

**💬 Explanation + Insight**

- Device security: Detects compromised devices
- Security measures: Implement appropriate security measures
- User experience: Handle jailbroken devices gracefully
- Monitoring: Monitor jailbreak detection
- Compliance: Ensure compliance with security policies

---

## **Q120. How do you implement data encryption in React Native?**

**🧠 Concept**

Data encryption is implemented using encryption libraries to encrypt sensitive data before storing or transmitting it.

**💻 Example**
```javascript
import CryptoJS from 'crypto-js';

const MyComponent = () => {
  const encryptData = (data, key) => {
    const encrypted = CryptoJS.AES.encrypt(JSON.stringify(data), key).toString();
    return encrypted;
  };

  const decryptData = (encryptedData, key) => {
    const decrypted = CryptoJS.AES.decrypt(encryptedData, key);
    return JSON.parse(decrypted.toString(CryptoJS.enc.Utf8));
  };

  return <View>{/* Component content */}</View>;
};
```

**💬 Explanation + Insight**

- Data protection: Protects sensitive data
- Encryption: Uses strong encryption algorithms
- Key management: Manages encryption keys securely
- Performance: Consider encryption performance impact
- Security: Ensures data security

---

## **Q121. How do you implement secure OTA updates in React Native?**

**🧠 Concept**

Secure OTA updates are implemented by validating update signatures, using secure channels, and implementing proper update mechanisms.

**💻 Example**
```javascript
import CodePush from 'react-native-code-push';

const MyComponent = () => {
  const [updateAvailable, setUpdateAvailable] = useState(false);

  useEffect(() => {
    const checkForUpdates = async () => {
      try {
        const update = await CodePush.checkForUpdate();
        if (update) {
          setUpdateAvailable(true);
        }
      } catch (error) {
        console.error('Error checking for updates:', error);
      }
    };

    checkForUpdates();
  }, []);

  const installUpdate = async () => {
    try {
      await CodePush.sync();
    } catch (error) {
      console.error('Error installing update:', error);
    }
  };

  return <View>{/* Component content */}</View>;
};
```

**💬 Explanation + Insight**

- Update validation: Validates update signatures
- Secure channels: Uses secure communication channels
- Rollback: Implements rollback mechanisms
- User experience: Provides smooth update experience
- Security: Ensures update security

---

## **Q122. How do you implement GDPR compliance in React Native?**

**🧠 Concept**

GDPR compliance is implemented by implementing data protection measures, user consent management, and privacy controls.

**💻 Example**
```javascript
const MyComponent = () => {
  const [consent, setConsent] = useState(false);

  const handleConsent = (accepted) => {
    setConsent(accepted);
    if (accepted) {
      // Enable data collection
      enableAnalytics();
    } else {
      // Disable data collection
      disableAnalytics();
    }
  };

  const requestDataDeletion = () => {
    // Implement data deletion
    deleteUserData();
  };

  return <View>{/* Component content */}</View>;
};
```

**💬 Explanation + Insight**

- Data protection: Implements data protection measures
- User consent: Manages user consent
- Privacy controls: Provides privacy controls
- Data deletion: Implements data deletion
- Compliance: Ensures GDPR compliance

---

## **Q123. How do you implement CCPA compliance in React Native?**

**🧠 Concept**

CCPA compliance is implemented by implementing privacy controls, data transparency, and user rights management.

**💻 Example**
```javascript
const MyComponent = () => {
  const [privacySettings, setPrivacySettings] = useState({});

  const handlePrivacySettings = (settings) => {
    setPrivacySettings(settings);
    // Update privacy settings
    updatePrivacySettings(settings);
  };

  const requestDataAccess = () => {
    // Implement data access request
    provideUserData();
  };

  return <View>{/* Component content */}</View>;
};
```

**💬 Explanation + Insight**

- Privacy controls: Implements privacy controls
- Data transparency: Provides data transparency
- User rights: Manages user rights
- Data access: Implements data access requests
- Compliance: Ensures CCPA compliance

---

## **Q124. How do you implement secure logout in React Native?**

**🧠 Concept**

Secure logout is implemented by clearing sensitive data, invalidating tokens, and ensuring proper session termination.

**💻 Example**
```javascript
const MyComponent = () => {
  const handleLogout = async () => {
    try {
      // Clear sensitive data
      await AsyncStorage.removeItem('authToken');
      await AsyncStorage.removeItem('userData');
      
      // Invalidate tokens
      await invalidateTokens();
      
      // Clear secure storage
      await Keychain.resetInternetCredentials('myapp');
      
      // Navigate to login
      navigation.navigate('Login');
    } catch (error) {
      console.error('Error during logout:', error);
    }
  };

  return <View>{/* Component content */}</View>;
};
```

**💬 Explanation + Insight**

- Data clearing: Clears sensitive data
- Token invalidation: Invalidates authentication tokens
- Session termination: Properly terminates sessions
- Security: Ensures secure logout
- User experience: Provides smooth logout experience

---

## **Q125. How do you implement biometric authentication in React Native?**

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

*This section covers crash handling, Error Boundaries, Sentry/Crashlytics integration, ANRs prevention, Keychain/Keystore security, SSL pinning, environment variables protection, jailbreak detection, data encryption, OTA updates security, GDPR/CCPA compliance, and secure logout.*
