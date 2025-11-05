# 2) Intermediate Level CSS (Q21–40)

---

## 21) What is CSS Flexbox and how does it work?

Flexbox helps you lay out items in one direction (row or column) with flexible sizing and easy alignment. Use it when you need to distribute space or center content.

```css
.container {
  display: flex;
  justify-content: space-between;
  align-items: center;
  flex-wrap: wrap;
}
```

- **Core Concept**: Flexbox works on two axes - main (flex-direction) and cross (perpendicular)
- **Real-World Use**: `flex` is shorthand for `flex-grow`, `flex-shrink`, and `flex-basis`
- **Alignment Control**: `justify-content` controls main axis, `align-items` controls cross axis
- **Common Mistake**: Items can grow/shrink based on available space and flex values
- **Interview Tip**: Explain that `order` property allows visual reordering without changing HTML structure

---

## 22) Explain CSS Grid and its key features.

Grid lets you create layouts with both rows and columns at once, giving you precise control over where items go. Perfect for complex page layouts.

```css
.grid-container {
  display: grid;
  grid-template-columns: repeat(3, 1fr);
  gap: 20px;
  grid-template-areas: "header header header" "sidebar content content" "footer footer footer";
}
```

- **Core Feature**: Unlike Flexbox, Grid handles both rows and columns simultaneously
- **Real-World Use**: Named grid areas make complex layouts more readable and maintainable
- **Advanced Feature**: `fr` units distribute available space proportionally
- **Optimization**: Grid can create implicit rows/columns when content exceeds defined tracks
- **Interview Tip**: Explain that items can be positioned using line numbers or named lines

---

## 23) What are CSS transitions and how do they work?

Transitions make property changes smooth over time instead of instant. Great for hover effects and user feedback.

```css
.button { background-color: #007bff; transition: all 0.3s ease-in-out; }
.button:hover { background-color: #0056b3; transform: scale(1.05); }
```

- **Core Purpose**: Can target specific properties or use `all` for multiple properties
- **Real-World Use**: Timing functions (`ease`, `linear`, `ease-in-out`) control animation curve
- **Performance**: GPU-accelerated properties (transform, opacity) perform better than layout properties
- **Advanced Feature**: JavaScript can listen to `transitionend` events for completion callbacks
- **Interview Tip**: Explain that different properties can have different durations and timing functions

---

## 24) Explain CSS animations and @keyframes.

Animations let you create complex, multi-step effects using @keyframes to define what happens at different points. Use them for loading spinners or page entrances.

```css
@keyframes slideIn {
  0% { transform: translateX(-100%); opacity: 0; }
  100% { transform: translateX(0); opacity: 1; }
}
.element { animation: slideIn 0.5s ease-in-out; }
```

- **Core Concept**: Multiple keyframes (0%, 25%, 50%, 100%) create complex animation sequences
- **Real-World Use**: Animation properties include duration, timing-function, delay, iteration-count, direction, fill-mode
- **Advanced Feature**: `forwards` keeps final state, `backwards` applies initial state before delay
- **Performance**: Use `transform` and `opacity` for smooth 60fps animations
- **Interview Tip**: Explain that animation events (`animationstart`, `animationend`) allow JavaScript control

---

## 25) What are CSS preprocessors and their benefits?

Preprocessors add programming features to CSS like variables and functions, then compile to regular CSS. They make CSS more maintainable and DRY.

```scss
$primary-color: #007bff;
@mixin button-style($bg-color, $text-color: white) {
  background-color: $bg-color;
  color: $text-color;
  padding: 10px 20px;
}
```

- **Core Benefit**: Mixins and functions eliminate CSS duplication and improve maintainability
- **Real-World Use**: Nesting provides logical grouping of related styles, reduces specificity conflicts
- **Advanced Feature**: Variables centralize color schemes, spacing, and other design tokens
- **Optimization**: Perform calculations directly in CSS for responsive design
- **Interview Tip**: Explain that modular CSS architecture uses `@import` and partial files

---

