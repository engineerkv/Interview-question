---
sidebar_position: 2
sidebar_label: "Operations & Debugging"
description: "Namespaces and RBAC, rolling updates and rollback, debugging CrashLoopBackOff, OOMKilled and Pending pods, disruption budgets and managed Kubernetes trade-offs."
---

# Kubernetes Operations & Debugging

> **Reviewed:** 2026-09 · **Level:** Senior / Tech Lead · **Type:** Foundational

These are the questions that separate "I've used Kubernetes" from "I've run Kubernetes in production". Core objects are covered in [Kubernetes Architecture & Workloads](./01-kubernetes-architecture-and-workloads.md).

---

## Q1. How do namespaces and RBAC work together for multi-team clusters?

**Short answer:** Namespaces are logical partitions for names, policies and quotas — they are **not** a hard security boundary on their own. RBAC grants permissions: a **Role** (namespaced) or **ClusterRole** (cluster-wide) lists allowed verbs on resources, and a **RoleBinding** or **ClusterRoleBinding** attaches it to users, groups or ServiceAccounts. For multi-team clusters I combine namespaces with RBAC, ResourceQuotas, LimitRanges, NetworkPolicies and Pod Security admission.

**Example:**

```yaml
apiVersion: rbac.authorization.k8s.io/v1
kind: Role
metadata:
  name: deployer
  namespace: team-orders
rules:
  - apiGroups: ["apps"]
    resources: ["deployments"]
    verbs: ["get", "list", "watch", "update", "patch"]
  - apiGroups: [""]
    resources: ["pods", "pods/log"]
    verbs: ["get", "list", "watch"]
---
apiVersion: rbac.authorization.k8s.io/v1
kind: RoleBinding
metadata:
  name: orders-ci-deployer
  namespace: team-orders
subjects:
  - kind: ServiceAccount
    name: ci-deployer
    namespace: team-orders
roleRef:
  kind: Role
  name: deployer
  apiGroup: rbac.authorization.k8s.io
```

**Trade-offs and pitfalls:**

- RBAC is additive only — there are no "deny" rules. Start from nothing and add.
- Granting `secrets: get` on a namespace means reading every secret in it.
- `cluster-admin` for CI pipelines is a common and dangerous shortcut.
- Pods get a ServiceAccount token by default; disable automounting for workloads that don't call the API.
- For strong isolation between untrusted tenants, separate clusters are often simpler than soft multi-tenancy.

<details>
<summary>Follow-up questions</summary>

- How do you check what a ServiceAccount can do? (`kubectl auth can-i --as=system:serviceaccount:ns:name ...`)
- How do cloud IAM identities map to Kubernetes (IRSA / EKS Pod Identity, GKE Workload Identity, AKS Workload Identity)?

</details>

**Remember:** Namespaces organise; RBAC, quotas and network policies actually isolate.

---

## Q2. How do rolling updates and rollbacks work in a Deployment?

**Short answer:** Changing the Pod template creates a new ReplicaSet. The Deployment scales the new one up and the old one down step by step, controlled by `maxSurge` (extra Pods allowed) and `maxUnavailable` (Pods allowed to be missing). New Pods only count once they are Ready. Rollback with `kubectl rollout undo` scales an older ReplicaSet back up — but in a GitOps setup the real rollback is reverting the commit.

**Example:**

```yaml
spec:
  replicas: 6
  revisionHistoryLimit: 5
  progressDeadlineSeconds: 600    # mark rollout failed if no progress in 10 min
  minReadySeconds: 10             # Pod must stay Ready 10s before it counts
  strategy:
    type: RollingUpdate
    rollingUpdate:
      maxSurge: 25%
      maxUnavailable: 0           # never go below desired capacity
```

```bash
kubectl rollout status deployment/orders          # wait and watch
kubectl rollout history deployment/orders         # list revisions
kubectl rollout undo deployment/orders            # back to previous revision
kubectl rollout undo deployment/orders --to-revision=3
```

**Trade-offs and pitfalls:**

