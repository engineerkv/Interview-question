# 9. Real-time Communication Protocols (Q106–120)

---

## Q106. What is short polling, and what are its advantages and disadvantages?

Short polling is a client-server communication technique where the client repeatedly sends HTTP requests at fixed intervals to check for updates - the server responds immediately with current data, whether or not there are updates. Use for low-frequency updates, simple implementations, when WebSockets unavailable.

- **Trade-offs**: Short polling is simplest real-time technique and requires no special server setup - polling interval must balance freshness vs server load and bandwidth, typical intervals are 1-30 seconds depending on use case. The catch is frequent polling drains mobile device batteries.

Example:

```javascript
function shortPoll(endpoint, interval = 5000) {
  setInterval(async () => {
    try {
      const response = await fetch(endpoint);
      const data = await response.json();
      if (data.updates) handleUpdates(data.updates);
    } catch (error) {
      console.error('Polling error:', error);
    }
  }, interval);
}
shortPoll('/api/notifications', 5000);
```

---

## Q107. What is long polling, and how does it differ from short polling?

Long polling is a technique where the client sends a request, and the server holds it open until new data is available or a timeout occurs - this reduces empty responses compared to short polling, but requires more server resources to maintain open connections. Better than short polling for moderate update frequency, when WebSockets unavailable.

- **Trade-offs**: Long polling reduces unnecessary requests by holding connections open until updates available - timeout handling is critical: too short wastes requests, too long causes connection issues. The catch is server must handle many concurrent open connections, requiring proper resource management - client reconnection logic needed for timeouts, network issues, and server restarts.

Example:

```javascript
async function longPoll(endpoint) {
  while (true) {
    try {
      const response = await fetch(endpoint, {
        method: 'GET',
        headers: { 'Timeout': '30000' }
      });
      if (response.status === 200) {
        const data = await response.json();
        handleUpdates(data);
      }
    } catch (error) {
      console.error('Long poll error:', error);
      await sleep(1000);
    }
  }
}
```

---

## Q108. What are WebSockets, and how do they enable real-time bidirectional communication?

WebSockets provide a full-duplex communication channel over a single TCP connection, allowing both client and server to send messages at any time without the overhead of HTTP request/response cycles - this enables low-latency, efficient real-time communication. Use for real-time chat, live updates, gaming, collaborative editing, trading platforms.

- **Trade-offs**: WebSocket handshake starts as HTTP request, then upgrades to persistent connection - full-duplex communication means both client and server can send messages anytime. Low latency with no HTTP request/response overhead after initial handshake - persistent connection means single TCP connection maintained throughout session.

Example:

```javascript
const socket = new WebSocket('wss://api.example.com/ws');
socket.onopen = () => {
  console.log('WebSocket connected');
  socket.send(JSON.stringify({ type: 'subscribe', channel: 'notifications' }));
};
socket.onmessage = (event) => {
  const data = JSON.parse(event.data);
  handleUpdate(data);
};
function sendMessage(message) {
  if (socket.readyState === WebSocket.OPEN) {
    socket.send(JSON.stringify(message));
  }
}
socket.onclose = () => {
  console.log('WebSocket closed');
  reconnect();
};
```

---

## Q109. What are Server-Sent Events (SSE), and how do they differ from WebSockets?

Server-Sent Events (SSE) enable unidirectional real-time communication from server to client over a standard HTTP connection - unlike WebSockets, SSE only allows server-to-client messages, but is simpler to implement and works well with HTTP infrastructure. Use for live feeds, notifications, dashboards, progress updates, one-way data streams.

- **Trade-offs**: SSE is unidirectional - only server can send messages, client uses standard HTTP. Simpler than WebSockets with no special protocol, works with standard HTTP infrastructure - automatic reconnection means EventSource handles reconnection automatically. HTTP/2 compatible and works well with HTTP/2 multiplexing.

Example:

```javascript
const eventSource = new EventSource('/api/events');
eventSource.onmessage = (event) => {
  const data = JSON.parse(event.data);
  handleUpdate(data);
};
eventSource.addEventListener('notification', (event) => {
  const notification = JSON.parse(event.data);
  showNotification(notification);
});
eventSource.onerror = (error) => {
  console.error('SSE error:', error);
};
eventSource.close();
```

---

## Q110. What are webhooks, and how do they facilitate communication between applications?

