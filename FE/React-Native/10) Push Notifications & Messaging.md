<div align="center">

**[← Previous: Build, Deployment & Stores](9%29%20Build%2C%20Deployment%20%26%20Stores.md)** | **[Next: Question List →](question.md)**

</div>

# 10. Push Notifications & Messaging (Q91–95)

---

## Q91. Difference between local and push notifications

Local notifications are scheduled by the app, while push notifications are sent from a server - choose based on use case. Local notifications (scheduled by the app, work offline), Push notifications (sent from server, require internet).

- **Trade-offs**: The catch is both work on iOS and Android (platform support) - users can disable both types (user control). Choose based on use case, but watch out - local for reminders, push for real-time updates.

Example:

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

---

## Q92. Implementing Firebase Cloud Messaging (FCM) for Android

Configure FCM for Android and APNs for iOS, then handle notification registration and display - configure both services for cross-platform support. FCM (Firebase Cloud Messaging for Android), APNs (Apple Push Notification service for iOS).

- **Trade-offs**: The catch is request notification permissions (permission handling) - different setup for iOS and Android (platform differences). Configure both services for cross-platform support, but watch out - get and manage FCM tokens (token management).

Example:

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

---

## Q93. Implementing Apple Push Notification service (APNs) for iOS

Use different notification handlers and display methods based on app state - handle both states for best UX. Foreground (app is active, show custom UI), Background (app is not active, use system notifications).

- **Trade-offs**: The catch is provide appropriate experience for each state (user experience) - handle notification data differently (data processing). Handle both states for best UX, but watch out - different logic for each state (different handling).

Example:

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

---

## Q94. Handling background and foreground notifications

Request notification permissions and configure notification channels for Android - set appropriate importance levels (channel importance). Configure notification channels for Android (Android channels).

- **Trade-offs**: The catch is different approaches for iOS and Android (platform differences) - users can control notification settings (user control). Set appropriate importance levels (channel importance), but watch out - request notification permissions (permission requests).

Example:

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

---

## Q95. Managing notification permissions and channels

Use proper payload validation, testing strategies, and security measures for push notifications - sanitize notification data (data sanitization). Validate notification payloads (payload validation).

- **Trade-offs**: The catch is test notification handling thoroughly (testing) - handle invalid payloads gracefully (error handling). Sanitize notification data (data sanitization), but watch out - secure notification data and endpoints (security).

Example:

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

---

---
