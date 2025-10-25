# 🏗️ Frontend System Design Interview Notes (2025 Edition)

## 🧩 Section 5 — Frontend Infrastructure, CI/CD & Delivery — Q86-Q110

---

### 86. 🧩 What does a typical frontend CI/CD pipeline look like?

**🧠 Concept**

Frontend CI/CD pipelines automate building, testing, and deploying applications through stages of validation and deployment.

**💻 Example**

```yaml
# GitHub Actions CI/CD pipeline
name: Frontend CI/CD
on: [push, pull_request]

jobs:
  test:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v3
      - uses: actions/setup-node@v3
      - run: npm ci
      - run: npm test
      - run: npm run lint
      - run: npm run build
  
  deploy:
    needs: test
    runs-on: ubuntu-latest
    steps:
      - run: npm run deploy
```

**💬 Explanation + Insight**

- **Automated Testing** - Run tests on every commit
- **Quality Gates** - Prevent deployment of broken code
- **Deployment** - Automate deployment process
- **Consistency** - Ensure consistent builds
- **Use Cases** - Large teams, production applications

---

### 87. 🧩 How do you automate builds for multiple environments (dev, staging, prod)?

**🧠 Concept**

Multi-environment builds use configuration management, environment variables, and deployment strategies to maintain consistency across environments.

**💻 Example**

```javascript
// Environment configuration
const configs = {
  development: {
    apiUrl: 'https://dev-api.example.com',
    debug: true,
    logLevel: 'debug'
  },
  staging: {
    apiUrl: 'https://staging-api.example.com',
    debug: false,
    logLevel: 'info'
  },
  production: {
    apiUrl: 'https://api.example.com',
    debug: false,
    logLevel: 'error'
  }
};

// Build script
const environment = process.env.NODE_ENV || 'development';
const config = configs[environment];
```

**💬 Explanation + Insight**

- **Environment Management** - Separate configurations per environment
- **Consistency** - Maintain consistency across environments
- **Deployment** - Automated deployment to multiple environments
- **Configuration** - Environment-specific settings
- **Use Cases** - Multi-environment applications, team workflows

---

### 88. 🧩 What is the difference between GitHub Actions, CircleCI, and GitLab CI?

**🧠 Concept**

Different CI/CD platforms offer varying features, pricing, and integration capabilities for frontend development workflows.

**💻 Example**

```javascript
// GitHub Actions
- Integrated with GitHub
- Free for public repos
- YAML configuration
- Marketplace integrations

// CircleCI
- Cloud and self-hosted
- Free tier available
- Docker support
- Parallel execution

// GitLab CI
- Integrated with GitLab
- Free for public repos
- YAML configuration
- Built-in container registry
```

**💬 Explanation + Insight**

- **GitHub Actions** - Integrated with GitHub, free for public repos
- **CircleCI** - Cloud and self-hosted options, Docker support
- **GitLab CI** - Integrated with GitLab, built-in features
- **Features** - Different capabilities and integrations
- **Use Cases** - Choose based on team needs and preferences

---

### 89. 🧩 What is Canary vs Blue-Green deployment?

**🧠 Concept**

Canary deployment gradually rolls out changes to a small percentage of users, while Blue-Green deployment switches traffic between two identical environments.

**💻 Example**

```javascript
// Canary deployment
1. Deploy to 5% of users
2. Monitor metrics
3. Gradually increase to 50%
4. Full rollout if successful
5. Rollback if issues detected

// Blue-Green deployment
1. Deploy to green environment
2. Test green environment
3. Switch traffic from blue to green
4. Keep blue as backup
5. Rollback to blue if needed
```

**💬 Explanation + Insight**

- **Canary** - Gradual rollout, risk mitigation
- **Blue-Green** - Instant switch, easy rollback
- **Risk Management** - Different risk levels
- **Rollback** - Easy rollback strategies
- **Use Cases** - Canary for risk reduction, Blue-Green for instant switch

---

### 90. 🧩 How do you automate rollbacks after failed deployments?

