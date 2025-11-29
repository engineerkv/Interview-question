<div align="center">

**[← Previous: Beginner Level CSS](1%29%20Beginner%20Level%20CSS.md)** | **[Next: Advanced CSS Concepts →](3%29%20Advanced%20CSS%20Concepts.md)**

</div>

# 2. Intermediate Level CSS (Q13–32)

---

## Q13. `visibility: hidden` vs `display: none`

`visibility: hidden` hides elements but preserves their space, while `display: none` removes elements completely from the layout - visibility preserves space, display removes from layout. `visibility: hidden` (element invisible but space preserved), `display: none` (element completely removed from layout).

- **Trade-offs**: The catch is not understanding when to use each, causing layout shifts - use `visibility` for toggling without layout shift. Visibility preserves space, display removes from layout, but watch out - `visibility: hidden` can be animated, `display: none` cannot be animated.

Example:

```css
.hidden-visibility { visibility: hidden; }
.hidden-display { display: none; }
```

---

## Q14. `z-index` and stacking context

`z-index` controls the stacking order of positioned elements, with higher values appearing on top - z-index only works on positioned elements. Only works on positioned elements (relative, absolute, fixed), higher z-index values appear on top.

- **Trade-offs**: The catch is using z-index on non-positioned elements (doesn't work), z-index wars - use sparingly to avoid z-index wars, understand stacking contexts. z-index only works on positioned elements, but watch out - creates stacking contexts, negative z-index values are allowed.

Example:

```css
.layer1 { 
  position: relative; 
  z-index: 1; 
  background-color: red; 
}
.layer2 { 
  position: relative; 
  z-index: 2; 
  background-color: blue; 
}
```

---

## Q15. Default positioning value for HTML elements

The default positioning value for HTML elements is `static`, which follows the normal document flow - static positioning is the default, follows normal flow. `static` is the default positioning, static elements follow normal document flow.

- **Trade-offs**: The catch is not understanding that static is default, other positioning values create new stacking contexts - most elements use static positioning by default. Static positioning is the default, follows normal flow, but watch out - static elements ignore `top`, `right`, `bottom`, `left` properties.

Example:

```css
.element { position: static; }
.box { 
  width: 200px; 
  height: 100px; 
  background-color: blue; 
}
```

---

## Q16. Inheritance in CSS and inheritable properties

Inheritance means child elements automatically get some properties from their parents, like font-family or color - inherited properties are more efficient than explicitly setting them on every element. Inherited properties include `font-family`, `font-size`, `color`, `line-height`, `text-align`, `visibility`.

- **Trade-offs**: The catch is properties cascade down through the DOM tree from parent to child - child elements can override inherited properties with their own values. Inherited properties are more efficient than explicitly setting them on every element, but watch out - non-inherited properties include `width`, `height`, `margin`, `padding`, `border`, `background`.

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

## Q17. Vendor prefixes: what they are and why they're used

Vendor prefixes are browser-specific prefixes added to CSS properties during experimental or early implementation phases - vendor prefixes are for experimental features, standard property comes last. `-webkit-` (Chrome, Safari, newer Edge), `-moz-` (Firefox), `-ms-` (Internet Explorer, older Edge), `-o-` (Opera, legacy).

- **Trade-offs**: The catch is not including standard property, forgetting prefixes - use build tools like autoprefixer to handle prefixes automatically. Vendor prefixes are for experimental features, standard property comes last, but watch out - always include standard property last, use autoprefixer tools for automatic prefixing.

Example:

```css
.animation {
  -webkit-transform: rotate(45deg);
  -moz-transform: rotate(45deg);
  transform: rotate(45deg);
}
```

---

## Q18. Shorthand properties in CSS

Shorthand properties allow setting multiple related CSS properties in a single declaration - shorthand properties are more efficient but order matters. Reduces code size and improves readability, common shorthands: `margin`, `padding`, `border`, `background`.

- **Trade-offs**: The catch is not understanding shorthand order (top, right, bottom, left) - use shorthand for efficiency, longhand for clarity. Shorthand properties are more efficient but order matters, but watch out - order matters in shorthand properties, can mix shorthand and longhand properties.

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

## Q19. Applying multiple classes to an element

Separate multiple class names with spaces in the HTML class attribute - each class applies its styles independently, and specificity combines. Multiple classes combine their styles, order in HTML doesn't affect CSS.

- **Trade-offs**: The catch is CSS specificity is based on selector, not class order - combine utility classes for flexible, maintainable styling. Multiple classes enable modular, reusable styling patterns, but watch out - use multiple classes for modular, reusable styling patterns.

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

## Q20. CSS Flexbox: what it is and how it works

Flexbox helps you lay out items in one direction (row or column) with flexible sizing and easy alignment - use it when you need to distribute space or center content. Flexbox works on two axes—main (flex-direction) and cross (perpendicular).

- **Trade-offs**: The catch is `justify-content` controls main axis, `align-items` controls cross axis - `order` property allows visual reordering without changing HTML structure. Flexbox simplifies one-dimensional layouts and alignment, but watch out - `flex` is shorthand for `flex-grow`, `flex-shrink`, and `flex-basis`.

Example:

```css
.container {
  display: flex;
  justify-content: space-between;
  align-items: center;
  flex-wrap: wrap;
}
```

---

## Q21. CSS Grid: what it is and its key features

Grid allows you to create layouts with both rows and columns at once, giving you precise control over where items go - perfect for complex page layouts. Unlike Flexbox, Grid handles both rows and columns simultaneously.

- **Trade-offs**: The catch is `fr` units distribute available space proportionally - Grid can create implicit rows/columns when content exceeds defined tracks. Grid is perfect for complex two-dimensional layouts, but watch out - named grid areas make complex layouts more readable and maintainable.

Example:

```css
.grid-container {
  display: grid;
  grid-template-columns: repeat(3, 1fr);
  gap: 20px;
  grid-template-areas: 
    "header header header" 
    "sidebar content content" 
    "footer footer footer";
}
```

---

## Q22. Flexbox vs Grid

Grid handles 2D layouts (both rows and columns), while Flexbox handles 1D (row OR column) - use Grid for page structure and Flexbox for components. Grid for page layouts and complex two-dimensional arrangements, Flexbox for component layouts and navigation bars.

- **Trade-offs**: The catch is trying to use one for everything instead of combining both - both have excellent modern browser support, Grid is newer. Flexbox is simpler to learn, Grid is more powerful but complex, but watch out - use Grid for overall structure, Flexbox for component internals—they complement each other.

Example:

```css
.page-layout { 
  display: grid; 
  grid-template-columns: 200px 1fr 200px; 
  min-height: 100vh; 
}
.card { 
  display: flex; 
  justify-content: center; 
  align-items: center; 
}
```

---

## Q23. CSS transitions: what they are and how to use them

Transitions make property changes smooth over time instead of instant - great for hover effects and user feedback, different properties can have different durations and timing functions. Can target specific properties or use `all` for multiple properties.

- **Trade-offs**: The catch is GPU-accelerated properties (transform, opacity) perform better than layout properties - JavaScript can listen to `transitionend` events for completion callbacks. Transitions provide smooth property changes over time, but watch out - timing functions (`ease`, `linear`, `ease-in-out`) control animation curve.

Example:

```css
.button { 
  background-color: #007bff; 
  transition: all 0.3s ease-in-out; 
}
.button:hover { 
  background-color: #0056b3; 
  transform: scale(1.05); 
}
```

---

## Q24. CSS animations: what they are and how to create them

Animations let you create complex, multi-step effects using @keyframes to define what happens at different points - use them for loading spinners or page entrances. Multiple keyframes (0%, 25%, 50%, 100%) create complex animation sequences.

- **Trade-offs**: The catch is `forwards` keeps final state, `backwards` applies initial state before delay - use `transform` and `opacity` for smooth 60fps animations. Animation events allow JavaScript control of animations, but watch out - animation properties include duration, timing-function, delay, iteration-count, direction, fill-mode.

Example:

```css
@keyframes slideIn {
  0% { transform: translateX(-100%); opacity: 0; }
  100% { transform: translateX(0); opacity: 1; }
}
.element { animation: slideIn 0.5s ease-in-out; }
```

---

## Q25. CSS cascade: what it is and how it works

The cascade is CSS's priority system—it decides which styles win based on order, specificity, and !important - later styles override earlier ones when specificity is equal. Later styles override earlier ones when specificity is equal (source order).

- **Trade-offs**: The catch is `!important` has highest priority but breaks cascade flow - some properties inherit from parent elements automatically. Modern CSS supports `@layer` for explicit cascade control, but watch out - higher specificity overrides lower specificity.

Example:

```css
.button { color: red; }
.button { color: blue; }
.button { color: green !important; }
```

---

## Q26. CSS combinators: what they are and how to use them

Combinators let you target elements based on their relationship to other elements—like children, siblings, or descendants - useful for styling nested structures. Descendant (space) targets any descendant, child (>) targets only direct children.

- **Trade-offs**: The catch is child combinators are generally faster than descendant combinators - use combinators to avoid adding unnecessary classes. Combinators help maintain clean HTML structure, but watch out - adjacent sibling (+) targets immediately following sibling, general sibling (~) targets all following siblings.

Example:

```css
.container p { color: blue; }
.container > p { font-weight: bold; }
h1 + p { margin-top: 0; }
h2 ~ p { color: gray; }
```

---

## Q27. `transition` vs `animation`

Transitions animate property changes between states, while animations create complex multi-step sequences with @keyframes - transitions are simpler, animations are more powerful. Transitions need a trigger (hover, focus), animations can run automatically.

- **Trade-offs**: The catch is transitions are simpler, animations offer more control with keyframes - both can be paused, reversed, or controlled with JavaScript. Transitions are simpler, animations offer more control, but watch out - use transitions for simple state changes, animations for complex sequences.

Example:

```css
/* Transition */
.button { 
  transition: background-color 0.3s; 
}
.button:hover { 
  background-color: blue; 
}

/* Animation */
@keyframes bounce {
  0%, 100% { transform: translateY(0); }
  50% { transform: translateY(-20px); }
}
.element { 
  animation: bounce 1s infinite; 
}
```

---

## Q28. Creating CSS animations using `@keyframes`

Use `@keyframes` to define animation steps, then apply with the `animation` property - keyframes define what happens at different points in the animation. Define keyframes with percentages (0%, 50%, 100%) or keywords (from, to).

- **Trade-offs**: The catch is `infinite` makes animation repeat, `alternate` reverses direction - use `fill-mode: forwards` to keep final state after animation ends. @keyframes enable complex, multi-step animations, but watch out - animation shorthand: name, duration, timing-function, delay, iteration-count, direction, fill-mode.

Example:

```css
@keyframes slideIn {
  0% { transform: translateX(-100%); opacity: 0; }
  50% { opacity: 0.5; }
  100% { transform: translateX(0); opacity: 1; }
}
.element { 
  animation: slideIn 0.5s ease-in-out 0.2s infinite alternate; 
}
```

---

## Q29. Media queries: what they are and how to use them

Media queries let you apply different styles based on device features like screen width - essential for making websites work on phones, tablets, and desktops. Common breakpoints are 768px (tablet), 1024px (desktop), 1200px (large desktop).

- **Trade-offs**: The catch is logical operators (`and`, `or`, `not`) combine multiple media conditions - media queries don't affect performance, only load appropriate CSS. Media features include width, orientation, prefers-color-scheme, but watch out - start with mobile styles, then add larger screen styles with `min-width` (mobile-first).

Example:

```css
.container { width: 100%; padding: 10px; }
@media (min-width: 768px) {
  .container { width: 750px; padding: 20px; }
}
@media (min-width: 1024px) { 
  .container { width: 1200px; 
}
```

---

## Q30. Creating responsive text with CSS

Use relative units (rem, em), viewport units (vw, vh), or `clamp()` for responsive text that scales with screen size - responsive text improves readability across devices. `clamp()` sets min, preferred, and max values for fluid scaling.

- **Trade-offs**: The catch is avoid fixed pixel sizes for text, use relative units - combine media queries with relative units for best results. Responsive text improves readability across devices, but watch out - use rem for consistent scaling, vw for viewport-based sizing.

Example:

```css
h1 { 
  font-size: clamp(1.5rem, 4vw, 3rem); 
}
p { 
  font-size: 1rem; 
  line-height: 1.6; 
}
@media (min-width: 768px) {
  p { font-size: 1.125rem; }
}
```

---

## Q31. CSS variables (custom properties): what they are, how to use them, and their role in design systems

CSS variables let you store values like colors or spacing that you can reuse anywhere and even change with JavaScript - perfect for theming and maintaining consistent design tokens. Variables inherit and can be overridden at different levels (root, element, pseudo-class).

- **Trade-offs**: The catch is JavaScript can change CSS variables: `element.style.setProperty('--color', 'red')` - variables are computed at runtime, use sparingly for performance-critical properties. CSS variables enable dynamic theming and design tokens, but watch out - `var(--color, #fallback)` provides fallback when variable is undefined.

Example:

```css
:root {
  --primary-color: #007bff;
  --secondary-color: #6c757d;
  --border-radius: 4px;
  --spacing-unit: 8px;
}
.button {
  background-color: var(--primary-color);
  padding: var(--spacing-unit);
  border-radius: var(--border-radius);
}
```

---

## Q32. SASS vs LESS

SASS and LESS are CSS preprocessors that add features like variables and mixins - SASS uses indentation or SCSS syntax, LESS uses CSS-like syntax, both compile to CSS. SASS has two syntaxes (indented SASS, SCSS), LESS uses CSS-like syntax.

- **Trade-offs**: The catch is SASS is more popular, LESS is easier for CSS developers - choose based on team preference and tooling support. Both preprocessors add power to CSS, choose based on preference, but watch out - both support variables, mixins, nesting, and functions.

Example:

```scss
// SASS/SCSS
$primary-color: #007bff;
@mixin button-style {
  padding: 10px 20px;
  background-color: $primary-color;
}
```

```less
// LESS
@primary-color: #007bff;
.button-style() {
  padding: 10px 20px;
  background-color: @primary-color;
}
```

---
