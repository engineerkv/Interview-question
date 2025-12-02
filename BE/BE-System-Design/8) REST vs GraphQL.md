# 3. REST vs GraphQL (Q41–50)

---

## Q41. 🔀 REST vs GraphQL and when to choose which

Choose REST when you need simple CRUD operations, want HTTP caching, need multiple endpoints for different resources, or want a well-established standard with lots of tooling. Choose GraphQL when you need flexible queries where clients request exactly the data they need, want to reduce overfetching and underfetching, or need to aggregate data from multiple sources. REST is better for simple APIs, GraphQL is better for complex data requirements.

- **Trade-offs**: REST is simpler and has better HTTP caching support, but the catch is clients often overfetch or underfetch data, requiring multiple requests. GraphQL gives clients control over what data they get, which reduces overfetching, but the tricky part is it's more complex to implement, caching is harder, and you need to handle the N+1 query problem.

---

## Q42. 📊 Overfetching vs underfetching in REST vs GraphQL

Overfetching happens when you get more data than you need - like fetching a user object with 20 fields when you only need the name. Underfetching happens when you need multiple requests to get all the data you need - like fetching a user, then their orders, then order items in separate requests. REST often causes both - you get full objects (overfetching) but need multiple requests for related data (underfetching). GraphQL allows clients to request exactly the fields they need in one query, reducing both problems.

- **Trade-offs**: GraphQL reduces overfetching and underfetching by allowing clients to specify exactly what they need, which improves performance and reduces bandwidth, but the catch is it shifts complexity to the server - you need to handle flexible queries efficiently. REST is simpler but can waste bandwidth and require multiple round trips.

---

## Q43. 🔢 N+1 problem in GraphQL

N+1 problem occurs when a GraphQL query triggers multiple database queries - like querying a list of users and their orders, which causes one query for users and N queries for each user's orders. This happens because GraphQL resolvers execute independently, and if you're not careful, each resolver makes a separate database query. Solve it by using DataLoader to batch and cache queries, or by fetching related data in a single query.

- **Trade-offs**: N+1 queries can kill performance, making GraphQL slower than REST, but the catch is you need to be aware of it and use batching tools. The tricky part is it's easy to introduce N+1 problems accidentally - every resolver that fetches related data needs to use batching, otherwise you get N+1 queries.

Example:

```javascript
// N+1 problem - bad
users.forEach(user => {
  const orders = db.orders.find({ userId: user.id }); // N queries
});

// Solution with DataLoader - good
const orderLoader = new DataLoader(userIds => 
  db.orders.find({ userId: { $in: userIds } })
);
users.forEach(user => {
  const orders = orderLoader.load(user.id); // Batched into 1 query
});
```

---

## Q44. 💾 GraphQL caching challenges

GraphQL caching is harder than REST because each query is unique - REST URLs are cacheable (GET /users/123), but GraphQL queries are POST requests with different query structures, so standard HTTP caching doesn't work well. Use query result caching based on query and variables, field-level caching, or persist queries where you store queries server-side and reference them by ID. Consider using CDNs with GraphQL-specific caching or Apollo Server's caching features.

- **Trade-offs**: GraphQL's flexibility makes caching harder, but the catch is you can still cache - you just need different strategies than REST. The tricky part is cache invalidation - when data changes, you need to invalidate all queries that include that data, which can be complex with nested queries.

---

## Q45. 📐 GraphQL schema design best practices

Design GraphQL schemas by using clear type names, avoiding deep nesting (keep it to 3-4 levels), using pagination for lists, implementing proper error handling with union types, and versioning carefully. Use input types for mutations, make fields nullable when appropriate, and design for the client's needs rather than your database structure. Keep schemas simple and focused, and use schema stitching or federation for large systems.

- **Trade-offs**: Good schema design makes APIs intuitive and performant, but the catch is it requires thinking about client needs upfront, which can be hard if you don't know all use cases. The tricky part is balancing flexibility with performance - too flexible and you enable expensive queries, too restrictive and you lose GraphQL's benefits.

---

## Q46. ⚡ GraphQL vs gRPC for backend services

GraphQL is a query language and runtime for APIs, best for client-server communication where clients need flexible data fetching - like web or mobile apps querying a backend. gRPC is a high-performance RPC framework using Protocol Buffers, best for service-to-service communication where you need low latency and high throughput - like microservices talking to each other. Use GraphQL for external APIs, use gRPC for internal services.

- **Trade-offs**: GraphQL provides flexibility and reduces overfetching for clients, but the catch is it's HTTP-based and has more overhead than gRPC. gRPC is faster and more efficient for service-to-service communication, but the tricky part is it's binary and less flexible - clients need to know the exact service contract upfront.

---

## Q47. ⚠️ Error handling differences between REST and GraphQL

REST uses HTTP status codes to indicate errors - like 400 for bad requests, 404 for not found, 500 for server errors. GraphQL always returns 200 OK, even for errors, and includes errors in the response body - errors are returned alongside data, so you can have partial success. Use GraphQL's error format with message, path, and extensions to provide detailed error information.

- **Trade-offs**: REST's HTTP status codes are standard and work well with HTTP caching and proxies, but the catch is you can only return one status code per response. GraphQL's error format is more flexible and allows partial failures, but the tricky part is clients need to check the errors array, and HTTP-level caching doesn't work well since everything returns 200.

---

## Q48. 🔢 Versioning in REST vs GraphQL

REST versions APIs by including version in the URL (like /v1/users) or headers, which allows multiple versions to coexist. GraphQL avoids versioning by evolving the schema - add new fields (backward compatible), deprecate old fields, and remove them later. GraphQL's type system enables schema evolution without breaking changes, so you can add fields without versioning.

- **Trade-offs**: REST versioning is explicit and allows multiple versions to run simultaneously, but the catch is you need to maintain multiple versions which is expensive. GraphQL's schema evolution avoids versioning, which is simpler, but the tricky part is you need discipline - breaking changes require coordinated deployments, and you need to deprecate fields before removing them.

---

## Q49. 🔐 Authentication differences between REST and GraphQL

REST typically uses HTTP headers for authentication - like Authorization header with Bearer tokens, or API keys in headers. GraphQL can use the same approaches, but since all requests go to a single endpoint, you authenticate at the resolver level or use middleware. Both can use JWT tokens, OAuth, or API keys, but GraphQL's single endpoint means you need to handle authentication in the GraphQL layer rather than at the route level.

- **Trade-offs**: REST's multiple endpoints allow different authentication per endpoint, which provides flexibility, but the catch is you need to configure auth for each route. GraphQL's single endpoint simplifies routing but requires auth logic in resolvers or middleware. The tricky part is GraphQL - you need to ensure all resolvers check authentication, not just the entry point.

---

## Q50. ⚡ Performance differences at scale

At scale, REST can be faster because HTTP caching works well, requests are simpler, and you can optimize individual endpoints. GraphQL can be slower due to N+1 queries, complex query execution, and lack of HTTP caching, but it reduces overfetching which saves bandwidth. Performance depends on implementation - well-optimized GraphQL with batching can match REST, but poorly optimized GraphQL with N+1 queries can be much slower.

- **Trade-offs**: REST's simplicity and HTTP caching can make it faster at scale, but the catch is overfetching wastes bandwidth and multiple requests add latency. GraphQL reduces bandwidth and round trips, but the tricky part is you need to optimize resolvers and use batching to avoid N+1 queries, otherwise performance suffers. The key is proper implementation - both can perform well if done right.