**🧠 Concept**

Automated rollbacks detect deployment failures and automatically revert to the previous working version to minimize downtime.

**💻 Example**

```javascript
// Rollback automation
const rollbackConfig = {
  healthCheck: {
    endpoint: '/health',
    timeout: 30000,
    retries: 3
  },
  rollback: {
    trigger: 'health-check-failure',
    action: 'revert-to-previous',
    timeout: 300000
  }
};

// Health check implementation
async function healthCheck() {
  try {
    const response = await fetch('/health');
    return response.ok;
  } catch (error) {
    return false;
  }
}
```

**💬 Explanation + Insight**

- **Health Monitoring** - Monitor application health
- **Automatic Rollback** - Revert on failure detection
- **Downtime Reduction** - Minimize service disruption
- **Reliability** - Improve deployment reliability
- **Use Cases** - Production applications, critical services

---

### 91. 🧩 What is the difference between incremental builds and cold builds?

**🧠 Concept**

Incremental builds only rebuild changed parts, while cold builds start from scratch, affecting build time and resource usage.

**💻 Example**

```javascript
// Incremental build
- Only rebuild changed files
- Faster build times
- Requires build cache
- More complex setup

// Cold build
- Build everything from scratch
- Slower build times
- No cache dependencies
- Simpler setup
```

**💬 Explanation + Insight**

- **Incremental** - Faster builds, cache dependencies
- **Cold** - Slower builds, no cache dependencies
- **Performance** - Different performance characteristics
- **Complexity** - Different complexity levels
- **Use Cases** - Incremental for development, cold for clean builds

---

### 92. 🧩 What is code splitting in CI/CD pipelines?

**🧠 Concept**

Code splitting in CI/CD involves dividing JavaScript bundles into smaller chunks during the build process for better performance.

**💻 Example**

```javascript
// Code splitting configuration
// webpack.config.js
module.exports = {
  optimization: {
    splitChunks: {
      chunks: 'all',
      cacheGroups: {
        vendor: {
          test: /[\\/]node_modules[\\/]/,
          name: 'vendors',
          chunks: 'all'
        }
      }
    }
  }
};

// CI/CD pipeline
- Build application
- Split code into chunks
- Upload chunks to CDN
- Deploy with chunk references
```

**💬 Explanation + Insight**

- **Bundle Optimization** - Divide bundles into chunks
- **Performance** - Improve loading performance
- **Caching** - Better caching of individual chunks
- **Deployment** - Deploy chunks separately
- **Use Cases** - Large applications, performance optimization

---

### 93. 🧩 How do you manage environment variables securely in CI?

**🧠 Concept**

Secure environment variable management involves using secrets managers, encryption, and access controls to protect sensitive data.

**💻 Example**

```yaml
# GitHub Secrets
secrets:
  API_KEY: ${{ secrets.API_KEY }}
  DATABASE_URL: ${{ secrets.DATABASE_URL }}

# AWS Secrets Manager
- name: Get secrets
  run: |
    aws secretsmanager get-secret-value \
      --secret-id production/secrets \
      --query SecretString --output text
```

**💬 Explanation + Insight**

- **Secrets Management** - Secure storage of sensitive data
- **Access Control** - Limit access to secrets
- **Encryption** - Encrypt secrets at rest and in transit
- **Rotation** - Regular secret rotation
- **Use Cases** - Production applications, sensitive data

---

### 94. 🧩 What are secrets managers (AWS Secrets, Vault), and why use them?

**🧠 Concept**

Secrets managers provide secure storage, rotation, and access control for sensitive data like API keys and database credentials.

**💻 Example**

```javascript
// AWS Secrets Manager
const AWS = require('aws-sdk');
const secretsManager = new AWS.SecretsManager();

const getSecret = async (secretName) => {
  const result = await secretsManager.getSecretValue({
    SecretId: secretName
  }).promise();
  return JSON.parse(result.SecretString);
};

// HashiCorp Vault
const vault = require('node-vault');
const client = vault({
  apiVersion: 'v1',
  endpoint: 'https://vault.example.com'
});
```

