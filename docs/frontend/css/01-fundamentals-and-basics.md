---
sidebar_label: "Fundamentals & Basics"
---
# 🧒 1. Fundamentals & Basics (Q1–12, Q16–19, Q25–26)
> **Reviewed:** 2026-09 · Modernized; legacy topics are labeled.

---

## Q1. 🎨 CSS and what it stands for

CSS stands for Cascading Style Sheets - it's a stylesheet language that describes how HTML documents look, separating content from presentation for maintainable styling. It enables consistent styling across web pages and works with HTML, XML, and other markup languages.

- **Trade-offs**: The catch is mixing content and presentation makes code harder to maintain - use external stylesheets for reusability and caching. CSS enables maintainable, scalable styling and supports responsive design, animations, and modern web development.

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

CSS can be included via inline styles, internal stylesheets, or external stylesheet files - external stylesheets are preferred for production websites because you can cache and reuse them. Inline has highest specificity, internal is page-specific, external is best for reusability.

- **Trade-offs**: The catch is overusing inline styles makes code hard to maintain - use external CSS for maintainability and caching. External stylesheets can be cached by browsers, which improves performance for production sites.

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

CSS selectors target HTML elements to apply styles, using various patterns to match elements - selector specificity determines which styles apply when multiple rules match. More specific selectors override less specific ones.

- **Trade-offs**: The catch is IDs should be unique per page, so don't overuse them for styling - use classes for styling and IDs for JavaScript targeting. Combine selectors for precise targeting, and use classes for reusable styles.

Example:

```css
p { color: blue; }
.highlight { background-color: yellow; }
#header { font-size: 24px; }
div p { margin: 10px; }

```

---

## Q4. 🏛️ Element, class, and ID selectors: differences

Element selectors target HTML tags, class selectors target elements with specific class attributes, and ID selectors target unique elements - classes are preferred for styling, IDs for JavaScript hooks. Element provides broad targeting, class is reusable, ID is unique with highest specificity.

- **Trade-offs**: The catch is using IDs for styling makes styles hard to override - use classes for reusable styles and IDs for JavaScript targeting. Specificity order is ID > Class > Element, so use classes for styling to keep specificity manageable.

Example:

```css
p { color: black; }
.highlight { background-color: yellow; }
#header { font-size: 24px; }

```

---

## Q5. 🧩 CSS Box Model and its components

The CSS Box Model defines how every HTML element is structured with four layers: content (inside), padding (space inside), border (line), and margin (space outside). Understanding the box model is crucial for creating precise layouts and avoiding unexpected sizing issues.

- **Trade-offs**: The catch is `content-box` (default) adds padding and border to width/height, causing overflow issues - use `border-box` globally for predictable sizing. Margin collapses vertically between adjacent elements, padding shows background color, and margin is transparent.

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

Margin creates space outside an element's border, while padding creates space inside an element's border - padding is inside the border and affects background color, margin is outside and transparent. Margin can collapse vertically between adjacent elements.

- **Trade-offs**: The catch is not understanding margin collapse can cause unexpected spacing - use padding for internal spacing and margin for external spacing. Padding increases element size, while margin doesn't affect element size.

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

`box-sizing` controls how the total width and height of an element is calculated, including or excluding padding and borders - `content-box` (default) sets width/height to content only, `border-box` includes padding and border. Border-box is preferred for predictable layouts.

- **Trade-offs**: The catch is not using border-box causes layout issues with padding - use `* { box-sizing: border-box; }` for consistent behavior. Modern CSS frameworks use border-box by default because it makes layouts more predictable.

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

These display values control how elements flow and interact with other elements on the page - block takes full width and starts on a new line, inline flows with text and ignores width/height, inline-block flows like inline but respects all properties. Inline-block is useful for buttons and form elements because it combines the best of both.

- **Trade-offs**: The catch is inline elements ignore width/height and only horizontal margins work - inline-block is the best of both, flowing like inline but respecting all properties. Use block for major layout elements and inline-block for buttons and form elements.

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

Pseudo-classes target element states (like `:hover`), while pseudo-elements create virtual elements (like `::before`) - pseudo-classes use single colon `:`, pseudo-elements use double colon `::`. Pseudo-classes target states, pseudo-elements create new elements.

- **Trade-offs**: The catch is `::before` requires `content` property to be visible - use pseudo-classes for states like `:hover` and `:focus`, pseudo-elements for generated content like `::before` and `::after`.

- **Modern pseudo-classes worth naming**: `:focus-visible` (keyboard focus rings without mouse rings), `:focus-within`, `:user-invalid` / `:user-valid` (validation styles only after the user interacts), `:is()` / `:where()` (group selectors), `:not()` with selector lists, and `:has()` (the "parent/relational" selector — see Q34 in [Modern CSS Features](./03-modern-css-features.md)). Newer pseudo-elements include `::backdrop` (for `<dialog>`/popovers), `::marker`, and `::view-transition-*`.

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

