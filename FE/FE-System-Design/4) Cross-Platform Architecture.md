# 4. Cross-Platform Architecture (Q38–47)

---

## Q38. How would you design a responsive, mobile-first web app?

Mobile-first design starts with the smallest screen size and progressively enhances for larger screens, using flexible layouts, touch-friendly interfaces, and performance optimization - test across different devices and screen sizes. Start with mobile constraints and progressively enhance.

- **Trade-offs**: The catch is use flexible grid systems and responsive units - optimize touch targets and interaction patterns. Test across different devices and screen sizes, but watch out - consider performance implications of responsive design.

Example:

```javascript
const ResponsiveApp = () => {
  const [isMobile, setIsMobile] = useState(false);
  
  useEffect(() => {
    const checkScreenSize = () => setIsMobile(window.innerWidth < 768);
    checkScreenSize();
    window.addEventListener('resize', checkScreenSize);
    return () => window.removeEventListener('resize', checkScreenSize);
  }, []);
  
  return (
    <div className="app">
      <Header isMobile={isMobile} />
      <main className={isMobile ? 'mobile-layout' : 'desktop-layout'}>
        <ContentArea />
      </main>
    </div>
  );
};
```

---

## Q39. What's the difference between responsive, adaptive, and fluid layouts?

Responsive layouts use flexible units and media queries, adaptive layouts serve different layouts for different screen sizes, and fluid layouts use relative units for smooth scaling - responsive is most common, adaptive for complex UIs. Responsive (flexible, single layout that adapts), Adaptive (multiple layouts for different screen sizes), Fluid (relative units for smooth scaling).

- **Trade-offs**: The catch is choose based on design requirements and complexity - consider maintenance and performance implications. Responsive is most common, adaptive for complex UIs, but watch out - mix approaches for different parts of the app.

Example:

```javascript
// Responsive layout with media queries
const ResponsiveLayout = () => (
  <div className="responsive-container">
    <div className="item">Item 1</div>
    <div className="item">Item 2</div>
  </div>
);

// Adaptive layout with different components
const AdaptiveLayout = ({ screenSize }) => {
  if (screenSize === 'mobile') return <MobileLayout />;
  if (screenSize === 'tablet') return <TabletLayout />;
  return <DesktopLayout />;
};
```

---

## Q40. How do you share code between web and mobile platforms?

Code sharing between web and mobile platforms can be achieved through shared business logic, common utilities, and cross-platform frameworks while maintaining platform-specific UI - implement proper abstraction layers. Share business logic and utilities across platforms.

- **Trade-offs**: The catch is keep UI components platform-specific - use monorepos for code organization. Implement proper abstraction layers, but watch out - consider cross-platform frameworks (React Native, Flutter).

Example:

```javascript
// Shared business logic
export const UserService = {
  async getUser(id) {
    const response = await fetch(`/api/users/${id}`);
    return response.json();
  },
  async updateUser(id, data) {
    const response = await fetch(`/api/users/${id}`, {
      method: 'PUT',
      body: JSON.stringify(data)
    });
    return response.json();
  }
};

// Shared utilities
export const ValidationUtils = {
  isValidEmail: (email) => /^[^\s@]+@[^\s@]+\.[^\s@]+$/.test(email),
  formatCurrency: (amount) => `$${amount.toFixed(2)}`
};
```

---

## Q41. What are PWAs and how do you make a web app installable and offline-first?

Progressive Web Apps (PWAs) are web applications that provide native app-like experiences through service workers, web app manifests, and offline functionality - PWAs bridge web and native app experiences. Implement service workers for offline functionality, create web app manifest for installability.

- **Trade-offs**: The catch is use responsive design and touch-friendly interfaces - implement push notifications and background sync. PWAs bridge web and native app experiences, but watch out - test across different browsers and devices.

Example:

```javascript
// Web App Manifest
const manifest = {
  "name": "My PWA App",
  "short_name": "PWA App",
  "start_url": "/",
  "display": "standalone",
  "icons": [
    { "src": "/icons/icon-192x192.png", "sizes": "192x192" },
    { "src": "/icons/icon-512x512.png", "sizes": "512x512" }
  ]
};

// Service Worker for offline functionality
self.addEventListener('install', (event) => {
  event.waitUntil(
    caches.open('v1').then((cache) => {
      return cache.addAll(['/', '/static/js/bundle.js', '/static/css/main.css']);
    })
  );
});
```

---

## Q42. How do you use service workers for offline caching and background sync?

Service workers enable offline functionality through caching strategies, background sync for data synchronization, and push notifications for user engagement - test offline functionality thoroughly. Implement different caching strategies for different content types.

- **Trade-offs**: The catch is use background sync for offline data synchronization - handle push notifications and user engagement. Test offline functionality thoroughly, but watch out - consider cache invalidation and update strategies.

Example:

```javascript
self.addEventListener('fetch', (event) => {
  const { request } = event;
  const url = new URL(request.url);
  
  if (url.pathname.startsWith('/api/')) {
    event.respondWith(networkFirst(request));
  } else if (url.pathname.startsWith('/static/')) {
    event.respondWith(cacheFirst(request));
  } else {
    event.respondWith(staleWhileRevalidate(request));
  }
});

// Background sync
self.addEventListener('sync', (event) => {
  if (event.tag === 'background-sync') {
    event.waitUntil(doBackgroundSync());
  }
});
```

