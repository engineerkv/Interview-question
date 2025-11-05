# ♿ 4. Accessibility (A11y) (Q46–60)

---

## 46) What is web accessibility and why is it important?

Web accessibility ensures websites are usable by people with disabilities. It follows WCAG guidelines for inclusive design.

```html
<img src="chart.jpg" alt="Sales increased 25% in Q3 2024" width="400" height="300">
<button aria-label="Close dialog" onclick="closeModal()">Close</button>
```

- **Core Purpose**: Make websites usable by people with disabilities (visual, motor, cognitive, hearing)
- **Real-World Impact**: Benefits 15% of global population, improves SEO and UX for all users
- **Legal Requirement**: Required by law in many jurisdictions (ADA, Section 508, EU Accessibility Act)
- **WCAG Guidelines**: Follow WCAG 2.1 AA guidelines for inclusive design
- **Interview Tip**: Explain that accessibility is not just nice-to-have, it's essential for inclusive web

---

## 47) What are ARIA attributes and when should you use them?

ARIA attributes provide additional information to screen readers when semantic HTML isn't sufficient.

```html
<button aria-expanded="false" aria-controls="menu" onclick="toggleMenu()">Menu</button>
<div id="menu" aria-hidden="true">Menu content</div>
```

- **Core Purpose**: Enhance accessibility when semantic HTML isn't enough
- **Real-World Use**: Dynamic content, custom widgets, or complex interactions
- **Best Practice**: Use semantic HTML first, add ARIA only when needed
- **Important Rule**: Don't override native semantics, ARIA doesn't change visual appearance
- **Interview Tip**: Explain that ARIA supplements HTML, doesn't replace semantic HTML

---

## 48) How do you create accessible images with alt text?

Provide meaningful `alt` text that describes the image's content and purpose. Use empty alt for decorative images.

```html
<img src="sales-chart.jpg" alt="Bar chart showing 25% increase in sales from Q2 to Q3 2024">
<img src="decoration.jpg" alt="" role="presentation">
```

- **Core Rule**: Alt text should be descriptive and concise, describe content and purpose
- **Real-World Use**: Informative images need alt text, decorative images need empty alt
- **Best Practice**: Don't start with "Image of" or "Picture of", consider context
- **Complex Images**: Use `longdesc` for complex images needing detailed descriptions
- **Interview Tip**: Explain that alt text enables screen readers to understand images

---

## 49) What is the difference between `aria-label` and `aria-labelledby`?

`aria-label` provides a direct label. `aria-labelledby` references other elements that serve as the label.

```html
<button aria-label="Close dialog">×</button>
<input type="search" aria-label="Search products">

<div id="search-label">Search</div>
<input type="text" aria-labelledby="search-label">
```

- **Core Difference**: `aria-label` is direct text, `aria-labelledby` references other elements
- **Real-World Use**: Use `aria-label` when no visible label, `aria-labelledby` when visible label exists
- **Precedence**: `aria-labelledby` takes precedence over `aria-label`
- **Multiple References**: `aria-labelledby` can reference multiple elements (space-separated IDs)
- **Interview Tip**: Explain that `aria-labelledby` is better when visible labels exist

---

## 50) How do you create accessible form controls?

Use proper labels, grouping, and ARIA attributes to make forms accessible to screen readers and keyboard users.

```html
<fieldset>
  <legend>Contact Information</legend>
  <label for="name">Full Name:</label>
  <input type="text" id="name" name="name" required aria-describedby="name-help">
  <div id="name-help">Enter your full legal name</div>
</fieldset>
```

- **Core Requirements**: Always provide labels, use fieldset/legend for groups, associate help text
- **Real-World Use**: Use `aria-describedby` for help text, `role="alert"` for error messages
- **Keyboard Navigation**: Test with keyboard navigation, ensure all controls are focusable
- **Best Practice**: Use proper input types, validation attributes, and clear instructions
- **Interview Tip**: Explain that accessible forms work for screen readers and keyboard users

---

## 51) What are landmark roles and how do you use them?

