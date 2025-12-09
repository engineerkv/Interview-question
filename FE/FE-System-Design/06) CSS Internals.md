# 🎨 CSS Internals

---

## 📍 Navigation

<div align="center">

[← Previous: HTML Internals](05%29%20HTML%20Internals.md) • [Home: Questions Index](question.md) • [Next: JavaScript Internals →](07%29%20JavaScript%20Internals.md)

[📋 Cheatsheet](FE-System-Design%20Interview%20Cheatsheet.md)

</div>

---

## Q8.6. How CSS Works Internally

CSS (Cascading Style Sheets) is the language for styling web pages. Understanding how CSS works under the hood helps you write better styles, debug layout issues, and optimize performance. When browsers process CSS, they handle parsing, cascade resolution, specificity calculation, layout computation, and rendering. This knowledge is crucial for senior developers - it helps you understand why certain CSS patterns work better, how to optimize CSS for performance, and how browsers interpret your styles.

---

## 1. CSS Parsing Process

### 🔹 Tokenization

The first step in CSS parsing is breaking CSS source into tokens:

**What is Tokenization:**
* Reads CSS character by character
* Identifies selectors, properties, values, at-rules
* Handles whitespace, comments, and special characters
* Produces stream of tokens for parser

**Token Types:**
* **Identifiers**: Property names, values (`color`, `red`)
* **Strings**: Quoted values (`"Arial"`, `'sans-serif'`)
* **Numbers**: Numeric values (`100`, `3.14`, `50%`)
* **Delimiters**: `{`, `}`, `:`, `;`, `,`
* **Whitespace**: Spaces, tabs, newlines (mostly ignored)
* **Comments**: `/* comment */` (removed during parsing)
* **At-keywords**: `@media`, `@keyframes`, `@import`

**Example:**
```css
.container {
  color: red;
  font-size: 16px;
}
```

Tokens produced:
1. Identifier: `.container`
2. Delimiter: `{`
3. Identifier: `color`
4. Delimiter: `:`
5. Identifier: `red`
6. Delimiter: `;`
7. Identifier: `font-size`
8. Delimiter: `:`
9. Number: `16`
10. Identifier: `px`
11. Delimiter: `;`
12. Delimiter: `}`

**Error Handling:**
* Invalid properties are ignored
* Malformed selectors cause rule to be dropped
* Invalid values fall back to initial or inherit
* Browsers are forgiving (skip invalid rules)

### 🔹 Parsing and Rule Construction

After tokenization, tokens are converted into CSS rules:

**How Parsing Works:**
* Groups tokens into rules
* Identifies selectors and declarations
* Builds rule objects with selector and properties
* Handles at-rules (`@media`, `@keyframes`, etc.)

**Rule Structure:**
* **Selector**: Which elements the rule applies to
* **Declarations**: Property-value pairs
* **Specificity**: Calculated from selector
* **Source**: Origin (author, user, user-agent)

**Example:**
```css
.container p {
  color: blue;
  margin: 10px;
}
```

Parsed rule:
* Selector: `.container p`
* Declarations:
  * `color: blue`
  * `margin: 10px`
* Specificity: (0, 1, 1) - class + element

**At-Rules:**
* `@media`: Media queries
* `@keyframes`: Animations
* `@import`: Import other stylesheets
* `@font-face`: Font definitions
* `@supports`: Feature queries

### 🔹 CSSOM Construction

The browser builds a CSSOM (CSS Object Model) tree:

**CSSOM Structure:**
* Tree representing CSS rules
* Similar to DOM but for styles
* Represents cascade and inheritance
* Used to compute final styles

**How CSSOM is Built:**
* Rules are added to CSSOM in order
* Specificity is calculated for each rule
* Cascade order is determined
* Inheritance relationships are established

**CSSOM vs DOM:**
* DOM: Structure of HTML elements
* CSSOM: Structure of CSS rules
* Combined to create render tree

📌 **In simple terms**: CSS parsing breaks source into tokens, then builds rules with selectors and declarations. The browser constructs a CSSOM tree representing all CSS rules, which is used to compute final styles for elements.

---

## 2. Cascade and Specificity

### 🔹 Cascade Order

The cascade determines which styles apply when multiple rules target the same element:

