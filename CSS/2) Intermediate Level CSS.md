# 2) Intermediate Level CSS (Q21–40)

## 21) What is CSS Flexbox and how does it work?

Concept:
Flexbox is a one-dimensional layout method that arranges items in rows or columns with flexible sizing and alignment capabilities.

Example:
```css
.container {
  display: flex;
  justify-content: space-between;
  align-items: center;
  flex-wrap: wrap;
}
```

Deep Insight:
- Main vs Cross Axis: Flexbox works on two axes - main (flex-direction) and cross (perpendicular)
- Flex Properties: `flex` is shorthand for `flex-grow`, `flex-shrink`, and `flex-basis`
- Alignment Control: `justify-content` controls main axis, `align-items` controls cross axis
- Flexible Sizing: Items can grow/shrink based on available space and flex values
- Order Control: `order` property allows visual reordering without changing HTML structure

## 22) Explain CSS Grid and its key features.

Concept:
CSS Grid is a two-dimensional layout system that creates complex layouts using rows and columns with precise control over item placement.

Example:
```css
.grid-container {
  display: grid;
  grid-template-columns: repeat(3, 1fr);
  grid-template-rows: auto 1fr auto;
  gap: 20px;
  grid-template-areas: 
    "header header header"
    "sidebar content content"
    "footer footer footer";
}
```

Deep Insight:
- **Two-Dimensional**: Unlike Flexbox, Grid handles both rows and columns simultaneously
- **Grid Areas**: Named grid areas make complex layouts more readable and maintainable
- **Fractional Units**: `fr` units distribute available space proportionally
- **Implicit vs Explicit**: Grid can create implicit rows/columns when content exceeds defined tracks
- **Grid Lines**: Items can be positioned using line numbers or named lines

## 23. What are CSS transitions and how do they work?

Concept:
CSS transitions provide smooth animations between different property values over a specified duration with customizable timing functions.

Example:
```css
.button {
  background-color: #007bff;
  transition: all 0.3s ease-in-out;
  transform: scale(1);
}

.button:hover {
  background-color: #0056b3;
  transform: scale(1.05);
}
```

Deep Insight:
- **Property-Specific**: Can target specific properties or use `all` for multiple properties
- **Timing Functions**: `ease`, `linear`, `ease-in`, `ease-out`, `ease-in-out` control animation curve
- **Performance**: GPU-accelerated properties (transform, opacity) perform better than layout properties
- **Transition Events**: JavaScript can listen to `transitionend` events for completion callbacks
- **Multiple Transitions**: Different properties can have different durations and timing functions

## 24. Explain CSS animations and @keyframes.

Concept:
CSS animations create complex, multi-step animations using @keyframes to define intermediate states and animation properties to control timing and behavior.

Example:
```css
@keyframes slideIn {
  0% {
    transform: translateX(-100%);
    opacity: 0;
  }
  50% {
```

Deep Insight:
- **Keyframe Control**: Multiple keyframes (0%, 25%, 50%, 100%) create complex animation sequences
- **Animation Properties**: `duration`, `timing-function`, `delay`, `iteration-count`, `direction`, `fill-mode`
- **Fill Modes**: `forwards` keeps final state, `backwards` applies initial state before delay
- **Performance**: Use `transform` and `opacity` for smooth 60fps animations
- **Animation Events**: `animationstart`, `animationend`, `animationiteration` for JavaScript control

## 25. What are CSS preprocessors and their benefits?

Concept:
CSS preprocessors extend CSS with programming features like variables, nesting, mixins, and functions, then compile to standard CSS.

Example:
```scss
// Variables
$primary-color: #007bff;
$border-radius: 4px;

// Mixin
@mixin button-style($bg-color, $text-color: white) {
```

