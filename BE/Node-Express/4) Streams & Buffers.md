# 4) Streams & Buffers (Q31–40)

## 31) What are Streams in Node.js, and why are they useful for large data processing?

Concept: Streams are objects that allow you to read data from a source or write data to a destination in a continuous fashion, enabling efficient processing of large datasets without loading everything into memory.

Example:
```javascript
const fs = require('fs');
const readStream = fs.createReadStream('large-file.txt');
const writeStream = fs.createWriteStream('output.txt');

readStream.pipe(writeStream);
```

Deep Insight:
- Process data in chunks instead of loading entire file
- Memory efficient for large files or datasets
- Can process data as it arrives (real-time)
- Enable backpressure handling for flow control
- Foundation for many Node.js APIs (HTTP, file system)

## 32) What are the four types of Streams (Readable, Writable, Duplex, Transform)?

Concept: Node.js has four stream types: Readable (data source), Writable (data destination), Duplex (both readable and writable), and Transform (duplex that modifies data as it flows through).

Example:
```javascript
const { Readable, Writable, Transform } = require('stream');

// Readable stream
const readable = new Readable({
  read() { this.push('data'); }
});

// Writable stream
const writable = new Writable({
  write(chunk, encoding, callback) {
    console.log(chunk.toString());
    callback();
  }
});
```

Deep Insight:
- Readable: Source of data (files, HTTP requests)
- Writable: Destination for data (files, HTTP responses)
- Duplex: Both readable and writable (TCP sockets)
- Transform: Duplex that modifies data (compression, encryption)
- Each type has specific methods and events

## 33) How does backpressure occur in Streams, and how can it be handled?

Concept: Backpressure occurs when data is produced faster than it can be consumed, causing memory issues, and is handled by pausing the readable stream when the writable stream is overwhelmed.

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
    // Simulate slow processing
    setTimeout(() => {
      console.log('Processed:', chunk.toString());
      callback();
    }, 100);
  }
});

readable.pipe(writable);
```

Deep Insight:
- Occurs when producer is faster than consumer
- Can cause memory leaks if not handled
- Node.js automatically handles backpressure with .pipe()
- Use .pause() and .resume() for manual control
- Monitor 'drain' event to know when to resume

## 34) What is a Buffer, and how is it different from a Stream?

Concept: A Buffer is a fixed-size memory allocation for handling binary data, while a Stream is an interface for continuous data flow, with Buffers being the data chunks that flow through streams.

Example:
```javascript
// Buffer - fixed size binary data
const buffer = Buffer.from('Hello World', 'utf8');
console.log(buffer.length); // 11
console.log(buffer.toString()); // 'Hello World'

// Stream - continuous data flow
const stream = fs.createReadStream('file.txt');
stream.on('data', (chunk) => {
  console.log('Received chunk:', chunk.length, 'bytes');
});
```

Deep Insight:
- Buffer: Fixed-size binary data container
- Stream: Interface for continuous data flow
- Buffers are the chunks that flow through streams
- Buffers are immutable once created
- Streams can process data of any size

## 35) How do you pipe Streams together?

Concept: Piping connects streams together so data flows from a readable stream to a writable stream, with automatic backpressure handling and error propagation.

Example:
```javascript
const fs = require('fs');
const zlib = require('zlib');

// Chain multiple streams
fs.createReadStream('input.txt')
  .pipe(zlib.createGzip())
  .pipe(fs.createWriteStream('output.txt.gz'));
```

Deep Insight:
- .pipe() connects readable to writable streams
- Returns the destination stream for chaining
- Handles backpressure automatically
- Propagates errors from source to destination
- Can chain multiple transform streams

## 36) How do you use Streams to copy large files efficiently?

Concept: Use readable and writable streams with piping to copy large files efficiently, processing data in chunks rather than loading the entire file into memory.

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

Deep Insight:
- Memory efficient for files larger than available RAM
- Processes data in chunks (default 64KB)
- Automatic backpressure handling
- Can monitor progress with events
- Much faster than readFile/writeFile for large files

## 37) How do you implement compression and decompression using Streams?

Concept: Use transform streams like zlib to compress or decompress data as it flows through the stream pipeline, enabling efficient data processing.

Example:
```javascript
const fs = require('fs');
const zlib = require('zlib');

// Compression
fs.createReadStream('input.txt')
  .pipe(zlib.createGzip())
  .pipe(fs.createWriteStream('input.txt.gz'));

// Decompression
fs.createReadStream('input.txt.gz')
  .pipe(zlib.createGunzip())
  .pipe(fs.createWriteStream('decompressed.txt'));
```

Deep Insight:
- zlib provides compression/decompression streams
- Can compress any data stream, not just files
- Different compression levels available
- Useful for reducing bandwidth and storage
- Can be chained with other transform streams

## 38) How do you handle encoding when working with Buffers and Streams?

Concept: Buffers store binary data and need encoding specification when converting to/from strings, while streams can specify encoding in their options.

Example:
```javascript
// Buffer encoding
const buffer = Buffer.from('Hello', 'utf8');
const string = buffer.toString('base64');

// Stream encoding
const readStream = fs.createReadStream('file.txt', { encoding: 'utf8' });
const writeStream = fs.createWriteStream('output.txt', { encoding: 'utf8' });
```

Deep Insight:
- Common encodings: utf8, ascii, base64, hex
- Default encoding is utf8 for strings
- Specify encoding when creating streams
- Buffers are always binary, strings need encoding
- Wrong encoding can corrupt data

## 39) How do you monitor stream performance or memory usage?

Concept: Monitor stream performance using events, timers, and memory usage tracking to identify bottlenecks and optimize data processing.

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

Deep Insight:
- Monitor 'data' events for throughput
- Use process.memoryUsage() for memory tracking
- Time operations to measure performance
- Watch for memory leaks in long-running streams
- Consider using stream.pipeline() for better error handling

## 40) What is highWaterMark, and how does it affect Streams?

Concept: highWaterMark is a threshold that controls when streams pause/resume, affecting memory usage and performance by determining how much data can be buffered.

Example:
```javascript
const fs = require('fs');

// Default highWaterMark (64KB)
const defaultStream = fs.createReadStream('file.txt');

// Custom highWaterMark (1MB)
const customStream = fs.createReadStream('file.txt', {
  highWaterMark: 1024 * 1024
});
```

Deep Insight:
- Controls internal buffer size for streams
- Higher values use more memory but may improve performance
- Lower values use less memory but may reduce performance
- Default is 64KB for most streams
- Tune based on available memory and performance requirements
