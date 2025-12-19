# 🧒 1. Fundamentals & Basics (Q1–13)

---

## 📍 Navigation

<div align="center">

[Home: README](../README.md) • [Next: Layout & Styling →](02%29%20Layout%20%26%20Styling.md)

[📋 Cheatsheet](CSS%20Interview%20Cheatsheet.md)

</div>

---

---

## Q1. 🎨 CSS and what it stands for

CSS stands for Cascading Style Sheets - it's a stylesheet language that describes how HTML documents look, separating content from presentation for maintainable styling. Separates content (HTML) from presentation (CSS), enables consistent styling across web pages.

- **Trade-offs**: The catch is mixing content and presentation, not using external stylesheets - works with HTML, XML, and other markup languages, essential for modern web. CSS enables maintainable, scalable styling, but watch out - supports responsive design, animations, and modern web development.

Example:

```css
body {
  font-family: Arial, sans-serif;
  background-color: #f0f0f0;
  margin: 0;
  padding: 20px;
}

```

---

## Q2. 🎨 Different ways to include CSS in a webpage

CSS can be included via inline styles, internal stylesheets, or external stylesheet files - external stylesheets are preferred for production websites because these can be cached and reused. Inline (highest specificity), internal (page-specific), external (best for reusability).

- **Trade-offs**: The catch is overusing inline styles, hard to maintain - use external CSS for maintainability and caching. External stylesheets are preferred for production websites, but watch out - external CSS can be cached by browsers, use external CSS for production.

Example:

```html
<p style="color: red;">Inline styling</p>
<style>
  body { background-color: #f0f0f0; }
</style>
<link rel="stylesheet" href="styles.css">

```

---

## Q3. 🎨 CSS selectors and examples

CSS selectors target HTML elements to apply styles, using various patterns to match elements - selector specificity determines which styles apply when multiple rules match. Selectors determine which elements get styled, more specific selectors override less specific ones.

- **Trade-offs**: The catch is IDs should be unique per page, don't overuse IDs for styling - use classes for styling, IDs for JavaScript targeting. Selector specificity determines which styles apply, but watch out - combine selectors for precise targeting, use classes for reusable styles.

Example:

```css
p { color: blue; }
.highlight { background-color: yellow; }
#header { font-size: 24px; }
div p { margin: 10px; }

```

---

## Q4. 🏛️ Element, class, and ID selectors: differences

Element selectors target HTML tags, class selectors target elements with specific class attributes, and ID selectors target unique elements - classes are preferred for styling, IDs for JavaScript hooks. Element (broad targeting), class (reusable), ID (unique, highest specificity).

- **Trade-offs**: The catch is using IDs for styling (should use classes), not understanding specificity - use classes for reusable styles, IDs for JavaScript targeting. Classes are preferred for styling, IDs for JavaScript hooks, but watch out - specificity order: ID > Class > Element, use classes for styling.

Example:

```css
p { color: black; }
.highlight { background-color: yellow; }
#header { font-size: 24px; }

```

---

## Q5. 🧩 CSS Box Model and its components

The CSS Box Model defines how every HTML element is structured with four layers: content (inside), padding (space inside), border (line), and margin (space outside). Understanding the box model is crucial for creating precise layouts and avoiding unexpected sizing issues.

- **Trade-offs**: The catch is `content-box` (default) adds padding and border to width/height, causing overflow issues - use `border-box` globally for predictable sizing. `content-box` adds padding/border to total size, `border-box` includes them in width/height, but watch out - margin collapses vertically between adjacent elements, padding shows background color, margin is transparent.

Example:

```css
.box {
  width: 200px;
  padding: 20px;
  border: 2px solid black;
  margin: 10px;
  box-sizing: border-box;
}
```

---

## Q6. 🤔 Margin vs padding

Margin creates space outside an element's border, while padding creates space inside an element's border - padding is inside the border, margin is outside. Padding (inside space, affects background color), margin (outside space, transparent, can collapse).

- **Trade-offs**: The catch is not understanding margin collapse, confusing padding and margin - use padding for internal spacing, margin for external spacing. Padding is inside the border, margin is outside, but watch out - padding increases element size, margin doesn't affect element size.

Example:

```css
.element {
  padding: 20px;
  margin: 10px;
  border: 1px solid black;
  background-color: lightgray;
}

```

---

## Q7. 💡 Purpose of the `box-sizing` property

`box-sizing` controls how the total width and height of an element is calculated, including or excluding padding and borders - border-box is preferred for predictable layouts. `content-box` (default, width/height = content only), `border-box` (includes padding and border).

- **Trade-offs**: The catch is not using border-box, causing layout issues with padding - use `* { box-sizing: border-box; }` for consistent behavior. Border-box is preferred for predictable layouts, but watch out - border-box makes layouts more predictable, modern CSS frameworks use it by default.

Example:

```css
.default {
  width: 200px;
  padding: 20px;
  border: 2px solid black;
}
.border-box {
  width: 200px;
  padding: 20px;
  border: 2px solid black;
  box-sizing: border-box;
}

```

---

## Q8. 🤔 `display: block`, `inline`, and `inline-block`: differences

These display values control how elements flow and interact with other elements on the page - inline-block is useful for buttons and form elements because it flows like inline but respects all properties. Block (full width, new line), inline (flows with text, ignores width/height), inline-block (flows like inline but respects all properties).

