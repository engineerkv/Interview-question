# 9) Real-time Communication Protocols (Q106–120)

---

## 106) What is short polling, and what are its advantages and disadvantages?

Concept:
Short polling is a client-server communication technique where the client repeatedly sends HTTP requests at fixed intervals to check for updates. The server responds immediately with current data, whether or not there are updates. This is simple to implement but can be inefficient due to frequent empty responses.

Example:
```javascript
// Short Polling Implementation
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

// Server-side (Express example)
app.get('/api/notifications', (req, res) => {
  // Server responds immediately with current state
  res.json({
    updates: checkForUpdates(),
    timestamp: Date.now()
  });
});

// Advantages:
// - Simple implementation
// - Works with standard HTTP
// - No special server infrastructure needed
// - Easy to debug

// Disadvantages:
// - Wastes bandwidth (many empty responses)
// - Increased server load (constant requests)
// - Delayed updates (up to polling interval)
// - Battery drain on mobile devices
```

Deep Insight:
- Short polling is simplest real-time technique; requires no special server setup
- Polling interval must balance freshness vs server load and bandwidth
- Typical intervals: 1-30 seconds depending on use case
- Battery impact: Frequent polling drains mobile device batteries
- Server load: Each client generates constant requests even without updates
- Use for: Low-frequency updates, simple implementations, when WebSockets unavailable
- Not ideal for: High-frequency updates, battery-sensitive apps, high-scale systems
- Alternatives: Long polling reduces empty responses, WebSockets for true real-time

---

## 107) What is long polling, and how does it differ from short polling?

Concept:
Long polling is a technique where the client sends a request, and the server holds it open until new data is available or a timeout occurs. This reduces empty responses compared to short polling, but requires more server resources to maintain open connections.

Example:
```javascript
// Long Polling Implementation
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
      // (loop continues automatically)
    } catch (error) {
      console.error('Long poll error:', error);
      // Wait before retrying to avoid hammering server
      await sleep(1000);
    }
  }
}

// Server-side (Node.js example)
app.get('/api/notifications/poll', (req, res) => {
  // Set timeout (e.g., 30 seconds)
  const timeout = setTimeout(() => {
    res.status(204).send(); // No content, client will retry
  }, 30000);
  
  // Check for updates
  const checkUpdates = () => {
    const updates = checkForUpdates();
    if (updates.length > 0) {
      clearTimeout(timeout);
      res.json({ updates });
    }
  };
  
  // Check immediately
  checkUpdates();
  
  // Also check periodically
  const interval = setInterval(checkUpdates, 1000);
  
  // Cleanup on client disconnect
  req.on('close', () => {
    clearTimeout(timeout);
    clearInterval(interval);
  });
});

// Comparison: Short vs Long Polling

// Short Polling:
// - Client: Request every 5s → immediate response → wait 5s → repeat
// - Server: Always responds immediately (often with "no updates")
// - Result: Many empty responses

// Long Polling:
// - Client: Request → wait for update or timeout → receive response → immediately request again
// - Server: Holds request open until update available or timeout
// - Result: Fewer empty responses, better efficiency
```

Deep Insight:
- Long polling reduces unnecessary requests by holding connections open until updates available
- Timeout handling is critical: Too short wastes requests, too long causes connection issues
- Server must handle many concurrent open connections, requiring proper resource management
- Client reconnection logic needed for timeouts, network issues, and server restarts
- Better than short polling for: Moderate update frequency, when WebSockets unavailable
- Challenges: Proxy/load balancer timeout limits, connection management complexity
- Use for: Real-time updates where WebSockets aren't feasible, moderate update frequency
- Not ideal for: Very high frequency updates, mobile apps (battery impact), simple implementations

---

## 108) What are WebSockets, and how do they enable real-time bidirectional communication?

Concept:
WebSockets provide a full-duplex communication channel over a single TCP connection, allowing both client and server to send messages at any time without the overhead of HTTP request/response cycles. This enables low-latency, efficient real-time communication.

