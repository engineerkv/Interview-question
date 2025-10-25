# ⚛️ React.js Interview Notes (2025 Edition)

## 🔍 Section 8 — Monitoring, Analytics, and Error Tracking — Q157-Q166

---

### 157. 🔍 How do you handle runtime errors in React?

**🧠 Concept**

Runtime errors in React are handled through Error Boundaries, which catch JavaScript errors and show a fallback UI.

**💻 Example**

```jsx
class ErrorBoundary extends React.Component {
  constructor(props) {
    super(props);
    this.state = { hasError: false };
  }

  static getDerivedStateFromError(error) {
    return { hasError: true };
  }

  componentDidCatch(error, errorInfo) {
    console.error('Error caught:', error, errorInfo);
  }
}
```

**💬 Explanation + Insight**

- **Error Boundaries** - Catch errors in component tree
- **Fallback UI** - Show error message instead of white screen
- **Error Logging** - Log errors to monitoring service
- **User Experience** - Prevent app crashes
- **Development** - Help identify and fix errors

---

### 158. 🔍 How do you implement error tracking in React?

**🧠 Concept**

Implement error tracking using services like Sentry, LogRocket, or custom error tracking to monitor and debug issues.

**💻 Example**

```jsx
import * as Sentry from '@sentry/react';

// Initialize Sentry
Sentry.init({
  dsn: 'YOUR_DSN',
  environment: process.env.NODE_ENV
});

// Error boundary with Sentry
class SentryErrorBoundary extends React.Component {
  componentDidCatch(error, errorInfo) {
    Sentry.captureException(error, {
      contexts: { react: errorInfo }
    });
  }
}
```

**💬 Explanation + Insight**

- **Error Monitoring** - Track errors in production
- **User Context** - Capture user actions leading to errors
- **Performance Impact** - Monitor error impact on performance
- **Alerting** - Get notified of critical errors
- **Debugging** - Use error context for debugging

---

### 159. 🔍 How do you implement performance monitoring in React?

**🧠 Concept**

Implement performance monitoring using React Profiler, web-vitals library, and custom performance metrics.

**💻 Example**

```jsx
import { Profiler } from 'react';

function onRenderCallback(id, phase, actualDuration) {
  console.log('Component:', id, 'Phase:', phase, 'Duration:', actualDuration);
  
  // Send to monitoring service
  analytics.track('component_render', {
    component: id,
    phase,
    duration: actualDuration
  });
}

function App() {
  return (
    <Profiler id="App" onRender={onRenderCallback}>
      <MyComponent />
    </Profiler>
  );
}
```

**💬 Explanation + Insight**

- **Performance Profiling** - Monitor component render times
- **Real User Monitoring** - Track actual user experience
- **Performance Budgets** - Set and monitor performance limits
- **Optimization** - Identify performance bottlenecks
- **Analytics** - Send performance data to analytics

---

### 160. 🔍 How do you implement user analytics in React?

**🧠 Concept**

Implement user analytics using Google Analytics, Mixpanel, or custom analytics to track user behavior and engagement.

**💻 Example**

```jsx
import { useEffect } from 'react';
import { useLocation } from 'react-router-dom';

function Analytics() {
  const location = useLocation();
  
  useEffect(() => {
    // Track page views
    gtag('config', 'GA_MEASUREMENT_ID', {
      page_path: location.pathname
    });
  }, [location]);
  
  return null;
}

// Track custom events
function trackEvent(eventName, parameters) {
  gtag('event', eventName, parameters);
}
```

**💬 Explanation + Insight**

- **User Behavior** - Track user interactions and flows
- **Conversion Tracking** - Monitor business metrics
- **A/B Testing** - Test different versions
- **User Segmentation** - Analyze different user groups
- **Business Intelligence** - Make data-driven decisions

---

### 161. 🔍 How do you implement real-time monitoring in React?

**🧠 Concept**

Implement real-time monitoring using WebSocket connections, Server-Sent Events, or third-party monitoring services.

**💻 Example**

```jsx
import { useEffect, useState } from 'react';

function RealTimeMonitoring() {
  const [metrics, setMetrics] = useState({});
  
  useEffect(() => {
    const ws = new WebSocket('ws://localhost:8080/metrics');
    
    ws.onmessage = (event) => {
      const data = JSON.parse(event.data);
      setMetrics(data);
    };
    
    return () => ws.close();
  }, []);
  
  return <div>CPU: {metrics.cpu}%, Memory: {metrics.memory}%</div>;
}
```

**💬 Explanation + Insight**

- **Live Monitoring** - Monitor app performance in real-time
- **Alerting** - Get immediate notifications of issues
- **Dashboard** - Visualize metrics in real-time
- **Debugging** - Debug issues as they happen
- **Proactive** - Prevent issues before they affect users

---

### 162. 🔍 How do you implement logging in React?

**🧠 Concept**

Implement logging using console methods, custom logging libraries, or structured logging services.

**💻 Example**

```jsx
// Custom logger
class Logger {
  static log(level, message, data) {
    const logEntry = {
      timestamp: new Date().toISOString(),
      level,
      message,
      data,
      userAgent: navigator.userAgent
    };
    
    console.log(JSON.stringify(logEntry));
  }
  
  static error(message, error) {
    this.log('ERROR', message, { error: error.message, stack: error.stack });
  }
}

// Usage in components
function MyComponent() {
  const handleClick = () => {
    Logger.log('INFO', 'Button clicked', { buttonId: 'submit' });
  };
  
  return <button onClick={handleClick}>Submit</button>;
}
```

**💬 Explanation + Insight**

