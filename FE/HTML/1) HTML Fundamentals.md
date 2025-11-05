# 🧠 1. HTML Fundamentals (Q1–15)

---

## 1) What is HTML and what does it stand for?

HTML stands for HyperText Markup Language. It's the standard markup language for creating web pages.

```html
<!DOCTYPE html>
<html>
  <head><title>My Web Page</title></head>
  <body><h1>Welcome</h1></body>
</html>
```

- **Core Purpose**: Describes the structure and content of web pages using tags
- **Real-World Use**: Foundation of all web development, works with CSS and JavaScript
- **HTML5**: Current standard with semantic elements and modern features
- **Hypertext**: Links between pages, making the web interconnected
- **Interview Tip**: Explain that HTML is the structure, CSS is the styling, JavaScript is the behavior

---

## 2) What is the difference between HTML and XHTML?

XHTML is HTML written as XML with stricter syntax rules. HTML5 is more forgiving and widely used.

```html
<!-- HTML5 (more forgiving) -->
<img src="image.jpg" alt="description">
<br>

<!-- XHTML (strict) -->
<img src="image.jpg" alt="description" />
```

- **Key Difference**: XHTML requires all tags closed, case-sensitive, and strict syntax
- **Real-World Use**: HTML5 is the modern standard, XHTML is mostly legacy
- **Syntax Rules**: XHTML requires quotes, proper nesting, and closing tags
- **HTML5 Advantage**: More forgiving syntax, better for rapid development
- **Interview Tip**: Explain that HTML5 is the current standard, XHTML is outdated

---

## 3) What are HTML elements, tags, and attributes?

Elements are complete structures. Tags are the markup syntax. Attributes provide additional information.

```html
<a href="https://example.com" target="_blank" class="link">
  Click here
</a>
<!-- <a> = opening tag, </a> = closing tag -->
<!-- href, target, class = attributes -->
<!-- Complete structure = element -->
```

- **Elements**: Opening tag, content, and closing tag together
- **Tags**: The markup syntax like `<a>` and `</a>`
- **Attributes**: Additional information like `href`, `target`, `class`
- **Self-Closing Tags**: Some tags like `<img>` don't need closing tags
- **Interview Tip**: Explain that elements are the complete structure, tags are just the syntax

---

## 4) What is the difference between block and inline elements?

Block elements take full width and create new lines. Inline elements flow with text and don't break lines.

```html
<!-- Block: full width, new line -->
<div>Block element</div>
<p>Paragraph</p>

<!-- Inline: flows with text -->
<span>Inline text</span> and <a href="#">link</a>
```

- **Block Elements**: Take full width, create new lines, can contain other elements
- **Inline Elements**: Flow with text, don't break lines, can't contain block elements
- **Real-World Use**: Block for layout, inline for text styling and links
- **CSS Display**: Can change element behavior with CSS `display` property
- **Interview Tip**: Explain that block elements are for structure, inline for text flow

---

## 5) What are the basic structure elements of an HTML document?

Every HTML document needs DOCTYPE, html root element, head for metadata, and body for content.

```html
<!DOCTYPE html>
<html>
  <head>
    <meta charset="UTF-8">
    <title>Document Title</title>
  </head>
  <body><h1>Hello World</h1></body>
</html>
```

- **DOCTYPE**: Tells browser which HTML version to use, must be first line
- **html**: Root element containing all page content
- **head**: Contains metadata not displayed on page (title, meta, links)
- **body**: Contains visible page content that users see
- **Interview Tip**: Explain that DOCTYPE prevents quirks mode, ensures consistent rendering

---

## 6) What is the DOCTYPE declaration and why is it important?

DOCTYPE tells the browser which HTML version to use. It triggers standards mode rendering.

```html
<!-- HTML5 DOCTYPE (simple) -->
<!DOCTYPE html>

<!-- Older HTML versions (complex) -->
<!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 4.01 Transitional//EN">
```

- **Core Purpose**: Prevents browser from using quirks mode rendering
- **Real-World Impact**: Ensures consistent rendering across different browsers
- **HTML5 Advantage**: Simple `<!DOCTYPE html>` is all you need
- **Must Be First**: Must be the very first line in HTML document
- **Interview Tip**: Explain that missing DOCTYPE can cause layout issues and inconsistent rendering

---

## 7) What are HTML comments and how do you write them?

HTML comments are non-displayed text used for documentation and debugging.

```html
<!-- Single-line comment -->
<!-- Multi-line comment
     spans multiple lines -->
<!-- <div>Hidden code</div> -->
```

- **Core Purpose**: Document code or temporarily disable HTML without deleting
- **Real-World Use**: Documentation, debugging, or hiding code temporarily
- **Syntax**: Start with `<!--` and end with `-->`
- **Limitation**: Can't nest comments inside other comments
- **Interview Tip**: Explain that comments are visible in page source, not secure for hiding secrets

---

## 8) What is the difference between `<div>` and `<span>`?

`<div>` is a block-level container. `<span>` is an inline container for styling or grouping text.

```html
<div class="container">
  <p>This is a paragraph with <span class="highlight">highlighted text</span> inside.</p>
  <div class="section">This is a section</div>
</div>
```

