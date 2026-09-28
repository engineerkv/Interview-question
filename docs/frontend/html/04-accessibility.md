---
sidebar_label: "Accessibility"
---
# ♿ 4. Accessibility (Q46–58)
> **Reviewed:** 2026-09 · Modernized; legacy topics are labeled.

---

## Q46. ♿ Accessibility and why it's important

Web accessibility ensures websites are usable by people with disabilities - it follows WCAG guidelines for inclusive design and benefits everyone, not just people with disabilities. Make websites usable by people with disabilities (visual, motor, cognitive, hearing).

- **Trade-offs**: The catch is required by law in many jurisdictions (ADA, Section 508, EU Accessibility Act) - follow **WCAG 2.2 AA** guidelines for inclusive design (older policies may still reference 2.1 AA; 2.2 is a superset apart from the removed 4.1.1 Parsing criterion). Accessibility is not just nice-to-have, it's essential for inclusive web, but watch out - the WHO estimates about 1.3 billion people (roughly 1 in 6) live with a significant disability, and accessible markup also improves SEO and UX for all users. The **European Accessibility Act** has applied to many consumer-facing products and services since June 2025.

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
<div id="menu" hidden>Menu content</div>

```

- **First rule of ARIA**: if a native element or attribute gives you the semantics and behaviour (`<button>`, `<dialog>`, `<details>`, `hidden`, `disabled`, `required`), use it instead of ARIA. "No ARIA is better than bad ARIA" — wrong roles or stale states (`aria-expanded` never updated) make things worse. Use the hidden attribute (or `display: none`) to hide collapsed content from everyone; `aria-hidden` only hides from assistive tech. For custom widgets, follow the WAI-ARIA Authoring Practices Guide (APG) patterns for roles and keyboard behaviour.

---

## Q48. 💡 Writing good alt text for images

Provide meaningful `alt` text that describes the image's content and purpose - use empty alt for decorative images, alt text enables screen readers to understand images. Alt text should be descriptive and concise, describe content and purpose.

- **Trade-offs**: The catch is don't start with "Image of" or "Picture of", consider context - for complex images (charts, diagrams) give a short `alt` plus a longer description in visible text, a `<figcaption>`, or a linked data table (referenced with `aria-describedby`). Alt text enables screen readers to understand images, but watch out - informative images need alt text, decorative images need empty alt (`alt=""`), and a missing `alt` attribute makes screen readers read the file name.

> **Legacy note (2026):** The `longdesc` attribute is obsolete in the HTML Living Standard and poorly supported — don't recommend it. Also, `role="presentation"` is redundant on an image that already has `alt=""`. AI-generated alt text can be a starting point, but a human should check it describes the image's *purpose in context*.

Example:

```html
<img src="sales-chart.jpg" alt="Bar chart showing 25% increase in sales from Q2 to Q3 2024">
<img src="decoration.jpg" alt="">

<figure>
  <img src="architecture.png" alt="System architecture overview" aria-describedby="arch-desc">
  <figcaption id="arch-desc">Requests go from the CDN to the API gateway, then to three services…</figcaption>
</figure>

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
  <input type="text" id="name" name="name" required autocomplete="name" aria-describedby="name-help name-error">
  <div id="name-help">Enter your full legal name</div>
  <div id="name-error" role="alert"></div>
</fieldset>

```

- **2026 checklist**: set `autocomplete` tokens (`email`, `name`, `current-password`, `one-time-code`) — WCAG 1.3.5 and 3.3.7 (Redundant Entry) reward it; set `aria-invalid="true"` on fields with errors; never rely on placeholder as the label; allow paste in password/OTP fields (WCAG 2.2 3.3.8 Accessible Authentication); and move focus to an error summary or the first invalid field on submit.

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

<!-- Equivalent roles with implicit live behaviour -->
<div role="status"></div>  <!-- polite -->
<div role="alert"></div>   <!-- assertive -->

```

- **Common pitfall**: the live region must already be **in the DOM (and empty) before** you inject the message — a region inserted together with its content is often not announced. This matters in React/SPAs: render the empty container on mount, then update its text. Keep messages short, and avoid firing many updates in quick succession.

---

## Q55. 📝 Creating accessible modal dialogs

Use the native **`<dialog>` element with `showModal()`** as the default in 2026 (Baseline since 2022). It gives you, for free: the `dialog` role, modal behaviour (the rest of the page becomes inert), focus moved into the dialog, **Escape to close**, rendering in the **top layer** (no `z-index` fights), and a `::backdrop` pseudo-element. Label it with `aria-labelledby` pointing at its heading.

- **Trade-offs**: The catch is you still need to return focus to the trigger element when closed (browsers generally do this for `showModal()`, but verify in your target browsers and frameworks), and you should put `autofocus` on the most sensible initial control. `dialog.show()` (non-modal) does **not** trap focus or make the page inert. Hand-rolled `<div role="dialog" aria-modal="true">` modals are the **legacy** approach — they need a manual focus trap, Escape handling, scroll locking, and `inert` on the background, and are easy to get wrong. The `closedby="any"` attribute (light dismiss on backdrop click) is newer and not yet in all engines.

