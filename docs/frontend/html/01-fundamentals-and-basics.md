---
sidebar_label: "Fundamentals & Basics"
---
# 📝 1. Fundamentals & Basics (Q1–13)

---

## Q1. 📄 HTML and what it stands for

HTML stands for HyperText Markup Language - it's the standard markup language for creating web pages that describes structure and content using tags. HTML5 is the current standard with semantic elements and modern features that enable links between pages, making the web interconnected.

- **Trade-offs**: HTML is the structure layer, CSS handles styling, and JavaScript adds behavior - they work together, but HTML alone creates static pages without interactivity or visual design.

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

## Q2. 📄 HTML vs XHTML

XHTML is HTML written as XML with stricter syntax rules - it requires all tags closed, case-sensitive attributes, and proper nesting. HTML5 is more forgiving and widely used, making it the modern standard for web development.

- **Trade-offs**: XHTML's strict syntax catches errors early but slows development, while HTML5's forgiving syntax is better for rapid development - HTML5 is the current standard, XHTML is mostly legacy.

Example:

```html
<!-- HTML5 (more forgiving) -->
<img src="image.jpg" alt="description">
<br>

<!-- XHTML (strict) -->
<img src="image.jpg" alt="description" />

```

---

## Q3. 📄 HTML elements, tags, and attributes

Elements are complete structures made of opening tag, content, and closing tag - tags are the markup syntax like `<a>` and `</a>`, while attributes provide additional information like `href`, `target`, or `class`. Some tags like `<img>` are self-closing and don't need a closing tag.

- **Trade-offs**: Attributes extend element functionality but can clutter code if overused - use semantic attributes like `alt` for accessibility, and keep class names meaningful for maintainability.

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

## Q4. 🤔 Block vs inline elements

Block elements take full width and create new lines, perfect for layout structure, while inline elements flow with text and don't break lines, ideal for text styling and links. You can change element behavior with the CSS `display` property.

- **Trade-offs**: Block elements are for structure and can contain other elements, while inline elements can't contain block elements - use block for layout containers, inline for text styling and links.

Example:

```html
<!-- Block: full width, new line -->
<div>Block element</div>
<p>Paragraph</p>

<!-- Inline: flows with text -->
<span>Inline text</span> and <a href="#">link</a>

```

---

## Q5. 📝 DOCTYPE declaration and its importance

DOCTYPE tells the browser which HTML version to use and triggers standards mode rendering, preventing quirks mode and ensuring consistent layout across browsers. HTML5's simple `<!DOCTYPE html>` must be the very first line in the document.

- **Trade-offs**: Missing DOCTYPE triggers quirks mode with inconsistent rendering and layout issues - always include it as the first line to ensure standards-compliant rendering across all browsers.

Example:

```html
<!-- HTML5 DOCTYPE (simple) -->
<!DOCTYPE html>

<!-- Older HTML versions (complex) -->
<!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 4.01 Transitional//EN">

```

---

## Q6. 🤔 `<div>` vs `<span>`

`<div>` is a block-level container for layout structure, while `<span>` is an inline container for styling or grouping text - both are generic with no semantic meaning. Use semantic elements when possible instead of generic containers.

- **Trade-offs**: Both lack semantic meaning, so prefer semantic HTML elements like `<header>`, `<nav>`, `<section>` for better accessibility and SEO - use `<div>` for layout containers, `<span>` for inline text styling.

Example:

```html
<div class="container">
  <p>This is a paragraph with <span class="highlight">highlighted text</span> inside.</p>
  <div class="section">This is a section</div>

```

---

## Q7. 📄 HTML entities and when to use them

HTML entities are special codes starting with `&` and ending with `;` that display characters with special meaning in HTML or characters not on your keyboard. Common ones: `&lt;` for <, `&gt;` for >, `&amp;` for &, `&nbsp;` for non-breaking space.

- **Trade-offs**: Entities prevent HTML from interpreting special characters as code, perfect for displaying code examples, copyright symbols, or currency symbols - but they're less readable than the actual characters when possible.

Example:

```html
<p>&lt;div&gt; is a tag</p>
<p>Copyright &copy; 2024</p>
<p>Price: &euro;25.99</p>

```

---

## Q8. 🤔 `<strong>` vs `<b>` tags

`<strong>` indicates importance and has semantic meaning that screen readers emphasize, while `<b>` is purely visual styling with no semantic meaning. Use `<strong>` for important text, `<b>` only when you need bold styling without meaning.

- **Trade-offs**: `<strong>` improves accessibility and SEO because screen readers emphasize it, while `<b>` is ignored by assistive technologies - prefer `<strong>` for better accessibility unless you specifically need visual-only bold styling.

Example:

```html
<p>This is <strong>important</strong> information.</p>
<p>This is <b>bold</b> text for visual emphasis.</p>

```

---

## Q9. 🤔 `<em>` vs `<i>` tags

`<em>` indicates emphasis with semantic meaning that screen readers stress, while `<i>` is purely visual styling with no semantic meaning. Use `<em>` for emphasized text, `<i>` for foreign words, technical terms, or visual-only italic styling.

- **Trade-offs**: `<em>` improves accessibility because screen readers stress it, while `<i>` is ignored by assistive technologies - prefer `<em>` for better accessibility unless you need visual-only italic styling for things like scientific names or foreign words.

Example:

```html
<p>This is <em>emphasized</em> text.</p>
<p>This is <i>italic</i> text for visual styling.</p>
<p><i>Homo sapiens</i> is the scientific name.</p>

```

---

## Q10. 📄 Creating hyperlinks in HTML

Use the `<a>` tag with `href` attribute to create clickable links - use descriptive link text for better accessibility and SEO. Use `rel="noopener"` with `target="_blank"` for security when opening external links in new tabs.

- **Trade-offs**: Descriptive link text improves accessibility and SEO, while generic text like "click here" is poor for both - use `#` followed by element ID for page anchors, and always include `rel="noopener"` for security with `target="_blank"`.

Example:

```html
<a href="https://example.com">External link</a>
<a href="/about.html">Internal link</a>
<a href="#section1">Anchor link</a>
<a href="mailto:email@example.com">Email link</a>

```

---

## Q11. 📄 Different types of lists in HTML

HTML supports three list types: unordered `<ul>` for bulleted lists, ordered `<ol>` for numbered sequential lists, and definition `<dl>` for terms and descriptions. Semantic list types improve accessibility and make styling easier.

- **Trade-offs**: Use `<ul>` for navigation menus and unordered items, `<ol>` for step-by-step instructions, and `<dl>` for glossaries - semantic lists are better for accessibility and styling than manually styled divs.

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

## Q12. 📄 Creating tables in HTML

Use `<table>`, `<tr>` for rows, `<td>` for data cells, and `<th>` for header cells to create structured data tables. Use `<thead>`, `<tbody>`, and `<tfoot>` for better structure, and `<caption>` for table descriptions.

- **Trade-offs**: Tables are for tabular data like schedules, statistics, or comparisons, not for layout - use semantic table structure with proper headers and captions for better accessibility and styling.

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

## Q13. 💡 Purpose of the `<meta>` tag

`<meta>` tags provide metadata about the HTML document for browsers and search engines - they're crucial for SEO, mobile optimization, and social sharing. Common uses include character encoding, viewport settings, SEO descriptions, and Open Graph tags.

- **Trade-offs**: Viewport meta is essential for responsive design on mobile devices, and description meta is used by search engines for snippets - missing meta tags can hurt SEO and mobile user experience.

Example:

```html
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<meta name="description" content="Page description">
<meta name="keywords" content="keyword1, keyword2">

```

---