**Cascade Layers (Priority Order):**
1. **User-agent styles**: Browser defaults (lowest priority)
2. **User styles**: User preferences (medium priority)
3. **Author styles**: Your CSS (highest priority)
4. **Important declarations**: `!important` (overrides all)

**Within Same Origin:**
* Later rules override earlier ones (if specificity is equal)
* Source order matters
* More specific selectors win

**Example:**
```css
/* Rule 1 */
p { color: red; }

/* Rule 2 - wins (same specificity, later) */
p { color: blue; }

/* Rule 3 - wins (higher specificity) */
.container p { color: green; }
```

### 🔹 Specificity Calculation

Specificity determines which rule wins when multiple rules apply:

**Specificity Formula:**
* (a, b, c, d)
* a: Inline styles (always wins)
* b: ID selectors
* c: Class, attribute, pseudo-class selectors
* d: Element, pseudo-element selectors

**Specificity Examples:**
* `p`: (0, 0, 0, 1) - 1 element
* `.container`: (0, 0, 1, 0) - 1 class
* `#header`: (0, 1, 0, 0) - 1 ID
* `.container p`: (0, 0, 1, 1) - 1 class + 1 element
* `#header .nav a:hover`: (0, 1, 2, 1) - 1 ID + 2 classes + 1 element + 1 pseudo-class
* `style="color: red"`: (1, 0, 0, 0) - inline style

**Specificity Rules:**
* Higher specificity wins
* If specificity is equal, later rule wins
* `!important` overrides specificity
* Universal selector (`*`) has no specificity

**Example:**
```css
/* Specificity: (0, 0, 0, 1) */
p { color: red; }

/* Specificity: (0, 0, 1, 1) - wins */
.container p { color: blue; }

/* Specificity: (0, 1, 0, 0) - wins */
#header { color: green; }

/* Specificity: (0, 0, 1, 1) but !important - wins */
.container p { color: yellow !important; }
```

### 🔹 Inheritance

Some CSS properties are inherited by child elements:

**Inherited Properties:**
* `color`, `font-family`, `font-size`
* `line-height`, `text-align`
* `visibility`, `cursor`

**Non-Inherited Properties:**
* `margin`, `padding`, `border`
* `width`, `height`, `background`
* `display`, `position`

**How Inheritance Works:**
* Child elements inherit computed values from parents
* Can override inherited values
* `inherit` keyword explicitly inherits
* `initial` resets to initial value

**Example:**
```css
body {
  color: blue;
  font-family: Arial;
  margin: 0; /* Not inherited */
}

p {
  /* Inherits color and font-family */
  /* margin is not inherited, uses initial value */
}
```

📌 **In simple terms**: The cascade determines which styles apply based on origin and source order. Specificity calculates selector weight (IDs > classes > elements). Some properties inherit from parents, others don't.

---

## 3. Layout Systems

### 🔹 Box Model

Every element is a rectangular box with specific areas:

**Box Model Components:**
* **Content**: Actual content (text, images)
* **Padding**: Space inside border
* **Border**: Border around padding
* **Margin**: Space outside border

**Box Sizing:**
* `content-box` (default): Width/height = content only
* `border-box`: Width/height = content + padding + border

**Example:**
```css
.box {
  width: 200px;
  padding: 20px;
  border: 5px solid black;
  margin: 10px;
  box-sizing: content-box; /* Total width: 200 + 40 + 10 + 20 = 270px */
}

.box-border {
  box-sizing: border-box; /* Total width: 200px (includes padding + border) */
}
```

### 🔹 Normal Flow

Default layout algorithm (block and inline):

**Block Elements:**
* Stack vertically
* Take full width of container
* Respect margin collapsing
* Examples: `<div>`, `<p>`, `<h1>`

**Inline Elements:**
* Flow horizontally
* Only take needed width
* Don't respect top/bottom margins
* Examples: `<span>`, `<a>`, `<strong>`

**Inline-Block:**
* Flows horizontally like inline
* Respects width/height like block
* Useful for horizontal layouts

### 🔹 Flexbox

Flexbox provides flexible one-dimensional layouts:

**Flex Container:**
* `display: flex` creates flex container
* Children become flex items
* Main axis and cross axis

**Flex Properties:**
* `flex-direction`: Row (default) or column
* `justify-content`: Alignment on main axis
* `align-items`: Alignment on cross axis
* `flex-wrap`: Wrap items to new line
* `gap`: Space between items

