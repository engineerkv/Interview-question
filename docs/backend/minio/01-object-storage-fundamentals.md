---
sidebar_label: "Object Storage Fundamentals"
description: "Object vs block vs file storage, S3 API compatibility, buckets, keys and metadata, and the consistency model of MinIO and S3."
---

# Object Storage Fundamentals (Q1-Q4)

> **Reviewed:** 2026-09 · **Level:** Senior · **Type:** Foundational

For AWS S3 itself (storage classes, IAM, networking), see [AWS cloud architecture](../../devops/cloud/01-aws-cloud-architecture.md). This section focuses on self-hosted, S3-compatible storage with MinIO and how applications integrate with it.

## Q1. Object storage stores whole objects by key over HTTP; block and file storage serve different needs

Block storage exposes raw volumes that an OS formats with a filesystem (a database's disk). File storage exposes a shared hierarchical filesystem over NFS/SMB (shared home directories, legacy apps). Object storage stores immutable blobs with metadata, addressed by bucket + key, accessed over an HTTP API. It scales out easily and suits user uploads, media, backups, logs, data lakes and ML datasets.

**How it works:**

| | Block | File | Object |
|---|---|---|---|
| Access | Mounted volume, low-level reads/writes | POSIX paths over NFS/SMB | HTTP API (`PUT`, `GET`, `DELETE`, `LIST`) |
| Update model | In-place byte updates | In-place, locks | Replace whole object (or multipart) |
| Scale | Per volume | Per filesystem | Very large number of objects per bucket |
| Latency | Lowest | Low | Higher per request |
| Typical use | Databases, VM disks | Shared files, legacy apps | Media, backups, static assets, data lakes |

**Trade-offs and pitfalls:**

- No partial in-place updates: appending to a log file means rewriting or writing new objects.
- "Folders" are a UI illusion over key prefixes (`users/42/avatar.png`).
- Don't run a database on object storage; do put its backups there.

**Remember:** Object storage = key → blob + metadata, over HTTP, scaled out.

## Q2. MinIO is a self-hosted, S3-API-compatible object store

MinIO implements the Amazon S3 API, so the same SDKs (AWS SDK, boto3) and tools work by changing the endpoint and credentials. Teams use it for on-prem or private-cloud object storage, for data residency, inside Kubernetes, and for local development parity with S3.

**Example:**

```bash
docker run -p 9000:9000 -p 9001:9001 \
  -e MINIO_ROOT_USER=minioadmin -e MINIO_ROOT_PASSWORD=change-me-now \
  -v "$PWD/data:/data" \
  quay.io/minio/minio server /data --console-address ":9001"

mc alias set local http://localhost:9000 minioadmin change-me-now
mc mb local/uploads
mc cp ./photo.jpg local/uploads/users/42/photo.jpg
```

**Trade-offs and pitfalls:**

- "S3-compatible" covers the core API well, but not every AWS feature exists (AWS-specific integrations such as some storage classes, IAM integration details, and other AWS services around S3). Test the specific APIs you use.
- Check the licensing and edition status before adopting, including how community builds and container images are currently distributed, since that has changed recently (see [MinIO vs S3](./06-minio-vs-s3.md)).
- Never ship the default root credentials; create per-application users (see [Access and security](./02-access-and-security.md)).

**Remember:** Same S3 API, your own servers.

## Q3. Buckets hold objects; keys, metadata and tags describe them

A **bucket** is a top-level namespace with its own policy, versioning, lifecycle and notification settings. An **object** is data plus metadata, identified by a **key** (a string that may contain `/`). System metadata includes size, ETag, `Content-Type`, last-modified; user metadata is set as `x-amz-meta-*` headers at upload and is immutable without rewriting. **Tags** are key-value pairs that can be changed later and used in lifecycle rules and policies.

**Example key design:**

```text
uploads/tenant-17/users/42/2026/09/28/3f2c9a.jpg        original
derived/tenant-17/users/42/3f2c9a/thumb-256.webp         derived thumbnail
exports/tenant-17/report-9912.csv                       temporary export (lifecycle-expired)
```

**Trade-offs and pitfalls:**

- Don't put PII (emails, names) in keys; keys show up in logs, URLs and listings.
- Use random or content-hash components to avoid collisions and guessable URLs.
- Group by lifecycle and access pattern with prefixes so policies and lifecycle rules can target them.
- An ETag is not always an MD5 of the content (multipart uploads and encryption change it); don't use it as a checksum without knowing how it was produced.

**Remember:** Prefixes are your folders, policy scopes and lifecycle scopes.

## Q4. Modern S3 and MinIO give strong read-after-write consistency

Amazon S3 provides strong read-after-write consistency for PUTs and DELETEs of objects and for list operations (since December 2020). MinIO also documents strict read-after-write and list-after-write consistency. After a successful write returns, subsequent reads see it. What you still don't get is transactions across multiple objects or conditional multi-object updates.

**Trade-offs and pitfalls:**

- Concurrent writers to the same key: last writer wins. Use unique keys per upload, or conditional requests (`If-Match`/`If-None-Match`) where supported by your S3 implementation and version.
- CDNs and caches in front of storage reintroduce staleness; use versioned/immutable keys for cached assets.
- "Rename" is copy + delete, not atomic.

**Remember:** Strongly consistent per object, no multi-object transactions; design keys to avoid overwrites.

## References

- [MinIO documentation](https://min.io/docs/minio/linux/index.html)
- [Amazon S3 User Guide](https://docs.aws.amazon.com/AmazonS3/latest/userguide/Welcome.html)
- [AWS cloud architecture (this site)](../../devops/cloud/01-aws-cloud-architecture.md)
