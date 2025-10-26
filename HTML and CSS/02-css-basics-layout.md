# 🎨 HTML & CSS Interview Notes (2025 Edition)

## 🟡 Section 2 — CSS Basics & Layout — Q21-Q40

---

### 21. 🟡 What is CSS, and why is it used?

**🧠 Concept**

CSS is the language that makes HTML look beautiful. It controls colors, fonts, layout, and visual effects.

**💻 Example**
```css
/* Basic CSS styling */
body {
    font-family: Arial, sans-serif;
    background-color: #f4f4f4;
    margin: 0;
    padding: 20px;
}

h1 {
    color: #333;
    text-align: center;
    font-size: 2.5rem;
}

.button {
    background-color: #007bff;
    color: white;
    padding: 10px 20px;
    border: none;
    border-radius: 5px;
    cursor: pointer;
}
```

**💬 Explanation + Insight**

- **Separation of Concerns** - CSS separates content (HTML) from presentation
- **Responsive Design** - Enables responsive design and consistent styling
- **Cascade Principle** - Follows the cascade principle (later rules override earlier ones)
- **Professional Look** - Makes websites look professional and polished
- **Visual Appeal** - Without CSS, websites would look plain and boring

---

### 22. 🟡 What are inline, internal, and external styles?

**🧠 Concept**

CSS can be applied in three ways: inline (within HTML elements), internal (in `<style>` tags), and external (in separate .css files).

**💻 Example**
```html
<!-- Inline styles -->
<p style="color: red; font-size: 18px;">This is inline styling</p>

<!-- Internal styles -->
<head>
    <style>
        .highlight {
            background-color: yellow;
            font-weight: bold;
        }
        #main-title {
            color: blue;
            text-align: center;
        }
    </style>
</head>

<!-- External styles -->
<head>
    <link rel="stylesheet" href="styles.css">
</head>
```

**💬 Explanation + Insight**

- **External Preferred** - External stylesheets are preferred for maintainability and performance
- **Inline Specificity** - Inline styles have the highest specificity and should be avoided except for dynamic styling
- **Internal Styles** - Internal styles are useful for page-specific styles
- **Shared Styles** - External styles can be shared across multiple pages
- **Right Choice** - Choose the right method for your needs

---

### 23. 🟡 What is the CSS box model?

**🧠 Concept**

The CSS box model describes how elements are rendered as rectangular boxes with content, padding, border, and margin areas.

**💻 Example**
```css
.box {
    width: 200px;           /* Content width */
    height: 100px;         /* Content height */
    padding: 20px;          /* Space inside border */
    border: 5px solid #333; /* Border around padding */
    margin: 10px;           /* Space outside border */
    background-color: #f0f0f0;
}

/* Total width = width + padding + border + margin */
/* Total = 200px + 40px + 10px + 20px = 270px */
```

**📝 Deeper Insight**

The box model can be changed with `box-sizing: border-box`, where width includes padding and border. This is often preferred for responsive design as it makes sizing more predictable.

---

### 24. 🟡 What is the difference between margin, border, and padding?

**🧠 Concept**

Margin is space outside the element, border is the visible edge, and padding is space inside the element between content and border.

**💻 Example**


```css
.element {
    /* Content area */
    width: 200px;
    height: 100px;
    background-color: lightblue;
    
    /* Padding - space inside border */
    padding: 20px; /* All sides */
    padding: 10px 20px; /* top/bottom left/right */
    padding: 10px 15px 20px 25px; /* top right bottom left */
    
    /* Border - visible edge */
    border: 3px solid red;
    border-width: 3px;
    border-style: solid;
    border-color: red;
    
    /* Margin - space outside border */
    margin: 30px; /* All sides */
    margin: 10px auto; /* top/bottom left/right (auto centers) */
}
```

**📝 Deeper Insight**

Margins can collapse (overlapping margins combine), while padding never collapses. Negative margins can be used for overlapping elements, while negative padding is not valid.

---

### 25. 🟡 Difference between display: none, visibility: hidden, and opacity: 0.

**🧠 Concept**

These properties hide elements differently: `display: none` removes from layout, `visibility: hidden` keeps space but hides content, and `opacity: 0` makes transparent but keeps interactivity.

**💻 Example**


```css
.hidden-display {
    display: none; /* Element completely removed from layout */
}

.hidden-visibility {
    visibility: hidden; /* Element hidden but takes up space */
}

.hidden-opacity {
    opacity: 0; /* Element transparent but still interactive */
}

/* Transitions work with opacity but not display */
.fade-out {
    opacity: 0;
    transition: opacity 0.3s ease;
}
```

**📝 Deeper Insight**

