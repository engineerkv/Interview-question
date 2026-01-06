# 🎯 2. Layout & Styling (Q13–15, Q20–24, Q27–32, Q36, Q40)

---

## 📍 Navigation

<div align="center">

[← Previous: Fundamentals & Basics](01%29%20Fundamentals%20%26%20Basics.md) • [Home: README](../README.md) • [Next: Architecture & Design Systems →](04%29%20Architecture%20%26%20Design%20Systems.md)

[📋 Cheatsheet](CSS%20Interview%20Cheatsheet.md)

</div>

---

---

## Q13. 🤔 `visibility: hidden` vs `display: none`

`visibility: hidden` hides elements but preserves their space, while `display: none` removes elements completely from the layout - visibility preserves space, display removes from layout. Element is invisible but space is preserved with `visibility: hidden`, element is completely removed from layout with `display: none`.

- **Trade-offs**: The catch is not understanding when to use each can cause layout shifts - use `visibility` for toggling without layout shift. `visibility: hidden` can be animated, but `display: none` cannot be animated.

Example:

```css
.hidden-visibility { visibility: hidden; }
.hidden-display { display: none; }

```

---

## Q14. 📇 `z-index` and stacking context

`z-index` controls the stacking order of positioned elements, with higher values appearing on top - z-index only works on positioned elements (relative, absolute, fixed). Higher z-index values appear on top.

- **Trade-offs**: The catch is using z-index on non-positioned elements doesn't work, and z-index wars can make code hard to maintain - use sparingly to avoid z-index wars and understand stacking contexts. Z-index creates stacking contexts, and negative z-index values are allowed.

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

## Q15. 📄 Default positioning value for HTML elements

The default positioning value for HTML elements is `static`, which follows the normal document flow - most elements use static positioning by default. Static elements follow normal document flow.

- **Trade-offs**: The catch is not understanding that static is default - other positioning values create new stacking contexts. Static elements ignore `top`, `right`, `bottom`, and `left` properties.

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

## Q20. 🎨 CSS Flexbox and how it works

Flexbox is a one-dimensional layout system for arranging items in rows or columns - use `justify-content` for main axis alignment and `align-items` for cross axis alignment. Perfect for component layouts, navigation bars, and centering content.

- **Trade-offs**: The catch is confusing `justify-content` (main axis) with `align-items` (cross axis), and forgetting `flex-wrap` causes overflow - use `flex: 1` shorthand for equal distribution. Flexbox is one-dimensional (row OR column), Grid is two-dimensional - `flex-grow` controls growth, `flex-shrink` controls shrinking, `flex-basis` sets initial size before growing/shrinking.

Example:

```css
.container {
  display: flex;
  justify-content: center;
  align-items: center;
  gap: 1rem;
}
.item {
  flex: 1;
}
```

---

## Q21. 🎨 CSS Grid and its key features

CSS Grid is a two-dimensional layout system for creating complex layouts with rows and columns simultaneously - use `grid-template-columns` and `grid-template-rows` to define tracks, `gap` for spacing. Perfect for page-level layouts, dashboards, and complex two-dimensional arrangements.

- **Trade-offs**: The catch is forgetting to define tracks causes items to stack in single column, and confusing `fr` (fraction) with `%` units - use `fr` units for flexible sizing and `minmax()` for responsive grids. Grid is two-dimensional (rows AND columns), Flexbox is one-dimensional - use `grid-area` or line numbers to place items, named areas are more readable than line numbers.

Example:

```css
.container {
  display: grid;
  grid-template-columns: repeat(3, 1fr);
  grid-template-rows: auto 1fr auto;
  gap: 1rem;
}
.item {
  grid-column: 1 / 3;
}
```

---

## Q36. 🎨 CSS subgrid and its use cases

CSS subgrid allows grid items to participate in their parent's grid layout, enabling complex nested grid structures with consistent alignment - subgrid has limited support, requires fallbacks for older browsers. Allows child grids to inherit parent grid structure and alignment.

- **Trade-offs**: The catch is ensures nested elements align with parent grid lines - enables sophisticated page layouts with multiple grid levels. Perfect for magazine-style layouts, complex dashboards, and nested components.

Example:

```css
.main-grid {
  display: grid;
  grid-template-columns: 200px 1fr 200px;
  gap: 20px;
}
.nested-grid {
  display: grid;
  grid-template-columns: subgrid;
  grid-column: 1 / -1;
}

```

---

## Q22. 🤔 Flexbox vs Grid

Grid handles 2D layouts (both rows and columns), while Flexbox handles 1D (row OR column) - use Grid for page structure and Flexbox for components. Grid is for page layouts and complex two-dimensional arrangements, Flexbox is for component layouts and navigation bars.

- **Trade-offs**: The catch is trying to use one for everything instead of combining both - both have excellent modern browser support, Grid is newer. Flexbox is simpler to learn, Grid is more powerful but complex - use Grid for overall structure and Flexbox for component internals, they complement each other.

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

## Q23. 🎨 CSS transitions and how to use them

Transitions make property changes smooth over time instead of instant - great for hover effects and user feedback, different properties can have different durations and timing functions. You can target specific properties or use `all` for multiple properties.