- Kubernetes does not auto-rollback a failed rollout; it just stops progressing. Automated rollback needs a tool (Argo Rollouts, Flagger) or pipeline logic.
- Old and new versions run side by side — APIs, events and database schemas must be backward compatible (see expand/contract in [Pipeline Design & Release Strategies](../ci-cd-and-releases/02-pipeline-design-and-release-strategies.md)).
- `kubectl rollout undo` makes the cluster drift from Git in a GitOps setup.
- Add a short `preStop` sleep so load balancers stop sending traffic before the app starts shutting down.

<details>
<summary>Follow-up questions</summary>

- How would you implement a canary on Kubernetes?
- Why do some requests still fail during a rolling update?

</details>

**Remember:** New ReplicaSet up, old down, gated by readiness; rollback means going back to an older ReplicaSet or an older commit.

---

## Q3. A Pod is in CrashLoopBackOff. How do you debug it?

**Short answer:** CrashLoopBackOff means the container starts, exits, and the kubelet keeps restarting it with increasing back-off delays. I check the exit code and last state with `describe`, read the **previous** container's logs, and then work through the usual causes: bad config or missing secret, app crash on startup, failing liveness probe, wrong command, or a dependency that isn't reachable.

**How it works (walkthrough):**

```bash
kubectl get pods -n team-orders
kubectl describe pod orders-7d9f-abc -n team-orders
#   Look at: Last State (Reason, Exit Code), Events, probe failures
kubectl logs orders-7d9f-abc -n team-orders --previous   # logs from the crashed run
kubectl get events -n team-orders --sort-by=.lastTimestamp
```

| Exit code / signal | Usual meaning |
| --- | --- |
| 1 (or other app code) | Application error — read the logs |
| 127 | Command not found — wrong entrypoint or missing binary |
| 126 | Command not executable — permissions |
| 137 | SIGKILL — often OOMKilled or killed after a failed liveness probe |
| 143 | SIGTERM — asked to stop (probe failure or shutdown) |

**Next steps:**

- Missing env var or Secret → check `envFrom` references and that the Secret exists in the same namespace.
- Liveness killing a slow start → add a startup probe.
- Need a shell but the image is distroless → `kubectl debug -it pod/orders-7d9f-abc --image=busybox --target=orders`.
- Reproduce locally with the same image and env.

<details>
<summary>Follow-up questions</summary>

- How do you tell a liveness-probe kill apart from an app crash? (events show "Liveness probe failed")
- The logs are empty. What next?

</details>

**Remember:** `describe` for the reason, `logs --previous` for the story, exit code for the category.

---

## Q4. A Pod keeps getting OOMKilled. What do you do?

**Short answer:** OOMKilled means the container went over its memory limit and the kernel killed it (exit code 137). First I decide whether it is a genuine need (limit too low for real workload) or a leak (memory grows until killed regardless of load). Then I either right-size the limit, fix the runtime heap configuration, or find the leak with profiling.

**How it works:**

1. Confirm: `kubectl describe pod` shows `Last State: Terminated, Reason: OOMKilled`.
2. Look at memory graphs over time: a sawtooth that climbs steadily then drops at each restart suggests a leak; a spike under load suggests under-sizing or unbounded buffering.
3. Check the runtime: is the heap limit aligned with the container limit? (For Node, `--max-old-space-size` should leave headroom for native memory and buffers; modern JVMs read container limits and can be tuned with `-XX:MaxRAMPercentage`.)
4. Check for unbounded work: loading whole files into memory, large query results, in-memory caches without eviction.
5. Profile: heap snapshots in staging, or continuous profiling in production.

**Trade-offs and pitfalls:** Simply doubling the limit hides leaks and costs money. Node-level OOM (the node itself running out) evicts Pods differently — BestEffort and Burstable Pods go first.

<details>
<summary>Follow-up questions</summary>

- Difference between OOMKilled and Evicted?
- How would you use streaming to reduce memory for a large export endpoint?

</details>

**Remember:** OOMKilled = over the memory limit; decide leak vs sizing before changing numbers.

---

## Q5. A Pod is stuck in Pending. What are the common causes?

