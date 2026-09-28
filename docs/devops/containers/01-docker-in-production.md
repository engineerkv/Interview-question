---
sidebar_position: 1
sidebar_label: "Docker in Production"
description: "Images, layers, multi-stage builds, image security, non-root users, Compose, secrets, registries and healthchecks."
---

# Docker in Production

> **Reviewed:** 2026-09 · **Level:** Senior / Tech Lead · **Type:** Foundational

Short introductions to image vs container, multi-stage builds, image size and Compose also exist in [Git, Docker, CI/CD, Tooling](../ci-cd-and-releases/01-git-docker-ci-cd-tooling.md). This page goes one level deeper, towards what you would defend in a production review.

---

## Q1. What is the difference between an image and a container, and what is a container really?

**Short answer:** An image is an immutable, layered filesystem snapshot plus metadata (entrypoint, env, exposed ports). A container is a running process started from that image, with a thin writable layer on top. Under the hood a container is just a Linux process isolated with **namespaces** (what it can see) and limited with **cgroups** (what it can use) — it is not a VM and shares the host kernel.

**How it works:**

- **Namespaces:** PID, network, mount, UTS, IPC, user — the process gets its own view of these.
- **cgroups:** limit CPU, memory, I/O. When a container exceeds its memory limit, the kernel OOM-kills it.
- **Union filesystem (overlayfs):** stacks read-only image layers with a writable container layer.
- **OCI standards:** image format and runtime spec, so images built by Docker run on containerd, CRI-O, Podman, etc.

| | VM | Container |
| --- | --- | --- |
| Isolation | Hardware virtualisation, own kernel | Kernel namespaces, shared kernel |
| Startup | Slower (boots an OS) | Fast (starts a process) |
| Size | Includes full OS | Only app + userland it needs |
| Security boundary | Stronger | Weaker; harden with non-root, seccomp, sandboxed runtimes |

<details>
<summary>Follow-up questions</summary>

- Why does a container's data disappear when it is removed?
- What happens when PID 1 inside a container doesn't handle SIGTERM?
- What are gVisor or Kata Containers used for?

</details>

**Remember:** A container is an isolated, resource-limited process; an image is its immutable template.

---

## Q2. How do image layers and build caching work, and how do you order a Dockerfile?

**Short answer:** Each filesystem-changing instruction (`RUN`, `COPY`, `ADD`) creates a layer. Docker reuses a cached layer if the instruction and its inputs haven't changed; once one layer changes, every layer after it is rebuilt. So I order instructions from least to most frequently changing: base image, system packages, dependency manifests, dependency install, then source code.

**How it works:** For `COPY`, the cache key includes the checksum of the copied files. Copying the whole repo before `npm ci` means any source change reinstalls all dependencies.

**Example:**

```dockerfile
# Bad: any code change invalidates the dependency install
COPY . .
RUN npm ci

# Good: dependencies are cached until package*.json changes
COPY package.json package-lock.json ./
RUN npm ci
COPY . .
```

**Trade-offs and pitfalls:**

- Combine `apt-get update` and `apt-get install` in one `RUN`, otherwise a stale cached `update` layer is reused.
- Deleting files in a later layer does **not** shrink the image — the data still exists in the earlier layer.
- In CI, caches are empty on fresh runners; use BuildKit cache export/import (for example registry or CI cache backends).
- Use a `.dockerignore` to keep `node_modules`, `.git` and local env files out of the build context.

<details>
<summary>Follow-up questions</summary>

- Why is my CI Docker build slow even though it's fast locally?
- What are BuildKit cache mounts (`RUN --mount=type=cache`)?

</details>

**Remember:** Order from stable to volatile; a changed layer rebuilds everything below it.

---

## Q3. Walk me through a production-grade Dockerfile.

**Short answer:** Multi-stage build, pinned small base image, dependency layer cached separately, production-only dependencies, non-root user, a proper init/signal handling story, a healthcheck, and no secrets baked in.

**Example (Node.js service):**

```dockerfile
# syntax=docker/dockerfile:1

# ---- Stage 1: install all deps and build ----
FROM node:20-bookworm-slim AS build
WORKDIR /app
# Copy manifests first so the install layer is cached
COPY package.json package-lock.json ./
RUN npm ci
COPY . .
RUN npm run build && npm prune --omit=dev   # drop devDependencies after build

# ---- Stage 2: minimal runtime ----
FROM node:20-bookworm-slim AS runtime
ENV NODE_ENV=production
WORKDIR /app

# Copy only what the app needs at runtime, owned by the non-root user
COPY --from=build --chown=node:node /app/node_modules ./node_modules
COPY --from=build --chown=node:node /app/dist ./dist
COPY --from=build --chown=node:node /app/package.json ./

# The official Node image ships a non-root "node" user
USER node
EXPOSE 3000

# Docker-level healthcheck (Kubernetes ignores this and uses probes instead)
HEALTHCHECK --interval=30s --timeout=3s --retries=3 \
  CMD node -e "fetch('http://localhost:3000/healthz').then(r=>process.exit(r.ok?0:1)).catch(()=>process.exit(1))"

# Exec form so node is PID 1 and receives SIGTERM directly
CMD ["node", "dist/server.js"]
```

