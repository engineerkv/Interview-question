---
sidebar_position: 100
sidebar_label: Cheatsheet
description: "One-page MinIO and object storage revision sheet: concepts, security checklist, upload patterns, data protection, commands and one-liners."
---

# MinIO Cheatsheet (Q1-Q30)

> **Reviewed:** 2026-09 · **Level:** Senior · **Type:** Foundational

## Concepts

- Object storage: bucket + key → bytes + metadata, over HTTP (S3 API).
- Prefixes act as folders, policy scopes and lifecycle scopes.
- Strong read-after-write per object; no multi-object transactions; rename = copy + delete.

## Security checklist

1. Root credentials only for admins; one user or service account per app.
2. Least-privilege policies: bucket ARN for `ListBucket`, `bucket/*` for object actions.
3. Private buckets by default; public content in a dedicated bucket behind a CDN.
4. Presigned URLs: short expiry (max 7 days for SigV4), signed with the **public** endpoint.
5. Verify uploads after the fact (HEAD size/type, async scan).
6. TLS on all endpoints; default bucket encryption; KMS treated as critical.
7. Audit logs and alerts on policy changes.

## Upload patterns

| Pattern | Use when |
|---|---|
| Presigned PUT | Single file, moderate size, browser/mobile |
| Presigned POST with policy | Need server-enforced size/type conditions |
| Multipart (SDK helper) | Large files from servers or workers |
| Resumable multipart with per-part presigned URLs | Large browser uploads over flaky networks |
| Proxy through API | Small files needing inline validation |

S3 multipart rules: parts 1-10,000, minimum 5 MiB except the last part, abort stale uploads via lifecycle.

## Data protection

| Feature | Protects against | Needs |
|---|---|---|
| Erasure coding | Drive/node failure | Planned parity |
| Versioning | Overwrites, accidental deletes | Lifecycle for noncurrent versions |
| Object lock (governance/compliance), legal hold | Deletion, ransomware via API | Versioning, enabled at bucket creation |
| Replication (bucket/site) | Site loss, locality | Versioning; async, RPO > 0 |
| Independent backups | Mistakes, malicious deletes, bad lifecycle rules | Separate credentials, restore drills |

## SDK configuration

```javascript
new S3Client({ endpoint, region: 'us-east-1', forcePathStyle: true, credentials });
```

```python
boto3.client("s3", endpoint_url=endpoint,
             config=Config(signature_version="s3v4", s3={"addressing_style": "path"}))
```

## Commands

```bash
mc alias set local http://localhost:9000 ACCESS SECRET
mc mb local/media                     # --with-lock for object locking
mc version enable local/media
mc ilm rule add local/media --prefix "exports/" --expire-days 7
mc encrypt set sse-s3 local/media
mc admin user add local app-user SECRET
mc admin policy attach local app-policy --user app-user
mc replicate add local/media --remote-bucket "https://user:pass@dr.example.com/media"
mc admin info local
mc admin heal local --recursive
```

## MinIO vs S3 in one breath

S3: managed, elastic, deep AWS integrations, pay per GB, request and egress. MinIO: same API, your hardware, your ops; wins on residency, control, predictable large volumes and dev parity. AGPLv3 license and recent community edition changes need legal and project-health review.

## One-liners

- API authorizes and signs; bytes go client to storage directly.
- Sign presigned URLs with the host the browser will call.
- Immutable keys + long Cache-Control + CDN.
- Redundancy is not backup.
- Compliance-mode lock cannot be undone; test retention settings.
- Create SDK clients per worker process after fork.

## Where to go next

- [Overview](./index.md) · [Question index](./question-index.md)
- [AWS cloud architecture](../../devops/cloud/01-aws-cloud-architecture.md)