**Short answer:** Pending means the scheduler cannot place the Pod, or it's waiting on something like a volume. `kubectl describe pod` almost always tells you why in the Events: insufficient CPU/memory (based on **requests**), node selector or affinity mismatch, taints without tolerations, unbound PVC or zone conflict, or quota exceeded.

| Event message (paraphrased) | Cause | Fix |
| --- | --- | --- |
| Insufficient cpu / memory | Requests don't fit on any node | Lower requests, add nodes, check autoscaler |
| Node(s) didn't match node selector/affinity | Labels don't match | Fix selector or label nodes |
| Node(s) had untolerated taint | Dedicated nodes (GPU, system) | Add toleration or use other nodes |
| Unbound PersistentVolumeClaim | No StorageClass or provisioning failing | Check StorageClass and CSI driver |
| Volume node affinity conflict | Disk in another zone | Schedule in the right zone; `WaitForFirstConsumer` |
| Exceeded quota | Namespace ResourceQuota full | Raise quota or clean up |

Also note: `ContainerCreating` or `ImagePullBackOff` are different states — the Pod *was* scheduled but can't start (image name/tag wrong, registry auth, volume mount failing).

<details>
<summary>Follow-up questions</summary>

- Cluster Autoscaler is enabled but Pods remain Pending. Why? (max nodes reached, instance type too small for the request, zone constraints)
- How do PriorityClasses and preemption affect Pending Pods?

</details>

**Remember:** Pending is a scheduling problem; the answer is in `describe` events.

---

## Q6. A Service returns errors or times out but the Pods look healthy. How do you debug it?

**Short answer:** I follow the request path hop by hop: DNS resolves → Service has endpoints → Pods are Ready and listening on the `targetPort` → NetworkPolicy allows the traffic → Ingress routes to the right Service and port. Most issues are label mismatches, wrong ports, readiness failures or network policies.

**Walkthrough:**

```bash
kubectl get endpointslices -l kubernetes.io/service-name=orders -n team-orders  # empty = selector mismatch or no Ready Pods
kubectl get svc orders -n team-orders -o yaml          # check selector, port, targetPort
kubectl port-forward pod/orders-7d9f-abc 8080:8080 -n team-orders   # bypass Service; test the Pod directly
kubectl run tmp --rm -it --image=busybox -n team-orders -- wget -qO- http://orders/healthz  # test from inside
kubectl get networkpolicy -n team-orders
kubectl describe ingress api -n team-orders            # backend service/port, controller events
```

- App listens on `127.0.0.1` instead of `0.0.0.0` → works in the container, unreachable from outside it.
- Port name vs number mismatch between Service and container.
- Ingress controller logs often show upstream errors (502/504) and which backend failed.

<details>
<summary>Follow-up questions</summary>

- What does a 502 vs 504 from the Ingress tell you?
- How would you debug intermittent timeouts only between two specific services?

</details>

**Remember:** Debug the path hop by hop; empty endpoints is the most common answer.

---

## Q7. What are PodDisruptionBudgets and how do node drains and upgrades affect your app?

**Short answer:** A PodDisruptionBudget (PDB) limits how many Pods of an app can be down at once during **voluntary** disruptions — node drains, cluster upgrades, autoscaler scale-down. Without a PDB, draining two nodes could take out all replicas at once. PDBs don't protect against involuntary failures like a node crash.

**Example:**

```yaml
apiVersion: policy/v1
kind: PodDisruptionBudget
metadata:
  name: orders
spec:
  minAvailable: 2          # or maxUnavailable: 1
  selector:
    matchLabels: { app: orders }
```

**Trade-offs and pitfalls:** A PDB with `minAvailable` equal to the replica count blocks drains forever and stalls upgrades. Combine PDBs with `topologySpreadConstraints` or anti-affinity so replicas are spread across nodes and zones.

<details>
<summary>Follow-up questions</summary>

- How would you upgrade a cluster with zero downtime?
- How do you spread replicas across availability zones?

</details>

