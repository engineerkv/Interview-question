# 5) Reliability, Fault Tolerance & Monitoring (Q41–50)

## 41) What is fault tolerance, and how is it achieved?

Concept: Fault tolerance is the ability to continue operating despite component failures through redundancy, error handling, and graceful degradation strategies.

Example:
```javascript
// Fault-tolerant service call
const callServiceWithFallback = async (serviceUrl, fallbackUrl) => {
  try {
    const response = await fetch(serviceUrl, { timeout: 5000 });
    if (response.ok) return await response.json();
    throw new Error('Service returned error');
  } catch (error) {
    console.log('Primary service failed, trying fallback');
    try {
      const response = await fetch(fallbackUrl, { timeout: 5000 });
      return await response.json();
    } catch (fallbackError) {
      throw new Error('All services failed');
    }
  }
};

// Retry with exponential backoff
const retryWithBackoff = async (fn, maxRetries = 3) => {
  for (let i = 0; i < maxRetries; i++) {
    try {
      return await fn();
    } catch (error) {
      if (i === maxRetries - 1) throw error;
      await new Promise(resolve => 
        setTimeout(resolve, Math.pow(2, i) * 1000)
      );
    }
  }
};
```

Deep Insight:
- Implement redundancy at multiple levels (hardware, software, data)
- Use circuit breakers to prevent cascading failures
- Design for graceful degradation when components fail
- Implement proper error handling and recovery mechanisms
- Test failure scenarios regularly through chaos engineering

## 42) What is the circuit breaker and bulkhead pattern?

Concept: Circuit breaker stops requests to failing services, while bulkhead isolates resources to prevent cascading failures in distributed systems.

Example:
```javascript
// Circuit breaker implementation
class CircuitBreaker {
  constructor(threshold = 5, timeout = 60000) {
    this.threshold = threshold;
    this.timeout = timeout;
    this.failureCount = 0;
    this.state = 'CLOSED';
    this.nextAttempt = Date.now();
  }
  
  async call(fn) {
    if (this.state === 'OPEN') {
      if (Date.now() < this.nextAttempt) {
        throw new Error('Circuit breaker is OPEN');
      }
      this.state = 'HALF_OPEN';
    }
    
    try {
      const result = await fn();
      this.onSuccess();
      return result;
    } catch (error) {
      this.onFailure();
      throw error;
    }
  }
  
  onSuccess() {
    this.failureCount = 0;
    this.state = 'CLOSED';
  }
  
  onFailure() {
    this.failureCount++;
    if (this.failureCount >= this.threshold) {
      this.state = 'OPEN';
      this.nextAttempt = Date.now() + this.timeout;
    }
  }
}

// Bulkhead pattern
class ResourcePool {
  constructor(maxConnections) {
    this.maxConnections = maxConnections;
    this.connections = [];
    this.waitingQueue = [];
  }
  
  async acquire() {
    if (this.connections.length < this.maxConnections) {
      const connection = await this.createConnection();
      this.connections.push(connection);
      return connection;
    }
    
    return new Promise((resolve) => {
      this.waitingQueue.push(resolve);
    });
  }
  
  release(connection) {
    const index = this.connections.indexOf(connection);
    if (index > -1) {
      this.connections.splice(index, 1);
      if (this.waitingQueue.length > 0) {
        const resolve = this.waitingQueue.shift();
        resolve(this.acquire());
      }
    }
  }
}
```

Deep Insight:
- Circuit breaker prevents cascading failures by stopping requests to failing services
- Bulkhead pattern isolates resources to prevent one failure from affecting others
- Both patterns improve system resilience and stability
- Implement at different levels (service, database, external API)
- Monitor circuit breaker states and adjust thresholds based on metrics

## 43) What is graceful degradation vs fail-fast?

Concept: Graceful degradation reduces functionality when components fail, while fail-fast stops immediately on errors, each with different trade-offs.

Example:
```javascript
// Graceful degradation
const getProductWithRecommendations = async (productId) => {
  const product = await productService.getProduct(productId);
  
  try {
    const recommendations = await recommendationService.getRecommendations(productId);
    return { ...product, recommendations };
  } catch (error) {
    console.log('Recommendations service failed, returning product without recommendations');
    return { ...product, recommendations: [] };
  }
};

// Fail-fast approach
const processPayment = async (paymentData) => {
  // Validate all required services are available
  await validateServices(['payment', 'inventory', 'notification']);
  
  // Process payment
  const result = await paymentService.process(paymentData);
  await inventoryService.updateStock(paymentData.items);
  await notificationService.sendConfirmation(paymentData.userId);
  
  return result;
};
```

Deep Insight:
- Graceful degradation: Better user experience but may hide issues
- Fail-fast: Easier to debug but can cause service unavailability
- Choose based on criticality of the operation
- Implement proper monitoring and alerting for both approaches
- Consider user impact when making design decisions

## 44) What is high availability (HA), and how do you design for it?

