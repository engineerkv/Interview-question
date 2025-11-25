# Section 10: Git, Docker, CI/CD, Tooling (Q191-Q210)

<div align="center">

**[← Previous: Communication Protocols](9%29%20Communication%20Protocols.md)** | **[Next: AI Tools →](11%29%20AI%20Tools.md)**

</div>

---

## Q191. Git merge vs rebase

Git merge creates a merge commit that combines two branches, preserving the history of both branches - the branch history shows when branches diverged and merged. Git rebase replays commits from one branch onto another, creating a linear history without merge commits - it rewrites commit history to make it look like work happened sequentially. Use merge to preserve branch history, use rebase to keep history clean and linear.

- **Trade-offs**: Merge preserves complete history which is good for understanding when branches were created and merged, but the catch is it creates merge commits that can clutter history. Rebase creates cleaner, linear history which is easier to read, but the tricky part is it rewrites history which can cause issues if others have based work on the rebased commits - never rebase shared branches.

---

## Q192. Git cherry-pick

Git cherry-pick applies a specific commit from one branch to another branch - you select a commit by hash and apply its changes to your current branch. This is useful for applying bug fixes or features from one branch to another without merging the entire branch. Cherry-pick creates a new commit with the same changes but a different commit hash.

- **Trade-offs**: Cherry-pick allows you to selectively apply commits, which is useful for hotfixes or backporting features, but the catch is it creates duplicate commits with different hashes, which can cause confusion. The tricky part is if the commit depends on other commits, you might need to cherry-pick multiple commits or resolve conflicts.

---

## Q193. Fixing merge conflicts

Fix merge conflicts by opening conflicted files, finding conflict markers (<<<<<<, ======, >>>>>>), and manually resolving which changes to keep. Edit the file to remove conflict markers and keep the desired code, then stage the resolved file and commit. Use merge tools or IDE features to help visualize and resolve conflicts. For complex conflicts, communicate with the other developer to understand the changes.

- **Trade-offs**: Manual conflict resolution gives you control over the final code, but the catch is it's time-consuming and error-prone, especially for large conflicts. The tricky part is understanding both sets of changes - you need to understand what each side was trying to do to resolve conflicts correctly, not just pick one side arbitrarily.

---

## Q194. GitFlow vs trunk-based development

GitFlow uses multiple long-lived branches - main for production, develop for integration, feature branches for new work, release branches for preparing releases, and hotfix branches for urgent fixes. Trunk-based development uses a single main branch where everyone commits frequently, with short-lived feature branches that are merged quickly. GitFlow provides more structure, trunk-based enables faster integration.

- **Trade-offs**: GitFlow provides clear branching structure and separation of concerns, but the catch is it's more complex and can slow down integration since features stay in branches longer. Trunk-based development enables faster integration and fewer merge conflicts, but the tricky part is it requires discipline - everyone needs to commit frequently and keep the main branch stable.

---

## Q195. Docker image vs container

A Docker image is a read-only template that defines how to create a container - it contains the application code, dependencies, and configuration. A container is a running instance of an image - when you run an image, Docker creates a container with a writable layer on top of the image. You can have multiple containers running from the same image, each with its own state.

- **Trade-offs**: Images are immutable and can be versioned and shared, which is great for consistency, but the catch is you need to rebuild images when code changes. Containers are ephemeral and can be created and destroyed easily, but the tricky part is any changes made to a running container are lost when it's removed, unless you commit them to a new image.

---

## Q196. Docker multi-stage builds

Docker multi-stage builds use multiple FROM statements in one Dockerfile, allowing you to use different base images for building and running - like using a large image with build tools to compile code, then copying only the compiled artifacts to a smaller runtime image. This reduces final image size by excluding build tools and dependencies that aren't needed at runtime.

- **Trade-offs**: Multi-stage builds significantly reduce image size, which improves deployment speed and reduces storage costs, but the catch is they make Dockerfiles more complex. The tricky part is understanding what to copy between stages - you need to copy only what's needed for runtime, not build artifacts or source code.

Example:

```dockerfile
# Build stage
FROM node:18 AS builder
WORKDIR /app
COPY package*.json ./
RUN npm install
COPY . .
RUN npm run build

# Runtime stage
FROM node:18-alpine
WORKDIR /app
COPY --from=builder /app/dist ./dist
COPY --from=builder /app/node_modules ./node_modules
CMD ["node", "dist/index.js"]
```