---

## Q43. How would you structure a project that supports web, mobile (React Native), and desktop (Electron)?

Multi-platform projects require shared business logic, platform-specific UI layers, and proper build configurations for each target platform - consider platform-specific features and limitations. Share business logic and utilities across platforms.

- **Trade-offs**: The catch is keep UI components platform-specific - use monorepos for code organization. Consider platform-specific features and limitations, but watch out - implement proper build configurations.

Example:

```javascript
// Project structure
/*
src/
  shared/
    services/api.js
    utils/validation.js
  web/
    components/
    App.js
  mobile/
    components/
    App.js
  desktop/
    main.js
    renderer/App.js
*/

// Shared API service
export const ApiService = {
  baseURL: process.env.REACT_APP_API_URL,
  async request(endpoint, options = {}) {
    const response = await fetch(`${this.baseURL}${endpoint}`, options);
    if (!response.ok) throw new Error(`API Error: ${response.status}`);
    return response.json();
  }
};
```

---

## Q44. What is the difference between React Native, Flutter, and Cordova?

These are different approaches to cross-platform mobile development: React Native uses native components, Flutter uses its own rendering engine, and Cordova wraps web apps in native containers - each has different trade-offs. React Native (JavaScript, native performance, large ecosystem), Flutter (Dart, consistent UI, fast development), Cordova (Web technologies, easy migration, limited performance).

- **Trade-offs**: The catch is choose based on team expertise and performance requirements - consider long-term maintenance and community support. Each has different trade-offs, but watch out - evaluate based on project requirements.

Example:

```javascript
// React Native - JavaScript with native components
import { View, Text, TouchableOpacity } from 'react-native';

const ReactNativeComponent = () => (
  <View style={styles.container}>
    <Text>Hello React Native</Text>
    <TouchableOpacity><Text>Press me</Text></TouchableOpacity>
  </View>
);

// Cordova - Web technologies in native container
const CordovaApp = () => (
  <div className="app">
    <h1>Hello Cordova</h1>
    <button onClick={() => navigator.camera.getPicture()}>Take Picture</button>
  </div>
);
```

---

## Q45. How do React Native and Flutter handle rendering differently?

React Native uses native components and bridges to communicate with native code, while Flutter uses its own rendering engine and widgets that compile to native code - Flutter has more consistent rendering, RN uses native components. React Native (bridge-based communication, native components), Flutter (direct compilation, custom rendering engine).

- **Trade-offs**: The catch is performance implications of different approaches - development experience and debugging differences. Flutter has more consistent rendering, RN uses native components, but watch out - consider platform-specific optimizations.

Example:

```javascript
// React Native - Bridge communication
const ReactNativeView = () => {
  const [data, setData] = useState(null);
  
  useEffect(() => {
    NativeModules.DataManager.getData((result) => {
      setData(result);
    });
  }, []);
  
  return <View><Text>{data}</Text></View>;
};
```

---

## Q46. What are the performance and ecosystem trade-offs between RN, Flutter, and hybrid apps?

Each approach has different performance characteristics, ecosystem maturity, and development trade-offs that should be considered based on project requirements - performance vs development speed trade-off. React Native (good balance of performance and ecosystem), Flutter (excellent performance, growing ecosystem), Cordova (easy development, limited performance).

- **Trade-offs**: The catch is consider team expertise and project timeline - evaluate long-term maintenance and updates. Performance vs development speed trade-off, but watch out - choose based on specific project needs.

Example:

```javascript
const performanceMetrics = {
  reactNative: {
    startupTime: 'Medium',
    memoryUsage: 'Medium',
    nativePerformance: 'High',
    bundleSize: 'Medium'
  },
  flutter: {
    startupTime: 'Fast',
    memoryUsage: 'Low',
    nativePerformance: 'High',
    bundleSize: 'Large'
  },
  cordova: {
    startupTime: 'Slow',
    memoryUsage: 'High',
    nativePerformance: 'Low',
    bundleSize: 'Small'
  }
};
```

---

## Q47. When would you choose web, hybrid, or native for a new product?

Platform choice depends on target audience, performance requirements, development resources, and long-term maintenance considerations - start with web, add native when needed. Web (best for content and information apps), Hybrid (good for apps needing some native features), Native (best for performance-critical and feature-rich apps).

- **Trade-offs**: The catch is consider target audience and device capabilities - evaluate development resources and timeline. Start with web, add native when needed, but watch out - consider hybrid approach for MVP, native for scale.

Example:

```javascript
const platformDecisionMatrix = {
  web: {
    when: ['Cross-platform reach is critical', 'Rapid prototyping'],
    pros: ['Single codebase', 'Easy deployment', 'No app store approval'],
    cons: ['Limited native features', 'Performance constraints']
  },
  hybrid: {
    when: ['Need some native features', 'Existing web application'],
    pros: ['Access to native APIs', 'Reuse existing web code'],
    cons: ['Performance overhead', 'Limited native UI customization']
  },
  native: {
    when: ['Performance is critical', 'Complex native features required'],
    pros: ['Best performance', 'Full access to platform features'],
    cons: ['Separate codebases', 'Higher development cost']
  }
};
```

---
