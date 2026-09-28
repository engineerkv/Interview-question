---
sidebar_label: "Architecture and Operations"
description: "Erasure coding, distributed MinIO deployments across drives and nodes, healing, monitoring and backups, explained conceptually."
---

# Architecture and Operations (Q19-Q22)

> **Reviewed:** 2026-09 · **Level:** Senior · **Type:** Foundational

This file keeps claims conceptual; exact parity defaults, sizing and supported topologies change between releases, so check the MinIO docs for your version.

## Q19. Erasure coding splits objects into data and parity shards across drives

Instead of storing full copies (replication), MinIO splits each object into data shards and computes parity shards, then spreads them across the drives of an **erasure set**. The object can be reconstructed from any combination of shards as long as enough remain (at least the number of data shards). You choose the parity level: more parity tolerates more drive or node failures but uses more raw capacity. MinIO also stores checksums to detect bit rot and repair corrupted shards.

**How it works:**

| Approach | Capacity efficiency | Failure tolerance | Read/write cost |
|---|---|---|---|
| Replication (N full copies) | 1/N usable | N-1 copies lost | Simple, cheap reads |
| Erasure coding (K data + M parity) | K/(K+M) usable | Up to M shards lost | Encoding CPU, reads touch multiple drives |

**Trade-offs and pitfalls:**

- Erasure coding protects against drive and node failures inside one deployment, not against deleting data or losing the whole site.
- Writes need a quorum of drives; if too many drives in a set are offline, writes (and eventually reads) fail even though some data is still on disk.
- Parity choice is made at deployment time; plan it up front.

**Remember:** Erasure coding = parity math instead of full copies; tolerate M failures for M parity shards.

## Q20. A distributed deployment is a set of nodes and drives organized into server pools

A production MinIO deployment runs the same server process on several nodes, each with several drives, all started with the same list of endpoints (MinIO's expansion notation describes them). MinIO groups the drives into erasure sets. To grow capacity you add a **server pool** (another group of nodes and drives) rather than adding single drives to an existing set.

**Example:**

```bash
# 4 nodes x 4 drives each, hostnames minio1..minio4, drives /mnt/disk1..4
minio server https://minio{1...4}.example.internal/mnt/disk{1...4}/minio \
  --console-address ":9001"

# later: expand with a second pool (all nodes restarted with both pools listed)
minio server https://minio{1...4}.example.internal/mnt/disk{1...4}/minio \
             https://minio{5...8}.example.internal/mnt/disk{1...4}/minio
```

**Trade-offs and pitfalls:**

- Use dedicated local drives (JBOD) of similar size and type; network-attached or RAID-underneath setups fight with erasure coding and are generally discouraged by MinIO docs.
- Every node needs a stable hostname and reliable, low-latency networking to the others; time skew and flaky networks cause hard-to-debug errors.
- On Kubernetes, the MinIO Operator manages tenants and pools; see [Orchestration](../../devops/orchestration/index.md).

**Remember:** Nodes × drives form erasure sets; grow by adding pools.

## Q21. Healing restores missing or corrupted shards; monitoring must catch problems early

When a drive is replaced or a node returns, MinIO **heals**: it rebuilds missing shards from the surviving data and parity. It also heals objects found corrupted (via checksums) during reads or background scans. Operationally, you watch drive and node health, healing progress, capacity, request errors and latency.

**Example:**

```bash
mc admin info local                 # nodes, drives, online/offline status
mc admin heal local --recursive     # trigger or inspect healing
mc admin prometheus generate local  # scrape config for Prometheus metrics
```

**Trade-offs and pitfalls:**

- During healing, the deployment has less spare redundancy; a second failure in the same erasure set matters more. Replace failed drives promptly.
- Alert on: drives offline, nodes offline, capacity thresholds, rising 5xx rates, replication lag, KMS reachability.
- Capacity: erasure-coded usable space is well below raw capacity; plan with the parity setting in mind.

**Remember:** Replace drives fast, watch healing and capacity, and alert on offline drives.

## Q22. Backups are separate from erasure coding and replication

Erasure coding protects against hardware failure; replication protects against site loss. Neither protects against a bad deploy that deletes objects, ransomware using valid credentials, or a lifecycle rule with the wrong prefix. You still need independent copies: a versioned, locked bucket in another deployment or cloud, with credentials that the primary's applications do not have.

**Example:** Nightly `mc mirror` (or replication) into a separate MinIO or S3 bucket with versioning and object lock in governance/compliance mode, owned by a backup account. Quarterly restore drills verify you can actually read the data back and measure how long it takes.

```bash
mc mirror --overwrite local/documents backup/documents-2026
```

**Trade-offs and pitfalls:**

- `mc mirror --remove` propagates deletions, which is exactly what backups should not do; understand the flags.
- Back up metadata too: bucket policies, lifecycle and replication configs, IAM (users, policies), and KMS keys.
- A backup you have never restored is a hope, not a backup.

**Remember:** Redundancy is not backup; keep an independent, immutable copy and test restores.

## References

- [MinIO documentation: erasure coding, deployment, healing, monitoring](https://min.io/docs/minio/linux/index.html)
- [Orchestration (this site)](../../devops/orchestration/index.md)
