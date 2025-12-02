# Section 4: AWS Cloud Architecture (Q81-Q105)

---

## Q81. ☁️ EC2 vs Lambda and when to choose

Choose EC2 when you need full control over the environment, long-running processes, or predictable workloads - like running a web server that's always on or processing large batch jobs. Choose Lambda for event-driven tasks, short-lived functions, or variable workloads - like processing file uploads, handling API requests, or responding to database changes.

- **Trade-offs**: EC2 gives you complete control and can run anything, but the catch is you manage the servers, patching, and scaling yourself. Lambda is serverless and auto-scales, but the tricky part is it has execution time limits, cold starts can add latency, and it's not great for long-running or CPU-intensive tasks.

---

## Q82. 📈 Auto Scaling Groups internal flow

Auto Scaling Groups monitor your instances and automatically add or remove them based on metrics like CPU usage or request count - when CPU goes above 70%, it launches new instances, and when it drops below 30%, it terminates extra instances. It uses CloudWatch alarms to trigger scaling actions, and you configure min/max/desired capacity to control the scaling range.

- **Trade-offs**: Auto Scaling keeps your costs down by removing unused instances and handles traffic spikes automatically, but the catch is there's a delay between detecting the need and launching instances, so you might want to scale proactively. The tricky part is configuring good scaling policies - too aggressive and you'll scale up and down constantly, too conservative and you'll be slow to respond to traffic changes.

---

## Q83. 🔐 IAM Users vs Roles vs Policies

IAM Users are permanent identities for people or applications that need long-term access - like developers or service accounts. IAM Roles are temporary credentials that can be assumed by users, services, or EC2 instances - like giving an EC2 instance permission to access S3. Policies are documents that define permissions - you attach policies to users, roles, or groups to grant access.

- **Trade-offs**: Users are simple but you have to manage credentials and rotate them regularly. Roles are more secure because credentials are temporary and automatically rotated, but the catch is you need to assume the role each time. The tricky part is following least privilege - only grant the minimum permissions needed, and use roles instead of users when possible.

---

## Q84. 🌐 VPC architecture

VPC is your private network in AWS where you launch resources - it's isolated from other AWS accounts and the internet by default. You create subnets in different availability zones for high availability, use route tables to control traffic flow, and use internet gateways or NAT gateways to connect to the internet. Public subnets have routes to the internet gateway, private subnets use NAT gateways for outbound internet access.

- **Trade-offs**: VPC gives you network isolation and control, which is essential for security, but the catch is you need to design your network carefully - subnet sizing, routing, and security groups all need planning. The tricky part is balancing security with accessibility - too restrictive and services can't communicate, too open and you're vulnerable to attacks.

---

## Q85. 🛡️ NACLs vs Security Groups

Security Groups are stateful firewalls at the instance level that allow traffic - you define rules for what's allowed, and responses are automatically allowed. NACLs are stateless network-level firewalls at the subnet level that can both allow and deny traffic - you define rules with explicit allow/deny, and you must allow both inbound and outbound traffic.

- **Trade-offs**: Security Groups are simpler and stateful, so you only define inbound rules and responses work automatically, but the catch is they can't deny traffic, only allow. NACLs give you deny capabilities and subnet-level control, but the tricky part is they're stateless so you need rules for both directions, and they're evaluated in order which can be confusing.

---

## Q86. ✅ Designing highly available AWS systems

Design for high availability by deploying across multiple availability zones, using load balancers to distribute traffic, enabling auto-scaling to handle load changes, and using managed services like RDS Multi-AZ for automatic failover. Use health checks to detect failures, configure automatic backups, and design stateless applications that can run on any instance.

- **Trade-offs**: Multi-AZ deployment provides redundancy and automatic failover, which is great for availability, but the catch is it costs more and adds complexity. The tricky part is you need to test failover scenarios regularly - just having redundancy doesn't help if failover doesn't work when you need it.

---

## Q87. 💾 S3 vs EFS vs EBS