`display: none` affects layout flow and cannot be animated. `visibility: hidden` maintains layout but prevents interaction. `opacity: 0` allows for smooth transitions and maintains element interactivity.

---

### 26. 🟡 What are the most common CSS units (px, em, rem, %, vw, vh)?

**🧠 Concept**

CSS units define measurement values: absolute units (px), relative units (em, rem, %), and viewport units (vw, vh) for different sizing needs.

**💻 Example**


```css
.container {
    /* Absolute units */
    width: 1200px; /* Fixed pixel width */
    
    /* Relative to parent */
    width: 80%; /* 80% of parent width */
    
    /* Relative to font size */
    font-size: 1.2em; /* 1.2 times parent font size */
    line-height: 1.5em; /* 1.5 times current font size */
    
    /* Relative to root font size */
    font-size: 1.2rem; /* 1.2 times root (html) font size */
    
    /* Viewport units */
    width: 100vw; /* 100% of viewport width */
    height: 50vh; /* 50% of viewport height */
    font-size: 4vw; /* Font size scales with viewport */
}

/* Responsive typography */
h1 {
    font-size: clamp(1.5rem, 4vw, 3rem); /* Min, preferred, max */
}
```

**📝 Deeper Insight**

`rem` is preferred for consistent scaling, `em` for component-relative sizing, `%` for responsive layouts, and viewport units for full-screen designs. `clamp()` combines these for fluid typography.

---

### 27. 🟡 What is the difference between relative, absolute, fixed, and sticky positioning?

**🧠 Concept**

CSS positioning controls how elements are placed: `static` (default flow), `relative` (offset from normal position), `absolute` (positioned relative to nearest positioned ancestor), `fixed` (relative to viewport), and `sticky` (switches between relative and fixed).

**💻 Example**


```css
/* Relative positioning */
.relative-box {
    position: relative;
    top: 20px; /* Moves 20px down from normal position */
    left: 10px; /* Moves 10px right from normal position */
}

/* Absolute positioning */
.absolute-box {
    position: absolute;
    top: 50px;
    right: 20px; /* Positioned relative to nearest positioned parent */
}

/* Fixed positioning */
.fixed-header {
    position: fixed;
    top: 0;
    left: 0;
    width: 100%;
    z-index: 1000; /* Stays at top of viewport */
}

/* Sticky positioning */
.sticky-nav {
    position: sticky;
    top: 0; /* Sticks to top when scrolling past */
    background-color: white;
    z-index: 100;
}
```

**📝 Deeper Insight**

Absolute and fixed elements are removed from normal flow. Sticky elements remain in flow until they reach their threshold, then behave like fixed. Z-index only works on positioned elements.

---

### 28. 🟡 What is z-index, and how does stacking context work?

**🧠 Concept**

Z-index controls the stacking order of positioned elements. Stacking context is created by positioned elements, opacity, transforms, and other properties, creating isolated stacking layers.

**💻 Example**


```css
/* Basic z-index */
.modal {
    position: fixed;
    z-index: 1000; /* Higher values appear on top */
}

.overlay {
    position: fixed;
    z-index: 999; /* Behind modal */
}

/* Stacking context example */
.parent {
    position: relative;
    z-index: 1; /* Creates new stacking context */
}

.child {
    position: absolute;
    z-index: 10; /* Only competes within parent's context */
}

/* Properties that create stacking context */
.stacking-context {
    position: relative;
    z-index: 0; /* Creates context */
    opacity: 0.99; /* Creates context */
    transform: translateZ(0); /* Creates context */
}
```

**📝 Deeper Insight**

Z-index only works on positioned elements. Each stacking context is isolated - a child with high z-index cannot escape its parent's context. Understanding stacking contexts is crucial for complex layouts.

---

### 29. 🟡 What are pseudo-classes (:hover, :focus) and pseudo-elements (::before, ::after)?

**🧠 Concept**

Pseudo-classes target element states (hover, focus, first-child), while pseudo-elements create virtual elements (::before, ::after) for styling without additional HTML.

**💻 Example**


```css
/* Pseudo-classes */
.button:hover {
    background-color: #0056b3;
    transform: translateY(-2px);
}

.input:focus {
    outline: 2px solid blue;
    box-shadow: 0 0 5px rgba(0, 123, 255, 0.5);
}

.list-item:first-child {
    font-weight: bold;
}

.list-item:nth-child(even) {
    background-color: #f8f9fa;
}

/* Pseudo-elements */
.quote::before {
    content: '"';
    font-size: 2em;
    color: #ccc;
}

.quote::after {
    content: '"';
    font-size: 2em;
    color: #ccc;
}

.tooltip::after {
    content: attr(data-tooltip);
    position: absolute;
    background: #333;
    color: white;
    padding: 5px;
    border-radius: 3px;
}
```

