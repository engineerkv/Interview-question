# 🌊 3. Streams & Buffers (Q29–38)

---

## 📍 Navigation

<div align="center">

[← Previous: Async Patterns & Events](02%29%20Async%20Patterns%20%26%20Events.md) • [Home: Question List](question.md) • [Next: Internals & Performance →](04%29%20Internals%20%26%20Performance.md)

[📋 Cheatsheet](Node-Express%20Interview%20Cheatsheet.md)

</div>

---

## Q29. 🌊 Streams in Node.js and why they're useful

Streams are objects that allow you to read data from a source or write data to a destination in a continuous fashion, enabling efficient processing of large datasets without loading everything into memory - they process data in chunks instead of loading entire file, are memory efficient for large files or datasets, and can process data as it arrives (real-time). Foundation for many Node.js APIs (HTTP, file system).

- **Trade-offs**: Process data in chunks instead of loading entire file - memory efficient for large files or datasets. Can process data as it arrives (real-time) - enable backpressure handling for flow control. Foundation for many Node.js APIs (HTTP, file system) - great for handling large files, but watch out - streams can be complex to debug and error handling requires careful attention.

Example:

```javascript
const fs = require('fs');
// Create readable stream: reads file in chunks (memory efficient)
const readStream = fs.createReadStream('large-file.txt');
// Create writable stream: writes data in chunks
const writeStream = fs.createWriteStream('output.txt');
// Pipe: connects streams, automatically handles backpressure
readStream.pipe(writeStream); // Data flows from readStream to writeStream

```

## Q30. 🌊 Different types of streams

Node.js has four stream types: Readable (data source like files, HTTP requests), Writable (data destination like files, HTTP responses), Duplex (both readable and writable like TCP sockets), and Transform (duplex that modifies data as it flows through like compression, encryption). Each type has specific methods and events.

- **Trade-offs**: Readable: source of data (files, HTTP requests) - Writable: destination for data (files, HTTP responses). Duplex: both readable and writable (TCP sockets) - Transform: duplex that modifies data (compression, encryption). Each type has specific methods and events - choose the right type based on your use case, and watch out - mixing stream types incorrectly can cause errors.

Example:

```javascript
const { Readable, Writable, Transform } = require('stream');

// Readable stream: source of data
const readable = new Readable({
  read() { this.push('data'); } // Push data when stream requests it
});

// Writable stream: destination for data
const writable = new Writable({
  write(chunk, encoding, callback) {
    console.log(chunk.toString()); // Process chunk
    callback(); // Signal that chunk was processed (required)
  }
});

```

## Q31. 🔧 Backpressure and how to handle it

Backpressure occurs when data is produced faster than it can be consumed, causing memory issues - it's handled by pausing the readable stream when the writable stream is overwhelmed. Node.js automatically handles backpressure with .pipe(), but you can use .pause() and .resume() for manual control, and monitor 'drain' event to know when to resume.

- **Trade-offs**: Occurs when producer is faster than consumer - can cause memory leaks if not handled. Node.js automatically handles backpressure with .pipe() - use .pause() and .resume() for manual control. Monitor 'drain' event to know when to resume - automatic handling works well, but watch out - manual control requires careful management to avoid data loss.

Example:

```javascript
const { Readable, Writable } = require('stream');

const readable = new Readable({
  read() {
    this.push('data chunk'); // Push data chunks
  }
});

// Writable stream with slow processing (simulates backpressure)
const writable = new Writable({
  write(chunk, encoding, callback) {
    setTimeout(() => {
      console.log('Processed:', chunk.toString());
      callback(); // Call callback when done (triggers drain event if needed)
    }, 100); // Slow processing
  }
});

// pipe() automatically handles backpressure: pauses readable when writable is busy
readable.pipe(writable);

```

## Q32. 💾 Buffers and how to use them

A Buffer is a fixed-size memory allocation for handling binary data in Node.js - it's a fixed-size binary data container that represents raw binary data, similar to arrays but for bytes. Buffers are immutable once created, can be created from strings, arrays, or other buffers, and are used when working with binary data like file operations, network protocols, or image processing.

