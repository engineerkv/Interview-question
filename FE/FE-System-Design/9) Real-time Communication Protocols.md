# 🔄 9. Real-time Communication Protocols (Q106–120)

---

## 🧩 Q106. What is short polling, and what are its advantages and disadvantages?

### 🧠 Concept

Short polling is a client-server communication technique where the client repeatedly sends HTTP requests at fixed intervals to check for updates. The server responds immediately with current data, whether or not there are updates. Use for low-frequency updates, simple implementations, when WebSockets unavailable.

---

### 💡 Example

```javascript
function shortPoll(endpoint, interval = 5000) {
  setInterval(async () => {
    try {
      const response = await fetch(endpoint);
      const data = await response.json();
      
      if (data.updates) {
        handleUpdates(data.updates);
      }
    } catch (error) {
      console.error('Polling error:', error);
    }
  }, interval);
}

// Usage
shortPoll('/api/notifications', 5000); // Poll every 5 seconds
```

---

### 🔍 Deep Insights

* **Rule:** Short polling is simplest real-time technique; requires no special server setup.
* **Use Case:** Polling interval must balance freshness vs server load and bandwidth.
* **Common Mistake:** Typical intervals: 1-30 seconds depending on use case.
* **Pro Tip:** Battery impact: Frequent polling drains mobile device batteries.

---

### ⭐ Senior Takeaway

Use for low-frequency updates, simple implementations, when WebSockets unavailable.

---

## 🧩 Q107. What is long polling, and how does it differ from short polling?

### 🧠 Concept

Long polling is a technique where the client sends a request, and the server holds it open until new data is available or a timeout occurs. This reduces empty responses compared to short polling, but requires more server resources to maintain open connections. Better than short polling for moderate update frequency, when WebSockets unavailable.

---

### 💡 Example

```javascript
async function longPoll(endpoint) {
  while (true) {
    try {
      const response = await fetch(endpoint, {
        method: 'GET',
        headers: { 'Timeout': '30000' } // 30 second timeout
      });
      
      if (response.status === 200) {
        const data = await response.json();
        handleUpdates(data);
      }
      
      // Immediately send next request after response
    } catch (error) {
      console.error('Long poll error:', error);
      await sleep(1000);
    }
  }
}
```

---

### 🔍 Deep Insights

* **Rule:** Long polling reduces unnecessary requests by holding connections open until updates available.
* **Use Case:** Timeout handling is critical: Too short wastes requests, too long causes connection issues.
* **Common Mistake:** Server must handle many concurrent open connections, requiring proper resource management.
* **Pro Tip:** Client reconnection logic needed for timeouts, network issues, and server restarts.

---

### ⭐ Senior Takeaway

Better than short polling for moderate update frequency, when WebSockets unavailable.

---

## 🧩 Q108. What are WebSockets, and how do they enable real-time bidirectional communication?

### 🧠 Concept

WebSockets provide a full-duplex communication channel over a single TCP connection, allowing both client and server to send messages at any time without the overhead of HTTP request/response cycles. This enables low-latency, efficient real-time communication. Use for real-time chat, live updates, gaming, collaborative editing, trading platforms.

---

### 💡 Example

```javascript
const socket = new WebSocket('wss://api.example.com/ws');

// Connection established
socket.onopen = () => {
  console.log('WebSocket connected');
  socket.send(JSON.stringify({ type: 'subscribe', channel: 'notifications' }));
};

// Receive message from server
socket.onmessage = (event) => {
  const data = JSON.parse(event.data);
  handleUpdate(data);
};

// Send message to server
function sendMessage(message) {
  if (socket.readyState === WebSocket.OPEN) {
    socket.send(JSON.stringify(message));
  }
}

// Handle close
socket.onclose = () => {
  console.log('WebSocket closed');
  reconnect();
};
```

---

### 🔍 Deep Insights

* **Rule:** WebSocket handshake starts as HTTP request, then upgrades to persistent connection.
* **Use Case:** Full-duplex communication: Both client and server can send messages anytime.
* **Common Mistake:** Low latency: No HTTP request/response overhead after initial handshake.
* **Pro Tip:** Persistent connection: Single TCP connection maintained throughout session.

---

### ⭐ Senior Takeaway

Use for real-time chat, live updates, gaming, collaborative editing, trading platforms.

