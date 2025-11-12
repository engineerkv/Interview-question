# 🧠 1. HTML Fundamentals (Q1–15)

---

## 🧩 Q1. What is HTML and what does it stand for?

### 🧠 Concept

HTML stands for HyperText Markup Language. It's the standard markup language for creating web pages, describing structure and content using tags.

---

### 💡 Example

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

### 🔍 Deep Insights

* **Rule:** HTML describes the structure and content of web pages using tags.
* **Use Case:** Foundation of all web development, works with CSS and JavaScript.
* **Common Mistake:** HTML5 is the current standard with semantic elements and modern features.
* **Pro Tip:** Hypertext enables links between pages, making the web interconnected.

---

### ⭐ Senior Takeaway

HTML is the structure, CSS is the styling, JavaScript is the behavior.

---

## 🧩 Q2. What is the difference between HTML and XHTML?

### 🧠 Concept

XHTML is HTML written as XML with stricter syntax rules. HTML5 is more forgiving and widely used, making it the modern standard.

---

### 💡 Example

```html
<!-- HTML5 (more forgiving) -->
<img src="image.jpg" alt="description">
<br>

<!-- XHTML (strict) -->
<img src="image.jpg" alt="description" />
```

---

### 🔍 Deep Insights

* **Rule:** XHTML requires all tags closed, case-sensitive, and strict syntax.
* **Use Case:** HTML5 is the modern standard, XHTML is mostly legacy.
* **Common Mistake:** XHTML requires quotes, proper nesting, and closing tags.
* **Pro Tip:** HTML5's more forgiving syntax is better for rapid development.

---

### ⭐ Senior Takeaway

HTML5 is the current standard, XHTML is outdated.

---

## 🧩 Q3. What are HTML elements, tags, and attributes?

### 🧠 Concept

Elements are complete structures. Tags are the markup syntax. Attributes provide additional information like links, classes, or IDs.

---

### 💡 Example

```html
<a href="https://example.com" target="_blank" class="link">
  Click here
</a>
<!-- <a> = opening tag, </a> = closing tag -->
<!-- href, target, class = attributes -->
<!-- Complete structure = element -->
```

---

### 🔍 Deep Insights

* **Rule:** Elements are opening tag, content, and closing tag together.
* **Use Case:** Tags are the markup syntax like `<a>` and `</a>`.
* **Common Mistake:** Attributes provide additional information like `href`, `target`, `class`.
* **Pro Tip:** Some tags like `<img>` don't need closing tags (self-closing).

---

### ⭐ Senior Takeaway

Elements are the complete structure, tags are just the syntax.

---

## 🧩 Q4. What is the difference between block and inline elements?

### 🧠 Concept

Block elements take full width and create new lines. Inline elements flow with text and don't break lines, perfect for text styling.

---

### 💡 Example

```html
<!-- Block: full width, new line -->
<div>Block element</div>
<p>Paragraph</p>

<!-- Inline: flows with text -->
<span>Inline text</span> and <a href="#">link</a>
```

---

### 🔍 Deep Insights

* **Rule:** Block elements take full width, create new lines, can contain other elements.
* **Use Case:** Inline elements flow with text, don't break lines, can't contain block elements.
* **Common Mistake:** Block for layout, inline for text styling and links.
* **Pro Tip:** Can change element behavior with CSS `display` property.

---

### ⭐ Senior Takeaway

Block elements are for structure, inline for text flow.

---

## 🧩 Q5. What are the basic structure elements of an HTML document?

### 🧠 Concept

Every HTML document needs DOCTYPE, html root element, head for metadata, and body for content. DOCTYPE prevents quirks mode.

---

### 💡 Example

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

### 🔍 Deep Insights

* **Rule:** DOCTYPE tells browser which HTML version to use, must be first line.
* **Use Case:** html is root element containing all page content.
* **Common Mistake:** head contains metadata not displayed on page (title, meta, links).
* **Pro Tip:** body contains visible page content that users see.

---

### ⭐ Senior Takeaway

DOCTYPE prevents quirks mode, ensures consistent rendering.

---

## 🧩 Q6. What is the DOCTYPE declaration and why is it important?