Deep Insight:
- **Code Reusability**: Mixins and functions eliminate CSS duplication and improve maintainability
- **Nesting**: Logical grouping of related styles reduces specificity conflicts
- **Variables**: Centralized color schemes, spacing, and other design tokens
- **Mathematical Operations**: Perform calculations directly in CSS for responsive design
- **Import System**: Modular CSS architecture with `@import` and partial files

## 26. Explain CSS specificity and how it works.

Concept:
CSS specificity determines which styles apply when multiple rules target the same element, calculated using a point system based on selector types.

Example:
```css
/* Specificity: 0,0,0,1 (1 element) */
div { color: red; }

/* Specificity: 0,0,1,0 (1 class) */
.container { color: blue; }

```

Deep Insight:
- **Specificity Calculation**: Inline styles (1000) > IDs (100) > Classes (10) > Elements (1)
- **Cascade Order**: When specificity is equal, later rules override earlier ones
- **!important Override**: `!important` has highest priority but should be used sparingly
- **Specificity Wars**: High specificity can make CSS hard to maintain and debug
- **Best Practices**: Use low specificity and rely on cascade order for maintainable CSS

## 27. What are CSS pseudo-classes and pseudo-elements?

Concept:
Pseudo-classes target element states (like :hover), while pseudo-elements create virtual elements (like ::before) for styling without additional HTML.

Example:
```css
/* Pseudo-classes */
.button:hover {
  background-color: #0056b3;
}

.button:focus {
```

Deep Insight:
- **State Targeting**: Pseudo-classes respond to user interactions and element states
- **Virtual Elements**: Pseudo-elements create content that doesn't exist in HTML
- **Content Property**: `::before` and `::after` require `content` property to be visible
- **Single Pseudo-element**: Each element can only have one `::before` and one `::after`
- **Accessibility**: Pseudo-elements are not accessible to screen readers, use sparingly

## 28. Explain CSS combinators and their usage.

Concept:
CSS combinators define relationships between selectors, allowing you to target elements based on their position in the document tree.

Example:
```css
/* Descendant combinator (space) */
.container p {
  color: blue;
}

/* Child combinator (>) */
```

Deep Insight:
- **Descendant (space)**: Targets any descendant at any level of nesting
- **Child (>):** Targets only direct children, not grandchildren or deeper
- **Adjacent Sibling (+):** Targets the immediately following sibling element
- **General Sibling (~):** Targets all following sibling elements
- **Performance**: Child combinators are generally faster than descendant combinators

## 29. What is the CSS cascade and how does it work?

Concept:
The CSS cascade determines which styles apply when multiple rules target the same element, based on source order, specificity, and importance.

Example:
```css
/* External stylesheet */
.button { color: red; }

/* Internal stylesheet */
.button { color: blue; }

```

Deep Insight:
- **Source Order**: Later styles override earlier ones when specificity is equal
- **Specificity**: Higher specificity overrides lower specificity
- **Importance**: `!important` has highest priority but breaks cascade flow
- **Inheritance**: Some properties inherit from parent elements automatically
- **Cascade Layers**: Modern CSS supports `@layer` for explicit cascade control

## 30. Explain CSS units and when to use each.

Concept:
CSS units define measurement values for properties, with absolute units (px) and relative units (em, rem, %) serving different purposes in responsive design.

Example:
```css
.container {
  width: 100%; /* Percentage of parent */
  max-width: 1200px; /* Absolute pixel value */
  padding: 1rem; /* Relative to root font size */
  margin: 2em; /* Relative to element's font size */
  font-size: 16px; /* Base font size */
```

Deep Insight:
- **Absolute Units**: `px` is fixed, `pt` for print, `in`, `cm`, `mm` for physical measurements
- **Relative Units**: `em` scales with element's font size, `rem` scales with root font size
- **Viewport Units**: `vw`, `vh`, `vmin`, `vmax` scale with viewport dimensions
- **Percentage**: `%` scales with parent element's corresponding property
- **Unitless Values**: `line-height`, `z-index` work better without units

