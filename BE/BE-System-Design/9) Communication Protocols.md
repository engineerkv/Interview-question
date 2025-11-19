# Section 9: Communication Protocols (Q176-Q190)

---

## Q176. HTTP/1.1 vs HTTP/2 vs HTTP/3.

HTTP/1.1 sends one request per connection and requires multiple connections for parallelism, which causes head-of-line blocking. HTTP/2 multiplexes multiple requests over a single connection, uses header compression, and supports server push, which improves performance. HTTP/3 uses QUIC protocol over UDP instead of TCP, eliminating head-of-line blocking and improving performance on unreliable networks.

- **Trade-offs**: HTTP/2 improves performance significantly over HTTP/1.1, but the catch is it still uses TCP which can cause head-of-line blocking. HTTP/3 eliminates TCP's head-of-line blocking and improves performance, but the tricky part is it's newer and has less tooling support. Choose HTTP/2 for most cases, HTTP/3 for better performance on unreliable networks.

---

## Q177. gRPC vs REST — when to use?

Use gRPC for service-to-service communication where you need high performance, low latency, and strong typing - like microservices talking to each other, or internal APIs. Use REST for client-server communication where you need HTTP caching, browser compatibility, or simple integration - like public APIs or web applications. gRPC uses Protocol Buffers and HTTP/2, REST uses JSON and HTTP/1.1 or HTTP/2.

- **Trade-offs**: gRPC is faster and more efficient with binary Protocol Buffers and HTTP/2, but the catch is it's not natively supported in browsers and requires code generation. REST is simpler, works everywhere, and has better tooling, but the tricky part is it's less efficient and has more overhead. Choose gRPC for internal services, REST for external APIs.

---

## Q178. WebSockets vs SSE vs Long Polling.

WebSockets provide full-duplex communication over a single persistent connection - both client and server can send messages anytime, perfect for real-time chat or gaming. SSE (Server-Sent Events) is one-way server-to-client streaming over HTTP - server pushes events to client, good for notifications or live updates. Long polling keeps HTTP requests open until the server has data - simpler than WebSockets but less efficient.

- **Trade-offs**: WebSockets provide the best real-time performance with low latency and bidirectional communication, but the catch is they're more complex and require connection management. SSE is simpler and works over HTTP, but only supports server-to-client communication. Long polling is simplest but has higher latency and overhead. Choose WebSockets for bidirectional real-time, SSE for server push, long polling for simple cases.

---

## Q179. TCP vs UDP — trade-offs.

TCP provides reliable, ordered delivery with error correction and flow control - packets are guaranteed to arrive in order, and lost packets are retransmitted. UDP is connectionless and unreliable - packets might be lost, duplicated, or arrive out of order, but it's faster with lower overhead. Use TCP when you need reliability, use UDP when you need speed and can handle packet loss.

- **Trade-offs**: TCP's reliability is essential for most applications, but the catch is it has more overhead and can be slower due to retransmissions and flow control. UDP is faster and has lower overhead, but the tricky part is you need to handle reliability yourself if needed. Choose TCP for most applications, UDP for real-time streaming or gaming where speed matters more than perfect reliability.

---

## Q180. What is QUIC and why is it fast?

QUIC is a transport protocol built on UDP that combines the best of TCP and TLS - it provides reliable, ordered delivery like TCP, but eliminates head-of-line blocking by using multiple streams, and includes encryption by default. QUIC is faster because it reduces connection establishment time (0-RTT for repeat connections), handles packet loss better, and doesn't have TCP's head-of-line blocking.

- **Trade-offs**: QUIC improves performance significantly, especially on unreliable networks, but the catch is it's newer and has less tooling and browser support than TCP. The tricky part is it uses UDP which some firewalls block, so you need to ensure network infrastructure supports it.

---

## Q181. Binary vs text protocols.

Binary protocols encode data in binary format, which is more compact and faster to parse - like Protocol Buffers, MessagePack, or gRPC. Text protocols encode data as human-readable text, which is easier to debug and works with standard tools - like JSON, XML, or HTTP. Binary protocols are more efficient, text protocols are more developer-friendly.

- **Trade-offs**: Binary protocols are faster and use less bandwidth, which is great for performance, but the catch is they're harder to debug and require code generation or special tools. Text protocols are human-readable and work with standard tools, but the tricky part is they're slower and use more bandwidth. Choose binary for performance-critical internal services, text for external APIs or debugging.

---

## Q182. MQTT — use cases.

MQTT is a lightweight messaging protocol designed for IoT devices and unreliable networks - it uses a publish-subscribe model where devices publish messages to topics, and subscribers receive messages. Use MQTT for IoT sensors, mobile apps with unreliable connections, or any scenario where you need lightweight messaging with low bandwidth and battery usage.

- **Trade-offs**: MQTT is lightweight and works well on unreliable networks, which is perfect for IoT, but the catch is it's not as feature-rich as other messaging systems - no message ordering guarantees, limited QoS options. The tricky part is it requires a broker, and you need to handle connection management for unreliable devices.

