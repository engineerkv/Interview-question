# 🧠 1. HTML Fundamentals (Q1–15)

---

## 1) What is HTML and what does it stand for?

Concept:
HTML (HyperText Markup Language) is the standard markup language for creating web pages and web applications.

Example:
```html
<!DOCTYPE html>
<html lang="en">
<head>
  <title>My Web Page</title>
</head>
<body>
  <h1>Welcome</h1>
</body>
</html>
```

Deep Insight:
- HTML describes the structure and content of web pages
- Uses tags to define elements and their relationships
- Works with CSS for styling and JavaScript for behavior
- HTML5 is the current standard with semantic elements
- Foundation of all web development

---

## 2) What is the difference between HTML and XHTML?

Concept:
XHTML is HTML written as XML, with stricter syntax rules and case sensitivity.

Example:
```html
<!-- HTML5 (more forgiving) -->
<img src="image.jpg" alt="description">
<br>

<!-- XHTML (strict) -->
<img src="image.jpg" alt="description" />
```

Deep Insight:
- XHTML requires all tags to be closed and properly nested
- XHTML is case-sensitive (lowercase only)
- XHTML requires quotes around all attribute values
- HTML5 is more forgiving and widely adopted
- XHTML is still valid HTML5

---

## 3) What are HTML elements, tags, and attributes?

Concept:
Elements are complete structures, tags are the markup syntax, and attributes provide additional information.

Example:
```html
<a href="https://example.com" target="_blank" class="link">
  Click here
</a>
<!-- <a> = opening tag, </a> = closing tag -->
<!-- href, target, class = attributes -->
<!-- Complete structure = element -->
```

Deep Insight:
- Elements consist of opening tag, content, and closing tag
- Self-closing tags don't need closing tags (e.g., `<img>`)
- Attributes provide metadata and behavior
- Some attributes are global (id, class, style)
- Attribute values should be quoted for consistency

---

## 4) What is the difference between block and inline elements?

Concept:
Block elements take full width and create new lines; inline elements flow with text and don't break lines.

Example:
```html
<!-- Block elements -->
<div>This is a block element</div>
<p>This is a paragraph</p>
<h1>This is a heading</h1>

<!-- Inline elements -->
```

Deep Insight:
- Block elements can contain other block and inline elements
- Inline elements cannot contain block elements
- Block elements respect width, height, and margin properties
- Inline elements ignore top/bottom margins
- CSS `display` property can change element behavior

---

## 5) What are the basic structure elements of an HTML document?

Concept:
Every HTML document needs a DOCTYPE, html root element, head for metadata, and body for content.

Example:
```html
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Document Title</title>
```

Deep Insight:
- DOCTYPE tells browser which HTML version to use
- `<html>` is the root element containing all content
- `<head>` contains metadata not displayed on page
- `<body>` contains visible page content
- `lang` attribute improves accessibility and SEO

---

## 6) What is the DOCTYPE declaration and why is it important?

Concept:
DOCTYPE tells the browser which HTML version to use and triggers standards mode rendering.

Example:
```html
<!-- HTML5 DOCTYPE (simple) -->
<!DOCTYPE html>

<!-- Older HTML versions (complex) -->
<!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 4.01 Transitional//EN">
```

Deep Insight:
- Prevents browser from using quirks mode
- Ensures consistent rendering across browsers
- HTML5 DOCTYPE is simple and widely supported
- Must be the first line in HTML document
- Missing DOCTYPE can cause layout issues

---

## 7) What are HTML comments and how do you write them?

Concept:
HTML comments are non-displayed text used for documentation and debugging.

Example:
```html
<!-- This is a single-line comment -->

<!--
  This is a multi-line comment
  that can span several lines
  and is useful for documentation
```

Deep Insight:
- Comments are not rendered in the browser
- Useful for documentation and debugging
- Can be placed anywhere in HTML
- Don't nest comments inside other comments
- Comments are visible in page source

---

## 8) What is the difference between `<div>` and `<span>`?

Concept:
`<div>` is a block-level container; `<span>` is an inline container for styling or grouping text.

Example:
```html
<div class="container">
  <p>This is a paragraph with <span class="highlight">highlighted text</span> inside.</p>
  <div class="section">This is a section</div>
</div>
```