## 31. What is the CSS box model and how does it work?

Concept:
The CSS box model describes how elements are rendered with content, padding, border, and margin areas that combine to create the total element size.

Example:
```css
.box {
  width: 200px;
  height: 100px;
  padding: 20px;
  border: 2px solid #333;
  margin: 10px;
```

Deep Insight:
- **Content Area**: The actual content (text, images) inside the element
- **Padding**: Space between content and border, affects background color
- **Border**: Visual boundary around padding, can be styled with color, width, style
- **Margin**: Space outside border, doesn't affect background, can collapse with adjacent margins
- **Box-Sizing**: `border-box` makes width/height include padding and border for easier calculations

## 32. Explain CSS positioning and its values.

Concept:
CSS positioning controls how elements are placed in the document flow, with static, relative, absolute, fixed, and sticky values each behaving differently.

Example:
```css
.static { position: static; } /* Default, follows normal flow */

.relative {
  position: relative;
  top: 10px;
  left: 20px; /* Offset from normal position */
```

Deep Insight:
- **Static**: Default positioning, elements follow normal document flow
- **Relative**: Element stays in flow but can be offset with top/right/bottom/left
- **Absolute**: Removed from flow, positioned relative to nearest positioned ancestor
- **Fixed**: Removed from flow, positioned relative to viewport, stays in place during scroll
- **Sticky**: Hybrid of relative and fixed, switches based on scroll position

## 33. What are CSS media queries and how do they work?

Concept:
CSS media queries apply styles conditionally based on device characteristics like screen size, resolution, orientation, and other media features.

Example:
```css
/* Mobile first approach */
.container {
  width: 100%;
  padding: 10px;
}

```

Deep Insight:
- **Breakpoints**: Common breakpoints are 768px (tablet), 1024px (desktop), 1200px (large desktop)
- **Mobile First**: Start with mobile styles, then add larger screen styles with `min-width`
- **Logical Operators**: `and`, `or`, `not` combine multiple media conditions
- **Media Features**: `width`, `height`, `orientation`, `resolution`, `prefers-color-scheme`
- **Performance**: Media queries don't affect performance, only load appropriate CSS

## 34. Explain CSS Grid vs Flexbox and when to use each.

Concept:
Grid is for two-dimensional layouts (rows and columns), while Flexbox is for one-dimensional layouts (either rows or columns), but they can work together.

Example:
```css
/* Grid for overall page layout */
.page-layout {
  display: grid;
  grid-template-columns: 200px 1fr 200px;
  grid-template-rows: auto 1fr auto;
  min-height: 100vh;
```

Deep Insight:
- **Grid Use Cases**: Page layouts, complex two-dimensional arrangements, overlapping elements
- **Flexbox Use Cases**: Component layouts, navigation bars, form controls, centering content
- **Combination**: Use Grid for overall structure, Flexbox for component internals
- **Browser Support**: Both have excellent modern browser support, but Grid is newer
- **Learning Curve**: Flexbox is simpler to learn, Grid is more powerful but complex

## 35. What are CSS custom properties (CSS variables)?

Concept:
CSS custom properties (variables) allow you to store values that can be reused throughout your stylesheet and updated dynamically with JavaScript.

Example:
```css
:root {
  --primary-color: #007bff;
  --secondary-color: #6c757d;
  --border-radius: 4px;
  --spacing-unit: 8px;
}
```

Deep Insight:
- **Scope**: Variables inherit and can be overridden at different levels (root, element, pseudo-class)
- **Fallback Values**: `var(--color, #fallback)` provides fallback when variable is undefined
- **Dynamic Updates**: JavaScript can change CSS variables: `element.style.setProperty('--color', 'red')`
- **Color Functions**: Modern CSS supports `color-mix()`, `hsl()`, `rgb()` with variables
- **Performance**: Variables are computed at runtime, so use sparingly for performance-critical properties