---

## Q197. Reducing Docker image size

Reduce Docker image size by using smaller base images (like Alpine Linux), using multi-stage builds to exclude build tools, removing unnecessary files and dependencies, combining RUN commands to reduce layers, and using .dockerignore to exclude files from the build context. Avoid installing unnecessary packages, clean up package caches, and only copy files needed for runtime.

- **Trade-offs**: Smaller images deploy faster and use less storage, which improves performance and reduces costs, but the catch is some optimizations can make builds slower or more complex. The tricky part is balancing image size with build time and maintainability - very aggressive size reduction can make Dockerfiles harder to understand.

---

## Q198. Docker Compose use cases

Use Docker Compose to define and run multi-container applications locally - you define services, networks, and volumes in a YAML file, and Compose starts all containers together. Use it for local development environments, testing multi-service applications, or running services that depend on each other. Compose simplifies managing multiple containers and their relationships.

- **Trade-offs**: Docker Compose makes it easy to run complex applications locally, which is great for development, but the catch is it's designed for single-machine deployment, not production clusters. The tricky part is it doesn't handle scaling or high availability - for production, you need Kubernetes or similar orchestration.

---

## Q199. Securing secrets in Docker

Secure secrets in Docker by using Docker secrets (in Swarm mode), mounting secrets as files instead of environment variables, using secret management services like AWS Secrets Manager, or using build-time secrets with BuildKit. Never hardcode secrets in Dockerfiles or commit them to version control. Use environment variables for non-sensitive config, secrets services for sensitive data.

- **Trade-offs**: Proper secret management prevents credential leaks, which is critical for security, but the catch is it adds complexity - you need to integrate with secret management services and handle secret rotation. The tricky part is balancing security with usability - too complex and developers might bypass it, too simple and secrets might be exposed.

---

## Q200. Kubernetes vs Docker differences

Docker is a containerization platform that packages applications into containers - it runs containers on a single machine. Kubernetes is an orchestration platform that manages containers across multiple machines - it handles scheduling, scaling, load balancing, and self-healing. Docker creates and runs containers, Kubernetes manages containerized applications at scale.

- **Trade-offs**: Docker is simpler and great for single-machine deployment or development, but the catch is it doesn't handle scaling, load balancing, or high availability. Kubernetes provides orchestration features for production deployments, but the tricky part is it's complex and has a steep learning curve - you need to understand pods, services, deployments, and more.

---

## Q201. CI/CD pipeline stages

CI/CD pipelines typically have stages like build (compile code, run tests), test (unit tests, integration tests), security scan (vulnerability scanning, code analysis), deploy to staging (deploy to test environment), integration tests (end-to-end tests), and deploy to production (deploy to live environment). Each stage runs automatically when the previous stage succeeds, and failures stop the pipeline.

- **Trade-offs**: Automated pipelines catch issues early and enable fast deployments, which is great, but the catch is you need to maintain and update pipelines as your application evolves. The tricky part is balancing speed with thoroughness - too many stages and deployments are slow, too few and you might miss issues.

---

## Q202. Blue-green vs canary deployments

Blue-green deployment runs two identical production environments and switches traffic from one to the other - you deploy new version to green, test it, then switch all traffic. Canary deployment gradually routes traffic to the new version - you deploy new version alongside old, route 10% of traffic to new version, monitor, then gradually increase to 100%. Blue-green is faster, canary is safer.

- **Trade-offs**: Blue-green deployments are faster and provide instant rollback, but the catch is you need double the infrastructure and all users switch at once, so issues affect everyone. Canary deployments reduce risk by testing with a small percentage of users first, but the tricky part is they're more complex and take longer to complete the rollout.

---

## Q203. Zero-downtime deployment techniques

Achieve zero-downtime deployments by using rolling updates (replace instances gradually), blue-green deployments (switch traffic instantly), or canary deployments (gradually route traffic). Use health checks to ensure new instances are ready before routing traffic, drain connections from old instances gracefully, and ensure backward compatibility so both versions can run simultaneously.

- **Trade-offs**: Zero-downtime deployments improve user experience and enable continuous deployment, but the catch is they require careful planning - you need health checks, graceful shutdowns, and backward compatibility. The tricky part is handling stateful services - databases and sessions need special handling during deployments.

---

## Q204. Postman automated testing