**Remember:** PDBs make voluntary disruption safe; spreading makes involuntary disruption survivable.

---

## Q8. How do you harden Pods with securityContext and Pod Security Standards?

**Short answer:** Set a `securityContext` so containers run as non-root, with a read-only root filesystem, no privilege escalation and all capabilities dropped. Enforce this cluster-wide with Pod Security admission using the `baseline` or `restricted` Pod Security Standards per namespace, or with a policy engine like Kyverno or OPA Gatekeeper.

**Example:**

```yaml
spec:
  automountServiceAccountToken: false
  securityContext:
    runAsNonRoot: true
    runAsUser: 10001
    seccompProfile: { type: RuntimeDefault }
  containers:
    - name: orders
      image: registry.example.com/orders:3f9c2a1
      securityContext:
        allowPrivilegeEscalation: false
        readOnlyRootFilesystem: true
        capabilities:
          drop: ["ALL"]
```

```bash
# Enforce the restricted standard on a namespace
kubectl label namespace team-orders pod-security.kubernetes.io/enforce=restricted
```

See also [DevSecOps & Supply Chain](../security-and-supply-chain/01-devsecops-and-supply-chain.md) for network policies and image policies.

<details>
<summary>Follow-up questions</summary>

- What replaced PodSecurityPolicy? (Pod Security admission, or policy engines)
- How do you roll out a stricter policy without breaking existing workloads? (`warn`/`audit` modes first)

</details>

**Remember:** Non-root, read-only, no escalation, no capabilities — enforced by admission, not by hope.

---

## Q9. Managed Kubernetes (EKS, GKE, AKS) vs self-managed — what are the trade-offs?

**Short answer:** Managed services run and upgrade the control plane (API server, etcd) for you and integrate with the cloud's IAM, load balancers and storage. You still own node configuration (unless using a fully managed mode), add-ons, upgrades of your workloads, security and cost. Self-managed gives full control but you carry etcd, upgrades, and HA yourself — rarely worth it unless you have on-prem, edge, or strict regulatory needs.

| Aspect | EKS (AWS) | GKE (Google Cloud) | AKS (Azure) |
| --- | --- | --- | --- |
| Hands-off mode | EKS Auto Mode; Fargate for serverless Pods | Autopilot | Virtual nodes; automatic mode options |
| Node autoscaling | Cluster Autoscaler or Karpenter | Built-in cluster autoscaler / node auto-provisioning | Cluster Autoscaler, node auto-provisioning |
| Workload identity | IRSA or EKS Pod Identity | Workload Identity Federation for GKE | Microsoft Entra Workload ID |
| Fits best when | You're already deep in AWS | You want the most opinionated managed experience | You're in the Microsoft/Entra ecosystem |

Feature names and pricing change often — verify current offerings before quoting them in an interview.

**Trade-offs and pitfalls:**

- Kubernetes itself might be overkill: for a handful of stateless services, ECS/Fargate, Cloud Run or Azure Container Apps can be much less operational work.
- Kubernetes minor versions have a limited support window; plan upgrades as a recurring activity, not a project.
- Add-ons (ingress, cert-manager, external-dns, observability agents) are yours to maintain.

<details>
<summary>Follow-up questions</summary>

- When would you *not* choose Kubernetes?
- How do you plan and test a Kubernetes version upgrade?

</details>

**Remember:** Managed Kubernetes removes control-plane toil, not platform ownership.

---

## References

- [Kubernetes documentation](https://kubernetes.io/docs/home/)
- [Debug running Pods](https://kubernetes.io/docs/tasks/debug/debug-application/debug-running-pod/)
- [Using RBAC authorization](https://kubernetes.io/docs/reference/access-authn-authz/rbac/)
- [Pod Security Standards](https://kubernetes.io/docs/concepts/security/pod-security-standards/)
- [Amazon EKS documentation](https://docs.aws.amazon.com/eks/)
- [Google Kubernetes Engine documentation](https://cloud.google.com/kubernetes-engine/docs)
- [Azure Kubernetes Service documentation](https://learn.microsoft.com/en-us/azure/aks/)
