# 🔧 8. Advanced HTML Concepts (Q102–111)

---

## 🧩 Q102. What is the difference between HTML and XML?

### 🧠 Concept

HTML is a markup language for web pages with predefined tags. XML is a markup language for data with custom tags. HTML is display-focused, XML is data-focused.

---

### 💡 Example

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

### 🔍 Deep Insights

* **Rule:** HTML has predefined semantic tags, XML allows custom tag definitions.
* **Use Case:** HTML is for presentation (web pages), XML is for data (configuration, APIs).
* **Common Mistake:** HTML is more forgiving with syntax, XML requires strict syntax rules.
* **Pro Tip:** HTML is for web pages, XML is for structured data exchange.

---

### ⭐ Senior Takeaway

HTML is display-focused, XML is data-focused.

---

## 🧩 Q103. How do you create custom attributes?

### 🧠 Concept

Use `data-*` attributes for custom data storage. This is the standard way to add custom attributes. Data attributes are the preferred way to add custom metadata.

---

### 💡 Example

```html
<div data-user-id="12345" data-role="admin" data-theme="dark">
  User content
</div>
```

---

### 🔍 Deep Insights

* **Rule:** `data-*` attributes are the standard way, validated by HTML validators.
* **Use Case:** Data attributes are accessible via `dataset` property in JavaScript.
* **Common Mistake:** Custom attributes require `getAttribute()`, not standard.
* **Pro Tip:** Use data attributes for component communication, feature flags.

---

### ⭐ Senior Takeaway

Data attributes are the preferred way to add custom metadata.

---

## 🧩 Q104. What is the purpose of the `<template>` element?

### 🧠 Concept

`<template>` defines reusable HTML content that isn't rendered until cloned and inserted into the document. Template element is essential for modern web components.

---

### 💡 Example

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

### 🔍 Deep Insights

* **Rule:** Template content isn't rendered initially, use `content.cloneNode(true)` to clone.
* **Use Case:** Great for dynamic content generation, works well with Web Components.
* **Common Mistake:** More efficient than innerHTML, better for performance.
* **Pro Tip:** Use for reusable content patterns, dynamic list generation.

---

### ⭐ Senior Takeaway

Template element is essential for modern web components.

---

## 🧩 Q105. How do you create accessible SPAs?

### 🧠 Concept

Use proper HTML structure, ARIA attributes, and focus management for accessible SPAs. Accessible SPAs require focus management and ARIA attributes.

---

### 💡 Example

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

### 🔍 Deep Insights

* **Rule:** Use proper landmark roles, implement focus management, provide skip links.
* **Use Case:** Use ARIA live regions for dynamic content, test with keyboard and screen readers.
* **Common Mistake:** Not managing focus when navigating, ignoring landmark roles.
* **Pro Tip:** Test with keyboard and screen readers, follow WCAG guidelines.

---

### ⭐ Senior Takeaway

Accessible SPAs require focus management and ARIA attributes.

---

## 🧩 Q106. How do you include CSS in HTML?

### 🧠 Concept

CSS can be included via external files, internal styles, inline styles, or imported stylesheets. External stylesheets are preferred for maintainability.

---

### 💡 Example

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

### 🔍 Deep Insights

* **Rule:** External (best for maintainability), internal (page-specific), inline (highest specificity).
* **Use Case:** External stylesheets are best for caching and maintainability.
* **Common Mistake:** Inline styles have highest specificity, can cause maintenance issues.
* **Pro Tip:** Order matters for CSS cascade, import can cause render-blocking.

---

### ⭐ Senior Takeaway

External stylesheets are preferred for maintainability.

---

## 🧩 Q107. How do you create responsive layouts?

### 🧠 Concept

Use flexible HTML structure with CSS Grid, Flexbox, and responsive techniques for different screen sizes. Responsive design requires semantic HTML and CSS techniques.

---

### 💡 Example

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

### 🔍 Deep Insights

* **Rule:** Use semantic HTML structure, implement CSS Grid and Flexbox.
* **Use Case:** Use media queries for breakpoints, consider mobile-first approach.
* **Common Mistake:** Not setting viewport meta tag, using fixed widths.
* **Pro Tip:** Test on different screen sizes, use responsive images.

