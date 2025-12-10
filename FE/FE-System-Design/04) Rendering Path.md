# 🎨 Rendering Path

---

## 📍 Navigation

<div align="center">

[← Previous: Networking](03%29%20Networking.md) • [Home: Questions Index](question.md) • [Next: HTML Internals →](05%29%20HTML%20Internals.md)

[📋 Cheatsheet](FE-System-Design%20Interview%20Cheatsheet.md)

</div>

---

---

## Q8. 🎨 Critical Rendering Path

The Critical Rendering Path is the sequence of steps the browser takes to convert HTML, CSS, and JavaScript into pixels on the screen. Understanding this path helps you optimize page load performance and create faster, more responsive websites. Every millisecond matters - a 100ms delay can reduce conversions by 1%.

---

## 1. 📄 HTML Parsing and DOM Construction

When the browser receives HTML bytes over the network, it can't use them directly. It needs to parse the HTML and build a data structure (the DOM) that JavaScript can manipulate and the browser can render.

### 🔹 Process

**Tokenization**

* The browser reads HTML character by character and breaks it into tokens

* Tokens are the basic building blocks: opening tags (`<div>`), closing tags (`</div>`), attributes, text content

* Example: `<div class="container">Hello</div>` becomes tokens: `<div>`, `class="container"`, `Hello`, `</div>`

* This happens incrementally - the browser doesn't wait for the entire HTML to download

**Tree Construction**

* Tokens are converted into DOM nodes (objects that represent HTML elements)

* The browser builds a tree structure based on the HTML hierarchy

* Parent-child relationships are established (a `<div>` contains a `<p>`, etc.)

* This creates the DOM (Document Object Model) tree

**DOM Tree**

* The DOM tree is a hierarchical tree structure representing your HTML

* Each HTML element becomes a node in the tree

* The tree structure makes it easy to navigate and manipulate elements