**How it works:** The build stage has compilers, dev dependencies and source; the runtime stage only receives build outputs. In production you would often pin the base image by digest (`node:20-bookworm-slim@sha256:...`) for reproducibility, and let a bot (Renovate/Dependabot) bump it.

**Trade-offs and pitfalls:**

- Shell form (`CMD node server.js`) runs under `/bin/sh`, which may not forward signals — graceful shutdown breaks.
- If your app spawns child processes, use a tiny init (`docker run --init` or `tini`) to reap zombies.
- Distroless or scratch images are smaller but have no shell, which makes debugging harder (use ephemeral debug containers).

<details>
<summary>Follow-up questions</summary>

- Why pin by digest rather than by tag?
- How would this differ for a Go binary? (static binary on `scratch` or distroless)

</details>

**Remember:** Build fat, ship thin, run as non-root, handle signals.

---

## Q4. How do you reduce image size and attack surface?

**Short answer:** Start from a minimal base (slim, Alpine, or distroless), use multi-stage builds, install only production dependencies, remove package manager caches in the same layer, and keep the build context small. Smaller images pull faster and contain fewer packages that scanners will flag.

**How it works:**

| Base | Pros | Cons |
| --- | --- | --- |
| Full Debian/Ubuntu | Familiar, easy debugging | Large, many CVEs to triage |
| `-slim` variants | Good balance, glibc | Still has a shell and package manager |
| Alpine | Very small | musl libc can cause native-module or DNS behaviour differences |
| Distroless | Minimal, no shell | Harder to debug; needs debug containers |
| `scratch` | Nothing at all | Only for static binaries |

**Trade-offs and pitfalls:** Size is a proxy, not the goal. The goal is fewer vulnerable packages and faster deploys. Don't switch to Alpine blindly for Node/Python apps with native extensions.

<details>
<summary>Follow-up questions</summary>

- A scanner reports 200 CVEs in your base image. How do you prioritise?
- How do you debug a distroless container in production?

</details>

**Remember:** Minimal base + multi-stage + prod-only deps = smaller and safer.

---

## Q5. Why run containers as non-root, and what else hardens a container?

**Short answer:** By default a container process runs as root (UID 0). If an attacker escapes the app or the container, root makes everything worse. Run as a non-root user, use a read-only root filesystem, drop Linux capabilities, block privilege escalation, and never run `--privileged` unless there is a very specific reason.

**Example (runtime flags):**

```bash
docker run \
  --user 10001:10001 \
  --read-only --tmpfs /tmp \
  --cap-drop ALL \
  --security-opt no-new-privileges \
  myapp:1.4.2
```

The Kubernetes equivalent is a `securityContext` (see [Kubernetes Architecture & Workloads](../orchestration/01-kubernetes-architecture-and-workloads.md)).

**Trade-offs and pitfalls:** Non-root users can't bind to ports below 1024 by default — listen on 8080/3000 and map ports. Mounting the Docker socket (`/var/run/docker.sock`) into a container effectively gives it root on the host.

<details>
<summary>Follow-up questions</summary>

- What are rootless Docker and user namespaces?
- Why is mounting the Docker socket dangerous?

</details>

**Remember:** Non-root, read-only, no extra capabilities, never privileged by default.

---

## Q6. How do you use Docker Compose for local development?

**Short answer:** Compose describes a multi-container app in one YAML file — app, database, cache, queue — so any engineer can run `docker compose up` and get a working environment. It is great for local dev and integration tests, but it is not a production orchestrator for multi-node workloads.

**Example:**

```yaml
# compose.yaml
services:
  api:
    build: .
    ports:
      - "3000:3000"
    environment:
      DATABASE_URL: postgres://app:app@db:5432/app   # "db" resolves via Compose DNS
      REDIS_URL: redis://cache:6379
    depends_on:
      db:
        condition: service_healthy   # wait until the DB healthcheck passes
    volumes:
      - ./src:/app/src               # bind mount for hot reload in dev

  db:
    image: postgres:16
    environment:
      POSTGRES_USER: app
      POSTGRES_PASSWORD: app         # local-only credentials
      POSTGRES_DB: app
    healthcheck:
      test: ["CMD-SHELL", "pg_isready -U app"]
      interval: 5s
      retries: 10
    volumes:
      - pgdata:/var/lib/postgresql/data

  cache:
    image: redis:7

volumes:
  pgdata:
```

**Trade-offs and pitfalls:**

- `depends_on` without a health condition only waits for the container to *start*, not to be *ready*.
- Bind mounts on macOS/Windows can be slow for large dependency trees.
- Keep dev and prod images close; a dev-only image that diverges hides bugs.