**📝 Deeper Insight**

Pseudo-elements require the `content` property to be visible. They're commonly used for decorative elements, icons, and tooltips without cluttering HTML. Pseudo-classes enable interactive states and structural selection.

---

### 30. 🟡 What are CSS combinators (>, +, ~, space)?

**🧠 Concept**

CSS combinators define relationships between selectors: descendant (space), child (>), adjacent sibling (+), and general sibling (~).

**💻 Example**


```css
/* Descendant selector (space) */
.container p {
    color: blue; /* All p elements inside .container */
}

/* Child selector (>) */
.container > p {
    font-weight: bold; /* Direct children only */
}

/* Adjacent sibling (+) */
h2 + p {
    margin-top: 0; /* p immediately after h2 */
}

/* General sibling (~) */
h2 ~ p {
    color: gray; /* All p elements after h2 at same level */
}

/* Complex combinations */
.nav > li:hover > a {
    color: red; /* a inside li that's hovered inside .nav */
}

.form-group input:focus + label {
    color: blue; /* label immediately after focused input */
}
```

**📝 Deeper Insight**

Combinators create specific targeting without adding classes. Child selector (>) is more performant than descendant selector. Adjacent sibling (+) is useful for form styling and layout adjustments.

---

### 31. 🟡 How do CSS media queries work?

**🧠 Concept**

Media queries apply styles based on device characteristics like screen size, resolution, orientation, and user preferences, enabling responsive design.

**💻 Example**


```css
/* Basic responsive breakpoints */
.container {
    width: 100%;
    padding: 20px;
}

/* Mobile first approach */
@media (min-width: 768px) {
    .container {
        max-width: 750px;
        margin: 0 auto;
    }
}

@media (min-width: 992px) {
    .container {
        max-width: 970px;
    }
}

@media (min-width: 1200px) {
    .container {
        max-width: 1170px;
    }
}

/* Complex media queries */
@media (min-width: 768px) and (max-width: 1024px) {
    .sidebar {
        display: none;
    }
}

@media (orientation: landscape) {
    .hero {
        height: 100vh;
    }
}

@media (prefers-reduced-motion: reduce) {
    * {
        animation-duration: 0.01ms !important;
        transition-duration: 0.01ms !important;
    }
}
```

**📝 Deeper Insight**

Mobile-first approach is preferred as it's more performant and easier to maintain. Media queries can target device capabilities, user preferences, and print styles, not just screen sizes.

---

### 32. 🟡 What is the difference between responsive and adaptive design?

**🧠 Concept**

Responsive design uses fluid layouts that adapt to any screen size, while adaptive design uses fixed layouts for specific breakpoints.

**💻 Example**


```css
/* Responsive Design - Fluid */
.responsive-container {
    width: 100%;
    max-width: 1200px;
    margin: 0 auto;
    padding: 0 20px;
}

.responsive-grid {
    display: grid;
    grid-template-columns: repeat(auto-fit, minmax(300px, 1fr));
    gap: 20px;
}

/* Adaptive Design - Fixed breakpoints */
.adaptive-container {
    width: 100%;
}

@media (max-width: 767px) {
    .adaptive-container { width: 100%; }
}

@media (min-width: 768px) and (max-width: 1023px) {
    .adaptive-container { width: 750px; }
}

@media (min-width: 1024px) {
    .adaptive-container { width: 970px; }
}
```

**📝 Deeper Insight**

Responsive design is more flexible and future-proof, while adaptive design offers more control over specific layouts. Modern web development typically combines both approaches.

---

### 33. 🟡 What is Flexbox, and how does it differ from Grid?

**🧠 Concept**

Flexbox is a one-dimensional layout method for arranging items in rows or columns, while CSS Grid is a two-dimensional system for complex layouts.

**💻 Example**


```css
/* Flexbox - One dimensional */
.flex-container {
    display: flex;
    flex-direction: row; /* or column */
    justify-content: space-between; /* Main axis */
    align-items: center; /* Cross axis */
    flex-wrap: wrap;
}

.flex-item {
    flex: 1; /* Grow to fill space */
    flex: 0 0 200px; /* Don't grow, don't shrink, 200px base */
}

/* CSS Grid - Two dimensional */
.grid-container {
    display: grid;
    grid-template-columns: 1fr 2fr 1fr; /* 3 columns */
    grid-template-rows: auto 1fr auto; /* 3 rows */
    gap: 20px;
    grid-template-areas: 
        "header header header"
        "sidebar main aside"
        "footer footer footer";
}

.header { grid-area: header; }
.sidebar { grid-area: sidebar; }
.main { grid-area: main; }
```

