# 🎯 2. Intermediate Level CSS (Q14–33)

---

## 🧩 Q14. What is the difference between `visibility: hidden` and `display: none`?

### 🧠 Concept

`visibility: hidden` hides elements but preserves their space. `display: none` removes elements completely from the layout. Visibility preserves space, display removes from layout.

---

### 💡 Example

```css
.hidden-visibility { visibility: hidden; }
.hidden-display { display: none; }
```

---

### 🔍 Deep Insights

* **Rule:** `visibility: hidden` (element invisible but space preserved), `display: none` (element completely removed from layout).
* **Use Case:** `visibility: hidden` can be animated, `display: none` cannot be animated.
* **Common Mistake:** Not understanding when to use each, causing layout shifts.
* **Pro Tip:** Use `visibility` for toggling without layout shift.

---

### ⭐ Senior Takeaway

Visibility preserves space, display removes from layout.

---

## 🧩 Q15. What is `z-index` and how does stacking context work?

### 🧠 Concept

`z-index` controls the stacking order of positioned elements, with higher values appearing on top. z-index only works on positioned elements.

---

### 💡 Example

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

### 🔍 Deep Insights

* **Rule:** Only works on positioned elements (relative, absolute, fixed), higher z-index values appear on top.
* **Use Case:** Creates stacking contexts, negative z-index values are allowed.
* **Common Mistake:** Using z-index on non-positioned elements (doesn't work), z-index wars.
* **Pro Tip:** Use sparingly to avoid z-index wars, understand stacking contexts.

---

### ⭐ Senior Takeaway

z-index only works on positioned elements.

---

## 🧩 Q16. What is the default positioning value for HTML elements?

### 🧠 Concept

The default positioning value for HTML elements is `static`, which follows the normal document flow. Static positioning is the default, follows normal flow.

---

### 💡 Example

```css
.element { position: static; }
.box { 
  width: 200px; 
  height: 100px; 
  background-color: blue; 
}
```

---

### 🔍 Deep Insights

* **Rule:** `static` is the default positioning, static elements follow normal document flow.
* **Use Case:** Static elements ignore `top`, `right`, `bottom`, `left` properties.
* **Common Mistake:** Not understanding that static is default, other positioning values create new stacking contexts.
* **Pro Tip:** Most elements use static positioning by default.

---

### ⭐ Senior Takeaway

Static positioning is the default, follows normal flow.

---

## 🧩 Q17. What is inheritance in CSS and which properties are inheritable?

### 🧠 Concept

Inheritance means child elements automatically get some properties from their parents, like font-family or color. Inherited properties are more efficient than explicitly setting them on every element.

---

### 💡 Example

```css
body {
  font-family: 'Arial', sans-serif;
  font-size: 16px;
  line-height: 1.5;
  color: #333;
}
```

---

### 🔍 Deep Insights

* **Rule:** Inherited properties include `font-family`, `font-size`, `color`, `line-height`, `text-align`, `visibility`.
* **Use Case:** Non-inherited properties include `width`, `height`, `margin`, `padding`, `border`, `background`.
* **Common Mistake:** Properties cascade down through the DOM tree from parent to child.
* **Pro Tip:** Child elements can override inherited properties with their own values.

---

### ⭐ Senior Takeaway

Inherited properties are more efficient than explicitly setting them on every element.

---

## 🧩 Q18. What are vendor prefixes and why are they used?

### 🧠 Concept

Vendor prefixes are browser-specific prefixes added to CSS properties during experimental or early implementation phases. Vendor prefixes are for experimental features, standard property comes last.

---

### 💡 Example

```css
.animation {
  -webkit-transform: rotate(45deg);
  -moz-transform: rotate(45deg);
  transform: rotate(45deg);
}
```

---

### 🔍 Deep Insights

* **Rule:** `-webkit-` (Chrome, Safari, newer Edge), `-moz-` (Firefox), `-ms-` (Internet Explorer, older Edge), `-o-` (Opera, legacy).
* **Use Case:** Always include standard property last, use autoprefixer tools for automatic prefixing.
* **Common Mistake:** Not including standard property, forgetting prefixes.
* **Pro Tip:** Use build tools like autoprefixer to handle prefixes automatically.

---

### ⭐ Senior Takeaway

Vendor prefixes are for experimental features, standard property comes last.

---

## 🧩 Q19. What are shorthand properties in CSS?

### 🧠 Concept

Shorthand properties allow setting multiple related CSS properties in a single declaration. Shorthand properties are more efficient but order matters.

---

### 💡 Example

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

### 🔍 Deep Insights

* **Rule:** Reduces code size and improves readability, common shorthands: `margin`, `padding`, `border`, `background`.
* **Use Case:** Order matters in shorthand properties, can mix shorthand and longhand properties.
* **Common Mistake:** Not understanding shorthand order (top, right, bottom, left).
* **Pro Tip:** Use shorthand for efficiency, longhand for clarity.

---

### ⭐ Senior Takeaway

Shorthand properties are more efficient but order matters.

---

## 🧩 Q20. How do you apply multiple classes to an element?

### 🧠 Concept

Separate multiple class names with spaces in the HTML class attribute. Each class applies its styles independently, and specificity combines.

---

### 💡 Example

```html
<div class="button primary large">Click me</div>
```

```css
.button { padding: 10px; }
.primary { background-color: blue; }
.large { font-size: 18px; }
```

---

### 🔍 Deep Insights

* **Rule:** Multiple classes combine their styles, order in HTML doesn't affect CSS.
* **Use Case:** Use multiple classes for modular, reusable styling patterns.
* **Common Mistake:** CSS specificity is based on selector, not class order.
* **Pro Tip:** Combine utility classes for flexible, maintainable styling.

---

### ⭐ Senior Takeaway

Multiple classes enable modular, reusable styling patterns.

---

## 🧩 Q21. What is CSS Flexbox and how does it work?

### 🧠 Concept

Flexbox helps you lay out items in one direction (row or column) with flexible sizing and easy alignment. Use it when you need to distribute space or center content.

---

### 💡 Example

```css
.container {
  display: flex;
  justify-content: space-between;
  align-items: center;
  flex-wrap: wrap;
}
```

---

### 🔍 Deep Insights

* **Rule:** Flexbox works on two axes—main (flex-direction) and cross (perpendicular).
* **Use Case:** `flex` is shorthand for `flex-grow`, `flex-shrink`, and `flex-basis`.
* **Common Mistake:** `justify-content` controls main axis, `align-items` controls cross axis.
* **Pro Tip:** `order` property allows visual reordering without changing HTML structure.

---

### ⭐ Senior Takeaway

Flexbox simplifies one-dimensional layouts and alignment.

---

## 🧩 Q22. Explain CSS Grid and its key features.

### 🧠 Concept

Grid lets you create layouts with both rows and columns at once, giving you precise control over where items go. Perfect for complex page layouts.

---

### 💡 Example

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

### 🔍 Deep Insights

* **Rule:** Unlike Flexbox, Grid handles both rows and columns simultaneously.
* **Use Case:** Named grid areas make complex layouts more readable and maintainable.
* **Common Mistake:** `fr` units distribute available space proportionally.
* **Pro Tip:** Grid can create implicit rows/columns when content exceeds defined tracks.

---

### ⭐ Senior Takeaway

Grid is perfect for complex two-dimensional layouts.

---

## 🧩 Q23. What is the difference between Flexbox and Grid?

### 🧠 Concept

Grid handles 2D layouts (both rows and columns), while Flexbox handles 1D (row OR column). Use Grid for page structure and Flexbox for components.

---

### 💡 Example

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

### 🔍 Deep Insights

* **Rule:** Grid for page layouts and complex two-dimensional arrangements, Flexbox for component layouts and navigation bars.
* **Use Case:** Use Grid for overall structure, Flexbox for component internals—they complement each other.
* **Common Mistake:** Trying to use one for everything instead of combining both.
* **Pro Tip:** Both have excellent modern browser support, Grid is newer.

---

### ⭐ Senior Takeaway

Flexbox is simpler to learn, Grid is more powerful but complex.

---

## 🧩 Q24. What are CSS transitions and how do you use them?

### 🧠 Concept

Transitions make property changes smooth over time instead of instant. Great for hover effects and user feedback. Different properties can have different durations and timing functions.

---

### 💡 Example

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

### 🔍 Deep Insights

* **Rule:** Can target specific properties or use `all` for multiple properties.
* **Use Case:** Timing functions (`ease`, `linear`, `ease-in-out`) control animation curve.
* **Common Mistake:** GPU-accelerated properties (transform, opacity) perform better than layout properties.
* **Pro Tip:** JavaScript can listen to `transitionend` events for completion callbacks.

---

### ⭐ Senior Takeaway

Transitions provide smooth property changes over time.

---

## 🧩 Q25. What are CSS animations and how do you create them?

### 🧠 Concept

Animations let you create complex, multi-step effects using @keyframes to define what happens at different points. Use them for loading spinners or page entrances.

---

### 💡 Example

```css
@keyframes slideIn {
  0% { transform: translateX(-100%); opacity: 0; }
  100% { transform: translateX(0); opacity: 1; }
}
.element { animation: slideIn 0.5s ease-in-out; }
```

---

### 🔍 Deep Insights

* **Rule:** Multiple keyframes (0%, 25%, 50%, 100%) create complex animation sequences.
* **Use Case:** Animation properties include duration, timing-function, delay, iteration-count, direction, fill-mode.
* **Common Mistake:** `forwards` keeps final state, `backwards` applies initial state before delay.
* **Pro Tip:** Use `transform` and `opacity` for smooth 60fps animations.

---

### ⭐ Senior Takeaway

Animation events allow JavaScript control of animations.

---

## 🧩 Q26. What is the CSS cascade and how does it work?

### 🧠 Concept

The cascade is CSS's priority system—it decides which styles win based on order, specificity, and !important. Later styles override earlier ones when specificity is equal.

---

### 💡 Example

```css
.button { color: red; }
.button { color: blue; }
.button { color: green !important; }
```

---

### 🔍 Deep Insights

* **Rule:** Later styles override earlier ones when specificity is equal (source order).
* **Use Case:** Higher specificity overrides lower specificity.
* **Common Mistake:** `!important` has highest priority but breaks cascade flow.
* **Pro Tip:** Some properties inherit from parent elements automatically.

---

### ⭐ Senior Takeaway

Modern CSS supports `@layer` for explicit cascade control.

---

## 🧩 Q27. What are CSS combinators and how do you use them?

### 🧠 Concept

Combinators let you target elements based on their relationship to other elements—like children, siblings, or descendants. Useful for styling nested structures.

---

### 💡 Example

```css
.container p { color: blue; }
.container > p { font-weight: bold; }
h1 + p { margin-top: 0; }
h2 ~ p { color: gray; }
```

---

### 🔍 Deep Insights

* **Rule:** Descendant (space) targets any descendant, child (>) targets only direct children.
* **Use Case:** Adjacent sibling (+) targets immediately following sibling, general sibling (~) targets all following siblings.
* **Common Mistake:** Child combinators are generally faster than descendant combinators.
* **Pro Tip:** Use combinators to avoid adding unnecessary classes.

---

### ⭐ Senior Takeaway

Combinators help maintain clean HTML structure.

---

## 🧩 Q28. What is the difference between `transition` and `animation`?

### 🧠 Concept

Transitions animate property changes between states. Animations create complex multi-step sequences with @keyframes. Transitions are simpler, animations are more powerful.

---

### 💡 Example

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

### 🔍 Deep Insights

* **Rule:** Transitions need a trigger (hover, focus), animations can run automatically.
* **Use Case:** Use transitions for simple state changes, animations for complex sequences.
* **Common Mistake:** Transitions are simpler, animations offer more control with keyframes.
* **Pro Tip:** Both can be paused, reversed, or controlled with JavaScript.

---

### ⭐ Senior Takeaway

Transitions are simpler, animations offer more control.

---

## 🧩 Q29. How do you create CSS animations using `@keyframes`?

### 🧠 Concept

Use `@keyframes` to define animation steps, then apply with the `animation` property. Keyframes define what happens at different points in the animation.

---

### 💡 Example

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

### 🔍 Deep Insights

* **Rule:** Define keyframes with percentages (0%, 50%, 100%) or keywords (from, to).
* **Use Case:** Animation shorthand: name, duration, timing-function, delay, iteration-count, direction, fill-mode.
* **Common Mistake:** `infinite` makes animation repeat, `alternate` reverses direction.
* **Pro Tip:** Use `fill-mode: forwards` to keep final state after animation ends.

---

### ⭐ Senior Takeaway

@keyframes enable complex, multi-step animations.

---

## 🧩 Q30. What are media queries and how do you use them?

### 🧠 Concept

Media queries let you apply different styles based on device features like screen width. Essential for making websites work on phones, tablets, and desktops.

---

### 💡 Example

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

### 🔍 Deep Insights

* **Rule:** Common breakpoints are 768px (tablet), 1024px (desktop), 1200px (large desktop).
* **Use Case:** Start with mobile styles, then add larger screen styles with `min-width` (mobile-first).
* **Common Mistake:** Logical operators (`and`, `or`, `not`) combine multiple media conditions.
* **Pro Tip:** Media queries don't affect performance, only load appropriate CSS.

---

### ⭐ Senior Takeaway

Media features include width, orientation, prefers-color-scheme.

---

## 🧩 Q31. How do you create responsive text with CSS?

### 🧠 Concept

Use relative units (rem, em), viewport units (vw, vh), or `clamp()` for responsive text that scales with screen size. Responsive text improves readability across devices.

---

### 💡 Example

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

### 🔍 Deep Insights

* **Rule:** `clamp()` sets min, preferred, and max values for fluid scaling.
* **Use Case:** Use rem for consistent scaling, vw for viewport-based sizing.
* **Common Mistake:** Avoid fixed pixel sizes for text, use relative units.
* **Pro Tip:** Combine media queries with relative units for best results.

---

### ⭐ Senior Takeaway

Responsive text improves readability across devices.

---

## 🧩 Q32. What are CSS variables and how do you use them?

### 🧠 Concept

CSS variables let you store values like colors or spacing that you can reuse anywhere and even change with JavaScript. Perfect for theming and maintaining consistent design tokens.

---

### 💡 Example

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

### 🔍 Deep Insights

* **Rule:** Variables inherit and can be overridden at different levels (root, element, pseudo-class).
* **Use Case:** `var(--color, #fallback)` provides fallback when variable is undefined.
* **Common Mistake:** JavaScript can change CSS variables: `element.style.setProperty('--color', 'red')`.
* **Pro Tip:** Variables are computed at runtime, use sparingly for performance-critical properties.

---

### ⭐ Senior Takeaway

CSS variables enable dynamic theming and design tokens.

---

## 🧩 Q33. What is the difference between SASS and LESS?

### 🧠 Concept

SASS and LESS are CSS preprocessors that add features like variables and mixins. SASS uses indentation or SCSS syntax, LESS uses CSS-like syntax. Both compile to CSS.

---

### 💡 Example

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

### 🔍 Deep Insights

* **Rule:** SASS has two syntaxes (indented SASS, SCSS), LESS uses CSS-like syntax.
* **Use Case:** Both support variables, mixins, nesting, and functions.
* **Common Mistake:** SASS is more popular, LESS is easier for CSS developers.
* **Pro Tip:** Choose based on team preference and tooling support.

---

### ⭐ Senior Takeaway

Both preprocessors add power to CSS, choose based on preference.

---
<｜tool▁calls▁begin｜><｜tool▁call▁begin｜>
grep