## 26) Explain CSS specificity and how it works.

Specificity is CSS's way of deciding which styles win when multiple rules target the same element. Higher specificity (IDs beat classes, classes beat elements) overrides lower specificity.

```css
div { color: red; }
.container { color: blue; }
#header { color: green; }
div.container { color: purple; }
```

- **Core Calculation**: Inline styles (1000) > IDs (100) > Classes (10) > Elements (1)
- **Real-World Use**: When specificity is equal, later rules override earlier ones (cascade order)
- **Common Mistake**: `!important` has highest priority but should be used sparingly
- **Optimization**: High specificity can make CSS hard to maintain and debug
- **Interview Tip**: Explain that use low specificity and rely on cascade order for maintainable CSS

---

## 27) What are CSS pseudo-classes and pseudo-elements?

Pseudo-classes target element states like :hover or :focus. Pseudo-elements create virtual elements like ::before that don't exist in your HTML.

```css
.button:hover { background-color: #0056b3; }
.button:focus { border: 2px solid blue; }
.button::before { content: "★ "; color: gold; }
.button::after { content: " ✓"; color: green; }
```

- **Core Difference**: Pseudo-classes respond to user interactions and element states
- **Real-World Use**: Pseudo-elements create content that doesn't exist in HTML
- **Common Mistake**: `::before` and `::after` require `content` property to be visible
- **Optimization**: Each element can only have one `::before` and one `::after`
- **Interview Tip**: Explain that pseudo-elements are not accessible to screen readers, use sparingly

---

## 28) Explain CSS combinators and their usage.

Combinators let you target elements based on their relationship to other elements - like children, siblings, or descendants. Useful for styling nested structures.

```css
.container p { color: blue; }
.container > p { font-weight: bold; }
h1 + p { margin-top: 0; }
h2 ~ p { color: gray; }
```

- **Core Types**: Descendant (space) targets any descendant, child (>) targets only direct children
- **Real-World Use**: Adjacent sibling (+) targets immediately following sibling, general sibling (~) targets all following siblings
- **Common Mistake**: Child combinators are generally faster than descendant combinators
- **Optimization**: Use combinators to avoid adding unnecessary classes
- **Interview Tip**: Explain that combinators help maintain clean HTML structure

---

## 29) What is the CSS cascade and how does it work?

The cascade is CSS's priority system - it decides which styles win based on order, specificity, and !important. Later styles override earlier ones when specificity is equal.

```css
.button { color: red; }
.button { color: blue; }
.button { color: green !important; }
```

- **Core Rule**: Later styles override earlier ones when specificity is equal (source order)
- **Real-World Use**: Higher specificity overrides lower specificity
- **Common Mistake**: `!important` has highest priority but breaks cascade flow
- **Optimization**: Some properties inherit from parent elements automatically
- **Interview Tip**: Explain that modern CSS supports `@layer` for explicit cascade control

---

## 30) Explain CSS units and when to use each.

CSS units come in two types: absolute (px) stays fixed, while relative (em, rem, %) scales with context. Use relative units for responsive designs.

```css
.container { width: 100%; max-width: 1200px; padding: 1rem; margin: 2em; font-size: 16px; }
```

- **Core Types**: Absolute units (`px`, `pt`) are fixed, relative units (`em`, `rem`, `%`) scale with context
- **Real-World Use**: `em` scales with element's font size, `rem` scales with root font size
- **Advanced Units**: Viewport units (`vw`, `vh`, `vmin`, `vmax`) scale with viewport dimensions
- **Optimization**: Percentage (`%`) scales with parent element's corresponding property
- **Interview Tip**: Explain that unitless values work better for `line-height` and `z-index`

---

## 31) What is the CSS box model and how does it work?

The box model shows how every element has four layers: content, padding, border, and margin. Understanding this helps you predict element sizes and spacing.

```css
.box {
  width: 200px;
  height: 100px;
  padding: 20px;
  border: 2px solid #333;
  margin: 10px;
}
```

