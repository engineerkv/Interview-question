# ♿ 4. Accessibility (A11y) (Q46–60)

---

## 46) What is web accessibility and why is it important?

Concept:
Web accessibility ensures websites are usable by people with disabilities, following WCAG guidelines for inclusive design.

Example:
```html
<!-- Accessible image -->
<img src="chart.jpg" alt="Sales increased 25% in Q3 2024" 
     width="400" height="300">

<!-- Accessible button -->
<button aria-label="Close dialog" onclick="closeModal()">
```

Deep Insight:
- Benefits 15% of global population with disabilities
- Improves SEO and user experience for all users
- Legal requirement in many jurisdictions
- Follows WCAG 2.1 AA guidelines
- Includes visual, motor, cognitive, and hearing impairments

---

## 47) What are ARIA attributes and when should you use them?

Concept:
ARIA (Accessible Rich Internet Applications) attributes provide additional information to screen readers when semantic HTML isn't sufficient.

Example:
```html
<!-- Button with expanded state -->
<button aria-expanded="false" aria-controls="menu" 
        onclick="toggleMenu()">
  Menu
</button>
<div id="menu" aria-hidden="true">Menu content</div>
```

Deep Insight:
- Use when semantic HTML isn't sufficient
- Don't override native semantics
- Test with screen readers
- ARIA doesn't change visual appearance
- Follow ARIA authoring practices

---

## 48) How do you create accessible images with alt text?

Concept:
Provide meaningful `alt` text that describes the image's content and purpose, using empty alt for decorative images.

Example:
```html
<!-- Informative image -->
<img src="sales-chart.jpg" 
     alt="Bar chart showing 25% increase in sales from Q2 to Q3 2024">

<!-- Decorative image -->
<img src="decoration.jpg" alt="" role="presentation">
```

Deep Insight:
- Alt text should be descriptive and concise
- Empty alt for decorative images
- Don't start with "Image of" or "Picture of"
- Consider context and surrounding content
- Use `longdesc` for complex images

---

## 49) What is the difference between `aria-label` and `aria-labelledby`?

Concept:
`aria-label` provides a direct label; `aria-labelledby` references other elements that serve as the label.

Example:
```html
<!-- aria-label: direct label -->
<button aria-label="Close dialog">×</button>
<input type="search" aria-label="Search products">

<!-- aria-labelledby: references other elements -->
<div id="search-label">Search</div>
```

Deep Insight:
- `aria-label` overrides element's text content
- `aria-labelledby` can reference multiple elements
- `aria-labelledby` takes precedence over `aria-label`
- Use when visible labels aren't sufficient
- Screen readers announce the label

---

## 50) How do you create accessible form controls?

Concept:
Use proper labels, grouping, and ARIA attributes to make forms accessible to screen readers and keyboard users.

Example:
```html
<fieldset>
  <legend>Contact Information</legend>
  
  <label for="name">Full Name:</label>
  <input type="text" id="name" name="name" required
         aria-describedby="name-help">
```

Deep Insight:
- Always provide labels for form controls
- Use fieldset/legend for related groups
- Associate help text with aria-describedby
- Use role="alert" for error messages
- Test with keyboard navigation

---

## 51) What are landmark roles and how do you use them?

Concept:
Landmark roles identify major sections of a page, helping screen reader users navigate efficiently.

Example:
```html
<body>
  <header role="banner">
    <h1>Site Title</h1>
    <nav role="navigation" aria-label="Main navigation">
      <ul>
        <li><a href="/">Home</a></li>
```

Deep Insight:
- Semantic HTML5 elements have implicit landmark roles
- Use ARIA roles when semantic elements aren't available
- Only one banner, main, and contentinfo per page
- Navigation can appear multiple times
- Screen readers use landmarks for navigation

---

## 52) How do you create accessible tables?

Concept:
Use proper table structure with headers, captions, and ARIA attributes to make data tables accessible.

Example:
```html
<table>
  <caption>Monthly Sales Report for 2024</caption>
  <thead>
    <tr>
      <th scope="col">Month</th>
      <th scope="col">Sales</th>
```

Deep Insight:
- Use `<caption>` to describe table purpose
- `<th>` elements define column and row headers
- `scope="col"` for column headers, `scope="row"` for row headers
- Use `<thead>`, `<tbody>`, `<tfoot>` for structure
- Screen readers announce headers with data

---

## 53) What is the purpose of `aria-hidden` attribute?

Concept:
`aria-hidden="true"` hides decorative elements from screen readers while keeping them visible to sighted users.

