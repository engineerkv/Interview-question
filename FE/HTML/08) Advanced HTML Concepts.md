# 🔧 8. Advanced HTML Concepts (Q102–110)

---

## 📍 Navigation

<div align="center">

[← Previous: Performance & SEO](07%29%20Performance%20%26%20SEO.md) • [Home: README](../README.md)

[📋 Cheatsheet](HTML%20Interview%20Cheatsheet.md)

</div>

---

---

## Q102. 📄 HTML vs XML

HTML is a markup language for web pages with predefined tags, while XML is a markup language for data with custom tags - HTML is display-focused, XML is data-focused. HTML has predefined semantic tags, XML allows custom tag definitions.

- **Trade-offs**: The catch is HTML is more forgiving with syntax, XML requires strict syntax rules - HTML is for web pages, XML is for structured data exchange. HTML is display-focused, XML is data-focused, but watch out - HTML is for presentation (web pages), XML is for data (configuration, APIs).

Example:

```html
<!-- HTML - predefined tags -->
<html>
  <head>
    <title>Web Page</title>
  </head>
  <body>
    <h1>Welcome</h1>
    <p>HTML content...</p>
  </body>
</html>

<!-- XML - custom tags -->
<?xml version="1.0" encoding="UTF-8"?>
<user>
  <id>12345</id>
  <name>John Doe</name>
  <email>john@example.com</email>
</user>

```

---

## Q103. 💡 Creating custom attributes

Use `data-*` attributes for custom data storage - this is the standard way to add custom attributes, data attributes are the preferred way to add custom metadata. `data-*` attributes are the standard way, validated by HTML validators.

- **Trade-offs**: The catch is custom attributes require `getAttribute()`, not standard - use data attributes for component communication, feature flags. Data attributes are the preferred way to add custom metadata, but watch out - data attributes are accessible via `dataset` property in JavaScript.

Example:

```html
<div data-user-id="12345" data-role="admin" data-theme="dark">
  User content
</div>

```

---

## Q104. 💡 Purpose of the `<template>` element

`<template>` defines reusable HTML content that isn't rendered until cloned and inserted into the document - template element is essential for modern web components. Template content isn't rendered initially, use `content.cloneNode(true)` to clone.

- **Trade-offs**: The catch is more efficient than innerHTML, better for performance - use for reusable content patterns, dynamic list generation. Template element is essential for modern web components, but watch out - great for dynamic content generation, works well with Web Components.

Example:

```html
<template id="user-card-template">
  <div class="user-card">
    <img src="" alt="User avatar" class="avatar">
    <h3 class="name"></h3>
    <p class="email"></p>
  </div>
</template>
<script>
const template = document.getElementById('user-card-template');
const clone = template.content.cloneNode(true);
clone.querySelector('.name').textContent = 'John Doe';
document.body.appendChild(clone);
</script>

```

---

## Q105. 💡 Creating accessible SPAs

Use proper HTML structure, ARIA attributes, and focus management for accessible SPAs - accessible SPAs require focus management and ARIA attributes. Use proper landmark roles, implement focus management, provide skip links.

- **Trade-offs**: The catch is not managing focus when navigating, ignoring landmark roles - test with keyboard and screen readers, follow WCAG guidelines. Accessible SPAs require focus management and ARIA attributes, but watch out - use ARIA live regions for dynamic content, test with keyboard and screen readers.

Example:

```html
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <title>Accessible SPA</title>
</head>
<body>
  <a href="#main" class="skip-link">Skip to main content</a>
  <header role="banner">
    <nav role="navigation" aria-label="Main navigation">
      <ul>
        <li><a href="/">Home</a></li>
      </ul>
    </nav>
  </header>
  <main role="main" id="main">
    <h1>Page Title</h1>
    <div aria-live="polite" id="dynamic-content">Content...</div>
  </main>
  <footer role="contentinfo">
    <p>Copyright 2024</p>
  </footer>
</body>
</html>

```

---

## Q106. 🎨 Including CSS in HTML

CSS can be included via external files, internal styles, inline styles, or imported stylesheets - external stylesheets are preferred for maintainability. External (best for maintainability), internal (page-specific), inline (highest specificity).

- **Trade-offs**: The catch is inline styles have highest specificity, can cause maintenance issues - order matters for CSS cascade, import can cause render-blocking. External stylesheets are preferred for maintainability, but watch out - external stylesheets are best for caching and maintainability.

Example:

```html
<head>
  <link rel="stylesheet" href="styles.css">
  <style>
    body { margin: 0; }
  </style>
</head>
<body>
  <div style="color: blue;">Inline styled content</div>
</body>

```

---

## Q107. 💡 Creating responsive layouts

Use flexible HTML structure with CSS Grid, Flexbox, and responsive techniques for different screen sizes - responsive design requires semantic HTML and CSS techniques. Use semantic HTML structure, implement CSS Grid and Flexbox.

- **Trade-offs**: The catch is not setting viewport meta tag, using fixed widths - test on different screen sizes, use responsive images. Responsive design requires semantic HTML and CSS techniques, but watch out - use media queries for breakpoints, consider mobile-first approach.

Example:

```html
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Responsive Layout</title>
</head>
<body>
  <header>
    <h1>Site Title</h1>
  </header>
  <main>
    <section>
      <h2>Content</h2>
      <p>Responsive content...</p>
    </section>
  </main>
  <aside>
    <h2>Sidebar</h2>
  </aside>
  <footer>
    <p>Footer</p>
  </footer>
</body>
</html>

```

---

## Q108. 💡 Creating data visualizations

Use proper HTML structure, ARIA attributes, and alternative text to make charts and graphs accessible - accessible visualizations require data tables and ARIA. Provide data tables for screen readers, use ARIA labels and descriptions.

- **Trade-offs**: The catch is not providing data tables, relying only on visual charts - test with assistive technologies, provide multiple ways to access data. Accessible visualizations require data tables and ARIA, but watch out - include alternative text descriptions, consider color-blind users.

Example:

```html
<div role="img" aria-labelledby="chart-title" aria-describedby="chart-description">
  <h3 id="chart-title">Sales by Quarter</h3>
  <p id="chart-description">
    Bar chart showing sales data: Q1 $50K, Q2 $75K, Q3 $60K, Q4 $90K
  </p>
  <div class="chart">
    <div class="bar" style="height: 50%;" aria-label="Q1: $50,000"></div>
  <table>
    <thead>
      <tr>
        <th>Quarter</th>
        <th>Sales</th>
      </tr>
    </thead>
    <tbody>
      <tr>
        <td>Q1</td>
        <td>$50,000</td>
      </tr>
    </tbody>
  </table>
</div>

```

---

## Q109. 🔧 Implementing internationalization

Use proper language attributes, character encoding, and direction attributes for international content - internationalization requires proper language and direction attributes. Use `lang` attribute for language, `dir` attribute for text direction (RTL).

- **Trade-offs**: The catch is not setting language attributes, ignoring RTL languages - test with different languages, use proper character encoding (UTF-8). Internationalization requires proper language and direction attributes, but watch out - use `datetime` for machine-readable dates, consider cultural differences.

Example:

```html
<html lang="en">
  <head>
    <meta charset="UTF-8">
    <title>English Page</title>
  </head>
  <body>
    <h1>Hello World</h1>
  </body>
</html>

<html lang="ar" dir="rtl">
  <head>
    <meta charset="UTF-8">
    <title>الصفحة العربية</title>
  </head>
  <body>
    <h1>مرحبا بالعالم</h1>
  </body>
</html>

<div lang="en">English text</div>
<div lang="es">Texto en español</div>

```

---

## Q110. 🧩 Creating interactive components

Use proper HTML semantics, ARIA attributes, and keyboard navigation for accessible interactive elements - accessible components require ARIA, keyboard support, and proper semantics. Use appropriate ARIA roles, implement keyboard navigation, provide clear labels.

- **Trade-offs**: The catch is not implementing keyboard navigation, missing ARIA attributes - ensure focus management, provide clear feedback for interactions. Accessible components require ARIA, keyboard support, and proper semantics, but watch out - test with screen readers, follow ARIA authoring practices.

Example:

```html
<div role="dialog" aria-labelledby="modal-title" aria-modal="true" aria-hidden="true" id="modal" tabindex="-1">
  <h2 id="modal-title">Modal Title</h2>
  <p>Modal content goes here...</p>
  <button aria-label="Close dialog" onclick="closeModal()">Close</button>
</div>
<button onclick="openModal()" aria-haspopup="dialog">Open Modal</button>

```

---

---

## 📍 Navigation

<div align="center">

[← Previous: Performance & SEO](07%29%20Performance%20%26%20SEO.md) • [Home: README](../README.md)

[📋 Cheatsheet](HTML%20Interview%20Cheatsheet.md)

</div>

---
