# 1) Beginner Level CSS (Q1–20)

---

## 1) What is CSS and what does it stand for?

Concept:
CSS (Cascading Style Sheets) is a stylesheet language used to describe the presentation and styling of HTML documents.

Example:
```css
body {
  font-family: Arial, sans-serif;
  background-color: #f0f0f0;
  margin: 0;
  padding: 20px;
}
```

Deep Insight:
- Separates content (HTML) from presentation (CSS)
- Enables consistent styling across multiple pages
- Supports responsive design and animations
- Works with HTML, XML, and other markup languages
- Essential for modern web development

---

## 2) What are the different ways to include CSS in a webpage (inline, internal, external)?

Concept:
CSS can be included via inline styles, internal stylesheets, or external stylesheet files.

Example:
```html
<!-- Inline CSS -->
<p style="color: red; font-size: 16px;">Inline styling</p>

<!-- Internal CSS -->
<head>
  <style>
    body { background-color: #f0f0f0; }
  </style>
</head>

<!-- External CSS -->
<link rel="stylesheet" href="styles.css">
```

Deep Insight:
- Inline: Highest specificity, hard to maintain
- Internal: Page-specific styles, medium maintainability
- External: Best for reusability and caching
- External CSS can be cached by browsers
- Use external CSS for production websites

---

## 3) What are CSS selectors? Give examples.

Concept:
CSS selectors target HTML elements to apply styles, using various patterns to match elements.

Example:
```css
/* Element selector */
p { color: blue; }

/* Class selector */
.highlight { background-color: yellow; }

/* ID selector */
#header { font-size: 24px; }

/* Descendant selector */
div p { margin: 10px; }
```

Deep Insight:
- Selectors determine which elements get styled
- More specific selectors override less specific ones
- Combine selectors for precise targeting
- Use classes for reusable styles
- IDs should be unique per page

---

## 4) What is the difference between element, class, and ID selectors?

Concept:
Element selectors target HTML tags, class selectors target elements with specific class attributes, and ID selectors target unique elements.

Example:
```css
/* Element selector - targets all <p> tags */
p { color: black; }

/* Class selector - targets elements with class="highlight" */
.highlight { background-color: yellow; }

/* ID selector - targets element with id="header" */
#header { font-size: 24px; }
```

Deep Insight:
- Element: Broad targeting, affects all matching tags
- Class: Reusable, can apply to multiple elements
- ID: Unique, highest specificity, one per page
- Specificity order: ID > Class > Element
- Use classes for styling, IDs for JavaScript targeting

---

## 5) What is the CSS Box Model and what are its components?

Concept:
The CSS Box Model describes how elements are rendered with content, padding, border, and margin areas.

Example:
```css
.box {
  width: 200px;        /* Content width */
  height: 100px;       /* Content height */
  padding: 20px;       /* Space inside border */
  border: 2px solid black; /* Border around padding */
  margin: 10px;        /* Space outside border */
}
```

Deep Insight:
- Content: The actual content (text, images)
- Padding: Space between content and border
- Border: Line around the padding
- Margin: Space outside the border
- Total width = content + padding + border + margin

---

## 6) What is the difference between margin and padding?

Concept:
Margin creates space outside an element's border; padding creates space inside an element's border.

Example:
```css
.element {
  padding: 20px;    /* Space inside the element */
  margin: 10px;     /* Space outside the element */
  border: 1px solid black;
  background-color: lightgray;
}
```

Deep Insight:
- Padding: Inside space, affects background color
- Margin: Outside space, transparent, can collapse
- Padding increases element size
- Margin doesn't affect element size
- Use padding for internal spacing, margin for external spacing

---

## 7) What is the purpose of the `box-sizing` property?

Concept:
`box-sizing` controls how the total width and height of an element is calculated, including or excluding padding and borders.

Example:
```css
/* Default behavior */
.default {
  width: 200px;
  padding: 20px;
  border: 2px solid black;
  /* Total width = 200px + 40px padding + 4px border = 244px */
}

/* Border-box behavior */
.border-box {
  width: 200px;
  padding: 20px;
  border: 2px solid black;
  box-sizing: border-box;
  /* Total width = 200px (includes padding and border) */
}
```

Deep Insight:
- `content-box`: Default, width/height = content only
- `border-box`: Width/height includes padding and border
- Border-box makes layouts more predictable
- Use `* { box-sizing: border-box; }` for consistent behavior
- Modern CSS frameworks use border-box by default

---

## 8) What is the difference between `display: block`, `inline`, and `inline-block`?

