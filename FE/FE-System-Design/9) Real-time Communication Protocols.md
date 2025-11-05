# 9) Real-time Communication Protocols (Q106–120)

---

## 106) What is short polling, and what are its advantages and disadvantages?

Short polling is a client-server communication technique where the client repeatedly sends HTTP requests at fixed intervals to check for updates. The server responds immediately with current data, whether or not there are updates. This is simple to implement but can be inefficient due to frequent empty responses.

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

- **Core Technique**: Short polling is simplest real-time technique; requires no special server setup
- **Real-World Trade-off**: Polling interval must balance freshness vs server load and bandwidth
- **Common Practice**: Typical intervals: 1-30 seconds depending on use case
- **Important Limitation**: Battery impact: Frequent polling drains mobile device batteries
- **Interview Tip**: Explain that use for low-frequency updates, simple implementations, when WebSockets unavailable

---

## 107) What is long polling, and how does it differ from short polling?

Long polling is a technique where the client sends a request, and the server holds it open until new data is available or a timeout occurs. This reduces empty responses compared to short polling, but requires more server resources to maintain open connections.

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

- **Core Benefit**: Long polling reduces unnecessary requests by holding connections open until updates available
- **Real-World Challenge**: Timeout handling is critical: Too short wastes requests, too long causes connection issues
- **Common Requirement**: Server must handle many concurrent open connections, requiring proper resource management
- **Advanced Feature**: Client reconnection logic needed for timeouts, network issues, and server restarts
- **Interview Tip**: Explain that better than short polling for moderate update frequency, when WebSockets unavailable

---

## 108) What are WebSockets, and how do they enable real-time bidirectional communication?

WebSockets provide a full-duplex communication channel over a single TCP connection, allowing both client and server to send messages at any time without the overhead of HTTP request/response cycles. This enables low-latency, efficient real-time communication.

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

- **Core Mechanism**: WebSocket handshake starts as HTTP request, then upgrades to persistent connection
- **Real-World Benefit**: Full-duplex communication: Both client and server can send messages anytime
- **Common Advantage**: Low latency: No HTTP request/response overhead after initial handshake
- **Advanced Feature**: Persistent connection: Single TCP connection maintained throughout session
- **Interview Tip**: Explain that use for real-time chat, live updates, gaming, collaborative editing, trading platforms

---

## 109) What are Server-Sent Events (SSE), and how do they differ from WebSockets?

Server-Sent Events (SSE) enable unidirectional real-time communication from server to client over a standard HTTP connection. Unlike WebSockets, SSE only allows server-to-client messages, but is simpler to implement and works well with HTTP infrastructure.

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

- **Core Difference**: SSE is unidirectional: Only server can send messages, client uses standard HTTP
- **Real-World Advantage**: Simpler than WebSockets: No special protocol, works with standard HTTP infrastructure
- **Common Feature**: Automatic reconnection: EventSource handles reconnection automatically
- **Advanced Feature**: HTTP/2 compatible: Works well with HTTP/2 multiplexing
- **Interview Tip**: Explain that use for live feeds, notifications, dashboards, progress updates, one-way data streams

---

## 110) What are webhooks, and how do they facilitate communication between applications?

Webhooks are HTTP callbacks that allow one application to notify another about events. Instead of polling, the provider sends HTTP POST requests to a subscriber's URL when events occur. This enables event-driven architecture and real-time updates without persistent connections.

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

- **Core Mechanism**: Webhooks enable event-driven architecture: Providers push events instead of clients polling
- **Real-World Use**: Server-to-server: Webhooks are HTTP POST requests between servers, not browser clients
- **Common Requirement**: Security: Always verify webhook signatures to prevent unauthorized requests
- **Advanced Feature**: Idempotency: Design handlers to process same event multiple times safely
- **Interview Tip**: Explain that use for payment processing, CI/CD notifications, third-party integrations, event-driven workflows

---

## 111) How do you choose between short polling, long polling, WebSockets, SSE, and webhooks?

Choose based on update frequency, directionality, infrastructure constraints, and use case requirements. Short/long polling for simple cases, WebSockets for bidirectional real-time, SSE for server-to-client streaming, and webhooks for cross-system event notifications.

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

- **Core Decision Factors**: Frequency matters (high frequency → WebSockets/SSE; low frequency → Polling/Webhooks), Directionality (bidirectional → WebSockets; server→client → SSE; cross-system → webhooks)
- **Real-World Choice**: Infrastructure: Standard HTTP → Polling/SSE; Special setup → WebSockets
- **Common Consideration**: Battery impact: Mobile apps prefer WebSockets/SSE over frequent polling
- **Advanced Strategy**: Hybrid approach: Combine techniques based on different use cases in same application
- **Interview Tip**: Explain that use WebSockets for chat, gaming, collaborative editing; SSE for notifications, live feeds; Webhooks for cross-service events

---