## 36. Explain CSS preprocessors (SASS/SCSS) in detail.

Concept:
SASS/SCSS extends CSS with programming features like variables, nesting, mixins, functions, and control structures, then compiles to standard CSS.

Example:
```scss
// Variables
$primary-color: #007bff;
$border-radius: 4px;
$breakpoints: (
  mobile: 768px,
  tablet: 1024px,
```

Deep Insight:
- **SASS vs SCSS**: SASS uses indentation, SCSS uses curly braces and semicolons
- **Compilation**: Preprocessors compile to CSS, so browser support depends on output CSS
- **Variables**: More powerful than CSS custom properties, support calculations and functions
- **Nesting**: Logical grouping but can create high specificity if overused
- **Import System**: Modular architecture with `@import` and partial files (underscore prefix)

## 37. What are CSS mixins and how do they work?

Concept:
CSS mixins are reusable blocks of styles that can be included in other selectors, eliminating code duplication and improving maintainability.

Example:
```scss
// Basic mixin
@mixin flex-center {
  display: flex;
  justify-content: center;
  align-items: center;
}
```

Deep Insight:
- **Code Reusability**: Mixins eliminate duplicate CSS and centralize common patterns
- **Parameters**: Mixins can accept parameters for customization and flexibility
- **Default Values**: Parameters can have default values for optional customization
- **Nesting**: Mixins can contain nested selectors and pseudo-classes
- **Compilation**: Mixins are expanded at compile time, so they don't exist in final CSS

## 38. Explain CSS @extend and placeholder selectors.

Concept:
`@extend` allows selectors to inherit styles from other selectors, while placeholder selectors (starting with %) create extendable base styles that don't output CSS themselves.

Example:
```scss
// Placeholder selector (won't output CSS)
%button-base {
  padding: 10px 20px;
  border: none;
  border-radius: 4px;
  cursor: pointer;
```

Deep Insight:
- **Placeholder Selectors**: Start with `%` and don't output CSS unless extended
- **Inheritance**: `@extend` creates a relationship between selectors, not just copying styles
- **Compilation**: Extended styles are merged into the extending selector in final CSS
- **Specificity**: Extended styles inherit the specificity of the original selector
- **Best Practices**: Use placeholders for base styles, mixins for parameterized styles

## 39. What are CSS functions and how do they work?

Concept:
CSS functions perform calculations, transformations, or operations on values, providing dynamic and responsive styling capabilities.

Example:
```css
.container {
  /* Mathematical functions */
  width: calc(100% - 40px);
  height: calc(100vh - 80px);
  
  /* Color functions */
```

Deep Insight:
- **Mathematical**: `calc()`, `min()`, `max()`, `clamp()` for responsive calculations
- **Color**: `rgb()`, `hsl()`, `color-mix()`, `lighten()`, `darken()` for color manipulation
- **Transform**: `translate()`, `rotate()`, `scale()`, `skew()` for element transformations
- **Filter**: `blur()`, `brightness()`, `contrast()`, `saturate()` for visual effects
- **Performance**: Some functions are GPU-accelerated, others trigger layout recalculations

## 40. Explain CSS inheritance and how it works.

Concept:
CSS inheritance allows child elements to automatically inherit certain properties from their parent elements, reducing code duplication and maintaining consistency.

Example:
```css
body {
  font-family: 'Arial', sans-serif;
  font-size: 16px;
  line-height: 1.5;
  color: #333;
}
```

Deep Insight:
- **Inherited Properties**: `font-family`, `font-size`, `color`, `line-height`, `text-align`, `visibility`
- **Non-Inherited Properties**: `width`, `height`, `margin`, `padding`, `border`, `background`
- **Inheritance Chain**: Properties cascade down through the DOM tree from parent to child
- **Override**: Child elements can override inherited properties with their own values
- **Performance**: Inherited properties are more efficient than explicitly setting them on every element