Concept:
These display values control how elements flow and interact with other elements on the page.

Example:
```css
.block {
  display: block;        /* Takes full width, new line */
  background-color: red;
  margin: 10px 0;
}

.inline {
  display: inline;       /* Flows with text, ignores width/height */
  background-color: blue;
}

.inline-block {
  display: inline-block; /* Flows like inline but respects all properties */
  width: 100px;
  background-color: green;
}
```

Deep Insight:
- Block: Full width, starts new line, respects all properties
- Inline: Flows with text, ignores width/height, only horizontal margins
- Inline-block: Best of both - flows like inline but respects all properties
- Use block for major layout elements
- Use inline-block for buttons and form elements

---

## 9) What are pseudo-classes and pseudo-elements? Give examples.

Concept:
Pseudo-classes target element states; pseudo-elements create virtual elements that don't exist in HTML.

Example:
```css
/* Pseudo-classes - element states */
a:hover { color: red; }           /* When hovering */
input:focus { border-color: blue; } /* When focused */
li:first-child { font-weight: bold; } /* First child */

/* Pseudo-elements - virtual elements */
p::before { content: "→ "; }      /* Adds arrow before paragraph */
p::after { content: " ←"; }       /* Adds arrow after paragraph */
```

Deep Insight:
- Pseudo-classes: `:hover`, `:focus`, `:nth-child()`
- Pseudo-elements: `::before`, `::after`, `::first-line`
- Pseudo-elements need `content` property to appear
- Use single `:` for pseudo-classes, double `::` for pseudo-elements
- Great for adding decorative elements without HTML

---

## 10) What is the difference between `:hover` and `::before`?

Concept:
`:hover` is a pseudo-class that targets an element's hover state; `::before` is a pseudo-element that creates content before an element.

Example:
```css
/* :hover - pseudo-class for hover state */
.button:hover {
  background-color: blue;
  transform: scale(1.1);
}

/* ::before - pseudo-element creates content */
.button::before {
  content: "★ ";
  color: gold;
}
```

Deep Insight:
- `:hover`: Targets existing element in hover state
- `::before`: Creates new virtual element before content
- Pseudo-classes use single colon `:`
- Pseudo-elements use double colon `::`
- `::before` requires `content` property to be visible

---

## 11) What is CSS specificity and how is it calculated?

Concept:
CSS specificity determines which styles apply when multiple rules target the same element, calculated using a point system.

Example:
```css
/* Specificity: 0,0,0,1 (element) */
p { color: black; }

/* Specificity: 0,0,1,0 (class) */
.highlight { color: yellow; }

/* Specificity: 0,0,1,1 (class + element) */
p.highlight { color: red; }

/* Specificity: 0,1,0,0 (ID) */
#title { color: blue; }
```

Deep Insight:
- Calculation: Inline styles (1000), IDs (100), Classes (10), Elements (1)
- Higher specificity wins
- `!important` overrides specificity
- Avoid high specificity for maintainability
- Use specificity calculator tools for complex cases

---

## 12) What are relative and absolute CSS units (`px`, `%`, `em`, `rem`, `vh`, `vw`)?

Concept:
CSS units define measurement values, with absolute units being fixed and relative units scaling based on other values.

Example:
```css
.container {
  width: 800px;        /* Absolute - fixed pixels */
  height: 50vh;        /* Relative - 50% of viewport height */
  font-size: 16px;     /* Absolute - fixed font size */
}

```

Deep Insight:
- Absolute: `px` - fixed size regardless of context
- Relative: `%`, `em`, `rem`, `vh`, `vw` - scale with context
- `em`: Relative to parent font size
- `rem`: Relative to root font size
- `vh`/`vw`: Relative to viewport dimensions
- Use relative units for responsive design

---

## 13) What is the difference between `position: relative`, `absolute`, `fixed`, and `sticky`?

Concept:
These position values control how elements are positioned relative to their normal flow and other elements.

Example:
```css
.relative {
  position: relative;  /* Positioned relative to normal position */
  top: 10px;
  left: 20px;
}

.absolute {
  position: absolute;  /* Removed from flow, positioned relative to parent */
  top: 50px;
  right: 10px;
}

.fixed {
  position: fixed;     /* Always relative to viewport */
  bottom: 20px;
  right: 20px;
}
```

Deep Insight:
- Relative: Moves from normal position, others flow around it
- Absolute: Removed from flow, positioned relative to positioned parent
- Fixed: Always relative to viewport, stays in place when scrolling
- Sticky: Acts like relative until scroll threshold, then like fixed
- Use `top`, `right`, `bottom`, `left` to position