- **Core Layers**: Content area (actual content), padding (space between content and border), border (visual boundary), margin (space outside border)
- **Real-World Use**: Padding affects background color, margin doesn't affect background and can collapse
- **Common Mistake**: Not understanding how box-sizing affects width/height calculations
- **Optimization**: `border-box` makes width/height include padding and border for easier calculations
- **Interview Tip**: Explain that margin collapse happens with adjacent elements

---

## 32) Explain CSS positioning and its values.

Positioning controls where elements sit in the page flow. Static is default, relative offsets from normal position, absolute/fixed remove from flow.

```css
.static { position: static; }
.relative { position: relative; top: 10px; left: 20px; }
.absolute { position: absolute; top: 50px; right: 10px; }
.fixed { position: fixed; bottom: 20px; right: 20px; }
```

- **Core Values**: Static (default, follows normal flow), relative (stays in flow but can be offset), absolute (removed from flow, relative to positioned ancestor), fixed (removed from flow, relative to viewport)
- **Real-World Use**: Sticky is hybrid of relative and fixed, switches based on scroll position
- **Common Mistake**: Absolute positioning requires positioned ancestor, otherwise uses viewport
- **Optimization**: Fixed positioning stays in place during scroll, useful for navigation bars
- **Interview Tip**: Explain that positioning creates new stacking contexts

---

## 33) What are CSS media queries and how do they work?

Media queries let you apply different styles based on device features like screen width. Essential for making websites work on phones, tablets, and desktops.

```css
.container { width: 100%; padding: 10px; }
@media (min-width: 768px) {
  .container { width: 750px; padding: 20px; }
}
@media (min-width: 1024px) { .container { width: 1200px; } }
```

- **Core Purpose**: Common breakpoints are 768px (tablet), 1024px (desktop), 1200px (large desktop)
- **Real-World Use**: Start with mobile styles, then add larger screen styles with `min-width` (mobile-first)
- **Advanced Features**: Logical operators (`and`, `or`, `not`) combine multiple media conditions
- **Optimization**: Media queries don't affect performance, only load appropriate CSS
- **Interview Tip**: Explain that media features include `width`, `orientation`, `prefers-color-scheme`

---

## 34) Explain CSS Grid vs Flexbox and when to use each.

Grid handles 2D layouts (both rows and columns), while Flexbox handles 1D (row OR column). Use Grid for page structure and Flexbox for components.

```css
.page-layout { display: grid; grid-template-columns: 200px 1fr 200px; min-height: 100vh; }
.card { display: flex; justify-content: center; align-items: center; }
```

- **Core Difference**: Grid for page layouts and complex two-dimensional arrangements, Flexbox for component layouts and navigation bars
- **Real-World Use**: Use Grid for overall structure, Flexbox for component internals - they complement each other
- **Common Mistake**: Trying to use one for everything instead of combining both
- **Optimization**: Both have excellent modern browser support, Grid is newer
- **Interview Tip**: Explain that Flexbox is simpler to learn, Grid is more powerful but complex

---

## 35) What are CSS custom properties (CSS variables)?

CSS variables let you store values like colors or spacing that you can reuse anywhere and even change with JavaScript. Perfect for theming and maintaining consistent design tokens.

```css
:root {
  --primary-color: #007bff;
  --secondary-color: #6c757d;
  --border-radius: 4px;
  --spacing-unit: 8px;
}
```

- **Core Feature**: Variables inherit and can be overridden at different levels (root, element, pseudo-class)
- **Real-World Use**: `var(--color, #fallback)` provides fallback when variable is undefined
- **Advanced Feature**: JavaScript can change CSS variables: `element.style.setProperty('--color', 'red')`
- **Optimization**: Modern CSS supports `color-mix()`, `hsl()`, `rgb()` with variables
- **Interview Tip**: Explain that variables are computed at runtime, use sparingly for performance-critical properties

---

## 36) Explain CSS preprocessors (SASS/SCSS) in detail.

SASS/SCSS adds programming features to CSS like variables and mixins, then compiles to regular CSS browsers understand. It makes CSS more powerful and maintainable.