Example:
```javascript
// WebSocket Client
const socket = new WebSocket('wss://api.example.com/ws');

// Connection established
socket.onopen = () => {
  console.log('WebSocket connected');
  // Send message to server
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

// Handle errors
socket.onerror = (error) => {
  console.error('WebSocket error:', error);
};

// Handle close
socket.onclose = () => {
  console.log('WebSocket closed');
  // Implement reconnection logic
  reconnect();
};

// Server-side (Node.js with ws library)
const WebSocket = require('ws');
const wss = new WebSocket.Server({ port: 8080 });

wss.on('connection', (ws) => {
  console.log('Client connected');
  
  // Send message to client
  ws.send(JSON.stringify({ type: 'welcome', message: 'Connected' }));
  
  // Receive message from client
  ws.on('message', (message) => {
    const data = JSON.parse(message);
    
    // Handle different message types
    if (data.type === 'subscribe') {
      // Add client to channel
      subscribeToChannel(ws, data.channel);
    } else if (data.type === 'message') {
      // Broadcast to other clients
      broadcast(data);
    }
  });
  
  ws.on('close', () => {
    console.log('Client disconnected');
    // Cleanup subscriptions
  });
});

// WebSocket Handshake Process
// 1. Client sends HTTP request with Upgrade header
const handshakeRequest = {
  'GET /ws HTTP/1.1': '',
  'Host': 'api.example.com',
  'Upgrade': 'websocket',
  'Connection': 'Upgrade',
  'Sec-WebSocket-Key': 'dGhlIHNhbXBsZSBub25jZQ==',
  'Sec-WebSocket-Version': '13'
};

// 2. Server responds with 101 Switching Protocols
const handshakeResponse = {
  'HTTP/1.1 101 Switching Protocols': '',
  'Upgrade': 'websocket',
  'Connection': 'Upgrade',
  'Sec-WebSocket-Accept': 'calculated-key'
};

// After handshake, connection is upgraded to WebSocket protocol
// Messages can flow bidirectionally without HTTP overhead
```

Deep Insight:
- WebSocket handshake starts as HTTP request, then upgrades to persistent connection
- Full-duplex communication: Both client and server can send messages anytime
- Low latency: No HTTP request/response overhead after initial handshake
- Persistent connection: Single TCP connection maintained throughout session
- Use for: Real-time chat, live updates, gaming, collaborative editing, trading platforms
- Efficient for: High-frequency updates, bidirectional communication needs
- Challenges: Connection management, reconnection logic, message ordering
- Alternatives: SSE for unidirectional server→client, polling for simple cases
- Scaling: Requires stateful servers or sticky sessions with load balancers

---

## 109) What are Server-Sent Events (SSE), and how do they differ from WebSockets?

Concept:
Server-Sent Events (SSE) enable unidirectional real-time communication from server to client over a standard HTTP connection. Unlike WebSockets, SSE only allows server-to-client messages, but is simpler to implement and works well with HTTP infrastructure.

Example:
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

eventSource.addEventListener('update', (event) => {
  const update = JSON.parse(event.data);
  updateUI(update);
});

// Handle errors
eventSource.onerror = (error) => {
  console.error('SSE error:', error);
  // EventSource automatically reconnects
};

// Close connection
eventSource.close();

// Server-side (Express example)
app.get('/api/events', (req, res) => {
  // Set SSE headers
  res.setHeader('Content-Type', 'text/event-stream');
  res.setHeader('Cache-Control', 'no-cache');
  res.setHeader('Connection', 'keep-alive');
  
  // Send initial connection message
  res.write('data: {"type":"connected","message":"SSE connection established"}\n\n');
  
  // Send periodic heartbeat to keep connection alive
  const heartbeat = setInterval(() => {
    res.write(': heartbeat\n\n');
  }, 30000);
  
  // Send actual events
  function sendEvent(eventType, data) {
    res.write(`event: ${eventType}\n`);
    res.write(`data: ${JSON.stringify(data)}\n\n`);
  }
  
  // Example: Send notification
  sendEvent('notification', {
    id: 1,
    message: 'New notification',
    timestamp: Date.now()
  });
  
  // Cleanup on client disconnect
  req.on('close', () => {
    clearInterval(heartbeat);
    res.end();
  });
});

// SSE Message Format
// Simple message:
// data: Hello World\n\n

// Named event:
// event: notification\n
// data: {"id": 1, "message": "New notification"}\n\n

// Multiple data lines (concatenated):
// data: First line\n
// data: Second line\n\n