S3 is object storage for files, backups, and static websites - it's highly durable and scales automatically, accessed via APIs. EFS is network file storage that multiple EC2 instances can mount simultaneously - like a shared drive in the cloud. EBS is block storage attached to a single EC2 instance - like a hard drive for your server.

- **Trade-offs**: S3 is cheap and durable for storing files, but the catch is it's not a file system - you can't mount it or use it like a regular drive. EFS works like a file system and can be shared, but it's more expensive and adds network latency. EBS is fast and works like a local disk, but the tricky part is it's tied to one instance and you need to manage backups yourself.

---

## Q88. 💰 S3 lifecycle and cost optimization

S3 lifecycle policies automatically move objects between storage classes or delete them based on age - like moving files to Glacier after 90 days, or deleting old logs after 1 year. Use lifecycle policies to reduce costs by moving infrequently accessed data to cheaper storage classes, and configure intelligent tiering to automatically optimize costs based on access patterns.

- **Trade-offs**: Lifecycle policies automate cost optimization, which saves money without manual work, but the catch is you need to understand your access patterns - moving data too aggressively to Glacier can make it slow to retrieve. The tricky part is balancing cost savings with access speed - cheaper storage means slower retrieval times.

---

## Q89. 🌍 Route53 routing policies

Route53 offers different routing policies to control how traffic is distributed - simple routing returns one IP, weighted routing splits traffic by percentage, latency-based routing sends users to the lowest latency region, failover routing switches to backup when primary fails, and geolocation routing routes based on user location. Choose based on your needs - failover for high availability, latency for performance, weighted for gradual rollouts.

- **Trade-offs**: Different routing policies solve different problems, but the catch is you need to understand how each works - weighted routing requires careful percentage management, latency routing needs good health checks. The tricky part is DNS caching - changes can take time to propagate, so failover might not be instant.

---

## Q90. 🔒 Securing S3 buckets

Secure S3 buckets by blocking public access by default, using bucket policies to control access, enabling versioning to recover from accidental deletions, enabling encryption at rest and in transit, and using IAM roles instead of access keys. Enable CloudTrail to audit access, use MFA delete for critical buckets, and configure lifecycle policies to automatically delete sensitive data.

- **Trade-offs**: Proper S3 security prevents data breaches, which is critical, but the catch is it requires understanding IAM policies, bucket policies, and ACLs which can be confusing. The tricky part is balancing security with usability - too restrictive and legitimate users can't access data, too open and you're vulnerable to attacks.

---

## Q91. 🚀 Deployment architecture for React + Node

Deploy React as static files to S3 with CloudFront CDN for fast global delivery, and deploy Node.js API to EC2 with Auto Scaling or use Lambda for serverless. Use API Gateway in front of Lambda, or Application Load Balancer in front of EC2 instances. Store environment variables in Systems Manager Parameter Store or Secrets Manager, and use Route53 for DNS.

- **Trade-offs**: S3 + CloudFront is cheap and scales automatically for static files, but the catch is you need to invalidate CloudFront cache when you deploy updates. EC2 gives you full control but you manage servers yourself, while Lambda is serverless but has cold starts. The tricky part is coordinating deployments - frontend and backend need to be compatible versions.

---

## Q92. 🔄 CI/CD pipelines for microservices

Design CI/CD pipelines with separate pipelines per microservice, using shared templates for consistency, and deploying to staging before production. Use CodePipeline to orchestrate builds and deployments, CodeBuild for building, and CodeDeploy for deploying. Tag deployments with version numbers, use blue-green or canary deployments for zero downtime, and run tests at each stage.

- **Trade-offs**: Separate pipelines give teams independence and faster deployments, but the catch is you need to coordinate shared dependencies and API contracts. The tricky part is managing database migrations across services - you need a strategy for schema changes that don't break other services.

---

## Q93. 🔄 Blue-green deployment

Blue-green deployment runs two identical production environments - blue is current, green is new version. You deploy the new version to green, test it, then switch traffic from blue to green. If something goes wrong, you switch back to blue immediately. This gives you instant rollback and zero downtime deployments.

