# 1. HTML Fundamentals (Q1–15)

---

## Q1. What is HTML and what does it stand for?

HTML stands for HyperText Markup Language - it's the standard markup language for creating web pages, describing structure and content using tags. HTML describes the structure and content of web pages using tags.

- **Trade-offs**: The catch is HTML5 is the current standard with semantic elements and modern features - hypertext enables links between pages, making the web interconnected. HTML is the structure, CSS is the styling, JavaScript is the behavior, but watch out - it's the foundation of all web development, works with CSS and JavaScript.

Example:

```html
<!DOCTYPE html>
<html>
  <head>
    <title>My Web Page</title>
  </head>
  <body>
    <h1>Welcome</h1>
  </body>
</html>
```

---

## Q2. What is the difference between HTML and XHTML?

XHTML is HTML written as XML with stricter syntax rules, while HTML5 is more forgiving and widely used, making it the modern standard. XHTML requires all tags closed, case-sensitive, and strict syntax.

- **Trade-offs**: The catch is XHTML requires quotes, proper nesting, and closing tags - HTML5's more forgiving syntax is better for rapid development. HTML5 is the current standard, XHTML is outdated, but watch out - HTML5 is the modern standard, XHTML is mostly legacy.

Example:

```html
<!-- HTML5 (more forgiving) -->
<img src="image.jpg" alt="description">
<br>

<!-- XHTML (strict) -->
<img src="image.jpg" alt="description" />
```

---

## Q3. What are HTML elements, tags, and attributes?

Elements are complete structures, tags are the markup syntax, and attributes provide additional information like links, classes, or IDs. Elements are opening tag, content, and closing tag together.

- **Trade-offs**: The catch is attributes provide additional information like `href`, `target`, `class` - some tags like `<img>` don't need closing tags (self-closing). Elements are the complete structure, tags are just the syntax, but watch out - tags are the markup syntax like `<a>` and `</a>`.

Example:

```html
<a href="https://example.com" target="_blank" class="link">
  Click here
</a>
<!-- <a> = opening tag, </a> = closing tag -->
<!-- href, target, class = attributes -->
<!-- Complete structure = element -->
```

---

## Q4. What is the difference between block and inline elements?

Block elements take full width and create new lines, while inline elements flow with text and don't break lines, perfect for text styling. Block elements take full width, create new lines, can contain other elements.

- **Trade-offs**: The catch is inline elements flow with text, don't break lines, can't contain block elements - can change element behavior with CSS `display` property. Block elements are for structure, inline for text flow, but watch out - block for layout, inline for text styling and links.

Example:

```html
<!-- Block: full width, new line -->
<div>Block element</div>
<p>Paragraph</p>

<!-- Inline: flows with text -->
<span>Inline text</span> and <a href="#">link</a>
```

---

## Q5. What are the basic structure elements of an HTML document?

Every HTML document needs DOCTYPE, html root element, head for metadata, and body for content - DOCTYPE prevents quirks mode. DOCTYPE tells browser which HTML version to use, must be first line.

- **Trade-offs**: The catch is head contains metadata not displayed on page (title, meta, links) - body contains visible page content that users see. DOCTYPE prevents quirks mode, ensures consistent rendering, but watch out - html is root element containing all page content.

Example:

```html
<!DOCTYPE html>
<html>
  <head>
    <meta charset="UTF-8">
    <title>Document Title</title>
  </head>
  <body>
    <h1>Hello World</h1>
  </body>
</html>
```

---

## Q6. What is the DOCTYPE declaration and why is it important?

DOCTYPE tells the browser which HTML version to use - it triggers standards mode rendering, preventing quirks mode and ensuring consistency. DOCTYPE prevents browser from using quirks mode rendering.

- **Trade-offs**: The catch is HTML5's simple `<!DOCTYPE html>` is all you need - must be the very first line in HTML document. Missing DOCTYPE can cause layout issues and inconsistent rendering, but watch out - ensures consistent rendering across different browsers.

Example:

```html
<!-- HTML5 DOCTYPE (simple) -->
<!DOCTYPE html>

<!-- Older HTML versions (complex) -->
<!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 4.01 Transitional//EN">
```

---

## Q7. What are HTML comments and how do you write them?

HTML comments are non-displayed text used for documentation and debugging - they're visible in page source, not secure for hiding secrets. Comments document code or temporarily disable HTML without deleting.

- **Trade-offs**: The catch is syntax starts with `<!--` and ends with `-->` - can't nest comments inside other comments. Comments are visible in page source, not secure for hiding secrets, but watch out - good for documentation, debugging, or hiding code temporarily.

Example:

```html
<!-- Single-line comment -->
<!-- Multi-line comment
     spans multiple lines -->
<!-- <div>Hidden code</div> -->
```

---

## Q8. What is the difference between `<div>` and `<span>`?

`<div>` is a block-level container for layout, while `<span>` is an inline container for styling or grouping text - both are generic with no semantic meaning. `<div>` is block-level, `<span>` is inline.

- **Trade-offs**: The catch is both are generic containers with no semantic meaning - use semantic elements when possible instead of generic containers. Semantic HTML is preferred over generic div/span, but watch out - `<div>` for layout, `<span>` for text styling.