**💬 Explanation + Insight**

- **Secure Storage** - Encrypted storage of secrets
- **Access Control** - Fine-grained access control
- **Rotation** - Automatic secret rotation
- **Auditing** - Track secret access
- **Use Cases** - Production applications, compliance requirements

---

### 95. 🧩 How do you handle versioning for shared UI libraries?

**🧠 Concept**

Shared UI library versioning involves semantic versioning, dependency management, and backward compatibility strategies.

**💻 Example**

```javascript
// Semantic versioning
const version = {
  major: 1,    // Breaking changes
  minor: 2,    // New features
  patch: 3     // Bug fixes
};

// Package.json
{
  "name": "@company/ui-library",
  "version": "1.2.3",
  "peerDependencies": {
    "react": ">=16.8.0"
  }
}

// Versioning strategy
- Major: Breaking changes
- Minor: New features, backward compatible
- Patch: Bug fixes, backward compatible
```

**💬 Explanation + Insight**

- **Semantic Versioning** - Standardized version numbering
- **Dependency Management** - Manage library dependencies
- **Backward Compatibility** - Maintain compatibility
- **Release Strategy** - Planned release cycles
- **Use Cases** - Shared libraries, component systems

---

### 96. 🧩 What is semantic versioning (semver)?

**🧠 Concept**

Semantic versioning uses a three-part version number (major.minor.patch) to communicate the nature of changes in software releases.

**💻 Example**

```javascript
// Semantic versioning format
MAJOR.MINOR.PATCH

// Examples
1.0.0 - Initial release
1.0.1 - Bug fix
1.1.0 - New feature
2.0.0 - Breaking change

// Version ranges
"^1.2.3" - Compatible with 1.x.x
"~1.2.3" - Compatible with 1.2.x
"1.2.3" - Exact version
```

**💬 Explanation + Insight**

- **Version Communication** - Communicate change nature
- **Dependency Management** - Manage version compatibility
- **Breaking Changes** - Major version for breaking changes
- **Feature Additions** - Minor version for new features
- **Use Cases** - Package management, dependency resolution

---

### 97. 🧩 How do you automate visual regression testing (Percy, Chromatic)?

**🧠 Concept**

Visual regression testing automatically detects visual changes in UI components, ensuring consistent appearance across updates.

**💻 Example**

```javascript
// Percy visual testing
import { percySnapshot } from '@percy/playwright';

test('visual regression test', async ({ page }) => {
  await page.goto('/');
  await percySnapshot(page, 'Homepage');
});

// Chromatic visual testing
// chromatic.config.js
module.exports = {
  projectToken: 'your-project-token',
  buildScriptName: 'build-storybook',
  storybookBuildDir: 'storybook-static'
};
```

**💬 Explanation + Insight**

- **Visual Consistency** - Ensure UI consistency
- **Automated Testing** - Automatic visual change detection
- **Regression Prevention** - Prevent visual regressions
- **Quality Assurance** - Maintain visual quality
- **Use Cases** - UI components, design systems

---

### 98. 🧩 How do you run Lighthouse or WebPageTest in pipelines?

**🧠 Concept**

Performance testing in CI/CD pipelines ensures performance standards are maintained through automated Lighthouse and WebPageTest runs.

**💻 Example**

```yaml
# Lighthouse CI in GitHub Actions
- name: Lighthouse CI
  uses: treosh/lighthouse-ci-action@v9
  with:
    configPath: './lighthouserc.json'
    uploadArtifacts: true
    temporaryPublicStorage: true

# WebPageTest integration
- name: WebPageTest
  run: |
    npm install -g webpagetest
    webpagetest test https://example.com --key $WPT_API_KEY
```

**💬 Explanation + Insight**