Webhooks are HTTP callbacks that allow one application to notify another about events - instead of polling, the provider sends HTTP POST requests to a subscriber's URL when events occur, enabling event-driven architecture and real-time updates without persistent connections. Use for payment processing, CI/CD notifications, third-party integrations, event-driven workflows.

- **Trade-offs**: Webhooks enable event-driven architecture - providers push events instead of clients polling. Server-to-server means webhooks are HTTP POST requests between servers, not browser clients - always verify webhook signatures to prevent unauthorized requests. Design handlers to process same event multiple times safely (idempotency).

Example:

```javascript
app.post('/webhook', express.raw({ type: 'application/json' }), (req, res) => {
  const signature = req.headers['x-webhook-signature'];
  const isValid = verifySignature(req.body, signature, webhookSecret);
  if (!isValid) return res.status(401).send('Invalid signature');
  const payload = JSON.parse(req.body.toString());
  switch (payload.event) {
    case 'payment.completed': handlePaymentCompleted(payload.data); break;
    case 'user.created': handleUserCreated(payload.data); break;
  }
  res.status(200).json({ received: true });
});
```

---

## Q111. How do you choose between short polling, long polling, WebSockets, SSE, and webhooks?

Choose based on update frequency, directionality, infrastructure constraints, and use case requirements - short/long polling for simple cases, WebSockets for bidirectional real-time, SSE for server-to-client streaming, and webhooks for cross-system event notifications. Use WebSockets for chat, gaming, collaborative editing; SSE for notifications, live feeds; Webhooks for cross-service events.

- **Trade-offs**: Frequency matters - high frequency → WebSockets/SSE; low frequency → Polling/Webhooks. Directionality - bidirectional → WebSockets; server→client → SSE; cross-system → webhooks. Infrastructure - standard HTTP → Polling/SSE; special setup → WebSockets. Battery impact - mobile apps prefer WebSockets/SSE over frequent polling. Hybrid approach - combine techniques based on different use cases in same application.

Example:

```javascript
const useWebSockets = {
  directionality: 'Bidirectional communication needed',
  updateFrequency: 'High (multiple updates per second)',
  examples: ['Real-time chat', 'Collaborative editing', 'Gaming']
};
const useSSE = {
  directionality: 'Server to client only',
  examples: ['Live news feeds', 'Progress updates', 'Real-time notifications']
};
const useWebhooks = {
  directionality: 'Cross-system notifications',
  examples: ['Payment processing', 'CI/CD events', 'Third-party integrations']
};
```

---

## Q112. How do you implement WebSocket reconnection logic?

WebSocket reconnection logic handles connection failures, network issues, and server restarts by automatically attempting to reconnect with exponential backoff. Implement proper reconnection logic for reliable real-time communication.

- **Trade-offs**: Implement exponential backoff for reconnection attempts - handle connection failures and network issues gracefully. Set maximum reconnection attempts to prevent infinite loops - notify users of connection status and reconnection attempts.

Example:

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

## Q113. How do you handle WebSocket message queuing?

WebSocket message queuing stores messages when the connection is closed and sends them when the connection is re-established, ensuring no messages are lost during disconnections. Implement message queuing for reliable message delivery.

- **Trade-offs**: Queue messages when connection is closed - send queued messages when connection is re-established. Limit queue size to prevent memory issues - implement message priority for important messages.

Example:

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

## Q114. How do you implement WebSocket heartbeat/ping-pong?

WebSocket heartbeat (ping-pong) keeps the connection alive and detects dead connections by sending periodic ping messages and expecting pong responses. Implement heartbeat to detect and handle dead connections.

- **Trade-offs**: Send periodic ping messages to keep connection alive - expect pong responses to detect dead connections. Close connection if pong not received within timeout - adjust heartbeat interval based on network conditions.