**📝 Deeper Insight**

Use Flexbox for component-level layouts (navigation, cards) and Grid for page-level layouts. They work well together - Grid for overall structure, Flexbox for content within grid areas.

---

### 34. 🟡 What is justify-content and align-items in Flexbox?

**🧠 Concept**

`justify-content` controls alignment along the main axis, while `align-items` controls alignment along the cross axis in Flexbox.

**💻 Example**


```css
.flex-container {
    display: flex;
    height: 300px;
    border: 2px solid #ccc;
}

/* Main axis alignment (justify-content) */
.justify-start { justify-content: flex-start; } /* Default */
.justify-center { justify-content: center; }
.justify-end { justify-content: flex-end; }
.justify-between { justify-content: space-between; }
.justify-around { justify-content: space-around; }
.justify-evenly { justify-content: space-evenly; }

/* Cross axis alignment (align-items) */
.align-start { align-items: flex-start; }
.align-center { align-items: center; }
.align-end { align-items: flex-end; }
.align-stretch { align-items: stretch; } /* Default */
.align-baseline { align-items: baseline; }

/* Individual item alignment */
.flex-item {
    align-self: center; /* Override align-items for this item */
}
```

**📝 Deeper Insight**

The main axis is determined by `flex-direction` (row = horizontal, column = vertical). Cross axis is perpendicular to main axis. These properties work together to create precise layouts.

---

### 35. 🟡 How do you create a two-column layout using Flexbox?

**🧠 Concept**

Flexbox two-column layouts use `flex` properties to control column widths and `flex-direction` to arrange content.

**💻 Example**


```css
/* Two-column layout with Flexbox */
.two-column {
    display: flex;
    gap: 20px;
    min-height: 400px;
}

.sidebar {
    flex: 0 0 250px; /* Fixed width sidebar */
    background-color: #f8f9fa;
    padding: 20px;
}

.main-content {
    flex: 1; /* Takes remaining space */
    background-color: white;
    padding: 20px;
}

/* Responsive two-column */
@media (max-width: 768px) {
    .two-column {
        flex-direction: column;
    }
    
    .sidebar {
        flex: none;
        order: 2; /* Move sidebar below content */
    }
}

/* Equal width columns */
.equal-columns {
    display: flex;
}

.equal-columns > * {
    flex: 1; /* Equal width */
}
```

**📝 Deeper Insight**

Flexbox excels at two-column layouts with its automatic space distribution. Use `flex: 1` for equal columns, `flex: 0 0 width` for fixed-width columns, and `flex-direction: column` for mobile responsiveness.

---

### 36. 🟡 What are CSS Grid rows, columns, and areas?

**🧠 Concept**

CSS Grid uses rows, columns, and named areas to create complex two-dimensional layouts with precise control over item placement.

**💻 Example**


```css
/* Grid with explicit rows and columns */
.grid-layout {
    display: grid;
    grid-template-columns: 200px 1fr 200px; /* 3 columns */
    grid-template-rows: 80px 1fr 60px; /* 3 rows */
    gap: 20px;
    height: 100vh;
}

/* Named grid areas */
.grid-areas {
    display: grid;
    grid-template-areas: 
        "header header header"
        "sidebar main aside"
        "footer footer footer";
    grid-template-columns: 200px 1fr 200px;
    grid-template-rows: 80px 1fr 60px;
    gap: 20px;
}

.header { grid-area: header; }
.sidebar { grid-area: sidebar; }
.main { grid-area: main; }
.aside { grid-area: aside; }
.footer { grid-area: footer; }

/* Responsive grid areas */
@media (max-width: 768px) {
    .grid-areas {
        grid-template-areas: 
            "header"
            "main"
            "sidebar"
            "aside"
            "footer";
        grid-template-columns: 1fr;
    }
}
```

**📝 Deeper Insight**

Grid areas make layouts more semantic and easier to maintain. The `fr` unit represents fractional space, making responsive grids more intuitive than percentage-based layouts.

---

### 37. 🟡 What is the fr unit in CSS Grid?

**🧠 Concept**

The `fr` (fractional) unit represents a fraction of available space in CSS Grid, making it easier to create flexible layouts.

**💻 Example**