- **Trade-offs**: The catch is overusing IDs makes styles hard to override and creates maintenance issues - use classes over IDs and keep specificity low. Inline styles (1,0,0,0) have highest specificity, IDs (0,1,0,0) beat classes (0,0,1,0) - `!important` overrides all specificity, and combinators don't add specificity.

Example:

```css
p { color: black; }              /* 0,0,0,1 */
.highlight { color: yellow; }    /* 0,0,1,0 - wins */
#header { color: blue; }         /* 0,1,0,0 - wins over class */

:is(#header, .nav) a { }         /* :is() takes the specificity of its MOST specific argument (the ID) */
:where(#header, .nav) a { }      /* :where() always adds 0 — great for resettable library defaults */
```

- **Modern nuances**: `:is()`, `:not()`, and `:has()` take the specificity of their most specific argument; `:where()` is always zero. **Cascade layers (`@layer`) are checked before specificity**, so a low-specificity rule in a later layer beats a high-specificity rule in an earlier layer — which is why layers are the modern alternative to specificity wars and `!important`. See Q35 in [Modern CSS Features](./03-modern-css-features.md).

---

## Q11. 🎨 Relative vs absolute CSS units

Relative units scale based on context (em, rem, %, vw, vh), while absolute units are fixed (px, pt, cm) - relative units are better for responsive design because they adapt to different screen sizes. Rem is relative to root font-size; em is relative to the element's own font-size (or the parent's font-size when used on `font-size` itself).

- **Trade-offs**: The catch is mixing absolute and relative units inconsistently can cause layout issues - use rem for font sizes, vw/vh for viewport-based sizing, and % for responsive layouts.

- **Modern units (Baseline)**:
  - **`dvh` / `svh` / `lvh`** – dynamic/small/large viewport height. `100vh` on mobile is taller than the visible area when the browser toolbar is shown; `100dvh` tracks the actual visible viewport, `100svh` is the safe minimum.
  - **Container query units** `cqi`, `cqb`, `cqw`, `cqh` – relative to the nearest size container (see Q33).
  - **`ch`** / **`lh`** – width of "0" (great for `max-width: 65ch` readable line length) / the element's line height.
  - `px` in CSS is a reference pixel, not a physical device pixel.

Example:

```css
.container {
  font-size: 16px;           /* absolute */
  padding: 1em;              /* relative to font-size */
  width: 50%;                /* relative to parent */
  height: 100vh;             /* relative to viewport */
  min-height: 100dvh;        /* tracks mobile browser UI showing/hiding */
}
.prose { max-width: 65ch; }

```

---

## Q12. 🤔 `position: relative`, `absolute`, `fixed`, and `sticky`: differences

Positioning controls how elements are placed - `relative` positions relative to itself, `absolute` to nearest positioned parent, `fixed` to viewport, `sticky` toggles between relative and fixed. Understanding positioning is key to complex layouts.

- **Trade-offs**: The catch is `absolute` positions relative to nearest positioned ancestor, not always the parent - `sticky` needs a threshold (top/bottom) and works within parent container. Use `absolute` for overlays, `fixed` for headers/footers, and `sticky` for scroll effects. Common gotcha: `sticky` silently fails if any ancestor has `overflow: hidden`/`auto`, and `fixed` becomes relative to an ancestor that has `transform`, `filter`, or `contain: paint`.

- **2026 notes**: use the logical shorthand `inset: 0` instead of `top/right/bottom/left: 0`. For tooltips and popovers, **CSS anchor positioning** (`anchor-name`, `position-anchor`, `position-area`) tethers an element to another without JavaScript — it shipped in Chromium first and is still reaching other engines, so treat it as emerging and keep a JS fallback (e.g. Floating UI). Top-layer elements (`<dialog>`, popovers) also avoid `z-index` battles entirely.

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

## Q16. 🧬 Inheritance in CSS and inheritable properties

Inheritance means child elements automatically get some properties from their parents, like font-family or color - inherited properties are more efficient than explicitly setting them on every element. Inherited properties include `font-family`, `font-size`, `color`, `line-height`, `text-align`, and `visibility`.

- **Trade-offs**: The catch is properties cascade down through the DOM tree from parent to child - child elements can override inherited properties with their own values. Non-inherited properties include `width`, `height`, `margin`, `padding`, `border`, and `background`.

Example:

```css
body {
  font-family: 'Arial', sans-serif;
  font-size: 16px;
  line-height: 1.5;
  color: #333;
}

```

---

## Q17. ❓ Vendor prefixes and why they're used

Vendor prefixes are browser-specific prefixes added to CSS properties during experimental or early implementation phases - vendor prefixes are for experimental features, standard property comes last. Common prefixes include `-webkit-` (Chrome, Safari, newer Edge), `-moz-` (Firefox), `-ms-` (Internet Explorer, older Edge), and `-o-` (Opera, legacy).

- **Trade-offs**: The catch is not including standard property or forgetting prefixes - use build tools like autoprefixer to handle prefixes automatically. Always include standard property last, and use autoprefixer tools for automatic prefixing.