---

## 🧩 Q109. What are Server-Sent Events (SSE), and how do they differ from WebSockets?

### 🧠 Concept

Server-Sent Events (SSE) enable unidirectional real-time communication from server to client over a standard HTTP connection. Unlike WebSockets, SSE only allows server-to-client messages, but is simpler to implement and works well with HTTP infrastructure. Use for live feeds, notifications, dashboards, progress updates, one-way data streams.

---

### 💡 Example

```javascript
// SSE Client
const eventSource = new EventSource('/api/events');

// Listen for messages
eventSource.onmessage = (event) => {
  const data = JSON.parse(event.data);
  handleUpdate(data);
};

// Listen for specific event types
eventSource.addEventListener('notification', (event) => {
  const notification = JSON.parse(event.data);
  showNotification(notification);
});

// Handle errors
eventSource.onerror = (error) => {
  console.error('SSE error:', error);
  // EventSource automatically reconnects
};

// Close connection
eventSource.close();
```

---

### 🔍 Deep Insights

* **Rule:** SSE is unidirectional: Only server can send messages, client uses standard HTTP.
* **Use Case:** Simpler than WebSockets: No special protocol, works with standard HTTP infrastructure.
* **Common Mistake:** Automatic reconnection: EventSource handles reconnection automatically.
* **Pro Tip:** HTTP/2 compatible: Works well with HTTP/2 multiplexing.

---

### ⭐ Senior Takeaway

Use for live feeds, notifications, dashboards, progress updates, one-way data streams.

---

## 🧩 Q110. What are webhooks, and how do they facilitate communication between applications?

### 🧠 Concept

Webhooks are HTTP callbacks that allow one application to notify another about events. Instead of polling, the provider sends HTTP POST requests to a subscriber's URL when events occur. This enables event-driven architecture and real-time updates without persistent connections. Use for payment processing, CI/CD notifications, third-party integrations, event-driven workflows.

---

### 💡 Example

```javascript
// Webhook Receiver (your application)
app.post('/webhook', express.raw({ type: 'application/json' }), (req, res) => {
  // 1. Verify webhook signature (security)
  const signature = req.headers['x-webhook-signature'];
  const isValid = verifySignature(req.body, signature, webhookSecret);
  
  if (!isValid) {
    return res.status(401).send('Invalid signature');
  }
  
  // 2. Parse webhook payload
  const payload = JSON.parse(req.body.toString());
  const event = payload.event;
  const data = payload.data;
  
  // 3. Handle different event types
  switch (event) {
    case 'payment.completed':
      handlePaymentCompleted(data);
      break;
    case 'user.created':
      handleUserCreated(data);
      break;
  }
  
  // 4. Respond quickly (within 5-10 seconds)
  res.status(200).json({ received: true });
});
```

---

### 🔍 Deep Insights

* **Rule:** Webhooks enable event-driven architecture: Providers push events instead of clients polling.
* **Use Case:** Server-to-server: Webhooks are HTTP POST requests between servers, not browser clients.
* **Common Mistake:** Security: Always verify webhook signatures to prevent unauthorized requests.
* **Pro Tip:** Idempotency: Design handlers to process same event multiple times safely.

---

### ⭐ Senior Takeaway

Use for payment processing, CI/CD notifications, third-party integrations, event-driven workflows.

---

## 🧩 Q111. How do you choose between short polling, long polling, WebSockets, SSE, and webhooks?

### 🧠 Concept

Choose based on update frequency, directionality, infrastructure constraints, and use case requirements. Short/long polling for simple cases, WebSockets for bidirectional real-time, SSE for server-to-client streaming, and webhooks for cross-system event notifications. Use WebSockets for chat, gaming, collaborative editing; SSE for notifications, live feeds; Webhooks for cross-service events.

---

### 💡 Example

```javascript
// Decision Matrix
const useWebSockets = {
  directionality: 'Bidirectional communication needed',
  updateFrequency: 'High (multiple updates per second)',
  latency: 'Low latency critical',
  examples: [
    'Real-time chat applications',
    'Collaborative editing',
    'Gaming',
    'Live trading platforms'
  ]
};

const useSSE = {
  directionality: 'Server to client only',
  updateFrequency: 'Moderate to high',
  examples: [
    'Live news feeds',
    'Progress updates',
    'Real-time notifications',
    'Dashboard updates'
  ]
};

const useWebhooks = {
  directionality: 'Cross-system notifications',
  communication: 'Server-to-server',
  examples: [
    'Payment processing notifications',
    'GitHub/GitLab CI/CD events',
    'Third-party service integrations'
  ]
};
```