- **Performance Testing** - Automated performance validation
- **Quality Gates** - Prevent performance regressions
- **Continuous Monitoring** - Ongoing performance tracking
- **Standards** - Maintain performance standards
- **Use Cases** - Performance-critical applications, quality assurance

---

### 99. 🧩 What is the difference between static and dynamic site hosting?

**🧠 Concept**

Static hosting serves pre-built files, while dynamic hosting generates content on-demand, each with different performance and complexity characteristics.

**💻 Example**

```javascript
// Static site hosting
- Pre-built HTML, CSS, JS files
- Served from CDN
- Fast performance
- No server processing
- Examples: Netlify, Vercel, GitHub Pages

// Dynamic site hosting
- Server-generated content
- Database integration
- User-specific content
- Server processing required
- Examples: AWS, Google Cloud, Azure
```

**💬 Explanation + Insight**

- **Static** - Pre-built files, fast performance
- **Dynamic** - Server-generated content, more complex
- **Performance** - Static typically faster
- **Complexity** - Dynamic more complex but more flexible
- **Use Cases** - Static for content sites, dynamic for applications

---

### 100. 🧩 How does Vercel, Netlify, or Cloudflare handle edge caching and deployment?

**🧠 Concept**

Modern hosting platforms provide edge caching, global distribution, and automated deployment for optimal performance and developer experience.

**💻 Example**

```javascript
// Vercel deployment
// vercel.json
{
  "builds": [
    {
      "src": "package.json",
      "use": "@vercel/static-build"
    }
  ],
  "functions": {
    "app/api/**/*.js": {
      "runtime": "nodejs18.x"
    }
  }
}

// Netlify deployment
# netlify.toml
[build]
  command = "npm run build"
  publish = "dist"

[[headers]]
  for = "/*"
  [headers.values]
    Cache-Control = "public, max-age=31536000"
```

**💬 Explanation + Insight**

- **Edge Caching** - Global content distribution
- **Automated Deployment** - Seamless deployment process
- **Performance** - Optimized for speed and reliability
- **Developer Experience** - Easy setup and management
- **Use Cases** - Modern web applications, static sites

---

### 101. 🧩 How do you dockerize frontend apps for reproducibility?

**🧠 Concept**

Dockerizing frontend applications ensures consistent environments across development, testing, and production through containerization.

**💻 Example**

```dockerfile
# Dockerfile for frontend app
FROM node:18-alpine

WORKDIR /app
COPY package*.json ./
RUN npm ci --only=production

COPY . .
RUN npm run build

FROM nginx:alpine
COPY --from=0 /app/dist /usr/share/nginx/html
COPY nginx.conf /etc/nginx/nginx.conf

EXPOSE 80
CMD ["nginx", "-g", "daemon off;"]
```

**💬 Explanation + Insight**

- **Reproducibility** - Consistent environments
- **Portability** - Run anywhere Docker runs
- **Isolation** - Isolated application environment
- **Scalability** - Easy horizontal scaling
- **Use Cases** - Production deployments, development environments

---

### 102. 🧩 How do you perform security scans in CI/CD?

**🧠 Concept**

Security scanning in CI/CD pipelines automatically detects vulnerabilities in dependencies, code, and configurations.

**💻 Example**

```yaml
# Security scanning in CI/CD
- name: Security scan
  run: |
    npm audit
    npm audit --audit-level high
    
- name: Dependency scan
  run: |
    npx audit-ci --config audit-ci.json
    
- name: Code security scan
  run: |
    npx eslint --ext .js,.jsx,.ts,.tsx src/
    npx security-audit
```

**💬 Explanation + Insight**

- **Vulnerability Detection** - Identify security issues
- **Automated Scanning** - Continuous security monitoring
- **Dependency Security** - Scan for vulnerable dependencies
- **Code Security** - Static code analysis
- **Use Cases** - Production applications, security compliance

---

### 103. 🧩 What is feature flagging, and how do you use LaunchDarkly or ConfigCat?

**🧠 Concept**

Feature flagging allows dynamic feature control without code deployment, enabling gradual rollouts and A/B testing.