**Flex Items:**
* `flex-grow`: How much item grows
* `flex-shrink`: How much item shrinks
* `flex-basis`: Initial size before growing/shrinking
* `flex`: Shorthand for grow, shrink, basis
* `align-self`: Override container alignment

**Example:**
```css
.container {
  display: flex;
  justify-content: space-between;
  align-items: center;
  gap: 20px;
}

.item {
  flex: 1; /* grow: 1, shrink: 1, basis: 0 */
}
```

**How Flexbox Works:**
* Calculates available space
* Distributes space based on flex values
* Aligns items on main and cross axes
* Handles wrapping and alignment

### 🔹 CSS Grid

Grid provides two-dimensional layouts:

**Grid Container:**
* `display: grid` creates grid container
* Defines rows and columns
* Children become grid items

**Grid Properties:**
* `grid-template-columns`: Define columns
* `grid-template-rows`: Define rows
* `grid-template-areas`: Named grid areas
* `gap`: Space between grid items
* `justify-items`: Horizontal alignment
* `align-items`: Vertical alignment

**Grid Items:**
* `grid-column`: Column placement
* `grid-row`: Row placement
* `grid-area`: Area placement
* `justify-self`: Override horizontal alignment
* `align-self`: Override vertical alignment

**Example:**
```css
.container {
  display: grid;
  grid-template-columns: 1fr 2fr 1fr;
  grid-template-rows: auto 1fr auto;
  gap: 20px;
}

.header {
  grid-column: 1 / -1; /* Span all columns */
}

.sidebar {
  grid-row: 2;
}
```

**How Grid Works:**
* Creates explicit grid lines
* Places items in grid cells
* Handles implicit tracks (auto-created)
* Aligns items within cells

### 🔹 Positioning

Positioning controls element placement:

**Position Values:**
* `static` (default): Normal flow
* `relative`: Offset from normal position
* `absolute`: Positioned relative to nearest positioned ancestor
* `fixed`: Positioned relative to viewport
* `sticky`: Switches between relative and fixed

**Positioning Properties:**
* `top`, `right`, `bottom`, `left`: Offsets
* `z-index`: Stacking order

**Example:**
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
  width: 100%;
}
```

📌 **In simple terms**: Box model defines content, padding, border, margin. Normal flow stacks blocks vertically. Flexbox creates flexible one-dimensional layouts. Grid creates two-dimensional layouts. Positioning removes elements from normal flow.

---

## 4. Rendering Pipeline

### 🔹 Style Calculation

Browsers calculate computed styles for each element:

**Process:**
1. Collect all rules matching element
2. Resolve cascade (origin, specificity, order)
3. Apply inheritance
4. Calculate computed values
5. Store in computed style object

**Computed Values:**
* Resolved values (percentages → pixels)
* Inherited values applied
* Default values for missing properties
* Used for layout and painting

**Example:**
```css
.container {
  font-size: 16px;
  width: 50%;
}

.item {
  font-size: 1.5em; /* Computed: 24px (1.5 × 16px) */
  width: 100px; /* Computed: 100px */
}
```

### 🔹 Layout (Reflow)

Layout calculates position and size of elements:

**Layout Process:**
1. Calculate width/height of each element
2. Determine position of each element
3. Handle floats and positioning
4. Calculate margins and padding
5. Build layout tree

**What Triggers Layout:**
* DOM changes (add/remove elements)
* Style changes (width, height, position)
* Window resize
* Font loading
* Content changes (text, images)

**Layout Performance:**
* Layout is expensive (recalculates positions)
* Minimize layout triggers
* Use `transform` and `opacity` (don't trigger layout)
* Batch DOM reads/writes

### 🔹 Paint

Paint fills pixels with colors and images:

**Paint Process:**
1. Create paint layers
2. Fill backgrounds
3. Draw borders
4. Render text
5. Paint images
6. Apply effects (shadows, gradients)

**Paint Layers:**
* Elements with `transform`, `opacity`, `filter` get own layer
* Layers are composited together
* Enables hardware acceleration
* Improves performance

**What Triggers Paint:**
* Style changes (color, background, border)
* Layout changes (triggers repaint)
* Visibility changes

### 🔹 Composite

Composite combines paint layers:

**Compositing Process:**
1. Combine paint layers
2. Apply transforms and opacity
3. Handle z-index stacking
4. Output final pixels to screen

**GPU Acceleration:**
* Transforms and opacity use GPU
* Faster than CPU painting
* Enables smooth animations
* Reduces main thread load

**Composite-Only Properties:**
* `transform`
* `opacity`
* `filter` (some browsers)
* Don't trigger layout or paint

📌 **In simple terms**: Style calculation resolves cascade and computes values. Layout calculates positions and sizes. Paint fills pixels. Composite combines layers. Optimize by minimizing layout/paint triggers and using composite-only properties.

---

## 5. Performance Optimization

### 🔹 CSS Performance Techniques

Optimize CSS for better performance:

**Minification:**
* Remove whitespace and comments
* Reduce file size
* Faster download and parsing

**Critical CSS:**
* Inline above-the-fold CSS
* Defer non-critical CSS
* Improves First Contentful Paint

**Avoid Expensive Selectors:**
* Avoid deep descendant selectors
* Avoid universal selector (`*`)
* Use classes instead of complex selectors

**Use Efficient Properties:**
* Prefer `transform` over `top/left`
* Prefer `opacity` over `visibility`
* Use `will-change` for animations

**Example:**
```css
/* Slow: Deep descendant */
div div div p { color: red; }