---

### 🔍 Deep Insights

* **Rule:** Frequency matters (high frequency → WebSockets/SSE; low frequency → Polling/Webhooks), Directionality (bidirectional → WebSockets; server→client → SSE; cross-system → webhooks).
* **Use Case:** Infrastructure: Standard HTTP → Polling/SSE; Special setup → WebSockets.
* **Common Mistake:** Battery impact: Mobile apps prefer WebSockets/SSE over frequent polling.
* **Pro Tip:** Hybrid approach: Combine techniques based on different use cases in same application.

---

### ⭐ Senior Takeaway

Use WebSockets for chat, gaming, collaborative editing; SSE for notifications, live feeds; Webhooks for cross-service events.

---

## 🧩 Q112. How do you implement WebSocket reconnection logic?

### 🧠 Concept

WebSocket reconnection logic handles connection failures, network issues, and server restarts by automatically attempting to reconnect with exponential backoff. Implement proper reconnection logic for reliable real-time communication.

---

### 💡 Example

```javascript
class WebSocketManager {
  constructor(url) {
    this.url = url;
    this.socket = null;
    this.reconnectAttempts = 0;
    this.maxReconnectAttempts = 5;
    this.reconnectDelay = 1000;
  }
  
  connect() {
    this.socket = new WebSocket(this.url);
    
    this.socket.onopen = () => {
      console.log('WebSocket connected');
      this.reconnectAttempts = 0;
    };
    
    this.socket.onclose = () => {
      console.log('WebSocket closed');
      this.reconnect();
    };
    
    this.socket.onerror = (error) => {
      console.error('WebSocket error:', error);
    };
  }
  
  reconnect() {
    if (this.reconnectAttempts < this.maxReconnectAttempts) {
      this.reconnectAttempts++;
      const delay = Math.min(this.reconnectDelay * Math.pow(2, this.reconnectAttempts), 30000);
      setTimeout(() => this.connect(), delay);
    }
  }
}
```

---

### 🔍 Deep Insights

* **Rule:** Implement exponential backoff for reconnection attempts.
* **Use Case:** Handle connection failures and network issues gracefully.
* **Common Mistake:** Set maximum reconnection attempts to prevent infinite loops.
* **Pro Tip:** Notify users of connection status and reconnection attempts.

---

### ⭐ Senior Takeaway

Implement proper reconnection logic for reliable real-time communication.

---

## 🧩 Q113. How do you handle WebSocket message queuing?

### 🧠 Concept

WebSocket message queuing stores messages when the connection is closed and sends them when the connection is re-established, ensuring no messages are lost during disconnections. Implement message queuing for reliable message delivery.

---

### 💡 Example

```javascript
class MessageQueue {
  constructor() {
    this.queue = [];
    this.socket = null;
  }
  
  setSocket(socket) {
    this.socket = socket;
    this.flushQueue();
  }
  
  send(message) {
    if (this.socket && this.socket.readyState === WebSocket.OPEN) {
      this.socket.send(JSON.stringify(message));
    } else {
      this.queue.push(message);
    }
  }
  
  flushQueue() {
    while (this.queue.length > 0 && this.socket && this.socket.readyState === WebSocket.OPEN) {
      const message = this.queue.shift();
      this.socket.send(JSON.stringify(message));
    }
  }
}
```

---

### 🔍 Deep Insights

* **Rule:** Queue messages when connection is closed.
* **Use Case:** Send queued messages when connection is re-established.
* **Common Mistake:** Limit queue size to prevent memory issues.
* **Pro Tip:** Implement message priority for important messages.

---

### ⭐ Senior Takeaway

Implement message queuing for reliable message delivery.

---

## 🧩 Q114. How do you implement WebSocket heartbeat/ping-pong?

### 🧠 Concept

WebSocket heartbeat (ping-pong) keeps the connection alive and detects dead connections by sending periodic ping messages and expecting pong responses. Implement heartbeat to detect and handle dead connections.

---

### 💡 Example