---

## 14) What is the difference between `visibility: hidden` and `display: none`?

Concept:
`visibility: hidden` hides elements but preserves their space; `display: none` removes elements completely from the layout.

Example:
```css
.hidden-visibility {
  visibility: hidden;  /* Hidden but takes up space */
  /* Element is invisible but still affects layout */
}

.hidden-display {
  display: none;       /* Completely removed from layout */
  /* Element is invisible and doesn't take up space */
}
```

Deep Insight:
- `visibility: hidden`: Element invisible but space preserved
- `display: none`: Element completely removed from layout
- `visibility: hidden` can be animated
- `display: none` cannot be animated
- Use `visibility` for toggling without layout shift

---

## 15) What is `z-index` and how does stacking context work?

Concept:
`z-index` controls the stacking order of positioned elements, with higher values appearing on top.

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
  /* This will appear on top of layer1 */
}
```

Deep Insight:
- Only works on positioned elements (relative, absolute, fixed)
- Higher z-index values appear on top
- Creates stacking contexts
- Negative z-index values are allowed
- Use sparingly to avoid z-index wars

---

## 16) What is the default positioning value for HTML elements?

Concept:
The default positioning value for HTML elements is `static`, which follows the normal document flow.

Example:
```css
/* Default positioning - no need to specify */
.element {
  position: static;  /* This is the default */
  /* Element flows normally in document */
}

```

Deep Insight:
- `static` is the default positioning
- Static elements ignore `top`, `right`, `bottom`, `left`
- Static elements follow normal document flow
- Other positioning values create new stacking contexts
- Most elements use static positioning by default

---

## 17) What is inheritance in CSS and which properties are inheritable?

Concept:
Inheritance allows child elements to inherit certain CSS properties from their parent elements.

Example:
```css
.parent {
  color: blue;           /* Inherited by children */
  font-family: Arial;    /* Inherited by children */
  font-size: 16px;       /* Inherited by children */
  background-color: red; /* NOT inherited */
  border: 1px solid black; /* NOT inherited */
```

Deep Insight:
- Text properties: `color`, `font-family`, `font-size`, `line-height`
- List properties: `list-style-type`, `list-style-position`
- Table properties: `border-collapse`, `border-spacing`
- Non-inherited: `background`, `border`, `margin`, `padding`, `width`, `height`
- Use `inherit` keyword to force inheritance

---

## 18) What are vendor prefixes and why are they used?

Concept:
Vendor prefixes are browser-specific prefixes added to CSS properties during experimental or early implementation phases.

Example:
```css
.animation {
  /* Webkit browsers (Chrome, Safari) */
  -webkit-transform: rotate(45deg);
  -webkit-transition: transform 0.3s ease;
  
  /* Mozilla browsers (Firefox) */
  -moz-transform: rotate(45deg);
  -moz-transition: transform 0.3s ease;
  
  /* Standard property (always last) */
  transform: rotate(45deg);
  transition: transform 0.3s ease;
}
```

Deep Insight:
- `-webkit-`: Chrome, Safari, newer Edge
- `-moz-`: Firefox
- `-ms-`: Internet Explorer, older Edge
- `-o-`: Opera (legacy)
- Always include standard property last
- Use autoprefixer tools for automatic prefixing

---

## 19) What are shorthand properties in CSS?

Concept:
Shorthand properties allow setting multiple related CSS properties in a single declaration.

Example:
```css
/* Long form */
.element {
  margin-top: 10px;
  margin-right: 20px;
  margin-bottom: 10px;
  margin-left: 20px;
}

/* Shorthand form */
.element {
  margin: 10px 20px;  /* top/bottom: 10px, left/right: 20px */
}
```

Deep Insight:
- Reduces code size and improves readability
- Common shorthands: `margin`, `padding`, `border`, `background`
- Order matters in shorthand properties
- Can mix shorthand and longhand properties
- Use shorthand for efficiency, longhand for clarity

---

## 20) How can you apply multiple classes to a single HTML element?

Concept:
HTML elements can have multiple class names separated by spaces, allowing combination of different styles.

Example:
```html
<!-- HTML with multiple classes -->
<button class="btn btn-primary btn-large">Click me</button>
<div class="card featured highlighted">Content</div>

<!-- CSS for multiple classes -->
.btn { padding: 10px; }
.btn-primary { background-color: blue; }
.btn-large { font-size: 18px; }
```

Deep Insight:
- Separate class names with spaces
- All classes apply to the element
- Order of classes doesn't matter
- Later classes can override earlier ones
- Great for modular CSS architecture