- **Structured Logging** - Use consistent log format
- **Log Levels** - Different levels for different importance
- **Context** - Include relevant context in logs
- **Centralized** - Send logs to centralized service
- **Debugging** - Use logs for debugging issues

---

### 163. 🔍 How do you implement health checks in React?

**🧠 Concept**

Implement health checks to monitor application health, API availability, and system status.

**💻 Example**

```jsx
import { useEffect, useState } from 'react';

function HealthCheck() {
  const [health, setHealth] = useState({ status: 'checking' });
  
  useEffect(() => {
    const checkHealth = async () => {
      try {
        const response = await fetch('/api/health');
        const data = await response.json();
        setHealth(data);
      } catch (error) {
        setHealth({ status: 'error', message: error.message });
      }
    };
    
    checkHealth();
    const interval = setInterval(checkHealth, 30000);
    
    return () => clearInterval(interval);
  }, []);
  
  return <div>Status: {health.status}</div>;
}
```

**💬 Explanation + Insight**

- **System Health** - Monitor overall application health
- **API Status** - Check API endpoint availability
- **Dependencies** - Monitor external service health
- **Alerting** - Get notified of health issues
- **Recovery** - Automatic recovery from issues

---

### 164. 🔍 How do you implement custom metrics in React?

**🧠 Concept**

Implement custom metrics to track business-specific KPIs, user engagement, and application performance.

**💻 Example**

```jsx
// Custom metrics tracking
class MetricsTracker {
  static trackCustomMetric(name, value, tags = {}) {
    const metric = {
      name,
      value,
      tags,
      timestamp: Date.now()
    };
    
    // Send to analytics service
    this.sendToAnalytics(metric);
  }
  
  static trackUserEngagement(action, duration) {
    this.trackCustomMetric('user_engagement', duration, {
      action,
      userId: getCurrentUserId()
    });
  }
}

// Usage in components
function EngagementTracker() {
  const [startTime, setStartTime] = useState(null);
  
  const handleStart = () => setStartTime(Date.now());
  const handleEnd = () => {
    if (startTime) {
      MetricsTracker.trackUserEngagement('video_watch', Date.now() - startTime);
    }
  };
  
  return <div onMouseEnter={handleStart} onMouseLeave={handleEnd}>Content</div>;
}
```

**💬 Explanation + Insight**

- **Business Metrics** - Track business-specific KPIs
- **User Engagement** - Monitor user interaction patterns
- **Performance Metrics** - Track custom performance indicators
- **A/B Testing** - Compare different implementations
- **Data-driven Decisions** - Use metrics for decision making

---

### 165. 🔍 How do you implement error recovery in React?

**🧠 Concept**

Implement error recovery using retry mechanisms, fallback strategies, and graceful degradation.

**💻 Example**

```jsx
import { useState, useEffect } from 'react';

function ResilientComponent() {
  const [data, setData] = useState(null);
  const [error, setError] = useState(null);
  const [retryCount, setRetryCount] = useState(0);
  
  const fetchData = async () => {
    try {
      const response = await fetch('/api/data');
      if (!response.ok) throw new Error('Network error');
      const result = await response.json();
      setData(result);
      setError(null);
    } catch (err) {
      setError(err);
      if (retryCount < 3) {
        setTimeout(() => {
          setRetryCount(prev => prev + 1);
          fetchData();
        }, 1000 * retryCount);
      }
    }
  };
  
  useEffect(() => {
    fetchData();
  }, [retryCount]);
  
  if (error && retryCount >= 3) {
    return <div>Service unavailable. Please try again later.</div>;
  }
  
  return <div>{data ? 'Data loaded' : 'Loading...'}</div>;
}
```

**💬 Explanation + Insight**

- **Retry Logic** - Automatically retry failed operations
- **Exponential Backoff** - Increase delay between retries
- **Fallback UI** - Show alternative content on errors
- **Graceful Degradation** - Maintain functionality with reduced features
- **User Experience** - Provide clear error messages

---

### 166. 🔍 How do you implement monitoring dashboards in React?

**🧠 Concept**

Implement monitoring dashboards using data visualization libraries to display metrics, alerts, and system status.

**💻 Example**

```jsx
import { useState, useEffect } from 'react';
import { LineChart, Line, XAxis, YAxis, CartesianGrid, Tooltip } from 'recharts';

function MonitoringDashboard() {
  const [metrics, setMetrics] = useState([]);
  
  useEffect(() => {
    const fetchMetrics = async () => {
      const response = await fetch('/api/metrics');
      const data = await response.json();
      setMetrics(data);
    };
    
    fetchMetrics();
    const interval = setInterval(fetchMetrics, 5000);
    
    return () => clearInterval(interval);
  }, []);
  
  return (
    <div>
      <h2>System Metrics</h2>
      <LineChart width={600} height={300} data={metrics}>
        <CartesianGrid strokeDasharray="3 3" />
        <XAxis dataKey="time" />
        <YAxis />
        <Tooltip />
        <Line type="monotone" dataKey="cpu" stroke="#8884d8" />
        <Line type="monotone" dataKey="memory" stroke="#82ca9d" />
      </LineChart>
    </div>
  );
}
```

**💬 Explanation + Insight**

- **Real-time Data** - Display live metrics and status
- **Visualization** - Use charts and graphs for data
- **Alerting** - Show alerts and notifications
- **Historical Data** - Display trends over time
- **Interactive** - Allow users to interact with data

---

*This comprehensive monitoring, analytics, and error tracking section covers essential React monitoring techniques including error handling, performance monitoring, user analytics, and real-time monitoring for production applications.*