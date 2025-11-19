# 4) Streams & Buffers (Q31–40)

## Q31. What are Streams in Node.js, and why are they useful for large data processing?

Streams are objects that allow you to read data from a source or write data to a destination in a continuous fashion, enabling efficient processing of large datasets without loading everything into memory - they process data in chunks instead of loading entire file, are memory efficient for large files or datasets, and can process data as it arrives (real-time). Foundation for many Node.js APIs (HTTP, file system).

- **Trade-offs**: Process data in chunks instead of loading entire file - memory efficient for large files or datasets. Can process data as it arrives (real-time) - enable backpressure handling for flow control. Foundation for many Node.js APIs (HTTP, file system) - great for handling large files, but watch out - streams can be complex to debug and error handling requires careful attention.

Example:

```javascript
const fs = require('fs');
const readStream = fs.createReadStream('large-file.txt');
const writeStream = fs.createWriteStream('output.txt');
readStream.pipe(writeStream);
```

## Q32. What are the four types of Streams (Readable, Writable, Duplex, Transform)?

Node.js has four stream types: Readable (data source like files, HTTP requests), Writable (data destination like files, HTTP responses), Duplex (both readable and writable like TCP sockets), and Transform (duplex that modifies data as it flows through like compression, encryption). Each type has specific methods and events.

- **Trade-offs**: Readable: source of data (files, HTTP requests) - Writable: destination for data (files, HTTP responses). Duplex: both readable and writable (TCP sockets) - Transform: duplex that modifies data (compression, encryption). Each type has specific methods and events - choose the right type based on your use case, and watch out - mixing stream types incorrectly can cause errors.

Example:

```javascript
const { Readable, Writable, Transform } = require('stream');

const readable = new Readable({
  read() { this.push('data'); }
});

const writable = new Writable({
  write(chunk, encoding, callback) {
    console.log(chunk.toString());
    callback();
  }
});
```

## Q33. How does backpressure occur in Streams, and how can it be handled?

Backpressure occurs when data is produced faster than it can be consumed, causing memory issues - it's handled by pausing the readable stream when the writable stream is overwhelmed. Node.js automatically handles backpressure with .pipe(), but you can use .pause() and .resume() for manual control, and monitor 'drain' event to know when to resume.

- **Trade-offs**: Occurs when producer is faster than consumer - can cause memory leaks if not handled. Node.js automatically handles backpressure with .pipe() - use .pause() and .resume() for manual control. Monitor 'drain' event to know when to resume - automatic handling works well, but watch out - manual control requires careful management to avoid data loss.

Example:

```javascript
const { Readable, Writable } = require('stream');

const readable = new Readable({
  read() {
    this.push('data chunk');
  }
});

const writable = new Writable({
  write(chunk, encoding, callback) {
    setTimeout(() => {
      console.log('Processed:', chunk.toString());
      callback();
    }, 100);
  }
});

readable.pipe(writable);
```

## Q34. What is a Buffer, and how is it different from a Stream?

A Buffer is a fixed-size memory allocation for handling binary data (fixed-size binary data container), while a Stream is an interface for continuous data flow - buffers are the chunks that flow through streams, buffers are immutable once created, and streams can process data of any size.

- **Trade-offs**: Buffer: fixed-size binary data container - Stream: interface for continuous data flow. Buffers are the chunks that flow through streams - buffers are immutable once created. Streams can process data of any size - buffers are good for small fixed data, streams are better for large or continuous data.

Example:

```javascript
const buffer = Buffer.from('Hello World', 'utf8');
console.log(buffer.length);
console.log(buffer.toString());

const stream = fs.createReadStream('file.txt');
stream.on('data', (chunk) => {
  console.log('Received chunk:', chunk.length, 'bytes');
});
```

## Q35. How do you pipe Streams together?

Piping connects streams together so data flows from a readable stream to a writable stream - .pipe() connects readable to writable streams, returns the destination stream for chaining, handles backpressure automatically, and propagates errors from source to destination. Can chain multiple transform streams.

- **Trade-offs**: .pipe() connects readable to writable streams - returns the destination stream for chaining. Handles backpressure automatically - propagates errors from source to destination. Can chain multiple transform streams - makes it easy to build data pipelines, but watch out - error handling can be tricky with long chains, so use stream.pipeline() for better error handling.

Example:

```javascript
const fs = require('fs');
const zlib = require('zlib');

fs.createReadStream('input.txt')
  .pipe(zlib.createGzip())
  .pipe(fs.createWriteStream('output.txt.gz'));
```

## Q36. How do you use Streams to copy large files efficiently?