Concept: High availability ensures the system is operational most of the time through redundancy, fault tolerance, and proper monitoring.

Example:
```javascript
// High availability setup
const createHAService = () => {
  const instances = [
    { id: 'instance-1', url: 'http://service1.example.com' },
    { id: 'instance-2', url: 'http://service2.example.com' },
    { id: 'instance-3', url: 'http://service3.example.com' }
  ];
  
  const healthCheck = async (instance) => {
    try {
      const response = await fetch(`${instance.url}/health`, { timeout: 5000 });
      return response.ok;
    } catch (error) {
      return false;
    }
  };
  
  const getHealthyInstance = async () => {
    for (const instance of instances) {
      if (await healthCheck(instance)) {
        return instance;
      }
    }
    throw new Error('No healthy instances available');
  };
  
  return { getHealthyInstance, healthCheck };
};
```

Deep Insight:
- Design for 99.9% uptime or higher
- Implement redundancy at multiple levels
- Use load balancers and health checks
- Plan for disaster recovery and backup strategies
- Monitor and alert on availability metrics

## 45) What are SLA, SLO, and SLI, and how are they used?

Concept: SLA is a contract, SLO is a target, and SLI is a measurement of service quality, forming the foundation of service level management.

Example:
```javascript
// SLI measurement
const measureAvailability = async () => {
  const totalRequests = await metrics.getCounter('total_requests');
  const successfulRequests = await metrics.getCounter('successful_requests');
  return (successfulRequests / totalRequests) * 100;
};

const measureLatency = async () => {
  const p99Latency = await metrics.getHistogram('request_duration').getPercentile(0.99);
  return p99Latency;
};

// SLO monitoring
const checkSLOs = async () => {
  const availability = await measureAvailability();
  const latency = await measureLatency();
  
  const slos = {
    availability: { target: 99.9, current: availability },
    latency: { target: 200, current: latency }
  };
  
  for (const [metric, slo] of Object.entries(slos)) {
    if (slo.current < slo.target) {
      await alerting.sendAlert(`${metric} SLO violated: ${slo.current} < ${slo.target}`);
    }
  }
};
```

Deep Insight:
- SLA: Legal contract with customers about service quality
- SLO: Internal targets for service quality
- SLI: Measurable indicators of service quality
- Use SLIs to monitor SLOs and ensure SLA compliance
- Set realistic targets based on business requirements

## 46) How do you implement monitoring and alerting effectively?

Concept: Effective monitoring uses metrics, logs, traces, and automated alerting for proactive issue detection and system health management.

Example:
```javascript
// Monitoring setup
const monitoring = {
  // Metrics collection
  recordMetric: (name, value, tags = {}) => {
    metrics.histogram(name, value, tags);
  },
  
  // Logging
  log: (level, message, context = {}) => {
    logger.log(level, message, {
      timestamp: new Date().toISOString(),
      service: 'user-service',
      ...context
    });
  },
  
  // Tracing
  trace: (operation, fn) => {
    const span = tracer.startSpan(operation);
    try {
      return fn(span);
    } finally {
      span.finish();
    }
  },
  
  // Alerting
  alert: (severity, message, context = {}) => {
    alerting.send({
      severity,
      message,
      context,
      timestamp: new Date().toISOString()
    });
  }
};

// Health check endpoint
app.get('/health', (req, res) => {
  const health = {
    status: 'healthy',
    timestamp: new Date().toISOString(),
    checks: {
      database: 'healthy',
      redis: 'healthy',
      external_api: 'healthy'
    }
  };
  
  res.json(health);
});
```

Deep Insight:
- Use the three pillars of observability: metrics, logs, and traces
- Implement health checks and readiness probes
- Set up automated alerting with proper thresholds
- Use dashboards for visualization and trend analysis
- Regular review and tuning of monitoring and alerting

## 47) What is centralized logging, and how do tools like ELK or Grafana help?

Concept: Centralized logging collects logs from all services in one place for analysis, troubleshooting, and monitoring across distributed systems.

Example:
```javascript
// Centralized logging setup
const winston = require('winston');
const { ElasticsearchTransport } = require('winston-elasticsearch');

const logger = winston.createLogger({
  level: 'info',
  format: winston.format.combine(
    winston.format.timestamp(),
    winston.format.errors({ stack: true }),
    winston.format.json()
  ),
  transports: [
    new winston.transports.Console(),
    new ElasticsearchTransport({
      level: 'info',
      clientOpts: { node: 'http://elasticsearch:9200' },
      index: 'application-logs'
    })
  ]
});

// Structured logging
const logUserAction = (userId, action, metadata = {}) => {
  logger.info('User action', {
    userId,
    action,
    timestamp: new Date().toISOString(),
    ...metadata
  });
};
```

Deep Insight:
- Centralized logging enables cross-service analysis and debugging
- Use structured logging with consistent formats
- Implement log aggregation and search capabilities
- Consider log retention and storage costs
- Use log analysis for security monitoring and compliance

## 48) What are health checks and readiness probes?