- **Core Difference**: `<div>` is block-level, `<span>` is inline
- **Real-World Use**: `<div>` for layout, `<span>` for text styling
- **Semantic Note**: Both are generic containers with no semantic meaning
- **Best Practice**: Use semantic elements when possible instead of generic containers
- **Interview Tip**: Explain that semantic HTML is preferred over generic div/span

---

## 9) What are HTML entities and when should you use them?

HTML entities are special codes for characters that have special meaning in HTML or aren't on keyboard.

```html
<p>&lt;div&gt; is a tag</p>
<p>Copyright &copy; 2024</p>
<p>Price: &euro;25.99</p>
```

- **Core Purpose**: Display special characters that HTML interprets as code
- **Common Entities**: `&lt;` for <, `&gt;` for >, `&amp;` for &, `&nbsp;` for space
- **Real-World Use**: Display code examples, copyright symbols, currency symbols
- **Syntax**: Start with `&` and end with `;`
- **Interview Tip**: Explain that entities prevent HTML from interpreting special characters as code

---

## 10) What is the difference between `<strong>` and `<b>` tags?

`<strong>` indicates importance and meaning. `<b>` is purely visual styling.

```html
<p>This is <strong>important</strong> information.</p>
<p>This is <b>bold</b> text for visual emphasis.</p>
```

- **Semantic Difference**: `<strong>` has semantic meaning, `<b>` is purely visual
- **Real-World Impact**: Screen readers emphasize `<strong>` content, ignore `<b>`
- **Best Practice**: Use `<strong>` for important text, `<b>` only when you need bold without meaning
- **Accessibility**: `<strong>` improves accessibility, `<b>` doesn't
- **Interview Tip**: Explain that semantic HTML improves accessibility and SEO

---

## 11) What is the difference between `<em>` and `<i>` tags?

`<em>` indicates emphasis and meaning. `<i>` is purely visual styling.

```html
<p>This is <em>emphasized</em> text.</p>
<p>This is <i>italic</i> text for visual styling.</p>
<p><i>Homo sapiens</i> is the scientific name.</p>
```

- **Semantic Difference**: `<em>` has semantic meaning, `<i>` is purely visual
- **Real-World Impact**: Screen readers stress `<em>` content, ignore `<i>`
- **Best Practice**: Use `<em>` for emphasized text, `<i>` for foreign words or technical terms
- **Accessibility**: `<em>` improves accessibility, `<i>` doesn't
- **Interview Tip**: Explain that semantic tags help screen readers understand content better

---

## 12) How do you create hyperlinks in HTML?

Use the `<a>` tag with `href` attribute to create clickable links.

```html
<a href="https://example.com">External link</a>
<a href="/about.html">Internal link</a>
<a href="#section1">Anchor link</a>
<a href="mailto:email@example.com">Email link</a>
```

- **Core Syntax**: `<a href="url">link text</a>` creates clickable links
- **Real-World Use**: Navigation, external links, email links, phone links
- **Security**: Use `rel="noopener"` with `target="_blank"` for security
- **Anchor Links**: Use `#` followed by element ID for page anchors
- **Interview Tip**: Explain that descriptive link text improves accessibility and SEO

---

## 13) What are the different types of lists in HTML?

HTML supports three list types: unordered (`<ul>`), ordered (`<ol>`), and definition (`<dl>`).

```html
<ul><li>Item 1</li><li>Item 2</li></ul>
<ol><li>First step</li><li>Second step</li></ol>
<dl>
  <dt>HTML</dt><dd>HyperText Markup Language</dd>
</dl>
```

- **Unordered Lists**: `<ul>` creates bulleted lists for items without order
- **Ordered Lists**: `<ol>` creates numbered lists for sequential items
- **Definition Lists**: `<dl>` creates definition lists with terms and descriptions
- **Real-World Use**: Navigation menus, step-by-step instructions, glossaries
- **Interview Tip**: Explain that semantic list types improve accessibility and styling

---

## 14) How do you create tables in HTML?

Use `<table>`, `<tr>`, `<td>`, and `<th>` elements to create structured data tables.

```html
<table>
  <thead>
    <tr><th>Name</th><th>Age</th></tr>
  </thead>
  <tbody><tr><td>John</td><td>30</td></tr></tbody>
</table>
```

- **Core Structure**: `<table>` contains `<tr>` (rows) which contain `<td>` (data) or `<th>` (headers)
- **Real-World Use**: Display structured data like schedules, statistics, or comparisons
- **Semantic Sections**: Use `<thead>`, `<tbody>`, `<tfoot>` for better structure
- **Accessibility**: Use `<th>` for headers, `<caption>` for table descriptions
- **Interview Tip**: Explain that tables are for tabular data, not layout

---

## 15) What is the purpose of the `<meta>` tag?

`<meta>` tags provide metadata about the HTML document for browsers and search engines.

```html
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<meta name="description" content="Page description">
<meta name="keywords" content="keyword1, keyword2">
```

- **Core Purpose**: Provide metadata not displayed on page but used by browsers and search engines
- **Real-World Use**: Character encoding, mobile viewport, SEO descriptions, social sharing
- **Viewport Meta**: Essential for responsive design on mobile devices
- **SEO Impact**: Description meta tag is used by search engines for snippets
- **Interview Tip**: Explain that meta tags are crucial for SEO and mobile optimization

---