<details>
<summary>Follow-up questions</summary>

- How would you use Compose in CI for integration tests?
- When would you choose a local Kubernetes (kind, minikube) over Compose?

</details>

**Remember:** Compose makes local environments reproducible; it is not your production platform.

---

## Q7. How do you handle secrets with containers?

**Short answer:** Never bake secrets into images — anyone who can pull the image can read every layer. Inject them at runtime from a secret manager (AWS Secrets Manager, GCP Secret Manager, Azure Key Vault, Vault) via the orchestrator. For build-time secrets such as a private registry token, use BuildKit secret mounts so they never land in a layer.

**Example:**

```dockerfile
# Build-time secret: available only during this RUN, not stored in the image
RUN --mount=type=secret,id=npm_token \
    NPM_TOKEN=$(cat /run/secrets/npm_token) npm ci
```

```bash
docker build --secret id=npm_token,env=NPM_TOKEN -t myapp .
```

**Trade-offs and pitfalls:**

- `ARG` and `ENV` values are visible in image history/metadata — not safe for secrets.
- Environment variables are convenient but can leak via crash dumps or debug endpoints; mounted files are often safer.
- Prefer short-lived, identity-based credentials (IAM roles for workloads) over static keys.

<details>
<summary>Follow-up questions</summary>

- How do you rotate a database password without downtime?
- How do you verify an image doesn't contain secrets? (scanners in CI)

</details>

**Remember:** Secrets are injected at runtime, never built into layers.

---

## Q8. What should you know about container registries and image tagging?

**Short answer:** A registry (ECR, Artifact Registry, ACR, GHCR, Docker Hub, Harbor) stores and distributes images. In production I tag images immutably (commit SHA or version), deploy by digest where possible, enable immutable tags and vulnerability scanning, and set lifecycle policies to delete old images.

**How it works:** A tag is a mutable pointer; a digest (`sha256:...`) identifies exact content. `latest` tells you nothing about what is running and makes rollbacks ambiguous.

**Example tagging scheme:**

```text
registry.example.com/orders-api:3f9c2a1          # git SHA, immutable
registry.example.com/orders-api:1.8.0            # release version
registry.example.com/orders-api@sha256:ab12...   # what the cluster actually runs
```

**Trade-offs and pitfalls:** Public registry rate limits can break CI — mirror or cache base images. Pull-through caches and private registries also reduce supply-chain risk.

<details>
<summary>Follow-up questions</summary>

- Why is deploying `:latest` a bad idea?
- How do you promote the same image from staging to production?

</details>

**Remember:** Build once, tag immutably, deploy by digest.

---

## Q9. What is a container healthcheck and how does it relate to orchestrator probes?

**Short answer:** A Docker `HEALTHCHECK` periodically runs a command and marks the container healthy or unhealthy; Compose and Swarm can act on it. Kubernetes ignores Dockerfile healthchecks and uses its own liveness, readiness and startup probes instead. Either way, the endpoint should be cheap and reflect whether *this process* can serve traffic.

**How it works:** A good health endpoint checks the process is responsive. Be careful about checking downstream dependencies in a liveness check — if the database is down, restarting every app container won't fix it and can cause a restart storm.

<details>
<summary>Follow-up questions</summary>

- What's the difference between "alive" and "ready"?
- Should a health endpoint call the database?

</details>

**Remember:** Health checks answer "is this process OK?", not "is the whole world OK?".

---

## Q10. How do you make containers shut down gracefully?

**Short answer:** On stop, the runtime sends SIGTERM to PID 1, waits for a grace period (10s by default in Docker, 30s by default in Kubernetes), then sends SIGKILL. The app must catch SIGTERM, stop accepting new work, finish in-flight requests, close connections, and exit.

**Example:**

```js
// Node.js: drain HTTP connections on SIGTERM
const server = app.listen(3000);
process.on('SIGTERM', () => {
  server.close(() => {        // stop accepting new connections, finish in-flight ones
    db.end().then(() => process.exit(0));
  });
  setTimeout(() => process.exit(1), 25_000).unref(); // hard stop before SIGKILL
});
```

**Trade-offs and pitfalls:** Shell-form `CMD` or wrapper scripts that don't `exec` swallow signals. Long-running jobs need checkpointing or a longer grace period.

<details>
<summary>Follow-up questions</summary>

- Why do some requests fail during a rolling update even with graceful shutdown? (endpoint removal race; add a short pre-stop delay)

</details>

**Remember:** Catch SIGTERM, drain, exit before the grace period ends.

---

## References

- [Docker documentation](https://docs.docker.com/)
- [Dockerfile reference](https://docs.docker.com/reference/dockerfile/)
- [Docker Compose documentation](https://docs.docker.com/compose/)
- [Open Container Initiative](https://opencontainers.org/)
- [OWASP Docker Security Cheat Sheet](https://cheatsheetseries.owasp.org/cheatsheets/Docker_Security_Cheat_Sheet.html)