- **Trade-offs**: Blue-green deployments eliminate downtime and provide instant rollback, which is great for critical systems, but the catch is you need double the infrastructure during deployment which costs more. The tricky part is managing stateful services - databases and sessions need to be handled carefully when switching environments.

---

## Q94. 🔄 Rolling updates with zero downtime

Rolling updates deploy new versions gradually by replacing instances one at a time - you launch new instances with the new version, wait for them to be healthy, then terminate old instances. Use health checks to ensure new instances are ready before terminating old ones, and configure your load balancer to drain connections from old instances gracefully.

- **Trade-offs**: Rolling updates minimize downtime and resource usage compared to blue-green, but the catch is there's a window where both versions run simultaneously, so you need backward compatibility. The tricky part is handling failed deployments - if new instances fail health checks, you need to stop the rollout and roll back.

---

## Q95. 🌍 CloudFront + S3 architecture

CloudFront CDN sits in front of S3 to cache and serve content from edge locations close to users - when a user requests a file, CloudFront checks its cache, and if it's not cached, it fetches from S3 and caches it for future requests. This reduces latency, offloads traffic from S3, and reduces costs by serving cached content.

- **Trade-offs**: CloudFront dramatically improves performance and reduces S3 costs, but the catch is you need to invalidate the cache when you update files, which takes time and costs money. The tricky part is cache configuration - TTL settings affect how fresh your content is versus how much you save on S3 requests.

---

## Q96. 🔗 S3 pre-signed URL flow

Pre-signed URLs give temporary access to S3 objects without exposing your AWS credentials - your server generates a signed URL with an expiration time, the client uses that URL to upload or download directly from S3. The URL includes authentication information in the query string, so S3 can verify the request without the client needing AWS credentials.

- **Trade-offs**: Pre-signed URLs allow clients to upload directly to S3, which reduces load on your server and is faster, but the catch is you lose control over the upload process - you can't validate files before they're uploaded. The tricky part is setting appropriate expiration times - too short and uploads fail, too long and URLs can be misused.

Example:

```javascript
// Generate pre-signed URL for upload
const s3 = new AWS.S3();
const params = {
  Bucket: 'my-bucket',
  Key: 'uploads/file.jpg',
  Expires: 3600, // 1 hour
  ContentType: 'image/jpeg'
};
const url = s3.getSignedUrl('putObject', params);
// Client uses this URL to upload directly to S3
```

---

## Q97. 🔐 Handling secrets with AWS Secrets Manager

Use Secrets Manager to store secrets like database passwords, API keys, and certificates - it encrypts secrets at rest, rotates them automatically, and provides APIs to retrieve them. Your application retrieves secrets at runtime using IAM roles, so secrets never appear in code or environment variables. Enable automatic rotation for database credentials to improve security.

- **Trade-offs**: Secrets Manager is secure and handles rotation automatically, which is great for compliance, but the catch is it costs money per secret and API calls. The tricky part is managing secret versions during rotation - your application needs to handle temporary failures when secrets are being rotated.

---

## Q98. 💰 AWS cost optimization best practices

Optimize costs by using reserved instances for predictable workloads, right-sizing instances based on actual usage, using spot instances for flexible workloads, enabling auto-scaling to remove unused resources, and using S3 lifecycle policies to move data to cheaper storage. Monitor costs with Cost Explorer, set up billing alerts, and tag resources to track spending by team or project.

- **Trade-offs**: Cost optimization saves money, but the catch is it requires ongoing monitoring and adjustment - what's optimal today might not be tomorrow. The tricky part is balancing cost with performance and reliability - cutting costs too aggressively can hurt user experience or system reliability.

---

## Q99. 🗄️ RDS vs DynamoDB vs Mongo Atlas

Choose RDS for relational data with complex queries, transactions, and SQL compatibility - like user accounts, orders, or financial data. Choose DynamoDB for high-scale key-value access with predictable performance - like session storage, user profiles, or real-time leaderboards. Choose Mongo Atlas for document data with flexible schemas - like content management, catalogs, or user-generated content.

