# ♿ Accessibility

---

## 📍 Navigation

<div align="center">

[← Previous: Logging & Monitoring](20%29%20Logging%20%26%20Monitoring.md) • [Home: Questions Index](question.md) • [Next: Offline Support →](22%29%20Offline%20Support.md)

[📋 Cheatsheet](FE-System-Design%20Interview%20Cheatsheet.md)

</div>

---

---

## 1. ♿ Keyboard Accessibility

Keyboard accessibility ensures that all interactive elements and flows can be used without a mouse, using only the keyboard (Tab, Shift+Tab, Enter, Space, Arrow keys). It's critical for many users with motor or visual impairments. Building keyboard-accessible interfaces is not just about compliance - it's about creating inclusive experiences that work for everyone.

### 🔹 Requirements

### 🔹 Focusable elements

* Use semantic elements: `button`, `a`, `input`, `select`, `textarea`

* Avoid `div`/`span` with click handlers unless you add:
  * `tabindex="0"` and
  * `role` + keyboard handlers

### 🔹 Logical tab order

* DOM order should match visual order

* Avoid large `tabindex` values; prefer natural flow

📌 **In simple terms**: Users should be able to reach and operate everything using Tab and Enter.

### 🔹 Implementation Tips

* Ensure visible **focus outlines** (never remove them without replacement)

* Provide **skip links** to jump over navigation

* Trap focus inside modals and restore on close

---

## ⭐ Summary — 10-second Interview Version

> "Keyboard accessibility means every interactive element works with Tab and Enter in a logical order, with clear focus indicators. I use semantic elements, manage focus correctly, and never rely only on mouse interactions."

---

## ⭐ Extra Points (If Interviewer Asks More)

### How do you test keyboard accessibility quickly?

Try using the site with only a keyboard—Tab, Shift+Tab, Enter, Space, and Arrow keys—until you complete main flows.

---

### 🔹 💡 Screen Reader Support

Screen readers read out the content and structure of the page to users who can’t see the screen. Good screen reader support relies on semantic HTML, meaningful labels, and ARIA only when needed.

---

### 🔹 💡 Semantic structure

* Proper heading hierarchy (`h1` → `h2` → `h3`…)

* Landmarks:
  * `header`, `nav`, `main`, `footer`, `aside`

* Lists (`ul`, `ol`) and tables with headers

📌 **In simple terms**: Semantic HTML gives screen readers a map of the page.

### 🔹 Labels and ARIA

* Use `<label for>` or `aria-label` / `aria-labelledby` for inputs

* Use ARIA roles and attributes only when semantics aren’t available

* Keep ARIA in sync with actual behavior (e.g., expanded/collapsed states)

---

### 🔹 💡 Focus Management

Focus management is about controlling which element is focused at any time, especially during dynamic UI changes like modals, drawers, and navigation.

### 🔹 Key Patterns

* **Initial focus** – when opening a modal, focus the first meaningful element

* **Focus trap** – keep Tab focus inside the modal until it’s closed

* **Focus restoration** – return focus to the triggering element on close

📌 **In simple terms**: Focus should always “follow the user’s attention” and never get lost.

---

### 🔹 💡 Implementation tips

* Use libraries (e.g., `focus-trap`) or UI frameworks with built-in support

* Avoid programmatically focusing elements too often; only when context changes

---

### 🔹 💡 Color Contrast

Color contrast ensures text and important UI elements are readable for users with low vision or color vision deficiencies.

### 🔹 WCAG Contrast Ratios

* Normal text: **4.5:1** (AA)

* Large text (≥18pt regular or 14pt bold): **3:1** (AA)

* UI components and graphics: 3:1

📌 **In simple terms**: Foreground and background colors must be different enough to read easily.

### 🔹 Practical Steps

* Use contrast checkers (axe, WebAIM, browser extensions)

* Avoid relying on color alone to convey meaning (add icons, text)

* Test themes (light/dark) against different backgrounds

---

### 🔹 ♿ Accessibility Tools

Accessibility tools help you automatically catch many issues and manually explore others. These tools are essential for integrating accessibility into your workflow.

### 🔹 Automated Tools

* **axe DevTools**, **Lighthouse**, **WAVE**

* Browser devtools accessibility panels

* CI integrations to fail builds on critical issues

📌 **In simple terms**: Automated tools act as linting and testing for accessibility basics.

### 🔹 Manual Tools

* Screen readers (NVDA, JAWS, VoiceOver)

* Keyboard-only navigation

* Color blindness simulators

---

### 🔹 ♿ Fixing Accessibility Issues

Fixing accessibility issues is an iterative process: discover problems, prioritize them by impact, and fix them using semantic HTML, ARIA, and design tweaks.

### 🔹 Typical Issues and Fixes

* Missing labels → add `<label>` or `aria-label`

* Incorrect heading order → restructure headings

* Low contrast → adjust colors

* Keyboard traps → fix focus handling and remove onclick-only interactions

📌 **In simple terms**: Most fixes are about using the right HTML elements and making sure these elements are labeled and reachable.

### 🔹 Workflow

1. Run automated tools and gather issues

2. Validate with manual testing for critical flows

3. Fix issues and re-test

4. Educate team and update component library so problems don’t come back

---

## ⭐ Summary — 10-second Interview Version

> "Accessibility includes keyboard navigation (Tab, Enter, logical order), screen reader support (semantic HTML, ARIA, labels), focus management (traps, restoration), color contrast (WCAG ratios), accessibility tools (axe, Lighthouse, manual testing), and fixing issues (semantic HTML, proper labels, design tweaks). Build inclusive experiences that work for everyone."

---

---

## 📍 Navigation

<div align="center">

[← Previous: Logging & Monitoring](20%29%20Logging%20%26%20Monitoring.md) • [Home: Questions Index](question.md) • [Next: Offline Support →](22%29%20Offline%20Support.md)

[📋 Cheatsheet](FE-System-Design%20Interview%20Cheatsheet.md)

</div>

---