Example:

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
    this.socket.onopen = () => this.startHeartbeat();
    this.socket.onmessage = (event) => {
      if (event.data === 'pong') clearTimeout(this.pongTimeout);
    };
    this.socket.onclose = () => this.stopHeartbeat();
  }
  startHeartbeat() {
    this.pingInterval = setInterval(() => {
      if (this.socket && this.socket.readyState === WebSocket.OPEN) {
        this.socket.send('ping');
        this.pongTimeout = setTimeout(() => this.socket.close(), 5000);
      }
    }, 30000);
  }
  stopHeartbeat() {
    if (this.pingInterval) clearInterval(this.pingInterval);
    if (this.pongTimeout) clearTimeout(this.pongTimeout);
  }
}
```

---

## Q115. How do you handle WebSocket authentication and authorization?

WebSocket authentication verifies client identity when establishing the connection, while authorization controls what data clients can access. Implement proper authentication and authorization for secure WebSocket connections.

- **Trade-offs**: Authenticate during WebSocket handshake or immediately after connection - use tokens or session IDs for authentication. Implement authorization checks for different channels or rooms - handle authentication failures gracefully.

Example:

```javascript
const socket = new WebSocket('wss://api.example.com/ws', ['token', authToken]);
socket.onopen = () => {
  socket.send(JSON.stringify({ type: 'auth', token: authToken }));
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

## Q116. How do you implement WebSocket room/channel subscriptions?

WebSocket room/channel subscriptions allow clients to join specific channels and receive messages only for those channels, enabling efficient message routing and filtering. Implement room subscriptions for scalable real-time communication.

- **Trade-offs**: Subscribe to channels to receive relevant messages - unsubscribe from channels when no longer needed. Handle subscription confirmations from server - manage subscriptions efficiently to reduce server load.

Example:

```javascript
class WebSocketChannelManager {
  constructor(socket) {
    this.socket = socket;
    this.subscriptions = new Set();
  }
  subscribe(channel) {
    if (!this.subscriptions.has(channel)) {
      this.socket.send(JSON.stringify({ type: 'subscribe', channel: channel }));
      this.subscriptions.add(channel);
    }
  }
  unsubscribe(channel) {
    if (this.subscriptions.has(channel)) {
      this.socket.send(JSON.stringify({ type: 'unsubscribe', channel: channel }));
      this.subscriptions.delete(channel);
    }
  }
}
```

---

## Q117. How do you handle WebSocket message ordering and delivery guarantees?

WebSocket message ordering ensures messages are processed in the correct order, while delivery guarantees ensure messages are received reliably. Implement message ordering and delivery guarantees for critical real-time features.

- **Trade-offs**: Use sequence numbers to ensure message ordering - queue out-of-order messages until previous messages arrive. Implement acknowledgment mechanism for delivery guarantees - handle duplicate messages gracefully.

Example:

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

## Q118. How do you implement WebSocket compression?

WebSocket compression reduces message size by compressing data before sending, reducing bandwidth usage and improving performance. Implement compression for large messages or bandwidth-constrained environments.

- **Trade-offs**: Use permessage-deflate extension for automatic compression - compression reduces bandwidth for large messages. Consider CPU overhead of compression - enable compression for bandwidth-constrained environments.

Example:

```javascript
const socket = new WebSocket('wss://api.example.com/ws', ['permessage-deflate']);
function sendCompressedMessage(data) {
  const compressed = compress(data);
  socket.send(compressed);
}
```

---

## Q119. How do you handle WebSocket scaling and load balancing?

WebSocket scaling requires sticky sessions, proper load balancing, and state management across multiple servers. Implement proper scaling strategies for high-traffic WebSocket applications.

- **Trade-offs**: Use sticky sessions to maintain connection to same server - implement proper load balancing for WebSocket connections. Handle server failures and connection migration - consider shared state storage for multi-server setups.

Example:

```javascript
const loadBalancerConfig = {
  sticky: true,
  algorithm: 'ip_hash',
  healthCheck: true
};
const socket = new WebSocket(`wss://server-${getServerId()}.example.com/ws`);
```

---

## Q120. How do you implement WebSocket fallback strategies?

WebSocket fallback strategies provide alternative communication methods when WebSockets are unavailable, such as long polling or SSE. Implement fallback strategies for maximum compatibility.

- **Trade-offs**: Try WebSocket first, fallback to SSE or long polling - provide seamless fallback for maximum compatibility. Handle different connection types transparently - test fallback strategies in different network conditions.

Example:

```javascript
class RealTimeConnection {
  constructor(url) {
    this.url = url;
    this.connection = null;
  }
  async connect() {
    if (WebSocket) {
      try {
        this.connection = new WebSocket(this.url);
        return;
      } catch (error) {
        console.warn('WebSocket failed, falling back to SSE');
      }
    }
    if (EventSource) {
      this.connection = new EventSource(this.url);
      return;
    }
    this.connection = new LongPollingConnection(this.url);
  }
}
```

---