> **Legacy note (2026):** Browsers stopped shipping new experimental features behind vendor prefixes years ago; new features ship behind **flags** or origin trials and are unprefixed when released. `-ms-` and `-o-` prefixes are only relevant for dead browsers (IE, Presto Opera). You'll still see a few `-webkit-` ones (e.g. `-webkit-line-clamp`, `-webkit-text-stroke`, some `backdrop-filter` in older Safari). Don't hand-write prefixes: let Autoprefixer or **Lightning CSS** add only what your `browserslist` targets need. Check support on [MDN](https://developer.mozilla.org/) or "Baseline" status.

Example:

```css
/* Legacy hand-prefixed code — unnecessary today, transform has been unprefixed for years */
.animation {
  -webkit-transform: rotate(45deg);
  -moz-transform: rotate(45deg);
  transform: rotate(45deg);
}

/* Still-common prefixed case */
.clamp {
  display: -webkit-box;
  -webkit-box-orient: vertical;
  -webkit-line-clamp: 3;
  overflow: hidden;
}

```

---

## Q18. 🎨 Shorthand properties in CSS

Shorthand properties allow setting multiple related CSS properties in a single declaration - shorthand properties are more efficient but order matters. Common shorthands include `margin`, `padding`, `border`, and `background`, which reduce code size and improve readability.

- **Trade-offs**: The catch is not understanding shorthand order (top, right, bottom, left) - use shorthand for efficiency and longhand for clarity. You can mix shorthand and longhand properties as needed.

Example:

```css
.element {
  margin-top: 10px;
  margin-right: 20px;
  margin-bottom: 10px;
  margin-left: 20px;
}
.element { margin: 10px 20px; }

```

---

## Q19. 🏛️ Applying multiple classes to an element

Separate multiple class names with spaces in the HTML class attribute - each class applies its styles independently, and specificity combines. Multiple classes combine their styles, and order in HTML doesn't affect CSS.

- **Trade-offs**: The catch is CSS specificity is based on selector, not class order - combine utility classes for flexible, maintainable styling. Multiple classes enable modular, reusable styling patterns.

Example:

```html
<div class="button primary large">Click me</div>

```

```css
.button { padding: 10px; }
.primary { background-color: blue; }
.large { font-size: 18px; }

```

---

## Q25. 🎨 CSS cascade and how it works

The cascade is CSS's priority system—it decides which styles win based on order, specificity, and !important - later styles override earlier ones when specificity is equal (source order). Some properties inherit from parent elements automatically.

- **Trade-offs**: The catch is `!important` has highest priority but breaks cascade flow - modern CSS supports `@layer` for explicit cascade control. Higher specificity overrides lower specificity.

- **Full cascade order (what the spec actually checks, in order)**:
  1. **Origin and importance** – user-agent, user, and author styles; `!important` flips the origin order
  2. **Context** – Shadow DOM encapsulation (outer vs inner context)
  3. **Element-attached styles** – inline `style=""`
  4. **Cascade layers** – `@layer` order (unlayered author styles beat all layered ones for normal declarations)
  5. **Specificity**
  6. **Scope proximity** – with `@scope`, the closer scope root wins (newer feature)
  7. **Order of appearance** – last one wins

Example:

```css
.button { color: red; }
.button { color: blue; }
.button { color: green !important; }

@layer reset, base, components, utilities;
@layer components { .button { color: navy; } }
@layer utilities { .text-red { color: red; } } /* beats .button in components, regardless of specificity */

```

---

## Q26. 🎨 CSS combinators and how to use them

Combinators let you target elements based on their relationship to other elements—like children, siblings, or descendants - useful for styling nested structures without adding extra classes. There are four types: descendant (space) targets any nested element at any level, child (>) targets only direct children, adjacent sibling (+) targets the immediately following sibling, and general sibling (~) targets all following siblings.

- **Trade-offs**: The catch is child combinators are generally faster than descendant combinators because they don't need to search through all descendants - use combinators to avoid adding unnecessary classes and keep HTML clean. Descendant selectors are more flexible but slower, child selectors are faster but more restrictive - adjacent sibling is useful for styling the first element after another, general sibling is useful for styling multiple following elements.

- **Reality check (2026)**: in modern engines, selector-matching cost is rarely the bottleneck for typical pages — layout, large DOMs, and JS are. Choose combinators for **maintainability** (low specificity, less coupling to DOM structure), and measure with DevTools' selector stats only if style recalculation shows up in profiles. Combinators can now also be used inside `:has()` to look *forward/down*: `h2:has(+ p)` styles an `h2` that is followed by a `p`.

Example:

```css
/* Descendant - targets all p inside .container at any level */
.container p { color: blue; }

/* Child - targets only direct p children of .container */
.container > p { font-weight: bold; }

/* Adjacent sibling - targets p immediately after h1 */
h1 + p { margin-top: 0; }

/* General sibling - targets all p elements after h2 */
h2 ~ p { color: gray; }
```

---

