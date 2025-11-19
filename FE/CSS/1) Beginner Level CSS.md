# 1. Beginner Level CSS (Q1–13)

---

## Q1. What is CSS and what does it stand for?

CSS stands for Cascading Style Sheets - it's a stylesheet language that describes how HTML documents look, separating content from presentation for maintainable styling. Separates content (HTML) from presentation (CSS), enables consistent styling.

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

## Q2. What are the different ways to include CSS in a webpage?

CSS can be included via inline styles, internal stylesheets, or external stylesheet files - external stylesheets are preferred for production websites because they can be cached and reused. Inline (highest specificity), internal (page-specific), external (best for reusability).

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

## Q3. What are CSS selectors? Give examples.

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

## Q4. What is the difference between element, class, and ID selectors?

Element selectors target HTML tags, class selectors target elements with specific class attributes, and ID selectors target unique elements - classes are preferred for styling, IDs for JavaScript hooks. Element (broad targeting), class (reusable), ID (unique, highest specificity).

- **Trade-offs**: The catch is using IDs for styling (should use classes), not understanding specificity - use classes for reusable styles, IDs for JavaScript targeting. Classes are preferred for styling, IDs for JavaScript hooks, but watch out - specificity order: ID > Class > Element, use classes for styling.

Example:

```css
p { color: black; }
.highlight { background-color: yellow; }
#header { font-size: 24px; }
```

---

## Q5. What is the CSS Box Model and what are its components?

The CSS Box Model describes how elements are sized and spaced - it consists of content, padding, border, and margin, layers from inside to outside, understanding the box model is essential for layout. Content → Padding → Border → Margin (from inside to outside).

- **Trade-offs**: The catch is not understanding that padding and border add to total element size by default - use `box-sizing: border-box` for predictable layouts. Box model understanding is essential for precise layouts, but watch out - `box-sizing: border-box` includes padding and border in width/height.

Example:

```css
.element {
  width: 200px;        /* content width */
  padding: 20px;      /* space inside border */
  border: 2px solid black; /* border around padding */
  margin: 10px;        /* space outside border */
  background-color: lightgray;
}
```

---

## Q6. What is the difference between margin and padding?

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

## Q7. What is the purpose of the `box-sizing` property?

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

## Q8. What is the difference between `display: block`, `inline`, and `inline-block`?

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

## Q9. What are pseudo-classes and pseudo-elements? Give examples.

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

## Q10. What is the difference between `:hover` and `::before`?

`:hover` is a pseudo-class that targets an element's hover state, while `::before` is a pseudo-element that creates content before an element - pseudo-classes target states, pseudo-elements create new elements. `:hover` targets existing element in hover state, `::before` creates new virtual element.

- **Trade-offs**: The catch is `::before` requires `content` property to be visible - use pseudo-classes for states, pseudo-elements for generated content. Pseudo-classes target states, pseudo-elements create new elements, but watch out - pseudo-classes use single colon `:`, pseudo-elements use double colon `::`.

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
```

---

## Q11. What is CSS specificity and how is it calculated?

CSS specificity determines which styles apply when multiple rules target the same element - higher specificity wins, specificity is calculated based on selectors. Specificity: inline styles (1,0,0,0) > IDs (0,1,0,0) > classes (0,0,1,0) > elements (0,0,0,1).

- **Trade-offs**: The catch is not understanding specificity order, causing unexpected style overrides - use `!important` sparingly, prefer increasing specificity naturally. Specificity determines which styles win when rules conflict, but watch out - more specific selectors override less specific ones.

Example:

```css
p { color: black; }                    /* 0,0,0,1 */
.highlight { color: yellow; }          /* 0,0,1,0 */
#header { color: blue; }               /* 0,1,0,0 */
#header.highlight { color: red; }      /* 0,1,1,0 */
```

---

## Q12. What are relative and absolute CSS units?

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

## Q13. What is the difference between `position: relative`, `absolute`, `fixed`, and `sticky`?

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