### 🧠 Concept

DOCTYPE tells the browser which HTML version to use. It triggers standards mode rendering, preventing quirks mode and ensuring consistency.

---

### 💡 Example

```html
<!-- HTML5 DOCTYPE (simple) -->
<!DOCTYPE html>

<!-- Older HTML versions (complex) -->
<!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 4.01 Transitional//EN">
```

---

### 🔍 Deep Insights

* **Rule:** DOCTYPE prevents browser from using quirks mode rendering.
* **Use Case:** Ensures consistent rendering across different browsers.
* **Common Mistake:** HTML5's simple `<!DOCTYPE html>` is all you need.
* **Pro Tip:** Must be the very first line in HTML document.

---

### ⭐ Senior Takeaway

Missing DOCTYPE can cause layout issues and inconsistent rendering.

---

## 🧩 Q7. What are HTML comments and how do you write them?

### 🧠 Concept

HTML comments are non-displayed text used for documentation and debugging. They're visible in page source, not secure for hiding secrets.

---

### 💡 Example

```html
<!-- Single-line comment -->
<!-- Multi-line comment
     spans multiple lines -->
<!-- <div>Hidden code</div> -->
```

---

### 🔍 Deep Insights

* **Rule:** Comments document code or temporarily disable HTML without deleting.
* **Use Case:** Documentation, debugging, or hiding code temporarily.
* **Common Mistake:** Syntax starts with `<!--` and ends with `-->`.
* **Pro Tip:** Can't nest comments inside other comments.

---

### ⭐ Senior Takeaway

Comments are visible in page source, not secure for hiding secrets.

---

## 🧩 Q8. What is the difference between `<div>` and `<span>`?

### 🧠 Concept

`<div>` is a block-level container for layout. `<span>` is an inline container for styling or grouping text. Both are generic with no semantic meaning.

---

### 💡 Example

```html
<div class="container">
  <p>This is a paragraph with <span class="highlight">highlighted text</span> inside.</p>
  <div class="section">This is a section</div>
</div>
```

---

### 🔍 Deep Insights

* **Rule:** `<div>` is block-level, `<span>` is inline.
* **Use Case:** `<div>` for layout, `<span>` for text styling.
* **Common Mistake:** Both are generic containers with no semantic meaning.
* **Pro Tip:** Use semantic elements when possible instead of generic containers.

---

### ⭐ Senior Takeaway

Semantic HTML is preferred over generic div/span.

---

## 🧩 Q9. What are HTML entities and when should you use them?

### 🧠 Concept

HTML entities are special codes for characters that have special meaning in HTML or aren't on keyboard. They prevent HTML from interpreting special characters as code.

---

### 💡 Example

```html
<p>&lt;div&gt; is a tag</p>
<p>Copyright &copy; 2024</p>
<p>Price: &euro;25.99</p>
```

---

### 🔍 Deep Insights

* **Rule:** Entities display special characters that HTML interprets as code.
* **Use Case:** Common entities: `&lt;` for <, `&gt;` for >, `&amp;` for &, `&nbsp;` for space.
* **Common Mistake:** Display code examples, copyright symbols, currency symbols.
* **Pro Tip:** Syntax starts with `&` and ends with `;`.

---

### ⭐ Senior Takeaway

Entities prevent HTML from interpreting special characters as code.

---

## 🧩 Q10. What is the difference between `<strong>` and `<b>` tags?

### 🧠 Concept

`<strong>` indicates importance and meaning. `<b>` is purely visual styling. Screen readers emphasize `<strong>` content, ignore `<b>`.

---

### 💡 Example

```html
<p>This is <strong>important</strong> information.</p>
<p>This is <b>bold</b> text for visual emphasis.</p>
```

---

### 🔍 Deep Insights

* **Rule:** `<strong>` has semantic meaning, `<b>` is purely visual.
* **Use Case:** Screen readers emphasize `<strong>` content, ignore `<b>`.
* **Common Mistake:** Use `<strong>` for important text, `<b>` only when you need bold without meaning.
* **Pro Tip:** `<strong>` improves accessibility, `<b>` doesn't.