Example:

```html
<button id="open">Open Settings</button>

<dialog id="settings" aria-labelledby="settings-title">
  <h2 id="settings-title">Settings</h2>
  <form method="dialog">
    <label>Theme <select name="theme"><option>Light</option><option>Dark</option></select></label>
    <button value="cancel">Cancel</button>
    <button value="save" autofocus>Save</button>
  </form>
</dialog>

<script>
  const dialog = document.getElementById('settings');
  document.getElementById('open').addEventListener('click', () => dialog.showModal());
  dialog.addEventListener('close', () => console.log(dialog.returnValue)); // "save" or "cancel"
</script>

```

```html
<!-- Legacy pattern (still seen in older codebases/libraries) -->
<div role="dialog" aria-labelledby="modal-title" aria-modal="true" id="modal" hidden>
  <h2 id="modal-title">Settings</h2>
  <button onclick="closeModal()">Close</button>
</div>

```

- **Related**: for non-modal overlays like menus, tooltips-with-content, and toasts, the **Popover API** (`popover` attribute + `popovertarget`) gives top-layer rendering and light-dismiss without JS — see Q73 in [HTML5 & Modern APIs](./05-html5-and-modern-apis.md).

---

## Q56. 📇 Purpose of `tabindex`

`tabindex` controls keyboard navigation order and focusability of elements - tabindex controls keyboard navigation, not just visual order. `0` (focusable in natural order), `-1` (focusable but not in tab order), positive numbers (avoid).

- **Trade-offs**: The catch is avoid positive numbers (custom tab order), use `0` or `-1` only - essential for keyboard accessibility and focus management. tabindex controls keyboard navigation, not just visual order, but watch out - use for custom interactive elements, skip decorative elements from tab order.

Example:

```html
<button tabindex="0">Button 1</button>
<input type="text" tabindex="0">
<button tabindex="-1">Skip from tab order</button>

<!-- Remove a whole region (e.g. behind a custom drawer) from focus AND the accessibility tree -->
<main inert>…</main>

```

- **Modern note**: the `inert` attribute (Baseline since 2023) makes a subtree non-focusable, non-clickable, and hidden from assistive tech — the clean replacement for manually setting `tabindex="-1"` on every background element. Use `tabindex="-1"` on headings or containers you move focus to programmatically (e.g. after an SPA route change). For widgets like tabs or toolbars, use a **roving tabindex** (only the active item has `tabindex="0"`).

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

- **2026 workflow**:
  - **Lint**: `eslint-plugin-jsx-a11y` (React) or equivalent
  - **Automated in CI**: axe-core via `jest-axe`/`vitest-axe`, the Storybook a11y addon, and `@axe-core/playwright` on key pages — fail builds on serious/critical violations
  - **Manual**: keyboard-only pass, zoom to 200–400%, screen readers (NVDA + Firefox/Chrome, VoiceOver + Safari on macOS/iOS, TalkBack on Android, JAWS if your users need it)
  - Automated tools only catch a portion of issues; they can't judge meaningful alt text, logical focus order, or whether a flow makes sense by ear. See [Frontend Accessibility deep dive](../architecture/21-accessibility.md).

---

## Q58. 💡 WCAG guidelines

WCAG provides standards for accessible web content with four principles: Perceivable, Operable, Understandable, Robust - WCAG is the standard for web accessibility. POUR (Perceivable, Operable, Understandable, Robust).

- **Trade-offs**: The catch is required by law in many countries (ADA, Section 508, EU Accessibility Act) - follow WCAG guidelines for text, images, forms, navigation. WCAG is the standard for web accessibility, but watch out - WCAG has three levels (A, AA, AAA), and most organizations target AA.

- **Current version: WCAG 2.2** (W3C Recommendation, October 2023). New AA-relevant criteria include:
  - **2.4.11 Focus Not Obscured (Minimum)** – sticky headers/banners must not completely hide the focused element
  - **2.5.7 Dragging Movements** – provide a non-drag alternative
  - **2.5.8 Target Size (Minimum)** – pointer targets at least 24×24 CSS px (or adequately spaced)
  - **3.3.7 Redundant Entry** (A) and **3.3.8 Accessible Authentication (Minimum)** – don't make users re-enter info or solve memory/transcription puzzles to log in
  - **3.2.6 Consistent Help** (A)
  - **4.1.1 Parsing was removed** (obsolete now that browsers parse HTML consistently)

> **Legacy note (2026):** WCAG 2.0/2.1 are still referenced by some laws and contracts, but new work should target 2.2 AA. WCAG 3 is an early working draft, not a compliance target.

Example:

```html
<img src="chart.jpg" alt="Sales increased 25% in Q3">
<button onclick="submitForm()" tabindex="0">Submit</button>
<label for="email">Email Address:</label>
<input type="email" id="email" required>

```

---