---

### ⭐ Senior Takeaway

Responsive design requires semantic HTML and CSS techniques.

---

## 🧩 Q108. What is the purpose of `<details>` and `<summary>`?

### 🧠 Concept

`<details>` creates collapsible content sections. `<summary>` provides the clickable header for the details. details/summary is native HTML, no JavaScript needed.

---

### 💡 Example

```html
<details>
  <summary>Click to expand</summary>
  <p>This content is hidden by default and can be toggled.</p>
</details>
<details open>
  <summary>Already expanded</summary>
  <p>This content is visible by default.</p>
</details>
```

---

### 🔍 Deep Insights

* **Rule:** Native collapsible functionality without JavaScript.
* **Use Case:** Good for FAQs, documentation, or any expandable content.
* **Common Mistake:** Can be nested for complex structures, accessible by default.
* **Pro Tip:** Use `open` attribute for default expanded state.

---

### ⭐ Senior Takeaway

details/summary is native HTML, no JavaScript needed.

---

## 🧩 Q109. How do you create data visualizations?

### 🧠 Concept

Use proper HTML structure, ARIA attributes, and alternative text to make charts and graphs accessible. Accessible visualizations require data tables and ARIA.

---

### 💡 Example

```html
<div role="img" aria-labelledby="chart-title" aria-describedby="chart-description">
  <h3 id="chart-title">Sales by Quarter</h3>
  <p id="chart-description">
    Bar chart showing sales data: Q1 $50K, Q2 $75K, Q3 $60K, Q4 $90K
  </p>
  <div class="chart">
    <div class="bar" style="height: 50%;" aria-label="Q1: $50,000"></div>
  </div>
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

### 🔍 Deep Insights

* **Rule:** Provide data tables for screen readers, use ARIA labels and descriptions.
* **Use Case:** Include alternative text descriptions, consider color-blind users.
* **Common Mistake:** Not providing data tables, relying only on visual charts.
* **Pro Tip:** Test with assistive technologies, provide multiple ways to access data.

---

### ⭐ Senior Takeaway

Accessible visualizations require data tables and ARIA.

---

## 🧩 Q110. How do you implement internationalization?

### 🧠 Concept

Use proper language attributes, character encoding, and direction attributes for international content. Internationalization requires proper language and direction attributes.

---

### 💡 Example

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

### 🔍 Deep Insights

* **Rule:** Use `lang` attribute for language, `dir` attribute for text direction (RTL).
* **Use Case:** Use `datetime` for machine-readable dates, consider cultural differences.
* **Common Mistake:** Not setting language attributes, ignoring RTL languages.
* **Pro Tip:** Test with different languages, use proper character encoding (UTF-8).

---

### ⭐ Senior Takeaway

Internationalization requires proper language and direction attributes.

---

## 🧩 Q111. How do you create interactive components?

### 🧠 Concept

Use proper HTML semantics, ARIA attributes, and keyboard navigation for accessible interactive elements. Accessible components require ARIA, keyboard support, and proper semantics.

---

### 💡 Example

```html
<div role="dialog" aria-labelledby="modal-title" aria-modal="true" aria-hidden="true" id="modal" tabindex="-1">
  <h2 id="modal-title">Modal Title</h2>
  <p>Modal content goes here...</p>
  <button aria-label="Close dialog" onclick="closeModal()">Close</button>
</div>
<button onclick="openModal()" aria-haspopup="dialog">Open Modal</button>
```

---

### 🔍 Deep Insights

* **Rule:** Use appropriate ARIA roles, implement keyboard navigation, provide clear labels.
* **Use Case:** Test with screen readers, follow ARIA authoring practices.
* **Common Mistake:** Not implementing keyboard navigation, missing ARIA attributes.
* **Pro Tip:** Ensure focus management, provide clear feedback for interactions.

---

### ⭐ Senior Takeaway

Accessible components require ARIA, keyboard support, and proper semantics.

---