---

### ⭐ Senior Takeaway

Semantic HTML improves accessibility and SEO.

---

## 🧩 Q11. What is the difference between `<em>` and `<i>` tags?

### 🧠 Concept

`<em>` indicates emphasis and meaning. `<i>` is purely visual styling. Screen readers stress `<em>` content, ignore `<i>`.

---

### 💡 Example

```html
<p>This is <em>emphasized</em> text.</p>
<p>This is <i>italic</i> text for visual styling.</p>
<p><i>Homo sapiens</i> is the scientific name.</p>
```

---

### 🔍 Deep Insights

* **Rule:** `<em>` has semantic meaning, `<i>` is purely visual.
* **Use Case:** Screen readers stress `<em>` content, ignore `<i>`.
* **Common Mistake:** Use `<em>` for emphasized text, `<i>` for foreign words or technical terms.
* **Pro Tip:** `<em>` improves accessibility, `<i>` doesn't.

---

### ⭐ Senior Takeaway

Semantic tags help screen readers understand content better.

---

## 🧩 Q12. How do you create hyperlinks in HTML?

### 🧠 Concept

Use the `<a>` tag with `href` attribute to create clickable links. Descriptive link text improves accessibility and SEO.

---

### 💡 Example

```html
<a href="https://example.com">External link</a>
<a href="/about.html">Internal link</a>
<a href="#section1">Anchor link</a>
<a href="mailto:email@example.com">Email link</a>
```

---

### 🔍 Deep Insights

* **Rule:** `<a href="url">link text</a>` creates clickable links.
* **Use Case:** Navigation, external links, email links, phone links.
* **Common Mistake:** Use `rel="noopener"` with `target="_blank"` for security.
* **Pro Tip:** Use `#` followed by element ID for page anchors.

---

### ⭐ Senior Takeaway

Descriptive link text improves accessibility and SEO.

---

## 🧩 Q13. What are the different types of lists in HTML?

### 🧠 Concept

HTML supports three list types: unordered (`<ul>`), ordered (`<ol>`), and definition (`<dl>`). Semantic list types improve accessibility and styling.

---

### 💡 Example

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

### 🔍 Deep Insights

* **Rule:** `<ul>` creates bulleted lists for items without order.
* **Use Case:** `<ol>` creates numbered lists for sequential items.
* **Common Mistake:** `<dl>` creates definition lists with terms and descriptions.
* **Pro Tip:** Real-world use: navigation menus, step-by-step instructions, glossaries.

---

### ⭐ Senior Takeaway

Semantic list types improve accessibility and styling.

---

## 🧩 Q14. How do you create tables in HTML?

### 🧠 Concept

Use `<table>`, `<tr>`, `<td>`, and `<th>` elements to create structured data tables. Tables are for tabular data, not layout.

---

### 💡 Example

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

### 🔍 Deep Insights

* **Rule:** `<table>` contains `<tr>` (rows) which contain `<td>` (data) or `<th>` (headers).
* **Use Case:** Display structured data like schedules, statistics, or comparisons.
* **Common Mistake:** Use `<thead>`, `<tbody>`, `<tfoot>` for better structure.
* **Pro Tip:** Use `<th>` for headers, `<caption>` for table descriptions.

---

### ⭐ Senior Takeaway

Tables are for tabular data, not layout.

---

## 🧩 Q15. What is the purpose of the `<meta>` tag?

### 🧠 Concept

`<meta>` tags provide metadata about the HTML document for browsers and search engines. They're crucial for SEO and mobile optimization.

---

### 💡 Example

```html
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<meta name="description" content="Page description">
<meta name="keywords" content="keyword1, keyword2">
```

---

### 🔍 Deep Insights

* **Rule:** Provide metadata not displayed on page but used by browsers and search engines.
* **Use Case:** Character encoding, mobile viewport, SEO descriptions, social sharing.
* **Common Mistake:** Viewport meta is essential for responsive design on mobile devices.
* **Pro Tip:** Description meta tag is used by search engines for snippets.

---

### ⭐ Senior Takeaway

Meta tags are crucial for SEO and mobile optimization.

---
