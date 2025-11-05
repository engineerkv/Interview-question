# 📳 10. Push Notifications & Messaging (Q91–95)

---

## 91) What is the difference between **local** and **push** notifications in React Native?

Local notifications are scheduled by the app, while push notifications are sent from a server.

```jsx
import PushNotification from 'react-native-push-notification';

// Local notification
const scheduleLocalNotification = () => {
  PushNotification.localNotification({
    title: 'Local Notification',
    message: 'This is a local notification',
    date: new Date(Date.now() + 60000) // 1 minute from now
  });
};

// Push notification - handled by server
```

- **Core Difference**: Local notifications (scheduled by the app, work offline), Push notifications (sent from server, require internet)
- **Real-World Use Cases**: Local for reminders, push for real-time updates
- **Common Advantage**: Both work on iOS and Android (platform support)
- **Advanced Feature**: Users can disable both types (user control)
- **Interview Tip**: Explain that choose based on use case

---

## 92) How do you implement push notifications with **FCM (Android)** and **APNs (iOS)**?

Configure FCM for Android and APNs for iOS, then handle notification registration and display.

```jsx
import messaging from '@react-native-firebase/messaging';
import { PermissionsAndroid, Platform } from 'react-native';

const requestPermission = async () => {
  if (Platform.OS === 'android') {
    const granted = await PermissionsAndroid.request(
      PermissionsAndroid.PERMISSIONS.POST_NOTIFICATIONS
    );
    return granted === PermissionsAndroid.RESULTS.GRANTED;
  } else {
    const authStatus = await messaging().requestPermission();
    return authStatus === messaging.AuthorizationStatus.AUTHORIZED;
  }
};

const getToken = async () => {
  const token = await messaging().getToken();
  return token;
};
```

- **Core Services**: FCM (Firebase Cloud Messaging for Android), APNs (Apple Push Notification service for iOS)
- **Real-World Use**: Get and manage FCM tokens (token management)
- **Common Practice**: Request notification permissions (permission handling)
- **Advanced Feature**: Different setup for iOS and Android (platform differences)
- **Interview Tip**: Explain that configure both services for cross-platform support

---

## 93) How do you handle **background** and **foreground** notifications differently?

Use different notification handlers and display methods based on app state.

```jsx
import messaging from '@react-native-firebase/messaging';
import { AppState } from 'react-native';

function NotificationHandler() {
  const [appState, setAppState] = useState(AppState.currentState);
  
  useEffect(() => {
    const unsubscribe = AppState.addEventListener('change', setAppState);
    
    // Foreground notification handler
    const unsubscribeForeground = messaging().onMessage(async remoteMessage => {
      if (appState === 'active') {
        // Show custom notification UI
        console.log('Foreground notification:', remoteMessage);
      }
    });
    
    // Background notification handler
    messaging().setBackgroundMessageHandler(async remoteMessage => {
      console.log('Background notification:', remoteMessage);
    });
    
    return () => {
      unsubscribe();
      unsubscribeForeground();
    };
  }, [appState]);
}
```

- **Core Difference**: Foreground (app is active, show custom UI), Background (app is not active, use system notifications)
- **Real-World Use**: Different logic for each state (different handling)
- **Common Practice**: Provide appropriate experience for each state (user experience)
- **Advanced Feature**: Handle notification data differently (data processing)
- **Interview Tip**: Explain that handle both states for best UX

---

## 94) How do you configure permissions and channels for notifications?

Request notification permissions and configure notification channels for Android.

```jsx
import { PermissionsAndroid, Platform } from 'react-native';
import PushNotification from 'react-native-push-notification';

const configureNotificationChannels = () => {
  if (Platform.OS === 'android') {
    PushNotification.createChannel(
      {
        channelId: 'default-channel',
        channelName: 'Default Channel',
        channelDescription: 'Default notification channel',
        importance: 4, // High importance
        vibrate: true
      },
      created => console.log(`Channel created: ${created}`)
    );
  }
};
```

- **Core Configuration**: Configure notification channels for Android (Android channels)
- **Real-World Use**: Request notification permissions (permission requests)
- **Common Practice**: Different approaches for iOS and Android (platform differences)
- **Advanced Feature**: Users can control notification settings (user control)
- **Interview Tip**: Explain that set appropriate importance levels (channel importance)

---

## 95) What are best practices for testing and securing push notification payloads?

Use proper payload validation, testing strategies, and security measures for push notifications.

```jsx
const validateNotificationPayload = (payload) => {
  const requiredFields = ['title', 'body', 'data'];
  
  for (const field of requiredFields) {
    if (!payload[field]) {
      throw new Error(`Missing required field: ${field}`);
    }
  }
  
  // Validate data types
  if (typeof payload.title !== 'string') {
    throw new Error('Title must be a string');
  }
  
  return true;
};
```

- **Core Practice**: Validate notification payloads (payload validation)
- **Real-World Security**: Secure notification data and endpoints (security)
- **Common Practice**: Test notification handling thoroughly (testing)
- **Advanced Feature**: Handle invalid payloads gracefully (error handling)
- **Interview Tip**: Explain that sanitize notification data (data sanitization)

---
