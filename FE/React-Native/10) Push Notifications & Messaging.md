# 📳 10. Push Notifications & Messaging (Q91–95)

---

## 🧩 Q91. What is the difference between local and push notifications?

### 🧠 Concept

Local notifications are scheduled by the app, while push notifications are sent from a server. Choose based on use case.

---

### 💡 Example

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

### 🔍 Deep Insights

* **Rule:** Local notifications (scheduled by the app, work offline), Push notifications (sent from server, require internet).
* **Use Case:** Local for reminders, push for real-time updates.
* **Common Mistake:** Both work on iOS and Android (platform support).
* **Pro Tip:** Users can disable both types (user control).

---

### ⭐ Senior Takeaway

Choose based on use case.

---

## 🧩 Q92. How do you implement push notifications with FCM (Android) and APNs (iOS)?

### 🧠 Concept

Configure FCM for Android and APNs for iOS, then handle notification registration and display. Configure both services for cross-platform support.

---

### 💡 Example

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

### 🔍 Deep Insights

* **Rule:** FCM (Firebase Cloud Messaging for Android), APNs (Apple Push Notification service for iOS).
* **Use Case:** Get and manage FCM tokens (token management).
* **Common Mistake:** Request notification permissions (permission handling).
* **Pro Tip:** Different setup for iOS and Android (platform differences).

---

### ⭐ Senior Takeaway

Configure both services for cross-platform support.

---

## 🧩 Q93. How do you handle background and foreground notifications differently?

### 🧠 Concept

Use different notification handlers and display methods based on app state. Handle both states for best UX.

---

### 💡 Example

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

### 🔍 Deep Insights

* **Rule:** Foreground (app is active, show custom UI), Background (app is not active, use system notifications).
* **Use Case:** Different logic for each state (different handling).
* **Common Mistake:** Provide appropriate experience for each state (user experience).
* **Pro Tip:** Handle notification data differently (data processing).

---

### ⭐ Senior Takeaway

Handle both states for best UX.

---

## 🧩 Q94. How do you configure permissions and channels for notifications?

### 🧠 Concept

Request notification permissions and configure notification channels for Android. Set appropriate importance levels (channel importance).

---

### 💡 Example

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

### 🔍 Deep Insights

* **Rule:** Configure notification channels for Android (Android channels).
* **Use Case:** Request notification permissions (permission requests).
* **Common Mistake:** Different approaches for iOS and Android (platform differences).
* **Pro Tip:** Users can control notification settings (user control).

---

### ⭐ Senior Takeaway

Set appropriate importance levels (channel importance).

---

## 🧩 Q95. What are best practices for testing and securing push notification payloads?

### 🧠 Concept

Use proper payload validation, testing strategies, and security measures for push notifications. Sanitize notification data (data sanitization).

---

### 💡 Example

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

### 🔍 Deep Insights

* **Rule:** Validate notification payloads (payload validation).
* **Use Case:** Secure notification data and endpoints (security).
* **Common Mistake:** Test notification handling thoroughly (testing).
* **Pro Tip:** Handle invalid payloads gracefully (error handling).

---

### ⭐ Senior Takeaway

Sanitize notification data (data sanitization).

---