- **Trade-offs**: The catch is GPU-accelerated properties (transform, opacity) perform better than layout properties - JavaScript can listen to `transitionend` events for completion callbacks. Timing functions (`ease`, `linear`, `ease-in-out`) control animation curve.

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

## Q24. 🎨 CSS animations and how to create them

Animations let you create complex, multi-step effects using @keyframes to define what happens at different points - use them for loading spinners or page entrances. Multiple keyframes (0%, 25%, 50%, 100%) create complex animation sequences.

- **Trade-offs**: The catch is `forwards` keeps final state, `backwards` applies initial state before delay - use `transform` and `opacity` for smooth 60fps animations. Animation properties include duration, timing-function, delay, iteration-count, direction, and fill-mode - animation events allow JavaScript control of animations.

Example:

```css
@keyframes slideIn {
  0% { transform: translateX(-100%); opacity: 0; }
  100% { transform: translateX(0); opacity: 1; }
}
.element { animation: slideIn 0.5s ease-in-out; }

```

---

## Q27. 🤔 `transition` vs `animation`

Transitions animate property changes between states, while animations create complex multi-step sequences with @keyframes - transitions are simpler, animations are more powerful. Transitions need a trigger (hover, focus), animations can run automatically.

- **Trade-offs**: The catch is transitions are simpler, animations offer more control with keyframes - both can be paused, reversed, or controlled with JavaScript. Use transitions for simple state changes and animations for complex sequences.

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

## Q28. 🎨 Creating CSS animations using `@keyframes`

Use `@keyframes` to define animation steps, then apply with the `animation` property - keyframes define what happens at different points in the animation. Define keyframes with percentages (0%, 50%, 100%) or keywords (from, to).

- **Trade-offs**: The catch is `infinite` makes animation repeat, `alternate` reverses direction - use `fill-mode: forwards` to keep final state after animation ends. Animation shorthand includes: name, duration, timing-function, delay, iteration-count, direction, fill-mode.

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

## Q29. 🎬 Media queries and how to use them

Media queries let you apply different styles based on device features like screen width - essential for making websites work on phones, tablets, and desktops. Common breakpoints are 768px (tablet), 1024px (desktop), 1200px (large desktop).

- **Trade-offs**: The catch is logical operators (`and`, `or`, `not`) combine multiple media conditions - media queries don't affect performance, only load appropriate CSS. Start with mobile styles, then add larger screen styles with `min-width` (mobile-first) - media features include width, orientation, and prefers-color-scheme.

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

## Q30. 🎨 Creating responsive text with CSS

Use relative units (rem, em), viewport units (vw, vh), or `clamp()` for responsive text that scales with screen size - responsive text improves readability across devices. `clamp()` sets min, preferred, and max values for fluid scaling.

- **Trade-offs**: The catch is avoid fixed pixel sizes for text, use relative units - combine media queries with relative units for best results. Use rem for consistent scaling and vw for viewport-based sizing.

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

## Q31. 🎨 CSS variables (custom properties), how to use them, and their role in design systems

CSS variables let you store values like colors or spacing that you can reuse anywhere and even change with JavaScript - perfect for theming and maintaining consistent design tokens. Variables inherit and can be overridden at different levels (root, element, pseudo-class).

- **Trade-offs**: The catch is JavaScript can change CSS variables: `element.style.setProperty('--color', 'red')` - variables are computed at runtime, use sparingly for performance-critical properties. `var(--color, #fallback)` provides fallback when variable is undefined - CSS variables enable dynamic theming and design tokens.

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

## Q40. 🔧 CSS `color-mix()` function and its usage

The `color-mix()` function allows you to blend two colors in a specified color space, giving you more control than traditional CSS - perfect for creating color variations and theming. Blends two colors in specified color space (srgb, display-p3, etc.).

- **Trade-offs**: The catch is supports percentage mixing and different color spaces - works with CSS custom properties for dynamic theming. Perfect for creating color variations, theming, and dynamic color schemes.

Example:

```css
:root {
  --primary: #007bff;
  --secondary: #6c757d;
}
.element {
  background-color: color-mix(
    in srgb,
    var(--primary) 70%,
    var(--secondary) 30%
  );
}

```

---

## Q32. 🤔 SASS vs LESS

SASS and LESS are CSS preprocessors that add features like variables and mixins - SASS uses indentation or SCSS syntax, LESS uses CSS-like syntax, both compile to CSS. SASS has two syntaxes (indented SASS, SCSS), LESS uses CSS-like syntax.

- **Trade-offs**: The catch is SASS is more popular, LESS is easier for CSS developers - choose based on team preference and tooling support. Both support variables, mixins, nesting, and functions - choose based on preference and team needs.

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

---

## 📍 Navigation

<div align="center">

[← Previous: Fundamentals & Basics](01%29%20Fundamentals%20%26%20Basics.md) • [Home: README](../README.md) • [Next: Architecture & Design Systems →](04%29%20Architecture%20%26%20Design%20Systems.md)

[📋 Cheatsheet](CSS%20Interview%20Cheatsheet.md)

</div>

---
