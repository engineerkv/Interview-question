# ♿ 4. Accessibility (A11y) (Q46–60)

---

## 📍 Navigation

<div align="center">

[Forms & Input Elements](03%29%20Forms%20%26%20Input%20Elements.md) • [Home: README](../README.md) • [HTML5 Features & APIs →](05%29%20HTML5%20Features%20%26%20APIs.md)

[📋 Cheatsheet](HTML%20Interview%20Cheatsheet.md)

</div>

---

---

## Q46. ♿ Accessibility and why it's important

Web accessibility ensures websites are usable by people with disabilities - it follows WCAG guidelines for inclusive design and benefits everyone, not just people with disabilities. Make websites usable by people with disabilities (visual, motor, cognitive, hearing).

- **Trade-offs**: The catch is required by law in many jurisdictions (ADA, Section 508, EU Accessibility Act) - follow WCAG 2.1 AA guidelines for inclusive design. Accessibility is not just nice-to-have, it's essential for inclusive web, but watch out - benefits 15% of global population, improves SEO and UX for all users.

Example:

```html
<img src="chart.jpg" alt="Sales increased 25% in Q3 2024" width="400" height="300">
<button aria-label="Close dialog" onclick="closeModal()">Close</button>

```

---

## Q47. ❓ ARIA attributes and how to use them

ARIA attributes provide additional information to screen readers when semantic HTML isn't sufficient - ARIA supplements HTML, doesn't replace semantic HTML. Enhance accessibility when semantic HTML isn't enough.

- **Trade-offs**: The catch is use semantic HTML first, add ARIA only when needed - don't override native semantics, ARIA doesn't change visual appearance. ARIA supplements HTML, doesn't replace semantic HTML, but watch out - good for dynamic content, custom widgets, or complex interactions.

Example:

```html
<button aria-expanded="false" aria-controls="menu" onclick="toggleMenu()">Menu</button>
<div id="menu" aria-hidden="true">Menu content</div>

```

---

## Q48. 💡 Writing good alt text for images

Provide meaningful `alt` text that describes the image's content and purpose - use empty alt for decorative images, alt text enables screen readers to understand images. Alt text should be descriptive and concise, describe content and purpose.

- **Trade-offs**: The catch is don't start with "Image of" or "Picture of", consider context - use `longdesc` for complex images needing detailed descriptions. Alt text enables screen readers to understand images, but watch out - informative images need alt text, decorative images need empty alt.

Example:

```html
<img src="sales-chart.jpg" alt="Bar chart showing 25% increase in sales from Q2 to Q3 2024">
<img src="decoration.jpg" alt="" role="presentation">

```

---

## Q49. 🤔 `aria-label` vs `aria-labelledby`

`aria-label` provides a direct label, while `aria-labelledby` references other elements that serve as the label - `aria-labelledby` is better when visible labels exist. `aria-label` is direct text, `aria-labelledby` references other elements.

- **Trade-offs**: The catch is `aria-labelledby` takes precedence over `aria-label` - `aria-labelledby` can reference multiple elements (space-separated IDs). `aria-labelledby` is better when visible labels exist, but watch out - use `aria-label` when no visible label, `aria-labelledby` when visible label exists.

Example:

```html
<button aria-label="Close dialog">×</button>
<input type="search" aria-label="Search products">

<div id="search-label">Search</div>
<input type="text" aria-labelledby="search-label">

```

---

## Q50. 📝 Making forms accessible

Use proper labels, grouping, and ARIA attributes to make forms accessible to screen readers and keyboard users - accessible forms work for screen readers and keyboard users. Always provide labels, use fieldset/legend for groups, associate help text.

- **Trade-offs**: The catch is test with keyboard navigation, ensure all controls are focusable - use proper input types, validation attributes, and clear instructions. Accessible forms work for screen readers and keyboard users, but watch out - use `aria-describedby` for help text, `role="alert"` for error messages.

Example:

```html
<fieldset>
  <legend>Contact Information</legend>
  <label for="name">Full Name:</label>
  <input type="text" id="name" name="name" required aria-describedby="name-help">
  <div id="name-help">Enter your full legal name</div>
</fieldset>

```