```javascript
class WebSocketWithHeartbeat {
  constructor(url) {
    this.url = url;
    this.socket = null;
    this.pingInterval = null;
    this.pongTimeout = null;
  }
  
  connect() {
    this.socket = new WebSocket(this.url);
    
    this.socket.onopen = () => {
      this.startHeartbeat();
    };
    
    this.socket.onmessage = (event) => {
      if (event.data === 'pong') {
        clearTimeout(this.pongTimeout);
      }
    };
    
    this.socket.onclose = () => {
      this.stopHeartbeat();
    };
  }
  
  startHeartbeat() {
    this.pingInterval = setInterval(() => {
      if (this.socket && this.socket.readyState === WebSocket.OPEN) {
        this.socket.send('ping');
        this.pongTimeout = setTimeout(() => {
          this.socket.close();
        }, 5000);
      }
    }, 30000);
  }
  
  stopHeartbeat() {
    if (this.pingInterval) {
      clearInterval(this.pingInterval);
    }
    if (this.pongTimeout) {
      clearTimeout(this.pongTimeout);
    }
  }
}
```

---

### 🔍 Deep Insights

* **Rule:** Send periodic ping messages to keep connection alive.
* **Use Case:** Expect pong responses to detect dead connections.
* **Common Mistake:** Close connection if pong not received within timeout.
* **Pro Tip:** Adjust heartbeat interval based on network conditions.

---

### ⭐ Senior Takeaway

Implement heartbeat to detect and handle dead connections.

---

## 🧩 Q115. How do you handle WebSocket authentication and authorization?

### 🧠 Concept

WebSocket authentication verifies client identity when establishing the connection, while authorization controls what data clients can access. Implement proper authentication and authorization for secure WebSocket connections.

---

### 💡 Example

```javascript
const socket = new WebSocket('wss://api.example.com/ws', ['token', authToken]);

socket.onopen = () => {
  // Send authentication message
  socket.send(JSON.stringify({
    type: 'auth',
    token: authToken
  }));
};

socket.onmessage = (event) => {
  const data = JSON.parse(event.data);
  
  if (data.type === 'auth_success') {
    console.log('Authenticated');
  } else if (data.type === 'auth_failed') {
    socket.close();
    redirectToLogin();
  }
};
```

---

### 🔍 Deep Insights

* **Rule:** Authenticate during WebSocket handshake or immediately after connection.
* **Use Case:** Use tokens or session IDs for authentication.
* **Common Mistake:** Implement authorization checks for different channels or rooms.
* **Pro Tip:** Handle authentication failures gracefully.

---

### ⭐ Senior Takeaway

Implement proper authentication and authorization for secure WebSocket connections.

---

## 🧩 Q116. How do you implement WebSocket room/channel subscriptions?

### 🧠 Concept

WebSocket room/channel subscriptions allow clients to join specific channels and receive messages only for those channels, enabling efficient message routing and filtering. Implement room subscriptions for scalable real-time communication.

---

### 💡 Example

```javascript
class WebSocketChannelManager {
  constructor(socket) {
    this.socket = socket;
    this.subscriptions = new Set();
  }
  
  subscribe(channel) {
    if (!this.subscriptions.has(channel)) {
      this.socket.send(JSON.stringify({
        type: 'subscribe',
        channel: channel
      }));
      this.subscriptions.add(channel);
    }
  }
  
  unsubscribe(channel) {
    if (this.subscriptions.has(channel)) {
      this.socket.send(JSON.stringify({
        type: 'unsubscribe',
        channel: channel
      }));
      this.subscriptions.delete(channel);
    }
  }
}
```

---

### 🔍 Deep Insights

* **Rule:** Subscribe to channels to receive relevant messages.
* **Use Case:** Unsubscribe from channels when no longer needed.
* **Common Mistake:** Handle subscription confirmations from server.
* **Pro Tip:** Manage subscriptions efficiently to reduce server load.

---

### ⭐ Senior Takeaway

Implement room subscriptions for scalable real-time communication.

---

## 🧩 Q117. How do you handle WebSocket message ordering and delivery guarantees?

### 🧠 Concept

WebSocket message ordering ensures messages are processed in the correct order, while delivery guarantees ensure messages are received reliably. Implement message ordering and delivery guarantees for critical real-time features.

---

### 💡 Example