Concept: Health checks verify if a service is running, while readiness probes check if it's ready to serve traffic, essential for service discovery and load balancing.

Example:
```javascript
// Health check implementation
const healthCheck = {
  // Liveness probe - is the service running?
  liveness: (req, res) => {
    res.json({ status: 'alive', timestamp: new Date().toISOString() });
  },
  
  // Readiness probe - is the service ready to serve traffic?
  readiness: async (req, res) => {
    const checks = {
      database: await checkDatabase(),
      redis: await checkRedis(),
      external_api: await checkExternalAPI()
    };
    
    const allHealthy = Object.values(checks).every(check => check.status === 'healthy');
    
    res.status(allHealthy ? 200 : 503).json({
      status: allHealthy ? 'ready' : 'not ready',
      checks,
      timestamp: new Date().toISOString()
    });
  }
};

// Database health check
const checkDatabase = async () => {
  try {
    await database.query('SELECT 1');
    return { status: 'healthy', responseTime: Date.now() - start };
  } catch (error) {
    return { status: 'unhealthy', error: error.message };
  }
};
```

Deep Insight:
- Liveness probes detect if the service is running
- Readiness probes detect if the service is ready to serve traffic
- Use different endpoints for different probe types
- Implement proper timeout and retry logic
- Essential for Kubernetes and container orchestration

## 49) What is chaos engineering, and why do companies like Netflix use it?

Concept: Chaos engineering tests system resilience by intentionally introducing failures in production to identify weaknesses and improve fault tolerance.

Example:
```javascript
// Chaos engineering tools
const chaos = {
  // Randomly fail requests
  randomFailure: (failureRate = 0.1) => {
    return (req, res, next) => {
      if (Math.random() < failureRate) {
        return res.status(500).json({ error: 'Chaos engineering failure' });
      }
      next();
    };
  },
  
  // Simulate network latency
  randomLatency: (maxLatency = 5000) => {
    return (req, res, next) => {
      const latency = Math.random() * maxLatency;
      setTimeout(next, latency);
    };
  },
  
  // Simulate database failures
  databaseChaos: (failureRate = 0.05) => {
    return (req, res, next) => {
      if (Math.random() < failureRate) {
        throw new Error('Database chaos failure');
      }
      next();
    };
  }
};

// Chaos experiments
const runChaosExperiment = async (experiment) => {
  console.log(`Starting chaos experiment: ${experiment.name}`);
  
  // Start monitoring
  const metrics = await startMonitoring();
  
  // Inject chaos
  await experiment.inject();
  
  // Wait for experiment duration
  await new Promise(resolve => setTimeout(resolve, experiment.duration));
  
  // Stop chaos
  await experiment.stop();
  
  // Analyze results
  const results = await analyzeResults(metrics);
  console.log(`Chaos experiment completed: ${results}`);
};
```

Deep Insight:
- Chaos engineering helps identify system weaknesses before they cause outages
- Start with small, controlled experiments in non-production environments
- Gradually increase scope and move to production
- Use monitoring and alerting to measure impact
- Essential for building resilient systems

## 50) How do you handle data backups and disaster recovery?

Concept: Data backups and disaster recovery ensure data safety and business continuity through regular backups, testing, and recovery procedures.

Example:
```javascript
// Backup strategy
const backupService = {
  // Full backup
  fullBackup: async () => {
    const timestamp = new Date().toISOString();
    const backupName = `full-backup-${timestamp}`;
    
    await database.backup(backupName);
    await uploadToS3(backupName);
    
    return backupName;
  },
  
  // Incremental backup
  incrementalBackup: async (lastBackup) => {
    const timestamp = new Date().toISOString();
    const backupName = `incremental-backup-${timestamp}`;
    
    const changes = await database.getChangesSince(lastBackup);
    await database.backup(backupName, changes);
    await uploadToS3(backupName);
    
    return backupName;
  },
  
  // Point-in-time recovery
  pointInTimeRecovery: async (targetTime) => {
    const fullBackup = await findFullBackupBefore(targetTime);
    const incrementalBackups = await findIncrementalBackups(fullBackup, targetTime);
    
    await database.restore(fullBackup);
    for (const backup of incrementalBackups) {
      await database.applyIncremental(backup);
    }
  }
};

// Disaster recovery plan
const disasterRecovery = {
  // Failover to backup region
  failover: async () => {
    await updateDNS('primary-region', 'backup-region');
    await scaleUpBackupRegion();
    await notifyTeams('Failover completed');
  },
  
  // Restore from backup
  restore: async (backupName) => {
    await downloadFromS3(backupName);
    await database.restore(backupName);
    await validateDataIntegrity();
  }
};
```

Deep Insight:
- Implement 3-2-1 backup strategy: 3 copies, 2 different media, 1 offsite
- Test backup and recovery procedures regularly
- Document and practice disaster recovery procedures
- Consider RTO (Recovery Time Objective) and RPO (Recovery Point Objective)
- Monitor backup success and alert on failures