- **Trade-offs**: The catch is inline elements ignore width/height, only horizontal margins work - inline-block is best of both—flows like inline but respects all properties. Inline-block is useful for buttons and form elements, but watch out - use block for major layout elements, inline-block for buttons and form elements.

Example:

```css
.block {
  display: block;
  background-color: red;
  margin: 10px 0;
}
.inline {
  display: inline;
  background-color: blue;
}
.inline-block {
  display: inline-block;
  width: 100px;
  background-color: green;
}

```

---

## Q9. 🏛️ Pseudo-classes and pseudo-elements and examples

Pseudo-classes target element states (like `:hover`), while pseudo-elements create virtual elements (like `::before`) - pseudo-classes target states, pseudo-elements create new elements. Pseudo-classes use single colon `:`, pseudo-elements use double colon `::`.

- **Trade-offs**: The catch is `::before` requires `content` property to be visible - use pseudo-classes for states, pseudo-elements for generated content. Pseudo-classes target states, pseudo-elements create new elements, but watch out - pseudo-classes for states (`:hover`, `:focus`), pseudo-elements for generated content (`::before`, `::after`).

Example:

```css
.button:hover {
  background-color: blue;
  transform: scale(1.1);
}
.button::before {
  content: "★ ";
  color: gold;
}
a:visited { color: purple; }
p::first-line { font-weight: bold; }

```

---

## Q10. 🎨 CSS specificity and how it's calculated

CSS specificity determines which CSS rule wins when multiple rules target the same element - calculated as (inline styles, IDs, classes, elements) with higher specificity winning. When specificity is equal, source order matters.

- **Trade-offs**: The catch is overusing IDs makes styles hard to override, escalating specificity creates maintenance issues - use classes over IDs, keep specificity low. Inline styles (1,0,0,0) have highest specificity, IDs (0,1,0,0) beat classes (0,0,1,0), but watch out - `!important` overrides all specificity, combinators don't add specificity, use classes for maintainability.

Example:

```css
p { color: black; }              /* 0,0,0,1 */
.highlight { color: yellow; }    /* 0,0,1,0 - wins */
#header { color: blue; }         /* 0,1,0,0 - wins over class */
```

---

## Q11. 🎨 Relative vs absolute CSS units

Relative units scale based on context (em, rem, %, vw, vh), while absolute units are fixed (px, pt, cm) - relative units are better for responsive design because they adapt to different screen sizes. Relative units (em, rem, %, vw, vh) scale with context, absolute units (px, pt) are fixed.

- **Trade-offs**: The catch is mixing absolute and relative units inconsistently - rem is relative to root font-size, em is relative to parent font-size. Relative units are better for responsive design, but watch out - use rem for font sizes, vw/vh for viewport-based sizing, % for responsive layouts.

Example:

```css
.container {
  font-size: 16px;           /* absolute */
  padding: 1em;              /* relative to font-size */
  width: 50%;                /* relative to parent */
  height: 100vh;             /* relative to viewport */
}

```

---

## Q12. 🤔 `position: relative`, `absolute`, `fixed`, and `sticky`: differences

Positioning controls how elements are placed - `relative` positions relative to itself, `absolute` to nearest positioned parent, `fixed` to viewport, `sticky` toggles between relative and fixed, understanding positioning is key to complex layouts. `relative` positions relative to normal flow, `absolute` to positioned parent, `fixed` to viewport, `sticky` toggles.

- **Trade-offs**: The catch is `absolute` positions relative to nearest positioned ancestor, not always parent - `sticky` needs a threshold (top/bottom) and works within parent container. Understanding positioning is key to complex layouts, but watch out - use `absolute` for overlays, `fixed` for headers/footers, `sticky` for scroll effects.

Example:

```css
.relative {
  position: relative;
  top: 10px;
  left: 20px;
}
.absolute {
  position: absolute;
  top: 0;
  right: 0;
}
.fixed {
  position: fixed;
  bottom: 0;
  right: 0;
}
.sticky {
  position: sticky;
  top: 0;
}

```

---

## Q13. 🛠️ What is a CSS preprocessor?

CSS preprocessors are tools that extend CSS with programming features like variables, nesting, mixins, and functions, then compile back to standard CSS that browsers can understand - preprocessors enhance CSS with powerful features while maintaining browser compatibility. Preprocessors add variables, nesting, mixins, functions, and imports to CSS before compilation.

- **Trade-offs**: The catch is requiring a build step to compile preprocessor code to CSS, learning new syntax - preprocessors improve maintainability and reduce code duplication. Preprocessors enhance CSS with powerful features while maintaining browser compatibility, but watch out - popular preprocessors include Sass/SCSS, Less, and Stylus, each with unique syntax and features.

Example:

```scss
// Variables
$primary-color: #007bff;
$spacing: 20px;

// Nesting
.button {
  padding: $spacing;
  background-color: $primary-color;

  &:hover {
    background-color: darken($primary-color, 10%);
  }
}

// Mixins
@mixin flex-center {
  display: flex;
  justify-content: center;
  align-items: center;
}

.container {
  @include flex-center;
}
```

---

---

## 📍 Navigation

<div align="center">

[Home: README](../README.md) • [Next: Layout & Styling →](02%29%20Layout%20%26%20Styling.md)

[📋 Cheatsheet](CSS%20Interview%20Cheatsheet.md)

</div>

---