```javascript
class OrderedMessageHandler {
  constructor() {
    this.expectedSequence = 0;
    this.messageQueue = new Map();
  }
  
  handleMessage(message) {
    if (message.sequence === this.expectedSequence) {
      this.processMessage(message);
      this.expectedSequence++;
      this.processQueuedMessages();
    } else {
      this.messageQueue.set(message.sequence, message);
    }
  }
  
  processQueuedMessages() {
    while (this.messageQueue.has(this.expectedSequence)) {
      const message = this.messageQueue.get(this.expectedSequence);
      this.processMessage(message);
      this.messageQueue.delete(this.expectedSequence);
      this.expectedSequence++;
    }
  }
}
```

---

### 🔍 Deep Insights

* **Rule:** Use sequence numbers to ensure message ordering.
* **Use Case:** Queue out-of-order messages until previous messages arrive.
* **Common Mistake:** Implement acknowledgment mechanism for delivery guarantees.
* **Pro Tip:** Handle duplicate messages gracefully.

---

### ⭐ Senior Takeaway

Implement message ordering and delivery guarantees for critical real-time features.

---

## 🧩 Q118. How do you implement WebSocket compression?

### 🧠 Concept

WebSocket compression reduces message size by compressing data before sending, reducing bandwidth usage and improving performance. Implement compression for large messages or bandwidth-constrained environments.

---

### 💡 Example

```javascript
// WebSocket with compression (permessage-deflate extension)
const socket = new WebSocket('wss://api.example.com/ws', ['permessage-deflate']);

// Compress large messages before sending
function sendCompressedMessage(data) {
  const compressed = compress(data);
  socket.send(compressed);
}
```

---

### 🔍 Deep Insights

* **Rule:** Use permessage-deflate extension for automatic compression.
* **Use Case:** Compression reduces bandwidth for large messages.
* **Common Mistake:** Consider CPU overhead of compression.
* **Pro Tip:** Enable compression for bandwidth-constrained environments.

---

### ⭐ Senior Takeaway

Implement compression for large messages or bandwidth-constrained environments.

---

## 🧩 Q119. How do you handle WebSocket scaling and load balancing?

### 🧠 Concept

WebSocket scaling requires sticky sessions, proper load balancing, and state management across multiple servers. Implement proper scaling strategies for high-traffic WebSocket applications.

---

### 💡 Example

```javascript
// Sticky session configuration
const loadBalancerConfig = {
  sticky: true,
  algorithm: 'ip_hash', // Route same IP to same server
  healthCheck: true
};

// WebSocket connection with server affinity
const socket = new WebSocket(`wss://server-${getServerId()}.example.com/ws`);
```

---

### 🔍 Deep Insights

* **Rule:** Use sticky sessions to maintain connection to same server.
* **Use Case:** Implement proper load balancing for WebSocket connections.
* **Common Mistake:** Handle server failures and connection migration.
* **Pro Tip:** Consider shared state storage for multi-server setups.

---

### ⭐ Senior Takeaway

Implement proper scaling strategies for high-traffic WebSocket applications.

---

## 🧩 Q120. How do you implement WebSocket fallback strategies?

### 🧠 Concept

WebSocket fallback strategies provide alternative communication methods when WebSockets are unavailable, such as long polling or SSE. Implement fallback strategies for maximum compatibility.

---

### 💡 Example

```javascript
class RealTimeConnection {
  constructor(url) {
    this.url = url;
    this.connection = null;
  }
  
  async connect() {
    // Try WebSocket first
    if (WebSocket) {
      try {
        this.connection = new WebSocket(this.url);
        return;
      } catch (error) {
        console.warn('WebSocket failed, falling back to SSE');
      }
    }
    
    // Fallback to SSE
    if (EventSource) {
      this.connection = new EventSource(this.url);
      return;
    }
    
    // Fallback to long polling
    this.connection = new LongPollingConnection(this.url);
  }
}
```

---

### 🔍 Deep Insights

* **Rule:** Try WebSocket first, fallback to SSE or long polling.
* **Use Case:** Provide seamless fallback for maximum compatibility.
* **Common Mistake:** Handle different connection types transparently.
* **Pro Tip:** Test fallback strategies in different network conditions.

---

### ⭐ Senior Takeaway

Implement fallback strategies for maximum compatibility.

---