* JavaScript can access and modify this tree (that's how frameworks like React work)

**Incremental Parsing**

* The browser doesn't wait for the entire HTML to download before starting to parse

* As soon as it receives some HTML bytes, it starts parsing

* This allows the browser to start building the DOM and downloading other resources early

* This is why you see pages render progressively (content appears as it downloads)

### 🔹 Blocking Resources

Understanding what blocks parsing and rendering is crucial for performance optimization.

**JavaScript Blocks Parsing**

* When the browser encounters a `<script>` tag, it **stops HTML parsing immediately**

* The browser downloads the JavaScript file (if external) or executes inline JavaScript

* After JavaScript executes, HTML parsing resumes

* **Why it blocks**: JavaScript can modify the DOM (`document.write()`, `document.createElement()`), so the browser must execute it before continuing to parse

* **Impact**: A large JavaScript file in the `<head>` can delay the entire page from rendering

* **Solution**: Use `async` or `defer` attributes, or move scripts to the bottom of `<body>`

**CSS Blocks Rendering**

* CSS must be downloaded and parsed before the browser can render anything

* The browser won't paint pixels until CSS is ready (prevents Flash of Unstyled Content - FOUC)

* **Why it blocks**: CSS determines how elements look - the browser needs to know styles before rendering

* **Impact**: Large CSS files delay First Contentful Paint (FCP)

* **Solution**: Inline critical CSS, defer non-critical CSS, minimize CSS size

**Images Don't Block**

* Images are downloaded asynchronously - these images don't block HTML parsing or initial rendering

* The browser can render the page structure first, then fill in images as those images load

* **Why images don't block**: Images don't affect the page structure or layout (unless these images are in the critical path)

* **Impact**: Large images can still slow down the page, but these images don't prevent initial render

* **Solution**: Use lazy loading, optimize image sizes, use modern formats (WebP, AVIF)

---

## 2. 🎨 CSS Parsing and CSSOM Construction

CSS is parsed to build the CSS Object Model (CSSOM) tree, which represents all CSS rules and how these rules apply to elements. The browser needs this to know how to style each element.

### 🔹 Process

**Parse CSS**

* The browser reads CSS rules from stylesheets (external files, `<style>` tags, inline styles)

* CSS is parsed into rules: selectors, properties, values

* Example: `.container { color: red; }` becomes a rule with selector `.container` and property `color: red`

**Resolve Conflicts (Cascade and Specificity)**

* Multiple CSS rules might apply to the same element

* The browser uses cascade and specificity to determine which rule wins

* **Cascade**: Later rules override earlier ones (if specificity is equal)

* **Specificity**: More specific selectors win (`.container p` beats `p`)

* **Important**: `!important` declarations override normal rules

* This determines the final styles for each element

**Build CSSOM**

* The browser builds a tree structure (CSSOM) representing CSS rules

* The CSSOM is similar to the DOM but for styles

* It represents how styles cascade and apply to elements

* This tree is used to compute final styles for each DOM element

**Calculate Computed Styles**

* For each element in the DOM, the browser calculates its final (computed) styles

* This combines: browser defaults, user styles, author styles, cascade, specificity

* The result is a set of final CSS properties for each element

* Example: An element might have `color: red` after all rules are resolved

### 🔹 CSS is Render-Blocking

**Why CSS Blocks Rendering:**

* The browser won't render (paint pixels) until CSS is parsed

* This prevents Flash of Unstyled Content (FOUC) - where content appears unstyled briefly

* The browser needs to know styles before rendering to avoid layout shifts

* **All CSS must be downloaded and parsed before first paint**

**Performance Impact:**

* Large CSS files delay First Contentful Paint (FCP)

* Multiple CSS files mean waiting for all of them

* Slow network connections make this worse

* This is why CSS optimization is critical for performance

**Optimization Strategies:**

* **Inline critical CSS**: Put above-the-fold styles directly in `<head>` to avoid a network request

* **Defer non-critical CSS**: Load below-the-fold styles after initial render

* **Minimize CSS**: Remove unused CSS, minify, compress

* **Split CSS**: Load only the CSS needed for the current page

* **Use media queries**: Load CSS conditionally (e.g., print styles only when printing)

---

## 3. 💡 JavaScript Execution

JavaScript execution plays a crucial role in the critical rendering path and can significantly impact page load performance.

### 🔹 Script Loading Strategies

**Blocking (Default)**

```html
<script src="app.js"></script>

```

* **Behavior**: When the browser encounters this script, it **stops HTML parsing immediately**

* **Download**: The browser downloads the script, and parsing remains blocked during download

* **Execution**: As soon as download completes, the script executes immediately

* **Order**: Scripts execute in the order these scripts appear in the HTML

* **DOM access**: The DOM may not be fully constructed when the script runs

* **Use case**: Scripts that must run before the page continues (rare - usually not recommended)

* **Performance impact**: Can significantly delay page rendering, especially if the script is large or slow to download

**Async**

```html
<script async src="app.js"></script>

```

* **Behavior**: The script downloads in parallel with HTML parsing (non-blocking download)

* **Download**: Downloads happen concurrently - HTML parsing continues

* **Execution**: As soon as the download completes, the script executes **immediately**, which **interrupts HTML parsing**

* **Order**: Execution order is **not guaranteed** - whichever script finishes downloading first executes first

* **DOM access**: The DOM may not be fully constructed when the script runs

* **Use case**: Independent scripts that don't depend on DOM or other scripts (analytics like Google Analytics, ads, widgets)

* **Performance impact**: Better than blocking, but can still interrupt parsing if it executes while HTML is being parsed

**Defer**

```html
<script defer src="app.js"></script>

```

* **Behavior**: The script downloads in parallel with HTML parsing, and execution is deferred

* **Download**: Downloads happen concurrently - HTML parsing continues

* **Execution**: Scripts execute **after HTML parsing is complete**, in order, before `DOMContentLoaded` fires

* **Order**: Execution order **is guaranteed** - scripts execute in the order these scripts appear in HTML

* **DOM access**: The DOM is fully constructed when the script runs (safe to access DOM)

* **Use case**: Scripts that need the full DOM (most application JavaScript, frameworks like React/Vue)

* **Performance impact**: Best for performance - doesn't block parsing, executes when DOM is ready

### 🔹 Comparison Table

| Attribute | Blocking | Async | Defer |
|-----------|----------|-------|-------|
| **HTML Parsing** | Blocked | Not blocked | Not blocked |
| **Download** | Blocking | Parallel | Parallel |
| **Execution** | Immediate | When ready | After parsing |
| **Execution Order** | Guaranteed | Not guaranteed | Guaranteed |
| **DOM Ready** | May not be | May not be | Yes |

📌 **In simple terms**: JavaScript execution blocks HTML parsing by default. Use `async` for independent scripts, use `defer` for scripts that need DOM.

---

## 4. 🌳 Render Tree Construction

The render tree combines DOM and CSSOM, but only includes visible elements (excludes `display: none`, `<head>`, etc.).

### 🔹 Process

* **Combine DOM + CSSOM**: Match DOM nodes with CSS rules

* **Filter invisible elements**: Remove elements that won't be displayed

* **Create render tree**: Tree of visible elements with computed styles

---

## 5. 📐 Layout (Reflow)

Layout calculates the exact position and size of each element on the page.

### 🔹 Process

* **Calculate dimensions**: Width, height, position for each element

* **Box model**: Content, padding, border, margin calculations

* **Positioning**: Normal flow, absolute, fixed, relative positioning

### 🔹 Layout is Expensive

* Recalculating layout (reflow) is CPU-intensive

* Triggers: Changing element size, adding/removing elements, window resize

* Should be minimized for performance

---

## 6. 💡 Paint

Paint fills in the pixels for each element based on the layout information.

### 🔹 Process

* **Create paint records**: List of drawing operations

* **Fill pixels**: Draw backgrounds, borders, text, images

* **Layers**: Elements may be painted to separate layers

---

## 7. 💡 Compositing

Compositing combines different layers into the final image displayed on screen.

### 🔹 Process

* **Layer creation**: Some elements create new layers (transform, opacity, will-change)

* **Layer painting**: Each layer is painted separately

* **Compositing**: Layers are combined in correct order

* **GPU acceleration**: Compositing can use GPU for better performance

---

## ⭐ Summary — 10-second Interview Version

> "The critical rendering path: browser parses HTML into DOM tree, parses CSS into CSSOM tree, executes JavaScript, combines DOM and CSSOM into render tree, calculates layout, paints pixels, and composites layers. Optimize by using async/defer for scripts, minimizing render-blocking resources, and reducing layout calculations."

---

## ⭐ Extra Points (If Interviewer Asks More)

### What blocks rendering?

CSS is render-blocking (must be parsed first). JavaScript blocks HTML parsing when encountered (unless async/defer). Images and fonts don't block initial render.

### How to optimize critical rendering path?

Inline critical CSS, defer non-critical CSS, use async/defer for JavaScript, minimize layout thrashing, use CSS transforms instead of changing position/size.

### What's the difference between async and defer?

async downloads in parallel and executes immediately when ready (may interrupt parsing). defer downloads in parallel but executes after HTML parsing completes (maintains order).

---

---

## 📍 Navigation

<div align="center">

[← Previous: Networking](03%29%20Networking.md) • [Home: Questions Index](question.md) • [Next: HTML Internals →](05%29%20HTML%20Internals.md)

[📋 Cheatsheet](FE-System-Design%20Interview%20Cheatsheet.md)

</div>

---