Postman automated testing allows you to write test scripts that run after API requests - you can validate responses, check status codes, verify response times, and chain requests together. Use Postman collections to organize tests, run them in CI/CD pipelines, and use environments to test against different stages. Tests run automatically and can be integrated into your deployment process.

- **Trade-offs**: Automated API testing catches regressions early and ensures APIs work correctly, which is great, but the catch is you need to maintain tests as APIs evolve. The tricky part is writing good tests - you need to test both happy paths and error cases, and tests need to be independent and idempotent.

---

## Q205. npm vs Yarn differences

npm is Node.js's default package manager that comes with Node.js, while Yarn is an alternative package manager created by Facebook. Yarn was faster and had better dependency resolution, but modern npm has caught up. Yarn uses yarn.lock, npm uses package-lock.json. Both work similarly, but Yarn has some features like workspaces and better offline support.

- **Trade-offs**: npm is built-in and widely used, which is convenient, but the catch is it was historically slower and had dependency resolution issues. Yarn provides better performance and features, but the tricky part is you need to install it separately and teams need to agree on which to use. Modern npm is competitive, so the choice is often based on team preference.

---

## Q206. package-lock.json vs yarn.lock

package-lock.json is npm's lock file that locks exact versions of all dependencies and their dependencies, ensuring consistent installs across environments. yarn.lock is Yarn's equivalent lock file that serves the same purpose. Both ensure that `npm install` or `yarn install` produces the same dependency tree every time, regardless of when or where it runs.

- **Trade-offs**: Lock files ensure consistent dependency versions, which prevents "works on my machine" issues, but the catch is you need to commit them to version control and update them when dependencies change. The tricky part is merge conflicts - lock files can have conflicts when multiple people update dependencies, and resolving them can be tedious.

---

## Q207. Peer dependencies in npm

Peer dependencies are dependencies that your package expects the consuming application to provide - like a React component library that expects React to be installed by the app using it, not bundled with the library. This prevents multiple versions of the same dependency from being installed, which is important for libraries that need to share a single instance of a dependency.

- **Trade-offs**: Peer dependencies prevent duplicate installations and version conflicts, which is good, but the catch is they require the consuming application to install the peer dependency, which can cause issues if versions don't match. The tricky part is version ranges - you need to specify compatible versions, but too strict and you break compatibility, too loose and you might get incompatible versions.

---

## Q208. Solving dependency conflicts

Solve dependency conflicts by updating packages to compatible versions, using npm's dependency resolution (npm tries to find compatible versions), using `npm install --force` or `--legacy-peer-deps` to bypass conflicts (not recommended), or using package managers that handle conflicts better. Check which packages require conflicting versions, update them if possible, or use resolutions/overrides to force specific versions.

- **Trade-offs**: Resolving conflicts properly ensures compatibility and prevents runtime issues, but the catch is it can be time-consuming and might require updating multiple packages. The tricky part is understanding the dependency tree - conflicts can be deep in the dependency chain, so you need to trace which packages are causing conflicts and why.

---

## Q209. Node.js performance debugging tools

Use Node.js performance debugging tools like the built-in profiler (`--prof`), Chrome DevTools for CPU profiling, `clinic.js` for performance analysis, or `0x` for flame graphs. Use `process.memoryUsage()` to monitor memory, `console.time()` for timing, and APM tools like New Relic or DataDog for production monitoring. Identify bottlenecks by profiling CPU usage, memory leaks, or slow operations.

- **Trade-offs**: Performance tools help you identify and fix bottlenecks, which is essential for optimization, but the catch is they add overhead and can slow down your application during profiling. The tricky part is interpreting the results - you need to understand what the tools are showing you to identify the actual problems, not just symptoms.

---

## Q210. Postman environments vs globals

Postman environments are sets of variables scoped to a specific environment - like development, staging, or production - where you can define different values for the same variable name (like different API URLs). Globals are variables available across all requests regardless of environment. Use environments for environment-specific config, use globals for values that are the same everywhere.

- **Trade-offs**: Environments enable testing against different stages without changing requests, which is convenient, but the catch is you need to manage multiple environment files. Globals are simpler but less flexible - they're the same everywhere, so you can't have different values per environment. The tricky part is knowing when to use each - use environments for URLs, API keys per environment, globals for constants.

---

<div align="center">

**[← Previous: Communication Protocols](9%29%20Communication%20Protocols.md)** | **[Next: AI Tools →](11%29%20AI%20Tools.md)**

</div>