// Comments (ignored by client):
// : This is a comment\n\n
```

Deep Insight:
- SSE is unidirectional: Only server can send messages, client uses standard HTTP
- Simpler than WebSockets: No special protocol, works with standard HTTP infrastructure
- Automatic reconnection: EventSource handles reconnection automatically
- Event types: Support for named events enables different message types
- HTTP/2 compatible: Works well with HTTP/2 multiplexing
- Use for: Live feeds, notifications, dashboards, progress updates, one-way data streams
- Limitations: Unidirectional (client can't send arbitrary messages), no binary data
- Not for: Chat applications, bidirectional communication, binary protocols
- Browser support: Excellent (except IE), EventSource API is native
- Comparison: SSE is simpler than WebSockets for server→client only; WebSockets for bidirectional

---

## 110) What are webhooks, and how do they facilitate communication between applications?

Concept:
Webhooks are HTTP callbacks that allow one application to notify another about events. Instead of polling, the provider sends HTTP POST requests to a subscriber's URL when events occur. This enables event-driven architecture and real-time updates without persistent connections.

Example:
```javascript
// Webhook Subscription (typically done via API or UI)
// 1. Register webhook URL with provider
POST https://api.provider.com/webhooks
{
  "url": "https://yourapp.com/webhook",
  "events": ["payment.completed", "user.created"],
  "secret": "webhook-secret-key"
}

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
    default:
      console.log('Unknown event type:', event);
  }
  
  // 4. Respond quickly (within 5-10 seconds)
  res.status(200).json({ received: true });
});

// Webhook Signature Verification
const crypto = require('crypto');

function verifySignature(payload, signature, secret) {
  const hmac = crypto.createHmac('sha256', secret);
  const digest = hmac.update(payload).digest('hex');
  const expectedSignature = `sha256=${digest}`;
  
  return crypto.timingSafeEqual(
    Buffer.from(signature),
    Buffer.from(expectedSignature)
  );
}

// Webhook Retry Logic (provider side)
// Providers typically retry failed webhooks:
// - Initial attempt
// - Retry after 1 minute
// - Retry after 5 minutes
// - Retry after 15 minutes
// - Retry after 1 hour
// - Give up after 24 hours

// Webhook Idempotency
// Handle duplicate webhooks (same event sent multiple times)
const processedEvents = new Set();

function handleWebhook(payload) {
  const eventId = payload.id;
  
  if (processedEvents.has(eventId)) {
    return; // Already processed
  }
  
  // Process event
  processEvent(payload);
  processedEvents.add(eventId);
}

// Webhook Testing (using ngrok for local development)
// 1. Start local server
// 2. Expose with ngrok: ngrok http 3000
// 3. Use ngrok URL for webhook: https://abc123.ngrok.io/webhook
```

Deep Insight:
- Webhooks enable event-driven architecture: Providers push events instead of clients polling
- Server-to-server: Webhooks are HTTP POST requests between servers, not browser clients
- Security: Always verify webhook signatures to prevent unauthorized requests
- Idempotency: Design handlers to process same event multiple times safely
- Retry logic: Providers retry failed webhooks; handlers must be resilient
- Use for: Payment processing, CI/CD notifications, third-party integrations, event-driven workflows
- Limitations: Requires public endpoint, firewall/proxy considerations, timeout handling
- Comparison: Webhooks for cross-system events; WebSockets/SSE for in-app real-time
- Best practices: Verify signatures, respond quickly, handle duplicates, log all webhooks
- Alternatives: Polling (simple but inefficient), WebSockets (requires persistent connection)

---

## 111) How do you choose between short polling, long polling, WebSockets, SSE, and webhooks?

Concept:
Choose based on update frequency, directionality, infrastructure constraints, and use case requirements. Short/long polling for simple cases, WebSockets for bidirectional real-time, SSE for server-to-client streaming, and webhooks for cross-system event notifications.

Example:
```javascript
// Decision Matrix

// Short Polling
// Use when:
const useShortPolling = {
  updateFrequency: 'Low (every few minutes or less)',
  complexity: 'Simple implementation required',
  infrastructure: 'Standard HTTP servers only',
  battery: 'Not a concern (web apps)',
  example: 'Check for new emails every 5 minutes'
};