Landmark roles identify major sections of a page, helping screen reader users navigate efficiently.

```html
<body>
  <header role="banner"><h1>Site Title</h1></header>
  <nav role="navigation" aria-label="Main navigation">
    <ul><li><a href="/">Home</a></li><li><a href="/about">About</a></li></ul>
  </nav>
  <main role="main"><h2>Main Content</h2></main>
  <footer role="contentinfo"><p>Copyright 2024</p></footer>
</body>
```

- **Core Purpose**: Create navigable regions for screen readers using semantic HTML5 elements
- **Real-World Use**: Semantic elements have implicit landmark roles, use ARIA roles if needed
- **Best Practice**: Only one banner, main, and contentinfo per page; navigation can appear multiple times
- **Accessibility**: Screen readers use landmarks for navigation, improves user experience
- **Interview Tip**: Explain that landmarks enable quick navigation for screen reader users

---

## 52) How do you create accessible tables?

Use proper table structure with headers, captions, and ARIA attributes to make data tables accessible.

```html
<table>
  <caption>Monthly Sales Report for 2024</caption>
  <thead>
    <tr><th scope="col">Month</th><th scope="col">Sales</th></tr>
  </thead>
  <tbody>
    <tr><td>January</td><td>$50,000</td></tr>
  </tbody>
</table>
```

- **Core Requirements**: Use `<caption>` for description, `<th>` for headers, `scope` for relationships
- **Real-World Use**: `scope="col"` for column headers, `scope="row"` for row headers
- **Structure**: Use `<thead>`, `<tbody>`, `<tfoot>` for proper table structure
- **Accessibility**: Screen readers announce headers with data cells
- **Interview Tip**: Explain that accessible tables require proper structure and headers

---

## 53) What is the purpose of `aria-hidden` attribute?

`aria-hidden="true"` hides decorative elements from screen readers while keeping them visible to sighted users.

```html
<button aria-label="Close dialog"><span aria-hidden="true">×</span></button>
<button aria-label="Search"><span aria-hidden="true">🔍</span></button>
```

- **Core Purpose**: Hide purely decorative elements from screen readers
- **Real-World Use**: Decorative icons, separators, or visual elements that don't add meaning
- **Important Rule**: Don't hide interactive elements, use for decorative content only
- **Accessibility**: Screen readers skip aria-hidden content, improves experience
- **Interview Tip**: Explain that aria-hidden is for decoration, not for hiding important content

---

## 54) How do you create accessible navigation menus?

Use semantic HTML with proper ARIA attributes and keyboard navigation support for accessible menus.

```html
<nav aria-label="Main navigation">
  <ul>
    <li><a href="/" aria-current="page">Home</a></li>
    <li><a href="/about">About</a></li>
    <li><a href="/contact">Contact</a></li>
  </ul>
</nav>
```

- **Core Requirements**: Use `<nav>` element, provide descriptive aria-label, support keyboard navigation
- **Real-World Use**: Use `aria-current="page"` for current page, `aria-expanded` for collapsible menus
- **Keyboard Navigation**: Support Tab, Enter, Escape keys for navigation
- **Best Practice**: Use semantic HTML, provide clear labels, ensure keyboard accessibility
- **Interview Tip**: Explain that accessible menus work with keyboard and screen readers

---

## 55) What are the different ARIA live regions?

ARIA live regions announce dynamic content changes to screen readers without interrupting current reading.

```html
<div aria-live="polite" id="status">Status updates appear here</div>
<div aria-live="assertive" id="alert">Error message appears here</div>
```

- **Core Types**: `polite` (announces when user finishes), `assertive` (interrupts immediately), `off` (no announcements)
- **Real-World Use**: Use for status updates, errors, notifications, or dynamic content changes
- **Best Practice**: Use `polite` for most cases, `assertive` only for urgent messages
- **Important Rule**: Don't overuse assertive regions, they interrupt user's current task
- **Interview Tip**: Explain that live regions announce dynamic content to screen readers

---

## 56) How do you create accessible modal dialogs?

Use proper ARIA attributes, focus management, and keyboard navigation for accessible modal dialogs.

