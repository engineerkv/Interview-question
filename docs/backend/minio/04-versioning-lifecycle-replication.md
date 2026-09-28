---
sidebar_label: "Versioning, Lifecycle and Replication"
description: "Bucket versioning, object locking and WORM retention, lifecycle expiry and transition rules, and bucket or site replication in MinIO."
---

# Versioning, Lifecycle and Replication (Q15-Q18)

> **Reviewed:** 2026-09 · **Level:** Senior · **Type:** Foundational

## Q15. Versioning keeps every version of an object and turns deletes into delete markers

With versioning enabled on a bucket, each PUT to a key creates a new version id instead of overwriting, and a simple DELETE adds a *delete marker* (the object looks gone, but older versions remain). You can read or restore a specific version. This protects against accidental overwrites and deletes, and is a prerequisite for object locking and replication.

**Example:**

```bash
mc version enable local/documents
mc ls --versions local/documents/contracts/acme.pdf
mc cp --version-id "<version-id>" local/documents/contracts/acme.pdf ./restored.pdf
```

**Trade-offs and pitfalls:**

- Storage grows with every version; pair versioning with lifecycle rules that expire noncurrent versions after N days.
- Deleting a specific version id is permanent; restrict `s3:DeleteObjectVersion` in policies.
- Versioning can be suspended but not fully removed once enabled.

**Remember:** Versioning = undo for overwrites and deletes; lifecycle keeps the cost bounded.

## Q16. Object locking provides WORM retention for compliance and ransomware protection

Object locking prevents a version from being deleted or overwritten for a retention period (write once, read many). **Governance** mode can be bypassed by users with special permission; **compliance** mode cannot be shortened or removed by anyone, including admins, until it expires. **Legal hold** blocks deletion indefinitely until removed. Object locking requires versioning and must be enabled when the bucket is created.

**Example:**

```bash
mc mb --with-lock local/audit-logs
mc retention set --default COMPLIANCE 365d local/audit-logs
mc legalhold set local/audit-logs/2026/09/case-123.json
```

**Trade-offs and pitfalls:**

- Compliance mode is irreversible for the retention period: a misconfigured default (for example, years instead of days) locks storage you cannot reclaim.
- WORM protects against deletion through the API; it does not replace off-site backups against losing the whole cluster.
- Confirm that the implementation meets your regulator's requirements; don't assume.

**Remember:** Governance can be bypassed with permission; compliance cannot.

## Q17. Lifecycle rules expire or transition objects automatically

Lifecycle (ILM) rules act on objects by prefix or tag and age: expire current versions, expire noncurrent versions, remove expired delete markers, abort incomplete multipart uploads, and in MinIO transition objects to a remote tier (for example, another MinIO deployment or a cloud object store) for cheaper storage.

**Example:**

```bash
# temporary exports disappear after 7 days
mc ilm rule add local/media --prefix "exports/" --expire-days 7
# keep old versions of documents for 30 days
mc ilm rule add local/documents --noncurrent-expire-days 30
```

```json
{
  "Rules": [
    {
      "ID": "abort-stale-multipart",
      "Status": "Enabled",
      "Filter": { "Prefix": "" },
      "AbortIncompleteMultipartUpload": { "DaysAfterInitiation": 3 }
    }
  ]
}
```

**Trade-offs and pitfalls:**

- Lifecycle is asynchronous; objects may remain for a while after they're eligible. Don't rely on it for exact-time deletion (e.g., "delete within one hour for GDPR"); do explicit deletes for that.
- Tiered objects have different latency and possibly retrieval cost; don't tier data that is read often.
- Test rules on a copy; a wrong prefix can expire production data.

**Remember:** Every bucket should have an explicit answer for "when does this data go away?".

## Q18. Replication copies objects to another bucket or site for DR and locality

MinIO supports **bucket replication** (server-side, asynchronous copying of objects and, optionally, deletes and metadata changes from a source bucket to a target bucket on another deployment) and **site replication** (keeping multiple MinIO deployments in sync, including buckets, policies and IAM). Both require versioning.

**Example:**

```bash
mc replicate add local/media \
  --remote-bucket "https://replica-user:secret@dr.example.com/media" \
  --replicate "delete,delete-marker,existing-objects"
mc replicate status local/media
```

**Trade-offs and pitfalls:**

- Asynchronous replication means a recovery point objective greater than zero: the latest writes may not be on the replica when the primary fails.
- Replicating deletes protects consistency but also replicates accidental deletes; versioning plus lock on the target helps.
- Replication is not backup: corruption or malicious deletes can replicate too. Keep independent, versioned, access-restricted copies.
- Monitor replication lag and failed replication counts.

**Remember:** Replication for availability and locality; backups for recovery from mistakes.

## References

- [MinIO documentation: versioning, object locking, lifecycle, replication](https://min.io/docs/minio/linux/index.html)
- [Amazon S3 User Guide: versioning, Object Lock, lifecycle](https://docs.aws.amazon.com/AmazonS3/latest/userguide/Welcome.html)
