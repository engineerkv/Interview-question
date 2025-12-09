# 📄 HTML Internals

---

## 📍 Navigation

<div align="center">

[← Previous: Rendering Path](04%29%20Rendering%20Path.md) • [Home: Questions Index](question.md) • [Next: CSS Internals →](06%29%20CSS%20Internals.md)

[📋 Cheatsheet](FE-System-Design%20Interview%20Cheatsheet.md)

</div>

---

## Q8.5. How HTML Works Internally

HTML (HyperText Markup Language) is the standard markup language for creating web pages. Understanding how HTML works under the hood helps you write better markup, optimize performance, and debug rendering issues. When browsers process HTML, they handle parsing, DOM construction, tokenization, tree building, and rendering. This knowledge is crucial for senior developers - it helps you understand why certain markup patterns work better, how to optimize HTML for performance, and how browsers interpret your code.

---

## 1. HTML Parsing Process

### 🔹 Tokenization (Lexical Analysis)

The first step in HTML parsing is breaking the HTML source into tokens:

**What is Tokenization:**
* Reads HTML character by character
* Identifies HTML tags, attributes, text content
* Handles special characters and entities
* Produces stream of tokens for parser

**Token Types:**
* **Start tag tokens**: `<div>`, `<p>`, `<img>`
* **End tag tokens**: `</div>`, `</p>`
* **Self-closing tags**: `<img />`, `<br />`
* **Attribute tokens**: `class="container"`, `id="main"`
* **Text tokens**: Content between tags
* **Comment tokens**: `<!-- comment -->`
* **DOCTYPE tokens**: `<!DOCTYPE html>`

**Character Entity Handling:**
* `&lt;` → `<`
* `&gt;` → `>`
* `&amp;` → `&`
* `&quot;` → `"`
* `&nbsp;` → Non-breaking space
* Numeric entities: `&#65;` → `A`

**Example:**
```html
<div class="container">Hello</div>
```

Tokens produced:
1. Start tag: `<div>`
2. Attribute: `class="container"`
3. Text: `Hello`
4. End tag: `</div>`

**Error Handling:**
* Malformed tags are handled gracefully
* Missing closing tags are auto-closed
* Invalid attributes are ignored
* Browsers are very forgiving (HTML5 error handling)

### 🔹 Tree Construction (DOM Building)

After tokenization, tokens are converted into a DOM tree:

**How Tree Construction Works:**
* Uses stack-based algorithm
* Start tags create elements and push to stack
* End tags pop from stack
* Text nodes are added to current element
* Builds parent-child relationships

**DOM Tree Structure:**
* **Document node**: Root of tree
* **Element nodes**: HTML elements (`<div>`, `<p>`, etc.)
* **Text nodes**: Text content
* **Attribute nodes**: Element attributes
* **Comment nodes**: HTML comments

**Tree Building Algorithm:**
1. Create Document node
2. For each token:
   - Start tag: Create element, add to current parent, push to stack
   - End tag: Pop from stack
   - Text: Create text node, add to current parent
   - Comment: Create comment node, add to current parent
3. Handle special cases (script tags, void elements)

**Example:**
```html
<html>
  <head>
    <title>Page</title>
  </head>
  <body>
    <div>Hello</div>
  </body>
</html>
```

DOM tree:
```
Document
└── html
    ├── head
    │   └── title
    │       └── "Page" (text)
    └── body
        └── div
            └── "Hello" (text)
```

**Special Elements:**
* **Void elements**: `<img>`, `<br>`, `<hr>` (no closing tag)
* **Script tags**: Pause parsing, execute script, resume
* **Style tags**: Parse CSS, apply styles
* **Form elements**: Special handling for form state

### 🔹 Incremental Parsing

Browsers parse HTML incrementally (as it arrives):

**Why Incremental Parsing:**
* HTML arrives in chunks over network
* Don't wait for entire document
* Start rendering as soon as possible
* Improves perceived performance

**How It Works:**
* Parse tokens as they arrive
* Build DOM tree incrementally
* Trigger rendering when enough content
* Continue parsing in background

**Benefits:**
* Faster Time to First Paint (TTFP)
* Better user experience
* Progressive rendering
* Can start executing scripts earlier

**Challenges:**
* Scripts can modify DOM during parsing
* Need to handle incomplete trees
* Re-parsing if scripts modify HTML

📌 **In simple terms**: HTML parsing breaks source into tokens (tags, attributes, text), then builds a DOM tree using a stack-based algorithm. Browsers parse incrementally as HTML arrives, enabling progressive rendering and faster initial display.

---

## 2. DOM (Document Object Model)

### 🔹 DOM Tree Structure

The DOM is a tree representation of HTML:

**Node Types:**
* **Document**: Root node (entire document)
* **Element**: HTML elements (`<div>`, `<p>`, etc.)
* **Text**: Text content
* **Attribute**: Element attributes (deprecated in DOM4)
* **Comment**: HTML comments
* **DocumentType**: DOCTYPE declaration
* **DocumentFragment**: Temporary container