**💻 Example**

```javascript
// Feature flag implementation
import { LaunchDarkly } from 'launchdarkly-js-client-sdk';

const ldClient = LaunchDarkly.initialize('your-client-id', user);

ldClient.on('ready', () => {
  const showNewFeature = ldClient.variation('new-feature', false);
  if (showNewFeature) {
    renderNewFeature();
  }
});

// ConfigCat implementation
import { createClient } from 'configcat-js';

const client = createClient('your-sdk-key');
const showFeature = await client.getValueAsync('new-feature', false);
```

**💬 Explanation + Insight**

- **Dynamic Control** - Control features without deployment
- **Gradual Rollout** - Roll out features gradually
- **A/B Testing** - Test different feature versions
- **Risk Mitigation** - Reduce deployment risks
- **Use Cases** - Feature rollouts, experimentation

---

### 104. 🧩 What is progressive rollout, and why is it safer?

**🧠 Concept**

Progressive rollout gradually increases the percentage of users receiving new features, allowing for risk assessment and quick rollback.

**💻 Example**

```javascript
// Progressive rollout strategy
const rolloutConfig = {
  phase1: { percentage: 5, duration: '1 hour' },
  phase2: { percentage: 25, duration: '2 hours' },
  phase3: { percentage: 50, duration: '4 hours' },
  phase4: { percentage: 100, duration: '24 hours' }
};

// Rollout implementation
function shouldShowFeature(userId, featureFlag) {
  const hash = hashUserId(userId);
  const percentage = getRolloutPercentage(featureFlag);
  return hash < percentage;
}
```

**💬 Explanation + Insight**

- **Risk Mitigation** - Reduce deployment risks
- **Gradual Increase** - Slowly increase user percentage
- **Monitoring** - Monitor metrics at each phase
- **Rollback** - Quick rollback if issues detected
- **Use Cases** - High-risk features, large user bases

---

### 105. 🧩 How do you automate bundle analysis and regression alerts?

**🧠 Concept**

Automated bundle analysis tracks bundle size changes and alerts on regressions to maintain performance standards.

**💻 Example**

```javascript
// Bundle analysis automation
const bundleAnalyzer = require('webpack-bundle-analyzer');

module.exports = {
  plugins: [
    new BundleAnalyzerPlugin({
      analyzerMode: 'static',
      openAnalyzer: false,
      generateStatsFile: true
    })
  ]
};

// Regression detection
const bundleSize = getBundleSize();
const threshold = 250000; // 250KB

if (bundleSize > threshold) {
  sendAlert(`Bundle size ${bundleSize} exceeds threshold ${threshold}`);
}
```

**💬 Explanation + Insight**

- **Bundle Monitoring** - Track bundle size changes
- **Regression Detection** - Identify size increases
- **Performance** - Maintain performance standards
- **Automation** - Automated monitoring and alerts
- **Use Cases** - Performance-critical applications, large teams

---

### 106. 🧩 What is an artifact repository, and how is it used in frontend builds?

**🧠 Concept**

Artifact repositories store build outputs, dependencies, and deployment artifacts for version control and distribution.

**💻 Example**

```javascript
// Artifact repository usage
// Store build artifacts
const artifacts = {
  build: 'dist/',
  assets: 'public/',
  bundles: 'bundles/',
  sourcemaps: 'sourcemaps/'
};

// Upload to repository
const uploadArtifacts = async () => {
  await uploadToRepository(artifacts);
};

// Retrieve artifacts
const downloadArtifacts = async (version) => {
  return await downloadFromRepository(version);
};
```

**💬 Explanation + Insight**

- **Artifact Storage** - Store build outputs
- **Version Control** - Track artifact versions
- **Distribution** - Distribute artifacts to environments
- **Backup** - Backup build artifacts
- **Use Cases** - Large applications, multiple environments

---

### 107. 🧩 What is incremental static regeneration (ISR), and how does it fit into CI/CD?

**🧠 Concept**