Deep Insight:
- `<div>` creates block-level containers for layout
- `<span>` creates inline containers for text styling
- Both are generic containers with no semantic meaning
- Use semantic elements when possible instead
- CSS can change their display behavior

---

## 9) What are HTML entities and when should you use them?

Concept:
HTML entities are special codes for characters that have special meaning in HTML or aren't on keyboard.

Example:
```html
<p>&lt;div&gt; is an HTML tag</p>
<p>Copyright &copy; 2024</p>
<p>Price: &euro;25.99</p>
<p>Non-breaking space: Hello&nbsp;World</p>
<p>Em dash: First&mdash;Second</p>
```

Deep Insight:
- Use `&lt;` and `&gt;` for < and > in text
- Use `&amp;` for & symbol
- Use `&nbsp;` for non-breaking spaces
- Use `&copy;` for copyright symbol
- Some characters require entities for proper display

---

## 10) What is the difference between `<strong>` and `<b>` tags?

Concept:
`<strong>` indicates importance and meaning; `<b>` is purely visual styling.

Example:
```html
<p>This is <strong>important</strong> information.</p>
<p>This is <b>bold</b> text for visual emphasis.</p>
```

Deep Insight:
- `<strong>` has semantic meaning (importance)
- `<b>` is purely visual (bold styling)
- Screen readers emphasize `<strong>` content
- Use `<strong>` for important text
- Use `<b>` only when you need bold without meaning

---

## 11) What is the difference between `<em>` and `<i>` tags?

Concept:
`<em>` indicates emphasis and meaning; `<i>` is purely visual styling.

Example:
```html
<p>This is <em>emphasized</em> text.</p>
<p>This is <i>italic</i> text for visual styling.</p>
<p><i>Homo sapiens</i> is the scientific name.</p>
```

Deep Insight:
- `<em>` has semantic meaning (emphasis)
- `<i>` is purely visual (italic styling)
- Screen readers stress `<em>` content
- Use `<em>` for emphasized text
- Use `<i>` for foreign words, technical terms, thoughts

---

## 12) How do you create hyperlinks in HTML?

Concept:
Use the `<a>` tag with `href` attribute to create clickable links.

Example:
```html
<a href="https://example.com">External link</a>
<a href="/about.html">Internal link</a>
<a href="#section1">Anchor link</a>
<a href="mailto:email@example.com">Email link</a>
<a href="tel:+1234567890">Phone link</a>
```

Deep Insight:
- `href` specifies the destination URL
- Use `target="_blank"` for new window/tab
- Use `rel="noopener"` for security with external links
- Anchor links use `#` followed by element ID
- Always provide descriptive link text

---

## 13) What are the different types of lists in HTML?

Concept:
HTML supports three list types: unordered (`<ul>`), ordered (`<ol>`), and definition (`<dl>`).

Example:
```html
<!-- Unordered list -->
<ul>
  <li>Item 1</li>
  <li>Item 2</li>
</ul>

```

Deep Insight:
- `<ul>` creates bulleted lists
- `<ol>` creates numbered lists
- `<dl>` creates definition lists
- Use `<li>` for list items
- Lists can be nested for complex structures

---

## 14) How do you create tables in HTML?

Concept:
Use `<table>`, `<tr>`, `<td>`, and `<th>` elements to create structured data tables.

Example:
```html
<table>
  <thead>
    <tr>
      <th>Name</th>
      <th>Age</th>
    </tr>
```

Deep Insight:
- `<table>` creates the table container
- `<tr>` creates table rows
- `<td>` creates table data cells
- `<th>` creates table header cells
- Use `<thead>`, `<tbody>`, `<tfoot>` for structure

---

## 15) What is the purpose of the `<meta>` tag?

Concept:
`<meta>` tags provide metadata about the HTML document for browsers and search engines.

Example:
```html
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<meta name="description" content="Page description">
<meta name="keywords" content="keyword1, keyword2">
<meta name="author" content="Author Name">
```

Deep Insight:
- `charset` specifies character encoding
- `viewport` controls mobile display
- `description` used by search engines
- `keywords` less important for SEO now
- `author` identifies page creator