**Node Relationships:**
* **Parent**: Element containing this node
* **Children**: Direct child nodes
* **Siblings**: Nodes with same parent
* **Descendants**: All nodes in subtree
* **Ancestors**: All nodes from root to this node

**Node Properties:**
* `nodeType`: Type of node (1 = Element, 3 = Text, etc.)
* `nodeName`: Name of node (tag name for elements)
* `nodeValue`: Value of node (text content for text nodes)
* `parentNode`: Parent node
* `childNodes`: Live NodeList of children
* `firstChild`, `lastChild`: First/last child
* `nextSibling`, `previousSibling`: Adjacent siblings

**Example:**
```javascript
// Accessing DOM nodes
const div = document.querySelector('div');
console.log(div.nodeType); // 1 (Element)
console.log(div.nodeName); // "DIV"
console.log(div.firstChild.nodeValue); // Text content
```

### 🔹 Element Interface

Elements extend Node with element-specific properties:

**Element Properties:**
* `tagName`: Tag name (uppercase)
* `id`: Element ID
* `className`: CSS class names
* `classList`: DOMTokenList for classes
* `attributes`: NamedNodeMap of attributes
* `innerHTML`: HTML content (get/set)
* `outerHTML`: Element and HTML content
* `textContent`: Text content (no HTML)
* `innerText`: Visible text (respects CSS)

**Element Methods:**
* `getAttribute(name)`: Get attribute value
* `setAttribute(name, value)`: Set attribute
* `removeAttribute(name)`: Remove attribute
* `hasAttribute(name)`: Check if attribute exists
* `querySelector(selector)`: Find descendant
* `querySelectorAll(selector)`: Find all descendants
* `closest(selector)`: Find ancestor
* `matches(selector)`: Check if matches selector

**Example:**
```javascript
const div = document.createElement('div');
div.id = 'container';
div.className = 'box';
div.setAttribute('data-id', '123');
div.innerHTML = '<p>Hello</p>';

console.log(div.getAttribute('data-id')); // "123"
console.log(div.textContent); // "Hello"
```

### 🔹 Live vs Static Collections

DOM collections can be live or static:

**Live Collections:**
* Update automatically when DOM changes
* `childNodes`, `children`, `attributes`
* Can cause performance issues
* Iterate carefully (cache length)

**Static Collections:**
* Snapshot at time of query
* `querySelectorAll()` returns NodeList (static in most cases)
* Safer for iteration
* Don't update automatically

**Example:**
```javascript
// Live collection
const children = div.children; // HTMLCollection (live)
div.appendChild(document.createElement('p'));
console.log(children.length); // Updated automatically

// Static collection
const nodes = div.querySelectorAll('p'); // NodeList (static)
div.appendChild(document.createElement('p'));
console.log(nodes.length); // Not updated
```

📌 **In simple terms**: DOM is a tree of nodes representing HTML. Elements have properties (id, className) and methods (querySelector, setAttribute). Collections can be live (update automatically) or static (snapshot).

---

## 3. HTML5 Features

### 🔹 Semantic Elements

HTML5 introduced semantic elements for better structure:

**Semantic Elements:**
* `<header>`, `<footer>`, `<nav>`, `<main>`
* `<article>`, `<section>`, `<aside>`
* `<figure>`, `<figcaption>`
* `<time>`, `<mark>`, `<progress>`

**Benefits:**
* Better accessibility (screen readers)
* Clearer document structure
* SEO improvements
* Easier styling and maintenance

**Example:**
```html
<header>
  <nav>
    <ul>
      <li><a href="/">Home</a></li>
    </ul>
  </nav>
</header>
<main>
  <article>
    <h1>Title</h1>
    <p>Content</p>
  </article>
</main>
<footer>
  <p>Copyright</p>
</footer>
```

### 🔹 Form Enhancements

HTML5 added new form input types and attributes:

**New Input Types:**
* `email`, `url`, `tel`, `number`, `date`, `time`
* `color`, `range`, `search`, `file`
* Browser provides native validation

**New Attributes:**
* `required`: Field must be filled
* `pattern`: Regex validation
* `placeholder`: Hint text
* `autocomplete`: Browser autocomplete
* `min`, `max`, `step`: Number/date constraints

**Example:**
```html
<form>
  <input type="email" required placeholder="Email">
  <input type="number" min="0" max="100" step="1">
  <input type="date" min="2024-01-01">
  <button type="submit">Submit</button>
</form>
```

### 🔹 Media Elements

HTML5 added native media support:

**Video Element:**
* `<video>`: Native video playback
* Supports multiple formats (MP4, WebM, Ogg)
* Controls, autoplay, loop attributes
* JavaScript API for control

**Audio Element:**
* `<audio>`: Native audio playback
* Similar to video element
* Lighter weight

**Example:**
```html
<video controls width="640" height="360">
  <source src="video.mp4" type="video/mp4">
  <source src="video.webm" type="video/webm">
  Your browser doesn't support video.
</video>
```

### 🔹 Canvas and SVG

HTML5 provides graphics capabilities:

**Canvas:**
* `<canvas>`: 2D/3D graphics with JavaScript
* Pixel-based rendering
* Good for games, charts, animations
* JavaScript API for drawing