Example:
```html
<!-- Decorative icons -->
<button aria-label="Close dialog">
  <span aria-hidden="true">×</span>
</button>

<button aria-label="Search">
```

Deep Insight:
- Hides purely decorative elements
- Don't hide interactive elements
- Use for icons, separators, decorative text
- Screen readers skip aria-hidden content
- Improves screen reader experience

---

## 54) How do you create accessible navigation menus?

Concept:
Use semantic HTML with proper ARIA attributes and keyboard navigation support for accessible menus.

Example:
```html
<nav aria-label="Main navigation">
  <ul>
    <li>
      <a href="/" aria-current="page">Home</a>
    </li>
    <li>
```

Deep Insight:
- Use `<nav>` element for navigation
- Provide descriptive aria-label
- Use `aria-current="page"` for current page
- Support keyboard navigation (Tab, Enter, Escape)
- Use `aria-expanded` for collapsible menus

---

## 55) What are the different ARIA live regions?

Concept:
ARIA live regions announce dynamic content changes to screen readers without interrupting current reading.

Example:
```html
<!-- Polite announcements -->
<div aria-live="polite" id="status">
  <!-- Status updates appear here -->
</div>

<!-- Assertive announcements -->
```

Deep Insight:
- `polite`: Announces when user finishes current task
- `assertive`: Interrupts to announce immediately
- `off`: No announcements (default)
- Use for status updates, errors, notifications
- Don't overuse assertive regions

---

## 56) How do you create accessible modal dialogs?

Concept:
Use proper ARIA attributes, focus management, and keyboard navigation for accessible modal dialogs.

Example:
```html
<!-- Modal trigger -->
<button onclick="openModal()">Open Settings</button>

<!-- Modal dialog -->
<div role="dialog" aria-labelledby="modal-title" 
     aria-modal="true" aria-hidden="true" id="modal">
```

Deep Insight:
- Use `role="dialog"` for modal dialogs
- `aria-modal="true"` indicates modal behavior
- `aria-labelledby` references dialog title
- Trap focus within modal
- Close on Escape key
- Return focus to trigger element

---

## 57) What is the purpose of `tabindex` attribute?

Concept:
`tabindex` controls keyboard navigation order and focusability of elements.

Example:
```html
<!-- Natural tab order (default) -->
<button tabindex="0">Button 1</button>
<input type="text" tabindex="0">
<button tabindex="0">Button 2</button>

<!-- Custom tab order -->
```

Deep Insight:
- `0`: Focusable in natural tab order
- `-1`: Focusable but not in tab order
- Positive numbers: Custom tab order (avoid)
- Use for custom interactive elements
- Essential for keyboard accessibility

---

## 58) How do you create accessible data tables?

Concept:
Use proper table structure with headers, captions, and ARIA attributes for complex data tables.

Example:
```html
<table role="table" aria-label="Employee Directory">
  <caption>Employee Directory - Q1 2024</caption>
  <thead>
    <tr role="row">
      <th scope="col" role="columnheader">Name</th>
      <th scope="col" role="columnheader">Department</th>
```

Deep Insight:
- Use explicit ARIA roles for complex tables
- `scope` attribute defines header relationships
- `role="columnheader"` for column headers
- `role="rowheader"` for row headers
- `role="cell"` for data cells

---

## 59) What are the WCAG guidelines and how do they apply to HTML?

Concept:
WCAG (Web Content Accessibility Guidelines) provide standards for accessible web content with four principles: Perceivable, Operable, Understandable, Robust.

Example:
```html
<!-- Perceivable: Provide text alternatives -->
<img src="chart.jpg" alt="Sales increased 25% in Q3">

<!-- Operable: Make all functionality keyboard accessible -->
<button onclick="submitForm()" tabindex="0">Submit</button>

```

Deep Insight:
- WCAG 2.1 has three levels: A, AA, AAA
- Most organizations target AA level
- Four principles: POUR (Perceivable, Operable, Understandable, Robust)
- Guidelines cover text, images, forms, navigation
- Legal requirement in many countries

---

## 60) How do you test HTML for accessibility issues?

Concept:
Use automated tools, manual testing, and assistive technologies to identify and fix accessibility issues.

Example:
```html
<!-- Test with screen reader -->
<button aria-label="Close dialog">×</button>

<!-- Test keyboard navigation -->
<a href="#main" class="skip-link">Skip to main content</a>

```

Deep Insight:
- Use automated tools: axe, WAVE, Lighthouse
- Test with screen readers: NVDA, JAWS, VoiceOver
- Test keyboard-only navigation
- Check color contrast ratios
- Validate HTML markup
- Test with real users when possible