---

## Q51. 💡 Creating accessible tables

Use proper table structure with headers, captions, and ARIA attributes to make data tables accessible - accessible tables require proper structure and headers. Use `<caption>` for description, `<th>` for headers, `scope` for relationships.

- **Trade-offs**: The catch is use `<thead>`, `<tbody>`, `<tfoot>` for proper table structure - screen readers announce headers with data cells. Accessible tables require proper structure and headers, but watch out - `scope="col"` for column headers, `scope="row"` for row headers.

Example:

```html
<table>
  <caption>Monthly Sales Report for 2024</caption>
  <thead>
    <tr>
      <th scope="col">Month</th>
      <th scope="col">Sales</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>January</td>
      <td>$50,000</td>
    </tr>
  </tbody>
</table>

```

---

## Q52. 💡 Purpose of `aria-hidden`

`aria-hidden="true"` hides decorative elements from screen readers while keeping them visible to sighted users - aria-hidden is for decoration, not for hiding important content. Hide purely decorative elements from screen readers.

- **Trade-offs**: The catch is don't hide interactive elements, use for decorative content only - screen readers skip aria-hidden content, improves experience. aria-hidden is for decoration, not for hiding important content, but watch out - good for decorative icons, separators, or visual elements that don't add meaning.

Example:

```html
<button aria-label="Close dialog">
  <span aria-hidden="true">×</span>
</button>
<button aria-label="Search">
  <span aria-hidden="true">🔍</span>
</button>

```

---

## Q53. 🧭 Creating accessible navigation

Use semantic HTML with proper ARIA attributes and keyboard navigation support for accessible menus - accessible menus work with keyboard and screen readers. Use `<nav>` element, provide descriptive aria-label, support keyboard navigation.

- **Trade-offs**: The catch is support Tab, Enter, Escape keys for navigation - use semantic HTML, provide clear labels, ensure keyboard accessibility. Accessible menus work with keyboard and screen readers, but watch out - use `aria-current="page"` for current page, `aria-expanded` for collapsible menus.

Example:

```html
<nav aria-label="Main navigation">
  <ul>
    <li><a href="/" aria-current="page">Home</a></li>
    <li><a href="/about">About</a></li>
    <li><a href="/contact">Contact</a></li>
  </ul>
</nav>

```

---

## Q54. ❓ Live regions and how to use them

ARIA live regions announce dynamic content changes to screen readers without interrupting current reading - live regions announce dynamic content to screen readers. `polite` (announces when user finishes), `assertive` (interrupts immediately), `off` (no announcements).

- **Trade-offs**: The catch is use `polite` for most cases, `assertive` only for urgent messages - don't overuse assertive regions, they interrupt user's current task. Live regions announce dynamic content to screen readers, but watch out - good for status updates, errors, notifications, or dynamic content changes.

Example:

```html
<div aria-live="polite" id="status">Status updates appear here</div>
<div aria-live="assertive" id="alert">Error message appears here</div>

```

---

## Q55. 📝 Creating accessible modal dialogs

Use proper ARIA attributes, focus management, and keyboard navigation for accessible modal dialogs - accessible modals require focus management and ARIA. Use `role="dialog"`, `aria-modal="true"`, trap focus, close on Escape.

- **Trade-offs**: The catch is trap focus within modal, return focus to trigger element when closed - screen readers announce modal and can navigate it properly. Accessible modals require focus management and ARIA, but watch out - modal dialogs need focus management, keyboard navigation, and proper ARIA.

Example:

```html
<button onclick="openModal()">Open Settings</button>
<div role="dialog" aria-labelledby="modal-title" aria-modal="true" aria-hidden="true" id="modal">
  <h2 id="modal-title">Settings</h2>
  <button onclick="closeModal()">Close</button>
</div>

```

---

## Q56. 📇 Purpose of `tabindex`

`tabindex` controls keyboard navigation order and focusability of elements - tabindex controls keyboard navigation, not just visual order. `0` (focusable in natural order), `-1` (focusable but not in tab order), positive numbers (avoid).