```html
<button onclick="openModal()">Open Settings</button>
<div role="dialog" aria-labelledby="modal-title" aria-modal="true" aria-hidden="true" id="modal">
  <h2 id="modal-title">Settings</h2>
  <button onclick="closeModal()">Close</button>
</div>
```

- **Core Requirements**: Use `role="dialog"`, `aria-modal="true"`, trap focus, close on Escape
- **Real-World Use**: Modal dialogs need focus management, keyboard navigation, and proper ARIA
- **Best Practice**: Trap focus within modal, return focus to trigger element when closed
- **Accessibility**: Screen readers announce modal and can navigate it properly
- **Interview Tip**: Explain that accessible modals require focus management and ARIA

---

## 57) What is the purpose of `tabindex` attribute?

`tabindex` controls keyboard navigation order and focusability of elements.

```html
<button tabindex="0">Button 1</button>
<input type="text" tabindex="0">
<button tabindex="-1">Skip from tab order</button>
```

- **Core Values**: `0` (focusable in natural order), `-1` (focusable but not in tab order), positive numbers (avoid)
- **Real-World Use**: Use for custom interactive elements, skip decorative elements from tab order
- **Best Practice**: Avoid positive numbers (custom tab order), use `0` or `-1` only
- **Accessibility**: Essential for keyboard accessibility and focus management
- **Interview Tip**: Explain that tabindex controls keyboard navigation, not just visual order

---

## 58) How do you create accessible data tables?

Use proper table structure with headers, captions, and ARIA attributes for complex data tables.

```html
<table role="table" aria-label="Employee Directory">
  <caption>Employee Directory - Q1 2024</caption>
  <thead>
    <tr role="row">
      <th scope="col" role="columnheader">Name</th>
      <th scope="col" role="columnheader">Department</th>
    </tr>
  </thead>
  <tbody>
    <tr role="row">
      <td role="cell">John Doe</td>
      <td role="cell">Engineering</td>
    </tr>
  </tbody>
</table>
```

- **Core Requirements**: Use explicit ARIA roles for complex tables, `scope` for header relationships
- **Real-World Use**: `role="columnheader"` for column headers, `role="rowheader"` for row headers
- **Best Practice**: Use `scope` attribute to define header relationships
- **Accessibility**: Screen readers understand table structure and relationships
- **Interview Tip**: Explain that complex tables need explicit ARIA roles and scope

---

## 59) What are the WCAG guidelines and how do they apply to HTML?

WCAG provides standards for accessible web content with four principles: Perceivable, Operable, Understandable, Robust.

```html
<img src="chart.jpg" alt="Sales increased 25% in Q3">
<button onclick="submitForm()" tabindex="0">Submit</button>
<label for="email">Email Address:</label>
<input type="email" id="email" required>
```

- **Core Principles**: POUR (Perceivable, Operable, Understandable, Robust)
- **Real-World Impact**: WCAG 2.1 has three levels (A, AA, AAA), most organizations target AA
- **Legal Requirement**: Required by law in many countries (ADA, Section 508, EU Accessibility Act)
- **Best Practice**: Follow WCAG guidelines for text, images, forms, navigation
- **Interview Tip**: Explain that WCAG is the standard for web accessibility

---

## 60) How do you test HTML for accessibility issues?

Use automated tools, manual testing, and assistive technologies to identify and fix accessibility issues.

```html
<button aria-label="Close dialog">×</button>
<a href="#main" class="skip-link">Skip to main content</a>
<p style="color: #000; background: #fff;">High contrast text</p>
<button style="outline: 2px solid blue;">Button with focus</button>
```

- **Automated Tools**: Use axe, WAVE, Lighthouse for automated accessibility testing
- **Manual Testing**: Test with screen readers (NVDA, JAWS, VoiceOver), keyboard-only navigation
- **Real-World Checklist**: Check color contrast, validate HTML, test focus indicators
- **User Testing**: Test with real users when possible for best results
- **Interview Tip**: Explain that accessibility testing requires both automated and manual testing

---