// Long Polling
// Use when:
const useLongPolling = {
  updateFrequency: 'Moderate (every few seconds)',
  infrastructure: 'Can handle many open connections',
  battery: 'Moderate concern',
  complexity: 'Need better efficiency than short polling',
  example: 'Chat application where WebSockets not available'
};

// WebSockets
// Use when:
const useWebSockets = {
  directionality: 'Bidirectional communication needed',
  updateFrequency: 'High (multiple updates per second)',
  latency: 'Low latency critical',
  connection: 'Persistent connection acceptable',
  examples: [
    'Real-time chat applications',
    'Collaborative editing',
    'Gaming',
    'Live trading platforms',
    'Real-time dashboards'
  ]
};

// Server-Sent Events (SSE)
// Use when:
const useSSE = {
  directionality: 'Server to client only',
  updateFrequency: 'Moderate to high',
  complexity: 'Simpler than WebSockets',
  infrastructure: 'Standard HTTP infrastructure',
  examples: [
    'Live news feeds',
    'Progress updates',
    'Real-time notifications',
    'Dashboard updates',
    'Live sports scores'
  ]
};

// Webhooks
// Use when:
const useWebhooks = {
  directionality: 'Cross-system notifications',
  communication: 'Server-to-server',
  events: 'Event-driven architecture',
  polling: 'Want to avoid polling',
  examples: [
    'Payment processing notifications',
    'GitHub/GitLab CI/CD events',
    'Third-party service integrations',
    'E-commerce order updates',
    'User activity notifications'
  ]
};

// Comparison Table
const comparison = {
  'Short Polling': {
    latency: 'High (polling interval)',
    efficiency: 'Low (many empty responses)',
    complexity: 'Very Low',
    direction: 'Bidirectional (via separate requests)',
    infrastructure: 'Standard HTTP'
  },
  'Long Polling': {
    latency: 'Medium (reduced empty responses)',
    efficiency: 'Medium',
    complexity: 'Low',
    direction: 'Bidirectional (via separate requests)',
    infrastructure: 'Standard HTTP (many open connections)'
  },
  'WebSockets': {
    latency: 'Very Low',
    efficiency: 'Very High',
    complexity: 'Medium',
    direction: 'Bidirectional',
    infrastructure: 'Persistent connections, stateful'
  },
  'SSE': {
    latency: 'Low',
    efficiency: 'High',
    complexity: 'Low',
    direction: 'Unidirectional (server→client)',
    infrastructure: 'Standard HTTP (keep-alive)'
  },
  'Webhooks': {
    latency: 'Low (event-driven)',
    efficiency: 'High (only when events occur)',
    complexity: 'Medium',
    direction: 'Unidirectional (provider→subscriber)',
    infrastructure: 'Public endpoint, signature verification'
  }
};

// Hybrid Approach
// Use multiple techniques in same application:
function setupRealTimeUpdates() {
  // WebSockets for chat (bidirectional)
  const chatSocket = new WebSocket('wss://api.example.com/chat');
  
  // SSE for notifications (server→client only)
  const notifications = new EventSource('/api/notifications/stream');
  
  // Webhooks for payment events (cross-system)
  app.post('/webhook/payment', handlePaymentWebhook);
  
  // Long polling for legacy browser support
  if (!window.WebSocket && !window.EventSource) {
    longPoll('/api/updates');
  }
}
```

Deep Insight:
- Frequency matters: High frequency → WebSockets/SSE; Low frequency → Polling/Webhooks
- Directionality: Bidirectional → WebSockets; Server→Client → SSE; Cross-system → Webhooks
- Infrastructure: Standard HTTP → Polling/SSE; Special setup → WebSockets
- Battery impact: Mobile apps prefer WebSockets/SSE over frequent polling
- Complexity: Simple → Polling; Complex real-time → WebSockets
- Use WebSockets for: Chat, gaming, collaborative editing, high-frequency updates
- Use SSE for: Notifications, live feeds, dashboards, server-initiated updates
- Use Webhooks for: Cross-service events, payment processing, CI/CD, third-party integrations
- Use Polling for: Simple implementations, low-frequency updates, when infrastructure is limited
- Hybrid approach: Combine techniques based on different use cases in same application

---