- **Trade-offs**: The catch is avoid positive numbers (custom tab order), use `0` or `-1` only - essential for keyboard accessibility and focus management. tabindex controls keyboard navigation, not just visual order, but watch out - use for custom interactive elements, skip decorative elements from tab order.

Example:

```html
<button tabindex="0">Button 1</button>
<input type="text" tabindex="0">
<button tabindex="-1">Skip from tab order</button>

```

---

## Q57. 🧪 Testing for accessibility

Use automated tools, manual testing, and assistive technologies to identify and fix accessibility issues - accessibility testing requires both automated and manual testing. Use axe, WAVE, Lighthouse for automated accessibility testing.

- **Trade-offs**: The catch is check color contrast, validate HTML, test focus indicators - test with real users when possible for best results. Accessibility testing requires both automated and manual testing, but watch out - test with screen readers (NVDA, JAWS, VoiceOver), keyboard-only navigation.

Example:

```html
<button aria-label="Close dialog">×</button>
<a href="#main" class="skip-link">Skip to main content</a>
<p style="color: #000; background: #fff;">High contrast text</p>
<button style="outline: 2px solid blue;">Button with focus</button>

```

---

## Q58. 💡 WCAG guidelines

WCAG provides standards for accessible web content with four principles: Perceivable, Operable, Understandable, Robust - WCAG is the standard for web accessibility. POUR (Perceivable, Operable, Understandable, Robust).

- **Trade-offs**: The catch is required by law in many countries (ADA, Section 508, EU Accessibility Act) - follow WCAG guidelines for text, images, forms, navigation. WCAG is the standard for web accessibility, but watch out - WCAG 2.1 has three levels (A, AA, AAA), most organizations target AA.

Example:

```html
<img src="chart.jpg" alt="Sales increased 25% in Q3">
<button onclick="submitForm()" tabindex="0">Submit</button>
<label for="email">Email Address:</label>
<input type="email" id="email" required>

```

---

## Q59. 📄 Semantic HTML5 elements and their usage

Semantic HTML5 elements like `<header>`, `<nav>`, `<main>`, `<article>`, `<section>`, `<aside>`, and `<footer>` provide meaning to content structure - they improve accessibility by helping screen readers understand page layout and navigation. These elements create a clear document outline and make content more accessible to assistive technologies.

- **Trade-offs**: The catch is using semantic elements improves SEO and accessibility automatically - screen readers can navigate by landmarks, but you still need ARIA labels for complex interactions. Semantic elements provide built-in accessibility benefits, but watch out - these don't replace proper ARIA attributes for dynamic content.

Example:

```html
<header>
  <nav aria-label="Main navigation">
    <ul>
      <li><a href="/">Home</a></li>
      <li><a href="/about">About</a></li>
    </ul>
  </nav>
</header>
<main>
  <article>
    <h1>Article Title</h1>
    <p>Content here...</p>
  </article>
</main>
<footer>Copyright 2024</footer>

```

---

## Q60. 📄 HTML5 APIs overview

HTML5 APIs provide browser-native capabilities for modern web applications - they include Canvas, Web Storage, Geolocation, Web Workers, Service Workers, and more. These APIs enable rich, interactive experiences without plugins, making web apps more powerful and accessible.

- **Trade-offs**: The catch is browser support varies - always check compatibility and provide fallbacks for older browsers. HTML5 APIs enable powerful features, but watch out - some require HTTPS, and feature detection is essential for graceful degradation.

Example:

```html
<!-- Canvas API -->
<canvas id="myCanvas" width="200" height="200"></canvas>

<!-- Web Storage -->
<script>
  localStorage.setItem('key', 'value');
  const data = localStorage.getItem('key');
</script>

<!-- Geolocation -->
<script>
  navigator.geolocation.getCurrentPosition(position => {
    console.log(position.coords.latitude, position.coords.longitude);
  });
</script>

```

---

---

## 📍 Navigation

<div align="center">

[Forms & Input Elements](03%29%20Forms%20%26%20Input%20Elements.md) • [Home: README](../README.md) • [HTML5 Features & APIs →](05%29%20HTML5%20Features%20%26%20APIs.md)

[📋 Cheatsheet](HTML%20Interview%20Cheatsheet.md)

</div>

---
