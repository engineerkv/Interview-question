# ♿ Accessibility

---

## 📍 Navigation

<div align="center">

[← Previous: Logging & Monitoring](20%29%20Logging%20%26%20Monitoring.md) • [Home: Questions Index](question.md) • [Next: Offline Support →](22%29%20Offline%20Support.md)

[📋 Cheatsheet](FE-System-Design%20Interview%20Cheatsheet.md)

</div>

---

---

## Q92. Keyboard Accessibility

Keyboard accessibility ensures that all interactive elements and flows can be used without a mouse, using only the keyboard (Tab, Shift+Tab, Enter, Space, Arrow keys). It's critical for many users with motor or visual impairments. Building keyboard-accessible interfaces is not just about compliance - it's about creating inclusive experiences that work for everyone.

---

## 1. Requirements

### 🔹 Focusable elements

* Use semantic elements: `button`, `a`, `input`, `select`, `textarea`

* Avoid `div`/`span` with click handlers unless you add:
  * `tabindex="0"` and
  * `role` + keyboard handlers

### 🔹 Logical tab order

* DOM order should match visual order

* Avoid large `tabindex` values; prefer natural flow

📌 **In simple terms**: Users should be able to reach and operate everything using Tab and Enter.

---

## 2. Implementation tips

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

## Q93. Screen Reader

Screen readers read out the content and structure of the page to users who can’t see the screen. Good screen reader support relies on semantic HTML, meaningful labels, and ARIA only when needed.

---

## 1. Semantic structure

* Proper heading hierarchy (`h1` → `h2` → `h3`…)

* Landmarks:
  * `header`, `nav`, `main`, `footer`, `aside`

* Lists (`ul`, `ol`) and tables with headers

📌 **In simple terms**: Semantic HTML gives screen readers a map of the page.

---

## 2. Labels and ARIA

* Use `<label for>` or `aria-label` / `aria-labelledby` for inputs

* Use ARIA roles and attributes only when semantics aren’t available

* Keep ARIA in sync with actual behavior (e.g., expanded/collapsed states)

---

## ⭐ Summary — 10-second Interview Version

> "Screen reader support comes from semantic HTML and clear labels first, with ARIA used sparingly to fill gaps. I structure pages with landmarks and headings so assistive tech has a clear map."

---

## ⭐ Extra Points (If Interviewer Asks More)

### How do you test screen reader behavior?

Use built-in screen readers like VoiceOver (macOS) or NVDA (Windows), navigate by headings/landmarks, and listen to how controls are announced.

---

## Q94. Focus Management

Focus management is about controlling which element is focused at any time, especially during dynamic UI changes like modals, drawers, and navigation.

---

## 1. Key patterns

* **Initial focus** – when opening a modal, focus the first meaningful element

* **Focus trap** – keep Tab focus inside the modal until it’s closed

* **Focus restoration** – return focus to the triggering element on close

📌 **In simple terms**: Focus should always “follow the user’s attention” and never get lost.

---

## 2. Implementation tips

* Use libraries (e.g., `focus-trap`) or UI frameworks with built-in support

* Avoid programmatically focusing elements too often; only when context changes

---

## ⭐ Summary — 10-second Interview Version

> "Good focus management ensures that opening and closing modals or pages always sends focus to the right place and keeps keyboard users inside the active context."

---

## ⭐ Extra Points (If Interviewer Asks More)

### Common bug?

Closing a modal without restoring focus, leaving keyboard users at the top of the page or with no visible focus.

---

## Q95. Color Contrast

Color contrast ensures text and important UI elements are readable for users with low vision or color vision deficiencies.

---

## 1. WCAG contrast ratios

* Normal text: **4.5:1** (AA)

* Large text (≥18pt regular or 14pt bold): **3:1** (AA)

* UI components and graphics: 3:1

📌 **In simple terms**: Foreground and background colors must be different enough to read easily.

---

## 2. Practical steps

* Use contrast checkers (axe, WebAIM, browser extensions)

* Avoid relying on color alone to convey meaning (add icons, text)

* Test themes (light/dark) against different backgrounds

---

## ⭐ Summary — 10-second Interview Version

> "Color contrast is about making sure text and key UI elements meet WCAG ratios like 4.5:1 so these elements are readable for everyone, including users with low vision."

---

## ⭐ Extra Points (If Interviewer Asks More)

### How do you fix poor contrast without redesigning everything?

Tweak one side of the color pair (usually text) towards darker or lighter while keeping brand colors for accents.

---

## Q96. Accessibility Tools

Accessibility tools help you automatically catch many issues and manually explore others. These tools are essential for integrating accessibility into your workflow.

---

## 1. Automated tools

* **axe DevTools**, **Lighthouse**, **WAVE**

* Browser devtools accessibility panels

* CI integrations to fail builds on critical issues

📌 **In simple terms**: Automated tools act as linting and testing for accessibility basics.

---

## 2. Manual tools

* Screen readers (NVDA, JAWS, VoiceOver)

* Keyboard-only navigation

* Color blindness simulators

---

## ⭐ Summary — 10-second Interview Version

> "Accessibility tools like axe and Lighthouse catch many problems automatically, and I combine them with manual keyboard and screen reader checks."

---

## ⭐ Extra Points (If Interviewer Asks More)

### How do you add accessibility checks to CI?

Run Lighthouse or axe against key pages, set thresholds, and fail builds when regressions appear.

---

## Q97. How to Fix Accessibility Issues

Fixing accessibility issues is an iterative process: discover problems, prioritize them by impact, and fix them using semantic HTML, ARIA, and design tweaks.

---

## 1. Typical issues and fixes

* Missing labels → add `<label>` or `aria-label`

* Incorrect heading order → restructure headings

* Low contrast → adjust colors

* Keyboard traps → fix focus handling and remove onclick-only interactions

📌 **In simple terms**: Most fixes are about using the right HTML elements and making sure these elements are labeled and reachable.

---

## 2. Workflow

1. Run automated tools and gather issues

2. Validate with manual testing for critical flows

3. Fix issues and re-test

4. Educate team and update component library so problems don’t come back

---

## ⭐ Summary — 10-second Interview Version

> "To fix accessibility, I use tools to find issues, manually verify important flows, then fix them using semantic HTML, proper labels, color tweaks, and better focus management."

---

## ⭐ Extra Points (If Interviewer Asks More)

### How do you prevent recurring accessibility issues?

Bake accessibility into shared components and design system, add lint rules, and include a11y checks in PR reviews and CI.

---

---

## 📍 Navigation

<div align="center">

[16) Logging & Monitoring.md](16%29%20Logging%20&%20Monitoring.md) • [Questions Index](question.md) • [18) Offline Support.md →](18%29%20Offline%20Support.md)

[FE-System-Design Cheatsheet](FE-System-Design%20Interview%20Cheatsheet.md]

</div>

---