```css
/* Fractional units */
.grid {
    display: grid;
    grid-template-columns: 1fr 2fr 1fr; /* 1:2:1 ratio */
    gap: 20px;
}

/* Mixed units */
.mixed-grid {
    display: grid;
    grid-template-columns: 200px 1fr 100px; /* Fixed, flexible, fixed */
}

/* Auto and fr */
.auto-fr {
    display: grid;
    grid-template-columns: auto 1fr auto; /* Content, flexible, content */
}

/* Multiple fr units */
.complex-grid {
    display: grid;
    grid-template-columns: 1fr 2fr 1fr 3fr; /* 1:2:1:3 ratio */
    grid-template-rows: 1fr 2fr; /* 1:2 ratio for rows */
}
```

**📝 Deeper Insight**

`fr` units distribute available space after fixed units are calculated. They're more intuitive than percentages for grid layouts and automatically handle gaps. `1fr` is equivalent to `1fr 1fr` when there are multiple equal fractions.

---

### 38. 🟡 What are CSS variables (--var), and how are they scoped?

**🧠 Concept**

CSS custom properties (variables) allow reusable values throughout stylesheets, with scoping based on the cascade and inheritance.

**💻 Example**


```css
/* Global variables (root scope) */
:root {
    --primary-color: #007bff;
    --secondary-color: #6c757d;
    --font-size-base: 16px;
    --spacing-unit: 8px;
}

/* Using variables */
.button {
    background-color: var(--primary-color);
    padding: var(--spacing-unit) calc(var(--spacing-unit) * 2);
    font-size: var(--font-size-base);
}

/* Scoped variables */
.card {
    --card-bg: #ffffff;
    --card-shadow: 0 2px 4px rgba(0,0,0,0.1);
    background: var(--card-bg);
    box-shadow: var(--card-shadow);
}

.card.dark {
    --card-bg: #333333;
    --card-shadow: 0 2px 4px rgba(255,255,255,0.1);
}

/* Fallback values */
.text {
    color: var(--text-color, #333333); /* Fallback to #333333 */
}
```

**📝 Deeper Insight**

CSS variables are inherited and can be overridden by more specific selectors. They enable theming, dynamic styling with JavaScript, and better maintainability. Variables are computed at runtime, allowing for dynamic changes.

---

### 39. 🟡 How do CSS transitions work?

**🧠 Concept**

CSS transitions smoothly animate property changes over time, providing better user experience for interactive elements.

**💻 Example**


```css
/* Basic transition */
.button {
    background-color: #007bff;
    color: white;
    padding: 10px 20px;
    border: none;
    border-radius: 4px;
    transition: background-color 0.3s ease;
}

.button:hover {
    background-color: #0056b3;
}

/* Multiple properties */
.card {
    transform: scale(1);
    opacity: 1;
    transition: transform 0.3s ease, opacity 0.3s ease;
}

.card:hover {
    transform: scale(1.05);
    opacity: 0.9;
}

/* Transition shorthand */
.element {
    transition: all 0.3s ease-in-out; /* All properties, 0.3s duration, ease-in-out timing */
}

/* Specific timing functions */
.timing-examples {
    transition: transform 0.5s linear; /* Constant speed */
    transition: transform 0.5s ease-in; /* Slow start */
    transition: transform 0.5s ease-out; /* Slow end */
    transition: transform 0.5s ease-in-out; /* Slow start and end */
}
```

**📝 Deeper Insight**

Transitions only work on animatable properties and require a trigger (hover, focus, class change). Use `transition: all` sparingly as it can impact performance. Transitions enhance perceived performance and provide visual feedback.

---

### 40. 🟡 What is the difference between transitions and keyframe animations?

**🧠 Concept**

Transitions animate between two states, while keyframe animations can have multiple steps and run independently of user interaction.

**💻 Example**


```css
/* Transitions - between two states */
.transition-example {
    background-color: blue;
    transition: background-color 0.3s ease;
}

.transition-example:hover {
    background-color: red;
}

/* Keyframe animations - multiple steps */
@keyframes slideIn {
    0% {
        transform: translateX(-100%);
        opacity: 0;
    }
    50% {
        transform: translateX(0);
        opacity: 0.5;
    }
    100% {
        transform: translateX(0);
        opacity: 1;
    }
}

.animation-example {
    animation: slideIn 1s ease-in-out;
}

/* Animation properties */
.animated-element {
    animation-name: slideIn;
    animation-duration: 1s;
    animation-timing-function: ease-in-out;
    animation-delay: 0.5s;
    animation-iteration-count: 3; /* or infinite */
    animation-direction: alternate;
    animation-fill-mode: forwards; /* Keep final state */
}
```

**📝 Deeper Insight**

Use transitions for simple state changes (hover, focus) and keyframe animations for complex sequences. Animations can run automatically and loop, while transitions require a trigger. Both can be paused with `animation-play-state: paused`.
