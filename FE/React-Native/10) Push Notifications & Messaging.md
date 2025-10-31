# 📳 10. Push Notifications & Messaging (Q91–95)

---

## 91) What is the difference between **local** and **push** notifications in React Native?

Concept:
Local notifications are scheduled by the app, while push notifications are sent from a server.

Example:
```jsx
import PushNotification from 'react-native-push-notification';

// Local notification
const scheduleLocalNotification = () => {
  PushNotification.localNotification({
    title: 'Local Notification',
```

Deep Insight:
- **Local Notifications**: Scheduled by the app, work offline
- **Push Notifications**: Sent from server, require internet
- **Use Cases**: Local for reminders, push for real-time updates
- **Platform Support**: Both work on iOS and Android
- **User Control**: Users can disable both types

---

## 92) How do you implement push notifications with **FCM (Android)** and **APNs (iOS)**?

Concept:
Configure FCM for Android and APNs for iOS, then handle notification registration and display.

Example:
```jsx
import messaging from '@react-native-firebase/messaging';
import { PermissionsAndroid, Platform } from 'react-native';

// Request permission
const requestPermission = async () => {
  if (Platform.OS === 'android') {
```

Deep Insight:
- **FCM**: Firebase Cloud Messaging for Android
- **APNs**: Apple Push Notification service for iOS
- **Token Management**: Get and manage FCM tokens
- **Permission Handling**: Request notification permissions
- **Platform Differences**: Different setup for iOS and Android

---

## 93) How do you handle **background** and **foreground** notifications differently?

Concept:
Use different notification handlers and display methods based on app state.

Example:
```jsx
import messaging from '@react-native-firebase/messaging';
import { AppState } from 'react-native';

function NotificationHandler() {
  const [appState, setAppState] = useState(AppState.currentState);
  
```

Deep Insight:
- **Foreground**: App is active, show custom UI
- **Background**: App is not active, use system notifications
- **Different Handling**: Different logic for each state
- **User Experience**: Provide appropriate experience for each state
- **Data Processing**: Handle notification data differently

---

## 94) How do you configure permissions and channels for notifications?

Concept:
Request notification permissions and configure notification channels for Android.

Example:
```jsx
import { PermissionsAndroid, Platform } from 'react-native';
import PushNotification from 'react-native-push-notification';

// Configure notification channels for Android
const configureNotificationChannels = () => {
  if (Platform.OS === 'android') {
```

Deep Insight:
- **Android Channels**: Configure notification channels for Android
- **Permission Requests**: Request notification permissions
- **Platform Differences**: Different approaches for iOS and Android
- **User Control**: Users can control notification settings
- **Channel Importance**: Set appropriate importance levels

---

## 95) What are best practices for testing and securing push notification payloads?

Concept:
Use proper payload validation, testing strategies, and security measures for push notifications.

Example:
```jsx
// Secure notification payload validation
const validateNotificationPayload = (payload) => {
  const requiredFields = ['title', 'body', 'data'];
  
  // Check required fields
  for (const field of requiredFields) {
```

Deep Insight:
- **Payload Validation**: Validate notification payloads
- **Security**: Secure notification data and endpoints
- **Testing**: Test notification handling thoroughly
- **Error Handling**: Handle invalid payloads gracefully
- **Data Sanitization**: Sanitize notification data

---