ISR allows static pages to be regenerated on-demand while serving cached versions, balancing performance and content freshness.

**💻 Example**

```javascript
// ISR implementation
export async function getStaticProps() {
  const data = await fetchData();
  
  return {
    props: { data },
    revalidate: 60 // Regenerate every 60 seconds
  };
}

// CI/CD integration
- Build static pages
- Deploy to CDN
- Set revalidation intervals
- Monitor cache hit rates
```

**💬 Explanation + Insight**

- **Static Performance** - Fast static page serving
- **Content Freshness** - Regenerate when needed
- **CDN Integration** - Work with CDN caching
- **Performance** - Balance speed and freshness
- **Use Cases** - Content sites, e-commerce, blogs

---

### 108. 🧩 What are best practices for build caching in monorepos?

**🧠 Concept**

Monorepo build caching optimizes build performance by caching dependencies, build outputs, and intermediate results.

**💻 Example**

```javascript
// Monorepo caching strategies
const cacheConfig = {
  dependencies: {
    cache: 'node_modules/.cache',
    strategy: 'content-hash'
  },
  build: {
    cache: '.build-cache',
    strategy: 'file-hash'
  },
  shared: {
    cache: 'shared/.cache',
    strategy: 'dependency-graph'
  }
};

// Cache implementation
const cache = new BuildCache(cacheConfig);
const cacheKey = generateCacheKey(dependencies, sourceFiles);
const cachedResult = cache.get(cacheKey);
```

**💬 Explanation + Insight**

- **Build Performance** - Faster builds through caching
- **Dependency Caching** - Cache node_modules and dependencies
- **Output Caching** - Cache build outputs
- **Shared Caching** - Share cache across projects
- **Use Cases** - Large monorepos, multiple teams

---

### 109. 🧩 What are pre-commit hooks, and how do you integrate Husky with lint-staged?

**🧠 Concept**

Pre-commit hooks run checks before commits, ensuring code quality and preventing bad code from entering the repository.

**💻 Example**

```javascript
// Husky pre-commit hook
// .husky/pre-commit
#!/usr/bin/env sh
. "$(dirname -- "$0")/_/husky.sh"

npx lint-staged

// lint-staged configuration
// package.json
{
  "lint-staged": {
    "*.{js,jsx,ts,tsx}": [
      "eslint --fix",
      "prettier --write"
    ],
    "*.{css,scss}": [
      "stylelint --fix"
    ]
  }
}
```

**💬 Explanation + Insight**

- **Code Quality** - Ensure code quality before commits
- **Automated Checks** - Run linting and formatting
- **Prevention** - Prevent bad code from entering repo
- **Team Standards** - Enforce team coding standards
- **Use Cases** - Team development, code quality assurance

---

### 110. 🧩 What are common bottlenecks in CI/CD pipelines for frontend teams?

**🧠 Concept**

Frontend CI/CD bottlenecks include slow builds, dependency installation, testing, and deployment processes that can be optimized.

**💻 Example**

```javascript
// Common bottlenecks and solutions
const bottlenecks = {
  slowBuilds: {
    problem: 'Large bundle sizes, complex builds',
    solution: 'Code splitting, build optimization'
  },
  dependencyInstall: {
    problem: 'Slow npm/yarn install',
    solution: 'Caching, lock files, faster package managers'
  },
  testing: {
    problem: 'Slow test execution',
    solution: 'Parallel testing, test optimization'
  },
  deployment: {
    problem: 'Slow deployment process',
    solution: 'CDN deployment, incremental builds'
  }
};
```

**💬 Explanation + Insight**

- **Build Performance** - Optimize build processes
- **Dependency Management** - Cache and optimize dependencies
- **Testing** - Parallel and optimize testing
- **Deployment** - Streamline deployment processes
- **Use Cases** - Large teams, performance optimization

---

*This comprehensive frontend infrastructure section covers all essential concepts including CI/CD pipelines, deployment strategies, security, versioning, and optimization techniques for building robust frontend delivery systems.*