```scss
$primary-color: #007bff;
$breakpoints: (mobile: 768px, tablet: 1024px, desktop: 1200px);
@mixin responsive($breakpoint) {
  @media (min-width: map-get($breakpoints, $breakpoint)) { @content; }
}
```

- **Core Difference**: SASS uses indentation, SCSS uses curly braces and semicolons
- **Real-World Use**: Preprocessors compile to CSS, so browser support depends on output CSS
- **Advanced Feature**: Variables are more powerful than CSS custom properties, support calculations and functions
- **Common Mistake**: Nesting can create high specificity if overused
- **Interview Tip**: Explain that modular architecture uses `@import` and partial files (underscore prefix)

---

## 37) What are CSS mixins and how do they work?

Mixins are reusable style blocks you can include anywhere, like functions for CSS. They eliminate repetition and make updates easier since you change code in one place.

```scss
@mixin flex-center {
  display: flex;
  justify-content: center;
  align-items: center;
}
```

- **Core Purpose**: Mixins eliminate duplicate CSS and centralize common patterns
- **Real-World Use**: Mixins can accept parameters for customization and flexibility
- **Advanced Feature**: Parameters can have default values for optional customization
- **Optimization**: Mixins can contain nested selectors and pseudo-classes
- **Interview Tip**: Explain that mixins are expanded at compile time, so they don't exist in final CSS

---

## 38) Explain CSS @extend and placeholder selectors.

@extend lets selectors inherit styles from others, while placeholders (starting with %) create base styles that only exist when extended. Use placeholders for shared base styles.

```scss
%button-base { padding: 10px 20px; border: none; border-radius: 4px; cursor: pointer; }
.btn-primary { @extend %button-base; background-color: blue; }
.btn-secondary { @extend %button-base; background-color: gray; }
```

- **Core Concept**: Placeholder selectors start with `%` and don't output CSS unless extended
- **Real-World Use**: `@extend` creates a relationship between selectors, not just copying styles
- **Advanced Feature**: Extended styles are merged into the extending selector in final CSS
- **Optimization**: Extended styles inherit the specificity of the original selector
- **Interview Tip**: Explain that use placeholders for base styles, mixins for parameterized styles

---

## 39) What are CSS functions and how do they work?

CSS functions let you do math, manipulate colors, transform elements, or apply filters. They make CSS more dynamic and responsive without JavaScript.

```css
.container { width: calc(100% - 40px); height: calc(100vh - 80px); }
.element { background-color: rgb(255, 0, 0); transform: translateX(50px); }
.image { filter: blur(5px) brightness(1.2); }
```

- **Core Types**: Mathematical (`calc()`, `min()`, `max()`, `clamp()`), color (`rgb()`, `hsl()`, `color-mix()`), transform (`translate()`, `rotate()`, `scale()`), filter (`blur()`, `brightness()`)
- **Real-World Use**: Use for responsive calculations, color manipulation, element transformations, visual effects
- **Common Mistake**: Some functions trigger layout recalculations, affecting performance
- **Optimization**: Some functions are GPU-accelerated, others trigger layout recalculations
- **Interview Tip**: Explain that CSS functions enable dynamic styling without JavaScript

---

## 40) Explain CSS inheritance and how it works.

Inheritance means child elements automatically get some properties from their parents, like font-family or color. This reduces repetition and keeps your styles consistent.

```css
body {
  font-family: 'Arial', sans-serif;
  font-size: 16px;
  line-height: 1.5;
  color: #333;
}
```

- **Core Concept**: Inherited properties include `font-family`, `font-size`, `color`, `line-height`, `text-align`, `visibility`
- **Real-World Use**: Non-inherited properties include `width`, `height`, `margin`, `padding`, `border`, `background`
- **Common Mistake**: Properties cascade down through the DOM tree from parent to child
- **Optimization**: Child elements can override inherited properties with their own values
- **Interview Tip**: Explain that inherited properties are more efficient than explicitly setting them on every element

---
