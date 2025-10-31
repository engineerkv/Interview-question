# 🔧 8. Advanced HTML Concepts (Q102–111)

---

## 102) What is the difference between HTML and XML?

Concept:
HTML is a markup language for web pages with predefined tags; XML is a markup language for data with custom tags.

Example:
```html
<!-- HTML - predefined tags -->
<html>
<head>
  <title>Web Page</title>
</head>
<body>
```

Deep Insight:
- HTML has predefined semantic tags
- XML allows custom tag definitions
- HTML is more forgiving with syntax
- XML requires strict syntax rules
- HTML is for presentation, XML for data

---

## 103) How do you create custom HTML attributes?

Concept:
Use `data-*` attributes for custom data storage or create non-standard attributes (though data-* is preferred).

Example:
```html
<!-- Data attributes (recommended) -->
<div data-user-id="12345" 
     data-role="admin" 
     data-theme="dark">
  User content
</div>
```

Deep Insight:
- `data-*` attributes are the standard way
- Data attributes are accessible via `dataset`
- Custom attributes require `getAttribute()`
- Data attributes are validated by HTML validators
- Use data attributes for component communication

---

## 104) What is the purpose of the `<template>` element?

Concept:
`<template>` defines reusable HTML content that isn't rendered until cloned and inserted into the document.

Example:
```html
<!-- Template definition -->
<template id="user-card-template">
  <div class="user-card">
    <img src="" alt="User avatar" class="avatar">
    <h3 class="name"></h3>
    <p class="email"></p>
```

Deep Insight:
- Template content isn't rendered initially
- Use `content.cloneNode(true)` to clone
- Great for dynamic content generation
- More efficient than innerHTML
- Works well with Web Components

---

## 105) How do you create accessible single-page applications?

Concept:
Use proper HTML structure, ARIA attributes, and focus management for accessible SPAs.

Example:
```html
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <title>Accessible SPA</title>
</head>
```

Deep Insight:
- Use proper landmark roles
- Implement focus management
- Provide skip links for navigation
- Use ARIA live regions for dynamic content
- Test with keyboard and screen readers

---

## 106) What are the different ways to include CSS in HTML?

Concept:
CSS can be included via external files, internal styles, inline styles, or imported stylesheets.

Example:
```html
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  
  <!-- External stylesheet -->
```

Deep Insight:
- External: Best for maintainability and caching
- Internal: Good for page-specific styles
- Inline: Use sparingly, highest specificity
- Import: Can cause render-blocking
- Order matters for CSS cascade

---

## 107) How do you create responsive HTML layouts?

Concept:
Use flexible HTML structure with CSS Grid, Flexbox, and responsive techniques for different screen sizes.

Example:
```html
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Responsive Layout</title>
```

Deep Insight:
- Use semantic HTML structure
- Implement CSS Grid and Flexbox
- Use media queries for breakpoints
- Consider mobile-first approach
- Test on different screen sizes

---

## 108) What is the purpose of the `<details>` and `<summary>` elements?

Concept:
`<details>` creates collapsible content sections; `<summary>` provides the clickable header for the details.

Example:
```html
<!-- Basic collapsible section -->
<details>
  <summary>Click to expand</summary>
  <p>This content is hidden by default and can be toggled.</p>
</details>

```

Deep Insight:
- Native collapsible functionality
- No JavaScript required
- Good for FAQs and documentation
- Can be nested for complex structures
- Accessible by default

---

## 109) How do you create accessible data visualizations?

Concept:
Use proper HTML structure, ARIA attributes, and alternative text to make charts and graphs accessible.

Example:
```html
<!-- Accessible bar chart -->
<div role="img" 
     aria-labelledby="chart-title" 
     aria-describedby="chart-description">
  <h3 id="chart-title">Sales by Quarter</h3>
  <p id="chart-description">
```

Deep Insight:
- Provide data tables for screen readers
- Use ARIA labels and descriptions
- Include alternative text descriptions
- Consider color-blind users
- Test with assistive technologies

---

## 110) What are the different ways to handle internationalization in HTML?

Concept:
Use proper language attributes, character encoding, and direction attributes for international content.

Example:
```html
<!-- English content -->
<html lang="en">
<head>
  <meta charset="UTF-8">
  <title>English Page</title>
</head>
```

Deep Insight:
- Use `lang` attribute for language
- Use `dir` attribute for text direction
- Use `datetime` for machine-readable dates
- Consider cultural differences in formatting
- Test with different languages

---

## 111) How do you create accessible interactive components?

Concept:
Use proper HTML semantics, ARIA attributes, and keyboard navigation for accessible interactive elements.

Example:
```html
<!-- Accessible modal dialog -->
<div role="dialog" 
     aria-labelledby="modal-title" 
     aria-modal="true" 
     aria-hidden="true" 
     id="modal">
```

Deep Insight:
- Use appropriate ARIA roles
- Implement keyboard navigation
- Provide clear labels and descriptions
- Test with screen readers
- Follow ARIA authoring practices
