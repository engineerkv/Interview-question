# 4) Cross-Platform Architecture (Q34–43)

---

## 34) How would you design a responsive, mobile-first web app?

Mobile-first design starts with the smallest screen size and progressively enhances for larger screens, using flexible layouts, touch-friendly interfaces, and performance optimization.

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

- **Core Principle**: Start with mobile constraints and progressively enhance
- **Real-World Use**: Use flexible grid systems and responsive units
- **Common Practice**: Optimize touch targets and interaction patterns
- **Advanced Consideration**: Consider performance implications of responsive design
- **Interview Tip**: Explain that test across different devices and screen sizes

---

## 35) What's the difference between responsive, adaptive, and fluid layouts?

Responsive layouts use flexible units and media queries, adaptive layouts serve different layouts for different screen sizes, and fluid layouts use relative units for smooth scaling.

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

- **Core Differences**: Responsive (flexible, single layout that adapts), Adaptive (multiple layouts for different screen sizes), Fluid (relative units for smooth scaling)
- **Real-World Choice**: Choose based on design requirements and complexity
- **Common Consideration**: Consider maintenance and performance implications
- **Advanced Strategy**: Mix approaches for different parts of the app
- **Interview Tip**: Explain that responsive is most common, adaptive for complex UIs

---

## 36) How do you share code between web and mobile platforms?

Code sharing between web and mobile platforms can be achieved through shared business logic, common utilities, and cross-platform frameworks while maintaining platform-specific UI.

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

- **Core Strategy**: Share business logic and utilities across platforms
- **Real-World Practice**: Keep UI components platform-specific
- **Common Approach**: Use monorepos for code organization
- **Advanced Option**: Consider cross-platform frameworks (React Native, Flutter)
- **Interview Tip**: Explain that implement proper abstraction layers

---

## 37) What are PWAs, and how do you make a web app installable and offline-first?

Progressive Web Apps (PWAs) are web applications that provide native app-like experiences through service workers, web app manifests, and offline functionality.

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

- **Core Features**: Implement service workers for offline functionality, create web app manifest for installability
- **Real-World Use**: Use responsive design and touch-friendly interfaces
- **Common Practice**: Implement push notifications and background sync
- **Advanced Feature**: Test across different browsers and devices
- **Interview Tip**: Explain that PWAs bridge web and native app experiences

---

## 38) How do you use service workers for offline caching and background sync?

Service workers enable offline functionality through caching strategies, background sync for data synchronization, and push notifications for user engagement.

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

- **Core Strategies**: Implement different caching strategies for different content types
- **Real-World Use**: Use background sync for offline data synchronization
- **Common Practice**: Handle push notifications and user engagement
- **Advanced Feature**: Consider cache invalidation and update strategies
- **Interview Tip**: Explain that test offline functionality thoroughly

---

## 39) How would you structure a project that supports web, mobile (React Native), and desktop (Electron)?

Multi-platform projects require shared business logic, platform-specific UI layers, and proper build configurations for each target platform.

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

- **Core Structure**: Share business logic and utilities across platforms
- **Real-World Practice**: Keep UI components platform-specific
- **Common Approach**: Use monorepos for code organization
- **Advanced Feature**: Implement proper build configurations
- **Interview Tip**: Explain that consider platform-specific features and limitations

---

## 40) What is the difference between React Native, Flutter, and Cordova?

These are different approaches to cross-platform mobile development: React Native uses native components, Flutter uses its own rendering engine, and Cordova wraps web apps in native containers.

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

- **Core Differences**: React Native (JavaScript, native performance, large ecosystem), Flutter (Dart, consistent UI, fast development), Cordova (Web technologies, easy migration, limited performance)
- **Real-World Choice**: Choose based on team expertise and performance requirements
- **Common Consideration**: Consider long-term maintenance and community support
- **Advanced Evaluation**: Evaluate based on project requirements
- **Interview Tip**: Explain that each has different trade-offs

---

## 41) How do React Native and Flutter handle rendering differently?

React Native uses native components and bridges to communicate with native code, while Flutter uses its own rendering engine and widgets that compile to native code.

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

- **Core Difference**: React Native (bridge-based communication, native components), Flutter (direct compilation, custom rendering engine)
- **Real-World Impact**: Performance implications of different approaches
- **Common Trade-off**: Development experience and debugging differences
- **Advanced Consideration**: Consider platform-specific optimizations
- **Interview Tip**: Explain that Flutter has more consistent rendering, RN uses native components

---

## 42) What are the performance and ecosystem trade-offs between RN, Flutter, and hybrid apps?

Each approach has different performance characteristics, ecosystem maturity, and development trade-offs that should be considered based on project requirements.

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

- **Core Trade-offs**: React Native (good balance of performance and ecosystem), Flutter (excellent performance, growing ecosystem), Cordova (easy development, limited performance)
- **Real-World Consideration**: Consider team expertise and project timeline
- **Common Evaluation**: Evaluate long-term maintenance and updates
- **Advanced Strategy**: Choose based on specific project needs
- **Interview Tip**: Explain that performance vs development speed trade-off

---

## 43) When would you choose web, hybrid, or native for a new product?

Platform choice depends on target audience, performance requirements, development resources, and long-term maintenance considerations.

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

- **Core Decision**: Web (best for content and information apps), Hybrid (good for apps needing some native features), Native (best for performance-critical and feature-rich apps)
- **Real-World Consideration**: Consider target audience and device capabilities
- **Common Evaluation**: Evaluate development resources and timeline
- **Advanced Strategy**: Consider hybrid approach for MVP, native for scale
- **Interview Tip**: Explain that start with web, add native when needed

---