Example:

```html
<div class="container">
  <p>This is a paragraph with <span class="highlight">highlighted text</span> inside.</p>
  <div class="section">This is a section</div>
</div>
```

---

## Q9. What are HTML entities and when should you use them?

HTML entities are special codes for characters that have special meaning in HTML or aren't on keyboard - they prevent HTML from interpreting special characters as code. Entities display special characters that HTML interprets as code.

- **Trade-offs**: The catch is common entities: `&lt;` for <, `&gt;` for >, `&amp;` for &, `&nbsp;` for space - syntax starts with `&` and ends with `;`. Entities prevent HTML from interpreting special characters as code, but watch out - good for displaying code examples, copyright symbols, currency symbols.

Example:

```html
<p>&lt;div&gt; is a tag</p>
<p>Copyright &copy; 2024</p>
<p>Price: &euro;25.99</p>
```

---

## Q10. What is the difference between `<strong>` and `<b>` tags?

`<strong>` indicates importance and meaning, while `<b>` is purely visual styling - screen readers emphasize `<strong>` content, ignore `<b>`. `<strong>` has semantic meaning, `<b>` is purely visual.

- **Trade-offs**: The catch is screen readers emphasize `<strong>` content, ignore `<b>` - use `<strong>` for important text, `<b>` only when you need bold without meaning. Semantic HTML improves accessibility and SEO, but watch out - `<strong>` improves accessibility, `<b>` doesn't.

Example:

```html
<p>This is <strong>important</strong> information.</p>
<p>This is <b>bold</b> text for visual emphasis.</p>
```

---

## Q11. What is the difference between `<em>` and `<i>` tags?

`<em>` indicates emphasis and meaning, while `<i>` is purely visual styling - screen readers stress `<em>` content, ignore `<i>`. `<em>` has semantic meaning, `<i>` is purely visual.

- **Trade-offs**: The catch is screen readers stress `<em>` content, ignore `<i>` - use `<em>` for emphasized text, `<i>` for foreign words or technical terms. Semantic tags help screen readers understand content better, but watch out - `<em>` improves accessibility, `<i>` doesn't.

Example:

```html
<p>This is <em>emphasized</em> text.</p>
<p>This is <i>italic</i> text for visual styling.</p>
<p><i>Homo sapiens</i> is the scientific name.</p>
```

---

## Q12. How do you create hyperlinks in HTML?

Use the `<a>` tag with `href` attribute to create clickable links - descriptive link text improves accessibility and SEO. `<a href="url">link text</a>` creates clickable links.

- **Trade-offs**: The catch is use `rel="noopener"` with `target="_blank"` for security - use `#` followed by element ID for page anchors. Descriptive link text improves accessibility and SEO, but watch out - good for navigation, external links, email links, phone links.

Example:

```html
<a href="https://example.com">External link</a>
<a href="/about.html">Internal link</a>
<a href="#section1">Anchor link</a>
<a href="mailto:email@example.com">Email link</a>
```

---

## Q13. What are the different types of lists in HTML?

HTML supports three list types: unordered (`<ul>`), ordered (`<ol>`), and definition (`<dl>`) - semantic list types improve accessibility and styling. `<ul>` creates bulleted lists for items without order.

- **Trade-offs**: The catch is `<dl>` creates definition lists with terms and descriptions - real-world use: navigation menus, step-by-step instructions, glossaries. Semantic list types improve accessibility and styling, but watch out - `<ol>` creates numbered lists for sequential items.

Example:

```html
<ul>
  <li>Item 1</li>
  <li>Item 2</li>
</ul>
<ol>
  <li>First step</li>
  <li>Second step</li>
</ol>
<dl>
  <dt>HTML</dt>
  <dd>HyperText Markup Language</dd>
</dl>
```

---

## Q14. How do you create tables in HTML?

Use `<table>`, `<tr>`, `<td>`, and `<th>` elements to create structured data tables - tables are for tabular data, not layout. `<table>` contains `<tr>` (rows) which contain `<td>` (data) or `<th>` (headers).

- **Trade-offs**: The catch is use `<thead>`, `<tbody>`, `<tfoot>` for better structure - use `<th>` for headers, `<caption>` for table descriptions. Tables are for tabular data, not layout, but watch out - good for displaying structured data like schedules, statistics, or comparisons.

Example:

```html
<table>
  <thead>
    <tr>
      <th>Name</th>
      <th>Age</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>John</td>
      <td>30</td>
    </tr>
  </tbody>
</table>
```

---

## Q15. What is the purpose of the `<meta>` tag?

`<meta>` tags provide metadata about the HTML document for browsers and search engines - they're crucial for SEO and mobile optimization. Provide metadata not displayed on page but used by browsers and search engines.

- **Trade-offs**: The catch is viewport meta is essential for responsive design on mobile devices - description meta tag is used by search engines for snippets. Meta tags are crucial for SEO and mobile optimization, but watch out - good for character encoding, mobile viewport, SEO descriptions, social sharing.

Example:

```html
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<meta name="description" content="Page description">
<meta name="keywords" content="keyword1, keyword2">
```

---