**SVG:**
* `<svg>`: Vector graphics
* XML-based, scalable
* Good for icons, illustrations
* CSS and JavaScript can style/control

**Example:**
```html
<!-- Canvas -->
<canvas id="myCanvas" width="200" height="200"></canvas>
<script>
  const ctx = document.getElementById('myCanvas').getContext('2d');
  ctx.fillStyle = 'red';
  ctx.fillRect(10, 10, 50, 50);
</script>

<!-- SVG -->
<svg width="200" height="200">
  <circle cx="50" cy="50" r="40" fill="blue"/>
</svg>
```

📌 **In simple terms**: HTML5 added semantic elements (header, nav, article), form enhancements (new input types, validation), media elements (video, audio), and graphics (canvas, SVG) for richer web applications.

---

## 4. Accessibility (A11y)

### 🔹 ARIA Attributes

ARIA (Accessible Rich Internet Applications) enhances accessibility:

**ARIA Roles:**
* `role="button"`, `role="dialog"`, `role="menu"`
* Define element purpose
* Help screen readers understand

**ARIA Properties:**
* `aria-label`: Accessible name
* `aria-labelledby`: Reference to labeling element
* `aria-describedby`: Reference to description
* `aria-hidden`: Hide from screen readers
* `aria-live`: Announce dynamic changes

**Example:**
```html
<button aria-label="Close dialog" aria-describedby="close-desc">
  ×
</button>
<span id="close-desc" class="sr-only">Closes the modal dialog</span>
```

### 🔹 Semantic HTML for Accessibility

Use semantic HTML for better accessibility:

**Headings:**
* Use `<h1>` through `<h6>` in order
* Don't skip levels
* One `<h1>` per page

**Lists:**
* Use `<ul>`, `<ol>`, `<li>` for lists
* Don't use divs for lists

**Forms:**
* Use `<label>` for form inputs
* Associate labels with inputs (`for` attribute or wrapping)
* Use `<fieldset>` and `<legend>` for groups

**Example:**
```html
<form>
  <fieldset>
    <legend>Contact Information</legend>
    <label for="email">Email:</label>
    <input type="email" id="email" name="email" required>
  </fieldset>
</form>
```

### 🔹 Keyboard Navigation

Ensure keyboard accessibility:

**Focus Management:**
* All interactive elements should be focusable
* Visible focus indicators
* Logical tab order
* Skip links for navigation

**Keyboard Events:**
* `Tab`: Move focus forward
* `Shift+Tab`: Move focus backward
* `Enter/Space`: Activate buttons/links
* `Arrow keys`: Navigate menus/lists

📌 **In simple terms**: Use ARIA attributes for complex interactions, semantic HTML for structure, and ensure keyboard navigation works. This makes websites accessible to screen readers and keyboard users.

---

## 5. Performance Optimization

### 🔹 HTML Optimization Techniques

Optimize HTML for better performance:

**Minification:**
* Remove whitespace and comments
* Reduce file size
* Faster download and parsing

**Defer and Async Scripts:**
* `defer`: Execute after HTML parsing
* `async`: Execute as soon as available
* Don't block HTML parsing

**Preload and Prefetch:**
* `<link rel="preload">`: Load critical resources early
* `<link rel="prefetch">`: Load resources for next page
* Improves perceived performance

**Example:**
```html
<!-- Defer script -->
<script src="app.js" defer></script>

<!-- Preload critical resource -->
<link rel="preload" href="font.woff2" as="font" type="font/woff2" crossorigin>

<!-- Prefetch next page -->
<link rel="prefetch" href="/next-page.html">
```

### 🔹 Critical Rendering Path

Optimize the critical rendering path:

**What is Critical Rendering Path:**
* Sequence of steps to render page
* HTML → DOM → CSSOM → Render Tree → Layout → Paint
* Optimize for faster rendering

**Optimization Strategies:**
* Inline critical CSS
* Defer non-critical CSS
* Minimize render-blocking resources
* Optimize HTML structure

📌 **In simple terms**: Minify HTML, use defer/async for scripts, preload critical resources, and optimize the critical rendering path for faster page loads.

---

## ⭐ Summary — Key Takeaways

**HTML Parsing:**
* Tokenization breaks HTML into tokens
* Tree construction builds DOM tree
* Incremental parsing enables progressive rendering

**DOM:**
* Tree structure of nodes
* Elements have properties and methods
* Live vs static collections

**HTML5 Features:**
* Semantic elements for structure
* Form enhancements for validation
* Media elements for rich content
* Canvas and SVG for graphics

**Accessibility:**
* ARIA attributes enhance accessibility
* Semantic HTML improves structure
* Keyboard navigation is essential

**Performance:**
* Minify HTML
* Defer/async scripts
* Preload critical resources
* Optimize critical rendering path

---

## 📍 Navigation

<div align="center">

[← Previous: Rendering Path](04%29%20Rendering%20Path.md) • [Home: Questions Index](question.md) • [Next: CSS Internals →](06%29%20CSS%20Internals.md)

[📋 Cheatsheet](FE-System-Design%20Interview%20Cheatsheet.md)

</div>

---