Use readable and writable streams with piping to copy large files efficiently, processing data in chunks rather than loading the entire file into memory - it's memory efficient for files larger than available RAM, processes data in chunks (default 64KB), and has automatic backpressure handling. Much faster than readFile/writeFile for large files.

- **Trade-offs**: Memory efficient for files larger than available RAM - processes data in chunks (default 64KB). Automatic backpressure handling - can monitor progress with events. Much faster than readFile/writeFile for large files - perfect for copying large files, but watch out - for small files, readFile/writeFile might be simpler and faster.

Example:

```javascript
const fs = require('fs');

function copyFile(source, destination) {
  const readStream = fs.createReadStream(source);
  const writeStream = fs.createWriteStream(destination);
  readStream.pipe(writeStream);
  writeStream.on('finish', () => {
    console.log('File copied successfully');
  });
}

copyFile('large-file.txt', 'copy.txt');
```

## Q37. How do you implement compression and decompression using Streams?

Use transform streams like zlib to compress or decompress data as it flows through the stream pipeline - zlib provides compression/decompression streams, can compress any data stream (not just files), has different compression levels available, and is useful for reducing bandwidth and storage. Can be chained with other transform streams.

- **Trade-offs**: zlib provides compression/decompression streams - can compress any data stream, not just files. Different compression levels available - useful for reducing bandwidth and storage. Can be chained with other transform streams - great for reducing file sizes, but watch out - compression adds CPU overhead, so balance compression level with performance needs.

Example:

```javascript
const fs = require('fs');
const zlib = require('zlib');

fs.createReadStream('input.txt')
  .pipe(zlib.createGzip())
  .pipe(fs.createWriteStream('input.txt.gz'));

fs.createReadStream('input.txt.gz')
  .pipe(zlib.createGunzip())
  .pipe(fs.createWriteStream('decompressed.txt'));
```

## Q38. How do you handle encoding when working with Buffers and Streams?

Buffers store binary data and need encoding specification when converting to/from strings, while streams can specify encoding in their options - common encodings are utf8, ascii, base64, hex, default encoding is utf8 for strings. Buffers are always binary, strings need encoding, and wrong encoding can corrupt data.

- **Trade-offs**: Common encodings: utf8, ascii, base64, hex - default encoding is utf8 for strings. Specify encoding when creating streams - buffers are always binary, strings need encoding. Wrong encoding can corrupt data - always specify encoding explicitly to avoid issues, especially when dealing with non-UTF8 data.

Example:

```javascript
const buffer = Buffer.from('Hello', 'utf8');
const string = buffer.toString('base64');

const readStream = fs.createReadStream('file.txt', { encoding: 'utf8' });
const writeStream = fs.createWriteStream('output.txt', { encoding: 'utf8' });
```

## Q39. How do you monitor stream performance or memory usage?

Monitor stream performance using events, timers, and memory usage tracking - monitor 'data' events for throughput, use process.memoryUsage() for memory tracking, time operations to measure performance, and watch for memory leaks in long-running streams. Consider using stream.pipeline() for better error handling.

- **Trade-offs**: Monitor 'data' events for throughput - use process.memoryUsage() for memory tracking. Time operations to measure performance - watch for memory leaks in long-running streams. Consider using stream.pipeline() for better error handling - monitoring helps identify bottlenecks, but watch out - too much logging can impact performance.

Example:

```javascript
const fs = require('fs');
const readStream = fs.createReadStream('large-file.txt');

let bytesProcessed = 0;
const startTime = Date.now();

readStream.on('data', (chunk) => {
  bytesProcessed += chunk.length;
  const memoryUsage = process.memoryUsage();
  console.log(`Processed: ${bytesProcessed} bytes, Memory: ${memoryUsage.heapUsed} bytes`);
});

readStream.on('end', () => {
  const duration = Date.now() - startTime;
  console.log(`Completed in ${duration}ms`);
});
```

## Q40. What is highWaterMark, and how does it affect Streams?

highWaterMark is a threshold that controls when streams pause/resume, affecting memory usage and performance by determining how much data can be buffered - it controls internal buffer size for streams, default is 64KB for most streams. Higher values use more memory but may improve performance, lower values use less memory but may reduce performance.

- **Trade-offs**: Controls internal buffer size for streams - higher values use more memory but may improve performance. Lower values use less memory but may reduce performance - default is 64KB for most streams. Tune based on available memory and performance requirements - larger buffers can improve throughput, but watch out - too large can cause memory issues.

Example:

```javascript
const fs = require('fs');

const defaultStream = fs.createReadStream('file.txt');

const customStream = fs.createReadStream('file.txt', {
  highWaterMark: 1024 * 1024
});
```
