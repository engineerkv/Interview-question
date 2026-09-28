---
sidebar_label: "Uploads and Downloads"
description: "Multipart and resumable uploads, streaming, range requests, content types, large files, and direct-to-storage vs proxied uploads."
---

# Uploads and Downloads (Q10-Q14)

> **Reviewed:** 2026-09 · **Level:** Senior · **Type:** Foundational

## Q10. Multipart upload splits large objects into parts uploaded independently

For large files, the client initiates a multipart upload (gets an upload id), uploads parts in parallel, then completes the upload by listing part numbers and ETags. The server assembles the object. Failed parts are retried individually instead of restarting the whole file. SDK helpers do this automatically above a size threshold.

**How it works (S3 API limits, which MinIO follows closely):**

- Parts are numbered 1 to 10,000.
- Every part except the last must be at least 5 MiB.
- Maximum single-PUT object size on S3 is 5 GiB; above that multipart is required (and recommended well before that).

**Example:**

```javascript
import { Upload } from '@aws-sdk/lib-storage';

const upload = new Upload({
  client: s3,
  params: { Bucket: 'media', Key: key, Body: fileStream, ContentType: 'video/mp4' },
  partSize: 16 * 1024 * 1024,   // 16 MiB parts
  queueSize: 4,                 // parallel parts
});
upload.on('httpUploadProgress', (p) => logger.info({ loaded: p.loaded }, 'upload progress'));
await upload.done();
```

**Trade-offs and pitfalls:**

- Abandoned multipart uploads keep their parts (and consume storage) until aborted. Add a lifecycle rule to abort incomplete uploads after a few days.
- Part size × 10,000 limits the maximum object size; pick part sizes accordingly for very large files.
- The final ETag of a multipart object is not the MD5 of the content.

**Remember:** Large file = multipart, parallel parts, and a lifecycle rule to clean up abandoned uploads.

## Q11. Resumable browser uploads are multipart uploads orchestrated by your API

To let a user resume after a network drop, the API starts a multipart upload, stores the upload id against the user's upload record, and hands out presigned URLs per part. The browser uploads parts, records which succeeded, and on resume asks the API which parts exist (`ListParts`). Finally the API calls `CompleteMultipartUpload`.

**How it works:**

1. `POST /uploads` → API calls `CreateMultipartUpload`, stores `uploadId`.
2. `POST /uploads/:id/parts?numbers=1-20` → API returns presigned `UploadPart` URLs.
3. Browser `PUT`s parts directly to MinIO, collecting ETags.
4. On reconnect, API calls `ListParts` and returns missing part numbers.
5. `POST /uploads/:id/complete` → API calls `CompleteMultipartUpload`, then verifies.

**Trade-offs and pitfalls:**

- The browser must be able to read the `ETag` response header, which requires CORS to expose it.
- Libraries like Uppy (with its S3 multipart plugin) or the tus protocol (with a tus server that writes to S3) save effort; tus needs its own server component.
- Authorize part URLs per upload id so users can't write into other uploads.

**Remember:** Resumable = multipart + persisted upload id + per-part presigned URLs.

## Q12. Stream data through your service instead of buffering whole files in memory

When the API or a worker must touch the bytes (proxying downloads, transforming, zipping), stream them. Reading a 2 GB file into memory per request is how services OOM under load. SDKs return streams for `GetObject` bodies and accept streams for uploads.

**Example:**

```javascript
// Express: stream an authorized download without buffering
app.get('/files/:id', async (req, res) => {
  const file = await files.authorize(req.user, req.params.id);
  const obj = await s3.send(new GetObjectCommand({ Bucket: 'media', Key: file.key }));
  res.setHeader('Content-Type', obj.ContentType ?? 'application/octet-stream');
  res.setHeader('Content-Length', String(obj.ContentLength));
  obj.Body.pipe(res);            // Node Readable stream
});
```

```python
# boto3: stream to disk in chunks
with open("/tmp/in.mp4", "wb") as f:
    s3.download_fileobj("media", key, f)
```

**Trade-offs and pitfalls:**

- Proxying still costs API bandwidth and connections; prefer presigned URLs unless you need to transform or strictly control access per byte.
- Handle client disconnects: destroy the upstream stream when the response closes, or you leak connections.

**Remember:** Stream, don't buffer; better yet, let the client go direct.

## Q13. Range requests and correct Content-Type make media and large downloads work well

HTTP `Range` requests (`Range: bytes=0-1048575`) fetch part of an object; S3/MinIO respond with `206 Partial Content`. Video players seek with them, download managers resume with them, and parallel downloaders split files with them. Setting `Content-Type` (and, where relevant, `Content-Disposition` and `Cache-Control`) at upload time determines how browsers treat the object.

**Example:**

```python
resp = s3.get_object(Bucket="media", Key=key, Range="bytes=0-1048575")
first_mb = resp["Body"].read()
```

**Trade-offs and pitfalls:**

- A missing or wrong `Content-Type` (e.g., `application/octet-stream` for video) breaks inline playback or forces downloads.
- Don't trust the client-provided type blindly; for user uploads, sniff the file type server-side (in a worker) and store a safe type. Serving user-uploaded HTML or SVG inline from your main domain is an XSS risk; use a separate domain or force download.

**Remember:** Ranges for seeking and resuming; correct headers set at upload.

## Q14. Direct-to-storage uploads usually beat proxying through the API

| | Direct upload (presigned) | Proxy through API |
|---|---|---|
| API bandwidth/CPU | None for the bytes | Full file per upload |
| Scalability | Storage scales the data path | API tier must scale for bytes |
| Validation | After upload (HEAD, async scan) | Inline, before storing |
| Complexity | CORS, completion callback, orphan cleanup | Simpler client |
| Good for | Media, large files, mobile apps | Small files, strict inline validation, legacy clients |

**Example:** Video platform: clients upload directly with resumable multipart. A MinIO bucket notification (or the completion call) enqueues a Celery task that validates, scans and transcodes. Until processing finishes, the object lives under a `quarantine/` prefix that is never served. See [App integration](./07-app-integration.md).

**Trade-offs and pitfalls:**

- Orphans: users request URLs and never complete. Clean up with lifecycle rules on the staging prefix and expire pending DB records.
- Malware scanning and content moderation must happen before objects are served.

> **Interview tip:** The standard senior answer is "presigned direct upload to a staging prefix, completion event, async validation and processing, then promote to the served prefix".

**Remember:** Bytes go client → storage; your API handles authorization and metadata.

## References

- [MinIO documentation: uploading objects, multipart](https://min.io/docs/minio/linux/index.html)
- [Amazon S3 User Guide: multipart upload, range GETs](https://docs.aws.amazon.com/AmazonS3/latest/userguide/Welcome.html)
- [Case studies: file storage and video streaming](../../case-studies/index.md)
