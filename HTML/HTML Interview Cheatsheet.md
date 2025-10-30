# 🌐 HTML Interview Cheatsheet

> **Quick Reference Guide** - Essential HTML concepts, semantic elements, and accessibility patterns for interviews

---

## 📋 **Table of Contents**

- [HTML Basics](#-html-basics)
- [Semantic Elements](#-semantic-elements)
- [Forms & Inputs](#-forms--inputs)
- [Accessibility](#-accessibility)
- [HTML5 Features](#-html5-features)
- [Media Elements](#-media-elements)
- [Performance & SEO](#-performance--seo)
- [Common Patterns](#-common-patterns)
- [Interview Keywords](#-interview-keywords)

---

## 🧠 **HTML Basics**

### **Document Structure**
```html
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Page Title</title>
</head>
<body>
  <!-- Content goes here -->
</body>
</html>
```

### **Element Types**
```html
<!-- Block elements -->
<div>, <p>, <h1>-<h6>, <section>, <article>

<!-- Inline elements -->
<span>, <a>, <strong>, <em>, <img>

<!-- Self-closing elements -->
<img>, <br>, <hr>, <input>, <meta>
```

### **Common Attributes**
```html
<!-- Global attributes -->
id="unique-id"
class="css-class"
style="inline-styles"
title="tooltip-text"
lang="en"
data-*="custom-data"

<!-- Link attributes -->
href="url"
target="_blank"
rel="noopener"
```

---

## 🏗️ **Semantic Elements**

### **Document Structure**
```html
<body>
  <header>Site header</header>
  <nav>Navigation</nav>
  <main>
    <article>
      <header>Article header</header>
      <section>Article section</section>
      <footer>Article footer</footer>
    </article>
    <aside>Sidebar</aside>
  </main>
  <footer>Site footer</footer>
</body>
```

### **Semantic Elements Guide**
| Element | Purpose | Can contain |
|---------|---------|-------------|
| `<header>` | Introductory content | Headings, nav, logo |
| `<nav>` | Navigation links | Links, lists |
| `<main>` | Primary content | Any content |
| `<article>` | Standalone content | Headings, sections |
| `<section>` | Thematic grouping | Headings, content |
| `<aside>` | Tangential content | Any content |
| `<footer>` | Closing content | Copyright, links |

### **Heading Hierarchy**
```html
<h1>Page Title (only one per page)</h1>
  <h2>Main Section</h2>
    <h3>Subsection</h3>
    <h3>Another Subsection</h3>
  <h2>Another Section</h2>
    <h3>Subsection</h3>
      <h4>Details</h4>
```

---

## 📝 **Forms & Inputs**

### **Basic Form Structure**
```html
<form action="/submit" method="POST">
  <fieldset>
    <legend>Personal Information</legend>
    
    <label for="name">Name:</label>
    <input type="text" id="name" name="name" required>
    
    <label for="email">Email:</label>
    <input type="email" id="email" name="email" required>
    
    <label for="age">Age:</label>
    <input type="number" id="age" name="age" min="0" max="120">
    
    <button type="submit">Submit</button>
  </fieldset>
</form>
```

### **Input Types**
```html
<!-- Text inputs -->
<input type="text" placeholder="Enter text">
<input type="email" placeholder="email@example.com">
<input type="password" placeholder="Password">
<input type="url" placeholder="https://example.com">
<input type="tel" placeholder="+1-234-567-8900">

<!-- Selection inputs -->
<input type="radio" name="choice" value="option1">
<input type="checkbox" name="features" value="feature1">
<select name="country">
  <option value="us">United States</option>
</select>

<!-- Other inputs -->
<input type="file" accept="image/*">
<input type="date">
<input type="time">
<input type="range" min="0" max="100">
<input type="color">
```

### **Form Validation**
```html
<!-- HTML5 validation attributes -->
<input required>                    <!-- Required field -->
<input minlength="3">              <!-- Minimum length -->
<input maxlength="50">             <!-- Maximum length -->
<input pattern="[A-Za-z]+">        <!-- Pattern matching -->
<input min="0" max="100">          <!-- Numeric range -->
<input type="email">               <!-- Email format -->
<input type="url">                 <!-- URL format -->
```

---

## ♿ **Accessibility**

### **ARIA Landmarks**
```html
<header role="banner">Site header</header>
<nav role="navigation" aria-label="Main navigation">Nav</nav>
<main role="main">Main content</main>
<aside role="complementary">Sidebar</aside>
<footer role="contentinfo">Site footer</footer>
```

### **ARIA Attributes**
```html
<!-- Labels and descriptions -->
<button aria-label="Close dialog">×</button>
<input aria-describedby="help-text">
<div id="help-text">This field is required</div>

<!-- States and properties -->
<button aria-expanded="false" aria-controls="menu">Menu</button>
<div id="menu" aria-hidden="true">Menu content</div>

<!-- Live regions -->
<div aria-live="polite">Status updates appear here</div>
<div aria-live="assertive">Urgent messages appear here</div>
```

### **Accessible Images**
```html
<!-- Decorative images -->
<img src="decoration.jpg" alt="" role="presentation">

<!-- Informative images -->
<img src="chart.jpg" alt="Sales increased 25% in Q3">

<!-- Complex images -->
<img src="infographic.jpg" alt="Detailed infographic">
<figcaption>Complete sales data for 2024</figcaption>
```

### **Keyboard Navigation**
```html
<!-- Focusable elements -->
<button tabindex="0">Focusable button</button>
<a href="#" tabindex="0">Focusable link</a>

<!-- Skip links -->
<a href="#main" class="skip-link">Skip to main content</a>

<!-- Focus management -->
<div tabindex="-1" id="main">Main content</div>
```

---

## 🚀 **HTML5 Features**

### **New Semantic Elements**
```html
<main>Primary content</main>
<section>Document section</section>
<article>Standalone article</article>
<aside>Sidebar content</aside>
<header>Header content</header>
<footer>Footer content</footer>
<nav>Navigation</nav>
<figure>
  <img src="image.jpg" alt="Description">
  <figcaption>Image caption</figcaption>
</figure>
<details>
  <summary>Click to expand</summary>
  <p>Hidden content</p>
</details>
```

### **New Input Types**
```html
<input type="email">
<input type="url">
<input type="tel">
<input type="search">
<input type="number">
<input type="range">
<input type="date">
<input type="time">
<input type="datetime-local">
<input type="color">
```

### **Data Attributes**
```html
<div data-user-id="123" data-role="admin">
  User content
</div>

<!-- Access with JavaScript -->
element.dataset.userId; // "123"
element.dataset.role;   // "admin"
```

---

## 🎬 **Media Elements**

### **Images**
```html
<!-- Basic image -->
<img src="image.jpg" alt="Description" width="300" height="200">

<!-- Responsive image -->
<img src="image.jpg" 
     srcset="image-320w.jpg 320w, image-640w.jpg 640w"
     sizes="(max-width: 600px) 320px, 640px"
     alt="Responsive image">

<!-- Picture element -->
<picture>
  <source media="(min-width: 800px)" srcset="large.jpg">
  <source media="(min-width: 400px)" srcset="medium.jpg">
  <img src="small.jpg" alt="Responsive image">
</picture>
```

### **Video**
```html
<video controls width="400" height="300">
  <source src="video.mp4" type="video/mp4">
  <source src="video.webm" type="video/webm">
  <track kind="subtitles" src="subtitles.vtt" srclang="en" label="English">
  Your browser doesn't support video.
</video>
```

### **Audio**
```html
<audio controls>
  <source src="audio.mp3" type="audio/mpeg">
  <source src="audio.ogg" type="audio/ogg">
  Your browser doesn't support audio.
</audio>
```

---

## ⚡ **Performance & SEO**

### **Meta Tags**
```html
<!-- Essential meta tags -->
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<meta name="description" content="Page description for SEO">
<meta name="robots" content="index, follow">

<!-- Open Graph (Social Media) -->
<meta property="og:title" content="Page Title">
<meta property="og:description" content="Page Description">
<meta property="og:image" content="image.jpg">
<meta property="og:url" content="https://example.com">

<!-- Twitter Cards -->
<meta name="twitter:card" content="summary_large_image">
<meta name="twitter:title" content="Page Title">
```

### **Performance Optimization**
```html
<!-- Lazy loading -->
<img src="image.jpg" loading="lazy" alt="Description">

<!-- Preload critical resources -->
<link rel="preload" href="critical.css" as="style">
<link rel="preload" href="hero-image.jpg" as="image">

<!-- DNS prefetch -->
<link rel="dns-prefetch" href="//fonts.googleapis.com">

<!-- Resource hints -->
<link rel="preconnect" href="https://api.example.com">
```

---

## 🎯 **Common Patterns**

### **Navigation Menu**
```html
<nav aria-label="Main navigation">
  <ul>
    <li><a href="/" aria-current="page">Home</a></li>
    <li><a href="/about">About</a></li>
    <li><a href="/contact">Contact</a></li>
  </ul>
</nav>
```

### **Breadcrumbs**
```html
<nav aria-label="Breadcrumb">
  <ol>
    <li><a href="/">Home</a></li>
    <li><a href="/category">Category</a></li>
    <li aria-current="page">Current Page</li>
  </ol>
</nav>
```

### **Modal Dialog**
```html
<div role="dialog" aria-labelledby="dialog-title" aria-modal="true">
  <h2 id="dialog-title">Dialog Title</h2>
  <p>Dialog content</p>
  <button aria-label="Close dialog">×</button>
</div>
```

### **Data Table**
```html
<table>
  <caption>Sales Data for Q1 2024</caption>
  <thead>
    <tr>
      <th scope="col">Month</th>
      <th scope="col">Sales</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th scope="row">January</th>
      <td>$10,000</td>
    </tr>
  </tbody>
</table>
```

---

## 🔑 **Interview Keywords**

### **Must Know Concepts**
- **Semantic HTML** - Meaningful element usage
- **Accessibility** - WCAG guidelines and ARIA
- **SEO** - Meta tags and structured data
- **Performance** - Optimization techniques
- **HTML5** - Modern features and APIs
- **Forms** - Input types and validation
- **Media** - Images, video, audio optimization

### **Common Gotchas**
```html
<!-- Don't skip heading levels -->
<h1>Title</h1>
<h3>Subtitle</h3> <!-- Wrong: skipped h2 -->

<!-- Don't use div for everything -->
<div>Click here</div> <!-- Wrong: use <button> -->

<!-- Always provide alt text -->
<img src="image.jpg"> <!-- Wrong: missing alt -->
```

### **Key Differences**
| Element | Purpose | When to use |
|---------|---------|-------------|
| `<div>` vs `<section>` | Generic vs thematic grouping | Use `<section>` when you need a heading |
| `<article>` vs `<section>` | Standalone vs grouped content | Use `<article>` for complete content |
| `<strong>` vs `<b>` | Importance vs visual styling | Use `<strong>` for important text |
| `<em>` vs `<i>` | Emphasis vs visual styling | Use `<em>` for emphasized text |

---

## 🎯 **Quick Reference**

### **Form Elements**
```html
<form>           <!-- Form container -->
<input>          <!-- Input field -->
<textarea>       <!-- Multi-line text -->
<select>         <!-- Dropdown -->
<button>         <!-- Button -->
<label>          <!-- Form label -->
<fieldset>       <!-- Group related fields -->
<legend>         <!-- Fieldset caption -->
```

### **List Elements**
```html
<ul>             <!-- Unordered list -->
<ol>             <!-- Ordered list -->
<li>             <!-- List item -->
<dl>             <!-- Definition list -->
<dt>             <!-- Definition term -->
<dd>             <!-- Definition description -->
```

### **Table Elements**
```html
<table>          <!-- Table container -->
<thead>          <!-- Table header -->
<tbody>          <!-- Table body -->
<tfoot>          <!-- Table footer -->
<tr>             <!-- Table row -->
<th>             <!-- Table header cell -->
<td>             <!-- Table data cell -->
<caption>        <!-- Table caption -->
```

---

## 🚀 **Final Tips**

1. **Use Semantic HTML** - Choose elements based on meaning, not appearance
2. **Test Accessibility** - Use screen readers and keyboard navigation
3. **Validate HTML** - Always check markup with validators
4. **Think Mobile-First** - Design for mobile devices first
5. **Optimize Performance** - Use lazy loading and resource hints
6. **Follow Standards** - Stay updated with HTML5+ features

---

## 🌐 **Browser Internals: What Happens When You Type a URL**

🔥 Fantastic question — this is **one of the most advanced and high-value interview topics** for front-end engineers and system design interviews:

> "What happens inside the browser when you type a URL and press Enter?"

Let's go **deep** — all the way from your keyboard input → DNS → HTTP → Rendering → Paint → JS execution — step by step.

### 🧠 **Overview**

When you type a URL like `https://www.example.com` and hit **Enter**, the browser performs **dozens of subsystems** working together:

1️⃣ **Networking** (DNS, TCP, TLS)  
2️⃣ **HTTP** (request → response)  
3️⃣ **Rendering pipeline** (HTML → DOM → CSSOM → Render Tree → Layout → Paint → Composite)  
4️⃣ **JavaScript engine execution** (V8, SpiderMonkey, etc.)  
5️⃣ **GPU compositing and display**

### ⚙️ **Detailed Step-by-Step Browser Workflow**

#### **1️⃣ You type the URL**
- Browser determines if it's a **search query** or a **direct URL**
- If it's a URL, it parses it into components:
  ```
  https://www.example.com:443/path?query=value#section
  ```
  - Protocol → `https`
  - Host → `www.example.com`
  - Port → `443`
  - Path → `/path`
  - Query → `?query=value`
  - Fragment → `#section`

#### **2️⃣ Browser checks caches**
Before making any network call, the browser checks:
- 🔹 **Memory Cache** (recently loaded resources)
- 🔹 **Disk Cache** (cached files)
- 🔹 **Service Worker Cache** (PWA layer)
- 🔹 **OS-level DNS Cache**
- 🔹 **HTTP Cache headers** (`ETag`, `Last-Modified`)

✅ If found and valid → loads from cache (super fast)  
❌ If not → proceeds to DNS resolution

#### **3️⃣ DNS Resolution**
Browser must convert the domain (`www.example.com`) into an IP address.

It checks in order:
1. Browser's DNS cache
2. OS cache (system resolver)
3. Router cache (local network)
4. ISP DNS server
5. Root DNS → TLD → Authoritative DNS

💡 Example result: `www.example.com → 93.184.216.34`

#### **4️⃣ TCP Handshake (Transport Layer)**
Now that the IP is known:
- Browser opens a **TCP connection** to the server (port 443 for HTTPS)
- Uses the **3-way handshake**:
  1. SYN → client says "Can we talk?"
  2. SYN-ACK → server says "Yes."
  3. ACK → connection established

#### **5️⃣ TLS/SSL Handshake (if HTTPS)**
Before data is sent, the browser establishes a **secure channel**:
1. Browser sends supported encryption algorithms + random key
2. Server responds with certificate + public key
3. Browser verifies certificate via **CA (Certificate Authority)**
4. Session key is generated and encrypted

✅ Now all communication is **encrypted and secure**

#### **6️⃣ HTTP Request (Application Layer)**
Once the secure connection is ready, the browser sends the HTTP request:

```http
GET / HTTP/1.1
Host: www.example.com
User-Agent: Chrome/121.0
Accept: text/html,application/xhtml+xml
Accept-Encoding: gzip, deflate, br
Connection: keep-alive
```

#### **7️⃣ Server Processing**
On the backend:
1. The web server (e.g., Nginx, Apache) receives the request
2. Passes it to the app server (Node.js, Python, etc.)
3. The application generates a response (HTML, JSON, etc.)
4. Server sends back an HTTP response

#### **8️⃣ Browser Receives Response**
- The browser starts receiving **HTML content in chunks**
- As soon as it gets the first bytes, it **starts parsing** — doesn't wait for the full document

### 🖥️ **RENDERING PIPELINE (Inside Browser Engine)**

Now we move from **network → rendering** inside the browser engine (Blink for Chrome, WebKit for Safari, Gecko for Firefox).

#### **9️⃣ HTML Parsing → DOM Construction**
- Browser's **HTML parser** converts HTML bytes → tokens → nodes → DOM tree

Example:
```html
<html>
  <body>
    <h1>Hello</h1>
  </body>
</html>
```

DOM Tree:
```
Document
 └── html
      └── body
           └── h1
```

#### **🔟 CSS Parsing → CSSOM Construction**
- The CSS files (linked or inline) are fetched and parsed in parallel
- Creates a **CSSOM (CSS Object Model)** — a tree of style rules

Example:
```css
h1 { color: blue; }
```

CSSOM:
```
h1 → { color: blue }
```

#### **1️⃣1️⃣ JavaScript Parsing and Execution (V8 Engine)**
- The HTML parser finds a `<script>` tag → **pauses DOM parsing** (blocking render) unless it's `async` or `defer`
- JS code is sent to **V8 engine**:
  1. Parsed → AST (Abstract Syntax Tree)
  2. Ignition → Bytecode
  3. TurboFan → Optimized machine code
- JS modifies DOM/CSSOM via the Web APIs

#### **1️⃣2️⃣ Render Tree Construction**
- The browser combines **DOM + CSSOM → Render Tree**
- The Render Tree only includes **visible elements** (no `<head>` or `display:none`)

#### **1️⃣3️⃣ Layout (Reflow)**
- Calculates the **exact position and size** (x, y, width, height) for each Render Tree node
- Dependent on viewport size, fonts, etc.

💡 Changing layout-affecting properties (like `width`, `padding`, `display`) triggers **reflows**

#### **1️⃣4️⃣ Paint**
- Each node is converted to **pixels** — colors, borders, shadows, etc.
- Painted into **layers** (like Photoshop layers)

#### **1️⃣5️⃣ Compositing (GPU)**
- Layers are **sent to the GPU**, where they are **composited** together
- Browser handles scrolling, animations, and opacity changes on the GPU for smoothness

✅ The final frame is now displayed on screen

#### **1️⃣6️⃣ JavaScript Event Loop Integration**
After rendering:
- **Event Loop** takes over — handling:
  - User events (`click`, `scroll`)
  - Microtasks (Promises, async/await)
  - Macrotasks (timers, I/O)
  - Rendering cycles (frames)
- Browser repeats: **Run → Render → Idle → Repeat (~60 FPS)**

#### **1️⃣7️⃣ Optimization & Caching**
- Browser stores responses in caches for reuse
- Prefetches DNS and resources for faster next visits
- Uses speculative parsing (loads JS/CSS ahead of time)

#### **1️⃣8️⃣ Security Layers**
- **Same-Origin Policy** → isolates sites
- **CSP (Content Security Policy)** → prevents XSS
- **Sandboxing** → each tab = isolated process
- **HTTPS Enforcement** → ensures encrypted communication

### 🧠 **Full Summary Flow**

| Stage | System / Component | Description |
|-------|-------------------|-------------|
| 1 | User Input | You type URL |
| 2 | Cache | Check local cache |
| 3 | DNS | Resolve domain to IP |
| 4 | TCP | Establish connection |
| 5 | TLS | Secure the channel |
| 6 | HTTP Request | Send GET request |
| 7 | Server | Process request |
| 8 | HTTP Response | Return HTML |
| 9 | HTML Parser | Build DOM |
| 10 | CSS Parser | Build CSSOM |
| 11 | JS Engine (V8) | Execute scripts |
| 12 | Render Tree | Combine DOM + CSSOM |
| 13 | Layout | Compute geometry |
| 14 | Paint | Convert to pixels |
| 15 | Composite | GPU merges layers |
| 16 | Event Loop | Handle async + re-renders |
| 17 | Cache Update | Save for next load |
| 18 | Security | Sandboxing, HTTPS, SOP |

### 💡 **Interview Summary Answer**

> "When you type a URL, the browser resolves DNS, establishes TCP/TLS connections, sends an HTTP request, and receives a response. Then the rendering engine parses HTML, builds the DOM and CSSOM, executes JS, combines them into a render tree, performs layout and paint, and finally composites layers to display pixels on screen — all managed via the event loop for interactivity."

---

## 📋 **Summary**

This comprehensive guide covers:

### **HTML Fundamentals**
- Document structure, semantic elements, forms, and accessibility
- HTML5 features, media elements, and performance optimization
- Common patterns and best practices

### **Browser Internals**
- Complete end-to-end flow from URL input to rendered page
- 18 detailed steps covering networking, rendering, and execution
- Deep dive into DOM construction, CSSOM, JavaScript execution, and GPU compositing

### **Key Interview Topics**
- Semantic HTML and accessibility (WCAG, ARIA)
- Performance optimization and SEO
- Browser rendering pipeline and event loop
- Security considerations and caching strategies

### **Quick Reference**
- Essential HTML elements and attributes
- Form validation and input types
- ARIA landmarks and accessibility patterns
- Meta tags and performance hints

**Master these concepts to excel in front-end engineering interviews! 🚀**

**Good luck with your HTML interview! 🎉**