/* Fast: Class selector */
.text { color: red; }

/* Slow: Triggers layout */
.element {
  top: 100px;
  left: 100px;
}

/* Fast: Composite only */
.element {
  transform: translate(100px, 100px);
}
```

### 🔹 Render-Blocking CSS

CSS blocks rendering until parsed:

**Why CSS Blocks:**
* Prevents Flash of Unstyled Content (FOUC)
* Browser needs styles before painting
* All CSS must be parsed before first paint

**Optimization Strategies:**
* Inline critical CSS
* Defer non-critical CSS
* Use `media` attribute for conditional loading
* Split CSS into multiple files

**Example:**
```html
<!-- Critical CSS inline -->
<style>
  /* Above-the-fold styles */
</style>

<!-- Non-critical CSS deferred -->
<link rel="preload" href="styles.css" as="style" onload="this.onload=null;this.rel='stylesheet'">
```

### 🔹 CSS Animations

Optimize animations for smooth performance:

**Use Transform and Opacity:**
* These properties use GPU
* Don't trigger layout or paint
* Smooth 60fps animations

**Avoid Layout-Triggering Properties:**
* `width`, `height`, `top`, `left`
* `margin`, `padding`
* Trigger expensive layout calculations

**Use `will-change`:**
* Hints browser to optimize
* Use sparingly (has cost)
* Remove when animation ends

**Example:**
```css
/* Good: GPU-accelerated */
@keyframes slide {
  from { transform: translateX(0); }
  to { transform: translateX(100px); }
}

/* Bad: Triggers layout */
@keyframes slide {
  from { left: 0; }
  to { left: 100px; }
}
```

📌 **In simple terms**: Minify CSS, inline critical CSS, avoid expensive selectors, use transform/opacity for animations, and defer non-critical CSS to improve performance.

---

## ⭐ Summary — Key Takeaways

**CSS Parsing:**
* Tokenization breaks CSS into tokens
* Parsing builds rules with selectors and declarations
* CSSOM tree represents all CSS rules

**Cascade and Specificity:**
* Cascade determines which styles apply
* Specificity calculates selector weight
* Inheritance passes some properties to children

**Layout Systems:**
* Box model: content, padding, border, margin
* Flexbox: One-dimensional flexible layouts
* Grid: Two-dimensional layouts
* Positioning: Removes from normal flow

**Rendering Pipeline:**
* Style calculation: Resolves cascade and computes values
* Layout: Calculates positions and sizes
* Paint: Fills pixels
* Composite: Combines layers

**Performance:**
* Minify CSS
* Inline critical CSS
* Use transform/opacity for animations
* Avoid expensive selectors

---

## 📍 Navigation

<div align="center">

[← Previous: HTML Internals](05%29%20HTML%20Internals.md) • [Home: Questions Index](question.md) • [Next: JavaScript Internals →](07%29%20JavaScript%20Internals.md)

[📋 Cheatsheet](FE-System-Design%20Interview%20Cheatsheet.md)

</div>

---