---

## Q183. Protocol overhead & latency.

Protocol overhead is the extra data and processing required by the protocol itself - like HTTP headers, TCP handshakes, or encryption overhead. Latency is the time it takes for a request to complete. Different protocols have different overhead - HTTP/1.1 has more overhead than HTTP/2, text protocols have more overhead than binary, and TCP handshakes add latency.

- **Trade-offs**: Lower overhead improves performance and reduces bandwidth, but the catch is protocols with less overhead are often more complex or less flexible. The tricky part is balancing overhead with features - you want minimal overhead, but you also need the features the protocol provides, so you can't always minimize overhead.

---

## Q184. DNS resolution flow.

DNS resolution translates domain names to IP addresses - when you request example.com, your computer asks a DNS resolver, which queries root servers, then TLD servers (.com), then authoritative name servers for the domain, following a hierarchy until it gets the IP address. The resolver caches the result to avoid repeated lookups. This process typically takes milliseconds but can be slower if DNS servers are slow or unreachable.

- **Trade-offs**: DNS caching speeds up subsequent lookups, which improves performance, but the catch is cached records can become stale if IP addresses change. The tricky part is DNS propagation - when you change DNS records, it can take time for changes to propagate worldwide, so you might see old IPs for a while.

---

## Q185. TLS handshake explained.

TLS handshake establishes an encrypted connection between client and server - the client sends a hello with supported cipher suites, the server responds with its certificate and chosen cipher, the client verifies the certificate and generates a shared secret, and both sides derive encryption keys. This happens before any data is sent, adding latency to the first request. The handshake ensures both parties can communicate securely.

- **Trade-offs**: TLS handshake provides secure communication, which is essential, but the catch is it adds latency - typically 1-2 round trips (100-300ms) before data can be sent. The tricky part is certificate validation - if certificate chains are long or validation is slow, handshake time increases. Use TLS session resumption to reduce handshake time for subsequent connections.

---

## Q186. TLS session resumption.

TLS session resumption allows clients to reuse previous TLS session parameters, skipping most of the handshake - the client sends a session ID or ticket from a previous connection, and if the server recognizes it, they can resume the session with just one round trip instead of a full handshake. This reduces latency for repeat connections from 2 round trips to 1 round trip.

- **Trade-offs**: Session resumption reduces handshake latency significantly, which improves performance, but the catch is sessions expire after a time period, so you still get full handshakes for new sessions. The tricky part is session storage - servers need to store session information, which uses memory, or use stateless session tickets which have security considerations.

---

## Q187. API communication patterns (request/response vs streaming).

Request/response pattern sends a request and waits for a response - like HTTP REST APIs where you make a request and get a response back. Streaming pattern sends data continuously as it becomes available - like WebSockets or gRPC streaming where data flows in real-time. Use request/response for traditional APIs, use streaming for real-time data, large file transfers, or when you need to send multiple messages.

- **Trade-offs**: Request/response is simple and works well for most APIs, but the catch is it requires a new request for each operation, which adds overhead. Streaming is more efficient for continuous data and reduces latency, but the tricky part is it requires connection management and handling backpressure when data flows faster than it can be processed.

---

## Q188. MTLS — mutual TLS use cases.

Mutual TLS (mTLS) requires both client and server to present certificates, authenticating both sides - unlike regular TLS where only the server has a certificate. Use mTLS for service-to-service authentication in microservices, API security where you need to verify clients, or zero-trust architectures where you don't trust the network. It provides strong authentication and prevents unauthorized access.

- **Trade-offs**: mTLS provides strong mutual authentication, which is great for security, but the catch is it requires certificate management for both clients and servers, which adds operational overhead. The tricky part is certificate rotation - you need to rotate client certificates regularly, and if certificates expire, services can't communicate.

---

## Q189. HTTP keep-alive.

HTTP keep-alive reuses the same TCP connection for multiple HTTP requests instead of opening a new connection for each request - the connection stays open after a response, and subsequent requests use the same connection. This reduces connection establishment overhead and improves performance by avoiding TCP handshakes for each request.

- **Trade-offs**: Keep-alive reduces latency and improves performance by reusing connections, but the catch is connections consume server resources, so you need timeouts to close idle connections. The tricky part is connection limits - servers have limits on open connections, so you need to balance keep-alive duration with connection limits.

---

## Q190. Connection multiplexing in HTTP/2.

HTTP/2 connection multiplexing allows multiple requests and responses to be sent over a single TCP connection simultaneously - requests are broken into frames that can be interleaved, so one slow request doesn't block others. This eliminates head-of-line blocking where one slow request blocks all other requests on the same connection, which was a problem in HTTP/1.1.

- **Trade-offs**: Multiplexing improves performance significantly by allowing parallel requests over one connection, which is great, but the catch is it still uses TCP, so if TCP packets are lost, all streams can be blocked. The tricky part is HTTP/2 still has some head-of-line blocking at the TCP level, which is why HTTP/3 uses QUIC over UDP to eliminate it completely.