- **Trade-offs**: RDS gives you SQL and ACID transactions but is harder to scale horizontally. DynamoDB scales automatically and has single-digit millisecond latency, but the catch is it's NoSQL with limited query capabilities. Mongo Atlas gives you MongoDB's flexibility with AWS management, but the tricky part is it's more expensive than self-managed MongoDB.

---

## Q100. 🔑 DynamoDB partition key design

Design partition keys to distribute data evenly across partitions and match your access patterns - use high-cardinality attributes like user_id or order_id, and avoid hot partitions where one key gets all the traffic. Use composite keys (partition + sort key) to model relationships and enable range queries, and consider using write sharding for high-write scenarios.

- **Trade-offs**: Good partition key design enables even distribution and fast queries, but the catch is you can't change the partition key after table creation without migrating data. The tricky part is balancing even distribution with query efficiency - you want even distribution to avoid throttling, but you also want queries to hit as few partitions as possible.

---

## Q101. ⚠️ DynamoDB throttling prevention

Prevent throttling by designing partition keys for even distribution, using on-demand capacity for unpredictable workloads, or provisioning enough capacity for predictable workloads. Enable auto-scaling to adjust capacity automatically, use exponential backoff when throttled, and monitor CloudWatch metrics to catch throttling early. For high-write scenarios, use write sharding to distribute writes across multiple partition keys.

- **Trade-offs**: On-demand capacity eliminates throttling but costs more for steady workloads. Provisioned capacity is cheaper but requires capacity planning. The tricky part is predicting capacity needs - over-provision and you waste money, under-provision and you get throttled.

---

## Q102. 📋 Multi-AZ replication in RDS

Multi-AZ replication creates a standby replica in a different availability zone that automatically takes over if the primary fails - data is synchronously replicated, so there's no data loss, and failover typically takes 60-120 seconds. The standby replica can't serve reads, it's only for failover, but it provides high availability and automatic backups.

- **Trade-offs**: Multi-AZ provides automatic failover and zero data loss, which is great for production databases, but the catch is it costs almost double and the standby can't serve reads. The tricky part is failover time - 60-120 seconds of downtime might be acceptable for some applications but not others, so you might need read replicas for faster recovery.

---

## Q103. 📖 RDS read replicas

RDS read replicas are asynchronous copies of your primary database that can serve read queries - you create replicas in different availability zones or regions, and they replicate changes from the primary with a small delay. Use read replicas to scale reads, reduce load on the primary, and provide disaster recovery. You can promote a read replica to become the primary if needed.

- **Trade-offs**: Read replicas allow you to scale reads almost infinitely and provide redundancy, but the catch is you get eventual consistency - reads might see slightly stale data. The tricky part is routing queries correctly - you need application logic to send reads to replicas and writes to primary, and you need to handle replica lag when you need fresh data.

---

## Q104. 🌐 DynamoDB Global Tables

DynamoDB Global Tables replicate your table across multiple regions automatically, so you can serve users from the nearest region with low latency. Writes to any region are replicated to all other regions within seconds, and each region can serve both reads and writes. This provides global low latency and disaster recovery.

- **Trade-offs**: Global Tables provide low latency worldwide and automatic disaster recovery, which is great for global applications, but the catch is they cost more since you're paying for multiple regions and replication. The tricky part is eventual consistency - writes in one region might take a few seconds to appear in other regions, so you need to handle this in your application.

---

## Q105. ⚡ On-demand vs provisioned capacity

On-demand capacity automatically scales up and down based on traffic, so you pay for what you use without capacity planning - perfect for unpredictable workloads or new applications. Provisioned capacity requires you to specify read and write capacity units, and you pay for that capacity whether you use it or not - better for predictable, steady workloads where you can optimize costs.

- **Trade-offs**: On-demand is simple and eliminates throttling, but the catch is it costs more for steady workloads - you pay a premium for the flexibility. Provisioned capacity is cheaper for predictable workloads, but the tricky part is you need to monitor and adjust capacity, and you can get throttled if traffic spikes unexpectedly.