- **Trade-offs**: Fixed-size binary data container - represents raw binary data like arrays but for bytes. Buffers are immutable once created - can be created from strings, arrays, or other buffers. Used for binary data operations - essential for file operations and network protocols, but watch out - buffers are fixed size, so you need to know the size beforehand or use streams for variable-size data.

Example:

```javascript
// Buffer: fixed-size binary data container
const buffer = Buffer.from('Hello World', 'utf8'); // Create buffer from string
console.log(buffer.length); // Size in bytes
console.log(buffer.toString()); // Convert back to string

const stream = fs.createReadStream('file.txt'); // Streams use buffers internally
stream.on('data', (chunk) => {
  console.log('Received chunk:', chunk.length, 'bytes');
});

```

## Q33. 🌊 Piping streams together

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

## Q34. 🌊 Handling file operations with streams

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

## Q35. 🌊 Implementing compression with streams

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

## Q36. 🌊 Handling encoding and decoding with streams

Buffers store binary data and need encoding specification when converting to/from strings, while streams can specify encoding in their options - common encodings are utf8, ascii, base64, hex, default encoding is utf8 for strings. Buffers are always binary, strings need encoding, and wrong encoding can corrupt data.

- **Trade-offs**: Common encodings: utf8, ascii, base64, hex - default encoding is utf8 for strings. Specify encoding when creating streams - buffers are always binary, strings need encoding. Wrong encoding can corrupt data - always specify encoding explicitly to avoid issues, especially when dealing with non-UTF8 data.

Example:

```javascript
const buffer = Buffer.from('Hello', 'utf8');
const string = buffer.toString('base64');

const readStream = fs.createReadStream('file.txt', { encoding: 'utf8' });
const writeStream = fs.createWriteStream('output.txt', { encoding: 'utf8' });

```

## Q37. 🌊 `highWaterMark` option in streams

highWaterMark is a threshold that controls when streams pause/resume, affecting memory usage and performance by determining how much data can be buffered - it controls internal buffer size for streams, default is 64KB for most streams. Higher values use more memory but may improve performance, lower values use less memory but may reduce performance.

- **Trade-offs**: Controls internal buffer size for streams - higher values use more memory but may improve performance. Lower values use less memory but may reduce performance - default is 64KB for most streams. Tune based on available memory and performance requirements - larger buffers can improve throughput, but watch out - too large can cause memory issues.

Example:

```javascript
const fs = require('fs');

const defaultStream = fs.createReadStream('file.txt');

const customStream = fs.createReadStream('file.txt', {
  highWaterMark: 1024 * 1024 // 1MB buffer instead of default 64KB
});

```

## Q38. 🌊 Creating custom streams

Custom streams are created by extending the base stream classes (Readable, Writable, Duplex, or Transform) and implementing their required methods - you extend the appropriate stream class, implement methods like _read() for Readable or _write() for Writable, and can add custom logic for data transformation or processing. Useful for creating reusable stream components with specific behavior.

- **Trade-offs**: Extend base stream classes (Readable, Writable, Duplex, Transform) - implement required methods like _read() or _write(). Can add custom logic for data transformation - useful for creating reusable stream components. Great for building data pipelines with custom processing, but watch out - need to handle errors properly and respect backpressure mechanisms.

Example:

```javascript
const { Readable, Transform } = require('stream');

class UppercaseTransform extends Transform {
  _transform(chunk, encoding, callback) {
    this.push(chunk.toString().toUpperCase());
    callback();
  }
}

class NumberGenerator extends Readable {
  constructor(options) {
    super(options);
    this.max = 10;
    this.index = 1;
  }

  _read() {
    if (this.index > this.max) {
      this.push(null); // End stream
    } else {
      this.push(String(this.index++));
    }
  }
}

const generator = new NumberGenerator();
const uppercase = new UppercaseTransform();

generator.pipe(uppercase).pipe(process.stdout);

```

---

## 📍 Navigation

<div align="center">

[← Previous: Async Patterns & Events](02%29%20Async%20Patterns%20%26%20Events.md) • [Home: Question List](question.md) • [Next: Internals & Performance →](04%29%20Internals%20%26%20Performance.md)

[📋 Cheatsheet](Node-Express%20Interview%20Cheatsheet.md)

</div>

---
